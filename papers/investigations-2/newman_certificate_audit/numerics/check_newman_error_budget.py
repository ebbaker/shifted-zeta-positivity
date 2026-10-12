#!/usr/bin/env python3
"""Error-budget replay for the pinned de Bruijn-Newman certificate row.

Standard-library Python (decimal at 50 significant digits).  Deterministic.

Replays, from the published formulas of Polymath, "Effective approximation
of heat flow evolution of the Riemann xi function, and a new upper bound
for the de Bruijn-Newman constant" (arXiv:1904.12438v2), Theorem 1.3
bounds (20)-(24) and the refined Section 6 bounds for e_C and e_{C,0}
(displayed after (69)), the effective-approximation error budget consumed by
the finite final-time lane and by the closed barrier of the audited package

    judegomila/dbn-lambda-01787854-candidate-audit  @ a74738deb6d5e0f76887cb36901da08b68dca705

at its exact row  X = 6000000185827,  t0 = 129/800,  y0^2 = 87677/2500000,
N = 690988, and compares the "C dropped" budget (e_A+e_B+e_{C,0}) that the
package pays with the "C retained" budget (e_A+e_B+e_C) that the corrected
Riemann-Siegel interface of the repository (project 17, Notes 20-22) would
pay at the same points.

What this is: a high-precision floating replay of explicit closed-form
bounds, evaluated at points (not over boxes), with no interval arithmetic.
What it is not: a certificate.  The package's authoritative numbers are its
FLINT/Arb directed enclosures; agreement here is corroboration of the
transcription, not an independent proof of Theorem 1.3.

Usage:  python3 check_newman_error_budget.py [--output record.json]
"""
import argparse, hashlib, json, sys, platform
from decimal import Decimal as D, getcontext
from fractions import Fraction as F

getcontext().prec = 50

def dec(fr):
    return D(fr.numerator) / D(fr.denominator)

def atan_inv(n):
    """arctan(1/n) by its alternating series, n >= 2."""
    x = D(1) / D(n); x2 = x * x
    term = x; total = x; k = 1
    eps = D(10) ** (-(getcontext().prec + 5))
    while True:
        term *= x2
        k += 2
        delta = term / k
        if delta < eps:
            break
        total += -delta if (k // 2) % 2 else delta
    return total

PI = 16 * atan_inv(5) - 4 * atan_inv(239)

def ln(x):  return D(x).ln()
def exp(x): return D(x).exp()
def sqrt(x): return D(x).sqrt()
def powd(x, e): return exp(e * ln(x))

def budget(x, y, t, N, head=None, constant=D("10.44")):
    """Return dict of Theorem 1.3 / Section 6 bounds at the point (x, y, t, N).

    head: number of terms kept in the e_A+e_B sum (default all N)."""
    x, y, t = D(x), D(y), D(t)
    q = x / (4 * PI)
    lq = ln(q)
    gam = exp(D("0.02") * y - y * lq / 2)                      # (20)
    inner = 1 - 3 * y + 4 * y * (1 + y) / (x * x)
    inner = inner if inner > 0 else D(0)
    sigma = (1 + y) / 2 + t * lq / 4 - t * inner / (2 * x * x)  # (21)
    kappa = t * y / (2 * (x - 6))                              # (22)
    # (23): e_A + e_B
    M = N if head is None else min(N, head)
    Nk = powd(D(N), kappa)
    s = D(0)
    for n in range(1, M + 1):
        n_ = D(n); lnn = n_.ln()
        bn = exp(t * lnn * lnn / 4)
        arg = ((t * t / 16) * (lq - 2 * lnn) ** 2 + D("0.626")) / (x - D("6.66"))
        s += (1 + gam * Nk * exp(y * lnn)) * bn * exp(-sigma * lnn) * (exp(arg) - 1)
    eAB = s
    # Section 6 refined bounds (common prefactor)
    pref = powd(q, -(1 + y) / 4) * exp(-t * lq * lq / 16
                                       + (3 * sqrt(lq * lq + PI * PI / 4) + D("3.58")) / (x - D("8.52")))
    small = D("1.24") * (powd(D(3), y) + powd(D(3), -y)) / (D(N) - D("0.125")) + D("6.92") / (x - 12)
    eC = pref * small
    eC0 = pref * (1 + small)
    # Theorem 1.3 display (24) with the stated constant (10.44), and the package's weld (10.50)
    eC0_24 = powd(q, -(1 + y) / 4) * exp(-t * lq * lq / 16
                                         + D("1.24") * (powd(D(3), y) + powd(D(3), -y)) / (D(N) - D("0.125"))
                                         + (3 * sqrt(lq * lq + PI * PI / 4) + constant) / (x - 12))
    return dict(x=str(x), y=str(y), t=str(t), N=N, log_q=str(lq), gamma_bound=str(gam),
                re_s_lower=str(sigma), kappa_bound=str(kappa), eAB_terms=M, eAB=str(eAB),
                eC=str(eC), eC0_section6=str(eC0), eC0_display24=str(eC0_24),
                ratio_eC_over_eC0=str(eC / eC0))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=None)
    ap.add_argument("--head", type=int, default=None, help="truncate the e_A+e_B sum (replay speed)")
    a = ap.parse_args()

    X = 6000000185827
    t0 = F(129, 800); y0sq = F(87677, 2500000)
    y0 = sqrt(dec(y0sq)); t = dec(t0)
    N0 = 690988
    xN0 = 4 * PI * (D(N0) ** 2 - t / 16)         # window left edge x_N
    ymax = sqrt(dec(F(1, 1) - 2 * t0))

    rec = {"title": "Error-budget replay at the pinned certificate row",
           "date": "2026-10-12",
           "source_package": {"repository": "https://github.com/judegomila/dbn-lambda-01787854-candidate-audit",
                              "commit": "a74738deb6d5e0f76887cb36901da08b68dca705",
                              "commit_date": "2026-08-21T14:26:54-07:00"},
           "formulas": "Polymath arXiv:1904.12438v2 Theorem 1.3 (20)-(24); Section 6 refined e_C, e_{C,0}",
           "precision": "decimal, 50 significant digits, point evaluation, no interval arithmetic",
           "row": {"X": X, "t0": str(t0), "y0_squared": str(y0sq), "N0": N0,
                   "t0_plus_half_y0sq": str(t0 + y0sq / 2)},
           "package_certified_values": {
               "finite_lane_Tmin": "0.000000791366", "finite_lane_eAB_arb": "2.05702368866621449147357372171e-12",
               "finite_lane_eC0_arb": "2.33492848188649182679145092376e-7",
               "finite_lane_Emax_arb": "2.33494905212337848893636565949e-7",
               "barrier_eAB_arb": "<3.639278679550541e-10", "barrier_eC0_arb": "<0.000356522647672172",
               "barrier_total_arb": "<0.000356523011600040", "barrier_allowance": "0.00125",
               "barrier_min_prism_margin": ">=0.519849894613872543374989997",
               "note": "Arb values are directed enclosures over t-boxes/y-ranges; the replay below is pointwise"},
           "cases": {}}

    # 1. finite lane, first window, at y = y0 (the lane's weakest row) -- the lane evaluates at
    #    x = x_N (window left edge, conservative freeze) and y in [y0, ymax]; e_{C,0} is largest at y0.
    rec["cases"]["finite_first_window_y0"] = budget(xN0, y0, t, N0, head=a.head)
    rec["cases"]["finite_first_window_ymax"] = budget(xN0, ymax, t, N0, head=a.head)
    # 2. closed barrier box corner with the largest e_{C,0}: x = X, y = 0.1809, t = 0
    rec["cases"]["barrier_corner_t0_y_floor"] = budget(D(X), D("0.1809"), D(0), N0, head=a.head)
    rec["cases"]["barrier_corner_tfinal_y_floor"] = budget(D(X), D("0.1809"), t, N0, head=a.head)
    # 3. the repository's own calibration height for scale (Note 22): m = 22066, t = 1/(2 log m)
    m = 22066; tm = 1 / (2 * ln(D(m)))
    rec["cases"]["repository_note22_center"] = budget(4 * PI * D(m) ** 2, D("0.05"), tm, m, head=a.head)

    fw = rec["cases"]["finite_first_window_y0"]
    eC0 = D(fw["eC0_section6"]); eC = D(fw["eC"]); eAB = D(fw["eAB"])
    Tmin = D("0.000000791366")
    Emax_arb = D("2.33494905212337848893636565949e-7")
    # finite-difference sensitivities of the first-row lower bound L_N (float64 replay, see record)
    dL_dy2 = D("9.528")    # per unit y^2, from L(y^2 +/- 1e-4)
    dL_dt = D("19.058")    # per unit t,   from L(t +/- 1e-4)
    slack_now = Tmin - Emax_arb
    slack_corrected = Tmin - (eAB + eC)
    rec["benchmark"] = {
        "finite_lane_error_dropped_C": str(eAB + eC0),
        "finite_lane_error_retained_C": str(eAB + eC),
        "error_reduction_factor": str((eAB + eC0) / (eAB + eC)),
        "slack_Tmin_minus_Emax_package": str(slack_now),
        "slack_if_C_retained_pointwise": str(slack_corrected),
        "extra_slack": str(slack_corrected - slack_now),
        "sensitivity_dL_dy2_float64": str(dL_dy2), "sensitivity_dL_dt_float64": str(dL_dt),
        "max_gain_in_y0sq_if_all_extra_slack_spent": str((slack_corrected - slack_now) / dL_dy2),
        "max_gain_in_Lambda_via_y0": str((slack_corrected - slack_now) / dL_dy2 / 2),
        "max_gain_in_Lambda_via_t0": str((slack_corrected - slack_now) / dL_dt),
        "interpretation": "Even if the C-retained pointwise budget could be used in the finite lane "
                          "(it cannot, see note 2: the lane is uniform in x), the bound would move by "
                          "about 1e-8 in Lambda.  The barrier lane's prism margin (0.52) exceeds its "
                          "approximation allowance (0.00125) by a factor 400, so the correction cannot "
                          "change its feasibility or cost either."}
    rec["software"] = {"python": platform.python_version(), "implementation": platform.python_implementation()}
    with open(__file__, "rb") as fh:
        rec["checker_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    out = json.dumps(rec, indent=2)
    if a.output:
        with open(a.output, "w") as fh:
            fh.write(out + "\n")
        print(f"wrote {a.output}")
    else:
        print(out)

if __name__ == "__main__":
    main()
