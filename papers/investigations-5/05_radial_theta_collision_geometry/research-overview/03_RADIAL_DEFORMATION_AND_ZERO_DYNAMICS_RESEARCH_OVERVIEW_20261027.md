# Research overview for integral preserving collision dynamics

27 October 2026, America/New_York. Updated for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0008. The chat0007 overview and LOC task meanings are retained historically in the progress register; this update records the broader invariant clarified in chat0008. The filename remains stable.

**Historical overview — superseded for current priorities on 28 October 2026 by [Overview04](04_CONSERVATIVE_THETA_FLOW_RESEARCH_OVERVIEW_20261028.md).** The stronger results and earlier LOC meanings below are retained. [Progress04](../research-progress/04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md) is the sole live register; the new program classifies B/E tasks before execution.

**The aim is simple auxiliary dynamics that act directly on the explicit theta sum and make collision degeneracy useful to analyze.** Only the complete observation integral must remain invariant. Its radial density may change, and no spatial direction is prescribed. [Note25][n25] is the current mathematical handoff.

## The invariant and the available freedom

For the canonical theta source,
\[
H(t,a)=\frac18\int_1^\infty r^{3/2}Q_t(r)\cos(a\log r/2)\,dr.
\]
A new representation has a full signed density j_s(t,a;X) with
\[
\boxed{\int_\Omega j_s(t,a;X)\,dX=H(t,a).}
\]
This identity is maintained as a parameter family so that differentiation also preserves the physical jet. An equation
\[
\partial_sj_s+\nabla\cdot J_s=0
\]
preserves the integral when its complete boundary flux is zero. A local or truncated integral retains its actual flux and tail contributions. Radial symmetry, positivity, a fixed operator, a fixed energy, and fixed radial marginals are not imposed on the general search.

Keeping a frequency-independent source and the old cosine testing kernel at every frequency would, by cosine-transform uniqueness, still force its original radial marginal. The weaker requirement therefore permits evolution of the full frequency-dependent density, or joint evolution of source and testing kernel. [Note25][n25] proves this qualification and gives both transport accounting and a completely specified heat example. It is not an obstruction to the weaker invariant.

## Established results and their interpretation

| Construction | Available result | Scope |
| --- | --- | --- |
| Multiplicative concentration and angular transport | Note20 gives normalized profiles, operator and boundary maps, and collision-adapted first moments | Stronger radial-integrand invariant; full details remain in the note |
| Matched steered tube | Note22 includes side and radial boundaries, complements, derivative costs and radial tails | No gain for the fixed-width axisymmetric multiplicative Wronskian comparison; no universal exclusion |
| Projected annular source flow | Note23 proves a unique evolution, explicit coercivity and convergence, dissipation and strict source-cost decrease | Smooth nonnegative freely selected penalty; no collision-specific cost law |
| Exterior response and local adjoint | Note23 specifies the coercive complementary channel, radial joins, physical boundary jets and complete signed variation | Source-cost dissipation does not sign the derived adjoint coupling |
| Explicit theta application | Note24 applies the bounded flow termwise and bounds a finite forcing approximation | Analytic interface, not a numerical theta evolution |
| Conservative full-density heat flow | Note25 gives an explicit Gaussian convolution of the complete theta density, preserving H and its finite spectral derivatives | Changes the radial integrand; no preferred axis or angular projection |
| Collision decay diagnostic | At the spatial origin, H=H_a=0 removes the two leading diffusion coefficients; explicit moment remainders give O(s^(-5/2)) instead of the nonzero component's s^(-3/2) leading order | A generic diagnostic, not growing amplification or a separating theta estimate |

The [manuscript][manuscript] incorporates Notes22–25, with the second approach and the conservative extension developed in Sections10–11 and the first approach referred to its notes. [Review13][review13] assesses the earlier bounded return; [Review14][review14] assesses this integration and its invariant change. All are same-assistant internal assessments, without independent specialist review.

## The next dynamics question

A collision is H(T,a)=H_a(T,a)=0. The desired auxiliary effect could be growth, concentration, or another geometric distinction that follows quantitatively from that degeneracy. It need not aim at a prescribed direction. The ordinary heat example reveals the cancellation by a faster decay of two components; it does not yet supply the proposed stronger magnification mechanism.

The next construction must specify the evolving field, its initial data, observation, parameter derivatives, domain and boundaries, and the precise quantity expected to amplify. A canonical theta estimate controlling that quantity is a separate requirement for an excluding application. Do not stipulate an impossible terminal state or divide by an unknown vanishing spectral value and count the resulting singularity as an estimate.

The local signed functional in Note23 is one defined alternative comparison. Its gradient is known, but its coupling to the source flow is unsigned. That route may be pursued if it helps the current objective; choosing a tube, penalty or direction is no longer the default prerequisite.

## Task meanings and completion criteria

| ID | Current role | Required return |
| --- | --- | --- |
| LOC-01 | Supporting construction of observation-preserving equations | A complete response and derivative map for a defined use; the original radial-preserving examples keep their scope |
| LOC-02 | Complete for the tested fixed-width multiplicative comparison | Change a named hypothesis before repeating the comparison |
| LOC-03 | Bounded projected prototype proved | A useful collision application remains open; its source descent is already established |
| LOC-04 | Canonical estimate, open | A proved quantitative comparison using complete theta information and all associated costs |
| LOC-05 | Later threshold application, open | Adequate time, height, tail and multiplicity coverage |
| LOC-06 | Current conservative dynamics question | Integral-preserving, direction-independent collision amplification with a useful estimate; Note25 supplies only the explicit heat baseline and decay diagnostic so far |

LOC-06 is added to preserve the original LOC-02/03 task identities. The user's weaker invariant supersedes the earlier general requirement; it does not retract the stronger results.

## Controls and the standard for progress

The exact Gaussian-polynomial control and applicable smooth registered controls preserve their collisions under both constructions. In particular, no hypothesis of the generic heat theorem fails for the exact control, and it has the same extra central decay. Controls with altered coefficients/reflection, incomplete arithmetic square sources, or modified Euler factors fail the corresponding full-theta premises, but this has not yet been converted into a separating estimate. Atomic sources lie outside the stated L¹-density formulation.

Use the [result index][results] and [avoid index][avoid], especially [collision controls][controls], [geometric realizations][realizations], [target classification][a01], [transported identities][a03], and [scope rules][a07]. A structural theorem can legitimately apply to controls. An excluding estimate must prove the extra canonical effect on its actual domain. No new de Bruijn–Newman upper bound or all-height simplicity theorem is claimed.

## Records and continuity

The [progress register][progress] owns task status; [current program][current] routes continuation. [Note21][handoff] is the earlier handoff answered by Notes22–23. [Brainstorm03][b03] records the collision-magnification objective and its subsequent invariant relaxation. Earlier Darboux, flux, moment and source-realization notes remain supporting material with their original scope.

Keep one active manuscript and edit its existing source in place. Research derivations belong in notes, assessments in reviews, and justified computations or small build records in numerics. Record actual milestones in DRAFT_HISTORY.md without new snapshot folders. The built-in manuscript preview is the current reading route; historical separate PDFs are identified in the build guide.

[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[progress]: ../research-progress/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROGRESS_20261027.md
[current]: ../CURRENT_RESEARCH_PROGRAM.md
[n25]: ../notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[review13]: ../reviews/13_TUBE_COMPARISON_AND_PROJECTED_FLOW_SELF_ASSESSMENT_20261027.md
[review14]: ../reviews/14_PROJECTED_FLOW_MANUSCRIPT_AND_COLLISION_SCOPE_20261027.md
[handoff]: ../notes/21_RADIAL_INTEGRAND_LOCALIZATION_CONTINUATION_20261027.md
[b03]: ../brainstorm/03_DIRECTION_INDEPENDENT_COLLISION_MAGNIFICATION_20261027.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[realizations]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
