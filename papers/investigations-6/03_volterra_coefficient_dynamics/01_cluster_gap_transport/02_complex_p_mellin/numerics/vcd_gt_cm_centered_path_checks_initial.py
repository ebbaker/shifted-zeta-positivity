#!/usr/bin/env python3
"""E42 fixed source-free exact-rational checks for Note51.

18 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
Actual model/effort unavailable; inherited configuration. This checks
algebra and bound inputs, not source values or Gaussian quadrature.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
CM = HERE.parent
REPO = next(p for p in HERE.parents if (p / "LARGE_FILES.md").is_file())
MANIFEST = CM / "research-progress/handoffs/VCD-GT-CM-E42-inputs-r1.json"
OUTPUT = HERE / "28_VCD_GT_CM_CENTERED_PATH_CHECKS_20261118.json"


def identity(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(REPO)), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify_inputs():
    result = []
    for expected in json.loads(MANIFEST.read_text())["inputs"]:
        actual = identity(REPO / expected["path"])
        if actual != expected:
            raise ValueError("Frozen input differs: " + expected["path"])
        result.append({**actual, "matches": True})
    return result


def main():
    verified = verify_inputs()
    checks = []

    def check(name, condition, **values):
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "passes": True,
                       "exact_values": {k: str(v) for k, v in values.items()}})

    a, R, d0 = F("14010.1"), F(14011), F(".5265")
    Delta, v = F(1,1024), F(1,16)
    alpha, beta = F(9999,10000), F(131,100)
    N_boundary = 2*R+1
    check("source_domain", d0 < 2 and 0 < Delta < F(1,10))
    check("Gaussian_shift_normalization", v*v == 4*Delta)
    check("radial_cover", a+d0 < R)
    check("central_source_disk", d0+8*v == F("1.0265") < F("1.05"))
    check("L_N_strict_boundary", (N_boundary/2-R)/v == 8)
    check("product_denominator", 1-F(1,2)**2 == F(3,4))
    check("calibration_factor_modulus", 2*(N_boundary*N_boundary-2) > a*a)
    check("calibration_log_denominator", 1-(a/N_boundary)**2 > F(3,4))

    c0 = F(4,3)*d0*(2*a+d0)
    c1 = F(8,3)*(a+d0)*v
    c2 = F(4,3)*v*v
    check("ratio_polynomial_coefficients", c0 == F(4,3)*(2*a*d0+d0*d0)
          and c1 == F(4,3)*(2*a*v+2*d0*v) and c2 == F(1,192),
          c0=c0, c1=c1, c2=c2)
    check("core_constant_floor", c0 > 19000)
    E_star = 1/(16*a)
    check("positive_Gaussian_parameters", 1-E_star*c2 > 0 and alpha-E_star*c2 > 0,
          E_star=E_star, central=1-E_star*c2, middle=alpha-E_star*c2)
    check("rate_coefficients_nonnegative", c0 > 0 and c1 > 0 and c2 > 0
          and beta+E_star*c1 > 0)

    lam = 1/(8*(1+Delta))
    b = 1-8*lam*Delta
    check("far_Gaussian_parameter", b == 1-2*lam*v*v == F(1024,1025), b=b)
    A = 2*R*R+F(4,3)*a*a
    check("far_positive_coefficients", A > 0 and v*v/b > 0 and 2*v*v > 0)
    check("far_L_bound", 8*b > 2)

    mass_poly_integral = 2*(1-F(1,3))
    check("Gaussian_mass_lower_bound_coefficients", mass_poly_integral/2 == F(2,3),
          integral_of_one_minus_r_squared=mass_poly_integral)
    core_floor = F(2,3)*5200000*19000*10/(2**40)
    check("positive_core_allowance_floor", core_floor > F(1,2), lower=core_floor)
    h, K1, r, q = F(35625), F(10400000), F(2,5), F(".100625")
    check("quotient_coefficient_floor", K1/(h*h) > F(1,128), coefficient=K1/(h*h))
    check("moment_coefficient_floor", 2*r/q > 7, coefficient=2*r/q)
    consumer_floor = 4*Delta*F(7,256)
    check("actual_consumer_allowance_failure", consumer_floor == F(7,65536) > F("1e-6"),
          lower=consumer_floor)

    control = json.loads((HERE/"25_VCD_GT_CM_E40_APPROXIMATION_CHECKS_20261118.json").read_text())
    check("inherited_exact_quartic", control["quartic"]["coefficient_identity_pass"]
          and F(control["quartic"]["strong_collar"]["E_N"]) == 0)
    if verify_inputs() != verified:
        raise ValueError("Inputs changed during checks")
    record = {
        "task":"VCD-GT-CM-E42 r1", "date":"2026-11-18", "timezone":"America/New_York",
        "prepared_for":"Edward Baker", "assistance":"OpenAI Codex LLM assistance; nonauthor internal shared-premise assessment",
        "actual_serving_model":None, "actual_serving_effort":None,
        "configuration":"inherited; prior E41 assessor, without serving attestation",
        "status":"fixed source-free exact-rational checks passed",
        "script":identity(Path(__file__).resolve()), "input_manifest":identity(MANIFEST),
        "verified_inputs":verified, "arithmetic":"Python standard-library fractions.Fraction; no floating samples",
        "python_version":sys.version.split()[0], "checks":checks, "all_passed":True,
        "analytical_proof_checks_not_established_by_the_script":[
            "GT Note12 equation (8) applies to every real Gaussian variable in the stated disk/time domain",
            "Gaussian integral J and its I1/I2 integration-by-parts recurrences",
            "nonnegative-integrand extensions defining Acent and the fixed E_star linear rate",
            "omitted-product logarithm is used only through L_N; separate far-path envelope includes calibration mismatch",
            "erfc(x)<=exp(-x^2)/(sqrt(pi)x) for x>0",
            "log L<=L<=bL^2/2 for L>=8 and b=1024/1025",
            "exp(-r^2)>=1-r^2 and sqrt(pi)<2 give Gaussian mass greater than 2/3"
        ],
        "limits":{
            "new_source_calls":0,"new_zero_calls":0,"Gaussian_numerical_quadrature":False,
            "source_certificate_replay":False,"numerical_feasibility_scan":False,
            "actual_error_lower_bound":False,"general_complexity_lower_bound":False,
            "specialist_review":False,
            "scope":"checks algebra and bound identities, with source estimates inherited and proof reviewed separately"
        }
    }
    OUTPUT.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"passed","checks":len(checks),"inputs":len(verified),"output":str(OUTPUT.relative_to(REPO))}))


if __name__ == "__main__":
    main()
