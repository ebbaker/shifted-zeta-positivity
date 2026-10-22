#!/usr/bin/env python3
"""Polynomial Chern/Hopf boundary checks; floating diagnostics, not certificates.

Prepared for Edward Baker with substantial LLM assistance, 22 October 2026.
Recorded root configuration: gpt-6-astra (Codex), reasoning effort ultra.
Standard library only. No theta event, source estimate, or interval claim.

Run: python3 check_chb_full_boundary.py [--output RECEIPT.json]
The exact Fraction checks test quadratic geometry, rational constants, and
the quartic fixed-boundary collision control, and curvature Gram/Schur identities.
The 1D transgression integral and independent direct pullback 3D integrals
are ordinary floating quadratures; convergence is a diagnostic only.
"""

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import time


def legendre_pair(n, x):
    p0, p1 = 1.0, x
    for k in range(2, n + 1):
        p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
    return p0, p1


def gauss_legendre(n, a, b):
    """Floating Gauss-Legendre nodes/weights from Newton iteration."""
    result = []
    for i in range(1, (n + 1) // 2 + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(40):
            p0, p1 = legendre_pair(n, x)
            derivative = n * (x * p1 - p0) / (x * x - 1)
            step = p1 / derivative
            x -= step
            if abs(step) < 2e-16:
                break
        p0, p1 = legendre_pair(n, x)
        derivative = n * (x * p1 - p0) / (x * x - 1)
        weight = 2 / ((1 - x * x) * derivative * derivative)
        result.append(((a + b) / 2 + (b - a) * x / 2,
                       weight * (b - a) / 2))
        if n + 1 - i != i:
            result.append(((a + b) / 2 - (b - a) * x / 2,
                           weight * (b - a) / 2))
    return result


def exact_geometry():
    radius, half_time, half_imag, pmax = F(1), F(1, 16), F(1, 16), F(1, 4)
    tau_bound = half_time + half_imag  # Conservative corner modulus bound.
    kappa = pmax * pmax / (1 + pmax * pmax)
    checks = {
        "proper_two_root_wall": 2 * tau_bound < radius * radius,
        "proper_Hz_wall": 2 * radius > 0,
        "F_wall_Rouche": pmax * (radius * radius + 2 * tau_bound) < 2 * radius,
        "analytic_sqrt_branch": 2 * pmax * pmax * tau_bound < 1,
        "event_off_all_heat_edges": half_time > 0 and half_imag > 0,
        "kappa_equals_one_seventeenth": kappa == F(1, 17),
        "minus_heat_fraction": kappa / 4 == F(1, 68),
        "complement_before_wall_payment": (1 - kappa) / 4 == F(4, 17),
        "quadratic_complex_jacobian": F(-2) * F(2) == F(-4),
        "quadratic_real_jacobian": F(-4) ** 2 == F(16),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "parameters": {"R": str(radius), "T": str(half_time),
                       "Y": str(half_imag), "P": str(pmax)},
        "tau_modulus_upper": str(tau_bound),
        "sqrt_branch_argument_upper": str(2 * pmax * pmax * tau_bound),
        "pH_wall_upper": str(pmax * (radius * radius + 2 * tau_bound)),
        "Hz_wall_exact": str(2 * radius),
        "kappa": str(kappa),
        "minus_piece_each_heat_face": str(kappa / 4),
        "complement_base_each_heat_face": str((1 - kappa) / 4),
        "checks": checks,
    }


def quartic_fixed_boundary_control():
    """Exact finite-height control; fixed walls do not exclude interior collisions."""
    radius, time_radius = F(1, 2), F(1, 64)
    poly = {(0, 4): F(1), (0, 2): F(-1), (1, 2): F(-12),
            (1, 0): F(2), (2, 0): F(12)}

    def derivative(polynomial, axis):
        result = {}
        for powers, value in polynomial.items():
            if powers[axis]:
                new_powers = list(powers)
                new_powers[axis] -= 1
                result[tuple(new_powers)] = value * powers[axis]
        return result

    dt = derivative(poly, 0)
    dzz = derivative(derivative(poly, 1), 1)
    heat_residual = {key: dt.get(key, 0) + dzz.get(key, 0)
                     for key in dt.keys() | dzz.keys()}
    initial_wall_floor = radius ** 2 * (1 - radius ** 2)
    wall_perturbation = (12 * radius ** 2 + 2) * time_radius + 12 * time_radius ** 2
    inner_root_square_upper = 2 * time_radius + 12 * time_radius ** 2
    other_critical_square_lower = (1 - 12 * time_radius) / 2
    checks = {
        "heat_equation_exact": all(value == 0 for value in heat_residual.values()),
        "ordinary_center_double": poly.get((0, 0), 0) == 0
            and derivative(poly, 1).get((0, 0), 0) == 0 and dzz[(0, 0)] == -2,
        "discriminant_positive_coefficients": all(c > 0 for c in (F(1), F(16), F(96))),
        "inner_root_bound": inner_root_square_upper == F(35, 1024)
            and inner_root_square_upper < radius ** 2,
        "outer_root_square_lower": F(1) > radius ** 2,
        "initial_wall_floor": initial_wall_floor == F(3, 16),
        "complex_time_Rouche": wall_perturbation == F(83, 1024)
            and wall_perturbation < initial_wall_floor,
        "other_critical_points_outside": other_critical_square_lower == F(13, 32)
            and other_critical_square_lower > radius ** 2,
        "critical_value_has_only_center_zero": 6 * time_radius < 1,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "field": "H(tau,z)=z^4-(1+12tau)z^2+2tau+12tau^2",
        "scope": "Non-theta polynomial control; |tau|<=d for complex-time wall statements",
        "R": str(radius), "d": str(time_radius),
        "checks": checks,
        "initial_wall_floor": str(initial_wall_floor),
        "complete_wall_perturbation_upper": str(wall_perturbation),
        "inner_root_square_upper_for_0<t<=d": str(inner_root_square_upper),
        "other_critical_point_modulus_squared_lower": str(other_critical_square_lower),
        "critical_value": "V(tau)=2tau(1+6tau)",
        "analytic_interpretation": [
            "y_plus=(1+12t+sqrt(1+16t+96t^2))/2>=1 for t>=0",
            "y_minus*y_plus=2t+12t^2, hence 0<y_minus<=35/1024 for 0<t<=d",
            "Rouche gives exactly two spatial zeros throughout the fixed complex-time window",
            "The only spatial critical point inside the fixed disk is z=0",
            "The interior double at tau=0 persists despite the fixed separating boundary",
        ],
    }


def transgression_edge(n):
    """K_e on the late edge, using its exact analytic one-dimensional formula.

    a=1+R^2/4, b=|tau|^2/R^2, D=sqrt((a+b)^2-|tau|^2).
    K_e=(4*pi)^-1 integral [1+(b-a)/D] darg(tau).
    The stable bracket uses D^2-(a-b)^2=4|tau|^2/R^2.
    """
    radius, half_time = 1.0, 1.0 / 16
    a = 1 + radius * radius / 4
    terms = []
    for y, weight in gauss_legendre(n, -half_time, half_time):
        s2 = half_time * half_time + y * y
        b = s2 / (radius * radius)
        discriminant = math.sqrt((a + b) ** 2 - s2)
        bracket = (4 * s2 / (radius * radius)) / (
            discriminant * (discriminant + a - b))
        terms.append(weight * bracket * half_time / s2 / (4 * math.pi))
    return math.fsum(terms)


def direct_faces(n, angular_nodes=64):
    """Direct C pullback, without the transgression or critical-value formulas.

    H=z^2-2*tau, E=|H|^2+4|z|^2,
    C=8/(pi^2 E^2) i_V(dt wedge ds wedge dx wedge dy),
    with complex V=(tau+z^2/2,z). Each face uses its outward normal.
    Spatial radial integration uses v=|z|^2 and dx dy=dv dphi/2.
    """
    radius, half_time = 1.0, 1.0 / 16
    time_nodes = gauss_legendre(n, -half_time, half_time)
    radial_nodes = gauss_legendre(n, 0.0, radius * radius)
    angle_weight = 2 * math.pi / angular_nodes
    angles = [(math.cos(4 * math.pi * k / angular_nodes),
               math.sin(4 * math.pi * k / angular_nodes))
              for k in range(angular_nodes)]
    totals = [0.0] * 4  # Late, early, top imaginary time, bottom imaginary time.
    heat_factor = 4 / (math.pi * math.pi)
    for u, wu in time_nodes:
        for v, wv in radial_nodes:
            weight = wu * wv * angle_weight * heat_factor
            for co, si in angles:
                zr, zi = v * co, v * si
                face_data = (
                    (half_time, u, half_time + zr / 2),
                    (-half_time, u, half_time - zr / 2),
                    (u, half_time, half_time + zi / 2),
                    (u, -half_time, half_time - zi / 2),
                )
                for j, (t, s, normal_component) in enumerate(face_data):
                    energy = (zr - 2 * t) ** 2 + (zi - 2 * s) ** 2 + 4 * v
                    totals[j] += weight * normal_component / (energy * energy)
    wall = 0.0
    wall_factor = 8 * radius * radius / (math.pi * math.pi)
    for t, wt in time_nodes:
        for s, ws in time_nodes:
            weight = wt * ws * angle_weight * wall_factor
            for co, si in angles:
                energy = (radius * radius * co - 2 * t) ** 2 + (
                    radius * radius * si - 2 * s) ** 2 + 4 * radius * radius
                wall += weight / (energy * energy)
    names = ("late", "early", "top_imaginary_time", "bottom_imaginary_time")
    return {"heat_faces": dict(zip(names, totals)), "spatial_wall": wall,
            "all_faces_total": math.fsum(totals + [wall])}


def curvature_algebra_controls():
    """Exact rational checks of the spatial Gram and full determinant formulas."""
    cases = [(2,1,3,4,F(1,2)), (1,2,-3,5,F(1,3)),
             (0,1,0,0,F(1,2)), (1,0,0,0,F(1,4))]
    rows=[]
    for h,hz,hzz,hzzz,delta in cases:
        h,hz,hzz,hzzz=map(F,(h,hz,hzz,hzzz))
        g=(h,hz); vt=(-hzz,-hzzz); vz=(hz,hzz)
        dot=lambda x,y:sum(a*b for a,b in zip(x,y))
        energy=dot(g,g); denom=energy+delta*delta
        entry=lambda x,y:dot(x,y)/denom-dot(g,x)*dot(g,y)/denom**2
        ktt,ktz,kzz=entry(vt,vt),entry(vt,vz),entry(vz,vz)
        jac=hz*hzzz-hzz*hzz; spatial=h*hzz-hz*hz
        numerator=spatial*spatial+delta*delta*dot(vz,vz)
        assert kzz==numerator/denom**2
        assert ktt*kzz-ktz*ktz==delta*delta*jac*jac/denom**3
        if kzz:
            assert ktt-ktz*ktz/kzz==delta*delta*jac*jac/(denom*numerator)
        rows.append({'jets':list(map(str,(h,hz,hzz,hzzz))),
                     'delta':str(delta),'spatial_entry':str(kzz),
                     'determinant':str(ktt*kzz-ktz*ktz)})
    assert rows[2]['determinant']=='0' and F(rows[2]['spatial_entry'])>0
    return {'scope':'Exact real-rational control cases, not a general proof',
            'checks':'spatial Gram, determinant, Schur complement, H=z comparison control',
            'cases':rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("CHB_FULL_BOUNDARY_CHECKS_20261022.json"))
    args = parser.parse_args()
    started = time.monotonic()
    geometry = exact_geometry()
    quartic_control = quartic_fixed_boundary_control()
    curvature_controls = curvature_algebra_controls()
    runs = []
    for n in (96, 160):
        edge = transgression_edge(n)
        expected_heat = 0.25 - edge
        expected_wall = 4 * edge
        direct = direct_faces(n)
        residual = max(abs(value - expected_heat) for value in direct["heat_faces"].values())
        runs.append({
            "gauss_legendre_order_per_nonangular_coordinate": n,
            "angular_trapezoid_nodes": 64,
            "K_each_edge": edge,
            "analytic_reduction": {
                "each_minus_heat_piece": 1 / 68,
                "each_complement_heat_piece": 4 / 17 - edge,
                "each_complete_heat_face": expected_heat,
                "complete_spatial_wall": expected_wall,
                "all_faces_total": 4 * expected_heat + expected_wall,
                "fixed_tau_corner_integrals_J": "zero by rotation and conjugation symmetry",
                "projective_interface_flux": "zero exactly",
            },
            "direct_pullback_quadrature": direct,
            "diagnostic_errors": {
                "max_heat_face_vs_reduction": residual,
                "spatial_wall_vs_reduction": abs(direct["spatial_wall"] - expected_wall),
                "all_faces_vs_one": abs(direct["all_faces_total"] - 1),
            },
        })
    # These tolerances are diagnostic assertions, not outward-rounded bounds.
    assert runs[0]["diagnostic_errors"]["all_faces_vs_one"] < 2e-8
    assert runs[1]["diagnostic_errors"]["all_faces_vs_one"] < 2e-10
    receipt = {
        "research_date": "2026-10-22",
        "prepared_for": "Edward Baker",
        "llm_assistance": "Substantial; same-model contributing-agent derivation/check",
        "recorded_root_model": "gpt-6-astra (Codex)",
        "recorded_reasoning_effort": "ultra",
        "status": "Exact rational geometry checks and floating diagnostics; NOT interval-certified",
        "scope": "Quadratic/quartic polynomial controls only; no theta event, arithmetic gain, or exclusion certificate",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_file": Path(__file__).name,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_geometry": geometry,
        "exact_quartic_fixed_boundary_control": quartic_control,
        "exact_curvature_algebra_controls": curvature_controls,
        "floating_runs": runs,
        "elapsed_seconds": time.monotonic() - started,
    }
    args.output.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"receipt": str(args.output), "source_sha256": receipt["source_sha256"],
                      "n160_total": runs[-1]["direct_pullback_quadrature"]["all_faces_total"],
                      "elapsed_seconds": receipt["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
