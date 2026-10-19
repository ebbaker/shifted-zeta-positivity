#!/usr/bin/env python3
"""S03-T1 identities and scoped split-prefix obstruction; no new allowance.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Actual authoring model/effort: gpt-6.1-sol / ultra. Internal checks only.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import flint
from flint import arb, acb, acb_series, ctx

INV=Path('papers/investigations-3/11_arithmetic_collision_rigidity')
LANE=INV/'symmetries/03_normalized_jet_rotation'

def A(x): return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def out(x): return x.str(38,more=True)
def check(c,msg):
    if not c: raise ArithmeticError(msg)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
    s=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def run(repo,bits):
    ctx.prec=bits;ctx.cap=8;ii=acb(0,1);pi=arb.pi();k=pi/8
    path=repo/INV/'symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py'
    t2=load(path,'coherent_full_'+str(bits));ev=t2.ClosedJetEvaluator(repo,bits);o=ev.old
    counts=dict(mode_symbol=0,source_kernel=0,correction_symbol=0,
                mode_heat_forcing=0,correction_heat_forcing=0)
    n1zero=True;bad_source=arb(0);bad_profile=arb(0)
    def contains_zero(x,msg):
        check(x.is_finite() and x.contains(0),msg)
    for tt in (F(1,100),F(21,200),F(1,5)):
        t=A(tt)
        for xx in (999,1000,1001):
            x=A(xx);z=acb_series([acb(x),acb(1)],3)
            ss=(1-ii*z)/2;s=(1-ii*acb(x))/2
            th,w,wp,b,bp,chi=ev.phase(x,t);mu=wp/w
            normal=o.normalizer(z,t);ee=(ii*th).exp()
            def RR(h): return h[0]+2*h[2]/w**2-wp*h[1]/w**3
            for n in range(1,9):
                ell=A(n).log()
                q=(-s*ell+t*(ell*ell-2*o.alpha(s)*ell)/4).exp()
                lam=ii*ell/2*(1+t*o.alphap(s)/2)
                lamp=t*ell*o.alphapp(s)/8
                sigma=lam*lam+lamp+(2*ii*w-mu)*lam
                qp=(-ss*ell+t*(ell*ell-2*o.alpha(ss)*ell)/4).exp()
                mode=(o.mt(ss,t)).exp()*qp/normal
                contains_zero(RR(mode)-ee*q*sigma/w**2,'mode symbol')
                counts['mode_symbol']+=1
                if n==1: check(sigma==0,'n=1 exact symbol');n1zero=n1zero and sigma==0
                # Compare physical x-series with an independently formed t-series.
                mode_phys=(o.m0(ss)-ss*ell+t*(o.alpha(ss)-ell)**2/4).exp()
                ts=acb_series([acb(t),acb(1)],2)
                mode_time=(o.m0(s)-s*ell+ts*(o.alpha(s)-ell)**2/4).exp()
                aa=o.alpha(s)-ell;beta=1+t*o.alphap(s)/2;B=aa*beta
                Bp=o.alphap(s)*beta+t*aa*o.alphapp(s)/2
                forcing=(aa*aa-B*B-Bp)/4*mode_time[0]
                contains_zero(mode_time[1]+2*mode_phys[2]-forcing,'mode heat forcing')
                counts['mode_heat_forcing']+=1
            # The source multiplier is formed BEFORE source integration.
            d=pi/8-4*A(1000).log()/1000
            for uu in (F(0),F(1,2),F(2)):
                v=acb(A(uu),d)
                g=(t*v*v+ii*z*v).exp()/normal
                Gamma=(ii*v-b)**2-bp-mu*(ii*v-b)+w*w
                expected=(t*v*v+ii*acb(x)*v).exp()/o.normalizer(acb(x),t)*Gamma/w**2
                contains_zero(RR(g)-expected,'filtered source kernel')
                counts['source_kernel']+=1
                if xx==1000 and tt==F(21,200) and uu==F(1,2):
                    bad_source=abs(expected-g[0]*(1-v*v/w**2)).lower()
            # Full profile derivatives, including both terms absent in frozen jets.
            J=o.J(z,t,8)[0]
            pref=-pi.sqrt()/4*(-k*z-k*k*t).exp()
            corr=pref*J/normal
            h=k+b
            bracket=2*J[2]-(2*h+mu)*J[1]+(h*h-bp+mu*h+w*w)*J[0]
            explicit=pref[0]/normal[0]*bracket/w**2
            contains_zero(RR(corr)-explicit,'full correction symbol')
            counts['correction_symbol']+=1
            ts=acb_series([acb(t),acb(1)],2)
            ct=-pi.sqrt()/4*(-k*acb(x)-k*k*ts).exp()*o.J(acb(x),ts,8)[0]
            cx=pref*J
            contains_zero(ct[1]+2*cx[2]-pref[0]*2*J[2],'correction heat forcing')
            counts['correction_heat_forcing']+=1
            if xx==1000 and tt==F(21,200):
                frozen=pref[0]/normal[0]*(h*h-bp+mu*h+w*w)*J[0]/w**2
                bad_profile=abs(explicit-frozen).lower()
    check(bad_source>0,'missing normalizer mutation undetected')
    check(bad_profile>0,'missing full profile derivatives mutation undetected')
    # Certified EXACT-POINT lower witness for any separate-prefix triangle rule.
    t=A(F(21,200));zs=[];witness=[]
    for xx in (999,1001):
        data=ev.jets(A(xx),t);f=data['full'];w=data['omega'];th=data['theta']
        W=acb(f[0],-f[1]/w);Z=(-ii*th).exp()*W;zs.append(Z)
        witness.append({'x':xx,'Z_full_approximation':out(Z),
                        'R_full_approximation':out(f[0]+f[2]/w**2-data['omega_x']*f[1]/w**3)})
    If=ii*(zs[1]-zs[0]);lower=abs(If).lower()
    check(lower>A('1.912087'),'split-prefix obstruction witness')
    # Exact controls exercise the physical filter, with their own equations.
    # At t=t_c: H=x^2, A=1, theta=x, f=2cos x. L H=x^2+2.
    xa=arb(-1);xe=arb(0)
    Z=lambda x:(-ii*x).exp()*acb(x*x,-2*x)
    Icontrol=ii*(Z(xe)-Z(xa))
    contains_zero(abs(Icontrol)-A(5).sqrt(),'heat polynomial collision endpoint')
    contains_zero(abs(Icontrol)-abs(Z(xa)),'collision cancels anchor exactly')
    for xc in (F(-1),F(-1,2),F(0)):
        xs=acb_series([acb(A(xc)),acb(1)],3)
        oscillator=2*xs.cos();polynomial=xs*xs
        contains_zero(oscillator[0]+2*oscillator[2],'oscillator filter annihilation')
        contains_zero(polynomial[0]+2*polynomial[2]-(A(xc)**2+2),
                      'polynomial physical filter')
    controls={'heat_polynomial_event':{'H':'x^2-2(t-t_c)','A':'1','theta':'x',
             'anchor':'-1','event':'0','filtered_H':'x^2+2','filtered_f':'0',
             'integral_modulus_at_event':out(abs(Icontrol)),
             'direct_series_filter_checks':3,
             'strict_anchor_preservation_fails':True},
             'oscillator':{'H':'2cos(x)','filtered_H':'0 identically',
                          'direct_series_filter_checks':3,
                          'comment':'Annihilation is an identity, not arithmetic exclusion.'}}
    return {'bits':bits,'checks':counts,'n1_symbol_exactly_zero':bool(n1zero),
            'mutation_separations':{'missing_normalizer_terms_lower':out(bad_source),
                                    'dropping_profile_derivatives_lower':out(bad_profile)},
            'split_prefix_witness':{'t':'21/200','anchor':999,'endpoint':1001,
                 'endpoints':witness,'I_full_approximation':out(If),
                 'modulus':out(abs(If)),'certified_lower':out(lower),
                 'rule':'Any B_Q >= |I_Q|, B_f >= |I_f| gives B_Q+B_f >= |I_f| > 1.912087.',
                 'scope':'Separate source/approximation prefix triangle rules only; not a residual lower bound.'},
            'controls':controls}

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    p.add_argument('--bits',type=int,nargs='+',default=[192,256])
    p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True)
    a=p.parse_args();repo=a.repo.resolve()
    paths=[INV/'symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py',
           INV/'symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py',
           INV/'symmetries/02_cutoff_reflection/numerics/S02_MATCHED_CORRECTION_20261019.json',
           INV/'numerics/high_height_consumer/high_height_consumer.py',
           INV/'manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex']
    result={'date':'2026-10-19','prepared_for':'Edward Baker',
            'actual_model':a.execution_model,'actual_effort':a.execution_effort,
            'llm_assistance':'substantial; same-model derivation and delegated internal audit',
            'python':platform.python_version(),'python_flint':flint.__version__,
            'script_sha256':sha(__file__),'source_sha256':{str(v):sha(repo/v) for v in paths},
            'status':'Exact derivation support and scoped separate-prefix obstruction; no new complete residual allowance.',
            'domain':'B=[1/100,1/5] x [999,1001]; identities analytic where branches and A*omega are admissible; witness point only.',
            'source_integral_evaluated':False,
            'runs':[run(repo,b) for b in a.bits]}
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(a.output),'runs':len(result['runs']),
                      'split_prefix_lower':[r['split_prefix_witness']['certified_lower'] for r in result['runs']]}))

if __name__=='__main__': main()
