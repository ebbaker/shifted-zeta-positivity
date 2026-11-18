# B10 r1 — Recursive enclosures and continuous forward–backward pairing

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model/effort unavailable in guarded
CM chat0004; conceptual adviser inherited settings. Lead-authored decision;
the integrated manuscript and this derivation are assessed by E32.

The author proposes repeated forward statistical acquisition, backward
improvement and another forward pass, possibly expressed continuously.
This note selects two complementary formulations: sound two-sided
trajectory enclosures, and an exact continuous forward-error/backward-
adjoint identity. **Status: proved elementary soundness and residual
identities under explicit hypotheses; no acquired strict canonical
improvement, convergence rate or source estimate.** Neither formulation
changes the physical Newman evolution or supplies a stable finite closure.

Read [result summaries][results], especially [cluster18][cluster] and
[collision controls12][controls], and [avoid][avoid], especially
[classification01][class], [premises02][premises], [coordinate changes03][coordinates],
[scope07][scope] and [joint12][joint]. [Note32][n32] gives the retained-F
consumer; [Note34][n34] gives the forward estimates and the exact limitation
of an unchanged initial-M return. Under avoid01 the present construction
is a representation and a conditional enclosure mechanism, not an
RH-equivalent reformulation or a new canonical sign criterion. A useful
milestone still needs a finite strict margin, source cost or coverage gain.

## 1. What a recursive gain would mean

Physical time t and refinement index k are different variables. A forward
step computes or encloses observations from the unchanged complete source;
a backward step constrains earlier observations using the same source,
the same labels and paid dynamics. Iteration may reduce an outer enclosure
by preserving correlations or adding checked observations. It does not
change the actual zero path or create a second independent copy of it.

Fix a finite interval with independently cleared counted contours. For a
pair, use regular coordinates c,D,M and complete traces, allowing both
signs of D when the pair contour remains separated. For an overlapping
block, use an independently valid common chart or larger-cluster symmetric
coordinates when edge charts fail. No chart is made regular merely by
introducing the refinement index. Full-time positivity is not an
admissibility condition for the path set whose positivity is sought.

The canonical field is deterministic. “Statistics” can mean a finite
empirical measure over labels or blocks, but changing a marginal enclosure
does not authorize changing the shared environment. Uniform labels carry
integer counts, including multiplicity; no statistical independence is
introduced. Source refinements must preserve every earlier verified
observation and its error allowance.

## 2. A sound two-sided recursion

Take finite times t_0<...<t_m. Let omega denote a common complete-source
record, including shared error parameters and label/count identifications.
Let E_i^0 be an outer set of augmented states (omega,z_i) at t_i. The true
record omega_* and true observables z_i* belong to all E_i^0. Let R_i be
a paid relation from augmented states at t_i to those at t_(i+1):

    ((omega,z_i),(omega,z_(i+1))) in R_i.

Each R_i contains the true transition and preserves the same omega.
It may be an outer relation, not an exact realizability characterization.
Let O_i^k be any newly acquired sound observation set containing the true
augmented state. If no new observation is obtained, take O_i^k universal.
Define Post_i(A) and Pre_i(B) as the two existential projections of R_i.
One simultaneous refinement is

    E_i^(k+1)=E_i^k intersect O_i^k
                intersect Post_(i-1)(E_(i-1)^k)
                intersect Pre_i(E_(i+1)^k),                 (1)

omitting nonexistent factors at i=0,m.

**Soundness theorem.** For every finite k, E_i^(k+1) is a subset of E_i^k
and contains the true augmented state. Proof is induction: the true
neighboring states are witnesses for both existential projections, and
the observation is sound. All intersections therefore retain the true
state. Empty output contradicts at least one input/transition/observation
premise; it is not automatically a zero-exclusion proof.

To bound a joint statistic, retain the full skeleton set

    P^k={ (omega,z_0,...,z_m): (omega,z_i) in E_i^k
                    and each adjacent transition belongs to R_i }. (2)

The same induction gives P^(k+1) subset P^k and the true skeleton in
every P^k. For any fixed real statistic Q on that skeleton,

    inf_(P^(k+1)) Q >= inf_(P^k) Q,
    sup_(P^(k+1)) Q <= sup_(P^k) Q.                         (3)

This proves nonworsening bounds, not strict improvement, an effective
limit, a fixed-point rate or exact characterization of feasible paths.
In fact, for fixed R_i there is the stronger identity

    P^(k+1) = {p in P^k: every node of p belongs to O_i^k}. (3a)

Each skeleton in P^k is its own witness for every neighboring projection;
it survives exactly when it satisfies the new observations. Thus with
universal observation sets, P^(k+1)=P^k and its exact joint statistic
bounds are unchanged. Projection sweeps can improve marginal outer
estimates by removing states with no compatible neighbors. Shrinking the
full already-retained feasible set requires new observations or soundly
refined transition relations. This sharpens the same-information screen:
the proposed recursion is an enclosure algorithm, not a new source of
information hidden in exact reversal.
Singleton marginal bounds can lose correlations still present in (2).
Relations that use independently reselected source records on each cell
are a different, usually weaker relaxation; they do not encode the claimed
common-source compatibility. An implementable outer Post/Pre operation
must itself retain the true transition and round outward. Intersecting
such outer images with E_i^k remains sound, although it need not recover
the exact operation (1).

For a whole-interval statistic, replace the skeleton set with sound
complete cell paths joined at their endpoints, or pay an explicit
between-node interpolation/derivative error. Positivity at sampled nodes
does not exclude a collision between them. To infer a positive D over a
desired interval, bound its whole-path minimum or use an independently
valid first-lower-exit argument; do not define P^k to exclude that exit.

### The exact-flow comparison

For one prescribed comparison flow Phi on a domain with unique forward
and reverse solutions, Phi^-1(Phi(A))=A. This follows by injectivity and
does not require a stability bound on the inverse. If the final set is
only the exact forward image of the initial set and no other constraint
is added, a forward/reverse pass adds no information. Outer interval
representations may still be tightened by reusing constraints they had
discarded. Independently checked same-source observations can also shrink
the feasible set. These possibilities are not excluded by the identity.

This is a scoped consistency test, not a universal no-improvement theorem
for source computation or recursive enclosures. The true canonical source
is one common record; an outer numerical source set represents uncertainty
about it, not permission to perturb theta's coefficients.

## 3. A continuous two-sided residual identity

Use the physical **forward** pair system on a regular independently
cleared tube, with D allowed to have either sign:

    y=(D,M),   y'=G_F(y),
    G_F(D,M)=(2-4DM, 2M^2-F(t)).                            (4)

F(t) is the actual complete physical forcing along this same pair. Its
use in (4) is not a claim that two moments form an autonomous closed
canonical system. A source acquisition, contour evaluation or regular
hierarchy must still supply it and its correlations.

Choose a C1 reference path yhat, an integrable reference forcing Fhat,
and define

    e=y-yhat,  deltaF=F-Fhat,
    r=yhat'-G_Fhat(yhat),
    Ahat=[[-4 Mhat,-4 Dhat],[0,4 Mhat]].

Exact expansion, with no omitted linearization remainder, gives

    e'=Ahat e+(-4 e_D e_M, 2 e_M^2-deltaF)-r.               (5)

For any target time tau in [a,b] and vector ell, solve the linear adjoint

    p'=-Ahat^T p,      p(tau)=ell.                          (6)

On the compact interval continuous Ahat has a unique solution in both
directions. With

    Psi=-4 p_D e_D e_M+2 p_M e_M^2-p_M deltaF-p dot r,

the product rule cancels the linear terms and gives (p dot e)'=Psi.
Consequently the same target error has both representations

    ell dot e(tau)=p(a) dot e(a)+integral_a^tau Psi dt
                  =p(b) dot e(b)-integral_tau^b Psi dt.     (7)

For ell=(1,0), this is the D-error. No division by D appears; target-pair
merger regularity is preserved as long as the complete exterior contour
and these regular observables remain valid. A neighboring edge may still
lose its chart, so (7) is not a simultaneous all-edge merger theorem.

If paid enclosures of the two right sides are I_L and I_R, then
`ell dot e(tau) in I_L intersect I_R`. Feeding the improved source/path
enclosure back into the signed integrals gives the continuous analogue
of (1). Strict interval shrinkage is possible but is not established for
the canonical application. Both endpoints, both integrals and every
refinement must retain the same actual e and deltaF. Their errors are
correlated, not independent measurements.

The transparent absolute allowance is

    |Psi| <=4|p_D|E_D E_M+2|p_M|E_M^2+|p_M|E_F
                            +|p_D|R_D+|p_M|R_M,            (8)

when |e_D|<=E_D, |e_M|<=E_M, |deltaF|<=E_F and |r_i|<=R_i.
This is an optional sufficient payment, not a demonstrated optimal one.
It can lose precisely the signed correlations sought by the project.
Large adjoint coefficients or unknown endpoint errors can erase any
benefit; source accuracy does not alone bound the signed integral.

Finite empirical averages of (7) are valid term by term with fixed
weights and consistently retained labels. They bound linear statistics
of the errors. They do not by themselves give a lower-tail or zero-
exception theorem. A bad-event majorant, its resolution/derivative costs,
full population/boundary coverage and an integer exclusion threshold must
still be paid. An average in time can miss an isolated collision.

## 4. Relation to the recent consumers

The unsigned backward force envelope of Note32 loses correlations and
has its stated .0008 cap. The fixed-K consumer fails the chosen compact
interval even with its retained transient. Those facts do not exclude
(1) or (7), which keep full joint source/path information, but they do
identify reductions not to repeat inside the iteration.

Note34 proves `(h-t)'=-2Fh^2` for the unchanged initial-M horizon in its
stated domain. Repeatedly forwarding data and applying exactly that
consumer cannot accumulate an endpoint gain while those hypotheses hold.
The recursive proposal must therefore retain a different quantitative
input, such as the physical forcing of Note32. Its conditional F>=.3
margin remains unacquired; this formulation does not obtain it by
iteration. It also does not show improvement over direct regular D/M or
source-discriminant computation with the identical information.

## 5. Controls and a finite future gate

The [control catalog][controls] is screened at premises. Quadratic and
quartic heat fields satisfy these local identities but lack the exact
canonical source/population; their collision paths are retained by every
sound filter whose data include them. Cosine and cosine-plus-constant
likewise test reversible and colliding cases, not theta. Euler translates
change exact arithmetic; weighted-square, finite-tail/score and finite-
prime controls fail complete reflected unit-weight source equality.
Reflected super-Gaussians fail the canonical order class; smooth/positive-
primitive and finite-profile controls do not supply the full canonical
source/count transfer. Changed observation kernels and fractional profiles
fail physical readout and integer multiplicity, respectively. RH-
conditional endpoint controls retain RH and changed arithmetic. Static
surgery lacks the common canonical heat path required by the proposal.
These failures distinguish source applications; the representation itself
does not sign theta or eliminate any control with sound supplied data.

Before a source execution, select one finite pair/block and physical
interval, independently paid common contours/counts, regular coordinates
through every relevant stop, initial and any later observations, and a
fixed joint statistic. Give the transition/adjoint residual error budget
including whole-time errors, tails, arithmetic, source correlations and
boundary events. Predeclare a strictly positive gain in margin, duration,
coverage or measured cost against the same-information direct comparator,
plus finite cell/refinement/runtime caps and a separate assessment.
If only (3) is known, the result is sound bookkeeping and no gain is
claimed. No execution or larger numerical campaign is issued here.

**Decision:** integrate the two rigorous interfaces as a distinct final
analytical section, with the recursive canonical improvement explicitly
open. The next conceptual B10 r2 gate is one source-specific strict
refinement estimate, not another formal iteration. E16 remains optional;
no manuscript statement should upgrade either interface into its missing
stable approximation theorem or a new bound on Lambda.

[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[coordinates]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[n32]: 32_VCD_GT_CM_FORCE_DISPERSION_AND_RETAINED_FORCING_20261118.md
[n34]: 34_VCD_GT_CM_TIME_ZERO_FORWARD_STATISTICS_20261118.md
