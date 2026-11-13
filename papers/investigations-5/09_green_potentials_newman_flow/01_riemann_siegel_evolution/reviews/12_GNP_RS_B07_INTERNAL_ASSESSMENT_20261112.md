# GNP-RS-B07 — contributing internal assessment

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Separate analytical reviewer in
chat0006, thread `01a1d151-91b1-7663-8f10-07d0b4f94163`. The actual backend
model and reasoning effort are unavailable in this agent's record; neither
is inferred from a recommendation or inherited task label.

**Disposition: accept Note23 at its stated inherited-input proof scope.**
The [proof](../notes/23_GNP_RS_B07_LOCALIZED_TAIL_AND_EXACT_BOUNDARY_20261112.md)
provides a quantitative improvement from the B06 interval exponent 3/8 to
1/4, with a positive fixed slack in each case. The exact boundary-weight
lemma removes the separate growing edge penalty. These are averaged
estimates, with no every-center consequence asserted.

This assessment is **contributing separate-agent internal checking**.
The reviewer supplied the exact convolution-weight variation/mass argument
and the weighted finite-head constants, then checked the completed proof.
The reviewer also independently checked the shifted third-derivative
calculation and its exponents against the primary source. Other helpers
contributed the arithmetic and oscillatory analysis. This is not an
independent specialist assessment or a demonstrated different-model review;
all share the inherited HDA/E01–E06 inputs.

## 1. Accepted statement and evidence level

For every fixed \(0<\rho\le1/4\), all sufficiently large real U, every
integer \(2\le P\le\lfloor L_U^2\rfloor\), and
\(U^{1/4+\rho}\le\ell\le U\), Note23 proves
\[
 |\mathscr R(U,\ell;P)-\mu_P|
 \le C\bigl(\sqrt{\mu_P}/L_U+L_U^{-2}\bigr)
       +O_\rho\bigl(U^{-\min(1/128,5\rho/24)}\bigr).
\]
At \(P_U=\lfloor L_U^2\rfloor\), the residual mean error is
\(O_\rho(L_U^{-3/2})\), and the mean itself is
\(O_\rho(L_U^{-1})\). The inherited transfer then yields Green mean
\(O_\rho(L_U^{-1/3})\) and fixed-threshold exceptional proportion
\(O_{h,\rho}(L_U^{-1})\). The source, physical clock, carrier, c=1
slice, block-constant prime cutoff and original Green geometry are retained.

The [result index](../../../../../result-summaries/README.md),
[heat-flow cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
and [avoid index](../../../../../avoid/README.md) govern the classification.
This is a quantitative milestone under
[avoid01](../../../../../avoid/01_restating_the_target.md), not an
RH-equivalent reformulation or an every-center estimate obtained from a
mean. The constants and finite onset have declared analytical dependencies;
their numerical values are not certified.

## 2. Exact boundary and norm checks

The distinction between the exact weight W and the full convolution
\(W_\infty\) is used only to bound total variation. For each fixed X,
the removed two-sided kernel tail has variation \(4K(r_X)\), including
both jumps. Applying the triangle inequality on each finite partition
before integrating over X proves
\[
 \operatorname{TV}(W)\le1+\ell/(2U^4).
\]
This does not differentiate the moving radius or drop the cutoff.
The kernel tail also gives the mass bound
\(1-(4/\pi)U^{-4}\le m_\sigma\le1\) for
\(d\sigma=2W\,dx/\ell\). Fubini's factor 1/2 is retained exactly.
The constant diagonal is therefore restored with only
\((4/\pi)\mu_PU^{-4}\), not a pointwise complete-arm envelope at the
outer endpoints.

The nonnegative smooth majorant equals one on a set containing the entire
support of W when \(r_*\le\ell\). Consequently it is consumed only
as an upper bound for squared norms. It does not replace the exact weight
in the diagonal or reflected calculation. The condition
\(Y\le N_{U-2\sqrt U}\) covers the full smooth-majorant support and
keeps every retained head mode active.

For finite coefficient products, the displayed weighted variation bound
\(\sup|Wa|+\operatorname{TV}(Wa)\le4g_kg_l\) is valid.
The normalization \(2/\ell\) then gives same-arm constant
120000, below the chosen 150000. The adjusted curvature gate is evaluated
at \(U-r_*\), while the lower carrier-curvature bound uses the enlarged
support inside \([U/2,3U]\). Together with the frequency gate it gives
the partial-integral bound \(48/L_0\). The reflected constant is
\(2\cdot2\cdot48\cdot4(8/3)^2<8000\), as stated.

The coefficient-diagonal estimate remains independent of P in its slowly
decaying error. The measure has mass at most one, so all triangle and
Cauchy–Schwarz comparisons in (B07.25) retain their constants. The original
physical-time and complete-field costs are paid before Fubini; neither
the floor cutoff nor the exact field remainder is differentiated.

## 3. Discrete tail estimate and source verification

The reviewer opened and read all three pages of Noam Elkies's
[author-hosted handout](https://people.math.harvard.edu/~elkies/M229.09/vdc.pdf).
Its inequality III and differencing proof support the discrete
third-derivative estimate used in (B07.13). Negative derivative is handled
by conjugation, and translated shorter partial intervals retain the same
bound with the encompassing block length. The trivial parameter regimes
and the integer choice of differencing length are covered. The
[source-use record](../references/01_GNP_RS_B07_DISCRETE_DERIVATIVE_SOURCE_USE_20261112.md)
correctly identifies this handout as the formal input; the separate Robert
copy is not needed to justify the theorem hypotheses.

Freezing the complete arithmetic arm over the entire majorant support
costs \(O(U^{-5/16})\) in amplitude. Weight and small-phase drift cost
\(O(\ell U^{-13/16})\), and the changing cutoff contributes
\(O(1+\ell/\sqrt U)\) terms, each \(O(U^{-5/16})\).
The squared-norm inequality gives the claimed \(U^{-5/8}\) error.
This step retains the actual cutoff crossings and involves no uniform
approximation of the full arm by its limiting fixed-index coefficients.

For comparable pairs, the phase satisfies
\(f_h'''\asymp-Uh/N^4\) on every allowed partial interval.
The explicit lower and upper constants in (B07.12) are valid. The amplitude
variation in (B07.15) follows from the coefficient logarithmic derivative
and one additional power of Fourier decay. The exact partition is by the
smaller index m; it therefore retains cross-block pairs instead of applying
blockwise Cauchy–Schwarz.

After the discrete estimate, the shift sums give exactly
\[
 U^{1/6}N^{1/4}\ell^{-7/6}
       +U^{-1/6}N^{3/4}\ell^{-5/6}.
\]
Both block powers are positive, so the dyadic sum is geometric and produces
\(U^{7/24}\ell^{-7/6}+U^{5/24}\ell^{-5/6}\) without a logarithmic
loss. Noncomparable pairs supply \(U^{3/8}\ell^{-4}\).
The exact diagonal and freezing costs complete (B07.19).

At \(\ell\ge U^{1/4+\rho}\), these two arithmetic errors become
\(U^{-7\rho/6}\) and \(U^{-5\rho/6}\). The residual comparison takes
their square roots; the slower term is \(U^{-5\rho/12}\).
The fixed head and multiplier cutoffs contribute \(U^{-1/64}\).
Absorbing the uniformly subpower Euler products gives the stated exponent
\(\min(1/128,5\rho/24)\). The finite-head same-arm logarithm is smaller
after the declared \(\rho\)-dependent onset. B06 with its parameter 1/8
covers \(\ell\ge\sqrt U\), so the two proved ranges overlap without
changing the reference cutoff or physical time.

## 4. Scope, controls and remaining work

The control screen follows the
[catalog](../../../../../result-summaries/12_collision_controls_and_screening.md),
[premise rule](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scope rule](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
Generic variation, derivative-test and norm inequalities can hold for
controls. Literal reuse also requires the canonical full arithmetic arm,
reflection, physical readout and field identification. A finite collision
does not by itself contradict the new asymptotic mean law. No witness is
relocated into the shrinking-time band, and no historical collision
certificate is rerun.

At \(\ell=U^{1/4}\), the two displayed tail majorants are order one.
This is the precise limitation of the current absolute summation over
shifts after a third-derivative bound. It is neither a lower bound on the
actual canonical correlations nor an obstruction to all local estimates.
The exact boundary lemma itself adds no growing edge penalty. The
[continuation](../notes/24_GNP_RS_B07_RETURN_AND_MODEL_CHANGE_20261112.md)
can therefore identify the remaining shifted arithmetic sum without
reopening the already paid boundary problem.

The result still permits localized positive Green mass. No every-center
estimate, moving-time persistence theorem, fixed-time zero count, full-c
extension, bounded-height coverage, shrinking-depth conclusion, time-zero
result or positive-threshold exclusion follows. The inherited provider
retains its original internal-review status. No height sampling, interval
certificate or new numerical evidence for an onset or sign was used in
this assessment.
