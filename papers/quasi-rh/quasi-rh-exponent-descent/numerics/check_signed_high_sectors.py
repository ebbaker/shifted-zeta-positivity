#!/usr/bin/env python3
"""Small exact audits of two controlled sectors and centered scale algebra.

Prepared for Edward Baker with substantial LLM assistance, 9 October 2026.
Model: GPT-6 (Codex), inherited configuration; effort not exposed.
Same-model finite internal audit, not a native analytic theorem.
Standard library only; deterministic JSON is written to stdout.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

COUNTS = Counter()
ZERO, ONE = (F(0), F(0)), (F(1), F(0))
ROOTS = (ONE, (F(0), F(1)), (F(-1), F(1)), (F(-1), F(0)),
         (F(0), F(-1)), (F(1), F(-1)))
PRIMES = (7, 13, 19)
PARAMETERS = {
    "date": "2026-10-09", "prime_norms": list(PRIMES),
    "coefficient_scales": {"D": 140, "N": 20, "Y1": 10, "Y2": 40, "slot": 10},
    "profiles": "same exact finite annular inverse/plain profiles as the centered-continuation checker, support[1/2,2]",
    "slot_primes": [7, 13],
    "finite_rows": "all triples of zero,1,omega; fixed multiplicative column ray retained",
    "selected_weight": "0 if index sum mod4 is zero, otherwise1+index sum",
    "kernel_scope": "One common synthetic selected weighted character kernel; not the native joint Poisson kernel or a high-conductor operator estimate",
    "exclusive_pair_cuts_B": [1, 7, 13, 49],
    "comparison_box": {"d": ["9/25", "21/50"], "r": ["7/10", "73/100"],
                       "m": ["2/5", "207/500"], "z": ["0", "2/45"]},
    "pair_cut_all_row_B_exponent": "d*r-1/500",
    "pair_cut_selected_B_exponent": "1+d*r-1/500-R",
    "selected_R_arithmetic_samples": ["0", "1/2", "1"],
    "squarefree_core_cutoff": "kappa_sf=1/2+(3*d/5-1/2)*r-z/2+9*m/10-3/2500",
    "weighted_defect_cutoff": "kappa_D=kappa_sf-3/200",
    "moving_weighted_defect_frontier": "kappa<=kappa_sf-eta/10, with0<=eta<=3/20",
    "moving_controlled_row_predicate": "Q*(Ndefect)^(1/10)<=U^kappa_sf and Ndefect<=U^(3/20)",
    "remaining_row_predicate": "Q>U^kappa1 and [Ndefect>U^(3/20) or Q*(Ndefect)^(1/10)>U^kappa_sf]",
    "moving_frontier_defect_samples": ["0", "3/80", "3/40", "9/80", "3/20"],
    "weighted_defect_definition": "lambda=sum(gamma_e,e2..5); theta=sum(e*gamma_e); eta=5*lambda-theta=sum((5-e)*gamma_e)",
    "defect_sector": "0<=eta<=3/20, kappa>=kappa1, physical kappa+4*lambda-eta<=1; kappa1=m+2*d*r/3-1/750",
    "fresh_fixed_global_contour_v_upper": "1/5000",
    "v_zero_arithmetic_endpoint": "Closure only; the analytic contour requires a fresh fixed v>0",
    "literal_global_center_cost": "4*v*(kappa-m), not hidden in epsilon",
    "operator_exponent": "1/6+kappa/6+5*(r+z)/6+eta/6",
    "height_budget": "Other fixed losses + finite b*eta_height <29/87500 for the inverse-sieve sector; <1/1750 for the exclusive-pair sector",
    "analytic_inputs": "Native transfer, fixed h/w column multipliers, sixth-order large sieve, marked coefficient norm, global direct/reflected plain bounds, and physical ideal counts are conditional analytic inputs, not certified here",
}


def check(condition, label):
    COUNTS[label] += 1
    if not condition:
        raise AssertionError(label)


def norm(a):
    ans = 1
    for p, e in zip(PRIMES, a):
        ans *= p ** e
    return ans


def ideals(cap):
    ranges = []
    for p in PRIMES:
        exponent, value = 0, 1
        while value * p <= cap:
            exponent += 1
            value *= p
        ranges.append(range(exponent + 1))
    return tuple(a for a in product(*ranges) if norm(a) <= cap)


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


def put(mapping, key, value):
    mapping[key] = add(mapping.get(key, ZERO), value)


def profile(t, inverse=False):
    if not F(1, 2) <= t <= 2:
        return ZERO
    return (2 - t, F(1, 3) + t) if inverse else (1 + t, 1 - t / 2)


def centered_maps():
    p = PARAMETERS["coefficient_scales"]
    d, nscale, y1, y2, slot_scale = (F(p[key]) for key in ("D", "N", "Y1", "Y2", "slot"))
    x = d * nscale ** 2 * slot_scale
    inverse = {a: scale(profile(F(norm(a), d), True), mu(a)) for a in ideals(2 * d)
               if mu(a) and profile(F(norm(a), d), True) != ZERO}
    plain = ideals(2 * max(nscale, y1, y2))
    slots = {tuple(int(q == prime) for prime in PRIMES): (F(i + 1), F(1 - i))
             for i, q in enumerate(PARAMETERS["slot_primes"])}
    original, comparison = {}, {}
    tuples = 0
    for a, v1, v2, slot in product(inverse, plain, plain, slots):
        base = mul(profile(F(norm(v1), nscale)), profile(F(norm(v2), nscale)))
        correction = mul(profile(F(norm(v1), y1)), profile(F(norm(v2), y2)))
        if base == correction == ZERO:
            continue
        tuples += 1
        check(all(e <= 2 for e in plus(a, slot)), "marked_inverse_slot_columns_have_valuation_at_most_two")
        outer = mul(inverse[a], slots[slot])
        column = plus(a, v1, v2, slot)
        put(original, column, mul(outer, base))
        put(comparison, column, mul(outer, correction))
    centered = {column: add(original.get(column, ZERO), scale(comparison.get(column, ZERO), -1))
                for column in set(original) | set(comparison)}
    return original, comparison, centered, x, tuples


def character(local_values, column):
    ans = ROOTS[sum((i + 1) * e for i, e in enumerate(column)) % 6]
    for local, exponent in zip(local_values, column):
        for _ in range(exponent):
            ans = mul(ans, local)
    return ans


def exclusive_decomposition(k, kp):
    c = tuple(e if e and f else 0 for e, f in zip(k, kp))
    d = tuple(f if e and f else 0 for e, f in zip(k, kp))
    a = tuple(e if not f else 0 for e, f in zip(k, kp))
    b = tuple(f if not e else 0 for e, f in zip(k, kp))
    return c, d, a, b


def pair_sector_checks():
    original, comparison, centered, x, tuples = centered_maps()
    columns = sorted(centered)
    rows = []
    physical_zeros = 0
    for indices in product(range(3), repeat=3):
        locals_ = tuple((ZERO, ONE, ROOTS[1])[i] for i in indices)
        phases = {k: character(locals_, k) for k in columns}
        for k, value in centered.items():
            if value != ZERO and any(e and locals_[i] == ZERO for i, e in enumerate(k)):
                check(phases[k] == ZERO, "actual_centered_column_keeps_physical_zero")
                physical_zeros += 1
        weight = 0 if sum(indices) % 4 == 0 else 1 + sum(indices)
        rows.append((weight, phases))
    row_mass = sum(weight for weight, _ in rows)
    kernel = {(k, kp): total(scale(mul(phases[k], conj(phases[kp])), weight)
                            for weight, phases in rows) for k, kp in product(columns, repeat=2)}
    decompositions = {}
    asym_common = differing_gcd = 0
    for k, kp in product(columns, repeat=2):
        c, d, a, b = exclusive_decomposition(k, kp)
        check(plus(c, a) == k and plus(d, b) == kp, "full_common_powers_reconstruct_both_columns")
        check(not any(e and f for e, f in zip(a, b)), "exclusive_residual_columns_are_coprime")
        check(not any((e + f) and (g + h) for e, f, g, h in zip(a, b, c, d)),
              "exclusive_residual_columns_avoid_both_full_common_parts")
        check(kernel[(kp, k)] == conj(kernel[(k, kp)]), "one_common_selected_kernel_has_reverse_conjugation")
        check(abs2(kernel[(k, kp)]) <= row_mass ** 2, "finite_selected_kernel_absolute_mass_bound")
        reverse = exclusive_decomposition(kp, k)
        check(reverse == (d, c, b, a), "exclusive_cut_decomposition_respects_pair_reversal")
        asym_common += any(e and f and e != f for e, f in zip(k, kp))
        gcd = tuple(min(e, f) for e, f in zip(k, kp))
        gcd_a = tuple(e - g for e, g in zip(k, gcd))
        gcd_b = tuple(f - g for f, g in zip(kp, gcd))
        differing_gcd += min(norm(a), norm(b)) != min(norm(gcd_a), norm(gcd_b))
        decompositions[(k, kp)] = (c, d, a, b)
    diagnostic = exclusive_decomposition((2, 1, 0), (1, 2, 0))
    check(diagnostic[2:] == ((0, 0, 0), (0, 0, 0)), "same_support_asymmetric_powers_have_unit_exclusive_parts")
    check(min(norm((1, 0, 0)), norm((0, 1, 0))) > 1,
          "ordinary_gcd_quotients_give_wrong_small_exclusive_cut")
    check(asym_common > 0 and differing_gcd > 0, "actual_centered_columns_exercise_asymmetric_common_ownership")

    def bilinear(left, right, predicate):
        return total(mul(mul(left.get(k, ZERO), conj(right.get(kp, ZERO))), kernel[(k, kp)])
                     for k, kp in product(columns, repeat=2) if predicate(k, kp))

    full = bilinear(centered, centered, lambda k, kp: True)
    direct = sum(weight * abs2(total(mul(centered[k], phases[k]) for k in columns)) for weight, phases in rows)
    check(full == (direct, F(0)), "full_centered_signed_pair_kernel_equals_selected_norm")
    records = []
    coefficient_bound = 1
    while any(abs2(value) > coefficient_bound ** 2 for value in centered.values()):
        coefficient_bound += 1
    for bound in PARAMETERS["exclusive_pair_cuts_B"]:
        predicate = lambda k, kp: min(norm(decompositions[(k, kp)][2]), norm(decompositions[(k, kp)][3])) <= bound
        complement = lambda k, kp: not predicate(k, kp)
        cut = bilinear(centered, centered, predicate)
        remainder = bilinear(centered, centered, complement)
        check(cut[1] == 0 and remainder[1] == 0, "symmetric_exclusive_sector_and_remainder_are_real")
        check(add(cut, remainder) == full, "exact_exclusive_sector_cut_reconstructs_complete_selected_cross_terms")
        four_rectangles = add(add(bilinear(original, original, predicate), bilinear(comparison, comparison, predicate)),
                              scale(add(bilinear(original, comparison, predicate), bilinear(comparison, original, predicate)), -1))
        check(four_rectangles == cut, "same_kernel_four_rectangle_centering_reconstructs_each_pair_sector")
        pair_count = sum(predicate(k, kp) for k, kp in product(columns, repeat=2))
        trivial_absolute_upper = F(row_mass * pair_count * coefficient_bound ** 2, x)
        check(abs2(scale(cut, 1 / x)) <= trivial_absolute_upper ** 2,
              "finite_absolute_pair_sector_bound_uses_complete_common_kernel")
        records.append({"B": bound, "ordered_pairs": pair_count, "sector": str(cut[0] / x),
                        "remainder": str(remainder[0] / x), "total": str(full[0] / x)})
    check(records[1]["ordered_pairs"] > records[0]["ordered_pairs"]
          and F(records[1]["sector"]) < F(records[0]["sector"]),
          "larger_pair_cut_can_reduce_signed_sector_despite_positive_complete_norm")
    return {"retained_marked_tuples": tuples, "centered_columns": len(columns), "finite_rows": len(rows),
            "selected_rows": sum(weight > 0 for weight, _ in rows), "selected_row_mass": row_mass,
            "physical_zero_witnesses": physical_zeros, "asymmetric_common_power_pairs": asym_common,
            "marked_inverse_slot_maximum_valuation": 2,
            "pairs_with_different_gcd_quotient_cut": differing_gcd, "cut_records": records,
            "signed_sector_is_not_monotone_in_pair_cut": True,
            "gcd_counterexample": {"k": "p^2*q", "k_prime": "p*q^2", "exclusive_parts": "1,1", "gcd_quotients": "p,q"},
            "scope": "Exact actual finite centered coefficient and one common synthetic weighted row kernel; the native pair-count theorem and signed high-conductor kernel estimate are not certified."}


def mellin_scale_checks():
    n, y1, y2 = F(20), F(10), F(40)
    ratio = y1 / n
    check(y1 * y2 == n ** 2, "Mellin_centering_equal_product_scales")
    unequal = []
    for t, w in product(range(1, 4), repeat=2):
        direct = n ** (t + w) - y1 ** t * y2 ** w
        linear = n ** (t + w) * (1 - ratio ** (t - w))
        reverse = n ** (t + w) - y1 ** w * y2 ** t
        symmetric = n ** (t + w) * (1 - (ratio ** (t - w) + ratio ** (w - t)) / 2)
        check(direct == linear, "exact_linear_centered_Mellin_scale_multiplier")
        check((direct + reverse) / 2 == symmetric, "exact_symmetric_centered_Mellin_scale_multiplier")
        check(t != w or direct == 0, "equal_exponents_cancel_exactly")
        if t != w:
            unequal.append(str(direct))
    check(any(F(value) != 0 for value in unequal), "unequal_exponents_do_not_cancel_automatically")
    n1, n2, yy1, yy2 = n / 7, n, y1 / 7, y2
    check(yy1 * yy2 == n1 * n2 and yy1 / n1 == ratio and yy2 / n2 == 1 / ratio,
          "owned_prime_extraction_preserves_relative_Mellin_scale_ratios")
    t, w = 1, 2
    actual_sym_child = ((n1 ** t * n2 ** w - yy1 ** t * yy2 ** w)
                        + (n1 ** w * n2 ** t - yy1 ** w * yy2 ** t)) / 2
    unjustified_replacement = n1 ** t * n2 ** w * (1 - (ratio ** (t - w) + ratio ** (w - t)) / 2)
    check(actual_sym_child != unjustified_replacement, "one_unequal_scale_child_cannot_use_balanced_quadratic_replacement")
    # Formal Taylor coefficients in z=t-w at h=1: 1-cosh(z).
    factorial = 1
    coefficients = []
    for order in range(5):
        if order:
            factorial *= order
        coefficient = F(0) if order == 0 or order % 2 else -F(1, factorial)
        coefficients.append(str(coefficient))
    check(coefficients == ["0", "0", "-1/2", "0", "-1/24"], "symmetric_Mellin_multiplier_has_quadratic_not_linear_zero")
    return {"linear_multiplier": "1-exp(-h*(t-w))", "symmetric_multiplier": "1-cosh(h*(t-w))",
            "quadratic_Taylor_coefficients_at_h_one": coefficients,
            "unequal_scale_child_counterexample": {"actual_symmetrized_scale_difference": str(actual_sym_child),
                                                   "invalid_balanced_replacement": str(unjustified_replacement)},
            "scope": "Diagnostic exact algebra. A quadratic zero does not prove frequency localization, contour movement or any power saving."}


def sector_ledgers():
    box = PARAMETERS["comparison_box"]
    ds, rs, ms, zs = (tuple(F(v) for v in box[key]) for key in ("d", "r", "m", "z"))
    target, v_max, eta_max = F(1, 700), F(1, 5000), F(3, 20)
    sf_cutoffs, defect_cutoffs, sf_minus_m, sf_lower_branch, sf_upper_branch, defect_improvements = [], [], [], [], [], []
    moving_frontiers = []
    moving_nominal_checks = moving_feasible_checks = 0
    moving_eta_samples = tuple(F(v) for v in PARAMETERS["moving_frontier_defect_samples"])
    for d, r, m, z in product(ds, rs, ms, zs):
        l = r + z
        b_all = d * r - F(1, 500)
        check(1 + b_all == 1 + d * r - F(1, 500), "all_row_exclusive_pair_cut_exact_target_exponent")
        check(b_all >= F(1, 4), "fixed_quarter_power_exclusive_cut_is_affordable")
        for R in (F(0), F(1, 2), F(1)):
            b_selected = 1 + d * r - F(1, 500) - R
            check(R + b_selected == 1 + d * r - F(1, 500), "selected_row_exclusive_pair_cut_keeps_literal_row_count")
        sf = F(1, 2) + (F(3, 5) * d - F(1, 2)) * r - z / 2 + F(9, 10) * m - F(3, 2500)
        defect = sf - F(3, 200)
        global_cut = m + F(2, 3) * d * r - F(1, 750)
        check(l / 2 < sf < l and sf > m, "squarefree_core_cutoff_within_dominant_sieve_branch")
        check(sf - m < F(3, 10), "squarefree_core_literal_global_cost_excess_below_three_tenths")
        operator = F(1, 6) + sf / 6 + 5 * l / 6
        nominal = operator + F(3, 2) * (sf - m)
        check(nominal == 1 + d * r - F(1, 500), "squarefree_core_marked_sieve_plus_center_exact_gain")
        for v in (F(0), v_max):
            extra = 4 * v * (sf - m)
            check(extra <= F(3, 12500), "squarefree_core_retains_literal_fresh_contour_cost")
            check(nominal + extra <= 1 + d * r - F(11, 6250), "squarefree_core_guaranteed_buffered_saving")
        sf_cutoffs.append(sf)
        defect_cutoffs.append(defect)
        sf_minus_m.append(sf - m)
        sf_lower_branch.append(sf - l / 2)
        sf_upper_branch.append(l - sf)
        defect_improvements.append(defect - global_cut)
        check(defect > global_cut and defect - global_cut > F(9, 250), "weighted_defect_cutoff_strictly_enlarges_global_sector")
        for kappa, eta in product((global_cut, defect), (F(0), eta_max)):
            lambda_lower = eta / 3
            lambda_upper = (1 - kappa + eta) / 4
            check(0 <= lambda_lower <= lambda_upper, "weighted_defect_feasible_radical_interval")
            for lam in (lambda_lower, lambda_upper):
                theta = 5 * lam - eta
                alpha = kappa - lam
                physical = kappa + 4 * lam - eta
                check(theta >= 2 * lam and physical <= 1, "weighted_defect_literal_physical_constraints")
                check(alpha >= (5 * kappa - 1 - eta) / 4 >= F(101, 240),
                      "weighted_defect_physical_constraint_forces_squarefree_row_radius")
                check(l / 2 < alpha < l, "weighted_defect_actual_Theta_row_radius_in_dominant_branch")
                theta_exponent = max(alpha, l, 5 * alpha / 6 + l / 3, alpha / 3 + 5 * l / 6)
                check(theta_exponent == alpha / 3 + 5 * l / 6,
                      "weighted_defect_sixth_sieve_dominant_term_is_on_actual_squarefree_radius")
                count_exponent = lam + (1 - kappa - theta + lam) / 6
                marked = count_exponent + theta_exponent
                check(marked == F(1, 6) + kappa / 6 + 5 * l / 6 + eta / 6,
                      "weighted_defect_h_and_sixthpower_counts_give_literal_eta_over_six")
                center_exponent = F(3, 2) * (kappa - m)
                check(marked + center_exponent <= 1 + d * r - F(1, 500),
                      "weighted_defect_cutoff_absorbs_eta_budget_nominally")
                extra = 4 * v_max * (kappa - m)
                check(0 <= extra <= F(3, 12500), "weighted_defect_keeps_literal_global_offset_cost")
                check(marked + center_exponent + extra <= 1 + d * r - F(11, 6250),
                      "weighted_defect_guaranteed_buffered_saving")
        for eta in moving_eta_samples:
            frontier = sf - eta / 10
            moving_frontiers.append(frontier)
            check(defect <= frontier <= sf and frontier > global_cut,
                  "moving_defect_frontier_contains_uniform_cutoff_and_extends_global_sector")
            check((eta != 0 or frontier == sf) and (eta != eta_max or frontier == defect),
                  "moving_defect_frontier_matches_squarefree_and_uniform_endpoints")
            frontier_nominal = F(1, 6) + frontier / 6 + 5 * l / 6 + eta / 6 + F(3, 2) * (frontier - m)
            check(frontier_nominal == 1 + d * r - F(1, 500),
                  "moving_defect_frontier_exactly_cancels_eta_nominal_cost")
            moving_nominal_checks += 1
            for kappa in (global_cut, frontier):
                lambda_lower, lambda_upper = eta / 3, (1 - kappa + eta) / 4
                check(0 <= lambda_lower <= lambda_upper,
                      "moving_defect_frontier_has_feasible_radical_endpoints")
                for lam in (lambda_lower, lambda_upper):
                    theta, alpha = 5 * lam - eta, kappa - lam
                    physical = kappa + 4 * lam - eta
                    check(theta >= 2 * lam and physical <= 1,
                          "moving_defect_frontier_keeps_literal_physical_constraints")
                    check(alpha >= (5 * kappa - 1 - eta) / 4 >= F(101, 240) and l / 2 < alpha < l,
                          "moving_defect_frontier_uses_actual_squarefree_Theta_radius_in_legal_branch")
                    theta_exponent = max(alpha, l, 5 * alpha / 6 + l / 3, alpha / 3 + 5 * l / 6)
                    check(theta_exponent == alpha / 3 + 5 * l / 6,
                          "moving_defect_frontier_preserves_dominant_Theta_term")
                    marked = lam + (1 - kappa - theta + lam) / 6 + theta_exponent
                    check(marked == F(1, 6) + kappa / 6 + 5 * l / 6 + eta / 6,
                          "moving_defect_frontier_retains_literal_eta_over_six_marked_cost")
                    nominal = marked + F(3, 2) * (kappa - m)
                    check(nominal <= frontier_nominal,
                          "all_rows_below_moving_frontier_fit_nominal_target_exponent")
                    extra = 4 * v_max * (kappa - m)
                    check(0 <= extra <= F(3, 12500)
                          and nominal + extra <= 1 + d * r - F(11, 6250),
                          "moving_defect_frontier_preserves_literal_contour_cost_and_target_reserve")
                    moving_feasible_checks += 1
            # The complete remaining predicate is the complement of the old
            # global sector together with the actual moving-frontier sector.
            for kappa in (global_cut, frontier, frontier + F(1, 10000)):
                global_controlled = kappa <= global_cut
                frontier_controlled = eta <= eta_max and kappa + eta / 10 <= sf
                residual = kappa > global_cut and (eta > eta_max or kappa + eta / 10 > sf)
                check(residual == (not (global_controlled or frontier_controlled)),
                      "remaining_predicate_is_exact_complement_of_global_and_moving_sectors")
        outside_eta = eta_max + F(1, 10000)
        for kappa in (global_cut, global_cut + F(1, 10000), sf - outside_eta / 10):
            global_controlled = kappa <= global_cut
            frontier_controlled = outside_eta <= eta_max and kappa + outside_eta / 10 <= sf
            residual = kappa > global_cut and (outside_eta > eta_max or kappa + outside_eta / 10 > sf)
            check(residual == (not (global_controlled or frontier_controlled)) == (kappa > global_cut),
                  "outside_defect_budget_keeps_exact_remaining_predicate_and_global_exception")
    check(min(sf_cutoffs) == F(141583, 225000) and max(sf_cutoffs) == F(3489, 5000), "squarefree_core_exact_cutoff_range")
    check(max(sf_minus_m) == F(713, 2500), "squarefree_core_exact_excess_upper")
    check(min(sf_lower_branch) == F(27229, 112500) and min(sf_upper_branch) == F(11, 5000),
          "squarefree_core_exact_dominant_branch_reserves")
    check(min(defect_cutoffs) == F(17276, 28125) and max(defect_cutoffs) == F(1707, 2500),
          "weighted_defect_exact_cutoff_range")
    check(min(defect_improvements) == F(2029, 56250), "weighted_defect_exact_improvement_over_global_cutoff")
    check(F(101, 240) - (max(rs) + max(zs)) / 2 == F(121, 3600),
          "weighted_defect_uniform_lower_Theta_branch_margin")
    check(F(11, 6250) - target == F(29, 87500), "inverse_sieve_exact_buffered_reserve_vs_target")
    check(F(1, 500) - target == F(1, 1750), "exclusive_pair_exact_reserve_vs_target")
    check(min(moving_frontiers) == min(defect_cutoffs) and max(moving_frontiers) == max(sf_cutoffs),
          "moving_frontier_exact_global_extrema_include_uniform_endpoint")
    # Multi-affine corner verification is continuous: each parameter separately
    # enters affinely in all cutoff/branch differences tested above. The local
    # Theta branch itself is compared by exact linear inequalities in alpha,l.
    return {"exclusive_pair_sector": {"all_row_B_exponent": "dr-1/500", "selected_B_exponent": "1+dr-1/500-R",
                                      "saving": "1/500", "reserve_vs_1_700": "1/1750", "fixed_B_exponent": "1/4"},
            "squarefree_core_sieve_sector": {"cutoff_range": [str(min(sf_cutoffs)), str(max(sf_cutoffs))],
                                            "actual_row_radius": "kappa, only for valuation-1 squarefree core",
                                            "kappa_minus_m_upper": str(max(sf_minus_m)),
                                            "lower_branch_margin": str(min(sf_lower_branch)), "upper_branch_margin": str(min(sf_upper_branch)),
                                            "nominal_saving": "1/500", "literal_offset_cost_upper": "3/12500",
                                            "buffered_saving": "11/6250", "reserve_vs_1_700": "29/87500"},
            "weighted_defect_extension": {"cutoff_range": [str(min(defect_cutoffs)), str(max(defect_cutoffs))],
                                          "eta_upper": "3/20", "actual_Theta_row_radius": "alpha=kappa-lambda",
                                          "uniform_alpha_lower": "101/240", "lower_branch_margin": "121/3600",
                                          "marked_mass_extra": "eta/6", "buffered_saving": "11/6250",
                                          "minimum_cutoff_improvement_over_kappa1": str(min(defect_improvements)),
                                          "scope": "Freeze higher-valuation h and sixthpower w; apply Theta to squarefree a1 at radiusU^alpha, never to all physical v at conductor radiusU^kappa."},
            "actual_moving_defect_frontier": {
                "formula": "kappa<=kappa_sf-eta/10, 0<=eta<=3/20",
                "frontier_range": [str(min(moving_frontiers)), str(max(moving_frontiers))],
                "tested_defects": [str(eta) for eta in moving_eta_samples],
                "exact_nominal_cancellation_cases": moving_nominal_checks,
                "feasible_radius_endpoint_cases": moving_feasible_checks,
                "uniform_kappa_D_role": "eta=3/20 endpoint and uniform quantitative corollary",
                "controlled_predicate": PARAMETERS["moving_controlled_row_predicate"],
                "remaining_predicate": PARAMETERS["remaining_row_predicate"],
                "nominal_saving": "1/500", "literal_contour_cost_upper": "3/12500",
                "buffered_saving": "11/6250", "reserve_vs_1_700": "29/87500",
                "actual_Theta_radius": "alpha=kappa-lambda, in[(r+z)/2,r+z] on the feasible high-conductor interval",
                "scope": "Endpoint bounds are continuous multi-affine/linear inequalities; interior defect samples independently exercise nominal cancellation and predicate boundaries. No analytic source estimate is certified.",
            },
            "continuous_arithmetic_scope": "Exact multi-affine corner bounds and linear feasible-defect endpoint inequalities; analytic counting, source envelopes and native transfer remain conditional.",
            "fixed_height_losses": PARAMETERS["height_budget"]}


def core_count_diagnostics():
    h_cap = 20
    squarefree_radicals = [b for b in ideals(h_cap) if mu(b)]
    actual = []
    for valuations in product((0, 2, 3, 4, 5), repeat=3):
        radical = tuple(int(e > 0) for e in valuations)
        if norm(radical) <= h_cap:
            actual.append(valuations)
    expected = sum(4 ** sum(b) for b in squarefree_radicals)
    check(len(actual) == expected == 13, "higher_valuation_h_count_keeps_all_four_prime_ownership_types")
    type_records = []
    gamma = F(1, 100)
    for e in (2, 3, 4, 5):
        lam, theta = gamma, e * gamma
        eta = 5 * lam - theta
        check(eta == (5 - e) * gamma and 0 <= eta <= 3 * lam, "weighted_defect_distinguishes_prime_valuations_two_through_five")
        type_records.append({"prime_valuation": e, "lambda": str(lam), "theta": str(theta), "eta": str(eta)})
    check(type_records[0]["eta"] == "3/100" and type_records[-1]["eta"] == "0",
          "valuation_two_and_five_have_different_defects_on_equal_radical")
    cases = ((1, 2, 5), (7, 8, 11), (6, 0, 5))
    records = []
    for u in cases:
        w = tuple(e // 6 for e in u)
        v = tuple(e % 6 for e in u)
        a1 = tuple(int(e == 1) for e in v)
        h = tuple(e if e >= 2 else 0 for e in v)
        check(tuple(6 * e + f for e, f in zip(w, plus(a1, h))) == u,
              "squarefree_a1_h_and_sixthpower_w_reconstruct_physical_row")
        check(not any(e and f for e, f in zip(a1, h)), "squarefree_a1_support_disjoint_from_h")
        records.append({"physical_valuations": list(u), "squarefree_a1": list(a1), "higher_valuation_h": list(h), "sixthpower_w": list(w)})
    return {"h_radical_cap": h_cap, "h_count": len(actual), "count_formula": "sum over squarefree b of4^omega(b)",
            "type_defects": type_records, "physical_decomposition_cases": records,
            "scope": "Finite ownership/count diagnostics; no ideal-count asymptotic or native conductor/operator transfer is proved."}


def run():
    pairs = pair_sector_checks()
    mellin = mellin_scale_checks()
    ledgers = sector_ledgers()
    cores = core_count_diagnostics()
    canonical = json.dumps(PARAMETERS, sort_keys=True, separators=(",", ":")).encode()
    return {"date": "2026-10-09", "author": "Prepared for Edward Baker with substantial LLM assistance",
            "model": "GPT-6 (Codex), inherited configuration", "reasoning_effort": "not exposed",
            "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "parameters_sha256": sha256(canonical).hexdigest(), "parameters": PARAMETERS,
            "assertions": sum(COUNTS.values()), "groups": dict(sorted(COUNTS.items())),
            "exclusive_full_column_pair_sectors": pairs, "centered_Mellin_scale_diagnostics": mellin,
            "sector_exponent_ledgers": ledgers, "squarefree_core_and_weighted_defect_diagnostics": cores,
            "limitations": [
                "The finite selected kernel is synthetic; it proves no native high-conductor signed correlation or Poisson estimate.",
                "Equal-product centering and its quadratic Mellin zero do not give frequency localization or a power saving by themselves.",
                "The squarefree radius in the sieve is alpha=kappa-lambda after freezingh,w; conductor ordering is not physical ordering.",
                "Native transfer, large sieve, counting, coefficient seminorms and global direct/reflected bounds remain conditional analytic inputs.",
                "All height degrees remain finite symbolic obligations; no detector schedule or full operational application is certified.",
                "Neither the surviving signed remainder nor a new RH implication is proved.",
            ]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
