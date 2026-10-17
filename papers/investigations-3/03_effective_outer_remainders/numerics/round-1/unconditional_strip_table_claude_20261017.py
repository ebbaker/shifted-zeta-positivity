#!/usr/bin/env python3
"""Exact and directed-rounding check of a stepped derivative-kernel table for Theorem 12 of
Hakimoglu-Brown, arXiv:2610.12803v1, started from the unconditional strip M(0) <= 1.

Prepared for Edward Baker with LLM assistance.  Model: Claude Opus 5.5 (configured
identifier claude-opus-5-5), Claude Cowork, reasoning effort max, 17 October 2026.
Standard library only (fractions, decimal); prints one deterministic JSON record.

Companion of papers/investigations-3/03_effective_outer_remainders/notes/round-1/
02_HAKIMOGLU_BROWN_COMPARISON_AND_UNCONDITIONAL_TABLE_CLAUDE_20261017.md.

What is checked, for TABLE_Q0_1 (q0 = 1, p = 61/20) and, as a control, for the paper's
Table 3 (q0 = 9/16):
  1. exact rational: the chain (t_i, d_i, q_i), q_n = b = 1/25, t_n <= 1/5, q_0 < p^2;
  2. exact rational: positivity of the Bernstein coefficients of the compactified
     polynomial (25) of the paper, via its (34)-(35), on eight U-subintervals;
  3. exact rational: k_i > 0 for the paper's (33), and the gate
     E_20(k_i d_i) (2 + k_i q_{i+1}) >= 2 + k_i q_i, E_20 the Taylor sum (<= exp);
  4. exact rational: L/4 > 5.5716 and N >= 69098 for x >= X (the paper's Section 8.2);
  5. directed rounding (decimal, 32 digits; exp and ln, documented as correctly rounded, are
     moved one unit outward; +, -, *, / are rounded toward the bound; integer powers by repeated
     multiplication): C_i <= C^cert and G_i >= G^cert, the paper's expressions
     (28)-(32) with its upper-bound inputs Z_*, psi_*, psi_2,* (Sections 8.1-8.2), on
     [t_i, t_i + 1/200], and eps_0 < 1/2.
If all hold, the paper's Theorem 12, with its Proposition 11, Lemma 10 and Lemma 2, gives
Lambda <= t_n + 1/50 with no zero-free half-plane as input.  The analytic statements are the
paper's (an unrefereed working draft) and are not proved here.
"""
import json
from decimal import Decimal as D, Context, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from fractions import Fraction as Fr
from math import comb

P = Fr(61, 20)
B = P * P
BQ = Fr(1, 25)
X = Fr(120000167903, 2)          # 60000083951.5
DT = Fr(1, 200)

# rows: 10^6 q_i, 10^4 C_i, 10^4 G_i, 10^3 lambda_i, 10^3 mu_i; t_i = i/200; d_i = 1/200 except the last
TABLE_Q0_1 = [
    (1000000, 52902, 2340, 1474, 481), (952036, 52964, 2322, 1524, 540),
    (904955, 53031, 2284, 1574, 609), (858867, 53100, 2234, 1621, 691),
    (813966, 53172, 2174, 1644, 738), (770525, 53245, 2107, 1658, 764),
    (728552, 53318, 2036, 1671, 788), (688021, 53390, 1962, 1684, 815),
    (648917, 53462, 1887, 1698, 841), (611181, 53533, 1813, 1710, 865),
    (574812, 53602, 1739, 1723, 892), (539777, 53670, 1667, 1735, 916),
    (506049, 53736, 1596, 1748, 944), (473600, 53800, 1528, 1759, 967),
    (442411, 53862, 1462, 1771, 995), (412455, 53922, 1399, 1782, 1018),
    (383698, 53980, 1338, 1794, 1046), (356111, 54036, 1280, 1804, 1068),
    (329670, 54090, 1225, 1815, 1096), (304348, 54143, 1172, 1824, 1118),
    (280116, 54193, 1122, 1834, 1139), (256931, 54242, 1074, 1844, 1167),
    (234774, 54288, 1028, 1853, 1188), (213607, 54334, 985, 1861, 1208),
    (193403, 54377, 944, 1869, 1227), (174128, 54419, 905, 1878, 1255),
    (155754, 54459, 867, 1885, 1273), (138247, 54498, 832, 1892, 1291),
    (121575, 54536, 798, 1899, 1308), (105705, 54572, 766, 1905, 1325),
    (90610, 54606, 736, 1912, 1341), (76255, 54640, 707, 1919, 1367),
    (62616, 54672, 679, 1925, 1383), (49660, 54703, 653, 1930, 1397)]
LAST_D_Q0_1 = Fr(391, 100000)

# the paper's Table 3 (q0 = 9/16), used as a control of this programme
TABLE_PAPER = [
    (562500, 52902, 2340, 1718, 868), (528937, 52964, 2322, 1729, 888),
    (496634, 53031, 2284, 1739, 907), (465546, 53100, 2234, 1749, 927),
    (435634, 53172, 2174, 1759, 945), (406850, 53245, 2107, 1769, 964),
    (379163, 53318, 2035, 1778, 982), (352551, 53390, 1962, 1791, 1015),
    (326987, 53462, 1887, 1800, 1034), (302441, 53533, 1813, 1808, 1051),
    (278890, 53602, 1739, 1822, 1088), (256302, 53670, 1667, 1830, 1106),
    (234657, 53736, 1596, 1838, 1123), (213926, 53800, 1528, 1845, 1140),
    (194091, 53862, 1462, 1853, 1156), (175117, 53922, 1399, 1866, 1197),
    (156984, 53980, 1338, 1872, 1213), (139669, 54036, 1280, 1879, 1229),
    (123142, 54090, 1225, 1885, 1244), (107379, 54143, 1172, 1892, 1259),
    (92351, 54193, 1122, 1897, 1273), (78037, 54242, 1074, 1910, 1318),
    (64407, 54288, 1028, 1915, 1332), (51439, 54334, 985, 1920, 1345)]
LAST_D_PAPER = Fr(463, 100000)


def rows_of(table, last_d):
    out = []
    for i, (q, C, G, lam, mu) in enumerate(table):
        d = DT if i < len(table) - 1 else last_d
        qn = Fr(table[i + 1][0], 10 ** 6) if i < len(table) - 1 else BQ
        out.append(dict(i=i, t=Fr(i, 200), d=d, q=Fr(q, 10 ** 6), qn=qn, C=Fr(C, 10 ** 4),
                        G=Fr(G, 10 ** 4), lam=Fr(lam, 1000), mu=Fr(mu, 1000)))
    return out


# --------------------------------------------------------------------------- exact parts
def E_low(x, n=20):
    s = Fr(0)
    term = Fr(1)
    for j in range(n + 1):
        s += term
        term = term * x / (j + 1)
    return s


def E_up(x, n=160):
    assert 0 <= x < n + 2
    s = E_low(x, n)
    tail = Fr(1)
    for j in range(1, n + 2):
        tail = tail * x / j
    return s + tail / (1 - x / (n + 2))


def padd(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, 0) + v
    return {k: v for k, v in c.items() if v != 0}


def pmul(a, b):
    c = {}
    for (i1, j1), v1 in a.items():
        for (i2, j2), v2 in b.items():
            k = (i1 + i2, j1 + j2)
            c[k] = c.get(k, 0) + v1 * v2
    return {k: v for k, v in c.items() if v != 0}


def psc(a, s):
    return {k: v * s for k, v in a.items()}


def phi_poly(A2, lam, mu):
    """The paper's (25) as {(deg D, deg r): coefficient}."""
    Dv = {(1, 0): Fr(1)}
    rv = {(0, 1): Fr(1)}
    one = {(0, 0): Fr(1)}
    w = padd(padd(Dv, psc(one, B)), psc(rv, -1))
    Dl = padd(pmul(w, w), psc(pmul(Dv, rv), 4))
    N = padd(padd(psc(pmul(w, Dl), 2 * lam), psc(pmul(padd(psc(w, 2), psc(one, 4 * B)), Dl), -mu)),
             psc(pmul(w, w), 8 * mu * B))
    fac = padd(padd(Dv, psc(one, A2)), psc(rv, 3))
    return padd(psc(pmul(Dl, Dl), 2), psc(pmul(fac, N), -1))


def lin_pow(c0, c1, n):
    res = [Fr(1)]
    for _ in range(n):
        new = [Fr(0)] * (len(res) + 1)
        for i, v in enumerate(res):
            new[i] += v * c0
            new[i + 1] += v * c1
        res = new
    return res


def bernstein_min(A2, lam, mu, nsub=8):
    Phi = phi_poly(A2, lam, mu)
    assert max(i for i, j in Phi) <= 4 and max(j for i, j in Phi) <= 4
    best = None
    for l in range(nsub):
        coef = [[Fr(0)] * 5 for _ in range(5)]
        for (i, j), ph in Phi.items():
            Ui = lin_pow(Fr(l, nsub), Fr(1, nsub), i)
            Wi = lin_pow(Fr(nsub - l, nsub), Fr(-1, nsub), 4 - i)
            prod = [Fr(0)] * 5
            for a, va in enumerate(Ui):
                for c, vc in enumerate(Wi):
                    prod[a + c] += va * vc
            fac = ph * B ** i * A2 ** j / B ** 4
            for k in range(5):
                coef[k][j] += fac * prod[k]
        for a in range(5):
            for bb in range(5):
                beta = Fr(0)
                for k in range(a + 1):
                    for m in range(bb + 1):
                        beta += coef[k][m] * Fr(comb(a, k), comb(4, k)) * Fr(comb(bb, m), comb(4, m))
                if best is None or beta < best:
                    best = beta
    return best


def kval(r):
    q, C, G, lam, mu = r["q"], r["C"], r["G"], r["lam"], r["mu"]
    return 4 * (lam * C / P - mu * G - 2 * lam / (B - q) - 2 * mu * (B + q) / (B - q) ** 2)


# --------------------------------------------------------------------------- directed rounding
PREC = 32
CU = Context(prec=PREC, rounding=ROUND_CEILING)
CD = Context(prec=PREC, rounding=ROUND_FLOOR)
CN = Context(prec=PREC, rounding=ROUND_HALF_EVEN)
N1 = 65536
NSTAR = 69098
LN = [None, None]
for _n in range(2, NSTAR + 1):
    _v = CN.ln(D(_n))
    LN.append((CN.next_minus(_v), CN.next_plus(_v)))


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
        PP.append((_v, _l, _j))
        _v *= _l
        _j += 1
FACT = [1, 1, 2]


def dec(fr):
    fr = Fr(fr)
    d = CN.divide(D(fr.numerator), D(fr.denominator))
    assert Fr(d) == fr
    return d


def exp_up(x_up):
    return CN.next_plus(CN.exp(x_up))


def ipow(ctx, x, n):
    """x^n for a small integer n >= 0 by repeated multiplication in the directed context ctx
    (Decimal power() is only 'almost always' correctly rounded)."""
    r = D(1)
    for _ in range(n):
        r = ctx.multiply(r, x)
    return r


def T_up(j, v):
    Llo, Lhi = LN[N1]
    vm1 = CD.subtract(v, D(1))
    assert vm1 > 0
    pw = exp_up(CU.multiply(CU.subtract(D(1), v), Llo))
    s = D(0)
    for k in range(j + 1):
        c = D(FACT[j] // FACT[j - k])
        num = CU.multiply(c, ipow(CU, Lhi, j - k))
        s = CU.add(s, CU.divide(num, ipow(CD, vm1, k + 1)))
    return CU.multiply(pw, s)


def prop11_cert(tm, tp):
    """Certified C lower bound and G upper bound of the paper's (31)-(32) on [tm, tp], p = 61/20."""
    sp = (1 + P) / 2
    u = dec(sp + Fr(557, 100) * tm)
    u8 = dec(sp + Fr(278, 100) * tm)
    e = dec((P - 1) / 2 - Fr(278, 100) * tm)
    assert e > 0
    tpd = dec(tp)
    nu = [None, None]
    Z = D(1)
    d0 = d1 = d2 = D(0)
    for n in range(2, N1 + 1):
        Llo, Lhi = LN[n]
        nu_up = exp_up(CU.multiply(-u, Llo))
        nu.append(nu_up)
        Z = CU.add(Z, nu_up)
        h_up = CU.subtract(exp_up(CU.divide(CU.multiply(tpd, CU.multiply(Lhi, Lhi)), D(4))), D(1))
        a0 = CU.multiply(h_up, nu_up)
        a1 = CU.multiply(a0, Lhi)
        d0 = CU.add(d0, a0)
        d1 = CU.add(d1, a1)
        d2 = CU.add(d2, CU.multiply(a1, Lhi))
    Z = CU.add(Z, T_up(0, u))
    psi = psi2 = D(0)
    for (n, l, j) in PP:
        Lh = LN[l][1]
        psi = CU.add(psi, CU.multiply(Lh, nu[n]))
        psi2 = CU.add(psi2, CU.multiply(D(j), CU.multiply(CU.multiply(Lh, Lh), nu[n])))
    psi = CU.add(psi, T_up(1, u))
    psi2 = CU.add(psi2, T_up(2, u))
    d0 = CU.add(d0, T_up(0, u8))
    d1 = CU.add(d1, T_up(1, u8))
    d2 = CU.add(d2, T_up(2, u8))
    pd = dec(P)
    Slo, Shi = LN[NSTAR]
    Nmp = exp_up(CU.multiply(-pd, Slo))
    Ne1 = exp_up(CU.multiply(CU.add(e, D(1)), Shi))
    Ne = exp_up(CU.multiply(e, Shi))
    rho0 = CU.multiply(D("1.01"), CU.multiply(Nmp, CU.add(CU.divide(Ne1, CD.add(e, D(1))), Ne)))
    Ls = CU.add(CU.multiply(D(2), Shi), D(3))
    rho1 = CU.multiply(Ls, rho0)
    rho2 = CU.multiply(CU.add(CU.multiply(Ls, Ls), D("1e-9")), rho0)
    eta0, eta1, eta2 = D("1e-6"), D("4e-5"), D("16e-4")
    c1, c2 = D("0.5000000001"), D("0.2500000001")
    e0 = CU.add(CU.add(d0, rho0), eta0)
    eps0 = CU.multiply(Z, e0)
    e1 = CU.add(CU.add(CU.multiply(c1, d1), rho1), eta1)
    eps1 = CU.multiply(Z, CU.add(e1, CU.multiply(c1, CU.multiply(psi, e0))))
    e2 = CU.add(CU.add(CU.add(CU.multiply(c2, d2), rho2), eta2), D("1e-9"))
    inner = CU.add(CU.add(e2, CU.multiply(D(2), CU.multiply(c1, CU.multiply(psi, e1)))),
                   CU.multiply(c2, CU.multiply(CU.add(psi2, CU.multiply(psi, psi)), e0)))
    eps2 = CU.multiply(Z, inner)
    om = CD.subtract(D(1), eps0)
    r1 = CU.divide(eps1, om)
    C_lo = CD.subtract(CD.subtract(CD.subtract(D("5.5716"), D("1e-6")), CU.multiply(c1, psi)), r1)
    G_up = CU.add(CU.add(CU.add(CU.multiply(c2, psi2), CU.divide(eps2, om)), CU.multiply(r1, r1)), D("2e-10"))
    return Fr(C_lo), Fr(G_up), Fr(eps0)


def fl(x, n=12):
    return float(f"{float(x):.{n}g}")


def check_table(rows, q0, scalars=True):
    out = {"q0": str(q0), "rows": len(rows)}
    ok = rows[0]["q"] == q0 and rows[0]["t"] == 0 and q0 < B
    for a, b in zip(rows, rows[1:]):
        ok = ok and b["t"] == a["t"] + a["d"] and b["q"] < a["q"] and b["q"] == a["qn"]
    tn = rows[-1]["t"] + rows[-1]["d"]
    ok = ok and rows[-1]["qn"] == BQ and tn <= Fr(1, 5) and all(r["qn"] >= BQ for r in rows)
    out["chain_ok"] = ok
    bern = []
    gates = []
    ks = []
    for r in rows:
        bern.append(bernstein_min(r["q"], r["lam"], r["mu"]))
        k = kval(r)
        ks.append(k)
        gates.append(E_low(k * r["d"]) * (2 + k * r["qn"]) - (2 + k * r["q"]))
    out["min_bernstein"] = fl(min(bern))
    out["all_bernstein_positive"] = all(x > 0 for x in bern)
    out["k_range"] = [fl(min(ks), 6), fl(max(ks), 6)]
    out["all_k_positive"] = all(k > 0 for k in ks)
    out["min_gate"] = fl(min(gates))
    out["all_gates_hold"] = all(g >= 0 for g in gates)
    if scalars:
        cm = gm = None
        e0max = Fr(0)
        for r in rows:
            Cc, Gc, e0 = prop11_cert(r["t"], r["t"] + DT)
            cm = Cc - r["C"] if cm is None else min(cm, Cc - r["C"])
            gm = Gc - r["G"] if gm is None else max(gm, Gc - r["G"])
            e0max = max(e0max, e0)
        out["min_C_cert_minus_C"] = fl(cm)
        out["max_G_cert_minus_G"] = fl(gm)
        out["max_eps0_cert"] = fl(e0max)
        out["scalars_ok"] = cm >= 0 and gm <= 0 and e0max < Fr(1, 2)
    out["t_n"] = str(tn)
    out["Lambda_bound"] = str(tn + BQ / 2)
    out["Lambda_bound_decimal"] = fl(tn + BQ / 2)
    out["all_checks_pass"] = all(out[k] for k in ("chain_ok", "all_bernstein_positive", "all_k_positive",
                                                   "all_gates_hold")) and out.get("scalars_ok", True)
    return out


def main():
    rec = {"programme": "unconditional_strip_table_claude_20261017.py",
           "model": "Claude Opus 5.5 (claude-opus-5-5), Claude Cowork, effort max",
           "date": "2026-10-17",
           "source": "Hakimoglu-Brown, arXiv:2610.12803v1 (working draft 7 October 2026): Lemma 2, "
                     "Lemma 10, Proposition 11, Theorem 12, Sections 8.1-8.2",
           "p": "61/20", "b": "1/25", "X": "60000083951.5"}
    # Section 8.2 of the paper: L/4 > 5.5716 and N >= 69098 for x >= X (pi < 355/113)
    rec["L_over_4_gt_5.5716"] = E_up(Fr(13929, 625)) < 113 * X / 1420
    rec["N_ge_69098"] = Fr(69098) ** 2 < 113 * X / 1420
    rec["q0_1_unconditional_strip"] = check_table(rows_of(TABLE_Q0_1, LAST_D_Q0_1), Fr(1))
    rec["control_paper_table3_q0_9_16"] = check_table(rows_of(TABLE_PAPER, LAST_D_PAPER), Fr(9, 16))
    rec["note"] = ("Exact rational checks of the chain, the Bernstein coefficients and the gates; "
                   "directed-rounding decimal evaluation of the paper's scalar expressions. The table "
                   "starts from the unconditional strip M(0) <= 1 (every zero of xi has 0 < Re s < 1) and "
                   "uses no zero-free half-plane. Its conclusion Lambda <= t_n + 1/50 is conditional on "
                   "the paper's analytic statements: Theorem 12 and Lemma 10; Proposition 11 with Lemma 3, "
                   "Lemma 6, the normalizer bounds of Section 3 and estimate (27); Lemma 2, which uses "
                   "Polymath's published boundary computation (Section 8.4(a), not replayed), the RH "
                   "verification, Polymath's Proposition 3.1(ii) and de Bruijn's theorem. None of these is "
                   "proved here.")
    print(json.dumps(rec, indent=1, sort_keys=False))


if __name__ == "__main__":
    main()
