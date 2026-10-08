# Arithmetic reduction centered at the carrier

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model analysis and cross-review are internal checks, not
independent specialist refereeing.

This investigation implements the parallel arithmetic program recommended
in the [prioritized assessment](../PRIORITIZED_ASSESSMENT_20261004.md).
Its object is the original complex prepared scalar \(\lambda_t(X)\): a
carrier-centered, signed Möbius–von Mangoldt correlation that keeps the
continuum, prime powers, strict cutoffs, and the entire spectral tail.

The [opening reduction](INITIAL_REDUCTION_20261004.md) derives that
correlation, treats its removable pole uniformly, and proves a spectral
tail bound with explicit logarithmic height dependence. It also extends
exact density cancellation to this family, with remainder below
\(2^{-32}r\) at the existing detector cutoff. Combined with the saved
Vaughan comparison, this gives a precise conditional arithmetic interface.
The spectral constant has not been numerically evaluated, and the central
signed correlation has not been bounded at the detector threshold.
No new arithmetic saving or zero-free box is proved.

The [review](../../../reviews/height_adapted_zero_detection/arithmetic_centered_at_carrier/INITIAL_REVIEW_20261004.md)
assesses the source recommendation and records the opening proof checks.
The [numerical guide](../../../numerics/height_adapted_zero_detection/arithmetic_centered_at_carrier/README.md)
describes small exact algebra checks and floating phase diagnostics.
These do not certify an asymptotic estimate or any zeta zero.

## What this program adds

The [height-uniform Vaughan reduction](../gaussian_localization/HEIGHT_UNIFORM_VAUGHAN_REDUCTION_20261004.md)
already proves the physical comparison. This program supplies its centered
cofactor spectrum and density-cancellation budget. It retains full
\(\Lambda\), whereas the earlier
[finite cross-spectrum](../../programs/01_signed_arithmetic_covariance/FINITE_CROSS_SPECTRUM_20261004.md)
uses primes. It also retains the full divisor range.

The neighboring
[finite Gaussian Möbius reduction](../gaussian_localization/FINITE_GAUSSIAN_MOBIUS_REDUCTION_20261004.md)
already provides a different arithmetic criterion with relative frequency
band \([-3,3]\). That route is a useful comparison. The present route
allows the original scalar to be studied across a continuous physical
scale interval; no advantage for its central arithmetic estimate has yet
been demonstrated.

## Next work and decision criteria

1. Evaluate a usable spectral constant from the fixed amplitude kernels,
   then select the smallest frequency cap whose entire tail fits the
   detector budget. Include the neighborhood of \(\nu=-t\), even when
   it is outside the retained band.
2. Decompose the exact central correlation into dyadic factor blocks,
   retaining the density transform and partial terminal blocks. Try one
   complete signed estimate with a stated carrier range. Absolute
   mean-square estimates alone are not the required saving.
3. Compare that factor range and frequency cap against the direct Gaussian
   target. Continue this route if it creates a tractable arithmetic
   estimate or a better detector interface; centering by itself is not
   evidence of either.
4. Only after a candidate estimate survives coherent-mode controls,
   establish its uniformity over the continuous carrier and prime-scale
   intervals and compare the resulting exclusion with classical inputs.

Save continuation notes here, numerical sources and small records in the
linked numerics directory, and reviews in the linked reviews directory.
Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md). No manuscript
snapshot is created. Future notable commits or tags belong in the
prime-variance project's existing DRAFT_HISTOR.md; no commit was made
for this opening investigation.
