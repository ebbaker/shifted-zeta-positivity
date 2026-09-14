# The interaction-shape period and its normalization constraint

This note continues the investigation after the first manuscript was saved. It derives an exact differential equation for the reference shape period and proves that changing this shape cannot preserve the elementary Euler period with a fixed identity source. The calculation is analytical; no numerical positivity estimate is used.

## 1. One reference function controls the new deformation

Use the two-complex-field polynomial
\[
G_c(A,B)=\frac12(A^2+B^2)+\frac c4(A^4+B^4+A^2B^2).
\]
Set \(s=A^2+B^2\), \(q_4=A^4+B^4+A^2B^2\). The physical conventions are
\[
\mathcal W_c=G_c/2,\qquad
D=\frac{Q_1-iQ_2}{2}=\bar\partial+\partial\mathfrak f_c\wedge,
\qquad \mathfrak f_c=G_c/4.
\]
Thus the canonical Higgs operator in this twisted-Dolbeault convention is multiplication by \([q_4/16]\). The superpotential variation \([q_4/8]\) is twice that operator. This fixes a factor that does not affect the previous zero-class exclusion but matters for a nonzero curvature equation. The physical Hamiltonian is \(H=2\{D,D^\dagger\}\).

The identity period being tested is separately specified:
\[
\mathcal C(c)=\frac1{2\pi}\int_{\mathbb R^2}
\exp[-s/2-cq_4/4]\,dA\,dB,\qquad \Re c>0.
\]
Its weight is \(e^{-G_c}\); it is not an assumed Hilbert norm and not automatically a canonically normalized physical brane state. The distinction between physical Hodge pairings and holomorphic periods is part of the supersymmetric framework, as developed by [Fan](https://arxiv.org/abs/1107.1290) and [Cecotti, Gaiotto and Vafa](https://arxiv.org/abs/1312.1008). The identities below are direct calculations for this polynomial.

For each compact subset of \(\Re c>0\), quartic decay uniformly dominates every derivative of the integrand. Therefore \(\mathcal C\) is holomorphic there. On \(c>0\), it is the Laplace transform of the strictly positive random variable \(q_4/4\) under the standard two-dimensional Gaussian measure. In particular,
\[
(-1)^k\mathcal C^{(k)}(c)
=\frac1{2\pi}\int_{\mathbb R^2}(q_4/4)^k e^{-s/2-cq_4/4}\,dA\,dB>0,
\qquad k\ge0.
\]
The strict inequality for \(k>0\) follows since \(q_4\) vanishes only at the origin on the real plane. Hence \(\mathcal C\) is strictly decreasing and nonconstant. This is an identity-based selection test, not a bound on a sampled arithmetic form.

## 2. A differential equation for the shape period

Temporarily introduce independent parameters
\[
I(M,g)=\frac1{2\pi}\int_{\mathbb R^2}
\exp[-Ms/2-gq_4/4]\,dA\,dB.
\]
The fixed-quartic period calculation established
\[
6g^2\partial_M^3 I-7gM\partial_M^2I
+(2M^2-7g)\partial_MI+2MI=0.
\]
It holds for the specified convergent cycles and their admissible flat transports. Here changing \(g\) changes all the quartic terms while their ratio stays fixed.

Integration by parts in the radial dilation direction gives the independent homogeneity identity
\[
(M\partial_M+2g\partial_g)I=-I.
\]
Indeed the integral of \(\partial_A(Ae^{-F})+\partial_B(Be^{-F})\) vanishes, where \(F=Ms/2+gq_4/4\), and its expansion is \(2I-M\langle s\rangle-g\langle q_4\rangle=0\).

Let \(A_n(c)=\partial_M^n I(1,c)\), so \(A_0=\mathcal C\). Differentiating homogeneity yields
\[
A_{n+1}=-(n+1)A_n-2cA_n'.
\]
Consequently
\[
\begin{aligned}
A_1&=-\mathcal C-2c\mathcal C',\\
A_2&=2\mathcal C+10c\mathcal C'+4c^2\mathcal C'',\\
A_3&=-6\mathcal C-54c\mathcal C'-48c^2\mathcal C''-8c^3\mathcal C'''.
\end{aligned}
\]
Substitution into the fixed-mass differential equation gives
\[
\boxed{
48c^4\mathcal C'''+(288c^3+28c^2)\mathcal C''
+(324c^2+56c+4)\mathcal C'+(36c+7)\mathcal C=0.
}
\]
This equation is regular on \(c\ne0\) as an ordinary differential equation, while zero is a singular point. It determines the identity period's transport once the appropriate cycle solution is selected; it does not determine the physical vacuum metric.

As an independent local check, the Gaussian moments give the right derivatives
\[
\mathcal C(0+)=1,\quad
\mathcal C'(0+)=-\frac74,\quad
\mathcal C''(0+)=\frac{297}{16},\quad
\mathcal C'''(0+)=-\frac{31815}{64}.
\]
Thus on the positive real axis
\[
\mathcal C(c)=1-\frac74c+\frac{297}{32}c^2+O(c^3).
\]
These are one-sided asymptotic jets. No convergent Taylor expansion through the singular point is asserted. Finite-order remainder estimates follow directly by integrating the Taylor remainder of \(e^{-cq_4/4}\) against the Gaussian measure.

The [exact checker](../numerics/check_shape_period.py) independently verifies the homogeneity derivative hierarchy, the differential-equation substitution, and nine coefficients obtained from Gaussian moments. Its [small record](../numerics/records/shape-period.json) states what these checks do and do not establish.

## 3. A fixed identity source cannot retain the Euler period while changing shape

For the mass-scaled family with a now variable shape, put
\[
F_M(U,V)=G_{c(M)}(\sqrt M\,U,\sqrt M\,V),
\]
where \(M\ne0\), \(c(M)\) is holomorphic into \(\Re c>0\), and the identity cycle is the pullback of the real plane. The period is exactly
\[
\mathcal P(M)=\frac{\mathcal C(c(M))}{M}.
\]
A constant source multiplier merely changes its fixed overall normalization.

**Proposition.** On a connected complex parameter domain, requiring this period to equal \(K/M\), with a fixed constant \(K\), forces \(c(M)\) to be constant.

**Proof.** The requirement is \(\mathcal C(c(M))=K\). If \(c\) were nonconstant, its image would be open by the open-mapping theorem. The holomorphic function \(\mathcal C\) would then be constant on an open subset of the connected right half-plane, hence everywhere there. This contradicts its strict decrease on the positive real axis. Locally near a positive shape, the same conclusion follows from \(\mathcal C'(c)<0\) and the inverse-function theorem.

The conclusion is about the specified identity insertion, cycle and scalar normalization. It does not exclude other observables, changes of boundary problem, a vector of source classes, or a physical pairing that does not require this period to stay fixed.

## 4. What a compensating source actually does

On a patch where \(\mathcal C(c)\ne0\), a holomorphic multiplier
\[
r(c)=\frac{\mathcal C(c_0)}{\mathcal C(c)}
\]
restores the Euler period, for any chosen reference shape \(c_0>0\). The corresponding physical identity metric becomes
\[
\|r(c(M))\alpha_M\|^2
=\frac{|\mathcal C(c_0)|^2}{|M|^2}
\frac{H(c(M),\overline{c(M)})}{|\mathcal C(c(M))|^2}.
\]
Thus the invariant quantity is
\[
\mathcal R(c,\bar c)=\frac{H(c,\bar c)}{|\mathcal C(c)|^2}.
\]
This formula removes a possible ambiguity in the next task: keeping a holomorphic factor by rescaling the source does not also preserve its physical metric. The source compensation is an algebraic option, not an independently justified physical boundary law.

The subsequent [physical-pairing test](07_PHYSICAL_PAIRING_TEST.md) establishes a stronger restriction using an exact phase symmetry of the physical Hamiltonian. In this family the physical identity metric is radial in \(c\), whereas the squared holomorphic period is not radial on any open region. The resulting ratio is nonconstant on every complex-open patch. Therefore even a common scalar source compensation cannot keep both the Euler period and Euler metric along a nonconstant holomorphic shape deformation. That statement retains the physical metric and source conventions specified here.

## 5. Why this is useful for theory selection

The calculation does not show that interactions are unhelpful. It identifies the first interaction deformation precisely enough to test the observable it was supposed to preserve. The mass-scaled fixed-shape theory remains a successful interacting control. Varying its shape introduces a nonzero chiral operator, but a single fixed identity period cannot conceal that change.

The next credible enlargement must change more than a scalar source normalization: for example, a physically specified multi-state boundary pairing, a new insertion or target metric, or a gluing mechanism that directly yields the arithmetic bilinear form. A comparison of vacuum metrics becomes informative once that physical source is supplied. The complete Weil contact, poles and infinite-dimensional preparation map remain unresolved.
