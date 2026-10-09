#!/usr/bin/env python3
"""Exact finite identities and budgets for mixed note 6.

Prepared for Edward Baker, 9 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; configured effort and exact
serving variant are not exposed and are not inferred. Standard library only.
Prints a deterministic small JSON record; writes no files. Formal characters
are not native residue symbols. No asymptotic operator bound is certified.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import prod
import json

counts = Counter()


def check(value, group):
    counts[group] += 1
    if not value:
        raise AssertionError(group)


# Exact arithmetic in Q[zeta_6], zeta_6^2 = zeta_6 - 1.
ZERO, ONE = (Q(0), Q(0)), (Q(1), Q(0))
ROOTS = (ONE, (Q(0), Q(1)), (Q(-1), Q(1)),
         (Q(-1), Q(0)), (Q(0), Q(-1)), (Q(1), Q(-1)))


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0] + x[1]*y[1]


def conj(x):
    return x[0] + x[1], -x[1]


def scale(x, c):
    return c*x[0], c*x[1]


def total(xs):
    answer = ZERO
    for x in xs:
        answer = add(answer, x)
    return answer


def norm2(x):
    return x[0]**2 + x[0]*x[1] + x[1]**2


# Distinct formal prime symbols may have equal norm.
NORMS = (2, 2, 3)
PAIRING = ((0, 1, 2), (1, 0, 5), (2, 5, 0))
ROWS = tuple(product(range(6), repeat=3))


def ideal_norm(v):
    return prod(p**a for p, a in zip(NORMS, v))


def phase(row, column):
    if any(a and b for a, b in zip(row, column)):
        return ZERO
    e = sum(row[i]*PAIRING[i][j]*column[j] for i in range(3) for j in range(3))
    return ROOTS[e % 6]


COLUMNS = tuple(product(range(8), repeat=3))
mask_witnesses = 0
for column in COLUMNS:
    base = tuple(a % 6 for a in column)
    sixth = tuple(a // 6 for a in column)
    check(tuple(a + 6*b for a, b in zip(base, sixth)) == column,
          "unique_sixth_power_column_decomposition")
    for row in ROWS:
        mask = not any(a and b for a, b in zip(row, sixth))
        check(phase(row, column) == scale(phase(row, base), int(mask)),
              "sixth_power_zero_mask_identity")
        mask_witnesses += not mask and phase(row, base) != ZERO
check(mask_witnesses > 0, "nontrivial_canceled_phase_mask")
check(ideal_norm((1, 0, 0)) == ideal_norm((0, 1, 0)),
      "equal_norm_distinct_prime_symbols")

# Keep fixed endpoint factors and arbitrary coefficients during decomposition.
frame_columns = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
                 (1, 1, 0), (2, 0, 1), (6, 0, 0), (0, 6, 0),
                 (0, 0, 6), (7, 0, 0), (0, 7, 1), (1, 0, 7))
frame_rows = ROWS[::7]
fixed_u, fixed_a = (1, 0, 0), (2, 0, 0)
coeffs = [scale(mul(phase(fixed_u, k), conj(phase(fixed_a, k))),
                Q((j % 7) - 3, 11)) for j, k in enumerate(frame_columns)]
grouped = {}
for k, coeff in zip(frame_columns, coeffs):
    base, sixth = tuple(a % 6 for a in k), tuple(a // 6 for a in k)
    grouped.setdefault(sixth, []).append((base, coeff))
masked_parts, unmasked_parts, full = {}, {}, []
for sixth, entries in grouped.items():
    raw = [total(mul(c, conj(phase(row, base))) for base, c in entries)
           for row in frame_rows]
    masked = [scale(x, int(not any(a and b for a, b in zip(row, sixth))))
              for row, x in zip(frame_rows, raw)]
    check(sum(map(norm2, masked)) <= sum(map(norm2, raw)),
          "mask_removed_only_after_positive_square")
    masked_parts[sixth], unmasked_parts[sixth] = masked, raw
for j, row in enumerate(frame_rows):
    direct = total(mul(c, conj(phase(row, k))) for k, c in zip(frame_columns, coeffs))
    decomposed = total(part[j] for part in masked_parts.values())
    check(direct == decomposed, "actual_fixed_coefficient_kernel_expansion")
    full.append(direct)
weighted_upper = sum(Q(ideal_norm(sixth))**-3 for sixth in grouped) * sum(
    Q(ideal_norm(sixth))**3 * sum(map(norm2, part))
    for sixth, part in masked_parts.items())
check(sum(map(norm2, full)) <= weighted_upper, "weighted_hilbert_cauchy")

# Full physical exterior norm, including its valuations, defines the new cut.
endpoint_pairs = [(ROWS[j], ROWS[(7*j+13) % len(ROWS)])
                  for j in range(0, len(ROWS), 11)]
non_squarefree_exteriors = 0
for u, h in endpoint_pairs:
    support = tuple(bool(a or b) for a, b in zip(u, h))
    for v in ROWS:
        fixed = tuple(a if inside else 0 for a, inside in zip(v, support))
        exterior = tuple(0 if inside else a for a, inside in zip(v, support))
        check(tuple(a+b for a, b in zip(fixed, exterior)) == v,
              "exact_middle_factor_partition")
        reverse = tuple(0 if a or b else c for a, b, c in zip(h, u, v))
        check(exterior == reverse, "external_cut_endpoint_reversal")
        for radius in (1, 2, 4, 12, 64):
            check((ideal_norm(exterior) <= radius) != (ideal_norm(exterior) > radius),
                  "exact_new_cut_complement")
        non_squarefree_exteriors += any(a > 1 for a in exterior)
check(non_squarefree_exteriors > 0, "physical_cap_includes_higher_valuations")

# Sharp-family supports on four formal prime ideals, each exponent 1/2 in U.
u, v, h = (1, 1, 0, 0), (1, 0, 0, 1), (1, 0, 1, 0)
edges = [sum(Q(1, 2) for a, b in zip(x, y) if a != b)
         for x, y in ((u, v), (v, h), (u, h))]
external_power = sum(Q(1, 2)*c for a, b, c in zip(u, h, v) if not (a or b))
check(edges == [Q(1)]*3 and external_power == Q(1, 2),
      "old_sharp_family_in_new_sector")

# A six-prime raw geometry survives the new physical exterior cap.
prime_powers = (Q(9,20), Q(1,20), Q(1,2), Q(1,2), Q(7,20), Q(1,10))
u, h, v = (1,1,1,0,0,0), (1,1,0,1,0,0), (1,0,0,0,1,2)
check([sum(p*a for p,a in zip(prime_powers,row)) for row in (u,h,v)] == [Q(1)]*3,
      "higher_valuation_complement_geometry")
check([sum(p for p,a,b in zip(prime_powers,left,right) if a != b)
       for left,right in ((u,v),(v,h),(u,h))] == [Q(1)]*3,
      "higher_valuation_complement_geometry")
check(sum(p*a for p,a,b,c in zip(prime_powers,v,u,h) if not (b or c)) == Q(11,20),
      "higher_valuation_complement_geometry")
check(sum(p for p,a in zip(prime_powers,v) if a) == Q(9,10),
      "higher_valuation_complement_geometry")

# Exact source parameter point and budgets.
d, x, eta, ell = Q(9, 25), Q(1, 2), Q(1, 5000), Q(1, 1000000)
a, bx, dx = Q(5, 6)-d, 2-Q(8, 9)*x, 3-Q(17, 9)*x
px = bx*(1-x)
jx = a*dx + d*px
row_count = 1-d + a*d*px/(2*jx)
f = a*bx/jx
rn = 1-f/2-(1-f)*eta/(d*(1-x))
mn = Q(1, 2)-a/jx*((1-x)/2-eta/d)
r, m = rn+Q(1, 20000), mn-Q(1, 40000)
z = (1-r)/2-ell/2
s, g = eta-d*(1-x)*Q(1, 20000)+ell, d*(r+z)
R, mu = row_count+ell, max(Q(0), 1-row_count-ell-g)
target = 3*(1+d*m-s)-2*m
kappa = Q(103, 200)
sigma = 5*kappa/6-2*m/3
reserve = target-(2*(1-mu)+g+d*m+sigma)
sharp_reserve = reserve+Q(1, 80)
uniform = 1-5*kappa/6-Q(21, 50)*(1+Q(73, 100))/2 \
          -(Q(4, 3)-2*Q(21, 50))*Q(207, 500)-3*Q(101, 500000)
check(reserve == Q(7362652673, 507450000000), "exact_new_sector_point_reserve")
check(sharp_reserve == Q(13705777673, 507450000000), "exact_sharp_family_reserve")
check(uniform == Q(4031, 1500000), "exact_uniform_new_sector_reserve")
for mm, kk in product((Q(2, 5), Q(207, 500)), (Q(1, 2), kappa)):
    sieve_terms = (kk, mm+kk/6, 5*kk/6+mm/3, kk/3+5*mm/6)
    check(max(sieve_terms) == 5*kk/6+mm/3, "dominant_physical_sieve_term")
for dd, rr, mm in product((Q(9, 25), Q(21, 50)),
                          (Q(7, 10), Q(73, 100)), (Q(2, 5), Q(207, 500))):
    check(2*mm-(1+rr)/2 < 0 and Q(4, 3)-2*dd > 0,
          "uniform_reserve_monotonicity")

capacity = Q(2, 9)*(1-2*m)
D = 2*d*m+d*capacity-g
best = (D+mu)/2
gap = s-best
fourth_gap = 2*s-mu-D
check(best == Q(165074, 1321484375), "direct_holder_budget")
check(gap == Q(88651, 1321484375), "direct_holder_budget")
check(fourth_gap == Q(177302, 1321484375), "direct_holder_budget")
y = (1-R-d*capacity)/2
check(y <= d*m and R+g <= 1, "marginal_saturation_model")
check(R+2*y+d*capacity == 1, "marginal_saturation_model")
check(R+g+y == 1+d*m-best, "marginal_saturation_model")
for alpha, beta in ((Q(0),Q(0)),(Q(1),Q(0)),(Q(0),Q(1,2)),(Q(1,2),Q(1,2))):
    exponent = R+g+d*m+alpha*mu+beta*(mu-D)
    check(exponent >= 1+d*m-best, "holder_vertex_envelope")

record = {
    "metadata": {"date": "2026-10-09", "prepared_for": "Edward Baker",
                 "model": "GPT-6 (Codex), inherited configuration",
                 "configured_reasoning_effort": "not exposed; not inferred",
                 "assistance": "Substantial LLM assistance"},
    "assertions_total": sum(counts.values()),
    "assertions_by_group": dict(sorted(counts.items())),
    "formal_rows": len(ROWS), "formal_columns": len(COLUMNS),
    "nontrivial_sixth_power_mask_witnesses": mask_witnesses,
    "new_external_factor_cap": str(kappa),
    "uniform_sector_reserve": str(uniform),
    "operational_point_sector_reserve": str(reserve),
    "old_sharp_family_reserve": str(sharp_reserve),
    "ideal_direct_saving": str(best), "ideal_direct_gap": str(gap),
    "inverse_weighted_fourth_gap": str(fourth_gap),
    "limitations": ["Formal cyclotomic identities and rational budgets only.",
                    "No native reciprocity or physical presentation validation.",
                    "No large-sieve theorem or asymptotic operator certification.",
                    "Ideal direct slot capacity is a favorable relaxation.",
                    "No full mixed energy, zero-free improvement, or RH implication."]}
print(json.dumps(record, sort_keys=True, indent=2))
