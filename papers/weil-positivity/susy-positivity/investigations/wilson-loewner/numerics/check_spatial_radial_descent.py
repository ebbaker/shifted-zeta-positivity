#!/usr/bin/env python3
"""Audit the fixed-sector radial-descent obstruction and the free arc state.

Standard library only. Exact rational algebra and floating-point diagnostics;
not a proof checker for the external supersymmetry/localization inputs.
See notes/SPATIAL_RADIAL_DESCENT_OBSTRUCTION_20260920.md.
"""

import argparse
import cmath
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform

from check_localization_hemisphere import integrator


def clean(poly):
    return {key: F(value) for key, value in poly.items() if value}


def add(left, right, scale=F(1)):
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, F(0)) + scale * value
    return clean(out)


def mul_var(poly, axis):
    out = {}
    for key, value in poly.items():
        shifted = list(key)
        shifted[axis] += 1
        out[tuple(shifted)] = value
    return out


def derivative(poly, axis):
    out = {}
    for key, value in poly.items():
        if key[axis]:
            shifted = list(key)
            shifted[axis] -= 1
            out[tuple(shifted)] = value * key[axis]
    return clean(out)


# Operators on P(Y,barY) exp(-Y barY), in units epsilon=1.
def q_left(poly):
    return mul_var(poly, 0)


def tq_left(poly):
    return add(mul_var(poly, 1), derivative(poly, 0), F(-1))


def q_right(poly):
    return add(mul_var(poly, 0), derivative(poly, 1), F(-1))


def tq_right(poly):
    return mul_var(poly, 1)


def radial_n(poly):
    # Coefficients of P(x) exp(-x); N=-x d/dx.
    out = {}
    for degree, value in poly.items():
        out[degree] = out.get(degree, F(0)) - degree * value
        out[degree + 1] = out.get(degree + 1, F(0)) + value
    return clean(out)


def radial_inner(left, right):
    # Real coefficients suffice for the exact adjoint checks here.
    return sum((a * b * F(math.factorial(i + j), 2 ** (i + j + 1))
                for i, a in left.items() for j, b in right.items()), F(0))


def legendre_sum(u, v, count):
    p0, p1 = 1.0, v
    terms = [math.exp(-abs(u) / 2)]
    if count > 1:
        terms.append(math.exp(-1.5 * abs(u)) * p1)
    for ell in range(2, count):
        p0, p1 = p1, ((2 * ell - 1) * v * p1 - (ell - 1) * p0) / ell
        terms.append(math.exp(-(ell + 0.5) * abs(u)) * p1)
    return math.fsum(terms)


def run(order):
    cases = []

    def exact(name, condition, detail):
        cases.append(dict(name=name, kind="exact_rational", passed=bool(condition),
                          detail=detail))

    def close(name, value, expected, tolerance=2e-11):
        error = abs(value - expected)
        cases.append(dict(name=name, kind="floating_point", error=error,
                          threshold=tolerance, passed=error <= tolerance))

    # D and the adapted R act with the same two weights on the P/S pieces.
    charge, d_charge = (F(1), F(1)), (F(1, 2), F(-1, 2))
    wedge = charge[0] * d_charge[1] - charge[1] * d_charge[0]
    exact("D_Q_not_proportional", wedge == -1, "wedge(Q,[D,Q])=-1")
    exact("D_minus_R_charge_weights", tuple(x - y for x, y in
          zip(d_charge, (F(1, 2), F(-1, 2)))) == (0, 0), "[D-R,Q]=0")

    # Evaluate the supersymmetry annihilator at the moved spatial point.
    for z in (F(-1, 3), F(1, 4), F(1, 3)):
        for scale in (F(1, 2), F(3, 2)):
            row = (-scale * z, F(1))
            old_pol = (F(1), z)
            moved_pol = (F(1), scale * z)
            residual = sum(a * b for a, b in zip(row, old_pol))
            correct = sum(a * b for a, b in zip(row, moved_pol))
            exact(f"nonclosed_dilated_scalar_z{z}_scale{scale}",
                  residual == z * (1 - scale) and residual != 0 and correct == 0,
                  f"Q residual={residual}; repolarized residual={correct}")
            # Original H basis, omitting the common 1/sqrt(2).
            old = (1 - z, 1 + z)
            moved = (1 - scale * z, 1 + scale * z)
            determinant = moved[0] * old[1] - moved[1] * old[0]
            exact(f"centered_original_basis_z{z}_scale{scale}",
                  determinant == 2 * residual, f"determinant={determinant}")

    # Exact conformal scaling of the curvature-dependent boundary locus.
    scale_root, sphere_r, y = F(3, 2), F(5, 3), F(7, 5)
    new_r, new_y = sphere_r * scale_root**2, y / scale_root
    exact("scaled_boundary_locus",
          new_y / new_r == y / sphere_r / scale_root**3,
          "normal derivative and Y/r both scale with weight 3/2")
    exact("overall_scale_fixes_field_x", new_r * new_y**2 == sphere_r * y**2,
          "r*Y^2 invariant; this scaling does not translate log x")
    # Jacobi with proposed weights +1/2,+1/2 fails at fixed epsilon=1.
    exact("equal_conformal_weights_fail_fixed_Weyl_relation",
          (F(1, 2) + F(1, 2)) * F(-1) != 0,
          "[D,[tildeQ,Q]] would equal -1, whereas [D,-I]=0")

    vacuum = {(0, 0): F(1)}
    pair = q_left(tq_right(vacuum))
    forward = q_left(tq_left(vacuum))
    reverse = tq_left(q_left(vacuum))
    exact("separated_poles_state", pair == {(1, 1): F(1)}, "P=Y*barY")
    exact("forward_order_state", forward == pair, "P=Y*barY")
    exact("reverse_order_state", reverse == {(1, 1): F(1), (0, 0): F(-1)},
          "P=Y*barY-1")
    symmetric = {key: value / 2 for key, value in add(forward, reverse).items()}
    exact("symmetric_local_composite",
          symmetric == {(1, 1): F(1), (0, 0): F(-1, 2)}, "P=Y*barY-1/2")
    exact("vacuum_left_right_Q", q_left(vacuum) == q_right(vacuum),
          "Q_L Psi0 = Q_R Psi0")
    exact("vacuum_left_right_tildeQ", tq_left(vacuum) == tq_right(vacuum),
          "tildeQ_L Psi0 = tildeQ_R Psi0")
    for a, b in ((0, 0), (1, 0), (0, 1), (2, 1), (2, 2)):
        poly = {(a, b): F(1)}
        comm = add(tq_left(q_left(poly)), q_left(tq_left(poly)), F(-1))
        exact(f"canonical_contact_on_monomial_{a}_{b}",
              comm == {key: -v for key, v in poly.items()}, "[tildeQ_L,Q_L]=-I")
        for left, right, label in ((q_left, q_right, "Q_Q"),
                                  (tq_left, q_right, "tildeQ_Q"),
                                  (tq_left, tq_right, "tildeQ_tildeQ")):
            exact(f"left_right_commute_{label}_{a}_{b}",
                  left(right(poly)) == right(left(poly)), "[left,right]=0")

    f0, f1 = {0: F(1)}, {1: F(1)}
    overlap = radial_inner(f0, f1) / radial_inner(f0, f0)
    exact("normalized_arc_overlap", overlap == F(1, 2), f"overlap/epsilon={overlap}")
    exact("pair_norm", radial_inner(f1, f1) == F(1, 4), "norm^2/epsilon^2=1/4")
    for m, n in ((0, 1), (1, 0), (1, 2), (2, 1), (2, 2)):
        f, g = {m: F(1)}, {n: F(1)}
        lhs = radial_inner(f, radial_n(g))
        rhs = radial_inner(add(f, radial_n(f), F(-1)), g)
        exact(f"ordinary_adjoint_{m}_{n}", lhs == rhs, f"N^dagger=1-N; both sides={lhs}")
    exact("self_adjoint_N_is_wrong",
          radial_inner(f0, radial_n(f1)) != radial_inner(radial_n(f0), f1),
          "<f0,N f1>=0 but <N f0,f1>=1/4")

    for ell in range(6):
        exact(f"spatial_energy_square_ell{ell}",
              F(ell * (ell + 1)) + F(1, 4) == F(2 * ell + 1, 2)**2,
              "ell(ell+1)+1/4=(ell+1/2)^2")
    for u, v in ((0.5, 0.2), (0.8, 1.0), (1.2, -1.0), (2.0, -0.4)):
        close(f"spatial_Legendre_covariance_{u}_{v}", legendre_sum(u, v, 80),
              1 / math.sqrt(2 * (math.cosh(u) - v)), 1e-13)

    r = 1.7
    epsilon = 1 / (4 * math.pi * r)
    for phi in (0.2, 0.7, 1.2, 2.1, 2.8):
        t = 2 * r * math.tan((phi - math.pi / 2) / 2)
        weyl = 1 / (1 + (t / (2 * r))**2)
        spatial = (math.cos(phi / 2) / math.sqrt(weyl),
                   math.sin(phi / 2) / math.sqrt(weyl))
        flat = ((1 - t / (2 * r)) / math.sqrt(2),
                (1 + t / (2 * r)) / math.sqrt(2))
        close(f"centered_stereographic_polarization_{phi}",
              max(abs(a - b) for a, b in zip(spatial, flat)), 0, 1e-14)

    for t1, t2 in ((-0.9, 0.2), (0.2, 0.8), (0.7, -0.3)):
        contraction_3d = (t2 - t1) / (2 * r) / (4 * math.pi * abs(t1 - t2))
        ward_1d = -epsilon * math.copysign(1, t1 - t2) / 2
        close(f"free_3d_vs_Ward_propagator_{t1}_{t2}", contraction_3d, ward_1d, 1e-15)
    close("canonical_propagator_jump", -epsilon / 2 - epsilon / 2, -epsilon, 1e-15)

    quad = integrator(order)

    def mellin(s, poly=lambda x: 1):
        return quad(lambda v: cmath.exp(s * v - math.exp(v)) * poly(math.exp(v)),
                    -60, 6, 66)

    for sigma in (0.0, 0.6, 1.5, 3.0):
        s = 0.5 - 1j * sigma
        vacuum_m = mellin(s)
        pair_m = mellin(s, lambda x: x)
        close(f"pair_Mellin_recurrence_sigma{sigma}", pair_m, s * vacuum_m)
        reverse_m = mellin(s, lambda x: x - 1)
        close(f"reverse_Mellin_recurrence_sigma{sigma}", reverse_m, (s - 1) * vacuum_m)
        # Test dilation directly by changing the argument and half-density.
        a = 0.37
        moved = quad(lambda v: cmath.exp(s * v - a / 2 - math.exp(v - a)),
                     -60, 6, 66)
        close(f"unitary_field_dilation_sigma{sigma}", moved,
              cmath.exp(-1j * sigma * a) * vacuum_m)
    spectral_pair_norm = quad(lambda sigma: (0.25 + sigma**2) /
                             (2 * math.cosh(math.pi * sigma)), -16, 16, 32)
    close("ordinary_pair_Mellin_norm", spectral_pair_norm, 0.25, 2e-13)
    return dict(schema=1, model="OpenAI GPT-6 (Codex; session-supplied identity)",
                effort="not exposed in this session; not inferred",
                python=platform.python_version(), parameters=dict(quadrature_order=order,
                mellin_log_x_bounds=[-60, 6], mellin_pieces=66, harmonic_terms=80),
                scope="Algebraic/floating-point audits of a fixed-sector obstruction; "
                      "no supersymmetry proof checker, interval certificate, spatial "
                      "Mellin dictionary, causal transfer or positivity certificate.",
                case_count=len(cases), all_pass=all(c['passed'] for c in cases), cases=cases,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                helper_sha256=hashlib.sha256(Path(__file__).with_name(
                    'check_localization_hemisphere.py').read_bytes()).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--order', type=int, default=24)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.order < 8:
        parser.error('--order must be at least 8')
    data = run(args.order)
    text = json.dumps(data, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(text)
        print(json.dumps(dict(output=str(args.output), case_count=data['case_count'],
                              all_pass=data['all_pass'])))
    else:
        print(text, end='')
    raise SystemExit(not data['all_pass'])


if __name__ == '__main__':
    main()
