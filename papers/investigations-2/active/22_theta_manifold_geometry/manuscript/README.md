# Manuscript

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**.

[Theta manifold geometry and signed heat-flow collision control](theta_manifold_geometry.tex) is the stable editable draft, written for Edward Baker. Its [31-page reading copy](../../../../../output/pdf/theta_manifold_geometry.pdf) contains the full narrative, proofs, references and LLM acknowledgment.

The integrated development emphasizes the fixed-endpoint chord exclusion theorem, sharp starting-energy threshold and cutoff transfer. It retains the physical jet geometry and source constructions, and adds complete bilocal identities, ASD metric freedom, the weighted-square collision control and reflection rigidity. The contour pilot is summarized with links; other exploratory proposals are assessed in [Overview 02](../research-overview/02_CHORD_CRITERION_AND_ARITHMETIC_BRIDGE_20261015.md). The theta-specific inequality and full domain coverage remain open.

The [integration review](../reviews/04_MANUSCRIPT_INTEGRATION_REVIEW_20261015.md) and [build record](BUILD_RECORD.json) state the current checks and limitations. All 31 rendered pages were individually inspected. The final export has no compiler warnings or overfull/underfull boxes. Existing computation manifests retain their historical identities; no new sign certificate is claimed.

The source is standalone and uses standard LaTeX packages. Open it in the desktop LaTeX editor for an editable source and live preview. For a terminal rebuild, from the repository root:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/theta-manifold-build \
  papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
```

Review the resulting PDF before replacing the reading copy, and update the build identity. Build intermediates belong outside the repository. Maintain [DRAFT_HISTORY.md](../DRAFT_HISTORY.md); future milestones should identify commits or tags without creating manuscript snapshot folders.
