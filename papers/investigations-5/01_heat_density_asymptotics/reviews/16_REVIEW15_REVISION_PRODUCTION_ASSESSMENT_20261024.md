# Review 15 revision: manuscript production assessment

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from this turn's session metadata. Chat 0008, thread
`01a17083-259a-7e01-b9d4-c61004237da7`.

Implemented the author's request to incorporate
[Review 15](15_MANUSCRIPT_REVIEW_AND_SOL_RECOMMENDATIONS_20261024.md),
including its required correction and all recommended additions.
This is a subsequent revision beyond completed HDA-10-MI1 r1.
Its frozen request, input manifest and [Review 14](14_MANUSCRIPT_INTEGRATION_PRODUCTION_REVIEW_20261024.md)
remain unchanged. Review 15's [input manifest](15_MANUSCRIPT_REVIEW_INPUTS_20261024.json)
matched all reviewed files, the 54-page export and the build record at
intake. Source notes and existing reviews were not rewritten. Later
Note 33 intake/handoff material in the live ledger was preserved.

This is source-fidelity checking, editing and PDF production, not a new
analytical derivation, independent mathematical audit or numerical
validation. Notes 30--31 and their original reviews retain their Astra
attribution and **proved in-note; same-assistant review only** status.
Review 15 was also written by the assistant that derived those sources.
The Sol production team cross-read transcriptions against the sources;
no unresolved transcription discrepancy was identified. That statement
is not a correctness certificate for the mathematics.

## Implemented changes

- Exactly three complete-source derivative-bound occurrences in
  `09_local_transfer.tex` now use `B_2^Phi`. The cell bounds `B_i`,
  composition budgets `B_m` and centered moments `B_j(Y)` retain their
  own meanings. No underlying interpolation inequality changed.
- New `13_positive_evolution.tex` follows the full saddle and integrates
  Note 31 PE1--PE44 with its proof mechanisms and exact derivative orders.
  Static U/W jets through four and density/curvature jets through two
  retain `C e_*`; current, actual Q, direct time and forcing/source
  terms through two have `C e_* mathcal L^2 <= C/sqrt(t)` at late time.
  Compact `[32,T]` outer rates retain separate constants and threshold.
- Cauchy transfer uses full analytic disks; pole/residue/regular-part
  comparisons retain the model root-speed residual. The regulator-uniform
  pole estimate retains `e(1+abs(log e))`; no log(q) or global regulator
  floor is substituted. The tail integral keeps its O(lambda) pole term.
- Direct weak current, exact time identities and the differentiated weak
  density identity retain all regulator terms with maximum kernel order
  four. Actual signed gradient stress is compared before taking bounds;
  squared filtered gradients are then separately paid to obtain Q/Delta Q.
- The exact nonzero full-saddle residual is retained unchanged. Model
  equations contain `+2 Re(K*Z_0)`, `+Delta Re(K*Z_0)/(2 pi)` and
  `+K*D_E`, with both curvature derivatives. PE34's weak residual
  correction is included. Its `C d_*` allowance is separate from the
  source-comparison error.
- Differentiated inner overlap has the coarser absolute rate
  `O(t^-1/2)+O(L kappa^-7/6)`; the sharper independent inner transport
  theorem and its gates remain. Compact-time evolution includes the
  actual flat-switch beta-prime payment and weaker time-error rate.
- Appendix A now gives Note 16 AT2--AT6's finite positive moment,
  variance and E4 formulas, v-prime/m3-prime allowances, recentering
  explanation and L-plus/minus-e_mu gates. Section 5.3 points to them.
- The common protocol contains the requested five-model/domain guide
  and notation key. It links theorems without maintaining a second full
  rate table. The kernel dummy variable is v rather than regulator q.
- Abstract/roadmap, inner and finite-time pointers, full-saddle conclusion,
  detailed coverage table, PE source crosswalk, acknowledgments and actual
  manual bibliography now describe results through Note 31. Note 31 and
  DLMF 1.9.31 are included; the reusable catalog was synchronized. The
  historical Note 30/MI1 scope is identified as historical.

The four diagnostic paragraphs, failed 192-cell trial and earlier proof
scopes are retained. No new numerical evaluator, machine-symbolic run,
plot, parameter search, onset certificate, snapshot, commit, push or
publication was performed. New text is consolidation of the cited sources.

## Production checks and artifact

The prescribed repository-root build succeeded:

```sh
python3 -B papers/investigations-5/01_heat_density_asymptotics/manuscript/build.py
```

Final PDF: **65 pages**, **780970 bytes**, SHA-256
`4fffcad599dbd0e29c4ac76704b5052a13a50e808a5a6443410ceb67664aec95`. The reading copy remains in ignored
`output/pdf/heat_density_asymptotics/heat_density_asymptotics.pdf`;
auxiliaries remain in its `.build/`. The unchanged driver detects the
checkout root. The [current record](../manuscript/BUILD_RECORD_20261024.json)
contains all 15 TeX hashes, script hash, actual export and previous-export
provenance, including the earlier 54-page revision.

- Zero LaTeX/package warnings and overfull/underfull boxes.
- Zero duplicate labels, unresolved source references/citations or literal
  question-mark references in extracted PDF text.
- All 42 local file links and named internal destinations resolve.
  The new official Cauchy URL was opened and equations 1.9.30--31 and
  their contour hypotheses inspected. The other five primary URLs are
  unchanged from the preceding verified build. No new literature claim,
  full-paper review or third-party download was made.
- All 65 pages rendered at 100 dpi and inspected in eight contact sheets
  by the production team. Individual readable inspections covered pages
  7,8,18,19,29,30,48,49,50,52,54,55,56,57,58,59,62,65. The guide,
  theorem tables, long weak/residual displays, coverage/crosswalk tables,
  finite E4 inputs, bibliography and page breaks show no clipping,
  overlap, missing symbols or material layout defect. A justified-table
  spacing warning was removed with ragged-right cells before final build.
- The final source diff, source/export hashes and file sizes were checked;
  new tracked text/records stay below 1 MiB, and the PDF remains ignored.
  Earlier frozen handoff/manifest, proof notes and analytical reviews
  retain their recorded hashes. Unrelated and concurrent work was preserved.

Production checks inspect the artifact; they are not mathematical or
numerical evidence for an asymptotic theorem.

## Disposition and remaining work

Review 15's notation correction, Note 31 integration, finite inner
allowances and early guide are implemented. No analytical discrepancy
remains recorded from source comparison. HDA-17 remains Ready, HDA-18
Gated and HDA-20 Ready without a distinct-reviewer audit. Their research
task rows were preserved. Same-time static/differentiated overlap still
does not provide a finite-time join. There is no autonomous closure,
certified numerical onset, RH or earlier-time simplicity conclusion.

**Next: Analytical — Astra.** Derive the finite-core accuracy and
compatibility estimates consumed by HDA-17/HDA-18 joining, following
[Note 32](../notes/32_CONTINUATION_FINITE_CORE_AND_JOINING_20261024.md) and
the live ledger, preserving all adaptive, residual and actual-covariance
terms. No numerical packet is ready or proposed.

Required context remains the [result index](../../../../result-summaries/README.md),
[heat-flow cluster 13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[control screen 12](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), particularly
[constant/object conventions](../../../../avoid/08_normalization_and_constant_slips.md),
[cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status synchronization](../../../../avoid/19_status_files_that_lag_the_findings.md).
