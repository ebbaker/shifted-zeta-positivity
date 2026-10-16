#!/usr/bin/env python3
"""Exact finite centered coefficients, owned extraction, and gated row masks.

Prepared for Edward Baker with substantial LLM assistance, 9 October 2026.
Model: GPT-6 (Codex), inherited configuration; reasoning effort not exposed.
Same-model internal arithmetic audit; no analytic smooth decay is proved.
Standard library only. Deterministic JSON is written to stdout.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

COUNTS = Counter()
ZERO, ONE = (F(0), F(0)), (F(1), F(0))
ROOTS = (ONE, (F(0), F(1)), (F(-1), F(1)), (F(-1), F(0)),
         (F(0), F(-1)), (F(1), F(-1)))
PARAMETERS = {
    "coefficient_prime_norms": [7, 13, 19],
    "D": 140, "N": 20, "Y1": 10, "Y2": 40, "slot_scale": 10,
    "live_slot_prime_norms": [7, 13],
    "profile_support": "1/2 <= norm/scale <= 2, including endpoints",
    "inverse_profile": "(2-t)+(1/3+t)*omega on support",
    "plain_profile": "(1+t)+(1-t/2)*omega on support",
    "slot_profile": "indicator of support; fixed complex coefficients at 7 and 13",
    "coefficient_row_local_values": ["zero", "1", "omega", "omega^2", "omega^3", "omega^4", "omega^5"],
    "selected_weight": "0 if index sum mod 4 is 0, otherwise 1+index sum",
    "projector_prime_weights": [2, 3, 16777259],
    "projector_U": 64 * 16777259,
    "projector_radial_envelope": "1 on U/4 <= norm(u) <= U, otherwise 0",
    "projector_m": "2/5", "high_conductor_exponent_margin": "1/1000",
    "projector_conductor": "product of prime weights with physical valuation mod 6 nonzero",
    "underlying_native_conductor_identification": "Imported native hypothesis; the synthetic conductor model is not its proof",
    "projector_character_phase": "omega^(sum_i((row_i mod 6)*column_(i+1 mod 3))), with original physical support zeros",
    "projector_full_selected_weight": "high-conductor and radial gates times 1+sum(physical valuations)",
    "projector_polynomial_columns": ["unit", "prime of weight 2", "prime of weight 3", "large prime"],
    "scope": "Formal monoids and synthetic multiplicative characters; no native field conductor transfer",
    "exponent_ledger": {
        "closed_comparison_box": {"d": ["9/25", "21/50"], "r": ["7/10", "73/100"], "m": ["2/5", "207/500"]},
        "adaptive_auxiliary_cutoff": "kappa0=m+d*r/2-1/1000",
        "uniform_auxiliary_cutoff": "21/40",
        "conditional_nonprincipal_completion_squared_exponent": "min(x,kappa-x)",
        "auxiliary_centered_mass_exponent": "1+2*kappa-2*m, before fixed costs",
        "target_saving": "1/700",
        "optional_physical_decay_cutoff": "27/100",
        "conditional_effective_completion_radius_exponent": "(1+5*kappa)/6",
        "height_and_profile_cost": "Uninstantiated positive fixed cost b_A*eta_ht + L_other; must fit strictly inside the stated reserve",
        "height_quantifier_order": "For desired power L, fix internal decay order A and finite height degree b_A, then choose the source height schedule exponent eta_ht within its cumulative frequency allowance, before any external tail order",
        "source_status": "Completion, selected auxiliary mass, arbitrary smooth decay and height/profile propagation are imported analytic hypotheses, not certified here",
        "optional_global_sector": {
            "cutoff": "kappa1=m+(2/3)*d*r-1/750",
            "fresh_fixed_global_contour_offset_range": "0 < v <= 1/3500",
            "v_zero_arithmetic_endpoint": "Closure used only for finite arithmetic checks; the analytic contour requires v>0",
            "family_scope": "Nonprincipal inducing characters; the centered principal response needs its separate argument",
            "global_strip_squared_exponent": "delta_g(v)=3/4+2*v",
            "matching_direct_reflected_plain_squared_envelope": "delta_g(v)*min(x,kappa1-x)",
            "source_offset_extra_squared_norm_cost": "4*v*(kappa1-m), retained literally rather than hidden in epsilon",
            "conditional_inputs": "beta_star<=7/8, global Lemmas 4.9 and 4.10, functional equation, and primary-deleted Euler bounds on both fixed positive half-lines",
            "source_proof_status": "Additional conditional analytic inputs; no source proof or contour theorem is certified",
        },
    },
}


def check(condition, label):
    COUNTS[label] += 1
    if not condition:
        raise AssertionError(label)


def norm(a, primes):
    ans = 1
    for p, e in zip(primes, a):
        ans *= p ** e
    return ans


def ideals(cap, primes):
    ranges = []
    for p in primes:
        value, exponent = 1, 0
        while value * p <= cap:
            value *= p
            exponent += 1
        ranges.append(range(exponent + 1))
    return tuple(a for a in product(*ranges) if norm(a, primes) <= cap)


def plus(*factors):
    return tuple(sum(es) for es in zip(*factors))


def mu(a):
    return 0 if any(e > 1 for e in a) else (-1) ** sum(a)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(a, c):
    return c * a[0], c * a[1]


def mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] + a[1] * b[1]


def conj(a):
    return a[0] + a[1], -a[1]


def abs2(a):
    return a[0] ** 2 + a[0] * a[1] + a[1] ** 2


def total(values):
    ans = ZERO
    for value in values:
        ans = add(ans, value)
    return ans


def supported(t):
    return F(1, 2) <= t <= 2


def inv_profile(t):
    return (2 - t, F(1, 3) + t) if supported(t) else ZERO


def plain_profile(t):
    return (1 + t, 1 - t / 2) if supported(t) else ZERO


def put(mapping, key, value):
    mapping[key] = add(mapping.get(key, ZERO), value)


def eval_polynomial(coefficients, character):
    return total(mul(value, character(column)) for column, value in coefficients.items())


def local_character(local_values, column):
    value = ROOTS[sum((i + 1) * e for i, e in enumerate(column)) % 6]
    for local, exponent in zip(local_values, column):
        for _ in range(exponent):
            value = mul(value, local)
    return value


def centered_coefficients():
    primes = tuple(PARAMETERS["coefficient_prime_norms"])
    d, nscale, y1, y2, pslot = (F(PARAMETERS[key]) for key in ("D", "N", "Y1", "Y2", "slot_scale"))
    check(y1 * y2 == nscale ** 2, "equal_two_plain_product_scales")
    x = d * nscale ** 2 * pslot
    inv = {a: scale(inv_profile(F(norm(a, primes), d)), mu(a))
           for a in ideals(2 * d, primes) if mu(a) and inv_profile(F(norm(a, primes), d)) != ZERO}
    plain_candidates = ideals(2 * max(nscale, y1, y2), primes)
    slots = {tuple(int(p == q) for p in primes): (F(i + 1), F(1 - i))
             for i, q in enumerate(PARAMETERS["live_slot_prime_norms"])}
    original, comparison, centered = {}, {}, {}
    tuples = []
    for a, v1, v2, slot in product(inv, plain_candidates, plain_candidates, slots):
        na, nv1, nv2, ns = (norm(t, primes) for t in (a, v1, v2, slot))
        base = mul(plain_profile(F(nv1, nscale)), plain_profile(F(nv2, nscale)))
        shifted = mul(plain_profile(F(nv1, y1)), plain_profile(F(nv2, y2)))
        delta = add(base, scale(shifted, -1))
        if base == ZERO and shifted == ZERO:
            continue
        slot_value = slots[slot] if supported(F(ns, pslot)) else ZERO
        outer = mul(inv[a], slot_value)
        column = plus(a, v1, v2, slot)
        put(original, column, mul(outer, base))
        put(comparison, column, mul(outer, shifted))
        put(centered, column, mul(outer, delta))
        tuples.append((a, v1, v2, slot))
    for column in set(original) | set(comparison) | set(centered):
        check(centered.get(column, ZERO) == add(original.get(column, ZERO), scale(comparison.get(column, ZERO), -1)),
              "flattened_centered_original_coefficient_difference")

    extraction_records = []
    ownership = Counter()
    extraction_phase_zero_witnesses = 0
    for prime_index, prime in enumerate(primes):
        max_k = max(column[prime_index] for column in centered)
        for k in range(max_k + 1):
            extracted = {}
            branch_count = 0
            for e, f1, f2, s in product((0, 1), range(k + 1), range(k + 1), (0, 1)):
                if e + f1 + f2 + s != k:
                    continue
                dd = d / prime ** e
                n1, n2 = nscale / prime ** f1, nscale / prime ** f2
                yy1, yy2 = y1 / prime ** f1, y2 / prime ** f2
                ps = pslot / prime ** s
                check(yy1 * yy2 == n1 * n2, "prime_extraction_preserves_equal_product_scales_branchwise")
                check(dd * n1 * n2 * ps == x / prime ** k, "formal_residual_product_normalizer_keeps_all_ownership")
                residual_inverse = [a for a in ideals(2 * dd, primes) if not a[prime_index] and mu(a)]
                residual_v1 = [a for a in ideals(2 * max(n1, yy1), primes) if not a[prime_index]]
                residual_v2 = [a for a in ideals(2 * max(n2, yy2), primes) if not a[prime_index]]
                residual_slots = []
                for slot, coefficient in slots.items():
                    if slot[prime_index] == s:
                        child = tuple(v - (s if i == prime_index else 0) for i, v in enumerate(slot))
                        residual_slots.append((child, coefficient))
                branch_nonzero = False
                for a, v1, v2, slot_data in product(residual_inverse, residual_v1, residual_v2, residual_slots):
                    slot, slot_coefficient = slot_data
                    inverse_value = scale(inv_profile(F(norm(a, primes), dd)), (-1) ** e * mu(a))
                    base = mul(plain_profile(F(norm(v1, primes), n1)), plain_profile(F(norm(v2, primes), n2)))
                    shifted = mul(plain_profile(F(norm(v1, primes), yy1)), plain_profile(F(norm(v2, primes), yy2)))
                    slot_value = slot_coefficient if supported(F(norm(slot, primes), ps)) else ZERO
                    coefficient = mul(mul(inverse_value, add(base, scale(shifted, -1))), slot_value)
                    if coefficient == ZERO:
                        continue
                    put(extracted, plus(a, v1, v2, slot), coefficient)
                    branch_nonzero = True
                    ownership[(e, f1, f2, s)] += 1
                branch_count += branch_nonzero
            actual = {tuple(v - (k if i == prime_index else 0) for i, v in enumerate(column)): coefficient
                      for column, coefficient in centered.items() if column[prime_index] == k}
            for child in set(actual) | set(extracted):
                check(actual.get(child, ZERO) == extracted.get(child, ZERO), "exact_owned_prime_extraction_of_centered_coefficient")
                # Norm identity for the formal scalar P^(-k/2), without irrational arithmetic.
                coefficient = extracted.get(child, ZERO)
                check(abs2(coefficient) / x == F(1, prime ** k) * abs2(coefficient) / (x / prime ** k),
                      "prime_extraction_scalar_squared_and_original_normalizer")
                p_column = tuple(int(i == prime_index) for i in range(len(primes)))
                original_column = tuple(v + (k if i == prime_index else 0) for i, v in enumerate(child))
                for local_values in product((ZERO, ONE, ROOTS[1]), repeat=len(primes)):
                    p_phase = local_character(local_values, p_column)
                    extracted_phase = ONE
                    for _ in range(k):
                        extracted_phase = mul(extracted_phase, p_phase)
                    reconstructed = mul(extracted_phase, local_character(local_values, child))
                    check(local_character(local_values, original_column) == reconstructed,
                          "owned_prime_extraction_keeps_physical_character_power")
                    if k and p_phase == ZERO and coefficient != ZERO:
                        check(reconstructed == ZERO, "owned_prime_extraction_never_divides_a_physical_zero")
                        extraction_phase_zero_witnesses += 1
            extraction_records.append({"prime_norm": prime, "total_exponent": k,
                                       "nonzero_owned_branches": branch_count, "residual_columns": len(actual)})
    check(any(e == 1 for e, _, _, _ in ownership), "extraction_has_inverse_owned_prime")
    check(any(e == 0 for e, _, _, _ in ownership), "extraction_has_prime_absent_from_inverse")
    check(any(f1 > 1 or f2 > 1 for _, f1, f2, _ in ownership), "extraction_has_unrestricted_plain_prime_power")
    check(any(s == 1 for _, _, _, s in ownership), "extraction_has_separate_live_slot_ownership")

    original_mass = comparison_mass = centered_mass = F(0)
    cross = ZERO
    zeros = selected_rows = 0
    options = (ZERO,) + ROOTS
    for indices in product(range(len(options)), repeat=3):
        locals_ = tuple(options[i] for i in indices)
        chi = lambda column: local_character(locals_, column)
        full = eval_polynomial(original, chi)
        error = eval_polynomial(comparison, chi)
        difference = eval_polynomial(centered, chi)
        inverse_response = eval_polynomial(inv, chi)
        plain_n = total(mul(plain_profile(F(norm(v, primes), nscale)), chi(v)) for v in plain_candidates)
        plain_y1 = total(mul(plain_profile(F(norm(v, primes), y1)), chi(v)) for v in plain_candidates)
        plain_y2 = total(mul(plain_profile(F(norm(v, primes), y2)), chi(v)) for v in plain_candidates)
        slot_response = eval_polynomial(slots, chi)
        check(full == mul(mul(inverse_response, mul(plain_n, plain_n)), slot_response),
              "flattened_original_equals_product_of_original_responses")
        check(error == mul(mul(inverse_response, mul(plain_y1, plain_y2)), slot_response),
              "flattened_comparison_equals_equal_product_scale_responses")
        check(difference == add(full, scale(error, -1)), "whole_centered_marked_polynomial_identity_per_row")
        check(abs2(full) - abs2(difference) == 2 * mul(full, conj(error))[0] + mul(full, conj(error))[1] - abs2(error),
              "complete_centered_comparison_identity_per_row")
        for column, coefficient in centered.items():
            if coefficient != ZERO and any(e and locals_[i] == ZERO for i, e in enumerate(column)):
                check(chi(column) == ZERO, "centered_coefficient_preserves_physical_zero")
                zeros += 1
        weight = 0 if sum(indices) % 4 == 0 else 1 + sum(indices)
        selected_rows += weight > 0
        original_mass += weight * abs2(full)
        comparison_mass += weight * abs2(error)
        centered_mass += weight * abs2(difference)
        cross = add(cross, scale(mul(full, conj(error)), weight))
    check(original_mass - centered_mass == 2 * cross[0] + cross[1] - comparison_mass,
          "full_selected_centered_complete_comparison_identity")
    check(abs2(cross) <= original_mass * comparison_mass, "full_selected_centered_weighted_cauchy")
    difference = abs(original_mass - centered_mass)
    check(difference <= comparison_mass or (difference - comparison_mass) ** 2 <= 4 * original_mass * comparison_mass,
          "full_selected_centered_difference_bound")
    return {"inverse_ideals": len(inv), "retained_marked_tuples": len(tuples), "flattened_centered_columns": len(centered),
            "common_square_normalizer_X": str(x), "finite_rows": len(options) ** 3,
            "selected_rows": selected_rows, "physical_zero_witnesses": zeros,
            "prime_extraction_phase_zero_witnesses": extraction_phase_zero_witnesses,
            "owned_extraction_branches": [{"inverse": e, "plain_1": f1, "plain_2": f2,
                                            "live_slot": s, "tuples": count}
                                           for (e, f1, f2, s), count in sorted(ownership.items())],
            "extraction_records": extraction_records,
            "normalized_selected_moments": {"original": str(original_mass / x), "comparison": str(comparison_mass / x),
                                            "centered": str(centered_mass / x),
                                            "twice_real_full_error_cross": str((2 * cross[0] + cross[1]) / x)}}


def projector_checks():
    primes = tuple(PARAMETERS["projector_prime_weights"])
    u_radius = PARAMETERS["projector_U"]
    m, margin = F(PARAMETERS["projector_m"]), F(PARAMETERS["high_conductor_exponent_margin"])
    high_exponent = 2 * m - margin
    q_exponent = (1 - 2 * m + margin) / 6
    check(high_exponent == F(799, 1000) and q_exponent == F(67, 2000), "high_conductor_gated_q_support_exact_exponent")
    all_rows = ideals(u_radius, primes)
    columns = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
    coefficients = (ONE, (F(2), F(-1)), (F(-1), F(2)), (F(3), F(1)))

    def conductor(u):
        return norm(tuple(int(e % 6 != 0) for e in u), primes)

    def weight(u):
        nu, cu = norm(u, primes), conductor(u)
        radial = u_radius // 4 <= nu <= u_radius
        high = cu ** high_exponent.denominator > u_radius ** high_exponent.numerator
        return 1 + sum(u) if radial and high else 0

    def chi(u, column):
        if any(e and f for e, f in zip(u, column)):
            return ZERO
        return ROOTS[sum((e % 6) * column[(i + 1) % len(primes)] for i, e in enumerate(u)) % 6]

    def polynomial(u, q=None):
        return total(mul(c, chi(u, column)) for column, c in zip(columns, coefficients)
                     if q is None or not any(e and f for e, f in zip(q, column)))

    direct = signed = absolute = F(0)
    active_q = set()
    principal_gated = replaced_weight_differences = nontrivial_q = 0
    q_records = []
    signed_by_row = defaultdict(lambda: F(0))
    for u in all_rows:
        projector = sum(mu(q) for q in product(*(range(e // 6 + 1) for e in u)))
        check(projector == int(all(e < 6 for e in u)), "complete_sixthfree_physical_row_projector")
        if all(e < 6 for e in u):
            direct += weight(u) * abs2(polynomial(u))
    # Enumerate sixth-power divisors without a floating-point root cutoff.
    possible_q = product(*(range(max(row[i] for row in all_rows) // 6 + 1) for i in range(len(primes))))
    for q in possible_q:
        if not mu(q):
            continue
        nq = norm(q, primes)
        if nq ** 6 > u_radius:
            continue
        q_total = F(0)
        gated_v = 0
        for v in ideals(u_radius // nq ** 6, primes):
            u = tuple(6 * e + f for e, f in zip(q, v))
            check(conductor(u) == conductor(v), "sixthpower_row_multiplier_preserves_inducing_conductor")
            for column in columns:
                actual = chi(u, column)
                expected = chi(v, column) if not any(e and f for e, f in zip(q, column)) else ZERO
                check(actual == expected, "sixthpower_row_multiplier_retains_physical_column_mask")
            gated_weight = weight(u)
            if not gated_weight:
                continue
            gated_v += 1
            active_q.add(nq)
            nontrivial_q += nq > 1
            principal_gated += conductor(v) == 1
            replaced_weight_differences += gated_weight != weight(v)
            check(norm(v, primes) >= conductor(v), "physical_v_norm_dominates_inducing_conductor")
            check(nq ** (6 * high_exponent.denominator) < u_radius ** (high_exponent.denominator - high_exponent.numerator),
                  "every_gated_q_obeys_exact_high_conductor_support_bound")
            check(conductor(v) > 1, "absolute_gated_masks_exclude_principal_inducing_rows")
            term = gated_weight * abs2(polynomial(v, q))
            q_total += term
            signed_by_row[u] += mu(q) * term
        signed += mu(q) * q_total
        absolute += abs(mu(q)) * q_total
        q_records.append({"q_norm": nq, "gated_inducing_rows": gated_v, "unsigned_contribution": str(q_total)})
    check(direct == signed, "full_selected_sixthfree_signed_mask_aggregate_identity")
    check(all(value == (weight(u) * abs2(polynomial(u)) if all(e < 6 for e in u) else 0)
              for u, value in signed_by_row.items()), "signed_gated_mask_identity_holds_per_physical_row")
    check(nontrivial_q > 0, "gated_support_has_nontrivial_q_branch")
    check(principal_gated == 0, "no_principal_inducing_row_survives_any_absolute_gated_mask")
    check(replaced_weight_differences > 0, "full_selected_weight_cannot_be_replaced_by_weight_of_v")
    check(absolute > signed, "absolute_gated_masks_still_restore_high_conductor_repeated_rows")
    return {"formal_rows": len(all_rows), "high_conductor_exponent": str(high_exponent),
            "gated_q_exponent_upper": str(q_exponent), "active_q_norms": sorted(active_q),
            "nontrivial_q_gated_inducing_rows": nontrivial_q, "principal_gated_inducing_rows": principal_gated,
            "gated_weights_different_from_weight_of_v": replaced_weight_differences,
            "selected_sixthfree_moment": str(direct), "signed_gated_mask_sum": str(signed),
            "absolute_gated_mask_sum": str(absolute), "q_records": sorted(q_records, key=lambda record: record["q_norm"]),
            "scope": "The synthetic conductor depends on valuations modulo six. This is calibrated algebra, not a native primitive-conductor theorem."}


def exponent_ledger():
    box = PARAMETERS["exponent_ledger"]["closed_comparison_box"]
    ds, rs, ms = (tuple(F(v) for v in box[key]) for key in ("d", "r", "m"))
    target, cut_gap = F(1, 700), F(1, 1000)
    kappas, uniform_savings, comparison_margins = [], [], []
    for d, r, m in product(ds, rs, ms):
        kappa = m + d * r / 2 - cut_gap
        check(kappa >= F(1, 2), "adaptive_auxiliary_cutoff_at_least_one_half")
        check(kappa < 2 * m and kappa < 4 * m - F(1, 2), "adaptive_auxiliary_cutoff_within_two_completion_branches")
        center_exponent = 2 * kappa - 2 * m
        check(center_exponent == d * r - F(1, 500), "adaptive_auxiliary_mass_exact_gain")
        comparison_exponent = min(F(1, 4), kappa - F(1, 4)) + min(2 * m - F(1, 4), kappa - 2 * m + F(1, 4))
        check(comparison_exponent == kappa + F(1, 2) - 2 * m <= center_exponent,
              "two_plain_comparison_completion_fits_centered_auxiliary_exponent")
        kappas.append(kappa)
        comparison_margins.append(center_exponent - comparison_exponent)
        uniform = F(PARAMETERS["exponent_ledger"]["uniform_auxiliary_cutoff"])
        uniform_gain = d * r - (2 * uniform - 2 * m)
        check(uniform >= F(1, 2) and uniform < 2 * m and uniform < 4 * m - F(1, 2),
              "uniform_auxiliary_cutoff_within_two_completion_branches")
        check(uniform_gain >= F(1, 500), "uniform_auxiliary_cutoff_gain_at_least_one_five_hundredth")
        uniform_savings.append(uniform_gain)
    check(min(kappas) == F(21, 40), "adaptive_auxiliary_cutoff_exact_minimum")
    check(min(uniform_savings) == F(1, 500), "uniform_auxiliary_cutoff_exact_minimum_gain")
    check(min(comparison_margins) == F(1, 40), "adaptive_comparison_completion_minimum_spare_exponent")
    reserve = F(1, 500) - target
    check(reserve == F(1, 1750) > 0, "auxiliary_centered_exact_target_reserve_before_fixed_losses")
    decay_cutoff = F(PARAMETERS["exponent_ledger"]["optional_physical_decay_cutoff"])
    effective = (1 + 5 * decay_cutoff) / 6
    gap = min(ms) - effective
    check(decay_cutoff < (6 * min(ms) - 1) / 5 and gap == F(1, 120),
          "optional_physical_completion_decay_cutoff_exact_positive_gap")
    check(2 * min(ms) - F(1, 4) - effective > gap,
          "long_comparison_plain_response_has_larger_decay_gap")
    principal_effective = F(1, 6)
    principal_gap = F(1, 4) - principal_effective
    check(principal_gap == F(1, 12) > 0, "principal_completion_shortest_plain_length_gap")
    global_kappas, global_savings, global_extras = [], [], []
    global_v_max = F(1, 3500)
    for d, r, m, v in product(ds, rs, ms, (F(0), global_v_max)):
        kappa1 = m + F(2, 3) * d * r - F(1, 750)
        delta_g = F(3, 4) + 2 * v
        increment = 2 * delta_g * (kappa1 - m)
        extra = 4 * v * (kappa1 - m)
        check(kappa1 >= F(1, 2) and kappa1 < 2 * m and kappa1 < 4 * m - F(1, 2),
              "optional_global_cutoff_within_all_direct_reflected_branches")
        check(0 < kappa1 - m < F(1, 4), "optional_global_cutoff_excess_strictly_below_one_quarter")
        check(increment == d * r - F(1, 500) + extra,
              "optional_global_norm_increment_keeps_literal_fresh_contour_offset")
        check(extra <= v and (v == 0 or extra < v), "optional_global_literal_offset_cost_less_than_v")
        correction = delta_g * (min(F(1, 4), kappa1 - F(1, 4))
                                + min(2 * m - F(1, 4), kappa1 - 2 * m + F(1, 4)))
        check(correction == delta_g * (kappa1 + F(1, 2) - 2 * m) <= increment,
              "optional_global_correction_product_no_larger_than_original")
        saving = d * r - increment
        check(saving >= F(1, 500) - global_v_max == F(3, 1750),
              "optional_global_sector_guaranteed_saving_after_literal_offset")
        q_support = (1 - 2 * m + F(1, 1000)) / 6
        check(q_support <= F(67, 2000), "all_coarse_box_high_conductor_gate_q_exponents_at_most_67_2000")
        global_kappas.append(kappa1)
        global_savings.append(saving)
        global_extras.append(extra)
    check(min(global_kappas) == F(17, 30) and max(global_kappas) == F(9256, 15000),
          "optional_global_cutoff_exact_closed_box_range")
    global_reserve = F(3, 1750) - target
    check(global_reserve == F(1, 3500), "optional_global_guaranteed_reserve_vs_target")
    return {"adaptive_cutoff_range": [str(min(kappas)), str(max(kappas))],
            "adaptive_auxiliary_mass_gain": "1/500", "uniform_cutoff_minimum_gain": str(min(uniform_savings)),
            "comparison_completion_minimum_spare_exponent": str(min(comparison_margins)),
            "reserve_vs_1_700_before_fixed_losses": str(reserve),
            "optional_physical_decay_cutoff": str(decay_cutoff),
            "optional_effective_completion_radius_exponent": str(effective),
            "optional_plain_length_minimum_decay_gap": str(gap),
            "principal_Q_one_effective_radius_exponent": str(principal_effective),
            "principal_shortest_plain_length_gap": str(principal_gap),
            "optional_global_sector": {
                "cutoff_range": [str(min(global_kappas)), str(max(global_kappas))],
                "fresh_fixed_contour_v_upper": str(global_v_max),
                "delta_g_formula": "3/4+2*v",
                "literal_extra_norm_exponent": "4*v*(kappa1-m)",
                "largest_corner_literal_extra_at_v_upper": str(max(global_extras)),
                "guaranteed_saving_after_literal_v_cost": "3/1750",
                "guaranteed_reserve_vs_1_700": str(global_reserve),
                "minimum_corner_saving_sharper_than_uniform_guarantee": str(min(global_savings)),
                "global_fixed_height_and_other_loss_budget": "b_global*eta_ht+L_other < 1/3500",
                "high_conductor_gate_q_exponent_upper": "67/2000",
                "status": "Matching global direct/reflected envelopes and native conductor identification are additional imported assumptions; source proofs and evaluated height constants are not certified.",
            },
            "height_and_profile_budget": {"available_reserve": str(reserve),
                                          "required_strict_inequality": "b_A*eta_ht + L_other < 1/1750",
                                          "degree_status": "Finite b_A is not evaluated; principal and rapid estimates retain H^b_A",
                                          "quantifier_order": "For desired power L, fix internal A and b_A, then choose eta_ht within the source cumulative frequency allowance, before the external tail order",
                                          "instantiated": False},
            "scope": "Exact rational corner comparisons and affine monotonicity. Completion bounds, mass assumptions, decay and height/profile constants remain unproved analytic inputs."}


def run():
    centered = centered_coefficients()
    projectors = projector_checks()
    ledger = exponent_ledger()
    canonical = json.dumps(PARAMETERS, sort_keys=True, separators=(",", ":")).encode()
    return {"date": "2026-10-09", "author": "Prepared for Edward Baker with substantial LLM assistance",
            "model": "GPT-6 (Codex), inherited configuration", "reasoning_effort": "not exposed",
            "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "parameters_sha256": sha256(canonical).hexdigest(), "parameters": PARAMETERS,
            "assertions": sum(COUNTS.values()), "groups": dict(sorted(COUNTS.items())),
            "centered_coefficient_and_owned_prime_extraction": centered,
            "sixthfree_high_conductor_full_selected_projector": projectors,
            "conditional_exponent_and_height_budget": ledger,
            "limitations": [
                "Finite monoids, synthetic local characters, profile values and selectors do not certify native transfer or actual detector bins.",
                "Equal product scales, coefficient identities and weighted Cauchy do not prove analytic decay or any source moment estimate.",
                "The formal primitive conductor model is not a proof of the actual native conductor formula.",
                "A gated positive mask family excludes its synthetic principal inducing rows; its high-conductor repeated-row terms still require analytic estimates.",
                "No smooth Poisson decay, recursive child estimates, height/profile propagation, mixed fourth theorem or RH implication is established.",
            ]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
