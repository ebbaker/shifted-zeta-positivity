#!/usr/bin/env python3
from pathlib import Path
import importlib.util, json, os, shutil, hashlib
base=Path('/home/ubuntu/rh-replay-preparation')
spec=importlib.util.spec_from_file_location('isolation',base/'check_linux_isolation.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
root=Path('/home/ubuntu/rh-replay-integration/simple-match');assert not root.exists();root.mkdir(parents=True)
upstream=Path('/home/ubuntu/rh-replay-tools/sources/comparator/tests/projects/simple_match')
for name in ['Challenge.lean','Solution.lean','config.json']: shutil.copy2(upstream/name,root/name)
(root/'lakefile.toml').write_text('name = "replaySmoke"\nversion = "0.1.0"\n\n[[lean_lib]]\nname = "Solution"\n\n[[lean_lib]]\nname = "Challenge"\n')
prefix='/home/ubuntu/rh-replay-tools/toolchain/lean-4.34.1-linux_aarch64'
env=dict(os.environ);env['PATH']='/home/ubuntu/rh-replay-tools/bin:'+prefix+'/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin';env['ELAN_TOOLCHAIN']='leanprover/lean4:v4.34.1'
command=['systemd-run','--property=RestrictAddressFamilies=~AF_UNIX','--user','--pty','--unit=rh-replay-smoke','--property=RuntimeMaxSec=120s','-E','PATH='+env['PATH'],'-E','ELAN_TOOLCHAIN='+env['ELAN_TOOLCHAIN'],'--working-directory='+str(root),'--','bash','-c','lake env comparator config.json']
a=m.run_pty(command,root,env,120)
log=base/'comparator_smoke.log';log.write_text(a.pop('stdout_stderr_combined'))
a.update({'log':str(log),'log_bytes':log.stat().st_size,'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest(),'source_profile':'pinned comparator simple_match fixture; sourcefullyread','mathematical_replay_run':False})
(base/'comparator_smoke.json').write_text(json.dumps(a,indent=2)+'\n')
print(log.read_text());print(json.dumps(a,indent=2));assert a['exit_code']==0 and not a['timed_out']
