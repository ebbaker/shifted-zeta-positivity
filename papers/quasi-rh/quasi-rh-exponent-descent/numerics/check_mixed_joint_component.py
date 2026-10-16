#!/usr/bin/env python3
"""Finite formal phases and rational budgets for the joint component cut.

Prepared for Edward Baker, 9 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured effort are not exposed and are not inferred. Standard library only.
Prints a small JSON record and writes no files. Native reciprocity, projected
conductor pair counting and asymptotic operator/moment inputs are not verified.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import lcm, prod
import json

counts = Counter()


def check(value, group):
    counts[group] += 1
    if not value:
        raise AssertionError(group)


# Exact integer arithmetic in Z[zeta_6], zeta_6^2 = zeta_6 - 1.
ZERO, ONE = (0, 0), (1, 0)
ROOTS = (ONE, (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0] + x[1]*y[1]


def conj(x):
    return x[0] + x[1], -x[1]


def scale(x, n):
    return n*x[0], n*x[1]


def total(xs):
    result = ZERO
    for x in xs:
        result = add(result, x)
    return result


def norm2(x):
    return x[0]**2 + x[0]*x[1] + x[1]**2


def power(x, j):
    result = ONE
    for _ in range(j):
        result = mul(result, x)
    return result


NORMS = (2, 3, 5, 7, 11)
PAIRING = ((0, 1, 2, 3, 4), (1, 0, 5, 2, 3), (2, 5, 0, 1, 4),
           (3, 2, 1, 0, 5), (4, 3, 4, 5, 0))


def ideal_norm(v):
    return prod(p**a for p, a in zip(NORMS, v))


def phase(row, column, orientation=1):
    if any(a and b for a, b in zip(row, column)):
        return ZERO
    exponent = sum(row[i]*PAIRING[i][j]*column[j]
                   for i in range(5) for j in range(5))
    return ROOTS[(orientation*exponent) % 6]


def unit_column(j, e=1):
    return tuple(e if i == j else 0 for i in range(5))


def plus(x, y):
    return tuple(a+b for a, b in zip(x, y))


def ratio(left, right, power_index=1):
    reduced = tuple((power_index*(a-b)) % 6 for a, b in zip(left, right))
    canceled = tuple(int((a or b) and not c)
                     for a, b, c in zip(left, right, reduced))
    return reduced, canceled


def mask(row, deletion):
    return int(not any(a and b for a, b in zip(row, deletion)))


def projected_conductors(left, right):
    delta = tuple((a-b) % 6 for a, b in zip(left, right))
    f2 = prod(p for p, e in zip(NORMS, delta) if e % 2)
    f3 = prod(p for p, e in zip(NORMS, delta) if e % 3)
    f6 = prod(p for p, e in zip(NORMS, delta) if e)
    return f2, f3, f6


unit = (0, 0, 0, 0, 0)
columns = (unit,) + tuple(unit_column(j, e) for j in range(5) for e in range(1, 7))
columns += ((0, 1, 1, 0, 0), (0, 2, 1, 0, 0), (0, 1, 2, 0, 0))
u, h, a = (1, 1, 0, 0, 0), (1, 0, 1, 0, 0), (1, 0, 0, 0, 0)
pq_blocks = ((unit_column(3), unit_column(4)),
             (unit_column(4), unit_column(3)))
middle_rows = tuple(plus(a, plus(p, tuple(2*x for x in q))) for p, q in pq_blocks)
test_rows = tuple(product(range(2), repeat=5)) + (u, h) + middle_rows
mask_witnesses = 0
projection_mask_witnesses = 0

for left in columns:
    for right in columns:
        f2, f3, f6 = projected_conductors(left, right)
        check(f6 == prod(p for p, x, y in zip(NORMS, left, right)
                        if (x-y) % 6), "full_ratio_conductor_support")
        reverse_f = projected_conductors(right, left)
        check((f2, f3, f6) == reverse_f, "projected_conductors_reversal_invariant")
        check(f6 == lcm(f2, f3), "full_ratio_is_lcm_of_projected_conductors")
        for j, expected_f in ((1, f6), (2, f3), (3, f2)):
            reduced, deletion = ratio(left, right, j)
            check(prod(p for p, e in zip(NORMS, reduced) if e) == expected_f,
                  "projected_component_conductor_identity")
            for row in test_rows:
                for orientation in (1, -1):
                    original = mul(phase(row, left, orientation),
                                   conj(phase(row, right, orientation)))
                    projected = scale(phase(row, reduced, orientation), mask(row, deletion))
                    check(power(original, j) == projected,
                          "zero_extended_projected_ratio_with_masks")
                if not mask(row, deletion) and phase(row, reduced) != ZERO:
                    if j == 1:
                        mask_witnesses += 1
                    else:
                        projection_mask_witnesses += 1
        for row in test_rows:
            original = mul(phase(row, left), conj(phase(row, right)))
            quadratic = power(original, 3)
            cubic = power(original, 2)
            check(original == mul(quadratic, conj(cubic)),
                  "full_phase_recovered_from_masked_projected_components")
check(mask_witnesses > 0, "nontrivial_canceled_full_phase_zero")
check(projection_mask_witnesses > 0, "nontrivial_canceled_projected_phase_zero")


def nu(column):
    return ROOTS[sum((i+1)*e for i, e in enumerate(column)) % 6]


def psi(row, column):
    return mul(nu(column), phase(row, column))


def mobius(column):
    return 0 if any(e > 1 for e in column) else (-1)**sum(column)


inverse_columns = tuple(product(range(2), repeat=5))
prime_columns = (unit_column(1), unit_column(2))
prime_coeff = (ROOTS[1], ROOTS[5])
D, N, prime_P = 25, 25, 9
weight_denominator = D*prime_P


def inverse_profile(column):
    n = ideal_norm(column)
    return (1+n % 3, n % 2) if 2 <= n <= 30 else ZERO


def plain_profile(column, seed):
    n = ideal_norm(column)
    if not 2 <= n <= 125:
        return ZERO
    return scale(ROOTS[(n+seed*(n % 7)) % 6], 1+n % 3)


def raw_weight(row):
    inverse = total(scale(mul(inverse_profile(d), psi(row, d)), mobius(d))
                    for d in inverse_columns)
    prime = total(mul(c, psi(row, p)) for c, p in zip(prime_coeff, prime_columns))
    return norm2(inverse)*norm2(prime)


# A coupled physical norm window is retained in the original selector.
# Both orders lie in one finite physical dyad; a further sharp condition is
# included to demonstrate that selectors stay on actual rows.
selected = {v: int(1000 <= ideal_norm(v) <= 2000 and v[3]+v[4] == 3)
            for v in middle_rows}
weights = {row: raw_weight(row) for row in (u, h)+middle_rows}
for p, q in pq_blocks:
    v = plus(a, plus(p, tuple(2*x for x in q)))
    check(ideal_norm(v) == ideal_norm(a)*ideal_norm(p)*ideal_norm(q)**2,
          "coupled_pq_squared_physical_norm")
    for k in columns:
        check(phase(v, k) == mul(phase(a, k), mul(phase(p, k), power(phase(q, k), 2))),
              "actual_pq_squared_kernel_factorization_with_zeros")
    direct_mq = total(scale(mul(inverse_profile(d), psi(v, d)), mobius(d))
                      for d in inverse_columns)
    direct_q = total(mul(c, psi(v, p0)) for c, p0 in zip(prime_coeff, prime_columns))
    expanded_mq = total(scale(mul(mul(inverse_profile(d), c), psi(v, plus(d, p0))),
                              mobius(d))
                        for d in inverse_columns for c, p0 in zip(prime_coeff, prime_columns))
    check(mul(direct_mq, direct_q) == expanded_mq,
          "actual_mobius_and_prime_weight_coefficient_expansion")
    check(norm2(expanded_mq) == weights[v], "actual_middle_weight_is_positive_square")
check(all(weights[row] > 0 for row in (u, h)+middle_rows),
      "actual_formal_endpoint_and_middle_weights_are_nonzero")

Z = ideal_norm(unit_column(3))*ideal_norm(unit_column(4))
equality_cap = Z**2*3
joint_caps = (Z**2, equality_cap, Z**2*5, Z**2*15)


def run_frame(seed):
    profiles = {k: plain_profile(k, seed) for k in columns}
    coefficients = {k: norm2(profiles[k]) for k in columns}
    s_raw = {row: total(mul(profiles[k], psi(row, k)) for k in columns) for row in (u, h)}

    def kernel_raw(left, right):
        return total(scale(mul(phase(left, k), conj(phase(right, k))), coefficients[k])
                     for k in columns)

    full = ZERO
    sectors = {cap: [ZERO, ZERO] for cap in joint_caps}
    removed_nonzero, retained_order6 = 0, 0
    for left, right in ((u, h), (h, u)):
        endpoint = scale(mul(conj(s_raw[left]), s_raw[right]), weights[left]*weights[right])
        direct_middle = total(scale(mul(kernel_raw(left, v), kernel_raw(v, right)),
                                    selected[v]*weights[v]) for v in middle_rows)
        expanded_middle = ZERO
        for k in columns:
            for kp in columns:
                f2, f3, f6 = projected_conductors(kp, k)
                reduced, deletion = ratio(kp, k)
                raw_inner = total(scale(mul(phase(v, kp), conj(phase(v, k))),
                                        selected[v]*weights[v]) for v in middle_rows)
                masked_inner = total(scale(phase(v, reduced),
                                           selected[v]*weights[v]*mask(v, deletion))
                                     for v in middle_rows)
                check(raw_inner == masked_inner,
                      "weighted_two_kernel_column_ratio_retains_all_masks")
                term = scale(mul(mul(phase(left, k), conj(phase(right, kp))), raw_inner),
                             coefficients[k]*coefficients[kp])
                expanded_middle = add(expanded_middle, term)
                chain_term = mul(endpoint, term)
                metric = Z**2*min(f2, f3)
                check(metric == Z**2*min(projected_conductors(k, kp)[:2]),
                      "joint_predicate_endpoint_column_reversal")
                for cap in joint_caps:
                    removed = metric <= cap
                    check(removed != (metric > cap), "exact_joint_cut_complement")
                    sectors[cap][int(not removed)] = add(sectors[cap][int(not removed)], chain_term)
                if k != kp and chain_term != ZERO:
                    removed_nonzero += metric <= equality_cap
                    retained_order6 += (metric > equality_cap
                                        and any((x-y) % 6 in (1, 5) for x, y in zip(kp, k)))
        check(direct_middle == expanded_middle, "actual_weighted_two_kernel_expansion")
        full = add(full, mul(endpoint, direct_middle))
    check(full[1] == 0, "full_coupled_endpoint_chain_is_real")
    for low, high in sectors.values():
        check(low[1] == 0 and high[1] == 0, "joint_components_are_real_by_reversal")
        check(add(low, high) == full, "joint_component_signed_exact_recombination")
    return full, sectors, removed_nonzero, retained_order6


# Try a bounded deterministic list of actual common profile phases; choose the
# first negative restricted-chain witness, if present. This is finite formal
# algebra, never a native selected-family asymptotic claim.
chosen = None
for seed in range(24):
    result = run_frame(seed)
    if chosen is None:
        chosen = (seed, result)
    if any(part[0] < 0 for pair in result[1].values() for part in pair):
        chosen = (seed, result)
        break
seed, (full, sectors, removed_nonzero, retained_order6) = chosen
check(removed_nonzero > 0, "nonzero_offdiagonal_joint_removed_terms")
check(retained_order6 > 0, "nonzero_full_order_six_joint_retained_terms")
equality_pairs = [(k, kp) for k in columns for kp in columns
                  if Z**2*min(projected_conductors(k, kp)[:2]) == equality_cap]
check(bool(equality_pairs), "joint_equality_is_on_removed_side")

# The actual finite high-component indicator on two distinct prime columns
# can destroy positivity of a Gram matrix.
filter_prime_columns = (unit_column(1), unit_column(2))
filter_matrix = tuple(tuple(int(Z**2*min(projected_conductors(k, kp)[:2])
                                > equality_cap)
                            for kp in filter_prime_columns)
                      for k in filter_prime_columns)
check(filter_matrix == ((0, 1), (1, 0)),
      "high_component_indicator_on_two_distinct_prime_columns")


def quadratic(matrix, vector):
    return sum(vector[i]*matrix[i][j]*vector[j]
               for i in range(len(vector)) for j in range(len(vector)))


check(quadratic(filter_matrix, (1, 1)) == 2, "high_component_filter_positive_direction")
check(quadratic(filter_matrix, (1, -1)) == -2, "high_component_filter_negative_direction")
check(filter_matrix[0][0] == filter_matrix[1][1] == 0 and filter_matrix[0][1] == 1,
      "two_prime_column_high_filter_has_zero_diagonal_nonzero_offdiagonal")

# Abstract aligned block frames show exact Schur-product norm saturation.
schur_records = []
for size, rblock, sblock, P, Qscalar in ((8, 2, 4, 3, 5), (12, 3, 6, 2, 7)):
    A = [[P if i//rblock == j//rblock else 0 for j in range(size)] for i in range(size)]
    B = [[Qscalar if i//sblock == j//sblock else 0 for j in range(size)] for i in range(size)]
    C = [[A[i][j]*B[i][j] for j in range(size)] for i in range(size)]
    check(rblock <= sblock and sblock % rblock == 0,
          "abstract_schur_block_partitions_are_nested")
    check(C == [[Qscalar*x for x in row] for row in A],
          "abstract_schur_product_equals_scalar_times_smaller_block")
    check(all(sum(row) == P*rblock for row in A), "abstract_A_all_ones_eigenvector")
    check(all(sum(row) == Qscalar*sblock for row in B), "abstract_B_all_ones_eigenvector")
    check(all(sum(row) == P*Qscalar*rblock for row in C),
          "abstract_schur_all_ones_eigenvector_saturates_norm")
    for vector in ((1,)*size, tuple((-1)**j for j in range(size))):
        check(quadratic(A, vector) == P*sum(sum(vector[i:i+rblock])**2
                                          for i in range(0, size, rblock)),
              "abstract_block_frame_positive_square_identity")
        check(quadratic(B, vector) == Qscalar*sum(sum(vector[i:i+sblock])**2
                                                for i in range(0, size, sblock)),
              "abstract_block_frame_positive_square_identity")
    schur_records.append({"size": size, "r": rblock, "s": sblock,
                          "norm_A": P*rblock, "norm_B": Qscalar*sblock,
                          "norm_schur": P*Qscalar*rblock})

# Exact continuous-envelope and illustrative source-point arithmetic.
cut = Q(142, 125)
cost = cut/2
uniform = 1-cost-Q(21, 50)*(1+Q(73, 100))/2 \
          +(2*Q(21, 50)-1)*Q(207, 500)-3*Q(101, 500000)
check(uniform == Q(927, 500000), "exact_uniform_joint_component_reserve")
check(uniform > 0, "uniform_joint_component_reserve_positive")
check(uniform > Q(19,12500), "old_error_reserve_remains_governing")
for dd, rr, mm in product((Q(9,25),Q(21,50)),
                          (Q(7,10),Q(73,100)),(Q(2,5),Q(207,500))):
    check(2*mm-(1+rr)/2 < 0 and 1-2*dd > 0,
          "continuous_uniform_envelope_derivative_signs")
for H in (1,2,4,8,16,32,64):
    cap = Q(64**2,H**2)
    check(H**2*cap == 64**2 and cap >= 1,
          "dyadic_count_product_cancels_radical_scale")
check(Q(64**2,128**2) < 1, "dyadic_cap_below_one_is_empty")
d = Q(9, 25)
r = Q(47752383, 67660000)
m = Q(54905017, 135320000)
z = Q(995377467, 6766000000)
s = Q(3, 15625)
g = d*(r+z)
mu = Q(12288947, 169150000000)
point = 1-cost-g+(2*d-1)*m-3*s+2*mu
check(point == Q(108685273, 9950000000), "exact_source_point_joint_component_reserve")
radical = Q(21, 50)
survivor_cap = cut-2*radical
check(survivor_cap == Q(37, 125), "survivor_projected_conductor_cap_point_296")
check(2*m > survivor_cap, "two_generic_prime_columns_remain_beyond_joint_component_cut")
check(2*radical+2*m > cut, "all_order_U_row_geometry_does_not_remove_all_column_pairs")

denominator = weight_denominator**3*N**3
negative_sector = any(part[0] < 0 for pair in sectors.values() for part in pair)
check(negative_sector, "restricted_joint_chain_has_exact_negative_witness")
record = {
    "title": "Finite joint projected-conductor component checks",
    "date": "2026-10-09", "author": "Prepared for Edward Baker",
    "model": "GPT-6 (Codex), inherited configuration",
    "effort": "Not exposed; not inferred",
    "llm_acknowledgement": "Substantial LLM assistance; same-model internal validation",
    "assertions": sum(counts.values()), "assertion_groups": dict(sorted(counts.items())),
    "formal_columns": len(columns), "formal_phase_rows": len(test_rows),
    "selected_coupled_middle_rows": sum(selected.values()),
    "common_profile_phase_seed": seed,
    "canceled_full_phase_witnesses": mask_witnesses,
    "canceled_projected_phase_witnesses": projection_mask_witnesses,
    "nonzero_offdiagonal_removed_terms": removed_nonzero,
    "nonzero_full_order_six_retained_terms": retained_order6,
    "joint_equality_pairs": len(equality_pairs),
    "negative_restricted_chain_witness": negative_sector,
    "full_chain": str(Q(full[0], denominator)),
    "joint_partitions": [{"cap": cap,
                          "removed": str(Q(parts[0][0], denominator)),
                          "retained": str(Q(parts[1][0], denominator))}
                         for cap, parts in sectors.items()],
    "high_component_filter_quadratic_forms": [2, -2],
    "abstract_schur_norm_saturation": schur_records,
    "uniform_reserve": str(uniform), "source_point_reserve": str(point),
    "survivor_component_cap": str(survivor_cap),
    "scope": "Formal cyclotomic phases, actual finite Mobius/prime weights, "
             "exact selectors/cuts and rational budgets only. No native reciprocity, "
             "projected pair count, source theorem or unbounded moment is certified.",
}

if __name__ == "__main__":
    print(json.dumps(record, sort_keys=True, indent=2))
