# Review: correlation resolution and Möbius energy

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded turn metadata. Separate derivations and cross-checks
within the same model; no specialist or different-model review.

**Verdict:** [Note 06][note] establishes the stated quantitative costs
within its declared information classes. It gives no upper arithmetic
estimate that excludes an original theta multiple zero. The positive
RHS-02 estimate, strict cap surplus and all-zero coverage remain open.

## 1. Finite-window correlation

The squared triangular Fourier transform gives exactly
`R(z)=6(z-sin z)/z^3`, with normalization `R(0)=1` and
`integral K_Delta^2=2/(3 Delta)`. Thus the unweighted occurrence diagonal
is `N`, coincident distinct occurrences contribute `sum m(m-1)`, and
all other pairs contribute strictly positively. A double costs two in
absolute excess units. Neither an `o(N)` error nor a proportion result
proves that this excess is below two.

The global surrogate `R(z)>=6/(|z|+3)^2` was checked independently on
`|z|<=2` using the alternating sine bound and on the complement using
`5z^2+3z-9>0`. Jensen applies to that convex surrogate; no convexity of
the oscillatory exact kernel is assumed. Listing all `N` occurrences,
including repeated locations, makes the explicit lower sum valid for
arbitrary multiplicity and clustering. The `k=1` term gives the initial
positive lower scale. Fixed-`K` summation followed by `K->infinity`
gives the sharp necessary constant `1/2` in
`liminf Delta W/N^(3/2)>=1/2` for successful certificates.

The equally spaced calculation has error `O(N/q^3)` and limit
`1/(2c^2)`, so it checks sharpness of the leading geometric constant.
It does not posit equal spacing for zeta. The whole-interval corollary
has coefficient `1/[2(2pi)^(3/2)]`; multiplying by `2pi` gives the
claimed nominal logarithmic prime horizon.

The exact quadratic prime expansion retains the complete gamma and
pole factor, the mixed term with that factor, and **both** frequencies
`log(n/r)` and `log(nr)`. Positivity of a Gram matrix cannot remove
these signed terms. The full zero sum has divergent unweighted square
integral and cannot replace the finite-window sum without payment.
The explicit extension by `R` on either side costs precisely
`N^2/(pi^4 Delta^3 R^3)`; exterior zeros within the enlarged interval
remain in the arithmetic expression. A numerical upper enclosure, if
one were attempted, would have to fit the actual slack below `N+2`,
not merely have an error smaller than two.

## 2. Universal multiplicative phases

The declaration of the phase class is essential. Complete
multiplicativity and every universal nonnegative square are preserved
by arbitrary prime phases, while an actual zero ordinate and RH's
full spectral information are not asserted for the witness.

At the all-negative prime assignment, only even powers distinguish
the signed sum from its completely negative absolute envelope. The
substitution `n=p^j` gives exactly the tapered sum of `Lambda(n)/n`
through `exp(V/2)`. Partial summation from the PNT gives limiting
correction one. Prime squares supply its leading part, and higher
even powers contribute `O(1/V)`.

For `p>=64`, the harmonic derivative sum at `r=1/8` is
`233/343<1`. Hence the first harmonic dominates every possible gain
from the others and the local minimum is at phase `pi`. The finitely
many smaller primes cost at most `K/V`, with
`K=4 sum_(p<64) log p/(sqrt p-1)`. This checks the lower bound as well
as the phase witness, establishing the actual torus minimum
`mu(V)=-C_V+1+o(1)`.
The final consolidation explicitly discards the zero-weight endpoint
before using the strict first-harmonic inequality; this repairs the
one missing qualifier identified in the final review.

The optimized additive comparison is uniform: the envelope difference
is bounded for all `V>=2pi`, and bounded bandwidth cannot compete with
Note 02's `log gamma/log log gamma` upper candidate. Thus near-minimizers
for both envelopes have `V->infinity`, making their infima differ by
`1+o(1)`. The microscopic `V=log gamma` payment and the exact signed-pole
comparison agree with Note 02's constants. This does not close all
signed Toeplitz or event-conditioned methods. It closes only the
claimed improvement from universal phase positivity for this consumer.

## 3. Möbius normalization and local energy

RH provides enough growth control to justify the Laplace identity
on `Re z>0` and Plancherel on `Re z=alpha/2`. The latter half-factor
is necessary for the constants. Local Laurent expansion at a zero of
exact order `m`, followed by scaling in disjoint neighborhoods of the
conjugate pair, gives
`2 binom(2m-2,m-1)|m!/(rho zeta^(m)(rho))|^2`.
For a double this is `16/|rho zeta''(rho)|^2`. The remainder of the
integral is nonnegative; no global zero expansion or negative
derivative moment is invoked.

The polynomial oscillation verifies sharpness for isolated-pole
extraction only. The finite-interval consequence correctly states a
**limsup**, with coefficient `8/[3|rho zeta''(rho)|^2]` for a double.
No Tauberian lower-liminf conclusion is smuggled in.

Summation by parts of `M(n)^2` gives the ordered correlation identity,
including the `n=1` term and the factor `1+alpha`. RH makes its boundary
term vanish for every `alpha>0`; it does not make the off-diagonal
series absolutely convergent there. The diagonal contributes only
`6/(pi^2 alpha)+O(1)`. Thus any cubic energy of a double must be
carried by the signed Möbius correlation, which remains unbounded in
the needed direction. Fixed positive Gaussian smoothing leaves the
pole exponent and a positive local coefficient; it does not provide
an upper bound or identify this energy with the theta deficit.

## 4. Imports, scope and research disposition

The primary-source checks included [Goldston][goldston], §5, and
[Goldston–Lee–Schettler–Suriajaya][pcc], Theorem 1, for the distinction
between proportion and all-zero conclusions. No best current proportion
or priority claim is made.

The opening theorem of [Balazard–de Roton][bdr] gives the stated
RH Möbius upper bound. Splitting its Abel integral at
`C alpha^(-2)(log(1/alpha))^(5+2eta)` yields (24), still much larger
than any fixed polynomial divergence. [Bui–Florea][bf], Theorem 1.2,
requires `log(1/beta)/log log T` bounded; it cannot be applied with
`beta->0` at fixed candidate height. [Bettin–Conrey–Farmer][bcf],
Theorem 1 and its following paragraph, explicitly retain the
simplicity already built into their derivative-moment hypothesis.
These imports supply no hidden all-zero upper bound.

The final note consolidates the three attempts; no separate criterion
family or broad source control was added. Existing endpoint controls
pass the correlation identity on their own data and fail unchanged
zeta arithmetic as already recorded. The new quantitative costs do
not prove impossibility for exact arithmetic or genuinely localized
correlations. The [progress register][progress] keeps those tasks open.

No numerical scan, additional zero certificate or manuscript was run.
The existing exact algebra replay was unchanged and was not rerun;
it would not certify these analytic estimates. Validation consists
of the written proofs, separate same-model cross-checks and primary
source verification, governed by [avoid 01][a01], [05][a05],
[07][a07], [12][a12] and [20][a20].

[note]: ../notes/06_SIGNED_CORRELATION_RESOLUTION_AND_MOBIUS_ENERGY_20261020.md
[progress]: ../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md
[goldston]: https://arxiv.org/pdf/math/0412313
[pcc]: https://arxiv.org/pdf/2503.15449
[bdr]: https://arxiv.org/pdf/0810.3587
[bf]: https://arxiv.org/pdf/2302.07226
[bcf]: https://arxiv.org/pdf/1211.5191
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
