# Measuring the Jacobi gap correction on the time-zero circle

19 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI Codex LLM assistance. The local public transcript records no lead model or effort. The three bounded E07 contributors were explicitly dispatched gpt-6.2-sol/ultra. Serving-backend metadata are unavailable.


**Interval-certified on one known-coverage chart.** On \(|z-36|=9\) at physical \(t=0\), the canonical 24-site head overestimates the squared half-gap. The signed-contour enclosure alone gives
\[
 -4.95800\,10^{-8}<D_F-D_{24}<-4.95742\,10^{-8}.
\]
The equally informed direct evaluation gives \(D_F-D_{24}\simeq-4.957710484497283\,10^{-8}\), with enclosure width below \(2.073\,10^{-35}\). Here and below approximate midpoint digits are rounded separately from the reported widths. The unsigned log bound proves positivity of the pair gap but leaves the sign of its change open. [Outward numerical record](../numerics/05_AGC_JH_E07_CERTIFICATE_20261119.json), [replay](../numerics/certify_e07.py), [matched internal assessment](../reviews/03_AGC_JH_CANONICAL_ACQUISITION_ASSESSMENT_20261119.md).

## What is measured

For the two counted roots, let \(D=((x_2-x_1)/2)^2\). The first variation \(J\) measures the change from the moving canonical \(N\)-site Jacobi head on this slice to the complete field. The requested observable is the sign and size of that correction with a complete error budget. Reality and the count of the physical pair already have a certificate. [B03 decision](../brainstorm/notes/05_AGC_JH_B03_CANONICAL_ACQUISITION_20261119.md), [frozen E07 request](../research-progress/handoffs/AGC_JH_E07_REQUEST_R1_20261119.md).

## Acquisition and independent count

At physical \(t=0\), \(F(z)=H_0(z)/H_0(0)=\xi((1+iz)/2)/\xi(1/2)\) is the exact normalized cosine transform of the unchanged full theta amplitude. Since \(F^{(2k)}(0)=(-1)^k\mu_{2k}\), a validated analytic jet at zero gives the moments of the normalized measure. The Gram matrix of the monomials splits by parity. Its positive LDL pivots are their squared monic orthogonal-polynomial norms \(h_j\). The edge between sites \(j-1\) and \(j\) is \(a_j=\sqrt{h_j/h_{j-1}}\). For an \(N\)-site head the full numerator used below consumes edges through \(a_{N-1}\), moments through order \(2N-2\). These are freshly enclosed time-zero quantities. [Complete-source identity](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md), [source and head evaluator](../numerics/e07_fields.py).

Two independent expansions about 36 enclose \(F\) and \(Y=[\exp(izJ_N)]_{00}\). The 144 source coefficients come from the normalized xi series. Positivity of the source gives \(\sup_{|w|\le24}|F(36+w)|\le F(24i)\). With \(q_*=10/24\), dropping all terms from degree 144 costs at most \(F(24i)q_*^{144}/(1-q_*)\) on \(|w|\le10\). For the finite field, apply \(\exp(36iJ_N)\) to the first basis vector and then repeatedly multiply by \(iJ_N\), dividing at each step by the Taylor index. A row-sum upper bound \(L\) for the real symmetric Jacobi matrix gives a uniform omitted tail at most \(e^{10L}(10L)^{144}/144!\). Interval edges enter the exponential and each matrix-vector multiplication. Each field's uniform remainder also bounds its first derivative error on radius 9 by the unit-radius Cauchy estimate. The exact xi identity includes every theta mode and the entire spatial tail. The complex-disk estimates do not invoke the inherited phase bound.

The HDC argument-principle certificate at zero counts exactly two zeros in \((26,46)+i(-2,2)\) with multiplicities. We replayed its original script: the stored wall, anchor power sums, count, checks and source hashes matched. The time-zero completed-zeta strip puts every zero of \(F\) in \(|\Im z|\le1\). Thus every possible \(F\) zero in the disk of radius \(9+1/64\) around 36 is in the HDC rectangle. Real sign changes on \((28,29)\) and \((42,43)\) place two distinct roots in the *open* radius-eight disk. This proves count two on both the inner and outer disks. The two collar boundary circles are covered by arcs. On each arc a centered third-order Taylor enclosure and a fourth-derivative majorant bound the two moduli and the subtracted numerator. The strict Rouché inequalities transfer both circle counts to \(Y\). Equal counts leave the intervening annulus free of zeros for each field. Maximum modulus applied to \(1/F,1/Y,q\) extends the floors and the ratio bound to its full interior. Two separate sign changes for \(Y\) on the same real brackets put its two roots inside the inner disk as well. Each root has multiplicity one by the count. The distance from either pair to the integration circle is at least \(b=1\). [HDC Note13](../../../../investigations-4/12_height_dependent_heat_contours/notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md), [strip and scaling](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/references/03_VCD_GT_STRIP_PRODUCT_SOURCE_USE_20261116.md).

## From the paid functional to the gap

Take \(q_0=q=(F-Y)/Y\), and \(c_Y=(x_1+x_2)/2\) for the counted \(Y\) roots. This choice sets the analytic modeling discrepancy \(e\) to zero. Subtracting the two centered coefficient sequences before evaluating encloses the full difference even where cancellation is large. Both analytic remainders and all arithmetic intervals are retained when enclosing the numerator, the floor, the quotient and the residues. The residue theorem gives

\[
 J=-\frac{1}{2\pi i}\oint_{|z-36|=9}(z-c_Y)\frac{F-Y}{Y}\,dz
   =-\sum_{i=1}^2(x_i-c_Y)\frac{(F-Y)(x_i)}{Y'(x_i)} .
\]

At a root the numerator equals \(F(x_i)\). The subtraction is useful for interval evaluation on a root bracket. This evaluation explicitly requires verified simple reference roots and nonzero derivative floors. Writing \(Y=(z-x_1)(z-x_2)U\) shows that \((x_i-c_Y)/Y'(x_i)=1/(2U(x_i))\). At a reference double the original contour residue gives \(J=-F(c_Y)/U(c_Y)\). The exact observable stays regular when the two roots merge. The separate derivative divisions actually used in this acquisition require simple roots. [Note04](04_AGC_JH_SIGNED_GAP_REMAINDER_20261119.md).

Write \(\eta\) for the acquired uniform bound on \(|q|\), and \(K=-\log(1-\eta)\). With radius 9 and buffer 1, Note04 gives

\[
 |D_F-D_Y-J|\le A=153(K-\eta)+\tfrac{81}{4}K^2 .
\]

The term \(81K^2/4\) pays for moving the pair center. The complete unsigned log allowance is \(153K+81K^2/4\). The equally informed direct evaluator has both fields, the common count, brackets, precision and oracle bounds. It encloses the real roots of \(F\) directly and computes their squared half-gap; the argument principle identifies this with the same two-root contour observable. It also has access to the signed estimate. Physical time, height, degree and moment order stay distinct: the singleton time weight is \(W(0,0)=1\), and the integrated time force is zero. No hierarchy truncation, split-power closure or limiting-root premise enters.


## Paid bounds and matched result

All decimals used as external endpoints or one-sided allowances below are rounded outward. The [execution record](../numerics/05_AGC_JH_E07_CERTIFICATE_20261119.json) stores rational endpoints, including source moments, all pivots, links, root and derivative brackets. N=24 passed the first declared level at 768 bits; N=28 and the second refinement were unused.

| Quantity | Certified bound or recorded value |
| --- | --- |
| Source setup | Moments 0,2,…,46; all 24 monic pivots positive; 23 positive edges. Two 144-term centered polynomials. \(F(24i)<20.886\), \(\lVert J_{24}\rVert<0.663\). |
| Source/head Taylor truncation on radius 10 | \(e_F<6.361\,10^{-54}\), \(e_Y<2.703\,10^{-129}\). Each also bounds its derivative truncation on radius 9. |
| Rounded Taylor coefficients, including source normalization and uncertain links | Radius-weighted coefficient radii below \(1.679\,10^{-196}\) for \(F\), \(8.448\,10^{-149}\) for \(Y\). Propagated inside the interval calculations. |
| Whole annulus \(9-1/64\le \lvert z-36\rvert\le9+1/64\) | \(\inf \lvert F\rvert>1.43319492857\,10^{-5}\), \(\inf \lvert Y\rvert>1.43319468318\,10^{-5}\); \(\sup \lvert F-Y\rvert<2.459\,10^{-12}\), \(\eta<1.715321\,10^{-7}\). Two boundary circles, 512 sectors each including conjugate reflections. |
| Count and clearance | Each field has two simple real roots in radius 8 and count two inside radius 9. The new annulus floors are in normalized field units. The old HDC wall floor is in physical units and applies to its rectangle. |
| Reference slopes and residue inputs | Left \(Y'\approx-1.390728\,10^{-3}\), right \(Y'\approx1.785258\,10^{-5}\). The two signed ratios \((F-Y)/Y'\) are approximately \(-1.99972\,10^{-18}\) and \(+7.19832\,10^{-9}\), respectively. The second root accounts for almost all of \(J\). |
| Signed first variation | \(J\approx-4.957710535627505\,10^{-8}\), enclosure width \(<2.865\,10^{-43}\). |
| Nonlinear payment | Log remainder \(<2.251\,10^{-12}\); center square \(<5.959\,10^{-13}\); their jointly evaluated sum \(A<2.846700\,10^{-12}\). |
| Complete lower and upper gap margins | \(47.4351009810912<D_F<47.4351009810970\) from \(D_Y+J\pm A\), with \(D_Y\approx47.43510103067121724\). Direct \(D_F\approx47.43510098109411239\). |

For the same quantity \(D_F-D_Y\), the unsigned log interval has width about \(5.24888\,10^{-5}\) and contains zero. Retaining \(J\) gives width below \(5.694\,10^{-12}\), more than 9.21 million times narrower, and certifies a negative correction. Directly bisecting each complete-source root at the same precision gives width below \(2.073\,10^{-35}\) for that same change. Its computation uses \((s_F-s_Y)(s_F+s_Y)\), where \(s\) is the half-gap. The direct interval is contained in the signed interval. Subtracting the certified \(J\) ball from the directly bracketed change locates the actual nonlinear correction near \(+5.11302\,10^{-16}\). Both methods clear the positive-gap threshold, including the unsigned bound. The narrower signed allowance matters when asking which way the finite head errs.

The recorded one-thread run took 0.725 seconds for the complete E07 attempt, including approximately 0.085 seconds for both fields and 0.623 seconds for collar certification. After shared setup, both reference and physical root pairs used 244 polynomial evaluations per pair; the two signed residues used four additional polynomial evaluations. The separate replay of the inherited HDC certificate took 10.73 seconds on this machine and is accounted for separately. These are observed costs of this implementation. The direct comparator can reuse every input and its root enclosures are tighter on this chart. No speed advantage is established.

## Collision controls and scope

This is a finite measured comparison under [classification01](../../../../../avoid/01_restating_the_target.md). [Result index](../../../../../result-summaries/README.md), [collision controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns index](../../../../../avoid/README.md), [control premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scoped exclusions07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md). The family-by-family premises are listed in [Review02](../reviews/02_AGC_JH_INTERFACE_AND_PARITY_ASSESSMENT_20261119.md). Explicitly, at any included double of the target, Note04 forces \(D_Y+J-A\le 0\) when its chart hypotheses hold. A double of the reference also removes this simple-pole acquisition premise. Euler-factor and Dirichlet perturbations lose the ordinary completion; weighted-square, finite-score and finite-prime variants lose unchanged coefficients or full reflection; reflected super-Gaussian, smooth-shape, positive-primitive, threshold/profile and compact parity controls lack the exact normalized xi source. The RH-conditional double keeps its conditional status. A changed observation loses the literal cosine transform. Relaxed profile measures and static reduced divisors lack the required physical integer zero divisor or common heat trajectory. These are logical event and premise tests, not new numerical measurements of those controls. The actual computation makes no sign claim beyond the single counted pair, time and degree.


For an exact check in the same geometry set \(u=z-36\), \(Y=u^2-1\), \(Z=u^2\). The target double and the reference roots \(u=\pm1\) are inside radius 8. On the working annulus, \(|q|=|1/(u^2-1)|\le[(9-1/64)^2-1]^{-1}<1\). The two residues of \(u/(u^2-1)\) give \(J=-1\), so \(D_Y+J-A=-A<0\) and direct evaluation gives \(D_Z=0\). This tests the critical sign and the strict-margin gate with a simple reference and a colliding target. It is an algebraic control outside the canonical source.
