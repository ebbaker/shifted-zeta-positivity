"""Replay the frozen AGC-JH-E08 real slab. Omit --output for JSON stdout.

19 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
Requested execution configuration gpt-6.2-sol / ultra. Serving metadata unavailable.
"""

import argparse
from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
import platform
from time import perf_counter
from zoneinfo import ZoneInfo

import flint
from flint import arb, ctx, fmpq

from certify_e07 import ball
from e08_chart import ChartFailure, Field, certify_collar, root_tubes
from e08_head import build_head
from e08_source import build_source


HERE = Path(__file__).resolve().parent
REQUEST = HERE.parent / "research-progress/handoffs/AGC_JH_E08_REQUEST_R1_20261119.md"
REQUEST_SHA = "fa8b897bb986e663b6055e11ae5aa02d6afc7c2ccf54825b9b84b9b47b201e4f"
ANCHOR = HERE / "05_AGC_JH_E07_CERTIFICATE_20261119.json"
ANCHOR_SHA = "ff76aeb4ae3c08ce62d9e4d5c92ef06e11ee91b99c1da5c532a8d215b86b8956"
LEVELS = ((10, 768, 144, 192, 512), (14, 1280, 160, 240, 1024))


def read_verified(path, digest):
    data = path.read_bytes()
    if sha256(data).hexdigest() != digest:
        raise ValueError(f"frozen input does not match SHA-256: {path.name}")
    return data


def allowance(eta):
    k = -(-eta).log1p()
    nonlinear = 153 * (k - eta)
    center = 81 * k ** 2 / 4
    return k, nonlinear, center, (nonlinear + center).upper(), (153 * k + center).upper()


def enclose_change(fields, time, eta, output):
    f, y, difference = fields
    costs = output["costs"] = {}
    start = perf_counter()
    output["F_brackets"] = []
    x = root_tubes(f, time, output["F_brackets"])
    output["Y_brackets"] = []
    h = root_tubes(y, time, output["Y_brackets"])
    for brackets, tubes in ((output["F_brackets"], x), (output["Y_brackets"], h)):
        for bracket, (root, slope) in zip(brackets, tubes):
            bracket.update(root=ball(root), slope=ball(slope))
    costs["common_bracket_seconds"] = perf_counter() - start

    start = perf_counter()
    numerators = [difference.real_range(root, time) for root, _ in h]
    costs["common_subtracted_numerator_seconds"] = perf_counter() - start
    output["shared_numerator_at_Y_root"] = list(map(ball, numerators))

    start = perf_counter()
    s_y = (h[1][0] - h[0][0]) / 2
    dy = s_y ** 2
    ratios = [numerator / slope for numerator, (_, slope) in zip(numerators, h)]
    j = -s_y * (ratios[1] - ratios[0])
    k, nonlinear, center, a, unsigned_a = allowance(eta)
    signed_change = j + arb(0, a)
    unsigned_change = arb(0, unsigned_a)
    output["allowances"] = {
        "analytical_phase_discrepancy": 0,
        "negative_log_1_minus_eta": ball(k),
        "nonlinear_log_term_upper": ball(nonlinear.upper()),
        "center_square_term_upper": ball(center.upper()),
        "A_upper": ball(a),
        "unsigned_upper": ball(unsigned_a),
    }
    output["signed_ratios"] = list(map(ball, ratios))
    output["signed_partial"] = {
        "J": ball(j), "signed_change": ball(signed_change),
        "paid_target_gap": ball(dy + signed_change),
    }
    costs["signed_calculation_seconds"] = perf_counter() - start

    start = perf_counter()
    displacements, slopes = [], []
    for numerator, (xr, _), (yr, _) in zip(numerators, x, h):
        # At each time the MVT slope point lies on this real segment.
        # The numerator is evaluated at that time's head root in both paths.
        slope = f.real_range(xr.union(yr), time, derivative=True)
        slopes.append(ball(slope))
        output["direct_segment_F_slopes"] = slopes
        if slope.contains(0):
            raise ChartFailure(f"direct segment slope contains zero: {slope.str(12)}")
        displacements.append(-numerator / slope)
    delta = displacements[1] - displacements[0]
    direct_change = delta * (s_y + delta / 4)
    output["direct_root_displacements"] = list(map(ball, displacements))
    costs["direct_calculation_seconds"] = perf_counter() - start

    values = {
        "half_gap_Y": s_y, "D_Y": dy, "J": j,
        "signed_change": signed_change, "direct_change": direct_change,
        "unsigned_change": unsigned_change,
        "paid_target_gap": dy + signed_change,
        "direct_target_gap": dy + direct_change,
        "unsigned_target_gap": dy + unsigned_change,
    }
    output["values"] = {name: ball(value) for name, value in values.items()}
    output["width_uppers"] = {name: ball(2 * value.rad()) for name, value in values.items()}
    return values, x, h


def stored_ball(item):
    return arb(fmpq(item["midpoint"]), fmpq(item["radius"]))


def anchor_checks(values, x, y, original):
    checks = {}
    for new, old in {
        "J": "J",
        "signed_change": "signed_gap_change",
        "direct_change": "direct_gap_change",
        "D_Y": "D_Y",
        "direct_target_gap": "direct_D_F",
    }.items():
        checks[f"{new}_overlaps_E07"] = values[new].overlaps(stored_ball(original["results"][old]))
    for label, pair in (("F", x), ("Y", y)):
        for i, (root, _) in enumerate(pair):
            old = original[f"{label}_real_brackets"][i]["root"]
            checks[f"{label}_root_{i + 1}_overlaps_E07"] = root.overlaps(stored_ball(old))
    return checks


def collision_check():
    # Exact control from Note07: on the same circle reference w²−1 and
    # target w² have a certified collar, but no two distinct target roots.
    # The residue gives J=−1 and D_Y=1, so the paid lower gap cannot pass.
    eta = (1 / ((9 - arb(1) / 64) ** 2 - 1)).upper()
    _, _, _, a, _ = allowance(eta)
    reference = (arb(-1), arb(1))
    target = (arb(0), arb(0))
    half_reference = (reference[1] - reference[0]) / 2
    half_target = (target[1] - target[0]) / 2
    quotients = [(w ** 2 - (w ** 2 - 1)) / (2 * w) for w in reference]
    j = -half_reference * (quotients[1] - quotients[0])
    checks = {
        "strict_collar_ratio": eta < 1,
        "counted_target_gap_exactly_zero": half_target ** 2 == 0,
        "regular_contour_J_exactly_minus_one": j == -1,
        "D_Y_plus_J_minus_A_nonpositive": half_reference ** 2 + j - a <= 0,
        "target_MVT_slope_at_double_zero": 2 * target[0] == 0,
    }
    if not all(checks.values()):
        raise ChartFailure("exact double control failed")
    return {
        "control": "Y(w)=w^2-1, F(w)=w^2, w=z-36",
        "loss_of_real_root_premise": "F is nonnegative on the real axis with a double root, so opposite signs cannot bracket its pair.",
        "checks": checks,
    }


def attempt(level, original):
    order, bits, source_terms, head_terms, sectors = level
    ctx.prec = bits
    output = {
        "sites": 24, "time_order": order, "precision_bits": bits,
        "source_spatial_terms": source_terms, "head_spatial_terms": head_terms,
        "sectors_per_radius": sectors, "costs": {},
    }
    costs = output["costs"]
    start = tick = perf_counter()
    stage = "complete source acquisition"
    try:
        f_rows, f_tail, output["source"] = build_source(order, bits, source_terms)
        costs["source_seconds"] = perf_counter() - tick
        stage = "moving head acquisition"
        tick = perf_counter()
        y_rows, y_tail, output["head"] = build_head(order, bits, head_terms)
        costs["head_seconds"] = perf_counter() - tick
        stage = "common Taylor model"
        tick = perf_counter()
        f, y = Field(f_rows, f_tail), Field(y_rows, y_tail)
        difference = f.difference(y)
        fields = f, y, difference
        costs["subtracted_model_seconds"] = perf_counter() - tick
        output["full_value_and_first_derivative_tail_uppers"] = {
            name: ball(field.tail) for name, field in zip(("F", "Y", "B"), fields)
        }

        stage = "common whole collar"
        tick = perf_counter()
        full_time = arb(fmpq(1, 2), fmpq(1, 2))
        output["collar"] = {}
        eta = certify_collar(fields, sectors, full_time, output["collar"])
        costs["collar_seconds"] = perf_counter() - tick

        stage = "full-slab signed and direct enclosures"
        tick = perf_counter()
        output["full_slab"] = {}
        values, x, h = enclose_change(fields, full_time, eta, output["full_slab"])
        output["collar"]["counting_gates"] = {
            "F_inner_and_outer_count": 2, "Y_inner_and_outer_count": 2,
            "both_pairs_simple_real_strictly_inside_radius_8": True,
        }
        costs["full_slab_seconds"] = perf_counter() - tick
        gates = output["acceptance_gates"] = {
            "whole_collar_ratio_strictly_less_than_one": eta < 1,
            "strict_signed_upper_negative": values["signed_change"] < 0,
            "strict_direct_upper_negative": values["direct_change"] < 0,
            "paid_target_gap_strictly_positive": values["paid_target_gap"] > 0,
            "signed_and_direct_changes_overlap": values["signed_change"].overlaps(values["direct_change"]),
        }
        failed = [name for name, passed in gates.items() if not passed]
        if failed:
            raise ChartFailure(f"acceptance gates unresolved: {', '.join(failed)}")

        stage = "E07 anchor and time uncertainty"
        tick = perf_counter()
        output["anchor_time_zero"] = {}
        at_zero, zx, zy = enclose_change(fields, arb(0), eta, output["anchor_time_zero"])
        output["right_endpoint"] = {}
        at_end, _, _ = enclose_change(fields, arb(1), eta, output["right_endpoint"])
        gates.update(anchor_checks(at_zero, zx, zy, original))
        e07_direct = stored_ball(original["results"]["direct_gap_change"])
        time_change = {
            "direct_change_minus_E07_zero_time_value_all_t": values["direct_change"] - e07_direct,
            "direct_endpoint_change_of_gap_correction_from_E07": at_end["direct_change"] - e07_direct,
        }
        output["time_uncertainty"] = {name: ball(value) for name, value in time_change.items()}
        gates["exact_double_event_control"] = bool(collision_check())
        costs["endpoint_and_anchor_seconds"] = perf_counter() - tick
        failed = [name for name, passed in gates.items() if not passed]
        if failed:
            raise ChartFailure(f"acceptance gates unresolved: {', '.join(failed)}")
        output["field_evaluation_counts"] = {
            name: {"arc": item.arc_calls, "real_value": item.value_calls, "real_derivative": item.derivative_calls}
            for name, item in zip(("F", "Y", "B"), fields)
        }
    except (ArithmeticError, ValueError) as error:
        output.update(status="failed", failed_stage=stage, failure=str(error))
        costs["stage_seconds_on_failure"] = perf_counter() - tick
    else:
        output["status"] = "accepted"
    costs["attempt_wall_seconds"] = perf_counter() - start
    return output


def run():
    read_verified(REQUEST, REQUEST_SHA)
    anchor = json.loads(read_verified(ANCHOR, ANCHOR_SHA))
    original = anchor["attempts"][0]
    if anchor["status"] != "accepted" or original["N"] != 24 or anchor["physical_time"] != "0":
        raise ValueError("unexpected E07 anchor result")
    tz = ZoneInfo("America/New_York")
    start = datetime.now(tz)
    tick = perf_counter()
    ctx.threads = 1
    attempts = []
    for level in LEVELS:
        result = attempt(level, original)
        attempts.append(result)
        if result["status"] == "accepted":
            break
    inputs = (
        "certify_e08.py", "e08_chart.py", "e08_head.py", "e08_source.py",
        "certify_e07.py", "e07_chart.py", "e07_fields.py",
    )
    return {
        "task": "AGC-JH-E08 r1",
        "author": "Prepared for Edward Baker with OpenAI Codex LLM assistance",
        "dispatch": {"requested_model": "gpt-6.2-sol", "requested_effort": "ultra",
                     "independent_serving_metadata": None},
        "started": start.isoformat(), "finished": datetime.now(tz).isoformat(),
        "wall_seconds": perf_counter() - tick,
        "runtime": {"python": platform.python_version(), "flint": flint.__FLINT_VERSION__,
                    "python_flint": flint.__version__, "flint_threads": ctx.threads},
        "input_sha256": {REQUEST.name: REQUEST_SHA, ANCHOR.name: ANCHOR_SHA},
        "code_sha256": {name: sha256((HERE / name).read_bytes()).hexdigest() for name in inputs},
        "physical_time": ["0", "1/10000"],
        "contour": {"center": 36, "radius": 9, "collar_offset": "1/64", "inner_radius": 8},
        "tails": {"value_disk_radius": 10, "first_z_derivative_disk_radius": 9},
        "shared_information": "Full field Taylor models, remainders, counts, local tubes, and subtracted numerator.",
        "event_control": collision_check(),
        "scope": "Single known-coverage slab and degree. No weighted forcing is evaluated.",
        "attempts": attempts, "status": attempts[-1]["status"],
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
