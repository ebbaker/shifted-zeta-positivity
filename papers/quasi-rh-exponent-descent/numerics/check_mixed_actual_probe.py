#!/usr/bin/env python3
"""Exact finite algebra for the mixed family's actual-probe cubic target.

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact variant and effort
are not exposed and are not inferred. Standard library only.

Rational Gaussian matrices test identities, positive spectral inequalities,
the open-chain partition with actual endpoints, and rational margins.
These are finite frames, not physical character or asymptotic certificates.
Prints deterministic JSON and writes no files.
"""

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
import itertools
import json
import random


counts = defaultdict(int)


def check(condition, group):
    counts[group] += 1
    if not condition:
        raise AssertionError(group)


@dataclass(frozen=True)
class Gaussian:
    real: F = F(0)
    imag: F = F(0)

    @staticmethod
    def make(value):
        return value if isinstance(value, Gaussian) else Gaussian(F(value))

    def __add__(self, other):
        other = self.make(other)
        return Gaussian(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self):
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other):
        return self + -self.make(other)

    def __rsub__(self, other):
        return self.make(other) + -self

    def __mul__(self, other):
        other = self.make(other)
        return Gaussian(self.real * other.real - self.imag * other.imag,
                        self.real * other.imag + self.imag * other.real)

    __rmul__ = __mul__

    def conjugate(self):
        return Gaussian(self.real, -self.imag)


ZERO = Gaussian()
ONE = Gaussian(F(1))


def adjoint(matrix):
    return [[matrix[i][j].conjugate() for i in range(len(matrix))]
            for j in range(len(matrix[0]))]


def product(left, right):
    return [[sum((left[i][k] * right[k][j] for k in range(len(right))), ZERO)
             for j in range(len(right[0]))] for i in range(len(left))]


def vector_product(matrix, vector):
    return [sum((a * b for a, b in zip(row, vector)), ZERO) for row in matrix]


def inner(left, right):
    return sum((a.conjugate() * b for a, b in zip(left, right)), ZERO)


def trace(matrix):
    return sum((matrix[i][i] for i in range(len(matrix))), ZERO)


def kind(cu, cv, ch):
    if cu == cv == ch:
        return "all_equal"
    if cu == ch:
        return "endpoints_equal"
    if cu == cv or cv == ch:
        return "adjacent_equal"
    return "pairwise_distinct"


def inspect_frame(raw, roots, classes):
    rows, columns = len(raw), len(raw[0])
    weights = [root * root for root in roots]
    weighted = [[roots[i] * value for value in raw[i]] for i in range(rows)]
    kernel = product(raw, adjoint(raw))
    gram = product(weighted, adjoint(weighted))
    column_gram = product(adjoint(weighted), weighted)
    probe = [ONE] * columns
    sums = vector_product(raw, probe)
    endpoint = [roots[i] * sums[i] for i in range(rows)]
    energy = inner(endpoint, endpoint)
    gram_squared = product(gram, gram)
    chain = inner(endpoint, vector_product(gram_squared, endpoint))
    positive_chain = inner(vector_product(gram, endpoint),
                           vector_product(gram, endpoint))
    column_cubed = product(product(column_gram, column_gram), column_gram)
    column_chain = inner(probe, vector_product(column_cubed, probe))
    cubic_trace = trace(product(gram_squared, gram))
    check(energy.imag == chain.imag == cubic_trace.imag == 0,
          "real_positive_functionals")
    check(energy.real >= 0 and chain.real >= 0 and cubic_trace.real >= 0,
          "real_positive_functionals")
    check(chain == positive_chain == column_chain, "probe_cubic_identities")
    check(trace(column_cubed) == cubic_trace, "probe_cubic_identities")
    check(energy.real ** 3 <= columns ** 2 * chain.real,
          "spectral_jensen_inequality")
    check(chain.real <= columns * cubic_trace.real,
          "probe_below_full_trace")

    grouped = defaultdict(lambda: ZERO)
    terms = defaultdict(int)
    for u, v, h in itertools.product(range(rows), repeat=3):
        term = (weights[u] * weights[v] * weights[h]
                * sums[u].conjugate() * kernel[u][v] * kernel[v][h] * sums[h])
        gram_term = (endpoint[u].conjugate()
                     * gram[u][v] * gram[v][h] * endpoint[h])
        check(term == gram_term, "actual_endpoint_open_chain_terms")
        category = kind(classes[u], classes[v], classes[h])
        grouped[category] = grouped[category] + term
        terms[category] += 1
    check(sum(grouped.values(), ZERO) == chain, "four_character_partition")
    check(sum(terms.values()) == rows ** 3, "four_character_partition")
    for category in ("all_equal", "adjacent_equal", "endpoints_equal", "pairwise_distinct"):
        check(grouped[category].imag == 0, "reversal_real_grouped_chains")
    check(grouped["all_equal"].real >= 0,
          "nonnegative_all_and_endpoint_equal")
    check(grouped["endpoints_equal"].real >= 0,
          "nonnegative_all_and_endpoint_equal")
    # All-equal and endpoint-equal are independently evaluated as positive
    # matrix block forms, rather than treated as arbitrary real groups.
    all_block = ZERO
    end_block = ZERO
    for first in sorted(set(classes)):
        first_rows = [i for i, c in enumerate(classes) if c == first]
        local_f = [endpoint[i] for i in first_rows]
        local_g = [[gram[i][j] for j in first_rows] for i in first_rows]
        all_block += inner(vector_product(local_g, local_f),
                           vector_product(local_g, local_f))
        for second in sorted(set(classes)):
            if second == first:
                continue
            second_rows = [i for i, c in enumerate(classes) if c == second]
            cross_g = [[gram[i][j] for j in first_rows] for i in second_rows]
            cross_f = vector_product(cross_g, local_f)
            end_block += inner(cross_f, cross_f)
    check(all_block == grouped["all_equal"], "positive_block_reconstruction")
    check(end_block == grouped["endpoints_equal"], "positive_block_reconstruction")
    return energy.real, chain.real, cubic_trace.real, grouped, terms


rng = random.Random(20261008)
frame_summaries = []
negative_group_counts = defaultdict(int)
partition_counts = defaultdict(int)
dimensions = ((1, 1), (2, 3), (3, 2), (3, 3), (4, 3), (4, 4),
              (5, 3), (5, 4))
for frame_index, (row_count, column_count) in enumerate(dimensions):
    for repetition in range(4):
        raw = [[Gaussian(F(rng.randrange(-3, 4), rng.randrange(1, 4)),
                         F(rng.randrange(-3, 4), rng.randrange(1, 4)))
                for _ in range(column_count)] for _ in range(row_count)]
        roots = [F(rng.randrange(0, 4)) for _ in range(row_count)]
        if repetition == 0:
            classes = [0] * row_count
        else:
            classes = [i % min(3, row_count) for i in range(row_count)]
        energy, chain, cubic_trace, grouped, terms = inspect_frame(raw, roots, classes)
        for category, count in terms.items():
            partition_counts[category] += count
        for category, value in grouped.items():
            if value.real < 0:
                negative_group_counts[category] += 1
        frame_summaries.append({"rows": row_count, "columns": column_count,
                                "repetition": repetition,
                                "zero_weight_rows": sum(root == 0 for root in roots)})

# A fixed actual all-ones probe avoids the large (1,-1) eigenspace.
strict_raw = [[Gaussian(F(5)), Gaussian(F(-5))], [ONE, ONE]]
strict = inspect_frame(strict_raw, [F(1), F(1)], [0, 1])
strict_energy, strict_chain, strict_trace = strict[:3]
check(strict_energy == 4 and strict_chain == 16 and strict_trace == 8 * 5 ** 6 + 8,
      "strict_relaxation_frame")
check(strict_chain < 2 * strict_trace, "strict_relaxation_frame")
check(strict_energy ** 3 == 4 * strict_chain, "strict_relaxation_frame")

# The initial constant vector and the open chain remain valid at zero energy.
zero = inspect_frame([[ZERO, ZERO], [ZERO, ZERO]], [F(1), F(2)], [0, 1])
check(zero[:3] == (F(0), F(0), F(0)), "zero_energy_frame")

old_all = F(154297, 500000)
old_repeat = F(147, 12500)
d_max = F(21, 50)
m_min = F(2, 5)
adjacent_bonus = (F(7, 8) - d_max) * m_min
other_bonus = (1 - d_max) * m_min
all_margin = old_all + other_bonus
adjacent_margin = old_repeat + adjacent_bonus
endpoint_margin = old_repeat + other_bonus
check(adjacent_bonus == F(91, 500) and other_bonus == F(29, 125),
      "rational_margin_comparisons")
check(all_margin == F(270297, 500000), "rational_margin_comparisons")
check(adjacent_margin == F(1211, 6250), "rational_margin_comparisons")
check(endpoint_margin == F(3047, 12500), "rational_margin_comparisons")
check(min(all_margin, adjacent_margin, endpoint_margin) > 0,
      "rational_margin_comparisons")
for d in (F(9, 25), F(39, 100), d_max):
    for m in (m_min, F(41, 100), F(1, 2)):
        # The derivative signs are explicit: these reserves increase in m
        # and decrease in d on the whole stated rectangle.
        check((F(7, 8) - d) * m >= adjacent_bonus,
              "rational_margin_comparisons")
        check((1 - d) * m >= other_bonus, "rational_margin_comparisons")
        check(F(7, 8) - d > 0 and 1 - d > 0,
              "rational_margin_comparisons")

# Target exponent transfer is an identity, not an assumed energy theorem.
for d, m, saving in itertools.product((F(9, 25), d_max),
                                     (F(2, 5), F(41, 100)),
                                     (F(0), F(1, 5000))):
    energy_target = 1 + d * m - saving
    h3 = 3 * (1 - (1 - d) * m - saving)
    probe_target = h3 + m
    check(2 * m + probe_target == 3 * energy_target,
          "target_exponent_transfer")

print(json.dumps({
    "metadata": {
        "date": "2026-10-08",
        "prepared_for": "Edward Baker",
        "assistance": "Substantial LLM assistance",
        "model": "GPT-6 (Codex), inherited configuration",
        "exact_serving_variant": "not exposed; not inferred",
        "configured_reasoning_effort": "not exposed; not inferred",
        "validation_status": "internal finite exact algebra and rational checks only",
    },
    "random_seed": 20261008,
    "rational_gaussian_frames": len(frame_summaries) + 2,
    "frames": frame_summaries,
    "open_chain_terms_by_character_type": dict(sorted(partition_counts.items())),
    "negative_group_witness_counts": dict(sorted(negative_group_counts.items())),
    "strict_relaxation_frame": {
        "a": 5, "column_count": 2,
        "energy": str(strict_energy), "probe_J": str(strict_chain),
        "full_trace": str(strict_trace),
    },
    "margin_bounds": {
        "all_equal": str(all_margin),
        "adjacent_equal": str(adjacent_margin),
        "endpoints_equal": str(endpoint_margin),
    },
    "assertions_by_group": dict(sorted(counts.items())),
    "assertions_total": sum(counts.values()),
    "limitations": [
        "Finite Gaussian frames are not physical Hecke character examples.",
        "The buffered plain estimate and kernel/fiber inputs remain imported analytic assumptions.",
        "The pairwise-inequivalent open-chain estimate is unproved.",
        "No new mixed moment or zero-free exponent is established.",
    ],
}, indent=2, sort_keys=True))
