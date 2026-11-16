#!/usr/bin/env python3
"""Generate the frozen TN6-E02 r1 certificate with python-flint 0.9.0.

Invoke with a Python containing python-flint, followed by --output NEW.json.
The parent watchdog can interrupt native FLINT calls. Checkpoints are
atomic, and the total/attempt counters survive an interrupted worker.
"""

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from math import factorial
import multiprocessing as mp
import os
from pathlib import Path
import platform
import sys
import time

import flint
from flint import acb, acb_mat, arb, arb_mat, ctx, fmpq

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REQUEST = HERE.parent / "research-progress/handoffs/TN6-E02-r1.md"
MANIFEST = HERE / "08_TN6_E02_R1_INPUT_MANIFEST_20261114.json"
INPUT_HASHES = {
    REQUEST: "3c581245746f1714b08e928191f84cf6f23528fe4eb2ad94ec04483ce56a56c7",
    MANIFEST: "48727341987b33e7ebe0f9c3914142d4d653085276ce21479682561e241bc0f2",
}
N, U, M = 16, 2, 8
PRECISIONS = (128, 256, 512)
PANELS = tuple((Fraction(j, 2), Fraction(j + 1, 2)) for j in range(4))
POINTS = tuple((t, x) for t in (Fraction(0), Fraction(1, 4), Fraction(1, 2))
               for x in (0, 4, 8))
CAPS = {
    "truncation_Q": Fraction(5, 10**9),
    "acquisition_9delta": Fraction(2, 10**9),
    "normalization_eta_Z": Fraction(1, 10**9),
    "each_chain_rounding": Fraction(1, 10**9),
    "each_chain_total": Fraction(1, 10**8),
    "each_direct_radius": Fraction(1, 10**9),
}
TOTAL_CALLBACKS, ATTEMPT_CALLBACKS = 800_000, 400_000
TOTAL_SECONDS, INTEGRAL_SECONDS, MATRIX_SECONDS = 900, 15, 30
SOURCE_LIMIT_EXIT = 75


class GateFailure(Exception):
    """A numerical acceptance gate failed at this precision."""


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def check_inputs():
    for path, digest in INPUT_HASHES.items():
        if sha256(path.read_bytes()) != digest:
            raise ValueError(f"frozen input digest mismatch: {path}")
    manifest = json.loads(MANIFEST.read_bytes())
    for entry in manifest["inputs"]:
        contents = (ROOT / entry["path"]).read_bytes()
        if len(contents) != entry["bytes"] or sha256(contents) != entry["sha256"]:
            raise ValueError(f'frozen input identity mismatch: {entry["path"]}')
    return manifest["inputs"]


def now_utc():
    return datetime.now(timezone.utc).isoformat()


def rational(x):
    return Fraction(str(x.fmpq()))


def exact_ball(q):
    return arb(fmpq(q.numerator, q.denominator))


def enclosing_radius(radius):
    """A ball centered at zero covering the rational radius outward."""
    return arb(0, exact_ball(radius).abs_upper())


def endpoints(lo, hi):
    pair = [str(lo), str(hi)]
    if [Fraction(s) for s in pair] != [lo, hi]:
        raise ArithmeticError("rational interval endpoint roundtrip failed")
    return pair


def pack_real(value):
    """Represent the actual Arb midpoint +/- magnitude by exact rationals."""
    if not value.is_finite():
        raise GateFailure("nonfinite real ball")
    mid, rad = rational(value.mid()), rational(value.rad())
    rebuilt = arb(exact_ball(mid), exact_ball(rad))
    if not rebuilt.contains(value):
        raise ArithmeticError("ball roundtrip failed to contain the original")
    return {"endpoints": endpoints(mid - rad, mid + rad),
            "midpoint": str(mid), "radius": str(rad)}


def pack_complex(value):
    if not value.is_finite():
        raise GateFailure("nonfinite complex ball")
    return {"real": pack_real(value.real), "imag": pack_real(value.imag)}


def ball_row_norm_upper(matrix):
    return max(sum(rational(matrix[i, j].abs_upper()) for j in range(matrix.ncols()))
               for i in range(matrix.nrows()))


def spatial_bound(pi):
    r = pi * (4 * U * arb(1)).exp()
    return 10 * (r + 2) * (-r / 2).exp()


def tail_bounds():
    pi = arb.pi()
    first = (M + 1)**4 * (-pi * (M + 1)**2).exp()
    ratio = (arb(M + 2) / (M + 1))**4 * (-(2 * M + 3) * pi).exp()
    if not ratio < 1:
        raise GateFailure("omitted-mode ratio upper bound is not below 1")
    common = 4 * pi**2 * (arb(U*U) / 2 + 9 * U).exp() * first / (1 - ratio)
    a = [rational((common * U**(2*k + 1)).upper()) for k in range(N + 1)]
    b = rational(spatial_bound(pi).upper())
    return a, b


def chain_bound_factor():
    return sum(Fraction(8**(2*N - 2*k), 2**k * factorial(k) * factorial(2*N - 2*k))
               for k in range(N + 1))


def atomic_checkpoint(path, record):
    staged = path.with_suffix(path.suffix + ".tmp")
    staged.write_text(json.dumps(record, indent=2, allow_nan=False) + "\n")
    os.replace(staged, path)


class Runner:
    def __init__(self, path, record, events, counts):
        self.path, self.record, self.events, self.counts = path, record, events, counts
        self.attempt = None

    def save(self):
        if self.attempt is not None:
            self.attempt["source_callbacks"] = self.counts[0] - self.attempt["start_callbacks"]
            self.attempt["finite_mode_evaluations"] = self.counts[1] - self.attempt["start_modes"]
        atomic_checkpoint(self.path, self.record)

    @contextmanager
    def phase(self, name):
        self.attempt["current_phase"] = name
        start = time.monotonic()
        self.save()
        try:
            yield
        finally:
            self.attempt["phase_wall_seconds"][name] = time.monotonic() - start
            self.save()

    @contextmanager
    def operation(self, entry, kind, limit_seconds):
        self.attempt[kind].append(entry)
        entry.update({
            "status": "active",
            "start_callbacks": self.counts[0],
            "start_modes": self.counts[1],
        })
        self.save()
        start = time.monotonic()
        self.events.send(("start", kind, len(self.attempt[kind]) - 1, start, limit_seconds))
        try:
            yield
            entry["status"] = "returned"
        except Exception as error:
            entry.update(status="failed", failure=str(error))
            raise
        finally:
            finish = time.monotonic()
            entry.update(
                wall_seconds=finish - start,
                source_callbacks=self.counts[0] - entry["start_callbacks"],
                finite_mode_evaluations=self.counts[1] - entry["start_modes"],
            )
            self.events.send(("finish", finish))
            if entry["wall_seconds"] > limit_seconds:
                entry.update(status="failed", failure=f"{limit_seconds}s per-call wall time exceeded")
            self.save()
            if entry["wall_seconds"] > limit_seconds:
                raise GateFailure(entry["failure"])

    def evaluate_integral(self, entry, panels, multiplier):
        p = self.attempt["precision_bits"]
        tolerance = exact_ball(Fraction(1, 2**(p - 32)))
        base_pi = arb.pi()
        mode_values = [base_pi * m*m for m in range(1, M + 1)]
        attempt_ceiling = self.attempt["start_callbacks"] + ATTEMPT_CALLBACKS
        source_ceiling = min(attempt_ceiling, TOTAL_CALLBACKS)

        def integrand(z, _analytic):
            # All powers are integers and all transcendental functions entire.
            self.counts[0] += 1
            growth = (4*z).exp()
            modes = acb(0)
            for pim2 in mode_values:
                r = growth * pim2
                modes += r * (2*r - 3) * (-r).exp()
                self.counts[1] += 1
            square = z * z
            value = (square / 2 + z).exp() * modes * multiplier(z, square)
            if self.counts[0] >= source_ceiling:
                # Cython may trap callback exceptions. A hard stop at the exact
                # ceiling preserves completed work and the shared counters.
                os._exit(SOURCE_LIMIT_EXIT)
            return value

        start, end = panels
        with self.operation(entry, "integrations", INTEGRAL_SECONDS):
            integral = acb.integral(
                integrand, exact_ball(start), exact_ball(end),
                abs_tol=tolerance, rel_tol=tolerance,
                deg_limit=64, eval_limit=8000, depth_limit=20,
            )
            entry["enclosure"] = pack_complex(integral)
            if not integral.imag.contains(0):
                raise GateFailure("a real-path integral has an imaginary enclosure excluding zero")
        return integral.real

    def panels(self, label, multiplier):
        values = []
        for start, end in PANELS:
            entry = {"quantity": label, "panel": [str(start), str(end)]}
            values.append(self.evaluate_integral(entry, (start, end), multiplier))
        return sum(values)

    def acquire(self):
        a, b = tail_bounds()
        self.attempt["tails"] = {
            "omitted_arithmetic_upper_by_even_degree": [str(value) for value in a],
            "spatial_upper_all_even_degrees": str(b),
            "direct_symmetric_radius": str((a[0] + b) / 2),
        }
        moments = []
        for k, omitted_arithmetic in enumerate(a):
            retained = self.panels({"moment_degree": 2*k}, lambda z, _: z**(2*k))
            half_tail = (omitted_arithmetic + b) / 2
            moment = 2 * retained + exact_ball(half_tail) + enclosing_radius(half_tail)
            moments.append(moment)
            self.attempt["moments"].append({"degree": 2*k, **pack_real(moment)})
            self.save()
        return moments, (a[0] + b) / 2

    def condition(self, moments, degrees):
        # D^(-1/2) G D^(-1/2), D = diag(G). Diagonal entries are
        # exactly one for every choice of the measured moments.
        diag_roots = [moments[i].sqrt() for i in degrees]
        block = arb_mat(len(degrees), len(degrees), [
            1 if i == j else moments[(d + e) // 2] / (diag_roots[i] * diag_roots[j])
            for i, d in enumerate(degrees) for j, e in enumerate(degrees)
        ])
        try:
            inverse = block.inv()
        except ZeroDivisionError as error:
            return {"status": "validated inverse unavailable", "detail": str(error)}
        norm = ball_row_norm_upper(block)
        inv_norm = ball_row_norm_upper(inverse)
        return {"status": "enclosed", "norm_inf_upper": str(norm),
                "inverse_norm_inf_upper": str(inv_norm), "kappa_inf_upper": str(norm * inv_norm)}

    def ldl(self, moments):
        norms = {}
        for parity in (0, 1):
            degrees = list(range(parity, N + 1, 2))
            lower = [[arb(0) for _ in degrees] for _ in degrees]
            pivots = []
            for i, degree in enumerate(degrees):
                pivot = moments[degree] - sum(lower[i][k]**2 * pivots[k] for k in range(i))
                norms[degree] = pivot
                enclosure = pack_real(pivot)
                positive = Fraction(enclosure["endpoints"][0]) > 0
                entry = {"degree": degree, "positive": positive, **enclosure}
                self.attempt["pivots"].append(entry)
                self.save()
                if not positive:
                    raise GateFailure(f"first undecided or nonpositive LDL pivot: h_{degree}")
                entry["relative_radius_to_midpoint"] = str(rational(pivot.rad()) / rational(pivot.mid()))
                entry["norm_to_diagonal"] = pack_real(pivot / moments[degree])
                pivots.append(pivot)
                for j in range(i + 1, len(degrees)):
                    cross = moments[(degrees[j] + degree) // 2]
                    correction = sum(lower[j][k] * lower[i][k] * pivots[k] for k in range(i))
                    lower[j][i] = (cross - correction) / pivot
            self.attempt["scaled_condition"][str(parity)] = self.condition(moments, degrees)
            self.save()
        return norms

    def nominal(self, norms):
        couplings = []
        for n in range(1, N + 1):
            a = (norms[n] / norms[n - 1]).sqrt()
            enclosure = pack_real(a)
            self.attempt["couplings"].append({"edge": n, **enclosure})
            self.save()
            if Fraction(enclosure["endpoints"][0]) <= 0:
                raise GateFailure(f"a_{n} is not certified strictly positive")
            couplings.append(a)
        mass = norms[0]
        mass_lower, mass_upper = (Fraction(s) for s in pack_real(mass)["endpoints"])
        mass_mid = rational(mass.mid())
        radii = [Fraction(0)] + [rational(a.rad()) for a in couplings[:N-1]] + [Fraction(0)]
        delta = max(radii[i] + radii[i + 1] for i in range(N))
        factor = chain_bound_factor()
        normalized_h = norms[N] / mass
        self.attempt["normalization"] = pack_real(mass)
        self.attempt["norm16_div_mass"] = pack_real(normalized_h)
        uniform = {
            "truncation_Q": rational(normalized_h.upper()) * factor,
            "acquisition_9delta": 9 * delta,
            "normalization_eta_Z": rational(mass.rad()) / mass_lower,
        }
        ideal_error = sum(uniform.values())
        self.attempt["uniform_error"] = {key: str(value) for key, value in uniform.items()}
        physical_error = ideal_error * mass_upper / 2
        self.attempt["uniform_error"].update({
            "S16": str(factor), "delta": str(delta), "sum": str(ideal_error),
            "physical_absolute_upper": str(physical_error),
        })
        self.save()
        for key, value in uniform.items():
            if value > CAPS[key]:
                raise GateFailure(f"{key} exceeds its normalized allowance")
        edges = [a.mid() for a in couplings[:N-1]]
        matrix = acb_mat(N, N, [
            edges[min(i, j)] if abs(i - j) == 1 else 0
            for i in range(N) for j in range(N)
        ])
        return matrix, mass_lower, mass_mid, ideal_error, physical_error

    def chain(self, matrix, mass_lower, mass_mid, ideal_error, physical_error):
        chain = []
        square = matrix * matrix
        for tau, x in POINTS:
            point = [str(tau), x]
            entry = {"point": point}
            exponent = matrix * acb(0, x) - square * exact_ball(tau)
            with self.operation(entry, "matrix_exponentials", MATRIX_SECONDS):
                entry_exp = exponent.exp()[0, 0]
                entry["matrix_entry"] = pack_complex(entry_exp)
                if not entry_exp.imag.contains(0):
                    raise GateFailure("parity requires the matrix scalar to be real")
            computed = entry_exp.real * exact_ball(mass_mid) / 2
            packed = pack_real(computed)
            mid, rad = Fraction(packed["midpoint"]), Fraction(packed["radius"])
            normalized_rounding = 2 * rad / mass_lower
            total = ideal_error + normalized_rounding
            field_interval = endpoints(mid - rad - physical_error, mid + rad + physical_error)
            chain.append((packed, field_interval))
            self.attempt["chain_samples"].append({
                "point": point, "nominal_physical_ball": packed,
                "physical_field_enclosure": field_interval,
                "normalized_numerical_error": str(normalized_rounding),
                "normalized_total": str(total),
            })
            self.save()
            if normalized_rounding > CAPS["each_chain_rounding"]:
                raise GateFailure(f"chain numerical radius exceeds its cap at {point}")
            if total > CAPS["each_chain_total"]:
                raise GateFailure(f"chain total error exceeds its cap at {point}")
        return chain

    def baseline(self, chain, tail, mass_lower):
        for (tau, x), (chain_value, field_interval) in zip(POINTS, chain):
            point = [str(tau), x]
            retained = self.panels(
                {"direct_sample": point},
                lambda z, square: (-exact_ball(tau) * square).exp() * (x * z).cos(),
            )
            direct = retained + enclosing_radius(tail)
            packed = pack_real(direct)
            direct_lo, direct_hi = (Fraction(v) for v in packed["endpoints"])
            chain_lo, chain_hi = (Fraction(v) for v in chain_value["endpoints"])
            chain_mid = Fraction(chain_value["midpoint"])
            field_lo, field_hi = (Fraction(v) for v in field_interval)
            overlap = max(direct_lo, field_lo) <= min(direct_hi, field_hi)
            normalized_radius = 2 * Fraction(packed["radius"]) / mass_lower
            self.attempt["direct_samples"].append({
                "point": point, "retained_physical_ball": pack_real(retained),
                "complete_physical_ball": packed, "normalized_radius": str(normalized_radius),
                "overlap_with_enlarged_chain": overlap,
                "nominal_minus_direct_physical_interval": endpoints(
                    chain_lo - direct_hi, chain_hi - direct_lo),
                "computed_midpoint_minus_direct_physical_interval": endpoints(
                    chain_mid - direct_hi, chain_mid - direct_lo),
            })
            self.save()
            if normalized_radius > CAPS["each_direct_radius"]:
                raise GateFailure(f"direct baseline radius exceeds its cap at {point}")
            if not overlap:
                raise GateFailure(f"matched complete-source enclosures are disjoint at {point}")

    def execute(self):
        for precision in PRECISIONS:
            start = time.monotonic()
            ctx.prec, ctx.threads = precision, 1
            self.attempt = {
                "precision_bits": precision, "status": "active",
                "requested_abs_and_rel_tolerance": str(Fraction(1, 2**(precision - 32))),
                "start_callbacks": self.counts[0], "start_modes": self.counts[1],
                "start_monotonic_seconds": start,
                "phase_wall_seconds": {}, "integrations": [], "matrix_exponentials": [],
                "moments": [], "pivots": [], "scaled_condition": {}, "couplings": [],
                "chain_samples": [], "direct_samples": [],
            }
            self.record["attempts"].append(self.attempt)
            self.save()
            try:
                with self.phase("acquisition"):
                    moments, tail = self.acquire()
                    norms = self.ldl(moments)
                    nominal = self.nominal(norms)
                with self.phase("chain_readouts"):
                    chain = self.chain(*nominal)
                with self.phase("direct_baseline"):
                    mass_lower = nominal[1]
                    self.baseline(chain, tail, mass_lower)
            except GateFailure as error:
                self.attempt.update(status="precision gate failed", failure=str(error))
            else:
                self.attempt["status"] = "complete pass"
                self.record["outcome"] = "complete pass"
            self.attempt["wall_seconds"] = time.monotonic() - start
            self.save()
            if self.record["outcome"] == "complete pass":
                return
        self.record["outcome"] = "precision ladder exhausted"
        self.save()


def worker(output, provenance, events, counts):
    runner = Runner(output, provenance, events, counts)
    try:
        runner.execute()
    except Exception as error:
        if runner.attempt is not None:
            runner.attempt.update(status="implementation error", failure=repr(error))
        provenance["outcome"] = "implementation error"
        runner.save()
        raise
    finally:
        events.close()


def watchdog(args, record):
    context = mp.get_context("spawn")
    watch, events = context.Pipe(duplex=False)
    counts = context.Array("q", [0, 0], lock=False)
    process = context.Process(target=worker, args=(args.output, record, events, counts))
    atomic_checkpoint(args.output, record)
    start = time.monotonic()
    process.start()
    events.close()
    active = None
    failure = None
    per_attempt_interrupt = None
    while True:
        if watch.poll(0.01):
            try:
                message = watch.recv()
            except EOFError:
                break
            if message[0] == "start":
                active = message[1:]
            elif active is not None:
                kind, index, begin, seconds = active
                if message[1] - begin > seconds:
                    # The worker also enforces this gate and records the return.
                    per_attempt_interrupt = f"{kind}[{index}] overshot its elapsed-time limit"
                active = None
        elapsed = time.monotonic()
        if elapsed - start >= TOTAL_SECONDS:
            failure = "total numerical wall-time limit reached"
            break
        if active is not None:
            kind, index, begin, seconds = active
            if elapsed - begin >= seconds:
                failure = f"{kind}[{index}] reached its {seconds}s wall-time limit"
                break
        if not process.is_alive() and not watch.poll():
            break
    if failure is not None and process.is_alive():
        process.kill()
    process.join()
    watch.close()
    elapsed = time.monotonic() - start
    saved = json.loads(args.output.read_text())
    if failure is None and process.exitcode == SOURCE_LIMIT_EXIT:
        last_attempt = saved["attempts"][-1]
        maximum = TOTAL_CALLBACKS if counts[0] >= TOTAL_CALLBACKS else ATTEMPT_CALLBACKS
        failure = f"the {maximum} source callback ceiling was reached"
        active_entries = [entry for entry in last_attempt["integrations"] if entry["status"] == "active"]
        if active_entries:
            index = last_attempt["integrations"].index(active_entries[-1])
            active = ("integrations", index, None, None)
    if failure is None and process.exitcode != 0 and saved["outcome"] == "active":
        failure = f"worker exited early with code {process.exitcode}"
    if failure is not None:
        saved["outcome"] = "work limit reached" if "limit" in failure or "ceiling" in failure else "worker failure"
        saved["failure"] = failure
        if saved["attempts"]:
            last_attempt = saved["attempts"][-1]
            last_attempt.update(
                status=saved["outcome"], failure=failure,
                wall_seconds=time.monotonic() - last_attempt["start_monotonic_seconds"],
                source_callbacks=counts[0] - last_attempt["start_callbacks"],
                finite_mode_evaluations=counts[1] - last_attempt["start_modes"],
            )
            if active is not None:
                kind, index, begin, _ = active
                entry = last_attempt[kind][index]
                entry.update(
                    status="interrupted", failure=failure,
                    source_callbacks=counts[0] - entry["start_callbacks"],
                    finite_mode_evaluations=counts[1] - entry["start_modes"],
                )
                if begin is not None:
                    entry["interruption_observed_seconds"] = elapsed + start - begin
    saved["process_execution"].update({
        "finished_utc": now_utc(),
        "numerical_process_wall_seconds": elapsed,
        "source_callbacks": counts[0], "finite_mode_evaluations": counts[1],
        "worker_exit_code": process.exitcode,
        "watchdog_return_overshoot": per_attempt_interrupt,
    })
    if saved["outcome"] == "complete pass":
        successful = saved["attempts"][-1]
        spent = [sum(a["phase_wall_seconds"].get(phase, 0.0) for a in saved["attempts"])
                 for phase in ("acquisition", "chain_readouts", "direct_baseline")]
        setup, chain, direct = spent
        first_exp = successful["matrix_exponentials"][0]["wall_seconds"]
        first_direct = sum(i["wall_seconds"] for i in successful["integrations"]
                           if i["quantity"].get("direct_sample") == ["0", 0])
        saved["costs"] = {
            "wall_seconds_by_phase_including_attempts": dict(zip(
                ("acquisition", "chain_readouts", "direct_baseline"), spent)),
            "successful_first_use_chain_acquisition_plus_exponential_seconds": (
                successful["phase_wall_seconds"]["acquisition"] + first_exp),
            "successful_first_use_direct_integral_calls_seconds": first_direct,
            "chain_setup_plus_nine_seconds_including_attempts": setup + chain,
            "chain_amortized_per_point_seconds_including_attempts": (setup + chain) / len(POINTS),
            "direct_nine_seconds_including_attempts": direct,
            "direct_amortized_per_point_seconds_including_attempts": direct / len(POINTS),
        }
    atomic_checkpoint(args.output, saved)
    print(f'{saved["outcome"]}: {args.output}', flush=True)
    return 0 if saved["outcome"] == "complete pass" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="New small JSON certificate path")
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output already exists; use a new path to preserve the saved record")
    args.output = args.output.resolve()
    sources = check_inputs()
    record = {
        "task": "TN6-E02", "request_revision": "r1", "date": "2026-11-14",
        "timezone": "America/New_York", "intended_author": "Edward Baker",
        "assistance": "OpenAI Codex LLM",
        "worker_dispatch": {"model": "gpt-6.1-sol", "effort": "ultra"},
        "independent_backend_or_effort_attestation": "unavailable",
        "input_hashes": {str(k.relative_to(ROOT)): v for k, v in INPUT_HASHES.items()},
        "all_manifest_sources_verified": sources,
        "script": {"path": str(Path(__file__).resolve().relative_to(ROOT)),
                   "sha256": sha256(Path(__file__).read_bytes())},
        "runtime": {"python": platform.python_version(), "python_executable": sys.executable,
                    "python_flint": flint.__version__, "flint": flint.__FLINT_VERSION__,
                    "system": platform.platform(), "threads": 1},
        "process_execution": {"started_utc": now_utc(), "implementation_correction_pass": 0},
        "parameters": {
            "sites": N, "cutoff_U": U, "mode_count_M": M,
            "panels": [[str(a), str(b)] for a, b in PANELS],
            "points": [[str(t), x] for t, x in POINTS],
            "precision_ladder_bits": PRECISIONS,
            "integration_limits": {"deg_limit": 64, "eval_limit": 8000, "depth_limit": 20},
            "source_limits": {"callbacks_per_attempt": ATTEMPT_CALLBACKS,
                              "callbacks_total": TOTAL_CALLBACKS},
            "wall_limits_seconds": {"total": TOTAL_SECONDS, "per_integral": INTEGRAL_SECONDS,
                                    "per_matrix_exponential": MATRIX_SECONDS},
            "normalized_caps": {name: str(value) for name, value in CAPS.items()},
        },
        "endpoint_format": "Exact rational strings. For each Arb, endpoints are its stored "
                           "dyadic midpoint plus/minus the stored outward magnitude radius. "
                           "Roundtrip checks parse every interval with Fraction and check "
                           "each repacked Arb contains the original.",
        "attempts": [],
        "outcome": "active",
    }
    return watchdog(args, record)


if __name__ == "__main__":
    sys.exit(main())
