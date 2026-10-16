# The near-BPS corner of the generalized cusp, the rounded flipped loop, and the closure audit

24 September 2026. Prepared for Edward Baker.

**Model:** Claude Opus 5.5 (Anthropic), model identifier `claude-opus-5-5` as reported by the runtime. The session configuration names `claude-fable-5-1`, and the serving model can differ.  
**Reasoning effort:** not exposed; not inferred.  
**Status:** this note carries out tasks 1–3 of the [continuation note](CONTINUATION_AFTER_FIRST_SESSION_20260924.md).

- **Checks.** Two standard-library programs, [`check_near_bps_corner.py`](../numerics/check_near_bps_corner.py) (56 cases) and [`check_rounded_and_closure.py`](../numerics/check_rounded_and_closure.py) (20 cases), with records. All cases pass.
- **Referee.** A separate referee context of the same model re-derived items 1–8 of Section 8 with its own code. It confirmed them, including an independent value of the rounding constant h, and flagged corrections, which are applied here.
- **Review.** There has been no independent specialist review.
- **Arithmetic.** No arithmetic claim is made.

**Repository baseline:** `8b22141`; uncommitted.

## 0. Summary

**1. The corner coefficient H.** H(λ,N) is the coefficient of the continuum |s| log term of the flipped loop. It is governed by the corner of the generalized cusp: φ = π − u, θ = π − xu, u → 0. There, the effective coupling is g = λu.

- *Exact slope.* The CHMS near-BPS formula fixes, at all couplings, the part of Γ linear in (cos θ − cos φ). In the corner this gives the exact slope at the BPS line, where the corner value is −2(1 − x)(π²/2)B(2λu/π).
- *Two loops.* Through two loops (Drukker–Forini, checked against three independent limits) the whole corner function is (1 − x²)[g/(16π) − g²/(192π²)] + O(gu, g²u log u). Hence H := lim Γ(π − u, π)/u = λ(1 − 1/N²)/(16π) has no two-loop correction.
- *All orders.* Order by order in perturbation theory H stays at its one-loop value, provided a standard multi-angle bound on antiparallel-lines singularities holds (Section 1.4).
- *Strong coupling.* In the planar classical string, the corner at g ≫ 1 is Γ = √(λu)F(x). F is given in closed parametric form and F(0) = 1/(√(2π)3^{3/4}) ≈ 0.1750. F reproduces the exact BPS-line slope, F′(1) = −¼√(2/π), which is a nontrivial check. It is not proportional to 1 − x², so the two-loop form does not persist at strong coupling.
- *Consequence for the flipped loop.* The per-cusp coefficient is Φ(λ|s|/3). It is one-loop exact as s → 0 at fixed λ, but it crosses over to ≈ 0.1750√(λ|s|/3) when 1/λ ≪ |s| ≪ 1 (planar). In the conformal theory, Loewner time therefore sets the effective coupling of the near-BPS corner: g(t) = λ|a|√t/3.

**2. The rounded family is finite.** Replace each cusp by a circular fillet of radius δ, and let the internal vector turn in step with the tangent. At one loop:
\[
\log W^{(1)}=-B_1\Big[A(s)\log\tfrac1{\hat\delta}+\tfrac{2\pi|s|}{3}\big(\log\tfrac{|s|}{3}-2\big)-h|s|\Big]+O(s^2),\qquad h=-4.0202,
\]
where δ̂ = δ/√t. The coefficient of log(1/δ̂) is the exact one-loop cusp sum A(s), and the formula is valid for δ̂ ≪ |s|. The |s| log|s| term comes from the fillet touching the legs at distance δ/tan(α/2) ≈ 6δ/|s| from the vertex. Every separation-based regulator (flow, point splitting, fillets) shares this mechanism. The constant h depends on the rounding convention.

**3. The Schwinger–Dyson audit does not close the flipped hierarchy.** At a finite regulator, the field equations reduce only three pieces of the second-equation insertions: the curvature-current part (q̇¹E₂ − q̇²E₁), the scalar Laplacian, and the radial derivatives. They leave these residual terms:

- transverse gauge currents;
- the transverse scalar Laplacian (D₃² + D₄²)Φ;
- scalar and fermion currents, and scalar-potential and Yukawa insertions;
- scalar commutators from transport along the chord;
- the tip gradient;
- ordered pairs.

At one loop, the field-equation part of a derivative moment is a pure regulator contact term, while the transverse part has a long-range 4/r⁴ kernel. So the residual cannot be dropped, even perturbatively.

## 1. The near-antiparallel, near-BPS corner of the generalized cusp

### 1.1 Why the corner controls the flipped loop

In the continuum, the flipped loop has two cusps with deflection φ_c = π − α_c and internal angle π, where α_c ≈ |s|/3 (first note, T3). Its log W carries −Σ_c Γ(π − α_c, π) log(ℓμ). The one-loop value Γ⁽¹⁾ = λ(1 − 1/N²)α/(16π) gave the coefficient 2πB₁|s|/3 used in the flipped-return note. The open question was whether higher orders change it.

### 1.2 Exact input: the part linear in cos θ − cos φ

At every loop order, Γ is a polynomial in cos θ that vanishes on the BPS line cos θ = cos φ. Hence Γ = Σ_{k≥1}(cos θ − cos φ)^k R_k(φ; λ, N).

The CHMS near-BPS formula (their eq. 8, derived from the latitude matrix model at finite N) is Γ ≈ −(φ² − θ²)B(λ̃)/(1 − φ²/π²), with λ̃ = λ(1 − φ²/π²). It determines ∂Γ/∂θ at θ = φ, and therefore R₁ exactly:
\[
R_1(\phi)=-\frac{2\phi\,B(\tilde\lambda)}{(1-\phi^2/\pi^2)\sin\phi}.
\]

In corner variables, cos θ − cos φ ≈ −(1 − x²)u²/2, sin φ ≈ u and λ̃ ≈ 2λu/π. The k = 1 part is therefore
\[
\Gamma_1=(1-x^2)\,\frac{\pi^2}{2}\,B\!\Big(\frac{2\lambda u}{\pi}\Big)\,(1+O(u)).
\]
The terms with k ≥ 2 vanish to second order at x = 1. This gives the first exact statement: in the corner, the slope at the BPS line is −∂Γ/∂x|_{x=1} = π²B(2λu/π). It is a function of the single effective coupling g = λu.

### 1.3 Two loops

The planar two-loop cusp is taken from Drukker–Forini (arXiv:1105.5144, eqs. 3.1–3.2), transcribed through a fetch summary. Here
- V^{(2)} = V_lad + V_int;
- V_int = −(2/3)(π² − φ²)V^{(1)};
- V_lad = −4(cos θ − cos φ)²/sin²φ · 𝔅(φ);
- 𝔅(φ) = Cl₃(2φ) − ζ(3) + φ Cl₂(2φ). The imaginary part cancels identically, as the referee checked.

The transcription passes three independent limits (W1–W3):
- At small angles, V^{(2)} → (2π²/3)(φ² − θ²), matching the planar B = λ/16π² − λ²/384π².
- The slope at the BPS line equals the CHMS value −(4/3)(π² − φ²)φ at every φ tested.
- In the antiparallel limit, the two-loop logarithm has the known coefficient λ²/(8π³).

In the corner, with 𝔅(π − u) = 2πu(log 2u − 1) − u² + …,
\[
\Gamma(\pi-u,\pi-xu)=(1-x^2)\Big[\frac{g}{16\pi}-\frac{g^2}{192\pi^2}\Big]+O(gu)+O(g^2u\log u).
\]
The O(gu) term is the one-loop correction −(1 − x²)λu²/(16π²). Through O(g²) this equals (1 − x²)(π²/2)B(2g/π) (W4, W5). At finite N the two-loop cusp is pure C_F C_A, as the referee noted, so the absence of a two-loop term in H also holds at finite N.

### 1.4 H to all orders in perturbation theory

At θ = π we have ξ := (cos θ − cos φ)/sin φ ≈ −u/2. Write Γ^{(L)} = Σ_k ξ^k c_k^{(L)}(φ).

- **The k = 1 term** is exact and contributes O(λ^L u^L).
- **The k ≥ 2 terms** are o(u) at θ = π provided c_k^{(L)}(π − u) = O(u^{k−1}·polylog u). That bound follows from the antiparallel bound Γ^{(L)}(π − u, θ_j) = O(u^{−1} polylog u) imposed at L − 1 distinct fixed θ_j: there ξ ≈ (1 + cos θ_j)/u, and inverting the Vandermonde matrix gives the bound on each c_k. The argument only needs those singularities to be o(u^{−3}).
- **The bound's status.** It holds at one and two loops and in the ladder limit. For general L it is a well-motivated assumption, not a theorem.

**Result.** Under that assumption, H(λ,N) = lim_{u→0}Γ(π − u, π)/u = λ(1 − 1/N²)/(16π) to all orders in perturbation theory. The statement is order by order. Carrying it beyond perturbation theory would need a corner function Φ(g,x) that is differentiable at g = 0, and that has not been shown.

### 1.5 Strong coupling: the classical corner

The planar classical string uses the ansatz z = r ζ(φ̂) with an S⁵ angle ϑ(φ̂). The two conserved charges give the opening angle Ω = π − φ, the internal angle θ, and Γ/√λ as one-dimensional integrals over the parameters (ζ₀, r₁). These integrals were checked analytically by the referee:
\[
\Omega=2\zeta_0\!\int_0^{\pi/2}\!\!\frac{\sin^2t\,dt}{\sqrt{1+\zeta_0^2\sin^2t}\sqrt{\sin^2t+r_1}},\quad
\theta=2\sqrt{r_1-1+\zeta_0^2r_1}\!\int_0^{\pi/2}\!\!\frac{dt}{\sqrt{1+\zeta_0^2\sin^2t}\sqrt{\sin^2t+r_1}},
\]
\[
\frac{\Gamma}{\sqrt\lambda}=\frac1{\pi\zeta_0}\Big[\int_0^{\pi/2}\frac{h(t)-\cos t}{\sin^2t}dt-1\Big],\qquad h=\frac{\sqrt{r_1}\sqrt{1+\zeta_0^2\sin^2t}}{\sqrt{\sin^2t+r_1}}.
\]

**Controls (S1–S4).**
- The antiparallel limit gives ΓΩ → −4π²/Γ(¼)⁴ (Maldacena).
- The small-angle limit gives Γ → −φ²/(4π²), i.e. B = √λ/4π².
- On the curve r₁ = 1/ζ₀² one finds θ = π/√(1 + ζ₀²) = π − Ω and Γ ≡ 0: this curve is the BPS line.
- The slope at the BPS line matches CHMS at strong coupling, φ/(2π²√(1 − φ²/π²)), at five values of φ to ≤ 2×10⁻⁶.

**Corner expansion.** In the corner the string does not stay thin. Its depth is ζ₀ ~ √Ω, much larger than the opening Ω: the string reaches far into AdS. With ζ₀ = √(wΩ) and 1/√r₁ = (2/π)√(Ω/w), the leading order in Ω gives the parametric form
\[
x=\frac{3}{\pi w}-\frac{\pi w}{4},\qquad \Gamma=\sqrt{\lambda\Omega}\,F,\qquad F=\frac14\Big(\sqrt w-\frac{4}{\pi^2w^{3/2}}\Big).
\]

**Checks of the parametric form** (S5, S6):
- It vanishes at x = 1 (w = 2/π), the BPS point.
- F(0) = 1/(√(2π)3^{3/4}) = 0.17501 at w = 2√3/π.
- F′(1) = −¼√(2/π). This equals −π²B(2g/π) at large g, i.e. the exact slope of Section 1.2 evaluated at strong coupling. The classical corner thus reproduces the one exactly known coefficient.
- The exact integrals approach the parametric form with O(Ω) corrections, checked at Ω = 10⁻³ and 10⁻⁴.

**Features of F.**
- F is not proportional to 1 − x². The k = 1 part alone would give F(0) = √(2/π)/8 ≈ 0.0997, so the k ≥ 2 terms are O(1) at large g.
- The parametrization is not even in x. The physical branch is F(|x|), which has a kink at θ = π with F′(0) = −0.1516. This is classical: antipodal points of S⁵ are joined by an S⁴ of great circles, so the string has zero modes there, and quantum effects should smooth the kink.
- A byproduct (S7): as x → ∞ the corner matches the antiparallel lines near θ = π. At strong coupling V_∥(θ) ≈ −√λ(π − θ)^{3/2}/(3^{3/2}√π L), whereas weak coupling gives ∝ (π − θ)². The strong-coupling law is non-analytic in cos θ, a λ → ∞-first effect. I did not find this law in the literature during this session.

**Scope.** The strong-coupling result is valid for 2λΩ/π ≫ 1 with Ω ≪ 1. It says nothing about H, which is the g → 0 slope.

### 1.6 What this means for the flipped loop

Per cusp, Γ_c = Φ(λα_c, x = 0), with α_c ≈ |s|/3, and:

- For λ|s| ≪ 1 at any λ, Φ ≈ g/(16π)(1 − 1/N²). The continuum law log W ≈ −(λ(1 − 1/N²)|s|/(24π))log(ℓμ) is one-loop exact in this regime (perturbatively, under the assumption of 1.4).
- For 1/λ ≪ |s| ≪ 1 (planar, strong coupling), Φ ≈ 0.1750√g, so log W ≈ −0.2021√(λ|s|) log(ℓμ).
- Since s = a√t, the Loewner time moves the corner through its effective coupling. In a strongly coupled theory, the continuum short-time law of the flipped loop changes from |s| log to √|s| log as t grows past ~9/(λa)², where g ≈ 1.
- The crossover function between the two regimes is not determined beyond O(g²). A two-loop calculation at x = 0 beyond the corner scaling, or the quantum string, would be needed.

## 2. The rounded flipped loop

**Construction.** Replace each cusp by the circular fillet of radius δ tangent to both legs; the fillet solves a two-variable tangency problem on the exact trace (R1). On each fillet, n = cos χ n₀ + sin χ m, with χ advancing by π across the fillet in proportion to the turning angle π − α_c. The loop is C¹ with smooth n, so its one-loop integral is finite.

**Controls.**
- A Zarembo "stadium" (antiparallel legs, semicircular ends, n rotating with the tangent) has an identically vanishing integrand. The numerics give 4×10⁻¹⁴, but that only checks the orientation and χ conventions.
- A constant-scalar stadium tests the kernel normalization against the antiparallel-lines law, converging slowly to 1 (0.984, 0.988).

**Result (R2, R3).** With δ taken as fixed fractions of s:

- The coefficient of log(1/δ) is the exact one-loop cusp sum A(s) = Σ 2(π − α_c)tan(α_c/2) = (2π/3)s − (2/9)s² + …. Successive differences halve.
- The finite part is
\[
R(s)=\lim_{\delta\to0}[I+A(s)\log(1/\delta)]=-\frac{2\pi s}{3}\Big(\log\frac s3-2\Big)+h\,s+O(s^2),\qquad h=-4.0202,
\]
constant in s to 10⁻⁴ over s = 0.1, 0.05 and 0.025. The referee's independent implementation gives h = −4.02025 at s = 0.1.

**Interpretation.** A fillet of radius δ at a cusp of opening α touches the legs at distance δ/tan(α/2) ≈ 2δ/α from the vertex. The near-BPS interaction accumulates πα per e-fold only where the sliver is wider than about δ. The effective cutoff is therefore ∝ δ/α, which produces −A log s.

- **Convention dependence.** Any cutoff proportional to δ/α gives the same |s| log|s| and a different h. The "sliver prediction" fixes only the s log s term. The O(s) constant is set by the hairpin ends and depends on convention: h nearly cancels the vertex-excision constant 4π/3, leaving R ≈ −(2πs/3)log(s/3) + 0.17 s.
- **Regime of validity.** The formula requires δ̂ ≪ |s|. If instead the rounding scales with the sliver, δ̂ = κ|s|, then log W is linear in |s| with a κ-dependent coefficient. As with the flow regimes, the scheme freedom at O(s) is the freedom in how the regulator scales with s. The scheme-independent content is A(s), whose coupling dependence is the H(λ) of Section 1.

## 3. Schwinger–Dyson audit of the flipped hierarchy

Take the bosonic action (1/g²)∫tr[½F² + (DΦ_I)² − ½[Φ_I,Φ_J]²] plus fermions, in the conventions of the first note. Its field equations are
\[
E_\nu\equiv D_\mu F_{\mu\nu}=-i[\Phi_I,D_\nu\Phi_I]+J^\psi_\nu,\qquad D_\mu D_\mu\Phi_I=[\Phi_J,[\Phi_J,\Phi_I]]+Y_I .
\]
At a finite regulator with an integration-by-parts identity, ⟨δ𝒪/δA^a_ν(x)⟩ = ⟨𝒪 δS/δA^a_ν(x)⟩. Here δS/δA_ν ∝ tr T^a(E_ν + i[Φ_I, D_νΦ_I] − J^ψ_ν), and similarly for the scalars. A chord insertion satisfies tr(X̂(r)Q) = X^a(rq) tr(T^a𝒬_r), where 𝒬_r is the holonomy based at rq. The field-equation combination inserted on the loop therefore equals a self-contact term δ⁴_reg(0)·C_F plus splitting terms wherever the loop passes through the point again, which never happens for this simple loop. That contact term is regulator dependent. At positive flow time, the flowed E is not δS/δA, and the flow-response kernel appears, as in the parent Section 7.2.

**Decomposing the single insertions of the second equation** (flipped note, Proposition 3):

1. **Gauge.** q̇·DF₁₂ = (q̇¹E₂ − q̇²E₁) + X_⊥, with X_⊥ = −q̇¹(D₃F₃₂ + D₄F₄₂) + q̇²(D₃F₃₁ + D₄F₄₁) (parent eq. 22). The first part reduces to the scalar current −i[Φ_I, D_νΦ_I] (all six scalars), the fermion current and a contact term. X_⊥ is irreducible.
2. **Scalar, radial part.** q̇^μn̂^νD_μD_νΦ = ρ̇ q̂·D(n̂·DΦ) + (k/|q|)n̂^μn̂^νD_μD_νΦ. The radial term integrates by parts through the transported derivative ∂_rX̂ = (q·DX)^ − |q|[Φ̂, X̂]. The commutator is present because the chord connection contains Φ (C1: FD check to 5×10⁻⁸; dropping the commutator gives an O(1) error). This yields a tip insertion (n̂·DΦ)^(1), the first moment 𝒢, and a commutator term.
3. **Scalar, normal part.** n̂n̂DDΦ = D²Φ − q̂q̂DDΦ − (D₃² + D₄²)Φ. D²Φ reduces to the scalar potential, the Yukawa term and a contact term. q̂q̂DDΦ is radial. The transverse Laplacian is irreducible. A harmonic four-dimensional field such as Φ = c(x₁² − x₃²)T³ satisfies every field equation yet has a planar Laplacian of 2c (C1), so the transverse term cannot be deleted.
4. **Tip gradient.** γ(q̇·DΦ)^(1) is irreducible, and in the continuum it is an insertion at a cusp.
5. **Rotation of n̂.** The term −(k/|q|²)∫r(q̂·DΦ)^ = −(k/|q|³)(Φ̂(1) − ∫Φ̂) is reducible.
6. **Ordered pairs** are new correlators.

**One loop.** At O(g²), with the free flowed propagator, the insertion (q̇¹E₂ − q̇²E₁) contracts with the loop through □k_τ = −4π² × (heat kernel), a pure contact term (C1). X_⊥ contracts through −4k′_τ(r²), which tends to 4/r⁴ at r ≫ √τ (C1). The geometric factor q̇ × dy has a definite sign along the trace across the sliver. So the transverse residual has a nonzero long-range, sliver-enhanced contribution, while the field-equation part is regulator contact. Deleting the transverse terms is therefore invalid in the actual perturbative theory, not only on artificial classical backgrounds.

**Verdict.** The flipped hierarchy does not close at second order under the Schwinger–Dyson equations. Its residual inventory is the pure-YM one, plus these terms:

- scalar and fermion currents;
- the transverse scalar Laplacian;
- scalar-potential and Yukawa insertions;
- transported scalar commutators;
- the tip gradient.

## 4. Assessment

- **The corner question has a clean answer.** H is one-loop exact as s → 0 at fixed λ, perturbatively and under a standard assumption. The approach is controlled by the effective coupling λ|s|, and at strong coupling there is a √(λ|s|) window with an explicit classical coefficient. The strong-coupling corner reproduces the exactly known BPS-line slope, which is a nontrivial internal consistency check.
- **Loewner time as effective coupling.** The observation that in the CFT Loewner time acts as the effective coupling of the corner, g(t) = λ|a|√t/3, is the most interesting physical by-product of the growing-trace analysis so far.
- **Arithmetic assessment unchanged.** Nothing here is causal or resembles the shifted-zeta transfer.
- **Rounding.** The rounded family gives a finite W(s, δ̂) whose universal content is again A(s).
- **Closure audit.** It confirms that the flipped hierarchy is an honest infinite hierarchy with a specific residual inventory. It is not a disguised closed system.

**Direction.** The physical M3/M4 programme for the flipped family is now in a well-understood state, and its remaining open item is the crossover function Φ(g, 0). The link to the Weil form has not strengthened: the growing-trace observables are Euclidean expectation values on a shape family, with no input/output structure. If the arithmetic goal remains primary, the next substantive step is conceptual rather than computational: identify a physical input/output channel with memory. The candidates are quartic displacement response, or a defect with its own dynamics, such as the finite-mass string endpoint. Otherwise the flipped-family results can stand as a self-contained physics contribution.

## 5. Next steps

1. **Φ(g, 0) beyond two loops.** Extract the three-loop corner from the known three-loop generalized cusp (CHMS arXiv:1203.1019; verify the citation), and test whether (1 − x²) survives at O(g³).
2. **One-loop quantum correction to the classical corner.** This would show how the S⁴ zero modes smooth the kink.
3. **A physical channel with memory.** For example, a finite-mass displacement response (string endpoint at z_m), or the quartic straight-line response. This is the prerequisite for any arithmetic comparison.
4. **Housekeeping.** Commit and refresh the package record; there is a stale `.git/index.lock` (Section 7).

## 6. Statement ledger

| Statement | Status |
|---|---|
| Exact k = 1 part and corner slope at the BPS line | Proof, given CHMS eq. 8 (literature) |
| Two-loop corner form and H with no two-loop term | Proof from the DF formulas, which are validated by three limits |
| H one-loop exact to all orders | Order-by-order argument under the multi-angle antiparallel bound (assumption) |
| Classical corner F(x), F(0), F′(1) | Derived analytically (leading order in Ω) and checked numerically; valid for λΩ ≫ 1 |
| Strong-coupling V_∥ ∝ (π − θ)^{3/2} | Derived; not located in the literature |
| Rounded one-loop A(s) coefficient | Numerical verification of an analytic expectation |
| h = −4.0202 | Labelled numerical constant (convention dependent) |
| Schwinger–Dyson residual inventory | Structural reading with explicit controls |

## 7. Records, review and repository state

Run from `papers/susy-positivity/investigations/wilson-loewner/`:

```sh
python3 N4SYM/numerics/check_near_bps_corner.py --output /tmp/n4sym-nb.json
python3 N4SYM/numerics/check_rounded_and_closure.py --output /tmp/n4sym-rc.json
```

Both use the standard library only and are deterministic. The second imports `check_trace_completion.py` and `check_flipped_return.py`. Records are in `N4SYM/numerics/records/`.

The referee report (same model, separate context) confirmed:
- the Clausen form of the bracket;
- all three limits of the DF transcription;
- the corner form, with the remainder corrected here to include the one-loop O(gu) term;
- the logic of 1.4, with its assumptions now stated;
- the string integrals, the BPS curve, the CHMS slope and the corner function F, all by independent expansion;
- the v^{3/2} law;
- the rounded-loop value of h, by an independent implementation.

The referee's wording corrections are applied: the Zarembo control is a conventions check, the strong-coupling scope is λΩ ≫ 1, the two-loop corner form holds only at two loops, and the H result is order by order.

The zero-byte `.git/index.lock` left by a `git status` in the previous session may still be present. Remove it before committing.

Prepared for Edward Baker with substantial LLM assistance (Claude Opus 5.5, Anthropic) in derivation, programming and drafting. Independent specialist review is outstanding.
