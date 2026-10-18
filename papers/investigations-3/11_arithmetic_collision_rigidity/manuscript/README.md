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
