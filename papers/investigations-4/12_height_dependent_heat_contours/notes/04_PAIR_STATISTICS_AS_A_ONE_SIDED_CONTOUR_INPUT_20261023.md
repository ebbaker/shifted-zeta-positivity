# Pair statistics as a one-sided input to the deformed cap

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Authoring derivation with a separate same-model check of the normalization and lower-bound transfer; no specialist review.

**Status: conceptual continuation and proved elementary conditional interface; no new theta statistics acquired.** The author's question is whether smoothing could improve the zero distribution enough to justify a statistical approximation, such as pair correlation, along the deformed contour. The answer is conditional but constructive: such a quantitative theorem would add information absent from the earlier matched-model comparison. For the present lower-bound objective, a truncated pair lower bound can suffice; full convergence of the singular inverse-square moment is stronger than needed.

Read [Note 02](02_FINITE_BAND_GEOMETRY_AND_COMPARISON_CONTRACT_20261023.md) for the geometry and source obligations and [Note 03](03_COMPLETE_COUPLED_EXPRESSION_AND_COMPARISON_20261023.md) for the complete boundary expression. This note refines the interpretation of the inherited [PCC screen](../../11_late_heat_caps_and_charge_transport/notes/07_PCC_WEIGHTED_MOMENTS_AND_CAP_PHASE_SCREEN_20261022.md): that note's sparse-defect obstruction concerns an upper bound, asymptotic equality, or exclusion of every exceptional pair. It does not forbid a one-sided lower bound for a positive real pair statistic. The [result index](../../../../result-summaries/README.md), [local geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../avoid/README.md), [classification](../../../../avoid/01_restating_the_target.md), [scope rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [coupling rule](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) remain in force.

## 1. The statistical observable that actually enters

At a real time a, suppose the selected finite population consists of m simple real roots x_j, with independently justified regular cap charts as in Note 02. Reality of this population is an explicit local premise, not inferred from a plot or a PCC label. Let nu>0 be a fixed unfolding density at this slice, and define the ordered off-diagonal pair measure

\[
 \mu=\frac1m\sum_{j\ne k}\delta_{\nu(x_j-x_k)},\qquad
 Q_{\rm pair}=\int s^{-2}\,d\mu(s).
\]

The diagonal is excluded by labels. The exact source-product identity becomes

\[
 K_{\mathscr D}(a)=4m\nu^2 Q_{\rm pair}+\mathcal B_U(a).
 \tag{1}
\]

Indeed Q_pair=(2/(m nu²)) sum_(j<k)(x_j−x_k)^(-2), while the coefficient on the unordered pair sum in K is 8. The analytic-factor term includes exterior roots and normalization and remains indispensable.

The unit-density sine-kernel candidate is

\[
 R_2(s)=1-\left(\frac{\sin\pi s}{\pi s}\right)^2.
\]

The inherited PCC note derives
\(\int_{\mathbb R}s^{-2}R_2(s)ds=2\pi^2/3\).
A clock has the different moment pi²/3. A pair law must specify a joint height, population, and heat-time limit; a fixed finite population is an atomic measure, not an exact continuous law. The trial band of Note 02 is not itself a PCC asymptotic regime. [Montgomery's original paper](https://www-personal.umich.edu/~hlm/paircor1.pdf) studies scaled high-ordinate statistics under RH and distinguishes its theorem from the conjectural full law. No RH-dependent source theorem is imported unconditionally here.

## 2. Weak convergence does give a useful one-sided implication

Suppose positive pair measures mu_n converge vaguely to R2(s)ds, against continuous compactly supported test functions. Assign Q_n=+infinity if distinct labels coincide. Then

\[
 \boxed{\liminf_n Q_n\ge\frac{2\pi^2}{3}.}
 \tag{2}
\]

**Proof.** For each nonnegative continuous compactly supported f, vanishing near zero and satisfying f(s)<=s^(-2) elsewhere, Q_n>=integral f dmu_n. Pass to the limit for this bounded test. Now take an increasing family of such cutoffs approaching s^(-2) for every nonzero s. Monotone convergence on the limiting measure gives (2). The missing singleton has zero limiting mass. No uniform integrability of the finite-array inverse-square weights is needed for this lower bound.

Sparse very close pairs can destroy an upper bound or convergence to a finite constant, but they only increase this real nonnegative statistic. Thus “ordinary PCC is insufficient for the inverse-square statistic” needs its intended direction stated. It is insufficient for a two-sided approximation without extra near-zero and far-tail control; it still supports (2). It supplies no numerical rate for a fixed band.

The finite version is more directly useful. Choose **one** nonnegative bounded continuous compactly supported f with f<=s^(-2), and prove

\[
 \int f\,d\mu\ge q_f-\eta_f,
 \qquad q_f=\int f(s)R_2(s)\,ds.
 \tag{3}
\]

Then Q_pair>=q_f−eta_f immediately. An exact sine-kernel target is optional: any justified explicit comparison giving a useful right-hand side works. A complete PCC theorem is therefore not the minimal next task. A finite, quantitative lower bound for the weighted test actually consumed by the cap may be sufficient.

This is an elementary conditional transfer, not an established bound (3) for theta. It does not exclude a finite exceptional event or supply the necessary reality and chart inputs.

## 3. Retain the costs needed for the original cap

Put a=−epsilon. Under the separate real-type, nonvanishing source-product and root-chart hypotheses of Note 03 (5), let J_a be the complementary part of the full left cap and let S_epsilon include every other outward face. The inherited transverse estimate gives

\[
 I_0\ge\frac{k_\rho Y}{\pi}
 [4m\nu^2(q_f-\eta_f)+\mathcal B_U(a)]
 +J_a-S_\epsilon-\frac{k_\rho Y^3}{6\pi}M_2,
 \quad M_2=\sup_{0\le\sigma\le Y}|K_{\mathscr D}''(a+i\sigma)|.
 \tag{4}
\]

Equivalently, if a jointly derived source estimate establishes

\[
 \frac{k_\rho Y}{\pi}\mathcal B_U(a)+J_a-S_\epsilon\ge L_{\rm rest},
\]

then the statistical input produces

\[
 \boxed{I_0\ge
 \frac{4k_\rho Ym\nu^2}{\pi}(q_f-\eta_f)
 +L_{\rm rest}-\frac{k_\rho Y^3}{6\pi}M_2.}
 \tag{5}
\]

This is a precise way in which statistical information could simplify the task: replace individually resolved real pair contributions by one proven weighted lower bound. Interior negative-time events remain allowed by the fixed-domain lower transfer. Boundary charts and the real slice used in (4) must still be independently justified.

There are two material qualifications. First, K'' and the complete complementary term can be sensitive to the close pairs that were harmless for the positive real lower bound. Their costs cannot be erased by (2) or (3). Second, for complex time the root term is (z_j−z_k)^(-2), not |z_j−z_k|^(-2). Ordinary PCC for real locations or projections has no control of those complex phases. One must either retain the transverse bound in (4), or prove an appropriate signed complex-gap estimate directly on the actual boundary. The polynomial control in Note 03 prevents treating a positive real statistic as automatically positive after that continuation.

The new statistical input would lie outside Note 03's comparison with a fixed shared holomorphic coefficient model. Exact path equality does not imply equal difficulty of proving new estimates on those paths. The direct comparator nevertheless receives the new theorem as well; the gain must be in the resulting complete bound or verified cost.

## 4. Smoothing the field does not automatically regularize its zeros

For the convention H_tau=−H_zz, moving to tau=−s damps source frequencies by e^(−su²) and solves ordinary forward heat in s. It reverses the repulsive real-zero motion in increasing tau. For example,

\[
 H(\tau,z)=z^2-a_0^2-2\tau,
 \qquad z_\pm(-s)=\pm\sqrt{a_0^2-2s}.
\]

The two initially real roots move together, collide at s=a0²/2, and become nonreal. This is an exact heat control, not a theta prediction. It rules out a generic inference that ordinary heat smoothing makes real root spacings more uniform. [Rodgers–Tao](https://arxiv.org/html/1801.05914) analyze repulsion and local equilibration in increasing heat parameter under their stated hypothetical all-real negative interval; their result cannot be reversed into such an unconditional smoothing theorem.

Nor must a more regular distribution have the sine-kernel law. [Polymath, Theorem 1.5](https://arxiv.org/html/1904.12438) proves approximately clock-like positive-time high roots in its x>=exp(C/t) regime. This is outside the proposed microscopic 0+ face. A reference law should be selected by a proved regime, not by identifying “smooth” with GUE.

There is also a scale check. With nu=ell(h)/pi and epsilon=c(h)/ell(h)², the duration measured in mean-spacing-squared units is epsilon nu²=c(h)/pi². If c(h) tends to zero, the proposed step has vanishing duration on that scale. Away from singularly close pairs, a major rearrangement would therefore need a separate quantitative mechanism. Exceptional close pairs can change much faster, which does not establish uniform statistical regularization.

## 5. Research consequence and scope

The revised constructive question is: **can the deformed theta field admit a quantitative lower bound (3), uniform over the chosen height-dependent regime, whose improvement survives the complete remainder in (5)?** A positive answer could justify more aggressive approximation of the bulk root statistics and make the contour useful. It could first yield averaged or finite-height bounds without excluding every exceptional zero. Full PCC is one possible input, but may be substantially stronger than needed.

The [registered collision controls](../../../../result-summaries/12_collision_controls_and_screening.md) continue to satisfy the generic transfer identities. The real-slice and complete-boundary premises are not automatic on their event-containing caps. Euler-factor/reflected/positive-primitive controls lack unchanged complete theta arithmetic; finite weighted-square and finite-prime controls fail the reflection/full-coefficient requirements specified in Note 02; normalized endpoint controls fail ordinary Dirichlet-series arithmetic. None of those distinctions by itself proves a favorable statistical estimate or excludes a control. The sparse-array construction is an information-class example, not a construction of theta zeros.

No task status advances: HDC-03 source acquisition and HDC-04's actual comparison are still open. This note records a potentially useful one-sided statistical route and narrows the earlier pessimistic interpretation; it does not assert that smoothing produces PCC or supplies the unpaid source bounds.

The author's subsequent density-one objective has a different, less singular consumer: [Note 05](05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md) transfers an earlier complete projected-pair upper bound to RH-conditional almost-all simplicity. [Note 06](06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md) connects the previously studied Vandermonde Hessian to a bounded spectral count of endpoint defects. Those real-time routes do not require completing the physical cap estimate first, and neither currently has its missing theta statistical upper bound.
