#!/usr/bin/env python3
"""Exact finite square-part removals and exponent ledgers; writes no files.

Prepared for Edward Baker with substantial LLM assistance, 9 October 2026.
Model: GPT-6 (Codex); inherited reasoning effort is not exposed.
Formal good-prime monoids and finite residue characters check identities.
The rational pole maps below are not zeta zeros or analytic pole proofs.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

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


def gcd_ideal(a, b):
    return tuple(min(x, y) for x, y in zip(a, b))


def high_squarepart_selected_checks():
    z, threshold, gcut, normalizer = 20, 14, 10, 200
    columns = native.ideals_up_to(z * z)
    squarefree = tuple(a for a in native.ideals_up_to(z) if native.mu(a))
    cofactor, high_cofactor, low_cofactor = Counter(), Counter(), Counter()
    retained, high = [], []
    for a, b in product(squarefree, repeat=2):
        t = native.plus(a, b)
        nt = native.ideal_norm(t)
        if nt <= threshold:
            continue
        g = gcd_ideal(a, b)
        h = native.quotient(t, native.plus(g, g))
        check(all(e <= 1 for e in g + h), "both_squarepart_and_core_are_squarefree")
        check(all(not (x and y) for x, y in zip(g, h)),
              "squarepart_and_signed_core_are_coprime")
        check(native.plus(native.plus(g, g), h) == t,
              "literal_inverse_factor_gcd_gives_unique_squarepart")
        check(native.mu(a) * native.mu(b) == native.mu(h),
              "literal_two_mobius_factors_have_signed_core_weight")
        coefficient = native.mu(a) * native.mu(b)
        cofactor[t] += coefficient
        (high_cofactor if native.ideal_norm(g) >= gcut else low_cofactor)[t] += coefficient
        for ell in native.ideals_up_to(z * z // nt):
            n = native.plus(t, ell)
            if native.profile(native.ideal_norm(n)) == ZERO:
                continue
            term = (a, b, ell, t, n, -coefficient)
            retained.append(term)
            if native.ideal_norm(g) >= gcut:
                high.append(term)
    check(bool(high) and len(high) < len(retained), "both_high_squarepart_and_remainder_tuples_present")
    check(any(ell == UNIT for _, _, ell, *_ in high),
          "high_squarepart_keeps_short_plain_quotient")
    for t in columns:
        check(cofactor[t] == high_cofactor[t] + low_cofactor[t],
              "exact_large_cofactor_split_at_inclusive_gcd_threshold")
        if any(e > 2 for e in t):
            check(cofactor[t] == 0, "cofactor_valuation_above_two_vanishes")
            continue
        g, h = tuple(e // 2 for e in t), tuple(e % 2 for e in t)
        count = sum(1 for a0 in native.ideals_up_to(z) if native.divides(a0, h)
                    and native.ideal_norm(native.plus(g, a0)) <= z
                    and native.ideal_norm(native.plus(g, native.quotient(h, a0))) <= z)
        expected = native.mu(h) * count if native.ideal_norm(t) > threshold else 0
        check(cofactor[t] == expected, "squarepart_regrouping_retains_both_original_caps")
        check(high_cofactor[t] == (expected if native.ideal_norm(g) >= gcut else 0),
              "high_squarepart_regrouping_equals_literal_inverse_factor_gcd_filter")
    for index, p in enumerate(native.NORMS):
        a = tuple(1 if i == index else 0 for i in range(len(native.NORMS)))
        t = native.plus(a, a)
        if p <= z:
            check(native.ideal_norm(gcd_ideal(a, a)) == p,
                  "prime_square_gcd_threshold_exact_endpoint")
            check(native.ideal_norm(gcd_ideal(a, a)) >= p
                  and not native.ideal_norm(gcd_ideal(a, a)) >= p + 1,
                  "inclusive_gcd_cut_keeps_equality_only")
            check(native.ideal_norm(t) == p * p and native.mu(t) == 0,
                  "retained_squarepart_can_have_zero_original_mobius_coefficient")

    orientation_records, zero_witnesses = [], 0
    for orientation in (1, -1):
        full_moment = high_moment = residual_moment = 0
        full_high_cross = ZERO
        for row in product(*(range(p) for p in native.NORMS)):
            phases = {n: native.psi(row, n, orientation) for n in columns}
            mstar = native.total(native.scale(native.mul(phases[n], native.profile(native.ideal_norm(n))), c)
                                 for _, _, _, _, n, c in retained)
            hlarge = native.total(native.scale(native.mul(phases[n], native.profile(native.ideal_norm(n))), c)
                                  for _, _, _, _, n, c in high)
            residual = native.add(mstar, native.scale(hlarge, -1))
            regrouped = native.total(native.scale(native.mul(phases[n], native.profile(native.ideal_norm(n))),
                                                   -sum(c for t, c in high_cofactor.items() if native.divides(t, n)))
                                      for n in columns)
            check(hlarge == regrouped, "high_squarepart_original_profile_exact_regrouping")
            check(native.add(residual, hlarge) == mstar,
                  "large_cofactor_equals_high_squarepart_plus_residual")
            cross = native.mul(mstar, native.conj(hlarge))
            check(native.norm2(mstar) - native.norm2(residual)
                  == 2 * cross[0] + cross[1] - native.norm2(hlarge),
                  "pointwise_full_high_cross_controls_complete_squarepart_removal")
            for _, _, _, _, n, _ in high:
                if any(e and residue == 0 for e, residue in zip(n, row)):
                    check(phases[n] == ZERO,
                          "high_squarepart_preserves_every_physical_character_zero")
                    zero_witnesses += 1
            plain = native.total(phases[n] for n in columns if 15 <= native.ideal_norm(n) <= 100)
            weight = native.norm2(plain) ** 2 * native.norm2(phases[(0, 1, 0)])
            if (row[0] + 2 * row[1] + 3 * row[2]) % 5 == 0:
                weight = 0
            full_moment += weight * native.norm2(mstar)
            high_moment += weight * native.norm2(hlarge)
            residual_moment += weight * native.norm2(residual)
            full_high_cross = native.add(full_high_cross, native.scale(cross, weight))
        twice_real = 2 * full_high_cross[0] + full_high_cross[1]
        check(full_moment - residual_moment == twice_real - high_moment,
              "selected_weighted_full_high_cross_identity")
        check(native.norm2(full_high_cross) <= full_moment * high_moment,
              "selected_weighted_complex_cauchy_for_high_squarepart")
        check(F(full_moment - residual_moment, normalizer)
              == F(twice_real - high_moment, normalizer),
              "original_inverse_square_normalizer_survives_squarepart_removal")
        check(full_moment > 0 and high_moment > 0 and residual_moment > 0,
              "selected_large_cofactor_high_squarepart_and_residual_moments_nonzero")
        orientation_records.append({"orientation": orientation,
                                    "large_cofactor_moment": str(F(full_moment, normalizer)),
                                    "high_squarepart_moment": str(F(high_moment, normalizer)),
                                    "residual_moment": str(F(residual_moment, normalizer)),
                                    "twice_real_full_high_cross": str(F(twice_real, normalizer))})
    return {"Z": z, "strict_product_cut": threshold, "inclusive_squarepart_cut": gcut,
            "inverse_square_normalizer": normalizer, "retained_tuples": len(retained),
            "high_squarepart_tuples": len(high), "physical_zero_witnesses": zero_witnesses,
            "finite_CRT_rows_per_orientation": 7 * 13 * 19,
            "orientation_records": orientation_records,
            "scope": "exact formal ideal/finite character identities with original finite complex annular profile and selected positive weight"}


def rational_exponent_checks():
    d0, d1, r0, r1 = F(9, 25), F(21, 50), F(7, 10), F(73, 100)
    m0, m1, emax, target = F(2, 5), F(207, 500), F(1, 1200000), F(1, 700)
    gammas, cross_savings, smooth_deficits = [], [], []
    for d, r, e in product((d0, d1), (r0, r1), (F(0), emax)):
        gamma = (1 - d) * r / 2 + F(1, 250)
        alpha = r / 2 - F(1, 4)
        square_gain = d * r - (r - 2 * gamma)
        cross = square_gain / 2 - 6 * r * e
        check(square_gain == F(1, 125), "high_squarepart_exact_unbuffered_square_gain")
        check(cross == F(1, 250) - 6 * r * e,
              "high_squarepart_literal_cross_buffer")
        check(-6 * e <= 0 and -6 * r < 0,
              "squarepart_cross_saving_continuous_monotonicity_in_r_and_buffer")
        check(-r / 2 < 0 and (1 - d) / 2 > 0,
              "squarepart_cut_monotonicity_gives_continuous_endpoint_range")
        check(gamma < r / 2 and 2 * gamma > alpha,
              "squarepart_cut_inside_inverse_cap_and_above_product_cut")
        check(F(1, 125) > cross > target,
              "high_squarepart_square_and_cross_errors_fit_target")
        gammas.append(gamma)
        cross_savings.append(cross)
        for m in (m0, m1):
            ecrit, edelete = (r - alpha) / 2, r / 2 - F(1, 6)
            elow = F(1, 6) + r - alpha + 2 * m
            deficit = elow - (1 + d * r - target)
            check(ecrit - edelete == F(1, 6) - alpha / 2,
                  "principal_pole_vs_prime_deletion_exact_gap")
            check(ecrit - edelete >= F(131, 1200),
                  "principal_pole_vs_prime_deletion_uniform_gap")
            check(-F(1, 4) < 0,
                  "principal_pole_vs_prime_deletion_gap_decreases_with_r")
            check(deficit == (F(1, 2) - d) * r + 2 * m - F(7, 12) + target,
                  "smooth_principal_envelope_exact_exponent_deficit")
            check(F(1, 2) - d > 0 and -r < 0 and F(2) > 0,
                  "smooth_deficit_continuous_derivative_signs")
            check(deficit >= F(1439, 5250), "smooth_principal_envelope_uniform_deficit")
            smooth_deficits.append(deficit)
    check(min(gammas) == F(207, 1000) and max(gammas) == F(297, 1250),
          "literal_squarepart_cut_range")
    minimum = F(79927, 20000000)
    check(min(cross_savings) == minimum, "literal_high_squarepart_cross_minimum")
    check(minimum - target == F(359489, 140000000), "high_squarepart_target_reserve")
    prior = F(7979, 2000000)
    check(min(prior, minimum) == prior,
          "combined_cofactor_and_squarepart_removals_keep_prior_saving")
    check(min(smooth_deficits) == F(1439, 5250), "literal_smooth_envelope_deficit_minimum")
    return {"squarepart_cut": "gamma=(1-d)r/2+1/250",
            "gamma_range": [str(F(207, 1000)), str(F(297, 1250))],
            "unbuffered_square_gain": rec(F(1, 125)),
            "literal_high_squarepart_cross_minimum": rec(minimum),
            "high_squarepart_reserve_vs_1_700": rec(minimum - target),
            "combined_cofactor_and_squarepart_saving": rec(prior),
            "principal_pole_vs_deletion_uniform_gap": rec(F(131, 1200)),
            "smooth_envelope_exponent": "1/6+r-alpha+2m, alpha=r/2-1/4, J empty",
            "smooth_envelope_target_deficit_minimum": rec(F(1439, 5250)),
            "scope": "exact rational formulas and derivative signs; no analytic lower bound or moment estimate is inferred from this checker"}


def formal_pole_map_checks():
    examples = ((F(1, 2), F(1)), (F(3, 5), F(7, 3)), (F(7, 8), F(11, 5)))
    records = []
    for r, rho in product((F(7, 10), F(73, 100)), examples):
        alpha = r / 2 - F(1, 4)
        ratio = alpha / r
        real, imaginary = rho
        check(0 < ratio < 1, "formal_pole_map_is_strict_contraction")
        start = rho
        for iteration in range(1, 9):
            real, imaginary = 1 + ratio * (real - 1), ratio * imaginary
            check((real, imaginary) == (1 + ratio ** iteration * (start[0] - 1),
                                       ratio ** iteration * start[1]),
                  "formal_pole_iteration_exact_affine_formula")
            check(0 < imaginary < start[1], "formal_pole_map_keeps_nonreal_ordinate_and_reduces_it")
            s_real, s_imaginary = r / 2 + alpha * (real - 1), alpha * imaginary
            check((F(1, 2) + s_real / r, s_imaginary / r)
                  == (1 + ratio * (real - 1), ratio * imaginary),
                  "formal_mellin_pole_scaling_matches_affine_zero_map")
        records.append({"r": str(r), "ratio": str(ratio),
                        "formal_start": [str(v) for v in start],
                        "formal_eighth_iterate": [str(real), str(imaginary)]})
    return {"map": "rho -> 1+(alpha/r)(rho-1), alpha=r/2-1/4",
            "formal_examples": records,
            "scope": "formal rational complex numbers only; these points are not asserted to be zeta zeros, and no analytic continuation or pole noncancellation is checked"}


def sixthfree_projector_and_zero_checks():
    for u in product(range(13), repeat=len(native.NORMS)):
        projector = sum(native.mu(q) for q in product(*(range(e // 6 + 1) for e in u)))
        check(projector == int(all(e < 6 for e in u)),
              "complete_sixthfree_divisor_projector_including_higher_powers")
    columns = set(native.ideals_up_to(400))
    for index in range(len(native.NORMS)):
        for exponent in (1, 6, 7):
            columns.add(tuple(exponent if i == index else 0 for i in range(len(native.NORMS))))
    columns = sorted(columns)
    qvalues = tuple(product((0, 1), repeat=len(native.NORMS)))
    zero_witnesses = 0
    for q in qvalues:
        nq = native.ideal_norm(q)
        for row in product(*(range(p) for p in native.NORMS)):
            multiplied = tuple(residue * pow(nq, 6, p) % p for residue, p in zip(row, native.NORMS))
            for orientation, k in product((1, -1), columns):
                mask = not any(x and y for x, y in zip(k, q))
                expected = native.psi(row, k, orientation) if mask else ZERO
                actual = native.psi(multiplied, k, orientation)
                check(actual == expected,
                      "sixthpower_row_replacement_retains_fixed_column_ray_and_coprimality_zero_mask")
                if not mask:
                    check(actual == ZERO, "sixthpower_row_replacement_cannot_cancel_a_nonunit_zero")
                    zero_witnesses += 1
    return {"formal_projector_valuations": list(range(13)),
            "finite_q_masks": len(qvalues), "formal_columns": len(columns),
            "finite_CRT_rows": 7 * 13 * 19, "zero_witnesses": zero_witnesses,
            "scope": "formal ideal projector and finite sixth-order characters with the unchanged fixed multiplicative column ray phase; no native family transfer or analytic row projection bound"}


def run():
    split = high_squarepart_selected_checks()
    budgets = rational_exponent_checks()
    maps = formal_pole_map_checks()
    projectors = sixthfree_projector_and_zero_checks()
    dependency = Path(native.__file__)
    return {"date": "2026-10-09", "author": "Prepared for Edward Baker with substantial LLM assistance",
            "model": "GPT-6 (Codex)", "reasoning_effort": "inherited configuration; not exposed",
            "status": "finite squarepart/cofactor identities, zero masks, projectors and exact rational ledgers only",
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "dependency_sha256": {dependency.name: hashlib.sha256(dependency.read_bytes()).hexdigest()},
            "dependency_initialization_assertions": sum(native.COUNTS.values()),
            "assertions": sum(COUNTS.values()), "groups": dict(sorted(COUNTS.items())),
            "high_squarepart_selected_split": split, "rational_exponent_ledger": budgets,
            "formal_pole_scaling": maps, "sixthfree_projector_and_character_masks": projectors,
            "limitations": ["No analytic mixed moment, selected-bin population, or cancellation estimate is proved.",
                            "Finite complex profile values do not prove smooth-profile or derivative uniformity.",
                            "Formal rational pole maps neither locate zeta zeros nor prove Mellin continuation or pole noncancellation.",
                            "The smooth-envelope exponent comparison is not itself a principal-row asymptotic or analytic lower bound.",
                            "No native reciprocity, lattice Poisson, finite-ray transfer, or analytic sixthfree projection estimate is verified.",
                            "No zero-free strip, detector coverage, boundary reuse, or RH descent is established."]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
