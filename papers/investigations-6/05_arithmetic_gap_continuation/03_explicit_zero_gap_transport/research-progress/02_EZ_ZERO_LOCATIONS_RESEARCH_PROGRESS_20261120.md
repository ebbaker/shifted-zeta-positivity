# Progress on explicit zero locations and backward gap control

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance. The desktop thread records gpt-6.2-astra/ultra. **This is the sole current progress register for the AGC-EZ task family.** [Overview](../research-overview/02_EZ_ZERO_LOCATIONS_RESEARCH_OVERVIEW_20261120.md) · [Plan and work limits](../research-plan/02_EZ_ZERO_LOCATIONS_RESEARCH_PLAN_20261120.md) · [Continuation prompt](../notes/10_EZ_ZERO_LOCATIONS_CONTINUATION_20261120.md)

## Starting state

**Setup complete. B07 is ready for a research session.** The first return is a formula-by-formula account of validity and finite-input precision, followed by a selection of one improvement to prove. The two requested papers have been checked for their relevant theorems, coordinate conventions and error ranges. Formal setup has issued no E packet. [Checked passages](../references/README.md#published-comparisons-for-the-fixed-time-zero-formulas)

| Inherited evidence | Status and scope at handoff |
| --- | --- |
| Counted large-time zero formulas | Written derivations for the local contour and the inverse in odd cumulants. For every fixed \(C\) the latter covers \(q_k\le C\ell_T\) at sufficiently large \(T\). The cubic resummation has a proved residual on this domain. The \(T=1000\) enclosures are finite checks with their own index and convergence tests. [Parent brainstorm Note 08](../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md) |
| Formula for every fixed rank | The full product gives a convergent factor-recovery limit at an independently all-real anchor. Uniform finite-order accuracy in spacing units as the rank grows is open for this use. [Factor recovery](../../01_jacobi_integer_hierarchy/brainstorm/notes/07_LARGE_TIME_FACTORIZATION_AND_BACKWARD_PROPAGATION_20261120.md) |
| Mixed exterior and time derivative | Fixed-order initialization and the full radial tail are derived in [Notes 08](../notes/08_EZ_LOCALIZATION_TO_MIXED_MOMENTS_20261120.md) and [09](../notes/09_EZ_COMPLETE_ANCHOR_FROM_ZERO_FORMULAS_20261120.md). The signed \(g_n^2M_n-2\) asymptotic has a smaller growing index range. The large-time integral uses information on each slice. [Internal assessment](../reviews/04_EZ_MIXED_MOMENT_ANCHOR_ASSESSMENT_20261120.md) |
| Published comparison | Polymath supplies counted high-label positions at fixed \(0<t\le1/2\). Platt–Trudgian supplies finite \(t=0\) coverage and the published consequence \(\Lambda\le0.2\). No same-domain positional advantage over Polymath has been established here. [Primary sources and comparison](../references/README.md#published-comparisons-for-the-fixed-time-zero-formulas) |

## Task register

| Task | Model and reason | State, dependency and expected return |
| --- | --- | --- |
| AGC-EZ-B07 | B · Astra/ultra, select the useful positional simplification | **Ready, unactivated.** Compare the counted contour, inverse/cubic and full-product formula. Select a shared position-error estimate or a wider quantified range. Write the first decision in `brainstorm/notes/`. |
| AGC-EZ-E10 | E · Sol 6.2/ultra, derive the chosen analytic remainder | Reserved for a frozen B07 specification. Return the position and adjacent-difference errors, count, source budget and matched comparison, or the exact failed inequality. |
| AGC-EZ-B08 | B · Astra/ultra, choose how to reach higher ranks at fixed time | Follows B07/E10's range and limiting estimate. Select finite-order factor recovery or a counted high-index reference. Identify a possible overlap and the data needed to match ranks. |
| AGC-EZ-E11 | E · Sol 6.2/ultra, bound the specified high-index approximation | Reserved for B08. Deliver a quantitative fixed-time range/precision result or a scoped failure, with a comparison against Polymath when both apply. |
| AGC-EZ-E12 | E · Sol 6.2/ultra, check position estimates and comparator | Reserved after a written E10 or E11 return. Record a dated assessment for each substantive position milestone. Include the extent of any remaining fixed-time height gap. |
| AGC-EZ-B06 | B · Astra/ultra, choose which signed time remainder to control | Deferred until the position stage has been assessed, including the fixed-time reach question and exterior errors. Reuse its earlier hierarchy question with the resulting anchor data. |
| AGC-EZ-E09 | E · Sol 6.2/ultra, propagate a bounded hierarchy remainder | Reserved for the subsequent B06 decision and issued specification. Return a counted backward interval, range and gap margin or a quantified obstruction. |

## Change of ownership and priorities · 20 November 2026

The [01 register](01_EZ_RESEARCH_PROGRESS_20261120.md) is the historical record. B01–B04 and E01–E07 keep their recorded outcomes, including the narrower high-time first-pair checks, the scoped phase obstruction and the far-strip estimate. The unissued B05/E08 strip follow-on remains superseded. B06/E09 keep their original dynamics question and IDs, now downstream of the position work. B07, E10, B08, E11 and E12 are the new position and assessment tasks. The parent AGC and both siblings retain ownership of their own task families. Prior frozen requests and returns remain in [handoffs](handoffs/).

Update this register after each decision, proof or scoped failure with the date, input versions, measured domain and error, strongest matched baseline, review and next dependency. For a numerical check, also record which analytical decision its outcome changes. The first unresolved quantity is the gain obtainable from the shared inverse before any time evolution.

**Manuscript revision, 20 November 2026.** The [working draft](../manuscript/README.md) now gives the physical neighboring-error identity, the finite-order product interval, the fixed-time published comparison, and the signed exterior estimate in that order. This integrates existing results. B07 remains ready to select a sharper estimate or a larger counted range. [Build record](../numerics/05_ZERO_LOCATIONS_MANUSCRIPT_BUILD_20261120.json)
