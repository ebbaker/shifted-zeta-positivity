# Continuation: identify collision signatures for the fixed-coefficient family

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **xhigh**. Investigation05 chat0042, *Clarify signed cross-production questions*.

| Next task | Type | Recommended model and reason | Ready or dependency | Expected output |
| --- | --- | --- | --- | --- |
| **Default: FCG-B01 — collision signatures and shortlist** | **B — brainstorm** | **Astra:** the useful collision behavior, geometric object, and preliminary theta connection remain conceptual choices | **Ready; not started at issue.** Re-read Progress06 before beginning | At most three defined leads, their collision implications and theta connections, and one ranked choice or a precise reason no lead is justified |

This is a dated continuation guide, not a research return or a second status register. [Progress06](../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md) alone owns live status. The author chooses the model, effort, and chat; this note dispatches no work.

## Where the discussion stands

[Overview06](../../research-overview/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_OVERVIEW_20261030.md) now contains both the explanatory background and the research plan. It covers the physical jet and carrier, normalized-flow breakdown and its positive-mass dependency, the fixed-coefficient alternative, parameter dependence, curvature and other possible signatures, and the distinction between a criterion and a theta-specific estimate.

The intended cycle is **propose a collision signature → connect it to theta information → test → assess → refine, retain, or retire**. Develop one candidate at a time and test its source connection early. Do not build a general geometric theory before identifying what theta information might make it useful.

No property X has been selected, no candidate ID registered, and no execution packet issued. The fixed-flow comparison and family constructions in chat0042 are same-assistant derivations, not independently assessed theta exclusion results. Progress05 is historical; its unfinished CTF tasks are preserved in Progress06's crosswalk. The old integrated signed-feedback question remains an available alternative under its original constraints, not the default next task.

## The author's potential regional argument

Use the actual physical jet

\[
J(T,A)=(H(T,A),H_A(T,A)),\qquad H_T=-H_{AA}.
\]

Let \(K\) be a compact convex region with nonempty interior contained in \(\{T>0\}\), such as a small closed disk around a physical mark. One possible target is a property \(\mathsf X(K,c)\) for which

\[
J\ne0\text{ everywhere on }K
\quad\Longleftrightarrow\quad
\exists\,0<c_K<\infty:\mathsf X(K,c_K).
\]

For contradiction, the essential half is

\[
\exists p\in K:J(p)=0
\quad\Longrightarrow\quad
\forall\,0<c<\infty:\neg\mathsf X(K,c).
\]

The separate theta-specific theorem would establish

\[
\forall\text{ such }K,\quad
\exists\,0<c_K<\infty:\mathsf X_\theta(K,c_K).
\]

One coefficient must work throughout K and remain constant in auxiliary time; different regions may use different coefficients. The property specifies its own time range or limiting regime. No global constant over the whole positive-time plane is required. The converse characterization is desirable but not necessary for exclusion.

Compactness makes continuous nonvanishing on the entire region, including its boundary, a positive uniform margin. Bounded open regions need not have that property. Convexity is a potentially useful geometry, not a noncollision argument. A proof covering only double collisions must retain that scope; endpoints, higher multiplicity, and any RH transfer remain separate.

This is a potential logical template, not a requirement that the signature use boundary data. Curvature, loss of rank, parameter sensitivity, normalized geometry, asymptotic modes, and topology remain eligible. Define the object precisely before assigning it a collision behavior. A Hessian, curve curvature, metric curvature, and winding are different quantities.

The [regional subsection](../../research-overview/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_OVERVIEW_20261030.md#potential-path-one-finite-coefficient-on-each-compact-region) gives the illustrative stationary property

\[
|J(p)|^2Q(c)\ge E_0(p)\quad(p\in K),
\qquad Q(c)=\|p_c\|_2^2\to\infty.
\]

It has the desired equivalence by compactness and the fixed-flow limit \(W_c\to Jp_c\). It is explicitly a reformulation. Using \(\min_K|J|>0\) to prove its theta side would assume the conclusion. Fixed-coefficient regularity alone cannot be X: colliding controls also have regular fixed flows and decay to zero. No transient energy conservation is imposed on the fixed-c equation.

## The bounded FCG-B01 return

Follow the [existing task contract](../../research-overview/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_OVERVIEW_20261030.md#fcg-b01-collision-signatures-and-shortlist). Produce one concise comparison note with at most three leads. For each:

1. Define the observable or geometric object, normalization, collision class, regional quantifiers, and auxiliary-time regime. State what a collision forces, with a short derivation or precise source; label any unproved implication conditional.
2. Name a preliminary complete-theta identity or estimate that might forbid that behavior. State the needed gain and the first bounded test. Do not treat source uniqueness or a formal identity as proof of the consumed inequality.
3. Explain the required passage from preparation to positive auxiliary time or the limit, including parameter uniformity. Keep any physical-mass assumption visible. Distinguish actual collision geometry from a singularity created by normalization.
4. Record relevant admitted control behavior and the claimed source distinction. Start from the prepared Gaussian-polynomial and weighted-square events at their actual marks; consult the wider control register for the proposed premises. A shared signature is expected. A colliding control sharing every excluding premise defeats the argument.

Rank one lead for further development, or give a scoped explanation that none is justified. The first round is limited to candidate selection and the local calculations needed for that decision. No numerical implementation, broad parameter scan, new PDE, full spectral theory, or general curvature classification is part of this task. The original drift, complete source, and unit preparation remain the starting family.

If selecting the source-to-signature argument still requires a conceptual choice, recommend **[B] FCG-B02 — Astra**. If the objective, method, inputs, finite limits, and acceptance test are already fixed, issue **[E] FCG-E01 — Sol** immediately. A complete argument may go directly to **[E] FCG-E02 — Sol** for assessment, without redundant execution. A precise obstruction can instead go to B03 for disposition. No candidate is retained merely because it has acquired a new notation.

## Sources, files, and continuity

Read the current Progress06 and Overview06 first, then the relevant precursor material:

- [Fixed compression and normalization](../CHAT0042_FIXED_COMPRESSION_AND_NORMALIZATION_COMPARISON_20261030.md).
- [Parameter families and collision indices](../CHAT0042_FIXED_FLOW_PARAMETER_FAMILY_AND_COLLISION_INDEX_20261030.md).
- [Auxiliary-evolution strategy assessment](../../reviews/CHAT0042_AUXILIARY_EVOLUTION_STRATEGY_ASSESSMENT_20261029.md), when using the normalized-flow comparison.
- [GPT_RESEARCH_MODEL_WORKFLOW](../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md), the [result index](../../../../../result-summaries/README.md), [local geometry](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), and [control register](../../../../../result-summaries/12_collision_controls_and_screening.md).
- The [avoid index](../../../../../avoid/README.md), especially [target reformulations](../../../../../avoid/01_restating_the_target.md), [control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scoped failures](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [circular assumptions](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md).

Use the primary linked proofs when a specific claim is needed. R16's unsigned closure failure and R17's prepared pointwise cross-sign failure retain their narrow scopes; neither rules out integrated cancellation or this broader family investigation. The preceding background supplies their references, so a full replay is not required for every candidate.

Save the return in this notes subfolder under its next unused filename, with actual model/effort, date, and evidence status. Record any candidate IDs and disposition in Progress06, update this folder's index, and preserve issued requests and failed evidence. Do not start a new manuscript or modify old proof sources merely to document the shortlist.

Maintain the standing chat-history workflow. Continuing this chat preserves its existing Investigation05 chat0042 registration. A genuinely new chat uses its own actual identity in Investigation05's chat-histories; it must not reuse or relocate chat0042's identity.

## Pasteable next-session prompt

> Read GPT_RESEARCH_MODEL_WORKFLOW.md, Progress06, Overview06, and the continuation note at notes/fixed_coefficient_parameter_geometry/01_CONTINUATION_FCG_B01_20261030.md in Investigation05. Complete **[B] FCG-B01 — collision signatures and shortlist**, recommended Astra. Compare at most three precisely defined collision behaviors, each with a derivation or explicit gap and a preliminary theta-specific connection. Include the author's potential compact-region formulation: a collision obstructs property X for every finite c, while theta information would establish some c_K shared across the region and constant in auxiliary time. Different compact regions may use different constants. Keep curvature, degeneracy, parameter sensitivity, asymptotic modes, and topology open; do not default to boundary information or select the stationary-energy reformulation merely because its equivalence is known. Screen the admitted controls, retain multiplicity and propagation dependencies, and rank one lead for an early source test, or explain why none is justified. Return one bounded comparison note and the next B02 decision or fixed E01/Sol contract, then stop at that boundary. No numerical implementation or extended general theory. Update Progress06 and preserve the appropriate chat-history identity.
