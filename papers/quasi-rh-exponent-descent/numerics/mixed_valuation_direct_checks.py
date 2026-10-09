"""Finite phase and budget checks for the inverse-weighted plain fourth target.

Prepared for Edward Baker, 9 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured effort are not exposed and are not inferred. Standard library only.
No native reciprocity, pair count, moment theorem or asymptotic is verified.
Importing this module neither runs checks nor prints anything.
"""

from collections import Counter
from itertools import product
from math import prod


def run_direct_checks(check, Q):
    """Run exact checks through check(bool, group); return a small JSON record."""
    groups = Counter()

    def verify(value, group):
        groups[group] += 1
        check(value, "direct_" + group)

    # Integer arithmetic in Z[zeta_6], zeta_6^2 = zeta_6 - 1.
    zero, one = (0, 0), (1, 0)
    roots = (one, (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))

    def add(x, y):
        return x[0] + y[0], x[1] + y[1]

    def mul(x, y):
        return (x[0] * y[0] - x[1] * y[1],
                x[0] * y[1] + x[1] * y[0] + x[1] * y[1])

    def conj(x):
        return x[0] + x[1], -x[1]

    def scale(x, n):
        return n * x[0], n * x[1]

    def total(xs):
        result = zero
        for x in xs:
            result = add(result, x)
        return result

    def norm2(x):
        return x[0] * x[0] + x[0] * x[1] + x[1] * x[1]

    # Distinct formal primes can have equal norm. These are formal phases,
    # rather than residue symbols or an arithmetic selected zero/profile bin.
    norms = (2, 2, 3)
    pairing = ((0, 1, 2), (1, 0, 5), (2, 5, 0))
    rows = tuple(product(range(6), repeat=3))
    columns = tuple(product(range(3), repeat=3))
    phase_rows = rows[::11]

    def ideal_norm(column):
        return prod(p ** a for p, a in zip(norms, column))

    def phase(row, column, orientation=1):
        if any(a and b for a, b in zip(row, column)):
            return zero
        exponent = sum(row[i] * pairing[i][j] * column[j]
                       for i in range(3) for j in range(3))
        return roots[(orientation * exponent) % 6]

    def ratio(left, right):
        reduced = tuple((a - b) % 6 for a, b in zip(left, right))
        canceled = tuple(int((a or b) and not c)
                         for a, b, c in zip(left, right, reduced))
        conductor = prod(p for p, c in zip(norms, reduced) if c)
        return reduced, canceled, conductor

    mask_witnesses = 0
    for left in columns:
        for right in columns:
            reduced, canceled, _ = ratio(left, right)
            for row in phase_rows:
                mask = int(not any(a and b for a, b in zip(row, canceled)))
                for orientation in (1, -1):
                    lhs = mul(phase(row, left, orientation),
                              conj(phase(row, right, orientation)))
                    rhs = scale(phase(row, reduced, orientation), mask)
                    verify(lhs == rhs, "zero_extended_inverse_ratio_identity")
                mask_witnesses += (not mask and phase(row, reduced) != zero)
    verify(mask_witnesses > 0, "canceled_phase_masks_are_nontrivial")

    def mobius(column):
        if any(a > 1 for a in column):
            return 0
        return (-1) ** sum(column)

    def fixed_nu(column):
        return roots[sum((j + 1) * a for j, a in enumerate(column)) % 6]

    def psi(row, column):
        return mul(fixed_nu(column), phase(row, column))

    def inverse_profile(column):
        n = ideal_norm(column)
        if not 2 <= n <= 12:
            return zero
        return scale(roots[n % 6], 1 + n % 3)

    def plain_profile(column):
        n = ideal_norm(column)
        return (1 + n % 4, n % 3 - 1)

    inverse_coeff = {
        column: scale(mul(fixed_nu(column), inverse_profile(column)),
                      mobius(column))
        for column in columns
    }
    for column in columns:
        if any(a > 1 for a in column):
            verify(inverse_coeff[column] == zero,
                   "nonsquarefree_inverse_coefficients_vanish")
    verify(any(c != zero for c in inverse_coeff.values()),
           "actual_mobius_inverse_is_nonzero")

    plain_columns = ((0, 0, 1), (2, 0, 0), (0, 2, 0), (1, 1, 0),
                     (1, 0, 1), (0, 1, 1), (1, 1, 1), (0, 0, 2),
                     (2, 1, 0))
    prime_columns = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    prime_coefficients = (one, roots[1], roots[5])
    inverse_D, plain_N, prime_P = 9, 9, 4
    weight_denominator = plain_N ** 2 * prime_P
    weight_raw = {}
    m_raw = {}
    selected = 0
    nonzero_weights = 0

    for row in rows:
        selector = int(row != (0, 0, 0) and ideal_norm(row) <= 64
                       and sum(row) % 3 != 1)
        selected += selector
        s_raw = total(mul(plain_profile(column), psi(row, column))
                      for column in plain_columns)
        q_raw = total(mul(coefficient, psi(row, column))
                      for coefficient, column in
                      zip(prime_coefficients, prime_columns))
        m_raw[row] = total(mul(coefficient, phase(row, column))
                           for column, coefficient in inverse_coeff.items())
        # V = selector |S|^4 |Q_J|^2; normalization is tracked globally,
        # so every cyclotomic ring pair stays integral throughout.
        weight_raw[row] = selector * norm2(s_raw) ** 2 * norm2(q_raw)
        verify(weight_raw[row] >= 0, "formal_plain_fourth_weight_is_positive")
        if not selector:
            verify(weight_raw[row] == 0, "selector_stays_in_plain_fourth_weight")
        nonzero_weights += bool(weight_raw[row])

    mass_raw = sum(weight_raw.values())
    verify(mass_raw > 0, "selected_plain_fourth_weight_is_nonzero")
    direct_raw = sum(weight_raw[row] * norm2(m_raw[row]) for row in rows)
    verify(direct_raw > 0, "selected_inverse_weighted_fourth_is_nonzero")
    direct_normalized = Q(direct_raw, inverse_D * weight_denominator)

    terms = {}
    mask_terms = 0
    for left in columns:
        for right in columns:
            reduced, canceled, conductor = ratio(left, right)
            kernel = total(scale(phase(row, reduced), weight_raw[row])
                           for row in rows
                           if not any(a and b for a, b in zip(row, canceled)))
            direct_kernel = total(
                scale(mul(phase(row, left), conj(phase(row, right))),
                      weight_raw[row]) for row in rows)
            verify(kernel == direct_kernel,
                   "actual_masked_positive_weight_kernel")
            verify(norm2(kernel) <= mass_raw ** 2,
                   "finite_kernel_modulus_bounded_by_positive_mass")
            coefficient = mul(inverse_coeff[left], conj(inverse_coeff[right]))
            terms[left, right] = (mul(coefficient, kernel), conductor)
            mask_terms += bool(any(canceled) and coefficient != zero
                               and kernel != zero)
    verify(mask_terms > 0, "nonzero_inverse_terms_retain_canceled_masks")
    expansion = total(term for term, _ in terms.values())
    verify(expansion == (direct_raw, 0),
           "actual_mobius_squared_expansion_equals_positive_moment")
    verify(Q(expansion[0], inverse_D * weight_denominator) == direct_normalized,
           "inverse_D_normalization_is_exact")

    partition_records = []
    low_offdiagonal_witnesses = 0
    for cap in (1, 2, 4, 12, 36, 144):
        low = total(term for term, conductor in terms.values()
                    if conductor <= cap)
        high = total(term for term, conductor in terms.values()
                     if conductor > cap)
        verify(low[1] == 0, "small_inverse_ratio_partition_is_real")
        verify(high[1] == 0, "large_inverse_ratio_partition_is_real")
        verify(add(low, high) == expansion,
               "inverse_ratio_partition_exact_recombination")
        for left in columns:
            for right in columns:
                term, conductor = terms[left, right]
                reverse, reverse_conductor = terms[right, left]
                verify(conductor == reverse_conductor,
                       "inverse_ratio_cut_is_reversal_invariant")
                verify(term == conj(reverse),
                       "inverse_pair_reversal_conjugates_actual_coefficients")
                low_offdiagonal_witnesses += bool(
                    cap == 4 and left != right and conductor <= cap and term != zero)
        partition_records.append({
            "cap": cap,
            "low": str(Q(low[0], inverse_D * weight_denominator)),
            "high": str(Q(high[0], inverse_D * weight_denominator)),
        })
    verify(low_offdiagonal_witnesses > 0,
           "small_inverse_ratio_sector_has_nonzero_offdiagonal_terms")

    # Exact illustrative source point and the actual whole-slot deficit.
    d = Q(9, 25)
    r = Q(47752383, 67660000)
    m = Q(54905017, 135320000)
    z = Q(995377467, 6766000000)
    s = Q(3, 15625)
    R = Q(58601, 84575) + Q(1, 1000000)
    g = d * (r + z)
    mu = max(Q(0), 1 - R - g)
    capacity = Q(2, 9) * (1 - 2 * m)
    D_J = 2 * d * m + d * capacity - g
    chi = max(Q(0), 2 * s - mu - D_J)
    reserve = d * r - chi - Q(1, 4)
    verify(capacity == Q(4251661, 101490000), "ideal_plain_fourth_slot_capacity")
    verify(chi == Q(177302, 1321484375), "ideal_inverse_weighted_fourth_deficit")
    verify(reserve == Q(166737511, 42287500000),
           "inverse_ratio_half_power_cap_exact_reserve")
    verify(reserve > 0, "inverse_ratio_half_power_cap_positive_reserve")

    shortfall_records = []
    sigma_ideal = max(mu, (D_J + mu) / 2)
    for shortfall in (Q(0), Q(1, 1000000), Q(1, 10000), Q(1, 1000)):
        actual_D_J = D_J - d * shortfall
        actual_chi = max(Q(0), 2 * s - mu - actual_D_J)
        actual_reserve = d * r - actual_chi - Q(1, 4)
        actual_sigma = max(mu, (actual_D_J + mu) / 2)
        verify(actual_chi == chi + d * shortfall,
               "actual_whole_slot_shortfall_increases_fourth_deficit")
        verify(actual_reserve == reserve - d * shortfall,
               "actual_whole_slot_shortfall_reduces_inverse_cut_reserve")
        verify(actual_sigma == max(mu, sigma_ideal - d * shortfall / 2),
               "actual_whole_slot_holders_envelope_keeps_mass_branch")
        verify(actual_reserve > 0, "sample_actual_whole_slot_caps_remain_safe")
        shortfall_records.append({
            "slot_shortfall": str(shortfall), "chi": str(actual_chi),
            "reserve": str(actual_reserve), "best_direct_saving": str(actual_sigma),
        })

    return {
        "assertions": sum(groups.values()),
        "assertion_groups": dict(sorted(groups.items())),
        "formal_rows": len(rows), "ratio_test_rows": len(phase_rows),
        "inverse_columns": len(columns), "selected_rows": selected,
        "nonzero_selected_weights": nonzero_weights,
        "canceled_mask_witnesses": mask_witnesses,
        "nonzero_masked_inverse_terms": mask_terms,
        "nonzero_low_offdiagonal_terms": low_offdiagonal_witnesses,
        "normalizations": {"inverse_D": inverse_D, "plain_N": plain_N,
                           "prime_P": prime_P},
        "positive_plain_fourth_mass": str(Q(mass_raw, weight_denominator)),
        "inverse_weighted_fourth": str(direct_normalized),
        "inverse_ratio_partitions": partition_records,
        "ideal_cap_reserve": str(reserve),
        "actual_whole_slot_samples": shortfall_records,
        "scope": "Finite formal phases, Mobius coefficients and rational budgets; "
                 "no native reciprocity, pair count or asymptotic moment is verified.",
    }
