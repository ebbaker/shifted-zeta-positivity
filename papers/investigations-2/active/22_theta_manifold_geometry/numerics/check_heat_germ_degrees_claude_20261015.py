#!/usr/bin/env python3
"""Exact checks for the second-round reply on the joint review of
Investigations 21 and 22 (reviews/18_..._CLAUDE_20261015.md).

Prepared for Edward Baker with LLM assistance.  Model: Claude Fable 5.1
(configured identifier ``claude-fable-5-1``), Claude Cowork, 15 October 2026.
Standard library only; every assertion in parts A, B, D and E is exact
rational arithmetic.  Part C is a labelled floating-point spot check of a
closed-form identity.

What is checked
---------------
A. Hermite heat germs.  For m = 2..9 the germ
       H_m(s,z) = sum_k (-1)^k m!/(k!(m-2k)!) s^k z^(m-2k)
   (the heat Taylor germ of an m-fold spatial zero at time T, with
   s = tau - T, so that H_s = -H_zz as for the manuscripts' fields)
   satisfies the backward heat equation exactly,
   H_z = m H_(m-1), and (H_m, d_z H_m) has the origin as its only common
   zero in C^2.  The local degree of the holomorphic map
   G_m = (H_m, d_z H_m): C^2 -> C^2 at the origin is computed as the degree
   in s of the exact Sylvester resultant Res_z(H_m - e1, d_z H_m - e2) for
   a fixed rational (e1, e2); by weighted homogeneity (weights 2 for s,
   1 for z) every solution of G_m = e lies at finite distance, so this is
   the number of preimages of a regular value, i.e. the four-dimensional
   local degree.  Expected: mu_m = m(m-1)/2.
B. Real spacetime index.  For e = (e1, 0) every real preimage has complex
   Jacobian H_zz^2 > 0 (Note 4 of Investigation 21, eq. (15): the real
   Jacobian of the quaternion lift is -|L_1|^2), so the real index of
   (H, H_x) is minus the number of real preimages.  Those are counted
   exactly through the Hermite roots: real solutions with s > 0 are the
   roots lambda of He_(m-1) with sign He_m(lambda) = sign e1, and for even
   m the line z = 0, s < 0 contributes one more when e1 > 0.  Expected
   index: -floor(m/2) for both signs of e1 (Note 01/04 of Investigation 22).
   Also checked: mu_m - floor(m/2) is even and vanishes only for m = 2.
C. The deformed commutation M_t D_d = exp(-2 t a u - t a^2) D_d M_t and
   its transform form H_{D_d Phi}(t,x) = d^(-1/2) e^(t a^2 - i a x)
   H_Phi(t, x + 2 i t a), a = (log d)/2, on a Gaussian source where both
   sides are closed forms (floating point, labelled).
D. The two polynomial controls of Response 17: H = x^2 + 2(T - t) has
   L_0(t,0) = -4(T-t) < 0 before its collision; H = z^2 - 2 tau + 1 has
   the single common zero (1/2, 0) of (H, H_z) and E(t,0) = (1-2t)^2.
E. The endpoint logic of the criterion table: on x^2 + 2(T - t) the strict
   stationary sign L_0 > 0 holds for t > T, fails at t = T (L_0 = 0 at the
   collision), and the weak form L_0 >= 0 holds for t >= T.
"""

import argparse
import cmath
import hashlib
import json
import math
import sys
from fractions import Fraction as Fr

ASSERTIONS = []


def check(name, ok, detail=None):
    ASSERTIONS.append({"name": name, "ok": bool(ok), "detail": detail})
    if not ok:
        print("FAILED:", name, detail, file=sys.stderr)


# ---------------------------------------------------------------------------
# Univariate polynomials over Q: lists of Fractions, index = power.
# ---------------------------------------------------------------------------

def ptrim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def pdeg(p):
    p = ptrim(p)
    return len(p) - 1 if p else -1


def padd(p, q):
    n = max(len(p), len(q))
    return ptrim([(p[i] if i < len(p) else Fr(0)) + (q[i] if i < len(q) else Fr(0)) for i in range(n)])


def pneg(p):
    return [-c for c in p]


def psub(p, q):
    return padd(p, pneg(q))


def pmul(p, q):
    p, q = ptrim(p), ptrim(q)
    if not p or not q:
        return []
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q):
            r[i + j] += a * b
    return ptrim(r)


def pscale(p, c):
    return ptrim([c * x for x in p])


def pdivmod(p, q):
    p, q = ptrim(p), ptrim(q)
    if not q:
        raise ZeroDivisionError
    quo = [Fr(0)] * max(len(p) - len(q) + 1, 1)
    rem = list(p)
    while rem and len(rem) >= len(q):
        c = rem[-1] / q[-1]
        k = len(rem) - len(q)
        quo[k] = c
        for i, b in enumerate(q):
            rem[i + k] -= c * b
        rem = ptrim(rem)
    return ptrim(quo), rem


def pdiv_exact(p, q):
    quo, rem = pdivmod(p, q)
    if rem:
        raise ArithmeticError("inexact polynomial division")
    return quo


def pgcd(p, q):
    p, q = ptrim(p), ptrim(q)
    while q:
        p, q = q, pdivmod(p, q)[1]
    if p:
        p = pscale(p, 1 / p[-1])
    return p


def pderiv(p):
    return ptrim([i * p[i] for i in range(1, len(p))])


def peval(p, x):
    r = Fr(0)
    for c in reversed(ptrim(p)):
        r = r * x + c
    return r


def pconst(c):
    return ptrim([Fr(c)])


# ---------------------------------------------------------------------------
# Determinant of a matrix with entries in Q[s]: fraction-free Bareiss.
# ---------------------------------------------------------------------------

def poly_det(M):
    n = len(M)
    M = [[ptrim(list(e)) for e in row] for row in M]
    sign = 1
    prev = pconst(1)
    for k in range(n - 1):
        if not M[k][k]:
            piv = None
            for i in range(k + 1, n):
                if M[i][k]:
                    piv = i
                    break
            if piv is None:
                return []
            M[k], M[piv] = M[piv], M[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = psub(pmul(M[i][j], M[k][k]), pmul(M[i][k], M[k][j]))
                M[i][j] = pdiv_exact(num, prev) if num else []
        prev = M[k][k]
    d = M[n - 1][n - 1]
    return pscale(d, sign) if d else []


# ---------------------------------------------------------------------------
# Bivariate polynomials in (s, z): dict {(k, l): Fraction} for s^k z^l.
# ---------------------------------------------------------------------------

def hermite_germ(m):
    """H_m(s,z) = sum_k (-1)^k m!/(k!(m-2k)!) s^k z^(m-2k), H_s = -H_zz."""
    H = {}
    for k in range(m // 2 + 1):
        H[(k, m - 2 * k)] = Fr((-1) ** k * math.factorial(m), math.factorial(k) * math.factorial(m - 2 * k))
    return H


def bderiv(H, var):
    out = {}
    for (k, l), c in H.items():
        if var == "s" and k > 0:
            out[(k - 1, l)] = out.get((k - 1, l), Fr(0)) + k * c
        if var == "z" and l > 0:
            out[(k, l - 1)] = out.get((k, l - 1), Fr(0)) + l * c
    return {key: v for key, v in out.items() if v != 0}


def badd(H, G, cg=Fr(1)):
    out = dict(H)
    for key, v in G.items():
        out[key] = out.get(key, Fr(0)) + cg * v
    return {key: v for key, v in out.items() if v != 0}


def bmul(H, G):
    out = {}
    for (k1, l1), a in H.items():
        for (k2, l2), b in G.items():
            key = (k1 + k2, l1 + l2)
            out[key] = out.get(key, Fr(0)) + a * b
    return {key: v for key, v in out.items() if v != 0}


def beval(H, s, z):
    return sum(c * s ** k * z ** l for (k, l), c in H.items())


def b_as_poly_in_z(H):
    """Return list over z-power of univariate polynomials in s."""
    if not H:
        return []
    degz = max(l for (_, l) in H)
    rows = [[] for _ in range(degz + 1)]
    for (k, l), c in H.items():
        p = rows[l]
        while len(p) <= k:
            p.append(Fr(0))
        p[k] += c
    return [ptrim(p) for p in rows]


def sylvester_resultant_in_z(F, G):
    """Res_z(F, G) as a polynomial in s (F, G bivariate dicts)."""
    f = b_as_poly_in_z(F)
    g = b_as_poly_in_z(G)
    df, dg = len(f) - 1, len(g) - 1
    n = df + dg
    M = [[[] for _ in range(n)] for _ in range(n)]
    # coefficients listed from highest z-power
    fc = list(reversed(f))
    gc = list(reversed(g))
    for i in range(dg):
        for j, c in enumerate(fc):
            M[i][i + j] = c
    for i in range(df):
        for j, c in enumerate(gc):
            M[dg + i][i + j] = c
    return poly_det(M)


def b_sub_z_const(H, zval):
    """H(s, zval) as a univariate polynomial in s."""
    out = []
    for (k, l), c in H.items():
        v = c * zval ** l
        while len(out) <= k:
            out.append(Fr(0))
        out[k] += v
    return ptrim(out)


# ---------------------------------------------------------------------------
# Hermite polynomials (probabilists') and exact Sturm root isolation.
# ---------------------------------------------------------------------------

def hermite_He(n):
    a, b = pconst(1), ptrim([Fr(0), Fr(1)])  # He_0, He_1
    if n == 0:
        return a
    for k in range(1, n):
        a, b = b, psub(pmul([Fr(0), Fr(1)], b), pscale(a, Fr(k)))
    return b


def sturm_sequence(p):
    seq = [ptrim(p), pderiv(p)]
    while seq[-1]:
        r = pdivmod(seq[-2], seq[-1])[1]
        if not r:
            break
        seq.append(pneg(r))
    return seq


def sign_changes(seq, x):
    vals = [peval(q, x) for q in seq]
    vals = [v for v in vals if v != 0]
    return sum(1 for a, b in zip(vals, vals[1:]) if (a > 0) != (b > 0))


def count_roots(seq, a, b):
    """Number of distinct real roots in (a, b]."""
    return sign_changes(seq, a) - sign_changes(seq, b)


def cauchy_bound(p):
    p = ptrim(p)
    return 1 + max(abs(c / p[-1]) for c in p[:-1]) if len(p) > 1 else Fr(1)


def isolate_roots(p):
    """Disjoint rational intervals (a, b] each holding exactly one root."""
    seq = sturm_sequence(p)
    B = cauchy_bound(p)
    stack = [(-B - 1, B + 1)]
    out = []
    while stack:
        a, b = stack.pop()
        n = count_roots(seq, a, b)
        if n == 0:
            continue
        if n == 1:
            out.append((a, b))
            continue
        mid = (a + b) / 2
        stack.append((a, mid))
        stack.append((mid, b))
    return sorted(out)


def refine_until_sign(p, q, a, b):
    """Shrink (a, b] around the unique root of p until q has no root in
    [a, b] and constant sign there; return that sign."""
    sp, sq = sturm_sequence(p), sturm_sequence(q)
    while True:
        if count_roots(sq, a, b) == 0 and peval(q, a) != 0 and peval(q, b) != 0 \
                and (peval(q, a) > 0) == (peval(q, b) > 0):
            return 1 if peval(q, a) > 0 else -1
        mid = (a + b) / 2
        if count_roots(sp, a, mid) == 1:
            b = mid
        else:
            a = mid


# ---------------------------------------------------------------------------
# Part A and B
# ---------------------------------------------------------------------------

def part_AB(m_max):
    results = []
    e1, e2 = Fr(3, 7), Fr(5, 11)
    for m in range(2, m_max + 1):
        H = hermite_germ(m)
        Hz = bderiv(H, "z")
        Hs = bderiv(H, "s")
        Hzz = bderiv(Hz, "z")
        # heat equation and the derivative identity H_z = m H_(m-1)
        check(f"m={m}: H_s = -H_zz", badd(Hs, Hzz) == {})
        check(f"m={m}: H_z = m H_(m-1)", Hz == {k: m * v for k, v in hermite_germ(m - 1).items()})
        # isolated common zero: chart z = 1 (covers all weighted orbits with z != 0)
        g = pgcd(b_sub_z_const(H, Fr(1)), b_sub_z_const(Hz, Fr(1)))
        check(f"m={m}: gcd(H(s,1), H_z(s,1)) constant", pdeg(g) == 0, {"gcd_degree": pdeg(g)})
        # chart z = 0: no common zero with s != 0
        h0, hz0 = b_sub_z_const(H, Fr(0)), b_sub_z_const(Hz, Fr(0))
        if m % 2 == 0:
            ok0 = pdeg(h0) == m // 2 and all(c == 0 for c in h0[:-1])
        else:
            ok0 = not h0 and pdeg(hz0) == (m - 1) // 2 and all(c == 0 for c in hz0[:-1])
        check(f"m={m}: z=0 chart has no common zero off the origin", ok0)
        # local degree via exact resultant degree
        F1 = badd(H, {(0, 0): -e1})
        F2 = badd(Hz, {(0, 0): -e2})
        R = sylvester_resultant_in_z(F1, F2)
        mu = pdeg(R)
        sqfree = pdeg(pgcd(R, pderiv(R))) == 0
        check(f"m={m}: resultant squarefree at e=(3/7,5/11)", sqfree)
        check(f"m={m}: local degree mu = m(m-1)/2", mu == m * (m - 1) // 2, {"mu": mu})
        # second generic point as a cross-check
        R2 = sylvester_resultant_in_z(badd(H, {(0, 0): Fr(-2, 9)}), badd(Hz, {(0, 0): Fr(1, 13)}))
        check(f"m={m}: local degree stable at a second value", pdeg(R2) == mu)
        # real index via Hermite roots, for e = (e1, 0), both signs of e1
        He_prev, He_m = hermite_He(m - 1), hermite_He(m)
        ivs = isolate_roots(He_prev)
        check(f"m={m}: He_(m-1) has m-1 real roots", len(ivs) == m - 1)
        signs = [refine_until_sign(He_prev, He_m, a, b) for a, b in ivs]
        n_pos = signs.count(1)
        n_neg = signs.count(-1)
        extra_pos = 1 if m % 2 == 0 else 0   # line z=0, s<0: H_m(s,0) > 0 there for even m
        idx_pos = -(n_pos + extra_pos)
        idx_neg = -n_neg
        check(f"m={m}: real index -floor(m/2) for e1>0", idx_pos == -(m // 2), {"index": idx_pos})
        check(f"m={m}: real index -floor(m/2) for e1<0", idx_neg == -(m // 2), {"index": idx_neg})
        # on every real preimage of (e1,0) the complex Jacobian is H_zz^2 > 0:
        # check the identity det_C = H_z H_zs - H_s H_zz = H_zz^2 - H_z H_zzz as polynomials
        detC = badd(bmul(Hz, bderiv(Hz, "s")), bmul(Hs, Hzz), Fr(-1))
        L1 = badd(bmul(Hzz, Hzz), bmul(Hz, bderiv(Hzz, "z")), Fr(-1))
        check(f"m={m}: det_C(z,s order) equals L_1 = H_zz^2 - H_z H_zzz", badd(detC, L1, Fr(-1)) == {})
        check(f"m={m}: mu - floor(m/2) even, zero only for m=2",
              (mu - m // 2) % 2 == 0 and ((mu - m // 2 == 0) == (m == 2)))
        results.append({"m": m, "complex_local_degree": mu, "real_index": idx_pos,
                        "He_sign_counts": {"positive": n_pos, "negative": n_neg},
                        "difference": mu - m // 2})
    return results


# ---------------------------------------------------------------------------
# Part C: deformed commutation on a Gaussian source (floating point)
# ---------------------------------------------------------------------------

def part_C():
    out = []
    for (t, d, x) in [(0.2, 2, 3.5), (0.05, 3, 11.0), (0.45, 7, -2.25), (0.3, 5, 0.75)]:
        a = 0.5 * math.log(d)
        A = 1.0 - t
        # H_Phi(t,x) for Phi = exp(-u^2):   sqrt(pi/A) exp(-x^2/(4A)), valid for complex x
        def Hg(xx):
            return cmath.sqrt(math.pi / A) * cmath.exp(-(xx * xx) / (4 * A))
        # H_{D_d Phi}(t,x) = d^{-1/2} int exp(t u^2 - (u+a)^2 + i x u) du, exponent -A u^2 + (ix-2a) u - a^2
        B = 1j * x - 2 * a
        lhs = d ** -0.5 * cmath.sqrt(math.pi / A) * cmath.exp(B * B / (4 * A) - a * a)
        rhs = d ** -0.5 * cmath.exp(t * a * a - 1j * a * x) * Hg(x + 2j * t * a)
        rel = abs(lhs - rhs) / abs(rhs)
        check(f"C: transform shift identity at t={t}, d={d}, x={x} (float)", rel < 1e-12, {"relative_error": rel})
        # pointwise multiplier identity: M_t D_d f = exp(-2 t a u - t a^2) D_d M_t f, f(u)=exp(-u^2)
        u = 0.37
        f = lambda v: math.exp(-v * v)
        left = math.exp(t * u * u) * d ** -0.5 * f(u + a)
        right = math.exp(-2 * t * a * u - t * a * a) * d ** -0.5 * math.exp(t * (u + a) ** 2) * f(u + a)
        check(f"C: multiplier identity at t={t}, d={d} (float)", abs(left - right) <= 1e-14 * abs(right))
        out.append({"t": t, "d": d, "x": x, "relative_error": rel})
    return out


# ---------------------------------------------------------------------------
# Part D and E: the two polynomial controls and the endpoint logic
# ---------------------------------------------------------------------------

def part_DE():
    T = Fr(3, 10)
    # germ x^2 + 2(T - t): L_0 = H_x^2 - H H_xx at x = 0
    for t in [Fr(1, 10), Fr(2, 10), T, Fr(4, 10)]:
        H = 2 * (T - t)
        Hx, Hxx = Fr(0), Fr(2)
        L0 = Hx * Hx - H * Hxx
        E = H * H + Hx * Hx
        check(f"D: germ L_0(t,0) = -4(T-t) at t={t}", L0 == -4 * (T - t), {"L0": str(L0), "E": str(E)})
        if t < T:
            check(f"E: sign fails before the collision at t={t}", L0 < 0 and E > 0)
        elif t == T:
            check("E: at the collision the strict sign fails and the weak sign holds", L0 == 0 and E == 0)
        else:
            check(f"E: strict sign holds after the collision at t={t}", L0 > 0)
    # control z^2 - 2 tau + 1 in (s, z) with H_s = -H_zz: H = z^2 - 2(1/2 - s) ... use tau directly:
    # H(tau, z) = z^2 - 2 tau + 1, H_z = 2z.  Common zeros: z = 0, tau = 1/2 only.
    Htau = {(0, 2): Fr(1), (1, 0): Fr(-2), (0, 0): Fr(1)}   # key (tau-power, z-power)
    Hz = bderiv(Htau, "z")
    R = sylvester_resultant_in_z(Htau, Hz)
    check("D: Res_z(H, H_z) for z^2 - 2tau + 1 is a nonzero multiple of (tau - 1/2)",
          pdeg(R) == 1 and peval(R, Fr(1, 2)) == 0, {"resultant": [str(c) for c in R]})
    for t in [Fr(0), Fr(1, 4), Fr(49, 100)]:
        E = (1 - 2 * t) ** 2
        check(f"D: E(t,0) = (1-2t)^2 at t={t}", beval(Htau, t, Fr(0)) ** 2 + 0 == E)
    # the m=3 example of Response 17: H = z^3 - 6 tau z, three preimages of (eps, 0), one real
    H3 = hermite_germ(3)        # in (s, z) with s = -tau orientation: z^3 - 6 s z ... sign convention below
    # hermite_germ(3) = z^3 - 6 s z^1 with H_s = -H_zz; Response 17 writes z^3 - 6 tau z with H_tau = -H_zz.
    check("D: m=3 germ is z^3 - 6 s z", H3 == {(0, 3): Fr(1), (1, 1): Fr(-6)})
    Hz3 = bderiv(H3, "z")
    R3 = sylvester_resultant_in_z(badd(H3, {(0, 0): Fr(-1, 5)}), Hz3)
    check("D: m=3, e=(1/5,0): three preimages", pdeg(R3) == 3)
    # exactly one real s-root? the real preimage has s = z^2/2 with z^3 = -e/2 < 0: one real z, one real s
    rr = isolate_roots(R3)
    check("D: m=3, e=(1/5,0): the resultant in s has exactly one real root", len(rr) == 1)
    # det_C = 36 z^2 on the preimages (where s = z^2/2): det_C = 18 z^2 + 36 s
    detC = badd(bmul(Hz3, bderiv(Hz3, "s")), bmul(bderiv(H3, "s"), bderiv(Hz3, "z")), Fr(-1))
    check("D: m=3 complex Jacobian is 18 z^2 + 36 s", detC == {(0, 2): Fr(18), (1, 0): Fr(36)})
    return {"T": str(T)}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--m-max", type=int, default=9)
    ap.add_argument("--output", help="write the JSON record here")
    args = ap.parse_args()
    ab = part_AB(args.m_max)
    c = part_C()
    de = part_DE()
    with open(__file__, "rb") as fh:
        self_hash = hashlib.sha256(fh.read()).hexdigest()
    record = {
        "title": "Heat-germ local degrees, real indices, deformed commutation and the two polynomial controls",
        "prepared_for": "Edward Baker",
        "model": "Claude Fable 5.1 (claude-fable-5-1), Claude Cowork, 15 October 2026",
        "script_sha256": self_hash,
        "python": sys.version.split()[0],
        "arithmetic": "exact rational (fractions.Fraction) in parts A, B, D, E; floating point in part C",
        "germ_table": ab,
        "formula": "complex local degree mu_m = m(m-1)/2 (weighted Bezout, weights 2 and 1); real index -floor(m/2)",
        "part_C": c,
        "part_DE": de,
        "assertions_total": len(ASSERTIONS),
        "assertions_failed": sum(1 for a in ASSERTIONS if not a["ok"]),
        "assertions": ASSERTIONS,
        "scope": ("Polynomial heat germs and closed-form Gaussian transforms only. "
                  "Nothing here evaluates the theta field, certifies a theta sign, or bears on RH."),
    }
    text = json.dumps(record, indent=1)
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(text + "\n")
    print(json.dumps({k: v for k, v in record.items() if k != "assertions"}, indent=1))
    return 0 if record["assertions_failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
