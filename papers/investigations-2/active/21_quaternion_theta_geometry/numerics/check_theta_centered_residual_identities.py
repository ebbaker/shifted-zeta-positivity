#!/usr/bin/env python3
"""Exact finite polynomial checks; standard library only.

Prepared for Edward Baker, 2026-10-14, with LLM assistance.
Parent-verified model gpt-6-astra, reasoning effort ultra.
These algebra checks do not prove any theta residual cone.
"""
from fractions import Fraction as Q
import argparse
from hashlib import sha256
import json
from pathlib import Path
import platform

N = 9
ZERO = (0,) * N

class P:
    def __init__(self, value=0):
        if isinstance(value, P):
            self.c = dict(value.c)
        elif isinstance(value, dict):
            self.c = {m: Q(v) for m, v in value.items() if v}
        else:
            self.c = {ZERO: Q(value)} if value else {}
    def __add__(self, other):
        out = dict(self.c)
        for m, v in P(other).c.items():
            out[m] = out.get(m, Q(0)) + v
        return P(out)
    __radd__ = __add__
    def __neg__(self): return P({m: -v for m,v in self.c.items()})
    def __sub__(self, other): return self + (-P(other))
    def __rsub__(self, other): return P(other) + (-self)
    def __mul__(self, other):
        out = {}
        for m, v in self.c.items():
            for n, w in P(other).c.items():
                z = tuple(i+j for i,j in zip(m,n))
                out[z] = out.get(z, Q(0)) + v*w
        return P(out)
    __rmul__ = __mul__
    def __pow__(self, k):
        out = P(1)
        for _ in range(k): out = out*self
        return out

def var(index):
    m = list(ZERO)
    m[index] = 1
    return P({tuple(m): 1})

a,b,eta,h0,h1,h2,h3,at,bt = [var(i) for i in range(N)]
mu = a*a+b*b
lam = b*b-a*a
E = h0*h0+h1*h1
C0 = -h2-2*a*h1-mu*h0
C1 = -h3-2*a*h2-mu*h1
L0 = h1*h1-h0*h2
L1 = h2*h2-h1*h3
slack = eta*eta*E-C0*C0-C1*C1
checks = []

def equal(name, left, right):
    difference = left-right
    if difference.c:
        raise AssertionError((name, difference.c))
    checks.append(name)

equal('full stationary-ideal SOS level 0',
      2*eta*(L0+(eta-mu)*E),
      (C0+eta*h0)**2+C1*C1+slack
      +2*eta*h1*((1-mu+Q(1,2)*eta)*h1+2*a*h0))
equal('full stationary-ideal SOS level 1',
      4*mu*L1+eta*eta*E,
      (2*mu*h1+C1)**2+C0*C0+slack
      +4*mu*h2*(h2+2*a*h1))
equal('balanced evolution real component',
      -h2, lam*h0+2*a*(h1+a*h0)+C0)
equal('balanced evolution imaginary component times b',
      -h3-a*h2,
      lam*(h1+a*h0)-2*a*b*b*h0+C1-a*C0)
equal('variable-parameter balanced evolution imaginary times b squared',
      b*(-h3-a*h2+at*h0)-bt*(h1+a*h0),
      b*(lam*(h1+a*h0)-2*a*b*b*h0+C1-a*C0)
      +b*at*h0-bt*(h1+a*h0))
P_rad=-h0*h2-h1*h3
S_tan=h1*h2-h0*h3
equal('radial and tangential squared identity',
      E*(h2*h2+h3*h3), P_rad*P_rad+S_tan*S_tan)
equal('arbitrary radial and phase centering; a=lambda b=rho in this check',
      E*((-h2-a*h0+b*h1)**2+(-h3-a*h1-b*h0)**2),
      (P_rad-a*E)**2+(S_tan-b*E)**2)
equal('physical heat drift residual',
      P_rad, mu*E+2*a*(h0*h1+h1*h2)+h0*C0+h1*C1)

wrong = ((C0+eta*h0)**2+C1*C1+slack
         +2*eta*h1*((1-mu)*h1+2*a*h0))
equal('level-zero off-stationary correction coefficient',
      2*eta*(L0+(eta-mu)*E)-wrong, eta*eta*h1*h1)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
record = {
    'date': '2026-10-14',
    'prepared_for': 'Edward Baker',
    'llm_assistance': 'Substantial',
    'recorded_model': 'gpt-6-astra',
    'recorded_effort': 'ultra',
    'source_name': Path(__file__).name,
    'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'python': platform.python_version(),
    'arithmetic': 'exact rational sparse polynomial coefficients; standard library',
    'status': 'PASS',
    'checks': len(checks),
    'identities': checks,
    'scope': 'Exact polynomial identities; no theta cone proved.'}
args.output.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'status': record['status'], 'checks': len(checks),
                  'output': str(args.output), 'source_sha256': record['source_sha256']}))
