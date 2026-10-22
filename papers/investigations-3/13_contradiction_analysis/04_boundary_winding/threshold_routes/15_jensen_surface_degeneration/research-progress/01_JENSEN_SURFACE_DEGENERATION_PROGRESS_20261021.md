# Jensen surface degeneration and resolution research progress

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

## Current status — first research round complete

[Note 01][note01] proves a complete coefficient-compression bound and a
local refinement of E5, then interval-certifies a root in
|s+199.79|<0.001 without RH. At the same 1e-9 approximation-error target,
the sufficient odd degree falls from **203199427483** to **46031859**,
a factor exceeding **4414**, with **65 retained coefficients** in either
case. These are sufficient bounds, not minimal degrees or evidence for
global simplicity.

The complete Jensen computation fails the predeclared factor-two speed
gate: the refined/direct ratios were **17.2** and **38.5** at 192/256
consumer bits. Central coefficient acquisition used 1024/1088 bits and
is included in those times. The two observations concern this specific
single-disk implementation; no universal performance claim follows.

**Decision:** retain the sharper estimate and the finite diagnostic;
stop extension of this fresh-acquisition, single-disk comparison. The
broader program remains in reserve pending a distinct useful objective.
The [self-review][review01] is same-assistant, not independent validation.

## Inherited evidence

| Evidence | Source and status | Limitation |
| --- | --- | --- |
| Strict finite Jensen hyperbolicity under RH | Existing [Jensen topology note][jensen]. | Allows repeated zeros of the limiting entire function. |
| Full-series O(1/d) bound and O(1/d²) remainder | Analytic E3–E6 calculations. | Complete moment constants may be expensive at large radius. |
| Double/triple profiles and simple-root displacement | E7–E9 with local errors. | No universal effective constants or all-multiplicity remainder follow. |
| Infinite-product double control and exact quadratic gap | E2 and E10. | Fail unchanged theta moments; no positive theta heat source is asserted. |
| Finite rational checks | Proposal Section 8: E3 through degree 40 and E10 at degrees 2–40. | Inherited transcription checks, not a new theta computation or global proof. |

The opening calculations have same-assistant assessment, not independent
specialist review.

## Task register

| ID | Status | Completion evidence required |
| --- | --- | --- |
| JSD-00 | Complete as program setup | Original scope, normalization, bounds and controls retained. |
| JSD-01 | Complete for the selected pilot; benefit gate failed | Fixed disk c=-199.79, r=.001; direct complete xi jets; factor-two time target in the [contract][contract01]. |
| JSD-02 | Complete for this disk | Full moments through the exact xi identity, coefficient rounding, complete tails, E4 and local E5 degree budgets; [record][record01]. |
| JSD-03 | Partial, bounded certificates complete | One simple theta zero; two finite branches of the infinite-product double control. Hypothetical theta double/triple enclosures and neighboring-zero budgets remain unexecuted. |
| JSD-04 | Complete as a scoped failed speed comparison | 192/256-bit complete runs, 4414-fold sufficient-degree reduction, and failed <=0.5 timing gate; [Note 01][note01], [self-review][review01]. |
| JSD-05 | Gated | No higher-height/multiplicity or period campaign; independent arithmetic exclusion remains absent. |

## Execution record — 21 October 2026

- Prepared for Edward Baker with substantial LLM assistance, recorded
  **gpt-6-astra (Codex), effort max**.
- Complete approximation error <1e-9; omitted Jensen tail <2.759e-17;
  refined paid boundary surplus >2.14981e-8. Both precision runs certify
  exactly one zero counted with multiplicity. No count below this window
  or new global zero coverage is claimed.
- The initial 192-bit central-series acquisition failed its coefficient
  error budget. The recorded repair adds 832 working guard bits without
  increasing the 65-coefficient budget. See the contract amendments.
- Exact quadratic-gap checks and an interval-certified infinite-product
  double control retain the distinction between finite simple branch
  points and a multiple limiting zero. The latter uses outer radius .01
  after .1 was inconclusive; the theta window was never changed.
- [Replay code][code01] and [small numerical record][record01] are in
  numerics/. The source derivation is in notes/ and its self-review in
  reviews/. There is no new manuscript or manuscript snapshot.
- This route-specific conversation is uniquely registered as chat 0001 in
  [chat-histories/][routehistory]; the original setup remains at its
  existing shared home.

## Next decision

Before acquiring more coefficients, specify a distinct benefit: for
example, an explicit multi-window task that can amortize the same prefix,
or a period/degeneration observable with a defined direct comparator.
Keep coefficient acquisition, rounding, complete tails and root-count
payments in that comparison. The present result does not measure those
other regimes, optimize the prefix, or establish a universal cost floor.
HMC-05 remains open and HMC-06 gated.

## Continuation and provenance

Use the [result index][results], [local geometry][local],
[control register][controls] and [avoid index][avoid], especially
[classification][a01], [scope][a07] and [numerical sequencing][a10].
Keep degree, physical heat time and coefficient-shift limits separate.

The setup is recorded once in [the boundary-winding archive][history].
Future entries should report degree, radius, height conversion, full
error, acquisition cost and review status. The separate
[HMC-05/06 gates][hmc] are unchanged.

[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[history]: ../../../chat-histories/0008_2026-10-21T16-44-53Z_create-proposal-research-folders.json
[hmc]: ../../10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[jensen]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[overview]: ../research-overview/01_JENSEN_SURFACE_DEGENERATION_PROGRAM_20261021.md
[proposals]: ../../10_rh_implies_simple_zeros/brainstorm/04_GLOBAL_HEAT_GEOMETRY_PROPOSALS_AND_INITIAL_SCREENS_20261021.md
[results]: ../../../../../../../result-summaries/README.md

[code01]: ../numerics/check_local_jensen_resolution.py
[contract01]: ../numerics/01_RESOLUTION_COMPARISON_CONTRACT_20261021.md
[note01]: ../notes/01_LOCAL_RESOLUTION_AND_COMPLETE_COST_COMPARISON_20261021.md
[record01]: ../numerics/JSD_RESOLUTION_COMPARISON_20261021.json
[review01]: ../reviews/01_LOCAL_RESOLUTION_SELF_REVIEW_20261021.md
[routehistory]: ../chat-histories/README.md
