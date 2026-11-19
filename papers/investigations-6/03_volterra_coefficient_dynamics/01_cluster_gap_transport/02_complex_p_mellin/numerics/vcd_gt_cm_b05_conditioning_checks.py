#!/usr/bin/env python3
"""E41 source-free exact-rational imports and Note50 constant checks.

18 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
Actual serving model/effort unavailable; assessor inherited configuration.
This checks recorded enclosures and algebra, not a fresh source certificate.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import sys


HERE = Path(__file__).resolve().parent
CM = HERE.parent
REPO = next(p for p in HERE.parents if (p / "LARGE_FILES.md").is_file())
MANIFEST = CM / "research-progress/handoffs/VCD-GT-CM-E41-inputs-r1.json"
OUTPUT = HERE / "27_VCD_GT_CM_B05_CONDITIONING_CHECKS_20261118.json"


def identity(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(REPO)), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify_inputs():
    manifest = json.loads(MANIFEST.read_text())
    verified = []
    for expected in manifest["inputs"]:
        actual = identity(REPO / expected["path"])
        if actual != expected:
            raise ValueError("Frozen input differs: " + expected["path"])
        verified.append({**actual, "matches": True})
    return verified


def ball(text):
    """Enclose printed decimal midpoint/radius strings exactly, no floats."""
    if not isinstance(text, str):
        raise TypeError("A recorded enclosure must be textual")
    if not text.startswith("["):
        value = F(text)
        return value, value
    match = re.fullmatch(r"\[([^\[\]]+) \+/- ([^\[\]]+)\]", text)
    if match is None:
        raise ValueError("Unsupported recorded enclosure: " + text)
    midpoint, radius = map(F, match.groups())
    if radius < 0:
        raise ValueError("Negative enclosure radius")
    return midpoint - radius, midpoint + radius


def main():
    verified = verify_inputs()
    source = json.loads((HERE / "22_VCD_GT_CM_CARDINAL_SOURCE_REFINEMENT_20261118.json").read_text())
    control = json.loads((HERE / "25_VCD_GT_CM_E40_APPROXIMATION_CHECKS_20261118.json").read_text())
    can = source["canonical"]
    whole = can["whole_interval"]["bounds"]
    checks = []

    def check(name, condition, **values):
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "passes": True,
                       "exact_values": {k: str(v) for k, v in values.items()}})

    center_lo = ball(whole["center_offset"]["lower"])[0]
    center_hi = ball(whole["center_offset"]["upper"])[1]
    D_lo = ball(whole["D"]["lower"])[0]
    M_lo = ball(whole["M"]["lower"])[0]
    M_hi = ball(whole["M"]["upper"])[1]
    endpoint_lo = ball(can["centered_direct"]["lower"])[0]
    endpoint_hi = ball(can["centered_direct"]["upper"])[1]
    geom_lo = ball(can["geometry"]["real_half_plane_lower_bounds"][1])[0]
    geom_hi = ball(can["geometry"]["modulus_upper_bounds"][1])[1]

    check("record_success_and_count", source["success"] and can["all_gates"]
          and can["count_on_each_boundary"] == 2)
    check("center_import", F(".0594948984") < center_lo <= center_hi < F(".0637644306"))
    check("positive_D_M_import", D_lo > 0 and M_lo > 0)
    check("M_range_import", F(".599312") < M_lo <= M_hi < F(".615573") < F(".616"))
    check("endpoint_import", F(".00082198577") < endpoint_lo <= endpoint_hi < F(".000823"))
    check("derivative_import", can["whole_time_monotonicity"]["all_gates"]
          and F(can["whole_time_monotonicity"]["derivative_lower_strict"]) == F(942, 625))
    check("outer_geometry_import", geom_lo > 1160000 and geom_hi < 4670000)

    Delta = F(1, 1024)
    r0, r, inner = F(4, 5), F(2, 5), F(3, 10)
    short_D = F(".000823") + 2 * (Delta + F(".0003"))
    long_D = F(".00082198577") + F(942, 625) * F(".1003")
    check("short_tube_D", short_D == F(".003376125") < F(1, 64), upper=short_D)
    check("long_interval_size_failure", long_D == F(".15199414577") > F(1, 16), lower=long_D)
    check("exterior_clearance", F("1.05") - F(".064") == F(".986") > r0)
    check("chart_drift", center_hi-center_lo < F(".00427") < r0/32)
    check("collar_parameter_ratios", F(1, 64) <= r0*r0/16 and F(1, 2) <= F(4, 5) <= 1)
    check("collar_a_at_least_two_via_logT_gt3", 14000 > 64 and F(4, 5)*3 > 2)

    q_inner = 57*r0*r0/1024
    q = 161*r0*r0/1024
    boundary_Q = F("1.114")**2 + F(".004")
    boundary_G_lower = 1160000 * F("1.05")**2
    boundary_G_upper = 4670000 * F("1.05")**2
    check("deflated_floor", boundary_Q == F("1.244996") and boundary_G_lower > 1000000*boundary_Q,
          Q_upper=boundary_Q, G_lower=boundary_G_lower)
    check("field_upper", boundary_G_upper < 5200000, upper=boundary_G_upper)
    check("new_circle_floors", q_inner == F(".035625") and q == F(".100625"))
    hG = 1000000*q_inner
    check("h_G", hG == 35625)
    check("Cauchy_padding", F(".064")+r+F(1, 2) < F("1.05"))
    K1 = 2*5200000
    check("K1_ratio", F(K1, 1)/hG < 300, ratio=F(K1, 1)/hG)
    check("trivial_tolerance_screen", 4*Delta*F(".616") < F(".002407") < F(".01"))
    coarse = 4*Delta*(F(".615573")-F(".599312"))/2
    check("coarse_midpoint_tolerance", coarse < F("3.176e-5"), error_upper=coarse)

    x0, x1 = F("1e-11"), F("1e-8")
    b = 2*x1+600*x0
    check("quotient_gate", x0 < F(1, 2) and b == F("2.6e-8"))
    ec1 = r*r/2
    eD1 = r**3/2+(r0/16)*ec1
    eD2 = ec1*ec1
    ustar = 17*r0/32
    eQ1 = 2*ustar*ec1+eD1
    eQ2 = ec1*ec1+eD2
    check("coordinate_coefficients", (ec1,eD1,eD2,eQ1,eQ2) ==
          tuple(map(F,[".08",".036",".0064",".104",".0128"])))
    check("kernel_constants", 2/q < 20 and (2/q)**2 < 400)
    coefficient = r*(20+300*400*(eQ1+eQ2))
    check("moment_coefficient", coefficient < 6000, coefficient=coefficient)
    check("denominator_gate", eQ1*b+eQ2*b*b < q/2)
    log_error = 4*Delta*6000*b
    check("log_consumer", log_error == F("6.09375e-7") < F("1e-6"), upper=log_error)
    check("integration_reserve", log_error+F("3e-7") < F("1e-6"), total=log_error+F("3e-7"))

    exponent = F(14000**2, 1)/(4*(1+Delta))
    check("global_exponent", exponent == F(14000**2*256,1025) > 48000000, lower=exponent)
    check("cutoff_cap_log_comparison", 48000000 > 40)
    beta = 1/(1+Delta)
    p, Y, d0 = F(1,16), F(1,4), F(".5265")
    check("padded_core", F(".064")+r+p == d0 and d0+Y == F(".7765") < F("1.05"))
    check("radial_cover", F("14010.1")+d0 < 14011)
    v_squared_at_half = F(1,4)*beta/(4*Delta)
    check("erfc_argument_bound", v_squared_at_half < 64, v_squared=v_squared_at_half)
    check("tail_exponent_screen", exponent-81-40 > 0, lower=exponent-81-40)

    quartic=control["quartic"]
    check("exact_quartic_preserved_import", quartic["coefficient_identity_pass"]
          and quartic["strong_collar"]["rational_subchecks_pass"]
          and F(quartic["strong_collar"]["E_N"]) == 0)
    if verify_inputs() != verified:
        raise ValueError("Inputs changed during checks")
    record={
        "task":"VCD-GT-CM-E41 r1", "date":"2026-11-18", "timezone":"America/New_York",
        "prepared_for":"Edward Baker", "assistance":"OpenAI Codex LLM assistance; nonauthor internal shared-premise assessment",
        "actual_serving_model":None, "actual_serving_effort":None,
        "configuration":"inherited; no serving attestation or inferred settings",
        "status":"exact-rational recorded-input and algebra checks passed",
        "script":identity(Path(__file__).resolve()), "input_manifest":identity(MANIFEST),
        "verified_inputs":verified, "arithmetic":"Python standard-library fractions.Fraction; exact decimal/radius parsing",
        "python_version":sys.version.split()[0], "checks":checks, "all_passed":True,
        "noncomputational_proof_inputs":[
            "log 2<1 and log 2>1/2 by its defining integral",
            "erfc(8)>exp(-81) by integration over [8,9] and pi<4",
            "maximum/minimum modulus and Cauchy formulas",
            "analytical Gaussian-tail integration and omitted-product argument in Note50"
        ],
        "limits":{
            "new_source_calls":0,"new_zero_calls":0,"source_certificate_replay":False,
            "Gaussian_numerical_integration":False,"numerical_feasibility_campaign":False,
            "actual_error_lower_bound":False,"general_complexity_lower_bound":False,
            "specialist_review":False,
            "scope":"checks algebra and previously recorded enclosures; does not independently reproduce Record22"
        }
    }
    OUTPUT.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"passed","checks":len(checks),"inputs":len(verified),"output":str(OUTPUT.relative_to(REPO))}))


if __name__ == "__main__":
    main()
