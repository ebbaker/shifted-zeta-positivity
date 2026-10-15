#!/usr/bin/env python3
"""Exact algebra checks for the complete correlation and hybrid formulas.

Drafted for Edward Baker with substantial LLM assistance, 2026-10-15.
Recorded model gpt-6-astra, effort ultra, verified from parent turn metadata.
Uses only Python's standard library and rational complex arithmetic.
The checks do not prove a theta sign or replace analytic domination.
"""
from fractions import Fraction as Q
from math import comb, factorial
import argparse
import hashlib
import json
from pathlib import Path


def cq(value):
    if isinstance(value, tuple):
        return value
    return Q(value), Q(0)


def ca(a, b):
    a, b = cq(a), cq(b)
    return a[0] + b[0], a[1] + b[1]


def cm(a, b):
    a, b = cq(a), cq(b)
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


I = (Q(0), Q(1))


class P:
    """Sparse polynomial over Q(i); all arithmetic and integration exact."""
    def __init__(self, n, terms=None):
        self.n = n
        self.d = {e: cq(c) for e, c in (terms or {}).items() if cq(c) != (0, 0)}

    @classmethod
    def c(cls, n, value):
        return cls(n, {(0,)*n: cq(value)})

    @classmethod
    def var(cls, n, j):
        e = tuple(int(k == j) for k in range(n))
        return cls(n, {e: cq(1)})

    def cast(self, value):
        return value if isinstance(value, P) else P.c(self.n, value)

    def __add__(self, other):
        other = self.cast(other)
        assert other.n == self.n
        d = self.d.copy()
        for e, c in other.d.items():
            d[e] = ca(d.get(e, (0, 0)), c)
        return P(self.n, d)

    __radd__ = __add__

    def __neg__(self):
        return P(self.n, {e: cm(-1, c) for e, c in self.d.items()})

    def __sub__(self, other):
        return self + (-self.cast(other))

    def __rsub__(self, other):
        return self.cast(other) - self

    def __mul__(self, other):
        other = self.cast(other)
        assert other.n == self.n
        d = {}
        for e, c in self.d.items():
            for f, k in other.d.items():
                g = tuple(a+b for a, b in zip(e, f))
                d[g] = ca(d.get(g, (0, 0)), cm(c, k))
        return P(self.n, d)

    __rmul__ = __mul__

    def __pow__(self, k):
        assert isinstance(k, int) and k >= 0
        result = P.c(self.n, 1)
        for _ in range(k):
            result = result * self
        return result

    def deriv(self, j):
        d = {}
        for e, c in self.d.items():
            if e[j]:
                f = list(e)
                f[j] -= 1
                d[tuple(f)] = cm(e[j], c)
        return P(self.n, d)

    def subst(self, values):
        assert len(values) == self.n
        n = values[0].n
        out = P.c(n, 0)
        for e, c in self.d.items():
            term = P.c(n, c)
            for v, power in zip(values, e):
                term = term * v**power
            out = out + term
        return out

    def real(self):
        return P(self.n, {e: (c[0], Q(0)) for e, c in self.d.items()})

    def constant(self):
        assert all(not any(e) for e in self.d)
        return self.d.get((0,)*self.n, (Q(0), Q(0)))


def integral_interval(poly, low, high):
    assert poly.n == 1
    ans = (Q(0), Q(0))
    for (k,), c in poly.d.items():
        ans = ca(ans, cm(c, (high**(k+1)-low**(k+1))/Q(k+1)))
    return ans


def integrate_polygon(poly, U, V):
    """Integrate in (s,r) over u=s+r in [-U,U], y=s-r in [0,V].

    Uses an independent three-piece s-slicing, not rectangle substitution.
    """
    assert poly.n == 2 and 0 < V <= 2*U
    z = P.var(1, 0)
    pieces = [
        (-U/2, (V-U)/2, -U-z, z),
        ((V-U)/2, U/2, z-V, z),
        (U/2, (U+V)/2, z-V, U-z),
    ]
    ans = (Q(0), Q(0))
    for lo, hi, lower, upper in pieces:
        after_r = P.c(1, 0)
        for (a, b), c in poly.d.items():
            after_r += z**a * (upper**(b+1)-lower**(b+1)) * cm(c, Q(1, b+1))
        ans = ca(ans, integral_interval(after_r, lo, hi))
    return ans


CHECKS = []


def check(name, value):
    if not value:
        raise AssertionError(name)
    CHECKS.append(name)


def equal(name, lhs, rhs=0):
    rhs = lhs.cast(rhs)
    check(name, not (lhs-rhs).d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    # Polarization and coordinate/Jacobian constants.
    u, v = [P.var(2, j) for j in range(2)]
    s, r = u, v
    for j in range(6):
        raw = (u*I)**(j+1)*(v*I)**(j+1)
        raw -= Q(1, 2)*((u*I)**j*(v*I)**(j+2)+(v*I)**j*(u*I)**(j+2))
        equal(f"symmetrized_L{j}", raw, Q(1, 2)*(-u*v)**j*(u-v)**2)
        changed = (raw*Q(1, 4)).subst([s+r, s-r])*2
        equal(f"Jacobian_normalization_L{j}", changed, r**2*(r**2-s**2)**j)
    equal("energy_Jacobian", ((1-u*v)*Q(1, 4)).subst([s+r, s-r])*2,
          Q(1, 2)*(1-s**2+r**2))
    equal("coordinate_inverse_u", ((u+v)*Q(1, 2)+(u-v)*Q(1, 2)), u)
    equal("coordinate_inverse_y", ((u+v)*Q(1, 2)-(u-v)*Q(1, 2)), v)

    # Exact time hierarchy at the integrand level.
    for m in range(4):
        for ell in range(7):
            rhs = P.c(2, 0)
            for k in range(ell+1):
                rhs += 2**ell*comb(ell, k)*s**(2*(ell-k))*r**(2*(m+k))
            equal(f"kernel_time_hierarchy_m{m}_ell{ell}",
                  r**(2*m)*(2*(s**2+r**2))**ell, rhs)

    # An independent differential-polynomial proof in the physical jets.
    h = [P.var(7, j) for j in range(7)]
    def dx(p):
        return sum((p.deriv(k)*h[k+1] for k in range(6)), P.c(7, 0))
    def dt(p):
        return sum((-p.deriv(k)*h[k+2] for k in range(5)), P.c(7, 0))
    L0, L1, E = h[1]**2-h[0]*h[2], h[2]**2-h[1]*h[3], h[0]**2+h[1]**2
    equal("independent_jet_heat_identity", dt(L0)+dx(dx(L0)), 2*L1)
    equal("independent_energy_derivative", dt(E)*Q(1, 2), -h[0]*h[2]-h[1]*h[3])

    # Complete/retained hybrid and common-observation stationary algebra.
    g = [P.var(6, j) for j in range(6)]
    H0, H1, H2, H3, N2, N3 = g
    B = -H0*N2-H1*N3
    equal("common_energy_tail", B-(-H0*H2-H1*H3),
          H0*(H2-N2)+H1*(H3-N3))
    equal("hybrid0_off_stationarity", -H0*N2-(H1**2-H0*H2),
          H0*(H2-N2)-H1**2)
    equal("hybrid1_off_stationarity", -H1*N3-(H2**2-H1*H3),
          H1*(H3-N3)-H2**2)
    vals = [P.var(5, k) for k in range(5)]
    equal("common_S0", B.subst([vals[0], P.c(5, 0), vals[1], vals[2], vals[3], vals[4]]),
          -vals[0]*vals[3])
    equal("common_S1_difference",
          (B+H1*N3).subst([vals[0], vals[1], P.c(5, 0), vals[2], vals[3], vals[4]]),
          -vals[0]*vals[3])
    equal("Young_payment_identity", (H0-H1)**2,
          H0**2+H1**2-2*H0*H1)

    # Original common-carrier exponent to original shifted source.
    t, a, d, vv = [P.var(4, k) for k in range(4)]
    equal("source_translation_heat_exponent",
          t*(vv+a*I)**2+t*d**2-2*t*d*(vv+a*I), t*(vv-d+a*I)**2)
    check("source_translation_n4", -Q(1, 2)+9*Q(1, 2) == 4)
    check("source_translation_n2", -Q(1, 2)+5*Q(1, 2) == 2)

    # Gaussian controls: H derivative polynomials, with common H factored out.
    x = P.var(1, 0)
    for alpha in [Q(1, 2), Q(1), Q(3, 2), Q(2)]:
        jets = [P.c(1, 1)]
        for _ in range(3):
            jets.append(jets[-1].deriv(0)-x*(Q(1)/(2*alpha))*jets[-1])
        l0 = jets[1]**2-jets[0]*jets[2]
        l1 = jets[2]**2-jets[1]*jets[3]
        equal(f"Gaussian_L0_alpha{alpha}", l0, Q(1, 2*alpha))
        equal(f"Gaussian_L1_alpha{alpha}", l1,
              Q(1, 2*alpha)*(Q(1, 2*alpha)+x**2*Q(1, 4*alpha**2)))
        # Normalized Fourier moment of s^2 for exp(-2 alpha s^2).
        fourier_s2 = Q(1, 4*alpha)-x**2*Q(1, 4*alpha**2)
        equal(f"Gaussian_energy_kernel_alpha{alpha}",
              1-fourier_s2+Q(1, 4*alpha), jets[0]**2+jets[1]**2)
        equal(f"Gaussian_signed_kernel_alpha{alpha}",
              Q(1, 2*alpha)*(Q(3, 4*alpha)-fourier_s2), l1)

    # Hybrid convolution: compare Taylor coefficients from products of
    # independent rectangle moments against direct polygon integration.
    # Real even w on [-U,U], complex retained source on [0,V]. These are
    # finite algebra controls, not theta-source sign tests.
    z = P.var(1, 0)
    for case, (U, V, a0) in enumerate([
        (Q(1), Q(1), Q(0)), (Q(2), Q(1), Q(1, 3)),
        (Q(1), Q(1, 2), Q(2, 5))
    ]):
        w = 1+z**2
        psi = 1+z*I+2*z**2
        q = -a0+z*I
        equal(f"polygon_area_case{case}",
              P.c(1, integrate_polygon(P.c(2, 1), U, V)), U*V)
        for j in (0, 1):
            degree = 8
            aa, bb = [], []
            for k in range(degree+1):
                aa.append(integral_interval((z*I)**j*w*(z*I)**k*Q(1, 2*factorial(k)), -U, U))
                bb.append(integral_interval(q**(j+2)*psi*(z*I)**k*Q(1, factorial(k)), Q(0), V))
                check(f"full_moment_real_case{case}_j{j}_k{k}", aa[-1][1] == 0)
            for k in range(degree+1):
                direct = Q(0)
                for ell in range(k+1):
                    direct -= aa[ell][0]*bb[k-ell][0]
                base = ((s+r)*I)**j * (-a0+(s-r)*I)**(j+2)
                base *= w.subst([s+r])*psi.subst([s-r])
                transformed = integrate_polygon(
                    -base*(s*cm(2, I))**k*Q(1, factorial(k)), U, V)[0]
                check(f"hybrid_polygon_case{case}_j{j}_Taylor{k}", direct == transformed)

    record = {
        "date": "2026-10-15",
        "purpose": "Exact correlation, physical-energy and retained hybrid-convolution algebra",
        "author": "Drafted for Edward Baker",
        "llm_assistance": True,
        "model": "gpt-6-astra",
        "reasoning_effort": "ultra",
        "configuration_source": "Verified parent turn metadata",
        "arithmetic": "Python standard library fractions.Fraction over Q(i)",
        "passed": len(CHECKS),
        "failed": 0,
        "checks": CHECKS,
        "scope": "Finite exact algebra and polygon moments; no theta sign, quadrature or analytic domination claim",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.output:
        args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({k: record[k] for k in ("passed", "failed", "arithmetic", "script_sha256")}))


if __name__ == "__main__":
    main()
