# Manuscript

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**.

[Theta manifold geometry and signed heat-flow collision control](theta_manifold_geometry.tex) is the stable editable draft, written for Edward Baker. Its [43-page reading copy](../../../../../output/pdf/theta_manifold_geometry.pdf) contains the full narrative, proofs, references and LLM acknowledgment.

The current integration adds exponential-average cutoff transfer, normalized coefficient recurrence, coupled-source and endpoint-strip identities, exact recurrence-defect stability, the sharp finite positive hierarchy, absorption-current approximation, and signed boundary geometry. New negative findings are summarized with references to detailed notes. The complete-theta signed trace estimate and event coverage remain open.

The [integration review](../reviews/09_RECURRENCE_MANUSCRIPT_INTEGRATION_REVIEW_20261015.md) and [build record](BUILD_RECORD.json) state the current checks and limitations. All 43 rendered pages were individually inspected; changed pages were rechecked after a heading repair. The final export has no compiler warnings or overfull/underfull boxes. Existing computation manifests retain their historical identities; no new sign certificate is claimed.

The source is standalone and uses standard LaTeX packages. Open it in the desktop LaTeX editor for an editable source and live preview. For a terminal rebuild, from the repository root:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/theta-manifold-build \
  papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
```

Review the resulting PDF before replacing the reading copy, and update the build identity. Build intermediates belong outside the repository. Maintain [DRAFT_HISTORY.md](../DRAFT_HISTORY.md); future milestones should identify commits or tags without creating manuscript snapshot folders.

Five relevant checkers passed 12,271 overlapping exact assertions in this integration. The [latest handoff](../notes/00_research_coordination/09_MANUSCRIPT_RECURRENCE_INTEGRATION_AND_NEXT_CHAT_20261015.md) records the next signed-boundary experiment and the current chat-history verification. Earlier manifests retain their historical source, PDF and research-note identities.
