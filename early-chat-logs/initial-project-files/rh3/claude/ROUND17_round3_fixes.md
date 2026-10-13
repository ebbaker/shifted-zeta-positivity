# ROUND 17 — Third referee pass: three fixes applied, paper at v3

**2026-08-28 (late).** Response to the third round of external referee-style feedback
(`omega_string_round16_feedback.md`), on `PAPER_omega_string.tex` v2. Verdict there: fixes of
rounds 15–16 all confirmed; two concrete mathematical issues and one wording issue remained.
All fixed; paper is now **v3 (12 pp., compiles clean)** in `claude/PAPER_omega_string.tex`.
Referee's confidence table after these fixes: strong on 1.1, 1.2, 1.5, 1.6(i), 1.6(ii), and
Remark 6.1; 1.3/1.4/1.6(iii) still gated solely by the Kasahara/continuity source check.

## Fixes

1. **Thm 1.6(i): complex mean-value step — a real proof error, fixed.** v2 wrote
   q_ω − q_ξ = (ω/w)(ξ′/ξ)′(½+ω*+w) for some ω* ∈ (0,ω); the one-variable MVT is not valid for
   complex-valued functions. Replaced by the fundamental theorem of calculus along the real
   segment: q_ω − q_ξ = (1/w)∫₀^ω (ξ′/ξ)′(½+t+w)dt, giving
   |q_ω−q_ξ| ≤ (ω/inf_K|w|)·sup_{K×[0,ω₀]}|(ξ′/ξ)′| — the same locally uniform O(ω). Theorem
   unchanged.

2. **Figure 1 right panel: title/caption mismatch — resolved by computation.** The plotted
   curves ARE the full closed-form density ρ_ω (not single Lorentzians); computed peaks
   ρ_ω(γ₁) = 0.6474 / 1.2786 / 3.1853 at ω = 0.5/0.25/0.1 vs bare-kernel peaks 1/(πω) =
   0.6366 / 1.2732 / 3.1831 — background of all other zeros = 0.011/0.005/0.002 (0.1–1.7% of
   peak), which is why the curves look like bare Poisson kernels. Panel retitled "Full spectral
   density near γ₁ as ω↓0" (referee's option 2), caption now quantifies the background. PNG
   regenerated.

3. **ρ_ω pointwise asymptotic at σ = 1 — weakened to what is proved.** v2 claimed
   ρ_ω(u) = (1/2π)log(u/2π) + O(1) uniformly down to σ = 1 from (ζ′/ζ)(σ+iu) = O(log u); the
   O(1) remainder does not follow (the ζ′/ζ term itself can be of size log u). Now: uniformly
   for σ ≥ 1, ρ_ω(u) = O(log u) (Stirling + Titchmarsh (3.11.7)) — all the
   ∫(1+λ)⁻¹dσ_ω < ∞ argument needs; the sharper O_σ(1) form is stated for fixed σ > 1 only
   (absolute convergence of the Dirichlet series), and RvM is described as the mean density
   only. Titchmarsh added to the bibliography (alphabetical order kept).

4. **Thm 1.4 (and 1.3) hypothesis wording** per the referee's suggested form: "Under the
   hypotheses of Theorem 1.1, m_ω(x) ~ 4x/(log x)²; in particular this holds unconditionally
   for ω ≥ ½" — separating the unconditional Weyl-side asymptotics from the conditional
   existence of the string. Thm 1.3 aligned the same way.

## Referee's structural additions (for the record)

- The critical-member transition picture is endorsed and sharpened into a three-stage scheme:
  a.c. measure above ω_c → a.c. + atoms at ω_c (when extremal zeros exist) → no positive
  Stieltjes realization below ω_c. "May eventually be one of the more memorable observations."
- Explicit instruction: after these fixes, **no further broad AI-referee passes** — the
  bottleneck is now the direct source check (Kasahara 1975 for Thms 1.3/1.4 normalization and
  endpoint conventions; the exact continuity theorem for 1.6(iii)), after which the paper is
  ready for human specialist review. Speculative physics (hyperbolic scattering, AdS/CFT)
  only after the inverse-spectral foundation is stabilized.

## Standing next actions

1. **USER:** hand-download Kasahara 1975 from J-STAGE (DOI 10.4099/math1924.1.67; free) and
   verify: the Tauberian implications q(−y) ~ c/√y ⇒ m(x) ~ c⁻²x and
   q(−y) ~ (¼log y)/√y ⇒ m(x) ~ 4x/log²x (hypotheses, endpoint orientation, normalization,
   constants), and the continuity theorem ([Kas75, Thm 1] per the secondhand pin) for the
   nonregular infinite strings used in 1.6(iii). Once verified, update the "Status of the
   Tauberian citations" paragraph and the theorem-status remarks.
2. Author block + acknowledgements; then human specialist review.
3. fig_string regeneration at the numerics-polish stage (paper Open Problem 3 route).
