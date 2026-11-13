# RSCT analytical manuscript

12 November 2026, America/New_York. Drafted for **Edward Baker** with substantial OpenAI Codex LLM assistance. Actual backend model and reasoning effort are unavailable in the recorded session configuration; neither is inferred.

**Status: analytical synthesis of RSCT R1–R9, with source evidence levels preserved; same-assistant checking only.** No new canonical sign, zero-exclusion region, independent provider audit, or executable RSCT-E01 method is claimed.

**Riemann–Siegel analysis at a possible positive Newman threshold: Complete local approximation, signed zero measurements, and the limits of calibrated phase constraints.**

- [External PDF reading copy](/private/tmp/rsct-manuscript-20261112/riemann_siegel_critical_time.pdf).
- [Editable main source](main.tex), [analytical source catalog](SOURCES.md), and [build script](build.sh).
- [Same-assistant synthesis review](../reviews/10_RSCT_ANALYTICAL_MANUSCRIPT_SELF_CHECK_20261112.md).
- [Small build and verification record](../numerics/RSCT_MANUSCRIPT_BUILD_RECORD_20261112.json).
- [Rewritten comparison and proposed questions in GNP-RS](../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/brainstorm/external/01_RSCT_MANUSCRIPT_COMPARISON_AND_PROPOSED_QUESTIONS_20261112.md).

The manuscript develops the finite event and exact reflected representation, fixed-height scalar and matrix measurements, the microscopic complete approximation, signed phase constructions, growing prime calibration, and the joint mirror condition. Section 10 ends the analytical development with outstanding tasks. Source notes and earlier reviews remain the historical proof record.

The [result index](../../../../result-summaries/README.md), [cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), and [avoid index](../../../../avoid/README.md), particularly [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md), remain controlling context. This is a synthesis milestone, not closure of the investigation.

## Build outside the repository

From the repository root:

    sh papers/investigations-5/10_riemann_siegel_critical_time/manuscript/build.sh

The default output directory is /private/tmp/rsct-manuscript-20261112. To choose another external directory:

    sh papers/investigations-5/10_riemann_siegel_critical_time/manuscript/build.sh /absolute/external/directory

Requirements are Python 3, latexmk, and pdfLaTeX with standard TeX Live packages. The script resolves the output path, rejects any location within the repository, and sends the PDF and all auxiliary build files to the external directory. It also handles the standard macOS TeX installation path.

This implements the user’s instruction to keep the PDF entirely outside the repository and [LARGE_FILES.md §1.8](../../../../LARGE_FILES.md). No manuscript snapshot directory is created. The temporary reading copy may be removed by system cleanup; regenerate it from these sources when needed.

The PDF’s internal links to repository sources use the local checkout in the main source’s RepoRoot definition. If building in another checkout, update that definition to the new absolute checkout location. This affects local navigation, not the mathematics or external citations.

## Main results to locate

| Manuscript location | Result |
| --- | --- |
| [§2](sections/01_scope_and_geometry.tex) | Inherited finite attainment; reflected Poisson sign; full value/derivative errors |
| [§3](sections/02_complete_representation.tex) | Exact evolved representation; named buffered approximation input with full correction |
| [§4](sections/03_fixed_height_measurements.tex) | Signed three-height cap, negative background, sign-changing kernel, matrix cap |
| [§5](sections/04_microscopic_acquisition.tex) | Fixed-order moments, Theorem 5.2 local approximation, event subtraction, signed-error payment |
| [§6](sections/05_phase_geometry.tex) | Full quadratic form, disk example, three-circle lemma and exact-circle construction |
| [§7](sections/06_multiplicative_calibration.tex) | Theorem 7.1 uniform calibration budget; Corollary 7.3 growing actual-prime range |
| [§8](sections/07_mirror_jet.tex) | Exact carrier cancellation, fourth-jet errors, Theorem 8.1 simultaneous signs |
| [§9](sections/08_controls_and_provenance.tex) | Exact threshold controls, scope table, source crosswalk and numerical role |
| [§10](sections/09_outstanding.tex) | Actual phase sign, stronger conditions, Green transfer, domain coverage and audit tasks |
