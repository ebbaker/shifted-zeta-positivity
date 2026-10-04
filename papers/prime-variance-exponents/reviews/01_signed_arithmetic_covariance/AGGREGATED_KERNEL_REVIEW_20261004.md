# Review of aggregated kernel localization and mixed discrepancy feedback

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred. This is
internal same-model analytical cross-review, not independent specialist
refereeing. No new global exponent or mathematical priority is claimed.

Reviewed materials:

- [Aggregated kernel continuation](../../notes/programs/01_signed_arithmetic_covariance/AGGREGATED_KERNEL_CONTINUATION_20261004.md).
- [Mixed discrepancy feedback](../../notes/programs/01_signed_arithmetic_covariance/MIXED_DISCREPANCY_FEEDBACK_20261004.md).
- [Exact kernel checker](../../numerics/01_signed_arithmetic_covariance/check_aggregated_kernel.py) and its [record](../../numerics/01_signed_arithmetic_covariance/aggregated_kernel_record_20261004.json).

## Scope and conclusion

The new results are reductions and method diagnostics. They remove an
unnecessary logarithmic loss, localize a divisor variable at a rigorously
budgeted power cost, and explain exact spectral feedback in a product of
two arithmetic discrepancies. They do not prove the remaining one-sided
inequality, an improved variance exponent, or a new zero-free strip.

Separate agents derived the small-divisor Poisson representation and the
mixed-discrepancy identity, and a further agent audited the Mellin residue
and deterministic power-mode calculation. The coordinating agent checked
normalizations, support, exponent arithmetic, and the exact numerical test.
The repository starting point was commit
`62ac139771ae317f6e4b624765783c6856739d8f` with a clean working tree.

## Analytic checks

The complement identity must include delta at m=1 globally. Its kernel
contribution vanishes on the retained interval only after U>C/A. This
justifies summing all multiples without an unrecorded lower-m correction.
The resulting Poisson sum has zero mean because integral v ell prime is
minus integral ell, which vanishes. The derivative measures are D^6 of
v ell prime and D^7 of ell; no additional smoothness is assumed.

The derivative kernel bound integrates against t to a constant independent
of X and U. It removes a log-squared factor but cannot change a subpower PNT
error into a fixed power. The primitive improves the exponent from six to
seven only because its Stieltjes integral uses total variation dtheta+dt.
Both E(T)P(T) and E(U)P(U) must stay. Including atoms in (U,T] verifies the
convention at prime endpoints.

For D=U X^(-kappa/14), the removed full-interval contribution is
O((D/U)^7)=O(X^(-kappa/2)). At the balanced cutoff,
D=X^(1/2-3kappa/28). For kappa=1/100 its exponent is 1397/2800, while U has
exponent 1399/2800. The prime variable reaches exponent 1401/2800. The
remaining signed integral is equivalent to the previous scalar target up
to an error at that same scale, for 0<kappa<14/29. No little-o comparison
is needed for this equivalence.

The terminal identity A_U(m)=mu(m) holds only where support imposes
U<m<=2U. It cannot be used on all m>U. The complementary divisor split
also must retain the original t integration interval even if each piece
has a larger support separately.

For mixed discrepancies, using M(s)-M(U) and E(t)-E(U) makes the strict
cutoff boundaries exact. The summed cofactor kernel has decay O(v^3) at
zero; its Mellin moment is z^2 zeta(z) L(z), initially proved by absolute
interchange on Re z>1 and then continued on Re z>-4. It must not be
obtained by termwise interchange outside that initial half-plane.

In the deterministic power-increment calculation, extending the product
variable integral down to zero is justified by the O(v^3) bound. The
remainder is O_z(X^(Re z-1) H^(-Re z-4)); a log H factor is unnecessary
because the relevant endpoint logarithm becomes log y under y=Hv. The
vanishing zeroth moment and logarithmic moment remove the increment
boundary terms in the full moment expression.

The simple-zero calculation is a deterministic complex-mode diagnostic.
It uses the coefficients that would belong to simple local poles; it does
not assert that all zeros are simple, that an actual zero expansion for M
converges, or that unexamined cross terms in the actual arithmetic may be discarded. The finite cross-mode formula was also reviewed: distinct zero modes have
vanishing leading moments, and a deterministic real conjugate pair
reproduces the original real scalar mode with the displayed lower-boundary
remainder. This is not a statement about an infinite expansion of the
actual errors. The real-beta saturation corollary follows directly from
continuity of the nonzero moment at one; it applies only to the broad
class of input functions subject to separate envelopes. The frozen
cutoff residue argument separately handles arbitrary zero multiplicity.
For moving cutoffs, the existing error comparison supplies the Mellin
tail continuation; substitution into a fixed-cutoff transform is invalid.

The main-note review found no substantive error and prompted three precision
fixes: the scalar comparison constant records its dependence on fixed kappa;
the seventh-order bound is called an improvement only for UT/X<=1; and the
singleton control comment specifies that its test point is outside the
retained interval. None changes the derivation or target budget.

## Reproducible finite checks

The standard-library checker completed 1,279 exact comparisons on 28
rational cases. It verifies the signed kernel and divisor identities,
partial-interval Stieltjes formula, error centering, and terminal shell.
The inputs deliberately use a polynomial kernel with rational coefficients
and atom weight p at prime p, rather than the fixed probe and log p.

Negative controls detect 277 nonzero omitted-endpoint instances, 15 cases
where the terminal formula used globally changes the correlation, and 28
cases requiring the global singleton correction. The counts are diagnostic
instances and do not measure asymptotic evidence. The record includes the
new script hash and the hash of the adjacent shared centering module.

These computations test finite algebra. They do not verify the analytic
variation constants, Fourier convergence, Mellin continuation, deterministic
power asymptotics, or the desired arithmetic inequality. Those items rely
on the displayed proofs and internal review. No numerical exponent fit or
large generated dataset is part of this continuation.

## Remaining obligation

Either sign of the complete localized correlation must still be bounded
at X^(-kappa/2) for one fixed positive kappa on all sufficiently large real
X. A product-envelope estimate or an independence heuristic does not
supply that result. The notes make this limitation explicit and retain
all signs, terminal intervals, and endpoint terms.
