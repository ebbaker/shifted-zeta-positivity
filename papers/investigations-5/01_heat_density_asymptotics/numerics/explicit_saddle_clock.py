#!/usr/bin/env python3
"""Note 19: exact polynomial controls and floating saddle-clock comparisons.

Prepared for Edward Baker, 24 October 2026, with substantial LLM assistance.
gpt-6-astra (Codex), actual effort max. No interval certificate or fitted roots.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys

import numpy as np

NUMERICS = Path(os.environ.get('HDA_NUMERICS', Path(__file__).resolve().parent))
sys.path.insert(0, str(NUMERICS))
from adaptive_transport_checks import finite_allowances, gauss_tail, saddle
from adaptive_transport_theta_pilot import observe
from two_time_limits_round3 import positive_source

C = F(315,256)
PI = math.pi
CB = 1/(1-16*math.exp(-3*PI))
BN = [F(1),F(-1,2),F(1,6),F(0),F(-1,30),F(0),F(1,42),F(0),F(-1,30),F(0),F(5,66)]


def bernoulli(n, x):
    return sum(math.comb(n,j)*BN[j]*x**(n-j) for j in range(n+1))


def frac(x):
    return x-math.floor(x)


def endpoint_derivative(j, ell, moment=False):
    ds = {4:384,5:3840,6:17280,7:40320,8:40320}
    def a(k): return C*ds.get(k,0)/ell**(k+1)
    return ell*a(j)+j*a(j-1) if moment else a(j)


def periodized(p, x, ell, moment=False):
    """P for k; D for s*k. Also their analytic partial derivatives in p."""
    left = frac((x-ell)/p+F(1,2))
    right = frac((x+ell)/p+F(1,2))
    result = 0 if moment else 1/p
    dp = 0 if moment else -1/p**2
    for j in range(4,10 if moment else 9):
        a = endpoint_derivative(j,ell,moment)
        am = (-1)**(j+int(moment))*a
        value = a*bernoulli(j+1,left)-am*bernoulli(j+1,right)
        result += p**j/math.factorial(j+1)*value
        dp += j*p**(j-1)/math.factorial(j+1)*value
        dp += p**j/math.factorial(j)*(a*bernoulli(j,left)*(-(x-ell)/p**2)
                       -am*bernoulli(j,right)*(-(x+ell)/p**2))
    return result, dp


def lattice(p, x, ell):
    lo=math.floor((x-ell)/p-F(1,2))-1
    hi=math.ceil((x+ell)/p-F(1,2))+1
    mass=moment=deriv=0
    for j in range(lo,hi+1):
        a=(j+F(1,2))*p
        s=(x-a)/ell
        if abs(s)<=1:
            k=C/ell*(1-s*s)**4
            kp=-8*C/ell**2*s*(1-s*s)**3
            mass+=k; moment+=a*k; deriv+=a*kp
    return mass,moment,deriv


def exact_checks():
    rows=[]
    for p in [F(2,3),F(3,2),F(7,3)]:
        for ell in [F(1),F(5,2)]:
            for x in [F(0),F(2,7),F(-17,5),ell+p/2]:
                P,Pp=periodized(p,x,ell)
                D,_=periodized(p,x,ell,True)
                m,v,d=lattice(p,x,ell)
                checks=[P==m,x*P-D==v,-p*Pp==d]
                assert all(checks),(p,x,ell,checks)
                rows.append({'p':str(p),'ell':str(ell),'x':str(x),'three_equalities':True})
    return {'arithmetic':'exact rational','cases':rows,'equalities':3*len(rows),
            'identities':['density periodization','first lattice moment','continuity derivative'],
            'includes_kernel_edge_crossings':True}


def source_bounds(t):
    L,kap=saddle(t)
    inherited=finite_allowances(t)
    if not inherited['source_gates']:
        return {'t':t,'source_gate':False,'inherited_gates':False}
    c=1/(4*math.e); h=kap**(1/12)
    q=t*L*L+9*L-PI*math.exp(4*L)
    QL=16*math.exp(-3*PI*math.exp(4*(L-.25)))
    dL=3/(2*PI)*math.exp(-4*(L-.25))+QL/(1-QL)
    ec=math.expm1(4*math.e/3*kap**(-.25))
    ec+=(ec+1)*dL
    def G(p,y):return 2*gauss_tail(p,.5,y/math.sqrt(kap),0)
    def D(p,y):
        left=math.log(CB)+(p+1)*math.log(L*math.sqrt(kap))+y*L-c*kap/16
        return ec*G(p,y)+2*(CB*gauss_tail(p,c,y/math.sqrt(kap),h)
            +gauss_tail(p,.5,y/math.sqrt(kap),h))+math.exp(left)
    zm=math.sqrt(2*PI)-D(0,0)
    if zm<=0: return {'t':t,'Z_lower':zm,'source_gate':False}
    def A(p,y):return kap**(-p/2)*(G(p,y)+D(p,y))/zm
    old=kap**(-.5)*D(1,0)/zm
    logp0=math.log(CB)-PI+.5*math.log(kap)-q-math.log(zm)
    p0=math.exp(logp0)
    eta=1+2*t/kap
    score_e=2*eta*A(2,4)+(5+p0)/kap
    emu=min(old,score_e)
    ev=2*eta*A(3,4)+5*A(1,0)/kap+L*p0/kap+emu**2
    B3=4*(A(3,0)+emu**3*A(0,0))
    dalpha=2*ev+B3/(L-emu)
    row={'t':t,'L':L,'kappa':kap,'Z_lower':zm,'source_gate':True,
         'old_mean_error':old,'score_mean_error':score_e,'mean_error':emu,
         'variance_error':ev,'alpha_error':dalpha,'boundary_log_upper':logp0,
         'boundary_float_underflow':p0==0,'inherited_gates':inherited.get('passed_all_gates',False)}
    if not row['inherited_gates']:return row
    X=inherited['X_upper']; delta=X*emu/L
    R=inherited['collar_radius_upper']
    r0=4*inherited['delta_upper']/inherited['mu_lower']
    n=2*inherited['mu_upper']*(10+R+delta)/PI+2
    k0=float(C)/10; k1=8*float(C)*(6/7)**3/math.sqrt(7)/100
    k2=8*float(C)/1000; h0=float(C)/.75
    dc=dalpha*X*k0+(2/kap)*delta*(k0+(X+delta)*k1)
    dt=dalpha*X*k1+(2/kap)*delta*(k1+(X+delta)*k2)
    ER=inherited['regulator_density_bias']+n*h0*k1*(r0+delta)
    EJ=inherited['moving_clock_current_error']+n*h0*dc
    ET=inherited['moving_clock_time_derivative_error']+n*h0*dt
    row.update(X_upper=X,lattice_displacement=delta,density_bound=ER,
               current_bound=EJ,time_derivative_bound=ET,
               new_coefficient_time_cost=n*h0*dt,
               total_time_bound_over_L_over_kappa=ET/(L/kap),
               inherited_time_bound_over_L_over_kappa=inherited['time_error_to_drift'],
               full_horizontal_buffer=10+2*R+delta)
    return row


def clock_values(t,x):
    L,kap=saddle(t); p=PI/L
    P,Pp=periodized(p,x,10.)
    D,_=periodized(p,x,10.,True)
    return np.array([P,-(2/kap)*(x*P-D),-(2/kap)*p*Pp],float)


def compare_observation(row,label):
    t=row['t']; x=row['x']; L,kap=saddle(t)
    values=clock_values(t,x)
    truth=np.array(row['zero_measure_observables'])
    mean=2*L/(PI*kap)
    ref=np.maximum(row.get('source_refinement',[0]*3),
                   row.get('contour_refinement',[0]*3))
    ref=np.maximum(ref,row.get('contour_height_change',[0]*3))
    return {'sample':label,'t':t,'x':x,'saddle_clock':values.tolist(),
            'theta_zero_observables':truth.tolist(),'absolute_errors':abs(values-truth).tolist(),
            'density_error_over_L_over_pi':float(abs(values[0]-truth[0])/(L/PI)),
            'time_error_over_saddle_mean_derivative':float(abs(values[2]-truth[2])/mean),
            'continuum_L_time_error_over_mean':float(abs(mean-truth[2])/mean),
            'reported_refinement_max':ref.tolist(),
            'time_refinement_over_mean':float(ref[2]/mean),
            'observed_mu_minus_L':row['mu']-L,
            'observed_alpha_minus_2_over_kappa':row['muprime']/row['mu']-2/kap}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--skip-new-theta',action='store_true');args=ap.parse_args()
    controls=exact_checks()
    old=json.loads((NUMERICS/'ADAPTIVE_TRANSPORT_THETA_PILOT_20261024.json').read_text())
    observations=[compare_observation(r,'reused Note 16 observation') for r in old['rows']]
    if not args.skip_new_theta:
        for t in [3e6,3e8]:
            L,kap,_,v,p,_=positive_source(t,48,14)
            mu=L+float(p@v)
            X=math.floor(mu*kap**(1/3)/PI)*PI/mu
            for part in [.37,.83]:
                center=part*(X-11)
                base=observe(t,center,32,12,224)
                finer=observe(t,center,48,14,320)
                displaced=observe(t,center,48,14,320,.8)
                def diff(a,b):return abs(np.array(a['zero_measure_observables'])-np.array(b['zero_measure_observables'])).tolist()
                finer.update(source_refinement=diff(base,finer),contour_refinement=[0]*3,
                             contour_height_change=diff(finer,displaced))
                observations.append(compare_observation(finer,'new held-out time and height; combined source/contour refinement'))
    bounds=[source_bounds(t) for t in [1e4,1e6,3e6,3e8,1e9,1e12,1e18,1e24]]
    by_time={r['t']:r for r in bounds}
    for row in observations:
        budget=by_time[row['t']]
        row['floating_inherited_gates_pass']=budget['inherited_gates']
        row['mean_coefficient_bound']=budget['mean_error']
        row['drift_coefficient_bound']=budget['alpha_error']
        assert abs(row['observed_mu_minus_L'])<=budget['mean_error']
        assert abs(row['observed_alpha_minus_2_over_kappa'])<=budget['alpha_error']
    dependencies=['adaptive_transport_checks.py','adaptive_transport_theta_pilot.py',
                  'two_time_limits_round3.py','ADAPTIVE_TRANSPORT_THETA_PILOT_20261024.json']
    result={'date':'2026-10-24','prepared_for':'Edward Baker','model':'gpt-6-astra',
            'reasoning_effort':'max','status':'Proved-in-note estimates; exact rational formula controls; floating theta diagnostics.',
            'python':platform.python_version(),'numpy':np.__version__,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{f:hashlib.sha256((NUMERICS/f).read_bytes()).hexdigest() for f in dependencies},
            'exact_controls':controls,'finite_allowances':bounds,'observations':observations,
            'limitations':['No interval arithmetic or finite onset certificate.',
              'New source and contour refinements are combined; reused observations retain their original separate refinements.',
              'No coefficients fitted; no theta roots acquired; no finite-epsilon peak sampling.',
              'Zero-measure observations require the separate analytical regulator-transfer bounds.',
              'No covariance closure, all-time trajectory solve or independent implementation.',
              'Very small source tails may underflow in the floating allowances; logs are retained for the boundary term.']}
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'exact_equalities':controls['equalities'],'observations':len(observations),
        'max_derivative_relative_error':max(r['time_error_over_saddle_mean_derivative'] for r in observations),
        'max_continuum_derivative_relative_error':max(r['continuum_L_time_error_over_mean'] for r in observations),
        'bounds':[{k:r.get(k) for k in ['t','inherited_gates','total_time_bound_over_L_over_kappa']} for r in bounds]}))


if __name__=='__main__': main()
