#!/usr/bin/env python3
"""Exact base-metric and path-restriction checks for Investigation 22."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

# Polynomials in (p,q), with an overall pi factored out of log metrics.
def clean(a):
    return {k:v for k,v in a.items() if v}
def add(*args):
    out={}
    for a in args:
        for k,v in a.items(): out[k]=out.get(k,F(0))+v
    return clean(out)
def scale(a,c): return clean({k:F(c)*v for k,v in a.items()})
def diff(a,i):
    out={}
    for k,v in a.items():
        if k[i]:
            m=list(k); m[i]-=1
            out[tuple(m)]=v*k[i]
    return clean(out)
def lap(a): return add(diff(diff(a,0),0),diff(diff(a,1),1))
def path(a): return clean({k:v for k,v in a.items() if k[0]==0})
checks=[]
def check(a,b,label):
    if a!=b: raise AssertionError((label,a,b))
    checks.append(label)

b_old={(0,3):F(2,3)}
b_new={(2,1):F(2)}
g_real={(2,1):F(1),(0,3):F(-1,3)}
g_imag={(3,0):F(-1,3),(1,2):F(1)}
check(diff(g_real,0),diff(g_imag,1),'Cauchy Riemann first equation for g/pi')
check(diff(g_real,1),scale(diff(g_imag,0),-1),'Cauchy Riemann second equation for g/pi')
check(add(b_new,scale(b_old,-1)),scale(g_real,2),'metric difference is twice real holomorphic cubic')
check(lap(b_old),{(0,1):F(4)},'original ASD base Poisson equation')
check(lap(b_new),{(0,1):F(4)},'adapted ASD base Poisson equation')
check(lap(g_real),{},'holomorphic cubic real part is harmonic')
# A_b=(b_p-i b_q)d tau/2. Along p=0, d tau=i dq.
check(path(scale(diff(b_old,1),F(1,2))),{(0,2):F(1)},'old real path connection is pi q squared dq')
check(path(diff(b_old,0)),{},'old path connection imaginary part zero')
check(path(b_new),{},'adapted path squared norm is one')
check(path(diff(b_new,0)),{},'adapted path connection first component zero')
check(path(diff(b_new,1)),{},'adapted path connection second component zero')
check(path(g_real),{(0,3):F(-1,3)},'cubic real restriction cancels old path primitive')
check(path(g_imag),{},'cubic imaginary restriction vanishes')
# Frame or metric changes by any real part of a holomorphic polynomial
# preserve the Laplacian. Verify a basis through degree eight.
from math import comb
for n in range(1,9):
    re={}; im={}
    for k in range(n+1):
        value=F(comb(n,k))
        if k%2==0: re[n-k,k]=value*((-1)**(k//2))
        else: im[n-k,k]=value*((-1)**((k-1)//2))
    check(lap(re),{},f'real holomorphic freedom degree {n}')
    check(lap(im),{},f'imaginary holomorphic freedom degree {n}')
# Exact pullback of a two-form: each tangent vector has only q component.
# Tensor-product source points are distinct copies, so there is no cross
# curvature term. This verifies restriction, not ambient flatness.
def skew_eval(form,v,w):
    return sum(c*(v[i]*w[j]-v[j]*w[i]) for (i,j),c in form.items())
# Curvature/(2*pi*i), q=arbitrary rational, coordinates p,q,r,s.
for q in (F(1),F(3,2),F(7)):
    form={(0,1):q,(2,3):F(-1)}
    tangent=(0,4*q,0,0)
    check(skew_eval(form,tangent,tangent),0,f'physical curvature restriction q={q}')
    # In 8D product coordinates, tangents lie in separate factors.
    form2=dict(form)
    form2.update({(i+4,j+4):c for (i,j),c in form.items()})
    U=tangent+(0,0,0,0); V=(0,0,0,0)+tangent
    check(skew_eval(form2,U,V),0,f'external tensor product restriction q={q}')

ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path); args=ap.parse_args()
record={'status':'pass','date':'2026-10-15','prepared_for':'Edward Baker',
'assistance':'Substantial LLM assistance','model':'gpt-6-astra','reasoning_effort':'ultra',
'exact_assertions':len(checks),'checks':checks,'arithmetic':'Python standard library fractions.Fraction',
'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
'scope':'Base ASD Poisson equation, holomorphic metric freedom, adapted physical path metric and connection, and external tensor curvature restriction.',
'not_established':['Theta signed estimate','Physical energy lower bound','Global modular descent','Analytic classification from finite checks']}
s=json.dumps(record,indent=2,sort_keys=True)+'\n'
if args.output: args.output.write_text(s)
print(s)
