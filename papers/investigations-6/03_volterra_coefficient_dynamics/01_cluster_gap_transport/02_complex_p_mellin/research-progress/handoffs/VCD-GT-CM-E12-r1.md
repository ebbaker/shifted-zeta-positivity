# VCD-GT-CM-E12 r1 — Analytical manuscript production

18 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex
LLM assistance. Actual root model/effort unavailable in the guarded registry.
Requested section authors gpt-6.1-sol/ultra; independent serving attestation
unavailable. Type E, fixed integration of established analytical results.

Author request: create a coherent, systematic analytical draft within CM,
citing the base VCD manuscript and predecessor folders as background. Write
editable sources in CM/manuscript, no snapshot folder. Save the reading PDF
in repository-root output/pdf/vcd-complex-p-mellin, ignored by Git. The lead
owns main.tex, framework, comparison/transport, discussion, bibliography,
build, source map, document updates, progress and history. Existing proofs
and predecessor manuscripts remain unchanged. No new numerical campaign.

Narrative contract: begin with the canonical heat field and counted pair,
state exactly the inherited strip/count/product/safe-line assumptions, derive
regular symmetric coordinates and rational contour moments, then derive the
complete integer S/T hierarchy, explain split-pole coordinates and the merger,
then extend to local complex powers and exact symmetry/defects, establish the
damped p-contour evolution with full errors, and finally compare signed
bounds and derive the conditional Riccati/gap consumer. The exact quartic and
static changed-divisor examples are analytical results, not numerics. Keep
proved formulas separate from a new signed estimate; no RH/collision result,
finite closure, arbitrary-sequence well-posedness or complex-p analytic
continuation beyond the proved domain is added.

Use a theorem/proof exposition for a mathematical reader, not a packet log.
Keep audit metadata, hashes and live task labels out of scientific exposition.
State citations to inherited inputs where used. Main bibliography keys made
available by the lead: BakerBase, BakerGT41, BakerGR02, BakerGR05, BakerGR07,
BakerCM03, BakerCM04, BakerCM05, BakerCM06, BakerCM08, BakerCM09, BakerCMReview,
DLMF, Voros2014. Do not import a new literature theorem. Local source IDs are
provenance, not substitute proofs. Full TeX section drafts use standard
amsmath/amsthm, theorem/lemma/proposition/corollary/remark/definition environments.
Available macros: \e, \ii, \dd, \R, \C, \N, \Cu, \Log, \Res, \cC.

## Disjoint authoring packets

**E12a, integer derivation** (input_audit): write only
manuscript/sections/02_integer_hierarchy.tex,
manuscript/sections/03_split_poles.tex and handoffs/VCD-GT-CM-E12a-return-r1.md.
Develop the full finite divided-difference derivation, every endpoint/diagonal
cancellation, canonical fixed-order passage, low-order S1/S2/T2 laws, mixed
basis reduction and full mixed/axis recurrence. Derive the exact quartic and
coordinate cusp, retaining canonical versus polynomial scopes. Reuse the
framework labels eq:domain, eq:count-safe, eq:pairlaw, prop:trace,
lem:slice-passage, which the lead supplies. Define sections sec:integer,
sec:split, theorem thm:hierarchy and eq:S-hierarchy, eq:T-hierarchy,
eq:low-orders. Other labels prefix int: or split:. About 350-500 TeX lines
if needed; completeness and coherence take priority over a rigid count.

**E12b, complex-power analysis** (time_law): write only
manuscript/sections/04_complex_powers.tex,
manuscript/sections/05_cauchy_evolution.tex,
manuscript/sections/08_analytic_constants.tex and handoffs/VCD-GT-CM-E12b-return-r1.md.
Derive branch atlas with merger/transition corrections, complete p/time law,
Schwarz identity and exact negative-axis weighted defect, both p contours,
complete N/Y/X error ledger and differentiated kernel. Retain local 2m²,
both verticals, all spatial connectors and the distinction of divisor values
and independent derivative domination. State exact normalization and domains.
Use appendix file 08 for detailed contour constants/clearance and tail proofs
so main flow is readable, but every main assertion must route to its proof.
Labels sec:complex, sec:cauchy, thm:complex-time, thm:damped-cauchy,
eq:complex-time, eq:forcing-contour, eq:vertical-tail; other labels prefix
cp:, cau: or app:. Main framework labels as above. Fixed damping and fixed
real edges only. No purported finite complex-p closure. About 450-650 TeX
lines across files if needed; do not compress away a required proof.

Each helper gets one production pass and up to two bounded consistency repairs.
Verify pins and source domains. Neither helper builds the final PDF or edits
shared files. Root reads/integrates both; E13 provides nonauthor manuscript
assessment after a frozen source manifest. E14 handles final render, document
reconciliation and next-session continuation. A needed new mathematical claim
returns to the lead for a separate B decision rather than being invented.

## Frozen analytical input SHA-256

- `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/notes/03_VCD_GT_CM_E02_COMPLEX_POWER_TIME_LAW_20261117.md`: `266a33ee15cfc8a8383005508ceb086a65d5f6b41628f9217c882db9194429cc`
- `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/notes/04_VCD_GT_CM_E08_CONJUGATION_AND_BRANCH_DEFECT_20261117.md`: `22dbde73daed6345a8824582e2b2d151481852ee861943d95f33b6134f9057b1`
- `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/notes/05_VCD_GT_CM_E03_DAMPED_CAUCHY_EVOLUTION_20261117.md`: `9e5264cfffa90d5d1e3d58d94ffe1bb9000b56bdf158a760e58c510fbbf9e21f`
- `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/notes/06_VCD_GT_CM_E05_SIGNED_FORCING_COMPARISON_20261117.md`: `68fa056dff54cdc78f3dcbb55935906b0f3b9b383746697374ccbcb6d1228d03`
- `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/notes/08_VCD_GT_CM_E09_SPLIT_POLE_INTEGER_HIERARCHY_20261118.md`: `b1a79a47972731bab2262c7d354076e83da8db850a0818b4074d057b9d9fffc6`
- `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/notes/09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md`: `8b440a2683515ad4f8f366bf91f78bc7e8cae986feaf6e194f33f4741aa7ff8f`
- `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/reviews/03_VCD_GT_CM_E04_CONTOUR_PROOFS_ASSESSMENT_20261117.md`: `4e2a8724f40d0617d40d089e5974a011449882aa9fd947c98642da4a140b10d9`
- `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/reviews/04_VCD_GT_CM_E06_SIGNED_BOUND_ASSESSMENT_20261117.md`: `f390411b838548b35fc7e088ba3b7eac7e1255b50a28c60ed28140b5d42aec4e`
- `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/reviews/05_VCD_GT_CM_E11_INTEGER_CLOSURE_ASSESSMENT_20261118.md`: `9b4331974a693acabdc677f24ea3d7970ab817c827cfbd55289ebbd1118be7b6`
