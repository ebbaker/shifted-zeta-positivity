#!/usr/bin/env python3
"""Fixed probe continuum bound via published finite-height RH and a zero tail.

Prepared for Edward Baker, 2026-10-03, with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and reasoning effort not exposed.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial, isqrt
from pathlib import Path
import json
import platform
import time
import flint
from flint import arb,ctx

DIAGONAL_SHA256='643456713dbbb3001c03ab4e1b4978fedd34fd7233c9ba1a6a2a2057889bf49a'
def ab(q):
    q=F(q)
    return arb(q.numerator)/q.denominator

def pack(x):
    if not x.is_finite(): raise ArithmeticError('non-finite interval')
    return {'lower':str(x.lower().fmpq()),'upper':str(x.upper().fmpq())}

def deriv(p,n=1):
    for _ in range(n):p=[i*p[i] for i in range(1,len(p))]
    return p

def val(p,x):
    return sum((c*x**j for j,c in enumerate(p)),F(0))

def l2sq(p):
    a=F(1,4)
    return sum((c*d*(a**(j+k+1)-(-a)**(j+k+1))/(j+k+1)
                for j,c in enumerate(p) for k,d in enumerate(p)),F(0))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bits',type=int,choices=[192,256],required=True)
    parser.add_argument('--diagonal',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();start=time.monotonic();ctx.prec=args.bits
    raw=args.diagonal.read_bytes()
    if sha256(raw).hexdigest()!=DIAGONAL_SHA256:
        raise ArithmeticError('Earlier diagonal certificate hash mismatch')
    prior=json.loads(raw)
    if prior['status']!='CERTIFIED_FIVE_TWO_SOURCE_GRAMS_ONLY':
        raise ArithmeticError('Unexpected earlier certificate status')
    q_upper=F(prior['Q_diagonal']['upper'])
    if not q_upper<F('1.46694003100529'):
        raise ArithmeticError('Claimed earlier diagonal upper bound fails')
    h=[F(0)]*17
    for j in range(9):h[2*j]=F(comb(8,j)*(-16)**j)
    g=[c/4 for c in deriv(h)]
    for j,c in enumerate(deriv(h,3)):g[j]-=c
    for k in range(5):
        if val(deriv(g,k),F(1,4))!=0 or val(deriv(g,k),F(-1,4))!=0:
            raise ArithmeticError('A lower distributional derivative has an atom')
    boundary=abs(val(deriv(g,5),F(1,4)))+abs(val(deriv(g,5),F(-1,4)))
    if boundary!=2*factorial(8)*8**8:raise ArithmeticError('Boundary atom mismatch')
    nu=l2sq(g);nu6=l2sq(deriv(g,6));half=nu6/2
    ceilroot=isqrt(half.numerator//half.denominator)+1
    if not F((ceilroot-1)**2)<=half<F(ceilroot**2):
        raise ArithmeticError('Integer square-root bracket fails')
    B=boundary+ceilroot;K2=B*B/nu
    if nu!=F(prior['source_exact_norm_squared_unnormalized']):
        raise ArithmeticError('Source normalization mismatch')
    T=arb(3)*10**12
    delta=24*(arb(1)/4).exp()*ab(K2)*T**(-11)*(T.log()/11+arb(1)/121)
    rmax=arb(500);rmin=arb(2);ell=arb(1)/2
    tailcost=delta*(1+(rmax/2).exp())
    arch=ell*(-arb(5)/2*(rmin-ell)).exp()/(1-(-2*(rmin-ell)).exp())
    bound=ab(q_upper)+tailcost+arch
    if not delta<ab('1.058e-116'):raise ArithmeticError('Tail constant bound fails')
    if not tailcost<ab('3.961e-8'):raise ArithmeticError('Horizon tail cost fails')
    if not arch<ab('0.01237498726501953'):raise ArithmeticError('Archimedean bound fails')
    if not bound<ab('1.47931505787654'):raise ArithmeticError('Tight continuum bound fails')
    if not bound<ab('1.48'):raise ArithmeticError('Continuum bound 1.48 fails')
    record={
        'status':'CERTIFIED_CONTINUUM_ABSOLUTE_BOUND_LT_1_48_ON_2_TO_500',
        'date':'2026-10-03','model':'GPT-6 (Codex)',
        'serving_variant':'not exposed','reasoning_effort':'not exposed',
        'bits':args.bits,'source_norm_squared':str(nu),
        'interior_sixth_derivative_norm_squared':str(nu6),
        'boundary_atom_total_variation':str(boundary),
        'interior_L1_upper_integer':ceilroot,
        'sixth_distributional_derivative_TV_upper_integer':str(B),
        'K_squared':str(K2),
        'published_RH_verified_height':'3000000000000',
        'zero_count_majorant':'N(t) <= t log(t), t >= 100',
        'delta_T':pack(delta),'horizon_tail_cost':pack(tailcost),
        'archimedean_remainder_bound_at_2':pack(arch),
        'imported_Q_upper':str(q_upper),'continuum_absolute_bound':pack(bound),
        'interval_r':['2','500'],'diagonal_certificate_sha256':DIAGONAL_SHA256,
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'seconds':time.monotonic()-start,
        'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,
                   'flint':flint.__FLINT_VERSION__},
        'limitations':[
            'Published finite-height RH theorem and explicit-formula proof are inputs, not rerun here.',
            'No primes or individual zero ordinates are enumerated.',
            'The bound 1.48 exceeds Q[g]; it proves neither global growth nor exact pairwise positivity.',
            'The high-zero tail grows exponentially with the separation at fixed verification height.']}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':record['status'],'bits':args.bits,
          'delta_T':str(delta),'tailcost':str(tailcost),'arch_at_2':str(arch),
          'bound':str(bound),'seconds':record['seconds']}))
if __name__=='__main__':main()
