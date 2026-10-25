# HDA-10-MI1 revision 1: integration and production assessment

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**.
Model and effort were read from this session's turn metadata.
Chat 0008, thread `01a17083-259a-7e01-b9d4-c61004237da7`.

This is manuscript production and source-fidelity assessment. It is not
a new mathematical derivation, a mathematical audit, an independent
specialist review, or numerical evidence for the theorems. The source
research retains its Astra attribution and same-assistant review status.

## Request and frozen inputs

Implemented [HDA-10-MI1 r1](../notes/MANUSCRIPT_INTEGRATION_FOR_SOL_20261024.md)
against its [input manifest](../notes/MANUSCRIPT_INTEGRATION_INPUTS_20261024.json).
All ten baseline TeX hashes, the build script and baseline build record
matched the manifest before edits. Notes 25--28 and 30 and Reviews 09--12
also matched their frozen hashes and were read for transcription. Their
hashes were checked again after the build; none was changed. Later
positive-evolution research, including Note 31, was expressly deferred by
the author. The live ledger's newer HDA-16/HDA-19 statuses were preserved.
The prior 28-page export and its source hashes are historical provenance
in the refreshed [build record](../manuscript/BUILD_RECORD_20261024.json).

Required context: [result index](../../../../result-summaries/README.md),
[heat-flow cluster 13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[control screen 12](../../../../result-summaries/12_collision_controls_and_screening.md),
[avoid index](../../../../avoid/README.md), particularly
[classification](../../../../avoid/01_restating_the_target.md),
[scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status synchronization](../../../../avoid/19_status_files_that_lag_the_findings.md).
This revision consolidates quantitative approximation estimates with their
existing domains; it supplies no new RH or simplicity criterion.

## Integrated source coverage

| Source groups | Manuscript placement and retained contract |
| --- | --- |
| Note 25 OH2--OH11 | `04_geometry_global.tex`: explicit complete-contour jet constants, both vertical ends, all theta modes, pre-switch physical observable/current/time/forcing/traces and actual Q/Delta Q tails, explicit density threshold. |
| Note 25 OH13--OH17 | `08_finite_time.tex`: fixed-positive-cutoff asymptotic, all cell derivative jumps/end derivatives, full off-axis buffer, absolute physical-potential obstruction and exact excluded class. The older fixed-buffer large-time obstruction remains. |
| Note 26 NE1--NE24 | `02_negative.tex`: exact negative regulator, source jets through four, direct finite evolution budgets, composition constants through the fifth scalar derivative, differentiated forcing and actual covariance cancellation, Gaussian equations and full-buffer traces. |
| Note 27 GO4--GO26; Note 28 JT10--JT21/JT18a | `11_gamma_outer_switch.tex`: exact xi/8 convolution and gamma factor 1/16, both reflected arms, four field-error payments relative to carrier sum, physical simple-root collars, arbitrary-positive-q transfer, static U/W jets through four and both regulator regimes. |
| Note 27 GO27--GO33; Note 28 JT22--JT33 | Same section: exact finite Bernoulli phase, separate compact/joint/continuum rates, O(1) absolute two-layer error, exact linear-model switch center, width and rescaled law, direct derivative payments and fixed-time nonuniform limit. |
| Note 28 JT34--JT36 | Same section: exact nonzero linear-model residual; its exponential joint threshold is a historical limitation of that model. |
| Note 30 FS3--FS20 | `12_full_gamma_saddle.tex`: specified implicit branch, fixed sector/determinant, both arms/connectors, whole-half-line majorant, cubic payment, middle, every arithmetic mode and the three-part field budget. |
| Note 30 FS21--FS31 | Same section: actual collars, unchanged-q transfer, complete-source mass anchor after the field proof, static spatial jets, all three uniform limits and actual same-time inner overlap. |
| Note 30 FS32--FS34 | Same section: direct implicit time/spatial derivatives and exact nonzero full-saddle residual, including sign, 1/16 and 5/64 coefficients. |

`10_global_protocol.tex` consolidates the existing kernel, real saddle,
positive and global regulators under their original labels; `01_framework.tex`
adds the static holomorphic weak identity without imposing a heat
hypothesis. Existing fixed-regulator theorems, inner-clock transport gates,
finite-source estimates and `09_local_transfer.tex` were retained. The
last file is byte-identical to the baseline. `14_scope_and_remaining_work.tex`
records each domain, target, rate and theorem and distinguishes spatial
matching from finite-heat-time joining. The abstract, roadmap, source
crosswalk, manual bibliography and preparation attribution now agree.
Notes 24/29 remain history; the integration specification is editorial.

Source-to-TeX checks retained physical potential offsets, common q,
t=-T sign, normalizations 1/8 and 1/16, exact covariance and adaptive
terms. Section transcriptions were cross-read within the Sol production
team. One missing joint-range error in the summary table was found and
corrected to match the already correct theorem. No unresolved analytical
source issue was identified by this fidelity check. This finding does not
validate the source proofs independently.

The complete-source contour application requires canonical even
reflection and its coefficient envelope; the gamma application requires
the unchanged xi completion/reflection and full ordinary Dirichlet
series. Existing control families are screened against those premises;
generic rational-map/covariance bounds remain applicable to other fields
with their own constants. No control numerics were rerun. Local simple
root collars are not a global multiple-event exclusion. Regularized
layers are not nonreal zeros.

## Actual production checks

The prescribed repository-root command succeeded:

```sh
python3 -B papers/investigations-5/01_heat_density_asymptotics/manuscript/build.py
```

The final reading copy is **54 pages**, **710538 bytes**, SHA-256
`e8d0a288f15e3122c1acce461bcd95aef69a7743893044fcf9d06852a8d36f81`.
It is at the ignored
`output/pdf/heat_density_asymptotics/heat_density_asymptotics.pdf`.
The build driver still detects the checkout root. No PDF or auxiliary
was placed beside the manuscript, no new snapshot folder or numerical
run was made, and no commit, push, release or publication was performed.

- All 14 TeX files and build.py are hashed in the refreshed record.
- Final log: zero LaTeX/package warnings, zero overfull/underfull boxes.
- Source scan: no duplicate labels, unresolved labels or citations; PDF
  text has zero literal question-mark references.
- All 39 local PDF file links resolve; all named internal link destinations
  resolve. The five external primary URLs were opened successfully;
  DLMF24.8.E3 resolves to its section. This is a link check, not a new
  full-paper review or bibliography-driven theorem extension.
- All 54 pages were rendered at 100 dpi to temporary PNGs and inspected in
  six contact sheets. Individual readable-page inspections covered pages
  10,11,23,31,33,35,37,39,40,43,45,47,48,51,54. Long displays,
  proof continuations, the two-page coverage table, crosswalk, bibliography
  and hyperlink text show no clipping, overlap, missing symbols or
  material layout defect. Two long displays were reflowed and tables made
  ragged-right before the final build. A missing logarithm typesetting
  macro was corrected; no mathematical coefficient was changed.
- Final changes and sizes were inspected; tracked text and records remain
  below 1 MiB, and the generated PDF is ignored. Unrelated worktree changes,
  source research, existing diagnostic failures and chat identities remain.

The build record contains the exact export hash and source versions.
Production checks do not support an asymptotic onset or prove theorems.

## Disposition and next task

HDA-10-MI1 r1 is complete at the author-frozen scope through Note 30.
The old 192-cell trial remains unaccepted. HDA-17 acceptance, HDA-18
all-time assembly and HDA-20 distinct/specialist review are not advanced
by typesetting. No autonomous density/covariance closure, certified
onset, RH result or earlier-time simplicity conclusion is asserted.
Positive evolution established subsequently in Note 31 remains outside
this manuscript version, without rolling back its live research status.

**Next: Analytical — Astra.** Produce HDA-17/HDA-18's finite-core and
joining error contract using Notes 26/30/31, with complete height
coverage, actual adaptive/residual/covariance terms and informative
source/jet input. The live ledger contains no decision-ready numerical
packet, so no new numerical assignment is proposed.
