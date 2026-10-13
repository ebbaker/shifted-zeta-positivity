"""
lab_lorentzian_test.py -- does the Lorentzian / Hodge-Riemann signature condition
imply hyperbolicity?  (Test of the bridge proposed in memo4 / memo5.)

Setup.  A univariate real polynomial p(X) = sum_j a_j X^j of degree d with positive
coefficients is hyperbolic iff all roots are real.  Homogenise to the bivariate
form h(x,y) = y^d p(x/y).  For bivariate forms with nonnegative coefficients,
Braenden-Huh "Lorentzian" reduces to: every (d-2)-fold derivative is a 2x2 form
with at most one positive eigenvalue, i.e. det <= 0, i.e.

      c_j^2 >= c_{j-1} c_{j+1}   for all j,      c_j := a_j / binom(d,j)

-- log-concavity of the normalised coefficients = NEWTON'S INEQUALITIES = the
first Turan inequality.  (Support is an interval, so M-convexity is automatic.)

Known: hyperbolic ==> Newton.  Question: does Newton ==> hyperbolic?
If not, the Lorentzian/Hodge-Riemann signature condition is strictly weaker than
hyperbolicity and cannot be a route to it.

Sampling strategy: generate log-concave c directly (c_j = exp(concave sequence)),
so Newton holds BY CONSTRUCTION, then test hyperbolicity.
"""
import numpy as np
from math import comb, exp, log

rng = np.random.default_rng(20260823)


def newton_ok(a, d, tol=0.0):
    c = [a[j] / comb(d, j) for j in range(d + 1)]
    return all(c[j] ** 2 >= c[j - 1] * c[j + 1] - tol for j in range(1, d))


def hyperbolic(a, tol=1e-9):
    # numpy wants highest degree first
    r = np.roots(np.array(a[::-1], dtype=float))
    if len(r) == 0:
        return True
    scale = max(1.0, np.max(np.abs(r)))
    return np.max(np.abs(r.imag)) <= tol * scale


def random_logconcave(d, curv=1.0, noise=0.0):
    """c_j = exp(v_j) with v strictly concave  =>  Newton holds by construction."""
    j = np.arange(d + 1)
    # concave quadratic + random linear tilt; noise kept small enough to stay concave
    v = -curv * (j - d / 2.0) ** 2 / d + rng.normal(0, 1) * (j - d / 2.0) / d
    if noise > 0:
        # second-difference-safe perturbation: add a concave random piece
        w = np.cumsum(np.cumsum(-np.abs(rng.normal(0, noise, d + 1))))
        v = v + w / max(1.0, np.max(np.abs(w)))
    c = np.exp(v - v.max())
    return [c[k] * comb(d, k) for k in range(d + 1)]


print("=" * 78)
print("TEST  Newton/Lorentzian  vs  hyperbolicity, over log-concave samples")
print("=" * 78)
print(f"{'d':>3} {'samples':>8} {'Newton':>8} {'Newton&hyp':>11} {'frac hyp':>10}")
N = 40000
first_ce = {}
for d in range(2, 11):
    nn = nh = 0
    for _ in range(N):
        a = random_logconcave(d, curv=rng.uniform(0.2, 4.0), noise=rng.uniform(0, 0.6))
        if not newton_ok(a, d):
            continue
        nn += 1
        if hyperbolic(a):
            nh += 1
        elif d not in first_ce:
            first_ce[d] = a
    frac = nh / nn if nn else float("nan")
    print(f"{d:>3} {N:>8} {nn:>8} {nh:>11} {frac:>10.4f}")

print()
print("=" * 78)
print("EXPLICIT COUNTEREXAMPLES: Newton holds, roots complex")
print("=" * 78)
for d in sorted(first_ce):
    a = first_ce[d]
    r = np.roots(np.array(a[::-1], dtype=float))
    nc = int(np.sum(np.abs(r.imag) > 1e-9))
    print(f"  d={d}: Newton OK, {nc} nonreal roots "
          f"(max |Im| = {np.max(np.abs(r.imag)):.4g})")

print()
print("=" * 78)
print("MINIMAL CLEAN COUNTEREXAMPLE (small integer coefficients)")
print("=" * 78)
# search small-integer quartics/quintics satisfying Newton with complex roots
found = []
for d in (4, 5):
    for _ in range(400000):
        a = [int(x) for x in rng.integers(1, 30, d + 1)]
        if newton_ok(a, d) and not hyperbolic(a):
            r = np.roots(np.array(a[::-1], dtype=float))
            found.append((d, a, int(np.sum(np.abs(r.imag) > 1e-9)), np.max(np.abs(r.imag))))
            break
for d, a, nc, mi in found:
    c = [a[j] / comb(d, j) for j in range(d + 1)]
    print(f"  d={d}:  p(X) = " + " + ".join(f"{a[j]}X^{j}" for j in range(d, -1, -1)).replace("X^0", "")
          )
    print(f"        normalised c = {[round(x,4) for x in c]}")
    print(f"        Newton ratios c_j^2/(c_{{j-1}}c_{{j+1}}) = "
          f"{[round(c[j]**2/(c[j-1]*c[j+1]),4) for j in range(1,d)]}  (all >= 1 OK)")
    print(f"        nonreal roots: {nc},  max |Im| = {mi:.4g}")

print()
print("=" * 78)
print("CONTROL: hyperbolic ==> Newton  (should never fail)")
print("=" * 78)
bad = 0
for _ in range(20000):
    d = int(rng.integers(2, 9))
    roots = -np.abs(rng.normal(0, 1, d)) - 0.01      # real negative roots
    a = np.poly(roots)[::-1].real.tolist()            # ascending, positive coeffs
    if not newton_ok(a, d, tol=1e-12 * max(a)):
        bad += 1
print(f"  hyperbolic samples violating Newton: {bad} / 20000")
