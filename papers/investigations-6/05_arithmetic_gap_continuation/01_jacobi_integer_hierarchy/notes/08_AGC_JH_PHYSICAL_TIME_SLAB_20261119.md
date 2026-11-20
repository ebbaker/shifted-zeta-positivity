# The degree-24 gap correction on a physical-time interval

19 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI Codex LLM assistance. Public history does not report the lead model/effort. The bounded implementation contributors were dispatched gpt-6.2-sol/ultra. [B04 decision](../brainstorm/notes/06_AGC_JH_B04_SLAB_DECISION_20261119.md), [frozen E08 r1](../research-progress/handoffs/AGC_JH_E08_REQUEST_R1_20261119.md).

## Certified result

**The moving 24-site head overestimates the squared half-gap throughout the closed physical-time interval.** Put \(\Delta(t)=D_F(t)-D_{24}(t)\). For every \(0\le t\le10^{-4}\) on \(|z-36|=9\), the first frozen calculation gives the following outward bounds. The two methods share the source, moving head, coefficient errors, collar data and root brackets. [Numerical certificate](../numerics/06_AGC_JH_E08_SLAB_CERTIFICATE_20261119.json), [matched internal assessment](../reviews/04_AGC_JH_SLAB_ASSESSMENT_20261119.md).

| Method | Enclosure of \(\Delta(t)\) | Upper bound on width |
| --- | --- | --- |
| Signed contour with complete nonlinear remainder | \((-4.958280826,-4.956734690)\times10^{-8}\) | \(1.546135\times10^{-11}\) |
| Direct root displacement with the same inputs | \((-4.957996104,-4.957019318)\times10^{-8}\) | \(9.767860\times10^{-12}\) |
| Unsigned logarithmic estimate | \((-2.624495,2.624495)\times10^{-5}\) | \(5.248989\times10^{-5}\) |

Widths use the stored rational endpoints before decimal rounding. The direct interval lies strictly inside the signed one. The signed calculation also gives \(D_F(t)>47.4345809848\). The unsigned estimate alone proves positive absolute gap on this previously counted region, while admitting both signs for the correction.

Specializing the same polynomial to \(t=10^{-4}\) and subtracting the independent saved E07 time-zero enclosure gives
\[
  4.05561835\times10^{-12}<\Delta(10^{-4})-\Delta(0)<4.05588776\times10^{-12}.
\]
Thus the approximation error decreases in magnitude from the first endpoint to the last. The full-slab upper/lower enclosures for \(\Delta(t)-\Delta(0)\) are \((-2.85619471,6.91166471)\times10^{-12}\). These are enclosures of values taken over time. Monotonicity between endpoints remains open.

## The observable and source of time correlation

Put \(T=10^{-4}\), \(s=t/T\in[0,1]\), \(w=z-36\), \(F_t=H_t/H_t(0)\), and \(Y_t=[\exp(izJ_{24}(t))]_{00}\). The roots inside \(|w|=9\) define the squared half-gaps \(D_F,D_{24}\). Each approximating polynomial has outward coefficients in \(s^kw^m\). Subtract the coefficients of the two fields while \(s\) and \(w\) are still indeterminates. Then evaluate the difference over the slab, adding the complete tails of both series. This ordering retains the cancellation between the physical motion and the motion of the true Jacobi head. Separately bounding those motions would spend uncertainty on a displacement shared by both roots.

The signed observable and error estimate come from [Note04](04_AGC_JH_SIGNED_GAP_REMAINDER_20261119.md). [Note07](07_AGC_JH_CANONICAL_SIGNED_CONTOUR_20261119.md) fixes the orientation and supplies an independent time-zero consistency check. We price the sign over the interval directly. No evolution of a truncated hierarchy, assumed monotonicity of the correction, or time-integrated forcing estimate enters the test.

## The complete source on the wide collar

Let \(d\mu_0\) be the even normalized full theta measure, \(g(t)=\int e^{tu^2}d\mu_0\), and \(U_t(z)=\int e^{tu^2}\cos(zu)d\mu_0\). On the positive half-line the probability measure has density \(\Phi(u)/H_0(0)\) after reflection. The inherited all-mode estimate is \(\Phi(u)\le C_\Phi\exp(9u-\pi e^{4u})\), with \(C_\Phi=2\pi^2/(1-16e^{-3\pi})\). It dominates polynomial factors and supplies analyticity in both variables. At zero, \(F_0(z)=\xi((1+iz)/2)/\xi(1/2)\). [HDC source and envelope](../../../../investigations-4/12_height_dependent_heat_contours/notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md), [derivation of the complete xi identity](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md).

For complex \(|t|\le\rho=1/20\) and \(|w|\le24\), the absolute numerator is bounded by the tilted positive-source cosh integral with argument 24. On \(0\le u\le1\), this costs at most \(e^\rho F_0(24i)\). On \(u\ge1\), integrate the all-mode envelope times \(e^{\rho u^2+24u}\). The same split with the bulk factor \(e^\rho-1\) at zero height bounds \(|g(t)-1|\) strictly below one. These two bounds control the normalized \(F_t=U_t/g(t)\) on the polydisk. Write \(c_j=[w^j]F_0(36+w)\). The raw time-space coefficient is
\[
 [s^kw^m]U_{Ts}(36+w)=\frac{(-T)^k(m+2k)!}{k!m!}c_{m+2k}.
\]
The mass coefficients are \(T^k\mu_{2k}(0)/k!\). Formal series division gives the normalized coefficients through the retained time order. For clarity, the source tail integral with additional exponential factor \(e^{Bu}\), \(B=0\) or 24, is bounded by
\[
 \frac{C_\Phi}{H_0(0)}\frac{e^{9+B-l}}{4l-9-B},\qquad l=\pi e^4-\rho .
\]
Here \(u^2\le e^{4(u-1)}\) and \(e^{4(u-1)}\ge1+4(u-1)\) for \(u\ge1\). The mass variation uses \(|e^{tu^2}-1|\le e^{\rho u^2}-1\). Bounding the omitted time and space coefficients by Cauchy's formula uses the ratios \(T/\rho=1/500\) and \(10/24\). The output covers the entire radius-ten disk. A radius-one Cauchy circle also pays for its first spatial derivative on radius nine. [Source evaluator](../numerics/e08_source.py).

## Why this is the moving canonical head

The time-zero xi moments and positive parity Gram pivots give the anchor monic norms \(h_j\), squared edges \(\beta_j=h_j/h_{j-1}\), and \(a_j=\sqrt{\beta_j}\). Differentiating along the actual heat tilt gives \(\dot\beta_j=\beta_j(\beta_{j+1}-\beta_{j-1})\), with \(\beta_0=0\). The last edge of the 24-site head is \(a_{23}\). Its first derivative uses \(\beta_{24}\) and its order-\(K\) time coefficient uses through \(\beta_{23+K}\). The required anchor moments end at order \(2(23+K)\). Higher links supply the true time derivatives of this fixed-size head. [VCD derivation](../../../03_volterra_coefficient_dynamics/manuscript/main.tex), [Van Assche, §2.3, Theorem 2.4 and symmetric quadratic specialization](https://arxiv.org/html/2202.11017v1#S2.SS3).

The remainder needs control away from the anchor. Use the time-zero orthonormal polynomials \(p_0,\ldots,p_{23}\) and the matrix \(G_{ij}(t)=\int p_i p_j e^{tu^2}\,d\mu_0\). Then \(G(0)=I\). On \(|u|\le1\), the operator norm of the variation is at most \(e^\rho-1\) by orthonormality and Cauchy–Schwarz for the two test vectors. On the complement one may bound it by the integral of \(\sum |p_j|^2\) times the absolute weight error. If \(L\) is an upper bound for the maximum absolute row sum of \(J_{24}(0)\), the characteristic-polynomial representation and interlacing of **source nodes** give
\[
 \sum_{j=0}^{23}|p_j(u)|^2\le
 \frac{24(1+L)^{46}}{\min_{0\le j\le23} h_j}|u|^{46},\qquad |u|\ge1 .
\]
Indeed the smaller principal heads have norm at most \(L\), and their monic characteristic polynomials have these nodes as roots. This argument makes no interlacing assumption on Fourier zeros. The theta tail pays for this large prefactor. For \(u\ge1\) absorb \(u^{46}\le e^{46(u-1)}\). The log of the resulting majorant has negative second derivative. Its tangent at 1 has negative slope \(2\rho+55-4\pi e^4\), so the half-line integral is bounded by its value at 1 divided by the magnitude of that slope. It yields \(\|G(t)-I\|\le\epsilon\) for every leading block on the complex time disk.

The degree-\(j\) Schur pivot \(S_j\) of this rebased matrix obeys \(|S_j-1|\le\epsilon+\epsilon^2/(1-\epsilon)=\sigma\). On real time, the unnormalized tilted monic norm is \(h_j S_j\). The identity extends analytically and its scalar normalization cancels in the edge ratio. Since \(\sigma<1\), the principal logarithms provide the unique analytic branches agreeing with the positive anchor,
\[
 a_j(t)=a_j(0)\exp[(\log S_j-\log S_{j-1})/2].
\]
Consequently \(\|J_{24}(t)-J_{24}(0)\|\le d=L\sigma/(1-\sigma)\). For the complex symmetric perturbation, the bounds on the maximum absolute column and row sums agree. Duhamel's formula and Grönwall's inequality, using the self-adjoint *anchor*, give
\[
 \|e^{izJ_{24}(t)}\|\le \exp(|\Im z|L+|z|d).
\]
The bound on \(|w|\le10\) therefore applies to complex time and can be used for a Cauchy time remainder. It does not assume that the complex-time matrix is self-adjoint.

Truncate the origin spatial exponential after \(P\) terms. On the same polydisk the uniform omitted norm is at most \(e^v v^P/P!\), \(v=46(L+d)\). The finite tridiagonal path recurrence constructs the exact retained time coefficients of this polynomial and spatial translation moves it to center 36. For example, taking the time tail of the true readout and the retained time coefficients of its spatial remainder costs at most
\[
 e^{10L+46d}\frac{(T/\rho)^{K+1}}{1-T/\rho}
 +\frac{e^v v^P}{P!(1-T/\rho)} .
\]
Interval arithmetic also encloses moment acquisition, formal algebra and spatial translation. [Head evaluator](../numerics/e08_head.py).

## Counts and two evaluations of the change

For each real time we require both circle counts, a common unit buffer and nonzero modulus on the entire annulus \(9-1/64\le|w|\le9+1/64\). The computation uses the inherited HDC count at time zero. The time-zero strip puts every possible source zero in either disk inside the HDC rectangle. Two sign changes exhaust its count at the anchor. The verified nonvanishing of the source on both walls throughout the slab then propagates each count by homotopy. The uniform real sign brackets \((28,29)\), \((42,43)\) put the source roots strictly inside radius 8. A strict Rouché bound for the two collar boundaries transfers their counts to \(Y\). Its two uniform sign brackets put both head roots inside radius 8. This gives simplicity by multiplicity and excludes any zero from the annulus. Maximum modulus applied to the reciprocals and \(B/Y\) extends the verified boundary estimates across the collar. [HDC count](../../../../investigations-4/12_height_dependent_heat_contours/numerics/07_COMPLETE_THETA_WALL_CERTIFICATE_20261023.json), [strip scaling](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/references/03_VCD_GT_STRIP_PRODUCT_SOURCE_USE_20261116.md).

Write \(x_i(t)\) for source roots and \(y_i(t)\) for head roots in those two disjoint brackets. Let \(h=(y_2-y_1)/2\), \(B=F-Y\), \(\eta\ge\sup|B/Y|\) and \(K_0=-\log(1-\eta)\). The simple-root residues and the previously proved contour remainder give
\[
 J=-h\left[\frac{B(y_2)}{Y_z(y_2)}-\frac{B(y_1)}{Y_z(y_1)}\right],
 \qquad
 |D_F-D_{24}-J|\le A=153(K_0-\eta)+\tfrac{81}{4}K_0^2 .
\]
The final term pays for the motion of the pair center. Every occurrence here has the same physical time. The direct comparator uses the same numerator and root tubes. For some \(\xi_i\) between \(y_i\) and \(x_i\), the mean-value theorem gives \(d_i=x_i-y_i=-B(y_i)/F_z(\xi_i)\). If the roots coincide and the derivative is cleared, the equality still gives zero displacement. With \(d=d_2-d_1\), the exact direct change is \(d(h+d/4)\). Slope intervals over both connecting segments and all time values must exclude zero. Subtracting two independent moving root enclosures is unnecessary. The prepared contour and integer S/T formulation retain their original domain through collision. Simple-pole and real-derivative shortcuts use the narrower domain certified here.

## Error and cost ledger

One degree-ten time expansion, 768-bit outward ball arithmetic, 144 source spatial terms and 192 head exponential terms sufficed. Each collar boundary is covered by 512 sectors. Real coefficients allow conjugation of 256 evaluated sectors. Fourth-order spatial remainders extend midpoint evaluations to every point of each arc. The interval \(s=[0,1]\) enters every such evaluation. [Collar and root evaluation](../numerics/e08_chart.py), [replay driver](../numerics/certify_e08.py).

| Input or allowance | Verified bound on the stated domain |
| --- | --- |
| Source, complex-time mass and normalized source majorant | \(\inf\lvert g\rvert>0.94872890\), \(\sup\lvert F\rvert<23.143152\) on the source polydisk |
| Complete source model | Joint tail \(<4.749216\times10^{-29}\) on radius 10, aggregate coefficient radii \(<2.070722\times10^{-196}\) |
| Moving head acquisition | Positive anchor pivots through degree 33, last moment order 66, \(\beta_{24}(0)\simeq0.11395870\) |
| Complex-time head | Gram variation \(<0.051271097\), Jacobi norm \(<0.700862635\), field majorant \(<4324.969\) |
| Complete head model | Joint tail \(<8.875286\times10^{-27}\) on radius 10, aggregate coefficient radii \(<1.165086\times10^{-145}\) |
| Count and clearance | Two simple real zeros of each field inside radius 8. On the collar, \(\lvert F\rvert>1.4331937907\times10^{-5}\), \(\lvert Y\rvert>1.4331935452\times10^{-5}\) |
| Complete numerator | \(\sup\lvert B\rvert<2.458437\times10^{-12}\), \(\eta<1.715356\times10^{-7}\) on the collar |
| Signed first variation | \((-4.957996144,-4.957019371)\times10^{-8}\) |
| Nonlinear logarithm and center square | \(<2.250971\times10^{-12}\) and \(<5.958452\times10^{-13}\), combined \(A<2.846816\times10^{-12}\) |
| Source slopes between matched roots | Left between \(-0.001391\) and \(-0.001390\), right between \(1.78519\times10^{-5}\) and \(1.78537\times10^{-5}\) |

Coefficients and root tubes are outward intervals. The displayed coefficient radii are already included in their polynomial evaluations. Shared real brackets and the difference numerator link both computations to the same two roots. The right physical root lies below its head root by about \(7.20\times10^{-9}\), whereas the left root lies above its head root by about \(2.00\times10^{-18}\). These opposite displacements give a direct explanation for the smaller physical gap.

The saved run took 10.19 s on one FLINT thread, of which 9.53 s was shared collar acquisition, 0.071 s source construction and 0.223 s moving-head construction. The full-slab common brackets and subtracted-numerator evaluations took another 0.138 s and 0.006 s. Given those data the signed evaluation took 0.00022 s and the direct evaluation 0.00457 s. These are timings of one shared implementation. The direct evaluation resolves the sign with a narrower interval from the same inputs. [Recorded costs and rational intervals](../numerics/06_AGC_JH_E08_SLAB_CERTIFICATE_20261119.json).

## Collision and scope checks

This is a measured finite error under [classification01](../../../../../avoid/01_restating_the_target.md). See the [result index](../../../../../result-summaries/README.md), [collision controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns index](../../../../../avoid/README.md), [premise screening02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and the [branch family screen](../reviews/02_AGC_JH_INTERFACE_AND_PARITY_ASSESSMENT_20261119.md). A negative gap *difference* is compatible with a target collision. Set \(Y=(z-36)^2-2t-1\), \(F=(z-36)^2-2t\). Both satisfy the physical unnormalized heat equation. At every time the two gap statistics give \(\Delta D=-1\), and the full contour gives \(J=-1\). At \(t=0\) a strict lower bound for the absolute target gap fails, as do the two separate simple target roots and cleared target slopes. Indeed the gaps are \(2t+1\) and \(2t\), and the coefficient of \(1/(z-36)\) in \((z-36)(F-Y)/Y\) is one. This heat control lacks the canonical source. For \(Y=F\), the strict negative correction gate fails identically. A reference double also removes both independently isolated simple reference roots and derivative divisions.

Euler-factor and Dirichlet controls lose the canonical ordinary xi completion. Weighted-square, finite-square, finite-score and finite-prime controls change coefficients or full reflection. The later-defect controls can preserve reflection but change the canonical arithmetic. Reflected super-Gaussian, log-concave shape, positive-primitive and finite-profile or atomic threshold controls lack the exact normalized theta law. The RH-conditional double keeps its hypothesis. Altered observations lose the literal cosine transform. Positive-measure profile relaxations and static reduced divisors lack the physical integer divisor or common heat path. The compact parity control lacks the complete canonical source. These are point-of-application premise tests, with no new numeric collision claims for the controls.

## Continuation

[B05 r1](../research-progress/handoffs/AGC_JH_B05_REQUEST_R1_20261119.md) asks whether the 24-to-26 degree increment and a separately bounded complete tail suffice to predict this sign using less source information. E08 supplies a reference value on this one slab. Higher-degree contraction and behavior on other circles are open.
