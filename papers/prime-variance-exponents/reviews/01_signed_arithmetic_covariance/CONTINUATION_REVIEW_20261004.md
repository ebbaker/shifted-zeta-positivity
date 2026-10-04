# Internal review: scalar detection, arithmetic overlap and cutoff transport

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not inferred. Coordinating proof checks
and separate same-model agent cross-reviews; not independent specialist
refereeing. No global fixed power saving or priority claim.

## Scope and result

Reviewed the [continuation summary](../../notes/programs/01_signed_arithmetic_covariance/SIGNED_COVARIANCE_CONTINUATION_20261004.md),
[scalar detector](../../notes/programs/01_signed_arithmetic_covariance/SCALAR_DETECTOR_20261004.md),
[arithmetic overlap](../../notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_OVERLAP_20261004.md),
[cutoff transport](../../notes/programs/01_signed_arithmetic_covariance/CUTOFF_TRANSPORT_20261004.md),
the new numerical sources and retained small sector record. Rechecked
relevant fixed-probe, Vaughan, Mellin and one-sided Landau interfaces in
the existing notes. The inherited manuscript equivalence and the complete
Landau lemma were used, not independently reproved from scratch.

No unresolved mathematical defect was found in the new deductions. The
most consequential change is that the earlier two-piece orthogonal split
does not create two independent global arithmetic obligations: the scalar
alone detects all forbidden zeros. Both pieces remain necessary in a
shell-local energy identity. Updated navigation explicitly distinguishes
these statements and preserves the earlier derivations.

## Scalar detector checks

- Verified q=7/3, S=X lambda_V, averaged support [A,2B], the formula
  ell(u)=u² int_(u/2)^u w(t)t^−3dt, and its zero ordinary moment and
  preserved logarithmic continuum c_w.
- Verified the Mellin multiplier D(z)=G(1/2−z)(2^(z+2)−1)/(q(z+2)).
  Its extra factor has zeros only on Re z=−2, with z=−2 removable.
  D(1)=0 cancels the zeta pole; D'(1)=c_w. At a forbidden zero the
  residue is −m_rho D(rho), which remains nonzero for any multiplicity.
- Checked the full lower support X=A and the exact n=2 compact initial
  cap for a one-sided logarithmic transform. This cap is entire; it was
  not silently omitted.
- Checked holomorphy under subpower scalar envelopes, closed-boundary
  intersection and the inherited variance converse, including kappa=1.
  No convergence on the boundary line or rightmost-zero assumption enters.
- Checked the one-sided Landau proof: the hypothetical envelope produces
  a nonnegative tail; its finite convergence abscissa cannot lie above
  b because the continued transform has no positive-real singularity
  there. Absolute transform convergence then follows. No sign bound is
  inferred merely from analyticity near the real axis.
- Checked the O(X^−1/2) centered-Vaughan scalar transfer, all-real-X
  quantifiers, and the x sin(x²) counterexample to a generic norm claim.

The cutoff-transport agent independently reviewed this proof and found no
correction needed. It establishes an equivalent criterion, not its premise.

## Arithmetic overlap checks

Checked the inner higher-prime-power reciprocal tail and resulting
O(X^(61/24)log²X) energy. This estimate is for the actual convolution
sector and is sufficient for kappa<11/24; its logarithm is retained at
the endpoint. Projection and scalar errors follow by contractivity and
Cauchy–Schwarz, not by deleting a covariance entry.

Checked the cap N/U<U² and the exact identity
A_U(qg)=−sum_(d|g)mu(d)=−1_(g=1) for q>U, g<U. The ordered semiprime
coefficients are −log(pq) for distinct primes and −log p for squares.
The smooth residual retains all remaining signs, multiplicities and
strict cutoffs. Distinct-prime exact collisions, repeated-prime channels
and near-product bounds were checked with the projected kernel present.
Affordable sectors of a signed quadratic form are not claimed to be
independently removable response vectors.

The classical quantitative PNT source was checked directly in
[Tao's Notes 2, Corollary 39 and Exercise 40](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/).
The two successive prime-measure replacements retain their strict lower
endpoints. The second weight is (x/q)int_(Uq/x)^infinity w, which vanishes
for q<=Ax/U by preparation. Its magnitude and derivative yield the stated
uniform logarithmic-quality error, with no power PNT assumption.

Re-derived the continuous semiprime integral, leading sign, second term,
and projection. The positive raw energy constant is q_0 c_w²/(13/24)²;
the projected one is c_w² sigma_a²/(13/24)^4, with sigma_a²>0. Thus even
separate projected-sector power bounds really fail for these arithmetic
coefficients. The all-logarithmic-order smooth/semiprime anticorrelation
follows from the inherited PNT baseline and the new power-small discarded
sectors. It is not a newly proved fixed power saving.

The scalar-detector agent independently checked the arithmetic and the
primary PNT input, including the anticorrelation conclusion. Finite
opposite semiprime signs in the pilot are consistent with a delayed
asymptotic range and are not used as proof of that asymptotic.

## Cutoff and frequency checks

Checked both signed cutoff-annulus formulas and the mixed rectangle by
direct convolution. The U transport cancels its raw linear term against
the continuum. The V transport retains its prime-response annulus until
V<AX is imposed. The simultaneous transport uses two disjoint strips,
with no duplicated corner. All real and integer cutoff endpoints retain
the correct strict/weak inequalities.

Verified the norm region u+v<=1−kappa/12 for fixed u,v>0, the bounded-V
logarithmic qualification, balanced exponent 1/2−kappa/24, and scalar
transport error O(X^−kappa/2). Checked convex averaging's variance identity
and its E² upper bound; no independence between nearby cutoffs is assumed.
The empty Type II anchor lies outside the affordable cutoff range.

Verified target-dependent cofactor, upper and lower Mellin cutoffs with
their exact logarithmic factors. The coefficient estimate is uniform in
the divisor threshold. The low-frequency bound uses oddness of g at the
bounded relative phase log(x/n), not an unbounded log n. Every fixed
nonzero frequency eventually remains, so no forbidden-zero frequency is
discarded permanently. Bare-power errors are correctly distinguished
from exact endpoint errors.

## Executed checks and limitations

The coordinating agent ran
[check_cutoff_transport.py](../../numerics/01_signed_arithmetic_covariance/check_cutoff_transport.py):
57,600 exact integer prime-log coefficient-vector comparisons and 50
rational continuum checks passed. Cases include noninteger cutoffs,
prime powers and nonvanishing prime-response cutoff annuli.

The [sector pilot](../../numerics/01_signed_arithmetic_covariance/centered_sector_pilot.py)
checks the large-prime classification in integer arithmetic, assembles
unordered semiprime coefficients independently, and retains smooth,
prime-power and continuum contributions. Four runs at two noninteger
shells and 128/256 nodes gave zero observed coefficient-decomposition
residual, an energy-split residual/X² below 3.23e-16, and listed normalized
energy refinement changes below 3.51e-8. The arithmetic-overlap agent
independently reviewed the implementation, including the square correction.

These are floating diagnostics and exact finite algebra checks. No
outward numerical enclosure, new zero computation, fitted exponent or
uniform finite-X error certificate is claimed. The sampled semiprime
scalar signs do not yet agree with the eventual leading asymptotic;
this effective-scale limitation is explicit in the source package.

No manuscript or compilation record changed. No third-party paper, sieve
array or Gram matrix was stored. Source hashes in the small diagnostic
record identify the run's inputs, not mathematical truth. The first
fixed-saving one-sided scalar bound remains open.

Final artifact checks passed: local Markdown links resolve, math delimiters
are balanced, numerical source hashes match the retained record, both new
Python sources compile, and `git diff --check` is clean. All changed/new
files, including the preceding preliminary work, remain below 1 MiB.
Changes are saved in the working tree; no commit or publication was made.
