# Straight-line response, energy accounting and the choice of trace completion in N=4 SYM

23 September 2026. Prepared for Edward Baker.

**Model:** Claude Opus 5.5 (Anthropic), model identifier `claude-opus-5-5` as reported by the runtime. The session configuration names `claude-fable-5-1`, and the serving model can differ.  
**Reasoning effort:** not exposed; not inferred.  
**Status:** first working session of the [N4SYM proposal](N4SYM_DISPLACEMENT_LOEWNER_RESEARCH_PROPOSAL_20260923.md), covering its Section 12 and part of work package D. Every statement is classified in Section 7. Two standard-library check programs (72 and 77 cases, all passing) are recorded in `../numerics/`. The same assistant audited this note ([review](../reviews/review_claude_first_session_20260923.md)); there has been no independent specialist review. No arithmetic realization is claimed, and no zeta value is computed anywhere.  
**Repository baseline:** `8b22141` (the commit that added the proposal). This note and its programs are uncommitted working-tree additions.

## 0. Results in brief

1. **The quadratic shape response of the straight line is fixed by B, apart from one scheme constant.** For the proposal's deformation family (2), and for every λ and N,
\[
\log Z[\epsilon h,\epsilon j]=\epsilon^2\Big\{\pi B\!\int\!\frac{dk}{2\pi}\big(|k|^3|\hat h(k)|^2-|k|\,|\hat\jmath(k)|^2\big)+c_R\!\int\!|\dot h|^2d\sigma\Big\}+O(\epsilon^4).
\]
The perimeter constant c_R is the only freedom left, and it vanishes in the natural Maldacena–Wilson scheme. There is no cubic term. With c_R = 0, the quadratic form is positive in the transverse direction (the Ḣ^{3/2} seminorm), negative in the internal direction (Ḣ^{1/2}), and exactly zero on the Zarembo profile j = ḣ; that zero is equivalent to the supersymmetry relation C_D = 6C_Φ. A scheme with c_R < 0, which is what a positive renormalized mass means, makes the transverse form negative at small k.
2. **The linear retarded response of the straight line is local.** Its susceptibility is the polynomial χ_R(ω) = m_R ω² + 2πiBω³, i.e. Abraham–Lorentz radiation reaction ⟨D⟩ = −m_R ḧ + 2πB h⃛. The reason is general to conformal line defects in any dimension: one-dimensional conformal symmetry fixes the two-point function, and because the displacement has integer dimension 2 its commutator is a pure contact term. The internal tilt channel is an exact resistor.
3. **The energy account works in total but not at finite time.** The total work of a compactly supported drive is 2πB‖ḧ‖², which reproduces the Correa–Henn–Maldacena–Sever radiated energy coefficient exactly. Over finite times, however, the renormalized account contains the indefinite Schott term −2πB ḣḧ. For any finite renormalized mass it is negative immediately after the onset of every drive with a finite-order onset and of the standard flat onsets e^{−1/x^α}. It is not negative for every C^∞ drive: oscillating onsets give counterexamples. Finite-time passivity survives only in the positive cutoff control, and only because of its divergent inertia δm_Λ = 4BΛ.
4. **Consequence for the arithmetic target.** Linear response about the straight line has no memory, a fixed exponent and no delays. It cannot realize the shifted-zeta transfer. This decides work package F negatively for that channel, and the result holds for every conformal line defect.
5. **In a conformal theory the Loewner time is not an independent clock.** For the linear driver u = at, the trace at time t is √t times the trace at time 1 with slope s = a√t. Renormalized loops therefore depend on t only through s (together with cusp anomalous scalings and the ratio of the rounding scale to √t). Short time and small driver are the same limit.
6. **The proposal's first growing-contour observable is dominated by a thin-sliver interaction.** That observable is the trace plus its straight return chord, with a constant scalar direction. As s → 0 it becomes a thin sliver dominated by the attraction between the trace and its own return chord. At one loop log W ≈ (3λ(1−1/N²)/(2π s))·log(1/ε̂), which diverges. The a = 0 member is infinite, not a control. The tangent-coupled alternative is trivial, since ⟨W⟩ = 1 for Zarembo loops.
7. **A workable replacement: flip the scalar on the return chord.** With n = −n₀ on the chord, the a = 0 identity control is restored. The exact first evolution equation is derived (Section 4.4) and checked by finite differences. The small-s limit is regular in both regimes: 1 + O(a²t³) at fixed flow resolution, and 1 − O(|s| log) at one loop in the continuum.

## 1. Conventions fixed (milestone M0, for the straight line)

The theory is SU(N) N=4 SYM, N ≥ 2, θ = 0, with Euclidean action (1/g²)∫tr(½F_{μν}F_{μν} + D_μΦ_I D_μΦ_I + …). Fields are Hermitian, tr T^aT^b = δ^{ab}/2, F_{μν} = ∂_μA_ν − ∂_νA_μ − i[A_μ,A_ν] and D_μ = ∂_μ − i[A_μ,·], as in the [parent variation section](../../sections/05_variation.tex). The Feynman-gauge propagators are g²δ^{ab}δ_{μν}/(4π²x²) for the gauge field and the same for each scalar. The line is W = N⁻¹ tr P exp∫(iA·ẋ + |ẋ| n·Φ), with larger parameters to the left.

The source sector is the infinite straight line x₀(σ) = (σ,0,0,0) with constant n₀. The relative functional is Z[h,j] = ⟨W[x_h,n_j]⟩/⟨W[x₀,n₀]⟩, and defect correlators ⟨⟨O₁…O_n⟩⟩ are path-ordered insertions divided by ⟨W⟩. Constant h is a translation and constant j an R-rotation, so both leave Z unchanged. These two symmetries are used below.

**First variation.** From the parent ordered-transport identity, with η = (0,h) and δn = j ⊥ n₀, the insertion is 𝔻_i h^i + Φ_a j^a with 𝔻_i = iF_{iσ} + D_iΦ_{n₀}. (The term Φ ẋ·η̇/v vanishes on the straight line.) This agrees with CHMS eq. (58) up to the sign of the F-term, which is tied to the orientation/ordering convention. Both one-point functions vanish, by conformal invariance and by SO(3)×SO(5).

**Adjoint.** The Euclidean displacement is Osterwalder–Schrader real: Θ𝔻(σ) = 𝔻(−σ), because F_{iσ} is odd under σ → −σ and complex conjugation flips the explicit i. Its positive two-point function is therefore the expected reflection-positivity statement. Wick rotation takes iF_{iσ} to F_{i0}, so the Lorentzian displacement F_{i0} + D_iΦ (electric plus scalar-gradient force) is Hermitian. The factor i is not a failure of Hermiticity, as the proposal anticipated. The tree-level check S1 confirms the sign: ⟨iF iF⟩ contributes +4 and ⟨∂Φ∂Φ⟩ contributes +2, in units of g²C_F/(4π²σ⁴). Hence C_D = 12B₁ with B₁ = λ(1−1/N²)/(16π²), and C_Φ = 2B₁.

**Inputs from the literature.** CHMS [P1] give C_D = 12B (eq. 55), C_Φ = 2B (eqs. 14, 20), Γ_cusp = −B(φ² − θ²) (eq. 25) with ⟨W⟩ ~ e^{−Γ log(L/ε)} (eq. 6), and ΔE = 2πB∫v̇² (eq. 5). They were checked in this session against the arXiv HTML full text, through an automated fetch-and-summarize tool, so the equation numbers should be confirmed by eye before any manuscript use.

## 2. Quadratic shape response (milestone M1 at second order)

**Proposition 1 (renormalized quadratic response).** Assume (a) the second variation of the renormalized log Z, restricted away from the diagonal, is given by the defect two-point functions; (b) its extension across the diagonal differs from any other by a finite-order local distribution whose coefficients carry powers of the regulator scale, apart from finite renormalization conditions (such as a finite value of c_R); (c) Z is invariant under translations, rotations, SO(5) and the reflection described below. Then the display in Section 0 holds. Equivalently,
\[
\log Z=\epsilon^2\Big\{\frac B2\iint\frac{|\dot h(\sigma)-\dot h(\sigma')|^2-|j(\sigma)-j(\sigma')|^2}{(\sigma-\sigma')^2}\,d\sigma\,d\sigma'+c_R\!\int\!|\dot h|^2\Big\}+O(\epsilon^4).
\]

*Proof.* The separated kernels are 12Bδ_{ij}σ⁻⁴, 2Bδ_{ab}σ⁻², and zero for the mixed pair: operators of different dimension have vanishing two-point functions on a conformal line, and SO(3)×SO(5) has no invariant tensor with one index of each kind.

For the extension across the diagonal, two extensions of an even kernel differ by Σc_n δ^{(2n)}. The family |σ|^λ has poles only at λ = −1, −3, …. So λ = −4 and λ = −2 are regular, the scale-covariant extensions are unique, and no logarithms occur. Their Fourier transforms follow by continuation of 2Γ(1−s)sin(πs/2)|k|^{s−1}: FT[|σ|⁻⁴] = (π/6)|k|³ and FT[|σ|⁻²] = −π|k|. Both vanish at k = 0, consistent with translation and internal-rotation invariance.

Dimensional analysis then limits the freedom. In the h-sector a δ term would carry Λ³ (excluded by translation invariance), a δ″ term carries mass dimension one (this is c_R, a cutoff-size coefficient in a positive regulator, a finite value after a renormalization condition), and δ^{(4)} and higher carry negative powers and vanish as the regulator is removed. In the j-sector the δ term carries Λ (excluded by R-invariance) and δ″ already vanishes, so the j-sector is completely universal. No mixed local term exists, for the same tensor reason as above.

Collecting coefficients: ½·12B·π/6 = πB and ½·2B·(−π) = −πB. The position-space form follows from ∬(g−g′)²/(σ−σ′)² = 2π∫|k||ĝ|²dk/2π.

Cubic terms need an SO(5) tensor of odd rank (there is none) or an SO(3) tensor ε_{ijk} with three displacements. The latter is excluded by the reflection x² → −x², combined with the reflection of one internal direction orthogonal to n₀. That combined reflection is a symmetry of the straight half-BPS line: it is inherited from a rotation of the ten-dimensional theory. Ordering signs in one-dimensional three-point functions do not evade this, because the reflection flips the overall sign. ∎ The quadratic part is proved under (a)–(c). The cubic vanishing is a proof sketch, because the ten-dimensional origin of the reflection is cited rather than rederived here.

**What is and is not fixed by the reference.** The perimeter term is c_R = −m_R/2, where m_R is the renormalized heavy-source mass of Section 3. It is not fixed by any symmetry. It is zero in any scheme in which the Maldacena–Wilson linear divergence cancels. The one-loop kernel realizes exactly that: its second variation equals the homogeneous finite-part extension, with no δ″ term (S3, and the integration-by-parts identity (|u|⁻²)″ = 6|u|⁻⁴ for the continued family). The second-order local insertions, from |ẋ| = 1 + ḣ²/2, from the normalization of n_j, and from the h h ∂∂ terms, contribute only through one-point functions of defect operators. Those are scheme constants and are absorbed in the δ and δ″ inventory above.

**Zarembo cancellation.** With a transverse direction identified with an internal direction orthogonal to n₀, the choice j = ḣ makes n_j exactly the unit tangent. The two terms of Proposition 1 then cancel, because |k|³|ĥ|² = |k|·|k ĥ|². In general the cancellation is (π/12)(C_D − 6C_Φ)|k|³, so it holds if and only if C_D = 6C_Φ. This is a self-contained check of the CHMS normalizations against Zarembo's non-renormalization (Section 4.3).

**One-loop check (S3).** The exact one-loop Maldacena–Wilson kernel ∬(|ẋ||ẏ|n·n′ − ẋ·ẏ)/|x−y|², evaluated on a Gaussian bump h = εe^{−σ²}, gives I(ε)/ε² → 2π. On an internal bump j = εe^{−σ²} it gives −π. These are the predictions πB₁∫|k|³|ĥ|² = 2πB₁ and −πB₁∫|k||ĵ|² = −πB₁, with B₁ stripped. The quartic deviation scales as ε², and a three-point Richardson extrapolation lands within 2×10⁻⁸. This is a floating diagnostic of an analytic expansion.

**The first correlators not determined by B.** At O(ε⁴) the response needs the connected four-point functions of the displacement multiplet (𝔻𝔻𝔻𝔻, 𝔻𝔻ΦΦ, ΦΦΦΦ). These are nontrivial functions of the cross-ratio. They are known at strong coupling from AdS₂ fluctuations (Giombi–Roiban–Tseytlin, arXiv:1706.00756; Ferrero–Meneghelli, arXiv:2103.10440) and constrained at finite coupling by integrability plus bootstrap (Cavaglià–Gromov–Julius–Preti, arXiv:2107.08510). The smooth hierarchy of work package B therefore has no unresolved term at second order and a known but nontrivial input at fourth. The first non-polynomial, nonlocal shape response lives at quartic order.

## 3. Retarded response, spectral measure and work (milestone M2)

Take H(s) = H₀ − h(s)D + (seagull), with D the Hermitian Lorentzian displacement and h the transverse displacement of the heavy source. Supplied work is W(T) = −∫_{−∞}^T ḣ⟨D⟩ ds.

**Spectral measure.** The Euclidean function 12B σ⁻⁴ equals ∫₀^∞ e^{−Ωσ}dμ(Ω) with dμ = (C_D/6)Ω³dΩ = 2BΩ³dΩ, confirming the proposal's (7). For the tilt, dμ_Φ = C_ΦΩ dΩ.

**Proposition 2 (locality of the linear straight-line response).** Under the same locality and scale axioms as Proposition 1, for any unitary conformal line defect, and in particular for the Maldacena–Wilson line at every λ and N, the Wightman function is ⟨D(s)D(0)⟩ = C_D/(s − i0)⁴. Its commutator is the contact distribution
\[
\langle[D(s),D(0)]\rangle=C_D\big[(s-i0)^{-4}-(s+i0)^{-4}\big]=-\frac{i\pi C_D}{3}\,\delta'''(s).
\]
Hence χ_R(s) = iθ(s)⟨[D(s),D(0)]⟩ is supported at s = 0 and defined up to local terms. The renormalized susceptibility is the polynomial
\[
\chi_R(\omega)=m_R\,\omega^2+i\,\frac{\pi C_D}{6}\,\omega^3=m_R\,\omega^2+2\pi i B\,\omega^3,
\qquad
\langle D(s)\rangle=-m_R\,\ddot h(s)+2\pi B\,\dddot h(s).
\]

*Proof.* One-dimensional conformal symmetry fixes the Euclidean two-point function of the dimension-2 primary. Its continuation σ = is + 0 gives the Wightman function. The distributional identity (x ∓ i0)^{−n} = x^{−n} ± iπ(−1)^{n−1}δ^{(n−1)}/(n−1)! gives the commutator.

The antihermitian part is fixed by the spectral density, Im χ_R(ω) = π sgn(ω)ρ(|ω|) = (πC_D/6)ω³. This excludes an iω term. The even part is c₀ + c₂ω², with c₀ = 0 because a static displacement is a symmetry (the seagull cancels the Kubo constant). An ω⁴ term would carry a negative power of the cutoff and vanishes. The heavy-source mass is m_R = c₂ = −2c_R, and continuing k → −iω maps the Euclidean kernel of Proposition 1 onto χ_R. ∎

Two consequences. First, the 2πB h⃛ term is the N=4 Abraham–Lorentz force; at strong coupling 2πB → √λ/(2π), Mikhailov's coefficient. Second, the mechanism is one-dimensional conformal symmetry plus the integer dimension of the displacement: the discontinuity of (s − i0)^{−2Δ} is a contact term exactly when 2Δ is an integer, and the displacement of a line defect has Δ = 2 in every bulk dimension. An earlier draft attributed this to Huygens' principle; that was wrong, since the statement holds in any dimension. Non-contact commutators, i.e. memory, first appear in higher-point functions.

**Proposition 3 (total work).** For a smooth compactly supported drive, W(∞) = 2πB∫ḧ² ds, independent of m_R and of the scheme. This is the CHMS radiated energy ΔE = 2πB∫v̇², including the coefficient.

*Proof.* Integrate by parts: −∫ḣ(−m_Rḧ + 2πB h⃛) = 2πB∫ḧ². ∎

This checks the normalization of the Euclidean-to-Lorentzian map for D and the identification of h. It is not independent evidence for CHMS, whose B enters both sides. S6 reproduces it from the spectral integral, where W_Λ(∞) = ∫dμ_Λ Ω|ĥ(Ω)|² increases monotonically to the target as Λ grows.

**Proposition 4 (the cutoff control is passive, carried by its inertia).** Take dμ_Λ = (C_D/6)Ω³e^{−Ω/Λ}dΩ with the translation seagull. Then:

- The mechanical impedance Z_Λ(p) = [χ_Λ(0) − χ_Λ(p)]/p = ∫(2/Ω)p/(p²+Ω²)dμ_Λ is a Foster function, hence positive real.
- For |p| ≪ Λ, Z_Λ(p) = δm_Λ p − 2πBp² + O(p³ log Λ/Λ), with δm_Λ = (C_D/3)Λ = 4BΛ.
- For every T, W_Λ(T) = ∫dμ_Λ(Ω)Ω⁻¹|∫_{−∞}^T e^{iΩs}ḣ ds|² ≥ 0.
- As Λ → ∞,
\[
W_\Lambda(T)=\frac{\delta m_\Lambda}{2}\dot h(T)^2+2\pi B\Big[\int_{-\infty}^T\ddot h^2\,ds-\dot h(T)\ddot h(T)\Big]+o(1).
\]

*Proof.* Integrating the Kubo kernel by parts cancels the seagull and gives the displayed form of W_Λ(T). For the asymptotics, write iΩF_T = e^{iΩT}ḣ(T) − H_T with H_T = ∫^T e^{iΩs}ḧ. Then ∫₀^∞(Ω²|F_T|² − ḣ(T)²)dΩ = π∫^Tḧ² − πḣ(T)ḧ(T), using Plancherel on the half-line and ∫₀^∞e^{iΩu}dΩ = πδ(u) + i P/u with the endpoint half-weight. Dominated convergence handles the factor e^{−Ω/Λ}, since Ω²|F_T|² − ḣ(T)² = (ḧ(T)² − 2ḣ(T)h⃛(T))/Ω² + O(Ω⁻⁴) is integrable. The same expansion gives the rate: the finite-Λ remainder is −(C_D/6)(ḧ(T)² − 2ḣ(T)h⃛(T))(log Λ)/Λ + O(1/Λ). ∎

S6 confirms the limit at five times T, and the O(log Λ/Λ) approach.

**Relation to the proposal's (8).** There Y_Λ = pχ_Λ is the Kubo response without the seagull. It is positive real for the supply h·d⟨D⟩/ds, but it keeps a static restoring term χ_Λ(0) = 8BΛ³ that the translation-invariant defect does not have. The "fifth power" in the proposal is correct for Y's Foster measure 2Ωdμ_Λ, whose mass is 96BΛ⁵. For comparison, dμ_Λ itself has mass 12BΛ⁴, and the physical impedance's measure (2/Ω)dμ_Λ has mass 8BΛ³.

**Proposition 5 (the renormalized finite-time account is never passive).** Let m_R ≥ 0 be finite. Let h vanish for s < s₀ and be C^{n+1} on [s₀, s₀ + δ) (one-sided derivatives at s₀), with h^{(k)}(s₀⁺) = 0 for k < n, h^{(n)}(s₀⁺) ≠ 0 and n ≥ 3. Then
\[
W_R(T)=\frac{m_R}{2}\dot h(T)^2+2\pi B\Big[\int_{s_0}^T\ddot h^2-\dot h(T)\ddot h(T)\Big]<0
\]
for all T > s₀ sufficiently close to s₀.

*Proof.* With x = T − s₀ and h ≈ cxⁿ, the bracket is −c²n²(n−1)(n−2)x^{2n−3}/(2n−3)·(1+o(1)), while m_Rḣ²/2 = O(x^{2n−2}). ∎

For the flat onsets e^{−1/x^α} the ratio ḣḧ/∫ḧ² tends to 2, so negativity persists (observation, checked by the independent referee). It does not hold for every C^∞ drive: an onset such as e^{−1/x}(1 + 0.9 sin(1/x²)) has ḣ = 0 at times accumulating at s₀, where W_R = 2πB∫ḧ² > 0. S6 exhibits the negativity for the drive (1−s²)⁵, where the onset ratio is 7/4, for m_R = 0, 10, 10³ and 10⁵.

This is the classical Abraham–Lorentz–Dirac–Schott account: the total is positive, and the Schott energy −2πBḣḧ is indefinite. Positivity at finite time is carried by regulator-scale inertia that renormalization removes. The natural Maldacena–Wilson scheme, c_R = 0 (hence m_R = 0), is the extreme case. This matches Fiol–Martínez-Montoya's observation (JHEP 03 (2020) 087) that for conformally coupled scalars the radiated power depends on the derivative of the acceleration and the radiative energy density is not positive definite. It is also why Chernicoff–García–Güijosa's finite-mass string equation (arXiv:0903.2047) has no pre-acceleration while the point limit is Lorentz–Dirac.

**Tilt channel.** With the R-rotation seagull, χ^Φ_R(ω) = iπC_Φω + O(ω² log(Λ/ω)/Λ), which is 2πiBω in the continuum, so ⟨Φ_a⟩ = −2πB ȷ̇_a. For every T, W^Φ(T) = 2πB∫_{−∞}^T ȷ̇² ≥ 0, from the cutoff-free half-line Plancherel identity (S6). The internal-direction channel is an exact ohmic resistor, finite-time passive with no counterterm. The two channels carry the same coefficient 2πB, as supersymmetry requires.

**Source norms.** Four norms appear here, and they should not be conflated:

- Euclidean shape Hessian: Ḣ^{3/2} for h and Ḣ^{1/2} for j.
- Total Lorentzian work: Ḣ² for h and Ḣ¹ for j.
- Finite-time renormalized storage: indefinite.

None of these is the unweighted L² norm of a signal. Comparing with L² radiation signals would need an additional map. At linear order that map would be a fixed differential operator, and it would not introduce memory.

**Consequence for work packages E and F.** At linear order about the straight line, any input/output channel built from D or Φ_a has a Laplace transfer that is a polynomial. With ω = ip, χ(p) = −m_Rp² + 2πBp³ for the displacement (so pχ = −m_Rp³ + 2πBp⁴) and χ^Φ(p) = −2πBp for the tilt. Changing λ or N changes only 2πB. There is no front (2π/p)^ω, no variable exponent, no delayed singularity, and no identity endpoint as a parameter varies.

The ultraviolet continuum does lie outside the finite-spectral-mass hypothesis of the [thermal front-rigidity theorem](../../WZW/notes/THERMAL_BOUNDARY_COUPLING_AND_FRONT_RIGIDITY_TEST_20260923.md). But the escape produces locality, not the needed front. The linear straight-line channel is closed as an arithmetic candidate. The closure is scoped to linear order on the straight line; it does not exclude nonlinear or non-straight constructions.

## 4. The growing trace (preparation for milestone M3)

### 4.1 Scaling collapse

**Proposition 6.** For u(t) = at, q_a(Tr) = √T q_{a√T}(r). More generally, the prefix generated by u up to time t is √t times the prefix generated by u_t(r) = u(tr)/√t up to time 1.

*Proof.* The chain g̃_r(z) = g_{Tr}(√T z)/√T satisfies the Loewner equation with driver u(Tr)/√T. ∎

In N=4 SYM, dilatation invariance of renormalized loops, up to cusp anomalous dimensions, then gives
\[
W(a,t)=F\big(a\sqrt t,\ \delta/\sqrt t\big)\,(\mu\sqrt t)^{-\Gamma_{\rm tot}(a\sqrt t)},
\]
where δ is the rounding scale and Γ_tot is the sum of the cusp anomalous dimensions, zero if rounding removes the cusps. The Loewner parameter is therefore not an independent clock in the conformal theory. The t-hierarchy for the linear driver is the dependence on one shape parameter s = a√t, and the short-time limit is the backtracking limit a → 0. This is proved given conformal invariance; T2 checks the scaling numerically. Pure YM at fixed flow resolution differs, because there t/τ is meaningful.

### 4.2 Constant n₀ with a straight return chord (the proposal's first observable)

In units where t = 1, the trace and chord bound a sliver of width w(y) = (s/6)y(2−y), where y ∈ [0,2] is the height along the chord. The cusp openings at base and tip are both s/3 (T3). The pairs on opposite legs are nearly antiparallel with the same scalar charge, so gauge and scalar exchange add.

**One loop (T4).** log W⁽¹⁾ = B₁[J_c(s) + O(s²)]: chord–chord pairs vanish and trace–trace pairs are O(s²) by the curvature bound. The trace–chord exchange J_c has a closed-form chord integral. With cusp neighbourhoods of size ε excised,
\[
s\,J_c(s)\longrightarrow 24\pi\log\frac{2-\varepsilon}{\varepsilon}\qquad(s\to0),
\]
confirmed numerically to 3×10⁻⁴ after extrapolation, with an s log s remainder. Thus log W⁽¹⁾ ≈ (3λ(1−1/N²)/(2πs))·log((2−ε)/ε). The logarithm per cusp is Γ⁽¹⁾(π − s/3, 0) = −3λ(1−1/N²)/(4πs), the near-antiparallel cusp.

**All orders (proof sketch).** The near-antiparallel limit Γ_cusp(π − θ, 0) ≈ −c(λ,N)/θ, where c is the antiparallel-lines potential coefficient (e.g. Drukker–Forini, arXiv:1105.5144), together with thin-loop factorization, gives log W ≈ (6c/s)[log(1/ε̂) + O(1)]. Here c = λ(1−1/N²)/(4π) + O(λ² log λ), and c = 4π²√λ/Γ(1/4)⁴ at planar strong coupling. So W diverges as t → 0 at fixed a, and the a = 0 member is not a normalizable control: it has zero width, so the linear divergence does not cancel.

**Smooth fields at fixed resolution.** Write R̃ for the base-to-tip transport with scalar −Φ. Then the exact first equation is
\[
\dot Q_t=\big[ikJ_t+k\mathcal G_t+(|\dot q|+q\cdot\dot q/|q|)\hat\Phi_t(1)\big]Q_t ,
\]
with hats taken with R̃. The tip coefficient ≈ 2/√t dominates, so W_τ = 1 + 8t⟨N⁻¹trΦ_{n₀}(0)²⟩_τ + O(t^{3/2}). This is perimeter growth from the non-cancelling scalar arclength coupling, not a shape response; T5 verifies the equation and the 8t coefficient configuration by configuration.

This observable is not recommended as the primary M3 family. In both regimes it measures the scalar self-interaction of the loop, and its continuum short-time limit is singular.

### 4.3 The tangent-coupled profile is trivial

With n = M T (Zarembo loops), ⟨W⟩ = 1 for every curve. The literature establishes this as follows: Zarembo (hep-th/0205160) found no quantum corrections for the planar 1/4-BPS case, at one loop and semiclassically; Guralnik–Kulik (hep-th/0309118) proved shape independence and ⟨W⟩ = 1; Dymarsky–Gubser–Guralnik–Maldacena (hep-th/0604058) confirmed it at strong coupling. Corners are BPS cusps (θ = φ, Γ_cusp = 0). So the trace plus chord in this family has Ẇ ≡ 0, and its first-equation insertion average vanishes identically. That is a Ward-identity control, not an evolution. Proposition 1 reproduces it at O(ε²) exactly because C_D = 6C_Φ. This family should be kept only as a null control.

### 4.4 The flipped-return completion

Keep n₀ on the trace and use −n₀ on the return chord. The chord traversed from tip to base with connection iA·dx − |dx|Φ is the inverse of the base-to-tip transport R with connection iA·dx + |dx|Φ. So Q_t = R_t(1)⁻¹U_t, with the same Maldacena–Wilson connection on both legs, and at a = 0 the transport is exactly the identity (T5: ‖Q − I‖ ≈ 2×10⁻¹⁵). In the continuum, opposite legs are nearly antiparallel with opposite scalar charge, which is the no-force configuration, and both cusps have (φ, θ) ≈ (π − s/3, π), i.e. they are nearly BPS.

**Proposition 7 (first equation, smooth fields, every configuration).** Let k = q₁q̇₂ − q₂q̇₁, n̂ = (−q₂, q₁)/|q| and γ_t = |q̇| − q·q̇/|q| = |q̇|(1 − cos β_t) ≥ 0, where β_t is the angle between q̇ and q. Let hats denote conjugation by the chord transport R_t(r). Then
\[
\boxed{\dot Q_t=\Big[\,ik\,(J_t+i\mathcal G_t)+\gamma_t\,\hat\Phi_t(1)\Big]Q_t,\qquad
J_t=\int_0^1 r\,\hat F_{12,t}(r)\,dr,\quad \mathcal G_t=\int_0^1 r\,\widehat{(\hat n\cdot D\Phi)}_t(r)\,dr.}
\]

*Proof.* Growing the prefix gives U̇ = (iA·q̇ + |q̇|Φ(q))U. The parent's ordered-transport variation on the chord x(r) = rq, with η = rq̇, gives Ṙ(1) = iA(q)·q̇ R(1) + ∫R(1,r)𝓘(r)R(r,0)dr, where
\[
\mathcal I(r)=r\,iF_{\nu\mu}\dot q^\nu q^\mu+r|q|\,\dot q^\nu D_\nu\Phi+\Phi\,q\cdot\dot q/|q| .
\]
The gauge tip terms cancel and leave |q̇|Φ̂(1). Next, F_{νμ}q̇^νq^μ = −kF₁₂. Splitting q̇ into its radial part and q̇_⊥ = (k/|q|)n̂, the radial gradient term integrates by parts, because ∂_rΦ̂ = (q·DΦ)^ (the chord connection commutes with Φ). This cancels the ∫Φ̂ term and leaves −(q·q̇/|q|)Φ̂(1). ∎

T5 checks the result against finite differences of directly integrated transports, on a noncommuting SU(2) background with nonconstant A and Φ. The relative error is ≤ 9×10⁻⁸ at eight (a,t) points for both families, with the decomposed and raw insertion forms agreeing to 2×10⁻¹¹.

The expectation-level equation is Ẇ = ik(M_F + iM_G) + γM_Φ, where M_X = ⟨N⁻¹tr(X Q)⟩ and X is J, 𝒢 or Φ̂(1). It holds under the parent's regularity and moment assumptions. Every coefficient vanishes at a = 0. For the linear driver, k = −(2a/3)√t(1 + 11s²/180 + …) and γ = (a²√t/18)(1 − 2s²/45 + …) (T5 and the referee). Their ratio γ/|k| = a/12 is dimensionful. The relative weight of the tip insertion therefore depends on the field scale: about a√τ at fixed flow resolution, and of order s in the continuum, where the only length is √t.

**Short time at fixed resolution (proof sketch; remainder not bounded here).** With 𝒜 = −(2a/9)t^{3/2} the oriented area,
\[
\tfrac1N\operatorname{tr}Q_t-1=\tfrac1{2N}\operatorname{tr}\Big(\mathcal A\,(iF_{12}+D_1\Phi)(0)+\tfrac{a^2t^{3/2}}{27}\Phi(0)\Big)^2+O(t^{7/2}),
\]
configuration by configuration; T5 finds agreement at the percent level at t = 10⁻³ and 2.5×10⁻⁴. In an SO(6)-invariant, parity-invariant flowed state this gives
\[
W^{\rm flip}_\tau=1+\frac{2a^2t^3}{81}\big(C^\Phi_\tau-C_\tau\big)+\frac{a^4t^3}{1458}S_\tau+O(t^{7/2}),
\]
with C_τ = ⟨N⁻¹trF₁₂²⟩_τ (the parent's coefficient), C^Φ_τ = ⟨N⁻¹tr(e·DΦ_{n₀})²⟩_τ and S_τ = ⟨N⁻¹trΦ_{n₀}²⟩_τ. The pure-YM term −(2a²/81)C_τt³ reappears, now competing with a scalar-gradient term of opposite sign.

**Continuum, one loop (T4).** log W⁽¹⁾ = B₁[J_f(s) + O(s²)] with
\[
J_f(s)/s\longrightarrow-\frac{2\pi}{3}\Big(\log\frac{2-\varepsilon}{\varepsilon}-2(1-\varepsilon)\Big),
\]
confirmed to 7×10⁻⁴. The logarithm per cusp is Γ⁽¹⁾(π − s/3, π) = λ(1−1/N²)s/(48π). So the continuum member approaches 1 like 1 − (λ(1−1/N²)/(24π))|s|[log(ℓ/ε) + O(1)]. The dependence on |a| is non-analytic, because the reflection a → −a is a symmetry.

The two regimes, a²t³ at fixed flow and |a|√t log in the continuum, are both regular. The order of the limits t → 0 and τ → 0 changes the exponent but does not produce a divergence. This family is the recommended primary observable for M3.

## 5. Assessment relative to the proposal

The proposal's cautions held up, and several of its open items are now decided:

- **Mixed separated terms.** The mixed terms in its (5) vanish by conformal symmetry and can be deleted with that justification.
- **Correlators not determined by C_D (Deliverable B).** At second order there are none, apart from c_R. The first nontrivial input is the four-point function of the displacement multiplet.
- **Deliverable C.** Complete for the straight line: a retarded kernel, its spectral data, the one local ambiguity m_R, the source norms, and the work and radiation identity. The finite-time failure of passivity is the scoped negative result the proposal allowed for.
- **Work packages E and F for the linear straight-line channel.** Closed negatively, for a structural reason (one-dimensional conformal symmetry with an integer protected dimension) that applies to every conformal line defect.
- **Work package D.** The recommended first observable should be replaced; the flipped return is proposed. The optional tangent-coupled family is a null control.
- **The spectral model (8).** It should include the seagull. The positive-real object for the agent's work is the impedance Z_Λ, not Y_Λ.

On the program goal. The displacement ↔ radiation channel was the most natural place in N=4 SYM to look for a causal positive response. At linear order it is local, so the arithmetic kernel's memory and log-n delays cannot come from it. They would have to come from nonlinear shape response (quartic order and beyond), from non-straight backgrounds, or from the Loewner family itself, whose conformal content is a one-parameter family of shapes W(s). Nothing found so far points toward the Weil form.

The one structural rhyme with the arithmetic side is that positivity holds cumulatively but not instantaneously, here because of the Schott term. It is an analogy and should not be read as evidence. The physical M3/M4 calculation is well posed and worth completing on its own terms. An arithmetic comparison should wait until a nonlocal causal kernel exists.

## 6. Next calculations

1. **One-loop flipped-return W(s), complete.** Add the trace–trace term, a stated cusp subtraction and the finite part as a function of s. Then repeat with a flow-smeared propagator to exhibit the crossover from |s| log to a²t³ at ℓ ~ √τ.
2. **Second evolution equation for the flipped family.** This is the analogue of parent eq. (2). It needs ordered double insertions of F̂, (n̂·DΦ)^ and Φ̂(1), and the derivative of the tip insertion, including q̇·DΦ at the tip.
3. **Quartic smooth-shape response.** Use the strong-coupling four-point functions of the displacement multiplet to obtain the O(ε⁴) term of log Z and its Lorentzian continuation. This is where nonlocal response first appears on the straight line.
4. **Closure audit for the flipped family** (parent Section 7.2 analogue). Record which transverse-current, Yukawa and scalar-potential insertions survive when the derivative moments are reduced with Schwinger–Dyson equations.
5. **Arithmetic comparison:** not until items 1–4 give a nonlocal causal kernel.

Items 1 and 2 were taken up on 24 September in the [flipped-return analysis](FLIPPED_RETURN_TRACE_ANALYSIS_20260924.md): the second equation, the complete one-loop structure in two schemes, and the closure inventory. The [continuation note](CONTINUATION_AFTER_FIRST_SESSION_20260924.md) gives the updated order of work.

## 7. Statement ledger, records and provenance

| Statement | Status |
|---|---|
| Proposition 1 (quadratic response) | Proof, conditional on stated defect-CFT axioms and CHMS inputs; reflection origin cited |
| Cubic vanishing | Proof sketch |
| Zarembo cancellation iff C_D = 6 C_Phi | Proof (algebra) |
| Proposition 2 (locality), Proposition 3 (total work) | Proof, under the same locality and scale axioms as Proposition 1 |
| Proposition 4 (cutoff passivity and asymptotics) | Proof, including the O(log Λ/Λ) rate |
| Proposition 5 (onset negativity) | Proof for finite-order onset; flat e^{−1/x^α} onsets are an observation; false for some oscillating C^∞ onsets |
| Tilt resistor | Proof |
| Proposition 6 (scaling) and the conformal collapse | Proof, given conformal invariance up to cusp anomalies |
| Sliver: one-loop 1/s law | Analytic leading order plus labelled numerical computation |
| Sliver: all orders | Proof sketch relying on the near-antiparallel cusp limit |
| Zarembo loops have W = 1 | Literature |
| Proposition 7 (flipped first equation) | Proof for smooth fields; expectation version conditional as in parent |
| Flipped short-time t^3 formula | Proof sketch, remainder unbounded |
| Flipped one-loop O(s) law | Analytic leading order plus labelled numerical computation |
| Arithmetic closure of the linear straight-line channel | Consequence of Propositions 2–3, scoped to linear order |

**Records.** Run from the investigation directory `papers/susy-positivity/investigations/wilson-loewner/`:

```sh
python3 N4SYM/numerics/check_straight_line_response.py --output /tmp/n4sym-sl.json
python3 N4SYM/numerics/check_trace_completion.py --output /tmp/n4sym-tc.json
```

Both use the standard library only and are deterministic, with preserved records under `N4SYM/numerics/records/`. They are not registered in `validation/drafts.py`, because N4SYM has no manuscript yet. The existing `validation/check_package.py check` already reported six inventory mismatches at `8b22141`, from the committed proposal, and these additions add more. It was deliberately not refreshed, because `refresh` rewrites the curated author and scope fields; see the audit.

**Primary sources.** Correa–Henn–Maldacena–Sever, [arXiv:1202.4455](https://arxiv.org/abs/1202.4455) (HTML full text consulted through a fetch summary for eqs. 5, 6, 14, 20, 25, 55, 58); Zarembo, [hep-th/0205160](https://arxiv.org/abs/hep-th/0205160); Guralnik–Kulik, [hep-th/0309118](https://arxiv.org/abs/hep-th/0309118); Dymarsky–Gubser–Guralnik–Maldacena, [hep-th/0604058](https://arxiv.org/abs/hep-th/0604058); Chernicoff–García–Güijosa, [arXiv:0903.2047](https://arxiv.org/abs/0903.2047); Fiol–Martínez-Montoya, [JHEP 03 (2020) 087](https://link.springer.com/article/10.1007/JHEP03(2020)087). Only the abstracts of these last five were consulted. The four-point-function references in Section 2 and Drukker–Forini are cited from memory and should be checked before any manuscript use. The [parent YM hierarchy](../../notes/GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md) supplied the tip series (independently re-derived here; c₁–c₁₂ agree exactly) and the transport conventions.

Prepared for Edward Baker with substantial LLM assistance (Claude Opus 5.5, Anthropic) in derivation, programming and drafting. The derivations were checked by the same assistant through independent numerical diagnostics; independent mathematical and physical review is outstanding.
