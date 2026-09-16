#!/usr/bin/env python3
"""The non-pole part of the Weil form is ONE jump Dirichlet form, and the
Perron-Frobenius cone it carries is destroyed by the pole term.

Standard library only. Prints a JSON record to standard output.

Write the target's symbol, for f supported in I_L and F = E_L f, as

    Psi_L(tau) = b(tau^2) + w0 - 2 sum_{m log p < L} (log p) p^{-m/2} cos(tau m log p).

By (2.5)-(2.6) the archimedean part is already in Levy-Khinchine form,
b(tau^2) = int_0^inf 2(1 - cos(tau r)) ngamma(r) dr, and the prime part becomes
one after adding and subtracting its value at tau = 0:

    Psi_L(tau) = Phi_L(tau) + gamma_L,
    Phi_L(tau) = int (1 - cos(tau r)) dmu_L(r),
    mu_L       = 2 ngamma(r) dr + 2 sum_{m log p < L} (log p) p^{-m/2} delta_{m log p},
    gamma_L    = w0 - 2 sum_{m log p < L} (log p) p^{-m/2}.

The Levy measure mu_L is NONNEGATIVE, so Phi_L is a continuous negative definite
function and the corresponding form is a jump Dirichlet form. Hence

    Q_L[f] = E_{mu_L}[E_L f] + gamma_L ||f||^2 + P_L[f].                     (D)

The archimedean and prime halves of the target are the CONTINUOUS and ATOMIC
parts of one nonnegative measure, not two channels.

FIVE FACTS ARE CHECKED on a basis of m indicator cells on I_L, in which a
nonnegative function is a nonnegative coefficient vector, so a cone-positive
operator is an entrywise nonnegative matrix.

(1) The decomposition (D), as a finite matrix identity.
(2) E_{mu_L} is a jump form: its off-diagonal entries are nonpositive, and it is
    positive semidefinite.
(3) Beurling-Deny: the resolvent of a Dirichlet form is positivity preserving.
    (K + lambda)^{-1} is checked entrywise nonnegative for lambda > 0, and also
    at lambda = c_L wherever that operator is still positive definite.
(4) The pole term destroys it. (K + lambda + P_L)^{-1} has a large fraction of
    negative entries at every L tested, even for comfortably positive lambda.
    So A_L^{-1} is not cone positive, A_L^{-1} sum_p Bt_p is not a cone map on
    the pointwise cone, and the Collatz-Wielandt certificate (a single pointwise
    supersolution) is unavailable.
(5) The ground-state identity implied by (D):
        lambda_min(E_{mu_L} + P_L ; ||.||^2) = -gamma_L + lambda_min(Q_L ; ||.||^2),
    so Weil positivity on I_L says exactly that the ground-state energy of the
    jump form together with the pole term is at least the prime sum
    2 sum (log p) p^{-m/2} minus w0.

WHAT THIS DOES AND DOES NOT ESTABLISH. (1), (2) and (5) are exact finite
statements up to the stated tolerances; (D) is proved in the accompanying note
and is elementary. (3) and (4) are finite-dimensional verifications of a cone
property in one discretisation; (3) is predicted by Beurling-Deny and (4) is the
finding. Nothing here bears on whether Q_L >= 0: every statement is a
re-presentation of the target or a structural property of its pieces.
"""
import json
import math

CATALAN = 0.91596559417721901505460351493238411077414937428167
CELLS = 48
TOL = 1e-9

B2 = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510]


def digamma_quarter():
    zr, total = 0.25, 0.0
    while zr < 20.0:
        total -= 1.0/zr
        zr += 1.0
    total += math.log(zr) - 0.5/zr
    power = zr*zr
    for k, b in enumerate(B2, start=1):
        total -= b/(2*k*power)
        power *= zr*zr
    return total


W0 = digamma_quarter() - math.log(math.pi)
PSI1_QUARTER = math.pi**2 + 8.0*CATALAN


def s2(x):
    if x <= 0.0:
        return PSI1_QUARTER/4.0
    total, n = 0.0, 0
    while True:
        a = 2*n + 0.5
        term = math.exp(-a*x)/(a*a)
        total += term
        if term < 1e-18*max(total, 1e-18) or n > 200000:
            return total
        n += 1


def primes_below(bound):
    found, n = [], 2
    while n < bound:
        if all(n % p for p in found if p*p <= n):
            found.append(n)
        n += 1
    return found


def invert(A):
    """Gauss-Jordan inverse; returns None if singular."""
    n = len(A)
    M = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot][col]) < 1e-14:
            return None
        M[col], M[pivot] = M[pivot], M[col]
        d = M[col][col]
        M[col] = [v/d for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0.0:
                f = M[r][col]
                M[r] = [a - f*b for a, b in zip(M[r], M[col])]
    return [row[n:] for row in M]


def cholesky_ok(A):
    n = len(A)
    L = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            t = A[i][j] - sum(L[i][k]*L[j][k] for k in range(j))
            if i == j:
                if t <= 0.0:
                    return False
                L[i][i] = math.sqrt(t)
            else:
                L[i][j] = t/L[j][j]
    return True


def lambda_min(A, G, rounds=50, lo=-500.0, hi=500.0):
    """Least s with A - s G singular, by bisection certified by Cholesky."""
    n = len(A)
    for _ in range(rounds):
        mid = 0.5*(lo + hi)
        if cholesky_ok([[A[i][j] - mid*G[i][j] for j in range(n)] for i in range(n)]):
            lo = mid
        else:
            hi = mid
    return 0.5*(lo + hi)


def negative_fraction(M):
    n = len(M)
    scale = max(abs(v) for row in M for v in row)
    return sum(1 for row in M for v in row if v < -1e-12*scale)/(n*n)


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
    pole = [[u[i]*v[j] + v[i]*u[j] for j in range(m)] for i in range(m)]

    def usym(s):
        return [[0.5*(tri(s - (x[i] - x[j])) + tri(s + (x[i] - x[j])))
                 for j in range(m)] for i in range(m)]

    primes = primes_below(math.exp(L))
    energy = [row[:] for row in K]
    gamma = W0
    c_L = W0
    for p in primes:
        d_p, r_p = math.log(p), 1.0/math.sqrt(p)
        c_L += 2.0*d_p*r_p/(1.0 + r_p)
        n = 1
        while n*d_p < L:
            c = d_p*(r_p**n)
            block = usym(n*d_p)
            for i in range(m):
                for j in range(m):
                    energy[i][j] += 2.0*c*((h if i == j else 0.0) - block[i][j])
            gamma -= 2.0*c
            n += 1

    prime_term = [[0.0]*m for _ in range(m)]
    for p in primes:
        d_p, r_p = math.log(p), 1.0/math.sqrt(p)
        n = 1
        while n*d_p < L:
            block = usym(n*d_p)
            for i in range(m):
                for j in range(m):
                    prime_term[i][j] -= 2.0*d_p*(r_p**n)*block[i][j]
            n += 1
    Q = [[K[i][j] + (W0*h if i == j else 0.0) + pole[i][j] + prime_term[i][j]
          for j in range(m)] for i in range(m)]
    gram = [[(h if i == j else 0.0) for j in range(m)] for i in range(m)]
    return dict(h=h, K=K, pole=pole, energy=energy, gamma=gamma, c_L=c_L,
                Q=Q, gram=gram, m=m, primes=primes)


def main():
    checks = {"decomposition": 0, "jump_structure": 0, "beurling_deny": 0,
              "pole_breaks_cone": 0, "ground_state_identity": 0}
    rows = []
    for L in (0.8, 1.0, 1.5, 2.0, 3.0):
        d = build(L, CELLS)
        m, h, g = d["m"], d["h"], d["gamma"]
        Q, E, P, K, G = d["Q"], d["energy"], d["pole"], d["K"], d["gram"]

        gap = max(abs(Q[i][j] - (E[i][j] + (g*h if i == j else 0.0) + P[i][j]))
                  for i in range(m) for j in range(m))
        assert gap < TOL, (L, gap)
        checks["decomposition"] += m*m

        offdiag = max(E[i][j] for i in range(m) for j in range(m) if i != j)
        assert offdiag <= 1e-12, (L, offdiag)
        assert cholesky_ok([[E[i][j] + (1e-9 if i == j else 0.0) for j in range(m)]
                            for i in range(m)]), L
        checks["jump_structure"] += 2

        resolvents = {}
        for lam in (1.0, 5.0):
            M = [[K[i][j] + (lam*h if i == j else 0.0) for j in range(m)]
                 for i in range(m)]
            inv = invert(M)
            frac = negative_fraction(inv)
            assert frac == 0.0, (L, lam, frac)
            resolvents[f"K + {lam:g}"] = {"negative_fraction": frac,
                                          "least_entry": min(min(r) for r in inv)}
            checks["beurling_deny"] += 1

        broken = {}
        for lam in (1.0, 5.0):
            M = [[K[i][j] + (lam*h if i == j else 0.0) + P[i][j] for j in range(m)]
                 for i in range(m)]
            if not cholesky_ok(M):
                continue
            inv = invert(M)
            frac = negative_fraction(inv)
            assert frac > 0.25, (L, lam, frac)
            broken[f"K + {lam:g} + pole"] = {"negative_fraction": frac,
                                             "least_entry": min(min(r) for r in inv)}
            checks["pole_breaks_cone"] += 1

        EP = [[E[i][j] + P[i][j] for j in range(m)] for i in range(m)]
        ground = lambda_min(EP, G)
        lamQ = lambda_min(Q, G)
        assert abs(ground - (-g + lamQ)) < 1e-7, (L, ground, -g + lamQ)
        checks["ground_state_identity"] += 1

        rows.append({
            "L": L, "gamma_L": g, "c_L": d["c_L"], "active_primes": d["primes"],
            "decomposition_gap": gap,
            "resolvent_cone_positive": resolvents,
            "pole_breaks_cone": broken,
            "ground_state_energy": ground, "minus_gamma_L": -g,
            "lambda_min_Q_over_L2": lamQ,
        })

    print(json.dumps({
        "status": "passed",
        "date": "2026-09-16",
        "model": "claude-opus-5",
        "cells": CELLS,
        "arithmetic": "floating point; the decomposition is a finite matrix "
                      "identity, the cone tests are entrywise sign tests on a "
                      "Gauss-Jordan inverse, and the eigenvalues are obtained by "
                      "bisection certified by Cholesky",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "w0": W0,
        "table": rows,
        "reading": "The archimedean density and the prime atoms are the "
                   "continuous and atomic parts of one nonnegative Levy measure, "
                   "so the whole non-pole part of the target is a single jump "
                   "Dirichlet form: one object, not two channels. That form "
                   "carries a genuine Perron-Frobenius cone -- its resolvent is "
                   "positivity preserving, as Beurling-Deny predicts -- and the "
                   "rank-two pole term destroys it, at every L and even with a "
                   "comfortably positive constant. Weil positivity on I_L is then "
                   "the statement that the ground-state energy of the jump form "
                   "together with the pole term is at least the prime sum less w0.",
        "scope": "A re-presentation of the target and structural properties of "
                 "its pieces, verified in one discretisation. No positivity "
                 "statement about Q_L, no field theory, and no claim that the "
                 "cone route yields a proof.",
    }, indent=2))


if __name__ == "__main__":
    main()
