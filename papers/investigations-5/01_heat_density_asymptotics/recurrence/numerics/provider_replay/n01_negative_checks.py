#!/usr/bin/env python3
"""Targeted N01 rejection controls after preflight audit fixes.
Prepared for Edward Baker, gpt-6.1-sol/ultra, 2026-10-26.
Uses only already generated N01 cases; does not enlarge the matrix.
"""
import argparse,copy,hashlib,importlib.util,json,os,resource,signal,subprocess,sys,time
from fractions import Fraction
from pathlib import Path

def atomic(p,r):
    q=p.with_name(p.name+'.tmp')
    with q.open('w') as f:
        json.dump(r,f,indent=2,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())
    os.replace(q,p)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--code-dir',type=Path,required=True);ap.add_argument('--cert-dir',type=Path,required=True);ap.add_argument('--record',type=Path,required=True);ap.add_argument('--budget-state',type=Path,required=True);o=ap.parse_args()
    state=json.loads(o.budget_state.read_text());prior=state['elapsed_compute_seconds'];start=time.perf_counter();allocation=min(60,900-prior-1);assert allocation>0
    state['elapsed_compute_seconds']=prior+allocation;state['pending_reservation']={'action':'targeted negative checks','seconds':allocation};atomic(o.budget_state,state)
    signal.setitimer(signal.ITIMER_REAL,allocation)
    sys.path.insert(0,str(o.code_dir));import gamma_provider as gamma;import gauss_provider as gauss
    g=json.loads((o.cert_dir/'gamma_1_0_32.json').read_text());q=json.loads((o.cert_dir/'gauss_2_32.json').read_text())
    checks=[]
    def rejects(name,fn,match=None):
        try:fn()
        except Exception as exc:
            msg=str(exc);assert match is None or match in msg,(name,msg)
            checks.append({'test':name,'rejected':True,'exception':type(exc).__name__,'reason':msg});return
        raise AssertionError(name+' accepted altered certificate')
    assert gamma.replay_case(g)['ok'] is True
    assert gauss.replay_case(q)['delivered'] is True
    # Alter mathematical output, radius and a structurally valid wrong primitive type.
    x=copy.deepcopy(g);x['jets'][0]['value'][0]=str(Fraction(x['jets'][0]['value'][0])+1)
    rejects('gamma altered delivered center',lambda:gamma.replay_case(x))
    x=copy.deepcopy(g);x['jets'][0]['radius']='0/1'
    rejects('gamma understated delivered radius',lambda:gamma.replay_case(x))
    x=copy.deepcopy(g['shift_logs'][0]);arg=x['angle']['argument'];x['angle']=copy.deepcopy(g['log_2pi']['pi']);x['angle']['argument']=arg
    rejects('gamma pi certificate substituted for atan child',lambda:gamma.replay_complex_log(x),'atan')
    x=copy.deepcopy(g['log_2pi']);x['pi']=copy.deepcopy(g['shift_logs'][0]['angle'])
    rejects('gamma atan certificate substituted for pi child',lambda:gamma.replay_log_2pi(x,Fraction(1,2**32)),'pi')
    x=copy.deepcopy(q);x['roots'][0]['weight']['n']=hex(int(x['roots'][0]['weight']['n'],0)+int(x['roots'][0]['weight']['d'],0))
    rejects('Gauss altered delivered weight',lambda:gauss.replay_case(x))
    x=copy.deepcopy(q);x['roots'][0]['weight_error']={'n':'0x0','d':'0x1'}
    rejects('Gauss understated weight radius',lambda:gauss.replay_case(x))
    x=copy.deepcopy(q);x['roots'][0]['root_count_open']=2
    rejects('Gauss altered root count',lambda:gauss.replay_case(x))
    x=copy.deepcopy(q);x['mapped_rules'][2]['left']={'n':'0x0','d':'0x1'}
    rejects('Gauss altered short-interval map',lambda:gauss.replay_case(x))
    # Exercise the public worker boundary, with the already certified gamma input.
    def worker_reject(name,path,args,match):
        t=time.perf_counter();r=subprocess.run([sys.executable,str(o.code_dir/'n01_worker.py'),'gamma','replay',str(path),'--args',json.dumps(args),'--time-seconds','10'],capture_output=True,text=True,timeout=11)
        assert r.returncode!=0 and match in r.stderr,(name,r.returncode,r.stdout,r.stderr)
        checks.append({'test':name,'rejected':True,'exit_code':r.returncode,'reason_match':match,'elapsed_seconds':time.perf_counter()-t})
    worker_reject('worker rejects certificate for different requested input',o.cert_dir/'gamma_1_0_32.json',[32,0,32],'input mismatch')
    bad=o.record.with_name('negative_nonfinite_certificate.json');bad.write_text(json.dumps(g)[:-1]+',"nonfinite":NaN}')
    worker_reject('worker rejects nonfinite serialized metadata',bad,[1,0,32],'NaN')
    bad.unlink()
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
    assert rss<=512*1024*1024
    elapsed=time.perf_counter()-start
    record={'request':'HDA-R05-N01 r1','model':'gpt-6.1-sol','effort':'ultra','date':'2026-10-26','scope':'Targeted rejection controls on existing matrix cells, prompted by preflight audit','positive_controls':2,'rejection_controls':checks,'count':len(checks),'all_rejected':True,'elapsed_seconds':elapsed,'peak_parent_rss_bytes':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [o.cert_dir/'gamma_1_0_32.json',o.cert_dir/'gauss_2_32.json']}}
    atomic(o.record,record);state['elapsed_compute_seconds']=prior+elapsed;state.pop('pending_reservation',None);state['attempts'].append({'record':o.record.name,'case_count':len(checks)+2});atomic(o.budget_state,state)
    print(json.dumps({'all_rejected':True,'count':len(checks),'elapsed_seconds':elapsed,'total_compute_seconds':state['elapsed_compute_seconds']}))
if __name__=='__main__':main()
