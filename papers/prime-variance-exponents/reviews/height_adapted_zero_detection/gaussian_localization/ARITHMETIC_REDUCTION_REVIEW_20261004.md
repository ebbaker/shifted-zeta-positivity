# Internal review of the Gaussian arithmetic reductions

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. Exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is same-model internal analysis and cross-review, not independent
specialist refereeing or formal proof verification.

The [finite Gaussian Möbius reduction](../../../notes/height_adapted_zero_detection/gaussian_localization/FINITE_GAUSSIAN_MOBIUS_REDUCTION_20261004.md)
and [height-uniform Vaughan comparison](../../../notes/height_adapted_zero_detection/gaussian_localization/HEIGHT_UNIFORM_VAUGHAN_REDUCTION_20261004.md)
have been checked internally. The identities and effective omitted-error
bounds support the stated conditional detector criteria. The retained
signed arithmetic inequality remains unproved; no new zero-free region
or numerical zero certificate follows from this review.

## Direct Gaussian reduction

Separate calculations checked the exact full-Lambda Möbius identity,
order-two Poisson coefficient, tilted Gaussian fourth moment, and bound
\(\|W''\|_1\le(T^2+1)e^{-511k/16}\). Removing divisors
\(d\le e^{15k}\) leaves the continuum coefficient with sign minus,
\(-\Phi(1)(1+L_D)\), and costs
\((5k/4)(T+1)^2e^{-31k/16}\).

The product tail was checked with the full divisor cumulative coefficient
bound, rather than a prime-only bound. The polynomial coefficients,
\(P(8)/8^2=219062021/234256\), and resulting
\(250k^{3/2}e^{-5k/2}\) bound agree. The strict divisor cutoff,
weak product cap, strict cofactor ceiling, and terminal \(B/r\) cap
are preserved. No lower product tail is silently deleted.

The optional continuous frequency-band bound costs
\(80k e^{-5k/2}\). Each deleted-error sector is below
\(\eta_N/16\) for every saved sample and every admissible carrier.
The direct criterion gives \(|\mathcal Z|<7\eta_N/16\); its
band-limited alternative gives the strict bound
\(|\mathcal Z|<\eta_N/2\). Both contradict the inherited detector
only if the retained arithmetic bound holds for every required carrier
and sample. Coverage of a continuous carrier interval is still required.

The fixed-cutoff meromorphic series retains every nontrivial zero residue
and the pole coefficient \(1+L_D\). The feasibility discussion correctly
limits its claims: phase factorization alone supplies no mixed-variable
oscillatory gain; testing absolute PNT envelopes is not an impossibility
theorem for signed cancellation. The optional relative-saving diagnostic
is not a necessary lower bound for the actual observable.

## Height-uniform scalar comparison

The derivative, measure, Poisson, and Vaughan calculations were checked
separately. The constants \(2^{74}T^7\), \(2^{75}T^7\), and
\(\kappa_7<2^{-16}\) give the explicit comparison

\[
|\lambda_t(X)-\mathcal J_{U,V;t}(X)|
\le2^{59}T^7X^{-7}[(1+\log X)U^7+(UV)^7].
\]

Two intermediate wording defects were corrected before saving: the
Euler-polynomial coefficient sum includes the coefficient of \(D_v\),
and the measure-conversion exponent uses \(|j-1/2|\). The interior
polynomial derivative range was extended through order nine to cover
the highest derivative's interior part. The final constants remain valid.
The final note also proves \(V<AX\) separately from \(U<X\).

The cutoff \(U=V=2^{-5}\sqrt{X/T}\,r^{1/14}\) satisfies all
support and lattice hypotheses on the saved scalar interval. It gives
an error at most \(2^{-10}r\), retaining the exact nonzero continuum,
all terminal support caps, and full \(\Lambda\) prime powers.
It localizes the missing estimate and does not provide a power saving
for the retained sum.

## Exact checks and practical limits

The [numerical guide](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
links two new standard-library replay sources and small records. The
direct checker passed 4,096 formal prime-log coefficient identities,
48 component checks with synthetic complex rational weights, Gaussian
moment calculations, the exact upper-tail polynomial, and outward budget
arithmetic. It checks its elementary-enclosure dependency's SHA-256 before
using it. The Vaughan checker passed 34 exact rational constant checks,
including the base probe norm, ninth derivative atoms, polynomial operator
coefficients, and final error constants.

No floating-point decision enters these new checks. The records identify
their source hashes; hashes identify files and do not prove inequalities.
Finite synthetic examples test algebra and conventions. The analytic
all-sample proofs are in the notes; these scripts are not proof assistants.
Neither script evaluates the enormous retained Möbius or Vaughan sums.

The deliverable is an effective arithmetic reduction and two precisely
stated sufficient hypotheses. The next substantive research task is a
complete signed dyadic estimate with its divisor, cofactor, and carrier
ranges stated, or a sharper Poisson analysis that reduces those costs.
An external specialist review and literature audit are needed before
making novelty or publication claims.
