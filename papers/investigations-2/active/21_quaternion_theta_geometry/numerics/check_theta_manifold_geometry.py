#!/usr/bin/env python3
"""Exact local geometry checks; standard library only, no theta certificate."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json

# Laurent polynomials in (p,q,r,s), with q>0 in the geometric application.
ZERO = (0, 0, 0, 0)
def clean(a):
    return {k: v for k, v in a.items() if v}
def mono(c=1, p=0, q=0, r=0, s=0):
    return clean({(p, q, r, s): F(c)})
def add(*args):
    out = {}
    for a in args:
        for k, v in a.items():
            out[k] = out.get(k, F(0)) + v
    return clean(out)
def scale(a, c):
    return clean({k: v*c for k, v in a.items()})
def mul(a, b):
    out = {}
    for k, v in a.items():
        for l, w in b.items():
            e = tuple(x+y for x, y in zip(k, l))
            out[e] = out.get(e, F(0)) + v*w
    return clean(out)
def diff(a, i):
    out = {}
    for k, v in a.items():
        if k[i]:
            e = list(k)
            e[i] -= 1
            out[tuple(e)] = v*k[i]
    return clean(out)
def parity(seq):
    return (-1)**sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1, len(seq)))
def wedge(a, b):
    out = {}
    for k, v in a.items():
        for l, w in b.items():
            seq = k+l
            if len(set(seq)) == len(seq):
                key = tuple(sorted(seq))
                out[key] = add(out.get(key, {}), scale(mul(v, w), parity(seq)))
    return {k: v for k, v in out.items() if v}
def exterior(a):
    out = {}
    for k, v in a.items():
        for i in range(4):
            if i not in k:
                seq = (i,)+k
                key = tuple(sorted(seq))
                out[key] = add(out.get(key, {}), scale(diff(v, i), parity(seq)))
    return {k: v for k, v in out.items() if v}

checks = 0
def check(a, b, name):
    global checks
    assert a == b, (name, a, b)
    checks += 1

# Hyperkahler triple, using orientation dp,dq,dr,ds.
omega = {(0,1): mono(q=1), (2,3): mono()}
real = {(0,2): mono(), (0,3): mono(p=1), (1,3): mono(-1,q=1)}
imag = {(1,2): mono(), (1,3): mono(p=1), (0,3): mono(q=1)}
triple = [omega, real, imag]
for i, a in enumerate(triple):
    check(exterior(a), {}, 'closed hyperkahler form')
    for j, b in enumerate(triple):
        check(wedge(a,b), {(0,1,2,3): mono(2,q=1)} if i == j else {}, 'triple wedge normalization')

# Compute Levi-Civita curvature directly in coordinates, independently of
# the closed-triple criterion. R^l_{ijk} = (R(partial_j,partial_k)partial_i)^l.
g = [[{} for _ in range(4)] for _ in range(4)]
gi = [[{} for _ in range(4)] for _ in range(4)]
g[0][0] = g[1][1] = mono(q=1)
g[2][2] = mono(q=-1)
g[2][3] = g[3][2] = mono(p=1,q=-1)
g[3][3] = add(mono(q=1),mono(p=2,q=-1))
gi[0][0] = gi[1][1] = gi[3][3] = mono(q=-1)
gi[2][2] = add(mono(q=1),mono(p=2,q=-1))
gi[2][3] = gi[3][2] = mono(-1,p=1,q=-1)
for i,j in product(range(4),repeat=2):
    check(add(*(mul(g[i][k],gi[k][j]) for k in range(4))), mono() if i == j else {}, 'metric inverse')
gamma = {}
for l,i,j in product(range(4),repeat=3):
    gamma[l,i,j] = scale(add(*(mul(gi[l][k],add(diff(g[k][j],i),diff(g[k][i],j),scale(diff(g[i][j],k),-1))) for k in range(4))),F(1,2))
curv = {}
for l,i,j,k in product(range(4),repeat=4):
    curv[l,i,j,k] = add(diff(gamma[l,k,i],j),scale(diff(gamma[l,j,i],k),-1),*(add(mul(gamma[m,k,i],gamma[l,j,m]),scale(mul(gamma[m,j,i],gamma[l,k,m]),-1)) for m in range(4)))
for i,k in product(range(4),repeat=2):
    check(add(*(curv[j,i,j,k] for j in range(4))), {}, 'Ricci flat')
check(curv[0,1,0,1],mono(F(1,2),q=-2),'nonzero curvature component')
sectional = mul(mono(q=-2),add(*(mul(g[0][l],curv[l,1,0,1]) for l in range(4))))
check(sectional,mono(F(1,2),q=-3),'horizontal sectional curvature')
for a,b,c in product(range(2),range(2),range(2,4)):
    check(gamma[c,a,b],{},'horizontal slices totally geodesic')

# Exact scalar checks independent of numerical sampling: the source operator
# acts on y^(1/4) Theta(y); D_u=4y d_y. Track derivatives of Theta formally.
def derivative_y(term):
    out = {}
    for (power,order),value in term.items():
        out[power-1,order] = out.get((power-1,order),F(0))+value*power
        out[power,order+1] = out.get((power,order+1),F(0))+value
    return clean(out)
def D_u(term):
    return {(power+1,order):4*value for (power,order),value in derivative_y(term).items()}
P = {(F(1,4),0):F(1)}
op = D_u(D_u(P))
op[F(1,4),0] -= 1
check(clean({k:v/16 for k,v in op.items()}),{(F(9,4),2):F(1),(F(5,4),1):F(3,2)},'theta primitive source operator')

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path)
args = parser.parse_args()
record = {
    'status':'pass', 'exact_assertions':checks, 'date':'2026-10-15',
    'prepared_for':'Edward Baker', 'assistance':'Substantial LLM assistance',
    'coordinating_model':'gpt-6-astra', 'coordinating_reasoning_effort':'ultra',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'arithmetic':'stdlib fractions.Fraction; exact Laurent polynomials',
    'scope':'Closed normalized semi-flat triple, inverse metric, Ricci tensor, nonzero sectional curvature, totally geodesic base slices, and formal theta source differential identity.',
    'not_established':['Global modular descent or metric completeness','Theta stationary sign or collision exclusion','The proposed one-sided turning estimate'],
}
serialized = json.dumps(record,indent=2,sort_keys=True)+'\n'
if args.output:
    args.output.write_text(serialized)
print(serialized)
