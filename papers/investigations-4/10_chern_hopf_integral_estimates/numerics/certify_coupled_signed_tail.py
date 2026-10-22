#!/usr/bin/env python3
"""Finite common-tail signed theta certificate, 22 October 2026.

Prepared for Edward Baker with substantial LLM assistance.
Recorded authoring model gpt-6.1-sol, effort ultra.
Requires python-flint 0.9.0. No RH assumption or exclusion conclusion.
Analytic proof and comparator scope are in local Note 02.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import signal
import time

import flint
from flint import acb, arb, ctx


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def rec(value):
    return value.str(85, more=True)


def controls():
    # At its event, the heat-weighted positive atomic source has masses
    # (9/10,1,1/10) at u=(0,1,2), and x=pi. An event at T=1/4 uses
    # original masses multiplied by exp(-T*u^2). Both equations vanish.
    pi = arb.pi()
    h2,h1,h0 = arb(-1),arb(0),-arb(1)/10
    m0,m4,m6,m8 = arb(1)/10,arb(8)/5,arb(32)/5,arb(128)/5
    exact_c2 = -arb(3)/5
    start = h2-h1/pi-pi**2*m4/3
    end = start+pi**4*m6/30
    end2 = h2+8*(-h0-m0)/pi**2-5*h1/pi+pi**4*m6/90
    start2 = end2-pi**6*m8/1680
    require(start < exact_c2 and exact_c2 < end,
            'one-equation estimator retains atomic collision')
    require(start2 < exact_c2 and exact_c2 < end2,
            'two-equation estimator retains atomic collision')
    return {'exact_event_control':{
        'heat_time':'1/4','height':'pi','heat_weighted_masses':['9/10','1','1/10'],
        'nodes':[0,1,2],'C0':'0','S1':'0','C2':'-3/5','C4':'3/5',
        'S3':'0','F':'-9/25','ordinary_double':True,
        'first_estimator_interval':[rec(start),rec(end)],
        'both_estimator_interval':[rec(start2),rec(end2)],
        'result':'both estimators retain the collision; no generic exclusion'},
        'published_family_screen':{
            'Euler_factor':'generic positive-source inequalities pass; unchanged canonical source and its recorded mode moments fail',
            'weighted_square':'generic inequalities pass; full reflection and unchanged coefficients fail',
            'reflected_super_Gaussian':'generic inequalities pass; integer-square canonical expansion fails',
            'smooth_shape_and_primitive':'generic inequalities pass; canonical arithmetic expansion fails',
            'finite_prime_orbit':'generic inequalities pass; full reflection and unchanged coefficients fail',
            'fixed_event_and_finite_profile':'generic inequalities pass; unchanged canonical source and full profile fail',
            'RH_conditional_endpoint':'generic inequalities pass; unchanged canonical source and ordinary Dirichlet arithmetic fail'},
        'screen_scope':'analytic application of proved universal kernel inequalities to the published controls; not a recomputation of their witnesses'}


ROOT_CENTER = '31.171417179658684689191458471044708211406421697860907074476119403575'


class Source:
    def __init__(self, bits):
        ctx.prec = bits
        self.pi = arb.pi()
        self.rows = []

    def omitted(self, j, first=8):
        # At t=0, exp(9u-lambda exp(4u)) <= exp(-lambda-bu).
        lam = self.pi*first**2
        b = 4*lam-9
        ratio = (arb(first+1)/first)**4*(-self.pi*(2*first+1)).exp()
        require(b > 0 and ratio < 1, 'omitted-tail prerequisites')
        return (2*lam**2*(-lam).exp()*math.factorial(j)
                / (b**(j+1)*(1-ratio))).upper()

    def exterior(self, j, first, last):
        # u^j <= exp(j(u-1)) for u>=1; concave exponent tangent at 1.
        out = arb(0)
        for n in range(first, last+1):
            lam = self.pi*n*n
            slope = 4*lam*arb(4).exp()-9-j
            require(slope > 0, 'exterior-tail prerequisite')
            out += 2*lam**2*(9-lam*arb(4).exp()).exp()/slope
        return out.upper()

    def crude_moment(self, j):
        out = arb(0)
        for n in range(1, 8):
            lam = self.pi*n*n
            b = 4*lam-9
            out += 2*lam**2*(-lam).exp()*math.factorial(j)/b**(j+1)
        return (out+self.omitted(j)).upper()

    def acquire(self, label, j, first, last, x=None, complete=False):
        start = time.monotonic()
        calls = 0
        def integrand(u, analytic):
            nonlocal calls
            calls += 1
            q = (4*u).exp()
            value = acb(0)
            for n in range(first, last+1):
                lam = self.pi*n*n
                value += (2*lam**2*q*q-3*lam*q)*(-lam*q).exp()
            value *= u.exp()*u**j
            if x is not None:
                value *= (x*u).sin() if j % 2 else (x*u).cos()
            return value
        core = acb.integral(integrand, 0, 1, abs_tol=arb('1e-78'),
                            rel_tol=arb('1e-75'), eval_limit=150000,
                            depth_limit=35)
        require(core.is_finite() and core.imag.contains(0), label+' real core')
        require(core.real.rad() < arb('1e-72'), label+' quadrature payment')
        exterior = self.exterior(j, first, last)
        omitted = self.omitted(j, last+1) if complete else arb(0)
        error = (core.real.rad()+exterior+omitted).upper()
        result = arb(core.real.mid(), error)
        if x is None:
            require(result > 0, label+' positive moment')
        self.rows.append({'label':label, 'order':j, 'first_mode':first,
                          'last_mode':last, 'complete_tail':complete,
                          'quadrature_radius':rec(core.real.rad().upper()),
                          'retained_exterior_upper':rec(exterior),
                          'omitted_modes_upper':rec(omitted),
                          'enclosure':rec(result), 'callbacks':calls,
                          'seconds':time.monotonic()-start})
        return result


def run(bits):
    source = Source(bits)
    started = time.monotonic()
    x = arb(ROOT_CENTER)
    omega = arb('1e-60')
    wall = arb(x, omega)
    h2 = source.acquire('head_C2', 2, 1, 3, x)
    h1 = source.acquire('head_S1', 1, 1, 3, x)
    h0 = source.acquire('head_C0', 0, 1, 3, x)
    moments = {j: source.acquire('tail_M'+str(j),j,4,7,complete=True)
               for j in (0,2,4,6,8)}
    m2,m4,m6 = [moments[j] for j in (2,4,6)]
    s1 = source.acquire('full_S1_at_center',1,1,7,x,complete=True)
    value = source.acquire('full_C0_at_center',0,1,7,x,complete=True)
    b3 = source.crude_moment(3)
    b2 = source.crude_moment(2)
    # S1_x=C2. The M2 tail and complete M3 pay the whole root bracket.
    derivative = arb(h2, (m2.upper()+b3*omega).upper())
    left_s1 = s1-omega*arb(h2,m2.upper())+arb(0,(b3*omega**2/2).upper())
    right_s1 = s1+omega*arb(h2,m2.upper())+arb(0,(b3*omega**2/2).upper())
    require(derivative < 0 and left_s1 > 0 and right_s1 < 0,
            'unique regular critical point in stated bracket')
    # H_x=0 at the actual root; Taylor from that root pays C0 variation.
    value = arb(value,(b2*omega**2/2).upper())
    require(value < 0, 'known sign of critical value')
    sigma, k = -1, arb(1)
    # Head acquisition errors plus wall errors. Interval arithmetic pays
    # the dependence of 1/x and the polynomial coefficients on wall.
    h2wall = arb(h2,(b3*omega).upper())
    h1wall = arb(h1,(b2*omega).upper())
    h0wall = arb(h0,(source.crude_moment(1)*omega).upper())
    base = h2wall-k*value
    separate = arb(base,m2.upper())
    taylor_start = base+m2-wall**2*m4/2
    taylor_end = taylor_start+wall**4*m6/24
    coupled_start = base-h1wall/wall-wall**2*m4/3
    coupled_end = coupled_start+wall**4*m6/30
    m0,m8 = moments[0],moments[8]
    value_coupled_end = (base+8*(value-h0wall-m0)/wall**2
                         -5*h1wall/wall+wall**4*m6/90)
    value_coupled_start = value_coupled_end-wall**6*m8/1680
    taylor6_end = base+m2-wall**2*m4/2+wall**4*m6/24
    taylor6_start = taylor6_end-wall**6*m8/720
    # Endpoints themselves carry acquisition balls; use outward endpoints.
    direct_interval = (separate.lower(),separate.upper())
    taylor_interval = (taylor_start.lower(),taylor_end.upper())
    coupled_interval = (coupled_start.lower(),coupled_end.upper())
    value_coupled_interval = (value_coupled_start.lower(),value_coupled_end.upper())
    taylor6_interval = (taylor6_start.lower(),taylor6_end.upper())
    lower_gain = (coupled_interval[0]-direct_interval[0]).lower()
    upper_gain = (direct_interval[1]-coupled_interval[1]).lower()
    taylor_lower_gain = (coupled_interval[0]-taylor_interval[0]).lower()
    taylor_upper_gain = (taylor_interval[1]-coupled_interval[1]).lower()
    require(lower_gain > 0 and upper_gain > 0,
            'strict complete containment versus separate M2')
    require(taylor_lower_gain > 0 and taylor_upper_gain > 0,
            'strict complete containment versus one-sided cos Taylor')
    width_d = direct_interval[1]-direct_interval[0]
    width_t = taylor_interval[1]-taylor_interval[0]
    width_c = coupled_interval[1]-coupled_interval[0]
    width_vc = value_coupled_interval[1]-value_coupled_interval[0]
    width_t6 = taylor6_interval[1]-taylor6_interval[0]
    require(value_coupled_interval[0] > taylor6_interval[0]
            and value_coupled_interval[1] < taylor6_interval[1],
            'finite strict containment versus same-moment sixth-order cosine')
    require(value_coupled_interval[0] > coupled_interval[0]
            and value_coupled_interval[1] < coupled_interval[1],
            'finite strict containment versus first coupled interval')
    require(width_vc/width_t6 < arb('0.4285714286'),
            'both-constraint finite width gain')
    require(width_c/width_d < arb('0.1'), 'recorded separate-width gain')
    require(width_c/width_t < arb('0.8000000001'), 'recorded Taylor-width gain')
    # These sufficient conditions use full moments, not tail asymptotics.
    require(wall**2*m4 < 4*m2 and wall**2*m6 < 12*m4,
            'analytic sufficient-condition check')
    # Signed amplitude reverses both endpoints because sigma=-1.
    signed = [-value_coupled_interval[1],-value_coupled_interval[0]]
    # A direct signed tail integral is the stronger same-source comparator.
    tail_c2 = source.acquire('direct_signed_tail_C2',2,4,7,x,complete=True)
    tail_c2_wall = arb(tail_c2,(source.crude_moment(3)*omega).upper())
    direct_signed = base+tail_c2_wall
    direct_signed_width = 2*direct_signed.rad()
    require(direct_signed_width < width_vc,
            'strongest acquired signed quadrature remains sharper')
    return {'bits':bits, 'seconds':time.monotonic()-started,
            'source_acquisitions':source.rows,
            'critical_bracket':{'t':'0','center':ROOT_CENTER,'radius':'1e-60',
                'wall':rec(wall),'left_S1':rec(left_s1),'right_S1':rec(right_s1),
                'S1_derivative_on_bracket':rec(derivative),
                'critical_value':rec(value),'sigma':sigma},
            'full_tail_moments':{str(j):rec(v) for j,v in moments.items()},
            'conditions':{'x2_M4_over_M2':rec(wall**2*m4/m2),
                          'x2_M6_over_M4':rec(wall**2*m6/m4)},
            'budget_k':'1',
            'unsigned_intervals':{'separate_M2':[rec(v) for v in direct_interval],
                'cos_Taylor':[rec(v) for v in taylor_interval],
                'coupled':[rec(v) for v in coupled_interval],
                'cos_Taylor6':[rec(v) for v in taylor6_interval],
                'value_and_stationarity':[rec(v) for v in value_coupled_interval]},
            'signed_coupled_interval':[rec(v) for v in signed],
            'widths':{'separate_M2':rec(width_d),'cos_Taylor':rec(width_t),
                'coupled':rec(width_c),'coupled_over_separate':rec(width_c/width_d),
                'coupled_over_cos_Taylor':rec(width_c/width_t),
                'cos_Taylor6':rec(width_t6),'value_and_stationarity':rec(width_vc),
                'both_over_cos_Taylor6':rec(width_vc/width_t6),
                'both_over_first_coupled':rec(width_vc/width_c),
                'stronger_direct_signed_tail':rec(direct_signed_width)},
            'complete_endpoint_gains':{'versus_separate_lower':rec(lower_gain),
                'versus_separate_upper':rec(upper_gain),
                'versus_cos_Taylor_lower':rec(taylor_lower_gain),
                'versus_cos_Taylor_upper':rec(taylor_upper_gain),
                'both_versus_cos_Taylor6_lower':rec((value_coupled_interval[0]-taylor6_interval[0]).lower()),
                'both_versus_cos_Taylor6_upper':rec((taylor6_interval[1]-value_coupled_interval[1]).lower())},
            'comparison_scope':{
                'shared_integrals':10,
                'additional_stronger_signed_tail_integrals':1,
                'tail_moment_comparison':'same head, exact C0=V and S1=0, complete M0/M2/M4/M6/M8; includes all recorded wall and source errors',
                'strongest_direct':'one additional signed tail integral beats the coupled moment certificate; no cost dominance claimed',
                'not_acquired':'no conditional theta collision, all-height margin, curvature or endpoint-exclusion certificate'}}


def main():
    signal.alarm(240)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--bits',type=int,default=320)
    args=parser.parse_args()
    require(args.bits >= 288, 'minimum precision')
    ctx.prec = args.bits
    receipt={'schema':'chb-coupled-signed-tail-v1','date':'2026-10-22',
             'prepared_for':'Edward Baker','authoring_model':'gpt-6.1-sol',
             'actual_effort':'ultra','LLM_assistance':'substantial',
             'review':'same-assistant and delegated same-model checks; no specialist review',
             'status':'finite interval certificate and scoped strict moment-comparator gain',
             'python':platform.python_version(),'python_flint':flint.__version__,
             'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'parameters':{'retained_head_modes':3,'acquisition_modes':7,
                 'source_cutoff':'1','heat_time':'0','abs_quad_tolerance':'1e-78',
                 'rel_quad_tolerance':'1e-75','maximum_seconds':240},
             'controls':controls(),'run':run(args.bits)}
    args.out.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':receipt['status'],
                     'widths':receipt['run']['widths'],
                     'conditions':receipt['run']['conditions'],
                     'seconds':receipt['run']['seconds']}))


if __name__ == '__main__':
    main()
