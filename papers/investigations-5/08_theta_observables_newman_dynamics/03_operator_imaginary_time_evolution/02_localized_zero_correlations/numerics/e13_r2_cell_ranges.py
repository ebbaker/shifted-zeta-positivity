#!/usr/bin/env python3
"""Fixed Request29 endpoint evaluator and external work supervisor.

9 November 2026, prepared for Edward Baker with OpenAI Codex assistance.
OC chat0010 recorded GPT-6.1 Sol / ultra. Per-turn backend settings unavailable.
"""

import argparse
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

from e13_r2_controls import run_controls
from e13_r2_evidence import EvidenceError, verify_evidence


HERE = Path(__file__).resolve().parent
T = 1000
TAIL = Fraction(1, 2**32)
GEOMETRY_CAP = Fraction(1261, 409600)
ARITHMETIC_CAP = Fraction(1, 1000)
RADIUS_CAP = Fraction(1, 200)
LADDER = (128, 256, 512)
TIME_CAP = 600
SPECIAL_CAP = 1400000
CONTROL_CAP = 10000
CONSTANT_CAP = 100
NAMES = ("exp", "erf", "pi", "sqrt", "pairs", "control_exp_erf", "passes")
STRUCT = struct.Struct("<" + "Q" * len(NAMES))
OFFSETS = {name: 8 * i for i, name in enumerate(NAMES)}


class GateError(Exception):
    def __init__(self, gate, detail):
        super().__init__(str(detail))
        self.gate = gate
        self.detail = detail


class Meter:
    """Make the counters available to the supervisor during library calls."""

    def __init__(self, mapping):
        self.mapping = mapping
        self.in_controls = False

    def __getitem__(self, name):
        return struct.unpack_from("<Q", self.mapping, OFFSETS[name])[0]

    def increment(self, name):
        struct.pack_into("<Q", self.mapping, OFFSETS[name], self[name] + 1)

    def __call__(self, name):
        if name in ("exp", "erf"):
            if self["exp"] + self["erf"] >= SPECIAL_CAP:
                raise GateError("elementary_calls", "cumulative exp/erf cap exhausted")
            if self.in_controls:
                if self["control_exp_erf"] >= CONTROL_CAP:
                    raise GateError("control_calls", "control exp/erf cap exhausted")
                self.increment("control_exp_erf")
        if name in ("pi", "sqrt") and self["pi"] + self["sqrt"] >= CONSTANT_CAP:
            raise GateError("constant_calls", "cumulative pi/sqrt cap exhausted")
        self.increment(name)

    def snapshot(self):
        return dict(zip(NAMES, STRUCT.unpack_from(self.mapping), strict=True))


def point(value):
    """Represent a dyadic exactly, or round a rational outward."""
    q = Fraction(value)
    d = q.denominator
    if d & (d - 1) == 0:
        return arb((q.numerator, 1 - d.bit_length()))
    return arb(fmpq(q.numerator, d))


def dyadic(value):
    m, e = value.man_exp()
    return [int(m), int(e)]


def unpack_dyadic(encoded):
    m, e = encoded
    if type(m) is not int or type(e) is not int:
        raise GateError("serialization", "invalid dyadic mantissa or exponent")
    return Fraction(m) * Fraction(2) ** e


def ball_fields(value):
    if not value.is_finite():
        raise GateError("nonfinite_endpoint", "endpoint arithmetic returned a nonfinite ball")
    return {"midpoint": dyadic(value.mid()), "radius": dyadic(value.rad())}


def bounds(value):
    fields = ball_fields(value)
    m = unpack_dyadic(fields["midpoint"])
    r = unpack_dyadic(fields["radius"])
    return m - r, m + r


def clip(value, cap, is_lower):
    """Outward monotone clipping, with shortcuts only for certain branches."""
    if not value.is_finite():
        raise GateError("nonfinite_endpoint", "nonfinite center endpoint")
    threshold = point(cap)
    if is_lower:
        if value >= threshold:
            return value
        if value <= threshold:
            return threshold
        op = max
    else:
        if value <= threshold:
            return value
        if value >= threshold:
            return threshold
        op = min
    a, b = bounds(value)
    return point(op(cap, a)).union(point(op(cap, b)))


def squared_range(lo, hi):
    """Exact range of t² on [lo,hi]."""
    a, b = lo**2, hi**2
    return (Fraction(0) if lo <= 0 <= hi else min(a, b), max(a, b))


def range_sum(cells, meter, *, drop_order=False, drop_self=False):
    """Outward evaluations of the lower and upper endpoint expressions."""
    cells = tuple(cells)
    if not cells:
        return arb(0), arb(0)

    def elementary(name, q):
        meter(name)
        return getattr(point(q), name)()

    def mark(lo, hi, shift):
        near, far = squared_range(lo - shift, hi - shift)
        return (elementary("exp", -Fraction(8, 17) * far),
                elementary("exp", -Fraction(8, 17) * near))

    meter("sqrt")
    scale = 32 * arb(2).sqrt() / 51
    meter("pi")
    pi = arb.pi()
    meter("sqrt")
    normalization = pi.sqrt() / (2 * T)
    half = Fraction(1, 2)
    data = [(lo, hi, n, mark(yl, yh, half), mark(yl, yh, -half))
            for lo, hi, yl, yh, n in cells]

    def base(l, u, other_l, other_u):
        mlo, mhi = (l + other_l)/2, (u + other_u)/2
        ilo = normalization * (elementary("erf", 2*T - mhi)
                               - elementary("erf", T - mlo))
        ihi = normalization * (elementary("erf", 2*T - mlo)
                               - elementary("erf", T - mhi))
        near, far = squared_range(other_l - u, other_u - l)
        return (clip(ilo, Fraction(0), True) * elementary("exp", -Fraction(25, 36)*far),
                clip(ihi, Fraction(2, T), False) * elementary("exp", -Fraction(25, 36)*near))

    lower, upper = arb(0), arb(0)
    for i, (l, u, n, plus, minus) in enumerate(data):
        if n > 1 and not drop_self:
            a, b = base(l, u, l, u)
            weight = n * (n - 1)
            lower += weight * a * plus[0] * minus[0]
            upper += weight * b * plus[1] * minus[1]
        for j in range(i + 1, len(data)):
            meter("pairs")
            other_l, other_u, k, other_plus, other_minus = data[j]
            a, b = base(l, u, other_l, other_u)
            marks_lo = plus[0] * other_minus[0]
            marks_hi = plus[1] * other_minus[1]
            if not drop_order:
                marks_lo += other_plus[0] * minus[0]
                marks_hi += other_plus[1] * minus[1]
            lower += n * k * a * marks_lo
            upper += n * k * b * marks_hi
    return scale * lower, scale * upper


def check_final_radius(a, b):
    if a > b:
        raise GateError("endpoint_order", "lower bound exceeds upper bound")
    if b - a >= 2 * RADIUS_CAP:
        raise GateError("final_radius", "exact final half-width is not strictly below 1/200")


def finalize(lower, upper, tail=TAIL):
    lo, hi = ball_fields(lower), ball_fields(upper)
    lo_mid, lo_rad = (unpack_dyadic(lo[k]) for k in ("midpoint", "radius"))
    hi_mid, hi_rad = (unpack_dyadic(hi[k]) for k in ("midpoint", "radius"))
    if lo_rad + hi_rad > ARITHMETIC_CAP:
        raise GateError("endpoint_arithmetic_radius", str(lo_rad + hi_rad))
    a, b = lo_mid - lo_rad, hi_mid + hi_rad
    if a > b:
        raise GateError("endpoint_order", "outward endpoint order is reversed")
    left, right = a - tail, b + tail
    check_final_radius(left, right)
    return {
        "lower_endpoint_ball": lo, "upper_endpoint_ball": hi,
        "arithmetic_radius_sum": str(lo_rad + hi_rad),
        "ideal_geometric_radius_strict_cap": str(GEOMETRY_CAP),
        "complete_omitted_divisor_allowance": str(tail),
        "conditional_radius_strict_cap": str(GEOMETRY_CAP + ARITHMETIC_CAP + tail),
        "exact_endpoints": [str(left), str(right)],
        "exact_radius": str((right - left)/2),
    }


def verify_serialized(certificate):
    """Reconstruct the interval and gates in exact rational arithmetic."""
    left_ball = certificate["lower_endpoint_ball"]
    right_ball = certificate["upper_endpoint_ball"]
    r_left, r_right = (unpack_dyadic(b["radius"]) for b in (left_ball, right_ball))
    if min(r_left, r_right) < 0:
        raise GateError("serialization", "negative serialized radius")
    if r_left + r_right > ARITHMETIC_CAP:
        raise GateError("endpoint_arithmetic_radius", "serialized arithmetic gate failed")
    if Fraction(certificate["arithmetic_radius_sum"]) != r_left + r_right:
        raise GateError("serialization", "arithmetic radius sum changed")
    if Fraction(certificate["complete_omitted_divisor_allowance"]) != TAIL:
        raise GateError("serialization", "omitted-divisor allowance changed")
    if Fraction(certificate["ideal_geometric_radius_strict_cap"]) != GEOMETRY_CAP or (
        Fraction(certificate["conditional_radius_strict_cap"]) != GEOMETRY_CAP + ARITHMETIC_CAP + TAIL
    ):
        raise GateError("serialization", "analytic allowance changed")
    left, right = map(Fraction, certificate["exact_endpoints"])
    reconstructed_left = unpack_dyadic(left_ball["midpoint"]) - (r_left + TAIL)
    reconstructed_right = unpack_dyadic(right_ball["midpoint"]) + (r_right + TAIL)
    if left != reconstructed_left or right != reconstructed_right:
        raise GateError("serialization", "serialized endpoints disagree with exact ball bounds")
    if left + TAIL > right - TAIL:
        raise GateError("endpoint_order", "serialized finite endpoints are reversed")
    radius = Fraction(certificate["exact_radius"])
    if radius < 0 or 2 * radius != right - left:
        raise GateError("serialization", "serialized radius does not match interval")
    if radius >= RADIUS_CAP:
        raise GateError("final_radius", "serialized radius is not strictly below 1/200")


def write_json(path, data):
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(data, sort_keys=True, indent=2, allow_nan=False) + "\n")
    temp.replace(path)


def work(run_dir, trace, progress_override):
    start = time.monotonic()
    ctx.threads = 1
    with (run_dir / "counters.bin").open("r+b") as f, mmap.mmap(f.fileno(), STRUCT.size) as mm:
        meter = Meter(mm)

        def stage(label):
            write_json(run_dir / "stage.json", {"last_completed_stage": label,
                                               "elapsed_worker_seconds": time.monotonic() - start})

        output = {"status": "failed_gate", "passes": []}
        try:
            if (flint.__version__, flint.__FLINT_VERSION__) != ("0.9.0", "3.6.0"):
                raise GateError("environment", "the inspected python-flint/FLINT versions are required")
            stage("runtime_verified")
            override = json.loads(progress_override.read_text()) if progress_override else None
            if override and "replay_progress_override" in override:
                override = override["replay_progress_override"]
            rows, evidence = verify_evidence(relocated_trace=trace, progress_override=override, stage=stage)
            output["evidence"] = evidence
            cells = [(*box, n) for box, n in rows]
            if len(cells) != 388 or any(n != 1 for *_, n in cells):
                raise GateError("census", "frozen singleton census failed")

            meter.in_controls = True
            ctx.prec = 128
            controls = run_controls(sys.modules[__name__], meter)
            meter.in_controls = False
            if controls["fixtures"] + evidence["evidence_fixtures"] > 32:
                raise GateError("control_fixtures", "combined fixture cap exhausted")
            output["controls"] = controls
            stage("synthetic_controls_passed")
            for bits in LADDER:
                ctx.prec = bits
                meter("passes")
                initial = meter.snapshot()
                pass_start = time.monotonic()
                lower, upper = range_sum(cells, meter)
                final = meter.snapshot()
                if final["pairs"] - initial["pairs"] != 75078:
                    raise GateError("pair_census", "the pass did not visit exactly 75078 pairs")
                if final["exp"] - initial["exp"] != 151708 or final["erf"] - initial["erf"] != 300312:
                    raise GateError("pair_work", "the pass did not evaluate every declared endpoint")
                pass_record = {"bits": bits, "seconds": time.monotonic() - pass_start,
                               "work": {k: final[k] - initial[k] for k in final if k != "passes"}}
                output["passes"].append(pass_record)
                stage(f"endpoint_expressions_{bits}_bits_completed")
                try:
                    certificate = finalize(lower, upper)
                except GateError as error:
                    pass_record["failed_gate"] = error.gate
                    pass_record["detail"] = error.detail
                    if error.gate not in {"endpoint_arithmetic_radius", "final_radius", "nonfinite_endpoint"}:
                        raise
                    continue
                certificate_path = run_dir / "certificate.json"
                write_json(certificate_path, certificate)
                reloaded = json.loads(certificate_path.read_text())
                verify_serialized(reloaded)
                stage("exact_certificate_reload_passed")
                output.update(status="certified", certificate=reloaded, exact_reload_verified=True)
                break
            else:
                first = output["passes"][0]["failed_gate"]
                raise GateError(first, "no precision pass satisfied the gates")
        except (GateError, EvidenceError) as error:
            output.update(status="failed_gate", gate=error.gate, detail=error.detail)
        except Exception as error:
            output.update(status="failed_gate", gate="implementation", detail=repr(error))
        write_json(run_dir / "worker-result.json", output)


def supervise(args):
    if args.record is None:
        raise ValueError("small execution record is required")
    if args.record.exists():
        raise FileExistsError(args.record)
    args.run_dir.mkdir()
    (args.run_dir / "counters.bin").write_bytes(bytes(STRUCT.size))
    call = [sys.executable, __file__, str(args.run_dir), "--worker"]
    if args.trace:
        call.extend(("--trace", str(args.trace)))
    if args.progress_override:
        call.extend(("--progress-override", str(args.progress_override)))
    started = time.monotonic()
    worker = subprocess.Popen(call)
    timed_out = False
    try:
        worker.wait(timeout=max(0, TIME_CAP - (time.monotonic() - started)))
    except subprocess.TimeoutExpired:
        timed_out = True
        worker.kill()
        worker.wait()
    elapsed = time.monotonic() - started
    raw = (args.run_dir / "counters.bin").read_bytes()
    counts = dict(zip(NAMES, STRUCT.unpack(raw), strict=True))
    stage_path = args.run_dir / "stage.json"
    stage = json.loads(stage_path.read_text()) if stage_path.is_file() else None
    result_path = args.run_dir / "worker-result.json"
    if timed_out:
        result = {"status": "failed_gate", "gate": "external_elapsed_time", "detail": "600 s ceiling"}
    elif worker.returncode or not result_path.is_file():
        result = {"status": "failed_gate", "gate": "implementation",
                  "detail": f"worker exited {worker.returncode} without a valid result"}
    else:
        result = json.loads(result_path.read_text())
    code_paths = (HERE / f"e13_r2_{name}.py" for name in ("cell_ranges", "evidence", "controls"))
    record = {
        "task": "TND-OC-E13 r2", "date_local": "2026-11-09", "timezone": "America/New_York",
        "prepared_for": "Edward Baker", "llm_assistance": "OpenAI Codex with internal helpers",
        "recorded_thread_model": "gpt-6.1-sol", "recorded_thread_effort": "ultra",
        "per_turn_backend_configuration": None, "repairs_used": 0,
        "runtime": {"python": platform.python_version(), "python_flint": flint.__version__,
                    "flint": flint.__FLINT_VERSION__, "external_elapsed_seconds": elapsed,
                    "external_cap_seconds": TIME_CAP, "external_timeout": timed_out, "workers": 1},
        "last_stage": stage, "work": counts, "canonical_source_calls": 0, "centroid_calls": 0,
        "run_directory": str(args.run_dir.resolve()), "result": result,
        "code_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in code_paths},
    }
    write_json(args.record, record)
    print(json.dumps({"status": result["status"], "gate": result.get("gate"), "work": counts,
                      "elapsed": elapsed, "record": str(args.record)}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("record", type=Path, nargs="?")
    parser.add_argument("--trace", type=Path)
    parser.add_argument("--progress-override", type=Path)
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        work(args.run_dir, args.trace, args.progress_override)
    else:
        supervise(args)


if __name__ == "__main__":
    main()
