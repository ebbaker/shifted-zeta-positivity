# Fermionic correlators and physical interpretations of the theta determinants

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**, from current-turn metadata. Research chat `01a19a10-57b7-7c52-940c-103fc06d15a5`.

**Scope:** author-requested conceptual exploration of quantum-field and topological-field interpretations during J-B10. This extends the explanatory discussion; it is not the completed signed-curvature estimate required by plan r1. The exact constructions below follow from existing source integrability and elementary determinant/CAR algebra. They have same-assistant analytical checking, not independent review. They prove no new canonical sign, curvature bound or RH statement.

**Answer:** the determinants admit exact smeared free-fermion correlation representations. The positive carrier also defines a biorthogonal particle ensemble with determinantal correlation functions. The coefficient minors are rectangular Schur specializations and obey a discrete bilinear determinant relation. A topological-field realization with an identified invariant, manifold and protected observable has not been constructed.

## 1. The physical origin of the theta source

Take a quantum particle on a circle of circumference 2pi, with periodic eigenstates exp(inx)/sqrt(2pi) and Hamiltonian L=-pi d^2/dx^2. Its energies are pi n^2, so, for beta>0,
\[
\operatorname{Tr}e^{-\beta L}=\sum_{n\in\mathbb Z}e^{-\pi\beta n^2}=\vartheta(\beta).
\]
This is an exact spectral computation, fixing the otherwise arbitrary energy units. The project's primitive and source are
\[
p(u)=\frac12e^u[\vartheta(e^{4u})-1],\qquad
\Phi(u)=\frac18(p''(u)-p(u)).
\]
Thus the source is a differential expression in a log-temperature reparametrization of the thermal trace, with the zero mode subtracted. This retains the complete integer-square spectrum. It is an ordinary trace, not a supersymmetric index or topological invariant. The Mellin parameter s used below is distinct from the thermal parameter beta and from physical heat time.

## 2. Exact 2r-operator free-fermion correlators

Keep the fixed coefficients c_n=integral u^(2n)Phi(u)du/(2n)!, c_n=0 for n<0, and D_(r,k)=det[c_(k+j-i)]. On the one-particle Hilbert space H=L^2((0,infinity),du), define real functions
\[
f_i(u)=\frac{\Phi^{(2i)}(u)}{\sqrt{\Phi(u)}},\qquad
g_{k,j}(u)=\frac{u^{2(k+j)}\sqrt{\Phi(u)}}{(2(k+j))!},
\quad 0\le i,j<r.
\]
All functions lie in H for each finite r,k. Near zero Phi is positive and smooth; in the tail, the fixed derivative ratios have at most fixed exponential growth in u while Phi decays double exponentially. The existing integration-by-parts identity gives
\[
\langle f_i,g_{k,j}\rangle=c_{k+j-i}.
\]
Let a(f),a^dagger(g) be annihilation and creation operators with the canonical anticommutation relation {a(f),a^dagger(g)}=<f,g>. In the empty vacuum,
\[
\boxed{D_{r,k}=\langle0|a(f_{r-1})\cdots a(f_0)
a^\dagger(g_{k,0})\cdots a^\dagger(g_{k,r-1})|0\rangle.}
\]
The order of the annihilators is essential. Expanding by the CAR gives the determinant, with r=1 giving the displayed inner product and r=2 giving its usual two terms. Equivalently,
\[
D_{r,k}=\langle f_0\wedge\cdots\wedge f_{r-1},
g_{k,0}\wedge\cdots\wedge g_{k,r-1}\rangle.
\]
This is an exact equal-time, smeared 2r-field correlation in a free-fermion Fock representation, or an overlap of r-particle Slater states. It is not a claim that r counts spacetime insertion points, that c_(k+j-i) is a translation-invariant propagator, or that a theta-selected local interacting action has been found. Theta enters these wavefunctions. The elementary Wick mechanism and its integrable-system extensions are documented in Alexandrov–Zabrodin, Section 2.3 and Section 2.7, [arXiv:1212.6049v3](https://arxiv.org/pdf/1212.6049v3).

The two Slater states differ. Their overlap need not be nonnegative in a positive Hilbert space. Cauchy–Schwarz gives an absolute upper bound, not the required sign. Replacing the overlap by its squared modulus changes the observable. Reflection positivity likewise would require an actual adjoint/reflection pairing for these insertions, not merely a unitary state space. This identifies the sign issue rather than resolving it.

## 3. Mellin curvature is a connected correlation in this representation

For the unnormalized integral M_r(s), use b_j(u)=u^(2j)sqrt(Phi(u)), and let |F_r> and |B_r> be the wedges of f_i and b_j. On r-particle coordinate wavefunctions define the self-adjoint multiplication operator
\[
\widehat T=2\sum_{j=1}^r\log u_j.
\]
Then the same determinant-composition identity gives
\[
M_r(s)=\langle F_r|e^{s\widehat T}|B_r\rangle,
\qquad s\ge0.
\]
The vectors are in the needed domains for every fixed s>=0, including additional fixed log powers. No unbounded-operator estimate is inferred merely from the notation. Where M_r(s)>0, define the normalized cross matrix element of a function of T by division by M_r(s). Direct differentiation gives
\[
\partial_s\log M_r=\langle\widehat T\rangle_s^{FB},\qquad
\partial_s^2\log M_r=
\langle\widehat T^2\rangle_s^{FB}
-(\langle\widehat T\rangle_s^{FB})^2.
\]
It has the form of a connected two-point response. Because the bra and ket differ, this is not the variance of a positive probability distribution. At r=3, the accepted signed-averaging result supplies M_3(s)>0; no such all-r real-tilt claim is imported. No Gaussian response bound follows from Wick's theorem alone.

## 4. A positive particle ensemble already exists for the carrier

The accepted R=Phi''/Phi has R'>0. For every fixed r and s>=0, the carrier on the ordered chamber is
\[
w_{r,s}(\mathbf u)=\prod_j u_j^{2s}\Phi(u_j)
V(\mathbf u^2)V(R(\mathbf u))>0.
\]
The associated full-orthant symmetric probability density is w_(r,s)/(r!Z_(r,s)), where Z is the ordered integral. It is exactly a biorthogonal ensemble: write a_i(u)=u^(2i)sqrt(u^(2s)Phi(u)) and b_i(u)=R(u)^i sqrt(u^(2s)Phi(u)). The density is the product of det[a_i(u_j)] and det[b_i(u_j)], normalized by its full integral. Absolute integrability follows from the same fixed-order tail bounds. Its pairing matrix A_ij=integral a_i b_j has det A=Z>0 by determinant composition, hence is invertible.

Its m-point particle densities, 1<=m<=r, are determinants of a correlation kernel. A consistent convention is K(x,y)=sum_(i,j) a_i(x)(A^(-1))_(j,i)b_j(y); the inverse transpose matters with this definition of A. Integrating K(x,x) gives r. This is the general construction in Borodin, Section 2, equations (2.8) onward, and Desrosiers–Forrester, Introduction, equations (1), (3)–(5). Use the normalized-marginal convention rho_m=r!/(r-m)! integral P_r; do not copy an additional normalization factor from the displayed v1 marginal formula.

The original determinant is still the inserted observable
\[
M_r(s)=Z_{r,s}\,E_{r,s}h_r.
\]
Thus positivity of the particle ensemble establishes Z>0, not the sign of the h_r insertion. At r=3 the complete curvature retains the centered-square covariance involving h_3. Controlling only the carrier's number fluctuations or variance leaves that term unresolved. A matrix-model or loop-equation approach would need relations for the insertion as well as the carrier.

The Gaussian source gives h_r=1 and reduces the derivative determinant to a positive Vandermonde factor. This is the familiar squared-Slater-determinant situation. Theta gives different derivative orbitals and a signed insertion. The Gaussian case checks normalization, not the theta response bound.

## 5. Schur functions and the bilinear integrable structure

Let H_n=c_n/c_0 and define a formal sequence of times t_m by
\[
\frac{F(z)}{c_0}=\sum_{n\ge0}H_nz^n
=\exp\!\left(\sum_{m\ge1}t_mz^m\right).
\]
The formal logarithm exists because H_0=1; no global zero-free logarithm is asserted. The complete symmetric functions at this specialization are h_n(t)=H_n. Jacobi–Trudi therefore gives exactly
\[
\boxed{D_{r,k}=c_0^r s_{(k^r)}(\mathbf t),}
\]
where (k^r) is the rectangle with r rows of length k. This follows entry by entry, including h_n=0 for negative n. These are specializations of the Schur functions that appear in free-fermion current matrix elements and integrable tau-functions; see Alexandrov–Zabrodin, Section 2.10, Section 3.4.1 and Appendix A, especially (A3).

The existing identity
\[
D_{r+1,k}D_{r-1,k}=D_{r,k}^2-D_{r,k-1}D_{r,k+1}
\]
is a bilinear determinant/Plucker relation of the type underlying discrete Toda equations. It is already a structural part of this problem. Naming it does not prove positivity, supply missing deformation variables, or construct a finite isomonodromic system for the theta source. The formal theta specialization is not known here to be Schur-positive; the positivity of general representation dimensions cannot be substituted for its value.

## 6. What would make a topological-field interpretation substantive

Witten's 1988 construction represents Donaldson invariants using observables of a twisted four-dimensional supersymmetric gauge theory. The key structure includes a cohomological symmetry Q, Q-closed observables, and a stress tensor that is a Q-commutator, so metric variations decouple subject to measure/anomaly and boundary conditions. Invariants concern smooth structure, not an assertion that every observable on a topological manifold is automatically positive. See [Witten, Sections 2–3 and 5](https://www.ias.edu/sites/default/files/sns/%5B109%5DCommMathPhys117-1988.pdf), particularly (3.8)–(3.10) and the associated qualification about the measure.

Here no spacetime manifold/moduli problem, Q-symmetry, protected observables or localization theorem has been identified that evaluates the unchanged theta D_(r,k). The determinants vary with the source and its wavefunctions. Wick and Plucker identities are generic and do not supply topological invariance. The circle heat trace depends on its geometric/thermal data. These observations leave a future cohomological construction open; they do not assert that no such construction can exist.

## 7. Research judgment and controls

The closest established mathematical-physics tools are the free-fermion and biorthogonal-ensemble descriptions. For this Mellin task, a useful conceptual test is whether the exact theta differential relations and source integration by parts yield an additional Ward/loop identity for the complete inserted generating function M_3(s). It would have to control the signed connected response relative to kappa_3, with origin, node faces, full spatial tails and the large-s range paid. Reproducing determinant composition or the known bilinear identity is not that estimate. No such identity or estimate is acquired in this note.

This follows the [result index](../../../../../../result-summaries/README.md), especially [prior physical-channel lessons](../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md) and [controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../../avoid/README.md), especially [re-realizations](../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

Claim-specific screen: Wick/exterior algebra and formal Schur specialization are generic and exclude none of the smooth positive even control sources that meet their integrability assumptions. Controls lacking full evenness do not satisfy the small-index endpoint identity as stated. Carrier biorthogonality additionally requires increasing R; that property is untested here for the controls. The exact circle spectrum/unchanged source construction is absent from the modified Euler-factor, weighted-square, reflected and positive-primitive sources, but identifying theta this way does not itself sign the amplitude. A positive-time collision is not a counterexample to a time-zero finite-order statement. The rescaled two-point example remains a screen against association/boundedness-only reasoning, not an actual fermion-theta realization.

**Next: [B] J-B10 — Astra.** If the author chooses this physical viewpoint, select one source-derived identity for the signed insertion and determine whether it gives a new response estimate beyond Wick/Plucker algebra. The previously proposed tail/compact route remains available. No new E contract, computational campaign, higher-order positivity result or topological theory is issued here.

Selected primary passages, inspection limits and external PDF receipts are recorded in [the physical-interpretation source note](../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md). No third-party PDF is stored in the repository.
