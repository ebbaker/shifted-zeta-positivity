#!/usr/bin/env python3
"""Exact polynomial boundary degree controls; no genuine-theta evaluation.
13 October 2026. Prepared for Edward Baker with LLM assistance.
Recorded model gpt-6-astra, reasoning effort ultra.
"""
from fractions import Fraction as Q
from math import comb, factorial
import hashlib
import json
from pathlib import Path


def derivative(p, axis):
    out = {}
    for powers, c in p.items():
        if powers[axis]:
            new = list(powers)
            new[axis] -= 1
            out[tuple(new)] = c * powers[axis]
    return out


def heat_poly(m):
    return {(j, m-2*j): Q((-1)**j*factorial(m), factorial(j)*factorial(m-2*j))
            for j in range(m//2+1)}


def restrict(p, start, end):
    """Power coefficients on oriented straight edge, parameter in [0,1]."""
    result = [Q(0)] * (max((sum(e) for e in p), default=0)+1)
    for (a,b), c in p.items():
        for i in range(a+1):
            for j in range(b+1):
                result[i+j] += (c*comb(a,i)*comb(b,j)*start[0]**(a-i)
                    *(end[0]-start[0])**i*start[1]**(b-j)*(end[1]-start[1])**j)
    n = len(result)-1
    return [sum((result[k]*Q(comb(i,k),comb(n,k)) for k in range(i+1)),Q(0))
            for i in range(n+1)]


def split(b):
    rows=[b]
    while len(rows[-1])>1:
        rows.append([(a+c)/2 for a,c in zip(rows[-1],rows[-1][1:])])
    return [r[0] for r in rows], [r[-1] for r in reversed(rows)]


def fixed_sign(b):
    return min(b)>0 or max(b)<0


def certified_edges(a,b,depth=0):
    # Curve and chord lie in the same convex open half-plane. Their straight
    # homotopy therefore avoids the origin on the entire parameter segment.
    if fixed_sign(a) or fixed_sign(b):
        return [((a[0],b[0]), (a[-1],b[-1]))]
    if depth>=40:
        raise ValueError('Boundary zero or unresolved Bernstein enclosure')
    al,ar=split(a); bl,br=split(b)
    return certified_edges(al,bl,depth+1)+certified_edges(ar,br,depth+1)


def winding(pair, rectangle):
    t0,t1,x0,x1=map(Q,rectangle)
    vertices=[(t0,x0),(t1,x0),(t1,x1),(t0,x1),(t0,x0)]
    edges=[]
    for start,end in zip(vertices,vertices[1:]):
        edges += certified_edges(restrict(pair[0],start,end),restrict(pair[1],start,end))
    w=0
    for (a,b),(c,d) in edges:
        determinant=a*d-c*b
        if b<=0<d and determinant>0: w+=1
        if d<=0<b and determinant<0: w-=1
    return w,len(edges)


def main():
    records=[]
    for m in range(2,11):
        p=heat_poly(m); px=derivative(p,1)
        pt=derivative(p,0); pxx=derivative(px,1)
        assert all(pt.get(k,0)+pxx.get(k,0)==0 for k in pt.keys()|pxx.keys())
        w,n=winding((p,px),(-1,1,-1,1)); assert w==-(m//2)
        wr,nr=winding((p,px),(1,-1,-1,1)); assert wr==-w
        records.append({'multiplicity':m,'winding':w,'certified_boundary_segments':n,
                        'reversed_orientation_winding':wr,'heat_equation_exact':True})
    # H=x is a heat solution with no joint zero.
    assert winding(({(0,1):Q(1)},{(0,0):Q(1)}),(-1,1,-1,1))[0]==0
    # Nonheat H=x^2+t^2-1/4 has two joint zeros of opposite degree.
    nonheat={(0,2):Q(1),(2,0):Q(1),(0,0):-Q(1,4)}
    w,n=winding((nonheat,derivative(nonheat,1)),(-1,1,-1,1)); assert w==0
    result={'date':'2026-10-13','prepared_for':'Edward Baker','model':'gpt-6-astra',
       'reasoning_effort':'ultra','method':'Exact Fraction arithmetic; Bernstein convex-hull half-plane enclosure and polygon ray-crossing winding',
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'orientation':'(time, space), counterclockwise',
       'heat_polynomial_controls':records,'collision_free_control_winding':0,
       'nonheat_opposite_index_control':{'winding':w,'joint_zeros':['(-1/2,0)','(1/2,0)'],
          'local_indices':[-1,1],'certified_boundary_segments':n},
       'scope':'Finite exact polynomial controls only; no genuine theta enclosure, cost improvement, or RH result.'}
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
