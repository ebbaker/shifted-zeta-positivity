# Polymath's error structure and a possible backward use

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. The guarded chat registry records
**gpt-6-astra, reasoning effort max**. Status: **selected-source audit,
elementary derivations and prospective acquisition question; same-assistant
checks**. No new canonical gap bound, improved onset, independent review,
manuscript milestone or main B/E task activation.

Read-first routing: [result index][results], [Cluster18][cluster],
[avoid index][avoid], [classification01][classification],
[premises02][premises], [scope07][scope], [joint bounds12][jointbounds]
and [Controls12][controls]. Under classification01, the equations below
are identities and the proposed finite comparison is a prospective
quantitative milestone. Their derivation is not evidence for RH or an
unacquired separation estimate.

## 1. The source has more information than its clock theorem

The selected passages of [Polymath, arXiv:1904.12438v2][source] are:

| Passage | Reusable information |
| --- | --- |
| §4, (35)--(41) | Exact Gaussian representations of arithmetic terms and the remainder, with a fixed integer cutoff. |
| Proposition 6.1, (44) | Explicit relative error for each approximated arithmetic term. |
| Proposition 6.3; Corollaries 6.4--6.5 | Riemann--Siegel remainder, its leading correction, and separate absolute error payments. |
| Theorem 1.3; (69)--(74) | Normalized finite-sum approximation for 0<t<=1/2, x>=200, 0<=y<=1. This domain does not require x>=exp(C/t). |
| Lemma 8.4; (92) | Spatial/time derivatives and holomorphy of the finite-sum approximant away from cutoff jumps. |
| Proposition 9.1; (99)--(104) | Dominance of the n=1 terms leads to two-carrier cancellation, clock localization and the exponential onset. |

The source-reading provenance and a coefficient issue are recorded in
the [updated receipt][receipt]. No numerical value of its asymptotic C
is extracted.

The useful distinction is between approximation error for the full
arithmetic expression and the error made by replacing that expression
by its n=1 terms. As time decreases, the n>=2 contributions can become
significant while the fuller approximation remains applicable. Those
contributions then belong in the reference field whose zeros are being
followed. Calling them all small error would preserve the limitation of
the clock argument. Retaining them is already part of Polymath's finite
calculations; the proposed new use concerns the gap-continuation consumer.

## 2. An exact error equation for an explicitly approximated term

Use s for the paper's complex argument and distinguish its carrier
mathfrak M from the exterior interaction M in our manuscript. Define

\[
 \ell_n(s)=\log\mathfrak M_0(s)-s\log n,\qquad
 a=\alpha(s)-\log n,\quad b=\alpha'(s),\quad c=\alpha''(s).
\]

The explicit approximation in Proposition 6.1 is

\[
 p_n(t,s)=\exp\left(\ell_n(s)+\frac t4a(s)^2\right).
\]

The exact term r_n from (39) satisfies
\(\partial_t r_n=\tfrac14\partial_s^2r_n\) on its nonreal-s domain.
Differentiate the explicitly defined p_n, not an O-symbol:

\[
 \frac{\partial_s p_n}{p_n}=a+\frac t2ab,\qquad
 \frac{\partial_s^2p_n}{p_n}
 =\left(a+\frac t2ab\right)^2+b+\frac t2(b^2+ac).
\]

Thus its exact heat defect is

\[
 \mathcal R_n:=\left(\partial_t-\frac14\partial_s^2\right)p_n
 =-\frac{p_n}{4}
 \left[b+t a^2b+\frac t2(b^2+ac)+\frac{t^2}{4}a^2b^2\right].
\]

For delta_n=r_n-p_n,

\[
 \left(\partial_t-\frac14\partial_s^2\right)\delta_n
 =-\mathcal R_n.
\]

This is an elementary derivation for the already published approximant,
not a claim that Polymath states this particular error equation or that
it is new in the literature. [Record06][record] checks the formal jet
algebra with exact rational coefficients. It supplies no bound for the
solution of this equation.

For the physical variables s=(1+iz)/2 or (1-iz)/2, the spatial second
derivative contributes -1/4. Consequently, for a fixed-N analytic
reference field P(t,z), set R=P_t+P_zz and E=H-P. Then

\[
 E_t+E_{zz}=-R,\qquad E_u=E_{zz}+R,\quad u=t_*-t.
\]

Here R is evaluated at t=t*-u in the backward equation. A sum of exact
r_n terms instead has zero heat defect on its valid domain, while its
complete remainder still requires a bound. This makes two different
research interfaces available: retain exact evolved terms and estimate
the remainder, or use their explicit approximations and pay the known
forcing plus the initial error. Neither option discards the exterior.

## 3. What a gap-oriented error calculation could retain

An existing cleared contour Gamma enclosing exactly two occurrences can
read the pair even at a merger. Let A_j=(2pi i)^(-1) integral z^j H_z/H,
c=A_1/2, and D=A_2/2-A_1^2/4. Differentiation using H_t=-H_zz and
integration by parts gives the elementary joint readout

\[
 D_t=\frac1{2\pi i}\oint_\Gamma (z-c)\frac{H_{zz}}H\,dz.
\]

Indeed A_j'=j(2pi i)^(-1) integral z^(j-1) H_zz/H. This is another
form of the existing pair law, not a new collision criterion.
For H=P+E on a contour where both denominators are nonzero,

\[
 \frac{H_{zz}}H-\frac{P_{zz}}P
 =\frac{P E_{zz}-P_{zz}E}{P(P+E)}.
\]

The numerator displays a possible common-error cancellation. For
E=lambda(t)P it vanishes exactly. A bound which estimates its two terms
independently loses that dependence. The actual center c and its error
must also be enclosed. Moreover P_zz/P is a heat readout of P; it is not
the time derivative of P's own zero coordinates unless P_t=-P_zz.
The defect R cannot be omitted in a propagation argument.

This suggests attempting a common contour and time-dependent error
enclosure for the entire numerator, then comparing it with the existing
direct D enclosure using the same information. The [manuscript's §15][jets]
already imports Polymath's spatial-jet idea and cancels the leading common
zero velocity. Its remaining estimates separately bound residual sizes.
Any further gain must identify a dependence that survives the full
quotient and contour calculation. A smaller intermediate residual alone
does not establish that gain.

## 4. Obligations before the error equation becomes useful

- **A common reference domain.** Freeze N on a time/spatial cell or pay
  each cutoff transition. The x,y notation for f_t can be rewritten
  holomorphically using (92); an unadjusted floor-valued N cannot be
  differentiated. The leading C_t correction in (69) is useful for
  value estimates, but its displayed x,y formula is not automatically a
  holomorphic reference for Cauchy estimates.
- **Full data for propagation.** A local heat equation does not propagate
  an error from a bounded interval using initial values there alone.
  Supply the spatial tails or boundary information, growth bounds and
  normalization-dependent coefficients. An exponentially small absolute
  field error need not be small relative to H near a zero.
- **A real improvement at the consumer.** Preserve the whole-time contour
  clearance/count, source remainder, spatial derivatives, initial pair
  margin and all correlations used. The target is a complete bound on
  shrinking over an extended interval, or a demonstrated cost saving at
  fixed coverage. Polymath's finite-sum/derivative route is itself a direct
  comparator, not an unused technique that can be claimed as our novelty.

These are prospective finite quantitative questions. The explicit source
bounds inspected here have positive-time hypotheses; no negative-time
extension is imported. The current manuscript's compact [stopping theorem][compact]
and [two-sided error identity][adjoint] are suitable existing consumers.
This note issues no numerical campaign or main-register task.

## 5. Controls and what the derivation does not establish

The [Discussion06 premise table][screen] screens every Controls12 class
against the unchanged-source use here. Euler-factor, weighted-square,
finite-source/prime, reflected, smooth and positive-primitive controls
fail the specified complete theta source identity; the table retains
their distinct reflection/order premises. Atomic and finite-profile
controls fail the full theta profile; the RH-conditional endpoint
construction changes ordinary Dirichlet arithmetic and has RH as a
premise. Changed observation kernels fail the physical Newman heat law.
Static divisor surgery supplies no common source heat path. No claim is
made that a future coarse numerical bound automatically distinguishes
all these classes.

The generic residual equations themselves admit colliding controls.
Take H=P=z²-2(t-T): E=R=0, yet a double occurs at t=T. Record06 retains
this exact control: starting from t*=1/2 with T=1/4, the integrated
shrinking allowance reaches the initial D exactly at the merger, so the
strict continuation margin fails. A perfect approximation of a colliding
reference must retain its collision. The manuscript's strong-collar
quartic and the remaining applicable controls likewise remain eligible
tests of a generic transfer. Their literal canonical-source premise
fails; small approximation error alone is never promoted to protection.

The outcome is a concrete source-based question with a computable forcing
term. It is not a newly acquired canonical bound or evidence that the
proposed error propagation beats direct source evaluation.

[source]: https://arxiv.org/html/1904.12438v2
[receipt]: ../references/02_HEIGHT_DENSITY_SOURCE_CHECK_20261119.md
[record]: ../numerics/06_POLYMATH_RESIDUAL_ALGEBRA_20261119.json
[jets]: ../../manuscript/sections/13_canonical_time.tex
[compact]: ../../manuscript/sections/15_compact_acquisition.tex
[adjoint]: ../../manuscript/sections/19_two_sided_refinement.tex
[screen]: 06_VCD_GT_CM_RESEARCH_POSITION_AND_PATHS_DISCUSSION_20261118.md
[results]: ../../../../../../../result-summaries/README.md
[cluster]: ../../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[avoid]: ../../../../../../../avoid/README.md
[classification]: ../../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[jointbounds]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md

## Follow-up: upper-bound comparators

The author's requested Platt–Trudgian/Gomila reading is recorded in
[Discussion12](12_VCD_GT_CM_UPPER_BOUND_COMPARATORS_AND_PROGRAM_REFINEMENT_20261119.md).
It adds a concrete prior benchmark: a smaller retained-C remainder did not
directly transfer to the audited triangle lower bound for the uncorrected
sum. The proposed residual experiment must therefore compare complete
margins for the correctly centered approximation, with the actual strip
or gap consumer specified before a campaign begins. This qualification
preserves the exact equations above and claims no new obstruction to
phase-sensitive or correlated estimates. Added 19 November 2026 for
Edward Baker with OpenAI Codex assistance; recorded gpt-6-astra/max.
