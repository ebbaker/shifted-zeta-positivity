#!/usr/bin/env python3
"""Replay the frozen E04-r3 geometry and moment gates for Edward Baker."""

import argparse
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import platform
import signal
import sys
from time import perf_counter
from types import ModuleType

import flint
from flint import acb, arb, ctx, fmpq


N = 128
DEGREE = 32
BITS = 224
GEOMETRY_SCHEDULE = ((16, 64), (32, 128), (64, 256), (128, 512))
COORDINATE_CELLS = 512
RESOURCE_SECONDS = 60
SOURCE_SCRIPT_SHA256 = "549f3073e8783a10fba75ea160d67928f6fdcb9082d21e3e68500bf9a86138a2"


class ResourceLimit(Exception):
    pass


def load_verified_consumer():
    path = Path(__file__).resolve().with_name("vcd_gt_lehmer_certificate.py")
    source = path.read_bytes()
    if sha256(source).hexdigest() != SOURCE_SCRIPT_SHA256:
        raise RuntimeError("pinned E04-r2 consumer hash mismatch")
    # Execute the bytes whose hash was checked, rather than reopening the path.
    module = ModuleType("pinned_lehmer_certificate")
    module.__file__ = str(path)
    sys.modules[module.__name__] = module
    exec(compile(source, str(path), "exec"), module.__dict__)
    return module


def rational(numerator, denominator):
    return arb(fmpq(numerator, denominator))


def disk_error(sample_radius, radius):
    """Note14 §2 and E03 r5, for target radius 0 < radius < 5."""
    pi = arb.pi()
    alpha, beta = rational(9999, 10000), rational(131, 100)
    line_amplitude = (beta**2 / (4 * alpha)).exp() / alpha.sqrt()
    m5 = 2 * arb(10**16) * line_amplitude
    lattice = 4 * arb(10**13) * arb(4).exp() * line_amplitude / (16 * pi).expm1()
    tail = 2 * arb(10**13) * (-144 * alpha + 12 * beta).exp() / (
        pi.sqrt() * (24 * alpha - beta)
    )
    rho, enclosing_radius = rational(9, 10), arb(5)
    sample = (lattice + tail + sample_radius) * sum(
        (radius / rho)**n for n in range(DEGREE + 1)
    )
    alias_ratio = (rho / enclosing_radius)**N
    ratio = radius / enclosing_radius
    alias = m5 * alias_ratio / (1 - alias_ratio) * sum(
        ratio**n for n in range(DEGREE + 1)
    )
    spatial_tail = m5 * ratio**(DEGREE + 1) / (1 - ratio)
    time_tail = (
        m5 * factorial(66) * rational(1, 20)**33
        / (factorial(33) * 2**31 * (enclosing_radius - radius)**66)
    )
    total = (65 * (sample + alias + spatial_tail) + time_tail).upper()
    return total, {
        "radius": str(radius),
        "M5_upper": str(m5.upper()),
        "archive_sample_disk_radius_upper": str(sample_radius),
        "source_lattice_upper": str(lattice.upper()),
        "source_tail_upper": str(tail.upper()),
        "spatial_sample_propagation_upper_before_time_operator": str(sample.upper()),
        "spatial_alias_upper_before_time_operator": str(alias.upper()),
        "spatial_truncation_upper_before_time_operator": str(spatial_tail.upper()),
        "time_operator_norm_upper": 65,
        "time_interpolation_upper": str(time_tail.upper()),
        "total_uniform_disk_error_upper": str(total),
    }


def boundary_circles(field, outer, arcs):
    return [field.circle(rational(3, 4), arcs), field.circle(outer, arcs)]


def scan_boundaries(field, circles, cells, indices, stop_on_failure=True):
    """Real-part and modulus bounds for the whole closed cells and arcs."""
    half_width = rational(1, cells)
    pads = [
        field.radii_for_time_cell(circle, half_width, arb.pi() / circle.arcs)
        for circle in circles
    ]
    floors = [None, None]
    ceilings = [arb(0), arb(0)]
    failure = None
    for index in indices:
        midpoint = acb(rational(2 * index + 1 - cells, cells))
        for boundary, (circle, paddings) in enumerate(zip(circles, pads)):
            for arc, (node, padding) in enumerate(zip(circle.nodes, paddings)):
                value = node.time_polynomial(midpoint)
                lower = (value.real - padding).lower()
                if not lower > 0 and failure is None:
                    failure = {
                        "time_cell_zero_based": index,
                        "boundary_index_zero_based": boundary,
                        "angular_arc_zero_based": arc,
                        "real_part_lower": str(lower),
                    }
                    if stop_on_failure:
                        return None, failure
                floor = floors[boundary]
                floors[boundary] = lower if floor is None else min(lower, floor)
                ceilings[boundary] = max(ceilings[boundary], (abs(value) + padding).upper())
    return (floors, ceilings), failure


def certify_boundaries(field, outer, result):
    result["attempts"] = []
    result["radii"] = ["3/4", "8/5" if outer > rational(21, 20) else "21/20"]
    for cells, arcs in GEOMETRY_SCHEDULE:
        attempt = {"time_cells": cells, "arcs_per_boundary": arcs, "status": "running"}
        result["attempts"].append(attempt)
        started = perf_counter()
        circles = boundary_circles(field, outer, arcs)
        geometry, failure = scan_boundaries(field, circles, cells, range(cells))
        attempt.update({
            "seconds": perf_counter() - started,
            "status": "passed" if failure is None else "failed real-part allowance",
            "failure": failure,
        })
        if failure is None:
            floors, ceilings = geometry
            result.update({
                "success": True,
                "argument_principle_count_on_each_boundary": 2,
                "real_half_plane_lower_bounds": [str(floor) for floor in floors],
                "modulus_upper_bounds": [str(ceiling) for ceiling in ceilings],
            })
            return circles, geometry
    result["success"] = False
    result["failure"] = "real-part allowance exhausted the frozen geometry schedule"
    return None


def gap_moments(target, values, center, errors):
    """Note14 (9)–(10), with no evaluation of the drift kernel."""
    p1, p2 = arb(0), arb(0)
    last = len(target.nodes) - 1
    for index, (node, value) in enumerate(zip(target.nodes, values)):
        if not value.real > 0:
            raise RuntimeError(f"target arc {index} log ball reaches the nonpositive half-plane")
        log = value.log() - center
        weight = 1 if index in (0, last) else 2
        product = node.w * log
        p1 -= weight * product.real
        p2 -= 2 * weight * (node.w * product).real
    p1 = p1 / N + arb(0, errors[0])
    p2 = p2 / N + arb(0, errors[1])
    center_offset = p1 / 2
    return center_offset, p2 / 2 - center_offset**2


def cell_moments(target, pads, center, errors, index):
    midpoint = acb(rational(2 * index + 1 - COORDINATE_CELLS, COORDINATE_CELLS))
    values = [node.time_polynomial(midpoint) + pad for node, pad in zip(target.nodes, pads)]
    return gap_moments(target, values, center, errors)


def coordinate_test(consumer, field, boundaries, data, result, quadratic):
    target = field.circle(rational(9, 10), N)
    # The shared constructor and padding supply the original log moment
    # bounds. Its integrate/enclose methods would evaluate K, so use neither.
    collar = consumer.ContourCertificate(field, target, boundaries, data)
    result["collar"] = collar.geometry_record(data)
    pads = collar.padding(rational(1, COORDINATE_CELLS))
    lower = [None, None]
    upper = [None, None]
    started = perf_counter()
    for index in range(COORDINATE_CELLS):
        result["cells_attempted"] = index + 1
        try:
            c, d = cell_moments(target, pads, collar.center, collar.moment_errors, index)
        except RuntimeError as failure:
            result.update({"failure": str(failure), "failure_cell_zero_based": index})
            break
        if quadratic:
            # D(t)=2(t-1/20)=x/10, so the linear exact range is paid
            # by enclosing its two endpoints on every closed cell.
            left = rational(2 * index - COORDINATE_CELLS, 10 * COORDINATE_CELLS)
            right = rational(2 * index + 2 - COORDINATE_CELLS, 10 * COORDINATE_CELLS)
            if not (c.contains(0) and d.contains(left) and d.contains(right)):
                result.update({
                    "failure": "moment intervals failed to enclose exact quadratic coordinates",
                    "failure_cell_zero_based": index,
                    "computed_center_offset": str(c),
                    "computed_D": str(d),
                })
                break
        for j, value in enumerate((c, d)):
            lo, hi = value.lower(), value.upper()
            lower[j] = lo if lower[j] is None else min(lower[j], lo)
            upper[j] = hi if upper[j] is None else max(upper[j], hi)
        result["cells_completed"] = index + 1
    result["seconds"] = perf_counter() - started
    if lower[0] is not None:
        center_abs = max(-lower[0], upper[0])
        d_abs = max(-lower[1], upper[1])
        result.update({
            "center_offset_lower": str(lower[0]),
            "center_offset_upper": str(upper[0]),
            "center_offset_abs_upper": str(center_abs),
            "D_lower": str(lower[1]),
            "D_upper": str(upper[1]),
            "D_abs_upper": str(d_abs),
            "center_abs_gate": bool(center_abs <= rational(7, 100)),
            "D_abs_gate": bool(d_abs <= rational(1, 5)),
        })
    if "failure" not in result and not (result["center_abs_gate"] and result["D_abs_gate"]):
        result["failure"] = "coordinate magnitude limit failed on the fixed 512 cells"
    result["success"] = "failure" not in result


def benchmark(consumer, wide, narrow, started):
    setup_times = []
    geometry_times = []
    cells, arcs = GEOMETRY_SCHEDULE[0]
    for field, radius in ((wide, rational(8, 5)), (narrow, rational(21, 20))):
        start = perf_counter()
        circles = boundary_circles(field, radius, arcs)
        setup_times.append(perf_counter() - start)
        start = perf_counter()
        scan_boundaries(field, circles, cells, [0], stop_on_failure=False)
        geometry_times.append(perf_counter() - start)
    start = perf_counter()
    target = narrow.circle(rational(9, 10), N)
    target_setup = perf_counter() - start
    start = perf_counter()
    pad = [consumer.rectangle(radius) for radius in narrow.radii_for_time_cell(
        target, rational(1, COORDINATE_CELLS), arb(0)
    )]
    for index in (0, 127, 255, 511):
        # These are timing-only moments with dummy centering and tails.
        # Production coordinates use freshly proved, full-slab collar data.
        cell_moments(target, pad, arb(0), (arb(0), arb(0)), index)
    coordinate_seconds = perf_counter() - start
    base_nodes = arcs // 2 + 1
    setup_scale = sum(arcs // 2 + 1 for _, arcs in GEOMETRY_SCHEDULE) / base_nodes
    scan_scale = sum(cells * (arcs // 2 + 1) for cells, arcs in GEOMETRY_SCHEDULE) / base_nodes
    # Both fields and both radius pairs are included even if an earlier
    # schedule passes. The independent wall clock enforces the actual cap.
    projected = perf_counter() - started + 2 * (
        setup_scale * sum(setup_times) + scan_scale * sum(geometry_times)
        + target_setup + COORDINATE_CELLS * coordinate_seconds / 4
    )
    return {
        "geometry_cells_tested": 2,
        "coordinate_cells_tested": 4,
        "geometry_setup_seconds_each_radius_pair": setup_times,
        "geometry_sample_seconds_each_radius_pair": geometry_times,
        "coordinate_circle_setup_seconds": target_setup,
        "coordinate_seconds": coordinate_seconds,
        "projection_seconds_at_cap": projected,
        "resource_gate": projected < RESOURCE_SECONDS,
    }


def field_test(consumer, wide, narrow, result, quadratic=False):
    result["fixed_sign"] = wide.sign
    if wide.sign != narrow.sign:
        raise RuntimeError("wide and narrow fields selected inconsistent signs")
    auxiliary = result["auxiliary_geometry"] = {}
    certify_boundaries(wide, rational(8, 5), auxiliary)
    collar = result["original_collar"] = {}
    coordinate_data = certify_boundaries(narrow, rational(21, 20), collar)
    coordinates = result["coordinates"] = {"cells_attempted": 0, "cells_completed": 0}
    if coordinate_data is None:
        coordinates.update({"success": False, "failure": "original collar gate failed"})
    else:
        boundaries, geometry = coordinate_data
        coordinate_test(consumer, narrow, boundaries, geometry, coordinates, quadratic)
    result["success"] = auxiliary["success"] and collar["success"] and coordinates["success"]


def resource_expired(_signal, _frame):
    raise ResourceLimit("60-second wall clock resource gate expired")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = BITS
    started = perf_counter()
    record = {
        "request": "VCD-GT-E04-r3",
        "date": "2026-11-16 America/New_York",
        "prepared_for": "Edward Baker",
        "llm_assistance": "Codex, explicit gpt-6.1-sol/ultra dispatch; no backend attestation",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "required_source_consumer_sha256": SOURCE_SCRIPT_SHA256,
        "versions": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "python_flint": flint.__version__,
            "flint": flint.__FLINT_VERSION__,
        },
        "precision": BITS,
        "spatial_and_time_degree": DEGREE,
        "circle_nodes": N,
        "geometry_schedule": GEOMETRY_SCHEDULE,
        "coordinate_cells": COORDINATE_CELLS,
        "resource_cap_seconds": RESOURCE_SECONDS,
        "canonical_xi_calls": 0,
        "drift_kernel_calls": 0,
        "early_gap_positivity_input": False,
    }
    signal.signal(signal.SIGALRM, resource_expired)
    signal.setitimer(signal.ITIMER_REAL, RESOURCE_SECONDS)
    try:
        record["stage"] = "verified consumer and source archive"
        consumer = load_verified_consumer()
        record["archive"] = {
            "name": consumer.ARCHIVE,
            "gzip_sha256": consumer.STORED_SHA256,
            "content_sha256": consumer.CONTENT_SHA256,
        }
        samples = consumer.archived_fields(args.cache_dir)
        record["archive"]["hashes_verified"] = True
        record["stage"] = "tensor and disk allowances"
        coefficients, sample_radius = consumer.tensor_coefficients(samples)
        wide_error, record["auxiliary_disk_error"] = disk_error(sample_radius, rational(8, 5))
        narrow_error, _, record["original_disk_error"] = consumer.tensor_error(sample_radius)
        wide = consumer.FieldPolynomial(coefficients, wide_error)
        narrow = consumer.FieldPolynomial(coefficients, narrow_error)
        record["tensor_setup_seconds"] = perf_counter() - started
        record["stage"] = "preflight"
        record["preflight"] = benchmark(consumer, wide, narrow, started)
        if not record["preflight"]["resource_gate"]:
            raise RuntimeError("preflight resource projection reached the 60-second cap")
        record["stage"] = "canonical geometry and moments"
        field_test(consumer, wide, narrow, record.setdefault("canonical", {}))
        record["stage"] = "quadratic control"
        quadratic = consumer.FieldPolynomial(consumer.quadratic_coefficients(), arb(0))
        control = record.setdefault("quadratic_control", {})
        field_test(consumer, quadratic, quadratic, control, quadratic=True)
        control["analytic_signed_budget_upper_margin"] = "-1/10"
        record["success"] = record["canonical"]["success"] and control["success"]
        record["stage"] = "complete"
    except (OSError, ResourceLimit, RuntimeError) as failure:
        record["success"] = False
        record["failure"] = str(failure)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    record["total_seconds"] = perf_counter() - started
    record["status"] = "geometry acquired pending internal review" if record["success"] else "failed gate"
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(record["status"], record.get("failure", ""), flush=True)
    return 0 if record["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
