#!/usr/bin/env python3
"""Prescribed Riemann--Siegel edge hierarchy and exact finite CR identities.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
The record supplies execution model/effort. Internal same-model work only.
Finite Gaussian quadrature and coefficient identities do not pay RS or tails.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import time
import flint
from flint import arb, acb, acb_series, ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
EVALUATOR=INV/'symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py'
COHERENT=INV/'symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py'

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def out(v):return v.str(45,more=True)
def trim(poly):
    poly=list(poly)
    while poly and poly[-1]==0:poly.pop()
    return poly
def add(*polys):
    result=[F(0)]*max([len(p) for p in polys]+[0])
    for poly in polys:
        for j,value in enumerate(poly):result[j]+=value
    return trim(result)
def mul(left,right):
    result=[F(0)]*(len(left)+len(right))
    for j,c in enumerate(left):
        for k,d in enumerate(right):result[j+k]+=c*d
    return trim(result)
def scale(poly,c):return trim([v*c for v in poly])
def derivative(poly):return trim([j*poly[j] for j in range(1,len(poly))])

def exact_cr_checks():
    d={(0,0):[F(1)]}
    get=lambda n,k:d.get((n,k),[])
    for n in range(1,13):
        for k in range(0,3*n//2+1):
            m=3*n-2*k
            if m:
                d[n,k]=add(scale(get(n-1,k),F(1,4*m)),
                    mul([F(1,2*m),F(-1,m)],get(n-1,k-1)),
                    scale(get(n-1,k-2),-m-1))
            else:
                d[n,k]=add(*(scale(get(n,j),-(-1)**(k-j)*F(
                    math.factorial(2*k-2*j),math.factorial(k-j)))
                    for j in range(k)))
    counts=[]
    for n in range(1,13):
        count=0
        for k in range(0,3*n//2+1):
            lhs=derivative(get(n,k))
            rhs=add(scale(get(n-1,k-1),-1),
                    mul([F(2*(n-2)),F(2)],get(n-2,k-3)))
            if lhs!=rhs:raise ArithmeticError(('CR coefficient identity',n,k))
            count+=1
        counts.append({'order':n,'identities':count})
    return {'arithmetic':'exact fractions over Q[sigma]',
            'identity':'partial_sigma d[n,k] = -d[n-1,k-1] + 2(n-2+sigma)d[n-2,k-3]',
            'orders':counts,'count':sum(v['identities'] for v in counts),
            'all_passed':True,
            'scope':'Finite coefficients through order 12 only; no asserted general induction or remainder inequality.'}

def run(repo,bits):
    ctx.prec=bits;ctx.cap=20
    evm=load(repo/EVALUATOR,'s03_rs_edge_evaluator_'+str(bits))
    ev=evm.ClosedJetEvaluator(repo,bits);old=ev.old
    ctx.cap=20;pi=arb.pi();ii=acb(0,1);t=arb(21)/200;x=arb(1000)
    z=acb_series([acb(x),acb(1)],3)
    tau=z/2+pi*t/8;a=(tau/(2*pi)).sqrt();p=17-2*a;h=p-p[0]
    def profile(w):
        return ((ii*pi*(w*w/2+arb(3)/8)).exp()
            -ii*arb(2).sqrt()*(pi*w/2).cos())/(2*(pi*w).cos())
    profile_coeff=profile(acb_series([p[0],acb(1)],18))
    derivatives=[sum((math.factorial(j+k)*profile_coeff[j+k]
                    /math.factorial(j)*h**j for j in range(3)),
                    acb_series([acb(0)],3)) for k in range(16)]
    sp=ii*tau;gamma=a.log()+ii*pi/4;m0base=old.m0(sp)
    theta,omega,omega_x,b,b_x,chi=ev.phase(x,t)
    def physical_profile_data(profile):
        real=acb_series([v.real for v in profile],3)
        imag=acb_series([v.imag for v in profile],3)
        normalized=old.W_real(z,t)*tau.sqrt()*(tau*real-imag)
        jet=[normalized[0].real,normalized[1].real,2*normalized[2].real]
        defect=jet[0]+jet[2]/omega**2-omega_x*jet[1]/omega**3
        if not all(v.is_finite() for v in jet+[defect]):
            raise ArithmeticError('nonfinite explicit edge profile')
        return {'normalized_value_x_xx':[out(v) for v in jet],
                'normalized_rotation_defect':out(defect)}
    # Explicit first formal terms are evaluated independently of the Gaussian
    # integral. They are explanatory coefficients, without an asymptotic error.
    c1=derivatives[3]/(12*pi*pi)
    eta_bar=(1/(6*sp)+(1/(2*sp)+1/(sp-1))/2
             +old.alphap(sp)*(arb(1)/4+t/2)/2)
    c2mean=(derivatives[6]/(288*pi**4)
             +(1-t)*derivatives[2]/(16*pi*pi)
             +ii*(t/2-arb(1)/12)*derivatives[0]/(8*pi))
    explicit_first_terms={
        'C1_over_a':physical_profile_data(c1/a),
        'eta_bar_times_C0':physical_profile_data(eta_bar*derivatives[0]),
        'mean_C2_over_a_squared':physical_profile_data(c2mean/(a*a)),
        'scope':'Explicit formal terms with complete normalizer and profile derivatives; no asymptotic truncation allowance or exact-residual claim.'}
    def exact_log_gamma_factor(s):
        return s.log()+(s-1).log()-s*pi.log()/2-arb(16).log()+(s/2).lgamma()
    def finite_coefficients(u,order):
        ds={(0,0):acb(1)};cs=[derivatives[0]]
        for n in range(1,order+1):
            for k in range(0,3*n//2+1):
                m=3*n-2*k
                if m:
                    ds[n,k]=(ds.get((n-1,k),acb(0))/(4*m)
                        +(1-2*u)*ds.get((n-1,k-1),acb(0))/(2*m)
                        -(m+1)*ds.get((n-1,k-2),acb(0)))
                else:
                    ds[n,k]=-sum(((-1)**(k-j)*ds[n,j]
                        *math.factorial(2*k-2*j)/math.factorial(k-j)
                        for j in range(k)),acb(0))
            ck=sum(((pi/(2*ii))**j*ds[n,j]*derivatives[3*n-2*j]
                for j in range(0,3*n//2+1)),acb_series([acb(0)],3))/pi**(2*n)
            cs.append(ck/a**n)
        return cs
    rows=[]
    for order in range(5):
        started=time.monotonic();calls=[0];coeff=[]
        for j in range(3):
            def integrand(v,analytic):
                calls[0]+=1;u=arb(1)/2+t.sqrt()*v
                eta=exact_log_gamma_factor(sp+u)-m0base-u*gamma
                total=sum(finite_coefficients(u,order),acb_series([acb(0)],3))
                return (eta.exp()*total)[j]*(-v*v).exp()/pi.sqrt()
            coeff.append(acb.integral(integrand,-10,10,
                        rel_tol=arb(2)**-110,abs_tol=arb(2)**-110))
        discrepancy=acb_series(coeff,3)-derivatives[0]
        rows.append({'K':order,**physical_profile_data(discrepancy),
                     'quadrature_callbacks':calls[0],
                     'observed_seconds':time.monotonic()-started})
    return {'bits':bits,'t':'21/200','x':1000,'cutoff':8,
            'p':out(p[0]),'gaussian_interval':['-10','10'],
            'relative_and_absolute_quadrature_tolerance':'2^-110',
            'explicit_first_terms':explicit_first_terms,
            'finite_gaussian_hierarchy':rows,
            'scope':'Outward finite Gaussian integral enclosures for prescribed C0..CK expression and coherent x derivatives. Gaussian tails and RS_K omitted; not an enclosure for exact edge residual, no independent complete allowance.'}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--bits',nargs='+',type=int,choices=[192,256],default=[192,256])
    parser.add_argument('--execution-model',required=True)
    parser.add_argument('--execution-effort',required=True)
    args=parser.parse_args();repo=args.repo.resolve()
    pins=[EVALUATOR,COHERENT,
          INV/'symmetries/02_cutoff_reflection/numerics/S02_MATCHED_CORRECTION_20261019.json']
    result={'date':'2026-10-19','prepared_for':'Edward Baker',
        'actual_model':args.execution_model,'actual_effort':args.execution_effort,
        'llm_assistance':'substantial; same-model delegated derivation and internal checks',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'script_sha256':sha(__file__),
        'source_sha256':{str(path):sha(repo/path) for path in pins},
        'primary_sources':[
          {'url':'https://arxiv.org/html/1904.12438v2','locations':'Section 4 equations (35)-(41), Section 6.2 equations (48)-(57)'},
          {'url':'https://arxiv.org/html/2407.06681v1','locations':'Section 5 equations (20)-(24), especially C1 in (22)'},
          {'url':'https://arxiv.org/html/2201.00342','locations':'Section 3.6 equation (29), Section 3.17 equations (86)-(89); exact recurrence only, no implementation inequalities imported'}],
        'status':'Exact finite polynomial identities and explanatory finite Gaussian hierarchy; not a complete new arithmetic residual bound.',
        'unpaid':['Gaussian integral outside [-10,10]',
                  'Riemann-Siegel RS_K remainder',
                  'coherent complex-disk remainder constants and derivative allowances',
                  'whole B-box parameter coverage and signed spatial prefix allowance'],
        'source_theta_taylor_data_used':False,
        'exact_CR_identities':exact_cr_checks(),
        'runs':[run(repo,bits) for bits in args.bits]}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'exact_CR_count':result['exact_CR_identities']['count'],
                      'bits':args.bits,'status':result['status']}))

if __name__=='__main__':main()
