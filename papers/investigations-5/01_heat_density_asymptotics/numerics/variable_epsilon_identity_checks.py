#!/usr/bin/env python3
"""Exact polynomial checks for Note 14; standard library only.

Prepared for Edward Baker, 2026-10-24.
Substantial LLM assistance: gpt-6-astra, recorded effort max.
These checks validate cleared identities for a heat-polynomial control.
They are not theta enclosures or independent mathematical review.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform

class Poly:
    """Sparse polynomials in t,x,y with exact rational coefficients."""
    def __init__(self, terms=0):
        if isinstance(terms, Poly):
            self.terms = dict(terms.terms)
        elif isinstance(terms, dict):
            self.terms = {a: Fraction(c) for a, c in terms.items() if c}
        else:
            self.terms = {(0, 0, 0): Fraction(terms)} if terms else {}

    def __add__(self, other):
        out = dict(self.terms)
        for a, c in Poly(other).terms.items():
            out[a] = out.get(a, Fraction(0)) + c
        return Poly(out)
    __radd__ = __add__

    def __neg__(self):
        return Poly({a: -c for a, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-Poly(other))

    def __rsub__(self, other):
        return Poly(other) - self

    def __mul__(self, other):
        out = {}
        for a, c in self.terms.items():
            for b, d in Poly(other).terms.items():
                ab = tuple(ai + bi for ai, bi in zip(a, b))
                out[ab] = out.get(ab, Fraction(0)) + c*d
        return Poly(out)
    __rmul__ = __mul__

    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        out = Poly(1)
        for _ in range(exponent):
            out = out * self
        return out

    def diff(self, axis):
        out = {}
        for a, c in self.terms.items():
            if a[axis]:
                b = list(a)
                b[axis] -= 1
                out[tuple(b)] = c*a[axis]
        return Poly(out)

    def is_zero(self):
        return not self.terms

def lap(p):
    return p.diff(1).diff(1) + p.diff(2).diff(2)

def grad_dot(a, b):
    return sum((a.diff(i)*b.diff(i) for i in (1, 2)), Poly())

def check_control(q):
    t, x, y = VARIABLES
    # H=z^2-2t, H_z=2z, H_zz=2; it includes a double event at t=z=0.
    a, b = x*x-y*y-2*t, 2*x*y
    f = a*a+b*b
    p = 4*(x*x+y*y)  # |H_z|^2
    flux = (4*x, -4*y)  # Re/Im(H_zz conjugate(H_z))
    D = f+q
    Dt = D.diff(0)
    gradq2 = grad_dot(q, q)
    Cnum = D*lap(q)-2*grad_dot(f, q)-gradq2
    potential = Dt + Fraction(1, 2)*(D.diff(1).diff(1)-D.diff(2).diff(2))
    potential -= q.diff(0)+Fraction(1, 2)*(q.diff(1).diff(1)-q.diff(2).diff(2))
    curvature = D*lap(D)-grad_dot(D, D)-4*q*p-Cnum
    # 4*pi*C = 2 div(w grad r)-w Delta r-w(1-w)|grad r|^2.
    divform = 2*q*(D*lap(q)-grad_dot(D, q))
    divform -= D*(q*lap(q)-gradq2)+f*gradq2
    curvature_divergence = q*Cnum-divform
    rho_num = q*p
    continuity = rho_num.diff(0)*D-2*rho_num*Dt
    for axis, aj in zip((1, 2), flux):
        jnum = q*aj
        continuity += jnum.diff(axis)*D-2*jnum*D.diff(axis)
    source_numerator = (D-2*q)*(q.diff(0)*p+sum(
        (q.diff(axis)*aj for axis, aj in zip((1, 2), flux)), Poly()))
    continuity -= source_numerator
    residuals = {
        "potential_forcing_cleared_D": potential,
        "curvature_correction_cleared_D_squared": curvature,
        "curvature_divergence_form_cleared_q_D_squared": curvature_divergence,
        "current_source_cleared_pi_D_cubed": continuity,
    }
    report = {name: {"identically_zero": v.is_zero(),
                     "nonzero_polynomial_coefficients": len(v.terms)}
              for name, v in residuals.items()}
    # Ensure the controls would detect dropping the new terms.
    raw_source = source_numerator
    report["extra_curvature_nonzero"] = not Cnum.is_zero()
    report["extra_current_source_nonzero"] = not raw_source.is_zero()
    for name, value in report.items():
        if isinstance(value, dict):
            assert value["identically_zero"], (name, value)
    return report

VARIABLES = tuple(Poly({tuple(int(j == i) for j in range(3)): 1})
                  for i in range(3))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    t, x, y = VARIABLES
    controls = {
        "constant_q": Poly(1),
        "time_only_q": 1+t*t,
        "height_time_q": 1+t*t+x*x,
        "full_space_time_q": 1+t*t+x*x+2*y*y,
    }
    report = {name: check_control(q) for name, q in controls.items()}
    assert not report["constant_q"]["extra_curvature_nonzero"]
    assert not report["constant_q"]["extra_current_source_nonzero"]
    assert not report["time_only_q"]["extra_curvature_nonzero"]
    assert report["time_only_q"]["extra_current_source_nonzero"]
    for name in ("height_time_q", "full_space_time_q"):
        assert report[name]["extra_curvature_nonzero"]
        assert report[name]["extra_current_source_nonzero"]
    # Exact rational checks of Gaussian control coefficients for eta^2=1/2,
    # at T=2, x=3, y=0. Common pi factors are retained in labels.
    eta2, T, xval = Fraction(1, 2), Fraction(2), Fraction(3)
    w = eta2/(1+eta2)
    gaussian = {
        "parameters": {"eta_squared": str(eta2), "T": str(T), "x": str(xval)},
        "pi_times_positive_density": str(w*(1-w)*xval*xval/(4*T*T)),
        "pi_times_curvature_density": str(-w/(4*T)),
        "potential_forcing": str(w/(2*T)),
        "curvature_density_is_negative": True,
        "scope": "Exact coefficients of the Gaussian control derived in Note 14; not a theta computation."
    }
    record = {
        "date": "2026-10-24",
        "prepared_for": "Edward Baker",
        "model": "gpt-6-astra",
        "reasoning_effort": "max",
        "status": "Exact rational polynomial identity checks; same-assistant implementation.",
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "identity_count": 16,
        "all_identities_zero": True,
        "control": "H(t,z)=z^2-2t, including its double event",
        "checks": report,
        "gaussian_control": gaussian,
        "limitations": [
            "No canonical-theta numerical enclosure.",
            "No independent implementation or review.",
            "No claim that a stationary profile excludes earlier collisions."
        ],
    }
    data = json.dumps(record, indent=2)+"\n"
    if args.output:
        args.output.write_text(data)
    print(json.dumps({"identities": 16, "all_zero": True,
                      "gaussian_pi_curvature": gaussian["pi_times_curvature_density"]}))

if __name__ == "__main__":
    main()
