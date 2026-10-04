#!/usr/bin/env python3
"""Outward finite-continuum signed-pair certificate; no global RH claim.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-03.
Model: GPT-6 (Codex); serving variant and effort not exposed or inferred.
Requires an existing python-flint installation; installs nothing.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import platform
import time

import flint
from flint import acb, arb, ctx


def derivative(p, n=1):
    for _ in range(n):
        p = [i*p[i] for i in range(1, len(p))]
    return p


def square_norm(p):
    out = Fraction(0)
    for i, u in enumerate(p):
        for j, v in enumerate(p):
            d = i+j
            if d % 2 == 0:
                out += u*v*Fraction(2, (d+1)*4**(d+1))
    return out


def ab(q):
    q = Fraction(q)
    return arb(q.numerator)/q.denominator


def pack(x):
    return {"lower": str(x.lower().fmpq()), "upper": str(x.upper().fmpq())}


def transform(s, nu):
    # Exact exponential monomial integration on [-1/4,1/4].
    ep, em = (s/4).exp(), (-s/4).exp()
    ints = [(ep-em)/s]
    for k in range(1, 17):
        boundary = ab(Fraction(1, 4)**k)*(em-(-1)**k*ep)
        ints.append((k*ints[-1]-boundary)/s)
    hh = sum(comb(8, j)*(-16)**j*ints[2*j] for j in range(9))
    return s*(ab(Fraction(1, 4))-s*s)*hh/nu.sqrt()


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, choices=[192, 256], required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    start = time.perf_counter()

    h = [Fraction(0)]*17
    for j in range(9):
        h[2*j] = Fraction(comb(8, j)*(-16)**j)
    hp, hppp = derivative(h), derivative(h, 3)
    g0 = [Fraction(0)]*len(hp)
    for i, v in enumerate(hp):
        g0[i] += v/4
    for i, v in enumerate(hppp):
        g0[i] -= v
    nu_q = square_norm(g0)
    nu6_q = square_norm(derivative(g0, 6))
    assert nu_q == Fraction(146640624550936576, 37921101075)
    assert nu6_q == Fraction(2504085215525628254072340480, 19)
    atom = 2*factorial(8)*8**8
    interior_l1 = 8117695446119
    assert interior_l1**2 > nu6_q/2
    b = atom+interior_l1
    assert b == 9470610144359
    nu = ab(nu_q)
    k = arb(b)/nu.sqrt()

    cutoff = arb(500)
    nzeros = cutoff.zeta_nzeros()
    if not nzeros == arb(269):
        raise ArithmeticError("Complete zero count at 500 is not 269")
    zeros = acb.zeta_zeros(1, 270)
    if not zeros[268].imag < cutoff or not zeros[269].imag > cutoff:
        raise ArithmeticError("Endpoint zero enumeration is incomplete")
    for i, z in enumerate(zeros):
        if not z.real == ab(Fraction(1, 2)):
            raise ArithmeticError("Low zero real part is not exactly 1/2")
        if i and not zeros[i-1].imag < z.imag:
            raise ArithmeticError("Low zero intervals are not disjoint")
    terms = [abs(transform(acb(0, z.imag), nu)) for z in zeros[:269]]
    low_mass = 2*sum(terms)
    # An infinite gamma^-6 majorant bounds the finite verified tail;
    # no critical-line claim is made above the published verified height.
    critical_tail = 12*k*cutoff**(-5)*(cutoff.log()/5+arb(1)/25)
    verified_height = arb(3)*10**12
    unknown_tail = (12*k*ab(Fraction(1, 8)).exp()*verified_height**(-5)
                    *(verified_height.log()/5+arb(1)/25))
    horizon = arb(225)
    high_horizon = unknown_tail*(horizon/2).exp()
    a = ab(Fraction(1, 4))
    trivial_at_one = (ab(Fraction(1, 2)).sqrt()
                      *(-ab(Fraction(5, 2))*(1-a)).exp()
                      /(1-(-2*(1-a)).exp()))
    p_bound = low_mass+critical_tail+high_horizon+trivial_at_one
    if not p_bound < ab(Fraction(497, 100)):
        raise ArithmeticError("Uniform p envelope is not below 4.97")

    initial_cutoff = ab(Fraction(5, 4)).exp()
    if not arb(3) < initial_cutoff or not initial_cutoff < arb(4):
        raise ArithmeticError("Initial prime-power set is not {2,3}")
    j_one = (arb(2).log()/arb(2).sqrt()
             +arb(3).log()/arb(3).sqrt())**2
    if not j_one < ab(Fraction(127, 100)):
        raise ArithmeticError("Initial energy upper is not below 1.27")

    log_two = arb(2).log()
    # Lower theta/x at x=e^10. All subtracted ratios decrease after it.
    u = arb(10)
    cheb_lower_ratio = (
        log_two-(2*log_two+u)*(-u).exp()
        -4*log_two*(-u/2).exp()-4*u*(-2*u/3).exp())
    if not cheb_lower_ratio > ab(Fraction(1, 2)):
        raise ArithmeticError("Chebyshev lower threshold fails")
    diagonal_constant = 20+40*log_two
    if not diagonal_constant < arb(48):
        raise ArithmeticError("Diagonal lower constant is not below 48")
    diagonal_lower_at_100 = Fraction(100**2, 4)-48
    j_upper_at_100 = (Fraction(127, 100)
                      +Fraction(497, 100)**2*(100-1))
    sign_margin = diagonal_lower_at_100-j_upper_at_100
    slope_margin = Fraction(100, 2)-Fraction(497, 100)**2
    assert sign_margin == Fraction(53409, 10000)
    assert sign_margin > 5 and slope_margin > 0

    record = {
        "date": "2026-10-03",
        "prepared_for": "Edward Baker",
        "model": "GPT-6 (Codex)",
        "serving_variant": "not exposed; not inferred",
        "reasoning_effort": "not exposed; not inferred",
        "llm_acknowledgement": "Prepared with substantial LLM assistance.",
        "status": "CERTIFIED_FINITE_CONTINUUM_CONSTANTS",
        "bits": args.bits,
        "source_norm_squared": str(nu_q),
        "interior_sixth_derivative_norm_squared": str(nu6_q),
        "boundary_atom_total_variation": atom,
        "interior_l1_upper_integer": interior_l1,
        "total_variation_upper_integer": b,
        "computed_zero_count_at_500": 269,
        "last_included_ordinate": pack(zeros[268].imag),
        "first_excluded_ordinate": pack(zeros[269].imag),
        "both_zero_signs_included": True,
        "published_verified_height": "3000000000000",
        "zero_count_majorant": "N(t)<=t log(t) for t>=100",
        "enclosures": {
            "K": pack(k),
            "low_linear_mass_through_500": pack(low_mass),
            "critical_linear_tail_majorant_above_500": pack(critical_tail),
            "unknown_linear_tail_constant": pack(unknown_tail),
            "unknown_tail_cost_at_225": pack(high_horizon),
            "trivial_zero_majorant_at_1": pack(trivial_at_one),
            "uniform_p_upper_on_1_to_225": pack(p_bound),
            "initial_energy_upper_at_1": pack(j_one),
            "theta_lower_ratio_at_exp10": pack(cheb_lower_ratio),
            "diagonal_lower_constant": pack(diagonal_constant),
        },
        "certified_rational_thresholds": {
            "p_uniform_upper": "497/100",
            "J_at_1_upper": "127/100",
            "theta_lower_ratio": "1/2",
            "diagonal_lower_constant_upper": "48",
            "D_lower_all_Y": "max(0,Y^2/4-48)",
            "D_upper_all_Y": "2 log(2) (Y^2+17/16)",
            "sign_margin_at_Y100": str(sign_margin),
            "increasing_D_minus_J_slope_after_Y100": str(slope_margin),
        },
        "conclusions": {
            "p_interval": ["1", "225"],
            "signed_pair_interval": ["100", "225"],
            "signed_pair_upper": "-5",
            "Theta_plus_on_signed_pair_interval": "0",
            "Theta_plus_on_0_to_225_upper": "25(1+Y)",
        },
        "external_inputs": [
            "Full linear smoothed explicit formula and normalization.",
            "Published Platt-Trudgian finite-height RH verification through 3e12.",
            "Published zero count, implying N(t)<=t log(t) above100.",
            "FLINT interval zero counting and enumeration."
        ],
        "limitations": [
            "No global quadratic estimate or RH proof.",
            "No source/A/B inverse or full selective-loss certificate computed.",
            "The finite-height theorem and analytic reductions are external to this scalar arithmetic check."
        ],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "runtime": {
            "python": platform.python_version(),
            "python_flint": flint.__version__,
            "flint": flint.__FLINT_VERSION__,
            "seconds": time.perf_counter()-start,
        },
    }
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": record["status"], "bits": args.bits,
                      "p_bound": str(p_bound), "J1_bound": str(j_one),
                      "margin": str(sign_margin),
                      "seconds": record["runtime"]["seconds"]}))


if __name__ == "__main__":
    run()
