# Sharp finite-sum bounds: numerics

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

Reproducible code, parameters and small execution records.

The [round-one pilots](round-1/README.md) contain an outward sharp-row
enclosure, the complete new-time approximation budget, a revised infinite
tail budget, an exact generic transfer counterexample, and the completed
four-leg outward transfer-gate implementation. Prepared for
Edward Baker with substantial LLM assistance, 17 October 2026,
**gpt-6.1-sol (Codex)**, effort **ultra**. No complete Newman certificate
has been produced.
Before each run, state the question, domain, baseline, accuracy, resource
limit and stopping answer. Distinguish floating diagnostics from
outward-rounded certificates. Record parameters, environment and actual
model/effort; a replay or hash does not prove the mathematical implication.

Follow [LARGE_FILES.md](../../../../LARGE_FILES.md). Keep regenerable large
outputs external, with a tracked guide and small hash-bound records when
first needed; no large archive is created by this setup.

Update, 17 October 2026: the [Claude review checks](round-1/claude-review/README.md)
support the [round-one cross-model review](../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md):
independent float64 rows, a definition-based check of the transfer-gate
numerator, fault injection in the engine, and floating planning meshes for
the proposed activation lemma (not a certificate). Added for Edward Baker
with LLM assistance, Claude Opus 5.5 (`claude-opus-5-5`), Claude Cowork,
effort max.

Update, 18 October 2026: the same folder holds the
[planning program](round-1/claude-review/activation_plan_claude_20261018.py)
behind Section 7 of the [working manuscript](../manuscript/sharp_finite_sum_bounds/main.tex)
(floating planning, not a certificate). Added for Edward Baker with LLM
assistance, Claude Opus 5.5 (`claude-opus-5-5`), Claude Cowork, effort max.
