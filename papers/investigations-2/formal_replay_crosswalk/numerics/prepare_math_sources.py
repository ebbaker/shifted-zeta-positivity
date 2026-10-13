#!/usr/bin/env python3
from pathlib import Path
import argparse, subprocess, json, hashlib, os
PIN='fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb'
p=argparse.ArgumentParser();p.add_argument('--checkout',type=Path,required=True);p.add_argument('--manifest',type=Path,required=True);p.add_argument('--expected-manifest-sha256',required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
def run(argv,cwd=None,input=None):
    return subprocess.check_output(argv,cwd=cwd,input=input,text=True).strip()
b=args.manifest.read_bytes();assert hashlib.sha256(b).hexdigest()==args.expected_manifest_sha256
m=json.loads(b);assert m['expected_commit']==PIN
rows=m['critical_nonmodule_files']+m['modules'];critical_paths=sorted({x['path'] for x in rows});assert len(critical_paths)==2959
paths=sorted(critical_paths+['lean/.gitignore'])
assert all(x.startswith('lean/') and '..' not in x.split('/') for x in paths)
root=args.checkout.expanduser().resolve();assert not root.exists(),'Use a fresh nonexistent checkout path'
root.mkdir(parents=True)
run(['git','init',str(root)]);run(['git','remote','add','origin','https://github.com/openai/math'],root)
run(['git','config','remote.origin.promisor','true'],root)
run(['git','config','remote.origin.partialclonefilter','blob:none'],root)
run(['git','fetch','--depth=1','--filter=blob:none','origin',PIN],root)
run(['git','sparse-checkout','init','--no-cone'],root)
run(['git','sparse-checkout','set','--no-cone','--stdin'],root,input=''.join('/'+x+'\n' for x in paths))
run(['git','checkout','--detach',PIN],root)
assert run(['git','rev-parse','HEAD'],root)==PIN
for r in rows:
    q=root/r['path'];assert q.is_file() and not q.is_symlink(),r['path']
    b=q.read_bytes();assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'],r['path']
assert run(['git','hash-object','lean/.gitignore'],root)=='b4510a3474296d8e4fdb5f5377cfe70234e8185c'
assert not run(['git','status','--porcelain'],root)
record={'status':'critical_sources_materialized_and_verified; proof_not_built','commit':PIN,'checkout':str(root),'critical_files':len(critical_paths),'additional_original_paths':['lean/.gitignore'],'materialized_files':len(paths),'source_bytes':sum(x['bytes'] for x in rows),'source_checkout_strategy':'non-cone sparse exact critical paths at pinned commit','project_configuration_changed':False,'solution_modules_compiled':False}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
