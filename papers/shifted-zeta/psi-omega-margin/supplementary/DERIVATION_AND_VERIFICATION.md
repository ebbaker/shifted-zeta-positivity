<!--
Date: 27 August 2026 (compiled from the round-13 recheck and the original derivation note).
Thread: psi_omega_margin (Paper 1) — supplementary derivation and verification record.
Status: live. This is a clean summary authored for the repository; the raw
        round-by-round research log is kept in the private project store (see STATUS.md).
-->

# Derivation and verification record — psi_omega_margin (Ψ_ω)

A self-contained companion to `psi_omega_margin.tex`: where each result comes from, how it was
checked, and the two corrections made to an earlier draft during the recheck. Every numerical
value below is reproduced by a script in `code/` (see the table at the end). Computations are
`mpmath` at 20–30 digits; Λ(n) by sieving.

## 1. The starting point (Suzuki)

Suzuki's §11 gives the shifted family Ψ_ω, its Laplace transform
`∫₀^∞ Ψ_ω(t)e^{izt}dt = −z⁻²(ξ′/ξ)(½+ω−iz)` (Im z > ½−ω), the zero-side series, and the
prime-side (arithmetic) series. The transcription of these four formulas was checked against the
source: the per-γ identity between the integral definition (11.1) and the zero-side series was
verified to 30 digits, including at complex γ (`code/c4_series_identity.py`).

## 2. The two closed forms

Define `A(ω) = Σ_γ (γ²+ω²)⁻¹` and `B(ω) = Σ_γ (γ²−ω²)(γ²+ω²)⁻²`. Evaluating the Hadamard
expansion `Σ_γ (z−γ)⁻¹ = (Ξ′/Ξ)(z)` at `z = ±iω` and using the functional-equation antisymmetry
`(ξ′/ξ)(1−s) = −(ξ′/ξ)(s)` gives, **unconditionally** (convergence needs only |Im γ| ≤ ½ < 14 ≤
|Re γ|):

> `A(ω) = ω⁻¹ (ξ′/ξ)(½+ω)`,  `B(ω) = (ξ′/ξ)′(½+ω) = d/dω [ ω A(ω) ]`.

Checked against direct summation over 250 zeros plus a Riemann–von Mangoldt tail: relative
discrepancy `1.13·10⁻⁴`, constant across ω (i.e. it is the tail-estimate error, not the
identity). `B(0) = Σ_γ γ⁻² = (ξ′/ξ)′(½) = 0.0462099862308…`, and `2B(0) = 0.09242… < 0.094`,
consistent with Suzuki's bound sup Ψ < 0.094. Monotonicity of A and the endpoint
`A(½⁻) = Σ_ρ 1/ρ(1−ρ) = 2+γ₀−log 4π = 0.0461914…` were verified on a grid.
(`code/c1_xi_values.py`, `code/c2_zero_sums.py`.)

## 3. The decomposition and the exact remainder

The clean identity behind the asymptotic is

> `(γ²−ω²)cos(γt) + 2γω sin(γt) = ½ e^{iγt}(γ−iω)² + ½ e^{−iγt}(γ+iω)²`,

verified to 10⁻²⁸ at complex γ (`code/c4_series_identity.py`). Dividing by
`(γ²+ω²)² = (γ−iω)²(γ+iω)²` gives the remainder in the form used throughout:

> `R_ω(t) = −(e^{−ωt}/2) Σ_γ [ e^{iγt}/(γ+iω)² + e^{−iγt}/(γ−iω)² ]`,

hence `|R_ω(t)| ≤ A*(ω) e^{−(ω−ϑ)t}` with `A*(ω) = ½ Σ_γ (|γ−iω|⁻² + |γ+iω|⁻²)`, and `A* = A`
under RH. The end-to-end test of the whole asymptotic against the **arithmetic** side (prime
powers p^m ≤ e¹⁵, no zeros used) sits inside the predicted envelope at every test point and
decays at the predicted rate (`code/c3_prime_side.py`); Suzuki's printed value
`Ψ(0.464002) = 0.03966175656…` is reproduced exactly, and `Ψ(0) = 0`.

## 4. Two corrections to the earlier draft (made during the recheck)

Both concern the earlier "universal threshold" statement and were fixed in the current paper.

1. **The old Theorem 1.3 was vacuous as stated.** Under RH, Ψ ≥ 0 pointwise (Suzuki Thm 1.7), so
   every term of the defining transform is non-negative and Ψ_ω ≥ 0 for *all* t — indeed Suzuki's
   §11 already notes, via Kreĭn–Langer, that any zero-free half-plane forces Ψ_ω ≥ 0 everywhere.
   The "there exists t₀" only weakens the *sufficiency* direction. The replacement (current
   Theorem 1.3) is the elementary linear lower bound with the explicit onset
   `t₀(ω) ≤ 0.0129 ω < 0.0065`, valid whenever the half-plane holds (boundary zeros included).
2. **The error constant was loose by a factor 2.** The two oscillatory terms combine into a
   single cosine of amplitude `γ²+ω²`, so under RH `|R_ω| ≤ A(ω)e^{−ωt}`, not `2A(ω)e^{−ωt}`.
   The equation `u + r = 2e^{−u}` and its root `u* ≈ 0.3748` were artifacts of bounding the two
   terms separately; the claimed range also failed near the endpoint (`u*(0.4999) > 0.3751475`).
   The clean bound removes all of this.

Other small fixes folded in at the same time: `W = +Ψ″` (a sign), the R_t normalisation
`2^{−1/2}`, the Fourier convention `φ̂(z) = ∫ φ(x)e^{izx}dx`, and the Nyman–Beurling contrast
remark rewritten onto the Balazard–Saias–Yor identity.

## 5. What the recheck confirmed

The main-term coefficients (Prop 1.1), the asymptotic's main term, the sensitivity proposition
(amplitude `2/(τ₀²+(δ−ω)²)`, rate δ−ω, phase `α = 2 arg(τ₀+i(δ−ω))`), and every table value
survived independent recomputation. The unconditional window (from RH verified to 3·10¹²) and the
phase-transition theorem were added and checked; the Dirichlet extension (q = 3, 4, 5), the
prime-side χ formula, and the Siegel-blindness proposition were derived and verified — see
`NEXT_STEPS.md` for the detail and `code/c5`–`c8` for the scripts.

## 6. Scripts

| script | verifies |
|---|---|
| `code/c1_xi_values.py` | (ξ′/ξ)(½+ω) and its derivative; B(0); monotonicity of the slope/ω; the withdrawn u* roots (documents correction 1) |
| `code/c2_zero_sums.py` | A, B by direct zero-sum + RvM tail vs the closed forms; Σ(Im ρ)⁻⁴ = 7.4346·10⁻⁵ (the t₀ constant) |
| `code/c3_prime_side.py` | prime-side Ψ_ω vs the asymptotic main term (no zeros used); Suzuki's printed value; Ψ(0)=0 |
| `code/c4_series_identity.py` | per-γ definition⟷series identity and the exponential decomposition, to 30/28 digits at complex γ |
| `code/c5_window.py` | the S-only unconditional window (t₋, t₊) |
| `code/c6_window_kv.py` | the zero-free-damped window E(t) and the endpoint law t₊ ≈ 0.72(½−ω)⁻² |
| `code/c7_dirichlet.py` | ξ(s,χ) checks; zero lists and counts (q=3,4,5); closed forms vs zero sums; conductor trend; Siegel-pair positivity |
| `code/c8_prime_side_chi.py` | the transform lemma (10⁻²²) and the prime-side Ψ_{ω,χ} vs main term |

Dependencies: `mpmath`, `numpy` (see `code/requirements.txt`).
