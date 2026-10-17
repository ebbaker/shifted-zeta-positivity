#!/usr/bin/env python3
"""Comparison of note 01's height-p transport floor with Hakimoglu-Brown's strip comparison
(arXiv:2610.12803v1), and planning runs of his Theorems 9 and 12 (Project 03, note 02).

Prepared for Edward Baker with LLM assistance.  Model: Claude Opus 5.5 (configured
identifier claude-opus-5-5), Claude Cowork, reasoning effort max, 17 October 2026.
Standard library only; imports the note 01 programme from this folder; prints one
deterministic JSON record (floats rounded to 12 significant figures).

Sections
  A  reproduction of the paper's printed certificates (one-step value (18); Table 2 by
     Theorem 9; the inputs of Tables 6-7 recomputed from Sections 8.1-8.2)
  B  floors and derivative bounds at p = 61/20 and 301/100: the paper's Propositions 8 and 11
     against note 01's Theorem 4.6 with a Cauchy-estimate derivative bound
  C  Theorem 12 from the unconditional strip q0 = 1 with the paper's Proposition 11: the
     construction of the table checked in unconditional_strip_table_claude_20261017.py, with
     exact Bernstein and gate checks; sensitivity to the step and the polynomial margin
  D  planning: Theorems 9 and 12 for zeta with note 01's floors at heights 2 <= p <= 3.5
  E  planning: Project 01's Target A with Theorem 12's kernel (note 01's floors), b -> 0
Sections B, D and E are floating evaluations (planning or numerical); C's scalars are floating
here and certified in the companion programme.
"""
import json
import math
import os
import sys
from fractions import Fraction as Fr
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import height_p_transport_claude_20261017 as hpt  # noqa: E402

PI = math.pi
sig = hpt.sig
XHB = 60000083951.5            # the paper's X = 6e10 + 83952 - 1/2
TZ = XHB / 2 - 1
ELLX = math.log(TZ / (2 * PI)) - 1e-6
BQ = 1 / 25

# --------------------------------------------------------------------------- the paper's inputs
N1 = 65536
LOGN = [0.0, 0.0] + [math.log(n) for n in range(2, N1 + 1)]


def _sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


PP = []
for _l in _sieve(N1):
    _v, _j = _l, 1
    while _v <= N1:
        PP.append((_v, math.log(_l), _j))
        _v *= _l
        _j += 1


def Tj(j, v):
    L = math.log(N1)
    s = 0.0
    for k in range(j + 1):
        s += math.factorial(j) / math.factorial(j - k) * L ** (j - k) / (v - 1) ** (k + 1)
    return N1 ** (1 - v) * s


def zeta_star(u):
    return 1 + sum(math.exp(-u * LOGN[n]) for n in range(2, N1 + 1)) + Tj(0, u)


def psi_star(u):
    return sum(ll * math.exp(-u * LOGN[n]) for (n, ll, j) in PP) + Tj(1, u)


def psi2_star(u):
    return sum(j * ll * ll * math.exp(-u * LOGN[n]) for (n, ll, j) in PP) + Tj(2, u)


def heat_sums(u, u8, tp, K0=N1, js=(0, 1, 2), integral=True):
    d = [0.0, 0.0, 0.0]
    for n in range(2, K0 + 1):
        ln = LOGN[n]
        w = (math.exp(tp * ln * ln / 4) - 1) * math.exp(-u * ln)
        d[0] += w
        d[1] += w * ln
        d[2] += w * ln * ln
    if integral:
        for j in js:
            d[j] += Tj(j, u8)
    return d


def prop11(tm, tp, p=61 / 20):
    """The paper's (28)-(32) with its upper-bound inputs Z_*, psi_*, psi_2,*; floating point."""
    sp = (1 + p) / 2
    u = sp + 5.57 * tm
    u8 = sp + 2.78 * tm
    Z, psi, psi2 = zeta_star(u), psi_star(u), psi2_star(u)
    d0, d1, d2 = heat_sums(u, u8, tp)
    Ns = 69098
    e = (p - 1) / 2 - 2.78 * tm
    rho0 = 1.01 * Ns ** (-p) * (Ns ** (e + 1) / (e + 1) + Ns ** e)
    Ls = 2 * math.log(Ns) + 3
    rho1, rho2 = Ls * rho0, (Ls * Ls + 1e-9) * rho0
    c1, c2 = 0.5 + 1e-10, 0.25 + 1e-10
    e0 = d0 + rho0 + 1e-6
    eps0 = Z * e0
    e1 = c1 * d1 + rho1 + 4e-5
    eps1 = Z * (e1 + c1 * psi * e0)
    e2 = c2 * d2 + rho2 + 16e-4 + 1e-9
    eps2 = Z * (e2 + 2 * c1 * psi * e1 + c2 * (psi2 + psi * psi) * e0)
    C = 5.5716 - 1e-6 - c1 * psi - eps1 / (1 - eps0)
    G = c2 * psi2 + eps2 / (1 - eps0) + (eps1 / (1 - eps0)) ** 2 + 2e-10
    return dict(C=C, G=G, Z=Z, psi=psi, psi2=psi2, d0=d0, d1=d1, d2=d2, rho0=rho0, rho1=rho1,
                rho2=rho2, eps0=eps0)


def prop8(tm, tp, p=301 / 100):
    """The paper's (23) (Euler-product estimate, Table 2), certified-form inputs; floating."""
    sp = (1 + p) / 2
    u = sp + 5.57 * tm
    Z = 1 + sum(math.exp(-u * LOGN[n]) for n in range(2, N1 + 1)) + N1 ** (1 - u) / (u - 1)
    psi = sum(ll * math.exp(-u * LOGN[n]) for (n, ll, j) in PP) + Tj(1, u)
    d = heat_sums(u, u, tp, integral=False)
    U0, U1 = d[0] + 4e-5, d[1] + 5e-4
    nu, eps0, eps1 = 0.5 + 1e-10, 2e-5, 6.6e-4
    C = 5.57 - 1e-6 - (nu * (psi + U1 * Z) + eps1 * Z) / (1 - (U0 + eps0) * Z)
    return dict(C=C, Z=Z, psi=psi, U0=U0, U1=U1)


# --------------------------------------------------------------------------- Lemma 10 / Theorems 9, 12
def make_samples(Bf, A2, nU=400, nr=40):
    pts = []
    Us = [k / nU for k in range(nU)] + [0.999, 0.9995, 0.9999, 0.99999]
    for U in Us:
        D = Bf * U / (1 - U)
        for m in range(nr + 1):
            r = A2 * m / nr
            w = D + Bf - r
            Dl = w * w + 4 * D * r
            Fac = D + A2 + 3 * r
            P1 = Fac * 2 * w * Dl
            pts.append((2 * Dl * Dl / P1, Fac * ((2 * w + 4 * Bf) * Dl - 8 * Bf * w * w) / P1))
    return pts


def best_k(C, G, p, A2, pts, margin=0.005, mu_hi=4.0):
    """max over mu of k in (33), lambda = sampled largest admissible value minus margin."""
    Bf = p * p

    def kv(mu):
        lam = min(a + mu * b for a, b in pts) - margin
        return 4 * (lam * C / p - mu * G - 2 * lam / (Bf - A2) - 2 * mu * (Bf + A2) / (Bf - A2) ** 2), lam

    lo, hi = 0.0, mu_hi
    g = (math.sqrt(5) - 1) / 2
    x1, x2 = hi - g * (hi - lo), lo + g * (hi - lo)
    f1, f2 = kv(x1)[0], kv(x2)[0]
    for _ in range(60):
        if f1 < f2:
            lo, x1, f1 = x1, x2, f2
            x2 = lo + g * (hi - lo)
            f2 = kv(x2)[0]
        else:
            hi, x2, f2 = x2, x1, f1
            x1 = hi - g * (hi - lo)
            f1 = kv(x1)[0]
    mu = (lo + hi) / 2
    k, lam = kv(mu)
    return k, lam, mu


def run_comparison(CG, p, q0, kernel, dt=1 / 200, tmax=0.2, b=BQ, margin=0.005, nU=200, nr=20):
    """Stepped Theorem 9 (kernel 9) or Theorem 12 (kernel 12); returns (t_n, steps) or (None, steps)."""
    Bf = p * p
    if kernel == 9 and Bf < 5 * q0 - 1e-12:
        return None, 0
    q, t, n = q0, 0.0, 0
    while True:
        tp = min(t + dt, tmax)
        C, G = CG(p, t, tp)
        if kernel == 12:
            k = best_k(C, G, p, q, make_samples(Bf, q, nU, nr), margin)[0]
        else:
            k = 4 * C / p - 8 / (Bf - q)
        if k <= 0:
            return None, n
        tf = math.log((2 + k * q) / (2 + k * b)) / k
        n += 1
        if tf <= tp - t:
            return t + tf, n
        q = ((2 + k * q) * math.exp(-k * (tp - t)) - 2) / k
        t = tp
        if t >= tmax - 1e-12:
            return None, n


def E_low(x, n=20):
    s, term = Fr(0), Fr(1)
    for j in range(n + 1):
        s += term
        term = term * x / (j + 1)
    return s


# exact Bernstein coefficients of the paper's (34)-(35)
def _padd(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, 0) + v
    return {k: v for k, v in c.items() if v != 0}


def _pmul(a, b):
    c = {}
    for (i1, j1), v1 in a.items():
        for (i2, j2), v2 in b.items():
            k = (i1 + i2, j1 + j2)
            c[k] = c.get(k, 0) + v1 * v2
    return {k: v for k, v in c.items() if v != 0}


def _psc(a, s):
    return {k: v * s for k, v in a.items()}


def _lin_pow(c0, c1, n):
    res = [Fr(1)]
    for _ in range(n):
        new = [Fr(0)] * (len(res) + 1)
        for i, v in enumerate(res):
            new[i] += v * c0
            new[i + 1] += v * c1
        res = new
    return res


def bernstein_min(B, A2, lam, mu, nsub=8):
    Dv, rv, one = {(1, 0): Fr(1)}, {(0, 1): Fr(1)}, {(0, 0): Fr(1)}
    w = _padd(_padd(Dv, _psc(one, B)), _psc(rv, -1))
    Dl = _padd(_pmul(w, w), _psc(_pmul(Dv, rv), 4))
    N = _padd(_padd(_psc(_pmul(w, Dl), 2 * lam), _psc(_pmul(_padd(_psc(w, 2), _psc(one, 4 * B)), Dl), -mu)),
              _psc(_pmul(w, w), 8 * mu * B))
    Phi = _padd(_psc(_pmul(Dl, Dl), 2), _psc(_pmul(_padd(_padd(Dv, _psc(one, A2)), _psc(rv, 3)), N), -1))
    best = None
    for l in range(nsub):
        coef = [[Fr(0)] * 5 for _ in range(5)]
        for (i, j), ph in Phi.items():
            Ui = _lin_pow(Fr(l, nsub), Fr(1, nsub), i)
            Wi = _lin_pow(Fr(nsub - l, nsub), Fr(-1, nsub), 4 - i)
            prod = [Fr(0)] * 5
            for a, va in enumerate(Ui):
                for c, vc in enumerate(Wi):
                    prod[a + c] += va * vc
            fac = ph * B ** i * A2 ** j / B ** 4
            for k in range(5):
                coef[k][j] += fac * prod[k]
        for a in range(5):
            for bb in range(5):
                beta = sum(coef[k][m] * Fr(comb(a, k), comb(4, k)) * Fr(comb(bb, m), comb(4, m))
                           for k in range(a + 1) for m in range(bb + 1))
                if best is None or beta < best:
                    best = beta
    return best


# --------------------------------------------------------------------------- note 01's floors
_EC = {}


def E_zeta(tau, p):
    key = (round(tau, 12), round(p, 12))
    if key not in _EC:
        _EC[key] = hpt.E_best(ELLX, tau, p, "zeta", T=TZ)[0]
    return _EC[key]


RS = (0.05, 0.1, 0.15, 0.25, 0.35)


def ours_zeta(p, tm, tp, rs=RS, pmin=1.3):
    """note 01's interval floor C and Cauchy-estimate derivative bound G for zeta at x >= X."""
    s0 = (1 + p) / 2
    tm2, tp2 = tm / 2, tp / 2
    ss = s0 + tm2 * ELLX / 2
    C = ELLX / 4 - 0.5 * hpt.kappa_r(ss) - E_zeta(math.sqrt(tp2), p) / 2
    main = 0.25 * (hpt.K2_r(ss) + 2 / TZ) / (1 - 2 * tp2 / TZ)
    G, rb = math.inf, None
    for r in rs:
        if p - 2 * r >= pmin:
            g = main + E_zeta(math.sqrt(tp2), p - 2 * r) / (4 * r)
            if g < G:
                G, rb = g, r
    return C, G, rb


def ours_family(q, a, p, tm, tp, rs=(0.05, 0.1, 0.15, 0.25), pmin=1.3):
    s0 = (1 + p) / 2
    taum, taup = math.sqrt(tm / 2), math.sqrt(tp / 2)
    l0, _ = hpt.ell_star0(q, a, p, tm)
    ss = s0 + taum * taum * l0 / 2
    C = l0 / 4 - 0.5 * hpt.kappa_r(ss) - hpt.E_best(l0, taup, p, "family", a)[0] / 2
    A1 = 0.25 * hpt.psi1_r((ss + a) / 2)
    main = 0.25 * (hpt.K2_r(ss) + A1) / (1 - taup * taup * A1)
    G = math.inf
    for r in rs:
        if p - 2 * r >= pmin:
            l0r, _ = hpt.ell_star0(q, a, p - 2 * r, tm)
            G = min(G, main + hpt.E_best(l0r, taup, p - 2 * r, "family", a)[0] / (4 * r))
    return C, G


# --------------------------------------------------------------------------- sections
TABLE2 = [(0, 562500, 52708), (1, 510004, 52851), (2, 460480, 53006), (3, 413770, 53166),
          (4, 369731, 53323), (5, 328228, 53475), (6, 289133, 53619), (7, 252324, 53754),
          (8, 217683, 53881), (9, 185096, 53999), (10, 154454, 54108), (11, 125652, 54209),
          (12, 98588, 54303), (13, 73166, 54390), (14, 49294, 54470)]
TABLE3_CG = [(52902, 2340), (52964, 2322), (53031, 2284), (53100, 2234), (53172, 2174),
             (53245, 2107), (53318, 2035), (53390, 1962), (53462, 1887), (53533, 1813),
             (53602, 1739), (53670, 1667), (53736, 1596), (53800, 1528), (53862, 1462),
             (53922, 1399), (53980, 1338), (54036, 1280), (54090, 1225), (54143, 1172),
             (54193, 1122), (54242, 1074), (54288, 1028), (54334, 985)]
TABLE6 = {0: (1622101766394, 548568036655, 839050132415), 12: (1402401939248, 344191284922, 441889941403),
          23: (1284531007297, 237543192549, 272365265934)}
TABLE7 = {0: (2333875727, 6985223600, 28309848180, 5463325, 138148683, 3493305246),
          12: (13521108993, 31439981634, 97404000815, 928038, 23466885, 593396825),
          23: (13576392076, 26288961540, 67521313978, 184036, 4653631, 117674307)}


def section_A():
    out = {}
    k = Fr(21, 4) - Fr(8) / (16 - Fr(9, 16))
    out["one_step_(18)"] = {"k": str(k), "value": sig(1 / 50 + math.log(73691 / 34608) / float(k)),
                            "paper": 0.1797275414}
    # Table 2 by Theorem 9 at p = 301/100
    p = Fr(301, 100)
    gates = []
    for i, (ii, q, C) in enumerate(TABLE2):
        q, C = Fr(q, 10 ** 6), Fr(C, 10 ** 4)
        qn = Fr(TABLE2[i + 1][1], 10 ** 6) if i < 14 else Fr(1, 25)
        d = Fr(1, 100) if i < 14 else Fr(51, 12500)
        kk = 4 * C / p - 8 / (p * p - q)
        gates.append(E_low(kk * d) * (2 + kk * qn) - (2 + kk * q))
    out["table2_theorem9"] = {"min_gate": sig(float(min(gates))), "all_gates_hold": all(g >= 0 for g in gates),
                              "final_time": "1801/12500", "Lambda": sig(1801 / 12500 + 1 / 50),
                              "paper_min_gate": 1.25e-7}
    # Proposition 8 at the Table 2 steps: floating C against the printed C_i
    c8 = []
    for (ii, q, C) in TABLE2:
        tm = ii / 100
        tp = tm + (0.01 if ii < 14 else 51 / 12500)
        c8.append(prop8(tm, tp)["C"] - C / 1e4)
    out["prop8_C_minus_table2_C"] = [sig(min(c8)), sig(max(c8))]
    # Tables 6-7 recomputed
    dev = {}
    for i in TABLE6:
        tm = i / 200
        tp = tm + (1 / 200 if i < 23 else 463 / 100000)
        r = prop11(tm, tp)
        mine = (r["Z"], r["psi"], r["psi2"], r["d0"], r["d1"], r["d2"], r["rho0"], r["rho1"], r["rho2"])
        theirs = TABLE6[i] + TABLE7[i]
        diffs = [t - a * 1e12 for a, t in zip(mine, theirs)]
        dev[str(i)] = [sig(min(diffs), 4), sig(max(diffs), 4)]
    out["tables6_7_(printed-recomputed)_in_1e-12_rows_0_12_23"] = dev
    cm, gm = math.inf, -math.inf
    for i, (C, G) in enumerate(TABLE3_CG):
        tm = i / 200
        tp = tm + (1 / 200 if i < 23 else 463 / 100000)
        r = prop11(tm, tp)
        cm = min(cm, r["C"] - C / 1e4)
        gm = max(gm, r["G"] - G / 1e4)
    out["table3_min(Cfloat-C_i)"] = sig(cm)
    out["table3_max(Gfloat-G_i)"] = sig(gm)
    return out


def section_B():
    rows = []
    for i in (0, 5, 10, 15, 20, 25, 30, 35, 39):
        tm, tp = i / 200, (i + 1) / 200
        h = prop11(tm, tp)
        C, G, r = ours_zeta(61 / 20, tm, tp)
        s0 = (1 + 61 / 20) / 2
        main = ELLX / 4 - 0.5 * hpt.kappa_r(s0 + tm * ELLX / 4)
        rows.append({"t_interval": [tm, tp], "main_term": sig(main, 8),
                     "paper_C": sig(h["C"], 8), "note01_C": sig(C, 8),
                     "paper_G": sig(h["G"], 6), "note01_G": sig(G, 6), "cauchy_radius": r,
                     "main_G": sig(0.25 * hpt.K2_r(s0 + tm * ELLX / 4), 6)})
    rows8 = []
    for (ii, q, Ct) in TABLE2[::2]:
        tm = ii / 100
        tp = tm + 0.01
        C, G, r = ours_zeta(301 / 100, tm, tp)
        rows8.append({"t_interval": [tm, tp], "paper_table2_C": Ct / 1e4, "note01_C": sig(C, 8)})
    return {"p_61_20": rows, "p_301_100": rows8,
            "note": "paper: floating evaluation of its (23) and (31)-(32) with its certified-form inputs; "
                    "note 01: Theorem 4.6 with the gain at t- and E at t+, and G from the Cauchy estimate "
                    "of Section 3 of note 02 (E at p-2r); floating, monotonicity of E in p sampled"}


def build_table(q0, dt=Fr(1, 200), tmax=Fr(1, 5), margin=0.005):
    p = Fr(61, 20)
    B = p * p
    b = Fr(1, 25)
    q, t, rows = Fr(q0), Fr(0), []
    while True:
        tp = min(t + dt, tmax)
        r = prop11(float(t), float(tp))
        C = Fr(math.floor((r["C"] - 2e-6) * 1e4), 10 ** 4)
        G = Fr(math.ceil((r["G"] + 2e-6) * 1e4), 10 ** 4)
        k, lam, mu = best_k(float(C), float(G), float(p), float(q), make_samples(float(B), float(q)), margin)
        lamF, muF = Fr(math.floor(lam * 1000), 1000), Fr(round(mu * 1000), 1000)
        bm = bernstein_min(B, q, lamF, muF)
        while bm <= 0:
            lamF -= Fr(1, 1000)
            bm = bernstein_min(B, q, lamF, muF)
        kk = 4 * (lamF * C / p - muF * G - 2 * lamF / (B - q) - 2 * muF * (B + q) / (B - q) ** 2)
        kf = float(kk)
        tf = math.log((2 + kf * float(q)) / (2 + kf * float(b))) / kf
        final = tf <= float(tp - t)
        if final:
            d, qn = Fr(math.ceil(tf * 1e5), 10 ** 5), b
        else:
            d = tp - t
            qn = Fr(math.ceil((((2 + kf * float(q)) * math.exp(-kf * float(d)) - 2) / kf) * 1e6) + 1, 10 ** 6)
        gate = E_low(kk * d) * (2 + kk * qn) - (2 + kk * q)
        rows.append({"t": str(t), "d": str(d), "1e6q": int(q * 10 ** 6), "1e4C": int(C * 10 ** 4),
                     "1e4G": int(G * 10 ** 4), "1e3lam": int(lamF * 1000), "1e3mu": int(muF * 1000),
                     "k": sig(kf, 8), "bernstein_min": sig(float(bm), 6), "gate": sig(float(gate), 6),
                     "C_float": sig(r["C"], 10), "G_float": sig(r["G"], 10)})
        if gate < 0:
            return None, rows
        if final:
            return t + d, rows
        q, t = qn, tp
        if t >= tmax:
            return None, rows


def section_C():
    tn, rows = build_table(Fr(1))
    tn916, rows916 = build_table(Fr(9, 16))
    sens = {}
    zcg = lambda p, tm, tp: (lambda r: (r["C"], r["G"]))(prop11(tm, tp))  # noqa: E731
    for label, dt, m in (("dt=1/100", 1 / 100, 0.005), ("dt=1/400", 1 / 400, 0.005), ("margin=0.02", 1 / 200, 0.02)):
        t1, n1 = run_comparison(zcg, 61 / 20, 1.0, 12, dt=dt, margin=m)
        sens[label] = None if t1 is None else sig(t1 + BQ / 2, 6)
    t9, n9 = run_comparison(zcg, 61 / 20, 1.0, 9)
    return {"q0_1_table": rows, "q0_1_final_time": str(tn), "q0_1_Lambda": str(tn + Fr(1, 50)),
            "q0_9_16_rebuilt_final_time": str(tn916), "q0_9_16_rebuilt_Lambda": str(tn916 + Fr(1, 50)),
            "paper_q0_9_16_Lambda": "13963/100000",
            "sensitivity_Lambda_q0_1_float": sens,
            "theorem9_q0_1_reaches_b_by_t_1_5": t9 is not None,
            "note": "C_i, G_i are the floating values of the paper's (31)-(32) rounded down and up to 1e-4 "
                    "with margin >= 2e-6; lambda_i, mu_i from the sampled optimum minus 0.005, rounded to "
                    "1e-3 and lowered until the exact Bernstein test passes; q_{i+1} the barrier value "
                    "rounded up to 1e-6 plus 1e-6; gates exact. The scalars are certified in "
                    "unconditional_strip_table_claude_20261017.py."}


def section_D():
    rows = []
    for p in (2.0, 2.25, 2.5, 2.75, 3.05, 3.5):
        for q0 in (1.0, 9 / 16):
            CG = lambda pp, tm, tp: ours_zeta(pp, tm, tp)[:2]  # noqa: E731
            t12, _ = run_comparison(CG, p, q0, 12)
            t9, _ = run_comparison(CG, p, q0, 9)
            rows.append({"p": p, "q0": sig(q0, 6),
                         "theorem12_Lambda": None if t12 is None else sig(t12 + BQ / 2, 6),
                         "theorem9_Lambda": None if t9 is None else sig(t9 + BQ / 2, 6)})
    return {"rows": rows, "note": "planning: note 01's floors (floating, monotonicity sampled) with the "
            "paper's Lemma 2 window t <= 1/5 at the paper's X; None = b not reached by t = 1/5 (or p^2 < 5 q0 "
            "for Theorem 9)"}


def section_E():
    rows = []
    for q in (10 ** 6, 10 ** 8, 10 ** 12):
        for a in (0, 1):
            res12, res9 = {}, {}
            for p in (2.5, 3.0, 3.5, 4.0):
                CG = lambda pp, tm, tp, q=q, a=a: ours_family(q, a, pp, tm, tp)  # noqa: E731
                t12, _ = run_comparison(CG, p, 1.0, 12, tmax=0.5, b=0.0)
                res12[p] = None if t12 is None else sig(t12, 6)
            for p in (2.25, 2.5):
                CG = lambda pp, tm, tp, q=q, a=a: ours_family(q, a, pp, tm, tp)  # noqa: E731
                t9, _ = run_comparison(CG, p, 1.0, 9, tmax=0.5, b=0.0)
                res9[p] = None if t9 is None else sig(t9, 6)
            b12 = min((v, p) for p, v in res12.items() if v is not None)
            b9 = min((v, p) for p, v in res9.items() if v is not None)
            rows.append({"q": q, "parity": a, "theorem12_by_p": {str(k): v for k, v in res12.items()},
                         "theorem9_by_p": {str(k): v for k, v in res9.items()},
                         "theorem12_best": b12[0], "theorem12_best_p": b12[1],
                         "theorem9_best": b9[0], "theorem9_best_p": b9[1],
                         "change": sig(b12[0] / b9[0] - 1, 4)})
    return {"rows": rows, "note": "planning: Project 01's Target A (every primitive character of conductor q, "
            "q0 = 1, b -> 0), conditional on H12, a written comparison theorem and the certification of "
            "note 01's evaluation; the value is the time at which the barrier reaches 0"}


def main():
    rec = {"programme": "hakimoglu_brown_comparison_claude_20261017.py",
           "model": "Claude Opus 5.5 (claude-opus-5-5), Claude Cowork, effort max",
           "date": "2026-10-17", "X": XHB, "ell_X": sig(ELLX)}
    rec["A_reproduction"] = section_A()
    rec["B_floors"] = section_B()
    rec["C_unconditional_table"] = section_C()
    rec["D_zeta_planning_note01_floors"] = section_D()
    rec["E_family_planning"] = section_E()
    print(json.dumps(rec, indent=1, sort_keys=False))


if __name__ == "__main__":
    main()
