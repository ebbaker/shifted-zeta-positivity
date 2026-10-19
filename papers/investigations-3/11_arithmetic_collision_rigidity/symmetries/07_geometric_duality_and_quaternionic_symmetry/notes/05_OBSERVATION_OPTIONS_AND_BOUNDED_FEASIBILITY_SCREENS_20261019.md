# S07 continuation options: earlier proposals and two additional screens

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, actual
reasoning effort **ultra**, verified from this turn's metadata. Internal
assessment with delegated same-model analysis/review; no specialist human
review. The two scoped inequalities below are proved here; the remaining
options are proposals, not new estimating results.

## Answer and decision

The alternatives were already listed in the [18 October assessment][old],
but most were not executed. S07-T1 established the finite jet space and
source/error contract; S07-T2 tested one particular whole-profile norm.
It did not test every signed observation, finite-kernel or adjoint method.
The preceding recommendation to leave T3 Waiting concerns its missing
useful input, not exhaustion of the S07 options.

This additional bounded assessment finds two inexpensive reasons not to
retune the failed estimate: changing the cutoff cannot rescue the same
norm/Cauchy rule, and projecting first still fails if the complement is
paid with that same norm. The first screen extends Note 04's exclusion
to a stated family of cutoffs; it does not retroactively enlarge that
note's original claim.

For a new analytic attempt, prioritize a short **complete signed-residual
representation audit** using the existing corrected S03 residual. For
practical geometric certification, the better-established alternative is
**GEO-T1 boundary winding**, once an actual consumer bottleneck is selected.
Neither alternative presently supplies a new advantage. **S07-T3 remains
Waiting; T4 Deferred; no new task IDs or automatic activation.** The earlier
bounded T1/T2 deliverables remain Complete.

Read the [result summaries][summaries] and [patterns to avoid][avoid],
especially [collision controls][controls], [theta bookkeeping][theta],
[geometric results][geometry], [target reformulations][a01], [scope][a07]
and [separate-bound losses][a12]. The new screens compare assigned
allowances, never actual-error lower bounds or physical signs.

## What was proposed, and what was actually done

| Option | Earlier coverage | Present disposition |
| --- | --- | --- |
| Whole-profile norm then Cauchy | Paid on N=2 in [Note 04][paid] | Closed as a loss to direct tails |
| Move or narrow the profile cutoff | Explicitly outside Note 04's original exclusion | Same-X rule now fails for every admissible cutoff preserving the N=2 samples; proof below |
| Finite V4 projection plus complement | Gram/kernel algebra in [Note 03][space]; useful physical complement estimate was not executed | The separate triangle variant with the old X complement now fails; a changed complement or signed estimate remains open |
| Sampling-adapted or mixed signed observation | Proposed in the earlier assessment; polarized Green identity/global dual test exist | Elementary sampling recovers direct tails; a useful residual-adjoint construction remains unproved |
| Physical boundary winding | Theorem and full-theta pilot exist in [Investigation 22][winding] | GEO-T1 matched bottleneck comparison still unexecuted; no demonstrated general cost advantage |
| Different form degree | Natural quaternionic curvature projection screened in the earlier assessment | A distinct ordinary operator/source-containing subspace has not been selected or paid; retain low priority |

## Cutoff retuning: an omitted integer forces a norm floor

Keep the original marked tube, B, physical measure and X from Notes 03/04:

\[
 Y(f)=\int(1+y^2)(|f|^2+|f_y|^2)dy,\qquad
 X(g)^2=\int_1^4\frac{dq}{4q}\int_{-1/4}^{1/4}[4Y(g)+Y(g_p)]dp.
\]

Allow any smooth cutoff, even p/q dependent, provided its residual belongs
to X and the physical N=2 samples are unchanged. In particular
\(g(0,q,\pm3)=a_q(3)\), where a_q is Note 04's source profile.
For the two disjoint unit intervals centered at ±3, elementary sampling
and the minimum weight give

\[
 Y(g(0,q))\ge\frac{29}{4}a_q(3)^2.
\]

Indeed each point square is at most twice the unweighted H1 integral
on its interval, and 1+y^2>=29/4 there. Note 03's Hilbert-valued base
trace gives Y(g(0,q))<=integral_p[4Y(g)+Y(g_p)]. Since a_q(3) decreases
on q>=1, restriction to q in [1,65/64] proves

\[
 X(g)^2\ge X_{cut}^2:=\frac{29}{16}\log(65/64)a_{65/64}(3)^2. \tag{1}
\]

Using the same physical weight-norm floors as Note 04, the unchanged
sqrt(20)X/Cauchy payments exceed

\[
 G_0>8.26666\,10^{-11},\qquad G_1>1.65170\,10^{-11}.
\]

The direct complete tail allowances remain <8.07803e-12 and <7.65021e-14,
so the ratios exceed **10.23** and **215.9**, respectively. These are
floors for the assigned rule, not actual errors. The screen permits any
cutoff satisfying the stated sample/domain conditions; it does not cover
a new observation norm or constant.

Narrowing the transition cannot evade (1). If g is zero at |y|=3-eps
and equals a_q(3) at |y|=3, 0<eps<=1, Cauchy on both transition intervals
also gives

\[
 Y(g(0,q))\ge
 \frac{2\{1+(3-\epsilon)^2\}}{\epsilon}a_q(3)^2. \tag{2}
\]

Moving the transition removes early annular mass but forces derivative
cost. A cutoff-width sweep under this unchanged rule is not warranted.

## Finite projection: the old complement payment keeps the annulus

Return to the original chi2 and write g=exp(pi p^2q)h_q,
\(h_q=a_q\rho\). Let b_j be Note 03's orthonormal profiles, Pi=Pi4.
Odd coefficients vanish. Let M_k be the Gaussian moment upper bounds
from Note 04, equation (5). The even coefficient bounds are

\[
 |\langle h,b_0\rangle|\le C_0=2\,2^{1/4}\pi^2 M_4,
\]
\[
 |\langle h,b_2\rangle|\le C_2=2\,2^{1/4}\pi^2(4\pi/\sqrt2)M_6,
 \quad
 |\langle h,b_4\rangle|\le C_4=2\,2^{1/4}\pi^2(16\pi^2/\sqrt{24})M_8.
 \tag{3}
\]

These follow from rho<=1, a_q<=pi^2 q^(9/4)y^4 exp(-pi q y^2),
|P2|<=4pi qy^2 and |P4|<=16pi^2q^2y^4 on |y|>=2. The relevant
q powers times exp(-2pi qy^2) decrease for q>=1, so (3) is uniform.

On the earlier witness Q=17/16, alpha=9/4<=|y|<=b=5/2, put
F=2^(1/4)Q^(1/4)exp(-pi alpha^2). Then

\[
 |\Pi h|\le B_*:=F\{C_0+(4\pi Qb^2/\sqrt2)C_2
                      +(16\pi^2Q^2b^4/\sqrt{24})C_4\}<2.30508\,10^{-11}.
\]

Meanwhile \(h\ge m=a_Q(b)/(1+e^{8/3})>2.31894\,10^{-8}\). Thus

\[
 X((1-\Pi)g)\ge\sqrt{(97/64)\log Q}\,(m-B_*)>7.02228\,10^{-9}. \tag{4}
\]

The complement's same-X payments alone exceed direct by **>1617** and
**>34118**. Adding any nonnegative projected-sector allowance cannot
rescue this separate triangle estimate. This does not exclude a changed
complement norm, observation-specific representer or signed recombination.

For example, the exact projected sampling kernel is
\(K(q,y)=\sum_{j=0,2,4}b_j(y;q)\sum_n b_j(n;q)\).
Here Lh=sum_n h(n). At p=0, L(Pi h)=integral hK, while
L((1-Pi)h)=2 sum_(n>=3)a_q(n)-integral hK. Keeping both terms signed
recombines to the original lattice sum. This identity alone gives no
new estimate and must not be counted as a gain.

## Options that remain substantive

A sampling seminorm such as
\(\int_1^4e^{u^2/5}u^j\sum_n|g(0,q,n)|dq/(4q)\)
removes the off-lattice tax. For this positive N=2 residual it is the
direct arithmetic-tail payment before envelope relaxation. It repairs
the mismatch but supplies no new arithmetic information. The raw N=2
error is also enormous in the high-height physical normalization. Do not
make this residual the default target of another large S07 computation.

The next analytic representation audit should instead freeze the actual
corrected residual

\[
 r=H/A-(G_8-\widehat C_8)/A
\]

on B. It must identify a natural ambient/sampled realization containing
this same residual, with every normalizer derivative, RS edge, boundary,
cutoff and tail term paid. Note 03 expressly supplies no such lift. A
physical adjoint for the already known annihilator merely returns
\(I_r=i[Z_r(t,x)-Z_r(t,999)]\), the existing S03 primitive.

Before a numerical campaign, require (i) a complete exact representation,
(ii) an independently computable quantitative gain beyond restating that
primitive or direct sampling,
and (iii) a justified source/error class. Stop if the construction needs
an unproved trace/lift or repeats the specific split-prefix or separate-
channel absolute-variation payment rules excluded below. S03 records losses >1.912087
for split source/approximation prefixes and >4037.45136 for one cell's
absolute shifted-channel variation.

If the representation gate passes, declare the information class and
compare a complete allowance with [S03 Note 07][s03-7]: independent
arithmetic <0.000854, or strongest source-informed <0.000266448. They are
not interchangeable benchmarks. A different cost/coverage objective needs
a separate matched contract. No new such input has been established here.

For a practical geometric route, GEO-T1 already has an observation-compatible
winding theorem and full-theta pilot. Select one real consumer bottleneck,
freeze common source/acquisition/accuracy budgets, and compare whole-boundary
winding with optimized interior certification, retaining both walls,
time faces, tangencies and errors. Repeating the old [0.01,0.2]x[25,45]
pilot supplies regression evidence, not a new milestone. Different kinds
of boundary and interior evaluator calls are not equivalent cost units.

## Verification and scope

The [new checker][code] and [192/256 records][record] outward-evaluate
(1), (3), (4) and the comparison constants. The proofs above supply their
continuous scope; checks do not turn proposals into theorems. The
[separate internal review][review] checks the deductions and the distinction
between prior proposals, executed results and still-unexecuted alternatives.
[Fresh source-specific regression controls][screen] retain five event-box
rejections and the separate Euler signed-witness rejection at unchanged
interfaces. There is no new strict physical acceptance rule. The source
premise distinctions remain those of Note 04; these upper-error screens
alone need not reject a colliding source.

No useful new physical estimate, sign, cost gain or coverage is claimed.
The two screens extend only the stated failed-payment classes. T3 stays
Waiting until a genuinely useful estimate or signed input is obtained.

[old]: ../../research-overview/02_S07_MISSING_ESTIMATES_AND_ALTERNATIVE_APPROACHES_20261018.md
[space]: 03_CONSTRAINED_THETA_JET_SPACE_AND_RESIDUAL_CONTRACT_20261019.md
[paid]: 04_PAID_PROFILE_TRACE_AND_DIRECT_TAIL_COMPARISON_20261019.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[geometry]: ../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[s03-7]: ../../03_normalized_jet_rotation/notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md
[winding]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[code]: ../numerics/screen_observation_options.py
[record]: ../numerics/S07_OPTIONS_192_20261019.json
[screen]: ../numerics/S07_OPTIONS_SOURCE_CONTROLS_20261019.json
[review]: ../reviews/05_OBSERVATION_OPTIONS_INTERNAL_REVIEW_20261019.md
