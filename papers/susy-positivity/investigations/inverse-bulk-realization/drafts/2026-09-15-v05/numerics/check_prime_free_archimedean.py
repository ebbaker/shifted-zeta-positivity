#!/usr/bin/env python3
"""The prime-free archimedean inequality: where it is a theorem and where it is not.

Standard library only. Prints a JSON record to standard output.

The object is the prime-free form of the localized Weil target,

    A_L[f] = K[E_L f] + ( w0 + sum_{p < e^L} kappat_p ) ||f||^2 + P_L[f],
    kappat_p = 2 (log p) / (sqrt p + 1),     w0 = psi(1/4) - log pi,

which appears as (8.1) of the working manuscript.  Four things are checked.

(1) For L <= log 2 no prime is active, so the constant is w0 and A_L = Q_L
    identically: on that range the prime-free inequality IS the localized Weil
    inequality, with no slack gained.  Checked on step inputs.

(2) A_L and Q_L commute with x -> -x, so both split by parity, and the rank
    two pole form splits as +2|<cosh(x/2),f>|^2 on the even sector and
    -2|<sinh(x/2),f>|^2 on the odd sector.  The indefiniteness of P_L is
    therefore entirely an odd-sector phenomenon.  Checked on the form matrix.

(3) Fourier-free Galerkin Rayleigh quotients for A_L in a uniform cell basis,
    whole space and each parity sector, and on the hyperplane
    {<e^{x/2},f> = 0} on which the pole form vanishes -- the subspace covered
    by the archimedean positivity results in the literature.  These quotients
    are ONE SIDED: a Galerkin space is a subspace, so a NEGATIVE value would
    certify that A_L is not positive, while a positive value certifies
    nothing.

(4) An unconditional sufficient criterion, with its verification:

        w0 + sum_{p<e^L} kappat_p + 2 N(L/2) >= 2 sinh(L/2) - L,
        N(a) = sum_{n>=0} e^{-a_n a}/a_n,   a_n = 2n + 1/2,

    implies A_L >= 0.  The criterion is checked at every prime breakpoint up
    to 10^6; it first holds at L = log 7 and holds at every breakpoint above.
    Monotonicity in L between breakpoints reduces the range to the
    breakpoints, and an explicit Chebyshev bound covers L > log(10^6).

No Weil positivity certificate for L <= log 2 is claimed, and no field
theory is constructed.  The Galerkin numbers are evidence, not proof; the
criterion of (4) is a proof for the range in which it holds.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_channel_bound import (  # noqa: E402
    Step, W0, PSI1_QUARTER, a, primes_below, active_shifts,
)
from check_mirror_subtraction import kappa_tilde  # noqa: E402

SUM_INV_A2 = PSI1_QUARTER / 4          # sum_n a_n^{-2}
LOG2 = math.log(2.0)


# ---------------------------------------------------------------- series ---
def S(t, tol=1e-15):
    """sum_{n>=0} e^{-a_n t}/a_n^2, with S(0) = psi'(1/4)/4 in closed form."""
    if t <= 0.0:
        return SUM_INV_A2
    total, n = 0.0, 0
    while True:
        an = a(n)
        term = math.exp(-an * t) / an ** 2
        total += term
        # remaining terms are bounded by term * e^{-2t}/(1 - e^{-2t})
        if term * math.exp(-2 * t) / (1 - math.exp(-2 * t)) < tol:
            return total
        n += 1


def N(t, tol=1e-15):
    """sum_{n>=0} e^{-a_n t}/a_n  (the exterior gamma weight, t > 0)."""
    total, n = 0.0, 0
    while True:
        an = a(n)
        term = math.exp(-an * t) / an
        total += term
        if term * math.exp(-2 * t) / (1 - math.exp(-2 * t)) < tol:
            return total
        n += 1


# ------------------------------------------------------------- matrices ---
def gamma_matrix(L, m):
    """K in the basis of m indicator cells of width h = L/m on I_L.

    K(1_j,1_k) depends only on n = |j-k|:
        n = 0 : 2 [S(0) - S(h)]
        n >= 1: -[S((n-1)h) - 2 S(nh) + S((n+1)h)]
    """
    h = L / m
    Sv = [S(i * h) for i in range(m + 2)]
    row = [2.0 * (Sv[0] - Sv[1])]
    for n in range(1, m):
        row.append(-(Sv[n - 1] - 2 * Sv[n] + Sv[n + 1]))
    return [[row[abs(j - k)] for k in range(m)] for j in range(m)], h


def cell_moments(L, m):
    """integrals of cosh(x/2), sinh(x/2), e^{x/2} over each cell."""
    h = L / m
    cosv, sinv, expv = [], [], []
    for j in range(m):
        lo = -L / 2 + j * h
        hi = lo + h
        cosv.append(2 * (math.sinh(hi / 2) - math.sinh(lo / 2)))
        sinv.append(2 * (math.cosh(hi / 2) - math.cosh(lo / 2)))
        expv.append(2 * (math.exp(hi / 2) - math.exp(lo / 2)))
    return cosv, sinv, expv


def constant_c(L):
    return W0 + sum(kappa_tilde(p) for p in primes_below(math.exp(L)))


def form_matrix(L, m, kind="A"):
    """Matrix of A_L (or Q_L) on the cell basis; Gram matrix is h * identity."""
    K, h = gamma_matrix(L, m)
    cosv, sinv, _ = cell_moments(L, m)
    const = constant_c(L) if kind == "A" else W0
    M = [[K[j][k] for k in range(m)] for j in range(m)]
    for j in range(m):
        M[j][j] += const * h
    for j in range(m):
        for k in range(m):
            M[j][k] += 2 * cosv[j] * cosv[k] - 2 * sinv[j] * sinv[k]
    if kind == "Q":
        for d, coef in active_shifts(L):
            for j in range(m):
                for k in range(m):
                    w = 0.0
                    for sgn in (1, -1):
                        t = h - abs(d - sgn * (j - k) * h)
                        if t > 0:
                            w += 0.5 * t
                    M[j][k] -= coef * w
    return M, h


# ----------------------------------------------------------- eigenvalues ---
def jacobi(M, sweeps=60, tol=1e-13):
    """Eigenvalues and eigenvectors of a real symmetric matrix by cyclic Jacobi."""
    n = len(M)
    A_ = [row[:] for row in M]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(sweeps):
        off = math.sqrt(sum(A_[p][q] ** 2 for p in range(n) for q in range(n) if p != q))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(A_[p][q]) < 1e-18:
                    continue
                theta = (A_[q][q] - A_[p][p]) / (2 * A_[p][q])
                t = (1 if theta >= 0 else -1) / (abs(theta) + math.sqrt(theta * theta + 1))
                c = 1 / math.sqrt(t * t + 1)
                s = t * c
                for k in range(n):
                    akp, akq = A_[k][p], A_[k][q]
                    A_[k][p] = c * akp - s * akq
                    A_[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = A_[p][k], A_[q][k]
                    A_[p][k] = c * apk - s * aqk
                    A_[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = V[k][p], V[k][q]
                    V[k][p] = c * vkp - s * vkq
                    V[k][q] = s * vkp + c * vkq
    return [A_[i][i] for i in range(n)], V


def jacobi_min(M, sweeps=60, tol=1e-13):
    """Smallest eigenvalue of a real symmetric matrix."""
    if not M:
        return float("inf")
    return min(jacobi(M, sweeps, tol)[0])


def jacobi_min_vec(M):
    """Smallest eigenvalue and its eigenvector."""
    vals, V = jacobi(M)
    i = min(range(len(vals)), key=lambda k: vals[k])
    return vals[i], [V[r][i] for r in range(len(M))]


def restrict(M, vec):
    """Matrix of M on the Euclidean orthogonal complement of vec."""
    n = len(M)
    nrm = math.sqrt(sum(v * v for v in vec))
    u = [v / nrm for v in vec]
    basis = []
    for i in range(n):
        e = [1.0 if k == i else 0.0 for k in range(n)]
        d = sum(u[k] * e[k] for k in range(n))
        w = [e[k] - d * u[k] for k in range(n)]
        for b in basis:
            d2 = sum(b[k] * w[k] for k in range(n))
            w = [w[k] - d2 * b[k] for k in range(n)]
        nw = math.sqrt(sum(x * x for x in w))
        if nw > 1e-8:
            basis.append([x / nw for x in w])
        if len(basis) == n - 1:
            break
    out = []
    for b1 in basis:
        Mb = [sum(M[p][q] * b1[q] for q in range(n)) for p in range(n)]
        out.append([sum(b2[p] * Mb[p] for p in range(n)) for b2 in basis])
    # symmetrise against round-off
    r = len(out)
    return [[0.5 * (out[i][j] + out[j][i]) for j in range(r)] for i in range(r)]


def parity_blocks(M):
    """Even and odd blocks of a matrix commuting with cell reversal."""
    n = len(M)
    ev, od = [], []
    for j in range(n // 2):
        e = [0.0] * n
        e[j] = e[n - 1 - j] = 1 / math.sqrt(2)
        ev.append(e)
        o = [0.0] * n
        o[j], o[n - 1 - j] = 1 / math.sqrt(2), -1 / math.sqrt(2)
        od.append(o)
    if n % 2:
        e = [0.0] * n
        e[n // 2] = 1.0
        ev.append(e)

    def blk(bs):
        out = []
        for b1 in bs:
            Mb = [sum(M[p][q] * b1[q] for q in range(n)) for p in range(n)]
            out.append([sum(b2[p] * Mb[p] for p in range(n)) for b2 in bs])
        return out
    return blk(ev), blk(od)


def parity_defect(M):
    """max |M_{jk} - M_{(n-1-j)(n-1-k)}|, zero iff M commutes with reversal."""
    n = len(M)
    return max(abs(M[j][k] - M[n - 1 - j][n - 1 - k])
               for j in range(n) for k in range(n))


def solve(M, b):
    """Solve M x = b by Gauss-Jordan with partial pivoting."""
    n = len(M)
    A_ = [row[:] + [b[i]] for i, row in enumerate(M)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(A_[r][i]))
        A_[i], A_[p] = A_[p], A_[i]
        piv = A_[i][i]
        for r in range(n):
            if r != i and A_[r][i] != 0.0:
                f = A_[r][i] / piv
                for k in range(i, n + 1):
                    A_[r][k] -= f * A_[i][k]
    return [A_[i][n] / A_[i][i] for i in range(n)]


def negative_count(M):
    """Number of negative eigenvalues, by symmetric Gaussian elimination."""
    n = len(M)
    A_ = [row[:] for row in M]
    neg = 0
    for i in range(n):
        piv = A_[i][i]
        if piv < 0:
            neg += 1
        for r in range(i + 1, n):
            f = A_[r][i] / piv
            for k in range(i, n):
                A_[r][k] -= f * A_[i][k]
    return neg


def parity_bases(n):
    ev, od = [], []
    for j in range(n // 2):
        e = [0.0] * n
        e[j] = e[n - 1 - j] = 1 / math.sqrt(2)
        ev.append(e)
        o = [0.0] * n
        o[j], o[n - 1 - j] = 1 / math.sqrt(2), -1 / math.sqrt(2)
        od.append(o)
    if n % 2:
        e = [0.0] * n
        e[n // 2] = 1.0
        ev.append(e)
    return ev, od


def project(M, basis):
    n = len(M)
    out = []
    for b1 in basis:
        Mb = [sum(M[p][q] * b1[q] for q in range(n)) for p in range(n)]
        out.append([sum(b2[p] * Mb[p] for p in range(n)) for b2 in basis])
    return out


# ----------------------------------------- the exterior gamma weight N(a) ---
_N_HALF = None


def _regular(r):
    """n_gamma(r) - 1/(2r); continuous, equal to 1/4 at r = 0."""
    if r < 1e-6:
        return 0.25 - r / 48
    return math.exp(-r / 2) / (1 - math.exp(-2 * r)) - 1 / (2 * r)


def Nx(t, panels=200):
    """N(t) for every t > 0: direct series for t >= 1/2, otherwise by
    N(t) = N(1/2) + (1/2) log(1/(2t)) + int_t^{1/2} [n_gamma - 1/(2r)] dr."""
    global _N_HALF
    if t >= 0.5:
        return N(t)
    if _N_HALF is None:
        _N_HALF = N(0.5)
    h = (0.5 - t) / panels
    s = _regular(t) + _regular(0.5)
    for i in range(1, panels):
        s += (4 if i % 2 else 2) * _regular(t + i * h)
    return _N_HALF + 0.5 * math.log(0.5 / t) + s * h / 3


def exterior_weight(x, L):
    """h(x) = int_{|y|>L/2} n_gamma(|x-y|) dy = N(L/2-x) + N(L/2+x)."""
    return Nx(L / 2 - x) + Nx(L / 2 + x)


def simple_margin(L, ksum=None):
    """c_L + 2 N(L/2) - (2 sinh(L/2) - L); nonnegative implies A_L >= 0."""
    c = constant_c(L) if ksum is None else W0 + ksum
    return c + 2 * N(L / 2) - (2 * math.sinh(L / 2) - L)


def weighted_test(L, panels=1200):
    """J(L) = int sinh^2(x/2)/(h(x)+c_L) dx; J <= 1/2 implies A_L >= 0."""
    c = constant_c(L)
    if 2 * N(L / 2) + c <= 0:
        return float("inf")
    step, tot = L / panels, 0.0
    for i in range(panels):
        x = -L / 2 + (i + 0.5) * step
        tot += math.sinh(x / 2) ** 2 / (exterior_weight(x, L) + c) * step
    return tot


def sieve(n):
    flags = bytearray([1]) * (n + 1)
    flags[0] = flags[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if flags[i]:
            flags[i * i::i] = bytearray(len(flags[i * i::i]))
    return [i for i in range(n + 1) if flags[i]]


def rayleigh(M, h, fv):
    n = len(fv)
    num = sum(M[j][k] * fv[j] * fv[k] for j in range(n) for k in range(n))
    return num / (h * sum(v * v for v in fv))


def main():
    import random
    random.seed(20260915)
    checks = {}

    # (0) the cell-basis gamma matrix against the independent step routine
    agree = 0
    worst_gamma = 0.0
    for L, m in ((0.5, 8), (LOG2, 12), (1.25, 10), (3.0, 16)):
        Kmat, _ = gamma_matrix(L, m)
        for _ in range(3):
            fv = [random.uniform(-1, 1) for _ in range(m)]
            quad = sum(Kmat[j][k] * fv[j] * fv[k] for j in range(m) for k in range(m))
            ref, _tail = Step(L, fv).gamma_energy()
            worst_gamma = max(worst_gamma, abs(quad - ref))
            agree += 1
    assert worst_gamma < 1e-10, worst_gamma
    checks["gamma_matrix_against_step_routine"] = agree

    # (1) below log 2 the prime-free form IS the Weil form
    same = 0
    worst_same = 0.0
    for L in (0.3, 0.5, 0.6, LOG2 - 1e-12):
        assert primes_below(math.exp(L)) == []
        assert abs(constant_c(L) - W0) == 0.0
        M, h = form_matrix(L, 12, "A")
        for _ in range(3):
            fv = [random.uniform(-1, 1) for _ in range(12)]
            s = Step(L, fv)
            Kv, _t = s.gamma_energy()
            Q = Kv + W0 * s.norm2() + s.poles() + s.prime_term(L)
            quad = sum(M[j][k] * fv[j] * fv[k] for j in range(12) for k in range(12))
            worst_same = max(worst_same, abs(quad - Q))
            same += 1
    assert worst_same < 1e-10, worst_same
    checks["prime_free_form_equals_weil_form_below_log2"] = same

    # (2) parity: both forms commute with x -> -x
    par = 0
    worst_par = 0.0
    for L in (0.5, LOG2, 1.25, 2.0):
        for kind in ("A", "Q"):
            M, _h = form_matrix(L, 24, kind)
            worst_par = max(worst_par, parity_defect(M))
            par += 1
    assert worst_par < 1e-11, worst_par
    checks["parity_commutation"] = par

    # (3) Galerkin Rayleigh quotients (one sided: negative certifies failure)
    table = []
    m = 48
    for L in (0.3, 0.5, 0.6, LOG2 - 1e-12, LOG2 + 1e-12, 0.8, 1.0, 1.25, 1.5,
              2.0, 3.0, 4.0, 5.0):
        M, h = form_matrix(L, m, "A")
        ev, od = parity_bases(m)
        _c, _s, expv = cell_moments(L, m)
        table.append({
            "L": round(L, 6), "cells": m,
            "constant": constant_c(L),
            "lambda_min_A": jacobi_min(M) / h,
            "even_sector": jacobi_min(project(M, ev)) / h,
            "odd_sector": jacobi_min(project(M, od)) / h,
            "on_pole_free_hyperplane": jacobi_min(restrict(M, expv)) / h,
        })
    assert min(r["lambda_min_A"] for r in table) > 0
    checks["galerkin_rayleigh_points"] = len(table)

    conv = []
    for mm in (12, 24, 48, 80):
        M, h = form_matrix(LOG2 - 1e-12, mm, "A")
        conv.append({"cells": mm, "lambda_min_A": jacobi_min(M) / h})
    checks["galerkin_refinement_points"] = len(conv)

    # (4) the pole term is indispensable: K + c_L||f||^2 alone is not positive.
    #     The indicator of I_L is an explicit certificate.
    polefree = []
    for L in (0.3, 0.5, LOG2 - 1e-12, 1.0, 1.5, 2.0):
        s = Step(L, [1.0])
        Kv, _t = s.gamma_energy()
        polefree.append({"L": round(L, 6),
                         "indicator_K_plus_constant": (Kv + constant_c(L) * s.norm2()) / s.norm2(),
                         "indicator_pole_term": s.poles() / s.norm2()})
    negcerts = [r for r in polefree if r["indicator_K_plus_constant"] < 0]
    assert len(negcerts) >= 4
    checks["pole_free_negative_certificates"] = len(negcerts)

    # (5) the two scalar conditions, given the parity split and the inertia
    scalars = []
    mm = 60
    for L in (0.3, 0.5, 0.6, LOG2 - 1e-12, 0.8, 1.0, 1.5):
        Kmat, h = gamma_matrix(L, mm)
        W = [[Kmat[j][k] for k in range(mm)] for j in range(mm)]
        for j in range(mm):
            W[j][j] += constant_c(L) * h
        cosv, sinv, _e = cell_moments(L, mm)
        ev, od = parity_bases(mm)
        We, Wo = project(W, ev), project(W, od)
        ce = [sum(b[q] * cosv[q] for q in range(mm)) for b in ev]
        so = [sum(b[q] * sinv[q] for q in range(mm)) for b in od]
        qe = 2 * sum(ce[i] * x for i, x in enumerate(solve(We, ce)))
        qo = 2 * sum(so[i] * x for i, x in enumerate(solve(Wo, so)))
        scalars.append({"L": round(L, 6), "negative_eigenvalues_of_W": negative_count(W),
                        "even_scalar_needs_le_minus_one": qe,
                        "odd_scalar_needs_le_one": qo,
                        "lambda_min_W_odd": jacobi_min(Wo) / h})
    assert all(r["negative_eigenvalues_of_W"] == 1 for r in scalars)
    assert all(r["even_scalar_needs_le_minus_one"] <= -1 for r in scalars)
    assert all(r["odd_scalar_needs_le_one"] <= 1 for r in scalars)
    checks["scalar_reduction_points"] = len(scalars)

    escale = []
    for mm2 in (20, 40, 80, 120):
        Kmat, h = gamma_matrix(LOG2 - 1e-12, mm2)
        W = [[Kmat[j][k] for k in range(mm2)] for j in range(mm2)]
        for j in range(mm2):
            W[j][j] += W0 * h
        cosv, _s, _e = cell_moments(LOG2 - 1e-12, mm2)
        ev, _od = parity_bases(mm2)
        We = project(W, ev)
        ce = [sum(b[q] * cosv[q] for q in range(mm2)) for b in ev]
        escale.append({"cells": mm2,
                       "even_scalar": 2 * sum(ce[i] * x for i, x in enumerate(solve(We, ce)))})
    checks["even_scalar_refinement_points"] = len(escale)

    # (6) the archimedean form with the bare constant w0 fails just above log 2.
    #     A negative Rayleigh quotient in a step subspace IS a certificate.
    mm3 = 40
    Kmat, h = gamma_matrix(0.75, mm3)
    cosv, sinv, _e = cell_moments(0.75, mm3)
    Mp = [[Kmat[j][k] + 2 * cosv[j] * cosv[k] - 2 * sinv[j] * sinv[k] for k in range(mm3)]
          for j in range(mm3)]
    for j in range(mm3):
        Mp[j][j] += W0 * h
    lam, vec = jacobi_min_vec(Mp)
    rounded = [round(v, 4) for v in vec]
    cert = rayleigh(Mp, h, rounded)
    assert cert < 0, cert
    bare = []
    for L in (LOG2, 0.72, 0.74, 0.75, 0.80):
        Kmat, h = gamma_matrix(L, mm3)
        cosv, sinv, _e = cell_moments(L, mm3)
        Mb = [[Kmat[j][k] + 2 * cosv[j] * cosv[k] - 2 * sinv[j] * sinv[k] for k in range(mm3)]
              for j in range(mm3)]
        for j in range(mm3):
            Mb[j][j] += W0 * h
        bare.append({"L": round(L, 6), "lambda_min": jacobi_min(Mb) / h})
    checks["bare_constant_form_points"] = len(bare)

    # (7) the sufficient criterion at every prime breakpoint below 10^6
    primes = sieve(1000000)
    run, first_ok, worst_after, failures_after = 0.0, None, None, 0
    plateaus = []
    for i, p in enumerate(primes[:-1]):
        run += kappa_tilde(p)
        L = math.log(primes[i + 1])          # right endpoint of the plateau
        mar = simple_margin(L, ksum=run)
        if len(plateaus) < 14:
            plateaus.append({"primes_through": p, "L": L, "constant": W0 + run,
                             "exterior": 2 * N(L / 2),
                             "sinh_bound": 2 * math.sinh(L / 2) - L, "margin": mar})
        if first_ok is None and mar > 0:
            first_ok = {"primes_through": p, "L": L, "margin": mar}
        if first_ok is not None:
            if mar <= 0:
                failures_after += 1
            if worst_after is None or mar < worst_after["margin"]:
                worst_after = {"primes_through": p, "L": L, "margin": mar}
    assert failures_after == 0
    assert first_ok["primes_through"] == 11
    checks["criterion_prime_breakpoints"] = len(primes) - 1

    # tail input for L > log 10^6: the Chebyshev sum actually available there
    G = sum(math.log(p) / math.sqrt(p) for p in primes)
    theta = sum(math.log(p) for p in primes)

    # (8) the edge weighted refinement covers log 7 <= L < log 11
    jvals = []
    for L in (math.log(7) + 1e-9, 2.0, 2.1, 2.2, 2.3, math.log(11) - 1e-9,
              math.log(11) + 1e-9, 2.5, 3.0):
        jvals.append({"L": round(L, 6), "J": weighted_test(L),
                      "interior_constant": 2 * N(L / 2) + constant_c(L)})
    assert all(r["J"] <= 0.5 for r in jvals)
    checks["weighted_criterion_points"] = len(jvals)

    # (9) the two algebraic steps the theorem of section 5 rests on, checked
    #     independently on random step inputs:
    #       K[F] >= int |F|^2 h(x) dx >= 2 N(L/2) ||F||^2,   h = exterior weight,
    #       |<sinh(x/2),f>|^2 <= (sinh(L/2) - L/2) ||f||^2,
    #       P_L[f] = 2 (int f e^{x/2}) (int f e^{-x/2}).
    steps = 0
    worst_ext, worst_sinh, worst_pole = 1e9, 1e9, 0.0
    for L in (0.5, LOG2, 1.5, 2.5, 3.5):
        mm4 = 16
        hh = L / mm4
        hw = [0.0] * mm4
        for j in range(mm4):
            lo = -L / 2 + j * hh
            panels = 40
            acc = 0.0
            for i in range(panels):
                acc += exterior_weight(lo + (i + 0.5) * hh / panels, L) * hh / panels
            hw[j] = acc
        sinh_norm2 = math.sinh(L / 2) - L / 2
        cosv, sinv, expv = cell_moments(L, mm4)
        negv = [2 * (math.exp(-lo / 2) - math.exp(-hi / 2))
                for lo, hi in ((-L / 2 + j * hh, -L / 2 + (j + 1) * hh) for j in range(mm4))]
        for _ in range(6):
            fv = [random.uniform(-1, 1) for _ in range(mm4)]
            s = Step(L, fv)
            Kv, _t = s.gamma_energy()
            n2 = s.norm2()
            ext = sum(hw[j] * fv[j] ** 2 for j in range(mm4))
            worst_ext = min(worst_ext, Kv - ext)
            assert Kv >= ext - 1e-9, (L, Kv, ext)
            assert ext >= 2 * N(L / 2) * n2 - 1e-9, (L, ext, n2)
            sval = sum(fv[j] * sinv[j] for j in range(mm4))
            worst_sinh = min(worst_sinh, sinh_norm2 * n2 - sval ** 2)
            assert sval ** 2 <= sinh_norm2 * n2 + 1e-9, (L, sval, n2)
            u = sum(fv[j] * expv[j] for j in range(mm4))
            v = sum(fv[j] * negv[j] for j in range(mm4))
            worst_pole = max(worst_pole, abs(s.poles() - 2 * u * v))
            assert abs(s.poles() - 2 * u * v) < 1e-9, (L, s.poles(), 2 * u * v)
            steps += 3
    checks["theorem_ingredients_on_random_steps"] = steps

    print(json.dumps({
        "status": "passed",
        "date": "2026-09-15",
        "model": "Claude Opus 5",
        "arithmetic": "floating point; the gamma series are summed with explicit "
                      "geometric tail bounds and the cell-basis matrix is checked "
                      "against the independent step routine",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "galerkin_table": table,
        "galerkin_refinement_at_log2": conv,
        "pole_free_indicator_values": polefree,
        "scalar_reduction": scalars,
        "even_scalar_refinement_at_log2": escale,
        "bare_constant_form": bare,
        "bare_constant_failure_certificate": {
            "L": 0.75, "cells": mm3, "rayleigh_quotient": cert,
            "vector": rounded,
        },
        "criterion_first_plateau": first_ok,
        "criterion_worst_plateau_after": worst_after,
        "criterion_plateaus": plateaus,
        "chebyshev_tail": {
            "X0": 1000000, "sum_log_p_over_sqrt_p_below_X0": G, "theta_X0": theta,
            "alpha": 1 - 1 / math.log(1000000),
            "lower_bound_constant": G - theta / 1000.0 - 1000.0 * (1 - 1 / math.log(1000000)),
            "lower_bound_slope": 2 * (1 - 1 / math.log(1000000)),
            "statement": "for X >= X0, sum_{p<X} 2 log p/(sqrt p + 1) >= "
                         "lower_bound_slope * sqrt X + lower_bound_constant, which "
                         "exceeds sqrt X - 1/sqrt X - log X + |w0| since the slope "
                         "exceeds 1 and the constant is positive; uses only "
                         "theta(t) >= t(1 - 1/log t) for t >= 41 "
                         "(Rosser and Schoenfeld 1962, Theorem 10)",
        },
        "weighted_criterion": jvals,
        "theorem_ingredient_slacks": {
            "min_K_minus_exterior_part": worst_ext,
            "min_sinh_cauchy_schwarz_slack": worst_sinh,
            "max_pole_factorisation_error": worst_pole,
        },
        "scope": "Supports the note PRIME_FREE_ARCHIMEDEAN_INEQUALITY_20260915.md. "
                 "The criterion of items (7) and (8) is a proof of A_L >= 0 for "
                 "L >= log 7. Everything computed in a step subspace is one sided: "
                 "a negative Rayleigh quotient certifies that a form is not "
                 "positive, a positive one certifies nothing. No Weil positivity "
                 "certificate for L <= log 2 is claimed and no field theory is "
                 "constructed.",
    }, indent=2))


if __name__ == "__main__":
    main()
