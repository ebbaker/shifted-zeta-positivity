# Log-temperature insertions and second-quantized source states

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance: **gpt-6-astra (Codex), recorded effort xhigh**. Chat `01a1a455-6c1d-7aa2-9723-43ab36704924`, turn `01a1a6ec-040d-7bc3-ba78-55f62698542b`; Mellin-curvature history **0004**.

**Subsequent fixed-temperature direction:** [Note05](05_FIXED_TEMPERATURE_DETERMINANT_AND_RADIAL_GREEN_20261104.md) follows the author’s correction: u remains a thermodynamic parameter, and physical creation operators act on spatial box modes. The psi(u) construction below remains an auxiliary encoding, not the selected physical model. Note05 also examines the fixed-temperature integrand and the Investigation05 radial Green identity.

**Author direction.** Explain the physical meaning of the orbital definitions instead of assigning them suggestive names. Use creation and annihilation operators and second-quantized notation for subsequent discussion. Keep the equilibrium density matrix and its equivalent TFD description, with the source factors in observable insertions. This clarifies [Note03](03_EQUILIBRIUM_PICTURES_AND_FERMION_NUMBER_20261104.md); it does not select a new Hamiltonian or justify a new physical degree of freedom.

**Correction of terminology and scope.** “Thermal-response polynomials” in Notes02–03 was descriptive shorthand, not a standard named family or an independently established physical interpretation. The P_l are the energy-insertion polynomials produced by logarithmic inverse-temperature differentiation of a particular unnormalized trace. The source orbitals a_i and b_j reproduce the requested pairings, but have not been derived as eigenmodes or physically distinguished preparations of the theta-spectrum Hamiltonian. In particular treating u as a wavefunction coordinate is an extra model choice when u initially labels inverse temperature. These are exact algebraic and thermodynamic identities with same-assistant derivation checks, not a new sign estimate or an independent review.

## 1. Define the physical energy-mode operators first

Let the fermionic mode operators satisfy
\[
\{\hat d_n,\hat d_m^\dagger\}=\delta_{nm},\qquad
\{\hat d_n,\hat d_m\}=\{\hat d_n^\dagger,\hat d_m^\dagger\}=0.
\]
Take
\[
\hat H_0=\sum_{n\ge1}E_n\hat d_n^\dagger\hat d_n,
\qquad E_n=\pi n^2,\qquad
\hat N_E=\sum_n\hat d_n^\dagger\hat d_n.
\tag{1}
\]
The geometric realization may be a Dirichlet particle on an interval. Its spatial coordinate is not identified with u by these equations. Denote the projector onto N_E = 1 by Pi_1. The partition function in the primitive is
\[
Q(\beta)=\operatorname{Tr}_{N_E=1}e^{-\beta\hat H_0}
=\sum_n e^{-\beta E_n},\qquad
\rho_{\beta,1}=\frac{\Pi_1e^{-\beta\hat H_0}}{Q(\beta)}.
\tag{2}
\]
The full Fock-space grand partition function would instead be a product over modes. The restriction in (2) is required by the literal primitive, not a claim that the eventual determinant model has only one particle.

Define the normal-ordered one-body insertion
\[
\hat{\mathcal P}_l(\beta)
=\sum_n P_l(\beta E_n)\hat d_n^\dagger\hat d_n.
\tag{3}
\]
On N_E = 1 it equals P_l(beta H_0). With beta = exp(4u),
\[
p(u)=e^uQ(\beta),\qquad
\Phi(u)=e^u\operatorname{Tr}_{N_E=1}
\left[\hat{\mathcal P}_0(\beta)e^{-\beta\hat H_0}\right],
\quad P_0(x)=2x^2-3x.
\tag{4}
\]
The density matrix and TFD are interchangeable in this expression. With separate left and auxiliary Fock factors, the TFD is
\[
|T_{\beta,1}\rangle=Q(\beta)^{-1/2}
\sum_n e^{-\beta E_n/2}
(\hat d_{n,L}^\dagger|0\rangle_L)\otimes
(\hat{\widetilde d}_{n,R}^\dagger|0\rangle_R).
\]
The explicit tensor convention avoids any implicit ordering convention between odd left and right operators. For the even left insertions at issue,
\(\operatorname{Tr}(\rho_{\beta,1}\hat{\mathcal P}_l)
=\langle T_{\beta,1}|\hat{\mathcal P}_{l,L}|T_{\beta,1}\rangle\).
The [checked Baker reference](../references/01_BAKER_THERMOFIELD_2020.md), equations (2.1)–(2.4), supplies this equivalence. No filtered equilibrium state is used.

## 2. Derive the polynomials from the operation they represent

At fixed energy E, put x = beta E. Since dx/du = 4x,
\[
\frac{d}{du}\left[e^u P_l(x)e^{-x}\right]
=e^u\left[4xP_l'(x)+(1-4x)P_l(x)\right]e^{-x}.
\tag{5}
\]
The three terms have distinct origins: differentiation of the insertion, differentiation of the theta prefactor e^u, and differentiation of the Boltzmann factor. Thus define
\[
P_{l+1}(x)=4xP_l'(x)+(1-4x)P_l(x).
\tag{6}
\]
It follows that
\[
\boxed{\Phi^{(l)}(u)=e^u\operatorname{Tr}_{N_E=1}
\left[\hat{\mathcal P}_l(\beta)e^{-\beta\hat H_0}\right].}
\tag{7}
\]
For example
\[
P_1(x)=-8x^3+30x^2-15x,
\qquad P_2(x)=32x^4-224x^3+330x^2-75x.
\]
The ordinary thermodynamic starting point is
\(\partial_\beta e^{-\beta\hat H_0}=-\hat H_0e^{-\beta\hat H_0}\).
Changing inverse temperature inserts energy. Equation (5) records the additional chain rule and explicit dependence specific to this theta observable. The index l counts derivatives of the inserted trace; it is neither a particle number nor an energy-level label. Temperature variation is not asserted to be a real-time evolution.

P_0 itself is fixed by the source reconstruction
\(\Phi=(\partial_u^2-1)p/8\). Indeed, on each mode,
\[
\frac18(\partial_u^2-1)[e^ue^{-x}]
=e^u(2x^2-3x)e^{-x}.
\tag{8}
\]
This identifies the exact observable needed for the source; it does not yet derive that observable from an independent mechanical coupling or symmetry principle.

Normalized thermal response is different. For a beta-dependent spectral observable O(beta),
\[
\frac{d}{d\beta}\langle O\rangle_{\beta,1}
=\langle\partial_\beta O\rangle_{\beta,1}
-\operatorname{Cov}_{\beta,1}(O,\hat H_0).
\tag{9}
\]
Equation (9) follows by differentiating both the trace numerator and Q. It explains why calling P_l simply “susceptibility polynomials” would be misleading: normalization and connected correlations are not included in that name. “Energy-insertion polynomials for logarithmic temperature derivatives” states their role more precisely. The [MC01 thermal source dictionary](../../01_circle_thermal_trace/notes/01_THERMAL_SOURCE_IDENTITY_RETURN_20261101.md) already derives the recurrence; no novelty is claimed for it.

## 3. What the orbital definitions actually choose

Let
\[
q_i(u)=\operatorname{Tr}[\rho_{\beta,1}\hat{\mathcal P}_{2i}(\beta)],
\quad a_i(u)=\sqrt{p(u)}q_i(u),\quad
b_j(u)=\frac{u^{2j}}{(2j)!}\sqrt{p(u)}.
\tag{10}
\]
By (7), a_i = Phi^(2i)/sqrt(p). The motivations and remaining choices are:

1. q_i is an equilibrium expectation with a precisely defined logarithmic-temperature derivative origin. This is a thermal statement about the energy modes in (1).
2. The powers u^(2j)/(2j)! select even moment coefficients. If a probe couples to U, the generating profile cosh(z u)sqrt(p(u)) has exactly these coefficients:
   \[
   \cosh(zu)\sqrt{p(u)}=\sum_{j\ge0}z^{2j}b_j(u).
   \tag{11}
   \]
   This is a moment/source expansion. A real exponential probe is not automatically a normalized or unitary preparation. With z imaginary it is the corresponding even Fourier probe.
3. Choosing sqrt(p) as a common scalar wavefunction envelope and regarding u as a one-particle coordinate are additional encoding choices. Equilibrium mechanics specifies a family rho_{beta,1}; it does not by itself make temperature a quantum coordinate or specify a coherent amplitude over different temperatures.

The moment pairing motivates the formulas mathematically:
\[
\langle a_i,b_j\rangle
=\int_0^\infty\Phi^{(2i)}(u)\frac{u^{2j}}{(2j)!}du=c_{j-i}.
\tag{12}
\]
It does not establish a dynamical state-preparation mechanism. More generally any positive envelope w for which the resulting functions are square integrable gives the same pairing with a_i = Phi^(2i)/w and b_j = u^(2j)w/(2j)!. The primitive selects a useful thermodynamic envelope, but the overlap identity alone cannot establish that it is uniquely physical. These are reciprocal rescalings, not unitary transformations preserving the separate Gram matrices.

All finite-order integrals above are controlled by the complete source's smooth endpoint and double-exponential tail. Integration by parts uses full theta reflection; it is not performed on a single thermal mode.

## 4. Creation and annihilation operators for the exact source encoding

If this source-coordinate encoding is used, define a canonical fermionic field
\[
\{\hat\psi(u),\hat\psi^\dagger(v)\}=\delta(u-v),\qquad
\{\hat\psi(u),\hat\psi(v)\}=0,
\quad\hat\psi(u)|0\rangle_u=0.
\tag{13}
\]
The fields are operator-valued distributions; the square-integrable profiles in (10) define the well-defined smeared creation operators
\[
\hat A_i^\dagger=\int_0^\infty a_i(u)\hat\psi^\dagger(u)du,
\qquad
\hat B_j^\dagger=\int_0^\infty b_j(u)\hat\psi^\dagger(u)du.
\tag{14}
\]
Annihilation operators use conjugate profiles. The CAR give
\[
\boxed{\{\hat A_i,\hat B_j^\dagger\}=c_{j-i}I.}
\tag{15}
\]
These smeared operators are not asserted to be separate orthonormal canonical modes: their same-family anticommutators are the corresponding Gram matrices, not delta_ij. The underlying psi field is canonical.

Define
\[
|A_r\rangle=\hat A_0^\dagger\cdots\hat A_{r-1}^\dagger|0\rangle_u,
\qquad
|B_{r,k}\rangle=\hat B_k^\dagger\cdots\hat B_{k+r-1}^\dagger|0\rangle_u.
\tag{16}
\]
Then, with the displayed operator order,
\[
\boxed{
D_{r,k}=\langle0|\hat A_{r-1}\cdots\hat A_0
\hat B_k^\dagger\cdots\hat B_{k+r-1}^\dagger|0\rangle_u
=\langle A_r|B_{r,k}\rangle.}
\tag{17}
\]
The determinant follows by successively anticommuting annihilators through the creators and using (15). No additional r! occurs. The source number operator
\(\hat N_u=\int\hat\psi^\dagger(u)\hat\psi(u)du\)
counts r particles in each state (16). Thus r is an exact particle count for this encoding. Physical identification with the energy-mode particles of (1) remains additional work.

The moment preparation has a compact second-quantized generating form:
\[
\hat B^\dagger(z)=\int_0^\infty\cosh(zu)\sqrt{p(u)}\hat\psi^\dagger(u)du
=\sum_{j\ge0}z^{2j}\hat B_j^\dagger.
\tag{18}
\]
For real z, the profiles are square integrable by the tail. The complete source gives
\(\langle0|\hat A_i\hat B^\dagger(z)|0\rangle_u
=z^{2i}\int_0^\infty\Phi(u)\cosh(zu)du\).
This connects the two operator families to derivative and moment probes, while still leaving their physical preparation to be derived.

## 5. The many-particle observable must be specified explicitly

There is a genuine choice when extending P_0 from one particle to r particles. The one-body insertion is
\[
\hat{\mathcal P}_0(\beta)
=2\beta^2\sum_nE_n^2\hat n_n-3\beta\hat H_0,
\qquad \hat n_n=\hat d_n^\dagger\hat d_n.
\]
A polynomial of total energy instead gives
\[
P_0(\beta\hat H_0)
=\hat{\mathcal P}_0(\beta)
+4\beta^2\sum_{n<m}E_nE_m\hat n_n\hat n_m.
\tag{19}
\]
The equality uses n_n^2 = n_n. These coincide on N_E = 1 and differ at higher particle number. The additional term is a two-body observable, whether or not it is chosen as an interaction in a Hamiltonian. Differentiating the fixed-r partition trace of exp(-beta H_0) inserts powers of total H_0; it cannot silently be identified with the second quantization of the one-particle polynomial. Neither choice is selected just by the primitive identity.

If the physical energy modes are kept as the starting point, a source preparation would ultimately require coefficients in expressions of the form
\(\hat A_i^\dagger=\sum_n A_{in}\hat d_n^\dagger\),
\(\hat B_j^\dagger=\sum_n B_{jn}\hat d_n^\dagger\),
or specified many-body operators. Those coefficients must come from a geometry, coupling, probe or state-preparation rule. An arbitrary identification of Hilbert spaces would preserve algebra but supply no physical selection. The nonorthogonal profiles a_i,b_j cannot simply be assigned distinct eigenenergies.

**Next conceptual focus:** start from the canonical energy modes (1), keep u as the thermal/source parameter unless a physical coordinate role is supplied, and investigate how derivative and moment probes are represented in that one Fock system. Equations (14)–(17) give the exact second-quantized source encoding to be matched. They are not yet the sought energy expectation of a selected Hamiltonian.

## 6. Evidence and control scope

This is a clarification of terminology, operator definitions and physical obligations, not a proposed positivity mechanism. The [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md), especially [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [circular definitions](../../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md), and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), retain their role.

The control premise screen in Notes02–03 is unchanged: CAR and reciprocal envelope rescalings do not distinguish canonical theta from other suitable smooth sources; weighted square controls share thermal insertion identities while failing unchanged weights/full reflection; Euler-factor and reflected shape controls fail the literal unit-weight square-spectrum reconstruction. No control is newly excluded, no r-particle sign is inferred from state positivity, and no numerical campaign is needed to establish the algebra above. The next gain would be a physically selected correspondence or an additional estimate, not a more suggestive name for these states.
