# Conservation laws and exterior flux: working manuscript

18 November 2026. Author: **Edward Baker**. Draft prepared with substantial
OpenAI Codex LLM assistance. Actual model and effort unavailable in the
guarded chat metadata. Status: **proved in this working draft, with exact
finite algebra checks and same-assistant assessment**; no independent
or specialist review.

The [LaTeX source](main.tex) derives the founding conservation results and
the bounded general homogeneous-flux extension. Its eight sections cover
the physical pair balance, finite coefficient integrals, specialized
Calogero matrix, scoped finite-head obstruction, full-field pullback and
Volterra flux, complete block flux, error comparisons, and collision
controls. The [reference guide](../references/README.md) identifies the
parent/base manuscripts and the actual external reading scope.

Build from the repository root:

```sh
sh papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/01_conservation_laws/manuscript/build.sh
```

The reading PDF and auxiliary files go only to the ignored root directory
[output/pdf/vcd-conservation-laws](../../../../../../../output/pdf/vcd-conservation-laws/).
The PDF is named `conservation_laws.pdf`. Do not copy it into this source
folder or create a manuscript snapshot. The small build/inspection record
in `numerics/` identifies the checked source and output hashes.

The radius factors concern the displayed source-error allowance, not a
total canonical width or cost gain. Root-coordinate uncertainty has an
explicit extra payment; quadrature and whole-time control remain separate.
