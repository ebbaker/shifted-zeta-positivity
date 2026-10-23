# Pair spectrum and curved contour research progress

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Mathematical status checked by a separate same-model agent; no specialist review.

**Current position:** the analytical program, exact evolution identities and finite simplicity-transfer mechanisms are recorded. The next substantive task is to obtain a useful bound from the complete theta source. No new theta spectral upper bound, improved simplicity proportion or all-simple theorem has been established.

This is a dated progress snapshot for the [new analytical overview][overview]. The [existing progress register][ledger] remains the sole mutable owner of HDC task statuses. This note records what is ready to use, what remains unproved and where the next analytical note should begin; it does not create a second task ledger.

## Objective and current priorities

The primary application is **RH implies simple zeros**. The intermediate global milestone is **RH implies almost all zeros simple**. Curved-contour transport and backward use of long-time data are methods to investigate toward those targets. An eventual application to RH remains separate, with the RH-dependent inputs explicitly identified.

HDC-07, complete source control of the filtered pair spectrum, is next. HDC-08 may develop curved-contour geometry in parallel. Backward propagation, growing-height upper estimates and conditional theorem assembly remain planned or dependent on those estimates. Numerics support analytical proofs and sharp controls; a broad numerical campaign is not the next task.

## Foundations already recorded

| Foundation | Established scope | Main source |
| --- | --- | --- |
| Complete finite physical-cap geometry and expression | HDC-01 is a specification; HDC-02 is a conditional exact expression retaining the complement, analytic factor and connecting faces. | [Notes 02–03][notes] and [Review 01][review1] |
| One-sided use of pair statistics | A truncated positive real pair lower bound can contribute to a cap lower bound. It does not pay the transverse or complementary terms. | [Note 04][n4] |
| Earlier-time density-one transfer | For a complete isolated population with real endpoint roots, M_0<=3 N_nr(a)/2. A near-zero upper bound for the complete projected-pair measure can therefore imply density-one simplicity. | [Note 05][n5] |
| Pair-spectrum simplicity transfer | Under RH and complete tracked endpoint populations, the matching argument gives M_0<=6q(t), with q(t)=Tr[4tL(I+4tL)^−1]. | [Note 06][n6] and [Review 02][review2] |
| Source, contour and backward identities | The complete force can be represented on a zero-free spatial wall; filtered evolution retains L+tL'; common-time moving-wall transport and the signed backward error identity are explicit. | [Overview 02][overview] and [Review 03][review3] |

These are identities and conditional transfers with their stated domains. They do not supply the missing theta upper estimate. The earlier fixed-band physical-cap acquisition remains open as a parallel branch, with no demonstrated theta comparison advantage.

## The quantitative distinction between the two simplicity targets

For a complete finite endpoint population and its positive-time descendants, put

\[
 R(t)=(I+4tL(t))^{-1},\qquad
 q(t)=\operatorname{Tr}(I-R(t)).
\]

Under RH, a multiple endpoint forces q(t)>=1/2. Thus an independently proved **q(t)<1/2** excludes all multiple endpoints in that population. Complete all-height coverage is still needed for every-zero simplicity.

The weaker bound **q(t_h)=o(N(h))** gives almost-all simplicity through M_0<=6q. It permits a sparse exceptional set. These thresholds must not be interchanged, and the time/height scale must come from source information rather than inspection of unknown endpoint gaps.

The collision singularity is understood: L itself diverges, while tL and bounded filters retain a finite nonzero signature. Regularizing the observable is useful only if it preserves that signature. Neither differentiating log Delta nor moving around a complex collision removes it.

## What remains open

The central missing result is a useful analytical upper bound for q, its large-eigenvalue count or the earlier projected-pair statistic, derived from the complete canonical source. Available identities identify the quantity to estimate; they do not establish a favorable sign or error budget.

Curved-contour wall and resolvent bounds also remain unpaid. A common complex-time path, a moving spatial wall and a height-dependent time graph are distinct geometries. An event-free contour need not be free of poles of the chosen resolvent. A proof must retain the relevant population, wall, slope, interpolation and invertibility conditions.

Backward use of late-time data needs a stability and precision theorem. Leading long-time asymptotics can agree for simple and multiple endpoint models. The retained terminal information and the complete integrated residual must distinguish those cases, with explicit backward error and growing-rank dependence.

The required global coverage, uniform height bounds and any new simplicity conclusion remain open. An RH-free application must establish endpoint reality independently before using the positive-spectrum argument. RH is not a source of negative-time reality or complex-time positivity.

## The next analytical note

HDC-07 should begin with one declared common-time population and spatial domain, using the complete H and its source. It should carry the exterior force through

\[
 q'=4\operatorname{Tr}\bigl[R^2(L+tL')\bigr]
\]

and its edge-weight representation, then use the wall formula for the divided differences of partial_z log U. This avoids inserting an unproved internal gap floor while keeping the wall floor and complete source errors explicit.

The deliverable is a **source-derived force or residual inequality** with its time, height and error dependence. It must identify where RH enters, retain the cancellation between scale differentiation and root motion, and compare the result with the absolute fallback estimate. Repeating the exact evolution equations does not complete the task. A precisely scoped explanation of why the selected information cannot improve the fallback is an acceptable diagnostic; it does not exclude other source estimates.

Use the quadratic, Hermite, simple-endpoint quadratic and sine controls already specified in the overview. Small exact or numerical checks may support factors, signs and constants after the analytical claim is stated. Keep the [result summaries][results] and [patterns to avoid][avoid] in view, especially [target reformulations][a01], [premature numerics][a10] and [loss of coupled cancellations][a12].

## Chat history verification

The execution conversation **Continue heat contour research**, thread `01a167d3-3ce1-7ba3-8551-633916294ba0`, remains history **0001** in this investigation. The [verification receipt][receipt] records a point-in-time comparison of **37 completed public messages** against the source session, in exact order. The stored byte hash, canonical conversation hash, original creation and first-capture times, linear message structure and preceding completed final reply were checked. No private reasoning or tool-message phases were admitted by the exporter.

The scan found one matching registration among 79 discovered indexes. One unrelated malformed index is recorded in the receipt; it contains no exact match for this thread and was left unchanged. The founding brainstorm conversation and its earlier verification receipt remain separate.

The verification is a snapshot: later authorized refreshes change its counts and hashes. This turn's unsent final reply cannot be in that snapshot; the standing bounded follow-up captures it after the real response and turn completion are recorded. Archive verification establishes provenance and message coverage, not mathematical correctness.

[overview]: ../research-overview/02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md
[ledger]: 01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md
[notes]: ../notes/README.md
[n4]: ../notes/04_PAIR_STATISTICS_AS_A_ONE_SIDED_CONTOUR_INPUT_20261023.md
[n5]: ../notes/05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md
[n6]: ../notes/06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md
[review1]: ../reviews/01_FINITE_CONTRACT_AND_COUPLED_ESTIMATOR_REVIEW_20261023.md
[review2]: ../reviews/02_PAIR_STATISTICS_AND_SIMPLICITY_TRANSFER_REVIEW_20261023.md
[review3]: ../reviews/03_ANALYTICAL_SPECTRAL_CONTOUR_PROGRAM_REVIEW_20261023.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[receipt]: ../chat-histories/VERIFICATION_EXECUTION_CHAT_20261023.json
