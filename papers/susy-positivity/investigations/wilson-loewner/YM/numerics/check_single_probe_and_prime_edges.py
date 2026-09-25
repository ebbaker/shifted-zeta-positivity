#!/usr/bin/env python3
"""Small floating controls; no RH, limiting theorem, or positivity certificate.

Prepared for Edward Baker with substantial GPT-6 (Codex) assistance.
Exact deployed variant and reasoning effort unavailable, not inferred.
Only NumPy is required. All arrays stay in memory.
"""
import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np


def product_transform(z, terms):
    """B(z) = product_{j>=1} sinh(2**(-j)*z)/(2**(-j)*z)."""
    z = np.asarray(z, dtype=complex)
    result = np.ones_like(z)
    for j in range(1, terms + 1):
        w = (2.0 ** (-j)) * z
        small = np.abs(w) < 1e-4
        v = np.empty_like(w)
        v[small] = 1 + w[small]**2 / 6 + w[small]**4 / 120
        v[~small] = np.sinh(w[~small]) / w[~small]
        result *= v
    return result


def prime_power_weights(limit):
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if prime[p]:
            prime[p*p::p] = False
    weights = np.zeros(limit + 1)
    for p in np.flatnonzero(prime):
        n = int(p)
        while n <= limit:
            weights[n] = np.log(float(p))
            n *= int(p)
    labels = np.flatnonzero(weights)
    return labels, weights[labels]


def bump_data(x, normalizer):
    """Independent diagnostic h: normalized exp(x-1/(1-x*x)) on (-1,1)."""
    x = np.asarray(x)
    h, hp, f = (np.zeros_like(x, dtype=float) for _ in range(3))
    inside = np.abs(x) < 1
    u = x[inside]
    d = 1 - u*u
    value = np.exp(u - 1/d) / normalizer
    logp = 1 - 2*u/d**2
    logpp = -2/d**2 - 8*u*u/d**3
    h[inside] = value
    hp[inside] = value * logp
    f[inside] = value * (0.25 - logp*logp - logpp)
    return h, hp, f


def edge_controls(cutoff, labels, weights, normalizer, order):
    x, quadrature = np.polynomial.legendre.leggauss(order)
    h, hp, _ = bump_data(x, normalizer)
    keep = (labels <= cutoff) & (labels >= cutoff*np.exp(-2))
    logs = np.log(labels[keep].astype(float))
    coeff = weights[keep] / np.sqrt(labels[keep]*float(cutoff))
    plus, minus = np.zeros(order), np.zeros(order)
    for j in range(0, order, 16):
        s = x[j:j+16, None]
        plus[j:j+16] = bump_data(np.log(cutoff) + s - logs, normalizer)[2] @ coeff
        minus[j:j+16] = bump_data(-np.log(cutoff) + s + logs, normalizer)[2] @ coeff
    expected_plus, expected_minus = hp + 0.5*h, -hp + 0.5*h
    expected_energy = float(quadrature @ (expected_plus**2 + expected_minus**2))
    observed_energy = float(quadrature @ (plus**2 + minus**2))
    error = float(np.sqrt(quadrature @ ((plus-expected_plus)**2 + (minus-expected_minus)**2)))
    return {
        "cutoff": int(cutoff), "quadrature_order": order,
        "relative_two_edge_L2_error": error/np.sqrt(expected_energy),
        "normalized_two_edge_energy": observed_energy,
        "predicted_two_edge_energy": expected_energy,
        "energy_ratio": observed_energy/expected_energy,
        "unscaled_edge_norm": np.sqrt(cutoff*observed_energy),
        "predicted_sqrt_cutoff_coefficient": np.sqrt(expected_energy),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    checks = []
    def check(name, passed, value):
        checks.append({"name": name, "passed": bool(passed), "value": value})

    # These finite product comparisons diagnose the explicit probe, not its
    # analytically proved zero-free strip or infinite convolution smoothness.
    zs = np.array([0j, 1+0j, 0.4+3j, -0.4+31j, 0.49+80j, -0.49-80j])
    b28, b40 = product_transform(zs, 28), product_transform(zs, 40)
    product_error = float(np.max(np.abs(b28/b40 - 1)))
    check('product refinement at six complex arguments', product_error < 2e-12, product_error)
    check('even product transform', np.max(np.abs(product_transform(-zs,40)-b40)) < 1e-14,
          float(np.max(np.abs(product_transform(-zs,40)-b40))))
    norm = complex(product_transform(np.array([1+0j]),40)[0])
    poles = np.array([-0.5+0j,0.5+0j])
    fp = (0.25-poles*poles)*product_transform(1+poles,40)/norm
    check('exact algebraic pole cancellation', np.max(np.abs(fp)) == 0, float(np.max(np.abs(fp))))
    lambdas = np.array([0+14j,0.4+14j,-0.4+14j,0.49+80j])
    factors = (0.25-lambdas*lambdas)**2 * product_transform(1+lambdas,40) * product_transform(1-lambdas,40) / norm**2
    check('nonzero sampled detection coefficients', np.min(np.abs(factors)) > 0, float(np.min(np.abs(factors))))
    line = np.array([0,7,14,31,80],dtype=float)
    fourier = (0.25+line*line)*product_transform(1-1j*line,40)/norm
    line_coeff = (0.25+line*line)**2 * product_transform(1+1j*line,40)*product_transform(1-1j*line,40)/norm**2
    positivity_error = float(np.max(np.abs(line_coeff-np.abs(fourier)**2)))
    check('critical-line coefficient equals squared Fourier modulus', positivity_error < 1e-12, positivity_error)

    x, w = np.polynomial.legendre.leggauss(500)
    normalizer = float(w @ np.exp(x-1/(1-x*x)))
    h, hp, f = bump_data(x, normalizer)
    moments = [float(w @ (np.exp(sign*x/2)*f)) for sign in [-1,1]]
    check('diagnostic bump pole moments', max(map(abs,moments)) < 1e-10, moments)
    energy = float(2*(w @ (hp*hp+0.25*h*h)))
    identity = float(w @ ((hp+0.5*h)**2+(-hp+0.5*h)**2))
    check('two edge energy identity', abs(identity-energy) < 1e-11, abs(identity-energy))

    # Direct numerical integration checks both integration-by-parts signs.
    q, qw = np.polynomial.legendre.leggauss(220)
    primitive_errors = []
    for s in [-0.7,-0.2,0.3,0.75]:
        up = s + (1-s)*(q+1)/2
        low = -1+(s+1)*(q+1)/2
        vp = np.exp(s/2)*(1-s)/2*(qw @ (np.exp(-up/2)*bump_data(up,normalizer)[2]))
        vm = np.exp(-s/2)*(s+1)/2*(qw @ (np.exp(low/2)*bump_data(low,normalizer)[2]))
        hs, hps, _ = bump_data(np.array([s]),normalizer)
        primitive_errors.extend([abs(vp-(hps[0]+0.5*hs[0])),abs(vm-(-hps[0]+0.5*hs[0]))])
    check('both boundary primitive identities', max(primitive_errors) < 1e-10, max(primitive_errors))

    cutoffs = [1000,10000,100000,1000000]
    labels, weights = prime_power_weights(max(cutoffs))
    rows = [edge_controls(a,labels,weights,normalizer,240) for a in cutoffs]
    fine = edge_controls(cutoffs[-1],labels,weights,normalizer,360)
    refinement = abs(fine['normalized_two_edge_energy']-rows[-1]['normalized_two_edge_energy']) / energy
    check('edge quadrature refinement', refinement < 1e-7, refinement)
    check('final two-edge profile accuracy', fine['relative_two_edge_L2_error'] < 0.03, fine['relative_two_edge_L2_error'])
    check('final normalized edge energy accuracy', abs(fine['energy_ratio']-1) < 0.03, fine['energy_ratio'])
    check('improvement over smallest cutoff', rows[-1]['relative_two_edge_L2_error'] < rows[0]['relative_two_edge_L2_error'],
          [rows[0]['relative_two_edge_L2_error'],rows[-1]['relative_two_edge_L2_error']])
    check('visible unscaled norm growth', rows[-1]['unscaled_edge_norm'] > 20*rows[0]['unscaled_edge_norm'],
          [rows[0]['unscaled_edge_norm'],rows[-1]['unscaled_edge_norm']])
    record = {
        "status": "floating diagnostics only; not proof of asymptotics, RH, or positivity",
        "prepared_for": "Edward Baker", "llm_assistance": "substantial",
        "model": "GPT-6 (Codex)", "exact_variant": "unavailable", "reasoning_effort": "unavailable",
        "baseline_commit": "f8b8622fbd687bd152dd40dcc0c4bbd4576008e5",
        "python": platform.python_version(), "numpy": np.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "parameters": {"probe_product_terms": [28,40], "prime_cutoffs": cutoffs,
                       "edge_orders": [240,360], "bump_normalization_order": 500},
        "limitations": ["No four-dimensional YM sampling.",
                        "The bump used for edge controls differs from the universal detection probe; the edge theorem applies to either.",
                        "No zeta zero list or target positive matrices were used.",
                        "Sharp prime cutoff boundary profiles only; no joint scale/cutoff limit tested."],
        "probe_coefficient_sample_moduli": [float(v) for v in np.abs(factors)],
        "bump_normalizer": normalizer, "pole_moments": moments,
        "edge_controls": rows, "refined_final_edge_control": fine,
        "checks": checks, "passed": sum(c['passed'] for c in checks), "total": len(checks),
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({"passed":record['passed'],"total":record['total'],"edge_controls":rows,
                      "refinement":refinement},indent=2))
    if record['passed'] != record['total']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
