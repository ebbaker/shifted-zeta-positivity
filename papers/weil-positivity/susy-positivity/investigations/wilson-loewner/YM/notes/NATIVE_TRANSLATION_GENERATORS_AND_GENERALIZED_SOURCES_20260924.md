# Native translation generators and generalized YM sources

Date: 24 September 2026, America/New_York.  
Prepared for Edward Baker with substantial LLM assistance.  
Model: GPT-6 (Codex). Reasoning effort: not exposed; not inferred.  
Status: analytical continuation, with scoped operator exclusions and a generalized-source construction. Not independently reviewed. The arithmetic matching problem remains open.

This continues the [global source audit](GLOBAL_SOURCE_AND_WARD_IDENTITY_AUDIT_20260924.md). The [project outline](../PROJECT_OUTLINE.md) defines the Weil form, pole-neutral test class, and fixed YM boundary space. OS positivity remains assumed. This note tests native candidates for the arithmetic translation action instead of extending numerical support windows.

## 1. The source action is a concrete operator question

Let \(\mathcal D^0\) be the global pole-neutral class, \(U_a f(x)=f(x-a)\), and suppose an exact source map exists:
\[
J:\mathcal D^0\longrightarrow\mathcal H_{\mathrm{YM}},
\qquad Q(f,g)=\langle Jf,Jg\rangle.
\tag{1}
\]
On \(\mathcal S=\overline{J\mathcal D^0}\), common-translation invariance of \(Q\) gives a strongly continuous unitary group
\[
V(a)Jf=J(U_a f),\qquad V(a)=e^{-iaG},
\tag{2}
\]
with selfadjoint generator \(G\). Differentiating on the smooth source image gives
\[
GJf=-iJ(f').
\tag{3}
\]
Indeed, all derivatives of the translated test exist in the smooth-test topology, so these source vectors lie in the domains of every power of \(G\).

An operator proposed on the larger YM Hilbert space must leave \(\mathcal S\) reducing and restrict to this action. Defining \(V\) from (1) is a necessary consequence, not a proof that the independently given YM operators realize it.

Reflection of the arithmetic coordinate is also a linear symmetry. Set \(Rf(x)=f(-x)\). The pole-neutral constraints are exchanged, and the gamma multiplier and paired prime shifts give
\[
Q(Rf,Rg)=Q(f,g),\qquad RU_aR=U_{-a}.
\]
Therefore \(\mathscr R Jf=J(Rf)\) is a unitary involution on \(\mathcal S\), and
\[
\mathscr R G\mathscr R=-G.
\tag{4}
\]
This arithmetic reflection need not already have a native physical interpretation. Its existence on an exact source image follows from the target pairing itself.

## 2. The generator must be unbounded in both directions

For a fixed nonzero \(h\in C_c^\infty(I)\), use the exactly pole-neutral family
\[
f_\lambda=\lambda^{-2}(-\partial_x^2+1/4)(e^{i\lambda x}h).
\]
The previous audit proves, at a fixed support interval,
\[
Q[f_\lambda]=\|h\|_2^2\log\lambda+O(1).
\tag{5}
\]
Applying the same proof to \(r_\lambda=(i\lambda)^{-1}f_\lambda'\) gives
\[
Q[f_\lambda']=\lambda^2\bigl(\|h\|_2^2\log\lambda+O(1)\bigr).
\tag{6}
\]
No RH assumption enters these fixed-support high-frequency estimates.

**Proposition 1.** The generator \(G\) in an exact realization cannot be bounded or semibounded. Its spectrum on \(\mathcal S\) is unbounded above and below.

**Proof.** If \(\|G\|\le M\), (1) and (3) imply
\[
Q[f']=\|GJf\|^2\le M^2 Q[f].
\]
Equations (5)–(6) contradict this as \(\lambda\to\infty\). If \(G\) were merely bounded below, (4) would bound it above as well, making it bounded. The same argument applies to an upper bound. ∎

This excludes identifying arithmetic translations with \(e^{-iaH}\) for a semibounded physical Hamiltonian \(H\), even after a constant energy shift. The previous audit already excluded the Euclidean decay action \(e^{-aH}\). The two arguments concern different evolutions and should not be conflated.

It also excludes using a bounded multiplication observable, or an operator on a fixed finite-dimensional trial space, as the exact arithmetic generator. A finite-dimensional approximation is still possible if its spectral range grows and the requisite global estimates are proved.

**What remains in scope.** The physical Hamiltonian may still govern preparation and causal evolution. This proposition only prohibits equating that one semibounded generator with the bilateral arithmetic translation action on the exact source image. A different native insertion generator, or an operator action with energy differences, could avoid this specific obstruction. A difference-of-energies representation would require its own sector, state, and OS/source-domain justification; it is not silently supplied by doubling the theory.

## 3. Periodic link rotations also fail

**Proposition 2.** No exact source translation group can satisfy \(V(P)=I\) on \(\mathcal S\) for a nonzero period \(P\).

**Proof.** Take \(P>0\) and choose the support of \(h\) in §2 narrow enough that it and its translate by \(P\) are disjoint. Let
\[
g_\lambda=f_\lambda-U_Pf_\lambda\in\mathcal D^0.
\]
All these tests have a common compact support. Writing \(f_\lambda=e^{i\lambda x}h_\lambda\), where \(h_\lambda\to h\) smoothly, gives
\[
g_\lambda=e^{i\lambda x}
\bigl(h_\lambda(x)-e^{-i\lambda P}h_\lambda(x-P)\bigr).
\]
The profiles in parentheses have uniform smooth bounds and squared \(L^2\) norm \(2\|h_\lambda\|_2^2\). The gamma asymptotic and finite prime bound used for (5) therefore give
\[
Q[g_\lambda]=2\|h\|_2^2\log\lambda+O(1)>0
\]
for large \(\lambda\). But periodicity and (2) give \(Jg_\lambda=0\), a contradiction. ∎

This rules out a single periodic link-rotation action, whenever it descends to the chosen source sector. Every one-parameter subgroup of \(SU(2)\) is periodic; commensurate torus rotations are periodic as well. Many individual link rotations also fail gauge-covariant sector preservation, which must be checked independently. An irrational one-parameter flow in a higher-rank torus need not be periodic and is not excluded by Proposition 2. Nor does this proposition classify general nonperiodic flows on the link configuration manifold.

Together, the two propositions require an unbounded, two-sided, nonperiodic arithmetic generator. These are necessary conditions, not sufficient evidence of an arithmetic match.

## 4. A native unitary flow with the correct weighted adjoint

The finite-slab boundary model supplies a precise framework to search further. Let \(M\) be the compact central-slice link manifold, \(m\) its Haar volume, and
\[
d\nu=w\,dm,\qquad w=Z^{-1}\Omega^2>0,
\qquad \mathcal H=L^2_{\mathrm{cov}}(\nu;\operatorname{End}\mathbb C^N).
\tag{7}
\]
Take a real smooth complete vector field \(D\) on \(M\), with flow \(\Phi_t\). For the covariant sector, require that the flow commute with gauge transformations. The matrix reference fiber is acted on by pullback of its covariant functions. On the full configuration space the same formulas do not need this restriction.

Define the positive Jacobian by
\[
\Phi_t^*\nu=j_t\nu,
\quad
\mathcal U_t B(U)=j_t(U)^{1/2}B(\Phi_t(U)).
\tag{8}
\]
Change of variables proves that \(\mathcal U_t\) is unitary, and the Jacobian chain rule proves the group law. Its derivative on smooth functions is
\[
A_D=D+\tfrac12\operatorname{div}_{\nu}D
=D+\tfrac12\operatorname{div}_mD+D\log\Omega.
\tag{9}
\]
This is skew-symmetric in the weighted inner product. The generator of \(\mathcal U_{-a}\) is selfadjoint by the unitary group construction and agrees on smooth vectors with
\[
G_D=-iA_D.
\tag{10}
\]
This statement uses the actual globally defined flow to select the generator and its domain, rather than inferring selfadjointness from a formal differential expression.

For a Haar-divergence-free link derivative, (10) is \(-i(D+D\log\Omega)\). The \(D\log\Omega\) term is essential; omitting it gives the wrong adjoint in the YM boundary metric. Individual colored link derivatives need not preserve the gauge-covariant sector, while suitably contracted combinations and gauge-equivariant vector fields can be considered there.

### What the weight does and does not add

The unitary identification \(WB=w^{1/2}B\) with Haar \(L^2\) gives the exact cancellation
\[
WG_DW^{-1}=-i\left(D+\tfrac12\operatorname{div}_mD\right).
\tag{11}
\]
Indeed, differentiating \(w^{-1/2}\) cancels the \(\tfrac12D\log w\) term. Thus, for a fixed geometric vector field \(D\), changing the positive Wilson weight does not change the conjugated generator or its spectrum. The state can still affect the chosen source vector, and a vector field derived from dynamics could itself vary with the state. Equation (11) only says that inserting the correct weighted adjoint into an otherwise fixed flow does not by itself create an arithmetic spectral law.

If \(\Phi_P=\mathrm{id}\), its Jacobian also returns to one, so \(\mathcal U_P=I\) even with the nonconstant YM weight. Weighting cannot evade the periodicity obstruction.

This supplies an actual class of native unitary operators and an exact audit of the dynamical information they contain. It does not yet select a nonperiodic vector field with the needed arithmetic structure.

## 5. A generalized source construction that survives the bounded-orbit exclusion

The previous audit rules out \(Jf=\int f(x)V(x)v\,dx\) when \(v\) is an ordinary finite-norm vector. There is a precise extension using a generalized vector of finite order.

Let \(G\) be a selfadjoint operator in the chosen admissible source sector, let \(\eta\in\mathcal H\) be a source seed, and fix \(s\ge0\). Define
\[
J_{G,\eta,s}f
=\widehat f(G)(1+G^2)^{s/2}\eta
:=\bigl[\widehat f(\lambda)(1+\lambda^2)^{s/2}\bigr](G)\eta.
\tag{12}
\]
The expression on the right is the definition. It does not assume \(\eta\) lies in the domain of the separate unbounded factor. Since \(\widehat f\) is Schwartz, the combined spectral multiplier is bounded.

**Proposition 3.** Formula (12) defines a continuous linear map on \(C_c^\infty(\mathbb R)\), hence on \(\mathcal D^0\), satisfying
\[
J_{G,\eta,s}(U_af)=e^{-iaG}J_{G,\eta,s}f.
\tag{13}
\]
Its reflected pairing, in an admissible OS sector, is
\[
\langle Jf,Jg\rangle
=\int\overline{\widehat f(\lambda)}\widehat g(\lambda)\,d\sigma(\lambda),
\qquad
d\sigma(\lambda)=(1+\lambda^2)^s\,d\mu_{\eta}^{G}(\lambda),
\tag{14}
\]
where \(\mu_{\eta}^{G}\) is the finite positive spectral measure of \(G\) at \(\eta\).

**Proof.** The spectral theorem gives (14). On a fixed compact support, integration by parts in the Fourier transform bounds \(\sup_\lambda (1+\lambda^2)^{s/2}|\widehat f(\lambda)|\) by a finite smooth seminorm of \(f\). This proves local test-space continuity, hence continuity on the compact-support test space. The identity \(\widehat{U_af}(\lambda)=e^{-ia\lambda}\widehat f(\lambda)\) proves (13). ∎

In a Hilbert scale for \(G\), this is smearing the generalized vector \(v=(1+G^2)^{s/2}\eta\). It belongs to the negative-order completion, although it may not belong to \(\mathcal H\). The measure in (14) is positive and locally finite, with \(\int(1+\lambda^2)^{-s}d\sigma=\|\eta\|^2\). This allows infinite total mass and therefore escapes the ordinary norm-integrable source-density hypothesis. At \(s=0\), or whenever \(v\) is actually a finite-norm vector, the previous exclusion applies again.

The construction is global before selecting a support length. It proves that a mathematically controlled generalized-source class is available in a fixed Hilbert space. To call it a YM realization, \(G\), its functional calculus, the seed, and the chosen completion must be justified in the admissible YM observable sector. To obtain the arithmetic target, one must still derive
\[
\int\overline{\widehat f}\,\widehat g\,d\sigma=Q(f,g)
\quad\text{for all }f,g\in\mathcal D^0.
\tag{15}
\]
Equation (15) is the unsolved arithmetic identity. Choosing a positive measure from a presumed RH zero spectrum would assume the desired sign. Choosing an arbitrary operator with a prescribed target spectrum would also fail to explain its native YM occurrence. The construction separates those difficult obligations instead of claiming they are settled by the spectral theorem.

### Relation to the compactness route

A positive electric/Sobolev control operator is useful even though it cannot be \(G\). On the compact link manifold, the quadratic form formed from the squared weighted link derivatives is nonnegative and supplies elliptic Sobolev control after summing all link and Lie-algebra directions. Its covariant restriction can furnish the stronger compactly embedded source space of the previous audit.

The Hilbert scale generated by \(G\) alone need not have compact embedding: a flow may leave infinitely many transverse directions uncontrolled. Thus (12) does not automatically establish the stronger Sobolev bounds required for a sequence of source approximants. Those bounds, retained gauge covariance, and any unbounded source relations need separate estimates. The roles of the arithmetic generator and the positive regularity-control operator should stay distinct.

## 6. What has changed in the research choice

The natural first proposals now have explicit outcomes:

| Candidate | Outcome |
|---|---|
| Physical Euclidean transfer \(e^{-aH}\), \(H\ge0\) | Excluded as the arithmetic translation action by norm invariance |
| Real-time group of a semibounded physical/electric Hamiltonian | Excluded as that action by spectral symmetry and high-frequency growth |
| Bounded observable or fixed finite trial-space generator | Excluded by the derivative-to-source norm ratio |
| Periodic link or torus rotation | Excluded by a compactly supported translate-difference test |
| Fixed weighted geometric flow | A genuine unitary action is available, but its generator is conjugate to the unweighted one; weighting alone supplies no arithmetic spectrum |
| Nonperiodic two-sided native insertion generator with a generalized source | Not excluded here; (12) gives a precise global source class once the generator and seed are justified |

The next useful bounded task is to find a concrete gauge-compatible nonperiodic generator from the existing loop/insertion dynamics and test whether its relations determine the spectral pairing (14). Merely picking a complicated vector field is insufficient. The question is whether the dynamics imposes the prime-power/gamma identity, or whether the source seed remains arbitrary enough that the pairing is underdetermined.

If no such relation appears, the honest outcome is that this fixed-flow source class does not yet bridge to arithmetic; a new algebra, source sector, or model would then need an explicit rationale. The causal objective remains available through a separate physical-time dictionary. These exclusions do not prove that no YM realization exists.

## 7. Verification record

The derivations check the translation-generator sign against \(U_af(x)=f(x-a)\), the linear arithmetic reflection and spectral symmetry, the common-support high-frequency estimates, the weighted Jacobian group law, the cancellation under \(W\), and the bounded combined multiplier in (12). The source construction avoids separately applying an unbounded factor outside its domain. No new Monte Carlo experiment was run.

All claims about the finite boundary state and the Weil normalization refer to the [finite-slab note](FINITE_SLAB_REFLECTION_AND_DISCRETE_HIERARCHY_20260924.md), [global source audit](GLOBAL_SOURCE_AND_WARD_IDENTITY_AUDIT_20260924.md), and [self-contained outline](../PROJECT_OUTLINE.md). These are displayed analytical arguments, not an independent review or a claim of novelty.
