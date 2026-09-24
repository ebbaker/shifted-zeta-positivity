# N=4 SYM: displacement response and Loewner growth

This investigation begins with the [detailed research proposal](notes/N4SYM_DISPLACEMENT_LOEWNER_RESEARCH_PROPOSAL_20260923.md), prepared for Edward Baker on 23 September 2026 with GPT-6 (Codex) assistance. The reasoning-effort setting was not exposed.

The physical objective is to derive Wilson-line shape and genuine-trace evolution within a fixed four-dimensional N=4 SYM theory, using displacement and internal-scalar insertions. The corresponding causal response and energy account are then to be determined. The straight BPS line is a controlled reference, and generic growing contours are not assumed to be BPS. Arithmetic realization is a later, conditional comparison.

- [Research notes](notes/README.md), [numerical checks](numerics/README.md) and [reviews](reviews/README.md).
- [Parent analysis: lessons from WZW and the subsequent tests](../notes/LESSONS_FROM_WZW_FOR_YM_AND_N4SYM_20260923.md).
- [Existing pure-YM hierarchy](../notes/GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md).

## Status after the first session (23–24 September 2026; Claude Opus 5.5)

1. **[Straight-line response and trace completion](notes/STRAIGHT_LINE_RESPONSE_AND_TRACE_COMPLETION_20260923.md)** covers milestones M0–M2 for the straight line and prepares M3.
   - The quadratic shape response is fixed by B, up to a single perimeter constant.
   - The linear retarded response is local: χ_R = m_Rω² + 2πiBω³ (Abraham–Lorentz). The total work is 2πB‖ḧ‖², which reproduces CHMS.
   - The renormalized finite-time account is not passive.
   - The linear straight-line channel is therefore closed as an arithmetic candidate.
   - The proposal's first growing-contour observable (constant scalar with a straight return chord) is a thin sliver dominated by trace–chord attraction, and it diverges as s = a√t → 0.
   - The tangent-coupled profile is trivial (⟨W⟩ = 1).
2. **[Flipped-return analysis](notes/FLIPPED_RETURN_TRACE_ANALYSIS_20260924.md)** studies the recommended M3 family: n₀ on the trace, −n₀ on the chord.
   - The first two smooth-field evolution equations are exact and verified.
   - The short-time law 1 + O(a²t³) at fixed flow resolution is independently confirmed by a one-loop Feynman integral.
   - The one-loop continuum structure is 1 − (2πB₁/3)|s|(log(ℓ/ε) − 2).
   - The flow regulator gives three regimes, with a regular limit in every order.
   - The closure inventory is not closed.
   - The all-orders near-BPS cusp coefficient H(λ,N) is open.
3. **[Near-BPS corner, rounding and closure](notes/NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md)** (second session, 24 September).
   - The corner coefficient of the flipped loop has effective coupling g = λ|s|/3.
   - It is one-loop exact as s → 0 (H = λ(1−1/N²)/16π, order by order, under a stated bound). The two-loop corner is (1 − x²)[g/16π − g²/192π²].
   - At strong coupling the classical corner is Γ = √(λu)F(x), with F(0) = 0.1750. It reproduces the exact CHMS slope at the BPS line.
   - The rounded family W(s, δ̂) is finite at one loop, with universal content A(s).
   - The Schwinger–Dyson audit leaves an explicit residual inventory, so the hierarchy is not closed.
4. **[Continuation for the next session](notes/CONTINUATION_AFTER_SECOND_SESSION_20260924.md).** It poses a decision: complete the flipped family as physics, or seek a physical channel with memory for the arithmetic goal.

Numerics: five standard-library programs with 72, 77, 47, 56 and 20 cases (272 total), all passing, deterministic, with records under `numerics/records/`. Reviews: two same-assistant audits, each with a separate referee context; there has been no independent specialist review.

No manuscript exists for this investigation. Manuscript milestones should use commits or tags recorded in a concise DRAFT_HISTORY.md, without creating dated manuscript snapshots. Work from this session is uncommitted.
