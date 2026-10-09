#!/usr/bin/env python3
"""Exact finite identities and budgets for mixed note 7.

Prepared for Edward Baker, 9 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; configured effort and exact
serving variant are not exposed and are not inferred. Standard library only.
Prints a small deterministic JSON record and writes no files. Formal phases
are not native residue symbols; no asymptotic sieve bound is certified.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import prod
import json

from mixed_valuation_direct_checks import run_direct_checks

counts = Counter()


def check(value, group):
    counts[group] += 1
    if not value:
        raise AssertionError(group)


# Integer arithmetic in Z[zeta_6], zeta_6^2 = zeta_6 - 1.
ZERO, ONE = (0, 0), (1, 0)
ROOTS = (ONE, (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
NORMS = (2, 2, 3)  # Distinct prime symbols can have the same norm.
PAIRING = ((0, 1, 2), (1, 0, 5), (2, 5, 0))
ROWS = tuple(product(range(6), repeat=3))
SUBSETS = tuple(tuple(e for e in range(1, 6) if mask & (1 << (e-1)))
                for mask in range(1, 32))


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]+a[1]*b[1]


def conj(a):
    return a[0]+a[1], -a[1]


def norm2(a):
    return a[0]**2+a[0]*a[1]+a[1]**2


def total(xs):
    result = ZERO
    for x in xs:
        result = add(result, x)
    return result


def phase(row, col):
    if any(a and b for a, b in zip(row, col)):
        return ZERO
    exponent = sum(row[i]*PAIRING[i][j]*col[j]
                   for i in range(3) for j in range(3))
    return ROOTS[exponent % 6]


def ideal_norm(row):
    return prod(p**a for p, a in zip(NORMS, row))


columns = tuple(product(range(3), repeat=3)) + ((6, 0, 0), (0, 7, 1), (1, 0, 6))
deletion_witnesses = 0
for xi in ROWS:
    factors = [tuple(int(a == e) for a in xi) for e in range(1, 6)]
    check(tuple(sum(e*factors[e-1][j] for e in range(1, 6))
                for j in range(3)) == xi, "unique_valuation_factorization")
    check(all(sum(t[j] for t in factors) <= 1 for j in range(3)),
          "squarefree_disjoint_valuation_roots")
    reflected = tuple(6-a if a else 0 for a in xi)
    for column in columns:
        check(phase(reflected, column) == conj(phase(xi, column)),
              "complementary_power_identity_with_zeros")
        deletion_witnesses += phase(xi, column) == ZERO and phase((0, 0, 0), column) != ZERO
    for selected, reverse in product(SUBSETS, (False, True)):
        varying = tuple(a if a in selected else 0 for a in xi)
        frozen = tuple(a if a not in selected else 0 for a in xi)
        auxiliary = tuple((6-a if reverse else a) if a else 0 for a in varying)
        recovered = tuple((6-a if reverse else a) if a else 0 for a in auxiliary)
        check(recovered == varying, "injective_grouped_sixth_free_variable")
        check(all(a < 6 for a in auxiliary), "auxiliary_rows_sixth_free")
        check(tuple(a+b for a, b in zip(varying, frozen)) == xi,
              "frozen_and_varying_actual_row_partition")
        for column in ((0, 0, 0), (1, 2, 0), (0, 1, 1)):
            value = conj(phase(auxiliary, column)) if reverse else phase(auxiliary, column)
            check(mul(value, phase(frozen, column)) == phase(xi, column),
                  "fixed_coefficient_grouped_kernel_identity")
check(deletion_witnesses > 0, "nontrivial_complementary_power_deletion_zeros")

# Actual subsets and nonuniform weights precede positive square enlargement.
for selected, reverse in product(SUBSETS, (False, True)):
    groups = {}
    for j, xi in enumerate(ROWS):
        frozen = tuple(a if a not in selected else 0 for a in xi)
        auxiliary = tuple((6-a if reverse else a) if a in selected else 0 for a in xi)
        groups.setdefault(frozen, []).append((j, xi, auxiliary))
    for frozen, members in groups.items():
        check(len({aux for _, _, aux in members}) == len(members),
              "no_hidden_grouped_row_multiplicity")
        left, right, actual = [], [], []
        for j, xi, auxiliary in members:
            # Fixed coefficients include all frozen zeros; original row xi remains.
            coeff_left = [mul(ROOTS[k % 6], phase(frozen, c))
                          for k, c in enumerate(columns[:9])]
            coeff_right = [mul(ROOTS[(2*k+1) % 6], phase(frozen, c))
                           for k, c in enumerate(columns[:9])]
            phases = [conj(phase(auxiliary, c)) if reverse else phase(auxiliary, c)
                      for c in columns[:9]]
            l = total(mul(c, p) for c, p in zip(coeff_left, phases))
            r = total(mul(c, p) for c, p in zip(coeff_right, phases))
            left.append(l)
            right.append(r)
            w = (j % 4) if (sum(xi) % 5 != 0 and ideal_norm(xi) <= 500) else 0
            actual.append(tuple(w*a for a in mul(l, r)))
        chain = total(actual)
        check(norm2(chain) <= 9*sum(map(norm2, left))*sum(map(norm2, right)),
              "actual_weight_cauchy_before_positive_enlargement")


def beta(y, m):
    return max(y-m, Q(0), 5*y/6-2*m/3, y/3-m/6)


def phi(xs, m):
    radical = sum(xs)
    return min(radical-sum(xs[e-1] for e in selected)
               + beta(sum((6-e if reverse else e)*xs[e-1] for e in selected), m)
               for selected, reverse in product(SUBSETS, (False, True)))


d, r, m = Q(9, 25), Q(47752383, 67660000), Q(54905017, 135320000)
z, s = Q(995377467, 6766000000), Q(3, 15625)
g, mu = d*(r+z), Q(12288947, 169150000000)
kappa = Q(103, 200)
threshold = 5*kappa/6-2*m/3
target = 3*(1+d*m-s)-2*m
budget = target-(2*(1-mu)+g+d*m)
uniform = 1-5*kappa/6-Q(21,50)*(1+Q(73,100))/2 \
          -(Q(4,3)-2*Q(21,50))*Q(207,500)-3*Q(101,500000)
check(uniform == Q(4031,1500000), "same_uniform_eighth_sector_reserve")
check(budget-threshold == Q(7362652673,507450000000),
      "same_exact_eighth_sector_point_reserve")
for mm in (Q(2,5), m, Q(207,500)):
    for multiplier in (Q(0), Q(1,4), Q(1,2), Q(3,4), Q(1), Q(3,2), Q(2), Q(5,2)):
        y = multiplier*mm
        piece = (Q(0) if y <= mm/2 else y/3-mm/6 if y <= mm
                 else 5*y/6-2*mm/3 if y <= 2*mm else y-mm)
        check(beta(y, mm) == piece, "continuous_beta_piecewise_breakpoints")
    check(beta(kappa, mm) == 5*kappa/6-2*mm/3,
          "threshold_is_sixth_free_operator_cost")
    for xs in ((Q(1,2),0,0,0,0), (0,0,0,0,Q(1,10)),
               (Q(1,10),Q(1,5),0,0,0)):
        xs = tuple(map(Q, xs))
        reflected = xs[::-1]
        check(phi(xs, mm) == phi(reflected, mm), "global_conjugation_cost_invariance")
        for boundary in (Q(0), 5*kappa/6-2*mm/3):
            check((phi(xs, mm) <= boundary) != (phi(xs, mm) > boundary),
                  "exact_eighth_cut_complement")
        if sum((e+1)*x for e,x in enumerate(xs)) <= kappa:
            check(phi(xs, mm) <= 5*kappa/6-2*mm/3, "seventh_cut_subsumed")
        if sum((5-e)*x for e,x in enumerate(xs)) <= kappa:
            check(phi(xs, mm) <= 5*kappa/6-2*mm/3, "conjugate_physical_cap_subsumed")

old_xs = (Q(7,20),Q(1,10),Q(0),Q(0),Q(0))
new_xs = (Q(13,50),Q(4,25),Q(0),Q(0),Q(0))
old_cost, survivor_cost = phi(old_xs,m), phi(new_xs,m)
check(old_cost == Q(13,60)-m/6 and old_cost <= threshold,
      "note6_survivor_now_controlled")
check(budget-old_cost == Q(6124435399,253725000000),
      "note6_survivor_exact_new_reserve")
old_uniform = Q(47,60)-Q(21,50)*(1+Q(73,100))/2 \
              -(Q(11,6)-2*Q(21,50))*Q(207,500)-3*Q(101,500000)
check(old_uniform == Q(12281,1500000), "note6_survivor_uniform_new_reserve")
check(survivor_cost == Q(37,150)-m/6 and survivor_cost > threshold,
      "new_raw_survivor_exact_minimum")
check(survivor_cost-budget == Q(1487314601,253725000000),
      "new_raw_survivor_estimate_deficit")
for mm in (Q(2,5), m, Q(207,500)):
    check(phi(new_xs,mm) == Q(37,150)-mm/6, "new_survivor_minimum_across_coarse_wedge")
    check(phi(new_xs,mm)-(5*kappa/6-2*mm/3) == mm/2-Q(73,400),
          "new_survivor_outside_eighth_cut")
    # Even a separately justified cubic root-row sieve has zero cost for q.
    cubic_cost = max(Q(4,25)-mm, Q(0), (Q(8,25)-mm)/3)
    check(Q(13,50)+cubic_cost > phi(new_xs,mm),
          "powered_cubic_single_factor_scout_does_not_close_survivor")

prime_powers = (Q(21,50),Q(2,25),Q(1,2),Q(1,2),Q(13,50),Q(4,25))
u,h,v = (1,1,1,0,0,0), (1,1,0,1,0,0), (1,0,0,0,1,2)
check([sum(p*a for p,a in zip(prime_powers,row)) for row in (u,h,v)] == [Q(1)]*3,
      "new_survivor_physical_rows")
edges = [sum(p for p,a,b in zip(prime_powers,left,right) if a != b)
         for left,right in ((u,v),(v,h),(u,h))]
check(edges == [Q(1)]*3, "new_survivor_primitive_ratio_conductors")
check(sum(p for p,a in zip(prime_powers,v) if a) == Q(21,25)
      and Q(21,25) > 2*Q(207,500)-Q(1,1000), "new_survivor_original_gate")
check(sum((e+1)*x for e,x in enumerate(new_xs)) == Q(29,50) > kappa,
      "new_survivor_seventh_cut_complement")
check(min(edges)>Q(6,25) and min(edges[0]+edges[1],edges[0]+edges[2],edges[1]+edges[2])>Q(17,20)
      and edges[0]+edges[1]-edges[2]>Q(12,25) and min(edges[:2])>Q(39,100)
      and edges[0]+edges[1]>Q(103,100) and 2*(edges[0]+edges[1])-edges[2]>Q(15,8),
      "new_survivor_all_six_old_complements")

direct = run_direct_checks(check, Q)
record = {
    "metadata": {"date":"2026-10-09", "prepared_for":"Edward Baker",
                 "model":"GPT-6 (Codex), inherited configuration",
                 "configured_reasoning_effort":"not exposed; not inferred",
                 "assistance":"Substantial LLM assistance"},
    "assertions_total":sum(counts.values()), "assertions_by_group":dict(sorted(counts.items())),
    "formal_exterior_rows":len(ROWS), "subset_orientation_choices":2*len(SUBSETS),
    "nontrivial_complementary_power_zero_witnesses":deletion_witnesses,
    "eighth_sector_uniform_reserve":str(uniform),
    "eighth_sector_point_reserve":str(budget-threshold),
    "note6_survivor_new_cost":str(old_cost), "note6_survivor_new_reserve":str(budget-old_cost),
    "new_raw_survivor_cost":str(survivor_cost), "new_raw_survivor_estimate_deficit":str(survivor_cost-budget),
    "direct_fourth":direct,
    "limitations":["Formal zero-extended phases and rational budgets only.",
                   "No native reciprocity, presentation transfer, or asymptotic sieve certification.",
                   "No selected-bin population or actual weight lower bound.",
                   "Direct slot capacity is a favorable relaxation; actual J must be legal.",
                   "Lower-order scout is not a newly imported native operator.",
                   "No full mixed moment, zero-free improvement, or RH implication."]}
print(json.dumps(record,sort_keys=True,indent=2))
