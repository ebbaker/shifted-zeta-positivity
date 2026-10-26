#!/usr/bin/env python3
"""N01 isolated finite case worker. Edward Baker; GPT-6.1 Sol, ultra, 2026-10-26."""
import argparse, hashlib, importlib, json, os, platform, resource, signal, sys, threading, time
from pathlib import Path

def main():
    a=argparse.ArgumentParser();a.add_argument('family',choices=['gamma','gauss']);a.add_argument('action',choices=['run','replay']);a.add_argument('certificate');a.add_argument('--args',default='[]');a.add_argument('--time-seconds',type=float,default=60);o=a.parse_args()
    if sys.flags.optimize: raise RuntimeError('Assertions must be enabled for this replay')
    signal.setitimer(signal.ITIMER_REAL,o.time_seconds)
    memory=512*1024*1024
    try:
        resource.setrlimit(resource.RLIMIT_AS,(memory,resource.getrlimit(resource.RLIMIT_AS)[1]))
        memory_method={'os_limit':'accepted','kind':'RLIMIT_AS'}
    except (ValueError,OSError) as exc:
        memory_method={'os_limit':'unavailable','reason':repr(exc),'kind':'measured peak RSS plus sampling watchdog; no hard address-space cap claimed'}
    def rss_bytes():
        v=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return v if platform.system()=='Darwin' else v*1024
    def watchdog():
        while True:
            if rss_bytes()>memory:
                os.write(2,b'Process RSS storage limit reached\n');os._exit(75)
            time.sleep(0.02)
    threading.Thread(target=watchdog,daemon=True).start()
    mod=importlib.import_module(o.family+'_provider')
    start=time.perf_counter()
    args=json.loads(o.args,parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))
    if o.action=='run':
        cert=mod.run_case(*args)
        assert mod.certificate_args(cert)==args, 'producer mathematical input mismatch'
        p=Path(o.certificate);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(cert,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n')
        result={'certificate_bytes':p.stat().st_size}
    else:
        cert=json.loads(Path(o.certificate).read_text(),parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))
        assert mod.certificate_args(cert)==args, 'replay mathematical input mismatch'
        result=mod.replay_case(cert)
        if result is False: raise AssertionError('replay returned False')
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if platform.system()!='Darwin': rss*=1024
    source=Path(mod.__file__)
    source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(source.parent.glob('*.py'))}
    if rss>memory: raise MemoryError('RSS exceeded process storage cap')
    delivered=(result.get('delivered',result.get('ok',False)) is True) if o.action=='replay' else True
    print(json.dumps({'success':True,'delivery_pass':delivered,'action':o.action,'family':o.family,'requested_args':args,'provider_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_hashes':source_hashes,'elapsed_seconds':time.perf_counter()-start,'peak_process_rss_bytes':rss,'storage_limit_bytes':memory,'storage_limit_method':memory_method,'python_optimize':sys.flags.optimize,'result':result},sort_keys=True,allow_nan=False))
if __name__=='__main__':main()
