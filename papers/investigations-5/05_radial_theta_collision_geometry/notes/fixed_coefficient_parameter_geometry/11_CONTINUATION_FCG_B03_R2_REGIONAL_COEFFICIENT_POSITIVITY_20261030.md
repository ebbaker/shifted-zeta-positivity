# Continuation for regional theta noncollapse and coefficient positivity

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **xhigh**, Investigation05 **chat0045**, *Review fixed coefficient research*.

**Default next task: [B] FCG-B03 R2 — Astra. Ready, not started.** Focus the brainstorm on the author's new candidate **FCG-C04 R1 — regional noncollapse from a source-derived coefficient**. Seek one finite coefficient common to a parameter ball, a theorem connecting that coefficient to a uniform energy lower bound, and theta information that proves the coefficient positive. Discovering the coefficient and the theorem is part of the task; neither is an intake requirement.

| Next task | Type | Recommended model and reason | Readiness or dependency | Expected output |
| --- | --- | --- | --- | --- |
| **FCG-B03 R2, focused on C04 R1** | **B — brainstorm** | **Astra:** the coefficient formula, regional estimating mechanism and useful theta identity remain conceptual choices | **Ready; default.** Use this note, Note10 and Progress06 | One explicit mathematical sketch with a precise missing lemma and bounded next step, a complete argument, or a scoped reason the attempted designs remain unsupported |
| FCG-B02, new request revision if needed | B — brainstorm | Astra: develop a retained mechanism whose central design remains unresolved | Only if R2 identifies a useful continuation requiring another conceptual decision | One fixed source-to-bound mechanism and remaining obligations; no automatic extra stage |
| FCG-E01, new packet if justified | E — execution | Sol: perform a specified analytical derivation or finite diagnostic | Coefficient/route, source, ball, finite limits and completion test fixed by B work | Requested proof calculation, diagnostic or scoped failed bound |
| FCG-E02, new assessment revision | E — execution | Sol: check a completed argument and its dependencies | A complete B or E return exists | Accept, correct or reject its stated claims; a complete B argument needs no redundant E01 rederivation |

[Progress06][progress] remains the sole live register. This is a proposed candidate and a focused continuation, not an established certificate or an execution packet. It supersedes [Note09][old] only as the current focus and routing for R2. Its bounded scope, openness to discovering new information, and preservation of earlier evidence remain. No model switch, chat creation, research dispatch or numerical campaign follows from this document.

## 1. The author's regional research question

For p=(T,A), keep the complete theta source and literal cosine,

\[
 H(T,A)=\int_0^\infty e^{Tu^2}\Phi(u)\cos(Au)\,du,
 \qquad J(p)=(H,H_A),\qquad H_T=-H_{AA}.
\]

Use the original drift v(X)=X+X/(1+|X|^2), the full spatial domain R3, and unit Gaussian preparation of the original radial data. With one coefficient c fixed in both physical parameters and auxiliary time,

\[
 \partial_sW_c=L_cW_c,\qquad
 L_c=\Delta+c\operatorname{div}(v\,\cdot),\qquad
 W_c(0;p)=W_0(p),\qquad E_c(s;p)=\|W_c(s;p)\|_2^2.
\]

Choose one closed parameter ball B contained in the prepared-data domain, initially in T>0. The intended target is

\[
 \exists\ c_B\in(0,\infty),\ \delta_B>0,\ S_B\in[0,\infty):
 \quad E_{c_B}(s;p)\ge\delta_B
 \quad\text{for every }p\in B\text{ and }s\ge S_B.
 \tag{1}
\]

All constants serve the entire ball. A late-time result suffices for collision exclusion; an all-time version may include the finite initial interval. No parameter-dependent coefficient c(p), energy conservation law, or exact stationary energy matching is required. The stationary matching coefficient discussed in Note10 is a separate diagnostic, not C04's proposed definition.

The first pass chooses one symbolic ball with explicit center/radius conditions or one concrete ball, recording its selection before testing the proposed estimate. The inherited K*=[1/8,3/8]x[4,45] and c=1 remain the C01 comparison baseline, not a mandatory new exclusion domain or a replacement for choosing B. Do not choose B solely by assuming its interior jet is nonzero. No cover, height scan or extension to an RH-related domain is part of this pass.

## 2. Why this differs from nonlinear feedback control

The same linear propagator acts across B. In particular,

\[
 \partial_s\partial_p^\nu W_c=L_c\partial_p^\nu W_c,
 \qquad U_{c,T}=-U_{c,AA}.
\]

There is one common spatial overlap kernel in the complete-source bilinear expressions. These structures permit joint estimates in physical parameters and use of theta identities across the ball. Differentiating the nonlinear feedback family instead introduces derivatives of its mark-dependent feedback coefficient. Bounding that nonlinear trajectory and choosing a pointwise stationary matching coefficient are distinct analytical tasks.

Regional noncollapse is logically equivalent to nonvanishing of J on compact B under the inherited convergence hypotheses. This classifies (1) as a reformulation; it does not establish equal proof difficulty or erase the different tools of the regional formulation. A source-derived proof of (1) would be useful even though its converse follows immediately from compactness. The question is whether the common family makes a theta estimate accessible, not whether another collision diagnostic can be renamed.

## 3. Available collision and coefficient sign information

Read [Note10][clarification], especially Sections 4, 7 and 8, together with its [fixed-flow][fixed] and [parameter-family][family] inputs. Their derivations have same-assistant checking only. E02 did not assess Note10 or the entirety of those inherited arguments; assess whatever a future claim actually imports.

For each positive fixed c,

\[
 W_c(s;p)\longrightarrow J(p)p_c,\qquad
 p_c=Z(c)^{-1}e^{-c\mathcal V},\quad
 \mathcal V=\tfrac12(|X|^2+\log(1+|X|^2)),
\]

with compact-uniform L2 convergence and fixed parameter-derivative estimates. Thus E_c tends to Q(c)|J|^2, Q(c)=||p_c||_2^2>0. At any collision J(p0)=0 in B, E_c(s;p0) tends to zero for every finite c>0, defeating (1). This implication does not require the collision to be an isolated nondegenerate double. Note10's quadratic local energy minimum and coefficient-matching exponent do require that extra hypothesis; do not extend those formulas to higher multiplicity.

For the other signs, the same fixed equation remains regular but cannot support noncollapse:

\[
 c=0:\quad E_c(s;p)\le(8\pi s)^{-3/2}\|W_0(p)\|_1^2\to0,
\]
\[
 c<0:\quad E_c'\le3cE_c,\qquad
 E_c(s;p)\le E_c(0;p)e^{3cs}\to0.
\]

These estimates are uniform on compact B and hold whether or not J vanishes. The negative sign reverses the comparison using div v>=3. For c<=0 the expression exp(-cV) is not integrable, so the normalized stationary density and positive-c partition-function formulas are unavailable.

Positive c is therefore necessary for (1), but its positivity alone is insufficient. Choosing c=1 gives no source discrimination. Generic smoothness, finite moments, positivity of the scalar carrier and fixed-flow upper boundedness also hold at admitted collisions.

## 4. Candidate C04 R1 and the three design obligations

Seek a finite real expression

\[
 c_B=\mathfrak c[\Phi,\text{literal cosine};B]
 \tag{2}
\]

that has a useful analytical form and is common to B. The notation does not define a formula or assert its existence. Fixed auxiliary choices may enter, but must be disclosed and remain common to the ball. The candidate is the following research design:

1. **Coefficient construction.** Identify the actual functional or relation in (2), the full source information it uses and what makes it well-defined. Prefer a real formula whose sign can be investigated without already assuming c_B>0 or min_B|J|>0.
2. **Regional implication.** Derive, or formulate as a precise missing lemma, a source-dependent theorem showing that positivity of this specific c_B gives (1), with all other hypotheses independently supplied. The connection might arise from a multiplier, a joint parameter identity, or a correlated energy estimate; no one of these is preselected. If the theorem also contains an unresolved signed margin, exhibit it rather than claiming that c_B's sign is the only remaining difficulty.
3. **Theta positivity.** Determine which complete theta relation could establish c_B>0, and whether that sign problem is more tractable than direct estimation of J on B or C01's signed curvature expression. Positivity may remain the main open lemma, provided its formula and a bounded test are concrete.

The conditional implication and positivity proof may be developed in either order or together. An unproved but explicit, falsifiable lemma is an acceptable B output. Neither a proved sign estimate nor a completed conditional theorem is required to begin the brainstorm.

Do not define c_B through an assumed positive minimum of |J|, through the pointwise stationary matching coefficient, or by an unknown positive lower energy bound. A displayed source integral is not automatically easier merely because it has a new name. Conversely, logical equivalence to regional nonvanishing is not an objection to a genuinely different method of estimating it.

The ball and the coefficient are part of the conceptual design. Keep changes to the equation, drift, preparation, literal observation or domain explicit; a proposal that needs such a change must state its consequences rather than inherit earlier conclusions silently.

## 5. Bounded comparison and control screen

Focus this R2 pass on C04. Keep **C01 as the one other candidate track for comparison**. Consider at most three concrete mechanism sketches in total, for example one or two C04 constructions and at most one substantive C01 mechanism. Do not fill the slots to reach three. C02, C03 and the inherited CTF integrated-feedback question retain their earlier statuses and are not additional substantive branches in this focused pass.

For each serious sketch, identify the coefficient or mathematical object, the theta input, the proposed regional implication, the missing sign/quantitative estimate, a reason it might help, and one bounded analytical way to support or falsify it. Compare with direct analysis using identical source information. Distinguish a parameter-boundary estimate or averaged energy bound from the pointwise-in-p lower bound in (1); an isolated interior zero can coexist with both.

Use the [control register][controls], keeping actual domains and failed premises:

| Control | Required comparison |
| --- | --- |
| Gaussian-polynomial source, event (1/4,2 sqrt(6)) | Its moment domain includes a small ball around the event, and its fixed flow decays at the center. It fails the full arithmetic theta source relation. A proposed coefficient/sign theorem relying only on its shared positivity, regularity and moments fails this screen. |
| Three positive square weights, certified event T=1/4, A in (44.1303,44.1304) | Use a suitable ball around its own event. It shares square support and preparation but fails unit theta coefficients/full reflection. Determine whether the coefficient becomes nonpositive or which additional theorem hypothesis fails. Do not assign theta's full Poisson identity to this source. |
| Other registered reflected, primitive-compatible or finite-information controls | Use when the sketch consumes their shared properties. Name the actual failed arithmetic, literal-observation or other premise; unresolved applicability remains explicit. |

No theorem should declare c_B positive for a colliding control while all hypotheses of its regional implication also hold. A control failure can occur in the sign or in an additional named premise; do not demand a universal sign rule for sources outside the theorem. Existing certified events need not be numerically replayed merely to state this analytical screen.

Retain all spatial exteriors, initial-ball contributions, parameter/spatial boundary terms and derivative terms introduced by the sketch. A bound at preparation alone needs a propagation or late-time argument. A source-dependent positive margin must pay the actual complete remainder.

## 6. Preserve the earlier findings

Read [B01][b01], [B02][b02], [E02][review] and [Note07][decision] as needed for the chosen source mechanism. E02 accepted B02's six fixed obligations without correction. The individual-mode absolute budget has epsilon log A_epsilon -> T^2 at B0 and Q(1); the undamped zero mode has infinite positive part on the prepared cone. Separate absolute payment of the exterior loses a precisely identified positive quantity. These are scoped failures of the tested method and endpoints.

Note07's complete dual-series regrouping restores integrability after summation and returns the original source product, without a signed estimate. It was not assessed by E02. Neither result excludes every signed grouping, fixed-window certificate or correlated remainder. Do not restart the failed separate-bound calculation with more precision or silently claim that C04 escapes it solely by changing the target name.

C01's limiting target remains Q(c)(H_A^2-HH_AA+C(H^2+H_A^2)). C04's limiting energy is Q(c)|J|^2. The comparison should explain what new source relation or propagation estimate the chosen formulation makes usable. An explicit obstruction or a clear missing lemma is a valid bounded outcome; it is not a conclusion that the entire investigation is exhausted.

## 7. Completion and continuation

Return one short comparison and one disposition:

- **Retain or revise C04:** provide a concrete coefficient construction or mechanism, its proposed regional theorem, the exact unresolved sign/estimate, a control assessment, why it may improve the direct task and one bounded next step.
- **Select C01 instead:** explain the specific analytical advantage found in this limited comparison and give its missing lemma and next step.
- **No supported mechanism in this pass:** identify exactly where the attempted constructions fail or remain undefined, preserving their scopes and the broader open problem.

Keep unresolved design as B work. When the method, input, ball, finite work limits and completion test are fixed, issue FCG-E01/Sol; a completed argument can go directly to FCG-E02/Sol. No simulations or parameter scans are authorized by this planning note. A fixed numerical diagnostic requires an execution packet specifying its cases, errors, precision/cutoff/refinement ceilings and stop rule.

Save the return in this notes folder, computations in the investigation's numerics folder and assessments in reviews. Update only Progress06 for live status. This planning document registers a candidate and sets the next focus; it is not a scientific milestone and does not warrant manuscript, result-summary or DRAFT_HISTORY promotion.

## 8. Chat continuity and pasteable prompt

This continuation was prepared in **chat0045**, thread `01a18cf3-0c8c-7ff3-83a8-9cb6bde9823a`, [public archive][history], actual **gpt-6-astra / xhigh**. Preserve its existing registration if continuing in place. Chat0043 owns the earlier B01–B03 return and Note09; chat0044 owns the separate E02 assessment. A genuinely new research chat receives its own Investigation05 registration. Do not merge those histories or infer specialist independence from a model change. Use the [official recorder][capture] at the start and end of replies, with bounded exact-turn final capture until native hooks are verified active.

> Read Progress06 and Note11 in notes/fixed_coefficient_parameter_geometry, then Note10 and the relevant inherited source/assessment files. Begin **[B] FCG-B03 R2 — Astra**, focused on **FCG-C04 R1: regional noncollapse from a source-derived coefficient**. Seek one finite coefficient c_B common to a closed parameter ball, a source-dependent theorem connecting its positivity to a uniform positive energy lower bound, and complete theta information that can prove its sign. The formula, implication and positivity mechanism are things to discover, not intake requirements. Preserve the regional formulation as analytically distinct from nonlinear feedback control and pointwise energy matching. Keep the complete source, literal cosine, original drift and unit preparation. The c<=0 decay laws and positive-c collision decay are inputs, not a positivity certificate. Compare C04 with C01 only, using at most three concrete mechanism sketches in total. Retain complete remainders, name the control premises, and compare direct analysis on identical source information. Return one credible lead with a precise missing lemma and bounded next step, a complete argument, or a scoped unsupported outcome. Issue Sol execution only after the route and completion test are fixed. Save the return, update Progress06 and preserve actual chat/model/effort identity.

[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[old]: 09_CONTINUATION_FCG_B03_R2_BRAINSTORM_20261030.md
[clarification]: 10_FIXED_FLOW_BOUNDEDNESS_AND_LOCAL_COLLISION_GEOMETRY_20261030.md
[fixed]: ../CHAT0042_FIXED_COMPRESSION_AND_NORMALIZATION_COMPARISON_20261030.md
[family]: ../CHAT0042_FIXED_FLOW_PARAMETER_FAMILY_AND_COLLISION_INDEX_20261030.md
[b01]: 01_COLLISION_SIGNATURE_COMPARISON_20261030.md
[b02]: 03_POISSON_LOCALIZATION_AND_RELATIVE_LOSS_B02_20261030.md
[review]: ../../reviews/fixed_coefficient_parameter_geometry/01_FCG_E02_R1_POISSON_LOCALIZATION_ASSESSMENT_20261030.md
[decision]: 07_C01_DISPOSITION_AFTER_E02_20261030.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[history]: ../../chat-histories/0045_2026-10-30T13-15-01Z_review-fixed-coefficient-research.json
[capture]: ../../../../../tools/CHAT_HISTORY.md

Follow the [model workflow](../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md), [result index](../../../../../result-summaries/README.md) and [theta-identity cluster](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), together with the [avoid index](../../../../../avoid/README.md), especially [target reformulations](../../../../../avoid/01_restating_the_target.md), [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [separate bounds](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [circular constants](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md).
