# Gaussian localization checks and diagnostics

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

These sources and small records support the
[opening investigation](../../../notes/height_adapted_zero_detection/gaussian_localization/INITIAL_INVESTIGATION_20261004.md)
and the
[explicit-constants continuation](../../../notes/height_adapted_zero_detection/gaussian_localization/EXPLICIT_CONSTANTS_AND_FINITE_WINDOW_20261004.md),
[finite Gaussian Möbius reduction](../../../notes/height_adapted_zero_detection/gaussian_localization/FINITE_GAUSSIAN_MOBIUS_REDUCTION_20261004.md), and
[height-uniform Vaughan comparison](../../../notes/height_adapted_zero_detection/gaussian_localization/HEIGHT_UNIFORM_VAUGHAN_REDUCTION_20261004.md).
They verify parameter arithmetic and formal examples. They contain no actual
zeta zeros and do not certify the required arithmetic cancellation estimate.

The original four sources and the new Poisson-refinement checker use the
Python standard library only. Run from this directory:

```sh
python3 check_gaussian_preflight.py
python3 check_explicit_gaussian_constants.py
python3 check_gaussian_arithmetic_reduction.py
python3 check_height_uniform_vaughan.py
python3 check_poisson_refinement.py
```

## Initial diagnostics

`check_gaussian_preflight.py` writes
`gaussian_preflight_record_20261004.json`. It checks exact rational gaps
319/256 and 63/16, the linked-parameter power identity, and a formal
positive-multiplicity pair that cancels at one Gaussian sample. It also
checks floating logarithmic error ratios for 1 through 4096 in the sample
allowance N. The largest sampled ratio is approximately 0.001018618 at N=1.
Those floating results are diagnostics, not outward certificates.

## Exact arithmetic behind the effective constants

`check_explicit_gaussian_constants.py` writes
`explicit_gaussian_constants_record_20261004.json`. It uses exact rational
arithmetic, positive-series remainder bounds, alternating-series bounds,
and outward rounding. No floating number decides a sign or a ceiling.

The source checks probe moments and derivative norms, amplitude constants,
positive endpoint-polynomial coefficients for the inverse pole, Gaussian
core and tail inequalities, inverse-norm moment majorants, and finite-budget
base inequalities. It encloses the Bellotti--Wong v2 guard-count expression
at four illustrative carrier heights. In particular the enclosure
[40.507495483735023800,40.507495483735023801] at height 3e12 gives N=41
and log-prime-scale cover [1008,8528]. These are consequences of a published
count theorem, not computations of the actual cluster of zeta zeros.

The note proves the all-height inequalities analytically. The source checks
their arithmetic ingredients and examples; it is not a formal verification
of the analysis. Each record carries its source SHA-256 for replay
identification. A hash does not establish a mathematical inequality.

## Exact arithmetic reduction checks

`check_gaussian_arithmetic_reduction.py` writes
`gaussian_arithmetic_reduction_record_20261004.json`. It checks 4,096
formal prime-log coefficient identities and 48 component checks with
synthetic complex rational weights and real cutoffs. Strict d>D, weak
dr<=B, full terminal caps, and prime powers are preserved. It verifies
Gaussian fourth-moment arithmetic, the exact product-tail polynomial,
and outward error-budget ratios. Its elementary-function dependency is
the adjacent `check_explicit_gaussian_constants.py`, whose expected
SHA-256 is checked before import. A changed dependency requires an audit.

`check_height_uniform_vaughan.py` writes
`height_uniform_vaughan_record_20261004.json`. Its 34 rational checks
cover the probe norm, polynomial derivative majorants, ninth derivative
endpoint atoms, normalized carrier coefficients, Euler-polynomial sums,
measure conversion, seventh derivative and Poisson constants, and the
cutoff's final error allowance.

Both new records carry their source SHA-256. No floating-point comparison
decides these checks. Finite formal examples and exact constant arithmetic
support the analytic proofs; they do not evaluate the proposed enormous
signed sums or prove the remaining cancellation inequalities. The
[internal review](../../../reviews/height_adapted_zero_detection/gaussian_localization/ARITHMETIC_REDUCTION_REVIEW_20261004.md)
records these limits.

## Poisson refinement and conditional signed criteria

`check_poisson_refinement.py` writes
`poisson_refinement_record_20261004.json`. It is standalone: the recorded
old-source hashes identify provenance and are not imported dependencies.
It checks exact formal prime-log identities, complex rational cap
identities, the full geometric mode sum, fractional Gaussian exponents,
ray-rotation constants, and all-sample budget arithmetic. It also checks
amplitude-derivative constants and the two conditional signed criteria,
including the corrected exponential base certificate and secondary
cutoff budgets, with synthetic partial-summation controls.

Read the [Poisson refinement](../../../notes/height_adapted_zero_detection/gaussian_localization/POISSON_SMALL_DIVISOR_REFINEMENT_20261004.md),
[basic signed attempt](../../../notes/height_adapted_zero_detection/gaussian_localization/SIGNED_DYADIC_ATTEMPT_20261004.md), and
[cofactor-aware criterion](../../../notes/height_adapted_zero_detection/gaussian_localization/COFACTOR_AWARE_SIGNED_CRITERION_20261004.md)
for the analytic arguments. The new deletion theorem has no Möbius
cancellation hypothesis. The signed criteria have an unproved finite
arithmetic hypothesis. This checker verifies their algebra and elementary
budget seeds; it does not formally verify contour rotation or Poisson
summation, evaluate the giant signed sums, or establish a zero-free box.
The [internal review](../../../reviews/height_adapted_zero_detection/gaussian_localization/POISSON_AND_SIGNED_REVIEW_20261004.md)
records the analytical checks and their limits.

No large arrays, third-party PDFs, inverse-kernel quadrature data, or zero
caches are stored. Follow the repository large-file policy if future
computations generate such data.
