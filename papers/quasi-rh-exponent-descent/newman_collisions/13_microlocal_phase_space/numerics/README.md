# Numerical and algebraic replay

10 October 2026. Model: GPT-6 (Codex); exact serving variant and configured reasoning effort unavailable and not inferred. Checks are internal, not independent mathematical review.

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_phase_space.py
```

The script requires only Python 3 and the standard library. It prints a small JSON record; [the run record](SCOUT_CHECK_RECORD_20261010.json) was produced on 10 October 2026 with Python 3.10.0. Status: **PASS**.

The four Gaussian jet polynomials were verified exactly over rational numbers. A Gaussian wave amplitude checks the full Husimi generator by finite differences; a finite complex block checks doubled value, derivative and positive-matrix observed squares. Those finite floating-point controls are not a genuine arithmetic sign certificate.

The source note supplies the analytic arguments. Floating-point checks are not rigorous numerical enclosures and are not independent mathematical validation. No large generated data are stored. Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md) if later computations need an archive.

## Genuine block-current continuation

Run the bounded interval checker from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_block_current.py
```

The default parameters are `M=N=22066`, `kappa=1`, and 60-digit Decimal
arithmetic. All 11033 terms in the actual relative block are enclosed with
outward rounding, Taylor/alternating-series trigonometric bounds and full
physical derivative drift. Unlike the initial replay above, this calculation
is an outward interval sign enclosure. It uses only Python 3's standard
library and takes a few seconds in the recorded environment.

[The certificate](BLOCK_CURRENT_CERTIFICATE_20261010.json) encloses
`J_B/w_N^2` strictly between `-181.169106` and `-181.169105`; its status is
**PASS**. [The build record](BLOCK_CURRENT_BUILD_RECORD_20261010.json) identifies
the exact source/certificate by SHA-256. Replaying computes the sign afresh;
hashes alone do not decide it.

This is a genuine finite-block current certificate, not a complete-sum sign,
candidate collision, threshold exclusion, or RH result. The checker asserts
a negative current at its default height; another `--M` is a separate
experiment and may fail that particular assertion. See Note 2 and Review 2
for the complete recombination and candidate-current tolerance.

## Complete current and genuine simple-zero rectangle

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_complete_current_rectangle.py
```

The new checker uses the exact `M=N=22066` center and all 22066 genuine
terms. It imports the preserved Note 2 arithmetic source after checking its
retained SHA-256, and evaluates integer powers locally by repeated outward
multiplication. A changed dependency fails closed before import.

The [complete certificate](COMPLETE_CURRENT_RECTANGLE_CERTIFICATE_20261010.json)
reports the block, complement and full current, the cross current, and
both difference-phase and reflected sum-phase energy interference.
It then certifies a positive-area rectangle with time increments
`0 <= t - t0 <= 8e-6` and height offsets `0.3 <= x - x0 <= 0.4`.
All spatial normalizer/drift corrections, physical fixed-height time
derivatives, coherent midpoint jets, sixth-moment remainders, and full
holomorphic value/derivative payments are retained.

Status: **PASS**. The paid endpoint values have opposite signs and the paid
normalized derivative `Q_t'` exceeds `10.20` throughout the rectangle. Therefore every time
in that interval has one unique simple genuine `H_t` zero in the specified
height interval; `H_t` and `H_t'` are jointly nonvanishing on the entire
rectangle. The uniform paid full-current reverse candidate inequality
also passes. This is a finite rectangle theorem, not sectorwide current
positivity, threshold exclusion, or an RH result.

The [build record](COMPLETE_CURRENT_RECTANGLE_BUILD_RECORD_20261010.json)
binds the new source, its preserved imported source and the certificate.
The replay decides each sign by arithmetic; hashes identify files. No
large data or nonstandard Python dependencies are required.
