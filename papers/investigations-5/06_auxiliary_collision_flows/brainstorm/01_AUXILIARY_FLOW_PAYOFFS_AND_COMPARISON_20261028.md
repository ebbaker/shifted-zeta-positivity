# Choosing what an auxiliary collision flow should make controllable

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Conversation: **Discuss auxiliary collision research**, Investigation06
chat0002, thread `01a1859f-de8b-7461-a0ae-740d57d845d2`.

**Status: exploratory discussion with a selected objective.** After the
[continuation note][continuation], the author selected **an independent
estimate that could constrain canonical theta collisions** as the leading
payoff. Diagnostic improvement is a supporting possibility. The mechanisms
below remain proposals for discussion; no preferred flow has been agreed.
The author subsequently requested the [research plan][plan] and
[progress register][progress], which now provide the task sequence and
live status. Candidate evolutions should be assessed by the estimate
they make accessible. Stronger visible splitting alone does not identify
the best candidate.

## 1 What the local response can distinguish

Retain the complete canonical source and the independent auxiliary parameter:
\[
F_q(t,s,z)=\int_0^\infty\Phi(u)e^{tu^2+s q(u)}\cos(zu)\,du,
\qquad F_q(t,0,z)=H(t,z).
\]
At a nondegenerate real double event \((T,a)\), put
\(A=H_{zz}(T,a)\ne0\) and \(R_q=F_{q,s}(T,0,a)\).
The inherited analytic squared gap satisfies
\[
D(t,s)=8\left[(t-T)-\kappa_qs\right]
 +O\!\left((|t-T|+|s|)^2\right),
\qquad \kappa_q=R_q/A.
\]
Thus the first-order effect on this observable is a displacement of the
collision time. A nonzero response supplies a transverse direction to the
local collision curve. It does not yet supply an independent constraint
on the physical slice.

The normalization issue can be seen without an approximation. For real
constants \(\alpha,\beta\), set
\(\widehat q=q+\alpha+\beta u^2\). Wherever the integrals converge,
\[
F_{\widehat q}(t,s,z)
 =e^{\alpha s}F_q(t+\beta s,s,z),
\qquad
\kappa_{\widehat q}=\kappa_q-\beta.
\]
The second identity follows from \(H(T,a)=0\) and
\(\int u^2\Phi(u)e^{Tu^2}\cos(au)\,du=-A\).
Rescaling \(q\) also rescales the auxiliary parameter. Before the time
direction and perturbation budget have been fixed, the raw size of
\(D_s\) is consequently not an intrinsic measure of improvement.
For bounded q the theta tail admits the displayed quadratic modification
for all complex parameters; other sources retain their convergence domain.

This is an elementary comparison drawn from the existing response law,
not an exclusion theorem. It is local to a nondegenerate double event and
its first-order squared-gap behavior. Distinct generators can have different
higher responses, global trajectories, analytic estimates and evaluation
costs. Once a physical path and normalization are fixed, their responses
are meaningful quantities to compare.

## 2 Three different payoffs

| Payoff | What would count as a gain | What must be supplied |
| --- | --- | --- |
| Collision diagnosis | A smaller certified uncertainty in a squared gap or cluster discriminant, or less work for the same uncertainty | A common domain, input accuracy, normalization, truncation allowance and evaluation-cost model |
| Controlled deformation | A proved comparison for how a collision curve, gap or suitable observable moves over a stated parameter range | A law for the chosen evolution and a justified comparison back to s=0 |
| Canonical collision exclusion | An independently proved theta estimate incompatible with the response forced by a hypothetical event | The complete source input, the quantitative separating bound and its actual failure on relevant colliding controls |

These aims can support one another, but they have different success
conditions. A diagnostic should respond on a colliding control. An
exclusion estimate must fail on a control when applied on a domain
containing its witness. A collision-free path in the enlarged parameter
space does not by itself establish that the physical slice is collision-free.

The analytic squared gap or local cluster coefficients remain sensible
diagnostic observables because they continue through coalescence. The
[survey's DY09][survey] provides an established numerical precedent. Continuation
of those observables still requires theta-specific error bounds and
control of the retained cluster; regularity alone is not a cost advantage.

For a route toward exclusion, the extra information may enter through the
initial source, an observable, or an estimate. The generator itself need
not encode the arithmetic. The useful question is which independently
accessible information the evolution makes available to a comparison.

## 3 What each candidate family would contribute

### Bounded source tilts as a comparison family

The cosine tilt gives an explicit, admissible family with an exact
translation representation. Its classical Bessel expansion implies that
the normalized evolution for s>=0 is an average of translated H values
([DLMF 10.35][dlmf]; the application to H is the survey's deduction).
At the matched mark its initial response is the positive integral of
\(\cos^2(au)\) against the heat-weighted source.

This makes it a useful reference calculation for propagation and error
accounting. It leaves a concrete question: can an implementation or
estimate improve on evaluating the relevant original H observations
directly, after paying for translated values and the series tail? Its
positive response also occurs for colliding controls. It has not yet
earned priority as an exclusion mechanism.

### Local differential evolutions

Quartic and more general local terms offer higher-jet responses and may
admit identities absent from the bounded cosine example. Their possible
benefit would be a usable differential inequality, localization estimate
or response bound for the complete source. The inherited quadratic heat
model has zero fourth derivative at its double event, so derivative order
alone does not guarantee a diagnostic response.

Pólya's universal-factor theorem restricts the even entire exponential
multiplier family to amplitude and admissible quadratic heat changes when
preservation is required for every admitted source. This is the consequence
recorded in the survey from [Newman–Wu, Theorem 2][newman-wu]. It leaves
source-specific estimates and other operator families open. A proposed
operator must come with an evolution on a stated analytic domain; a
theorem for one operator does not automatically establish its exponential.

### Coupled interactions as a source of comparison laws

[Hou–Jiang–Newman][hjn] proves disjoint trajectories when one edge coupling
increases in a finite ferromagnetic Ising system whose positive-interaction
graph is connected. Its Curie–Weiss result uses a cooperative zero system.
This suggests examining what relation makes the motion controllable, and
whether a justified theta construction could supply a useful counterpart.

There is an important repository constraint beyond the new survey.
[Result summary 17][stable-models] records scoped obstructions to
independent Bernoulli products, specified quartic constructions and certain
heat-prepared stable models. Those restrictions also affect a known stable
Bessel source, so they limit those constructions rather than decide theta
stability. General interacting infinitesimal arrays remain outside the
recorded exclusions.

An exact representation of \(H(0,z)/H(0,0)\) as a characteristic function
in the Lee–Yang class would already imply RH. It is therefore a major
sufficient target, not a modest
preliminary lemma; no converse or equivalence to RH is asserted here.
Likewise, putting the complete theta source into a single component and
assuming that component is Lee–Yang supplies the missing zero information
as a premise. A smaller exploratory question is whether an explicit
interaction identity yields a useful bounded comparison before such a
global representation is available. No such identity is supplied by this
brainstorm.

## 4 Analytic collision-control screen

The reparameterization identity and local response law use convergence,
the heat equation and double-event nondegeneracy. They also hold for
admitted colliding controls, so neither is proposed as a separating
criterion. The following screen applies the [control register][controls]
and the survey's existing calculations; it is not a new numerical run.

| Control | Shared input for bounded tilts | Missing canonical premise |
| --- | --- | --- |
| Euler-factor controls | Positive source, dominated tilt and the same marked square response | Unchanged canonical Euler factors and coefficients |
| Weighted-square and finite-source controls | Positive continuous source on the admitted domain and the same local event calculation | Complete coefficients or full reflection; their event need not be an all-real threshold |
| Finite-prime-compatible controls | Bounded perturbations and compatibility with selected arithmetic observations | Full reflection and unchanged complete theta coefficients |
| Reflected super-Gaussian controls | Reflection, positive Gram forms and the same bounded response | Canonical square arithmetic |
| Smooth shape and positive-primitive controls | Strong shape or primitive positivity and the same bounded response | Canonical square arithmetic and any actual separating estimate |
| Note38 polynomial-Gaussian control | Strict cosine response at its stated nondegenerate event | Theta tail and canonical arithmetic; positive quartic tilting is outside its domain |
| Survey atomic control | Bounded tilt and strict response on its explicit support | Continuity, theta tail and canonical arithmetic |

For the last control, \((1-p)e^s+pe^{-s}\cos z\), with \(1/2<p<1\),
has its double event at \(z=\pi\),
\(s=\tfrac12\log(p/(1-p))\). Direct differentiation gives
\(F_s=2pe^{-s}>0\) and \(F_{zz}=pe^{-s}>0\) there.
This checks that a positive, finite auxiliary response is compatible with
a collision in that class. [Note38][n38] supplies the continuous Gaussian control.
The absent canonical premises in the table become useful only when an
estimate actually uses them and discriminates the control.

## 5 Selected objective and open mechanisms

**Author decision, 28 October 2026:** lead with an independent estimate
that could constrain canonical theta collisions. The choice of evolution,
observable, domain and first quantitative target remains open.

Independence concerns the proof inputs. An estimate must be derived from
the complete source and established analytic facts without assuming the
noncollision or positive first-jet margin it is intended to establish.
It can be strong enough to imply the desired result; a reformulation
becomes useful when a new argument actually proves its missing estimate.
An event-conditioned calculation is also legitimate, provided its inputs
do not already exclude the hypothetical event.

### Two possible proof mechanisms

A regular auxiliary evolution could admit an observable for which a
hypothetical collision forces one behavior and an independently acquired
theta estimate forces an incompatible behavior. A schematic comparison
would be an event lower bound L and a complete-source upper bound U<L
for the same normalized quantity on the same stated domain. These letters
are placeholders for an estimate to discover, not a new exclusion
criterion or an acquired bound. A sign or monotonicity comparison could
serve the same role.

An evolution with a singular collision response could instead turn the
event into breakdown, while an independent a priori estimate prevents
that breakdown. The existing feedback magnifier supplies the first half.
[Note29][n29] explains why the tested carrier argument does not supply the
second: its persistent term is
\[
\frac{\mu^2}{M},\qquad
\mu^2=H(T,a)^2+H_z(T,a)^2.
\]
Thus that particular lower bound contains the unknown margin itself.
This scopes the carrier comparison; it does not rule out a different
estimate for the same flow or a different singular evolution.

The bounded cosine family occupies a different position: its theta-source
integral is already entire in the auxiliary parameter, including at a
physical double event. Regularity of that field therefore cannot exclude
such an event. Its exclusion use would require an additional observable
and an incompatible estimate, or a controlled comparison with the physical
slice. This distinction helps compare the two mechanisms without treating
well-posedness as a collision theorem.

### Information an estimate must retain

The useful next discussion is how a local or coupled evolution could make
an estimate involving the signed complete theta source easier to prove.
[Result summary 14][arithmetic] records both exact identities identifying
theta and specific decompositions whose separate absolute estimates lose
essential cancellation. Exact source identification does not itself
supply the signed estimate. A candidate should expose which correlation,
interaction term or boundary contribution it makes controllable and why
that bound follows from the actual source.

For each concrete candidate, the control table in Section 4 must be
applied to the proposed bound, including its constants and domain. Merely
listing a canonical identity absent from a control is insufficient if
the derived estimate is also satisfied by that control. Conversely, a
finite certificate need only reject a control when its claimed domain
contains the control's collision.

A first useful outcome could be a new quantitative restriction on event
location, curvature or response, or a new collision-free region, with a
comparison against existing direct estimates. It need not solve the full
problem. Any global conclusion would additionally need the height range,
time range and multiplicities covered by its collision reduction; the
local nondegenerate-double calculation does not supply those extensions.

The [result index][results], [avoid index][avoid], [target classification
rule][a01], [control rule][a02], [coordinate-change pattern][a03] and
[scope rule][a07] remain the governing references. This objective update
selects the desired payoff without selecting a PDE or numerical campaign.

## Source and checking scope

The continuation, [overview][overview] and [survey][survey] supply the inherited local formulas
and candidate comparisons. This session checked the primary statements in
Hou–Jiang–Newman Theorems 1–2 and Remarks 1 and 4, Newman–Wu Theorem 2,
and DLMF 10.35.1–2 and 10.35.5. These references already appear in the
investigation catalog. The parameter-change and atomic-control identities
above are elementary algebra checked by the drafting assistant. There is
no independent specialist review, certified theta computation or new
collision exclusion in this discussion.

[continuation]: ../notes/01_CONTINUATION_AFTER_LITERATURE_SURVEY_20261028.md
[overview]: ../research-overview/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_OVERVIEW_20261028.md
[survey]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md
[n38]: ../../05_radial_theta_collision_geometry/notes/38_AUXILIARY_SOURCE_FLOWS_AND_COLLISION_RESPONSE_20261028.md
[n29]: ../../05_radial_theta_collision_geometry/notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[arithmetic]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[stable-models]: ../../../../result-summaries/17_constructive_stable_model_obstructions.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[dlmf]: https://dlmf.nist.gov/10.35
[newman-wu]: https://arxiv.org/html/1901.06596v2
[hjn]: https://arxiv.org/html/2208.00917v1

[plan]: ../research-overview/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_OVERVIEW_20261028.md#research-plan-for-an-independent-theta-estimate
[progress]: ../research-progress/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_PROGRESS_20261028.md
