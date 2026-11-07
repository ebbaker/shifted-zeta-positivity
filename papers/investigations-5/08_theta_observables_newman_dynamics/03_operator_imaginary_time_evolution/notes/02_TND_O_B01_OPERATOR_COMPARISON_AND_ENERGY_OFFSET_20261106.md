# TND-O-B01: two operator realizations and the cylinder energy offset

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, verified from this turn's metadata. Branch chat0001. **B — initial conceptual analysis, r1.**

**Outcome.** Recommend a cylinder realization with Fourier-prepared source amplitude, a fixed lowest-angular-shell readout, and the relative-energy generator **K = L0 − 4I**. It answers the author's imaginary-time interpretation question without a count instrument. The alternative is the scalar G realization in its explicitly transported H² norm. Neither supplies a theta-specific signed estimate or an intrinsic preparation law.

**Evidence.** The algebra and short spectral-gap argument below are B01 proof-author calculations, with one local normalization/energy clarification. They have no separate assessment. The complete domain, semigroup, observation and finite-order theorem remains the proposed **TND-O-E01** task; it has not been executed. This is a representation/interpretation and scoped compatibility analysis under [avoid/01][a01], not an RH criterion. See the [decision][decision], [proposed contract][request] and [sole register][progress].

## 1. Inherited baseline and the question actually changed

[Parent Note02][parent], §§5–7, (22)–(40), and [shared Review01][review], §§4–5, already give

\[
F_\lambda(u)=e^{\lambda u^2}\Phi(u),\quad
H_\lambda(z)=\tfrac12\int_{\mathbb R}F_\lambda(u)e^{izu}\,du,
\quad LG_\lambda=8F_\lambda,\quad L=1-\partial_u^2,
\]
\[
\partial_\lambda F_\lambda=X_u^2F_\lambda,\quad
\partial_\lambda H_\lambda=-\partial_z^2H_\lambda,\quad
\partial_\lambda G_\lambda=BG_\lambda,\quad B=L^{-1}X_u^2L.
\tag{1}
\]

The source is supplied, including complete unit weights, reflection and absolute scale. Its canonical normalization is H0(z)=ξ((1+iz)/2)/8. The normalization and heat sign were freshly checked in [Rodgers–Tao v5, Introduction (1)–(4)](https://arxiv.org/html/1801.05914v5#S1); no main zero theorem is used. Source and tail payments remain the inherited local proofs, not a new literature claim.

Ordinary cylinder heat applied to a **position-encoded source**, followed by its Fourier readout, multiplies that readout by a Gaussian. That is the established auxiliary baseline. Here the second candidate deliberately changes the encoding: the source occupies **radial momentum**, and the Newman function is read as a **position amplitude**. No equation identifying those different fields is silently imposed.

Throughout, λ=λ0−τ, τ≥0. The initial λ0 may be any finite real number. The physical cylinder remains the radius-1/2 product cylinder; no wall, radial box or discretization is introduced.

## 2. Candidate A: scalar/source realization in a transported norm

Let H_F=L²_even(R,du) and M=X_u², with maximal domain {f∈H_F: u²f∈L²} and core C∞_c,even. Its explicit imaginary-time action is f↦e^(−τu²)f. This acts boundedly for every τ≥0. Positive Newman increments require the unbounded inverse on its domain; the canonical orbit exists for every finite λ by the inherited source decay.

Use the proposed scalar Hilbert space

\[
\mathcal H_G=H^2_{\rm even}(\mathbb R),\qquad
\langle G_1,G_2\rangle_G=\tfrac1{64}\langle LG_1,LG_2\rangle_{L^2},
\quad U G=LG/8.
\tag{2}
\]

Thus U is unitary onto H_F by construction. The norm is
(||G||²+2||G′||²+||G″||²)/64. It is a transported source/Sobolev norm, not ordinary scalar-cylinder L² or a newly derived physical energy.

The candidate nonnegative self-adjoint realization is U⁻¹MU, with

\[
\operatorname{Dom}B_G=\{G\in H^2_{\rm even}:u^2LG\in L^2\},\qquad
\mathcal C_G=8L^{-1}C^\infty_{c,\rm even},
\]
\[
S_G(\tau)G=L^{-1}e^{-\tau u^2}LG,\qquad
\mathcal R_GG=\sqrt{\pi/2}\,\mathscr F(UG).
\tag{3}
\]

Here the unitary full-line Fourier convention is the parent's. On even inputs the forward/inverse signs agree. The source multiplication proof transports its domain and contraction properties; E01 is **not** asked to develop this alternative. Equations (2)–(3) specify the operator realization to which such claims belong. They make no claim about self-adjointness, closure or semigroup bounds in **ordinary L² for G**.

For canonical G, R_G is exactly the old real readout. Its raw integral
(1+z²)∫G(u)e^(izu)du/16 is initially valid only for |Im z|<1. The source transform gives its entire continuation; the new norm does not enlarge the raw strip.

**Useful consequence and baseline.** A complete proof would settle a clean scalar well-posedness/stability question. But ||S_G(τ)G||_G=||e^(−τu²)UG||₂: it is exactly the direct-source estimate. The result explains a norm and domain; it produces no extra arithmetic information. It also does not identify G with a spinor or with a square-root probability amplitude.

## 3. Candidate B: Fourier preparation in the cylinder's lowest angular shell

Use the inherited full spinor space

\[
\mathcal H_C=L^2(\mathbb R_v,dv;\mathcal K),\quad
\mathcal K=L^2(S^2,\Sigma;d\Omega),\quad A=D^2,\quad
L_0=-\partial_v^2+4A.
\]

All angular shells n≥1, rank P_n=4n, and both Dirac signs remain in the ambient operator. The angular eigenvalues/multiplicities were checked against [Camporesi–Higuchi v1, (3.40), (3.54)](https://arxiv.org/html/gr-qc/9505009v1), with the parent's self-adjoint convention and shifted index. The product-cylinder domain is inherited from parent Note02 §3, not imported from that article.

Choose a fixed unit vector χ∈Ran P1 and make the **single operator modification**

\[
K=L_0-4I=-\partial_v^2+4(A-I).
\tag{4}
\]

This subtracts the lowest angular energy; it is not an added fitted potential. On the full Fourier/shell resolution its multiplier is p²+4(n²−1)≥0. The intended maximal domain is

\[
\left\{\Psi\in\mathcal H_C:
\sum_{n\ge1}\int_{\mathbb R}[p^2+4(n^2-1)]^2
\|P_n\widehat\Psi(p)\|_{\mathcal K}^2\,dp<\infty\right\}.
\tag{5}
\]

It is the same set as Dom L0. The proposed core is smooth compactly supported radial fields with finitely many complete angular shells. The intended heat action multiplies each channel by exp(−τ[p²+4(n²−1)]). Zero is a spectral threshold, **not a normalizable ground eigenstate**: p=0 has measure zero. Selecting χ is a declared preparation/readout choice; it is not a parallel spinor, a unique rotationally invariant choice, or replacement of the complete angular Green response by n=1.

Define a source encoding and a bounded field readout by

\[
\widehat{E_\chi f}(p)=f(p)\chi,\qquad
(R_\chi\Psi)(x)=\sqrt{\pi/2}\,\langle\chi,\Psi(x)\rangle_{\mathcal K}.
\tag{6}
\]

The angular pairing is conjugate-linear in χ. Eχ is isometric and ||Rχ||=√(π/2), as maps between the declared L² spaces. **No point evaluation is asserted to be bounded on arbitrary L².** Rχ returns an L² function of x; the canonical source supplies its smooth/entire representative separately.

| Symbol | Role in this candidate |
| --- | --- |
| u | Original source/logarithmic variable and externally prescribed scan argument |
| p | Radial momentum of the physical cylinder; the encoder supplies the calibration p=u |
| v | Physical cylinder position |
| x | Real Newman argument, identified with v at the readout; complex z is analytic continuation, not a physical momentum eigenvalue |

For even f with the required integrability, RχEχf=∫₀∞f(u)cos(xu)du. The design algebra is

\[
KE_\chi=E_\chi X_u^2,\qquad
R_\chi K=(-\partial_x^2)R_\chi,
\tag{7}
\]

on the corresponding domains: the latter follows from (A−I)χ=0 and applies to the full K domain. For canonical preparation,

\[
\Psi_0=E_\chi F_{\lambda_0}
=\sqrt{2/\pi}\,H_{\lambda_0}(v)\chi,
\]
\[
\Psi_\tau=e^{-\tau K}\Psi_0,
\qquad R_\chi\Psi_\tau=H_{\lambda_0-\tau}.
\tag{8}
\]

The equality is first on the real line; its entire continuation is paid through F. The prepared orbit occupies a reducing part of the lowest shell. Higher shells are retained by the full operator and annihilated by this chosen readout; no full-spectrum excitation is claimed. A unit χ may contain both signs of D in that shell. No parity reduction of the first-order Dirac operator is used.

**What is supplied.** The complete theta source, its Fourier preparation including phase/scale, p=u calibration, χ, and the linear amplitude readout. The formula for Ψ0 contains H because it is the Fourier transform being prepared; it does not generate theta from a simpler intrinsic state. It uses no zeros of H to fit K. Ψ is an unnormalized linear spinor amplitude, not sqrt(F), a density matrix, or a Born probability. If physical energy units are wanted, H_rel=εK and τ=εt_E/ℏ use the inherited ε; the λ clock is an explicit identification.

## 4. One local clarification: the energy offset is visible in absolute ITE amplitudes

Keeping L0, the same preparation and fixed readout give

\[
R_\chi e^{-\tau L_0}E_\chi F_{\lambda_0}
=e^{-4\tau}H_{\lambda_0-\tau}.
\tag{9}
\]

Thus the constant offset in (4) cannot be omitted when exact absolute normalization is required. Equivalently one may keep L0 and use e^(4τ)Rχ, but that is an explicitly **time-dependent**, amplifying calibration. The proposed contract chooses (4) and fixed Rχ. No time-dependent calibration is hidden in (8).

There is a stronger reason this factor matters. For any bounded fixed linear map R:H_C→L²(R) and any fixed finite-norm Ψ0,

\[
\|Re^{-\tau L_0}\Psi_0\|_2
\le\|R\|\,\|\Psi_0\|_2e^{-4\tau}.
\tag{10}
\]

On the other hand, Plancherel and the smooth positive source at zero give

\[
\|H_{\lambda_0-\tau}\|_2
=\sqrt{\pi/2}\,\|e^{-\tau u^2}F_{\lambda_0}\|_2
\sim \Phi(0)(\pi/2)^{3/4}\tau^{-1/4}.
\tag{11}
\]

To check the last coefficient, set u=y/√τ in the squared source norm. Its leading factor is Φ(0)²√(π/(2τ)); boundedness of Fλ0 and a Gaussian dominate the rescaled integral. The positive θ half-line expansion gives Φ(0)>0, and Fλ0(0)=Φ(0).

Equations (10)–(11) contradict equality for **all τ≥0**. This is a B01 argument against an unshifted-L0 realization with a bounded fixed L² readout and a fixed finite-norm initial field. It covers nonlocal bounded readouts too. It does **not** exclude unbounded/distributional observations, time-dependent calibration, other generators/encodings, or intrinsic models outside these assumptions. We make no additional finite-time-only obstruction claim. It is not an obstruction to imaginary-time evolution itself.

## 5. Useful consequence, complete payments and limits

The selected benefit is precise: a nonnegative relative-energy Hamiltonian on the stated cylinder can realize the Newman heat family, with an explicit bounded intertwiner, while the unshifted cylinder's spectral gap obstructs the same absolute all-time target in the class (10). This distinguishes an operator interpretation from the original position-source/Fourier-readout auxiliary flow.

The direct baseline still agrees exactly. For any two even L² source inputs f,g,

\[
\|R_\chi e^{-\tau K}E_\chi(f-g)\|_2
=\sqrt{\pi/2}\,\|e^{-\tau u^2}(f-g)\|_2.
\tag{12}
\]

There is no improvement in stability or sign information from the embedding. A geometric explanation is the eligible consumer here. Claims of an intrinsic source law, collision restriction or estimating gain would require another independently useful premise and a new B decision.

For E01, fix |λ0|≤M, 0≤τ≤T, any compact complex-z set and arbitrary **fixed finite** derivative orders. Parent (29)–(34) apply with M+T, since λ0−τ∈[−M−T,M]. They pay every source moment and the full arithmetic tail, hence all prepared K powers and readout derivatives. The entire continuation remains a source statement. Full K-domain/core claims require complete shell exhaustion; the prepared lowest-shell reduction does not stand in for that proof. No growth-in-order theorem, reverse-time bounded semigroup, finite-box approximation or numerical campaign is included.

## 6. Control screen against the actual premises

The [control cluster][controls] is the starting inventory. Here the generic Hilbert construction needs even L² input; finite K powers require polynomial L² moments, and entire readouts require exponential L¹ moments. **Smoothness of f in its source coordinate is not required for these K-domain assertions.** Source differentiation is a different claim.

| Family | Admitted structure and actual premise it fails |
| --- | --- |
| Euler-factor sources | Their smooth even rapidly decaying sources admit both encodings and the gap argument when f(0)>0. They fail unchanged theta arithmetic, which is not used to make K nonnegative or the readout intertwine. No exclusion. |
| Weighted-square / finite-prime controls | Even reflected densities with the recorded rapid tails satisfy the needed L²/moment conditions despite possible unmatched smooth reflection endpoints. They fail full unit weights and/or complete canonical reflection. Those failures do not remove them from this generic operator realization; no unproved spatial source-derivative/core statement is imported. |
| Reflected super-Gaussian / smooth shape / positive-primitive controls | Applicable even L² and exponential-moment data pass. Exact canonical arithmetic fails but is not used by the generic realization. They remain collision controls. |
| Atoms and continuous finite-profile controls | Atoms fail the actual L²-density premise, not merely smoothness; generalized-state versions are outside this contract. Even continuous compactly supported controls do satisfy the L²/moment premises and are not excluded just because they lack smoothness. |

An explicit witness prevents overinterpretation. [Direct Note04 §7][witness] records Φ*(u)=c exp(−u²/4)g(u), where g is the positive even mixture of exp(−u⁴) and its translates by ±4. Its super-Gaussian tail pays every required moment here. Take λ0=1/2 in (8). At τ=1/4 and x=π/4 the output has H*=H*′=0 and H*″>0, exactly as in that source. This bounded heat evolution with a nonnegative self-adjoint generator therefore coexists with a positive-Newman-time collision. No new numerical test is needed. The witness fails canonical theta arithmetic, which has supplied the initial profile but has not entered a new signed estimate.

## 7. Decision and continuation boundary

Prefer Candidate B for the author's Hamiltonian/geometric question. Candidate A remains a valid narrowly scoped alternative if retaining G itself is the priority. The only local clarification was the energy-origin/absolute-amplitude payment in §4. No third mechanism, new interaction family, count problem or auxiliary conditioning problem was opened.

The [proposed E01 r1][request] freezes Candidate B's proof route and six acceptance obligations. **Next: [E] TND-O-E01 — Sol**, after the author selects this route in discussion. It is ready as a contract, unissued/unactivated as work. E02 remains reserved. If the author instead requires a theta source derived intrinsically from the unmodified cylinder, the precise missing premise is a preparation/observation law that supplies the canonical arithmetic profile without prescribing it; this comparison has not furnished that law.

This analysis follows the [result index][results], [theta bookkeeping][theta] and [patterns index][avoid], especially [used control premises][a02], [re-realizations][a03] and [scoped exclusions][a07]. No investigation closes, manuscript milestone, global result-summary promotion, independent specialist review or formal verification is claimed. The [model-change continuation][continuation] preserves the same boundary.

[parent]: ../../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md
[review]: ../../reviews/01_TND_E03_R2_GEOMETRY_SOURCE_AND_TRANSPORT_ASSESSMENT_20261106.md
[witness]: ../../01_direct_newman_realization/notes/04_TND_D_B02_COLLISION_DYNAMICS_RECONNAISSANCE_20261106.md
[decision]: ../brainstorm/notes/01_TND_O_B01_TWO_REALIZATION_DECISION_20261106.md
[request]: ../research-progress/handoffs/03_TND_O_E01_R1_PROPOSED_REQUEST_20261106.md
[progress]: ../research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md
[continuation]: 03_TND_O_B01_CONTINUATION_AND_MODEL_CHANGE_20261106.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
