#!/usr/bin/env python3
"""Exact controls for BW12 Notes 07--09; no theta-source acquisition.

Prepared for Edward Baker, 2026-10-21, with substantial LLM assistance.
Recorded model gpt-6-astra, effort ultra. Python standard library only.
Outputs a small reproducible JSON record to stdout; no files are mutated.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial, prod
import json


def determinant(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    ans = Q(1)
    for k in range(len(a)):
        pivot = next((j for j in range(k, len(a)) if a[j][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            ans = -ans
        d = a[k][k]
        ans *= d
        for i in range(k + 1, len(a)):
            f = a[i][k] / d
            for j in range(k + 1, len(a)):
                a[i][j] -= f * a[k][j]
    return ans


def discriminant(coeffs):
    # Descending coefficients; Sylvester determinant of P and P'.
    n = len(coeffs) - 1
    deriv = [coeffs[i] * (n - i) for i in range(n)]
    rows = []
    for j in range(n - 1):
        rows.append([0] * j + coeffs + [0] * (n - 2 - j))
    for j in range(n):
        rows.append([0] * j + deriv + [0] * (n - 1 - j))
    return (-1) ** (n * (n - 1) // 2) * determinant(rows) / coeffs[0]


def heat_monomial_coefficients(m, t):
    out = [Q(0)] * (m + 1)
    for k in range(m // 2 + 1):
        out[2 * k] = Q(factorial(m), factorial(k) * factorial(m - 2 * k)) * (-t) ** k
    return out


def cluster_law(inside, outside):
    x = list(map(Q, inside)); y = list(map(Q, outside)); pairs = list(combinations(range(len(x)), 2))
    velocities = [2 * sum((1 / (v - w) for j, w in enumerate(x) if i != j), Q(0))
                  + 2 * sum((1 / (v - w) for w in y), Q(0)) for i, v in enumerate(x)]
    differences = [(x[i] - x[j]) ** 2 for i, j in pairs]
    d = prod(differences)
    trans = sum((d / w for w in differences), Q(0))
    dprime = d * sum((2 * (velocities[i] - velocities[j]) / (x[i] - x[j]) for i, j in pairs), Q(0))
    def exterior_q(v):
        return sum((1 / (v - w) for w in y), Q(0))
    b = 4 * sum(((exterior_q(x[i]) - exterior_q(x[j])) / (x[i] - x[j]) for i, j in pairs), Q(0))
    assert dprime == 8 * trans + b * d
    # Check the exact contour formula by summing simple residues at cluster roots.
    residue = Q(0)
    for i, v in enumerate(x):
        pzz_over_pz = 2 * sum((1 / (v - w) for j, w in enumerate(x) if i != j), Q(0))
        residue += exterior_q(v) * pzz_over_pz
    assert b == 2 * residue
    return {'inside': inside, 'outside': outside, 'D': str(d), 'T': str(trans),
            'B': str(b), 'D_prime': str(dprime), 'law_verified': True}


def main():
    hermite = []
    for m in range(2, 9):
        n = m * (m - 1) // 2
        constant = 2 ** n * prod(k ** k for k in range(1, m + 1))
        for t in [Q(-2), Q(-1), Q(1, 3), Q(1), Q(2)]:
            d = discriminant(heat_monomial_coefficients(m, t))
            assert d == constant * t ** n
        hermite.append({'m': m, 'charge': n, 'D_coefficient': constant,
                        'T_coefficient': str(Q(n * constant, 8)),
                        'negative_time_T_sign': (-1) ** (n - 1)})
    clusters = [cluster_law([-1, 1], [-3, 4]),
                cluster_law([-1, 0, 2], [-4, 5]),
                cluster_law([-3, -1, 1, 2], [-7, 6]),
                cluster_law([-3, -1, 0, 2, 4], [-8, 7]),
                cluster_law([-5, -3, -1, 1, 2, 4], [-9, 8])]
    for triple in [(-2, -1, 3), (-1, 0, 2), (1, 3, 7)]:
        v = list(map(Q, triple)); c = sum(v) / 3
        p = sum((v[i] - c) * (v[j] - c) for i, j in combinations(range(3), 2))
        squared = [(v[i] - v[j]) ** 2 for i, j in combinations(range(3), 2)]
        trans = sum(squared[i] * squared[j] for i, j in combinations(range(3), 2))
        assert trans == 9 * p * p
    # The two moment increments implied by log(H/F) recover the exact quadratic discriminant.
    response = []
    for e0, e1 in [(Q(1, 7), Q(0)), (Q(0), Q(2, 9)), (Q(-1, 5), Q(1, 3))]:
        b, c = Q(2, 5), Q(-3, 7)
        d0 = b * b - 4 * c
        dh = (b + e1) ** 2 - 4 * (c + e0)
        linear = 2 * b * e1 - 4 * e0
        assert dh - d0 == linear + e1 * e1
        response.append({'E_constant': str(e0), 'E_linear': str(e1),
                         'Delta_change': str(dh - d0), 'linear_term': str(linear),
                         'quadratic_remainder': str(e1 * e1)})
    # Section 3.1: F=z^2-2t, E=z/16 +/-1/32; use sqrt(2)/2 < 3/4.
    inner_ratio = Q(3, 32) / Q(1, 4)
    outer_ratio = Q(5, 32) / Q(13, 4)
    wall_floor = Q(13, 4) - Q(5, 32)
    curvature_floor = 2 * wall_floor / 9
    # -log(1-q) <= q/(1-q) supplies a rational upper bound.
    log_upper = outer_ratio / (1 - outer_ratio)
    cap_error_upper = 24 * log_upper + 4 * log_upper ** 2
    assert inner_ratio < 1 and outer_ratio < 1 and cap_error_upper < 2
    assert curvature_floor == Q(11, 16)
    event_controls = []
    for c in [-Q(1, 32), Q(1, 32)]:
        exact_time = c / 2 - Q(1, 2048)
        location_upper = c / 2
        assert exact_time <= location_upper
        assert (exact_time < 0) == (c < 0)
        event_controls.append({'constant': str(c), 'exact_event_time': str(exact_time),
                               'proved_location_upper': str(location_upper)})
    print(json.dumps({'date': '2026-10-21', 'prepared_for': 'Edward Baker',
          'model': 'gpt-6-astra', 'effort': 'ultra',
          'status': 'exact rational algebra controls; not a theta certificate',
          'hermite_births': hermite, 'exterior_cluster_controls': clusters,
          'cubic_T_identity_controls': 3, 'quadratic_response_controls': response,
          'boundary_paid_homotopy': {'inner_ratio_upper': str(inner_ratio),
              'outer_ratio_upper': str(outer_ratio), 'outer_wall_floor': str(wall_floor),
              'curvature_floor': str(curvature_floor), 'cap_error_upper': str(cap_error_upper),
              'reference_cap_margin': '2', 'event_controls': event_controls},
          'all_checks_passed': True}, indent=2))


if __name__ == '__main__':
    main()
