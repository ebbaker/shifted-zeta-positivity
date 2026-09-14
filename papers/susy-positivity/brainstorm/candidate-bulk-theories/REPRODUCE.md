# Reproducing the calculations

All paths below are relative to this package unless specified otherwise. The new code requires **Python 3 and NumPy** only. It does not require SciPy, SymPy, mpmath, network access, or zero data. Do not run the older certificate dependencies with Python optimization (`-O`); their rational helper uses assertions and the replay checks that optimized mode is refused.

## New identity diagnostics

From the repository root:

```bash
python3 papers/susy-positivity/brainstorm/candidate-bulk-theories/calculations/check_models.py \
  --output /tmp/susy-bulk-model-diagnostics.json
```

The recorded run used Python 3.12.14 and NumPy 2.3.5. In the Codex desktop environment the bundled Python was `/Users/ebbaker/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`; that machine-specific executable is not required by the code.

The checker:

* Compares the full two-component gamma amplitude pairing, including analytic exterior tails, with the contact-minus-exponential kernel on two complex smooth bumps at two quadrature orders.
* Checks nilpotence, harmonicity, same-range reparametrization, survival of the boundary class, collapse of exact states, and failure of raw finite-time heat protection in a finite periodic-difference control.
* Tests the finite-horizon Poisson identity, endpoint term, scattering defect, forward semigroup and mixed-adjoint cap, and the complete two-label Gram expansion on exact integer-delay matrices.
* Separately uses actual $\log2,\log3$ in continuum polynomial quadratures at specified lengths, including repeated prime powers and an inactive-prime control. The integer-delay matrices are not used as approximations to these irrational delays.
* Checks the scalar Euler derivative, the Dirac trace obstruction, Robin energy signs, coherent tower first and product-mixed variations, and both continuous residuals' Fourier transforms including their contact/mass-tail accounting.

All seeds, coefficients, lengths, quadrature orders and mass cutoffs are printed in the code or output. Matrix and quadrature diagnostics are **not proofs of continuum positivity**. The analytical derivations are in the notes. Gaussian quadrature is not accompanied by an interval error certificate; two orders and analytic identities are diagnostics, and the recorded mass-tail inequality only bounds the indicated mass truncation.

## Earlier certificates and later progress reports

From the repository root, choose a directory that does not yet exist:

```bash
python3 papers/susy-positivity/investigations/positive-factorizations/checks/replay.py \
  --output-dir /tmp/susy-bulk-prior-replay
```

This copies the historical checkers to a temporary directory, runs them there, extracts the two round-4 programs from their progress note, and checks that historical outputs were preserved. It records each exit code and its output hashes. The fresh run included in this package is `results/prior-replay/`. Its exact rational comparisons establish the signs stated in the older arguments, subject to the supplied analytical reductions and checker correctness. Their decimal renderings are explanatory.

## Small records and integrity

`results/source-record.json` identifies the repository inputs and the primary PDF versions inspected. `results/package-record.json` retains the original byte sizes and SHA-256 hashes under `files`, and the original verification under its recorded date. Its `current_files` inventory records the files after the 14 September navigation repairs, excluding the record itself. These hashes identify the recorded bytes, not mathematical correctness or bit-for-bit numerical portability across libraries. The new model JSON is a small diagnostic record; no matrix archive is needed to run any check.

No data consumer depends on an external file in this pass. The primary PDFs were temporary source-reading material and are cited by URL, version/page, and hash; they are not third-party material committed to the repository.

## Large-file policy and future calculations

Follow the repository-root `LARGE_FILES.md`: keep sources and small records in git; keep large derived matrices, sweeps, caches and bundles outside it. No such large numerical files were generated here. The current source and record files are all far below 1 MB.

For a continuation that generates large data, use this archive root:

```bash
export SUSY_POSITIVITY_ARCHIVES=/Users/Shared/szp-archive/susy-positivity/numerics-archives
```

Mirror a package-relative path such as `candidate-bulk-theories/output/<run>/...` under that root. Add an `ARCHIVES.md` and ignore rule **with the first data file**, record regeneration parameters plus stored-file and canonical-content hashes, and make a consumer look first in its normal local location and then under `SUSY_POSITIVITY_ARCHIVES`, failing closed on missing or mismatched data. Do not hard-code the maintainer's archive path into a loader. This is the policy for future large output, not a claim that an archive dataset already exists for these small diagnostics.
