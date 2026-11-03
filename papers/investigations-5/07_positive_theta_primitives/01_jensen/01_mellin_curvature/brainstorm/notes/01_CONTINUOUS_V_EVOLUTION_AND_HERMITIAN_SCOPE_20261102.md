# Continuous evolution of the theta fermionic transfer

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual recorded model **gpt-6-astra (Codex)**, effort **xhigh**. Chat 01a19d42-585c-73b1-bb49-1faaad2b400f. Direct algebraic discussion and same-assistant checks; no separate review, new theta sign estimate, or branch execution milestone.

This continues [the basic transfer explanation](../03_FERMIONIC_TRANSFER_FROM_BASICS_20261102.md). The author's questions concern physics language, finite-time continuous evolution, Hermitian coordinates, and differentiation in v. The most concrete answer is an exact nonautonomous evolution in v, locally on the infinite space and globally on each finite mode truncation. A fixed positive metric cannot make its generator Hermitian. Enlarging the system is a distinct possibility.

## Exact evolution in v

Keep H=ell^2(N_0), S|0>=0, S|j>=|j-1>, and
\[
K_v=F(vS)/F(v),\qquad F(w)=\sum_{n\ge0}c_nw^n,\quad c_n>0.
\]
The full unchanged theta source fixes c_n. Operator power series and their derivatives converge in norm on compact v intervals. K_0=I, even though the all-minor sign criterion at v=0 is vacuous.

Where F(vS) has a bounded inverse, direct differentiation gives
\[
\frac{dK_v}{dv}=G(v)K_v,\qquad
G(v)=S F'(vS)F(vS)^{-1}-\frac{F'(v)}{F(v)}I. \tag{1}
\]
All these operators commute. Thus K_v is exactly the evolution from v=0; the intermediate propagator is K_b K_a^{-1}. Endpoint contraction and positive entries do not by themselves imply corresponding properties for these intermediate propagators.

An explicit sufficient local condition is F(v)<2c_0:
\[
\|(F(vS)-c_0I)/c_0\|\le (F(v)-c_0)/c_0<1.
\]
More generally, a zero-free neighborhood of the closed disk |w|<=v gives an analytic inverse and logarithm. On H_N=span{|0>,...,|N>}, S is nilpotent and F(vS) is invertible for every finite positive v, since its diagonal is c_0.

On each finite particle sector, differentiation commutes with the exterior-power construction:
\[
\partial_v\bigwedge^r K_v
=d\Gamma_r(G(v))\bigwedge^rK_v,\qquad
d\Gamma_r(G)=\sum_{\ell=1}^rG^{(\ell)}.
\]
This is a number-preserving quadratic fermionic generator. The full Fock generator generally is unbounded; the finite-particle domain is the natural starting domain. No bounded full-Fock generator is asserted.

## Small v and the logarithmic coefficients

Write, within the zero-free Taylor disk,
\[
\log(F(w)/c_0)=\sum_{n\ge1}b_nw^n.
\]
Then
\[
G(v)=\sum_{n\ge1}n b_n v^{n-1}(S^n-I),\quad
b_1=\alpha=c_1/c_0,\quad
b_2=\beta=c_2/c_0-\alpha^2/2. \tag{2}
\]
In particular,
\[
G(0)=\alpha(S-I),\qquad
G(v)=\alpha(S-I)+2\beta v(S^2-I)+O(v^2).
\]
The leading term is continuous directed nearest-neighbor hopping with killing at the left boundary. Its finite-time transfer is exp(alpha t(S-I)). That exponential agrees with K_v only to first order in general; F(w)=c_0 exp(alpha w) gives an exact comparison model.

Equation (2) identifies the precise issue for a classical jump interpretation: its off-diagonal coefficients must be nonnegative. For example, beta<0 would produce a negative two-step infinitesimal weight. No numerical value or new certified sign for theta beta is claimed here. The elementary positive-factor model F(w)=1+aw, a>0, already has beta=-a^2/2; positive endpoint transfers and total nonnegativity do not guarantee positive intermediate jump rates for this particular v path.

A distinct autonomous interpolation to a fixed sufficiently small v_* is
\[
U(t)=\exp(tB),\quad B=\log F(v_*S)-\log F(v_*)I,\quad U(1)=K_{v_*}.
\]
Choose the analytic logarithm near the full closed disk, consistent with log c_0 at zero. Its symbol is a fractional power of F(v_*z)/F(v_*); the shift functional calculus bounds ||U(t)||<=1 for t>=0. This interpolation need not equal K_{t v_*}, need not have nonnegative entries at intermediate t, and is not a Hermitian Hamiltonian construction.

## The scaling parameter as a field conjugate to displacement

With tau=log v and mu(v)=sum n p_n(v)=vF'(v)/F(v),
\[
\partial_\tau p_n=(n-\mu)p_n,\qquad
\partial_\tau\mu=\operatorname{Var}_{p(v)}n.
\]
Thus v is naturally an activity weighting jump length. It is not already physical time, source heat time, or Mellin tilt.

On the finite-support core, with N|j>=j|j>,
\[
v\partial_vK_v=K_vN-NK_v-\mu(v)K_v. \tag{3}
\]
This is a rescaling commutator plus normalization. The corresponding diagonal similarities are exact on finite cutoffs; no bounded invertible similarity on the infinite Hilbert space is asserted.

Every fixed ordered occupation amplitude still has its v dependence given by a strictly positive scalar times the same coefficient minor. The v path supplies an evolution equation but does not change the original sign question.

## Why fixed coordinates cannot make the exact generator Hermitian

The invariant two-mode restriction of (1) is exactly
\[
G(v)|_{H_1}=
\begin{pmatrix}
-F'(v)/F(v)&\alpha\\
0&-F'(v)/F(v)
\end{pmatrix},\qquad \alpha>0. \tag{4}
\]
Let lambda=-F'(v)/F(v). Then (G-lambda)|0>=0 and (G-lambda)|1>=alpha|0>. Symmetry in any positive-definite inner product containing both states would imply
\[
\alpha\langle0,0\rangle
=\langle0,(G-\lambda)1\rangle
=\langle(G-\lambda)0,1\rangle=0,
\]
a contradiction. This also applies to the original K_v block with alpha replaced by p_1(v). A fixed invertible coordinate change cannot remove a Jordan chain.

Conventional real-time evolution has an anti-Hermitian generator -iH; imaginary-time evolution has generator -H. Multiplication by i or a nonzero time-rescaling factor does not remove the Jordan obstruction. A time-dependent real-time Hermitian Hamiltonian still has a unitary endpoint and cannot give K_v directly on this same state space.

Time-dependent coordinate changes add a connection term. Where K_v is invertible, psi=K_v chi even makes chi'=0. That formal simplification changes the metric/observables and does not establish a fixed-metric closed quantum realization. Products of time-dependent imaginary-time Hermitian transfers need not be self-adjoint at their endpoint; the single-exponential obstruction does not exclude that larger class.

## Large v and the limits of a bounded generator

For fixed finite i,j, K_v(i,j) tends to zero as v tends to infinity: its numerator is a fixed polynomial term and F(v) exceeds every fixed polynomial eventually. K_v therefore tends strongly to zero, using ||K_v||<=1 and density of finite-support vectors. Nevertheless ||K_v||=1 for each finite v, because the normalized backward-shift eigenvectors with real eigenvalue lambda approaching 1 give eigenvalues F(v lambda)/F(v) approaching 1. This is not convergence in operator norm.

If F has a zero w_0 and v>|w_0|, then lambda=w_0/v lies in the open unit disk and
\[
S(1,\lambda,\lambda^2,\ldots)=\lambda(1,\lambda,\lambda^2,\ldots).
\]
Consequently K_v has a nontrivial kernel. The inverse formula (1) cannot continue globally across all v as a bounded generator with integrable norm on every finite interval: such finite-time evolutions are invertible. This does not exclude unbounded-generator evolutions, dilations, or finite-cutoff models.

## Two physical alternatives

A positive planar directed network with ordered sources and sinks expresses every minor as a sum of weights of vertex-disjoint paths. Fomin–Zelevinsky, Planar networks, Lemma 1 and Corollary 2 give this standard mechanism. A local layer T_a=(I+aS)/(1+a), a>=0, permits only staying or moving one site, and cannot allow ordered paths to overtake without collision. Products preserve total nonnegativity. Constructing exact theta weights from such layers is an RH-strength task; taking positive factors from an assumed negative-real zero factorization merely restates RH. Chin's one-dimensional Gaussian-propagator sign argument is related physics background, not a theorem for the theta long-jump kernel.

For every fixed v, contraction also gives a conventional quantum realization on a larger Hilbert space. With D_K=(I-K* K)^(1/2),
\[
U_K=\begin{pmatrix}K&D_{K^*}\\D_K&-K^*\end{pmatrix}
\]
is unitary (Robinson, Theorem 2). A self-adjoint logarithm of U_K gives U_K=exp(-iT H_total) for any T>0. Preparing in the first copy of H and projecting back produces K. This is a compression or conditioned amplitude, not a change of coordinates. It provides one endpoint at a time, not a common local Hamiltonian for the full v family. No locality, arithmetic simplicity, or occupation-amplitude sign follows from this generic dilation.

## Classification and controls

Read the [result index](../../../../../../../result-summaries/README.md), especially [theta physical assessments](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../../../avoid/README.md), especially [reformulations](../../../../../../../avoid/01_restating_the_target.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). These are evolution identities, structural questions, and explicitly scoped obstructions; no all-minor estimate has been obtained.

The [standing controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md) screen the generic mechanisms. F_*(w)=1+w+2w^2 gives a bounded transfer, the same local differentiability/invertibility, and a unitary dilation, but its two-fermion amplitude at v=1 is -1/16. It fails unchanged theta reconstruction. Gaussian, Euler-factor, reflected and smooth positive-primitive sources share generic coefficient evolution where their sums converge; they do not inherit any unproved theta generator estimate. Weighted-square and finite-prime changes fail unchanged theta weights and may also fail full continuous-orbital endpoint conditions. A positive-time collision alone does not assign a time-zero minor sign. Merely naming the canonical source is not a quantitative discriminator.

[Primary-source inspection record](../../../../references/11_FERMIONIC_EVOLUTION_SOURCES_20261102.md). Discussion remains in this brainstorm; frozen MC02 results and shared research-progress registers are unchanged.
