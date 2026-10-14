# Euler-factor controls

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

**Correction, 13 October 2026.** Prepared for Edward Baker with LLM
assistance by `gpt-6-astra` (Codex), reasoning effort **ultra**. Original
Claude provenance above is retained. This revision distinguishes tracked
collision times from the global Newman constant and corrects the witness
margin; it introduces no new numerical certificate.

Status: **shared control screen in force; first results recorded. Next:
certify one Laguerre witness with outward arithmetic.**

The controls \(\Phi_{c,p}=\Phi+\tfrac c2[\Phi(\cdot+a)+\Phi(\cdot-a)]\),
\(a=\tfrac12\log p\), \(0<c<1\), preserve theta's real zeros at
\(t=0\), positivity and evenness, and the local Euler-factor and Hecke
relations at every prime other than \(p\), yet have
\(\Lambda_{c,p}>0\). These shared properties are the specified screen;
the controls do not preserve every property of the genuine theta source. They were
introduced in the
[Claude review](../../brainstorm/reviews/REVIEW_OF_ACTIVE_LIFTED_THETA_DIRECTIONS_CLAUDE_20261013.md)
(§1.3). This folder makes them a portfolio-wide screen and studies them.

- The [program](notes/INITIAL_RESEARCH_PROGRAM_20261013.md) states the
  **three-controls protocol** (shape kernel, real-axis perturbations,
  Euler-factor controls) that every new identity or certificate should
  report.
- [Note 1](notes/1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md) gives
  the exact Newman flow of the controls; a one-point Laguerre witness
  criterion that proves \(\Lambda_{c,p}>t\) once its negative value is
  certified; a numerical table of lowest-pair collision times \(T_0(c,p)\);
  and the formal local expansion \(T_0=t_m-S_2t_m^2+\cdots\), with
  \(t_m=4\log(1/c)/(\log p)^2\) and
  \(S_2=\xi''(\tfrac12)/(2\xi(\tfrac12))\). No global identification
  \(T_0=\Lambda_{c,p}\) or certified positive-time lower bound is claimed.
- The [numerics](numerics/README.md) hold the checker and record.

The rank-two reading of the controls is in
[direction 18](../18_rank_two_automorphic_lift/README.md), Proposition 4.

Save derivations in `notes/`, small reproducible checks in `numerics/`,
assessments in `reviews/`, and future project conversations in
`chat-histories/`. Follow [LARGE_FILES.md](../../../../LARGE_FILES.md) and
the [active portfolio](../README.md). No manuscript snapshot is created;
milestones are in [DRAFT_HISTORY.md](DRAFT_HISTORY.md).
