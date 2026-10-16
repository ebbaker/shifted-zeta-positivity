#!/usr/bin/env python3
"""Finite conductor geometry and actual-endpoint chain checks.

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact variant and reasoning
effort are not exposed and are not inferred. Standard library only.
Prints a small deterministic JSON record and writes no files.
Formal prime symbols and character frames do not certify native reciprocity,
an imported analytic bound, asymptotic counts, or an unbounded moment.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from math import prod
import json
import random


counts = Counter()


def check(value, group):
    counts[group] += 1
    if not value:
        raise AssertionError(group)


NORMS = (7, 7, 13)  # Equal norm does not identify the first two ideals.
ROWS = tuple(product(range(6), repeat=len(NORMS)))
SUPPORTS = tuple(product(range(2), repeat=len(NORMS)))


def support(left, right):
    return tuple(int(a != b) for a, b in zip(left, right))


def norm(bits):
    return prod(n ** b for n, b in zip(NORMS, bits))


for a, b, c in product(range(6), repeat=3):
    p, q, f = int(a != b), int(b != c), int(a != c)
    extra = int(a != c and b not in (a, c))
    doubled = int(a == c and b != a)
    check(p + q == f + extra + 2 * doubled, "local_PQ_equals_FAB_squared")

for u in ROWS:
    histogram = Counter(support(u, v) for v in ROWS)
    for f in SUPPORTS:
        check(histogram[f] == 5 ** sum(f), "fixed_row_neighbor_multiplicity")
check(norm((1, 0, 0)) == norm((0, 1, 0)), "equal_norm_distinct_supports")
check((1, 0, 0) != (0, 1, 0), "equal_norm_distinct_supports")

rng = random.Random(20261008)
endpoint_pairs = [(ROWS[0], ROWS[-1]), (ROWS[0], ROWS[0])]
endpoint_pairs += [(rng.choice(ROWS), rng.choice(ROWS)) for _ in range(38)]
cutoffs = (1, 7, 13, 49, 91, 637)
for u, h in endpoint_pairs:
    f = support(u, h)
    nf = norm(f)
    for v in ROWS:
        p, q = support(u, v), support(v, h)
        extra = tuple(int(a != c and b not in (a, c))
                      for a, b, c in zip(u, v, h))
        doubled = tuple(int(a == c and b != a)
                        for a, b, c in zip(u, v, h))
        check(norm(p) * norm(q) == nf * norm(extra) * norm(doubled) ** 2,
              "coupled_conductor_norm_identity")
        check(all(not (a and b) for a, b in zip(f, doubled)),
              "new_support_disjoint_from_endpoint_support")
    for v1, v2 in product(cutoffs, repeat=2):
        actual = sum(norm(support(u, v)) <= v1
                     and norm(support(v, h)) <= v2 for v in ROWS)
        upper = 6 ** sum(f) * sum(
            5 ** sum(b) for b in SUPPORTS
            if all(not (a and c) for a, c in zip(f, b))
            and nf * norm(b) ** 2 <= v1 * v2)
        check(actual <= upper, "coupled_middle_count_majorant")
        if v1 * v2 < nf:
            check(actual == 0, "conductor_triangle_empty_range")
    for radius in cutoffs:
        actual = sum(norm(support(u, v)) * norm(support(v, h)) <= radius * nf
                     for v in ROWS)
        upper = 6 ** sum(f) * sum(
            5 ** sum(b) for b in SUPPORTS
            if all(not (a and c) for a, c in zip(f, b))
            and norm(b) ** 2 <= radius)
        check(actual <= upper, "coupled_conductor_excess_count")

# Exact arithmetic in Z[zeta_6], with zeta_6^2=zeta_6-1.
def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c + b * d


def conjugate(x):
    return x[0] + x[1], -x[1]


def scale(x, a):
    return x[0] * a, x[1] * a


def squared(x):
    return x[0] ** 2 + x[0] * x[1] + x[1] ** 2


ZERO, ONE = (Q(0), Q(0)), (Q(1), Q(0))
ROOTS = (ONE, (Q(0), Q(1)), (Q(-1), Q(1)),
         (Q(-1), Q(0)), (Q(0), Q(-1)), (Q(1), Q(-1)))


def total(values):
    out = ZERO
    for value in values:
        out = add(out, value)
    return out


def phase(row, column):
    if any(a and b for a, b in zip(row, column)):
        return ZERO
    pairing = ((0, 1, 2), (1, 0, 5), (2, 5, 0))
    exponent = sum(row[i] * pairing[i][j] * column[j]
                   for i in range(3) for j in range(3))
    return ROOTS[exponent % 6]


# These formal masked frames test expansion and absolute sector bounds;
# they are not a construction of physical residue symbols or selected bins.
frame_rows = [ROWS[0], (1, 0, 0), (0, 1, 0), (0, 0, 1),
              (1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 1, 0),
              (1, 2, 0), (3, 0, 1), (0, 3, 2), (5, 1, 0)]
columns = SUPPORTS
profiles = tuple(Q(a, 8) for a in (1, 2, -1, 3, 1, -2, 2, 1))
t = [[scale(phase(u, k), profiles[j]) for j, k in enumerate(columns)]
     for u in frame_rows]
sums = [total(row) for row in t]
kernel = [[total(mul(t[i][k], conjugate(t[j][k]))
                 for k in range(len(columns))) for j in range(len(t))]
          for i in range(len(t))]
deleted_entries = sum(value == ZERO for row in t for value in row)
check(deleted_entries > 0, "physical_style_deletion_zeros_retained")
shared_row, shared_column = (1, 0, 0), (1, 0, 0)
check(support(shared_row, shared_row) == (0, 0, 0)
      and mul(phase(shared_row, shared_column),
              conjugate(phase(shared_row, shared_column))) == ZERO,
      "canceled_phase_keeps_deletion_zero")
weights = [Q((i % 4) ** 2, 9) for i in range(len(frame_rows))]
mass, envelope = sum(weights), max(weights)
endpoint_bound = max(map(squared, sums))
kernel_bound = max(squared(kernel[i][j]) for i in range(len(t))
                   for j in range(len(t)) if i != j)
triples = tuple(product(range(len(t)), repeat=3))
nonzero_sector_witnesses = 0


def term(i, j, k):
    return scale(mul(mul(mul(conjugate(sums[i]), kernel[i][j]),
                         kernel[j][k]), sums[k]),
                 weights[i] * weights[j] * weights[k])


for radius in (1, 7, 13, 49, 91):
    degrees = [sum(weights[j] for j, v in enumerate(frame_rows)
                   if norm(support(u, v)) <= radius) for u in frame_rows]
    degree = max(degrees)
    count_bound = max(sum(norm(support(u, v)) <= radius for v in frame_rows)
                      for u in frame_rows)
    check(degree <= envelope * count_bound, "weighted_neighbor_degree")
    selected = [(i, j, k) for i, j, k in triples if len({i, j, k}) == 3
                and min(norm(support(frame_rows[a], frame_rows[b]))
                        for a, b in ((i, j), (j, k), (i, k))) <= radius]
    value = total(term(*triple) for triple in selected)
    weighted_count = sum(weights[i] * weights[j] * weights[k]
                         for i, j, k in selected)
    check(weighted_count <= 3 * mass ** 2 * degree,
          "any_close_edge_weighted_triples")
    bound = kernel_bound * endpoint_bound * weighted_count
    check(squared(value) <= bound ** 2, "actual_endpoint_sector_bound")
    check(value == conjugate(value), "reversal_real_sector")
    nonzero_sector_witnesses += value != ZERO

for v1, v2 in product((7, 13, 49), repeat=2):
    degree1 = max(sum(weights[j] for j, v in enumerate(frame_rows)
                      if norm(support(u, v)) <= v1) for u in frame_rows)
    degree2 = max(sum(weights[j] for j, v in enumerate(frame_rows)
                      if norm(support(u, v)) <= v2) for u in frame_rows)
    for first, second in combinations(((0, 1), (1, 2), (0, 2)), 2):
        selected = [r for r in triples if len(set(r)) == 3
                    and norm(support(frame_rows[r[first[0]]],
                                     frame_rows[r[first[1]]])) <= v1
                    and norm(support(frame_rows[r[second[0]]],
                                     frame_rows[r[second[1]]])) <= v2]
        weighted_count = sum(prod(weights[x] for x in r) for r in selected)
        check(weighted_count <= mass * degree1 * degree2,
              "two_close_edges_tree_weighted_count")
        value = total(term(*r) for r in selected)
        bound = kernel_bound * endpoint_bound * weighted_count
        check(squared(value) <= bound ** 2, "tree_actual_endpoint_sector_bound")

check(nonzero_sector_witnesses > 0, "nonzero_selected_chain_witness")


def category(i, j, k, size):
    quv = norm(support(frame_rows[i], frame_rows[j]))
    qvh = norm(support(frame_rows[j], frame_rows[k]))
    quh = norm(support(frame_rows[i], frame_rows[k]))
    p = quv * qvh
    tests = (
        min(quv, qvh, quh) ** 25 <= size ** 6,
        min(p, quv * quh, qvh * quh) ** 20 <= size ** 17,
        p ** 25 <= size ** 12 * quh ** 25,
        min(quv, qvh) ** 100 <= size ** 39,
        p ** 100 <= size ** 103,
        p ** 16 <= size ** 15 * quh ** 8,
    )
    return next((f"Gamma_{a + 1}" for a, yes in enumerate(tests) if yes),
                "remaining")


partition_counts = Counter()
for size in (2, 16, 256, 4096):
    groups = {f"Gamma_{i}": ZERO for i in range(1, 7)}
    groups["remaining"] = ZERO
    full = ZERO
    for i, j, k in triples:
        if len({i, j, k}) != 3:
            continue
        key = category(i, j, k, size)
        check(key == category(k, j, i, size), "six_sector_reversal_invariance")
        value = term(i, j, k)
        groups[key] = add(groups[key], value)
        full = add(full, value)
        partition_counts[key] += 1
    check(total(groups.values()) == full, "six_sector_exact_chain_partition")
    for value in groups.values():
        check(value == conjugate(value), "six_sector_real_grouped_chains")

old_repeat = Q(147, 12500)
endpoint_reserve = old_repeat + (1 - Q(21, 50)) * Q(2, 5)
single_reserve = endpoint_reserve - Q(6, 25)
tree_baseline = 2 * old_repeat + (Q(15, 4) - 4 * Q(21, 50)) * Q(2, 5)
tree_reserve = tree_baseline - Q(17, 20)
coupled_kappa = (2 * Q(3, 5) - Q(3, 4)) / 2
coupled_reserve = endpoint_reserve - coupled_kappa
ratio_reserve = endpoint_reserve - Q(6, 25)
poisson_single_reserve = endpoint_reserve + Q(7, 8) * Q(2, 5) - Q(3, 2) * Q(39, 100)
poisson_product_reserve = tree_baseline + Q(7, 4) * Q(2, 5) - Q(3, 2) * Q(103, 100)
coupled_poisson_reserve = endpoint_reserve + Q(7, 4) * Q(2, 5) - Q(15, 16)
check(endpoint_reserve == Q(3047, 12500), "exact_uniform_reserves")
check(single_reserve == Q(47, 12500), "exact_uniform_reserves")
check(tree_reserve == Q(19, 12500), "exact_uniform_reserves")
check(coupled_kappa == Q(9, 40), "exact_uniform_reserves")
check(coupled_reserve == Q(469, 25000), "exact_uniform_reserves")
check(ratio_reserve == Q(47, 12500), "exact_uniform_reserves")
check(poisson_single_reserve == Q(219, 25000), "exact_uniform_reserves")
check(poisson_product_reserve == Q(163, 25000), "exact_uniform_reserves")
check(coupled_poisson_reserve == Q(313, 50000), "exact_uniform_reserves")
for d, m, mu, saving, g in product((Q(9, 25), Q(21, 50)),
                                  (Q(2, 5), Q(41, 100)),
                                  (Q(0), Q(1, 5000)),
                                  (Q(0), Q(101, 500000)),
                                  (Q(3, 10), Q(7, 20))):
    target = 3 * (1 - (1 - d) * m - saving) + m
    repeat0 = 1 - g - (Q(11, 4) - 3 * d) * m - 3 * saving
    tree_margin = target - (1 - mu + 2 * g + (d - Q(1, 4)) * m)
    check(tree_margin == 2 * repeat0 + (Q(15, 4) - 4 * d) * m
          + mu + 3 * saving, "tree_margin_algebra")
    for q1, q2, f in ((Q(3, 5), Q(3, 5), Q(3, 4)),
                      (Q(1, 2), Q(1, 2), Q(4, 5))):
        kappa = max(Q(0), (q1 + q2 - f) / 2)
        sector = 2 * (1 - mu) + g + (d - Q(1, 4)) * m + kappa
        check(target - sector == repeat0 + (1 - d) * m + 2 * mu - kappa,
              "coupled_margin_algebra")
    single_poisson = 2 * (1 - mu) + g + (d - Q(9, 8)) * m + Q(3, 2) * Q(39, 100)
    product_poisson = 1 - mu + 2 * g + (d - 2) * m + Q(3, 2) * Q(103, 100)
    check(target - single_poisson == repeat0 + (1 - d) * m + 2 * mu
          + Q(7, 8) * m - Q(3, 2) * Q(39, 100), "poisson_sector_margin_algebra")
    check(target - product_poisson == tree_margin + Q(7, 4) * m
          - Q(3, 2) * Q(103, 100), "poisson_sector_margin_algebra")
    mixed_poisson = 2 * (1 - mu) + g + (d - 2) * m + Q(15, 16)
    check(target - mixed_poisson == repeat0 + (1 - d) * m + 2 * mu
          + Q(7, 4) * m - Q(15, 16), "poisson_sector_margin_algebra")

eta_plus = Q(101, 500000)  # eta+2 ell, near-saturated legal slots.
absolute_gap = (Q(7, 4) - 2 * Q(21, 50)) * Q(2, 5) - 3 * eta_plus
check(absolute_gap == Q(181697, 500000), "remaining_absolute_budget_deficit")
# Valuation support example: u=abc, v=abd, h=ade, with a exponent .42
# and b,c,d,e exponent .29 in norm. All three physical row norms have power1.
example = ((1, 1, 1, 0, 0), (1, 1, 0, 1, 0), (1, 0, 0, 1, 1))
prime_exponents = (Q(21, 50),) + (Q(29, 100),) * 4
row_exponents = [sum(e * bit for e, bit in zip(prime_exponents, u))
                 for u in example]
edge_exponents = [sum(e for e, a, b in zip(prime_exponents, example[i], example[j])
                      if a != b) for i, j in ((0, 1), (1, 2), (0, 2))]
check(row_exponents == [Q(1)] * 3, "growing_coupled_support_example")
check(edge_exponents == [Q(29, 50), Q(29, 50), Q(29, 25)],
      "growing_coupled_support_example")
check(min(edge_exponents) > Q(6, 25)
      and sum(sorted(edge_exponents)[:2]) > Q(17, 20),
      "coupled_example_beyond_basic_sector_cuts")
check(min(edge_exponents[:2]) > Q(39, 100)
      and sum(edge_exponents[:2]) > Q(103, 100)
      and sum(edge_exponents[:2]) - edge_exponents[2] < Q(12, 25),
      "coupled_example_beyond_poisson_sector_cuts")
# A second geometric sector: u=ab,h=ac,v=ad, with a exponent .71
# and b,c,d exponent .29. Its three quotient conductors have power .58.
equal_edges = Q(29, 50)
check(equal_edges > Q(39, 100) and 2 * equal_edges > Q(103, 100)
      and equal_edges > Q(12, 25) and 3 * equal_edges < Q(15, 8),
      "coupled_poisson_example_beyond_other_cuts")

# Exact operational point; this checks the budget, not existence of its bin.
d, x, eta, ell = Q(9, 25), Q(1, 2), Q(1, 5000), Q(1, 1000000)
a = Q(5, 6) - d
bx, dx = 2 - Q(8, 9) * x, 3 - Q(17, 9) * x
px = bx * (1 - x)
jx = a * dx + d * px
row_count = 1 - d + a * d * px / (2 * jx)
factor = a * bx / jx
rn = 1 - factor / 2 - (1 - factor) * eta / (d * (1 - x))
mn = Q(1, 2) - a / jx * ((1 - x) / 2 - eta / d)
r, m = rn + Q(1, 20000), mn - Q(1, 40000)
z = (1 - r) / 2 - ell / 2
saving = eta - d * (1 - x) * Q(1, 20000) + ell
g = d * (r + z)
mu = max(Q(0), 1 - row_count - ell - g)
target = 3 * (1 - (1 - d) * m - saving) + m
middle_budget = target - (2 * (1 - mu) + g + (d - Q(1, 4)) * m)
sharp_count_gap = Q(1, 2) - middle_budget
check(row_count == Q(58601, 84575) and r == Q(47752383, 67660000),
      "exact_operational_point")
check(m == Q(54905017, 135320000) and z == Q(995377467, 6766000000),
      "exact_operational_point")
check(g == Q(51935541903, 169150000000) and saving == Q(3, 15625),
      "exact_operational_point")
check(mu == Q(12288947, 169150000000) and r + 2 * z == 1 - ell,
      "exact_operational_point")
check(middle_budget == Q(92902792407, 338300000000), "sharp_middle_count_budget")
check(sharp_count_gap == Q(76247207593, 338300000000), "sharp_middle_count_budget")

print(json.dumps({
    "metadata": {"date": "2026-10-08", "prepared_for": "Edward Baker",
                 "model": "GPT-6 (Codex), inherited configuration",
                 "exact_serving_variant": "not exposed; not inferred",
                 "configured_reasoning_effort": "not exposed; not inferred",
                 "assistance": "Substantial LLM assistance"},
    "assertions_total": sum(counts.values()),
    "assertions_by_group": dict(sorted(counts.items())),
    "formal_prime_norms": NORMS,
    "sixth_power_free_rows": len(ROWS),
    "coupled_endpoint_pairs": len(endpoint_pairs),
    "finite_frame_rows": len(frame_rows),
    "finite_frame_deleted_entries": deleted_entries,
    "nonzero_sector_witnesses": nonzero_sector_witnesses,
    "six_sector_partition_counts": dict(sorted(partition_counts.items())),
    "uniform_exponent_reserves": {"one_edge": str(single_reserve),
                                  "two_edge_product": str(tree_reserve),
                                  "coupled_rectangle": str(coupled_reserve),
                                  "coupled_excess_ratio": str(ratio_reserve),
                                  "poisson_one_leg": str(poisson_single_reserve),
                                  "poisson_leg_product": str(poisson_product_reserve),
                                  "coupled_poisson": str(coupled_poisson_reserve)},
    "remaining_absolute_gap_lower_bound": str(absolute_gap),
    "sharp_middle_count_budget_gap_at_operational_point": str(sharp_count_gap),
    "limitations": ["Finite formal ideal and masked-frame checks only.",
                    "No native reciprocity or asymptotic conductor count validation.",
                    "No analytic Poisson or conductor-growth theorem validation.",
                    "Imported endpoint and kernel inputs remain conditional.",
                    "No full mixed moment or zero-free improvement."]
}, indent=2, sort_keys=True))
