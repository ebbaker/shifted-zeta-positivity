#!/usr/bin/env python3
"""Finite exact checks for the scalar stationary geometry review.

15 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra, effort ultra. Analytic local classification and
infinite-current limits are proved in the note, not certified by these checks.
"""
from fractions import Fraction as Q
from math import factorial, comb
from collections import Counter
from pathlib import Path
import argparse, hashlib, json, random

# Reuse the reviewed rational polynomial engine, without running its checks.
from check_joint_source_current import Poly

S=Poly({(1,0,0):1}); X=Poly({(0,1,0):1}); ZERO=Poly()
counts=Counter()
def check(group,condition):
    if not condition: raise AssertionError(group)
    counts[group]+=1

def heat(m):
    return sum((Q(factorial(m),factorial(p)*factorial(m-2*p))*S**p*X**(m-2*p)
                for p in range(m//2+1)),ZERO)

def along_linear(poly,d):
    out={}
    for (a,b,c),value in poly.terms.items():
        assert c==0
        out[(a+b,0,0)]=out.get((a+b,0,0),0)+value*d**b
    return Poly(out)

def coefficient(poly,power): return poly.terms.get((power,0,0),Q(0))

def heat_checks():
    for k in range(13):
        p=heat(2*k)
        check('even_heat_polynomial_equation',p.diff()==p.diff(1).diff(1))
        check('positive_y_constant_for_positive_time',coefficient(p,k)>0)
        for a in range(k+1):
            check('heat_polynomial_dominates_radial_binomial',
                  p.terms[(a,2*k-2*a,0)]>=comb(k,a))
        if k:
            check('second_derivative_even_heat_polynomial',
                  p.diff(1).diff(1)==2*k*(2*k-1)*heat(2*k-2))
    for r in range(1,9):
        for j in (0,1):
            m=2*r+j
            for sign in (Q(-1),Q(1)):
                for b in (Q(-2,3),Q(0),Q(3,5)):
                    h=sign*(heat(m)+b*heat(m+1))
                    w=h if j==0 else h.diff(1)
                    alpha=sign*factorial(m); beta=sign*b*factorial(m+1)
                    d=-beta/(r*alpha)
                    stationary=along_linear(w.diff(1),d)
                    check('stationary_first_displacement_cancels',
                          all(power[0]>=r+1 for power in stationary.terms))
                    ws=along_linear(w,d)
                    check('stationary_amplitude_leading_order',
                          coefficient(ws,r)==alpha/factorial(r)
                          and all(power[0]>=r for power in ws.terms))
                    if j:
                        hs=along_linear(h,d)
                        expected=-beta/(alpha*r*(r+1))
                        check('odd_jet_extra_order',all(power[0]>=r+1 for power in hs.terms))
                        check('odd_jet_ratio_first_coefficient',
                              coefficient(hs,r+1)==coefficient(ws,r)*expected)
    # Both exact collision controls obey the scalar geometry but violate a
    # bounded positive endpoint ratio. These are non-theta controls.
    delta=Q(1,4)
    previous=Q(0)
    for k in range(1,13):
        s=Q(1,2**k)
        ratio=1+delta**2/(2*s)
        check('even_control_scalar_ratio',(delta**2+2*s)/(2*s)==ratio)
        check('odd_control_scalar_ratio',(3*delta**2+6*s)/(6*s)==ratio)
        check('control_positive_ratio_grows',ratio>previous)
        previous=ratio

def poly(rng):
    return Poly({(k,0,0):Q(rng.randint(-8,8),rng.randint(1,7)) for k in range(5)})

def trace(j,k,m,u):
    return (j[0]-j[1]+j[m+1]-j[m]).integrate_u(u)+sum(
        (k[n].at_u(u)-k[n].at_u(0) for n in range(1,m+1)),ZERO)

def green(values,n):
    return sum(((m-n)*value for m,value in values.items() if m>n),Q(0))

def gauge_checks():
    rng=random.Random(20261015)
    for m in range(1,9):
        for trial in range(5):
            j=[poly(rng) for _ in range(m+2)]
            k=[poly(rng) for _ in range(m+1)]
            l=[poly(rng) for _ in range(m+2)]
            jt=[a+b.diff() for a,b in zip(j,l)]
            kt=[k[0]]+[k[n]-l[n-1]+2*l[n]-l[n+1] for n in range(1,m+1)]
            u=Q(trial+2,3)
            check('all_four_rectangle_edges_gauge_invariant',trace(j,k,m,u)==trace(jt,kt,m,u))
            for n in range(1,m+1):
                check('joint_divergence_gauge_invariant',
                      j[n-1]-2*j[n]+j[n+1]+k[n].diff()
                      ==jt[n-1]-2*jt[n]+jt[n+1]+kt[n].diff())
        j={n:Q(rng.randint(-8,8),5) for n in range(m+1)}
        k={n:Q(rng.randint(-8,8),7) for n in range(1,m+2)}
        a={n:j.get(n-1,0)-2*j.get(n,0)+j.get(n+1,0)-k.get(n,0)
           for n in range(1,m+3)}
        for n in range(m+3):
            check('canonical_integrated_current',j.get(n,0)-green(k,n)==green(a,n))
        check('canonical_combined_lower_trace',green(a,0)-green(a,1)==sum(a.values()))
        # Collar gamma(u)=1-u on [0,1] tests its endpoint transfer exactly.
        gamma=1-S
        for n in range(1,m+2):
            collar_lap=gamma*(green(k,n-1)-2*green(k,n)+green(k,n+1))
            check('collar_cancels_source_lower_flux',(gamma*k[n]-collar_lap).at_u(0)==0)
        check('collar_index_flux_sign',
              (gamma.diff()*(green(k,0)-green(k,1))).integrate_u(Q(1))==-sum(k.values()))

def cone_checks():
    for kappa in (Q(1,4),Q(1),Q(3,2)):
        for a in (Q(-3),Q(-1,2),Q(0),Q(2,3),Q(4)):
            for b in (Q(-5),Q(-1),Q(0),Q(1,3),Q(3)):
                q=max(Q(0),b+kappa*abs(a))
                for z in (-kappa,-kappa/2,Q(0),kappa/2,kappa):
                    check('cone_coefficient_upper_bound',b+a*z<=q)
                endpoint=kappa if a>=0 else -kappa
                check('cone_constant_is_exact_nonnegative_supremum',max(Q(0),b+a*endpoint)==q)
        for power in range(1,9):
            tau=Q(1,2**power); a=1/tau**2; b=-kappa/tau**2
            check('singular_cone_favorable_cancellation',max(Q(0),b+kappa*abs(a))==0)
            z=kappa+1
            check('full_plane_has_divergent_positive_direction',
                  (b+a*z)/(1+z*z)==1/((1+z*z)*tau**2))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    heat_checks(); gauge_checks(); cone_checks()
    import check_joint_source_current as engine
    result={'status':'passed','date':'2026-10-15','prepared_for':'Edward Baker',
        'llm_assistance':'Substantial LLM assistance','model':'gpt-6-astra','reasoning_effort':'ultra',
        'exact_assertions':sum(counts.values()),'groups':dict(sorted(counts.items())),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'polynomial_engine_sha256':hashlib.sha256(Path(engine.__file__).read_bytes()).hexdigest(),
        'scope':'Finite rational heat-polynomial, gauge, and cone checks. The general analytic stationary-set classification and all infinite limits require the proofs in the note. Non-theta controls demonstrate that the simplification alone supplies no sign theorem.'}
    text=json.dumps(result,indent=2)+'\n'
    if args.output: args.output.write_text(text)
    print(text,end='')

if __name__=='__main__': main()
