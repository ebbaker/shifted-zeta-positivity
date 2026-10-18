# Explicit heat zero counts: notes

Updated 17 October 2026 for Edward Baker with substantial LLM assistance:
**gpt-6.1-sol (Codex)**, effort **ultra**. Setup: gpt-6-astra, ultra.

| Note | Scope | Current review status |
| --- | --- | --- |
| [01: consumer audit and constant ledger](01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md) | Conditional comparison-to-count extraction and inactive consumer gate | Same-model Review 01 and cross-model Review 02 |
| [02: explicit off-axis comparison](02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md) | Comparison and local count for X>=2000000 | Cross-model Review 02 accepts as proved from named imports |
| [Round-2 continuation, Note 01](round-2/01_LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CODEX_20261017.md) | Comparison for x>=100000; paired extraction gives K_t(X)<=0.9 log(X+2)+6 | Proved in-note from named imports; same-model checks only |

The original note paths and text remain unchanged as the hash-identified
baseline covered by [Claude Review 02](../reviews/02_CROSS_MODEL_REVIEW_NOTES_01_02_AND_MANUSCRIPT_CLAUDE_20261017.md).
Their in-text deferral statements describe their creation status.
The user requested the [round-2 continuation](round-2/README.md) after that
review; its new proof is not covered by the older review.

Use dated numbered notes with intended author, model/effort, assistance,
sources, status and next decision. Computations belong in numerics,
assessments in reviews. The [original proposal](../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
and [manuscript baseline](../manuscript/README.md) retain their historical scope.

Baseline identity qualification: Note 01 already received a hyperlink-only
repair in commit `452eee4`. The old review/build hash identifies the text
before that repair. The [round-2 execution record](../numerics/round-2/LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CHECKS_20261017.json)
checks that reversing exactly the one repaired link recovers those reviewed
bytes; no mathematical text changed. This round leaves Note 01 unchanged.

Manuscript integration completed at the user's request, 17 October 2026:
[current source/PDF and build record](../manuscript/README.md). Both
comparison regimes and the paired extraction are included. New proof and
transcription checks remain same-model work; the historical notes are
unchanged. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), ultra**.
