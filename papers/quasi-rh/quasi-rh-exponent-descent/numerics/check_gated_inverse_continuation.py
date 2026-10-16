#!/usr/bin/env python3
"""Exact capacity, gate, paid-margin and positive-moment-envelope checks.

No character rows or zeros are synthesized. The extremizer is solely a
model of the named scalar positive-moment constraints, with their actual
original-slot capacities. It is not a native arithmetic counterexample.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

COUNT = 0
ETA, ELL = F(1, 5000), F(1, 10**6)


def check(value, message=""):
    global COUNT
    COUNT += 1
    if not value:
        raise AssertionError(message)


def params(d, x):
    a, B, D = F(5, 6)-d, 2-8*x/9, 3-17*x/9
    P, J = B*(1-x), a*D+d*B*(1-x)
    Fx = a*B/J
    Rstar = 1-d+a*d*P/(2*J)
    Rnew = Rstar-Fx*ETA
    rnew = 1-Fx/2-(1-Fx)*ETA/(d*(1-x))
    mnew = F(1, 2)-a/J*((1-x)/2-ETA/d)
    check(1-d*(x+(1-x)*rnew) == Rnew+ETA)
    check(1-d*(4*x/9+B*mnew) == Rnew)
    return B, D, Fx, Rstar, Rnew, rnew, mnew


def below_capacity(cap, width, decrement):
    # Largest whole cardinality at or below a strictly shortened capacity.
    target = max(F(0), cap-decrement)
    return target // width


def one_case(d, x):
    B, D, Fx, Rstar, Rnew, rnew, mnew = params(d, x)
    low = (Fx*ETA+ELL)/(d*B)
    high = (ETA-Fx*ETA-ELL)/(d*(1-x))
    check(0 < low < high < (ETA+ELL)/(d*(1-x)))
    ar = (low+high)/2
    bm = ar  # The exact simultaneous detector support boundary r+m=tnew.
    r, m = rnew+ar, mnew-bm
    check(F(7, 10) < r < F(73, 100))
    check(F(2, 5) < m < F(207, 500))
    check(ar > -F(39, 14)*ELL)
    check(bm > -ELL/(d*B) and bm <= ar+ELL)
    zM, zP, zS = (1-r)/2, 2*(1-2*m)/9, 2*(1-m)/9
    check(zP < zM < F(3, 20))
    check(zM < (3-2*r)/8)
    q, R = d*x, Rstar+ELL
    AI = 1-d*r-2*q*zM
    PP = 1-2*d*m-2*q*zP
    PS = 1-d*m-2*q*zS
    check(AI > R and PP > R)
    check(PS > PP)
    rho = min(R, AI, PP, PS)
    check(rho == R)
    check(rho-Rnew == Fx*ETA+ELL)

    # A source-compatible fine original width. The moment mesh is a
    # separate imported requirement; this illustration does not fix it.
    width, L = ELL/8, F(1, 4)
    K = L // width
    check(K % 2 == 0 and L > F(1, 5))
    nI = below_capacity(zM, width, ELL/2)
    zI = nI*width
    tI = zM-zI
    check(ELL/2 <= tI <= 5*ELL/8)
    check(r+2*zI < 1 and 2*r+8*zI < 3)
    nJ = below_capacity(zP, width, ELL/8)
    zJ = nJ*width
    check(nJ < nI and zP-zJ <= ELL/4)
    check(2*m+F(9, 2)*zJ < 1)

    # Every legal original-slot subset is covered analytically by its
    # total cardinality: q is constant, so the endpoint is the strongest.
    for power, cap in [(1, zS), (2, zP)]:
        maxn = below_capacity(cap, width, ELL/16)
        for n in [0, 1, maxn//2, maxn-1, maxn]:
            zz = n*width
            check(power*m+F(9, 2)*zz < 1)
            check(rho+power*d*m+2*q*zz < 1)
    maxn = below_capacity(zM, width, ELL/16)
    for n in [0, 1, maxn//2, maxn-1, maxn]:
        zz = n*width
        check(r+2*zz < 1 and 2*r+8*zz < 3)
        check(rho+d*r+2*q*zz < 1)
    # Grant the stronger continuous endpoint moments as well.
    check(rho+d*r+2*q*zM <= 1)
    check(rho+2*d*m+2*q*zP <= 1)
    check(rho+d*m+2*q*zS <= 1)

    # The exact optimal scalar envelope for the gated inverse energy.
    GI, GM, GP = q*zI, q*zM, q*zP
    g_bin = 1-R-d*r-2*GI
    g_extension = 2*(GM-GI)
    g_fourth = 2*d*m-d*r-2*(GI-GP)
    g_second = d*m-d*r-2*(GI-q*zS)
    g_best = max(0, g_bin, g_extension, g_fourth, g_second)
    g_need = 1-Rnew-d*r-2*GI
    check(g_best == 1-rho-d*r-2*GI)
    check(g_need-g_best == Fx*ETA+ELL)

    # Hölder products of ALL these positive constraints cannot improve
    # the bound: the one-level extremizer satisfies each one exactly or
    # with slack. Check interpolated plain powers throughout [1,2].
    for t in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
        power = 1+t
        cap = (1-t)*zS+t*zP
        check(rho+power*d*m+2*q*cap <= 1)
        check(power*d*m-d*r-2*(GI-q*cap) <= g_best)

    return {"d": str(d), "x": str(x), "r": str(r), "m": str(m),
            "support_boundary_a_r_b_m": str(ar),
            "central_interval_lower": str(low), "central_interval_upper": str(high),
            "central_interval_width": str(high-low),
            "positive_moment_count_exponent": str(rho),
            "target_count_exponent": str(Rnew),
            "best_positive_gated_mass_gain": str(g_best),
            "needed_gated_mass_gain": str(g_need),
            "remaining_exponent_deficit": str(g_need-g_best),
            "illustrative_original_slot_count": int(K),
            "whole_inverse_slot_count": int(nI), "whole_plain_fourth_slot_count": int(nJ)}


def continuous_ledger():
    dlo, dhi = F(9, 25), F(21, 50)
    Bmin, Bmax = F(14, 9), F(352, 225)
    Dmin, Dmax = F(37, 18), F(1867, 900)
    Jmax = (F(5, 6)-dlo)*Dmax+dhi*Bmax*F(51, 100)
    c_minus_F_lower = dlo*Bmin**2*F(1, 2)/(Dmax*Jmax)
    width_lower = Dmin*(ETA*c_minus_F_lower-ELL)/(dhi*Bmax*F(51, 100))
    check(width_lower == F(9483150683821, 50056274942682624))
    check(width_lower > F(1, 6000))
    Fmin = F(1091200, 2012413)
    deficit_lower = Fmin*ETA+ELL
    check(deficit_lower > F(109, 10**6))
    # Rounded original physical prefixes, with extra literal losses <=ell/4.
    inverse_round = dhi*3*ELL/4
    plain_round = dhi*3*ELL/8
    inverse_reserve = 3*ELL/4-inverse_round-ELL/4
    plain_reserve = 3*ELL/4-plain_round-ELL/4
    check(inverse_reserve == 37*ELL/200)
    check(plain_reserve == 137*ELL/400)
    # Effective gate loss <=ell/4 leaves strict room at this stronger
    # conductor frontier; fixed constants are absorbed at the threshold.
    new_conductor_width = ELL/(2*dlo)
    check(new_conductor_width == F(1, 720000))
    check(new_conductor_width < F(1, 1000))
    check(ELL/4 < dlo/F(1000))
    return {"central_interval_width_uniform_lower": str(width_lower),
            "central_count_deficit_uniform_lower": str(deficit_lower),
            "c_minus_F_uniform_lower": str(c_minus_F_lower),
            "effective_gate_loss_assumed_upper": str(ELL/4),
            "forced_conductor_frontier_width": str(new_conductor_width),
            "extra_count_loss_assumed_upper": str(ELL/4),
            "paid_inverse_sliver_reserve": str(inverse_reserve),
            "paid_plain_sliver_reserve": str(plain_reserve)}


def main():
    cases = [one_case(d, x) for d, x in itertools.product(
        [F(9, 25), F(39, 100), F(2, 5), F(21, 50)],
        [F(49, 100), F(99, 200), F(1, 2)])]
    ledger = continuous_ledger()
    record = {"date": "2026-10-09", "assertions": COUNT,
              "scope": "Exact scalar consequences of named native marginal moments and original-slot capacities. No native row realization, new arithmetic tail saving, or zero-free theorem is proved.",
              "cases": cases, "continuous_ledger": ledger,
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out = Path(__file__).with_name("gated_inverse_continuation_record_20261009.json")
    out.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n")
    print(f"{COUNT} assertions passed; wrote {out.name}")
    print(f"Central-band width > 1/6000; remaining deficit >= {ledger['central_count_deficit_uniform_lower']}")
    print("Gated rows force conductor exponent > 2m-1/720000 under the stated loss budget")


if __name__ == "__main__":
    main()
