# Sharp finite-sum bounds: manuscript

17 October 2026. Drafted for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

**Status: user-requested unreviewed working draft.** The manuscript assembles
the native sharp binding, certified four-leg strip transfer, one complete
finite window, and the revised infinite tail at t = 0.157. The finite floors
690989 ≤ N < 3840000 remain open. The proposed Newman bound is explicitly
conditional; no new bound is established.

- [Compiled manuscript](sharp_finite_sum_bounds/sharp_finite_sum_bounds.pdf)
- [Editable LaTeX source](sharp_finite_sum_bounds/main.tex)
- [Build record and input identities](sharp_finite_sum_bounds/BUILD_RECORD.json)
- [Contract and feasibility ledger](../notes/round-1/01_SHARP_WEIGHT_CONTRACT_AND_FEASIBILITY_20261017.md)
- [Bounded transfer implementation](../notes/round-1/02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md)
- [Numerical evidence and reproduction commands](../numerics/round-1/README.md)

The title page states “Drafted for Edward Baker”; the acknowledgements record
LLM assistance and the model/effort. Same-model internal checks, compilation
and visual inspection do not replace the pending round-level cross-model
and specialist review. Imported approximation, initial-verification and
barrier inputs remain identified in the text.

Open the `sharp_finite_sum_bounds` project folder in the Codex LaTeX editor
for source editing and the live PDF preview. The exported PDF was built with
TeX Live 2023 and latexmk 4.79, with auxiliary files outside the repository;
the exact export command and file hashes are in the build record. All 14
pages were rendered and visually checked, with no final compiler warnings.

This is the sole editable manuscript project, created at the user's request
before a reviewed milestone. Future revisions use this source and the concise
[DRAFT_HISTORY.md](../DRAFT_HISTORY.md); no snapshot folder was created.
