# Return to the source states represented by K

3 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual **gpt-6.1-sol (Codex), reasoning effort ultra**, chat `01a19fdd-4e1e-7061-9ec4-141ca78368ce`, turn `01a1a021-8a0a-7033-b8b7-00470aeb19d2`, unique brainstorm history **0002**. A read-only inherited same-model support agent checked the finite overlap/synthesis and normalization equations. This is explanatory same-execution checking, not a new independent assessment.

**Author correction and scope.** The author asks to separate the earlier realization results from the current discussion and to focus on the actual states represented through K. The Hamiltonian decomposition of a prescribed G is an algebraic split; it does not explain a relationship between source-derived states. The prior answer emphasized implementation rather than that relationship. E01/E06's earlier positivity/regularity claims retain their stated evidence and scope, while the current conceptual discussion returns to the source pairing. This note reconstructs known identities and their interpretation; it selects no new energy model or sign mechanism.

## 1. Original source-derived states

Let h_u=L²((0,infinity),du) with the complete canonical theta source Phi. The original two orbital families are
\[
f_i(u)=\frac{\Phi^{(2i)}(u)}{\sqrt{\Phi(u)}},\qquad
g_j(u)=\frac{u^{2j}\sqrt{\Phi(u)}}{(2j)!},\qquad i,j\ge0.
\tag{1}
\]
Their finite-index Hilbert membership and boundary/tail justifications belong to the existing accepted source representation. With c_n the complete source moments and c_n=0 for n<0, integration by parts gives
\[
\boxed{\langle f_i,g_j\rangle=c_{j-i}.}
\tag{2}
\]
At f_0=g_0=sqrt(Phi), the lowest pair coincides. Beyond that the two families in general differ. No claim that either family is an orthonormal basis or a family of energy eigenstates is made.

For increasing finite lists I=(i_1,...,i_r) and J=(j_1,...,j_r), the exact exterior overlap is
\[
\langle f_{i_1}\wedge\cdots\wedge f_{i_r},
g_{j_1}\wedge\cdots\wedge g_{j_r}\rangle
=\det[c_{j_b-i_a}].
\tag{3}
\]
Let M^f_I=(<f_{i_a},f_{i_b}>) and M^g_J=(<g_{j_a},g_{j_b}>). Whenever both wedges are nonzero, their normalized states satisfy
\[
\boxed{
\langle\widehat F_I,\widehat G_J\rangle
=\frac{\det[c_{j_b-i_a}]}
{\sqrt{\det M^f_I\det M^g_J}}.}
\tag{4}
\]
This is a genuine relation between two source-derived many-particle states, with their actual Hilbert norms. It is an inherited exact pairing, not an estimate on its sign.

## 2. What the coefficient transfer represents

For v>0 and orthonormal coefficient labels e_i,
\[
\langle e_i,K_ve_j\rangle
=\frac{c_{j-i}v^{j-i}}{F(v)}
=\left\langle v^{-i}f_i,\frac{v^j}{F(v)}g_j\right\rangle.
\tag{5}
\]
All scales are positive real. To make the relation explicit without an infinite-family boundedness assumption, fix N and define finite synthesis maps
\[
A_{v,N}e_i=v^{-i}f_i,\qquad
B_{v,N}e_j=\frac{v^j}{F(v)}g_j,\qquad 0\le i,j\le N.
\]
Then
\[
\boxed{K_{v,N}=A_{v,N}^\dagger B_{v,N}.}
\tag{6}
\]
Thus K is a matrix of cross-overlaps between the two finite orbital lists. The maps A,B are generally not isometries: A†A and B†B are their respective Gram matrices, not identity. Equation (6) alone is not an assertion that K physically evolves the source state g_j into f_i or into a source-space expansion with coefficients K_ij. In particular,
\[
A_{v,N}K_{v,N}e_j=A_{v,N}A_{v,N}^\dagger B_{v,N}e_j
\]
does not generally equal B_{v,N}e_j. A coordinate/frame conversion would need its actual Gram metric and domain, rather than an implicit orthonormal identification. If A†A is invertible, the actual source-space projection is
\[
P_{\operatorname{ran}A}B=A(A^\dagger A)^{-1}K_{v,N}.
\]
Thus K together with the source Gram matrix determines this projection, rather than itself being a source-space evolution operator.

A decisive distinction for the present discussion is that normalized individual source orbitals do not change with v:
\[
\frac{v^{-i}f_i}{\|v^{-i}f_i\|}=\frac{f_i}{\|f_i\|},\qquad
\frac{v^jg_j/F(v)}{\|v^jg_j/F(v)\|}=\frac{g_j}{\|g_j\|}.
\tag{7}
\]
The same positive rescalings cancel in normalized nonzero source wedges. Activity variation therefore does not, by this identity, describe physical motion of these original normalized wavefunctions. The v-dependent coefficient evolution is an additional realization on a different Hilbert-space encoding.

## 3. States in the coefficient-space realization

The separate coefficient state space is ell²(N0), and
\[
K_ve_j=\frac1{F(v)}\sum_{n=0}^j c_nv^n e_{j-n}.
\tag{8}
\]
If the conditional interpretation is used, the one-particle success probability and normalized output are
\[
p_j(v)=\frac{\sum_{n=0}^j c_n^2v^{2n}}{F(v)^2},\qquad
\boxed{\psi_j(v)=\frac{\sum_{n=0}^j c_nv^n e_{j-n}}
{\sqrt{\sum_{n=0}^j c_n^2v^{2n}}}.}
\tag{9}
\]
For a coefficient occupation state |J>, the corresponding unnormalized output is the wedge of the vectors in (8), with norm squared
\[
p_J(v)=\det[(K_v^\dagger K_v)_{J,J}].
\]
The input e_j is a coefficient label and is not, by its label, a theta energy eigenstate. These are precise relationships within the coefficient-space model, while (1)–(4) describe the original source orbitals. Matching their amplitudes is not a unitary identification of the complete state spaces or their energy observables.

## 4. Reframed energy question

The source energies E_n=pi n² belong to the positive-mode circle operator L_+. They enter Phi, which defines both orbital families (1). A substantive energy explanation would identify how the common source spectrum constrains these two different preparations, their mixed overlaps, and the relevant signed observable. It should not assume that derivative label i, moment label j and energy label n are the same index, or that nonorthogonal orbitals are distinct eigenstates of one self-adjoint operator.

The split G=-iH-R/2 and the chosen bath completion describe ways of realizing a coefficient transfer once K has been prescribed. They do not by themselves supply that source-state comparison. This corrects the emphasis of the preceding discussion without changing any frozen realization theorem. The inherited cross-pairing is already known; writing it again is orientation, not a new RH criterion or gain.

**Continuation:** prioritize the source-state relationship before a further choice of Hamiltonian spectrum. B04's energy-first discussion should consume this clarification alongside Note06 and Handoff08; a change to a genuinely new source-energy representation remains an explicit B03 conceptual revision under the existing contract. No such representation is selected in this note. The author is not required to invent the missing relation; the next conceptual task must investigate it from the canonical source and existing reviewed energy-response dictionary.

Read the [MC02 source-pairing/transfer return](../../../02_fermionic_correlators/notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md) and its [separate review](../../../02_fermionic_correlators/reviews/01_MC02_E01_SEPARATE_REVIEW_20261101.md), [energy-priority Note06](06_ENERGY_PRIORITY_FINITE_LIMITS_AND_INDIRECT_ROUTES_20261103.md), and [Hamiltonian equations Note07](07_HAMILTONIAN_CONSTRUCTION_EQUATIONS_20261103.md). Read also [result summaries](../../../../../../../../result-summaries/README.md), especially [theta/bookkeeping](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and [avoid](../../../../../../../../avoid/README.md), especially [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [reformulations](../../../../../../../../avoid/01_restating_the_target.md), and [joint signed estimates](../../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

Current task readiness stays in the [sole MC08 register](../../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md). Preserve unique brainstorm chat/history 0002 across model changes. Actual configuration here is Sol/ultra; conceptual continuation remains recommended Astra under B04/B03 as scoped above. No frozen input, manuscript, prior chat identity or issued request is edited.
