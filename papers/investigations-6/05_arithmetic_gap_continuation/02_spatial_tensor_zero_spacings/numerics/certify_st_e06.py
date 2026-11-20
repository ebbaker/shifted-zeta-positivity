"""Replay AGC-ST-E06 r1 using python-flint. With no --output, write JSON to stdout.

20 November 2026. Prepared for Edward Baker with OpenAI Codex LLM assistance.
Dispatched as gpt-6.2-sol / ultra. Serving configuration not separately attested.
"""

import argparse
from datetime import datetime
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
import platform
import sys
from time import perf_counter
from zoneinfo import ZoneInfo

import flint
from flint import arb, ctx, fmpq


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
JH = HERE.parents[1] / "01_jacobi_integer_hierarchy/numerics"
HDC = ROOT / "papers/investigations-4/12_height_dependent_heat_contours/numerics"
REQUEST = HERE.parent / "research-progress/handoffs/AGC_ST_E06_REQUEST_R1_20261120.md"
JH_RECORD = JH / "06_AGC_JH_E08_SLAB_CERTIFICATE_20261119.json"
HDC_RECORD = HDC / "07_COMPLETE_THETA_WALL_CERTIFICATE_20261023.json"
FROZEN_INPUTS = {
    REQUEST: "809807cffb398a16fb335f79910780622506487e59ebd4ab6b7ad2ba51b348af",
    JH_RECORD: "2197c811918435dc3ee8787a4c9f03b4f03aab67efddecff650dba58cec5758d",
    HDC_RECORD: "966540b5221b7b5f6cd4d73672728bee1fc26045efdb69c38bde4e9a813239dc",
}
BOX = {
    "x": ["26", "46"], "y": ["-2", "2"],
    "Re_tau": ["-1/10000", "1/10000"], "Im_tau": ["-1/10000", "1/10000"],
}
T = fmpq(1, 10000)
TIME = ["0", str(T)]
CENTER = 36
RADIUS = 15
LOCAL_ORDER = 4
SOURCE_LEVEL = (10, 768, 144)
ZONE = ZoneInfo("America/New_York")


class GateFailure(ValueError):
    """The frozen enclosure did not prove a required predicate."""


def require(predicate, label):
    if not predicate:
        raise GateFailure(label)


def verified(path, expected, hashes):
    data = path.read_bytes()
    relative = str(path.relative_to(ROOT))
    digest = sha256(data).hexdigest()
    require(digest == expected, f"SHA-256 mismatch for {relative}: {digest}")
    hashes[relative] = digest
    return data


def inherited_inputs(hashes):
    raw = {path: verified(path, digest, hashes) for path, digest in FROZEN_INPUTS.items()}
    jh = json.loads(raw[JH_RECORD])
    hdc = json.loads(raw[HDC_RECORD])
    verified(HDC / "07_certify_complete_theta_wall_20261023.py", hdc["script_sha256"], hashes)
    verified(HDC / "hdc13_theta_core.py", hdc["core_sha256"], hashes)
    for name, digest in jh["code_sha256"].items():
        verified(JH / name, digest, hashes)
    for name, digest in jh["input_sha256"].items():
        directory = JH.parent / "research-progress/handoffs" if name.endswith(".md") else JH
        verified(directory / name, digest, hashes)
    require(hdc["status"] == "PASS" and hdc["anchor_tau"] == "0"
            and hdc["physical_box"] == BOX and hdc["complete_zero_count_uniform_D"] == 2,
            "HDC count identity, source anchor or physical geometry failed")
    require(jh["status"] == "accepted" and jh["physical_time"] == TIME
            and jh["contour"] == {"center": 36, "radius": 9, "collar_offset": "1/64", "inner_radius": 8},
            "JH slab or source geometry failed")
    attempt, = jh["attempts"]
    require((attempt["time_order"], attempt["precision_bits"], attempt["source_spatial_terms"])
            == SOURCE_LEVEL and attempt["status"] == "accepted",
            "inherited JH source level or full-slab status failed")
    collar = attempt["collar"]
    gates = collar["counting_gates"]
    require(collar["prior_HDC_count"]["sha256"] == FROZEN_INPUTS[HDC_RECORD]
            and gates["F_inner_and_outer_count"] == 2
            and gates["both_pairs_simple_real_strictly_inside_radius_8"],
            "JH physical count, simplicity or HDC cross-reference failed")
    brackets = attempt["full_slab"]["F_brackets"]
    require([item["initial"] for item in brackets] == [[28, 29], [42, 43]]
            and [item["initial_signs"] for item in brackets] == [[1, -1], [-1, 1]],
            "physical root brackets or their real sign orientations failed")
    return brackets, arb(hdc["wall"]["minimum_full_D_floor"])


def decimal_at_scale(integer, places):
    digits = f"{abs(integer):0{places + 1}d}"
    text = f"{digits[:-places]}.{digits[-places:]}".rstrip("0").rstrip(".")
    return f"-{text}" if integer < 0 else text


def interval(value, places=60):
    """Serialize a compact decimal enclosure by exact directed rounding."""
    require(value.is_finite(), "nonfinite interval in output")
    scale = 10**places
    lo = (value.lower().fmpq() * scale).floor()
    hi = (value.upper().fmpq() * scale).ceil()
    return {"lower": decimal_at_scale(int(lo), places), "upper": decimal_at_scale(int(hi), places)}


def horner(coefficients, x):
    result = arb(0)
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


class CompleteSource:
    """Re-use the normalized JH coefficients, with a new radius-15 tail."""

    def __init__(self, rows, metadata):
        cauchy_radius = metadata["cauchy_spatial_radius"]
        time_radius = fmpq(metadata["cauchy_time_radius"])
        majorant = arb(fmpq(metadata["normalized_polydisk_majorant"]["upper"]))
        gamma = arb(T / time_radius)
        ratio = arb(fmpq(RADIUS, cauchy_radius))
        time_order, _, terms = SOURCE_LEVEL
        self.time_tail = (majorant * gamma**(time_order + 1) / (1 - gamma)).upper()
        self.spatial_tail = (majorant * ratio**terms / ((1 - ratio) * (1 - gamma))).upper()
        self.tail = (self.time_tail + self.spatial_tail).upper()
        self.coefficient_radii = sum(
            coefficient.rad() * RADIUS**j for row in rows for j, coefficient in enumerate(row)
        ).upper()
        self.jets = [
            [[comb(j, order) * row[j] for j in range(order, len(row))] for row in rows]
            for order in range(LOCAL_ORDER + 5)
        ]
        require(cauchy_radius == 24 and time_radius == fmpq(1, 20) and majorant > 0,
                "unexpected source Cauchy domain or majorant")
        require(self.tail < arb("1e-26"), "radius-15 complete source tail too wide")

    def evaluate(self, x, s, order=0):
        w = x - CENTER
        padding = int(order != 0)  # unit Cauchy circle for the true-minus-polynomial jet
        require(w.abs_upper() + padding <= RADIUS, "spatial evaluation outside the paid disk")
        middle = w.mid()
        delta = w - middle
        last = order + LOCAL_ORDER
        polynomial_majorant = sum(
            horner([abs(coefficient) for coefficient in row], w.abs_upper())
            for row in self.jets[last]
        )
        polynomial_error = (
            factorial(last) // factorial(LOCAL_ORDER)
            * polynomial_majorant * delta.abs_upper()**LOCAL_ORDER
        ).abs_upper()
        local_terms = [
            factorial(order + k) // factorial(k)
            * horner([horner(row, middle) for row in self.jets[order + k]], s)
            for k in range(LOCAL_ORDER)
        ]
        return horner(local_terms, delta) + arb(0, (polynomial_error + factorial(order)*self.tail).upper())


def strict_sign(value):
    return int(value > 0) - int(value < 0)


def evaluate_slab(record):
    brackets, hdc_floor = inherited_inputs(record["input_sha256"])
    ctx.threads = 1
    ctx.prec = SOURCE_LEVEL[1]
    sys.path.insert(0, str(JH))
    from e08_source import build_source

    rows, _, metadata = build_source(*SOURCE_LEVEL)
    source = CompleteSource(rows, metadata)
    s = arb(0).union(arb(1))
    record["inherited_chart"] = {
        "physical_box": BOX, "complete_count": 2, "strip_half_width": 1,
        "wall_floor_receipt": interval(hdc_floor),
    }
    record["source"] = {
        "normalization": "H(t,z)/H(t,0) with H(t,0)>0",
        "time_degree": SOURCE_LEVEL[0], "precision_bits": SOURCE_LEVEL[1],
        "spatial_terms": SOURCE_LEVEL[2], "center": CENTER,
        "complex_value_radius": RADIUS, "unit_derivative_Cauchy_circle": 1,
        "majorant_radius": 24, "majorant_complex_time_radius": "1/20",
        "time_tail_upper": interval(source.time_tail),
        "spatial_tail_upper": interval(source.spatial_tail),
        "complete_tail_upper": interval(source.tail),
        "coefficient_radius_sum_at_15_upper": interval(source.coefficient_radii, places=205),
        "derivative_tail_uppers": [interval((factorial(j)*source.tail).upper()) for j in range(1, 5)],
    }
    require(hdc_floor > 0, "HDC record has no positive wall floor")

    sign_points = [fmpq(499, 10), fmpq(501, 10)]
    sign_values = [source.evaluate(arb(point), s) for point in sign_points]
    signs = list(map(strict_sign, sign_values))
    record["exterior_sign_bracket"] = [
        {"abscissa": str(point), "source_value": interval(value), "sign": sign}
        for point, value, sign in zip(sign_points, sign_values, signs)
    ]
    require(signs[0] and signs[1] == -signs[0], "unresolved full-slab exterior sign bracket")

    target_roots = [
        arb(fmpq(item["root"]["lower"])).union(arb(fmpq(item["root"]["upper"])))
        for item in brackets
    ]
    a, b = target_roots
    require(a > 28 and a < 29 and b > 42 and b < 43,
            "inherited target roots outside their physical brackets")
    gap = b - a
    ratio_upper = ((arb(sign_points[-1]) - b) / gap).upper()
    record["spatial"] = {"gap": interval(gap), "selected_normalized_distance_upper": interval(ratio_upper)}
    require(gap > 13 and gap < 15 and ratio_upper < arb(fmpq(3, 5)),
            "gap or selected normalized distance not certified")
    sector_margin = fmpq(16, 125) - fmpq(1, 8)
    threshold = ((fmpq(3, 5)**-3) - (fmpq(8, 5)**-3)) / 2
    require(sector_margin > 0 and threshold == fmpq(60625, 27648) and threshold > fmpq(219, 100),
            "exact complement or K lower constant failed")
    acceleration_floor = 16 * (threshold - 1) / 15**3
    require(acceleration_floor > fmpq(1, 180), "acceleration conversion failed")
    record["spatial"].update({
        "short_sector_margin": str(sector_margin), "K_lower": str(threshold),
        "gap_acceleration_lower": str(acceleration_floor),
        "strict_simple_acceleration_lower": "1/180",
        "strict_midpoint_excess_lower": str(T**2 / 1440),
    })

    record["direct_roots"] = []
    accelerations = []
    for name, root in zip(("left", "right"), target_roots):
        hz, hzz, hzzz, hzzzz = [source.evaluate(root, s, order) for order in range(1, 5)]
        item = {
            "target": name, "tube": interval(root),
            "normalized_spatial_jets_1_through_4": list(map(interval, (hz, hzz, hzzz, hzzzz))),
        }
        record["direct_roots"].append(item)
        require(strict_sign(hz), f"{name} source spatial derivative includes zero")
        velocity = hzz / hz
        acceleration = -hzzzz / hz + 2 * velocity * hzzz / hz - velocity**2 * hzz / hz
        accelerations.append(acceleration)
        item.update(velocity=interval(velocity), acceleration=interval(acceleration))
    acceleration_difference = accelerations[1] - accelerations[0]
    direct = 1 + gap**3 * acceleration_difference / 16
    direct_interval = interval(direct)
    recorded_width = arb(direct_interval["upper"]) - arb(direct_interval["lower"])
    record["direct"] = {
        "gap_acceleration": interval(acceleration_difference),
        "K": direct_interval,
        "K_width_upper": interval(recorded_width.upper()),
        "entire_K_interval_above_2.19": bool(direct > arb(fmpq(219, 100))),
        "entire_K_interval_above_selected_kernel_floor": bool(direct > arb(threshold)),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="file for the compact JSON record")
    args = parser.parse_args()
    start = perf_counter()
    record = {
        "task": "AGC-ST-E06 r1",
        "author": "Prepared for Edward Baker with OpenAI Codex LLM assistance",
        "dispatch": {"model": "gpt-6.2-sol", "reasoning_effort": "ultra", "separate_backend_attestation": False},
        "started": datetime.now(ZONE).isoformat(),
        "runtime": {
            "python": platform.python_version(), "python_flint": flint.__version__,
            "flint": flint.__FLINT_VERSION__, "threads": 1,
        },
        "driver_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "input_sha256": {},
        "physical_time": TIME,
        "repair_used": False,
    }
    try:
        evaluate_slab(record)
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
