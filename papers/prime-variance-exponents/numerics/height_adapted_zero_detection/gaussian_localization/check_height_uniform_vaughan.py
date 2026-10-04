"""Exact rational certificates for the height-uniform Vaughan note.

Prepared for Edward Baker with substantial LLM assistance, 4 Oct 2026.
Model: GPT-6 (Codex), inherited configuration; exact variant/effort unknown.
No numerical-grid assertion or independent arithmetic estimate is used.
"""

from fractions import Fraction as F
from math import comb, factorial
from hashlib import sha256
from pathlib import Path
import json


def qtext(x):
    x = F(x)
    return str(x.numerator) + "/" + str(x.denominator)


checks = {}
records = {}

# Exact polynomial integral: integral_{-1/4}^{1/4} h(v)^2 dv.
a0 = sum(F((-1)**j * comb(16,j),2*(2*j+1)) for j in range(17))
checks["h_L2_norm_above_13_over_40"] = a0 > F(13,40)**2
records["h_L2_norm_squared"] = qtext(a0)

# The exact coefficient majorant on |v|<=1/4 is
# 4^m sum_j binom(8,j) (2j)_m. Each (2j)_m<=16^m.
majorants = []
for m in range(10):
    exact = 4 ** m * sum(
        comb(8, j) * factorial(2*j) // factorial(2*j-m)
        for j in range(9) if 2*j >= m
    )
    bound = 256 * 64 ** m
    checks["h_derivative_coefficient_majorant_m" + str(m)] = exact <= bound
    majorants.append({"m": m, "exact_majorant": exact, "upper": bound})
records["h_derivative_majorants"] = majorants

c0 = 8 ** 8 * factorial(8)
checks["endpoint_atom_pair_below_2pow41"] = 2*c0 < 2 ** 41
checks["ninth_variation_below_2pow62"] = 2 ** 61 + 2*c0 < 2 ** 62
records["endpoint_atom_single"] = c0

T = F(100)
coefficient_ratio = (1 + 3*T + (3*T*T + F(1,4))
                     + (T**3 + T/F(4))) / (F(13,40)*T**3)
checks["A_coefficient_sum_below_four"] = coefficient_ratio < 4
records["A_coefficient_sum_at_T100_upper"] = qtext(coefficient_ratio)

# Every normalized factor 1+(ell+3/2)/T decreases with T.
polynomial_ratios = []
for j in range(7):
    ratio = F(1)
    for ell in range(j):
        ratio *= (T + ell + F(3,2))/T
    checks["D_polynomial_coefficient_sum_j" + str(j)] = ratio < 2
    polynomial_ratios.append({"j": j, "upper_at_T100": qtext(ratio)})
records["D_polynomial_coefficient_ratios"] = polynomial_ratios

# log(2)=2 sum_{j>=0} (1/3)^(2j+1)/(2j+1).
# The first two positive terms are a lower bound. Bound the remaining
# denominators from below by 5 to obtain a rational upper bound.
log2_lower = F(56,81)
log2_upper = log2_lower + F(1,540)
checks["exp_11_over_8_below_four"] = 2*log2_lower > F(11,8)
checks["log2_below_seven_tenths"] = log2_upper < F(7,10)
checks["log2_below_three_quarters"] = log2_upper < F(3,4)
# -log(3/4)=2 atanh(1/7)>2/7>1/4, so exp(-1/4)>3/4.
checks["A_above_three_quarters"] = F(2,7) > F(1,4)
checks["A_reciprocal_seventh_below_eight"] = F(7,4) < 3*log2_lower
records["log2_rational_lower"] = qtext(log2_lower)
records["log2_rational_upper"] = qtext(log2_upper)

factorial_sum_ratio = sum(F(factorial(6),factorial(j))*T**(j-6)
                          for j in range(7))
checks["sixth_leibniz_sum_below_two"] = factorial_sum_ratio < 2
records["sixth_leibniz_sum_at_T100"] = qtext(factorial_sum_ratio)

# The retained terms, relative to 2^67 T^7, from the deliberately
# overestimated endpoint identity and logarithmic product rule.
ell7_coefficient = F(96) + F(144,100)
elllog7_coefficient = F(128) + F(336,100)
checks["ell_seventh_variation_below_2pow74"] = ell7_coefficient < 128
checks["ell_log_seventh_variation_below_2pow75"] = elllog7_coefficient < 256
records["ell_seventh_coefficient_in_2pow67_units"] = qtext(ell7_coefficient)
records["ell_log_seventh_coefficient_in_2pow67_units"] = qtext(elllog7_coefficient)

# zeta(7)<2, pi>3 imply kappa_7<4/6^7<2^-16.
checks["poisson_kappa7_below_2pow_minus16"] = F(4,6**7) < F(1,2**16)
records["poisson_kappa7_rational_upper"] = qtext(F(4,6**7))

logU_N_coefficient = F(27*24,56)-F(1,2)-F(31,140)
logU_constant = F(27*24,56)-F(39,7)*F(7,10)
checks["cutoff_logU_coefficient"] = logU_N_coefficient == F(217,20)
checks["cutoff_logU_constant"] = logU_constant == F(537,70)
checks["cutoff_logU_above_ten_N"] = logU_N_coefficient > 10 and logU_constant > 0
checks["Vaughan_error_two_terms_below_2pow_minus10"] = 2**60*F(1,2**70) == F(1,2**10)
records["logU_N_coefficient"] = qtext(logU_N_coefficient)
records["logU_constant"] = qtext(logU_constant)

assert all(checks.values()), {k:v for k,v in checks.items() if not v}
result = {
    "date": "2026-10-04",
    "prepared_for": "Edward Baker",
    "model": "GPT-6 (Codex), inherited configuration; exact variant and reasoning effort not exposed",
    "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "claim_scope": "exact rational ingredients for the analytic height-uniform bounds; no evaluation or cancellation estimate of the retained arithmetic sum",
    "checks": checks,
    "records": records,
    "status": "checks passed; signed arithmetic bound remains unproved",
}
target = Path(__file__).resolve().with_name("height_uniform_vaughan_record_20261004.json")
target.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({"record":str(target), "source_sha256":result["source_sha256"],
                  "checks_passed":len(checks), "scope":result["claim_scope"]},indent=2))
