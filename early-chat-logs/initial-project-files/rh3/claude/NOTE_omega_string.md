# The unconditional ω-string of ζ: spectral measure identified, string computed

**2026-08-28.** First concrete round of the physics/inverse-spectral companion paper
(ROUND14 follow-up). **Revised same day (Round 15):** claims re-tiered after external
referee-style feedback; two numerical errata fixed; the §1 measure identification and the §1
representation/margin identity are now proved as Theorems A–B, and the degeneration claims as
Theorems E/E′, in `ROUND15_referee_audit_omega_string.md` — read that doc alongside this one.
Everything below is for the shifted family at ω ≥ 1/2, where the Kreĭn–Langer correspondence
applies **unconditionally** (ξ ≠ 0 on Re s ≥ 1 is classical). Conventions aligned with Suzuki
JLMS §9 (read from `suzuki.pdf`): string S[m,L], equation dy′ + z y dm = 0, Weyl function
q(z) = lim_{x→L} ψ/φ = b + ∫₀^∞ dσ(λ)/(λ−z); his RH-conditional case is
q_ξ(z) = i(ξ′/ξ)(½−i√z)/√z with masses 2 at λ = γ² — Kotani's "zeta string",
m_ξ(x) ~ 4x(log x)⁻² as x→0+.

## 1. The object and its spectral measure (Theorem A; verified 6 ways)

For ω ≥ 1/2 define **q_ω(z) := i(ξ′/ξ)(½+ω−i√z)/√z ∈ N_S** (unconditionally; ROUND15 Thm A).
Its spectral measure is **absolutely continuous**:

> dσ_ω(λ) = ρ_ω(√λ)/√λ dλ on λ ≥ 0, equivalently dµ_ω(u) = ρ_ω(u)du on ℝ (even), with
> **ρ_ω(u) = (1/π) Re(ξ′/ξ)(½+ω+iu) = (1/π) Σ_ρ (σ−β)/((σ−β)²+(u−τ)²)**, σ = ½+ω
>
> — the zero-counting measure smeared by Poisson kernels whose width is each zero's
> distance to the line Re s = ½+ω (width = ω for a zero exactly when that zero is on the
> critical line; so "all widths = ω" is an RH-conditioned statement).

Numerical verification (`s1*` scripts, mpmath):
1. **Closed form vs Lorentzian zero-sum** (1000 zeros + RvM tail): reldiff 1e-5…1e-7 at
   ω = 0.5, 0.75 across u = 0…60. ✓
2. **Prime side** at σ = 2 (Λ-sieve to 3·10⁵): diff ~ 2e-7. ✓
3. **Positivity** at ω = ½ on u ∈ [0,200]: min = ρ(0) = (ξ′/ξ)(1)/π = 0.0073516 > 0. ✓
4. **Integrated spectral measure has the same leading Riemann–von Mangoldt growth as the
   zero-counting function**: ∫₀^100 ρ = 29.111 vs N(100) = 29.002 (smearing-level agreement);
   N_σ(u) ~ (u/2π)log(u/2πe). (An a.c. measure is not an eigenvalue count of a discrete
   operator — no Hilbert–Pólya claim is made here.) ✓
5. **Spectral representation** Ψ_ω(t) = ∫_ℝ (1−cos ut)/u² ρ_ω(u)du (now ROUND15 Thm B, exact
   normalization proved via the Laplace-transform block), tested against Suzuki's explicit
   arithmetic Ψ_{1/2} formula: reldiff 1.3e-6 (t=2), 2.8e-5 (t=5), 2.8e-4 (t=10; residual =
   tail truncation). Consequence (Thm B corollary): **margin slope = π·ρ_ω(0)** — the linear
   margin of the ROUND13/14 paper is exactly π × (spectral density at u = 0, in the
   frequency-line normalization). ✓
6. **Weyl function = Stieltjes transform of dσ_ω** at complex test points: reldiff 4e-7;
   per-pair residue identity re-verified in ROUND15 to 1e-33…1e-44. ✓

## 2. The string, computed (the *discrete* inverse problem solved to high precision)

Method: discretize dσ_ω by Gauss–Legendre panels (≤ 152 point masses), then recover the
unique Stieltjes string by **Herglotz peeling** — m₁ = 1/σ(ℝ), l₁ = σ₀²/σ₁, new measure =
poles/residues of 1/(1/q + zm₁), iterated with bracketed root-finding (one root per gap,
guaranteed by interlacing), at dps 90–120. Validation: synthetic round-trip exact to 1e-121;
every production string reproduces its target q(z) to ≤ 1e-117; all masses/lengths positive.
**Scope of the 1e-117 figure:** it certifies inversion of the finite *discretized* measure
only; convergence of the finite string to the continuum ζ-string is a separate question whose
error is quadrature/discretization-dominated and is what the flat-control calibration below
measures.

**Results (ω = 0.5, 0.75, 1.0; scripts s3–s10):**

- **Bulk (IR) law: ρ_∞(ω) = (ξ′/ξ)(½+ω)⁻² — now ROUND15 Thm C (proved modulo one Kasahara
  citation).** Analytic origin: q_ω(−y) → (ξ′/ξ)(½+ω)/√y as y→0⁺, the Weyl function of a
  homogeneous string of density slope⁻². Numerics: raw secant fits give fitted/predicted =
  1.30760, 1.30774, 1.30776 at ω = 0.5, 0.75, 1.0 — the **ω-scaling law is exact to ~1e-4**;
  the common 1.308 is pure discretization bias, measured on an exactly-solvable flat control
  (same grid): 1.30826. Control-corrected absolute agreement: **0.9995, 0.9996, 0.9996**
  (validation of Thm C, not its proof). At ω = ½ the unconditional bulk density of the zeta
  string is (ξ′/ξ)(1)⁻² = **1874.7243** [erratum, was 1874.7255; slope closed form
  (ξ′/ξ)(1) = γ/2 + 1 − ½log 4π = 0.0230957090].
- **Profile:** M_ζ(x)/M_flat(x) (bias-cancelled) rises from ≈0 (light, Kotani-type UV
  region) through an **arithmetic crossover at x ≈ 0.05–1** (dual to the first zeros:
  x ~ q(−γ₁²) ≈ 0.05) to the homogeneous bulk (= 1 within 1e-3 for x ≳ 3). (Numerical
  evidence; the crossover location is the one structural feature with an analytic anchor.)
- **UV law: now ROUND15 Thm D (proved modulo the same citation).** Kotani's m(x) ~ 4x(log x)⁻²
  is the y→∞ limit of the Kasahara dual pair x(y) = q(−y), M ~ 1/(y q(−y)) — for the ω-strings
  this holds **unconditionally** with identical leading form (RvM density is ω-independent).
  [Erratum, was "ratio → 1.08 at y = 1e-6":] on the analytic dual curve the ratio
  M/[4x/log²x] is 374, 4.26, 1.388, 1.093, 1.008, 0.974 at y = 1, 10³, 10⁶, 10⁹, 10¹², 10¹⁵,
  → 1 (non-monotone, slowly varying corrections). Numerically unreachable in the
  reconstructed string at feasible cutoffs (needs log²x ≫ 1): an analytic statement.
- Total length L = ∞ (q(0⁻) = ∞); the spectrum is **purely absolutely continuous**.

## 3. The dictionary this establishes — tiered (was "all rigorous"; re-tiered per referee)

**Theorem-grade (ROUND15):**
- ζ carries an unconditional one-parameter family of Kreĭn strings/canonical systems built
  from PNT-grade arithmetic (Thm A); margin slope = π·ρ_ω(0) (Thm B) and, modulo one
  citation, = 1/√ρ_∞ (Thm C).
- **Degeneration:** RH ⟺ the family extends to all ω > 0 (Thm E′: below ω_c, q_ω has
  non-real poles, the Herglotz property fails, and no positive string realization exists —
  whether the formal boundary density ρ_ω itself goes negative below ω_c is open and not
  needed). Under RH, as ω↓0 the measures converge vaguely to Kotani's pure-point measure
  2Σδ_{γ²} (Thm E): an **a.c.-to-pure-point spectral transition** at exactly ω = 0. On the
  time side, thm:transition of the margin paper gives the order-parameter jump.

**Standard consequence once cited:** the UV law m ~ 4x/log²x (Thm D); string convergence
m_ω → m_ξ at continuity points under RH (Thm E(iii), Kreĭn-correspondence continuity).

**Numerical evidence:** DOS = RvM mean + prime oscillations at smearing level; the
UV–crossover–bulk profile; the absolute IR constant (control-corrected 0.9995–0.9996).

**Physics gloss (interpretation only, after the mathematics):** zeros ↔ Lorentzian resonances
(width ω under RH); ω ↔ broadening/damping scale; margin slope ↔ zero-energy DOS; bulk
density ↔ inverse square of the margin slope ("the central quantity of the margin paper is
the bulk sound speed"); ρ_∞ ~ (B(0)ω)⁻² → ∞ as ω↓0 under RH (the bulk becomes infinitely
heavy). Words like "localization" and "phase transition" are glosses — no eigenfunction or
dynamical statement is claimed.

## 4. Caveats / open items for the companion paper

1. ~~The measure identification (§1) needs the two-line analytic proof written out~~ **done**
   (ROUND15 Thm A: paired Hadamard + residue lemma + Kreĭn–Langer [16] Thm 5.1); Thm B does
   the representation and normalization.
2. Absolute IR constant demonstrated via control-cancellation; a direct high-resolution
   computation needs uniform-in-u node spacing δu ≈ π/(X√ρ_∞) (N ~ 10³–10⁴ masses —
   O(n³) peeling infeasible; a Gelfand–Levitan or Padé/Kasahara route would do better).
3. ~~UV Kotani law: prove via Kasahara~~ **reduced to citation-pinning** (ROUND15 Thms C–D:
   proofs written; need the precise numbered theorems in Kasahara 1975 / Kac–Kreĭn /
   Kotani–Watanabe — retrieval task like the Bombieri §8 check).
4. Contact points: Kotani (ResearchGate 348522988), Burnol's Kreĭn string (ROUND11 §3.7c),
   Lagarias 2006 de Branges realizations, Berry–Keating regularized count.
5. Candidate titles now from the referee's §9: "The Shifted Zeta String: An Unconditional
   Inverse-Spectral Family and Its RH Endpoint" / "Poisson-Broadened Zeta Zeros and the
   Shifted Kreĭn String". Structure: Theorems A, B, C, D, E′, E; physics dictionary last.
6. Figure spec (referee §5): density figure retitled "Poisson-smoothed zero spectral
   measure"; caption conditions widths on RH with the low plotted zeros noted as verified;
   exact density visually distinguished from the RvM mean. String figure framed as numerical
   evidence; bulk density attributed to Thm C with numerics as validation.

## 5. Reproduction

`~/work/omega_string/` (session of 2026-08-28 a.m.): `common.py` (ξ′/ξ with Stieltjes-series
regularization at s=1), `s1*_measure` (six checks), `s2_string.py` (peeling + forward map),
`s3_run.py` (production runs: w05_main/ext/coarse/ir, w075, w10), `s5–s7` (Kasahara,
convergence, IR fits), `s8–s10` (flat-control calibration + bias-cancelled ratios),
`s11_figs.py` (fig_density.png, fig_string.png). All strings forward-verified ≤ 1e-117.
Round 15 additions: `~/work/round15/v1_identities.py`, `v2_thmE_kasahara.py` (residue lemma,
transform block, errata recomputation, Thm E convergence tables) — outputs recorded in
`ROUND15_referee_audit_omega_string.md`.
