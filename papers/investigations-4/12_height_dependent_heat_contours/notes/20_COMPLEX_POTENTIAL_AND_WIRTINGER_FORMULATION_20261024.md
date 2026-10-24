# Complex derivatives and a complex potential for the zero field

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded reasoning effort max**. Same-assistant derivation and symbolic checks.

This answers the author's notation question about `eq:SP` in [book.tex](../manuscript/book.tex). It is an exact reformulation of the existing equations, with no new estimate or restriction on collisions. Reading anchors: the [result index](../../../../result-summaries/README.md), especially [local heat geometry and the complex-field result](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), and the [avoid index](../../../../avoid/README.md), especially [coordinate reformulations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [normalization checks](../../../../avoid/08_normalization_and_constant_slips.md). The initial derivation left the manuscript unchanged; the author-requested integration is recorded below.

## 1. The compact formulation

Retain the book's definitions and its constant regulator:

\[
z=x+iy,\quad H_t=-H_{zz},\quad D=|H|^2+\epsilon^2,
\quad A=\frac{\epsilon H_z}{\sqrt\pi D},\quad\rho=|A|^2.
\]

For all smooth fields, define the Wirtinger derivatives

\[
\partial_z=\tfrac12(\partial_x-i\partial_y),\qquad
\partial_{\bar z}=\tfrac12(\partial_x+i\partial_y).
\]

They satisfy

\[
\Delta=4\partial_z\partial_{\bar z},\qquad
\partial_x\partial_y=i(\partial_z^2-\partial_{\bar z}^2).
\]

Let \(S=\log D\) and introduce the complex potential

\[
W=2S_{zz}
=2\left(\frac{\overline H H_{zz}}D
-\frac{\overline H^{\,2}H_z^2}{D^2}\right).
\]

Since \(S\) is real and \(S_{z\bar z}=\pi\rho\),

\[
V=-2S_{xy}=2\operatorname{Im}W,\qquad
W_{\bar z}=2\pi\rho_z.
\]

Thus the book's Schrödinger–Poisson equations become

\[
\boxed{\begin{aligned}
A_t&=A_{\bar z\bar z}-A_{zz}+(\overline W-W)A,\\
W_{\bar z}&=2\pi\partial_z|A|^2.
\end{aligned}}
\tag{1}
\]

The scalar potential in the Schrödinger equation remains real: \(i(\overline W-W)=V\). The extra real component of \(W\) packages the spatial constraint. All displayed formulas are smooth at zeros of \(H\) and \(H_z\) for \(\epsilon>0\).

For a direct check of the Poisson coefficient,

\[
\Delta V=2\operatorname{Im}(4\partial_z W_{\bar z})
=16\pi\operatorname{Im}\rho_{zz}
=-8\pi\rho_{xy}.
\]

## 2. Equivalence and the potential ambiguity

Conversely, let \(V\) and \(\rho\) be real smooth functions satisfying the book's Poisson equation. Write \(W=u+iV/2\). The second equation in (1) is exactly

\[
u_x=2\pi\rho_x+\tfrac12 V_y,\qquad
u_y=-2\pi\rho_y-\tfrac12 V_x.
\]

The equality of mixed derivatives is precisely \(\Delta V=-8\pi\rho_{xy}\). Hence a corresponding \(u\) exists on every simply connected spatial patch, uniquely up to a real spatial constant (which may depend on time). That constant cancels from \(\overline W-W\). On a multiply connected domain, periods must also be checked.

If only the constraint for \(W\) is prescribed, its ambiguity is addition of a holomorphic function. This changes \(V\) by a harmonic function, reproducing the original Poisson ambiguity. For the lifted field, \(W=2\partial_z^2\log D\) selects a specific potential. Global Fourier inversion still requires the book's stated hypotheses; the complex notation does not establish them for theta.

For example, the translation-invariant choice, where applicable, is

\[
\widehat W(k_x,k_y)=2\pi\frac{k_x-ik_y}{k_x+ik_y}\widehat\rho(k_x,k_y),\qquad k\ne0.
\]

For real \(\rho\), its \(2\operatorname{Im}W\) has multiplier \(-8\pi k_xk_y/(k_x^2+k_y^2)\), exactly the book's selected real potential. The zero frequency is treated under the same functional assumptions as in the book.

## 3. A complex field is not necessarily a holomorphic field

Although \(H_{\bar z}=0\),

\[
A_{\bar z}=-S_{\bar z}A
=-\frac{\epsilon}{\sqrt\pi}
\frac{H\,|H_z|^2}{D^2}.
\]

Consequently \(A\) is generally nonholomorphic. The potential is likewise generally nonholomorphic because \(W_{\bar z}=2\pi\rho_z\). One must retain both Wirtinger derivatives. In particular, \(A_{\bar z\bar z}\) cannot be replaced with \(\overline{A_{zz}}\).

The spatial domain is still two real dimensions, represented by one complex coordinate. Complex notation is natural for the analytic seed, amplitude and currents; real coordinates remain useful for boundaries and quadratic forms. With \(X=(x+y)/\sqrt2\) and \(Y=(y-x)/\sqrt2\),

\[
-\partial_{xy}=-\tfrac12(\partial_{XX}-\partial_{YY}),
\]

which displays the indefinite kinetic operator. A complex rewriting does not turn it into the usual elliptic Schrödinger Laplacian.

## 4. The current also simplifies

For any smooth complex amplitude, the book's current has the exact expression

\[
j=\overline A\,\partial_z A-A\,\partial_z\overline A.
\]

Its real and imaginary parts are the book's \(x\)- and \(y\)-currents. The continuity equation becomes

\[
\rho_t+\partial_z j+\partial_{\bar z}\overline j=0.
\]

For the holomorphic lift this reduces to \(j=\epsilon^2H_{zz}\overline{H_z}/(\pi D^2)\). On a phase chart \(A=R e^{i\theta}\), it reads \(j=2i\rho\theta_z\), so the phase velocity is \(v=2i\theta_z=\theta_y+i\theta_x\).

## 5. Direct comparison with complex DS-II notation

Put \(w=e^{-i\pi/4}z\) and define, with \(z=e^{i\pi/4}w\),

\[
U(t,w)=\sqrt\pi\,A(t,z),\qquad Q(t,w)=iW(t,z).
\]

No time rescaling is needed for this particular convention. Equation (1) gives

\[
U_t=i\{U_{ww}+U_{\bar w\bar w}+(Q+\overline Q)U\},
\qquad Q_{\bar w}=2\partial_w|U|^2.
\]

This is the normalization of **the introductory equation (1)** in [Taimanov, arXiv:2111.07251v1](https://arxiv.org/html/2111.07251v1). That passage was checked on 24 October 2026. The later theorem display in that version places the factor two differently, so formulas should be compared using the displayed normalization, not merely the name DS-II. Only the differential-system comparison is used. The [reference catalog](../references/sources.json) retains the existing article provenance and external PDF receipt.

For presentation, use (1) as the compact complex form and retain `eq:SP` as its real-coordinate equivalent. The gain is a shorter field/current calculus and a direct literature dictionary; there is no additional positivity or collision exclusion.

## Verification

The [exact generic-jet check](../numerics/20_check_complex_potential.py) verifies the evolution, complex constraint, real-potential recovery, density, current, continuity, nonholomorphic derivative and Fourier coefficient. [Execution record](../numerics/20_COMPLEX_POTENTIAL_CHECKS_20261024.json). The jet calculation uses no division by \(H\) or \(H_z\), so it includes critical and multiple points. These are same-assistant algebra checks; the local converse and domain qualifications are established by the displayed differential argument.

## Author-requested manuscript integration

24 October 2026, **gpt-6-astra (Codex), actual effort max**, for Edward Baker with substantial LLM assistance. The author then requested this presentation in [book.tex](../manuscript/book.tex). Both Wirtinger derivatives and the complex potential now enter the setup, and the complex system leads the field theorem. Its proof, current, selected Fourier potential, DS-II dictionary and normalized-state/residual equations use the same convention. The original real `eq:SP` and real energy geometry remain. The later observable source was updated consistently with the new residual. [Same-assistant review](../reviews/18_COMPLEX_POTENTIAL_PRESENTATION_REVIEW_20261024.md) and [16-page build receipt](../manuscript/BOOK_COMPLEX_POTENTIAL_BUILD_RECORD_20261024.json). No new theta estimate or manuscript snapshot.
