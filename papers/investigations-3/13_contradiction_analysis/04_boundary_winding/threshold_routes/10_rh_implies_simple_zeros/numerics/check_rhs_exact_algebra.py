#!/usr/bin/env python3
"""Replay the fixed algebra contract; no theta quadrature or zero scan.
Prepared for Edward Baker, 2026-10-20; LLM gpt-6-astra, effort ultra.
"""
from fractions import Fraction as F
from math import factorial, comb
import hashlib
import json
from pathlib import Path


def mul(a, b):
    out = {}
    for j, v in a.items():
        for k, w in b.items():
            out[j+k] = out.get(j+k, F(0)) + v*w
    return out


def deriv(a):
    return {j-1: j*v for j, v in a.items() if j}


def shifted(a, center):
    out = {}
    for j, v in a.items():
        for k in range(j+1):
            out[k] = out.get(k, F(0)) + v*comb(j,k)*center**(j-k)
    return out


def heat(a, s):
    out = {}
    for j, v in a.items():
        for k in range(j//2+1):
            out[j-2*k] = out.get(j-2*k, F(0)) + (
                v*F(factorial(j), factorial(k)*factorial(j-2*k))*(-s)**k)
    return out


def gaussian(a, s):
    return sum((v*F(factorial(j),factorial(j//2))*s**(j//2)
                for j,v in a.items() if j%2 == 0), F(0))


def direct_deficit(a, s):
    cap = heat(a, s)
    dcap = deriv(cap)
    return s*gaussian(mul(dcap,dcap),s)-gaussian(mul(cap,cap),s)


def hermite_deficit(a, s):
    return sum((F(j-2,2)*(2*s)**j*factorial(j)*v*v
                for j,v in a.items()),F(0))


def run():
    counts = {}
    for m in range(2,13):
        a = {m:F(1)}
        s = F(3,7)
        expected = F(m-2,2)*(2*s)**m*factorial(m)
        assert direct_deficit(a,s) == hermite_deficit(a,s) == expected
    counts['heat_monomials'] = 11
    fixture_values = []
    for a in map(F,(1,2,3)):
        polynomial = {4:F(1),2:-2*a*a,0:a**4}
        local = shifted(polynomial,a)
        assert local[0] == local[1] == 0
        h2 = 2*local[2]
        h3 = 6*local[3]
        h4 = 24*local[4]
        L = h3/(3*h2)
        S = L*L-h4/(6*h2)
        assert S == F(1,2)/(a*a)
        for divisor in (16,8,4):
            s = a*a/divisor
            direct = direct_deficit(local,s)
            low_modes = h2*h2*(6*s**3*L*L+24*s**4*(L*L-S)**2)
            floor = 6*s**4*h2*h2/a**4
            assert direct == hermite_deficit(local,s) == low_modes
            assert direct >= floor
            fixture_values.append({'a':str(a),'s':str(s),'D':str(direct),'lower_bound':str(floor)})
    counts['double_event_fixtures'] = len(fixture_values)
    equality = 0
    for j in range(1,36):
        for k in range(1,8):
            N=F(j,k)
            n=N.numerator//N.denominator
            finite=(2/N)*(1+2*sum((1-F(r)/N for r in range(1,n+1)),F(0)))
            fraction=N-n
            closed=2*(1+fraction*(1-fraction)/(N*N))
            assert finite == closed and closed >= 2
            assert (closed == 2) == (N.denominator == 1)
            equality += closed == 2
    counts['fejer_control_rationals'] = 245
    counts['integer_equality_cases'] = equality
    return {'status':'all exact checks passed','arithmetic':'fractions.Fraction',
            'scope':'finite algebra only; no theta zero certificate or proof of asymptotic estimates',
            'counts':counts,'double_event_fixtures':fixture_values}

if __name__ == '__main__':
    result=run()
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['contract_sha256']=hashlib.sha256(Path(__file__).with_name('EXACT_ALGEBRA_CONTRACT_20261020.md').read_bytes()).hexdigest()
    print(json.dumps(result,indent=2,sort_keys=True))
