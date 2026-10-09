#!/usr/bin/env python3
"""Exact finite tests of note 22's masked squarefree discrepancy bridge.
Prepared for Edward Baker with substantial LLM assistance, 8 October 2026.
Model: GPT-6 (Codex), inherited variant and effort not exposed.
Finite formal ideal algebra only; no analytic moment or reciprocity check.
"""
from fractions import Fraction as Q
from itertools import product
from math import prod
from pathlib import Path
import importlib.util
import json
import sys

sys.dont_write_bytecode = True

NORMS = (2, 3, 5, 7)
CAP = 1000
IDEALS = []
def generate(i, n, exponents):
    if i == len(NORMS):
        IDEALS.append(tuple(exponents))
        return
    j = 0
    while n <= CAP:
        generate(i + 1, n, exponents + [j])
        n *= NORMS[i]
        j += 1
generate(0, 1, [])
IDEALS.sort(key=lambda e: (prod(p**j for p,j in zip(NORMS,e)), e))
def norm(e): return prod(p**j for p,j in zip(NORMS,e))
def divs(e): return product(*(range(j+1) for j in e))
def sub(e,a): return tuple(x-y for x,y in zip(e,a))
def mu(e): return 0 if any(j>1 for j in e) else (-1)**sum(e)
def coprime(e,a): return not any(x and y for x,y in zip(e,a))
def primepower(e): return sum(j>0 for j in e)==1

def c_z(d,z):
    return sum(mu(a)*mu(sub(d,a)) for a in divs(d)
               if norm(a)<=z and norm(sub(d,a))<=z)

def finite_bridge_tests():
    counters = dict(masked_convolutions=0, projected_tail_identities=0,
                    outer_divisor_regroupings=0, phase_deletion_checks=0,
                    nonsquarefree_inner_pairs=0, semiprime_checks=0)
    phase_weights=(1,2,3,5)
    deletion_sets=((),(0,),(2,),(0,3))
    def character(e,deleted):
        return None if any(e[i] for i in deleted) else sum(j*w for j,w in zip(e,phase_weights))%6
    def character_product(chars):
        return None if None in chars else sum(chars)%6
    for logweights in ((1,3,2,5),(2,3,5,7)):
        lognorm=lambda e: sum(j*w for j,w in zip(e,logweights))
        for n in IDEALS:
            for h in divs(n):
                if mu(h)==0: continue
                t=sub(n,h)
                convolution=0
                for a in divs(t):
                    ell=sub(t,a)
                    if not primepower(ell): continue
                    if not coprime(t,h): continue
                    idx=next(i for i,j in enumerate(ell) if j)
                    convolution+=mu(a)*logweights[idx]
                    if not mu(t): counters['nonsquarefree_inner_pairs']+=1
                    for deleted in deletion_sets:
                        chars=[character(h,deleted),character(a,deleted),character(ell,deleted)]
                        assert character_product(chars)==character(n,deleted)
                        counters['phase_deletion_checks']+=1
                expected=-mu(t)*lognorm(t) if coprime(t,h) else 0
                assert convolution==expected
                counters['masked_convolutions']+=1
            norm_divisors=sorted({norm(d) for d in divs(n)})
            ys=sorted({Q(1,2),Q(1),Q(7),Q(13),Q(31)} |
                      {Q(d) for d in norm_divisors} |
                      {Q(2*d-1,2) for d in norm_divisors})
            for z in (7,13,31):
                cz={d:c_z(d,z) for d in divs(n)}
                for y in ys:
                    direct=-sum(v for d,v in cz.items() if norm(d)>y) if mu(n) else 0
                    bridge=-int(y<1) if mu(n) else 0
                    regroup=-int(y<1) if mu(n) else 0
                    for h in divs(n):
                        if mu(h)==0: continue
                        t=sub(n,h)
                        if norm(t)<=1 or norm(t)>z: continue
                        k=0
                        if coprime(t,h):
                            for a in divs(t):
                                ell=sub(t,a)
                                if primepower(ell):
                                    idx=next(i for i,j in enumerate(ell) if j)
                                    k+=mu(a)*logweights[idx]
                        J=Q(0)
                        for c in divs(h):
                            m=sub(h,c)
                            assert mu(c) and mu(m) and coprime(c,m)
                            if norm(c)>z or norm(t)*norm(c)<=y: continue
                            divisor_log=lognorm(t)+lognorm(c)
                            term=Q(2*mu(c)*k,divisor_log)
                            bridge+=term
                            J+=Q(mu(c),divisor_log)
                        regroup+=2*k*J
                    assert bridge==direct, (n,z,y,bridge,direct)
                    assert regroup==direct
                    counters['projected_tail_identities']+=1
                    counters['outer_divisor_regroupings']+=1
    for q,r,z,y in ((2,3,3,1),(3,5,5,2),(5,7,7,3)):
        for weights in ((1,3),(2,5)):
            lq,lr=weights
            assert 2*lq*(Q(1,lq)-Q(1,lq+lr))+2*lr*(Q(1,lr)-Q(1,lq+lr))==2
            assert 1<=y<min(q,r) and max(q,r)<=z<q*r
            counters['semiprime_checks']+=1
    return counters

def weighted_original_tuple_tests():
    # Independently expand the original truncated a*b*m tuple and the
    # masked c*m*(a*ell) bridge. All coefficients lie in Q[zeta_6].
    roots=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
    zero=(Q(0),Q(0))
    def add(x,y): return (x[0]+y[0],x[1]+y[1])
    def scale(x,s): return (x[0]*s,x[1]*s)
    def multiply(x,y):
        return (x[0]*y[0]-x[1]*y[1],
                x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
    phases=(1,2,3,5)
    logweights=(2,3,5,7)
    lognorm=lambda e: sum(j*w for j,w in zip(e,logweights))
    count=0
    for deleted in ((),(0,),(2,),(0,3)):
        def character(e):
            if any(e[i] for i in deleted): return zero
            return roots[sum(j*w for j,w in zip(e,phases))%6]
        for n in IDEALS:
            for y in (Q(1,2),Q(1),Q(7),Q(13),Q(14)):
                z=13
                original=zero
                if mu(n):
                    for a in divs(n):
                        remainder=sub(n,a)
                        for b in divs(remainder):
                            m=sub(remainder,b)
                            if norm(a)>z or norm(b)>z or norm(a)*norm(b)<=y:
                                continue
                            value=multiply(multiply(character(a),character(b)),character(m))
                            original=add(original,scale(value,-mu(a)*mu(b)))
                bridge=scale(character(n),-1) if mu(n) and y<1 else zero
                for c in divs(n):
                    if not mu(c) or norm(c)>z: continue
                    remainder=sub(n,c)
                    for m in divs(remainder):
                        if not mu(m) or not coprime(c,m): continue
                        t=sub(remainder,m)
                        if norm(t)<=1 or norm(t)>z or norm(t)*norm(c)<=y:
                            continue
                        h=tuple(x+y for x,y in zip(c,m))
                        outer=multiply(character(c),character(m))
                        for a in divs(t):
                            ell=sub(t,a)
                            if not primepower(ell) or not coprime(a,h) or not coprime(ell,h):
                                continue
                            idx=next(i for i,j in enumerate(ell) if j)
                            value=multiply(outer,multiply(character(a),character(ell)))
                            coefficient=Q(2*mu(c)*mu(a)*logweights[idx],lognorm(t)+lognorm(c))
                            bridge=add(bridge,scale(value,coefficient))
                assert original==bridge,(n,y,deleted,original,bridge)
                count+=1
    return dict(weighted_original_tuple_checks=count)

def existing_masked_riesz_tests():
    # This finite integral test depends only on the existing checker source.
    checker=Path(__file__).with_name('check_short_family_ideal_discrepancy.py')
    spec=importlib.util.spec_from_file_location('ideal_discrepancy_checker',checker)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    count=raw_count=interval_count=0
    for support in product((0,1),repeat=6):
        outer={i for i,j in enumerate(support) if j}
        for phases,original,delta in (((0,0,0,0,0,0),{0},1),
                                      ((1,2,3,4,5,1),{1,3},0)):
            deleted=tuple(sorted(outer|original))
            intervals,raw=mod.check_discrepancy(phases,deleted,delta,3000,7,13)
            count+=1
            interval_count+=intervals
            raw_count+=raw
    return dict(masked_mixed_integrals=count,masked_complete_edge_closures=count,
                masked_raw_stieltjes_checks=raw_count,staircase_intervals=interval_count)

if __name__=='__main__':
    result={'date':'2026-10-08','status':'passed','formal_ideal_count':len(IDEALS),
            'author':'Prepared for Edward Baker with substantial LLM assistance',
            'model':'GPT-6 (Codex), inherited variant/effort not exposed',
            **finite_bridge_tests(),**weighted_original_tuple_tests(),
            **existing_masked_riesz_tests(),
            'ring':'Exact rational specializations of additive formal logs; existing integral tests in Q[zeta_6][log rational primes]',
            'scope':'Finite formal ideal algebra and endpoints only; no asymptotic, conductor-uniform estimate, Poisson, reciprocity, or full-tail moment validation'}
    print(json.dumps(result,indent=2,sort_keys=True))
