# Quarter-step research packet

Start with [the mathematical analysis](quarter_step_analysis.md). It separates two results in the working Weil-depth v0.3 normalization:

- A full-operator central certificate at depth 1.98, covering the first quarter of the extension from log 7 to log 8, and its small-positive-shift contraction consequence.
- A central residual estimate allowing all new-slab inputs while retaining 128 old polynomial modes. The residual penalty is at most 0.004 times the proposed continuation energy.

Normalization verification remains separate. This packet does not prove an all-depth recursion.

## Reproduction

Use Python 3.10 with the versions in [requirements.txt](requirements.txt). The recorded environment used FLINT 3.6.0 through python-flint 0.9.0. Keep this directory beside the preceding three research packets; its imports reuse their mathematical routines and the unchanged v0.3 certificate source.

Run from this directory, with assertions enabled:

```sh
python central_residual.py --output residual_128_32.json
python central_residual.py --degree 340 --log-degree 90 --bits 6656 --output residual_128_32_replay.json
python central_residual.py --old 32 --new 8 --output residual_32_8.json
python reference_check.py --output reference_256.json
python path_corollary.py
python cross_checks.py
```

The reference check rebuilds its full matrices before validation and takes several minutes in the recorded environment. The main residual runs take roughly two minutes each. Timings depend on hardware.

## Records

| File | Purpose |
|---|---|
| `residual_128_32.json` | Full new-output Gram, analytic error budget, three sign checks, exact rational continuation coefficients |
| `residual_128_32_replay.json` | Increased profile/logarithm degree and precision, same certified inequalities |
| `residual_32_8.json` | Smaller retained old/continuation spaces, residual factor 0.006 |
| `reference_256.json` | Full-operator reference validation at 99/50, requested floor 1e-31, both parity checks |
| `path_corollary.json` | Interval-checked constants for the shift interval and relative coupling consequences |
| `cross_checks.json` | Independent numerical kernel and quadrature checks on a smaller example; not a positivity certificate |
| `verification_manifest.json` | Final audit of saved result status, recorded source hashes, and dependency hashes |

Source hashes in the result files identify the code used for those runs. Some helper modules import further modules without using their functions in a given calculation; the final manifest also records those local dependencies. The reference result retains validation bounds and pivots, not a standalone saved copy of the raw matrices.

The original manuscript source is the pinned repository commit `a566944dc1be2899e37fce3d0e857516ced33d8f`. The wrapper calls the unchanged copy at `../critical-path-20260910/reference_certify_arb.py`. No synced project source or manuscript was edited.
