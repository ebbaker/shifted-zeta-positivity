#!/usr/bin/env python3
"""Independent checks supporting review_20260913.md.

Run with Python 3 and NumPy. No imports from the manuscript's verification
programs. Exact Fraction checks are distinguished from floating-point
diagnostics. Neither the diagnostics nor this program prove RH or certify an
arithmetic Schur matrix. JSON is printed to stdout; source files are not edited.
"""

from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


def quad(fun, left, right, order=120):
    nodes, weights = leggauss(order)
    xs = left + (nodes + 1) * (right - left) / 2
    return np.dot(weights, fun(xs)) * (right - left) / 2


def exact_checks():
    a = [F(4 * k + 1, 2) for k in range(64)]
    mass_sum = sum((2 / ak * F(144) / (ak * ak + 144) for ak in a), F(0))
    beta_upper = F(58, 100) + F(11, 7) + F(21, 10) + F(23, 20) + F(43, 1000) + F(1, 2)
    assert beta_upper == F(41611, 7000)
    assert mass_sum > F(3007, 500) > beta_upper + F(1, 16)
    higher_mass_bound = 2 / F(5, 2) ** 3 + 1 / (2 * F(5, 2) ** 2)
    density_bound = -1 + higher_mass_bound * F(22, 7) ** 2 / 4
    assert higher_mass_bound == F(26, 125)
    assert density_bound == F(-2979, 6125)
    h256 = sum((F(1, k) for k in range(1, 257)), F(0))
    assert h256 - 8 * F(6931, 10000) < F(58, 100)
    assert sum((F(11, 10) ** k / factorial(k) for k in range(6)), F(0)) > 3
    assert sum((F(1, k) for k in range(1, 9)), F(0)) - F(11, 5) == F(29, 56)
    log2_lower = 2 * sum((F(1, (2 * j + 1) * 3 ** (2 * j + 1)) for j in range(5)), F(0))
    assert log2_lower > F(6931, 10000)
    log2_upper = log2_lower + 2 * F(1, 11 * 3 ** 11) / (1 - F(1, 9))
    assert log2_upper < F(7, 10)
    # exp(23/20) > 22/7 > pi implies log(pi) < 23/20.
    assert sum((F(23, 20) ** k / factorial(k) for k in range(8)), F(0)) > F(22, 7)
    sinh_partial = 2 * sum((F(1, 2) ** (2 * j + 1) / factorial(2 * j + 1) for j in range(4)), F(0))
    sinh_tail = 2 * F(1, 2) ** 9 / factorial(9) / (1 - F(1, 440))
    assert sinh_partial + sinh_tail - 1 < F(43, 1000)
    return {
        "arithmetic": "exact rational arithmetic",
        "mass_sum_64_decimal_for_readability": float(mass_sum),
        "mass_sum_minus_3007_over_500": str(mass_sum - F(3007, 500)),
        "3007_over_500_minus_cutoff_threshold": "99/14000",
        "beta_upper": str(beta_upper),
        "density_control_upper": str(density_bound),
        "auxiliary_log_exp_sinh_euler_comparisons": "passed",
    }


def cosine_data(length, count):
    omega = np.arange(count) * np.pi / length
    nu = np.full(count, np.sqrt(2 / length))
    nu[0] = length ** -0.5
    return omega, nu


def shift_matrix(length, count, distance):
    omega, nu = cosine_data(length, count)

    def integral(lam, phase):
        if lam == 0:
            return (length - distance) * np.cos(phase)
        return (np.sin(lam * length + phase) - np.sin(lam * distance + phase)) / lam

    return np.array([
        [nu[i] * nu[j] / 2 * (
            integral(omega[i] - omega[j], omega[j] * distance)
            + integral(omega[i] + omega[j], -omega[j] * distance))
         for j in range(count)] for i in range(count)
    ])


def entry_diagnostics():
    largest = {name: 0.0 for name in ("green_kernel", "boundary_column", "boundary_entry", "shift_entry", "pole_entry", "full_parity")}
    for length in (0.2, 1.0, 3.1):
        count = 6
        omega, nu = cosine_data(length, count)
        nodes, weights = leggauss(100)
        xs, ws = (nodes + 1) * length / 2, weights * length / 2
        cosines = np.cos(xs[:, None] * omega) * nu
        for mass in (0.5, 2.5, 12.5):
            u, v, r = np.exp(-mass * xs), np.exp(-mass * (length - xs)), np.exp(-mass * length)
            coefficient = np.array([[1, r], [r, 1]]) / (1 - r * r)
            rank_kernel = np.stack([u, v], axis=1) @ coefficient @ np.stack([u, v])
            xx, yy = xs[:, None], xs[None, :]
            neumann = np.cosh(mass * np.minimum(xx, yy)) * np.cosh(mass * (length - np.maximum(xx, yy))) / (mass * np.sinh(mass * length))
            free = np.exp(-mass * np.abs(xx - yy)) / (2 * mass)
            largest["green_kernel"] = max(largest["green_kernel"], float(np.max(np.abs(2 * mass * (neumann - free) - rank_kernel))))
            integrated_columns = rank_kernel @ (ws[:, None] * cosines)
            columns = (u[:, None] + v[:, None] * (-1.0) ** np.arange(count)) * (nu * mass / (mass * mass + omega * omega))
            largest["boundary_column"] = max(largest["boundary_column"], float(np.max(np.abs(integrated_columns - columns))))
            entries = cosines.T @ (ws[:, None] * integrated_columns)
            expected = np.zeros((count, count))
            for i in range(count):
                for j in range(count):
                    if (i - j) % 2 == 0:
                        expected[i, j] = 2 * nu[i] * nu[j] * mass ** 2 * (1 - (-1) ** j * r) / ((mass * mass + omega[i] ** 2) * (mass * mass + omega[j] ** 2))
            largest["boundary_entry"] = max(largest["boundary_entry"], float(np.max(np.abs(entries - expected))))
        for distance in (length / 7, length / 2, 0.99 * length):
            formula = shift_matrix(length, count, distance)
            direct = np.array([[quad(lambda x: nu[i] * nu[j] * np.cos(omega[i] * x) * np.cos(omega[j] * (x - distance)), distance, length) for j in range(count)] for i in range(count)])
            largest["shift_entry"] = max(largest["shift_entry"], float(np.max(np.abs(formula - direct))))
            opposite = (np.arange(count)[:, None] - np.arange(count)[None, :]) % 2 != 0
            largest["full_parity"] = max(largest["full_parity"], float(np.max(np.abs((formula + formula.T)[opposite]))))
        jpos = 0.5 * (((-1.0) ** np.arange(count)) * np.exp(length / 2) - 1) / (0.25 + omega ** 2)
        jneg = -0.5 * (((-1.0) ** np.arange(count)) * np.exp(-length / 2) - 1) / (0.25 + omega ** 2)
        c = nu / 2 * (np.exp(-length / 4) * jpos + np.exp(length / 4) * jneg)
        s = nu / 2 * (np.exp(-length / 4) * jpos - np.exp(length / 4) * jneg)
        direct_c = cosines.T @ (ws * np.cosh((xs - length / 2) / 2))
        direct_s = cosines.T @ (ws * np.sinh((xs - length / 2) / 2))
        largest["pole_entry"] = max(largest["pole_entry"], float(np.max(np.abs(c - direct_c))), float(np.max(np.abs(s - direct_s))))
    assert max(largest.values()) < 2e-11
    return {"arithmetic": "floating-point quadrature diagnostics, not interval certificates", "maximum_absolute_errors": largest}


def normalization_diagnostic():
    length, count, masses = 1.7, 4, 30000
    omega, nu = cosine_data(length, count)
    coeff = np.array([1, 0.3 + 0.2j, -0.4j, 0.15])
    norm_squared = float(np.vdot(coeff, coeff).real)

    def f(x):
        return (np.cos(x[:, None] * omega) * nu) @ coeff

    def correlation(r):
        return float(quad(lambda x: (f(x).conj() * f(x - r)).real, r, length)) if r < length else 0.0

    def kernel(r):
        return np.exp(-r / 2) / (-np.expm1(-2 * r))

    def gamma_integrand(rs):
        hs = np.array([correlation(r) for r in rs])
        return -(2 * hs - 2 * np.exp(-rs / 2) * norm_squared) * kernel(rs)

    gamma_functional = quad(gamma_integrand, 0, length)
    for left, right in zip((length, 4, 12, 40), (4, 12, 40, 80)):
        gamma_functional += quad(gamma_integrand, left, right)
    gamma_functional -= (np.log(4 * np.pi) + np.euler_gamma) * norm_squared
    pole = quad(lambda rs: 4 * np.cosh(rs / 2) * np.array([correlation(r) for r in rs]), 0, length)
    primes = 0.0
    for p in (2, 3, 5):
        m = 1
        while m * np.log(p) < length:
            primes -= 2 * np.log(p) * p ** (-m / 2) * correlation(m * np.log(p))
            m += 1
    direct_weil = gamma_functional + pole + primes

    a = 2 * np.arange(masses, dtype=float) + 0.5
    bj = np.sum((2 / a[:, None]) * omega ** 2 / (a[:, None] ** 2 + omega ** 2), axis=0)
    kmat = np.zeros((count, count))
    for i in range(count):
        for j in range(count):
            if (i - j) % 2 == 0:
                kmat[i, j] = 2 * nu[i] * nu[j] * np.sum(a ** 2 * (1 - (-1) ** j * np.exp(-a * length)) / ((a ** 2 + omega[i] ** 2) * (a ** 2 + omega[j] ** 2)))
    w0 = -np.euler_gamma - np.pi / 2 - 3 * np.log(2) - np.log(np.pi)
    gamma_matrix = float(np.vdot(coeff, (np.diag(bj + w0) + kmat) @ coeff).real)
    # Analytic bounds on the omitted diagonal scalar tail and compressed K tail.
    aj = 2 * masses + 0.5
    scalar_tail = omega[-1] ** 2 * (2 / aj ** 3 + 1 / (2 * aj ** 2))
    compressed_tail = 2 * np.sum(nu ** 2) * (1 + np.exp(-aj * length)) * (1 / aj ** 2 + 1 / (2 * aj))
    allowance = norm_squared * (scalar_tail + compressed_tail)
    error = gamma_functional - gamma_matrix
    assert -1e-9 < error < allowance + 1e-9
    return {
        "arithmetic": "floating-point integration with an analytic mass-tail comparison; not a sign certificate",
        "length": length, "mass_count": masses, "direct_weil_value": direct_weil,
        "spatial_minus_finite_cosine_gamma": error, "analytic_mass_tail_allowance": allowance,
        "active_prime_powers": [2, 3, 4, 5],
    }


def matrix_diagnostics():
    rng = np.random.default_rng(13092026)
    max_identity_error, minimum_order_margin = 0.0, float("inf")

    def adj(x):
        return x.conj().T

    def rand(rows, cols):
        return rng.normal(size=(rows, cols)) + 1j * rng.normal(size=(rows, cols))

    def check_identity(lhs, rhs):
        nonlocal max_identity_error
        err = float(np.linalg.norm(lhs - rhs, 2))
        max_identity_error = max(max_identity_error, err)
        assert err < 5e-10

    def check_positive(matrix):
        nonlocal minimum_order_margin
        minimum = float(np.linalg.eigvalsh((matrix + adj(matrix)) / 2)[0])
        minimum_order_margin = min(minimum_order_margin, minimum)
        assert minimum > -5e-10

    for _ in range(12):
        low, high, used = 3, 7, 4
        d = np.arange(2, high + 2, dtype=float)
        c = rand(high, high) / 4
        h = np.diag(d) + adj(c) @ c
        b, a0 = rand(high, low), rand(low, low)
        a = (a0 + adj(a0)) / 2
        w = np.block([[a, adj(b)], [b, h]])
        response = adj(b) @ np.linalg.solve(h, b)
        schur = a - response
        y = np.zeros((high, low), dtype=complex)
        y[:used] = np.linalg.solve(h[:used, :used], b[:used])
        residual = b - h @ y
        check_identity(response, adj(b) @ y + adj(y) @ b - adj(y) @ h @ y + adj(residual) @ np.linalg.solve(h, residual))
        upper = a - adj(b) @ y
        lower = upper - adj(residual) @ residual / d[used]
        check_positive(upper - schur)
        check_positive(schur - lower)
        # Model a positive finite-mass omission that also has mixed columns.
        z = rand(low + high, 2) / 20
        omission = z @ adj(z)
        wj = w - omission
        v0 = np.vstack([np.eye(low), -y])
        cj = adj(v0) @ wj @ v0
        approx_residual = (wj @ v0)[low:]
        eta = np.linalg.norm(omission, 2)
        epsilon = eta * np.linalg.norm(v0, 2) / np.sqrt(d[0])
        split = 3
        gram = adj(approx_residual) @ approx_residual
        rm = approx_residual[:split]
        tm = adj(rm) @ (rm / d[:split, None]) + (gram - adj(rm) @ rm) / d[split]
        check_positive(tm - adj(approx_residual) @ (approx_residual / d[:, None]))
        certified_lower = cj - tm - (2 * np.sqrt(np.linalg.norm(tm, 2)) * epsilon + epsilon ** 2) * np.eye(low)
        check_positive(schur - certified_lower)
        for alpha in (12.0, 27.0):
            v = np.linalg.inv(h + alpha * np.eye(high))
            g = a + alpha * np.eye(low) - adj(b) @ v @ b
            defect = alpha * np.eye(low) + adj(b) @ (np.linalg.inv(h) - v) @ b
            check_identity(g - defect, schur)
    return {"arithmetic": "deterministic complex floating-point diagnostics; not proofs of infinite-dimensional assertions", "cases": 12, "maximum_identity_error": max_identity_error, "minimum_order_margin": minimum_order_margin}


def main():
    manuscript_dir = Path(__file__).resolve().parent.parent
    record = {
        "review": "review_20260913.md",
        "source_sha256": {name: hashlib.sha256((manuscript_dir / name).read_bytes()).hexdigest() for name in ("manuscript.tex", "derivations.tex")},
        "exact_constants": exact_checks(),
        "kernel_and_entry_diagnostics": entry_diagnostics(),
        "normalization_diagnostic": normalization_diagnostic(),
        "response_and_error_propagation_diagnostics": matrix_diagnostics(),
        "status": "all checks passed",
        "scope": "Supporting checks only. Analytic arguments were reviewed in prose; no arithmetic Schur positivity certificate, formal proof, or RH verification is supplied.",
    }
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
