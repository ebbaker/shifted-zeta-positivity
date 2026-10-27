# Three regime heat flow dynamics research overview

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

## Objective

Determine which features of the canonical heat flow depend on the Newman
threshold and endpoint multiplicities, then seek estimates of those
features from the complete theta source. Compare actual solution behavior
before selecting an exclusion inequality. A useful first result could
quantify a response, constrain a multiplicity population, or bound the
location of nonreal zeros without settling RH or simplicity.

This is a new investigation with a fresh [TRD progress register][progress].
Its founding comparison is [the three-regime brainstorm in 03][founding].
The existing approximation, application and collision-bound tasks keep
their original owners. In particular, the narrower acquisition work in 03
does not establish that the positive-threshold approaches in 02 are weaker.

The [result index][results] and [avoid index][avoid] apply throughout.
Relevant inputs are [heat-flow results][heat], [local geometry][geometry]
and [collision controls][controls]. Classify every proposed implication
under [target versus milestone][classification], screen its actual premises
under [control screening][screen], and preserve [scoped conclusions][scope].

## One canonical solution and three hypotheses

Use the repository normalization

\[
\partial_tH=-\partial_z^2H,\qquad
H(0,z)=\frac18\xi\!\left(\frac{1+iz}{2}\right).
\]

The hypotheses concern this same solution and its unchanged source. They
do not specify three freely chosen initial-value problems. With the known
nonnegativity of the Newman constant, the following cases are exhaustive.

| Regime | At time zero | Near the relevant endpoint | Main quantitative question |
| --- | --- | --- | --- |
| A: \(\Lambda=T>0\) | Some zeros are nonreal | The canonical positive-threshold reduction supplies a finite real multiple event at T; above T the zeros are real and simple | Which constraint on the actual solution can exclude or bound a positive T? |
| B: \(\Lambda=0\), some multiple zeros | All zeros are real, with at least one multiple site | A multiple site splits on the square-root time scale, with nonreal descendants just before zero | How do sparse events and positive populations affect observable responses? |
| C: \(\Lambda=0\), all zeros simple | All zeros are real and simple | Every fixed compact region remains free of nonreal zeros for sufficiently small negative time; nonreal zeros still occur elsewhere | How does the necessary observation region grow as negative time approaches zero? |

The finite-event assertion in A uses the canonical uniform exterior input
in [02's positive-threshold analysis][threshold]; it is not a theorem for
every heat flow. Near T the source is \(e^{Tu^2}\Phi(u)\), so a time shift
must retain that changed source. In C, compact stability gives no uniform
lower gap and no escape rate. These are inherited facts, not new outputs
of this investigation.

## Compare time and height together

The long-term objective covers all real times and all heights through
compatible estimates on declared regions. Each comparison must state time,
height, transverse width, regulator and averaging width together.

| Region | Existing information | What remains to compare |
| --- | --- | --- |
| Negative times bounded away from zero | Canonical negative-time formulas and nonreal-zero existence | Distribution, transverse displacement and matching to the near-zero region |
| \(t\to0^-\) in a fixed bounded region | Distinct local signatures for A, B and C | Effective errors and the resolution required to observe them |
| \(t\to0\), height increasing | The fixed-window and large-height limits need not commute | Small-gap populations, multiplicity statistics and nonreal-zero locations |
| \(t\to T\) under A | Local Hermite splitting at a finite event | Constraints using the complete shifted source and exterior interactions |
| Fixed positive time at large height | Eventual real and simple high zeros are already unconditional | Time-dependent onset and exceptional regions; a common leading term is not a discriminator |
| Large positive or large negative time | 01 supplies useful asymptotic models | Matching and conditional subleading terms, rather than assuming distinct leading profiles |

Use the [Book's canonical atlas][canonical] for the actual domains and
normalizations. In joint limits record both \(|t|\log X\) and
\(|t|(\log X)^2\) when relevant; they are different scales. The Book's
prescribed regulator switch times are not Newman thresholds.

## First observables and their resolution

For a fixed nonnegative smooth compact cutoff \(\chi\), count zeros with
multiplicity and set

\[
Y_\chi(\tau)=\sum_{H(-\tau,z)=0}\chi(z)(\Im z)^2,
\qquad \tau>0.
\]

The inherited local expansion gives, in either RH regime,

\[
Y_\chi(\tau)
=2\tau\sum_{H(0,a)=0}\chi(a)m_a(m_a-1)+o(\tau).
\tag{1}
\]

In A, a cutoff seeing an off-axis time-zero zero has a positive limiting
moment. In B, a cutoff positive at a multiple site has a positive linear
coefficient. In C, each fixed cutoff eventually has exactly zero moment.
These statements concern the zero measure before regularization. They
provide a conditional comparison, not an independently estimated
contradiction.

For buffered finite windows write
\(N_X=\sum m_a\) and \(M_X=\sum m_a(m_a-1)\). The ratio \(M_X/N_X\)
is a natural population statistic. A positive fraction of zero labels
belonging to multiple sites forces a positive ratio. A finite exceptional
set disappears under this normalization, although its local moment remains
detectable. Unbounded multiplicities require the weighted statistic;
the fraction of distinct zero sites alone does not suffice.

Equation (1) fixes the window first. Extending it to \(X=X(\tau)\)
requires quantitative control of near collisions as well as exact
multiplicities. The exact control

\[
F(t,z)=z^2-a^2-2t,\qquad
Y(\tau)=4(\tau-a^2/2)_+
\tag{2}
\]

has simple zeros at zero but resembles a double endpoint when
\(a^2\ll\tau\). Its negative threshold makes it a resolution calibration,
not a canonical example of C. The [universal local-profile result][profile]
and [all-multiple coarse-count control][allmultiple] also rule out using a
shared leading profile or one-point counting law alone as the separator.

In C a second observable is

\[
R_*(\tau)=\inf\{|z|:H(-\tau,z)=0,\ \Im z\ne0\}.
\tag{3}
\]

Compact stability implies \(R_*(\tau)\to\infty\), without a rate or
monotonicity. In A and B a fixed compact region contains nonreal zeros
for all sufficiently small \(\tau\). Equation (3) uses complex radius;
a statement about horizontal height needs transverse control. Constructing
a very high nonreal zero gives an upper bound for this infimum, not a
lower bound excluding lower zeros.

## Use the exact observable equations

01's [physical system][physical] retains potential U, density R, current J
and the actual signed covariance Q. In the auxiliary constant-regulator,
fixed-filter case the equations include

\[
U_t=-\tfrac12\bigl[(\partial_x^2-\partial_y^2)U
 +U_x^2-U_y^2+Q\bigr],\quad
\Delta U=4\pi R,\quad R_t+\operatorname{div}J=0.
\]

The original adaptive regulator adds the documented correction terms.
Retain those terms, the mean product and Q; choosing a convenient closure
for Q would change the problem. The original fixed resolution can suppress
endpoint information even when its global approximation is accurate.

Define auxiliary diagnostics separately. For constant nonzero normalization
A and constant \(\eta>0\), a useful weak potential expression is

\[
Y_{\chi,\eta}(\tau)=\frac1{4\pi}\int_{\mathbb C}
 \log\bigl(|H(-\tau,z)/A|^2+\eta^2\bigr)
 \Delta\bigl[\chi(z)(\Im z)^2\bigr]\,dA(z).
\tag{4}
\]

At fixed \(\tau\), regulator removal recovers \(Y_\chi\). A normalized
field error \(\delta\) contributes at most

\[
\frac{\|\Delta(\chi y^2)\|_1}{4\pi}\frac{\delta}{\eta}.
\tag{5}
\]

Resolving (1) by this transfer requires \(\delta/\eta=o(\tau)\)
and a separately controlled regulator bias. Moving tests change derivative
norms; moving filters add commutators. The first task is to quantify these
costs together with multiplicity, small gaps and boundary flux. Existing
fixed-slab weak estimates in [Summary76][summary76] are inputs, not a
near-zero uniform regulator-removal theorem.

## Functional approximation as a second main approach

[Dobner's paper][dobner] supplies a complementary route through an
approximating function and contour zero transport. The checked formulas,
normalization and initial parameter analysis are in the
[source record][dobnerrecord]. Its nonnegativity conclusion is shared by
all three regimes; the new objective is quantitative information that
changes the comparison above.

Start with the sharper error expression before its final simplification.
Track the location of a seed zero, its contour floor, the allowed
translation heights and the change of coordinates simultaneously as
\(t\uparrow0\). Compare those demands with 01's retained-source formulas
on genuinely overlapping domains. A better approximation error alone need
not improve a witness height if the contour floor or recurrence cost
dominates.

For A, also ask which consequences of a positive threshold can be imposed
on a functional approximation to the actual shifted source. Do not apply
a theorem for an ordinary completed Dirichlet series to a positive-time
deformation without proving that its hypotheses survive. A simple shift
of the known nonnegativity argument does not exclude a positive threshold.

## Research sequence and meaningful gains

1. **Build the conditional atlas.** State compatible models for the three
   hypotheses, with all scales and inherited assumptions explicit.
2. **Quantify a response on specified windows.** Start with (1), (2) and
   (4), then derive a uniform remainder or identify the precise obstruction
   to growing windows. Separate positive populations from sparse events.
3. **Audit the functional approximation budget.** Obtain a complete
   conditional witness-height formula, including seed and recurrence data,
   and compare the sharper published error with the Book's estimates.
4. **Match the actual equations and source.** Seek a coefficient, rate,
   support restriction or fluctuation estimate that one regime requires
   and the complete canonical solution constrains independently.

The first two quantitative tasks are response resolution and the functional
approximation budget. They can inform each other without either being
reduced to 03's P/J endpoint tests. Later estimates may feed P/J/V/E,
Rodgers–Tao comparisons, or a specified Newman upper-bound improvement.

A meaningful advance must improve a stated bound or establish a new
uniformity range. An RH-equivalent reformulation is classified once;
numerical agreement with it is not progress toward its proof. For every
candidate record the complete error, baseline, applicable controls and
the quantity actually improved. A negative outcome is reported only for
the tested observable and scale.

## Required control comparisons

The opening screen reuses the recorded analytic controls; no new control
certificate is asserted. It identifies why generic hypotheses cannot
already select the canonical regime.

| Control | What it tests | Premise it does not supply |
| --- | --- | --- |
| Hermite and quadratic heat fields | Universal local splitting and unresolved simple pairs | Complete canonical theta source and global zero statistics |
| Positive atomic and theta-close multiple-endpoint sources | Positivity, normalization and local profiles can coexist with collisions | Unchanged ordinary theta Dirichlet arithmetic; the precise preservation lists differ |
| Euler-factor controls | Positive thresholds can survive substantial analytic structure | Original coefficients and completion; each parameter's all-real premise must be checked |
| Weighted-square and finite-tail controls | Local collisions and finite source measurements | The all-real interval needed for the RH population comparison |
| Reflected, shape, positive-primitive, finite-prime and finite-profile controls | Their named structural data do not by themselves exclude events | The full unchanged normalized source; missing premises differ between families |
| All-multiple coarse-count control | Even pervasive multiplicity can pass coarse count and wall estimates | Canonical arithmetic; a proposed stronger derived bound still needs an actual test |

Full theta arithmetic is an input, not an already acquired favorable
inequality. Preserve cancellations and coupled estimates as required by
[the separate-bounds warning][coupled].

[progress]: ../research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md
[founding]: ../../03_heat_flow_collision_bounds/brainstorm/02_THREE_REGIME_DYNAMICS_AND_COMPARATIVE_ASYMPTOTICS_20261026.md
[threshold]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[canonical]: ../../01_heat_density_asymptotics/book/sections/01_canonical.tex
[physical]: ../../01_heat_density_asymptotics/book/sections/05_physical.tex
[summary76]: ../../01_heat_density_asymptotics/notes/76_CHAT0028_RESEARCH_SUMMARY_20261026.md
[profile]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[allmultiple]: ../../../investigations-4/12_height_dependent_heat_contours/brainstorm/notes/18_RH_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_THEOREM_20261023.md
[dobner]: https://arxiv.org/abs/2005.05142v2
[dobnerrecord]: ../references/01_DOBNER_FUNCTIONAL_APPROXIMATION_20261026.md
[results]: ../../../../result-summaries/README.md
[heat]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[classification]: ../../../../avoid/01_restating_the_target.md
[screen]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[coupled]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
