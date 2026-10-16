#!/usr/bin/env python3
"""Exact rational certificate of a deliberately broad filtered contraction.

Uses Gamma(1+w)>=exp(-gamma*w), pi<22/7, gamma<H_1000-log(1000),
and rational series enclosures for log and exp. No floating sign decision.
This certifies only w=1/10,L=1/2,ell^2=1/10, not an admissible removal path.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import math


def log_bounds(q, terms=64):
    q=F(q)
    k=0
    while q>=2:
        q/=2
        k+=1
    assert 1<=q<2
    def series(z):
        low=2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
        tail=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
        return low,low+tail
    a,b=series((q-1)/(q+1))
    c,d=series(F(1,3))
    return a+k*c,b+k*d


def exp_upper(q,terms=40):
    q=F(q)
    assert q>=0 and q<F(terms+2)
    partial=sum((q**j/F(math.factorial(j)) for j in range(terms+1)),F(0))
    first=q**(terms+1)/F(math.factorial(terms+1))
    return partial+first/(1-q/F(terms+2))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'records/ema-coarse-certificate-20260920.json')
    args=ap.parse_args()
    omega,L,ell2=F(1,10),F(1,2),F(1,10)
    gamma_upper=sum((F(1,j) for j in range(1,1001)),F(0))-log_bounds(1000)[0]
    log_pi_upper=log_bounds(F(22,7))[1]
    mh2_upper=exp_upper(2*omega*(log_pi_upper+gamma_upper))
    growth_upper=exp_upper((F(1,2)-omega)*L)
    upper=mh2_upper*(1+2*omega*L*growth_upper)**2/(1+2*ell2/(L*L))
    # Small outward rational bound for the record. Every inequality is exact.
    denominator=10**12
    numerator=(upper.numerator*denominator+upper.denominator-1)//upper.denominator
    ceiling=F(numerator,denominator)
    assert upper<=ceiling<F(1)
    result={'schema':1,'date':'2026-09-20','program':Path(__file__).name,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic':'Python Fraction; exact rational comparison; decimal display is not the sign decision',
        'parameters':{'L':'1/2','omega':'1/10','ell_squared':'1/10'},
        'upper_bound_squared_norm':{'numerator':numerator,'denominator':denominator,'decimal':float(ceiling)},
        'strictly_below_one':ceiling<1,'gamma_upper_display':float(gamma_upper),
        'method':'Reduced complete kernel L1 majorant times exact EMA norm bound; both pole contributions preserved by S10 cancellation.',
        'scope':'One all-input output-filtered contraction at a deliberately contaminating schedule point. No contraction of V inferred; no all-depth or removal certificate.'}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
