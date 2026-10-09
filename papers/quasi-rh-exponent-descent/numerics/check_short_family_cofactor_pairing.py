#!/usr/bin/env python3
"""Exact finite checks for notes 24--25, 8 October 2026.

Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

This free ideal monoid keeps equal-norm primes distinct. It compares the
original truncated tuple coefficients with complete cofactor pairing,
cyclotomic dilation filters, Euler Jacobians and translated formal moments.
Rational budgets are finite checks, not PNT, Taylor remainder, lattice
asymptotic, physical reciprocity or an unbounded moment verification.
Standard library only; deterministic JSON on stdout; writes no files.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb, isqrt, prod
import json


counts = Counter()
NORMS = (7, 7, 13, 1009, 1033)
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def check(group, value):
    counts[group] += 1
    if not value:
        raise AssertionError(group)


def norm(mask):
    return prod(n for i, n in enumerate(NORMS) if mask & (1 << i))


def mu(mask):
    return (-1) ** mask.bit_count()


def divisors(mask):
    return [d for d in range(1 << len(NORMS)) if d & mask == d]


def cm(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c + b * d)


def ca(x, y):
    return (x[0] + y[0], x[1] + y[1])


def cs(x, scale):
    return (x[0] * scale, x[1] * scale)


def csum(values):
    result = ZERO
    for value in values:
        result = ca(result, value)
    return result


def phase(mask, values):
    result = ONE
    for i, value in enumerate(values):
        if mask & (1 << i):
            result = cm(result, value)
    return result


def actual_terms(mask, z, y):
    indices = [i for i in range(len(NORMS)) if mask & (1 << i)]
    terms = []
    for slots in product(range(3), repeat=len(indices)):
        a = b = m = 0
        for i, slot in zip(indices, slots):
            if slot == 0:
                a |= 1 << i
            elif slot == 1:
                b |= 1 << i
            else:
                m |= 1 << i
        if norm(a) <= z and norm(b) <= z and norm(a) * norm(b) > y:
            terms.append((a, b, m, -mu(a) * mu(b)))
    return terms


core = (1 << 3) | (1 << 4)
pairing_cases = 0
for modulus in range(8):
    maximum_norm = norm(modulus)
    z = isqrt(maximum_norm * norm(core))
    if z * z < maximum_norm * norm(core):
        z += 1
    y = Q(maximum_norm)
    for b in divisors(modulus):
        n = b | core
        check("inverse_profile_geometry", z < norm(n) <= z * z)
        check("saturation_and_rough_geometry", norm(b) <= y < NORMS[3])
        terms = actual_terms(n, z, y)
        check("original_tuple_cofactor_coefficient",
              sum(sign for _, _, _, sign in terms) == 2 * mu(b))
        check("ordered_unordered_factor", 2 * mu(b) == mu(b) + mu(b))
        for deleted in (None, 0, 2, 3):
            values = [ROOTS[(i + modulus) % 6] for i in range(len(NORMS))]
            if deleted is not None:
                values[deleted] = ZERO
            direct = csum(cs(cm(cm(phase(a, values), phase(bb, values)),
                                phase(m, values)), sign)
                          for a, bb, m, sign in terms)
            check("phase_and_deletion_pairing",
                  direct == cs(phase(n, values), 2 * mu(b)))
        pairing_cases += 1

    # The same degree-k dilation filter is computed independently by its
    # Euler product and by complete signed divisor enumeration.
    for row in (ROOTS, (ZERO, ROOTS[2], ROOTS[4], ONE, ONE)):
        values = tuple(row[i] for i in range(len(NORMS)))
        for degree in range(-1, 5):
            direct = csum(cs(phase(b, values), mu(b) * Q(norm(b)) ** degree)
                          for b in divisors(modulus))
            euler = ONE
            for i in range(3):
                if modulus & (1 << i):
                    euler = cm(euler, ca(ONE, cs(values[i], -Q(NORMS[i]) ** degree)))
            check("dilation_euler_filter", direct == euler)

    pminus = prod((Q(NORMS[i] - 1, NORMS[i])
                   for i in range(3) if modulus & (1 << i)), start=Q(1))
    zplus = prod((Q(NORMS[i] + 1, NORMS[i])
                  for i in range(3) if modulus & (1 << i)), start=Q(1))
    check("signed_jacobian_density",
          sum(Q(mu(b), norm(b)) for b in divisors(modulus)) == pminus > 0)
    check("absolute_jacobian_mass",
          sum(Q(1, norm(b)) for b in divisors(modulus)) == zplus)
    check("density_ratio_bound", zplus / pminus <= 1 / pminus ** 2)
    if modulus:
        check("unweighted_inverse_is_different", sum(mu(b) for b in divisors(modulus)) == 0)

    for logweights in ((Q(1), Q(2), Q(3)), (Q(1, 2), Q(1, 2), Q(7, 3))):
        lognorm = lambda b: sum((logweights[i] for i in range(3) if b & (1 << i)), Q(0))
        s = sum((logweights[i] / (NORMS[i] + 1)
                 for i in range(3) if modulus & (1 << i)), Q(0))
        check("absolute_weighted_first_log_moment",
              sum(lognorm(b) / norm(b) for b in divisors(modulus)) == zplus * s)
        for first in range(1, 7):
            moments = [Q(0)] * first + [Q(2, 3)]
            for degree in range(first + 1):
                translated = sum(
                    Q(mu(b), norm(b)) * sum(
                        comb(degree, j) * moments[j] * lognorm(b) ** (degree - j)
                        for j in range(degree + 1))
                    for b in divisors(modulus))
                expected = pminus * moments[degree]
                check("first_nonzero_translated_moment", translated == expected)

# Norm equality cannot collapse ideal symbols or Euler multiplicity.
check("equal_norm_distinct_symbols", norm(1) == norm(2) and divisors(1) != divisors(2))
check("equal_norm_euler_multiplicity",
      sum(Q(mu(b), norm(b)) for b in divisors(3)) == Q(6, 7) ** 2)

# A balanced triple violates the rough-core premise of a partial one-prime
# resummation. All three singleton divisors, not just the chosen one, enter.
triple_norms = (31, 37, 43)
triple_z = isqrt(prod(triple_norms)) + 1
triple_y = Q(43)
def triple_c(mask):
    indices = [i for i in range(3) if mask & (1 << i)]
    result = 0
    for slots in product(range(2), repeat=len(indices)):
        a = prod(triple_norms[i] for i, slot in zip(indices, slots) if slot == 0)
        b = prod(triple_norms[i] for i, slot in zip(indices, slots) if slot == 1)
        if a <= triple_z and b <= triple_z:
            result += (-1) ** len(indices)
    return result
triple_tail = -sum(triple_c(mask) for mask in range(8)
                   if prod(triple_norms[i] for i in range(3) if mask & (1 << i)) > triple_y)
check("balanced_triple_true_coefficient", triple_tail == -6)
check("balanced_triple_missing_prefix_terms", triple_tail - (-2) == -4)

# Exact coefficient-level decomposition of the saturated rough response
# into a free masked sum and its signed complement, with no estimate for
# the complement inferred from the free sum.
for modulus in range(8):
    y = Q(norm(modulus))
    for exponents in product(range(3), repeat=len(NORMS)):
        support = sum(1 << i for i, e in enumerate(exponents) if e)
        coprime = not support & modulus
        rough = all(NORMS[i] > y for i, e in enumerate(exponents) if e)
        squarefree = all(e <= 1 for e in exponents)
        selected = rough and squarefree
        mobius = (-1) ** sum(exponents) if squarefree else 0
        actual = (1 + mobius) if selected else 0
        free = int(coprime)
        remainder = (mobius if selected else 0) - int(coprime and not selected)
        check("exact_free_plus_complement", actual == free + remainder)
        if selected:
            check("rough_residual_coprime_to_mask", coprime)
        if not squarefree and coprime:
            check("nonsquarefree_complement_retained", free == 1 and remainder == -1 and actual == 0)

for beta in (Q(1, 100), Q(1, 40), Q(49, 1000)):
    eta = (Q(1, 20) - beta) / 2
    check("main_row_saturation_margin", Q(1, 20) - eta > beta)
    check("uniform_rough_prime_margin", Q(1, 2) - beta > Q(9, 20))
    check("coherent_saturation_margin", Q(23, 60) > beta)
    check("row_lattice_error_margin", Q(1, 30) + Q(1, 10000) < Q(1, 15))
check("free_completion_saturation_ratio", 2 * Q(9, 20) - 1 == -Q(1, 10))
check("retained_power_deficit", Q(16, 15) - Q(4, 5) == Q(4, 15))

print(json.dumps({
    "metadata": {
        "date": "2026-10-08", "prepared_for": "Edward Baker",
        "assistance": "Substantial LLM assistance", "model": "GPT-6 (Codex), inherited configuration",
        "exact_serving_variant": "not exposed; not inferred",
        "configured_reasoning_effort": "not exposed; not inferred",
    },
    "assertions_by_group": dict(sorted(counts.items())),
    "assertions_total": sum(counts.values()),
    "actual_pairing_cases": pairing_cases,
    "prime_symbol_norms": NORMS,
    "balanced_triple": {"norms": triple_norms, "z": triple_z, "Y": 43,
                        "actual_coefficient": triple_tail, "missing_prefix": -4},
    "scope": "Finite ideal algebra, exact phases, formal log substitutions and rational budgets only.",
    "limitations": ["No PNT, uniform Taylor remainder, infinite moment or physical reciprocity validation.",
                    "The selected-block obstruction is not a lower bound for the full signed response."],
}, indent=2, sort_keys=True))
