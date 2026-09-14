"""Reproduce Round 1 diagnostics. Python 3 + NumPy; no zeta-zero archive.

These floating-point checks are diagnostics, not interval certificates.
Analytic statements and their proofs are in INVESTIGATION_round1.md.
"""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

EULER = 0.577215664901532860606512090082402431
W0 = -EULER - math.pi / 2 - 3 * math.log(2) - math.log(math.pi)


def j(t):
    return np.exp(-t / 2) / (-np.expm1(-2 * t))


def R(t):
    return 2 * np.cosh(t / 2) - j(t)


def tail(a):
    r = np.exp(-a / 2)
    return np.arctanh(r) + np.arctan(r)


def quad_rule(a, b, n):
    z, w = leggauss(n)
    return (a + b) / 2 + (b - a) * z / 2, (b - a) * w / 2


def digamma(z):
    """Recurrence into a right half-plane, followed by an asymptotic series."""
    correction = 0j
    while z.real < 32:
        correction -= 1 / z
        z += 1
    coeffs = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730]
    ans = cmath.log(z) - 1 / (2 * z)
    for k, b in enumerate(coeffs, 1):
        ans -= b / (2 * k * z ** (2 * k))
    return ans + correction


def multiplier_checks():
    rows = []
    for tau in [0.0, 0.5, 1.0, 3.0, 10.0]:
        integ = 0.0
        for a, b in zip([0, 1, 2, 4, 8, 16, 32, 64], [1, 2, 4, 8, 16, 32, 64, 128]):
            t, w = quad_rule(a, b, 128)
            integ += np.dot(w, 4 * j(t) * np.sin(tau * t / 2) ** 2)
        direct = digamma(0.25 + 0.5j * tau).real - math.log(math.pi)
        rows.append(dict(tau=tau, direct=direct, jump=W0 + integ,
                         absolute_difference=abs(direct - W0 - integ)))
    assert max(r['absolute_difference'] for r in rows) < 2e-11
    return rows


def gamma_check(L, omega, n):
    x, w = quad_rule(-L / 2, L / 2, n)

    def raw(xx):
        y = 2 * xx / L
        return (1 - y * y) ** 3 * (1 + 0.35 * y + 0.2j * y * y)

    scale = math.sqrt(float(np.dot(w, np.abs(raw(x)) ** 2)))

    def f(xx):
        return raw(xx) / scale

    fx = f(x)
    norm = float(np.dot(w, abs(fx) ** 2))
    C = np.dot(w, fx * np.cosh(x / 2))
    S = np.dot(w, fx * np.sinh(x / 2))

    # Independent 1D autocorrelation route, with exact polynomial inner quadrature.
    t, wt = quad_rule(0, L, n)
    u, wu = leggauss(12)
    xx = -t[:, None] / 2 + (L - t[:, None]) * u[None, :] / 2
    corr = (L - t) / 2 * ((np.conj(f(xx + t[:, None])) * f(xx)) @ wu)
    base = W0 * norm + np.dot(wt, 2 * j(t) * (norm - corr.real))
    base += 2 * norm * float(tail(L)) + 2 * abs(C) ** 2 - 2 * abs(S) ** 2
    shift = np.dot(wt, 4 * np.sinh(omega * t / 2) ** 2 * R(t) * corr.real)
    target = float(base + shift)

    # Explicit difference-factor route. Integrate the triangle x<y using t=y-x,
    # so the weak diagonal cusp does not degrade a square-grid quadrature.
    squared_difference = abs(f(xx + t[:, None]) - f(xx)) ** 2
    difference_integral = (L-t) / 2 * (squared_difference @ wu)
    h = -R(t)
    edge = float(np.dot(wt, np.cosh(omega*t) * h * difference_integral))
    kappa = W0 + tail(x + L / 2) + tail(L / 2 - x)
    kappa += 8 * math.sinh(L / 4) * np.cosh(x / 2)
    v, wv = quad_rule(0, 1, 64)
    for length in [x+L/2, L/2-x]:
        d = length[:, None] * v[None, :]
        row_integral = length * ((-2*np.sinh(omega*d/2)**2 * R(d)) @ wv)
        kappa -= row_integral
    potential = float(np.dot(w, kappa * abs(fx) ** 2))
    return dict(L=L, omega=omega, nodes=n, target=target, edge=edge,
                potential=potential, factor_form=edge + potential,
                absolute_difference=abs(target - edge - potential),
                sampled_kappa_min=float(kappa.min()),
                all_off_diagonal_edge_weights_positive=bool(np.all(h >= 0)))


def prime_checks():
    # At L = 3 log(2)/2 < log(3), only n=2 is active. A six-cell shift
    # on nine cells gives the exact block algebra of the two paired end regions.
    c = math.log(2) / math.sqrt(2)
    T = np.zeros((9, 9))
    for k in range(3):
        T[k + 6, k] = 1
    P, F = T.T @ T, T @ T.T
    B = math.sqrt(c) * (P - T.T)
    target = c * (P + F - T - T.T)
    arithmetic = -c * (T + T.T)
    rng = np.random.default_rng(20260911)
    v = rng.normal(size=9) + 1j * rng.normal(size=9)
    a, b = 0.7, 1.1
    X = a * np.eye(9) - b * T
    error = np.max(abs(X.T @ X - (a*a*np.eye(9) + b*b*P - a*b*(T+T.T))))
    ans = dict(c=c, total_length=1.5*math.log(2),
               nilpotent_error=float(np.max(abs(T @ T))),
               full_shift_identity_error=float(error),
               edge_identity_error=float(np.max(abs(B.T @ B - target))),
               complex_vector_identity_error=float(abs(np.vdot(B @ v, B @ v) - np.vdot(v, target @ v))),
               arithmetic_eigenvalues=np.linalg.eigvalsh(arithmetic).tolist(),
               forced_diagonal=np.diag(c * (P + F)).tolist())
    assert ans['edge_identity_error'] < 1e-14
    assert ans['complex_vector_identity_error'] < 1e-13
    assert ans['full_shift_identity_error'] < 1e-14
    return ans


def main():
    lo, hi = 0.2, 0.4
    for _ in range(70):
        mid = (lo + hi) / 2
        if float(R(mid)) < 0:
            lo = mid
        else:
            hi = mid
    threshold = (lo + hi) / 2
    c0 = math.log(4 / math.pi) - EULER + 7 / 16
    shift_loss = math.exp(1 / 8) * math.cosh(1 / 8) / 512
    gamma = [gamma_check(L, omega, n) for L, omega in [(0.2, 0), (0.25, 0),
             (0.25, 0.5), (math.log(2), 0)] for n in [96, 192]]
    for row in gamma:
        assert row['absolute_difference'] < 2e-10, row
        if row['L'] <= 0.25:
            assert row['sampled_kappa_min'] > 0.099
            assert row['all_off_diagonal_edge_weights_positive']
    out = dict(status='floating-point diagnostics, not an interval certificate',
               gamma_zero_shift_lower_bound=c0,
               uniform_shift_loss_upper_bound=shift_loss,
               uniform_small_slab_lower_bound=c0-shift_loss,
               kernel_sign_threshold=threshold,
               phase_triangle={'R(0.2)':float(R(0.2)), 'R(0.4)':float(R(0.4)),
                               'cycle_product':float(R(0.2)**2 * R(0.4))},
               multiplier_checks=multiplier_checks(), gamma_checks=gamma,
               first_prime=prime_checks(),
               comb_nonclosability=[{'R':2*math.pi*k, 'L2_norm_squared':1/(3*math.pi*k),
                                     'sampling_norm_squared_exact':1}
                                    for k in [1, 10, 100, 1000]])
    dest = Path(__file__).with_name('diagnostics.json')
    dest.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
