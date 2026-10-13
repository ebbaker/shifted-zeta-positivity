# Round 14: independent check of the concise (ChatGPT) draft — verified, with fixes

**2026-08-28.** Teddy ran the 21 pp. paper through ChatGPT, which produced a 9-page
collaboration draft (`psi_omega_margin_concise.tex`, retitled "Quantitative asymptotics for
Suzuki's shifted screw functions") intended for a first approach to Suzuki and other
mathematicians. This round is a full independent verification of that draft against the project's
verified results (ROUND13, PROGRESS, NOTE_oneside_criterion) plus fresh numerics. The canonical
concise draft is now `claude/PAPER_psi_omega_concise.tex`.

## 1. Verdict

The condensation is faithful and the strategy is sound. Every theorem in the concise draft is a
result this project has already verified (exact decomposition, A/B closed forms, threshold,
critical-shift dichotomy = the order-parameter theorem with the physics language removed,
single-quartet sensitivity, Ψ^[1] criterion, pointwise one-sided corollary, L¹ theorem). Every
proof was re-derived line by line this round and every numerical constant recomputed in mpmath
(B(0), 2+γ₀−log 4π, Σ(Im ρ)⁻⁴, Σ|γ|⁻³, the t₀ coefficient, the 0.0316 onset; the R-decomposition
and A*−B identities re-checked to 25+ digits).

## 2. ChatGPT's monotonicity correction is real — and the FULL paper still has the bug

The 21 pp. `PAPER_psi_omega_margin.tex` (Prop 3.x monotonicity of A) asserts
"X>|Y| is equivalent to (|a|−|b|)²+ω²>0". This is algebraically false:
X−|Y| = (|a|−|b|)² + ω² − 2b² (verified symbolically and numerically; at (a,b,ω)=(50,0.3,0.1)
the two sides differ by exactly 2b² = 0.18). The RESULT is fine — X−|Y| ≥ 14²−¼−14 > 0 from
|a|≥14, |b|≤½ — which is the proof the concise draft now carries. **Action item: patch the same
step in `PAPER_psi_omega_margin.tex` before it goes anywhere.**

## 3. Fixes applied to the concise draft this round

1. **δ-range in Corollary 4.2 / final remarks.** "some δ>0 ⟹ Θ≤1−δ" is only proved for
   δ ≤ ½−ω (for larger δ the hypothesis has ε<0; the transform's double pole at z=0 — the linear
   main term — blocks Landau below 0, so the method caps at Θ ≤ ½+ω there). Now stated as
   δ ∈ (0, ½−ω]. Same imprecision exists in the full paper's Cor. 10.7(iii) — fix there too.
2. **Real-γ case in the monotonicity proof.** Pairing γ with γ̄ is the identity pairing for real
   γ (would double-count); real γ now handled separately (trivially decreasing).
3. **Numeric precision.** Σ_ρ(Im ρ)⁻⁴ = 7.43452×10⁻⁵ (1000 zeros + RvM tail), so the draft's and
   ROUND13's "7.4346×10⁻⁵" was off in the 5th digit → now "7.4345…×10⁻⁵ < 7.44×10⁻⁵". Likewise
   "t₀ ≤ 0.01288…ω" was wrong as a decimal expansion (true coefficient 0.012876) → theorem now
   states the safe bound t₀ ≤ 0.0129ω < 0.0065, proof shows the 7.44e-5 chain.
4. **Dangling references.** Ingham and Kreĭn–Langer were in the bibliography but uncited. Now
   cited where they belong: Kreĭn–Langer at Suzuki's pointwise-positivity remark (§1) and in a new
   remark after Theorem 3.2; Ingham Ch. V in the §4 preamble, positioning the one-sided section
   honestly as twice-integrated damped analogues of E. Schmidt/Landau oscillation theorems —
   Suzuki will know these, so the draft should place itself relative to them.
5. **New remark after the threshold theorem** pre-empting the obvious referee reaction ("Suzuki
   already has Ψ_ω ≥ 0 everywhere"): what the theorem adds is the linear lower bound (the
   criterion is never asymptotically saturated) and an elementary, Kreĭn–Langer-free proof.
6. Abstract: A*(ω) flagged as "an explicit constant"; date bumped.

## 4. On the two removals (both justified)

- **Unconditional-window proposition**: correctly retracted from the concise draft. Beyond the
  proof needing a genuine Stieltjes treatment of the zero-counting error, the endpoint law
  t₊ = (4/c+o(1))(½−ω)⁻² as ω→½⁻ is not the literal asymptotic: per PROGRESS §1 the KV branch
  takes over for ½−ω ≲ 2×10⁻⁵ and gives t₊ ≍ (½−ω)^{−5/2−o(1)}. The full paper's Prop. 1.6
  states the (½−ω)⁻² law in the literal limit — **also needs fixing in the full paper** (restrict
  to the classical-branch regime or state as a lower bound).
- **Dirichlet/Siegel section**: fine to hold back; final remarks flag it. The verified material
  (PROGRESS §2) is ready to restore on interest.

## 5. Status

- Concise draft: verified, corrected, compiles clean (pdflatex, 9 pp.), delivered to Teddy.
  Author/address placeholders still blank for him to fill.
- Strategy: use the concise draft for the first contact (per ROUND13 §6 item 4 / PROGRESS §4b
  draft letter); numerics + Dirichlet material as a follow-up.
- Open action items on the FULL paper before any wider circulation: (a) monotonicity-proof step
  (§2 above), (b) Cor. 10.7(iii) δ-range, (c) endpoint-law statement in Prop. 1.6, (d) the same
  7.4345 vs 7.4346 digit.

## Reproduction

`check_constants.py` (mpmath, dps 25–30): B(0)=0.0462099862308…, endpoint 0.0461914179…,
S₄=7.43452×10⁻⁵ (300 and 1000 zeros, RvM tail), S₃=Σ|γ|⁻³=0.00145911, 8S₄/endpoint=0.0128760,
S₃/B(0)=0.0315756, slope/ω monotone 0.04621→0.04619, R-decomposition identity residual ~1e-27,
A*−B quartet identity residual ~4e-34, old-proof gap = 2b² exactly.

## 6. Update (2026-08-28)

Letter to Suzuki **sent** by Teddy on 2026-08-28, with the corrected concise draft attached and an
AI-use acknowledgement section (Claude: derivations/verification/numerics/drafting; ChatGPT:
condensation/editing/review incl. one proof correction) added to the tex. Awaiting reply. While
waiting, the natural next task is item 5 of §5: apply the four flagged fixes to the full
`PAPER_psi_omega_margin.tex` so it is ready to send if he engages.

## 7. Full-paper patches applied (2026-08-28, same day)

All four §5 action items on `PAPER_psi_omega_margin.tex` are now **done** (patched in place,
pdflatex clean, 24 pp., no undefined refs):
(a) monotonicity proof now argues X−|Y| = a²−b²+ω²−2|ab| ≥ 14²−¼−14 > 0 directly (real-γ case
noted); (b) Cor. oneside(iii) restricted to δ ∈ (0, ½−ω]; (c) endpoint law restated: t₊ ≈
(4/c)(½−ω)⁻² only in the classically-governed regime (½−ω ≳ 4·10⁻⁵), with the true literal-limit
asymptotic t₊ = (½−ω)^{−5/2+o(1)} from the KV branch — abstract, Prop. window, proof, and both
discussion mentions all updated; (d) S₄ digit corrected to 7.4345…×10⁻⁵ and the theorem constant
to 0.01287…ω (proof chain via 7.44e-5 → 0.01288…ω unchanged and still correct).
