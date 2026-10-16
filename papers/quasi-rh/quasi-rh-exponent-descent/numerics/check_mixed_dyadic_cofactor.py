#!/usr/bin/env python3
"""Exact finite dyadic large-cofactor checks; prints JSON and writes no files.

Prepared for Edward Baker with substantial LLM assistance, 9 October 2026.
Model: GPT-6 (Codex); inherited reasoning effort is not exposed.
Run with python3 -B. Formal ideal monoids, finite residue characters, and
rational budgets verify finite identities, not native analytic moments.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

# Importing the read-only dependency must not create a bytecode file.
sys.dont_write_bytecode = True
import check_mixed_signed_bilinear as native

COUNTS = Counter()
ZERO, ONE = native.ZERO, native.ONE
UNIT = (0,) * len(native.NORMS)


def check(value, group):
    COUNTS[group] += 1
    assert value, group


def rec(value):
    return {"exact": str(value), "decimal": float(value)}


@lru_cache(maxsize=None)
def squarefree_divisors(n):
    return tuple(product(*(range(min(e, 1) + 1) for e in n)))


@lru_cache(maxsize=None)
def h_coefficient(n, za, zb, threshold):
    """Sum mu(a)mu(b) over ab|n, inclusive caps, and strict ab>T."""
    ans = 0
    for a in squarefree_divisors(n):
        na = native.ideal_norm(a)
        if na > za:
            continue
        for b in squarefree_divisors(n):
            nb = native.ideal_norm(b)
            if nb <= zb and na * nb > threshold and native.divides(native.plus(a, b), n):
                ans += native.mu(a) * native.mu(b)
    return ans


def rational_budget_checks():
    d0, d1, r0, r1 = F(9, 25), F(21, 50), F(7, 10), F(73, 100)
    emax, target = F(1, 1200000), F(1, 700)
    corners = []
    for d, r, e in product((d0, d1), (r0, r1), (F(0), emax)):
        alpha = r / 2 - F(1, 4)
        delta = d * (2 * r - 1) - (1 + d) * alpha
        square = delta - (24 - 12 * r + 12 * alpha) * e
        cross = delta / 2 - (12 + 6 * alpha) * e
        check(delta == alpha * (3 * d - 1), "adaptive_exact_gain_factorization")
        check(24 - 12 * r + 12 * alpha == 21 - 6 * r,
              "adaptive_literal_short_buffer")
        check((e * (24 - 12 * r + 12 * alpha) + 12 * e * r) / 2
              == (12 + 6 * alpha) * e, "correlated_cross_buffer_before_maximization")
        check(F(1, 10) <= alpha <= F(23, 200), "adaptive_cut_in_uniform_range")
        x = r - alpha
        check(x == r / 2 + F(1, 4) and F(3, 5) <= x <= F(123, 200),
              "short_boundary_plain_quotient_at_least_three_fifths")
        # Exact derivatives prove the continuous corner minimum; corner
        # samples alone are not claimed as a continuous certificate.
        check(3 * alpha > 0 and 3 * alpha / 2 > 0,
              "short_and_cross_gains_increase_with_d")
        check((3 * d - 1) / 2 + 6 * e > 0
              and (3 * d - 1) / 4 - 3 * e > 0,
              "short_and_cross_gains_increase_with_r")
        check(-(21 - 6 * r) < 0 and -(12 + 6 * alpha) < 0,
              "short_and_cross_gains_decrease_with_buffer")
        corners.append((d, r, e, square, cross))
    square_min, cross_min = F(3993, 500000), F(7979, 2000000)
    check(min(row[3] for row in corners) == square_min,
          "literal_adaptive_short_square_minimum")
    check(min(row[4] for row in corners) == cross_min,
          "literal_adaptive_complete_removal_minimum")
    check(square_min > cross_min > target, "both_errors_fit_common_fourth_target")
    check(cross_min - target == F(35853, 14000000), "complete_removal_spare")
    # Throughout the box, the short square lies below the complete-removal
    # error: square-cross=delta/2-6e(2-2r+alpha).
    gap_lower = F(1, 125) / 2 - 6 * emax * (2 - 2 * r0 + F(23, 200))
    check(gap_lower > 0, "continuous_short_square_vs_cross_lower_envelope")
    for d, r, e, square, cross in corners:
        check(square - cross >= gap_lower, "short_square_vs_cross_corner_consistency")
    return {"adaptive_cut": "alpha = r/2 - 1/4",
            "plain_boundary": "x = r-alpha = r/2+1/4 in [3/5,123/200]",
            "domain": {"d": [str(d0), str(d1)], "r": [str(r0), str(r1)],
                       "literal_source_buffer": ["0", str(emax)]},
            "unbuffered_square_gain": "alpha(3d-1)",
            "literal_short_square_minimum": rec(square_min),
            "literal_complete_removal_minimum": rec(cross_min),
            "reserve_vs_1_700": rec(cross_min - target),
            "continuous_short_square_minus_cross_lower_bound": rec(gap_lower),
            "scope": "exact rational monotonicity and exponent comparison only"}


def gcd_coefficient_checks():
    zvalues = (F(1, 2), F(1), F(7), F(13), F(19), F(20), F(49), F(91))
    ideals = tuple(product(range(4), repeat=len(native.NORMS)))
    zero_higher_powers = 0
    for z in zvalues:
        for t in ideals:
            direct = sum(native.mu(a) * native.mu(b)
                         for a in squarefree_divisors(t) for b in squarefree_divisors(t)
                         if native.plus(a, b) == t
                         and native.ideal_norm(a) <= z and native.ideal_norm(b) <= z)
            if any(e > 2 for e in t):
                check(direct == 0, "cofactor_has_no_valuation_above_two")
                zero_higher_powers += 1
                continue
            g = tuple(e // 2 for e in t)
            h = tuple(e % 2 for e in t)
            check(all(not (a and b) for a, b in zip(g, h)),
                  "g_squared_h_factorization_is_coprime")
            partitions = 0
            for a0 in squarefree_divisors(h):
                b0 = native.quotient(h, a0)
                check(all(not (a and b) for a, b in zip(a0, b0)),
                      "ordered_h_partitions_are_coprime")
                if native.ideal_norm(native.plus(g, a0)) <= z and native.ideal_norm(native.plus(g, b0)) <= z:
                    partitions += 1
            check(direct == native.mu(h) * partitions,
                  "exact_truncated_cofactor_gcd_partition_formula")
    return {"caps": [str(z) for z in zvalues], "formal_ideals": len(ideals),
            "higher_power_zero_cases": zero_higher_powers,
            "formula": "c_Z(g^2 h) = mu(h) times ordered coprime squarefree h-partition count, with both original caps"}


def prime_power_branch_checks():
    cap_pairs = ((F(1, 2), F(20)), (F(1), F(1)), (F(7), F(13)),
                 (F(13), F(7)), (F(19), F(19)), (F(20), F(20)),
                 (F(49), F(91)))
    thresholds = (F(1, 2), F(1), F(7), F(13), F(14), F(19), F(49), F(91))
    for index, p in enumerate(native.NORMS):
        for other in product(range(3), repeat=len(native.NORMS) - 1):
            n0, remaining = [], iter(other)
            for i in range(len(native.NORMS)):
                n0.append(0 if i == index else next(remaining))
            n0 = tuple(n0)
            for k, caps, threshold in product(range(8), cap_pairs, thresholds):
                n = tuple(k if i == index else e for i, e in enumerate(n0))
                za, zb = caps
                rhs = sum((-1) ** (ea + eb) * h_coefficient(
                          n0, za / p ** ea, zb / p ** eb, threshold / p ** (ea + eb))
                          for ea, eb in product((0, 1), repeat=2) if ea + eb <= k)
                check(h_coefficient(n, za, zb, threshold) == rhs,
                      "exact_prime_power_branch_with_rescaled_caps_and_strict_cut")
                if k >= 2:
                    square = tuple(2 if i == index else e for i, e in enumerate(n0))
                    check(h_coefficient(n, za, zb, threshold)
                          == h_coefficient(square, za, zb, threshold),
                          "prime_power_branch_saturates_from_exponent_two")
    check(h_coefficient(UNIT, F(1), F(1), F(1, 2)) == 1,
          "rescaled_threshold_below_one_retains_unit_pair")
    check(h_coefficient(UNIT, F(1), F(1), F(1)) == 0,
          "strict_threshold_equality_excludes_unit_pair")
    check(h_coefficient(UNIT, F(1, 2), F(1), F(0)) == 0,
          "rescaled_cap_below_one_is_empty")
    witnesses = []
    for index, p in enumerate(native.NORMS):
        n = tuple(2 if i == index else 0 for i in range(len(native.NORMS)))
        check(h_coefficient(n, F(p), F(p), F(p - 1)) == -1,
              "prime_square_large_cofactor_coefficient_is_minus_one")
        check(h_coefficient(n, F(p), F(p), F(p)) == 1,
              "strict_prime_threshold_removes_two_unbalanced_pairs")
        check(h_coefficient(n, F(p), F(p), F(p * p)) == 0,
              "strict_prime_square_product_endpoint_is_excluded")
        witnesses.append({"prime_norm": p, "square_norm": p * p,
                          "Z": p, "T": p - 1, "large_cofactor_coefficient": -1})
    return {"prime_exponents": list(range(8)), "cap_pairs": [[str(a), str(b)] for a, b in cap_pairs],
            "thresholds": [str(t) for t in thresholds],
            "prime_square_witnesses": witnesses,
            "scope": "coefficient identity includes empty rescaled caps, unit quotients, and inclusive cap endpoints"}


def dyad(n):
    assert n >= 1
    return n.bit_length() - 1


def dyadic_selected_checks():
    z, threshold, normalizer = 20, 14, 200
    columns = native.ideals_up_to(z * z)
    small = tuple(n for n in native.ideals_up_to(z) if native.mu(n))
    terms, blocks = [], {}
    for a, b in product(small, repeat=2):
        nab = native.ideal_norm(a) * native.ideal_norm(b)
        if nab <= threshold:
            continue
        for ell in native.ideals_up_to(z * z // nab):
            n = native.plus(native.plus(a, b), ell)
            if native.profile(native.ideal_norm(n)) == ZERO:
                continue
            key = tuple(dyad(native.ideal_norm(v)) for v in (a, b, ell))
            check(all(2 ** j <= native.ideal_norm(v) < 2 ** (j + 1)
                      for j, v in zip(key, (a, b, ell))),
                  "exact_half_open_dyadic_factor_partition")
            check(native.ideal_norm(a) <= z and native.ideal_norm(b) <= z
                  and nab > threshold, "dyadic_blocks_retain_both_caps_and_strict_product_cut")
            term = (a, b, ell, n, -native.mu(a) * native.mu(b))
            terms.append(term)
            blocks.setdefault(key, []).append(term)
    check(len(terms) == sum(len(v) for v in blocks.values()), "dyadic_partition_has_no_lost_or_repeated_tuple")
    for j in range(1, 12):
        check(dyad(2 ** j) == j and dyad(2 ** j - 1) == j - 1,
              "half_open_power_of_two_endpoints")
    check(any(a == UNIT or b == UNIT for a, b, *_ in terms), "unbalanced_squarefree_factors_present")
    check(any(ell == UNIT for _, _, ell, *_ in terms), "unit_plain_quotient_present")
    check(any(native.mu(n) == 0 for _, _, _, n, _ in terms), "squareful_annular_columns_present")
    check(any(native.profile(native.ideal_norm(n))[1] != 0 for _, _, _, n, _ in terms),
          "original_annular_profile_has_nonreal_coefficients")
    for n in columns:
        grouped = sum(c for _, _, _, column, c in terms if column == n)
        expected = -h_coefficient(n, F(z), F(z), F(threshold))
        if native.profile(native.ideal_norm(n)) == ZERO:
            expected = 0
        check(grouped == expected, "dyadic_tuple_recombination_equals_large_cofactor_divisor_coefficient")
    keys, orientation_records = sorted(blocks), []
    zero_witnesses = 0
    for orientation in (1, -1):
        full_moment = short_moment = large_moment = diagonal_moment = 0
        full_short_cross, ordered_cross = ZERO, ZERO
        for row in product(*(range(p) for p in native.NORMS)):
            phases = {n: native.psi(row, n, orientation) for n in columns}
            original = native.total(native.scale(native.mul(phases[n], native.profile(native.ideal_norm(n))), native.mu(n))
                                    for n in columns)
            block_values = []
            for key in keys:
                value = native.total(native.scale(native.mul(phases[n], native.profile(native.ideal_norm(n))), c)
                                     for _, _, _, n, c in blocks[key])
                block_values.append(value)
            large = native.total(block_values)
            short = native.total(native.scale(native.mul(phases[n], native.profile(native.ideal_norm(n))),
                                              -sum(native.mu(a) * native.mu(b) for a, b in product(small, repeat=2)
                                                   if native.ideal_norm(a) * native.ideal_norm(b) <= threshold
                                                   and native.divides(native.plus(a, b), n))) for n in columns)
            check(native.add(short, large) == original,
                  "native_both_orientation_original_annulus_reconstruction")
            paired = native.total(native.mul(a, native.conj(b)) for a, b in product(block_values, repeat=2))
            check(paired == native.scale(ONE, native.norm2(large)),
                  "all_ordered_dyadic_cross_terms_reconstruct_positive_norm")
            for n in columns:
                if any(e and residue == 0 for e, residue in zip(n, row)):
                    check(phases[n] == ZERO, "physical_zeros_retained_in_squareful_and_higher_power_columns")
                    zero_witnesses += 1
            plain = native.total(phases[n] for n in columns if 15 <= native.ideal_norm(n) <= 100)
            weight = native.norm2(plain) ** 2 * native.norm2(phases[(0, 1, 0)])
            if (row[0] + 2 * row[1] + 3 * row[2]) % 5 == 0:
                weight = 0
            full_moment += weight * native.norm2(original)
            short_moment += weight * native.norm2(short)
            large_moment += weight * native.norm2(large)
            diagonal_moment += weight * sum(native.norm2(v) for v in block_values)
            ordered_cross = native.add(ordered_cross, native.scale(paired, weight))
            full_short_cross = native.add(full_short_cross, native.scale(native.mul(original, native.conj(short)), weight))
        check(ordered_cross == native.scale(ONE, large_moment),
              "selected_weighted_ordered_block_pairs_equal_large_moment")
        real_twice = 2 * full_short_cross[0] + full_short_cross[1]
        check(full_moment - large_moment == real_twice - short_moment,
              "selected_full_short_cross_controls_complete_removal")
        check(native.norm2(full_short_cross) <= full_moment * short_moment,
              "selected_weighted_complex_Cauchy")
        check(F(full_moment - large_moment, normalizer)
              == F(real_twice - short_moment, normalizer),
              "original_inverse_square_normalizer_retained")
        check(full_moment > 0 and short_moment > 0 and large_moment > 0,
              "selected_original_short_and_large_moments_nonzero")
        check(large_moment != diagonal_moment, "dyadic_selected_cross_terms_cannot_be_discarded")
        orientation_records.append({"orientation": orientation,
                                    "original_moment": str(F(full_moment, normalizer)),
                                    "short_moment": str(F(short_moment, normalizer)),
                                    "large_cofactor_moment": str(F(large_moment, normalizer)),
                                    "block_diagonal_moment": str(F(diagonal_moment, normalizer)),
                                    "ordered_off_diagonal_contribution": str(F(large_moment - diagonal_moment, normalizer))})
    return {"Z": z, "strict_product_threshold": threshold, "inverse_normalizer": normalizer,
            "formal_columns": len(columns), "retained_tuples": len(terms),
            "half_open_dyadic_blocks": len(blocks), "block_indices": [list(k) for k in keys],
            "finite_CRT_rows_per_orientation": 7 * 13 * 19,
            "physical_zero_witnesses": zero_witnesses, "orientation_records": orientation_records,
            "scope": "formal good-prime ideals and finite local residue characters, with complex finite annular values and a selected positive response weight"}


def run():
    budgets = rational_budget_checks()
    gcd_coefficients = gcd_coefficient_checks()
    prime_branches = prime_power_branch_checks()
    dyadic = dyadic_selected_checks()
    dependency_path = Path(native.__file__)
    return {"date": "2026-10-09", "author": "Prepared for Edward Baker with substantial LLM assistance",
            "model": "GPT-6 (Codex)", "reasoning_effort": "inherited configuration; not exposed",
            "status": "exact finite coefficient identities and rational budgets; no asymptotic moment proved",
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "dependency_sha256": {dependency_path.name: hashlib.sha256(dependency_path.read_bytes()).hexdigest()},
            "assertions": sum(COUNTS.values()), "groups": dict(sorted(COUNTS.items())),
            "dependency_initialization_assertions": sum(native.COUNTS.values()),
            "adaptive_budget": budgets, "gcd_coefficient_identity": gcd_coefficients,
            "prime_power_branch_identity": prime_branches, "dyadic_selected_recombination": dyadic,
            "limitations": ["No native reciprocity or lattice Poisson theorem is certified.",
                            "Finite annular values do not establish smooth-profile or derivative uniformity.",
                            "No selected detector-bin population, source coefficient extension, or new moment is proved.",
                            "No asymptotic pair count, family-boundary improvement, or RH implication is proved."]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
