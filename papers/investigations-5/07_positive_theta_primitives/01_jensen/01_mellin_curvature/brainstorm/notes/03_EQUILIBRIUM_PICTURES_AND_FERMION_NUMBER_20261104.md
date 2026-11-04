# Equilibrium pictures and fermion number

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance: **gpt-6-astra (Codex), recorded effort xhigh**. Chat `01a1a455-6c1d-7aa2-9723-43ab36704924`, turn `01a1a6df-8a6e-77f1-b776-b0d8d2b015d0`; Mellin-curvature history **0004**.

**Subsequent motivation and notation clarification:** [Note04](04_LOG_TEMPERATURE_INSERTIONS_AND_SECOND_QUANTIZATION_20261104.md) derives the P_l as logarithmic-temperature derivative insertions, identifies the remaining physical assumptions in the source orbitals, and adopts creation/annihilation notation. The phrase “thermal-response polynomials” was descriptive shorthand, not a standard physical classification.

**Author direction.** Keep the original equilibrium density matrix and its thermofield purification as equivalent descriptions, with the polynomial energy factors in the observables. The author's reference to equation (2.3) illustrates how to obtain the primitive; it does not select purification over density matrices or ask for a different equilibrium ensemble. Interpret determinant order r through many-particle states, rather than treating r independently replicated thermal systems as the preferred physical picture.

This revises the preferred presentation of [Note02](02_THERMOFIELD_SOURCE_STATES_AND_ENERGY_EXPECTATIONS_20261103.md). Its filtered-state and product-copy identities remain algebraically valid, but are not the modeling direction selected by the author. This note records exact identities and the remaining identification question, not a new positivity estimate, a new Hamiltonian, or a new investigation launch. Checking is by the same assistant; no independent review or numerical experiment is claimed.

## 1. One equilibrium state, two descriptions

Let h have the simple spectrum E_n = pi n^2, n >= 1. For beta > 0,
\[
Q(\beta)=\operatorname{Tr}e^{-\beta h},\qquad
\rho_\beta=Q(\beta)^{-1}e^{-\beta h},
\]
\[
|T_\beta\rangle=Q(\beta)^{-1/2}
\sum_n e^{-\beta E_n/2}|n,\bar n\rangle,
\quad
\operatorname{Tr}(\rho_\beta O)
=\langle T_\beta|O_L|T_\beta\rangle.
\tag{1}
\]
This is the density-matrix/TFD equivalence in Baker's [equations (2.1)–(2.4)](https://arxiv.org/pdf/2001.02713v1#page=3), previously checked in the [reference record](../references/01_BAKER_THERMOFIELD_2020.md). The right copy purifies the state; it is not a further physical particle or an independently prepared ensemble.

With beta = exp(4u), the complete primitive and source are
\[
p(u)=e^uQ(\beta),\qquad
\Phi(u)=p(u)\operatorname{Tr}[\rho_\beta P_0(\beta h)]
=p(u)\langle T_\beta|P_0(\beta h_L)|T_\beta\rangle,
\quad P_0(x)=2x^2-3x.
\tag{2}
\]
Equivalently p is the squared norm of the unnormalized vector
\(e^{u/2}\sum_n e^{-\beta E_n/2}|n,\bar n\rangle\).
The normalized density matrix alone does not retain the partition-function normalization Q; Q is kept explicitly in (2). No filtered density matrix is introduced.

For the inherited recurrence
\[
P_{\ell+1}(x)=4xP_\ell'(x)+(1-4x)P_\ell(x),
\]
define the scalar responses
\[
q_i(u)=\operatorname{Tr}[\rho_{e^{4u}}P_{2i}(e^{4u}h)]
=\langle T_{e^{4u}}|P_{2i}(e^{4u}h_L)|T_{e^{4u}}\rangle.
\tag{3}
\]
Then \(\Phi^{(2i)}(u)=p(u)q_i(u)\). The full response polynomial includes differentiation of all thermal weights and prefactors. No differentiation of a normalized state is silently identified with multiplication by P_{2i}.

## 2. An unfiltered choice of source orbitals

In the original one-particle source Hilbert space \(\mathcal H_u=L^2((0,\infty),du)\), set
\[
a_i(u)=\sqrt{p(u)}q_i(u)=\frac{\Phi^{(2i)}(u)}{\sqrt{p(u)}},
\qquad
b_j(u)=\frac{u^{2j}}{(2j)!}\sqrt{p(u)}.
\tag{4}
\]
The density matrix and TFD used to compute q_i remain the original equilibrium ones. The common wavefunction envelope is sqrt(p); P_0 and all higher responses remain observables evaluated in that state. In particular a_0 and b_0 differ.

These are reciprocal reweightings of the original source states:
\[
a_i=\sqrt{\Phi/p}\,f_i,\qquad
b_j=\sqrt{p/\Phi}\,g_j.
\]
Therefore, using complete-source integration by parts,
\[
\boxed{\langle a_i,b_j\rangle
=\int_0^\infty\frac{u^{2j}}{(2j)!}\Phi^{(2i)}(u)du
=c_{j-i}.}
\tag{5}
\]
This preserves the mixed pairings and their determinants, not the separate Gram matrices. No unitary equivalence of the two pairs of orbital families is asserted. At each finite index the new orbitals are square integrable: p is positive and smooth at the origin; source responses grow at most polynomially in exp(4u) relative to p in the tail, while p decays double exponentially. All endpoint cancellations in (5) still use the complete source Phi, not an individual mode.

## 3. r is exactly the fermion number of the source Slater states

For the rectangular determinant, use zero-based indices:
\[
D_{r,k}=\det[c_{k+b-a}]_{a,b=0}^{r-1}.
\]
Define vectors in the r-particle sector \(\bigwedge^r\mathcal H_u\):
\[
|A_r\rangle=a_0\wedge\cdots\wedge a_{r-1},\qquad
|B_{r,k}\rangle=b_k\wedge\cdots\wedge b_{k+r-1}.
\tag{6}
\]
Then
\[
\boxed{D_{r,k}=\langle A_r|B_{r,k}\rangle,\qquad
\widehat N A_r=rA_r,\quad\widehat N B_{r,k}=rB_{r,k}.}
\tag{7}
\]
Thus r has an exact particle-number interpretation here, beyond an analogy. The states are generally unnormalized; division by their two actual Gram norms gives a normalized transition amplitude. The original f/g wedges give the same unnormalized determinant and the same particle number.

In creation-operator language,
\[
|A_r\rangle=\hat a^\dagger(a_0)\cdots\hat a^\dagger(a_{r-1})|0\rangle,
\quad
|B_{r,k}\rangle=\hat a^\dagger(b_k)\cdots\hat a^\dagger(b_{k+r-1})|0\rangle.
\]
The canonical anticommutation relations produce the determinant in (7). Its exchange signs are those of identical fermions. The r coordinate slots in a first-quantized wavefunction describe r particles; they do not label r independently prepared experiments. Antisymmetrization of a product of one identical orbital would vanish for r > 1; the distinct orbitals in (6) are essential.

For example, with the convention giving unit-norm wedges of orthonormal orbitals,
\[
B_{r,k}(u_1,\ldots,u_r)
=\frac{\prod_{\ell=1}^r\sqrt{p(u_\ell)}}{\sqrt{r!}}
\det_{b,\ell}\left[\frac{u_\ell^{2(k+b)}}{(2k+2b)!}\right].
\tag{8}
\]
The determinant is a positive constant times
\(\prod_\ell u_\ell^{2k}\prod_{\ell<m}(u_m^2-u_\ell^2)\).
This explicitly displays the Pauli nodes at coincident source coordinates. Equation (8), rather than a product of r copies of the same pure state, is the appropriate wavefunction for this particle interpretation.

## 4. Equilibrium for r particles and its thermofield description

If h is the physical one-particle Hamiltonian, its free fermionic extension is
\[
H_r=d\Gamma(h)|_{\wedge^r\mathcal H_E}
=\left.\sum_{\ell=1}^r h_\ell\right|_{\wedge^r\mathcal H_E}.
\tag{9}
\]
The fixed-particle-number density matrix and its equivalent TFD are
\[
\rho_{\beta,r}=Z_r(\beta)^{-1}e^{-\beta H_r},\quad
Z_r(\beta)=\sum_{n_1<\cdots<n_r}
e^{-\beta(E_{n_1}+\cdots+E_{n_r})},
\tag{10}
\]
\[
|T_{\beta,r}\rangle=
\frac1{\sqrt{Z_r(\beta)}}\sum_{n_1<\cdots<n_r}
e^{-\beta(E_{n_1}+\cdots+E_{n_r})/2}
|n_1\wedge\cdots\wedge n_r\rangle_L
|\overline{n_1\wedge\cdots\wedge n_r}\rangle_R.
\tag{11}
\]
This doubles the entire r-particle sector for purification. Physical particle number is r, read on the left sector. The same trace/TFD identity (1) holds with rho_{beta,r} and T_{beta,r}. Interactions can replace the free H_r once specified; equation (1) still applies with its many-body eigenbasis.

Exchange distinguishes this ensemble from independent copies: for instance
\[
Z_1(\beta)=Q(\beta),\qquad
Z_2(\beta)=\tfrac12[Q(\beta)^2-Q(2\beta)].
\tag{12}
\]
This follows by removing equal indices from the double sum and dividing by the two orderings. The primitive remains e^u Z_1(e^{4u}); replacing it by e^u Z_r would change the original source.

There are two spaces to connect: the exact source Slaters (6) lie in wedge^r H_u, while the displayed geometric equilibrium (9) is on wedge^r H_E. We have not supplied a distinguished state/operator correspondence between them that makes D_{r,k} a thermal energy expectation. An arbitrary Hilbert-space isomorphism would not supply that correspondence. The original determinant is already a genuine r-fermion transition amplitude; identifying these source fermions with the geometric theta-spectrum particles remains an open modeling step. Similarly, wedge^r of a doubled one-particle space is not automatically the TFD double of wedge^r of the physical space.

## 5. Scope and next discussion

The author-selected formulation is: use rho or TFD interchangeably for the same equilibrium state; retain P_0 and the higher responses as observable insertions; use r-particle Slater/Fock sectors for determinant order. The outstanding energy question concerns a common Hamiltonian and preparation/observable map that explains those source-state amplitudes. A transition overlap is not by itself a diagonal energy expectation or a thermal trace, and ordinary positivity of rho does not sign it.

This is a change in representation and modeling preference with no new sign estimate. The [MC02 source-sector construction](../../02_fermionic_correlators/notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md), Section 1, already establishes r-particle source overlaps. Nothing here revives its separate coefficient-transfer dynamics as the selected Hamiltonian. The [MC01 thermal dictionary](../../01_circle_thermal_trace/notes/01_THERMAL_SOURCE_IDENTITY_RETURN_20261101.md) supplies the response recurrence; its filtered ensemble is not required for (2)–(5).

Read with the [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md), especially [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). The analytical control screen in Note02 remains applicable: generic Slater and density/TFD identities also hold for controls with the relevant regularity; weighted-square controls fail full unchanged weights/reflection, and reflected or Euler-modified controls fail the literal unchanged theta spectral reconstruction. No control is declared to fail a new uncomputed bound, and no numerical controls are rerun for this exact change of representation.
