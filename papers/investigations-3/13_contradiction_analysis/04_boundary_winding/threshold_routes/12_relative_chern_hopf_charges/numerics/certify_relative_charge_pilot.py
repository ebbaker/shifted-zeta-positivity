#!/usr/bin/env python3
"""Bounded relative-charge/direct comparison, 21 October 2026.
Prepared for Edward Baker with substantial LLM assistance.
Authoring model gpt-6-astra (Codex), actual reasoning effort max.
Requires python-flint 0.9.0. Analytic payments are in BW12 Note 01.
No RH assumption, global simplicity conclusion, or independent review.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import signal
import time

import flint
from flint import arb, acb, ctx


def A(value):
    q = Q(value)
    return arb(q.numerator) / q.denominator


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def rec(value):
    return value.str(45, more=True)


def tails(j, T, Y, pi):
    """Complete omitted modes and retained exterior, N=4 and U=1.

    The integrand majorant is 2*pi^2*n^4*u^j*exp(
        T*u^2+(9+Y)*u-pi*n^2*exp(4*u)).
    Tangents of its concave log give the two integrals; the omitted-mode
    ratio is bounded independently of j by q below.
    """
    m = 5
    lam = pi*m*m
    b = 4*lam-9-Y
    q = A(Q(m+1, m))**4*(-pi*(2*m+1)).exp()
    require(T >= 0 and Y >= 0 and b > 0 and q < 1,
            'omitted-mode slope or ratio')
    require(16*lam > 2*T, 'omitted-mode concavity')
    omitted = 2*pi*pi*m**4*(-lam).exp()*math.factorial(j)/(b**(j+1)*(1-q))
    exterior = arb(0)
    for n in range(1,5):
        lam = pi*n*n
        d = 4*lam*arb(4).exp()-9-Y-2*T-j
        require(d > 0 and 16*lam*arb(4).exp() > 2*T,
                'retained exterior slope or concavity')
        exterior += 2*lam*lam*(T+9+Y-lam*arb(4).exp()).exp()/d
    return omitted.upper(), exterior.upper()


def acquire(kind, j, a, T, R, pi):
    calls = 0
    start = time.monotonic()
    def f(u, analytic):
        # All operations are entire; no branch-sensitive operation is used.
        nonlocal calls
        calls += 1
        q = (4*u).exp()
        v = acb(0)
        for n in range(1,5):
            lam = pi*n*n
            v += (2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
        if kind == 'moment':
            return ((1+R)*u+T*u*u).exp()*v*u**j
        phase = a*u
        trig = (phase.cos, phase.sin, phase.cos, phase.sin)[j % 4]()
        if j % 4 in (1,2):
            trig = -trig
        return u.exp()*v*u**j*trig
    core = acb.integral(f,0,1,abs_tol=arb('1e-32'),rel_tol=arb('1e-28'),
                        eval_limit=100000,depth_limit=30)
    require(core.is_finite() and core.imag.contains(0), 'finite real core')
    require(core.real.rad() < arb('1e-28'), 'core error budget')
    omitted, exterior = tails(j,T if kind=='moment' else arb(0),
                                R if kind=='moment' else arb(0),pi)
    tail = (omitted+exterior).upper()
    metadata = {'kind':kind,'order':j,'core':rec(core.real),
                'quadrature_radius':rec(core.real.rad().upper()),
                'omitted_modes_upper':rec(omitted),
                'retained_exterior_upper':rec(exterior),
                'callbacks':calls,'seconds':time.monotonic()-start}
    if kind == 'moment':
        require(core.real > 0, 'positive source moment')
        upper = (core.real.upper()+tail).upper()
        metadata['complete_upper'] = rec(upper)
        return upper, metadata
    midpoint = core.real.mid()
    error = (core.real.rad()+tail).upper()
    metadata.update({'midpoint':rec(midpoint),'complete_error_upper':rec(error),
                     'complete_enclosure':rec(arb(midpoint,error))})
    return (midpoint,error),metadata


def exact_controls(T,R):
    # H=w^2-2t, G=(-2t+w^2,2w), F=(-2t,2w).
    # On |t/T|^2+|w/R|^2=1, inf ||F|| = 2 min(T,R).
    b = 2*min(T,R)
    e = R*R
    require(e < b, 'quadratic charge-one homotopy')
    # Constant degree-zero reference v=(1,0) is challenged at (t,w)=(T,0).
    require(1+2*T > 1, 'degree-zero constant must reject quadratic event')
    # Cubic H=z^3-(4+6t)z+2: z^3=1; t=(-4+3z^2)/6.
    require(Q(-4+3,6) == Q(-1,6), 'real cubic event time')
    # Its time-zero discriminant, 4*4^3-27*2^2, is positive.
    require(4*4**3-27*2**2 == 148, 'cubic discriminant')
    return {'quadratic':{'H':'w^2-2t','reference':'(-2t,2w)',
            'reference_complex_determinant':'-4','reference_degree':1,
            'boundary_floor':str(b),'error_upper':str(e),'gap':str(b-e),
            'domain_radii':[str(T),str(R)],
            'constant_reference_degree':0,'constant_reference_norm':'1',
            'constant_reference_error_at_t_T_w_0':str(1+2*T),
            'direct_exclusion':'must fail because G(0,0)=0'},
            'cubic':{'H':'z^3-(4+6t)z+2','event_equations':'z^3=1; t=(-4+3z^2)/6',
            'event_jacobian':'-36 z^2, nonzero at all three events',
            'complex_events':3,'real_events':1,'real_event_time':'-1/6',
            'time_zero_discriminant':148,
            'scope':'exact algebra screen, not theta or a numerical boundary integral'}}


def run(bits):
    ctx.prec = bits
    start = time.monotonic()
    a,T,R = A(Q(113,4)),A(Q(1,100)),A(Q(1,8))
    pi = arb.pi()
    coeff=[]; delta=[]; rows=[]
    for j in range(4):
        (c,d),row=acquire('jet',j,a,T,R,pi)
        coeff.append(c);delta.append(d);rows.append(row)
    moments={}
    for j in range(2,6):
        moments[j],row=acquire('moment',j,a,T,R,pi)
        rows.append(row)
    errors=[];remainders=[]
    for j in (0,1):
        rem=(R*R*moments[j+2]+2*R*T*moments[j+3]+T*T*moments[j+4])/2
        rem=rem.upper(); remainders.append(rem)
        errors.append((delta[j]+R*delta[j+1]+T*delta[j+2]+rem).upper())
    b=(coeff[1].abs_lower()-R*abs(coeff[2])-T*abs(coeff[3])).lower()
    e=(errors[0]**2+errors[1]**2).sqrt().upper()
    boundary_gap=(b-e).lower()
    direct_gap=(b-errors[1]).lower()
    require(b>0 and boundary_gap>A('0.00007495'), 'paid zero-degree boundary gap')
    require(direct_gap>A('0.00007993'), 'paid direct derivative gap')
    require(direct_gap>boundary_gap, 'fixed-component comparison')
    # The real t=0 line has a unique simple zero in [a-R/2,a+R/2].
    w=R/2
    sign_error=(delta[0]+w*delta[1]+w*w*moments[2]/2).upper()
    left=arb(coeff[0]-w*coeff[1],sign_error)
    right=arb(coeff[0]+w*coeff[1],sign_error)
    require(left>0 and right<0 and coeff[1]<0, 'nonvacuous simple-zero coverage')
    direct_rows=[r for r in rows if (r['kind']=='jet' and r['order'] in (1,2,3))
                                      or (r['kind']=='moment' and r['order'] in (3,4,5))]
    require(len(direct_rows)==6 and len(rows)==8, 'acquisition subset accounting')
    return {'bits':bits,'seconds':time.monotonic()-start,
            'domain':{'type':'smooth complex ellipsoid',
                      'center_t':'0','center_z':'113/4','time_radius':'1/100','space_radius':'1/8',
                      'definition':'|t/(1/100)|^2+|(z-113/4)/(1/8)|^2 < 1',
                      'orientation':'dRe(t) dIm(t) dRe(z) dIm(z)',
                      'physical_slice':'real ellipse, including t=0 and z in (28.125,28.375)'},
            'reference':'(c0+c1*w-c2*t, c1+c2*w-c3*t), w=z-113/4',
            'reference_degree':0,'certified_charge':0,
            'source_acquisitions':rows,'component_remainders':[rec(v) for v in remainders],
            'component_complete_errors':[rec(v) for v in errors],
            'reference_floor_lower':rec(b),'vector_error_upper':rec(e),
            'boundary_gap_lower':rec(boundary_gap),'direct_derivative_floor_lower':rec(direct_gap),
            'gap_ratio_direct_over_boundary':rec(direct_gap/boundary_gap),
            'root_bracket':{'t':'0','left_z':'451/16','right_z':'453/16',
                            'left_H':rec(left),'right_H':rec(right),
                            'unique_and_simple':'real monotonicity from derivative exclusion'},
            'cost':{'boundary_scalar_integrals':8,'direct_scalar_integrals':6,
                    'boundary_callbacks':sum(r['callbacks'] for r in rows),
                    'direct_subset_callbacks':sum(r['callbacks'] for r in direct_rows),
                    'boundary_acquisition_seconds':sum(r['seconds'] for r in rows),
                    'direct_subset_acquisition_seconds':sum(r['seconds'] for r in direct_rows),
                    'timing_scope':'one shared acquisition; direct time sums its required subset, not a separate timed run',
                    'boundary_mesh_cells':0,'interior_mesh_cells':0,
                    'coverage':'both bounds apply throughout the same ellipsoid; the majorants also cover the containing polydisc',
                    'extra_root_bracket':'no extra integrals; uses already acquired boundary inputs; not needed for exclusion'}}


def main():
    signal.alarm(180)
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--bits',type=int,default=192)
    args=p.parse_args()
    require(args.bits>=128,'minimum precision')
    result={'schema':'rch12-bounded-relative-charge-v1','date':'2026-10-21',
            'timezone':'America/New_York','prepared_for':'Edward Baker',
            'authoring_model':'gpt-6-astra','actual_effort':'max',
            'LLM_assistance':'substantial; same-assistant derivation and checks',
            'status':'finite interval certificate and scoped comparison; no global theta conclusion',
            'python':platform.python_version(),'python_flint':flint.__version__,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'parameters':{'modes':4,'source_cutoff':'1','abs_quad_tolerance':'1e-32',
                          'rel_quad_tolerance':'1e-28','max_seconds':180,
                          'eval_limit_per_integral':100000,'depth_limit':30},
            'controls':exact_controls(Q(1,100),Q(1,8)), 'run':run(args.bits)}
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    r=result['run']
    print(json.dumps({k:r[k] for k in ('certified_charge','reference_floor_lower',
          'vector_error_upper','boundary_gap_lower','direct_derivative_floor_lower','cost')}))

if __name__=='__main__':
    main()
