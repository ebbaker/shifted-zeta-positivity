#!/usr/bin/env python3
"""Exact finite checks for the squarefree saturated-cofactor decomposition.

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.

Standard library only. The six prime symbols have norms 7, 7, 13, 31, 37,
and 43: equal norm does not imply equality or divisibility. Original tail
coefficients are enumerated independently as ordered (a,b,m) assignments.
Complex phases are exact sixth roots in Z[omega], with deletion zeros.
Prints deterministic JSON and writes no files.

Finite algebra and rational budgets do not certify physical reciprocity,
conductor comparisons, Poisson completion, sieve inputs, ideal asymptotics,
or the open full squarefree signed moment.
"""

import itertools
import json
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache


PRIME_NORMS = (7, 7, 13, 31, 37, 43)
ALL = (1 << len(PRIME_NORMS)) - 1
ZERO = (0, 0)
ONE = (1, 0)
ROOTS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
counts = defaultdict(int)
witnesses = defaultdict(int)


def check(condition, group, detail=""):
    counts[group] += 1
    if not condition:
        raise AssertionError(detail or group)


def norm(mask):
    value = 1
    for index, pnorm in enumerate(PRIME_NORMS):
        if mask & (1 << index):
            value *= pnorm
    return value


def omega(mask):
    return mask.bit_count()


def mobius(mask):
    return (-1) ** omega(mask)


@lru_cache(None)
def divisors(mask):
    return tuple(d for d in range(ALL + 1) if d & mask == d)


@lru_cache(None)
def triples(mask):
    # This enumeration is independent of the low-prefix and parity formulas.
    indices = [i for i in range(len(PRIME_NORMS)) if mask & (1 << i)]
    result = []
    for assignments in itertools.product(range(3), repeat=len(indices)):
        factors = [0, 0, 0]
        for index, assignment in zip(indices, assignments):
            factors[assignment] |= 1 << index
        result.append(tuple(factors))
    return tuple(result)


@lru_cache(None)
def truncated_convolution(mask, z):
    # Direct ordered bipartitions of d=a*b; no divisor-prefix formula used.
    indices = [i for i in range(len(PRIME_NORMS)) if mask & (1 << i)]
    value = 0
    for assignments in itertools.product(range(2), repeat=len(indices)):
        a = sum(1 << i for i, slot in zip(indices, assignments) if slot == 0)
        b = mask ^ a
        if norm(a) <= z and norm(b) <= z:
            value += mobius(a) * mobius(b)
    return value


def original_tail_terms(mask, z, cutoff):
    return tuple((a, b, m, -mobius(a) * mobius(b))
                 for a, b, m in triples(mask)
                 if norm(a) <= z and norm(b) <= z
                 and norm(a) * norm(b) > cutoff)


def low_prefix(mask, cutoff):
    return mobius(mask) + sum((-2) ** omega(d) for d in divisors(mask)
                             if norm(d) <= cutoff)


def decomposition(mask, cutoff):
    if cutoff < 1:
        # The unit divisor is excluded; the saturated formula needs this case.
        return 0, mask, 0, 0, mobius(mask)
    small = sum(1 << i for i, pnorm in enumerate(PRIME_NORMS)
                if mask & (1 << i) and pnorm <= cutoff)
    rough = mask ^ small
    overflow = sum((-2) ** omega(d) for d in divisors(small)
                   if norm(d) > cutoff)
    parity = mobius(small) * (1 + mobius(rough))
    return small, rough, parity, overflow, parity - overflow


def saturated_even(mask, cutoff):
    if cutoff < 1:
        return 0
    small, rough, _, _, _ = decomposition(mask, cutoff)
    return 2 * mobius(small) if norm(small) <= cutoff and mobius(rough) == 1 else 0


def zmul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zscale(k, x):
    return (k * x[0], k * x[1])


def zsum(values):
    result = ZERO
    for value in values:
        result = zadd(result, value)
    return result


def phase(mask, prime_values):
    value = ONE
    for i, prime_value in enumerate(prime_values):
        if mask & (1 << i):
            value = zmul(value, prime_value)
    return value


# Equal-norm symbols enter a prime norm cutoff simultaneously, but remain
# distinct in ideals, triples, divisors, phases, and zero extensions.
check(norm(1) == norm(2) == 7 and 1 != 2, "equal_norm_symbols")
check(1 & 2 == 0 and divisors(1) != divisors(2), "equal_norm_symbols")
small_at_seven = decomposition(3, Fraction(7))[0]
check(small_at_seven == 3 and norm(small_at_seven) == 49,
      "equal_norm_symbols")

z_values = (7, 13, 31, 43, 100, 300, 588, 2000)
profile_cases = 0
cutoff_cases = 0
for z in z_values:
    for mask in range(1, ALL + 1):
        if not (z < norm(mask) <= z * z):
            continue
        profile_cases += 1
        check(sum(truncated_convolution(d, z) for d in divisors(mask))
              == -mobius(mask), "full_inverse_on_profile")
        thresholds = sorted({norm(d) for d in divisors(mask) if norm(d) <= z})
        cutoffs = {Fraction(0), Fraction(1, 2), Fraction(1), Fraction(z)}
        for threshold in thresholds:
            cutoffs.add(Fraction(threshold))
            if threshold > 1:
                cutoffs.add(Fraction(2 * threshold - 1, 2))
            if threshold + Fraction(1, 2) <= z:
                cutoffs.add(Fraction(2 * threshold + 1, 2))
        for cutoff in sorted(cutoffs):
            cutoff_cases += 1
            terms = original_tail_terms(mask, z, cutoff)
            original = sum(term[3] for term in terms)
            divisor_tail = -sum(truncated_convolution(d, z)
                                for d in divisors(mask) if norm(d) > cutoff)
            check(original == divisor_tail, "original_tuple_vs_divisor_tail")
            check(original == low_prefix(mask, cutoff), "original_tuple_vs_low_prefix")
            small, rough, parity, overflow, recombined = decomposition(mask, cutoff)
            check(original == recombined, "complete_parity_overflow_decomposition")
            check(small & rough == 0 and small | rough == mask,
                  "canonical_coprimality")
            if cutoff >= 1:
                check(all(PRIME_NORMS[i] <= cutoff
                          for i in range(len(PRIME_NORMS)) if small & (1 << i)),
                      "prime_cutoff_endpoints")
                check(all(PRIME_NORMS[i] > cutoff
                          for i in range(len(PRIME_NORMS)) if rough & (1 << i)),
                      "prime_cutoff_endpoints")
                small_prefix = sum((-2) ** omega(d) for d in divisors(small)
                                   if norm(d) <= cutoff)
                check(original == mobius(small) * mobius(rough) + small_prefix,
                      "small_prime_cofactor_inverse")
                if norm(small) <= cutoff:
                    check(overflow == 0, "saturated_overflow_empty")
                    check(original == mobius(small) * (1 + mobius(rough)),
                          "saturated_parity")
                    witnesses["saturated_odd" if omega(rough) % 2 else "saturated_even"] += 1
                    if omega(rough) % 2:
                        check(original == 0, "saturated_odd_zero")
                        if terms:
                            witnesses["nonempty_zero_tail"] += 1
                else:
                    check(saturated_even(mask, cutoff) == 0,
                          "unsaturated_retained_selector")
                    witnesses["unsaturated"] += 1
            else:
                check(original == mobius(mask), "unit_endpoint_below_one")

        # All threshold changes are fixed divisor-norm jumps. Test the actual
        # retained coefficients, not just a proposed upper envelope.
        previous_t = mobius(mask)
        previous_g = 0
        previous_h = mobius(mask)
        variation_t = variation_g = variation_h = 0
        t_jumps = []
        g_jumps = []
        h_jumps = []
        for index, threshold in enumerate(thresholds):
            current_t = sum(term[3] for term in original_tail_terms(mask, z, threshold))
            current_g = saturated_even(mask, threshold)
            current_h = current_t - current_g
            t_jumps.append(current_t - previous_t)
            g_jumps.append(current_g - previous_g)
            h_jumps.append(current_h - previous_h)
            variation_t += abs(t_jumps[-1])
            variation_g += abs(g_jumps[-1])
            variation_h += abs(h_jumps[-1])
            next_threshold = thresholds[index + 1] if index + 1 < len(thresholds) else z + 1
            if threshold < z:
                midpoint = min(Fraction(threshold + next_threshold, 2), Fraction(2 * z + 1, 2))
                if midpoint <= z:
                    check(low_prefix(mask, midpoint) == current_t,
                          "piecewise_constant_between_divisors")
                    check(saturated_even(mask, midpoint) == current_g,
                          "piecewise_constant_between_divisors")
            previous_t, previous_g, previous_h = current_t, current_g, current_h
        check(variation_t <= 3 ** omega(mask), "jump_variation_bounds")
        check(variation_g <= 8 * omega(mask) + 2, "jump_variation_bounds")
        check(variation_h <= 3 ** omega(mask) + 8 * omega(mask) + 2,
              "jump_variation_bounds")
        for jump_values, initial in ((t_jumps, mobius(mask)),
                                     (g_jumps, 0), (h_jumps, mobius(mask))):
            # At any binary partition level disjoint intervals obey the
            # variation-squared bound used before the physical operator.
            size = 1
            while size < len(jump_values):
                size *= 2
            padded = jump_values + [0] * (size - len(jump_values))
            width = 1
            total_variation = sum(abs(value) for value in padded)
            while width <= size:
                interval_sums = [sum(padded[left:left + width])
                                 for left in range(0, size, width)]
                check(sum(value * value for value in interval_sums)
                      <= total_variation ** 2, "binary_level_variation_bound")
                width *= 2
            check(initial + sum(jump_values)
                  == (previous_t if jump_values is t_jumps else
                      previous_g if jump_values is g_jumps else previous_h),
                  "jump_reconstruction")

# Off-profile algebra is checked separately so that r=1 and saturation at
# Y=N(s) are tested without falsely invoking the truncated inverse there.
for mask in range(ALL + 1):
    for cutoff in (Fraction(0), Fraction(1, 2), Fraction(1),
                   Fraction(7), Fraction(norm(mask)), Fraction(norm(mask) + 1)):
        small, rough, parity, overflow, recombined = decomposition(mask, cutoff)
        check(recombined == low_prefix(mask, cutoff), "off_profile_finite_identity")
        if cutoff >= norm(mask):
            check(rough == 0 and small == mask and overflow == 0,
                  "unit_rough_core_and_saturation_equality")
            check(recombined == 2 * mobius(mask),
                  "unit_rough_core_and_saturation_equality")

# A nonunit cofactor with three rough primes has nonempty signed tail
# channels, including both signs, which cancel at the common total ideal.
triple_mask = (1 << 0) | (1 << 3) | (1 << 4) | (1 << 5)
triple_z = 588
triple_y = Fraction(7)
triple_terms = original_tail_terms(triple_mask, triple_z, triple_y)
check(norm(triple_mask) == 345247 and triple_z < norm(triple_mask) <= triple_z ** 2,
      "nonunit_three_prime_witness")
check(len(triple_terms) > 0 and {term[3] for term in triple_terms} == {-1, 1},
      "nonunit_three_prime_witness")
check(sum(term[3] for term in triple_terms) == 0,
      "nonunit_three_prime_witness")
check(decomposition(triple_mask, triple_y)[:2] == (1, triple_mask ^ 1),
      "nonunit_three_prime_witness")
for rough_subset_size in (1, 2):
    for rough_indices in itertools.combinations((3, 4, 5), rough_subset_size):
        rough_divisor = sum(1 << i for i in rough_indices)
        for cofactor_divisor in (0, 1):
            d = rough_divisor | cofactor_divisor
            expected = (-2 if rough_subset_size == 1 else 2) * ((-2) ** omega(cofactor_divisor))
            check(truncated_convolution(d, triple_z) == expected,
                  "explicit_single_pair_compensation")
check(truncated_convolution(triple_mask, triple_z) == 0,
      "explicit_single_pair_compensation")

# A saturated even rough core survives, so the zero theorem cannot be
# broadened to every rough product or promoted to a full moment bound.
semiprime_mask = (1 << 3) | (1 << 4)
semiprime_z = 37
semiprime_y = Fraction(13)
check(semiprime_z < norm(semiprime_mask) <= semiprime_z ** 2,
      "surviving_semiprime")
check(sum(term[3] for term in original_tail_terms(semiprime_mask, semiprime_z, semiprime_y)) == 2,
      "surviving_semiprime")
check(decomposition(semiprime_mask, semiprime_y)[2:] == (2, 0, 2),
      "surviving_semiprime")

nu_values = tuple(ROOTS[i % 6] for i in range(len(PRIME_NORMS)))
row_values = (
    tuple(ROOTS[(i + 1) % 6] for i in range(len(PRIME_NORMS))),
    (ZERO, ROOTS[2], ROOTS[3], ROOTS[4], ROOTS[5], ROOTS[0]),
    (ROOTS[0], ROOTS[1], ZERO, ROOTS[3], ZERO, ROOTS[5]),
    (ROOTS[5], ZERO, ROOTS[1], ROOTS[2], ROOTS[3], ROOTS[4]),
)
phase_cases = 0
for rows in row_values:
    values = tuple(zmul(nu, row) for nu, row in zip(nu_values, rows))
    for mask, z, cutoff in ((triple_mask, triple_z, triple_y),
                            (semiprime_mask, semiprime_z, semiprime_y),
                            (ALL, 2000, Fraction(13))):
        terms = original_tail_terms(mask, z, cutoff)
        direct = zsum(zscale(sign, zmul(zmul(phase(a, values), phase(b, values)), phase(m, values)))
                      for a, b, m, sign in terms)
        coefficient = sum(term[3] for term in terms)
        check(direct == zscale(coefficient, phase(mask, values)),
              "complex_phases_and_deletion_zeros")
        for a, b, m, _ in terms:
            check(a & b == a & m == b & m == 0 and a | b | m == mask,
                  "actual_tuple_coprimality")
        phase_cases += 1

# Exact exponent budgets for the growing-cofactor three-prime sector.
h = Fraction(2, 5)
theta = Fraction(11, 20)
y_exponent = 1 - theta
beta = Fraction(1, 40)
eta = Fraction(1, 80)
large_conductor = Fraction(1, 8)
rough_prime = Fraction(13, 40)
main_row = h + eta
check(y_exponent == Fraction(9, 20), "rational_power_budgets")
check(main_row == Fraction(33, 80), "rational_power_budgets")
check(y_exponent - main_row == Fraction(3, 80) > beta,
      "rational_power_budgets")
check(y_exponent - large_conductor == rough_prime,
      "rational_power_budgets")
check(3 * rough_prime + beta == 1, "rational_power_budgets")
check((1 - beta) / 3 == rough_prime < Fraction(1, 2),
      "rational_power_budgets")
check(beta + Fraction(1, 3) < Fraction(1, 2),
      "rational_power_budgets")
check(2 * rough_prime > Fraction(1, 2), "rational_power_budgets")
check(h / 6 == Fraction(1, 15) < large_conductor,
      "rational_power_budgets")
check(y_exponent - h == Fraction(1, 20) > 0,
      "rational_power_budgets")
check(main_row - h == eta > 0, "rational_power_budgets")
operator_exponents = (h, 1 + h / 6, 5 * h / 6 + Fraction(1, 3),
                      h / 3 + Fraction(5, 6))
check(operator_exponents == (Fraction(2, 5), Fraction(16, 15),
                            Fraction(2, 3), Fraction(29, 30)),
      "rational_power_budgets")
check(max(operator_exponents) - Fraction(4, 5) == Fraction(4, 15),
      "rational_power_budgets")

print(json.dumps({
    "metadata": {
        "date": "2026-10-08",
        "prepared_for": "Edward Baker",
        "assistance": "Substantial LLM assistance",
        "model": "GPT-6 (Codex), inherited configuration",
        "exact_serving_variant": "not exposed; not inferred",
        "configured_reasoning_effort": "not exposed; not inferred",
        "validation_status": "internal finite algebra and rational checks only",
    },
    "prime_symbol_norms": PRIME_NORMS,
    "profile_cases": profile_cases,
    "cutoff_cases": cutoff_cases,
    "phase_cases": phase_cases,
    "nonunit_three_prime_witness": {
        "norm": norm(triple_mask), "z": triple_z, "Y": 7,
        "tail_tuples": len(triple_terms),
        "positive_tuples": sum(term[3] > 0 for term in triple_terms),
        "negative_tuples": sum(term[3] < 0 for term in triple_terms),
        "coefficient": sum(term[3] for term in triple_terms),
    },
    "assertions_by_group": dict(sorted(counts.items())),
    "assertions_total": sum(counts.values()),
    "witness_counts": dict(sorted(witnesses.items())),
    "limitations": [
        "The ideal model is a free multiplicative monoid, not a reciprocity certificate.",
        "Finite checks do not validate completion, sieve, conductor comparisons, or asymptotic counting.",
        "The surviving semiprime and unsaturated response are not controlled at exponent 4/5.",
        "The generic retained-sector bound keeps exponent 16/15 at H=D^(2/5).",
    ],
}, indent=2, sort_keys=True))
