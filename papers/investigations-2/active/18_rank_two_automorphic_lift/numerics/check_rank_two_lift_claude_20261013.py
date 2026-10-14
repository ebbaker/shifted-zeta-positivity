#!/usr/bin/env python3
"""Checks for direction 18 (rank-two automorphic lift), first note.

Prepared for Edward Baker with LLM assistance, 13 October 2026.
Model: Claude Opus 5.5 (configured identifier claude-opus-5-5), Claude Cowork,
reasoning effort max.

Standard library only.  Part E uses exact rational arithmetic.  Part N is a
double-precision quadrature replay; it is evidence, not an interval
certificate.

Run:
    python3 -I check_rank_two_lift_claude_20261013.py --output RECORD.json

Notation (see notes/1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md):
    Phi(u) = sum_n (2 pi^2 n^4 e^{9u} - 3 pi n^2 e^{5u}) exp(-pi n^2 e^{4u}),
    H_t(x) = (1/2) int e^{t u^2 + i x u} Phi(u) du,
    L0 = H_x^2 - H H_xx,   L1 = H_xx^2 - H_x H_xxx,
    D(sigma, rho) = (((sigma+rho)^2)/4 - 1)(((sigma-rho)^2)/4 - 1),
    K_w(y) = 4 sqrt(y) sum_n lambda_w(n) K_{w-1/2}(2 pi n y),
    lambda_w(n) = sum_{ab=n} (a/b)^{w-1/2}.
Theorem 1:  int e^{kappa s} Phi(s+r) Phi(s-r) ds
            = (1/512) D(-kappa, d/dr) K_{1/2+kappa/4}(e^{4r}).
Theorem 2:  L_j(H_t; x) = int int r^2 (r^2 - s^2)^j e^{2t(s^2+r^2)}
            Phi(s+r) Phi(s-r) e^{2ixs} ds dr, rewritten with Theorem 1 and
            e^{2ts^2} = E exp(V s), V ~ N(0, 4t).
"""

import argparse
import cmath
import hashlib
import json
import math
import platform
import random
import sys
from fractions import Fraction as Fr

PI = math.pi
RESULTS = {}
FAILURES = []


def record(section, name, value, ok=True):
    RESULTS.setdefault(section, {})[name] = value
    if not ok:
        FAILURES.append(f"{section}/{name}")


def sig(x, d=12):
    if isinstance(x, complex):
        return [sig(x.real, d), sig(x.imag, d)]
    if x == 0 or not math.isfinite(x):
        return x
    return float(f"{x:.{d}g}")


def err3(x):
    return float(f"{x:.2g}")


# ---------------------------------------------------------------------------
# Part E: exact algebra
# ---------------------------------------------------------------------------

class Poly:
    """Univariate polynomial with Fraction coefficients (index = degree)."""

    def __init__(self, c):
        c = [Fr(v) for v in c]
        while len(c) > 1 and c[-1] == 0:
            c.pop()
        self.c = c

    def __add__(self, o):
        o = o if isinstance(o, Poly) else Poly([o])
        n = max(len(self.c), len(o.c))
        return Poly([(self.c[i] if i < len(self.c) else 0) + (o.c[i] if i < len(o.c) else 0) for i in range(n)])

    __radd__ = __add__

    def __neg__(self):
        return Poly([-v for v in self.c])

    def __sub__(self, o):
        return self + (-(o if isinstance(o, Poly) else Poly([o])))

    def __rsub__(self, o):
        return Poly([o]) - self

    def __mul__(self, o):
        o = o if isinstance(o, Poly) else Poly([o])
        out = [Fr(0)] * (len(self.c) + len(o.c) - 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(o.c):
                out[i + j] += a * b
        return Poly(out)

    __rmul__ = __mul__

    def is_zero(self):
        return all(v == 0 for v in self.c)


def D_sym(sigma, rho):
    return ((sigma + rho) * (sigma + rho) * Fr(1, 4) - 1) * ((sigma - rho) * (sigma - rho) * Fr(1, 4) - 1)


def part_e():
    w = Poly([0, 1])
    sigma = 2 - 4 * w  # sigma = -kappa, kappa = 4w - 2
    names = {"w": w, "1-w": 1 - w, "-w": -w, "w-1": w - 1}
    ann = {}
    for name, beta in names.items():
        ann[name] = D_sym(sigma, 4 * beta).is_zero()
    record("E_exact", "E1_insertion_annihilates_four_constant_term_powers", ann, all(ann.values()))

    # expanded form of D
    rng = random.Random(20261013)
    ok = True
    for _ in range(40):
        s = Fr(rng.randint(-50, 50), rng.randint(1, 9))
        r = Fr(rng.randint(-50, 50), rng.randint(1, 9))
        lhs = ((s + r) ** 2 / 4 - 1) * ((s - r) ** 2 / 4 - 1)
        rhs = (s * s / 4 - 1) ** 2 - (s * s / 8 + Fr(1, 2)) * r * r + r ** 4 / 16
        ok &= lhs == rhs
    record("E_exact", "E1b_expanded_form_D", ok, ok)

    # E2: (d^2/du^2 - 1)[X e^{-Y}] = 8 (2 Y^2 X - 3 Y X) e^{-Y}, X = e^u, Y = pi n^2 e^{4u}
    # represent P(X,Y) e^{-Y} by dict {(i,j): coeff}; d/du acts as X dX + 4 Y dY - 4 Y.
    def ddu(P):
        out = {}
        for (i, j), c in P.items():
            for key, val in (((i, j), c * (i + 4 * j)), ((i, j + 1), -4 * c)):
                if val:
                    out[key] = out.get(key, 0) + val
        return {k: v for k, v in out.items() if v}
    F = {(1, 0): Fr(1)}
    F2 = ddu(ddu(F))
    lhs = dict(F2)
    lhs[(1, 0)] = lhs.get((1, 0), 0) - 1
    lhs = {k: v for k, v in lhs.items() if v}
    rhs = {(1, 2): Fr(16), (1, 1): Fr(-24)}
    record("E_exact", "E2_insertion_generates_theta_term", lhs == rhs, lhs == rhs)

    # E3: pair weights.  L0 integrand (1/4)(u2^2 - u1 u2), L1 integrand (1/4)(u1^2 u2^2 - u1 u2^3);
    # symmetrize, substitute u = s +- r, Jacobian 2 -> r^2 and r^2 (r^2 - s^2).
    ok0 = ok1 = True
    for _ in range(40):
        s = Fr(rng.randint(-30, 30), rng.randint(1, 7))
        r = Fr(rng.randint(-30, 30), rng.randint(1, 7))
        u1, u2 = s + r, s - r
        sym0 = Fr(1, 4) * ((u2 * u2 - u1 * u2) + (u1 * u1 - u2 * u1)) / 2
        sym1 = Fr(1, 4) * ((u1 * u1 * u2 * u2 - u1 * u2 ** 3) + (u2 * u2 * u1 * u1 - u2 * u1 ** 3)) / 2
        ok0 &= 2 * sym0 == r * r
        ok1 &= 2 * sym1 == r * r * (r * r - s * s)
    record("E_exact", "E3_pair_weights_r2_and_r2(r2-s2)", {"L0": ok0, "L1": ok1}, ok0 and ok1)

    # E4: Gaussian tilting.  d^k/da^k e^{2 t a^2} = q_k(a) e^{2 t a^2} with q_{k+1} = q_k' + 4 t a q_k;
    # claim q_k(a) = E[(4 t a + Z)^k], Z ~ N(0, 4t).  Check as polynomials in a at rational t.
    ok = True
    for t in (Fr(1, 20), Fr(3, 7), Fr(2)):
        q = Poly([1])
        for k in range(0, 9):
            # expectation polynomial
            e = Poly([0])
            for j in range(0, k + 1, 2):
                dfact = 1
                for m in range(j - 1, 0, -2):
                    dfact *= m
                mom = (4 * t) ** (j // 2) * dfact
                e = e + Poly([math.comb(k, j) * mom]) * _pow(Poly([0, 4 * t]), k - j)
            ok &= (q - e).is_zero()
            # next derivative
            dq = Poly([i * q.c[i] for i in range(1, len(q.c))] or [0])
            q = dq + Poly([0, 4 * t]) * q
    record("E_exact", "E4_gaussian_tilting_moments_k_le_8", ok, ok)

    # E5: index-two sublattice counting and the rectangular two-coset identity.
    okc = True
    for m in range(-12, 13):
        for n in range(-12, 13):
            cnt = (m % 2 == 0) + (n % 2 == 0) + ((m - n) % 2 == 0)
            okc &= cnt == 1 + 2 * (m % 2 == 0 and n % 2 == 0)
    okp = True
    for _ in range(40):
        A, B, C, Dv = (Fr(rng.randint(-40, 40), rng.randint(1, 9)) for _ in range(4))
        okp &= B * C + A * Dv + B * Dv + (A - B) * (C - Dv) == A * C + 2 * B * Dv
    record("E_exact", "E5_index_two_sublattice_count_and_coset_identity", {"count": okc, "theta_identity": okp}, okc and okp)

    # E6: pair two-coset identity over Q(sqrt 2) (pairs (a, b) = a + b sqrt2).
    def qm(x, y):
        return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def qa(*xs):
        return (sum(x[0] for x in xs), sum(x[1] for x in xs))

    def qs(x, y):
        return (x[0] - y[0], x[1] - y[1])

    r2 = (Fr(0), Fr(1))
    inv_r2 = (Fr(0), Fr(1, 2))
    ok = True
    for _ in range(40):
        P1, M1, P2, M2 = ((Fr(rng.randint(-40, 40), rng.randint(1, 9)), Fr(0)) for _ in range(4))
        e1, e2 = qm(inv_r2, P1), qm(inv_r2, P2)          # Phi_e(u_i - beta)
        o1, o2 = qs(M1, e1), qs(M2, e2)                   # Phi_o(u_i - beta)
        lhs = qa(qm(P1, M2), qm(M1, P2), qm(r2, qa(qm(e1, e2), qm(o1, o2))))
        rhs = qm(r2, qa(qm(M1, M2), qm(P1, P2)))
        ok &= lhs == rhs
    record("E_exact", "E6_pair_two_coset_identity_Q_sqrt2", ok, ok)

    # E7: Hecke multiplicativity at 2 as an identity of multisets of ratios a/b.
    def R(n):
        out = []
        for a in range(1, n + 1):
            if n % a == 0:
                out.append(Fr(a, n // a))
        return sorted(out)
    ok = True
    for m in range(1, 129):
        left = sorted([2 * x for x in R(m)] + [x / 2 for x in R(m)])
        right = sorted(R(2 * m) + (R(m // 2) if m % 2 == 0 else []))
        ok &= left == right
    record("E_exact", "E7_hecke_relation_at_2_ratio_multisets_m_le_128", ok, ok)

    # E8: control coefficients a_n = 1 + (2 sqrt p / c) 1_{p|n} + p 1_{p^2|n}: a_{2m} = a_m iff p odd.
    def a_ind(n, p):
        return (n % p == 0, n % (p * p) == 0)
    odd_ok = all(a_ind(2 * m, p) == a_ind(m, p) for p in (3, 5, 7, 11) for m in range(1, 400))
    two_fails = a_ind(2, 2) != a_ind(1, 2)
    record("E_exact", "E8_two_adic_self_similarity_of_controls",
           {"holds_for_p_in_3_5_7_11": odd_ok, "fails_for_p_2": two_fails}, odd_ok and two_fails)


def _pow(p, k):
    out = Poly([1])
    for _ in range(k):
        out = out * p
    return out


# ---------------------------------------------------------------------------
# Part N: double-precision replay
# ---------------------------------------------------------------------------

def gauss_legendre(n):
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(PI * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-16:
                break
        xs.append(x)
        ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws


def phi_series(z):
    e4, e5, e9 = cmath.exp(4 * z), cmath.exp(5 * z), cmath.exp(9 * z)
    s = 0j
    n = 1
    while True:
        t = (2 * PI * PI * n ** 4 * e9 - 3 * PI * n * n * e5) * cmath.exp(-PI * n * n * e4)
        s += t
        if abs(t) < 1e-32 and n >= 2:
            break
        n += 1
    return s


def phi(z):
    z = complex(z)
    return phi_series(-z if z.real < 0 else z)


def moments(t, x, src, theta=0.3, U=2.0, n=1200, kmax=3):
    """M_k = int u^k e^{t u^2} src(u) e^{i x u} du on the line Im u = theta (full line)."""
    h = 2 * U / n
    out = [0j] * (kmax + 1)
    for j in range(n + 1):
        z = complex(-U + j * h, theta)
        wgt = 0.5 if j in (0, n) else 1.0
        base = wgt * cmath.exp(t * z * z + 1j * x * z) * src(z)
        p = 1
        for k in range(kmax + 1):
            out[k] += p * base
            p *= z
    return [h * o for o in out]


def laguerre_direct(t, x):
    M = moments(t, x, phi)
    H = [0.5 * M[k] * (1j) ** k for k in range(4)]   # H^{(k)} = (1/2) int (iu)^k ...
    return (H[1] ** 2 - H[0] * H[2]), (H[2] ** 2 - H[1] * H[3]), H


P_POLY = [[1.0]]
for _k in range(4):
    cur = P_POLY[-1]
    nxt = [0.0] * (len(cur) + 1)
    for i, c in enumerate(cur):
        nxt[i] += 2 * c
        nxt[i + 1] += -4 * c
        if i >= 1:
            nxt[i] += 4 * i * c
    P_POLY.append(nxt)


def peval(coeffs, z):
    s = 0
    for c in reversed(coeffs):
        s = s * z + c
    return s


def gauss_expect(poly, c0, var):
    mom = [1, 0, var, 0, 3 * var * var, 0, 15 * var ** 3]
    total = 0
    for k, ck in enumerate(poly):
        if ck == 0:
            continue
        s = 0
        for j in range(0, k + 1, 2):
            s += math.comb(k, j) * c0 ** (k - j) * mom[j]
        total += ck * s
    return total


def pderiv(a):
    return [i * a[i] for i in range(1, len(a))] or [0]


def padd(*ps):
    n = max(len(p) for p in ps)
    return [sum(p[i] if i < len(p) else 0 for p in ps) for i in range(n)]


def pscale(a, c):
    return [c * v for v in a]


def cusp_pieces(y, n, theta, vmax, nv):
    """Yield (weight, L, C) for the Whittaker integral of mode n at shape y on Im v = theta."""
    hv = 2 * vmax / nv
    for a in range(1, n + 1):
        if n % a:
            continue
        ell = math.log(a / (n // a))
        for k in range(nv + 1):
            vc = complex(-vmax + k * hv, theta)
            C = 2 * PI * n * y * cmath.cosh(vc)
            if C.real > 95:
                continue
            yield (0.5 if k in (0, nv) else 1.0) * hv, vc + ell, C


def kernel_fixed_r(r, kappa, theta=1.0, vmax=4.5, nv=600, nmax=12):
    """(1/512) D(-kappa, d/dr) K_{1/2+kappa/4}(e^{4r}) via the Whittaker integral."""
    y = math.exp(4 * r)
    A = (kappa * kappa / 4 - 1) ** 2
    B = kappa * kappa / 8 + 0.5
    tot = 0j
    for n in range(1, nmax + 1):
        for wv, L, C in cusp_pieces(y, n, theta, vmax, nv):
            g = A - B * peval(P_POLY[2], C) + peval(P_POLY[4], C) / 16
            tot += wv * 2 * math.sqrt(y) * cmath.exp(-C + kappa * L / 4) * g
    return tot / 512


def pair_fixed_r(r, kappa, S=2.5, n=5000):
    h = 2 * S / n
    tot = 0j
    for j in range(n + 1):
        s = -S + j * h
        wgt = 0.5 if j in (0, n) else 1.0
        tot += wgt * cmath.exp(kappa * s) * phi(s + r) * phi(s - r)
    return tot * h


def lift(t, x, want_L1=True, Rmax=0.6, nr=32, vmax=4.5, nv=300, theta=1.0, nmax=10):
    """Theorem 2: returns (L0, L1, modes) with modes[n] = contribution of Whittaker mode n to L0."""
    rs, rws = gauss_legendre(nr)
    var = 4 * t
    L0 = 0j
    L1 = 0j
    modes = {}
    for q, qw in zip(rs, rws):
        r = 0.5 * Rmax * (q + 1)
        rw = 0.5 * Rmax * qw
        y = math.exp(4 * r)
        wr = r * r * math.exp(2 * t * r * r)
        for n in range(1, nmax + 1):
            S0 = 0j
            S2 = 0j
            for wv, L, C in cusp_pieces(y, n, theta, vmax, nv):
                P2 = peval(P_POLY[2], C)
                P4 = peval(P_POLY[4], C)
                g = [1 - P2 / 2 + P4 / 16, 0, -0.5 - P2 / 8, 0, 1 / 16]
                pref = wv * 2 * math.sqrt(y) * cmath.exp(-C + 1j * x * L / 2 + t * L * L / 8)
                c0 = 2j * x + t * L
                S0 += pref * gauss_expect(g, c0, var)
                if want_L1:
                    g1 = pderiv(g)
                    g2 = pderiv(g1)
                    qp = padd(pscale(g, (L / 4) ** 2), pscale(g1, L / 2), g2)
                    S2 += pref * gauss_expect(qp, c0, var)
            modes[n] = modes.get(n, 0) + rw * wr * S0 / 256
            L0 += rw * wr * S0 / 256
            if want_L1:
                L1 += rw * wr * (r * r * S0 - S2) / 256
    return L0, L1, modes


def whittaker_K(y, w, theta=1.0, vmax=5.0, nv=800, nmax=40, twist=False):
    """Cusp part of E*(x0 + iy, w): x0 = 0 (twist False) or 1/2 (twist True)."""
    nu = w - 0.5
    tot = 0j
    for n in range(1, nmax + 1):
        sgn = (-1) ** n if twist else 1
        part = 0j
        for wv, L, C in cusp_pieces(y, n, theta, vmax, nv):
            part += wv * cmath.exp(-C + nu * L)
        tot += sgn * part
    return 2 * math.sqrt(y) * tot



def lift_translated(t, x, alpha, beta, Rmax=0.6, nr=40, vmax=4.5, nv=300, theta=1.0, nmax=10):
    """Proposition 4(a) term: E_V[e^{-kappa alpha} int_R (r-beta)^2 e^{2t(r-beta)^2} K_kappa(r) dr], kappa = 2ix+V.

    Uses evenness of K_kappa in r; the factor e^{-V alpha} is absorbed by Gaussian tilting."""
    rs, rws = gauss_legendre(nr)
    var = 4 * t
    tot = 0j
    for q, qw in zip(rs, rws):
        r = 0.5 * Rmax * (q + 1)
        rw = 0.5 * Rmax * qw
        y = math.exp(4 * r)
        W = (r - beta) ** 2 * math.exp(2 * t * (r - beta) ** 2) + (r + beta) ** 2 * math.exp(2 * t * (r + beta) ** 2)
        S0 = 0j
        for n in range(1, nmax + 1):
            for wv, L, C in cusp_pieces(y, n, theta, vmax, nv):
                P2 = peval(P_POLY[2], C)
                P4 = peval(P_POLY[4], C)
                g = [1 - P2 / 2 + P4 / 16, 0, -0.5 - P2 / 8, 0, 1 / 16]
                lam = L / 4 - alpha
                pref = wv * 2 * math.sqrt(y) * cmath.exp(-C + 0.5j * x * L - 2j * x * alpha + 2 * t * lam * lam)
                S0 += pref * gauss_expect(g, 2j * x + 4 * t * lam, var)
        tot += rw * W * S0 / 512
    return tot


def part_n():
    # N1 fixed-r identity (Theorem 1), including complex kappa
    rows = []
    worst = 0.0
    for r, kappa in [(0.0, 8j), (0.1, 16j), (0.3, 16j), (0.05, 0.7 + 3j), (0.2, 0.4 + 16j)]:
        lhs = pair_fixed_r(r, kappa)
        rhs = kernel_fixed_r(r, kappa)
        e = abs(lhs - rhs) / abs(lhs)
        worst = max(worst, e)
        rows.append({"r": r, "kappa": sig(complex(kappa), 6), "pair_integral": sig(lhs, 12), "cusp_formula": sig(rhs, 12), "rel_err": err3(e)})
    record("N_float", "N1_fixed_r_identity", {"rows": rows, "max_rel_err": err3(worst)}, worst < 1e-9)

    # N2 Newman-time Laguerre expressions
    rows = []
    worst = 0.0
    for t, x in [(0.0, 8.0), (0.05, 8.0), (0.05, 28.27)]:
        L0d, L1d, H = laguerre_direct(t, x)
        L0l, L1l, _ = lift(t, x)
        e0 = abs(L0d - L0l) / abs(L0d)
        e1 = abs(L1d - L1l) / abs(L1d)
        worst = max(worst, e0, e1)
        rows.append({"t": t, "x": x, "H": sig(H[0].real), "L0_direct": sig(L0d.real), "L0_lift": sig(L0l.real),
                     "L1_direct": sig(L1d.real), "L1_lift": sig(L1l.real), "rel_err_L0": err3(e0), "rel_err_L1": err3(e1)})
    record("N_float", "N2_newman_time_cusp_formula", {"rows": rows, "max_rel_err": err3(worst)}, worst < 1e-9)

    # N3 Whittaker-mode shares of L0 (diagnostic)
    rows = []
    worst = 0.0
    for t in (0.0, 0.05):
        for x in (4.0, 8.0, 12.0, 20.0, 28.27, 42.0):
            L0d, _, _ = laguerre_direct(t, x)
            L0l, _, modes = lift(t, x, want_L1=False)
            e = abs(L0d - L0l) / abs(L0d)
            worst = max(worst, e)
            rows.append({"t": t, "x": x, "L0": sig(L0d.real, 6),
                         "mode_share": {str(n): sig(modes[n].real / L0d.real, 4) for n in range(1, 5)},
                         "rel_err_total": err3(e)})
    record("N_float", "N3_whittaker_mode_shares", {"rows": rows, "max_rel_err": err3(worst)}, worst < 1e-8)

    # N3b higher heights: the mode expansion starts to oscillate (diagnostic; contour Im v closer to pi/2)
    rows = []
    worst = 0.0
    for x, theta, vmax, nv, nmax in ((46.0, 1.2, 5.5, 1400, 20), (54.0, 1.2, 5.5, 1400, 20),
                                     (80.0, 1.3, 6.0, 2400, 24), (100.0, 1.36, 6.5, 3600, 28)):
        L0d, _, _ = laguerre_direct(0.0, x)
        L0l, _, modes = lift(0.0, x, want_L1=False, Rmax=0.6, nr=40, vmax=vmax, nv=nv, theta=theta, nmax=nmax)
        e = abs(L0d - L0l) / abs(L0d)
        worst = max(worst, e)
        rows.append({"t": 0.0, "x": x, "L0": sig(L0d.real, 6),
                     "mode_share": {str(n): sig(modes[n].real / L0d.real, 4) for n in range(1, 6)},
                     "rel_err_total": err3(e)})
    record("N_float", "N3b_mode_shares_higher_heights", {"rows": rows, "max_rel_err": err3(worst)}, worst < 1e-3)

    # N3c sign of the folded kernel K_{2ix}(r) = int e^{2ixs} Phi(s+r) Phi(s-r) ds on r in [0, 0.6]
    rows = []
    for x in (8.0, 16.0, 22.0, 22.5, 28.27):
        vals = [pair_fixed_r(0.05 * j, 2j * x, n=1500).real for j in range(13)]
        rows.append({"x": x, "kernel_at_r0": sig(vals[0], 6), "min_over_grid": sig(min(vals), 6),
                     "positive_on_grid": all(v > 0 for v in vals)})
    ok = rows[0]["positive_on_grid"] and rows[2]["positive_on_grid"] and not rows[3]["positive_on_grid"] and not rows[4]["positive_on_grid"]
    record("N_float", "N3c_folded_kernel_sign", {"rows": rows}, ok)

    # N4 Hecke relation at 2 on the geodesics Re z = 0 and Re z = 1/2 (cusp parts)
    rows = []
    worst = 0.0
    for w in (0.5 + 4j, 0.5 + 14.134725141734694j, 0.7 + 3j):
        lam2 = 2 ** (w - 0.5) + 2 ** (0.5 - w)
        for y in (0.9, 1.0, 1.7):
            lhs = whittaker_K(2 * y, w) + whittaker_K(y / 2, w) + whittaker_K(y / 2, w, twist=True)
            rhs = math.sqrt(2) * lam2 * whittaker_K(y, w)
            scale = abs(whittaker_K(2 * y, w)) + abs(whittaker_K(y / 2, w)) + abs(rhs)
            e = abs(lhs - rhs) / scale
            worst = max(worst, e)
            rows.append({"w": sig(complex(w), 10), "y": y, "lhs": sig(lhs, 10), "rhs": sig(rhs, 10), "scaled_err": err3(e)})
    record("N_float", "N4_hecke_at_2_two_geodesics", {"rows": rows, "max_scaled_err": err3(worst)}, worst < 1e-10)

    # N5 two-coset identity at Newman time, physical form (Theorem 3)
    beta = 0.25 * math.log(2)

    def phi_e(z):
        return phi(z + 2 * beta) / math.sqrt(2)

    def sym(MF, MG):
        # weight-r^2 pair transform of F(u1)G(u2) + G(u1)F(u2): (1/4)[M2F M0G + M0F M2G - 2 M1F M1G]
        return 0.25 * (MF[2] * MG[0] + MF[0] * MG[2] - 2 * MF[1] * MG[1])

    def diag(M):
        # weight-r^2 pair transform of F(u1)F(u2): (1/4)(M0 M2 - M1^2); equals L0 for F = Phi
        return 0.25 * (M[0] * M[2] - M[1] * M[1])

    rows = []
    worst = 0.0
    for t, x in [(0.0, 8.0), (0.05, 8.0), (0.1, 20.0)]:
        Mp = moments(t, x, lambda z: phi(z + beta), kmax=2)
        Mm = moments(t, x, lambda z: phi(z - beta), kmax=2)
        Me = moments(t, x, lambda z: phi_e(z - beta), kmax=2)
        Mo = moments(t, x, lambda z: phi(z - beta) - phi_e(z - beta), kmax=2)
        unequal = sym(Mp, Mm)                                # Pi(s, r+beta) + Pi(s, r-beta)
        twisted = math.sqrt(2) * (diag(Me) + diag(Mo))       # Pi_tw
        lhs = unequal + twisted
        Mz1 = moments(t, x - 2j * t * beta, phi, kmax=2)
        Mz2 = moments(t, x + 2j * t * beta, phi, kmax=2)
        rhs = math.sqrt(2) * math.exp(2 * t * beta * beta) * (
            cmath.exp(2j * x * beta) * diag(Mz1) + cmath.exp(-2j * x * beta) * diag(Mz2))
        L0chk = abs(diag(moments(t, x, phi, kmax=2)) - laguerre_direct(t, x)[0])
        e = abs(lhs - rhs) / (abs(unequal) + abs(twisted))
        worst = max(worst, e)
        worst = max(worst, L0chk / abs(unequal))
        rows.append({"t": t, "x": x, "unequal_scale_channel": sig(unequal.real, 10), "twisted_channel": sig(twisted.real, 10),
                     "volume_shifted_rhs": sig(rhs.real, 10), "scaled_err": err3(e)})
    record("N_float", "N5_two_coset_identity_newman_time", {"rows": rows, "max_scaled_err": err3(worst)}, worst < 1e-10)

    # N6 control test of the q-adic self-similarity behind the two-coset identity:
    # Phi - q^{-1/2} Phi(. + (1/2) log q) equals the part with q not dividing n iff the Dirichlet
    # coefficients satisfy a_{qm} = a_m.  For Phi_{c,p} this holds iff q != p.
    def phi1(z):
        return (2 * PI * PI * cmath.exp(9 * z) - 3 * PI * cmath.exp(5 * z)) * cmath.exp(-PI * cmath.exp(4 * z))

    def control(p, c):
        if c == 0:
            return phi
        a = 0.5 * math.log(p)
        return lambda z: phi(z) + 0.5 * c * (phi(z + a) + phi(z - a))

    def coprime_part(p, c, q, u):
        # Phi_{c,p}(u) = sum_n (c/2) p^{-1/2} a_n (n/p)^{-1/2} phi1(u + (1/2) log(n/p)); keep q not dividing n.
        tot = 0.0
        for n in range(1, 6000):
            if n % q == 0:
                continue
            nu = n / p if c else float(n)
            if PI * nu * nu * math.exp(4 * u) > 800:
                break
            if c:
                an = 0.5 * c / math.sqrt(p) * (1 + (2 * math.sqrt(p) / c) * (n % p == 0) + p * (n % (p * p) == 0))
            else:
                an = 1.0
            tot += an * nu ** -0.5 * phi1(complex(u + 0.5 * math.log(nu), 0)).real
        return tot

    out = {}
    ok = True
    for p, c in ((2, 0.0), (2, 0.5), (3, 0.5)):
        F = control(p, c)
        for q in (2, 3):
            worst = 0.0
            scale = 0.0
            for j in range(0, 41):
                u = -0.5 + j * 0.05
                lhs = (F(u) - F(u + 0.5 * math.log(q)) / math.sqrt(q)).real
                rhs = coprime_part(p, c, q, u)
                worst = max(worst, abs(lhs - rhs))
                scale = max(scale, abs(F(u).real))
            ratio = worst / scale
            label = "theta" if c == 0 else f"Phi_c={c},p={p}"
            out[f"{label}|q={q}"] = err3(ratio)
            expect_hold = (c == 0) or (q != p)
            ok &= (ratio < 1e-12) if expect_hold else (ratio > 1e-2)
    record("N_float", "N6_q_adic_self_similarity_control_test", out, ok)


    # N7 Proposition 4(a): controls = same cusp kernel with translated weights and volume phases
    rows = []
    worst = 0.0
    for p, c, t, x in ((3, 0.5, 0.05, 5.0), (2, 0.5, 0.0, 9.0), (5, 0.7, 0.1, 3.0)):
        a = 0.5 * math.log(p)
        cc = {0: 1.0, 1: c / 2, -1: c / 2}
        tot = 0j
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                tot += cc[j] * cc[k] * lift_translated(t, x, (j + k) * a / 2, (j - k) * a / 2)
        U = max(2.0, a + 1.7)
        src = (lambda aa, cc_: (lambda z: phi(z) + 0.5 * cc_ * (phi(z + aa) + phi(z - aa))))(a, c)
        M = moments(t, x, src, U=U, n=int(600 * U), kmax=2)
        direct = 0.25 * (M[0] * M[2] - M[1] ** 2)
        e = abs(direct - tot) / abs(direct)
        worst = max(worst, e)
        rows.append({"p": p, "c": c, "t": t, "x": x, "L0_control_direct": sig(direct.real, 10),
                     "L0_control_translated_weights": sig(tot.real, 10), "rel_err": err3(e)})
    record("N_float", "N7_controls_translated_weights", {"rows": rows, "max_rel_err": err3(worst)}, worst < 1e-9)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=None)
    args = ap.parse_args()
    part_e()
    part_n()
    with open(__file__, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    rec = {
        "title": "Rank-two automorphic lift: cusp formula, Newman time, two-coset identity, control test",
        "date": "2026-10-13",
        "prepared_for": "Edward Baker",
        "model": "Claude Opus 5.5 (claude-opus-5-5), Claude Cowork, effort max",
        "script_sha256": digest,
        "python": platform.python_version(),
        "status": "PASS" if not FAILURES else "FAIL",
        "failures": FAILURES,
        "results": RESULTS,
        "scope": "Part E exact rational; Part N double-precision quadrature, not interval-certified.",
    }
    text = json.dumps(rec, indent=1, sort_keys=True)
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(text + "\n")
    print(text)
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
