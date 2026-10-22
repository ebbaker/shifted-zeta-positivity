#!/usr/bin/env python3
"""One complete Arb comparison on |z-35|<=8, t=0, not an RH certificate.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-22.
Recorded model gpt-6.1-sol, reasoning effort ultra. Requires python-flint0.9.
See Note04 and the fixed comparison contract for definitions and scope.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import platform
import time

import flint
from flint import acb, arb, ctx
from rhe_actual_theta_core import ActualThetaCore
from rhe_actual_theta_contract import acquire_roots, certify_count

BITS=160
BOUNDARY_LEVELS=(512,1024,2048,4096)
DIRECT_LEVELS=(32,64,128,256)
TARGET=arb(1)/4
I=acb(0,1)


def require(test,label):
    if not test:raise ArithmeticError(label)


def interval(x):
    require(x.is_finite(),'nonfinite reported interval')
    scale=10**6
    lo=(x.lower()*scale).floor().unique_fmpz()
    hi=(x.upper()*scale).ceil().unique_fmpz()
    return dict(ball=x.str(40),lower_exact=str(lo)+'/'+str(scale),
                upper_exact=str(hi)+'/'+str(scale),
                relative_diameter=((x.upper()-x.lower())/abs(x.mid())).str(20) if abs(x.mid())>0 else None)


def target_met(x):
    return x>0 and ((x.upper()-x.lower())/x.mid()).upper()<=TARGET


def principal_unit(core,z):
    unit=core.V_cell(z)
    require(unit.is_finite(),'unit cell outside polynomial range domain')
    require(unit.real>0 or not unit.imag.contains(0),'unit cell crosses square-root cut')
    return 1/unit.sqrt(analytic=True)


def certify_unit_chart(core,cells=512):
    started=time.perf_counter();floor=arb('1e100');ceiling=arb(0)
    for j in range(cells):
        theta=2*arb.pi()*arb(2*j+1,1)/(2*cells)
        z=35+8*acb(0,theta).exp()
        v=core.V_cell(z)
        require(v.is_finite() and abs(v).lower()>0,'boundary unit floor')
        require(v.real>0 or not v.imag.contains(0),'boundary unit log branch')
        floor=min(floor,abs(v).lower());ceiling=max(ceiling,abs(v).upper())
    require(core.V_cell(43).real>0,'positive square-root basepoint')
    # Exact count+roots make V holomorphic/nonzero. Max principles extend
    # these boundary bounds and this normalized logarithm to the whole disk.
    return dict(cells=cells,unit_floor_lower=floor.str(40),
                unit_ceiling_upper=ceiling.str(40),
                principal_log_normalized_positive_at_43=True,
                seconds=time.perf_counter()-started)


def boundary_consumer(core,roots,cells):
    started=time.perf_counter();before=core.counts.copy()
    alpha,beta=roots;m=(alpha+beta)/2;a=(beta-alpha)/2
    h=arb.pi()/cells;prefix=arb(0);Q=arb(0);residual=arb(0)
    for j in range(cells):
        theta=arb.pi()*arb(2*j+1,1)/(2*cells)
        e=acb(0,theta).exp();z=35+8*e
        shifted=z-m
        # |z-m|>a on the true boundary, so the root near 1 is coherent.
        y0=shifted*(1-(a/shifted)**2).sqrt(analytic=True)
        B=I*8*e*principal_unit(core,z)/y0
        require(B.is_finite(),'nonfinite boundary differential')
        within=prefix+h*arb('0.5','0.5')*B.real
        residual+=4*h*within*B.imag
        Q+=2*h*B.imag
        prefix+=h*B.real
    u0=((43-m)/a).acosh()
    p=arb(0)
    for j in range(cells):
        t=arb(2*j+1,1)/(2*cells)
        z=m+a*(u0*t).cosh()
        v=core.V_cell(z)
        require(v.is_finite() and v.real>0,'positive real unit on transverse cell')
        # V is exactly real on this real path by conjugation.
        p-=2*u0/cells/v.real.sqrt()
    require(Q>0 and p<0,'period sign convention')
    center=-Q*p
    energy=center+residual
    require(energy.is_finite(),'nonfinite boundary energy')
    return energy,dict(cells=cells,energy=interval(energy),Q=interval(Q),p=interval(p),
                       center=interval(center),exterior_correction=interval(residual),
                       cut_payment=interval(center/2),physical_payment=interval(center/2+residual),
                       primitive_half_boundary=prefix.str(35),target_met=target_met(energy),
                       unit_calls=core.counts['Vcell']-before['Vcell'],
                       seconds=time.perf_counter()-started)


def direct_consumer(core,roots,cells):
    started=time.perf_counter();before=core.counts.copy()
    alpha,beta=roots;m=(alpha+beta)/2;a=(beta-alpha)/2;d=m-35
    total=arb(0);h=arb.pi()/cells
    for j in range(cells):
        theta=arb.pi()*arb(2*j+1,1)/(2*cells)
        U=((-d*theta.cos()+(64+(a*a-d*d)*theta.sin()**2).sqrt())/a).acosh()
        require(U.is_finite() and U>0,'regularized domain extent')
        for k in range(cells):
            t=arb(2*k+1,1)/(2*cells)
            z=m+a*acb(U*t,theta).cosh()
            v=core.V_cell(z)
            require(v.is_finite() and abs(v).lower()>0,'direct cell unit floor')
            total+=4*h/cells*U/abs(v)
    require(total.is_finite() and total>0,'nonfinite direct energy')
    return total,dict(cells_per_direction=cells,energy=interval(total),target_met=target_met(total),
                      unit_calls=core.counts['Vcell']-before['Vcell'],seconds=time.perf_counter()-started)


def run():
    ctx.prec=BITS
    setup_started=time.perf_counter()
    root_started=time.perf_counter();roots,root_record=acquire_roots(80)
    root_seconds=time.perf_counter()-root_started
    count=certify_count(N=8192)
    core=ActualThetaCore(bits=BITS,terms=65).set_roots(*roots)
    chart=certify_unit_chart(core)
    setup_seconds=time.perf_counter()-setup_started
    setup_calls=core.counts.copy()
    brows=[];drows=[]
    for n in BOUNDARY_LEVELS:
        be,brow=boundary_consumer(core,roots,n);brows.append(brow)
        if brow['target_met']:break
    for n in DIRECT_LEVELS:
        de,drow=direct_consumer(core,roots,n);drows.append(drow)
        if drow['target_met']:break
    require(not(be.upper()<de.lower() or de.upper()<be.lower()),'disjoint rigorous method enclosures')
    lower=max(Fraction(brows[-1]['energy']['lower_exact']),Fraction(drows[-1]['energy']['lower_exact']))
    upper=min(Fraction(brows[-1]['energy']['upper_exact']),Fraction(drows[-1]['energy']['upper_exact']))
    shared=dict(lower_exact=str(lower),upper_exact=str(upper),
                meaning='exact intersection of the reported outward rational endpoint enclosures')
    btime=sum(x['seconds'] for x in brows);dtime=sum(x['seconds'] for x in drows)
    files=[Path(__file__),Path(__file__).with_name('rhe_actual_theta_core.py'),
           Path(__file__).with_name('rhe_actual_theta_contract.py'),
           Path(__file__).with_name('03_ACTUAL_THETA_COMPARISON_CONTRACT_20261022.md')]
    return dict(date='2026-10-22',prepared_for='Edward Baker',model='gpt-6.1-sol',reasoning_effort='ultra',
                status='outward-ball finite-fiber enclosure; implementation-specific comparison',
                python=platform.python_version(),python_flint=flint.__version__,flint=flint.__FLINT_VERSION__,
                precision_bits=BITS,source='H0(z)=xi((1+i*z)/2)/8; unchanged full canonical theta source',
                time=0,center=35,radius=8,relative_diameter_target='1/4',
                source_file_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
                roots=root_record,zero_count=count,unit_chart=chart,
                taylor=dict(terms=65,cauchy_radius=16,majorant=core.M.str(40),
                            field_tail=core.tail0.str(40),field_derivative_tail=core.tail1.str(40),
                            unit_tail=core.tail2half.str(40),
                            polynomial_third_derivative_radius9=core.Vthird.str(40)),
                common_setup=dict(seconds=setup_seconds,root_seconds=root_seconds,
                                  taylor_seconds=core.timings['setup'],unit_calls=setup_calls['Vcell'],
                                  canonical_xi_scalar_or_series_calls=2+168+count['canonical_xi_calls']),
                boundary_attempts=brows,direct_attempts=drows,
                comparison=dict(boundary_target_met=brows[-1]['target_met'],direct_target_met=drows[-1]['target_met'],
                                boundary_contains_direct=be.lower()<=de.lower() and be.upper()>=de.upper(),
                                direct_contains_boundary=de.lower()<=be.lower() and de.upper()>=be.upper(),
                                shared_intersection=shared,boundary_consumer_total_seconds=btime,
                                direct_consumer_total_seconds=dtime,
                                boundary_fresh_total_seconds=setup_seconds+btime,
                                direct_fresh_total_seconds=setup_seconds+dtime,
                                boundary_unit_calls=sum(x['unit_calls'] for x in brows),
                                direct_unit_calls=sum(x['unit_calls'] for x in drows),
                                direct_over_boundary_consumer_time=dtime/btime,
                                direct_over_boundary_fresh_time=(setup_seconds+dtime)/(setup_seconds+btime)),
                scope='Both receive identical source/root/unit oracle. Period observations and their energy identity may be reused by direct evaluation; no intrinsic method dominance, global RH or simplicity claim.')


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
