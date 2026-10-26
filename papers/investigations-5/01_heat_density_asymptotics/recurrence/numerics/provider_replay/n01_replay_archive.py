#!/usr/bin/env python3
"""Hash-bound N01 replay. Edward Baker with LLM assistance, gpt-6.1-sol,
ultra, 2026-10-26. Standard library only. Rejects missing/mismatched data.
Lookup: numerics/output/n01/... then same relative path under
HDA_RECURRENCE_ARCHIVES. See recurrence/ARCHIVES.md.
"""
import argparse,hashlib,json,os,subprocess,sys,time
from pathlib import Path

def locate(numerics,relative):
    rel=Path(relative)
    if rel.is_absolute() or '..' in rel.parts:raise ValueError('unsafe certificate path')
    local=numerics/rel
    if local.is_file():return local
    root=os.environ.get('HDA_RECURRENCE_ARCHIVES')
    if root and (Path(root)/rel).is_file():return Path(root)/rel
    raise FileNotFoundError(str(rel)+' absent; regenerate with n01_run.py or provide HDA_RECURRENCE_ARCHIVES as documented in ARCHIVES.md')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--manifest',type=Path,default=Path(__file__).resolve().parents[1]/'01_PROVIDER_REPLAY_20261026.json');ap.add_argument('--seconds',type=float,default=900);o=ap.parse_args();assert 0<o.seconds<=900
    rec=json.loads(o.manifest.read_text());numerics=o.manifest.resolve().parent;start=time.perf_counter();total=0
    for item in rec['source_files']:
        path=numerics/item['path']
        if hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:raise ValueError('source mismatch: '+item['path'])
    for item in rec['certificates']:
        p=locate(numerics,item['path'])
        if hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:raise ValueError('certificate hash mismatch: '+item['path'])
        remaining=o.seconds-(time.perf_counter()-start)
        if remaining<=1:raise TimeoutError('finite replay budget reached')
        cmd=[sys.executable,str(Path(__file__).with_name('n01_worker.py')),item['family'],'replay',str(p),'--args',json.dumps(item['args']),'--time-seconds',str(min(60,remaining-0.5))]
        result=subprocess.run(cmd,capture_output=True,text=True,timeout=min(60,remaining-0.5))
        if result.returncode:raise RuntimeError(item['path']+': '+result.stderr)
        row=json.loads(result.stdout)
        if not row['success'] or not row['delivery_pass']:raise ValueError('delivery replay rejected '+item['path'])
        total+=1
    print(json.dumps({'replayed_certificates':total,'elapsed_seconds':time.perf_counter()-start,'status':'all finite delivery inequalities passed','scope':'software/premise consistency replay; not independent specialist validation'}))
if __name__=='__main__':main()
