#!/usr/bin/env python3
"""Complete theta baseline for the bounded 01/18 comparison.

14 October 2026, prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra (Codex), reasoning effort ultra.
Requires python-flint 0.9.0. All sign decisions use Arb enclosures.
"""
import argparse
import hashlib
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path
import flint
from flint import acb, arb, ctx, fmpq


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def q(v):
    v = Fraction(v)
    return arb(fmpq(v.numerator, v.denominator))


def interval(lo, hi):
    lo, hi = Fraction(lo), Fraction(hi)
    return arb(q((lo+hi)/2), q((hi-lo)/2))


def encode(v):
    def endpoint(x):
        m, e = x.man_exp()
        return {'mantissa': str(m), 'exponent': int(e)}
    return {'display': v.str(30), 'lower_dyadic': endpoint(v.lower()),
            'upper_dyadic': endpoint(v.upper())}


def run():
    ctx.prec = 256
    pi, t = arb.pi(), q('1/20')
    # For u in [0,1], each omitted positive majorant decreases with u.
    # Consecutive n terms are bounded by the ratio at n=9 and u=0.
    ratio9 = q('10000/6561') * (-19*pi).exp()
    theta_tail = 2*pi*pi*9**4*(-81*pi).exp()/(1-ratio9)
    require(ratio9 < 1, 'Index-tail ratio must be below one')
    # For u >= 1, sum n^4 exp(-pi n^2 exp(4u)) <= 2 exp(-pi exp(4u)).
    ratio1 = 16*(-3*pi*arb(4).exp()).exp()
    require(ratio1 < q('1/2'), 'Full-source geometric ratio must be below one half')
    def source_tail(k):
        slope = 4*pi*arb(4).exp()-9-q('1/10')-k
        require(slope > 0, 'Source tail must decrease')
        return 4*pi*pi*(9+t-pi*arb(4).exp()).exp()/slope
    tails = [theta_tail+source_tail(k) for k in range(20)]
    # The global positive source moment through order 19 is < 2:
    # on [0,1], u^k <=1 and the heated positive majorant decreases;
    # on [1,infinity), use source_tail(k).
    finite_mass_bound = 2*pi*pi*(-pi).exp()/(1-16*(-3*pi).exp())
    require(finite_mass_bound+source_tail(19) < 2, 'Global moment bound failed')
    evaluation_count = 0
    def point_jet(x, k):
        def integrand(u, analytic):
            nonlocal evaluation_count
            evaluation_count += 1
            if 8*evaluation_count > 1000000:
                raise RuntimeError('Declared one-million theta-summand evaluation budget exceeded')
            e4, e5, e9 = (4*u).exp(), (5*u).exp(), (9*u).exp()
            source = sum((2*pi*pi*n**4*e9-3*pi*n*n*e5)
                         *(-pi*n*n*e4).exp() for n in range(1,9))
            phase = (x*u).cos() if k%2 == 0 else (x*u).sin()
            if k%4 in (1,2):
                phase = -phase
            # This finite integrand is entire, so analytic=True is valid.
            return u**k*(t*u*u).exp()*source*phase
        value = acb.integral(integrand, 0, 1, abs_tol=arb('1e-65'),
                             rel_tol=arb('1e-65'), deg_limit=120,
                             eval_limit=100000, depth_limit=30)
        require(value.is_finite() and value.imag.contains(0), 'Nonfinite or nonreal quadrature')
        return value.real+arb(0,tails[k].upper())
    rows = []
    for j, center in ((0, Fraction('204.088')), (1, Fraction('205.557'))):
        started, before = time.perf_counter(), evaluation_count
        jets = [point_jet(q(center), k) for k in range(19)]
        def transport(k, lo, hi):
            offset = interval(lo,hi)
            result = arb(0)
            for n in range(15,-1,-1):
                result = result*offset+jets[k+n]/math.factorial(n)
            radius = max(abs(Fraction(lo)),abs(Fraction(hi)))
            remainder = 2*q(radius)**16/math.factorial(16)
            return result+arb(0,remainder.upper())
        lo, hi = Fraction('-1/1000'), Fraction('1/1000')
        broad = [transport(k,lo,hi) for k in range(4)]
        left, right = transport(j+1,lo,lo), transport(j+1,hi,hi)
        require((left < 0 and right > 0) or (left > 0 and right < 0), 'No endpoint sign change')
        require(not broad[j+2].contains(0), 'Stationary-root uniqueness not certified')
        for _ in range(40):
            mid = (lo+hi)/2
            value = transport(j+1,mid,mid)
            require(not value.contains(0), 'Precision insufficient to bisect stationary root')
            if (left < 0 and value < 0) or (left > 0 and value > 0):
                lo, left = mid, value
            else:
                hi, right = mid, value
        stationary_jets = [transport(k,lo,hi) for k in range(4)]
        conditional = -stationary_jets[j]*stationary_jets[j+2]
        require(conditional > 0, 'Conditional Laguerre sign failed')
        broad_conditional = -broad[j]*broad[j+2]
        require(broad_conditional > 0, 'Whole-cell conditional sign failed')
        baseline_error = max(v.rad() for v in jets)
        require(baseline_error < arb('1e-60'), 'Baseline jet error exceeded target')
        require(conditional.rad() < arb('1e-72'), 'Conditional-form width exceeded target')
        rows.append({'j':j, 't':'1/20', 'initial_x_cell':
                     [str(center-Fraction('1/1000')),str(center+Fraction('1/1000'))],
                     'center':str(center),
                     'stationary_root_bracket':[str(center+lo),str(center+hi)],
                     'center_jets':[encode(v) for v in jets],
                     'cell_jets':[encode(v) for v in broad],
                     'stationary_jets':[encode(v) for v in stationary_jets],
                     'conditional_laguerre':encode(conditional),
                     'whole_cell_conditional_product':encode(broad_conditional),
                     'unique_stationary_root':True,
                     'evaluations':evaluation_count-before,
                     'runtime_seconds':time.perf_counter()-started})
    return {'status':'PASS','date':'2026-10-14','prepared_for':'Edward Baker',
            'llm_assistance':'Substantial; internal research, not independent validation',
            'model':'gpt-6-astra','reasoning_effort':'ultra',
            'arithmetic':'Arb/ACB outward balls, 256 bits',
            'python':platform.python_version(),'python_flint':flint.__version__,
            'parameters':{'theta_indices':8,'source_interval':['0','1'],
                          'taylor_degree':15,'global_moment_bound':'2',
                          'absolute_quadrature_tolerance':'1e-65',
                          'relative_quadrature_tolerance':'1e-65',
                          'max_theta_summand_evaluations':1000000,'target_seconds_per_cell':60},
            'tail_bounds':{'theta_index':encode(theta_tail),
                           'source_through_jet19':encode(source_tail(19)),
                           'positive_mass_bound':encode(finite_mass_bound+source_tail(19))},
            'cells':rows,'total_evaluations':evaluation_count,
            'total_theta_summand_evaluations':8*evaluation_count,
            'scope':'Two fixed-time stationary cells only. Baseline direct-source evaluation; no new 01 or 18 sign mechanism, no time interval or global result.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--record',type=Path,required=True)
    args=parser.parse_args()
    result=run()
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.record.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'record':str(args.record),
                      'evaluations':result['total_evaluations'],
                      'conditional_laguerre':[r['conditional_laguerre']['display'] for r in result['cells']]}))


if __name__=='__main__':
    main()
