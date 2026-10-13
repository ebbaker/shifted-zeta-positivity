# ROUND 18 — Kasahara 1975 verified against the original; Paper 2 synced with concise Paper 1

**2026-08-28 (night).** Two inputs this round: the user's hand-downloaded `Kasahara.pdf` with
accompanying check notes (`Kasahara_notes.md`), and a fourth referee pass
(`omega_string_round17_feedback.md`) whose only substantive finding was cross-version drift —
Paper 2 was still citing the superseded 24-page margin draft instead of the concise Paper 1
(`PAPER_psi_omega_concise.tex`, "Quantitative asymptotics for Suzuki's shifted screw
functions"). Both handled; paper is **v4 (12 pp., compiles clean)**. **The Kasahara gate — the
last external dependency — is closed.** All of Theorems 1.1–1.6 and Remark 6.1 are now fully
sourced; per the referee, the next stage is human specialist review.

## 1. Kasahara 1975, verified directly (independently of the notes)

Read from the uploaded PDF (Japan. J. Math. 1 (1975), 67–84):

- **Conventions (§1, (5)–(9)):** mass functions are non-decreasing, **left-continuous**,
  m(0)=0 (Watanabe's inextensible measures); characteristic function
  h(s) = lim_{x→ℓ−} ψ(x,−s)/φ(x,−s) = a + ∫₀^∞ dσ(t)/(s+t) — i.e. **h(s) = q_ω(−s)** in our
  normalisation; (8): a = inf{x: m(x)>0} (our b = 0 ⇒ no initial massless gap);
  (9): **ℓ = lim_{s→0} h(s) = h(0)** — gives L_ω = ∞ directly from q_ω(0⁻) = ∞, now cited in
  the Theorem 1.1 proof (previously routed through Theorem 1.3).
- **Theorem 1 (continuity of Kreĭn's correspondence):** for strings m_n, the three conditions
  (i) m_n(x) → m_0(x) at each continuity point of m_0, (ii) φ_n(x,−s) → φ_0(x,−s),
  (iii) h_n(s) → h_0(s) for s > 0, are mutually equivalent. **Exactly as pinned secondhand in
  ROUND15 — [Kas75, Thm 1] was correct.** Our use: q_ω(−s) → q_ξ(−s) pointwise on s > 0
  (from Thm 1.6(i)) along any ω_n ↓ 0 ⇒ m_ω → m_ξ at continuity points. Theorem 1.6(iii)
  fully sourced.
- **Example 1:** m(x) = x^{1/α−1} has h(s) = D_α s^{−α} with
  D_α = {α(1−α)}^{−α}Γ(1+α)/Γ(1−α); at α = ½:
  D_{1/2} = (¼)^{−1/2}·Γ(3/2)/Γ(1/2) = 2·(√π/2)/√π = **1**. ✓
- **Theorem 2 (+ (30)′, (31)′):** for L continuous slowly varying at ∞[0] with t^αL(t)
  increasing for large [small] t and f_α its inverse: (30) h(s) ~ D_α s^{−α}L(1/s) as
  s→0[∞] ⟺ (31) m(xλ)/f_α(λ) → x^{1/α−1}; scaled forms (30)′/(31)′; and **(iii)** for α ≠ 0
  the equivalences (A) h ~ D_α s^{−α}L(1/s) ⟺ (B) σ(λ) asymptotics ⟺ (C)
  **m(x) ~ x^{1/α−1}K_α(x)** as x→∞[0+], K_α(x) = x^{−1/α}f_α(x) slowly varying.
- **IR application (Thm 1.3):** α = ½, L ≡ c = (ξ′/ξ)(σ), D_{1/2} = 1; (A)⇔(C) with
  f_{1/2}(x) = (x/c)² gives K_{1/2} ≡ c⁻², i.e. m_ω(x)/x → c⁻². **Constant confirmed by the
  original theorem** — no longer merely calibrated by the homogeneous string.
- **UV application (Thm 1.4):** α = ½ at the bracketed endpoint, L(t) = ¼log(1/t) (slowly
  varying at 0; ¼√t log(1/t) increasing for small t); inverting t ↦ ¼√t log(1/t) gives
  f_{1/2}(x) ~ 4x²/log²x, K_{1/2}(x) ~ 4/log²x, so m_ω(x) ~ 4x/(log x)². **Factor 4 and
  endpoint orientation confirmed.** Consistent with the user-note derivation via (31)′
  (r = √A L(A), y ~ 2r/log(1/r)) — the (iii)(A)⇔(C) route used in the paper avoids the
  scaling manipulation entirely, and both agree.
- The notes' claims all check out; the paper's proofs of 1.3/1.4 are rewritten as direct
  applications of [Kas75, Thm 2(iii) + Example 1], replacing the informal dual-curve
  derivation (which survives as the numerical illustration in Remark 5.1).

## 2. Cross-version sync with concise Paper 1 (referee round 4)

Numbering established by direct count of `PAPER_psi_omega_concise.tex` (remarks share the
theorem counter — the feedback's "Theorem 3.3" for the dichotomy is off by one):
Lemma 2.1 conv; **Prop 2.2** closed forms A, B; Remark 2.3 B(0); **Thm 2.4** exact
decomposition; **Cor 3.1** linear margin; **Thm 3.2** onset; Remark 3.3; **Thm 3.4
critical-shift dichotomy**; Cor 3.5 bounded characterization; Prop 3.6 single-zero
contribution; Prop 4.1 integrated form; Cor 4.2 one-sided; Thm 4.3 averaged L¹ form.

Edits applied to Paper 2:
1. Intro: removed the claim that [13] "posed the problem of computing" the strings (true only
   of the withdrawn long draft); replaced by the referee's suggested framing — shifted
   Herglotz positivity (recalled in [13]) + Kreĭn's correspondence suggests the family,
   extending Suzuki's ω = 0 construction; this paper develops it.
2. [13, Thm 1.5] → **[13, Thm 3.4]** (named "critical-shift dichotomy" in text); margin
   lower bound cited as **[13, Cor 3.1]** in the Thm 1.3 proof.
3. Open Problem (family aspect): Option A rewrite — cites only what the concise final remarks
   contain (self-dual Dirichlet analogues; off-central real zeros lack oscillatory phase);
   Siegel-blindness no longer attributed to [13] as a theorem. (The full Dirichlet/Siegel
   material remains available in PROGRESS §2 if it is ever restored to Paper 1 — Option B.)
4. Bibliography: [13] retitled "Quantitative asymptotics for Suzuki's shifted screw
   functions", companion paper, 2026.
5. "Status of the Tauberian citations" → "**Source of the Tauberian input**": definitive
   citations, the h(s) = q(−s) and left-continuity convention notes; KW1982/KW2009/KW2010/EKT
   kept as "see also".
6. Acknowledgements: AI-assistance disclosure stub added (user to finalize wording).

## 3. State of the companion paper (v4)

- **Fully proved, all sources verified:** Thms 1.1, 1.2, 1.3, 1.4, 1.5, 1.6(i)–(iii),
  Remark 6.1. No "modulo" language remains anywhere.
- Remaining before circulation: author block + final acknowledgements wording (user);
  optional fig_string regeneration (numerics polish; Open Problem 3 route); then **human
  specialist review** (inverse-spectral / analytic number theory), per the referee's explicit
  recommendation that further LLM passes are no longer the binding constraint.
- Suzuki correspondence: the drafted letter (PROGRESS §4b) can now mention both papers.
