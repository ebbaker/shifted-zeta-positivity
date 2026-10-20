#!/usr/bin/env python3
"""Four fixed whole-cell tests beyond the inherited x=1001 edge.

Prepared for Edward Baker, 20 October 2026, with substantial LLM
assistance. gpt-6-astra, reasoning effort ultra. Same-model internal work.
Reuses an exactly pinned 160-bit source acquisition; it does not present
192/256-bit arithmetic replay as fresh source quadrature.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as F
from pathlib import Path
import platform
import signal
import subprocess
import sys
import time

sys.dont_write_bytecode = True
from flint import arb, ctx
import flint

HISTORICAL_COMMIT = "ad4783b067548a10b8bfa65de8b4a0a47b1aa924"
SOURCE_REL = Path("papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer")
EXPECTED_BASE_SHA = "e96feb2b4c3e84de3025713b486fb8cf99fdd810f61366b79a0da188eb12535f"
EXPECTED_SETUP_SHA = "c5598f9dfcc9ba0601b85989703a1e945db54beaf91396258e9758a8a9f3604f"
T0, T1 = F(99999, 10**6), F(100001, 10**6)
XC, TC = F(1000), F(21, 200)
X0, X1 = F(1001), F(1002)
ADDED_CAP = "1e-6"
STRICT_MARGIN = "1e-6"


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def A(q):
    return arb(q.numerator) / q.denominator if isinstance(q, F) else arb(q)


def interval(a, b):
    return arb(A((a + b) / 2), A((b - a) / 2))


def dyadic(x):
    check(x.is_finite() and x.is_exact(), "finite exact dyadic required")
    m, e = x.man_exp()
    return {"mantissa": str(m), "exponent": int(e)}


def rec(x):
    check(x.is_finite(), "cannot serialize nonfinite ball")
    return {
        "display": x.str(50, more=True),
        "lower_dyadic": dyadic(x.lower()),
        "upper_dyadic": dyadic(x.upper()),
    }


def poly(cs, x):
    out = cs[-1]
    for c in reversed(cs[:-1]):
        out = out*x+c
    return out


def pin_sources(repo):
    folder = repo / SOURCE_REL
    basepath, setuppath = folder/"high_height_consumer.py", folder/"SETUP.json"
    check(digest(basepath) == EXPECTED_BASE_SHA, "imported source code hash changed")
    check(digest(setuppath) == EXPECTED_SETUP_SHA, "imported source acquisition hash changed")
    spec = importlib.util.spec_from_file_location("bw09_pinned_high_height", basepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    data = json.loads(setuppath.read_text())
    # Current code matches. Do not call validate_setup(data,repo), which would
    # compare the old manuscript manifest to an intentionally expanded document.
    # Instead verify every original manuscript byte against its pinned Git state.
    module.validate_setup(data)
    note = data["source_pins"]["note11"]
    check(digest(repo/note["path"]) == note["sha256"], "nonstationary theorem hash changed")
    mismatch = []
    for entry in data["source_pins"]["manuscript_tex_manifest"]:
        raw = subprocess.check_output(
            ["git", "show", HISTORICAL_COMMIT+":"+entry["path"]], cwd=repo,
            stderr=subprocess.PIPE,
        )
        check(hashlib.sha256(raw).hexdigest() == entry["sha256"],
              "historical manuscript hash mismatch: "+entry["path"])
        if digest(repo/entry["path"]) != entry["sha256"]:
            mismatch.append(entry["path"])
    canonical = json.dumps(data["source_pins"]["manuscript_tex_manifest"],
                           sort_keys=True, separators=(",", ":")).encode()
    check(hashlib.sha256(canonical).hexdigest() ==
          data["source_pins"]["manuscript_tex_manifest_sha256"],
          "original manuscript manifest aggregate mismatch")
    original = {row["path"]:row["sha256"]
                for row in data["source_pins"]["manuscript_tex_manifest"]}
    main = data["source_pins"]["manuscript_main"]
    check(original.get(main["path"]) == main["sha256"],
          "original main-source pin absent from verified manifest")
    current_pins = module.source_pins(repo)
    current = {row["path"]:row["sha256"]
               for row in current_pins["manuscript_tex_manifest"]}
    current_diff = {
        "added": sorted(set(current)-set(original)),
        "removed": sorted(set(original)-set(current)),
        "changed": sorted(p for p in set(current)&set(original)
                          if current[p] != original[p]),
    }
    return module, data, {
        "base_code": {"path": str(basepath.relative_to(repo)), "sha256": digest(basepath)},
        "setup": {"path": str(setuppath.relative_to(repo)), "sha256": digest(setuppath)},
        "note11": note,
        "original_manuscript_commit": HISTORICAL_COMMIT,
        "original_manuscript_manifest": data["source_pins"]["manuscript_tex_manifest"],
        "original_manuscript_manifest_sha256": data["source_pins"]["manuscript_tex_manifest_sha256"],
        "original_manuscript_manifest_verified_from_git": True,
        "original_main_pin_verified": True,
        "current_manuscript_files_changed_since_acquisition": mismatch,
        "current_complete_source_pins": current_pins,
        "current_vs_original_manuscript_manifest": current_diff,
        "cache_mutated": False,
    }


def tail_bounds(bits):
    ctx.prec = bits
    pi = arb.pi()
    d = pi/8-4*arb(1000).log()/1000
    c, sine = (4*d).cos(), (4*d).sin()
    m, U, Tmax = 12, arb(2), arb(1)/5
    # Keep the old majorant's left endpoint x=999. Revalidate new right
    # endpoint x=1002; the complete-theta mode estimate depends on it.
    normleft = arb(1000)**(arb(9)/4)*d.exp()
    B = 4*c*pi*m*m-9
    P = 4*sine*pi*m*m-arb(1002)-2*Tmax*d
    ratio = (arb(m+1)/m)**4*(-c*pi*(2*m+1)).exp()
    check(d > 0 and d < pi/8 and c > 0 and sine > 0,
          "frozen shift admissibility")
    check(B > 0 and P > 0 and 8*c*pi*m*m >= Tmax and ratio < 1,
          "new whole-domain mode admissibility")
    S = (2*pi*pi*m**4+3*pi*m*m)*(-c*pi*m*m).exp()/(1-ratio)
    modes, sources, Ds, Cs = [], [], [], []
    for j in range(2):
        Q = sum((math.comb(j, k)*d**(j-k)*math.factorial(k)/B**k
                 for k in range(j+1)), arb(0))
        modes.append((normleft*2*S*Q/P).upper())
        source = arb(0)
        for n in range(1, m):
            lam = pi*n*n
            D = 4*c*lam*(4*U).exp()-9-2*Tmax*U-arb(j)/(U+d)
            C = 16*c*lam*(4*U).exp()-2*Tmax
            check(D > 0 and C > 0, "retained-source tangent admissibility")
            Ds.append(D.lower())
            Cs.append(C.lower())
            source += ((2*lam*lam+3*lam)*(U+d)**j
                       *(Tmax*U*U+9*U-c*lam*(4*U).exp()).exp()/D)
        sources.append((normleft*source).upper())
    return modes, sources, {
        "shift_d": rec(d), "cos_4d": rec(c), "sin_4d": rec(sine),
        "B": rec(B), "new_phase_gap_at_x1002": rec(P),
        "geometric_ratio": rec(ratio),
        "eight_c_pi_m2_minus_Tmax": rec(8*c*pi*m*m-Tmax),
        "minimum_source_D": rec(min(Ds)),
        "minimum_source_concavity": rec(min(Cs)),
        "normalized_mode_tail": [rec(x) for x in modes],
        "normalized_retained_source_tail": [rec(x) for x in sources],
        "physical_derivative_orders": [0, 1],
    }


def execute_precision(module, setup, bits):
    started = time.monotonic()
    ctx.prec = bits
    cached = setup["setup"]
    moments, quadrature_radii = [], []
    for j, row in enumerate(cached["midpoint_jets"]):
        check(row["j"] == j, "cached moment order mismatch")
        value = module.undyadic(row["midpoint_dyadic"])
        radius = module.undyadic(row["quadrature_radius_dyadic"])
        check(radius >= 0, "negative cached quadrature radius")
        moments.append(value)
        quadrature_radii.append(radius)
    check(len(moments) == 51, "incomplete cached finite-integral derivative list")
    M = module.undyadic(cached["common_moment_dyadic"])
    check(M > 0, "nonpositive imported derivative majorant")
    modes, sources, admissibility = tail_bounds(bits)

    # This is the explicit extension proof's full geometric domain check:
    # every spatial Taylor segment stays in x>=999; every time Taylor
    # segment stays inside the original [1/100,1/5] majorant interval.
    check(F(1,100) <= T0 <= T1 <= F(1,5), "event time outside derivative domain")
    check(F(1,100) <= TC <= F(1,5), "Taylor time center outside derivative domain")
    check(F(999) <= XC <= X0 <= X1, "Taylor path outside retained derivative domain")
    check(1+24+2*(12+1) <= 52, "required derivative exceeds imported bound")
    check(1+24+2*12 < len(moments), "required midpoint derivative absent")
    fact = [math.factorial(j) for j in range(53)]
    dt = interval(T0,T1)-A(TC)
    Delta = A(max(abs(T0-TC), abs(T1-TC)))
    edges = [X0+F(k,4) for k in range(5)]
    check(edges[0] == X0 and edges[-1] == X1 and
          all(b-a == F(1,4) for a,b in zip(edges,edges[1:])),
          "fixed closed-cell coverage failed")
    rows = []
    for x0,x1 in zip(edges,edges[1:]):
        dx = interval(x0,x1)-A(XC)
        R = A(max(abs(x0-XC),abs(x1-XC)))
        rem = (M*(R**25/fact[25]+R.exp()*Delta**13/fact[13])).upper()
        tw = [Delta**k/fact[k] for k in range(13)]
        sw = [R**l/fact[l] for l in range(25)]
        values, payments = [], []
        for j in range(2):
            coefficients = [
                poly([(-1)**k*moments[j+l+2*k]/fact[k] for k in range(13)],dt)/fact[l]
                for l in range(25)
            ]
            image = poly(coefficients,dx)
            quad = sum((sw[l]*tw[k]*quadrature_radii[j+l+2*k]
                        for l in range(25) for k in range(13)),arb(0)).upper()
            total = (rem+quad+modes[j]+sources[j]).upper()
            # This is a NEW predeclared allowance. The original evaluator
            # retains its 1e-8 cap and is not called beyond its domain.
            check(total < arb(ADDED_CAP), "new 1e-6 added-error allowance failed")
            physical = image+arb(0,total)
            values.append(physical)
            payments.append({
                "polynomial_image": rec(image), "taylor": rec(rem),
                "quadrature": rec(quad), "mode": rec(modes[j]),
                "source": rec(sources[j]), "total": rec(total),
            })
        lowers = [v.abs_lower() for v in values]
        selected = 0 if lowers[0] >= lowers[1] else 1
        passed = bool(lowers[selected] > arb(STRICT_MARGIN))
        rows.append({
            "time": [str(T0),str(T1)], "space": [str(x0),str(x1)],
            "closed_cell": True, "R": rec(R), "Delta": rec(Delta),
            "physical_H_over_Gstar": rec(values[0]),
            "physical_Hx_over_Gstar": rec(values[1]),
            "selected_component": ["H","Hx"][selected],
            "selected_sign": "positive" if values[selected] > 0 else (
                "negative" if values[selected] < 0 else "undetermined"),
            "selected_absolute_lower": rec(lowers[selected]),
            "payments": payments,
            "passes_predeclared_margin": passed,
        })
    min_margin = min(module.undyadic(row["selected_absolute_lower"]["lower_dyadic"])
                     for row in rows)
    max_error = max(module.undyadic(payment["total"]["upper_dyadic"])
                    for row in rows for payment in row["payments"])
    passed = all(row["passes_predeclared_margin"] for row in rows)
    controls = []
    # Same strict first-jet selector on the control's own exact heat
    # polynomial. The event is on the shared seam of two closed cells;
    # no theta source error or scale is assigned to this polynomial.
    for left,right in [(F(4005,4),F(2003,2)),(F(2003,2),F(4007,4))]:
        y = interval(left,right)-A(F(2003,2))
        tau = interval(T0,T1)-A(F(1,10))
        h, hx = module.square(y)-2*tau, 2*y
        rejected = not bool(max(h.abs_lower(),hx.abs_lower()) > arb(STRICT_MARGIN))
        check(rejected, "own-polynomial exact seam event was falsely excluded")
        controls.append({
            "field": "H=(x-1001.5)^2-2(t-0.1)",
            "space": [str(left),str(right)],
            "time": [str(T0),str(T1)],
            "own_polynomial_H": rec(h), "own_polynomial_Hx": rec(hx),
            "source_error": "0; exact polynomial, not theta-normalized",
            "exact_event_on_closed_seam_rejected": rejected,
        })
    return {
        "arithmetic_precision_bits": bits,
        "imported_source_acquisition_precision_bits": setup["actual_precision_bits"],
        "status": "pass" if passed else "bounded_failure_no_subdivision",
        "domain_checks": {
            "time_and_Taylor_paths_in_original_derivative_time_domain": True,
            "spatial_paths_in_x_ge_999_extension": True,
            "maximum_required_midpoint_order": 49,
            "maximum_required_remainder_order": 51,
            "imported_common_derivative_order": 52,
            "majorant_extension_reason": "fixed positive normalization; e^(-d x) decreases for d>0, so original bound at xmin999 controls every real x>=999",
            "retained_derivative_majorant_over_Gstar": rec(M),
            "complete_four_closed_quarter_cells_verified": True,
        },
        "admissibility": admissibility,
        "cells": rows,
        "minimum_coordinate_margin_over_Gstar": rec(min_margin),
        "maximum_added_component_error_over_Gstar": rec(max_error),
        "new_midpoint_quadratures": 0,
        "new_majorant_quadratures": 0,
        "own_polynomial_negative_controls": controls,
        "seconds": time.monotonic()-started,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args = parser.parse_args()
    started = time.monotonic()
    def expired(signum,frame):
        raise TimeoutError("predeclared 300 second whole-run limit")
    signal.signal(signal.SIGALRM,expired)
    signal.setitimer(signal.ITIMER_REAL,300)
    report = {
        "date": "2026-10-20", "timezone": "America/New_York",
        "prepared_for": "Edward Baker",
        "model": "gpt-6-astra", "reasoning_effort": "ultra",
        "llm_assistance": "substantial; same-model internal verification",
        "python": platform.python_version(), "python_flint": flint.__version__,
        "wrapper_sha256": digest(__file__),
        "predeclared": {
            "domain": {"time": [str(T0),str(T1)],"space": [str(X0),str(X1)]},
            "arithmetic_precisions_bits": [192,256],
            "fixed_cell_count_per_precision": 4,
            "spatial_cell_width": "1/4",
            "whole_time_interval_on_every_cell": True,
            "maximum_added_component_error_over_Gstar": ADDED_CAP,
            "strict_coordinate_margin_over_Gstar": STRICT_MARGIN,
            "whole_run_limit_seconds": 300,
            "scan_or_adaptive_repair": False,
        },
        "normalization": "fixed positive Gstar=1000^(7/4)*exp(-125*pi), never differentiated",
        "comparison": "No phase or consumer advantage claimed; winding comparison fields unavailable",
        "scope": "Only first-jet event exclusion on this exact closed box; no later-event or global-threshold conclusion",
    }
    try:
        module,setup,pins = pin_sources(args.repo.resolve())
        report["source_pins"] = pins
        report["arithmetic_replays"] = [
            execute_precision(module,setup,bits) for bits in (192,256)
        ]
        report["status"] = ("pass" if all(r["status"]=="pass" for r in
                                        report["arithmetic_replays"]) else "bounded_failure")
    except Exception as exc:
        report.update(status="bounded_failure",failure_type=type(exc).__name__,
                      failure_message=str(exc))
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
    report["elapsed_seconds"] = time.monotonic()-started
    args.output.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({
        "status":report["status"], "elapsed_seconds":report["elapsed_seconds"],
        "precisions":[{"bits":r["arithmetic_precision_bits"],"status":r["status"],
                       "margin":r["minimum_coordinate_margin_over_Gstar"]["display"],
                       "max_added_error":r["maximum_added_component_error_over_Gstar"]["display"]}
                      for r in report.get("arithmetic_replays",[])],
        "failure":report.get("failure_message"),
    },indent=2))
    return 0 if report["status"]=="pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
