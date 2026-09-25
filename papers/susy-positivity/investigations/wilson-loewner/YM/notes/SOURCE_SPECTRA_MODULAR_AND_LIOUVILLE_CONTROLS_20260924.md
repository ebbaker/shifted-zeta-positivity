# Spectral consequences of an exact pairing: modular and Liouville controls

Date: 24 September 2026, America/New_York.  
Prepared for Edward Baker with substantial LLM assistance.  
Model exposed: GPT-6 (Codex); exact variant and configured reasoning effort not exposed, not inferred.  
Baseline: b60a2e27b9a39be33b1b43bb7b99172cdc5e7573.  
Status: session deductions with proofs and explicit conditional hypotheses; not independently reviewed. These are scoped tests of operator identifications, not a no-go theorem for YM realization.

Read with the [critical review](../reviews/GLOBAL_MECHANISMS_CRITICAL_REVIEW_20260924.md), [global determination theorem](OFF_DIAGONAL_RIGIDITY_AND_COMPACT_SOURCE_EXISTENCE_20260924.md), and [primary-source ledger](GLOBAL_MECHANISMS_PRIMARY_SOURCE_LEDGER_20260924.md).

## 1. An exact source image has a more specific spectrum than “two-sided”

Suppose a continuous linear map \(J:\mathcal D^0\to\mathcal H\) into a positive Hilbert space satisfies
\[
\langle Jf,Jg\rangle=Q(f,g).
\tag{1}
\]
Let \(\mathcal S=\overline{J\mathcal D^0}\). The preceding notes correctly construct
\[
V(a)Jf=J(U_af),\qquad V(a)=e^{-iaG}.
\tag{2}
\]
This induced action needs no separate physical interpretation.

**Proposition 1 (conditional identification of the source spectrum).** Under (1), let \(\gamma\) range over distinct ordinates of the nontrivial zeta zeros and \(m_\gamma\) be their multiplicities. Then
\[
(\mathcal S,V)\simeq
\left(\ell^2(\{\gamma\},m_\gamma),
      F(\gamma)\mapsto e^{-ia\gamma}F(\gamma)\right).
\tag{3}
\]
Thus \(G\) has pure point spectrum, with one source-space eigenline per distinct ordinate. A zero of multiplicity \(m_\gamma\) contributes its weight to the norm; it does not force a Jordan block or \(m_\gamma\) independent source eigenvectors.

**Proof.** Equation (1) gives positivity of \(Q\) on all of \(\mathcal D^0\). The restricted Weil criterion implies RH. This implication is used as a consequence of (1), not as an input for constructing \(J\).

Under that consequence, the explicit formula in the outline's Fourier normalization is
\[
Q(f,g)=\sum_\gamma m_\gamma
\overline{\widehat f(\gamma)}\,\widehat g(\gamma).
\tag{4}
\]
The possible initial sign \(-\gamma\) from Mellin conventions disappears by reindexing the conjugate zeros. The sum converges absolutely for smooth compactly supported tests, since the zero-counting measure has polynomial growth.

Consequently \(Jf\mapsto(\widehat f(\gamma))_\gamma\) defines an isometry onto the closure of these evaluation vectors. That closure is the whole weighted sequence space. To see this, suppose \(z\in\ell^2(m_\gamma)\) is orthogonal to all of them. The distribution
\[
D_z=\sum_\gamma m_\gamma\overline{z_\gamma}\,\delta_\gamma
\]
is tempered by Cauchy–Schwarz and polynomial growth of the zero count. Testing against \(\widehat{Th}=(\tau^2+1/4)\widehat h\), for every \(h\in C_c^\infty\), shows
\((\tau^2+1/4)D_z=0\). Indeed Fourier transforms of these \(h\)'s are dense in the Schwartz space. The reciprocal multiplier \(1/(\tau^2+1/4)\) preserves that space, so \(D_z=0\) and \(z=0\). Finally \(\widehat{U_af}=e^{-ia\tau}\widehat f\) proves (3). \(\square\)

The restricted criterion and explicit formula were checked in [Connes–Consani, Appendices B–C](https://arxiv.org/pdf/2006.13771). No presumptive RH zero spectrum has been used to build a YM operator.

**Consequence for proposed native operators.** If a pre-existing selfadjoint YM operator is required to implement (2), its reducing source sector must contain these point eigenvalues with the actual source weights. A purely continuous native spectrum is insufficient. In the finite-order spectral-source ansatz, the source measure is absolutely continuous with respect to the seed's spectral measure, so polynomial weighting cannot turn continuous spectral mass into atoms.

This is stricter than the preceding unboundedness/nonperiodicity tests, but still applies only to an asserted identification with a native operator. It imposes no obstacle to seeking \(J\) first.

## 2. The current boundary multiplication algebra has trivial modular flow

Consider the bounded covariant matrix functions in the finite-slab construction, with pointwise multiplication and adjoint. Their state is
\[
\tau(B)=\int_M \frac1N\operatorname{tr}B(U)\,d\nu(U).
\]
It is a faithful finite trace, since \(\tau(BC)=\tau(CB)\) pointwise under the matrix trace. The closure in its \(L^2\) representation has cyclic separating vector \(I\).

**Proposition 2.** The modular operator of this algebra and this vector is the identity.

**Proof.** The Tomita operator on its dense core is \(S(B)=B^\dagger\). Traciality gives \(\|B^\dagger\|_2=\|B\|_2\); hence \(S\) extends to an antiunitary involution. Its polar decomposition has \(\Delta=S^*S=I\). \(\square\)

The scalar gauge-invariant multiplication algebra has the same conclusion. A nonconstant Wilson density changes integration weights, but it is central in this algebra and does not make the state nontracial. In particular, multiplication by \(-\log w(U)\) is not the modular Hamiltonian of this representation.

**Control.** A faithful noncentral matrix density on a noncommutative algebra has nontrivial modular flow, as the thermal example below shows. The conclusion is about the specified boundary state/algebra, not all YM algebras. Adding electric operators changes the algebra; taking all of \(B(\mathcal H)\) with a pure vector state does not automatically fix the issue, since that vector is not separating when \(\dim\mathcal H>1\).

## 3. Geometric vacuum wedge modular flow also has a scoped obstruction

The original [Bisognano–Wichmann paper](https://doi.org/10.1063/1.522605) identifies wedge modular structure with boosts under its relativistic field and domain hypotheses. For a prospective continuum YM observable net, existence, the spectrum condition, standardness, and the applicable wedge modular identification must be supplied. Finite-slab OS positivity alone gives none of these.

There is an elementary spectral test independent of the mass gap.

**Lemma 3.** Let a strongly continuous unitary Poincaré representation have joint translation spectrum in the closed forward cone. Assume its translation-invariant subspace is one-dimensional, spanned by a Poincaré-invariant vacuum \(\Omega\). The selfadjoint generator of a one-axis Lorentz boost group has no eigenvectors other than multiples of \(\Omega\).

**Proof.** If \(\psi\) is a boost eigenvector, its finite positive joint momentum spectral measure \(\mu_\psi\) is boost invariant: the phase of the vector cancels in every spectral projection expectation.

On the forward cone put \(p_\pm=p^0\pm p^1\ge0\). A boost scales these by \(e^t\) and \(e^{-t}\), up to an immaterial sign convention. The marginal on \(p_+>0\), pushed forward by \(\log p_+\), is a finite translation-invariant measure on \(\mathbb R\), hence zero. For example all disjoint translates of \([0,1)\) would otherwise have the same positive mass. The same applies to \(p_->0\).

Thus \(\mu_\psi\) is supported on \(p_+=p_-=0\). The forward-cone condition then forces all momentum components to vanish. The vector is translation invariant, hence a multiple of \(\Omega\); its boost eigenvalue is zero. \(\square\)

**Corollary 4.** Under these hypotheses, no source map satisfying (1) can identify the arithmetic action with a nonzero constant rescaling of geometric vacuum wedge modular time on a reducing source subspace.

**Proof.** Proposition 1 requires nonzero point eigenvalues, while Lemma 3 forbids them for the boost. The wedge modular identification transfers the contradiction. \(\square\)

**Controls and limits.** Boosts on a one-particle rapidity space act by translations and have continuous spectrum, consistent with the lemma. A bilateral diagonal operator on \(\ell^2\) can have arbitrary point eigenvalues, so the conclusion is not a prohibition of two-sided selfadjoint operators. Nonvacuum states, nongeometric modular flows, nonwedge algebras, and representations with a larger zero-momentum sector are outside the stated hypotheses. Generalized seeds do not evade the corollary if every smeared source must still be a vector in this same Hilbert space.

## 4. Energy differences: what a thermal Liouville sector actually adds

Let a physical Hilbert space \(\mathfrak h\) have a selfadjoint Hamiltonian with eigenbasis \(H|n\rangle=E_n|n\rangle\), and assume
\[
\rho=Z_\beta^{-1}e^{-\beta H},\quad Z_\beta<\infty,\quad \beta>0.
\]
On the Hilbert space of Hilbert–Schmidt operators \(\mathrm{HS}(\mathfrak h)\), the selfadjoint Liouville generator is
\[
L=H_{\rm left}-H_{\rm right},\qquad
L|m\rangle\langle n|=(E_m-E_n)|m\rangle\langle n|.
\tag{5}
\]
It is defined by the commuting left/right spectral resolutions. This is the standard GNS representation of the faithful Gibbs state, with vector \(\rho^{1/2}\), not the original finite-slab boundary vector. No second dynamical gauge field is required to define it, but the state and observable representation have changed.

For a bounded selfadjoint \(A\), the vector \(v=A\rho^{1/2}\) has spectral measure
\[
\mu_v=\sum_{m,n}r_n|A_{mn}|^2\delta_{E_m-E_n},
\quad r_n=Z_\beta^{-1}e^{-\beta E_n}.
\tag{6}
\]
Swapping \(m,n\) proves the detailed-balance relation
\[
\mu_v(-d\lambda)=e^{-\beta\lambda}\mu_v(d\lambda).
\tag{7}
\]
An even measure of this particular form must therefore be supported at zero. This prevents that selfadjoint-observable seed from giving the nontrivial even arithmetic measure. Nonselfadjoint seeds are not covered by this statement.

There is a precise way to remove the asymmetry:
\[
v_c=\rho^{1/4}A\rho^{1/4},\qquad
\mu_{v_c}=\sum_{m,n}\sqrt{r_mr_n}|A_{mn}|^2\delta_{E_m-E_n}.
\tag{8}
\]
For selfadjoint \(A\), this measure is even. Schatten Hölder gives
\(\|v_c\|_{\rm HS}\le\|A\|\), so it is an ordinary finite-norm vector. Smearing its unitary orbit is still excluded by the earlier high-frequency argument. A singular source or a finite-order generalized seed remains necessary.

The thermal modular operator is \(\Delta=\rho_{\rm left}\rho_{\rm right}^{-1}=e^{-\beta L}\); thus \(-\log\Delta=\beta L\). These formulas also give the explicit nontracial control for Proposition 2.

**Exact missing lemma.** One would need a gauge-admissible generalized source in this thermal operator sector whose spectral mass at actual YM energy differences equals the arithmetic measure, or whose pairing satisfies the separated-support identity. The source domain must control the unbounded insertions and the Gibbs factors. Neither (5) nor (8) produces prime powers, gamma normalization, or the required energy differences.

**Vacuum caution.** Writing a commutator on \(A\Omega\) does not automatically create a two-sided representation. If \(H\Omega=0\), then \([H,A]\Omega=HA\Omega\) on the common domain; the physical vacuum Hilbert generator remains semibounded. The thermal standard representation is a substantive sector/state choice.

## 5. Arithmetic modules: multiplicities, pairing freedom, and a faithful-jet trap

Meyer constructs an arithmetic quotient and a character without assuming RH. His Corollary 4.2, including its proof, explicitly locates derivative-evaluation generalized eigenvectors in the **continuous dual** of that quotient. They are not automatically normalizable Hilbert vectors. The geometric character in Theorem 5.8 is a virtual trace before removing the pole contribution. These distinctions matter when proposing occurrence in YM.

Two elementary controls constrain a faithful module ansatz:

1. On two distinct unitary character lines, every diagonal form
   \(a|z_1|^2+b|z_2|^2\), with real \(a,b\), is invariant. One normalization leaves freedom. Reflection pairs the weights at opposite frequencies, but does not determine all weights. Module occurrence and translation covariance alone therefore do not imply pairing uniqueness.
2. Suppose a chosen finite jet module carries \(D=\rho I+N\), with \(N\ne0\) nilpotent, and is injected into actual Hilbert vectors intertwining \(e^{t(D-1/2)}\) with a unitary group. On an eigenvector, norm invariance forces \(\operatorname{Re}\rho=1/2\). On a nontrivial Jordan chain, the orbit has polynomial growth in \(t\), contradicting norm invariance. Thus that faithful finite-jet occurrence requires \(N=0\).

**Scope.** If one insists that all multiplicity jets attached to every zero occur faithfully as non-null Hilbert vectors, the ansatz also requires simple zeros. The original Weil-pairing problem does not: Proposition 1 retains multiple zeros as positive weights. This is not a theorem that an arbitrary continuous map from Meyer's original Fréchet quotient imposes simplicity. Dual distribution vectors need not be in the physical Hilbert space, and a nonfaithful map may kill nilpotent directions. Any proposed module realization must specify which of these objects it uses.

Trace multiplicities can fix information that an invariant inner product alone leaves free. But replacing a nuclear character by a Hilbert–Schmidt norm requires an actual star representation and the correct trace/state identity. Taking a trace in a new operator space is an additional structure unless its equivalence to the stipulated YM OS pairing is proved.

## 6. Outcome for the investigation

These controls rule out several **particular operator identifications**: the present tracial boundary modular flow, geometric vacuum wedge boosts under the stated hypotheses, and ordinary finite-norm Liouville seeds. Thermal centered generalized sources remain a coherent class, with the arithmetic identity entirely unresolved.

The main existence route need not pass any of these operator gates. It can seek actual YM source vectors and prove their pairing through the global determination theorem. The native causal target still requires physical preparation, evolution, readout, and an ordinary energy estimate identifying the specified shifted-zeta ratio; no proposition here supplies it.

Verification: all finite-dimensional thermal identities were recomputed directly; the boost lemma was proved from momentum spectral measures; the arithmetic spectral statement uses RH only after deriving it conditionally from an exact positive realization. No numerical zero list or designed spectrum was used. Independent review remains required.
