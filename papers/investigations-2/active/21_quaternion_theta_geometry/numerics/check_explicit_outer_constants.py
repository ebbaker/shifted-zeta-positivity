#!/usr/bin/env python3
"""Exact rational audit of budgets in the explicit outer-threshold proof.

This checks arithmetic and sufficient polynomial inequalities on L >= 1000.
It does not verify the imported Riemann--Siegel theorem, analyticity, complex
function identities, or the analytic reductions to the checked inequalities.
No large exponential or floating-point approximation is evaluated.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json

BASE = 1000
checks = []


def fracstr(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def exact(name, actual, relation, expected, reason):
    actual, expected = F(actual), F(expected)
    ok = {"==": actual == expected, "<": actual < expected,
          "<=": actual <= expected, ">": actual > expected,
          ">=": actual >= expected}[relation]
    checks.append({"name": name, "kind": "exact_rational", "actual": fracstr(actual),
                   "relation": relation, "expected": fracstr(expected),
                   "passed": ok, "reason": reason})


def positive_poly(name, coefficients, reason):
    """Certify polynomial > 0 for L >= BASE by shifting L=BASE+y."""
    coefficients = list(map(F, coefficients))
    shifted = [sum(coefficients[j] * comb(j, k) * BASE ** (j-k)
                   for j in range(k, len(coefficients)))
               for k in range(len(coefficients))]
    ok = shifted[0] > 0 and all(c >= 0 for c in shifted)
    checks.append({"name": name, "kind": "positive_polynomial_on_half_line",
                   "base": BASE,
                   "coefficients_ascending": [fracstr(c) for c in coefficients],
                   "shifted_coefficients_ascending": [fracstr(c) for c in shifted],
                   "passed": ok, "reason": reason})


def integral_moment(a, m):
    # Integral from 1 to infinity of (log y + 1)^m y^(-1-a) dy.
    return sum(F(comb(m, j) * factorial(j), 1) / a ** (j+1)
               for j in range(m+1))


def main(output):
    weighted_moment = integral_moment(F(1, 16), 2)
    exact("weighted_log_square_moment", weighted_moment, "==", 8720,
          "Exact evaluation of 2/a^3+2/a^2+1/a at a=1/16.")
    exact("weighted_moment_rounding", weighted_moment, "<", 9000,
          "Safe integer majorant for the logarithmic moment.")
    exact("uniform_time_factor", F(19, 4)+8, "<", 13,
          "Uses the analytic bound s exp(-s log(2)/8) <= 8/(e log(2)) < 8.")
    exact("weighted_discrepancy_numerator", F(9000 * 13, 4), "==", 29250,
          "Coefficient before division by L_u.")
    positive_poly("weighted_Lu_comparison", [-30000, 750],
                  "30000(L-1)-29250L > 0; L_u >= L-1.")
    positive_poly("zeta_tail_exponential_reduction", [1, -98, 1],
                  "(L-1)^2 >= 96L implies exp((L-1)/4) >= 3L by exp(a)>=a^2/2.")
    exact("weighted_total_rounding", 30000+1, "<", 31000,
          "Pays the finite weighted discrepancy and the zeta tail.")
    positive_poly("disc_log_change", [-4, 0, 0, 1],
                  "L^3>4 gives 2/(xL)<1 using x>=exp(L)>=L^2/2.")
    positive_poly("disc_theta_margin", [-8, 0, 0, 1],
                  "L^3>8 implies 1/(xL)<1/4, hence theta_u>=19/4.")
    positive_poly("weighted_exponent_loss", [-56, -16, 1],
                  "1/(2L)+7/(4L^2)<1/32; bounds delta using u>=L^2/2.")
    exact("summable_exponent", F(1,2)+F(19,32)-F(1,32), "==", F(17,16),
          "Endpoint lower exponent after disc losses.")
    positive_poly("zeta_real_part_margin", [-24, -8, 3],
                  "3/16-1/(2L)-3/(2L^2)>0, so Re w >= 3/2.")
    positive_poly("alpha_magnitude_remainder", [-56, 0, -84, 0, 3],
                  "With pi<22/7 and u>=L^2/2, 3/u+1/u^2<3/14.")
    positive_poly("alpha_magnitude_to_L", [-3, 1],
                  "(L+1)/2+1 <= L.")
    positive_poly("cutoff_lower_bound", [-3, 1],
                  "exp((L-1)/2)>=1+(L-1)/2>=2 gives floor(a)>=a/2.")
    exact("cutoff_logarithmic_correction", F(22,7)*F(1,2)/8, "<", 1,
          "pi*t/8<1 proves log N <= L_u/2+1/u.")
    positive_poly("kappa_exponent", [-13, 0, 1],
                  "u>=L^2/2>13/2 implies 1/[4(u-6)]<1/2.")
    exact("RS_weight_total", (1+2*2)*(1+16), "==", 85,
          "gamma and N^|kappa| bounded by 2; zeta(17/16)<=17.")
    positive_poly("RS_exponent_numerator", [-65, -2, 1],
                  "(L+1)^2/64+1 <= L^2/32.")
    exact("RS_exponent_less_than_one", F(1,8), "<", 1,
          "q<=L^2/(16u)<=1/8 from u>=L^2/2.")
    exact("RS_AB_rounding", F(85,8), "<", 11,
          "e^q-1<=2q supplies this coefficient.")
    positive_poly("RS_AB_exponential_payment", [-264, 1],
                  "exp(L)>=L^4/24>=11L^3.")
    positive_poly("RS_C_first_correction", [-319, -2, 1],
                  "160/(L-1)^2<1/2 pays 20 exp(-(L-1)/2).")
    positive_poly("RS_C_second_correction", [-336, 0, 0, 1],
                  "168/L^3<1/2 pays 7L exp(-L).")
    exact("RS_C_main_decay", F(1,4)+F(19,64), ">", F(1,2),
          "The C-term main exponential has at least half-L_u decay.")
    exact("disc_error_gamma_units", 2*3*31000+3*2, "==", 186006,
          "Two weighted discrepancies plus the entire imported error.")
    exact("disc_error_Q_units", 186006*3, "==", 558018,
          "Reciprocal zeta bound yields Gamma<=3|Q|.")
    exact("disc_error_rounding", 558018, "<", 560000,
          "Rounded bound used before Cauchy differentiation.")
    factors = [factorial(k)*4**k for k in range(4)]
    exact("Cauchy_max_factor", max(factors), "==", 384,
          "Maximum of k!*4^k for k=0,1,2,3.")
    exact("Cauchy_normalized_budget", F(560000,2)*max(factors), "==", 107520000,
          "Normalization divides by 2|Q|(L/4)^k.")
    moments = [integral_moment(F(1,2), k) for k in (1,2,3)]
    for k, (actual, value) in enumerate(zip(moments, (6,26,158)), 1):
        exact(f"zeta_log_derivative_{k}", actual, "==", value,
              "Exact integral majorant for sum (log n)^k n^(-3/2).")
    positive_poly("alpha_derivative_domain", [-288, 0, 1],
                  "x>=L^2/2>144 permits all stated alpha derivative bounds.")
    positive_poly("gamma_carrier_first_derivative", [-112, -14, 17],
                  "pi/8+2/x+L/(4x)<1 using pi<22/7 and x>=L^2/2.")
    positive_poly("gamma_carrier_second_derivative", [-4, -3, -4, 0, 4],
                  "1/L^2+(4+3L)/(4L^4)<1 majorizes |G''|.")
    positive_poly("gamma_carrier_third_derivative", [-18, -9, -6, 0, 0, 0, 4],
                  "3/(2L^4)+(18+9L)/(4L^6)<1 majorizes |G'''|.")
    exact("carrier_log_first", 1+6, "==", 7, "Chain rule and |w'|<=1.")
    exact("carrier_log_second", 1+26+6, "==", 33, "Chain rule with |w'|,|w''|<=1.")
    exact("carrier_log_third", 1+158+3*26+6, "==", 243,
          "Chain rule with first three w derivatives bounded by 1.")
    exact("carrier_third_constant", 7**3+3*7*33+243, "==", 1279,
          "Constant part of exponential derivative formula.")
    exact("carrier_third_linear", 3*7**2+3*33, "==", 246,
          "Linear-in-omega part of third-derivative discrepancy.")
    exact("carrier_third_quadratic", 3*7, "==", 21,
          "Quadratic-in-omega part of third-derivative discrepancy.")
    exact("carrier_first_budget", 7*4, "<", 100, "First carrier jet.")
    positive_poly("carrier_second_budget", [-1312, 44],
                  "56/L+1312/L^2<100/L.")
    positive_poly("carrier_third_budget", [-81856, -3936, 16],
                  "84/L+3936/L^2+81856/L^3<100/L.")
    exact("complete_budget", 107520000+100, "==", 107520100,
          "Cauchy and carrier errors added.")
    exact("complete_budget_rounding", 107520100, "<", 108000000,
          "Uniform bound used in theorem statement.")
    exact("threshold_budget", F(108000000,10**9), "==", F(27,250),
          "At L=10^9 the rounded error bound is exactly 0.108.")
    exact("threshold_meets_one_eighth", F(27,250), "<", F(1,8),
          "Strict margin to the requested normalized four-jet error.")
    exact("norm_lower_bound", 1-4*F(1,8), "==", F(1,2),
          "Note 17 perturbation bound for the first-pair normalized norm.")
    exact("Laguerre_lower_bound", 1-4*F(1,8)-F(1,8)**2, "==", F(31,64),
          "Note 17 perturbation bound for either normalized Laguerre form.")
    failures = [r["name"] for r in checks if not r["passed"]]
    receipt = {
        "schema": "inv21-explicit-outer-constants-v1",
        "date": "2026-10-14", "prepared_for": "Edward Baker",
        "assistance": "Substantial LLM assistance; Codex subagent with independent internal review",
        "model": "gpt-6-astra", "reasoning_effort": "ultra",
        "model_provenance": "Parent agent verified inherited current-turn configuration.",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "candidate": {"L_min_for_algebra": BASE, "L_min_for_signs": 10**9,
                      "X1": "4*pi*exp(10^9)", "normalized_error": "108000000/L"},
        "passed": not failures, "check_count": len(checks), "failures": failures,
        "scope": ["Exact rational arithmetic for stated budgets",
                  "Sufficient polynomial inequalities for every real L>=1000 via nonnegative shifted coefficients",
                  "No floating-point exponential or quadrature evaluation"],
        "not_verified": ["Polymath Theorem 1.3 itself",
                         "Analytic identities and reductions in the accompanying proof",
                         "Analytic facts exp(y)>=sum_{j=0}^m y^j/j! for y>=0, pi<22/7, 2<e<3, log(2)>1/2",
                         "Finite-strip or inner-region coverage; RH"],
        "checks": checks,
    }
    output.write_text(json.dumps(receipt, indent=2)+"\n")
    print(json.dumps({"passed": not failures, "check_count": len(checks),
                      "failures": failures, "output": str(output)}, indent=2))
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("/private/tmp/EXPLICIT_OUTER_CONSTANTS_20261014.json"))
    main(parser.parse_args().output)
