---
research_program: ALG
secondary_programs: [PR02, PR02-CORR]
status: unconditional_averaged_bound_and_open_pointwise_certificate
---

# Oriented octonionic currents and accretive source certificates

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6.1-sol**, reasoning effort **ultra**, supplied from current-session metadata. This analytic continuation uses no numerical experiments.

The physical first jet admits an unconditional, sharp **spatially averaged signed bound** paid by its original energy. The same calculation identifies why localization does not yield the missing pointwise stationary bound. Separate source differential certificates give a quotient-free analytic target for the two branches; no such theta certificate has been proved here. The manuscript's proved pointwise domains are unchanged.

## Exact signed current

Use [Note 15](../15_OCTONIONIC_LIFT_AND_ASSOCIATOR_SIGN_TARGET_20261014.md) and [Note 35](35_REFLECTED_LIFT_AND_PHYSICAL_REDUCTIONS_20261015.md):

\[
G_j=h_j+\mathbf jh_{j+1},\qquad
\mathcal L_j=h_{j+1}^2-h_jh_{j+2},\qquad
E=h_0^2+h_1^2,\qquad \mathbf u=\ell\mathbf j.
\]

On the physical slice,

\[
[G_j\mathbf i,G_{j+1}\mathbf i,\ell]
=2\mathbf u\mathcal L_j.
\tag{1}
\]

Let \(f=h_j\), and let \(\chi>0\) be \(C^1\). Direct differentiation gives

\[
\boxed{
\chi\mathcal L_j+\frac{\chi'^2}{8\chi}f^2
+\partial_x(\chi ff')
=2\chi\left(f'+\frac{\chi'}{4\chi}f\right)^2.}
\tag{2}
\]

Multiplying (2) by \(2\mathbf u\) is an exact associator-current identity with nonnegative density on the specified ray \(\{s\mathbf u:s\ge0\}\). The scalar orientation has not been replaced by the norm of an associator. The derivative is a genuine spatial flux, whose sign cannot be discarded pointwise.

If \(\chi ff'\) has vanishing endpoint flux and \(|\partial_x\log\chi|\le a\), integration proves

\[
\int\chi\mathcal L_j\,dx
\ge-\frac{a^2}{8}\int\chi h_j^2\,dx.
\tag{3}
\]

The domain can be the line or an interval with zero endpoint flux. Endpoints where \(f=0\) or \(f'=0\) suffice. In particular, on an interval between such endpoints,

\[
\int\mathcal L_j\,dx=2\int h_{j+1}^2\,dx\ge0.
\tag{4}
\]

For \(j=0,1\), each right side of (3) is bounded below by the same coefficient times \(-\int\chi E\). Adding the two sharper branch inequalities gives

\[
\int\chi(\mathcal L_0+\mathcal L_1)\,dx
\ge-\frac{a^2}{8}\int\chi E\,dx.
\tag{5}
\]

This estimate uses the physical two-jet energy, not the norm of the doubled octonionic lift.

## Sharp smooth localization

A smooth weight permits a better exact constant. Fix \(a>0\), \(x_0\in\mathbb R\), and put

\[
\chi(x)=\operatorname{sech}(a(x-x_0)),\qquad
\nu=\frac{\sqrt2-1}{2},\qquad
c_*:=2\nu^2=\frac{3-2\sqrt2}{2}.
\]

**Theorem.** For each \(j=0,1\), with integrals over the real line,

\[
\boxed{
\int\chi\mathcal L_j\,dx
\ge-c_*a^2\int\chi h_j^2\,dx
\ge-c_*a^2\int\chi E\,dx.}
\tag{6}
\]

Furthermore,

\[
\boxed{
\int\chi(\mathcal L_0+\mathcal L_1)\,dx
\ge-c_*a^2\int\chi E\,dx.}
\tag{7}
\]

**Proof.** Put \(g=\sqrt\chi f\). Integration by parts gives

\[
\int\chi(f'^2-ff'')\,dx
=2\int g'^2\,dx
+\frac12\int(\log\chi)''g^2\,dx
=2\int g'^2\,dx-\frac{a^2}{2}\int\operatorname{sech}^2(a(x-x_0))g^2\,dx.
\]

Because \(\nu(\nu+1)=1/4\), completing the square yields

\[
\boxed{
\int\chi\mathcal L_j\,dx+c_*a^2\int\chi f^2\,dx
=2\int\{g'+\nu a\tanh(a(x-x_0))g\}^2\,dx\ge0.}
\tag{8}
\]

The inequalities \(h_0^2,h_1^2\le E\), and their sum \(E\), prove (6) and (7). No stationarity substitution was used.

The constant \(c_*\) is sharp in the general weighted Sobolev class. Equality is attained by

\[
g=\operatorname{sech}^{\nu}(a(x-x_0)),\qquad
f=\cosh^{1-1/\sqrt2}(a(x-x_0)).
\]

Here \(\chi f^2=g^2\) is integrable. Smooth compactly supported truncations approach equality, since the weighted cutoff errors tend to zero. This establishes optimality for general admissible functions, not an assertion that the theta subfamily attains equality.

For the complete theta source all integration and endpoint conditions hold. For each compact real-time interval and each fixed \(0<a_0<\pi/8\), the complete-source strip shift gives

\[
|h_k(t,x)|\le C_{k,a_0}e^{-a_0|x|}.
\]

The heat and polynomial factors are dominated by the complete source's double-exponential tail uniformly on that time interval. Thus the weighted spatial flux vanishes and all displayed integrals converge. No theta-index truncation enters this proof.

## Why this does not prove the stationary target

The theorem is an unconditional signed estimate, but it is spatially averaged. Localizing to width \(1/a\) costs \(a^2\), so it does not give a locally bounded coefficient at an individual stationary point as \(a\to\infty\). The backward-heat polynomial collision controls satisfy the same exact current identity while retaining their adverse stationary pole. Theta-specific information is still needed to control the spatial flux or the corresponding signed boundary projection at physical-energy scale.

## Accretivity permits arbitrary angular motion

Identify the physical quaternion \(F=h_0+\mathbf jh_1\) with \(f=(h_0,h_1)\), and let

\[
J(A,B)=(-B,A),\qquad J^*=-J.
\]

For a source-prescribed real matrix \(M=S+\omega J\), with \(S=S^*\),

\[
f\cdot Mf=f\cdot Sf,\qquad
[F\mathbf i,(\omega JF)\mathbf k,\ell]=0.
\tag{9}
\]

Thus an angular component can be arbitrarily large without contributing to the radial loss. If, on the full stationary set \(h_{j+1}=0\), an independently established source identity gives

\[
F_t=MF+c_jh_{j+1}+R_j,\qquad
S\succeq-\kappa_jI,\qquad
F\cdot R_j\ge-b_jE,
\]

then

\[
\mathcal L_j\ge-(\kappa_j+b_j)E.
\tag{10}
\]

Only the coefficients entering the loss must be locally bounded through covered candidate events. The identity must be defined at every point where it is invoked, but the skew coefficient's size does not enter (10). Estimating the full residual norm imposes the stronger sufficient condition \(|R_j|\le b_j\sqrt E\) and can unnecessarily penalize angular motion. A source-frequency-dependent angular generator has an additional signed commutator after source integration; it cannot simply be discarded as in (9).

## Quotient-free branch-specific source certificates

On the real source half-line let

\[
w(u)=e^{tu^2}\Phi(u),\qquad
\mathsf T_w A=A'+\left(2tu+\frac{\Phi'}{\Phi}\right)A,
\qquad w\mathsf T_wA=(wA)'.
\]

The complete theta source satisfies \(\Phi(u)>0\) for \(u\ge0\). The last form avoids division by \(\Phi\) in an algebraic certificate. Require \(wA\to0\) at both endpoints whenever integrating \(\mathsf T_w A\).

For the first branch, suppose prescribed real coefficients \(a_0,b_0\) and a source field \(A_0\) satisfy the pointwise identity

\[
(u^2-a_0)\cos(xu)+b_0u\sin(xu)=\mathsf T_w A_0(u).
\tag{11}
\]

Integration gives \(-h_2=a_0h_0+b_0h_1\), so on \(S_0\),

\[
\mathcal L_0=a_0E\ge-\max\{-a_0,0\}E.
\tag{12}
\]

There is no need to control \(-h_3\): its second-component pairing with \(F\) is zero on \(S_0\).

For the second branch, prescribe \(a_1,b_1,c_1,A_1\) and prove

\[
-u^3\sin(xu)-a_1\cos(xu)+b_1u\sin(xu)+c_1u^2\cos(xu)
=\mathsf T_w A_1(u).
\tag{13}
\]

This gives \(-h_3=a_1h_0+b_1h_1+c_1h_2\). On \(S_1\),

\[
\mathcal L_1=a_1h_0h_1+b_1h_1^2
\ge-\frac{\sqrt{b_1^2+a_1^2}-b_1}{2}E.
\tag{14}
\]

The coefficient is the negative part of the smallest eigenvalue of the selfadjoint matrix
\(\begin{pmatrix}0&a_1/2\\a_1/2&b_1\end{pmatrix}\).

These certificates retain full stationarity and prescribe coefficients before evaluating the physical jet. To constitute an arithmetic mechanism, \(A_j\) should be an explicit finite differential expression in the complete theta source, its modular/differential data, and prescribed phase parameters. Defining \(A_j\) by an incomplete integral of the left side merely transfers the unknown physical cancellation into an endpoint. Likewise, coefficients defined by \(-h_2/h_0\) or other unknown jet ratios do not establish local boundedness at a candidate collision.

One may add explicit source residuals to (11) and (13), but their integrated signed products must then be paid by \(E\). A raw absolute source moment gives only a square-root-energy scale and is insufficient. The half-line integrals of individual theta terms can be valid; using finitely many terms changes the source and requires retaining all omitted contributions and boundary cancellations. Negative-end Poisson obstructions concern the separate global integrations analyzed in Note 42 and are not a categorical objection to half-line terms.

No complete-theta certificates satisfying (11) and (13), or their signed residual versions, have been proved here. Equations (6)–(8) are the new unconditional averaged theorem; equations (11)–(14) specify a stronger analytic target for the still-open pointwise stationary estimate.


## Frequency-dependent angular motion retains a signed commutator

With \(v_x(u)=(\cos xu,-u\sin xu)\), \(w_t(u)=e^{tu^2}\Phi(u)\), and
\[
Q_\omega=\int_0^\infty w_t(u)\omega(u)Jv_x(u)\,du,
\]
symmetrization yields the exact formula
\[
F\cdot Q_\omega=\frac12\iint w_t(u)w_t(v)
\{\omega(u)-\omega(v)\}\det(v_x(u),v_x(v))\,du\,dv,
\]
\[
\det(v_x(u),v_x(v))
=u\sin(xu)\cos(xv)-v\cos(xu)\sin(xv).
\]
For a source supported in \(0\le u\le\pi/(2x)\), \(x>0\), the source
angle decreases and a nondecreasing \(\omega\) makes this pairing
nonnegative. The full theta source is unbounded in \(u\); its omitted
exterior cannot be discarded or paid by an absolute moment at energy
scale. This compact-source fact is therefore not a theta pointwise sign
theorem. It isolates the exact signed commutator a frequency-dependent
octonionic frame must retain.

The complementary pointwise boundary theorem and complete Gaussian
staircase payment are in [Note 46](../02_signed_cusp_control/46_OCTONIONIC_BOUNDARY_CURRENT_AND_SIGNED_CUTOFF_TARGET_20261015.md).
[Review 29](../../reviews/29_OCTONIONIC_SIGNED_BOUND_ANALYTIC_REVIEW_20261015.md)
records the analytic proof audit. No new numerical calculation is used.
