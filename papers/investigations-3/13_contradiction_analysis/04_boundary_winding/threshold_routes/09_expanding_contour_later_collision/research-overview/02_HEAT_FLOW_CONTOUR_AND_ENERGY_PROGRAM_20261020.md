# Bounded program for heat flow contours and Gaussian cap energy

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**, actual reasoning
effort **ultra**, verified from the parent turn metadata.

**Original handoff status: prepared; quantitative execution had not started.**
**Execution update, 20 October 2026:** one bounded round is now complete;
[Note 07](../notes/07_FIXED_GAUSSIAN_COMPARISON_20261020.md) records direct
exclusion and the failed matched Gaussian estimator, and
[Note 08](../notes/08_LOCALIZED_COMPARATOR_AND_LEVEL_CONTROL_20261020.md)
records the positive localized comparator and exact level-arc controls.
The matching progress register holds current measurements and task status.
The remainder of this overview preserves the original estimating contracts
and their at-handoff availability statements. This program
turns the alternatives in [Notes 05][n5] and [06][n6] into bounded estimate
requests. Its first priority is one fixed-scale Gaussian cap deficit,
compared with the strongest same-data direct first-jet consumer. The
requested outcome is a measured strict margin, a measured cost advantage,
or a precise failure of the selected estimate. Preparing this program is
not a new theta result.

The [original BW09 register][bw09] remains authoritative for BW09-00–06,
the later-collision target, and overall coverage. The [matching HFCE
register][progress] governs only HFCE-00–07 below. Direct Gaussian event
exclusion, later negative Laguerre expression, and extra winding have
different conclusions and must retain separate measurements. The original
[expanding-contour overview][original] remains in force where applicable.

Read the [result index][results], [collision controls][controls], and
[avoid index][avoid], particularly [reformulations][a01], [own-control
screening][a02], [scoped conclusions][a07], [question before numerics][a10],
[signed recombination][a12], and [measured gain before expansion][a20].
The existing derivations have separate same-model internal mathematical
reviews; there is no specialist or independent-implementation review.

## 1. Inherited facts and the unresolved parameter window

Use the unchanged complete source
\[
 H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
 \qquad H_t=-H_{xx},\qquad J=H+iH_x.
\]
The inherited BW09 ordinary-event class is
\[
 0<T=\Lambda\le1/5,\quad a\in[1001,1002],\quad
 H(T,a)=H_x(T,a)=0,\quad h_2\ne0.
\]
No event is observed, no nonempty event set is asserted, and no uniform
positive curvature floor is supplied. [Note 04][n4] already excludes all
multiplicities throughout
\[
 B_{\rm excluded}=[0.099999,0.100001]\times[1001,1002].
\]
The inherited coverage ledger also has applicable exclusions, including
its height edge at 1001 in its stated time range. **The first surviving
closed numerical window is not yet selected.** HFCE-01 must choose one
rational closed rectangle \(B=I_T\times I_a\) inside the parent parameter
range after checking the complete current coverage ledger. Removing a
known exclusion does not prove that a remaining point is an event.

The Gaussian test requires only \(h_0=h_1=0\), so a strict negative result
would exclude every multiple zero in its certified window, whether or not
it is an ordinary threshold event. The nonzero-level contour requires
an isolated ordinary event, \(h_2\ne0\), and additional continuation
premises. Do not transfer one contract's hypotheses to the other.

The inherited facts are reusable inputs, not new HFCE execution:

* The physical degree is \(-q_0-K_{\rm later}\), where
  \(q_0=\lfloor m_0/2\rfloor\); the ordinary-event regularization has
  degree \(-K_{\rm later}\).
* Unsigned disks centered at 1 cannot force negative regularized degree
  in the precisely stated information class of [Note 01][n1].
* Root walls remove wall phase, but their cap count still supplies the
  missing information. A collision exactly on a contour makes physical
  winding undefined; its enclosing connector or regularization must be paid.
* A nonzero \(H/h_2\) level arc makes its phase endpoint-determined.
* The Gaussian deficit and localized Laguerre identities below are proved
  and reviewed in-note. No fixed-scale theta deficit, negative localized
  average, or signed theta winding margin has been acquired.

## 2. Primary contract: one fixed Gaussian cap

Before acquisition, freeze one \(s_0>0\), the entire window \(B\), a fixed
positive normalization \(A_*>0\), the cap integration or source-kernel
method, cutoffs, precision, allowed subdivisions, and a whole-run budget.
Pin the actual source and consumer versions, including uncommitted inputs.
The scale may depend on the declared window when the contract is written;
it may not be selected afterwards merely to avoid a zero. Physical
functions are normalized by the fixed \(A_*\), which is not differentiated.
Every cap time lies in \(I_T+s_0\); inherited first-jet caches do not cover
this range or its spatial integration interval without explicit validation.

Set
\[
 G_s(y)=(4\pi s)^{-1/2}e^{-y^2/(4s)},\qquad
 D_s(T,a)=s\int G_sH_x(T+s,a+y)^2\,dy
                  -\int G_sH(T+s,a+y)^2\,dy.
\]
The reviewed Hermite identity is
\[
 D_s=-h_0^2-sh_1^2+
 \sum_{n\ge3}\frac{n-2}{2}\frac{(2s)^n}{n!}h_n^2.
\]
Thus a complete uniform bound \(D_{s_0}/A_*^2\le-\delta<0\) on
\(B\) proves \((h_0^2+s_0h_1^2)/A_*^2\ge\delta\) there. This is
**direct event exclusion**, not a later-collision certificate.
The exact identity is available for every admissible source; theta's
unchanged complete coefficients must supply the distinguishing estimate.

The ability to choose an unspecified sufficiently small \(s\) is only a
reformulation of first-jet nonvanishing. It is not an acceptance criterion.
At an event \(D_s\ge0\); equality is quadratic, while a nonzero bounded
theta cap would have \(D_s>0\), without a supplied uniform margin.

### Complete error contract

There are two legitimate implementations. Select one before acquisition;
use the other only as a declared comparator or a separately recorded retry.

**Cap integration.** On a finite interval \(|y|\le L\), obtain complete
approximants \(P_0,P_1\) to \(H,H_x\), with whole-parameter error bounds
\(\varepsilon_0,\varepsilon_1\). The squared-function payment includes
\[
 \int_{-L}^{L}G_s\!
 \left[s(2|P_1|\varepsilon_1+\varepsilon_1^2)
       +2|P_0|\varepsilon_0+\varepsilon_0^2\right]dy.
\]
Pay retained quadrature and arithmetic separately. With uniform complete
source moment bounds \(M_j\ge\sup_{I_T+s_0,x}|\partial_x^jH|\), the
omitted spatial part is bounded by
\[
 (s_0M_1^2+M_0^2)\operatorname{erfc}\!
       \left(\frac{L}{2\sqrt{s_0}}\right).
\]
This crude global bound may overwhelm the small high-height signal;
assess its numerical size before acquiring a cap grid. Any sharper tail
must have a proof. The physical estimator needs orders 0 and 1;
interpolation may require higher derivatives, whose actual orders and
complete tail payments must be declared.

**Signed two-source kernel.** With \(w=e^{(T+s_0)u^2}\Phi(u)\), retain
\[
 \frac12\iint w(u)w(v)\left[
 (s_0uv-1)e^{-s_0(u-v)^2}\cos(a(u-v))
 -(s_0uv+1)e^{-s_0(u+v)^2}\cos(a(u+v))\right]du\,dv.
\]
The two terms and parameter correlations must survive the estimate.
A mode/spatial truncation in either variable requires the entire omitted
pair region, without omitting or double-counting the overlap. For a
nonnegative retained source with moments \(m_j\), omitted-source moments
\(r_j\), and the crude kernel bound \(|K|\le1+s_0uv\), one valid pair-tail
payment is
\[
 2m_0r_0+r_0^2+s_0(2m_1r_1+r_1^2).
\]
It covers source truncation only; quadrature, arithmetic, propagated
coefficient errors, and all \(T,a\) uncertainty remain separate payments.
The bound's usefulness must be measured, not presumed.

### Same-data baseline and measurements

First check whether an available complete direct first-jet bound already
excludes \(B\). If so, record the exclusion under its existing source and
do not call its repetition new coverage. A separately declared cost
comparison can still be informative.

From the same complete cap/source data, use both direct Gaussian moments
\(h_j=\int G_{s_0}\partial_y^jH(T+s_0,a+y)dy\), \(j=0,1\), and every
stronger applicable direct first-jet consumer. Preserve correlations when
they improve the baseline; do not weaken it to manufacture a gain.
Let \(L_{\rm direct}\) be its strongest certified lower bound for
\((h_0^2+s_0h_1^2)/A_*^2\). If the deficit estimator returns a complete
upper bound \(U_D\), record
\[
 L_D=\max(0,-U_D),\qquad G_E=L_D-L_{\rm direct},\qquad
 \delta_D=-U_D.
\]
Only \(\delta_D>0\) certifies the desired strict exclusion. Report the
raw deficit interval, every error component, event coverage, source
acquisition cost and consumer cost; no winding units are assigned to
this scalar comparison. Unavailable quantities remain unavailable.

## 3. Secondary bounded comparisons

**Localized BW-05 functional.** Freeze a nonnegative compact \(C^2\)
weight and a separated later-time window, or one later cap. The target is
\[
 A_\psi=\int\psi(H_x^2-HH_{xx})
       =2\int\psi H_x^2-\frac12\int\psi''H^2<0.
\]
Its support must extend beyond the established local region where the
Laguerre form is positive. Whole-line unweighted integration and weights
with everywhere nonnegative cosine transform cannot supply the desired
sign. Pay product and weight-derivative errors and all parameter
uncertainty. Compare with the strongest same-data pointwise BW-05
consumer; if it needs \(H_{xx}\), report the cost of obtaining that
component rather than assuming it free or unavailable. This conclusion
is later nonrealness, distinct from a forced later real collision.

**Nonzero level contour.** Freeze an actual connected arc
\(H/h_2=e>0\), a cap, and an isolating event contract. Prove continuation,
exactly two intended cap endpoints, a Jordan curve, no boundary collision,
and the complete initial-event accounting. If the cap has \(N\) simple
interior zeros, its physical degree is \(-N/2\). The curved side is paid
by endpoint phases; its separation \(|h_2|e\) is event-dependent.
For an ordinary initial event and no other earlier event, extra collision
requires \(N\ge4\). The usual \(N=2\) is consistent. Failure of the
level graph when \(H_{xx}=0\) does not prove a collision. A numerical
curvature floor, if needed, restricts coverage and must be stated.
Compare total acquisition and complete-contour cost with the existing
parabolic and root-wall consumers on the same data. A cheaper curve
can be useful without being called a new theta sign.

**Zero-interaction energy.** Keep this deferred. Activation requires a
specific finite root set or an explicitly renormalized theta system,
paid exterior interactions and moving-cutoff terms, a declared reference
configuration, and an independently estimable arithmetic quantity in
conflict with the resulting inequality. The finite identity
\(U'=-2|\nabla U|^2\) assumes a complete simple real-root polynomial
system. It cannot be applied to one pair while discarding other real or
complex roots. Rodgers–Tao's lower-bound direction does not supply the
upper bound sought here. Generic forward repulsion alone is not an
activation condition.

## 4. Tasks, gates, and stopping decisions

| ID | Bounded task | Entry and completion gate |
| --- | --- | --- |
| HFCE-00 | Record program, register and inherited provenance | Prepared by these documents; no new estimate. |
| HFCE-01 | Select one surviving window and freeze one scale/method | Check current coverage; write complete parameter, tail, error, work-budget and baseline contract before acquisition. |
| HFCE-02 | Implement the chosen finite consumer and own controls | HFCE-01 fixed; replay exact quadratic/cubic and positive-source controls, interval products, tails and refusals; retain a small auditable receipt. |
| HFCE-03 | Acquire one complete theta deficit and matched first-jet comparison | HFCE-02 checked; one declared window, no automatic expansion; record strict margin or the complete remaining deficit. |
| HFCE-04 | Test one fixed localized BW-05 functional as a comparator | Separate frozen weight/window and budget; activate only after the primary assessment or a concrete reason this consumer has cheaper applicable data. |
| HFCE-05 | Test one actual nonzero-level contour consumer | Paid isolation/continuation contract and cap data; measure full-boundary cost or sign against the strongest applicable same-data contour baseline. |
| HFCE-06 | Review the bounded round and make a continuation decision | Assess whichever frozen consumer was executed; update both registers without changing unexecuted tasks to completed. |
| HFCE-07 | Root-interaction energy | Deferred until the explicit hypotheses and new arithmetic statistic above are supplied. |

Stop the selected numerical attempt if its error budget cannot resolve
the predeclared margin at the permitted cost, if its input window is
already excluded, or if its claimed new premise is only a target
reformulation. Record the reason and the paid deficit. A changed scale,
window, tail method or statistic is a new contract, not an invisible
adaptive repair. A positive deficit value is not evidence for a collision.

Broader height/time coverage and infinite-cap work remain governed by
BW09-05–06 and the existing coverage ledger. A Gaussian strict exclusion
already excludes all multiplicities in its own window, but does not
supply global coverage or extend an ordinary-event level-curve proof.
This handoff records no new numerical acquisition; execution begins with
HFCE-01's concrete question.

## 5. Required own-control screen

| Control | Required outcome and distinguishing premise |
| --- | --- |
| Quadratic \(H=h_2(y^2/2-\tau)\), both signs | \(D_s=0\); no strict Gaussian exclusion, no later event. Rounded root triangle has physical degree \(-1\), regularized degree zero. |
| Cubic matching arbitrary \(h_2\ne0,h_3\) | \(D_s=2h_3^2s^3/3\ge0\); true all-real threshold and no later event. The prescribed initial jets do not force a negative deficit. |
| Positive atomic \(H=1+e^{t-T_0}\cos x\) at \((T_0,\pi)\) | \(D_s=1+s\sinh(2s)-\cosh(2s)>0\); bounded positive-source actual threshold, no later event. Isolate one of its periodic simultaneous events for contour work. It lacks theta's complete source. |
| Multiplicity-four heat polynomial | Refuse the ordinary \(h_2\ne0\) contour quotient; Gaussian common-zero inequality still applies. Do not count initial index \(-2\) as two later doubles. |
| Two-event quartic | Detect the later event with full index accounting; its first event is not the all-real threshold. |
| Positive atomic/finite-profile threshold families | Apply their own complete-source data. Generic positivity/profile moments cannot supply the contrary sign; do not assign theta error allowances. |
| Euler-factor, weighted-square, finite-prime, reflected and positive-primitive families | Use supplied events and their own moments; name the missing complete-theta, reflection or threshold premise from the catalogue. A threshold lower bound is not an event, and a local event is not automatically an all-real threshold. |

For an actual proposed inequality, perform the applicable own-data
substitution; “not theta” alone is not a deficit calculation. The present
analytic substitutions are inherited screens, not a fresh computational
campaign on every family. Review independence and source versions belong
in each execution receipt. Research goes in `notes/`, small computation
records in `numerics/`, and assessments in `reviews/`; no new snapshot
manuscript folders are created.

[progress]: ../research-progress/02_HEAT_FLOW_CONTOUR_AND_ENERGY_PROGRESS_20261020.md
[bw09]: ../research-progress/01_EXPANDING_CONTOUR_PROGRESS_20261020.md
[original]: 01_EXPANDING_CONTOUR_RESEARCH_PROGRAM_20261020.md
[n1]: ../notes/01_FINITE_CONTOUR_AND_SOURCE_CONTRACT_20261020.md
[n4]: ../notes/04_BOUNDED_THETA_EVENT_GATE_20261020.md
[n5]: ../notes/05_TOPOLOGICAL_ALTERNATIVES_AND_ENERGY_OBSERVATIONS_20261020.md
[n6]: ../notes/06_HEAT_FLOW_CONTOURS_AND_GAUSSIAN_CAP_ENERGY_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
