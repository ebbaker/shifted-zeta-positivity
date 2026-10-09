#!/usr/bin/env python3
"""Separate finite algebra and rational audit of Note 25, sections 1--2.

Prepared for Edward Baker with substantial LLM assistance, 9 October 2026.
Model: GPT-6 (Codex), inherited configuration; serving variant and reasoning
effort are not exposed. This is same-model internal verification.

Standard library only. No files are written; JSON is sent to stdout.
Finite monoids and synthetic characters do not establish analytic estimates.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


PARAMETERS = {
    "prime_norms": [7, 13, 19],
    "inverse_cap_Z": 140,
    "inclusive_squarepart_cut_G": 7,
    "strict_product_cut_T": 14,
    "original_annulus_inclusive": [4900, 19600],
    "inverse_square_normalizer_D": 19600,
    "finite_local_character_values": ["zero", "1", "omega", "omega^2", "-1"],
    "finite_profile": "(1 + norm % 7) + ((norm % 5) - 2) * omega on the annulus",
    "synthetic_selected_weight": "0 if sum(local-value indices) mod 4 == 0; otherwise 1 + sum(indices)",
    "d_endpoints": ["9/25", "21/50"],
    "r_endpoints": ["7/10", "73/100"],
    "m_endpoints": ["2/5", "207/500"],
    "source_buffer_endpoints": ["0", "1/1200000"],
    "baseline_slot_envelope": "Gamma_J = 0, the optimistic deficit comparison",
    "target_saving": "1/700",
    "centered_comparison": {
        "scope": "Actual operational region only; enclosures are imported, not proved here",
        "operational_r_strict_lower": "70571698/100000000",
        "operational_m_strict_lower": "40398543/100000000",
        "operational_enclosures_imported_from": "papers/quasi-rh-exponent-descent/numerics/mixed_conductor_refinement_certificate_20261008.json",
        "imported_certificate_sha256_at_review": "83d7a10a3d2200d41414c14012b74fa45fcb72be8831534b88a00c37559b3df4",
        "imported_certificate_exact_r_lower": "33424168063/47362000000",
        "imported_certificate_exact_m_lower": "5191212484451/12849999000000",
        "slot_capacity_z_J_upper": "2/45",
        "centered_square_saving_formula": "lambda_center = d*(r+2*m-3/2)",
        "centered_square_source_cost_formula": "(30-24*m)*e",
        "original_full_source_cost_formula": "12*r*e",
        "centered_complete_cross_saving_formula": "lambda_center/2-(15-12*m+6*r)*e",
    },
}
COUNTS = Counter()
NORMS = tuple(PARAMETERS["prime_norms"])
UNIT = (0, 0, 0)
ZERO, ONE = (0, 0), (1, 0)
ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def check(condition, name):
    COUNTS[name] += 1
    if not condition:
        raise AssertionError(name)


def norm(a):
    result = 1
    for p, e in zip(NORMS, a):
        result *= p ** e
    return result


def ideals(cap):
    ranges = []
    for p in NORMS:
        bound, value = 0, 1
        while value * p <= cap:
            bound += 1
            value *= p
        ranges.append(range(bound + 1))
    return tuple(a for a in product(*ranges) if norm(a) <= cap)


def times(a, b):
    return tuple(x + y for x, y in zip(a, b))


def mobius(a):
    return 0 if any(e > 1 for e in a) else (-1) ** sum(a)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(a, c):
    return c * a[0], c * a[1]


def multiply(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def conjugate(a):
    return a[0] + a[1], -a[1]


def abs2(a):
    return a[0] ** 2 + a[0] * a[1] + a[1] ** 2


def sum_complex(values):
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


def character(local_values, a):
    # A fixed column ray factor is kept, including when another factor is zero.
    value = ROOTS[sum((i + 1) * e for i, e in enumerate(a)) % 6]
    for local, exponent in zip(local_values, a):
        for _ in range(exponent):
            value = multiply(value, local)
    return value


def profile(n):
    lower, upper = PARAMETERS["original_annulus_inclusive"]
    return (1 + n % 7, n % 5 - 2) if lower <= n <= upper else ZERO


def capped_core_count(h, cap):
    total = 0
    for a0 in product(*(range(e + 1) for e in h)):
        b0 = tuple(e - x for e, x in zip(h, a0))
        total += norm(a0) <= cap and norm(b0) <= cap
    return total


def finite_algebra():
    z = PARAMETERS["inverse_cap_Z"]
    gcut = PARAMETERS["inclusive_squarepart_cut_G"]
    threshold = PARAMETERS["strict_product_cut_T"]
    upper = PARAMETERS["original_annulus_inclusive"][1]
    squarefree = tuple(a for a in ideals(z) if mobius(a))
    direct, direct_high, cofactor = Counter(), Counter(), Counter()
    retained_tuples = nontrivial = two_nonunit_cores = 0
    witness = None
    for a, b in product(squarefree, repeat=2):
        t = times(a, b)
        if norm(t) <= threshold:
            continue
        g = tuple(min(x, y) for x, y in zip(a, b))
        h = tuple(e - 2 * f for e, f in zip(t, g))
        check(mobius(a) * mobius(b) == mobius(h), "signed_core_from_two_inverse_factors")
        cofactor[t] += mobius(a) * mobius(b)
        for ell in ideals(upper // norm(t)):
            n = times(t, ell)
            if profile(norm(n)) == ZERO:
                continue
            retained_tuples += 1
            coefficient = -mobius(a) * mobius(b)
            direct[n] += coefficient
            if norm(g) >= gcut:
                direct_high[n] += coefficient
            if norm(g) > 1 and norm(h) > 1:
                nontrivial += 1
            a0 = tuple(x - y for x, y in zip(a, g))
            b0 = tuple(x - y for x, y in zip(b, g))
            if norm(g) > 1 and norm(a0) > 1 and norm(b0) > 1:
                two_nonunit_cores += 1
                witness = {"a": norm(a), "b": norm(b), "g": norm(g),
                           "h": norm(h), "plain_quotient": norm(ell), "total_column": norm(n)}

    grouped, grouped_high = Counter(), Counter()
    for t in ideals(z * z):
        if any(e > 2 for e in t):
            check(cofactor[t] == 0, "valuation_above_two_has_zero_cofactor")
            continue
        g, h = tuple(e // 2 for e in t), tuple(e % 2 for e in t)
        expected = mobius(h) * capped_core_count(h, Q(z, norm(g))) if norm(t) > threshold else 0
        check(cofactor[t] == expected, "two_caps_squarepart_coefficient_identity")
        if expected:
            for ell in ideals(upper // norm(t)):
                n = times(t, ell)
                if profile(norm(n)) == ZERO:
                    continue
                grouped[n] -= expected
                if norm(g) >= gcut:
                    grouped_high[n] -= expected
    columns = ideals(upper)
    for n in columns:
        check(direct[n] == grouped[n], "whole_annulus_polynomial_coefficient_regrouping")
        check(direct_high[n] == grouped_high[n], "whole_annulus_high_squarepart_regrouping")
    check(nontrivial > 0 and two_nonunit_cores > 0, "explicit_nontrivial_squarepart_and_both_nonunit_core_factors")
    h = (0, 1, 1)
    cap_count = capped_core_count(h, 20)
    cap_product = capped_core_count((0, 1, 0), 20) * capped_core_count((0, 0, 1), 20)
    check(cap_count == 2 and cap_product == 4, "nonmultiplicative_capped_divisor_count_witness")

    local_options = (ZERO, ONE, ROOTS[1], ROOTS[2], ROOTS[3])
    fstar = fhigh = fresidual = 0
    cross = ZERO
    zero_witnesses = selected_rows = 0
    for indices in product(range(len(local_options)), repeat=3):
        local = tuple(local_options[i] for i in indices)
        phases = {n: character(local, n) for n in columns}
        full = sum_complex(scale(multiply(phases[n], profile(norm(n))), c) for n, c in direct.items())
        high = sum_complex(scale(multiply(phases[n], profile(norm(n))), c) for n, c in direct_high.items())
        residual = add(full, scale(high, -1))
        row_cross = multiply(full, conjugate(high))
        twice_real = 2 * row_cross[0] + row_cross[1]
        check(abs2(full) - abs2(residual) == twice_real - abs2(high), "complete_cross_identity_per_row")
        for n, c in direct_high.items():
            if c and any(e and local[i] == ZERO for i, e in enumerate(n)):
                check(phases[n] == ZERO, "physical_character_zeros_retained")
                zero_witnesses += 1
        weight = 0 if sum(indices) % 4 == 0 else 1 + sum(indices)
        selected_rows += weight > 0
        fstar += weight * abs2(full)
        fhigh += weight * abs2(high)
        fresidual += weight * abs2(residual)
        cross = add(cross, scale(row_cross, weight))
    twice_real = 2 * cross[0] + cross[1]
    check(fstar - fresidual == twice_real - fhigh, "positive_selected_weight_complete_cross_identity")
    check(abs2(cross) <= fstar * fhigh, "positive_selected_weight_complex_cauchy")
    # Exact squared comparison avoids approximating a square root.
    difference = abs(fstar - fresidual)
    check(difference <= fhigh or (difference - fhigh) ** 2 <= 4 * fstar * fhigh,
          "full_difference_bound_by_twice_cauchy_plus_high_square")
    check(fstar > 0 and fhigh > 0 and fresidual > 0, "nonzero_full_high_residual_moments")
    d = PARAMETERS["inverse_square_normalizer_D"]
    return {
        "squarefree_inverse_factors": len(squarefree), "retained_factor_quotient_tuples": retained_tuples,
        "nontrivial_squarepart_and_core_tuples": nontrivial,
        "both_nonunit_reduced_inverse_factors_tuples": two_nonunit_cores,
        "both_nonunit_reduced_factors_witness": witness,
        "capped_divisor_nonmultiplicativity": {"h": 247, "cap": 20, "d_cap_h": cap_count,
                                               "product_of_prime_counts": cap_product},
        "finite_rows": len(local_options) ** 3, "synthetic_selected_rows": selected_rows,
        "physical_zero_witnesses": zero_witnesses,
        "normalized_selected_moments": {"full": str(Q(fstar, d)), "high": str(Q(fhigh, d)),
                                        "residual": str(Q(fresidual, d)), "twice_real_full_high_cross": str(Q(twice_real, d))},
    }


def rational_ledger():
    ds, rs, ms = (Q(9, 25), Q(21, 50)), (Q(7, 10), Q(73, 100)), (Q(2, 5), Q(207, 500))
    es, target = (Q(0), Q(1, 1200000)), Q(1, 700)
    gammas, cross_savings, prior_savings, deficits = [], [], [], []
    for d, r, e in product(ds, rs, es):
        gamma = (1 - d) * r / 2 + Q(1, 250)
        alpha = r / 2 - Q(1, 4)
        square_gain = d * r - (r - 2 * gamma)
        cross = square_gain / 2 - 6 * r * e
        prior = (2 * r - 1) * (3 * d - 1) / 8 - (Q(21, 2) + 3 * r) * e
        check(square_gain == Q(1, 125), "exact_high_squarepart_square_saving")
        check(cross == Q(1, 250) - 6 * r * e, "exact_full_cross_source_buffer_saving")
        check(cross > target and gamma < r / 2 and 2 * gamma > alpha, "squarepart_cut_support_and_target_margin")
        gammas.append(gamma)
        cross_savings.append(cross)
        prior_savings.append(prior)
        for m in ms:
            endpoint = 2 * d * m + Q(5, 6) + r / 3
            deficit = endpoint - (1 + d * r - target)
            check(deficit == -Q(1, 6) + r * (Q(1, 3) - d) + 2 * d * m + target,
                  "legal_sieve_exact_endpoint_deficit")
            for y in (Q(0), alpha, Q(1, 2), r):
                theta = max(Q(1), y, Q(5, 6) + y / 3, Q(1, 3) + 5 * y / 6)
                check(theta == max(Q(1), Q(5, 6) + y / 3), "sixth_sieve_dominant_terms_on_breakpoints")
                check(2 * d * m + r - y + theta >= endpoint,
                      "short_quotient_endpoint_is_best_on_breakpoints")
            check(2 * m - r > 0 and 2 * d > 0, "sieve_deficit_monotonicity_in_d_and_m")
            deficits.append(deficit)
    check(-Q(1) < 0 and -Q(2, 3) < 0, "piecewise_affine_sieve_exponent_slopes_in_y")
    check(Q(1, 3) - ds[0] < 0, "sieve_deficit_slope_in_r_at_minimum_d")
    check(Q(1, 50) - 3 * es[1] > 0, "adaptive_cofactor_saving_increases_in_r")
    check(min(gammas) == Q(207, 1000) and max(gammas) == Q(297, 1250), "squarepart_cut_exact_extrema")
    check(min(cross_savings) == Q(79927, 20000000), "full_cross_exact_uniform_saving")
    check(min(cross_savings) - target == Q(359489, 140000000), "high_squarepart_exact_target_reserve")
    check(min(prior_savings) == Q(7979, 2000000), "adaptive_cofactor_exact_uniform_saving")
    combined = min(min(cross_savings), min(prior_savings))
    check(combined - target == Q(35853, 14000000), "combined_removal_exact_target_reserve")
    check(min(deficits) == Q(5423, 52500), "legal_sieve_exact_uniform_minimum_deficit")
    return {"gamma_range": [str(min(gammas)), str(max(gammas))],
            "high_squarepart_square_saving": "1/125", "full_cross_minimum_saving": str(min(cross_savings)),
            "full_cross_target_reserve": str(min(cross_savings) - target),
            "combined_removal_saving": str(combined), "combined_target_reserve": str(combined - target),
            "legal_sieve_minimum_deficit": str(min(deficits)),
            "legal_sieve_minimum_corner": {"d": "9/25", "m": "2/5", "r": "73/100", "Gamma_J": "0"},
            "continuous_scope": "Exact endpoint/breakpoint arithmetic with explicitly checked affine slopes; source and profile costs remain inherited assumptions."}


def centered_comparison_ledger():
    imported = PARAMETERS["centered_comparison"]
    r_lower, m_lower = Q(imported["operational_r_strict_lower"]), Q(imported["operational_m_strict_lower"])
    r_upper, d_lower, m_coarse_lower = Q(73, 100), Q(9, 25), Q(2, 5)
    e_upper, target, z_upper = Q(1, 1200000), Q(1, 700), Q(imported["slot_capacity_z_J_upper"])
    check(Q(imported["imported_certificate_exact_r_lower"]) > r_lower,
          "imported_exact_r_lower_exceeds_rounded_operational_lower")
    check(Q(imported["imported_certificate_exact_m_lower"]) > m_lower,
          "imported_exact_m_lower_exceeds_rounded_operational_lower")
    operational_bracket = r_lower + 2 * m_lower - Q(3, 2)
    check(operational_bracket > 0, "centered_square_saving_positive_on_imported_operational_region")
    lam = d_lower * operational_bracket
    check(lam == Q(769941, 156250000), "centered_square_exact_operational_saving_lower")
    square_cost_upper = 30 - 24 * m_coarse_lower
    cross_cost_upper = 15 - 12 * m_coarse_lower + 6 * r_upper
    check(cross_cost_upper == Q(729, 50), "centered_complete_cross_source_cost_upper")
    check(cross_cost_upper == (square_cost_upper + 12 * r_upper) / 2,
          "centered_complete_cross_cost_is_half_sum_of_full_and_error_costs")
    delta = lam / 2 - cross_cost_upper * e_upper
    square_saving = lam - square_cost_upper * e_upper
    check(delta == Q(6129153, 2500000000), "centered_complete_cross_exact_operational_saving_lower")
    check(square_saving > delta > target, "centered_error_square_and_complete_cross_fit_target")
    reserve = delta - target
    check(reserve == Q(17904071, 17500000000), "centered_complete_cross_exact_target_reserve")
    coarse_bracket = Q(7, 10) + 2 * m_coarse_lower - Q(3, 2)
    check(coarse_bracket == 0 and d_lower * coarse_bracket == 0,
          "coarse_box_centered_square_saving_lower_is_zero")
    first_capacity, fourth_capacity = r_upper + 2 * z_upper, 2 * r_upper + 8 * z_upper
    check(first_capacity == Q(737, 900) and first_capacity < 1,
          "centered_first_source_moment_capacity_arithmetic")
    check(fourth_capacity == Q(817, 450) and fourth_capacity < 3,
          "centered_fourth_source_moment_capacity_arithmetic")
    return {
        "operational_square_saving_lower": {"exact": str(lam), "decimal": float(lam)},
        "square_source_cost_upper": str(square_cost_upper),
        "complete_cross_source_cost_upper": str(cross_cost_upper),
        "operational_buffered_square_saving_lower": str(square_saving),
        "operational_complete_cross_saving_lower": {"exact": str(delta), "decimal": float(delta)},
        "complete_cross_reserve_vs_1_700": {"exact": str(reserve), "decimal": float(reserve)},
        "coarse_box_square_saving_lower": "0",
        "capacity_arithmetic": {"r_plus_2_z_J_upper": str(first_capacity),
                                "2_r_plus_8_z_J_upper": str(fourth_capacity)},
        "scope": "Arithmetic conditional on imported operational enclosures, slot capacity and stated source-cost formulas; no centered comparison or source moment theorem is certified.",
    }


def run():
    finite = finite_algebra()
    ledger = rational_ledger()
    centered = centered_comparison_ledger()
    canonical_parameters = json.dumps(PARAMETERS, sort_keys=True, separators=(",", ":")).encode()
    return {
        "date": "2026-10-09", "author": "Prepared for Edward Baker with substantial LLM assistance",
        "model": "GPT-6 (Codex), inherited configuration", "reasoning_effort": "not exposed",
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "parameters_sha256": sha256(canonical_parameters).hexdigest(), "parameters": PARAMETERS,
        "assertions": sum(COUNTS.values()), "groups": dict(sorted(COUNTS.items())),
        "finite_algebra_and_selected_cross": finite, "section_1_2_rational_ledger": ledger,
        "centered_comparison_arithmetic": centered,
        "limitations": [
            "The three-prime monoid is not the full good-ideal monoid of the field.",
            "Synthetic multiplicative characters and selected weights do not verify native transfer or actual detector-bin hypotheses.",
            "Finite profile values do not prove smooth-profile, derivative or height uniformity.",
            "The positive ideal count, selected fourth mass and large-sieve inputs are analytic assumptions, not certified here.",
            "The baseline slot comparison omits fixed positive profile/source/amplitude costs; those worsen the sieve deficit.",
            "Centered-comparison arithmetic imports the operational enclosures and source-cost formulas; it proves no source moment theorem, centered analytic comparison, or uniform profile bound.",
            "No analytic lower bound, principal-row Mellin obstruction, mixed fourth theorem, or RH implication is proved.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
