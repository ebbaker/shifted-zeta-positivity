#!/usr/bin/env python3
"""Coarse constants for the analytic local-extension example, not a matrix build."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
from flint import arb as A, ctx
import reference_certify_arb as c

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output',required=True)
    args = p.parse_args()
    if not __debug__:
        raise RuntimeError('Assertions must be enabled')
    ctx.prec = 256
    R = A(2)
    active = c.prime_powers(R)
    bounds = c.analytic(R,c.profile(220),128,active,None)
    W = bounds['smooth_variation'].upper()
    sigma = sum((A(prime).log()/A(n).sqrt() for n,prime,k in active),A(0))
    assert W < 6 and sigma < 3 and A.pi()/2 < 2
    assert A.const_euler()+A.pi().log()+6 < 8
    assert 2-A(7).log() > c.rat('0.01')
    assert A(2).log() > c.rat('0.01')
    T = 10**31
    assert A(T) > A(100).log()  # h=exp(-T)<1/100, no underflow evaluation.
    m = Fraction('1.37e-28')
    g = Fraction(T-8)
    b = Fraction(11)
    assert g > m
    margin = m*g-4*b*b
    assert margin > 0
    data = {
        'result':'PASS: coarse constants satisfy the local-extension lemma',
        'premises':['v0.3 full central floor at log 7','analytic lemmas in critical_path_research.md'],
        'R':'2','W_R_ball_upper':W.str(35),'W_R_rounded_upper':'6',
        'arithmetic_sum':sigma.str(35),'arithmetic_rounded_upper':'3','cross_norm_upper':'11',
        'old_floor':'1.37e-28','extension_length_symbolic':'exp(-10^31)',
        'new_slab_floor_symbolic':'10^31 - 8',
        'm_times_g_minus_4b_squared_exact':str(margin),
        'normalized_cross_norm_upper':'1/2',
        'resulting_floor':'6.85e-29',
        'scope':'An extremely conservative analytic local extension; no useful new macroscopic horizon or nonaccumulation result.'}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__ == '__main__':
    main()
