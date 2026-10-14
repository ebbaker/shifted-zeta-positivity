# Euler-factor controls

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

**Correction, 13 October 2026.** Prepared for Edward Baker with LLM
assistance by `gpt-6-astra` (Codex), reasoning effort **ultra**. Original
Claude provenance above is retained. This revision distinguishes tracked
collision times from the global Newman constant and corrects the witness
margin; it introduces no new numerical certificate.

ChatGPT - **Certification, 14 October 2026.** Prepared for Edward Baker with LLM
assistance by `gpt-6-astra` (Codex), reasoning effort **ultra**.

**Manuscript, 14 October 2026.** Prepared for Edward Baker with LLM
assistance. Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`;
the serving model may differ), Claude Cowork, reasoning effort **max**.

Status: **shared control screen in force. One outward certificate
([Note 2](notes/2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md)) proves
\(\Lambda_{1/2,41}>1/5\); the [manuscript](manuscript/euler_factor_controls.tex)
certifies \(\Lambda_{1/2,p}>1/5\) for every prime \(p\le41\) with an
independent program and adds an asymptotic lower bound. Next: independent
specialist review of the manuscript.**

The fixed-witness task is complete. Further control work should address a
named hypothesis or domain that needs screening. The proposed local-branch
theorem targets a lower bound \(\Lambda_{c,p}\ge t_m-S_2t_m^2+O(a^{-6})\).
The manuscript's Theorem 1.4 proves a bound of this form,
\(\Lambda_{c,p}>t_m-S_2t_m^2-Qa^{-6}\) with explicit \(Q\), by a witness at
\(x=\pi/a\); the implicit-function construction of the collision branch
itself remains unexecuted. The
[shared execution review](../../brainstorm/reviews/MATCHED_01_18_AND_19_RESULTS_CODEX_20261014.md)
records the stopping conditions and preserves the distinction between a
tracked collision and the global Newman constant.

Claude - **Manuscript, 14 October 2026.** Prepared for Edward Baker with LLM
assistance. Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`;
the serving model may differ), Claude Cowork, reasoning effort **max**.

Status: **shared control screen in force; manuscript drafted with certified
witnesses (14 October 2026). Next: independent specialist review of the
manuscript and its certificate program.**

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
ChatGPT - \(S_2=\xi''(\tfrac12)/(2\xi(\tfrac12))\). No global identification
  \(T_0=\Lambda_{c,p}\) is claimed.
- [Note 2](notes/2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md) certifies
  \(\Lambda_{1/2,41}>1/5\) by a strictly negative raw Laguerre
  witness at the rational point \(x=168413/100000\), including
  validated quadrature and all source and control-shift tails.
- The [manuscript](manuscript/euler_factor_controls.tex) (LaTeX source;
  compiled PDFs are not stored) proves \(\Lambda_{1/2,p}>0.2\) for every
  prime \(p\le41\) and \(\Lambda_{1/2,p}>0.1787854\) for \(p=43,47\), by
  outward-rounded interval certificates of single Laguerre witnesses. It
  also proves \(\Lambda_{c,p}>t_m-S_2t_m^2-\tfrac1{50}a^{-6}\) for
  \(\tfrac12\le c<1\), \(p\ge29\), with a second explicit regime, and
  records the arithmetic of the controls (extended Selberg class,
  conductor \(p^2\), local factor tempered exactly when \(c\ge1\)) and what
  they imply for proofs of upper bounds. Its certificate program shares no
  code or method with Note 2's; evaluated at Note 2's point, its enclosures
  of \(H,H',H''\) and \(\mathscr L_0\) lie inside Note 2's.
- The [internal verification](reviews/1_MANUSCRIPT_AND_CERTIFICATE_VERIFICATION_CLAUDE_20261014.md)
  found and removed a rounding defect in the first version of the
  manuscript's certificate program; the regenerated enclosures contain
  independent 75-digit values. Its addendum records the comparison with
  Note 2.
- The [numerics](numerics/README.md) preserve the exploratory table and
<<<<<<< HEAD
  hold both outward checkers with their records: Note 2's exact-endpoint
  certificate and the manuscript's certificate program.
=======
  provide the new outward checker and exact-endpoint certificate.
 Claude - \(S_2=\xi''(\tfrac12)/(2\xi(\tfrac12))\). Note 1 claims no global
  identification \(T_0=\Lambda_{c,p}\) and no certified bound; the
  certified lower bounds are in the manuscript below.
- The [manuscript](manuscript/euler_factor_controls.pdf)
  ([source](manuscript/euler_factor_controls.tex)) proves
  \(\Lambda_{1/2,p}>0.2\) for every prime \(p\le41\) and
  \(\Lambda_{1/2,p}>0.1787854\) for \(p=43,47\), by outward-rounded interval
  certificates of single Laguerre witnesses. It also proves
  \(\Lambda_{c,p}>t_m-S_2t_m^2-\tfrac1{50}a^{-6}\) for
  \(\tfrac12\le c<1\), \(p\ge29\), with a second explicit regime, and records
  the arithmetic of the controls (extended Selberg class, conductor \(p^2\),
  local factor tempered exactly when \(c\ge1\)) and what they imply for
  proofs of upper bounds.
- The [internal verification](reviews/1_MANUSCRIPT_AND_CERTIFICATE_VERIFICATION_CLAUDE_20261014.md)
  found and removed a rounding defect in the first certificate program; the
  regenerated enclosures contain independent 75-digit values.
- The [numerics](numerics/README.md) hold the floating-point checker and
  record of Note 1 and the certificate program and record of the
  manuscript.
>>>>>>> 94745f3 (Merged work from ChatGPT)

The rank-two reading of the controls is in
[direction 18](../18_rank_two_automorphic_lift/README.md), Proposition 4.

Save derivations in `notes/`, small reproducible checks in `numerics/`,
assessments in `reviews/`, and future project conversations in
`chat-histories/`. Follow [LARGE_FILES.md](../../../../LARGE_FILES.md) and
the [active portfolio](../README.md). No manuscript snapshot is created;
milestones are in [DRAFT_HISTORY.md](DRAFT_HISTORY.md).
