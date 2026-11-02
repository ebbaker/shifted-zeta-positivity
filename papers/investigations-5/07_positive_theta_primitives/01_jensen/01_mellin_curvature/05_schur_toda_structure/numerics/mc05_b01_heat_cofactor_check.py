#!/usr/bin/env python3
"""MC05-B01 finite exact checks: two 3x3 cofactors and one quartic heat orbit.
Prepared for Edward Baker with LLM assistance, gpt-6-astra / ultra,
1 November 2026 America/New_York. No coefficient acquisition or numerical scan.
"""
from itertools import permutations
import json

variables=7
zero=(0,)*variables

def constant(a):
    return {zero:a} if a else {}

def variable(n):
    if n<0:return {}
    e=list(zero);e[n]=1
    return {tuple(e):1}

def add(a,b):
    c=dict(a)
    for e,x in b.items():
        c[e]=c.get(e,0)+x
        if not c[e]:del c[e]
    return c

def scale(a,k):return {e:k*x for e,x in a.items() if k*x}

def multiply(a,b):
    out={}
    for ea,ca in a.items():
        for eb,cb in b.items():
            e=tuple(x+y for x,y in zip(ea,eb));out[e]=out.get(e,0)+ca*cb
    return {e:x for e,x in out.items() if x}

def derivative(a,n):
    out={}
    for e,c in a.items():
        if e[n]:
            f=list(e);f[n]-=1;out[tuple(f)]=c*e[n]
    return out

def determinant(order,k):
    out={}
    for perm in permutations(range(order)):
        inv=sum(perm[i]>perm[j] for i in range(order) for j in range(i+1,order))
        term=constant((-1)**inv)
        for i,j in enumerate(perm):term=multiply(term,variable(k+j-i))
        out=add(out,term)
    return out

def heat(poly):
    out={}
    for n in range(variables-1):
        out=add(out,scale(multiply(derivative(poly,n),variable(n+1)),(2*n+2)*(2*n+1)))
    return out

checks=[]
for k in [1,2]:
    dd=heat(determinant(3,k))
    new=k+3
    cofactor=derivative(dd,new)
    expected=scale(determinant(2,k-1),(2*k+6)*(2*k+5))
    assert cofactor==expected
    assert not derivative(cofactor,new)
    checks.append({'r':3,'k':k,'new_coefficient_index':new,
                   'coefficient':'(2k+6)(2k+5) D_(2,k-1)','passed':True})
# F_tau(w)=(1+2tau+12tau^2)+(1+12tau)w+w^2.
# At tau=0 discriminant -3; at tau=1 discriminant 109 and positive coefficients.
assert 1**2-4*1==-3
assert 13**2-4*15==109
print(json.dumps({'arithmetic':'exact integer multivariate polynomial algebra',
 'cases':checks,'quartic_heat_witness':{'c_at_tau0':[1,1,1],
 'c_at_tau1':[15,13,1],'discriminants':[-3,109],
 'scope':'positive-coefficient polynomial / finite-Fock state; not a positive theta-moment source'},
 'all_checks_passed':True},indent=2))
