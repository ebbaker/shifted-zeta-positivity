"""Replay AGC-ST-Z-E04 r1 with separate predictor and terminal comparison phases.

20 November 2026. Prepared for Edward Baker with OpenAI Codex LLM assistance.
Dispatched as gpt-6.2-sol / ultra. Serving configuration not separately attested.
"""

import argparse
from dataclasses import dataclass
from datetime import datetime
from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import platform
import sys
from zoneinfo import ZoneInfo

import flint
from flint import arb, ctx, fmpq


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
JH = HERE.parents[1] / "01_jacobi_integer_hierarchy/numerics"
HDC = ROOT / "papers/investigations-4/12_height_dependent_heat_contours/numerics"
ANCHORS = JH / "05_AGC_JH_E07_CERTIFICATE_20261119.json"
WALL = HDC / "07_COMPLETE_THETA_WALL_CERTIFICATE_20261023.json"
REQUEST = HERE.parent / "research-progress/handoffs/AGC_ST_Z_E04_REQUEST_R1_20261120.md"
B03 = HERE.parent / "brainstorm/notes/07_AGC_ST_Z_B03_CANONICAL_POSITION_TEST_20261120.md"
FROZEN_INPUTS = {
    REQUEST: "da88ae98bf342d14f24d94c6c5eed0b4eef7f20d8d419aa38b5dae7c17c361a9",
    B03: "f1d431ff1ab2c483f9dae2ee5559f3f2762376f6ea1ecdf957882f0456362823",
    HERE / "certify_st_e06.py": "df6c07fa5b0942eb534a0358d242e499ded37626e25ca61475b064fbeddc1be4",
    ANCHORS: "ff76aeb4ae3c08ce62d9e4d5c92ef06e11ee91b99c1da5c532a8d215b86b8956",
    JH / "e08_source.py": "776b13f8cf71de6e9eecfe2d07cb8b9653374aaac40ff925f210a36ecb4305ef",
    JH / "e07_fields.py": "081ce436a582a87e4f3dd1ab88db259e5469b9c48a389d2b4d2af3c02e5da081",
    WALL: "966540b5221b7b5f6cd4d73672728bee1fc26045efdb69c38bde4e9a813239dc",
}
TASK = "AGC-ST-Z-E04 r1"
SOURCE_LEVEL = (10, 768, 144)
T = Fraction(1, 10000)
TAYLOR_WEIGHT = T**2 / 2
PREDICT_LIMIT = Fraction("1e-10")
DIRECT_LIMIT = Fraction("1e-16")
MIDPOINT_CAP = 62
COARSE = ((28, 29), (42, 43))
SIGNS = ((1, -1), (-1, 1))
BOX = {
    "x": ["26", "46"], "y": ["-2", "2"],
    "Re_tau": ["-1/10000", "1/10000"], "Im_tau": ["-1/10000", "1/10000"],
}


class GateFailure(ValueError):
    """A frozen premise or comparison could not be verified."""


def require(predicate, message):
    if not predicate:
        raise GateFailure(message)


def q(value):
    return fmpq(value.numerator, value.denominator)


def decimal(integer, places):
    digits = f"{abs(integer):0{places + 1}d}"
    sign = "-" if integer < 0 else ""
    return f"{sign}{digits[:-places]}.{digits[-places:]}".rstrip("0").rstrip(".")


@dataclass(frozen=True)
class Bounds:
    """Exact endpoints enclosing a real interval."""

    lower: Fraction
    upper: Fraction

    @classmethod
    def from_ball(cls, value):
        require(value.is_finite(), "Nonfinite Arb result.")
        return cls(Fraction(str(value.lower().fmpq())), Fraction(str(value.upper().fmpq())))

    @classmethod
    def from_record(cls, entry):
        return cls(Fraction(entry["lower"]), Fraction(entry["upper"]))

    def ball(self):
        return arb(q(self.lower)).union(arb(q(self.upper)))

    def __add__(self, other):
        return Bounds(self.lower + other.lower, self.upper + other.upper)

    def __sub__(self, other):
        return Bounds(self.lower - other.upper, self.upper - other.lower)

    def scale(self, scalar):
        return Bounds(scalar * self.lower, scalar * self.upper)

    def record(self, places=60):
        scale = 10**places
        lower = self.lower * scale
        upper = self.upper * scale
        low = lower.numerator // lower.denominator
        high = -(-upper.numerator // upper.denominator)
        return {
            "lower": decimal(low, places),
            "upper": decimal(high, places),
            "width_outward": decimal(high - low, places),
        }


def sign(value):
    return int(value > 0) - int(value < 0)


def bounds_sign(value):
    return int(value.lower > 0) - int(value.upper < 0)


def hash_read(path, digest, hashes):
    raw = path.read_bytes()
    actual = sha256(raw).hexdigest()
    relative = str(path.relative_to(ROOT))
    require(actual == digest, f"SHA-256 mismatch for {relative}.")
    hashes[relative] = actual
    return raw


def load_inputs():
    hashes = {}
    data = {path: hash_read(path, digest, hashes) for path, digest in FROZEN_INPUTS.items()}
    anchor = json.loads(data[ANCHORS])
    wall = json.loads(data[WALL])
    hash_read(HDC / "07_certify_complete_theta_wall_20261023.py", wall["script_sha256"], hashes)
    hash_read(HDC / "hdc13_theta_core.py", wall["core_sha256"], hashes)
    for name, digest in anchor["replay_sha256"].items():
        hash_read(JH / name, digest, hashes)
    require(wall["status"] == "PASS" and wall["anchor_tau"] == "0"
            and wall["physical_box"] == BOX and wall["complete_zero_count_uniform_D"] == 2,
            "The HDC wall and count do not match the specified physical chart.")
    floor = arb(wall["wall"]["minimum_full_D_floor"])
    require(floor > 0, "HDC wall floor is not positive.")
    require(anchor["status"] == "accepted" and anchor["physical_time"] == "0",
            "The accepted E07 physical time-zero anchor is unavailable.")
    accepted, = [entry for entry in anchor["attempts"] if entry["status"] == "accepted"]
    brackets = accepted["F_real_brackets"]
    require(tuple(tuple(entry["initial_endpoints"]) for entry in brackets) == COARSE,
            "Time-zero intervals do not identify the declared coarse boxes.")
    anchors = [Bounds.from_record(entry["root"]) for entry in brackets]
    require(all(lo < bracket.lower < bracket.upper < hi
                for bracket, (lo, hi) in zip(anchors, COARSE)),
            "A time-zero anchor is outside its coarse box.")
    return hashes, anchors, Bounds.from_ball(floor).record()


def build_complete_source():
    from certify_st_e06 import CompleteSource

    sys.path.insert(0, str(JH))
    from e08_source import build_source

    rows, _, metadata = build_source(*SOURCE_LEVEL)
    source = CompleteSource(rows, metadata)
    coefficient_digest = sha256()
    for row in rows:
        for coefficient in row:
            enclosure = Bounds.from_ball(coefficient)
            coefficient_digest.update(f"{enclosure.lower} {enclosure.upper}\n".encode())
    source_record = {
        "normalization": "F(t,z)=H(t,z)/H(t,0), with H(t,0)>0 on the slab",
        "time_polynomial_coordinate": "t/T",
        "time_order": SOURCE_LEVEL[0],
        "precision_bits": SOURCE_LEVEL[1],
        "spatial_terms": SOURCE_LEVEL[2],
        "spatial_center": 36,
        "complex_value_radius": 15,
        "unit_derivative_cauchy_circle": 1,
        "majorant_radius": metadata["cauchy_spatial_radius"],
        "majorant_complex_time_radius": metadata["cauchy_time_radius"],
        "coefficient_interval_sha256": coefficient_digest.hexdigest(),
        "time_tail_upper": Bounds.from_ball(source.time_tail).record(),
        "spatial_tail_upper": Bounds.from_ball(source.spatial_tail).record(),
        "complete_tail_upper": Bounds.from_ball(source.tail).record(),
        "coefficient_radius_sum_at_15_upper": Bounds.from_ball(source.coefficient_radii).record(205),
        "analytic_tail_uppers_for_derivatives_1_through_4": [
            Bounds.from_ball((factorial(j) * source.tail).upper()).record() for j in range(1, 5)
        ],
    }
    return source, source_record


def predict_paths(source, anchors, speed_bound, calls):
    boxes = [anchor + Bounds(-speed_bound * T, speed_bound * T) for anchor in anchors]
    require(boxes[0].upper < boxes[1].lower
            and all(lo < box.lower < box.upper < hi for box, (lo, hi) in zip(boxes, COARSE)),
            "First-exit boxes must stay within distinct coarse intervals.")
    slab = arb(0).union(arb(1))
    paths = []
    for name, anchor, box in zip(("lower", "upper"), anchors, boxes):
        jets = [source.evaluate(box.ball(), slab, order) for order in range(1, 5)]
        calls["slab_derivative_calls"] += len(jets)
        f1, f2, f3, f4 = jets
        require(sign(f1), f"{name} path slope includes zero with padding {speed_bound}T.")
        speed = f2 / f1
        require(abs(speed) < speed_bound, f"{name} path speed is not strictly below {speed_bound}.")
        acceleration = -f4 / f1 + 2 * speed * f3 / f1 - speed**3
        anchor_f1, anchor_f2 = [source.evaluate(anchor.ball(), arb(0), order) for order in (1, 2)]
        calls["anchor_derivative_calls"] += 2
        require(sign(anchor_f1), f"{name} time-zero slope includes zero.")
        velocity = Bounds.from_ball(anchor_f2 / anchor_f1)
        mean_acceleration = Bounds.from_ball(acceleration)
        tangent_defect = mean_acceleration.scale(TAYLOR_WEIGHT)
        displacement = velocity.scale(T) + tangent_defect
        endpoint = anchor + displacement
        item = {
            "target": name,
            "anchor": anchor.record(),
            "candidate_path": box.record(),
            "slab_jet_inputs_1_through_4": [Bounds.from_ball(jet).record() for jet in jets],
            "slope_abs_floor": Bounds.from_ball(f1.abs_lower()).record(),
            "path_velocity": Bounds.from_ball(speed).record(),
            "path_speed_abs_upper": Bounds.from_ball(speed.abs_upper()).record(),
            "anchor_jet_inputs_1_and_2": [Bounds.from_ball(value).record() for value in (anchor_f1, anchor_f2)],
            "anchor_velocity": velocity.record(),
            "weighted_mean_acceleration": mean_acceleration.record(),
            "tangent_defect": tangent_defect.record(),
            "tangent_defect_sign": bounds_sign(tangent_defect),
            "displacement": displacement.record(),
            "displacement_sign": bounds_sign(displacement),
            "absolute_endpoint": endpoint.record(),
        }
        paths.append((item, displacement, endpoint, tangent_defect))
    return paths


def predict(source, receipt, anchors):
    calls = {"slab_derivative_calls": 0, "anchor_derivative_calls": 0, "terminal_value_calls": 0}
    receipt["source_calls"] = calls
    try:
        speed_bound = 2
        paths = predict_paths(source, anchors, speed_bound, calls)
    except GateFailure as failure:
        receipt["original_first_exit_failure"] = str(failure)
        speed_bound = 4
        paths = predict_paths(source, anchors, speed_bound, calls)
    receipt["first_exit_speed_ceiling_and_padding_multiple"] = speed_bound
    receipt["endpoint_paths"] = [item for item, *_ in paths]
    (_, da, a, ra), (_, db, b, rb) = paths
    half = Fraction(1, 2)
    center = (a + b).scale(half)
    half_gap = (b - a).scale(half)
    require(half_gap.lower > 0, "The positive half-gap projection was not proved.")
    center_delta = (da + db).scale(half)
    center_defect = (ra + rb).scale(half)
    receipt["shared_outputs"] = {
        "center": center.record(),
        "positive_half_gap": half_gap.record(),
        "signed_discriminant": Bounds(half_gap.lower**2, half_gap.upper**2).record(),
        "center_displacement": center_delta.record(),
        "center_displacement_sign": bounds_sign(center_delta),
        "center_tangent_defect": center_defect.record(),
        "center_tangent_defect_sign": bounds_sign(center_defect),
    }
    receipt["independently_boxed_center_and_discriminant"] = {
        "lower_endpoint": (center - half_gap).record(),
        "upper_endpoint": (center + half_gap).record(),
        "square_root_step": "Exact inverse on the positive interval used to form D.",
    }
    receipt["prediction_gates"] = {
        "center_and_both_individual_displacements_negative": all(
            bounds_sign(value) == -1 for value in (center_delta, da, db)
        ),
        "both_endpoints_and_center_displacement_width_below_1e-10": all(
            Fraction(value.record()["width_outward"]) < PREDICT_LIMIT for value in (a, b, center_delta)
        ),
    }


def bisect(source, coarse, signs):
    lo, hi = map(Fraction, coarse)
    end_time = arb(1)
    values = [source.evaluate(arb(q(point)), end_time) for point in (lo, hi)]
    require(tuple(map(sign, values)) == signs, f"Coarse end-time signs unresolved at {coarse}.")
    midpoints = 0
    ambiguous = None
    while hi - lo > DIRECT_LIMIT and midpoints < MIDPOINT_CAP:
        midpoint = (lo + hi) / 2
        result = sign(source.evaluate(arb(q(midpoint)), end_time))
        midpoints += 1
        if not result:
            ambiguous = str(midpoint)
            break
        if result == signs[0]:
            lo = midpoint
        else:
            hi = midpoint
    bracket = Bounds(lo, hi).record()
    return {
        "initial_endpoints": coarse,
        "initial_values": [Bounds.from_ball(value).record() for value in values],
        "initial_signs": signs,
        "bracket": bracket,
        "midpoint_tests": midpoints,
        "source_value_calls": 2 + midpoints,
        "ambiguous_midpoint": ambiguous,
        "target_width_at_most_1e-16": Fraction(bracket["width_outward"]) <= DIRECT_LIMIT,
    }


def compare(source, prediction):
    direct = [bisect(source, box, signs) for box, signs in zip(COARSE, SIGNS)]
    for saved, measured in zip(prediction["endpoint_paths"], direct):
        projected = Bounds.from_record(saved["absolute_endpoint"])
        bracket = Bounds.from_record(measured["bracket"])
        measured["overlaps_prediction"] = (
            max(projected.lower, bracket.lower) <= min(projected.upper, bracket.upper)
        )
        measured["contained_in_prediction"] = (
            projected.lower <= bracket.lower <= bracket.upper <= projected.upper
        )
        measured["narrower_than_prediction"] = (
            Fraction(measured["bracket"]["width_outward"])
            < Fraction(saved["absolute_endpoint"]["width_outward"])
        )
    return direct


def write_record(path, value):
    raw = (json.dumps(value, sort_keys=True, indent=2) + "\n").encode()
    with path.open("xb") as output:
        output.write(raw)
    return sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    phases = parser.add_subparsers(dest="phase", required=True)
    predictor = phases.add_parser("predict", help="Write the prediction and print its SHA-256.")
    predictor.add_argument("--output", type=Path, required=True)
    comparator = phases.add_parser("compare", help="Read the sealed prediction before evaluating final roots.")
    comparator.add_argument("--prediction", type=Path, required=True)
    comparator.add_argument("--prediction-sha256", required=True)
    comparator.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.threads = 1
    ctx.prec = SOURCE_LEVEL[1]
    record = {
        "task": TASK,
        "phase": args.phase,
        "author": "Prepared for Edward Baker with OpenAI Codex LLM assistance",
        "dispatch": {"model": "gpt-6.2-sol", "effort": "ultra", "separate_backend_attestation": False},
        "driver_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "runtime": {"python": platform.python_version(), "python_flint": flint.__version__,
                    "flint": flint.__FLINT_VERSION__, "flint_threads": ctx.threads},
    }
    try:
        if args.phase == "compare":
            raw = args.prediction.read_bytes()
            require(sha256(raw).hexdigest() == args.prediction_sha256,
                    "The saved pre-terminal prediction SHA-256 does not match.")
            prediction = json.loads(raw)
            require(prediction.get("task") == TASK and prediction.get("phase") == "predict"
                    and prediction.get("status") in {"pass", "threshold_failure"}
                    and prediction.get("driver_sha256") == record["driver_sha256"]
                    and prediction["source_calls"]["terminal_value_calls"] == 0,
                    "The saved prediction is not a completed separate predictor phase.")
            record["sealed_prediction_sha256"] = args.prediction_sha256
            record["sealed_prediction"] = prediction
        hashes, anchors, wall_floor = load_inputs()
        record["input_sha256"] = hashes
        if args.phase == "compare":
            require(prediction["input_sha256"] == hashes, "The input files changed after prediction.")
        source, metadata = build_complete_source()
        if args.phase == "predict":
            record["chart"] = {"physical_box": BOX, "complete_count": 2, "wall_floor_receipt": wall_floor}
            record["source"] = metadata
            record["time"] = {"slab": ["0", str(T)], "initial_velocity_weight": str(T),
                              "weighted_mean_acceleration_weight": str(TAYLOR_WEIGHT)}
            predict(source, record, anchors)
            passed = all(record["prediction_gates"].values())
        else:
            require(prediction["source"] == metadata, "The complete source changed after prediction.")
            direct = compare(source, prediction)
            record["direct"] = direct
            record["direct_total_source_value_calls"] = sum(item["source_value_calls"] for item in direct)
            record["source_builds"] = {"predict": 1, "compare": 1}
            record["run_recorded_at"] = datetime.now(ZoneInfo("America/New_York")).isoformat()
            passed = all(prediction["prediction_gates"].values()) and all(
                item["target_width_at_most_1e-16"] and item["overlaps_prediction"] for item in direct
            )
        record["status"] = "pass" if passed else "threshold_failure"
    except (GateFailure, ArithmeticError) as error:
        record["status"] = "premise_failure"
        record["failed_gate"] = str(error)
    print(write_record(args.output, record))
    return 0 if record["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
