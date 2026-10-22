#!/usr/bin/env python3
"""Fixed-radius real Thom support comparison on the complete theta pilot.

22 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Coordinating model gpt-6.1-sol, effort ultra, verified by coordinator from
turn metadata. Delegated process configuration is not independently recorded.

Requires python-flint >=0.9.0. No external data or network is used. The
complete-source supplier and first-jet enclosure below are adapted from
Investigation 22's unchanged check_theta_boundary_winding.py, SHA256
ad11eea2ead62eb3a009de3ce0308dc5b94f048293cd9daca500795578926634.
The formulas, fixed box, precision and source cutoffs remain identical.
The inherited source was inspected and replayed before this comparison was
specified; its expected empty support is disclosed, not a blind discovery.

The declared radius is 1e-9, collar b=1.5e-9, 160 bits. A complete source
comparison is certified, but this estimator gains no stronger allowance:
every rejected support rectangle already excludes a common jet zero.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import time
from fractions import Fraction as F
from pathlib import Path

import flint
from flint import acb, arb, ctx

UPSTREAM_PATH = "papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_boundary_winding.py"
UPSTREAM_SHA256 = "ad11eea2ead62eb3a009de3ce0308dc5b94f048293cd9daca500795578926634"
RADIUS = F(1, 10**9)
COLLAR = F(3, 2 * 10**9)
BITS = 160


def trim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return p


def poly_eval(p, x):
    r = F(0)
    for z in reversed(p):
        r = r * x + z
    return r


def poly_deriv(p):
    return trim([i * p[i] for i in range(1, len(p))])


def poly_rem(p, q):
    p = trim(p)
    while p and len(p) >= len(q):
        delta = len(p) - len(q)
        scale = p[-1] / q[-1]
        for j, z in enumerate(q):
            p[j + delta] -= scale * z
        p = trim(p)
    return p


def sturm(p):
    seq = [trim(p), poly_deriv(p)]
    if not seq[-1]:
        return seq[:1]
    while True:
        r = poly_rem(seq[-2], seq[-1])
        if not r:
            return seq
        # Positive rescaling reduces exact-rational expression growth.
        r = [-z / abs(r[-1]) for z in r]
        seq.append(r)


def sign(v):
    return (v > 0) - (v < 0)


def variations(seq, x):
    s = [sign(poly_eval(p, x)) for p in seq]
    s = [v for v in s if v]
    return sum(a != b for a, b in zip(s, s[1:]))


def root_count(seq, lo, hi):
    if not poly_eval(seq[0], lo) or not poly_eval(seq[0], hi):
        raise ValueError("Sturm boundary root: move the exact test boundary")
    return variations(seq, lo) - variations(seq, hi)


def positive_crossings(p, lo, hi):
    seq = sturm(p)
    if len(seq[-1]) != 1:
        raise ValueError("time-face roots are not certified simple")

    def isolate(a, b):
        n = root_count(seq, a, b)
        if not n:
            return 0
        if n == 1:
            if poly_eval(p, a) * poly_eval(p, b) >= 0:
                raise AssertionError("simple-root sign change is missing")
            return int(poly_eval(p, b) > 0)
        mid = (a + b) / 2
        k = 3
        while not poly_eval(p, mid):
            mid = (a + b) / 2 + (b - a) / (2**k)
            k += 1
        return isolate(a, mid) + isolate(mid, b)

    return root_count(seq, lo, hi), isolate(lo, hi)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--upstream-checker", type=Path,
                        help="optional unchanged original file to hash-check")
    args = parser.parse_args()
    ctx.prec = BITS
    start = time.monotonic()
    checks = []

    def check(label, value):
        if not value:
            raise AssertionError(label)
        checks.append(label)

    def A(x):
        return arb(x.numerator) / x.denominator if isinstance(x, F) else arb(x)

    def interval(lo, hi):
        return arb(A((lo + hi) / 2), A((hi - lo) / 2))

    def rec(v):
        return v.str(32, more=True)

    def canonical(v):
        return json.dumps(v, sort_keys=True, separators=(",", ":")).encode()

    upstream_verified = False
    if args.upstream_checker:
        check("upstream_file_hash_matches_declared_supplier",
              hashlib.sha256(args.upstream_checker.read_bytes()).hexdigest() == UPSTREAM_SHA256)
        upstream_verified = True

    # Fixed contract; these parameters are not adapted after acquisition.
    tlo, thi, xlo, xhi = map(F, ["0.01", "0.20", "25", "45"])
    tc, xc = (tlo + thi) / 2, (xlo + xhi) / 2
    pi = arb.pi()
    N, L, K = 4, 50, 12
    JMAX, MOMAX = L + 2 * K + 1, L + 2 * K + 3
    T, DT, DX = A(thi), A((thi - tlo) / 2), A((xhi - xlo) / 2)
    check("fixed_radius_below_collar", 0 < RADIUS < COLLAR)
    check("positive_time_and_time_upper_bound", A(tlo) > 0 and T <= arb(1) / 4)

    # BEGIN COMPLETE THETA SUPPLIER, adapted without formula changes.
    # phi_n=(p_n''-p_n)/8, p_n=exp(u-pi*n^2*exp(4u)). On [0,1],
    # all moments through MOMAX have e^(t*u^2)*u^j <= exp(T).
    mode_ratio = 4 * (-pi * (2 * N + 3)).exp()
    beta_tail = 4 * pi * (N + 1)**2 * (-pi * (N + 1)**2).exp() / (1 - mode_ratio)
    mode_tail = T.exp() * beta_tail / 8
    # On u>=1 use u^j<=exp(j*(u-1)) and the decaying tangent at u=1.
    # This is an ALL-MODES source-ray bound, not a finite-mode ray bound.
    e4 = arb(4).exp()
    source_ratio = 16 * (-3 * pi * e4).exp()
    source_denom = 4 * pi * e4 - 9 - MOMAX - 2 * T
    check("source_ray_tangent_decays", source_denom > 0 and 2 * T < 16 * pi * e4)
    check("both_geometric_tail_ratios_below_one", mode_ratio < 1 and source_ratio < 1)
    source_tail = 2 * pi * pi * (T + 9 - pi * e4).exp() / source_denom / (1 - source_ratio)
    jet_tail = mode_tail + source_tail
    betas = sum(((4 * pi * n * n - 1) * (-pi * n * n).exp()
                 for n in range(1, N + 1)), arb(0))
    M = T.exp() * (betas + beta_tail) / 8 + source_tail
    taylor_error = M * (DX**(L + 1) / math.factorial(L + 1)
                       + DX.exp() * DT**(K + 1) / math.factorial(K + 1))
    integral_start = time.monotonic()
    jets = []
    for j in range(JMAX + 1):
        def ff(u, analytic):
            q = (4 * u).exp()
            phi = sum(((2 * (pi * n * n)**2 * q * q - 3 * pi * n * n * q)
                       * (-pi * n * n * q).exp() for n in range(1, N + 1)), acb(0))
            phase = A(xc) * u
            tr = (phase.cos(), -phase.sin(), -phase.cos(), phase.sin())[j % 4]
            return (A(tc) * u * u + u).exp() * phi * u**j * tr

        z = acb.integral(ff, 0, 1, abs_tol=arb("1e-35"), rel_tol=arb("1e-28"),
                         eval_limit=200000, depth_limit=30)
        check("finite_real_midpoint_integral_" + str(j), z.is_finite() and z.imag.contains(0))
        jets.append(z.real + arb(0, jet_tail))
    integral_elapsed = time.monotonic() - integral_start
    cache = {}

    def coefficients(t0, t1, j):
        key = (t0, t1, j)
        if key not in cache:
            dt = interval(t0, t1) - A(tc)
            c = []
            for l in range(L + 1):
                r = jets[l + 2 * K + j] / math.factorial(K)
                for k in range(K - 1, -1, -1):
                    r = -dt * r + jets[l + 2 * k + j] / math.factorial(k)
                c.append(r / math.factorial(l))
            cache[key] = c
        return cache[key]

    def enclose(t0, t1, x0, x1):
        dx = interval(x0, x1) - A(xc)
        out = []
        for j in (0, 1):
            if t0 == t1:
                c = coefficients(t0, t1, j)
                r = c[-1]
                for z in reversed(c[:-1]):
                    r = r * dx + z
            else:
                dt = interval(t0, t1) - A(tc)
                c = []
                for k in range(K + 1):
                    z = jets[L + 2 * k + j] / math.factorial(L)
                    for l in range(L - 1, -1, -1):
                        z = z * dx + jets[l + 2 * k + j] / math.factorial(l)
                    c.append(z / math.factorial(k))
                r = c[-1]
                for z in reversed(c[:-1]):
                    r = -dt * r + z
            out.append(r + arb(0, taylor_error))
        return out
    # END COMPLETE THETA SUPPLIER.

    def separator(v):
        choices = [(z.abs_lower(), j, 1 if z > 0 else -1)
                   for j, z in enumerate(v) if z > 0 or z < 0]
        return max(choices, key=lambda q: float(q[0])) if choices else None

    def support_classifier(v):
        """Only strict whole-rectangle separation can certify empty support."""
        floor = (v[0].abs_lower()**2 + v[1].abs_lower()**2).sqrt().lower()
        return ("support_rejected" if floor > A(RADIUS) else "inconclusive"), floor

    def boundary_classifier(v):
        floor = (v[0].abs_lower()**2 + v[1].abs_lower()**2).sqrt().lower()
        return "collar_validated" if floor > A(COLLAR) else "refused"

    # Replay practical complete boundary winding, counting every actual range
    # and vertex call. Optional historical root-count wall checks are not run.
    boundary = []
    boundary_ranges = 0

    def edge(q0, q1, depth=0):
        nonlocal boundary_ranges
        boundary_ranges += 1
        v = enclose(min(q0[0], q1[0]), max(q0[0], q1[0]),
                    min(q0[1], q1[1]), max(q0[1], q1[1]))
        s = separator(v)
        if s:
            boundary.append((q0, q1, s))
            return
        if depth >= 30:
            raise RuntimeError("boundary refinement limit")
        mid = tuple((a + b) / 2 for a, b in zip(q0, q1))
        edge(q0, mid, depth + 1)
        edge(mid, q1, depth + 1)

    boundary_start = time.monotonic()
    corners = [(tlo, xlo), (thi, xlo), (thi, xhi), (tlo, xhi), (tlo, xlo)]
    for q0, q1 in zip(corners, corners[1:]):
        edge(q0, q1)
    boundary_floor = min(s[0] for _, _, s in boundary)
    check("declared_collar_below_certified_boundary_floor", boundary_floor > A(COLLAR))
    polygon = []
    for q0, _, _ in boundary:
        v = enclose(q0[0], q0[0], q0[1], q0[1])
        polygon.append(tuple(F(float(z.mid())) for z in v))
    for i, (_, _, (_, j, s)) in enumerate(boundary):
        check("boundary_polygon_halfplane_" + str(i),
              s * polygon[i][j] > 0 and s * polygon[(i + 1) % len(polygon)][j] > 0)
    winding = 0
    for q, r in zip(polygon, polygon[1:] + polygon[:1]):
        x, y = q
        X, Y = r
        cross = x * Y - X * y
        if y <= 0 < Y and cross > 0:
            winding += 1
        elif Y <= 0 < y and cross < 0:
            winding -= 1
    check("boundary_winding_zero", winding == 0)
    check("inherited_practical_boundary_counts_reproduced",
          boundary_ranges == 464 and len(boundary) == 234)
    boundary_elapsed = time.monotonic() - boundary_start

    def strip_cover(method):
        accepted = []
        evaluations = 0
        begin = time.monotonic()

        def visit(lo, hi, depth=0):
            nonlocal evaluations
            evaluations += 1
            v = enclose(tlo, thi, lo, hi)
            s = separator(v)
            if method == "direct":
                ok = s is not None
                floor = s[0] if ok else arb(0)
            else:
                # The closest point of the interval rectangle to zero has
                # these two coordinate distances. Arb rounds outwards.
                status, floor = support_classifier(v)
                ok = status == "support_rejected"
            if ok:
                # Every accepted support rectangle also directly excludes
                # zero; there is no hidden active-support quadrature here.
                check(method + "_accepted_strip_nonzero_" + str(len(accepted)), s is not None)
                accepted.append((lo, hi, floor))
                return
            if depth >= 30:
                raise RuntimeError(method + " strip refinement limit")
            mid = (lo + hi) / 2
            visit(lo, mid, depth + 1)
            visit(mid, hi, depth + 1)

        visit(xlo, xhi)
        check(method + "_whole_rectangle_coverage", accepted[0][0] == xlo
              and accepted[-1][1] == xhi
              and all(a[1] == b[0] for a, b in zip(accepted, accepted[1:])))
        return accepted, evaluations, time.monotonic() - begin

    direct, direct_evals, direct_elapsed = strip_cover("direct")
    support, support_evals, support_elapsed = strip_cover("support")
    check("inherited_direct_counts_reproduced", len(direct) == 128 and direct_evals == 255)
    support_floor = min(z[2] for z in support)
    check("support_cover_also_pays_declared_boundary_collar",
          all(z[2] > A(COLLAR) for z in support))
    # s=|y|^2/r^2, g(s)=exp[-s/(1-s)] on s<1, zero otherwise.
    # rho_r=g(s)/[pi*r^2*(1-s)^2]=-g'(s)/(pi*r^2) is normalized.
    # No normalizer evaluation, higher jets, nonlinear products or signed
    # quadrature is needed: every complete F enclosure misses its support.
    exact_integral = ["0", "0"]
    check("every_support_rectangle_strictly_outside_support", support_floor > A(RADIUS))

    # Adverse classifier controls: uncertain or active support must not be
    # reclassified as a zero integral, and a boundary event has no collar.
    support_hit = support_classifier([arb(0), arb(0)])[0]
    unresolved = support_classifier([arb(0, A(2 * RADIUS)), arb(0, A(2 * RADIUS))])[0]
    nonzero_inside_support = support_classifier([A(RADIUS) / 2, arb(0)])[0]
    boundary_event = boundary_classifier([arb(0), arb(0)])
    point_jet = enclose(tc, tc, xc, xc)
    inflated_jet = [z + arb(0, M) for z in point_jet]
    injected_error = support_classifier(inflated_jet)[0]
    check("support_hit_returns_inconclusive", support_hit == "inconclusive")
    check("unresolved_box_returns_inconclusive", unresolved == "inconclusive")
    check("nonzero_but_inside_support_returns_inconclusive", nonzero_inside_support == "inconclusive")
    check("boundary_event_returns_refused", boundary_event == "refused")
    check("injected_first_jet_error_returns_inconclusive", injected_error == "inconclusive")

    # Collision-free backward-heat field H=x has F=(x,1), L1=0.
    # The same rejection path must accept its complete constant-Hx floor.
    linear_status, linear_floor = support_classifier([arb(0, 1), arb(1)])
    check("collision_free_linear_field_support_rejected", linear_status == "support_rejected")

    # Exact quadratic target-preimage control. F=(x^2-2t,2x) is a global
    # diffeomorphism with det DF=-4 and L1=4. On D=F^{-1}(B_1), K=1.
    # The radial compact integral equals int_0^1 -g'(s) ds; the substitution
    # v=s/(1-s) reduces it to int_0^infty exp(-v) dv. Integrate [0,1]
    # with Arb and pay its exact tail exp(-1). This avoids endpoint sampling
    # of a smooth, nonanalytic cutoff. The determinant payment is exact.
    check("quadratic_global_map_determinant", F(-2) * 2 - F(0) == -4)
    compact_radial = acb.integral(lambda v, analytic: (-v).exp(), 0, 1,
                                 abs_tol=arb("1e-35"), rel_tol=arb("1e-28"))
    check("compact_radial_control_finite_real", compact_radial.is_finite() and compact_radial.imag.contains(0))
    compact_mass = compact_radial.real + arb(-1).exp()
    check("quadratic_compact_target_preimage_mass_one", compact_mass.contains(1))
    # On the same unit target disk and lambda=1, the Gaussian integrates
    # exp(-q) dq for q=|y|^2, with correction -exp(-1), exactly.
    disk_gaussian = compact_radial.real
    disk_correction = -arb(-1).exp()
    check("quadratic_disk_gaussian_corrected_mass_one", (disk_gaussian - disk_correction).contains(1))
    check("quadratic_disk_gaussian_uncorrected_mass_not_one", disk_gaussian < arb("0.7"))

    # Exact Hermite controls: independently count oriented ray crossings on
    # both time faces; certify no H zero on either whole spatial wall using
    # rational Sturm chains. The enclosing event has order m at (0,0).
    polynomial_controls = []
    for m in range(2, 13):
        for overall in (1, -1):
            terms = {(k, m - 2 * k): F(overall * math.factorial(m) * (-1)**k,
                                               math.factorial(k) * math.factorial(m - 2 * k))
                     for k in range(m // 2 + 1)}
            delta, width = F(1, 100), F(10)
            for wall in (-width, width):
                p = [F(0)] * (m // 2 + 1)
                for (k, j), c in terms.items():
                    p[k] += c * wall**j
                check("hermite_wall_no_zero_" + str((m, overall, wall)),
                      root_count(sturm(p), -delta, delta) == 0)
            faces = []
            for t in (-delta, delta):
                p = [F(0)] * (m + 1)
                for (k, j), c in terms.items():
                    p[j] += c * t**k
                faces.append(positive_crossings(p, -width, width))
            actual_wind = faces[0][1] - faces[1][1]
            check("hermite_real_degree_" + str((m, overall)), actual_wind == -(m // 2))
            check("hermite_time_face_counts_" + str((m, overall)),
                  faces[0][0] == m % 2 and faces[1][0] == m)
            polynomial_controls.append({"order": m, "overall_sign": overall,
                                        "time_face_counts": [z[0] for z in faces],
                                        "oriented_winding": actual_wind,
                                        "real_weight_floor_m_over_2": m // 2})
    check("quadratic_boundary_event_refused",
          boundary_classifier([A(F(0)**2 - 2 * F(0)), A(2 * F(0))]) == "refused")

    # Gaussian regression: H=x^2-2t on [-1,1]^2, lambda=1, K=1.
    # Integrate t exactly by erf; independently integrate all four oriented
    # beta edges. Omitting the finite-lambda correction measurably fails.
    def integrate_real(fn):
        z = acb.integral(fn, -1, 1, abs_tol=arb("1e-35"), rel_tol=arb("1e-28"),
                         eval_limit=200000, depth_limit=30)
        check("quadratic_gaussian_integral_finite_real_" + str(len(checks)),
              z.is_finite() and z.imag.contains(0))
        return z.real

    sqrt_pi = pi.sqrt()
    gaussian_bulk = integrate_real(lambda x, analytic:
                                   (-4 * x*x).exp() * ((x*x + 2).erf() - (x*x - 2).erf())) / sqrt_pi

    def walls(t, analytic):
        E = (1 - 2*t)**2 + 4
        return -8 * (-E).exp() / E

    def faces(x, analytic):
        Eplus = (x*x - 2)**2 + 4*x*x
        Eminus = (x*x + 2)**2 + 4*x*x
        return (-2*x*x - 4) * (-Eplus).exp() / Eplus - (-2*x*x + 4) * (-Eminus).exp() / Eminus

    gaussian_correction = (integrate_real(walls) + integrate_real(faces)) / (2 * pi)
    check("quadratic_gaussian_identity_with_complete_correction",
          (gaussian_bulk - 1 - gaussian_correction).contains(0))
    check("omitting_gaussian_correction_detectably_fails", gaussian_correction < arb("-0.001"))
    check("corrected_gaussian_recovers_unit_real_weight", (gaussian_bulk - gaussian_correction).contains(1))

    poly_records = [[[str(z.numerator), str(z.denominator)] for z in q] for q in polygon]
    output = {
        "date": "2026-10-22", "timezone": "America/New_York", "prepared_for": "Edward Baker",
        "llm_assistance": "Substantial LLM assistance; Arb/Acb validation and exact-rational polynomial and polygon controls.",
        "coordinating_model": "gpt-6.1-sol", "coordinating_reasoning_effort": "ultra",
        "provenance": "Coordinator verified its metadata; delegated configuration not independently recorded.",
        "checker": Path(__file__).name, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "upstream_supplier": {"repository_path": UPSTREAM_PATH, "sha256": UPSTREAM_SHA256,
                              "optional_original_file_verified": upstream_verified,
                              "adaptation": "Copied complete-source formulas, remainder and first-jet Horner supplier; unchanged mathematical parameters."},
        "python_version": platform.python_version(), "python_flint_version": flint.__version__, "precision_bits": BITS,
        "declared_contract": {"box_t": [str(tlo), str(thi)], "box_x": [str(xlo), str(xhi)],
                              "midpoint": [str(tc), str(xc)], "support_radius": str(RADIUS), "collar_radius": str(COLLAR),
                              "density": "s=|y|^2/r^2; rho_r=exp(-s/(1-s))/(pi*r^2*(1-s)^2) for s<1, zero otherwise",
                              "target_integral_error": "0 by exact whole-cell support rejection",
                              "preacquisition_disclosure": "Inherited pilot and replay were inspected before this fixed comparison; support-empty outcome was anticipated. No radius tuning."},
        "source": {"finite_modes": N, "finite_source_cutoff": 1, "midpoint_jets": len(jets),
                   "maximum_midpoint_jet_order": JMAX, "maximum_moment_order": MOMAX,
                   "taylor_degrees": {"x": L, "t": K}, "absolute_moment_bound": rec(M),
                   "omitted_mode_bound_u_0_1": rec(mode_tail), "all_modes_source_ray_bound_u_ge_1": rec(source_tail),
                   "complete_jet_tail": rec(jet_tail), "uniform_taylor_error_each_component": rec(taylor_error)},
        "boundary_winding": {"orientation": "dt wedge dx", "accepted_segments": len(boundary),
                             "range_evaluations": boundary_ranges, "vertex_evaluations": len(polygon),
                             "total_enclosure_evaluations": boundary_ranges + len(polygon),
                             "minimum_coordinate_floor": rec(boundary_floor), "winding_exact": winding,
                             "polygon_sha256": hashlib.sha256(canonical(poly_records)).hexdigest(),
                             "optional_whole_wall_checks_performed": 0},
        "direct_baseline": {"method": "Adaptive x-only strips retaining the full time interval; one strict coordinate sign.",
                            "accepted_strips": len(direct), "range_evaluations": direct_evals,
                            "minimum_coordinate_floor": rec(min(z[2] for z in direct)), "complete_collision_allowance": ["0", "0"]},
        "compact_support": {"method": "Adaptive x-only strips; interval-rectangle norm lower bound strictly exceeds fixed r.",
                            "accepted_strips": len(support), "range_evaluations": support_evals,
                            "minimum_norm_floor": rec(support_floor), "exact_signed_integral_enclosure": exact_integral,
                            "active_support_cells": 0, "extra_Hxx_Hxxx_acquisitions": 0,
                            "nonlinear_product_or_signed_quadrature_acquisitions": 0,
                            "standalone_boundary_floor_shared_with_cover": True,
                            "standalone_enclosure_evaluations": support_evals,
                            "same_first_jet_coordinate_information_already_excludes_zero": True,
                            "strip_intervals": [[str(a), str(b)] for a, b, _ in support]},
        "cost_accounting": {"shared_midpoint_integrals": len(jets),
                            "diagnostic_actual_midpoint_control_enclosures": 1,
                            "measured_replay_total_enclosures_including_diagnostic": boundary_ranges + len(polygon) + direct_evals + support_evals + 1,
                            "standalone_winding_after_shared_supplier": boundary_ranges + len(polygon),
                            "standalone_direct_after_shared_supplier": direct_evals,
                            "standalone_support_after_shared_supplier": support_evals,
                            "boundary_first_support_if_floor_acquired_separately": boundary_ranges + support_evals,
                            "boundary_first_cost_explanation": "464 boundary ranges pay the floor, plus support ranges. The 234 polygon vertices are unnecessary when acquiring only the boundary floor.",
                            "separate_boundary_floor_assembly_after_support_cover": 0,
                            "assessment": "Support cells also pay the boundary collar by covering the entire closed rectangle; do not double-charge the separate winding replay. No stricter allowance or acquisition benefit over direct coordinate strips is established."},
        "controls": {"hermite_domain": {"t": ["-1/100", "1/100"], "x": ["-10", "10"]},
                     "hermite_real_degrees": polynomial_controls,
                     "adverse_status_tests": {"exact_support_hit": support_hit,
                                              "unresolved_support_rectangle": unresolved,
                                              "nonzero_point_inside_support": nonzero_inside_support,
                                              "exact_quadratic_boundary_event": boundary_event,
                                              "actual_midpoint_first_jet_with_added_absolute_error_M": injected_error},
                     "collision_free_linear_field": {"H": "x", "Hx": "1", "L1": "0", "status": linear_status,
                                                       "norm_floor": rec(linear_floor), "compact_mass_exact": ["0", "0"]},
                     "quadratic_target_preimage": {"map": "F=(x^2-2t,2x)", "domain": "F^{-1}(open unit target disk)",
                                                    "det_DF_exact": "-4", "L1_exact": "4", "K": 1,
                                                    "compact_mass_enclosure": rec(compact_mass),
                                                    "compact_normalization_payment": "v=s/(1-s); integral exp(-v) on [0,1] plus exact tail exp(-1)",
                                                    "gaussian_lambda": "1", "gaussian_radius": "1",
                                                    "gaussian_mass_enclosure": rec(disk_gaussian),
                                                    "gaussian_exact_expression": "1-exp(-1)",
                                                    "gaussian_boundary_correction": rec(disk_correction)},
                     "boundary_event_policy": "Exact quadratic common zero on the time-face is refused; no finite positive boundary floor exists there.",
                     "quadratic_gaussian": {"box_t": ["-1", "1"], "box_x": ["-1", "1"], "lambda": "1", "K": 1,
                                            "bulk_integral": rec(gaussian_bulk), "complete_boundary_correction": rec(gaussian_correction),
                                            "bulk_minus_correction": rec(gaussian_bulk - gaussian_correction),
                                            "identity_residual": rec(gaussian_bulk - 1 - gaussian_correction)}},
        "timing_seconds": {"shared_midpoint_integrals": integral_elapsed, "boundary_winding": boundary_elapsed,
                           "direct_strips": direct_elapsed, "support_strips": support_elapsed,
                           "total_including_controls": time.monotonic() - start},
        "assertions_passed": len(checks),
        "establishes": ["The fixed compact density has empty pullback support on this complete-source rectangle, so its signed integral is exactly zero.",
                        "The prescribed collar is paid on the boundary and by the support cover.",
                        "Every accepted support rectangle already directly excludes a common first-jet zero; this does not improve the complete allowance or acquisition cost over the practical direct baseline."],
        "does_not_establish": ["A new excluded theta region or improved Newman bound, RH, or simplicity.",
                               "A comparison with active-support signed quadrature or any obstruction to other densities, domains or bulk estimators.",
                               "An independent specialist review or formal verification."]}
    text = json.dumps(output, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
    print("PASS", len(checks), "assertions; winding", winding, "; direct", direct_evals,
          "; support", support_evals, "; exact integral [0,0]", flush=True)


if __name__ == "__main__":
    main()
