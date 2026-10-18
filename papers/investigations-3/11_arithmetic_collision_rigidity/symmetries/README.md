# Symmetry investigations

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual reasoning
effort **max**. Program organization; no new estimate or numerical run.

Start with the [detailed research program and investigation guide][guide].
These six folders cover the four directions in the [original continuation
context][context] and the additional [manifold and Hodge assessment][review].
Every folder has enough context to begin a focused continuation: equations,
known results, missing estimate, first experiment, controls, and deliverables.

| Direction | Initial status | Next bounded task |
| --- | --- | --- |
| [S01 Modular self duality](01_modular_self_duality/README.md) | Exact law known; quantitative gain open | Specify a complete paired representation and a new remainder comparison |
| [S02 Cutoff reflection](02_cutoff_reflection/README.md) | Leading correction parity known | Retain the signed correction and compare complete jet errors |
| [S03 Normalized jet rotation](03_normalized_jet_rotation/README.md) | Rotation-defect identity available | Bound a complete arithmetic defect integral and pay derivative costs |
| [S04 Time height scaling](04_time_height_scaling/README.md) | Fixed-mode limit known; full signed limit open | Separate low modes, intermediate range, and growing cutoff uniformly |
| [S05 Covariant theta jets](05_covariant_theta_jets/README.md) | Normalized ladder and inversion signs available | Test a cancellation-preserving algebra/evaluation improvement |
| [S06 Hodge and transverse geometry](06_hodge_and_transverse_geometry/README.md) | Generic Hodge and tangential ASD limitations established | Identify a transverse or coupled signed mechanism with an exact physical map |

The first quantitative priority is S02, followed by S03. S01 supplies the
arithmetic symmetry, S04 organizes regimes, and S05 supplies a convenient
source basis. S06 is an exploratory direction with its own requirement for
a new estimating mechanism. The numbering is a stable directory map, not
an execution order. New quantitative work in these folders has not begun.

The manuscript baseline remains the [current integrated source][manuscript].
On the slab [1/100,1/5], its real gap is (1001,exp(2000)); the symmetry
program has not changed that coverage. Read the [result summaries][summaries]
and [patterns to avoid][avoid], especially the [control summary][controls],
before using an identity as an exclusion argument.

When a direction is executed, add its `notes/`, `numerics/`, and `reviews/`
subfolders as needed and link the completed results here and in its README.
Preserve signed cancellations, exact source provenance, actual model/effort,
and the declared pass/fail comparison. Existing research documents remain
at their canonical locations. New direction chats may register locally;
the current conversation keeps its [existing brainstorm history][chat].
The detailed guide gives the shared storage and history rules.

[guide]: ../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[context]: ../brainstorm/02_SYMMETRY_PROGRAM_CONTINUATION_CONTEXT_20261018.md
[review]: ../reviews/14_HODGE_AND_MODULAR_SYMMETRY_ASSESSMENT_20261018.md
[manuscript]: ../manuscript/README.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[chat]: ../brainstorm/chat-histories/0001_2026-10-18T23-12-26Z_assess-hodge-symmetry-ideas.json
