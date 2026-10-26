#!/usr/bin/env python3
"""Bounded N01 producer/replay harness. Prepared for Edward Baker with LLM
assistance, gpt-6.1-sol, actual effort ultra, 26 October 2026.
Default compute cap900sec includes generation+separate-process replay.
"""
import argparse,hashlib,json,os,platform,subprocess,sys,time
from pathlib import Path

META={'prepared_for':'Edward Baker','date':'2026-10-26','model':'gpt-6.1-sol','effort':'ultra','thread_id':'01a176ea-3f14-7972-bc9c-9aeb6fb50fd4','turn_id':'01a17838-69d0-76c1-82a0-8e808ec78797','request':'HDA-R05-N01 r1'}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def atomic_json(path,data):
    tmp=path.with_name(path.name+'.tmp')
    with tmp.open('w') as f:
        json.dump(data,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())
    os.replace(tmp,path)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--record',type=Path,required=True);ap.add_argument('--budget-state',type=Path,required=True);ap.add_argument('--families',nargs='+',choices=['gamma','gauss'],default=['gamma','gauss']);ap.add_argument('--budget',type=float,default=900);ap.add_argument('--case-seconds',type=float,default=60);o=ap.parse_args()
    assert 0<o.budget<=900 and 0<o.case_seconds<=900
    base=Path(__file__).resolve().parent;o.output_dir.mkdir(parents=True,exist_ok=True)
    state=json.loads(o.budget_state.read_text()) if o.budget_state.exists() else {'elapsed_compute_seconds':0.0,'attempts':[]}
    previous=state['elapsed_compute_seconds'];start=time.perf_counter()
    rec={**META,'python':sys.version,'platform':platform.platform(),'backend':'stdlib Fraction/int','limits':{'total_compute_seconds':o.budget,'per_child_seconds':o.case_seconds,'process_bytes':512*1024*1024,'gauss_depth':8192,'sign_queries':250000,'gamma_terms_plus_shifts':4096,'primitive_fractional_bits':8192,'primitive_series_terms':4096},'prior_compute_seconds':previous,'source_hashes':{},'cases':[]}
    for p in sorted(base.glob('*.py')):
        rec['source_hashes'][p.name]=digest(p)
    def save():
        rec['elapsed_this_attempt_seconds']=time.perf_counter()-start
        rec['total_compute_seconds']=previous+rec['elapsed_this_attempt_seconds']
        atomic_json(o.record,rec)
        state['elapsed_compute_seconds']=rec['total_compute_seconds']
        state.pop('pending_reservation',None)
        atomic_json(o.budget_state,state)
    def child(family,action,path,args):
        remaining=o.budget-previous-(time.perf_counter()-start)
        if remaining<=1:return {'success':False,'reason':'total compute budget exhausted before child'}
        allocation=min(o.case_seconds,remaining-0.5)
        state['elapsed_compute_seconds']=previous+(time.perf_counter()-start)+allocation
        state['pending_reservation']={'family':family,'action':action,'args':args,'seconds':allocation,'reason':'Conservatively charged on interrupted parent; refunded to actual elapsed after completed pair.'}
        atomic_json(o.budget_state,state)
        cmd=[sys.executable,str(base/'n01_worker.py'),family,action,str(path),'--args',json.dumps(args),'--time-seconds',str(allocation)]
        t=time.perf_counter()
        try:
            r=subprocess.run(cmd,capture_output=True,text=True,timeout=allocation,cwd=base)
            if r.returncode!=0:return {'success':False,'reason':'worker failed','exit_code':r.returncode,'stderr':r.stderr[-12000:],'wall_seconds':time.perf_counter()-t}
            x=json.loads(r.stdout,parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))
            assert isinstance(x,dict) and x['success'] is True
            assert x['requested_args']==args
            assert x['provider_sha256']==rec['source_hashes'][family+'_provider.py'], 'provider changed during execution'
            assert x['source_hashes']==rec['source_hashes'], 'source files changed during execution'
            if action=='run': assert path.is_file() and path.stat().st_size>0
            if action=='replay' and not x['delivery_pass']:
                x['success']=False;x['reason']='valid failure/capped certificate; requested delivery not established'
            x['wall_seconds']=time.perf_counter()-t;return x
        except subprocess.TimeoutExpired:return {'success':False,'reason':'child computation time allocation reached','wall_seconds':time.perf_counter()-t}
        except Exception as exc:return {'success':False,'reason':'invalid worker output/certificate: '+repr(exc),'wall_seconds':time.perf_counter()-t}
    jobs=[]
    for P in [32,64,128]:
        if 'gauss' in o.families:
            for s in [1,2,4,8,16]:jobs.append(('gauss',[s,P]))
        if 'gamma' in o.families:
            for J in [0,2,8]:
                for u in [1,32,256,4096]:jobs.append(('gamma',[u,J,P]))
    stopped={}
    for family,args in jobs:
        label=family+'_'+'_'.join(map(str,args));path=o.output_dir/(label+'.json');row={'family':family,'args':args,'label':label,'certificate_file':path.name}
        if family in stopped:
            row.update(status='not_run_after_channel_stop',reason=stopped[family]);rec['cases'].append(row);save();continue
        row['producer']=child(family,'run',path,args)
        if not row['producer']['success']:
            row.update(status='failed_or_inconclusive',reason=row['producer']['reason']);stopped[family]=label+': '+row['reason']
            if path.is_file():
                row['partial_certificate_sha256']=digest(path);row['partial_certificate_bytes']=path.stat().st_size
        else:
            try:
                row['certificate_sha256']=digest(path);row['certificate_bytes']=path.stat().st_size
                row['replay']=child(family,'replay',path,args)
            except Exception as exc:
                row['replay']={'success':False,'reason':'certificate read/hash failure: '+repr(exc)}
            if not row['replay']['success']:
                row.update(status='replay_failed_or_inconclusive',reason=row['replay']['reason']);stopped[family]=label+': '+row['reason']
            else:row['status']='delivered_and_replayed'
        rec['cases'].append(row);save()
        print(json.dumps({'case':label,'status':row['status'],'total_compute_seconds':round(rec['total_compute_seconds'],3)}),flush=True)
    rec['counts']={k:sum(x['status']==k for x in rec['cases']) for k in sorted(set(x['status'] for x in rec['cases']))}
    rec['complete_at_bounded_scope']=True
    state['attempts'].append({'record':o.record.name,'case_count':len(rec['cases'])});save()
    print(json.dumps({'counts':rec['counts'],'total_compute_seconds':rec['total_compute_seconds'],'record':str(o.record)}),flush=True)
if __name__=='__main__':main()
