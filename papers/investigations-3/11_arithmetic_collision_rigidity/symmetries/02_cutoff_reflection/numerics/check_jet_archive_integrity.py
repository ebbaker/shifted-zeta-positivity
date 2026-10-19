#!/usr/bin/env python3
"""Replay S02 table loading and fail-closed integrity guards.
Prepared for Edward Baker, 19 October 2026, substantial LLM assistance.
Authoring gpt-6.1-sol, actual effort ultra; internal verification.
"""
import argparse,gzip,hashlib,importlib.util,json,os,tempfile
from pathlib import Path
from flint import arb,ctx

p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
p.add_argument('--record',type=Path,required=True);p.add_argument('--archive-root',type=Path,required=True)
p.add_argument('--output',type=Path,required=True);a=p.parse_args()
modpath=a.repo/'papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py'
s=importlib.util.spec_from_file_location('s02_archive_checker',modpath);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
data=json.loads(a.record.read_text());ctx.prec=256
os.environ['S02_JET_ARCHIVES']=str(a.archive_root)
checks=[]
for run in data['runs']:
 receipt=run['archive'];count=0;mins={k:arb(1000) for k in ['frozen','full']}
 for row in m.load_cell_archive(a.repo,receipt):
  assert row['cell']==[count//128,count%128]
  for key in mins:
   value=arb(row['methods'][key]['schur_excess_lower']).lower();assert value>0
   mins[key]=min(mins[key],value)
  count+=1
 assert count==4096
 checks.append({'bits':run['bits'],'all_rows_loaded':count,'positive_serialized_Schur_excess':{k:m.out(v) for k,v in mins.items()},'stored_and_canonical_identities_checked':True})
receipt=data['runs'][0]['archive'];failures=[]
def rejection(label,rec,exception):
 exposed=0
 try:
  for row in m.load_cell_archive(a.repo,rec):
   exposed+=1;break
 except exception as exc:
  assert exposed==0
  failures.append({'case':label,'rejected_before_any_row':True,'error':str(exc)})
 else:raise AssertionError('archive guard accepted '+label)
bad=dict(receipt,stored_sha256='0'*64);rejection('wrong stored hash',bad,ArithmeticError)
bad=dict(receipt,canonical_jsonl_content_sha256='0'*64);rejection('wrong canonical mathematical hash',bad,ArithmeticError)
root=m.locate_archive(a.repo,receipt['relative_path'])
with tempfile.TemporaryDirectory(prefix='s02-archive-guards-') as tmp:
 os.environ['S02_JET_ARCHIVES']=tmp
 rejection('missing archive',receipt,FileNotFoundError)
 dst=Path(tmp)/receipt['relative_path'];dst.parent.mkdir(parents=True)
 with gzip.open(root,'rb') as old,dst.open('wb') as raw:
  with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as new:
   header=json.loads(next(old));header['producer_sha256']='0'*64
   new.write(m.canonical_line(header))
   for line in old:new.write(line)
 changed=dict(receipt,stored_sha256=m.digest(dst))
 rejection('stale producer with valid cell content',changed,ArithmeticError)
os.environ['S02_JET_ARCHIVES']=str(a.archive_root)
record={'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker','actual_model':'gpt-6.1-sol','actual_effort':'ultra','llm_assistance':'substantial; internal archive replay','status':'pass','producer_sha256':m.digest(modpath),'summary_sha256':m.digest(a.record),'checker_sha256':m.digest(__file__),'archives':checks,'fail_closed_guards':failures,'scope':'Hash identity, schema/producer/source/order loading, positive stored bounds and missing/corrupted input guards. Mathematical claims depend on the complete evaluator and proof.'}
a.output.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'pass','archives':len(checks),'rows':8192,'rejected_before_data':len(failures)}))
