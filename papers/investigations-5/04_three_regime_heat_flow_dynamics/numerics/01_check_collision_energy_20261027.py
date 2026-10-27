#!/usr/bin/env python3
"""Bounded exact-rational checks for CE Notes09-10; no theta evaluation.

Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra (Codex), effort max, 27 October 2026.
Uses only the Python standard library; expected runtime below 10 seconds.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p or [F(0)]


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += v
    return trim(out)


def scale(a, c): return trim([v*c for v in a])
def sub(a, b): return add(a, scale(b, -1))


def mul(a, b):
    out = [F(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return trim(out)


def derivative(a): return trim([i*a[i] for i in range(1, len(a))])


def divmod_poly(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    q = [F(0)] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        k, c = len(a)-len(b), a[-1]/b[-1]
        q[k] += c
        a = sub(a, [F(0)]*k + scale(b, c))
    return trim(q), trim(a)


def mod(a, b): return divmod_poly(a, b)[1]


def inverse_mod(a, p):
    old_r, r, old_s, s = p, a, [F(0)], [F(1)]
    while r != [0]:
        q, rem = divmod_poly(old_r, r)
        old_r, r = r, rem
        old_s, s = s, sub(old_s, mul(q, s))
    assert len(old_r) == 1 and old_r[0] != 0
    return mod(scale(old_s, 1/old_r[0]), p)


def heat(n, s):
    out = [F(0)]*(n+1)
    for k in range(n//2+1):
        out[n-2*k] = F(factorial(n), factorial(k)*factorial(n-2*k))*(-s)**k
    return trim(out)


def root_power_sums(p, count):
    m = len(p)-1
    assert p[-1] == 1
    a = [F(1)] + [p[m-k] for k in range(1,m+1)]
    out = [F(m)]
    for k in range(1,count+1):
        if k <= m:
            out.append(-sum(a[j]*out[k-j] for j in range(1,k))-k*a[k])
        else:
            out.append(-sum(a[j]*out[k-j] for j in range(1,m+1)))
    return out


def trace_mod(poly, p):
    z = mod(poly, p)
    ps = root_power_sums(p, len(z)-1)
    return sum(v*ps[i] for i,v in enumerate(z))


def run():
    records = []
    for m in range(2,13):
        for s in [F(-1),F(1),F(3,2),F(4)]:
            p, p1, p2 = heat(m,s), heat(m+1,s), heat(m+2,s)
            dp, ddp = derivative(p), derivative(derivative(p))
            assert mod(add(p1,scale(dp,2*s)),p) == [0]
            assert derivative(p1) == scale(p,m+1)
            assert mod(sub(scale(ddp,2*s),mul([0,1],dp)),p) == [0]
            # Independent alpha^2 and beta coefficients of the second root correction.
            alpha2 = sub(add(scale(ddp,2*s*s),scale(derivative(p1),2*s)),
                         scale(mul([0,1],dp),s))
            beta = add(p2,scale(mul([0,1],dp),2*s))
            assert mod(alpha2,p) == [0] and mod(beta,p) == [0]
            ratio = mod(mul(ddp,inverse_mod(dp,p)),p)
            energy = trace_mod(mul(ratio,ratio),p)/8
            expected = F(m*(m-1),16)/s
            assert energy == expected
            if s == 1:
                assert root_power_sums(p,2)[2] == 2*m*(m-1)
            records.append({'m':m,'s':str(s),'inverse_square_energy':str(energy)})

    # Generic rational root configurations and a nonconstant exterior force.
    exterior_records = []
    for m in range(2,9):
        x = [F(i*i+2*i-3,3) for i in range(m)]
        S = [sum(1/(x[i]-x[j]) for j in range(m) if i!=j) for i in range(m)]
        b = [F(1,3)+F(2,5)*z-F(3,7)*z*z for z in x]
        velocity = [2*S[i]+2*b[i] for i in range(m)]
        E = sum(1/(x[i]-x[j])**2 for i in range(m) for j in range(i+1,m))
        B = sum((b[i]-b[j])/(x[i]-x[j]) for i in range(m) for j in range(i+1,m))
        dlogD = 2*sum((velocity[i]-velocity[j])/(x[i]-x[j])
                     for i in range(m) for j in range(i+1,m))
        assert dlogD == 8*E+4*B
        assert B != 0 and dlogD != 8*E
        exterior_records.append({'m':m,'E':str(E),'B':str(B),'dlogD':str(dlogD)})

    # Stationary sine roots (spacing one) require precisely the omitted-root force.
    for x in [[F(0),F(1)],[F(-1),F(0),F(1)]]:
        m=len(x)
        S=[sum(1/(x[i]-x[j]) for j in range(m) if i!=j) for i in range(m)]
        E=sum(1/(x[i]-x[j])**2 for i in range(m) for j in range(i+1,m))
        B=sum((-S[i]+S[j])/(x[i]-x[j]) for i in range(m) for j in range(i+1,m))
        assert 8*E+4*B == 0

    # Cubic numerator Q=(a1^2-3a2)^2 at non-symmetric exact root sets.
    for x in [[F(-3),F(2),F(7)],[F(-5,3),F(1,7),F(12,5)]]:
        gaps=[(x[i]-x[j])**2 for i in range(3) for j in range(i+1,3)]
        Q=sum(gaps[i]*gaps[j] for i in range(3) for j in range(i+1,3))
        a1=-sum(x); a2=sum(x[i]*x[j] for i in range(3) for j in range(i+1,3))
        assert Q == (a1*a1-3*a2)**2

    # Positive atomic threshold: solve the small zero via y^2=v(u).
    v=[F(0),F(2),F(-10,3)]
    v2=mul(v,v)
    cos_y=add(sub([1],scale(v,F(1,2))),scale(v2,F(1,24)))
    cos_2y=add(sub([1],scale(v,2)),scale(v2,F(2,3)))
    exp_3u=[F(1),F(3),F(9,2)]
    residual=sub(mul(exp_3u,cos_2y),cos_y)
    assert residual[:3] == [0,0,0]
    gamma=F(-5,6); kappa=F(1,8)
    assert -2*kappa*gamma == F(5,24)
    assert -6*kappa*gamma == F(5,8)
    assert F(3*2,16) == F(3,8)
    return {
        'status':'passed',
        'scope':'exact rational finite algebra; no theta source evaluation, interval certificate, or independent review',
        'model':'gpt-6-astra','effort':'max','date':'2026-10-27',
        'hermite_cases':records,'nonzero_exterior_cases':exterior_records,
        'additional_checks':['stationary sine exterior cancellation for m=2,3',
                             'cubic Q polynomial on two nonsymmetric root sets',
                             'atomic threshold small-root expansion through u^2',
                             'atomic energy constants 5/24 and 5/8'],
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run()
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','scope','script_sha256']}))
