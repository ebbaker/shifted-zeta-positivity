# Sharp finite-sum bounds: manuscript

17 October 2026. Drafted for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
Section 7 and the rebuild of 18 October 2026: drafted for Edward Baker with
LLM assistance, **Claude Opus 5.5** (`claude-opus-5-5`), Claude Cowork,
reasoning effort **max**.

**Status: user-requested unreviewed working draft.** The manuscript assembles
the native sharp binding, certified four-leg strip transfer, one complete
finite window, and the revised infinite tail at t = 0.157. The finite floors
690989 ≤ N < 3840000 remain open. Section 7 (activation along a leg) reduces
them to certified rows and outward activation bounds on a finite mesh, which a
floating plan puts at twenty rows; only the first row is certified. The
proposed Newman bound is explicitly conditional; no new bound is established.

- [Compiled manuscript](sharp_finite_sum_bounds/sharp_finite_sum_bounds.pdf)
- [Editable LaTeX source](sharp_finite_sum_bounds/main.tex)
- [Build record and input identities](sharp_finite_sum_bounds/BUILD_RECORD.json)
- [Contract and feasibility ledger](../notes/round-1/01_SHARP_WEIGHT_CONTRACT_AND_FEASIBILITY_20261017.md)
- [Bounded transfer implementation](../notes/round-1/02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md)
- [Numerical evidence and reproduction commands](../numerics/round-1/README.md)
- [Round-one cross-model review](../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md) and the
  [support computations for Section 7](../numerics/round-1/claude-review/README.md)

The title page states “Drafted for Edward Baker”; the acknowledgements record
LLM assistance and the model/effort. Same-model internal checks, compilation
and visual inspection do not replace the pending round-level cross-model
and specialist review. Imported approximation, initial-verification and
barrier inputs remain identified in the text.

Open the `sharp_finite_sum_bounds` project folder in the Codex LaTeX editor
for source editing and the live PDF preview. The exported PDF was rebuilt on
18 October 2026 with TeX Live 2023 (pdfTeX 1.40.25, cm-super fonts) and
latexmk 4.83, with auxiliary files outside the repository; the exact export
command and file hashes are in the build record, which also keeps the
identity of the first build (14 pages, latexmk 4.79). All 18 pages were
rendered and checked, with no final compiler warnings.

This is the sole editable manuscript project, created at the user's request
before a reviewed milestone. Future revisions use this source and the concise
[DRAFT_HISTORY.md](../DRAFT_HISTORY.md); no snapshot folder was created.
