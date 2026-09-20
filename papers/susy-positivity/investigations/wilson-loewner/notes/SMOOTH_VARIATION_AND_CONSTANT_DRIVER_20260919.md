# Smooth Wilson variation and the constant Loewner driver

19 September 2026. OpenAI GPT-6 (Codex), for Edward Baker.

**Status:** exact classical transport identities and a classification under
the displayed complex bulk BPS equation. The variable-scalar construction
is a bulk control, not a solution of the physical defect endpoint problem.
There are 102 finite diagnostics; no continuum quantum or RH claim.

**Subsequent calculation:** the defect projector and ordinary scalar
endpoints are analyzed in
[the endpoint note](DEFECT_PROJECTORS_AND_ENDPOINT_POLARIZATIONS_20260919.md).
The bulk-control status below is retained as the conclusion of this first
calculation; the later note supplies the additional endpoint result.

## 1. A precise Loewner description of the existing contours

Use one plane spanned by a defect tangent and its normal, with
\(z=x+iy\), \(y>0\). For \(r>0\), the common-reference semicircle,
oriented from \(r\) to zero, is

\[
z_r(\theta)=\frac r2(1+\cos\theta+i\sin\theta),\qquad 0\le\theta<\pi.
\tag{1.1}
\]

The Mobius map \(w=-1/z\) preserves the upper half-plane and gives

\[
w_r(\theta)=-\frac1r+\frac i r\tan\frac\theta2.
\tag{1.2}
\]

This is a vertical slit with starting point \(a=-1/r\). In the capacity
convention \(\partial_t g_t(w)=2/(g_t(w)-U_t)\), constant driving
\(U_t=a\) gives

\[
g_t(w)=a+\sqrt{(w-a)^2+4t},\qquad
\gamma_t=a+2i\sqrt t,\qquad
z_t=-\frac1{a+2i\sqrt t}.
\tag{1.3}
\]

Choose the square-root branch with \(g_t(w)\sim w\) at infinity.
The expansion is \(g_t(w)=w+2t/w+O(w^{-2})\), so the half-plane capacity
is \(2t\). The Loewner normalization is checked against
[Lawler, Lecture 2, Proposition 2.17 and (2.8), printed p. 19](https://math.uchicago.edu/~lawler/utah.pdf).
Equations (1.2)-(1.3) follow by direct substitution and differentiation.

The two parameters obey

\[
t=\frac{\tan^2(\theta/2)}{4r^2}.
\tag{1.4}
\]

The full semicircle completes at \(t=\infty\). Rescaling the original
endpoint by \(r\mapsto\lambda r\) rescales inverted capacity by
\(t\mapsto\lambda^{-2}t\) at fixed angle. Consequently this capacity
parameter is not yet the arithmetic coordinate \(\log r\), nor the shift
\(\omega\). Equation (1.4) is the dictionary actually obtained.

This use of inversion identifies contours. It does not assert equality of
renormalized line expectations through a conformal transformation singular
at the reference endpoint.

## 2. Fixed-charge rigidity for the inherited scalar coupling

Let \(\Gamma_1,\Gamma_3,\Gamma_I\) be Euclidean Clifford generators,
\(\{\Gamma_A,\Gamma_B\}=2\delta_{AB}\), and put
\(J=i\Gamma_I\Gamma_3\). Fix a nonzero complex spinor satisfying

\[
\epsilon_s=0,\qquad J\epsilon_c=-\epsilon_c.
\tag{2.1}
\]

These are the common bulk conditions inherited from the
[angular construction](../../wilson-lines/notes/ANGULAR_SMEARING_AND_ROBIN_MODEL_20260919.md).
For a regular real planar curve \(X=(x,y)\ne0\), take the same constant,
positive scalar coupling \(X_I|dX|\). Write \(v=|\dot X|>0\). The bulk
condition is

\[
(i\dot x\Gamma_1+i\dot y\Gamma_3+v\Gamma_I)
(x\Gamma_1+y\Gamma_3)\epsilon_c=0.
\tag{2.2}
\]

**Proposition 2.1.** Under (2.1), equation (2.2) holds precisely when

\[
\frac{\dot z}{|\dot z|}=\frac{i z^2}{|z|^2}.
\tag{2.3}
\]

Thus \(-1/z\) has constant real part and increasing imaginary part.
Connected solutions are subarcs of circles through zero with center on the
real axis, or of the degenerate imaginary-axis line. A solution connecting
the finite boundary point \(r\ne0\) to zero is the corresponding upper
semicircle, with this orientation.

*Proof.* From (2.1), \(\Gamma_I\epsilon_c=-i\Gamma_3\epsilon_c\).
Dividing (2.2) by \(i\) reduces it to

\[
(A+B\Gamma_1\Gamma_3)\epsilon_c=0,
\quad A=x\dot x+y\dot y+vy,\quad
B=y\dot x-x\dot y+vx.
\tag{2.4}
\]

Since \((\Gamma_1\Gamma_3)^2=-1\), multiplication by
\(A-B\Gamma_1\Gamma_3\) gives \((A^2+B^2)\epsilon_c=0\).
The coefficients are real and the spinor is nonzero, so \(A=B=0\).
Solving these two real equations gives

\[
\frac{\dot x}{v}=-\frac{2xy}{x^2+y^2},\qquad
\frac{\dot y}{v}=\frac{x^2-y^2}{x^2+y^2}.
\]

This is (2.3), and \(d(-1/z)/ds=iv/|z|^2\). Conversely these equations
make both coefficients in (2.4) zero. The level set
\(\Re(-1/z)=a\ne0\) is \(x^2+y^2=-x/a\), the claimed circle. QED.

For example, perturb an inverted curve to
\(w(s)=a+\varepsilon h(s)+is\). Equation (2.3) requires
\(\varepsilon h'(s)=0\). A constant perturbation merely changes the slit
location; one vanishing at both ends is trivial. A regular Loewner trace
preserving this charge and scalar coupling must therefore have constant
driving, by the normalized vertical-slit solution and uniqueness of its map.

**Scope:** this is a restriction in one fixed normal plane, with one fixed
bulk charge and constant scalar coupling. It does not classify other
supercharges, nonplanar curves, varying internal couplings, non-BPS
observables, or ensembles of constant-driver curves. It uses no endpoint
supersymmetry or physical spinor-reality assertion.

## 3. The Wilson shape derivative, including scalar and endpoint terms

Work first with smooth finite matrix fields and a regular \(C^2\) curve
\(X:[0,1]\to\mathbb R^d\). This gives an ordinary differential equation;
a regulated quantum application requires the same terms plus a specified
renormalization prescription. Let

\[
M(s)=iA_\mu(X)\dot X^\mu+\Phi(X,s)v,
\quad\Phi=n^I(s)X_I(X),\quad
U(b,a)=\mathcal P\exp\int_a^b M(s)ds.
\tag{3.1}
\]

Larger parameters stand to the left, so \(\partial_bU(b,a)=M(b)U(b,a)\).
Use \(D_\nu\Phi=\partial_\nu\Phi-i[A_\nu,\Phi]\) and
\(F_{\nu\mu}=\partial_\nu A_\mu-\partial_\mu A_\nu-i[A_\nu,A_\mu]\).
Vary \(X\) by \(\eta\) and \(n\) by \(\delta n\), with the fields fixed.

**Proposition 3.1.** The exact first variation is

\[
\delta U(1,0)=C_1U(1,0)-U(1,0)C_0
+\int_0^1U(1,s)\mathcal I(s)U(s,0)ds,
\quad C_s=iA_\nu(X(s))\eta^\nu(s),
\tag{3.2}
\]

\[
\mathcal I=
iF_{\nu\mu}\eta^\nu\dot X^\mu
+vD_\nu\Phi\,\eta^\nu
+\Phi\,\frac{\dot X\cdot\dot\eta}{v}
+vX_I\,\delta n^I.
\tag{3.3}
\]

*Proof.* Differentiate the defining ODE, obtaining
\(\delta U=\int U\delta M U\). Direct differentiation gives
\(\delta M=\dot C+[C,M]+\mathcal I\). Meanwhile

\[
\frac d{ds}\{U(1,s)CU(s,0)\}
=U(1,s)(\dot C+[C,M])U(s,0).
\]

Integrating proves (3.2). This also fixes all signs and ordering. QED.

For constant \(n\) and fixed endpoints, another integration by parts gives
the normal displacement insertion

\[
\delta U=\int_C U(1,s)\eta^\nu\mathcal D_\nu U(s,0)d\ell,
\qquad
\mathcal D_\nu=iF_{\nu\mu}T^\mu
+(\delta_\nu{}^\mu-T_\nu T^\mu)D_\mu\Phi-\Phi k_\nu,
\tag{3.4}
\]

where \(T=dX/d\ell\), \(k=dT/d\ell\). In particular
\(T^\nu\mathcal D_\nu=0\): tangential fixed-endpoint changes only
reparameterize the path. The curvature term \(-\Phi k_\nu\) is necessary
because the scalar couples to arclength. Formula (3.4) is not asserted for
varying \(n\) without its additional terms; (3.3) is the general formula.

For \(\mathcal O=\bar q(y)U(1,0)q(x)\), \(x=X(0)\), \(y=X(1)\), the
boundary terms combine with endpoint variations into

\[
\delta\mathcal O=
\eta_y^\nu(\partial_\nu\bar q+i\bar qA_\nu)(y)Uq(x)
+\bar q(y)U\eta_x^\nu(D_\nu q)(x)
+\int_0^1\bar q(y)U(1,s)\mathcal I(s)U(s,0)q(x)ds.
\tag{3.5}
\]

This applies to the defect field only when the moving endpoints remain on
the defect. Variations of endpoint R-symmetry polarizations, if present,
must be added separately.

## 4. Substituting a regular Loewner deformation

Let \(f_t=g_t^{-1}\), and choose a fixed smooth reference curve \(\zeta(s)\)
where \(f_t\) is regular, away from the driving singularity. For
\(X_t(s)=f_t(\zeta(s))\), differentiation of
\(g_t(f_t(w))=w\) gives

\[
\eta_t(s)=\partial_tX_t(s)
=-\frac{2f_t'(\zeta(s))}{\zeta(s)-U_t}.
\tag{4.1}
\]

Insert its real and imaginary parts into (3.3) and (3.5). This is a concrete
Loewner-induced Wilson evolution with the endpoint terms retained. It is
a pullback of a test contour, not a formula for the newly grown trace at
its singular tip. Endpoints on regular real boundary segments stay on the
defect in this planar model.

The growing prefix of (1.3) instead ends at a bulk point \(z_t\). Its
transported vector \(U[z_t\leftarrow r]q(r)\) carries color at that moving
tip. One cannot close it by inserting a defect field \(q(z_t)\).
A completed-curve conditional expectation or an explicitly specified
tip-state/gluing construction is needed to use those prefixes physically.

For a Brownian driver, (4.1) remains a finite-variation equation at a fixed
reference coordinate before singularities. In centered coordinates,
\(F_t(w)=f_t(w+U_t)\), with \(dU_t=\sqrt\kappa\,dB_t\), the stopped smooth
calculus instead gives

\[
dF_t(w)=\left[-\frac{2F_t'(w)}w+\frac\kappa2F_t''(w)\right]dt
+\sqrt\kappa F_t'(w)dB_t.
\tag{4.2}
\]

The Itô term comes from that change of coordinates. Neither equation defines
a Wilson scalar arclength integral on an unregulated rough trace.

### Why the formula is not yet a closed scalar generator

There is no configuration-independent multiplicative shape generator for
one Wilson observable, with coefficients determined only by the contour.
For a direct control take \(A_x=cy\), \(A_y=\Phi=0\) in an abelian theory
and the straight path \((s,0)\). Its holonomy is one for every \(c\).
Under \(\eta=(0,h(s))\), with \(h(0)=h(1)=0\),

\[
\delta U=ic\int_0^1h(s)ds.
\tag{4.3}
\]

Thus the same original observable has different shape derivatives. The
flat control \(A=d\chi\) does give shape independence at fixed endpoints.
This excludes only universal closure of that simple kind. Averaged
correlations may close through field equations, Ward identities or a
protected reduction, which remain to be supplied.

At leading free order, the common-reference transports are identity.
Keeping endpoints and their angular profiles fixed therefore leaves

\[
C_\rho(u)=\frac{e^{-|u|/2}}{1-\rho^4e^{-2|u|}}
\tag{4.4}
\]

unchanged under an interior contour deformation. The current free endpoint
kernel cannot distinguish Loewner drivers. Shape dependence must be sought
beyond that order or in an additional, explicitly defined sector.

## 5. A varying-scalar bulk control

To test the scope of Proposition 2.1, use the established tangent-coupled
ansatz \(n^I=M^I{}_\mu T^\mu\), \(M^TM=I\). Then
\(M(s)=(iA_\mu+M^I{}_\mu X_I)\dot X^\mu\).
See [Zarembo, (2.5)-(2.9), printed p. 3](https://arxiv.org/pdf/hep-th/0205160).

For a plane, choose orthogonal internal directions \(I_x,I_y\). The
commuting involutions
\(K_x=i\Gamma_{I_x}\Gamma_1\), \(K_y=i\Gamma_{I_y}\Gamma_3\)
have a nonzero common \(-1\) eigenspace in the complex Clifford module.
The projector \(P=(1-K_x)(1-K_y)/4\) obeys

\[
\big[iT_x\Gamma_1+iT_y\Gamma_3
+T_x\Gamma_{I_x}+T_y\Gamma_{I_y}\big]P=0
\tag{5.1}
\]

for every real unit tangent. This supplies the required positive control:
arbitrary smooth planar contours can obey a common bulk condition after
changing the scalar prescription. It does not preserve (2.1) by assertion.

For equal free bulk gauge/scalar propagators, the exchange numerator is
\(-\dot X\cdot\dot Y+|\dot X||\dot Y|n_X\cdot n_Y=0\).
Consequently this control supplies no contour dependence from that bulk
exchange alone. Defect interactions and endpoint terms are not included.

## 6. The physical endpoint test still needed

The endpoint variations must be solved together with the bulk conditions,
not inferred from (5.1). In
[Baker, Appendix C, (81)-(82), printed p. 25](https://arxiv.org/pdf/1102.4948),
the variations are \(\delta q_m=2\bar\zeta_{im}\Psi_i\) and
\(\delta\bar q_m=2\bar\Psi_i\zeta_{im}\). For polarized endpoints,
their corresponding contractions with \(\zeta\) must vanish at each
endpoint, subject to the defect projection and physical conjugation rules.
The paper's ray and semicircle examples illustrate why endpoint choices
matter; they do not settle the tangent-coupled construction.

The next calculation is therefore to find, or exclude within a stated
ansatz, a common physical charge and endpoint polarization for a varying-
scalar, common-reference family. Only then should one try to close its
insertion hierarchy or select a stochastic ensemble.

## 7. Checks and statement ledger

[The check program](../numerics/check_smooth_variation.py) uses independent
ordered-exponential integration versus the curvature/scalar insertion
formula, including moving endpoints and reparameterization controls. It
also checks the inverse-map geometry, nonvertical fixed-charge failures,
constant-driver controls, the varying-scalar Clifford projector, and
abelian curved/flat backgrounds. See the
[record](../numerics/records/smooth-variation-checks.json).

All 102 cases pass. The direct nonabelian finite-difference comparisons
agree within \(2.7\times10^{-10}\) on the recorded backgrounds; reducing
the variation size improves them. The integration mesh is checked at 400
and 800 steps. These are diagnostics of formulas already derived, not
certificates for quantum fields or a rough-curve limit.

| Statement | Status |
|---|---|
| Semicircle/constant-driver dictionary | Exact algebra and Loewner ODE |
| Planar rigidity under (2.1)-(2.2) | Proof above; restricted bulk hypotheses |
| Smooth matrix-field variation (3.2)-(3.5) | Exact ODE derivation |
| Regular pullback and centered-coordinate evolution | Chain rule / stopped smooth Itô calculation |
| Arbitrary-tangent scalar control | Complex bulk algebra and free bulk exchange only |
| Defect endpoint charge, reality and adjoint | Open |
| Renormalized insertion hierarchy and positivity | Open |
| Arithmetic shift, prime weights and complete transfer | Open |

The printed pages containing the cited Loewner normalization, tangent-
coupling equations and endpoint variations were visually checked. There
is no novelty claim for the standard variation formula or tangent-coupled
Wilson construction, and no independent review of the new application yet.
