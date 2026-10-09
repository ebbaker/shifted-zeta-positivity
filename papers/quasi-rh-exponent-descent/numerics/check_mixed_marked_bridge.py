#!/usr/bin/env python3
"""Small exact checks for the marked fourth bridge and native contour tests.

Prepared for Edward Baker, 9 October 2026, with GPT-6 (Codex).
Inherited effort configuration is not exposed; serving variant not inferred.
Finite identities and rational ledgers only, not a native moment certificate.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

count = 0

def check(condition):
    global count
    assert condition
    count += 1

def rec(x):
    return {"exact": str(x), "decimal": float(x)}

chi = F(1, 540)
budget_path = Path(__file__).with_name("mixed_operational_budget_record_20261009.json")
budget_bytes = budget_path.read_bytes()
budget_record = json.loads(budget_bytes)
continuous_sup = F(budget_record["continuous_certificate"]["chi_cap_supremum"]["exact"])
check(continuous_sup == F(43774520332379, 30789918900000000))
rho = F(1, 100000)
e = F(1, 1200000)
check(12 * e == rho)
gap = (1 - F(21, 50)) * F(7, 10) + 2 * F(2, 5) - 1 + chi
check(gap == F(103, 500) + chi)
check(gap > F(1, 5))
left, right = chi / (2 * F(73, 100)), chi / (2 * F(7, 10))
check(left == F(5, 3942))
check(right == F(1, 756))
check(F(17, 25) - right > F(1, 2))
check(2 * (F(17, 25) - right) > 1)
check(4 < 7)  # 2/sqrt(7)<1: native good-prime correction has no local zero.

# Conditional source-slot recipe: supply and capacities use their stated
# source ranges; no synthetic slot list is certified as an actual witness.
ell = F(1, 1000000)
hmax, nu_inverse, nu_fourth = ell / 4, ell / 2, F(1, 2000)
t_inverse_max = nu_inverse + hmax
qmax = F(21, 50) / 2
witness_cost = 2 * qmax * t_inverse_max
remaining_witness = ell - witness_cost
check(witness_cost == F(63, 200) * ell)
check(remaining_witness == F(137, 200) * ell)
positive_supply_lower = 2 * F(49, 100) * F(1, 5)
inverse_cap_upper = (1 - F(7, 10)) / 2
check(positive_supply_lower > inverse_cap_upper)
inverse_selected_lower = (1 - F(73, 100)) / 2 - t_inverse_max
fourth_cap_upper = 2 * (1 - 2 * F(2, 5)) / 9
check(inverse_selected_lower > fourth_cap_upper)
check(nu_fourth + hmax < F(1, 1000))
check(F(9, 2) * nu_fourth == F(9, 4000))
minimum_even_k = 1333334
check(2 * F(1, 6) / minimum_even_k < hmax)
check(2 * F(1, 6) / (minimum_even_k - 2) >= hmax)
fine_fourth_decrement = ell / 2
fine_fourth_shortfall = fine_fourth_decrement + hmax
fine_chi_upper = continuous_sup + F(21, 50) * fine_fourth_shortfall
fine_common = F(1, 700)
fine_chi_reserve = fine_common - fine_chi_upper
check(fine_fourth_shortfall == 3 * ell / 4)
check(fine_chi_upper == F(17513687662733, 12315967560000000))
check(fine_chi_reserve == F(563861960869, 86211772920000000))
check(fine_chi_reserve > 0)
check(F(9, 2) * fine_fourth_decrement == F(9, 4000000))
check(F(9, 25) / 125 - fine_common == F(127, 87500))
check(chi - fine_common == F(2, 4725))
check(F(103, 500) + fine_common == F(363, 1750))

# The three coprime local states and collision correction are compared
# before discarding either coefficient sign. Values are formal rational
# variables; they are not asserted to be native sextic character values.
values = [F(0), F(1, 8), -F(1, 8), F(1, 4), -F(1, 4)]
for x, y in product(values, repeat=2):
    correction = 1 - x * y / ((1 - x) * (1 - y))
    check((1 - x) * (1 - y) * correction == 1 - x - y)
    if x == 0 or y == 0:
        check(correction == 1)

# Ideal Mobius convolved with two unweighted ideal sums is the constant
# coefficient one. Prime valuations suffice by multiplicativity.
for exponent in range(21):
    coefficient = exponent + 1
    if exponent:
        coefficient -= exponent
    check(coefficient == 1)
for exponents in product(range(5), repeat=3):
    coefficient = 1
    for exponent in exponents:
        coefficient *= (exponent + 1) - (exponent if exponent else 0)
    check(coefficient == 1)

# Annular prime-product identity. Independent prime ideal labels with
# norms 13,7,7 can occur over the Eisenstein field. This is a finite
# coefficient check, not a scale/witness realization of the working bin.
norms = [13, 7, 7]
def norm(exponents):
    result = 1
    for p, exponent in zip(norms, exponents):
        result *= p ** exponent
    return result

def mu(exponents):
    if any(exponent > 1 for exponent in exponents):
        return 0
    return (-1) ** sum(exponents)

def inverse_profile(n):
    return int(F(9, 10) * 13 <= n <= F(11, 10) * 13)

def plain_profile(n):
    return int(F(9, 10) * 7 <= n <= F(11, 10) * 7)

allocations = []
weighted = unweighted = 0
for owners in product(range(3), repeat=3):
    vectors = [tuple(int(owner == slot) for owner in owners)
               for slot in range(3)]
    d, k, l = vectors
    contribution = mu(d) * inverse_profile(norm(d)) * plain_profile(norm(k)) * plain_profile(norm(l))
    weighted += contribution
    unweighted += mu(d)
    if contribution:
        allocations.append({"owners": list(owners), "coefficient": contribution})
check(unweighted == 1)
check(weighted == -2)
check(len(allocations) == 2)

# Strict high-response threshold and exact layer-integration identity.
q_values = [F(0), F(1, 2), F(1), F(3, 2), F(2)]
weights = [F(3, 2), F(2), F(1, 3), F(7, 4), F(1, 5)]
for threshold in [F(0), F(1, 2), F(1), F(3, 2), F(2)]:
    endpoints = sorted({threshold, max(q_values)} |
                       {q for q in q_values if q >= threshold})
    integral = F(0)
    for lower, upper in zip(endpoints, endpoints[1:]):
        middle = (lower + upper) / 2
        tail_mass = sum(v for q, v in zip(q_values, weights) if q > middle)
        integral += (upper - lower) * tail_mass
    low = sum(v * min(q, threshold) for q, v in zip(q_values, weights))
    check(low + integral == sum(v * q for q, v in zip(q_values, weights)))

# The unchanged first-transform ledger adds one mixed allowance.
for c, d, rad, complementary, p, s, q in [
    (F(0), F(0), F(0), F(0), F(0), F(0), F(0)),
    (F(3, 10), F(1, 10), F(1, 10), F(0), F(1, 10), F(1, 100), F(0)),
]:
    a, row, allowance = F(31, 20), F(1), F(1, 4)
    bc = max(F(0), (3 * c - 5 * d - rad) / 6)
    bd = max(F(0), (3 * d - 5 * c - rad) / 6)
    moving = q + rad + complementary
    result = row - a - rad / 2 - complementary + p + s + (
        2 * a - c - d + 2 * moving + bc + bd - 2 * s + 2 * allowance) / 2
    ledger = row + q + allowance + (bc + bd - (c + d - 2 * p - rad)) / 2
    check(result == ledger)

record = {
    "status": "finite identities and rational diagnostics only; mixed estimate remains open",
    "assertions": count,
    "source_pdf_sha256": "8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7",
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "operational_budget_record_sha256": hashlib.sha256(budget_bytes).hexdigest(),
    "unchanged_diagonal_budget_gap_lower": rec(gap),
    "symmetric_contour_shift_range": {
        "strict_lower": rec(left), "upper": rec(right)},
    "buffer": {"e_max": rec(e), "rho_12e_max": rec(rho)},
    "conditional_source_slot_recipe": {
        "max_original_slot_width": rec(hmax),
        "inverse_capacity_decrement": rec(nu_inverse),
        "inverse_shortfall_upper": rec(t_inverse_max),
        "fourth_capacity_decrement": rec(nu_fourth),
        "fourth_strict_margin": rec(F(9, 4000)),
        "witness_rounding_cost_upper": rec(witness_cost),
        "remaining_witness_loss_budget": rec(remaining_witness),
        "minimum_even_K_for_width_only_at_geometry_ell_1_6": minimum_even_k,
        "finer_fourth_decrement": rec(fine_fourth_decrement),
        "finer_fourth_shortfall_upper": rec(fine_fourth_shortfall),
        "finer_fourth_strict_margin": rec(F(9, 4000000)),
        "finer_fourth_chi_upper": rec(fine_chi_upper),
        "finer_common_sufficient_saving": rec(fine_common),
        "finer_common_saving_reserve": rec(fine_chi_reserve),
        "scope": "conditional on source supply L>1/5, amplitude bins, global beta<=7/8, and all shape/height inputs; K must also satisfy the moment mesh",
    },
    "annular_prime_product": {
        "norms": norms, "full_convolution": unweighted,
        "annular_convolution": weighted, "allocations": allocations,
        "scope": "finite coefficient algebra only, no working-bin or native-row realization"},
    "limitations": [
        "No all-height reciprocal control below the buffered line.",
        "No evaluated physical slot or simultaneous witness manifest.",
        "No lower bound for the actual selected energy or the full Gauss norm.",
        "Formal rational Euler variables are not native residue-symbol data.",
    ],
}
print(json.dumps(record, indent=2, sort_keys=True))
