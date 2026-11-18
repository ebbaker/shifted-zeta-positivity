#!/usr/bin/env python3
"""E36 fixed common-log discriminant comparison for Edward Baker.

18 November 2026. OpenAI Codex assistance; actual model/effort unavailable.
No new source samples or full-time replay. Analytical proof: CM Note42.
"""

import argparse
from dataclasses import dataclass
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import platform
import statistics
import sys
from time import perf_counter

import flint
from flint import acb, arb, ctx

CM = Path(__file__).resolve().parents[1]
ROOT = CM.parents[4]
EXT_PATH = CM / "numerics/vcd_gt_cm_extended_source.py"
EXT_HASH = "890d5585fa8c395c1f57868ac80a4311ffd58052f5d8510e32ba7ccb1cf8e15e"
MANIFEST = CM / "research-progress/handoffs/VCD-GT-CM-E36-inputs-r1.json"
E34_PATH = CM / "numerics/16_VCD_GT_CM_EXTENDED_SOURCE_CERTIFICATE_20261118.json"
START = perf_counter()
CAP_SECONDS = 120


def check_time():
    if perf_counter()-START > CAP_SECONDS:
        raise RuntimeError("E36 120-second cap exhausted")


def import_extended():
    if sha256(EXT_PATH.read_bytes()).hexdigest() != EXT_HASH:
        raise RuntimeError("E34 consumer hash mismatch")
    spec = importlib.util.spec_from_file_location("vcd_gt_cm_e36_extended", EXT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ext = import_extended()
base = ext.base
q = base.fixed_q


def verify_inputs():
    manifest = json.loads(MANIFEST.read_text())
    for row in manifest["files"]:
        data = (ROOT / row["path"]).read_bytes()
        if len(data) != row["bytes"] or sha256(data).hexdigest() != row["sha256"]:
            raise RuntimeError("E36 frozen input mismatch: " + row["path"])
    return manifest["files"]


@dataclass
class Row:
    w: acb
    w2: acb
    ell: acb
    a: arb
    b: arb
    weight: int


@dataclass
class Prepared:
    rows: list
    gamma0: arb
    s20: arb
    epsilon1: arb
    epsilon2: arb
    h: arb
    boxes: list
    inherited_endpoint: arb
    preparation_record: dict


def exact_point(value, name):
    if not value.is_exact():
        raise RuntimeError(name + " is not an exact representable value")
    return value


def fixed_geometry(field):
    """Reproduce just the successful E34 16-by-64 geometry, no refinement."""
    start = perf_counter()
    cells, arcs = 16, 64
    circles = [field.circle(q(3, 4), arcs), field.circle(q(21, 20), arcs)]
    half = ext.midpoint_halfwidth(0, cells)[1]
    pads = [field.radii_for_time_cell(c, half, arb.pi()/arcs) for c in circles]
    floors, ceilings = [None, None], [arb(0), arb(0)]
    for i in range(cells):
        check_time()
        midpoint, _ = ext.midpoint_halfwidth(i, cells)
        for j, (circle, padding) in enumerate(zip(circles, pads)):
            for node, pad in zip(circle.nodes, padding):
                value = node.time_polynomial(acb(midpoint))
                low = (value.real-pad).lower()
                if not low > 0:
                    raise RuntimeError("fixed 16-by-64 geometry failed")
                floors[j] = low if floors[j] is None else min(floors[j], low)
                ceilings[j] = max(ceilings[j], (abs(value)+pad).upper())
    return circles, (floors, ceilings), perf_counter()-start


def prepare(field, time):
    started = perf_counter()
    circles, geometry, geometry_seconds = fixed_geometry(field)
    target_started = perf_counter()
    target = field.circle(q(9, 10), base.N)
    cert = ext.ExtendedCertificate(field, target, circles, geometry)
    target_seconds = perf_counter()-target_started
    logs_started = perf_counter()
    pads = cert.padding(arb(0))
    x = acb(20*time-1)
    rows, boxes = [], []
    nominal1, nominal2 = arb(0), arb(0)
    old1, old2 = arb(0), arb(0)
    for j, (node, pad) in enumerate(zip(target.nodes, pads)):
        check_time()
        value = node.time_polynomial(x)+pad
        if not value.real > 0:
            raise RuntimeError("endpoint source log reaches nonpositive half-plane")
        log = value.log()-cert.center
        re, im = log.real, log.imag
        mr, mi = exact_point(re.mid(), "real midpoint"), exact_point(im.mid(), "imag midpoint")
        a, b = exact_point(re.rad(), "real radius"), exact_point(im.rad(), "imag radius")
        ell = acb(mr, mi)
        weight = 1 if j in (0, len(target.nodes)-1) else 2
        w, w2 = node.w, node.w**2
        rows.append(Row(w, w2, ell, a, b, weight))
        boxes.append({"node": j, "weight": weight,
                      "real_midpoint_exact": str(mr.fmpq()), "imag_midpoint_exact": str(mi.fmpq()),
                      "real_radius_exact": str(a.fmpq()), "imag_radius_exact": str(b.fmpq())})
        product = w*log
        old1 -= weight*product.real
        old2 -= 2*weight*(w*product).real
        nominal1 -= weight*(w*ell).real
        nominal2 -= weight*(w2*ell).real
    epsilon1, epsilon2 = cert.moment_errors
    exact_point(epsilon1, "chosen first annular allowance")
    exact_point(epsilon2, "chosen second annular allowance")
    oldp1 = old1/base.N+arb(0, epsilon1)
    oldp2 = old2/base.N+arb(0, epsilon2)
    oldd = oldp2/2-(oldp1/2)**2
    gamma0, s20 = nominal1/(2*base.N), nominal2/base.N
    h = exact_point(gamma0.mid(), "frozen reference h")
    logs_seconds = perf_counter()-logs_started
    prep = {"geometry_seconds": geometry_seconds, "target_and_tail_setup_seconds": target_seconds,
            "endpoint_logs_and_nominal_moments_seconds": logs_seconds,
            "total_seconds": perf_counter()-started,
            "geometry": cert.geometry_record(geometry), "geometry_cells": 16, "arcs_per_boundary": 64,
            "count_on_each_boundary": 2, "represented_contour_nodes": base.N,
            "complex_log_evaluations": len(rows), "box_conversion_enlargement": "none: exact Arb dyadic midpoint/radius",
            "log_boxes_sha256": sha256(json.dumps(boxes, sort_keys=True, separators=(",", ":")).encode()).hexdigest()}
    return Prepared(rows, gamma0, s20, epsilon1, epsilon2, h, boxes, oldd, prep)


def support(prepared, kernel):
    """Full lower/upper enclosure of the exact rectangular support value."""
    return sum(row.weight*(abs(kernel(row).real)*row.a + abs(kernel(row).imag)*row.b)
               for row in prepared.rows)/base.N


def square_range(value):
    left, right = value.lower(), value.upper()
    largest = max(abs(left), abs(right))
    high = (largest**2).upper()
    low = arb(0) if value.contains(0) else (min(abs(left), abs(right))**2).lower()
    return low, high


def separate(prepared):
    rg = (support(prepared, lambda row: row.w)+prepared.epsilon1)/2
    r2 = support(prepared, lambda row: row.w2)+prepared.epsilon2/2
    g0, s0 = prepared.gamma0, prepared.s20
    if not g0 > rg:
        # General rectangle, needed by the exact quadratic collision control.
        gamma = g0+arb(0, rg.upper())
        sqlo, sqhi = square_range(gamma)
        lower = s0-r2-sqhi
        upper = s0+r2-sqlo
        width = upper-lower
        width_formula = "general Cartesian square range"
    else:
        lower = s0-r2-(g0+rg)**2
        upper = s0+r2-(g0-rg)**2
        width = 2*r2+4*g0*rg
        width_formula = "2*r2+4*gamma0*r_gamma; gamma0>r_gamma verified"
    return {"r_gamma": rg, "r2": r2, "lower": lower, "upper": upper,
            "width": width, "width_formula": width_formula}


def correlated(prepared):
    rg = (support(prepared, lambda row: row.w)+prepared.epsilon1)/2
    h = prepared.h
    rh = support(prepared, lambda row: row.w2-h*row.w)+prepared.epsilon2/2+abs(h)*prepared.epsilon1
    j0 = prepared.s20-2*h*prepared.gamma0+h*h
    gamma = prepared.gamma0+arb(0, rg.upper())
    sqlo, sqhi = square_range(gamma-h)
    lower_expr, upper_expr = j0-rh-sqhi, j0+rh-sqlo
    lower, upper = lower_expr.lower(), upper_expr.upper()
    width = (upper-lower).upper()
    return {"r_gamma": rg, "R_h": rh, "h": h, "J0": j0, "Gamma": gamma,
            "square_lower": sqlo, "square_upper": sqhi,
            "lower": lower, "upper": upper, "width_upper": width}


def printable(values):
    return {key: str(value) if isinstance(value, (arb, acb)) else value for key, value in values.items()}


def benchmark(prepared):
    # Exactly one untimed warmup of each; these values own the comparison.
    separate_result, correlated_result = separate(prepared), correlated(prepared)
    times = {"separate": [], "correlated": []}
    orders = []
    for i in range(21):
        check_time()
        order = (("separate", separate), ("correlated", correlated)) if i % 2 == 0 else (
            ("correlated", correlated), ("separate", separate))
        orders.append([name for name, _ in order])
        for name, function in order:
            started = perf_counter()
            result = function(prepared)
            times[name].append(perf_counter()-started)
            expected = separate_result if name == "separate" else correlated_result
            if printable(result) != printable(expected):
                raise RuntimeError("assembly output changed during fixed timing diagnostic")
    timing = {"untimed_warmups_per_method": 1, "paired_repetitions": 21, "orders": orders,
              "seconds": times, "median_seconds": {name: statistics.median(xs) for name, xs in times.items()},
              "accounting": "shared preparation charged to both; arithmetic and total runtime not asserted equal"}
    timing["median_correlated_over_separate"] = timing["median_seconds"]["correlated"]/timing["median_seconds"]["separate"]
    return separate_result, correlated_result, timing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 224
    record = {"request": "VCD-GT-CM-E36-r1", "date": "2026-11-18 America/New_York",
              "prepared_for": "Edward Baker", "llm_assistance": "OpenAI Codex; actual model/effort unavailable; inherited",
              "status": "pending separate E37 assessment", "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "versions": {"python": platform.python_version(), "platform": platform.platform(),
                           "python_flint": flint.__version__, "flint": flint.__FLINT_VERSION__},
              "bits": 224, "source_calls": 0, "degree_time_and_space": 32, "contour_nodes": 128,
              "time": "-3/10000", "inherited_whole_interval": ["-3/10000", "1/10"],
              "inherited_statistic": "min_I D = D(-.0003), E34 paid D_t>1.5072",
              "new_whole_time_cells": 0, "full_E34_time_audit_rerun": False,
              "elapsed_cap_seconds": CAP_SECONDS, "local_repair_limit": 2, "local_repairs_used": 1,
              "local_repair": "Account separately for field construction and full common preparation; no mathematical change",
              "first_successful_attempt": {
                  "script_sha256": "cfb8c99adca9c7e744dd4a1559c1387c2c2e78a9da8ad49985d2aa4023746875",
                  "record_sha256": "9a8c311eb54d8d040d91465428bbe86b443fe9357a01fba8a11cb7549e536245",
                  "reading_copy": "/private/tmp/vcd-gt-cm-E36-attempt1.json",
                  "all_mathematical_gates_passed": True,
                  "width_reduction_percent_vs_sharp_lower_summary": "6.40310139",
                  "width_reduction_percent_vs_E34_lower_summary": "26.09208424",
                  "elapsed_seconds": 0.3436674579861574},
              "archive": {"name": base.ARCHIVE, "stored_sha256": base.STORED_SHA256, "content_sha256": base.CONTENT_SHA256}}
    exit_code = 0
    try:
        started = perf_counter()
        record["verified_frozen_inputs"] = verify_inputs()
        record["input_validation_seconds"] = perf_counter()-started
        inherited = json.loads(E34_PATH.read_text())
        if inherited["script_sha256"] != EXT_HASH or not inherited["success"]:
            raise RuntimeError("inconsistent E34 source certificate")
        source_started = perf_counter()
        samples = base.archived_fields(args.cache_dir)
        archive_seconds = perf_counter()-source_started
        reconstruction_started = perf_counter()
        coefficients, sample_radius = base.tensor_coefficients(samples)
        error, _, ts, ds, error_record = ext.extended_error(sample_radius)
        reconstruction_seconds = perf_counter()-reconstruction_started
        field_started = perf_counter()
        field = ext.ExtendedField(coefficients, error, ts, ds)
        field_seconds = perf_counter()-field_started
        prepared = prepare(field, -q(3, 10000))
        full_common_seconds = perf_counter()-source_started
        old = inherited["canonical"]["endpoints"]["negative_terminal"]
        if str(prepared.inherited_endpoint) != old["D"]:
            raise RuntimeError("reconstructed E34 endpoint interval differs")
        if str(prepared.inherited_endpoint.lower()) != old["D_lower"] or str(prepared.inherited_endpoint.upper()) != old["D_upper"]:
            raise RuntimeError("reconstructed E34 endpoint bounds differ")
        if prepared.preparation_record["geometry"] != inherited["canonical"]["geometry"]:
            raise RuntimeError("reconstructed E34 geometry differs")
        sep, corr, timing = benchmark(prepared)
        oldlo, oldhi = arb(old["D_lower"]), arb(old["D_upper"])
        old_width = oldhi-oldlo
        gates = {"one_percent_width_gain_vs_sharp_rectangle": corr["width_upper"] <= q(99, 100)*sep["width"].lower(),
                 "one_percent_width_gain_vs_E34": corr["width_upper"] <= q(99, 100)*old_width.lower(),
                 "lower_strictly_improves_sharp_rectangle": corr["lower"] > sep["lower"].upper(),
                 "lower_strictly_improves_E34": corr["lower"] > oldlo.upper(),
                 "D_above_fixed_target": corr["lower"] > q(16246, 10**8)}
        ratio_sharp = corr["width_upper"]/sep["width"]
        ratio_old = corr["width_upper"]/old_width
        record["canonical"] = {
            "source_preparation": {"archive_load_hash_check_seconds": archive_seconds,
                                   "polynomial_and_error_reconstruction_seconds": reconstruction_seconds,
                                   "field_construction_seconds": field_seconds,
                                   "endpoint_preparation": prepared.preparation_record,
                                   "total_common_seconds": full_common_seconds},
            "same_E34_geometry_and_endpoint_reproduced": True,
            "extended_source_error": error_record,
            "log_rectangles": prepared.boxes,
            "nominal_gamma0": str(prepared.gamma0), "nominal_half_p2": str(prepared.s20),
            "epsilon1": str(prepared.epsilon1), "epsilon2": str(prepared.epsilon2),
            "reference_h_exact": str(prepared.h.fmpq()),
            "sharp_separate_moments": printable(sep), "correlated": printable(corr),
            "recorded_E34": {"lower": old["D_lower"], "upper": old["D_upper"], "width": str(old_width)},
            "width_ratio_to_sharp": str(ratio_sharp), "width_ratio_to_E34": str(ratio_old),
            "width_reduction_percent_vs_sharp": str(100*(1-ratio_sharp)),
            "width_reduction_percent_vs_E34": str(100*(1-ratio_old)),
            "gates": gates, "all_gates": all(gates.values()), "timing": timing,
            "assembly_work": {"both": "two 65-term rectangular support sums, nominal moments shared",
                              "separate": "kernels w and w^2; Cartesian square range",
                              "correlated": "kernels w and w^2-h*w; centered nominal value and full shifted square",
                              "claim": "equal source/node/log budget; no equal arithmetic or speed claim"}}
        control_started = perf_counter()
        cfield = ext.ExtendedField(base.quadratic_coefficients(), arb(0), ts, ds)
        control = prepare(cfield, q(1, 20))
        csep, ccorr = separate(control), correlated(control)
        retains_zero = (csep["lower"].lower() <= 0 and csep["upper"].upper() >= 0
                        and ccorr["lower"] <= 0 and ccorr["upper"] >= 0)
        record["quadratic_control"] = {"time": "1/20", "exact_D": 0,
                                       "preparation": control.preparation_record,
                                       "sharp_separate": printable(csep), "correlated": printable(ccorr),
                                       "retains_collision": retains_zero, "seconds": perf_counter()-control_started}
        record["total_complex_logs"] = len(prepared.rows)+len(control.rows)
        record["success"] = all(gates.values()) and retains_zero
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
