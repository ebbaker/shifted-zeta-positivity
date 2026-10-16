# Independent review of "Yang–Mills boundary sources and the Weil form" (consolidated draft, 25 September 2026)

25 September 2026. Prepared for Edward Baker by Claude (Anthropic). Model line: claude-fable-5-1 (Fable 5.1) per the runtime environment, session configured as claude-opus-5-5; the serving model may differ. Reasoning effort not exposed.

Reviewed object: `manuscript.pdf` / `manuscript.tex` and `sections/*.tex` at commit `187548e` (identical to the author's local checkout; working tree clean), together with all twenty notes, the seven earlier reviews, `PROJECT_OUTLINE.md`, and the seven numerical programs with their records. The earlier reviews were all produced by the same assistant that wrote the manuscript (GPT-6 Codex); this is the first assessment from a different system. It is still a model-assisted review, not a human specialist's.

Classification used throughout: **proof** (complete argument from stated hypotheses, rederived here), **computer-assisted** (interval-certified; none in this folder), **floating** (double-precision diagnostic), **heuristic**.

## 0. Verdict

1. **The mathematics is correct.** Every displayed formula in Sections 1–10 and Appendix B was rederived by hand, and every proof was followed; the constants (1.9), the Gram matrix (2.11), the electric pairing (3.5)–(3.8), the branching law (4.6), the Mellin/gamma identity behind (5.17), the flow Jacobian (7.2), the edge profiles (8.9)–(8.11), the determinant in Theorem 9.1, and the probe (10.2) all check. No error was found in any theorem or proof. Independent numerics (Section 2 below) confirm the two central limits, Theorem 4.1 and Theorem 5.2, to 10⁻¹⁴, and confirm, for the first time in this folder, the normalization of the Weil form (1.5) against the actual zeta zeros.

2. **The manuscript under-states its central scientific fact: the Yang–Mills state is inert in every affirmative identity.** The prime mixed limits (4.7)–(4.9), the archimedean limit (5.14) and the complete signed identity (5.19) hold for *every* smooth positive plaquette marginal ρ, and they reduce, after the unitary 𝒲ρ of (5.9), to two classical objects on ℓ²(ℕ) and L²(ℝ₊): Burnol's conductor operator log|x| + log|p| (whose spectral function on even functions is exactly Re ψ(¼ + iτ/2) − log π) and the multiplicative shift eₙ ↦ e_{an} (the Adams operation ψᵃ on SU(2) characters, or equivalently the Bost–Connes isometry μ_a). The arithmetic content is put in by hand through the labels n ∈ ℕ and the coefficients n^{−1/2}; SU(2) contributes those labels and a unitary dressing, nothing else. The notes say this plainly (quoted in Section 3.1 below); the manuscript never does. As written, the abstract and Section 1.2 invite a reader to think the "actual interacting state" did work.

3. **The negative results are the substantive output, and they are strong enough to close the fixed-finite-slab route.** Proposition 1.2 (a source locally bounded in any ordinary input norm cannot realize Q) together with the uniformity remark in Appendix B.4 excludes every smearing law ∫ f(x)A(x)dx with locally integrable ‖A‖ — hence every smearing of a bounded observable family on a finite lattice with a smooth weight — and every limit of such laws with uniform local bounds; Theorem 7.2 (Lebesgue spectrum of the current) excludes every vector-field-generated translation; Theorem 6.1 shows the limiting winding module, which is L²(ℝ × ẑ) with Bost–Connes relations, cannot be embedded boundedly into the SU(2) class sector; Proposition 8.1 and Theorem 8.2 show positive completions of the prime part diverge. These four are clean, general, and reusable as filters for other candidates (see the companion note on next steps).

4. **Theorem 10.4 is a transfer statement, not a reduction in difficulty.** Its hypothesis (10.9) already implies RH by Theorem 10.2 and forces the spectral measure (10.10) to be the zero measure. The manuscript says the hypothesis is "substantial and unverified"; it should also say that it is at least as strong as RH. The unconditional probe criterion (Theorem 10.2, Corollary 10.3) is an elementary consequence of the explicit formula for one pole-neutral test with nonvanishing transform — tidy and explicit, not new in substance.

5. **Recommendation.** Accept the pause as a closure. Apply the revisions in Section 4 (framing, literature identifications, one logical qualification, minor corrections), record the new zero-list control in the ledger, then freeze the document as a negative-result record of the program. Do not reopen the hierarchy numerics or the phase-by-phase repairs.

## 1. What was checked and how

### 1.1 Hand rederivation

- **Section 1.** Fundamental solution of −∂² + ¼ and the tail cancellation in Lemma 1.1; the expansion (1.11); the leading logarithm in (1.12); the identity (1.8) from ψ(z) − ψ(a) = ∫₀^∞ (e^{−at} − e^{−zt})/(1 − e^{−t}) dt with t = 2r; ψ(¼) = −γ − π/2 − 3 log 2; the Fourier asymptotic. The pole term (1.7) equals 2 Re( M̄₊ M₋ ) for M± = ∫ e^{±x/2} f, which is the correct Weil pole contribution for the autocorrelation of f.
- **Section 2.** Radial Haar measure (2/π) sin²θ dθ, t₀ − t₂ = 1, and the Gram matrix (2.11).
- **Section 3.** w_k = t_k − ½(t_{k+2} + t_{k−2}); the Haar norm ½ Σ|a(k+2) − a(k)|²; the radial pairing nm cos((m−n)θ) and the angular pairing 2 sin nθ sin mθ / sin²θ from the round metric on SU(2) ≅ S³ with iσ_j orthonormal (this is also where ℓ = 4 and the Casimir n² − 1 come from); the Mellin transform of φ(u) = u²(2πu² − 3)e^{−πu²}, namely s(s−1)π^{−s/2}Γ(s/2)/(4π), and hence ξ(s)/π in (3.14).
- **Section 4.** The weighted adjoint (4.3) by the a-fold change of variable; ‖V_a‖² ≤ C_ρ/c_ρ; ρ_a = Σ_m t_{am} e^{imθ} → t₀; the Toeplitz Riemann sum and Σ_k t_k e^{ikα} = ρ(α); the branching law (4.6) by the root-of-unity sum; the gcd count in (4.8); the coefficient c_m log p at label mp.
- **Section 5.** A₀χₙ = (i/2){(n+½)χ_{n+1} − (n−½)χ_{n−1}} from [E₀, X] with Xχₙ = ½(χ_{n+1} + χ_{n−1}); the three phase asymptotics of Proposition 5.1 and the a = 2 defect 2ρ(π)‖f′‖²/ρ(0); the factor a in (5.7) from ‖eˣ U_{log a} f‖² = a² ∫ e^{2x}|f|²; the unitarity of 𝒲ρ and the Liouville form −∂² + v″/v; the exact −R cancellation through the isometry B; the Mellin transform of the cosine transform, 2(2π)^{−s}Γ(s)cos(πs/2), and its reduction by duplication and reflection to π^{½−s}Γ(s/2)/Γ((1−s)/2), giving γ₊(τ) = π^{iτ}Γ(¼ − iτ/2)/Γ(¼ + iτ/2); i γ₊′/γ₊ = Re ψ(¼ + iτ/2) − log π; the cancellation of the differentiated terms; the sine-channel variant with ¾. (5.19) follows from (5.14) and (4.7) by polarization of (1.5) on 𝒟⁰.
- **Section 6.** The identification of the rational-phase sum with L²(ℝ × ẑ) via Fourier series on ẑ (characters e^{2πirz}, r ∈ ℚ/ℤ), the isometry (6.2) with range projection 1_{aẑ} (measure 1/a), the adjoint argument with Π(1 − 1/p) → 0, and the closability argument in Theorem 6.3 (including that ‖f_L‖₂ → 0 while Q[f_L] → m_{γ₀}).
- **Section 7.** Yθ = −sin θ, div_m Y = −3 cos θ from Δ_{S³} cos θ = −3 cos θ per link, the Jacobian (7.2), the unitary ℛ, the exact Riemann sum (7.7), the unitarity of the sine transform, and the flow-box argument of Theorem 7.2 (r = log tan(θ/2), Yr = −1, one crossing of θ = π/2 per trajectory).
- **Section 8.** ‖V_aF‖² = ∫|F|²ρ_a → t₀‖F‖²_Haar; the explicit coercive bound with the minimizer b log p/(δ + log p); the Stieltjes form of the edge sum, the substitution u = s − log q, and the integration by parts giving h′ + h/2; the exponential expansion of n_Γ with the j = 0 term killed by pole neutrality.
- **Section 9.** Kernel supported at the origin ⇒ finite sum of δ^{(d)}; even real Fourier polynomial; degree ≤ 4 from the logarithmic growth; Vandermonde determinant (−¾)(−8/9)(−5/36) = −5/54; the finite-intersection-property argument.
- **Section 10.** Support and Laplace transform of the infinite convolution of uniforms; zeros of sinh(a_j z)/(a_j z) on the imaginary axis so that 𝓑(1 + z) ≠ 0 for |Re z| < ½; F(±½) = 0; the coefficient F(λ)F(−λ) from the cross-correlation ∫ f̄(x)e^{λx} ∫ f(y)e^{−λy} with the translate; the Laplace-transform/pole argument in both directions; the tempered case via the smooth cutoff; the mean-square identity in Corollary 10.3; the functional-calculus domain in Theorem 10.4.
- **Appendix A.** The two-mode ODE and its SU(2) solution (μ₃ = 0), the linear-driver expansion ϑ = −(2a√C₀/9)t^{3/2}, and the Loewner tip series for q̇ = 1 − 2/q from the implicit equation q + 2 log(1 − q/2) = t. The Monte Carlo numbers were not reproduced (see 1.3).
- **Appendix B.** KMS detailed balance and the centered weights; the 2D gluing formulas; ζ(2g − 2); the scattering coefficient Λ_ξ(2s − 1)/Λ_ξ(2s) and the algebraic relation to ξ(z)/ξ(z + 1).

### 1.2 Independent numerics (new program)

`numerics/check_probe_against_zeros.py`, written from the displayed formulas only, with discretizations different from the existing suite (direct θ-quadrature on a geometric grid for the log-angle term; sparse Gram sums for a five-harmonic marginal; Fourier-side correlation integrals for the probe). Record: `numerics/records/probe-against-zeros-20260925.json`; zero ordinates in `numerics/records/zeta-zeros-700.json` (mpmath, first 700 zeros, last ordinate 1062.915…). All 29 controls pass:

| Control | Result |
|---|---|
| m₊(0) = ψ(¼) − log π versus −γ − π/2 − 3 log 2 − log π | 1.8·10⁻¹⁵ |
| Theorem 5.2, complex f ≠ g, N = 256 and 1024, direct quadrature | 7.6·10⁻¹⁵, 9.6·10⁻¹⁵ |
| Theorem 4.1 with ρ = c(1 + 0.3cos θ + 0.25cos 2θ + 0.1cos 3θ − 0.05cos 5θ), N = 4096: prime mixed limit a = 2, 3, 5 | ≤ 7.3·10⁻¹⁰, O(N⁻²) convergence |
| wound norms a = 2, 3 (ρ_a(0)/ρ(0) = 0.78125, 0.6875, versus Haar ½, ⅓) | ≤ 2.7·10⁻⁹ |
| gcd formula (4.8) for (a,b) = (2,4), (2,3) | ≤ 3.0·10⁻¹⁰ |
| **C_*(t) from the definition (10.3) versus Σ_γ 2|f̂_*(γ)|² cos γt over 700 zeros, twelve t in [0, 7]** | **≤ 1.1·10⁻¹³** |
| closed tail (10.4) at t = 2.5, 3, 4, 6 | ≤ 2.5·10⁻¹⁵ |
| mean square of C_* on [0, 200] versus Σ 2|w_γ|² (Corollary 10.3) | 0.1 % |
| Q[f_*] = C_*(0) = 6.34767… > 0 | — |

The sixth row is the one control the folder lacked: it tests the digamma multiplier, the contact constant, the factor −2Λ(a)/√a, the pole convention and the Fourier convention of (1.5) against arithmetic the manuscript never uses (the ledger in Appendix C says "No zeta zero list was used"). Agreement to 10⁻¹³ at twelve translates leaves no room for a normalization slip anywhere in Sections 1, 5 or 10. Tail weight beyond the last zero is 5·10⁻¹⁸.

### 1.3 Repository checks, build, and provenance (rerun in a clean container)

- All six runnable programs reproduce their records: 13/13, 19/19, 19/19, 57/57, 64/64, 64/64 controls pass; the largest deviation from any recorded value is 1.3·10⁻¹¹ on a quantity of size 2.5·10³ (roundoff). The script hashes recorded inside each record match the files on disk.
- `check_positive_hierarchy.py` crashes on NumPy ≥ 2.4 (`np.trapz` was removed; lines 231 and 234). With `np.trapezoid` it passes 64/64. This should be fixed for reproducibility.
- `check_finite_slab.py` has no sampling-free mode; the sampler `sample_finite_slab.cpp` compiles with g++ 13 and clang++, but the Monte Carlo was not rerun. The pre-sampling controls (geometry, quaternion algebra, 30 projection systems) reproduce exactly. The loop expectations in Appendix A.3 therefore rest on the recorded run only.
- `BUILD_RECORD.json`: all 67 fingerprinted files match by sha256 and size; the PDF has 35 pages. `latexmk` rebuilds with zero errors, zero unresolved references, zero overfull boxes; the rebuilt text is byte-identical to the committed PDF's text.
- Notes versus manuscript: no formula, constant, sign, or exponent differs. Items the manuscript dropped are listed in Section 3.4.

## 2. Classification of results

| Result | Status | Verified | Remark |
|---|---|---|---|
| Lemma 1.1, Prop. 1.2 | proof | hand | (1.12) is the UV requirement every candidate must meet |
| Prop. 2.1, compact tail (2.8), marginal (2.9)–(2.11), Ward argument 2.4 | proof | hand | finite-lattice statements |
| Theorem 3.1 | proof | hand; 64 floating controls | the local bound (3.6) is the decisive line |
| Euler/Poisson identities 3.1 | proof | hand; numeric Mellin check | |
| Theorem 4.1, Prop. 4.2 | proof | hand; new non-Haar controls | universal over ρ (Section 3.1) |
| Weak escape (4.15) | proof | hand | |
| Prop. 5.1 | proof | hand; 3 floating controls | |
| Theorem 5.2 | proof | hand; new independent quadrature | Burnol's conductor identity in disguise |
| (5.19) complete signed identity | proof (iterated limit) | hand | restatement of the explicit formula on 𝒟⁰ |
| (5.20)–(5.21) phase divergences | proof | hand; 2 floating controls | |
| Theorem 6.1 | proof | hand | clean; the limiting module is L²(ℝ × ẑ) with Bost–Connes relations |
| Lemma 6.2, Theorem 6.3 | proof | hand | 6.3 proves RH inside a contradiction argument; logically fine |
| Theorem 7.1, (7.8)–(7.9) | proof | hand; 19 floating controls | |
| Theorem 7.2 | proof | hand | strongest obstruction in the paper; flow-box argument |
| Prop. 8.1, Theorem 8.2 | proof | hand | |
| Theorem 8.3 | proof (PNT) | hand; 5 floating controls at A ≤ 10⁶ | |
| Theorem 9.1 | proof | hand | |
| Theorem 9.2, OS/phase-space variant | proof (abstract) | hand | hypotheses never met here |
| Lemma 10.1, Theorem 10.2, Cor. 10.3 | proof | hand; new zero-list control | elementary from the explicit formula |
| Theorem 10.4 | proof | hand | hypothesis ≥ RH (Section 3.3) |
| Appendix A continuous/discrete identities | proof (under stated regulated hypotheses) | hand where checkable | |
| Appendix A.3 experiment | floating Monte Carlo | not rerun | negative small-family result; no arithmetic content |
| Appendix B | proof / comparison | hand | |

## 3. Findings

### 3.1 The affirmative identities are independent of the Yang–Mills state (major, framing)

Where ρ enters: in (4.7) only through the packet normalization ρ(α)^{−1/2}, which cancels; in (5.14) not at all, because φₙ = ρ^{−1/2}χₙ is an orthonormal basis and 𝒲ρ maps it to Haar sines, so ⟨F_R f, C_ρ F_R g⟩_ν is literally a computation in L²(0, π) with the Haar weight. The compensation v″/v in (5.10) is precisely the removal of the only ρ-dependent term. ρ at the nonzero roots of unity enters only the *obstruction* quantities: ρ_a(0)/ρ(0) in (4.9), (7.9) and the contact divergence; ρ(π) in the a = 2 defect; Σρ(β)sin²β in (5.7); t₀ in Proposition 8.1.

The notes already state this: "The coefficient in (1) is also universal over smooth positive marginal densities … it has not been shown to express special four-dimensional YM dynamics" (`notes/CHARACTER_CHANNEL_LIMITS…`, line 247); "The prescription includes rho in both operator and source … it consequently works for every smooth positive marginal and does not identify special four-dimensional dynamics" (`notes/ELECTRIC_PARITY…`, line 142). The manuscript's only trace is "The φₙ are an actual orthonormal basis" (Section 5.3) and the weight-transport paragraph in Appendix B.1.

Consequence for the reader: the abstract's "Character packets in its actual interacting state have exact phase branching and limiting winding pairings with the prime-power weights" is true but misleading; the same sentence holds for the Haar measure on one copy of SU(2), for U(1) with labels ℕ, or for ℓ²(ℕ) with no group at all. The signed identity (5.19) is, after 𝒲ρ, the statement

  Q(f, g) = ⟨Mf, (H_Burnol − Σ_a Λ(a)(ψᵃ + ψᵃ*)) Mg⟩ in the limit of Mellin packets M f = Σ n^{−1/2} f(log(n/N)) eₙ,

i.e. the explicit formula written in Burnol–Connes form. That is a correct and useful way to organize the explicit formula, but it is not a Yang–Mills result. Section 1.2, Section 11 and the abstract should say so in one sentence each.

### 3.2 Missing literature identifications (major, novelty statement)

- C_ρ of (5.12) is Burnol's conductor operator log|x| + log|p| restricted to the even sector: log D is log|p| on the sine (Dirichlet) sector of L²(0, π) rescaled to ℝ₊, and B* M_{log q} B is log|x| transported through the parity map. Burnol's theorem (math/9811040) gives the spectral function Re ψ(¼ + iτ/2) − log π on even functions and Re ψ(¾ + iτ/2) − log π on odd functions, which is exactly the pair the manuscript recovers with and without B. The manuscript cites Burnol only as "compare". The notes (`ELECTRIC_PARITY…`, line 32) are explicit that no novelty is claimed for this operator; the manuscript should be equally explicit.
- V_a F(g) = χ_a(g)F(gᵃ) is the Adams operation ψᵃ on the representation ring of SU(2) (composed with multiplication by χ_a, which converts ψᵃ on class functions to the label shift n ↦ an on the χₙ basis). The Haar limiting module of Theorem 6.1, L²(ℝ × ẑ) with isometries 𝒱_a, 𝒱_a*𝒱_a = 1, 𝒱_a𝒱_a* = 1_{aẑ}, is the Bost–Connes structure (Bost–Connes 1995; Connes 1999; Connes–Consani). The manuscript should name it; Theorem 6.1 then reads "the SU(2) class sector cannot host the Bost–Connes module", which is a sharper and more quotable statement.
- The bibliography also omits the sources the earlier review ranked (Burnol math/0001013, Bost–Connes, Connes 1998/9, Deninger, Hedenmalm) and the primary-source ledger in the notes. Since the manuscript claims no novelty for "conductor-operator and explicit-formula mathematics" (Section 1.2), it should cite the actual sources of those ingredients.

### 3.3 Theorem 10.4 does not reduce difficulty (medium, logic)

By Theorem 10.2, any vector v with ⟨v, V_t v⟩ = C_*(t) has a bounded correlation, hence RH holds, hence the spectral measure of v is (10.10), i.e. the zero measure with weights |f̂_*(γ)|². The "spectral filtering construction" then produces J from v by dividing by f̂_*. So the theorem transfers a zero-measure vector into a source law; it does not lower the bar. The text "reduces the amount of mixed data that needs to be established" (Section 11) should be replaced by "replaces the full pairing by one correlation whose existence is itself at least as strong as RH". The last sentence of Section 11's penultimate paragraph ("It is not legitimate to define the physical spectral measure by the zero ordinates and then invoke that theorem") already points this way.

### 3.4 Material in the notes that the manuscript dropped (medium)

A referee would want: (i) the universality statements above; (ii) the Ṽ_a = ρ^{−1/2}V_aρ^{1/2} negative full-core control (`ELECTRIC_PARITY…`, lines 334–341), which shows the completion becomes −∞ on an explicit two-label vector; (iii) the observation that B*M_hB with any smooth real h adds h(0)⟨f, g⟩ in the packet limit (`reviews/ELECTRIC_PARITY…`, line 134), which shows the contact constant m₊(0) is fixed by the choice of angle unit and parity map, not by any dynamics — this belongs next to the sentence "the parity and the 2π Fourier convention are mathematical parts of the construction"; (iv) the interacting-experiment details (`FIRST_INTERACTING…`, lines 93–124: successive-step distances ≈ 1.1, 1.1, 1.4, Gram condition numbers 220–2702, cold/hot differences 0.3–1.4σ) which justify the sentence "these families did not establish useful closure"; (v) the ranked-mechanisms table of the 24 September review.

### 3.5 Wording that overstates (minor)

- Section 5.2: "Its multiplier will be derived, not assigned." The multiplier is computed from the insertion; the insertion (compensation v″/v, polar map B, angle in turns) was chosen to produce it. Suggested: "The multiplier is computed from the specified insertion; the insertion itself is chosen, and no Yang–Mills principle selecting it has been found."
- Section 1.2: "two actual generalized-source constructions with nonarithmetic pairings" — fine, but add "both universal over the boundary weight".
- Section 11, first paragraph: add "It holds for every smooth positive marginal and is a rearrangement of the explicit formula on Mellin packets."

### 3.6 Minor corrections

- `check_positive_hierarchy.py`: `np.trapz` → `np.trapezoid` (lines 231, 234).
- Appendix C ledger: add the zero-list control; change "No zeta zero list was used" to say which control now uses one.
- `DRAFT_HISTOR.md` should be `DRAFT_HISTORY.md` (the parent folder and the project convention use the full name); `BUILD.md` and `README.md` link to the short name.
- `PROJECT_OUTLINE.md` (lines 35, 114–122, 186) retains the causal K_ω(z) transfer as a second goal; the manuscript mentions K_ω only as a comparison (Appendix B.4). Align one with the other.
- Typography: "converges smoothly to h" and "Let U denote", "boundary functions B,C" lack math mode (Sections 1.3, 2.1); "Mobius" → "Möbius" (twice); the `\hypersetup` author field says "Drafted for Edward Baker; GPT-6 (Codex) assistance", which is fine, but the title page should carry the author's name as the project convention requires ("Edward B. Baker III" or "Drafted for Edward Baker" consistently).

## 4. Recommended edits, in order

1. Abstract: after "Together these yield the complete signed Weil mixed limit, but not a positive source norm", add "The affirmative identities hold for every smooth positive boundary weight and reduce to Burnol's conductor operator and the Adams operations on ℓ²(ℕ); the Yang–Mills state enters only the obstructions."
2. Section 1.2: add the universality sentence and the identification of the three classical ingredients (Burnol operator, Adams operations / Bost–Connes isometries, explicit formula), with citations.
3. After Theorem 5.2: a remark identifying C_ρ with Burnol's operator and stating that any B*M_hB adds h(0)⟨f, g⟩.
4. After Theorem 6.1: name the limiting module as the Bost–Connes module.
5. Section 10.3 and Section 11: qualify Theorem 10.4 as in 3.3.
6. Section 11: add the two dropped controls of 3.4 (ii)–(iii) as one paragraph.
7. Appendix C: ledger row for `check_probe_against_zeros.py`; fix the "no zero list" sentence.
8. The minor corrections of 3.6; rebuild; refresh `BUILD_RECORD.json`; rename `DRAFT_HISTOR.md`.
9. Tag the result (the project's DRAFT_HISTORY convention points milestones at commits or tags, not snapshot folders).

## 5. Assessment of interest

As a positive-result paper: low. Its affirmative content is a correct rearrangement of the explicit formula in operator form, known since Burnol and Connes, dressed into a lattice Hilbert space by a unitary.

As a negative-result record: moderate and useful within the program. Proposition 1.2, Theorem 6.1, Theorem 7.2 and Proposition 8.1 are short, general, and correct; together they say that no smearing of bounded observables in a finite lattice with a smooth weight (nor any limit of such smearings with uniform local bounds), no vector-field-generated translation, and no termwise-positive completion of the prime part can realize the Weil form, and that the natural home of the winding structure is the Bost–Connes module rather than a compact-group class sector. Those four statements are the transferable output of the YM investigation, and the companion note turns them into a filter for the program's remaining physics candidates.

Section 10's probe is a neat explicit device (a compactly supported pole-neutral test whose Fourier transform has no real zeros, constructed without any zero data), and the resulting one-function criterion for RH is correct; it is a direct consequence of the explicit formula rather than a new criterion.

## 6. Files added by this review

- `reviews/REVIEW_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md` (this file)
- `notes/STRUCTURAL_REQUIREMENTS_AND_NEXT_STEPS_20260925.md` (companion)
- `numerics/check_probe_against_zeros.py`, `numerics/records/probe-against-zeros-20260925.json`, `numerics/records/zeta-zeros-700.json`
- Index entries in `README.md`, `notes/README.md`, `reviews/README.md`, `numerics/README.md`, and the root `CHANGELOG.md`.

No manuscript source, existing note, review, program or record was modified. Nothing was committed.

## 7. Errata (25 September 2026, after the GPT-6 response)

The [response](../response/RESPONSE_TO_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md) and my [reply](../response/CLAUDE_REPLY_TO_RESPONSE_20260925.md) record the discussion; the text above is left as written, with these corrections:

1. **Section 1.2, table row "wound norms".** "versus Haar ½, ⅓" is wrong. The total Haar wound norm is ‖f‖² for every a (V_a is an isometry in the Haar limit); ½ and ⅓ are the identity-phase shares a^{−1}‖f‖², the very quantity the manuscript warns against after (4.9). The pass/fail targets ρ_a(0)/ρ(0) were correct. The program's metadata field `haar_value` has been renamed `identity_phase_part`, with `haar_total_wound_norm` added.
2. **Section 1.2, last paragraph.** "Tail weight beyond the last zero is 5·10⁻¹⁸" reported a single sampled weight, not a tail bound. The regenerated record carries a rigorous envelope bound: Σ_{|γ|>1062.9} 2|f̂_*(γ)|² ≤ 1.2·10⁻¹² on the critical line and ≤ 5.6·10⁻¹¹ for hypothetical zeros anywhere in |Re z| ≤ ½ at t ≤ 7 (control 7). "Leaves no room for a normalization slip" is replaced by: a floating diagnostic agreeing to 10⁻¹³ with a proved remainder below 10⁻¹⁰; a normalization error in (1.5), (1.9) or (10.3) would appear at the 10⁻² to 10⁰ level.
3. **Verdict item 2 and Section 3.1.** "The Yang–Mills state is inert in every affirmative identity" and "enters only the obstructions" overstate: the wound pairings (4.8)–(4.9) and the recovered source (7.3) have state-dependent coefficients. The accurate statement is that the two limits that build (5.19), namely (4.7) and (5.14), are universal over smooth positive marginals, and that the ρ-dependent coefficients are exactly the ones that do not enter (5.19).
4. **Verdict item 3 and Section 5.** "Close the fixed-finite-slab route" is a research judgement, not a theorem: Proposition 1.2 excludes laws locally bounded in an ordinary input norm, not derivative-type distributional laws on the (infinite-dimensional) link-function space; Theorem 7.2 needs its global-section hypothesis (the Kronecker flow on 𝕋² is a smooth flow with pure point spectrum); Theorem 6.1 constrains bounded winding-preserving recovery, not sources in general; Proposition 8.1 excludes one positive decomposition. The four conditions R1–R4 of the companion note are restated with these scopes as N1–N4 in the reply and in the revised note.
5. **Section 3.2.** "Channel-free" (in the companion note) was wrong: the Haar limiting module keeps all a branches, with norms a^{−1}‖f‖² and (1 − a^{−1})‖f‖²; it is their isometric completion.
6. **Section 3.6, `np.trapz`.** Recommend a fallback (`getattr(np, "trapezoid", getattr(np, "trapz", None))`) rather than a replacement, so older environments still run.
7. **Section 3.6, `DRAFT_HISTOR.md`.** The response says the project instructions prescribe this name; the instructions I have say `DRAFT_HISTORY.md`, and the parent folder uses that form. Left as a recommendation for the author.
