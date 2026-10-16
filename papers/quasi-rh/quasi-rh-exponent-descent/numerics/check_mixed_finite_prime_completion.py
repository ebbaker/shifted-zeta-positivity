#!/usr/bin/env python3
"""Exact finite checks for finite-prime completion of a selected ratio form.

Prepared for Edward Baker, 9 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed.
Formal phases verify algebra, not reciprocity, selected bins or an asymptotic
signed estimate. Uses the standard library, prints JSON, and writes no files.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import prod
import hashlib
import json
from pathlib import Path


ZERO, ONE = (0, 0), (1, 0)
ROOTS = (ONE, (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
NORMS = (2, 3, 5, 7)
PAIRING = ((0, 1, 2, 3), (1, 0, 5, 2), (2, 5, 0, 1), (3, 2, 1, 0))
COUNTS = Counter()


def check(condition, name):
    COUNTS[name] += 1
    assert condition, name


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


def ideal_norm(c):
    return prod(n ** e for n, e in zip(NORMS, c))


def mu(c):
    return (-1) ** sum(c)


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def core(a, b):
    return tuple(abs(x - y) for x, y in zip(a, b))


def gcd(a, b):
    return tuple(min(x, y) for x, y in zip(a, b))


def psi(row, column, orientation):
    if any(x and y for x, y in zip(row, column)):
        return ZERO
    native = sum(row[i] * PAIRING[i][j] * column[j]
                 for i in range(4) for j in range(4))
    fixed = sum((i + 1) * e for i, e in enumerate(column))
    return ROOTS[(orientation * native + fixed) % 6]


def profile(c):
    n = ideal_norm(c)
    if not 6 <= n <= 30:
        return ZERO
    return scale(ROOTS[n % 6], 1 + n % 3)


def divisors(mask):
    return tuple(c for c in SQUAREFREE
                 if all(e <= m for e, m in zip(c, mask)))


def p_free(mask):
    return tuple(c for c in SQUAREFREE
                 if all(not (e and m) for e, m in zip(c, mask)))


def split_at_mask(c, mask):
    b = tuple(e * m for e, m in zip(c, mask))
    e = tuple(x - y for x, y in zip(c, b))
    return b, e


SQUAREFREE = tuple(product(range(2), repeat=4))
all_rows = tuple(product(range(6), repeat=4))
ROWS = tuple(dict.fromkeys(all_rows[::31] + all_rows[:10]))
CAPS = (F(5), F(49, 2), F(35), F(65))


def run():
    plain = tuple(c for c in product(range(3), repeat=4)
                  if 2 <= ideal_norm(c) <= 35)
    primes = tuple(tuple(int(i == j) for i in range(4)) for j in range(4))
    weights = {}
    for row in ROWS:
        s = total(mul((1 + ideal_norm(c) % 3, ideal_norm(c) % 2),
                      psi(row, c, 1)) for c in plain)
        q = total(mul(ROOTS[j], psi(row, c, 1))
                  for j, c in enumerate(primes))
        selector = int(sum(row) % 3 != 1 and row != (0, 0, 0, 0))
        weights[row] = selector * norm2(s) ** 2 * norm2(q)
    check(sum(weights.values()) > 0, "nonzero_selected_fourth_weight")
    summaries = []
    deleted_gcd_term_observed = False
    compatible_completed_nonzero = False
    compatible_boundary_nonzero = False
    for orientation in (1, -1):
        direct_amplitudes = {
            row: total(scale(mul(profile(c), psi(row, c, orientation)), mu(c))
                       for c in SQUAREFREE) for row in ROWS}
        pair_terms = {
            (left, right): total(scale(mul(
                mul(profile(left), conj(profile(right))),
                mul(psi(row, left, orientation),
                    conj(psi(row, right, orientation)))),
                weights[row] * mu(left) * mu(right)) for row in ROWS)
            for left, right in product(SQUAREFREE, repeat=2)}
        for mask in SQUAREFREE:
            divs, free = divisors(mask), p_free(mask)
            for c in SQUAREFREE:
                b, e = split_at_mask(c, mask)
                check(plus(b, e) == c and b in divs and e in free,
                      "unique_column_split")
            paired = {}
            for row in ROWS:
                for e in free:
                    paired[row, e] = total(
                        scale(mul(psi(row, b, orientation),
                                  profile(plus(b, e))), mu(b)) for b in divs)
                completed = total(
                    scale(mul(psi(row, e, orientation), paired[row, e]), mu(e))
                    for e in free)
                check(completed == direct_amplitudes[row],
                      "completed_inverse_amplitude")
                mellin_sum = total(scale(psi(row, b, orientation),
                                         F(mu(b), ideal_norm(b))) for b in divs)
                euler = ONE
                for p in primes:
                    if p in divs:
                        euler = mul(euler, add(ONE, scale(
                            psi(row, p, orientation), -F(1, ideal_norm(p)))))
                check(mellin_sum == euler, "finite_mellin_euler_multiplier")
            for cap in CAPS:
                direct_high, crossing, stable_original = ZERO, ZERO, ZERO
                has_equality, has_crossing = False, False
                for left, right in product(SQUAREFREE, repeat=2):
                    b, e = split_at_mask(left, mask)
                    bp, ep = split_at_mask(right, mask)
                    full = ideal_norm(core(left, right))
                    base = ideal_norm(core(e, ep))
                    finite = ideal_norm(core(b, bp))
                    check(full == base * finite and finite <= ideal_norm(mask),
                          "exact_factorization_of_ratio_core")
                    term = pair_terms[left, right]
                    if full > cap:
                        direct_high = add(direct_high, term)
                    if base > cap:
                        stable_original = add(stable_original, term)
                        check(full > cap, "stable_high_contains_every_prime_state")
                    elif full > cap:
                        crossing = add(crossing, term)
                        check(full <= cap * ideal_norm(mask),
                              "crossing_shell_full_ratio_cap")
                        has_crossing = has_crossing or term != ZERO
                    has_equality = has_equality or full == cap
                stable_completed = total(
                    scale(mul(mul(psi(row, e, orientation),
                                  conj(psi(row, ep, orientation))),
                              mul(paired[row, e], conj(paired[row, ep]))),
                          weights[row] * mu(e) * mu(ep))
                    for e, ep in product(free, repeat=2)
                    if ideal_norm(core(e, ep)) > cap for row in ROWS)
                check(stable_completed == stable_original,
                      "filtered_complete_prime_pairing")
                check(add(stable_completed, crossing) == direct_high,
                      "signed_remainder_equals_stable_plus_crossing")
                check(stable_completed[1] == crossing[1] == direct_high[1] == 0,
                      "all_three_forms_real_by_reversal")
                if cap in (F(5), F(35)):
                    check(has_equality, "strict_cutoff_equality_present")
                summaries.append({"orientation": orientation,
                                  "mask_norm": ideal_norm(mask),
                                  "cap": str(cap),
                                  "nonzero_crossing": has_crossing})
            for gcd_cutoff in (F(2), F(5), F(10), F(35)):
                free_gcd_cutoff = gcd_cutoff / ideal_norm(mask)
                original_low_gcd = ZERO
                completed_direct = ZERO
                boundary_direct = ZERO
                boundary_by_whole_gcd = ZERO
                for left, right in product(SQUAREFREE, repeat=2):
                    b, e = split_at_mask(left, mask)
                    bp, ep = split_at_mask(right, mask)
                    full_gcd = gcd(left, right)
                    finite_gcd = gcd(b, bp)
                    free_gcd = gcd(e, ep)
                    check(plus(finite_gcd, free_gcd) == full_gcd,
                          "compatible_gcd_factorization")
                    _, full_gcd_p_free = split_at_mask(full_gcd, mask)
                    check(full_gcd_p_free == free_gcd,
                          "boundary_membership_depends_only_on_original_gcd")
                    term = pair_terms[left, right]
                    if ideal_norm(full_gcd) < gcd_cutoff:
                        original_low_gcd = add(original_low_gcd, term)
                        if profile(left) != ZERO and profile(right) != ZERO:
                            check(F(ideal_norm(core(left, right)))
                                  > F(36) / gcd_cutoff ** 2,
                                  "low_gcd_original_annuli_force_large_ratio")
                        if ideal_norm(free_gcd) >= free_gcd_cutoff:
                            boundary_direct = add(boundary_direct, term)
                    if ideal_norm(free_gcd) < free_gcd_cutoff:
                        completed_direct = add(completed_direct, term)
                        check(ideal_norm(full_gcd) < gcd_cutoff,
                              "stable_free_gcd_all_prime_states_below_full_cutoff")
                    if (ideal_norm(full_gcd) < gcd_cutoff
                            and ideal_norm(full_gcd_p_free) >= free_gcd_cutoff):
                        boundary_by_whole_gcd = add(boundary_by_whole_gcd, term)
                completed_gcd_filtered = total(
                    scale(mul(mul(psi(row, e, orientation),
                                  conj(psi(row, ep, orientation))),
                              mul(paired[row, e], conj(paired[row, ep]))),
                          weights[row] * mu(e) * mu(ep))
                    for e, ep in product(free, repeat=2)
                    if ideal_norm(gcd(e, ep)) < free_gcd_cutoff for row in ROWS)
                check(completed_gcd_filtered == completed_direct,
                      "compatible_filtered_complete_prime_pairing")
                check(boundary_direct == boundary_by_whole_gcd,
                      "compatible_boundary_is_union_of_whole_fixed_gcd_forms")
                check(add(completed_gcd_filtered, boundary_direct) == original_low_gcd,
                      "near_remainder_equals_completed_plus_gcd_boundary")
                check(completed_gcd_filtered[1] == boundary_direct[1]
                      == original_low_gcd[1] == 0,
                      "compatible_forms_real_by_reversal")
                if ideal_norm(mask) > 1:
                    compatible_completed_nonzero |= completed_gcd_filtered != ZERO
                    compatible_boundary_nonzero |= boundary_direct != ZERO
        for row in ROWS:
            for p in primes:
                for e, ep in product(p_free(p), repeat=2):
                    a, ap = profile(e), profile(plus(p, e))
                    b, bp = profile(ep), profile(plus(p, ep))
                    phase = psi(row, p, orientation)
                    four = total((mul(a, conj(b)),
                                  scale(mul(mul(phase, ap), conj(b)), -1),
                                  scale(mul(mul(conj(phase), a), conj(bp)), -1),
                                  scale(mul(ap, conj(bp)), norm2(phase))))
                    product_form = mul(add(a, scale(mul(phase, ap), -1)),
                                       conj(add(b, scale(mul(phase, bp), -1))))
                    check(four == product_form, "four_states_keep_gcd_zero_mask")
                    if phase == ZERO and mul(ap, conj(bp)) != ZERO:
                        deleted_gcd_term_observed = True
                phase = psi(row, p, orientation)
                n = ideal_norm(p)
                s, t, z = 1, 2, 1
                explicit = total((ONE,
                                  scale(phase, -F(1, n ** (s + z))),
                                  scale(conj(phase), -F(1, n ** (t + z))),
                                  (F(norm2(phase), n ** (s + t)), 0)))
                local_states = total((ONE,
                    scale(phase, -F(1, n ** (s + z))),
                    scale(conj(phase), -F(1, n ** (t + z))),
                    scale(mul(phase, conj(phase)), F(1, n ** (s + t)))))
                check(explicit == local_states, "three_variable_gcd_euler_factor")
                zero_ratio_factor = total((ONE,
                    scale(phase, -F(1, n ** s)),
                    scale(conj(phase), -F(1, n ** t)),
                    (F(norm2(phase), n ** (s + t)), 0)))
                inverse_l_factors = mul(add(ONE, scale(phase, -F(1, n ** s))),
                                        add(ONE, scale(conj(phase), -F(1, n ** t))))
                check(zero_ratio_factor == inverse_l_factors,
                      "uncut_euler_factor_splits_into_two_inverse_l_factors")
    gamma = F(140772625414022617, 64335535541550000000)
    eta = F(1, 250)
    reserve = gamma - eta / 2
    check(reserve == F(12101554330922617, 64335535541550000000),
          "exact_uniform_crossing_reserve")
    check(reserve > 0, "uniform_mask_budget_positive")
    check(any(s["nonzero_crossing"] for s in summaries),
          "crossing_error_is_not_formally_zero")
    check(deleted_gcd_term_observed, "dropping_gcd_mask_changes_a_nonzero_term")
    check(compatible_completed_nonzero,
          "nonunit_mask_compatible_completed_form_nonzero")
    check(compatible_boundary_nonzero,
          "nonunit_mask_compatible_gcd_boundary_nonzero")
    compatible_eta = F(1, 25000)
    compatible_reserve = F(9, 25) * (F(1, 125) - compatible_eta) - F(1, 540)
    check(compatible_reserve == F(17107, 16875000),
          "exact_compatible_gcd_boundary_reserve")
    check(compatible_reserve > F(1, 1000),
          "compatible_gcd_boundary_reserve_exceeds_one_thousandth")
    buffered_compatible_reserve = compatible_reserve - F(1, 100000) * (
        F(73, 100) - F(1, 125) + compatible_eta)
    check(buffered_compatible_reserve == F(67940623, 67500000000),
          "exact_compatible_fixed_buffer_reserve")
    check(buffered_compatible_reserve > F(1, 1000),
          "compatible_fixed_buffer_reserve_exceeds_one_thousandth")
    return {"status": "PASS", "model": "GPT-6 (Codex)",
            "reasoning_effort": "inherited, not exposed",
            "scope": "finite algebra; no native/asymptotic correlation certified",
            "assertions": sum(COUNTS.values()), "groups": dict(sorted(COUNTS.items())),
            "rows": len(ROWS), "prime_masks": len(SQUAREFREE),
            "orientations": [1, -1], "crossing_reserve_exact": str(reserve),
            "crossing_reserve_decimal": float(reserve),
            "compatible_mask_exponent": str(compatible_eta),
            "compatible_boundary_reserve_exact": str(compatible_reserve),
            "compatible_boundary_reserve_decimal": float(compatible_reserve),
            "compatible_fixed_buffer_reserve_exact": str(buffered_compatible_reserve),
            "compatible_fixed_buffer_rho_cap": str(F(1, 100000)),
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
