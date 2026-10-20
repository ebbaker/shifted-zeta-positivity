# Review: zero deflation and rational resolution

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded session metadata. Several separate same-model
derivations and cross-checks; **no specialist or different-model review**.

**Verdict:** the quantitative statements in [Note 04][note] pass this
internal analytical review. They establish error budgets and scoped
estimator limitations, not RH-to-simplicity or a new theta exclusion.
The [program][program] and [progress register][progress] retain their
positive arithmetic and strict-surplus gates.

## 1. Identities and constants checked

- **Deflation and membership.** The full and finite Stieltjes formulas
  include the endpoint contribution. Their bounded count-error norm is
  one; the annular version uses its own enclosed cumulative count.
  The power-kernel Lipschitz maximum is at
  `|r|/delta=(2n+1)^(-1/2)`, giving Note 04 (3), including
  `3 sqrt(3)/(8 delta)` at `n=1`. The second Poisson sample bounds the
  entire remaining tail, without discarding distant or reflected zeros.
  The final multiplicity enclosure in (6) has width
  `(T_+-T_-)+(L_+-L_-)+epsilon`.
- **Actual tail.** Two derivations check the coefficient, sharp error
  and endpoints in (7). The radial count changes from a difference to
  a sum when `r` crosses `gamma`. Subtracting `rL/pi` on **both** sides
  of that transition leaves the stated `O_delta(1/gamma)` distant
  error. The lower endpoint `-K(H)C(H)` is necessary. All original
  multiplicities are included. With `H=cL`, the residual tends to
  `delta^2/(pi c)` and the noncentral count is asymptotic to `cL^2/pi`.
- **Arithmetic resolution.** The derivative formula begins with
  `(1/delta) Re xi'/xi=sum m/(delta^2+v^2)`, so the factorial and power
  in (10) are correct. The Gaussian Fourier integral, finite positive
  coefficients, prime prefactor `1/pi` and two pole terms agree.
  The test meets the analytic-strip explicit-formula conditions for
  every finite `n` and `delta>1/2`.
- **Absolute prime payment.** At the auxiliary ordinate zero,
  `C_n=2r_delta^n+G_n(0)-S_n(0)` is exact. `xi(1/2)!=0` and total zero
  counting justify a fixed `N_abs(T)<=C T^2` for all `T>=0`. Thus
  `S_n(0)<=C delta^2/(n-1)` for `n>=2`; the same restriction is used
  for the first absolute moment of the kernel. This proves uniform
  `C_n=2r_delta^n+O(I_n)` on all sequences with `I_n->0`.
- **Optimization.** The even-unimodal logarithmic probability bound
  integrates to exactly `2 log 2`, proving the gamma lower bound
  uniformly in both parameters. Any competitive sequence forces
  `I_n=O(1/sqrt(log L))`, so the preceding uniform payment identity
  applies. `n log r_delta>=n/(4delta^2)` gives the lower constant
  `1/(4sqrt(pi))`; fixed arbitrarily large delta gives the matching
  upper constant. The proof does not exchange an unproved fixed-delta
  and variable-delta limit. Both the fixed-parameter statement (17)
  and full infimum (18) pass.
- **Conditional certificates.** The separation and inverse-square
  estimates follow termwise by positivity. The coordinate conversion
  `S_x=T_gamma/4` is correct. The monotone incomplete-gamma payment
  covers every prime-tail term when `log X>=n/sigma`; no actual
  numerical multiplicity recovery is claimed.
- **Trigonometric audit.** For every allowed `k`, the denominator
  bracket is at most `p_delta(0)+p_delta(2gamma)` term by term.
  Its delta derivative has the stated strictly negative numerator.
  The ratio lower bound requires `a_gamma>0`, as used. The finite
  threshold `2pi exp(9)` gives a strict value above two without a
  numerical approximation. `T=1+cos theta` with
  `sigma-1=(log gamma)^(-1/2)` attains the leading constant `1/4`.
  Nonnegative combinations at different sigma preserve the lower
  bound; arbitrary signed Toeplitz constructions are outside it.

## 2. Corrections and precision requirements resolved

1. Replaced the draft's ambiguous error condition by **interval width
   below one**; an error radius below one would allow two integers.
   Even width below one does not specify which integer is recovered.
2. Restricted the illustrative `N(gamma+r)-N(gamma-r)-m` membership
   formula to `0<r<gamma`, with consistent boundaries. The full radial
   formulas independently count both positive and negative ordinates.
3. Made the annular error hypothesis explicit. Subtracting two
   uncertain cumulative counts cannot be charged as one endpoint error.
4. Required sample and completeness enclosures uniformly at the actual
   target ordinate when its location is uncertain. A midpoint sample
   without correction does not have central contribution exactly `m`.
5. Separated the sufficient window from the second-sample upper bound
   from the necessary asymptotic cost proved using the actual tail.
   A big-O upper bound alone cannot establish necessity.
6. Specified the polynomial control's function and derivative sign:
   the failure is `-D_A'/D_A<0` on the far positive real axis. The bare
   polynomial's ordinary derivative ratio has the opposite sign.
7. Fixed a stray punctuation token in the staged gamma integral.
   Also corrected two doubled TeX backslashes before `sqrt X` in
   [Note 02][n2]; that repair changes formatting only.

The complete proofs are in Note 04; staging discussions are not treated
as additional repository results. No unresolved mathematical objection
from these internal checks remains in the installed statements.

## 3. Controls, imports and scope

The endpoint Euler and isolated positive-source controls retain their
central mass two after every legitimate noncentral subtraction. Their
changed arithmetic is retained: the first changes conductor and has
negative logarithmic coefficients; the second lacks an ordinary
Dirichlet series. Zeta powers change degree, pole order and coefficient
size. None is asserted to satisfy every unchanged zeta premise.
The isolated control can approach a base zero, defeating a uniform
inverse-square upper bound based only on the broad structural premises.
This does not defeat an estimate using the exact original arithmetic.

The primary inputs rechecked were [Goldston–Gonek][gg], equations
(1)–(4), Theorem 1, Corollary 1 and Lemma 1, for counts and the explicit
formula; and [DLMF 10.49][dlmf], for the terminating half-integer
coefficients. The Fourier integral also derives those coefficients.
These inputs do not assume simplicity. The sharp tail and optimized
envelope are derived here from those inputs, with no novelty claim.

No sign scan, new empirical dataset or manuscript was started. The
existing 265-fixture exact-algebra replay was not rerun because none of
its formulas or code changed; it does not certify this note's infinite
estimates. Analytical cross-checks supply the present validation.

The scope rules in [avoid 01][a01], [02][a02], [05][a05], [07][a07],
[12][a12] and [20][a20], and the [collision catalogue][controls], were
applied. The reviewed conclusion is **explicit deflation costs and
scoped estimating failures**. There is still no strict cap surplus,
negative Gaussian deficit, excluded theta multiple-zero class, or
all-zero simplicity proof.

[note]: ../notes/04_ZERO_DEFLATION_AND_RATIONAL_RESOLUTION_20261020.md
[n2]: ../notes/02_FINITE_PRIME_FEJER_RESOLUTION_TEST_20261020.md
[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[progress]: ../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md
[gg]: https://arxiv.org/pdf/math/0511092
[dlmf]: https://dlmf.nist.gov/10.49
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
