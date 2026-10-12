#!/usr/bin/env python3
"""Floating-point landscape of the Dini y-transfer gate ratio (exploration tool).

Needs numpy.  Not a check programme: float64 point sampling, no error bounds.
The certified statement is made by check_dini_gate_margin.py (standard library,
directed-rounding intervals); this script locates the maxima and the zeros of
C0 that the certified run has to resolve, and evaluates the ratio at the leaf
the package's verifier reports as worst.

Gate (provenance/TRIANGLE_Y_DINI_THEOREM.independent.md of the pinned package
judegomila/dbn-lambda-01787854-candidate-audit @ a74738de):
    ratio = G h_+ / ((L/2)|C0|),  h = |LC + C'| + (g - L/2)|C|,  G = exp(y (L + g)),
    g = 1/50 - (1/2) log(max(N_min^2, e^{2L}/d_j^2) - t/16).

Prepared for Edward Baker with LLM assistance (Claude Opus 5.5, claude-opus-5-5),
12 October 2026.

Usage:  python3 explore_dini_gate_landscape.py [--nL 20001] [--ny 81] [--output rec.json]
"""
import argparse
import hashlib
import itertools
import json
import math
import platform

import numpy as np

T = 0.16125
Y0 = math.sqrt(0.0350708)
YMAX = math.sqrt(1 - 2 * T)
LEGS = [((2, 3, 5, 7, 11), 690988, 728999), ((2, 3, 5, 7), 729000, 818999),
        ((2, 3, 5), 819000, 1027999), ((2, 3), 1028000, 3840000)]
# leaves reported as worst by the package verifier (logs/triangle_y_dini_256.log)
PACKAGE_WORST = {
    (2, 3, 5, 7, 11): dict(gmask=19, L=(1.0418546566960283, 1.0543084951295314),
                           y=(0.19969058624497746, 0.20217430455339475), ratio_ub=0.99999860767275095),
    (2, 3, 5, 7): dict(gmask=15, L=(2.5190428321629144, 2.5315489667629487),
                       y=(0.20714174117022932, 0.20962545947864661), ratio_ub=0.99997108988463879),
    (2, 3, 5): dict(gmask=7, L=(0.71838681372645952, 0.72469672201858804),
                    y=(0.20714174117022932, 0.20962545947864661), ratio_ub=0.99999531405046582),
    (2, 3): dict(gmask=3, L=(3.5697049871544797, 3.9806418166682707),
                 y=(0.26675098057224422, 0.34622996644159743), ratio_ub=0.99224052112549543),
}


def cells(P, nlo, nhi):
    k = len(P)
    for gmask in range(1 << k):
        Gp = [P[i] for i in range(k) if gmask >> i & 1]
        divs = sorted((math.prod(c), c) for r in range(len(Gp) + 1) for c in itertools.combinations(Gp, r))
        for j in range(len(divs)):
            rmax = divs[j][0]
            rprev = divs[j - 1][0] if j else 0
            lmin = math.log(2) if j == 0 else math.log(nlo * rprev)
            lmax = math.log(nhi * rmax)
            yield gmask, math.prod(Gp), rprev, rmax, divs[j:], lmin, lmax


def parts(L, ys, active, rmax, nlo):
    q = np.maximum(float(nlo) ** 2, np.exp(2 * L) / rmax ** 2) - T / 16
    g = 1 / 50 - 0.5 * np.log(q)
    C0 = np.zeros_like(L)
    C = np.zeros((L.shape[0], ys.shape[1]))
    LCC = np.zeros_like(C)
    for d, ps in active:
        s = (-1) ** len(ps)
        ld = math.log(d)
        r = np.exp((T / 4) * (sum(math.log(p) ** 2 for p in ps) + ld * ld - 2 * L * ld))
        C0 += s * r
        C += s * r * d ** (-ys)
        LCC += s * (L - ld) * r * d ** (-ys)
    h = np.abs(LCC) + (g - L / 2) * np.abs(C)
    G = np.exp(ys * (L + g))
    with np.errstate(divide="ignore", invalid="ignore"):
        R = np.where(h > 0, G * h / ((L / 2) * np.abs(C0)), 0.0)
    return C0, h, R


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nL", type=int, default=20001)
    ap.add_argument("--ny", type=int, default=81)
    ap.add_argument("--output", default=None)
    a = ap.parse_args()
    ys = np.linspace(Y0, YMAX, a.ny)[None, :]
    out = {"title": "Float landscape of the Dini gate ratio", "date": "2026-10-12",
           "model": "Claude Opus 5.5 (claude-opus-5-5)", "grid": [a.nL, a.ny], "legs": []}
    for P, nlo, nhi in LEGS:
        rec = {"P": list(P), "max_ratio_covered_domain": 0.0, "max_ratio_physical": 0.0,
               "max_h_covered_domain": -1e9, "C0_zeros": []}
        for gmask, G0, rprev, rmax, active, lmin, lmax in cells(P, nlo, nhi):
            L = np.linspace(lmin, lmax, a.nL)[:, None]
            C0, h, R = parts(L, ys, active, rmax, nlo)
            i = np.unravel_index(np.argmax(R), R.shape)
            if R[i] > rec["max_ratio_covered_domain"]:
                rec["max_ratio_covered_domain"] = float(R[i])
                rec["argmax_covered"] = dict(G0=G0, sector=[rprev, rmax], L=float(L[i[0], 0]), y=float(ys[0, i[1]]))
            phys = L[:, 0] >= math.log(max(2, G0))
            if phys.any():
                Rp = R[phys]
                ip = np.unravel_index(np.argmax(Rp), Rp.shape)
                if Rp[ip] > rec["max_ratio_physical"]:
                    rec["max_ratio_physical"] = float(Rp[ip])
                    rec["argmax_physical"] = dict(G0=G0, sector=[rprev, rmax], L=float(L[phys][ip[0], 0]),
                                                  y=float(ys[0, ip[1]]))
            if h.max() > rec["max_h_covered_domain"]:
                rec["max_h_covered_domain"] = float(h.max())
            c = C0[:, 0]
            for z in np.where(np.sign(c[:-1]) * np.sign(c[1:]) <= 0)[0]:
                Lz = float(L[z + 1, 0])          # right end of the bracketing grid step
                _, hz, _ = parts(np.array([[Lz]]), ys, active, rmax, nlo)
                rec["C0_zeros"].append(dict(G0=G0, sector=[rprev, rmax], L=round(Lz, 6),
                                            n_equiv=round(math.exp(Lz), 3), max_y_h=round(float(hz.max()), 4),
                                            physical=bool(Lz >= math.log(max(2, G0)) - 1e-9)))
        w = PACKAGE_WORST[P]
        Gp = [P[i] for i in range(len(P)) if w["gmask"] >> i & 1]
        divs = sorted((math.prod(c), c) for r in range(len(Gp) + 1) for c in itertools.combinations(Gp, r))
        Lw = np.linspace(w["L"][0], w["L"][1], 101)[:, None]
        yw = np.linspace(w["y"][0], w["y"][1], 41)[None, :]
        _, _, Rw = parts(Lw, yw, divs, 1, nlo)       # the package's worst leaves all lie in sector (0, 1]
        rec["package_worst_leaf"] = dict(G0=math.prod(Gp), L=list(w["L"]), y=list(w["y"]),
                                         package_ratio_upper_bound=w["ratio_ub"],
                                         sampled_max_ratio_in_leaf=float(Rw.max()),
                                         physical=bool(w["L"][1] >= math.log(math.prod(Gp))))
        out["legs"].append(rec)
        print(json.dumps({k: v for k, v in rec.items() if k != "C0_zeros"}))
    out["software"] = {"python": platform.python_version(), "numpy": np.__version__}
    with open(__file__, "rb") as fh:
        out["script_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    js = json.dumps(out, indent=1)
    if a.output:
        open(a.output, "w").write(js + "\n")
    else:
        print(js)


if __name__ == "__main__":
    main()
