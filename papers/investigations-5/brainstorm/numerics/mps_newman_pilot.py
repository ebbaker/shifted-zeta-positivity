#!/usr/bin/env python3
"""Bounded MPS representation pilot, not a zero or interval certificate.

Prepared for Edward Baker, 2026-11-13, with OpenAI Codex assistance.
Actual backend model and effort are unavailable in recorded configurations.
Requires Python 3 and NumPy. No large arrays are saved.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform

import numpy as np


def row_times(row, matrix):
    return [sum(row[k] * matrix[k][j] for k in range(len(row)))
            for j in range(len(row))]


def exact_checks():
    a = F(-15, 8)
    weights = [F(2), F(1), F(1, 2), F(1, 4)]
    coefficients = [F(1), F(-2), F(3), F(-1), F(2)]
    for bits in itertools.product((0, 1), repeat=4):
        row = [F(1), 2 * a, a * a]
        polyrow = [a ** k for k in range(5)]
        for weight, bit in zip(weights, bits):
            q = weight * bit
            row = row_times(row, [[1, 2 * q, q * q], [0, 1, q], [0, 0, 1]])
            shift = [[F(math.comb(j, k)) * q ** (j - k) if j >= k else F(0)
                      for j in range(5)] for k in range(5)]
            polyrow = row_times(polyrow, shift)
        u = a + sum(w * b for w, b in zip(weights, bits))
        assert row[-1] == u * u
        assert sum(v * c for v, c in zip(polyrow, coefficients)) == sum(
            c * u ** j for j, c in enumerate(coefficients))
    # q F = a q^2 + 2q + a; a=1 gives (q+1)^2.
    # At the event the amplitude matrix [[1,1],[1,1]] has rank one.
    controls = []
    for amp in [F(1, 2), F(1), F(2)]:
        controls.append({"amplitude": str(amp),
                         "quadratic_discriminant": str(4 * (1 - amp * amp)),
                         "state_matrix_determinant": str(amp * amp - 1)})
    return {"rational_generator_and_polynomial_checks": "passed on all 16 configurations",
            "three_atom_control": controls,
            "scope": "Finite algebra checks; continuum statements have written derivations"}


def theta_source(u, modes=8):
    """Literal positive-half-line series, reflected evenly; floating prefix."""
    v = np.abs(u)
    r = np.pi * np.exp(4 * v[:, None]) * np.arange(1, modes + 1)[None, :] ** 2
    return np.exp(v) * np.sum((2 * r * r - 3 * r) * np.exp(-r), axis=1)


def tt_svd(vector, bits, relative_tolerance):
    """Left-to-right TT-SVD with an equal squared-error budget per cut."""
    budget = (relative_tolerance * np.linalg.norm(vector)) ** 2 / (bits - 1)
    remaining = vector.reshape((2,) * bits)
    left = 1
    cores, discarded = [], []
    for site in range(bits - 1):
        matrix = remaining.reshape(left * 2, -1)
        u, singular, vh = np.linalg.svd(matrix, full_matrices=False)
        tail = np.append(np.cumsum((singular[::-1] ** 2))[::-1], 0.0)
        rank = next(r for r in range(1, len(singular) + 1) if tail[r] <= budget)
        cores.append(u[:, :rank].reshape(left, 2, rank))
        discarded.append(float(tail[rank]))
        remaining = singular[:rank, None] * vh[:rank, :]
        left = rank
    cores.append(remaining.reshape(left, 2, 1))
    return cores, math.sqrt(sum(discarded))


def reconstruct(cores):
    tensor = cores[0]
    for core in cores[1:]:
        tensor = np.tensordot(tensor, core, axes=(-1, 0))
    return tensor.reshape(-1)


def contract(cores, z, a, weights, spacing):
    value = np.ones((1,), dtype=complex)
    for core, weight in zip(cores, weights):
        value = value @ (core[:, 0, :] + np.exp(1j * z * weight) * core[:, 1, :])
    return complex(math.sqrt(spacing) / 2 * np.exp(1j * z * a) * value[0])


def pair(value):
    return [float(np.real(value)), float(np.imag(value))]


def pilot():
    rows = []
    radius, lambda0 = 2.0, 0.5
    probes = [0.0, 20.0, 40.0, 80.0, 40.0 + 4j, 40.0 + 8j]
    for bits in [10, 12]:
        count = 2 ** bits
        spacing = 2 * radius / count
        a = -radius + spacing / 2
        weights = [spacing * 2 ** (bits - 1 - k) for k in range(bits)]
        coordinates = a + spacing * np.arange(count)
        source = theta_source(coordinates)
        initial = math.sqrt(spacing) * np.exp(lambda0 * coordinates ** 2) * source
        for target_time in [0.5, 0.0]:
            tau = lambda0 - target_time
            exact_grid = np.exp(-tau * coordinates ** 2) * initial
            for tolerance in [1e-8, 1e-12]:
                cores, discarded_estimate = tt_svd(exact_grid, bits, tolerance)
                approximation = reconstruct(cores)
                error = float(np.linalg.norm(approximation - exact_grid))
                observations = []
                for z in probes:
                    factors = np.exp(1j * z * coordinates)
                    dense = math.sqrt(spacing) / 2 * np.dot(factors, exact_grid)
                    compressed = contract(cores, z, a, weights, spacing)
                    # Cauchy bound is exact for exact arithmetic, evaluated here in binary64.
                    cauchy = math.sqrt(spacing) / 2 * np.linalg.norm(factors) * error
                    observations.append({"z": pair(z), "dense_grid": pair(dense),
                                         "mps_contraction": pair(compressed),
                                         "compression_difference": abs(dense - compressed),
                                         "cauchy_bound_floating": float(cauchy),
                                         "difference_over_dense_modulus": float(abs(dense - compressed) / abs(dense))})
                rows.append({"bits": bits, "grid_points": count, "lambda": target_time,
                             "tau_from_lambda0": tau, "relative_tolerance_requested": tolerance,
                             "ranks": [c.shape[2] for c in cores[:-1]],
                             "maximum_bond_dimension": max(c.shape[2] for c in cores),
                             "stored_real_parameters": sum(c.size for c in cores),
                             "state_norm": float(np.linalg.norm(exact_grid)),
                             "state_error": error, "relative_state_error": error / float(np.linalg.norm(exact_grid)),
                             "discarded_singular_value_error_estimate": discarded_estimate,
                             "observations": observations})
    return rows


def main():
    here = Path(__file__).resolve()
    result = {"date_local": "2026-11-13", "timezone": "America/New_York",
              "executed_at_utc": datetime.now(timezone.utc).isoformat(),
              "prepared_for": "Edward Baker", "llm_assistance": "OpenAI Codex",
              "actual_model": None, "actual_effort": None,
              "python": platform.python_version(), "numpy": np.__version__,
              "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
              "scope": "Exact finite rational identities plus floating dense-grid compression pilot; no interval certification, no continuum quadrature certificate, no all-height rank law or zero conclusion",
              "parameters": {"source_radius": 2, "source_modes": 8, "lambda0": 0.5,
                             "source_convention": "H_lambda(z)=one half full-line Fourier integral of exp(lambda*u^2)*Phi(u)",
                             "generation": "Each slice obtained by exact diagonal grid evolution, then independently compressed; no adaptive MPS time integrator benchmarked",
                             "storage": "Only small summaries retained; dense vectors and cores regenerated in memory"},
              "exact_checks": exact_checks(), "floating_cases": pilot()}
    output = here.with_name("MPS_NEWMAN_PILOT_20261113.json")
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(output)
    for r in result["floating_cases"]:
        obs = next(o for o in r["observations"] if o["z"] == [80.0, 0.0])
        print({"bits": r["bits"], "lambda": r["lambda"],
               "tol": r["relative_tolerance_requested"], "D": r["maximum_bond_dimension"],
               "parameters": r["stored_real_parameters"], "relative_state_error": r["relative_state_error"],
               "relative_grid_observation_error_at_80": obs["difference_over_dense_modulus"]})


if __name__ == "__main__":
    main()
