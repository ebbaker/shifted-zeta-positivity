#!/usr/bin/env python3
"""The Weil form as a compression of the gamma energy, with no unproved
positivity anywhere in the presentation.

Standard library only. Prints a JSON record to standard output.

Corollary 7.9 presents Q_L as a compression of a source for the prime-free
form A_L. That presentation needs A_L >= 0, which is Yoshida's theorem below
log 2, Proposition 8.1 above log 7, and open on the compact window between.
It also needs a source for A_L, which no one has.

Both requirements can be removed. Split the pole form by parity, (2.17), and
move its positive half to the source side and its negative half to the
subtracted side:

    K_+[f] = K[E_L f] + (c_L)_+ ||f||^2 + 2 |<cosh(x/2), f>|^2,           (S)
    T_L[f] = (c_L)_- ||f||^2 + 2 |<sinh(x/2), f>|^2
             + sum_{p in P} Bt_{r_p,d_p}[E_L f],                          (T)
    c_L    = w0 + sum_{p in P} kappat_p ,   (c)_+ = max(c,0), (c)_- = max(-c,0),

for any finite prime set P containing every p < e^L. Then

    Q_L[f] = K_+[f] - T_L[f]                                              (I)

identically, and:

* `K_+` is manifestly a positive norm, explicitly
  `K_+ f = ( b^{1/2}(D) E_L f , sqrt2 <cosh(x/2),f> )` in
  `L^2(R) + C`, because the gamma multiplier `b(tau^2)` of (2.6) is
  nonnegative. No theorem is needed for its positivity, and it is the one
  object in the manuscript with an explicit source.
* `T_L` is manifestly positive for every `L`: each of its three terms is
  separately nonnegative, the last by Proposition 7.7. The constant sits on
  whichever side its sign puts it, so no range restriction arises; `c_L <= 0`
  holds exactly for `L < log 13`, which this programme locates, and above that
  the constant simply joins the source.
* So for every `L`, Weil positivity on `I_L` is exactly the single domination
  `T_L <= K_+`, equivalently `||K_+^{-1/2} T_L K_+^{-1/2}|| <= 1`, and `Q_L` is
  a compression of the gamma source. Nothing in the presentation assumes an
  unproved inequality: (8.1) is not needed for it.

FOUR FACTS ARE CHECKED, on the basis of m indicator cells on I_L.

(1) The identity (I), against the manuscript's own `form_matrix` for A_L and
    Q_L, together with the subtraction form (7.18) as a cross-check on the
    mirror matrices built here.
(2) Which side the constant falls on: `c_L` is a step function of L with jumps
    at the primes, and the cumulative sum of kappat crosses `-w0 = 5.3722...`
    at p = 13, so `c_L <= 0` exactly for `L < log 13`.
(3) `T_L >= 0` on the cell basis, above and below that crossing, with its least
    eigenvalue.
(4) The saturation `||K_+^{-1/2} T_L K_+^{-1/2}||` in the cell subspace, by
    power iteration on the generalized problem.

WHAT THIS DOES AND DOES NOT ESTABLISH. (1) and (2) are exact finite
statements. (3) corroborates a positivity that is anyway manifest term by
term. (4) is ONE SIDED: a subspace value above one would certify that the
domination fails, a value below one certifies nothing, and the value is
expected to sit just below one because Q_L is nearly degenerate. No Weil
positivity certificate is claimed, and no field theory is constructed: the
source for K_+ is a Fourier multiplier, not a physically derived preparation.

Written by Claude Opus 5 (Anthropic), 15 September 2026.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_channel_bound import W0, primes_below            # noqa: E402
from check_mirror_subtraction import kappa_tilde            # noqa: E402
from check_prime_free_archimedean import (                  # noqa: E402
    cell_moments, constant_c, form_matrix, gamma_matrix, jacobi_min, solve,
)

CELLS = 40


def mirror_matrix(L, m, p):
    """Bt_{r_p,d_p} on the cell basis: kappat ||F||^2 + 2 d sum_n r^n Re<F,U_{nd}F>."""
    h = L / m
    r, d = p ** -0.5, math.log(p)
    M = [[0.0] * m for _ in range(m)]
    for j in range(m):
        M[j][j] += kappa_tilde(p) * h
    n = 1
    while n * d < L:
        coef = 2 * d * r ** n
        for j in range(m):
            for k in range(m):
                w = 0.0
                for sgn in (1, -1):
                    t = h - abs(n * d - sgn * (j - k) * h)
                    if t > 0:
                        w += 0.5 * t
                M[j][k] += coef * w
        n += 1
    return M


def add(A, B, s=1.0):
    return [[A[j][k] + s * B[j][k] for k in range(len(A))] for j in range(len(A))]


def max_gap(A, B):
    return max(abs(A[j][k] - B[j][k]) for j in range(len(A)) for k in range(len(A)))


def source_and_subtracted(L, m):
    """K_+ and T_L on the cell basis."""
    K, h = gamma_matrix(L, m)
    cosv, sinv, _ = cell_moments(L, m)
    Kp = [[K[j][k] + 2 * cosv[j] * cosv[k] for k in range(m)] for j in range(m)]
    T = [[2 * sinv[j] * sinv[k] for k in range(m)] for j in range(m)]
    cL = constant_c(L)
    for j in range(m):                       # the constant joins whichever side
        Kp[j][j] += max(cL, 0.0) * h         # its sign puts it on
        T[j][j] += max(-cL, 0.0) * h
    for p in primes_below(math.exp(L)):
        T = add(T, mirror_matrix(L, m, p))
    return Kp, T, h, cL


def top_generalized(T, Kp, iters=600):
    """Largest eigenvalue of Kp^{-1} T by power iteration."""
    n = len(T)
    x = [1.0 / (i + 1) for i in range(n)]
    lam = 0.0
    for _ in range(iters):
        Tx = [sum(T[i][k] * x[k] for k in range(n)) for i in range(n)]
        y = solve(Kp, Tx)
        nrm = math.sqrt(sum(t * t for t in y))
        if nrm == 0.0:
            return 0.0
        x = [t / nrm for t in y]
        Tx = [sum(T[i][k] * x[k] for k in range(n)) for i in range(n)]
        Kx = [sum(Kp[i][k] * x[k] for k in range(n)) for i in range(n)]
        lam = sum(x[i] * Tx[i] for i in range(n)) / sum(x[i] * Kx[i] for i in range(n))
    return lam


def main():
    checks = {}

    # ------------------------------------------------------------- fact (2)
    # the constant is a step function of L; locate where it turns nonnegative
    cum, crossing = W0, None
    ladder = []
    for p in primes_below(60):
        cum += kappa_tilde(p)
        ladder.append({"p": p, "c_after": cum})
        if cum > 0 and crossing is None:
            crossing = p
    assert crossing == 13, "the constant does not change sign at p = 13"
    assert constant_c(math.log(13) - 1e-9) < 0 <= constant_c(math.log(13) + 1e-9)
    checks["constant_sign_ladder"] = len(ladder)

    # ---------------------------------------------------- facts (1), (3), (4)
    rows = []
    gaps = 0.0
    for L in (0.5, 0.8, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0):
        m = CELLS
        Kp, T, h, cL = source_and_subtracted(L, m)
        Q, _ = form_matrix(L, m, kind="Q")
        A, _ = form_matrix(L, m, kind="A")

        # (1) the identity Q = K_+ - T, and the subtraction form as a cross-check
        gaps = max(gaps, max_gap(add(Kp, T, -1.0), Q))
        Asub = A
        for p in primes_below(math.exp(L)):
            Asub = add(Asub, mirror_matrix(L, m, p), -1.0)
        gaps = max(gaps, max_gap(Asub, Q))

        # (3) positivity of the subtracted form
        lamT = jacobi_min(T) / h
        # (4) saturation, one sided
        sat = top_generalized(T, Kp)
        rows.append({"L": L, "c_L": cL, "constant_side": "source" if cL > 0 else "subtracted",
                     "lambda_min_T_over_norm": lamT,
                     "saturation_subspace": sat,
                     "lambda_min_Q_over_K_plus": 1.0 - sat})
        assert lamT >= 0, "the subtracted form must be positive"
        assert sat < 1.0, "a subspace saturation above one would certify failure"
    assert gaps < 1e-9, "the identity Q_L = K_+ - T_L failed"
    checks["identity_and_subtraction_form"] = 2 * len(rows) * CELLS * CELLS
    checks["subtracted_form_positive"] = len(rows)
    checks["saturation_points"] = len(rows)

    print(json.dumps({
        "status": "passed",
        "date": "2026-09-15",
        "model": "claude-opus-5",
        "cells": CELLS,
        "arithmetic": "floating point; the identity is a finite matrix identity, "
                      "the saturation is a one-sided subspace value",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "max_identity_gap": gaps,
        "constant_sign_change_at_prime": crossing,
        "constant_ladder": ladder,
        "table": rows,
        "reading": "K_+ is the gamma energy plus the positive half of the pole "
                   "form and is manifestly a norm; T_L is the negative contact, "
                   "the negative half of the pole form and every mirror prime "
                   "reference, and is manifestly positive at every L; the "
                   "constant joins whichever side its sign puts it on, and is "
                   "nonpositive exactly below log 13. Their "
                   "difference is Q_L identically, so Weil "
                   "positivity is the single domination T_L <= K_+ and needs no "
                   "unproved positivity as input. The saturation column is one "
                   "sided and sits just below one because Q_L is nearly "
                   "degenerate; it certifies nothing on its own.",
        "scope": "An exact re-presentation of the target plus one-sided "
                 "subspace evidence. No Weil positivity certificate, no "
                 "physically derived source, and no statement about the "
                 "compression's construction.",
    }, indent=2))


if __name__ == "__main__":
    main()
