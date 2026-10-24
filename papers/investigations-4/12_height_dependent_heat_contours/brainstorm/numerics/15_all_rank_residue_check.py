#!/usr/bin/env python3
"""Exact check of the all-rank marked-prime mixed-residue identity.

Prepared for Edward Baker, 2026-10-23, with substantial LLM assistance.
Recorded model: gpt-6-astra (Codex); reasoning effort: ultra.
Requires Python 3 and SymPy. This performs exact rational algebra, not a
numerical computation of zeta zeros or a proof of the arithmetic error bounds.

Put h=theta, q=1/t, and
    M0(s)=(1+h)/(h*s**2)-2/(h*s**3).
The right generating mark is exp(z*H_v); the swapped-left mark is exp(z*H_u).
Take the s=0 residue of exp(h*s)*M0(s) times each marked F/G branch first.

For the right F branch, let
    C_R=b*(t+a)*(t+c)/((a+b)*(b+c)*t),
    r0=b*q, r1=(1-b*q)*q, r2=-(1-b*q)*q**2,
    H_R0=2*q-1/(t+a)-1/(t+c).
The residue is C_R*exp(z*H_R0) times
    r0+(1-h)/h*(r1-z*q**2*r0)
       -2/h*(r2-z*q**2*r1+z*q**3*r0+z**2*q**4*r0/2).
For the left branch F(a,b,c;t,s), use
    C_L=b*(t+b)/((a+b)*(b+c)), d=a*c*q,
    E=a+c-t-a*c*q, r0=(a+c)*q-a*c*q**2,
    r1=-E*q**2, r2=E*q**3, H_L0=q-1/(t+b),
    c1=h-z*q**2, c2=c1**2/2+z*q**3,
    c3=c1**3/6+c1*z*q**3-z*q**4.
The residue is C_L*exp(z*H_L0) times
    (1+h)/h*(d*c2+r0*c1+r1)-2/h*(d*c3+r0*c2+r1*c1+r2).
For G use the right bracket, C_J=(t+a)/(a+b), and H_J0=q-1/(t+a).

After a,b,c are replaced by eps*A,eps*B,eps*C, the prefactors have at
most a simple eps pole. The right bracket's z**2 coefficient has an extra
factor eps; the left bracket's z**3 coefficient has eps**2, and its z**2
coefficient has eps. Since H_R0,H_L0=O(eps), the eps**3 coefficient has
z-degree at most 5; the J eps**2 coefficient has degree at most 4. Thus
checking the resulting finite generating polynomial settles every rank.

The complete three-branch sums have removable shift poles. Their eps**3
coefficient is homogeneous cubic in A,B,C, so a unit mixed finite difference
extracts exactly its ABC coefficient. Likewise for the quadratic J sum.
This is exact coefficient extraction, not finite-step differentiation.

Expected complete s=0 residue:
    (1+h)**3/(6*h) * (1/2 + q + z*q**2 + z**2*q**4/2).
For rank k, extract [z**k] and then multiply by h**(-k). Consequently all
ranks k>=3 have zero mixed residue. Discarding the s=-t residue and passing
from HLZ arithmetic sums to these kernels require the separate analytic
proof in Note15; this script does not establish those steps.
"""

import argparse
import itertools
import json
from pathlib import Path

import sympy as sp

q, z, theta, eps = sp.symbols("q z theta eps")
M1 = (1 + theta) / theta
M2 = -2 / theta


def exp_coefficients(kind, a, b, c, phase, maximum):
    """Coefficients of exp(phase*eps+z*H(0)) through eps**maximum."""
    exponent = {}
    for power in range(1, maximum + 1):
        shift_power = (
            a**power + c**power
            if kind == "right"
            else b**power if kind == "left" else a**power
        )
        exponent[power] = z * (-1) ** (power + 1) * shift_power * q ** (power + 1)
        if power == 1:
            exponent[power] += phase
    result = [sp.Integer(1)]
    for degree in range(1, maximum + 1):
        result.append(
            sp.expand(
                sum(j * exponent[j] * result[degree - j] for j in range(1, degree + 1))
                / degree
            )
        )
    return result


def residue_shift_coefficient(kind, a, b, c, phase, order):
    """[eps**order] of one exact baseline s=0 residue, including its phase."""
    shifted_b = eps * b
    r0 = shifted_b * q
    r1 = (1 - shifted_b * q) * q
    r2 = -(1 - shifted_b * q) * q**2
    right_bracket = (
        r0
        + (1 - theta) / theta * (r1 - z * q**2 * r0)
        + M2 * (r2 - z * q**2 * r1 + z * q**3 * r0 + z**2 * q**4 * r0 / 2)
    )
    # The common eps**(-1) is removed from each prefactor here; it is
    # restored by requesting exponential coefficient order+1-j below.
    if kind == "right":
        prefactor_times_bracket = (
            sp.Rational(b, (a + b) * (b + c))
            * (1 / q + eps * (a + c) + eps**2 * a * c * q)
            * right_bracket
        )
    elif kind == "left":
        d = eps**2 * a * c * q
        edge = eps * (a + c) - 1 / q - eps**2 * a * c * q
        r0 = eps * (a + c) * q - eps**2 * a * c * q**2
        r1 = -edge * q**2
        r2 = edge * q**3
        c1 = theta - z * q**2
        c2 = c1**2 / 2 + z * q**3
        c3 = c1**3 / 6 + c1 * z * q**3 - z * q**4
        left_bracket = M1 * (d * c2 + r0 * c1 + r1) + M2 * (
            d * c3 + r0 * c2 + r1 * c1 + r2
        )
        prefactor_times_bracket = (
            sp.Rational(b, (a + b) * (b + c)) * (1 / q + eps * b) * left_bracket
        )
    else:
        prefactor_times_bracket = sp.Rational(1, a + b) * (1 / q + eps * a) * right_bracket

    polynomial = sp.Poly(sp.expand(prefactor_times_bracket), eps)
    exponential = exp_coefficients(kind, a, b, c, phase, order + 1)
    return sp.expand(
        sum(
            coefficient * exponential[order + 1 - powers[0]]
            for powers, coefficient in polynomial.terms()
            if powers[0] <= order + 1
        )
    )


def complete_residue(starts):
    right_i = sp.Integer(0)
    left_i = sp.Integer(0)
    for increments in itertools.product((0, 1), repeat=3):
        a, b, c = (base + delta for base, delta in zip(starts, increments))
        sign = (-1) ** (3 - sum(increments))
        right_i += sign * (
            residue_shift_coefficient("right", a, b, c, 0, 3)
            + residue_shift_coefficient("right", -b, -a, c, -a - b, 3)
            + residue_shift_coefficient("right", a, -c, -b, -b - c, 3)
        )
        # Swapping the I orientation exchanges a,b before forming branches.
        left_i += sign * (
            residue_shift_coefficient("left", b, a, c, 0, 3)
            + residue_shift_coefficient("left", -a, -b, c, -a - b, 3)
            + residue_shift_coefficient("left", b, -c, -a, -a - c, 3)
        )
    j_term = sp.Integer(0)
    for da, db in itertools.product((0, 1), repeat=2):
        a, b = starts[0] + da, starts[1] + db
        j_term += (-1) ** (2 - da - db) * (
            residue_shift_coefficient("j", a, b, 0, 0, 2)
            + residue_shift_coefficient("j", -b, -a, 0, -a - b, 2)
        )
    return tuple(sp.factor(sp.expand(part)) for part in (right_i, left_i, j_term))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", type=Path, required=True, help="Destination JSON result")
    args = parser.parse_args()
    expected = (1 + theta) ** 3 / (6 * theta) * (
        sp.Rational(1, 2) + q + z * q**2 + z**2 * q**4 / 2
    )
    checks = []
    previous = None
    for starts in ((1, 3, 5), (2, 7, 11)):
        components = complete_residue(starts)
        degrees = [int(sp.Poly(part, z).degree()) for part in components]
        assert degrees[0] <= 5 and degrees[1] <= 5 and degrees[2] <= 4
        result = sp.factor(sum(components))
        assert sp.cancel(result - expected) == 0
        assert sp.Poly(result, z).degree() == 2
        if previous is not None:
            assert all(sp.cancel(a - b) == 0 for a, b in zip(previous, components))
        previous = components
        checks.append(
            {
                "starting_triple": list(starts),
                "component_degrees_in_z": dict(zip(("I_right", "I_swapped_left", "J"), degrees)),
                "complete_residue": str(result),
                "difference_from_expected": "0",
                "components": dict(zip(("I_right", "I_swapped_left", "J"), map(str, components))),
                "rank_coefficients_0_to_6": {
                    str(k): str(sp.factor(sp.expand(result).coeff(z, k))) for k in range(7)
                },
            }
        )
    report = {
        "status": "PASS",
        "date": "2026-10-23",
        "prepared_for": "Edward Baker",
        "model": "gpt-6-astra (Codex)",
        "reasoning_effort": "ultra",
        "method": "Exact SymPy rational coefficient extraction; no zeta-zero numerics",
        "sympy_version": sp.__version__,
        "variables": {"q": "1/t", "theta": "fixed mollifier length exponent", "z": "formal prime marker"},
        "expected_residue": str(sp.factor(expected)),
        "rank_normalization": "Multiply [z**k] by theta**(-k)",
        "a_priori_degree_bounds": {"I": 5, "J": 4},
        "checks": checks,
        "scope": "Checks algebra only; arithmetic localization, discarded residue, and optimization scope are proved separately in Note15.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS: all-rank residue identity at both starting triples; ranks >= 3 vanish.")


if __name__ == "__main__":
    main()
