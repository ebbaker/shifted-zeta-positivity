# Research milestones

Prepared for Edward Baker with LLM assistance.

- **13 October 2026 — Folder created; first results.** Claude Opus 5.5
  (`claude-opus-5-5`), Claude Cowork, effort **max**. Added the
  [program and three-controls protocol](notes/INITIAL_RESEARCH_PROGRAM_20261013.md)
  and [Note 1](notes/1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md):
  exact flow, Laguerre-witness criterion, a numerical collision table
  (originally labelled \(\Lambda_{c,p}\)), and a formal local expansion
  with numerical agreement.
  Standard-library checker and small record in `numerics/`. No certified
  bound yet. Not yet committed when written; the commit that adds this
  folder is the reference version.

- **13 October 2026 — Collision notation and witness-margin correction.**
  Prepared for Edward Baker with LLM assistance by `gpt-6-astra` (Codex),
  effort **ultra**. Corrected [Note 1](notes/1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md)
  and the [program](notes/INITIAL_RESEARCH_PROGRAM_20261013.md) to use
  \(T_0\) for tracked collisions, retain global-zero and certification
  obligations, and distinguish a diverging normalized witness from a
  shrinking raw margin. Added the [legacy-key guide](numerics/README.md#legacy-labels-and-what-the-record-establishes);
  checker and numerical records are unchanged. Snapshot reference: the
  commit containing this correction; no new manuscript snapshot.
