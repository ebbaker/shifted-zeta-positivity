#!/usr/bin/env python3
"""Exact controls for paired-face phase and spatial-wall transport.

Prepared for Edward Baker, 20 October 2026, with substantial LLM assistance.
Authoring model gpt-6-astra (Codex), recorded reasoning effort max.
Standard-library rational arithmetic; no theta acquisition or sampled signs.
"""

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path


BASE = Path("papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_spacetime_topology.py")
BASE_HASH = "365a80726ee9dbdff99ab16cd00a59fe3a62cfe779700463840bbfcfac933424"
GEO = Path("papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/numerics/GEO_T1_COMPARISON_192_20261019.json")
GEO_HASH = "f2b8b9e7ef91f746bae82f46dd0c2f8a0294a0616a73a030b5be6690322fbfd8"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(root):
    if digest(root / BASE) != BASE_HASH:
        raise ValueError("inherited exact polynomial helper changed")
    spec = importlib.util.spec_from_file_location("spacetime_exact", root / BASE)
    B = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(B)
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    def add(*polys):
        result = [F(0)] * max((len(p) for p in polys), default=0)
        for p in polys:
            for i, v in enumerate(p):
                result[i] += v
        return B.trim(result)

    def scale(p, c):
        return B.trim([c * v for v in p])

    def mul(p, q):
        result = [F(0)] * max(0, len(p) + len(q) - 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                result[i + j] += a * b
        return B.trim(result)

    def gcd(p, q):
        while q:
            _, r = B.poly_divmod(p, q)
            p, q = q, r
        return B.positive_normalize(p)

    def squarefree(p):
        d = gcd(p, B.poly_derivative(p))
        return B.poly_divmod(p, d)[0]

    def has_root(p, left, right):
        if not p:
            return True
        if B.poly_eval(p, left) == 0 or B.poly_eval(p, right) == 0:
            return True
        return bool(B.root_count(B.sturm_sequence(p), left, right))

    def refine(p, left, right):
        # The polynomial supplied here is squarefree and the interval
        # contains one simple root. Keep endpoints strictly off that root.
        middle = (left + right) / 2
        denominator = 8
        while B.poly_eval(p, middle) == 0:
            middle = (left + right) / 2 + (right - left) / denominator
            denominator *= 2
        if B.poly_eval(p, left) * B.poly_eval(p, middle) < 0:
            return left, middle
        return middle, right

    def crossings(p, q, left, right):
        """All p=0 crossings, with the local degree and sign of q.

        Finite-fixture interface: nonzero endpoints of p, or identically
        zero p with a strictly positive q throughout. Common zeros reject.
        """
        if has_root(gcd(p, q), left, right):
            raise ValueError("curve passes through zero")
        if not p:
            if B.poly_eval(q, left) > 0 and not has_root(q, left, right):
                return []
            raise ValueError("curve lies on the chosen cut")
        if B.poly_eval(p, left) == 0 or B.poly_eval(p, right) == 0:
            raise ValueError("fixture endpoint needs a different cut")
        sf = squarefree(p)
        sturm = B.sturm_sequence(sf)
        rows = []
        for a, b in B.isolate_simple_roots(sf, sturm, left, right):
            for _ in range(512):
                if not has_root(q, a, b):
                    break
                a, b = refine(sf, a, b)
            else:
                raise ValueError("root separation budget exhausted")
            check(B.poly_eval(q, a) * B.poly_eval(q, b) > 0,
                  "whole isolating interval has one q sign")
            degree = (B.sign(B.poly_eval(p, b)) -
                      B.sign(B.poly_eval(p, a))) // 2
            rows.append({"interval": [str(a), str(b)],
                         "local_degree": degree,
                         "other_sign": B.sign(B.poly_eval(q, a))})
        check(len(rows) == B.root_count(sturm, left, right),
              "all distinct scalar roots retained")
        return rows

    def cut_index(real, imag, left, right):
        rows = crossings(imag, real, left, right)
        # Imaginary part crossing upward on the negative real axis is
        # clockwise relative to the principal branch.
        return -sum(r["local_degree"] for r in rows
                    if r["other_sign"] < 0)

    def physical_cut(real, imag, left, right):
        # One fixed orientation-preserving frame keeps these fixtures'
        # corner jets off the cut, including the constant negative control.
        # Multiplication by 1+3i has degree zero and multiplies R by 10.
        return cut_index(add(real, scale(imag, -3)),
                         add(scale(real, 3), imag), left, right)

    def chord(p, left, right):
        a, b = B.poly_eval(p, left), B.poly_eval(p, right)
        return B.trim([a, b - a])

    fixtures = [
        ("constant", {(0, 0): F(1)}, F(1), 0, 0, [0, 0]),
        ("simple_static_root", {(0, 1): F(1)}, F(1), 0, 0, [0, 0]),
        ("ordinary_double", B.heat_polynomial(2), F(1), -1, -1, [0, 0]),
        ("triple", B.heat_polynomial(3), F(1), -1, -1, [0, 0]),
        ("fourth_order_narrow", B.heat_polynomial(4), F(1, 4),
         -2, 0, [-1, 1]),
        ("two_ordinary_doubles_narrow",
         B.add2(B.heat_polynomial(4), {(0, 0): F(-3)}),
         F(1, 4), -2, 0, [-1, 1]),
    ]
    cases = []
    for name, original, radius, expected, expected_n, expected_k in fixtures:
        for sign in (F(1), F(-1)):
            h = B.scale2(original, sign)
            hx = B.derivative2(h, 1)
            check(not B.add2(B.derivative2(h, 0), B.derivative2(hx, 1)),
                  "exact backward heat equation")
            fminus, fplus = (B.restrict(h, 0, t) for t in (F(-1), F(1)))
            gminus, gplus = (B.restrict(hx, 0, t) if hx else []
                            for t in (F(-1), F(1)))
            C = add(mul(fplus, fminus), mul(gplus, gminus))
            D = add(mul(gplus, fminus), scale(mul(fplus, gminus), -1))
            n = cut_index(C, D, -radius, radius)
            walls = []
            wall_raw = []
            for x in (-radius, radius):
                f = B.restrict(h, 1, x)
                g = B.restrict(hx, 1, x) if hx else []
                raw = physical_cut(f, g, F(-1), F(1))
                reference = physical_cut(chord(f, F(-1), F(1)),
                                         chord(g, F(-1), F(1)), F(0), F(1))
                walls.append(raw - reference)
                wall_raw.append(raw)
            face_raw = [physical_cut(f, g, -radius, radius)
                        for f, g in ((fminus, gminus), (fplus, gplus))]
            full = wall_raw[0] + face_raw[1] - wall_raw[1] - face_raw[0]
            check(full == n + walls[0] - walls[1],
                  "relative phase plus BOTH wall transports equals full winding")
            check(full == expected and n == expected_n and walls == expected_k,
                  "expected control outcome, including overall sign invariance")

            # Independent real-zero wall-flux calculation, on the same source.
            roots = [crossings(f, g, -radius, radius)
                     for f, g in ((fminus, gminus), (fplus, gplus))]
            flux = []
            for x in (-radius, radius):
                f = B.restrict(h, 1, x)
                g = B.restrict(hx, 1, x) if hx else []
                rows = crossings(f, g, F(-1), F(1))
                flux.append(sum(r["local_degree"] * r["other_sign"] for r in rows))
            flux_winding = F(len(roots[0]) - len(roots[1]) - flux[0] + flux[1], 2)
            check(flux_winding == full, "independent root-count and wall-flux identity")
            cases.append({"name": name, "overall_sign": int(sign),
                          "box": ["-1", "1", str(-radius), str(radius)],
                          "paired_real_coefficients": [str(v) for v in C],
                          "paired_imaginary_coefficients": [str(v) for v in D],
                          "relative_face_integer": n,
                          "wall_transport_integers": walls,
                          "full_physical_winding": full,
                          "time_face_root_counts": [len(r) for r in roots],
                          "wall_flux_terms": flux})

    r = F(1, 4)
    for constant, coefficient, lower in [
        (F(0), F(120), F(3441, 32)),
        (F(-3), F(126), F(5697, 128)),
    ]:
        h = B.add2(B.heat_polynomial(4), {(0, 0): constant})
        hx = B.derivative2(h, 1)
        fm, fp = (B.restrict(h, 0, t) for t in (F(-1), F(1)))
        gm, gp = (B.restrict(hx, 0, t) for t in (F(-1), F(1)))
        C = add(mul(fp, fm), mul(gp, gm))
        D = add(mul(gp, fm), scale(mul(fp, gm), -1))
        A = 12 + constant
        check(C == [A*A, F(0), F(-576), F(0), -coefficient,
                    F(0), F(16), F(0), F(1)], "paired polynomial coefficients")
        check(D == [F(0), -48*A, F(0), F(0), F(0), F(48)],
              "paired imaginary polynomial")
        check(A*A - 576*r*r - coefficient*r**4 == lower and lower > 0,
              "whole-interval strictly positive face-product lower bound")
        # The unique zero of Hx on each wall is t=x^2/6, and H there is
        # constant - 2*x^4/3 < 0. Thus each wall contributes one cut crossing.
        for x in (-r, r):
            tstar = x*x/6
            fwall, gwall = (B.restrict(p, 1, x) for p in (h, hx))
            check(B.poly_eval(gwall, tstar) == 0,
                  "exact wall cut crossing")
            check(B.poly_eval(fwall, tstar) == constant - F(2, 3)*x**4 < 0,
                  "wall crossing lies on negative real axis")

    # Fail-closed: a double event on the final time face makes R vanish.
    h = B.add2(B.heat_polynomial(2), {(0, 0): F(2)})
    hx = B.derivative2(h, 1)
    fm, fp = (B.restrict(h, 0, t) for t in (F(-1), F(1)))
    gm, gp = (B.restrict(hx, 0, t) for t in (F(-1), F(1)))
    C = add(mul(fp, fm), mul(gp, gm))
    D = add(mul(gp, fm), scale(mul(fp, gm), -1))
    rejected = False
    try:
        cut_index(C, D, F(-1), F(1))
    except ValueError as error:
        rejected = "passes through zero" in str(error)
    check(rejected, "boundary event has no assigned winding")

    # Generic, conservative robust slit test for a complex error disk.
    def robust_slit(c_lower, d_lower, d_upper, error):
        if error < 0:
            raise ValueError("negative error")
        return (c_lower > error or d_lower > error or d_upper < -error)

    check(robust_slit(F(2), F(-3), F(3), F(1)), "positive-real robust separator")
    check(robust_slit(F(-2), F(2), F(3), F(1)), "imaginary robust separator")
    check(not robust_slit(F(-2), F(0), F(0), F(0)), "negative cut rejects")
    check(not robust_slit(F(1), F(0), F(0), F(1)), "error touching zero rejects")

    # Normalized double-event faces p_+=(y^2/2-1,y), p_-=(y^2/2+1,y).
    # For |y|<=1/2, both component errors <=1/8 force a negative-cut
    # crossing, rather than merely failing to prove its absence.
    check(F(65, 64) <= F(9, 8)**2, "upper model face modulus bound")
    check(F(97, 64) <= F(5, 4)**2, "lower model face modulus bound")
    check(F(2) < F(3, 2)**2, "rational upper bound for sqrt(2)")
    epsilon = F(1, 8)
    product_error = F(57, 16)*epsilon + 2*epsilon**2
    check(product_error == F(61, 128), "complete normalized product error")
    check(-F(47, 64) + product_error == -F(33, 128),
          "uniform strictly negative real part near the event")
    check(F(1) - product_error == F(67, 128),
          "opposite endpoint signs force an antipodal crossing")

    # Check the symmetrized complete-source kernels on exact positive
    # finite-atom heat sources. At x=k*pi/2 all needed trigonometric
    # values are rational. Put exp(h)=r, so every heat weight is exact.
    atom_cases = 0
    frequencies = [0, 1, 2, 3]
    for weights in ([F(1), F(2), F(3), F(4)],
                    [F(3, 2), F(2, 7), F(5, 4), F(1, 9)]):
        for rheat in (F(2), F(3, 2)):
            for angle in range(4):
                cosine = [F([1, 0, -1, 0][u*angle % 4]) for u in frequencies]
                sine = [F([0, 1, 0, -1][u*angle % 4]) for u in frequencies]
                jp = [sum(w*rheat**(u*u)*c
                          for w, u, c in zip(weights, frequencies, cosine)),
                      -sum(w*rheat**(u*u)*u*s
                           for w, u, s in zip(weights, frequencies, sine))]
                jm = [sum(w*rheat**(-u*u)*c
                          for w, u, c in zip(weights, frequencies, cosine)),
                      -sum(w*rheat**(-u*u)*u*s
                           for w, u, s in zip(weights, frequencies, sine))]
                direct_c = jp[0]*jm[0] + jp[1]*jm[1]
                direct_s = jp[1]*jm[0] - jp[0]*jm[1]
                kernel_c, kernel_s = F(0), F(0)
                for i, u in enumerate(frequencies):
                    for j, v in enumerate(frequencies):
                        factor = rheat**(u*u-v*v)
                        cosh = (factor + 1/factor)/2
                        sinh = (factor - 1/factor)/2
                        kernel_c += weights[i]*weights[j]*cosh*(
                            cosine[i]*cosine[j] + u*v*sine[i]*sine[j])
                        kernel_s += weights[i]*weights[j]*sinh*(
                            v*cosine[i]*sine[j] - u*sine[i]*cosine[j])
                check(direct_c == kernel_c and direct_s == kernel_s,
                      "complete paired-source kernel sign and factor")
                atom_cases += 1

    # Reuse an existing theta receipt; do not call this fresh quadrature.
    check(digest(root / GEO) == GEO_HASH, "recorded theta halfplanes unchanged")
    geo = json.loads((root / GEO).read_text())
    boundary = geo["winding"]["boundary"]
    expected_partition = [
        (["1/100", "999"], ["1/5", "999"], 0, -1),
        (["1/5", "999"], ["1/5", "1000"], 1, 1),
        (["1/5", "1000"], ["1/5", "2001/2"], 1, 1),
        (["1/5", "2001/2"], ["1/5", "1001"], 1, 1),
        (["1/5", "1001"], ["1/100", "1001"], 1, 1),
        (["1/100", "1001"], ["1/100", "1000"], 1, 1),
        (["1/100", "1000"], ["1/100", "999"], 1, 1),
    ]
    check(len(boundary) == len(expected_partition), "whole recorded boundary")
    for row, expected in zip(boundary, expected_partition):
        check((row["from"], row["to"], row["component"], row["sign"]) == expected,
              "exact face partition and required strict halfplane")
        check(F(row["margin_lower"]) > 0, "strict recorded whole-segment margin")
    check(geo["winding"]["status"] == "pass" and geo["winding"]["degree"] == 0,
          "imported zero-degree status")
    check(geo["direct"]["status"] == "pass" and geo["direct"]["calls"] == 7,
          "stronger already-successful interior baseline retained")

    return {"schema": "bw-direct-relative-phase-v1", "date": "2026-10-20",
            "prepared_for": "Edward Baker", "actual_model": "gpt-6-astra (Codex)",
            "actual_effort": "max", "llm_assistance": "substantial; author self-checks only",
            "status": "PASS", "arithmetic": "exact Fraction, Sturm root isolation",
            "scope": "finite polynomial controls and error-interface checks; no theta acquisition",
            "checks": checks, "cases": cases,
            "exact_positive_atom_kernel_cases": atom_cases,
            "wall_only_counterexample_margins": {
                "fourth_order": "3441/32",
                "two_ordinary_doubles": "5697/128"},
            "normalized_double_face_bounds": {
                "component_error_at_most": "1/8",
                "product_error_at_most": "61/128",
                "paired_real_part_at_most": "-33/128",
                "opposite_endpoint_imaginary_margins_at_least": "67/128"},
            "inherited_theta_receipt": {
                "domain": geo["winding"]["box"],
                "relative_slit_condition": "follows from Hx>0 on both complete time faces",
                "wall_transport_integers": [0, 0],
                "source_reacquired": False, "new_coverage": False,
                "winding_calls_in_old_record": geo["winding"]["calls"],
                "direct_calls_in_old_record": geo["direct"]["calls"]},
            "source_sha256": {str(BASE): BASE_HASH, str(GEO): GEO_HASH},
            "checker_sha256": digest(Path(__file__))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    record = run(args.repo_root.resolve())
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "checks": record["checks"],
                      "cases": len(record["cases"]), "output": str(args.output)}))


if __name__ == "__main__":
    main()
