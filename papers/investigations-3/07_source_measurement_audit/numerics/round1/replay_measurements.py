#!/usr/bin/env python3
"""Independent bounded source-jet and finite-measurement replay.

Prepared for Edward Baker, 16 October 2026. Substantial LLM assistance:
gpt-6.1-sol (Codex), reasoning effort ultra, as recorded by the parent task.
Requires mpmath. Floating quadrature error estimates are diagnostics, not
certificates; omitted coefficient and integral tails use explicit bounds.
No imported original solver and no normal equations are used.
"""

import argparse
import hashlib
import json
import platform
import time
from pathlib import Path

import mpmath as mp


CASES = (
    ("t0_x30", "0", "30"),
    ("t0_x44_1303", "0", "44.1303"),
    ("t025_x44_1303", "0.25", "44.1303"),
    ("t0_x60", "0", "60"),
    ("t0_x70", "0", "70"),
    ("t0_x85", "0", "85"),
)
BREAKS = ("0", "0.0125", "0.025", "0.05", "0.1", "0.2", "0.4", "0.8", "1.8")
THETA_TERMS = 10


def fmt(x):
    return mp.nstr(x, mp.mp.dps, strip_zeros=False)


def serialize(obj):
    if isinstance(obj, dict):
        return {str(k): serialize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [serialize(v) for v in obj]
    if isinstance(obj, mp.matrix):
        return [[fmt(obj[i, j]) for j in range(obj.cols)] for i in range(obj.rows)]
    if isinstance(obj, mp.mpf):
        return fmt(obj)
    return obj


def phi(n, u):
    q = mp.pi * n * n * mp.exp(4 * u)
    return mp.exp(u - q) * (2 * q * q - 3 * q)


def beta_values(n=6):
    return [mp.exp(-mp.pi * j * j) * (4 * mp.pi * j * j - 1) for j in range(1, n + 1)]


def tail_bound(start_n, lower_u, moment):
    """Bound all n>=start_n, u>=lower_u, for t<=1/4 and moment k=0,1.

    Use u^k <= exp(k*u), ((k+1)u+u^2/4) <= (k+1)exp(4u)/4,
    |phi_n| <= 2exp(u)q_n^2 exp(-q_n), and integrate q_n.
    With a=1-(k+1)/(4*pi*n^2), a>=a_N, the first term majorant
    is ((Q/(2*a_N)) + 1/(2*a_N^2))*exp((k+1)*exp(4U)/4-Q).
    The n-tail is geometric with ratio at most ((N+1)/N)^2
    exp(-pi*exp(4U)*(2N+1)).
    """
    n = mp.mpf(start_n)
    u = mp.mpf(lower_u)
    scale = mp.exp(4 * u)
    a = 1 - (moment + 1) / (4 * mp.pi * n * n)
    q = mp.pi * n * n * scale
    first = (q / (2 * a) + 1 / (2 * a * a)) * mp.exp((moment + 1) * scale / 4 - q)
    ratio = ((n + 1) / n) ** 2 * mp.exp(-mp.pi * scale * (2 * n + 1))
    return first / (1 - ratio)


def integrate_modes(t, x, modes):
    breaks = [mp.mpf(v) for v in BREAKS]

    def integrand(u):
        source = mp.fsum(phi(n, u) for n in modes)
        return mp.exp(t * u * u) * source * mp.mpc(mp.cos(x * u), -u * mp.sin(x * u))

    value, heuristic = mp.quad(integrand, breaks, method="tanh-sinh", error=True)
    return [value.real, value.imag], heuristic


def xi_jet(x):
    def baseline(y):
        s = (1 + 1j * y) / 2
        return (s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s) / 16).real

    return [baseline(x), mp.diff(baseline, x)]


def evaluate(dps, output):
    mp.mp.dps = dps
    started = time.monotonic()
    result = {
        "schema": "source_measurement_evaluation_v1",
        "status": "floating TS evaluation with analytic coefficient/integral tail bounds; quadrature not certified",
        "dps": dps,
        "python": platform.python_version(),
        "mpmath": mp.__version__,
        "beta": beta_values(),
        "theta_terms": THETA_TERMS,
        "quadrature_breakpoints": list(BREAKS),
        "cases": [],
    }
    for name, ts, xs in CASES:
        case_start = time.monotonic()
        t, x = mp.mpf(ts), mp.mpf(xs)
        values, heuristics = [], []
        for n in range(1, 7):
            val, err = integrate_modes(t, x, [n])
            values.append(val)
            heuristics.append(err)
        theta_tail, tail_heuristic = integrate_modes(t, x, range(7, THETA_TERMS + 1))
        h = [mp.fsum(val[k] for val in values) + theta_tail[k] for k in range(2)]
        case = {
            "id": name,
            "t": ts,
            "x": xs,
            "B": [[v[k] for v in values] for k in range(2)],
            "h": h,
            "theta_tail_after_6": theta_tail,
            "bounds": {
                "theta_coefficient_tail_n_ge_11": [tail_bound(THETA_TERMS + 1, 0, k) for k in range(2)],
                "integral_tail_u_ge_1_8_all_modes": [tail_bound(1, mp.mpf(BREAKS[-1]), k) for k in range(2)],
                "quadrature_heuristic_mode_errors": heuristics,
                "quadrature_heuristic_theta_tail_error": tail_heuristic,
                "quadrature_status": "mpmath heuristic estimate only; precision agreement is not a certificate",
            },
            "wall_seconds": time.monotonic() - case_start,
        }
        if t == 0:
            exact = xi_jet(x)
            case["time_zero_xi_check"] = {
                "formula": "xi((1+i*x)/2)/8 and physical x derivative",
                "xi_jet": exact,
                "absolute_differences": [abs(h[k] - exact[k]) for k in range(2)],
            }
        result["cases"].append(case)
        result["wall_seconds"] = time.monotonic() - started
        Path(output).write_text(json.dumps(serialize(result), indent=2) + "\n")
        print(json.dumps({"stage": "evaluation", "dps": dps, "case": name, "h": serialize(h), "wall_seconds": case["wall_seconds"]}), flush=True)
    return result


def tangent_basis(beta, anchor):
    pivot = 1 if anchor else 0
    indices = range(pivot + 1, 6)
    q = mp.zeros(6, 5 - int(anchor))
    for j, node in enumerate(indices):
        q[node, j] = 1
        q[pivot, j] = -beta[node] / beta[pivot]
    return q


def measurement_matrix(name):
    if name == "recurrence":
        return mp.matrix([[int(j == k - 1) - 2 * int(j == k) + int(j == k + 1) for j in range(1, 7)] for k in range(1, 8)])
    return mp.matrix([[phi(n, mp.mpf(j) / 20) - phi(n, -mp.mpf(j) / 20) for n in range(1, 7)] for j in range(1, 13)])


def conditioning(evaluation, output):
    dps = evaluation["dps"]
    mp.mp.dps = dps
    beta = [mp.mpf(v) for v in evaluation["beta"]]
    records = []
    for case in evaluation["cases"]:
        b = mp.matrix(case["B"])
        h = mp.matrix(case["h"])
        for anchor in (False, True):
            q = tangent_basis(beta, anchor)
            for name in ("recurrence", "reflection"):
                m = measurement_matrix(name)
                # mpmath.qr returns a full orthogonal factor. Select thin rows.
                u_full, r_full = mp.qr(m * q)
                r = r_full[:q.cols, :]
                u = u_full[:, :q.cols]
                # A=BQ R^{-1}; use back substitution via lu_solve on the
                # transpose, rather than inverse or normal equations.
                bq = b * q
                a = mp.matrix([list(mp.lu_solve(r.T, bq[k, :].T)) for k in range(2)])
                left, singular, right = mp.svd_r(a)
                rotated = left.T * h
                solution_y = -right.T * mp.matrix([rotated[k] / singular[k] for k in range(2)])
                coeff = q * mp.lu_solve(r, solution_y)
                c = singular[0]
                eta = mp.norm(h) / c
                distance = mp.norm(solution_y)
                residual = b * coeff + h
                norm_residual = mp.fsum(beta[k] * coeff[k] for k in range(6))
                records.append({
                    "case": case["id"], "anchor": anchor, "measurement": name,
                    "tangent_dimension": q.cols, "measurement_rows": m.rows,
                    "C": c, "eta_sufficient_exclusion_radius": eta,
                    "actual_equality_measurement_distance": distance,
                    "distance_over_eta": distance / eta,
                    "singular_values_A": list(singular),
                    "singular_ratio": singular[0] / singular[1],
                    "equality_minimizer_coeff_delta": list(coeff),
                    "minimum_source_coefficient": min(1 + v for v in coeff),
                    "jet_residual": list(residual),
                    "primitive_normalization_residual": norm_residual,
                    "anchor_residual": coeff[0] if anchor else None,
                    "measurement_norm_check": mp.norm(m * coeff),
                    "thin_QR_residual_frobenius": mp.norm(m * q - u * r),
                    "linear_algebra_status": "floating QR and SVD; full row rank observed without a rank cutoff",
                })
    result = {"schema": "source_measurement_conditioning_v1", "dps": dps, "status": "floating conditioning and equality distances; error propagation requires external certificate", "records": records}
    Path(output).write_text(json.dumps(serialize(result), indent=2) + "\n")
    return result


def compare_precision(output_dir, original_record=None):
    """One fixed 80/120 comparison; deliberately not an error certificate."""
    mp.mp.dps = 140
    paths = [output_dir / f"EVALUATION_DPS{dps}.json" for dps in (80, 120)]
    if not all(path.exists() for path in paths):
        return
    low, high = [json.loads(path.read_text()) for path in paths]
    comparison = {"schema": "source_measurement_comparison_v1", "status": "precision and original-record diagnostics, not quadrature or solve certificates", "source_code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "evaluation_file_sha256": {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}, "cases": [], "conditioning": []}
    original = json.loads(Path(original_record).read_text()) if original_record else None
    for i, (a, b) in enumerate(zip(low["cases"], high["cases"])):
        record = {"case": a["id"], "B_max_abs_80_vs_120": max(abs(mp.mpf(a["B"][k][j]) - mp.mpf(b["B"][k][j])) for k in range(2) for j in range(6)), "h_abs_80_vs_120": [abs(mp.mpf(a["h"][k]) - mp.mpf(b["h"][k])) for k in range(2)], "h_relative_l2_80_vs_120": mp.norm(mp.matrix(a["h"]) - mp.matrix(b["h"])) / mp.norm(mp.matrix(b["h"]))}
        if original:
            old = original["B_measurement_conditioning"]["rows"][i]
            original_h = mp.matrix([mp.mpf(str(v)) for v in old["jet_h"]])
            record["h_abs_original_vs_120"] = list(abs(original_h[k] - mp.mpf(b["h"][k])) for k in range(2))
            record["h_relative_l2_original_vs_120"] = mp.norm(original_h - mp.matrix(b["h"])) / mp.norm(mp.matrix(b["h"]))
        comparison["cases"].append(record)
    cpaths = [output_dir / f"CONDITIONING_DPS{dps}.json" for dps in (80, 120)]
    if all(path.exists() for path in cpaths):
        clow, chigh = [json.loads(path.read_text()) for path in cpaths]
        for a, b in zip(clow["records"], chigh["records"]):
            record = {key: a[key] for key in ("case", "anchor", "measurement")}
            for key in ("C", "eta_sufficient_exclusion_radius", "actual_equality_measurement_distance", "distance_over_eta"):
                record[key + "_relative_80_vs_120"] = abs(mp.mpf(a[key]) / mp.mpf(b[key]) - 1)
            if original:
                i = next(i for i, case in enumerate(high["cases"]) if case["id"] == a["case"])
                old = original["B_measurement_conditioning"]["rows"][i]["anchored" if a["anchor"] else "unanchored"]
                for key, oldkey in (("C", "C_" + a["measurement"]), ("eta_sufficient_exclusion_radius", "eta_" + a["measurement"])):
                    record[key + "_relative_original_vs_120"] = abs(mp.mpf(str(old[oldkey])) / mp.mpf(b[key]) - 1)
            comparison["conditioning"].append(record)
    if original:
        comparison["original_record_sha256"] = hashlib.sha256(Path(original_record).read_bytes()).hexdigest()
        comparison["original_record_basename"] = Path(original_record).name
    (output_dir / "PRECISION_AND_ORIGINAL_COMPARISON.json").write_text(json.dumps(serialize(comparison), indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, choices=(80, 120), required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("."))
    parser.add_argument("--conditioning-only", action="store_true")
    parser.add_argument("--compare-record", type=Path, help="Optional original JSON; read only after independent implementation and evaluation")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    evaluation_path = args.output_dir / f"EVALUATION_DPS{args.dps}.json"
    if args.conditioning_only:
        evaluation = json.loads(evaluation_path.read_text())
    else:
        evaluation = evaluate(args.dps, evaluation_path)
    result = conditioning(evaluation, args.output_dir / f"CONDITIONING_DPS{args.dps}.json")
    compare_precision(args.output_dir, args.compare_record)
    print(json.dumps({"stage": "conditioning", "dps": args.dps, "records": len(result["records"])}), flush=True)


if __name__ == "__main__":
    main()
