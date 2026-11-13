# Analytical continuation for growing Euler cutoffs and all heights

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Chat0005, “Review Riemann–Siegel
research,” thread `01a1d0f2-d298-7bb0-8216-92b682abb5b2`. The recorded
configuration supplies neither the actual backend model nor reasoning
effort; neither is inferred.

**Current disposition: GNP-RS-B06 is author-selected and pending analytical
execution.** The author requested that the growing-cutoff strategy be
incorporated into the overview and progress register, with emphasis on
analytical routes capable of extending to every height. This note supplies
the continuation. The documentation update is complete; the proposed
growing-cutoff theorem is unproved. No dependent E task is issued here.

The [sole progress register][progress] owns task status. This is the current
GNP-RS continuation, replacing the earlier no-next-task routing after
B05/E06 for this selected strategy. Their completed results and scoped
obstructions remain unchanged. Parent time-zero work and RSCT's separate
positive-threshold problem retain their ownership.

## 1. Read first and preserve the evidence level

Read the [result index][results] and [avoid index][avoid], specifically
[heat-flow cluster11][cluster11], [collision controls12][controls],
[target classification][avoid01], [control premises][avoid02],
[scoped exclusions][avoid07], and [separate signed estimates][avoid12].
Then read, in order:

1. The updated [overview][overview], especially its current strategy section,
   and the [progress register][progress].
2. [Brainstorm Note04][discussion], Sections 3 and 5–7, and the
   [external RSCT comparison][comparison]. These contain proposals, not
   a proof of the growing-cutoff mean.
3. [E05 Note14][e05], Section 2 in full: the fixed-P coefficient expansion,
   diagonal, same-arm pairs, reflected multiplier, complete-field error,
   moving-clock comparison and convolution edges.
4. [E03 Note07][e03] for the underlying uniform oscillatory and fixed-clock
   estimates, and [E01 Note03][e01] for normalization and tails.
5. [E06 Note17][e06], Sections 1–2, for uniform adaptive phase and reference
   costs, and [E07 Note19][e07] for the actual-value mean consequences.
   Their linked assessments retain their stated shared-input/internal scope.

Follow a dependency into the HDA source when its precise constant, chart,
derivative or cutoff assumption is used. The provider is an inherited
theorem with internal review, not a new independently audited input.
Before importing additional external estimates, check their primary
sources and record versions and scope under the repository reference workflow.

## 2. Freeze the canonical objects and the first domain

Keep the complete theta field, clock \(\partial_\lambda H=-H_{zz}\),
carrier \(C_-\), strip \(0<\Im z<8\), observation point \(X+4i\), and
all reflected, gamma, cutoff, correction and remote-tail terms. Write
\[
 L_X=\log(X/(4\pi)),\qquad V_\lambda=H_\lambda/C_-,\qquad
 K(t)=\frac1{16\cosh(\pi t/8)},\qquad
 W_X=[X-(32/\pi)\log X,X+(32/\pi)\log X].
\]
Start with \(c=1\), \(\lambda=1/L_X\). For real \(x\),
\[
 \nu_\lambda(x)=x/2+\pi\lambda/8,\quad
 \phi_\lambda(x)=2\Theta(\lambda,x),\quad
 E_P(x)=\prod_{p\le P}(1-p^{-3/4}e^{i\nu_\lambda(x)\log p})^{-1},
\]
\[
 R_P(X,1)=\int_{W_X}K(x-X)
 \frac{|V_\lambda(x)-E_P(x)-e^{i\phi_\lambda(x)}\overline{E_P(x)}|^2}
 {|E_P(x)|^2}\,dx.                                            \tag{1}
\]
The physical time and cutoff remain fixed inside each spatial integral.
Do not replace that time by \(1/L_x\) without paying the comparison.

The first chosen cutoff is \(P_U=\lfloor L_U^2\rfloor\), constant across
\([U,2U]\). Every estimate must apply to **all real \(U\ge U_0\)**,
with dependencies and finite onset conditions stated analytically.
Sampled heights, a chosen subsequence and unspecified \(O_P\) constants
do not meet this requirement.

This is the initial asymptotic domain, not the complete all-height
objective. The latter includes exceptional centers; the finite initial
range is an explicit separate obligation. Extension to the original
\(c\in[1/2,1]\) band, changing cutoffs within a block, shrinking zero
depth and time zero each require their own uniform argument.

## 3. First quantitative milestone

E05 proves only the fixed-P limit, with
\[
 \mu_P=\zeta(3/2)\prod_{p\le P}(1-p^{-3/2})-1.
\]
The first target is an explicit bound
\[
 \left|\frac1U\int_U^{2U}R_{P_U}(X,1)\,dX-\mu_{P_U}\right|
 \le\varepsilon(U,U,P_U),\qquad
 \varepsilon(U,U,P_U)\longrightarrow0.                       \tag{2}
\]
An error \(O(L_U^{-1})\) is a stronger rate to test, not a promised
answer. Preserve parameter dependence for \(2\le P\le\lfloor L_U^2\rfloor\)
where the proof permits it; report any narrower valid range explicitly.
No growing-P limit follows by substitution into E05's fixed-P estimates.

To retain a route toward every center, carry a translated outer interval
through the calculation rather than hiding its length in \(U\):
\[
 \mathscr R(U,\ell;P):=\frac1\ell
        \int_U^{U+\ell}R_P(X,1)\,dX,\qquad 1\le\ell\le U.      \tag{3}
\]
Seek a bound for \(|\mathscr R(U,\ell;P)-\mu_P|\) with explicit
\(U,\ell,P\) dependence and a proved admissible interval-length range.
The case \(\ell=U\) is the first checkpoint. The initial proof need not
work on all shorter intervals: determining the shortest range on which
its error is useful is a required output, not an assumption. A theorem
uniform over translated long intervals is still an averaged theorem.

Under [avoid01][avoid01], (2) is an **unproved quantitative milestone**.
Its measurable gains are a rate, an admissible cutoff range and an
interval-length range. Merely restating (2) is no progress.

## 4. First analytical route and error accounting

Begin with weighted truncation by integer size, rather than charging the
full reciprocal-product support \(D_P=\prod_{p\le P}p\). At \(c=1\),
\[
 E_P^{-1}=\sum_{d\mid D_P}\mu(d)d^{-3/4}e^{i\nu\log d}.
\]
For fixed \(0<\eta<1/4\), the elementary estimate in Note04 gives
\[
 \sum_{\substack{d\mid D_P\\d>M}}d^{-3/4}
 \le M^{-\eta}\exp(C_\eta P^{1/4+\eta}).                     \tag{4}
\]
The positive expansion of \(E_P\) has an analogous tail bound. For
\(P=O((\log U)^2)\) and \(M=U^\theta\), fixed \(\theta>0\), the
bound is \(U^{-\theta\eta+o(1)}\). Verify it in the receiving proof and
keep its norm and parameter dependencies explicit. It is a truncation
aid, not a canonical sign estimate.

Do not fix a favorable \(\theta\) before the competing errors are known.
Produce one error ledger covering:

| Term | Required analytical payment |
| --- | --- |
| Reciprocal and Euler tails | Bound the discarded terms after multiplication by the complete arithmetic arms, in the norm actually consumed. A small multiplier tail alone is insufficient. |
| Diagonal | Quantify convergence of the heat-weighted coefficients to the P-rough diagonal defining \(\mu_P\), uniformly over the chosen growing range. Replace fixed-index dominated convergence by an explicit tail and finite-part estimate. |
| Same-arm off-diagonal terms | Retain every pair and expose frequency separation, amplitudes, total variation, cutoff jumps, interval endpoints and the loss from division by \(\ell\). |
| Reflected cross terms | Retain the full \(\overline Q/Q\) multiplier for \(Q=E_P^{-1}\); pay its rational-frequency truncation and the derivative/curvature estimates uniformly in the growing parameters. |
| Complete-field correction | Include the exact correction and inherited residual after reference normalization, with the required product or mean-square bounds. |
| Physical clock | Pay the comparison between \(1/L_X\), fixed inside \(W_X\), and any auxiliary \(1/L_x\) used in height integration. |
| Spatial and height edges | Pay the kernel mass, moving window, remote logarithmic tails and every translated interval edge with its \(\ell\) dependence. |

Combine the payments into a written \(\varepsilon(U,\ell,P)\), with
the admissible choices of \(M,\eta\), any multiplier cutoffs, and the
onset conditions. Mean-square estimates may avoid losses caused by
pointwise arm envelopes; justify the consumed norm rather than assuming
that a uniform multiplier tail survives every multiplication.

Retain the actual same-height logarithmic phase trajectory. Averaging
over independently chosen prime phases is not a replacement for the
physical height average. A new auxiliary average requires its own
comparison with (1).

Label each bound as pointwise in height, uniform over translated intervals
but averaged, or valid only after a limiting average. Preserve the uniform
truncation and reference estimates as separate reusable lemmas. A faster
dyadic rate is not worth obscuring the pointwise information or signed
correlations needed for a later argument at every center.

If the first route encounters a structural obstruction, record the exact
failed estimate and the parameter range where it fails. One localized
repair is reasonable; repeated relabeling or a second unrelated research
program is not this continuation's task.

## 5. Required assessment of extension to every height

A successful dyadic theorem is useful but does not complete the author's
objective. The existing transfer, for admissible growing cutoffs, implies
\[
 J_{1/L_X}(X)\le\delta/4+R_P(X,1)/(2\delta^2)+O(L_X^{-1}).      \tag{5}
\]
Since \(\mu_P\le2P^{-1/2}\), (2) would yield
\[
 \frac1U\int_U^{2U}J_{1/L_X}(X)\,dX
 \ll\bigl(2P_U^{-1/2}+\varepsilon(U,U,P_U)\bigr)^{1/3}
       +L_U^{-1}.                                             \tag{6}
\]
In particular, the proposed error \(O(L_U^{-1})\) would give
\(O(L_U^{-1/3})\). Both rate assertions remain conditional on (2).
An isolated spatial contribution can be compatible with such a mean.

The B06 return must assess the following routes without declaring them proved:

- **Localization of the same arithmetic proof.** Determine the actual
  loss as \(\ell\) decreases in (3), and whether any quantitative local
  or maximal estimate is available. Report the first term that prevents
  further localization. Do not infer pointwise control by setting
  \(\ell=1\) in an estimate proved only for long intervals.
- **A direct signed estimate at exceptional centers.** Keep the full
  logarithm and residual/phase correlation if a separate squared-residual
  payment is too large. Failure of an adaptive residual bound would not
  imply a large actual Green value. This is an identified later need,
  not an instruction to repeat the already excluded fixed-P tangent.
- **Space-time persistence if using a mean to exclude defects.** A defect
  must force a quantitatively specified mass on a region covered by the
  proved bound. Along the moving-time curve, wherever differentiable,
  \[
  \frac{d}{dX}J_{1/L_X}(X)=
  \left(\partial_XJ_\lambda(X)-\frac{\partial_\lambda J_\lambda(X)}
  {XL_X^2}\right)_{\lambda=1/L_X}.
  \]
  Spatial smoothing alone does not control the time term near a collision.
  Any persistence width and mass comparison must be proved, with singular
  event times treated separately.

These are the possible bridges to an every-center conclusion. None is
supplied by the mean theorem itself. The fixed-depth consumer remains
\(J_\lambda(X)<m(1/2,1)\); an eventual bound at that depth still leaves
shrinking depth, other times and finite heights. The all-center time-zero
vanishing statement is the RH-equivalent endpoint and is not counted as
an intermediate estimate.

For full-height coverage, record a domain ledger: proved asymptotic region,
finite onset dependencies, bounded-height region remaining, c-range,
depth/radius choices, and any missing overlaps. Prefer analytical coverage
of the remaining region when available. Finite-height certification can
only be a separately justified final component after an analytic estimate
has an actual margin; samples cannot establish a uniform law.

## 6. Controls and acceptance conditions

Before promoting an estimate, apply the [control catalog][controls] and
[avoid02][avoid02] at the controls' recorded witness domains. The analytical
premise screen, inherited from Note04, is:

| Control family | Missing premise in the literal canonical application |
| --- | --- |
| Euler-factor and translated sources | Unchanged coefficients, arithmetic completion and prime subtraction. |
| Weighted squares, finite tails/prefixes and finite-prime orbits | The complete canonical square series together with full reflection; matching finite data is insufficient. Local events need not be all-real thresholds. |
| Reflected super-Gaussian, smooth and positive-primitive sources | Complete theta square-series arithmetic. |
| Atomic, finite-profile and compact continuous thresholds | Full theta profile and canonical high-zero behavior. |
| Conditional endpoint controls | Ordinary Dirichlet arithmetic; their conditional premise remains explicit. |
| Counter-kernels and variable readouts | Literal complete source and/or cosine readout with the physical generator. |
| Relaxed Green profiles | Exact integer zero measure and simultaneous identification with the full boundary field. |
| RSCT calibrated multiplicative models | Actual phase trajectory beyond the calibrated set; no complete Green-window law or canonical global all-real field is supplied. |

The elementary truncation and scalar transfer can hold for eligible
controls. An isolated collision is compatible with a mean theorem.
Consequently, this premise screen is not a claim that every control
violates (2), and no numerical certificate rerun is implied. A future
exclusion must identify a quantitative distinction on the relevant
witness domain, not merely name the canonical source.

A useful B06 return consists of one of:

1. A proved quantitative growing-cutoff estimate, with all terms paid,
   its exact interval-length range and a scoped assessment of the remaining
   every-center gap.
2. A proved intermediate bound with a numerical exponent or explicit
   parameter gain and a precisely identified remaining proof obligation.
3. A scoped obstruction identifying the first failed inequality and its
   parameter dependence, while distinguishing method failure from failure
   of the actual Green bound.

No new mean result is reported as every-center control. No numerical
campaign, source/clock change, sampled-height argument or broader RSCT
event exclusion is part of this first pass. No specialist audit is claimed
for the inherited provider. A dependent E task may be formulated only when
its statement and analytical route are fixed; no E08 is issued by this note.

## 7. Continuation prompt

Continue GNP-RS-B06 from this note. The author selected the growing Euler
cutoff strategy and requires analytical methods with a stated route toward
every height, including exceptional centers. Refresh the registered chat
history first and read the overview, sole progress register, result/avoid
indexes, and the E03/E05/E06 proof sources in Section 1.

Begin the bounded analytical proof attempt for the c=1 residual mean with
P_U=floor(log(U/(4π))²). Keep the cutoff constant on each outer interval
and time fixed inside each spatial integral. Start with weighted truncation
of the reciprocal and Euler expansions, then replace E05's fixed-P limits
by a complete quantitative error ledger. Carry the translated interval
length explicitly, even if the first useful range is only dyadic, and
derive the admissible truncation exponents rather than choosing them from
numerical trials. Retain all reflected cross terms, correction, cutoff
jumps, clock and edge costs. Distinguish the lemmas valid pointwise in
height from those that depend on averaging.

Return a proved bound or the first precise obstruction, with the range
valid for every sufficiently large real starting height. Report how far
the proof localizes, what new input an every-center statement would need,
and the remaining finite-height/time/depth coverage. Do not call a mean
bound a pointwise result or infer one from sampled heights. Preserve the
scopes of the earlier fixed-reference and RSCT control results.

Record new research notes in this investigation's brainstorm folder,
small computations or execution records in numerics if actually needed,
and this chat in its existing chat-histories folder. Record Edward Baker
as intended author, LLM assistance and only model/effort actually available
from the execution record. Update the sole progress register with the
actual result and arrange bounded exact-turn capture of the real final
reply. Do not create manuscript snapshot folders.

[overview]: ../../research-overview/01_GNP_RS_RESEARCH_OVERVIEW_20261110.md
[progress]: ../../research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md
[discussion]: 04_GNP_RS_STATE_OPEN_PROBLEMS_AND_PATHS_20261112.md
[comparison]: ../external/01_RSCT_MANUSCRIPT_COMPARISON_AND_PROPOSED_QUESTIONS_20261112.md
[results]: ../../../../../../result-summaries/README.md
[cluster11]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[avoid01]: ../../../../../../avoid/01_restating_the_target.md
[avoid02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[avoid07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[avoid12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[e01]: ../../notes/03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md
[e03]: ../../notes/07_GNP_RS_E03_COHERENT_JENSEN_OBSTRUCTION_20261111.md
[e05]: ../../notes/14_GNP_RS_E05_FINITE_EULER_RESIDUAL_20261111.md
[e06]: ../../notes/17_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_20261111.md
[e07]: ../../notes/19_GNP_RS_MANUSCRIPT_AND_AVERAGED_GREEN_VALUES_20261111.md
