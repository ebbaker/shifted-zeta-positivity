#!/usr/bin/env python3
"""Small exact algebra checks for RHE Notes 06 and 08; not a theta certificate."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def lift(poly):
    """d/du [lambda exp(5u-v) P(v)], v=lambda exp(4u)."""
    ans = [0] * (len(poly) + 1)
    for k, a in enumerate(poly):
        ans[k] += (5 + 4 * k) * a
        ans[k + 1] -= 4 * a
    return ans


def primitive_at(poly, x):
    return sum(F(a, k + 1) * x ** (k + 1) for k, a in enumerate(poly))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    p0 = [-3, 2]
    p1 = lift(p0)
    p2 = lift(p1)
    assert p1 == [-15, 30, -8]
    assert p2 == [-75, 330, -224, 32]
    laplace_shape = [-1, 4, -3]
    assert primitive_at(laplace_shape, F(1)) == 0
    abs_integral = -2 * primitive_at(laplace_shape, F(1, 3))
    assert abs_integral == F(8, 27)
    laplace_l1_over_pi = 12 * abs_integral
    error_constant_over_pi = 2 * laplace_l1_over_pi
    assert laplace_l1_over_pi == F(32, 9)
    assert error_constant_over_pi == F(64, 9)
    # pi>3 and this positive Taylor lower bound imply 256 exp(-3 pi)<1.
    factorial = 1
    exp9_lower = F(0)
    for k in range(5):
        if k:
            factorial *= k
        exp9_lower += F(9 ** k, factorial)
    assert exp9_lower > 256
    delta, nu = F(1, 24), F(23, 24)
    finite_part_excess_over_pi = delta ** 2 / (2 * nu ** 3)
    assert finite_part_excess_over_pi == F(12, 23 ** 3)
    result = {
        'date': '2026-10-22',
        'prepared_for': 'Edward Baker',
        'model': 'gpt-6.1-sol',
        'reasoning_effort': 'ultra',
        'status': 'exact rational and integer algebra checks passed',
        'scope': 'Checks displayed coefficients and constants only; not a proof replay, source acquisition, quadrature interval, or theta event certificate.',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_polynomials_ascending': [p0, p1, p2],
        'cutoff_laplacian_L1_over_pi': str(laplace_l1_over_pi),
        'cutoff_model_error_over_pi_epsilon': str(error_constant_over_pi),
        'exp9_positive_Taylor_lower_bound': str(exp9_lower),
        'finite_part_excess_over_pi_per_absA': str(finite_part_excess_over_pi),
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'output': str(args.output)}))


if __name__ == '__main__':
    main()
