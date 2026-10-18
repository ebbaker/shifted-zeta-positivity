# Positive Arithmetic Packets for the Theta Heat Flow

18 October 2026, America/New_York. Drafted for Edward Baker with substantial
LLM assistance. Revised integration: **gpt-6.1-sol, ultra**, coordinated and
edited by **gpt-6-astra, ultra**. Original development: **gpt-6-astra, max**.

The [canonical LaTeX project](positive_arithmetic_packets/main.tex) now
contains seven sections and compiles to a **30-page working draft**.
It develops theta inversion, finite Euler heat algebra, complete half-line
packets, positive higher-mode carriers, full modular cancellation, scoped
collision controls and cancellation-preserving shifted approximation.
Notes 05–06 are incorporated with complete proofs and quantitative errors.

The main additions are broad complex-strip positivity, the combined
logarithmic derivative budget and **E/64** carrier payment, sharper real
residual jets, a complex-strip relative estimate, and finite shifted-mode
derivative errors. A near-boundary contour gives an asymptotic improvement
relative to a nonzero gamma envelope, without an effective onset or cost
claim. The full signed theta margin remains open. No theta collision
exclusion or new Newman bound follows from this revision.

- [Local reading-copy PDF](../../../../output/pdf/positive_arithmetic_packets.pdf)
  (30 pages, generated under the ignored root output folder).
- [Source and build record](positive_arithmetic_packets/BUILD_RECORD.json).
- [Integration review](../reviews/05_UPDATED_MANUSCRIPT_INTEGRATION_REVIEW_CODEX_20261018.md)
  (internal LLM checks by contributing Sol and Astra assistants).
- [Revised scalar checker](../numerics/certify_updated_manuscript.py) and
  [retained enclosures](../numerics/UPDATED_MANUSCRIPT_CONSTANTS_20261018.json).
- [Updated Sol research plan](../research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md).
- [Overview 02 bounded research continuation](../notes/02_updated_research_plan/README.md):
  finite interval evaluator and signed certificate, assessed internally by
  gpt-6.1-sol at actual effort max on 18 October 2026. These later notes
  are outside the pinned manuscript source set; the global consumer remains
  unclosed.
- [Draft history](../DRAFT_HISTORY.md).

Open the project directory in the built-in LaTeX editor for editable source
and a live preview. A terminal rebuild uses an external build directory;
run twice from `manuscript/positive_arithmetic_packets`:

```sh
mkdir -p /tmp/positive-arithmetic-packets-build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/positive-arithmetic-packets-build main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/positive-arithmetic-packets-build main.tex
```

The source has no external graphics, bibliography database or unpublished
note imports. The collision construction explicitly imports Polymath's
high-zero theorem and the classical zero-strip theorem; the auxiliary
packet estimates do not use these inputs. Preserve this as the current
manuscript, with milestones in the concise draft history and future Git
commits or tags; create no new snapshot folders. Compilation and scalar
certificates are separate from mathematical validation.

## Later analytic supplement

[Note 11](../notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md) improves the
near-boundary arithmetic tail by nonstationary phase, supplies an explicit
uniform onset, and records bounded retained-integral costs. This later
supplement is outside the eight-file manuscript pin above. Its
[Review 10](../reviews/10_EFFECTIVE_NONSTATIONARY_TAIL_AND_POINT_EVALUATOR_REVIEW_20261018.md) is same-model internal assessment,
**gpt-6.1-sol, actual effort ultra**, 18 October 2026, for Edward Baker
with substantial LLM assistance. A future manuscript integration should
replace the historical unevaluated-onset discussion with this proved
estimate while retaining the separate physical-margin obligation.

## Finite consumer supplements

[Note 12](../notes/02_updated_research_plan/12_HIGH_HEIGHT_SIGNED_CONSUMER_AND_MATCHED_COMPARISON_20261018.md) and
[Note 13](../notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md) consume the new tail,
certify a signed box and a complete complex wall, and prove finite-height
noncollision through named imports. They are later supplements outside
the current manuscript pin. [Review 11](../reviews/11_HIGH_HEIGHT_SIGNED_AND_VERTICAL_WALL_REVIEW_20261018.md), for Edward Baker
with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**,
18 October 2026, records the internal review and remaining exterior gap.
