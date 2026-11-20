"""Replay AGC-JH-E07 r1. Omit --output to write the record to stdout.

Prepared for Edward Baker, 19 November 2026, with OpenAI Codex assistance.
Requested execution model gpt-6.2-sol / ultra. Serving metadata unavailable.
"""

import argparse
from datetime import datetime
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import platform
from time import perf_counter
from zoneinfo import ZoneInfo

import flint
from flint import arb, ctx

from e07_chart import ChartFailure, certify_chart
from e07_fields import build_fields


HERE = Path(__file__).resolve().parent
REQUEST = HERE.parent / "research-progress/handoffs/AGC_JH_E07_REQUEST_R1_20261119.md"
REQUEST_SHA256 = "f0e1a470a96d9db051bb7b3f0d9c7e8eec0362946746cfcb94cc2626b72bfdc0"
LEVELS = ((24, 768, 512), (28, 1280, 4096))
BRACKETS = ((28, 29), (42, 43))
BISECTIONS = 120
CENTER, RADIUS, INNER, BUFFER = 36, 9, 8, 1


class GateFailure(ValueError):
    """A measured failure under the frozen budget."""


def ball(value):
    """Serialize the exact Arb midpoint and magnitude radius as rationals."""
    if not value.is_finite():
        raise GateFailure("nonfinite Arb enclosure")
    midpoint = Fraction(str(value.mid().fmpq()))
    radius = Fraction(str(value.rad().fmpq()))
    return {
        "midpoint": str(midpoint),
        "radius": str(radius),
        "lower": str(midpoint - radius),
        "upper": str(midpoint + radius),
    }


def evaluate(coefficients, point, error):
    shifted = point - CENTER
    value = arb(0)
    for coefficient in reversed(coefficients):
        value = value * shifted + coefficient
    return value + arb(0, error.abs_upper())


def sign(value):
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def bisect_root(coefficients, error, endpoints, observations):
    left, right = map(arb, endpoints)
    f_left = evaluate(coefficients, left, error)
    f_right = evaluate(coefficients, right, error)
    observations.update(endpoint_values=[ball(f_left), ball(f_right)],
                        evaluations=2, bisections=0, unresolved_midpoint=False)
    left_sign = sign(f_left)
    if left_sign == 0 or sign(f_right) != -left_sign:
        raise GateFailure(f"unresolved opposite signs at {endpoints}")
    for _ in range(BISECTIONS):
        midpoint = (left + right) / 2
        midpoint_sign = sign(evaluate(coefficients, midpoint, error))
        observations["evaluations"] += 1
        if midpoint_sign == 0:
            observations["unresolved_midpoint"] = True
            break
        if midpoint_sign == left_sign:
            left = midpoint
        else:
            right = midpoint
        observations["bisections"] += 1
    result = left.union(right)
    if not (result - CENTER).abs_upper() < INNER:
        raise GateFailure(f"retained bracket touches the inner boundary at {endpoints}")
    observations["root"] = ball(result)
    return result


def roots(coefficients, error, observations):
    result = []
    for endpoints in BRACKETS:
        details = {"initial_endpoints": list(endpoints)}
        observations.append(details)
        result.append(bisect_root(coefficients, error, endpoints, details))
    return result


def correction(f, y, ef, ey, eta, output):
    costs = output["costs"]
    start = perf_counter()
    reference_brackets = output["Y_real_brackets"] = []
    target_brackets = output["F_real_brackets"] = []
    xy = roots(y, ey, reference_brackets)
    costs["reference_root_seconds"] = perf_counter() - start
    costs["reference_root_polynomial_evaluations"] = sum(v["evaluations"] for v in reference_brackets)
    start = perf_counter()
    xf = roots(f, ef, target_brackets)
    costs["direct_F_root_seconds"] = perf_counter() - start
    costs["direct_F_root_polynomial_evaluations"] = sum(v["evaluations"] for v in target_brackets)
    output["counts_and_buffer"] = {
        "F_outer": 2, "Y_outer": 2, "F_inner": 2, "Y_inner": 2,
        "inner_radius": INNER, "buffer": BUFFER,
        "strict_radial_root_upper": ball(max((x - CENTER).abs_upper() for x in xy + xf)),
        "reason": "HDC and zero strip with F sign brackets; collar Rouche for Y; "
                  "two disjoint sign brackets for each field strictly inside radius 8",
    }

    start = perf_counter()
    length = max(len(f), len(y))
    difference = [
        (f[k] if k < len(f) else arb(0)) - (y[k] if k < len(y) else arb(0))
        for k in range(length)
    ]
    derivative = [k * coefficient for k, coefficient in enumerate(y) if k != 0]
    values = output["residues"] = []
    ratios = []
    for x in xy:
        numerator = evaluate(difference, x, ef + ey)
        # Unit Cauchy disk fits inside the radius-10 Taylor domain.
        slope = evaluate(derivative, x, ey)
        values.append({"F_minus_Y_at_Y_root": ball(numerator), "Y_prime": ball(slope)})
        if sign(slope) == 0:
            raise GateFailure("Y derivative enclosure contains zero at a retained root")
        ratios.append(numerator / slope)
        values[-1]["quotient"] = ball(ratios[-1])
    half_y = (xy[1] - xy[0]) / 2
    j = -half_y * (ratios[1] - ratios[0])
    dy = half_y ** 2
    log_bound = -(-eta).log1p()
    linear_factor = RADIUS * (2 * RADIUS - BUFFER)
    center_square = RADIUS ** 2 * log_bound ** 2 / 4
    nonlinear = linear_factor * (log_bound - eta)
    allowance = (nonlinear + center_square).abs_upper()
    unsigned_allowance = (linear_factor * log_bound + center_square).abs_upper()
    signed_change = j + arb(0, allowance)
    signed_gap = dy + signed_change
    unsigned_change = arb(0, unsigned_allowance)
    unsigned_gap = dy + unsigned_change
    costs["signed_functional_and_allowance_seconds"] = perf_counter() - start
    costs["signed_residue_polynomial_evaluations"] = 4

    start = perf_counter()
    half_f = (xf[1] - xf[0]) / 2
    direct_gap = half_f ** 2
    direct_change = (half_f - half_y) * (half_f + half_y)
    costs["direct_gap_arithmetic_seconds"] = perf_counter() - start
    output["allowances"] = {
        "analytic_phase_e": "0", "eta_upper": ball(eta),
        "minus_log_one_minus_eta": ball(log_bound),
        "curvature_log_component": ball(nonlinear),
        "center_square_component": ball(center_square),
        "signed_A_upper": ball(allowance), "unsigned_A_upper": ball(unsigned_allowance),
        "F_value_tail_upper": ball(ef), "Y_value_tail_upper": ball(ey),
        "Y_first_derivative_tail_upper": ball(ey),
        "value_tail_scope": "|z-36|<=10", "weight": "W(0,0)=1",
    }
    enclosures = {
        "D_Y": dy, "J": j,
        "signed_D_F": signed_gap, "unsigned_D_F": unsigned_gap, "direct_D_F": direct_gap,
        "signed_gap_change": signed_change, "unsigned_gap_change": unsigned_change,
        "direct_gap_change": direct_change,
    }
    output["results"] = {
        **{name: ball(value) for name, value in enclosures.items()},
        "widths": {name: ball(2 * value.rad()) for name, value in enclosures.items()},
        "J_sign": sign(j), "direct_gap_change_sign": sign(direct_change),
        "J_magnitude_exceeds_signed_A": j.abs_lower() > allowance,
    }
    output["acceptance_gates"] = {
        "eta_strictly_less_than_one": eta < 1,
        "outer_and_inner_counts_and_common_buffer": True,
        "J_sign_resolved": sign(j) != 0,
        "paid_signed_gap_lower_positive": signed_gap > 0,
        "signed_D_F_overlaps_direct": signed_gap.overlaps(direct_gap),
        "signed_gap_change_overlaps_direct": signed_change.overlaps(direct_change),
    }


def attempt(n, bits, sectors):
    output = {"N": n, "bits": bits, "sector_cap_per_radius": sectors, "costs": {}}
    costs = output["costs"]
    start = perf_counter()
    stage = "field acquisition"
    tick = start
    try:
        f, y, ef, ey, output["fields"] = build_fields(n, bits)
        costs["field_acquisition_seconds"] = perf_counter() - tick
        stage = "contour clearance"
        tick = perf_counter()
        eta, output["chart"] = certify_chart(f, y, ef, ey, sectors)
        costs["contour_clearance_seconds"] = perf_counter() - tick
        eta = eta.abs_upper()
        output["eta_upper"] = ball(eta)
        if not eta < 1:
            raise GateFailure("relative collar bound reaches one")
        stage = "signed and direct comparison"
        tick = perf_counter()
        correction(f, y, ef, ey, eta, output)
        costs["signed_and_direct_seconds"] = perf_counter() - tick
        if not all(output["acceptance_gates"].values()):
            failures = [key for key, passed in output["acceptance_gates"].items() if not passed]
            raise GateFailure("acceptance gates: " + ", ".join(failures))
    except (ValueError, ArithmeticError) as error:
        if isinstance(error, ChartFailure):
            output["chart"] = error.metadata
        output.update(status="failed", failed_stage=stage, failure=str(error))
        costs["stage_seconds_on_failure"] = perf_counter() - tick
    else:
        output["status"] = "accepted"
    costs["attempt_wall_seconds"] = perf_counter() - start
    return output


def run():
    if sha256(REQUEST.read_bytes()).hexdigest() != REQUEST_SHA256:
        raise ValueError("frozen AGC-JH-E07 request digest mismatch")
    timezone = ZoneInfo("America/New_York")
    started = datetime.now(timezone)
    start = perf_counter()
    ctx.threads = 1
    attempts = []
    for level in LEVELS:
        result = attempt(*level)
        attempts.append(result)
        if result["status"] == "accepted":
            break
    inputs = {
        name: sha256((HERE / name).read_bytes()).hexdigest()
        for name in ("certify_e07.py", "e07_fields.py", "e07_chart.py")
    }
    return {
        "task": "AGC-JH-E07 r1",
        "author": "Prepared for Edward Baker with OpenAI Codex LLM assistance",
        "dispatch": {"requested_model": "gpt-6.2-sol", "requested_effort": "ultra",
                     "independent_serving_metadata": None},
        "started": started.isoformat(), "finished": datetime.now(timezone).isoformat(),
        "wall_seconds": perf_counter() - start,
        "runtime": {"python": platform.python_version(), "python_flint": flint.__version__,
                    "flint": flint.__FLINT_VERSION__, "flint_threads": ctx.threads},
        "request_sha256": REQUEST_SHA256, "replay_sha256": inputs,
        "physical_time": "0", "contour": {"center": CENTER, "radius": RADIUS,
                                          "inner_radius": INNER, "buffer": BUFFER},
        "allowance_accounting": "The two calculations share F, Y, source tails and counts.",
        "scope": "Known-coverage conditioning at one physical-time slice",
        "status": result["status"], "attempts": attempts,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New record path. Omit to emit JSON to stdout.")
    args = parser.parse_args()
    if args.output is not None and args.output.exists():
        parser.error("output path already exists")
    record = run()
    payload = json.dumps(record, indent=2, allow_nan=False) + "\n"
    if args.output is None:
        print(payload, end="")
    else:
        with args.output.open("x", encoding="utf-8") as saved:
            saved.write(payload)
    return 0 if record["status"] == "accepted" else 2


if __name__ == "__main__":
    raise SystemExit(main())
