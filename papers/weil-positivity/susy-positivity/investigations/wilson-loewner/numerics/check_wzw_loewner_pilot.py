#!/usr/bin/env python3
"""SU(2)_2 boundary WZW / deterministic Loewner pilot.

Prepared for Edward Baker with GPT-6 (Codex) assistance, 2026-09-22.
Effort setting not exposed. Exact rational algebra and floating diagnostics;
not an interval certificate, path-integral simulation, or arithmetic theorem.
Requires Python 3 and NumPy. No external datasets or network access.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np

NU = 0.25
H = 3.0 / 16.0
I2 = np.eye(2)
D = np.diag([-1.5, 0.5])  # T_01
B = np.array([[0.0, math.sqrt(3) / 2], [math.sqrt(3) / 2, -1.0]])  # T_12
C = -1.5 * I2 - D - B  # T_02
R = np.array([[0.5, math.sqrt(3) / 2], [-math.sqrt(3) / 2, 0.5]])
Z = np.diag([1.0, -1.0])
CHANNEL_METRIC = np.diag([1.0, 4.0 / 3.0])
CHANNEL_SCALE = np.diag([1.0, math.sqrt(3) / 2])
FUSION = np.array([[1 / math.sqrt(2), -math.sqrt(2 / 3)],
                   [math.sqrt(3 / 8), 1 / math.sqrt(2)]])


def blocks(r):
    """Columns: vacuum and spin-one Frobenius blocks, 0 < r < 1."""
    if not 0 < float(np.real(r)) < 1:
        raise ValueError("The chosen branch requires 0 < Re(r) < 1")
    s = np.sqrt(1 - r)
    p = (r * (1 - r)) ** (-3 / 8)
    f0 = p / (2 * math.sqrt(2)) * np.array([
        (1 + s) ** 1.5, -math.sqrt(3) * (1 - s) * np.sqrt(1 + s)])
    f1 = p / math.sqrt(6) * np.array([
        -(1 - s) ** 1.5, math.sqrt(3) * (1 + s) * np.sqrt(1 - s)])
    return np.column_stack([f0, f1])


def frobenius(r, channel, terms=120, nu=NU, residue=B):
    """Independent power-series solution of the KZ equation."""
    lam = nu * D[channel, channel]
    v = I2[:, channel].copy()
    partial = v.copy()
    answer = v.copy()
    for n in range(1, terms):
        v = np.linalg.solve((lam + n) * I2 - nu * D, -nu * residue @ partial)
        answer += r ** n * v
        partial += v
    return r ** lam * answer


def q_matrix(a, b):
    return D / a + C / b


def generator(a, b, speed):
    q = q_matrix(a, b)
    return -NU * (2 * q @ q + speed * q)


def unreduced_generator(a, b, speed):
    ax = NU * (D / a + B / (a - b))
    ay = NU * (C / b + B / (b - a))
    return ((2 / a - speed) * ax + (2 / b - speed) * ay
            - 2 * H * (1 / a ** 2 + 1 / b ** 2) * I2)


def evaluation(a, b, log_jx=0.0, log_jy=0.0):
    return np.exp(H * (log_jx + log_jy)) * b ** (-2 * H) * blocks(a / b)


def rk4(rhs, state, t0, t1, steps):
    state = np.asarray(state, dtype=float).copy()
    dt = (t1 - t0) / steps
    for n in range(steps):
        t = t0 + n * dt
        k1 = rhs(t, state)
        k2 = rhs(t + dt / 2, state + dt * k1 / 2)
        k3 = rhs(t + dt / 2, state + dt * k2 / 2)
        k4 = rhs(t + dt, state + dt * k3)
        state += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return state


def evolve(speed, steps, t0=0.0, t1=0.2, geometry=None, initial=None):
    """Integrate geometry, Jacobians, the full propagator and norm balance."""
    geometry = np.array([1.0, 2.0, 0.0, 0.0]) if geometry is None else geometry
    initial = evaluation(*geometry)[:, 0] if initial is None else initial
    state = np.concatenate([geometry, I2.ravel(), [0.0]])

    def rhs(t, state):
        a, b, ljx, ljy = state[:4]
        if not 0 < a < b:
            raise ValueError("A spectator left the admissible ordered chamber")
        v = speed(t)
        u = state[4:8].reshape(2, 2)
        m = u @ initial
        q = q_matrix(a, b)
        loss = 4 * NU * np.dot(q @ m, q @ m) + 2 * NU * v * np.dot(m, q @ m)
        return np.concatenate([[2 / a - v, 2 / b - v, -2 / a ** 2, -2 / b ** 2],
                               (generator(a, b, v) @ u).ravel(), [loss]])

    return rk4(rhs, state, t0, t1, steps)


def rational_checks():
    """Exact identities in basis (e0, e1/sqrt(3)), using Fraction only."""
    def mat(rows):
        return [[F(x) for x in row] for row in rows]

    def add(a, b):
        return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]

    def mul(a, b):
        return [[sum(a[i][l] * b[l][j] for l in range(2)) for j in range(2)]
                for i in range(2)]

    d = mat([[F(-3, 2), 0], [0, F(1, 2)]])
    c = mat([[0, F(-1, 2)], [F(-3, 2), -1]])
    b = mat([[0, F(1, 2)], [F(3, 2), -1]])
    casimir = mat([[F(3, 4), 0], [0, F(3, 4)]])
    return {
        "exact_T01_square": add(mul(d, d), d) == casimir,
        "exact_T02_square": add(mul(c, c), c) == casimir,
        "exact_anticommutator": add(mul(d, c), mul(c, d)) == b,
        "exact_three_residue_sum": add(add(d, c), b) == mat([[F(-3, 2), 0], [0, F(-3, 2)]]),
        "exact_vacuum_exponent": F(1, 4) * F(-3, 2) == -2 * F(3, 16),
        "exact_spin_one_exponent": F(1, 4) * F(1, 2) == F(1, 2) - 2 * F(3, 16),
        "exact_moving_driver_witness": -F(1, 4) * (2 * (F(9, 4) + F(3, 16)) - 6) == F(9, 32),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = []

    def check(name, value, threshold=2e-11, comparison="<=", kind="floating"):
        value = float(value)
        passed = math.isfinite(value) and (value <= threshold if comparison == "<=" else value >= threshold)
        cases.append(dict(name=name, value=value, threshold=threshold,
                          comparison=comparison, passed=passed, kind=kind))

    for name, passed in rational_checks().items():
        check(name, 0 if passed else 1, 0, kind="exact rational")

    singlet = np.array([0, 1, -1, 0]) / math.sqrt(2)
    plus = np.array([1, 0, 0, 0])
    minus = np.array([0, 0, 0, 1])
    zero = np.array([0, 1, 1, 0]) / math.sqrt(2)
    embedding = np.column_stack([np.kron(singlet, singlet),
                                (np.kron(plus, minus) + np.kron(minus, plus)
                                 - np.kron(zero, zero)) / math.sqrt(3)])
    pauli = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]),
             np.diag([1, -1])]

    def site(a, i):
        result = np.ones((1, 1))
        for j in range(4):
            result = np.kron(result, a if i == j else I2)
        return result

    check("singlet_embedding_orthonormal", np.linalg.norm(embedding.T @ embedding - I2))
    for a, sigma in enumerate(pauli):
        total = sum(site(sigma / math.sqrt(2), i) for i in range(4))
        check(f"total_SU2_generator_{a}", np.linalg.norm(total @ embedding))
    for i, j, residue in [(0, 1, D), (0, 2, C), (1, 2, B)]:
        operator = sum(site(sigma / math.sqrt(2), i) @ site(sigma / math.sqrt(2), j)
                       for sigma in pauli)
        check(f"Pauli_reduction_{i}{j}", np.linalg.norm(operator @ embedding - embedding @ residue))

    fusion_residuals = []
    for r in [0.07, 0.2, 0.5, 0.73]:
        f = blocks(r)
        series = np.column_stack([frobenius(r, i) for i in range(2)])
        check(f"algebraic_vs_Frobenius_r{r}", np.linalg.norm(f - series))
        derivative = np.imag(blocks(r + 1e-25j)) / 1e-25
        check(f"algebraic_KZ_derivative_r{r}", np.linalg.norm(derivative - NU * (D / r + B / (r - 1)) @ f))
        t_blocks = R @ Z @ blocks(1 - r) @ Z
        residual = np.linalg.norm(np.linalg.solve(t_blocks, f) - FUSION)
        fusion_residuals.append(residual)
        check(f"fusion_connection_r{r}", residual)

    check("channel_pairing_preserved_by_fusion", np.linalg.norm(FUSION.T @ CHANNEL_METRIC @ FUSION - CHANNEL_METRIC))
    orthogonal_fusion = np.linalg.solve(CHANNEL_SCALE, FUSION @ CHANNEL_SCALE)
    check("orthonormal_fusion_matrix", np.linalg.norm(orthogonal_fusion - np.array([[1, -1], [1, 1]]) / math.sqrt(2)))
    braid = np.diag(np.exp(2j * np.pi * np.array([-3 / 8, 1 / 8])))
    check("channel_pairing_preserved_by_local_monodromy", np.linalg.norm(braid.conj().T @ CHANNEL_METRIC @ braid - CHANNEL_METRIC))

    # KZ partial derivatives, including the moving tip, tested independently.
    coords = np.array([0.13, 1.21, 2.54])
    def at_coordinates(v):
        u, x, y = v
        return (y - u) ** (-2 * H) * blocks((x - u) / (y - u))
    u, x, y = coords
    a, b = x - u, y - u
    connections = [-NU * q_matrix(a, b), NU * (D / a + B / (a - b)),
                   NU * (C / b + B / (b - a))]
    for i, connection in enumerate(connections):
        shifted = coords.astype(complex)
        shifted[i] += 1e-25j
        derivative = np.imag(at_coordinates(shifted)) / 1e-25
        check(f"KZ_coordinate_derivative_{i}", np.linalg.norm(derivative - connection @ at_coordinates(coords)))

    for a, b, v in [(1, 2, 0), (1, 2, 4), (0.7, 1.6, -0.8), (-2, -0.5, 0)]:
        g = generator(a, b, v)
        q = q_matrix(a, b)
        check(f"Ward_KZ_square_reduction_{a}_{b}_{v}", np.linalg.norm(g - unreduced_generator(a, b, v)))
        completed = -2 * NU * (q + v * I2 / 4) @ (q + v * I2 / 4) + NU * v ** 2 * I2 / 8
        check(f"driver_completed_square_{a}_{b}_{v}", np.linalg.norm(g - completed))

    drivers = {"constant": lambda t: 0.0, "linear_0.8": lambda t: 0.8,
               "linear_4": lambda t: 4.0, "linear_minus_0.8": lambda t: -0.8,
               "sine_0.4_sin_2t": lambda t: 0.8 * math.cos(2 * t)}
    initial_eval = evaluation(1, 2)
    initial = initial_eval[:, 0]
    initial_norm2 = float(initial @ initial)
    samples = {}
    for name, speed in drivers.items():
        coarse = evolve(speed, 512)
        fine = evolve(speed, 1024)
        geometry = fine[:4]
        propagator = fine[4:8].reshape(2, 2)
        direct = evaluation(*geometry)
        check(f"RK4_refinement_{name}", np.linalg.norm(coarse - fine), 2e-10)
        check(f"full_block_pullback_{name}", np.linalg.norm(propagator @ initial_eval - direct), 2e-10)
        final = propagator @ initial
        check(f"integrated_norm_balance_{name}", abs(final @ final + fine[8] - initial_norm2), 2e-10)

        half = evolve(speed, 512, t1=0.1)
        second = evolve(speed, 512, t0=0.1, geometry=half[:4],
                        initial=half[4:8].reshape(2, 2) @ initial)
        composed = second[4:8].reshape(2, 2) @ half[4:8].reshape(2, 2)
        check(f"propagator_composition_{name}", np.linalg.norm(propagator - composed), 2e-10)
        h_initial = np.linalg.inv(initial_eval).T @ CHANNEL_METRIC @ np.linalg.inv(initial_eval)
        h_final = np.linalg.inv(direct).T @ CHANNEL_METRIC @ np.linalg.inv(direct)
        check(f"CS_pairing_in_evaluated_coordinates_{name}", np.linalg.norm(propagator.T @ h_final @ propagator - h_initial), 2e-9)
        samples[name] = dict(final_relative_points=geometry[:2].tolist(),
                             initial_block=initial.tolist(), final_block=final.tolist(),
                             initial_norm_squared=initial_norm2, final_norm_squared=float(final @ final),
                             integrated_signed_loss=float(fine[8]),
                             largest_propagator_singular_value=float(np.linalg.svd(propagator, compute_uv=False)[0]))
        if name == "constant":
            aa, bb = math.sqrt(1.8), math.sqrt(4.8)
            expected_geometry = [aa, bb, math.log(1 / aa), math.log(2 / bb)]
            check("constant_driver_exact_geometry", np.linalg.norm(geometry - expected_geometry))
            check("constant_driver_propagator_contraction", samples[name]["largest_propagator_singular_value"], 1.0)

    check("positive_moving_driver_e0_witness", generator(1, 2, 4)[0, 0], 0.28, ">=")
    cardy_derivative = 2 * initial @ generator(1, 2, 4) @ initial
    check("positive_moving_driver_Cardy_block_witness", cardy_derivative, 0.43, ">=")
    check("omitting_tip_drift_is_detected", np.linalg.norm(generator(1, 2, 4) - generator(1, 2, 0)), 1.0, ">=")
    check("omitting_Jacobians_is_detected", 2 * H * (1 + 1 / 4), 0.46, ">=")
    check("single_tensor_component_not_closed", abs(generator(1, 2, 0)[0, 1]), 0.32, ">=")

    record = dict(
        schema_version=1, date="2026-09-22", prepared_for="Edward Baker",
        model="GPT-6 (Codex; developer-provided identity)", effort="not exposed; not inferred",
        scope="Exact finite representation identities and floating diagnostics for the boundary WZW pilot; no arithmetic realization, interval certification or independent review",
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        environment=dict(python=platform.python_version(), numpy=np.__version__),
        parameters=dict(k=2, h=H, nu=NU, initial_points=[0, 1, 2, "infinity"], final_capacity=0.2,
                        integration_steps=[512, 1024], Frobenius_terms=120,
                        boundary_labels=[0, 0.5, 0, 0.5, 0]),
        exact_rational_cases=sum(c["kind"] == "exact rational" for c in cases),
        case_count=len(cases), all_pass=all(c["passed"] for c in cases), cases=cases,
        samples=samples,
        moving_driver_initial_Cardy_norm_squared_derivative=float(cardy_derivative),
        maximum_fusion_connection_residual=max(fusion_residuals),
    )
    output = json.dumps(record, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
        print(json.dumps({"output": str(args.output), "case_count": len(cases), "all_pass": record["all_pass"],
                          "failed": [c for c in cases if not c["passed"]]}))
    else:
        print(output, end="")
    raise SystemExit(0 if record["all_pass"] else 1)


if __name__ == "__main__":
    main()
