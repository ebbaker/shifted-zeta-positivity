# ROUND 16 — Second referee pass on the draft: six fixes applied, one real error caught

**2026-08-28 (evening).** Response to the second round of external referee-style feedback
(`omega_string_round15_feedback.md`), this time on `PAPER_omega_string.tex` (v1) itself. The
feedback's overall verdict: "major improvement … a credible second paper if the
Kasahara/Kreĭn references survive direct checking," with confidence High on Theorems 1.1, 1.2,
1.5, 1.6(i), high-in-substance on 1.6(ii), medium-high on 1.3/1.4 (pending Kasahara), medium on
1.6(iii). All six of its concrete points were adopted; the paper is now **v2 (12 pp., compiles
clean)**, replacing v1 in `claude/PAPER_omega_string.tex`.

## Triage and disposition

1. **Standing hypothesis at ω = ½ — a real logical error, confirmed and fixed.** v1 declared
   σ > Θ as standing hypothesis and called it unconditional for ω ≥ ½. At ω = ½ (σ = 1) this
   is wrong as stated: every individual zero has β < 1, but Θ = 1 is not excluded. Verified
   that no proof uses a uniform gap — only the pointwise inequality enters (analyticity uses
   only that {Re s > σ} is zero-free; boundary continuity uses discreteness + no zeros ON
   Re s = σ; the tail bound ρ_ω(u) = (1/2π)log(u/2π) + O(1) holds uniformly down to σ = 1 via
   (ζ′/ζ)(σ+iu) = O(log u) for σ ≥ 1). Fix: standing hypothesis (7) is now **β < σ for every
   zero** — unconditional for σ ≥ 1, the zero-free half-plane hypothesis for σ < 1 — with an
   explicit sentence that no uniform gap is asserted or needed. All downstream references to
   (7) adjusted (Thm 1.1 proof ×4, Thm 1.3 proof).

2. **ω_c boundary — "cannot be continued below ω_c", and a new Remark 6.1 (the critical
   member).** The referee is right that at ω = ω_c the positive string may survive; in fact it
   always does: if Θ is not attained, (7) holds at ω_c and Theorem 1.1 applies verbatim; if it
   is attained, boundary zeros contribute *real* poles on the cut, which Stieltjes functions
   permit, and the contribution of a boundary pair {σ_c±iτ} of multiplicity m is **exactly**
   (m/w)[1/(w−iτ)+1/(w+iτ)] = 2m/(τ²−z) — a point mass 2m at τ², the degenerate a→0⁺ case of
   the residue lemma, with Kotani's mass normalisation. So the critical member is a string with
   point masses at the extremal ordinates embedded in the a.c. background of the remaining
   zeros. Added as Remark 6.1; "ceases to exist at ω_c" → "cannot be continued below ω_c"
   throughout; new open problem (§9.2) on characterising the critical string. (Consistent with
   the margin paper, where the time-side criterion also survives at the critical shift.)

3. **Theorem 1.6(ii) — proof replaced by the direct Poisson approximate-identity argument.**
   The referee's concern about Grommer–Hamburger for infinite-mass measures is fair. New proof:
   under RH ρ_ω = (1/π)Σ_τ ω/(ω²+(u−τ)²); for f ∈ C_c with support in [−R,R], each term →
   f(τ), dominated uniformly in ω ≤ 1 by min(‖f‖_∞, π⁻¹‖f‖₁ dist(τ,[−R,R])⁻²), summable by
   Στ⁻² < ∞; dominated convergence for the series, then pushforward under u ↦ u². The
   Herglotz-convergence route is demoted to a parenthetical alternative "with care, both
   measures having infinite total mass". The sharpening of the Lorentzians is now literally
   the proof.

4. **Kasahara remains the bottleneck — acknowledged, unchanged.** The two implications needing
   the original text: q(−y) ~ c/√y ⇒ m(x) ~ c⁻²x, and q(−y) ~ (¼log y)/√y ⇒ m(x) ~ 4x/log²x
   (endpoint orientation, normalisation, regular-variation conventions), plus the exact
   continuity theorem for nonregular infinite strings behind 1.6(iii). The paper's "Status of
   the Tauberian citations" paragraph already flags exactly this; the **user action from
   ROUND15 §8.1 stands**: hand-download Kasahara 1975 from J-STAGE (DOI 10.4099/math1924.1.67)
   and confirm hypotheses/numbering/constants.

5. **Abstract narrowed** per the referee's exact suggestion: "We verify every statement
   numerically…" → "We provide independent numerical checks of the spectral formulas and
   compute finite approximations to the associated strings…".

6. **Figure 1 caption qualified:** the right panel is the exact closed-form density ρ_ω near
   γ₁ — unconditional for this zero (critical-line location verified) — but for ω < ½ its
   interpretation as the spectral density of a positive string is conditional (Theorem 1.5).
   Figure otherwise retained unchanged, per the referee.

## Referee's structural read (for the record)

The feedback endorses the chain Ψ_ω → q_ω → σ_ω → m_ω with the two boxed correspondences
(margin ↔ zero-frequency DOS ↔ bulk density; Poisson-broadened a.c. → pure-point Kotani at the
RH endpoint), notes Theorems 1.1–1.2 alone already constitute a coherent short inverse-spectral
result if the asymptotic theorems needed revision, and closes: "stabilize the inverse-spectral
mathematics before adding further physics" — i.e., the Kasahara hand-check is the gating item,
ahead of any AdS/scattering speculation.

## State of the paper after v2

- Proved in-paper, no external gaps: Thms 1.1, 1.2, 1.5, 1.6(i), 1.6(ii) (now direct), Remark
  6.1 (critical member, exact point-mass identity).
- Proved modulo the Kasahara hand-check: Thms 1.3, 1.4, 1.6(iii).
- Remaining before submission: author block; Kasahara verification (user); fig_string
  regeneration at the numerics-polish stage; optional: Suzuki correspondence (letter drafted in
  PROGRESS §4b).
