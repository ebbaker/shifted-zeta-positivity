# Weil-depth paper — v0.4 revision note (10 September 2026)

Branch `finite-horizon-weil` of `ebbaker/shifted-zeta-positivity`, folder `papers/weil-depth`.
Baseline: `a566944` (v0.3 at `6a87626` plus the ChatGPT review of v0.3). All changes below are
**staged but not committed** in Teddy's local clone (`~/Documents/shifted-zeta-positivity`);
the local branch was fast-forwarded from `6a87626` to `a566944` over HTTPS first.

## Review applied

`archive/reviews/2026-09-09_review-of-v0.3_chatgpt/FINITE_HORIZON_WEIL_V03_REVIEW_20260909.md`
(moved there from the loose location it was committed at). Disposition, item by item, in
`RESPONSE_20260910.md` in the same folder; `REVIEW_CHANGES.patch` is the v0.3 → v0.4 diff.
No certificate, floor, upper bound or continuation constant changed; no numerics were rerun.

1. **Table 3 rounding directions** — `numerics/make_tables.py` rewritten to parse Arb balls as
   intervals and round lower values down from the lower endpoint, upper values up from the
   upper endpoint (`log 7` row: 0.6075→0.6074, 3.73e-37→3.74e-37, 4.6e-295→4.7e-295; other
   rows moved outward similarly). `paper_numbers.json` now records endpoints. Tables 1–2
   unchanged. Independently re-verified by parsing the LaTeX tables against the JSON records.
2. **Super-exponential decay** — abstract, §1, §7.1 restated as observations on seven
   horizons; no decay law at unbounded depth claimed; Zhu's law described as empirical /
   conjectural, large-window bound conditional on RH (checked against arXiv:2608.24827v2).
3. **Horizon ceiling** — abstract and §7.2 restated as resource projections; recorded that
   `a_{N,L} → +∞` at fixed `L<3` (`K_L`, `Σ_L` finite); 0.6-floor sufficiency at new horizons
   flagged unknown; `10^-34`/unit qualified as local extrapolation.
4. **Lemma 3.3 proof** — false `|p±α|,|p±β| ≥ η−1/2` replaced by `|p−α| ≥ η−1/2`,
   `|p+β| ≥ η+1/2` (denominator factors of `ρ_s = (p+α)(p−β)/((p−α)(p+β))`).
5. **Packaging** — `SHA256SUMS.txt` regenerated (71 entries, no `.DS_Store`); `.gitignore`
   excludes `.DS_Store` and manuscript build outputs; new tracked `ARCHIVES.md` documents the
   external archive layout/hashes (archives live at
   `~/Documents/shifted-zeta-positivity-archive/weil-depth/numerics-archives`); "any machine"
   hash-portability wording limited to tested environments everywhere.
6. **Clarifications** — Yoshida / Connes–Consani Theorem 1 hypotheses (support and
   Fourier-vanishing at ±i/2, resp. i/2 and 0) cited as printed; vanishing conditions
   identified with removal of the pole term `2|C|²−2|S|²`; `log 2` row described as the
   full-form statement, not "recovering" theirs. "Cross-check" → "consistent with his reported
   enclosure". Appendix B exact/model sentence added. §6 renamed. Acknowledgment updated.

## Files

Version bumped to 0.4 (10 Sept 2026) in tex, README, STATUS, CONTINUATION, BUILD_RECORD.
`finite_horizon_weil_v0.4.pdf` rebuilt with latexmk (TeX Live 2022; 22 pages; no warnings, no
overfull boxes). v0.3 deliverables archived under `archive/drafts/v0.3_2026-09-09/`;
`archive/README.md` table extended.

## Repository-level follow-up (same day, also staged)

- **`LARGE_FILES.md`** (repo root): the convention for keeping large files off GitHub —
  ~1 MB ceiling on committed files, regenerable derived data never versioned, two hashes
  (file + content) in the small records, hash-bound replay, `<PAPER>_ARCHIVES` env-var lookup,
  sibling folder `shifted-zeta-positivity-archive/<slug>/numerics-archives/` mirroring the
  paper layout with `README.md` (copy of the tracked `ARCHIVES.md`) and `SHA256SUMS.txt`;
  step-by-step procedure for adding a file / starting a paper / supplying data to a reviewer /
  repairing a mistaken commit; pre-commit size-check commands; what a Zenodo release archives.
  Records that `main` has no blob > 1 MB while `finite-horizon-weil` history still references
  ~130 MB of old archive blobs → squash-merge, then delete the branch.
- Root `README.md`: "five" working drafts, weil-depth block in the program diagram, `papers/`
  row, new "Large files" section, release-contents note, formalizers paragraph.
- `papers/README.md`: weil-depth row (v0.4, three review rounds, author block "Edward Baker"),
  layout note, "two threads" paragraph, dates → 10 Sept.
- `MANIFEST.md` (six folders, LARGE_FILES.md, weil-depth entry), `CHANGELOG.md` (Unreleased
  entry for the paper and the convention), root `.gitignore` (`numerics-archives/`),
  `.github/workflows/build-latex.yml` (7th matrix entry: `papers/weil-depth/manuscript`,
  `finite_horizon_weil`, 22 pages — untested in CI), `papers/weil-depth/ARCHIVES.md` cross-ref.
- External archive folder README replaced by a header + copy of `ARCHIVES.md` (old copy at
  the VM's `$HOME/numerics-archives_README_old.md` only; not in git).

## Operational caveat for sessions on Teddy's linked Mac (learned 10 Sept)

Git run through the mounted repo folder can create files under `.git` but cannot delete them
(the mount refuses unlink inside `.git`, even after deletion approval). Any git command that
takes and then removes a lock — `git fetch` (maintenance.lock), a ref update (`HEAD.lock`),
`git status` refreshing the index (`index.lock`) — leaves a 0-byte `*.lock` behind, and a
leftover `HEAD.lock` or `index.lock` makes Teddy's own `git commit` fail ("cannot lock ref
'HEAD'" / "index.lock: File exists"). That happened this session and was fixed by renaming the
three stale locks into `.git/stale-locks-from-claude-session-20260910/` (renames work; git
ignores unknown files in `.git`). Rules for future sessions: run read-only git with
`GIT_OPTIONAL_LOCKS=0`; avoid write operations (fetch/merge/add) from the VM unless
necessary, and after any such operation run `find .git -name '*.lock'` and rename leftovers
away; let Teddy commit from his Mac.

## Left open

- `numerics/output/enclosure_table.tex` (from `enclose_certificate.py --summary`) still prints
  midpoints of the printed upper-bound balls; not a manuscript input; needs python-flint to
  regenerate (unavailable on the local VM). Fix `summary()` to print `mid + rad` next
  numerical session.
- Author block inconsistency: weil-depth tex says "Edward Baker"; the other papers use
  "Edward B. Baker III". Not changed — Teddy's call.
- `papers/defect-depth/defect_depth.pdf` was recompiled outside the session on 10 Sept
  (15 pp. vs committed 14 pp.); Teddy staged it himself afterwards.
- Commit (Teddy's call), then the planned squash merge into `main`.
