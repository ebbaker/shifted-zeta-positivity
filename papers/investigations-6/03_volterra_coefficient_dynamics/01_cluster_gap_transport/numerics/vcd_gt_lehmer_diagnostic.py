#!/usr/bin/env python3
"""VCD-GT-E04-r1, 16 November 2026, for Edward Baker with Codex assistance.

Run with python-flint 0.9.0. The two prescribed levels run in order.
Arb bounds finite arithmetic. E08 source padding does not pay for the
spatial contour or time quadratures.
"""

import argparse
from dataclasses import dataclass
import gzip
from hashlib import sha256
import json
from math import inf, nextafter
from pathlib import Path
import platform
from time import perf_counter

import flint
from flint import acb, arb, ctx


@dataclass(frozen=True)
class Level:
    name: str
    bits: int
    lattice_denominator: int
    circle_count: int
    time_count: int


LEVELS = (Level("coarse", 160, 3, 64, 16), Level("fine", 224, 4, 128, 32))


def midpoint(value):
    return float(value.mid())


def upper(value):
    return nextafter(float(value.upper()), inf)


def lower(value):
    return nextafter(float(value.lower()), -inf)


def ball_record(value):
    return {"midpoint": midpoint(value), "radius_upper": upper(value.rad())}


def theta_nodes(count, rho, pi):
    upper_half = [rho * acb(0, 2 * pi * j / count).exp() for j in range(count // 2 + 1)]
    upper_half[0] = acb(rho)
    upper_half[-1] = acb(-rho)
    return upper_half + [point.conjugate() for point in reversed(upper_half[1:-1])]


class XiSource:
    def __init__(self, pi, a, circle, lattice_denominator):
        self.pi = pi
        self.log_pi = pi.log()
        self.log_gauge = pi * a / 8
        self.a = a
        self.circle = circle
        self.denominator = lattice_denominator
        self.limit = 12 * lattice_denominator
        self.h = arb(1) / lattice_denominator
        self.prefactor = self.h / pi.sqrt()
        self.r_values = [self.h * k for k in range(self.limit + 1)]
        self.weights = [(-r * r).exp() for r in self.r_values]
        self.at_t0 = []
        self.xi_calls = 0
        self.xi_seconds = 0.0

    def source_error(self):
        # E08 majorant, for |z-a| <= 2 and 0 <= t <= 1/10.
        constant = arb(10**13)
        alpha = arb(9999) / 10000
        beta = arb(131) / 100
        line_mass = 2 * constant * (self.pi / alpha).sqrt() * (4 + beta**2 / (4 * alpha)).exp()
        lattice = 2 * line_mass / (self.pi.sqrt() * (4 * self.pi / self.h).expm1())
        tail = 2 * constant * (-144 * alpha + 12 * beta).exp() / (self.pi.sqrt() * (24 * alpha - beta))
        return lattice, tail

    def xi(self, w, shift):
        start = perf_counter()
        s = acb((1 - w.imag - shift) / 2, (self.a + w.real) / 2)
        # Evaluate one stable log-gamma exponent, including the fixed gauge.
        value = (self.log_gauge + (s / 2).lgamma() - s * self.log_pi / 2).exp()
        value *= s * (s - 1) * s.zeta() / 16
        self.xi_calls += 1
        self.xi_seconds += perf_counter() - start
        if not value.is_finite():
            raise GateFailure("source returned a nonfinite xi ball")
        return value

    def contour(self, time_index, t):
        half = len(self.circle) // 2
        if time_index == 0:
            self.at_t0 = [self.xi(w, 0) for w in self.circle[:half + 1]]
            values = self.at_t0[:]
        else:
            scale = 2 * t.sqrt()
            shifts = [scale * r for r in self.r_values]
            values = []
            for j, w in enumerate(self.circle[:half + 1]):
                value = self.at_t0[j]
                for k in range(1, self.limit + 1):
                    positive = self.xi(w, shifts[k])
                    if j in (0, half):
                        # At a real point the opposite lattice term is its conjugate.
                        pair = 2 * positive.real
                    else:
                        pair = positive + self.xi(w, -shifts[k])
                    value += self.weights[k] * pair
                values.append(self.prefactor * value)
        values[0] = acb(values[0].real)
        values[-1] = acb(values[-1].real)
        return values + [value.conjugate() for value in reversed(values[1:-1])]


class GateFailure(RuntimeError):
    pass


def contour_log(values, pi):
    """Anchor the finite polygon log at its first node and track its winding."""
    ratios = [values[(j + 1) % len(values)] / value for j, value in enumerate(values)]
    increments = [ratio.arg() for ratio in ratios]
    phase_max = max(increments, key=lambda value: upper(abs(value)))
    if not abs(phase_max) < pi / 2:
        raise GateFailure("sampled phase increment is not bounded by pi/2")
    winding_ball = sum(increments) / (2 * pi)
    winding = round(midpoint(winding_ball))
    if not abs(winding_ball - winding) < arb(1) / 4:
        raise GateFailure("sampled winding has no unique integer")
    # Each principal ratio argument is bounded away from its negative-real cut.
    # On the resulting polygon these increments define the unwrapped log.
    log_values = [acb(0)]
    phase = arb(0)
    for value, increment in zip(values[1:], increments):
        phase += increment
        log_values.append(acb(abs(value / values[0]).log(), phase))
    return log_values, winding, upper(abs(phase_max))


def pair_moments(log_values, circle, rho):
    n = len(circle)
    p1 = -sum(w * log for w, log in zip(circle, log_values)) / n
    p2 = -2 * sum(w**2 * log for w, log in zip(circle, log_values)) / n
    center_offset = p1 / 2
    gap = p2 / 2 - center_offset**2
    # An unordered-pair buffer lower estimate for these finite-rule coordinates.
    buffer = rho - abs(center_offset) - abs(gap).sqrt()
    if not buffer > 0:
        raise GateFailure("sampled moment reconstruction has no positive pair buffer")
    terms = []
    for w, log in zip(circle, log_values):
        offset = w - center_offset
        quadratic = offset**2 - gap
        if quadratic.contains(0):
            raise GateFailure("sampled rational K denominator may vanish")
        terms.append(2 * w * offset * log / quadratic**2)
    curvature = sum(terms) / n
    return center_offset, gap, curvature, buffer


def contour_row(values, circle, rho, pi, source_error):
    min_modulus = min(abs(value).lower() for value in values)
    if not min_modulus > 10 * source_error:
        raise GateFailure("source allowance exceeds one tenth of the sampled modulus floor")
    _, winding, max_field_step = contour_log(values, pi)
    if winding != 2:
        raise GateFailure(f"sampled field winding is {winding}, expected 2")
    normalized = [value / w**2 for value, w in zip(values, circle)]
    logs, log_winding, max_log_step = contour_log(normalized, pi)
    if log_winding != 0:
        raise GateFailure(f"sampled normalized winding is {log_winding}, expected 0")
    center, gap, curvature, buffer = pair_moments(logs, circle, rho)
    modulus_ratio = source_error / min_modulus
    ell = -(1 - modulus_ratio).log()
    # A disk perturbation relative to the approximate field pays ell at each
    # node. Anchoring subtracts another such perturbation at node zero.
    if not arb(max(max_field_step, max_log_step)) + 2 * ell < pi / 2:
        raise GateFailure("source padding cannot preserve the sampled phase separation")
    component_radius = (2 * ell).upper()
    padding = acb(arb(0, component_radius), arb(0, component_radius))
    padded_logs = [logs[0], *(log + padding for log in logs[1:])]
    _, gap_padded, curvature_padded, buffer_padded = pair_moments(padded_logs, circle, rho)
    return {
        "center_offset": center,
        "D": gap,
        "K": curvature,
        "D_padded": gap_padded.real,
        "K_padded": curvature_padded.real,
        "buffer_lower": lower(buffer_padded),
        "buffer_unpadded_lower": lower(buffer),
        "modulus_lower": lower(min_modulus),
        "relative_source_error_upper": upper(modulus_ratio),
        "max_field_phase_step": max_field_step,
        "max_log_phase_step": max_log_step,
        "winding": winding,
    }


class TimeRule:
    def __init__(self, n):
        self.n = n
        self.v = arb(1) / 10
        self.basis = [
            [arb.cos_pi_fmpq(flint.fmpq((n - j) * k, n)) for k in range(n + 2)]
            for j in range(n + 1)
        ]
        self.times = [self.v * (1 + basis[1]) / 2 for basis in self.basis]
        # Exact endpoints and double-event sample, without cosine roundoff.
        self.times[0] = arb(0)
        self.times[n // 2] = self.v / 2
        self.times[-1] = self.v
        self.weights = [arb(1)] * (n + 1)
        self.weights[0] = self.weights[-1] = arb(1) / 2

    def coefficients(self, samples):
        weighted = [weight * sample for weight, sample in zip(self.weights, samples)]
        return [
            2 * self.weights[k] * sum(row[k] * value for row, value in zip(self.basis, weighted)) / self.n
            for k in range(self.n + 1)
        ]

    def primitive_to_end(self, basis, coefficients):
        # The times are mapped affinely from x in [-1, 1].
        result = coefficients[0] * (1 - basis[1])
        result += coefficients[1] * (1 - basis[2]) / 4
        for k in range(2, self.n + 1):
            integral = (1 - basis[k + 1]) / (2 * (k + 1)) - (1 - basis[k - 1]) / (2 * (k - 1))
            result += coefficients[k] * integral
        return self.v * result / 2

    def cost(self, k_samples):
        coefficients = self.coefficients(k_samples)
        weights = [(4 * self.primitive_to_end(row, coefficients)).exp() for row in self.basis]
        # Clenshaw-Curtis by exact integrals of the interpolated weight basis.
        coeff_weights = self.coefficients(weights)
        cost = self.v * sum(2 * coeff_weights[k] / (1 - k**2) for k in range(0, self.n + 1, 2))
        return weights[0], cost


def diagnostics(rule, gaps, ks):
    w, cost = rule.cost(ks)
    w_abs, cost_abs = rule.cost([abs(k) for k in ks])
    signed_margin = gaps[-1] - cost
    abs_margin = gaps[-1] - cost_abs
    transported = signed_margin / w
    return {
        "D_0_direct": gaps[0], "D_v": gaps[-1],
        "W_0_signed": w, "W_0_absolute": w_abs,
        "B_signed": cost, "B_absolute": cost_abs,
        "D_v_minus_B_signed": signed_margin, "D_v_minus_B_absolute": abs_margin,
        "D_0_transported_signed": transported,
        "D_0_transported_absolute": abs_margin / w_abs,
        "D_0_absolute_cost_with_signed_weight": abs_margin / w,
        "identity_mismatch": transported - gaps[0],
    }


def summarize_rows(rows):
    result = {
        "min_modulus": min(row["modulus_lower"] for row in rows),
        "min_pair_buffer": min(row["buffer_unpadded_lower"] for row in rows),
        "min_pair_buffer_source_padded": min(row["buffer_lower"] for row in rows),
        "max_relative_source_error": max(row["relative_source_error_upper"] for row in rows),
        "max_field_phase_step_radians": max(row["max_field_phase_step"] for row in rows),
        "max_normalized_phase_step_radians": max(row["max_log_phase_step"] for row in rows),
        "sampled_polygon_windings": sorted({row["winding"] for row in rows}),
        "K_sample_min": min(midpoint(row["K"].real) for row in rows),
        "K_sample_max": max(midpoint(row["K"].real) for row in rows),
        "D_sample_min": min(midpoint(row["D"].real) for row in rows),
        "D_sample_max": max(midpoint(row["D"].real) for row in rows),
    }
    for key in ("center_offset", "D", "K"):
        result[f"max_imaginary_{key}"] = max(upper(abs(row[key].imag)) for row in rows)
    return result


def quadratic_control(level, circle, rho, pi, rule):
    start = perf_counter()
    rows = []
    for t in rule.times:
        exact_gap = 2 * (t - arb(1) / 20)
        rows.append(contour_row([w**2 - exact_gap for w in circle], circle, rho, pi, arb(0)))
    gaps = [row["D"].real for row in rows]
    ks = [row["K"].real for row in rows]
    values = diagnostics(rule, gaps, ks)
    d_residue = max(upper(abs(d - 2 * (t - arb(1) / 20))) for t, d in zip(rule.times, gaps))
    k_residue = max(upper(abs(k)) for k in ks)
    if max(d_residue, k_residue) > 1e-20 or not values["D_v_minus_B_signed"] < 0:
        raise GateFailure("exact quadratic fails the contour/time regression")
    return {
        "geometry": summarize_rows(rows),
        "comparison": {key: ball_record(value) for key, value in values.items()},
        "max_D_absolute_residue": d_residue,
        "max_K_absolute_residue": k_residue,
        "D_at_double": ball_record(gaps[level.time_count // 2]),
        "seconds": perf_counter() - start,
    }


def field_archive(path, level, fields):
    def components(value):
        return [list(map(int, part.mid_rad_10exp())) for part in (value.real, value.imag)]

    archive = {
        "level": level.__dict__,
        "component_format": "[midpoint_integer, radius_integer, exponent] in decimal powers",
        "array_order": "ascending Chebyshev-Lobatto time, counterclockwise angle starting at zero",
        "field_values": [[components(value) for value in field] for field in fields],
    }
    payload = json.dumps(archive, separators=(",", ":")).encode()
    stored = gzip.compress(payload, mtime=0)
    path.write_bytes(stored)
    return {
        "filename": path.name,
        "content_sha256": sha256(payload).hexdigest(),
        "gzip_sha256": sha256(stored).hexdigest(),
        "gzip_bytes": len(stored),
    }


def run_level(level, cache_dir):
    start = perf_counter()
    ctx.prec = level.bits
    pi = arb.pi()
    a = arb(140101) / 10
    rho = arb(9) / 10
    circle = theta_nodes(level.circle_count, rho, pi)
    rule = TimeRule(level.time_count)
    source = XiSource(pi, a, circle, level.lattice_denominator)
    lattice_error, tail_error = source.source_error()
    control = quadratic_control(level, circle, rho, pi, rule)
    rows = []
    fields = []
    source_seconds = 0.0
    contour_seconds = 0.0
    fail = None
    for j, t in enumerate(rule.times):
        try:
            started = perf_counter()
            field = source.contour(j, t)
            fields.append(field)
            source_seconds += perf_counter() - started
            field_error = arb(0) if j == 0 else (lattice_error + tail_error).upper()
            started = perf_counter()
            rows.append(contour_row(field, circle, rho, pi, field_error))
            contour_seconds += perf_counter() - started
        except GateFailure as exc:
            fail = {"time_index": j, "t": midpoint(t), "reason": str(exc)}
            break
    result = {
        "level": level.__dict__,
        "source_error": {"lattice": ball_record(lattice_error), "tail": ball_record(tail_error)},
        "source_xi_calls": source.xi_calls,
        "canonical_sampled_contours_completed": len(rows),
        "quadratic_control": control,
        "source_xi_seconds": source.xi_seconds,
        "source_total_seconds": source_seconds,
        "contour_consumer_seconds": contour_seconds,
        "failed_gate": fail,
    }
    if rows:
        result["geometry"] = summarize_rows(rows)
    if fail is None:
        started = perf_counter()
        plain = diagnostics(rule, [row["D"].real for row in rows], [row["K"].real for row in rows])
        padded = diagnostics(rule, [row["D_padded"] for row in rows], [row["K_padded"] for row in rows])
        result["comparison"] = {key: ball_record(value) for key, value in plain.items()}
        result["source_padded_comparison"] = {key: ball_record(value) for key, value in padded.items()}
        result["time_consumer_seconds"] = perf_counter() - started
        result["D_by_time"] = [midpoint(row["D"].real) for row in rows]
        result["K_by_time"] = [midpoint(row["K"].real) for row in rows]
    result["field_archive"] = field_archive(cache_dir / f"E04-r1-{level.name}-fields.json.gz", level, fields)
    result["total_seconds"] = perf_counter() - start
    return result


def agreement(coarse, fine):
    common_times = {}
    for key in ("D_by_time", "K_by_time"):
        common_times[key] = max(abs(left - right) for left, right in zip(coarse[key], fine[key][::2]))
    comparisons = {
        name: abs(value["midpoint"] - fine["comparison"][name]["midpoint"])
        for name, value in coarse["comparison"].items()
    }
    return {"max_difference_at_common_times": common_times, "comparison_difference": comparisons}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--cache-dir", type=Path, required=True)
    args = parser.parse_args()
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    result = {
        "request": "VCD-GT-E04-r1",
        "date": "2026-11-16 America/New_York",
        "prepared_for": "Edward Baker",
        "llm_assistance": "OpenAI Codex; explicit gpt-6.1-sol / ultra dispatch; no separate backend attestation",
        "status": "floating contour/time diagnostic; source padding at sampled nodes only",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "platform": {"python": platform.python_version(), "python_flint": flint.__version__, "machine": platform.machine()},
        "levels": [],
    }
    for level in LEVELS:
        print(f"starting {level.name}", flush=True)
        evidence = run_level(level, args.cache_dir)
        result["levels"].append(evidence)
        if len(result["levels"]) == 2 and not evidence["failed_gate"]:
            result["agreement"] = agreement(*result["levels"])
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(f"{level.name}: {evidence['source_xi_calls']} xi calls in {evidence['total_seconds']:.2f} seconds; "
              f"gate: {evidence['failed_gate']}", flush=True)
        if evidence["failed_gate"]:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
