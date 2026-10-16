# An exact cycle-independent test of the quartic Euler period

These are direct analytic deductions for the interacting prime sector. No numerical bound or assumption about the Riemann hypothesis is used.

## Result

For fixed \(g>0\) and \(\lambda=g/2\), no flat, convergent rapid-decay relative cycle with the identity insertion can produce the Euler period \(1/M\) on any nonempty open parameter region. This includes arbitrary constant complex linear combinations of thimbles. The exclusion follows from a third-order differential equation obeyed by every such period; it does not require guessing which saddle dominates or assuming that parity-related periods are independent.

There is an instructive escape if the interaction itself varies with the mass: \(g(M)=cM^2\), \(\lambda(M)=cM^2/2\). That family gives an exact normalized Euler period and a physical identity-class metric proportional to \(|M|^{-2}\), while remaining quartic and cross-coupled. However, its mass deformation lies in the Jacobian ideal, so its chiral mass operator is zero. It restores these Euler factors through a field dilation and a singular limit at \(M=0\), without supplying a nontrivial ordinary chiral \(tt^*\) curvature.

The first result rules out repairing the fixed-coupling model simply by changing its integration cycle. The second shows why retaining a holomorphic Euler period and obtaining useful interacting parameter geometry are separate requirements.

## 1. Cycle assumptions and normalization

Consider
\[
F_{M,g,\lambda}(U,V)
=\frac M2(U^2+V^2)+\frac g4(U^4+V^4)
+\frac\lambda2U^2V^2.
\]
The associated full superpotential has the normalization
\[
\mathcal W=\frac12[e^Y-aY+F],
\]
so its prime-sector holomorphic period uses \(e^{-F}\), not \(e^{-F/2}\).

For a locally flat family of rapid-decay relative cycles \(\Gamma_M\), write
\[
\langle P\rangle_M
=\frac1{2\pi}\int_{\Gamma_M}P(U,V)e^{-F}\,dU\wedge dV.
\]
The intended cycles have no finite-field boundary, decay sufficiently rapidly that the displayed polynomial moments and integrations by parts converge, and are transported without fitted \(M\)-dependent coefficients. Consequently differentiation with respect to \(M\) differentiates the integrand, modulo exact forms whose boundary integrals vanish. Ordinary Lefschetz thimbles and fixed relative-homology combinations, transported across chambers with their appropriate basis changes, have this meaning. The general contour framework is explained in [Witten, *Analytic Continuation of Chern–Simons Theory*](https://arxiv.org/abs/1001.2933); the calculation below is independent and finite dimensional.

These hypotheses exclude an added finite boundary, a singular insertion, a deliberately parameter-dependent linear combination of cycles, or a conditionally convergent prescription for which the boundary terms below do not vanish. Any such alternative must specify its additional physical data. No parity or exchange symmetry is imposed on \(\Gamma_M\).

## 2. A closed three-component moment system

Set
\[
s=U^2+V^2,\qquad t=U^2V^2,
\qquad I=\langle1\rangle_M,\quad
A=\langle s\rangle_M,\quad B=\langle t\rangle_M.
\]
Keep \(g,\lambda\) fixed while differentiating. Since \(\partial_MF=s/2\),
\[
I'=-\frac A2,
\qquad A'=-\frac12\langle s^2\rangle_M,
\qquad B'=-\frac12\langle st\rangle_M.
\]
The two exact integration-by-parts identities needed to close this system are
\[
\int_{\Gamma_M}
\bigl[\partial_U(Ue^{-F})+\partial_V(Ve^{-F})\bigr]
\,dU\wedge dV=0,
\]
and
\[
\int_{\Gamma_M}
\bigl[\partial_U(UV^2e^{-F})+\partial_V(VU^2e^{-F})\bigr]
\,dU\wedge dV=0.
\]
Each integrand is an exact two-form with a rapidly decaying primitive. Expanding gives
\[
2I-MA-g\langle U^4+V^4\rangle_M-2\lambda B=0,
\]
\[
A-2MB-(g+\lambda)\langle st\rangle_M=0.
\]
Using \(s^2=U^4+V^4+2t\), one obtains
\[
\boxed{
\begin{aligned}
I'&=-A/2,\\
A'&=-I/g+MA/(2g)-(g-\lambda)B/g,\\
B'&=-A/[2(g+\lambda)]+MB/(g+\lambda).
\end{aligned}}
\]
Here \(g\ne0\) and \(g+\lambda\ne0\), as in the proposed model. This is an exact reduction of the identity period and its mass derivatives to at most three independent functions. The full nine-vacuum system need not have rank three; the identity insertion along this one-parameter family probes only this closed moment subsystem.

Eliminating \(A,B\), for \(g\ne\lambda\), gives the scalar equation
\[
\boxed{
2g(g+\lambda)I'''
-(3g+\lambda)MI''
+\bigl[M^2-(3g+\lambda)\bigr]I'
+MI=0.}
\]
For example,
\[
A=-2I',\qquad
B=\frac{2gI''-MI'-I}{g-\lambda},
\]
and substitution into the third first-order equation proves the displayed formula.

At \(\lambda=g/2\), it becomes
\[
\boxed{
\mathcal L_g I:=
6g^2 I'''-7gM I''+(2M^2-7g)I'+2MI=0.
}
\]
This is a Picard–Fuchs/Schwinger–Dyson equation for these exponential periods, derived here rather than quoted from the literature.

The [exact rational checker](../numerics/check_quartic_period_identity.py) verifies this specialization's moment elimination and the reciprocal residual below. It checks the algebra following the analytic integration-by-parts identities, not the cycle hypotheses themselves.

## 3. The Euler function fails the equation

Direct substitution gives
\[
\boxed{
\mathcal L_g\!\left(\frac1M\right)
=-\frac{g(7M^2+36g)}{M^4}.
}
\]
For \(g>0\), this rational function is not identically zero on any nonempty open region. Hence \(I(M)=1/M\) is impossible there. Multiplying \(1/M\) by any nonzero constant does not help.

The conclusion applies individually to every admissible cycle and to every constant complex linear combination. A symmetry-related combination can give zero; it still obeys the same equation. Cancellations between growing saddle contributions cannot evade a differential identity satisfied by their sum. No independence assertion about the nine individual thimble periods is needed.

There is a second interpretation of the same obstruction. The three-component system has coefficients entire in \(M\), and the leading scalar coefficient \(6g^2\) is nonzero. Therefore each local identity period analytically continues as an entire solution in the finite \(M\)-plane. In particular it cannot develop a pole at \(M=0\), even though the classical critical points collide there. The pole-free linear system establishes this conclusion without requiring a separate global classification of thimbles. Stokes jumps of a chosen asymptotic basis are not poles of a fixed transported period.

The Gaussian case is singular in this respect. At \(g=\lambda=0\), the real-cycle integral is \(1/M\) for \(\Re M>0\), and confinement disappears at \(M=0\). At fixed nonzero quartic coupling the quartic remains there. Its leading homogeneous gradient has no nonzero complex zero when \(g^2\ne\lambda^2\); it continues to control infinity when the quadratic term vanishes. The strongly tame Landau–Ginzburg framework relevant to this distinction is developed by [Fan, *Schrödinger Equations, Deformation Theory and tt* Geometry*](https://arxiv.org/abs/1107.1290). Positivity and confinement can survive while the desired Euler singularity does not.

For the real cycle one can also check the first large-positive-\(M\) correction directly from Gaussian moments:
\[
I_{\mathbb R^2}(M)
\sim\frac1M\left[1-\frac{3g+\lambda}{2M^2}+O(M^{-4})\right]
=\frac1M\left[1-\frac{7g}{4M^2}+O(M^{-4})\right].
\]
This agrees with the differential equation. The exact exclusion above is stronger: it does not rely on the real cycle or on this asymptotic expansion.

## 4. An exact interacting escape, and why it is geometrically limited

The theorem fixed the quartic couplings. If changing the theory permits a mass-dependent quartic coupling, choose a constant \(c>0\) and set
\[
g(M)=cM^2,\qquad\lambda(M)=\frac c2M^2.
\]
Then
\[
F_M(U,V)=G_c(\sqrt M\,U,\sqrt M\,V),
\]
where
\[
G_c(x,y)=\frac12(x^2+y^2)
+\frac c4(x^4+y^4+x^2y^2).
\]
This is quartic and contains a cross interaction. For \(M>0\), the real-cycle change of variables gives the exact identity
\[
\frac1{2\pi}\int_{\mathbb R^2}e^{-F_M}\,dU\,dV
=\frac{C_c}{M},
\qquad
C_c=\frac1{2\pi}\int_{\mathbb R^2}e^{-G_c}\,dx\,dy>0.
\]
Normalizing once by the same period at \(M=1\) therefore yields precisely \(1/M\). For complex nonzero \(M\), use the transported cycle \(\Gamma_M=M^{-1/2}\mathbb R^2\) on a local square-root branch; the same holomorphic identity follows. This uses no fitted \(M\)-dependent boundary coefficients. It changes the bulk couplings, so the fixed-coupling differential equation does not apply: differentiating now includes their derivatives.

At \(M=0\), all coefficients of \(F_M\) vanish and confinement is lost. The eight nonzero critical points satisfy coordinates of order \(M^{-1/2}\), so they escape to infinity. This degeneration restores a place for the Euler pole. For each nonzero \(M\), the nine critical points remain nondegenerate and the degree-four part still controls infinity.

There is nevertheless an exact limitation:
\[
\boxed{
\partial_M F_M
=\frac{U\,\partial_UF_M+V\,\partial_VF_M}{2M}.
}
\]
Thus the total mass derivative is in the Jacobian ideal. For \(\mathcal W=F_M/2\), its chiral class likewise vanishes:
\[
[\partial_M\mathcal W]=0
\quad\text{in}\quad
\mathbb C[U,V]/(\partial_UF_M,\partial_VF_M),
\qquad M\ne0.
\]
One can also see this from the critical values of \(F_M\): they are \(0\), \(-1/(4c)\), and \(-1/(3c)\), independently of \(M\).

Under the ordinary chiral \(tt^*\) identification of the Higgs operator with multiplication by this class, \(C_M=0\). The equation then forces zero curvature in this parameter direction. The period's mass dependence comes from the volume-form Jacobian \(dU\wedge dV=M^{-1}dx\wedge dy\) and the specified frame. A non-Gaussian interaction has preserved the Euler factor, but has not made this mass direction nontrivial in the chiral ring.

### The same dilation determines a physical Euler metric

There is also a physical metric calculation for this scaling family. Keep the ordinary flat target metric in the \((U,V)\) coordinates and the four-supercharge Hilbert space of differential forms. Let \(\alpha_c\) be the physical harmonic representative of the identity Jacobi class \(dZ_1\wedge dZ_2\) for the \(M=1\) theory, using its natural Landau–Ginzburg Hodge identification and a fixed superpotential normalization. Strong tameness provides the harmonic representatives; the identity class is nonzero and has a finite positive norm
\[
H_c=\|\alpha_c\|^2>0.
\]
No explicit solution for \(\alpha_c\) or numerical value of \(H_c\) is needed below.

Define the holomorphic dilation
\[
\phi_M(U,V)=(Z_1,Z_2)=(\sqrt M\,U,\sqrt M\,V).
\]
It obeys
\[
\phi_M^*g_{\mathrm{flat}}=|M|g_{\mathrm{flat}},
\qquad h_M=\phi_M^*h_c,
\qquad h=\Re\mathcal W.
\]
Pullback intertwines the twisted exterior differential \(d_h=d+dh\wedge\). For a constant metric rescaling \(g\mapsto ag\), its Hilbert adjoint and Laplacian satisfy
\[
d_h^{\dagger,ag}=a^{-1}d_h^{\dagger,g},
\qquad
\Delta_{h,ag}=a^{-1}\Delta_{h,g}.
\]
Thus their harmonic kernels are unchanged by this rescaling. The corresponding statement holds for the twisted Dolbeault realization used to identify Jacobi classes, since its degree-one differential is also metric independent. This verifies the naturality of the harmonic representative under the dilation.

In real dimension four, the norm of a degree-two form is invariant under a constant conformal metric change:
\[
\|\beta\|^2_{ag}=a^{4/2-2}\|\beta\|^2_g=\|\beta\|^2_g.
\]
Consequently \(\phi_M^*\) is an isometry between the two physical middle-degree harmonic spaces when each original target is given its ordinary flat metric. Because
\[
\phi_M^*(dZ_1\wedge dZ_2)=M\,dU\wedge dV,
\]
the harmonic representative in the fixed identity-source frame is
\[
\alpha_M=M^{-1}\phi_M^*\alpha_c,
\qquad
\boxed{\quad \|\alpha_M\|^2=\frac{H_c}{|M|^2}.\quad}
\]
This is an actual interacting physical vacuum metric, not a squared holomorphic period asserted to be one. The source frame is the identity Jacobi class in the stated coordinates. The argument uses a local square-root branch; changing the branch composes with \((Z_1,Z_2)\mapsto(-Z_1,-Z_2)\). This preserves the superpotential, the metric, and the identity two-form class, so uniqueness of its harmonic representative leaves this particular source unchanged. Other vacuum classes can have nontrivial monodromy.

In the same specified normalization the two quantities are
\[
\mathcal P(M)=\frac{C_c}{M},\qquad
g_{\mathrm{id}}(M,\bar M)=\frac{H_c}{|M|^2}.
\]
The real constants \(C_c>0\) and \(H_c>0\) are different unevaluated quantities. Their equality \(H_c=C_c^2\) has not been established. A single source rescaling changes the period linearly and its physical norm quadratically; it cannot be claimed to set both constants to one. The normalized ratios \(\mathcal P(M)/\mathcal P(1)=1/M\) and \(g_{\mathrm{id}}(M)/g_{\mathrm{id}}(1)=|M|^{-2}\) are both exact.

Finally, \(\partial_M\partial_{\bar M}\log g_{\mathrm{id}}=0\) away from zero, consistently with the vanishing chiral mass class. The holomorphic frame change \(\alpha_M\mapsto M\alpha_M\) removes its local Euler denominator. Its significance remains relative to a physically specified source. The scaling family supplies a non-Gaussian physical Euler metric, but still does not determine the normalization needed for the full arithmetic contact or convert the pole terms into a positive pairing.

## 5. Consequences for the next theory

For the proposed fixed quartic model, choosing another ordinary thimble or a constant combination of boundary states with the identity insertion cannot recover the elementary Euler period. A viable next construction must change something substantive: the bulk deformation, the physical insertion or boundary problem, or the observable being matched. Merely invoking the extra vacua does not remove the exact differential constraint.

The scaling family shows a sharper next criterion. Seek an interacting deformation that retains the required arithmetic amplitude and its singular degeneration while its relevant parameter operator survives in the Jacobian ring. If the deformation is only a holomorphic field dilation, the resulting Euler factor can remain entirely a source/frame effect, just as in the quadratic benchmark.

Alternatively, a construction may seek a physical Hermitian pairing that is not this identity period. Neither the fixed-coupling no-go nor the scaling example excludes that route. It would need its own explicitly specified source, observable, and normalization identity. None of the period statements here establishes positivity of the complete Weil form.

## Sources and status

The moment system, scalar differential operator, universal-cycle exclusion, and scaling-family test are original calculations in this note. Their derivations are explicit; they have not undergone independent specialist review. The sources are used only for the general contour and supersymmetric analytic settings:

- Edward Witten, [*Analytic Continuation of Chern–Simons Theory*](https://arxiv.org/abs/1001.2933), 2010.
- Huijun Fan, [*Schrödinger Equations, Deformation Theory and tt* Geometry*](https://arxiv.org/abs/1107.1290), 2011.
