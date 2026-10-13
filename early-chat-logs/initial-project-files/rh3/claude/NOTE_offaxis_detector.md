# A velocity-residual detector for off-axis zeros of Ξ and Selberg-class L-functions

**Draft paper. 2026-08-25.** All numerics reproduced by the scripts in the Round-3/4 bundles.
Target: a short methods paper. Everything below is unconditional (no RH assumed anywhere);
"certified" means rigorous modulo floating-point (an interval-arithmetic port, e.g. ARB, is the
remaining engineering).

---

## 1. Setup

Let `Ξ(z) = ξ(1/2 + iz)` — even, entire, order 1, real on ℝ, zero multiset `{±ρ_k}` with
`Σ 1/|ρ_k|² < ∞`, so the genus-0-in-`z²` Hadamard product `Ξ(z) = Ξ(0) ∏ (1 − z²/ρ_k²)` converges.
Everything below uses only these properties, so it applies verbatim to `Λ(1/2+iz)` for any
self-dual Selberg-class L-function (demonstrated for `L(s, χ_4)` in §6).

**Lemma 1 (velocity identity).** At any simple real zero `γ_j` of `Ξ`,

> `V_j := Ξ''(γ_j)/Ξ'(γ_j) = Σ_{ρ ≠ γ_j} 2/(γ_j − ρ)`,

the sum over all zeros (both signs, hidden ones included), absolutely convergent after the
symmetric pairing `ρ ↔ −ρ`.

*Proof.* Partial fractions: near a simple zero, `Ξ'/Ξ = (z−γ_j)^{−1} + Σ_{ρ≠γ_j}(γ_j−ρ)^{−1} +
O(z−γ_j)`, while the Taylor expansion of `Ξ'/Ξ` at `γ_j` has constant term `Ξ''(γ_j)/(2Ξ'(γ_j))`. ∎

`V_j` is also the instantaneous velocity of `γ_j` under the backward heat (De Bruijn–Newman) flow,
and equals the 2-D Coulomb field of the full zero gas evaluated at `γ_j`. The left side is
computable to arbitrary precision from `ζ` alone; the right side sees every zero, wherever it is.
That asymmetry is the detector.

**Lemma 2 (multipole sign discriminant).** Let a configuration of two zeros with real part sum
`2τ` be hidden near `τ`, and let `x` be real with `d = x − τ`, `|d|` large compared to the
configuration size. Its contribution to the field at `x` is

- off-axis quadruple `±(τ ± iσ)`:  `4d/(d² + σ²) = 4/d − 4σ²/d³ + O(d^{−5})`,
- on-axis pair `±(τ ± a)`:   `2/(d−a) + 2/(d+a) = 4/d + 4a²/d³ + O(d^{−5})`

(plus the mirror terms in `x + τ`, smooth and common to both). The monopole is common; the first
distinguishing term is the quadrupole, and **its sign records whether the hidden displacement is
perpendicular or parallel to the axis**. ∎ (Two lines of Taylor expansion.)

Electrostatic reading: hidden charge is an inverse-source problem for the log-potential measured
on the axis, and the perpendicular second moment enters the axial field with a negative sign.

## 2. The detector

Data: real zeros `γ_1 < … < γ_K` (the visible list), and measured `V_j` at selected `j`. Statistic:

> `R_j = V_j − Σ_{k ≤ K, k≠j} 2/(γ_j−γ_k) − Σ_{k ≤ K} 2/(γ_j+γ_k) − T_j`,

`T_j` the certified tail (§3). Under completeness of the visible list, `R_j` lies in a certified
band `±ε_j`. A hidden configuration adds its Lemma-2 field to every `R_j`. The pipeline:

1. **Existence.** Any `|R_j| > ε_j` certifies a defect (hidden zeros or a missed real zero).
2. **Localisation.** The monopole `4m/(x−τ)` across several `R_j` gives the count `2m` and centre τ
   (cross-checked against Turing/argument-principle counting, which supplies `m` independently).
3. **Characterisation.** Nonlinear fit of the exact off-axis model vs the exact on-axis model
   (mirror terms included); the better model and its parameter give `(τ, σ)` or `(τ, a)`.
   On noiseless synthetic data both recover their parameter to machine precision with model
   separation `~10^{12}` (§5); the certified version compares fit residuals against `ε_j`.
4. **Margin.** The detected configuration plus the local visible zeros feed the Calogero–Moser
   pencil `X + tY`; its real-spectrum threshold is the local De Bruijn–Newman margin, i.e. the
   interaction-corrected version of `σ²/2` (cf. Csordas–Smith–Varga's Lehmer-pair machinery, of
   which this is the off-axis dual).

## 3. Certification of the tail

With `N(u) = θ(u)/π + 1 + S(u)` exactly (`θ` the Riemann–Siegel theta, `S = π^{−1} arg ζ`), and
`f(u) = 4γ_j/(γ_j² − u²)` (negative, increasing on `(U, ∞)` for `U > γ_j`),

> `T_j = ∫_U^∞ f(u) θ'(u)/π du − f(U)·S(U) − ∫_U^∞ f'(u) S(u) du`,

where `U` is any point separating `γ_K` from `γ_{K+1}`. The first term is a numerical integral of
explicit smooth functions; the second is **exactly computable** because `S(U) = K − θ(U)/π − 1` at
a truncation point known to separate the zeros; the third is bounded rigorously by
`ε_j = ∫_U^∞ f'(u)·B(u) du` with Trudgian's unconditional bound `|S(u)| ≤ 0.111 log u +
0.275 log log u + 2.450` (`u ≥ e`, arXiv:1208.5846). A second integration by parts through
explicit `S_1` bounds would tighten `ε_j` further; it has not been needed.

**Measured performance (K = 1000, U ≈ 1419.92, S(U) = +0.153426):**

| `γ_j` | observed `R_j` | certified `ε_j` | headroom |
|---|---|---|---|
| 103.73 | `−6.3e−08` | `8.0e−04` | `10^{4.1}` |
| 146.00 | `−9.0e−08` | `1.1e−03` | `10^{4.1}` |
| 202.49 | `−1.3e−07` | `1.6e−03` | `10^{4.1}` |
| 321.16 | `−2.2e−07` | `2.6e−03` | `10^{4.1}` |
| 544.32 | `−4.5e−07` | `4.9e−03` | `10^{4.0}` |

The exact-`S(U)` boundary term is what removed the `~4e−4` systematic of the naive
smooth-density tail; the observed residual is now dominated by the 25-digit storage of the zero
list, four orders below the certified band.

**Certified thresholds** (at `γ ≈ 146`, `ε = 1.1e−03`): a hidden quadruple's *existence* signal
`4/d` exceeds `2ε` out to `d ≈ 1.7·10³` — i.e. any hidden zero anywhere near the data window is
certifiably visible; *sign-discrimination* (off- vs on-axis) requires `4σ²/d³ > 2ε`:
`σ_min ≈ 0.024` at `d = 1`, `0.067` at `d = 2`, `0.27` at `d = 5`. For calibration, the Polymath15
bound `Λ ≤ 0.2` confines any off-axis zero to `σ ≲ 0.66`: the entire allowed range is inside the
certified sensitive band at `d ≤ 5`.

## 4. What it adds over existing verification technology

Turing's method (and its modern implementations, Booker, Platt, Platt–Trudgian) certifies
*completeness by counting*: an argument-principle count against zeros found on the line. It reports
a discrepancy only as "a zero is missing below T", with no location, no `σ`, and no margin. The
velocity-residual detector is complementary and strictly finer-grained: it localises (`τ`),
characterises (`σ` vs `a`, by a sign), and quantifies (local Λ margin through the pencil). Its
inputs are two derivative values of the completed function per measured zero — available wherever
zeros are computed. It does not replace Turing's method (which supplies the integer count `m`
cheaply); it upgrades a count discrepancy into a diagnosis.

Related machinery: Csordas–Smith–Varga (Constr. Approx. 10, 1994) turn unusually close *real*
pairs (Lehmer pairs) into lower bounds on Λ; Lemma 2 + the pencil is the off-axis counterpart.
The velocity `V_j` itself is classical (it is the DBN flow velocity, Rodgers–Tao Thm 11); the
detector's content is the certified residual decomposition and the sign discriminant.

## 5. Synthetic validation (from Round 3)

80 true ordinates; zeros #45–46 replaced by hidden configurations at their midpoint; detector sees
only the remaining real zeros. Exact-model comparison: hidden `σ = 0.8` and `σ = 0.2` quadruples
recovered exactly (rms `2e−16`, model separation `≥ 10^{12}`); hidden real pairs `a = 0.3, 0.9`
recovered exactly and correctly classified; empty case identically zero. Near-field shape matches
the Lorentzian-dipole prediction to all digits. Scripts `d1_synthetic.py`, `d2_modelfit.py`.

## 6. Portability: Dirichlet beta

`Λ_β(s) = (π/4)^{−(s+1)/2} Γ((s+1)/2) L(s, χ_4)`, `Ξ_β(z) = Λ_β(1/2+iz)`: even, real, first zeros
`6.0209, 10.2438, 12.9881, …` (recomputed). With 70 zeros found by sign-scanning and the density
`dN = (2π)^{−1} log(2u/π) du`, the null test gives residuals `+4.4e−4, +7.9e−4, +1.2e−3` at
`γ_{11}, γ_{21}, γ_{31}` — the same quality as the zeta test at comparable visible-list length,
with the (uncertified, smooth-density) tail. Certification for Dirichlet L-functions needs the
analogue of the exact `θ/π + 1 + S` decomposition and an explicit `|S(u, χ)|` bound
(available in the literature); nothing else changes. Script `h4_beta.py`.

## 7. Limitations and the honest statement

- The certificate is modulo floating point: `V_j`, the theta integrals, and `ε_j` are computed in
  high-precision arithmetic, not interval arithmetic. An ARB port is mechanical.
- The method certifies and diagnoses; it does not prove. If RH is true the detector will only ever
  output null results; its value is verification infrastructure (especially for L-functions where
  verified heights are low), plus the geometric dictionary it operationalises: zeros as a 2-D
  Coulomb gas whose on-axis field is exactly measurable, hidden charge as a solvable
  inverse-source problem, margins as pencil spectra on Calogero–Moser space.
- Detection *radius* vs *density*: the certified existence radius (~10³ at K = 1000) far exceeds
  the window where sign-discrimination is certified (d ≲ 5–10); in practice one measures `V_j` at
  several zeros bracketing the suspect region, which is exactly the regime where discrimination is
  strongest.

## 8. Reproduction

`h3_certified.py` (certified zeta null test, thresholds), `d1_synthetic.py`/`d2_modelfit.py`
(injection tests), `d3_nulltest.py` (Round-3 baseline), `d4_margin_meter.py` (pencil margins),
`h4_beta.py` (Dirichlet beta), zero caches `zeros80.json`, `zeros301.json`, `zeros1001.json`,
`beta_zeros.json`. Dependencies: `numpy`, `scipy`, `mpmath`.
