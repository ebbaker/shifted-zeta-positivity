---
research_program: ALG
secondary_programs: [PR02, PR02-CORR]
status: exact_disk_completion_and_centered_source_positivity_pointwise_target_open
---

# Polarized Hodge disk identity and centered source positivity

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This is an analytic research continuation; no numerical pilot or new pointwise collision exclusion is asserted.

[Note 50](50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md) realizes the signed theta expression as a polarized pairing of closed self-dual forms. Here that pairing has an exact planar Dirichlet completion, with a sharp boundary payment. Separately, the complete positive theta source gives nonnegative averages of both branches for a class of weights centered at the source's reflection origin, including every centered Gaussian. These strengthen the available integrated information but do not supply the stationary physical-energy estimate. [Note 47](47_ORIENTED_CURRENT_AND_ACCRETIVE_SOURCE_CERTIFICATES_20261015.md) provides the complementary translated spatial estimate and source-certificate target.

## 1. The signed density is a transverse second derivative

For holomorphic \(f\), set
\[
\ell_f(z)=|f'(z)|^2-\operatorname{Re}(f(z)\overline{f''(z)}),
\qquad U(x,y)=|f(x+iy)|^2.
\]
The Cauchy–Riemann equations give the exact identities
\[
\boxed{\ell_f=\tfrac12U_{yy}
=2|f'|^2-\tfrac12U_{xx}.}
\tag{1}
\]
For real-reflection data, \(f(\bar z)=\overline{f(z)}\), one has \(U_y(x,0)=0\). This vanishing normal derivative does not determine the sign of \(U_{yy}(x,0)\). On the real line, \(\ell_{h_j}=\mathcal L_j\); off it, this is precisely Note 50's Hermitian extension.

## 2. Exact disk completion and sharp boundary loss

Let \(D_R=\{|z-x_0|<R\}\), with \(x_0\) real, and assume \(f\) is holomorphic near its closure. Define
\[
g_R(z)=\left(1-\frac{(z-x_0)^2}{R^2}\right)f(z).
\]
Then
\[
\boxed{
\int_{D_R}\ell_f\,dA
+\frac1{2R}\int_{\partial D_R}|f|^2\,ds
=\frac12\int_{D_R}|g_R'|^2\,dA\ge0.}
\tag{2}
\]
The quantity on the right is a positive Dirichlet integral. The boundary payment on the left retains the information that a norm-only argument would otherwise lose.

**Proof.** Expand \(f(x_0+R\zeta)=\sum_{n\ge0}b_n\zeta^n\), setting \(b_{-1}=b_{-2}=0\). Orthogonality of angular modes gives
\[
\frac1\pi\int_{D_R}\ell_f\,dA
=\sum_{n\ge0}n|b_n|^2
-\operatorname{Re}\sum_{n\ge0}(n+2)b_n\overline{b_{n+2}},
\tag{3}
\]
\[
\frac1{2\pi R}\int_{\partial D_R}|f|^2\,ds=\sum_{n\ge0}|b_n|^2,
\qquad
\frac1\pi\int_{D_R}|g_R'|^2\,dA
=\sum_{n\ge1}n|b_n-b_{n-2}|^2.
\]
Expanding the last square proves (2). The stated regularity justifies all series operations.

The loss coefficient is sharp even among real-reflection polynomials stationary at the disk center. Put
\[
f_N(z)=\sum_{m=0}^N\left(1-\frac m{N+1}\right)
\left(\frac{z-x_0}{R}\right)^{2m}.
\]
Writing \(B_R=(2R)^{-1}\int_{\partial D_R}|f_N|^2ds\), direct summation gives
\[
B_R=\pi\frac{(N+2)(2N+3)}{6(N+1)},\qquad
\frac{\int_{D_R}\ell_{f_N}\,dA}{B_R}
=-\frac{2N}{2N+3}\longrightarrow-1.
\tag{4}
\]
Here \(f_N(x_0)=1\) and \(f_N'(x_0)=0\), while the integrated negative loss grows without bound. Thus even a fixed-radius disk estimate paid only by the central first-jet energy cannot hold for arbitrary holomorphic fields. No sharpness claim is made for the theta subfamily.

Equation (1) also gives the ordinary boundary-flux identity
\[
\int_{D_R}\ell_f\,dA=\frac12\int_{\partial D_R}U_y n_y\,ds.
\tag{5}
\]
For an annulus \(r<|z-x_0|<R\), this is the outer disk flux minus the inner disk flux. The inner boundary is an additional signed term; it cannot be omitted to obtain positivity. Neither (2) nor (5) relies on a singular double-boundary kernel from the older drafts.

## 3. Complete-source positivity for centered weights

Use the existing normalization
\[
H(t,z)=\int_0^\infty w_t(u)\cos(zu)\,du,
\qquad w_t(u)=e^{tu^2}\Phi(u)>0,
\qquad h_j=\partial_z^jH.
\]
Let \(\chi\) be a nonzero, real, even, nonnegative integrable weight and define
\[
\widehat\chi(\xi)=\int_{\mathbb R}\chi(x)\cos(\xi x)\,dx,
\qquad
W_j(t,y)=\int_{\mathbb R}\chi(x)\ell_{h_j}(t,x+iy)\,dx.
\]
If \(\widehat\chi\ge0\), then \(W_0(t,y)>0\). If, additionally, \(\widehat\chi\) is nonincreasing on \([0,\infty)\), then \(W_1(t,y)>0\). These conclusions hold for every real \(t,y\). In particular, for \(\chi_a(x)=e^{-a^2x^2}\), \(a>0\), both statements hold because
\[
\widehat\chi_a(\xi)=\frac{\sqrt\pi}{a}e^{-\xi^2/(4a^2)}.
\tag{6}
\]

Here is a direct proof with all constants. Set \(\rho_t(u)=w_t(|u|)/2\) on the full frequency line, so \(H(t,z)=\int_{\mathbb R}\rho_t(u)e^{iuz}du\). Symmetrizing the second-derivative term yields
\[
\ell_{h_j}(t,x+iy)
=\frac12\iint_{\mathbb R^2}
\rho_t(u)\rho_t(v)(uv)^j(u+v)^2
\cos((u-v)x)e^{-(u+v)y}\,du\,dv.
\tag{7}
\]
Integration against \(\chi\), followed by folding the four frequency quadrants, gives
\[
\boxed{
W_j(t,y)=\frac14\int_0^\infty\!\int_0^\infty
w_t(u)w_t(v)(uv)^j
\left[
(u+v)^2\widehat\chi(u-v)\cosh((u+v)y)
+(-1)^j(u-v)^2\widehat\chi(u+v)\cosh((u-v)y)
\right]du\,dv.}
\tag{8}
\]
For \(j=0\), both terms are nonnegative. For \(j=1\), the first dominates the second: \(u+v\ge|u-v|\), the Fourier transform decreases with absolute frequency, and \(\cosh\) increases with its nonnegative argument. Strict positivity follows on a set near \(u=v>0\), since \(\widehat\chi(0)>0\) and the source is positive. The complete source's double-exponential tail dominates every polynomial and every factor \(e^{|y|(|u|+|v|)}\), uniformly on compact real-time intervals. This justifies differentiation, symmetrization, and integration without a theta-index cutoff.

At \(y=0\), (8) proves nonnegative centered averages of each physical branch and their sum. This removes the negative payment appearing in Note 47 for these centered weights. The additional conclusion uses positivity of the complete source, rather than holomorphicity alone.

## 4. What translation and localization cost

The origin in (8) is essential. Replacing \(\chi(x)\) by \(\chi(x-x_0)\) inserts \(\cos((u-v)x_0)\) in its first term and \(\cos((u+v)x_0)\) in its second. These factors can change sign independently. The proof therefore does not transfer to a general stationary point, and its frequency comparison supplies no bound by the physical energy \(E=h_0^2+h_1^2\) there.

Similarly, the boundary norm in (2) is an auxiliary spectral-circle quantity. It is not controlled by the central physical energy merely because the forms are closed, self-dual, or reflected. Equation (4) explicitly separates these quantities. The positive Dirichlet remainder also does not imply that the signed density at the disk center is nonnegative.

An exact positive-source example quantifies this last distinction. Fix \(a,k>0\) and an event time \(T\), and let
\[
H(t,z)=a+b(t)\cos(kz),\qquad b(t)=a e^{k^2(t-T)}.
\tag{9}
\]
This is a backward-heat solution with a positive atomic cosine source. At \(x_*=\pi/k\) and \(\delta=T-t>0\), write \(\varepsilon=a-b(t)>0\). Then
\[
h_1=0,\qquad E=\varepsilon^2,\qquad
\mathcal L_0=-bk^2\varepsilon,\qquad
\frac{\mathcal L_0}{E}
=-\frac{k^2}{e^{k^2\delta}-1}
=-\frac1\delta+O(1).
\tag{10}
\]
On a disk centered at \(x_*\), put \(\zeta=z-x_*\), so \(f(\zeta)=a-b\cos(k\zeta)\). Direct calculation gives
\[
\ell_f=b^2k^2\cosh(2k\operatorname{Im}\zeta)
-abk^2\operatorname{Re}\cos(k\zeta).
\]
The harmonic mean-value identity and a termwise disk integration give
\[
\boxed{
\frac1{\pi R^2}\int_{D_R(x_*)}\ell_f\,dA
=k^2b^2\left[M(kR)-e^{k^2\delta}\right],
\qquad M(s)=\frac{I_1(2s)}s
=\sum_{n=0}^\infty\frac{s^{2n}}{n!(n+1)!}.}
\tag{11}
\]
The series defines the displayed modified-Bessel expression, including \(M(0)=1\). Every fixed \(R>0\) has \(M(kR)>1\). Consequently its disk average is positive sufficiently close to the event, while the central signed density remains negative and its energy-relative ratio diverges.

Since \(M\) is strictly increasing for positive arguments and \(M(s)=1+s^2/2+O(s^4)\), the unique radius at which the average changes sign satisfies
\[
R_{\mathrm{crit}}^2=2\delta+O(\delta^2).
\tag{12}
\]
The disk average is negative only for \(R<R_{\mathrm{crit}}\). Thus detecting this adverse central sign forces the spectral disk to shrink at the collision scale. The example is a control, not the theta source; it proves that positive-source structure alone does not bridge this localization gap.

The new results are (2), its sharpness within the general holomorphic class, and the complete-theta centered positivity (8). The remaining research target is a theta-specific restriction that controls translated signed boundary data at physical-energy scale. The manuscript, finite certificates, and existing pointwise domains are unchanged.
