# Theta observables and Newman dynamics

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

**Shared analytical background — 6 November 2026, gpt-6-astra/max:** [TND-E06 manuscript](manuscript/README.md) is complete as one evolving analytical source, with proofs of the shared geometry/source/transport dictionary and both conditional realizations. [Integration and progress review](reviews/02_SHARED_ANALYTICAL_BACKGROUND_MANUSCRIPT_REVIEW_20261106.md) records the 19-page build, evidence levels and branch snapshot through 01:53 America/New_York. Both branch E01/E02 realizations are internally accepted within scope; later direct collision reconnaissance is proof-author material, and auxiliary sharp conditioning bounds remain a selected target at that cutoff. Use the branch registers for subsequent status; earlier dated continuation suggestions below are historical.

Adapt MC11's angular–radial Dirac-square model on the spherical cylinder to Investigation05's radial theta geometry and de Bruijn–Newman framework. A leading priority is understanding the Hamiltonian as naturally as possible. Direct representation of Newman flow through radial spectral modes and a natural auxiliary flow remain two avenues for discussion. See the [author's model and flow clarification][clarification].

**Shared assessment return — 6 November 2026, gpt-6.1-sol/ultra:** [TND-E03 r2 Review01](reviews/01_TND_E03_R2_GEOMETRY_SOURCE_AND_TRANSPORT_ASSESSMENT_20261106.md) accepts parent E01 within its stated comparison/source-transport scope, with no required mathematical correction. The ordinary-heat/scalar-comparator generator distinction is explicit. This internal same-model review supplies the shared prerequisite to both branch E02 assessments, without assessing or activating them. [Continuation/model-change guidance](research-progress/handoffs/03_TND_E03_R2_RETURN_AND_MODEL_CONTINUATION_20261106.md) recommends auxiliary TND-A-E02/Sol next. The parent and branch registers remain the sole live owners; earlier setup paragraphs below are dated snapshots.

**Current organization: two numbered research branches**, created at the author's request after TND-B01's comparison. Planning update: 5 November 2026, prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra/ultra**, chat0003. E01 retains proof-author comparison scope. The branch registers below own subsequent construction choices.

| Branch | Overview | Research plan | Sole branch register |
| --- | --- | --- | --- |
| [01 Direct Newman realization](01_direct_newman_realization/README.md) | [Overview](01_direct_newman_realization/research-overview/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_OVERVIEW_20261105.md) | [Plan r1](01_direct_newman_realization/research-plan/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PLAN_20261105.md) | [TND-D progress](01_direct_newman_realization/research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md) |
| [02 Hamiltonian auxiliary dynamics](02_hamiltonian_auxiliary_dynamics/README.md) | [Overview](02_hamiltonian_auxiliary_dynamics/research-overview/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_OVERVIEW_20261105.md) | [Plan r1](02_hamiltonian_auxiliary_dynamics/research-plan/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_PLAN_20261105.md) | [TND-A progress](02_hamiltonian_auxiliary_dynamics/research-progress/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_PROGRESS_20261105.md) |

The [shared overview][overview], [shared progress register][progress] and [B01 decision](brainstorm/notes/04_TND_B01_TWO_AVENUE_DECISION_AND_BRANCH_PLANS_20261105.md) retain common model/evidence and the task crosswalk. Shared E01 assessment is TND-E03 r2; each branch owns its future realization and assessment. No E02 execution packet, numerical work or external status change accompanies this planning setup.

Use the [continuation note with pasteable prompts](notes/03_BRANCH_CONTINUATION_AND_PASTEABLE_PROMPTS_20261106.md) for either branch. Each branch now has a reference-use index following the root REFERENCE_WORKFLOW.md. For future branches or a new investigation elsewhere, see the root [setup workflow](../../../INVESTIGATION_SETUP_WORKFLOW.md).

**Auxiliary continuation pointer, 6 November 2026 (gpt-6-astra/max):** [Branch Decision01](02_hamiltonian_auxiliary_dynamics/brainstorm/notes/01_TND_A_B01_R1_SUPPLIED_PROPER_TIME_RESPONSE_DECISION_20261106.md) and its [frozen request](02_hamiltonian_auxiliary_dynamics/research-progress/handoffs/02_TND_A_E01_R1_FROZEN_REQUEST_20261106.md) record the supplied-apparatus choice. Use the auxiliary branch's sole register for live status and the request for its next prompt. This pointer changes no shared or sibling task status.

Direct-branch navigation added 6 November 2026, **gpt-6-astra / max**, direct chat0001: [B01 Decision01](01_direct_newman_realization/brainstorm/notes/01_TND_D_B01_CONDITIONAL_QUADRATURE_DECISION_20261106.md) and [the frozen E01 r1 packet](01_direct_newman_realization/research-progress/handoffs/02_TND_D_E01_R1_REQUEST_20261106.md). The direct branch register owns their live disposition. Shared, sibling and external task statuses are unchanged.

## Why this investigation is a direct child of investigations 5

[Investigation05][radial] contributes radial theta geometry, source-defined Newman evolution and conservative collision diagnostics. [MC11 within Investigation07][mc] contributes the Dirac-cylinder response, energy filtering and explicit theta observables. Neither supplies the whole proposed program. A common home alongside them makes those inputs equally visible and leaves room for other relevant work.

The founding [MC11 brainstorm][origin] remains at its original location. The author's choice superseded its tentative nested `12_theta_observables_newman_dynamics/` location and immediate contract-selection suggestion. The subsequent discussion led to the two branch plans and their dated opening choices. Existing proofs, manuscripts, task states and assessments stay with their source investigations.

## Working aims

- Understand the geometric Dirac-square Hamiltonian and use the full cylinder model to adapt Investigation05's scalar theta field and Newman framework.
- Consider radial spectral representation of Newman flow and a natural auxiliary flow, retaining both until their physical and mathematical roles are clearer.
- Explain the relation between angular energy measurements, the theta source and the signed Newman transform, with consistent normalizations and distinct parameters.
- Explore whether the model exposes a useful new relation or estimate for the signed collision observations, while recognizing physical model development as a worthwhile outcome in its own right.

The [observable derivations][observables] have proof-author checks and a pending MC11 assessment. The accepted cylinder/source results retain their existing scopes. No new mathematical result or collision exclusion is claimed by opening this investigation.

## Analytical standard

Work with arbitrary angular indices and the complete angular sum, the continuous full-line radial spectrum, and arbitrary finite derivative or moment orders where used. Record order dependence and justify every claimed limit. A theorem for each finite order is not automatically uniform in order. Finite cases and numerical scans do not substitute for a general analytical mechanism; any later numerical test needs its own bounded hypothesis and stopping rule.

## Documents and continuity

| Location | Purpose |
| --- | --- |
| [Overview and research plan][overview] | Fixed starting model, scientific aims and bounded B/E task specifications |
| [Shared research progress][progress] | Sole register for shared TND tasks, with branch ownership and task crosswalk |
| [Planning decisions][planning-decisions] | Analytical and general-index emphasis; closing the opening discussion at planning scope |
| [Initial continuation][continuation] | Historical opening brief; its deferred-plan and B00-next instructions are superseded |
| [Brainstorm proposal][proposal] | Initial proposal, with its ordering qualified by the author clarification |
| [Hamiltonian and flow clarification][clarification] | Current starting model and the direct Newman versus auxiliary flow avenues |
| `brainstorm/notes/` | Conceptual discussion notes, as requested by the author |
| `notes/` | Existing continuation brief and subsequent research notes |
| [Chat history guide][history] | Founding archive pointer and registration instructions for future chats |
| [Draft history][draft-history] | Concise notable document milestones |

The parent research-progress/ folder contains the shared register; each numbered branch has its own sole register for its distinct task family. Create other folders when their work is needed. Analytical derivations belong in `notes/`, conceptual decisions in `brainstorm/notes/`, assessments in `reviews/`, and any authorized numerical work in `numerics/`. A later manuscript would remain one evolving source.

The [result summaries][results], [patterns to avoid][avoid], [research model workflow][workflow], [large-file policy][large] and [chat-history workflow][capture] apply. The founding chat retains its unique MC11 history0006 registration; new chats devoted to this investigation should register here.

[overview]: research-overview/01_THETA_OBSERVABLES_AND_NEWMAN_DYNAMICS_DRAFT_OVERVIEW_20261105.md
[continuation]: notes/01_BRAINSTORM_CONTINUATION_20261105.md
[radial]: ../05_radial_theta_collision_geometry/README.md
[mc]: ../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/README.md
[origin]: ../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/brainstorm/notes/08_THETA_OBSERVABLES_AND_NEWMAN_INVESTIGATION_STARTING_POINT_20261105.md
[observables]: ../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/13_MC11_BR02_R1_PHYSICAL_OBSERVABLES_AND_NEWMAN_CONNECTION_20261105.md
[history]: chat-histories/README.md
[draft-history]: DRAFT_HISTORY.md
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[workflow]: ../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[large]: ../../../LARGE_FILES.md
[capture]: ../../../tools/CHAT_HISTORY.md

[proposal]: brainstorm/notes/01_HIGH_LEVEL_RESEARCH_PROPOSAL_20261105.md

[clarification]: brainstorm/notes/02_DIRAC_CYLINDER_HAMILTONIAN_PRIORITY_20261105.md

[progress]: research-progress/01_THETA_OBSERVABLES_AND_NEWMAN_DYNAMICS_RESEARCH_PROGRESS_20261105.md
[planning-decisions]: brainstorm/notes/03_ANALYTICAL_RESEARCH_PLAN_DECISIONS_20261105.md

[e01-note]: notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md
[e01-handoff]: research-progress/handoffs/01_TND_E01_R1_RETURN_AND_MODEL_CONTINUATION_20261105.md
