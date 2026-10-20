# Expanding heat flow contours and later collisions

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Initial planning: **gpt-6-astra (Codex), max**;
research and manuscript revision: **gpt-6-astra, ultra**, verified from turn
metadata. Separate same-model internal review; no specialist review.

**Route BW-09. Current state: phase-concentration manuscript revised;
analytical continuation program prepared.** The finite root-wall identity,
quadratic endpoint bounds and complete-source theta saddle asymptotic are
established in the linked proofs. A strict theta cap-phase surplus and the
later-collision target remain open. New PSC estimates are not yet executed.

Start with the [current manuscript](manuscript/main.tex),
[analytical research plan](research-overview/03_ANALYTICAL_PHASE_SURPLUS_PROGRAM_20261020.md),
and [matching progress register](research-progress/03_ANALYTICAL_PHASE_SURPLUS_PROGRESS_20261020.md).
Following simple roots cancels the wall phase exactly. A regular cap with
N interior simple roots has phase decrease (N+1)π. A complete strict bound
above π would force a later event. The cap at infinity does not remove
its half-turn: the quadratic concentrates it near endpoints, whereas
theta's fixed-index large-time profile concentrates it near an interior
extremum. Neither concentration statement proves the missing surplus.

The [original BW09 program](research-overview/01_EXPANDING_CONTOUR_RESEARCH_PROGRAM_20261020.md)
and [register](research-progress/01_EXPANDING_CONTOUR_PROGRESS_20261020.md)
govern overall coverage, continuation, multiplicities and the later-collision
target. The [HFCE program](research-overview/02_HEAT_FLOW_CONTOUR_AND_ENERGY_PROGRAM_20261020.md)
and [register](research-progress/02_HEAT_FLOW_CONTOUR_AND_ENERGY_PROGRESS_20261020.md)
retain the completed bounded energy comparisons and their unexecuted gates.
The first finite round and later HFCE round excluded two small event boxes;
the frozen Gaussian estimate failed its sign, and one localized average
was proved positive. These outcomes are separate from winding estimates.

Use “heat flow contour” or “parabolic heat flow contour”: increasing t is
the backward-heat direction, and the square-root opening is a diffusive
scale rather than a finite causal cone.

| Location | Purpose |
| --- | --- |
| [Manuscript](manuscript/main.tex) | Coherent analytical argument, proofs and links to longer derivations |
| [Research overview](research-overview/README.md) | Programs and acceptance conditions |
| [Research progress](research-progress/README.md) | Distinct BW09, HFCE and PSC task statuses |
| [Notes](notes/README.md) | Earlier derivations and bounded estimate contracts |
| [Brainstorm](brainstorm/README.md) | Further analytical notes from the current conversation |
| [Numerics](numerics/README.md) | Supporting bounded checks and small source records |
| [Reviews](reviews/README.md) | Assessments of specified claims and versions |
| [Preserved draft](drafts/README.md) | Exact previous source, saved at the user's explicit request |
| [Chat histories](chat-histories/README.md) | Existing route conversations and capture policy |

The [draft history](DRAFT_HISTORY.md) records the revision and its review.
The [originating note](../../notes/04_EXPANDING_CONTOURS_AND_A_LATER_COLLISION_TARGET_20261020.md)
contains the initial proposal. The [parent register](../../research-progress/02_THRESHOLD_SIGNED_ARITHMETIC_PROGRESS_20261020.md)
continues to govern BW2 tasks without reopening earlier closed attempts.
Read the [result summaries](../../../../../../result-summaries/README.md),
[collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [patterns to avoid](../../../../../../avoid/README.md).
[Boundary-winding home](../../README.md) · [Route index](../README.md).

Separate track, 20 October 2026 (**gpt-6-astra, ultra**):
[BW-10 — RH implies simple zeros](../10_rh_implies_simple_zeros/README.md)
uses the shared contour machinery for a distinct target: excluding a multiple
zero at heat time zero under RH. Its brainstorm, program, progress and
chat history live there. The BW-09 positive-threshold program retains its
existing scope and statuses.
