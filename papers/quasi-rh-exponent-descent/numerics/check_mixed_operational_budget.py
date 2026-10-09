#!/usr/bin/env python3
"""Exact operational fourth-budget certificate; no moment estimate is proved.

Prepared for Edward Baker, 9 October 2026, with GPT-6 (Codex), inherited
configuration; exact serving variant and reasoning effort are not exposed.
Only the standard library is required. Output is a small deterministic record.
An optional --slots JSON evaluates a supplied fixed ORIGINAL slot list; its
arithmetic success does not verify source profile/mesh/witness hypotheses.
"""
from fractions import Fraction as F
from itertools import combinations
from dataclasses import dataclass
import argparse
import json
from pathlib import Path

ETA, ELL = F(1, 5000), F(1, 1000000)
D0, D1, X0, X1 = F(9, 25), F(21, 50), F(49, 100), F(1, 2)
TI, SHORTFALL, COMMON = ELL / 2, F(1, 1000), F(1, 540)


def rec(value):
    return {"exact": str(value), "decimal": float(value)}


def scalar(d, x):
    a = F(5, 6) - d
    b = 2 - F(8, 9) * x
    dx = 3 - F(17, 9) * x
    p = b * (1 - x)
    j = a * dx + d * p
    f = a * b / j
    rs = 1 - d + a * d * p / (2 * j)
    rn = 1 - f / 2 - (1 - f) * ETA / (d * (1 - x))
    mn = F(1, 2) - a / j * ((1 - x) / 2 - ETA / d)
    return dict(a=a, b=b, dx=dx, p=p, j=j, f=f, rs=rs, rn=rn, mn=mn)


def budget(d, x, ar, bm, ti=TI, h=F(0)):
    q = scalar(d, x)
    r, m = q["rn"] + ar, q["mn"] - bm
    s = ETA - d * (1 - x) * ar + ELL
    z = (1 - r) / 2 - ti
    g = d * (r + z)
    mu0 = 1 - q["rs"] - ELL - g
    mu = max(F(0), mu0)
    cm = 2 * (1 - 2 * m) / 9
    dc = 2 * d * m + d * cm - g
    raw = 2 * s - mu - dc
    chi = max(F(0), raw + d * h)
    return dict(r=r, m=m, s=s, z=z, g=g, mu0=mu0, mu=mu,
                cm=cm, d_cap=dc, raw_chi_cap=raw, chi=chi,
                halfcap_reserve=d * r - chi - F(1, 4),
                mass_closes=(mu >= s),
                h_half_limit=r - 1 / (4 * d) - raw / d)


def upper_formula(d, x):
    q = scalar(d, x)
    geom = 5 * q["a"] * (1 - 2 * x) / (18 * q["j"]) * (
        d - 2 * ETA / (1 - x))
    cmax = geom + (28 * ETA + 37 * ELL) / (18 * (1 - x)) + (
        14 * ELL / 9 - TI) * d
    cmin = max(F(0), geom - 5 * ELL * (1 - 2 * x) / (
        9 * q["b"] * (1 - x)) - d * TI)
    gam = d - F(1, 4) - q["a"] * (23 - 18 * x) / (
        18 * q["j"]) * (d - 2 * ETA / (1 - x)) - (
        28 * ETA + 19 * ELL) / (18 * (1 - x)) - (
        14 * ELL / 9 - TI) * d
    return cmin, cmax, gam


def continuous_certificate():
    # Monotonicity is proved on the continuous box by rational envelope
    # inequalities, not by checking a parameter grid.
    amin, amax = F(5, 6) - D1, F(5, 6) - D0
    bmin, bmax = 2 - F(8, 9) * X1, 2 - F(8, 9) * X0
    dxmin, dxmax = 3 - F(17, 9) * X1, 3 - F(17, 9) * X0
    pmin, pmax = bmin * (1 - X1), bmax * (1 - X0)
    jmin, jmax = amin * dxmin + D0 * pmin, amax * dxmax + D1 * pmax
    vmin, vmax = 2 * ETA / (1 - X0), 2 * ETA / (1 - X1)
    # Q=a(d-v)/J: Q_d=(a^2 D_x-d^2 P_x+(5/6)P_x v)/J^2.
    qd_numerator_lower = amin ** 2 * dxmin - D1 ** 2 * pmax
    assert qd_numerator_lower > 0
    # The last positive term is omitted in this numerator lower bound.
    jx_abs_upper = F(17, 9) * amax + D1 * (F(26, 9) - F(16, 9) * X0)
    cx_upper = F(5, 18) * (
        -2 * amin * (D0 - vmax) / jmax
        + amax * (1 - 2 * X0) * (D1 - vmin) * jx_abs_upper / jmin ** 2
    ) + (28 * ETA + 37 * ELL) / (18 * (1 - X1) ** 2)
    assert cx_upper < 0
    c_d_lower = 14 * ELL / 9 - TI
    assert c_d_lower > 0
    # A=-18J-(23-18x)J_x; its d coefficient decreases with x.
    coefficient_derivative_upper = -F(368, 9) + 32 * X1
    a_poly_lower = -F(475, 54) + D0 * (
        41 - F(368, 9) * X1 + 16 * X1 ** 2)
    assert coefficient_derivative_upper < 0 and a_poly_lower > 0
    # Gamma_x=-a*A*(d-v)/(18J^2)
    #          +[2 eta*a*(23-18x)/J-(28 eta+19 ell)]/[18(1-x)^2].
    kmax = 23 - 18 * X0
    ratio_upper = kmax / dxmin  # a K/J <= K/D_x
    gx_second_numerator_upper = 2 * ETA * ratio_upper - (28 * ETA + 19 * ELL)
    assert gx_second_numerator_upper < 0
    # 0<Q_d<a/J<=1/D_x gives Gamma_d>1-c-K/(18D_x).
    gd_lower = 1 - (14 * ELL / 9 - TI) - kmax / (18 * dxmin)
    assert gd_lower > F(1, 2)
    # Feasible u_min=v_L-ell. Its dr-1/4 branch exceeds the upper-corner
    # G(d,x) by L+(10eta+19ell)/(18(1-x))+d ell/18-ell/B_x.
    assert D0 * bmin == F(14, 25)
    first_branch_difference_lower = (10 * ETA + 19 * ELL) / (
        18 * (1 - X0)) + D0 * ELL / 18 - ELL / bmin
    assert first_branch_difference_lower > 0
    fmax, fmin = scalar(D0, X1)["f"], scalar(D1, X0)["f"]
    # F_d<0,F_x>0 (explicit derivative identities in the note).
    r_lower = 1 - fmax / 2 - (1 - fmin) * ETA / (
        D0 * (1 - X1)) - 39 * ELL / 14
    dr_minus_quarter_lower = D0 * r_lower - F(1, 4)
    chi_sup = upper_formula(D1, X0)[1]
    gamma_inf = upper_formula(D0, X1)[2]
    assert dr_minus_quarter_lower > gamma_inf > 0
    chi_whole_upper = chi_sup + D1 * SHORTFALL
    gamma_whole_lower = gamma_inf - D1 * SHORTFALL
    common_halfcap_lower = dr_minus_quarter_lower - COMMON
    assert chi_whole_upper < COMMON
    assert gamma_whole_lower > F(17, 5000)
    assert common_halfcap_lower > F(1, 500)
    # At ar_H the mu0 formula is strictly negative: both bracket terms
    # are negative and -ell[1+1/(2(1-x))]+d ti<0.
    mu_upper_bound = -ELL * (1 + 1 / (2 * (1 - X0))) + D1 * TI
    assert mu_upper_bound < 0
    return {
        "scope": "continuous closed operational wedge; t_I=ell/2; universal envelopes",
        "chi_cap_supremum": rec(chi_sup),
        "chi_cap_infimum": rec(F(0)),
        "halfcap_variable_chi_infimum": rec(gamma_inf),
        "fourth_whole_shortfall_cap": rec(SHORTFALL),
        "chi_whole_uniform_upper": rec(chi_whole_upper),
        "halfcap_variable_chi_whole_lower": rec(gamma_whole_lower),
        "common_sufficient_fourth_saving": rec(COMMON),
        "common_saving_halfcap_reserve_lower": rec(common_halfcap_lower),
        "common_saving_halfcap_reserve_comparison": "> 1/500",
        "uniform_scope_extension": "t_I>=ell/2, fixed available s and h_J<=1/1000, only when the actual witness budget still holds",
        "r_lower_for_common_target": rec(r_lower),
        "monotonicity_certificates": {
            "Q_d_numerator_lower": rec(qd_numerator_lower),
            "Cmax_x_derivative_upper": rec(cx_upper),
            "Cmax_d_derivative_lower": rec(c_d_lower),
            "Gamma_x_A_lower": rec(a_poly_lower),
            "Gamma_x_second_numerator_upper": rec(gx_second_numerator_upper),
            "Gamma_d_derivative_lower": rec(gd_lower),
            "Gamma_first_branch_difference_lower": rec(first_branch_difference_lower),
            "mu0_at_upper_ar_upper_bound": rec(mu_upper_bound),
        },
    }


@dataclass(frozen=True)
class Slot:
    name: str
    length: F
    envelope: F
    gain: F = F(0)  # Unsquared witness lower gain, supplied separately.


def exact_fourth_subset(slots, cap):
    """Pareto dynamic programming for fixed I; all original slots stay whole."""
    if cap < 0:
        raise ValueError("negative fourth capacity")
    if len({s.name for s in slots}) != len(slots):
        raise ValueError("slot IDs must be unique")
    if any(s.length < 0 for s in slots):
        raise ValueError("slot lengths must be nonnegative")
    # The dictionary keeps one deterministic witness for each reachable
    # length. Dominance pruning then retains only increasing envelopes.
    frontier = [(F(0), F(0), ())]
    for slot in slots:
        by_length = {length: (value, ids) for length, value, ids in frontier}
        for length, value, ids in frontier:
            newlen, newval = length + slot.length, value + slot.envelope
            if newlen <= cap:
                old = by_length.get(newlen)
                candidate = (newval, ids + (slot.name,))
                if old is None or candidate[0] > old[0] or (
                        candidate[0] == old[0] and candidate[1] < old[1]):
                    by_length[newlen] = candidate
        frontier, best = [], None
        for length, (value, ids) in sorted(by_length.items()):
            if best is None or value > best:
                frontier.append((length, value, ids))
                best = value
    return max(frontier, key=lambda item: (item[1], -item[0], tuple(reversed(item[2]))))


def brute_fourth_subset(slots, cap):
    candidates = []
    for size in range(len(slots) + 1):
        for inds in combinations(range(len(slots)), size):
            length = sum((slots[i].length for i in inds), F(0))
            value = sum((slots[i].envelope for i in inds), F(0))
            if length <= cap:
                candidates.append((length, value))
    bestvalue = max(value for _, value in candidates)
    return min(length for length, value in candidates if value == bestvalue), bestvalue


def slot_checks():
    # Formal arithmetic examples; no physical detector or profile realization.
    arbitrary = [Slot("a", F(6, 100), F(9, 100)),
                 Slot("b", F(5, 100), F(8, 100)),
                 Slot("c", F(4, 100), F(7, 100))]
    answer = exact_fourth_subset(arbitrary, F(9, 100))
    assert answer[:2] == brute_fourth_subset(arbitrary, F(9, 100))
    assert answer[2] == ("b", "c")  # A prefix taking a is not optimal.
    # Meaningful strict-boundary case: the sum 9/100 fits at the endpoint,
    # but must fail after a positive decrement; no fractional slot is used.
    strict = exact_fourth_subset(arbitrary, F(9, 100) - F(1, 1000000))
    assert strict[:2] == brute_fourth_subset(arbitrary, F(9, 100) - F(1, 1000000))
    assert strict[2] == ("a",)
    d, x, ar, bm = D0, X1, F(1, 20000), F(1, 40000)
    b = budget(d, x, ar, bm)
    width = b["z"] / 512
    slots = [Slot(f"s{i:03d}", width, d * width, d * x * width)
             for i in range(512)]
    decrement = F(1, 10000000)
    selected = exact_fourth_subset(slots, b["cm"] - decrement)
    assert selected[0] <= b["cm"] - decrement
    h = b["cm"] - selected[0]
    assert h <= decrement + width < SHORTFALL
    bj = budget(d, x, ar, bm, h=h)
    gain = sum((slot.gain for slot in slots), F(0))
    rn = scalar(d, x)["rn"]
    f = scalar(d, x)["f"]
    rnew = scalar(d, x)["rs"] - f * ETA
    witness_required = 1 - rnew - d * b["r"] - 2 * gain
    ideal_s0 = ETA - d * (1 - x) * (b["r"] - rn)
    assert witness_required == ideal_s0 + 2 * d * x * TI
    firstmargin = 1 - b["r"] - 2 * b["z"]
    secondmargin = 3 - 2 * b["r"] - 8 * b["z"]
    fourthmargin = 1 - 2 * b["m"] - F(9, 2) * selected[0]
    assert firstmargin == ELL and secondmargin > 0 and fourthmargin > 0
    assert bj["chi"] < COMMON
    assert d * b["r"] - COMMON - F(1, 4) > F(1, 500)
    return {
        "scope": "synthetic rational lengths/envelopes/gains only; source legality unverified",
        "nonuniform_envelope_counterexample": {
            "capacity": "9/100", "optimal_ids": list(answer[2]),
            "optimal_envelope": rec(answer[1]),
            "strict_decrement_optimal_ids": list(strict[2]),
        },
        "uniform_formal_list": {
            "slots": 512, "width": rec(width), "chosen_slots": len(selected[2]),
            "capacity_decrement": rec(decrement), "fourth_shortfall": rec(h),
            "first_inverse_capacity_margin": rec(firstmargin),
            "second_inverse_capacity_margin": rec(secondmargin),
            "fourth_capacity_margin": rec(fourthmargin),
            "witness_saving_required_before_other_losses": rec(witness_required),
            "remaining_fixed_witness_loss_budget": rec(b["s"] - witness_required),
            "chi": rec(bj["chi"]), "halfcap_reserve": rec(bj["halfcap_reserve"]),
        },
    }


def slice_records():
    out = []
    for d in (D0, F(39, 100), D1):
        for x in (X0, X1):
            b = budget(d, x, F(1, 20000), F(1, 40000))
            enlarged_total_deficit = budget(d, x, F(1, 20000), F(1, 40000),
                                            ti=3 * ELL / 4)
            assert enlarged_total_deficit["chi"] <= b["chi"]
            cmin, cmax, gam = upper_formula(d, x)
            ah = (ETA + ELL) / (d * (1 - x))
            lower = -ELL / (d * scalar(d, x)["b"])
            assert budget(d, x, ah, lower)["chi"] == cmin
            assert budget(d, x, ah, ah + ELL)["chi"] == cmax
            assert budget(d, x, ah, ah + ELL)["halfcap_reserve"] == gam
            out.append({"d": str(d), "x": str(x),
                        "central_slice_chi": rec(b["chi"]),
                        "central_slice_mu": rec(b["mu"]),
                        "fixed_dx_wedge_chi_min": rec(cmin),
                        "fixed_dx_wedge_chi_sup": rec(cmax),
                        "fixed_dx_wedge_halfcap_inf": rec(gam)})
    return out


def supplied_slots(path):
    spec = json.loads(Path(path).read_text())
    slots = [Slot(s["id"], F(s["length"]), F(s["envelope"]), F(s.get("gain", "0")))
             for s in spec["slots"]]
    cap = F(spec["capacity"]) - F(spec.get("capacity_decrement", "0"))
    length, envelope, ids = exact_fourth_subset(slots, cap)
    return {"arithmetic_only": True, "original_file": str(path),
            "provenance_assertions_not_verified": spec.get("source_provenance", {}),
            "selected_original_ids": list(ids), "length": rec(length),
            "envelope": rec(envelope), "effective_capacity": rec(cap)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slots", help="optional original fixed slot specification JSON")
    args = parser.parse_args()
    output = {
        "date": "2026-10-09",
        "model": "GPT-6 (Codex), inherited configuration; exact variant and effort not exposed",
        "status": "conditional exact budget certificate; no new asymptotic moment, witness realization, or zero-free boundary",
        "continuous_certificate": continuous_certificate(),
        "slice_comparisons": slice_records(),
        "finite_subset_checks": slot_checks(),
    }
    if args.slots:
        output["supplied_original_slots"] = supplied_slots(args.slots)
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
