# Round 13: adversarial re-check of the Ψ_ω paper — two corrections, two strengthenings

**2026-08-27 (second pass).** Full re-derivation and independent numerics on
`PAPER_psi_omega_margin.tex` / `NOTE_psi_omega_margin.md`, against the full text of Suzuki
2206.03682 (read from `suzuki.pdf`, §§1–11 including the §11 prose around Theorem 11.1). The paper
has been revised in place. This round supersedes NOTE items 5 (universal threshold) and, in part,
7.2 (large-t numerics), and corrects the constant in item 4.

## 1. What survived verification (all re-derived and re-computed independently)

- Suzuki's §11 formulas as transcribed: the integral definition (11.1), the Laplace identity
  (11.2), the zero-side series, and the prime-side formula are **verbatim correct** against the
  source. Per-γ identity (definition ⟷ series) verified to 30 digits, including complex γ.
- **Prop AB** (`A(ω) = ω⁻¹(ξ′/ξ)(½+ω)`, `B(ω) = (ξ′/ξ)′(½+ω)`): correct — and in fact
  **unconditional** (convergence needs only |Im γ| ≤ ½ < 14 ≤ |Re γ|). The paper conditioned it
  on ϑ < ω unnecessarily; now stated unconditionally.
- **Theorem asym main term**: correct, and unconditional; only the remainder's decay uses the
  hypothesis.
- **Prop sens**: re-derived exactly, amplitude `2/(τ₀²+(δ−ω)²)`, rate `δ−ω`, phase
  `α = 2 arg(τ₀+i(δ−ω))` — all confirmed; the sens table's numbers reproduce analytically
  (drift-only rows match `log((60ωA₀+B₀)/(40ωA₀+B₀))/20 = 0.01838 / 0.01682`).
- **All numerics**: Check 0 exact (`Ψ(0.464002) = 0.03966175656`); all six prime-side rows
  reproduce to 9 digits (fresh sieve to e¹⁵); slope/B/r table values exact; `B(0) =
  0.0462099862308`.

## 2. Correction 1 — the "universal threshold u* ≈ 0.3748/ω" is withdrawn

NOTE §3 / old Theorem 1.3 ("Assume RH … Ψ_ω > 0 for t > u*/ω, u* ∈ [0.374822, 0.375148]") fails
twice over:

1. **It was vacuous as stated.** Under RH, Ψ ≥ 0 pointwise (Suzuki Thm 1.7), and every term of
   definition (11.1) has a nonnegative kernel, so Ψ_ω ≥ 0 for **all** t — t₀ = 0, trivially.
   Worse: **Suzuki's §11 itself already observes** (via Kreĭn–Langer, [14, Satz 5.9]) that *any*
   zero-free half-plane Re s > ½+ω forces Ψ_ω ≥ 0 **everywhere**. The "there exists t₀" in
   Theorem 11.1 weakens only the *sufficiency* direction. Missed on first read; now cited in the
   paper (§1.4, Remark 5.2).
2. **The constant 2 was loose.** `(γ²−ω²)cos θ + 2γω sin θ` has amplitude exactly `γ²+ω²`, so
   under RH |R| ≤ A(ω)e^{−ωt}, not 2A(ω)e^{−ωt}; the equation `u + r = 2e^{−u}` and its root
   0.3748 were artifacts of bounding the two oscillatory terms separately. (Also the claimed
   range failed near the endpoint: u*(0.4999) = 0.3751606 > 0.3751475.)

**Replacement (stronger, and elementary).** Clean remainder form:
`R = −(e^{−ωt}/2) Σ_γ [e^{iγt}/(γ+iω)² + e^{−iγt}/(γ−iω)²]`, giving
`|R| ≤ A*(ω) e^{−(ω−ϑ)t}` with `A* := ½Σ(|γ−iω|⁻² + |γ+iω|⁻²)`, valid up to ϑ = ω, `A* = A`
under RH. Per-zero identity:

> `A* − B = Σ_γ [(b−ω)²/|γ−iω|⁴ + (b+ω)²/|γ+iω|⁴] ≤ 8ω² Σ_ρ (Im ρ)⁻⁴ = 8ω² · 7.4346×10⁻⁵`,

and `ωA(ω) = (ξ′/ξ)(½+ω) ≥ (2+γ₀−log 4π)ω` — A(ω) is **decreasing, unconditionally**, from
0.046210 to `Σ 1/ρ(1−ρ) = 2+γ₀−log 4π = 0.0461914` (the same constant as the Nyman–Beurling
floor of ROUND9, since `γ²+¼ = ρ(1−ρ)`). New Theorem 1.3: **whenever ξ ≠ 0 for Re s > ½+ω (the
only case the criterion holds), Ψ_ω(t) ≥ margin − A* for all t, and Ψ_ω(t) > 0 for every
t > t₀(ω) ≤ 0.0129·ω < 0.0065** — a bounded threshold, covering even boundary zeros ϑ = ω,
where a boundary quartet's undamped oscillation (amplitude 2/τ²) is covered twice over by its own
contribution (4/τ²) to the intercept B. What the theorem adds over Suzuki's pointwise ≥ 0 is the
explicit linear lower bound and the elementary proof (no Kreĭn–Langer).

## 3. Correction 2 — the error constant in headline item 4

Abstract/theorem constant under RH is now `ω⁻¹(ξ′/ξ)(½+ω)` (factor 2 removed), and `A*(ω)` in
general.

## 4. New: unconditional window — and NOTE §7 item 2 is dead

Splitting the remainder at the verification height `T_v = 3×10¹²` (Platt–Trudgian, BLMS 53
(2021)): unconditionally

> `Ψ_ω(t) ≥ margin − A(ω)e^{−ωt} − S·e^{(½−ω)t}`, `S = Σ_{|τ|>T_v} τ⁻² < 3.2×10⁻¹²`.

Windows of unconditional positivity (t₋, t₊): ω=0.05: (8×10⁻⁵, 55.1); 0.1: (1.6×10⁻⁴, 63.7);
0.25: (4×10⁻⁴, 107.2); 0.4: (6.4×10⁻⁴, 282.1); 0.49: (7.9×10⁻⁴, 3079). In x = eᵗ: 10²⁴ to
10¹³³⁷. **So "compute Ψ_ω past e²⁰ as a Θ-probe" (NOTE §7 item 2) is provably fruitless**: every
feasible argument sits deep inside the window where positivity is already unconditional.

The same mechanism corrects the framing of NOTE §7 item 1 / old §7.4: **zero-density estimates
cannot bound the obstruction by the margin for any ω** — they bound counts, are consistent with a
single zero at any β < 1, and one permitted zero gives e^{(β−½−ω)t}, defeating any linear margin
as t → ∞. Structural, not a matter of effort. What density/zero-free inputs *do* control is the
**onset** of possible failure (KV forces zeros with β near 1 to height ≥ exp(c(1−β)^{−3/2}));
the productive quantitative program is pushing the window, not proving the criterion. Rewritten as
§9.4 of the paper.

## 5. Other fixes in the paper

`W = +Ψ″` (sign was wrong); `R_t` carries the normalisation 2^{−1/2}; Fourier convention
`φ̂(z) = ∫φ(x)e^{izx}dx` added to the explicit formula (matches Suzuki §3); Suzuki's semigroup /
monotone-in-ω law recorded (Remark 2.2); NB-contrast remark rewritten on the Balazard–Saias–Yor
identity (detection needs log N ≳ τ²/δ) instead of the vaguer "exponentially small perturbation";
Guth–Maynard updated to Ann. of Math. (2) 203 (2026); added Platt–Trudgian, BSY, Trudgian (2014,
explicit N(T)), Davenport, Titchmarsh; the 12-citation claim dated "as of August 2026". Compiled
clean (pdflatex, 15 pp., no undefined refs).

## 6. Updated next steps

1. **Push the window** — feed KV zero-free region + density estimates through the remainder
   decomposition to extend Prop 1.6 beyond the verification height. This is the honest
   quantitative program that replaces old §7.4's question (which has a structurally negative
   answer as posed).
2. **Selberg-class / GRH version** — Suzuki 2209.12832 has screw functions for the extended
   Selberg class *without* the shift; adding the shift gives the graded criterion with margin
   slope `(ξ_F′/ξ_F)(½+ω)` essentially mechanically, and would widen the paper's interest.
3. **ω_c as a critical point** — the family is monotone in ω (semigroup law); is there a sharper
   statement at ω = ω_c (e.g. behaviour of the margin/oscillation balance as ω ↓ ω_c)?
4. NOTE §7 items 3 (Bombieri Rend. Lincei §8 priority read) and 4 (write to Suzuki) stand.

## 7. Reproduction (this round)

| script | produces |
|---|---|
| `c1_xi_values.py` | slope/B/r table, u* roots incl. endpoint failure, (ξ′/ξ)(½+ω)/ω monotonicity |
| `c2_zero_sums.py` | S₄ = Σ(Im ρ)⁻⁴ = 7.4346×10⁻⁵, A/B direct-vs-closed, new t₀ bound 0.0129ω |
| `c3_prime_side.py` | prime-side table rows (sieve to e¹⁵), Check 0 |
| `c4_series_identity.py` | per-γ identity, exponential decomposition, A*−B identity (30 digits) |
| `c5_window.py` | S < 3.2×10⁻¹², unconditional windows (t₋, t₊) |

`mpmath`, `numpy`. Sources: `suzuki.pdf` (full §11 text), Platt–Trudgian BLMS 53 (2021),
Balazard–Saias–Yor Adv. Math. 143 (1999), annals.math.princeton.edu (Guth–Maynard, Ann. of Math.
203 (2026) no. 2), ROUND9 §§1–2 (NB floor and insensitivity mechanism).
