#!/usr/bin/env python3
"""Real Thom integral-budget comparison with unresolved complete theta boxes.

22 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Coordinating model gpt-6.1-sol, effort ultra, verified by coordinator from
turn metadata. Delegated process configuration is not independently recorded.

Requires python-flint >=0.9.0. No external data or network is used. The
complete-source supplier and jet enclosure below are adapted from
Investigation 22's unchanged check_theta_boundary_winding.py, SHA256
ad11eea2ead62eb3a009de3ce0308dc5b94f048293cd9daca500795578926634.
The formulas, fixed box, precision and source cutoffs remain identical.
The inherited supplier was inspected and replayed before this comparison.
Tiny-radius empty support was already certified. Wider-radius pullback
emptiness is neither assumed nor established by this calculation.

The opening tiny-radius attempt is retained as a scoped failure: it does
not reach a positive integral budget before all support boxes reject.
The prospective wider variant fixes r=1e-7, b=1.5e-7, 160 bits and target
upper<3/4 before acquisition. Both variants use at most 4095 bulk ranges.
No interior nonvanishing premise is used to stop the budget algorithm.
The source now includes derivatives H through Hxxx; midpoint order 77,
complete moments through 79. Actual target support is not asserted nonempty;
uncertain pullback-support cells are retained and integrated by bounds.
"""
from __future__ import annotations

import argparse
import hashlib
import heapq
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
RADIUS = F(1, 10**7)
COLLAR = F(3, 2 * 10**7)
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
    JMAX, MOMAX = L + 2 * K + 3, L + 2 * K + 5
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

    def enclose(t0, t1, x0, x1, orders=(0, 1, 2, 3)):
        dx = interval(x0, x1) - A(xc)
        out = []
        for j in orders:
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

    # Count complete source-range acquisitions and the number of components
    # actually enclosed. Quadrature setup (78 jets) is counted separately.
    source_calls = {}

    def evaluate(category, t0, t1, x0, x1, orders=(0, 1, 2, 3)):
        count = source_calls.setdefault(category, {"range_calls": 0, "component_ranges": 0})
        count["range_calls"] += 1
        count["component_ranges"] += len(orders)
        return enclose(t0, t1, x0, x1, orders=orders)

    # The larger collar pays the complete boundary for both variants. No
    # winding polygon or vertex evaluations, and no interior cover, is used.
    boundary_leaves = []
    boundary_start = time.monotonic()

    def boundary_edge(q0, q1, depth=0):
        h, h1 = evaluate("boundary", min(q0[0], q1[0]), max(q0[0], q1[0]),
                         min(q0[1], q1[1]), max(q0[1], q1[1]), orders=(0, 1))
        floor = (h.abs_lower()**2 + h1.abs_lower()**2).sqrt().lower()
        if floor > A(COLLAR):
            boundary_leaves.append((q0, q1, floor))
            return
        if source_calls["boundary"]["range_calls"] >= 4092 or depth >= 40:
            raise RuntimeError("boundary floor acquisition limit; no integral conclusion")
        mid = tuple((a + b) / 2 for a, b in zip(q0, q1))
        boundary_edge(q0, mid, depth + 1)
        boundary_edge(mid, q1, depth + 1)

    corners = [(tlo, xlo), (thi, xlo), (thi, xhi), (tlo, xhi), (tlo, xlo)]
    for q0, q1 in zip(corners, corners[1:]):
        boundary_edge(q0, q1)
    boundary_elapsed = time.monotonic() - boundary_start
    boundary_floor = min(z[2] for z in boundary_leaves)
    check("every_complete_boundary_range_pays_wider_collar",
          all(z[2] > A(COLLAR) for z in boundary_leaves))

    def budget_run(name, radius, field, times, spatial, maximum_ranges=4095):
        """Stop using the integral upper sum alone; diagnose origins later."""
        rho_max = 4 / (arb(1).exp() * pi * A(radius)**2)
        target = arb(3) / 4
        calls = 0
        heap = []
        leaves = {}
        next_id = 0
        first_below_one = None
        previous_nonzero = None
        begin = time.monotonic()

        def acquire(lo, hi, depth):
            nonlocal calls, next_id
            calls += 1
            h, h1, h2, h3 = field(times[0], times[1], lo, hi)
            if not all(z.is_finite() for z in (h, h1, h2, h3)):
                raise RuntimeError(name + ": nonfinite jet enclosure; no integral conclusion")
            norm2_lower = (h.abs_lower()**2 + h1.abs_lower()**2).lower()
            # Product form is valid even if h2 contains zero. Some supported
            # python-flint versions dispatch interval **2 through a real
            # power routine that returns nonfinite at a sign-changing ball.
            lag = h2*h2 - h1*h3
            if norm2_lower > A(radius)**2:
                lower = upper = arb(0)
                status = "support_rejected"
            else:
                area = A((times[1]-times[0]) * (hi-lo))
                lower = (area * rho_max * min(lag.lower(), arb(0))).lower()
                upper = (area * rho_max * max(lag.upper(), arb(0))).upper()
                status = "retained_uncertain_support"
            record = {"lo": lo, "hi": hi, "depth": depth, "lower": lower, "upper": upper,
                      "status": status, "origin_in_first_jet_box": h.contains(0) and h1.contains(0),
                      "jet": (h, h1, h2, h3), "laguerre": lag}
            ident = next_id
            next_id += 1
            leaves[ident] = record
            if upper > 0:
                # Floating-point priority only chooses the next subdivision;
                # every proof comparison uses outward Arb endpoints below.
                heapq.heappush(heap, (-float(upper), ident))

        acquire(spatial[0], spatial[1], 0)
        while True:
            lower = sum((z["lower"] for z in leaves.values()), arb(0)).lower()
            upper = sum((z["upper"] for z in leaves.values()), arb(0)).upper()
            if upper < 1 and first_below_one is None:
                first_below_one = {"range_calls": calls, "upper": rec(upper)}
            if upper < target:
                status = "integral_upper_below_three_quarters"
                break
            previous_nonzero = {"range_calls": calls, "upper": rec(upper),
                                "uncertain_cells": sum(z["status"] != "support_rejected" for z in leaves.values())}
            if calls + 2 > maximum_ranges:
                status = "maximum_range_limit_inconclusive"
                break
            if not heap:
                status = "no_positive_upper_cell_inconclusive"
                break
            _, ident = heapq.heappop(heap)
            old = leaves.pop(ident)
            if old["depth"] >= 64:
                leaves[ident] = old
                status = "maximum_refinement_depth_inconclusive"
                break
            mid = (old["lo"] + old["hi"]) / 2
            acquire(old["lo"], mid, old["depth"] + 1)
            acquire(mid, old["hi"], old["depth"] + 1)

        ordered = sorted(leaves.values(), key=lambda z: z["lo"])
        check(name + "_covers_whole_domain", ordered[0]["lo"] == spatial[0]
              and ordered[-1]["hi"] == spatial[1]
              and all(a["hi"] == b["lo"] for a, b in zip(ordered, ordered[1:])))
        retained = [z for z in ordered if z["status"] != "support_rejected"]
        origin_cells = [z for z in retained if z["origin_in_first_jet_box"]]
        records = [{"x": [str(z["lo"]), str(z["hi"])], "status": z["status"],
                    "lower": rec(z["lower"]), "upper": rec(z["upper"]),
                    "origin_in_first_jet_box": z["origin_in_first_jet_box"]} for z in ordered]
        return {"name": name, "support_radius": str(radius), "target_upper": "3/4",
                "maximum_range_calls": maximum_ranges, "range_calls": calls, "component_ranges": 4*calls,
                "status": status, "integral_enclosure": [rec(lower), rec(upper)],
                "accepted_partition_cells": len(ordered), "support_rejected_cells": len(ordered)-len(retained),
                "retained_uncertain_support_cells": len(retained), "origin_containing_first_jet_boxes_after_stopping": len(origin_cells),
                "retained_positive_upper_mass": rec(sum((z["upper"] for z in retained), arb(0)).upper()),
                "first_below_one": first_below_one, "previous_nonzero_budget": previous_nonzero,
                "interior_nonvanishing_consulted_as_stopping_premise": False,
                "partition_sha256": hashlib.sha256(canonical(records)).hexdigest(),
                "retained_cell_records": [{**q, "jet_enclosures": [rec(j) for j in z["jet"]],
                                           "L1_enclosure": rec(z["laguerre"])}
                                          for q, z in zip(records, ordered) if z["status"] != "support_rejected"],
                "timing_seconds": time.monotonic() - begin}

    tiny = budget_run("tiny_radius", F(1, 10**9),
                      lambda *q: evaluate("tiny_bulk", *q), (tlo, thi), (xlo, xhi))
    tiny["scoped_comparison_outcome"] = "Failure to retain an uncertain integral contribution: all support boxes reject before a positive upper below one is reached."
    wide = budget_run("wider_radius", RADIUS,
                      lambda *q: evaluate("wide_bulk", *q), (tlo, thi), (xlo, xhi))
    wide["scoped_comparison_outcome"] = "Integral budget succeeds with positive retained uncertain-cell upper mass; actual pullback support nonemptiness is not asserted."
    check("tiny_radius_does_not_retain_uncertain_integral_cells", tiny["retained_uncertain_support_cells"] == 0)
    check("wide_integral_upper_below_one", arb(wide["integral_enclosure"][1]) < 1)
    check("wide_integral_stops_with_origin_containing_complete_first_jet_boxes",
          wide["origin_containing_first_jet_boxes_after_stopping"] > 0)
    check("wide_integral_retains_positive_uncertain_upper_mass", arb(wide["retained_positive_upper_mass"]) > 0)

    # Same 78-jet setup, but only two range components are acquired for the
    # practical coordinate direct comparator. It is deliberately run AFTER
    # the integral stopping decision and cannot supply that decision.
    direct_start = time.monotonic()
    direct_leaves = []

    def direct_cover(lo, hi, depth=0):
        h = evaluate("direct", tlo, thi, lo, hi, orders=(0, 1))
        s = separator(h)
        if s:
            direct_leaves.append((lo, hi, s[0]))
            return
        if depth >= 40:
            raise RuntimeError("direct comparator refinement limit")
        mid = (lo+hi)/2
        direct_cover(lo, mid, depth+1)
        direct_cover(mid, hi, depth+1)

    direct_cover(xlo, xhi)
    direct_elapsed = time.monotonic()-direct_start
    check("direct_baseline_reproduces_255_ranges", source_calls["direct"]["range_calls"] == 255)

    # Adverse control: H=x^2-2t on [-1,1]^2 has K=1. Its target preimage
    # of the radius-r disk is entirely interior, so the compact mass is 1.
    # The integral-budget machinery must not produce an upper below one.
    def quadratic_field(t0, t1, x0, x1):
        x, t = interval(x0, x1), interval(t0, t1)
        return (x*x-2*t, 2*x, arb(2), arb(0))

    quadratic = budget_run("quadratic_collision", F(1, 2), quadratic_field,
                           (F(-1), F(1)), (F(-1), F(1)), maximum_ranges=127)
    # This control's declared collar is b=3/4. On the time faces |H|>=1;
    # on the spatial walls |Hx|=2, so all four whole edges pay that collar.
    quadratic_boundary_floors = []
    for u0, u1, v0, v1 in [(F(-1), F(-1), F(-1), F(1)),
                           (F(1), F(1), F(-1), F(1)),
                           (F(-1), F(1), F(-1), F(-1)),
                           (F(-1), F(1), F(1), F(1))]:
        h, h1, _, _ = quadratic_field(u0, u1, v0, v1)
        floor = (h.abs_lower()**2+h1.abs_lower()**2).sqrt().lower()
        quadratic_boundary_floors.append(floor)
    check("quadratic_control_complete_boundary_pays_three_quarters_collar",
          all(z > arb(3)/4 for z in quadratic_boundary_floors))
    check("colliding_quadratic_budget_does_not_certify", arb(quadratic["integral_enclosure"][1]) >= 1)
    check("colliding_quadratic_returns_inconclusive", quadratic["status"].endswith("inconclusive"))

    # Deliberately inflated uncertainty supplies insufficiently precise
    # source information. Add the common absolute moment M to every
    # one of the four jet enclosures and keep a separate small stress budget.
    def inflated_source(*q):
        return [z + arb(0, M) for z in evaluate("inflated_error_control", *q)]

    inflated = budget_run("inflated_source_error", RADIUS, inflated_source,
                          (tlo, thi), (xlo, xhi), maximum_ranges=31)
    check("inflated_source_error_does_not_certify", inflated["status"].endswith("inconclusive")
          and arb(inflated["integral_enclosure"][1]) >= 1)
    check("boundary_event_is_refused", boundary_classifier([arb(0), arb(0)]) == "refused")

    output = {
        "date": "2026-10-22", "timezone": "America/New_York", "prepared_for": "Edward Baker",
        "llm_assistance": "Substantial LLM assistance; complete-source Arb/Acb interval enclosures.",
        "coordinating_model": "gpt-6.1-sol", "coordinating_reasoning_effort": "ultra",
        "provenance": "Coordinator verified metadata; delegated configuration not independently recorded.",
        "checker": Path(__file__).name, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "upstream_supplier": {"path": UPSTREAM_PATH, "sha256": UPSTREAM_SHA256,
                              "optional_original_hash_verified": upstream_verified,
                              "extension": "Same formulas; jets H through Hxxx, midpoint orders 0..77, moments through79."},
        "python_version": platform.python_version(), "python_flint_version": flint.__version__, "precision_bits": BITS,
        "contract": {"t": [str(tlo), str(thi)], "x": [str(xlo), str(xhi)], "orientation": "dt wedge dx",
                     "density": "s=|y|^2/r^2; exp(-s/(1-s))/(pi*r^2*(1-s)^2) for s<1, zero otherwise",
                     "global_density_upper": "4/(e*pi*r^2)", "bulk_target": "upper<3/4", "bulk_range_cap": 4095,
                     "split_rule": "Bisect x of the retained cell with largest positive integral upper; full time interval retained.",
                     "stopping_rule": "Integral upper only; interior nonvanishing and origin counts are not consulted.",
                     "collar_radius": str(COLLAR), "disclosure": "Tiny-radius empty support was previously certified; tiny attempt and source point scouting precede the wider fixed contract. No adaptive radius change within a run. Wider-radius pullback emptiness is neither assumed nor established; nonemptiness is not claimed."},
        "source": {"finite_modes": N, "source_cutoff": 1, "midpoint_jets": len(jets), "maximum_jet_order": JMAX,
                   "maximum_moment_order": MOMAX, "taylor_degrees": {"x": L, "t": K}, "moment_upper": rec(M),
                   "omitted_mode_bound": rec(mode_tail), "all_modes_source_ray_bound": rec(source_tail),
                   "complete_jet_tail": rec(jet_tail), "uniform_taylor_error_per_jet": rec(taylor_error)},
        "complete_boundary": {"method": "Adaptive whole-edge first-jet norm bounds; no winding polygon or interior proof.",
                              "status": "complete_collar_floor_certified",
                              "range_calls": source_calls["boundary"]["range_calls"], "component_ranges": source_calls["boundary"]["component_ranges"],
                              "accepted_segments": len(boundary_leaves), "minimum_norm_floor": rec(boundary_floor),
                              "collar_paid_for_both_variants": True, "vertex_evaluations": 0},
        "variants": {"tiny_radius": tiny, "wider_radius": wide},
        "direct_comparator": {"method": "Same complete source; adaptive x-only full-time coordinate separation AFTER integral result.",
                              "range_calls": source_calls["direct"]["range_calls"], "component_ranges": source_calls["direct"]["component_ranges"],
                              "accepted_strips": len(direct_leaves), "source_midpoint_jets_shared": 78,
                              "standalone_minimum_midpoint_jets_for_first_jet": 76},
        "controls": {"quadratic_exact_mass": "1", "quadratic_exact_mass_reason": "det DF=-4, L1=4; the entire radius-1/2 target disk preimage lies inside [-1,1]^2, and rho is normalized.",
                     "quadratic_collar": "3/4", "quadratic_boundary_norm_floors": [rec(z) for z in quadratic_boundary_floors],
                     "quadratic_integral_budget": quadratic,
                     "source_error_stress": inflated, "exact_boundary_event_status": "refused"},
        "cost_accounting": {"source_calls_by_consumer": source_calls,
                            "shared_midpoint_integrals": len(jets), "extra_midpoint_integrals_beyond_first_jet": 2,
                            "wide_bulk_four_component_ranges": 4*wide["range_calls"],
                            "wide_boundary_plus_bulk_range_calls": source_calls["boundary"]["range_calls"]+wide["range_calls"],
                            "direct_two_component_ranges": source_calls["direct"]["component_ranges"],
                            "assessment": "This certifies an integral upper before complete interior nonvanishing. It is not an acquisition saving: the stronger source setup, four-component bulk ranges and separately paid boundary must be charged."},
        "timing_seconds": {"source_setup": integral_elapsed, "boundary": boundary_elapsed,
                           "direct": direct_elapsed, "total": time.monotonic()-start},
        "assertions_passed": len(checks),
        "establishes": ["A complete compact degree-integral upper below one on this finite theta rectangle with positive uncertain-cell upper mass and origin-containing first-jet boxes retained.",
                        "Boundary and complete source payments are supplied; the integer index is therefore zero without using the later direct comparator."],
        "does_not_establish": ["Either nonemptiness or emptiness of the wider-radius target pullback support, a signed cancellation benefit or a speed/acquisition advantage.",
                               "New excluded height coverage, a global theta estimate, RH or endpoint simplicity."]}
    text = json.dumps(output, indent=2)+"\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
    print("PASS", len(checks), "assertions; wide integral", wide["integral_enclosure"],
          "; retained origin boxes", wide["origin_containing_first_jet_boxes_after_stopping"],
          "; bulk ranges", wide["range_calls"], flush=True)


if __name__ == "__main__":
    main()

