#!/usr/bin/env python3
"""Fixed signed potential enclosure. Prepared for Edward Baker, 2026-10-22.

Substantial LLM assistance; gpt-6.1-sol (Codex), effort ultra.
See 07_SIGNED_POTENTIAL_CONTRACT_20261022.md for proof and fixed budget.
"""
import argparse
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb,acb,ctx
import rhe_actual_theta_core as core_module
from rhe_actual_theta_core import ActualThetaCore


def require(value,label):
    if not value:
        raise ArithmeticError(label)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rec(value):
    require(value.is_finite(),'nonfinite output')
    scale=10**35
    lo=(value.lower()*scale).floor().unique_fmpz()
    hi=(value.upper()*scale).ceil().unique_fmpz()
    require(lo is not None and hi is not None,'unresolved exact endpoints')
    return dict(ball=value.str(35),lower_exact=f'{lo}/{scale}',upper_exact=f'{hi}/{scale}')


def rational(text):
    f=Fraction(text)
    return arb(f.numerator)/f.denominator


def w(x):
    return (1-x*x)**3


def wp(x):
    return -6*x*(1-x*x)**2


def wpp(x):
    return -6+36*x*x-30*x**4


def F(x):
    return x-x**3+3*x**5/5-x**7/7


def xF(x):
    return x*x/2-3*x**4/4+x**6/2-x**8/8


def xD(x):
    return x*wp(x)-w(x)


def axis_cells(a,b,n):
    out=[]
    for j in range(n):
        left=arb(a)+arb(b-a)*j/n
        right=arb(a)+arb(b-a)*(j+1)/n
        c=(left+right)/2;half=(right-left)/2
        box=c+arb(0,half.abs_upper())
        i0=F(right)-F(left)
        i1=xF(right)-xF(left)-c*i0
        d0=wp(right)-wp(left)
        d1=xD(right)-xD(left)-c*d0
        out.append((c,half,i0,i1,d0,d1,abs(w(box)).upper(),abs(wpp(box)).upper()))
    return out


def jets(coeff,z):
    p=acb(coeff[-1]);d=acb(0);e=acb(0)
    for c in coeff[-2::-1]:
        e=e*z+2*d
        d=d*z+p
        p=p*z+c
    return p,d,e


def mesh(coeff,third,L,nx,ny,source_error):
    xs=axis_cells(-1,1,nx);ys=axis_cells(0,1,ny)
    center_sum=arb(0);error_sum=arb(0);kernel_sum=arb(0);kernel_abs=arb(0)
    floor_count=0;fallback_count=0;min_floor=None;max_hessian=arb(0)
    for sc,sh,si0,si1,sd0,sd1,sw,sd in xs:
        for vc,vh,vi0,vi1,vd0,vd1,vw,vd in ys:
            k00=sd0*vi0+si0*vd0
            k10=sd1*vi0+si1*vd0
            k01=sd0*vi1+si0*vd1
            kab=(2*sh)*(2*vh)*(sd*vw+sw*vd)
            require(kab>=0,'nonnegative kernel allowance')
            kernel_sum+=k00;kernel_abs+=kab
            r=L*(sh*sh+vh*vh).sqrt()
            f,f1,f2=jets(coeff,L*acb(sc,vc))
            u=abs(f)
            m1=(abs(f1)+abs(f2)*r+third*r*r/2).upper()
            m2=(abs(f2)+third*r).upper()
            lower=(u-m1*r).lower()
            if lower>0:
                floor_count+=1
                min_floor=lower if min_floor is None else min(min_floor,lower)
                gx=L*(f1*f.conjugate()).real/u
                gy=L*(acb(0,1)*f1*f.conjugate()).real/u
                hessian=(m2+m1*m1/lower).upper()
                max_hessian=max(max_hessian,hessian)
                center_sum+=u*k00+gx*k10+gy*k01
                error_sum+=hessian*r*r*kab/2
            else:
                fallback_count+=1
                center_sum+=u*k00
                error_sum+=m1*r*kab
    require(kernel_sum.contains(0),'signed kernel cancellation')
    total_error=(error_sum+source_error).abs_upper()
    potential=center_sum+arb(0,total_error)
    return potential,dict(nx=nx,ny=ny,cells=nx*ny,
        affine_cells=floor_count,lipschitz_fallback_cells=fallback_count,
        minimum_derived_polynomial_modulus_floor=rec(min_floor) if min_floor is not None else None,
        maximum_hessian_bound=rec(max_hessian),
        signed_kernel_sum=rec(kernel_sum),absolute_kernel_upper=rec(kernel_abs),
        signed_affine_sum=rec(center_sum),quadrature_error_allowance=rec(error_sum),
        source_error_allowance=rec(source_error),potential=rec(potential),
        accuracy_target_passed=bool(potential.rad()<=arb('5e-7')))


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--contract',type=Path,required=True)
    p.add_argument('--bulk-receipt',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();ctx.prec=192
    core=ActualThetaCore(bits=192,terms=65,center=35,radius=8,cauchy_radius=16)
    coeff=[acb(core.coeff[k],(k+1)*core.coeff[k+1]) for k in range(core.N-1)]+[acb(core.coeff[-1])]
    third=sum((k*(k-1)*(k-2)*abs(coeff[k])*core.r**(k-3) for k in range(3,len(coeff))),arb(0)).upper()
    L=4*arb(2).sqrt()
    # Exact geometry: L²+h²=32+32=64 equals source radius².
    require(core.r==8 and core.C==35,'fixed source geometry')
    kernel_norm=arb(12288)/(875*arb(5).sqrt())
    source_error=((core.tail0+core.tail1)*kernel_norm).upper()
    old=json.loads(args.bulk_receipt.read_text())
    require(old['schema']=='rhe-canonical-bulk-lower-v1' and old['geometry']['time']=='0','bulk receipt schema')
    require(old['oracle_sha256']==digest(core_module.__file__),'same canonical source oracle')
    require(old['geometry']['source_center']=='35' and old['geometry']['cutoff_half_width_and_height']=='4sqrt(2)','same bulk geometry')
    delta=rational(old['M_phi_lower']['lower_exact'])
    levels=[]
    for nx,ny in [(128,64),(256,128)]:
        potential,level=mesh(coeff,third,L,nx,ny,source_error)
        levels.append(level)
        if level['accuracy_target_passed']:
            break
    require(levels[-1]['accuracy_target_passed'],'frozen mesh budget did not reach accuracy target')
    combined=(potential-delta).upper()
    out=dict(schema='rhe-signed-potential-v1',date='2026-10-22',prepared_for='Edward Baker',
        model='gpt-6.1-sol',reasoning_effort='ultra',LLM_assistance='substantial',
        status='fixed canonical signed potential interval-certified',
        python=platform.python_version(),python_flint=flint.__version__,bits=192,
        script_sha256=digest(__file__),oracle_sha256=digest(core_module.__file__),
        contract_sha256=digest(args.contract),bulk_receipt_sha256=digest(args.bulk_receipt),
        geometry=dict(time='0',center='35',half_width='4sqrt(2)',height='4sqrt(2)',
            source_radius='8',outer_cauchy_radius='16',terms=65,source_inclusion='32+32=64'),
        polynomial_third_derivative_upper=rec(third),source_J_error=rec(core.tail0+core.tail1),
        source_potential_error=rec(source_error),bulk_lower_used=rec(delta),
        attempted_levels=levels,potential=rec(potential),trace_upper_via_previous_bulk_lower=rec(combined),
        conditions=dict(accuracy_target_passed=True,signed_kernel_retained=True,
            root_free_fallback_available=True,all_source_coefficient_and_rounding_errors_retained=True,
            positive_potential_certified=bool(potential>0),negative_trace_upper_certified=bool(combined<0)),
        scope='Fixed amplitude-weighted spatial trace. No RH, global signed margin, cap surplus or new collision conclusion.')
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','potential','trace_upper_via_previous_bulk_lower','conditions']}))


if __name__=='__main__':
    main()
