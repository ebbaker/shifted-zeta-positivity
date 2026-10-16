#!/usr/bin/env python3
"""Exact finite checks for Note 28; analytic asymptotics remain imported/proved in prose."""

from fractions import Fraction as Q
from math import comb, factorial, prod
from pathlib import Path
import hashlib
import json

ASSERTIONS = 0


def check(value):
    global ASSERTIONS
    assert value
    ASSERTIONS += 1


def subsets(j):
    return range(1 << j)


def selected(mask, values):
    return [x for i, x in enumerate(values) if mask & (1 << i)]


def volume_moment(shifts, v, degree):
    """Exact integral of (v+sum t_i)^degree over the product [0,h_i]."""
    moments = [v ** r for r in range(degree + 1)]
    for h in shifts:
        moments = [sum(Q(comb(r, k)) * moments[r - k] * h ** (k + 1)
                       / (k + 1) for k in range(r + 1))
                   for r in range(degree + 1)]
    return moments[degree]


def run():
    coefficient_cases = moment_cases = polynomial_cases = derivative_cases = 0
    # Distinct ideal symbols may share their norms; no prime ideal enumeration is asserted.
    norm_lists = [[7, 7, 13, 13, 19, 19, 31, 31][:j] for j in range(1, 9)]
    norm_lists += [[7, 13, 19, 31, 37, 43][:j] for j in range(1, 7)]
    for norms in norm_lists:
        j = len(norms)
        coefficients = {s: prod(selected(s, norms)) *
                        prod(1 - q for i, q in enumerate(norms) if not s & (1 << i))
                        for s in subsets(j)}
        check(sum(abs(a) for a in coefficients.values()) == prod(2 * q - 1 for q in norms))
        check(prod(norms) <= sum(abs(a) for a in coefficients.values()) <= (1 << j) * prod(norms))
        check(prod(norms) >= factorial(j // 2) ** 2)
        grouped = {}
        for b in subsets(j):
            nb = prod(selected(b, norms))
            total = sum(a for s, a in coefficients.items() if s & b == b)
            check(total == nb)
            signed = (-1) ** b.bit_count() * total
            grouped[nb] = grouped.get(nb, 0) + signed
            coefficient_cases += 1
        check(grouped[1] == 1)
        # Ordinary uncompensated inverse leaves the positive Jacobian Euler product.
        check(sum(Q((-1) ** b.bit_count(), prod(selected(b, norms))) for b in subsets(j))
              == prod(1 - Q(1, q) for q in norms))

    # These are formal rational shifts, not logarithms of the norms above.
    shift_lists = [[Q(i + 1, 3) for i in range(j)] for j in range(1, 9)]
    shift_lists += [[Q(2, 3)] * j for j in range(1, 9)]
    for shifts in shift_lists:
        j = len(shifts)
        for k in range(j + 1):
            value = sum((-1) ** b.bit_count() * sum(selected(b, shifts), Q(0)) ** k
                        for b in subsets(j))
            expected = 0 if k < j else (-1) ** j * factorial(j) * prod(shifts)
            check(value == expected)
            moment_cases += 1
        for v in [Q(0), Q(1, 5), Q(3, 2)]:
            for k in range(j + 6):
                difference = sum((-1) ** b.bit_count() *
                                 (v + sum(selected(b, shifts), Q(0))) ** k
                                 for b in subsets(j))
                integral = (0 if k < j else (-1) ** j * Q(factorial(k), factorial(k - j))
                            * volume_moment(shifts, v, k - j))
                check(difference == integral)
                polynomial_cases += 1

    for m in range(1, 41):
        alpha = sum(Q(1, (1 << (m - k)) * k) for k in range(1, m + 1))
        check(alpha >= Q(1, m))
        check(factorial(m) * alpha >= factorial(m - 1))
        for y in [Q(0), Q(1, 10), Q(1, 4), Q(3, 4), Q(9, 10)]:
            for k in range(1, m + 1):
                term_ratio = Q(k, 1 - y) + Q(m - k + 1, 2 - y)
                check(term_ratio <= Q(m + 1, 1 - y))
                derivative_cases += 1
            # h^(m)/(m*h^(m-1)) = 1/(2-y), the extra g' term.
            hm = Q(factorial(m)) / (2 ** m * (1 - y / 2) ** (m + 1))
            hm1 = Q(factorial(m - 1)) / (2 ** (m - 1) * (1 - y / 2) ** m)
            check(hm / (m * hm1) == Q(1, 2 - y))
            check(Q(m + 1, 1 - y) + Q(1, 2 - y) <= Q(m + 2, 1 - y))
            derivative_cases += 2

    # The coherent energy surplus is fixed; logarithmic annihilation does not alter it.
    check(-Q(14, 15) + 2 == Q(16, 15))
    check(Q(16, 15) - Q(4, 5) == Q(4, 15))
    check(Q(1, 2) + Q(1, 40) < 1)  # diagonal error for beta < 1/20
    return {
        "status": "passed",
        "arithmetic": "exact rational and integer",
        "assertions": ASSERTIONS,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "coefficient_cases": coefficient_cases,
        "formal_shift_moment_cases": moment_cases,
        "polynomial_integral_cases": polynomial_cases,
        "derivative_term_cases": derivative_cases,
        "norm_lists_include_distinct_symbols_with_equal_norms": True,
        "scope": "finite identities only; rational shifts are not substituted for logarithms",
        "unverified_by_script": ["fixed-field prime ideal theorem", "coprime lattice asymptotic",
                                 "uniform growing-order analytic limit", "full-response covariance"],
    }


if __name__ == "__main__":
    record = run()
    output = Path(__file__).with_name("growing_cofactor_barrier_record_20261009.json")
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps(record, sort_keys=True))
