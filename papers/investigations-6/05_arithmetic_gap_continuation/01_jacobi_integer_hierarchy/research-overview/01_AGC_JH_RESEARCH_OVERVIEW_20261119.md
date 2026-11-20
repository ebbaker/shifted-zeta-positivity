# Research overview: Jacobi truncation and the integer hierarchy

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual lead model/effort unavailable in
canonical public-history metadata. Author-selected continuation defaults,
revised 19 November 2026: Astra/ultra lead, with gpt-6.2-sol/ultra bounded
helpers authorized. The earlier Sol 6.1 setup review retains its provenance.

**Research setup, not a new theorem or acquired canonical inequality.**
The [plan](../research-plan/01_AGC_JH_RESEARCH_PLAN_20261119.md) defines work;
the [sole register](../research-progress/01_AGC_JH_RESEARCH_PROGRESS_20261119.md)
owns status. Read the [result index](../../../../../result-summaries/README.md),
especially [approximation18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [patterns index](../../../../../avoid/README.md), particularly
[target classification01](../../../../../avoid/01_restating_the_target.md),
[control premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate caution03](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[joint errors12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [sibling results15](../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md).

## 1. Question and why this is a useful return

Can a canonical Jacobi degree update, together with its exact omitted-tail
response, control a counted zero cluster's integer exterior moments with
enough sign and compatibility to improve a complete gap-continuation
estimate? A particularly interesting outcome would be an induction in N
whose invariant includes the cluster count, contour clearance, compatible
moments and the paid source error.

VCD began with coefficient dynamics, found the boundary-memory problem,
and moved to counted clusters and their heat-time transport. That led to
the complete integer S/T and split-pole p,q hierarchy, then to separate
complex-exponent representations and compatible approximation. We now
start with the hierarchy's precise consumers and ask what the original
Jacobi system can supply. The proposed gain is a signed estimate, not
another exact change of coordinates.

The preferred first route is a **joint degree/time error estimate on one
counted pair chart**, with N versus N+2 available when parity helps.
Derive the integer hierarchy forced by the actual Jacobi heat defect and
compare it with the exact degree increment before taking absolute values.
This is more concrete than positing a closed ODE for arbitrary truncated
moments. Whether it improves on an equally informed direct calculation
remains a research question.

## 2. Fixed source, three parameters, two finite evolutions

Keep the complete theta amplitude and literal Fourier observation:
\[
 H(t,z)=\int_0^\infty e^{tv^2}\Phi(v)\cos(zv)\,dv,\qquad
 Z_t=\int_{\mathbb R}e^{tv^2}\Phi(v)\,dv,\qquad F_t=2H(t,\cdot)/Z_t.
\]
The source and normalization are those of the
[AGC overview](../../research-overview/01_AGC_RESEARCH_OVERVIEW_20261119.md)
and [VCD manuscript, moving-basis evolution](../../../03_volterra_coefficient_dynamics/manuscript/main.tex).
Initially restrict inherited uniform estimates to real t in [0,1/2].
A wider regime requires an explicit new estimate.

For the orthonormal source polynomials,
\[
 vq_n=a_{n+1}q_{n+1}+a_nq_{n-1},\quad
 a_n=\sqrt{\beta_n},\quad
 \partial_t\beta_n=\beta_n(\beta_{n+1}-\beta_{n-1}),\quad \beta_0=0,
\]
\[
 F_t(z)=\langle e_0,e^{izJ(t)}e_0\rangle,\qquad
 G_{N,t}(z)=\langle e_0,e^{izJ_N(t)}e_0\rangle.
\]
Here J_N is the principal N-site block, with sites 0 through N-1.
The three parameters have distinct roles: t is physical Newman time,
z (or real x) is observation height, and N is approximation degree.
Use L for a retained moment order; neither L nor a zero-product cutoff
is the number of Jacobi sites.

The eigenvalues of J_N are source nodes. The zeros under study are zeros
of G_N in z. Even G_2 is a cosine with infinitely many zeros. Thus a finite
matrix neither gives a finite zero divisor nor closes finitely many
exterior moments. Real source nodes and their interlacing do not imply
Fourier-zero interlacing. See [VCD finite readouts](../../../03_volterra_coefficient_dynamics/manuscript/sections/readouts.tex),
equations finite-readout, two-zero-problems and small-heads.

There are two finite families worth comparing at the first decision:

1. **Moving canonical head:** G_{N,t} uses the true coefficients at each
   t. Its last coefficient derivative depends on the omitted beta_N.
   Setting beta_N=0 produces a different finite Volterra flow. For N>=2
   the actual head has the exact defect
   \[
   R_N=(\partial_t+\partial_z^2+\beta_1)G_{N,t}
       =\beta_N\beta_{N-1}\partial_{\beta_{N-1}}G_{N,t}.
   \]
   This is inherited from [VCD gap transport](../../../03_volterra_coefficient_dynamics/manuscript/sections/gap_transport.tex),
   equation gt-residual-contour, including its spectral contour formula.
2. **Fixed initial head with heat weighting:** a candidate comparison is
   \[
   \widehat F_N(t,z)=
   \frac{\langle e_0,e^{(t-t_*)J_N(t_*)^2}e^{izJ_N(t_*)}e_0\rangle}
        {\langle e_0,e^{(t-t_*)J_N(t_*)^2}e_0\rangle}.
   \]
   This is the finite analogue of VCD's exact fixed-basis representation,
   equation twochains. Its heat normalization, relation to the closed
   finite Volterra lattice, and complete approximation error are tasks
   to check if selected. It agrees with G_{N,t_*} at the initial slice,
   but must not be identified with G_{N,t} at later times.

The first family is the default analytical baseline because its signed
error and defect are already developed. The second is a bounded
alternative if removing the time defect actually improves the complete
budget. Neither is a changed physical source: both are approximants whose
difference from the unchanged theta field must be paid.

## 3. The integer hierarchy is the target description

On a conjugation-symmetric count-two chart define
\[
 c=(z_++z_-)/2,\quad D=((z_+-z_-)/2)^2,\quad s=\sqrt D,\quad
 X_j=\rho_j-c-s,\quad Y_j=\rho_j-c+s,
\]
\[
 P_{p,q}=\sum_{\rho_j\ {\rm exterior}}X_j^{-p}Y_j^{-q}.
\]
Keep p,q positive integers in mixed rows, and the necessary axes
(p,0),(0,q) with p or q at least two. Thus the complete domain is
p,q in the nonnegative integers with p+q>=2. The first-power axis sums
are not individually introduced in the infinite system.

The full exterior, multiplicities and compatibility of neighboring pair
charts are part of the data. The integer recurrence is algebraically
closed as an **infinite** hierarchy. Through D=0 use
\[
 Q_j=(\rho_j-c)^2-D,\quad
 S_n=\sum_jQ_j^{-n}\ (n\ge1),\quad
 T_n=\sum_j(\rho_j-c)Q_j^{-n}\ (n\ge2),
\]
\[
 M=P_{1,1}=S_1,\qquad
 S_n=P_{n,n},\qquad T_n=\tfrac12(P_{n-1,n}+P_{n,n-1}).
\]
These retain both even and odd relative information; moments of Q alone
lose it. The S/T variables are regular through a target merger where
split labels and their 1/s coefficients are not.
[AGC manuscript, integer split recurrence and symmetric evolution](../../manuscript/sections/03_hierarchy.tex),
equations hier-P, hier-mixed, hier-axis-one/two, hier-overlap and hier-change,
is the primary current source. No independent complex p,q extension is
selected; the separate single complex exponent is background only.

The lowest actual-field equations are
\[
 \partial_tD=2-4DM,\qquad
 \partial_tM=2M^2-12S_2-16DS_3.
\]
In backward time u=t_*-t, the useful consumer is the complete integrated
gap drift, or its equivalent whole-interval transport budget. The
hierarchy helps only if the necessary signed combinations, contour floors
and time integrals can be bounded without assuming the separation sought.

## 4. Available bridge and the new work it still needs

For fixed t the omitted Jacobi chain gives exact memory in **x**, not t:
\[
 \frac{dy}{dx}=iJ_Ny-\beta_N b\int_0^x
 k_N(x-v)y_{N-1}(v)\,dv,\qquad
 F-G_N=-\beta_N(p_N*k_N*y_{N-1}),
\]
with y the projected full orbit, b=e_{N-1}, p_N=e_0^Te^{ixJ_N}b,
and k_N the disconnected tail's diagonal propagator.
[VCD boundary-memory proposition](../../../03_volterra_coefficient_dynamics/manuscript/sections/memory.tex)
proves these identities. The exact kernel retains the omitted chain;
it is not a finite closure. Its real-axis bound does not imply a uniform
bound at complex heights as the cut moves.

A second signed description, already proved in the VCD manuscript, is
\[
 F-G_N=L_NE_N,\qquad
 L_N=(-1)^N\Big(\prod_{j=1}^N\beta_j\Big)\frac{z^{2N}}{(2N)!},
\]
\[
 G_{N+1}-G_N=L_N\left(E_N+
 \frac{\beta_{N+1}z^2}{(2N+1)(2N+2)}E_{N+1}\right).
\]
See [complete error law](../../../03_volterra_coefficient_dynamics/manuscript/sections/error_law.tex)
and [successive degrees](../../../03_volterra_coefficient_dynamics/manuscript/sections/zero_geometry.tex),
equations error-factorization and degree-step. E_N is an entire
characteristic transform of a specified error law, not a freely selected
phase. Estimating its correlation with the actual readout is additional work.
These displayed degree formulas concern the moving canonical family.
If the fixed-initial-head heat-weighted family is selected, derive its
weighted degree increment and the two normalization factors separately;
the moving-head identity cannot be transferred verbatim to later times.

For a field Y with residual R=(partial_t+partial_z^2+beta_1)Y,
the counted-pair law is already
\[
 \partial_tD_Y=2-4D_YM_Y
 -\frac1{2\pi i}\oint_\Gamma (z-c_Y)\frac{R}{Y}\,dz.
\]
Here M_Y is the exterior interaction in a justified product/contour
description; its definition and product assumptions must be verified for
each finite family. This formula is inherited from
[VCD pair transport](../../../03_volterra_coefficient_dynamics/manuscript/sections/gap_transport.tex),
with K_Y=-M_Y. The new task is the matching forced integer hierarchy and
a **joint bound** on its degree update and residual, including changes of
c,D and the trace kernels. One must not apply the unforced theta hierarchy
to moving G_N without these terms.

The bridge should use count-two contour moments and the analytic logarithm
of G_{N+k}/G_N on a cleared collar (k=1 or 2). This avoids imposing real
simple limiting roots. It must carry the normalization, denominator,
logarithm condition, all omitted terms, and any chart transitions.
The route is a proposed estimate, not an established sign mechanism.

## 5. Induction in N: the precise opportunity

An induction should propagate a useful cluster statement, not all-real
zeros of every finite readout. Candidate A is a count/collar invariant and
a lower bound on the limiting or transported D, with a summable,
fully accumulated degree-error budget. A finite positive margin is a
valid local result but not an all-height theorem.

Candidate B adapts the earlier
[VCD degree-nonreality proposal](../../../03_volterra_coefficient_dynamics/02_degree_nonreality_contraction/research-overview/01_VCD_NC_RESEARCH_OVERVIEW_20261116.md):
\[
 u_N=(-D_N)_+,\qquad
 u_{N+k}\le(1-\alpha_N)u_N+\varepsilon_N,\quad
 0<\alpha_N\le1,\quad\varepsilon_N\ge0,
\]
\[
 \sum_{N\ {\rm along\ the\ chosen\ subsequence}}\alpha_N=\infty,
 \qquad \varepsilon_N/\alpha_N\longrightarrow0.
\]
Together with a justified common cluster and D_N->D, these conditions
force D>=0. The elementary implication is inherited; the **canonical
inequality is unproved**. Alpha and epsilon must be acquired independently
of the desired sign, from specified source/hierarchy information.
The new branch tests whether the integer hierarchy supplies that missing
input. It does not relabel the old conditional implication as a result.

Two-degree steps can avoid parity alternation, but both the subsequence
and identification of its limiting cluster must be justified. N-dependent
contours require additional transition payments. Summable gains alone
are insufficient, and rapid convergence can converge to a nonreal pair.
The inherited fixed-simple-real-zero asymptotic assumes the real simple
limiting root and cannot seed an argument whose purpose is to prove reality.

D>=0 permits a double real zero. Collision exclusion across physical time
needs control on the relevant time neighborhood, and a two-zero argument
does not cover larger clusters. Extending any mechanism to all heights
and time zero would reach the full reality target. That target is stated
here once; finite checks are not evidence for it.

## 6. Established obstacles, with their scope

| Inherited result | Constraint on this plan |
| --- | --- |
| Jacobi quadrature converges on fixed compact complex sets, uniformly on compact heat intervals; counted c_N,D_N converge with paid contour margins | Convergence identifies clusters but supplies no favorable sign. The count and denominator floor need independent acquisition. |
| Exact midpoint reconstruction with the same tail model gives the same direct readout | A factorization alone cannot improve the same-information consumer. |
| Finite canonical head/score matching admits the E07 perturbations; E10 permits either sign of the next score defect under its different smooth-source conditions | Finite score consistency is not a source-specific induction. E07 has no prescribed compact nonreal-zero location; E10 has no proved Fourier-zero conclusion. |
| Full canonical score equations characterize the source under their integrability hypotheses | Source identification alone gives no quantitative tail-to-gap gain. |
| Fixed integer moment heads have four boundary residual rows and geometrically small fixed-collar tails | The independently paid constant-tail, absolute-Jacobian comparison diverges factorially with moment order. This excludes that allowance, not signed evolution or every closure. |
| AGC's recent independent core-rotation envelopes fail, even with the actual dyadic phase | Preserve shared phase/source information. Those arithmetic estimator exclusions do not exclude Jacobi/hierarchy coupling. |

Sources: [VCD cluster resolution](../../../03_volterra_coefficient_dynamics/manuscript/sections/cluster_resolution.tex);
[VCD connected synthesis09](../../../03_volterra_coefficient_dynamics/notes/09_VCD_CONNECTED_RESEARCH_SYNTHESIS_20261116.md);
[midpoint synthesis15](../../../03_volterra_coefficient_dynamics/notes/15_VCD_MIDPOINT_RESEARCH_SYNTHESIS_20261116.md);
[CM finite hierarchy](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/manuscript/sections/10_finite_hierarchy.tex),
propositions fin:residual and fin:positive-box; and
[AGC continuation24](../../notes/24_AGC_ACTUAL_PHASE_MILESTONE_AND_CONTINUATION_20261119.md).
The CM common-time approximation uses a finite **zero product**, not J_N;
its accuracy and conditioning cannot be transferred by identifying cutoffs.

## 7. Analytical control screen at setup

This is a premise screen using the recorded proofs in
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
not a fresh replay or a newly verified induction inequality. Every later
candidate must additionally test its quantitative premise on a domain
containing the relevant control event. Failing a literal source identity
does not establish failure of a coarse inequality derived from it.

| Control family | Premise absent from the intended theta application; consequence |
| --- | --- |
| Euler-factor sources | Unchanged ordinary Dirichlet coefficients and full theta source fail; generic positivity, Jacobi identities and heat flow still do not distinguish them. |
| Weighted-square and finite square-tail controls | Full reflection/canonical coefficients fail despite selected endpoint, moment or score matches. Nonreal zeros need not occur in a prescribed compact chart. |
| Reflected super-Gaussian | Unchanged square arithmetic fails; the theta order-one product regime is also not inherited. Reflection and positive Fourier–Gram forms alone do not supply the sign. |
| Smooth shape/positive-primitive controls | Exact theta square expansion fails while strong shape, primitive and endpoint information can survive. |
| Finite-prime controls | Full canonical reflection/arithmetic fails; fixed finite prime agreement is not uniform full-source information. |
| Atomic threshold and finite-profile controls, including continuous compact extensions | Full theta profile/growth and eventual simplicity fail. Atomic chains terminate; continuous extensions have different support and source-score hypotheses. |
| RH-conditional endpoint controls | Ordinary Dirichlet arithmetic fails and the construction retains its RH hypothesis. Do not merge its preservation list with a different control. |
| Changed observation kernels | The literal cosine/Newman observation equation fails. The source operator alone cannot replace it. |
| Actual-profile positive-measure relaxations | The actual integer zero divisor/field-realizability premise fails; positive fractional masses are not a physical theta event. |
| VCD E07 finite canonical-score and E10 smooth next-defect controls | E07 loses later smooth reflection and has nonreal zeros without a fixed compact location. E10 changes arithmetic and proves next-defect freedom, not collision. Keep the two classes separate. |
| Static divisor examples with missing odd information | They test insufficient reduced coordinates, not a common-time theta field. The present full p,q or S/T system retains the missing odd data. |

On a genuinely colliding continuous control, a common approximating cluster
on its nonreal side has u_N tending to a positive limit. Therefore the
proposed contraction, divergent gain and subordinate-error conditions
cannot all hold there. This logical test does not identify which
unproved canonical estimate fails. The exact quadratic heat solution
z^2-2(t-T) likewise shows why zero defect alone cannot protect a gap:
its strict integrated gap margin fails. The Gaussian three-site example
in VCD tests the separate false inference from positive Jacobi nodes
to all-real Fourier zeros; it does not satisfy the theta coefficient envelope.

## 8. Evidence, comparison and ownership

A useful first result is a proved and assessed complete bound with a
nonvacuous constant/range, a certified local margin, or a quantitative
failure of a specified estimating class. Exact bridge identities are
infrastructure; they must be labeled as such. A new region, stronger
Newman bound, or uniform induction would be separate achievements.

Give the direct comparator the same coefficients, extra links, source
tails, arithmetic information, time anchors and contour data. A gain in
an outer error bound can be useful; no gain over the exact same feasible
set is presumed. Report cost only when measured. Known-coverage cells
are conditioning tests, not new coverage. Do not import AGC's
D_H>.1493308659 as a Jacobi certificate without a new comparison.

All inherited reviews are internal LLM checks, often sharing source
premises, not independent specialist review. Reference ownership and
inspection scope are in [references](../references/README.md).
AGC-JH owns the coupled interface and its consumers; VCD-NC's general
fixed-time degree question and parent AGC-B07/E19 remain unchanged.


## First milestone update, 19 November 2026

[Notes02–06 and their assessment](../notes/06_AGC_JH_FIRST_RESEARCH_MILESTONE_20261119.md) now supply the forced integer interface and a complete signed first-variation remainder. The finite two-degree difference has a source-node simplex formula using only the acquired prefix, and its complete relative time forcing reduces to endpoint corrections. Direct contour evaluation with the same inputs can do the same. An explicit continuous compact positive source has infinitely many positive and negative counted-gap increments on each parity; this rejects a generic eventual-monotonicity inference, not a theta-specific induction. At this first milestone the canonical signed functional, count/floor data and seed remained unpaid, leading to B03 r2. The second milestone below supplies the signed correction on one chart.

## Second milestone, 19 November 2026

[Note07](../notes/07_AGC_JH_CANONICAL_SIGNED_CONTOUR_20261119.md) supplies the first measured canonical signed correction in this branch, at physical time zero and N=24. It uses an independently counted low band. Both complete-source and finite-head error enter, and direct bracketing gives a tighter correction. [Review03](../reviews/03_AGC_JH_CANONICAL_ACQUISITION_ASSESSMENT_20261119.md) assesses this fixed scope. At the second milestone, physical-time persistence on one already counted slab was the open extension.

## Third milestone, 19 November 2026

[Note08](../notes/08_AGC_JH_PHYSICAL_TIME_SLAB_20261119.md) settles that extension for degree 24 on [0, 0.0001]. At every time the head overestimates the squared half-gap by at least 4.956734690e−8. The matched direct interval is narrower, and the endpoint change resolves a small decrease in the magnitude of the error. The inputs include anchor moments through order 66 and a new model of the complete source on the wide collar. [Review04](../reviews/04_AGC_JH_SLAB_ASSESSMENT_20261119.md) describes shared premises and the replay. [B05 r1](../research-progress/handoffs/AGC_JH_B05_REQUEST_R1_20261119.md) asks if a finite degree increment can reduce the source information needed.

**First manuscript, 20 November 2026.** The [working draft](../manuscript/README.md) develops the fixed source, integer hierarchy, finite-step comparison, signed allowance and parity obstruction in order. Its final section sets out the outstanding analytical challenges. [Assessment05](../reviews/05_AGC_JH_FIRST_MANUSCRIPT_ASSESSMENT_20261120.md).
