#!/usr/bin/env python3
"""Independent complete-jet enclosures for the six fixed audit observations.

Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol, effort ultra, 16 October 2026.
Requires python-flint; no inherited numerical solver is imported.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
import time
from pathlib import Path
import flint
from flint import arb, acb, ctx

CASES = [('0','30'),('0','44.1303'),('0.25','44.1303'),
         ('0','60'),('0','70'),('0','85')]

def ball(x):
    return x.str(120, more=True)

def coefficient_tail(start, j):
    """Uniform t<=1/4, any real x, sum_{n>=start}|d_x^j H_n|."""
    lam=arb.pi()*start*start
    first=2*lam*lam*(-lam).exp()/(4*lam-9)**(j+1)
    ratio=(arb(start+1)/start)**4*(-arb.pi()*(2*start+1)).exp()
    assert ratio<1
    return first/(1-ratio)

def integral_tail(n,j,t,U):
    """Positive majorant on [U,infty) after expansion about U."""
    lam=arb.pi()*n*n
    q=lam*(4*U).exp()
    rate=4*q-9-2*t*U
    assert rate>0 and 8*q>t
    height=2*lam*lam*(9*U+t*U*U-q).exp()
    return height/rate if j==0 else height*(U/rate+1/rate**2)

def run(bits, output, max_seconds):
    started=time.monotonic();ctx.prec=bits; U=arb(9)/5
    result={'schema':'source_measurement_ball_evaluation_v1',
            'date':'2026-10-16','prepared_for':'Edward Baker',
            'model':'gpt-6.1-sol','reasoning_effort':'ultra',
            'llm_assistance':'Substantial LLM assistance; validated quadrature and analytic tails.',
            'python_version':platform.python_version(),
            'python_flint_version':flint.__version__,'precision_bits':bits,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract':{'cases':CASES,'source_nodes_integrated':10,
                        'upper_integration_endpoint':'9/5',
                        'rel_tol_scaled':'1e-95','abs_tol_scaled':'1e-100',
                        'max_seconds':max_seconds},
            'beta':[ball((4*arb.pi()*n*n-1)*(-arb.pi()*n*n).exp()) for n in range(1,7)],
            'coefficient_tail_after_10':[ball(coefficient_tail(11,j)) for j in (0,1)],
            'cases':[]}
    for ts,xs in CASES:
        t,x=arb(ts),arb(xs);cols=[[],[]];scaled=[[],[]];tail_values=[[],[]]
        for n in range(1,11):
            lam=arb.pi()*n*n
            for j in (0,1):
                if time.monotonic()-started>max_seconds: raise TimeoutError('fixed replay budget reached')
                def f(u,analytic):
                    e=(4*u).exp();q=lam*e
                    z=(t*u*u+u-lam*(e-1)).exp()*(2*q*q-3*q)
                    return z*(x*u).cos() if j==0 else -u*z*(x*u).sin()
                z=acb.integral(f,0,U,rel_tol=arb('1e-95'),abs_tol=arb('1e-100'),
                               eval_limit=150000,depth_limit=35)
                if not(z.is_finite() and z.imag.contains(0)):
                    raise ArithmeticError(('nonfinite quadrature',ts,xs,n,j))
                tail=integral_tail(n,j,t,U)
                value=z.real*(-lam).exp()+arb(0,tail.upper())
                cols[j].append(value);scaled[j].append(z.real);tail_values[j].append(tail)
            print('enclosed',ts,xs,n,flush=True)
        h=[sum(cols[j],arb(0))+arb(0,coefficient_tail(11,j).upper()) for j in (0,1)]
        result['cases'].append({'id':f't{ts}_x{xs}','t':ts,'x':xs,
                                'B':[[ball(v) for v in row[:6]] for row in cols],
                                'columns_through_10':[[ball(v) for v in row] for row in cols],
                                'scaled_columns_through_10':[[ball(v) for v in row] for row in scaled],
                                'h':[ball(v) for v in h],
                                'theta_tail_after_6':[ball(sum(cols[j][6:],arb(0))+arb(0,coefficient_tail(11,j).upper())) for j in (0,1)],
                                'integration_tail_bounds':[[ball(v) for v in row] for row in tail_values]})
        result['elapsed_seconds']=time.monotonic()-started
        output.write_text(json.dumps(result,indent=2)+'\n')
        print('case complete',ts,xs,'elapsed',result['elapsed_seconds'],flush=True)
    print('complete',output,'elapsed',time.monotonic()-started,flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bits',type=int,default=448)
    parser.add_argument('--max-seconds',type=int,default=1800)
    parser.add_argument('--output',type=Path,required=True)
    a=parser.parse_args();run(a.bits,a.output,a.max_seconds)
