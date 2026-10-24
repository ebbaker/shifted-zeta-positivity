# Continue after the fixed-offset contour theorem

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

Read [Note 18](18_RH_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_THEOREM_20261023.md) and [Review 09](../reviews/09_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_REVIEW_20261023.md) first. They complete the concrete question left in [Continuation 17](17_CONTINUATION_CONSERVED_SPATIAL_CONTOURS_20261023.md). This is a proof under initial RH, not numerical support for a conjectured formula. It allows multiplicities and makes no novelty or specialist-validation claim.

**Later manuscript update:** the author subsequently requested promotion and a rewrite of the book, with dated TeX drafts retained. [Note 20](20_THEOREM_CENTERED_BOOK_REVISION_20261023.md) and [Review 10](../reviews/10_THEOREM_CENTERED_BOOK_REVIEW_20261023.md) supersede the manuscript-status statements below; the remaining analytic task is unchanged.

## What is now acquired

For F=H(0,z), p=F'/F, L=log Y, fixed positive spatial offsets and any fixed c>0,

\[
 \frac{H(-s,z)}{F(z)e^{sp(z)^2}}
 =1+s p'(z)(1+2sp(z)^2)+O(L^{-2}),\qquad 0\le s\le c/L^2.
\]

The errors have the same fixed-order spatial derivative bounds on paid smaller strips. RH, the paired product and complete zero count give p and its fixed derivatives O(L). An Euler-region log-derivative anchor initializes p; RH pays its continuation into the strip. The global horizontal ratio exp(integral p) handles every Gaussian tail relative to the complete small F. A separate absolute tail or assumed negative-time floor is not needed.

Nonvanishing, velocity control and a finite-buffer ODE give the actual H dz material lift:

\[
 Z=z_a-sp(z_a)+O(L^{-2}),\qquad
 Z_a=1-sp'(z_a)+O(L^{-2}).
\]

It remains a graph, covers the target interval using explicit initial end extensions, and moves upward as heat time runs backward, with vertical displacement comparable to sL. The continuous tangent angle is controlled. Primitive escape is paid by spatial containment; no global critical-value separation is imposed. See the proof for quantifiers, margins and s=0.

## What the theorem does not distinguish

The positive even superexponential Fourier-source field

\[
 G_0(z)=F(z/2)^2[1+\cos((\log2)z/4)]
\]

has no simple zeros under RH, yet shares the same two coarse zero-count main terms, the logarithmic derivative orders, the exact Gaussian law and every estimate used above. Its source is not the canonical theta source. The proof uses classical complete xi information but does not yet acquire an inequality that fails for this control.

The quadratic model also shows why the formula cannot simply be extended down to offsets beta/L through an allowed double. The earlier nonreal population inside the high outer wall remains unbounded in the needed sense. A regular wall, even with no crossings through it, does not control that population or the full simplicity resource.

## Next substantive task

Use the completed outer wall as an input. Seek either a useful estimate for the complete earlier nonreal resource at s approximately L^-2, or a near-axis comparison retaining the exact local zero/cluster factor. Identify in advance which multiplicity-sensitive observable the estimate controls, and which actual theta arithmetic premise excludes G_0. Pay every carrier derivative, full source error, endpoint term and small-value denominator before invoking the [joint consumer](12_HERMITE_CLUSTER_DOMINATION_AND_JOINT_CONSUMER_20261023.md) or the book's current-limit machinery.

Do not assume a shrinking-strip floor that rules out the very endpoint double under investigation. Do not treat a higher-order fixed-offset expansion or a longer regular-wall time interval as a simplicity gain without a complete consumer. The scale and final theorem remain flexible; numerics support an identified analytic argument only.

[SCF progress](../research-progress/03_CONSERVED_SPATIAL_CONTOURS_PROGRESS_20261023.md) records the fixed-offset parts of SCF-01/02 as completed; their broader scope and SCF-03/04 remain open. [SIMP progress](../research-progress/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRESS_20261023.md) retains the open multiplicity goal. Main.tex still holds the provisional conservation exposition; this round did not alter either manuscript or create a draft snapshot.

Follow the [result index](../../../../../result-summaries/README.md), [local-geometry summary](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../../avoid/README.md), [shared-premise discipline](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), and [coupled-estimate discipline](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The [reference catalog](../../references/README.md) contains inspected classical inputs and external PDF receipts.

This execution chat is **history 0008, Continue contour conservation study**, thread `01a16b52-9407-7e80-8f09-3d5b3303e5b2`, in brainstorm/chat-histories. Preserve its own identity; Note 17's history 0007 belongs to a different chat. At each reply follow [tools/CHAT_HISTORY.md](../../../../../tools/CHAT_HISTORY.md), including the start/end refresh and final bounded exact-turn follow-up. No trusted native completion hook has been verified in this round.
