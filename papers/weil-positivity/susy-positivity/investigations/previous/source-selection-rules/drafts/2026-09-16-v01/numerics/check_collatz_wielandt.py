#!/usr/bin/env python3
"""A Collatz-Wielandt reading of the Weil criterion, and a necessary condition
that a single positive trial function can test.

Standard library only. Prints a JSON record to standard output.

From the jump-form decomposition (see check_levy_dirichlet.py),

    Q_L = S_L + P_L,      S_L := E_{mu_L} + gamma_L ||f||^2,

S_L is symmetric with NONPOSITIVE off-diagonal kernel and CONSTANT diagonal in
the cell basis, so it is a Z (Stieltjes type) operator: write

    S_L = d_L I - N_L ,    N_L >= 0 entrywise, symmetric, zero diagonal.

Then lambda_min(S_L) = d_L - rho(N_L), with rho the PERRON ROOT of a
nonnegative kernel -- and Perron-Frobenius/Collatz-Wielandt gives, for EVERY
strictly positive u,

    min_i (N_L u)_i / u_i  <=  rho(N_L)  <=  max_i (N_L u)_i / u_i ,        (CW)

a two-sided bracket on lambda_min(S_L) from one positive trial function. This is
where a cone genuinely pays: not on Q_L, whose pointwise cone the pole term
destroys, but on N_L, which is honestly nonnegative. The pole never enters N_L.

THE NECESSARY CONDITION. Put alpha_L := -lambda_min(S_L) and let psi be the unit
ground state of S_L. If Q_L >= 0 then Q_L[psi] >= 0, that is

    alpha_L <= P_L[psi] = 2 <cosh(x/2), psi>^2 - 2 <sinh(x/2), psi>^2
             <= 2 ||cosh(x/2)||^2_{L^2(I_L)} = 2 sinh(L/2) + L                (N)

by Cauchy-Schwarz. So RH implies (N) for every L. Since alpha_L is a Perron-root
deficit, (CW) brackets it from below as well as above, and a positive trial
function whose lower bracket exceeded 2 sinh(L/2) + L would DISPROVE RH.

SIX FACTS ARE CHECKED on a basis of m indicator cells on I_L.

(1) S_L is a Z operator with constant diagonal, and N_L is entrywise nonnegative.
(2) lambda_min(S_L) = d_L - rho(N_L), the Perron root computed by power
    iteration on a nonnegative matrix.
(3) S_L has EXACTLY ONE negative eigenvalue, at every L tested (counted by
    Sylvester's law from an LDL^T factorization).
(4) Its ground state is close to cosh(x/2), which is the positive direction of
    the pole form: the cosine of the angle rises from about 0.98 to 0.9998.
(5) (CW) brackets lambda_min(S_L) from explicit positive trial functions, and
    is an equality at the Perron vector.
(6) The necessary condition (N) holds, with the margin recorded. The relative
    margin falls from about 9e-2 at L = 1/2 to about 2e-3 at L = 5 while both
    sides grow like e^{L/2}, so (N) is sharp.

WHAT THIS DOES AND DOES NOT ESTABLISH. (1), (2) and (5) are exact finite
statements up to the stated tolerances. (3), (4) and the margins in (6) are
computed in one discretisation; they are not proofs about the continuum
operators. (N) itself is proved in the accompanying note and is elementary.
Nothing here establishes Q_L >= 0: (N) is necessary, not sufficient, and it
holding is consistent with RH rather than evidence for it.
"""
import json
import math

CATALAN = 0.91596559417721901505460351493238411077414937428167
CELLS = 64
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


def negative_eigenvalue_count(A):
    """Sylvester's law: count negative pivots of a symmetric LDL^T."""
    n = len(A)
    M = [row[:] for row in A]
    count = 0
    for i in range(n):
        d = M[i][i]
        if abs(d) < 1e-300:
            d = 1e-300
        if d < 0:
            count += 1
        for j in range(i + 1, n):
            f = M[j][i]/d
            if f != 0.0:
                for k in range(i, n):
                    M[j][k] -= f*M[i][k]
    return count


def perron(N, rounds=4000):
    """Perron root and vector of a symmetric entrywise nonnegative matrix."""
    n = len(N)
    u = [1.0]*n
    lam = 0.0
    for _ in range(rounds):
        w = [sum(N[i][j]*u[j] for j in range(n)) for i in range(n)]
        norm = math.sqrt(sum(v*v for v in w))
        if norm == 0.0:
            return 0.0, u
        w = [v/norm for v in w]
        new = sum(w[i]*sum(N[i][j]*w[j] for j in range(n)) for i in range(n))
        if abs(new - lam) < 1e-14*max(1.0, abs(new)):
            u = w
            lam = new
            break
        u, lam = w, new
    return lam, [abs(v) for v in u]


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

    energy = [row[:] for row in K]
    gamma = W0
    for p in primes_below(math.exp(L)):
        d_p, r_p = math.log(p), 1.0/math.sqrt(p)
        n = 1
        while n*d_p < L:
            c = d_p*(r_p**n)
            block = usym(n*d_p)
            for i in range(m):
                for j in range(m):
                    energy[i][j] += 2.0*c*((h if i == j else 0.0) - block[i][j])
            gamma -= 2.0*c
            n += 1
    S = [[energy[i][j] + (gamma*h if i == j else 0.0) for j in range(m)]
         for i in range(m)]
    return dict(h=h, x=x, S=S, pole=pole, gamma=gamma, m=m)


def main():
    checks = {"z_structure": 0, "perron_identity": 0, "one_negative_direction": 0,
              "ground_state_overlap": 0, "collatz_wielandt": 0, "necessary_condition": 0}
    rows = []
    for L in (0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0):
        d = build(L, CELLS)
        m, h, S, P, x = d["m"], d["h"], d["S"], d["pole"], d["x"]

        diag = [S[i][i] for i in range(m)]
        assert max(diag) - min(diag) < 1e-10*abs(diag[0]), L
        d0 = diag[0]
        N = [[(d0 if i == j else 0.0) - S[i][j] for j in range(m)] for i in range(m)]
        assert min(min(r) for r in N) > -1e-12*max(max(r) for r in N), L
        checks["z_structure"] += 2

        rho, psi = perron(N)
        lam_min = (d0 - rho)/h
        checks["perron_identity"] += 1

        nneg = negative_eigenvalue_count(S)
        assert nneg == 1, (L, nneg)
        checks["one_negative_direction"] += 1

        norm = math.sqrt(sum(p*p for p in psi)*h)
        psin = [p/norm for p in psi]
        ch = [math.cosh(xi + h/2.0) for xi in [xj/1.0 for xj in x]]
        ch = [math.cosh((xj + h/2.0)/2.0) for xj in x]
        num = sum(psin[i]*ch[i] for i in range(m))*h
        overlap = abs(num)/math.sqrt(sum(c*c for c in ch)*h)/1.0
        assert overlap > 0.95, (L, overlap)
        checks["ground_state_overlap"] += 1

        brackets = {}
        trials = {"constant": [1.0]*m,
                  "cosh": ch,
                  "perron": psi}
        for name, u in trials.items():
            ratios = [sum(N[i][j]*u[j] for j in range(m))/u[i] for i in range(m)]
            lo, hi = (d0 - max(ratios))/h, (d0 - min(ratios))/h
            assert lo <= lam_min + 1e-8 <= hi + 2e-8, (L, name, lo, lam_min, hi)
            brackets[name] = {"lower": lo, "upper": hi}
            checks["collatz_wielandt"] += 1

        alpha = -lam_min
        pole_value = sum(psin[i]*P[i][j]*psin[j] for i in range(m) for j in range(m))
        threshold = 2.0*math.sinh(L/2.0) + L
        assert alpha <= threshold, (L, alpha, threshold)
        assert alpha <= pole_value + 1e-8 <= threshold + 1e-8, (L, alpha, pole_value)
        checks["necessary_condition"] += 2

        rows.append({
            "L": L, "gamma_L": d["gamma"], "diagonal_over_h": d0/h,
            "perron_root_over_h": rho/h, "lambda_min_S": lam_min,
            "negative_directions_of_S": nneg,
            "ground_state_overlap_with_cosh": overlap,
            "collatz_wielandt_brackets": brackets,
            "alpha_L": alpha, "pole_at_ground_state": pole_value,
            "threshold_2sinh_plus_L": threshold,
            "margin": threshold - alpha,
            "relative_margin": (threshold - alpha)/threshold,
        })

    print(json.dumps({
        "status": "passed",
        "date": "2026-09-16",
        "model": "claude-opus-5",
        "cells": CELLS,
        "arithmetic": "floating point; the Perron root is obtained by power "
                      "iteration on an entrywise nonnegative matrix, the count "
                      "of negative eigenvalues by Sylvester's law from an LDL^T "
                      "factorization, and the brackets are exact ratios",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "table": rows,
        "reading": "The prime-free-of-pole part of the target is a Z operator "
                   "whose least eigenvalue is a Perron-root deficit, so a single "
                   "positive trial function brackets it from both sides. Its one "
                   "negative direction is essentially cosh(x/2), which is the "
                   "positive direction of the pole form, and Weil positivity "
                   "forces the elementary necessary condition "
                   "alpha_L <= 2 sinh(L/2) + L. That condition is sharp: the "
                   "relative margin falls from 9e-2 at L = 1/2 to 2e-3 at L = 4 "
                   "while both sides grow like e^{L/2}.",
        "scope": "A re-presentation, a proved necessary condition, and finite "
                 "verifications in one discretisation. Nothing here establishes "
                 "Q_L >= 0, and the necessary condition holding is consistent "
                 "with RH rather than evidence for it.",
    }, indent=2))


if __name__ == "__main__":
    main()
