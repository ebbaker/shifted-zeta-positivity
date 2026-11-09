#!/usr/bin/env python3
"""E13 r1 fixed contour-centroid projection and externally timed replay.

9 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
Recorded thread settings GPT-6.1 Sol / ultra, OC chat0010. Per-turn backend
configuration is unavailable. See Request27 for mathematical scope.
"""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import mmap
from pathlib import Path
import platform
import struct
import subprocess
import sys
import time

import flint
from flint import arb, ctx, fmpq

from e13_contours import GateError, acquire, zeta_source


HERE = Path(__file__).resolve().parent
INVESTIGATION = HERE.parent
REPOSITORY = HERE.parents[5]
INPUTS = INVESTIGATION / "research-progress/handoffs/27_TND_OC_E13_R1_INPUTS_20261109.json"
INPUTS_HASH = "968f65aa0e177570630e65a9f60731ea600cdf9a40bbf516152e6c4636940b54"
LADDER = (128, 256, 512)
NAMES = (
    "attempted_nodes", "accepted_segments", "scalar_calls", "cubic_calls",
    "boundary_segment_attempts", "boundary_subdivisions",
    "moment_segment_attempts", "moment_subdivisions",
    "precision_128", "precision_256", "precision_512",
    "kernel_128", "kernel_256", "kernel_512",
)
OFFSETS = {name: 8 * i for i, name in enumerate(NAMES)}
COUNTER_BYTES = 8 * len(NAMES)
LIMITS = {
    "attempted_nodes": 100000,
    "accepted_segments": 1000000,
    **{f"kernel_{bits}": 3200000 for bits in LADDER},
}
ZETA_CAP = 2000000
KERNEL_CAP = 9600000
TIME_CAP = 1800


class Meter:
    """Share exact counters with the supervisor even during a library call."""

    def __init__(self, mapping):
        self.mapping = mapping

    def __getitem__(self, name):
        return struct.unpack_from("<Q", self.mapping, OFFSETS[name])[0]

    def __call__(self, name):
        count = self[name]
        if name in LIMITS and count >= LIMITS[name]:
            raise GateError(name, f"cumulative cap {LIMITS[name]} exhausted")
        if name in ("scalar_calls", "cubic_calls"):
            if self["scalar_calls"] + self["cubic_calls"] >= ZETA_CAP:
                raise GateError("canonical_source_calls", f"cumulative cap {ZETA_CAP} exhausted")
        if name.startswith("kernel_") and sum(self[f"kernel_{bits}"] for bits in LADDER) >= KERNEL_CAP:
            raise GateError("kernel_total", f"cumulative cap {KERNEL_CAP} exhausted")
        struct.pack_into("<Q", self.mapping, OFFSETS[name], count + 1)


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def exact_dyadic(value):
    mantissa, exponent = value.man_exp()
    return [int(mantissa), int(exponent)]


def serialize_ball(value):
    return {"midpoint": exact_dyadic(value.mid()), "radius": exact_dyadic(value.rad())}


def real(value):
    value = Fraction(value)
    return arb(fmpq(value.numerator, value.denominator))


def coordinate(value):
    value = Fraction(value)
    denominator = value.denominator
    if denominator & (denominator - 1):
        raise GateError("centroid_dyadic", "non-dyadic centroid coordinate")
    return arb((value.numerator, 1 - denominator.bit_length()))


def projection(leaves, elementary):
    """Sum both ordered marks for each off-diagonal pair, and factorial diagonals."""
    data = []
    plus_offset = real(Fraction(1, 2))
    mark_coefficient = real(Fraction(8, 17))
    gap_coefficient = real(Fraction(25, 36))
    scale = 32 * arb(2).sqrt() * arb.pi().sqrt() / (51 * 2000)
    for count, x, y, _ in leaves:
        x, y = coordinate(x), coordinate(y)
        plus = elementary("exp", -mark_coefficient * (y - plus_offset)**2)
        minus = elementary("exp", -mark_coefficient * (y + plus_offset)**2)
        data.append((count, x, plus, minus))

    def center(m):
        return elementary("erf", 2000 - m) - elementary("erf", 1000 - m)

    total = arb(0)
    for i, (count, x, plus, minus) in enumerate(data):
        if count > 1:
            total += count * (count - 1) * plus * minus * center(x)
        for j in range(i):
            other_count, other_x, other_plus, other_minus = data[j]
            gap = elementary("exp", -gap_coefficient * (x - other_x)**2)
            mark_sum = plus * other_minus + other_plus * minus
            total += count * other_count * mark_sum * gap * center((x + other_x)/2)
    return scale * total


def analytic_error(count, leaves):
    # For a singleton the root is exactly its centroid, so it adds zero to S2.
    multiple_labels = sum(n for n, _, _, _ in leaves if n > 1)
    cluster = Fraction((18 * count + 5) * multiple_labels, 1000 * 2**24)
    centroid = Fraction(18 * count**2 + 4 * count, 1000 * 2**24)
    tail = Fraction(1, 2**32)
    return {"cluster": cluster, "centroid": centroid, "tail": tail,
            "total": cluster + centroid + tail}


def evaluate(count, leaves, meter, emit):
    if count < 0 or count > 1024 or len(leaves) > 1024:
        raise GateError("divisor_count", "final count or occupied-leaf cap")
    if sum(leaf[0] for leaf in leaves) != count or any(leaf[0] <= 0 for leaf in leaves):
        raise GateError("divisor_completeness", "occupied multiplicities do not sum to outer count")
    if any(not sigma.is_finite() or not (0 <= sigma <= arb((1, -24)))
           for _, _, _, sigma in leaves):
        raise GateError("centroid_radius", "invalid final Euclidean error")
    errors = analytic_error(count, leaves)
    for bits in LADDER:
        ctx.prec = bits
        meter(f"precision_{bits}")

        def elementary(name, argument):
            meter(f"kernel_{bits}")
            return getattr(argument, name)()

        approximation = projection(leaves, elementary)
        emit({"kind": "kernel_pass", "bits": bits,
              "arithmetic": serialize_ball(approximation) if approximation.is_finite() else None})
        if not approximation.is_finite() or not approximation.rad() <= arb(1) / 400:
            continue
        enclosure = approximation + arb(0, real(errors["total"]).upper())
        if enclosure.is_finite() and enclosure.rad() < arb(1) / 200:
            return {
                "status": "certified", "outer_count": count, "occupied_leaves": len(leaves),
                "multiplicities": dict(sorted(Counter(leaf[0] for leaf in leaves).items())),
                "precision_bits": bits, "arithmetic_ball": serialize_ball(approximation),
                "analytic_error_rationals": {k: str(v) for k, v in errors.items()},
                "canonical_ball": serialize_ball(enclosure),
                "canonical_lower_upper_exact_dyadic": [
                    exact_dyadic(enclosure.lower()), exact_dyadic(enclosure.upper())],
                "canonical_ball_display": enclosure.str(20),
            }
    raise GateError("projection_radius", "precision ladder exhausted at arithmetic or final radius gate")


def preflight():
    input_bytes = INPUTS.read_bytes()
    if hashlib.sha256(input_bytes).hexdigest() != INPUTS_HASH:
        raise GateError("frozen_manifest", "Inputs27 digest differs")
    drift = []
    for item in json.loads(input_bytes)["files"]:
        contents = (REPOSITORY / item["path"]).read_bytes()
        digest = hashlib.sha256(contents).hexdigest()
        if (len(contents), digest) == (item["bytes"], item["sha256"]):
            continue
        if item["role"] == "mathematical_contract":
            raise GateError("frozen_mathematics", f"hash differs for {item['path']}")
        drift.append({"role": item["role"], "path": item["path"],
                      "bytes": len(contents), "sha256": digest})
    result = subprocess.run([sys.executable, HERE / "check_b10_r2_cluster_constants.py"],
                            check=True, capture_output=True, text=True)
    return {"inputs_sha256": INPUTS_HASH, "context_drift": drift,
            "exact_constant_replay": json.loads(result.stdout)}


def run_worker(run_dir):
    ctx.threads = 1
    ctx.cap = 4
    with (run_dir / "counters.bin").open("r+b") as file, \
         mmap.mmap(file.fileno(), COUNTER_BYTES) as mapping, \
         (run_dir / "contours.jsonl").open("x", buffering=1) as events:
        meter = Meter(mapping)

        def emit(event):
            events.write(canonical_json(event) + "\n")

        try:
            count, leaves = acquire(zeta_source, meter, emit)
            emit({"kind": "acquisition_complete", "outer_count": count, "leaves": len(leaves)})
            result = evaluate(count, leaves, meter, emit)
        except GateError as error:
            result = {"status": "failed_gate", "gate": error.gate, "detail": error.detail}
        except Exception as error:
            emit({"kind": "implementation_exception", "detail": repr(error)})
            raise
        (run_dir / "worker-result.json").write_text(canonical_json(result) + "\n")


def log_summary(path):
    stored = hashlib.sha256()
    canonical = hashlib.sha256()
    kinds = Counter()
    last = None
    last_key_events = {}
    partial = False
    if not path.exists():
        return None
    with path.open("rb") as file:
        for line in file:
            stored.update(line)
            if not line.endswith(b"\n"):
                partial = True
                continue
            event = json.loads(line)
            kind = event.get("event", event.get("kind", "unspecified"))
            kinds[kind] += 1
            canonical.update((canonical_json(event) + "\n").encode())
            if "edges" in event:
                event["edge_fragment_counts"] = [len(edge) for edge in event.pop("edges")]
            last = event
            if kind in {"outer_count", "acquisition_complete", "cell_winding", "centroid",
                        "occupied_leaf", "leaf_completeness", "kernel_pass",
                        "candidate_cut_failed", "implementation_exception"}:
                last_key_events[kind] = last
    return {"bytes": path.stat().st_size, "stored_sha256": stored.hexdigest(),
            "canonical_content_sha256": canonical.hexdigest(),
            "truncated_last_line": partial, "event_counts": dict(kinds),
            "last_event": last, "last_key_events": last_key_events}


def supervise(run_dir, record):
    verified = preflight()
    run_dir = run_dir.resolve()
    if run_dir.is_relative_to(REPOSITORY):
        raise ValueError("Contour evidence directory must be outside the repository")
    if record.exists():
        raise FileExistsError(record)
    run_dir.mkdir()
    (run_dir / "counters.bin").write_bytes(bytes(COUNTER_BYTES))
    started = time.monotonic()
    worker = subprocess.Popen([sys.executable, __file__, "--worker", str(run_dir)])
    timed_out = False
    try:
        worker.wait(timeout=max(0, TIME_CAP - (time.monotonic() - started)))
    except subprocess.TimeoutExpired:
        timed_out = True
        worker.kill()
        worker.wait()
    elapsed = time.monotonic() - started
    result_path = run_dir / "worker-result.json"
    if timed_out:
        result = {"status": "failed_gate", "gate": "canonical_runtime",
                  "detail": "External supervisor stopped acquisition/evaluation at the 1800 s ceiling."}
    elif worker.returncode != 0 or not result_path.is_file():
        result = {"status": "failed_gate", "gate": "implementation",
                  "detail": f"Worker exit code {worker.returncode}; see external event log."}
    else:
        result = json.loads(result_path.read_text())
    raw = (run_dir / "counters.bin").read_bytes()
    counters = dict(zip(NAMES, struct.unpack("<" + "Q" * len(NAMES), raw), strict=True))
    summary = {
        "task": "TND-OC-E13 r1", "date_local": "2026-11-09", "timezone": "America/New_York",
        "prepared_for": "Edward Baker", "llm_assistance": "OpenAI Codex, with internal helper agents",
        "recorded_thread_model": "gpt-6.1-sol", "recorded_thread_effort": "ultra",
        "per_turn_backend_configuration": None, "repairs_used": 0,
        "runtime": {"python": platform.python_version(), "python_flint": flint.__version__,
                    "flint": flint.__FLINT_VERSION__, "threads": 1, "seconds": elapsed,
                    "external_timeout": timed_out, "ceiling_seconds": TIME_CAP},
        "preflight": verified, "result": result, "work": counters,
        "evidence_directory": str(run_dir), "contour_log": log_summary(run_dir / "contours.jsonl"),
        "code_sha256": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                        for name in ("e13_gaussian_pilot.py", "e13_contours.py")},
    }
    with record.open("x") as output:
        json.dump(summary, output, indent=2, sort_keys=True)
        output.write("\n")
    print(canonical_json(result))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("record", type=Path, nargs="?")
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        run_worker(args.run_dir)
    elif args.record is None:
        parser.error("small execution record path required")
    else:
        supervise(args.run_dir, args.record)


if __name__ == "__main__":
    main()
