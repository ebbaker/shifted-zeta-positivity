#!/usr/bin/env python3
"""Finite exact checks for mixed note 10.

Prepared for Edward Baker, 9 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed.
Formal ideal monoids and cyclotomic phases check algebra, not native
reciprocity, selected zero bins, ideal asymptotics, or a new mixed moment.
Standard library only; prints a deterministic small JSON record.
"""

from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import prod
import json


ZERO, ONE = (0, 0), (1, 0)
ROOTS = (ONE, (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
NORMS = (2, 3, 5, 7)
PAIRING = ((0, 1, 2, 3), (1, 0, 5, 2),
           (2, 5, 0, 1), (3, 2, 1, 0))
COUNTS = Counter()


def check(value, group):
    COUNTS[group] += 1
    if not value:
        raise AssertionError(group)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def conj(a):
    return a[0] + a[1], -a[1]


def scale(a, n):
    return n * a[0], n * a[1]


def norm2(a):
    return a[0] ** 2 + a[0] * a[1] + a[1] ** 2


def total(values):
    out = ZERO
    for value in values:
        out = add(out, value)
    return out


def ideal_norm(column):
    return prod(n ** e for n, e in zip(NORMS, column))


def mobius(column):
    return 0 if max(column) > 1 else (-1) ** sum(column)


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def phase(row, column, orientation=1):
    if any(x and y for x, y in zip(row, column)):
        return ZERO
    exponent = sum(row[i] * PAIRING[i][j] * column[j]
                   for i in range(4) for j in range(4))
    return ROOTS[(orientation * exponent) % 6]


def nu(column):
    return ROOTS[sum((i + 1) * x for i, x in enumerate(column)) % 6]


def psi(row, column, orientation=1):
    # The fixed ray factor is not conjugated when the native orientation flips.
    return mul(nu(column), phase(row, column, orientation))


def profile(column):
    n = ideal_norm(column)
    if not 6 <= n <= 30:
        return ZERO
    return scale(ROOTS[n % 6], 1 + n % 3)


def split(left, right):
    gcd = tuple(min(x, y) for x, y in zip(left, right))
    a = tuple(x - g for x, g in zip(left, gcd))
    b = tuple(y - g for y, g in zip(right, gcd))
    core = plus(a, b)
    sextic = tuple(x + 5 * y for x, y in zip(a, b))
    return gcd, a, b, core, sextic


def record_fraction(value):
    return {"exact": str(value), "decimal": float(value)}


def run():
    squarefree = tuple(product(range(2), repeat=4))
    all_rows = tuple(product(range(6), repeat=4))
    rows = tuple(dict.fromkeys(all_rows[::17] + all_rows[:20]))
    plain = tuple(c for c in product(range(3), repeat=4)
                  if 2 <= ideal_norm(c) <= 35)
    primes = tuple(tuple(int(i == j) for i in range(4)) for j in range(4))
    selected_mass = {}
    for row in rows:
        s = total(mul((1 + ideal_norm(c) % 3, ideal_norm(c) % 2),
                      psi(row, c)) for c in plain)
        q = total(mul(ROOTS[j], psi(row, c)) for j, c in enumerate(primes))
        selector = int(row != (0, 0, 0, 0) and sum(row) % 3 != 1)
        selected_mass[row] = selector * norm2(s) ** 2 * norm2(q)
    check(sum(selected_mass.values()) > 0, "nonzero_selected_fourth_weight")

    summaries = []
    for orientation in (1, -1):
        direct = sum(
            selected_mass[row] * norm2(total(
                scale(mul(profile(c), psi(row, c, orientation)), mobius(c))
                for c in squarefree)) for row in rows)
        by_core = defaultdict(lambda: ZERO)
        pair_terms = {}
        missing_mask = 0
        for left, right in product(squarefree, repeat=2):
            gcd, a, b, core, sextic = split(left, right)
            check(all(not (x and y) for x, y in zip(a, b)),
                  "coprime_ratio_factors")
            check(all(not (g and (x or y)) for g, x, y in zip(gcd, a, b)),
                  "gcd_coprime_to_ratio")
            check(mobius(left) * mobius(right) == mobius(core),
                  "mobius_sign_on_ratio_core")
            check(ideal_norm(left) * ideal_norm(right)
                  == ideal_norm(gcd) ** 2 * ideal_norm(core),
                  "norm_identity")
            check(prod(n for n, e in zip(NORMS, sextic) if e)
                  == ideal_norm(core), "primitive_good_radical_is_core")
            check(plus(gcd, a) == left and plus(gcd, b) == right,
                  "exact_pair_reconstruction")
            coefficient = scale(mul(profile(left), conj(profile(right))),
                                mobius(core))
            direct_kernel = total(
                scale(mul(psi(row, left, orientation),
                          conj(psi(row, right, orientation))),
                      selected_mass[row]) for row in rows)
            core_kernel = ZERO
            for row in rows:
                lhs = mul(psi(row, left, orientation),
                          conj(psi(row, right, orientation)))
                reduced = mul(psi(row, a, orientation),
                              conj(psi(row, b, orientation)))
                rhs = scale(reduced, norm2(psi(row, gcd, orientation)))
                check(lhs == rhs, "gcd_mask_identity")
                native_reduced = mul(
                    mul(nu(a), conj(nu(b))), phase(row, sextic, orientation))
                check(reduced == native_reduced,
                      "fixed_ray_phase_kept_separate")
                core_kernel = add(core_kernel, scale(rhs, selected_mass[row]))
                missing_mask += bool(
                    coefficient != ZERO and selected_mass[row]
                    and reduced != ZERO and norm2(psi(row, gcd, orientation)) == 0)
            check(core_kernel == direct_kernel, "weighted_core_kernel")
            term = mul(coefficient, core_kernel)
            pair_terms[left, right] = (term, ideal_norm(core))
            by_core[core] = add(by_core[core], term)
            if profile(left) != ZERO and profile(right) != ZERO:
                a_norm, b_norm = ideal_norm(a), ideal_norm(b)
                check(F(1, 5) <= F(a_norm, b_norm) <= 5,
                      "annular_balance")
                check(36 <= ideal_norm(gcd) ** 2 * ideal_norm(core) <= 900,
                      "gcd_scale_from_annuli")
                if sum(core) == 1:
                    check(ideal_norm(core) <= 5, "prime_core_bounded_by_balance")
        check(total(by_core.values()) == (direct, 0),
              "core_recombination_equals_positive_fourth")
        inverse_D, plain_N, prime_P = 12, 12, 7
        denominator = inverse_D * plain_N ** 2 * prime_P
        normalized = F(direct, denominator)
        check(F(total(by_core.values())[0], denominator) == normalized,
              "inverse_and_fourth_normalizations_retained")
        check(all(value[1] == 0 for value in by_core.values()),
              "each_core_is_real_by_pair_reversal")
        check(missing_mask > 0, "dropping_gcd_mask_changes_actual_terms")
        for cap in (F(5), F(49, 2), F(65)):
            low = total(term for term, conductor in pair_terms.values()
                        if conductor <= cap)
            high = total(term for term, conductor in pair_terms.values()
                         if conductor > cap)
            regrouped_high = total(value for core, value in by_core.items()
                                   if ideal_norm(core) > cap)
            check(high == regrouped_high and add(low, high) == (direct, 0),
                  "strict_ratio_cut_recombines")
            check(low[1] == high[1] == 0, "cut_parts_are_real")
        summaries.append({"orientation": orientation,
                          "raw_positive_moment": direct,
                          "normalized_positive_moment": record_fraction(normalized),
                          "nonzero_core_groups": sum(v != ZERO for v in by_core.values()),
                          "nontrivial_gcd_mask_witnesses": missing_mask})

    d, r, m = F(9, 25), F(47752383, 67660000), F(54905017, 135320000)
    s, mu = F(3, 15625), F(12288947, 169150000000)
    g = F(51935541903, 169150000000)
    c_m = 2 * (1 - 2 * m) / 9
    gamma_j = d * c_m
    chi = 2 * s - mu - (2 * d * m + gamma_j - g)
    theta = F(5, 6) + r / 3
    for branch in (F(1), r, F(1, 3) + 5 * r / 6):
        check(theta > branch, "legal_inverse_operator_dominant_term")
    gap = theta + 2 * d * m + gamma_j - (1 + d * r - chi)
    check(gap > 0, "positive_inverse_sieve_does_not_close_fourth")
    check(chi == F(177302, 1321484375), "favorable_chi_matches_existing_note")
    check(d * r - chi - F(1, 4) == F(166737511, 42287500000),
          "half_ratio_cap_reserve_matches_existing_note")
    return {
        "date": "2026-10-09",
        "model": "GPT-6 (Codex)",
        "reasoning_effort": "inherited configuration; not exposed",
        "scope": "finite formal phases, exact regroupings, and rational exponent comparisons only",
        "assertions": sum(COUNTS.values()),
        "groups": dict(sorted(COUNTS.items())),
        "formal_prime_norms": list(NORMS),
        "sampled_formal_rows": len(rows),
        "inverse_squarefree_columns": len(squarefree),
        "orientation_summaries": summaries,
        "favorable_point": {
            "chi": record_fraction(chi),
            "inverse_operator_exponent": record_fraction(theta),
            "fourth_positive_sieve_exponent_deficit": record_fraction(gap),
        },
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
