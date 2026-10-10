# Exact finite scout checks

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Internal LLM checks are not
independent mathematical validation.

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/09_prime_phase_torus/numerics/check_prime_torus_scout.py
```

The checker uses only the Python standard library, with exact `Fraction`
coefficients in sparse formal polynomials. It writes
[prime_torus_scout_record_20261010.json](prime_torus_scout_record_20261010.json) with its own source SHA-256,
assertion count, and check families. The retained run passed 510
assertions. A fresh repeat reproduced the record byte for byte.

Drift-containing orbit curvature, finite heat residual, complete block cross correlation, monomial factorization through 256, and raw jets through order four.

No huge-height heat evaluation, actual-phase sign estimate, time-remainder bound, or density-to-collision transfer is certified. An unrestricted torus bound remains ruled out by the prior complete twist construction.
Assertion counts and source hashes establish reproducible finite algebra,
not independent mathematical evidence for the missing research theorem.
The analytic domain and interchange arguments are in
[Note 1](../notes/1_ACTUAL_ORBIT_JETS_AND_EXACT_FINITE_HEAT_RESIDUAL_20261010.md). A failed assertion exits without reporting
success; no floating root searches or uncertified numerical signs are used.

All retained files are small. No external archive is needed for these
checks; follow [LARGE_FILES.md](../../../../../LARGE_FILES.md) if future
experiments generate large derived data.

## Centered continuation

Run the additional checker from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/09_prime_phase_torus/numerics/check_centered_prime_collision.py
```

The retained [source-bound record](centered_prime_collision_record_20261010.json)
reports **11,061 exact assertions**. A fresh repeat reproduced the record
byte for byte. The checks cover independent affine-centered raw Bell rows,
candidate elimination after multiplication by `c`, full drift/curvature
residual polynomials, the centered threshold coefficient, measured
quadratic perturbation payments, and ratio/product pair regrouping.

Complete ordered-pair and block/core partitions are replayed through
`N=24`. Their rational unit-complex prime monomials and formal additive
prime logs verify identities; they are not evaluations of the actual
coupled large-height orbit. Rational checks of the exponent ledger confirm
the exact reserves used in the analytic argument. They do not verify a
uniform signed arithmetic theorem or the imported exponential-sum theorem.

The [continuation note](../notes/2_CENTERED_COLLISION_JETS_AND_RATIO_PRODUCT_CORRELATIONS_20261010.md)
provides the domain, common-height, fixed-cutoff, normalizer, and payment
arguments. The new checker is standard-library-only and produces a small
deterministic record. It establishes no sign certificate for its remaining
threshold criterion.

## Paid dual kernels and actual-height rank

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/09_prime_phase_torus/numerics/check_paid_dual_kernels.py
```

The [source-bound record](paid_dual_kernel_record_20261010.json) retains
**495 exact assertions** for the null quadratic identity, both candidate
tolerance payments, sine/cosine signs, ratio/product regrouping, normalized
threshold scaling, Schur projection, both-sign relaxed moment witnesses,
and the actual-frequency three-term control.

The checker also uses outward 60-digit Decimal intervals to certify a
five-node feature determinant at the genuine state `N=22066`,
`t=1/(2 log N)`, `x=4 pi N^2`. It is positive between `155000000`
and `156000000`, with width below `1e-30`. Strict positivity of all actual
weights then proves that the complete five-feature Gram and residual
Schur complement are positive definite. The center is not asserted to
be a candidate.

The interval arithmetic is imported from Program 13's unchanged
[check_block_current.py](../../13_microlocal_phase_space/numerics/check_block_current.py).
Its source hash is checked before import; a changed source fails closed
until reviewed and rebound. No library installation or full-cutoff phase
dataset is needed. Integer powers are locally overridden by exact rational
endpoint powers followed by directed Decimal division; the imported file
is unchanged. The [Note 3](../notes/3_PAID_DUAL_KERNELS_AND_ACTUAL_FREQUENCY_RELAXATION_LOSS_20261010.md)
and [Review 3](../reviews/3_PAID_DUAL_KERNEL_INTERNAL_REVIEW_20261010.md)
explain what the genuine rank witness, formal controls, and Hilbert-space
relaxation establish. A fresh replay reproduced the small record byte
for byte. No negative threshold bound or genuine collision is certified.

## Prescribed heat-weight covariance

Run the continuation checker from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/09_prime_phase_torus/numerics/check_prescribed_heat_covariance.py
```

Its [source-bound record](prescribed_heat_covariance_record_20261010.json)
retains **327 exact assertions**. Gaussian moments, the centered prescribed
quadratic weight and its multiplicative cross term, all four covariance
kernel signs, the complete block/core recombination, and the shifted
signed-moment hierarchy are checked through exact formal degree 12 in
`sqrt(t/2)`. The finite models retain one common rational phase generator
and the prescribed quadratic heat coefficient shape. They are algebraic
controls, not actual huge-height arithmetic evaluations.

For an independent replay without replacing the retained record, add
`--output /tmp/prescribed_heat_covariance_replay.json`. The fresh replay
matches the default small record byte for byte. No external dependency,
library install, or full phase dataset is needed.

[Note 4](../notes/4_PRESCRIBED_HEAT_WEIGHT_COVARIANCE_AND_SIGNED_HIERARCHY_20261010.md)
proves the exact Gaussian decomposition, infinite signed hierarchy,
finite tail payment, and uniform asymptotic order of the explicitly
positive covariance envelope. The envelope's lower bound is independent
of phases; it does not give a lower bound for the signed covariance.
[Review 4](../reviews/4_PRESCRIBED_HEAT_COVARIANCE_INTERNAL_REVIEW_20261010.md)
records that distinction. No negative threshold sign is certified.

## Sharp one-sided dual payment

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/09_prime_phase_torus/numerics/check_curved_one_sided_dual_payment.py
```

The [record](curved_one_sided_dual_payment_record_20261010.json) retains
**10,081 exact assertions** and 233 critical root intervals evaluated.
The checker solves the finite quadratic payment on `s^2+|v|<=1` using
exact square-free cubic isolation and rational interval evaluation.
Known sharp diagonal, linear and cross cases, singular ridges, constant
edges, and interior stationary points are tested. Twelve physical-drift
coordinate controls compare the sharp one-sided payment with the old
absolute square. Eight common higher-moment corners and 32 common
transformed-coefficient corners give exact payments for their declared
independent boxes. All four sine/cosine dual channels remain present.

Use `--output /tmp/curved_one_sided_dual_payment_replay.json` for a fresh
replay without replacing the retained record; that output matches byte
for byte. The source uses only standard-library Fraction arithmetic.
The rational controls verify payment geometry and algebra, not actual
large-height arithmetic candidates or a negative threshold margin.

[Note 5](../notes/5_SHARP_ONE_SIDED_DUAL_PAYMENTS_ON_CORRELATED_CANDIDATES_20261010.md)
proves the general finite critical-set formula and one-sided certificate.
[Review 5](../reviews/5_CURVED_ONE_SIDED_DUAL_PAYMENT_INTERNAL_REVIEW_20261010.md)
records degeneracy, root-counting and sharpness scope. The prescribed
four-channel signed upper bound remains the missing research input.
