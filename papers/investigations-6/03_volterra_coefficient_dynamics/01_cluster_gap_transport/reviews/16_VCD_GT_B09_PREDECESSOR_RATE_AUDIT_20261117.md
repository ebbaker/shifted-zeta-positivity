# VCD-GT-B09 predecessor rate audit

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Audit worker dispatch recorded as
**gpt-6.1-sol / ultra**.

**E support of VCD-GT-B09.** Fixed documentary and algebraic check against the
selected-pair consumer. The completion test is to trace each audited bound,
its normalization and domain, and its available rate at microscopic width
and spacing-squared time. The results below concern the supplied bounds.
The conceptual choice of an additional estimate belongs to B09. No
numerical or external-source acquisition was performed. [Established
results][results] · [Collision controls][controls] · [Patterns to avoid][avoid] ·
[Scope rule][scope] · [Sibling reuse][reuse].

## Consumer and scale

On a paid count-two tube write the pair as the zero divisor of
\(Q(z)=(z-c(t))^2-D(t)\). Its exterior kernel for \(\rho=c+x+iy\) is
\(q(x,y,D)=\Re[((x+iy)^2-D)^{-1}]\), with one copy per exterior label.
Write \(S_R\) for the sum at \(|x|\le R\) and \(T_R=M-S_R\). The
regular deflated formula for \(M\) works for real and conjugate pairs and
extends to \(D=0\). With \(L=\log c_*\) frozen at an anchor height and
\(\ell=L^{-1}\), the microscopic kernel is
\(\ell^2q=\Re[((x/\ell+iy/\ell)^2-D/\ell^2)^{-1}]\).
Order-one terms in this scaling can occur with a paid microscopic collar.
The usable canonical signed estimate is the far theorem, uniform for
\(0\le t\le1/2\), \(c\ge16\pi\), \(|D|\le1\) and \(3\le R\le c/2\):
\[
 T_R=\frac{\log(c/(4\pi))}{2\pi R}
 +O\!\left(\frac{\log(2+c)}{R^2}+\frac{\log(2+c)}{R^3}
                    +\frac{\log(2+c)}{c}\right).
\]
At \(R=\sqrt L\) and comparable heights \(c\asymp c_*\) this gives
\(\ell^2T_R=(2\pi L^{3/2})^{-1}+O(L^{-2})\).
The established backward consumer compares the paid lower anchor at \(v\) with
\(2\int_u^v\exp(-4\int_a^v M(b)\,db)\,da\). On time intervals of order
\(\ell^2\), uncertainties in the lower bound for \(\ell^2 S_R\) act in
the exponent on an order-one rescaled interval. The rate tests below
check whether the supplied inputs bound that kernel or the signed time
integral on the same selected tube. [Note24, (1)–(4)][gt24] ·
[Note33, lines 206–248][gt33] · [Note35, lines 33–74][gt35].

## Zero statistics and time rates

- **TND-O canonical localized modulus.** Set
  \(Q_{X,r}=\sum_j\chi((x_j-X)/r)y_j^2\), with a fixed
  \(\chi\in C_c^2([-1,1])\), \(0\le\chi\le1\).
  For complete canonical zeros with multiplicity,
  \(H_0(z)=\xi(1/2+iz/2)/8\) and \(\partial_\lambda H=-H_{zz}\),
  the bound is
  \[
    |\partial_\lambda Q_{X,r}|\le344A^2
    (\|\chi\|_\infty+\|\chi'\|_\infty+\|\chi''\|_\infty)
    r^{-2}\log^2(2+X).
  \]
  Here \(X\ge10\), \(0<r\le1\), \(0\le\lambda\le1/2\),
  initially on simple relevant-root intervals. \(A\) is the absolute,
  unevaluated strip-count/safe-line constant. The later assembly extends
  the same Lipschitz estimate to the full time interval. At
  \(r\asymp\ell\) and \(\Delta\lambda\asymp\ell^2\) the raw increment
  allowance is \(O(L^2)\). A single mark with \(|y_j|\asymp\ell\)
  and order-one window weight contributes \(O(L^{-2})\).
  The estimate controls unsigned variation of a transverse moment.
  Its proof of instantaneous sharpness uses a coarse-premise polynomial
  class, with no canonical all-time sharpness claim. [TND-O Note18,
  lines 20–40, 114–121, 248–301][o18] · [TND-O Note19, lines 16–33][o19].

- **TND-O broad transverse density.** With \(L_T=\log T\),
  \(a_T(x)=\chi((x-3T/2)/T)\), support \([T/2,5T/2]\) and plateau
  \([T,2T]\), put \(Q_{T,g}=\sum_j a_T(x_j)g(y_j)\) for even convex
  \(g\in C^2([-1,1])\), \(g(0)=0\). For \(T\ge8\) and
  \(0\le\alpha\le\beta\le1/2\),
  \[
    Q_{T,g}(\beta)\le Q_{T,g}(\alpha)
    +D_\chi\|g\|_\infty(\beta-\alpha)L_T^3,qquad
    D_\chi=A^2(36\|\chi''\|_\infty+1200\|\chi'\|_\infty).
  \]
  Its complete-field density consequence is
  \(\#\{T\le x_j\le2T,\ |y_j|>v\}\le B_bTL_T e^{-bvL_T}\),
  \(0<v<1\), fixed \(0<b<1/2\), uniformly for the same time slab.
  At \(v\asymp L_T^{-1}\) this permits population order \(T L_T\).
  The normalized center average is
  \(T^{-1}\int_T^{2T}Q_{X,r}^p\,dX\le
  C_b^{\rm mom}r(A_b^{\rm mom})^p(2p)!/L_T^p\) for every integer \(p\ge1\).
  An isolated conjugate pair at height \(d\), with its center profile
  wholly in the averaging band, has stand-alone signal
  \((r/T)(2d^2)^p\int\chi^p\) from its two labels. The source's exact
  allowance divided by that signal is at least
  \((C_b^{\rm mom}T/\int\chi)\exp[-\sqrt{2L_T/A_b^{\rm mom}}]\) in the
  strip, uniformly in \(p\). This divergence concerns the bound.
  The broad convex gain does not supply an every-center marked mass,
  even with all orders available. [TND-O Note21, lines 52–101, 375–423][o21].

- **TND-OC complete marked-pair time modulus.** Fix \(T\ge10\),
  \(X\) uniform on \([T,2T]\), \(\ell_o=\min(1,4\pi/\log T)\),
  \(J=\ell_o^2\), and \(\epsilon=\ell_o/4\).
  Write \(f_{X,u}(z)=J W_X(z)G_\epsilon(X+\ell_o u-z)\) with the prescribed
  unit physical window and the complete planar Gaussian
  \(G_\epsilon(w)=(2\pi\epsilon^2)^{-1}e^{-|w|^2/(2\epsilon^2)}\).
  The raw pair at one common center is \(R_{2,\lambda,X}(u,v)=
  \sum_{j\ne k}f_{X,u}(z_j)f_{X,v}(z_k)\).
  The diagonal subtraction deletes equal labels and retains distinct
  coincident labels. The connected profile subtracts the product of
  separately center-averaged first profiles from the center-averaged
  raw pair. On \([-1,1]+i[-1,1]\) and its square, uniformly over
  \(0\le\lambda,\mu\le1/2\), the first and self profiles have
  Lipschitz constants \(L_1,L_d=O_A((\log T)^4)\), and the raw and
  connected pair constants are \(L_2,L_C=O_A((\log T)^5)\).
  The first and raw-pair bounds apply pathwise and after averaging.
  The bound crosses multiple events. On spacing-squared time the raw
  pair allowance is \(O_A((\log T)^3)\), while each localized ordered
  pair contributes at most \((J/(2\pi\epsilon^2))^2=O(1)\) pathwise.
  The cutoff error in (5) only truncates the safe-line-subtracted distant
  field along the exact canonical divisor. An independently acquired
  initial pair profile still incurs its own error plus this time
  allowance. No selected exterior third mark or condition on the rest
  of the cloud is supplied. [TND-OC Note17, lines 19–71, 232–318, 379–385][oc17].

- **TND-OC visibility and finite-error blur.** A single upper zero at
  height \(d\) contributes at most \(\pi d/T\) to the uniform center
  average of the Green statistic. The squared Green statistic uses
  both a one-point term and the raw factorial pair term. The fixed
  positive-blur comparison for the exact quadratic heat polynomial
  shows a difference \(O_\epsilon(d^2)\) between the real and imaginary
  pair profiles while their internal inverse-square sum is \(1/(2d^2)\).
  This is a stability obstruction for the stated profile inference and
  internal singular observable. Exact Gaussian convolution remains
  injective on finite measures. The example supplies no obstruction for
  the regular exterior \(M\) once its own conditioning and collar are
  available. The inherited finite factorial triple identity for testing
  selected labels needs a conditional denominator and visibility of a
  selected exception when used statistically. Ordinary factorial
  densities at a double have not been supplied. [TND-OC Note14,
  lines 194–276, 285–319][oc14] · [GT Discussion12, lines 120–162][gt12].

## Complete-source responses and signed insertions

- **Direct Newman conditional covariance.** Laboratory time \(s\) gives
  \(\lambda(s)=1/2-\gamma s\), \(0\le s\le\gamma^{-1}\).
  The complete source probability is
  \(w_s(u)=e^{\lambda(s)u^2}\Phi(u)/Z_{\lambda(s)}\), with
  \(Z_\lambda=2H_\lambda(0)\). For paid fixed observables,
  \(\partial_s E_s a=-\gamma\operatorname{Cov}_s(a,U^2)\).
  The normalized cosine \(C=E_s\cos(kU)\) satisfies
  \(C_s=\gamma(C_{kk}+\mu_2 C)\). At \(C=0\), the two nonnegative
  cosine-sector masses agree, say at \(m\), and
  \(C_{kk}=-m(B_+-B_-)\), with \(B_\pm\) their normalized second moments.
  The Cauchy–Schwarz bound is an absolute first-time speed.
  Neither it nor the exact signed-sector split gives a lower bound on
  the joint higher spatial jets relative to \(F''(c)^2\), or an
  exterior interaction on a selected tube. [TND-D Note04,
  lines 18–61, 180–208][d04].

- **Inserted Ward ensemble.** At physical time zero and Mellin
  parameter \(s\ge0\), the ordered three-source-node carrier is
  \(w_s=q^s\prod_j\Phi(u_j)V(\mathbf u^2)V(R(\mathbf u))\),
  \(q=\prod_j u_j^2\), \(R=\Phi''/\Phi\).
  With signed insertion \(h\), \(M_3=Z E_s h\), and undivided response
  \(N=Z E_s J\), the established identity is
  \((s+1/2)M_3'+3M_3+N=0\).
  For \(T_M=\log q\), \(a=M_3'/M_3\), \(A_s=E_s h\),
  the curvature is
  \((\log M_3)''=[-a-E_s((T_M-a)J)/A_s]/(s+1/2)\).
  The mixed lower bound required by its Gaussian comparator remains
  unproved. The actual-source nonclosure excludes the specified fixed
  finite-polynomial pointwise ansatz \(J=P(T_M)h\). The variables are
  source nodes and a coefficient-moment tilt. Their formulas therefore
  have no selected zero marks, heat-time increment rate or paid
  curvature comparison for the present consumer. [MC04 Note01,
  lines 28–99, 115–154][ward] · [Separate internal assessment][wardreview].

- **Jensen signed averaging.** In the ordered four-source-node carrier
  \(w_{4,k}=q^k\prod_j\Phi(u_j)V(\mathbf u^2)V(R(\mathbf u))\),
  \(A_{4,k}=E_{4,k}h_4=F_{4,k}D_{4,k}/Z_{4,k}\), where
  \(F_{4,k}=\prod_{j=0}^3(2k+2j)!\). For fixed origin-side
  nodes \(a<b<c\) in the \(R\) coordinate, the actual source has
  \(\partial_Xh_4=24\alpha X^{-3/2}+O(X^{-2})<0\) eventually with
  \(\alpha=(\Phi^{(4)}/\Phi)[a,b,c]<0\).
  This defeats the global coordinatewise monotonicity premise of that
  order-four association argument. For \(k=0,1\), the later
  conditional average over the three interior source nodes tends to
  \(A_{3,k}>0\) as the outer node goes to infinity, and the selected
  marginal comparison has a positive eventual tail.
  The exact increment \(\operatorname{Cov}_{4,0}(h_4,q)/E_{4,0}q\)
  still needs a quantitative signed compact-plus-tail integral.
  Its large argument is a source coordinate and its clock an integer
  moment index. Neither is the chosen pair height or Newman time.
  [Signed-averaging Notes01, lines 21–47, 142–164][ja1] ·
  [Note03, lines 19–36, 40–98][ja3].

- **GT direct Fourier numerator.** The relevant deflated object is
  \(M=\int_0^1(\mathcal L[A]/A^2)(z_-+s(z_+-z_-))\,ds\) with
  \(A=F/Q\), \(\mathcal L[A]=(A')^2-AA''\). For \(D<0\) it is a
  vertical-segment average. At a real nondegenerate double it equals
  \([2(F''')^2-3F''F'''']/(18(F'')^2)\) at the center.
  For \(F\) the transform of the positively normalized even theta
  density, the numerator's complete positive spectral measure is the
  pushforward of \(\tfrac12u^2v^2(3u^2-4uv+3v^2)\,d\mu(u)d\mu(v)\)
  under \(u+v\). The zero-frequency atom is zero and the
  constant-mode/absolute-remainder allowance is exactly \(-3m_2m_4\).
  The other evaluated proposal fails a principal-minor test for the
  stated unchanged finite matrix with at least two distinct positive
  radii. Neither allowance pays the positive normalized numerator.
  These failures leave other jointly signed groupings outside their
  scope. [GT Note24, lines 29–69, 74–134][gt24] ·
  [GT Note28, lines 62–83, 133–188][gt28].

The audits preserve the role of the controls. The fixed-slice fields of
Note34 have identical projected counts, order/strip and a common collar
but opposite normalized signs. A positive Fourier-source representation
and a common physical heat-time tube are outside their supplied data.
The polynomial blur comparison has its own finite-error and internal
interaction scope. The positive-source finite Fourier examples defeat
generic positivity of the numerator under the shared finite-source
premises. The remaining order, strip, reflection and realizability
checks retain the documented classes in GT Notes28 and 33 and TND-OC
Note17. No audited predecessor supplies a selected-pair signed near lower
bound or an adequately accurate signed time integral at the needed scale.
The same shortfall applies to a direct evaluator given these inputs.
[GT Note35, lines 80–141][gt35] · [GT Note28, §4][gt28] ·
[GT Note33, §6][gt33] · [TND-OC Note17, §6][oc17].

[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[reuse]: ../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md
[gt12]: ../brainstorm/notes/12_VCD_GT_CORRELATION_PREDECESSORS_AND_DOUBLE_CLUSTER_DISCUSSION_20261117.md
[gt24]: ../notes/24_VCD_GT_FOURIER_GROUPING_AND_DEFLATED_CURVATURE_20261116.md
[gt28]: ../notes/28_VCD_GT_E03_FOURIER_GROUPING_SCREENS_20261116.md
[gt33]: ../notes/33_VCD_GT_E12_UNIFORM_SIGNED_FAR_EXTERIOR_20261117.md
[gt35]: ../notes/35_VCD_GT_B07_B08_SYNTHESIS_AND_CONTINUATION_20261117.md
[o18]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md
[o19]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/19_TND_O_E12_COLLISION_STABLE_MOMENT_ASSEMBLY_20261107.md
[o21]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md
[oc14]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/notes/14_TND_OC_B08_ARITHMETIC_MARGINAL_COLLISION_FRICTION_20261108.md
[oc17]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/notes/17_TND_OC_E10_R1_FULL_MARKED_PAIR_EVOLUTION_PROOF_20261108.md
[d04]: ../../../../investigations-5/08_theta_observables_newman_dynamics/01_direct_newman_realization/notes/04_TND_D_B02_COLLISION_DYNAMICS_RECONNAISSANCE_20261106.md
[ward]: ../../../../investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/04_biorthogonal_ensembles/notes/01_INSERTED_ENSEMBLE_IDENTITY_RETURN_20261101.md
[wardreview]: ../../../../investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/04_biorthogonal_ensembles/reviews/01_MC04_E01_SEPARATE_REVIEW_20261101.md
[ja1]: ../../../../investigations-5/07_positive_theta_primitives/01_jensen/02_signed_averaging/notes/01_INITIAL_BRANCH_EVALUATION_20261101.md
[ja3]: ../../../../investigations-5/07_positive_theta_primitives/01_jensen/02_signed_averaging/notes/03_J_B11_CONDITIONAL_AVERAGING_BRAINSTORM_20261101.md
