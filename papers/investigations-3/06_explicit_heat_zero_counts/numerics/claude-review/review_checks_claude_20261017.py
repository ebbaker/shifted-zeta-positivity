#!/usr/bin/env python3
"""Independent review checks for Investigation 06 (explicit heat zero counts).

Prepared for Edward Baker with LLM assistance, 17 October 2026.
Model: Claude Opus 5.5 (configured identifier claude-opus-5-5), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier. Support computations for
reviews/02_CROSS_MODEL_REVIEW_NOTES_01_02_AND_MANUSCRIPT_CLAUDE_20261017.md.

Depends on mpmath only. Imports nothing from the project's programs and does
not reuse their constants except where a section states that it tests one.
Every section prints what it checks and has a pass condition that can fail;
--inject-normalization deliberately uses the wrong heat coefficient
exp(t*alpha^2/2) in the carrier and must make section A fail (exit 1).

Sections
  A  Direct off-axis comparison at points of the claimed domain: H_t from the
     heat-kernel convolution of xi (Polymath (35)), against the carrier
     M_t(s_+) and against the Riemann-Siegel main-term approximant.
  B  The comparison disk at a stress point where the dominant Dirichlet
     polynomial is nearly aligned: circle maximum, Cauchy-integral estimate
     of F'/F at the centre, the Poisson sum D_t(U), and the implied count.
  C  Sampled checks of the elementary carrier inequalities used in Note 02
     (equations (4), (5), (6), (15), (16), (17)) and in the Note 01 lemma.
  D  The Gaussian moment formula (9) against quadrature, and the claimed
     factor below 2.
  E  Source observations: the constant before Polymath (60), the t/2 versus
     t/4 heat coefficient after (99), and the fixed-index remainder RS_m.
  F  Benchmarks: the true density, the theorem's bound, and an explicit t=0
     unit-window bound (Bellotti-Wong, arXiv:2412.15470v2, Corollary 1.6).
  G  Reviewer arithmetic (planning numbers, not proofs): the cutoff at which
     the notes' own ingredients close the comparison budget when the
     remainder constant is tracked in a, and the constants a disk band
     y in [4,5] would give.

Status: floating diagnostics at 30-60 significant digits. Sampled checks do
not prove universal inequalities; the quadrature in A and B is not outward
rounded. Nothing here certifies the theorem or says anything about RH.
"""

import argparse
import hashlib
import json
import platform
import sys
import time

import mpmath as mp

# ---------------------------------------------------------------- carriers

def xi(s):
    return s * (s - 1) / 2 * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def M0(s):
    return (s * (s - 1) / 16 * mp.power(mp.pi, -s / 2) * mp.sqrt(2 * mp.pi)
            * mp.exp((s / 2 - mp.mpf(1) / 2) * mp.log(s / 2) - s / 2))


def alpha(s):
    return 1 / (2 * s) + 1 / (s - 1) + mp.log(s / (2 * mp.pi)) / 2


def alpha_prime(s):
    return -1 / (2 * s * s) - 1 / (s - 1) ** 2 + 1 / (2 * s)


HEAT_COEFF = {"value": mp.mpf(1) / 4}   # 1/2 under --inject-normalization


def Mt(s, t):
    return mp.exp(HEAT_COEFF["value"] * t * alpha(s) ** 2) * M0(s)


def H_conv(t, z, h=mp.mpf('0.25'), vlo=-16, vhi=12):
    """H_t(z) = int (1/8) xi((1+iz)/2 + sqrt(t) v) e^{-v^2}/sqrt(pi) dv (trapezoid)."""
    s0 = (1 + 1j * z) / 2
    st = mp.sqrt(t)
    n = int(mp.nint((vhi - vlo) / h))
    tot = mp.mpc(0)
    for k in range(n + 1):
        v = vlo + k * h
        tot += mp.exp(-v * v) * xi(s0 + st * v) / 8
    return tot * h / mp.sqrt(mp.pi)


def main_terms(t, z):
    """Riemann-Siegel main-term approximant to H_t/M_t(s_+), with its parts."""
    x, y = mp.re(z), mp.im(z)
    sp = mp.mpc((1 + y) / 2, -x / 2)
    sm = mp.mpc((1 - y) / 2, x / 2)
    N = int(mp.floor(mp.sqrt(x / (4 * mp.pi) + t / 16)))
    ap, am = alpha(sp), alpha(sm)
    dom = mp.mpc(0)
    opp = mp.mpc(0)
    majorant = mp.mpf(0)
    for n in range(1, N + 1):
        b = mp.exp(t * mp.log(n) ** 2 / 4)
        dom += b * mp.power(n, -sp - t * ap / 2)
        opp += b * mp.power(n, -sm - t * am / 2)
        if n >= 2:
            majorant += b * mp.power(n, -mp.re(sp) - t * mp.re(ap) / 2)
    gam = Mt(sm, t) / Mt(sp, t)
    return {"N": N, "f": dom + gam * opp, "dominant_excess": dom - 1,
            "opposite": gam * opp, "dominant_majorant": majorant}


def F_direct(t, z, **kw):
    sp = (1 - 1j * z) / 2
    return H_conv(t, z, **kw) / Mt(sp, t)


BUDGET = mp.mpf(96624791) / 147000000      # Theorem 1.2 of the manuscript


def fl(v, d=12):
    return mp.nstr(v, d)


# ---------------------------------------------------------------- sections

def section_A(results, quick):
    mp.mp.dps = 30
    rows = []
    ok = True
    xs = [mp.mpf(2_000_000), mp.mpf(10_000_000)]
    ys = [mp.mpf(3), mp.mpf('3.5'), mp.mpf(4)]
    ts = [mp.mpf('1e-4'), mp.mpf('0.05'), mp.mpf('0.25'), mp.mpf('0.5')]
    if quick:
        xs, ys, ts = xs[:1], [mp.mpf(3)], [mp.mpf('1e-4'), mp.mpf('0.5')]
    # stress point: dominant Dirichlet polynomial nearly aligned at y=3
    stress_x = mp.mpf('2324466.298474')
    pts = [(x, y, t) for x in xs for y in ys for t in ts]
    pts += [(stress_x, mp.mpf(3), mp.mpf('1e-4')), (stress_x, mp.mpf(3), mp.mpf('0.05'))]
    for (x, y, t) in pts:
        z = mp.mpc(x, y)
        F = F_direct(t, z)
        mt = main_terms(t, z)
        allowance = mp.mpf(1) / 25000 + 26 / x
        row = {"x": fl(x, 13), "y": fl(y, 3), "t": fl(t, 3), "N": mt["N"],
               "abs_F_minus_1": fl(abs(F - 1)),
               "abs_F_minus_main_terms": fl(abs(F - mt["f"]), 6),
               "allowance_ordinary_plus_remainder": fl(allowance, 6),
               "abs_dominant_excess": fl(abs(mt["dominant_excess"])),
               "dominant_majorant": fl(mt["dominant_majorant"]),
               "abs_opposite_branch": fl(abs(mt["opposite"]), 6)}
        row["pass"] = bool(abs(F - 1) < BUDGET and abs(F - mt["f"]) < allowance
                           and mt["dominant_majorant"] <= mp.zeta(2) - 1
                           and abs(mt["opposite"]) < mp.mpf(11) / 1000)
        ok &= row["pass"]
        rows.append(row)
        print("A", row, flush=True)
    # quadrature convergence at two points
    conv = []
    for (x, y, t) in [(mp.mpf(2_000_000), mp.mpf(3), mp.mpf('0.5')),
                      (mp.mpf(2_000_000), mp.mpf(4), mp.mpf('1e-4'))]:
        z = mp.mpc(x, y)
        a = F_direct(t, z)
        b = F_direct(t, z, h=mp.mpf('0.2'), vlo=-18, vhi=14)
        conv.append({"x": fl(x, 9), "y": fl(y, 3), "t": fl(t, 3),
                     "abs_difference_h025_vs_h020_wider": fl(abs(a - b), 3),
                     "pass": bool(abs(a - b) < mp.mpf('1e-15'))})
        ok &= conv[-1]["pass"]
        print("A-conv", conv[-1], flush=True)
    results["A"] = {"checks": "H_t/M_t(s_+) by direct heat-kernel convolution of xi at claimed-domain points;"
                              " |F-1| against the theorem's budget 96624791/147000000; |F-main terms| against"
                              " the note's ordinary-error plus remainder allowance 1/25000+26/x; main-term"
                              " pieces against their bounds zeta(2)-1 and 11/1000",
                    "points": rows, "convergence": conv, "pass": ok}
    return ok


def section_B(results, quick):
    mp.mp.dps = 30
    U = mp.mpf('2324466.298474')       # disk centre abscissa; bottom point at y=3 is the stress point
    X = U - mp.mpf(1) / 2
    w = mp.mpc(U, mp.mpf(7) / 2)
    r = mp.mpf(1) / 2
    K = 12 if not quick else 8
    out = []
    ok = True
    for t in ([mp.mpf('1e-4'), mp.mpf('0.5')] if not quick else [mp.mpf('1e-4')]):
        vals = []
        for k in range(K):
            th = 2 * mp.pi * k / K
            z = w + r * mp.expj(th)
            vals.append((th, F_direct(t, z)))
        Fc = F_direct(t, w)
        circ_max = max(abs(v - 1) for _, v in vals)
        # Cauchy: F'(w) = (1/(2 pi i)) int F(z)/(z-w)^2 dz  ->  mean of F(w+r e^{i th}) e^{-i th} / r
        Fp = sum(v * mp.expj(-th) for th, v in vals) / (K * r)
        # aliasing check: the mean of F on the circle reproduces F(w)
        Fmean = sum(v for _, v in vals) / K
        s = (1 - 1j * w) / 2
        BpB = (-1j / 2) * alpha(s) * (1 + t / 2 * alpha_prime(s))
        D = -mp.im(BpB + Fp / Fc)
        bound_D = mp.mpf(2003) / 8000 * mp.log(X + 2) + mp.mpf(14) / 3
        row = {"t": fl(t, 3), "X": fl(X, 13), "circle_points": K,
               "max_abs_F_minus_1_on_circle": fl(circ_max),
               "abs_F_minus_1_at_centre": fl(abs(Fc - 1)),
               "mean_value_check_abs_error": fl(abs(Fmean - Fc), 3),
               "abs_FprimeoverF_at_centre": fl(abs(Fp / Fc)),
               "lemma_allowance_14_over_3": fl(mp.mpf(14) / 3),
               "abs_BprimeoverB": fl(abs(BpB)),
               "D_t_U": fl(D),
               "lemma_bound_on_D": fl(bound_D),
               "implied_count_bound_41_over_9_D": fl(mp.mpf(41) / 9 * D, 6),
               "theorem_count_bound": fl(mp.mpf(6) / 5 * mp.log(X + 2) + 22, 6),
               "density_one_over_4pi_log": fl(mp.log(X / (4 * mp.pi)) / (4 * mp.pi), 6)}
        row["pass"] = bool(circ_max < BUDGET and abs(Fp / Fc) <= mp.mpf(14) / 3 and D <= bound_D
                           and abs(Fmean - Fc) < mp.mpf('1e-8'))
        ok &= row["pass"]
        out.append(row)
        print("B", row, flush=True)
    results["B"] = {"checks": "the extraction lemma's disk at a stress point (bottom point y=3 nearly aligned):"
                              " circle maximum of |F-1|, Cauchy estimate of F'/F, Poisson sum D_t(U) and"
                              " the implied count (41/9)D against the theorem's bound",
                    "rows": out, "pass": ok}
    return ok


def section_C(results, quick):
    ok = True
    worst = {}
    def upd(name, margin, where):
        # margin: (bound - quantity) scaled by the bound, so that it is comparable across heights
        nonlocal ok
        if name not in worst or margin < worst[name][0]:
            worst[name] = (margin, where)
        if margin < 0:
            ok = False
    xs = ['2e6', '2.5e6', '1e7', '1e9', '1e12', '1e20', '1e40']
    sigmas = ['-1.5', '-1.25', '-1', '2', '2.25', '2.5']
    ys = ['3', '3.5', '4']
    ts = ['1e-6', '0.1', '0.5']
    for xstr in xs:
        # precision grows with the height: several bounds are tight only at order 1/x^2
        mp.mp.dps = 60 + 3 * int(mp.ceil(mp.log10(mp.mpf(xstr))))
        x = mp.mpf(xstr)
        sigmas_m = [mp.mpf(v) for v in sigmas]
        ys_m = [mp.mpf(v) for v in ys]
        ts_m = [mp.mpf(v) for v in ts]
        T = x / 2
        Q = x / (4 * mp.pi)
        L = mp.log(Q)
        for sg in sigmas_m:
            for sgn in (1, -1):
                s = mp.mpc(sg, sgn * T)
                a = alpha(s)
                # additive bounds of size 1/x^2 and 1/x: margins scaled by x^2 and x respectively
                upd("(4) Re alpha >= L/2-13/x^2  [margin*x^2]", (mp.re(a) - (L / 2 - 13 / x ** 2)) * x ** 2, (xstr, str(sg), sgn))
                dev = abs(a - L / 2 - sgn * 1j * mp.pi / 4)
                upd("(4) |alpha-L/2-+i pi/4| <= 11/(2x)+25/(4x^2)  [margin*x^2]",
                    (11 / (2 * x) + 25 / (4 * x ** 2) - dev) * x ** 2, (xstr, str(sg), sgn))
                for t in ts_m:
                    Nn = int(mp.floor(mp.sqrt(Q + t / 16)))
                    upd("(5) log N <= 2 Re alpha  (W_n<=1)", 2 * mp.re(a) - mp.log(Nn), (xstr, str(sg), str(t)))
                    for n in (1, Nn):
                        expo = ((t ** 2 / 8) * abs(a - mp.log(n)) ** 2 + t / 4 + mp.mpf(1) / 6) / (T - mp.mpf('3.33'))
                        upd("(6) Prop 6.1 error < 1/50000  [relative]", 1 - (mp.exp(expo) - 1) * 50000, (xstr, str(sg), str(t), n))
        for y in ys_m:
            A = (1 + y) / 2
            sp = mp.mpc(A, -T)
            sm = mp.mpc(1 - A, T)
            for t in ts_m:
                Nn = int(mp.floor(mp.sqrt(Q + t / 16)))
                ratio = abs(Mt(sm, t) / Mt(sp, t))
                upd("(15) |M_t(s-)/M_t(s+)| < 2Q^{-y/2}  [1 - quantity/bound]", 1 - ratio / (2 * Q ** (-y / 2)), (xstr, str(y), str(t)))
                Tp = T + mp.pi * t / 8
                lhs16 = mp.exp(t * mp.pi ** 2 / 64) * abs(M0(mp.mpc(0, Tp))) / abs(Mt(sp, t))
                upd("(16) e^{t pi^2/64}|M_0(iT')|/|M_t(s+)| <= Q^{-(1+y)/4}  [1 - quantity/bound]",
                    1 - lhs16 / Q ** (-(1 + y) / 4), (xstr, str(y), str(t)))
                upd("(17) ratio*N^{(y+1)/2} < 4Q^{-1/2}  [1 - quantity/bound]",
                    1 - ratio * mp.mpf(Nn) ** ((y + 1) / 2) / (4 * Q ** mp.mpf(-0.5)), (xstr, str(y), str(t)))
                upd("(17) 4Q^{-1/2} < 11/1000  [1 - quantity/bound]", 1 - 4 * Q ** mp.mpf(-0.5) / (mp.mpf(11) / 1000),
                    (xstr, str(y), str(t)))
    mp.mp.dps = 60
    # Note 01 lemma: carrier derivative at the disk centre for X >= 200
    for X in [mp.mpf(v) for v in ('200', '1000', '1e5', '2e6', '1e12', '1e30')]:
        U = X + mp.mpf(1) / 2
        s = mp.mpc(mp.mpf(9) / 4, -U / 2)
        a, ap = alpha(s), alpha_prime(s)
        upd("Note01 |alpha| < log(X+2)/2", mp.log(X + 2) / 2 - abs(a), str(X))
        upd("Note01 |alpha'| <= 103/20000", mp.mpf(103) / 20000 - abs(ap), str(X))
        for t in (mp.mpf('1e-6'), mp.mpf('0.5')):
            BpB = abs((-1j / 2) * a * (1 + t / 2 * ap))
            upd("Note01 |B'/B| <= (2003/8000) log(X+2)", mp.mpf(2003) / 8000 * mp.log(X + 2) - BpB, (str(X), str(t)))
    table = {k: {"min_margin": mp.nstr(v[0], 6), "at": str(v[1])} for k, v in worst.items()}
    for k, v in table.items():
        print("C", k, v, flush=True)
    results["C"] = {"checks": "sampled margins of the elementary carrier inequalities, scaled as labelled"
                              " (x^2 times an additive margin, or 1 - quantity/bound); a negative margin anywhere"
                              " fails; sampling does not prove the inequalities between sample points",
                    "worst_margins": table, "pass": ok}
    return ok


def section_D(results, quick):
    mp.mp.dps = 40
    ok = True
    rows = []
    for D in (mp.mpf(20), mp.mpf(10) ** 6 - 3):
        for t in (mp.mpf('0.5'), mp.mpf('0.01')):
            for sg in (mp.mpf('-1.5'), mp.mpf('0.5'), mp.mpf('2.5')):
                for b in (mp.mpf(0), mp.log(9), -mp.log(2)):
                    h = 1 - t / D
                    closed = h ** mp.mpf(-0.5) * mp.exp((sg ** 2 + 1) / D + b * sg + t * (sg / D + b / 2) ** 2 / h)
                    f = lambda u: mp.exp((u * u + 1) / D + b * u - (u - sg) ** 2 / t) / mp.sqrt(mp.pi * t)
                    quad = mp.quad(f, [-mp.inf, sg - 5 * mp.sqrt(t), sg, sg + 5 * mp.sqrt(t), mp.inf])
                    rel = abs(quad / closed - 1)
                    row = {"D": mp.nstr(D, 8), "t": str(t), "sigma": str(sg), "b": mp.nstr(b, 6),
                           "relative_difference": mp.nstr(rel, 3)}
                    row["pass"] = bool(rel < mp.mpf('1e-25'))
                    if D > 100 and b != 0:
                        factor = closed / mp.exp(b * sg)
                        row["factor_after_removing_e^{b sigma}"] = mp.nstr(factor, 8)
                        row["pass"] = row["pass"] and bool(factor < 2)
                    ok &= row["pass"]
                    rows.append(row)
    # J_0 < 4/3 at the extreme
    D = mp.mpf(10) ** 6 - 3
    J0 = (1 - mp.mpf('0.5') / D) ** mp.mpf(-0.5) * mp.exp((mp.mpf('2.5') ** 2 + 1) / D + mp.mpf('0.5') * (mp.mpf('2.5') / D) ** 2 / (1 - mp.mpf('0.5') / D))
    ok &= bool(J0 < mp.mpf(4) / 3)
    for row in rows[:3]:
        print("D", row, flush=True)
    print("D J0 at sigma=5/2,t=1/2,D=1e6-3:", mp.nstr(J0, 10), flush=True)
    results["D"] = {"checks": "closed form (9) for J_b against adaptive quadrature; factor after removing"
                              " e^{b sigma} below 2 at D=10^6-3; J_0 below 4/3",
                    "rows": rows, "J0_extreme": mp.nstr(J0, 12), "pass": ok}
    return ok


def section_E(results, quick):
    mp.mp.dps = 50
    ok = True
    out = {}
    # (i) the constant before Polymath (60): 1/(12(T'/2-0.33)) <= (1/3)/(4(T-3)) as printed
    rows = []
    for T in (mp.mpf(100), mp.mpf(10) ** 6):
        for t in (mp.mpf(0), mp.mpf('0.5')):
            Tp = T + mp.pi * t / 8
            stirling = 1 / (12 * (Tp / 2 - mp.mpf('0.33')))
            printed = (mp.mpf(1) / 3) / (4 * (T - 3))
            corrected = (mp.mpf(2) / 3) / (4 * (T - 3))
            rows.append({"T": mp.nstr(T, 7), "t": str(t), "stirling_term": mp.nstr(stirling, 8),
                         "printed_allowance": mp.nstr(printed, 8), "corrected_allowance_2_over_3": mp.nstr(corrected, 8),
                         "printed_holds": bool(stirling <= printed), "corrected_holds": bool(stirling <= corrected)})
            ok &= (not rows[-1]["printed_holds"]) and rows[-1]["corrected_holds"]
    out["constant_before_60"] = rows
    # (ii) Re s_* against (21) [t/4] and the display after (99) [t/2], for y in [3,4]
    rows = []
    for x in (mp.mpf('2e6'), mp.mpf('1e12')):
        for y in (mp.mpf(3), mp.mpf(4)):
            t = mp.mpf('0.5')
            s = mp.mpc((1 + y) / 2, -x / 2)
            re_sstar = mp.re(s + t / 2 * alpha(s))
            quarter = (1 + y) / 2 + t / 4 * mp.log(x / (4 * mp.pi))
            half = (1 + y) / 2 + t / 2 * mp.log(x / (4 * mp.pi))
            rows.append({"x": mp.nstr(x, 6), "y": str(y), "Re_s_star": mp.nstr(re_sstar, 15),
                         "minus_t_over_4_version": mp.nstr(re_sstar - quarter, 6),
                         "minus_t_over_2_version": mp.nstr(re_sstar - half, 6)})
            ok &= bool(abs(re_sstar - quarter) < 1 / x) and bool(re_sstar - half < -1)
    out["heat_coefficient_after_99"] = rows
    # (iii) fixed-index remainder RS_m when K_u=m: (1/2) Gamma(nu) (1.1/a)^{2 nu}, nu=(m+1)/2
    rows = []
    for a in (mp.mpf('300.5'), mp.mpf(1000), mp.mpf(10) ** 4):
        m = int(mp.floor(2 * a * a))
        nu = mp.mpf(m + 1) / 2
        log10_rs = mp.log10(mp.mpf(1) / 2) + mp.loggamma(nu) / mp.log(10) + 2 * nu * mp.log10(mp.mpf('1.1') / a)
        log10_Ea = -mp.log10(a) - a * a / 2 / mp.log(10)
        rows.append({"a": mp.nstr(a, 6), "m": m, "log10_RS_m_bound": mp.nstr(log10_rs, 10),
                     "log10_E_a": mp.nstr(log10_Ea, 10), "below_E_a": bool(log10_rs < log10_Ea)})
        ok &= rows[-1]["below_E_a"]
    out["fixed_index_remainder"] = rows
    # (iv) bookkeeping: does the RS index fall inside the displayed tail range [2a^2, -u+4]?
    a = mp.mpf('300.5')
    m = int(mp.floor(2 * a * a))
    cases = []
    for u in (mp.mpf('-0.5'), mp.mpf(-10), mp.mpf(-(m - 4)), mp.mpf(-(m - 3)) - mp.mpf('0.5'), mp.mpf(-(m + 7)) - mp.mpf('0.25')):
        dyn = int(mp.floor(-u)) + 3
        Ku = max(dyn, m)
        idx = Ku + 1
        in_tail = bool(idx >= 2 * a * a and idx <= -u + 4)
        cases.append({"u": mp.nstr(u, 10), "K_u": Ku, "K_u_set_by_height_m_only": dyn < m, "RS_index": idx,
                      "RS_index_in_displayed_tail": in_tail})
        # the displayed tail holds the RS term exactly when K_u = floor(-u)+3, i.e. unless m strictly wins
        ok &= (in_tail == (dyn >= m))
    out["remainder_bookkeeping_a_300.5"] = cases
    for k, v in out.items():
        print("E", k, v, flush=True)
    results["E"] = {"checks": "(i) printed constant before Polymath (60) fails, corrected 2/3 holds; (ii) Re s_* follows"
                              " t/4 (21), not t/2 (after 99); (iii) RS_m <= E_a; (iv) RS index lies in the displayed tail"
                              " exactly when floor(-u)+3 >= m (so it is missed when the height index m strictly wins)",
                    "results": out, "pass": ok}
    return ok


def section_F(results, quick):
    mp.mp.dps = 30
    rows = []
    for X in (mp.mpf('2e6'), mp.mpf('1e10'), mp.mpf('1e20')):
        T = X / 2
        rows.append({"X": mp.nstr(X, 6),
                     "theorem_bound_6_5_log_plus_22": mp.nstr(mp.mpf(6) / 5 * mp.log(X + 2) + 22, 6),
                     "sharp_constants_82123_72000_and_574_27": mp.nstr(mp.mpf(82123) / 72000 * mp.log(X + 2) + mp.mpf(574) / 27, 6),
                     "mean_density_log(X/4pi)/(4pi)": mp.nstr(mp.log(X / (4 * mp.pi)) / (4 * mp.pi), 6),
                     "t0_benchmark_BellottiWong_Cor1.6_unit_T_window": (
                         mp.nstr(mp.log(T) / (2 * mp.pi) + mp.mpf('4.8405'), 6) if T + 1 <= mp.mpf('30610046000')
                         else mp.nstr((1 / (2 * mp.pi) + mp.mpf('0.20152')) * mp.log(T)
                                      + min(mp.mpf('0.4892') * mp.log(mp.log(T)) + mp.mpf('14.2040'),
                                            mp.mpf('3.3769') * mp.log(mp.log(T)) + mp.mpf('2.8062')) + 1 / (25 * T), 6))})
    for r in rows:
        print("F", r, flush=True)
    results["F"] = {"checks": "benchmarks only (no pass condition beyond arithmetic): the t=0 row bounds N(T+1)-N(T),"
                              " which contains the half-unit T window of a unit x window; t=0 is outside the theorem's"
                              " domain 0<t<=1/2", "rows": rows, "pass": True}
    return True


def section_G(results, quick):
    """Reviewer arithmetic, not a proof: where the notes' own ingredients close the budget.

    Band [3,4] (the notes' disk, centre 7i/2): budget = 95/147 + 4Q^{-1/2} + ordinary + 2 K_R/Q with
    K_R = (1/2)e^{14/(T-6)} + 97.374/(a-0.865) + 2/a carried as a function of a = sqrt(Q) instead of
    being forced below 1 by a > 300.  Band [4,5] (disk centre 9i/2): the same ingredients with
    zeta(5/2)-1, 4Q^{-3/4}, 9^sigma <= 729, 2^{-sigma} < 4, sigma^2 <= 9 and 2 K_R Q^{-5/4}; kernel
    floor 11/61.  Lemma 4 would have to be restated with K_R(a) and its side conditions rechecked
    (its 'factor below 2' step uses D > 1000(sigma^2+1)), so x_min is a planning number only.
    """
    mp.mp.dps = 30
    z2 = mp.zeta(2)
    z52 = mp.zeta(mp.mpf(5) / 2)

    def budget(x, band):
        Q = x / (4 * mp.pi)
        T = x / 2
        a = mp.sqrt(Q)
        u = (3 * mp.log(x) ** 2 / 32 + mp.mpf(7) / 8) / x
        eps = mp.exp(u) - 1
        if band == 34:
            opp = 4 * Q ** mp.mpf(-0.5)
            KR = mp.exp(14 / (T - 6)) / 2 + mp.mpf('97.374') / (a - mp.mpf('0.865')) + 2 / a
            return mp.mpf(95) / 147 + opp + (z2 + opp) * eps + 2 * KR / Q
        opp = 4 * Q ** mp.mpf(-0.75)
        KR = mp.exp(mp.mpf('19.5') / (T - 6)) / 2 + mp.mpf('291.832') / (a - mp.mpf('0.865')) + 2 / a
        return (z52 - 1) + opp + (z52 + opp) * eps + 2 * KR * Q ** mp.mpf(-1.25)

    def side_ok(x, band):
        T = x / 2
        D = T - 3
        smax2 = 9 if band == 45 else mp.mpf(25) / 4
        return (smax2 + 1) / D < mp.mpf(1) / 1000 and 1 - mp.mpf(1) / (2 * D) > mp.mpf(999) / 1000

    out = {}
    for band in (34, 45):
        grid = [mp.mpf(10) ** (mp.mpf(k) / 20) for k in range(40, 141)]   # 10^2 .. 10^7
        closes = [x for x in grid if budget(x, band) < mp.mpf(7) / 10]
        xmin_budget = min(closes) if closes else None
        both = [x for x in grid if budget(x, band) < mp.mpf(7) / 10 and side_ok(x, band)]
        xmin_both = min(both) if both else None
        X = mp.mpf('2e6')
        q = budget(X + mp.mpf(1) / 2, band)
        floor = mp.mpf(9) / 41 if band == 34 else mp.mpf(11) / 61
        coeff = mp.mpf(2003) / 8000 / floor
        const = (q / ((1 - q) / 2)) / floor
        out["band_%d" % band] = {
            "x_min_where_budget_below_7_10_(grid)": mp.nstr(xmin_budget, 4) if xmin_budget else None,
            "x_min_also_meeting_written_side_conditions": mp.nstr(xmin_both, 4) if xmin_both else None,
            "budget_q_at_X=2e6": mp.nstr(q, 6),
            "count_bound_coefficient_of_log(X+2)": mp.nstr(coeff, 6),
            "count_bound_additive_constant_using_q": mp.nstr(const, 6),
            "count_bound_at_X=2e6": mp.nstr(coeff * mp.log(X + 2) + const, 6)}
        print("G", band, out["band_%d" % band], flush=True)
    results["G"] = {"checks": "reviewer arithmetic only: cutoff and constants obtainable from the notes' own"
                              " ingredients, for the [3,4] band with K_R tracked in a and for a [4,5] band;"
                              " planning numbers, not proved extensions",
                    "results": out, "pass": True}
    return True


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--output", default=None)
    p.add_argument("--sections", default="ABCDEFG")
    p.add_argument("--quick", action="store_true", help="smaller grids (for a fast replay)")
    p.add_argument("--inject-normalization", action="store_true",
                   help="use exp(t alpha^2/2) in M_t; section A must then fail")
    args = p.parse_args()
    if args.inject_normalization:
        HEAT_COEFF["value"] = mp.mpf(1) / 2
    with open(__file__, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    results = {"script": "review_checks_claude_20261017.py", "script_sha256": digest,
               "environment": {"python": platform.python_version(), "mpmath": mp.__version__,
                               "platform": platform.system()},
               "inject_normalization": args.inject_normalization,
               "sections_run": args.sections, "quick": args.quick}
    t0 = time.time()
    ok = True
    for sec, fn in (("A", section_A), ("B", section_B), ("C", section_C), ("D", section_D),
                    ("E", section_E), ("F", section_F), ("G", section_G)):
        if sec in args.sections:
            s0 = time.time()
            ok &= fn(results, args.quick)
            results[sec]["runtime_seconds"] = round(time.time() - s0, 1)
    results["runtime_seconds"] = round(time.time() - t0, 1)
    results["status"] = "pass" if ok else "fail"
    text = json.dumps(results, indent=1, default=str)
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(text + "\n")
    print("STATUS", results["status"], "runtime", results["runtime_seconds"])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
