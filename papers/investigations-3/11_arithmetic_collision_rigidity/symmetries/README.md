# Symmetry investigations

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual reasoning
effort **max** at initialization. Execution updates are attributed below.

Start with the [detailed research program and investigation guide][guide].
These six folders cover the four directions in the [original continuation
context][context] and the additional [manifold and Hodge assessment][review].
Every folder has enough context to begin a focused continuation: equations,
known results, missing estimate, first experiment, controls, and deliverables.

| Direction | Current status | Next bounded task |
| --- | --- | --- |
| [S01 Modular self duality](01_modular_self_duality/README.md) | Paired-endpoint tail and complete-error gain proved and checked on the height-1000 pilot | Transfer the smaller error; a retained signed estimate remains open |
| [S02 Cutoff reflection](02_cutoff_reflection/README.md) | Complete disk-error decrease checked on pilot and cutoff crossing | Compare with earlier correlated correction or feed paid jets to S03 |
| [S03 Normalized jet rotation](03_normalized_jet_rotation/README.md) | Correlated residual increment <0.000266448 and paid transport checked on pilot; direct bound remains stronger | Derive a uniform bound from the residual's arithmetic structure at growing height |
| [S04 Time height scaling](04_time_height_scaling/README.md) | Uniform full-cutoff scalar/first-jet replacement paid on kappa [1,2]; complete signed limit open | Estimate the retained signed core; a rotation consumer needs a second-derivative payment |
| [S05 Covariant theta jets](05_covariant_theta_jets/README.md) | Normalized ladder and inversion signs available | Test a cancellation-preserving algebra/evaluation improvement |
| [S06 Hodge and transverse geometry](06_hodge_and_transverse_geometry/README.md) | Generic Hodge and tangential ASD limitations established | Identify a transverse or coupled signed mechanism with an exact physical map |

The first quantitative priority is S02, followed by S03. S01 supplies the
arithmetic symmetry, S04 organizes regimes, and S05 supplies a convenient
source basis. S06 is an exploratory direction with its own requirement for
a new estimating mechanism. The numbering is a stable directory map, not
an execution order. At the user’s request, S01 has now completed its first
bounded comparison: the [paired-endpoint derivation](01_modular_self_duality/notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md)
reduces the complete added errors at orders 0–2 on the existing pilot.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**, 18 October 2026; [internal review](01_modular_self_duality/reviews/01_PAIRED_ENDPOINT_INTERNAL_REVIEW_20261018.md).

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
