# Investigations 3 brainstorm numerics

16 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork, reasoning effort max.

Labelled support computations for the brainstorm notes and reviews. Each
entry states its arithmetic and dependencies; scripts print JSON records. Nothing here is a
certificate: the records support remarks in the notes and prove nothing.

| Script | Record | Supports |
| --- | --- | --- |
| [`check_brainstorm_modifications_claude_20261016.py`](check_brainstorm_modifications_claude_20261016.py) | [`CHECK_BRAINSTORM_MODIFICATIONS_CLAUDE_20261016.json`](CHECK_BRAINSTORM_MODIFICATIONS_CLAUDE_20261016.json) | [Note 03](../notes/03_MODIFICATIONS_AND_ALTERNATIVE_DIRECTIONS_CLAUDE_20261016.md): field scale against source scale at the three-square control's height (A); endpoint tails of the half-line square terms and the exponentially small reflection tolerance, with the control's sup-norm distance (B); the attraction law for the top complex zero with Trudgian's \(S(T)\) bound, and a grid check of its elementary inequality (C). Composite Simpson on \([0,1.8]\), about \(10^{-12}\) absolute at the heights used. |

The original Claude script runs from anywhere with
`python3 -I <script> > <record>`; its output is byte-identical across runs.


## Codex response checks

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Coordinating model **gpt-6-astra (Codex)**, reasoning effort **ultra**, verified
from session metadata. These small diagnostics support the
[response to Note 03](../reviews/02_RESPONSE_TO_CLAUDE_BRAINSTORM_CODEX_20261016.md).

| Script | Record | Scope |
| --- | --- | --- |
| [Coefficient distance and attraction audit](audit_note03_coefficient_distance_and_attraction.py) | [Floating record](NOTE03_COEFFICIENT_DISTANCE_AND_ATTRACTION_AUDIT.json) | NumPy least-squares solves using Claude's quadrature; dependency hash checked before replay. Corrects pair-versus-zero counting in the attraction calculation; the positive-time count remains an unproved input. |
| [Independent high-precision distance check](check_note03_distance_high_precision.py) | [60-digit record](NOTE03_DISTANCE_HIGH_PRECISION.json) | Independent elementary source implementation with mpmath tanh-sinh quadrature. Confirms the suppression and negative-coefficient examples and compares the time-zero transform with xi/8. |

From the repository root, with NumPy and mpmath installed:

```sh
python3 papers/brainstorm/investigations-3/numerics/audit_note03_coefficient_distance_and_attraction.py --repo .
python3 papers/brainstorm/investigations-3/numerics/check_note03_distance_high_precision.py
```

Both scripts write only to stdout. Records identify the producing script
and environment. The arithmetic is floating, without interval quadrature
or tail certification; displayed linear residuals describe the computed
systems. No numerical comparison here certifies a collision or a Newman
bound. Cross-platform byte identity is not asserted.

## Claude reply checks

16 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork, reasoning effort max.
These diagnostics support the
[reply to Codex's response](../reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md).

| Script | Record | Scope |
| --- | --- | --- |
| [`check_codex_response_reply_claude_20261016.py`](check_codex_response_reply_claude_20261016.py) | [`CHECK_CODEX_RESPONSE_REPLY_CLAUDE_20261016.json`](CHECK_CODEX_RESPONSE_REPLY_CLAUDE_20261016.json) | (A) the coefficient experiment repaired with nonnegative weights and the primitive-endpoint normalization, reproducing the three-square control; (B) the conditioning constant and admissible measurement error of the response's inequality for recurrence-defect and reflection-sample designs at heights 30 to 85; (C) independent replay of the corrected attraction numbers; (D) the shrinking-window energy identity. Standard library only; reuses the original Claude script's quadrature (dependency hash checked) with 180000 Simpson panels above \(x=50\); deterministic output. |

Run from this folder with `python3 -I check_codex_response_reply_claude_20261016.py > CHECK_CODEX_RESPONSE_REPLY_CLAUDE_20261016.json`; it reads its dependency from the same folder. Floating diagnostics, not certificates: no collision, zero-free region or Newman bound is certified.
