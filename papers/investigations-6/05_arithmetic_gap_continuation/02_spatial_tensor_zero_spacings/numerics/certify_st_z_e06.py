"""Replay the AGC-ST-Z-E06 r1 fixed exterior probe certificate.

20 November 2026. Prepared for Edward Baker with OpenAI Codex LLM assistance.
Dispatched as gpt-6.2-sol / ultra. Serving configuration not separately attested.
"""

import argparse
from datetime import datetime
from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import platform
import sys
from time import perf_counter

import flint
from flint import arb, ctx, fmpq

from certify_st_e06 import (
    BOX, HDC, JH, ROOT, SOURCE_LEVEL, T, TIME, ZONE, CompleteSource,
    GateFailure, interval, require, strict_sign, verified,
)


HERE = Path(__file__).resolve().parent
REQUEST = HERE.parent / "research-progress/handoffs/AGC_ST_Z_E06_REQUEST_R1_20261120.md"
ANCHOR = JH / "05_AGC_JH_E07_CERTIFICATE_20261119.json"
WALL = HDC / "07_COMPLETE_THETA_WALL_CERTIFICATE_20261023.json"
INPUTS = {
    REQUEST: "22c29f0c044eb56f9c50f05bf145bc46f54ce00e5c4a9fbd2e9c590b41b51a9c",
    ANCHOR: "ff76aeb4ae3c08ce62d9e4d5c92ef06e11ee91b99c1da5c532a8d215b86b8956",
    WALL: "966540b5221b7b5f6cd4d73672728bee1fc26045efdb69c38bde4e9a813239dc",
    HERE / "certify_st_e06.py": "df6c07fa5b0942eb534a0358d242e499ded37626e25ca61475b064fbeddc1be4",
    JH / "e08_source.py": "776b13f8cf71de6e9eecfe2d07cb8b9653374aaac40ff925f210a36ecb4305ef",
}
PROBE = fmpq(87, 2)
TARGET_BRACKETS = ((28, 29), (42, 43))
EXTERIOR_BRACKET = (fmpq(499, 10), fmpq(501, 10))


def hull(lower, upper):
    return arb(lower).union(arb(upper))


def cube_inverse(x):
    require(not x.contains(0), "zero in a cubic denominator")
    return hull(1 / x.upper()**3, 1 / x.lower()**3)


def width_upper(value):
    endpoints = interval(value)
    width = Fraction(endpoints["upper"]) - Fraction(endpoints["lower"])
    return fmpq(width.numerator, width.denominator)


def acquire_anchor_and_wall(hashes):
    files = {path: verified(path, digest, hashes) for path, digest in INPUTS.items()}
    anchor = json.loads(files[ANCHOR])
    wall = json.loads(files[WALL])
    verified(HDC / "07_certify_complete_theta_wall_20261023.py", wall["script_sha256"], hashes)
    verified(HDC / "hdc13_theta_core.py", wall["core_sha256"], hashes)
    for name, digest in anchor["replay_sha256"].items():
        verified(JH / name, digest, hashes)
    anchor_request = JH.parent / "research-progress/handoffs/AGC_JH_E07_REQUEST_R1_20261119.md"
    verified(anchor_request, anchor["request_sha256"], hashes)
    require(wall["status"] == "PASS" and wall["physical_box"] == BOX
            and wall["anchor_tau"] == "0" and wall["complete_zero_count_uniform_D"] == 2,
            "HDC complete wall and count on the frozen geometry")
    wall_floor = arb(wall["wall"]["minimum_full_D_floor"]).lower()
    require(wall_floor > 0, "HDC wall lacks a positive modulus floor")
    require(anchor["status"] == "accepted" and anchor["physical_time"] == "0",
            "time-zero JH anchor failed")
    attempt, = anchor["attempts"]
    require(attempt["status"] == "accepted" and attempt["counts_and_buffer"]["F_inner"] == 2,
            "JH time-zero source count failed")
    anchors = []
    for item, (lo, hi) in zip(attempt["F_real_brackets"], TARGET_BRACKETS, strict=True):
        require(item["initial_endpoints"] == [lo, hi], "unexpected anchor bracket")
        root = hull(fmpq(item["root"]["lower"]), fmpq(item["root"]["upper"]))
        require(root > lo and root < hi, "anchor enclosure escaped its integer bracket")
        anchors.append(root)
    return anchors, wall_floor


def signs_at(source, elapsed, points, expected):
    values = [source.evaluate(arb(point), elapsed) for point in points]
    signs = list(map(strict_sign, values))
    require(signs == expected, f"unresolved full-slab signs at {points}")
    return [
        {"height": str(point), "value": interval(value), "sign": sign}
        for point, value, sign in zip(points, values, signs)
    ]


def selected_lower(x):
    # K_d increases with x and decreases with d on this real domain.
    edge = x.lower()
    far = arb(EXTERIOR_BRACKET[1])
    return (cube_inverse(far - edge) - cube_inverse(far + edge)).lower()


def acceleration_bounds(boxes, observed_trace):
    a, b = boxes
    require(a > 0 and a < b and b < arb(PROBE), "ordered boxes below the probe")
    deflation = sum(cube_inverse(arb(PROBE) - r) for r in (a, -a, b, -b))
    upper = (observed_trace + deflation).upper()
    lower = [selected_lower(x) for x in boxes]
    require(all(value > 0 and value <= upper for value in lower),
            "exterior lower kernels and fixed-probe upper bound are inconsistent")
    exterior = [hull(value, upper) for value in lower]
    gap = b - a
    mirror_shared = cube_inverse(a + b)
    mutual = cube_inverse(gap)
    reflected = [cube_inverse(2*x) for x in boxes]
    internal = [
        reflected[0] + mirror_shared - mutual,
        reflected[1] + mirror_shared + mutual,
    ]
    accelerations = [8 * (higher - finite) for higher, finite in zip(exterior, internal)]
    center = 4 * (exterior[0] + exterior[1] - reflected[0] - reflected[1] - 2*mirror_shared)
    return accelerations, center, {
        "trajectory_boxes": list(map(interval, boxes)),
        "probe_deflation_correction": interval(deflation),
        "exterior_at_probe_upper": interval(upper),
        "selected_occurrence_lower": list(map(interval, lower)),
        "exterior_at_targets": list(map(interval, exterior)),
        "signed_internal_and_mirror_sums": list(map(interval, internal)),
        "accelerations": list(map(interval, accelerations)),
        "center_acceleration_mutual_cubes_canceled": interval(center),
    }


def evaluate(record):
    ctx.threads = 1
    ctx.prec = SOURCE_LEVEL[1]
    anchors, wall_floor = acquire_anchor_and_wall(record["input_sha256"])
    lower_count = arb(13).zeta_nzeros()
    require(lower_count.is_exact() and lower_count == 0, "complete FLINT N(13) was not exactly zero")
    record["count"] = {
        "zeta_N_13": str(lower_count), "works_with_multiplicity": True,
        "canonical_strip_half_width": 1, "physical_wall": BOX,
        "wall_floor": interval(wall_floor), "marked_count": 2,
        "lower_rectangle": {"x": [0, 26], "y": [-2, 2], "count": 0},
        "positive_exterior_real_part_strict_lower": 46,
    }

    sys.path.insert(0, str(JH))
    from e08_source import build_source

    rows, _, metadata = build_source(*SOURCE_LEVEL)
    source = CompleteSource(rows, metadata)
    full_time = hull(0, 1)  # scaled physical time, t/T
    record["source"] = {
        "level": list(SOURCE_LEVEL), "normalization": "H(t,z)/H(t,0)",
        "paid_spatial_radius": 15, "center": 36, "derivative_cauchy_radius": 1,
        "time_tail_upper": interval(source.time_tail),
        "spatial_tail_upper": interval(source.spatial_tail),
        "analytic_jet_tail_uppers_0_through_3": [
            interval((factorial(j)*source.tail).upper()) for j in range(4)
        ],
        "coefficient_radii_sum_at_radius_15": interval(source.coefficient_radii, places=205),
    }
    record["integer_wall_signs"] = signs_at(source, full_time, (28, 29, 42, 43), [1, -1, -1, 1])
    record["exterior_signs"] = signs_at(source, full_time, EXTERIOR_BRACKET, [1, -1])
    velocities = []
    record["anchors"] = []
    for x0 in anchors:
        hz, hzz = [source.evaluate(x0, arb(0), order) for order in (1, 2)]
        require(strict_sign(hz), "an anchor's derivative contains zero")
        velocity = hzz / hz
        velocities.append(velocity)
        record["anchors"].append({
            "root_at_zero": interval(x0), "normalized_H1": interval(hz),
            "normalized_H2": interval(hzz), "velocity_at_zero": interval(velocity),
        })

    f, f1, f2, f3 = [source.evaluate(arb(PROBE), full_time, j) for j in range(4)]
    require(strict_sign(f), "fixed probe field contains zero")
    ratio1 = f1 / f
    observed_trace = -(f3 / f - 3*ratio1*(f2 / f) + 2*ratio1**3) / 2
    record["fixed_probe"] = {
        "height": str(PROBE), "jets_0_through_3": list(map(interval, (f, f1, f2, f3))),
        "normalized_modulus_floor": interval(f.abs_lower()),
        "negative_half_log_third_derivative": interval(observed_trace),
        "trace_width": str(width_upper(observed_trace)),
        "post_anchor_target_jets": 0,
    }

    coarse = [hull(lo, hi) for lo, hi in TARGET_BRACKETS]
    coarse_acc, _, record["coarse"] = acceleration_bounds(coarse, observed_trace)
    elapsed = hull(0, T)
    elapsed_weight = hull(0, T**2 / 2)
    boxes = [
        x0 + elapsed*v0 + elapsed_weight*acc
        for x0, v0, acc in zip(anchors, velocities, coarse_acc)
    ]
    require(all(box > lo and box < hi for box, (lo, hi) in zip(boxes, TARGET_BRACKETS)),
            "coarse-acceleration trajectory containment in the disjoint integer boxes")
    acc, center_acc, record["refined"] = acceleration_bounds(boxes, observed_trace)

    correction = [T**2 / 2 * value for value in acc]
    displacement = [T*v0 + rem for v0, rem in zip(velocities, correction)]
    endpoint = [x0 + dx for x0, dx in zip(anchors, displacement)]
    end_width = list(map(width_upper, endpoint))
    center_displacement = T*(velocities[0] + velocities[1])/2 + T**2*center_acc/2
    center_displacement = center_displacement.intersection((displacement[0] + displacement[1])/2)
    half_gap = (endpoint[1] - endpoint[0])/2
    require(half_gap > 0, "predicted signed discriminant lost separation")
    record["prediction"] = {
        "joint_generators": "p_i=x_i(0)+T v_i(0)+T^2 weighted_acceleration_i/2; "
                            "c=(p_a+p_b)/2, D=((p_b-p_a)/2)^2",
        "tangent_corrections": list(map(interval, correction)),
        "signed_displacements": list(map(interval, displacement)),
        "endpoints": list(map(interval, endpoint)),
        "endpoint_width_uppers": [interval(arb(width).upper()) for width in end_width],
        "center_displacement": interval(center_displacement),
        "positive_half_gap": interval(half_gap),
        "signed_D": interval(half_gap**2),
    }
    require(acc[0] > arb("0.001"), "a'' > 1e-3")
    require(acc[1] > arb("0.01"), "b'' > 1e-2")
    require(all(rem > 0 for rem in correction), "both corrections above the initial tangents")
    require(all(dx < 0 for dx in displacement), "both physical displacements negative")
    require(all(width < fmpq(1, 10**7) for width in end_width), "both endpoint widths < 1e-7")
    record["frozen_gates"] = "all passed"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="optional destination for the JSON record")
    args = parser.parse_args()
    start = perf_counter()
    record = {
        "task": "AGC-ST-Z-E06 r1",
        "author": "Prepared for Edward Baker with OpenAI Codex LLM assistance",
        "dispatch": {"model": "gpt-6.2-sol", "effort": "ultra", "separate_backend_attestation": False},
        "started": datetime.now(ZONE).isoformat(),
        "driver_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "input_sha256": {},
        "runtime": {
            "python": platform.python_version(), "python_flint": flint.__version__,
            "flint": flint.__FLINT_VERSION__, "threads": 1,
        },
        "physical_time": TIME,
    }
    try:
        evaluate(record)
    except GateFailure as exc:
        record.update(status="failed gate", failure=str(exc))
    else:
        record["status"] = "certified"
    record["finished"] = datetime.now(ZONE).isoformat()
    record["wall_seconds"] = perf_counter() - start
    payload = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload)
    else:
        print(payload, end="")
    return 0 if record["status"] == "certified" else 1


if __name__ == "__main__":
    sys.exit(main())
