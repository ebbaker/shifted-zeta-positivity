#!/usr/bin/env python3
"""Replay scalar constants and the finite arithmetic heat-Stirling ledger.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
This checks the companion written proof's elementary constants, then consumes
its relative mode-error and Cauchy-derivative bounds. It does not numerically
prove that theorem, evaluate exact Gaussian quadrature, or bound the RS edge
or the complete physical-source residual.
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
import sys
sys.dont_write_bytecode = True
import flint
from flint import arb, acb, ctx

INV = Path('papers/investigations-3/11_arithmetic_collision_rigidity')
MODE_SOURCE = INV/'symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py'
SYMBOL_NOTE = INV/'symmetries/03_normalized_jet_rotation/notes/03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md'

def A(value):
    return arb(value.numerator)/value.denominator if isinstance(value,F) else arb(value)
def out(value):return value.str(38,more=True)
def interval(lo,hi):
    lo,hi=A(lo),A(hi)
    return arb((lo+hi)/2,((hi-lo)/2).upper())
def check(condition,message):
    if not condition:raise ArithmeticError(message)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module

def scalar_checks():
    pi=arb.pi();moments={}
    for j in range(1,7):
        moments[j]=sum((A(math.comb(j,k))*A('.2')**A(F(k,2))
            *A('.235')**(j-k)*A(F(k+1,2)).gamma()/pi.sqrt()
            for k in range(j+1)),A(0))
    aa,bb,cc=A('.000351'),A('.00051'),A('3.75e-7')
    c1,c0=1/(6*A('494.5')*476),A('9.3e-10')
    h2=(aa*aa+bb*bb*moments[4]+cc*cc*moments[6]
        +2*aa*bb*moments[2]+2*aa*cc*moments[3]+2*bb*cc*moments[5])
    first=c1*moments[1]+cc*moments[3]+c0
    alpha_real_lower=(A('494.5')/(2*pi)).log()/2-A('1.5')/A('494.5')
    alpha_imag_abs=pi/4+A('5.5')/A('494.5')/2+A('1.5')/A('494.5')
    numbers={
        's_upper':(A('500.5')**2+A('.5')**2).sqrt()+5,
        'alpha_abs':(((A('505.6')/(2*pi)).log()/2+A('1.5')/A('494.5'))**2
            +alpha_imag_abs**2).sqrt(),
        'alpha_imag_abs':alpha_imag_abs,
        'delta_max':A('.2').sqrt()*40+A('.235'),
        'alpha_prime':1/(2*A('494.5'))+A('1.5')/A('494.5')**2,
        'alpha_second':A(3)/476**3+A('.5')/476**2,
        'stirling_R3':(A('1.619')/2).cos()**-4/(45*A(476)**3),
        'h_max':aa+bb*A('18.2')**2+cc*A('18.2')**3,
        'first_error_moment':first,
        'h2_moment':h2,
        'exp_hmax':A('.172').exp(),
        'central_bound':first+A('.172').exp()*h2/2,
        'exact_tail_bound':2*(450-A('.86')*40**2).exp()/(2*A('.86')*40*pi.sqrt()),
        'poly_tail_initial_log':((507+A('.45')*40)**2/16).log(),
        'non_gamma_tail_initial_log':(6+A('.45')*40)*pi.log()/2+A('2.35')*(A('.235')+A('.45')*40),
    }
    caps={
        's_upper':'505.6','alpha_abs':'2.35','alpha_imag_abs':'.8','delta_max':'18.2',
        'alpha_prime':'.00102','alpha_second':'2.25e-6',
        'stirling_R3':'9.3e-10','h_max':'.172','first_error_moment':'4.14e-7',
        'h2_moment':'2.56e-7','exp_hmax':'1.188','central_bound':'5.7e-7',
        'exact_tail_bound':'1e-300','poly_tail_initial_log':'16',
        'non_gamma_tail_initial_log':'64',
    }
    checks={key:bool(value<A(caps[key]))for key,value in numbers.items()}
    lower_m0=(2*A('494.5').log()+A('.5')*(2*pi).log()-A(16).log()
        -A('2.75')*(A('505.6')/2).log()
        -A('505.5')/2*(pi/2+A('5.5')/A('494.5'))
        -A('2.75')-A('2.75')*pi.log())
    checks['m0_lower_above_minus420']=bool(lower_m0>-420)
    checks['alpha_real_lower_exceeds_log8']=bool(alpha_real_lower>A(8).log())
    moment_caps={1:'.488',2:'.275',3:'.177',4:'.128',5:'.102',6:'.089'}
    for j,value in moments.items():checks[f'moment_{j}']=bool(value<A(moment_caps[j]))
    check(all(checks.values()),'scalar proof constant failed: '+str(checks))
    return {'all_checks_pass':True,'values':{k:out(v)for k,v in numbers.items()},
        'caps':caps,'moments':{str(j):out(v)for j,v in moments.items()},
        'moment_caps':{str(j):v for j,v in moment_caps.items()},
        'm0_lower':out(lower_m0),'alpha_real_lower':out(alpha_real_lower),
        'log8':out(A(8).log()),'checks':checks}

def finite_mode_ledger(repo,bits):
    o=load(repo/MODE_SOURCE,'heat_stirling_modes_'+str(bits))
    x=interval(999,1001);t=interval(F(1,100),F(1,5));ii=acb(0,1)
    s=(1-ii*acb(x))/2
    mp=lambda v:o.alpha(v)*(1+t*o.alphap(v)/2)
    mpp=lambda v:o.alphap(v)*(1+t*o.alphap(v)/2)+t*o.alpha(v)*o.alphapp(v)/2
    omega=(-(mp(s)+mp(1-s))/4).real
    omega_x=(ii*(mpp(s)-mpp(1-s))/8).real
    b=(-ii*(mp(s)-mp(1-s))/4).real
    b_x=(-(mpp(s)+mpp(1-s))/8).real
    check(omega<0 and omega.abs_lower()>0,'nonzero oriented phase derivative')
    mu=omega_x/omega;beta=1+t*o.alphap(s)/2
    e0,e1,e2=A('6e-7'),A('6e-8'),A('1.2e-8')
    rows=[];value=A(0);normal_x=A(0);normal_xx=A(0)
    physical_x=A(0);physical_xx=A(0);filtered=A(0)
    for n in range(1,9):
        ell=A(n).log()
        logp=-s*ell+t*(ell*ell-2*o.alpha(s)*ell)/4
        amplitude=logp.real.exp().upper()
        lam=ii*ell*beta/2;lam_x=t*ell*o.alphapp(s)/8
        sigma=lam*lam+lam_x+(2*ii*omega-mu)*lam
        normal_rate=ii*omega+lam;normal_accel=normal_rate*normal_rate+ii*omega_x+lam_x
        physical_rate=b+normal_rate;physical_accel=physical_rate*physical_rate+b_x+ii*omega_x+lam_x
        rate=2*ii*omega+2*lam-mu
        errors={
            'normalized_value':2*amplitude*e0,
            'normalized_x':2*amplitude*(abs(normal_rate).upper()*e0+e1),
            'normalized_xx':2*amplitude*(abs(normal_accel).upper()*e0+2*abs(normal_rate).upper()*e1+e2),
            'physical_x_over_A':2*amplitude*(abs(physical_rate).upper()*e0+e1),
            'physical_xx_over_A':2*amplitude*(abs(physical_accel).upper()*e0+2*abs(physical_rate).upper()*e1+e2),
            'normalized_filtered':2*amplitude/omega.abs_lower()**2*(abs(sigma).upper()*e0+abs(rate).upper()*e1+e2),
        }
        for key,v in errors.items():check(v.is_finite() and v>=0,'finite positive error '+key)
        if n==1:check(sigma==0,'n=1 exact zero symbol')
        value+=errors['normalized_value'];normal_x+=errors['normalized_x'];normal_xx+=errors['normalized_xx']
        physical_x+=errors['physical_x_over_A'];physical_xx+=errors['physical_xx_over_A'];filtered+=errors['normalized_filtered']
        rows.append({'n':n,'mode_amplitude_over_A_upper':out(amplitude),
            'sigma_modulus_upper':out(abs(sigma).upper()),
            'filtered_derivative_coefficient_modulus_upper':out(abs(rate).upper()),
            'errors':{key:out(v.upper())for key,v in errors.items()}})
    totals={'normalized_value':value,'normalized_x':normal_x,'normalized_xx':normal_xx,
        'physical_x_over_A':physical_x,'physical_xx_over_A':physical_xx,
        'normalized_filtered':filtered}
    return {'domain':{'t':['1/100','1/5'],'x':['999','1001']},
        'cover':'one outward interval image of the full real box; eight arithmetic modes; two conjugate channels',
        'relative_mode_error_inputs':{'value':'6e-7','x':'6e-8','xx':'1.2e-8',
            'status':'Inputs from companion written bounded heat-Stirling proof; scalar checks support its constants.'},
        'normalizer':{key:out(v)for key,v in {'omega':omega,'omega_x':omega_x,'mu':mu,'b':b,'b_x':b_x}.items()},
        'formula':'2/|omega|^2 sum_n |p_n| (|sigma_n|e0+|2i omega+2lambda_n-mu|e1+e2)',
        'totals':{key:out(v.upper())for key,v in totals.items()},'modes':rows,
        'scope':'Certified finite-mode remainder payments conditional only on the companion proved mode-error bounds; no RS-edge or complete-H residual bound.'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--bits',type=int,nargs='+',default=[192,256])
    parser.add_argument('--execution-model',required=True);parser.add_argument('--execution-effort',required=True)
    args=parser.parse_args();repo=args.repo.resolve();runs=[]
    check(all(bits in (192,256)for bits in args.bits),'supported replay precisions: 192,256')
    for bits in args.bits:
        ctx.prec=bits
        runs.append({'bits':bits,'scalar_checks':scalar_checks(),'finite_mode_ledger':finite_mode_ledger(repo,bits)})
    result={'date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
        'actual_model':args.execution_model,'actual_effort':args.execution_effort,
        'llm_assistance':'substantial; same-model derivation and internal review; no independent specialist review',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'script_sha256':sha(__file__),'source_sha256':{str(path):sha(repo/path)for path in (MODE_SOURCE,SYMBOL_NOTE)},
        'scope':'Bounded heat-Stirling scalar constant replay and finite arithmetic-mode remainder ledger only. No exact Gaussian quadrature, RS-edge or complete physical residual estimate.',
        'runs':runs}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'runs':len(runs),
        'all_scalar_checks_pass':True,'totals':[r['finite_mode_ledger']['totals']for r in runs]}))

if __name__=='__main__':main()
