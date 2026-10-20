# Local winding at a double threshold event numerics

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**; actual reasoning effort **xhigh**, verified from recorded turn metadata.

The [exact paired-face control checker](check_paired_face_contract.py) and its [small receipt](PAIRED_FACE_CONTROLS_20261019.json) record eight finite control cases. Event controls have degree -1; event-free, boundary-zero, uncertainty, orientation and coverage cases behave as required. No theta quadrature or theta event was computed.

Execution update, 19 October 2026: prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

Replay from the repository root with Python 3, passing the checker --repo . and --output /tmp/bw01-paired-face-replay.json. The receipt identifies the source versions. Results use exact rational whole-segment bounds and exact polygon degree.

 Before a diagnostic, freeze its mathematical question, domain, source versions, full error ledger, comparator and falsifying outcome. Keep scripts and small execution records here; keep large regenerable output outside Git under the [large-file policy][large]. Separate floating diagnostics, exact controls and interval certificates.

[Research home](../README.md).

[program]: ../../../research-overview/01_THRESHOLD_BOUNDARY_WINDING_RESEARCH_PROGRAM_20261019.md
[progress]: ../../../research-progress/01_THRESHOLD_BOUNDARY_WINDING_PROGRESS_20261019.md
[large]: ../../../../../../../LARGE_FILES.md
[history]: ../../../../../../../tools/CHAT_HISTORY.md
[predecessor]: ../../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[index]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[walls]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md

20 October 2026, gpt-6-astra, ultra: [exact checker](check_event_conditioned_positive_source.py), [small execution record](EVENT_CONDITIONED_POSITIVE_SOURCE_20261020.json). These are own-source controls and analytic coefficient enclosures; no theta event or new region is measured.
