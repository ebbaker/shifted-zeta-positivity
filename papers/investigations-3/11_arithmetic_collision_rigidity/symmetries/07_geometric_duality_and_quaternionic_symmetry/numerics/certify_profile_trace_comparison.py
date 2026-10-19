#!/usr/bin/env python3
"""S07-T2: outward-rounded evaluation of the fixed N=2 profile contract.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Actual model gpt-6.1-sol (Codex), reasoning effort ultra.

This evaluates the written analytic bounds. It is not a physical-sign
certificate, a lower bound on an actual signed error, or an acquisition of
the common retained-source approximation. See the accompanying Note 04.
Dependency: python-flint. Run from the repository root with --repo .,
--precision 192 (or 256), and --output /tmp/s07_t2_replay.json.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform
import sys

import flint
from flint import arb, ctx


LANE = Path('papers/investigations-3/11_arithmetic_collision_rigidity/'
            'symmetries/07_geometric_duality_and_quaternionic_symmetry')
NOTE03 = LANE / 'notes/03_CONSTRAINED_THETA_JET_SPACE_AND_RESIDUAL_CONTRACT_20261019.md'
NOTE04 = LANE / 'notes/04_PAID_PROFILE_TRACE_AND_DIRECT_TAIL_COMPARISON_20261019.md'


def require(condition, message):
    """Run guards even under python -O; overlapping Arb comparisons fail."""
    if not bool(condition):
        raise ValueError(message)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def polynomial_product(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += F(x) * F(y)
    return out


def exact_support_checks():
    """Finite algebra supporting the analytic arguments, not replacing them."""
    require(polynomial_product([1, 0, -1], [1, 0, -1]) ==
            [F(1), F(0), F(-2), F(0), F(1)], 'cutoff denominator algebra')
    # (1-d^2)^2+4d^2 = (1+d^2)^2. Together with cosh(z)^2>=1+z^2,
    # z=2d/(1-d^2), this proves rho'<=2/(1+d^2)<=2 for |d|<1.
    require([1, 0, 2, 0, 1] == polynomial_product([1, 0, 1], [1, 0, 1]),
            'cutoff derivative comparison algebra')
    require(polynomial_product([-1, 2], [-3, 1]) == [3, -7, 2],
            'source derivative factorization')
    require(F(9, 4) + F(3, 2)/(4-F(3, 2)) - 4 == F(-23, 20),
            'q monotonicity support')
    require(2 + F(3, 2)/(4-F(3, 2)) - 4 == F(-7, 5),
            'y monotonicity support')
    require(2 * F(1, 4)**3 / 3 == F(1, 96), 'p second moment')
    require(4 * F(1, 2) * F(1, 2) * F(97, 16) / 4 == F(97, 64),
            'lower witness volume and physical measure')
    require(4 * F(1, 96) == F(1, 24), 'p derivative upper coefficient')
    # Derivatives of positive exponential polynomial antiderivatives:
    # J3(Q)-J2(Q) = exp(-lambda Q)*[(Q^3-Q^2)/lambda
    #  +(3Q^2-2Q)/lambda^2+(6Q-2)/lambda^3+6/lambda^4].
    p = [F(0), F(0), F(-1), F(1)]
    derivatives = [p]
    for _ in range(3):
        p = [F(i)*p[i] for i in range(1, len(p))]
        derivatives.append(p)
    require(derivatives == [[0, 0, -1, 1], [0, -2, 3], [-2, 6], [6]],
            'Jdiff antiderivative polynomial')
    return {
        'actual_cutoff_derivative_upper': '2',
        'cutoff_support': 'rho=0 for |y|<=2, rho=1 for |y|>=3',
        'cutoff_proof': ('rho=logistic(-1/x+1/(1-x)); d=2x-1; '
                         'rho_prime=2(1+d^2)/[(1-d^2)^2 cosh(z)^2]; '
                         'z=2d/(1-d^2); cosh(z)^2>=1+z^2'),
        'finite_rational_identities': 'passed',
        'continuous_inequalities': 'proved in Note 04; not inferred from samples',
    }


def record_ball(value, digits):
    require(value.is_finite(), 'nonfinite interval in output')
    return {'enclosure': value.str(digits),
            'interpretation': 'Arb outward-rounded real ball'}


def run(repo, precision):
    require(precision >= 128, 'precision must be at least 128 bits')
    require(precision <= 4096, 'precision above bounded replay limit')
    require((repo / 'AGENTS.md').is_file() and (repo / '.git').exists(),
            'repository markers missing')
    require((repo / NOTE03).is_file(), 'required S07-T1 source note missing')
    note03_text = (repo / NOTE03).read_text()
    require('N=2' in note03_text and '20 X' in note03_text,
            'S07-T1 contract source changed or wrong source note')
    ctx.prec = precision
    support = exact_support_checks()
    R = lambda numerator, denominator=1: arb(numerator) / denominator
    pi = arb.pi()
    U = arb(4).log()/4
    lam = 9*pi - R(1, 80)
    require(pi > 3 and lam > 0, 'elementary constants and decay')
    require(8*pi > R(13, 2), 'q-uniform moment monotonicity')
    require(arb(2).exp() > 4, 'heat-factor inequality e^2>4')
    r1 = R(4, 3)**4 * (-7*pi).exp()
    r4 = R(4, 3)**4 * (-28*pi).exp()
    require(0 < r4 and r4 < r1 and r1 < 1, 'tail geometric ratios')

    # Lower X: all p, q in [1,17/16], |y| in [9/4,5/2].
    # The source profile decreases in q and |y| on this region.
    q_witness, y_witness = R(17, 16), R(5, 2)
    w = pi*q_witness*y_witness**2
    a_min = (q_witness.log()/4).exp() * w*(w-R(3, 2)) * (-w).exp()
    rho_min = 1/(1+R(8, 3).exp())
    x2_lower = R(97, 64)*q_witness.log()*(a_min*rho_min)**2
    x_lower = x2_lower.sqrt()

    # Upper X: |g|^2+|g_y|^2 <= exp(2*pi*p^2*q)*(9*a^2+2*a_y^2),
    # with the actual smooth cutoff derivative bound |chi'|<=2.
    # Gaussian moments here are UPPER bounds; M0 uses the Gaussian tail
    # inequality and the remaining moments use the positive recurrence.
    gaussian_edge = (-8*pi).exp()
    moments = {0: gaussian_edge/(8*pi)}
    for k in range(2, 13, 2):
        moments[k] = (R(2**(k-1))*gaussian_edge/(4*pi)
                      + R(k-1)*moments[k-2]/(4*pi))
    J_upper = 2*(9*pi**4*(moments[8]+moments[10])
                 + 8*pi**6*(moments[10]+moments[12]))
    p_factor_upper = (pi/2).exp()*(2+2*pi**2/3)
    x2_upper = U*p_factor_upper*J_upper
    x_upper = x2_upper.sqrt()
    require(0 < x_lower and x_lower < x_upper, 'X norm bracket')

    # Uniform kernel norm bounds, using t>=0 and x>=999 for the lower
    # expressions, and t<=1/5 and |sin|,|cos|<=1 for the upper expressions.
    c0sq_lower = U/2 - R(1, 4*999)
    c1sq_lower = (U**3/6 - U**2/(4*999)
                   - U/(4*999**2) - R(1, 8*999**3))
    c0_lower, c1_lower = c0sq_lower.sqrt(), c1sq_lower.sqrt()
    heat_upper = (U**2/5).exp()
    c0_upper = heat_upper*U.sqrt()
    c1_upper = heat_upper*(U**3/3).sqrt()
    require(0 < c0_lower and c0_lower < c0_upper, 'value kernel bounds')
    require(0 < c1_lower and c1_lower < c1_upper, 'derivative kernel bounds')
    geometric_floor = [arb(20).sqrt()*x_lower*c0_lower,
                       arb(20).sqrt()*x_lower*c1_lower]
    geometric_upper = [arb(20).sqrt()*x_upper*c0_upper,
                       arb(20).sqrt()*x_upper*c1_upper]

    def J(k, Q):
        return (-lam*Q).exp()*sum(
            (R(math.factorial(k), math.factorial(k-i))*Q**(k-i)
             /lam**(i+1) for i in range(k+1)), arb(0))

    def Jdiff(Q):
        return (-lam*Q).exp()*((Q**3-Q**2)/lam
                +(3*Q**2-2*Q)/lam**2+(6*Q-2)/lam**3+6/lam**4)

    # Jdiff keeps the positive polynomial expression. Subtracting J3-J2
    # numerically is unnecessary; the exact support check derives it.
    J2_1, J2_4 = J(2, arb(1)), J(2, arb(4))
    Jdiff_1, Jdiff_4 = Jdiff(arb(1)), Jdiff(arb(4))
    require(J2_1 > J2_4 and Jdiff_1 > Jdiff_4 and Jdiff_4 > 0,
            'positive direct inside/outside integrals')
    prefactors = [81*pi**2/2, 81*pi**2/8]
    inside_integrals = [J2_1-J2_4, Jdiff_1-Jdiff_4]
    outside_integrals = [J2_4, Jdiff_4]
    direct_inside = [prefactors[j]*inside_integrals[j]/(1-r1) for j in (0, 1)]
    outside = [prefactors[j]*outside_integrals[j]/(1-r4) for j in (0, 1)]
    direct_total = [direct_inside[j]+outside[j] for j in (0, 1)]
    ratios = [geometric_floor[j]/direct_total[j] for j in (0, 1)]

    checks = {
        'X_norm_lower_above_7.02927e-9': x_lower > arb('7.02927e-9'),
        'X_norm_upper_below_0.026484': x_upper < arb('0.026484'),
        'assigned_floor_0_above_1.30765e-8': geometric_floor[0] > arb('1.30765e-8'),
        'assigned_floor_1_above_2.61274e-9': geometric_floor[1] > arb('2.61274e-9'),
        'geometric_assigned_floor_0_over_direct_upper_exceeds_1618': ratios[0] > 1618,
        'geometric_assigned_floor_1_over_direct_upper_exceeds_34152': ratios[1] > 34152,
        'geometric_assigned_upper_0_below_0.071421': geometric_upper[0] < arb('0.071421'),
        'geometric_assigned_upper_1_below_0.014291': geometric_upper[1] < arb('0.014291'),
        'direct_total_upper_0_below_8.07803e-12': direct_total[0] < arb('8.07803e-12'),
        'direct_total_upper_1_below_7.65021e-14': direct_total[1] < arb('7.65021e-14'),
        'outside_upper_0_below_1.84725e-47': outside[0] < arb('1.84725e-47'),
        'outside_upper_1_below_1.40207e-47': outside[1] < arb('1.40207e-47'),
    }
    for name, passed in checks.items():
        require(passed, name)
    values = {
        'pi': pi, 'U': U, 'lambda': lam, 'r_at_1': r1, 'r_at_4': r4,
        'witness_a_lower_expression': a_min, 'witness_rho_lower_expression': rho_min,
        'X_squared_lower_expression': x2_lower, 'X_squared_upper_expression': x2_upper,
        'X_lower_expression': x_lower, 'X_upper_expression': x_upper,
        'J_profile_upper_expression': J_upper, 'p_factor_upper_expression': p_factor_upper,
        'kernel_0_lower_expression': c0_lower, 'kernel_0_upper_expression': c0_upper,
        'kernel_1_lower_expression': c1_lower, 'kernel_1_upper_expression': c1_upper,
    }
    for j in (0, 1):
        values.update({
            f'assigned_geometric_floor_{j}': geometric_floor[j],
            f'assigned_geometric_upper_{j}': geometric_upper[j],
            f'direct_inside_upper_{j}': direct_inside[j],
            f'common_outside_upper_{j}': outside[j],
            f'direct_total_upper_{j}': direct_total[j],
            f'assigned_floor_over_direct_upper_{j}': ratios[j],
        })
    Gc = (R(7, 4)*arb(1000).log()-125*pi).exp()
    values['Gc_fixed_reference'] = Gc
    for j in (0, 1):
        values[f'assigned_geometric_floor_{j}_over_Gc'] = geometric_floor[j]/Gc
        values[f'assigned_geometric_upper_{j}_over_Gc'] = geometric_upper[j]/Gc
        values[f'direct_total_upper_{j}_over_Gc'] = direct_total[j]/Gc
    for name, value in values.items():
        require(value.is_finite() and value > 0, f'{name}: finite strict positivity')
    for j in (0, 1):
        require(geometric_floor[j] < geometric_upper[j], 'assigned payment bracket')
        require(direct_inside[j] > 0 and outside[j] > 0, 'positive complete components')
        require(geometric_floor[j] > direct_inside[j], 'componentwise fixed-contract loss')

    digits = max(30, int(precision*math.log10(2))-8)
    pins = {'checker': {'path': str(Path(__file__).resolve()),
                        'sha256': sha256(__file__)},
            'S07_T1_source_note': {'path': str(NOTE03), 'sha256': sha256(repo/NOTE03)}}
    if (repo/NOTE04).is_file():
        pins['S07_T2_source_note'] = {'path': str(NOTE04), 'sha256': sha256(repo/NOTE04)}
    else:
        pins['S07_T2_source_note'] = {'path': str(NOTE04),
                                     'status': 'not present when this replay ran'}
    return {
        'schema': 's07-t2-fixed-profile-trace-comparison-v1',
        'date': '2026-10-19',
        'generated_at_utc': datetime.now(timezone.utc).isoformat(),
        'prepared_for': 'Edward Baker',
        'LLM_assistance': 'substantial; internal same-model computation',
        'actual_model': 'gpt-6.1-sol (Codex)',
        'reasoning_effort': 'ultra',
        'runtime': {'python': platform.python_version(), 'python_flint': flint.__version__,
                    'precision_bits': precision, 'executable': sys.executable},
        'status': 'certified evaluation of stated analytic bounds; fixed contract loses',
        'contract': {
            'N': 2, 'p': ['-1/4', '1/4'], 'q': ['1', '4'],
            'B_t': ['1/100', '1/5'], 'B_x': ['999', '1001'],
            'physical_measure': 'du=dq/(4q), q=exp(4u)',
            'profile': 'g=exp(pi*p^2*q)*a_q*(1-chi_2)',
            'observation': 'orders j=0,1; actual cosine and sine kernel L2 norms',
            'retained_source': ('exact symbolic hatH2: n=1,2 retained for all q>=1; '
                                'same retained source in both comparisons'),
            'outside_tube': 'only n>=3, q>4; identical explicit upper payments',
            'common_acquisitions': ('retained-source arithmetic/rounding/quadrature, '
                                    'anchor and any consumer propagation remain '
                                    'symbolic, identical, and unperformed'),
            'complete_ledgers': {
                'direct_j': 'Q_j + direct_inside_upper_j + common_outside_upper_j',
                'geometric_j': 'Q_j + sqrt(20)*X(g)*C_j(t,x) + common_outside_upper_j',
                'meaning_Q_j': ('a common nonnegative certified acquisition/consumer '
                                'payment if a concrete approximant is acquired'),
            },
            'normalization': ('raw physical H,Hx units; also report common fixed '
                              'Gc=1000^(7/4)*exp(-125*pi) conversion'),
            'scope': ('lower bounds are on assigned Cauchy payments only, not on '
                      'actual signed residuals or errors; no new nonzero anchor, '
                      'physical sign, cost advantage, coverage or RH claim'),
            'frozen_parameter_guards': 'all support and pilot parameters are fixed constants',
        },
        'exact_support': support,
        'proof_inputs': {
            'heat_factor': 'u^2<=q/16; e^(t*u^2)<=e^(q/80) for t<=1/5',
            'direct_order1': 'u=log(q)/4<=(q-1)/4',
            'direct_Jdiff': ('exp(-lambda*Q)*((Q^3-Q^2)/lambda+'
                             '(3Q^2-2Q)/lambda^2+(6Q-2)/lambda^3+6/lambda^4)'),
            'moment_M0_upper': 'exp(-8*pi)/(8*pi)',
            'moment_recurrence': 'M_k=2^(k-1)*exp(-8*pi)/(4*pi)+(k-1)*M_(k-2)/(4*pi)',
            'continuous_proofs': 'see Note 04; no sampled extremum or quadrature is used',
        },
        'interval_values': {name: record_ball(value, digits) for name, value in values.items()},
        'gaussian_moment_upper_values': {str(k): record_ball(v, digits)
                                        for k, v in moments.items()},
        'required_threshold_checks': {name: bool(passed) for name, passed in checks.items()},
        'all_required_checks_passed': True,
        'source_pins': pins,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True, type=Path)
    parser.add_argument('--precision', '--bits', type=int, default=192)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    report = run(args.repo, args.precision)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': report['status'], 'precision_bits': args.precision,
                      'output': str(args.output.resolve()),
                      'all_required_checks_passed': True}))


if __name__ == '__main__':
    main()
