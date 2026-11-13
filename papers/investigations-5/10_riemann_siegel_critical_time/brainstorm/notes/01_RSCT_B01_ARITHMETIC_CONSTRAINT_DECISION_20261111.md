# RSCT-B01 decision: test the reflected Poisson constraint, stop before unpaid acquisition

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0001. Actual backend model and effort are unavailable in the recorded configuration. Type **B**; recommended configuration was GPT-6 Astra, ultra, not a statement of actual settings.

**Disposition: B01 complete with a scoped failed-acquisition/overlap return. E01 remains reserved and not executable.** The [supporting derivation](../../notes/03_RSCT_B01_REFLECTED_POISSON_TEST_20261111.md) is the only new analytical note. The [sole register](../../research-progress/01_RSCT_RESEARCH_PROGRESS_20261111.md) owns live status. No new exclusion region, numerical campaign or manuscript.

## Decision and result

The bounded pass compared exactly two formulations:

| Formulation | What the all-real condition adds | Disposition |
| --- | --- | --- |
| Complete-arm phase at a real zero | Product constraints on H, but no signed constraint on the chosen arm's imaginary part | Not selected: stationary phase and arm-zero alternatives remain; an exact heat polynomial screens representation-only inference |
| Complete-field reflected Poisson mass above the candidate event | Nonvanishing off the real axis and a positive contribution from every real zero, including the reflected event | Selected and tested analytically; gives an exact necessary lower bound but no opposing canonical arithmetic estimate |

With \(F=H_T\) given by the complete evolved reflected RS formula, \(z=a+iy\), \(k=1+y^2/(4a^2+y^2)\), the selected arithmetic quantity is
\[
\mathcal B=2k|F|^2+y\Im(F'\bar F).
\]
An all-real event of multiplicity m≥2 forces
\[
\mathcal B=((2-m)k-y^2 S)|F|^2<0,
\quad S=\sum_{r\ne\pm a}((a-r)^2+y^2)^{-1}>0.
\]
The attempted arithmetic constraint is a positive lower bound for B at some y, using the canonical arms independently of their zero description. The formula retains both reflected arms, gamma factors, all arithmetic modes, full remainder and physical derivative. It does not divide by a possibly vanishing complete arm.

This pass **did not prove that positive lower bound**. The precise first unpaid premise is the sign and size of the complete mixed arithmetic terms. All-realness supplies the opposing geometric inequality, not its contradiction. The positive three-atom threshold control yields B<0 despite positivity, the physical heat equation and all-realness. Its failed premise is the unchanged complete theta arithmetic. This excludes only that reduced-information inference.

The supporting note pays both value and derivative errors in an explicit quadratic envelope. At a double event the true residual is order y^6, although its separate terms are order y^4; making y small therefore does not automatically help an estimate using separate errors. These are elementary diagnostic identities, not new canonical gains. No error order is asserted for a differentiated RS approximation.

## Classification and comparison

The [result index](../../../../../result-summaries/README.md), especially [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md) and [geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), and the [avoid index](../../../../../avoid/README.md) govern this return. Apply [01](../../../../../avoid/01_restating_the_target.md), [02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) and [07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

At an all-real slice, existence of a height y with B>0 is just nonmultiplicity at a. The all-threshold demand is thus the inherited final-strength endpoint problem, not a new intermediate theorem supported by tests. The tests above concern the sufficiency of reduced premises and the error interface, not RH.

The complete-population Poisson density overlaps the existing HCB acquisition program. HCB's integrated descendant excess and this pointwise reflected mass have different consumers and constants; neither result is transferred to the other. A generic first-jet floor would remain HCB-05 work. Its failed n=1 triangle methods do not imply failure of all signed estimates for B. OA remains parked: no starting pair or signed force is supplied here. GNP-RS Green values vanish at the all-real slice and do not acquire B's opposite sign.

## Stop and continuation gate

This is the specified completion option 3, not a failed execution of E01. No fixed proof method for the missing canonical inequality has been identified, so issuing E01 would merely rename that open problem.

Do not automatically open a third formulation or run numerical samples. A future **B01 reopening** needs a named new signed arithmetic input or method, a specified intermediate time-height region, and a comparison with existing HCB ownership. Its question is whether that input controls the full mixed expression with a positive paid margin. If it does, freeze E01 for GPT-6.1 Sol; otherwise return the exact failed premise. The continuation and model-change guidance are in [Continuation01](../../notes/01_RSCT_CONTINUATION_AND_PROMPT_20261111.md). This pass was checked by the [same assistant](../../reviews/01_RSCT_B01_SAME_ASSISTANT_CHECK_20261111.md), not independently reviewed.
