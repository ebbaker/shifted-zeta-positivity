# Fermionic transfer explained from one particle to all determinant orders

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Chat `01a19a6a-7223-7c00-801b-172a5a8ff81b`; [public history](chat-histories/index.json).

**J-B10 — B, recommended Astra:** conceptual explanation in response to the author's questions. This reuses the exact [MC02 return](../02_fermionic_correlators/notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md) and its [separate internal review](../02_fermionic_correlators/reviews/01_MC02_E01_SEPARATE_REVIEW_20261101.md). No technical continuation or simulation is selected. The construction is an exact representation, with no new amplitude inequality or novelty claim.

The central idea is to use the theta coefficients as a rule for transferring one particle between modes. Apply that same rule to several identical fermions. Fermionic antisymmetry combines the one-particle transfers into determinants, and those determinants are precisely the coefficient minors already studied in the Jensen program.

## One particle and a transfer rule

Let |j> denote a particle occupying mode j, with j=0,1,2,... . These modes label a basis; identifying them with positions in an apparatus would be an additional physical realization. A one-particle state is a square-summable superposition
\[
|\psi\rangle=\sum_{j\ge0}\psi_j|j\rangle.
\]
For a normalized state, sum |psi_j|^2=1. The one-particle Hilbert space is thus H=ell^2(N_0).

A linear transfer K is specified by the amplitudes K_ij=<i|K|j>. Consider a rule with real nonnegative left-step weights p_n:
\[
K|j\rangle=p_0|j\rangle+p_1|j-1\rangle+\cdots+p_j|0\rangle.
\]
Steps beyond the left boundary contribute zero. In the basis ordered 0,1,2,...,
\[
K=\begin{pmatrix}
p_0&p_1&p_2&p_3&\cdots\\
0&p_0&p_1&p_2&\cdots\\
0&0&p_0&p_1&\cdots\\
\vdots&&\ddots&\ddots&\ddots
\end{pmatrix}.
\]
It is Toeplitz because an entry depends only on the displacement j-i. The amplitudes can also be viewed as classical left-step weights with boundary loss. That analogy must not identify p_n with quantum measurement probabilities: quantum probabilities use squared amplitudes, with the appropriate normalization and physical operation specified. The construction below uses a contraction, not a unitary evolution.

The one-particle vector |0> means a particle at mode zero. The empty many-particle state is a different vector, denoted |Omega> below. Boundary attenuation in this transfer does not add a transition from a one-particle sector into the vacuum sector.

## How the complete theta source fixes the weights

At source heat time zero, keep the full canonical source
\[
\Phi(u)=\sum_{m\ge1}(2\pi^2m^4e^{9u}-3\pi m^2e^{5u})e^{-\pi m^2e^{4u}},
\qquad
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du.
\]
Set c_n=0 for negative integer indices and F(w)=sum c_n w^n. For any fixed v>0,
\[
p_n(v)=\frac{c_nv^n}{F(v)},\qquad p_n>0,\qquad\sum_{n\ge0}p_n=1.
\]
F is entire, so the denominator is finite and positive. The parameter v rescales the coefficients; it is not source heat time, thermal inverse temperature, or Mellin tilt. One may take v=1 to understand the construction.

Define the backward shift by S|0>=0 and S|j>=|j-1> for j>=1. Then
\[
K_v=\sum_{n\ge0}p_n(v)S^n=\frac{F(vS)}{F(v)},
\qquad
\langle i|K_v|j\rangle=\frac{c_{j-i}v^{j-i}}{F(v)}.
\]
The operator series converges absolutely in norm, and
\[
\|K_v\|\le\sum_{n\ge0}p_n\|S^n\|\le1.
\]
This proves existence and boundedness independently of any desired minor sign. In particular, there is one well-defined transfer for all subsequent finite particle sectors.

## Two identical fermions produce a determinant

The defining statistical rule is antisymmetry under exchange. For distinct ordered modes j_1<j_2, the normalized two-fermion occupation state is
\[
|j_1,j_2\rangle
=\frac{|j_1\rangle\otimes|j_2\rangle-|j_2\rangle\otimes|j_1\rangle}{\sqrt2}.
\]
If both modes coincide, this vector is zero. This is the exclusion rule for a single fermionic mode. The state is denoted |j_1> wedge |j_2>. The ordered occupation convention fixes the sign: exchanging the written order multiplies the vector by -1.

The free two-particle transfer applies K to each factor, giving K tensor K restricted to antisymmetric states, denoted wedge^2 K. Expanding the two antisymmetric states gives
\[
\begin{aligned}
\langle i_1,i_2|\bigwedge^2K|j_1,j_2\rangle
&=K_{i_1j_1}K_{i_2j_2}-K_{i_1j_2}K_{i_2j_1}\\
&=\det\begin{pmatrix}K_{i_1j_1}&K_{i_1j_2}\\K_{i_2j_1}&K_{i_2j_2}\end{pmatrix}.
\end{aligned}
\]
The normalization factors cancel exactly; there is no extra 2!. The minus sign is forced by exchange. Free here means that the same one-particle map acts on each factor, with no added interparticle potential. Antisymmetry still produces exchange correlations.

For initial occupied modes {1,2} and final modes {0,1},
\[
\langle0,1|\bigwedge^2K|1,2\rangle=p_1^2-p_0p_2.
\]
The first product assigns 1 to 0 and 2 to 1; the second assigns 2 to 0 and 1 to 1. These are two assignments in the antisymmetric amplitude, not independently observed trajectories of labeled particles. The exchange assignment enters with a minus sign.

For theta the expression is
\[
p_1^2-p_0p_2=\frac{v^2}{F(v)^2}(c_1^2-c_0c_2)
=\frac{v^2}{F(v)^2}D_{2,1}.
\]
This is the simplest illustration of determinant positivity becoming a fermionic-amplitude question.

Positive p_n alone do not settle the sign. The frozen MC02 relaxation uses F_*(w)=1+w+2w^2 and v=1, hence p=(1/4,1/4,1/2), for which the amplitude is -1/16. This is an exact illustrative non-theta transfer, not a source counterexample or new computation. It fails the unchanged canonical coefficient reconstruction. A negative amplitude is physically permissible; its squared modulus is nonnegative. Squaring would erase the sign information being studied.

## Arbitrary particle number and Fock space

For strictly increasing lists I=(i_1,...,i_r) and J=(j_1,...,j_r), antisymmetrization over all assignments gives
\[
\langle I|\bigwedge^r K|J\rangle
=\sum_{\pi\in S_r}\operatorname{sgn}(\pi)\prod_{a=1}^rK_{i_a,j_{\pi(a)}}
=\det[K_{i_a,j_b}].
\]
This is the finite Slater-determinant rule. The exchange algebra and related Wick determinant are standard; [Alexandrov-Zabrodin, Sections 2.1 and 2.3](https://arxiv.org/pdf/1212.6049v3) provide the established fermionic context. The finite empty-vacuum wedge derivation here requires neither a filled Dirac sea nor an infinite-current construction.

Fock space collects all particle numbers:
\[
\mathcal F_-(H)=\mathbb C|\Omega\rangle\oplus H\oplus\bigwedge^2H\oplus\bigwedge^3H\oplus\cdots,
\qquad
\Gamma(K_v)=1\oplus K_v\oplus\bigwedge^2K_v\oplus\cdots.
\]
Each block preserves particle number. Since ||wedge^r K_v||<=||K_v||^r<=1, the direct sum is bounded on the full Fock space. This includes every finite sector; an infinitely occupied sea is not introduced.

Substituting the theta matrix elements and factoring positive row and column scales gives the decisive formula
\[
\boxed{
\langle I|\Gamma(K_v)|J\rangle
=\frac{v^{\sum J-\sum I}}{F(v)^r}
\det[c_{j_b-i_a}].
}
\]
For consecutive configurations, writing A_{r,k}(v) for this occupation amplitude (distinct from earlier normalized signed expectations),
\[
A_{r,k}(v):=\langle0,\ldots,r-1|\Gamma(K_v)|k,\ldots,k+r-1\rangle
=\frac{v^{rk}}{F(v)^r}D_{r,k}.
\]
Thus r=3 really is the three-particle sector of the same transfer whose four-particle sector contains D_{4,k}. General ordered lists include all the nonrectangular minors as well.

## Why this reaches RH and what it does not supply

The exact coefficient identity is
\[
F(z^2)=\frac18\xi\bigl((1+z)/2\bigr).
\]
For this entire function of order one half, the classical coefficient-total-positivity characterization identifies negative-real zeros of F with nonnegative minors of its Toeplitz matrix. The scaling agrees with [Katkova, equations (3)–(6), Definition 2, Theorem ASWE and Theorem C](https://arxiv.org/html/math/0505174v1). The coefficient scaling there is b_n=8*4^n*c_n, which preserves all minor signs. Selected primary statements were rechecked, not their original proofs re-audited.

Consequently, in the fixed increasing-order occupation basis,
\[
\mathrm{RH}\quad\Longleftrightarrow\quad
\langle I|\Gamma(K_v)|J\rangle\ge0
\quad\text{for all finite }r\text{ and all increasing }I,J.
\]
One fixed v>0 suffices. This sign condition depends on the specified basis and phase convention; it is not an invariant requirement that every physical transition amplitude must have positive phase. Nor is it ordinary nonnegativity of probabilities or positive semidefiniteness of a Hamiltonian.

The exact K_v is non-self-adjoint. On span{|0>,|1>} its invariant restriction is
\[
\begin{pmatrix}p_0&p_1\\0&p_0\end{pmatrix},\qquad p_1>0.
\]
It is a nontrivial Jordan block, so no positive-definite inner product retaining these states makes this exact transfer self-adjoint. This rules out the attempted identification with one self-adjoint equilibrium transfer e^(-tH) in that class. It does not exclude other realizations or total positivity; even the Gaussian total-positive example has the same obstruction. An explicit laboratory implementation is not supplied by the algebraic construction.

The gain is that one bounded, fully specified operator contains every coefficient-minor question. Its missing theorem would explain from the canonical theta weights why all the exchange cancellations have the required signs, or supply a quantitative relation between the relevant amplitudes. Contraction only controls magnitudes. In particular the original r=3 Gaussian comparison asks for
\[
\frac{A_{3,k-1}(v)A_{3,k+1}(v)}{A_{3,k}(v)^2}\le\frac{k}{k+3},
\]
which does not follow from |A_{3,k}|<=1. Changing v has not been identified with changing real Mellin tilt s.

The continuous source connection also remains exact: f_i=Phi^(2i)/sqrt(Phi) and g_j=u^(2j)sqrt(Phi)/(2j)! satisfy <f_i,g_j>=c_(j-i). Their exterior overlaps give the same minors. Because the two families differ, this is a signed overlap rather than a squared norm; full endpoint evenness and tails are needed for the integration-by-parts identity.

## Clarification of the quantifier on v

2 November 2026. Prepared for Edward Baker with substantial LLM assistance, actual gpt-6-astra / xhigh, in response to the author's follow-up.

**One fixed finite v_0>0 suffices**, for example v_0=1. The positivity statement must hold for every finite particle number and every pair of ordered occupation lists at that value. It need not be proved separately throughout the v family.

For each fixed r,I,J, write the transfer amplitude as A_v(I,J). The exact scaling gives
\[
A_v(I,J)=
\left(\frac{F(v_0)}{F(v)}\right)^r
\left(\frac{v}{v_0}\right)^{\sum J-\sum I}
A_{v_0}(I,J),\qquad v,v_0>0.
\]
The multiplier is strictly positive. Hence all finite amplitude signs are independent of positive v, and the following statements are equivalent: RH; the required all-sector positivity at one chosen positive v; and that positivity at every positive v. No uniform-in-v estimate is required. This uses finite matrix-element scaling, not an asserted bounded similarity between infinite-dimensional operators.

The endpoint v=0 is excluded: K_0=I, which is automatically nonnegative in every occupation sector and has lost the off-diagonal coefficient information. Positivity only in the v-to-zero limit therefore would not suffice.

## Interpretation and standing controls

Read with the [result index](../../../../../../result-summaries/README.md), especially [the theta physical assessments](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../../avoid/README.md), especially [reformulations](../../../../../../avoid/01_restating_the_target.md), [joint signed estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). The representation is not additional evidence for RH.

The existing [collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md) can also admit generic coefficient-transfer encodings when their positive generating sums converge. Their unchanged canonical theta reconstruction fails; finite-square variants may additionally fail the endpoint conditions needed for the continuous-orbital formula. No uncomputed control-amplitude sign is assigned. The exact polynomial example above specifically screens the claim that nonnegative one-particle weights and contraction bounds force fermionic signs.

**Next: [B] J-B10 — Astra**, continue the author's questions. The canonical return, review, branch registers and other investigations remain unchanged.
