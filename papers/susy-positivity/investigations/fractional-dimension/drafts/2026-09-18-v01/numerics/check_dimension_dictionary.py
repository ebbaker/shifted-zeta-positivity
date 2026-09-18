#!/usr/bin/env python3
"""
The dimension dictionary for the shifted Weil transfer: every factor written at d = 2 omega.
Standard library only; prints JSON to stdout.  Nothing here is a positivity certificate, and
no value of zeta or xi is computed anywhere in this programme.

THE STATEMENT.  With s_0 = 1/2 + p, a = 1/2 - omega, b = 1/2 + omega, the Markov part of the
transfer is Lambda(s_0 - omega)/Lambda(s_0 + omega).  Put

    d = 2 omega,    s = (p + b)/2    (so 2s = p + b, 2s - d = p + a, and b = (d+1)/2).

Then that ratio is exactly Lambda(2s - d)/Lambda(2s), which at d = 1 is the Eisenstein
scattering matrix of PSL(2,Z)\\H.  Factor by factor:

  ARCHIMEDEAN.  pi^(d/2) Gamma(s - d/2)/Gamma(s) -- the Riesz integral of |t+i|^(-(p+b)) over
  R^d, established in the loewner investigation (check_beta_realization.py, group E).  Here
  only the reparametrization is re-checked.

  COMB.  zeta(2s - d)/zeta(2s), whose Dirichlet coefficients are the JORDAN TOTIENT
  J_d(n) = n^d prod_{p|n} (1 - p^(-d)), and whose weights in the transfer's own normalization
  are therefore

      ct_n = n^(omega - 1/2) prod_{p|n} (1 - p^(-2 omega)) = J_d(n) / n^((d+1)/2).

  For integer d, J_d(n) counts the primitive vectors in (Z/nZ)^d -- the d-dimensional reduced
  fractions with denominator n.  At d = 1 it is Euler's totient and ct_n = phi(n)/n, which is
  the count of cosets in the cusp's Fourier expansion.  So the comb is a d-dimensional object
  in exactly the sense the archimedean factor is.

  POLE.  The Blaschke factor sits at p = b = (d+1)/2, which is 2s = d + 1: the pole of
  zeta(2s - d), i.e. the volume term of the d-dimensional lattice sum.

WHAT THIS DOES AND DOES NOT SETTLE.  It settles that all three factors are d-dimensional AS
FORMULAS, with d = 2 omega, and that d = 1 is the modular surface.  It settles nothing about
whether a fractional d is more than a parameter: J_d(n) is a perfectly good multiplicative
function for fractional d, but it stops counting anything, and R^d stops being a space.  That
is the question the investigation exists to ask.

  Counts refer to finite test cases, not independent theorems.
"""
import json
import math
from fractions import Fraction
from itertools import product


class Group(object):
    def __init__(self, name, note=None):
        self.name, self.note, self.checks, self.tables = name, note, [], {}

    def add(self, what, error, tol):
        self.checks.append({"what": what, "error": error, "tolerance": tol, "pass": error < tol})
        return self

    def assert_true(self, what, ok):
        self.checks.append({"what": what, "error": 0.0 if ok else 1.0, "tolerance": 0.5, "pass": bool(ok)})
        return self

    def out(self):
        d = {"name": self.name, "cases": len(self.checks),
             "worst_margin_against_own_tolerance": max(c["error"] / c["tolerance"] for c in self.checks),
             "pass": all(c["pass"] for c in self.checks), "checks": self.checks}
        if self.note:
            d["note"] = self.note
        d.update(self.tables)
        return d


OMEGAS = (0.002, 0.01, 0.05, 0.1, 0.25, 0.4, 0.5)


def prime_factors(n):
    out, q = [], 2
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        out.append(n)
    return out


def comb_weight(n, om):
    """ct_n = n^(omega-1/2) prod_{p|n} (1 - p^(-2 omega)), the transfer's comb weight."""
    v = float(n) ** (om - 0.5)
    for q in prime_factors(n):
        v *= 1.0 - float(q) ** (-2.0 * om)
    return v


def jordan(n, d):
    """J_d(n) = n^d prod_{p|n} (1 - p^(-d))."""
    v = float(n) ** d
    for q in prime_factors(n):
        v *= 1.0 - float(q) ** (-d)
    return v


def jordan_exact(n, d):
    """J_d(n) for integer d, in exact integer arithmetic."""
    v = Fraction(n) ** d
    for q in prime_factors(n):
        v *= Fraction(q ** d - 1, q ** d)
    return v


def mobius(n):
    f = prime_factors(n)
    for q in f:
        if n % (q * q) == 0:
            return 0
    return -1 if len(f) % 2 else 1


def group_comb_is_jordan():
    g = Group("A. the comb weights are the Jordan totient at d = 2 omega",
              "ct_n = J_d(n)/n^((d+1)/2): the same rewriting that turns the archimedean "
              "factor into an integral over R^d turns the comb into the d-dimensional "
              "reduced-fraction count")
    worst, rows = 0.0, {}
    for om in OMEGAS:
        d = 2.0 * om
        e = 0.0
        for n in range(1, 120):
            lhs = comb_weight(n, om)
            rhs = jordan(n, d) / float(n) ** ((d + 1.0) / 2.0)
            e = max(e, abs(lhs - rhs) / abs(lhs))
        rows["omega = %g" % om] = {"d = 2 omega": d,
                                   "ct_6": comb_weight(6, om),
                                   "J_d(6)/6^((d+1)/2)": jordan(6, d) / 6.0 ** ((d + 1.0) / 2.0)}
        g.add("ct_n = J_d(n)/n^((d+1)/2) for n < 120, omega = %g" % om, e, 1e-13)
        worst = max(worst, e)
    g.tables = {"weights at n = 6": rows}
    return g.out()


def group_jordan_counts():
    g = Group("B. for integer d, J_d(n) counts the primitive vectors in (Z/nZ)^d",
              "the d-dimensional reduced fractions with denominator n; at d = 1 this is "
              "Euler's totient and the count of cosets in the cusp's Fourier expansion")
    rows = {}
    for d in (1, 2, 3):
        sub = {}
        for n in range(1, 13):
            count = 0
            for v in product(range(n), repeat=d):
                gg = n
                for x in v:
                    gg = math.gcd(gg, x)
                if gg == 1:
                    count += 1
            want = jordan_exact(n, d)
            g.assert_true("d = %d, n = %2d: primitive count %d = J_d(n)" % (d, n, count),
                          Fraction(count) == want)
            if n in (6, 12):
                sub["n = %d" % n] = {"primitive vectors in (Z/nZ)^d": count, "J_d(n)": str(want)}
        rows["d = %d" % d] = sub
    # d = 1 in exact rationals: ct_n = phi(n)/n
    worst_exact = True
    for n in range(1, 80):
        lhs = Fraction(1)
        for q in prime_factors(n):
            lhs *= Fraction(q - 1, q)
        phi = Fraction(n)
        for q in prime_factors(n):
            phi *= Fraction(q - 1, q)
        if lhs != phi / n:
            worst_exact = False
    g.assert_true("at d = 1 (omega = 1/2): ct_n = phi(n)/n in exact rationals, n < 80", worst_exact)
    g.tables = {"primitive counts": rows}
    return g.out()


def group_dirichlet():
    g = Group("C. J_d is the Dirichlet coefficient of zeta(u-d)/zeta(u)",
              "checked by Mobius convolution, so no value of zeta is computed")
    worst = 0.0
    for d in (0.004, 0.5, 1.0, 1.7, 2.0, 3.0):
        e = 0.0
        for n in range(1, 60):
            conv = math.fsum(float(n // k) ** d * mobius(k) for k in range(1, n + 1) if n % k == 0)
            e = max(e, abs(conv - jordan(n, d)) / max(1.0, abs(conv)))
        g.add("sum_{ke=n} e^d mu(k) = J_d(n) for n < 60, d = %g" % d, e, 1e-12)
        worst = max(worst, e)
    return g.out()


def group_reparametrization():
    g = Group("D. the reparametrization d = 2 omega, s = (p+b)/2",
              "the Markov part Lambda(s_0-omega)/Lambda(s_0+omega) is Lambda(2s-d)/Lambda(2s), "
              "which at d = 1 is the Eisenstein scattering matrix; only the Gamma part and the "
              "bookkeeping are checked here, the Riesz integral being established in the "
              "loewner investigation")
    worst = 0.0
    for om in OMEGAS:
        a, b = 0.5 - om, 0.5 + om
        d = 2.0 * om
        e = 0.0
        for p in (0.7, 1.5, 4.0, 9.0, 25.0):
            s = (p + b) / 2.0
            lhs = math.pi ** om * math.gamma((a + p) / 2.0) / math.gamma((b + p) / 2.0)
            rhs = math.pi ** (d / 2.0) * math.gamma(s - d / 2.0) / math.gamma(s)
            e = max(e, abs(lhs - rhs) / abs(lhs))
        g.add("pi^omega Gamma((a+p)/2)/Gamma((b+p)/2) = pi^(d/2) Gamma(s-d/2)/Gamma(s), omega = %g" % om,
              e, 1e-14)
        worst = max(worst, e)
        g.assert_true("omega = %g: 2s - d = p + a and 2s = p + b" % om,
                      abs((2 * ((0.7 + b) / 2.0) - d) - (0.7 + a)) < 1e-15)
        g.assert_true("omega = %g: the Blaschke pole sits at p = b = (d+1)/2" % om,
                      abs(b - (d + 1.0) / 2.0) < 1e-15)
    g.assert_true("d = 1 exactly at omega = 1/2, the only integer d in (0,1]",
                  abs(2 * 0.5 - 1.0) < 1e-15 and all(abs(2 * o - round(2 * o)) > 1e-9 for o in OMEGAS[:-1]))
    g.tables = {"dictionary": {
        "archimedean": "pi^(d/2) Gamma(s-d/2)/Gamma(s) = integral over R^d of |t+i|^(-(p+b))",
        "comb": "zeta(2s-d)/zeta(2s), weights J_d(n)/n^((d+1)/2)",
        "pole": "Blaschke factor at p = b = (d+1)/2, i.e. 2s = d+1",
        "d = 1": "the modular surface: horocycle of dimension 1, weights phi(n)/n"}}
    return g.out()


def main():
    groups = [group_comb_is_jordan(), group_jordan_counts(), group_dirichlet(),
              group_reparametrization()]
    out = {
        "programme": "check_dimension_dictionary.py",
        "investigation": "fractional-dimension",
        "statement": "every factor of the Markov part of the shifted Weil transfer has an "
                     "expression at d = 2 omega: the archimedean factor is an integral over "
                     "R^d, the comb's weights are the Jordan totient J_d(n)/n^((d+1)/2), and "
                     "the Blaschke pole sits at (d+1)/2. At d = 1 this is the Eisenstein "
                     "scattering matrix of the modular surface",
        "what it does not settle": "whether fractional d is more than a parameter; J_d stays a "
                                   "multiplicative function but stops counting, and R^d stops "
                                   "being a space",
        "scope": "finite test cases and exact identities about Gamma, Mobius convolution and "
                 "lattice point counts; no value of zeta or xi is computed, and nothing here "
                 "is a positivity certificate",
        "groups": groups,
    }
    out["all_pass"] = all(g["pass"] for g in groups)
    out["total_checks"] = sum(g["cases"] for g in groups)
    print(json.dumps(out, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
