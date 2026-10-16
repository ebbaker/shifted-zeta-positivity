#!/usr/bin/env python3
"""Independent angular-quadrature controls for the winding energy identity.

Prepared for Edward Baker with GPT-6 (Codex) assistance, 2026-09-25.
Reasoning effort is not exposed and is not inferred.
These prescribed densities are algebra controls, not interacting YM samples.
"""

import argparse
import hashlib
import json
from pathlib import Path
import platform

import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    seed = 20260925
    rng = np.random.default_rng(seed)
    modes = np.arange(-7, 8)
    gridsize = 4096
    theta = (np.arange(gridsize) + 0.5) * np.pi / gridsize
    cosines = np.cos(modes[:, None] * theta)
    sines = np.sin(modes[:, None] * theta)
    checks = []

    def check(label, actual, expected):
        error = float(abs(actual - expected))
        scale = max(1.0, float(abs(actual)), float(abs(expected)))
        tolerance = 5e-12 * scale
        checks.append({"label": label, "absolute_error": error,
                       "scaled_error": error / scale,
                       "tolerance": tolerance, "passed": error <= tolerance})

    for name, alpha, beta in [("Haar", 0.0, 0.0),
                               ("positive_central_control", 0.35, 0.2)]:
        normalization = 1 - beta / 2
        rho = (1 + alpha * np.cos(theta) + beta * np.cos(2 * theta)) / normalization

        def t(k):
            return {0: 1.0, 1: alpha / 2, 2: beta / 2}.get(abs(int(k)), 0.0) / normalization

        def w(k):
            return t(k) - (t(k - 2) + t(k + 2)) / 2

        gram = np.array([[w(m - n) for m in modes] for n in modes])
        energy = np.array([[n * m * w(m - n) + 2 * (t(m - n) - t(m + n))
                            for m in modes] for n in modes])
        for trial in range(12):
            a = rng.normal(size=len(modes)) + 1j * rng.normal(size=len(modes))
            b = rng.normal(size=len(modes)) + 1j * rng.normal(size=len(modes))
            ca, sa = a @ cosines, a @ sines
            cb, sb = b @ cosines, b @ sines
            dca, dsa = -(modes * a) @ sines, (modes * a) @ cosines
            dcb, dsb = -(modes * b) @ sines, (modes * b) @ cosines
            norm_integral = 2 * np.mean(rho * np.sin(theta)**2 * (ca.conj() * cb + sa.conj() * sb))
            energy_integral = 2 * np.mean(rho * (np.sin(theta)**2 *
                (dca.conj() * dcb + dsa.conj() * dsb) + 2 * sa.conj() * sb))
            check(f"{name}: norm mixed pairing {trial}", np.vdot(a, gram @ b), norm_integral)
            check(f"{name}: electric mixed pairing {trial}", np.vdot(a, energy @ b), energy_integral)
            if name == "Haar":
                da, db = dict(zip(modes, a)), dict(zip(modes, b))
                diff_pair = 0j
                for k in range(int(modes[0]) - 2, int(modes[-1]) + 1):
                    delta_a = (k + 2) * da.get(k + 2, 0) - k * da.get(k, 0)
                    delta_b = (k + 2) * db.get(k + 2, 0) - k * db.get(k, 0)
                    diff_pair += 0.5 * np.conj(delta_a) * delta_b
                angular_pair = sum(np.conj(da[k] - da.get(-k, 0)) *
                                   (db[k] - db.get(-k, 0)) for k in modes)
                check(f"Haar: finite-difference pairing {trial}",
                      np.vdot(a, energy @ b), diff_pair + angular_pair)

        if name == "Haar":
            index = {int(n): j for j, n in enumerate(modes)}
            check("fundamental Casimir", energy[index[1], index[1]], 3)
            check("double winding diagonal", energy[index[2], index[2]], 6)
            check("opposite fundamental windings", energy[index[-1], index[1]], -1.5)
            check("constant is annihilated", np.max(np.abs(energy[index[0], :])), 0)

    record = {
        "date": "2026-09-25",
        "prepared_for": "Edward Baker",
        "model": "GPT-6 (Codex)",
        "reasoning_effort": "not exposed; not inferred",
        "purpose": "Deterministic algebra controls; neither interacting YM sampling nor a proof of the infinite-source limit.",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "parameters": {"seed": seed, "winding_range": [-7, 7], "angular_midpoints": gridsize,
                       "mixed_trials_per_density": 12,
                       "densities": ["rho=1", "rho=(1+0.35*cos(theta)+0.2*cos(2*theta))/0.9"]},
        "check_count": len(checks),
        "all_passed": all(c["passed"] for c in checks),
        "max_scaled_error": max(c["scaled_error"] for c in checks),
        "checks": checks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: record[k] for k in ("check_count", "all_passed", "max_scaled_error")}))
    if not record["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
