# N=4 SYM: displacement response and Loewner growth

This investigation begins with the [detailed research proposal](notes/N4SYM_DISPLACEMENT_LOEWNER_RESEARCH_PROPOSAL_20260923.md), prepared for Edward Baker on 23 September 2026 with GPT-6 (Codex) assistance. The reasoning-effort setting was not exposed.

The physical objective is to derive Wilson-line shape and genuine-trace evolution within a fixed four-dimensional N=4 SYM theory, using displacement and internal-scalar insertions. The corresponding causal response and energy account are then to be determined. The straight BPS line is a controlled reference, and generic growing contours are not assumed to be BPS. Arithmetic realization is a later, conditional comparison.

- [Research notes](notes/README.md), [numerical checks](numerics/README.md) and [reviews](reviews/README.md).
- [Parent analysis: lessons from WZW and the subsequent tests](../notes/LESSONS_FROM_WZW_FOR_YM_AND_N4SYM_20260923.md).
- [Existing pure-YM hierarchy](../notes/GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md).

## Status after the first and second sessions (23–24 September 2026; Claude Opus 5.5)

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

## Status after the third session (24 September 2026; Claude Fable 5.1)

The author chose option (B) of the second continuation: return to the arithmetic goal by looking for a physical channel with memory.

5. **[Finite-mass memory and the quartic response](notes/FINITE_MASS_MEMORY_AND_QUARTIC_RESPONSE_20260924.md)**.
   - The finite-mass source (string endpoint at z_m = √λ/2πm) is the first channel with memory. Exactly at linear order: F = mŸ, X = Y + z_mẎ, mẌ = F + z_mḞ, with Y the retarded auxiliary trajectory; the memory is one exponential, χ_m(ω) = −mω²/(1 − iωz_m), whose first two terms reproduce the Abraham–Lorentz response of the first note.
   - Finite mass restores finite-time passivity: W(T) = (m/2)Ẏ² + (√λ/2π)∫Ÿ² ≥ 0; the Schott term is the O(z_m) truncation of the positive square.
   - The boundary field of the moving source (dilaton-coupled operator) is exactly local in the retarded time: the depth integral is a total derivative, and the transfer function is e^{iωr_m} times a closed-form quartic polynomial. A referee context reports that this contradicts a 1999 broadening claim (Callan–Güijosa), to be checked by eye.
   - Verdict: rational transfer, one pole, one fixed delay, integer exponents. The channel fails the front-and-tangent test; no arithmetic comparison is run.
   - The quartic straight-line response is the first nonlocal one; its memory is set by the non-protected dimension Δ₆(λ) ∈ (1, 2), but the straight line has no scale, so no fixed delays can arise at any order. The transcribed GRT Δ = 1 four-point functions pass crossing and OPE tests; the Δ = 2 transcription fails them and is not used.
6. **[Continuation for the next session](notes/CONTINUATION_AFTER_THIRD_SESSION_20260924.md).**

Numerics: seven standard-library programs with 72, 77, 47, 56, 20, 107 and 93 cases (472 total), all passing, deterministic, with records under `numerics/records/`. Reviews: three same-assistant audits, each with separate referee contexts; there has been no independent specialist review.

A first draft manuscript covering the three sessions, *Displacement response and Loewner growth for the half-BPS Wilson line: locality, memory and the limits of an arithmetic reading*, is at [manuscript.tex](manuscript.tex) ([PDF](manuscript.pdf), [build notes](BUILD.md), [milestone index](DRAFT_HISTORY.md)). It is drafted for the author and has had no independent review. Manuscript milestones use commits or tags recorded in DRAFT_HISTORY.md, without dated snapshots. Work from all three sessions is uncommitted.
