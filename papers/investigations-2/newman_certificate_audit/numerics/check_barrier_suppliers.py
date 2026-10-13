#!/usr/bin/env python3
"""Independent standard-library checks of the barrier suppliers of the pinned
Gomila package (hypothesis (iii) of Polymath Theorem 1.2).

Audited package: judegomila/dbn-lambda-01787854-candidate-audit at commit
a74738deb6d5e0f76887cb36901da08b68dca705 (seal 443/443):
BARRIER_CERTIFICATE.md, DERIVATIVE_BOX_LEMMA.md,
barrier/src/TloopSinglemat_closed_cert.c, barrier/src/verify_uniform_error_01787854.c
and the sealed transcript barrier/certificates/barrier_target_closed.log.

Box: R = [X, X+1] + i[0.1809, 1], X = 6000000185827, 0 <= t <= t0 = 129/800,
N = 690988 throughout.  Polymath inputs (arXiv:1904.12438v2, read from the
project's TeX source km-git-acc/dbn_upper_bound Writeup/debruijn.tex at
8e8a6ab): Theorem 1.3 bounds (20)--(23), the 10.50 form of Proposition
6.6(vi) (ERROR_CONSTANT_WELD.md), and Lemma 8.4 (derivative bounds).

Parts (each a rigorous computation with directed rounding: decimal at PREC
digits, + - * / with ROUND_FLOOR / ROUND_CEILING, exp / ln / sqrt correctly
rounded and padded by a relative 10^-(PREC-2); pi by Machin in rationals):

  1. uniform    The uniform approximation-error budget on R x [0, t0]
                (verify_uniform_error_01787854.c): N constant, the sum core,
                the prefactor, u_n, e_A + e_B, e_{C,0}, total < 0.00125.
  2. gates      The fail-closed gates of the derivative-box lemma: c_x > 0,
                h_y < 0, the A-core y-slope eta < 0, 2 log N < log(X/4 pi),
                the tail-exponent gate c0 > (1/2) log N and the tail
                monotonicity gate (y0 - 1)/2 + 1/log 16 < 0, with values.
  3. majorants  The Lemma 8.4 majorants of the program (endpoint-separated
                factors at (X, y0), log factors at X + 1 and y = 1) summed
                DIRECTLY over n = 1..N -- no head + integral, no quadrature --
                as upper bounds, at the seams of selected prisms (D_z) and on
                their closed time prisms (D_t, t-decorrelated: the decreasing
                heat factor at the left seam, the increasing factors at the
                right seam).  Compared with the integer ceilings of the
                transcript, which must not be smaller.
  4. transcript The sealed transcript, re-parsed: 883 prisms, consecutive
                byte-identical seams from exactly 0 to an enclosure of
                129/800, mesh = 4 Dz - 4, spatial = Dz/(2(Dz-1)), time =
                Dt (t_{i+1} - t_i), winding inside (-1/4, 1/4), and the gate
                min_mesh - spatial - time - 0.00125 > 0 recomputed from the
                printed ball endpoints in exact rationals; per-prism
                tolerances of D_z, D_t and of the joint majorants.
                Optionally the package's corroborating macOS/Clang/FLINT
                3.6.0 transcript is parsed the same way and compared with
                the canonical one prism by prism.
  5. taylor     The omitted-Taylor-term bound of StoredSumTaylorTail_cert.c:
                the hypotheses |Re D| < 0.694, |Im D| < 0.7855 for
                D = log(N/2) - alpha(u), u in {1 - s, conj(s)}, on the box
                (from explicit real formulas for alpha), the expansion
                radius |w| < 0.66, |gamma| < 0.089 from (20), and the direct
                sum sqrt(n0) sum_n n^{-1/2} (e^B I_A + e^A I_B) < 1e-20 with
                A = 0.66 |log(n/n0)|, B = 0.2 log(n/n0)^2/4, n0 = N/2, and
                the geometric tail bounds I = r^62/62!/(1 - r/63).

Prepared for Edward Baker with LLM assistance (Claude Opus 5.5,
claude-opus-5-5), 13 October 2026.  Internal check, not independent review.

Usage:
    python3 check_barrier_suppliers.py --transcript PATH/barrier_target_closed.log \\
        [--corroborating-transcript PATH/barrier_target_closed_macos_arm64_flint36.log] --output rec.json
(the retained record was produced with the two sealed transcripts of the
pinned package; about 9 minutes, almost all of it in parts 3 and 5).
"""
import argparse
import decimal
import hashlib
import json
import platform
import re
import sys
import time
from decimal import Context, Decimal as Dc, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from fractions import Fraction as F

PREC = 34
CN = Context(prec=PREC, rounding=ROUND_HALF_EVEN)
CF = Context(prec=PREC, rounding=ROUND_FLOOR)
CC = Context(prec=PREC, rounding=ROUND_CEILING)
decimal.setcontext(Context(prec=PREC, rounding=ROUND_HALF_EVEN))
ETA = Dc(10) ** (-(PREC - 2))
ONE = Dc(1)
ZERO = Dc(0)

TRANSCRIPT_SHA256 = "2d010f70902dca1627f40ddcd68f3954b37fd9596f7840787415eeafb20805f4"
MACOS_TRANSCRIPT_SHA256 = "34f8ed82bcb47a3783099206f67599cf975b7d28cfa398d8a765118311954db7"
PACKAGE = {"repository": "https://github.com/judegomila/dbn-lambda-01787854-candidate-audit",
           "commit": "a74738deb6d5e0f76887cb36901da08b68dca705",
           "transcript": "barrier/certificates/barrier_target_closed.log",
           "transcript_sha256": TRANSCRIPT_SHA256,
           "corroborating_transcript": "barrier/certificates/barrier_target_closed_macos_arm64_flint36.log",
           "corroborating_transcript_sha256": MACOS_TRANSCRIPT_SHA256}

X = 6000000185827
N = 690988
T0 = F(129, 800)
Y0 = F(1809, 10000)
ALLOW = F(125, 100000)        # 0.00125
HEAD = 16


def lo(fr):
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


def expm1_hi(u):
    """Upper bound of e^u - 1 for 0 <= u <= 1/2, in exact rationals:
    sum_{k>=1} u^k/k! <= u + u^2/2 + u^3/(6(1-u)).  (exp_hi(u) - 1 would lose
    about 10^-(PREC-2)/u in relative accuracy for tiny u.)"""
    U = F(u)
    assert 0 <= U <= F(1, 2)
    return hi(U + U * U / 2 + U ** 3 / (6 * (1 - U)))


def atan_inv(k, terms):
    s = F(0)
    for j in range(terms):
        s += F((-1) ** j, (2 * j + 1) * k ** (2 * j + 1))
    s2 = s + F((-1) ** terms, (2 * terms + 1) * k ** (2 * terms + 1))
    return (min(s, s2), max(s, s2))


def pi_enclosure():
    a5, a239 = atan_inv(5, 40), atan_inv(239, 16)
    return lo(16 * a5[0] - 4 * a239[1]), hi(16 * a5[1] - 4 * a239[0])


PI_LO, PI_HI = pi_enclosure()


def s(x, digits=20):
    return format(Context(prec=digits).plus(x), "E") if x != 0 else "0"


def add_hi(*xs):
    r = ZERO
    for v in xs:
        r = CC.add(r, v)
    return r


def add_lo(*xs):
    r = ZERO
    for v in xs:
        r = CF.add(r, v)
    return r


# ----------------------------------------------------------------------------- shared box constants

def box_constants():
    c = {}
    four_pi = (CF.multiply(4, PI_LO), CC.multiply(4, PI_HI))
    c["q_lo"] = CF.divide(Dc(X), four_pi[1])                 # X/(4 pi)
    c["q_hi"] = CC.divide(Dc(X), four_pi[0])
    c["qu_lo"] = CF.divide(Dc(X + 1), four_pi[1])            # (X+1)/(4 pi)
    c["qu_hi"] = CC.divide(Dc(X + 1), four_pi[0])
    c["L_lo"], c["L_hi"] = ln_lo(c["q_lo"]), ln_hi(c["q_hi"])
    c["Lu_lo"], c["Lu_hi"] = ln_lo(c["qu_lo"]), ln_hi(c["qu_hi"])
    c["lnN_lo"], c["lnN_hi"] = ln_lo(Dc(N)), ln_hi(Dc(N))
    c["inv_xm6_hi"] = hi(F(1, X - 6))
    c["inv_xm6_lo"] = lo(F(1, X - 6))
    return c


# ----------------------------------------------------------------------------- part 1


def part_uniform(res, gates):
    c = box_constants()
    # N(x,t) = floor(sqrt(x/4pi + t/16)) is increasing in x and t: check the two corners exactly
    for (xx, tt, name) in ((X, F(0), "corner (X,0)"), (X + 1, T0, "corner (X+1,t0)")):
        # N^2 <= x/(4 pi) + t/16 < (N+1)^2  <=>  4 pi (N^2 - t/16) <= x < 4 pi ((N+1)^2 - t/16)
        lower_ok = CC.multiply(CC.multiply(4, PI_HI), hi(F(N * N) - tt / 16)) <= Dc(xx)
        upper_ok = Dc(xx) < CF.multiply(CF.multiply(4, PI_LO), lo(F((N + 1) ** 2) - tt / 16))
        gates["uniform.N=690988_at_" + name] = bool(lower_ok and upper_ok)
    gates["uniform.N^2<X/(4pi)"] = Dc(N * N) < c["q_lo"]
    gates["uniform.2logN<log(X/4pi)"] = CC.multiply(2, c["lnN_hi"]) < c["L_lo"]
    a = F(1, 2) * (1 + Y0)
    delta = F(1) * T0 * (1 + F(8, X * X)) / (2 * X * X)
    aeff = a - delta
    gates["uniform.0<a_eff<1"] = (0 < aeff < 1)
    # S <= 1 + (N^{1-a_eff} - 1)/(1 - a_eff)
    one_m = lo(1 - aeff)
    one_m_hi = hi(1 - aeff)
    Npow = exp_hi(CC.multiply(one_m_hi, c["lnN_hi"]))
    smax = CC.add(ONE, CC.divide(CC.subtract(Npow, ONE), one_m))
    kap = exp_hi(CC.multiply(CC.multiply(hi(T0), c["lnN_hi"]), CC.divide(c["inv_xm6_hi"], 2)))
    pmax = CC.add(ONE, CC.multiply(exp_hi(hi(F(1, 50))), kap))
    umax = CC.divide(CC.add(CC.multiply(CC.divide(CC.multiply(hi(T0), hi(T0)), 16), CC.multiply(c["Lu_hi"], c["Lu_hi"])),
                            hi(F(626, 1000))), lo(F(X) - F(666, 100)))
    eab = CC.multiply(CC.multiply(pmax, smax), expm1_hi(umax))
    f1 = exp_hi(-CF.multiply(CF.divide(CF.add(ONE, lo(Y0)), 4), c["L_lo"]))       # (X/4pi)^{-(1+ymin)/4}
    e2 = CC.divide(CC.multiply(hi(F(124, 100)), hi(F(10, 3))), lo(F(N) - F(1, 8)))  # 1.24 (3 + 1/3)/(N - 1/8)
    absl = sqrt_hi(CC.add(CC.multiply(c["Lu_hi"], c["Lu_hi"]), CC.divide(CC.multiply(PI_HI, PI_HI), 4)))
    e3 = CC.divide(CC.add(CC.multiply(3, absl), hi(F(21, 2))), lo(F(X - 12)))
    ec0 = CC.multiply(f1, exp_hi(CC.add(e2, e3)))
    tot = CC.add(eab, ec0)
    res["uniform.a_eff"] = str(aeff)
    res["uniform.sum_core_hi"] = s(smax)
    res["uniform.prefactor_hi"] = s(pmax)
    res["uniform.u_n_hi"] = s(umax)
    res["uniform.eAB_hi"] = s(eab)
    res["uniform.eC0_hi"] = s(ec0)
    res["uniform.total_hi"] = s(tot)
    res["uniform.total_hi_all_digits"] = s(tot, PREC)
    res["uniform.package_total_upper"] = "3.565230116000396683802985102688090540476E-4"
    res["uniform.total_hi_minus_package_upper"] = s(CC.subtract(tot, Dc("3.565230116000396683802985102688090540476E-4")), 4)
    gates["uniform.total<0.00125"] = tot < lo(ALLOW)
    gates["uniform.total<=package_total+1e-30"] = tot <= Dc("3.565230116000396683802985102688090540476E-4") + Dc("1E-30")


# ----------------------------------------------------------------------------- part 2


def part_gates(res, gates):
    c = box_constants()
    y0 = Y0
    # c_x > 0: 1/(4(X+1)) - 2/X^3 > 0 (with X^2 > 8)
    gates["gates.X^2>8"] = X * X > 8
    gates["gates.c_x>0:1/(4(X+1))-2/X^3>0"] = F(1, 4 * (X + 1)) - F(2, X ** 3) > 0
    # h_y = -3 + 4(1+2y)/x^2 < 0 on 0 <= y <= 1: 12/X^2 - 3 < 0
    gates["gates.h_y<0:12/X^2-3<0"] = F(12, X * X) - 3 < 0
    # A-core y-slope: 0.02 - log(X/4pi)/2 + t0 log N/(2(X-6)) + log(N)/2 < 0
    eta = add_hi(hi(F(1, 50)), -CF.divide(c["L_lo"], 2),
                 CC.multiply(CC.multiply(hi(T0), c["lnN_hi"]), CC.divide(c["inv_xm6_hi"], 2)),
                 CC.divide(c["lnN_hi"], 2))
    res["gates.eta_hi"] = s(eta, 12)
    gates["gates.A-core_y-slope_eta<0"] = eta < 0
    # const1 = c(X, y0) = log(X/4pi)/4 - (1 - 3y0 + 4y0(1+y0)/X^2)_+/(2X^2)
    hpos = max(F(0), 1 - 3 * y0 + 4 * y0 * (1 + y0) / (X * X))
    c0_lo = CF.subtract(CF.divide(c["L_lo"], 4), hi(hpos / (2 * X * X)))
    c0_hi = CC.subtract(CC.divide(c["L_hi"], 4), lo(hpos / (2 * X * X)))
    res["gates.const1"] = [s(c0_lo, 25), s(c0_hi, 25)]
    gates["gates.tail_exponent:c0>(1/2)logN"] = c0_lo > CC.divide(c["lnN_hi"], 2)
    res["gates.tail_exponent_margin_lo"] = s(CF.subtract(c0_lo, CC.divide(c["lnN_hi"], 2)), 12)
    # the positive part of (21) at (X, y0) and its weight in const1
    res["gates.const1_positive_part_term_hi"] = s(hi(hpos / (2 * X * X)), 6)
    tm = CC.add(hi((y0 - 1) / 2), CC.divide(ONE, ln_lo(Dc(HEAD))))
    res["gates.tail_monotonicity_value_hi"] = s(tm, 12)
    gates["gates.tail_monotonicity:(y0-1)/2+1/log16<0"] = tm < 0
    gates["gates.bracket_positivity:2logN<log(X/4pi)"] = CC.multiply(2, c["lnN_hi"]) < c["L_lo"]
    return c0_lo


# ----------------------------------------------------------------------------- part 3


def majorant_tables():
    """ln n (lo, hi) and n^{y0} (hi) for n = 1..N."""
    lnlo = [ZERO] * (N + 1)
    lnhi = [ZERO] * (N + 1)
    ny_hi = [ONE] * (N + 1)
    y0hi = hi(Y0)
    for n in range(2, N + 1):
        d = Dc(n)
        a, b = ln_lo(d), ln_hi(d)
        lnlo[n], lnhi[n] = a, b
        ny_hi[n] = exp_hi(CC.multiply(y0hi, b))
    return lnlo, lnhi, ny_hi


def afac_hi(c, t_hi):
    # e^{0.02 y0} (X/4pi)^{-y0/2} N^{t y0/(2(X-6))}, increasing in t
    e1 = CC.multiply(hi(F(1, 50)), hi(Y0))
    e2 = -CF.multiply(CF.divide(lo(Y0), 2), c["L_lo"])
    e3 = CC.multiply(CC.multiply(CC.multiply(t_hi, hi(Y0)), CC.divide(c["inv_xm6_hi"], 2)), c["lnN_hi"])
    return exp_hi(add_hi(e1, e2, e3))


def direct_majorants(c, c0_lo, tabs, ta, tb):
    """Upper bounds of the program's Lemma 8.4 majorant sums over n = 1..N, for t in [ta, tb]:
    D_z(t) majorant and D_t majorant, summed directly.  Heat factor at ta (decreasing in t),
    afac and the t/(4(x-6)) factor at tb (increasing)."""
    lnlo, lnhi, ny_hi = tabs
    ta_lo, tb_hi = lo(ta), hi(tb)
    af = afac_hi(c, tb_hi)
    tq = CC.multiply(CC.divide(tb_hi, 4), c["inv_xm6_hi"])                    # t/(4(X-6))
    half_plus = CC.add(lo(F(1, 2)), tq)
    # L1 = log(|2 + i(X+1)|/4pi) + pi + 3/X, the A-bracket factor of D_z
    mod_hi = sqrt_hi(hi(F(4) + F(X + 1) ** 2))
    L1 = add_hi(ln_hi(CC.divide(mod_hi, CF.multiply(4, PI_LO))), PI_HI, hi(F(3, X)))
    est_z = CC.multiply(CC.multiply(L1, af), half_plus)
    # D_t constants: C2 = log((X+1)/4pi)/4 + pi/8 + 2/(X-6); E2 = (1/4)(pi/2 + 8/(X-6))(log((X+1)/4pi) + 8/(X-6))
    C2 = add_hi(CC.divide(c["Lu_hi"], 4), CC.divide(PI_HI, 8), CC.multiply(2, c["inv_xm6_hi"]))
    E2 = CC.divide(CC.multiply(add_hi(CC.divide(PI_HI, 2), CC.multiply(8, c["inv_xm6_hi"])),
                               add_hi(c["Lu_hi"], CC.multiply(8, c["inv_xm6_hi"]))), 4)
    est_t = CC.multiply(E2, af)
    base = CF.divide(CF.add(ONE, lo(Y0)), 2)                                  # (1+y0)/2 lower
    dz = ZERO
    dt = ZERO
    dz_head = ZERO
    dt_head = ZERO
    for n in range(1, N + 1):
        if n == 1:
            # log n = 0: P = 1; D_z term = afac * L1 * (1/2 + t/(4(X-6)));  D_t term = afac * E2
            tz = est_z
            tt = est_t
        else:
            a, b = lnlo[n], lnhi[n]
            # exponent of P = -(1+y0)/2 log n + t (log^2 n / 4 - c0 log n), upper bound at t = ta (bracket <= 0)
            br = CC.subtract(CC.divide(CC.multiply(b, b), 4), CF.multiply(c0_lo, a))
            assert br < 0
            ex = CC.add(-CF.multiply(base, a), CC.multiply(ta_lo, br))
            P = exp_hi(ex)
            Ay = CC.multiply(af, ny_hi[n])                                       # afac n^{y0}
            # D_z: log n (1/2 + tq (1 + afac n^y)) + n^y est_z
            tz = add_hi(CC.multiply(b, CC.add(lo(F(1, 2)), CC.multiply(tq, CC.add(ONE, Ay)))),
                        CC.multiply(ny_hi[n], est_z))
            tz = CC.multiply(P, tz)
            # D_t: (1 + afac n^y) log n (C2 - log n /4) + n^y est_t
            brt = CC.multiply(b, CC.subtract(C2, CF.divide(a, 4)))
            assert brt > 0
            tt = add_hi(CC.multiply(CC.add(ONE, Ay), brt), CC.multiply(ny_hi[n], est_t))
            tt = CC.multiply(P, tt)
        dz = CC.add(dz, tz)
        dt = CC.add(dt, tt)
        if n <= HEAD:
            dz_head = CC.add(dz_head, tz)
            dt_head = CC.add(dt_head, tt)
    return dz, dt, dz_head, dt_head


# ----------------------------------------------------------------------------- part 4

BALL = re.compile(r"\[([-+0-9.eE]+) \+/- ([0-9.eE+-]+)\]")


def ball(tok):
    """Exact rational enclosure [lo, hi] of an Arb-printed ball or plain decimal."""
    tok = tok.strip()
    m = BALL.fullmatch(tok)
    if m:
        mid, rad = F(Dc(m.group(1))), F(Dc(m.group(2)))
        return mid - rad, mid + rad
    m = re.fullmatch(r"\[\+/- ([0-9.eE+-]+)\]", tok)
    if m:
        rad = F(Dc(m.group(1)))
        return -rad, rad
    v = F(Dc(tok))
    return v, v


PRISM = re.compile(r"^Prism\((\d+)\) t=\[(.*?),(\[[^\]]*\]|[^\],]*)\] winding=(\S+(?: \S+ \S+)?) min_mesh=(.*?) Dz=(\S+) "
                   r"Dt=(\S+) spatial=(.*?) time=(.*?) eps=(.*?) margin=(.*?) mesh=(\d+) PASS$")


def split_t(seg):
    """Split 'A,B' where A and B are balls or plain decimals."""
    if seg.startswith("["):
        k = seg.index("]") + 1
        return seg[:k], seg[k + 1:]
    k = seg.index(",")
    return seg[:k], seg[k + 1:]


def part_transcript(path, res, gates, label="transcript", expected_sha=TRANSCRIPT_SHA256):
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    res[label + ".sha256"] = sha
    gates[label + ".sha256_matches_seal"] = (sha == expected_sha)
    prisms = []
    for line in raw.decode().splitlines():
        if not line.startswith("Prism("):
            continue
        k = int(line[6:line.index(")")])
        t_seg = line[line.index("t=[") + 3:line.index("] winding=")]
        ta_s, tb_s = split_t(t_seg)
        rest = line[line.index("] winding=") + 10:]
        fields = {}
        for key in ("winding", "min_mesh", "Dz", "Dt", "spatial", "time", "eps", "margin", "mesh"):
            pass
        # tokenise " key=value" pairs; values may contain spaces inside brackets
        toks = re.findall(r"(winding|min_mesh|Dz|Dt|spatial|time|eps|margin|mesh)=(\[[^\]]*\]|\S+)", "winding=" + rest)
        for key, val in toks:
            fields[key] = val
        prisms.append({"k": k, "ta": ta_s, "tb": tb_s, **fields})
    gates[label + ".883_prisms_numbered_1..883"] = ([p["k"] for p in prisms] == list(range(1, 884)))
    seams_ok = all(prisms[i]["tb"] == prisms[i + 1]["ta"] for i in range(len(prisms) - 1))
    gates[label + ".seams_byte_identical"] = seams_ok
    gates[label + ".first_seam_exactly_0"] = (prisms[0]["ta"] == "0")
    lt, ht = ball(prisms[-1]["tb"])
    gates[label + ".last_seam_encloses_129/800"] = (lt <= T0 <= ht)
    worst = None
    rows = []
    allok = True
    for p in prisms:
        dz = ball(p["Dz"])
        dt = ball(p["Dt"])
        assert dz[0] == dz[1] and dt[0] == dt[1] and dz[0].denominator == 1 and dt[0].denominator == 1
        Dz, Dt = dz[0], dt[0]
        num = int(Dz)
        mesh_ok = int(p["mesh"]) == 4 * num - 4
        sp = ball(p["spatial"])
        sp_exact = F(Dz) / (2 * (num - 1))
        sp_ok = sp[0] <= sp_exact <= sp[1]
        ta, tb = ball(p["ta"]), ball(p["tb"])
        dtau_hi = tb[1] - ta[0]
        tm = ball(p["time"])
        tm_ok = tm[1] >= Dt * (tb[0] - ta[1])           # printed time error encloses Dt*(t_{i+1}-t_i)
        mm = ball(p["min_mesh"])
        w = ball(p["winding"])
        w_ok = (-F(1, 4) < w[0] and w[1] < F(1, 4))
        eps = ball(p["eps"])
        eps_ok = eps[0] <= ALLOW <= eps[1]
        # recomputed gate: min_mesh_lo - spatial_exact - Dt*(tb_hi - ta_lo) - 0.00125 > 0
        margin = mm[0] - sp_exact - Dt * dtau_hi - ALLOW
        ok = mesh_ok and sp_ok and tm_ok and w_ok and eps_ok and margin > 0
        allok = allok and ok
        # tolerances (others fixed): D_z alone, D_t alone, joint
        avail = mm[0] - ALLOW
        tol_z = (avail - Dt * dtau_hi) / sp_exact
        tol_t = (avail - sp_exact) / (Dt * dtau_hi)
        tol_j = avail / (sp_exact + Dt * dtau_hi)
        row = {"k": p["k"], "Dz": int(Dz), "Dt": int(Dt), "margin_lo": float(margin),
               "tol_Dz": float(tol_z), "tol_Dt": float(tol_t), "tol_joint": float(tol_j)}
        rows.append(row)
        if worst is None or margin < worst[0]:
            worst = (margin, p["k"])
    gates[label + ".every_prism_gate_recomputed_positive"] = allok
    res[label + ".min_recomputed_margin"] = {"prism": worst[1], "margin_lo": s(Dc(worst[0].numerator) / Dc(worst[0].denominator), 21)}
    for key in ("tol_Dz", "tol_Dt", "tol_joint"):
        m = min(rows, key=lambda r: r[key])
        res[label + ".min_" + key] = {"prism": m["k"], "value": round(m[key], 6)}
    res[label + ".prisms"] = len(prisms)
    res[label + ".mesh_evaluations"] = sum(4 * r["Dz"] - 4 for r in rows)
    return prisms, rows


# ----------------------------------------------------------------------------- main


def cross_transcripts(pa, ra, pb, rb, res, gates):
    """Prism-by-prism comparison of two complete transcripts of the same sealed source."""
    gates["cross.same_prism_count"] = (len(pa) == len(pb))
    gates["cross.identical_Dz_Dt_mesh"] = all(a["Dz"] == b["Dz"] and a["Dt"] == b["Dt"] and a["mesh"] == b["mesh"]
                                              for a, b in zip(pa, pb))
    same_seams = sum(1 for a, b in zip(pa, pb) if a["tb"] == b["tb"])
    dseam = max(abs(sum(ball(a["tb"])) / 2 - sum(ball(b["tb"])) / 2) for a, b in zip(pa, pb))
    dmm = max(abs(sum(ball(a["min_mesh"])) / 2 - sum(ball(b["min_mesh"])) / 2) for a, b in zip(pa, pb))
    res["cross.right_seams_byte_identical_count"] = same_seams
    res["cross.max_abs_seam_midpoint_difference"] = float(dseam)
    res["cross.max_abs_min_mesh_midpoint_difference"] = float(dmm)
    ma = min(r["margin_lo"] for r in ra)
    mb = min(r["margin_lo"] for r in rb)
    res["cross.smaller_min_margin_float"] = min(ma, mb)


def part_taylor(res, gates, tabs):
    """Part 5: the omitted-Taylor-term bound of StoredSumTaylorTail_cert.c, from its hypotheses."""
    import math
    lnlo, lnhi, _ = tabs
    n0i = N // 2
    assert 2 * n0i == N
    l0_lo, l0_hi = lnlo[n0i], lnhi[n0i]
    c = box_constants()
    # u = (a - i x)/2 with a in [0, 2] (a = 1 + y for u = 1 - s, a = 1 - y for u = conj s), x in [X, X+1]:
    #   Re alpha(u) = a/(a^2+x^2) + 2(a-2)/((a-2)^2+x^2) + (1/2) log(sqrt(a^2+x^2)/(4 pi))
    #   Im alpha(u) = x/(a^2+x^2) + 2x/((a-2)^2+x^2) - (1/2)(pi/2 - atan(a/x))
    re_al_lo = CF.subtract(CF.divide(c["L_lo"], 2), hi(F(4, X * X)))
    mod_hi = sqrt_hi(hi(F(4) + F(X + 1) ** 2))
    re_al_hi = CC.add(CC.divide(ln_hi(CC.divide(mod_hi, CF.multiply(4, PI_LO))), 2), hi(F(2, X * X)))
    reD_lo, reD_hi = CF.subtract(l0_lo, re_al_hi), CC.subtract(l0_hi, re_al_lo)
    gates["taylor.Re_D<0_on_box"] = reD_hi < 0
    abs_reD = -reD_lo
    imD_lo, imD_hi = CF.subtract(CF.divide(PI_LO, 4), hi(F(4, X))), CC.divide(PI_HI, 4)
    gates["taylor.Im_D>0_on_box"] = imD_lo > 0
    abs_imD = imD_hi
    res["taylor.|Re D|_hi"] = s(abs_reD, 16)
    res["taylor.|Im D|_hi"] = s(abs_imD, 16)
    gates["taylor.|Re D|<0.694"] = abs_reD < Dc("0.694")
    gates["taylor.|Im D|<0.7855"] = abs_imD < Dc("0.7855")
    # |w| <= hypot(|Re base| + T|Re D|/2, |Im base| + T|Im D|/2), |Re base| <= 1/2, |Im base| <= 1/4
    for name, T, dre, dim in (("package_constants_T=0.1809", F(1809, 10000), Dc("0.694"), Dc("0.7855")),
                              ("these_bounds_T=0.1809", F(1809, 10000), abs_reD, abs_imD),
                              ("these_bounds_T=t0", T0, abs_reD, abs_imD)):
        wr = CC.add(hi(F(1, 2)), CC.multiply(hi(T / 2), dre))
        wi = CC.add(hi(F(1, 4)), CC.multiply(hi(T / 2), dim))
        wmod = sqrt_hi(CC.add(CC.multiply(wr, wr), CC.multiply(wi, wi)))
        res["taylor.|w|_hi_" + name] = s(wmod, 16)
        gates["taylor.|w|<0.66_" + name] = wmod < Dc("0.66")
    # prefactors: Re alpha >= (1/2) log n0 bounds the B prefactor by 1 and the A prefactor by |gamma| sqrt(n0)
    gates["taylor.Re_alpha>(1/2)log_n0"] = re_al_lo > CC.divide(l0_hi, 2)
    g_hi = exp_hi(CC.add(CC.multiply(hi(F(1, 50)), hi(Y0)), -CF.multiply(CF.divide(lo(Y0), 2), c["L_lo"])))
    res["taylor.|gamma|_hi_from_(20)"] = s(g_hi, 16)
    gates["taylor.|gamma|<0.089"] = g_hi < Dc("0.089")
    gates["taylor.1+0.089*sqrt(n0)<sqrt(n0)"] = CC.add(ONE, CC.multiply(Dc("0.089"), sqrt_hi(Dc(n0i)))) < sqrt_lo(Dc(n0i))
    # the direct finite sum of the termwise remainder majorant, m = 62 first omitted index
    m = 62
    lnfact_lo = ln_lo(Dc(math.factorial(m)))
    k066, k005 = Dc("0.66"), Dc("0.05")
    total = ZERO
    for n in range(1, N + 1):
        if n == n0i:
            continue
        a_lo, a_hi = (ZERO, ZERO) if n == 1 else (lnlo[n], lnhi[n])
        labs = max(CC.subtract(a_hi, l0_lo), CC.subtract(l0_hi, a_lo))
        A = CC.multiply(k066, labs)
        B = CC.multiply(CC.multiply(labs, labs), k005)
        IA = CC.divide(exp_hi(CC.subtract(CC.multiply(m, ln_hi(A)), lnfact_lo)), CF.subtract(ONE, CC.divide(A, m + 1)))
        IB = CC.divide(exp_hi(CC.subtract(CC.multiply(m, ln_hi(B)), lnfact_lo)), CF.subtract(ONE, CC.divide(B, m + 1)))
        term = CC.add(CC.multiply(exp_hi(B), IA), CC.multiply(exp_hi(A), IB))
        total = CC.add(total, CC.divide(term, ONE if n == 1 else sqrt_lo(Dc(n))))
    total = CC.multiply(total, sqrt_hi(Dc(n0i)))
    res["taylor.truncation_total_hi"] = s(total, 16)
    res["taylor.package_truncation_total"] = "1.95423459324476106401834086256e-22"
    gates["taylor.truncation_total<1e-20"] = total < Dc("1e-20")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--transcript", required=True, help="barrier/certificates/barrier_target_closed.log of the pinned package")
    ap.add_argument("--corroborating-transcript", help="barrier/certificates/barrier_target_closed_macos_arm64_flint36.log")
    ap.add_argument("--output")
    ap.add_argument("--prisms", default="1,2,441,882,883", help="prisms whose D_z, D_t are recomputed by direct summation")
    args = ap.parse_args()
    t_start = time.time()
    res, gates = {}, {}
    part_uniform(res, gates)
    c0_lo = part_gates(res, gates)
    prisms, rows = part_transcript(args.transcript, res, gates)
    if args.corroborating_transcript:
        pm, rm = part_transcript(args.corroborating_transcript, res, gates, "transcript_macos", MACOS_TRANSCRIPT_SHA256)
        cross_transcripts(prisms, rows, pm, rm, res, gates)
    c = box_constants()
    tabs = majorant_tables()
    part_taylor(res, gates, tabs)
    sel = [int(v) for v in args.prisms.split(",")]
    maj = []
    for k in sel:
        p = prisms[k - 1]
        ta = ball(p["ta"])
        tb = ball(p["tb"])
        # D_z at the seam t_k (its printed enclosure); D_t on the closed prism [t_k, t_{k+1}]
        dz, _, dz_head, _ = direct_majorants(c, c0_lo, tabs, ta[0], ta[1])
        _, dt, _, dt_head = direct_majorants(c, c0_lo, tabs, ta[0], tb[1])
        Dz = int(ball(p["Dz"])[0])
        Dt = int(ball(p["Dt"])[0])
        ok = (dz <= Dz and dt <= Dt)
        gates["majorants.prism_%d_direct_sums<=transcript_ceilings" % k] = ok
        maj.append({"prism": k, "t_seam": p["ta"], "t_next": p["tb"],
                    "Dz_direct_sum_hi": s(dz, 16), "Dz_transcript": Dz, "Dz_head16_hi": s(dz_head, 12),
                    "Dt_direct_sum_hi": s(dt, 16), "Dt_transcript": Dt, "Dt_head16_hi": s(dt_head, 12),
                    "ratio_Dz_transcript/direct": round(float(Dz) / float(dz), 9),
                    "ratio_Dt_transcript/direct": round(float(Dt) / float(dt), 9)})
    res["majorants"] = maj
    allpass = all(bool(v) for v in gates.values())
    rec = {"title": "Independent standard-library checks of the barrier suppliers",
           "date": "2026-10-13", "model": "Claude Opus 5.5 (claude-opus-5-5)",
           "source_package": PACKAGE, "precision_digits": PREC,
           "gates": {k: bool(v) for k, v in sorted(gates.items())}, "results": res,
           "all_gates_pass": allpass,
           "software": {"python": platform.python_version(), "implementation": platform.python_implementation()}}
    with open(__file__, "rb") as fh:
        rec["checker_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    out = json.dumps(rec, indent=1)
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(out + "\n")
    for k, v in sorted(gates.items()):
        print(("PASS " if v else "FAIL ") + k)
    print("ALL PASS" if allpass else "FAILURE", "(%.1f s)" % (time.time() - t_start), file=sys.stderr)
    return 0 if allpass else 1


if __name__ == "__main__":
    sys.exit(main())
