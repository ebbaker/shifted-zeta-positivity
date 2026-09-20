# Ground transforms, contact subtraction, and coherent pole completion

Analytic investigation following the theory survey. The calculations below are exact on a smooth compactly supported core, with extensions stated where needed. They neither assume Weil positivity nor establish it. No numerical positivity bounds are used. The deductions are recorded for this program without a claim of literature priority.

## Result and scope

A positive scalar ground-state transform can absorb a local potential into a positive jump energy, but it cannot reproduce the full Weil form in the natural arithmetic position frame. The obstruction is already visible before the first prime:

- The continuous off-diagonal kernel changes sign at an explicit distance \(r_*=\log\rho\), where \(\rho>1\) solves \(\rho^3-\rho-1=0\).
- For every interval of length \(L>r_*\), the full Weil form has a positive bilinear cross term between suitable disjoint nonnegative inputs. Scalar positive-ground-state transforms of real diffusion/jump energies, with any local killing potential, have nonpositive such cross terms.
- For \(L>2r_*\), three separated patches have positive couplings around a triangle. Even a scalar phase change cannot remove all these signs. This threshold is below \(\log2\).

These are obstructions to a scalar reversible/Markov boundary-energy realization with the stated local source identification. They do not exclude positive Hamiltonians in general, derivative or composite observables, matrix-valued states, magnetic connections, coherent constraints, or interacting supersymmetric theories.

The constructive outcome is an exact separation of what those more general mechanisms must supply: pole interference has a positive-square realization only with a prescribed additional diagonal, while eliminating the normalized arithmetic contact requires an infinite-rank constraint. A finite collection of pole amplitudes alone cannot do both.

## 1. Fixed support, finite primes, and the normalized positive energy

Let \(I=(-L/2,L/2)\), \(F=E_Lf\), and choose a finite set \(\mathcal S\) containing every prime with \(\log p<L\). This support condition is part of the task: fixed-\(\mathcal S\) full positivity is not demanded on arbitrarily large intervals.

At the critical parameter define

\[
n_\gamma(r)=\frac{e^{-|r|/2}}{1-e^{-2|r|}},\qquad r\ne0,
\]

\[
a_{p,m}=(\log p)p^{-m/2},\quad d_{p,m}=m\log p,\qquad
\nu_{\mathcal S}(dr)=n_\gamma(r)\,dr+
\sum_{p\in\mathcal S,m\ge1}a_{p,m}
(\delta_{d_{p,m}}+\delta_{-d_{p,m}})(dr).
\]

The gamma density behaves as \(1/(2|r|)\) at zero and decays exponentially. The prime part has finite mass for finite \(\mathcal S\). The positive jump form is

\[
j_{\mathcal S,L}(f,g)=\frac12\int_{\mathbb R}\nu_{\mathcal S}(dr)
\int_{\mathbb R}
\overline{F(x+r)-F(x)}\,[G(x+r)-G(x)]\,dx.
\]

Its Fourier symbol is

\[
j_{\mathcal S}(\tau)
=B(\tau^2)+2\sum_{p\in\mathcal S,m\ge1}a_{p,m}
[1-\cos(d_{p,m}\tau)].
\]

Let \(J_{\mathcal S,L}\) be the associated nonnegative operator. Its form domain is the logarithmic domain of the gamma kinetic form; the finite-prime addition is bounded.

Put

\[
\kappa_{\mathcal S}=-w_0+
2\sum_{p\in\mathcal S,m\ge1}a_{p,m}>0,\qquad
w_0=\psi(1/4)-\log\pi<0.
\]

The complete target is exactly

\[
W_L=J_{\mathcal S,L}-\kappa_{\mathcal S}I+P_L,
\qquad
P_L(x,y)=p(x,y):=2\cosh((x-y)/2).
\]

Equivalently \(P_L=2|c\rangle\langle c|-2|s\rangle\langle s|\), with \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\). Every inactive jump contributes its diagonal \(2a_{p,m}\|f\|^2\) to \(j\), canceled by \(\kappa_{\mathcal S}\). Thus extra primes in \(\mathcal S\) do not change \(W_L\).

## 2. Exact scalar ground-state substitution

The use of a positive comparison state to factor a Schrödinger or jump form is standard. Nonlocal ground-state representations are developed, for example, by [Frank–Seiringer, Non-linear ground state representations and sharp Hardy inequalities](https://arxiv.org/abs/0803.0503). Here the relevant quadratic identity is derived directly, including the poles and interval exterior.

Let \(\mu_{\mathcal S}(dx,dy)\) be the symmetric internal jump measure on \(I^2\):

\[
\mu_{\mathcal S}(dx,dy)
=n_\gamma(x-y)\,dx\,dy
+\sum_{p,m}a_{p,m}\,dx
[\delta_{x+d_{p,m}}+\delta_{x-d_{p,m}}](dy)\big|_{I^2}.
\]

The escape rate from \(I\) is

\[
k_{\rm esc}(x)=
\int_{\{r:x+r\notin I\}}\nu_{\mathcal S}(dr).
\]

It is finite at every interior point and has a logarithmic divergence near the endpoints from the gamma part. Then

\[
j(f,g)=\frac12\int_{I^2}
(\overline{f(x)-f(y)})(g(x)-g(y))\,\mu_{\mathcal S}(dx,dy)
+\int_I k_{\rm esc}(x)\overline{f(x)}g(x)\,dx.
\]

Take a real \(h\in C^1(\overline I)\) with \(0<\inf h\le\sup h<\infty\). Zero extension places \(h\) in the logarithmic form domain; expressions below can first be used on \(f=hu,\ g=hv\), with \(u,v\in C_c^\infty(I)\). The jump action \(J h\) is understood with the same zero exterior.

Expanding the differences and symmetrizing gives

\[
j(hu,hv)=
\frac12\int_{I^2}h(x)h(y)
(\overline{u(x)-u(y)})(v(x)-v(y))\,\mu_{\mathcal S}(dx,dy)
+\int_I h(x)(Jh)(x)\overline{u(x)}v(x)\,dx.
\]

This identity shows exactly how a scalar ground transform can generate a potential:

\[
J+V_h=D_h^*D_h,\qquad
V_h(x)=-\frac{(Jh)(x)}{h(x)},
\]

as an identity of forms on the common core, where \(D_h\) is the internal incidence map

\[
(D_hf)(x,y)=
\sqrt{\frac{h(x)h(y)}2}
\left(\frac{f(x)}{h(x)}-\frac{f(y)}{h(y)}\right)
\]

in \(L^2(I^2,\mu_{\mathcal S})\). In particular the regular comparison state has \(D_hh=0\). The right side defines a positive closed-form realization after closing the incidence operator. Identifying that realization with a prescribed operator sum on a larger domain requires matching the closures; the core identity alone must not be used to bypass this step. Multiplication by bounded positive Lipschitz \(h\), with bounded Lipschitz inverse, preserves the original logarithmic form domain. All sign obstructions below already hold on compactly supported smooth inputs and therefore do not depend on a favorable choice of extension.

A negative potential is not itself an obstruction on a bounded interval: for \(h=1\), the transform removes the positive exterior escape rate. If \(h\) is a positive eigenfunction of \(J\) with eigenvalue \(\lambda\), this construction gives \(J-\lambda I\). To obtain the prescribed constant \(-\kappa_{\mathcal S}\), however, the eigenvalue or an additional identity must select that exact number. Scaling \(h\) by a constant changes neither \(V_h\) nor the operator. Raw normalization of a SUSY zero-state ray cannot tune this contact.

This is the scalar zero-form mechanism underlying a Witten deformation; [Witten's Supersymmetry and Morse theory](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf) supplies the broader supersymmetric context. Higher-degree or matrix-valued sectors need not have the scalar sign properties used below.

## 3. Including the poles produces a signed ground representation

The elementary pole identity is

\[
\langle f,Pg\rangle
=\int_I r_P(x)\overline{f(x)}g(x)\,dx
-\frac12\int_{I^2}p(x,y)
(\overline{f(x)-f(y)})(g(x)-g(y))\,dx\,dy,
\]

where

\[
r_P(x)=\int_I p(x,y)\,dy
=8\sinh(L/4)\cosh(x/2).
\]

Therefore the exact transformed full form is

\[
\boxed{
q_L(hu,hv)=
\frac12\int_{I^2}h(x)h(y)
(\overline{u(x)-u(y)})(v(x)-v(y))
\,[\mu_{\mathcal S}(dx,dy)-p(x,y)\,dx\,dy]
+\int_I h(x)(W_Lh)(x)\overline{u(x)}v(x)\,dx.}
\]

This remains an algebraic identity without assuming \(W_L\ge0\), \(W_Lh=0\), or \(W_Lh\ge0\). If one could choose \(W_Lh=0\), the first term would still have a signed edge measure. Thus the existence of a positive formal zero state would not give the usual positive ground-state proof. The pole kernel is an off-diagonal change, not a local killing potential.

## 4. A sign threshold inside prime-free intervals

At separated points away from prime delays, the off-diagonal kernel of the full form is

\[
R(r)=2\cosh(r/2)-\frac{e^{-r/2}}{1-e^{-2r}},\qquad r>0.
\]

Set \(x=e^r>1\). Direct simplification gives

\[
R(r)=e^{-r/2}\frac{x^3-x-1}{x^2-1}.
\]

Since \(x^3-x-1\) is strictly increasing for \(x>1\), it has a unique root \(\rho>1\). Hence

\[
R(r)<0\quad(0<r<r_*),\qquad
R(r)>0\quad(r>r_*),\qquad r_*=\log\rho.
\]

The approximate value \(r_*\simeq0.2812\) is only an orientation; the polynomial identity gives the exact sign proof.

Fix any \(L>r_*\). Choose \(d\in(r_*,L)\) which is not an active prime-power delay, and two sufficiently narrow disjoint patches in \(I\) separated by \(d\). There are only finitely many active delays, so their entire difference set can avoid all of them while remaining in \((r_*,L)\). For nonzero nonnegative smooth \(u,v\) supported in the two patches,

\[
q_L(u,v)=\int_{I^2}u(x)R(|x-y|)v(y)\,dx\,dy>0.
\]

The local contact vanishes on disjoint supports; the prime atoms give no contribution by construction.

In contrast, every real scalar jump/diffusion form with nonnegative edge weights has

\[
\mathcal E(u,v)\le0
\]

for disjoint nonnegative \(u,v\). For jumps this is simply the negative cross integral; the local diffusion and any local potential give zero cross term. A positive scalar multiplication by \(h\) preserves disjointness and nonnegativity.

**Scoped obstruction.** For \(L>r_*\), the full Weil form cannot be the positive-\(h\) transform of a real scalar diffusion/jump form plus a local potential, with the arithmetic input identified pointwise with the scalar boundary field. This holds in valid one-prime support windows and even before prime two enters. It is not the unrelated fixed-prime large-support obstruction.

The same sign property persists under eliminating auxiliary variables from a scalar Markov bulk. At a finite regulator, a real symmetric positive diffusion/jump matrix has nonpositive off-diagonal entries; its positive invertible interior block has entrywise nonnegative inverse, so its Schur complement retains nonpositive off-diagonal entries. More generally, minimizing a scalar Dirichlet energy preserves its contraction/Markov property. Adding more scalar reversible auxiliary variables does not evade this sign test.

## 5. Scalar phase changes and frustrated triangles

Allow a scalar phase frame \(f(x)\mapsto e^{i\theta(x)}f(x)\). If \(L>2r_*\), choose three small patches centered at \(x_1<x_2<x_3\), with all three separations above \(r_*\) and away from prime delays. Such a choice is possible by taking adjacent spacings slightly above \(r_*\). Their mutual continuous off-diagonal coefficients are positive.

To transform all three coefficients into real nonpositive Markov coefficients would require

\[
e^{i(\theta_2-\theta_1)}
=e^{i(\theta_3-\theta_2)}
=e^{i(\theta_1-\theta_3)}=-1.
\]

Multiplying gives \(1=-1\), a contradiction. The same argument applies to nonzero scalar amplitudes with phases; positive amplitudes do not change signs. Patches can be used in place of point values to formulate the argument almost everywhere.

Since \(\rho<\sqrt2\), as follows by evaluating \(x^3-x-1\) at \(\sqrt2\),

\[
2r_*<\log2.
\]

Thus this scalar phase obstruction also occurs within the prime-free range. A genuine magnetic or matrix connection can have nontrivial loop holonomy and is not a scalar pure gauge. It lies outside the excluded class.

Positive signed-incidence energies can reproduce the offending signs: an edge with positive off-diagonal coefficient uses \(|f(x)+f(y)|^2\), rather than \(|f(x)-f(y)|^2\). But a triangle of such edges admits no nonzero covariantly constant scalar zero state. Its frustration and its required diagonal energy must be dealt with by a more substantial theory.

## 6. Exact coherent pole square and its compulsory diagonal

There is a useful constructive identity, valid for all complex \(f,g\):

\[
e_P^+(f,g)=\frac12\int_{I^2}p(x,y)
(\overline{f(x)+f(y)})(g(x)+g(y))\,dx\,dy
=\langle f,Pg\rangle+\int_I r_P(x)\overline f g\,dx.
\]

Since \(p(x,y)>0\), \(e_P^+[f]\ge0\). Therefore

\[
\boxed{q_L[f]=j_{\mathcal S,L}[f]+e_P^+[f]
-\int_I[\kappa_{\mathcal S}+r_P(x)]|f(x)|^2\,dx.}
\]

The positive interference square reproduces the full signed rank-two pole form. It also forces a strictly positive diagonal companion. Restoring the arithmetic target requires subtracting that companion together with the already negative contact. This is a positive construction of the relative pole contribution, not a completion of the whole form.

One can reduce unnecessary diagonal cost by combining the continuous gamma and pole edges first. Write \(\omega(x,y)=n_\gamma(x-y)-p(x,y)\). A positive magnetic edge form with weight \(|\omega|\) and sign connection \(\operatorname{sgn}\omega\) has the desired continuous off-diagonal kernel. Relative to the signed-difference form, its extra diagonal is exactly

\[
2\int_I R(|x-y|)_+\,dy.
\]

That quantity is finite because \(R_+\) vanishes near the diagonal. The remaining local potential is fixed by the target, not freely adjustable. The triangle argument shows why this magnetic realization cannot be reduced to a scalar positive-ground-state transform.

## 7. Coherent constraints must handle an infinite-rank contact

The normalized jump form is an explicitly known positive reference. Define

\[
D_{\mathcal S,L}=\kappa_{\mathcal S}I-P_L,\qquad
W_L=J_{\mathcal S,L}-D_{\mathcal S,L}.
\]

Even though \(P_L\) is rank two, \(D_{\mathcal S,L}\) has infinite rank because \(\kappa_{\mathcal S}>0\). A finite-rank change of prepared boundary states or a finite-dimensional projection of the jump state map cannot supply this entire subtraction.

In the one-prime window \(\log2<L\le\log3\), \(D_{\mathcal S,L}\) is itself positive, independently of Weil positivity. Indeed

\[
\|c\|^2=L/2+\sinh(L/2),\qquad
\|s\|^2=-L/2+\sinh(L/2),\qquad c\perp s,
\]

so its eigenvalues are

\[
\kappa_{\mathcal S}-2\|c\|^2,\qquad
\kappa_{\mathcal S}+2\|s\|^2,\qquad
\kappa_{\mathcal S}\text{ on }\{c,s\}^{\perp}.
\]

The first is positive in this window: \(2\|c\|^2\le\log3+2/\sqrt3<3\), whereas
\(-w_0=\gamma_E+\pi/2+3\log2+\log\pi>3\), and \(\kappa_{\mathcal S}\ge-w_0\). These elementary comparisons concern a known rank-two perturbation of the identity, not a numerical lower bound for \(W_L\).

Consequently \(D^{1/2}\) is explicitly obtainable from these two projections and \(\sqrt{\kappa_{\mathcal S}}I\). Introducing a bulk variable \(z\) with

\[
\mathcal A[f,z]=j[f]-2\operatorname{Re}\langle D^{1/2}f,z\rangle+\|z\|^2
=q_L[f]+\|z-D^{1/2}f\|^2
\]

does give the desired Schur complement. But it is positive if and only if \(q_L\) is positive. Calling this action a positive completion would insert the unresolved claim. Adding the missing \(+\langle f,Df\rangle\) makes the action manifestly positive and makes its minimized value \(j[f]\), losing precisely the desired subtraction.

This algebra specifies what a nontrivial coherent-constraint mechanism must achieve: an independently derived infinite-dimensional contraction/projection identity for the contact together with the finite pole sectors. A projector defined only after factoring the unknown \(W_L\) does not provide it.

## 8. Implications for the next theory choice

The scalar Doob route is useful for generating known positive potentials and interpreting normalized jump energies. It cannot complete the present target while retaining a pointwise scalar boundary source and reversible/Markov edges. The obstruction is the signed geometry of the full kernel, not merely a divergent prime sum or a failed low-order approximation.

The next candidate should therefore have at least one genuinely different ingredient:

1. A matrix or fermionic state map with nontrivial interference/holonomy, whose ordinary norm remains positive.
2. A nonlocal or derivative boundary observable, so positivity need not appear as a scalar Markov energy in arithmetic position.
3. A polarized relative cohomology or an infinite-dimensional constraint that determines the diagonal subtraction and both pole sectors from the same identity.

These are possibilities, not established repairs. Their first test should compute the complete bilinear kernel and the compulsory diagonal terms from an independently specified action or gluing law. Merely adjusting a ground-state normalization, appending two pole states, or adding more scalar stochastic auxiliary variables does not pass that test.
