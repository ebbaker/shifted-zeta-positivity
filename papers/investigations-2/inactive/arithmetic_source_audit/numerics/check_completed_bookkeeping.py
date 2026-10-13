#!/usr/bin/env python3
"""Exact finite diagnostics of paper2.tex, physical lines 1915--2215.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-12.
Model: GPT-6 (Codex); inherited configuration. Exact serving variant and
configured reasoning effort are not exposed and are not inferred.
No classical large sieve, theta transformation, decay theorem, or unbounded
mean-square estimate is certified by these finite checks.
Python standard library only; optional --source is hash-checked before work.
"""

import argparse
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from math import isqrt
from pathlib import Path
import platform

EXPECTED_SOURCE_SHA256 = "d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d"
ONE = (1,0)
UNITS = [(1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,1)]
PRIMES = [(-2,-3),(1,-3),(-2,0),(1,2)] # norms 7,13,4,3; last two in S.
COUNTS,NEGATIVE = {},{}


def check(ok,label):
    assert ok,label
    COUNTS[label] = COUNTS.get(label,0)+1


def negative(ok,label,example):
    if ok:
        r = NEGATIVE.setdefault(label,{"detected":0,"example":example})
        r["detected"] += 1


def mul(a,b):
    return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1]


def norm(a):
    return a[0]**2-a[0]*a[1]+a[1]**2


def powe(a,n):
    r=ONE
    while n:
        if n&1:r=mul(r,a)
        a,n=mul(a,a),n//2
    return r


def ringprod(seq):
    r=ONE
    for a in seq:r=mul(r,a)
    return r


class SexticSplitField:
    """Actual O/(a+b omega) character exponents, without floating roots."""
    def __init__(self,p,element):
        self.p,self.element=p,element
        self.omega=-element[0]*pow(element[1],-1,p)%p
        roots=[pow(1+self.omega,j,p) for j in range(6)]
        assert len(set(roots))==6
        self.chars={x:None if x==0 else roots.index(pow(x,(p-1)//6,p)) for x in range(p)}

    def char(self,a):
        return self.chars[(a[0]+a[1]*self.omega)%self.p]


FIELDS=[SexticSplitField(7,PRIMES[0]),SexticSplitField(13,PRIMES[1])]


def chi(a,selected):
    phases=[FIELDS[i].char(a) for i in selected]
    return None if any(p is None for p in phases) else sum(phases)%6


def twisted(k,g,selected,at_S=False):
    # None is the zero value. This explicitly retains masks on powers zero.
    if at_S:return None
    a,b=chi(k,selected),chi(g,selected)
    return None if a is None or b is None else (a+4*b)%6


def radd(a,b):
    return a[0]+b[0],a[1]+b[1]


def rscale(a,c):
    return a[0]*c,a[1]*c


def rmul(a,b,q):
    return a[0]*b[0]+q*a[1]*b[1],a[0]*b[1]+a[1]*b[0]


def qsurd(q,t):
    """q^(t/2), represented exactly as A+B sqrt(q), A/B rational."""
    root=isqrt(q)
    if root*root==q:
        return Q(root)**t,Q(0)
    a,parity=divmod(t,2)
    coefficient=Q(q)**a
    return (Q(0),coefficient) if parity else (coefficient,Q(0))


def coefficient(n,b):
    # Deliberately arbitrary and nonzero for n=2; squarefreeness must be
    # enforced by summation/masks rather than hidden in this coefficient.
    return Q((n+2)*(b+3)*(n+b+1),17) if b<=3 else Q(0)


def weight(x):
    return 1/(1+x)**2


def prepared(q,Y,phase,coefficient_fn):
    ans=(Q(0),Q(0))
    for n,b in product((0,1),range(5)):
        scalar=coefficient_fn(n,b)*phase**(n+b)*weight(Q(q)**(n+3*b)/Y)
        ans=radd(ans,rscale(qsurd(q,-n-2*b),scalar))
    return ans


def check_j4_reindex():
    for q,Y,phase in product((7,13,19,25,121),(Q(1,2),Q(1),Q(7),Q(150)),(-1,1)):
        direct=(Q(0),Q(0))
        for n,b in product((0,1),range(5)):
            # B_{p,4}=q^-1/2(-1+q*1_{p|nb^3}); n is squarefree.
            local=(-1+q*int(n>0 or b>0))
            scalar=coefficient(n,b)*phase**(n+b)*local*weight(Q(q)**(n+3*b)/(q*q*Y))
            direct=radd(direct,rscale(qsurd(q,-n-2*b-1),scalar))
        const=rscale(rmul(qsurd(q,-1),prepared(q,q*q*Y,phase,coefficient),q),-1)
        cn=lambda n,b:coefficient(n+1,b) if n==0 else Q(0)
        cb=lambda n,b:coefficient(n,b+1) if n==0 else Q(0)
        nbranch=rscale(prepared(q,q*Y,phase,cn),phase)
        bbranch=rscale(rmul(qsurd(q,-1),prepared(q,Y/q,phase,cb),q),phase)
        exact=radd(radd(const,nbranch),bbranch)
        check(direct==exact,"j4_reindex_finite_sum")
        wrong_bcoef=rscale(prepared(q,Y/q,phase,cb),phase)
        negative(direct!=radd(radd(const,nbranch),wrong_bcoef),"omit_b_branch_q_inverse_sqrt",{"q":q,"Y":str(Y),"phase":phase})
        wrong_bscale=rscale(rmul(qsurd(q,-1),prepared(q,Y,phase,cb),q),phase)
        negative(direct!=radd(radd(const,nbranch),wrong_bscale),"b_branch_scale_Y_instead_of_Y_over_q",{"q":q,"Y":str(Y),"phase":phase})
        wrong_nscale=rscale(prepared(q,q*q*Y,phase,cn),phase)
        negative(direct!=radd(radd(const,wrong_nscale),bbranch),"n_branch_scale_q_squared_Y",{"q":q,"Y":str(Y),"phase":phase})
        wrong_nmask=rscale(prepared(q,q*Y,phase,lambda n,b:coefficient(n+1,b)),phase)
        negative(direct!=radd(radd(const,wrong_nmask),bbranch),"omit_n_branch_squarefree_mask",{"q":q,"Y":str(Y),"phase":phase})
        wrong_bmask=rscale(rmul(qsurd(q,-1),prepared(q,Y/q,phase,lambda n,b:coefficient(n,b+1)),q),phase)
        negative(direct!=radd(radd(const,nbranch),wrong_bmask),"omit_b_branch_disjointness_mask",{"q":q,"Y":str(Y),"phase":phase})


def local_updates(q,j,active=True):
    if not active:
        assert j==0
        return [(Q(1),Q(1))]
    if j==0:return [(Q(1,q),Q(q*q))]
    if j==4:return [(Q(1,q),Q(q*q)),(Q(1),Q(q)),(Q(1,q),Q(1,q))]
    return [(Q(1),Q(q*q))]


def check_conductor_ledger():
    records=[]
    for q,tbit,gval in product((7,13,25,121),(0,1),range(19)):
        if tbit==gval==0:continue
        j=(tbit+4*gval)%6
        exactbudget=Q(q)**(2 if tbit else gval)
        finalbudget=Q(q)**(2*tbit+gval)
        states=local_updates(q,j)
        if j==0:states+=local_updates(q,j,False)
        for a2,y in states:
            check(a2<=1,"ledger_amplitude_never_increases")
            check(a2*y<=exactbudget,"ledger_overlap_val_budget")
            check(a2*y<=finalbudget,"ledger_final_t_squared_g_budget")
        if tbit:check(j%2==1,"overlapping_t_prime_is_odd")
        elif j==2:check(gval>=2,"j2_requires_g_valuation_two")
        if gval==1 and tbit==0:
            negative(Q(q*q)>exactbudget,"omit_j4_constant_attenuation_breaks_g_budget",{"q":q,"gval":gval})
        if j==0:
            negative(Q(q*q)>q,"omit_j0_attenuation_breaks_claimed_local_q_cost",{"q":q,"gval":gval})
        if q==7:records.append({"tbit":tbit,"gval":gval,"j":j,"worst_a2Y_multiplier":str(max(a*y for a,y in states)),"budget":str(exactbudget)})
    # Distinct-prime updates multiply; sample combinations include all 6 j's.
    for choices in product([(0,1),(0,2),(0,3),(1,0),(1,1),(1,2)],repeat=3):
        productbudget=Q(1)
        maximum=Q(1)
        for q,(tbit,gval) in zip((7,13,25),choices):
            j=(tbit+4*gval)%6
            maximum*=max(a*y for a,y in local_updates(q,j))
            productbudget*=Q(q)**(2 if tbit else gval)
        check(maximum<=productbudget,"ledger_three_prime_multiplicativity")
    return records


def check_general_rows():
    rows={}
    masks=list(product((0,1),repeat=2))
    fvalues=[ringprod(powe(p,n) for p,n in zip(PRIMES[:2],mask)) for mask in masks]
    for exponents in product(range(6),repeat=4):
        sexps=tuple(a%2 for a in exponents)
        vexps=tuple(a//2 for a in exponents)
        s=ringprod(powe(p,n) for p,n in zip(PRIMES,sexps))
        v=ringprod(powe(p,n) for p,n in zip(PRIMES,vexps))
        generator=ringprod(powe(p,n) for p,n in zip(PRIMES,exponents))
        check(mul(s,mul(v,v))==generator,"row_squarefree_square_factorization")
        check(norm(s)*norm(v)**2==norm(generator),"row_norm_factorization")
        negative(any(a and b for a,b in zip(sexps,vexps)),"impose_s_v_coprimality_loses_rows",{"valuations":exponents})
        for unit in UNITS:
            k=mul(unit,generator)
            check(k not in rows,"row_decomposition_actual_ring_unique")
            rows[k]=(unit,s,v)
            for f in fvalues:
                g=mul(f,mul(v,v))
                for selected in ((0,),(1,),(0,1)):
                    lhs=twisted(k,f,selected)
                    rhs=twisted(mul(unit,s),g,selected)
                    check(lhs==rhs,"general_row_zero_extended_identity")
                    # S extension excludes columns, even when row/g meet S.
                    check(twisted(k,f,selected,True)==twisted(mul(unit,s),g,selected,True),"general_row_S_zero_extension")
                    negative(lhs!=twisted(mul(unit,s),mul(f,v),selected),"use_f_v_instead_of_f_v_squared",{"k":k,"f":f,"s":s,"v":v,"n_fields":selected})
                    if lhs is None:
                        # A unit-only interpretation of a reduced exponent
                        # would replace a zero character value by root phase 0.
                        bad=chi(k,selected),chi(f,selected)
                        badphase=((0 if bad[0] is None else bad[0])+4*(0 if bad[1] is None else bad[1]))%6
                        negative(lhs!=badphase,"discard_zero_masks_during_exponent_reduction",{"k":k,"f":f,"v":v,"n_fields":selected})
    # Polynomial bounds and summand normalization, all exact rational.
    for H,X,Nf,Nv in product((1,16,100,10000),(1,3,100),(1,7,91),(1,3,4,7,13)):
        if Nv*Nv>H:continue
        H0,Ng=Q(H,Nv*Nv),Nf*Nv*Nv
        check(H0>=1 and Ng<=H*Nf,"general_row_polynomial_range")
        check(H0+H0*H0*Ng/X==(Q(H)+Q(H*H*Nf,X))/(Nv*Nv),"general_row_Nv_inverse_square_normalization")
        negative(H0+H0*H0*Ng/X!=(Q(H)+Q(H*H*Nf,X))/Nv,"wrong_Nv_inverse_first_power",{"H":H,"X":X,"Nf":Nf,"Nv":Nv})
    for H0,Nt,Ng,X in product((1,7,100),(1,3,49),(1,7,125),(1,3,100)):
        H=H0*Nt
        rawY=Q(H0*H0*Nt*Nt*Ng*Ng,X)
        check(rawY==Q(H*H*Ng*Ng,X),"raw_conductor_Y_polynomial_bound")
    return len(rows)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source",type=Path,default=None)
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name("completed_bookkeeping_record_20261012.json"))
    args=parser.parse_args()
    observed=None
    if args.source is not None:
        observed=hashlib.sha256(args.source.read_bytes()).hexdigest()
        if observed!=EXPECTED_SOURCE_SHA256:parser.error("source hash mismatch; expected "+EXPECTED_SOURCE_SHA256+"; observed "+observed)
    check_j4_reindex()
    ledger=check_conductor_ledger()
    rowcount=check_general_rows()
    assert len(NEGATIVE)==11 and all(v["detected"]>0 for v in NEGATIVE.values())
    record={"date":"2026-10-12","prepared_for":"Edward Baker","model":"GPT-6 (Codex); inherited configuration",
            "serving_variant":"exact serving variant not exposed; not inferred",
            "effort":"exact configured effort not exposed; not inferred","expected_source_sha256":EXPECTED_SOURCE_SHA256,
            "source_sha256":observed,"source_path":None if args.source is None else str(args.source),"source_hash_verified":args.source is not None,
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"python_version":platform.python_version(),
            "python_implementation":platform.python_implementation(),"source_physical_lines":[1915,2215],"status":"pass",
            "exact_assertion_count":sum(COUNTS.values()),"exact_assertions":COUNTS,"floating_comparison_count":0,
            "negative_controls":NEGATIVE,"local_ledger_q7":ledger,"row_elements_checked":rowcount,
            "coverage":{"j4":"40 exact finite sums in Q(sqrt(q)), 5 norms, 4 rational scales, both quadratic phases; arbitrary nonzero coefficient beyond squarefree n domain",
                        "ledger":"t valuation 0/1, g valuations 0..18, 4 prime norms; active/inactive j=0 choices, all three j=4 branches; 216 three-prime worst-case products",
                        "rows":"7776 actual O elements, all 6 units, valuations 0..5 at norms 7,13,4,3; 4 squarefree f, actual sextic characters at denominators of norms 7,13,91; explicit S zero extension",
                        "limits":"finite bookkeeping only; theta transformation, uniformity, quadratic large sieve, smooth separation, infinite dyadic sums, and zeta_K(2) convergence remain mathematical imports or analytical reasoning"}}
    args.output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"pass","exact_assertion_count":record["exact_assertion_count"],"floating_comparison_count":0,
                      "negative_controls":len(NEGATIVE),"row_elements_checked":rowcount,"record":str(args.output)},indent=2))


if __name__=="__main__":main()
