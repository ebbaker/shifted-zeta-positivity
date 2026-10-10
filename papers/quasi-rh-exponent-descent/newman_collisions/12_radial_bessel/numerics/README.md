# Numerical and algebraic replay

10 October 2026. Model: GPT-6 (Codex); exact serving variant and configured reasoning effort unavailable and not inferred. Checks are internal, not independent mathematical review.

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/numerics/check_radial.py
```

The script requires only Python 3 and the standard library. It prints a small JSON record; [the run record](SCOUT_CHECK_RECORD_20261010.json) was produced on 10 October 2026 with Python 3.10.0. Status: **PASS**.

Integer polynomial recurrences, rational sign bounds, exponential constants and infinite geometric tail bounds were checked exactly with Fraction and rational Taylor enclosures. The first 18 positive tail terms and sampled theta values are separate floating-point diagnostics; global radius coverage follows from the analytic bounds in the note. The exploratory central value is not an interval certificate.

For the continuation run:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/numerics/check_radial_center_obstructions.py
```

[The continuation record](CENTER_OBSTRUCTIONS_CHECK_RECORD_20261010.json) has status **PASS** and its source SHA-256 digest. This checker uses outward Decimal arithmetic, rational Machin bounds, Taylor/geometric exponential enclosures and the infinite theta tail. It encloses the squared-radius log-convexity determinant below zero and the dimension-11 inverse at the center below zero uniformly on 0<=t<=0.05. Sparse exact Fraction polynomial algebra checks the sine collision dictionary and full deflation through multiplicity six.

The source notes supply the analytic arguments. Floating-point diagnostics in the initial replay remain exploratory; they are separate from the continuation's outward center certificates. Internal checks are not independent mathematical validation. No large generated data are stored. Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md) if later computations need an archive.
