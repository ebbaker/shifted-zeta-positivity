# Verification infrastructure worth reusing

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

Not theorems, but the machinery that made the theorems checkable, and
that any new investigation should reuse rather than rebuild.

- **Statement inventory and ledger.** The first-slab blueprint lists every
  statement with its dependencies, proof status (paper, computer, asserted)
  and human-verification status, twinned with a machine-readable ledger.
  The same layout is the intended model for later papers.
- **Check-programme conventions.** Standard-library Python, deterministic
  JSON output, a record file whose hashes identify the script and inputs,
  registered for byte-identical replay; exact rational arithmetic where
  possible; python-flint only for validated enclosures (the convention
  should say so once). Receipts describe their scope (polynomial germs,
  rational surrogates, or genuine theta integrals) so counts are read
  correctly.
- **Certificate formats.** Outward interval arithmetic (Arb or
  python-flint) with explicit tail allowances; containment tests, not
  overlap tests; two independent programs sharing no code for a headline
  bound (19's practice); a record of the environment and runtime.
- **Large-data policy.** A 1 MB ceiling on committed files, regenerable
  data outside git bound by two hashes, an environment-variable lookup, a
  pre-commit size check and a CI hygiene check (README links, manifest
  hashes, file sizes; not mathematics and not conflict markers).
- **Chat recorders.** Registered research conversations per
  investigation, with a Cowork recorder that refreshes a session's own
  record at the end of every turn, a Codex/ChatGPT importer, locks, and
  integrity checks.
- **Review protocol.** Cross-model review rounds, verdict files, errata as
  dated addenda with the original text kept, a redaction checklist, and
  release gates (status current, every note in the checklist, code passing
  D1–D5).

## Status

In use; the hygiene checker runs in CI. Known gaps: no conflict-marker
test, the human-verification columns are unfilled, and the first-slab
certificate code is outside the tree pending its release gate.

## Reusable for

Starting a new investigation with the right skeleton (notes/, numerics/,
reviews/, DRAFT_HISTORY.md, chat-histories/), writing a checker that a
reviewer can replay, and recording a certificate that a later audit can
re-run.

## Where

- Blueprint and ledger: first slab's [`blueprint/README.md`](../papers/weil-positivity/shifted-zeta/first-slab-positivity/blueprint/README.md), [`blueprint/statements.md`](../papers/weil-positivity/shifted-zeta/first-slab-positivity/blueprint/statements.md), [`blueprint/ledger.yaml`](../papers/weil-positivity/shifted-zeta/first-slab-positivity/blueprint/ledger.yaml).
- Verification: first slab's [`verification/README.md`](../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/README.md) (the standing method rules), [`verification/CHECKLIST.md`](../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/CHECKLIST.md), [`PROTOCOL_C1_C2.md`](../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/PROTOCOL_C1_C2.md).
- Conventions: [`AGENTS.md`](../AGENTS.md), [`CONTRIBUTING.md`](../CONTRIBUTING.md), [`RELEASING.md`](../RELEASING.md), [`LARGE_FILES.md`](../LARGE_FILES.md), [`REDACTION_CHECKLIST.md`](../early-chat-logs/initial-project-files/rh3/REDACTION_CHECKLIST.md) (research log), [`CERTIFICATE_CODE.md`](../papers/weil-positivity/shifted-zeta/first-slab-positivity/CERTIFICATE_CODE.md) (first-slab release gate).
- Tools: [`tools/CHAT_HISTORY.md`](../tools/CHAT_HISTORY.md), [`tools/record_Claude_cowork_chat.py`](../tools/record_Claude_cowork_chat.py), [`tools/record_Claude_export_chat.py`](../tools/record_Claude_export_chat.py), [`tools/check_repository_hygiene.py`](../tools/check_repository_hygiene.py), [`papers/investigations-2/record_chat.py`](../papers/investigations-2/record_chat.py).
- Examples of the checker convention: [loewner numerics README](../papers/weil-positivity/susy-positivity/investigations/loewner/numerics/README.md); [22 numerics README](../papers/investigations-2/active/22_theta_manifold_geometry/numerics/README.md); a two-program certificate: [19's certified witness](../papers/investigations-2/active/19_euler_factor_controls/notes/2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md).
- Lessons on design: [`LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md`](../papers/weil-positivity/shifted-zeta/storage-depth/LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md).
