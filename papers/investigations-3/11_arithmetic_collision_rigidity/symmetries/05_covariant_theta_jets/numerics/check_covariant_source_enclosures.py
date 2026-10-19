#!/usr/bin/env python3
"""Cancellation-safe complete theta source jets and a bounded interval comparison.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual effort ultra. Same-model internal checks.
Source derivatives are in u, not spectral derivatives or physical heat time.
Requires python-flint. No collision-exclusion claim is made.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import statistics
import time
import flint
from flint import arb, acb, ctx


def check(ok, message):
    if not ok:
        raise ArithmeticError(message)


def A(q):
    q = F(q)
    return arb(q.numerator) / q.denominator


def box(lo, hi):
    lo, hi = F(lo), F(hi)
    return arb(A((lo+hi)/2), A((hi-lo)/2).upper())


def mul_power(x, n):
    # Repeated integer multiplication also works for balls containing zero.
    out = x*0+1
    for _ in range(n):
        out = out*x
    return out


def add_poly(a, b, factor=1):
    out = list(a)+[0]*max(0, len(b)-len(a))
    for j,c in enumerate(b):
        out[j] += factor*c
    while len(out)>1 and not out[-1]:
        out.pop()
    return out


def next_source(p):
    # Existing recurrence, also in Investigation 22's square-control checker.
    out = [0]*(len(p)+1)
    for j,c in enumerate(p):
        out[j] += (1+4*j)*c
        out[j+1] -= 4*c
    return out


POLYS = [[0,-3,2]]
for _ in range(8):
    POLYS.append(next_source(POLYS[-1]))


def hermite(m):
    return [(-4)**j*math.factorial(2*m)//
            (math.factorial(2*j)*2**(m-j)*math.factorial(m-j))
            for j in range(m+1)]


def exact_checks():
    c = {0:-3, 2:1}
    rows=[]
    for r in range(9):
        p=[0]
        for m,v in c.items():
            p=add_poly(p,hermite(m),v)
        check(p==[8*v for v in POLYS[r]], 'combined covariant coefficients')
        check(p[0]==0, 'zero lattice mode not cancelled')
        rows.append({'source_order':r,'covariant_coefficients':{str(2*m):v for m,v in c.items()},
                     'combined_mode_coefficients':POLYS[r]})
        new={}
        for m,v in c.items():
            new[m+1]=new.get(m+1,0)+v
            if m:
                new[m-1]=new.get(m-1,0)-(2*m)*(2*m-1)*v
        c={m:v for m,v in new.items() if v}
    return rows


def horner(p,v):
    # Zero constant is factored before evaluation to preserve cancellation.
    out=v*0+p[-1]
    for c in reversed(p[1:-1]):
        out=out*v+c
    return out*v if p[0]==0 else out*v+p[0]


def source_tail(order, alo, ahi, bmax, modes):
    """Uniform absolute infinite n>modes tail on a rectangular source cell.

    bmax is an Arb upper enclosure of |Im u|; require bmax<pi/8.
    Polynomial and exponential factors use separate safe rectangle endpoints.
    The power-specific geometric ratios decrease with n.
    """
    check(F(0)<=alo<=ahi, 'tail requires nonnegative real source coordinate')
    check(bmax>=0 and bmax<arb.pi()/8, 'tail outside holomorphic strip')
    low=arb.pi()*(4*A(alo)).exp()
    high=arb.pi()*(4*A(ahi)).exp()
    c=(4*bmax).cos()
    check(c>0, 'nonpositive Gaussian decay')
    n=modes+1
    tail=arb(0)
    for j,p in enumerate(POLYS[order]):
        if p:
            ratio=(arb(n+1)/n)**(2*j)*(-c*low*(2*n+1)).exp()
            check(ratio<1, 'geometric source tail is not contracting')
            tail += abs(p)*(high*n*n)**j*(-c*low*n*n).exp()/(1-ratio)
    return (A(ahi).exp()*tail).upper()


def full_source(u, alo, ahi, bmax, orders, modes=8):
    """Complete jets: combine the mode polynomial before ball evaluation."""
    q=(4*u).exp()
    out=[u*0 for _ in orders]
    for n in range(1,modes+1):
        v=arb.pi()*n*n*q
        pref=(u-v).exp()
        for k,r in enumerate(orders):
            out[k] += pref*horner(POLYS[r],v)
    tails=[source_tail(r,alo,ahi,bmax,modes) for r in orders]
    for k,e in enumerate(tails):
        out[k] += acb(arb(0,e),arb(0,e)) if isinstance(u,acb) else arb(0,e)
    return out,tails


def load_baseline(repo):
    path=repo/'papers/investigations-3/11_arithmetic_collision_rigidity/numerics/check_positive_packets.py'
    spec=importlib.util.spec_from_file_location('s05_actual_source_baseline',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.source_jet,path


def baseline(u,alo,ahi,bmax,source_jet,modes=8):
    out=[u*0 for _ in range(3)]
    for n in range(1,modes+1):
        values=source_jet(u,n,0)
        for r in range(3):
            out[r] += values[r]
    tails=[source_tail(r,alo,ahi,bmax,modes) for r in range(3)]
    for r,e in enumerate(tails):
        out[r] += acb(arb(0,e),arb(0,e)) if isinstance(u,acb) else arb(0,e)
    return out,tails


def endpoint_taylor(h,endpoints,modes=8):
    """Uniform real [0,h] enclosure, using complete modular source evenness.

    Taylor through source order 7 (odd endpoint coefficients exactly zero).
    Remainder uses the complete eighth derivative on the same real cell.
    """
    u=box(0,h)
    u2=box(0,h*h)
    eighth,tails=full_source(u,F(0),h,arb(0),[8],modes)
    bound=abs(eighth[0]).upper()
    values=[]
    errors=[]
    for r in range(3):
        powers=list(range(r%2,7-r,2))
        terms={k:endpoints[r+k]/math.factorial(k) for k in powers}
        acc=terms[powers[-1]]
        for k in reversed(powers[:-1]):
            acc=acc*u2+terms[k]
        if r%2:
            acc=acc*u
        error=(bound*A(h)**(8-r)/math.factorial(8-r)).upper()
        values.append(acc+arb(0,error))
        errors.append(error)
    return values,{'complete_eighth_derivative_abs_bound':bound,
                   'eighth_derivative_mode_tail':tails[0],
                   'taylor_remainders':errors}


def rad(x):
    return max(x.real.rad(),x.imag.rad()) if isinstance(x,acb) else x.rad()


def rec(x):
    if isinstance(x,(arb,acb)):
        return x.str(45,more=True)
    if isinstance(x,dict):
        return {k:rec(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [rec(v) for v in x]
    return x


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--bits',type=int,default=192)
    parser.add_argument('--execution-model',required=True)
    parser.add_argument('--execution-effort',required=True)
    args=parser.parse_args()
    ctx.prec=args.bits
    started=time.monotonic()
    source_jet,baseline_path=load_baseline(args.repo)
    algebra=exact_checks()
    endpoints,endpoint_tails=full_source(arb(0),F(0),F(0),arb(0),list(range(7)))
    check(all(endpoints[r].contains(0) for r in (1,3,5)), 'modular odd endpoint diagnostic')
    # Analytic modular parity, not the finite diagnostic, justifies exact zeros.
    for r in (1,3,5):
        endpoints[r]=arb(0)
    cells=[]
    ratios={kind:[[] for _ in range(3)] for kind in ('real','shifted')}
    for kind in ('real','shifted'):
        for j in range(64):
            lo,hi=F(j,64),F(j+1,64)
            bmax=arb(0) if kind=='real' else arb.pi()/16
            u=box(lo,hi) if kind=='real' else acb(box(lo,hi),bmax)
            direct,tails=baseline(u,lo,hi,bmax,source_jet)
            fused,_=full_source(u,lo,hi,bmax,list(range(3)))
            check(all(a.overlaps(b) for a,b in zip(direct,fused)), 'matched source cells disagree')
            row_ratios=[]
            for r in range(3):
                ratio=rad(direct[r])/rad(fused[r])
                ratios[kind][r].append(ratio)
                row_ratios.append(ratio)
            cells.append({'kind':kind,'real_source_cell':[str(lo),str(hi)],
                          'direct':direct,'fused':fused,'common_mode_tails':tails,
                          'direct_over_fused_radius':row_ratios})
    parity=[]
    # Local comparison gate: all derivatives at the listed h<=1/64 improve.
    for h in (F(1,16),F(1,64),F(1,256),F(1,1024)):
        direct,tails=baseline(box(0,h),F(0),h,arb(0),source_jet)
        fused,_=full_source(box(0,h),F(0),h,arb(0),list(range(3)))
        taylor,budget=endpoint_taylor(h,endpoints)
        improvement=[rad(direct[r])/rad(taylor[r]) for r in range(3)]
        fused_improvement=[rad(fused[r])/rad(taylor[r]) for r in range(3)]
        check(all(a.overlaps(b) for a,b in zip(direct,taylor)), 'Taylor/direct mismatch')
        if h<=F(1,64):
            check(all(x>1 for x in improvement),'declared parity width gate failed')
        parity.append({'h':str(h),'source_cell':['0',str(h)],'direct':direct,
                       'fused':fused,'parity_taylor':taylor,
                       'direct_over_taylor_radius':improvement,
                       'fused_over_taylor_radius':fused_improvement,
                       'common_direct_tails':tails,'budget':budget,
                       'naive_value_remainder_integral_payment_t_le_one_fifth':
                           (A(h)*(A(h*h)/5).exp()*budget['taylor_remainders'][0]).upper(),
                       'in_primary_gate':h<=F(1,64)})
    # Additional point diagnostics; not substitutes for the Taylor proof.
    point_checks=[]
    for h in (F(1,64),F(1,256),F(1,1024)):
        enclosure,_=endpoint_taylor(h,endpoints)
        for u0 in (F(0),h/2,h):
            value,_=full_source(A(u0),u0,u0,arb(0),list(range(3)))
            check(all(a.contains(b) for a,b in zip(enclosure,value)), 'Taylor point containment')
            point_checks.append({'h':str(h),'point':str(u0),'contained':True})
    # A fixed weighted square mode has the local ladder but is not even.
    # A theta tail would change the control. Use the finite mode directly here.
    weighted_first=source_jet(arb(0),1,0)[1]
    check(not weighted_first.contains(0), 'weighted-mode control unexpectedly even')
    # Negative-u evaluation is reflection of the full source, never a reflected mode.
    negative_checks=[]
    for u0 in (F(1,64),F(1,4)):
        plus,_=full_source(A(u0),u0,u0,arb(0),list(range(3)))
        # Direct negative-u series needs a different tail bound; do not fake one.
        negative_checks.append({'negative_point':str(-u0),
                                'reflection_enclosure':[(-1)**r*plus[r] for r in range(3)],
                                'basis':'established complete-source modular parity'})
    summary={kind:[{'order':r,'minimum_direct_over_fused_radius_lower':min(x.lower() for x in v),
                    'maximum_direct_over_fused_radius_upper':max(x.upper() for x in v),
                    'median_radius_ratio_floating':statistics.median(map(float,v)),
                    'strictly_tighter_cells':sum(x>1 for x in v),'cell_count':len(v)}
                   for r,v in enumerate(data)] for kind,data in ratios.items()}
    paths=[baseline_path,
       args.repo/'papers/investigations-2/active/22_theta_manifold_geometry/numerics/certify_square_support_endpoint_collision.py',
       args.repo/'papers/investigations-3/11_arithmetic_collision_rigidity/notes/07_HODGE_MODULAR_DUALITY_AND_ROTATION_DEFECT_20261018.md',
       args.repo/'papers/investigations-3/11_arithmetic_collision_rigidity/research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md']
    record={'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker',
        'actual_model':args.execution_model,'actual_effort':args.execution_effort,
        'llm_assistance':'substantial; same-model interval implementation and internal review',
        'status':'bounded complete-source enclosure comparison; no spectral exclusion',
        'python':platform.python_version(),'python_flint':flint.__version__,'precision_bits':ctx.prec,
        'source_derivatives':[0,1,2],'retained_modes':8,
        'rounding':'outward Arb/Acb balls, complete infinite source tails; no quadrature',
        'primary_gate':{'target':'strictly smaller enclosing radius for every source derivative 0,1,2 on [0,h]',
                        'h':['1/64','1/256','1/1024'],'baseline':'existing source_jet at t=0, summed over modes 1..8 with common tails',
                        'method':'complete-source even Taylor polynomial through degree 7, eighth-derivative remainder',
                        'gate_passed':True},
        'exact_algebra':algebra,'endpoint_jets':endpoints,'endpoint_mode_tails':endpoint_tails,
        'whole_cover_summary':summary,
        'whole_cover':cells,'parity_comparison':parity,'point_diagnostics':point_checks,
        'weighted_mode_countercheck':{'first_derivative':weighted_first,'parity_shortcut_rejected':True},
        'negative_source_reflection':negative_checks,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_sha256':{str(p.relative_to(args.repo)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        'comparison_cost':'fixed 8 modes; endpoint setup through derivative 6, per-cell derivative 8; timings below are whole-run diagnostics, not matched speedup',
        'seconds':time.monotonic()-started,
        'not_established':['novel polynomial recurrence','improved physical H,Hx,Hxx error','new finite exclusion region',
                           'runtime speedup','global estimate','Newman bound','independent specialist review']}
    args.output.write_text(json.dumps(rec(record),indent=2)+'\n')
    print(json.dumps(rec({'passed':True,'bits':ctx.prec,'whole_cover_summary':summary,
                         'parity':[{k:row[k] for k in ('h','direct_over_taylor_radius')} for row in parity],
                         'seconds':record['seconds']}),indent=2))


if __name__=='__main__':
    main()
