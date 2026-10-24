#!/usr/bin/env python3
"""Exact symbolic checks for the discrete Feng mixed-moment kernel.

Prepared for Edward Baker, 23 October 2026, with substantial LLM assistance.
Recorded model: gpt-6-astra (Codex); reasoning effort: ultra.

Requires Python 3 and SymPy. This file has no local-data or path dependencies.
Usage:
    python3 14_discrete_feng_kernel_check.py --output result.json

Scope: symbolic algebra only. The source-to-moment passage, uniform arithmetic
errors, Mellin localization, smoothing requirements, and limiting null directions
require the separate analytic proof. In particular the formal monomial checks do
not prove the actual low-smoothing moment asymptotics.

The derivative check uses homogeneous polynomial division and exact coefficient
extraction, independently of the finite-difference method used to first obtain
the kernels. No floating-point arithmetic or zeta-zero data is used.
"""

from __future__ import annotations

import argparse
import json
import platform
import time
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

s, t, a, b, c, theta = sp.symbols("s t a b c theta")
SHIFT_VARS = (a, b, c)
CHECKS: list[dict[str, object]] = []


def require(condition: bool, name: str) -> None:
    """An assertion that remains enabled under python -O."""
    if not condition:
        raise AssertionError(name)
    CHECKS.append({"name": name, "passed": True})


def equal(actual: sp.Expr, expected: sp.Expr, name: str) -> None:
    difference = sp.cancel(actual - expected)
    if difference != 0:
        raise AssertionError(f"{name}: nonzero exact difference {difference}")
    CHECKS.append({"name": name, "passed": True, "exact_difference": "0"})


def homogeneous_parts(poly: sp.Expr, degree: int) -> dict[int, sp.Expr]:
    parts = {d: sp.S.Zero for d in range(degree + 1)}
    for monomial, coefficient in sp.Poly(sp.expand(poly), *SHIFT_VARS).terms():
        d = sum(monomial)
        if d <= degree:
            parts[d] += coefficient * sp.prod(
                variable**power for variable, power in zip(SHIFT_VARS, monomial)
            )
    return parts


def i_kernel(mark: str) -> sp.Expr:
    """Extract abc from the three F branches by exact polynomial division.

    F=b(s+b)(t+a)(t+c)/[(a+b)(b+c)(s+t)t]. Markers are
    right: (1/(s+t)-1/(t+a)-1/(t+c)+1/t)^2/2,
    left:  (1/(s+t)-1/(s+b))^2/2.
    The common theta^-2 marker normalization is intentionally excluded.

    Removing the two homogeneous shift-pole factors makes total numerator
    degree five sufficient. Reciprocal factors need only their first five
    homogeneous terms; exponential factors need only degrees zero to four.
    """
    if mark == "right":
        d = -s * t**2 + t**2 * (a + c) + a * c * (s + 2 * t)
        inverse_numerator = sp.Add(*(
            (-a)**i * (-c)**j * t**(4-i-j)
            for i in range(5) for j in range(5-i)
        ))
        regular = b * (s+b) * d**2 * inverse_numerator
        constant_denominator = 2 * t**9 * (s+t)**3
    elif mark == "left":
        inverse_numerator = sp.Add(*((-b)**i * s**(4-i) for i in range(5)))
        regular = b * (t+a) * (t+c) * (b-t)**2 * inverse_numerator
        constant_denominator = 2 * t * (s+t)**3 * s**5
    elif mark == "none":
        regular = b * (s+b) * (t+a) * (t+c)
        constant_denominator = t * (s+t)
    else:
        raise ValueError(mark)

    h = homogeneous_parts(regular, 5)
    numerator = (a-c) * h[5]
    for k in range(5):
        second = h[5-k].subs({a: -b, b: -a, c: c}, simultaneous=True)
        third = h[5-k].subs({a: a, b: -c, c: -b}, simultaneous=True)
        numerator += (b+c) * (-a-b)**k / sp.factorial(k) * second
        numerator -= (a+b) * (-b-c)**k / sp.factorial(k) * third

    pole_factors = (a+b) * (b+c) * (a-c)
    quotient, remainder = sp.div(
        sp.Poly(sp.expand(numerator), a, b, c, s, t),
        sp.Poly(pole_factors, a, b, c, s, t),
    )
    require(remainder.is_zero, f"I_{mark}: exact shift-pole cancellation")
    quotient = sp.Poly(quotient.as_expr(), a, b, c)
    require(quotient.total_degree() == 3, f"I_{mark}: quotient degree three")
    return sp.factor(quotient.coeff_monomial(a*b*c) / constant_denominator)


def j_kernel(mark: str) -> sp.Expr:
    """Extract ab from G(a,b)+exp(-a-b)G(-b,-a), without finite differences.

    G=(s+b)(t+a)/[(a+b)(s+t)]. Its right marker is
    (1/(s+t)-1/(t+a))^2/2, again without theta^-2.
    """
    if mark == "right":
        inverse_numerator = sp.Add(*((-a)**i * t**(3-i) for i in range(4)))
        regular = (s+b) * (a-s)**2 * inverse_numerator
        constant_denominator = 2 * (s+t)**3 * t**4
    elif mark == "none":
        regular = (s+b) * (t+a)
        constant_denominator = s+t
    else:
        raise ValueError(mark)

    h = homogeneous_parts(regular, 3)
    numerator = h[3] - sum(
        (-a-b)**k / sp.factorial(k)
        * h[3-k].subs({a: -b, b: -a}, simultaneous=True)
        for k in range(4)
    )
    quotient, remainder = sp.div(
        sp.Poly(sp.expand(numerator), a, b, s, t),
        sp.Poly(a+b, a, b, s, t),
    )
    require(remainder.is_zero, f"J_{mark}: exact shift-pole cancellation")
    quotient = sp.Poly(quotient.as_expr(), a, b)
    require(quotient.total_degree() == 2, f"J_{mark}: quotient degree two")
    return sp.factor(quotient.coeff_monomial(a*b) / constant_denominator)


def expected_component_kernels() -> dict[str, sp.Expr]:
    return {
        "I_none": -(3*s*t**2-4*s*t-12*s+8*t**2-24)/(24*t*(s+t)),
        "I_right": -(
            3*s**3*t**3+4*s**3*t**2-24*s**3+16*s**2*t**3
            -24*s**2*t**2-24*s**2*t-36*s*t**3-24*s*t**2-48*t**3
        )/(48*t**4*(s+t)**3),
        "I_left": -(
            3*s**4*t**4-20*s**4*t**3+72*s**4*t-24*s**4
            -8*s**3*t**4+24*s**3*t**3+72*s**3*t**2-96*s**3*t
            +12*s**2*t**4+24*s**2*t**3-144*s**2*t**2-96*s*t**3-24*t**4
        )/(48*s**5*t*(s+t)**3),
        "J_none": (2*s*t+3*s+3*t+6)/(6*(s+t)),
        "J_right": (
            2*s**3*t**3-3*s**3*t**2+6*s**3-3*s**2*t**3
            -6*s**2*t**2+18*s**2*t-12*s*t**3+18*s*t**2+6*t**3
        )/(12*t**4*(s+t)**3),
    }


def formal_double_inverse(expr: sp.Expr) -> sp.Expr:
    """Exact iterated inverse transform at (theta,theta) for these kernels.

    Expand over s^-A t^-B (s+t)^-C. For A,B>0 and C>0 the common
    convolution gives theta^(A+B+C-2) (A+B-2)! /
    [(A-1)! (B-1)! (A+B+C-2)!]. C=0 separates the two transforms.
    If one of A,B is nonpositive, the boundary polynomial contributes zero
    here only when A+B>1. Any other boundary case raises an exception.
    This is a rational-transform calculation, not an arithmetic tail bound.
    """
    numerator, denominator = sp.fraction(sp.cancel(expr))
    powers = sp.factor(denominator).as_powers_dict()
    aa, bb, cc = (int(powers.get(v, 0)) for v in (s, t, s+t))
    constant = sp.cancel(denominator / (s**aa*t**bb*(s+t)**cc))
    if {s, t} & constant.free_symbols:
        raise ValueError(f"Unexpected denominator: {denominator}")
    answer = sp.S.Zero
    for (i, j), coefficient in sp.Poly(numerator, s, t).terms():
        A, B, C = aa-i, bb-j, cc
        if C == 0:
            term = (
                theta**(A+B-2)/(sp.factorial(A-1)*sp.factorial(B-1))
                if A > 0 and B > 0 else sp.S.Zero
            )
        elif A > 0 and B > 0:
            term = (
                theta**(A+B+C-2)*sp.factorial(A+B-2)
                /(sp.factorial(A-1)*sp.factorial(B-1)*sp.factorial(A+B+C-2))
            )
        elif A+B > 1:
            term = sp.S.Zero
        else:
            raise ValueError(f"Unpaid boundary term A={A}, B={B}, C={C}")
        answer += coefficient/constant*term
    return sp.factor(answer)


def residue_from_principal_part(expr: sp.Expr, pole: sp.Expr) -> sp.Expr:
    """Residue of exp(theta*(s-pole))*expr at pole, by the exact Laurent part."""
    x = sp.Symbol("x")
    shifted = sp.cancel(expr.subs(s, x+pole))
    # These rational kernels have pole order at most four. The analytic
    # part cannot contribute, and four exponential terms suffice.
    exponential_jet = sum((theta*x)**k/sp.factorial(k) for k in range(4))
    return sp.factor(sp.residue(exponential_jet*shifted, x, 0))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write JSON here; otherwise print JSON.")
    args = parser.parse_args()
    started = time.monotonic()

    kernels = {f"I_{m}": i_kernel(m) for m in ("none", "right", "left")}
    kernels.update({f"J_{m}": j_kernel(m) for m in ("none", "right")})
    for name, expected in expected_component_kernels().items():
        equal(kernels[name], expected, f"{name}: displayed component formula")
    swap = lambda expr: expr.subs({s: t, t: s}, simultaneous=True)
    K0 = sp.factor(kernels["I_none"]+swap(kernels["I_none"])+kernels["J_none"])
    K1 = sp.factor(kernels["I_right"]+swap(kernels["I_left"])+kernels["J_right"])
    expected_K0 = (
        s**2*t**2+4*s**2*t+6*s**2+4*s*t**2+12*s*t+12*s+6*t**2+12*t
    )/(12*s*t*(s+t))
    expected_K1 = (
        s**4*t**4-4*s**4*t**3-6*s**4*t**2+24*s**4*t+12*s**4
        -4*s**3*t**4-12*s**3*t**3+36*s**3*t**2+48*s**3*t
        -6*s**2*t**4+12*s**2*t**3+72*s**2*t**2+48*s*t**3+12*t**4
    )/(24*s*t**5*(s+t)**3)
    equal(K0, expected_K0, "K0: assembled unmarked kernel")
    equal(K1, expected_K1, "K1: assembled marked kernel")

    displayed_partial_fractions = (
        -t**2/(24*(s+t)**3)
        +(3*t**3-4*t**2+12)/(24*t**2*(s+t)**2)
        -(3*t**3-8*t**2-6*t+36)/(24*t**3*(s+t))
        +(t**4-4*t**3-6*t**2+24*t+12)/(24*t**5)
        +1/(2*s*t**4)
    )
    equal(K1, displayed_partial_fractions, "K1: displayed partial fractions (note equation 8)")
    equal(sp.apart(K1, s), displayed_partial_fractions, "K1: independent SymPy partial fractions")

    M0 = lambda z: (1+theta)/(theta*z**2)-2/(theta*z**3)
    a0 = (theta**2+3*theta+3)/6
    b00 = formal_double_inverse(K0*M0(s)*M0(t))
    expected_b00 = (1+theta)**3*(theta**2+3*theta+3)/(36*theta)
    equal(b00, expected_b00, "baseline: kernel inverse transform b00")
    equal(b00.subs(theta, sp.Rational(1, 2)), sp.Rational(57, 64), "baseline: b00 at theta=1/2")
    c_theta = 6*theta/(1+theta)**3
    equal(a0/b00, c_theta, "baseline: optimal coefficient c_theta")
    equal(a0**2/b00, 1-(1+theta)**-3, "baseline: leading quotient F_theta")
    equal((a0**2/b00).subs(theta, sp.Rational(1, 2)), sp.Rational(19, 27), "baseline: quotient at theta=1/2")

    inner_rational = sp.cancel(M0(s)*K1)
    R0 = residue_from_principal_part(inner_rational, sp.S.Zero)
    Rtheta = residue_from_principal_part(inner_rational, -t)
    expected_R0 = (1+theta)**3/(12*theta*t**4)
    expected_Rtheta = (
        -theta*(1+theta)/48+1/(24*t)-(1+theta)/(6*t**2)-1/(3*t**3)
        +(6*theta**2+9*theta-1)/(12*theta*t**4)+1/(2*t**5)
    )
    equal(R0, expected_R0, "s-inversion: residue R0 at zero")
    equal(Rtheta, expected_Rtheta, "s-inversion: residue Rtheta after removing exp(-theta*t)")

    monomials = []
    for B in (1, 2, 5, 10, 30, 100):
        MB = sp.factorial(B)/(theta**B*t**(B+1))
        cross = formal_double_inverse(K1*M0(s)*MB/theta**2)
        product = (B+1)*(B+2)*(B+3)*(B+4)
        weighted_integral = sp.Rational(6, product)
        predicted_cross = theta*(1+theta)**3*weighted_integral/72
        a1 = theta**2*weighted_integral/12
        equal(cross, predicted_cross, f"formal P1=u^{B}: full double inverse identity")
        # After outer exponential cancellation all tail poles are at zero;
        # its O(t^-2) decay permits closing right. No 1/t term remains.
        tail = sp.cancel(MB*Rtheta)
        numerator, denominator = sp.fraction(tail)
        decay_order = sp.degree(denominator, t)-sp.degree(numerator, t)
        require(decay_order >= 2, f"formal P1=u^{B}: remainder decays at least t^-2")
        equal(sp.residue(tail, t, 0), 0, f"formal P1=u^{B}: no boundary 1/t coefficient")
        equal(a1-c_theta*cross, 0, f"formal P1=u^{B}: zero residual correlation")
        monomials.append({
            "degree": B,
            "scope": "formal rational-transform identity only",
            "weighted_profile_integral": str(weighted_integral),
            "first_moment_coefficient": str(sp.factor(a1)),
            "mixed_moment_coefficient": str(sp.factor(cross)),
            "residual_correlation": "0",
            "remainder_decay_order": int(decay_order),
        })

    report = {
        "status": "passed",
        "scope": "symbolic algebra only; analytic proof and arithmetic convergence are separate",
        "research_date": "2026-10-23",
        "prepared_for": "Edward Baker",
        "llm_assistance": {"model": "gpt-6-astra (Codex)", "reasoning_effort": "ultra"},
        "run_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "sympy_version": sp.__version__,
        "elapsed_seconds": round(time.monotonic()-started, 6),
        "method": "exact homogeneous polynomial division and coefficient extraction; no finite differences or floating point",
        "parameters": "Fixed 0<theta<1/2 in the analytic application; rational identities use symbolic theta.",
        "normalization": "K1 excludes the outer theta^-2; Rtheta excludes exp(-theta*t).",
        "component_kernels": {name: str(value) for name, value in kernels.items()},
        "assembled_kernels": {"K0": str(K0), "K1": str(K1)},
        "displayed_K1_partial_fractions": str(displayed_partial_fractions),
        "baseline": {
            "a0": str(a0), "b00": str(b00), "b00_at_half": "57/64",
            "c_theta": str(c_theta), "F_theta": "1 - (1 + theta)**(-3)",
            "F_at_half": "19/27",
        },
        "s_residues": {"R0": str(R0), "Rtheta": str(expected_Rtheta)},
        "general_polynomial_consequence": {
            "condition": "P1 is a polynomial with P1(0)=0",
            "formal_b01": "theta*(1+theta)^3/72 * integral_0^1 (1-u)^3 P1(u) du",
            "formal_a1": "theta^2/12 * integral_0^1 (1-u)^3 P1(u) du",
            "formal_residual_correlation": "0",
            "proof_scope": "Residues plus linearity and inverse-transform convolution; this report does not prove the arithmetic passage.",
        },
        "monomial_checks": monomials,
        "assertion_count": len(CHECKS),
        "checks": CHECKS,
    }
    output = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"PASS: {len(CHECKS)} exact symbolic assertions; JSON written to {args.output}")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
