#!/usr/bin/env python3
"""Exact fixed-probe constants for the complete continuum response.

Prepared for Edward Baker, 2026-10-03, with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and reasoning effort not exposed.
Only standard-library rational polynomial arithmetic is used.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from hashlib import sha256
import json


def derivative(p):
    return [i*p[i] for i in range(1,len(p))] or [Q(0)]


def product(p,q):
    out=[Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]+=a*b
    return out


def integral(p):
    a=Q(1,4)
    return sum((c*(a**(i+1)-(-a)**(i+1))/Q(i+1)
                for i,c in enumerate(p)),Q(0))


def main():
    h=[Q(0)]*17
    for j in range(9):
        h[2*j]=Q(comb(8,j)*(-16)**j)
    h1=derivative(h)
    h2=derivative(h1)
    h3=derivative(h2)
    g0=[c/4 for c in h1]
    for i,c in enumerate(h3):
        g0[i]-=c
    g1=derivative(g0)
    q5=[Q(1)]
    for _ in range(5):
        q5=product(q5,[Q(1),Q(0),Q(-16)])
    factored=product(product([Q(0),Q(-64)],q5),
                     [Q(2689),Q(0),Q(-215072),Q(0),Q(256)])
    assert factored==g0
    nu=integral(product(g0,g0))
    n1=integral(product(h1,h1))
    n2=integral(product(h2,h2))
    ng1=integral(product(g1,g1))
    assert nu==Q(146640624550936576,37921101075)
    continuum=(n2+n1/4)/nu
    derivative_energy=ng1/nu+Q(1,4)
    assert continuum==Q(917180,580421327)
    assert integral(product(h1,h2))==0
    row={
        'date':'2026-10-03','prepared_for':'Edward Baker',
        'model':'GPT-6 (Codex)','serving_variant':'not exposed',
        'reasoning_effort':'not exposed',
        'llm_acknowledgement':'Prepared with substantial LLM assistance.',
        'status':'EXACT RATIONAL FIXED-PROBE CONSTANTS',
        'g0_norm_squared':str(nu),
        'h_prime_norm_squared':str(n1),
        'h_double_prime_norm_squared':str(n2),
        'g0_prime_norm_squared':str(ng1),
        'continuum_response_norm_squared':str(continuum),
        'continuum_response_norm_squared_decimal_diagnostic':float(continuum),
        'Dg_equals_normalized_g_prime_norm_squared_plus_one_quarter':str(derivative_energy),
        'Dg_decimal_diagnostic':float(derivative_energy),
        'cross_h_prime_h_double_prime_integral':'0',
        'factored_g0_matches_derivative_construction':True,
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'limitations':'Only exact fixed-profile constants. No prime discrepancy or global response bound is certified.'
    }
    (Path(__file__).parent/'continuum_record.json').write_text(json.dumps(row,indent=2)+'\n')
    print(json.dumps({k:row[k] for k in ['status','continuum_response_norm_squared','Dg_equals_normalized_g_prime_norm_squared_plus_one_quarter']}))


if __name__=='__main__':
    main()
