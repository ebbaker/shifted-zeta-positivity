# Archive — older drafts and reviews of the Weil-depth paper

Nothing in this folder is current. The working draft is always the one at the top level of
`papers/weil-depth/` (see `../README.md`). Each version below is kept together with the
review that produced the next one, so the sequence can be read without digging through git
history.

| Version | Date | Folder | Produced by | Reviewed in |
|---|---|---|---|---|
| v0.1 | 2026-09-09 | `drafts/v0.1_2026-09-09/` | initial draft (OpenAI/Codex-assisted); certificate `Q_(0,9/5) ≥ 1e-26 I` only | `reviews/2026-09-09_review-of-v0.1_codex/` |
| v0.2 | 2026-09-09 | `drafts/v0.2_2026-09-09/` | applied the v0.1 review; added the `log 7` certificate, independent implementation, recursion identities | `reviews/2026-09-09_review-of-v0.2_claude/` |
| v0.3 | 2026-09-09 | `drafts/v0.3_2026-09-09/` | applied the v0.2 review: two-sided enclosures at seven horizons, sector-wise statements, written-out continuation proof, related-work rewrite, trimmed recursion material to an appendix | `reviews/2026-09-09_review-of-v0.3_chatgpt/` |
| v0.4 | 2026-09-10 | *current* (top level) | applied the v0.3 review: directed rounding in Table 3, decay and horizon-ceiling claims restated as observations and resource projections, Laplace-line denominator bound corrected, classical hypotheses cited precisely, tracked `ARCHIVES.md`; no certificate changed | — |

## drafts/

* `v0.1_2026-09-09/` — the original review PDF (`FINITE_HORIZON_WEIL_REVIEW_20260909.pdf`)
  and, under `package/`, the contents of the v0.1 package as submitted for review (LaTeX
  source, top-level documents, numerics code and the 9/5 certificate) except its 11 MB matrix
  archive; the complete ZIP (`FINITE_HORIZON_WEIL_REVIEW_PACKAGE_20260909.zip`, SHA-256
  `e0b66ad3…`) is kept with the other large files outside git (see `../ARCHIVES.md`).
* `v0.2_2026-09-09/` — the v0.2 PDF, its LaTeX source and bibliography, and the v0.2
  top-level documents (`README.md`, `STATUS.md`, `CONTINUATION_WEIL_DEPTH_20260909.md`,
  `REVIEW_BUILD_RECORD.json`, `SHA256SUMS.txt`). The v0.2 numerical archives for 9/5 and
  `log 7` are unchanged in the current `numerics/output/` (same matrix hashes); only their
  certificate and analysis files were regenerated at the sharper floors.
* `v0.3_2026-09-09/` — the v0.3 PDF, its LaTeX source, bibliography and generated tables, and
  the v0.3 top-level documents (`README.md`, `STATUS.md`, `CONTINUATION.md`,
  `BUILD_RECORD.json`, `SHA256SUMS.txt`). No numerical record changed between v0.3 and v0.4;
  the only code change is the directed rounding in `numerics/make_tables.py` (v0.3 version in
  git history at `a566944`), which regenerated the tables and `output/paper_numbers.json`.

## reviews/

* `2026-09-09_review-of-v0.1_codex/` — `REVIEW_20260909.md` (machine-assisted review that
  produced v0.2) and `REVIEW_CHANGES.patch` (the v0.1 → v0.2 diff).
* `2026-09-09_review-of-v0.2_claude/` — `REVIEW_CLAUDE_20260909.md` (machine-assisted
  review with independent recomputation that produced v0.3). Its verification scripts are
  kept live under `../numerics/review_claude/` because they still apply to the current
  package.
* `2026-09-09_review-of-v0.3_chatgpt/` — `FINITE_HORIZON_WEIL_V03_REVIEW_20260909.md`
  (machine-assisted review of v0.3 without recomputation, which produced v0.4),
  `RESPONSE_20260910.md` (item-by-item disposition) and `REVIEW_CHANGES.patch` (the
  v0.3 → v0.4 diff of text, tables and code).

## background/

Historical research reports and checksum lists that preceded v0.1 (`ORIGINAL_*`,
`ARITHMETIC_DEPTH_*`), moved here from `numerics/background/`. Their statements about
what was or was not yet computed describe their own date and are superseded by the
current `STATUS.md`.

[Storage-depth paper (v0.3, working draft)](../../storage-depth/README.md) · [All manuscripts](../../README.md)
