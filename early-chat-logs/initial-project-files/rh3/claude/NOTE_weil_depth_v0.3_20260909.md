# Weil-depth paper: v0.3 applied (9 September 2026)

Applied the recommendations of `REVIEW_CLAUDE_weil_depth_20260909.md` to `papers/weil-depth` in the
shifted-zeta-positivity repository (working tree only; not committed).

**Results now certified (N=128, Arb ball arithmetic, no zeta zeros used).** Two-sided enclosures of
λ_min(Q_{0,L}) at seven horizons, sector-wise, with the even ground state certified at each:

| L | floor m | upper bound | odd floor | odd upper | shift | decay |
|---|---|---|---|---|---|---|
| log2 | 1.32e-3 | 1.33e-3 | 7.31e-2 | 7.32e-2 | 4e-2 | 6e-4 |
| log3 | 5.52e-8 | 5.54e-8 | 1.49e-5 | 1.50e-5 | 2e-4 | 2e-8 |
| log4 | 7.48e-13 | 7.57e-13 | 4.71e-10 | 4.77e-10 | 5e-7 | 3e-13 |
| log5 | 8.95e-18 | 9.30e-18 | 9.45e-15 | 9.70e-15 | 1e-9 | 4e-18 |
| log6 | 5.93e-23 | 7.33e-23 | 1.07e-19 | 1.36e-19 | 3e-12 | 2e-23 |
| 9/5 | 3.38e-23 | 4.14e-23 | 5.73e-20 | 7.23e-20 | 2e-12 | 1e-23 |
| log7 | 1.37e-28 | 6.81e-28 | 4.78e-25 | 1.57e-24 | 4e-15 | 6e-29 |

Independent implementation reproduces all seven; all-entry cross-checks pass; the log5 row reproduces
Zhu's floor 8.9e-18 at total length 1.6.

**Manuscript v0.3 changes.** Theorem 1.1 consolidated with Tables 1–2; Lemma 3.3 + full proof of
Prop. 3.4 (weighted Laplace line); Remark 4.2 (Weber–Schafheitlin sharpness); Theorem 6.1 (all seven
horizons) and Prop. 6.2 (upper bounds, even ground state); related work rewritten (Yoshida 1992,
Connes–Consani 2021, Zhu 2026); §7.2 quantifies N needed at log8 (~310), log11 (~950), log13 (~1900),
log16 (~4400), L→3 (~27,000); recursion algebra moved to Appendix B; acknowledgment lists both assistants.

**Package.** New `numerics/enclose_certificate.py` (sector bisection + ball Rayleigh upper bounds +
exact continuation constants) and `make_tables.py` (tables generated from JSON with consistency
asserts); `compare_implementations.py` extended to all pairs; `independent_arb.py` empty-sum fix at
log2. New archives for log2–log6 (~65 MB); independent archives kept for 9/5 and log7 only.

**Folder layout.** Top level = current draft only (README, STATUS, CONTINUATION, BUILD_RECORD,
SHA256SUMS, finite_horizon_weil_v0.3.pdf, manuscript/, numerics/). `archive/README.md` indexes
`archive/drafts/v0.1_2026-09-09`, `archive/drafts/v0.2_2026-09-09`, `archive/reviews/2026-09-09_review-of-v0.1_codex`,
`archive/reviews/2026-09-09_review-of-v0.2_claude`, `archive/background/`.

**Open for Teddy.** Author line still "Edward Baker" (repository convention elsewhere is
"Edward B. Baker III"); Yoshida bibliographic details (pp. 281–325) to double-check; commit when satisfied.
Next experiment: log 8 at N=512, M≈300, ~2300 bits (CONTINUATION.md).

## Addendum (later on 9 Sept 2026): large files removed from git

Decision: ball-matrix archives are deterministic builder output and are not versioned. They were
moved to `papers/weil-depth/numerics-archives/` (gitignored; 122 MB: seven central archives, two
independent archives, the v0.1 package ZIP), with their own README and SHA256SUMS; Teddy intends to
move that folder off the repo (possibly to his own machine). Certificates now carry
`matrices_content_sha256` (hash of the four ball matrices + run parameters, independent of
timestamps/runtime/bounds); rebuilds under Python 3.10/3.11/3.12 give identical content hashes at 9/5
and log7. Scripts fall back to `$WEIL_ARCHIVES/<relative path>` when an archive is absent. The v0.1
package's small contents were extracted to `archive/drafts/v0.1_2026-09-09/package/`. Plan: commit the
removal on `finite-horizon-weil`, squash-merge into `main` (which contains no heavy blobs), delete the
branch locally and on GitHub so the blobs become unreachable.
