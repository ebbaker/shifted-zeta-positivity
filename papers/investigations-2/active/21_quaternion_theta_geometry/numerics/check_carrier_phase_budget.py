#!/usr/bin/env python3
"""Exact finite arithmetic supporting the carrier-to-phase estimate."""
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

checks = []
def verify(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

L0 = 100002
V0 = L0 - 1
X0 = 10**12
R0 = 10**6
b = F(1001, 1000)
D, B, C = 34, 260, 3100
A0 = F(36138917, 16)
G0 = F(962773, 671)
lam = F(21807, 254720000) - F(63, 50) * F(1, 100000)
verify('elementary height implies x greater than 10^12', F(L0**3, 6) > X0)
verify('square-root endpoint', R0**2 == X0)
verify('alpha correction less than one', F(11,14) + F(4,X0) < 1)
verify('alpha prime allowance', 1 + F(6,X0) <= 2)
verify('alpha second allowance', 2 + F(24,X0) <= 3)
verify('alpha third allowance', 8 + F(144,X0) <= 9)
verify('b allowance', 1 + F(1,2*X0) <= b)
for m, expected in [(1,65), (2,1028), (3,24603)]:
    verify(f'zeta logarithmic derivative constant {m}', math.factorial(m)*8**(m+1)+m**m == expected)
verify('first logarithmic derivative correction', (1 + F(1,2*R0) + 65*b)/2 < D)
verify('q2 first residual', 2*b/X0 < 1)
verify('q2 second residual', F(3,4*X0*R0) + F(195,4*X0**2) < 1)
verify('q2 total', (2+1028*b*b)/4 < B)
verify('q3 first residual', 3*b/X0**2 < 1)
verify('q3 second residual', F(3,X0**3) < 1)
verify('q3 third residual', F(9,4*X0**2*R0) + F(585,4*X0**3) < 1)
verify('q3 fourth residual', F(9,4)*1028*b/X0**2 < 1)
verify('q3 total', (4+24603*b**3)/8 < C)
verify('order one coefficient', 4*D == 136)
verify('order two leading coefficient', 8*D == 272)
verify('order two residual coefficient', 16*(D*D+B) == 22656)
verify('order three leading coefficient', 12*D == 408)
verify('order three second coefficient', 48*(D*D+B) == 67968)
verify('order three third coefficient', 64*(D**3+3*D*B+C) == 4411136)
verify('order one dominated by 409/L', 136 <= 409)
verify('order two dominated by 409/L', 272+F(22656,L0) <= 409)
verify('order three dominated by 409/L', 408+F(67968,L0)+F(4411136,L0**2) <= 409)
verify('lambda exceeds one over 14000', lam > F(1,14000))
verify('analytic replacement Cauchy coefficient', math.factorial(3)*4**3*F(9,2) == 1728)
verify('six budget shares total one eighth', 6*F(1,48) == F(1,8))
verify('low-index sufficient log-height', 48*1728*4*A0 == 749376582912)
verify('exponent-pair log coefficient', 48*1728*8 == 663552)
verify('ordinary tail budget exponent', F(V0,40)**3/6 > 48*1728*64)
verify('quadratic absorbed by exponential', F(V0,4)**3/6 >= V0**2)
verify('first RS error budget', F(V0**2,8) > 48*1728*16)
verify('second RS error budget', F(2*V0**2,25) > 48*1728*6)
verify('carrier budget share', L0 > 48*409)
verify('energy lower bound at d=1/8', 4*(1-4*F(1,8)) == 2)
verify('Laguerre lower bound at d=1/8', 4*(1-4*F(1,8)-F(1,8)**2) == F(31,16))

# Minimal exact sparse-polynomial algebra, with variables q1,q2,q3.
def add(*polys):
    out = {}
    for poly in polys:
        for powers, coeff in poly.items():
            out[powers] = out.get(powers,0)+coeff
    return {p:c for p,c in out.items() if c}
def mul(a,b):
    out = {}
    for p,c in a.items():
        for q,d in b.items():
            r = tuple(i+j for i,j in zip(p,q))
            out[r] = out.get(r,0)+c*d
    return out
def deriv(poly):
    out = {}
    for p,c in poly.items():
        for k in range(2):
            if p[k]:
                q=list(p); q[k]-=1; q[k+1]+=1; q=tuple(q)
                out[q] = out.get(q,0)+c*p[k]
        if p[2]:
            raise AssertionError('unexpected fourth derivative')
    return out
q1={(1,0,0):1}
p0={(0,0,0):1}
p1=add(mul(q1,p0),deriv(p0))
p2=add(mul(q1,p1),deriv(p1))
p3=add(mul(q1,p2),deriv(p2))
verify('Q first derivative polynomial', p1 == {(1,0,0):1})
verify('Q second derivative polynomial', p2 == {(2,0,0):1,(0,1,0):1})
verify('Q third derivative polynomial', p3 == {(3,0,0):1,(1,1,0):3,(0,0,1):1})

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path)
args=parser.parse_args()
record={
    'purpose':'Exact finite arithmetic for the complete carrier-to-phase budget; no imported exponent-pair constants evaluated.',
    'date':'2026-10-15',
    'prepared_for':'Edward Baker',
    'assistance':'Substantial LLM assistance',
    'coordinating_model':'gpt-6-astra',
    'coordinating_reasoning_effort':'ultra',
    'model_provenance':'Parent conversation metadata; worker configuration not independently asserted.',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'assertions_passed':len(checks),
    'checks':checks,
    'carrier_error_bound':'409/L for L >= 100002',
    'physical_error_bound':'1728 B_C(L) + 409/L',
    'sufficient_conditional_log_height':'1 + max(749376582912, 14000 log(663552 G0 C_EP))',
    'remaining_inputs':['Actual numerical exponent-pair constants at eta=1e-5','Any exponent-pair source validity threshold'],
    'limits':['Finite arithmetic only','No evaluated imported arithmetic constants','No new unconditional sign domain','No stationary-root certification'],
}
serialized=json.dumps(record,indent=2,sort_keys=True)+'\n'
if args.output:
    args.output.write_text(serialized)
print(serialized)
