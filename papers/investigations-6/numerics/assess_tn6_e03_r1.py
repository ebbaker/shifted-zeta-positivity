#!/usr/bin/env python3
"""Check the TN6-E02 r1 endpoint ledger and compare its one E03 replay.

Run with ordinary Python and pass the separately generated replay JSON,
optionally with the outer watchdog receipt. This script launches no generator.
Prepared 2026-11-14 for Edward Baker with OpenAI Codex LLM assistance.
Dispatch gpt-6.1-sol / ultra; independent runtime attestation unavailable.
"""

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial, isclose
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
E03_MANIFEST = "10_TN6_E03_R1_INPUT_MANIFEST_20261114.json"
E02_MANIFEST = "08_TN6_E02_R1_INPUT_MANIFEST_20261114.json"
ORIGINAL = HERE / "09_TN6_E02_R1_CERTIFICATE_20261114.json"
MANIFESTS = (
    (E03_MANIFEST, "2270c45b826e3c73b459d2b176b7333252fa680d81eaa9ff98820ac822769778", 7),
    (E02_MANIFEST, "48727341987b33e7ebe0f9c3914142d4d653085276ce21479682561e241bc0f2", 22),
)
PANELS = [["0", "1/2"], ["1/2", "1"], ["1", "3/2"], ["3/2", "2"]]
POINTS = [[t, x] for t in ("0", "1/4", "1/2") for x in (0, 4, 8)]
CAPS = {
    "truncation_Q": F("5e-9"), "acquisition_9delta": F("2e-9"),
    "normalization_eta_Z": F("1e-9"), "each_chain_rounding": F("1e-9"),
    "each_chain_total": F("1e-8"), "each_direct_radius": F("1e-9"),
}
S16 = sum(F(8**(32 - 2*k), 2**k * factorial(k) * factorial(32 - 2*k))
          for k in range(17))


def require(condition, label):
    if not condition:
        raise ValueError(label)


def verify_manifest(name, digest, count):
    data = (HERE / name).read_bytes()
    require(sha256(data).hexdigest() == digest, name)
    entries = json.loads(data)["inputs"]
    require(len(entries) == count == len({e["path"] for e in entries}), name)
    for entry in entries:
        source = (ROOT / entry["path"]).read_bytes()
        require((len(source), sha256(source).hexdigest()) ==
                (entry["bytes"], entry["sha256"]), entry["path"])
    return {"path": str((HERE / name).relative_to(ROOT)), "bytes": len(data),
            "sha256": digest, "verified_inputs": entries}


def ends(ball):
    return tuple(map(F, ball["endpoints"]))


def contains(outer, inner, label):
    require(outer[0] <= inner[0] <= inner[1] <= outer[1], label)


def balls(node):
    if isinstance(node, dict):
        if {"endpoints", "midpoint", "radius"} <= node.keys():
            yield node
        for item in node.values():
            yield from balls(item)
    elif isinstance(node, list):
        for item in node:
            yield from balls(item)


def add_panels(ops, quantity):
    require([op["panel"] for op in ops] == PANELS, quantity)
    require(all(op["quantity"] == quantity for op in ops), quantity)
    return tuple(map(sum, zip(*(ends(op["enclosure"]["real"]) for op in ops))))


def check_attempt(a, p, expected_callbacks, start):
    passing = p == 256
    require(a["status"] == ("complete pass" if passing else "precision gate failed"), p)
    require(F(a["requested_abs_and_rel_tolerance"]) == F(1, 2**(p - 32)), p)
    require(a["start_callbacks"] == start and a["start_modes"] == 8*start, p)
    sections = (("integrations", 104 if passing else 68, 15),
                ("matrix_exponentials", 9 if passing else 0, 30))
    callback_total = start
    after_moments = start + sum(op["source_callbacks"] for op in a["integrations"][:68])
    for section, count, wall_limit in sections:
        require(len(a[section]) == count, (p, section))
        for i, op in enumerate(a[section]):
            expected_start = callback_total if section == "integrations" else after_moments
            require((op["start_callbacks"], op["start_modes"]) ==
                    (expected_start, 8*expected_start), (p, section, i, "counter start"))
            nz = op["source_callbacks"]
            require(nz > 0 if section == "integrations" else nz == 0, (p, section, i))
            require(op["finite_mode_evaluations"] == 8*nz, (p, section, i, "modes"))
            require(op["status"] == "returned" and 0 <= op["wall_seconds"] <= wall_limit,
                    (p, section, i, "operation time"))
            name = "enclosure" if section == "integrations" else "matrix_entry"
            contains(ends(op[name]["imag"]), (0, 0), (p, section, i, "reality"))
            callback_total += nz
    require(callback_total - start == expected_callbacks == a["source_callbacks"] < 400000
            and a["finite_mode_evaluations"] == 8*expected_callbacks, (p, "callbacks"))

    arithmetic = list(map(F, a["tails"]["omitted_arithmetic_upper_by_even_degree"]))
    spatial = F(a["tails"]["spatial_upper_all_even_degrees"])
    tail = F(a["tails"]["direct_symmetric_radius"])
    require(len(arithmetic) == 17 and arithmetic[0] > 0 and spatial > 0 and
            all(v == arithmetic[0] * 4**k for k, v in enumerate(arithmetic)) and
            2*tail == arithmetic[0] + spatial, (p, "tail scale"))
    require([m["degree"] for m in a["moments"]] == list(range(0, 33, 2)), p)
    moments = {m["degree"]: ends(m) for m in a["moments"]}
    for k, upper in enumerate(arithmetic):
        lo, hi = add_panels(a["integrations"][4*k:4*k+4], {"moment_degree": 2*k})
        contains(moments[2*k], (2*lo, 2*hi + upper + spatial), (p, 2*k, "moment"))
        require(moments[2*k][0] > 0, (p, 2*k, "positive moment"))

    require([h["degree"] for h in a["pivots"]] ==
            list(range(0, 17, 2)) + list(range(1, 16, 2)), p)
    pivots = {h["degree"]: ends(h) for h in a["pivots"]}
    for h in a["pivots"]:
        n = h["degree"]
        lo, hi = pivots[n]
        mlo, mhi = moments[2*n]
        require(h["positive"] is True and lo > 0, (p, n, "positive pivot"))
        require(F(h["relative_radius_to_midpoint"]) == F(h["radius"])/F(h["midpoint"]),
                (p, n, "relative pivot radius"))
        contains(ends(h["norm_to_diagonal"]), (lo/mhi, hi/mlo), (p, n, "norm ratio"))
    require(set(a["scaled_condition"]) == {"0", "1"}, (p, "condition blocks"))
    for block in a["scaled_condition"].values():
        require(block["status"] == "enclosed" and F(block["kappa_inf_upper"]) ==
                F(block["norm_inf_upper"]) * F(block["inverse_norm_inf_upper"]),
                (p, "condition upper bound"))

    coeff = a["couplings"]
    require([c["edge"] for c in coeff] == list(range(1, 17)), p)
    for n, coupling in enumerate(coeff, 1):
        lo, hi = ends(coupling)
        require(lo > 0, (p, n, "positive coupling"))
        contains((lo**2, hi**2), (pivots[n][0]/pivots[n-1][1],
                                  pivots[n][1]/pivots[n-1][0]), (p, n, "coupling ratio"))
    mass = a["normalization"]
    ml, mu = ends(mass)
    require((ml, mu) == pivots[0] == moments[0], (p, "raw mass"))
    ratio = ends(a["norm16_div_mass"])
    contains(ratio, (pivots[16][0]/mu, pivots[16][1]/ml), (p, "omitted edge norm"))
    pads = [F(0)] + [F(c["radius"]) for c in coeff[:15]] + [F(0)]
    row_sums = [left+right for left, right in zip(pads, pads[1:])]
    delta = max(row_sums)
    gate = {"truncation_Q": ratio[1] * S16, "acquisition_9delta": 9*delta,
            "normalization_eta_Z": F(mass["radius"])/ml}
    ideal = sum(gate.values())
    phys = ideal * mu / 2
    expected = gate | {"sum": ideal, "physical_absolute_upper": phys, "S16": S16, "delta": delta}
    require(expected == {k: F(v) for k, v in a["uniform_error"].items()}, (p, "uniform ledger"))
    require([k for k, value in gate.items() if value > CAPS[k]] ==
            ([] if passing else ["acquisition_9delta"]), (p, "frozen gate"))
    if passing:
        require("failure" not in a and ideal < F("1.515e-25"), (p, "pass"))
    else:
        require(a["failure"] == "acquisition_9delta exceeds its normalized allowance",
                (p, "recorded failure"))
    samples = a["chain_samples"]
    direct = a["direct_samples"]
    for group in (a["matrix_exponentials"], samples, direct):
        require([s["point"] for s in group] == (POINTS if passing else []), (p, "point order"))

    rounding, totals, radii, differences = [], [], [], []
    for i, (m, c, d) in enumerate(zip(a["matrix_exponentials"], samples, direct)):
        point = POINTS[i]
        mlo, mhi = ends(m["matrix_entry"]["real"])
        scale = F(mass["midpoint"])/2
        cball = c["nominal_physical_ball"]
        cl, cu = ends(cball)
        contains((cl, cu), (mlo*scale, mhi*scale), (point, "matrix scale"))
        k = F(cball["midpoint"])
        num = 2*F(cball["radius"])/ml
        field = (cl-phys, cu+phys)
        require(F(c["normalized_numerical_error"]) == num <= CAPS["each_chain_rounding"] and
                F(c["normalized_total"]) == ideal+num <= CAPS["each_chain_total"] and
                ideal+num < F("1.515e-25") and
                tuple(map(F, c["physical_field_enclosure"])) == field, (point, "sample ledger"))
        rball = d["retained_physical_ball"]
        rlo, rhi = ends(rball)
        l, u = ends(d["complete_physical_ball"])
        contains((rlo, rhi), add_panels(a["integrations"][68+4*i:72+4*i],
                                        {"direct_sample": point}), (point, "direct panels"))
        contains((l, u), (rlo-tail, rhi+tail), (point, "direct tails"))
        radius = 2*F(d["complete_physical_ball"]["radius"])/ml
        diff = (cl-u, cu-l)
        require(F(d["normalized_radius"]) == radius <= CAPS["each_direct_radius"] and
                d["overlap_with_enlarged_chain"] is True and
                max(l, field[0]) <= min(u, field[1]) and
                tuple(map(F, d["nominal_minus_direct_physical_interval"])) == diff and
                tuple(map(F, d["computed_midpoint_minus_direct_physical_interval"])) == (k-u, k-l),
                (point, "overlap and differences"))
        rounding.append(num)
        totals.append(ideal+num)
        radii.append(radius)
        differences.append(max(map(abs, diff)))

    receipt = {"precision_bits": p, "status": a["status"], "couplings_positive": len(coeff),
               "pivots_positive": len(pivots), "max_radius_internal_row_zero_based": row_sums.index(delta),
               "uniform_error_exact": a["uniform_error"], "callbacks": expected_callbacks,
               "finite_mode_evaluations": 8*expected_callbacks, "integral_calls": len(a["integrations"]),
               "matrix_exponentials": len(samples), "attempt_wall_seconds": a["wall_seconds"],
               "max_integral_call_seconds": max(op["wall_seconds"] for op in a["integrations"])}
    if passing:
        require(max(rounding) < F("1.740e-77") and max(radii) < F("3.812e-68") and
                max(differences) < F("7.771e-27"), "rounded bounds quoted in E02")
        receipt.update(nine_chain_total_max_exact=str(max(totals)),
                       nine_chain_rounding_max_exact=str(max(rounding)),
                       nine_direct_radius_max_exact=str(max(radii)),
                       nine_abs_nominal_minus_direct_max_exact=str(max(differences)),
                       max_difference_point=POINTS[differences.index(max(differences))],
                       max_matrix_exponential_seconds=max(op["wall_seconds"]
                                                          for op in a["matrix_exponentials"]))
    return receipt


def check_record(record, pinned):
    require(record["all_manifest_sources_verified"] == pinned, "E02 reported manifest entries")
    cfg = record["parameters"]
    require(cfg == {
        "sites": 16, "cutoff_U": 2, "mode_count_M": 8, "panels": PANELS, "points": POINTS,
        "precision_ladder_bits": [128, 256, 512], "normalized_caps": {k: str(v) for k, v in CAPS.items()},
        "integration_limits": {"deg_limit": 64, "eval_limit": 8000, "depth_limit": 20},
        "source_limits": {"callbacks_per_attempt": 400000, "callbacks_total": 800000},
        "wall_limits_seconds": {"total": 900, "per_integral": 15, "per_matrix_exponential": 30},
    }, "frozen parameters")
    endpoints = list(balls(record))
    require(len(endpoints) == 527, "endpoint count")
    for ball in endpoints:
        m, r = F(ball["midpoint"]), F(ball["radius"])
        require(r >= 0 and ends(ball) == (m-r, m+r), "endpoint reconstruction")
        require(all(q.denominator.bit_count() == 1 for q in (m, r)), "dyadic precision")
    first, second = record["attempts"]
    require([first["precision_bits"], second["precision_bits"]] == [128, 256], "attempt order")
    outcomes = [check_attempt(first, 128, 4384, 0), check_attempt(second, 256, 15636, 4384)]

    run = record["process_execution"]
    require(record["outcome"] == "complete pass" and run["implementation_correction_pass"] == 0 and
            run["worker_exit_code"] == 0 and run["watchdog_return_overshoot"] is None and
            run["source_callbacks"] == 20020 < 800000 and run["finite_mode_evaluations"] == 160160 and
            0 < run["numerical_process_wall_seconds"] < 900, "end-to-end work gates")
    acc = first["phase_wall_seconds"]["acquisition"] + second["phase_wall_seconds"]["acquisition"]
    chain = second["phase_wall_seconds"]["chain_readouts"]
    direct = second["phase_wall_seconds"]["direct_baseline"]
    require(set(first["phase_wall_seconds"]) == {"acquisition"} and
            set(second["phase_wall_seconds"]) == {"acquisition", "chain_readouts", "direct_baseline"} and
            all(0 < sum(a["phase_wall_seconds"].values()) < a["wall_seconds"] for a in (first, second)) and
            sum(a["wall_seconds"] for a in (first, second)) < run["numerical_process_wall_seconds"],
            "timing hierarchy")
    require(record["costs"]["wall_seconds_by_phase_including_attempts"] ==
            {"acquisition": acc, "chain_readouts": chain, "direct_baseline": direct}, "phase costs")
    expected_costs = {
        "successful_first_use_chain_acquisition_plus_exponential_seconds":
            second["phase_wall_seconds"]["acquisition"] + second["matrix_exponentials"][0]["wall_seconds"],
        "successful_first_use_direct_integral_calls_seconds":
            sum(op["wall_seconds"] for op in second["integrations"][68:72]),
        "chain_setup_plus_nine_seconds_including_attempts": acc + chain,
        "chain_amortized_per_point_seconds_including_attempts": (acc+chain)/9,
        "direct_nine_seconds_including_attempts": direct,
        "direct_amortized_per_point_seconds_including_attempts": direct/9,
    }
    for key, value in expected_costs.items():
        require(isclose(record["costs"][key], value, rel_tol=1e-12), key)
    return {"endpoint_triples_checked": len(endpoints), "attempts": outcomes,
            "runtime": record["runtime"], "process_execution": run.copy(), "costs": record["costs"]}


def payload(record):
    """Drop only the observed run-specific timing fields and cost sums."""
    del record["costs"]
    for key in ("started_utc", "finished_utc", "numerical_process_wall_seconds"):
        del record["process_execution"][key]
    for attempt in record["attempts"]:
        for key in ("wall_seconds", "start_monotonic_seconds", "phase_wall_seconds"):
            del attempt[key]
        for field in ("integrations", "matrix_exponentials"):
            for operation in attempt[field]:
                del operation["wall_seconds"]
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("replay", type=Path, help="Previously generated, separate JSON")
    parser.add_argument("--outer-receipt", type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    manifests = [verify_manifest(*item) for item in MANIFESTS]
    require(not args.replay.samefile(ORIGINAL), "replay must be separate from original")
    run_data = [p.read_bytes() for p in (ORIGINAL, args.replay)]
    records = [json.loads(data) for data in run_data]
    checked = [check_record(r, manifests[1]["verified_inputs"]) for r in records]
    left, right = (payload(r) for r in records)
    require(left == right, "exact scientific payload, count or gate difference")
    encoded = json.dumps(left, sort_keys=True, separators=(",", ":")).encode()
    outer = json.loads(args.outer_receipt.read_bytes()) if args.outer_receipt else None
    if outer is not None:
        require(outer["process_group_watchdog"] is True and outer["timed_out"] is False and
                outer["exit_code"] == 0 and outer["outer_limit_seconds"] == 60 and
                checked[1]["process_execution"]["numerical_process_wall_seconds"] <=
                outer["outer_seconds"] < 60, "E03 outer process-group limit")
    elapsed = time.monotonic() - start
    receipt = dict(
        task="TN6-E03", revision="r1", date="2026-11-14", timezone="America/New_York",
        intended_author="Edward Baker", assistance="OpenAI Codex LLM",
        worker_dispatch={"model": "gpt-6.1-sol", "effort": "ultra"},
        independent_backend_or_effort_attestation="unavailable",
        disposition="Accepted as a finite certificate at the issued scope.",
        reviewed_E02_status="Complete pass at 256 bits, certified within the issued execution scope.",
        verified_manifests=manifests,
        original=checked[0] | {"path": str(ORIGINAL.relative_to(ROOT)),
                               "sha256": sha256(run_data[0]).hexdigest(), "bytes": len(run_data[0])},
        replay=checked[1] | {"sha256": sha256(run_data[1]).hexdigest(), "bytes": len(run_data[1]),
                             "outer_watchdog": outer, "full_generator_replays": 1},
        exact_payload_comparison={"equal": True, "canonical_sha256": sha256(encoded).hexdigest(),
                                  "removed_fields": ["process timestamps and wall time",
                                                     "attempt start and elapsed phase and operation times",
                                                     "derived timing costs"]},
        exact_rational_validator_wall_seconds=elapsed,
        validator_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        response_checks_used=0,
    )
    print(json.dumps(receipt, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
