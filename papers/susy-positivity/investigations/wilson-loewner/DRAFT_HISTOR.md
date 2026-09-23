# Draft and research milestone index

Future manuscript milestones should reference commits or tags. No new draft
snapshot is created for these research addenda. Existing snapshots remain
indexed in [drafts/README.md](drafts/README.md).

| Date | Investigation | Version reference | Why it matters | Research and review |
|---|---|---|---|---|
| 2026-09-23 | Wilson--Loewner / WZW standalone write-up | [Live source](WZW/manuscript.tex), uncommitted addition based on `20f252d3d0430216078045d5823271e1a2e0031d`; that commit does not contain the write-up | Separate manuscript for the completed WZW pilot and direct arithmetic-source connection; parent manuscript pair and historical research preserved | [Continuation](WZW/notes/CONTINUATION_AFTER_WZW_WRITEUP_20260923.md), [internal audit](WZW/reviews/review_codex_manuscript_20260923.md), [build record](WZW/BUILD_RECORD.json) |
| 2026-09-22 | Wilson--Loewner: direct arithmetic source | Uncommitted research addendum based on `20f252d3d0430216078045d5823271e1a2e0031d`; that commit does not contain this addendum | Normalized Loewner source from shifted xi, exact arithmetic recovery, xi-linearized flow, continuation and generator obstructions, and weighted operator control; manuscripts unchanged | [Note](notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md), [internal audit](reviews/review_codex_arithmetic_loewner_source_20260922.md), [checks](numerics/records/arithmetic-loewner-source-20260922.json) |
| 2026-09-22 | Wilson--Loewner: SU(2)_2 boundary pilot | Uncommitted research addendum based on `20f252d3d0430216078045d5823271e1a2e0031d`; that commit does not contain this addendum | Explicit blocks, complete deterministic generator, constant-driver tensor norm balance, separate CS pairing, and raw-smearing limitation; manuscripts unchanged | [Note](notes/SU2_LEVEL2_DETERMINISTIC_LOEWNER_PILOT_20260922.md), [internal audit](reviews/review_codex_wzw_loewner_pilot_20260922.md), [checks](numerics/records/wzw-loewner-pilot-20260922.json) |

Replace the working-tree references with the containing commit when these
addenda are committed. Detailed research history stays in the linked files.
