# Threshold signed arithmetic results and next questions

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
actual reasoning effort **max**, verified from this turn's recorded metadata.

**The program has a quantitative necessary condition for a hypothetical
theta collision, together with increasingly strong obstructions to the
selected ways of obtaining the opposite sign. It has no new theta event
exclusion.** The latest round explains why exact Gram correlations,
source positivity and selected profile information remain insufficient
in the information classes studied. Its results leave estimates using
additional information about the unchanged theta source open.

This synthesis follows the [signed arithmetic program][program],
[eight-route description][routes], [active progress register][progress]
and [round review][round-review], with the supporting proofs linked
below. Sources were read at repository revision
`574b658061c5144a78d44a805fe2c116d86f9397`. The preceding discussion is in
[chat 3][previous-discussion], execution in [chat 4][execution-chat],
and this discussion in [chat 5][this-chat]. This is a brainstorming
synthesis of existing results; the questions below do not change task
status or claim new theorems.

## The comparison we need

The working assumption is a hypothetical positive threshold
\(T=\Lambda>0\) of the unchanged flow \(H_t=-H_{xx}\). At an ordinary
double event \((T,a)\), with \(a>0\), write
\(h_j=\partial_x^jH(T,a)\). Thus \(H=H_x=0\) and \(h_2\ne0\).
These are unknown event parameters, not measured theta data.

The [BW-08 bound][jet] gives

\[
S_2=\frac{h_3^2}{9h_2^2}-\frac{h_4}{6h_2}>L_2(a),
\qquad b=\max\{a,40\},
\]
\[
L_2(a)=\frac1{2a^2}
 +\frac1{4b}\log\frac{b+1}{4\pi}
 -\frac4{a^2+b^2}
 >\frac1{2a^2}+\frac1{40b}.
\]

For a proved fixed \(0<L\le L_2(a)\) on a declared event class, this means

\[
Q_L=2h_3^2-3h_2h_4-18Lh_2^2
   =18h_2^2(S_2-L)>0.
\]

The desired opposing arithmetic estimate is \(Q_L\le0\), or an
independent \(S_2\le L\). A numerical realization must include every
acquisition and parameter error in \(\widehat Q_L+E_L\le0\).
A restricted exclusion would be a meaningful first outcome. Excluding
every possible positive threshold event, including all multiplicities,
would settle RH through the inherited reduction; that global target is
a reformulation, not an achieved estimate.

The sign problem has a useful geometric interpretation. Deflating the
double zero gives

\[
S_2=\frac1{2a^2}
 +\sum_{\rho>0,\ \rho\ne a}m_\rho
   \left(\frac1{(a-\rho)^2}+\frac1{(a+\rho)^2}\right)
\]

under the all-real paired-product hypotheses. An additional root near
\(a\) makes this quantity large. The lower bound is established; the
unresolved arithmetic input must constrain the assumed event strongly
enough to conflict with it.

## Results already available from the first round

| Route | Result available | What it does not supply |
| --- | --- | --- |
| BW-08 | For every \(a>0\) and finite \(m\ge2\), a necessary bound \(S_m>L_m(a)>m/(4a^2)+1/(40\max\{a,20m\})\). For doubles, a finite critical-value pair is strictly negative on an explicitly paid event-dependent interval. | An opposing sign or an excluded event. A more negative pair does not imply zero winding. |
| BW-01 | A positive three-atom control has a genuine threshold, exact cancellation, fixed event height, uniform moments and the two selected imaginary-axis floors, yet retains the collision sign. | An obstruction to every estimate using the complete theta source. |
| BW-02–05 | An explicit forward neighborhood of a double event has a positive Laguerre expression, two real simple roots in the controlled complex disk and zero winding on enclosed later domains. | A nonlocal implication forcing a witness elsewhere for the same function. |
| BW-06 | Complete boundary remainder bounds through derivative order \(m+2\) recover the physical degree \(-\lfloor m/2\rfloor\) for every finite multiplicity. | Zero winding from symmetric absolute remainders around the collision model. |
| BW-07 | Conditional on an exact \(m\)-fold theta threshold event, differentiating \(m-2\) times produces a double event with the same threshold; both parities retain the necessary bound. | Closure of a future arithmetic exclusion under the changed source, or identification of the derivative field's winding with the original winding. |

The canonical sources are the [all-height bound][jet],
[fixed-event control][atomic], [forward-neighborhood theorem][forward],
[physical remainder audit][allm] and [differentiation theorem][derivative].
The differentiated critical-value transfer uses original derivatives
through order \(m+4\). These are reusable analytic results with their
stated internal reviews, rather than a completed contradiction.

## What the signed arithmetic round added

### Exact theta correlations improve the selected bound but cannot sign it

The [Gram study][gram] uses the full theta measure
\(d\nu=e^{Tu^2}\Phi(u)\,du\) for \(0<T\le1/2\), \(a>0\). It retains
the exact fifteen correlations of the five source functions generating
derivatives zero through four, the two event cancellations and a norm
budget. The correlations are coupled to one actual height; this is not
an independent-phase model.

The decisive relaxation replaces the physical multiplier \(w=1\) by
arbitrary multipliers with \(\|w\|^2\le M_0=\int d\nu\). If \(K\) is the
Gram matrix after projecting out the event constraints, the exact
optimized allowance satisfies

\[
0<
2M_0\frac{\det K}{\det K_{\{2,4\},\{2,4\}}}
\le U_\theta<U_{\rm box}.
\]

Thus retaining correlations strictly improves the best matched
independent-coordinate box estimate, while the optimal allowance itself
remains positive. This is an analytic obstruction to that relaxation,
even with exact data. More precision cannot correct it.

The omitted mass anchor is informative:
\(\langle w,1\rangle=M_0\), together with the norm budget, forces \(w=1\).
But this only restores the physical source; it does not estimate its
unknown quadratic. Approximate anchoring controls the distance to that
source, while still requiring signed information about the physical
center.

### Positivity and a genuine threshold do not repair the relaxation

The [continuous-source extension][positive] constructs nonnegative
continuous compact sources with genuine positive thresholds at fixed
\(a=20\), for every \(0<T\le1/2\). They satisfy the reference theta norm
budget, exact event cancellation and common complete moment bounds,
while \(S_2\to+\infty\) and \(Q_L>0\) for every fixed finite \(L\) once
the family parameter is sufficiently close to its limit.

This closes the objection that the original Gram witnesses were merely
signed multipliers without physical threshold behavior. It does not
make these sources theta. Their mass falls short of theta's by at least

\[
\delta_U=M_0-\sqrt{M_0N_U}>0,
\qquad N_U=\nu([0,U])<M_0.
\]

They also lack theta's complete coefficients, full support, unbounded
large-height profile and eventual simplicity at the threshold. Their
curvature \(h_2\) tends to zero. The divergence of \(S_2\) is therefore
not a uniform positive lower margin for the raw \(Q_L\).

### Finite profile information can conceal a degenerating event

The [profile study][profile] examines
\(D_T(b)=\partial_b\log H(T,ib)\). For any prescribed finite set of
distinct positive observation heights, it constructs families with
exactly unchanged profile samples and normalization, while \(S_2\)
diverges. There are both polynomial examples and positive finite-atom
examples with genuine thresholds and common moments. The continuous
extension preserves the finite-sample obstruction after smoothing.

**The common sample values are constructed values, not arbitrary
prescribed values and not acquired theta values.** The theorem does not
show that theta's actual finite profile vector admits these families.
The polynomial family has only the designated pair of multiple zeros
at the threshold but lacks a positive source. The positive-source
families have infinitely many simultaneous multiple zeros there. Their
different premise sets must be kept separate.

A further quantitative result gives

\[
\sup_{b\ge0}|D_\eta(b)-D_*(b)|\le\frac{8\eta}{a},
\qquad
S_2(F_\eta)\ge\frac{25}{8a^2\eta^2}.
\]

Thus even an arbitrarily small positive uniform profile tolerance
around the specified limiting atomic profile admits unbounded normalized
jets. The center \(D_*\) is not theta's profile; exact full-profile
uniqueness is not contradicted.

The study also proves a genuine conditional upper bound from one
profile observation. It requires

\[
0<R<\frac2{a^2+b^2},
\qquad R=\frac{D_T(b)}b-\frac4{a^2+b^2}.
\]

Theta's inherited lower floor forces the opposite strict inequality
for every \(b\ge40\). This particular upper-bound mechanism therefore
fails its applicability test at the observation heights used by BW-08.
Other combinations of actual profile data remain untreated.

## What the controls require us to distinguish

The [repository result summaries][results] and [patterns to avoid][avoid]
apply, especially [control screening][controls],
[target classification][a01], [shared premises][a02],
[scoped negative results][a07] and [signed recombination][a12].
The following records the existing analytical screen; it does not
assign new events or computed signs to untested controls.

| Control class | What survives | Missing premise or limitation relevant to a continuation |
| --- | --- | --- |
| Signed Gram multipliers | Exact reference correlations, norm budget and event constraints | Physical multiplier identity and mass anchor; positivity and a true threshold are not supplied by this first construction. |
| Continuous compact threshold controls | Positivity, continuity, reference norm budget, true threshold and common moments | Theta mass anchor, complete coefficients, full profile growth and eventual simplicity at the threshold. |
| Polynomial finite-profile family | Fixed constructed samples, actual threshold and only the designated multiple zeros | Positive theta source, complete coefficients and theta growth. Eventual simplicity alone does not exclude its nearby simple root. |
| Positive finite-profile families and their continuous extensions | Fixed constructed samples, normalization, moments and actual threshold | Actual theta values, complete coefficients, full growth and eventual simplicity at the threshold. |
| Euler-factor controls | Positive source, genuine positive thresholds and every inherited imaginary-axis lower floor | Unchanged theta coefficients. Merely adding more of the same lower floors does not reject them. |
| Weighted-square and finite-prime controls | Their documented positivity, local events and partial arithmetic constraints | Full normalized reflection or complete coefficients. Their local events must not be treated as all-real thresholds. |
| Reflected, smooth-shape and positive-primitive controls | Their documented reflection, decay or auxiliary positivity | Complete normalized theta arithmetic; no additional threshold premise is supplied by those properties. |
| Hermite and quartic models; positive-kernel controls | Their documented local collision laws and, where proved, threshold facts | Complete theta source or xi identity. Product/order hypotheses must be checked for each family. |
| Smooth-density and two-channel realizations; multiplicative phase relaxations | Their auxiliary positivity or relaxed arithmetic constraints | Respectively, an identified physical threshold source, or coupling to one actual height with its weights and cutoff. |

Failure of a literal theta identity is not evidence that a control fails
a derived inequality. A proposed estimate must identify and use a
quantitative distinction.

## Questions for the next discussion

### First priority is a signed estimate using the fixed theta source

Which specific signed interaction in the complete source can be bounded
more sharply when \(H=H_x=0\) is imposed? The obvious consumer remains
\(Q_L\), with its mixed term retained. Rewriting it or restoring \(w=1\)
is not itself the required gain.

A promising proposal would name an actual coefficient relation or
affine observation, show how it changes the allowed signed jets, and
state the improvement over the strongest comparison using the same
information. The new mass-deficit result is a useful screening fact,
but a mass restriction without signed physical data only returns the
original problem. Euler-factor and finite-prime controls remain
necessary checks on any claimed arithmetic distinction.

The initial milestone can be a quantitative upper-bound improvement
with its remaining deficit, rather than a global exclusion. If the
Project 11 arithmetic approximation is used, its complete fourth-jet
contract, normalizer conversion and cutoff corrections must first be
justified; the existing first-jet contract is insufficient.

### The profile alternative needs actual values and quantitative separation

Can theta's actual profile values on a specified event domain exclude
the nearby-root degenerations, with an explicit conditioning bound?
That question is outside the constructed-vector obstructions. Adding
sample count alone is inside the failure already proved.

A restricted class with a stated curvature or neighboring-root
separation bound is also outside those obstructions. But such a bound
must be derived for the application or openly define the restricted
class. Nonzero curvature at each double event does not give a uniform
floor. Eventual simplicity at the threshold does not prevent an
arbitrarily close simple neighbor, as the polynomial example shows.
Even eliminating these degenerations would still require an upper
bound small enough to conflict with \(L_2(a)\).

The first decision is whether there is a concrete observation and a
plausible quantitative separation argument. The failed one-sample
consumer at \(b\ge40\) should not be relaunched with higher precision.

### Later witnesses and multiplicity remain conditional follow-ons

A later-witness route needs a relation for the unchanged function
reaching beyond the proved forward neighborhood, with a strictly
positive time separation. Neither changed-source controls nor a larger
search box supply that relation.

Once a useful signed double-event estimate exists, its hypotheses decide
whether to extend it directly through BW-06 or through the derivative
source in BW-07. There is presently no exclusion base case to extend.
These routes remain available without requiring another round of
multiplicity calculations now.

My suggested opening question is: **what observation retains a signed
feature of the physical theta source that the surviving controls lack,
and what quantitative improvement should it buy?** Until one is
specified, additional Gram precision, source-continuity repairs,
profile-sample counts and equivalent representations repeat the
information classes already screened.

## Present stopping point

BW2-01/02/03 are closed selected attempts and BW2-07 is their completed
review. BW2-04/05/06 remain deferred. No theta jets were acquired in
this round, and it established no new theta event exclusion, covered
region, later witness, physical-transfer margin or Newman-bound
improvement.

The three studies have proofs in the notes and separate-agent,
same-model internal reviews. The finite control replay uses exact
rational arithmetic; repeated executions of the same script are not
independent implementations. Specialist review remains outstanding.
New work, if selected, should reopen the appropriate task in the
[existing active register][progress].

[program]: ../research-overview/02_THRESHOLD_SIGNED_ARITHMETIC_RESEARCH_PROGRAM_20261020.md
[routes]: ../threshold_routes/README.md
[progress]: ../research-progress/02_THRESHOLD_SIGNED_ARITHMETIC_PROGRESS_20261020.md
[round-review]: ../reviews/01_THRESHOLD_SIGNED_ARITHMETIC_ROUND_REVIEW_20261020.md
[jet]: ../threshold_routes/08_deflated_jet_hierarchy/notes/04_ALL_HEIGHT_MULTIPLICITY_JET_BOUND_20261020.md
[atomic]: ../threshold_routes/01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md
[forward]: ../threshold_routes/05_later_laguerre_violation/notes/02_QUANTITATIVE_FORWARD_NEIGHBORHOOD_EXCLUSION_20261020.md
[allm]: ../threshold_routes/06_direct_all_multiplicity/notes/02_ALL_MULTIPLICITY_REMAINDER_AUDIT_20261020.md
[derivative]: ../threshold_routes/07_multiplicity_reduction/notes/02_DIFFERENTIATED_THRESHOLD_TRANSFER_20261020.md
[gram]: ../../02_threshold_jet_sign/notes/02_EVENT_CONDITIONED_THETA_GRAM_OBSTRUCTION_20261020.md
[positive]: ../../02_threshold_jet_sign/notes/03_POSITIVE_MULTIPLIER_GRAM_EXTENSION_20261020.md
[profile]: ../threshold_routes/08_deflated_jet_hierarchy/notes/05_FINITE_PROFILE_CONDITIONING_OBSTRUCTIONS_20261020.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[previous-discussion]: ../chat-histories/0003_2026-10-20T04-37-25Z_review-boundary-winding-progress.json
[execution-chat]: ../chat-histories/0004_2026-10-20T04-56-09Z_continue-signed-arithmetic-research.json
[this-chat]: ../chat-histories/0005_2026-10-20T05-48-11Z_summarize-signed-arithmetic-research.json
