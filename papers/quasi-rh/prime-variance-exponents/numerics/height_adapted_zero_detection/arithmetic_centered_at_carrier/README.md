# Checks for the carrier centered arithmetic reduction

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.

Run `python3 check_centered_reduction.py` from this directory. The script
uses the Python standard library and writes the small adjacent
`centered_reduction_record_20261004.json`. For an external staging copy,
pass `--source-root` with the prime-variance project directory to record
the source hashes from that checkout.

The checker tests full-\(\Lambda\) Vaughan convolution with formal
prime-log coefficients, the high-divisor/cofactor grouping with strict
cutoffs and terminal products, and exact density cancellation with
complex rational polynomial kernels. It also verifies rational
constants in the new effective density budget. Floating diagnostics
test the carrier phase in the centered spectral integrand and the
continuous value of the density transform at its shifted origin.

Negative controls drop prime powers, change a strict lower cutoff,
omit the carrier prefactor, and conjugate the second spectral factor.
Each control must change a diagnostic result. Passing examples verify
these finite identities, not an arithmetic saving.

The synthetic kernels are supported on \([1,2]\) and are derivatives
of compact polynomials. They test density algebra and endpoint
conventions; they do not have the actual prepared probe's regularity
or variation constants. Formal prime-log coefficient vectors avoid
floating equality decisions in the arithmetic identities. All
floating checks are labeled separately in the record.

Read the [opening reduction](../../../notes/height_adapted_zero_detection/arithmetic_centered_at_carrier/INITIAL_REDUCTION_20261004.md)
and [internal review](../../../reviews/height_adapted_zero_detection/arithmetic_centered_at_carrier/INITIAL_REVIEW_20261004.md)
for the analytic proof and scope. No Fourier quadrature, outward zero
certificate, actual-prime sweep, or asymptotic central estimate is
performed. Source hashes identify the files read; they do not prove
their claims. Keep larger regenerable output outside Git under the
repository's large-file policy.
