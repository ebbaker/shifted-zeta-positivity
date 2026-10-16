# Same-assistant audit of the second N4SYM session (24 September 2026)

**Model:** Claude Opus 5.5 (Anthropic), model identifier `claude-opus-5-5` as reported by the runtime (session configuration `claude-fable-5-1`; the serving model can differ). Reasoning effort not exposed.  
**Kind:** an internal audit, with a separate adversarial referee context of the same model. This is **not** an independent specialist review.  
**Scope:** [near-BPS corner, rounding and closure](../notes/NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md); [`check_near_bps_corner.py`](../numerics/check_near_bps_corner.py); [`check_rounded_and_closure.py`](../numerics/check_rounded_and_closure.py).

## Referee pass

The referee re-derived eight items with its own mpmath/scipy code, including an independent implementation of the rounded loop.

**Confirmed:**
- The Clausen form of the two-loop bracket, with an exact cancellation of the imaginary part.
- The three validating limits of the transcribed Drukker–Forini two-loop cusp: small angle, the BPS-line slope at every φ, and the antiparallel logarithm.
- The corner form through two loops.
- The classical string integrals. The referee derived them from Nambu–Goto and confirmed the BPS curve θ = π/√(1+ζ₀²) analytically.
- The strong-coupling CHMS slope.
- The corner function F(x), with F(0) = 0.17501 and F′(1) = −¼√(2/π).
- The v^{3/2} law.
- The rounding constant h: the referee obtained −4.02025 at s = 0.1, against −4.020216.

**Corrections, all applied in the note:**
1. The two-loop corner remainder omitted the one-loop O(λu²) = O(gu) term.
2. The all-orders H argument needs a multi-angle antiparallel-lines bound. The singular behaviour at L − 1 distinct θ_j must be bounded, not only at θ = 0. The result is order by order in perturbation theory, not nonperturbative.
3. The rounded formula must use the exact cusp sum A(s) as the log(1/δ) coefficient. The O(s) constant h is convention dependent.
4. The Zarembo-stadium test only checks conventions, because its integrand vanishes identically. The constant-scalar stadium is what checks normalization.
5. The strong-coupling corner holds only for λΩ ≫ 1 and says nothing about H. Its kink at θ = π is a classical zero-mode effect.
6. The two-loop form (1 − x²)(π²/2)B(2g/π) should not be extrapolated: at strong coupling F is not proportional to 1 − x².

## Residual concerns for a specialist

- **The Drukker–Forini formulas** were taken from an automated fetch summary. The three limits make a transcription error unlikely, but the equations should still be compared with the paper by eye.
- **The CHMS near-BPS formula** is used as an exact input. Its derivation, from the latitude matrix model together with the relation to the cusp, is standard, but the note does not re-derive it.
- **The multi-angle antiparallel bound** in the all-orders argument is an assumption beyond two loops.
- **The v^{3/2} strong-coupling law** for antiparallel lines near θ = π was not found in the literature during this session. It may be known.
- **The Schwinger–Dyson audit** is structural. Its one-loop statement (field-equation part contact, transverse part long range) is exhibited through the propagator kernels, not through a full moment calculation.

## Repository hygiene

Nothing is committed. `validation/check_package.py` still reports inventory mismatches, as it already did at `8b22141`. A zero-byte `.git/index.lock` left by an earlier `git status` may still be present and should be removed before committing.
