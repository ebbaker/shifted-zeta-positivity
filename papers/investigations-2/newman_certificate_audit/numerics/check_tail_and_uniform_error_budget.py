#!/usr/bin/env python3
"""Independent standard-library re-evaluation of the tail lemma and of the
uniform finite-lane error budget of the pinned Gomila package.

Audited package: judegomila/dbn-lambda-01787854-candidate-audit at commit
a74738deb6d5e0f76887cb36901da08b68dca705 (seal 443/443):

  * TAIL_LEMMA.md with verifiers/verify_tail_arb.c (logs/tail_arb_{256,512}.log):
    every N >= N* = 3840000, t in [129/800, 161250001/10^9],
    y in [y0, sqrt(1 - 2t)], with the exact convolution head M = 153814
    and the error head M_err = 3000;
  * Proposition 4.10 of PROOF_NOTE.md (gates U1--U5) with
    verifiers/verify_prop410_arb.c (logs/prop410_arb_{256,512}.log): the
    uniform budget E_max = e_A + e_B + e_{C,0} on every window N >= N0 =
    690988, y in [y0, sqrt(1 - 2 t0)], t in the same t-box, head m0 = 2000.

Published inputs (Polymath, arXiv:1904.12438v2; read from the project's own
TeX source, km-git-acc/dbn_upper_bound, Writeup/debruijn.tex at 8e8a6ab,
mathematically identical to a377700 of 26 July 2019): Theorem 1.3 with the
bounds (20)--(22), (23), the exact definitions (71)--(72), the epsilon bound
in the proof of Proposition 6.6(iv)--(v), Proposition 6.6(vi), and the
1 + u <= e^u, 1/(x - 8.52) <= 1/(x - 12) consequence with constant
3.58 + 6.92 = 10.50 (ERROR_CONSTANT_WELD.md).

What is computed, with directed rounding (decimal, PREC digits; + - * / with
ROUND_FLOOR / ROUND_CEILING, exp / ln / sqrt correctly rounded and padded by
a relative 10^-(PREC-2)), as rigorous upper or lower bounds:

  tail   delta_hat, kappa_hat, sigma_1, sigma_2 on the y-box and the extended
         hull; the exact convolution coefficients c_m(t) (m <= M) as
         t-intervals; P, TR, OV, M_max, G, the A head PA and cap, AB;
         D = P + TR + OV + M_max AB and the OV-free D' = P + TR + M_max AB;
         flow = (1 - D)/M_max and flow' = (1 - D')/M_max; the error terms
         e_A + e_B (from (71)--(72) termwise) and e_{C,0} (10.50 form);
         every gate of verify_tail_arb.c, with its value.
  E_max  delta_1, sigma_1, U1max, P_max, the m0 = 2000 head and cap, S_max,
         e_A + e_B, e_{C,0}, E_max, and every gate of verify_prop410_arb.c,
         with its value; T_min - E_max for the stored floor and for the
         certified floor of note 3.

Enclosure conventions mirror the package where the lemma prescribes them
(lower point of sigma over the whole box, t_hi in the positive quadratic
term, the extended y-interval evaluated as a decorrelated hull), so that the
printed digits can be compared with the Arb transcripts; every choice is a
valid upper bound on its own.  -ln(1 - z) <= z/(1 - z) is used for the
cutoff correction instead of an evaluated logarithm.

Self-tests (--selftest): the convolution partition (4.3) is checked
coefficientwise in exact integer arithmetic at reduced size; the overlap of
the OV caps with the TR caps is checked; pi (Machin) and the padded
exp / ln / sqrt are checked against 2*PREC-digit evaluations.

Prepared for Edward Baker with LLM assistance (Claude Opus 5.5,
claude-opus-5-5), 12 October 2026.  Internal check, not independent review.

Usage:
    python3 check_tail_and_uniform_error_budget.py --selftest --output rec.json
(the retained record was produced by exactly this command; under a minute).
"""
import argparse
import decimal
import hashlib
import json
import math
import platform
import random
import sys
import time
from decimal import Context, Decimal as Dc, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from fractions import Fraction as F

PREC = 50
CN = Context(prec=PREC, rounding=ROUND_HALF_EVEN)
CF = Context(prec=PREC, rounding=ROUND_FLOOR)
CC = Context(prec=PREC, rounding=ROUND_CEILING)
decimal.setcontext(Context(prec=PREC, rounding=ROUND_HALF_EVEN))
ETA = Dc(10) ** (-(PREC - 2))
ONE = Dc(1)
ZERO = Dc(0)

PACKAGE = {"repository": "https://github.com/judegomila/dbn-lambda-01787854-candidate-audit",
           "commit": "a74738deb6d5e0f76887cb36901da08b68dca705",
           "tail_lemma": "TAIL_LEMMA.md", "tail_verifier": "verifiers/verify_tail_arb.c",
           "tail_verifier_sha256": "see SHA256SUMS of the package",
           "prop410_verifier": "verifiers/verify_prop410_arb.c",
           "prop410_verifier_sha256": "0d40f9b8137f83fcfd7c6546e333d23acac052fa7ca3822f4d7d3075c62e66d8"}
POLYMATH = {"paper": "D.H.J. Polymath, arXiv:1904.12438v2 (posted 2019-08-04)",
            "source_read": "https://github.com/km-git-acc/dbn_upper_bound, Writeup/debruijn.tex",
            "commit": "8e8a6ab1115d67aad66f6dbef374eef64922a060",
            "tex_sha256": "0115d452da906c5bbaacb1ee0ce851e568d8d5f62f27c71a4bf8d281b5788647",
            "identical_math_to": "a377700a91c33c77904038c6622a2dea0344717d (2019-07-26)"}

# Values printed by the package's Arb transcripts (identical at 256 and 512 bits).
PACKAGE_TAIL = {"P": "0.170228023678122321113605335857", "TR": "0.262901330124790788866827788829",
                "OV": "0.0392426812101768475583366613548", "Mmax": "1.60828914495414088402844775061",
                "AB": "0.327894319270989311336437998039", "D": "0.999720909388749436758326982808",
                "flow": "0.000173532608938003678257214829009", "eAB": "4.93807921086187273290965029672e-13",
                "eC0": "1.16711096273536263367986975936e-8", "err": "1.16716034352747125240719885587e-8",
                "margin": "0.000173520937334568403544690757021"}
PACKAGE_PROP410 = {"eAB": "2.05702368866621449147357372171e-12", "eC0": "2.33492848188649182679145092376e-7",
                   "Emax": "2.33494905212337848893636565949e-7", "Tmin_minus_Emax": "5.57871094787662151106363434051e-7",
                   "head": "1.44876762495760296178674790494", "cap": "0.943027908358772718191521507425",
                   "Smax": "3.39179553331637567997826941236", "Pmax": "2.02020134002695090625827654559",
                   "U1max": "3.00202962917846556019239760834e-13"}

# ----------------------------------------------------------------------------- directed arithmetic


def lo(fr):
    """Largest PREC-digit decimal <= the rational fr."""
    fr = F(fr)
    return CF.divide(Dc(fr.numerator), Dc(fr.denominator))


def hi(fr):
    fr = F(fr)
    return CC.divide(Dc(fr.numerator), Dc(fr.denominator))


def exp_lo(x):
    return CF.multiply(CN.exp(x), CF.subtract(ONE, ETA))


def exp_hi(x):
    return CC.multiply(CN.exp(x), CC.add(ONE, ETA))


def ln_lo(x):
    v = CN.ln(x)
    return CF.subtract(v, CC.multiply(ETA, max(ONE, v.copy_abs())))


def ln_hi(x):
    v = CN.ln(x)
    return CC.add(v, CC.multiply(ETA, max(ONE, v.copy_abs())))


def sqrt_lo(x):
    return CF.multiply(CN.sqrt(x), CF.subtract(ONE, ETA))


def sqrt_hi(x):
    return CC.multiply(CN.sqrt(x), CC.add(ONE, ETA))


def mul_lo(a, b):
    return CF.multiply(a, b)


def mul_hi(a, b):
    return CC.multiply(a, b)


def add_lo(*xs):
    s = ZERO
    for x in xs:
        s = CF.add(s, x)
    return s


def add_hi(*xs):
    s = ZERO
    for x in xs:
        s = CC.add(s, x)
    return s


def imul(a, b):
    """Interval product, a=(lo,hi), b=(lo,hi)."""
    ps = [(x, y) for x in a for y in b]
    return (min(CF.multiply(x, y) for x, y in ps), max(CC.multiply(x, y) for x, y in ps))


def atan_inv(k, terms):
    """Enclosure of atan(1/k) by the alternating series (exact rationals)."""
    s = F(0)
    for j in range(terms):
        s += F((-1) ** j, (2 * j + 1) * k ** (2 * j + 1))
    s_next = s + F((-1) ** terms, (2 * terms + 1) * k ** (2 * terms + 1))
    return (min(s, s_next), max(s, s_next))


def pi_enclosure():
    a5 = atan_inv(5, 60)
    a239 = atan_inv(239, 25)
    plo = 16 * a5[0] - 4 * a239[1]
    phi = 16 * a5[1] - 4 * a239[0]
    assert phi - plo < F(1, 10 ** 70)
    return lo(plo), hi(phi)


PI_LO, PI_HI = pi_enclosure()


def s(x, digits=30):
    """Decimal to string with the given significant digits (record only)."""
    return format(Context(prec=digits).plus(x), "E") if x != 0 else "0"


def ln_pair(n):
    d = Dc(n)
    return ln_lo(d), ln_hi(d)


# ----------------------------------------------------------------------------- shared exact inputs

T_LO = F(129, 800)
T_HI = F(161250001, 10 ** 9)
Y0SQ = F(87677, 2500000)
YMAXSQ = F(271, 400)           # 1 - 2 t0
C002 = F(1, 50)               # 0.02
C0626 = F(313, 500)           # 0.626
C666 = F(333, 50)             # 6.66
C124 = F(31, 25)              # 1.24
C1050 = F(21, 2)              # 10.50 = 3.58 + 6.92


def cap_hi(la, lc, sigma_lo, t_hi):
    """Upper bound of Cap_t(a,c;sigma) = max(E(a),E(c)) log(c/a), E(u) = exp((1-sigma)log u + (t/4)log^2 u),
    for sigma >= sigma_lo, t <= t_hi, log a in la=(lo,hi), log c in lc=(lo,hi); requires log a >= 0."""
    assert la[0] >= 0
    one_minus = (CF.subtract(ONE, sigma_lo), CC.subtract(ONE, sigma_lo))   # 1 - sigma <= 1 - sigma_lo

    def e_hi(lu):
        # (1-sigma) log u <= (1 - sigma_lo) log u; maximise over log u in lu
        lin = max(CC.multiply(one_minus[1], lu[0]), CC.multiply(one_minus[1], lu[1]))
        quad = CC.multiply(CC.divide(t_hi, 4), CC.multiply(lu[1], lu[1]))
        return exp_hi(CC.add(lin, quad))
    m = max(e_hi(la), e_hi(lc))
    width = CC.subtract(lc[1], la[0])
    return CC.multiply(m, width)


def gates_fixed_left(la, lnN, t_lo_d, sigma_lo):
    """Lower bounds of the two all-N gates (6.4), (6.5) for a cap with fixed left end a:
    (t/2) log a (log N - log a) > 1 and (sigma - 1)(log N - log a) > 1."""
    width_lo = CF.subtract(lnN[0], la[1])
    ga = CF.multiply(CF.multiply(CF.divide(t_lo_d, 2), la[0]), width_lo)
    gb = CF.multiply(CF.subtract(sigma_lo, ONE), width_lo)
    return ga, gb


# ----------------------------------------------------------------------------- tail lemma


def tail(results, gates):
    N = 3840000
    M = 153814
    MERR = 3000
    S = [1, 2, 3, 4, 5, 6, 7, 10, 11, 13, 14]
    LAM = {1: F(1), 2: F(-1021, 1000), 3: F(-1054, 1000), 4: F(-9, 200), 5: F(-1119, 1000),
           6: F(1001, 1000), 7: F(-1043, 1000), 10: F(128, 125), 11: F(-161, 200), 13: F(-447, 500),
           14: F(456373, 500000)}
    YB = (F(1872719, 10 ** 7), F(23409, 125000))
    YE = (F(1872719, 10 ** 7), F(8231039, 10 ** 7))

    # exact gates (Fraction arithmetic)
    gates["tail.exact.ybox_contains_y0"] = (YB[0] ** 2 < Y0SQ < YB[1] ** 2)
    gates["tail.exact.yext_top_ge_sqrt(1-2t0)"] = (YE[1] ** 2 >= 1 - 2 * T_LO)
    gates["tail.exact.previous_grid_point_below_sqrt(1-2t0)"] = ((YE[1] - F(1, 10 ** 7)) ** 2 < 1 - 2 * T_LO)
    gates["tail.exact.ybox_top_below_sqrt(1-2t)_on_I_t"] = (YB[1] ** 2 <= 1 - 2 * T_HI)
    gates["tail.exact.target_identity"] = (T_LO + Y0SQ / 2 == F(893927, 5000000))
    gates["tail.exact.lambda1=1"] = (LAM[1] == 1)
    gates["tail.exact.sum|lambda|=9918746/10^6"] = (sum(abs(v) for v in LAM.values()) == F(9918746, 10 ** 6))
    gates["tail.exact.N>M>Merr>1"] = (N > M > MERR > 1)
    gates["tail.exact.domain_0<t<=1/2_0<y<=1"] = (0 < T_LO and T_HI <= F(1, 2) and 0 < YE[0] and YE[1] <= 1)
    gates["tail.exact.OVW_N>=d(d+1)"] = all(N >= d * (d + 1) for d in S)
    # OV caps [N/(d+1), N] lie inside the TR caps [floor(M/d), N]: OV double counts part of TR
    gates["tail.exact.OV_caps_inside_TR_caps"] = all(M // d <= F(N, d + 1) for d in S if d > 1)

    t_lo, t_hi = lo(T_LO), hi(T_HI)
    lnN = ln_pair(N)
    n2 = F(N * N)
    q = (n2 - T_HI / 16, n2 - T_LO / 16)                    # N^2 - t/16 over I_t (exact)
    l1 = (ln_lo(lo(q[0])), ln_hi(hi(q[1])))
    x1 = (CF.multiply(CF.multiply(4, PI_LO), lo(q[0])), CC.multiply(CC.multiply(4, PI_HI), hi(q[1])))
    z = (T_LO / (16 * n2), T_HI / (16 * n2))
    gates["tail.domain.X_N>200_and_>12"] = x1[0] > 200
    gates["tail.domain.log(N^2-t/16)>2"] = l1[0] > 2
    gates["tail.domain.0<z<1"] = (0 < z[0] and z[1] < 1)
    gates["tail.window_log_gate.N(1-z)>1"] = (N * (1 - z[1]) > 1)

    # delta_hat >= (t/4)(-log(1-z)) + t/(2 X_N^2), using -log(1-z) <= z/(1-z)
    zz = hi(z[1] / (1 - z[1]))
    delta = add_hi(CC.multiply(CC.divide(t_hi, 4), zz), CC.divide(t_hi, CF.multiply(2, CF.multiply(x1[0], x1[0]))))
    kappa = CC.divide(t_hi, CF.multiply(2, CF.subtract(x1[0], 6)))
    base_lo = CF.subtract(CF.add(lo(F(1, 2)), CF.multiply(CF.divide(t_lo, 2), lnN[0])), delta)
    s1box = CF.add(base_lo, CF.divide(lo(YB[0]), 2))
    s2box = CF.subtract(CF.subtract(base_lo, kappa), CC.divide(hi(YB[1]), 2))
    s1ext = CF.add(base_lo, CF.divide(lo(YE[0]), 2))
    s2ext = CF.subtract(CF.subtract(base_lo, kappa), CC.divide(hi(YE[1]), 2))
    thr = CC.multiply(CC.divide(t_hi, 2), lnN[1])
    gates["tail.SC1.sigma1>(t/2)logN"] = (s1box > thr and s1ext > thr)
    gates["tail.SC2.sigma2>(t/2)logN"] = (s2box > thr and s2ext > thr)
    gates["tail.SC3.sigma1,sigma2>1_on_ext"] = (s1ext > 1 and s2ext > 1)
    results["tail.delta_hat"] = s(delta)
    results["tail.kappa_hat"] = s(kappa)
    results["tail.sigma1_box_lo"] = s(s1box)
    results["tail.sigma2_box_lo"] = s(s2box)
    results["tail.sigma1_ext_lo"] = s(s1ext)
    results["tail.sigma2_ext_lo"] = s(s2ext)
    results["tail.SC_threshold_hi"] = s(thr)

    # logs and b_t(k) enclosures, k <= M
    LNLO = [ZERO] * (M + 1)
    LNHI = [ZERO] * (M + 1)
    BLO = [ONE] * (M + 1)
    BHI = [ONE] * (M + 1)
    t4_lo = CF.divide(t_lo, 4)
    t4_hi = CC.divide(t_hi, 4)
    for k in range(2, M + 1):
        a, b = ln_pair(k)
        LNLO[k], LNHI[k] = a, b
        BLO[k] = exp_lo(CF.multiply(t4_lo, CF.multiply(a, a)))
        BHI[k] = exp_hi(CC.multiply(t4_hi, CC.multiply(b, b)))

    # exact convolution c_m(t) = sum_{d | m, d in S} lambda_d b_t(m/d), as t-intervals
    clo = [ZERO] * (M + 1)
    chi = [ZERO] * (M + 1)
    for d in S:
        lamlo, lamhi = lo(LAM[d]), hi(LAM[d])
        for k in range(1, M // d + 1):
            m = d * k
            if m < 2:
                continue
            if LAM[d] > 0:
                clo[m] = CF.add(clo[m], CF.multiply(lamlo, BLO[k]))
                chi[m] = CC.add(chi[m], CC.multiply(lamhi, BHI[k]))
            else:
                clo[m] = CF.add(clo[m], CF.multiply(lamlo, BHI[k]))
                chi[m] = CC.add(chi[m], CC.multiply(lamhi, BLO[k]))

    # P = sum_{m=2}^M |c_m| m^{-sigma1}
    P = ZERO
    Pw = ZERO
    for m in range(2, M + 1):
        am = max(clo[m].copy_abs(), chi[m].copy_abs())
        w = CC.subtract(chi[m], clo[m])
        pw = exp_hi(CC.multiply(-s1box, LNLO[m]))
        P = CC.add(P, CC.multiply(am, pw))
        Pw = CC.add(Pw, CC.multiply(w, pw))
    results["tail.P_hi"] = s(P)
    results["tail.P_t_interval_width_contribution_hi"] = s(Pw)

    # TR, OV, Mmax
    TR = ZERO
    OV = ZERO
    MM = ZERO
    routed = []
    for d in S:
        lam_abs = hi(abs(LAM[d]))
        dpow = ONE if d == 1 else exp_hi(CC.multiply(-s1box, ln_pair(d)[0]))
        coef = CC.multiply(lam_abs, dpow)
        MM = CC.add(MM, coef)
        a = M // d
        la = (LNLO[a], LNHI[a]) if a >= 2 else (ZERO, ZERO)
        TR = CC.add(TR, CC.multiply(coef, cap_hi(la, lnN, s1box, t_hi)))
        ga, gb = gates_fixed_left(la, lnN, t_lo, s1ext)
        routed.append({"d": d, "a": a, "gate_a_lo": s(ga, 12), "gate_b_lo": s(gb, 12),
                       "ok": bool(ga > 1 and gb > 1 and 1 <= a < N)})
        if d > 1:
            ld1 = ln_pair(d + 1)
            la_ov = (CF.subtract(lnN[0], ld1[1]), CC.subtract(lnN[1], ld1[0]))
            OV = CC.add(OV, CC.multiply(coef, cap_hi(la_ov, lnN, s1box, t_hi)))
    results["tail.TR_hi"] = s(TR)
    results["tail.OV_hi"] = s(OV)
    results["tail.Mmax_hi"] = s(MM)
    results["tail.GN-TR_routed_gates"] = routed
    gates["tail.GN-TR.all_routed_caps"] = all(r["ok"] for r in routed)
    gates["tail.OVW.sigma1_ext>1"] = s1ext > 1

    # G = e^{0.02 y} (N^2 - t/16)^{-y/2} on the y-box, as a decorrelated hull (package form):
    # e^{0.02 y_hi} exp(-y_lo L_lo / 2).  (The exact maximum, at y_lo, is smaller by e^{0.02 (y_hi - y_lo)}.)
    assert CC.subtract(hi(C002), CF.divide(l1[0], 2)) < 0
    Gbox = CC.multiply(exp_hi(CC.multiply(hi(C002), hi(YB[1]))), exp_hi(-CF.divide(CF.multiply(lo(YB[0]), l1[0]), 2)))
    # A head and cap on the y-box
    PA = ONE
    for n in range(2, M + 1):
        PA = CC.add(PA, exp_hi(CC.subtract(CC.multiply(t4_hi, CC.multiply(LNHI[n], LNHI[n])),
                                           CF.multiply(s2box, LNLO[n]))))
    capB = cap_hi((LNLO[M], LNHI[M]), lnN, s2box, t_hi)
    AB = CC.multiply(Gbox, CC.add(PA, capB))
    results["tail.Gbox_hi"] = s(Gbox)
    results["tail.PA_hi"] = s(PA)
    results["tail.capB_hi"] = s(capB)
    results["tail.AB_hi"] = s(AB)
    ga, gb_ext = gates_fixed_left((LNLO[M], LNHI[M]), lnN, t_lo, s2ext)
    _, gb_box = gates_fixed_left((LNLO[M], LNHI[M]), lnN, t_lo, s2box)
    results["tail.GN-AB.gate_a_lo"] = s(ga, 15)
    results["tail.GN-AB.gate_b_ext_lo"] = s(gb_ext, 15)
    results["tail.GN-AB.gate_b_box_lo"] = s(gb_box, 15)
    gates["tail.GN-AB.ext_hull(as_in_package)"] = (ga > 1 and gb_ext > 1)
    # how the head M is fixed by this gate: the extended-hull gate (sigma2 at the top of the hull)
    # fails already at M + 1, while the box gate (sufficient, see note 4 section 3.5) admits much larger heads
    _, gb_next = gates_fixed_left(ln_pair(M + 1), lnN, t_lo, s2ext)
    results["tail.GN-AB.gate_b_ext_lo_at_M+1"] = s(gb_next, 15)
    results["tail.GN-AB.ext_gate_fails_at_M+1"] = bool(not gb_next > 1)
    lo_m, hi_m = M, N - 1
    while hi_m - lo_m > 1:
        mid = (lo_m + hi_m) // 2
        _, g = gates_fixed_left(ln_pair(mid), lnN, t_lo, s2box)
        if g > 1:
            lo_m = mid
        else:
            hi_m = mid
    results["tail.GN-AB.largest_head_with_box_gate_b>1"] = lo_m
    gates["tail.GN-AB.box_only(sufficient,_see_note_4)"] = (ga > 1 and gb_box > 1)

    MAB = CC.multiply(MM, AB)
    D = add_hi(P, TR, OV, MAB)
    Dp = add_hi(P, TR, MAB)
    flow = CF.divide(CF.subtract(ONE, D), MM)
    flowp = CF.divide(CF.subtract(ONE, Dp), MM)
    results["tail.Mmax_AB_hi"] = s(MAB)
    results["tail.D_hi(with_OV)"] = s(D)
    results["tail.Dprime_hi(without_OV)"] = s(Dp)
    results["tail.flow_lo(with_OV)"] = s(flow)
    results["tail.flowprime_lo(without_OV)"] = s(flowp)
    gates["tail.decisive.D<1"] = D < 1
    gates["tail.decisive.D<0.999721"] = D < lo(F(999721, 10 ** 6))
    gates["tail.P_width<1-D"] = Pw < CF.subtract(ONE, D)
    # reserves and tolerances (with the other suppliers held fixed)
    res_ov = CF.subtract(ONE, D)
    res = CF.subtract(ONE, Dp)
    results["tail.reserve_1-D(with_OV)_lo"] = s(res_ov, 12)
    results["tail.reserve_1-Dprime(without_OV)_lo"] = s(res, 12)
    tol = {}
    for name, val in (("P", P), ("TR", TR), ("Mmax*AB", MAB)):
        tol[name] = {"with_OV": s(CF.divide(res_ov, val), 6), "without_OV": s(CF.divide(res, val), 6)}
    results["tail.relative_tolerance(reserve/component)"] = tol

    # y-monotonicity gate: 0.02 - L/2 + log(N)/2 < 0
    ym = CC.add(CC.subtract(hi(C002), CF.divide(l1[0], 2)), CC.divide(lnN[1], 2))
    results["tail.YM_gate_hi"] = s(ym, 12)
    gates["tail.YM"] = ym < 0

    # error terms
    delerr = CC.divide(CC.add(CC.multiply(CC.divide(CC.multiply(t_hi, t_hi), 16), CC.multiply(l1[1], l1[1])),
                              hi(C0626)), CF.subtract(x1[0], lo(C666)))
    assert delerr < Dc("0.5")
    em1 = CC.subtract(exp_hi(delerr), ONE)                 # e^Delta - 1 (about 36 correct digits)
    SB = ONE
    PAe = ONE
    for n in range(2, MERR + 1):
        q2 = CC.multiply(t4_hi, CC.multiply(LNHI[n], LNHI[n]))
        SB = CC.add(SB, exp_hi(CC.subtract(q2, CF.multiply(s1ext, LNLO[n]))))
        PAe = CC.add(PAe, exp_hi(CC.subtract(q2, CF.multiply(s2ext, LNLO[n]))))
    laE = (LNLO[MERR], LNHI[MERR])
    SB = CC.add(SB, cap_hi(laE, lnN, s1ext, t_hi))
    PAe = CC.add(PAe, cap_hi(laE, lnN, s2ext, t_hi))
    Gerr = CC.multiply(exp_hi(CC.multiply(hi(C002), hi(YE[1]))), exp_hi(-CF.divide(CF.multiply(lo(YE[0]), l1[0]), 2)))
    Gerr_exact_max = exp_hi(CC.multiply(lo(YE[0]), CC.subtract(hi(C002), CF.divide(l1[0], 2))))
    results["tail.Gerr_exact_max_at_y_lo_hi"] = s(Gerr_exact_max)
    eAB = CC.multiply(em1, CC.add(SB, CC.multiply(Gerr, PAe)))
    ga1, gb1 = gates_fixed_left(laE, lnN, t_lo, s1ext)
    _, gb2 = gates_fixed_left(laE, lnN, t_lo, s2ext)
    gates["tail.GN-error.both_Merr_caps"] = (ga1 > 1 and gb1 > 1 and gb2 > 1)
    results["tail.GN-error.gates_lo"] = [s(ga1, 12), s(gb1, 12), s(gb2, 12)]
    gates["tail.Delta_N-monotonicity.(t^2/16)L(L-2)+0.626>0"] = (l1[0] > 2)
    gates["tail.eC0_quotient_N-monotonicity.3<10.50"] = (3 < C1050 and x1[0] > 12)
    # e_C0 (10.50 form), hull over (t, y) as in the package
    ln3 = ln_pair(3)
    p3 = add_hi(exp_hi(CC.multiply(hi(YE[1]), ln3[1])), exp_hi(CC.multiply(-lo(YE[0]), ln3[0])))
    absl = sqrt_hi(CC.add(CC.multiply(l1[1], l1[1]), CC.divide(CC.multiply(PI_HI, PI_HI), 4)))
    expo = add_hi(-CF.divide(CF.multiply(CF.add(ONE, lo(YE[0])), l1[0]), 4),
                  -CF.divide(CF.multiply(t_lo, CF.multiply(l1[0], l1[0])), 16),
                  CC.divide(CC.multiply(hi(C124), p3), CF.subtract(Dc(N), lo(F(1, 8)))),
                  CC.divide(CC.add(CC.multiply(3, absl), hi(C1050)), CF.subtract(x1[0], 12)))
    eC0 = exp_hi(expo)
    err = CC.add(eAB, eC0)
    results["tail.Delta_hi"] = s(delerr)
    results["tail.SB_hi"] = s(SB)
    results["tail.PAerr_hi"] = s(PAe)
    results["tail.Gerr_hi"] = s(Gerr)
    results["tail.eAB_hi"] = s(eAB)
    results["tail.eC0_hi"] = s(eC0)
    results["tail.err_hi"] = s(err)
    margin = CF.subtract(flow, err)
    marginp = CF.subtract(flowp, err)
    results["tail.margin_lo(with_OV)"] = s(margin)
    results["tail.marginprime_lo(without_OV)"] = s(marginp)
    gates["tail.decisive.flow>err>0"] = (flow > err > 0 and margin > 0)
    gates["tail.decisive.flow-err>0.00017352"] = margin > lo(F(17352, 10 ** 8))
    # comparison with the package's Arb transcript
    cmp = {}
    for key, mine in (("P", P), ("TR", TR), ("OV", OV), ("Mmax", MM), ("AB", AB), ("D", D), ("flow", flow),
                      ("eAB", eAB), ("eC0", eC0), ("err", err), ("margin", margin)):
        pk = Dc(PACKAGE_TAIL[key])
        lower = key in ("flow", "margin")
        cmp[key] = {"package": PACKAGE_TAIL[key], "this": s(mine), "relative_difference": s(CN.divide(mine - pk, pk), 3),
                    "package_is_more_conservative": bool(mine >= pk if lower else mine <= pk)}
    results["tail.comparison_with_package_transcript"] = cmp


# ----------------------------------------------------------------------------- Proposition 4.10


def prop410(results, gates):
    N0 = 690988
    M0 = 2000
    t_lo, t_hi = lo(T_LO), hi(T_HI)
    y0 = (sqrt_lo(lo(Y0SQ)), sqrt_hi(hi(Y0SQ)))
    ymax = (sqrt_lo(lo(YMAXSQ)), sqrt_hi(hi(YMAXSQ)))
    lnN0 = ln_pair(N0)
    lnm0 = ln_pair(M0)
    n2 = F(N0 * N0)
    q = (n2 - T_HI / 16, n2 - T_LO / 16)
    log0 = (ln_lo(lo(q[0])), ln_hi(hi(q[1])))
    x0 = (CF.multiply(CF.multiply(4, PI_LO), lo(q[0])), CC.multiply(CC.multiply(4, PI_HI), hi(q[1])))
    z = (T_LO / (16 * n2), T_HI / (16 * n2))
    gates["prop410.exact.target_identity"] = (T_LO + Y0SQ / 2 == F(893927, 5000000))
    gates["prop410.exact.tbox"] = (T_LO == F(161250000, 10 ** 9) and T_HI <= F(1, 4))
    gates["prop410.exact.floor>coarse_budget"] = F(791366, 10 ** 12) > F(234, 10 ** 9)
    gates["prop410.exact.0<y0^2<ymax^2<=1"] = (0 < Y0SQ < YMAXSQ <= 1)
    gates["prop410.domain.0<z<1"] = (0 < z[0] and z[1] < 1)
    gates["prop410.domain.x0>12"] = x0[0] > 12
    gates["prop410.domain.logN0>logm0"] = lnN0[0] > lnm0[1]
    gates["prop410.domain.N0-1/8>0"] = N0 > F(1, 8)
    zz = hi(z[1] / (1 - z[1]))
    delta1 = add_hi(CC.multiply(CC.divide(t_hi, 4), zz), CC.divide(t_hi, CF.multiply(2, CF.multiply(x0[0], x0[0]))))
    sigma1 = CF.subtract(add_lo(CF.divide(CF.add(ONE, y0[0]), 2), CF.multiply(CF.divide(t_lo, 2), lnN0[0])), delta1)
    y1 = add_hi(hi(C002), -CF.divide(log0[0], 2), CC.divide(lnN0[1], 2))
    kappa = CC.divide(t_hi, CF.multiply(2, CF.subtract(x0[0], 6)))
    gates["prop410.G0_positive_part.8/x0^2<3y0"] = CC.divide(8, CF.multiply(x0[0], x0[0])) < CF.multiply(3, y0[0])
    gates["prop410.sigma1>0"] = sigma1 > 0
    gates["prop410.Y1<0"] = y1 < 0
    gates["prop410.0<kappa<1"] = (0 < kappa < 1)
    gates["prop410.U1_log_domain.log0>2"] = log0[0] > 2
    gates["prop410.U2_logN0>1/2"] = lnN0[0] > Dc("0.5")
    u3a = CF.subtract(CF.divide(CF.add(ONE, y0[0]), 2), delta1)
    gates["prop410.U3a.(1+y0)/2-delta1>0"] = u3a > 0
    inv_w = CC.divide(ONE, CF.subtract(lnN0[0], lnm0[1]))
    gt1 = CC.add(-CF.multiply(CF.divide(t_lo, 2), lnm0[0]), inv_w)
    gt2 = add_hi(CC.divide(CC.subtract(ONE, y0[0]), 2), delta1, -CF.multiply(CF.divide(t_lo, 2), lnN0[0]), inv_w)
    gates["prop410.U3b.g_t1<0"] = gt1 < 0
    gates["prop410.U3c.g_t2<0"] = gt2 < 0
    gates["prop410.U5.3/10.50<1"] = F(3) / C1050 < 1
    results["prop410.delta1_hi"] = s(delta1)
    results["prop410.sigma1_lo"] = s(sigma1)
    results["prop410.Y1_hi"] = s(y1, 12)
    results["prop410.kappa_hi"] = s(kappa)
    results["prop410.g_t1_hi"] = s(gt1, 12)
    results["prop410.g_t2_hi"] = s(gt2, 12)
    # U1: delta in the epsilon bound, maximal at x0 (L > 2) and at n = 1
    u1 = CC.divide(CC.add(CC.multiply(CC.divide(CC.multiply(t_hi, t_hi), 16), CC.multiply(log0[1], log0[1])),
                          hi(C0626)), CF.subtract(x0[0], lo(C666)))
    # U2: 1 + |gamma| N^|kappa| n^y <= 1 + e^{0.02} (1 - z)^{-1/2} exp(t log N0/(2(x0 - 6)))
    pm = CC.add(ONE, CC.multiply(CC.multiply(exp_hi(hi(C002)), CC.divide(ONE, sqrt_lo(lo(1 - z[1])))),
                                 exp_hi(CC.divide(CC.multiply(t_hi, lnN0[1]), CF.multiply(2, CF.subtract(x0[0], 6))))))
    # U3: sum_{n<=N} b_n n^{-sigma1} <= 1 + head(2..m0) + cap(m0, N0)
    t4_hi = CC.divide(t_hi, 4)
    head = ZERO
    for n in range(2, M0 + 1):
        a, b = ln_pair(n)
        head = CC.add(head, exp_hi(CC.subtract(CC.multiply(t4_hi, CC.multiply(b, b)), CF.multiply(sigma1, a))))
    cap = cap_hi(lnm0, lnN0, sigma1, t_hi)
    smax = add_hi(ONE, head, cap)
    em1 = CC.subtract(exp_hi(u1), ONE)
    eAB = CC.multiply(CC.multiply(pm, smax), em1)
    # U4/U5: e_C0 (10.50 form); factors maximised separately
    ln3 = ln_pair(3)
    p3 = add_hi(exp_hi(CC.multiply(ymax[1], ln3[1])), exp_hi(-CF.multiply(ymax[0], ln3[0])))
    absl = sqrt_hi(CC.add(CC.multiply(log0[1], log0[1]), CC.divide(CC.multiply(PI_HI, PI_HI), 4)))
    expo = add_hi(-CF.divide(CF.multiply(CF.add(ONE, y0[0]), log0[0]), 4),
                  -CF.divide(CF.multiply(t_lo, CF.multiply(log0[0], log0[0])), 16),
                  CC.divide(CC.multiply(hi(C124), p3), CF.subtract(Dc(N0), lo(F(1, 8)))),
                  CC.divide(CC.add(CC.multiply(3, absl), hi(C1050)), CF.subtract(x0[0], 12)))
    eC0 = exp_hi(expo)
    emax = CC.add(eAB, eC0)
    tmin = lo(F(791366, 10 ** 12))
    lcert = Dc("7.9136674559412E-7")   # note 3, certified lower bound of L_690988(t0, y0)
    results["prop410.U1max_hi"] = s(u1)
    results["prop410.Pmax_hi"] = s(pm)
    results["prop410.head_hi"] = s(head)
    results["prop410.cap_hi"] = s(cap)
    results["prop410.Smax_hi"] = s(smax)
    results["prop410.eAB_hi"] = s(eAB)
    results["prop410.eC0_hi"] = s(eC0)
    results["prop410.Emax_hi"] = s(emax)
    results["prop410.Tmin-Emax_lo"] = s(CF.subtract(tmin, emax))
    results["prop410.Lcert-Emax_lo"] = s(CF.subtract(lcert, emax))
    results["prop410.Lcert/Emax_lo"] = s(CF.divide(lcert, emax), 8)
    results["prop410.Tmin/Emax_lo"] = s(CF.divide(tmin, emax), 8)
    gates["prop410.decisive.eAB<206/10^14"] = eAB < lo(F(206, 10 ** 14))
    gates["prop410.decisive.eC0<stated"] = eC0 < lo(F(233492848188649183, 10 ** 24))
    gates["prop410.decisive.Emax<stated"] = emax < lo(F(233494905212337849, 10 ** 24))
    gates["prop410.decisive.Emax<234/10^9"] = emax < lo(F(234, 10 ** 9))
    gates["prop410.decisive.Tmin-Emax>557/10^9"] = CF.subtract(tmin, emax) > hi(F(557, 10 ** 9))
    cmp = {}
    for key, mine in (("eAB", eAB), ("eC0", eC0), ("Emax", emax), ("head", head), ("cap", cap), ("Smax", smax),
                      ("Pmax", pm), ("U1max", u1)):
        pk = Dc(PACKAGE_PROP410[key])
        cmp[key] = {"package": PACKAGE_PROP410[key], "this": s(mine), "relative_difference": s(CN.divide(mine - pk, pk), 3),
                    "package_is_more_conservative": bool(mine <= pk)}
    results["prop410.comparison_with_package_transcript"] = cmp


# ----------------------------------------------------------------------------- self-tests


def selftest(results):
    out = {}
    # (a) partition (4.3), coefficientwise, exact integers, reduced size
    S = [1, 2, 3, 4, 5, 6, 7, 10, 11, 13, 14]
    lam = {1: 10 ** 6, 2: -1021000, 3: -1054000, 4: -45000, 5: -1119000, 6: 1001000, 7: -1043000,
           10: 1024000, 11: -805000, 13: -894000, 14: 912746}
    rng = random.Random(20261012)
    ok = True
    cases = []
    for (Mr, Nr) in ((500, 2000), (153, 154), (997, 5000), (14, 15)):
        w = [0] + [rng.randint(1, 10 ** 6) for _ in range(Nr)]
        w[1] = 1
        lhs = {}
        for d in S:
            for k in range(1, Nr + 1):
                lhs[d * k] = lhs.get(d * k, 0) + lam[d] * w[k]
        rhs = {}
        c = {}
        for d in S:
            for k in range(1, Mr // d + 1):
                c[d * k] = c.get(d * k, 0) + lam[d] * w[k]
        for m, v in c.items():
            rhs[m] = rhs.get(m, 0) + v
        for d in S:
            for k in range(Mr // d + 1, Nr + 1):
                rhs[d * k] = rhs.get(d * k, 0) + lam[d] * w[k]
        same = (lhs == rhs) and c.get(1) == lam[1]
        ok = ok and same
        cases.append({"M": Mr, "N": Nr, "identical": same})
    out["partition_(4.3)_coefficientwise_exact"] = {"ok": ok, "cases": cases}
    # (b) pi and the padded transcendental enclosures against 2*PREC-digit values
    hp = Context(prec=2 * PREC, rounding=ROUND_HALF_EVEN)
    a5 = atan_inv(5, 120)
    a239 = atan_inv(239, 50)
    pi_ref = 16 * a5[0] - 4 * a239[1]
    out["pi_enclosure"] = {"ok": PI_LO <= hp.divide(Dc(pi_ref.numerator), Dc(pi_ref.denominator)) <= PI_HI,
                           "math.pi_inside": PI_LO <= Dc(math.pi) + Dc("1e-15") and Dc(math.pi) - Dc("1e-15") <= PI_HI}
    bad = 0
    for i in range(2000):
        x = Dc(rng.uniform(-30, 30)).quantize(Dc("1E-20"))
        u = Dc(rng.uniform(1e-3, 1e7)).quantize(Dc("1E-12"))
        ex = hp.exp(x)
        lu = hp.ln(u)
        sq = hp.sqrt(u)
        if not (exp_lo(x) <= ex <= exp_hi(x) and ln_lo(u) <= lu <= ln_hi(u) and sqrt_lo(u) <= sq <= sqrt_hi(u)):
            bad += 1
    out["transcendental_enclosures_2000_random"] = {"ok": bad == 0, "violations": bad}
    # (c) endpoint-cap lemma on small cases (float exploration, not part of any decision)
    worst = 0.0
    for (tt, sg, a, c) in ((0.16125, 1.9, 50, 3000), (0.16125, 1.35, 200, 20000), (0.3, 3.0, 10, 1000)):
        lhs = sum(math.exp(tt / 4 * math.log(n) ** 2) * n ** (-sg) for n in range(a + 1, c + 1))
        e = lambda u: math.exp((1 - sg) * math.log(u) + tt / 4 * math.log(u) ** 2)
        rhs = max(e(a), e(c)) * math.log(c / a)
        worst = max(worst, lhs / rhs)
    out["endpoint_cap_lemma_float_ratio_max(must_be<1)"] = round(worst, 6)
    results["selftest"] = out
    return ok and out["pi_enclosure"]["ok"] and bad == 0 and worst < 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--output", help="JSON record path")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--part", choices=["all", "tail", "prop410"], default="all")
    args = ap.parse_args()
    t0 = time.time()
    results = {}
    gates = {}
    ok_self = True
    if args.selftest:
        ok_self = selftest(results)
    if args.part in ("all", "prop410"):
        prop410(results, gates)
    if args.part in ("all", "tail"):
        tail(results, gates)
    allpass = all(bool(v) for v in gates.values()) and ok_self
    rec = {"title": "Independent re-evaluation of the tail lemma and the uniform finite-lane error budget",
           "date": "2026-10-12", "model": "Claude Opus 5.5 (claude-opus-5-5)",
           "source_package": PACKAGE, "polymath_source": POLYMATH, "precision_digits": PREC,
           "part": args.part, "gates": {k: bool(v) for k, v in sorted(gates.items())},
           "results": results, "all_gates_pass": allpass,
           "software": {"python": platform.python_version(), "implementation": platform.python_implementation()}}
    with open(__file__, "rb") as fh:
        rec["checker_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    out = json.dumps(rec, indent=1, sort_keys=False)
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(out + "\n")
    for k, v in sorted(gates.items()):
        print(("PASS " if v else "FAIL ") + k)
    print("selftest:", "PASS" if ok_self else "FAIL") if args.selftest else None
    print("ALL PASS" if allpass else "FAILURE", "(%.1f s)" % (time.time() - t0), file=sys.stderr)
    return 0 if allpass else 1


if __name__ == "__main__":
    sys.exit(main())
