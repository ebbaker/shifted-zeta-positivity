# N4SYM research notes

Reading order:

1. [Displacement operators, Loewner growth and energy accounting: research proposal](N4SYM_DISPLACEMENT_LOEWNER_RESEARCH_PROPOSAL_20260923.md) — 23 September 2026 (GPT-6, Codex). Fixed SU(N) N=4 SYM probe sector; smooth shape hierarchy; retarded spectral/work analysis; rounded genuine Loewner trace; possible causal channel; conditional arithmetic tests; milestones and first-session handoff.
2. [Straight-line response, energy accounting and the choice of trace completion](STRAIGHT_LINE_RESPONSE_AND_TRACE_COMPLETION_20260923.md) — 23 September 2026 (Claude Opus 5.5). This note carries out the proposal's first session.
   - The quadratic response is fixed by B, and the Zarembo cancellation holds if and only if C_D = 6C_Φ.
   - The linear straight-line response is local: Abraham–Lorentz, with the tilt channel an exact resistor.
   - Total work reproduces CHMS, but finite-time non-passivity follows from the Schott term.
   - Loewner time collapses to s = a√t in the conformal theory.
   - The constant-n₀ chord completion is dominated by a thin sliver, and the tangent-coupled family is trivial.
   - The flipped-return completion is proposed, with its exact first evolution equation.
3. [The flipped-return Loewner loop: evolution equations, one-loop structure and regimes](FLIPPED_RETURN_TRACE_ANALYSIS_20260924.md) — 24 September 2026 (Claude Opus 5.5).
   - Exact first and second equations for smooth fields; the tip coefficient is the growth rate of the perimeter mismatch.
   - The short-time t³ law is confirmed by a one-loop flowed integral.
   - Continuum one loop: A(s) and F(s) = (4π/3)s + ….
   - Three flow regimes, including the |s| log|s| behaviour of separation-based schemes.
   - Closure inventory, and the open near-BPS coefficient H(λ,N).
4. [Continuation after the first session](CONTINUATION_AFTER_FIRST_SESSION_20260924.md) (preserved).
5. [The near-BPS corner of the generalized cusp, the rounded flipped loop, and the closure audit](NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md) — 24 September 2026 (Claude Opus 5.5).
   - The exact slope of the corner at the BPS line comes from CHMS.
   - Two-loop corner via Drukker–Forini (validated by three limits); H is one-loop exact order by order.
   - Classical-string corner function F(x), with a √(λu) window.
   - Rounded one-loop family with h = −4.0202.
   - Schwinger–Dyson residual inventory with one-loop kernel controls.
6. [Continuation after the second session](CONTINUATION_AFTER_SECOND_SESSION_20260924.md) — current handoff.

The proposal builds on the [parent cross-theory lessons](../../notes/LESSONS_FROM_WZW_FOR_YM_AND_N4SYM_20260923.md) and preserves the physical objective of the [genuine-trace continuation](../../notes/RESEARCH_CONTINUATION_AFTER_GROWING_TRACE_20260921.md).

Each research note identifies its assumptions, result status, model and exposed effort setting, together with the relevant diagnostic and review records. Checks are in [`../numerics`](../numerics/README.md) and audits in [`../reviews`](../reviews/README.md).
