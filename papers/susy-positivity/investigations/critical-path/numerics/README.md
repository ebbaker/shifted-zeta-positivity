# Arithmetic EMA anchor certificate

[certify_ema_original_anchor.py](certify_ema_original_anchor.py) is a
standard-library-only, outward rational interval certificate. It proves the
finite scalar and matrix bounds used in the [anchor note](../notes/EMA_TOWER_ORIGINAL_TRANSFER_ANCHOR_20260920.md)
to establish Q(0,1/2) >= I/40 and the original cumulative defect
D(0.001,1/2) >= 0.000049998 I on every L2 input. The finite tower has 32
prescribed scales; 16 cosine head modes and an explicit infinite-complement
bound complete the proof. No output smoother is used.

- [40-digit record](records/ema-original-anchor-20260920.json).
- [60-digit replay](records/ema-original-anchor-60digits-20260920.json).
- [Separate reduction checker](check_ema_anchor_reduction.py) and its
  [record](records/ema-anchor-reduction-checks-20260920.json): 130 Fraction-based
  interval controls, rejection of an indefinite matrix, and direct-response
  quadrature agreement below 3.7e-14. NumPy is needed only for this checker.
- [Review and anchor provenance](records/ema-review-anchor-provenance-20260920.json).

From the repository root, writing fresh replay records outside the repository:

```sh
python3 papers/susy-positivity/investigations/critical-path/numerics/certify_ema_original_anchor.py --output /tmp/ema-original-anchor-replay.json
python3 papers/susy-positivity/investigations/critical-path/numerics/certify_ema_original_anchor.py --digits 60 --output /tmp/ema-original-anchor-replay-60.json
python3 papers/susy-positivity/investigations/critical-path/numerics/check_ema_anchor_reduction.py --output /tmp/ema-anchor-reduction-replay.json
```

No floating eigenvalue is used for a certificate sign decision. The programs
refuse assertion-disabled Python execution. Mathematical validity also depends
on the analytic reduction in the note; independent specialist review remains
outstanding. This is a fixed-window anchor, not an all-depth theorem or a new
known positivity horizon. Historical records below are unchanged.

## Earlier EMA controls

[check_ema_controls.py](check_ema_controls.py) is a standalone Python
standard-library diagnostic program. Its [record](records/ema-controls.json)
contains 57 passing cases from the 20 September 2026 run.

The checks cover the causal EMA energy identity, all-pass boundary storage,
fixed-rate cancellation of a growing exponential, direct convolution against
closed differential-equation solutions, complex inputs, carried memory at
an interval join, monotonicity in smoothing length, the gamma EMA sum,
an expanding toy transfer, two smoothing-removal rates, and path-EMA clock
scaling. The mathematical derivations and limitations are in the
[continuation note](../notes/EMA_SMOOTHING_AND_POSITIVITY_CONTINUATION_20260920.md).

Run from the investigation directory:

    python3 numerics/check_ema_controls.py

The program prints JSON and exits unsuccessfully if a comparison fails.
It uses binary64 adaptive quadrature, not interval enclosures. The rate
experiment uses the explicitly nonarithmetic transfer exp(omega) I.
No arithmetic operator norm, unresolved complement, interacting field
theory, or all-depth positivity statement is certified by these controls.
The 57 cases are separate from the 299 cases in Wilson–Loewner version 0.4.


## Arithmetic pilot and rigorous coarse bound, 20 September 2026

- [adaptive_ema_pilot.py](adaptive_ema_pilot.py) imports the parent Loewner
  transfer and central-form machinery. It compares full output functions on
  L=1/2 for N=24 and 40 inputs, five shifts, four boundary schedules, and three
  shift-path averages. Both local and pole contributions are retained.
  [Record](records/adaptive-ema-pilot-20260920.json): finite-input diagnostics,
  empirical refinement errors, exact-identity residuals, and analytic complement
  bound formulas evaluated in binary64. It needs Python 3 and NumPy.
- [certify_ema_coarse_bound.py](certify_ema_coarse_bound.py) uses exact rational
  arithmetic to prove a squared norm upper bound 0.987339385394 for the complete
  output-filtered transfer at omega=0.1, ell=sqrt(omega), L=1/2.
  [Certificate](records/ema-coarse-certificate-20260920.json). This is a
  deliberately contaminating schedule point, not an original-transfer or
  admissible-removal certificate. Standard library only.
- [Audit note](../notes/ADAPTIVE_EMA_AUDIT_AND_PILOT_20260920.md) gives proofs,
  assumptions, numerical comparisons and the precise missing input-complement
  estimate. [Provenance](records/adaptive-ema-audit-provenance-20260920.json)
  records model/effort, hashes, commands and preservation checks.

Run from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 python3 papers/susy-positivity/investigations/critical-path/numerics/adaptive_ema_pilot.py
python3 papers/susy-positivity/investigations/critical-path/numerics/certify_ema_coarse_bound.py
```

The pilot record is a small summary; no large matrix archive is stored. The
earlier 57-case record and Wilson–Loewner v0.4 sources/snapshots are unchanged.
