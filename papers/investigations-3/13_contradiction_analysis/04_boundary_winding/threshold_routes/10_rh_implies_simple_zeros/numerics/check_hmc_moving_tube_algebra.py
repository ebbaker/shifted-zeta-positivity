#!/usr/bin/env python3
"""Frozen exact algebra for HMC-04 / Note 21.

Prepared for Edward Baker, 2026-10-21, with gpt-6-astra / max assistance.
Domain: heat-polynomial degrees 2, 3, 4, 6; one moving rectangular average;
the rational jet and source-frequency fixtures declared below.
Arithmetic: sparse polynomials over fractions.Fraction, no tolerances.
Stop on the first failed identity. No adaptive fixture selection.
This is not a theta quadrature, floor certificate, infinite-product proof,
endpoint-uniform estimate, performance benchmark, or simplicity result.
"""

import argparse
import datetime
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import platform


class Poly:
    """Sparse rational polynomial in (t, x, v)."""

    def __init__(self, terms=0):
        raw = terms if isinstance(terms, dict) else {(0, 0, 0): F(terms)}
        self.terms = {k: F(v) for k, v in raw.items() if v}

    @staticmethod
    def cast(other):
        return other if isinstance(other, Poly) else Poly(other)

    def __add__(self, other):
        out = self.terms.copy()
        for k, v in self.cast(other).terms.items():
            out[k] = out.get(k, F(0)) + v
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        out = {}
        for k, a in self.terms.items():
            for l, b in self.cast(other).terms.items():
                m = tuple(i+j for i, j in zip(k, l))
                out[m] = out.get(m, F(0)) + a*b
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        out = Poly(1)
        for _ in range(n):
            out = out*self
        return out

    def __eq__(self, other):
        return self.terms == self.cast(other).terms

    def d(self, axis):
        out = {}
        for k, a in self.terms.items():
            if k[axis]:
                l = list(k)
                l[axis] -= 1
                out[tuple(l)] = a*k[axis]
        return Poly(out)

    def integral(self, axis):
        out = {}
        for k, a in self.terms.items():
            l = list(k)
            l[axis] += 1
            out[tuple(l)] = a/l[axis]
        return Poly(out)

    def at(self, axis, replacement):
        replacement = self.cast(replacement)
        out = Poly()
        for k, a in self.terms.items():
            l = list(k)
            n, l[axis] = l[axis], 0
            out += Poly({tuple(l): a}) * replacement**n
        return out

    def between(self, axis, lo, hi):
        p = self.integral(axis)
        return p.at(axis, hi)-p.at(axis, lo)

    def average_v(self, eta):
        out = Poly()
        for (j, k, n), a in self.terms.items():
            if n % 2 == 0:
                out += Poly({(j, k, 0): a/F(n+1)}) * eta**n
        return out


t, x, v = [Poly({tuple(int(i == j) for i in range(3)): 1}) for j in range(3)]


def heat_jet(m, primitive=False):
    real, imag = Poly(), Poly()
    for j in range(m//2+1):
        degree = m-2*j
        coeff = F((-1)**j*factorial(m), factorial(j)*factorial(degree))
        if primitive:
            degree += 1
            coeff /= degree
        for k in range(degree+1):
            term = Poly({(j, degree-k, k): coeff*comb(degree, k)*(-1)**(k//2)})
            if k % 2:
                imag += term
            else:
                real += term
    return real, imag


def real_pair(f, g):
    return f[0]*g[0]+f[1]*g[1]


def imag_pair(f, g):
    return f[1]*g[0]-f[0]*g[1]


def check_heat_model(m):
    h = [heat_jet(m)]
    for _ in range(6):
        h.append(tuple(p.d(1) for p in h[-1]))
    primitive = heat_jet(m, primitive=True)
    for r in range(2):
        assert h[0][r].d(0) == -h[2][r]
        assert primitive[r].d(1) == h[0][r]
    q = real_pair(h[1], h[1])-real_pair(h[0], h[2])
    A = F(-1, 2)*(imag_pair(h[0], h[1])-imag_pair(primitive, h[2]))
    B = F(1, 2)*(real_pair(h[0], h[1])-real_pair(primitive, h[2]))
    G = real_pair(h[0], h[0])
    psi = F(1, 2)*imag_pair(primitive, h[1])
    assert B.d(1)-A.d(2) == q
    assert G.d(2).d(2) == 2*q
    assert psi.d(2) == B
    assert A-psi.d(1) == F(-1, 2)*G.d(2)
    qvv = (3*real_pair(h[2], h[2])-4*real_pair(h[1], h[3])
           +real_pair(h[0], h[4]))
    qvvt = (4*real_pair(h[3], h[3])-7*real_pair(h[2], h[4])
            +4*real_pair(h[1], h[5])-real_pair(h[0], h[6]))
    assert q.d(2).d(2) == qvv
    assert qvv.d(0) == qvvt
    hr = [r.at(2, 0) for r, _ in h]
    E = hr[0]**2+hr[1]**2
    lag = hr[1]**2-hr[0]*hr[2]
    current = hr[1]*hr[2]-hr[0]*hr[3]
    assert (lag.d(0)*E-lag*E.d(0)+current.d(1)*E-current*E.d(1)) == 0
    # Clear E^2 in the weighted Stokes identity, including W_x B.
    assert E*(B.d(1)-A.d(2))-E.d(1)*B == E*q-E.d(1)*B
    # A nonconstant physical weight checks the face/correction cancellation.
    W = 1+t+x*x
    lo, hi, eta = F(-1, 3), F(4, 3), F(2, 5)
    boundary = ((W*B).at(1, hi)-(W*B).at(1, lo)).between(2, -eta, eta)
    boundary += ((W*A).at(2, -eta)-(W*A).at(2, eta)).between(1, lo, hi)
    correction = (W.d(1)*B).between(1, lo, hi).between(2, -eta, eta)
    bulk = (W*q).between(1, lo, hi).between(2, -eta, eta)
    assert boundary-correction == bulk
    # The changed primitive has only transverse faces and no weight term.
    aligned = F(1, 2)*(W*(G.d(2).at(2, eta)-G.d(2).at(2, -eta))).between(1, lo, hi)
    assert aligned == bulk
    if m == 2:
        assert q == 2*x*x+4*t+6*v*v
        assert q.average_v(Poly(eta))-q.at(2, 0) == 2*eta*eta
    return {"degree": m, "orientation_gauge_phase_and_derivatives": "pass"}


def check_reynolds():
    # Nonzero endpoint and thickness motion, with t/x/v cross terms.
    field = 1+t*x*x+(x+t)*v*v+t*t*v**4+v*(x+1)
    a, b, eta = t, t+1+t*t, 1+F(1, 2)*t
    avg = field.average_v(eta)
    lhs = avg.between(1, a, b).d(0)
    thickness_derivative = Poly()
    for (j, k, n), coefficient in field.terms.items():
        if n and n % 2 == 0:
            thickness_derivative += Poly({(j, k, 0): coefficient*F(n, n+1)})*eta**(n-1)
    rhs = field.d(0).average_v(eta).between(1, a, b)
    rhs += b.d(0)*avg.at(1, b)-a.d(0)*avg.at(1, a)
    rhs += eta.d(0)*thickness_derivative.between(1, a, b)
    assert lhs == rhs
    assert (v*v).average_v(eta) == F(1, 3)*eta*eta
    # F_vv=2 for v^2: the trace constant is exactly 1/6.
    assert F(1, 6)*2*eta*eta == (v*v).average_v(eta)
    return {"moving_endpoints_thickness_and_normalization": "pass",
            "trace_coefficient": "1/6", "thickness_derivative_coefficient": "1/3"}


def check_moving_jet():
    for h0, h1, h2, h3, g, gp, speed in (
        (F(2), F(3), F(-1), F(4), F(2, 3), F(5), F(-2)),
        (F(0), F(2), F(3), F(-4), F(4, 3), F(-2), F(7)),
    ):
        E = h0*h0+h1*h1
        rho, omega = (h1*h1-h0*h2)/E, (h1*h2-h0*h3)/E
        Kt, Ky = -h2+speed*h1, g*h1
        Kyt = gp*h1+g*(-h3+speed*h2)
        imag_t = Kyt/g-gp*Ky/(g*g)
        assert (h0*imag_t-h1*Kt)/E == omega-speed*rho
    return {"physical_derivative_scale_cancellation": "pass"}


def check_source_coefficients():
    for u, s in ((F(0), F(1)), (F(2), F(3)), (F(3, 2), F(3, 2))):
        assert u*s/2+(u*u+s*s)/4 == (u+s)**2/4
        assert -u*s/2+(u*u+s*s)/4 == (u-s)**2/4
    return {"sum_and_difference_frequency_weights": "pass"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = {
        "status": "passed", "date": "2026-10-21",
        "prepared_for": "Edward Baker", "model": "gpt-6-astra", "effort": "max",
        "verified_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "python": platform.python_version(),
        "arithmetic": "Python standard-library Fraction; sparse polynomial identities",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "heat_models": [check_heat_model(m) for m in (2, 3, 4, 6)],
        "reynolds": check_reynolds(), "moving_jet": check_moving_jet(),
        "source_kernel": check_source_coefficients(),
        "scope": "Frozen finite algebra only; no theta floor, quadrature, infinite-product or simplicity certificate.",
    }
    encoded = json.dumps(record, indent=2)+"\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
