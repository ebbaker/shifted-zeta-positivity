#!/usr/bin/env python3
"""E34 fixed complete-source extension for Edward Baker, 18 November 2026.

OpenAI Codex LLM assistance; actual model/effort unavailable, inherited.
The analytical payments are in CM Note39. No new source samples are made.
"""

import argparse
from hashlib import sha256
import importlib.util
import json
from math import factorial
from pathlib import Path
import platform
import sys
from time import perf_counter

import flint
from flint import acb, acb_poly, arb, ctx

CM = Path(__file__).resolve().parents[1]
GT = CM.parent
ROOT = CM.parents[4]
BASE_PATH = GT / "numerics/vcd_gt_lehmer_certificate.py"
BASE_HASH = "549f3073e8783a10fba75ea160d67928f6fdcb9082d21e3e68500bf9a86138a2"
MANIFEST = CM / "research-progress/handoffs/VCD-GT-CM-E34-inputs-r1.json"
START = perf_counter()
CAP_SECONDS = 1200


def check_time():
    if perf_counter() - START > CAP_SECONDS:
        raise RuntimeError("E34 elapsed-time cap exhausted")


def load_base():
    if sha256(BASE_PATH.read_bytes()).hexdigest() != BASE_HASH:
        raise RuntimeError("inherited consumer hash mismatch")
    spec = importlib.util.spec_from_file_location("vcd_gt_e34_base", BASE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = load_base()
q = base.fixed_q
upper = base.abs_upper


def check_pins():
    manifest = json.loads(MANIFEST.read_text())
    checked = []
    for row in manifest["files"]:
        data = (ROOT / row["path"]).read_bytes()
        if len(data) != row["bytes"] or sha256(data).hexdigest() != row["sha256"]:
            raise RuntimeError("frozen input mismatch: " + row["path"])
        checked.append(row)
    return checked


def chebyshev_weights():
    x = q(503, 500)
    ts = [arb(1), x]
    us = [arb(1), 2*x]
    for _ in range(2, 33):
        ts.append(2*x*ts[-1] - ts[-2])
        us.append(2*x*us[-1] - us[-2])
    ds = [arb(0)] + [k*us[k-1] for k in range(1, 33)]
    if not ts[32] < 17 or not (x*x-1)*us[31] < 2:
        raise RuntimeError("extrapolation constants failed")
    return ts, ds, (x*x-1)*us[31]


def extended_error(sample_radius):
    _, source_error, old = base.tensor_error(sample_radius)
    node_error = sum(arb(old[key]) for key in (
        "spatial_sample_propagation_upper_before_time_operator",
        "spatial_alias_upper_before_time_operator",
        "spatial_truncation_upper_before_time_operator"))
    m9 = q(81*27, 32)*7016**3*3508**2
    if not m9 < 3*10**20:
        raise RuntimeError("radius-nine majorant constant failed")
    ts, ds, product = chebyshev_weights()
    if not 64*ts[32] < 1100:
        raise RuntimeError("Lobatto norm gate failed")
    time_error = (arb(4*10**20)*factorial(66)*q(1, 20)**33*2 /
                  (factorial(33)*2**31*(arb(5)-q(21, 20))**66))
    error = (1100*node_error + time_error).upper()
    if not error < q(53, 100):
        raise RuntimeError("extended disk error exceeds frozen 0.53 allowance")
    return error, source_error, ts, ds, {
        "inherited_node_error_components": old,
        "radius9_time_zero_majorant": str(m9),
        "negative_time_radius5_majorant": 4*10**20,
        "T32_at_503_over_500": str(ts[32]),
        "exterior_node_product_factor": str(product),
        "Lobatto_operator_allowance": 1100,
        "time_interpolation_error_upper": str(time_error.upper()),
        "uniform_extended_disk_error_upper": str(error),
    }


class ExtendedField(base.FieldPolynomial):
    def __init__(self, coefficients, error, t_weights, d_weights):
        super().__init__(coefficients, error)
        self.t_weights = t_weights
        self.d_weights = d_weights

    def circle(self, radius, count):
        by_radius = [[value*radius**(n-2) for value in row]
                     for n, row in enumerate(self.coefficients)]
        angle_derivative = sum(
            abs(n-2)*sum(upper(value)*self.t_weights[k]
                         for k, value in enumerate(row))
            for n, row in enumerate(by_radius)).upper()
        nodes = []
        for j in range(count//2 + 1):
            unit = base.exp_pi_i(2*j, count)
            phases = [unit**(n-2) for n in range(base.DEGREE+1)]
            coefficients = [self.sign*sum(row[k]*phase for row, phase in zip(by_radius, phases))
                            for k in range(base.DEGREE+1)]
            derivative = sum(self.d_weights[k]*upper(value)
                             for k, value in enumerate(coefficients)).upper()
            polynomial = sum((coefficient*basis for coefficient, basis in zip(coefficients, self.basis)),
                             acb_poly())
            nodes.append(base.AngularNode(radius*unit, polynomial, derivative))
        return base.Circle(radius, count, nodes, angle_derivative)


def midpoint_halfwidth(i, cells):
    half = q(1003, 1000*cells)
    return -q(503, 500)+(2*i+1)*half, half


def geometry(field, attempts):
    circles = None
    for cells, arcs in base.GEOMETRY_SCHEDULE:
        start = perf_counter()
        if circles is None or circles[0].arcs != arcs:
            circles = [field.circle(q(3, 4), arcs), field.circle(q(21, 20), arcs)]
        half = midpoint_halfwidth(0, cells)[1]
        pads = [field.radii_for_time_cell(circle, half, arb.pi()/arcs) for circle in circles]
        floors, ceilings = [None, None], [arb(0), arb(0)]
        failure = None
        for i in range(cells):
            check_time()
            midpoint, _ = midpoint_halfwidth(i, cells)
            for j, (circle, padding) in enumerate(zip(circles, pads)):
                for node, pad in zip(circle.nodes, padding):
                    value = node.time_polynomial(acb(midpoint))
                    low = (value.real-pad).lower()
                    if not low > 0:
                        failure = {"time_cell": i, "boundary": j, "real_lower": str(low)}
                        break
                    floors[j] = low if floors[j] is None else min(floors[j], low)
                    ceilings[j] = max(ceilings[j], (abs(value)+pad).upper())
                if failure:
                    break
            if failure:
                break
        attempts.append({"cells": cells, "arcs": arcs, "failure": failure,
                         "seconds": perf_counter()-start})
        if failure is None:
            return circles, (floors, ceilings)
    raise RuntimeError("extended geometry schedule exhausted")


class ExtendedCertificate(base.ContourCertificate):
    def integrate(self, values):
        c, d, old_k, q_bounds, m_error = super().integrate(values)
        c_bound, d_bound = upper(c), upper(d)
        f_bounds = [2*circle.radius*(circle.radius+c_bound)*log_bound*
                    (24/q_bound**3+48*d_bound/q_bound**4)
                    for circle, log_bound, q_bound in zip(self.boundaries, self.log_bounds, q_bounds)]
        f_error = self.mean_error(f_bounds)
        total = arb(0)
        last = len(self.target.nodes)-1
        for j, (node, value) in enumerate(zip(self.target.nodes, values)):
            log = value.log()-self.center
            offset = node.w-c
            quadratic = offset**2-d
            if quadratic.contains(0):
                raise RuntimeError("forcing node denominator contains zero")
            weight = 1 if j in (0, last) else 2
            total -= weight*(2*node.w*offset*log*(24/quadratic**3+48*d/quadratic**4)).real
        forcing = total/base.N + arb(0, f_error)
        return c, d, -old_k, forcing, q_bounds, m_error, f_error


def describe(values):
    c, d, m, f, q_bounds, m_error, f_error = values
    return {"center_offset": str(c), "D": str(d), "D_lower": str(d.lower()),
            "D_upper": str(d.upper()), "M": str(m), "F": str(f),
            "F_lower": str(f.lower()), "F_upper": str(f.upper()),
            "Q_collar_lower_bounds": [str(x) for x in q_bounds],
            "M_annular_error_upper": str(m_error), "F_annular_error_upper": str(f_error)}


def endpoint(cert, time):
    return cert.enclose(20*time-1, cert.padding(arb(0)))


def time_pass(cert, count):
    start = perf_counter()
    half = midpoint_halfwidth(0, count)[1]
    pads = cert.padding(half)
    low, high = [None]*4, [None]*4
    q_floors = None
    errors = [arb(0), arb(0)]
    for i in range(count):
        check_time()
        mid, _ = midpoint_halfwidth(i, count)
        try:
            values = cert.enclose(mid, pads)
        except (base.GateFailure, RuntimeError) as exc:
            return None, {"cells_attempted": i+1, "cells_total": count,
                          "failure": str(exc), "seconds": perf_counter()-start}
        for j, value in enumerate(values[:4]):
            low[j] = value.lower() if low[j] is None else min(low[j], value.lower())
            high[j] = value.upper() if high[j] is None else max(high[j], value.upper())
        q_floors = values[4] if q_floors is None else [min(a, b) for a, b in zip(q_floors, values[4])]
        errors = [max(a, b) for a, b in zip(errors, values[5:])]
    gates = {"center_abs_lt_1_over_10": max(abs(low[0]), abs(high[0])) < q(1, 10),
             "D_abs_lt_1_over_5": max(abs(low[1]), abs(high[1])) < q(1, 5),
             "D_gt_1_over_10000": low[1] > q(1, 10000),
             "F_ge_3_over_10": low[3] >= q(3, 10)}
    result = {"bounds": {name: {"lower": str(lo), "upper": str(hi)}
                         for name, lo, hi in zip(("center_offset", "D", "M", "F"), low, high)},
              "Q_collar_lower_bounds": [str(x) for x in q_floors],
              "annular_error_upper": {"M": str(errors[0]), "F": str(errors[1])},
              "gates": gates, "all_gates": all(gates.values()),
              "direct_D_margin_above_stop_lower": str((low[1]-q(1, 10000)).lower())}
    attempt = {"cells_attempted": count, "cells_total": count, "failure": None,
               "gates": gates, "seconds": perf_counter()-start}
    return result, attempt


def retained_comparison():
    d, b, duration, f = q(1787368, 10**7), q(6037742, 10**7), q(1003, 10000), q(3, 10)
    lam = (2*f).sqrt()
    s = (lam*duration).sinh()/lam
    w = (lam*duration).cosh()+2*b*s
    result = w*(d*w-2*s)
    margin = result-q(1, 10000)
    if not margin > q(6246, 10**8):
        raise RuntimeError("retained forcing rational margin check failed")
    return {"d": str(d), "b": str(b), "F_floor": str(f), "duration": str(duration),
            "D_lower_at_terminal": str(result.lower()), "margin_above_stop_lower": str(margin.lower()),
            "same_information_direct_DM": "identical comparison; no algorithmic advantage claimed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = base.BITS
    record = {"request": "VCD-GT-CM-E34-r1", "date": "2026-11-18 America/New_York",
              "prepared_for": "Edward Baker", "llm_assistance": "OpenAI Codex; actual model/effort unavailable; inherited",
              "status": "execution pending separate E35 assessment", "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "versions": {"python": platform.python_version(), "platform": platform.platform(),
                           "python_flint": flint.__version__, "flint": flint.__FLINT_VERSION__},
              "source_calls": 0, "bits": base.BITS, "spatial_degree": 32, "time_degree": 32,
              "contour_nodes": 128, "time_interval": ["-3/10000", "1/10"],
              "geometry_schedule": base.GEOMETRY_SCHEDULE, "time_schedule": base.TIME_SCHEDULE,
              "elapsed_cap_seconds": CAP_SECONDS, "local_repair_limit": 2, "local_repairs_used": 0,
              "archive": {"name": base.ARCHIVE, "stored_sha256": base.STORED_SHA256, "content_sha256": base.CONTENT_SHA256},
              "canonical": {"geometry_attempts": [], "time_attempts": []},
              "quadratic_control": {"geometry_attempts": [], "time_attempts": []}}
    exit_code = 0
    try:
        record["verified_frozen_inputs"] = check_pins()
        samples = base.archived_fields(args.cache_dir)
        coefficients, sample_radius = base.tensor_coefficients(samples)
        error, source_error, ts, ds, record["extended_error"] = extended_error(sample_radius)
        field = ExtendedField(coefficients, error, ts, ds)
        circles, data = geometry(field, record["canonical"]["geometry_attempts"])
        cert = ExtendedCertificate(field, field.circle(q(9, 10), base.N), circles, data)
        canonical = record["canonical"]
        canonical["sign"] = field.sign
        canonical["geometry"] = cert.geometry_record(data)
        canonical["count_on_each_boundary"] = 2
        canonical["endpoints"] = {name: describe(endpoint(cert, time)) for name, time in
                                  (("negative_terminal", -q(3, 10000)), ("time_zero", arb(0)), ("positive_anchor", q(1, 10)))}
        canonical["inherited_endpoint_rows_with_new_geometry"] = {
            "time_zero": describe(cert.archived_endpoint(samples[0], arb(0))),
            "positive_anchor": describe(cert.archived_endpoint(samples[-1], source_error))}
        for count in base.TIME_SCHEDULE:
            result, attempt = time_pass(cert, count)
            canonical["time_attempts"].append(attempt)
            if result is not None:
                canonical["whole_interval"] = result
                if result["all_gates"]:
                    break
        canonical["success"] = canonical.get("whole_interval", {}).get("all_gates", False)
        record["retained_F_comparison"] = retained_comparison()
        control = record["quadratic_control"]
        cfield = ExtendedField(base.quadratic_coefficients(), arb(0), ts, ds)
        ccircles, cdata = geometry(cfield, control["geometry_attempts"])
        ccert = ExtendedCertificate(cfield, cfield.circle(q(9, 10), base.N), ccircles, cdata)
        control["geometry"] = ccert.geometry_record(cdata)
        control["count_on_each_boundary"] = 2
        cresult, cattempt = time_pass(ccert, base.TIME_SCHEDULE[0])
        control["time_attempts"].append(cattempt)
        control["whole_interval"] = cresult
        collision = endpoint(ccert, q(1, 20))
        control["collision_time"] = describe(collision)
        control["success"] = (cresult is not None and not cresult["gates"]["F_ge_3_over_10"]
                              and not cresult["gates"]["D_gt_1_over_10000"]
                              and collision[1].contains(0) and collision[3].contains(0)
                              and arb(cresult["bounds"]["F"]["lower"]) <= 0
                              and arb(cresult["bounds"]["F"]["upper"]) >= 0)
        record["success"] = canonical["success"] and control["success"]
        if not record["success"]:
            exit_code = 1
    except Exception as exc:
        record["success"] = False
        record["failure"] = type(exc).__name__ + ": " + str(exc)
        exit_code = 1
    record["elapsed_seconds"] = perf_counter()-START
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"output": str(args.output), "success": record["success"],
                      "failure": record.get("failure"), "elapsed_seconds": record["elapsed_seconds"]}))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
