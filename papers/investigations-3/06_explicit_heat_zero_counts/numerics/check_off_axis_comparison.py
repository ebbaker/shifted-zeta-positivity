#!/usr/bin/env python3
"""Exact finite constants for Note 02; the analytic proof is in the note.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-17.
Recorded model: gpt-6.1-sol (Codex), reasoning effort ultra.
Python standard library only. A low comparison ceiling is a budget failure
injection, not a counterexample to the actual heat comparison.
"""
import argparse
from fractions import Fraction as Q
import json
import sys


def exp_bounds(x, n=40):
    """Positive Taylor lower sum and geometric upper tail, x>=0."""
    if x < 0 or x >= n + 2:
        raise ValueError("unsupported exponential enclosure parameters")
    term, total = Q(1), Q(1)
    for k in range(1, n + 1):
        term *= x / k
        total += term
    next_term = term * x / (n + 1)
    return total, total + next_term / (1 - x / (n + 2))


def atan_bounds(x, n):
    # Alternating Taylor series for 0<x<1.
    total = sum(((-1)**k * x**(2*k+1) / (2*k+1) for k in range(n)), Q(0))
    following = total + (-1)**n * x**(2*n+1) / (2*n+1)
    return min(total, following), max(total, following)


def log2_bounds(n=14):
    # log2=2 atanh(1/3), with a positive geometric tail majorant.
    z = Q(1, 3)
    lower = 2 * sum((z**(2*k+1)/(2*k+1) for k in range(n)), Q(0))
    upper = lower + 2*z**(2*n+1)/((2*n+1)*(1-z*z))
    return lower, upper


def run(ceiling):
    checks = []
    def require(name, value):
        checks.append({"name": name, "passed": bool(value)})

    a5lo, a5hi = atan_bounds(Q(1, 5), 18)
    a239lo, a239hi = atan_bounds(Q(1, 239), 6)
    pi_lo, pi_hi = 16*a5lo - 4*a239hi, 16*a5hi - 4*a239lo
    e_lo, e_hi = exp_bounds(Q(1))
    log2lo, log2hi = log2_bounds()
    require("pi enclosure within declared rational cuts", Q(157, 50) < pi_lo < pi_hi < Q(22, 7))
    require("elementary exponential cuts", Q(8, 3) < e_lo < e_hi < 3)
    require("log2 lower moment comparison", log2lo > Q(2, 3))
    require("log3 upper cut", exp_bounds(Q(11, 10))[0] > 3)
    require("square-root cuts", pi_hi < Q(71, 40)**2 and pi_hi < 4 and Q(99, 70)**2 > 2)

    x0, tmin, amin = Q(2_000_000), Q(1_000_000), Q(300)
    require("log cutoff below 15", exp_bounds(Q(15))[0] > x0)
    require("log cutoff above 8", 3**8 < x0)
    require("ordinary denominator bound", x0/2 - Q(333, 100) >= x0/3)
    ordinary_exponent = (3*Q(15)**2/32 + Q(7, 8))/x0
    require("ordinary exponent endpoint", ordinary_exponent == Q(703, 32*2_000_000))
    require("ordinary exponential allowance", ordinary_exponent < Q(1, 8) and Q(8, 7)*ordinary_exponent < Q(1, 50000))
    require("heat weight reserve at cutoff", Q(1, 2) - pi_hi/(16*x0) - 26/x0**2 > 0)
    require("alpha modulus remainder", Q(11, 2)/x0 + Q(25, 4)/x0**2 < 6/x0)
    require("alpha phase remainder below one", pi_hi/4 + Q(11, 4)/tmin + Q(85, 16)/tmin**2 < 1)
    require("gamma algebraic absorption", Q(101, 100)/2 * 3 + Q(102, 100) < 3 and 85/x0 < Q(1, 100) and 6/x0 < Q(1, 100))
    require("gamma exponential below two", exp_bounds(Q(15)/x0)[1] < 2)
    require("carrier heat exponent nonpositive", 6*pi_hi/x0 < 1 and x0/13 > 3)

    dmin = tmin - 3
    hmin = 1 - Q(1, 2)/dmin
    require("gaussian h lower bound", hmin > Q(999, 1000))
    require("gaussian sigma reserve", Q(29, 4)/dmin < Q(1, 1000))
    require("gaussian linear reserve", Q(5, 2)/dmin < Q(1, 1000))
    require("gaussian log prefactor reserve", Q(1, 2)/(2*dmin*hmin) < Q(1, 1000))
    moment_log = Q(2, 1000) + Q(1, 2)*Q(1101, 1000)**2*Q(1000, 999)
    require("gaussian nontrivial moment below two", moment_log < Q(2, 3) and exp_bounds(moment_log)[1] < 2)
    require("zero moment exponent reserve", 2*Q(5, 2)**2+Q(1, 2)+1 == 14 and 14/(tmin-6) < Q(1, 4))
    require("a above three hundred", tmin/(2*pi_hi) > amin**2)

    require("positive coefficient leading cut", 1/(8*pi_lo) < Q(1, 5)**2)
    require("positive remainder coefficient cut", Q(11, 10)**2/7 < Q(173, 1000))
    require("negative coefficient prefactor", Q(99, 70)/(4*pi_lo*pi_lo) < Q(36, 1000))
    rho = Q(445, 1000)
    require("negative coefficient geometric rate", 1/((3-2*log2hi)*pi_lo) < rho*rho)
    require("negative even coefficient sum", rho**2/(1-rho**2) < Q(247, 1000))
    require("negative odd coefficient sum", rho**3/(1-rho**2)*Q(71, 80) < Q(98, 1000))
    require("negative baseline compression", Q(36, 1000)*(rho*Q(71, 40)+Q(247, 1000)/amin+Q(98, 1000)/amin**2) < Q(29, 1000))

    # Fixed-height-index RS remainder, separated from the dynamic tail.
    require("fixed-index logarithm coefficient", exp_bounds(Q(1, 5), n=2)[0] > Q(121, 100))
    stirling_error = 1/(12*(amin**2-Q(33, 100)))
    require("fixed-index real Stirling prefactor", Q(8, 3)*exp_bounds(stirling_error)[1] < 3)
    require("fixed-index nu ratio allowance", Q(1, 2)+1/(4*amin**2) < 1)
    require("fixed-index extra exponential absorbed", 1+Q(3, 10)*amin**2 > 5)
    require("fixed-index gaussian contribution", Q(4, 3)/(1+amin**2/2) < 1)

    coefficient = Q(2, 5)*243 + Q(58, 1000)*3
    require("gaussian coefficient total", coefficient == Q(97374, 1000))
    require("coefficient allowance for all a above cutoff", coefficient < 98 and coefficient*amin < 98*(amin-Q(865, 1000)))
    # Exact rational bounds for f(14),f(15), using e>8/3 and sqrt(pi)<2.
    f14 = Q(11, 10)**14 * 720 * 2**10 * Q(3, 8)**100
    f15 = Q(11, 10)**15 * Q(135135, 64) * 2**11 * Q(3, 8)**121
    require("tail base 14", f14 < Q(1, 10**30))
    require("tail base 15", f15 < Q(1, 10**30))
    require("tail two-step ratio", Q(121, 50)*14*Q(3, 8)**44 < 1)
    require("tail ratio decreases", Q(15, 14)*Q(3, 8)**4 < 1)
    require("tail gaussian domination", 1/dmin < Q(1, 8))
    require("tail below one over a", Q(4, 10**30) < amin**13)
    require("full remainder bracket endpoint equality", Q(1, 2)*Q(4, 3)+100/amin == 1)

    zeta2_upper = Q(22, 7)**2/6
    require("zeta2 comparison rational", zeta2_upper == Q(242, 147))
    require("finite cutoff power allowance", Q(33, 32)**2 < 2)
    require("opposite branch allowance", 16*13/x0 < Q(11, 1000)**2)
    require("ordinary normalized error allowance", (zeta2_upper+Q(11, 1000))/50000 < Q(1, 25000))
    require("remainder normalization allowance", 4*pi_hi < 13)
    budget = zeta2_upper-1 + Q(11, 1000) + Q(1, 25000) + 26/x0
    require("comparison below 33 over 50", budget < Q(33, 50))
    require("requested comparison ceiling fits budget", budget < ceiling)
    return {
        "status": "pass" if all(c["passed"] for c in checks) else "fail",
        "checks": checks,
        "domain": {"x_min": int(x0), "t": "0<t<=1/2", "y": "3<=y<=4"},
        "comparison_budget_upper": str(budget),
        "comparison_ceiling": str(ceiling),
        "ordinary_relative_error_allowance": "1/50000",
        "scope": "Finite rational constants for the written analytic derivation; no zero survey or formal proof certification.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comparison-ceiling", type=Q, default=Q(7, 10))
    args = parser.parse_args()
    result = run(args.comparison_ceiling)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "pass" else 1)
