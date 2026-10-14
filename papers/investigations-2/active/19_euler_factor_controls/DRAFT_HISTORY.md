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

- **14 October 2026 — Manuscript with certified and asymptotic lower
  bounds.** Claude Opus 5.5 (`claude-opus-5-5`; the serving model may
  differ), Claude Cowork, effort **max**. Added the
  [manuscript source](manuscript/euler_factor_controls.tex) and compiled
  [PDF](manuscript/euler_factor_controls.pdf) (16 pages; "Drafted for
  Edward Baker", with an LLM acknowledgement); the standard-library
  [certificate program](numerics/check_euler_control_witnesses_claude_20261014.py)
  and its [record](numerics/EULER_CONTROL_WITNESS_CERTIFICATES_20261014.json)
  (status PASS: fifteen witnesses, theta moments and the inequality of the
  asymptotic theorem; source SHA-256 `5e0b538c...`); and the
  [internal verification](reviews/1_MANUSCRIPT_AND_CERTIFICATE_VERIFICATION_CLAUDE_20261014.md).
  The verification found that the first version of the program rounded
  negation in the default 28-digit context; the program was corrected and
  the record regenerated before these files were added. Folder, numerics
  and review READMEs and the portfolio indexes were updated to the new
  status. Not yet committed when written; the commit that adds the
  manuscript is the reference version.
