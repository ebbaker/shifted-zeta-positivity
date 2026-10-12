#!/usr/bin/env python3
"""Exact finite algebra for the original moment and final extraction chain.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-12.
Model GPT-6 (Codex), inherited configuration. Exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Standard library only. This checks exponents, normalizations and Euler
polynomials, not analytic estimates, smooth kernels, or a quasi-RH theorem.
Optional source hash is checked before any diagnostic arithmetic/output.
"""

import argparse
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path
import platform

PINNED_SHA="d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d"
COUNTS,NEGATIVE={},{}


def check(ok,label):
    assert ok,label
    COUNTS[label]=COUNTS.get(label,0)+1


def negative(ok,label,example):
    if ok:
        r=NEGATIVE.setdefault(label,{"detected":0,"example":example})
        r["detected"]+=1


def normalization_and_exponents():
    # Exact Z[zeta_6], zeta_6^2-zeta_6+1=0, including character zero.
    def rootmul(x,y):
        return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1]
    for value in ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1),(0,0)):
        sixth=(1,0)
        for _ in range(6):sixth=rootmul(sixth,value)
        check(sixth==((0,0) if value==(0,0) else (1,0)),"sixth_character_power_retains_zero_mask")
        negative(sixth!=(1,0),"replace_sixth_character_power_by_one",{"character_value":value,"sixth_power":sixth})
    D=Q(7)
    energies=(Q(3),Q(5),Q(11))
    weights=(Q(1),Q(2),Q(1))
    smoothed=sum(w*a for w,a in zip(weights,energies))
    MD=smoothed/D
    check(smoothed==D*MD,"restore_outside_D_exact_normalization")
    check(sum(energies)<=D*MD,"positive_weight_dominates_original_moment")
    negative(sum(energies)>MD,"omit_outside_D",{"D":"7","normalized_moment":str(MD),"original_subsum":str(sum(energies))})
    choices=[]
    for delta in (Q(1,10**6),Q(1,100),Q(1,24),Q(1,10),Q(1,2),Q(1),Q(7)):
        theta=min(Q(1,10),3*delta/5)
        moment_loss=delta/2
        logarithm_loss=delta/2
        total_loss=moment_loss+logarithm_loss
        Hexp=1+theta
        Yexp=Hexp/6
        moment_exp=1+Hexp+moment_loss
        square_main=moment_exp+logarithm_loss-Yexp
        square_error=2-2*Yexp
        main=square_main/2
        error=square_error/2
        check(0<theta<=Q(1,10),"positive_theta_choice")
        check(square_main==Q(11,6)+5*theta/6+total_loss,"prime_average_main_squared_exponent")
        check(square_error==Q(5,3)-theta/3,"prime_average_error_squared_exponent")
        check(main==Q(11,12)+5*theta/12+total_loss/2,"sixth_power_extraction_amplitude")
        check(error==Q(5,6)-theta/6<main,"prime_extraction_error_subordinate")
        check(main-Q(11,12)<=3*delta/4<delta,"requested_delta_with_reserved_margin")
        wrong=Q(11,12)+5*theta/12+(delta+delta)/2
        negative(wrong>Q(11,12)+delta,"double_spend_requested_loss",{"delta":str(delta),"theta":str(theta),"wrong_final_loss":str(wrong-Q(11,12))})
        negative(Q(11,12)+5*theta/12+total_loss>Q(11,12)+delta,"omit_square_root_loss_halving",{"delta":str(delta),"theta":str(theta)})
        check(Yexp*6==Hexp,"sixth_power_rows_fit_H_exponent")
        choices.append({"delta":str(delta),"theta":str(theta),"moment_loss":str(moment_loss),"logarithm_loss":str(logarithm_loss),"final_main_exponent":str(main),"error_exponent":str(error),"reserved_margin":str(Q(11,12)+delta-main)})
    for epsilon in (Q(1,100),Q(1,7),Q(1)):
        check(epsilon/3+epsilon/3+epsilon/3==epsilon,"canonical_three_loss_budget")
        check(epsilon/2+epsilon/2==epsilon,"Poisson_block_and_dyadic_loss_budget")
        negative(epsilon/2+epsilon/2+epsilon/2>epsilon,"overspend_three_half_losses",{"epsilon":str(epsilon)})
    # Actual ideal norm boundary: N(p^6)=N(p)^6, not N(p)^3.
    pnorm=7
    H=pnorm**6
    check(pnorm**6==H,"sixth_power_norm_boundary")
    wrongH=pnorm**3
    negative(pnorm**6>wrongH,"wrong_sixth_root_factor",{"norm_p":7,"wrong_H":wrongH,"wrong_Y":7,"actual_row_norm":pnorm**6})
    return choices


def initial_scales():
    thresholds=[]
    for theta,C in product((Q(1,100),Q(1,10),Q(1,24)),(Q(1),Q(2),Q(16),Q(100))):
        a,b=theta.numerator,theta.denominator
        n=1
        while 2**(a*n)<C:n+=1
        # D=2^(2bn) gives D^theta=2^(2an) and D^(theta/2)=2^(an).
        check(C<=2**(a*n),"fixed_C_large_D_threshold")
        check(C*Q(2)**(-2*a*n)<=Q(2)**(-a*n),"initial_gap_admits_kappa_theta_over_two")
        thresholds.append({"theta":str(theta),"C":str(C),"D_as_power_of_two_exponent":2*b*n,"D_to_theta_over_two":str(2**(a*n))})
    # Rational sample D^theta=4; retaining C explicitly detects premature use.
    D=Q(2**20)
    H=4*D
    for B,F,C,Nd in product((Q(1),Q(2),Q(16)),(Q(1),Q(3),Q(7)),(Q(1),Q(2),Q(4)),(Q(1),Q(7),Q(91))):
        X=D/(B*F)
        Sigma=X*F
        HH=C*D*D/(H*B*B)
        check(Sigma==D/B,"initial_XF_equals_D_over_B")
        check(HH/Sigma==C/(4*B),"initial_gap_retains_fixed_C_and_B")
        if HH>=1:check(B*B<=C*D/4,"nonempty_dual_rows_bound_B")
        v=Q(4)
        if X>=1/v:check(F<=v*D/B,"nonempty_initial_columns_bound_F")
        check((X/Nd)*(F*Nd)==Sigma,"divisor_exclusion_preserves_XF")
        check(H*B/(D*D)*B*Sigma*Sigma==H,"dyadic_b_count_restores_H")
        negative(H*B/(D*D)*Sigma*Sigma!=H,"omit_b_block_ideal_count",{"B":str(B),"missing_count_value":str(H*B/(D*D)*Sigma*Sigma),"target_H":str(H)})
    negative(Q(100,4)>Q(1,2),"drop_fixed_C_large_D_qualification",{"D":"2^20","theta":"1/10","C":"100","B":"1","gap":"25","required_gap":"1/2"})
    # theta=0 never supplies a positive power gap from C=B=1.
    negative(Q(1)>Q(1,2),"substitute_theta_zero_into_positive_gap",{"theta":"0","C":"1","B":"1","actual_gap":"1","positive_target_gap":"1/2"})
    for X,v in product((Q(1,100),Q(1,8),Q(1,2)),(Q(2),Q(8))):
        if X<1/v:check(v*X<1,"short_initial_column_empty")
        else:check(1/X<=v,"short_initial_nonempty_counting_constant")
    check(Q(1,2)<1,"initial_row_bound_below_one_empty")
    # A divisor shift really may cross X=1, while the unit column survives.
    X,F,Nd,Hdual,v=map(Q,(2,1,7,1,4))
    Xd,Fd=X/Nd,F*Nd
    check(Xd*Fd==X*F,"short_divisor_shift_product")
    check(Q(1)<1/Xd<v and Xd>=1/v,"short_divisor_shift_unit_support")
    check(Hdual/Xd<=v*Hdual<=v*(Xd*Fd),"short_divisor_shift_direct_counting_bound")
    negative(Xd<1,"assume_every_shifted_column_scale_at_least_one",{"X":"2","N(d)":"7","shifted_X":str(Xd),"shifted_F":str(Fd),"unit_position":str(1/Xd),"support":"[1,4]"})
    return thresholds


def pconstant(c):
    return {} if not c else {(0,0,0):c}


def padd(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,0)+v
        if not out[k]:del out[k]
    return out


def pmul(a,b):
    out={}
    for ka,va in a.items():
        for kb,vb in b.items():
            k=tuple(x+y for x,y in zip(ka,kb))
            out[k]=out.get(k,0)+va*vb
            if not out[k]:del out[k]
    return out


def local_linear(sign=1,variable="a"):
    # Formal independent variables a,g,T; a and g represent local values.
    return {(0,0,0):1,(1,0,1) if variable=="a" else (0,1,1):-sign}


def polynomial_text(poly):
    return [{"a_power":a,"g_power":g,"T_power":t,"coefficient":v} for (a,g,t),v in sorted(poly.items())]


def Euler_polynomials():
    one=pconstant(1)
    minus=local_linear(1)
    plus=local_linear(-1)
    split=pmul(minus,minus)
    inert=pmul(minus,plus)
    ramified=pmul(minus,one)
    check(split=={(0,0,0):1,(1,0,1):-2,(2,0,2):1},"split_base_change_local_polynomial")
    check(inert=={(0,0,0):1,(2,0,2):-1},"inert_base_change_local_polynomial")
    check(ramified==minus,"ramified_unramified_character_local_polynomial")
    # Norm-square at inert p induces nu(p)=chi(p)^2. A missing square fails.
    wronginert={(0,0,0):1,(1,0,2):-1}
    negative(wronginert!=inert,"omit_inert_norm_character_square",{"correct":"1-a^2 T^2","wrong":"1-a T^2"})
    # When chi=chi_{-3}, its primitive Hecke base change is trivial.
    # Both modulus-3 Dirichlet factors have omitted Euler factors at 3.
    primitiveHecke={(0,0,0):1,(0,0,1):-1}
    imprimitiveDirichlet=one
    check(pmul(imprimitiveDirichlet,primitiveHecke)==primitiveHecke,"ramified_base_change_finite_correction")
    negative(primitiveHecke!=imprimitiveDirichlet,"claim_uncorrected_ramified_base_change_equality",{"rational_prime":3,"primitive_Hecke_inverse_factor":"1-T","imprimitive_Dirichlet_inverse_product":"1","character":"chi_{-3}"})
    # Omitting an unramified prime from an imprimitive L-function multiplies
    # the L-function by its inverse local Euler polynomial.
    for kind,poly in (("split",split),("inert",inert),("ramified",ramified)):
        # Independently generate local Euler series through T degree 6.
        if kind=="split":series={(n,0,n):n+1 for n in range(7)}
        elif kind=="inert":series={(2*n,0,2*n):1 for n in range(4)}
        else:series={(n,0,n):1 for n in range(7)}
        truncated={k:v for k,v in pmul(series,poly).items() if k[2]<=6}
        check(truncated==one,"Euler_series_inverse_"+kind)
        check(pmul(one,poly)==poly,"imprimitive_omission_factor_"+kind)
        negative(poly!=one,"erase_imprimitive_finite_correction",{"type":kind})
    for q,kind in ((7,"split"),(13,"split"),(2,"inert"),(5,"inert"),(3,"ramified")):
        inv=(1-Q(1,q))**2 if kind=="split" else 1-Q(1,q*q) if kind=="inert" else 1-Q(1,q)
        check((1/inv)*inv==1,"imprimitive_correction_numeric_rational_"+kind)
    # All finite-order local factors stay nonzero in Re(s)>0: if sigma=a/b>0,
    # q^(a)>1, so q^(-sigma)<1. This checks the exact algebraic inequality,
    # not a numerical value of a complex Euler factor.
    for q,sigma in product((3,4,7,13,25),(Q(1,10**6),Q(1,12),Q(1),Q(7,2))):
        check(q**sigma.numerator>1 and sigma.denominator>0,"positive_half_plane_local_modulus_inequality")
    # Pole at s=1 can occur only in the trivial character. In a finite
    # abstract character group, multiplying by the distinguished order-two
    # character makes the other factor exactly that character if one is trivial.
    distinguished=(1,0)
    for chi in product(range(2),range(4)):
        other=((chi[0]+1)%2,chi[1])
        if chi==(0,0) or other==(0,0):
            check((chi if other==(0,0) else other)==distinguished,"pole_cancellation_other_factor_is_chi_minus_three")
    return {"split":polynomial_text(split),"inert":polynomial_text(inert),"ramified_unramified_character":polynomial_text(ramified),"ramified_induced_character_caveat":"primitive base change may recover a local factor absent from imprimitive Dirichlet factors; finite correction required"}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source",type=Path,default=None)
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name("final_assembly_record_20261012.json"))
    args=parser.parse_args()
    observed=None
    if args.source is not None:
        observed=hashlib.sha256(args.source.read_bytes()).hexdigest()
        if observed!=PINNED_SHA:parser.error("source hash mismatch; expected "+PINNED_SHA+"; observed "+observed)
    choices=normalization_and_exponents()
    thresholds=initial_scales()
    polynomials=Euler_polynomials()
    required=["omit_outside_D","replace_sixth_character_power_by_one","wrong_sixth_root_factor","double_spend_requested_loss","omit_square_root_loss_halving",
              "overspend_three_half_losses","omit_b_block_ideal_count","drop_fixed_C_large_D_qualification",
              "substitute_theta_zero_into_positive_gap","assume_every_shifted_column_scale_at_least_one","omit_inert_norm_character_square","claim_uncorrected_ramified_base_change_equality","erase_imprimitive_finite_correction"]
    assert all(NEGATIVE.get(k,{}).get("detected",0)>0 for k in required)
    record={"date":"2026-10-12","prepared_for":"Edward Baker","model":"GPT-6 (Codex); inherited configuration",
            "serving_variant":"not exposed; not inferred","effort":"not exposed; not inferred","LLM_assistance":"substantial; internal exact algebra diagnostics",
            "expected_source_sha256":PINNED_SHA,"source_sha256":observed,"source_path":None if args.source is None else str(args.source),
            "source_hash_verified":args.source is not None,"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "python_version":platform.python_version(),"python_implementation":platform.python_implementation(),"status":"pass",
            "source_physical_lines":[[665,770],[1000,1045],[1230,1248],[1613,1629]],"exact_assertion_count":sum(COUNTS.values()),
            "exact_assertions":COUNTS,"floating_comparison_count":0,"negative_controls":NEGATIVE,"positive_loss_choices":choices,
            "large_D_threshold_examples":thresholds,"Euler_polynomials":polynomials,
            "limits":"Exact normalization/exponent/formal-polynomial checks only. No ideal prime counting, moment estimate, kernel nonvanishing, canonical inequality, Mellin holomorphy, Hecke continuation, base-change theorem, Dirichlet nonvanishing, or quasi-RH theorem is established. Bounds concern fixed characters and fixed S; conductor/height uniformity is not supplied or tested."}
    args.output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"pass","exact_assertion_count":record["exact_assertion_count"],"floating_comparison_count":0,"negative_control_families":len(NEGATIVE),"script_sha256":record["script_sha256"]},indent=2))


if __name__=="__main__":main()
