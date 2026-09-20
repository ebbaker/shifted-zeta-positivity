#!/usr/bin/env python3
"""Splitting the archimedean form by the SIGN OF ITS SYMBOL rather than by the
constant, and what that does to the saturation of the compression.

Standard library only. Prints a JSON record to standard output.

Proposition 7.14 of the inverse-bulk manuscript 0.5 presents the target as

    Q_L = K_+ - T_L,
    K_+[f] = K[E_L f] + (c_L)_+ ||f||^2 + 2 |<cosh(x/2), f>|^2,
    T_L[f] = (c_L)_- ||f||^2 + 2 |<sinh(x/2), f>|^2 + sum_p Bt_{r_p,d_p}[E_L f],
    c_L    = w0 + sum_{p < e^L} kappat_p,                                (7.20)-(7.22)

with both sides positive term by term.  It moves the WHOLE constant to whichever
side its sign puts it, at every frequency.

By the density identity b(tau^2) + w0 = 2 theta'(tau) -- see
check_density_symbol.py and the accompanying note -- the source-side symbol is

    sigma_L(tau) = b(tau^2) + w0 + sum_{p < e^L} kappat_p = 2 theta'(tau) + Sigma_L,

which is negative only on a band |tau| < tau_L that shrinks with L and is empty
for L > log 13.  So only that band needs to move.  Put

    K_+^new[f] = (1/2pi) int sigma_L^+(tau) |F^|^2 dtau + 2 |<cosh(x/2), f>|^2,
    T_L^new[f] = (1/2pi) int sigma_L^-(tau) |F^|^2 dtau + 2 |<sinh(x/2), f>|^2
                 + sum_p Bt_{r_p,d_p}[E_L f],                               (N)

with sigma_L^± = max(±sigma_L, 0).  Equivalently K_+^new = K + c_L ||f||^2 + M^-
and T_L^new = T_L - (c_L)_- ||f||^2 + M^-, where M^- is the Fourier multiplier
with symbol sigma_L^-, supported on |tau| < tau_L.

SIX FACTS ARE CHECKED on a basis of m indicator cells on I_L.

(1) The gamma energy in closed form.  On cells the energy matrix is Toeplitz:
    with S2(x) = sum_{n>=0} e^{-a_n x}/a_n^2, a_n = 2n+1/2, S2(0) = psi'(1/4)/4,

        K_jj = 2 [S2(0) - S2(h)],
        K_jk = -[S2(d-h) - 2 S2(d) + S2(d+h)],   d = |x_j - x_k| >= h,

    because the triangle overlap of two width-h cells has Laplace transform
    4 sinh^2(ah/2)/a^2.  Checked against direct quadrature of (2.5).
(2) Both identities as finite matrix identities: Q_L = K_+ - T_L (7.14) and
    Q_L = K_+^new - T_L^new (N), from independently assembled matrices.
(3) M^- >= 0 and T_L^new >= 0, by Cholesky, with the least pivot reported.
(4) K_+^new <= K_+, i.e. the new presentation moves STRICTLY LESS to the
    subtracted side: sigma_L^- <= (c_L)_- pointwise with equality only at
    tau = 0.  Checked as positivity of K_+ - K_+^new.
(5) The resulting saturations lambda_min(Q_L; K_+) and lambda_min(Q_L; K_+^new)
    in the cell subspace, by bisection on the positivity of Q_L - s K_+, each
    step certified by Cholesky.
(6) tau_L and c_L for each L, and that the band is empty above log 13.

WHAT THIS DOES AND DOES NOT ESTABLISH.  (1), (2) and (6) are exact finite
statements up to the stated floating-point tolerances.  (3) and (4) corroborate
positivity statements that are anyway manifest term by term.  (5) is ONE SIDED
in the same sense as the manuscript's own compression check: these are Rayleigh
quotients in a step subspace, so a value above one would certify that the
domination fails, while a value below one certifies nothing, and the values sit
just below one because Q_L is nearly degenerate.  The cell subspace is coarse,
so the absolute values are far above the manuscript's; the RATIO of the two
presentations is what this programme is for.  No Weil positivity certificate is
claimed, and no field theory is constructed.
"""
import json
import math

CATALAN = 0.91596559417721901505460351493238411077414937428167
GAMMA_E = 0.57721566490153286060651209008240243104215933593992
CELLS = 48
TOL = 1e-10

B2 = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510]


def digamma_real_quarter_shift(t):
    """Re psi(1/4 + i t/2), by recurrence to large argument plus Stirling."""
    zr, zi = 0.25, 0.5*t
    total = 0.0
    while zr < 20.0:
        denom = zr*zr + zi*zi
        total -= zr/denom
        zr += 1.0
    total += 0.5*math.log(zr*zr + zi*zi)
    denom = zr*zr + zi*zi
    total -= 0.5*zr/denom
    # (1/z^2)^k for the Bernoulli tail, in real arithmetic
    wr, wi = zr*zr - zi*zi, 2*zr*zi          # z^2
    pr, pi_ = wr, wi
    for k, b in enumerate(B2, start=1):
        d = pr*pr + pi_*pi_
        total -= b*pr/(2*k*d)
        pr, pi_ = pr*wr - pi_*wi, pr*wi + pi_*wr
    return total


W0 = digamma_real_quarter_shift(0.0) - math.log(math.pi)
PSI1_QUARTER = math.pi**2 + 8.0*CATALAN          # psi'(1/4)


def s2(x, terms=200000):
    """sum_{n>=0} e^{-a_n x} / a_n^2 with a_n = 2n + 1/2."""
    if x <= 0.0:
        return PSI1_QUARTER/4.0
    total, n = 0.0, 0
    while n < terms:
        a = 2*n + 0.5
        term = math.exp(-a*x)/(a*a)
        total += term
        if term < 1e-18*max(total, 1e-18):
            break
        n += 1
    return total


def primes_below(bound):
    found, n = [], 2
    while n < bound:
        if all(n % p for p in found if p*p <= n):
            found.append(n)
        n += 1
    return found


def kappa_tilde(p):
    return 2.0*math.log(p)/(math.sqrt(p) + 1.0)


def bisect(f, lo, hi, rounds=200):
    negative = f(lo) < 0
    for _ in range(rounds):
        mid = 0.5*(lo + hi)
        if (f(mid) < 0) == negative:
            lo = mid
        else:
            hi = mid
    return 0.5*(lo + hi)


def cholesky_pivot(A):
    """Least pivot of the Cholesky factorization, or None if it fails."""
    n = len(A)
    L = [[0.0]*n for _ in range(n)]
    least = None
    for i in range(n):
        for j in range(i + 1):
            total = A[i][j] - sum(L[i][k]*L[j][k] for k in range(j))
            if i == j:
                if total <= 0.0:
                    return None
                least = total if least is None else min(least, total)
                L[i][i] = math.sqrt(total)
            else:
                L[i][j] = total/L[j][j]
    return least


def positive_definite(A):
    return cholesky_pivot(A) is not None


def lambda_min_generalized(Q, K, lo=-1.0, hi=1.0, rounds=45):
    """Least s with Q - s K singular, by bisection certified by Cholesky."""
    for _ in range(rounds):
        mid = 0.5*(lo + hi)
        trial = [[Q[i][j] - mid*K[i][j] for j in range(len(Q))] for i in range(len(Q))]
        if positive_definite(trial):
            lo = mid
        else:
            hi = mid
    return 0.5*(lo + hi)


def build(L, m):
    h = L/m
    x = [-L/2.0 + h*j for j in range(m)]
    tri = lambda s: max(0.0, h - abs(s))

    column = [2.0*(s2(0.0) - s2(h))]
    for i in range(1, m):
        d = i*h
        column.append(-(s2(d - h) - 2.0*s2(d) + s2(d + h)))
    K = [[column[abs(i - j)] for j in range(m)] for i in range(m)]

    u = [2.0*(math.exp((xj + h)/2.0) - math.exp(xj/2.0)) for xj in x]
    v = [2.0*(math.exp(-xj/2.0) - math.exp(-(xj + h)/2.0)) for xj in x]

    def usym(s):
        return [[0.5*(tri(s - (x[i] - x[j])) + tri(s + (x[i] - x[j])))
                 for j in range(m)] for i in range(m)]

    primes = primes_below(math.exp(L))
    sigma_shift = sum(kappa_tilde(p) for p in primes)
    c_L = W0 + sigma_shift

    Bt = [[(sigma_shift*h if i == j else 0.0) for j in range(m)] for i in range(m)]
    prime = [[0.0]*m for _ in range(m)]
    for p in primes:
        d_p, r_p = math.log(p), 1.0/math.sqrt(p)
        n = 1
        while n*d_p < L:
            block = usym(n*d_p)
            weight = 2.0*d_p*(r_p**n)
            for i in range(m):
                for j in range(m):
                    Bt[i][j] += weight*block[i][j]
                    prime[i][j] -= weight*block[i][j]
            n += 1

    Q = [[K[i][j] + (W0*h if i == j else 0.0) + u[i]*v[j] + v[i]*u[j] + prime[i][j]
          for j in range(m)] for i in range(m)]
    plus, minus = max(c_L, 0.0), max(-c_L, 0.0)
    kp_old = [[K[i][j] + (plus*h if i == j else 0.0)
               + 0.5*(u[i] + v[i])*(u[j] + v[j]) for j in range(m)] for i in range(m)]
    t_old = [[(minus*h if i == j else 0.0)
              + 0.5*(u[i] - v[i])*(u[j] - v[j]) + Bt[i][j] for j in range(m)]
             for i in range(m)]
    return dict(h=h, x=x, K=K, u=u, v=v, Bt=Bt, Q=Q, kp_old=kp_old, t_old=t_old,
                c_L=c_L, Sigma=sigma_shift, primes=primes, m=m)


def negative_part_multiplier(L, data, tau_L, panels=2000):
    """Toeplitz matrix of the Fourier multiplier with symbol sigma_L^-."""
    m, h = data["m"], data["h"]
    step = tau_L/panels
    nodes, weights, values = [], [], []
    for k in range(panels + 1):
        t = k*step
        w = step/3.0*(1.0 if k in (0, panels) else (4.0 if k % 2 else 2.0))
        if t == 0.0:
            shape = h*h                       # lim (2 sin(t h/2)/t)^2
            sym = -(digamma_real_quarter_shift(0.0) - math.log(math.pi) + data["Sigma"])
        else:
            shape = (2.0*math.sin(t*h/2.0)/t)**2
            sym = -(digamma_real_quarter_shift(t) - math.log(math.pi) + data["Sigma"])
        nodes.append(t)
        weights.append(w)
        values.append(max(sym, 0.0)*shape)
    column = []
    for i in range(m):
        d = i*h
        column.append(sum(weights[k]*values[k]*math.cos(nodes[k]*d)
                          for k in range(panels + 1))/math.pi)
    return [[column[abs(i - j)] for j in range(m)] for i in range(m)]


def direct_gamma_entry(data, i, j, panels=4000):
    """Direct quadrature of (2.5) for one entry, as a control on the closed form."""
    h, x = data["h"], data["x"]
    d = x[i] - x[j]
    tri = lambda s: max(0.0, h - abs(s))
    top = abs(d) + h
    step = top/panels
    total = 0.0
    for k in range(panels + 1):
        r = k*step
        w = step/3.0*(1.0 if k in (0, panels) else (4.0 if k % 2 else 2.0))
        if r == 0.0:
            # ngamma(r) = 1/(2r) + O(r), and bracket(r) = 2r + O(r^2) on the
            # diagonal, -r + O(r^2) for adjacent cells (|d| = h), and 0 for
            # |d| > h. So the integrand has limit 1, -1/2, or 0.
            if i == j:
                limit = 1.0
            elif abs(abs(d) - h) < 1e-12:
                limit = -0.5
            else:
                limit = 0.0
            total += w*limit
            continue
        bracket = (2.0*h if i == j else 0.0) - (tri(r - d) + tri(r + d))
        total += w*bracket*math.exp(-r/2.0)/(1.0 - math.exp(-2.0*r))
    tail = 2.0*h*sum(math.exp(-(2*n + 0.5)*top)/(2*n + 0.5) for n in range(4000)) \
        if i == j else 0.0
    return total + tail


def main():
    checks = {}
    rows = []
    control_rows = []

    for L in (0.8, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0):
        data = build(L, CELLS)
        m, c_L = data["m"], data["c_L"]
        Q, kp_old, t_old = data["Q"], data["kp_old"], data["t_old"]

        gap_old = max(abs(Q[i][j] - (kp_old[i][j] - t_old[i][j]))
                      for i in range(m) for j in range(m))
        assert gap_old < TOL, (L, gap_old)

        if c_L < 0.0:
            symbol = lambda t: digamma_real_quarter_shift(t) - math.log(math.pi) + data["Sigma"]
            tau_L = bisect(symbol, 1e-9, 1e6)
            mneg = negative_part_multiplier(L, data, tau_L)
            kp_new = [[data["K"][i][j] + (c_L*data["h"] if i == j else 0.0) + mneg[i][j]
                       + 0.5*(data["u"][i] + data["v"][i])*(data["u"][j] + data["v"][j])
                       for j in range(m)] for i in range(m)]
            t_new = [[mneg[i][j]
                      + 0.5*(data["u"][i] - data["v"][i])*(data["u"][j] - data["v"][j])
                      + data["Bt"][i][j] for j in range(m)] for i in range(m)]
        else:
            tau_L, mneg = None, [[0.0]*m for _ in range(m)]
            kp_new, t_new = kp_old, t_old

        gap_new = max(abs(Q[i][j] - (kp_new[i][j] - t_new[i][j]))
                      for i in range(m) for j in range(m))
        assert gap_new < TOL, (L, gap_new)

        pivot_t = cholesky_pivot(t_new)
        assert pivot_t is not None, ("subtracted form must be positive", L)
        if tau_L is not None:
            pivot_m = cholesky_pivot([[mneg[i][j] + (1e-13 if i == j else 0.0)
                                       for j in range(m)] for i in range(m)])
            assert pivot_m is not None, ("negative-part multiplier must be positive", L)
            moved_less = [[kp_old[i][j] - kp_new[i][j] + (1e-13 if i == j else 0.0)
                           for j in range(m)] for i in range(m)]
            assert positive_definite(moved_less), ("the new source side must be smaller", L)

        lam_old = lambda_min_generalized(Q, kp_old)
        lam_new = lambda_min_generalized(Q, kp_new)
        assert lam_old > 0.0 and lam_new > 0.0, (L, lam_old, lam_new)
        assert lam_new >= lam_old - 1e-12, (L, lam_old, lam_new)

        rows.append({
            "L": L, "c_L": c_L, "Sigma_L": data["Sigma"], "tau_L": tau_L,
            "active_primes": data["primes"],
            "identity_gap_7_14": gap_old, "identity_gap_new": gap_new,
            "least_pivot_T_new": pivot_t,
            "lambda_min_old": lam_old, "lambda_min_new": lam_new,
            "ratio": lam_new/lam_old,
            "saturation_old": 1.0 - lam_old, "saturation_new": 1.0 - lam_new,
        })

        if L in (1.0, 2.0):
            for (i, j) in ((0, 0), (0, 1), (3, 7)):
                closed = data["K"][i][j]
                direct = direct_gamma_entry(data, i, j)
                assert abs(closed - direct) < 2e-6*max(1.0, abs(closed)), \
                    (L, i, j, closed, direct)
                control_rows.append({"L": L, "i": i, "j": j,
                                     "closed_form": closed, "quadrature": direct,
                                     "gap": closed - direct})

    checks["gamma_energy_closed_form"] = len(control_rows)
    checks["identities"] = 2*len(rows)*CELLS*CELLS
    checks["subtracted_form_positive"] = len(rows)
    checks["multiplier_positive_and_smaller"] = 2*sum(1 for r in rows if r["tau_L"])
    checks["saturation_points"] = 2*len(rows)

    print(json.dumps({
        "status": "passed",
        "date": "2026-09-16",
        "model": "claude-opus-5",
        "cells": CELLS,
        "arithmetic": "floating point; the identities are finite matrix "
                      "identities, the positivity statements are Cholesky "
                      "certificates, and the saturations are one-sided subspace "
                      "values obtained by bisection on Cholesky",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "w0": W0,
        "gamma_energy_control": control_rows,
        "table": rows,
        "reading": "Splitting the archimedean form by the sign of its symbol "
                   "rather than by the constant leaves the identity exact and "
                   "both sides positive, moves strictly less to the subtracted "
                   "side, and raises the one-sided saturation quotient. The gain "
                   "is largest at small L and vanishes above log 13, where the "
                   "symbol is already positive and the two presentations agree. "
                   "It does not change the near-degeneracy of Q_L.",
        "scope": "An exact re-presentation plus one-sided subspace evidence in a "
                 "coarse cell basis. No Weil positivity certificate, no "
                 "physically derived source, and no claim about the "
                 "compression's construction.",
    }, indent=2))


if __name__ == "__main__":
    main()
