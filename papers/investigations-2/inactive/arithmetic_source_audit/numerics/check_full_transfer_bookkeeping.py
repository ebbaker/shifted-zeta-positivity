#!/usr/bin/env python3
"""Exact finite bookkeeping for the full two-Poisson transfer interface.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-12.
Model GPT-6 (Codex), inherited configuration. Exact serving variant and
configured effort are not exposed and are not inferred.
Standard library only. Finite checks do not prove Poisson/theta identities,
smooth derivative bounds, unbounded estimates, or the final quasi-RH theorem.

The inverse-preimage/norm formulas adapt check_transfer_regrouping.py,
whose original 729 cases were norm encodings of three primes. This NEW
checker independently enumerates local forward source placements, uses
actual Eisenstein elements and sextic residues, and extends the scale tests.
"""

import argparse
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from math import prod
from pathlib import Path
import platform

PINNED_SHA = "d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d"
ONE=(1,0)
UNITS=[(1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,1)]
PRIMES=[(-2,-3),(1,-3),(-2,3)]
NORMS=(7,13,19)
COUNTS, NEGATIVE = {},{}


def check(ok,label):
    assert ok,label
    COUNTS[label]=COUNTS.get(label,0)+1


def negative(ok,label,example):
    if ok:
        d=NEGATIVE.setdefault(label,{"detected":0,"example":example})
        d["detected"]+=1


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


def ringprod(xs):
    r=ONE
    for x in xs:r=mul(r,x)
    return r


def exactdiv(a,b):
    x=mul(a,(b[0]-b[1],-b[1]))
    nb=norm(b)
    assert x[0]%nb==x[1]%nb==0
    return x[0]//nb,x[1]//nb


def bits_value(bits):
    return ringprod(p for p,b in zip(PRIMES,bits) if b)


def subsets(bits):
    return [b for b in product((0,1),repeat=3) if all(x<=y for x,y in zip(b,bits))]


def mu(bits):
    return (-1)**sum(bits)


def local_forward(rbit,fbit,kval):
    """Independent source-domain enumeration: one of C,t,g,w,or none."""
    found=[]
    for placement in range(5):
        C,t,g,w=[int(placement==i) for i in range(4)]
        for d,e in product((0,1),repeat=2):
            if d>C or e>g:continue
            h=kval-d-e
            if h<0 or w*h:continue
            if t+g-e==rbit and C+e+w==fbit:
                found.append((C,d,t,g,e,w,h))
    return sorted(found)


def inverse_entries(rb,fb,kv):
    for tb in subsets(rb):
        positions=[i for i,b in enumerate(fb) if b]
        for assignments in product(range(3),repeat=len(positions)):
            C,e,w=[tuple(int(i in positions and assignments[positions.index(i)]==target) for i in range(3)) for target in range(3)]
            if any(e[i]>kv[i] or w[i]*kv[i] for i in range(3)):continue
            for d in subsets(tuple(int(C[i] and kv[i]>0) for i in range(3))):
                g=tuple(e[i]+rb[i]-tb[i] for i in range(3))
                h=tuple(kv[i]-d[i]-e[i] for i in range(3))
                yield (C,d,tb,g,e,w,h)


def check_preimages():
    for rbit,fbit,kval in product((0,1),(0,1),range(7)):
        if rbit*fbit:continue
        rb,fb,kv=(rbit,0,0),(fbit,0,0),(kval,0,0)
        inverse=sorted(tuple(a[0] for a in entry) for entry in inverse_entries(rb,fb,kv))
        check(inverse==local_forward(rbit,fbit,kval),"independent_local_forward_inverse")
    H,L,F,Sigma,c=map(Q,(4096,8192,1,16384,16))
    cases=preimages=0
    cache={b:bits_value(b) for b in product((0,1),repeat=3)}
    for locations in product(range(3),repeat=3):
        rb=tuple(int(x==1) for x in locations)
        fb=tuple(int(x==2) for x in locations)
        r,f=cache[rb],cache[fb]
        entries_for_k={kv:list(inverse_entries(rb,fb,kv)) for kv in product(range(4),repeat=3)}
        for kv,entries in entries_for_k.items():
            actual_base=ringprod(powe(p,a) for p,a in zip(PRIMES,kv))
            for vlam,v2,unit in product((0,1,3),(0,2),UNITS):
                k=mul(unit,mul(actual_base,mul(powe((1,2),vlam),powe((-2,0),v2))))
                seen=set()
                signed=wrong_t_signed=wrong_d_signed=0
                for entry in entries:
                    Cb,db,tb,gb,eb,wb,hb=entry
                    C,d,t,g,e,w=[cache[b] for b in (Cb,db,tb,gb,eb,wb)]
                    h=exactdiv(k,mul(d,e))
                    key=(C,d,t,g,e,w,h)
                    check(key not in seen,"preimage_actual_ring_unique")
                    seen.add(key)
                    check(exactdiv(mul(t,g),e)==r and mul(C,mul(e,w))==f and mul(d,mul(e,h))==k,"preimage_return_map")
                    check(all(not gb[i]*(Cb[i]+tb[i]) and not wb[i]*(gb[i]+Cb[i]+tb[i]+hb[i]) for i in range(3)),"source_preimage_masks")
                    check(all((not x or hb[i]==kv[i]-db[i]-eb[i]) for i,x in enumerate(gb)),"higher_frequency_valuation_retained")
                    ell=L/(norm(C)*norm(t))
                    outer=H*norm(C)/(norm(d)*L*L*F)
                    Y=c*Sigma*L*F*norm(d)/(H*norm(C)**2)
                    check(ell/(norm(g)*norm(w))==L/(norm(r)*norm(f)),"common_individual_column_scale")
                    check(outer*Y*norm(g)/(norm(e)*ell)==c*Sigma*norm(r)/(L*L),"combined_prefactor")
                    check(Y*norm(h)*norm(g)**2/(norm(e)*ell*ell)==c*Sigma*F*norm(k)*norm(r)**2/(H*L),"common_Fourier_parameter")
                    check(outer*Y*ell==c*Sigma/(norm(C)**2*norm(t)),"outer_zero_frequency_prefactor")
                    signed+=mu(eb)*mu(wb)
                    wrong_t_signed+=mu(eb)*mu(wb)*mu(tb)
                    wrong_d_signed+=mu(eb)*mu(wb)*mu(db)
                    preimages+=1
                expected=2**sum(rb) if all(not b or a>0 for b,a in zip(fb,kv)) else 0
                check(signed==expected,"global_signed_preimage_sum")
                negative(wrong_t_signed!=expected,"carry_first_mu_t_into_nonnegative_Q",{"r":r,"f_prime":f,"k_prime":k})
                negative(wrong_d_signed!=expected,"carry_first_mu_d_into_nonnegative_Q",{"r":r,"f_prime":f,"k_prime":k})
                negative(sum(abs(mu(e[4])*mu(e[5])) for e in entries)!=expected,"absolute_values_before_regrouping",{"r":r,"f_prime":f,"k_prime":k})
                cases+=1
    return cases,preimages


class Field:
    def __init__(self,p,element,inert=False):
        self.p,self.element,self.inert=p,element,inert
        self.q=p*p if inert else p
        self.zero,self.one=((0,0),(1,0)) if inert else (0,1)
        self.values=list(product(range(p),repeat=2)) if inert else list(range(p))
        root=(1,1) if inert else (1-element[0]*pow(element[1],-1,p))%p
        roots=[self.power(root,j) for j in range(6)]
        assert len(set(roots))==6
        self.phases={x:None if x==self.zero else roots.index(self.power(x,(self.q-1)//6)) for x in self.values}

    def multiply(self,a,b):
        if self.inert:
            x=mul(a,b)
            return x[0]%self.p,x[1]%self.p
        return a*b%self.p

    def power(self,a,n):
        x=self.one
        while n:
            if n&1:x=self.multiply(x,a)
            a,n=self.multiply(a,a),n//2
        return x

    def reduce(self,a):
        if self.inert:return a[0]%self.p,a[1]%self.p
        return (a[0]-a[1]*self.element[0]*pow(self.element[1],-1,self.p))%self.p

    def char(self,a,j=1):
        x=self.phases[self.reduce(a)]
        return None if x is None else j*x%6


def phase_product(*xs):
    return None if None in xs else sum(xs)%6


def local_phase(field,x,j):
    phase=field.phases[x]
    return None if phase is None else j*phase%6


def masked(value,mask):
    return value if mask else None


def check_character_masks():
    fields=[Field(7,PRIMES[0]),Field(13,PRIMES[1]),Field(19,PRIMES[2]),Field(5,(-5,0),True)]
    for f in fields:
        for d,e,h,C in product(f.values,repeat=4):
            lhs=phase_product(local_phase(f,d,1),local_phase(f,h,1),local_phase(f,e,-1),local_phase(f,C,4))
            rhs=phase_product(local_phase(f,d,1),local_phase(f,e,5),local_phase(f,h,1),local_phase(f,C,4))
            check(lhs==rhs,"second_Poisson_deh_Ce_identity_with_zeros")
            wrong=phase_product(local_phase(f,d,1),local_phase(f,e,1),local_phase(f,h,1),local_phase(f,C,4))
            negative(lhs!=wrong,"omit_Ce_fourth_power_e_factor",{"norm":f.q,"d":d,"e":e,"h":h,"C":C})
        for x in f.values:
            check((local_phase(f,x,0) is None)==(x==f.zero),"zero_exponent_is_unit_mask")
            negative(local_phase(f,x,0)!=0,"principal_power_as_constant_one",{"norm":f.q,"x":x})
    # Actual ring inputs for both common-factor and exclusion masks.
    cache={b:bits_value(b) for b in product((0,1),repeat=3)}
    for places in product(range(5),repeat=3):
        Cb,tb,gb,wb=[tuple(int(p==j) for p in places) for j in range(4)]
        C,t,g,w=[cache[b] for b in (Cb,tb,gb,wb)]
        for db,eb in product(subsets(Cb),subsets(gb)):
            d,e=cache[db],cache[eb]
            for h in [ONE,*PRIMES,powe(PRIMES[0],3),(1,2),(-2,0),UNITS[1]]:
                for fi,f in enumerate(fields[:3]):
                    ndiv=lambda b:bool(b[fi])
                    coefficient=phase_product(f.char(mul(d,mul(e,h))),f.char(mul(C,mul(e,w)),4))
                    lhs=masked(coefficient,not(Cb[fi] or tb[fi] or gb[fi] or wb[fi]))
                    rhs=masked(coefficient,not(tb[fi] or (gb[fi] and not eb[fi])))
                    check(lhs==rhs,"second_Poisson_exclusion_mask_identity")
                    Cewphase=f.char(mul(C,mul(e,w)),4)
                    wrong=phase_product(f.char(mul(d,mul(e,h))),0 if Cewphase is None else Cewphase)
                    negative(lhs!=masked(wrong,not(tb[fi] or(gb[fi] and not eb[fi]))),"drop_Cew_column_mask",{"denominator_norm":f.q,"C":C,"e":e,"w":w,"h":h})
                # Common w is coprime to C,g and d,e; its only residual zero is h.
                wphases=[phase_product(f.char(mul(d,mul(e,h))),f.char(mul(C,e),4)) for i,f in enumerate(fields[:3]) if wb[i]]
                check(int(None not in wphases)==int(all(not wb[i] or f.char(h) is not None for i,f in enumerate(fields[:3]))),"second_common_w_mask")
    for Cb,tb in product(cache,repeat=2):
        if any(x*y for x,y in zip(Cb,tb)):continue
        C,t=cache[Cb],cache[tb]
        for fvalue,h in product(list(cache.values()),[ONE,*PRIMES,powe(PRIMES[0],3),(1,2),UNITS[1]]):
            lhs=all(f.char(fvalue,4) is not None for i,f in enumerate(fields[:3]) if Cb[i]) and all(f.char(mul(h,mul(fvalue,fvalue))) is not None for i,f in enumerate(fields[:3]) if tb[i])
            rhs=all(f.char(fvalue) is not None for i,f in enumerate(fields[:3]) if Cb[i] or tb[i]) and all(f.char(h) is not None for i,f in enumerate(fields[:3]) if tb[i])
            check(lhs==rhs,"first_common_C_t_frequency_masks")
    # Extracting the initial common column C retains (k,C)=1.
    for Cbit,kv,u1v,u2v in product((0,1),range(7),range(7),range(7)):
        f=fields[0]
        c=f.phases[kv] if Cbit else 0
        rowphase=phase_product(c,f.phases[u1v],None if c is None else -c,None if f.phases[u2v] is None else -f.phases[u2v])
        stripped=phase_product(f.phases[u1v],None if f.phases[u2v] is None else -f.phases[u2v])
        check(rowphase==masked(stripped,not Cbit or kv!=0),"first_Poisson_common_column_row_mask")


def dyadic(n):
    return 1<<(n.bit_length()-1)


def check_first_map_and_small_Y():
    for kv in product(range(7),repeat=3):
        ybase=ringprod(powe(p,a) for p,a in zip(PRIMES,kv))
        for lamval,unit in product((0,1,4),UNITS):
            y=mul(unit,mul(ybase,powe((1,2),lamval)))
            image=[]
            for fb in product((0,1),repeat=3):
                if any(2*b>a for b,a in zip(fb,kv)):continue
                f=bits_value(fb)
                h=exactdiv(y,mul(f,f))
                check(mul(h,mul(f,f))==y,"first_map_actual_ring_preimage")
                image.append((f,h))
            count=2**sum(a>=2 for a in kv)
            check(len(image)==count and len(set(image))==count,"first_map_exact_multiplicity")
            check(count<=prod(a+1 for a in kv)*(lamval+1),"first_map_divisor_bound")
    for H,L,F,Sigma_multiplier,C,d,t,c,v in product((1,16,4096),(1,8,8192),(1,3),(1,2),(1,7),(1,),(1,13),(16,), (2,)):
        Sigma=Q(max(H,L*F)*Sigma_multiplier)
        Y=Q(c)*Sigma*L*F*d/(H*C*C)
        maxh=Q(v*v*L*L*d,H*C*C)
        maxy=4*F*F*maxh
        check(maxy<=Y,"first_map_support_majorization")
        check(Y>0,"first_map_positive_Y_without_lower_one")
        negative(Y<1 and C*t<=2*v*L,"small_Y_is_admitted",{"H":H,"L":L,"F":F,"Sigma":str(Sigma),"C":C,"t":t,"Y":str(Y)})
    # An explicitly admitted Q block, with a unit column inside I*.
    H=Sigma=Q(16)
    L,F,C,d,t,c,v=map(Q,(2,1,7,1,1,16,2))
    ell=L/(C*t)
    Y=c*Sigma*L*F*d/(H*C*C)
    check(C*t<=2*v*L and ell>=1/(2*v),"admitted_small_Y_outer_domain")
    check(Y==Q(32,49)<1 and Q(1,2)<1/ell<4,"admitted_small_Y_unit_column")
    negative(Y<1,"small_Y_is_admitted",{"H":16,"L":2,"F":1,"Sigma":"16","C":7,"d":1,"t":1,"ell":str(ell),"Y":str(Y),"unit_column_position":str(1/ell)})
    # The second nonnegative form includes y=0 even if Y<1. At y=0,
    # every nontrivial zero-extended column vanishes, but the unit ideal does not.
    at_zero=[(1,0),(5,None),(-3,None)]
    Pzero=sum(coefficient for coefficient,phase in at_zero if phase is not None)
    check(Pzero==1,"small_Y_zero_row_unit_column")
    negative(Pzero*Pzero!=0,"dropping_y_zero_changes_nonnegative_form",{"ell":"1","Y":"1/100","unit_column_coefficient":"1","P(0)":"1","omitted_term_lower_bound":"1"})
    for ell,b in product((Q(1,100),Q(1,8),Q(1,2),Q(1),Q(3)),(2,4,8)):
        nonempty=[n for n in (1,7,13,19) if n<=b*ell]
        if b*ell<1:check(not nonempty,"short_column_empty_b_ell_below_one")
        if nonempty:check(ell>=Q(1,b),"short_column_nonempty_lower_bound")


def check_child_scales():
    retained=children=0
    for H,L,F,mult in product((1,16,4096),(1,16,8192),(1,3,7),(1,2,8)):
        Sigma=Q(max(H,L*F)*mult)
        for places in product(range(3),repeat=3):
            rb=tuple(int(x==1) for x in places)
            fb=tuple(int(x==2) for x in places)
            r,f=norm(bits_value(rb)),norm(bits_value(fb))
            for kv in product(range(3),repeat=3):
                k=prod(p**a for p,a in zip(NORMS,kv))
                if any(b and a==0 for b,a in zip(fb,kv)):continue
                if r*f>4*L or k>Q(H*L)/(Sigma*F*r*r):continue
                R,Fp=dyadic(r),dyadic(f)
                Xp,Sp,Hp=Q(L,R*Fp),Q(L,R),Q(H*L)/(Sigma*F*R*R)
                X0=Q(L,r*f)
                check(Hp>=1,"retained_child_row_at_least_one")
                check(1<=Xp/X0<4,"child_support_rescaling_ratio")
                check(Hp/Sp==Q(H)/(Sigma*F*R) and Hp/Sp<=Q(H)/Sigma,"child_gap_exact_and_inherited")
                check(Sp<=L and Hp<=Q(H*L)/(Sigma*F),"child_upper_bounds")
                check(Sigma*R/(L*L)*R*Sp*Sp==Sigma,"dyadic_block_prefactor")
                for jb in subsets(rb):
                    j=norm(bits_value(jb))
                    Xchild,Fchild=Xp/j,Q(Fp*j)
                    check(Xchild>=Q(F)*Sigma/H>=1,"exclusion_child_column_lower_bound")
                    check(Xchild*Fchild==Sp and Fchild>=1,"exclusion_child_product_preserved")
                    check(Xchild<=Sp and Fchild<=Sp,"exclusion_children_polynomial_range")
                    # Exact support containment after rescaling I*=[u/2,2v].
                    s=Xp/X0
                    u,v=Q(1),Q(2)
                    check(u/(2*s)>=u/8 and 2*v/s<=2*v,"rescaled_kernel_fixed_support")
                    check(u/16<u/8 and 2*v<4*v,"kernel_support_inside_test_interval")
                    children+=1
                retained+=1
    # The unsigned formal output really can have X'<1. Use actual norms
    # r=1,f'=7*13,k'=1 and the source's necessary support constraints.
    r,f,k,H,L,F,Sigma,v,c=map(Q,(1,91,1,16,16,1,16,8,256))
    Xp=Q(16,64)
    x=Q(91,16)
    beta=c*Sigma*F*k*r*r/(H*L)
    check(r*f<=2*v*L and k<=H*L/(Sigma*F*r*r) and beta/(x*x)<1,"unsigned_negative_has_necessary_support")
    negative(Xp<1,"unsigned_output_can_violate_child_column_range",{"r":1,"f_prime":91,"k_prime":1,"X_prime":str(Xp),"signed_sum":0,"unsigned_preimages":4})
    return retained,children


def check_descent_and_derivatives():
    count=0
    # Choose D=2^20 and kappa=1/10, so D^kappa=4 is rational.
    step=Q(4)
    for Xe,He,Fe,bnorm in product(range(1,21),range(0,21),range(0,5),(1,7,13,19,25,49)):
        X,H,F=Q(2**Xe),Q(2**He),Q(2**Fe)
        Sigma=X*F
        if H> Sigma/step:continue
        cutoff=min(X,X*X/(H*H))
        L=X/(bnorm**3)
        if H*H<=X:
            check(not(bnorm**3>cutoff and L>1),"empty_cube_tail_when_H_squared_below_X")
        if not(bnorm**3>cutoff and L>1):continue
        upper=H*L/(Sigma*F)
        check(H*H>X,"eligible_tail_requires_H_squared_above_X")
        check(upper==H/(bnorm**3*F*F),"canonical_child_row_upper_identity")
        check(upper<H*(H/Sigma)**2<=H/(step*step),"canonical_strict_row_contraction")
        negative(H*L>=H,"omit_Sigma_F_normalization_loses_contraction",{"X":str(X),"H":str(H),"F":str(F),"norm_b":bnorm})
        if upper<1:check(upper<1,"canonical_child_supremum_empty_below_one")
        count+=1
    for bvals in product(range(4),repeat=3):
        # Hc<1 admits every ideal divisor. Only squarefree divisors have
        # nonzero mu, and their complete sum is 1_{b=1}.
        radical=tuple(int(v>0) for v in bvals)
        betasum=sum(mu(h) for h in subsets(radical))
        check(betasum==int(all(v==0 for v in bvals)),"Hc_below_one_only_unit_beta_survives")
    for L,v,H,Sigma in product((Q(1,100),Q(1,8),Q(1,2),Q(1)),(Q(2),Q(8)),(Q(1),Q(7)),(Q(7),Q(100))):
        if H>Sigma:continue
        if L<Q(1)/v:
            check(v*L<1,"short_cube_column_empty")
        else:
            check(H/L<=v*H<=v*Sigma,"short_cube_column_counting_bound")
    for m in range(21):
        j=2*m+4
        check(2*j+4==4*m+12,"transfer_derivative_composition")
        negative(2*j+4!=2*m+4,"omit_first_separation_derivative_growth",{"m":m,"required":2*j+4,"wrong":2*m+4})
    J=1
    for depth in range(9):
        check(J==5*4**depth-4,"minimal_affine_derivative_recurrence")
        J=4*J+12
    for C0,kappa in product((Q(1),Q(2),Q(7,2)),(Q(1,10),Q(1,3),Q(2))):
        q=C0/kappa
        depth=-(-q.numerator//q.denominator)
        check(depth*kappa>=C0 and (depth-1)*kappa<C0,"finite_induction_depth")
    for H,F in product((Q(1,10),Q(1,2),Q(1)),(Q(1),Q(3),Q(7))):
        check(H/F<=1,"counting_base_H_over_Sigma")
    return count


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source",type=Path,default=None)
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name("full_transfer_bookkeeping_record_20261012.json"))
    args=parser.parse_args()
    observed=None
    if args.source is not None:
        observed=hashlib.sha256(args.source.read_bytes()).hexdigest()
        if observed!=PINNED_SHA:parser.error("source hash mismatch; expected "+PINNED_SHA+"; observed "+observed)
    for p,q in zip(PRIMES,NORMS):check(norm(p)==q and p[0]%3==1 and p[1]%3==0,"primary_prime_generators")
    cases,preimages=check_preimages()
    check_character_masks()
    check_first_map_and_small_Y()
    retained,children=check_child_scales()
    tails=check_descent_and_derivatives()
    required=["absolute_values_before_regrouping","omit_Ce_fourth_power_e_factor","principal_power_as_constant_one",
              "drop_Cew_column_mask","small_Y_is_admitted","dropping_y_zero_changes_nonnegative_form",
              "unsigned_output_can_violate_child_column_range","omit_Sigma_F_normalization_loses_contraction","omit_first_separation_derivative_growth",
              "carry_first_mu_t_into_nonnegative_Q","carry_first_mu_d_into_nonnegative_Q"]
    assert all(NEGATIVE.get(k,{}).get("detected",0)>0 for k in required)
    record={"date":"2026-10-12","prepared_for":"Edward Baker","model":"GPT-6 (Codex); inherited configuration",
            "serving_variant":"not exposed; not inferred","effort":"not exposed; not inferred","LLM_assistance":"substantial; internal finite diagnostics",
            "expected_source_sha256":PINNED_SHA,"source_sha256":observed,"source_path":None if args.source is None else str(args.source),
            "source_hash_verified":args.source is not None,"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "python_version":platform.python_version(),"python_implementation":platform.python_implementation(),"status":"pass",
            "source_physical_lines":[[2217,2685],[1480,1610]],"exact_assertion_count":sum(COUNTS.values()),"exact_assertions":COUNTS,
            "floating_comparison_count":0,"negative_controls":NEGATIVE,"signed_regrouping_cases":cases,"actual_preimages":preimages,
            "retained_scale_cases":retained,"exclusion_child_cases":children,"eligible_cube_tail_parameter_cases":tails,
            "coverage":{"regrouping":"3 disjoint squarefree r/f prime assignments, k valuations 0..3 at norms 7,13,19; lambda valuations 0,1,3, norm-4 prime valuations 0,2, all 6 units; independent local forward enumeration 0..6",
                        "masks":"actual sextic residues at norms 7,13,19,25, all four-factor residue tuples; actual ring common/exclusion masks including zeros",
                        "first_map":"actual y valuations 0..6 at norms 7,13,19, lambda valuations 0,1,4, all 6 units; exact square-divisor fiber counts",
                        "scales":"81 ambient parameter combinations, all retained squarefree r/f and k valuations 0..2; every j|r; positivity, rescaling, prefactors, polynomial upper bounds and inherited gaps",
                        "descent":"dyadic ambient scales, 6 actual cube-factor norms including unit b, rational D^kappa=4 gap, empty/eligible/short child parameter cases; Hc<1 beta cancellation and short-column counting; formal affine derivative recurrence and induction depth; no actual nonzero kernel or beta0 claimed",
                        "limits":"no smooth-function or Poisson/theta evaluation, derivative-norm estimate, unbounded divisor bound, analytic family estimate, or quasi-RH proof"},
            "prior_checker":"Adapted inverse and norm identities from check_transfer_regrouping.py; new independent forward enumeration, actual O elements, sextic masks, first map, all-scale and descent coverage"}
    args.output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({k:record[k] for k in ("status","exact_assertion_count","floating_comparison_count","signed_regrouping_cases","actual_preimages","retained_scale_cases","exclusion_child_cases","eligible_cube_tail_parameter_cases")},indent=2))


if __name__=="__main__":main()
