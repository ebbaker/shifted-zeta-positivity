"""v1_pencil.py -- verification of the Calogero--Moser pencil identity

    (e^{-t d^2/dz^2} p)(z) = det(zI - X - tY)

for monic p with distinct roots z_1..z_n, where
    X = diag(z_j),  Y_jk = 2/(z_j - z_k) (j != k),  Y_jj = sum_{k != j} 2/(z_j - z_k).

Checks:
  (1) rank-one relation [X,Y] + 2I = 2J  (J = all-ones)
  (2) coefficient match of both sides for random real and conjugate-pair data,
      n = 2..7, several t values
  (3) Lambda(z^2 + y0^2) = y0^2/2 via the pencil (bisection on reality of spectrum)
  (4) Hermite benchmark: Lambda(He_d, unit root variance) = -1/(2(d-1))
  (5) five k=2 conjugate-pair-pair configurations: pencil threshold vs direct
      root tracking of the heat flow
"""
import numpy as np
from itertools import combinations
from math import comb
import numpy.polynomial.polynomial as npp

rng = np.random.default_rng(20260825)


def cm_pair(roots):
    z = np.asarray(roots, dtype=complex)
    n = len(z)
    X = np.diag(z)
    Y = np.zeros((n, n), dtype=complex)
    for j in range(n):
        for k in range(n):
            if j != k:
                Y[j, k] = 2.0 / (z[j] - z[k])
        Y[j, j] = sum(2.0 / (z[j] - z[k]) for k in range(n) if k != j)
    return X, Y


def heat_coeffs(c_desc, t):
    """e^{-t d^2} applied to poly with descending coeffs c_desc."""
    n = len(c_desc) - 1
    c = np.array(c_desc, dtype=complex)  # c[i] multiplies z^(n-i)
    out = np.zeros_like(c)
    for i in range(n + 1):
        m = n - i  # degree of the monomial
        # e^{-t d^2} z^m = sum_j (-t)^j / j! * m!/(m-2j)! z^{m-2j}
        for j in range(m // 2 + 1):
            fall = 1.0
            for a in range(2 * j):
                fall *= (m - a)
            term = c[i] * (-t) ** j / __import__("math").factorial(j) * fall
            out[i + 2 * j] += term
    return out


def charpoly(M):
    return np.poly(M)  # descending, monic


print("=" * 72)
print("(1)+(2) identity check, n = 2..7")
print("=" * 72)
worst = {}
for n in range(2, 8):
    errs = []
    rerr = []
    for trial in range(4):
        if trial % 2 == 0:
            roots = rng.normal(size=n) * 2  # real
        else:
            roots = []
            m = n
            while m >= 2:
                a, b = rng.normal(size=2)
                roots += [complex(a, abs(b) + 0.3), complex(a, -abs(b) - 0.3)]
                m -= 2
            if m:
                roots.append(complex(rng.normal(), 0))
            roots = np.array(roots)
        X, Y = cm_pair(roots)
        n_ = len(roots)
        R = X @ Y - Y @ X + 2 * np.eye(n_) - 2 * np.ones((n_, n_))
        rerr.append(np.abs(R).max())
        p = np.poly(roots)
        for t in (0.13, -0.4, 0.7 + 0.2j):
            lhs = heat_coeffs(p, t)
            rhs = charpoly(X + t * Y)
            scale = np.abs(lhs).max()
            errs.append(np.abs(lhs - rhs).max() / scale)
    worst[n] = (max(errs), max(rerr))
    print(f"  n={n}:  max rel coeff err {max(errs):.3e}   rank-one resid {max(rerr):.3e}")

print()
print("=" * 72)
print("(3) Lambda(z^2 + y0^2) = y0^2/2 via pencil")
print("=" * 72)


def pencil_lambda(roots, lo=-5.0, hi=5.0, tol=1e-12):
    X, Y = cm_pair(roots)

    def isreal(t):
        ev = np.linalg.eigvals(X + t * Y)
        return np.abs(ev.imag).max() < 1e-9

    assert isreal(hi) and not isreal(lo), "bracket failed"
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if isreal(mid):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


for y0 in (0.5, 1.0, 2.0):
    lam = pencil_lambda([1j * y0, -1j * y0])
    print(f"  y0={y0}:  pencil Lambda = {lam:.12f}   exact {y0**2/2:.12f}   "
          f"err {abs(lam - y0**2/2):.2e}")

print()
print("=" * 72)
print("(4) Hermite benchmark: Lambda = -1/(2(d-1)) at unit root variance")
print("=" * 72)


def he_roots(d):
    # probabilists' Hermite via numpy
    c = np.zeros(d + 1)
    c[d] = 1
    r = npp.polyroots(npp.herme2poly_wrapper(c)) if False else None
    from numpy.polynomial.hermite_e import herme2poly
    cc = herme2poly(c)
    return npp.polyroots(cc)


for d in (4, 6, 8):
    r = he_roots(d)
    r = np.real(r)
    var = np.mean(r ** 2)
    rn = r / np.sqrt(var)
    lam = pencil_lambda(rn, lo=-2.0, hi=1.0)
    print(f"  d={d}:  pencil Lambda = {lam:.10f}   exact {-1/(2*(d-1)):.10f}   "
          f"err {abs(lam + 1/(2*(d-1))):.2e}")

print()
print("=" * 72)
print("(5) k=2 configurations: pencil vs direct root tracking")
print("=" * 72)


def track_lambda(roots, tol=1e-10):
    """Direct: integrate nothing -- just evaluate heat-flowed polynomial's
    root reality by bisection on t, using exact heat action on coefficients."""
    p = np.poly(np.asarray(roots, dtype=complex))

    def isreal(t):
        c = heat_coeffs(p, t)
        rr = np.roots(c)
        return np.abs(rr.imag).max() < 1e-8

    lo, hi = 0.0, 4.0
    assert isreal(hi) and not isreal(lo)
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if isreal(mid):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


configs = [((0.0, 1.0), (3.0, 0.5)),
           ((0.0, 1.0), (0.3, 0.5)),
           ((-1.0, 1.0), (1.0, 1.0)),
           ((0.0, 0.2), (0.25, 0.2)),
           ((0.0, 1.0), (0.0, 0.5))]
recorded = [0.42976, 0.22008, 0.40825, 0.01505, 0.17482]
for (c1, c2), rec in zip(configs, recorded):
    roots = [complex(c1[0], c1[1]), complex(c1[0], -c1[1]),
             complex(c2[0], c2[1]), complex(c2[0], -c2[1])]
    lam_p = pencil_lambda(roots, lo=0.0, hi=4.0)
    lam_t = track_lambda(roots)
    print(f"  {c1} {c2}:  pencil {lam_p:.5f}   tracking {lam_t:.5f}   "
          f"recorded {rec:.5f}   |diff| {abs(lam_p-lam_t):.1e}")
