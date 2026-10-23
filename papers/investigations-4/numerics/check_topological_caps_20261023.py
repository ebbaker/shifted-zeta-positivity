#!/usr/bin/env python3
"""Small floating controls for the topological transport manuscript.

Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra, reasoning effort max, 23 October 2026.
These checks are neither a proof nor a theta-zero certificate.
"""
import argparse
import cmath
import json
import math
import random
from pathlib import Path


def simpson(f, lo, hi, n):
    assert n % 2 == 0
    h = (hi - lo) / n
    return h / 3 * (f(lo) + f(hi) + sum(
        (4 if j % 2 else 2) * f(lo + j * h) for j in range(1, n)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    rng = random.Random(20261023)
    v_cases = []
    centroid_errors = []
    for m in (1, 2, 3, 8, 16, 64, 128):
        harmonic = [0.0]
        for j in range(1, m):
            harmonic.append(harmonic[-1] + 1 / j)
        coefficients = [harmonic[j] - harmonic[m - 1 - j] for j in range(m)]
        assert sum(map(abs, coefficients)) <= 2 * max(m - 1, 0) + 1e-12
        for eta in (1e-5, 0.1, math.pi / 8):
            patterns = {
                'translation': [eta * (0.6 + 0.8j)] * m,
                'outward': [eta * (1 if c >= 0 else -1) for c in coefficients],
                'imaginary_outward': [1j * eta * (1 if c >= 0 else -1)
                                       for c in coefficients],
                'alternating': [eta * (-1) ** j for j in range(m)],
                'complex_random': [eta * rng.random() * cmath.exp(2j * math.pi * rng.random())
                                   for _ in range(m)],
            }
            for name, delta in patterns.items():
                pairs = [(delta[j] - delta[i]) / (math.pi * (j - i))
                         for i in range(m) for j in range(i + 1, m)]
                log_ratio = 2 * sum(cmath.log(1 + u) for u in pairs)
                bound = 4 * max(m - 1, 0) * eta / math.pi + 8 * m * eta * eta / 9
                assert abs(log_ratio) <= bound + 1e-10
                linear_direct = math.pi * sum(pairs)
                linear_grouped = sum(d * c for d, c in zip(delta, coefficients))
                centroid_errors.append(abs(linear_direct - linear_grouped))
                v_cases.append({'m': m, 'eta': eta, 'pattern': name,
                                'absolute_log': abs(log_ratio), 'bound': bound,
                                'ratio': abs(log_ratio) / bound if bound else 0.0})

    # Independent disk pullback quadrature for H=z^2-2*tau.
    T, Y, radius = 1.0, 0.7, 0.4
    k = radius * radius / (1 + radius * radius)
    cap_rows = []
    for sign in (-1, 1):
        def at_s(s):
            tau = complex(T, s)
            def at_r(r):
                angular = 0.0
                for j in range(64):
                    q = r * cmath.exp(2j * math.pi * j / 64)
                    root = cmath.sqrt(q * q + 2 * tau)
                    z = q + sign * root
                    angular += (sign / (root * z)).real
                return (angular * 2 * math.pi / 64) * 2 * r / (1 + r * r) ** 2
            return simpson(at_r, 0, radius, 48) / (4 * math.pi * math.pi)
        computed = simpson(at_s, -Y, Y, 96)
        exact = k * math.atan(Y / T) / (2 * math.pi)
        error = abs(computed - exact)
        assert error < 1e-8
        cap_rows.append({'branch': sign, 'direct_disk_integral': computed,
                         'phase_formula': exact, 'absolute_error': error})

    # A nonzero analytic-factor phase with a stationary root population.
    m, lam, width = 7, 2.0, 3.0
    true_phase_increment = 2 * m * lam * lam * width
    principal_increment = cmath.phase(cmath.exp(1j * true_phase_increment))
    sine = {'m': m, 'lambda': lam, 'Y': width, 'vandermonde_phase': 0.0,
            'lifted_phase_increment': true_phase_increment,
            'principal_argument_of_endpoint_ratio': principal_increment,
            'true_cap': k * true_phase_increment / (2 * math.pi),
            'incorrect_principal_cap': k * principal_increment / (2 * math.pi)}
    assert abs(sine['true_cap'] - sine['incorrect_principal_cap']) > 1

    # Exact saddle definition checks the leading coefficient for a late edge.
    theta, r, width = 0.5, 0.2, 0.4
    edge_rows = []
    def heat_time(L):
        return (4 * math.pi * math.exp(4 * L) - 9) / (2 * L)
    for L in (2, 3, 4, 6, 10, 20):
        T = heat_time(L)
        target = theta * T
        lo, hi = 1.0, L
        for _ in range(100):
            mid = (lo + hi) / 2
            if heat_time(mid) < target:
                lo = mid
            else:
                hi = mid
        La = (lo + hi) / 2
        exact_reference = r * r * width * (La * La - L * L) / (2 * math.pi * (L * L + r * r))
        leading = -r * r * width * math.log(1 / theta) / (4 * math.pi * L)
        edge_rows.append({'L_T': L, 'L_theta_T': La,
                          'reference_edge_per_root': exact_reference,
                          'leading_term': leading, 'ratio': exact_reference / leading})

    result = {
        'date': '2026-10-23', 'prepared_for': 'Edward Baker',
        'model': 'gpt-6-astra', 'reasoning_effort': 'max',
        'status': 'floating diagnostic controls; not interval-certified',
        'scope': 'No actual theta zero or cap was numerically evaluated. The manuscript proofs are analytic.',
        'vandermonde_cases': len(v_cases),
        'largest_vandermonde_bound_ratio': max(c['ratio'] for c in v_cases),
        'largest_linear_regrouping_error': max(centroid_errors),
        'vandermonde_cases_detail': v_cases,
        'quadratic_disk_caps': cap_rows,
        'nonzero_unit_and_phase_lift_control': sine,
        'saddle_edge_references': edge_rows,
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in (
        'vandermonde_cases', 'largest_vandermonde_bound_ratio',
        'largest_linear_regrouping_error')}))
    print(json.dumps({'quadratic_max_error': max(x['absolute_error'] for x in cap_rows),
                      'record': str(args.output)}))


if __name__ == '__main__':
    main()
