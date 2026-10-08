#!/usr/bin/env python3
"""Exact exponent checks for selector and live-divisor continuation notes.

Prepared for Edward Baker, 2026-10-08, with GPT-6 (Codex) assistance.
Exact serving variant and configured reasoning effort are not exposed.
No finite computation here proves analytic cancellation or profile mass.
"""
from fractions import Fraction as F
from itertools import product
import json


def record(value):
    return {"exact": str(value), "decimal": float(value)}


eta = F(1, 5000)
ds = (F(9, 25), F(21, 50))
rs = (F(7, 10), F(37, 50))
ms = (F(9, 25), F(1, 2))
corners = list(product(ds, rs, ms))
gap, mean_zero, sigma_required, inverse_budget, endpoint_cost = [], [], [], [], []
for delta, r, m in corners:
    z = (1-r)/2  # capacity endpoint; actual strict decrement is rho > 0
    K = 1 + delta*m - eta
    B6 = K - m - z
    assert B6 == 1 - (1-delta)*m - z - eta
    available_inverse = F(1, 6) + 3*r/4
    difference = available_inverse - B6
    assert difference == (1-delta)*m+r/4-F(1, 3)+eta
    gap.append(difference)
    inverse_budget.append(B6)
    margin = K - (F(1, 6)+r-m+z)
    assert margin == F(1, 3)-r/2+(1+delta)*m-eta
    mean_zero.append(margin)
    sigma = F(3, 4)+(F(1, 3)-(1-delta)*m-eta)/(2*r)
    assert F(1, 6)+(2*sigma-1)*r+m+z == K
    assert sigma < F(7, 8)
    sigma_required.append(sigma)
    endpoint_cost.append(m-delta*m+eta)

# The gap and mean-zero expressions are monotone separately in every
# variable. For sigma_required the numerator 1/3-(1-delta)m-eta is
# positive throughout the box, so it decreases with r and m, increases
# with delta. Thus these corner extrema certify the continuous box.
assert min(F(1, 3)-(1-d)*m-eta for d, _, m in corners) > 0
assert (min(gap), max(gap)) == (F(19, 375), F(1289, 7500))
assert min(mean_zero) == F(6791, 15000)
assert (min(sigma_required), max(sigma_required)) == (
    F(16847, 22200), F(3523, 4200))
assert (min(inverse_budget), max(inverse_budget)) == (
    F(2649, 5000), F(661, 1000))
assert (min(endpoint_cost), max(endpoint_cost)) == (
    F(209, 1000), F(1601, 5000))
assert min(r+m for r in rs for m in ms) == F(53, 50)

# Check the live-label change as polynomial identities, comparing
# coefficients in formal variables (L, beta, V, lambda, z_n, 1).
def plus(*polys):
    return tuple(sum(entries) for entries in zip(*polys))


def scale(c, poly):
    return tuple(c*x for x in poly)


L, beta, V, lam, zn, one = [tuple(F(int(i == j)) for j in range(6))
                           for i in range(6)]
R = plus(L, scale(-1, beta), scale(-1, V))
M = plus(scale(2, L), scale(-2, beta), scale(-1, one))
Ftotal = plus(R, V)
new_R, new_V = plus(R, scale(-1, lam)), plus(V, lam)
assert plus(new_R, new_V) == Ftotal
kappa = plus(one, scale(-2, L), beta)
assert plus(kappa, beta, scale(2, Ftotal)) == one
first = plus(Ftotal, scale(-1, M), scale(-1, zn), scale(-1, beta))
second = plus(scale(4, Ftotal), scale(-3, M), scale(-6, zn))
assert first == plus(one, scale(-1, L), scale(-1, zn))
assert second == plus(scale(3, one), scale(-2, L), scale(2, beta), scale(-6, zn))

result = {
    "status": "exact budget and polynomial identities only; mixed saving unproved",
    "sixth_power_available_minus_required_at_rho_zero": {
        "min": record(min(gap)), "max": record(max(gap)),
        "rho_dependence": "subtract rho from both extrema",
    },
    "inverse_average_budget_at_rho_zero": {
        "min": record(min(inverse_budget)), "max": record(max(inverse_budget)),
        "rho_dependence": "add rho",
    },
    "mean_zero_principal_layer_min_margin": record(min(mean_zero)),
    "pointwise_sigma_budget_at_rho_zero": {
        "min": record(min(sigma_required)), "max": record(max(sigma_required)),
        "interpretation": "sufficient pointwise budget, not a proved or required zero-free theorem",
    },
    "plain_divisor_endpoint_cauchy_excess": {
        "min": record(min(endpoint_cost)), "max": record(max(endpoint_cost)),
        "interpretation": "hypothetical canonical bound; its actual width hypotheses fail",
    },
    "live_label_identities": {
        "F_unchanged": True, "kappa_plus_beta_plus_2F": "1",
        "first_width_margin": "1-L-z_n",
        "second_width_margin": "3-2L+2beta-6z_n",
        "uniform_upper_bound_first_margin": record(F(-3, 50)),
    },
    "proof_scope": "continuous extrema by stated monotonicity; exact polynomial coefficient comparison",
}
print(json.dumps(result, indent=2, sort_keys=True))
