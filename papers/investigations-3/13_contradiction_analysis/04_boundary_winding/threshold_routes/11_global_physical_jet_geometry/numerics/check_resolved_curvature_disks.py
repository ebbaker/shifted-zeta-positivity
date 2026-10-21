#!/usr/bin/env python3
"""Finite exact checks for GPJ Note 01, 21 October 2026.

Prepared for Edward Baker with substantial LLM assistance.
Recorded authoring model gpt-6-astra (Codex), reasoning effort max.
Uses the standard library; does not evaluate theta or prove analytic limits.
"""
import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, isqrt
from pathlib import Path
import hashlib
import json
import platform


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else Q(0))
                 + (q[i] if i < len(q) else Q(0))
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return trim([c*v for v in p])


def deriv(p):
    return trim([i*p[i] for i in range(1, len(p))] or [Q(0)])


def mul(p, q):
    result = [Q(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i+j] += a*b
    return trim(result)


def hermite(n):
    if n == 0:
        return [Q(1)]
    prev, cur = [Q(1)], [Q(0), Q(1)]
    for k in range(1, n):
        prev, cur = cur, add([Q(0)]+cur, scale(prev, -k))
    return cur


def heat_monomial(n, t):
    p = [Q(0)]*(n+1)
    for k in range(n//2+1):
        p[n-2*k] = Q(factorial(n), factorial(k)*factorial(n-2*k))*(-t)**k
    return trim(p)


@dataclass(frozen=True)
class GQ:
    re: Q = Q(0)
    im: Q = Q(0)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, GQ) else GQ(Q(x))

    def __add__(self, other):
        b = self.coerce(other)
        return GQ(self.re+b.re, self.im+b.im)

    __radd__ = __add__

    def __neg__(self):
        return GQ(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        b = self.coerce(other)
        return GQ(self.re*b.re-self.im*b.im, self.re*b.im+self.im*b.re)

    __rmul__ = __mul__

    def norm2(self):
        return self.re*self.re+self.im*self.im

    def __truediv__(self, other):
        b = self.coerce(other)
        v = self*GQ(b.re, -b.im)
        return GQ(v.re/b.norm2(), v.im/b.norm2())


def evaluate(p, z):
    value = GQ()
    for v in reversed(p):
        value = value*z+v
    return value


def sqrt_interval(q, places=50):
    """Outward rational square-root enclosure using integers only."""
    den = 10**places
    k = isqrt((q.numerator*den*den)//q.denominator)
    lo, hi = Q(k, den), Q(k+1, den)
    require(lo*lo <= q <= hi*hi, "rational square-root bounds")
    return lo, hi


def mass_interval(C, eta):
    require(0 <= eta < 1, "injectivity margin")
    a, b = C*(1-eta), C*(1+eta)
    return a*a/(1+a*a), b*b/(1+b*b)


def finite_controls():
    cases = []
    tau = Q(1, 8)
    for m, d, Y, h, B2, bstar in (
        (2, Q(1,4), Q(1,2), Q(3,4), Q(2), Q(1,2)),
        (3, Q(1,8), Q(5,4), Q(115,64), Q(15,2), Q(45,64)),
    ):
        C = Q(1)
        require(tau*C/m <= d and h > 0 and bstar > 0, "disk prerequisites")
        qbound = B2*C/(m*h)
        eta = (tau*Y*qbound+tau*tau*qbound*qbound)/m
        lo, hi = mass_interval(C, eta)
        expected = Q(1,18) if m == 2 else Q(131,1587)
        require(eta == expected, "displayed eta")
        if m == 2:
            require((lo, hi) == (Q(289,613), Q(361,685)), "double mass interval")
        else:
            require(h == 2-3*Q(1,4)**2-Q(1,4)**3, "cubic scalar floor")
            require(bstar == 6*d-3*d*d, "cubic critical circle")
        cases.append({
            "multiplicity": m, "tau": str(tau), "time": str(tau*tau/2),
            "d": str(d), "Y": str(Y), "direct_scalar_floor": str(h),
            "B2": str(B2), "critical_circle_floor": str(bstar),
            "Q_bound": str(qbound), "eta": str(eta),
            "mass_over_pi": [str(lo), str(hi)],
        })
    t = tau*tau/2
    dl, du = sqrt_interval(t**4+64)
    numerator = t*t-4
    lower, upper = 1+numerator/dl, 1+numerator/du
    require(Q("0.5000076") < lower <= upper < Q("0.5000077"),
            "displayed exact quadratic area bracket")
    require(Q(289,613) < lower and upper < Q(361,685),
            "independent exact area fits G9")
    # Fixed disk R=1 contains two simple roots at this positive time.
    require(1 > 2*t and 1-4*t*t > 0, "whole-disk small-area test fails")
    return {
        "G9_controls": cases,
        "exact_double_disk_radius": str(t),
        "exact_double_mass_over_pi_interval": [str(lower), str(upper)],
        "whole_disk_countercheck": {
            "R": "1", "t": str(t),
            "two_roots_strictly_inside": True,
            "both_roots_simple": True,
            "gauss_area_strictly_above_pi": True,
            "method": "exact discriminant, root-radius and numerator signs",
        },
    }


def algebra_checks():
    # Independent recurrence and heat-operator constructions.
    for m in range(2, 17):
        p = hermite(m)
        dp, ddp = deriv(p), deriv(deriv(p))
        require(add(add(ddp, scale([Q(0)]+dp, -1)), scale(p, m)) == [Q(0)],
                "Hermite equation")
        require(dp == scale(hermite(m-1), m), "Hermite derivative normalization")
        for tau in (Q(1,8), Q(1,16)):
            t = tau*tau/2
            heat = heat_monomial(m, t)
            require(trim([v*tau**j/tau**m for j,v in enumerate(heat)]) == p,
                    "heat sign and sqrt(2t) normalization")
            # d/dt(exp(-t D^2) z^m) = -D^2(exp(-t D^2) z^m).
            dt = [Q(0)]*(m+1)
            for k in range(1, m//2+1):
                dt[m-2*k] = (Q(factorial(m), factorial(k)*factorial(m-2*k))
                              *k*(-1)**k*t**(k-1))
            require(trim(dt) == scale(deriv(deriv(heat)), -1), "heat PDE")

    points = [GQ(Q(0),Q(1)), GQ(Q(1),Q(1,2)), GQ(Q(-1,3),Q(2,3))]
    samples = 0
    for m in range(2, 9):
        for tau in (Q(1,8), Q(1,16)):
            t = tau*tau/2
            # Non-even local factors exercise an asymmetric heat germ.
            hpoly = add(add(heat_monomial(m,t), scale(heat_monomial(m+1,t),Q(1,3))),
                        scale(heat_monomial(m+2,t),Q(1,5)))
            ppoly = add(add(hermite(m), scale(hermite(m+1),tau/3)),
                        scale(hermite(m+2),tau*tau/5))
            for y in points:
                z = tau*y
                h, hz, hzz = [evaluate(poly,z) for poly in
                              (hpoly,deriv(hpoly),deriv(deriv(hpoly)))]
                p, py, pyy = [evaluate(poly,y) for poly in
                              (ppoly,deriv(ppoly),deriv(deriv(ppoly)))]
                require(h == tau**m*p, "asymmetric complete field scaling")
                require(p.norm2() > 0, "test point away from poles")
                F = py/(tau*p)
                Fprime = (pyy/p-(py/p)*(py/p))/m
                S = pyy-y*py+m*p
                require(Fprime+1 == (tau*y*F-tau*tau*F*F+S/p)/m,
                        "complex Riccati identity G10")
                det = h*hzz-hz*hz
                physical = det.norm2()/(h.norm2()+hz.norm2())**2*(tau*tau/m)**2
                pulled = Fprime.norm2()/(1+F.norm2())**2
                require(physical == pulled, "complex area Jacobian and first-jet normalization")
                samples += 1
    return {
        "Hermite_orders": [2,16], "heat_scales": ["1/8","1/16"],
        "asymmetric_orders": [2,8], "complex_rational_samples": samples,
        "verified": ["Hermite ODE and derivative", "independent heat normalization and PDE",
                     "asymmetric complete-germ scaling", "G10 complex Riccati identity",
                     "G2 pullback Jacobian at the original first jet"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    base = Path("papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes")
    references = [
        base/"10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md",
        base/"10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md",
        base/"10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md",
        base/"10_rh_implies_simple_zeros/notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md",
    ]
    # The local note is beside this checker, so staged and installed replays agree.
    note = Path(__file__).resolve().parents[1]/"notes/01_RESOLVED_CURVATURE_DISKS_AND_DIRECT_COMPARISON_20261021.md"
    result = {
        "date": "2026-10-21 America/New_York",
        "prepared_for": "Edward Baker",
        "llm_assistance": "Substantial",
        "authoring_model": "gpt-6-astra", "reasoning_effort": "max",
        "status": "finite exact transcription and control checks; no numerical theta certificate",
        "scope_limit": "Does not establish analytic univalence, convergence, tail estimates, or a global exclusion.",
        "arithmetic": "Python standard-library rational and Gaussian-rational arithmetic; integer square-root enclosures",
        "python": platform.python_version(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "note_sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
        "references_sha256": {str(p): hashlib.sha256((args.repo/p).read_bytes()).hexdigest() for p in references},
        "algebra": algebra_checks(),
        "controls": finite_controls(),
    }
    args.out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"passed", "complex_samples":result["algebra"]["complex_rational_samples"],
                      "control_orders":[2,3], "theta_evaluations":0, "receipt":str(args.out)}))


if __name__ == "__main__":
    main()
