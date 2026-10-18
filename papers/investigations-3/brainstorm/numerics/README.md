# Investigations 3 brainstorm numerics

18 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork, reasoning effort max;
the session is configured as `claude-opus-5-5` and the serving model may
differ from the configured identifier.

Labelled support computations for the notes and reviews in this folder.
Scripts are standard-library Python, run from anywhere with
`python3 -I <script> > <record>`, and print deterministic JSON. Nothing
here is a certificate: the records support planning remarks and prove
nothing about any \(L\)-function.

| Script | Record | Supports |
| --- | --- | --- |
| [`planning_arithmetic_claude_20261018.py`](planning_arithmetic_claude_20261018.py) | [`PLANNING_ARITHMETIC_CLAUDE_20261018.json`](PLANNING_ARITHMETIC_CLAUDE_20261018.json) | [Review 04](../04_REVIEW_OF_ASSESSMENT_AND_DIRECTION_CLAUDE_20261018.md): the conductor-rate note's \(T(q)\) on a ladder of conductors against its asymptotic form (A); sensitivity of \(T(10^{12})\) to the transport remainder \(E\) (B); dependence on the comparison height \(p\in[\sqrt5,4]\) with \(\kappa((1+p)/2)\) from the von Mangoldt sum to \(2\cdot10^5\) plus an integral tail bound (C); dependence on the initial squared strip (D); the crossover between \(T(q)\) and a hypothetical \(c/\log q\) bound (E); the smallest conductor at which the restart is nonvacuous and what the same restart would give below \(10^{12}\) if the envelope extended (F); and a recomputation of the conductor-rate note's displayed constants and of the restart note's two exact gates (G). Floating point throughout; the \(\kappa\) tail bound errs in the safe direction (floor understated, times overstated). |

The record's section G reproduces \(L(10^{12})=25.909075565\),
\(T(10^{12})=0.2130631631\) and the gate values \(e^{kT}=4.4990\) against
\(1+k/2=4.4973\) stated in the
[conductor-rate note](../notes/01_CONDUCTOR_RATE_FROM_UNIFORM_FLOOR_CODEX_20261017.md)
and the [restart note](../../03_effective_outer_remainders/notes/round-2/02_RESTARTED_STRIP_COMPARISON_CODEX_20261017.md);
agreement of a floating recomputation with an exact certificate is a
consistency check on the formulas, not a second certificate.
