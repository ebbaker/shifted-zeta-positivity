#!/usr/bin/env python3
"""Exact affine Ward jet freedom and rational-anchor divergence checks."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib
import json
import math


class P:
    size = 9
    def __init__(self, data=0):
        if isinstance(data,P):
            self.a = dict(data.a)
        elif isinstance(data,dict):
            self.a = {k:F(v) for k,v in data.items() if v}
        else:
            self.a = {} if not data else {(0,)*self.size:F(data)}
    @classmethod
    def var(cls,i):
        key = [0]*cls.size
        key[i] = 1
        return cls({tuple(key):1})
    def __add__(self,other):
        out = dict(self.a)
        for k,v in P(other).a.items():
            out[k] = out.get(k,F(0))+v
        return P(out)
    __radd__ = __add__
    def __neg__(self):
        return P({k:-v for k,v in self.a.items()})
    def __sub__(self,other):
        return self+-P(other)
    def __mul__(self,other):
        out = {}
        for k,v in self.a.items():
            for l,w in P(other).a.items():
                key = tuple(a+b for a,b in zip(k,l))
                out[key] = out.get(key,F(0))+v*w
        return P(out)
    __rmul__ = __mul__
    def __pow__(self,n):
        out = P(1)
        for _ in range(n):
            out = out*self
        return out
    def d(self,i):
        out = {}
        for k,v in self.a.items():
            if k[i]:
                key = list(k)
                key[i] -= 1
                out[tuple(key)] = v*k[i]
        return P(out)
    def __eq__(self,other):
        return self.a == P(other).a
    def eval(self,values):
        return sum((v*math.prod(values[j]**k[j] for j in range(self.size))
                    for k,v in self.a.items()), F(0))


t,x,*J = [P.var(j) for j in range(9)]
a = 2*t-1-x*x
K = []
for j in range(5):
    row = (P(1) if j==0 else P(0))+(a+4*t*j)*J[j]
    row += 4*t*x*J[j+1]-4*t*t*J[j+2]
    if j:
        row -= 2*j*x*J[j-1]
    if j >= 2:
        row -= j*(j-1)*J[j-2]
    K.append(row)


def dx(poly):
    return poly.d(1)+sum((J[j+1]*poly.d(j+2)
                         for j in range(6)),P(0))


checks = 0
for j in range(4):
    assert dx(K[j]) == K[j+1]
    checks += 1
jac = [[K[j+2].d(k+6) for k in range(3)] for j in range(3)]
expected = [[-4*t*t,0,0],[4*t*x,-4*t*t,0],
            [a+16*t,4*t*x,-4*t*t]]
for j in range(3):
    for k in range(3):
        assert jac[j][k] == expected[j][k]
        checks += 1
det = P(0)
for perm in permutations(range(3)):
    sign = (-1)**sum(perm[i]>perm[j] for i in range(3)
                    for j in range(i+1,3))
    term = P(sign)
    for j in range(3):
        term *= jac[j][perm[j]]
    det += term
assert det == -64*t**6
checks += 1
threshold = x*x*(2*K[3]*K[3]-3*K[2]*K[4])-9*K[2]*K[2]
assert threshold.d(8) == 12*t*t*x*x*K[2]
checks += 1

# Formal candidate jets: not realizations of theta or any positive kernel.
examples = []
for h4 in (F(0),F(-4)):
    tv,xv = F(1,20),F(1)
    av = 2*tv-1-xv*xv
    js = [F(0),F(0),1/(4*tv*tv)]
    js.append(((av+4*tv)*js[1]-2*xv*js[0]
               +4*tv*xv*js[2])/(4*tv*tv))
    js.append(((av+8*tv)*js[2]-4*xv*js[1]-2*js[0]
               +4*tv*xv*js[3]-16)/(4*tv*tv))
    js.append(((av+12*tv)*js[3]-6*xv*js[2]-6*js[1]
               +4*tv*xv*js[4])/(4*tv*tv))
    js.append(((av+16*tv)*js[4]-8*xv*js[3]-12*js[2]
               +4*tv*xv*js[5]-16*h4)/(4*tv*tv))
    values = [tv,xv]+js
    assert [p.eval(values) for p in K] == [0,0,16,0,16*h4]
    sign = threshold.eval(values)/256
    assert sign == -3*h4-9
    examples.append({'time':str(tv),'height':str(xv),
                     'J_jets':[str(v) for v in js],
                     'H_jets':['0','0','1','0',str(h4)],
                     'raw_threshold_expression':str(sign)})
    checks += 2
anchor = [F(math.factorial(2*j),math.factorial(j)) for j in range(7)]
for j in range(6):
    assert anchor[j+1]/anchor[j] == 4*j+2
    checks += 1

source = Path(__file__).resolve()
record = {
    'date':'2026-10-10',
    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'assertions_passed':checks,
    'conditional_higher_jet_jacobian_determinant':'-64*t^6',
    'formal_candidate_opposite_sign_examples':examples,
    'rational_anchor_formal_time_coefficients':[str(v) for v in anchor],
    'scope':'Exact formal jet freedom and zero-radius rational-anchor series; examples are not actual theta or positive-kernel states. No collision exclusion or independent validation.',
}
target = source.with_name('conditional_endpoint_record_20261010.json')
target.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps({'record':target.name,'passed':checks},sort_keys=True))
