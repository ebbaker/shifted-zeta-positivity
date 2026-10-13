#!/usr/bin/env python3
from pathlib import Path
import subprocess, os, json, hashlib, datetime
root=Path('/home/ubuntu/rh-replay-source/lean');base=Path('/home/ubuntu/rh-replay-preparation');tools=Path('/home/ubuntu/rh-replay-tools')
pre=json.loads((base/'linux_dependency_preparation.json').read_text());assert pre['status']=='all_42_pins_and_23_prescribed_patches_verified'
iso=json.loads((base/'linux_isolation_001.json').read_text());assert iso['all_controls_passed'] and iso['passed_count']==16
mathlib=root/'.lake/packages/mathlib';pin=subprocess.check_output(['git','-C',str(mathlib),'rev-parse','HEAD'],text=True).strip();assert pin=='d13f23b723b8a846827a245b89c10fc7d3f11612'
manifest=root/'lake-manifest.json';before=hashlib.sha256(manifest.read_bytes()).hexdigest()
assert not (root/'.lake/build').exists(),'Use a fresh mathematical checking baseline'
prefix=tools/'toolchain/lean-4.34.1-linux_aarch64';env=dict(os.environ)
for key in list(env):
 if key.startswith('MATHLIB_CACHE') or key in ['LEAN_PATH','LEAN_SYSROOT','LEAN_SRC_PATH','LEAN_CC']: env.pop(key)
env['PATH']=str(tools/'bin')+':'+str(prefix/'bin')+':/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin';env['ELAN_TOOLCHAIN']='leanprover/lean4:v4.34.1';env['MATHLIB_NO_CACHE_ON_UPDATE']='1'
command=[str(prefix/'bin/lake'),'exe','cache','get','--repo=leanprover-community/mathlib4','--cache-from=master']
record={'schema':'trusted-mathlib-cache-preparation-v1','started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mathlib_commit':pin,'command':command,'working_directory':str(root),'trust_policy':'Official Mathlib master/release/staging cache and default read-only legacy fallback only; no forks, alternative scopes or unsafe history search. Cache artifact contents are trusted to match their source inputs, as allowed by comparator README.','source_manifest_sha256_before':before,'mathematical_solution_modules_compiled':False,'mathematical_replay_run':False}
log=base/'trusted_mathlib_cache.log'
with log.open('wb') as out:
 p=subprocess.run(command,cwd=root,env=env,stdout=out,stderr=subprocess.STDOUT)
record['exit_code']=p.returncode;record['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();record['source_manifest_sha256_after']=hashlib.sha256(manifest.read_bytes()).hexdigest();record['log']={'path':str(log),'bytes':log.stat().st_size,'sha256':hashlib.sha256(log.read_bytes()).hexdigest()};record['status']='trusted_cache_prepared' if p.returncode==0 and before==record['source_manifest_sha256_after'] else 'operational_failure'
(base/'trusted_mathlib_cache_preparation.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
assert p.returncode==0 and before==record['source_manifest_sha256_after']
assert not (root/'.lake/build/lib/lean/OAI').exists(),'A mathematical solution was unexpectedly built'
