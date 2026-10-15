#!/usr/bin/env python3
"""Fresh full-source stationary roots on three frozen theta curves; baseline only.
Prepared for Edward Baker, 2026-10-15; substantial LLM assistance.
Recorded model gpt-6-astra, reasoning effort ultra.
"""
import sys
import argparse
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import json,time,platform
from math import factorial
import flint
from flint import arb,ctx

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import check_shifted_contour_payments as source
import certify_phase_centered_residual as base

def require(ok,msg):
    if not ok: raise RuntimeError(msg)
def rat(q):
    q=Q(q);return arb(q.numerator)/q.denominator
def enc(v):
    require(v.is_finite(),'finite enclosure')
    def end(x):
        m,e=x.man_exp();return [str(m),int(e)]
    return [end(v.lower()),end(v.upper())]
def sym(v):return arb(0,v.upper())
def digest(p):return sha256(Path(p).read_bytes()).hexdigest()
def sign(v):return 1 if v.lower()>0 else -1 if v.upper()<0 else 0

def main(args):
    started=time.monotonic();ctx.prec=args.bits
    require(args.bits>=192,'minimum bits')
    a=arb.pi()/16;c=arb.pi()/8;N=8;U=arb(3)/2;T=arb(1)/2
    tol=arb(2)**(-(args.bits-64));lx=8;lt=4;top=4+2*(lt-1)+lx-1;mtop=top+1
    npay=[source.index_payment(k,a,N,T)[0] for k in range(mtop+1)]
    upay=[source.integration_payment(k,a,U,T)[0] for k in range(mtop+1)]
    payments=[npay[k]+upay[k] for k in range(mtop+1)]
    moments=[base.moment(k,a,N,U,T,tol) for k in range(mtop+1)]
    print('moments paid',round(time.monotonic()-started,2),flush=True)
    def ttheta(theta,x):return rat(theta)/(x/(4*arb.pi())).log()
    def sample(theta,x,j):
        X=rat(x);t=ttheta(theta,X)
        require(0<t<T,'theta time in proved interval')
        scale=((c-a)*X).exp()
        value=scale*(source.finite_integral(j,a,N,U,t,X,tol)+sym(payments[j]))
        return value,t
    rows=[]
    for theta in [Q(1,2),Q(3,4),Q(1)]:
      for j,window in [(0,(101,102)),(1,(103,104))]:
        left,right=map(Q,window)
        vl,_=sample(theta,left,j+1);vr,_=sample(theta,right,j+1)
        require(sign(vl)*sign(vr)==-1,'initial genuine endpoint signs')
        original=[enc(vl),enc(vr)]
        trace=[]
        for step in range(6):
            middle=(left+right)/2;vm,_=sample(theta,middle,j+1)
            require(sign(vm)!=0,'bisection point resolved')
            trace.append({'x':str(middle),'normalized_stationary_jet':enc(vm)})
            if sign(vm)==sign(vl):left,vl=middle,vm
            else:right,vr=middle,vm
        X=rat((left+right)/2);dx=rat((right-left)/2)
        tl=ttheta(theta,rat(right)).lower();tr=ttheta(theta,rat(left)).upper()
        tc=(tl+tr)/2;dt=((tr-tl)/2).upper()
        require(0<tl and tr<T,'whole root rectangle in source time range')
        scale=((c-a)*X).exp()
        finite=[source.finite_integral(k,a,N,U,tc,X,tol) for k in range(top+1)]
        center=[scale*(finite[k]+sym(payments[k])) for k in range(top+1)]
        uniform_scale=((c-a)*X+a*dx).exp()
        maj=[uniform_scale*M for M in moments]
        data=[base.transport(center,maj,k,dx,dt,lx,lt) for k in range(5)]
        h=[v[0] for v in data]
        xb=X+sym(dx);L=(xb/(4*arb.pi())).log()
        curve_derivative=h[j+2]+rat(theta)/(xb*L*L)*h[j+3]
        require(sign(curve_derivative)!=0,'genuine theta-curve monotonicity')
        require(sign(curve_derivative)==sign(vr),'derivative agrees with endpoint crossing')
        lag=-h[j]*h[j+2]
        verdict='CERTIFIED_POSITIVE' if lag.lower()>0 else ('CERTIFIED_NEGATIVE' if lag.upper()<0 else 'UNDECIDED')
        rows.append({'theta':str(theta),'j':j,'initial_x_window':list(map(str,window)),
          'initial_endpoint_stationary_jets':original,'bisection_trace':trace,
          'root_x_bracket':[str(left),str(right)],'root_time_enclosure':[enc(tl),enc(tr)],
          'left_stationary_jet':enc(vl),'right_stationary_jet':enc(vr),
          'normalization':'e^(pi*xc/8), constant over the closed rectangle',
          'endpoint_normalization':'e^(pi*x_endpoint/8), positive; endpoint values used only for signs',
          'stationary_L_normalization':'e^(pi*xc/4)',
          'xc':str((left+right)/2),'tc':enc(tc),'dt':enc(dt),'dx':str((right-left)/2),
          'center_complete_jets':[enc(v) for v in center],
          'center_scaled_finite_quadrature_radii':[enc(scale*v.rad()) for v in finite],
          'whole_rectangle_complete_jets':[enc(v) for v in h],
          'space_payments':[enc(v[1]) for v in data],'time_payments':[enc(v[2]) for v in data],
          'curve_stationary_derivative':enc(curve_derivative),
          'unique_full_stationary_root':True,'fixed_kappa':0,
          'stationary_L_scaled':enc(lag),'stationary_L_verdict':verdict,
          'display_only':{'x_bracket':[str(left),str(right)],'time':(tc+sym(dt)).str(10),'L':lag.str(12),'curve_derivative':curve_derivative.str(12)}})
        print('theta',theta,'j',j,'root',[str(left),str(right)],'L',lag.str(12),verdict,'seconds',round(time.monotonic()-started,2),flush=True)
    record={'schema':'inv21_fresh_predetermined_theta_stationary_baseline_v1','date':'2026-10-15',
      'prepared_for':'Edward Baker','llm_assistance':'substantial','recorded_model':'gpt-6-astra','recorded_effort':'ultra',
      'status':'COMPLETED_BASELINE','script_sha256':digest(__file__),
      'dependencies':[{'name':p.name,'sha256':digest(p)} for p in [Path(source.__file__),Path(base.__file__)]],
      'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'bits':args.bits,'seconds':time.monotonic()-started},
      'frozen_protocol':{'theta':['1/2','3/4','1'],'initial_windows':{'0':['101','102'],'1':['103','104']},
          'bisection_steps':6,'a':'pi/16','N':8,'U':'3/2','tmax':'1/2','space_order':lx,'time_order':lt,'center_jet_top':top,'moment_top':mtop,'kappa0':0,'kappa1':0,
          'rule_changed_after_observation':False},
      'identities':{'theta':'theta=t log(x/(4pi))','stationarity':'S_j={h_(j+1)=0}',
          'curve_derivative':'d_x h_(j+1)(theta/log(x/(4pi)),x)=h_(j+2)+theta/[x log(x/(4pi))^2] h_(j+3)',
          'stationary_L':'L_j=-h_j h_(j+2) on full S_j; no energy quotient'},
      'source_payments':{'index':[enc(v) for v in npay],'integration':[enc(v) for v in upay],
          'complete_unscaled_moment_majorants':[enc(v) for v in moments]},
      'rows':rows,'root_count':len(rows),'positive_stationary_L_count':sum(r['stationary_L_verdict']=='CERTIFIED_POSITIVE' for r in rows),
      'limitations':['This is a fresh complete-source stationary baseline. It does not validate a transformed Poisson split or any arithmetic mechanism.',
        'All six root neighborhoods lie in a previously certified bounded height domain. No expanded sign domain, arbitrary-height assertion, predecessor coverage, or RH conclusion follows.',
        'The analytic source contour deformation, complete-index tails, integration tails, heat equation, and moment transport lemmas are trusted imported results. Arb/Acb arithmetic and quadrature are not formally verified here.',
        'Every endpoint is evaluated on the exact fixed-theta curve with ball enclosures. Monotonicity and signs are certified on its containing closed parameter rectangle.',
        'The zero-loss baseline is frozen before these fresh calculations. It is tested through direct signed products, never obtained by dividing by a sampled energy floor.']}
    payload=json.dumps(record,sort_keys=True,separators=(',',':'))+'\n'
    require(len(payload.encode())<1048576,'small output record')
    args.output.write_text(payload)
    print('OUTPUT',args.output,'bytes',len(payload),'seconds',round(time.monotonic()-started,2),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--bits',type=int,default=192);main(p.parse_args())
