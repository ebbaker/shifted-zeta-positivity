#!/usr/bin/env python3
"""Fixed canonical whole rectangle bulk payment; see adjacent contract.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-22;
gpt-6.1-sol (Codex), reasoning effort ultra.
"""
import argparse
import hashlib
import importlib.util
import json
import platform
from pathlib import Path
import flint
from flint import arb,acb,ctx
import rhe_actual_theta_core as core_module
from rhe_actual_theta_core import ActualThetaCore


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--contract',type=Path,required=True)
    p.add_argument('--potential-script',type=Path,required=True)
    p.add_argument('--potential-receipt',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();ctx.prec=192
    spec=importlib.util.spec_from_file_location('signed_potential_helpers',args.potential_script)
    h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
    old=json.loads(args.potential_receipt.read_text())
    h.require(old['script_sha256']==h.digest(args.potential_script),'hash-bound potential helper')
    h.require(old['schema']=='rhe-signed-potential-v1','potential schema')
    level=old['attempted_levels'][-1]
    h.require(level['nx']==128 and level['ny']==64 and len(old['attempted_levels'])==1,'fixed accepted mesh')
    core=ActualThetaCore(bits=192,terms=65,center=35,radius=8,cauchy_radius=16)
    h.require(old['oracle_sha256']==h.digest(core_module.__file__),'same canonical oracle')
    coeff=[acb(core.coeff[k],(k+1)*core.coeff[k+1]) for k in range(core.N-1)]+[acb(core.coeff[-1])]
    third=sum((k*(k-1)*(k-2)*abs(coeff[k])*core.r**(k-3) for k in range(3,len(coeff))),arb(0)).upper()
    epsJ=(core.tail0+core.tail1).upper()
    epsJprime=(core.tail1+2*core.tail2half).upper()
    L=4*arb(2).sqrt();lower_sum=arb(0);upper_sum=arb(0)
    min_floor=None;upper_available=True;positive_lower_cells=0;zero_lower_cells=0
    for sc,sh,si0,*unused_x in h.axis_cells(-1,1,128):
        for vc,vh,vi0,*unused_y in h.axis_cells(0,1,64):
            f,f1,f2=h.jets(coeff,L*acb(sc,vc))
            r=L*(sh*sh+vh*vh).sqrt()
            d1=(abs(f1)+abs(f2)*r+third*r*r/2).upper()
            d2=(abs(f2)+third*r).upper()
            b=(abs(f)+d1*r+epsJ).upper()
            h.require(b>0,'positive cell denominator upper')
            derivative_lower=(abs(f1)-d2*r-epsJprime).lower()
            derivative_lower=max(arb(0),derivative_lower)
            mass=32*si0*vi0
            h.require(mass>0,'positive exact integrated cutoff weight')
            lower_sum+=mass*derivative_lower**2/b
            if derivative_lower>0:
                positive_lower_cells+=1
            else:
                zero_lower_cells+=1
            a=(abs(f)-d1*r-epsJ).lower()
            if a>0:
                min_floor=a if min_floor is None else min(min_floor,a)
                derivative_upper=(abs(f1)+d2*r+epsJprime).upper()
                upper_sum+=mass*derivative_upper**2/a
            else:
                upper_available=False
    lower=lower_sum.lower()
    previous=h.rational(old['bulk_lower_used']['lower_exact'])
    h.require(lower>previous,'strict improvement of existing mass lower')
    Plo=h.rational(old['potential']['lower_exact'])
    Phi=h.rational(old['potential']['upper_exact'])
    trace_upper=(Phi-lower).upper()
    trace_lower=(Plo-upper_sum.upper()).lower() if upper_available else None
    out=dict(schema='rhe-whole-rectangle-bulk-v1',date='2026-10-22',prepared_for='Edward Baker',
        model='gpt-6.1-sol',reasoning_effort='ultra',LLM_assistance='substantial',
        status='fixed whole rectangle canonical bulk payment interval-certified',
        python=platform.python_version(),python_flint=flint.__version__,bits=192,
        script_sha256=h.digest(__file__),contract_sha256=h.digest(args.contract),
        oracle_sha256=h.digest(core_module.__file__),potential_script_sha256=h.digest(args.potential_script),
        potential_receipt_sha256=h.digest(args.potential_receipt),geometry=old['geometry'],
        cells=8192,positive_density_lower_cells=positive_lower_cells,zero_density_lower_cells=zero_lower_cells,
        source_J_error=h.rec(epsJ),source_Jprime_error=h.rec(epsJprime),
        minimum_derived_canonical_J_floor=h.rec(min_floor) if upper_available else None,
        previous_disk_mass_lower_exact=old['bulk_lower_used']['lower_exact'],whole_rectangle_mass_lower=h.rec(lower),
        whole_rectangle_mass_upper=h.rec(upper_sum.upper()) if upper_available else None,
        trace_upper=h.rec(trace_upper),trace_lower=h.rec(trace_lower) if upper_available else None,
        improvement_factor_over_previous_mass_lower=h.rec(lower/previous),
        conditions=dict(strictly_improved_mass_lower=True,all_cell_weights_positive=True,
            lower_uses_no_J_floor=True,complete_mass_upper_available=upper_available,
            positive_area_derived_trace_certified=bool(trace_lower>0) if trace_lower is not None else False,
            all_source_coefficient_and_rounding_errors_retained=True),
        interpretation='P and bulk estimates use the same complete canonical data; correlations are conservatively enclosed. No global sign, RH, cap surplus, collision exclusion or method-cost dominance.')
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','whole_rectangle_mass_lower','whole_rectangle_mass_upper','trace_lower','trace_upper','conditions']}))


if __name__=='__main__':
    main()
