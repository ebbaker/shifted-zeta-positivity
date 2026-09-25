#!/usr/bin/env python3
"""Reproduce the finite-slab experiment; raw data and binaries stay outside Git.

Prepared for Edward Baker, 2026-09-24, with GPT-6 (Codex) assistance.
Reasoning effort not exposed; not inferred. Requires Python 3, NumPy, C++17.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import numpy as np

CAPACITIES = [0.0, 1.0, 2.8, 6.0]
SEEDS = [924101, 924102, 924103, 924104]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_hash(array):
    return hashlib.sha256(json.dumps(array.tolist(), separators=(",", ":"),
                                     allow_nan=False).encode()).hexdigest()


def word(points):
    out = []
    for a, b in zip(points, points[1:]):
        dx, dy = b[0] - a[0], b[1] - a[1]
        assert abs(dx) + abs(dy) == 1, (a, b)
        out.append((1 if dx > 0 else -1) if dx else (2 if dy > 0 else -2))
    return out


def geometry(ds):
    s = 1e-5
    q = 2j*s + 2*s*s/3 - 1j*s**3/18 + s**4/135
    trace = [(0, 0)]
    result = [{"capacity": 0., "tip": [0., 0.], "trace": [], "chord": [], "area": 0.}]
    def f(s, q):
        return 2*s*(1 - 2/q)
    for t in CAPACITIES[1:]:
        stop = np.sqrt(t)
        while s < stop:
            h = min(ds, stop-s)
            k1 = f(s, q)
            k2 = f(s+h/2, q+h*k1/2)
            k3 = f(s+h/2, q+h*k2/2)
            k4 = f(s+h, q+h*k3)
            q += h*(k1+2*k2+2*k3+k4)/6
            s += h
            v = tuple(np.floor([q.real+.5, q.imag+.5]).astype(int))
            if v != trace[-1]:
                trace.append(v)
        chord = []
        for r in np.linspace(0, 1, int(2/ds)+1):
            v = tuple(np.floor([r*q.real+.5, r*q.imag+.5]).astype(int))
            if not chord or v != chord[-1]:
                chord.append(v)
        loop = trace + chord[::-1]
        area = sum(a[0]*b[1]-a[1]*b[0] for a, b in zip(loop, loop[1:]))/2
        result.append({"capacity": t, "tip": [q.real, q.imag],
                       "trace": word(trace), "chord": word(chord), "area": float(area)})
    return result


def analyze(mean):
    n = len(CAPACITIES)
    k = mean[1:1+n*n].reshape(n, n)
    offset = 1+n*n
    g = mean[offset:offset+9*n].reshape(n, 3, 3)
    trans = mean[offset+9*n:].reshape(n-1, 3, 3)
    ell = np.sqrt(np.maximum(0, 2-2*np.diag(k, 1)))
    answers = {}
    for m in [1, 2, 3]:
        c = np.zeros(m)
        c[0] = 1
        rho, predicted, norm, schur_eigen = [], [1.], [1.], []
        for j in range(n-1):
            gn, gp, tn = g[j, :m, :m], g[j+1, :m, :m], trans[j, :m, :m]
            schur = gn - tn.T @ np.linalg.solve(gp, tn)
            schur = (schur+schur.T)/2
            schur_eigen.append(float(np.linalg.eigvalsh(schur)[0]))
            rho.append(np.sqrt(max(0, c@schur@c)))
            c = np.linalg.solve(gp, tn@c)
            predicted.append(float(g[j+1, 0, :m]@c))
            norm.append(float(c@gp@c))
        local_bounds, pair_bounds, dual_bounds = [0.], [0.], [0.]
        for final in range(1, n):
            local_bounds.append(sum(min(2., sum(ell[j:final]))*rho[j-1] for j in range(1, final+1)))
            pair_bounds.append(sum(np.sqrt(max(0, 2-2*k[final, j]))*rho[j-1] for j in range(1, final+1)))
            h = np.zeros(m)
            h[0] = 1.
            delta = np.zeros(final)
            for j in range(final-1, -1, -1):
                gn, gp, tn = g[j, :m, :m], g[j+1, :m, :m], trans[j, :m, :m]
                dual_schur = gp-tn@np.linalg.solve(gn, tn.T)
                delta[j] = np.sqrt(max(0, h@dual_schur@h))
                h = np.linalg.solve(gn, tn.T@h)
            dual_bounds.append(sum(rho[j-1]*sum(delta[j:]) for j in range(1, final+1)))
        diff = np.array(predicted)-k[0]
        assert min(schur_eigen) > -1e-9
        assert np.max(np.abs(diff)-pair_bounds) < 1e-9
        assert np.max(np.abs(diff)-dual_bounds) < 1e-9
        assert max(abs(np.diff(norm)+np.square(rho))) < 1e-9
        answers[str(m)] = {"prediction": predicted, "signed_error": diff.tolist(),
                           "residual_norms": list(map(float, rho)), "retained_norm_squared": norm,
                           "local_step_bound": list(map(float, local_bounds)),
                           "pair_informed_bound": list(map(float, pair_bounds)),
                           "primal_dual_bound": list(map(float, dual_bounds)),
                           "min_schur_eigenvalue": min(schur_eigen)}
    return {"plaquette": float(mean[0]), "wilson": k[0].tolist(),
            "loop_gram_min_eigenvalue": float(np.linalg.eigvalsh(k)[0]),
            "basis_gram_conditions": [float(np.linalg.cond(x)) for x in g],
            "step_distances": ell.tolist(), "models": answers}


def tau_initial_positive(series):
    x = np.asarray(series)-np.mean(series)
    den = x@x
    if den == 0:
        return 0.5
    ac = [1.]+[float(x[:-j]@x[j:]/den) for j in range(1, min(len(x)//3, 100))]
    total = 0.
    for j in range(1, len(ac)-1, 2):
        pair = ac[j]+ac[j+1]
        if pair <= 0:
            break
        total += pair
    return .5+total


def quaternion_controls():
    rng = np.random.default_rng(67201)
    sig = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])
    err = 0.
    for _ in range(100):
        a, b = rng.normal(size=(2, 4))
        a /= np.linalg.norm(a)
        b /= np.linalg.norm(b)
        c = np.r_[a[0]*b[0]-a[1:]@b[1:], a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:], b[1:])]
        mat = lambda q: q[0]*np.eye(2)-1j*np.einsum("a,aij->ij", q[1:], sig)
        err = max(err, float(np.max(np.abs(mat(a)@mat(b)-mat(c)))))
    haar = rng.normal(size=(200000, 4))
    haar /= np.linalg.norm(haar, axis=1)[:, None]
    assert err < 1e-12
    assert abs(np.mean(haar[:, 0])) < .005
    assert abs(np.mean(haar[:, 0]**2)-.25) < .005
    return {"matrix_product_error": err, "haar_q0_mean": float(haar[:, 0].mean()),
            "haar_q0_second_moment": float(np.mean(haar[:, 0]**2))}


def projection_controls():
    """Independent dense complex-unitary controls for moving projection and dual bounds."""
    rng = np.random.default_rng(912030)
    max_residual_error, max_norm_error = 0., 0.
    for _ in range(30):
        e = np.eye(7, dtype=complex)[:, 0]
        bases = []
        for j in range(5):
            b = rng.normal(size=(7, 3))+1j*rng.normal(size=(7, 3))
            b[:, 0] = e
            bases.append(np.linalg.qr(b)[0])
        us = [np.linalg.qr(rng.normal(size=(7, 7))+1j*rng.normal(size=(7, 7)))[0] for _ in range(4)]
        exact, state = e.copy(), e.copy()
        residuals = []
        ts = []
        for j, u in enumerate(us):
            t = bases[j+1].conj().T@u@bases[j]
            c = bases[j].conj().T@state
            new = bases[j+1]@t@c
            r = new-u@state
            rho2 = (c.conj()@(np.eye(3)-t.conj().T@t)@c).real
            max_residual_error = max(max_residual_error, abs(rho2-np.vdot(r, r).real))
            max_norm_error = max(max_norm_error, abs(np.vdot(state, state).real-np.vdot(new, new).real-rho2))
            residuals.append(float(np.linalg.norm(r)))
            state, exact = new, u@exact
            ts.append(t)
        delta = np.zeros(4)
        dual = e.copy()
        for j in range(3, -1, -1):
            d = us[j].conj().T@dual
            next_dual = bases[j]@bases[j].conj().T@d
            delta[j] = np.linalg.norm(next_dual-d)
            dual = next_dual
        bound = sum(residuals[j-1]*sum(delta[j:]) for j in range(1, 5))
        assert abs(np.vdot(e, state-exact)) <= bound+1e-12
    assert max_residual_error < 1e-12 and max_norm_error < 1e-12
    return {"cases": 30, "max_residual_schur_error": float(max_residual_error),
            "max_norm_loss_error": float(max_norm_error), "all_primal_dual_bounds_pass": True}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--work-dir", type=Path, required=True)
    p.add_argument("--record", type=Path, required=True)
    p.add_argument("--analyze-only", action="store_true")
    args = p.parse_args()
    work = args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    here = Path(__file__).resolve().parent
    geom, fine = geometry(1e-4), geometry(5e-5)
    assert all(x["trace"] == y["trace"] and x["chord"] == y["chord"] for x, y in zip(geom, fine))
    implicit_error = max(abs(complex(*x["tip"])+2*np.log(1-complex(*x["tip"])/2)-x["capacity"]) for x in geom[1:])
    tip_refinement_error = max(abs(complex(*x["tip"])-complex(*y["tip"])) for x, y in zip(geom, fine))
    assert implicit_error < 1e-9 and tip_refinement_error < 1e-9
    paths = work/"paths.txt"
    paths.write_text(str(len(geom))+"\n"+"\n".join(str(len(x[name]))+" "+" ".join(map(str, x[name])) for x in geom for name in ["trace", "chord"])+"\n")
    controls = quaternion_controls()
    projection_checks = projection_controls()
    config = {"L": 6, "Nt": 5, "beta": 1.6, "burn_sweeps": 600, "production_sweeps": 2400,
              "thin": 6, "proposal_delta": 1.2, "hits_per_link": 3,
              "seeds": SEEDS, "starts": ["cold", "hot", "cold", "hot"],
              "boundary": "periodic in space; open in physical Euclidean time",
              "measurements_per_chain": 400, "spatial_anchors_per_measurement": 216}
    config_hash = hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest()
    raw_manifest = work/"raw_manifest.json"
    if not args.analyze_only:
        subprocess.run(["clang++", "-std=c++17", "-O3", str(here/"sample_finite_slab.cpp"), "-o", str(work/"sampler")], check=True)
        def run(i):
            command = [str(work/"sampler"), "6", "5", "1.6", str(SEEDS[i]), str(i%2), "600", "2400", "6", "1.2", "3", str(paths)]
            with (work/f"chain{i}.txt").open("w") as out, (work/f"chain{i}.log").open("w") as log:
                subprocess.run(command, stdout=out, stderr=log, check=True)
            print(f"Finished chain {i}", flush=True)
        with ThreadPoolExecutor(max_workers=4) as pool:
            list(pool.map(run, range(4)))
        raw = []
        for i in range(4):
            f = work/f"chain{i}.txt"
            raw.append({"file": f.name, "sha256": sha(f), "content_sha256": canonical_hash(np.loadtxt(f)), "bytes": f.stat().st_size,
                        "log_file": f"chain{i}.log", "log_sha256": sha(work/f"chain{i}.log")})
        raw_manifest.write_text(json.dumps({"config_hash": config_hash, "sources": {name: sha(here/name) for name in ["sample_finite_slab.cpp", "check_finite_slab.py"]}, "raw": raw}, indent=2)+"\n")
    manifest = json.loads(raw_manifest.read_text())
    assert manifest["config_hash"] == config_hash
    assert manifest["sources"]["sample_finite_slab.cpp"] == sha(here/"sample_finite_slab.cpp")
    for item in manifest["raw"]:
        assert sha(work/item["file"]) == item["sha256"]
        assert sha(work/item["log_file"]) == item["log_sha256"]
    arrays = [np.loadtxt(work/item["file"]) for item in manifest["raw"]]
    assert all(x.shape == (400, 80) and np.isfinite(x).all() for x in arrays)
    mean = np.mean(arrays, axis=(0, 1))
    result = analyze(mean)
    perchain = [analyze(x.mean(axis=0)) for x in arrays]
    statistics = {}
    rng = np.random.default_rng(924200)
    for block in [5, 10, 20, 40]:
        blocks = [x.reshape(-1, block, 80).mean(axis=1) for x in arrays]
        means = np.vstack(blocks)
        se = means.std(axis=0, ddof=1)/np.sqrt(len(means))
        # Stratified nonoverlapping-batch bootstrap, preserving observable correlations.
        boots = [analyze(np.mean([b[rng.integers(len(b), size=len(b))].mean(axis=0) for b in blocks], axis=0)) for _ in range(400)]
        model_stats = {}
        for m in ["1", "2", "3"]:
            model_stats[m] = {}
            for key in ["prediction", "signed_error", "local_step_bound", "pair_informed_bound", "primal_dual_bound"]:
                values = np.array([v["models"][m][key] for v in boots])
                model_stats[m][key] = {"bootstrap_se": values.std(axis=0, ddof=1).tolist(), "percentile_95": np.quantile(values, [.025, .975], axis=0).tolist()}
        statistics[str(block)] = {"block_sweeps": block*6, "blocks_per_chain": len(blocks[0]),
                                 "plaquette_se": float(se[0]), "wilson_se": se[1:5].tolist(), "models": model_stats}
    checks = [list(map(json.loads, (work/f"chain{i}.log").read_text().splitlines())) for i in range(4)]
    tau = [{"plaquette": tau_initial_positive(x[:, 0]), "W1": tau_initial_positive(x[:, 2]), "W2": tau_initial_positive(x[:, 3]), "W3": tau_initial_positive(x[:, 4])} for x in arrays]
    hot_cold = {}
    for label, col in [("plaquette", 0), ("W1", 2), ("W2", 3), ("W3", 4)]:
        group = [np.vstack([arrays[i].reshape(-1, 20, 80).mean(axis=1) for i in ids])[:, col] for ids in [[0, 2], [1, 3]]]
        diff = group[1].mean()-group[0].mean()
        se = np.sqrt(sum(x.var(ddof=1)/len(x) for x in group))
        hot_cold[label] = {"hot_minus_cold": float(diff), "batch_se": float(se), "z_score": float(diff/se)}
    # Fixed basis: fit on chains 0,1; validate W on independent chains 2,3.
    train = analyze(np.mean(arrays[:2], axis=(0, 1)))
    test = analyze(np.mean(arrays[2:], axis=(0, 1)))
    split = {m: (np.array(train["models"][m]["prediction"])-test["wilson"]).tolist() for m in ["1", "2", "3"]}
    record = {"date": "2026-09-24", "prepared_for": "Edward Baker", "model": "GPT-6 (Codex)",
              "reasoning_effort": "not exposed; not inferred", "status": "exploratory Monte Carlo; not an interval certificate or mixing proof",
              "environment": {"python": sys.version, "numpy": np.__version__, "platform": platform.platform()},
              "config": config, "geometry": geom, "geometry_resolution_words_agree": True,
              "geometry_implicit_equation_error": float(implicit_error), "geometry_tip_refinement_error": float(tip_refinement_error),
              "quaternion_controls": controls, "chain_controls": checks, "estimate": result,
              "independent_projection_controls": projection_checks,
              "per_chain": perchain, "statistics": statistics, "tau_in_measurement_units": tau,
              "hot_cold": hot_cold, "split_validation_signed_error": split,
              "source_hashes": {name: sha(here/name) for name in ["sample_finite_slab.cpp", "check_finite_slab.py"]},
              "raw_manifest": manifest,
              "raw_data_policy": "Regenerate with this script in a scratch directory outside Git. Analyze-only requires its hash-checked manifest. No remote data are needed."}
    args.record.parent.mkdir(parents=True, exist_ok=True)
    args.record.write_text(json.dumps(record, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"estimate": result, "hot_cold": hot_cold, "tau": tau, "record": str(args.record)}, indent=2))


if __name__ == "__main__":
    main()
