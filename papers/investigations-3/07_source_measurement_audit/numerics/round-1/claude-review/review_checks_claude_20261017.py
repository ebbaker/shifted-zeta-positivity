#!/usr/bin/env python3
"""Cross-model review checks for investigations-3 Project 07, round one.

17 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier claude-opus-5-5), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier. This program supports the round-one review
reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md.

Requires mpmath only (run with mpmath 1.4.1). Deterministic
apart from the runtime fields; writes one JSON record (--output).

Independence. Nothing is imported or copied from the Project 07 programs or
from the original Claude brainstorm solver. Methods differ where practical:
  * t = 0 mode jets by a closed form (upper incomplete gamma), theta jet at
    t = 0 from xi itself; t = 1/4 jets by Gauss-Legendre quadrature (the
    replay used tanh-sinh and Arb);
  * C and r_M from the 2 x 2 whitened jet matrix, r_M again from a KKT solve
    on R^6 (the replay used QR/SVD and a Gram identity);
  * endpoint polynomials by Leibniz/Hermite (the replay used one combined
    recurrence).
Status: floating-point diagnostics at 60 digits, except Sections G and H,
which use mpmath interval arithmetic (iv) for the displayed inequalities.
Section labels match the review.

  A  jets at the six replay observations, compared with the committed balls
  B  C, eta, r_M for the 24 conditioning combinations
  C  the alignment abscissa in each zero gap, where r_M = eta
  D  theta-tail coefficient feasibility at alignment abscissae
  P  the 32 prescribed-abscissa coefficient problems, classified by rank and
     planar Caratheodory (the replay used Farkas witnesses)
  E  the three-square control bracket (sign change of Phi'(0))
  F  Note 05 endpoint constants and a falsification test of the remainders
  G  Note 02 envelope constants in interval arithmetic
  H  explicit height above which a reflection-breaking perturbation has
     no real zeros (interval arithmetic), and one preregistered floating
     illustration at sixteen-digit recurrence size
"""
import argparse
import hashlib
import itertools
import json
import math
import platform
import time
from pathlib import Path

import mpmath as mp
from mpmath import iv

DPS = 60
mp.mp.dps = DPS
START = time.monotonic()


def s(x, d=15):
    """Short string of an mpf/mpc/float."""
    if isinstance(x, (mp.mpc, complex)):
        return [mp.nstr(mp.re(x), d), mp.nstr(mp.im(x), d)]
    return mp.nstr(x, d)


# ---------------------------------------------------------------------------
# Source modes and normalization
# ---------------------------------------------------------------------------

def lam(n):
    return mp.pi * n * n


def beta(n):
    return (4 * mp.pi * n * n - 1) * mp.exp(-mp.pi * n * n)


def phi(n, u):
    q = lam(n) * mp.exp(4 * u)
    return mp.exp(u - q) * (2 * q * q - 3 * q)


# P_m(q) with phi_n^{(m)}(u) = e^{u-q} P_m(q): P_{m+1} = (1-4q)P_m + 4q P_m'
def phi_polys(mmax):
    polys = [{2: 2, 1: -3}]          # dict power -> integer coefficient
    for _ in range(mmax):
        p = polys[-1]
        r = {}
        for k, c in p.items():
            r[k] = r.get(k, 0) + c            # (1)P
            r[k + 1] = r.get(k + 1, 0) - 4 * c  # (-4q)P
            if k:
                r[k] = r.get(k, 0) + 4 * k * c  # 4q P'
        polys.append({k: c for k, c in r.items() if c})
    return polys


PHI_POLYS = phi_polys(9)


def phi_deriv0(n, m):
    """phi_n^{(m)}(0) = e^{-lambda} P_m(lambda)."""
    a = lam(n)
    return mp.exp(-a) * mp.fsum(c * a ** k for k, c in PHI_POLYS[m].items())


# ---------------------------------------------------------------------------
# Jets.  t = 0: closed forms.  General t: Gauss-Legendre quadrature.
# ---------------------------------------------------------------------------

def _G(a, s_):
    # int_1^inf w^{s-1} e^{-a w} dw = a^{-s} Gamma(s, a)
    return a ** (-s_) * mp.gammainc(s_, a)


def mode_F0(n, x):
    a = lam(n)
    s1 = mp.mpf(9) / 4 + 1j * x / 4
    s2 = mp.mpf(5) / 4 + 1j * x / 4
    return (2 * a * a * _G(a, s1) - 3 * a * _G(a, s2)) / 4


def mode_jet0(n, x, kmax=1):
    """[H_n, H_n', ..., H_n^{(kmax)}](0, x) from the closed form."""
    out = [mp.re(mode_F0(n, x))]
    for k in range(1, kmax + 1):
        out.append(mp.re(mp.diff(lambda y: mode_F0(n, y), x, k)))
    return out


def xi(s_):
    return s_ * (s_ - 1) / 2 * mp.pi ** (-s_ / 2) * mp.gamma(s_ / 2) * mp.zeta(s_)


def theta_jet0(x, kmax=1):
    F = lambda y: xi((1 + 1j * y) / 2) / 8
    out = [mp.re(F(x))]
    for k in range(1, kmax + 1):
        out.append(mp.re(mp.diff(F, x, k)))
    return out


V_PTS = ([mp.mpf(j) / 2 for j in range(0, 40)] + [mp.mpf(j) for j in range(20, 60, 2)]
         + [mp.mpf(j) for j in range(60, 201, 10)])


def mode_jet_quad(n, t, x, kmax=1):
    """int_0^inf e^{t u^2} phi_n(u) d^k/dx^k cos(xu) du, k = 0..kmax.

    Substitute w = e^{4u} = 1 + v/lambda_n, so that the integrand is
    e^{-lambda_n} e^{-v} times a slowly varying factor; Gauss-Legendre on
    fixed panels of [0, 200].  The omitted v > 200 tail is below e^{-190}
    times the integrand scale, negligible at 60 digits for these heights.
    """
    a = lam(n)
    out = []
    for k in range(kmax + 1):
        def f(v, k=k):
            w = 1 + v / a
            lw = mp.log(w)
            u = lw / 4
            amp = mp.exp(-v + t * lw * lw / 16) * w ** (mp.mpf(1) / 4) * (2 * a * a * w * w - 3 * a * w) / (4 * a * w)
            return amp * u ** k * mp.cos(x * u + k * mp.pi / 2)
        out.append(mp.exp(-a) * mp.quad(f, V_PTS, method="gauss-legendre"))
    return out


THETA_MODES = 7          # theta jet from modes 1..7; mode 8 is below e^{-64 pi}


_cache = {}


def jets(t, x, kmax=1):
    """Return (B, h): B[k][n-1] for n = 1..6 and h[k], k = 0..kmax."""
    key = (mp.nstr(t, 30), mp.nstr(x, 40), kmax)
    if key in _cache:
        return _cache[key]
    if t == 0:
        cols = [mode_jet0(n, x, kmax) for n in range(1, 7)]
        hh = theta_jet0(x, kmax)
    else:
        cols = [mode_jet_quad(n, t, x, kmax) for n in range(1, THETA_MODES + 1)]
        hh = [mp.fsum(c[k] for c in cols) for k in range(kmax + 1)]
        cols = cols[:6]
    B = [[cols[n][k] for n in range(6)] for k in range(kmax + 1)]
    _cache[key] = (B, hh)
    return B, hh


# ---------------------------------------------------------------------------
# Spaces, designs, conditioning
# ---------------------------------------------------------------------------

def nullspace_basis(rows, dim):
    """Orthonormal basis (columns) of {d in R^dim : rows d = 0} via QR of rows^T."""
    K = mp.matrix(rows).T                    # dim x c
    Q, R = mp.qr(K, mode="full")
    c = len(rows)
    return mp.matrix([[Q[i, j] for j in range(c, dim)] for i in range(dim)])


def space(N, anchored):
    rows = [[beta(n) for n in range(1, N + 1)]]
    if anchored:
        rows.append([1] + [0] * (N - 1))
    return nullspace_basis(rows, N)


def design(name):
    if name == "recurrence":
        return mp.matrix([[(1 if j == k - 1 else 0) - (2 if j == k else 0) + (1 if j == k + 1 else 0)
                           for j in range(1, 7)] for k in range(1, 8)])
    return mp.matrix([[phi(n, mp.mpf(j) / 20) - phi(n, -mp.mpf(j) / 20) for n in range(1, 7)]
                      for j in range(1, 13)])


DESIGNS = {name: design(name) for name in ("recurrence", "reflection")}
SPACES6 = {anchor: space(6, anchor) for anchor in (False, True)}


def whitened(Bjet, Z, M):
    """X = B Z, G = (MZ)^T (MZ), S = X G^{-1} X^T (2 x 2)."""
    X = mp.matrix(Bjet) * Z
    MZ = M * Z
    G = MZ.T * MZ
    Y = mp.matrix(Z.cols, 2)
    for j in range(2):
        col = mp.lu_solve(G, X[j, :].T)
        for i in range(Z.cols):
            Y[i, j] = col[i]
    S = X * Y
    S = (S + S.T) / 2
    return X, G, Y, S


def eig2(S):
    a, b, c = S[0, 0], S[0, 1], S[1, 1]
    disc = mp.sqrt((a - c) ** 2 / 4 + b * b)
    l1, l2 = (a + c) / 2 + disc, (a + c) / 2 - disc
    # top eigenvector (l1 - c, b): (S - l1) v = 0 because (a - l1)(c - l1) = b^2;
    # its first component l1 - c >= 0.
    v = mp.matrix([l1 - c, b])
    nv = mp.sqrt(v[0] ** 2 + v[1] ** 2)
    if nv == 0:
        v = mp.matrix([0, 1])
    else:
        v = v / nv
    return l1, l2, v


def conditioning(t, x, Z, M, kmax=1):
    B, hh = jets(t, x, kmax)
    h = mp.matrix([hh[0], hh[1]])
    X, G, Y, S = whitened([B[0], B[1]], Z, M)
    l1, l2, u1 = eig2(S)
    C = mp.sqrt(l1)
    hn = mp.sqrt(h[0] ** 2 + h[1] ** 2)
    eta = hn / C
    Sinv_h = mp.lu_solve(S, h)
    rM = mp.sqrt((h.T * Sinv_h)[0, 0])
    # measurement minimizer delta* = -Z G^{-1} X^T S^{-1} h
    delta = -(Z * (Y * Sinv_h))
    align = (h[0] * (-u1[1]) + h[1] * u1[0]) / hn      # sin(angle(h) - angle(u1))
    return {"C": C, "eta": eta, "rM": rM, "delta": delta, "align": align,
            "h": h, "u1": u1, "l1": l1, "l2": l2, "B": B, "hh": hh}


def kkt_rM(t, x, M, anchored):
    """Independent r_M: min ||M d|| s.t. B d = -h, beta.d = 0 (, d_1 = 0) on R^6."""
    B, hh = jets(t, x, 1)
    rows = [B[0], B[1], [beta(n) for n in range(1, 7)]]
    rhs = [-hh[0], -hh[1], 0]
    if anchored:
        rows.append([1, 0, 0, 0, 0, 0])
        rhs.append(0)
    # scale constraint rows to unit norm for conditioning
    scaled_rows, scaled_rhs = [], []
    for r, b in zip(rows, rhs):
        nr = mp.sqrt(mp.fsum(v * v for v in r))
        scaled_rows.append([v / nr for v in r])
        scaled_rhs.append(b / nr)
    K = mp.matrix(scaled_rows)
    H = M.T * M
    c = K.rows
    KKT = mp.zeros(6 + c, 6 + c)
    for i in range(6):
        for j in range(6):
            KKT[i, j] = H[i, j]
    for i in range(c):
        for j in range(6):
            KKT[6 + i, j] = K[i, j]
            KKT[j, 6 + i] = K[i, j]
    rhsv = mp.matrix([0] * 6 + scaled_rhs)
    sol = mp.lu_solve(KKT, rhsv)
    d = mp.matrix([sol[i] for i in range(6)])
    Md = M * d
    return mp.sqrt(mp.fsum(v * v for v in Md)), d


# ---------------------------------------------------------------------------
# Root finding by bisection (Illinois) on a sign change
# ---------------------------------------------------------------------------

def bracket_root(f, a, b, tol=mp.mpf(10) ** -30, maxit=200):
    fa, fb = f(a), f(b)
    if fa == 0:
        return a
    if fb == 0:
        return b
    if (fa > 0) == (fb > 0):
        raise ValueError("no sign change")
    side = 0
    for _ in range(maxit):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        if abs(b - a) < tol or fc == 0:
            return c
        if (fc > 0) == (fb > 0):
            b, fb = c, fc
            if side == -1:
                fa /= 2
            side = -1
        else:
            a, fa = c, fc
            if side == 1:
                fb /= 2
            side = 1
    return (a + b) / 2


def scan_sign_changes(f, a, b, steps):
    xs = [a + (b - a) * j / steps for j in range(steps + 1)]
    vals = [f(x) for x in xs]
    out = []
    for j in range(steps):
        if vals[j] == 0 or (vals[j] > 0) != (vals[j + 1] > 0):
            out.append((xs[j], xs[j + 1]))
    return out


def theta_zero(t, guess, width=mp.mpf("0.6")):
    f = lambda x: jets(t, x, 1)[1][0]
    return bracket_root(f, guess - width, guess + width, tol=mp.mpf(10) ** -25)


# ---------------------------------------------------------------------------
# Section A: jets at the six observations
# ---------------------------------------------------------------------------

OBS = [(mp.mpf(0), mp.mpf(30)), (mp.mpf(0), mp.mpf("44.1303")), (mp.mpf(1) / 4, mp.mpf("44.1303")),
       (mp.mpf(0), mp.mpf(60)), (mp.mpf(0), mp.mpf(70)), (mp.mpf(0), mp.mpf(85))]
OBS_ID = ["t0_x30", "t0_x44.1303", "t0.25_x44.1303", "t0_x60", "t0_x70", "t0_x85"]


def ball_mid_rad(sv):
    sv = sv.strip()[1:-1]
    if "+/-" in sv:
        m, r = sv.split("+/-")
        return mp.mpf(m.strip()), mp.mpf(r.strip())
    return mp.mpf(sv), mp.mpf(0)


def section_A(committed_eval):
    out = []
    E = json.loads(Path(committed_eval).read_text()) if committed_eval else None
    for (t, x), oid in zip(OBS, OBS_ID):
        B, hh = jets(t, x, 1)
        row = {"id": oid, "method": "closed form (xi, incomplete gamma)" if t == 0 else "Gauss-Legendre after e^{4u} = 1 + v/lambda, 74 panels on [0, 200]",
               "h": [s(hh[0], 20), s(hh[1], 20)]}
        if t != 0:
            # quadrature cross-check of the closed form at t = 0 for the same x
            Bq = [mode_jet_quad(n, mp.mpf(0), x, 1) for n in range(1, 7)]
            B0 = [mode_jet0(n, x, 1) for n in range(1, 7)]
            row["quadrature_vs_closed_form_t0_max_rel"] = s(max(abs(Bq[n][k] / B0[n][k] - 1)
                                                                for n in range(6) for k in range(2)), 5)
        if E:
            case = next(c for c in E["cases"] if c["id"] == oid)
            worst_h, worst_B, inside = mp.mpf(0), mp.mpf(0), True
            for k in range(2):
                m, r = ball_mid_rad(case["h"][k])
                worst_h = max(worst_h, abs(hh[k] / m - 1))
                inside = inside and abs(hh[k] - m) <= r + abs(m) * mp.mpf(10) ** -45
                for n in range(6):
                    mb, rb = ball_mid_rad(case["B"][k][n])
                    worst_B = max(worst_B, abs(B[k][n] / mb - 1))
            row["max_rel_diff_h_vs_committed"] = s(worst_h, 5)
            row["max_rel_diff_B_vs_committed"] = s(worst_B, 5)
            row["h_inside_committed_ball_up_to_1e-45_rel"] = bool(inside)
        out.append(row)
    return out


# ---------------------------------------------------------------------------
# Section B: conditioning at the six observations
# ---------------------------------------------------------------------------

def section_B(committed_meas):
    Mc = json.loads(Path(committed_meas).read_text()) if committed_meas else None
    rows = []
    for (t, x), oid in zip(OBS, OBS_ID):
        for anchor in (False, True):
            for name, M in DESIGNS.items():
                r = conditioning(t, x, SPACES6[anchor], M)
                rk, _ = kkt_rM(t, x, M, anchor)
                rec = {"id": oid, "anchor": anchor, "design": name,
                       "C": s(r["C"], 12), "eta": s(r["eta"], 12), "r_M": s(r["rM"], 12),
                       "r_M_over_eta": s(r["rM"] / r["eta"], 8),
                       "kkt_r_M_rel_diff": s(abs(rk / r["rM"] - 1), 3),
                       "minimizer_min_coefficient": s(min(1 + r["delta"][i] for i in range(6)), 8)}
                if Mc:
                    c = next(z for z in Mc["rows"] if z["id"] == oid and z["anchor"] == anchor and z["design"] == name)
                    for key, ck in (("C", "C"), ("eta", "eta"), ("r_M", "actual_unconstrained_measurement_distance")):
                        m, _ = ball_mid_rad(c[ck])
                        rec[key + "_rel_diff_vs_committed"] = s(abs((r["C"] if key == "C" else r["eta"] if key == "eta" else r["rM"]) / m - 1), 3)
                rows.append(rec)
    return rows


# ---------------------------------------------------------------------------
# Section C: alignment abscissae
# ---------------------------------------------------------------------------

def gaps():
    """Zero gaps of H_theta(t, .) containing the six observations."""
    g0 = [2 * mp.zetazero(k).imag for k in range(1, 10)]
    out = []
    for (t, x), oid in zip(OBS, OBS_ID):
        if t == 0:
            zs = g0
        else:
            zs = [theta_zero(t, z) for z in g0[:4]]
        lo = max(z for z in zs if z < x)
        hi = min(z for z in zs if z > x)
        out.append((t, x, oid, lo, hi))
    return out


def alignment_point(t, lo, hi, Z, M, scan=24):
    eps = (hi - lo) * mp.mpf(10) ** -6
    f = lambda y: conditioning(t, y, Z, M)["align"]
    # the sign of `align` changes where h passes through +/- u1 (r_M = eta) and,
    # with the opposite crossing, through the zeros themselves; choose the
    # sign change at which r_M/eta is smallest.
    brackets = scan_sign_changes(f, lo + eps, hi - eps, scan)
    best = None
    for a, b in brackets:
        xr = bracket_root(f, a, b)
        r = conditioning(t, xr, Z, M)
        ratio = r["rM"] / r["eta"]
        if best is None or ratio < best[1]:
            best = (xr, ratio, r)
    return best


def frozen_curvature(t, x, delta6):
    B, hh = jets(t, x, 2)
    return hh[2] + mp.fsum(B[2][n] * delta6[n] for n in range(6))


def section_C(gap_list):
    rows = []
    for t, x, oid, lo, hi in gap_list:
        for anchor in (False, True):
            for name, M in DESIGNS.items():
                listed = conditioning(t, x, SPACES6[anchor], M)
                xs, ratio, r = alignment_point(t, lo, hi, SPACES6[anchor], M)
                d = r["delta"]
                mincoef = min(1 + d[i] for i in range(6))
                K = frozen_curvature(t, xs, [d[i] for i in range(6)])
                B, hh = jets(t, xs, 1)
                res = [hh[k] + mp.fsum(B[k][n] * d[n] for n in range(6)) for k in range(2)]
                rows.append({"listed_point": oid, "zero_gap": [s(lo, 10), s(hi, 10)],
                             "anchor": anchor, "design": name, "x_star": s(xs, 15),
                             "eta_at_x_star": s(r["eta"], 10), "r_M_at_x_star": s(r["rM"], 10),
                             "r_M_over_eta_at_x_star_minus_1": s(ratio - 1, 3),
                             "eta_at_listed_point": s(listed["eta"], 10),
                             "r_M_at_listed_point": s(listed["rM"], 10),
                             "eta_star_over_eta_listed": s(r["eta"] / listed["eta"], 6),
                             "minimizer_min_coefficient": s(mincoef, 10),
                             "minimizer_sup_change": s(max(abs(d[i]) for i in range(6)), 6),
                             "double_jet_residual_relative": s(max(abs(res[k]) for k in range(2)) /
                                                               mp.sqrt(hh[0] ** 2 + hh[1] ** 2), 3),
                             "frozen_H_xx": s(K, 8)})
    return rows


# ---------------------------------------------------------------------------
# Section D: theta-tail feasibility at the Euclidean alignment abscissa
# ---------------------------------------------------------------------------

def theta_tail_problem(t, x, N, anchored):
    """Return (Z, X, h): V_N basis (N x d), jets of basis, theta jet."""
    B, hh = jets(t, x, 1)
    Z = space(N, anchored)
    X = mp.matrix([[mp.fsum(B[k][n] * Z[n, j] for n in range(N)) for j in range(Z.cols)] for k in range(2)])
    return Z, X, mp.matrix([hh[0], hh[1]])


def euclid_solution(t, x, N, anchored):
    Z, X, h = theta_tail_problem(t, x, N, anchored)
    d = Z.cols
    if d == 1:
        v = mp.matrix([X[0, 0], X[1, 0]])
        cross = (h[0] * v[1] - h[1] * v[0]) / (mp.sqrt(h[0] ** 2 + h[1] ** 2) * mp.sqrt(v[0] ** 2 + v[1] ** 2))
        eps = -(h[0] * v[0] + h[1] * v[1]) / (v[0] ** 2 + v[1] ** 2)
        return cross, Z * mp.matrix([eps])
    S = X * X.T
    l1, l2, u1 = eig2(S)
    hn = mp.sqrt(h[0] ** 2 + h[1] ** 2)
    align = (h[0] * (-u1[1]) + h[1] * u1[0]) / hn
    y = -(X.T * mp.lu_solve(S, h))
    return align, Z * y


def section_D(gap_list):
    wanted = {"t0.25_x44.1303", "t0_x60"}
    rows = []
    for t, x, oid, lo, hi in gap_list:
        if oid not in wanted:
            continue
        for N in (2, 3, 4, 6):
            for anchored in (False, True):
                if N == 2 and anchored:
                    rows.append({"listed_point": oid, "N": N, "anchor": anchored,
                                 "result": "tangent space {0}: no perturbation, infeasible at every abscissa"})
                    continue
                eps_ = (hi - lo) * mp.mpf(10) ** -6
                f = lambda y: euclid_solution(t, y, N, anchored)[0]
                brs = scan_sign_changes(f, lo + eps_, hi - eps_, 24)
                cands = []
                for a, b in brs:
                    xr = bracket_root(f, a, b)
                    _, dvec = euclid_solution(t, xr, N, anchored)
                    cands.append((max(abs(dvec[i]) for i in range(N)), xr, dvec))
                cands.sort(key=lambda z: z[0])
                sup, xr, dvec = cands[0]
                B, hh = jets(t, xr, 1)
                res = [hh[k] + mp.fsum(B[k][n] * dvec[n] for n in range(N)) for k in range(2)]
                rows.append({"listed_point": oid, "N": N, "anchor": anchored, "x_star": s(xr, 15),
                             "coefficients_a_first_N": [s(1 + dvec[i], 12) for i in range(N)],
                             "min_coefficient": s(min(1 + dvec[i] for i in range(N)), 10),
                             "sup_change": s(sup, 6),
                             "normalization_residual": s(mp.fsum(beta(n + 1) * dvec[n] for n in range(N)), 3),
                             "double_jet_residual_relative": s(max(abs(res[k]) for k in range(2)) /
                                                               mp.sqrt(hh[0] ** 2 + hh[1] ** 2), 3),
                             "frozen_H_xx": s(frozen_curvature(t, xr, [dvec[i] for i in range(N)] + [0] * (6 - N)), 8),
                             "positive": bool(min(1 + dvec[i] for i in range(N)) > 0)})
    return rows


# ---------------------------------------------------------------------------
# Section P: the 32 prescribed-abscissa problems
# ---------------------------------------------------------------------------

def _det2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def _in_triangle(q, a, b, c):
    d1 = _det2([b[0] - a[0], b[1] - a[1]], [q[0] - a[0], q[1] - a[1]])
    d2 = _det2([c[0] - b[0], c[1] - b[1]], [q[0] - b[0], q[1] - b[1]])
    d3 = _det2([a[0] - c[0], a[1] - c[1]], [q[0] - c[0], q[1] - c[1]])
    area = abs(_det2([b[0] - a[0], b[1] - a[1]], [c[0] - a[0], c[1] - a[1]]))
    if area == 0:
        return False, mp.mpf(0)
    inside = (d1 >= 0 and d2 >= 0 and d3 >= 0) or (d1 <= 0 and d2 <= 0 and d3 <= 0)
    return inside, min(abs(d1), abs(d2), abs(d3)) / area


def _scaled_singular_values(Mx):
    rows = []
    for i in range(Mx.rows):
        nr = mp.sqrt(mp.fsum(Mx[i, j] ** 2 for j in range(Mx.cols)))
        rows.append([Mx[i, j] / nr for j in range(Mx.cols)])
    sv = mp.svd_r(mp.matrix(rows), compute_uv=False)
    return [sv[i] for i in range(len(sv))]


def classify_prescribed(t, x, N, tail, anchor):
    B, hh = jets(t, x, 1)
    bt = [beta(n) for n in range(1, 7)]
    J = list(range(1 if anchor else 0, N))
    if tail == "theta":
        tailjet = [hh[k] - mp.fsum(B[k][:N]) for k in range(2)]
        tailbeta = mp.mpf(1) / 2 - mp.fsum(bt[:N])
    else:
        tailjet, tailbeta = [mp.mpf(0), mp.mpf(0)], mp.mpf(0)
    r = [-tailjet[k] - (B[k][0] if anchor else 0) for k in range(2)]
    m = mp.mpf(1) / 2 - tailbeta - (bt[0] if anchor else 0)
    E = mp.matrix([[B[0][n] for n in J], [B[1][n] for n in J], [bt[n] for n in J]])
    aug = mp.matrix([[B[0][n] for n in J] + [r[0]], [B[1][n] for n in J] + [r[1]], [bt[n] for n in J] + [m]])
    svE, svA = _scaled_singular_values(E), _scaled_singular_values(aug)
    tol = mp.mpf(10) ** -40
    eq_feasible = sum(1 for v in svE if v > tol) == sum(1 for v in svA if v > tol)
    p = [[B[0][n] / bt[n], B[1][n] / bt[n]] for n in J]
    q = [r[0] / m, r[1] / m]
    inside, margin = False, mp.mpf(0)
    if len(J) >= 3:
        for a3, b3, c3 in itertools.combinations(p, 3):
            ok, mg = _in_triangle(q, a3, b3, c3)
            if ok:
                inside, margin = True, max(margin, mg)
    elif len(J) == 2 and eq_feasible:
        d = [p[1][0] - p[0][0], p[1][1] - p[0][1]]
        s_ = ((q[0] - p[0][0]) * d[0] + (q[1] - p[0][1]) * d[1]) / (d[0] ** 2 + d[1] ** 2)
        inside = 0 <= s_ <= 1
    return {"N": N, "tail": tail, "anchor": anchor, "free_nodes": [n + 1 for n in J],
            "min_scaled_singular_value_augmented": s(min(svA), 4),
            "equality_feasible": bool(eq_feasible), "nonnegative_feasible": bool(inside and eq_feasible),
            "triangle_margin": s(margin, 4) if inside else None}


def section_P(committed_feas):
    committed = json.loads(Path(committed_feas).read_text()) if committed_feas else None
    rows, agree = [], 0
    for (t, x, pid) in ((mp.mpf(1) / 4, mp.mpf("44.1303"), "t025_x44_1303"), (mp.mpf(0), mp.mpf(60), "t0_x60")):
        for N in (2, 3, 4, 6):
            for tail in ("theta", "zero"):
                for anchor in (False, True):
                    c = classify_prescribed(t, x, N, tail, anchor)
                    c["point"] = pid
                    if committed:
                        cc = next(z for z in committed["cases"] if z["point_id"] == pid and z["N"] == N
                                  and z["tail"] == tail and z["anchor_a1"] == anchor)
                        mine_eq = "certified_feasible" if c["equality_feasible"] else "certified_infeasible"
                        mine_pos = ("certified_feasible_and_euclidean_optimal" if c["nonnegative_feasible"]
                                    else "certified_infeasible")
                        c["committed"] = [cc["equality_status"], cc["positive_status"]]
                        c["agrees_with_committed"] = (mine_eq == cc["equality_status"] and mine_pos == cc["positive_status"])
                        agree += c["agrees_with_committed"]
                    rows.append(c)
    return {"rows": rows, "agreements_with_committed": agree, "cases": len(rows)}


# ---------------------------------------------------------------------------
# Section E: three-square bracket
# ---------------------------------------------------------------------------

def three_node_zero_tail(t, x):
    B, hh = jets(t, x, 1)
    E = mp.matrix([[B[0][0], B[0][1], B[0][2]], [B[1][0], B[1][1], B[1][2]], [beta(1), beta(2), beta(3)]])
    a = mp.lu_solve(E, mp.matrix([0, 0, mp.mpf(1) / 2]))
    d1 = mp.fsum(a[n] * phi_deriv0(n + 1, 1) for n in range(3))
    d3 = mp.fsum(a[n] * phi_deriv0(n + 1, 3) for n in range(3))
    return a, d1, d3


def section_E():
    t = mp.mpf(1) / 4
    out = {}
    for xs in ("44.1303", "44.1304"):
        a, d1, d3 = three_node_zero_tail(t, mp.mpf(xs))
        out[xs] = {"a": [s(a[i], 12) for i in range(3)], "Phi_prime_0": s(d1, 10), "Phi_triple_prime_0": s(d3, 10)}
    root = bracket_root(lambda y: three_node_zero_tail(t, y)[1], mp.mpf("44.1303"), mp.mpf("44.1304"),
                        tol=mp.mpf(10) ** -20)
    a, d1, d3 = three_node_zero_tail(t, root)
    scale = a[0]                     # raw control has a_1 = 1
    out["root_of_Phi_prime_0"] = {"x": s(root, 15), "a_normalized": [s(a[i], 12) for i in range(3)],
                                  "a_raw_rescaled_to_a1_eq_1": [s(a[i] / scale, 10) for i in range(3)],
                                  "normalization_factor_c": s(scale, 12), "Phi_triple_prime_0_raw": s(d3 / scale, 8),
                                  "control_table_22_05_01": "a_2 in (0.87916, 0.87919), a_3 in (57740, 57745), c near 1.0000347152, Phi''' in (-40.00, -39.98)"}
    return out


# ---------------------------------------------------------------------------
# Section F: Note 05 constants
# ---------------------------------------------------------------------------

T05 = mp.mpf(1) / 4


def hermite_polys(kmax):
    """(e^{t u^2})^{(j)} = e^{t u^2} He_j(u, t); dict (i, l) -> int for u^i t^l."""
    polys = [{(0, 0): 1}]
    for _ in range(kmax):
        p = polys[-1]
        r = {}
        for (i, l), c in p.items():
            if i:
                r[(i - 1, l)] = r.get((i - 1, l), 0) + i * c
            r[(i + 1, l + 1)] = r.get((i + 1, l + 1), 0) + 2 * c
        polys.append({k: c for k, c in r.items() if c})
    return polys


HE = hermite_polys(9)


def g_poly(k):
    """g^{(k)} = e^{t u^2 + u - q} * sum (i,j,l)->c u^i q^j t^l (Leibniz)."""
    r = {}
    for jj in range(k + 1):
        binom = math.comb(k, jj)
        for (i, l), c1 in HE[jj].items():
            for qk, c2 in PHI_POLYS[k - jj].items():
                key = (i, qk, l)
                r[key] = r.get(key, 0) + binom * c1 * c2
    return {key: c for key, c in r.items() if c}


def ug_poly(k):
    """(u g)^{(k)} = u g^{(k)} + k g^{(k-1)}."""
    r = {}
    for (i, j, l), c in g_poly(k).items():
        r[(i + 1, j, l)] = r.get((i + 1, j, l), 0) + c
    if k:
        for (i, j, l), c in g_poly(k - 1).items():
            r[(i, j, l)] = r.get((i, j, l), 0) + k * c
    return {key: c for key, c in r.items() if c}


def monomial_majorant(n, i, j):
    a = lam(n)
    c = 1 - T05 / (8 * a)
    sh = mp.mpf(j) + mp.mpf(1) / 2
    return mp.factorial(i) / (4 * mp.sqrt(a)) * c ** (-sh) * mp.gammainc(sh, c * a)


def l1_majorant(direction, poly):
    tot = mp.mpf(0)
    for node, dn in enumerate(direction, start=1):
        if dn == 0:
            continue
        for (i, j, l), c in poly.items():
            tot += abs(dn) * abs(c) * T05 ** l * monomial_majorant(node, i, j)
    return tot


def endpoint_value(direction, k, t):
    """g^{(k)}(0) for the direction: Leibniz with (e^{tu^2})^{(2i)}(0) = (2i)!/i! t^i."""
    tot = mp.mpf(0)
    for node, dn in enumerate(direction, start=1):
        for i in range(k // 2 + 1):
            tot += dn * math.comb(k, 2 * i) * mp.factorial(2 * i) / mp.factorial(i) * t ** i * phi_deriv0(node, k - 2 * i)
    return tot


def endpoint_coeff_sum(direction, k):
    """Sum over powers of t of |coefficient| T^l (the Note 05 endpoint sup majorant)."""
    tot = mp.mpf(0)
    for i in range(k // 2 + 1):
        ci = mp.fsum(dn * math.comb(k, 2 * i) * mp.factorial(2 * i) / mp.factorial(i) * phi_deriv0(node, k - 2 * i)
                     for node, dn in enumerate(direction, start=1))
        tot += abs(ci) * T05 ** i
    return tot


def directions05():
    b1, b2, b3 = beta(1), beta(2), beta(3)
    v2 = [-b2 / b1, mp.mpf(1), mp.mpf(0)]
    v3 = [-b3 / b1, mp.mpf(0), mp.mpf(1)]
    l0 = lambda v: mp.fsum(v[n] * phi_deriv0(n + 1, 1) for n in range(3))
    rho = l0(v3) / l0(v2)
    A = v2
    Bd = [v3[i] - rho * v2[i] for i in range(3)]
    return A, Bd, rho


def jet_dir(direction, t, x, kmax=1):
    B, hh = jets(t, x, kmax)
    return [mp.fsum(direction[n] * B[k][n] for n in range(3)) for k in range(kmax + 1)]


def section_F(committed_onset):
    A, Bd, rho = directions05()
    a = -endpoint_value(A, 1, 0)
    b = endpoint_value(Bd, 3, 0)
    out = {"A": [s(v, 15) for v in A], "B": [s(v, 15) for v in Bd], "rho": s(rho, 15),
           "a": s(a, 15), "b": s(b, 15), "f_B_prime_0": s(endpoint_value(Bd, 1, 0), 5)}
    endA = endpoint_coeff_sum(A, 3)
    endB = endpoint_coeff_sum(Bd, 5)
    gA, ugA = l1_majorant(A, g_poly(4)), l1_majorant(A, ug_poly(5))
    gB, ugB = l1_majorant(Bd, g_poly(6)), l1_majorant(Bd, ug_poly(7))
    EA, FA = endA + gA, 4 * endA + ugA
    EB, FB = endB + gB, 6 * endB + ugB
    p, r = 2, 4
    L = (r - p) * abs(a * b)
    K2 = abs(a) * FB + r * abs(b) * EA + abs(b) * FA + p * abs(a) * EB
    K4 = EA * FB + EB * FA
    XD = mp.sqrt((K2 + mp.sqrt(K2 * K2 + 2 * L * K4)) / L)
    KD = mp.sqrt((abs(a) + EA) ** 2 + (p * abs(a) + FA) ** 2 + (abs(b) + EB) ** 2 + (r * abs(b) + FB) ** 2)
    Pn = max(mp.sqrt(A[i] ** 2 + Bd[i] ** 2) for i in range(3))
    pref = 12 * KD * Pn / (5 * L)
    X = 3915
    dbound = pref * mp.mpf(X) ** 5 * mp.exp(-mp.pi * X / 16)
    out["constants"] = {"E_A": s(EA, 14), "F_A": s(FA, 14), "E_B": s(EB, 14), "F_B": s(FB, 14),
                        "L": s(L, 14), "K2": s(K2, 14), "K4": s(K4, 14), "X_D": s(XD, 14),
                        "K_D": s(KD, 14), "P_2_to_inf": s(Pn, 14), "prefactor": s(pref, 14),
                        "delta_bound_at_3915": s(dbound, 10),
                        "relative_det_remainder_at_3915": s(K2 / (L * X ** 2) + K4 / (L * mp.mpf(X) ** 4), 12)}
    if committed_onset:
        Cj = json.loads(Path(committed_onset).read_text())
        cmp_ = {}
        for key, path in (("E_A", ("remainder_constants", "E_A")), ("F_A", ("remainder_constants", "F_A")),
                          ("E_B", ("remainder_constants", "E_B")), ("F_B", ("remainder_constants", "F_B")),
                          ("L", ("determinant", "L_lower")), ("K2", ("determinant", "K2_upper")),
                          ("K4", ("determinant", "K4_upper")), ("X_D", ("determinant", "X_D_upper")),
                          ("K_D", ("positivity", "K_D_upper")), ("prefactor", ("positivity", "prefactor_upper"))):
            m, _ = ball_mid_rad(Cj[path[0]][path[1]])
            mine = {"E_A": EA, "F_A": FA, "E_B": EB, "F_B": FB, "L": L, "K2": K2, "K4": K4,
                    "X_D": XD, "K_D": KD, "prefactor": pref}[key]
            cmp_[key] = s(abs(mine / m - 1), 3)
        out["relative_difference_vs_committed_record"] = cmp_
    # falsification test of the four remainder bounds and the determinant bound
    tests = []
    for t in (mp.mpf(0), T05):
        for x in (5, 10, 20, 40, 80):
            x = mp.mpf(x)
            HA = jet_dir(A, t, x)
            HB = jet_dir(Bd, t, x)
            rA0 = abs(HA[0] - a * x ** -2) / (EA * x ** -4)
            rA1 = abs(HA[1] + 2 * a * x ** -3) / (FA * x ** -5)
            rB0 = abs(HB[0] - b * x ** -4) / (EB * x ** -6)
            rB1 = abs(HB[1] + 4 * b * x ** -5) / (FB * x ** -7)
            det = HA[0] * HB[1] - HA[1] * HB[0]
            rD = abs(det - (p - r) * a * b * x ** -7) / (K2 * x ** -9 + K4 * x ** -11)
            tests.append({"t": s(t, 4), "x": s(x, 4),
                          "ratio_to_bound": {"H_A": s(rA0, 4), "H_A_x": s(rA1, 4), "H_B": s(rB0, 4),
                                             "H_B_x": s(rB1, 4), "det": s(rD, 4)},
                          "all_below_one": bool(max(rA0, rA1, rB0, rB1, rD) < 1)})
    out["remainder_falsification_tests"] = tests
    # sampled true L1 norms versus majorants (t = 0 and 1/4)
    def l1_true(direction, poly, t):
        def g(u):
            tot = mp.mpf(0)
            for node, dn in enumerate(direction, start=1):
                q = lam(node) * mp.exp(4 * u)
                pe = mp.fsum(c * u ** i * q ** j * t ** l for (i, j, l), c in poly.items())
                tot += dn * mp.exp(t * u * u + u - q) * pe
            return abs(tot)
        with mp.workdps(30):
            pts = [mp.mpf(13) / 10 * j / 130 for j in range(131)]
            return mp.quad(g, pts, method="gauss-legendre")
    samp = {}
    for label, direction, poly, maj in (("A_g4", A, g_poly(4), gA), ("A_ug5", A, ug_poly(5), ugA),
                                         ("B_g6", Bd, g_poly(6), gB), ("B_ug7", Bd, ug_poly(7), ugB)):
        samp[label] = {"majorant": s(maj, 10),
                       "true_L1_t0": s(l1_true(direction, poly, mp.mpf(0)), 10),
                       "true_L1_t_quarter": s(l1_true(direction, poly, T05), 10)}
    out["sampled_true_L1_norms"] = samp
    return out, (a, EA)


# ---------------------------------------------------------------------------
# Section G: Note 02 envelope constants in interval arithmetic
# ---------------------------------------------------------------------------

def section_G():
    iv.dps = 50
    pi = iv.pi
    y = pi / 16
    T = iv.mpf(1) / 4
    c = iv.cos(4 * y)
    kappa = 8 * c * pi - T
    l9 = 4 * c * pi - 9
    l5 = 4 * c * pi - 5
    assert kappa.a > 0 and l9.b < 0 and l5.a > 0
    J09 = iv.sqrt(pi / kappa) * iv.exp(l9 ** 2 / (4 * kappa))
    J19 = (1 - l9 * J09) / (2 * kappa)
    J05 = iv.sqrt(pi / kappa) / 2
    J15 = 1 / (2 * kappa)
    a2 = 4 * pi
    qa = iv.mpf(9) / 4 * iv.exp(-5 * c * pi)
    q0 = iv.exp(-5 * c * pi)
    assert qa.b < 1 and (2 * c * a2).a > 9
    Sa = a2 * iv.exp(-c * a2) / (1 - qa)
    S0 = iv.exp(-c * a2) / (1 - q0)
    KHt = Sa / c + 3 * S0 / (2 * c)
    KXt = (1 / (2 * c * c) + 3 / (4 * c * c * a2)) * S0 + y * KHt
    KH = iv.exp(-c * pi) * (2 * pi * pi * J09 + 3 * pi * J05) + KHt
    KX = iv.exp(-c * pi) * (2 * pi * pi * (J19 + y * J09) + 3 * pi * (J15 + y * J05)) + KXt
    K = iv.sqrt(KH * KH + KX * KX)
    res = {"K_H_upper": mp.nstr(KH.b, 15), "K_X_upper": mp.nstr(KX.b, 15), "K_upper": mp.nstr(K.b, 15),
           "K_H_below_stated_1.125808767": bool(KH.b < iv.mpf("1.125808767").a),
           "K_X_below_stated_0.314420277": bool(KX.b < iv.mpf("0.314420277").a),
           "K_below_6_5": bool(K.b < iv.mpf(6).a / 5)}
    # envelope versus actual jets (floating)
    env = []
    for t, x in [(0, 0), (0, 10), (0, 30), (0, 44.1303), (0.25, 44.1303), (0, 85)]:
        _, hh = jets(mp.mpf(t), mp.mpf(x), 1) if x != 0 else (None, theta_jet0(mp.mpf("1e-30"), 1))
        hn = mp.sqrt(hh[0] ** 2 + hh[1] ** 2)
        env.append({"t": t, "x": x, "jet_norm": s(hn, 6), "jet_norm_times_exp_pi_x_over_16": s(hn * mp.exp(mp.pi * x / 16), 6)})
    res["envelope_samples"] = env
    return res


# ---------------------------------------------------------------------------
# Section H: no real zeros above an explicit height
# ---------------------------------------------------------------------------

def section_H(aE):
    a, EA = aE
    iv.dps = 50
    # outward constants from the committed Note 05 record (|a| lower, E_A upper)
    a_lo = iv.mpf("0.0395122594985")
    EA_hi = iv.mpf("745.331444")
    assert a_lo.b <= abs(a) and EA_hi.a >= EA
    MAv = DESIGNS["recurrence"] * mp.matrix(directions05()[0] + [0, 0, 0])
    MA = mp.sqrt(mp.fsum(MAv[i] ** 2 for i in range(MAv.rows)))
    out = {"recurrence_norm_of_A": s(MA, 12)}
    for label, eps in (("coefficient_sup_1e-16", iv.mpf("1e-16")),
                       ("recurrence_norm_1e-16", iv.mpf("1e-16") / iv.mpf(mp.nstr(MA, 40)) * iv.mpf("0.99999999"))):
        X = 140
        while True:
            xv = iv.mpf(X)
            lhs = eps * (a_lo * xv ** -2 - EA_hi * xv ** -4)
            rhs = iv.mpf(6) / 5 * iv.exp(-iv.pi * xv / 16)
            if lhs.a > rhs.b:
                break
            X += 1
        # monotonicity of (|a| x^-2 - E_A x^-4) e^{pi x/16} for x >= X: log-derivative
        # pi/16 - (2|a|x^2 - 4E_A)/(x(|a|x^2 - E_A)) > pi/16 - 2/(x - E_A/(|a| x)) > 0
        xv = iv.mpf(X)
        mono = iv.pi / 16 - 2 / (xv - EA_hi / (a_lo * xv))
        out[label] = {"X": X, "monotone_beyond": bool(mono.a > 0),
                      "statement": "for 0<=t<=1/4 and real x>=X, |eps H_A(t,x)| > (6/5)e^{-pi x/16} >= |H_theta(t,x)|, so H_theta+eps H_A has no real zero there"}
    # one preregistered floating illustration: t = 0, eps = +/- 1e-16/||M_rec A||,
    # count sign changes of H_theta + eps H_A on [100, 300], step 1/20.
    A = directions05()[0]
    epsf = mp.mpf("1e-16") / MA
    illus = {}
    grid = [mp.mpf(100) + mp.mpf(j) / 20 for j in range(4001)]
    vals_theta, vals_A = [], []
    with mp.workdps(30):
        for x in grid:
            vals_theta.append(theta_jet0(x, 0)[0])
            vals_A.append(mp.fsum(A[n] * mp.re(mode_F0(n + 1, x)) for n in range(3)))
    def changes(vals):
        return [grid[j] for j in range(len(vals) - 1) if (vals[j] > 0) != (vals[j + 1] > 0)]
    zt = changes(vals_theta)
    illus["theta_sign_changes_100_300"] = len(zt)
    for sign in (1, -1):
        va = [vt + sign * epsf * vA for vt, vA in zip(vals_theta, vals_A)]
        zc = changes(va)
        illus["eps_sign_%+d" % sign] = {"sign_changes": len(zc), "last_sign_change_near": s(zc[-1], 6) if zc else None}
    illus["contract"] = ("preregistered: t=0, direction A of Note 05, recurrence measurement norm exactly 1e-16, "
                         "grid [100,300] step 0.05, sign changes only; floating, a near-pair can be missed")
    out["illustration"] = illus
    return out


# ---------------------------------------------------------------------------

def rec_keys(rec):
    return {k.split("_")[0] for k in rec}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--committed-dir", type=Path, help="directory holding the committed round-1 JSON records")
    ap.add_argument("--sections", default="ABCDPEFGH")
    args = ap.parse_args()
    cd = args.committed_dir
    rec = {"schema": "project07_round1_review_checks_v1", "date": "2026-10-17",
           "prepared_for": "Edward Baker", "model": "Claude Opus 5.5 (claude-opus-5-5)",
           "reasoning_effort": "max", "status": "floating diagnostics at 60 digits except Sections G-H (interval)",
           "python": platform.python_version(), "mpmath": mp.__version__,
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if cd:
        rec["committed_record_sha256"] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                          for p in sorted(cd.glob("*.json"))}
    secs = args.sections
    gl = None
    if "A" in secs:
        rec["A_jets"] = section_A(cd / "CERTIFIED_EVALUATION.json" if cd else None)
        print("A done", time.monotonic() - START, flush=True)
    if "B" in secs:
        rec["B_conditioning"] = section_B(cd / "CERTIFIED_MEASUREMENTS.json" if cd else None)
        print("B done", time.monotonic() - START, flush=True)
    if "C" in secs or "D" in secs:
        gl = gaps()
        rec["zero_gaps"] = [{"listed_point": oid, "gap": [s(lo, 12), s(hi, 12)]} for _, _, oid, lo, hi in gl]
    if "C" in secs:
        rec["C_alignment"] = section_C(gl)
        print("C done", time.monotonic() - START, flush=True)
    if "D" in secs:
        rec["D_theta_tail_feasibility_at_alignment"] = section_D(gl)
        print("D done", time.monotonic() - START, flush=True)
    if "P" in secs:
        rec["P_prescribed_classification"] = section_P(cd / "CERTIFIED_FEASIBILITY.json" if cd else None)
        print("P done", time.monotonic() - START, flush=True)
    if "E" in secs:
        rec["E_three_square_bracket"] = section_E()
        print("E done", time.monotonic() - START, flush=True)
    aE = None
    if "F" in secs or "H" in secs:
        rec["F_note05_constants"], aE = section_F(cd / "CONCRETE_ONSET_BUDGET.json" if cd else None)
        print("F done", time.monotonic() - START, flush=True)
    if "G" in secs:
        rec["G_envelope"] = section_G()
        print("G done", time.monotonic() - START, flush=True)
    if "H" in secs:
        rec["H_no_real_zeros"] = section_H(aE)
        print("H done", time.monotonic() - START, flush=True)
    if "C" in rec_keys(rec):
        c = rec["C_alignment"]
        rec["summary_C"] = {
            "combinations": len(c),
            "max_abs_rM_over_eta_minus_1_at_alignment": max(abs(float(z["r_M_over_eta_at_x_star_minus_1"])) for z in c),
            "eta_star_over_eta_listed_range": [min(float(z["eta_star_over_eta_listed"]) for z in c),
                                               max(float(z["eta_star_over_eta_listed"]) for z in c)],
            "listed_rM_over_eta_range": [min(float(z["r_M_at_listed_point"]) / float(z["eta_at_listed_point"]) for z in c),
                                         max(float(z["r_M_at_listed_point"]) / float(z["eta_at_listed_point"]) for z in c)],
            "nonzero_frozen_H_xx_all": all(float(z["frozen_H_xx"]) != 0 for z in c)}
    rec["elapsed_seconds"] = round(time.monotonic() - START, 1)
    args.output.write_text(json.dumps(rec, indent=1) + "\n")
    print("written", args.output, rec["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    main()
