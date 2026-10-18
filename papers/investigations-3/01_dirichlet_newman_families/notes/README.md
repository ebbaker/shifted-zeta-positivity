# Dirichlet Newman families: notes

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

Incremental derivations and one coordination note per phase.

Begin with the bounded task in the [initial proposal](../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md).
Use dated numbered notes, one owner
per file, and one coordination note per phase. Include the intended author,
LLM assistance, actual model and effort, claim status, sources, and next
decision. Keep computations in numerics and assessments in reviews.

Notes are organized by research round. Round 1 retains the initial
contract; round 2 proves the positive-time floor and compact comparison;
round 3 removes confinement by approximation and supplies the manuscript.
The [relocation receipt](round-1/RELOCATION_20261017.json) identifies the
link-only move-time bytes and the original as-reviewed identity. A later,
explicitly dated annotation corrects the first note's literature search.
The round-2 annotation points to its unconditional continuation.

| Note | Date and model | Status |
| --- | --- | --- |
| [Round 1: normalization and transfer contract](round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md) | 17 October 2026; Claude Opus 5.5 (`claude-opus-5-5`), Claude Cowork, effort max | Reviewed in [review 01](../reviews/01_NORMALIZATION_AND_TRANSFER_CONTRACT_REVIEW_CODEX_20261017.md); targeted corrections and proof repairs supplied in round 2. Original planning tables retain their stated open assumptions |
| [Round 2: positive-time floor and conditional comparison](round-2/02_BURGERS_FLOOR_AND_CONDITIONAL_COMPARISON_CODEX_20261017.md) | 17 October 2026; gpt-6.1-sol (Codex), effort ultra | Proved in-note: explicit Burgers/Riccati floor and completed barrier repairs. Conditional only on H12: 0.27 at q >= 10^12 and O((log q)^(-4/7)); exact scalar certificate. Historical conditional result; round 3 bypasses H12. Cross-model review pending |
| [Round 3: sine-tail limit and comparison without confinement](round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md) | 17 October 2026; gpt-6.1-sol (Codex), effort ultra | Proved in-note: approximation removes H12 from the comparison, yielding 0.27 at q >= 10^12 and O((log q)^(-4/7)); incorporated in the manuscript. [Internal same-model check](../reviews/02_SINE_TAIL_AND_MANUSCRIPT_CHECK_CODEX_20261017.md); specialist review pending |
