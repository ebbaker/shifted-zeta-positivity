#!/usr/bin/env python3
"""MC08-E01 r1: exact checks of proved bounds, not a theta numerical scan.

Prepared for Edward Baker with LLM assistance, gpt-6.1-sol / ultra,
2 November 2026. Standard-library rational arithmetic only.
Run from any directory. Prints a small JSON record; does not write files.
"""

from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path


def add(*polys):
    out = {}
    for p in polys:
        for power, coefficient in p.items():
            out[power] = out.get(power, Q()) + coefficient
    return {power: coefficient for power, coefficient in out.items() if coefficient}


def scale(p, value):
    return {power: coefficient * value for power, coefficient in p.items() if coefficient * value}


def mul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            power = (i + k, j + l)
            out[power] = out.get(power, Q()) + a * b
    return {power: coefficient for power, coefficient in out.items() if coefficient}


def main():
    e3_lower = sum((Q(3**k, factorial(k)) for k in range(9)), Q())
    e_upper = sum((Q(1, factorial(k)) for k in range(4)), Q()) + Q(1, 24) / (1 - Q(1, 5))
    exp_9_2_upper = Q(11, 4)**4 * Q(5, 3)
    assert e3_lower > 20
    assert e_upper == Q(87, 32) < Q(11, 4) < Q(25, 9)
    assert exp_9_2_upper == Q(73205, 768) < 100
    assert Q(22, 7) * Q(4, 3) == Q(88, 21) < Q(9, 2)

    j0_upper, j0_lower = Q(1, 209), Q(1, 1600)
    j2_upper, c_upper = Q(2, 25289), Q(11, 2223)
    c0_lower = Q(1, 16) - j0_upper / 8
    alpha_lower = 2 * j0_lower - j2_upper
    q4_upper = (3 * c_upper + j0_upper) / (8 * c0_lower)
    assert c0_lower == Q(207, 3344)
    assert alpha_lower == Q(23689, 20231200) > Q(1, 1000)
    assert q4_upper == Q(320, 8073) < Q(1, 25)
    assert q4_upper / (1 - q4_upper) < Q(1, 24)

    v_star, x_star = Q(1, 25), Q(1, 100)
    assert x_star == v_star / 4
    tail_upper = ((1 + 4*x_star + x_star*x_star) / (1 - x_star)**4 - 1) / 96
    assert tail_upper == Q(2650133, 3073907232) < Q(7, 8000)
    assert Q(1, 1000) - tail_upper > Q(1, 8000)

    # Polynomials in v,x, x=cos(theta). Compare all coefficients, no sampling.
    one = {(0, 0): Q(1)}
    F = {(0, 0): Q(1), (1, 0): Q(1), (2, 0): Q(2)}
    D = {(0, 0): Q(1), (2, 0): Q(-3), (4, 0): Q(4),
         (1, 1): Q(2), (3, 1): Q(4), (2, 2): Q(8)}
    N = {(1, 0): Q(-6), (3, 0): Q(16), (0, 1): Q(2),
         (2, 1): Q(12), (1, 2): Q(16)}
    lhs = add(mul({(0, 0): Q(2), (1, 0): Q(8)}, D), scale(mul(F, N), -1))
    rhs = scale(mul(mul(add(one, {(0, 1): Q(-1)}),
                        add(one, {(2, 0): Q(-2)})),
                    {(0, 0): Q(1), (1, 0): Q(7), (2, 0): Q(2), (1, 1): Q(8)}), 2)
    assert lhs == rhs
    # F*'(vz)*z/F*(vz): real-part numerator N/2; |F*(vz)|^2=D.
    b2 = Q(2) - Q(1, 2)
    b3 = -Q(2) + Q(1, 3)
    assert b2 == Q(3, 2) and b3 == -Q(5, 3)
    assert 1*1 - 1*2 == -1
    # 1-v+2v^2 = 2(v-1/4)^2+7/8 > 0.
    assert Q(2)*Q(1, 4)**2 + Q(7, 8) == 1

    bounds = {
        'e3_lower': e3_lower, 'e_upper': e_upper,
        'exp_9_2_upper': exp_9_2_upper, 'J0_lower': j0_lower,
        'J0_upper': j0_upper, 'J2_upper': j2_upper, 'C_upper': c_upper,
        'c0_lower': c0_lower, 'b1_lower': alpha_lower,
        'q4_upper': q4_upper, 'log_absolute_upper': Q(1, 24),
        'zero_free_radius': Q(4), 'v_star': v_star,
        'coefficient_tail_upper': tail_upper,
        'relative_R_margin': Q(1, 8000),
        'tail_gap_to_7_over_8000': Q(7, 8000)-tail_upper,
    }
    record = {
        'task': 'MC08-E01', 'request_revision': 'r1', 'date': '2026-11-02',
        'prepared_for': 'Edward Baker',
        'llm_assistance': 'Substantial; gpt-6.1-sol (Codex), effort ultra',
        'evidence': 'Exact rational support for analytic proof; no quadrature, theta cutoff or angle scan',
        'program_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'rational_bounds': {k: str(v) for k, v in bounds.items()},
        'checks': {
            'all_rational_inequalities': 'pass',
            'polynomial_symbol_identity_all_coefficients': 'pass',
            'polynomial_negative_two_particle_minor': 'pass',
            'polynomial_negative_three_step_generator_coefficient': 'pass',
        },
        'scope': {
            'analytic_claim': 'R(v)>=1/8000*(2I-S-S*) for 0<=v<=1/25 on ell^2(N0)',
            'not_established_by_this_program': 'source identities, infinite operator theorem, CP construction, theta minor signs or Mellin comparison',
            'v_equals_1': 'not covered; no failure asserted',
        },
    }
    print(json.dumps(record, indent=2) + '\n', end='')


if __name__ == '__main__':
    main()
