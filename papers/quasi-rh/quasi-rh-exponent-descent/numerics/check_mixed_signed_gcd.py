#!/usr/bin/env python3
"""Exact identities for mixed note 14; prints JSON and writes no files.

Prepared for Edward Baker, 9 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex). Effort: inherited configuration, not exposed.
Formal monoids validate algebra and rational reserves, not native characters,
buffered reciprocal bounds, selected bins, or an asymptotic mixed moment.
Uses the exact phase arithmetic from check_mixed_mobius_ratio_core.py.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

import check_mixed_mobius_ratio_core as m

COUNTS = Counter()
SF = tuple(product(range(2), repeat=4))
ZERO_IDEAL = (0, 0, 0, 0)
D = 12


def check(condition, group):
    COUNTS[group] += 1
    if not condition:
        raise AssertionError(group)


def coprime(a, b):
    return all(not (x and y) for x, y in zip(a, b))


def polynomial(row, q, orientation, delete=True):
    return m.total(m.scale(m.mul(m.profile(m.plus(q, c)),
                                m.psi(row, c, orientation)), m.mobius(c))
                   for c in SF if not delete or coprime(c, q))


def smooth_ideals(q):
    # Norms above 30 cannot contribute to any original-profile term.
    return tuple(k for k in product(range(5), repeat=4)
                 if all(not e or allowed for e, allowed in zip(k, q))
                 and m.ideal_norm(k) <= 30)


def run():
    rows = tuple(dict.fromkeys(tuple(product(range(6), repeat=4))[::37]
                              + tuple(product(range(6), repeat=4))[:12]))
    plain = tuple(c for c in product(range(3), repeat=4)
                  if 2 <= m.ideal_norm(c) <= 35)
    primes = tuple(tuple(int(i == j) for i in range(4)) for j in range(4))
    summaries = []
    for orientation in (1, -1):
        weights = {}
        for row in rows:
            s = m.total(m.mul((1 + m.ideal_norm(c) % 3,
                               m.ideal_norm(c) % 2),
                              m.psi(row, c, orientation)) for c in plain)
            q = m.total(m.mul(m.ROOTS[j], m.psi(row, c, orientation))
                        for j, c in enumerate(primes))
            selector = int(row != ZERO_IDEAL and sum(row) % 3 != 1)
            weights[row] = selector * m.norm2(s) ** 2 * m.norm2(q)
        check(sum(weights.values()) > 0, "assembled_selected_fourth_weight")

        for row, q in product(rows, SF):
            lhs = polynomial(row, q, orientation)
            rhs = m.total(m.mul(m.psi(row, k, orientation),
                                polynomial(row, m.plus(q, k), orientation,
                                           delete=False))
                          for k in smooth_ideals(q))
            check(lhs == rhs, "deleted_inverse_q_smooth_convolution")

        direct_by_g = {g: m.ZERO for g in SF}
        small_by_g = {g: m.ZERO for g in SF}
        cap = F(8)  # sqrt(64); equality remains in the small sector.
        for left, right in product(SF, repeat=2):
            g, a, b, core, _ = m.split(left, right)
            check(m.mobius(left) * m.mobius(right)
                  == m.mobius(a) * m.mobius(b), "gcd_sign_squares_away")
            coefficient = m.scale(m.mul(m.profile(left),
                                        m.conj(m.profile(right))),
                                  m.mobius(left) * m.mobius(right))
            kernel = m.total(m.scale(m.mul(m.psi(row, left, orientation),
                                          m.conj(m.psi(row, right, orientation))),
                                    weights[row]) for row in rows)
            term = m.mul(coefficient, kernel)
            direct_by_g[g] = m.add(direct_by_g[g], term)
            if m.ideal_norm(core) <= cap:
                small_by_g[g] = m.add(small_by_g[g], term)

        inversion_by_g = {}
        nonzero_alternating_terms = 0
        deleted_gcd_changes = 0
        for g in SF:
            answer = 0
            for h in SF:
                if not coprime(g, h):
                    continue
                q = m.plus(g, h)
                for row in rows:
                    square = m.norm2(polynomial(row, q, orientation))
                    mask = m.norm2(m.psi(row, q, orientation))
                    contribution = weights[row] * mask * square
                    answer += m.mobius(h) * contribution
                    nonzero_alternating_terms += bool(contribution)
                    deleted_gcd_changes += bool(weights[row] * square and not mask)
            inversion_by_g[g] = (answer, 0)
            check(inversion_by_g[g] == direct_by_g[g],
                  "fixed_gcd_coprimality_inversion")
        check(nonzero_alternating_terms > 0, "alternating_short_squares_nonempty")
        check(deleted_gcd_changes > 0, "canceled_zero_mask_is_essential")

        for cutoff in (F(3, 2), F(2), F(5), F(10)):
            high = m.total(v for g, v in direct_by_g.items()
                           if m.ideal_norm(g) >= cutoff)
            inverted = m.total(v for g, v in inversion_by_g.items()
                               if m.ideal_norm(g) >= cutoff)
            low = m.total(v for g, v in small_by_g.items()
                          if m.ideal_norm(g) >= cutoff)
            large_direct = m.total(m.add(v, m.scale(small_by_g[g], -1))
                                   for g, v in direct_by_g.items()
                                   if m.ideal_norm(g) >= cutoff)
            check(high == inverted, "whole_high_gcd_sector")
            check(large_direct == m.add(inverted, m.scale(low, -1)),
                  "restore_strict_ratio_cut_by_subtraction")
            check(high[1] == low[1] == large_direct[1] == 0,
                  "all_filtered_parts_are_real")
            check(F(high[0], D) == F(inverted[0], D),
                  "original_inverse_normalization")

            low_gcd = m.total(v for g, v in inversion_by_g.items()
                              if m.ideal_norm(g) < cutoff)
            regrouped = 0
            lambdas = {}
            for q in SF:
                divisors = tuple(g for g in SF
                                 if all(x <= y for x, y in zip(g, q)))
                coefficient = sum(m.mobius(tuple(y - x for x, y in zip(g, q)))
                                  for g in divisors if m.ideal_norm(g) < cutoff)
                lambdas[q] = coefficient
                if 1 < m.ideal_norm(q) < cutoff:
                    check(coefficient == 0,
                          "truncated_divisor_weight_cancels_small_q")
                regrouped += coefficient * sum(
                    weights[row] * m.norm2(m.psi(row, q, orientation))
                    * m.norm2(polynomial(row, q, orientation)) for row in rows)
            check(lambdas[ZERO_IDEAL] == 1,
                  "truncated_divisor_weight_at_identity")
            check(low_gcd == (regrouped, 0),
                  "low_gcd_signed_square_aggregate")
            if cutoff == 2:
                check(any(v < 0 for v in lambdas.values())
                      and any(v > 0 for q, v in lambdas.items() if q != ZERO_IDEAL),
                      "truncated_divisor_weights_have_both_signs")

        # A0 support is [1/2,5/2], U=64, cube root U=4.
        # G0=cD/U^(1/3)=3/2; remaining gcd is 1, so f>U^(2/3).
        geometry_count = 0
        for left, right in product(SF, repeat=2):
            if m.profile(left) == m.ZERO or m.profile(right) == m.ZERO:
                continue
            g, a, b, core, _ = m.split(left, right)
            if m.ideal_norm(g) < F(3, 2):
                geometry_count += 1
                check(m.ideal_norm(core) > 16,
                      "global_strip_joint_cut_implies_two_thirds_core")
        check(geometry_count > 0, "remaining_joint_geometry_nonempty")
        summaries.append({"orientation": orientation,
                          "raw_moment": m.total(direct_by_g.values())[0],
                          "nonzero_alternating_terms": nonzero_alternating_terms,
                          "essential_mask_witnesses": deleted_gcd_changes,
                          "remaining_geometry_pairs": geometry_count})

    c_star, q_star, d_min, r_min = F(1, 540), F(1, 125), F(9, 25), F(7, 10)
    gcd_reserve = d_min * q_star - c_star
    inherited_reserve = F(140772625414022617, 64335535541550000000)
    check(gcd_reserve == F(347, 337500), "exact_uniform_gcd_reserve")
    check(gcd_reserve > F(1, 1000), "gcd_reserve_exceeds_one_thousandth")
    rho, r_max = F(1, 100000), F(73, 100)
    buffered_reserve = gcd_reserve - rho * (r_max - q_star)
    check(buffered_reserve > F(1, 1000),
          "literal_source_buffer_fits_gcd_reserve")
    completion_eta = F(1, 25000)
    completion_reserve = d_min * (q_star - completion_eta) - c_star
    check(completion_reserve == F(17107, 16875000),
          "compatible_completion_boundary_reserve")
    completion_buffered_reserve = completion_reserve - rho * (
        r_max - q_star + completion_eta)
    check(completion_buffered_reserve > F(1, 1000),
          "literal_source_buffer_fits_completion_reserve")
    check(inherited_reserve > F(1, 500), "old_small_ratio_reserve_retained")
    check(2 * r_min - 2 * q_star == F(173, 125),
          "coarse_remaining_core_exponent")
    check(2 * r_min - 2 * q_star > F(1, 2),
          "remaining_core_automatically_above_old_cap")
    for d in (F(9, 25), F(39, 100), F(21, 50)):
        for r in (F(7, 10), F(47752383, 67660000), F(73, 100)):
            check(1 + d * (r - q_star)
                  <= 1 + d * r - c_star - gcd_reserve,
                  "gcd_sector_exponent_comparison")
    source = Path(__file__)
    return {"date": "2026-10-09", "model": "GPT-6 (Codex)",
            "reasoning_effort": "inherited configuration; not exposed",
            "scope": "finite exact algebra and rational exponent comparisons only",
            "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "phase_dependency_sha256": hashlib.sha256(
                source.with_name("check_mixed_mobius_ratio_core.py").read_bytes()).hexdigest(),
            "assertions": sum(COUNTS.values()), "groups": dict(sorted(COUNTS.items())),
            "formal_prime_norms": list(m.NORMS), "formal_rows": len(rows),
            "orientation_summaries": summaries,
            "budget": {"common_fourth_saving": str(c_star),
                       "gcd_cutoff_exponent": str(q_star),
                       "uniform_gcd_reserve": str(gcd_reserve),
                       "literal_buffer_exponent_allowance": str(rho),
                       "gcd_reserve_after_literal_buffer": str(buffered_reserve),
                       "compatible_completion_mask_exponent": str(completion_eta),
                       "compatible_completion_boundary_reserve": str(completion_reserve),
                       "completion_reserve_after_literal_buffer": str(completion_buffered_reserve),
                       "inherited_small_ratio_reserve": str(inherited_reserve),
                       "coarse_remaining_core_exponent": str(2 * r_min - 2 * q_star)}}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
