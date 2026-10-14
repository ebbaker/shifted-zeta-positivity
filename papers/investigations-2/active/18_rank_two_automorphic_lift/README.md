# Rank two automorphic lift

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

Status: **first bounded tasks A1–A3 complete; exact identities, no sign.
One bounded task (A4) remains before the stop rule applies.**

This is direction A of the
[Claude review](../../brainstorm/reviews/REVIEW_OF_ACTIVE_LIFTED_THETA_DIRECTIONS_CLAUDE_20261013.md)
(§3). It absorbs card 09, the [recommendations](../CLOSE_AND_MERGE_RECOMMENDATIONS_CLAUDE_20261013.md)
propose folding 07 and 15 into it, and it carries out the "09-to-06"
allocation of the
[Codex first pass](../../brainstorm/reviews/PRIORITY_RESEARCH_FIRST_PASS_CODEX_20261013.md).
In volume and shape coordinates the theta pair source is a lattice theta
function; its volume transform is the completed Eisenstein series on the
imaginary-axis geodesic, and the physical height is the spectral parameter.

[Note 1](notes/1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md) proves:

- the physical insertion annihilates the Eisenstein constant term, so both
  Laguerre expressions are folded moments of a pure cusp kernel at every
  Newman time (Theorems 1–2);
- card 09's two-coset identity is the Hecke correspondence at 2, exact at
  every Newman time (Theorem 3);
- the Euler-factor controls share the cusp kernel and every Hecke relation
  at the other primes, so no finite set of Hecke relations can prove
  \(\Lambda\le0\) (Proposition 4).

Read the [program](notes/INITIAL_RESEARCH_PROGRAM_20261013.md) for scope,
tasks and the stop rule, and the [numerics](numerics/README.md) for the
checker and record. The controls themselves live in
[direction 19](../19_euler_factor_controls/README.md).

Save derivations in `notes/`, small reproducible checks in `numerics/`,
assessments in `reviews/`, and future project conversations in
`chat-histories/`. Follow [LARGE_FILES.md](../../../../LARGE_FILES.md) and
the [active portfolio](../README.md). No manuscript snapshot is created;
milestones are in [DRAFT_HISTORY.md](DRAFT_HISTORY.md).
