#!/usr/bin/env python3
"""Finite exact checks for the genuine signed heat continuation.

Prepared for Edward Baker with substantial LLM assistance, 9 October 2026.
Model: GPT-6 (Codex); exact serving variant and configured effort are not
exposed and are not inferred. Mathematical arithmetic uses exact fractions.

Scope: polynomial identities and scalar reserves, finite cyclic partitions,
and formal multiplicative orthogonality at small integer cutoffs. Imported
exponential-sum theorems, uniform analytic limits, and collision exclusion
are not certified. No heat functions, physical phases, or height grids are
evaluated. Stdout is deterministic; --output optionally saves the same bytes.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


counts = {}


def require(category, condition):
    if not condition:
        raise AssertionError(category)
    counts[category] = counts.get(category, 0) + 1


def canonical(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def poly_add(left, right):
    size = max(len(left), len(right))
    return canonical(tuple((left[i] if i < len(left) else 0)
                           + (right[i] if i < len(right) else 0)
                           for i in range(size)))


def poly_scale(poly, value):
    return canonical(tuple(value * item for item in poly))


def poly_mul(left, right):
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return canonical(result)


def exp_bounds(value, terms=160):
    """Positive Taylor bounds with an exact geometric upper remainder."""
    value = F(value)
    if not 0 <= value < terms + 2:
        raise ValueError("Unsupported exponential argument")
    term = total = F(1)
    for index in range(1, terms + 1):
        term *= value / index
        total += term
    first_omitted = term * value / (terms + 1)
    return total, total + first_omitted / (1 - value / (terms + 2))


def exponent_checks():
    a = (F(0), F(1, 4), F(-1, 16))
    b = (F(0), F(1, 4), F(1, 16))
    d = (F(0), F(3, 4), F(1, 16))
    require("exponents", poly_add(a, b) == (0, F(1, 2)))
    require("exponents", poly_add(d, poly_scale(b, -1)) == (0, F(1, 2)))
    require("exponents", poly_add(d, a) == (0, 1))
    require("exponents", poly_add(a, (F(-3, 16),)) ==
            poly_scale(poly_mul((-1, 1), (3, -1)), F(1, 16)))
    require("exponents", poly_add(b, (F(-5, 16),)) ==
            poly_scale(poly_mul((-1, 1), (5, 1)), F(1, 16)))
    # Endpoint exponent for the Bourgain pair; this remains positive on [1,2].
    p, q = F(13, 84), F(55, 84)
    endpoint = ((p + q) / 2 - F(1, 4), F(-1, 16))
    require("exponents", endpoint == (F(13, 84), F(-1, 16)))
    require("exponents", poly_add(endpoint, (F(-5, 168),)) ==
            (F(1, 8), F(-1, 16)))
    require("exponents", p + q == F(17, 21))
    require("exponents", F(17, 21) > F(1, 2) + F(2, 8))

    # Actual short-edge powers: H=N^(3/4), minimum s_kappa=5/8.
    beta, s_min = F(3, 4), F(5, 8)
    powers = (3 * beta / 4, beta - F(1, 6), beta / 4 + F(1, 4))
    require("short_edge_powers", powers == (F(9, 16), F(7, 12), F(7, 16)))
    for value in powers:
        require("short_edge_powers", value <= F(7, 12))
    require("short_edge_powers", F(7, 12) - s_min == F(-1, 24))
    require("short_edge_powers", F(7, 12) + beta - 1 - s_min == F(-7, 24))
    require("short_edge_powers", F(2, 3) + F(1, 8) == F(19, 24))
    require("short_edge_powers", beta < F(19, 24))

    # Continuous polynomial identities for the averaging and freezing ranges.
    require("range_exponents", poly_add(poly_scale(a, 2), (0, F(-1, 2))) ==
            (0, 0, F(-1, 8)))
    freeze = poly_add(poly_scale(a, 5), (0, -1))
    require("range_exponents", freeze == (0, F(1, 4), F(-5, 16)))
    require("range_exponents", poly_add(freeze, (F(1, 16),)) ==
            poly_scale(poly_mul((-1, 1), (1, 5)), F(-1, 16)))
    # H_p / exp(-a/(2t)) has polynomial exponent 5a/2, with positive minimum.
    require("range_exponents", poly_add(poly_scale(a, 2), poly_scale(a, F(1, 2))) ==
            poly_scale(a, F(5, 2)))
    require("range_exponents", F(5, 2) * F(3, 16) == F(15, 32))
    require("range_exponents", F(1, 2)**2 * F(1, 5) == F(1, 20))
    require("range_exponents", F(1, 2) * 20 == 10)


def edge_reserve_checks():
    # Conditional scalar reserves; the analytic derivative/weight estimates
    # supplying their hypotheses are proved in the note, not by this code.
    n_min, t_max = F(22000), F(1, 20)
    x_min = 11 * n_min**2
    require("edge_reserves", n_min > 10**4)
    require("edge_reserves", F(201, 100) / F(9, 10)**3 < 4)
    require("edge_reserves", 2 * (n_min + 1)**2 + t_max / 6 <=
            F(201, 100) * n_min**2)
    require("edge_reserves", 2 * (n_min**2 - t_max / 16) - t_max / 6 >= n_min**2)
    require("edge_reserves", 4 < F(3, 2)**4)
    require("edge_reserves", 16 < F(8, 5)**6)
    require("edge_reserves", 11 * F(3, 2) < 18)
    require("edge_reserves", 11 * F(8, 5) < 18)
    require("edge_reserves", 11 < 18)
    require("edge_reserves", 4 <= 18)

    weight_log_reserve = ((1 + F(1, 10) / n_min) / (2 * n_min)
                          + (1 + F(1, 10) / n_min) / (2 * x_min**2))
    require("edge_reserves", weight_log_reserve < F(1, 1000))
    require("edge_reserves", exp_bounds(F(1, 1000))[1] < F(101, 100))
    require("edge_reserves", F(101, 100) / F(9, 10) < 2)
    require("edge_reserves", 18 * 2 < 40)

    r_reserve = (4 + 2 * n_min / x_min**2 + 16 * t_max / x_min**2
                 + 8 * t_max * n_min / x_min**4 + 2 * t_max * n_min / x_min)
    require("edge_reserves", r_reserve < 5)
    require("edge_reserves", (2 * n_min + 4 * t_max) / x_min < 1)
    require("edge_reserves", 5 + 1 <= 6)
    require("edge_reserves", 2 + t_max * 3 / x_min < 3)
    require("edge_reserves", 3 / F(9, 10) < 4)
    require("edge_reserves", 6 + 4 <= 10)
    require("edge_reserves", F(101, 100) * 6 + 2 * 10 + 2 * 4 < 40)
    require("edge_reserves", 18 * 40 == 720)
    require("edge_reserves", 720 < 800)
    require("edge_reserves", F(40) * 2 == 80)
    require("edge_reserves", F(800) / 2 == 400)


def contraction_checks():
    rho, epsilon, tau = F(1, 10), F(1, 100), F(1, 50)
    require("contraction", F(2) < F(3, 2)**2)
    # J^T J=[[1,-1/2],[-1/2,1]], with eigenvalues 1/2 and 3/2.
    require("contraction", 1 - F(1, 2) == F(1, 2))
    require("contraction", 1 + F(1, 2) == F(3, 2))
    require("contraction", 1 - F(1, 2)**2 == F(1, 2) * F(3, 2))
    map_reserve = F(3, 2) * (rho**2 / 2 + 3 * epsilon + tau)
    require("contraction", map_reserve == F(33, 400))
    require("contraction", map_reserve < rho)
    lip_reserve = F(3, 2) * rho + 2 * epsilon
    require("contraction", lip_reserve == F(17, 100))
    require("contraction", lip_reserve < 1)


def hull_checks():
    vertices = [(F(13, 84), F(55, 84)),
                (F(4742, 38463), F(35731, 51284)),
                (F(18, 199), F(593, 796)),
                (F(2779, 38033), F(58699, 76066)),
                (F(715, 10238), F(7955, 10238))]
    vertices.extend((p / (2 * p + 2), q / (2 * p + 2) + F(1, 2))
                    for p, q in tuple(vertices[1:]))
    for p, q in vertices:
        require("surveyed_hull", p + q >= F(17, 21))
        require("surveyed_hull", (q - F(1, 2)) + (p + F(1, 2)) == p + q)
    require("surveyed_hull", 0 + 1 >= F(17, 21))
    require("surveyed_hull", F(1, 2) + F(1, 2) >= F(17, 21))
    # Infinite-family identity as polynomials in m, not a finite m grid.
    numerator = (2, -7, 3)
    require("surveyed_hull", poly_add(poly_mul((-2, 3), (-1, 1)), (0, -2)) ==
            numerator)
    require("surveyed_hull", poly_add(poly_scale(poly_mul((0, 1), (-1, 1)), 3),
                                     poly_scale(numerator, -1)) == (-2, 4))
    # For m>=5, 4m-2>=18, (m-1)(m+2)>=28, and deficit<=3/28.
    require("surveyed_hull", 4 * 5 - 2 > 0)
    require("surveyed_hull", (5 - 1) * (5 + 2) == 28)
    require("surveyed_hull", F(3, 28) < F(4, 21))


def cyclic_checks():
    for case in range(1, 17):
        weights = [F(129 - n, n + case) + F(case % 3, 1000 * n)
                   for n in range(1, 129)]
        groups = [F(0), F(0), F(0)]
        for index, weight in enumerate(weights):
            if index:
                require("cyclic_partition", weight <= weights[index - 1])
            groups[index % 3] += weight
            require("cyclic_partition", groups[0] >= groups[1] >= groups[2])
            require("cyclic_partition", max(groups) - min(groups) <= weights[0])


def factor_integer(value):
    factors = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            value //= divisor
        divisor += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def multiplicative_checks():
    for cutoff in (64, 128, 256):
        factorizations = {n: factor_integer(n) for n in range(1, cutoff + 1)}
        primes = [n for n in range(2, cutoff + 1) if factorizations[n] == {n: 1}]
        vectors = {n: tuple(factorizations[n].get(p, 0) for p in primes)
                   for n in range(1, cutoff + 1)}
        for n, vector in vectors.items():
            reconstructed = 1
            for p, exponent in zip(primes, vector):
                reconstructed *= p**exponent
            require("formal_orthogonality", reconstructed == n)
        constant_terms = 0
        for n in range(1, cutoff + 1):
            for m in range(1, cutoff + 1):
                is_constant = all(left == right
                                  for left, right in zip(vectors[n], vectors[m]))
                require("formal_orthogonality", is_constant == (n == m))
                constant_terms += is_constant
                # Product collisions retain the multiplicative, rather than
                # independently assigned coefficient, phase correlations.
                summed = tuple(left + right
                               for left, right in zip(vectors[n], vectors[m]))
                product_factors = factor_integer(n * m)
                require("formal_orthogonality", summed ==
                        tuple(product_factors.get(p, 0) for p in primes))
        require("formal_orthogonality", constant_terms == cutoff)
        for p in primes:
            if 2 * p > cutoff:
                position = primes.index(p)
                for n in range(1, cutoff + 1):
                    require("isolated_prime", vectors[n][position] == (1 if n == p else 0))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optionally save the deterministic stdout JSON")
    args = parser.parse_args()
    exponent_checks()
    edge_reserve_checks()
    contraction_checks()
    hull_checks()
    cyclic_checks()
    multiplicative_checks()
    record = {
        "investigation": "genuine signed heat next-input scout",
        "date": "2026-10-09",
        "model": "GPT-6 (Codex); exact serving variant not exposed",
        "reasoning_effort": "not exposed; not inferred",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "exact fractions and integers; no floating tolerance",
        "assertions": sum(counts.values()),
        "assertions_by_category": dict(sorted(counts.items())),
        "result": "pass",
        "scope": [
            "polynomial exponent identities and short-edge scalar reserves",
            "contraction and cited surveyed-hull scalar reserves",
            "finite cyclic monotone partitions and formal prime-vector orthogonality",
        ],
        "not_certified": [
            "imported exponential-sum theorems or analytic weight and derivative estimates",
            "uniform limits, physical phases, prime asymptotics, or genuine heat-function evaluations",
            "actual collision exclusion, RH, or a complete signed lower bound",
        ],
    }
    output = json.dumps(record, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
