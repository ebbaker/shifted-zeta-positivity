# 13 Contradiction analysis for the Riemann Hypothesis

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model: **gpt-6-astra (Codex)**;
actual reasoning effort: **xhigh**, verified from the recorded turn metadata.

**Status: five contradiction routes have opening notes. Boundary winding now has its own research program, progress register and eight threshold sub-investigations.** No new arithmetic estimate, manuscript or mathematical review is claimed by that planning setup. The earlier bounded polynomial replay is recorded within boundary winding. A consolidated program for all five contradiction routes remains deferred.

This investigation asks which independently provable arithmetic statements
could contradict a necessary consequence of an RH counterexample. The
[living brainstorm][brainstorm] catalogues the common insights and the
distinction between a small retained jet and an actual collision.

The inherited reduction is that failure of RH forces a positive Newman
threshold with a finite real multiple zero, and all zeros are real at that
threshold. Each route selects a different observable for a possible
contradiction. The [predecessor][predecessor] supplies the finite-collision
bridge; the [local-law summary][laws] and [controls][controls] give its
geometric consequences and limitations. Restricted event exclusions or new
arithmetic restrictions remain worthwhile without a global RH conclusion.

## Contradiction routes

| Route | Opening question | Initial note |
| --- | --- | --- |
| [01 Retained first jet separation](01_retained_jet_separation/README.md) | Can the genuine arithmetic jet stay outside the collision error disk, or can joint residual information exclude exact cancellation inside it? | [Opening note](01_retained_jet_separation/notes/01_INITIAL_RESEARCH_NOTE_20261019.md) |
| [02 Threshold higher jet sign](02_threshold_jet_sign/README.md) | Can small first-jet coordinates force an arithmetic higher-derivative sign incompatible with an all-real threshold event? | [Opening note](02_threshold_jet_sign/notes/01_INITIAL_RESEARCH_NOTE_20261019.md) |
| [03 Complete source reflection incompatibility](03_source_reflection_incompatibility/README.md) | Does collision matching force a detectable violation of complete source reflection or a quantitatively constrained arithmetic observation? | [Opening note](03_source_reflection_incompatibility/notes/01_INITIAL_RESEARCH_NOTE_20261019.md) |
| [04 Boundary winding](04_boundary_winding/README.md) | Can arithmetic boundary information force winding zero on a region in which a hypothetical event would force negative winding? | [Opening note](04_boundary_winding/notes/01_INITIAL_RESEARCH_NOTE_20261019.md) |
| [05 Collision divergence and arithmetic bounds](05_collision_divergence/README.md) | Can genuine arithmetic bound a stationary collision ratio more strongly than its forced negative pole? | [Opening note](05_collision_divergence/notes/01_INITIAL_RESEARCH_NOTE_20261019.md) |

Correlated residual estimates belong in route 01. Conditional cancellation
analysis can connect routes 01 and 02 or select an observation for route 03.
Diagnostics support a named estimating question within the relevant route.
These are possible methods, not additional contradiction families.

## Relationship to existing work

Project 11 retains ownership of its arithmetic approximation and residual
theorems. This investigation analyzes the contradictory implications those
theorems might support and alternative source, boundary, or rate estimates.
The [Project 11 assessment][review19] and [existing arithmetic program][program11]
remain at their canonical locations and keep their current statuses.
Research sources remain at their canonical paths. The setup conversation
now has its sole registration in the [brainstorm archive](../brainstorm/chat-histories/0011_2026-10-20T01-37-24Z_explain-arithmetic-rigidity-obstacle.json),
following Edward's requested relocation on 19 October 2026.

Each route has the standard folders below and an initial note in notes/.
The shared folders here are available for later cross-route work. [Boundary winding now has a scoped program](04_boundary_winding/research-overview/01_THRESHOLD_BOUNDARY_WINDING_RESEARCH_PROGRAM_20261019.md) and [progress register](04_boundary_winding/research-progress/01_THRESHOLD_BOUNDARY_WINDING_PROGRESS_20261019.md). The other route overviews and this investigation-wide overview remain reserved for later synthesis; no consolidated five-route program is created.

## Folder guide

| Folder | Purpose |
| --- | --- |
| [notes](notes/README.md) | Incremental derivations, precise estimate requests, and scoped attempts. |
| [numerics](numerics/README.md) | Reproducible computations and small execution records. |
| [reviews](reviews/README.md) | Assessments of identified versions, claims, and error transfers. |
| [source-documents](source-documents/README.md) | Links to canonical sources and provenance; no copied papers. |
| [brainstorm](brainstorm/README.md) | Alternative mechanisms and questions tied to a stated contradiction. |
| [manuscript](manuscript/README.md) | Future manuscript source and build records when warranted. |
| [research-overview](research-overview/README.md) | Reserved for later synthesis after the individual routes are explored. |
| [chat-histories](chat-histories/README.md) | Canonical archives of new conversations affiliated with this home. |

Read the [result summaries][results] and [patterns to avoid][avoid], with
the specific [classification][classification], [control][control-rule],
[scope][scope], and [signed-estimate][pairing] entries. See the
[draft-history placeholder](DRAFT_HISTORY.md) and [large-file policy][large].

[brainstorm]: ../brainstorm/notes/04_SMALL_JET_OBSTRUCTION_AND_RH_CONTRADICTION_TARGETS_ASTRA_20261019.md
[review19]: ../11_arithmetic_collision_rigidity/reviews/19_FIXED_FUNCTION_PROGRAM_AND_AMBITIOUS_NEXT_STEPS_REVIEW_ASTRA_20261019.md
[program11]: ../research-overview/03_FIXED_FUNCTION_ARITHMETIC_RESEARCH_PROGRAM_20261019.md
[predecessor]: ../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[laws]: ../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[classification]: ../../../avoid/01_restating_the_target.md
[control-rule]: ../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[pairing]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[large]: ../../../LARGE_FILES.md
