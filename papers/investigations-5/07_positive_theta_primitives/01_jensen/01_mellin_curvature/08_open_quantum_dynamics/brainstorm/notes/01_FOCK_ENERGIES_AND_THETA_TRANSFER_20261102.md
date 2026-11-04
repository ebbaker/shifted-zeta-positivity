# MC08-B03: Fock-state energies and the theta transfer

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **max**; chat `01a19f55-b2e6-75f0-a465-ad11ad5d5488`, turn `01a19f57-dc7c-7901-a6d1-30b1e21e30db`. This new conversation is brainstorm history **0001**, distinct from the existing branch history 0003.

**Scope:** the author requests an explanation of energy, Fock states and the transfer before discussing the outstanding signed estimate. This note supplies that explanation. It follows the [continuation manuscript](../../manuscript/main.tex), especially Sections 2–4, 6 and 9, and [Handoff06](../../research-progress/handoffs/06_MC08_MANUSCRIPT_AND_NEXT_SESSION_20261102.md). The zero-diagonal observation and two-site example below are direct explanatory deductions from the displayed generator, with same-assistant algebraic checking only. They are not an independently reviewed research result. B03 mechanism selection and the separate E04 check remain pending.

## 1. A Fock space needs a Hamiltonian before states have energies

Given a one-particle Hilbert space h, the fermionic Fock space is
\[
\mathcal F_-(h)=\mathbb C\Omega\oplus h\oplus\wedge^2 h\oplus\cdots.
\]
It organizes states by particle number and imposes antisymmetry. It does not assign energy by itself. An orthonormal mode basis gives occupation states
\[
|J\rangle=b_{m_1}^\dagger\cdots b_{m_r}^\dagger\Omega,
\qquad m_1<\cdots<m_r.
\]
Each mode is occupied zero or one times. Specify a self-adjoint one-particle Hamiltonian h_1. For the noninteracting models here the many-particle Hamiltonian is its additive lift
\[
\mathbb H=d\Gamma(h_1)=\sum_{a,b}(h_1)_{ab}b_a^\dagger b_b.
\]
On the r-particle sector this applies h_1 to each particle and sums the results. Normal ordering fixes the vacuum energy to zero. If the chosen modes diagonalize h_1, with energies epsilon_m, then
\[
\mathbb H|J\rangle=E_J|J\rangle,
\qquad E_J=\sum_{m\in J}\epsilon_m.
\]
If they do not diagonalize h_1, an occupation state generally has an energy distribution, rather than one definite energy. For a normalized finite superposition of energy eigenstates, psi=sum_J C_J |J>, the mean energy is sum_J |C_J|^2 E_J. For a mixed state it is Tr(rho H), when finite.

Two different Hamiltonians and two different sets of fermion modes occur in this manuscript. Abstract Hilbert-space isomorphism does not by itself identify their operators or observables.

## 2. The theta source supplies ordinary square energies

For the periodic circle coordinate x in [0,2pi),
\[
L=-\pi\partial_x^2,\qquad L\frac{e^{imx}}{\sqrt{2\pi}}
=\pi m^2\frac{e^{imx}}{\sqrt{2\pi}}.
\]
The source uses one representative of each nonzero +/-m pair, equivalently the positive-momentum subspace m>=1. Its one-particle energies are
\[
E_m=\pi m^2=\pi,4\pi,9\pi,16\pi,\ldots.
\]
These are the canonical mathematical units of the theta exponent. The full circle has a zero mode and twofold nonzero degeneracy; the reduced trace removes them as specified below.

With energy-mode fermions b_m, define
\[
\mathbb H_\theta=d\Gamma(L_+)=\sum_{m\ge1}\pi m^2 b_m^\dagger b_m.
\]
Here the occupation basis really is an energy eigenbasis:

| Occupied positive energy modes | Energy |
| --- | --- |
| none (vacuum Omega) | 0 |
| {1} | pi |
| {2} | 4pi |
| {1,2} | 5pi |
| {1,3} | 10pi |
| {1,2,3} | 14pi |

There is no state with two fermions in the same retained mode. Particle number alone does not determine energy: {1,2} and {1,3} both contain two particles. The lowest energy at fixed particle number r is pi r(r+1)(2r+1)/6, by filling modes 1 through r. The vacuum is the global ground state of this nonnegative Hamiltonian.

On the infinite Fock space the operator domain consists of expansions with sum_J E_J^2 |C_J|^2 finite; finite mean energy requires the weaker sum_J E_J |C_J|^2 finite. All finite occupation examples lie in the operator domain.

The thermal amplitude operator is diagonal:
\[
e^{-\beta\mathbb H_\theta}=\Gamma(e^{-\beta L_+}),\qquad
 e^{-\beta\mathbb H_\theta}|J\rangle=e^{-\beta E_J}|J\rangle.
\]
This is imaginary-time/thermal evolution, while real-time closed evolution would multiply |J> by exp(-it E_J), with hbar=1. A Boltzmann weight is an ensemble weight before normalization; it is not a probability for changing one energy mode into another.

## 3. How these energies enter the source

The [DLMF defining theta series, 20.2.3](https://dlmf.nist.gov/20.2.E3), reinspected on this turn at z=0 and q=exp(-pi beta), gives the same complete square-spectrum sum as the manuscript. In its normalization,
\[
Q(\beta)=\sum_{m\ge1}e^{-\beta E_m}
=\tfrac12(\operatorname{Tr}e^{-\beta L}-1),
\qquad \beta=e^{4u},\qquad p(u)=e^uQ(\beta).
\]
The subtraction removes the zero mode; the factor one half removes the +/-m multiplicity. Q is a one-particle trace. If one introduces all fermionic particle numbers, then
\[
\Xi(\beta,z)=\operatorname{Tr}_{\mathcal F_-}
 [z^{\mathcal N}e^{-\beta\mathbb H_\theta}]
=\prod_{m\ge1}(1+ze^{-\beta E_m}),\qquad [z]\Xi=Q.
\]
Thus the primitive uses the coefficient of z, not the whole grand partition function. z is a particle-number fugacity here and is distinct from transfer activity v.

The source Phi=(p''-p)/8 inserts an energy polynomial:
\[
\Phi(u)=e^u\sum_{m\ge1}P_0(\beta E_m)e^{-\beta E_m},
\qquad P_0(x)=2x^2-3x.
\]
On u>=0, beta E_m>=pi, so this filter is positive. The normalized state is
\[
\rho_u(m)=\frac{P_0(\beta E_m)e^{-\beta E_m}}
 {\sum_{n\ge1}P_0(\beta E_n)e^{-\beta E_n}}.
\]
It is a one-particle filtered thermal mixture. Its mean underlying energy is sum_m rho_u(m) E_m. Changing u changes its weights and its temperature-dependent filter; it does not change the fixed eigenvalues E_m. No positive-filter claim is made for all beta>0.

The [reviewed MC01 dictionary](../../../01_circle_thermal_trace/notes/01_THERMAL_SOURCE_IDENTITY_RETURN_20261101.md) explains the original continuum orbitals in L2((0,infinity),du):
\[
f_i=\Phi^{(2i)}/\sqrt\Phi,
\qquad g_j=u^{2j}\sqrt\Phi/(2j)!,
\qquad \langle f_i,g_j\rangle=c_{j-i}.
\]
Their labels specify derivatives and moments. They are not orthonormal energy modes. With
\[
P_{n+1}(x)=4xP_n'(x)+(1-4x)P_n(x),
\]
the exact connection is
\[
f_i(u)=\sqrt{\Phi(u)}\,
\mathbb E_{\rho_u}[P_{2i}(\beta E_m)/P_0(\beta E_m)].
\]
Every f_i therefore contains the full energy spectrum. The integer i selects an observable averaged over energy, while m labels an energy eigenstate. The orbitals are functions of source coordinate u, distinct from circle wavefunctions of x. Their exterior products are legitimate fermionic states after normalization, but the manuscript assigns no separate Hamiltonian on their continuum orbital space.

## 4. The coefficient transfer acts on another set of modes

The discrete transfer space is h_c=ell2(N0), with orthonormal coefficient sites |j>_c and creators a_j^dagger. The one-particle state |0>_c is an occupied site, not the empty Fock vacuum Omega. Define
\[
c_n=\frac{1}{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,
\quad F(w)=\sum_{n\ge0}c_nw^n,
\quad S|j\rangle_c=|j-1\rangle_c\ (j\ge1),\quad S|0\rangle_c=0.
\]
The coefficients c_n combine all energies and source coordinates. They are not single-level Boltzmann weights. The exact normalized transfer is
\[
K_v=F(vS)/F(v),\qquad
K_v|j\rangle_c=\frac1{F(v)}\sum_{n=0}^j c_nv^n|j-n\rangle_c.
\]
It moves amplitude among coefficient sites, and the complete denominator F(v) fixes its normalization. It is a contraction for v>=0, with K_0=I. Its Fock lift
\[
\Gamma(K_v)=\bigoplus_{r\ge0}\wedge^rK_v
\]
preserves particle number and has vacuum block +1. It applies K_v to each occupied orbital and antisymmetrizes. The result is usually a superposition of occupation patterns. Exterior antisymmetry automatically removes repeated-mode occupations and produces determinant amplitudes.

For increasing occupation lists I,J of length r and v>0,
\[
\langle I|\Gamma(K_v)|J\rangle
=\frac{v^{\sum J-\sum I}}{F(v)^r}\det[c_{j_b-i_a}].
\]
For I=(0,...,r-1), J=(k,...,k+r-1), this is v^(rk) D_(r,k)/F(v)^r. This is how the original coefficient determinants occur as physical amplitudes. Squaring would instead give a probability and remove the amplitude's sign; the manuscript's coherent reference measurement recovers the signed amplitude with its success normalization.

The diagram of dependencies is: square energies -> filtered source Phi -> moments c_n -> F and K_v -> fermionic determinant amplitudes. This is a construction from the source data, not a stated unitary identification of the energy modes b_m and coefficient-site modes a_j.

## 5. The energy operator in the MC08 dynamical model

The manuscript realizes the transfer as evolution conditioned on no particle-loss count. On 0<=v<=1/25,
\[
G(v)=K'_vK_v^{-1},\quad
H(v)=\tfrac i2(G-G^\dagger),\quad
\mathsf R(v)=-(G+G^\dagger)\ge0,
\qquad G=-iH-\mathsf R/2.
\]
Here v is the chosen evolution clock, distinct from inverse temperature beta and source coordinate u. With this clock and hbar=1, the system energy observable is
\[
\mathbb H_{\rm MC08}(v)=d\Gamma(H(v))
=\sum_{i,j}H_{ij}(v)a_i^\dagger a_j.
\]
The normal-ordered vacuum has energy zero. The unnormalized no-count state obeys
\[
\partial_v\psi=d\Gamma(G)\psi
=(-i\mathbb H_{\rm MC08}-\tfrac12d\Gamma(\mathsf R))\psi,
\qquad \psi(v)=\Gamma(K_v)\psi(0).
\]
The squared norm is its no-count probability. At finite cutoff, jumps L_mu=sum_j (sqrt R)_(mu j) a_j remove one particle. The coherent Hamiltonian and no-count transfer preserve number; the full loss channel can decrease it. Loss of particles is not by itself an assertion of decreasing expectation of H(v) or equilibration at theta temperature beta.

To assign definite instantaneous energies in a finite-mode model, diagonalize H_N(v). If its eigenvalues are epsilon_alpha(v), occupations of its orthonormal eigenmodes have summed energies sum epsilon_alpha(v). The coefficient-site occupation states generally are not those eigenstates. The infinite-mode operator remains self-adjoint, but an orthonormal discrete energy eigenbasis is not presumed; the spectral theorem supplies the general definition. On each fixed r sector dGamma(H) is bounded; no uniform full-Fock boundedness is inferred.

There is a useful direct deduction. Since all theta coefficients are real,
\[
G(v)=\sum_{n\ge1}\alpha_n(v)(S^n-I),\qquad
H(v)=\frac i2\sum_{n\ge1}\alpha_n(v)(S^n-(S^\dagger)^n),
\]
where alpha_n=n lambda_n v^(n-1) and log(F(w)/c_0)=sum lambda_n w^n. The Hamiltonian has zero diagonal in the coefficient basis. Therefore, for every finite coefficient-site occupation state,
\[
\langle J|\mathbb H_{\rm MC08}(v)|J\rangle
=\sum_{j\in J}H_{jj}(v)=0.
\]
This is zero mean energy, not a statement that every occupation state is a zero-energy eigenstate. Coherences matter.

For an explicit illustration take the finite two-site model N=1 at v=0. Put alpha=c_1/c_0>0. Then
\[
H_1(0)=\frac\alpha2\begin{pmatrix}0&i\\-i&0\end{pmatrix},\qquad
|+\rangle=\frac{|0\rangle_c-i|1\rangle_c}{\sqrt2},\quad
|-\rangle=\frac{|0\rangle_c+i|1\rangle_c}{\sqrt2},
\]
with energies +alpha/2 and -alpha/2 respectively. Each site state gives these two outcomes with equal probabilities and has mean zero and variance alpha^2/4. In its four-dimensional Fock space the vacuum and doubly occupied state have energy zero, while the two one-particle energy modes have the two opposite energies. Thus the vacuum's normal-ordering reference zero is not a ground-state assertion for this Hamiltonian. This example is the finite model, not an invariant spectral block of the infinite H.

K_v itself is generally non-Hermitian and cannot be read as exp(-beta L_+) or exp(-beta H) for a self-adjoint Hamiltonian. The two-site transfer already has a nontrivial Jordan block. Its physical meaning here is a conditioned amplitude evolution combining H and loss; the ordinary theta heat operator is diagonal in its energy basis. These are the manuscript's two distinct uses of operator evolution.

## 6. Provenance and continuation boundary

The source/filter/response identities retain [MC01's separate cross-model internal review](../../../01_circle_thermal_trace/reviews/01_MC01_E01_SEPARATE_REVIEW_20261101.md). The MC08 local loss construction retains its [separate same-model assessment](../../reviews/02_OPEN_QUANTUM_DYNAMICS_ASSESSMENT_20261102.md). Neither is specialist human validation. This note is exposition and the simple deductions explicitly identified above, with no new signed estimate or selected mechanism. The current request deliberately stops before evaluating proposals for B03.

Read with [result summaries](../../../../../../../../result-summaries/README.md), especially [theta identities and bookkeeping](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and [patterns to avoid](../../../../../../../../avoid/README.md), especially [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [normalization and endpoint conventions](../../../../../../../../avoid/08_normalization_and_constant_slips.md). These links record inherited scope; this explanation does not promote a representation into an estimate.

The sole task status stays in the [MC08 register](../../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md). This conversation's public history is maintained under [brainstorm/chat-histories](../chat-histories/README.md); no earlier chat is moved, renumbered or reused. No manuscript milestone, numerical campaign or new execution packet is created by this explanation.
