# A physical channel with memory: the finite-mass source, its exactly local boundary field, and the quartic straight-line response

24 September 2026. Prepared for Edward Baker.

**Model:** Claude Fable 5.1 (Anthropic), session configuration `claude-fable-5-1`; the serving model can differ and the runtime did not expose a model identifier for this session.  
**Reasoning effort:** not exposed; not inferred.  
**Status:** this note carries out option (B) of the [second continuation](CONTINUATION_AFTER_SECOND_SESSION_20260924.md), chosen by the author: return to the arithmetic goal by looking for a physical channel with memory. Tasks B1 (finite-mass heavy source) and B2 (quartic straight-line response) are covered.

- **Checks.** Two standard-library programs, [`check_finite_mass_response.py`](../numerics/check_finite_mass_response.py) (107 cases) and [`check_quartic_input.py`](../numerics/check_quartic_input.py) (93 cases), with records. All cases pass, deterministically.
- **Referee.** Two separate referee contexts of the same model re-derived every item of Sections 1–3 with their own code (Section 7). They confirmed all of them, corrected one remainder order and one sign in a limit, and added qualifications that are incorporated here. One referee located a 1999 paper whose published conclusion for the observable of Section 2 disagrees with the exact result found here; that comparison is recorded with its caveat.
- **Review.** There has been no independent specialist review.
- **Arithmetic.** No arithmetic comparison is run. The decision not to run one is itself a result (Section 4).

**Repository baseline:** `8b22141`; the first two N4SYM sessions and this one are uncommitted.

## 0. Summary

**1. The finite-mass source is the first channel with memory, and its memory is a single exponential.** At strong coupling the heavy source of mass m is the endpoint of a string at z_m = √λ/(2πm) (Chernicoff–García–Güijosa). Linearizing the string about the static configuration and imposing the endpoint condition Π^z = F, the retarded solution x(t,z) = Y(t − z + z_m) + z Ẏ(t − z + z_m) gives three exact statements:
\[
F(t)=m\,\ddot Y(t),\qquad X(t)=Y(t)+z_m\dot Y(t),\qquad m\ddot X=F+z_m\dot F .
\]
Here X is the physical endpoint position and Y the retarded auxiliary trajectory. The third equation is the nonrelativistic, small-force limit of the CGG equation (their eq. 28), recovered independently. The auxiliary trajectory is the causal exponential smearing of the physical one, Y = (1 + z_m d/dt)⁻¹X, so the force needed to sustain a prescribed trajectory has the susceptibility
\[
\chi_m(\omega)=\frac{-m\,\omega^2}{1-i\omega z_m}=-m\omega^2-i\frac{\sqrt\lambda}{2\pi}\omega^3+\frac{\sqrt\lambda}{2\pi}z_m\omega^4+\dots,
\]
with a single pole at ω = −i/z_m. The first two terms are the mass and the Abraham–Lorentz/Mikhailov term of the first note (2πB → √λ/2π), and the rest is the memory. The memory scale is the Compton scale z_m of the dressed quark, as the continuation anticipated.

**2. Finite mass restores finite-time passivity, and the Schott term is the cross term of a square.** The work supplied by the force is exactly
\[
W(T)=\int_{-\infty}^T F\dot X\,dt=\frac m2\dot Y(T)^2+\frac{\sqrt\lambda}{2\pi}\int_{-\infty}^T\ddot Y^2\,dt\ \ge 0\quad\text{for every }T,
\]
where (√λ/2π)Ÿ² = (√λ/2πm²)F² is the CGG radiation rate (their eq. 35, nonrelativistic). Both terms are the string's own energy: the first is the total-derivative part of the string energy density, the second the energy of the wave in flight. As m → ∞ at fixed λ, (m/2)Ẏ² = (m/2)Ẋ² − (√λ/2π)ẊẌ + O(√λ z_m), so the indefinite Schott energy of the first note's Proposition 5 is the O(z_m) truncation of a positive quantity. For the drive (1 − s²)⁵ of that proposition, the renormalized point account is negative just after onset while the finite-mass account is nonnegative (cases D).

**3. The boundary field of the moving source is exactly local in the retarded time.** For the dilaton-coupled operator O (Δ = 4), the linear response of ⟨O(t, r⃗)⟩ to the endpoint motion is an integral over the string depth z ∈ [z_m, ∞) with a continuum of delays u(z) = z − z_m + √(z² + r²). The integrand is nevertheless an exact z-derivative, so only the endpoint contributes:
\[
\widehat{\langle O\rangle}^{(1)}(\omega)\propto e^{i\omega r_m}\,P_4(\omega)\,\hat Y(\omega),\qquad r_m=\sqrt{r^2+z_m^2},
\]
with P₄ a quartic polynomial in closed form (Section 2.3). The response is a fourth-order differential operator on Y evaluated at the single delay r_m, the bulk null travel time from the endpoint to the boundary point. For z_m → 0 it collapses to P = (1 − iωr)/(4r⁶): the boundary point at distance r sees Y(t − r) + rẎ(t − r) = x(t, z = r), the string at height r at the same time. In terms of the physical trajectory the only memory is again (1 − iωz_m)⁻¹. A referee context found that Callan–Güijosa (1999) computed this observable at z_m = 0 and reported an "infinitely broadened pulse"; their intermediate kernel differs from the exact one beyond ω = 0 (Section 2.4, with caveat). The exact localization is the dilaton analogue of the light-cone localization of the energy density of the Mikhailov string (Athanasiou–Chesler–Liu–Nickel–Rajagopal; Hatta–Iancu–Mueller–Triantafyllopoulos; Hubeny).

**4. Verdict for the arithmetic goal.** At linear order the finite-mass channel is a rational transfer function with one simple pole, times a single fixed light-travel delay. The exponents are integers fixed by the wave equation and by the integer dimension of O; the single scale z_m rescales time without changing the shape. There is no power front (2π/p)^ω, no logarithmic tangent and no hierarchy of delays. The channel fails the "front and tangent" test of the proposal's Section 9 before any prime is involved, so no arithmetic comparison is run. The physical results of items 1–3 stand on their own.

**5. The quartic straight-line response has memory, a coupling-dependent exponent, and no scale.** The generalized free field is exactly linear, so the cubic retarded response is entirely the connected four-point function of the displacement multiplet, O(1/√λ) at strong coupling. For the tilt channel it is controlled by the singlet exchange of the lowest non-protected operator Φ₆, of dimension Δ₆(λ) = 1 + λ/4π² + … (weak) and 2 − 5/√λ + 295/24λ − 305/16λ^{3/2} + … (strong), which gives power-law kernels with a coupling-dependent exponent. But every kernel about the straight line is homogeneous in the time differences: the defect has no scale, so no fixed delays can arise at any order without a background. The transcribed strong-coupling four-point functions of the Δ = 1 fields (GRT eq. 4.19) pass crossing symmetry in both channels and reproduce the anomalous dimensions −5, −5, −4 through their logarithms; the transcribed Δ = 2 functions fail crossing and are not used.

## 1. The finite-mass source at strong coupling (task B1)

### 1.1 Setup and conventions

Poincaré AdS₅, ds² = (R²/z²)(−dt² + dx⃗² + dz²), Nambu–Goto tension 1/(2πα′), R²/α′ = √λ; R = 1 below. The string ends on a flavour brane at z = z_m (T = 0, flat embedding) and extends to the Poincaré horizon. Its static energy is m = (√λ/2π)∫_{z_m}^∞ dz/z² = √λ/(2πz_m), which is CGG's relation z_m = √λ/(2πm). An external force acts on the endpoint through S_F = ∫dt F(t)x(t, z_m), equivalently CGG's boundary condition Π^z_x|_{z_m} = F (their eq. 6). One transverse direction is kept; the three decouple at linear order.

**Quadratic action and equations.** √(−det g) = z⁻²√(1 + x′² − ẋ²), so S₂ = −(√λ/4π)∫dt dz z⁻²(x′² − ẋ²) and ẍ = x″ − (2/z)x′. The boundary variation gives (√λ/2π)z_m⁻²x′(t,z_m) + F = 0, i.e. x′(t,z_m) = −(z_m/m)F(t). The sign is physical: a positive force makes the endpoint lead and the string trail (x′ < 0). The boundary term at z → ∞ vanishes for a source switched on at finite time because the retarded solution vanishes at large depth; for monochromatic modes the infalling condition is imposed by hand.

**Retarded solution.** The mode equation f″ − (2/z)f′ + ω²f = 0 is Bessel of order 3/2, hence elementary: f_± = (1 ∓ iωz)e^{±iωz}. With e^{−iωt}, the branch (1 − iωz)e^{−iω(t−z)} moves toward the horizon and is the retarded one; the other is a wave emerging from the horizon and is excluded by the vacuum initial condition (equivalently by Im ω > 0). In the time domain,
\[
x(t,z)=\tilde X(t-z)+z\,\tilde X'(t-z),
\]
the linearization of Mikhailov's solution. Write Y(t) := X̃(t − z_m).

### 1.2 Exact endpoint relations (Proposition 1)

From x′(t,z) = −zX̃″(t − z) and the boundary condition, F(t) = mŸ(t). From X(t) = x(t, z_m), X = Y + z_mẎ. Therefore mẌ = F + z_mḞ. All three are exact at linear order (cases A, to 10⁻⁶ or better). CGG's equation (28) and radiation rate (35), as transcribed through a fetch summary of arXiv:0906.1592, reduce in the nonrelativistic small-force limit to m dv/dt = F + z_m dF/dt and dE/dt = (√λ/2πm²)F² (cases E; the residual scales as the cube of the amplitude). The dispersion relation (34) gives, in the same limit, the intrinsic momentum p_q = mv − z_mF = mẎ: the auxiliary velocity is the momentum of the dressed quark.

**Memory representation (Proposition 2).** Y = (1 + z_m∂_t)⁻¹X with the causal kernel z_m⁻¹e^{−s/z_m}θ(s) (case B). Hence F̂ = χ_m(ω)X̂ with χ_m = −mω²/(1 − iωz_m), pole at ω = −i/z_m (lower half-plane, causal for e^{−iωt}), and the expansion displayed in Section 0. With the first note's convention χ_R := −χ_m, the first two terms are m_Rω² + 2πiBω³ at m_R = m and 2πB = √λ/2π. At ωz_m ≫ 1 the endpoint is a pure damper, |χ_m| → (m/z_m)ω = (2πm²/√λ)ω: the string is an infinite transmission line.

**Qualifications (referee).** Rationality holds for endpoint quantities at T = 0, in the strict planar limit (rigid flavour brane; its back-reaction and "flavour photon" radiation are O(1/N)), at strict λ → ∞, and at linear order. A black-brane background replaces the single pole by a quasinormal tower and drag. The S⁵ fluctuations decouple at quadratic order and are not sourced by a four-dimensional force.

### 1.3 Energy account (Proposition 3)

FẊ = mŸ(Ẏ + z_mŸ) = d/dt[(m/2)Ẏ²] + mz_mŸ², and mz_m = √λ/2π. So
\[
W(T)=\frac m2\dot Y(T)^2+\frac{\sqrt\lambda}{2\pi}\int_{-\infty}^T\ddot Y^2dt,
\]
given Ẏ(−∞) = 0 (string initially static). Both terms are nonnegative for every T (cases C, D). The canonical energy density of S₂ is ℋ = (√λ/4π)z⁻²(ẋ² + x′²) with flux S_z = −(√λ/2π)z⁻²ẋx′. On the retarded solution, ẋ² + x′² = X̃′² + 2zX̃′X̃″ + 2z²X̃″²; the first two terms are −z²∂_z[X̃′(t−z)²/z], which integrates to Ẏ²/z_m, and the third gives (√λ/2π)∫_{−∞}^tŸ²: hence ∫_{z_m}^∞ℋ dz = W(t) exactly (case C, string_energy_equals_work). The flux at the endpoint equals FẊ and at large depth tends to (√λ/2π)X̃″(t − z)². Note that (m/2)Ẏ² is not the endpoint kinetic energy (m/2)Ẋ².

**Point limit (Proposition 4).** Ẏ = Σ_n(−z_m∂_t)ⁿẊ gives (m/2)Ẏ² = (m/2)Ẋ² − (√λ/2π)ẊẌ + (√λ/4π)z_m(Ẍ² + 2ẊX⃛) + O(√λz_m²). The cross term is the Lorentz–Dirac Schott energy. The remainder is O(z_m) at fixed λ, not O(z_m²) as first written (referee correction); the expansion is asymptotic for ωz_m ≪ 1. Cases D verify the O(z_m) coefficient and that the deviation halves with z_m.

### 1.4 Front test on the endpoint channel

The maps X → F and X → Ÿ have one simple pole; F → Ÿ = F/m has none; F → X has a double pole at ω = 0 and no finite pole. No delay factors appear (the shift z_m between X̃ and Y is absorbed in the definition of Y). The kernel shape is universal: χ_m z_m³/√λ = −(ωz_m)²/(2π(1 − iωz_m)) depends on ωz_m only (case F). Low- and high-frequency exponents are 2 and 1. So there is no power front with a non-integer exponent, no logarithmic tangent and no delay hierarchy. The channel fails the "front and tangent" row of the proposal's Section 9 table.

## 2. The boundary field of the moving source (task B1, extended)

### 2.1 Retarded bulk-to-boundary propagator

For a Δ = 4 operator, K_E = Cz⁴/(z² + ρ² + τ_E²)⁴. The Wightman continuation τ_E = i(τ − iε) and the Kubo sign give
\[
K_R(\tau,\rho,z)=-2\theta(\tau)\,\mathrm{Im}\,K_W=-\frac{\pi}{3}\,C\,\theta(\tau)\,z^4\,\delta'''(z^2+\rho^2-\tau^2),
\]
using Im(s + iε)⁻⁴ = (π/6)δ‴(s). It is normalized so that ∫dτ K_R = ∫dτ_E K_E = Cz⁴(5π/16)(z² + ρ²)^{−7/2}; the referee also checked that its Laplace transform equals the Euclidean Fourier transform at ω = iΩ to 13 digits. The response is supported on the light cone t − t′ = √(ρ² + z²) only, because (s + iε)⁻⁴ is real for s ≠ 0; this relies on the integer dimension. For non-integer Δ the interior would carry a power-law tail sin(πΔ)θ(−s)|s|^{−Δ}. All dilaton Kaluza–Klein harmonics have Δ = 4 + ℓ.

### 2.2 Linear response and static check

The string sources O with density z⁻² at transverse position x(t′,z)ê. To first order, |r⃗ − xê|² = r² − 2x(r⃗·ê), so
\[
\langle O\rangle^{(1)}(t,\vec r)=\frac{2\pi}{3}C\,(\vec r\cdot\hat e)\int_{z_m}^\infty dz\,z^2\;\partial_s^4\Big[\frac{x(t-\sqrt s,z)}{2\sqrt s}\Big]_{s=z^2+r^2}.
\]
For a constant displacement this is (35π/16)C(r⃗·ê)x₀∫dz z²(z² + r²)^{−9/2}, which equals −x₀ê·∇ of the static profile C(5π/16)∫dz z²(z² + r²)^{−7/2} (cases G, static_dipole_sum_rule; the ratio 4 = dipole/monopole). The static profile is Coulombic at r ≫ z_m and regular at r → 0, CGG's "gluonic cloud" of size z_m.

### 2.3 Exact localization (Proposition 5)

For Y = e^{−iωt}, x(t′,z) = e^{−iωt′}(1 − iωz)e^{iω(z−z_m)} and, with g₄(s;ω) := ∂_s⁴[e^{iω√s}/(2√s)] = e^{iωρ}ρ⁻⁹[(ωρ)⁴ + 10i(ωρ)³ − 45(ωρ)² − 105i(ωρ) + 105]/32 (ρ = √s),
\[
\mathcal T(\omega;r,z_m)=\int_{z_m}^\infty dz\,z^2(1-i\omega z)e^{i\omega(z-z_m)}g_4(z^2+r^2;\omega).
\]
The delays u(z) = z − z_m + √(z² + r²) increase monotonically from r_m = √(r² + z_m²), so a continuum of delays seems to contribute. It does not. The integrand is an exact z-derivative, dG/dz, with
\[
G(z)=-\,e^{i\omega(z+\rho)}\frac{N(z,\rho,\omega)}{32\,\rho^7(\rho+z)^3},\qquad \rho=\sqrt{z^2+r^2},
\]
\[
N=\omega^4\rho^3z^3(\rho+z)^2+2i\omega^3\rho^2z^2(\rho+z)^2(2\rho+3z)-\omega^2\rho z(\rho+z)(8\rho^3+24\rho^2z+33\rho z^2+15z^3)
\]
\[
\qquad-\,i\omega(\rho+z)S_4+S_4,\qquad S_4=8\rho^4+24\rho^3z+48\rho^2z^2+45\rho z^3+15z^4 .
\]
G was found by a polynomial ansatz with (ρ² − z²) denominators and verified by symbolic differentiation (a Laurent-polynomial ansatz in z and ρ alone has no solution; the (ρ + z)⁻³ is essential). Since G → −e^{2iωz}ω⁴/(64z²) → 0 as z → ∞,
\[
\mathcal T(\omega;r,z_m)=e^{i\omega r_m}\,P_4(\omega),\qquad P_4(\omega)=\frac{N(z_m,r_m,\omega)}{32\,r_m^7(r_m+z_m)^3}.
\]
Cases G verify the total derivative at three points to 10⁻⁶, the closed form against contour-rotated quadrature at five (ω, r, z_m) points to 10⁻⁸, and the time-domain statement directly: for a short pulse in Y the depth integral equals Σ_k c_k i^k Y^{(k)}(t − r_m) to 10⁻⁶ relative, vanishes before the arrival and vanishes again after the pulse has passed (no tail).

**Consequences.**
- (a) As a functional of Y the boundary response is a real fourth-order differential operator at the single delay r_m, the bulk null travel time from the endpoint to the boundary point (Paley–Wiener: an entire function of exponential type r_m).
- (b) In terms of the physical trajectory, T̂_X = e^{iωr_m}P₄(ω)/(1 − iωz_m); N is not divisible by (1 − iωz), so the exponential memory is genuinely present and is the *only* memory.
- (c) For z_m → 0, P₄ → (1 − iωr)/(4r⁶), i.e. ⟨O⟩^{(1)} ∝ (r⃗·ê)[Y(t − r) + rẎ(t − r)]/(4r⁶) = (r⃗·ê)x(t, z = r)/(4r⁶): the boundary point at distance r reads the string at height z = r at the same time (sign corrected by the referee). The high-frequency exponent is 1; for z_m > 0 it is 4 with coefficient z_m³/(32r_m⁵u′(z_m)), the stationary-phase-free endpoint asymptotics (cases G).
- (d) The static value P₄(0) = S₄/(32r_m⁷(r_m + z_m)³) is a closed form for (105/32)∫_{z_m}^∞z²(z² + r²)^{−9/2}dz (case G, static_closed_form).
- (e) The far field, to leading order in 1/r at fixed ω, is e^{iωr}[ω⁴z_m³ + 4iω³z_m² − 8ω²z_m − 8iω]/(32r⁵): local in t − r, and reducing to −iω/(4r⁵) for the massless quark (cases G, far_field).

**Mechanism.** The Δ = 4 propagator is light-cone supported (2.1), and the retarded string x = Y(u) + zẎ(u) = −z²∂_z[Y(u)/z] is a congruence of null rays from the endpoint. The retarded field of a null source in AdS is a shock wave whose boundary imprint is the boundary light cone of the emission event (Hubeny's picture for ⟨T_μν⟩). G(z) is the imprint of the segment [z, ∞), and the sum telescopes. The same localization of the energy density holds for the full nonlinear Mikhailov string (Athanasiou et al.; Hatta et al.), which suggests, but does not prove, that the dilaton localization persists beyond linear order. This is an open item.

### 2.4 Relation to Callan–Güijosa (with caveat)

A referee context reports that Callan and Güijosa (Nucl. Phys. B 565 (2000) 157, hep-th/9906153) computed this observable for z_m → 0 with the same wave and the same z⁻² source, obtained an intermediate kernel (their eq. 25) f(u) = iω³/u⁶ − 12ω²/u⁷ − 57iω/u⁸ + 105/u⁹ and a final superposition over delays ζ|x|, ζ ∈ [1, ∞) (their eq. 26), and described an "infinitely broadened pulse". The exact kernel here is 32g₄e^{−iωρ} = ω⁴/ρ⁵ + 10iω³/ρ⁶ − 45ω²/ρ⁷ − 105iω/ρ⁸ + 105/ρ⁹; the two agree only at ω = 0. The referee also found their (26) inconsistent with their (25) in the ω → 0 limit. If confirmed, the broadening is an algebra error in the 1999 paper and Proposition 5 corrects it. **Caveat:** the referee read the arXiv PDF through a text extractor, and this session could not fetch the paper (rate limit). The comparison must be checked by eye against the journal version before any public statement.

### 2.5 Front test on the boundary channel

T̂_X = e^{iωr_m}P₄(ω)/(1 − iωz_m): one fixed delay, one simple pole, integer exponents. The single scale z_m rescales the shape. Agreeing with Section 1.4: no front, no tangent, no delay hierarchy. A finite temperature would add quasinormal poles ω_n ∝ T but no logarithms of primes.

## 3. The quartic straight-line response (task B2)

### 3.1 Operator content of the tilt channel

Deform the internal direction to n(σ) = (j_a(σ), √(1 − j²)) on S⁵, a = 1…5, with |ẋ| = 1. The coupling is exp∫[j_aΦ_a + (√(1 − j²) − 1)Φ₆], and odd orders vanish by SO(5). The O(j⁴) term of log Z is complete with four pieces (referee): (1/4!)∫⁴ j j j j⟨Φ_aΦ_bΦ_cΦ_d⟩_conn; −(1/4)∫³ j_aj_bj²⟨Φ_aΦ_bΦ₆⟩; +(1/8)∫²j²j²⟨Φ₆Φ₆⟩_conn; −(1/8)∫j⁴⟨Φ₆⟩. Φ₆ inserted on the half-BPS line is the lowest non-protected operator (Polchinski–Sully; Beccaria–Giombi–Tseytlin eq. 3.6–3.7): Δ₆ = 1 + λ/4π² + O(λ²) at weak coupling and 2 − 5/√λ + 295/(24λ) − 305/(16λ^{3/2}) + (351845/13824 − 75ζ(3)/2)/λ² + … at strong coupling (Ferrero–Meneghelli, agreeing with the quantum spectral curve of Grabner–Gromov–Julius), where at strong coupling Φ₆ ↔ y^ay^a (GRT eq. 4.43). Remarks: ⟨Φ₆⟩ vanishes in a conformal scheme but in a cutoff scheme is a linear divergence that is needed to make the tree-level quartic term finite; the Φ₆ terms are contact-type (two source times coincide) and at weak coupling ⟨Φ₆Φ₆⟩ is the leading quartic response, O(λ), whereas the connected four-point function is O(λ²); the ⟨Φ₆Φ₆⟩ term gives j_a(t)∫dt′j(t′)²|t − t′|^{−2Δ₆}, a coupling-dependent power law; GRT's unit-normalized G must be multiplied by (2B)².

### 3.2 Structural propositions

**Proposition 6 (the GFF is linear).** In the λ → ∞ limit the defect fields are generalized free, [Φ(t), Φ(0)] is a c-number (∝ δ′ for Δ = 1), and every nested commutator vanishes. The cubic retarded response therefore comes entirely from the connected four-point function; at separated source times it is O(1/√λ) in unit normalization. Equivalently, log Z = −S_cl[n] + O(λ⁰) and its quartic term is the tree Witten diagram of the sphere fluctuations.

**Proposition 7 (memory).** The connected function at O(1/√λ) contains log|χ| and log|1 − χ| with nonzero coefficients (at χ → 1 they are −2/5, −1, +1 in the S, T, A channels), whereas the GFF part is rational. The Lorentzian continuation of a rational function gives contact-supported commutators; that of the logarithms gives step-function discontinuities. So the cubic response has memory at O(1/√λ). The logarithms of χ are γ log χ from χ^{Δ₀+γ/√λ}: the memory is tied to the anomalous dimensions, which resum to power laws with coupling-dependent exponents. A retarded kernel needs all Wightman orderings, i.e. the continuation across χ = 0, 1, ∞ with iε prescriptions; this was not carried out.

**Proposition 8 (no scale).** Dilatations make every retarded kernel about the straight line homogeneous in the time differences; the cubic tilt kernel has degree −4. Anomalous-dimension logarithms appear as log(t_ij/t_kl) and are scale-free. A constant background tilt is an SO(6) rotation of the half-BPS line and introduces no scale either. Hence no fixed delay, and in particular no hierarchy at log 2, log 3, …, can arise about the straight line at any order. A time-dependent background, a curved contour, a temperature or a smeared observable would introduce a scale.

### 3.3 Validation of the strong-coupling input

The four-point functions were transcribed from a fetch summary of GRT (eqs. 4.3, 4.19, 5.17–5.19), so they were tested rather than trusted. With χ = t₁₂t₃₄/(t₁₃t₂₄), G = G^{(0)} + G^{(1)}/√λ and the S, T, A structures, crossing 1 ↔ 2 gives G_{S,T}(χ) = G_{S,T}(χ/(χ − 1)), G_A(χ) = −G_A(χ/(χ − 1)); crossing 1 ↔ 3 gives G(χ) = (χ/(1 − χ))^{2Δ}R G(1 − χ) with R₅ = [[1/5, 28/25, −4/5], [1/2, 3/10, 1/2], [−1/2, 7/10, 1/2]] for SO(5) and R₃ = [[1/3, 10/9, −2/3], [1/2, 1/6, 1/2], [−1/2, 5/6, 1/2]] for SO(3) (both R² = 1; the referee derived them independently).

- **Δ = 1 (y^a), the superprimary of the displacement multiplet.** G^{(0)} and the transcribed G^{(1)} satisfy both crossing relations to 10⁻¹⁰ (cases Y). G_S^{(1)} = −2χ² log χ − (43/30)χ² + O(χ³ log χ) with no constant and no linear term, so the identity is not corrected. The χⁿ log χ coefficients, divided by the GFF OPE coefficients 2/5, 3/5, −1, give γ_S = −5 (Δ₆ at strong coupling), γ_T(Δ₀ = 4) = −5 (GRT eq. 4.34 with n = 1) and γ_A(Δ₀ = 3) = −4; there is no χ² log χ term in the T channel, as the protected Δ = 2 traceless-symmetric operator requires. The referee, peeling off blocks order by order, found the patterns γ_S(n) = −(2n² + 3n + 5), γ_T(n) = −(2n² + 3n), γ_A(n) = −(2n² + 5n + 4), to be compared with GRT eqs. 4.34–4.36. The Δ = 1 transcription is therefore validated and usable.
- **Δ = 2 (x^i).** The GFF part passes; the transcribed tree functions violate crossing in 16 of 18 relations and give γ_T(Δ₀ = 4) = −40/9 instead of the −5 of GRT eq. 5.24 (cases X). The transcription is unreliable and is not used. The displacement four-point function is in any case fixed by the superconformal Ward identities from the Δ = 1 function (Liendo–Meneghelli–Mitev; Ferrero–Meneghelli: ⟨𝒟𝒟𝒟𝒟⟩ = f𝔛 + 𝔻f).
- **Integrability.** For all-equal internal indices G₁₁₁₁ = G_S + (8/5)G_T and G^{(1)}_{1111} = −2χ² log χ + …, so the quartic tilt integrand G^{(1)}/(t₁₂²t₃₄²) is integrable at coincident points (cases Q).

### 3.4 Verdict for the arithmetic goal

The quartic response is the first nonlocal one on the straight line and its memory exponent, set by Δ₆(λ) ∈ (1, 2), is coupling dependent. That is a structural fact worth recording against the front-rigidity results of the WZW notes: a fixed protected dimension gives no variable exponent, but a non-protected one does. However: (i) the response is nonlinear, and the proposal's tests presuppose a linear channel; a linear channel would need a background that supplies a scale; (ii) by Proposition 8 no channel about the straight line has fixed delays, so the "first prime delay" row cannot be passed in principle; (iii) the theory is not to be adjusted to a target, and the relation λ ↔ ω would be exactly such an adjustment. No arithmetic comparison is run.

## 4. Assessment

- **Option (B) has a clean outcome.** The finite-mass source is a physical channel with memory, its memory is one exponential, its boundary field is exactly local in retarded time, and the channel is rational. The quartic straight-line response has memory with a tunable exponent but no scale. Neither supports an arithmetic comparison.
- **The physical results are self-contained.** Exact linearized CGG dynamics, a positive finite-time energy account that exhibits the Schott term as a truncation, and the exact light-cone localization of the dilaton response with a closed-form quartic transfer function (contradicting, if the referee's reading holds, a 1999 claim of broadening) are results independent of the arithmetic goal.
- **What memory exists in N=4 SYM line defects.** Three kinds were met: the Compton-scale exponential of a massive source (rational), the anomalous-dimension power laws of non-protected operators (scale-free), and, prospectively, quasinormal towers at finite temperature (rational poles). None has a hierarchy of fixed delays.

## 5. Next steps

1. **Check Callan–Güijosa by eye** (journal version, eqs. 25–26) before stating the correction publicly.
2. **Nonlinear localization.** Test whether the dilaton response of the full Mikhailov string localizes on the light cone at O(Y²), as the energy density does.
3. **Lorentzian cubic kernel.** Continue G^{(1)} across χ = 0, 1, ∞ with the iε prescriptions and compute the third-order Kubo kernel of the tilt channel, or equivalently the Lorentzian tree Witten diagram of the AdS₂ sphere fluctuations with the light-cone-supported Δ = 1 propagator. This would make Proposition 7 quantitative.
4. **Linearization about a background with a scale** (a rotating internal direction, or a cusp), if a linear channel with memory about the line is still wanted. Any such construction must derive its scale, not choose it.
5. **Manuscript.** A draft covering the three N4SYM sessions is in `N4SYM/manuscript.tex` (Section 7).

## 6. Statement ledger

| Statement | Status |
|---|---|
| m = √λ/(2πz_m); S₂; bulk equation; boundary condition sign | Proof (elementary), referee confirmed |
| F = mŸ, X = Y + z_mẎ, mẌ = F + z_mḞ | Proof, exact at linear order |
| Agreement with CGG eqs. 28, 35, 34 in the nonrelativistic limit | Check of transcribed formulas (fetch summary); numbers to be confirmed by eye |
| χ_m rational with one pole; expansion matching Prop. 2 of the first note | Proof |
| Energy identity and string-energy identity | Proof |
| Schott term as O(z_m) truncation; remainder O(√λ z_m) | Proof (asymptotic series) |
| Finite-time passivity of the finite-mass account | Proof, given Ẏ(−∞) = 0 |
| Retarded Δ = 4 propagator, sign and constants | Proof, referee confirmed two ways |
| Exact localization: G(z) and P₄ | Proof (symbolic differentiation), numerically verified |
| Massless limit P₄ → (1 − iωr)/(4r⁶) | Proof |
| Callan–Güijosa discrepancy | Referee reading through a text extractor; unverified by eye |
| Front test failure (linear finite-mass channel) | Proof, under the qualifications of 1.2 |
| GFF cubic response vanishes | Proof |
| Cubic response has memory at O(1/√λ) | Proof sketch (discontinuity structure); Lorentzian kernel not computed |
| No scale about the straight line | Proof (dilatations) |
| Δ = 1 transcription validated | Numerical verification of crossing and OPE constraints |
| Δ = 2 transcription unreliable | Numerical falsification |
| Anomalous-dimension patterns γ_{S,T,A}(n) | Referee observation from the transcribed functions; compare with GRT 4.34–4.36 |
| Δ₆(λ) expansions | Literature (BGT; FM; GGJ), transcribed |

## 7. Records, review and repository state

Run from `papers/susy-positivity/investigations/wilson-loewner/`:

```sh
python3 N4SYM/numerics/check_finite_mass_response.py --output /tmp/n4sym-fm.json
python3 N4SYM/numerics/check_quartic_input.py --output /tmp/n4sym-qi.json
```

Both use the standard library only, run in a few seconds, and are byte-for-byte deterministic. Records are in `N4SYM/numerics/records/`. The [audit](../reviews/review_claude_third_session_20260924.md) records the two referee passes. A draft manuscript covering the three sessions is at [`../manuscript.tex`](../manuscript.tex), with [`../BUILD.md`](../BUILD.md) and [`../DRAFT_HISTORY.md`](../DRAFT_HISTORY.md); the programs are not yet registered in a validation replay.

Pages that could not be read this session: the arXiv abstract pages of 0903.2047 and the PDF of hep-th/9906153 were refused by the fetch proxy (rate limit). Publication data were taken from the INSPIRE API; the CGG equations from the arXiv PDF of 0906.1592 through a fetch summary; the GRT, BGT and FM formulas likewise. All formula transcriptions used in derivations were validated by limits or by crossing, as recorded above.

Prepared for Edward Baker with substantial LLM assistance (Claude Fable 5.1, Anthropic) in derivation, programming and drafting. Independent specialist review is outstanding.
