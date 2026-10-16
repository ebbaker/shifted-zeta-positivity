#!/usr/bin/env python3
"""Checks specific to the response to review_20260913.md.

Python 3 and NumPy. Prints JSON, without editing source files.
Exact rational checks concern the cutoff search logic and prime row sums.
Floating-point checks are diagnostics for the additional bounds and source
projection, not interval certificates or proofs of the analytic theorems.
No arithmetic Schur positivity certificate is computed.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import numpy as np


def rational_checks():
    row_cases = 0
    for h in range(1, 25):
        for q in (F(1, 7), F(1, 2), F(7, 8)):
            rows = [
                sum((q ** j for j in range(1, i)), F(0))
                + sum((q ** j for j in range(1, h - i + 1)), F(0))
                for i in range(1, h + 1)
            ]
            central = q / (1 - q) * (
                2 - q ** ((h - 1) // 2) - q ** (h // 2)
            )
            assert max(rows) == central
            row_cases += 1

    # Synthetic exact constants: the first candidate equals the threshold.
    # All enclosure widths are exactly 2**(-r). This checks the search
    # convention, not the implementation of arithmetic scalar enclosures.
    beta, delta = F(1), F(1, 16)

    def b(j):
        return beta + delta + F(j - 1, 16)

    selected = None
    for r in range(1, 20):
        half_width = F(1, 2 ** (r + 1))
        beta_upper = beta + half_width
        candidates = [
            j for j in range(1, r + 1)
            if b(j) - half_width > beta_upper + delta
        ]
        assert 1 not in candidates
        if candidates:
            selected = (min(candidates), r)
            break
    # The first non-strict admissible index is 1; the first strict one is 2;
    # the least certified index at the first successful stage is 3.
    assert selected == (3, 4), selected
    return {
        "method": "exact Fraction arithmetic",
        "central_row_cases": row_cases,
        "equality_at_first_candidate": True,
        "selected_cutoff": selected[0],
        "first_successful_stage": selected[1],
        "search_scope": "synthetic rational enclosure protocol only",
    }


def compressed_tail_diagnostics():
    ratios = []
    for length in (0.2, 1.0, 3.1):
        h = 6
        nu = np.full(h, np.sqrt(2 / length))
        nu[0] = length ** -0.5
        omega = np.arange(h) * np.pi / length
        for start in (0, 1, 10, 100):
            masses = 2 * np.arange(start, start + 8000, dtype=float) + 0.5
            aj = 2 * start + 0.5
            scalar = (1 + np.exp(-aj * length)) * (
                aj ** -2 + 1 / (2 * aj)
            )
            tail = np.zeros((h, h))
            for i in range(h):
                for j in range(h):
                    if (i - j) % 2 == 0:
                        tail[i, j] = 2 * nu[i] * nu[j] * np.sum(
                            masses ** 2
                            * (1 - (-1) ** j * np.exp(-masses * length))
                            / (
                                (masses ** 2 + omega[i] ** 2)
                                * (masses ** 2 + omega[j] ** 2)
                            )
                        )
                    assert abs(tail[i, j]) <= (
                        2 * nu[i] * nu[j] * scalar + 1e-12
                    )
            bound = 2 * (2 * h - 1) / length * scalar
            ratio = float(np.linalg.norm(tail, 2) / bound)
            assert ratio <= 1 + 1e-12
            ratios.append(ratio)
    return {
        "method": "floating-point finite tail diagnostics",
        "cases": len(ratios),
        "largest_compressed_norm_to_bound_ratio": max(ratios),
        "scope": "8,000 omitted terms sampled per case; the full-tail bound is proved in the text",
    }


def response_diagnostics():
    rng = np.random.default_rng(1309202602)
    adj = lambda x: x.conj().T
    rand = lambda m, n: rng.normal(size=(m, n)) + 1j * rng.normal(size=(m, n))
    worst_identity = 0.0
    worst_orthogonality = 0.0
    max_gap_ratio = 0.0

    def positive_sqrt(x):
        lam, v = np.linalg.eigh(x)
        assert min(lam) > 0
        return (v * np.sqrt(lam)) @ adj(v)

    for _ in range(12):
        low, high, retained = 3, 7, 4
        d = np.arange(2, high + 2, dtype=float)
        z = rand(high, high) / 5
        perturbation = adj(z) @ z
        h = np.diag(d) + perturbation
        b, a0 = rand(high, low), rand(low, low)
        a = (a0 + adj(a0)) / 2
        w = np.block([[a, adj(b)], [b, h]])
        schur = a - adj(b) @ np.linalg.solve(h, b)
        y = np.zeros((high, low), dtype=complex)
        y[:retained] = np.linalg.solve(h[:retained, :retained], b[:retained])
        residual = b - h @ y
        v0 = np.vstack([np.eye(low), -y])
        variational = adj(v0) @ w @ v0 - adj(residual) @ np.linalg.solve(h, residual)
        err = float(np.linalg.norm(schur - variational, 2))
        assert err < 1e-10
        worst_identity = max(worst_identity, err)

        gap = np.linalg.norm(adj(residual) @ residual, 2) / d[retained]
        crude_bound = (
            np.linalg.norm(b, 2) ** 2
            * (1 + np.linalg.norm(perturbation, 2) / d[0]) ** 2
            / d[retained]
        )
        assert gap <= crude_bound * (1 + 1e-12)
        max_gap_ratio = max(max_gap_ratio, float(gap / crude_bound))

        alpha = max(1.0, 1.0 - float(np.linalg.eigvalsh(w)[0]))
        t = w + alpha * np.eye(low + high)
        source = positive_sqrt(t)
        v = np.linalg.inv(h + alpha * np.eye(high))
        c = source @ np.vstack([np.eye(low), -v @ b])
        g = a + alpha * np.eye(low) - adj(b) @ v @ b
        defect = alpha * np.eye(low) + adj(b) @ (np.linalg.inv(h) - v) @ b
        gram_error = float(np.linalg.norm(adj(c) @ c - g, 2))
        orth_error = float(np.linalg.norm(adj(source[:, low:]) @ c, 2))
        assert gram_error < 1e-10 and orth_error < 1e-10
        worst_identity = max(worst_identity, gram_error)
        worst_orthogonality = max(worst_orthogonality, orth_error)
        inverse_sqrt_g = np.linalg.inv(positive_sqrt(g))
        comparison = inverse_sqrt_g @ defect @ inverse_sqrt_g
        extended_map = positive_sqrt(defect) @ np.linalg.pinv(c)
        assert abs(np.linalg.norm(extended_map, 2) ** 2
                   - np.linalg.eigvalsh(comparison)[-1]) < 1e-10
    return {
        "method": "deterministic complex floating-point diagnostics",
        "cases": 12,
        "maximum_identity_error": worst_identity,
        "maximum_high_output_pairing": worst_orthogonality,
        "largest_enclosure_gap_to_crude_bound_ratio": max_gap_ratio,
        "projected_source_and_contraction_norm": "passed",
    }


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    result = {
        "source_sha256": {
            name: hashlib.sha256((root / name).read_bytes()).hexdigest()
            for name in ("manuscript.tex", "derivations.tex")
        },
        "rational_checks": rational_checks(),
        "compressed_tail_diagnostics": compressed_tail_diagnostics(),
        "response_diagnostics": response_diagnostics(),
        "status": "all checks passed",
        "scope": "Supporting checks of the revisions; human analytic review and the arithmetic matrix conjecture remain open.",
    }
    print(json.dumps(result, indent=2))
