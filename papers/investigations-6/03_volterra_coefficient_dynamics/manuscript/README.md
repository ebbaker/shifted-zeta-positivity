# Jacobi dynamics and signed quadrature error for the Newman heat flow

**Analytical draft, expanded 16 November 2026.** Edward Baker, with
substantial OpenAI Codex LLM assistance. The actual model and reasoning
effort for this integration are unavailable in the recorded configuration.
The earlier 14 November drafting dispatch was gpt-6.1-sol / ultra;
that historical setting is not attributed to the present integration.

[Editable master](main.tex) includes the analytical files in
[sections/](sections/). The current
[reading PDF](../../../../output/pdf/volterra_coefficient_dynamics/volterra_coefficient_dynamics.pdf)
is generated under the repository-root ignored output folder. It is not
a versioned manuscript artifact. See the
[integration and reading guide](../notes/25_VCD_ANALYTICAL_READOUT_MANUSCRIPT_INTEGRATION_20261116.md),
[fixed-zero discussion](../notes/26_VCD_FIXED_ZERO_STABILIZATION_AND_PHASE_20261116.md),
[cluster and heat-collision discussion](../notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md),
[current same-assistant assessment](../reviews/11_VCD_CLUSTER_RESOLUTION_ASSESSMENT_20261116.md)
and [current build record](../numerics/14_VCD_CLUSTER_RESOLUTION_MANUSCRIPT_BUILD_20261116.json).
The earlier integration and build records remain historical.

## Reading route

- **§§1–2:** variables, source probability, normalization and polynomial basis.
- **§5:** finite readouts, exact moments, spectral versus Fourier zeros,
  and the Christoffel–Darboux explanation of polynomial phase.
- **§6:** omitted-tail memory and the bilinear midpoint identity.
- **§§7–8:** the complete error law, its moments and explicit complex phase bound.
- **§§9–10:** directed error geometry, conditional zero counts, consecutive
  degrees and the local zero-displacement lemma. §10.1 explains phase
  through the circle example; §10.3 derives fixed-zero stabilization and
  the alternating displacement ratio (10.8)–(10.9).
- **§10.4:** convergence uniform on compact heat-time intervals,
  contour moments of unresolved pairs, and quantitative resolution near
  a fixed isolated double collision. §5.3 explicitly distinguishes the
  polynomial phase from the contour phase that counts zeros of F.
- **§11:** all-degree source characterization, control scopes and reference routes.

The coefficient evolution and confinement proofs remain in §§3–4.
The fixed-initial-chain heat estimate is now Appendix A.
No numerical quantity is used as a premise in these proofs.
No canonical zero-confinement theorem or successful contour family is claimed.

## Build a reading copy

From this manuscript directory, with pdfLaTeX and latexmk installed:

~~~sh
vcd_output_dir="$(git rev-parse --show-toplevel)/output/pdf/volterra_coefficient_dynamics"
mkdir -p "$vcd_output_dir"
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$vcd_output_dir" -jobname=volterra_coefficient_dynamics main.tex
~~~

Alternatively, use an absolute temporary output directory outside the
repository. The 16 November checked build used
/private/tmp/vcd-cluster-resolution-20261116 for intermediate files and copied
the finished PDF to the ignored location linked above. The source has no
numerical or external data-file dependency. PDF metadata may differ on
recompilation; build hashes identify one reading copy, not a proof.
Follow [LARGE_FILES](../../../../LARGE_FILES.md), especially rule 8.
