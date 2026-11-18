#!/usr/bin/env python3
"""E38 actual-cardinal source refinement for Edward Baker, 18 Nov 2026.

OpenAI Codex LLM assistance; selected helper gpt-6.1-sol / ultra;
independent serving attestation unavailable. Proof: CM Note45.
Only 1100 -> 17 in the nodal source amplification changes.
"""

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from math import factorial
from pathlib import Path
import platform
import statistics
import sys
from time import perf_counter

import flint
from flint import acb, arb, ctx

CM = Path(__file__).resolve().parents[1]
ROOT = CM.parents[4]
CORRELATION_PATH = CM / "numerics/vcd_gt_cm_correlated_discriminant.py"
CORRELATION_HASH = "b2d799e20654e76ff72ca949278d5d192396b527eb05ae25d6b8813f374fbf52"
RECORD19_PATH = CM / "numerics/19_VCD_GT_CM_CORRELATED_DISCRIMINANT_20261118.json"
MANIFEST = CM / "research-progress/handoffs/VCD-GT-CM-E38-inputs-r1.json"
START = perf_counter()
CAP_SECONDS = 1200


def check_time():
    if perf_counter()-START > CAP_SECONDS:
        raise RuntimeError("E38 1200-second cap exhausted")


def load_correlation():
    if sha256(CORRELATION_PATH.read_bytes()).hexdigest() != CORRELATION_HASH:
        raise RuntimeError("inherited E36 consumer hash mismatch")
    spec = importlib.util.spec_from_file_location("vcd_gt_cm_e38_correlation", CORRELATION_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


corr = load_correlation()
ext, base = corr.ext, corr.base
q = base.fixed_q


def verify_inputs():
    manifest = json.loads(MANIFEST.read_text())
    if not manifest.get("files"):
        raise RuntimeError("empty E38 frozen input manifest")
    checked = {}
    for row in manifest["files"]:
        data = (ROOT / row["path"]).read_bytes()
        if len(data) != row["bytes"] or sha256(data).hexdigest() != row["sha256"]:
            raise RuntimeError("E38 frozen input mismatch: " + row["path"])
        checked[row["path"]] = row
    # Require the most consequential data/code consumers to be manifest-bound.
    for path in (RECORD19_PATH, CORRELATION_PATH, corr.EXT_PATH, base.__file__):
        relative = str(Path(path).resolve().relative_to(ROOT))
        if relative not in checked:
            raise RuntimeError("E38 manifest omits required input: " + relative)
    return manifest["files"]


def cardinal_error(sample_radius):
    """Retain all old payments and weights; replace only node norm 1100 by17."""
    old_error, source_error, ts, ds, inherited = ext.extended_error(sample_radius)
    old = inherited["inherited_node_error_components"]
    node_error = sum(arb(old[key]) for key in (
        "spatial_sample_propagation_upper_before_time_operator",
        "spatial_alias_upper_before_time_operator",
        "spatial_truncation_upper_before_time_operator"))
    time_error = (arb(4*10**20)*factorial(66)*q(1, 20)**33*2 /
                  (factorial(33)*2**31*(arb(5)-q(21, 20))**66))
    t0, t1, x = Fraction(1), Fraction(503, 500), Fraction(503, 500)
    for _ in range(1, 32):
        t0, t1 = t1, 2*x*t1-t0
    if not t1 < 17 or not 8 < 17 or not ts[32] < 17:
        raise RuntimeError("exact cardinal bound failed")
    error = (17*node_error+time_error).upper()
    if not error < q(82, 10000) or not error < old_error:
        raise RuntimeError("fixed refined source allowance failed")
    return error, source_error, ts, ds, {
        "inherited_extended_error_record": inherited,
        "E_node_upper": str(node_error.upper()),
        "Lobatto_operator_allowance": 17,
        "cardinal_proof": "Note45: actual endpoint-weighted DCT-I; interior sqrt64, exterior T32",
        "T32_exact_numerator": t1.numerator,
        "T32_exact_denominator": t1.denominator,
        "T32_exact_margin_to_17_numerator": 17*t1.denominator-t1.numerator,
        "time_interpolation_error_upper_unchanged": str(time_error.upper()),
        "uniform_extended_disk_error_upper": str(error),
        "old_uniform_extended_disk_error_upper": str(old_error),
        "source_error_ratio_to_old": str(error/old_error),
        "derivative_weights": "unchanged T_k(503/500), k U_(k-1)(503/500)",
        "arithmetic_payment": "all coefficients and evaluations kept as outward Acb balls; diagnostic not added twice",
    }


def coefficient_audit(coefficients, ts):
    started = perf_counter()
    radii, allowance = [], arb(0)
    radius = q(21, 20)
    for n, row in enumerate(coefficients):
        for k, value in enumerate(row):
            a, b = value.real.rad(), value.imag.rad()
            disk = (a*a+b*b).sqrt().upper()
            radii.append(disk)
            allowance += radius**n*ts[k]*disk
    return {
        "exact_polynomial": "archive decimal midpoints -> exact root-of-unity DFT -> exact endpoint-weighted DCT-I",
        "coefficient_count": len(radii),
        "maximum_coefficient_disk_radius_upper": str(max(radii)),
        "uniform_disk_coefficient_radius_sum_upper": str(allowance.upper()),
        "treatment": "diagnostic of arithmetic already paid inside coefficient balls; no coefficient midpoint extraction",
        "seconds": perf_counter()-started,
    }


def prepare(cert, time):
    """Exactly the E36 shared log rectangles, using the newly enclosed common cert."""
    started = perf_counter()
    pads = cert.padding(arb(0))
    x = acb(20*time-1)
    rows, boxes = [], []
    nominal1, nominal2 = arb(0), arb(0)
    old1, old2 = arb(0), arb(0)
    for j, (node, pad) in enumerate(zip(cert.target.nodes, pads)):
        check_time()
        value = node.time_polynomial(x)+pad
        if not value.real > 0:
            raise RuntimeError("endpoint source log reaches nonpositive half-plane")
        log = value.log()-cert.center
        mr = corr.exact_point(log.real.mid(), "real log midpoint")
        mi = corr.exact_point(log.imag.mid(), "imag log midpoint")
        a = corr.exact_point(log.real.rad(), "real log radius")
        b = corr.exact_point(log.imag.rad(), "imag log radius")
        ell, w = acb(mr, mi), node.w
        w2 = w*w
        weight = 1 if j in (0, len(cert.target.nodes)-1) else 2
        rows.append(corr.Row(w, w2, ell, a, b, weight))
        boxes.append({"node": j, "weight": weight,
                      "real_midpoint_exact": str(mr.fmpq()), "imag_midpoint_exact": str(mi.fmpq()),
                      "real_radius_exact": str(a.fmpq()), "imag_radius_exact": str(b.fmpq())})
        nominal1 -= weight*(w*ell).real
        nominal2 -= weight*(w2*ell).real
        product = w*log
        old1 -= weight*product.real
        old2 -= 2*weight*(w*product).real
    epsilon1, epsilon2 = cert.moment_errors
    corr.exact_point(epsilon1, "first annular allowance")
    corr.exact_point(epsilon2, "second annular allowance")
    gamma0, s20 = nominal1/(2*base.N), nominal2/base.N
    h = corr.exact_point(gamma0.mid(), "fixed reference h")
    oldp1 = old1/base.N+arb(0, epsilon1)
    oldp2 = old2/base.N+arb(0, epsilon2)
    inherited_endpoint = oldp2/2-(oldp1/2)**2
    prep = {"endpoint_logs_and_nominal_moments_seconds": perf_counter()-started,
            "represented_contour_nodes": base.N, "complex_log_evaluations": len(rows),
            "box_conversion_enlargement": "none: exact dyadic log midpoint/radius",
            "log_boxes_sha256": sha256(json.dumps(boxes, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
            "annular_tail_payment": "same Laurent formulas and radii; log bounds re-enclosed with the common geometry"}
    return corr.Prepared(rows, gamma0, s20, epsilon1, epsilon2, h, boxes, inherited_endpoint, prep)


def assemblies(prepared):
    separate, centered = corr.separate(prepared), corr.correlated(prepared)
    times = {"independent_moments": [], "centered_direct": []}
    orders = []
    for i in range(21):
        check_time()
        order = (("independent_moments", corr.separate), ("centered_direct", corr.correlated))
        if i % 2:
            order = order[::-1]
        orders.append([name for name, _ in order])
        for name, function in order:
            started = perf_counter()
            result = function(prepared)
            times[name].append(perf_counter()-started)
            expected = separate if name == "independent_moments" else centered
            if corr.printable(result) != corr.printable(expected):
                raise RuntimeError("fixed assembly changed during timing diagnostic")
    return separate, centered, {
        "untimed_warmups_per_method": 1, "paired_repetitions": 21,
        "orders": orders, "seconds": times,
        "median_seconds": {name: statistics.median(xs) for name, xs in times.items()},
        "accounting": "full common preparation charged to both; no equal total arithmetic or speed claim",
    }


def full_source_certificate(field, record):
    geometry_started = perf_counter()
    circles, data = ext.geometry(field, record["geometry_attempts"])
    geometry_seconds = perf_counter()-geometry_started
    target_started = perf_counter()
    target = field.circle(q(9, 10), base.N)
    cert = ext.ExtendedCertificate(field, target, circles, data)
    record["geometry"] = cert.geometry_record(data)
    record["count_on_each_boundary"] = 2
    target_seconds = perf_counter()-target_started
    path_started = perf_counter()
    result, attempt = ext.time_pass(cert, 512)
    record["time_attempts"] = [attempt]
    record["whole_interval"] = result
    record["path_seconds"] = perf_counter()-path_started
    record["geometry_seconds"] = geometry_seconds
    record["target_and_tail_setup_seconds"] = target_seconds
    if result is None:
        raise RuntimeError("fixed 512-cell whole-time enclosure failed")
    return cert, result


def monotonicity(result):
    bounds = result["bounds"]
    dlo, dhi = arb(bounds["D"]["lower"]), arb(bounds["D"]["upper"])
    mlo, mhi = arb(bounds["M"]["lower"]), arb(bounds["M"]["upper"])
    gates = {"D_abs_lt_1_over_5": max(abs(dlo), abs(dhi)) < q(1, 5),
             "M_positive": mlo > 0,
             "M_lt_77_over_125": mhi < q(77, 125)}
    return {"identity": "D_t=2-4DM, complete-source Note39 on the full I",
            "gates": gates, "all_gates": all(gates.values()),
            "derivative_lower_strict": "942/625",
            "statistic": "min_I D = D(-3/10000)",
            "scope": "full 512 closed cells; D of either sign allowed in the monotonicity proof"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 224
    record = {
        "request": "VCD-GT-CM-E38-r1", "date": "2026-11-18 America/New_York",
        "prepared_for": "Edward Baker", "llm_assistance": "OpenAI Codex",
        "selected_helper_model": "gpt-6.1-sol", "selected_reasoning_effort": "ultra",
        "serving_attestation": "unavailable; selection is not independent backend attestation",
        "status": "pending separate nonauthor final assessment",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "versions": {"python": platform.python_version(), "platform": platform.platform(),
                     "python_flint": flint.__version__, "flint": flint.__FLINT_VERSION__},
        "source_calls": 0, "bits": 224, "spatial_degree": 32, "time_degree": 32,
        "contour_nodes": 128, "time_interval": ["-3/10000", "1/10"],
        "geometry_schedule": base.GEOMETRY_SCHEDULE, "time_cells": 512,
        "elapsed_cap_seconds": CAP_SECONDS, "local_repair_limit": 2, "local_repairs_used": 2,
        "local_repairs": [
            "Reuse existing endpoint log boxes for old direct interval; remove redundant 65-log integration, no source/mathematical budget change",
            "Record actual duplicate log evaluations inside inherited full-F consumer and decompose existing centered width; no formula/source/target change",
        ],
        "first_successful_attempt": {
            "script_sha256": "89d1e3c1c0f4a8da1db9b93802ece3bd7f233757750f379ea98fd74289240a40",
            "record_sha256": "21a837e286f4d709d2fb2ebc76cb20eb48ebd43a5475c316e049b618a102ea4d",
            "reading_copy": "/private/tmp/vcd-gt-cm-E38-primary-20261118.json",
            "all_mathematical_gates_passed": True,
            "centered_width_upper_summary": "2.29767332903e-8",
            "width_factor_gain_summary": "33.9494266997",
            "elapsed_seconds": 1.4826946670073085,
        },
        "archive": {"name": base.ARCHIVE, "stored_sha256": base.STORED_SHA256,
                    "content_sha256": base.CONTENT_SHA256},
        "canonical": {"geometry_attempts": []}, "quadratic_control": {"geometry_attempts": []},
    }
    exit_code = 0
    try:
        started = perf_counter()
        record["verified_frozen_inputs"] = verify_inputs()
        record["verified_inherited_source_inputs"] = ext.check_pins()
        record["input_validation_seconds"] = perf_counter()-started
        old_record = json.loads(RECORD19_PATH.read_text())
        if not old_record["success"] or old_record["script_sha256"] != CORRELATION_HASH:
            raise RuntimeError("inconsistent Record19 centered baseline")
        common_started = perf_counter()
        started = perf_counter()
        samples = base.archived_fields(args.cache_dir)
        archive_seconds = perf_counter()-started
        started = perf_counter()
        coefficients, sample_radius = base.tensor_coefficients(samples)
        error, source_error, ts, ds, error_record = cardinal_error(sample_radius)
        reconstruction_seconds = perf_counter()-started
        audit = coefficient_audit(coefficients, ts)
        started = perf_counter()
        field = ext.ExtendedField(coefficients, error, ts, ds)
        field_seconds = perf_counter()-started
        canonical = record["canonical"]
        canonical["source_error"] = error_record
        canonical["coefficient_arithmetic"] = audit
        cert, path_result = full_source_certificate(field, canonical)
        canonical["whole_time_monotonicity"] = monotonicity(path_result)
        prepared = prepare(cert, -q(3, 10000))
        common_seconds = perf_counter()-common_started
        separate, centered, timing = assemblies(prepared)
        baseline = old_record["canonical"]["correlated"]
        old_width = arb(baseline["upper"])-arb(baseline["lower"])
        sep_width = separate["width"]
        ratio = centered["width_upper"]/old_width
        residual_ratio = centered["width_upper"]/sep_width
        annular_support = prepared.epsilon2/2+abs(centered["h"])*prepared.epsilon1
        log_support = centered["R_h"]-annular_support
        square_width = centered["square_upper"]-centered["square_lower"]
        gates = {
            "tenfold_narrower_than_Record19_centered": centered["width_upper"] <= old_width.lower()/10,
            "above_fixed_D_stop": centered["lower"] > q(1, 10000),
            "centered_no_wider_than_new_independent": centered["width_upper"] <= sep_width.lower(),
            "full_time_source_and_geometry_gates": path_result["all_gates"],
            "full_time_monotonicity_gates": canonical["whole_time_monotonicity"]["all_gates"],
        }
        canonical.update({
            "source_preparation": {"archive_load_hash_check_seconds": archive_seconds,
                                   "polynomial_and_error_reconstruction_seconds": reconstruction_seconds,
                                   "coefficient_audit_seconds": audit["seconds"],
                                   "field_construction_seconds": field_seconds,
                                   "geometry_seconds": canonical["geometry_seconds"],
                                   "target_and_tail_setup_seconds": canonical["target_and_tail_setup_seconds"],
                                   "whole_time_path_seconds": canonical["path_seconds"],
                                   "endpoint_preparation": prepared.preparation_record,
                                   "total_common_seconds": common_seconds},
            "source_error_at_archived_endpoint_unchanged": str(source_error),
            "log_rectangles": prepared.boxes,
            "nominal_gamma0": str(prepared.gamma0), "nominal_half_p2": str(prepared.s20),
            "epsilon1": str(prepared.epsilon1), "epsilon2": str(prepared.epsilon2),
            "reference_h_exact": str(prepared.h.fmpq()),
            "independent_moments": corr.printable(separate), "centered_direct": corr.printable(centered),
            "Record19_centered_baseline": {"lower": baseline["lower"], "upper": baseline["upper"],
                                          "width": str(old_width),
                                          "source_error": old_record["canonical"]["extended_source_error"]["uniform_extended_disk_error_upper"]},
            "width_ratio_to_Record19_centered": str(ratio),
            "width_reduction_percent_source_accounting_vs_Record19_centered": str(100*(1-ratio)),
            "width_factor_gain_vs_Record19_centered": str(old_width/centered["width_upper"]),
            "residual_centered_width_ratio_to_new_independent": str(residual_ratio),
            "residual_centered_width_reduction_percent": str(100*(1-residual_ratio)),
            "centered_width_decomposition": {
                "twice_log_rectangle_support": str(2*log_support),
                "twice_annular_tail_support": str(2*annular_support),
                "shifted_square_range_width": str(square_width),
                "log_fraction_of_width": str(2*log_support/centered["width_upper"]),
                "annular_fraction_of_width": str(2*annular_support/centered["width_upper"]),
                "nominal_and_endpoint_rounding": "remaining outward arithmetic, enclosed in the reported full width",
                "scope": "decomposition of existing R_h and tail data; no new source acquisition",
            },
            "gates": gates, "all_gates": all(gates.values()), "assembly_timing": timing,
            "assembly_work": {"both": "same source, geometry, 65 log rectangles, two support sums and annular errors",
                              "independent": "w and w^2 kernels, Cartesian square range",
                              "centered": "w and w^2-h*w kernels, full shifted square range",
                              "claim": "source-accounting width gain; no equality of total cost or recursive advantage"},
        })
        control_started = perf_counter()
        control = record["quadratic_control"]
        cfield = ext.ExtendedField(base.quadratic_coefficients(), arb(0), ts, ds)
        ccert, cpath = full_source_certificate(cfield, control)
        cprepared = prepare(ccert, q(1, 20))
        csep, ccorr = corr.separate(cprepared), corr.correlated(cprepared)
        collision = ext.endpoint(ccert, q(1, 20))
        collision_retained = (csep["lower"].lower() <= 0 <= csep["upper"].upper()
                              and ccorr["lower"] <= 0 <= ccorr["upper"]
                              and collision[1].contains(0) and collision[3].contains(0))
        strict_gates_fail = (not cpath["gates"]["D_gt_1_over_10000"]
                             and not cpath["gates"]["F_ge_3_over_10"])
        control.update({"time": "1/20", "exact_D": 0, "exact_F": 0,
                        "endpoint_preparation": cprepared.preparation_record,
                        "independent_moments": corr.printable(csep), "centered_direct": corr.printable(ccorr),
                        "collision_time": ext.describe(collision),
                        "retains_collision": collision_retained, "strict_path_gates_fail": strict_gates_fail,
                        "success": collision_retained and strict_gates_fail,
                        "seconds": perf_counter()-control_started})
        record["complex_log_work"] = {
            "represented_contour_nodes": 128, "shared_rectangles_per_endpoint": 65,
            "inherited_full_F_log_passes_per_time_cell": 2,
            "canonical_and_control_path_log_evaluations": 2*512*2*65,
            "two_shared_endpoint_preparation_log_evaluations": 2*65,
            "separate_quadratic_collision_consumer_log_evaluations": 2*65,
            "total_actual_complex_log_evaluations": 2*512*2*65+2*65+2*65,
            "accounting": "all inherited duplicate evaluations included; assemblies use prepared boxes and evaluate no new logs",
        }
        record["success"] = all(gates.values()) and control["success"]
        if not record["success"]:
            exit_code = 1
    except Exception as exc:
        record["success"] = False
        record["failure"] = type(exc).__name__+": "+str(exc)
        exit_code = 1
    record["elapsed_seconds"] = perf_counter()-START
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"output": str(args.output), "success": record["success"],
                      "failure": record.get("failure"), "elapsed_seconds": record["elapsed_seconds"]}))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
