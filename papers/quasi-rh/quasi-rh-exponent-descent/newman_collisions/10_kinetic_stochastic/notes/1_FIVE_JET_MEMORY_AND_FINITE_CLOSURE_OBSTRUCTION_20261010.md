# Five-jet memory and the finite-closure obstruction

10 October 2026. Prepared with substantial LLM assistance. Model: GPT-6
(Codex); the exact serving variant and configured reasoning effort are not
available in this session and are not inferred. Checks recorded below are
internal checks, not independent mathematical review.

This is the bounded initial scout for program 10 in [Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
Its substantive result is an exact five-jet projection with a positive
memory quadratic form but an unsigned forcing, and a proof that no nonzero
finite-dimensional invariant subspace of the cutoff multiplication generator
exists. Thus a finite Markov or jet closure requires a new restriction or a
measured remainder. Keeping memory does reproduce the genuine heat function.

## 1. Genuine state and domains

Write \(m_t(u)=e^{tu^2}\Phi_e(u)\), with the manuscript's full even theta
kernel, and put
\[
 H_t(z)=\tfrac12\int_{\mathbb R}e^{izu}m_t(u)\,du,
 \qquad \partial_tm_t=\mathsf Lm_t=u^2m_t.
\]
Here \(\mathsf L\) means multiplication by \(u^2\). The state belongs,
for every fixed real time, to
\(L^1\cap L^2\) with every polynomial and fixed exponential weight.
Multiplication by \(u^2\) is positive selfadjoint on
\(D(\mathsf L)=\{f:u^2f\in L^2\}\), but \(e^{t\mathsf L}\) is unbounded on all of
\(L^2\) for \(t>0\). The theta state is an analytic vector in the sense
needed for this explicit evolution. Positivity of the state is not
conservation of its mass.

The Fourier observation and every fixed-time spatial derivative converge
locally uniformly in \((t,z)\), giving
\[
 h_j(t,x)=H_t^{(j)}(x)
 =\tfrac12\int r_j(u;x)m_t(u)\,du,
 \quad r_j=u^j\cos(xu+j\pi/2),\quad
 \partial_th_j=-h_{j+2}.
\tag{1}
\]
The functions \(r_j\) are even. The scale \(L=\kappa/t\) used in the
collision vector is unrelated to this multiplication operator; where both
occur below, the latter is denoted \(\mathsf L\).

For a probability state \(p_t=m_t/Z_t\), \(Z_t=\int m_t\), the exact
equation is
\[
 \partial_tp_t=(u^2-\mu_2(t))p_t,
 \quad \mu_2=\int u^2p_t,
 \quad C_t=H_t/H_t(0),\quad
 \partial_tC_t=-C_t''-\mu_2C_t.
\tag{2}
\]
This is a replicator growth equation. It is not a diffusion generator with
an invariant probability measure. If (2) is projected, its time-dependent
blocks require a chronological propagator, rather than the fixed
exponential used next.

## 2. An exact five-channel memory system

Fix one height \(x_*\ne0\), a cutoff \(U>0\), and work in the real Hilbert
space \(\mathcal H_U=L^2([-U,U],du)\). All projections in this section
are fixed in time and height. Let \(V\) be the span of \(r_0,\ldots,r_4\)
at \(x_*\), and let \(P\) be its orthogonal projection, \(R=I-P\).
The five functions are independent: an analytic identity between a
polynomial times \(\cos(x_*u)\) and a polynomial times \(\sin(x_*u)\)
would give a rational expression for \(\tan(x_*u)\), which is impossible
unless both polynomials vanish. Thus the Gram matrix
\(S_{jk}=\langle r_j,r_k\rangle\) is positive definite.

For \(f_t=m_t\mathbf1_{[-U,U]}\), set \(a_t=Pf_t\), \(b_t=Rf_t\),
and define the bounded blocks
\[
 A=P\mathsf LP|_V,\quad B=P\mathsf LR,\quad
 C=R\mathsf LP|_V=B^*,\quad D=R\mathsf LR|_{R\mathcal H_U}.
\]
Every block norm is at most \(U^2\). Eliminating \(b\) gives exactly
\[
 \dot a_t=Aa_t+Be^{tD}b_0
       +\int_0^tK(t-s)a_s\,ds,
 \qquad K(\tau)=Be^{\tau D}C.
\tag{3}
\]
No noise, memory, or initial unresolved component has been dropped. The
raw jets are \(h_j^U=\langle r_j,a_t\rangle/2\). One can recover the
resolved state as \(a_t=2\sum_j r_j(S^{-1}h^U)_j\); consequently the
Euclidean matrix for (3) must retain the Gram factors. Positivity statements
are made in the Hilbert metric, equivalently the \(S^{-1}\) metric on jets.

There is a useful exact additional identity:
\[
 \langle v,K(\tau)v\rangle
   =\|e^{\tau D/2}Cv\|^2\ge0\quad(\tau\ge0),
 \qquad 0\le K(\tau)\le e^{\tau U^2}BB^*
\tag{4}
\]
in the quadratic-form sense. The final upper bound uses
\(0\le D\le U^2I\). This is an amplifying memory, not damping. It
does not assign a componentwise sign to \(K(\tau)a_s\), or any sign to
\(Be^{tD}b_0\).

Since \(\mathsf Lr_j=-r_{j+2}\) for \(j\le2\), the first three
raw-jet rows have no hidden contribution:
\[
 \dot h_0^U=-h_2^U,\qquad
 \dot h_1^U=-h_3^U,\qquad
 \dot h_2^U=-h_4^U.
\tag{5}
\]
Hidden forcing and memory first enter the third and fourth derivative rows,
through \(r_5,r_6\). This locates the missing information precisely for
the fourth-jet collision test. At \(h_0^U=h_1^U=0\), neither (4) nor
(5) fixes the signs or relative size of \(h_2^U,h_3^U,h_4^U\).

## 3. A finite exact closure is impossible in this architecture

Suppose a nonzero finite-dimensional \(V_0\subset\mathcal H_U\) were
invariant under multiplication by \(u^2\). The restriction of the
selfadjoint bounded operator to \(V_0\) is a real symmetric finite matrix
and has an eigenvector \(f\ne0\). Then \((u^2-\lambda)f(u)=0\)
almost everywhere. The level set \(u^2=\lambda\) has Lebesgue measure
zero; hence \(f=0\), a contradiction. This proves the claimed obstruction
for every finite orthogonal resolved subspace, not only the five jets.

It does not prohibit a nonorthogonal state-dependent closure on one special
arithmetic trajectory, an infinite hierarchy, or atomic spectral models.
It does show why replacing (3) by \(\dot a=Aa\) is an additional
approximation rather than a derived finite heat model.

The manuscript's strictly positive decreasing kernel
\(q=(e^{-\cosh u})^{(4)}+324e^{-\cosh u}\) has a positive all-real
threshold. It satisfies the same equations (1)–(5), with the same memory
positivity. Its role is a generic-kernel control; it is not the theta state.
The genuine adjacent packet separately defeats a diagonal energy lower
bound, and the complete multiplicative twist defeats a bound uniform over
all twists. Neither control supplies an actual theta collision.

## 4. Tail and normalizer payment

For \(r\ge0\), the theta series gives the convenient bound
\[
 0<\Phi(r)\le32\exp(9r-\pi e^{4r}).
\]
Indeed, drop the negative term in each summand and use
\(2\pi^2\sum n^4e^{-\pi(n^2-1)}<32\). On
\(0\le t\le T=1/20\), \(|\Im z|\le Y=1\), and \(U\ge1\), put
\[
 d_j(U)=4\pi e^{4U}-2TU-10-j/U.
\]
For \(0\le j\le6\), this is positive and the logarithmic derivative
of the positive tail integrand is at most \(-d_j(U)\) beyond \(U\).
Therefore
\[
 |H_t^{(j)}(z)-(H_t^U)^{(j)}(z)|
 \le E_j(U):=
 \frac{32U^j e^{TU^2+10U-\pi e^{4U}}}{d_j(U)}.
\tag{6}
\]
This includes both spectral tails and the factor \(1/2\) in the full
Fourier integral. The cutoff is held fixed in all derivatives.

On any closed rectangle and its required complex disks where the
manuscript's \(A_t\) is analytic and nonzero, define
\(M_k=\sup|\partial_z^k(A_t^{-1})|\). Then the normalized jet payment is
\[
 |Q_t^{(j)}-(H_t^U/A_t)^{(j)}|
 \le\sum_{k=0}^j{j\choose k}M_kE_{j-k}(U).
\tag{7}
\]
In the shrinking sector, one must choose \(U\) using (7), including the
possibly tiny normalizer; a small unnormalized tail alone is insufficient.
No large-height numerical enclosure of \(M_k\) is asserted here.

Writing \(b=\partial_x\log A_t\), \(a_0=\partial_t\log A_t\), the
genuine normalized equation is
\[
 Q_t{}_t=-Q_t''-2bQ_t'-(a_0+b_x+b^2)Q_t.
\tag{8}
\]
Thus the observed pair is
\((H_t/(2A_t),2(H_t'-bH_t)/(LA_t))\); the amplitude drift is present.
Higher jets use the full product rule in (7). The measured fourth-jet
payment from Note 13 remains required for any eventual sign claim.

## 5. Result and continuation

The cutoff model is a genuine exact realization with a paid removal formula.
The new obstruction concerns finite invariant closure, while (4) identifies
what its positive memory actually controls. The missing arithmetic input is
a candidate-conditioned estimate for the \(r_5,r_6\) forcing, or for an
infinite resolved hierarchy, strong enough to affect the signed threshold
test. A norm estimate of size \(e^{tU^2}\) does not bridge Note 13's
derivative-probe scale deficit.

The most useful next bounded task is to express the two forcing channels
through theta modularity and test whether the resulting conditional residual
has a signed relation to \(h_2,h_3,h_4\). Without such a restriction this
program stops at representation and a scoped obstruction.

For the general memory formalism see Darve, Solomon and Kia,
[Computing Generalized Langevin Equations and Generalized Fokker–Planck Equations](https://mc.stanford.edu/cgi-bin/images/c/c1/Darve_pnas_2009.pdf).
Equations (3)–(5) above are derived directly for this bounded multiplication
operator and do not import a theta theorem from that paper. No collision
exclusion or RH conclusion is obtained.
