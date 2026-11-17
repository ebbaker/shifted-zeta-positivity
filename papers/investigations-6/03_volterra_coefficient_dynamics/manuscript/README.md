# Jacobi dynamics, signed error, and cluster transport for the Newman heat flow

**Analytical draft, expanded 17 November 2026.** Edward Baker, with
substantial OpenAI Codex LLM assistance. Actual lead model and reasoning
effort for this integration are unavailable in the recorded configuration.
Fixed section and assessment helpers were dispatched gpt-6.1-sol / ultra,
without separate backend attestation. Review is internal, with shared
inherited premises and contributor overlap; no specialist review is claimed.

[Editable master](main.tex) includes the analytical files in [sections/](sections/).
The [75-page reading PDF](../../../../output/pdf/volterra_coefficient_dynamics/volterra_coefficient_dynamics.pdf)
is generated under the repository-root ignored output folder.
[GT Integration43](../01_cluster_gap_transport/notes/43_VCD_GT_RECENT_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261117.md)
maps the analytical results through fixed-collar occupation and exact
interaction dynamics. [Assessment20](../01_cluster_gap_transport/reviews/20_VCD_GT_E24_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261117.md)
records the separate integrated internal assessment; its author contributed
to no manuscript section. [Session24](../01_cluster_gap_transport/numerics/24_VCD_GT_RECENT_ANALYTICAL_MANUSCRIPT_BUILD_20261117.json)
records source preservation, bounded corrections, build and visual checks.
[Scientific continuation42](../01_cluster_gap_transport/notes/42_VCD_GT_B11_FIXED_COLLAR_SYNTHESIS_20261117.md)
routes the unactivated B12 question. Earlier integration notes, assessments
and build records remain historical.

## Reading route

- **§§1–4:** variables, complete source, normalization, polynomial basis,
  moving Jacobi evolution and coefficient confinement.
- **§§5–6:** Gaussian quadrature, spectral versus Fourier zeros, polynomial
  phase, omitted-chain memory and the intermediate-mode identity.
- **§§7–9:** entire signed error law, explicit concentration/phase bound,
  directed enclosures and equal-coefficient comparisons.
- **§10:** fixed-zero stabilization, contour coordinates and conditional
  resolution through a fixed isolated double event.
- **§11:** all-degree canonical-score characterization, control scopes,
  and the transition from approximation to zero geometry.
- **§12:** uniform physical-time error, regular gap law, both-coordinate
  and drift transfer, actual Jacobi heat defect, joint signed transport,
  paid time errors and matched envelopes.
- **§13:** fixed-event uniqueness and signed shift, critical-scale
  cancellation, directly calculated deflation kernel and shorter-slab
  next-head comparison.
- **§14:** Laurent source formula, scoped separate-tail failure,
  order/strip/product derivation, sharp exterior weights, real-bracket
  lower counts, full-time moving boundary signs and exact quartic control.
- **§15:** uniform projected counting through time zero, signed far-tail
  asymptotic, microscopic normalization and identical-count sign controls.
- **§16:** convex heat balance, source transverse density and moments,
  exact radial comparison and center averages, isolated-pair counts and
  fixed-collar negative pair-time occupation.
- **§17:** exact exterior-interaction evolution through multiple roots,
  complete shell bounds, conditional Riccati and integrated-cost allowances,
  and the limits of converting occupation to a slice count.
- **§18:** normalized deflated curvature and Fourier numerator; finite
  Gram and separate-mode obstructions; complete-source optimal favorable-phase
  allowance, anti-diagonal expansion and scoped averaging failure.
- **§19:** selected-pair signed information, forcing, visibility, tube and
  incoming-data acquisition, joint Fourier phases, larger clusters and
  uniform-family challenges.
- **Appendix A:** fixed-initial-chain heat estimate.
- **Appendix B:** analytical source-evaluation, interpolation and contour
  bounds, extended majorants for moving boundary centers, then supporting
  local numerical certificates.

The mathematical assumptions and scope accompany each result. The fixed
tube numerical corollaries are explicit supporting instances. No global
zero-confinement theorem, new Newman bound or exclusive transport gain is claimed.

## Build a reading copy

From this manuscript directory, with pdfLaTeX and latexmk installed:

~~~sh
vcd_build_dir="$(mktemp -d /private/tmp/vcd-reading-XXXXXX)"
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$vcd_build_dir" -jobname=volterra_coefficient_dynamics main.tex
~~~

Inspect the PDF before copying it to the ignored output location above.
The current E23 build uses /private/tmp/vcd-gt-e23-20261117-build for
intermediates. Session24 records the final page count, hashes and all-page
visual checks, together with the reference, citation and box-warning checks. The source
has no numerical data-file dependency. PDF hashes identify one reading
copy, not a mathematical proof. Follow [LARGE_FILES](../../../../LARGE_FILES.md).
