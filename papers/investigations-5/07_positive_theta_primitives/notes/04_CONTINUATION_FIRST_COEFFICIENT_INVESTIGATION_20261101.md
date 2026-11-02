# Continuation: choosing the first coefficient representation

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **xhigh**.

**Recommended next investigation: [B] J-B01 — Astra.** Compare direct
Jensen-polynomial representations with coefficient Toeplitz determinant
representations, and select one concrete transfer problem. This is a
continuation within Investigation07, not a new numbered investigation.
This note prepares the next session; it does not execute J-B01 or select
its mathematical mechanism. Live status remains in the owning registers.

| Next task | Type | Recommended model and reason | Ready or dependency | Expected output |
| --- | --- | --- | --- | --- |
| **Default: J-B01** | B — brainstorm | Astra — choose the representation and identify a plausible source-to-coefficient sign mechanism | Ready for discussion; not started | One bounded comparison and decision note, with a missing estimate and next work contract |
| Alternative: SL-B01 | B — brainstorm | Astra — choose how a complete correlation could acquire positive definiteness | Ready for discussion; not started | One comparison for K_1 or its spectral counterpart, under the existing spectral contract |
| J-E01 | E — execution | Sol — carry out a specified normalization and transfer derivation | Requires J-B01 selection and a fixed request | Exact formula, one classical baseline check and remaining obligations |
| PT-B01 | B — brainstorm | Astra — choose a reusable method for a concrete route need | Requires an actual J or SL tool request | One shared-method contract or a scoped unresolved step |

The [Jensen overview][j-overview] defines J-B01's existing scope.
The [Jensen progress register][j-progress] owns its readiness and return.
The [shared register][base-progress] and [spectral register][sl-progress]
retain their separate task identities. Model recommendations follow the
[repository workflow][workflow]; the author chooses the actual model,
effort and chat.

## Why start here

CNV provides a concrete example of transferring source information to
normalized moment inequalities. The Jacobi differential algebra and
primitive identities give exact relations that might enrich such a
transfer. The coefficient route is therefore a natural first place to
ask what additional information these tools provide after integration.

This is a working priority, consistent with [Note03][formulations],
not evidence that the route will succeed. The unresolved step is the
sign of the complete coefficient expression, with useful dependence on
degree/order and shift/index. Pointwise closure of theta derivatives
does not establish that step.

The [spectral route][sl-overview] remains an independent ready alternative.
It need not wait for Jensen work. Investigation05 supplies techniques
and boundary-accounting lessons; its unfinished collision questions are
not prerequisites for either route.

## Read before continuing

Start with this note, the [Jensen overview][j-overview] and its
[live register][j-progress]. Then read:

1. [Note02: CNV transfer and theta differential closure][closure],
   especially the pointwise differential system, the moment transfer,
   and the gap between source and integrated identities.
2. [Note03: RH formulations and research direction][formulations],
   especially the coefficient normalization, source-concavity diagnostic
   and known parameter ranges.
3. [Note01: literature techniques and inherited tools][foundation],
   using the [reference index][references] and
   [formulation-source record][formulation-sources] to locate primary
   statements actually needed by the comparison.
4. The [overall overview][base-overview], [result index][results] and
   [avoid index][avoid], particularly [theta identities][theta],
   [controls][controls], [reformulations][reformulations],
   [joint estimates][joint] and [unchecked imports][imports].

Read primary theorem statements before relying on their precise
hypotheses. The recent preprints retain the inspection limits already
recorded in the catalog. Repeating their claims in a continuation does
not constitute a proof audit.

## Fixed mathematical objects

Retain the canonical theta source and the half-line normalization
\[
H(z)=\int_0^\infty\Phi(u)\cos(zu)\,du,\qquad
b_n=\int_0^\infty u^{2n}\Phi(u)\,du,\qquad
c_n=\frac{b_n}{(2n)!},\qquad\gamma_n=n!c_n.
\]
The two candidate families are
\[
J_\gamma^{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma_{n+j}X^j,
\qquad
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},
\]
with negative-index c coefficients set to zero.

All-degree Jensen hyperbolicity is the classical RH destination.
For the determinant formulation the complete condition concerns all
finite Toeplitz minors; reducing to selected consecutive minors requires
the appropriate theorem and its hypotheses. Keep c, gamma and raw b
distinct. Positive raw-moment Hankel matrices do not supply the required
coefficient condition.

## The bounded question for J-B01

Compare at most the two representations above. For each, answer:

1. **What is the exact object whose sign or hyperbolicity must be proved?**
   Identify the full integral or determinant expression, its parameter
   domain, factorial normalization and convergence requirements.
2. **Where could theta information enter the argument?** Identify the
   proposed use of Jacobi identities, modular relations or primitive
   integration by parts. State the actual missing implication after
   integration, including any mixed terms or endpoints.
3. **What does the classical baseline already prove?** Separate a
   normalization check from a new estimate. State the quantifiers of
   the relevant fixed-degree, fixed-order or tail theorem. Keep the
   small-shift/increasing-degree and small-index/increasing-order
   regimes visible.
4. **What makes this a tractable next investigation?** Identify one
   concrete lemma or inequality to study, its consumer and its possible
   payoff. If no tractable step emerges, explain the precise obstruction
   or missing input instead of introducing another equivalent criterion.

For the determinant candidate, take particular care with the oscillatory
factor in Katkova's representation: a Vandermonde square alone does not
sign the whole integral. Source derivative-Hankel signs and coefficient
Toeplitz signs require an explicit bridge. The known source-concavity
results should guide that question, not be assumed to extend automatically
to every determinant order.

This selection round may derive enough identities to expose the issue.
A long routine derivation, numerical implementation or broad scan belongs
in a separately specified E request once the mechanism is chosen.

## Required return and stopping point

Save one J-B01 decision note in the Jensen route's notes folder, created
with that first substantive artifact. It should contain:

- The two candidates considered, the selected family and reason for the
  choice, or a scoped account of why neither is ready.
- The complete target expression, declared domain, literature comparison
  and first unresolved sign or uniformity estimate.
- The canonical-theta premise intended to supply additional information.
  For a proposed sufficient claim, apply the relevant [controls][controls]
  to its actual hypotheses and conclusion, identifying each failed
  premise as required by the [control guidance][shape]. Match the
  control's time and parameter domain to the claim.
- A bounded **[E] J-E01 — Sol** request when the analytical route is
  specified: input versions, formulas/lemmas, one classical check,
  permitted routine choices, completion condition and the event requiring
  a return to J-B01. If a shared conceptual step must come first,
  formulate the consuming request for PT-B01 instead.

Stop after that decision and contract, or after documenting the unresolved
choice. Do not silently expand to a third representation, a new flow or
an unrestricted numerical search. A scoped failure completes this bounded
comparison without closing the Jensen program; preserve the class tested,
following [scoped-exclusion guidance][scopes].

No new sufficient estimate is proposed or screened in this continuation.
The source-concavity diagnostic and prior control records retain their
existing scope. There is no new mathematical result or review claim.

## Recording the next session

Reread the live register before work. Mark J-B01 Active when its research
actually begins and save the dated outcome there, preserving other chats'
updates. Put route-specific derivations in Jensen notes, computations in
its numerics folder and assessments in its reviews folder. Reusable tools
and the canonical reference catalog remain at the investigation base.

Follow the [chat-history workflow][chat-workflow]. A genuinely new
Jensen-only chat should be affiliated with the Jensen route. Continuing
this existing cross-route chat retains its current unique base
registration; do not duplicate or relocate it merely because J-B01 is
the next task. Record actual model and effort from the session.

## Pasteable continuation prompt

> Continue Investigation07 in
> /Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/07_positive_theta_primitives.
> Read AGENTS.md and GPT_RESEARCH_MODEL_WORKFLOW.md at the repository root,
> then notes/04_CONTINUATION_FIRST_COEFFICIENT_INVESTIGATION_20261101.md
> and the linked Jensen overview and live progress register.
> Begin [B] J-B01: compare direct Jensen-polynomial and ordinary-coefficient
> Toeplitz determinant representations. Select one concrete transfer
> problem, preserving the canonical source and coefficient normalization.
> Identify the exact expression, domain, literature baseline, theta-specific
> input and missing sign or uniformity estimate. Return one decision note
> and a bounded J-E01 request for Sol, or a concrete PT-B01 shared-tool
> request if that conceptual step must come first. If neither representation
> is ready, record the precise unresolved choice or scoped failure.
> Follow the note's evidence and control requirements, update the owning
> progress register, and stop at that boundary.

[j-overview]: ../01_jensen/research-overview/01_JENSEN_RESEARCH_OVERVIEW_20261101.md
[j-progress]: ../01_jensen/research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[sl-overview]: ../02_spectral_laguerre/research-overview/01_SPECTRAL_LAGUERRE_RESEARCH_OVERVIEW_20261101.md
[sl-progress]: ../02_spectral_laguerre/research-progress/01_SPECTRAL_LAGUERRE_RESEARCH_PROGRESS_20261101.md
[base-overview]: ../research-overview/01_POSITIVE_THETA_PRIMITIVES_RESEARCH_OVERVIEW_20261101.md
[base-progress]: ../research-progress/01_POSITIVE_THETA_PRIMITIVES_RESEARCH_PROGRESS_20261101.md
[closure]: 02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md
[formulations]: 03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md
[foundation]: 01_LITERATURE_TECHNIQUES_AND_RADIAL_INHERITANCE_20261101.md
[references]: ../references/README.md
[formulation-sources]: ../references/04_RH_FORMULATION_SOURCES_20261101.md
[results]: ../../../../result-summaries/README.md
[theta]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[reformulations]: ../../../../avoid/01_restating_the_target.md
[shape]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[joint]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scopes]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[imports]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[chat-workflow]: ../../../../tools/CHAT_HISTORY.md
