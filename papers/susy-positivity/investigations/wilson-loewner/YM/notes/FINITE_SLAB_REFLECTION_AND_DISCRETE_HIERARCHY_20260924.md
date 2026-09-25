# Reflection-boundary realization and a discrete controlled hierarchy

24 September 2026. Prepared for Edward Baker with substantial GPT-6 (Codex) assistance. Reasoning effort: not exposed; not inferred. These are research-note derivations, not independently reviewed results.

This continues the [preliminary analysis](YM_POSITIVE_HIERARCHY_PRELIMINARY_ANALYSIS_20260924.md) and carries out the first construction in the [research plan](YM_REFLECTION_AND_HIERARCHY_RESEARCH_PLAN_20260924.md). The companion [interacting experiment and next steps](FIRST_INTERACTING_SLAB_TEST_AND_CONTINUATION_20260924.md) tests the construction in four-dimensional lattice SU(2) theory.

The main advance is an exact finite-regulator answer to the OS null-space objection: spatial loop multiplication descends to a reflected Hilbert space when the loops depend only on the shared reflection slice. A finite open slab gives the state and the gluing formula explicitly. This establishes a setting in which the positive configuration norm has a reflection interpretation. It does not establish the corresponding statement for arbitrary operators in a positive-time half-space, for the scalar-coupled N4SYM observable, or in the continuum.

The second advance is an exact discrete residual calculus. Orthogonal compression of finite loop steps loses norm, unlike the continuous skew-generator Galerkin system in the preliminary note. Keeping that distinction yields computable forward, output-specific, and forward/backward error estimates. The first interacting test finds those estimates too large to justify the small trial families.

## 1. A completely specified finite state

Take pure SU(N) Wilson gauge theory at theta zero on a finite spatial three-torus and physical Euclidean-time sites

\[
\tau=-T,-T+1,\ldots,0,\ldots,T,
\]

with open outer time boundaries and normalized Haar integration on every existing link. No boundary sources or matter fields are inserted. The action is

\[
S=\beta\sum_p\left(1-\frac1N\operatorname{Re}\operatorname{tr}U_p\right).
\]

This is the usual gauge-invariant lattice framework introduced by [Wilson (1974)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.10.2445). All identities below are derived directly for this finite integral; no continuum or strong-coupling expansion is needed.

Let \(U\) denote all spatial links on \(\tau=0\). Let \(X_+\) contain all other links belonging to the positive half slab, including temporal links from 0 to 1. Define \(X_-\) correspondingly. Reflection reverses temporal-link orientation, taking its matrix adjoint, and preserves spatial-link orientation. Because plaquettes are nearest-neighbor objects, there is no plaquette involving both strict half interiors. Consequently,

\[
S(U,X_+,X_-)=S_0(U)+S_+(U,X_+)+S_-(U,X_-),
\qquad S_-=\theta S_+.
\]

Here \(S_0\) contains just the spatial plaquettes on the central slice. Set

\[
h(U)=\int dX_+\,e^{-S_+(U,X_+)},\qquad
\Omega(U)=e^{-S_0(U)/2}h(U).
\]

The exact central-slice distribution is

\[
d\nu(U)=Z^{-1}\Omega(U)^2dU,
\qquad Z=\int\Omega(U)^2dU.
\tag{1}
\]

The action is bounded and continuous on a finite product of compact groups. Thus \(\Omega\) is continuous, strictly positive and bounded above and below. Gauge invariance follows by a change of variables in the half-slab integral.

**State qualification.** \(\Omega\) is the amplitude prepared by this finite slab with unit outer-boundary amplitude. It has not been identified with an infinite-time ground-state wavefunction. Sending \(T\) to infinity, establishing vacuum convergence, and removing the spatial cutoff are separate tasks. The experiment uses \(T=2\).

## 2. Reflected matrix networks and the reference color indices

Fix a base vertex \(b\) on the central slice. A matrix-valued half-slab function \(F\) carries a reference endomorphism fiber at \(b\):

\[
F(U^g,X_+^g)=g(b)F(U,X_+)g(b)^{-1}.
\]

Its half-slab amplitude is

\[
\psi_F(U)=e^{-S_0(U)/2}\int dX_+\,e^{-S_+(U,X_+)}F(U,X_+).
\]

Gluing a reflected, adjointed copy of \(F_i\) to \(F_j\), and contracting both reference color indices with the normalized matrix trace, gives

\[
\langle F_i,F_j\rangle_{\rm refl}
=\frac1Z\int dU\,\frac1N\operatorname{tr}
\bigl(\psi_{F_i}(U)^\dagger\psi_{F_j}(U)\bigr).
\tag{2}
\]

This follows by separately integrating \(X_-\) and \(X_+\) in the full Wilson measure. In particular every finite Gram matrix is positive semidefinite. The null space is exactly the kernel of \(F\mapsto\psi_F\), modulo equality almost everywhere.

For a boundary function \(B(U)\),

\[
\psi_B=\Omega B,\qquad
\langle B_i,B_j\rangle_{\rm refl}
=\mathbb E_\nu\frac1N\operatorname{tr}B_i^\dagger B_j.
\tag{3}
\]

Thus the map \(B\mapsto Z^{-1/2}\Omega B\) is an isometry from the covariant subspace of \(L^2(\nu;\operatorname{End}\mathbb C^N)\) to the reflected boundary realization with Haar measure. The positive lower bound on \(\Omega\) also makes the boundary functions sufficient to represent the completed covariant image in (2).

This explicitly retains the singlet and adjoint reference-color channels in an endomorphism fiber. It adds no dynamical bulk matter. All reported contractions are gauge invariant. Tracing each matrix before constructing the Hilbert norm would discard these channels and is a different reduction. We do not identify the extended reference-fiber space with the ordinary scalar gauge-invariant Hilbert space without stating that extra structure.

For based spatial loops \(C_i\), let \(Q_i(U)\) be their ordered link products. Then

\[
K_{ij}=\mathbb E_\nu\frac1N\operatorname{tr}Q_i^\dagger Q_j,
\quad K\succeq0,\quad K_{ii}=1.
\tag{4}
\]

The network is the closed based word with product \(Q_i^\dagger Q_j\). With \(Q_0=I\), \(K_{0i}\) is precisely the Wilson-loop expectation. This is a zero-separation boundary gluing identity: it requires neither propagation of an external color charge for a nonzero physical time nor a static-source energy subtraction.

## 3. Why boundary multiplication escapes the earlier counterexample

Let \(D(U)\) be any bounded covariant boundary matrix. Multiplication intertwines the half integral:

\[
\psi_{DF}(U)=D(U)\psi_F(U).
\tag{5}
\]

Hence it preserves the OS null space. If \(D(U)^\dagger D(U)=I\), it is unitary on the reflected Hilbert space, with inverse multiplication by \(D^\dagger\). This proves the descent property, rather than inferring it from configuration-wise unitarity alone.

The preliminary independent-sign counterexample used a multiplier depending on an integrated interior variable. It could not be pulled through the half integral: a null function could acquire a nonzero amplitude. Equation (5) identifies exactly which hypothesis removes that problem here.

The reflection is in physical Euclidean time; Loewner capacity parametrizes contours in a spatial plane on the slice. Capacity is not physical time. We have constructed a unitary family of changes of a boundary observable, not a Lorentzian evolution or an arbitrary-input passive channel.

The elementary site-reflection factorization above should also not be confused with a proof of a strictly positive one-step transfer matrix. The latter is a stronger standard lattice result; see [Lüscher (1977)](https://link.springer.com/article/10.1007/BF01614090). The publisher's abstract was checked for context, not its subscription-only full proof. Our finite-slab argument is self-contained and requires only (1)–(5).

### A useful consequence for regulator design

Any deterministic, gauge-covariant map from the central spatial links to SU(N) spatial links remains within this boundary algebra. Loops formed from those links still obey (3)–(5). Thus a smoothing operation using **only the spatial slice** can be investigated without losing this finite-lattice reflection construction. For example, a smooth link flow \(\partial_\sigma V_l=X_l(V)V_l\), with traceless anti-Hermitian \(X_l\) transforming at the starting vertex and constructed solely from spatial loops, preserves group membership and boundary dependence.

This is an admissibility result, not a bound on smoothing bias. One must still specify the flow, compare its observable with the unsmoothed loop, and study the fixed-physical-smoothing-scale limit. A four-dimensional flow using links on both sides of the reflection plane does not automatically satisfy (5).

## 4. Exact finite contour steps

Choose actual lattice loops \(Q_0=I,Q_1,\ldots,Q_M\) on the slice. The same \(\nu\) is used at every step. Define unitary multiplication operators

\[
\mathcal U_n X=D_nX,\qquad D_n=Q_{n+1}Q_n^\dagger.
\]

Then \(\Psi_n=Q_n\) obeys \(\Psi_{n+1}=\mathcal U_n\Psi_n\), \(\|\Psi_n\|=1\), and \(W_n=\langle e,\Psi_n\rangle\), where \(e=I\) has norm one. There is no interpolation or lattice field-strength approximation in this equation.

Writing \(P=|e\rangle\langle e|\), \(\Psi_n=eW_n+z_n\), gives

\[
|W_n|^2+\|z_n\|^2=1.
\tag{6}
\]

The complement can return amplitude to \(W\). In block notation \(a_n=P\mathcal U_nP\), \(b_n=P\mathcal U_nP^\perp\), \(c_n=P^\perp\mathcal U_nP\), \(d_n=P^\perp\mathcal U_nP^\perp\), its elimination yields

\[
W_{n+1}=a_nW_n+
\sum_{j=0}^{n-1}b_n d_{n-1}\cdots d_{j+1}c_jW_j.
\tag{7}
\]

The empty product is the identity and \(z_0=0\). These are exact memory terms. A product of scalar expectations \(\prod a_n\) deletes them. The individual memory coefficients need not be positive; (6) is the positive storage identity. In particular (7) is not being identified with the continuous two-time Gram kernel derived for a skew generator in the preliminary note.

## 5. Moving finite families and the Schur residual

Let \(B_n\) denote a column family of covariant boundary functions spanning \(S_n\), with \(e\in S_n\). Remove linear dependencies and assume the Gram matrix \(G_n=B_n^\dagger B_n\) is positive definite. Adjoint here uses the Hilbert inner product (3), not merely pointwise matrix adjoint. Let

\[
T_n=B_{n+1}^\dagger\mathcal U_nB_n,\qquad
\Pi_n=B_nG_n^{-1}B_n^\dagger.
\]

The discrete approximation is

\[
\widehat\Psi_n=B_nc_n,\qquad
c_{n+1}=G_{n+1}^{-1}T_nc_n,
\qquad \widehat\Psi_0=e.
\tag{8}
\]

Its residual is orthogonal to the destination family:

\[
r_{n+1}=\widehat\Psi_{n+1}-\mathcal U_n\widehat\Psi_n,
\quad r_{n+1}\perp S_{n+1},
\]

\[
\rho_{n+1}^2=\|r_{n+1}\|^2
=c_n^\dagger\left(G_n-T_n^\dagger G_{n+1}^{-1}T_n\right)c_n.
\tag{9}
\]

The matrix in parentheses is a positive Schur complement of the joint Gram matrix of \(\mathcal U_nB_n\) and \(B_{n+1}\). Therefore

\[
\|\widehat\Psi_n\|^2-\|\widehat\Psi_{n+1}\|^2=\rho_{n+1}^2.
\tag{10}
\]

This is a **contractive compression**. It is not the norm-preserving continuous Galerkin evolution previously derived. The sum of discarded norms in (10) measures approximation loss; it is not the exact complement norm in (6), because discarded pieces can subsequently interfere and return.

The recurrence for \(E_n=\widehat\Psi_n-\Psi_n\) gives

\[
E_N=\sum_{j=1}^N\mathcal U_{N\leftarrow j}r_j,
\qquad \|E_N\|\le\sum_{j=1}^N\rho_j,
\tag{11}
\]

where \(\mathcal U_{N\leftarrow j}=\mathcal U_{N-1}\cdots\mathcal U_j\). Since \(r_j\perp e\),

\[
|\widehat W_N-W_N|
\le\sum_{j=1}^N\eta_{N,j}\rho_j,
\quad
\eta_{N,j}=\|(\mathcal U_{N\leftarrow j}^\dagger-I)e\|.
\tag{12}
\]

Telescoping the actual loop products gives

\[
\eta_{N,j}^2=2-2\operatorname{Re}K_{Nj},\qquad
\eta_{N,N}=0.
\tag{13}
\]

An estimate using only successive-loop data is

\[
\eta_{N,j}\le\min\left(2,\sum_{k=j}^{N-1}\ell_k\right),
\qquad \ell_k=\sqrt{2-2\operatorname{Re}K_{k+1,k}}.
\tag{14}
\]

Equation (13) is useful diagnostically but requires future pair-loop measurements; it is not a free prediction of the final loop. Equation (14) avoids these extra pairs. Both express why an observable error can be much smaller than its state error. The most recent residual has no immediate effect on \(W_N\), but can affect later outputs.

## 6. An output bound from a backward hierarchy

A further estimate can be computed from the **same** \(G_n,T_n\) used in (8), without the future loop Gram entries in (13). Fix output step \(N\), set \(\chi_N=e\), and run

\[
\chi_j=\Pi_j\mathcal U_j^\dagger\chi_{j+1},
\quad s_j=\chi_j-\mathcal U_j^\dagger\chi_{j+1},
\quad \delta_j=\|s_j\|.
\]

Writing \(\chi_j=B_jh_j\),

\[
h_j=G_j^{-1}T_j^\dagger h_{j+1},
\quad
\delta_j^2=h_{j+1}^\dagger
\left(G_{j+1}-T_jG_j^{-1}T_j^\dagger\right)h_{j+1}.
\tag{15}
\]

The exact backward state is \(p_j=\mathcal U_{N\leftarrow j}^\dagger e\). Unitarity gives \(\|p_j-\chi_j\|\le\sum_{k=j}^{N-1}\delta_k\). Pairing (11) with \(e\) and using \(r_j\perp\chi_j\) proves

\[
\boxed{
|\widehat W_N-W_N|
\le\sum_{j=1}^N\rho_j\sum_{k=j}^{N-1}\delta_k.}
\tag{16}
\]

Thus one can improve the output guarantee by approximating both the forward loop state and the backward readout. The estimate is exact for the true Gram data; Monte Carlo evaluation adds statistical uncertainty. The companion computation checks the algebra independently on 30 dense complex-unitary systems with moving subspaces. In the interacting run (16) improves the simpler bounds but remains too large to be useful. It is a direction for better observable selection, not a retrospective explanation that the tested family succeeded.

## 7. What has and has not overcome the N4SYM obstruction

The N4SYM study found genuine extra insertion sectors, nonunitary scalar-coupled transport, and failure of the proposed small closed hierarchy. None is contradicted here. We changed to pure gauge transport on a specified spatial boundary and preserved all omitted sectors through either exact memory or an explicit residual.

The progress is substantive but conditional on that changed problem:

| Earlier difficulty | Result at the finite YM boundary | Remaining burden |
|---|---|---|
| Configuration positivity need not descend through OS nulls | Boundary multiplication satisfies the intertwining identity (5) | Interior observables and the original N4SYM loop require their own construction |
| Infinite insertion hierarchy | Every chosen family has exact Schur residuals and bounds (9), (12), (16) | The residuals must actually become small at affordable dimension |
| Coarse lattice geometry has no exact clover generator | Actual finite loop products define every step | A relation to smooth contour evolution must be proved under refinement |
| Smoothing can mix reflection halves | Slice-only covariant group-valued smoothing stays in the boundary algebra | Its bias, continuum limit and effect on residuals are untested |
| A positive physical norm was mistaken for an arithmetic mechanism | The boundary Wilson norm and its readout are explicitly identified | No arithmetic response, prime delays, or Weil-form identity follows |

The finite reflection construction can now be treated as a completed local derivation awaiting review. The small-family efficiency question remains open, with an unfavorable first coarse-lattice result. That result and the next discriminating experiment are recorded separately.
