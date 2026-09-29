# Ground-selection diagnostic, 28 September 2026

Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and reasoning effort are not exposed.

These are bounded multiprecision observations comparing the analytic Xi-kernel proxy to actual finite even Weil grounds. They are not interval certificates, prolate-candidate computations, or infinite-support evidence. Read the [diagnostic review](../../reviews/CCM_XI_GROUND_DIAGNOSTIC_20260928.md) and the [analytic target](../../notes/CCM_GROUND_SELECTION_TARGET_20260928.md) for interpretation.

From this directory, with Python and mpmath 1.3.0 installed:

```sh
python3 -B check_xi_ground_comparison.py --repo-numerics .. --digits 90 --case 5,8 --case 5,16 --case 13,8 --case 13,16 --case 13,32 --case 29,16 --case 29,32 --output fresh-90.json
python3 -B check_xi_ground_comparison.py --repo-numerics .. --digits 130 --case 13,32 --case 13,64 --case 29,32 --output fresh-130.json
python3 -B check_xi_candidate_normalization.py --repo-numerics .. fresh-normalization.json
python3 -B summarize_xi_ground_comparison.py
```

The last command verifies source bindings and precision agreement in the **saved** records and rewrites their small summary. It performs no eigensolve. Preserve historical inputs; use separate output filenames for fresh computations. No dense matrix is stored.

- [90-digit observations](xi-ground-comparison-90.json).
- [130-digit repeats and N=64 observation](xi-ground-comparison-130.json).
- [Precision and eigenbasis summary](xi-ground-comparison-summary.json).
- [Independent candidate normalization](xi-candidate-normalization.json).
- [Portable-source check](portable-source-verification.json).

The `run-sources/` directory preserves exact original generator/dependency versions and original record bytes for the hashes embedded in those runs. It is a reproducibility record, not the replay entry point. The original metadata contained an unverified model-variant label; the active metadata corrects this without altering numerical fields. The portable generator changes dependency discovery and metadata, not the mathematical routines. The source-verification record compares their syntax trees; fresh help and candidate-normalization checks were run after packaging.

The numerical centered residual \(\|(A-\rho)\widehat v\|\) is distinct from the uncentered continuum residual \(\|W_bv_b\|\) used in the analytic overlap criterion. The finite complement in the eigenbasis summary is also distinct from the uncomputed infinite Fourier tail.
