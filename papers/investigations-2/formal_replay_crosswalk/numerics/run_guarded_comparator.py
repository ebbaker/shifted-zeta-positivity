#!/usr/bin/env python3
"""Run one pinned mathematical target under the tested Linux checking guard."""
from pathlib import Path
import argparse, json, os, subprocess, importlib.util, hashlib, datetime, re
p=argparse.ArgumentParser();p.add_argument('--target',choices=['zeta','Dirichlet','Hecke'],required=True);p.add_argument('--attempt',default='001');p.add_argument('--baseline-name',required=True);p.add_argument('--timeout',type=int,default=7200);args=p.parse_args()
assert re.fullmatch('[a-z0-9-]+',args.attempt);assert 60<=args.timeout<=21600
base=Path('/home/ubuntu/rh-replay-preparation');root=Path('/home/ubuntu/rh-replay-source/lean');tools=Path('/home/ubuntu/rh-replay-tools')
assert os.getuid()!=0
output=base/f'replay_{args.target}_{args.attempt}.json';assert not output.exists(),'Preserve old attempt; use a new filename'
assert not (root/'.lake/build/lib/lean/OAI').exists(),'Restore the clean baseline before another target'
assert not (root/'.lake/build/lib/lean/ComparatorChallenges').exists(),'Checking baseline has already compiled a challenge'
iso=json.loads((base/'linux_isolation_001.json').read_text());assert iso['all_controls_passed'] and iso['passed_count']==16
boot=json.loads((tools/'bootstrap_linux_tools_result.json').read_text());assert boot['status']=='auxiliary_tools_built'
assert hashlib.sha256((tools/'bin/landrun').read_bytes()).hexdigest()==iso['tools']['landrun']['sha256']
for key in ['comparator','lean4export','landrun']: assert hashlib.sha256((tools/'bin'/key).read_bytes()).hexdigest()==boot['binaries'][key]['sha256']
configs={'zeta':'QuasiRiemannHypothesis','Dirichlet':'DirichletSevenEighths','Hecke':'HeckeSevenEighths'}
config=root/'ComparatorChallenges'/(configs[args.target]+'.json');configuration=json.loads(config.read_text());assert configuration['permitted_axioms']==['propext','Quot.sound','Classical.choice'];assert configuration.get('definition_names',[])==[] and not configuration['enable_nanoda']
env=dict(os.environ);env['FORMAL_REPLAY_ARCHIVES']=str(base/'archive')
pre=subprocess.run(['python3',str(base/'check_replay_inputs.py'),'--checkout',str(root.parent),'--verify-record',str(base/'source_inventory_20261012.json')],env=env,capture_output=True,text=True)
prelog=base/f'replay_{args.target}_{args.attempt}_source_preflight.log';prelog.write_text(pre.stdout+pre.stderr);assert pre.returncode==0
prefix=Path(boot['lean_invocation']['prefix']);env['PATH']=str(tools/'bin')+':'+str(prefix/'bin')+':/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin';env['ELAN_TOOLCHAIN']='leanprover/lean4:v4.34.1'
unit=f'rh-replay-{args.target.lower()}-{args.attempt}'
command=['systemd-run','--property=RestrictAddressFamilies=~AF_UNIX','--user','--pty','--unit='+unit,'--property=RuntimeMaxSec='+str(args.timeout)+'s','-E','PATH='+env['PATH'],'-E','ELAN_TOOLCHAIN='+env['ELAN_TOOLCHAIN'],'--working-directory='+str(root),'--','bash','-c','lake env comparator "$1"','bash','ComparatorChallenges/'+config.name]
a={'schema':'guarded-mathematical-replay-v1','target':args.target,'attempt':args.attempt,'status':'running','started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'model':'GPT-6 (Codex); exact serving variant unexposed','effort':'not exposed; not inferred','baseline_name':args.baseline_name,'fresh_OAI_and_challenge_build_trees_absent':True,'configuration':configuration,'configuration_sha256':hashlib.sha256(config.read_bytes()).hexdigest(),'command':command,'actual_axioms':None,'actual_axiom_report_note':'Pinned comparator verifies allowed-set compliance but does not emit exact used set or accepted-export digest.','kernel_result':None,'axiom_allowed_set_compliance':None,'statement_comparison':None,'untrusted_solution_compilation_outside_guard':False}
output.write_text(json.dumps(a,indent=2)+'\n')
spec=importlib.util.spec_from_file_location('isolation',base/'check_linux_isolation.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
result=m.run_pty(command,root,env,args.timeout+30)
log=base/f'replay_{args.target}_{args.attempt}.log';text=result.pop('stdout_stderr_combined');log.write_text(text)
okay=result['exit_code']==0 and not result['timed_out'] and 'Lean default kernel accepts the solution' in text and 'Your solution is okay!' in text
if result['timed_out']: subprocess.run(['systemctl','--user','stop',unit+'.service'],capture_output=True)
a.update({'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'process_result':result,'status':'comparator_accepted' if okay else 'unsuccessful_attempt_requires_classification','log':{'path':str(log),'bytes':log.stat().st_size,'sha256':hashlib.sha256(log.read_bytes()).hexdigest()},'source_preflight_log':{'path':str(prelog),'sha256':hashlib.sha256(prelog.read_bytes()).hexdigest()},'kernel_result':'accepted' if okay else None,'axiom_allowed_set_compliance':'passed' if okay else None,'statement_comparison':'passed' if okay else None})
output.write_text(json.dumps(a,indent=2)+'\n');print(json.dumps(a,indent=2));raise SystemExit(0 if okay else 1)
