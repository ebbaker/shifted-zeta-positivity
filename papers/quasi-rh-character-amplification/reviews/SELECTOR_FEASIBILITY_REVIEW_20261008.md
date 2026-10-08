# Scoped review of the row-selector feasibility gate

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

This is a fresh same-model review of
[SELECTOR_FEASIBILITY_20261008.md](../notes/SELECTOR_FEASIBILITY_20261008.md).
It is not specialist refereeing or formal verification. The source's deep
moment and zero-free results remain assumptions. The reviewed local text
of the September 30 companion matches the PDF identity recorded in the
[continuation input review](CONTINUATION_INPUT_REVIEW_20261008.md).

No mathematical defect was found in the exact sixth-power extraction,
the conditional budget calculation, or the stated elementary mean-zero
partial theorem. Their conclusions do not establish the requested mixed
saving. The following checks specify the scope of that assessment.

## Positive enlargement and unit multiplicities

The smooth majorant is applied to the whole nonnegative norm. This makes
`E_C <= E_Phi` valid without inserting the exceptional-row indicator into
a smooth Poisson kernel. The argument does not enlarge individual signed
column-pair contributions.

For each nonzero ideal `a`, the sixth power of a generator is independent
of the generator because the six units all have sixth power one. If two
such elements agree, their generators differ by a sixth root of unity and
their ideals agree. Hence the ideal-indexed sum counts each sixth-power
row once. Its `O(U^(1/6))` size is correct; an additional factor six would
be incorrect. The factor six in the separate smooth lattice count has a
different purpose: it divides the six generators of each ideal.

For a general row `u`, valuations modulo six recover its sixth-power-free
ideal and the remaining sixth-power ideal uniquely; retaining the unit
in the seed `b` then recovers the element. The principal-seed extension
uses the source's local ramification fact: a valuation from one through
five outside the fixed excluded primes gives a nontrivial local
character that the fixed ray twist cannot cancel. Consequently principal
seeds are supported on the fixed set and form a finite set. Their unit
factors must remain distinct. This uses the same character presentation
as the manuscript and does not assert such a decomposition for arbitrary
unrelated row characters.

## Masks and the normalized plain error

For `u = alpha_a^6` and `nu = 1`, the displayed character value is exactly
`1_(a,n)=1`, for either orientation. The extracted inverse, plain and
prime factors therefore retain every original moving coprimality mask.
Taking their product also retains masks on primes shared by different
column variables. The fixed exclusions remain in the original column
supports throughout.

Let `R_a` be the union of those fixed exclusions with the prime divisors
of `a`. Inclusion-exclusion reduces the unnormalized plain sum to smooth
ideal sums at scales `N/Ne`, for `e | R_a`. On the sixth-power dyad,
`Ne <= C U^(1/6)`, whereas `N >= U^(9/25)`. Thus every residual scale is
at least one for sufficiently large `U`.

For a smooth annular profile, Poisson summation on the fixed Eisenstein
lattice gives the area term with an absolute `O(H^J)` error on such
scales. Dividing by six counts ideals. Summing the errors over the
divisors of `R_a` costs only `U^epsilon`. Normalizing the original plain
sum by `N^(-1/2)` therefore gives exactly

    S^(a) = N^(1/2) c(a) beta_B
               + O_epsilon(N^(-1/2) U^epsilon H^J).

In particular the error is not inferred from a sharp ideal-count error
of order the square root of the scale. Source Lemma 18.3, equation
(18.45), independently states this smooth absolute-error estimate.

The coefficient `c(a)` is positive in the principal case, is bounded
above by a fixed constant, and has reciprocal `O_epsilon(U^epsilon)`.
The main integral must include the actual norm twist. Its vanishing at
one parameter does not imply vanishing for the derivative profiles used
in a Sobolev argument. The note states that limitation explicitly.

The prime deletion identity is exact. Its error bound uses only
`omega(a) = O(log U)` and the profile supremum. No prime distribution
claim is needed for it. Conversely, arbitrary permitted prime lists and
bounded complex coefficients need not have positive principal mass.
For bounded prime slots, any lower-bound diagnostic must retain the
additional coprimality restriction on the roots, as the note does.

## Conditional inverse budget

The weight `G(a) = U^(-m-z)|S^(a)Q^(a)|^2` gives the stated equivalence
without an asymptotic. An unweighted inverse requirement follows only on
the subfamily where a lower bound for this actual weight has been
established. This distinction prevents a diagnostic main-term example
from being asserted for the detector's unspecified fixed profiles.

Assuming the source's global seven-eighths theorem, Lemmas 4.9 and 4.10
bound the reciprocal of zeta and the inverse deleted Euler product on
`Re s = 7/8 + v`. Smooth Mellin inversion gives
`|M^(a)|^2 << D^(3/4+epsilon) U^epsilon H^A` after allocating the small
losses. The principal pole contributes no residue to the reciprocal.
The original smooth inverse profile is retained in that argument.

Summing over the roots gives exponent `1/6 + 3r/4`. Against the inverse
budget `B6 = 1-(1-delta)m-z-eta`, and putting
`z=(1-r)/2-rho`, the exact difference is

    (1-delta)m + r/4 - 1/3 + eta - rho.

Its extrema before `-rho` are `19/375` and `1289/7500`. The corresponding
sufficient pointwise exponents `sigma_req` at `rho=0` have extrema
`16847/22200` and `3523/4200`. These were also recomputed directly with
rational arithmetic. Monotonicity proves the extrema on the continuous
box; checking corners alone without that argument would not suffice.

The profile-sensitive upper bound correctly retains `beta_B` and the
actual unmasked prime sums before applying triangle bounds. The positive
deficit is a failure of the checked upper bound to reach the target. It
does not supply a lower bound, a counterexample, or a necessary zero-free
half-plane. Principal row conductors are correctly distinguished from
the ratio conductors of column pairs.

## Elementary partial theorem and remaining scope

When `beta_B=0`, the normalized plain estimate gives
`|S^(a)|^2 << N^(-1) U^epsilon H^A`. The direct bounds
`|M^(a)|^2 << D H^A` and `|Q^(a)|^2 << U^z H^A`, followed by the root
count, yield exponent `1/6+r-m+z`. No imported seven-eighths theorem is
needed for this partial bound. Since `z <= (1-r)/2`, its margin below
`K` is at least

    1/3-r/2+(1+delta)m-eta >= 6791/15000.

The minimum is attained at `r=37/50`, `delta=m=9/25`; the expression is
monotone in each variable on the box. Bounded slots and empty supports
cause no exception to the upper bound. The finite principal-seed
extension introduces only fixed constants.

This theorem controls one added layer, with a stated profile condition.
It does not bound the other rows of the smooth enlarged family and does
not control the actual restricted mixed moment. The note's decision to
keep the row selector unless the added rows are independently settled is
therefore justified. Its selector-preserving positive estimate remains
an open input, equivalent at the target scale to the existing one-sided
signed-kernel target. No new zero-free payoff follows from the partial
theorem.

## Manuscript consolidation and executable check

The added manuscript subsection `sec:selector-test` was checked against
the detailed note. Its exact sixth-power norm, character-zero masks,
plain main term and normalized error, prime deletion identity, weighted
inverse budget, and rational gap interval agree with the reviewed
calculations. Proposition `prop:mean-zero` includes the needed hypotheses
`nu=1` and `beta_B=0`, and its proof obtains the exponent and uniform
margin above without assuming the source's zero-free theorem. The
surrounding text correctly restricts this proposition to the principal
layer and retains the derivative-profile and other-added-row limitations.
No mathematical correction was needed in that subsection.

The command

    python3 papers/quasi-rh-character-amplification/numerics/check_selector_feasibility.py

completed successfully, reproducing the selector budget constants stated
above. The rational assertions and their monotonicity comments were also
read. The script includes separate live-divisor identities; their full
arithmetic transform is outside this selector review. Compilation and
rendering are recorded by the parent continuation, not inferred from
this algebraic check. No hashes are fixed by this review while the parent
manuscript remains under consolidation.

## Final parent consolidation record

After the selector review, the parent added the checked live-divisor
summary to the same manuscript, linked the research and review records,
and compiled the final saved source successfully with the desktop
editor's native compiler on 8 October 2026. The editor was requested
to open the existing manuscript. This records compilation, not a
rendered-page visual inspection or an exported PDF.

The exact arithmetic record reproduces byte-for-byte from
`check_selector_feasibility.py`. All 68 manuscript labels are unique;
all 70 `ref`/`eqref` uses resolve. Local links in the changed research
indexes and new notes/reviews resolve, and `git diff --check` passes.
The checks do not prove any of the remaining analytic estimates.

Final manuscript SHA-256:
`535ea905ebf9e84ce38c1f349cd8bec73b04cdf46b345e6e97058460fee58bd5`.
No commit, tag, manuscript snapshot folder, or third-party PDF was added.
The pre-existing uncommitted continuation plan was left intact.
