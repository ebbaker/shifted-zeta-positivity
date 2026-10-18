#!/usr/bin/env python3
"""Scalar replay for the effective nonstationary-phase arithmetic tail.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Actual inherited execution configuration: gpt-6.1-sol, effort ultra.
This checks scalar constants in an analytic theorem, not retained-mode
quadrature, a nonzero physical jet, a collision exclusion, or a Newman bound.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform

import flint
from flint import arb, ctx


def A(value):
    return arb(value.numerator) / value.denominator if isinstance(value, F) else arb(value)


def rec(value):
    return value.str(40, more=True)


def check(condition, name):
    if not condition:
        raise ArithmeticError(name)


def frozen_bound(x, m, d, T=F(1,2), Y=F(1), j=0):
    x, T, Y = A(x), A(T), A(Y)
    pi = arb.pi()
    check(0 < d < pi/8, 'shift outside source strip')
    p = pi*(4*d).cos()
    q = p*m*m
    B = 4*q-9-Y
    gap = 4*pi*(4*d).sin()*m*m-x-2*T*d
    check(B > 0 and 8*q >= T, 'amplitude monotonicity failed')
    check(gap > 0, 'nonpositive phase gap')
    check(q >= 1, 'Gaussian tail not monotone')
    eta = gap/(m*m)
    Q = sum((math.comb(j,k)*d**(j-k)*math.factorial(k)/B**k
             for k in range(j+1)), arb(0))
    bracket = 4*pi*pi*(m*m+A(m)/(2*p)+1/(4*p*p*m))+6*pi*(1+1/(2*p*m))
    return ((pi/8-d)*x-q).exp()/x**(arb(7)/4)*Q*bracket/eta


def ceil_sqrt_rational(value):
    value = F(value)
    m = math.isqrt(value.numerator // value.denominator)
    if F(m*m) < value:
        m += 1
    check(F((m-1)**2) < value <= F(m*m), 'exact ceiling bracket')
    return m


def case(a, beta, X, asserted_upper):
    a, beta, X = F(a), F(beta), F(X)
    T, Y = F(1, 2), F(1)
    aa, bb, xx = A(a), A(beta), A(X)
    pi, L = arb.pi(), xx.log()
    theta = 4*aa*L/xx
    kappa, sigma = 1-theta**2/6, 1-theta**2/2
    alpha = 4*pi*aa*kappa*bb
    M = 1+1/(bb*xx).sqrt()
    eta = 4*pi*sigma-1/bb-A(T)*pi/(4*bb*xx)
    q0 = alpha*L
    b0 = 4*q0-9-A(Y)
    delta = 4-(9+A(Y))/q0
    q1 = pi/8+1/b0
    q2 = (pi/8)**2+pi/(4*b0)+2/b0**2
    checks = {
        'log_X_gt_2': L > 2,
        'theta_between_zero_and_pi_over_two': 0 < theta < pi/2,
        'kappa_positive': kappa > 0,
        'sigma_positive': sigma > 0,
        'phase_gap_positive': eta > 0,
        'gaussian_monotone_q_ge_1': q0 >= 1,
        'amplitude_rate_positive': b0 > 0,
        'time_absorption': 8*q0 >= A(T),
        'Q1_at_most_one': q1 <= 1,
        'Q2_at_most_one': q2 <= 1,
        'absolute_tail_delta_positive': delta > 0,
    }
    for name, passed in checks.items():
        check(passed, name)

    Cphase = (
        4*pi**2*M**2*bb/eta*L/xx.sqrt()
        + pi*M*bb.sqrt()/(2*eta*aa*kappa)
        + 1/(16*eta*aa**2*kappa**2*bb.sqrt()*L)
        + 6*pi/eta*L/(xx*xx.sqrt())
        + 3/(4*eta*aa*kappa*bb.sqrt()*xx)
    )
    phase_power = aa-A(F(1,4))-alpha
    check(phase_power < 0, 'decreasing phase envelope')
    phase_onset = Cphase*(phase_power*L).exp()/L
    check(phase_onset < A(F(asserted_upper)), 'asserted all-height phase bound')

    Cabsolute = (
        pi*M**2*bb/(2*aa*kappa*delta)*L/xx.sqrt()
        + M*bb.sqrt()/(16*aa**2*kappa**2*delta)
        + 1/(128*pi*aa**3*kappa**3*delta*bb.sqrt()*L)
        + 3/(4*aa*kappa*delta)*L/(xx*xx.sqrt())
        + 3/(32*pi*aa**2*kappa**2*delta*bb.sqrt()*xx)
    )
    absolute_power = A(F(3,4))+aa-alpha
    check(absolute_power < 0, 'decreasing absolute envelope')
    absolute_onset = Cabsolute*(absolute_power*L).exp()/L**2

    samples = []
    for x in (X, X+1, 2*X):
        m = ceil_sqrt_rational(beta*x)
        # The uniform ceiling bound follows analytically from ceil(sqrt(v))
        # <=sqrt(v)+1 and x>=X; these strict cases also replay it numerically.
        check(A(m) <= M*(bb*A(x)).sqrt(), 'sample uniform ceiling bound')
        d = pi/8-aa*A(x).log()/A(x)
        actual = [frozen_bound(x,m,d,j=j) for j in range(3)]
        uniform_at_x = Cphase*(phase_power*A(x).log()).exp()/A(x).log()
        for bound in actual:
            check(bound < uniform_at_x, 'direct frozen bound exceeds uniform envelope')
        samples.append({'x': str(x), 'first_omitted_mode': m,
                        'retained_modes': m-1,
                        'actual_frozen_gaussian_phase_bounds': [rec(v) for v in actual],
                        'uniform_envelope_at_x': rec(uniform_at_x)})

    return {
        'a': str(a), 'beta': str(beta), 'X': str(X),
        'T': str(T), 'Y': str(Y), 'orders': [0,1,2],
        'asserted_uniform_relative_upper': str(F(asserted_upper)),
        'theta_X': rec(theta), 'kappa': rec(kappa), 'sigma': rec(sigma),
        'alpha': rec(alpha), 'M': rec(M), 'eta': rec(eta),
        'q_at_least': rec(q0), 'b_at_least': rec(b0),
        'Q1_at_most': rec(q1), 'Q2_at_most': rec(q2),
        'C_phase': rec(Cphase), 'phase_power': rec(phase_power),
        'phase_relative_bound_at_onset': rec(phase_onset),
        'C_absolute': rec(Cabsolute), 'absolute_power': rec(absolute_power),
        'absolute_relative_bound_at_onset': rec(absolute_onset),
        'all_analytic_hypotheses_interval_checked': True,
        'finite_ceiling_samples': samples,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--model', default='gpt-6.1-sol')
    parser.add_argument('--effort', default='ultra')
    parser.add_argument('--precision', type=int, default=192)
    args = parser.parse_args()
    ctx.prec = args.precision
    inv = args.repo/'papers/investigations-3/11_arithmetic_collision_rigidity'
    pins = [
        'manuscript/positive_arithmetic_packets/sections/07_shifted_approximation.tex',
        'notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md',
        'research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md',
        'notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md',
        'notes/02_updated_research_plan/08_MATCHED_PILOT_AND_CONTROL_SCREEN_20261018.md',
        'notes/02_updated_research_plan/09_COMPLETE_MODULAR_SIGNED_ESTIMATE_20261018.md',
        'notes/02_updated_research_plan/10_GLOBAL_CONSUMER_AND_COVERAGE_LEDGER_20261018.md',
    ]
    negative = []
    pi = arb.pi()
    bad_cases = [
        ('negative phase gap', 1000, 5, pi/16, 'nonpositive phase gap'),
        ('insufficient amplitude decay', 1000, 5, pi/8-arb(1)/100000,
         'amplitude monotonicity failed'),
        ('zero contour shift', 1000, 16, arb(0), 'shift outside source strip'),
        ('strip boundary shift', 1000, 16, pi/8, 'shift outside source strip'),
    ]
    for name,x,m,d,expected in bad_cases:
        try:
            frozen_bound(x,m,d)
        except ArithmeticError as exc:
            check(str(exc) == expected, 'unexpected rejection reason')
            negative.append({'case':name,'x':x,'first_omitted_mode':m,
                             'd':rec(d),'rejected':True,'reason':str(exc)})
        else:
            raise ArithmeticError('invalid frozen contour accepted')
    result = {
        'date': '2026-10-18', 'timezone': 'America/New_York',
        'prepared_for': 'Edward Baker',
        'llm_assistance': 'substantial; same-model internal scalar replay',
        'actual_model': args.model, 'actual_effort': args.effort,
        'configuration_provenance': 'inherited parent execution metadata',
        'python': platform.python_version(), 'python_flint': flint.__version__,
        'precision_bits': ctx.prec,
        'status': 'scalar interval replay of analytic arithmetic-tail constants',
        'limitations': [
            'not a retained-mode quadrature certificate',
            'not a physical-field or first-jet lower bound',
            'not global collision-free coverage or a Newman bound',
            'derivatives freeze the selected contour and cutoff',
        ],
        'source_sha256': {p: hashlib.sha256((inv/p).read_bytes()).hexdigest()
                          for p in pins},
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'invalid_contract_rejections': negative,
        'cases': [
            case(4,F(1,8),1000,F(2,10**9)),
            case(4,F(1,10),20000,F(6,10**8)),
            case(4,F(1,10),100000,F(4,10**9)),
        ],
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status':'PASS', 'output':str(args.output),
                      'cases':len(result['cases'])}))


if __name__ == '__main__':
    main()
