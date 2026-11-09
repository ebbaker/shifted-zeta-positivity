# Gaussian height localization for marked zero marginals

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Runtime model `gpt-6.1-sol`,
reasoning effort unavailable. OC chat0008. The author proposed using
a Gaussian height weight to simplify explicit calculations from the
complete theta source. Root is the sole writer, with read-only analytical
checks at inherited configuration.

**Status.** Exact Gaussian identities and conditional-on-inherited-inputs
convergence estimates, with internal author checks. This note prepares
B10 to decide whether the simpler kernel buys a useful canonical
estimate. It supplies the complete Gaussian-weighted representation
and tail control. A joint logarithmic estimate with a useful error and
a canonical pair profile are still open.

The [result index][results] and [avoid index][avoid] route to
[geometry13][geometry], [theta14][theta], [controls12][controls],
[classification01][a01], [premises02][a02] and [scope07][a07].
This is a localization and source-access question for an empirical
factorial marginal. Collision exclusion and a Vandermonde joint law
would each need additional hypotheses and estimates.

## 1. Keep the two Gaussian choices distinct

Use the complete canonical family
\[
 H_\lambda(z)=\int_0^\infty e^{\lambda t^2}\Phi(t)\cos(zt)\,dt,
 \qquad 0\le\lambda\le1/2 .
\]
Write \(z_j=x_j+iy_j\), with distinct labels for multiplicity copies.
The [compact-window E10 proof][e10] weights zeros by a compact
horizontal taper, multiplies by a transverse cutoff \(\kappa_0\),
and blurs their observed locations by a planar Gaussian of physical
width \(\epsilon\). The author's change replaces the horizontal taper
by
\[
 w_{X,h}(x)=e^{-(x-X)^2/(2h^2)},\qquad
 W_{X,h}(x+iy)=w_{X,h}(x)\kappa_0(y).
 \tag{1}
\]
The transverse cutoff is 1 on the whole canonical strip \(|y|\le1\)
and vanishes for \(|y|\ge2\). It keeps source-side tests in a fixed
vertical band. Here \(h\) is a standard deviation. In E10, \(h=1\)
was a compact support radius. The same numerical choice of \(h\)
therefore changes the observed statistic.

For comparison with [B06][b06] keep the center law \(X\) uniform on
\([T,2T]\), \(\ell=\min(1,4\pi/\log T)\), \(\epsilon=\ell/4\),
\(J=\ell^2\) and \(u,v\in Q=[-1,1]+i[-1,1]\). Hold \(h>0\) fixed,
with \(h=1\) for the proposed initial comparison. Define
\[
 \begin{aligned}
 f_{X,u}(z)&=J W_{X,h}(z)G_\epsilon(X+\ell u-z),\\
 r_X(u)&=\sum_j f_{X,u}(z_j),\qquad
 d_X(u,v)=\sum_j f_{X,u}(z_j)f_{X,v}(z_j),\\
 R_{2,X}(u,v)&=\sum_{j\ne k}f_{X,u}(z_j)f_{X,v}(z_k)
                    =r_X(u)r_X(v)-d_X(u,v).
 \end{aligned}                                                    \tag{2}
\]
\(G_\epsilon\) is the normalized planar Gaussian. Averaging uses
the same \(X\) within each product. The connected density subtracts
\(\mathbb E_X r_X(u)\,\mathbb E_X r_X(v)\) from the averaged
\(R_{2,X}\). The self term has \(W_{X,h}^2\), and separate labels at
the same zero survive in the factorial pair. Counts are unnormalized.
Both imaginary marks survive.

These weights define how the actual zeros are observed. The weight in
a [Vandermonde ensemble density][vdw] instead defines the law of all
the coordinates before taking a marginal. A model comparison could
apply (1)–(2) to both its pair marginal and the empirical one.

## 2. Exact separation of the height kernel

For \(m=(x_j+x_k)/2\) and \(d=x_j-x_k\), completing the square gives
\[
 w_{X,h}(x_j)w_{X,h}(x_k)
   =e^{-(m-X)^2/h^2}\,e^{-d^2/(4h^2)} .
 \tag{3}
\]
The window therefore has a midpoint width \(h/\sqrt2\) and a
height-difference width \(\sqrt2 h\). This factors the window
weights. In the full \(R_{2,X}\), the observation kernels still
depend on \(X\), so their product stays inside the average.

For a test expressed directly in physical separation and imaginary
marks and independent of \(X\), the average of the window weights is
\[
 \frac{h\sqrt\pi}{2T} e^{-d^2/(4h^2)}
 \left[\operatorname{erf}\!\left(\frac{2T-m}{h}\right)-
       \operatorname{erf}\!\left(\frac{T-m}{h}\right)\right].
 \tag{4}
\]
This is an exact finite-interval midpoint factor, including both
edges of the center range. It is available for a declared separation
projection, while the primary profile retains the two location
coordinates. Integrating the midpoint loses information about the
midpoint, even if both imaginary marks are kept.

There is also an exact per-pair center integral for the full
blurred profile. Write
\[
 \sigma^2=\frac{h^2\epsilon^2}{h^2+\epsilon^2},\qquad
 \alpha=\frac{h^2}{h^2+\epsilon^2},\qquad
 a_u(z)=x-\alpha\ell\Re u .
\]
The product of the two horizontal Gaussians inside \(f_{X,u}\)
is a Gaussian in \(X\) of variance \(\sigma^2\) centered at
\(a_u(z)\). The full prefactor, independent of \(X\), is
\[
 a_0\kappa_0(y)
  \exp\!\left[-\frac{(y-\ell\Im u)^2}{2\epsilon^2}
              -\frac{\ell^2(\Re u)^2}{2(h^2+\epsilon^2)}\right],
 \qquad a_0=\frac{J}{2\pi\epsilon^2}.
\]
For \(f_{X,u}(z_j)f_{X,v}(z_k)\), use the midpoint and difference
of \(a_u(z_j),a_v(z_k)\) in (4), and replace \(h\) there by
\(\sigma\). Multiply by the two prefactors. This removes the
center quadrature exactly for every labelled pair. It leaves the
canonical zero information needed to perform the sum.

## 3. Pay the Gaussian weight outside a finite window

[Parent Note18 (4)][p18] and its [E13 assessment][p13] give a
single finite absolute \(A\) for all times here such that each
unit interval starting at \(q\) contains at most \(A\log(2+|q|)\)
zero labels. For integer \(R\ge0\) let
\[
 B_R(X)=2A\sum_{n=R}^{\infty}
 \bigl[\log(2+X)+\log(n+2)\bigr]e^{-n^2/(2h^2)}.
 \tag{5}
\]
The shells \(n\le |x_j-X|<n+1\) are covered by two unit
intervals starting at \(X+n\) and \(X-n-1\). Their logarithms
are at most \(\log(X+n+3)\le \log(2+X)+\log(n+2)\). Thus the
total window weight is at most \(B_0(X)\), and the weight discarded
by omitting \(|x_j-X|\ge R\) is at most \(B_R(X)\).
Both statements are uniform in Newman time. The same series with
\(X=2T\) bounds the whole center interval. A fixed retained slab
\([T-R,2T+R]\) pays that same omitted mass and allows the exact
center integral in §2 over every retained pair.

Set \(a_0=J/(2\pi\epsilon^2)\). The corresponding first-intensity
error is at most \(a_0 B_R(X)\) everywhere in the observation plane.
A discarded pair has at least one discarded label, so its total
contribution to \(R_{2,X}\) is at most \(2a_0^2 B_0(X)B_R(X)\).
For the averaged connected profile, the pair cost plus the change
in the product of the averaged first intensities costs at most
\(4a_0^2 B_0(2T)B_R(2T)\). These are truncation errors for
statistics on the complete divisor. They neither require a new
zero dynamics nor approximate the missing joint log field.

## 4. What a Gaussian buys in the theta representation

Let \(\gamma_h\) be the normalized real Gaussian with variance \(h^2\).
Convolving \(H_\lambda\) horizontally gives the exact identity
\[
 \int_{\mathbb R}\gamma_h(X-x)H_\lambda(x+iy)\,dx
       =H_{\lambda-h^2/2}(X+iy).
 \tag{6}
\]
Indeed the Gaussian multiplies the cosine mode of frequency \(t\)
by \(e^{-h^2t^2/2}\). Interchange is absolutely justified by the
complete theta decay at fixed \(y\). Equation (6) is a linear
transform identity. The heat family on the right is defined by its
integral even when \(\lambda-h^2/2<0\). The zero statistics under
consideration stay at the original \(\lambda\).

A local polynomial makes the noncommutation explicit. For
\(P_\lambda(z)=z^2-2\lambda\) at \(\lambda=h^2/2\), the horizontal
Gaussian convolution gives \(z^2\), with a double zero at the
origin. The original polynomial has distinct roots at \(\pm h\).
At the origin the Gaussian average of \(\log|x^2-h^2|\) is
finite, while the log modulus of the convolved polynomial is
\(-\infty\). This is an exact polynomial heat example of the
distinction between the linear source and the log calculation.

The zero measure is \((2\pi)^{-1}\Delta\log|H_\lambda|\).
To use this identity with (1)–(2), justify removing the horizontal
cutoff in the distributional calculation. The parent safe-line
bound provides a coarse, sufficient log tail. Choose
\[
 M=\max\!\left(1,\int_0^\infty
      e^{t^2/2+11t}\Phi(t)\,dt\right).
\]
Then \(|H_\lambda|\le M\) on every disk \(D(q+4i,7)\).
The cosine source gives \(H_\lambda(4i)\ge H_0(4i)>0\).
Integrating the real part of \(H_\lambda'/H_\lambda\) on the
zero-free line \(y=4\) gives
\[
 \log|H_\lambda(q+4i)|
 \ge \log H_0(4i)-A|q|\log(2+|q|).
\]
The circular mean of \(\log|H_\lambda|\) about the safe point
is at least its value there by subharmonicity. Integrating in
the radius, and using \(|\log|H||\le 2\log M-\log|H|\), yields
\[
 \int_{[q,q+1]\times[-2,2]} |\log|H_\lambda(z)||\,dA(z)
 \le 49\pi\bigl[2\log M-\log H_0(4i)+A|q|\log(2+|q|)\bigr].
 \tag{7}
\]
The rectangle fits in the disk since its furthest corner is
\(\sqrt{37}\) from the center. All the inputs in (7) are uniform
on the declared time interval.

The Laplacians of \(f_{X,u}\) and \(f_{X,u}f_{X,v}\) have Gaussian
decay in \(x-X\) times at most a quadratic polynomial, with
uniform coefficients for fixed \(T,h,\epsilon\) and observations
in \(Q\). Their support in \(y\) stays in \([-2,2]\). Multiply
each test by a smooth horizontal cutoff that is 1 up to
\(|x-X|\le R\), 0 beyond \(R+1\), and has two uniformly bounded
derivatives. The Laplacian error is supported in \(|x-X|\ge R\)
and has the same Gaussian times polynomial bound. Using (7)
on both horizontal shell intervals makes that error summable
against \(|\log|H_\lambda||\), with a vanishing uniform tail.
Equation (5) gives convergence on the zero side. Thus (2) has
the absolutely convergent source formulas
\[
 r_X(u)=\frac1{2\pi}\int_{\mathbb C}\log|H_\lambda(z)|
                                  \Delta f_{X,u}(z)\,dA(z),\qquad
 d_X(u,v)=\frac1{2\pi}\int_{\mathbb C}\log|H_\lambda(z)|
                    \Delta(f_{X,u}f_{X,v})(z)\,dA(z).
 \tag{8}
\]
Uniform absolute bounds on these weighted integrals give Fubini
for their products and the center average. In coordinates relative
to \(X\), the kernels are fixed, while the log fields are
\(L_X(\xi)=\log|H_\lambda(X+\xi)|\). The averaged pair uses
\(\mathbb E_X[L_X(\xi)L_X(\omega)]\) against the two first kernels
and the separate \(W^2\) self term. The connected pair uses the
same-center covariance in place of the product expectation,
exactly as in [Note14 (6)][b08]. This statement concerns the
absolutely integrated expressions, with fields interpreted almost
everywhere where required.

Equations (5) and (7) control different tails. One counts remote
zeros with small weights. The other controls the noncompact
log-source contraction, including the negative log near zeros.
A whole-line comparison with an approximating source would also
need a paid log tail for that source. Neither estimate gives a
sharp joint-log estimate for the canonical source. The linear identity (6)
has no corresponding rule that takes the logarithm through the
Gaussian. B10 must identify any additional cancellation or
arithmetic input explicitly.

## 5. What the next pass must distinguish

[Plan02's B10 entry][plan] starts at time zero and compares two
routes. The full pair route asks whether the explicit Gaussian
kernels help bound the joint log contraction with both marked
locations intact. The projected route uses (3)–(4) for a bounded
test of separation with both imaginary marks retained, and must
justify the projection's own analytic and approximation costs.
The latter supplies evidence only for its stated projection.

Use the [B09 screen][b09] and [controls12][controls] at premise
level. The Gaussian identities apply generically to their stated
kernels and analytic heat sources. The canonical strip, complete
theta coefficients and safe-line/count package enter separately.
The relevant distinctions for B10 are:

| Control class | Premise to track |
| --- | --- |
| Euler-factor | The complete unmodified coefficients and completion fail. Gaussian algebra survives. |
| Weighted-square / finite-tail, finite-prime orbit | Complete normalized reflection and unit coefficients fail in the cited classes. Matching a finite set of identities supplies no canonical joint estimate. |
| Reflected super-Gaussian, smooth shape / positive primitive | The full arithmetic theta square expansion fails. Smooth positive shape is compatible with the local identities and with collisions. |
| Atomic and finite-profile thresholds | Complete theta profile and growth fail. Eventual simplicity is a further distinction of the cited witnesses and is unnecessary for (3)–(8). |
| RH-conditional theta-close endpoint | Ordinary Dirichlet-series arithmetic fails. Its doubles are compatible with these regularized statistics. |
| Variable observation kernel | The physical cosine/Newman equation fails. Changing the Gaussian height window leaves that physical equation intact. |
| Fractional-profile relaxation | The fractional witness lacks an integer labelled divisor. It cannot justify the factorial self subtraction for the actual zeros. |

This is an analytical screen using the recorded witnesses. It does
not claim that a control fails a Gaussian identity or must violate
a proposed regularity bound. Any new source-specific bound must
identify the premise that earns its claimed gain. Existing
compact-window E09 and E10/E12 results keep their scope. The
[continuation][cont] fixes the next decision and its model guidance.

[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[geometry]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[vdw]: ../research-overview/01_TND_OC_RESEARCH_OVERVIEW_20261107.md#2-what-vandermonde-marginalization-does
[e10]: 17_TND_OC_E10_R1_FULL_MARKED_PAIR_EVOLUTION_PROOF_20261108.md
[b06]: 11_TND_OC_B06_CENTER_LAW_AND_JOINT_SOURCE_DECISION_20261108.md
[b08]: 14_TND_OC_B08_ARITHMETIC_MARGINAL_COLLISION_FRICTION_20261108.md
[b09]: 16_TND_OC_B09_FULL_PAIR_EVOLUTION_DESIGN_20261108.md
[p18]: ../../notes/18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md
[p13]: ../../reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md
[plan]: ../research-plan/02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PLAN_20261108.md#b10--can-a-gaussian-height-window-pay-for-a-theta-pair-estimate
[cont]: ../continuation-notes/21_TND_OC_GAUSSIAN_HEIGHT_WINDOW_AND_MODEL_CHANGE_20261109.md
