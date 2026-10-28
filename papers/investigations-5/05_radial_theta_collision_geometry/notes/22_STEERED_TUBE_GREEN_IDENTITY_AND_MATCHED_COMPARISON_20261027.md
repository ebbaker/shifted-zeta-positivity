# Complete steered-tube identity and matched radial comparison

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0008, **Continue radial theta investigation**.

**Status: proved in-note, with same-assistant internal assessment.** This completes the bounded LOC-02 calculation requested by [Note21](21_RADIAL_INTEGRAND_LOCALIZATION_CONTINUATION_20261027.md) for the selected multiplicative response and a tube of fixed angular width. Its signed Green identity and its absolute bulk allowance are the same positive multiple of their radial counterparts. The moving side has nonzero pointwise flux, but zero total signed flux. This is a precise limitation of this comparison, not of general integrand-preserving deformations. The complementary projected-flow return is [Note23](23_PROJECTED_ANNULAR_FLOW_RESPONSE_AND_LOCAL_ADJOINT_20261027.md).

The classification is a finite-domain structural identity and matched-estimator obstruction; no new RH criterion or theta inequality is proposed. Read the [result index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), [controls](../../../../result-summaries/12_collision_controls_and_screening.md), [target classification](../../../../avoid/01_restating_the_target.md), [transported-identity caution](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), and [scope rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. Domain, response, and the full operator

Fix physical time t, a real running parameter λ>0 in a compact interval, and a frozen construction frequency a_*>0 and scale b>0. Set x=log r, u=x/2, and retain the selected tails

\[
Y(x)=\int_x^\infty \frac{\sin(\sqrt\lambda(v-x))}{\sqrt\lambda}g_t(v)\,dv,
\quad Z=\partial_\lambda Y,
\quad g_t=r^{5/2}Q_t.
\]

Then Y''+λY=g_t and Z''+λZ=−Y, where these primes are x derivatives. Define

\[
\psi=r^{-1/2}Y,\quad \zeta=r^{-1/2}Z,\quad
K=Y^2+g_tZ,\quad W=YZ'-Y'Z.
\tag{1}
\]

Thus W'=−K, W(∞)=0, and

\[
W(0)=Y(0)B_\lambda-BZ(0),\quad B=-8H(t,2\sqrt\lambda).
\tag{2}
\]

Let n(r) be the collision-adapted unit vector of Note20; all r derivatives below are explicitly r derivatives. For finite 0≤s≤S set

\[
q=n(r)\cdot\omega,\quad A=\frac{s e^{sq}}{\sinh s},\quad
\ell=\log A,\quad f=A\psi,\quad h=A\zeta=\partial_\lambda f.
\]

A=1 at s=0. The axis is frozen during spectral differentiation. With V=(λ+1/4)/r² and w=A^{-2},

\[
L_s=w^{-1}\operatorname{div}(w\nabla)+V_s,
\quad V_s=V+|\nabla\ell|^2-\Delta\ell,
\quad L_sf=AQ_t,\quad L_sh=-f/r^2.
\tag{3}
\]

In particular, no homogeneous equation has replaced the forced response. The steering terms are

\[
|\nabla\ell|^2=s^2[(n_r\cdot\omega)^2+(1-q^2)/r^2],
\quad
\Delta\ell=s[(n_{rr}+2n_r/r)\cdot\omega-2q/r^2].
\tag{4}
\]

Fix 1<r_-<r_+<∞ and 0<δ<π. Write c=cos δ, d=sin δ, x_±=log r_± and

\[
D_c=\{r_-<r<r_+,\ q>c\},\qquad \alpha=(1-c)/2.
\]

All normalized volume and surface integrals below use dV/(4π) and dS/(4π); spherical averaging is P. The finite tube is piecewise smooth, with its circular edges of surface measure zero. No artificial boundary condition is imposed on f or h.

## 2. The current, drift, and potential

For any two smooth fields the weighted Green formula is

\[
\int_{D_c}w(fL_sh-hL_sf)\,\frac{dV}{4\pi}
=\int_{\partial D_c}w(f\partial_Nh-h\partial_Nf)\,\frac{dS}{4\pi}.
\tag{5}
\]

The corresponding first identity includes
\(\int w fL_sf=\int_{\partial}wf\partial_Nf-\int w|\nabla f|^2+\int wV_sf^2\), with the same measures. Thus all terms in (4) are present before polarization. In (5) the entire scalar potential cancels **pointwise**, including n_{rr}. The differentiated spectral potential has already supplied the term −f/r² in (3).

Direct product differentiation gives the particularly simple current

\[
J=f\nabla h-h\nabla f=A^2r^{-2}W\,e_r,
\quad wJ=r^{-2}W\,e_r,
\tag{6}
\]
\[
\operatorname{div}(wJ)=-r^{-3}K,
\qquad
\operatorname{div}J=-A^2r^{-3}K+2\nabla\ell\cdot J.
\tag{7}
\]

The ∇A terms in the current cancel, not in the individual gradients. Equations (4)–(7) display where the drift and potential contributions went; they have not been neglected.

## 3. The moving lateral boundary

On q=c, write ω=c n+d e(φ), with e a unit tangent circle at n. Since n_r·n=0,

\[
q_r=d\,n_r\cdot e(\phi),\quad
D=|\nabla q|=\sqrt{q_r^2+d^2/r^2},\quad
N=-\nabla q/D,\quad dS=r^2D\,dr\,d\phi.
\tag{8}
\]

The outward normal is toward decreasing q. The surface formula follows either by parametrization or the coarea formula applied to q−c. Therefore

\[
\int_{\mathrm{side}}wJ\cdot N\,\frac{dS}{4\pi}
=-\frac1{4\pi}\int_{r_-}^{r_+}W\int_0^{2\pi}q_r\,d\phi\,dr=0.
\tag{9}
\]

For the unweighted current the same calculation has the constant factor A(c)² and still gives zero. The pointwise flux is generally nonzero. Its exact unsigned amount is

\[
\int_{\mathrm{side}}|wJ\cdot N|\,\frac{dS}{4\pi}
=\frac{d}{\pi}\int_{r_-}^{r_+}|W|\,|n_r|\,dr,
\tag{10}
\]

and the unweighted amount is A(c)² times (10). Here ∫₀²π|n_r·e|dφ=4|n_r|. The collision-adapted axis has the explicit finite-parameter cost

\[
|n_r|=\frac{b|a_*u+\sin(a_*u)\cos(a_*u)|}{2r m(u)^2},
\quad n_{rr}=\frac{n_{uu}-2n_u}{4r^2}.
\tag{11}
\]

There is no all-height bound in this formula. On each declared compact annulus its denominator has a positive minimum.

The ordinary drift integral also vanishes after angular integration:

\[
\int_{D_c}2\nabla\ell\cdot J\,\frac{dV}{4\pi}
=2s\int W\,P(A^2q_r\mathbf1_{q>c})\,dr=0.
\tag{12}
\]

Rotational symmetry makes P(A²ω 1_{q>c}) parallel to n. If this correlation is discarded, the exact unsigned payment is instead

\[
\frac{2s}{\pi}\left[\int_c^1 A(v)^2\sqrt{1-v^2}\,dv\right]
\int_{r_-}^{r_+}|W|\,|n_r|\,dr.
\tag{13}
\]

These are actual steering costs, not terms covered by the first-moment mass leakage bound.

## 4. Complete finite-tube identities

Put

\[
C_s(c)=P(A^2\mathbf1_{q>c})
=\frac{s(e^{2s}-e^{2sc})}{4\sinh^2s},\quad
D_s(c)=\frac{s(e^{2sc}-e^{-2s})}{4\sinh^2s}.
\tag{14}
\]

At s=0 these are α and 1−α; C_s+D_s=s coth s. The outer and inner weighted face fluxes are αW(x_+) and −αW(x_-). Equations (5)–(9) give

\[
\boxed{\alpha\int_{x_-}^{x_+}K\,dx
=\alpha[W(x_-)-W(x_+)].}
\tag{15}
\]

For the ordinary measure, the face coefficients are C_s(c); (9) and (12) give

\[
\boxed{C_s(c)\int_{x_-}^{x_+}K\,dx
=C_s(c)[W(x_-)-W(x_+)].}
\tag{16}
\]

The complementary angular region gives precisely (15) with 1−α and (16) with D_s. Thus the induced measure removes the concentration, while the ordinary measure retains it as the same positive scalar on both sides of the signed identity.

This cancellation extends to any positive C² profile A=a(q), independent of r except through n(r), on a tube with constant c: replace C_s by (1/2)∫_c^1a(v)²dv. It does **not** assert the same conclusion for arbitrary r-dependent profiles, variable widths, non-axisymmetric cutoffs, other currents, or nonmultiplicative responses. For example, if c=c(r), the ordinary side flux is

\[
\frac12\int A(c(r))^2 W c'(r)\,dr=-\int C'(r)W\,dr,
\tag{17}
\]

which must be retained. No cutoff was used in (15)–(16).

## 5. Physical boundary, radial tails, and the matched comparison

The exact radial assembly is

\[
W(0)=\int_0^{x_-}K\,dx+\int_{x_-}^{x_+}K\,dx+\int_{x_+}^\infty K\,dx.
\tag{18}
\]

At an event B=B_λ=0, only the full sum is forced to zero. The artificial faces at r_± do not replace r=1. At the physical boundary, w(f R_sh−h R_sf)=W(0) pointwise, using the transformed boundary operator of Note20. The ordinary spherical average is (s coth s)W(0).

Here is an explicit common allowance for the omitted radial intervals. For j=0,1,2,3 set M_j(x)=∫_x^∞(v−x)^j|g_t(v)|dv. The sine kernel and its spectral derivative give

\[
|Y|\le M_1,\quad |Y'|\le M_0,\quad
|Z|\le M_3/6,\quad |Z'|\le M_2/2,
\tag{19}
\]
\[
|K|\le M_1^2+|g_t|M_3/6,
\qquad |W|\le M_1M_2/2+M_0M_3/6.
\tag{20}
\]

For example, ∂_λ[sin(√λτ)/√λ]=−∫₀^τ v sin(√λv)/(2√λ)dv has modulus at most τ³/6. Canonical tails make (20) integrable. Equations (18)–(20) give justified inner/outer payments without deleting radial contributions. They are the **same** payments in the tube comparison after dividing by its positive angular coefficient.

More precisely,

\[
\int_{D_c} A^2 r^{-3}|K|\,\frac{dV}{4\pi}
=C_s(c)\int_{x_-}^{x_+}|K|\,dx.
\tag{21}
\]

The positive norm term Y² and signed forcing term g_tZ also receive exactly the same coefficient separately. Consequently the signed-to-absolute ratio, the interval enclosure derived from any common radial enclosure of K, and the relative radial-tail allowance are unchanged. Independent absolute bounds on (10) or (13) can only add nonnegative error to this matched calculation. This is the claimed comparison, not merely normalization of H.

Ordinary quadratic leakage has fraction

\[
\frac{D_s}{C_s+D_s}=\frac{e^{2sc}-e^{-2s}}{e^{2s}-e^{-2s}},
\tag{22}
\]

whereas total quadratic mass is s coth s. Neither is the linear mass allowance in Note20. At fixed δ and large s, the quadratic exterior fraction decreases but the normalized signed comparison (21) does not improve. No infinite-s operator is used.

## 6. Exact collision control and assessment

For the manuscript's λ=6 control,

\[
Y_*=(4x^2+4)e^{-x^2},\quad Z_*=-e^{-x^2},\quad
g_*=(16x^4+24)e^{-x^2},
\]
\[
W_*=8xe^{-2x^2},\qquad K_*=8(4x^2-1)e^{-2x^2}.
\tag{23}
\]

Thus W_*(0)=W_*(∞)=0, K_* changes sign at x=1/2, and every finite-tube identity above holds while the exact double event remains. W_*>0 on every artificial radial face with x>0; a zero physical boundary current has not supplied zero tube data. The selected tails are the unique responses with the recorded rapid outer decay at this real λ, so Z_* is indeed the fixed-source spectral derivative.

The [checker and small record](../numerics/14_TUBE_AND_PROJECTED_FLOW_CHECKS_20261027.json) check exact control polynomial identities and separately labeled floating geometry/operator diagnostics, including the nonzero side term for a variable-width control. These diagnostics detect normal/drift mistakes; they do not certify theta data or the analytic theorems. [Review13](../reviews/13_TUBE_COMPARISON_AND_PROJECTED_FLOW_SELF_ASSESSMENT_20261027.md) records the full check scope.

The registered smooth Euler-factor, weighted-square, finite-prime, reflected, smooth-shape and positive-primitive controls satisfy this generic calculation on their convergence domains. No generic hypothesis here excludes them. Their absent canonical premises are respectively the unchanged arithmetic/conductor data; complete theta coefficients and full reflection; or the complete square-source marginal, as in [Brainstorm01's table](../brainstorm/01_RADIAL_INTEGRAND_PRESERVING_DEFORMATIONS_AND_COLLISION_LOCALIZATION_20261027.md). The Gaussian control lacks the theta marginal and tails. Atomic controls require a distributional extension and are not covered by this smooth proof; conditional endpoint controls retain their conditional scope. No prior numerical collision certificate was rerun.

**Disposition:** the fixed-width, axisymmetric multiplicative Wronskian comparison is complete and supplies no improvement over the matched radial comparison. Proceed to the bounded projected-flow construction in Note23. Other currents and deformations remain outside this conclusion; a theta-specific signed estimate and any positive-threshold contradiction remain open.
