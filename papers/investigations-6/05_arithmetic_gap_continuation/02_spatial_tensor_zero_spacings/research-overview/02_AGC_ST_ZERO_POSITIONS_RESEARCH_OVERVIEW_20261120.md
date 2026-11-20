# Predicting the position of a marked zero

20 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI Codex LLM assistance. The coordinating chat's actual model and reasoning effort are unavailable in its registered history. Scientific setup for task family **AGC-ST-Z**. The cited proofs and assessments retain their own provenance. This overview issues no research packet.

**Research update, 20 November 2026.** Prepared for Edward Baker with Codex assistance, coordinating gpt-6.2-astra/ultra. For the pair initially in [28,29] and [42,43], the independent anchors and a complete exterior bound now give finite signed position estimates at physical time 0.0001. The original scientific question and its known benchmarks follow. [Position results, comparison and remaining question](../notes/13_AGC_ST_Z_POSITION_MILESTONE_AND_CONTINUATION_20261120.md).

## Which position should the tree predict?

Start with a marked adjacent pair at a reference time \(s\), an absolute origin in Newman height, and an orientation identifying the lower or upper member. Can signed information carried by its spatial environment predict the location of that member at \(t\)? The time displacement \(x_\pm(t)-x_\pm(s)\), or its difference from an independently specified clock displacement, is an analytical target. The initial location, admissible arithmetic source information, time interval and rule for continuing the label must be specified before making the prediction. An interval for the initial coordinate plus a displacement enclosure gives an absolute position interval. The starting gap alone supplies no origin.

The literal field is \(H(t,z)=\int_0^\infty e^{tv^2}\Phi(v)\cos(zv)\,dv\) with the complete theta coefficients. It satisfies \(H_t=-H_{zz}\) and \(H(0,z)=\xi((1+iz)/2)/8\). A positive real \(z\) at \(t=0\) gives the critical-line ordinate \(z/2\). Begin on a compact real time chart with a conjugation-invariant cleared boundary enclosing two zero occurrences and retaining the same pair. An ordinal \(n\) needs a certified initial count or a theorem calibrating the source labels to that ordinal. A high clock label can independently identify a marked root. A chart alone identifies a local unordered pair. [AGC §1, source and normalization](../../manuscript/sections/01_source.tex), [§2, counted pair](../../manuscript/sections/02_pair_chain.tex)

## Where absolute motion enters

Write \(P=(z-c)^2-D,\ H=PA,\ R=A_z/A\) on the marked chart. For \(D>0\), \(a=c-\sqrt D,\ b=c+\sqrt D\), and \(g=b-a\). Let \(\mathcal I f=(2\pi i)^{-1}\oint_\Gamma f(z)\,dz\) and \(B=H_z/H\). The complete-field formulas are

\[
 \begin{aligned}
 c&=\tfrac12\mathcal I(zB), & D&=\tfrac12\mathcal I(z^2 B)-c^2,\\
 c_t&=R(a)+R(b)=\tfrac12\mathcal I(H_{zz}/H),&
 D_t&=2-4DM,\qquad M=-\frac{R(b)-R(a)}{b-a}.
 \end{aligned}
\]

The sum of exterior values supplies the signed common motion. Its divided difference supplies the relative motion. Upward multiplication of sibling polynomials and downward transmission of the sibling logarithmic derivative assemble the same \(R\). The exterior includes every occurrence, with multiplicity, even at nonreal positions. Canonical opposite-pair grouping or the cleared contour controls its first-power contribution. An unrestricted, unregularized absolute first-power sum over those occurrences is generally unavailable. The formula for \(c_t\) also permits direct evaluation on the *single* target contour. These are inherited exact identities. [Spatial split and exterior germ](../notes/02_AGC_ST_E01_SPLIT_GENERATOR_20261120.md), [E02, paired readouts and time jets](../notes/03_AGC_ST_E02_PAIR_AND_FORCING_20261120.md), [internal assessment](../reviews/02_AGC_ST_LOCAL_GENERATOR_ASSESSMENT_20261120.md)

For physical \(s<t\) within a separated chart the endpoint displacement is

\[
 x_\pm(t)-x_\pm(s)=\int_s^t [R(a)+R(b)](\tau)\,d\tau
                     \ \pm\big(\sqrt{D(t)}-\sqrt{D(s)}\big).
\]

Backward from \(t_*\) with \(u=t_*-t\), the center integrand changes sign, as does \(D_u=-2+4DM\). On a simple branch the direct velocity is \(x_t=H_{zz}/H_z\). At a double the symmetric coordinates remain analytic, \(c_t=2R(c)\) and \(D_t=2\). The individual square-root labels there ordinarily have no finite physical-time derivative. Transport the counted polynomial or the pair \((c,D)\) through that time. A negative real \(D\) gives a conjugate pair. Switching chart walls or continuing a label past a merger needs a certified overlap and an explicit convention for any individual label. [AGC §2](../../manuscript/sections/02_pair_chain.tex), [E02, Hermite remainder at a double](../notes/03_AGC_ST_E02_PAIR_AND_FORCING_20261120.md)

## What the existing forcing result contributes

E03 takes the two actual endpoints, the actual gap and labeled exterior marks as inputs. Real left and right marks at normalized outward distances \(x_{m,-},x_{m,+}\) contribute the sum of the same kernel at those distances. Their mean and quadratic errors retain a cancellation in the dimensionless forcing \(K=24D^2S_2+32D^3S_3\), where \(S_j\) sums the inverse \(j\)-th powers of \((\rho-a)(\rho-b)\) over the complete exterior. Swapping left and right preserves this information. The forcing governs \(g_{tt}=16(K-1)/g^3\) on a separated real chart. Integrating that equation would require independent initial \(g\) and \(g_t\) and would still leave the signed center displacement to be determined. [E03 finite-head inequalities and signed complement](../notes/04_AGC_ST_E03_PAIRED_FORCING_20261120.md)

E04 fixes a positive-time slab \([t_0,t_*]\subset(0,1/2]\), a sufficiently high source clock label \(n\), \(X=q_n(t_*)\) and \(L=\log(X/(4\pi))\). Let \(\sigma_X\) bound the position error for all retained high labels, including the targets and the exterior marks. It obtains

\[
 |K-1|\ll L\sigma_X+(X^2L^3)^{-1}+(XL)^{-3}.
\]

The improved deterministic term comes from pairing opposite displacements before taking absolute values. The source term dominates that improvement, and the direct sum given the same pairs attains the same bound. The uniform exhaustion concerns forcing *values*; the contour argument supplies time derivatives separately. The clock already supplies the positive location and common labels. The result gives no center velocity by differentiating a position error. E05 r2 accepted E03 on its separated slice and E04 on its fixed positive slab in a separate internal assessment. The height onset depends on \(t_0>0\). [E04 proof and direct comparisons](../notes/05_AGC_ST_E04_CANONICAL_FORCING_20261120.md), [E05 r2 assessment](../reviews/03_AGC_ST_SPATIAL_FORCING_ASSESSMENT_20261120.md), [recorded disposition](../research-progress/handoffs/AGC_ST_E05_RETURN_R2_20261120.md)

## A finite orientation test

For any real-even physical solution, reflecting the marked pair \((a,b)\mapsto(-b,-a)\) preserves the gap and complete forcing, and interchanges the left and right marks. The center and its velocity change sign. This is a symmetry of the literal theta field when the choice of marked pair ranges over both halves. Specifying a *positive* high clock label supplies additional information and excludes the reflected negative mark from that target class.

A finite even control exhibits the velocity distinction without a translation of the source. Initialize polynomial heat flow at \(H(0,z)=(z^2-1)(z^2-4)\). On a short interval the roots remain real and simple. At time zero use \(x_t=2\sum_{\rho\ne x}1/(x-\rho)\). The velocities at \(1,2\) are \(-1/3,19/6\); the pair center velocity is \(17/12\). Its reflected pair at \(-2,-1\) has center velocity \(-17/12\) and the same gap and \(K\). The conclusion concerns unoriented, reflection-invariant summaries of marked pairs of even heat fields. This finite field lacks the complete theta source. Neither the example nor the canonical symmetry establishes two possible values for a fixed, independently identified positive theta zero. [AGC §2, finite-product velocity](../../manuscript/sections/02_pair_chain.tex), [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)

## What would distinguish a predictive estimate?

Even an initial anchor on the positive half-line leaves a real information question. In Baker's [shared brainstorm addendum](../../../brainstorm/notes/06_SPATIAL_TTN_ZERO_SPACING_20261119.md#20-november-2026-discussion-of-absolute-zero-positions), the initial even polynomials \((z^2-1)(z^2-4)(z^2-u)\), with \(u=1/4\) and \(u=6\), give polynomial heat solutions with the same marked positive roots \(1,2\) and the same complete \(M=37/20\) and \(D'=3/20\) at that slice. Their centers move at \(103/20\) and \(-59/60\), respectively. This rules out recovery of that instantaneous center velocity from the specified anchored data in this finite polynomial class. It gives a starting control for testing any proposed *additional* oriented message. The [complete gap-lattice proposition](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/manuscript/sections/14_coupled_lattice.tex) explains the corresponding translation freedom in the full simple real chain and the dependence on nonreal exterior data when only a real block is given.

A first decision should choose an oriented, source-acquirable quantity, such as the integrated exterior sum after subtracting a named reference center velocity. Specify an anchor, a nonzero time span, the signed output and the complete residual budget. Spatial siblings might cancel contributions to that integral, or a holomorphic boundary approximation might have a small signed error in its center readout. Both mechanisms need a controlled remainder for the full exterior, including the phase or orientation lost by a span-only summary. Reading the target-time zero or an equivalently precise center as an input would make recovery of that same position a diagnostic. Target-time source evaluation can instead serve as direct comparison; any source information given to the spatial predictor must also be available to its comparator.

There are two concrete benchmarks. With the E04 position data, the known source clock already gives \(x_n(t)-x_n(s)=q_n(t)-q_n(s)+O(\sigma_X)\) on its slab. With the additional holomorphic spatial residual, the earlier CM analysis gives \(|x'_n+\pi/4|\ll L\epsilon_X\) for \(\epsilon_X=X^{-c_*t_0}+L/X\). Consequently the direct displacement is \(-\pi(t-s)/4+O(|t-s|L\epsilon_X)\) for positive high labels, and averaging the two endpoint bounds gives the corresponding center estimate. In a finite chart, direct root velocities and the single-contour center drift use exactly the same arithmetic inputs as a factorized calculation. Recovering any of these bounds is a compatibility check. A meaningful new estimate must improve the signed residual or the resulting endpoint enclosure for a specified interval at matched information, or exhibit a quantified obstruction for a stated class of spatial states. [E04, source localization](../notes/05_AGC_ST_E04_CANONICAL_FORCING_20261120.md), [CM §13, canonical velocity bound and integrated comparison](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/manuscript/sections/13_canonical_time.tex), [E02, direct contour](../notes/03_AGC_ST_E02_PAIR_AND_FORCING_20261120.md)

The comparison belongs in position units. If \(D,\widehat D\ge d>0\), then
\[
 |x_\pm-\widehat x_\pm|
 \le |c-\widehat c|+\frac{|D-\widehat D|}{\sqrt D+\sqrt{\widehat D}}
 \le |c-\widehat c|+\frac{|D-\widehat D|}{2\sqrt d}.
\]
This enclosure applies independently at each time and can lose correlations when used twice for a displacement. A sharper joint enclosure would have to retain those correlations. Near \(D=0\), root recovery becomes ill-conditioned; the polynomial or a two-root enclosure can still be quantitative. Any estimate using \(B\), \(R\) or \(H_{zz}/H\) also pays the actual boundary denominator floor, derivative errors and integration errors throughout the chart. Small error in a tensor or in \(K\) alone supplies none of those allowances. [AGC §6, denominators and joint readout](../../manuscript/sections/06_residual_transport.tex), [§8, coupled two-root error](../../manuscript/sections/08_local_estimates.tex)

## What would an infinite tree contribute?

For a depth or cutoff \(L_0\), let \(v_{L_0}\) be the signed center velocity computed from its retained oriented blocks. A candidate approximation result would supply an independently established envelope \(e_{L_0}\) on the path with \(|v_{L_0}-c'|\le e_{L_0}\). Its contribution to the absolute position error is at most \(\int_{\min(s,t)}^{\max(s,t)}e_{L_0}(\tau)\,d\tau\), in addition to the initial center error and the relative-motion error. The research question is which cancellations yield a useful decay rate for that integral from the actual data. Refining the partition of a fixed divisor, exhausting its distant exterior and increasing the number of retained coefficients are distinct operations. Each asserted limit must state what is fixed, what is uniform in time, and whether the equally informed direct integral shares the same bound. For several adjacent zeros, \(x_{n+k}=x_n+\sum_{j=0}^{k-1}g_{n+j}\) is also a direct comparator once one absolute coordinate is given. A joint enclosure should retain the common anchor and shared-edge errors. [Gap-chain and block telescope](../../manuscript/sections/02_pair_chain.tex)

## Premises and research ownership

The [results index](../../../../../result-summaries/README.md) and [patterns index](../../../../../avoid/README.md) route the [tensor and gap results](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md), [target classification](../../../../../avoid/01_restating_the_target.md), [control-premise rule](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) and [coordinate-realization caution](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md). A finite displacement estimate is a local analytical target. A spatial realization of the exact drift is a representation identity. Neither supplies a global zero-location theorem.

- An Euler-factor control with \(0<c<1\) preserves the entire real zero list at time zero while changing the simple-root velocity by \(2f'/f\), \(f=1+c\cos(ax)\). It fails the unchanged arithmetic source and exterior. Thus even *absolute initial positions* may be insufficient for the subsequent motion across this control class.
- Weighted squares and finite-square modifications change the full coefficients; finite-prime orbit controls can preserve selected identities while failing full reflection. Reflected super-Gaussian and smooth positive-primitive controls lack the complete theta square expansion. Reflection rigidity in the normalized square-comb class identifies the source but gives no signed center estimate.
- The low-rank three-atom field \(2+2e^{t-T}\cos z\) has a genuine double at \(T\) and lacks the full theta source. A position calculation there must admit the coalesced pair. Fixed-event and finite-profile families fail the complete profile or eventual simplicity, while the RH-conditional endpoint perturbation fails ordinary Dirichlet arithmetic. A changed observation kernel fails the fixed cosine dynamics. These examples test the proposed premises on their named classes. [Analytical control crosswalk](01_AGC_ST_RESEARCH_OVERVIEW_20261119.md#tests-and-ownership)

**AGC-ST-Z-B01** is the unissued conceptual choice of an initial anchor, signed predicting state, time family and equally informed direct comparison. The [zero-position plan](../research-plan/02_AGC_ST_ZERO_POSITIONS_RESEARCH_PLAN_20261120.md) and [zero-position register](../research-progress/02_AGC_ST_ZERO_POSITIONS_RESEARCH_PROGRESS_20261120.md) own this sequence. Existing forcing work stays with the [gap register](../research-progress/01_AGC_ST_RESEARCH_PROGRESS_20261119.md); [AGC](../../README.md) and [the parallel Jacobi investigation](../../01_jacobi_integer_hierarchy/README.md) retain their respective arithmetic and finite-degree questions. Bibliographic records, inspected passages and source ownership are in the [branch reference guide](../references/README.md).
