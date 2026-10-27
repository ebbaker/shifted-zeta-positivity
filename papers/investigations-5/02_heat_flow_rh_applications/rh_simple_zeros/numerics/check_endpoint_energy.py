#!/usr/bin/env python3
"""Exact rational normalization checks for the RH/simplicity review.

26 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Authoring/checking model: gpt-6-astra; recorded effort: max.
These finite algebra checks are not evidence for RH or simplicity.
"""
from fractions import Fraction as F
from math import factorial, prod
import argparse
import json


def determinant(rows):
    a = [[F(x) for x in row] for row in rows]
    n, out = len(a), F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        p = a[j][j]
        out *= p
        for i in range(j + 1, n):
            ratio = a[i][j] / p
            for k in range(j + 1, n):
                a[i][k] -= ratio * a[j][k]
            a[i][j] = 0
    return out


def discriminant(p):
    # Descending coefficients; all heat polynomials below are monic.
    n = len(p) - 1
    dp = [(n - i) * p[i] for i in range(n)]
    rows = []
    for shift in range(n - 1):
        rows.append([0] * shift + p + [0] * (n - 2 - shift))
    for shift in range(n):
        rows.append([0] * shift + dp + [0] * (n - 1 - shift))
    return (-1) ** (n * (n - 1) // 2) * determinant(rows) / p[0]


def heat_polynomial(m, t):
    p = [F(0)] * (m + 1)
    for k in range(m // 2 + 1):
        p[2 * k] = F((-1) ** k * factorial(m), factorial(k) * factorial(m - 2 * k)) * t ** k
    return p


def run():
    cases = [[-1, 1], [-1, 0, 1], [-3, -1, 2], [-4, -1, 2, 6],
             [-7, -3, 0, 2, 9], [-9, -4, -1, 1, 5, 11]]
    algebra = []
    for values in cases:
        x = list(map(F, values)); m = len(x)
        force = [2 * sum((1 / (x[i] - x[j]) for j in range(m) if i != j), F(0)) for i in range(m)]
        energy = sum((1 / (x[i] - x[j]) ** 2 for i in range(m) for j in range(m) if i != j), F(0))
        ratios = [(force[i] - force[j]) / (x[i] - x[j]) for i in range(m) for j in range(i + 1, m)]
        dissipation = sum((r * r for r in ratios), F(0))
        direct_derivative = -2 * sum(((force[i] - force[j]) / (x[i] - x[j]) ** 3 for i in range(m) for j in range(m) if i != j), F(0))
        c = F(m * (m - 1), 8)
        assert energy == sum((v * v for v in force), F(0)) / 4
        assert sum(ratios, F(0)) == 2 * energy
        assert direct_derivative == -dissipation
        assert dissipation >= energy ** 2 / c
        # A linear exterior drift gives B=-2*lambda*E; constants cancel.
        slope = F(-3, 7)
        drift = [slope * v + F(5, 11) for v in x]
        exterior = -2 * sum(((drift[i] - drift[j]) / (x[i] - x[j]) ** 3 for i in range(m) for j in range(m) if i != j), F(0))
        assert exterior == -2 * slope * energy
        algebra.append({'roots': values, 'ordered_energy': str(energy),
                        'dissipation': str(dissipation),
                        'sharp_cauchy_bound': str(energy ** 2 / c),
                        'equality': dissipation == energy ** 2 / c})
    births = []
    for m in range(2, 9):
        M = m * (m - 1) // 2
        d_hermite = prod(k ** k for k in range(1, m + 1))
        for t in (F(1, 3), F(1), F(2)):
            p = heat_polynomial(m, t)
            disc = discriminant(p)
            assert disc == (2 * t) ** M * d_hermite
            # Verify 2t P'' - x P' + m P == 0 coefficient by coefficient.
            for j in range(m + 1):
                coefficient = j * p[j]
                if j >= 2:
                    coefficient += 2 * t * (m - j + 2) * (m - j + 1) * p[j - 2]
                assert coefficient == 0
            root_square_sum = p[1] ** 2 - 2 * p[2]
            energy = root_square_sum / (16 * t * t)
            assert energy == F(m * (m - 1), 8) / t
        q0 = m - sum((F(1, k) for k in range(1, m + 1)), F(0))
        births.append({'multiplicity': m, 'ordered_energy_coefficient': str(F(m * (m - 1), 8)),
                       'discriminant_time_order': M, 'hermite_discriminant': d_hermite,
                       'filter_limit_m_minus_Hm': str(q0)})
    return {'status': 'PASS', 'date_local': '2026-10-26', 'prepared_for': 'Edward Baker',
            'model': 'gpt-6-astra', 'reasoning_effort': 'max', 'LLM_assistance': 'substantial',
            'scope': 'exact finite algebra and normalization checks, not theta endpoint estimates',
            'rational_configurations': algebra, 'heat_births': births,
            'heat_birth_times_checked': ['1/3', '1', '2']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    result = run()
    with open(args.output, 'w') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'status': result['status'], 'configurations': len(result['rational_configurations']),
                      'multiplicities': [b['multiplicity'] for b in result['heat_births']]}))
