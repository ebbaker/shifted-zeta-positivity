# Vafa–Witten continuation and overall brainstorm addendum

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; conceptual author/coordinator **gpt-6-astra / ultra**, separate checking **gpt-6.1-sol / ultra**. Internal LLM review with shared primary sources, not independent specialist review.

**The earlier failure was local. The requested continuation now yields an exact physical RH reformulation, while leaving the Mellin inequality open.** [Return02](../07_donaldson_witten_theory/notes/02_POINT_INSERTIONS_AND_VAFA_WITTEN_ANOMALY_RETURN_20261101.md) and [Review02](../07_donaldson_witten_theory/reviews/02_MC07_E02_SEPARATE_REVIEW_20261101.md) contain the bounded assessment and separate checking. Review disposition: accepted at stated scope, without correction.

| Next task | Type | Recommended model | Readiness | Output |
| --- | --- | --- | --- | --- |
| **MC07-B03: one boundary-response mechanism** | B — conceptual | Astra; independent sign information is still missing | Ready for a future authorized continuation, unstarted | One Ward-identity route applied to the complete signed insertion, or its exact uncontrolled term |
| J-B10 overall planning, alternative | B — conceptual | Astra | Ready with Continuation07 and Addenda08–09 | Compare this physical route with MC03's analytical localization and MC05's oscillator route; choose one priority |

## What failed, and how far that failure reaches

The first Donaldson assessment tested one complete protected surface correlator on the complex projective plane. Its degree rule forced a zero Taylor coefficient where theta has a positive one. It did not exclude Donaldson theory or topological field theory as a whole.

Adding a point observable repairs that first missing coefficient. The continuation then finds an exact relation between two later coefficients that prevents the match even with complex rescalings. The same relation excludes every finite odd polynomial of point insertions added to the identity, within the same manifold, bundle and parameter dictionary. Higher even point powers, other source choices and other theories remain outside the proof. This is a larger, precisely stated family within one theory.

## What works in the related theory

The successful candidate changes to the Vafa–Witten twist of N=4 SO(3) gauge theory on CP2. The published completed partition function has a holomorphic anomaly: a dependence on the conjugate coupling that survives because field space is noncompact. A boundary contribution produces exactly the full integer-square theta sum after specified normalization. The primary source is [Dabholkar–Putrov–Witten, 2020](https://arxiv.org/pdf/2004.14387v3).

Let A(beta) denote that normalized response. The return proves A(beta)=Theta(beta) for every beta>0, with beta=8 pi/g² at zero Yang–Mills angle. The explicitly completed Mellin transform of A(beta)-1 is exactly xi(s). Consequently RH becomes a statement that all zeros of this anomaly Mellin period lie on Re(s)=1/2. This is a nonlocal transform over coupling, not an equality between xi and an ordinary local protected correlator. Its normalization is fixed by the explicit mathematical completion; the cited physical derivation has the sign and measure caveats recorded in Return02.

This advances the author's physical-reformulation goal beyond the earlier theta factor inside a modular integrand. It identifies a specific theory, sector, completed response and full transform. The construction uses known anomaly and theta identities; no historical novelty claim is made.

## What does not follow, and the next useful question

The complete canonical source is recovered by differentiating the whole normalized response. Every mode, both signed source terms and the negative region of the determinant insertion h3 are retained. No new bound on the full Mellin curvature, including its two covariance terms, follows. The added proved comparison domain is empty.

The anomaly derivative also annihilates the holomorphic class-number series. Its counting data have therefore supplied no extra inequality through this extraction. Physical source identification alone does not establish the desired comparison. This is the specific issue that makes MC07-B03 a conceptual task rather than routine execution.

**Default next task:** inspect at most two boundary Ward identities, select one, and determine whether it supplies information about the unchanged signed insertion beyond the theta identity itself. Return a justified term or bound on a stated domain, or the surviving uncontrolled contribution. Reproducing theta or renaming the desired comparison completes that attempt as a scoped failure. No numerical work is ready until such a return fixes a separate E contract. The [local plan](../07_donaldson_witten_theory/research-plan/01_DONALDSON_WITTEN_ASSESSMENT_PLAN_20261101.md) and [sole MC07 register](../07_donaldson_witten_theory/research-progress/01_DONALDSON_WITTEN_RESEARCH_PROGRESS_20261101.md) own this scope and readiness.

For the overall brainstorm, retain two success criteria: new analytical information for Mellin comparison, and a useful physical reformulation. The present continuation succeeds at the latter only. The earlier six assessments and [Continuation07](07_CONTINUATION_OVERALL_PHYSICS_BRAINSTORM_20261101.md) remain frozen. [Addendum08](08_DONALDSON_WITTEN_ASSESSMENT_AND_BRAINSTORM_ADDENDUM_20261101.md)'s unassessed point-insertion alternatives and no-B02 launch statement describe the earlier stage; the author's later request authorized this bounded continuation. The next unused parent note number is now provisionally **10**.

Use the [result index](../../../../../../result-summaries/README.md), [theta results](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [avoid index](../../../../../../avoid/README.md), [reformulation rule](../../../../../../avoid/01_restating_the_target.md) and [scoped-exclusion rule](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). Return02 names which exact-source premise each relevant collision control fails; no inequality has been claimed to pass those controls. [Source record](../../../references/09_VAFA_WITTEN_CONTINUATION_SOURCES_20261101.md) and [completion record](../07_donaldson_witten_theory/numerics/MC07_B02_COMPLETION_RECORD_20261102.json) preserve provenance.

Pasteable continuation:

> Read MC07 Return02, Review02, this Addendum09, and the local overview, plan and sole progress register. Execute [B] MC07-B03 within its two-identity/one-worked-route limit. Keep the complete normalized anomaly, signed theta source and h3. Identify a boundary Ward identity that supplies new information for the complete Mellin response, or return its exact uncontrolled term. Distinguish an independent bound from an RH-equivalent reformulation. Do not start numerics or expand the theory search. Freeze the result and specify separate E checking.

**Next: [B] MC07-B03 — Astra**, one bounded boundary-response assessment.
