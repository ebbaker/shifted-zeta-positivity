#!/usr/bin/env python3
"""Replay the fixed E04-r2 contour and uniform-time enclosure for Edward Baker."""

import argparse
from dataclasses import dataclass
import gzip
from hashlib import sha256
import json
from math import factorial
import os
from pathlib import Path
import platform
from time import perf_counter

import flint
from flint import acb, acb_poly, arb, ctx, fmpq


N = 128
DEGREE = 32
BITS = 224
GEOMETRY_SCHEDULE = ((16, 64), (32, 128), (64, 256), (128, 512), (256, 512))
TIME_SCHEDULE = (512, 1024, 2048, 4096, 8192)
ARCHIVE = "E04-r1-fine-fields.json.gz"
STORED_SHA256 = "033f83cb4a8d6bd411e4861380a78e054ab70f7c60079b98a75bd159644a078a"
CONTENT_SHA256 = "508d0feec6655524f1927d5b2877b1171c92a5a553053b7ef428fc680eb6f816"


class GateFailure(RuntimeError):
    pass


def ball(value):
    return str(value)


def abs_upper(value):
    return abs(value).upper()


def fixed_q(numerator, denominator):
    return arb(fmpq(numerator, denominator))


def exp_pi_i(numerator, denominator):
    angle = fmpq(numerator, denominator)
    return acb(arb.cos_pi_fmpq(angle), arb.sin_pi_fmpq(angle))


def archived_fields(cache_dir):
    relative = Path("numerics-archives") / ARCHIVE
    normal = Path(__file__).resolve().parents[1] / relative
    if cache_dir:
        path = cache_dir / ARCHIVE
    elif normal.is_file():
        path = normal
    elif location := os.getenv("VCD_GT_ARCHIVES"):
        path = Path(location) / relative
    else:
        path = normal
    if not path.is_file():
        raise GateFailure(f"missing archive {path}; regenerate via the fixed E04-r1 script")
    stored = path.read_bytes()
    if sha256(stored).hexdigest() != STORED_SHA256:
        raise GateFailure("fine gzip archive hash mismatch")
    payload = gzip.decompress(stored)
    if sha256(payload).hexdigest() != CONTENT_SHA256:
        raise GateFailure("fine canonical content hash mismatch")
    decoded = json.loads(payload)
    expected_level = {"name": "fine", "bits": BITS, "lattice_denominator": 4,
                      "circle_count": N, "time_count": DEGREE}
    if decoded["level"] != expected_level:
        raise GateFailure("unexpected archive grid metadata")
    fields = decoded["field_values"]
    if len(fields) != DEGREE + 1 or any(len(row) != N for row in fields):
        raise GateFailure("unexpected archive array shape")
    return fields


def midpoint_and_radius(parts):
    midpoints = []
    radii = []
    for midpoint, radius, exponent in parts:
        unit = arb(10) ** exponent
        midpoints.append(midpoint * unit)
        radii.append(radius * unit)
    return acb(*midpoints), (radii[0]**2 + radii[1]**2).sqrt().upper()


def tensor_coefficients(samples):
    """Coefficients A[n][k] of w**n T_k(x), x = 20*t-1."""
    rho = fixed_q(9, 10)
    polar = [exp_pi_i(-2 * j, N) for j in range(N)]
    powers = [[unit**n for unit in polar] for n in range(DEGREE + 1)]
    by_time = []
    radii = []
    for row in samples:
        values_and_radii = [midpoint_and_radius(parts) for parts in row]
        values = [item[0] for item in values_and_radii]
        radii.extend(item[1] for item in values_and_radii)
        by_time.append([
            sum(value * factor for value, factor in zip(values, powers[n])) / (N * rho**n)
            for n in range(DEGREE + 1)
        ])
    half = fixed_q(1, 2)
    endpoints = [half] + [arb(1)] * (DEGREE - 1) + [half]
    cosine = [[arb.cos_pi_fmpq(fmpq((DEGREE - j) * k, DEGREE)) for j in range(DEGREE + 1)]
              for k in range(DEGREE + 1)]
    coefficients = []
    for n in range(DEGREE + 1):
        weighted_samples = [endpoints[j] * by_time[j][n] for j in range(DEGREE + 1)]
        coefficients.append([
            2 * endpoints[k] * sum(c * value for c, value in zip(cosine[k], weighted_samples)) / DEGREE
            for k in range(DEGREE + 1)
        ])
    return coefficients, max(radii)


def tensor_error(sample_radius):
    pi = arb.pi()
    alpha, beta = fixed_q(9999, 10000), fixed_q(131, 100)
    c2, c5 = arb(10**13), arb(10**16)
    r, outer, major_radius = fixed_q(9, 10), fixed_q(21, 20), arb(5)
    line_amplitude = (beta**2 / (4 * alpha)).exp() / alpha.sqrt()
    m5 = 2 * c5 * line_amplitude
    lattice = 4 * c2 * arb(4).exp() * line_amplitude / (16 * pi).expm1()
    tail = 2 * c2 * (-144 * alpha + 12 * beta).exp() / (pi.sqrt() * (24 * alpha - beta))
    sample = (lattice + tail + sample_radius) * sum((outer / r)**n for n in range(DEGREE + 1))
    alias_ratio = (r / major_radius)**N
    alias = m5 * alias_ratio / (1 - alias_ratio) * sum((outer / major_radius)**n for n in range(DEGREE + 1))
    tail_ratio = outer / major_radius
    spatial_tail = m5 * tail_ratio**(DEGREE + 1) / (1 - tail_ratio)
    time_tail = (m5 * factorial(66) * fixed_q(1, 20)**33
                 / (factorial(33) * 2**31 * (major_radius - outer)**66))
    uniform = 65 * (sample + alias + spatial_tail) + time_tail
    return uniform.upper(), (lattice + tail).upper(), {
        "M5_upper": ball(m5.upper()),
        "archive_sample_disk_radius_upper": ball(sample_radius),
        "source_lattice_upper": ball(lattice.upper()),
        "source_tail_upper": ball(tail.upper()),
        "spatial_sample_propagation_upper_before_time_operator": ball(sample.upper()),
        "spatial_alias_upper_before_time_operator": ball(alias.upper()),
        "spatial_truncation_upper_before_time_operator": ball(spatial_tail.upper()),
        "time_operator_norm_upper": 65,
        "time_interpolation_upper": ball(time_tail.upper()),
        "total_uniform_disk_error_upper": ball(uniform.upper()),
    }


def quadratic_coefficients():
    coefficients = [[acb(0) for _ in range(DEGREE + 1)] for _ in range(DEGREE + 1)]
    coefficients[0][1] = acb(-fixed_q(1, 10))
    coefficients[2][0] = acb(1)
    return coefficients


def chebyshev_polynomials():
    x = acb_poly([0, 1])
    basis = [acb_poly([1]), x]
    for _ in range(2, DEGREE + 1):
        basis.append(2 * x * basis[-1] - basis[-2])
    return basis


@dataclass
class AngularNode:
    w: acb
    time_polynomial: acb_poly
    time_derivative_upper: arb


@dataclass
class Circle:
    radius: arb
    arcs: int
    nodes: list
    angle_derivative_upper: arb


class FieldPolynomial:
    def __init__(self, coefficients, error):
        self.coefficients = coefficients
        self.error = error
        self.basis = chebyshev_polynomials()
        self.sign = 1
        radius = fixed_q(9, 10)
        right_value = sum(radius**(n - 2) * sum((-1)**k * value for k, value in enumerate(row))
                          for n, row in enumerate(coefficients))
        if right_value.real < 0:
            self.sign = -1
        elif not right_value.real > 0:
            raise GateFailure("ambiguous real reference sign")

    def circle(self, radius, count):
        by_radius = [[value * radius**(n - 2) for value in row]
                     for n, row in enumerate(self.coefficients)]
        angle_derivative = sum(abs(n - 2) * sum(abs_upper(value) for value in row)
                               for n, row in enumerate(by_radius)).upper()
        nodes = []
        # The real polynomial is not needed for conjugation reduction. The
        # complete field has real coefficients, so its reflected cells follow.
        for j in range(count // 2 + 1):
            unit = exp_pi_i(2 * j, count)
            phases = [unit**(n - 2) for n in range(DEGREE + 1)]
            coefficients = [self.sign * sum(row[k] * phase for row, phase in zip(by_radius, phases))
                            for k in range(DEGREE + 1)]
            time_derivative = sum(k**2 * abs_upper(value) for k, value in enumerate(coefficients)).upper()
            polynomial = sum((coefficient * basis for coefficient, basis in zip(coefficients, self.basis)),
                             acb_poly())
            nodes.append(AngularNode(radius * unit, polynomial, time_derivative))
        return Circle(radius, count, nodes, angle_derivative)

    def radii_for_time_cell(self, circle, half_width, angle_half_width):
        common = self.error / circle.radius**2 + angle_half_width * circle.angle_derivative_upper
        return [(common + half_width * node.time_derivative_upper).upper() for node in circle.nodes]


def rectangle(radius):
    return acb(arb(0, radius), arb(0, radius))


def geometry_pass(field, circles, cells):
    half_width = fixed_q(1, cells)
    boundary_radii = [field.radii_for_time_cell(circle, half_width, arb.pi() / circle.arcs)
                      for circle in circles]
    floors = [None, None]
    ceilings = [arb(0), arb(0)]
    for i in range(cells):
        mid = acb(fixed_q(2 * i + 1 - cells, cells))
        for j, (circle, paddings) in enumerate(zip(circles, boundary_radii)):
            for node, padding in zip(circle.nodes, paddings):
                value = node.time_polynomial(mid)
                real_lower = (value.real - padding).lower()
                if not real_lower > 0:
                    return None, {"time_cell": i, "boundary": j, "real_lower": ball(real_lower)}
                floors[j] = real_lower if floors[j] is None else min(floors[j], real_lower)
                ceilings[j] = max(ceilings[j], (abs(value) + padding).upper())
    return (floors, ceilings), None


def certify_geometry(field):
    attempts = []
    boundaries = None
    for cells, arcs in GEOMETRY_SCHEDULE:
        start = perf_counter()
        if boundaries is None or boundaries[0].arcs != arcs:
            boundaries = [field.circle(fixed_q(3, 4), arcs), field.circle(fixed_q(21, 20), arcs)]
        data, failure = geometry_pass(field, boundaries, cells)
        attempts.append({"cells": cells, "arcs_per_boundary": arcs, "failure": failure,
                         "seconds": perf_counter() - start})
        if failure is None:
            return boundaries, data, attempts
    raise GateFailure(f"collar real-part test exhausted its cap: {attempts}")


class ContourCertificate:
    def __init__(self, field, target, boundaries, geometry):
        self.target = target
        self.field = field
        self.boundaries = boundaries
        floors, ceilings = geometry
        self.center = ((min(floors).log() + max(ceilings).log()) / 2).mid()
        pi = arb.pi()
        self.log_bounds = [
            (max(abs_upper(floor.log() - self.center), abs_upper(ceiling.log() - self.center))**2
             + (pi / 2)**2).sqrt().upper()
            for floor, ceiling in zip(floors, ceilings)
        ]
        ratios = [(boundaries[0].radius / target.radius)**N, (target.radius / boundaries[1].radius)**N]
        self.tail_weights = [(ratio / (1 - ratio)).upper() for ratio in ratios]
        self.moment_errors = [self.mean_error([k * circle.radius**k * log_bound
                                             for circle, log_bound in zip(boundaries, self.log_bounds)])
                              for k in (1, 2)]

    def mean_error(self, boundary_bounds):
        return sum(b * w for b, w in zip(boundary_bounds, self.tail_weights)).upper()

    def padding(self, half_width):
        return [rectangle(radius) for radius in self.field.radii_for_time_cell(self.target, half_width, arb(0))]

    def enclose(self, x_midpoint, pads):
        x = acb(x_midpoint)
        return self.integrate([node.time_polynomial(x) + pad for node, pad in zip(self.target.nodes, pads)])

    def archived_endpoint(self, row, source_error):
        values = []
        for node, parts in zip(self.target.nodes, row):
            midpoint, stored_radius = midpoint_and_radius(parts)
            scaled_error = ((source_error + stored_radius) / self.target.radius**2).upper()
            values.append(self.field.sign * midpoint / node.w**2 + rectangle(scaled_error))
        return self.integrate(values)

    def integrate(self, values):
        sums = [arb(0), arb(0)]
        logs = []
        last = len(self.target.nodes) - 1
        for j, (node, value) in enumerate(zip(self.target.nodes, values)):
            if not value.real > 0:
                raise GateFailure("target node log ball reaches the nonpositive half-plane")
            log = value.log() - self.center
            weight = 1 if j in (0, last) else 2
            logs.append(log)
            product = node.w * log
            sums[0] -= weight * product.real
            sums[1] -= (2 * weight) * (node.w * product).real
        p1, p2 = [mean / N + arb(0, err) for mean, err in zip(sums, self.moment_errors)]
        c = p1 / 2
        d = p2 / 2 - c**2
        c_bound, d_bound = abs_upper(c), abs_upper(d)
        kernel_bounds = []
        q_lower_bounds = []
        for circle, log_bound in zip(self.boundaries, self.log_bounds):
            radius = circle.radius
            if not c_bound < radius:
                raise GateFailure("center bound reaches collar boundary")
            q_lower = ((radius - c_bound)**2 - d_bound).lower()
            if not q_lower > 0:
                raise GateFailure("coordinate enclosure cannot lower bound collar Q")
            q_lower_bounds.append(q_lower)
            kernel_bounds.append(2 * radius * (radius + c_bound) * log_bound / q_lower**2)
        k_error = self.mean_error(kernel_bounds)
        total = arb(0)
        for j, (node, log) in enumerate(zip(self.target.nodes, logs)):
            offset = node.w - c
            q = offset**2 - d
            if q.contains(0):
                raise GateFailure("interval kernel denominator contains zero at target node")
            weight = 1 if j in (0, last) else 2
            total += (2 * weight) * (node.w * offset * log / q**2).real
        k = total / N + arb(0, k_error)
        return c, d, k, q_lower_bounds, k_error

    def geometry_record(self, data):
        floors, ceilings = data
        return {
            "real_half_plane_lower_bounds": [ball(x) for x in floors],
            "modulus_upper_bounds": [ball(x) for x in ceilings],
            "log_center": ball(self.center),
            "centered_log_upper_bounds": [ball(x) for x in self.log_bounds],
            "p1_p2_annular_error_upper_bounds": [ball(x) for x in self.moment_errors],
        }


def cell_summary(certificate, count):
    start = perf_counter()
    pads = certificate.padding(fixed_q(1, count))
    aggregate_lower = None
    aggregate_upper = None
    q_floors = None
    max_error = arb(0)
    for i in range(count):
        midpoint = fixed_q(2 * i + 1 - count, count)
        try:
            _, _, k, q_bounds, error = certificate.enclose(midpoint, pads)
        except GateFailure as exc:
            return None, {"cells_attempted": i + 1, "failure": str(exc), "seconds": perf_counter() - start}
        aggregate_lower = k.lower() if aggregate_lower is None else min(aggregate_lower, k.lower())
        aggregate_upper = k.upper() if aggregate_upper is None else max(aggregate_upper, k.upper())
        q_floors = q_bounds if q_floors is None else [min(a, b) for a, b in zip(q_floors, q_bounds)]
        max_error = max(max_error, error)
    return (aggregate_lower, aggregate_upper), {
        "cells_attempted": count,
        "K_lower": ball(aggregate_lower), "K_upper": ball(aggregate_upper),
        "Q_collar_lower_bounds": [ball(floor) for floor in q_floors],
        "K_annular_error_upper": ball(max_error),
        "seconds": perf_counter() - start,
    }


def time_cost(k):
    if k.is_zero():
        return fixed_q(1, 5)
    return (fixed_q(2, 5) * k).expm1() / (2 * k)


def point_record(result):
    center, gap, curvature, q_floors, tail = result
    return {"center_offset": ball(center), "D": ball(gap), "D_lower": ball(gap.lower()),
            "D_upper": ball(gap.upper()), "K": ball(curvature),
            "Q_collar_lower_bounds": [ball(q) for q in q_floors], "K_annular_error_upper": ball(tail)}


def endpoint_certificate(cert, geometry, attempts):
    pad = cert.padding(arb(0))
    zero = cert.enclose(arb(-1), pad)
    terminal = cert.enclose(arb(1), pad)
    return zero, terminal, {
        "geometry_attempts": attempts,
        "geometry": cert.geometry_record(geometry),
        "argument_principle_count_on_each_boundary": 2,
        "D_0_direct": point_record(zero),
        "D_v_incoming": point_record(terminal),
    }


def canonical_certificate(cert, geometry, attempts, samples, source_error):
    _, _, result = endpoint_certificate(cert, geometry, attempts)
    zero = cert.archived_endpoint(samples[0], arb(0))
    terminal = cert.archived_endpoint(samples[-1], source_error)
    result["tensor_D_0"] = result["D_0_direct"]
    result["tensor_D_v"] = result["D_v_incoming"]
    result["D_0_direct"] = point_record(zero)
    result["D_v_incoming"] = point_record(terminal)
    result["incoming_and_direct_source"] = "archived contour endpoint rows with their own source allowances"
    result["time_attempts"] = []
    for count in TIME_SCHEDULE:
        k_range, summary = cell_summary(cert, count)
        result["time_attempts"].append(summary)
        if k_range is None:
            continue
        _, upper = k_range
        target_preferred = fixed_q(-59, 100)
        if upper <= target_preferred:
            k_upper = target_preferred
        elif upper <= fixed_q(-58, 100):
            k_upper = upper
        else:
            continue
        cost = time_cost(k_upper)
        weight = (fixed_q(2, 5) * k_upper).exp()
        margin = (terminal[1].lower() - cost.upper()).lower()
        if not margin > 0:
            continue
        transported_lower = (margin / weight.upper()).lower()
        abs_margin_upper = (terminal[1].upper() - fixed_q(1, 5)).upper()
        result["comparison"] = {
            "used_K_upper": ball(k_upper),
            "B_signed_upper": ball(cost.upper()),
            "W_signed_upper": ball(weight.upper()),
            "signed_margin_lower": ball(margin),
            "D_0_transported_lower": ball(transported_lower),
            "D_0_direct_positive": bool(zero[1] > 0),
            "absolute_margin_upper": ball(abs_margin_upper),
            "absolute_test_fails": bool(abs_margin_upper < 0),
        }
        result["success"] = bool(zero[1] > 0 and abs_margin_upper < 0)
        return result
    result["success"] = False
    result["failure"] = "uniform K/time margin gate exhausted the fixed cell cap"
    return result


def control_certificate():
    field = FieldPolynomial(quadratic_coefficients(), arb(0))
    geometry_circles, geometry, attempts = certify_geometry(field)
    cert = ContourCertificate(field, field.circle(fixed_q(9, 10), N), geometry_circles, geometry)
    zero, terminal, result = endpoint_certificate(cert, geometry, attempts)
    k_range, summary = cell_summary(cert, TIME_SCHEDULE[0])
    result["time_attempt"] = summary
    if k_range is None:
        result["success"] = False
        return result
    k_lower, k_upper = k_range
    cost = time_cost(k_lower).union(time_cost(k_upper))
    worst_margin = (terminal[1].upper() - time_cost(k_lower).lower()).upper()
    gap_double = cert.enclose(arb(0), cert.padding(arb(0)))[1]
    result.update({"B": ball(cost), "signed_margin_upper": ball(worst_margin), "D_at_double": ball(gap_double)})
    result["success"] = bool(k_lower <= 0 <= k_upper and terminal[1].contains(fixed_q(1, 10))
                             and zero[1].contains(fixed_q(-1, 10)) and gap_double.contains(0)
                             and cost.contains(fixed_q(1, 5)) and worst_margin < 0)
    return result


def benchmark(certificate):
    start = perf_counter()
    count = TIME_SCHEDULE[0]
    pads = certificate.padding(fixed_q(1, count))
    for i in (0, 3, 127, 255, 384, 511):
        certificate.enclose(fixed_q(2 * i + 1 - count, count), pads)
    seconds = perf_counter() - start
    estimate = seconds * (sum(TIME_SCHEDULE) + TIME_SCHEDULE[0]) / 6
    return {"tested_cells": 6, "seconds": seconds, "projection_seconds_at_cap": estimate,
            "resource_gate": estimate < 1200}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = BITS
    started = perf_counter()
    record = {
        "request": "VCD-GT-E04-r2",
        "date": "2026-11-16 America/New_York",
        "prepared_for": "Edward Baker",
        "llm_assistance": "Codex, explicit gpt-6.1-sol/ultra dispatch; no backend attestation",
        "status": "started",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "versions": {"python": platform.python_version(), "platform": platform.platform(),
                     "python_flint": flint.__version__, "flint": flint.__FLINT_VERSION__},
        "archive": {"name": ARCHIVE, "gzip_sha256": STORED_SHA256, "content_sha256": CONTENT_SHA256},
        "precision": BITS, "spatial_and_time_degree": DEGREE, "circle_nodes": N,
        "canonical_xi_calls": 0, "geometry_caps": GEOMETRY_SCHEDULE[-1], "time_cell_cap": TIME_SCHEDULE[-1],
    }
    try:
        samples = archived_fields(args.cache_dir)
        coefficients, archive_error = tensor_coefficients(samples)
        error, source_error, record["tensor_error"] = tensor_error(archive_error)
        field = FieldPolynomial(coefficients, error)
        record["fixed_sign"] = field.sign
        record["tensor_setup_seconds"] = perf_counter() - started
        target = field.circle(fixed_q(9, 10), N)
        circles, geometry, attempts = certify_geometry(field)
        cert = ContourCertificate(field, target, circles, geometry)
        record["preflight"] = benchmark(cert)
        print(json.dumps({"geometry": attempts, "preflight": record["preflight"]}), flush=True)
        if not record["preflight"]["resource_gate"]:
            raise GateFailure("preflight resource projection exceeds 20 minutes")
        record["canonical"] = canonical_certificate(cert, geometry, attempts, samples, source_error)
        record["quadratic_control"] = control_certificate()
        record["success"] = record["canonical"]["success"] and record["quadratic_control"]["success"]
        record["status"] = "complete enclosure pending separate internal review" if record["success"] else "failed gate"
    except GateFailure as exc:
        record["status"] = "failed gate"
        record["success"] = False
        record["failure"] = str(exc)
    record["total_seconds"] = perf_counter() - started
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(record["status"], record.get("failure", ""), flush=True)
    return 0 if record["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
