# Möbius and balanced-variance pilot

4 October 2026. Prepared with substantial LLM assistance; GPT-6 (Codex),
inherited configuration, exact serving variant and reasoning effort not exposed.
This is a floating diagnostic, not an outward certificate or a global bound.

The [script](pilot.py) evaluates the exact arithmetic decompositions proved in
the [localization note](../../notes/MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md).
It uses NumPy, sieves Möbius and von Mangoldt coefficients, and keeps all
prime powers, support endpoints, and terminal divisor cutoffs. No sieve or
large array is stored. The retained [record](record.json) is small JSON.

Run from the repository root:

```bash
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 \
  papers/prime-variance-exponents/numerics/mobius_reduction_20261004/pilot.py \
  --output /tmp/prime-variance-mobius-pilot.json
```

The defaults use six noninteger shell origins from 1000.25 to 300000.5,
128 and 256 Gauss–Legendre nodes, and
D=floor(X^(11/12)/(4(log X)^(1/6))). The cofactor count is the exact
finite ceiling floor(floor(2BX)/(D+1)), between 25 and 44 in this run.
The smaller cutoff prefactor only changes fixed constants in the proof.

The script independently computes the low-divisor and high-divisor
coefficient arrays and compares their sum with Lambda. It evaluates the
original response, low-divisor response, and every retained signed cofactor
component on the same complete shell. Their Gram trace is the sum of
component energies; their signed Gram sum is the energy of their sum.

| X | Original variance / X² | Low-divisor energy / X² | Cofactor Gram trace / X² | Signed sum / trace |
| ---: | ---: | ---: | ---: | ---: |
| 1000.25 | 2.047491499 | 0.001710190 | 134.534433 | 0.0151482 |
| 3000.5 | 0.608826046 | 0.000159086 | 221.946126 | 0.00273401 |
| 10000.25 | 3.084832696 | 0.000040496 | 281.599267 | 0.0109549 |
| 30000.5 | 2.579278624 | 0.000027346 | 448.180275 | 0.00575488 |
| 100000.25 | 2.303141730 | 0.000022219 | 463.326939 | 0.00497182 |
| 300000.5 | 2.474554345 | 0.000006822 | 678.923964 | 0.00364566 |

These are 256-node results. The total cofactor energy is much smaller than
the sum of individual energies in these samples, so its cross terms exhibit
substantial aggregate cancellation. This is the intended diagnostic. No
monotone growth claim or fitted asymptotic exponent is inferred.

The maximum change in original variance/X² between 128 and 256 nodes is
less than 2.76e-8. Across both refinements, the maximum coefficient-identity
residual is below 3.20e-14 and the maximum response-identity residual is
below 4.35e-11. These are observed floating residuals; they do not certify
quadrature errors or unsampled X values. Across all recorded normalized
energy columns, including the larger Gram traces, the maximum refinement
change is below 9.64e-7.

The balanced calculation uses U=V=floor(X^(11/24)) and retains the
logarithmic Type I continuum. It records the two nonnegative pieces

\[
\|B-\lambda_Xx\|_2^2,
\qquad \frac73X^3|\lambda_X+c_wM_1(U)|^2,
\qquad \lambda_X=\langle B,x\rangle/(7X^3/3),
\]

whose sum is the centered Type II energy. The observed normalized splitting
residual is below 5.36e-16 across both refinements. Its difference from the original variance can
still be of quadratic order; the theorem gives a norm comparison, not an
equality of leading coefficients at this cutoff. Prime powers in the inner
Vaughan coefficient are retained.

See the [independent internal code review](../../reviews/MOBIUS_PILOT_REVIEW_20261004.md)
and [localization proof review](../../reviews/ARITHMETIC_LOCALIZATION_REVIEW_20261004.md).
The global arithmetic power-saving target remains open.
