# Investigations 3 brainstorm numerics

16 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork, reasoning effort max.

Labelled support computations for the brainstorm notes. Standard-library
Python, deterministic, one JSON record per script. Nothing here is a
certificate: the records support remarks in the notes and prove nothing.

| Script | Record | Supports |
| --- | --- | --- |
| [`check_brainstorm_modifications_claude_20261016.py`](check_brainstorm_modifications_claude_20261016.py) | [`CHECK_BRAINSTORM_MODIFICATIONS_CLAUDE_20261016.json`](CHECK_BRAINSTORM_MODIFICATIONS_CLAUDE_20261016.json) | [Note 03](../notes/03_MODIFICATIONS_AND_ALTERNATIVE_DIRECTIONS_CLAUDE_20261016.md): field scale against source scale at the three-square control's height (A); endpoint tails of the half-line square terms and the exponentially small reflection tolerance, with the control's sup-norm distance (B); the attraction law for the top complex zero with Trudgian's \(S(T)\) bound, and a grid check of its elementary inequality (C). Composite Simpson on \([0,1.8]\), about \(10^{-12}\) absolute at the heights used. |

Run from anywhere with `python3 -I <script> > <record>`; the output is
byte-identical across runs.
