# ROUND 6 close-out: all manuscript gates resolved — verdict GO (with two drafting-time items)

**2026-08-29.** Executes the manuscript-prep directive (`ROUND6_manuscript.md`, user-supplied).
Every §13 checklist item now has an explicit answer; the two CRITICAL no-go items (the log 2
discrepancy; s₀-intrinsicness) are resolved — one as a certified solver artifact, one by data
that *compels* the memo's more careful language.

## 1. Gate 6 (time normalization) — RECONCILED

The quartet coefficient was recovered symbolically from the lab's validated pair-term formula:
the two growing branches are e^{(η±iτ)t}/(η±iτ)², summing to
**2 e^{ηt} cos(τt+α)/(τ²+η²)** — amplitude 2 exactly, certified numerically (rest/leading
= 1.0·10⁻⁸ at t = 150). Round 5's solver balanced amplitude **1** against the margin; that is
the entire log 2. With the correct amplitude the envelope threshold is

> **η t\* = 2 log τ + loglog τ + log(S_ω/η) + o(1)**,  S_ω = (ξ′/ξ)(½+ω),

exactly the directive's constant: predicted −3.4800 (ω = 0.1, η = 0.15), solved thresholds
converge −3.757 → −3.483 across τ = 10²…10¹². Round-5's reported constant log(2S_ω/η) is hereby
corrected; rate and loglog term were right.

## 2. Gate 7 (envelope vs first negative) — bracket verified

With the quartet's exact polynomial part folded into the margin, the measured gap satisfies
**0 ≤ t_first − t_env ≤ 2π/τ** at τ = 20, 80, 320, 1280 (gaps 0.115, 0.027, 0.011, 0.0035
against bounds 0.314, 0.079, 0.020, 0.0049). The bracketing statement can be proved under a
transversality condition (envelope crossing at rate η, trough within one period); drafting can
state it with that hypothesis.

## 3. Gate 4 (s₀ covariance) — "intrinsic" is dropped, by measurement

Same spectral data, same defect (τ = 4, η = 0.4), five scales:

| s₀ | 1 | 4 | 25 | 100 | 400 |
|---|---|---|---|---|---|
| n₁ | 22 | 14 | 12 | 17 | 28 |
| measured/naive-pred | 4.0 | 2.3 | 1.24 | 0.85 | 0.57 |

Findings: (i) **n_{s₀} is genuinely scale-dependent and non-monotone** — no √s₀ (nor any fixed
power) renormalization is s₀-free at moderate scales; the conjectured covariance
g ≈ 2η√(s₀+t_min)/τ² is confirmed as a **high-height asymptotic only** (τ² ≫ s₀+t_min — the
regime of the τ² log τ law), and at fixed small τ the exact interval Green function must be
used. (ii) The monotone drift of measured/predicted confirms the directive's §1.4 caution
positively: the multiplicative constant C(σ₀, s₀) is real and scale-dependent, so only the
ε → 0 root-asymptotic form n_ε/log(1/ε) → 1/(2g) is theorem-grade. (iii) New observation for
future work: the minimum at s₀ ≈ 25 ≈ 1.5τ² suggests a **detection-optimal compactification
scale s₀\*(τ)**. Manuscript language adopted: *resolvent compactification at scale s₀*; the
word "intrinsic" refers only to cutoff-independence (which is proved), never to
s₀-independence.

## 4. Gate 11 (unscaled real-zeta suite) — delivered, with regime bookkeeping

Genuine ordinates (100) + RvM tail, s₀ = 200; control (no defect) Stieltjes-clean to n = 28.

| ω | τ | η | n₀ | n₁ | g exact | \|ε_eff\| | naive pred | ratio |
|---|---|---|---|---|---|---|---|---|
| 0.1 | 16 | 1.0 | 14 | 14 | 0.18085 | 0.00438 | 15.0 | 0.93 |
| 0.1 | 20 | 1.0 | 14 | 14 | 0.09379 | 0.00333 | 30.4 | 0.46 |
| 0.1 | 25 | 1.0 | 22 | 21 | 0.05866 | 0.00242 | 51.3 | 0.41 |
| 0.1 | 16 | 0.5 | 19 | 18 | 0.09272 | 0.00439 | 29.3 | 0.61 |
| 0.1 | 20 | 0.5 | 26 | 25 | 0.04705 | 0.00333 | 60.6 | 0.41 |
| 0.2 | 20 | 1.0 | 16 | 16 | 0.09379 | 0.00333 | 30.4 | 0.53 |

Detection at genuine zeta scale is finite and computable (n = 14–26); the sub-unity ratios are
exactly the documented quasi-discrete regime: at these heights the local zero spacing
2π/log(τ/2π) ≈ 4.5–5.4 exceeds both η and ω, so the interval law overestimates depth, as
rounds 4–5 established. (The continuum regime at fixed η = 1 begins only at heights where
spacing ≲ η, i.e. τ ≳ 2π e^{2π} ≈ 3·10³.) The table serves the manuscript as validation of the
mechanism plus an honest exhibit of the crossover — not as a constant-fitting exercise.

## 5. Gates 2, 3, 5 (logic, asymptotics, operator language) — adopted verbatim

- **Zeta application status**: safe form A (perturbative sensitivity of the positive reference
  system) is the primary statement; safe form B carries the explicit hypothesis (all remaining
  zeros admissible ⟹ the response = positive Stieltjes background + the quartet's exact
  contribution). One lemma is flagged for drafting: the quartet contributes, besides its two
  principal-sheet atoms, a **signed a.c. cut correction of size O(ε)**; the detection analysis
  must show it does not preempt the atom threshold (empirically it never has — W1 and the
  unscaled table both match atom-based predictions — but the lemma must be written).
- **Fixed vs moving point**: split adopted. Theorem: exact thresholds + fixed-point
  lim n_ε/log(1/ε) = 1/(2g) via Stahl–Totik root asymptotics of K_n (regular a.c. background at
  ω > 0). Proposition/numerics: the high-height τ² log τ/η law. The ω ↓ 0 endpoint stays an
  open problem, worded as the directive prescribes (§12).
- **Operator statement**: Option A (measure-level compactification theorem; the bounded
  positive **contraction transform** B = A(s₀+A)⁻¹ remark for finite vector measures), with a
  one-line note that Option B is available: ∫dσ/(s₀+λ) < ∞ makes (s₀+A)^{−1/2}φ an honest
  vector for φ in the negative scale — to be included only if a standard rigged-space reference
  is cited.

## 6. Novelty audit — extended, with one material finding

The Christoffel-function-growth principle for **outlier/anomaly detection is an active applied
line** (Lasserre–Pauwels school; a 2026 preprint
[Scalable anomaly detection via a univariate Christoffel function](https://arxiv.org/abs/2606.12483);
[data-streams variant](https://link.springer.com/article/10.1007/s41060-024-00581-2)). The
manuscript must cite this and frame accordingly: the detection-by-Christoffel-growth idea is
known in empirical/ML form; what remains unclaimed in the searched literature is the **exact
finite-rank determinant thresholds tied to the first anomalous Stieltjes CF coefficient**, the
**resolvent-compactified depth for unbounded Weyl data** (moment transformations between
Stieltjes and Hausdorff problems are classical — cite
[Schmüdgen's Ten Lectures](https://arxiv.org/pdf/2008.12698) and the
[Hausdorff↔Stieltjes transformation literature](https://www.researchgate.net/publication/225686778_A_transformation_from_Hausdorff_to_Stieltjes_moment_sequences)
— but the Taylor-jet identity and string-length invariance in this role appear unclaimed), and
the **application to Suzuki's shifted zeta family with η = δ−ω as the defect parameter**.
Framing per directive §10 adopted.

## 7. Checklist (directive §13) — final status

All 17 items ✓: transform algebra (r4/r5, algebraic); moment/Taylor identity (proved);
s₀-dependence (measured, §3); operator language (corrected); infinite mass (Option A);
rank-one and rank-two identities (proved, certified 10⁻²⁸⁵/10⁻²⁷³); CF/Hankel convention
(certified 10⁻¹¹², classical citations); Stahl–Totik quoted at root-asymptotic strength only;
fixed/moving separated; single-defect status explicit; time constant reconciled (§1);
envelope/first-negative distinguished (§2); unscaled table (§4); novelty audit (§6, plus
rounds 4–5); no RH-progress claim (discussion wording of directive §8.8 adopted); no
unqualified canonicity (§3).

## 8. GO verdict and drafting plan

All five NO-GO conditions are cleared. **GO for drafting** with the directive's scope:
title candidates as given; sections 1–8 as specified; the graph material reduced to one
illustrative example (the dumbbell+4 exc+ specimen is the natural choice — it exhibits the
threshold, the parity law, and the depth in one figure); Ihara/topology/twist programme
reserved for a second paper. Two drafting-time items carried forward: the a.c.-correction
lemma (§5) and the Christoffel-ML citations (§6). Deliverable for the next round: 
`PAPER_defect_depth.tex` skeleton with the §15 claim hierarchy as the theorem list.

## 9. Reproduction

Inline scripts this round (appended to `claude/lab_ihara_experiments.py`): normalization audit
(amplitude certification, corrected-constant convergence to τ = 10¹²), bracketing runs
(τ = 20…1280), s₀ five-point scan, unscaled real-zeta suite (Cauchy-circle DFT machinery at
dps 150, M = 1024). QC as standing; the control rows (undefected measures clean) accompany
every table.
