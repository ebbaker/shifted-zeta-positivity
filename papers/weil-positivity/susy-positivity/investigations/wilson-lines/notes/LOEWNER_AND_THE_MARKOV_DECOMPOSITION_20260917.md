# Where the field strength is, a Loewner proposal, and the Markov decomposition of the transfer

**Author: Claude Fable 5.1 (Anthropic), model `claude-fable-5-1`.** 17 September
2026 (New York). Research note, written at Edward Baker's direction after the
[review of the same day](../reviews/review_claude-fable-5-1_2026-09-17.md), in
answer to three questions he put against manuscript 0.8: what exactly is abelian
in the shift flow; whether the flatness of Section 9 really rules out a curved
realization; and whether a Loewner-type evolution could construct the path
independently, with positivity coming from conformality rather than from
arithmetic.

**No manuscript change has been made.** Section 8 lists what this note
recommends. Sections 1--3 are corrections and framing; Section 4 is the one
piece of new mathematics, a decomposition of the transfer kernel into an
explicit positive part and an explicit rank-two correction, verified in
Section 5; Section 6 says what it does to the Loewner idea.

---

## 0. Summary

1. **What is abelian, precisely.** At fixed $L$ every $V_{\omega,L}$ and
   $G_{\omega,L}$ is the compression to $I_L$ of a function of the single
   operator $D=-i\partial_x$, realized causally: the $\omega$-flow is
   *translation-invariant along the line*, so its generators are all functions
   of the line momentum and commute. That is a selection on realizations --- the
   $F$-insertions implementing $\omega$ must act, after transport, as functions
   of one operator, uniformly along the line --- and not a no-go for non-abelian
   theories. The two-parameter algebra is **not** abelian: $[G,B_L]=-B_LG\neq0$,
   so transport along a path in $(\omega,L)$, including any critical path, is a
   genuinely ordered product; it is path-independent because the connection is
   flat.

2. **Flatness is a tautology, and the field strength was being sought in the
   wrong object.** For any single-valued family $V$ with $dV=\mathcal A\,V$ the
   curvature of $\mathcal A$ annihilates $V$, on the two-parameter slice and on
   the whole space of contours alike, and fibre deformations act as symmetries.
   In the non-Abelian Stokes variation $F_{\mu\nu}$ appears as the *coefficient*
   of the deformation --- the transported insertion along the line --- not as the
   curvature of the connection on deformation space. The object to match with a
   transported $F$-insertion is $G_{\omega,L}$ itself, nonzero and carrying the
   primes; the object to match with the endpoint term $A_\mu\delta x^\mu$ is
   $B_L$. Manuscript Section 9.2 should be reread in that light: it correctly
   finds zero where zero was guaranteed, and the constraints on a realization
   are the two of item 1 rather than the absence of curvature.

3. **Loewner evolution has the right shape in four respects and a fatal one in
   the naive form.** Whole-plane Loewner time is log-conformal-radius, the
   manuscript's $x=\log r$; its symmetry group is the Weil form's; $L$ is the
   modulus of the annulus it sweeps; the Loewner equation is a tip equation with
   a scalar driving function, the shape of Proposition 9.1; and the chain is a
   path-ordered product in the Witt algebra. But the expected composition
   operator of a rotation-invariant random conformal map on *analytic* functions
   is the pure dilation $h\mapsto h(\phi'(0)z)$, for every map (Lemma 3.1), so a
   realization must act on non-analytic observables, whose radial Markov kernel
   is not translation-invariant. The identification "expected composition
   operator $=$ transfer" is dead on arrival; what survives is stated in Section 6.

4. **The transfer is a completely monotone kernel times a rank-two rational
   factor, and everything is elementary** (Section 4, proved and verified).
   With $\Lambda(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u)$, $s=\tfrac12+p$,
   $a=\tfrac12-\omega$, $b=\tfrac12+\omega$:
   \[
    K_\omega=R_\omega\,\widetilde K_\omega,\qquad
    \widetilde K_\omega(p)=\frac{\Lambda(s-\omega)}{\Lambda(s+\omega)},\qquad
    R_\omega(p)=\frac{(p+a)(p-b)}{(p+b)(p-a)}
    =1-\frac{4\omega b}{p+b}-\frac{4\omega a}{p-a},
   \]
   and $\widetilde K_\omega$ is **completely monotone on $p>b$**, hence the
   Laplace transform of a **positive measure**
   \[
    \widetilde k_\omega=k^\Gamma_\omega*\sum_{n\geq1}\widetilde c_n\,\delta_{\log n},
    \qquad
    k^\Gamma_\omega(x)=\frac{2\pi^\omega}{\Gamma(\omega)}\,(2\sinh x)^{\omega-1}e^{x/2},
    \qquad
    \widetilde c_n=n^{\omega-\frac12}\prod_{p\mid n}\big(1-p^{-2\omega}\big)>0 .
   \]
   The causal kernel of the transfer is therefore
   $k_\omega=\widetilde k_\omega-4\omega b\,e^{-b\cdot}*\widetilde k_\omega
   -4\omega a\,e^{a\cdot}*\widetilde k_\omega$: a positive measure minus two
   exponential smoothings of itself. **The entire non-Markov content of the
   shifted transfer is the $s(s-1)$ of $\xi$** --- the pole of $\zeta$ and the
   trivial factor, the two endpoint modes $r^{\pm\frac12}$ of the ray shifted by
   $\omega$. The archimedean piece is the law of a squared radius ratio,
   $(r_1/r_2)^2\sim\mathrm{Beta}(\tfrac14-\tfrac\omega2,\omega)$: the quarter of
   the delay test is a Beta parameter. The prime atoms carry the weights
   $\widetilde c_n$, which are $2\omega\Lambda(n)n^{-1/2}$ to first order and are
   the abelian monodromies $p^{\omega}$ per traversal of the local Euler factor.

5. **Consequences.** $V_{\omega,L}$ can be assembled *exactly* from elementary
   functions and the integers $n<e^L$, with no $\xi$ and no zeros, just as $Q_L$
   is assembled from the explicit formula. The kernel is positive and
   integrably singular at $x=0$ and at every $\log n$, on a negative continuous
   background $-\omega[4\cosh\tfrac x2-2n_\gamma(x)]+O(\omega^2)$ that changes
   sign at $x_0=0.28120$, the root of $u^3+u^2=1$, $u=e^{-x_0}$. Its
   large-$x$ behaviour is the prime number theorem: the comb mass
   $\sum_{n<e^x}\widetilde c_n$ and the background both grow like $e^{x/2}$ at
   first order and cancel on average, and the zeros govern the fluctuation. So a
   Markov or conformal realization, whose positivity is structural, would have
   to produce $\widetilde k_\omega$ --- a Beta-distributed continuous delay and
   a multiplicative positive comb, both of which are the kind of thing Bessel
   processes and Lévy-driven Loewner chains produce --- and then the rank-two
   subtraction from the two marked points, whose exact balance against the
   comb is the zero-free strip. **That is where the arithmetic hides in this
   picture, and it is a much smaller and more concrete place than "the
   theory".**

6. **The one thing the Loewner idea would have to deliver, and the first
   computation** (Section 6): a dilation-invariant observable of a Lévy-driven
   whole-plane chain whose kernel on the ray has the Beta continuous part and
   the multiplicative comb, followed by a determination of what the two marked
   points contribute. The first half is a Bessel-process computation; the
   second is where I expect it to fail, and a failure there would be a sharper
   statement than the investigation has now.

---

## 1. What exactly is abelian, and what the critical path is

### 1.1 The commutative algebra

Fix $L$. By (2.9) and (2.11) of the manuscript,
$V_{\omega,L}=P_L\,K_\omega(D)\,P_L$ and $G_{\omega,L}=P_L\,a_\omega(D)\,P_L$
where $D=-i\partial_x$ and the functions are realized causally, on
$\operatorname{Re}p=\eta>1$. Lemma 5.1 says compression to $I_L$ is
multiplicative on causal kernels, so the map $T:\ b(D)\mapsto P_L\,b(D)\,P_L$ is
an algebra homomorphism from the (commutative) algebra of causal symbols onto
its image $\mathcal A_L$, which is therefore commutative. Both families lie in
$\mathcal A_L$ for every $\omega$. In a discretization ordered by $x$,
$\mathcal A_L$ is the algebra of lower-triangular Toeplitz matrices, power
series in one nilpotent shift.

So what is abelian is **translation invariance along the line**: every
$\omega$ acts on $I_L$ by a kernel depending only on the separation $x-y$, with
the prime atoms at fixed separations $m\log p$; every generator is a function of
the line momentum; two functions of one operator commute. Read as a condition on
a gauge realization, the transported $F$-insertions implementing the
$\omega$-deformation must act as functions of a single operator, uniformly
along the line --- a Cartan-like or center-like direction of the theory, not a
generic one. It is a selection, not an impossibility. The manuscript's
"the mechanism has nothing to act on" overstates this.

### 1.2 The two-parameter algebra is triangular, and transport along a path is ordered

Proposition 9.3 of the manuscript gives, with $B_L=\tfrac12\delta_{L/2}\otimes\mathrm{ev}_{L/2}$,
\[
 G_{\omega,L}B_L=0,\qquad B_LG_{\omega,L}\neq0,\qquad [G_{\omega,L},B_L]=-B_LG_{\omega,L}.
\]
The algebra generated by the bulk and endpoint directions is triangular, not
commutative. Along a path $t\mapsto(\omega(t),L(t))$ the transport
\[
 \mathcal P\exp\int\big(\dot L\,B_L-\dot\omega\,G_{\omega,L}\big)\,dt
\]
is a genuinely ordered product: the two tangent generators at different points
do not commute, and no rearrangement collapses it to an exponential. **Along a
critical path the flow is not abelian.** What is true is that the value of the
transport depends only on the endpoints, because the connection is flat --- and
flatness is the subject of the next section.

## 2. Flatness is a tautology; the field strength is the generator

### 2.1 Any single-valued family gives a flat connection

Let $V(\alpha)$ be any family of operators depending smoothly on parameters
$\alpha\in M$ and satisfying $dV=\mathcal A\,V$ for an operator-valued one-form
$\mathcal A$ on $M$. Then $0=d^2V=d(\mathcal AV)=(d\mathcal A)V-\mathcal A\wedge dV
=(d\mathcal A-\mathcal A\wedge\mathcal A)V$, so the curvature
$\mathcal F=d\mathcal A-\mathcal A\wedge\mathcal A$ annihilates the range of $V$;
when $V$ is invertible, $\mathcal A=dV\,V^{-1}$ is pure gauge. Here
$V_{\omega,L}$ is a Volterra operator with dense range, so $\mathcal F=0$. This
is Proposition 9.4, and it holds for *every* choice of second parameter on which
the transfer depends single-valuedly, and on the whole space of contours in any
realization $W[C]$ with $W=V\circ\pi$: pulling a flat connection back to a
larger space keeps it flat, and the fibre directions --- deformations that do
not move $(\omega,L)$ --- act trivially on $W$, i.e. as symmetries. The residual
conformal group of Section 10.4 is one such family. Remark 9.6 of the manuscript
says this about the fibre; the point here is that it is true by construction and
carries no information about the realization.

### 2.2 In the non-Abelian Stokes variation, $F$ is the coefficient

For an open line $W[C]=P\exp\int_CA$ from $x_i$ to $x_f$, a variation
$\delta x^\mu(s)$ of the contour gives
\[
 \delta W=\int_C ds\;W_{f\to s}\,F_{\mu\nu}(x(s))\,\dot x^\nu\delta x^\mu\,W_{s\to i}
 \;+\;A_\mu(x_f)\delta x_f^\mu\,W\;-\;W\,A_\mu(x_i)\delta x_i^\mu .
\]
The field strength enters as the coefficient of the bulk deformation --- the
transported insertion along the line --- and the endpoint terms are covariant
translations of the ends. Writing this as $\delta W=\mathcal A\,W$, the
one-form $\mathcal A$ *is* the $F$-insertion, and its curvature on deformation
space is zero by §2.1. The surface-ordering content of the non-Abelian Stokes
theorem is in $\mathcal A$, not in $\mathcal F$.

The consequence for the proposal is a change of target. The arithmetic
connection is $(-G_{\omega,L}\,d\omega,\ B_L\,dL)$. Its bulk coefficient
$G_{\omega,L}$ is the object to match with a transported $F$-insertion; its
endpoint coefficient $B_L$ is the object to match with $A_\mu\delta x^\mu$ at
the moving end (the trailing end is killed by causality, Proposition 9.1). Both
are nonzero, and the first carries the whole Weil form including the primes.
The two constraints on a realization are then exactly §1.1 and §1.2: the
$\omega$-insertions must commute among themselves and with the transport
(translation invariance along the line), and they must fail to commute with the
endpoint term in the one-sided way $GB=0\neq BG$. That is the deformation
algebra of an open line with a pinned tail and a free head, which is what the
manuscript's Section 9.1 found; Section 9.2's "no curvature to extract" is not
an obstruction to it and should not be read as one.

### 2.3 What then remains as the obstruction

Not flatness. The dichotomy (Proposition 7.2): whatever realizes $G$ as an
$F$-insertion, the contraction of the resulting transport at fixed $\omega$ for
all $L$ is a zero-free strip of width $\omega$, so the realization's
unitarity must be exactly critical --- saturated at every length by a
superexponentially small, density-driven margin. Section 4 locates where in the
transfer that criticality sits.

## 3. The Loewner proposal

### 3.1 Four structural affinities

*Time.* Whole-plane Loewner evolution grows a hull $K_t$ from the origin toward
infinity, parametrized so that the logarithmic capacity of $K_t$ is $t$: the
Loewner time is log-conformal-radius, which is the arithmetic coordinate
$x=\log r$ of manuscript Section 10.4 exactly.

*Symmetry.* The whole-plane setting has two marked points, $0$ and $\infty$; the
Möbius maps preserving them are dilations $r\mapsto\lambda r$ and inversions
$r\mapsto\mu/r$, which is precisely the exact symmetry group of the Weil form
(translations and reflection in $x$). The interval $I_L$ is the annulus
$e^{-L/2}<r<e^{L/2}$ of modulus $L/2\pi$, the natural span of Loewner time.

*The tip.* The Loewner equation $\partial_tg_t(z)=g_t(z)\dfrac{e^{iU_t}+g_t(z)}{e^{iU_t}-g_t(z)}$
(exterior normalization) is a tip equation: the vector field is singular only
at the image of the growing end, and its coefficient is one scalar, the driving
function $U_t$. Proposition 9.1 has the same shape, $\partial_LV_{\omega,L}=B_LV_{\omega,L}$
with $B_L$ rank one at the tip and the boundary value $(V_\omega f)(L/2)$ as
the scalar coefficient.

*Ordering.* The chain $g_t$ is the flow of the time-dependent vector field
$v_t=z\frac{e^{iU_t}+z}{e^{iU_t}-z}$, a path-ordered product in the Witt algebra;
Bauer--Bernard write $G_t^{-1}\partial_tG_t$ as a combination of $L_{-2}$ and
$L_{-1}$ driven by $U_t$. This supplies exactly the ordered, infinite-dimensional
structure the $\omega$-direction lacks, with functions on the domain as the
representation space --- Condition 10.1's first clause for free. And composition
with a univalent self-map of the disc is a contraction on Hardy-type spaces by
Littlewood subordination, so a chain hands one a family of contractions with a
positive defect and no arithmetic in it.

### 3.2 Lemma: rotation-averaged composition operators on analytic functions are dilations

> **Lemma 3.1.** Let $\phi$ be analytic near $0$ with $\phi(0)=0$, and let $h$
> be analytic. Then
> $\displaystyle\frac1{2\pi}\int_0^{2\pi}h\big(e^{i\theta}\phi(e^{-i\theta}z)\big)\,d\theta=h\big(\phi'(0)\,z\big)$.
> Consequently, for a random conformal map $g$ with rotation-invariant law and
> deterministic $g'(0)$, $\mathbb E[h\circ g]=h(g'(0)\,\cdot)$ for every analytic
> $h$; the same holds at $\infty$ for exterior maps $g(z)=e^{-t}z+O(1)$.

*Proof.* It suffices to take $h=z^n$. Then $e^{in\theta}\phi(e^{-i\theta}z)^n
=e^{in\theta}\sum_{k\geq n}b_ke^{-ik\theta}z^k$, and the average keeps only
$k=n$, whose coefficient is $b_n=\phi'(0)^n$. $\square$

So on $H^2$, on the Dirichlet space, on any space of analytic functions, the
expected composition operator of a rotation-invariant chain with the standard
capacity normalization is $h\mapsto h(e^{-t}z)$: a pure delay by $t$ in $x$,
symbol $e^{-tp}$, carrying no information about the chain. The shape of the
curve lives entirely in non-analytic observables --- $|g|$, harmonic measure,
$\mathbb E|g'|^q$ --- which is where the SLE multifractal literature lives. **A
Loewner realization of the transfer must act on real-valued, non-analytic
observables.** The natural one is the radial Markov process
$Y_t=\log|g_t(z)|$, whose transition kernel, however, depends on the distance to
the hull and is not translation-invariant in $Y$; translation invariance along
the arithmetic line then becomes a symmetry requirement on the observable (it
must be dilation-covariant, hence a function of a radius *ratio*), and I return
to this in Section 6 after the decomposition that says what such an observable
would have to produce.

## 4. The Markov decomposition of the transfer

Everything in this section is unconditional and elementary. Throughout
$s=\tfrac12+p$, $0<\omega<\tfrac12$, $a=\tfrac12-\omega$, $b=\tfrac12+\omega$,
$\Lambda(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u)$ so that $\xi(u)=\tfrac12u(u-1)\Lambda(u)$,
and $n_\gamma(x)=e^{-x/2}/(1-e^{-2x})$ as in the manuscript.

### 4.1 Statement

> **Proposition 4.1 (factorization).** $K_\omega(p)=R_\omega(p)\,\widetilde K_\omega(p)$ with
> \[
>  \widetilde K_\omega(p)=\frac{\Lambda(s-\omega)}{\Lambda(s+\omega)},\qquad
>  R_\omega(p)=\frac{(s-\omega)(s-\omega-1)}{(s+\omega)(s+\omega-1)}
>  =\frac{(p+a)(p-b)}{(p+b)(p-a)}
>  =1-\frac{4\omega b}{p+b}-\frac{4\omega a}{p-a}.
> \]
> The zeros of $R_\omega$ at $p=-a$ and $p=b$ cancel the poles of
> $\widetilde K_\omega$ there (the poles of $\Lambda(s-\omega)$ at $s-\omega\in\{0,1\}$),
> and the poles of $R_\omega$ at $p=-b$ and $p=a$ cancel the zeros of
> $\widetilde K_\omega$ there (the poles of $\Lambda(s+\omega)$). Both factors
> are unimodular on $\operatorname{Re}p=0$.

> **Proposition 4.2 (complete monotonicity).** $\widetilde K_\omega$ is
> completely monotone on $(b,\infty)$: $(-1)^k\widetilde K_\omega^{(k)}(p)\geq0$
> for all $k\geq0$, $p>b$. Hence, by Bernstein's theorem, $\widetilde K_\omega$
> is the Laplace transform of a positive measure $\widetilde k_\omega$ on
> $[0,\infty)$, which is the causal inverse Laplace kernel of $\widetilde K_\omega$
> on any line $\operatorname{Re}p=\eta>b$.

*Proof.* On $p>b$ both $\Lambda(s\pm\omega)$ are positive, so
$\Phi(p):=-\log\widetilde K_\omega(p)$ is real, with
\[
 \Phi'(p)=\tfrac12\big[\psi(\tfrac{s+\omega}2)-\psi(\tfrac{s-\omega}2)\big]
 +\frac{\zeta'}{\zeta}(s+\omega)-\frac{\zeta'}{\zeta}(s-\omega)
 =\int_0^\omega\Big(\tfrac14\big[\psi'(\tfrac{s-t}2)+\psi'(\tfrac{s+t}2)\big]
 +\sum_{n\geq2}\Lambda(n)\log n\,\big[n^{-s+t}+n^{-s-t}\big]\Big)dt .
\]
Each integrand is completely monotone in $p$ ($\psi'(z)=\sum_k(z+k)^{-2}$ and
$n^{-p}$ are), so $\Phi'$ is completely monotone; a function with completely
monotone derivative is a Bernstein function up to an additive constant on any
$(p_0,\infty)$, and $e^{-\Phi}$ is then completely monotone there; let
$p_0\downarrow b$. Bernstein's theorem gives the positive measure. $\square$

> **Proposition 4.3 (the pieces).** $\widetilde K_\omega=K^\Gamma_\omega K^\zeta_\omega$ with
> \[
>  K^\Gamma_\omega(p)=\pi^\omega\frac{\Gamma(\frac{s-\omega}2)}{\Gamma(\frac{s+\omega}2)}
>  =\int_0^\infty e^{-px}\,k^\Gamma_\omega(x)\,dx,\qquad
>  k^\Gamma_\omega(x)=\frac{2\pi^\omega}{\Gamma(\omega)}\,(2\sinh x)^{\omega-1}e^{x/2}
>  =\frac{2\pi^\omega}{\Gamma(\omega)}\,(2\sinh x)^{\omega}\,n_\gamma(x),
> \]
> \[
>  K^\zeta_\omega(p)=\frac{\zeta(s-\omega)}{\zeta(s+\omega)}=\sum_{n\geq1}c_n\,n^{-s}
>  =\int e^{-px}\sum_n\widetilde c_n\,\delta_{\log n},\qquad
>  c_n=n^{\omega}\prod_{p\mid n}(1-p^{-2\omega}),\quad
>  \widetilde c_n=c_n\,n^{-1/2}>0 ,
> \]
> so that $\widetilde k_\omega=k^\Gamma_\omega*\sum_n\widetilde c_n\delta_{\log n}
> =\sum_n\widetilde c_n\,k^\Gamma_\omega(\,\cdot-\log n)$, a sum of shifted
> Beta kernels, and
> \[
>  k_\omega=\widetilde k_\omega-4\omega b\,\big(e^{-b\,\cdot}\mathbf 1_{>0}\big)*\widetilde k_\omega
>  -4\omega a\,\big(e^{a\,\cdot}\mathbf 1_{>0}\big)*\widetilde k_\omega .
> \]

*Proof.* The Beta integral: with $u=r^2$,
$\int_0^1r^{s-\omega-1}(1-r^2)^{\omega-1}dr=\tfrac12B(\tfrac{s-\omega}2,\omega)
=\frac{\Gamma(\frac{s-\omega}2)\Gamma(\omega)}{2\Gamma(\frac{s+\omega}2)}$, and
$r=e^{-x}$ turns it into $\int_0^\infty e^{-(s-\omega)x}(1-e^{-2x})^{\omega-1}dx$;
with $s=\tfrac12+p$ and $(1-e^{-2x})^{\omega-1}e^{-(\frac12-\omega)x}=(2\sinh x)^{\omega-1}e^{x/2}$
this is the displayed $k^\Gamma_\omega$ (note $1-e^{-2x}=e^{-x}\,2\sinh x$, so
$n_\gamma(x)=e^{x/2}/(2\sinh x)$ and the two forms agree). The Dirichlet coefficients:
$\zeta(s-\omega)=\sum n^\omega n^{-s}$ and $1/\zeta(s+\omega)=\sum\mu(n)n^{-\omega}n^{-s}$,
so $c_{p^k}=p^{k\omega}-p^{(k-2)\omega}=p^{k\omega}(1-p^{-2\omega})$ for $k\geq1$
and $c$ is multiplicative; $n^{-s}=n^{-1/2}e^{-p\log n}$ puts the weight
$\widetilde c_n=c_nn^{-1/2}$ on the atom at $\log n$. The last display is the
convolution theorem applied to the partial fractions of $R_\omega$, whose
residues are $-4\omega b$ at $p=-b$ and $-4\omega a$ at $p=a$. $\square$

### 4.2 What the decomposition says

**(a) The transfer is elementary on $I_L$.** Only $n<e^L$ contribute to
$k_\omega$ on $[0,L)$, since $k^\Gamma_\omega(\cdot-\log n)$ vanishes below
$\log n$. So $V_{\omega,L}$ is assembled exactly from $(2\sinh x)^{\omega-1}e^{x/2}$,
the numbers $\widetilde c_n$ for $n<e^L$, and two exponentials --- no $\xi$, no
$\zeta$ on a line, no zeros --- in precisely the way $Q_L$ is assembled from the
explicit formula. This makes the compressed transfer, its norm, its defect and
its cumulative Cayley coordinate computable to arbitrary precision in the same
style as the existing assembler, and it should replace the far-right-line
Fourier realization wherever that was used numerically.

**(b) The first-order kernel and its sign.** As $\omega\downarrow0$, off the
atoms,
\[
 \frac{k_\omega(x)}{\omega}\longrightarrow 2n_\gamma(x)-4\cosh\tfrac x2 ,
 \qquad
 \widetilde c_n=2\omega\,\Lambda(n)\,n^{-1/2}+O(\omega^2),
\]
consistent with Theorem 3.1's kernels ($-\omega g_0$). The continuous part is
positive for $x<x_0$ and negative beyond, where $n_\gamma(x_0)=2\cosh\frac{x_0}2$,
i.e. $u^3+u^2=1$ with $u=e^{-x_0}$: $x_0=0.2811996$. So the kernel is a
positive integrable singularity $\frac{(2\pi)^\omega}{\Gamma(\omega)}x^{\omega-1}$
at the origin, positive integrable singularities $\widetilde c_n\,k^\Gamma_\omega(x-\log n)$
at every $\log n$, and a negative continuous background produced entirely by
$R_\omega$: $\widetilde k_\omega\geq0$ everywhere, and both subtracted terms are
positive.

**(c) The non-Markov part is rank two and sits at the marked points.** In the
ray variable the two exponentials are $r^{-\frac12-\omega}$ and $r^{\frac12-\omega}$,
the endpoint modes $r^{\pm\frac12}$ of Condition 10.3 shifted by $\omega$; they
are the modes at $0$ and $\infty$, i.e. at the poles $s=0,1$ of $\zeta$. Their
coefficients $4\omega(\tfrac12\pm\omega)$ vanish with $\omega$, and at
$\omega=\tfrac12$ the second vanishes identically ($a=0$) while the first is
$2$: at the endpoint shift the non-Markov correction is a single first-order
all-pass factor $\frac{p-1}{p+1}$, which is the $\frac{s-1}{s}$ separating the
$\xi$-ratio from the Eisenstein scattering matrix in the review's Section 4.

**(d) The quarter is a Beta parameter.** With $u=e^{-2x}=(r_1/r_2)^2$, the
archimedean kernel is $k^\Gamma_\omega(x)dx\propto u^{\frac14-\frac\omega2-1}(1-u)^{\omega-1}du$:
the archimedean transfer moves a point from radius $r_1$ to $r_2>r_1$ with
$(r_1/r_2)^2\sim\mathrm{Beta}(\tfrac14-\tfrac\omega2,\ \omega)$, up to the
normalization $\pi^\omega\Gamma(\frac14-\frac\omega2)/\Gamma(\frac14+\frac\omega2)$.
The first parameter is the delay test's archimedean shift $a=\tfrac14$ displaced
by half the resonance width, the second is the width itself, and the whole
tower $\Gamma(s/2)$ is the statement that the natural variable is $r^2$ ---
the "two-sheeted cover" the manuscript's outlook item 1 asked for. At
$\omega\to0$ the law concentrates at $u=1$ (no motion); at $\omega=\tfrac12$ it
degenerates at $u=0$, which is the pole of $K^\Gamma_{1/2}$ at $p=0$. Beta laws
of squared radius ratios are what Bessel processes and radial Loewner chains
produce, and this is the identification Section 6 asks for.

**(e) The atoms are abelian monodromies.** The local factor
$\frac{1-p^{-\omega}z}{1-p^{\omega}z}$, $z=e^{-s\log p}$, of $K^\zeta_\omega$ is
a one-delay feedback loop of length $\log p$ with loop gain $p^{\omega}$ and
feedforward $-p^{-\omega}$: its kernel is $\delta_0+(1-p^{-2\omega})\sum_{k\geq1}p^{k\omega}\delta_{k\log p}$
before the $n^{-1/2}$. A traversal of the loop at ratio $p$ multiplies by the
scalar $p^{\omega}$; that is the monodromy at the puncture of manuscript
Section 9.4, made explicit, and it is a scalar because the local factor is a
ratio of determinants. For an Artin $L$-function it would be a ratio of
$\det(1-\rho(\mathrm{Frob}_p)\,p^{\mp\omega}z)$ --- still scalar. Nothing here
changes that assessment; it names the number.

**(f) Large $x$ is the prime number theorem, and the zeros are the
fluctuation.** To first order the comb mass below $x$ is
$2\omega\sum_{n<e^x}\Lambda(n)n^{-1/2}\approx4\omega e^{x/2}$ and the
integrated background is $-8\omega\sinh\frac x2\approx-4\omega e^{x/2}$: they
cancel on average, by $\sum_{n\leq N}\Lambda(n)n^{-1/2}\sim2\sqrt N$, and the
remainder $-\sum_\rho N^{\rho-1/2}/(\rho-\tfrac12)$ is the fluctuation the zeros
control. Unconditionally $k_\omega(x)=O(e^{(\theta-\omega+\epsilon)x})$ with
$\theta=\sup\operatorname{Re}(\rho-\tfrac12)$, and under RH $k_\omega$ decays like
$e^{-\omega x}$ with the residue expansion $\sum_\rho\frac{\xi(\rho-2\omega)}{\xi'(\rho)}e^{(-\omega+i\gamma_\rho)x}$
of the review's Section 5.2. So the decomposition displays the dichotomy of
Proposition 7.2 at the level of the kernel: the Markov part grows like $e^{bx}$,
$R_\omega$ removes the growth exactly and unconditionally, and what is left
decays if and only if the zeros allow it.

### 4.3 What it does not say

It does not make $V_\omega$ a Markov operator, and it cannot: a positive kernel
of mass $K_\omega(0)=1$ would make $V_{\omega,L}$ a contraction for every $L$ and
prove a zero-free strip. The first-order background is negative for $x>x_0$,
and Section 5 shows the sign changes at every $\omega$ computed. What it does is
put the whole failure of positivity into one rational factor with two poles,
whose residues are explicit, and identify the positive part with objects
(a Beta law, a multiplicative comb) that probability and conformal geometry
know how to produce.

## 5. Numerics

`numerics/exploratory/transfer_kernel.py` (unregistered, mpmath; 30 digits)
assembles $k_\omega$ from Proposition 4.3 and runs seven checks. At
$\omega=0.1$, $L=2.5$:

| check | what | result |
|---|---|---|
| A | $\int_0^\infty e^{-px}k^\Gamma_\omega=K^\Gamma_\omega(p)$ at four real $p$ | rel. $3.6\times10^{-30}$ |
| B | $c_n>0$ for $n\leq2\times10^4$; $\sum c_nn^{-s}=K^\zeta_\omega$ at $p=2,3,4$ | all positive; rel. $1.1\times10^{-7},3.5\times10^{-12},1.2\times10^{-16}$, each below its tail bound |
| C | $R_\omega\widetilde K_\omega=K_\omega$ and the partial fractions, at five complex $p$ | rel. $2.1\times10^{-31}$ |
| D | $(-1)^k\widetilde K^{(k)}_\omega(p)>0$, $k\leq6$, $p\in\{1,1.5,3\}$ | all positive |
| E | $k_\omega/\omega$ against $2n_\gamma-4\cosh\frac x2$ off the atoms; $\widetilde c_n$ against $2\omega\Lambda(n)n^{-1/2}$ | agree to $O(\omega)$: at $\omega=0.02$ the ratio is $0.994$--$1.006$ at $x\in\{0.5,0.65,1.0,1.35,1.55\}$; $\widetilde c_2=0.0981$ vs $0.0980$, $\widetilde c_3=0.1271$ vs $0.1269$ |
| F | table of $k_\omega$, $\widetilde k_\omega$ on $(0,2.5)$ | below |
| G | truncated Laplace transform $\int_0^Xe^{-px}k_\omega$ against $K_\omega(p)$, $X=2,3,4$ | $p=3$: differences $6.2\times10^{-5},5.2\times10^{-6},1.1\times10^{-7}$; $p=5$: $1.0\times10^{-6},1.3\times10^{-8},4.2\times10^{-11}$ --- geometric in $X$, so the kernel-level assembly is right and the residual is the tail |

Check G is the one that tests the kernel rather than the symbol; it was also
what caught an error in the first version of the programme, which had omitted
the $n^{-1/2}$ in $\widetilde c_n$ (the symbol checks A--D all passed with the
wrong weights). The first-order root $x_0=0.28120$ is reproduced by the sign
change of $k_{0.1}$ between $x=0.281$ ($+0.018$) and $x=0.300$ ($-0.006$), and
at $\omega=0.02$ ($+0.0304$ at $0.2$, $-0.0039$ at $0.3$).

Selected values of $k_\omega$ at $\omega=0.1$ (positive spikes at $\log n$ are
integrable singularities; the grid point $0.72$ is $0.027$ past $\log2$):

| $x$ | $0.05$ | $0.20$ | $0.281$ | $0.30$ | $0.50$ | $0.65$ | $0.72$ | $0.80$ | $1.00$ | $1.15$ | $1.35$ | $1.55$ | $1.65$ | $1.90$ | $1.98$ | $2.30$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $k_{0.1}$ | $+1.547$ | $+0.170$ | $+0.018$ | $-0.006$ | $-0.161$ | $-0.221$ | $+0.049$ | $-0.206$ | $-0.310$ | $-0.161$ | $-0.389$ | $-0.434$ | $-0.198$ | $-0.550$ | $-0.244$ | $-0.656$ |
| $\widetilde k_{0.1}$ | $1.919$ | $0.591$ | $0.450$ | $0.428$ | $0.292$ | $0.242$ | $0.551$ | $0.307$ | $0.221$ | $0.432$ | $0.232$ | $0.244$ | $0.547$ | $0.252$ | $0.626$ | $0.350$ |
| $\frac{k}{\omega}$ vs $2n_\gamma-4\cosh\frac x2$ | $15.5/16.5$ | $1.70/1.47$ | $0.18/0.00$ | $-0.06/-0.23$ | $-1.61/-1.66$ | $-2.21/-2.23$ | atom | $-2.06/-2.64$ | $-3.10/-3.11$ | atom | $-3.89/-3.85$ | $-4.34/-4.30$ | atom | $-5.50/-5.15$ | atom | $-6.56/-6.31$ |

The same programme at $\omega=0.25$ shows the wider spikes at $\log2,\log3,\log5,\log7,\log8$
crossing zero on the grid, and at $\omega=0.02$ only the crossing at $x_0$,
the spikes being too narrow for the grid; all seven checks pass at every
$\omega$ run. The record for $\omega=0.1$ is `transfer_kernel_omega0.1.json`
beside the programme.

## 6. What a Loewner or Markov realization must produce, and the first computation

The decomposition turns the question of Section 3 into a specification.

**What it must produce.** A dilation-invariant observable of a random
conformal chain on the punctured plane whose kernel on the ray, as a function of
the radius ratio $r_2/r_1=e^x$, is $\widetilde k_\omega$: the
$\mathrm{Beta}(\tfrac14-\tfrac\omega2,\omega)$ law of the squared ratio for the
continuous part, and the multiplicative comb $\widetilde c_n$ at integer ratios.
The Beta part is the natural target for a Bessel-process or radial-Loewner
hitting law: the squared conformal radius at a disconnection or hitting time of
a Bessel process of dimension $\delta$ has Beta-type laws whose parameters are
affine in $\delta$, and one asks which $\delta$ and which event give the
parameters $(\tfrac14-\tfrac\omega2,\omega)$ --- in particular where the
$\tfrac14$ comes from, since it must be the same $\tfrac14$ that the delay test
measures. The comb is the natural target for a Lévy-driven chain
(Oikonomou--Rushkin--Gruzberg--Kadanoff; Chen--Rohde) whose driving process
jumps: a jump in the driving function at a time when the hull has capacity $e^t$
produces a discontinuity in the radial kernel at the ratio $e^{\Delta t}$, and
the requirement is that the jump ratios be exactly the integers, with weights
multiplicative in $n$ and equal to $n^{\omega-1/2}\prod_{p|n}(1-p^{-2\omega})$.
Multiplicativity is the constraint with teeth: it says the jumps at $\log p$
and $\log q$ compose independently, which is the statement that the loops at
different punctures commute (Section 4.2(e)).

**Where it will fail, and why that is informative.** Suppose both are achieved,
so that a structurally positive chain produces $\widetilde V_\omega$. The
transfer is then $R_\omega\widetilde V_\omega$, and the rank-two factor has to
come from the two marked points: in the ray picture the subtracted exponentials
are the modes $r^{-\frac12-\omega}$ at $0$ and $r^{\frac12-\omega}$ at $\infty$,
with coefficients $4\omega(\tfrac12\pm\omega)$ that the chain's normalization at
its two ends would have to supply, with the right sign. By the dichotomy, the
resulting operator is a contraction at every $L$ if and only if $\xi$ has no
zero at distance $>\omega$ from the line, so whatever the chain produces at the
marked points is exactly balanced against its comb by the zeros. A structural
construction cannot know that; so either the marked-point contribution comes
out wrong --- in which case the obstruction has been located in two numbers,
the coefficients of $r^{-\frac12-\omega}$ and $r^{\frac12-\omega}$ --- or it comes
out right, which would be a construction of a contraction and a theorem. I
expect the former, and it would still be the sharpest statement about this
direction the investigation has: not "no theory", but "the two endpoint
coefficients".

**The first computation, in order.**

1. *The Beta law.* Identify the Bessel dimension and stopping rule whose
   squared radius ratio is $\mathrm{Beta}(\tfrac14-\tfrac\omega2,\omega)$, or
   show that no radial Loewner hitting law has $\tfrac14$ in the first slot.
   This is a self-contained problem in Bessel processes and needs no arithmetic.
2. *The comb.* Compute the radial kernel of a whole-plane chain driven by a
   compound-Poisson process, in the co-moving coordinate $\xi=x-t$, and
   determine whether jumps of the driving function produce atoms in the *ratio*
   variable at all, and with what composition law. If the composition is not
   multiplicative the Loewner route to the comb is closed.
3. *The marked points.* Only if 1 and 2 succeed: compute what the chain's
   normalization at $0$ and $\infty$ contributes, and compare with
   $-4\omega(\tfrac12+\omega)$ and $-4\omega(\tfrac12-\omega)$.
4. Independently of the above, **port the assembly of Section 4.2(a) to a
   registered programme** and use it to recompute $\lVert V_{\omega,L}\rVert$
   and the cumulative Cayley coordinate at the three recorded horizons: the
   elementary kernel makes the contraction side of the programme as computable
   as the form side has been.

## 7. Status of every statement

- **Written proof, unconditional:** Propositions 4.1--4.3 and Lemma 3.1; the
  first-order law and the root $x_0$ of §4.2(b); the residues of $R_\omega$;
  §2.1.
- **Labelled numerical computation (unregistered, mpmath):** every number in
  Section 5, produced by `numerics/exploratory/transfer_kernel.py`.
- **Reading of the physics:** §2.2 (the non-Abelian Stokes variation of an open
  line, standard), §3.1 (whole-plane Loewner conventions; the Bauer--Bernard
  Virasoro form), and the Bessel-process and Lévy-Loewner references in
  Section 6, cited from memory for structure and not re-derived here.
- **Proposal:** all of Section 6.
- **Conditional on RH:** only the decay statement and the residue expansion
  quoted in §4.2(f).
- **Not claimed:** a Markov realization of the transfer, a contraction, a
  positivity statement, or anything about the zeros.

## 8. Recommendations to the manuscript

1. Section 9.2: state that flatness is automatic for any single-valued family
   (§2.1), and replace "no curvature to extract" with the two constraints of
   §1.1--1.2 as the content of the non-Abelian Stokes matching; move the
   identification "$G\leftrightarrow$ transported $F$-insertion,
   $B_L\leftrightarrow$ endpoint term" from Section 10.1's prose into Section 9.
2. Add Propositions 4.1--4.3 after Theorem 3.1 as "the transfer kernel in
   closed form", with §4.2(a)--(c); it is the transfer-side counterpart of the
   theorem and the natural place to record that the pole factor is the whole
   non-Markov part.
3. Add the Beta reading §4.2(d) to Section 11.7's discussion of the quarter,
   and the monodromy number §4.2(e) to Section 9.4.
4. Register the elementary assembly (item 4 of Section 6).

## 9. Reproduction

```sh
cd numerics/exploratory
python3 transfer_kernel.py 0.1 2.5     # ~2 min; JSON to stdout; record kept as transfer_kernel_omega0.1.json
python3 transfer_kernel.py 0.25 2.5
python3 transfer_kernel.py 0.02 2.5
```

See the [notes index](README.md) and the [review](../reviews/review_claude-fable-5-1_2026-09-17.md).
