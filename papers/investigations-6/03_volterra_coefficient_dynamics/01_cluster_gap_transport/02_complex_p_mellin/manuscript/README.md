# Analytical manuscript

18 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI Codex LLM assistance. Actual lead model/effort unavailable in the guarded registry; earlier helpers requested **gpt-6.1-sol / ultra**, current revision helpers inherited settings, without independent serving attestation.

The editable draft is [main.tex](main.tex): **Exterior moment hierarchies and gap transport in the Newman heat flow**.
It is authored for Edward Baker, with an LLM-assistance acknowledgment.
The manuscript belongs to CM, as expressly requested; base VCD and GT/GR
sources are cited background. No predecessor manuscript has been edited.

The reading copy is [complex_power_evolution.pdf](../../../../../../output/pdf/vcd-complex-p-mellin/complex_power_evolution.pdf),
under the ignored root output folder. Generated PDFs and build/render
intermediates are not versioned. No manuscript snapshot folder is created.

## Build

From the repository root, with TeX Live and latexmk available:

```sh
sh papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/manuscript/build.sh
```

The script determines the repository root, sets the bibliography search
path for the shared VCD database, and builds only under
`output/pdf/vcd-complex-p-mellin/`. The local bibliography contains internal
sources; checked external records are reused from the
[canonical VCD database](../../../references/induction.bib). TeX Live's
`plainurl` style retains the primary reference links. Build status, tool
versions, source/output hashes and visual checks are recorded in
[record08](../numerics/08_VCD_GT_CM_RECENT_MANUSCRIPT_BUILD_RECORD_20261118.json);
record05 remains the historical first build.

## Reading order and source map

| Manuscript part | Principal established sources |
| --- | --- |
| 1. Complete source, pair and rational traces | [Base manuscript](../../../manuscript/main.tex); [GT Note41](../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md); [GT assessment19](../../reviews/19_VCD_GT_E22_FIXED_COLLAR_ASSESSMENT_20261117.md) |
| 2. Full integer hierarchy | [CM Note09](../notes/09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md); inherited next moment in [GR Note02](../../01_gaussian_resolvent_hierarchy/notes/02_VCD_GT_GR_E02_CANONICAL_MOMENTS_20261117.md) |
| 3. Split poles, algebraic equivalence and exact quartic | [CM Note08](../notes/08_VCD_GT_CM_E09_SPLIT_POLE_INTEGER_HIERARCHY_20261118.md); [integer assessment05](../reviews/05_VCD_GT_CM_E11_INTEGER_CLOSURE_ASSESSMENT_20261118.md) |
| 4. Finite heads and compatible approximation | [Note15](../notes/15_VCD_GT_CM_B05_BBGKY_TRUNCATION_RECONSIDERATION_20261118.md); full residual/path proofs now separately assessed in [E19](../reviews/10_VCD_GT_CM_E19_RECENT_MANUSCRIPT_ASSESSMENT_20261118.md); the common-time approximation theorem remains open |
| 5. Complex powers, time law and branch defects | [CM Note03](../notes/03_VCD_GT_CM_E02_COMPLEX_POWER_TIME_LAW_20261117.md); [CM Note04](../notes/04_VCD_GT_CM_E08_CONJUGATION_AND_BRANCH_DEFECT_20261117.md) |
| 6 and Appendix A. Damped contours, clearance and N/X/Y errors | [CM Note05](../notes/05_VCD_GT_CM_E03_DAMPED_CAUCHY_EVOLUTION_20261117.md); Note03; [contour assessment03](../reviews/03_VCD_GT_CM_E04_CONTOUR_PROOFS_ASSESSMENT_20261117.md) |
| 7. Signed comparison, static example, conditional transport | [CM Note06](../notes/06_VCD_GT_CM_E05_SIGNED_FORCING_COMPARISON_20261117.md); [CM assessment04](../reviews/04_VCD_GT_CM_E06_SIGNED_BOUND_ASSESSMENT_20261117.md); [GR Note05](../../01_gaussian_resolvent_hierarchy/notes/05_VCD_GT_GR_E06_FORCING_TRANSFER_AND_COST_20261117.md); [GR assessment05](../../01_gaussian_resolvent_hierarchy/reviews/05_VCD_GT_GR_E07_FORCING_AND_SCOPE_ASSESSMENT_20261117.md) |
| 8. Joint forcing, energy and deflated derivatives | [Note13](../notes/13_VCD_GT_CM_B03_JOINT_TRANSPORT_AND_SUPERZETA_20261118.md); [E15 assessment](../reviews/08_VCD_GT_CM_B03_JOINT_TRANSPORT_ASSESSMENT_20261118.md) |
| 9. Backward comparison and regional statistics | [Note16](../notes/16_VCD_GT_CM_B06_CLOSEST_PAIR_SELECTION_20261118.md); [Note17](../notes/17_VCD_GT_CM_B07_REGIONAL_GAP_STATISTICS_AND_BACKWARD_COMPARISON_20261118.md); [E17 assessment](../reviews/09_VCD_GT_CM_E17_REGIONAL_STATISTICS_ASSESSMENT_20261118.md); canonical count in [GT Note33](../../notes/33_VCD_GT_E12_UNIFORM_SIGNED_FAR_EXTERIOR_20261117.md); fixed-blur OC results cited in the bibliography |
| 10. Interpretation and scope | [GR synthesis07](../../01_gaussian_resolvent_hierarchy/notes/07_VCD_GT_GR_SESSION_SYNTHESIS_AND_CONTINUATION_20261117.md); [control summary12](../../../../../../result-summaries/12_collision_controls_and_screening.md); [checked superzeta passages](../references/03_VCD_GT_CM_SUPERZETA_SOURCE_SCREEN_20261117.md) |

Internal bibliography titles route to these source files. They are working
proofs and internal shared-premise assessments, not peer-reviewed literature.
DLMF and Voros are used only at the checked background scope recorded in
CM/references; no new superzeta continuation theorem is imported.

## Production and assessment

The original E12--E14 milestone produced the earlier 25-page draft;
its requests, assessments and build record remain historical. The current
[E18 request](../research-progress/handoffs/VCD-GT-CM-E18-r1.md) integrates
recent analytical results into that same editable manuscript.
[E19 assessment10](../reviews/10_VCD_GT_CM_E19_RECENT_MANUSCRIPT_ASSESSMENT_20261118.md)
accepts the corrected source within its stated domains after three local
definition/scope clarifications, with no formula change. The original and
corrected source manifests identify both reviewed versions.

The final reading copy has **38 pages**, with clean compilation and complete
visual inspection. [Integration18](../notes/18_VCD_GT_CM_RECENT_MANUSCRIPT_INTEGRATION_20261118.md)
records claims, repairs, source preservation and production checks;
[Continuation19](../notes/19_VCD_GT_CM_REGIONAL_STATISTICS_MANUSCRIPT_CONTINUATION_20261118.md)
is the next-session handoff. [Record08](../numerics/08_VCD_GT_CM_RECENT_MANUSCRIPT_BUILD_RECORD_20261118.json)
identifies the source/PDF and rendering. The [sole register](../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md)
owns live status.

The general signed forcing estimate, canonical statistical acquisition and
global reality descent remain open. Finite-divisor approximation is the
independent ready [E16 r2](../research-progress/handoffs/VCD-GT-CM-E16-r2.md)
task, explicitly rebound to the revised framework source without changing
its scientific contract. All predecessor manuscripts and research notes
remain unchanged. Numerics are supporting evidence only; the present proofs
use analytical identities, exact examples and explicit comparisons.
