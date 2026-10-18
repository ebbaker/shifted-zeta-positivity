#!/usr/bin/env python3
"""One preregistered bounded theta-tail alignment bracket; no grid search.
Prepared for Edward Baker, 17 October 2026 (America/New_York).
Substantial LLM assistance: gpt-6.1-sol, reasoning effort ultra.
Self-contained python-flint computation. Evaluation repeats round-one
certify_evaluation.py's scaled Acb quadrature and positive tail bounds,
extended to x derivatives 0,1,2 and a local Taylor enclosure.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform, resource, signal, sys, time
from pathlib import Path
import flint
from flint import arb, acb, arb_mat, ctx

LOW='44.1060084240845'
MID='44.1060084240846'
HIGH='44.1060084240847'
T='0.25'
MAX_SECONDS=120
MAX_RSS_BYTES=512*1024*1024
STARTED=None

def peak_rss_bytes():
    raw=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if platform.system()=='Darwin' else raw*1024)
def check_budget():
    if time.monotonic()-STARTED>MAX_SECONDS: raise TimeoutError('120-second contract exceeded')
    if peak_rss_bytes()>MAX_RSS_BYTES: raise MemoryError('512-MiB peak-RSS contract exceeded')
def wall_timeout(signum,frame):
    raise TimeoutError('120-second wall-clock contract exceeded')

def ball(x): return x.str(90,more=True)
def radial(r): return arb(0,r.upper())
def coefficient_tail(start,j):
    lam=arb.pi()*start*start
    first=2*lam*lam*(-lam).exp()*math.factorial(j)/(4*lam-9)**(j+1)
    ratio=(arb(start+1)/start)**4*(-arb.pi()*(2*start+1)).exp()
    assert ratio<1
    return first/(1-ratio)
def integral_tail(n,j,t,U):
    lam=arb.pi()*n*n; q=lam*(4*U).exp()
    rate=4*q-9-2*t*U
    assert rate>0 and 8*q>t
    height=2*lam*lam*(9*U+t*U*U-q).exp()
    return height*sum(arb(math.comb(j,k)*math.factorial(k))*U**(j-k)/rate**(k+1) for k in range(j+1))
def full_abs_bound(n,j):
    lam=arb.pi()*n*n
    return 2*lam*lam*(-lam).exp()*math.factorial(j)/(4*lam-9)**(j+1)
def evaluate(xs,kmax):
    t,x=arb(T),arb(xs); U=arb(9)/5; cols=[[] for _ in range(kmax+1)]
    for n in range(1,11):
        lam=arb.pi()*n*n
        for j in range(kmax+1):
            check_budget()
            def f(u,analytic):
                e=(4*u).exp();q=lam*e
                z=(t*u*u+u-lam*(e-1)).exp()*(2*q*q-3*q)
                trig=((x*u).cos(),-(x*u).sin(),-(x*u).cos())[j]
                return u**j*z*trig
            z=acb.integral(f,0,U,rel_tol=arb('1e-95'),abs_tol=arb('1e-100'),eval_limit=150000,depth_limit=35)
            check_budget()
            assert z.is_finite() and z.imag.contains(0)
            cols[j].append(z.real*(-lam).exp()+radial(integral_tail(n,j,t,U)))
    h=[sum(cols[j],arb(0))+radial(coefficient_tail(11,j)) for j in range(kmax+1)]
    return cols,h

def matrices():
    beta=[(4*arb.pi()*n*n-1)*(-arb.pi()*n*n).exp() for n in range(1,7)]
    Q=arb_mat(6,5)
    for j,n in enumerate(range(1,6)):
        Q[n,j]=1; Q[0,j]=-beta[n]/beta[0]
    M=arb_mat([[sum(c for idx,c in ((k-1,1),(k,-2),(k+1,1)) if idx==n) for n in range(1,7)] for k in range(1,8)])
    D=M*Q;G=D.transpose()*D;P=Q*G.inv()*Q.transpose()
    return beta,Q,M,G,P

def quantities(cols,hh,Q,P):
    B=arb_mat([row[:6] for row in cols[:2]])
    S=B*P*B.transpose();a,b,c=S[0,0],(S[0,1]+S[1,0])/2,S[1,1]
    h=arb_mat([[hh[0]],[hh[1]]]);hn2=hh[0]**2+hh[1]**2
    F=b*(hh[0]**2-hh[1]**2)+(c-a)*hh[0]*hh[1]
    disc=((a-c)**2+4*b*b).sqrt();lam=(a+c+disc)/2
    top_test=(h.transpose()*S*h)[0,0]-(a+c)*hn2/2
    # At every F=0 with top_test>0, this equals the exact equality minimizer.
    delta=-(P*B.transpose()*h)/lam
    X=B*Q
    minors=[X[0,i]*X[1,j]-X[0,j]*X[1,i] for i in range(5) for j in range(i+1,5)]
    curv=hh[2]+sum(cols[2][n]*delta[n,0] for n in range(6)) if len(cols)>2 else None
    eta=(hn2/lam).sqrt()
    return F,disc,top_test,delta,curv,eta,minors,S

def run(output):
    global STARTED
    STARTED=started=time.monotonic();ctx.prec=448
    signal.signal(signal.SIGALRM,wall_timeout)
    signal.setitimer(signal.ITIMER_REAL,MAX_SECONDS)
    check_budget()
    beta,Q,M,G,P=matrices()
    endpoints=[]
    for xs in (LOW,HIGH):
        cols,hh=evaluate(xs,2)
        out=quantities(cols,hh,Q,P)
        endpoints.append({'x':xs,'F_det_h_Sh':ball(out[0]),'F_sign':1 if out[0]>0 else -1 if out[0]<0 else 0})
        print('endpoint',xs,ball(out[0]),flush=True)
    assert endpoints[0]['F_sign']*endpoints[1]['F_sign']==-1
    cols,hh=evaluate(MID,2)
    r=max((arb(MID)-arb(LOW)).abs_upper(),(arb(HIGH)-arb(MID)).abs_upper())
    # Taylor enclosure for all x in [LOW,HIGH]. The j=0,1 remainders
    # use computed next derivatives and a global (j+2)-derivative bound;
    # j=2 uses the global third derivative bound. All valid t<=1/4.
    local=[]
    for j in range(3):
        row=[]
        for n in range(1,11):
            if j<2:
                allowance=abs(cols[j+1][n-1])*r+full_abs_bound(n,j+2)*r*r/2
            else: allowance=full_abs_bound(n,3)*r
            row.append(cols[j][n-1]+radial(allowance))
        local.append(row)
    hlocal=[sum(local[j],arb(0))+radial(coefficient_tail(11,j)) for j in range(3)]
    F,disc,top_test,delta,curv,eta,minors,S=quantities(local,hlocal,Q,P)
    assert disc>0 and top_test>0
    assert any(m>0 or m<0 for m in minors)
    coeff=[1+delta[n,0] for n in range(6)]
    assert all(v>0 for v in coeff)
    assert curv<0
    # Exact algebraic checks: normalization follows from beta^T Q=0,
    # and equality and optimality hold at a bracket root by F=0/top_test.
    normres=sum(beta[n]*delta[n,0] for n in range(6))
    assert normres.contains(0)
    assert (Q.transpose()*arb_mat([[v] for v in beta])).contains(arb_mat(5,1))
    record={
      'schema':'source_measurement_single_gap_alignment_ball_v1',
      'date':'2026-10-17','timezone':'America/New_York','prepared_for':'Edward Baker',
      'model':'gpt-6.1-sol','reasoning_effort':'ultra',
      'llm_assistance':'Substantial LLM assistance; same-model internal audit, not independent specialist review.',
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'environment':{'python':platform.python_version(),'python_flint':flint.__version__,'precision_bits':448},
      'contract':{'time':T,'design':'unscaled recurrence, 7 rows','free_nodes':6,'anchor':False,'tail':'theta','normalization':'beta dot delta=0','bracket':[LOW,HIGH],'source_nodes_integrated':10,'upper_integration_endpoint':'9/5','no_grid':True,'max_seconds':MAX_SECONDS,'max_peak_rss_bytes':MAX_RSS_BYTES},
      'method':'Scaled Acb finite quadrature; analytic integral and coefficient tails; Taylor enclosure across one preregistered interval; IVT on F=det(h,S h), top eigenspace selected by positive Rayleigh gap.',
      'endpoints':endpoints,
      'interval':{'x':ball(arb(MID)+radial(r)),'h':[ball(v) for v in hlocal],
       'S':[[ball(S[i,j]) for j in range(2)] for i in range(2)],
       'eigenvalue_gap':ball(disc),'top_selection_test':ball(top_test),
       'rank_minor_certified_count':sum(m>0 or m<0 for m in minors),
       'eta_at_root':ball(eta),'coefficients_at_root':[ball(v) for v in coeff],
       'frozen_H_xx_at_root':ball(curv),'normalization_residual_enclosure':ball(normres)},
      'conclusions':{'exists_alignment_root':True,'h_nonzero':True,'rank_two':True,'simple_top':True,'r_M_equals_eta_at_root':True,'all_source_coefficients_positive_at_root':True,'frozen_curvature_negative_at_root':True,'root_unique':'not asserted','adjacent_theta_zero_gap_certified':'not asserted; review floating gap only'},
      'elapsed_seconds':time.monotonic()-started,'peak_rss_bytes':peak_rss_bytes()}
    check_budget()
    math_fields=('contract','endpoints','interval','conclusions')
    mathematical_content={key:record[key] for key in math_fields}
    canonical=json.dumps(mathematical_content,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
    record['mathematical_content_hash']={'algorithm':'SHA-256','projection':list(math_fields),'canonicalization':'UTF-8 json.dumps(sort_keys=True,separators=(comma,colon),ensure_ascii=False)','sha256':hashlib.sha256(canonical).hexdigest()}
    signal.setitimer(signal.ITIMER_REAL,0)
    output.write_text(json.dumps(record,indent=2)+'\n')
    print('eta',ball(eta),'curvature',ball(curv),'coefficients',[ball(v) for v in coeff],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();run(a.output)
