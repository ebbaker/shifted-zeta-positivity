#!/usr/bin/env python3
"""Finite algebra for the sphere/Schur note; no arithmetic positivity claim."""

from fractions import Fraction as F
import json
from math import comb, factorial, sqrt


def product(values):
    result = F(1)
    for value in values:
        result *= value
    return result


def pochhammer(a, base, length):
    return product(1 - a * base**j for j in range(length))


def sphere_norm(n, t_squared):
    return (
        F(factorial(n)**2, factorial(2*n + 1))
        * product(k*k + t_squared for k in range(1, n + 1))
    )


def schur_coefficients(q, maximum):
    return [(-q)**n / pochhammer(q*q, q*q, n)
            for n in range(maximum + 1)]


def main():
    counts = {}

    count = 0
    for n in range(11):
        # After u = x/(1-x), integrate x^n (1-x)^n by expansion.
        integrated_polynomial = sum(
            F((-1)**k * comb(n, k), n + k + 1)
            for k in range(n + 1)
        )
        beta_value = F(factorial(n)**2, factorial(2*n + 1))
        assert integrated_polynomial == beta_value
        count += 1
    counts['sphere_radial_integral'] = count

    count = 0
    for t in (F(0), F(1, 2), F(1), F(3, 2)):
        real, imag = F(1), F(0)
        for n in range(11):
            norm_from_derivative = (real*real + imag*imag) * F(
                factorial(n)**2, factorial(2*n + 1)
            )
            assert norm_from_derivative == sphere_norm(n, t*t)
            real, imag = (-(n + 1)*real - t*imag,
                          t*real - (n + 1)*imag)
            count += 1
        ratio0 = sphere_norm(1, t*t)
        ratio1 = sphere_norm(2, t*t) / sphere_norm(1, t*t)
        assert ratio1 - ratio0 == (19 + t*t) / 30
        assert ratio1 > ratio0
        count += 1
    counts['sphere_derivative_norm_and_repetition'] = count

    count = 0
    for q in (F(1, 3), F(1, 2), F(2, 3)):
        base = q*q
        for v in (F(-2, 5), F(1, 4), F(3, 5)):
            for length in (1, 2, 5):
                # The finite product has an end factor. Retain it.
                lhs = pochhammer(-q*v, base, length) / pochhammer(
                    -q*base*v, base, length
                )
                rhs = (1 + q*v) / (1 + q*base**length*v)
                assert lhs == rhs
                count += 1
    counts['elementary_shift_with_finite_end_factor'] = count

    count = 0
    for q in (F(1, 3), F(1, 2), F(2, 3)):
        base = q*q
        for v in (F(-2, 5), F(1, 4), F(3, 5)):
            for length in (1, 2, 4):
                def spherical_product(argument):
                    return (
                        pochhammer(base*argument**2, base, length)
                        * pochhammer(argument**2, base, length)
                        / pochhammer(-q*argument, base, length)**8
                    )

                lhs = spherical_product(base*v) / spherical_product(v)
                ratio = (1 + q*v)**8 / (
                    (1 - v*v)*(1 - base*v*v)**2*(1 - base**2*v*v)
                )
                end_factor = (
                    (1 - base**length*v*v)
                    * (1 - base**(length + 1)*v*v)**2
                    * (1 - base**(length + 2)*v*v)
                    / (1 + q*base**length*v)**8
                )
                assert lhs == ratio * end_factor
                count += 1
    counts['four_flavour_shift_with_finite_end_factors'] = count

    count = 0
    for q in (F(1, 3), F(1, 2), F(2, 3)):
        for maximum in (2, 5, 9):
            coefficients = schur_coefficients(q, maximum)
            z = sum(c*c for c in coefficients)
            overlap = sum(coefficients[n]*coefficients[n-1]
                          for n in range(1, maximum + 1))
            # X is bilateral: the final q*c_N coefficient is still present.
            shifted = [coefficients[0]] + [
                coefficients[n] + q*coefficients[n-1]
                for n in range(1, maximum + 1)
            ] + [q*coefficients[-1]]
            direct_norm = sum(c*c for c in shifted)
            assert direct_norm == (1 + q*q)*z + 2*q*overlap
            assert direct_norm == sum(
                q**(4*n)*c*c for n, c in enumerate(coefficients)
            ) + q*q*coefficients[-1]**2
            count += 2
    counts['complete_common_state_norm_with_boundary_coefficient'] = count

    count = 0
    for q in (F(1, 3), F(1, 2), F(2, 3)):
        coefficients = schur_coefficients(q, 13)
        for n in range(10):
            for m in (1, 2, 3, 4):
                lhs = (-1)**m * coefficients[n]*coefficients[n + m]
                plain_return = q**m * coefficients[n]**2
                rhs = plain_return / product(
                    1 - q**(2*(n + j)) for j in range(1, m + 1)
                )
                assert lhs == rhs
                assert lhs > plain_return
                count += 1
    counts['strict_repetition_coefficient_identity'] = count

    # Floating-point illustration only: no certified truncation error.
    q_float = 1 / sqrt(2)
    base_float = q_float*q_float
    last = 240
    coeff_float = [1.0]
    for n in range(1, last + 1):
        coeff_float.append(-q_float*coeff_float[-1]/(1 - base_float**n))
    z_float = sum(c*c for c in coeff_float)
    overlaps = {
        str(m): {
            'normalized_overlap': (-1)**m * sum(
                coeff_float[n]*coeff_float[n + m]
                for n in range(last + 1 - m)
            ) / z_float,
            'isolated_factor_prediction': q_float**m,
        }
        for m in (1, 2)
    }
    print(json.dumps({
        'status': 'passed',
        'date': '2026-09-14',
        'arithmetic': 'exact rational except the separately labelled illustration',
        'checks': counts,
        'total_checks': sum(counts.values()),
        'overlap_illustration_only': {
            'q': q_float,
            'highest_charge_retained': last,
            'squared_norm_without_common_physical_factor': z_float,
            'repetitions': overlaps,
            'certified_error_bound': False,
        },
        'scope': (
            'Finite algebra supporting the written model tests. '
            'Infinite products retain their finite end factors in these checks. '
            'No proof checker for Mellin integrals, infinite sums, operator domains, '
            'or QFT construction; no matched full Weil pairing or RH claim.'
        ),
    }, indent=2))


if __name__ == '__main__':
    main()
