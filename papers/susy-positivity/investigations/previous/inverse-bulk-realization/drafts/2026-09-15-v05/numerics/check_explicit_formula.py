#!/usr/bin/env python3
"""Normalization check: the localized Weil form against the sum over zeta zeros.

Standard library only. Prints a JSON record to standard output.

Weil's explicit formula, in the normalization used by the manuscript, states
that W(F * F~) equals the sum of the entire function G(tau) = |F^(tau)|^2 over
the ordinates of the nontrivial zeros. This programme evaluates both sides for
an explicit smooth test function and reports their difference. It is a
labelled floating-point check of the manuscript's conventions -- the gamma
kernel, the constant, the pole term and the prime coefficients together -- and
is not a proof of the explicit formula, nor evidence for the Riemann hypothesis:
the zeros it uses are computed on the critical line by construction.
"""
import cmath
import json
import math

EULER_GAMMA = 0.57721566490153286060651209008240243104215933593992
PSI_QUARTER = -EULER_GAMMA - math.pi / 2 - 3 * math.log(2)
W0 = PSI_QUARTER - math.log(math.pi)
NGAMMA_TERMS = 400


# ---------------------------------------------------------------- zeta zeros
def eta(s, n=48):
    """Dirichlet eta by Borwein's acceleration; accurate for moderate |Im s|."""
    d = [0.0] * (n + 1)
    c = float(n)
    d[0] = c
    for i in range(1, n + 1):
        c *= 2.0 * (n - i + 1) * (n + i - 1) / (i * (2 * i - 1))
        d[i] = d[i - 1] + c
    dn = d[n]
    total = 0.0 + 0.0j
    for k in range(n):
        total += (-1) ** k * (d[k] - dn) / (k + 1) ** s
    return -total / dn


def zeta(s, n=48):
    return eta(s, n) / (1 - 2 ** (1 - s))


def log_gamma(z):
    """Lanczos approximation (g = 7, n = 9)."""
    g = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
         771.32342877765313, -176.61502916214059, 12.507343278686905,
         -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7]
    if z.real < 0.5:
        return cmath.log(cmath.pi / cmath.sin(cmath.pi * z)) - log_gamma(1 - z)
    z -= 1
    x = g[0]
    for i in range(1, 9):
        x += g[i] / (z + i)
    t = z + 7.5
    return 0.5 * math.log(2 * math.pi) + (z + 0.5) * cmath.log(t) - t + cmath.log(x)


def theta(t):
    return (log_gamma(complex(0.25, t / 2))).imag - t * math.log(math.pi) / 2


def hardy_Z(t):
    return (cmath.exp(1j * theta(t)) * zeta(complex(0.5, t))).real


def zeros(count):
    """Ordinates of the first `count` zeros, by sign change and bisection."""
    out, t, step = [], 5.0, 0.05
    prev = hardy_Z(t)
    while len(out) < count:
        t2 = t + step
        cur = hardy_Z(t2)
        if prev == 0.0:
            out.append(t)
        elif prev * cur < 0:
            lo, hi = t, t2
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if hardy_Z(lo) * hardy_Z(mid) <= 0:
                    hi = mid
                else:
                    lo = mid
                if hi - lo < 1e-13:
                    break
            out.append(0.5 * (lo + hi))
        t, prev = t2, cur
    return out


# ------------------------------------------------------------ the test input
class RaisedCosine:
    """F(x) = (1 + cos(2 pi x / L)) / 2 on I_L, zero outside. Smooth enough that
    the zero sum converges rapidly; its Fourier transform is elementary."""

    def __init__(self, L):
        self.L = L
        self.w = 2 * math.pi / L

    def __call__(self, x):
        if abs(x) >= self.L / 2:
            return 0.0
        return 0.5 * (1 + math.cos(self.w * x))

    def hat(self, tau):
        """F^(tau) = -w^2 sin(tau L/2) / (tau (tau^2 - w^2)); removable at 0, +-w."""
        L, w = self.L, self.w
        if abs(tau) < 1e-7:
            return 0.5 * L
        if abs(abs(tau) - w) < 1e-7:
            return 0.25 * L
        return -w * w * math.sin(tau * L / 2) / (tau * (tau * tau - w * w))


# ------------------------------------------------------------------ quadrature
def gauss_legendre(n):
    nodes, weights = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, 0.0
            for j in range(1, n + 1):
                p0, p1 = ((2 * j - 1) * x * p0 - (j - 1) * p1) / j, p0
            dp = n * (x * p0 - p1) / (x * x - 1)
            dx = -p0 / dp
            x += dx
            if abs(dx) < 1e-15:
                break
        nodes.append(x)
        weights.append(2 / ((1 - x * x) * dp * dp))
    return nodes, weights


GL_N, GL_W = gauss_legendre(80)


def integrate(f, a, b, panels=12):
    total = 0.0
    for k in range(panels):
        u = a + (b - a) * k / panels
        v = a + (b - a) * (k + 1) / panels
        for x, w in zip(GL_N, GL_W):
            total += 0.5 * (v - u) * w * f(0.5 * (v - u) * x + 0.5 * (u + v))
    return total


def graded(f, a, b, levels=40):
    """Integrate over [a,b] with panels graded geometrically towards a."""
    total, edges = 0.0, [a] + [a + (b - a) * 2.0 ** (-m) for m in range(levels, -1, -1)]
    for lo, hi in zip(edges, edges[1:]):
        total += integrate(f, lo, hi, panels=1)
    return total


def n_gamma(r):
    return math.exp(-r / 2) / (1 - math.exp(-2 * r))


def primes_below(x):
    out, k = [], 2
    while k < x:
        if all(k % d for d in range(2, int(k ** 0.5) + 1)):
            out.append(k)
        k += 1
    return out


def weil_form(F):
    L = F.L
    corr = {}

    def c(r):
        if r not in corr:
            corr[r] = integrate(lambda x: F(x) * F(x - r), -L / 2 + r, L / 2, panels=24)
        return corr[r]

    n2 = c(0.0)
    K = 2 * graded(lambda r: (n2 - c(r)) * n_gamma(r), 0.0, L)
    K += 2 * n2 * sum(math.exp(-(2 * n + 0.5) * L) / (2 * n + 0.5) for n in range(NGAMMA_TERMS))
    pc = integrate(lambda x: F(x) * math.cosh(x / 2), -L / 2, L / 2, panels=24)
    ps = integrate(lambda x: F(x) * math.sinh(x / 2), -L / 2, L / 2, panels=24)
    poles = 2 * pc ** 2 - 2 * ps ** 2
    prime = 0.0
    for p in primes_below(math.exp(L)):
        d, m = math.log(p), 1
        while m * d < L:
            prime -= 2 * math.log(p) * p ** (-m / 2.0) * c(m * d)
            m += 1
    return {"norm2": n2, "gamma": K, "contact": W0 * n2, "poles": poles,
            "primes": prime, "total": K + W0 * n2 + poles + prime}


def main():
    gam = zeros(60)
    known = [14.134725141734693, 21.022039638771554, 25.010857580145688,
             30.424876125859513, 32.935061587739189]
    errs = [abs(gam[i] - known[i]) for i in range(len(known))]
    assert max(errs) < 1e-9, errs

    cases = []
    for L in (2.0, 3.0, 4.0):
        F = RaisedCosine(L)
        left = weil_form(F)
        partial, running = [], 0.0
        for i, g in enumerate(gam):
            running += 2 * F.hat(g) ** 2          # the zero and its mirror -g
            if i + 1 in (10, 20, 40, 60):
                partial.append({"zeros": i + 1, "sum": running})
        cases.append({
            "L": L, "pieces": left, "zero_sum": running,
            "zero_sum_partials": partial,
            "difference": left["total"] - running,
            "relative_difference": (left["total"] - running) / abs(left["total"]),
            "cancellation_ratio": max(abs(v) for k, v in left.items()
                                      if k not in ("total", "norm2")) / abs(left["total"]),
        })
    assert all(abs(c["difference"]) < 1e-8 for c in cases)

    print(json.dumps({
        "status": "passed",
        "date": "2026-09-15",
        "arithmetic": "floating point; labelled illustration, not an exact check",
        "checks": {"zero_ordinates_against_published_values": len(known),
                   "explicit_formula_cases": len(cases)},
        "total_checks": len(known) + len(cases),
        "zeros_used": len(gam),
        "first_zeros": gam[:5],
        "cases": cases,
        "scope": "Confirms that the manuscript's normalization of the Weil "
                 "functional reproduces the sum over zeta zeros for explicit "
                 "smooth inputs. It does not prove the explicit formula, does "
                 "not verify Weil positivity, and is not evidence for the "
                 "Riemann hypothesis: the ordinates are computed on the "
                 "critical line by construction.",
    }, indent=2))


if __name__ == "__main__":
    main()
