# Restoring the generalized correlation and marginal objective

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Authenticated chat0003,
thread 01a1bbc2-ac28-71c1-8bf0-aefeb0b06ce8. Actual recorded model and
effort are unavailable. No model change or delegation.

**Status: author-scope clarification and elementary illustrative
construction; no new canonical correlation estimate or proof assessment.**
The author explains that the intended objects were generalized pair
correlation functions, possibly Gaussian-smoothed, obtained by taking
two-zero or higher marginals. That understanding agrees with the earlier
[author ideas](../brainstorm/notes/01_TND_OC_AUTHOR_IDEAS_AND_SELECTION_BOUNDARY_20261107.md)
and [goal alignment](../brainstorm/notes/05_TND_OC_AUTHOR_GOAL_ALIGNMENT_20261108.md).

The completed work became centered on scalar nonreal-pair detectors and
their approximation error. B04 retained a separation-dependent test,
but controlling one tested integral is not developing the full
correlation function. Its transverse weights vanish on every real
configuration, so that particular projection also discards the all-real
spacing information that belongs to the broader objective.

**The generalized marginal program is the primary objective; scalar
defect tests and their approximation theorems are supporting tools.**
The current analytical manuscript records that narrower line coherently.
It is not a completed development of the author's generalized
correlation-function program. Its mathematical statements and their
assessment levels are not retracted by this scope clarification.

## A legitimate Gaussian-smoothed marginal construction

The absence of an established random-matrix law for canonical zeros is
not an obstruction to defining their empirical marginals and smoothing
them. For illustration fix a compact observation region containing
N>=2 labelled zeros z_1,...,z_N, retaining multiplicity copies. This is a
fixed finite configuration, not yet a choice of the full research regime.
For epsilon>0 let the normalized planar Gaussian be

\[
G_\epsilon(u)=\frac{1}{2\pi\epsilon^2}
 \exp\!\left(-\frac{|u|^2}{2\epsilon^2}\right),
\qquad \int_{\mathbb C}G_\epsilon\,dA=1 .
\]

Convolving the symmetrized atomic N-zero law in every coordinate gives
the symmetric probability density

\[
p_{N,\epsilon}(u_1,\ldots,u_N)
=\frac1{N!}\sum_{\sigma\in S_N}
  \prod_{a=1}^N G_\epsilon(u_a-z_{\sigma(a)}).
\tag{1}
\]

Equivalently, permute the labels uniformly and add independent Gaussian
observation errors. This specifies a smoothing law; it does not assert
that the original zeros have independent Gaussian positions.
Every term integrates to one, so (1) is normalized.

For 1<=k<=N, integrating out u_(k+1),...,u_N gives

\[
p^{(k)}_{N,\epsilon}(u_1,\ldots,u_k)
=\frac1{(N)_k}
 \sum_{\substack{j_1,\ldots,j_k\\\text{distinct labels}}}
 \prod_{a=1}^kG_\epsilon(u_a-z_{j_a}),
\qquad (N)_k=\frac{N!}{(N-k)!}.
\tag{2}
\]

Indeed the discarded Gaussian factors integrate to one and each
ordered k-tuple appears in (N-k)! permutations. Thus the smoothed
factorial correlation density is

\[
R_{k,\epsilon}=(N)_k p^{(k)}_{N,\epsilon},
\qquad
R_{2,\epsilon}(u,v)=
\sum_{j\ne k}G_\epsilon(u-z_j)G_\epsilon(v-z_k).
\tag{3}
\]

This is exactly Gaussian convolution of the factorial measure in each
coordinate. It has total mass (N)_k and obeys
integral R_(k,epsilon) dA(u_k) = (N-k+1) R_(k-1,epsilon).
For bounded continuous test functions the measures converge back to
the finite atomic factorial measures as epsilon decreases to zero,
by the Gaussian approximate-identity property term by term. Distinct
labels at a repeated location remain present; no simplicity assumption
has entered.

Equation (3) is a function of two planar locations, retaining four real
coordinates before any projection. For all-real roots it still contains
nontrivial horizontal pair information. Writing G_epsilon(x+iy)
=g_epsilon(x)g_epsilon(y), it becomes

\[
R_{2,\epsilon}(u,v)
=g_\epsilon(\operatorname{Im}u)
 g_\epsilon(\operatorname{Im}v)
\sum_{j\ne k}g_\epsilon(\operatorname{Re}u-x_j)
             g_\epsilon(\operatorname{Re}v-x_k).
\tag{4}
\]

The transverse Gaussian spread in (4) is imposed observation smoothing,
not evidence of nonreal original roots.

This elementary construction makes the author's proposed marginalization
literal. It is a representation, not a new arithmetic estimate,
universal pair law, determinantal formula or RH gain. It also does not
settle which version of localization is most useful. Gaussian
center-window weighting, Gaussian convolution of the measures, and an
assumed Gaussian ensemble are different operations. The first two are
available constructions; the third would require independent justification.
Weighting only the retained coordinates and reweighting the entire
N-coordinate law before marginalization are likewise different.

## Where the substantive research belongs

The next conceptual task should specify the complete correlation object,
then study a source-derived formula, quantitative estimate, limiting
profile, or evolution for it. It must choose horizontal/transverse scales,
the time regime, normalization, and any center averaging or unfolding.
A normalized pair-density ratio, a factorial density, and a
separation distribution should not be identified without their
normalizations and projections.

In particular, smoothing the atomic measure makes a function but does not
by itself predict its shape. A useful canonical estimate must use more
than the unknown zero locations rewritten in (3). The existing E02
logarithm estimate and B04 tensor argument may support such access after
the new tests, boundary treatment and any Gaussian tails have been paid.
Their compact-test error bound cannot simply be declared a theorem for
untruncated Gaussians or moving hard windows.

The next research output is not required to be an immediate one-defect
exclusion criterion. It must retain the full pair/higher object until a
declared projection is needed. A further scalar approximation theorem
alone would leave the present scope problem unresolved.

## Classification, controls, and source use

Read the [result index](../../../../../../result-summaries/README.md)
and [avoid index](../../../../../../avoid/README.md), especially
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
[classification01](../../../../../../avoid/01_restating_the_target.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [volume20](../../../../../../avoid/20_volume_without_a_gain.md).

Equations (1)--(4) are finite marginalization/convolution identities.
No canonical separation mechanism or exclusion estimate is proposed.
Every finite zero configuration obtained from the catalogued controls
also admits this construction. No control fails its mathematical
premises, and no source-specific failure is used to infer a favorable
value. The Euler, weighted-square, reflected, shape/primitive,
finite-prime, atomic/profile, conditional endpoint, altered-observation
and relaxed-profile families retain exactly the canonical-premise
distinctions in [B04 Note05](05_TND_OC_B04_ARITHMETIC_RECONCILIATION_AND_ROUTE_COMPARISON_20261108.md).
The relaxed-profile family additionally needs an integer divisor before
it can be interpreted as a literal labelled zero configuration.

Primary passage reopened on 8 November 2026:
[Borodin, version 1, Section 2, (2.1)](https://arxiv.org/pdf/0911.1153v1),
PDF page 2, defines correlation measures by sums over distinct points and
correlation functions as densities. Its general exposition assumes
simple configurations. Here multiplicity-labelled atoms and their
Gaussian convolution are handled directly by the finite permutation
proof; no simplicity of canonical zeros or determinantal law is imported.
Reuse the canonical parent bibliography entry Borodin2009DPP; no new
article copy, full proof audit or novelty claim is made.

## Disposition

The scope clarification is complete. Proposed next research:
**[B] TND-OC-B05 — specify the full localized pair/higher-marginal program
and its Gaussian smoothing**, recommended Astra because localization,
averaging and the useful source-side comparison remain consequential
choices. B05 is ready for continuation, not executed by this explanatory
answer. E04 and E03 remain pending optional fixed assessments of the
supporting work, with their original inputs and acceptance boundaries.
The [sole register](../research-progress/01_TND_OC_RESEARCH_PROGRESS_20261107.md)
and [Continuation10](../continuation-notes/10_TND_OC_GENERALIZED_MARGINAL_REALIGNMENT_AND_MODEL_CHANGE_20261108.md)
now make that research priority explicit.
