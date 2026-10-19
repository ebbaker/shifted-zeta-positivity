#!/usr/bin/env python3
"""S01 paired-endpoint arithmetic tail and matched complete-error comparison.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual effort ultra. Internal verification.
Requires python-flint 0.9.0. Outputs small records; no global exclusion.
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
import sys
import time

import flint
from flint import acb, arb, ctx


INV = Path('papers/investigations-3/11_arithmetic_collision_rigidity')


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def s(value):
    return value.str(45, more=True)


def A(value):
    return arb(value.numerator)/value.denominator if isinstance(value, F) else arb(value)


def box(left, right):
    left, right = F(left), F(right)
    return arb(A((left+right)/2), A((right-left)/2))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_module(path):
    spec = importlib.util.spec_from_file_location('s01_reference_evaluator', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def admissible(d, m, xhi, T, Y):
    pi = arb.pi()
    c, sd = (4*d).cos(), (4*d).sin()
    B = 4*c*pi*m*m-9-Y
    P = 4*sd*pi*m*m-xhi-2*T*d
    check(d > 0 and d < pi/8, 'shift outside open source strip')
    check(B > 0 and 8*c*pi*m*m >= T, 'amplitude monotonicity failed')
    check(P > 0, 'nonstationary phase gap failed')
    return c, sd, B, P


def tail_bounds(Y, bits):
    """Whole-domain physical derivative bounds divided by fixed G0(1000).

    Every finite endpoint is summed with its sign. All remaining n>=24
    use a proved infinite geometric majorant, never a floating cutoff.
    """
    ctx.prec = bits
    pi = arb.pi()
    d = pi/8-4*arb(1000).log()/1000
    m, M, T, tau = 12, 24, arb(1)/5, arb(1)/100
    xhi, tt, xx = arb(1001), box('1/100', '1/5'), box(999, 1001)
    c, sd, B, P = admissible(d, m, xhi, T, arb(Y))
    endpoint, mass = arb(0), arb(0)
    endpoint_rows = []
    for n in range(m, M):
        lam = pi*n*n
        aa, bb = 2*lam*lam, 3*lam
        C = aa*(9*d-sd*lam).sin()-bb*(5*d-sd*lam).sin()
        pbox = 4*sd*lam-xx-2*tt*d
        pmin = 4*sd*lam-xhi-2*T*d
        check(pbox > 0 and pmin > 0, 'finite phase denominator failed')
        signed = (-c*lam).exp()*C/pbox
        endpoint += signed
        mass += (-c*lam).exp()*(aa+bb)/pmin
        endpoint_rows.append({'n': n, 'C_over_A': s(C/(aa+bb)),
                              'signed_endpoint_uniform': s(signed)})
    lamM = pi*M*M
    pM = 4*sd*lamM-xhi-2*T*d
    rho = (arb(M+1)/M)**2*(-c*pi*(2*M+1)).exp()
    check(pM > 0 and rho < 1, 'infinite geometric tail failed')
    infinite = (2*lamM*lamM+3*lamM)*(-c*lamM).exp()/pM/(1-rho)
    mass += infinite
    endpoint_abs = endpoint.abs_upper()+infinite
    check(endpoint_abs < mass, 'signed endpoint loses its comparison gain')
    beta = arb(29)/125
    check(endpoint_abs < beta*mass, 'rational endpoint allowance failed')
    # This common factor returns the physical jet to a fixed normalization.
    # Both baselines get identical heat damping, isolating the pairing gain.
    factor = arb(1000)**(arb(9)/4)*d.exp()*(-tau*d*d).exp()
    ratio4 = (arb(m+1)/m)**4*(-c*pi*(2*m+1)).exp()
    check(ratio4 < 1, 'reference geometric majorant failed')
    source_majorant = (2*pi*pi*m**4+3*pi*m*m)*(-c*pi*m*m).exp()/(1-ratio4)
    rows, values = [], []
    for j in range(3):
        Q = sum((math.comb(j,k)*d**(j-k)*math.factorial(k)/B**k
                 for k in range(j+1)), arb(0))
        modewise = factor*2*Q*mass
        paired = factor*(d**j*beta+2*Q-d**j)*mass
        reference = arb(1000)**(arb(9)/4)*d.exp()*2*Q*source_majorant/P
        check(paired < modewise and paired < reference, 'strict tail gain failed')
        check(paired/modewise < arb('0.64'), 'declared conservative pairing gate failed')
        rows.append({'j':j, 'reference_geometric_norm':s(reference),
                     'matched_modewise_norm':s(modewise), 'paired_norm':s(paired),
                     'paired_over_matched':s(paired/modewise),
                     'paired_over_reference':s(paired/reference)})
        values.append(paired.upper())
    return {'Y':Y, 'bits':bits, 'd':s(d), 'B':s(B), 'P':s(P),
            'geometric_remainder_from_n':M, 'geometric_ratio':s(rho),
            'infinite_endpoint_and_mass_tail':s(infinite),
            'signed_endpoint_sum_uniform':s(endpoint), 'positive_mass_uniform':s(mass),
            'endpoint_abs_over_mass':s(endpoint_abs/mass),
            'rational_endpoint_ratio_allowance':'29/125',
            'endpoint_rows':endpoint_rows, 'derivatives':rows}, values


def vertical_fixture():
    """Exact non-even source: the vertical segment is compulsory, also off-axis."""
    d, z = arb(1)/4, acb(2, arb(1)/2)
    den = 1+z*z
    hs = [1/den, -2*z/(den*den), (6*z*z-2)/(den*den*den)]
    N = d.cos()+z*d.sin()
    results = []
    for j in range(3):
        pj = acb(0)
        for k in range(j+1):
            Nk = N*hs[k]+(k*d.sin()*hs[k-1] if k else 0)
            pj += math.comb(j,k)*(-d)**(j-k)*Nk
        pj *= (-d*z).exp()
        bj = acb.integral(lambda v, analytic: v.sin()*(-z*v).exp()*(-v)**j,
                          0, d, abs_tol=arb('1e-45'), rel_tol=arb('1e-40'))
        check((hs[j]-pj-bj).contains(0), 'vertical fixture derivative identity failed')
        check(not (hs[j]-pj).contains(0), 'dropping vertical fixture was accepted')
        results.append({'j':j, 'vertical_real':s(bj.real), 'vertical_imag':s(bj.imag),
                        'identity_enclosed':True, 'omitted_boundary_rejected':True})
    return results


def negative_cases():
    pi = arb.pi()
    good_d = pi/8-4*arb(1000).log()/1000
    cases = [('zero shift', arb(0), 12, arb(1001), arb(1)),
             ('strip edge', pi/8, 12, arb(1001), arb(1)),
             ('stationary omitted mode', good_d, 8, arb(1001), arb(1)),
             ('oversized spectral height', good_d, 12, arb(2000), arb(1)),
             ('oversized imaginary width', good_d, 12, arb(1001), arb(1000))]
    rows = []
    for name, d, m, xhi, Y in cases:
        try:
            admissible(d,m,xhi,arb(1)/5,Y)
        except ArithmeticError as exc:
            rows.append({'case':name, 'rejected':True, 'reason':str(exc)})
        else:
            raise ArithmeticError('invalid domain accepted: '+name)
    return rows


def complete_comparison(repo, bits, improved):
    path = repo/INV/'numerics/high_height_consumer/high_height_consumer.py'
    base = load_module(path)
    ev = base.bounded(lambda:base.WholeCellEvaluator(bits),60)
    _, budgets = ev.enclose(F(1,100),F(1,5),F(999),F(1001))
    rows = []
    for j, budget in enumerate(budgets):
        common = budget['quadrature']+budget['taylor']+budget['source']
        old = common+budget['mode']
        new = common+improved[j]
        check(new < old, 'strict complete added-error gain failed')
        rows.append({'j':j, 'old_mode_norm':s(budget['mode']),
            'new_mode_norm':s(improved[j]), 'retained_source_tail_norm':s(budget['source']),
            'quadrature_with_internal_rounding_norm':s(budget['quadrature']),
            'whole_box_taylor_norm':s(budget['taylor']),
            'old_complete_added_error_norm':s(old), 'new_complete_added_error_norm':s(new),
            'new_over_old_complete':s(new/old),
            'same_exact_midpoint_polynomial_and_image_enclosure':True})
    return {'bits':bits, 'setup_seconds':ev.setup_seconds,
        'quadrature_callbacks':ev.callbacks, 'rows':rows,
        'scope':'Uniform added errors of the same exact midpoint polynomial on the full closed real rectangle. Polynomial image rounding is the identical shared outward image enclosure. No fresh signed-region or timing claim.',
        'normalization':'All physical spectral derivatives divided by the fixed positive G0(1000); d,m,U,G0 frozen.',
        'evaluator_sha256':digest(path)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--bits',type=int,default=192)
    p.add_argument('--execution-model',required=True)
    p.add_argument('--execution-effort',required=True)
    p.add_argument('--skip-complete-evaluator',action='store_true')
    args = p.parse_args()
    started = time.monotonic()
    repo = args.repo.resolve()
    replays, primary = [], None
    for bits in [args.bits,args.bits+64]:
        for Y in [0,1]:
            record, values = tail_bounds(Y,bits)
            replays.append(record)
            if bits == args.bits and Y == 0:
                primary = values
    for k in range(2):
        for j in range(3):
            for field in ['reference_geometric_norm','matched_modewise_norm','paired_norm']:
                check(arb(replays[k]['derivatives'][j][field]).overlaps(
                    arb(replays[k+2]['derivatives'][j][field])), 'precision replay disjoint')
    ctx.prec = args.bits
    complete = None if args.skip_complete_evaluator else complete_comparison(repo,args.bits,primary)
    pins = [repo/INV/'research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md',
            repo/INV/'manuscript/positive_arithmetic_packets/sections/01_theta.tex',
            repo/INV/'manuscript/positive_arithmetic_packets/sections/05_controls.tex',
            repo/INV/'manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex',
            repo/INV/'manuscript/positive_arithmetic_packets/sections/08_effective_tails.tex',
            repo/INV/'numerics/high_height_consumer/high_height_consumer.py']
    report = {'date':'2026-10-18', 'timezone':'America/New_York',
        'prepared_for':'Edward Baker','actual_model':args.execution_model,
        'actual_effort':args.execution_effort, 'llm_assistance':'substantial; internal same-model derivation and review',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'script_sha256':digest(__file__),
        'source_sha256':{str(p.relative_to(repo)):digest(p) for p in pins},
        'domain':{'t':['1/100','1/5'],'Re_z':[999,1001],'abs_Im_z_upper':1},
        'frozen':{'d':'pi/8-4*log(1000)/1000','first_omitted_mode':12,
                  'last_finitely_summed_tail_mode':23,'retained_source_U':2},
        'comparison_gate':'strict complete added-error decrease at identical polynomial, coverage and precision; no performance gate',
        'rounding':'outward Arb/Acb; a proved geometric bound covers every omitted n>=24',
        'tail_replays':replays, 'complete_error_comparison':complete,
        'non_even_source_vertical_segment':vertical_fixture(),
        'inadmissible_parameter_rejections':negative_cases(),
        'status':'pass', 'new_signed_coverage':False, 'new_Newman_bound':False,
        'seconds':time.monotonic()-started}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'pass','output':str(args.output),
        'paired_tail_ratios':[r['derivatives'][0]['paired_over_matched'] for r in replays[:2]],
        'complete_ratios':None if complete is None else [r['new_over_old_complete'] for r in complete['rows']],
        'seconds':report['seconds']}))


if __name__ == '__main__':
    main()
