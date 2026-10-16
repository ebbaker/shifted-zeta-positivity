# Finite support for the complete block-covariance investigation

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not inferred. Internal numerical
diagnostics only; no new outward certificate or global exponent.

## Chosen deliverable

Support [program 01's complete Gram split](../01_signed_arithmetic_covariance/PRELIMINARY_INVESTIGATION_20261004.md)
with a reproducible, small calculation that preserves divisor cutoffs,
prime powers, terminal blocks, projected cross terms and the Vaughan
continuum. This is a new bounded diagnostic, rather than another finite
variance-range claim. The previous outward finite-range packages are not
recomputed or upgraded by this work.

## What was actually computed

The [script](../../../numerics/10_finite_certificates_support/block_gram_preflight.py)
imports the existing fixed probe and sieve, then independently assembles
complete dyadic cofactor coefficients and m-blocked Vaughan coefficients.
On the noninteger shells X=1000.25 and 10000.5, it uses 128 and 256
Gauss–Legendre nodes. Parameters are D=floor(X^(9/10)) and
U=V=floor(X^(11/24)); these integer cutoffs implement the strict real
cutoff conditions exactly. The final cofactor blocks are partial.

It checks the original divisor identity against independently sieved
Lambda, the prime-place decomposition at p=2,3, and the matrix identity
G=G-perp+||x||² lambda lambda-transpose. The energy record separates
the projected shape and the complete continuum mismatch. It retains
only small summaries; sieve and Gram arrays are not saved.

The [record](../../../numerics/10_finite_certificates_support/block_gram_record_20261004.json)
includes source hashes, Python/NumPy versions, all parameters, signed
off-diagonal sums, trace summaries and error diagnostics.

| Check | Observed result |
| --- | ---: |
| Maximum original divisor coefficient error | 7.11e-15 |
| Maximum normalized whole-energy split error | 2.29e-14 |
| Maximum 128→256 change among whole/shape/scalar/trace/off-diagonal energies divided by X² | 4.80e-7 |
| Real shells | 2 |
| Quadrature runs | 4 |

These are observed floating residuals, not interval-enclosed errors. Node
refinement is not a proof of quadrature accuracy or continuous-X control.

## New practical finding

At the pure-power cofactor cutoff, the discarded low-divisor energy/X² is
30.66 and 127.40 on the two shells. The proved O(X^(9/5)log²X) bound
is asymptotic with large fixed constants; it need not be small at these
scales. Therefore finite plots of this retained response cannot safely
be read as plots of prime variance. Report the exact remainder alongside
every retained energy. The older pilot's smaller cutoff prefactor is a
useful effective-scale choice, not a contradiction of this observation.

The Vaughan diagnostics keep the continuum cancellation explicit and
are easier to interpret here. Neither the choice of scale nor that
observation predicts asymptotic superiority.

## Next support gate

Once program 01 names an arithmetic cross-term inequality, adapt this
small harness to that inequality and exhibit its signed head, cutoff
annulus and scalar mismatch separately. A counterexample to the proposed
finite inequality is useful. Passing samples are only diagnostic.

Only promote a run to a certificate after replacing the relevant
arithmetic/quadrature calculations by outward enclosures and proving
all unsampled tails and continuous-parameter coverage. No current
global task calls for a larger zero table or a larger variance sweep.

This program is necessary support, not an independent candidate for a
first global exponent. A fixed finite prefix cannot settle the all-height
statement in the [overview](../../PROJECT_OVERVIEW_20261004.md).
