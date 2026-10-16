#!/usr/bin/env python3
"""Exact finite truncated-Mobius bilinear checks; writes no files.

Prepared for Edward Baker with substantial LLM assistance, 9 October 2026.
Model: GPT-6 (Codex). Inherited reasoning effort is not exposed.
Finite good-prime monoids and local finite-field residue characters verify
algebra, normalization, zeros and rational budgets, not detector moments.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path

COUNTS = Counter()
NORMS = (7, 13, 19)
GENERATORS = (3, 2, 2)
ZERO, ONE = (0, 0), (1, 0)
ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def check(value, group):
    COUNTS[group] += 1
    assert value, group


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def scale(x, a):
    return x[0] * a, x[1] * a


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] + x[1] * y[1])


def conj(x):
    return x[0] + x[1], -x[1]


def norm2(x):
    return x[0] ** 2 + x[0] * x[1] + x[1] ** 2


def total(values):
    ans = ZERO
    for value in values:
        ans = add(ans, value)
    return ans


def ideal_norm(e):
    ans = 1
    for p, power in zip(NORMS, e):
        ans *= p ** power
    return ans


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def divides(a, b):
    return all(x <= y for x, y in zip(a, b))


def quotient(b, a):
    return tuple(y - x for x, y in zip(a, b))


def mu(e):
    return 0 if any(x > 1 for x in e) else (-1) ** sum(e)


def ideals_up_to(cap):
    limits = []
    for p in NORMS:
        power, value = 0, 1
        while value * p <= cap:
            power += 1
            value *= p
        limits.append(range(power + 1))
    return tuple(e for e in product(*limits) if ideal_norm(e) <= cap)


LOCAL = []
for p, generator in zip(NORMS, GENERATORS):
    values = {0: ZERO}
    for j in range(p - 1):
        residue = pow(generator, j, p)
        check(residue not in values, "native_local_generator_exact_order")
        values[residue] = ROOTS[j % 6]
    check(len(values) == p, "complete_native_local_character")
    LOCAL.append(values)


def psi(row, ideal, orientation):
    # A fixed multiplicative sixth-root ray phase is retained separately.
    value = ROOTS[sum((i + 1) * e for i, e in enumerate(ideal)) % 6]
    for local, residue, exponent in zip(LOCAL, row, ideal):
        if exponent:
            char = local[residue]
            if not orientation == 1:
                char = conj(char)
            for _ in range(exponent):
                value = mul(value, char)
    return value


def profile(n):
    # Complex finite profile values; not a physical smooth-profile assertion.
    if not 100 <= n <= 400:
        return ZERO
    return n + 1, (n % 11) - 5


def rec(x):
    return {"exact": str(x), "decimal": float(x)}


def endpoint_and_power_checks():
    records = []
    for cutoff in (7, 49, 343):
        small = ideals_up_to(cutoff)
        coefficients = Counter()
        for a in small:
            for b in small:
                coefficients[plus(a, b)] += mu(a) * mu(b)
        columns = ideals_up_to(cutoff ** 2)
        for n in columns:
            rhs = 2 * (mu(n) if ideal_norm(n) <= cutoff else 0)
            rhs -= sum(c for t, c in coefficients.items() if divides(t, n))
            check(rhs == mu(n), "inclusive_cutoff_endpoint_K2_identity")
        records.append({"Z": cutoff, "product_cap": cutoff ** 2,
                        "formal_columns": len(columns)})
    for prime_index in range(len(NORMS)):
        for exponent in range(7):
            n = tuple(exponent if i == prime_index else 0 for i in range(3))
            local_square = sum(mu(tuple(j if i == prime_index else 0
                                        for i in range(3)))
                               * mu(tuple(exponent - j if i == prime_index else 0
                                          for i in range(3)))
                               for j in range(exponent + 1))
            check(local_square == ((1, -2, 1)[exponent] if exponent < 3 else 0),
                  "untruncated_local_convolution_through_sixth_power")
            for orientation in (1, -1):
                row = tuple(0 if i == prime_index else 1 for i in range(3))
                check(psi(row, n, orientation) == (ONE if exponent == 0 else ZERO),
                      "canceled_sixth_power_still_punctures_physical_row")
    return records


def signed_projector_toy_checks():
    """Finite integer CRT congruence toy; does not certify sextic reciprocity.

    It checks the exact plus-congruence/sign and s|j support without using
    the source's global R factor, native lattice, masks or Poisson theorem.
    """
    moduli = (1, 7, 13, 91)

    def residue_character(n, modulus):
        value = ONE
        for p, local in zip(NORMS[:2], LOCAL[:2]):
            if modulus % p == 0:
                value = mul(value, local[n % p])
        return value

    def divisors_of_gcd(a, b):
        common_primes = tuple(p for p in NORMS[:2] if a % p == b % p == 0)
        ans = [(1, 1)]
        for p in common_primes:
            ans += [(p * s, -sign) for s, sign in tuple(ans)]
        return ans

    nonzero_support_witnesses = 0
    canceled_diagonal_columns = 0
    for a in moduli:
        for b in moduli:
            modulus = a * b
            plus_kernel, minus_kernel = [ZERO] * modulus, [ZERO] * modulus
            for x in range(a):
                for y in range(b):
                    value = mul(residue_character(x, a),
                                conj(residue_character(y, b)))
                    j_plus, j_minus = (b * x + a * y) % modulus, (b * x - a * y) % modulus
                    plus_kernel[j_plus] = add(plus_kernel[j_plus], value)
                    minus_kernel[j_minus] = add(minus_kernel[j_minus], value)
            labels = divisors_of_gcd(a, b)
            sign = conj(residue_character(-1, b))
            phi_a = sum(residue_character(x, a) != ZERO for x in range(a))
            check(minus_kernel[0] == (scale(ONE, phi_a) if a == b else ZERO),
                  "toy_minus_kernel_zero_diagonal")
            for j in range(modulus):
                check(plus_kernel[j] == mul(sign, minus_kernel[j]),
                      "toy_minus_h_conjugation_sign")
                projected = total(scale(plus_kernel[j], coefficient)
                                  for s, coefficient in labels)
                check(projected == (plus_kernel[j] if len(labels) == 1 else ZERO),
                      "toy_full_signed_coprimality_projector")
                for s, _ in labels:
                    if j and j % s:
                        check(plus_kernel[j] == ZERO,
                              "toy_nonzero_frequency_label_requires_s_divides_j")
                    elif j and s > 1 and plus_kernel[j] != ZERO:
                        nonzero_support_witnesses += 1
            if a == b > 1:
                check(plus_kernel[0] != ZERO
                      and total(scale(plus_kernel[0], sign) for _, sign in labels) == ZERO,
                      "toy_artificial_zero_diagonal_cancels_before_Cauchy")
                canceled_diagonal_columns += 1
    check(nonzero_support_witnesses > 0, "toy_divisor_frequency_support_nonempty")
    return {"moduli": list(moduli),
            "nonzero_supported_label_witnesses": nonzero_support_witnesses,
            "artificial_diagonal_columns_canceled": canceled_diagonal_columns,
            "scope": "integer CRT congruence/sign/projector toy; no native reciprocity or lattice proof"}


def run():
    endpoint_records = endpoint_and_power_checks()
    projector_record = signed_projector_toy_checks()
    Z, D, TYPE_I = 20, 200, 14
    columns = ideals_up_to(Z * Z)
    small = ideals_up_to(Z)
    cofactor = {}
    for t in columns:
        cofactor[t] = sum(mu(a) * mu(b)
                          for a in small for b in small if plus(a, b) == t)
    for n in columns:
        rhs = 2 * (mu(n) if ideal_norm(n) <= Z else 0)
        rhs -= sum(cofactor[t] for t in columns if divides(t, n))
        check(rhs == mu(n), "truncated_K2_all_ideals_including_higher_powers")
        if profile(ideal_norm(n)) != ZERO:
            check(ideal_norm(n) > Z, "short_Mobius_term_vanishes_on_original_annulus")
            check(-sum(cofactor[t] for t in columns if divides(t, n)) == mu(n),
                  "annular_coefficient_reconstruction")
        if ideal_norm(n) <= TYPE_I:
            expected = 1
            for e in n:
                expected *= (1, -2, 1)[e] if e <= 2 else 0
            check(cofactor[n] == expected, "small_cofactor_untruncated_Mobius_square")
    # A square of a prime above Z demonstrates why the product cap matters.
    n = (0, 0, 2)
    Z_failure = 10
    cut = ideals_up_to(Z_failure)
    rhs = 2 * (mu(n) if ideal_norm(n) <= Z_failure else 0)
    rhs -= sum(mu(a) * mu(b) for a in cut for b in cut
               if divides(plus(a, b), n))
    check(ideal_norm(n) > Z_failure ** 2 and rhs != mu(n),
          "identity_not_asserted_beyond_truncation_product_cap")

    orientation_records = []
    canceled_zero_witnesses = 0
    for orientation in (1, -1):
        FI = FT = FII = 0
        cross_full_small = ZERO
        for row in product(*(range(p) for p in NORMS)):
            phases = {n: psi(row, n, orientation) for n in columns}
            for n in columns:
                if any(e and residue == 0 for e, residue in zip(n, row)):
                    check(phases[n] == ZERO, "physical_zeros_retained_in_all_positive_powers")
                    canceled_zero_witnesses += 1
            original = total(scale(mul(phases[n], profile(ideal_norm(n))), mu(n))
                             for n in columns)
            short_terms, long_terms = [], []
            for t in columns:
                if not cofactor[t]:
                    continue
                inner = total(mul(phases[v], profile(ideal_norm(plus(t, v))))
                              for v in columns if ideal_norm(plus(t, v)) <= 400)
                term = scale(mul(phases[t], inner), -cofactor[t])
                (short_terms if ideal_norm(t) <= TYPE_I else long_terms).append(term)
            first, second = total(short_terms), total(long_terms)
            check(add(first, second) == original,
                  "bilinear_reconstruction_with_profiles_ray_phase_and_zeros")
            check(norm2(original) == norm2(first) + norm2(second)
                  + 2 * (mul(first, conj(second))[0]
                         + F(mul(first, conj(second))[1], 2)),
                  "pointwise_partition_keeps_cross_term")
            # Assemble a positive response weight before imposing a sharp selector.
            plain = total(phases[n] for n in columns if 15 <= ideal_norm(n) <= 100)
            slot = phases[(0, 1, 0)]
            weight = norm2(plain) ** 2 * norm2(slot)
            if (row[0] + 2 * row[1] + 3 * row[2]) % 5 == 0:
                weight = 0
            FT += weight * norm2(original)
            FI += weight * norm2(first)
            FII += weight * norm2(second)
            cross_full_small = add(cross_full_small,
                                   scale(mul(original, conj(first)), weight))
        real_twice = 2 * cross_full_small[0] + cross_full_small[1]
        check(FT - FII == real_twice - FI,
              "selected_weighted_difference_uses_full_small_cross")
        check(norm2(cross_full_small) <= FT * FI,
              "weighted_complex_Cauchy_for_the_actual_cross")
        check(F(FT, D) - F(FII, D) == F(real_twice - FI, D),
              "original_inverse_square_normalizer_retained")
        check(FI > 0 and FII > 0 and FT > 0,
              "both_bilinear_parts_and_selected_weight_nonzero")
        orientation_records.append({"orientation": orientation,
                                    "original_moment": str(F(FT, D)),
                                    "type_I_moment": str(F(FI, D)),
                                    "large_cofactor_moment": str(F(FII, D))})

    tau, d0, r0, r1 = F(1, 10), F(9, 25), F(7, 10), F(73, 100)
    emax, chi = F(1, 1200000), F(1, 700)
    unbuffered_gain = d0 * (2 * r0 - 1) - (1 + d0) * tau
    check(unbuffered_gain == F(1, 125), "uniform_type_I_gain")
    check(2 * r0 - 1 - tau == F(3, 10) > 0,
          "unbuffered_gain_increases_with_d")
    check(2 * d0 == F(18, 25) > 0, "unbuffered_gain_increases_with_r")
    # The joint cross exponent must be formed before maximizing r:
    # half of e(24-12r+12tau) plus half of 12er equals e(12+6tau).
    for r in (r0, r1):
        reflected = emax * (24 - 12 * r + 12 * tau)
        inverse = 12 * emax * r
        check((reflected + inverse) / 2 == (12 + 6 * tau) * emax,
              "literal_cross_buffer_cancels_r")
    type_I_gain = unbuffered_gain - emax * (24 - 12 * r0 + 12 * tau)
    error_gain = unbuffered_gain / 2 - (12 + 6 * tau) * emax
    check(type_I_gain == F(3993, 500000), "literal_type_I_gain")
    check(error_gain == F(7979, 2000000), "literal_difference_gain")
    check(type_I_gain > error_gain > chi, "difference_affordable_against_new_target")
    check(error_gain - chi == F(35853, 14000000), "difference_target_reserve")
    check(error_gain > F(1, 540), "difference_also_affordable_against_old_target")
    return {"model": "GPT-6 (Codex)",
            "reasoning_effort": "inherited configuration; not exposed",
            "author": "Prepared for Edward Baker with substantial LLM assistance",
            "scope": "finite coefficient/phase identities and rational budgets only",
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "assertions": sum(COUNTS.values()), "groups": dict(sorted(COUNTS.items())),
            "good_prime_norms": list(NORMS), "formal_columns": len(columns),
            "local_finite_field_CRT_rows_per_orientation": 7 * 13 * 19,
            "physical_zero_witnesses": canceled_zero_witnesses,
            "parameters": {"Z": Z, "D": D, "type_I_cut": TYPE_I},
            "endpoint_records": endpoint_records,
            "signed_projector_toy": projector_record,
            "rational_budget": {"unbuffered_type_I_gain": rec(unbuffered_gain),
                                "literal_buffer_type_I_gain": rec(type_I_gain),
                                "literal_buffer_difference_gain": rec(error_gain),
                                "difference_reserve_vs_1_700": rec(error_gain - chi),
                                "difference_reserve_vs_1_540": rec(error_gain - F(1, 540))},
            "orientation_records": orientation_records}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
