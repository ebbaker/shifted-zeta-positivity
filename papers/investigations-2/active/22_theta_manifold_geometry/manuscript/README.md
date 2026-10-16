# Manuscript

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**.

[Theta manifold geometry and signed heat-flow collision control](theta_manifold_geometry.tex) is the stable editable manuscript, drafted for Edward Baker. Its 56-page reading copy, built into the repository-root `output/pdf/` folder (ignored by git since 16 October 2026; the research links inside the PDF are relative to that folder), includes the complete local backward stationary locus, scalar signed criterion, invariant joint trace, and the arithmetic continuation. Section 12, pages 45–50, gives the multiplicative theta identities, explicit uniform moment remainder, complete transformed lower intervals and primitive edges, and the nonlocal boundary obstructions. Earlier geometric and control results remain in place.

The [current review](../reviews/15_ARITHMETIC_MANUSCRIPT_INTEGRATION_REVIEW_20261015.md), [integration manifest](../numerics/ARITHMETIC_MANUSCRIPT_INTEGRATION_CHECKS_20261015.json) and [build record](BUILD_RECORD.json) identify the final source/PDF and verification. Both compilers succeed without remaining warnings or overfull/underfull boxes. All 56 final pages were visually inspected, and the arithmetic checker passed 47 exact assertions. Infinite identities and analytic limits retain their separate proofs. The theta-specific all-event signed trace estimate remains open.

The source is standalone and uses standard LaTeX packages. Open it in the desktop LaTeX editor for source and live preview. For a terminal rebuild from the repository root:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/theta-manifold-build \
  papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
```

Review the PDF before replacing the reading copy in `output/pdf/` and update its build identity. Keep build intermediates outside the repository. [Draft history](../DRAFT_HISTORY.md) indexes milestones without new snapshot folders.

The [latest handoff](../notes/00_research_coordination/13_ARITHMETIC_MANUSCRIPT_INTEGRATION_AND_HISTORY_20261015.md) records this integration and the chat-history audit. The compact-surface direction remains parked. The [separate positive-tail pilot](../notes/00_research_coordination/11_SCALAR_MANUSCRIPT_AND_POSITIVE_TAIL_CONTINUATION_20261015.md) remains incremental research. Earlier manifests retain their historical identities.
