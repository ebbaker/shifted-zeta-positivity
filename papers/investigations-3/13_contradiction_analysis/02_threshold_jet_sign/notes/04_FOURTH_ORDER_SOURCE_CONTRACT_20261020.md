# BW2-01.A: complete-source fourth-order validation contract

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), actual reasoning effort
ultra**, verified from this turn's recorded metadata. Internal same-model
derivation and checking; no specialist review.

**Classification: bounded infrastructure and feasibility milestone.**
This contract executes the permitted already-covered validation alternative
in [overview 03][program]. It does not propose a new global criterion.
The [result summaries][results] and [avoid index][avoid] apply, particularly
[collision controls][controls], [target classification][target],
[normalization][normalization], [scoped claims][scope], and
[signed recombination][signed].

## 1. Frozen question, coverage, and target

The exact bounded event domain is

\[
 D_*=[99999/10^6,100001/10^6]\times
 [29999999/10^6,30000001/10^6].
\]

Write its upper spatial endpoint as \(a_+=30000001/10^6\). Freeze

\[
 L=\frac1{2a_+^2}+\frac1{1600},\qquad A=1,\qquad
 Q_L=2h_3^2-3h_2h_4-18Lh_2^2.
\]

The inherited all-height theorem gives \(S_2>L\) at every hypothetical
ordinary double event in this domain. The lower floor is paid using
\(a\le a_+<40\), exactly as in overview 03, not optimized after looking
at numerical output. No curvature floor is introduced.

The [existing complete shifted evaluator][old-note] already certifies
the real first jet throughout
\(D_0=[1/100,1/5]\times[25,45]\), which contains \(D_*\).
Consequently the physical event class here is already empty. The strongest
applicable source-informed baseline is that event exclusion, not a positive
independent fourth-jet box allowance. This is known before acquisition.

The new questions are (i) whether a complete, source-pinned enclosure
through order six passes the fixed validation contract, and (ii) whether
one shared holomorphic source residual can be returned through order four
without identifying independently truncated component polynomials as the
derivatives of one polynomial. A correct event consumer must reject this
validation case before sign optimization. Such rejection is not a
fourth-order improvement or new covered region. No numeric
\(U_{\rm base},U_{\rm new},G_Q,d_Q,\delta_Q\) is assigned to an empty
feasible event set.

## 2. Source producer and shared residual

The producer is Project 11's unchanged
`numerics/certify_shifted_theta_jet.py`, extended by a separate wrapper and
derivation rather than editing the historical evaluator. Use its complete
reflected theta integral, with the negative half retained by exact
conjugacy at the real Taylor center. Freeze \(d=\pi/16\), modes \(1,\dots,4\),
source endpoint \(U=1\), center \((21/200,35)\), spatial degree 50 and
time degree 12.

The direct output components are \(h_j\), \(0\le j\le6\), in physical
normalization \(H(0,z)=\xi((1+iz)/2)/8\). The new component maximum requires
midpoint derivatives through 80 and Taylor remainder bounds through 82.
The producer must recheck the source-tail tangent and common-moment
admissibility at those actual orders, not inherit the old order-78 checks.
The physical heat identity \(H_t=-H_{xx}\) then pays first-order time
uncertainty in \(h_4\) via \(h_6\).

For the joint interface, let \(P_0(t,z)\) be the exact rational polynomial formed from
dyadic midpoint source jets and the integer factorial denominators.
For every real \((t,a)\in D_*\), bound \(H(t,z)-P_0(t,z)\) on
\(|z-a|\le R=1/2\), uniformly by \(\eta\). An enclosing rectangle is allowed,
with its entire complex image paid. Define
\(p_j=\partial_z^jP_0(t,a)\); the real Schur class is applied to this
single residual. The evaluator's separately truncated polynomials for
component \(j\) need not equal \(\partial_z^jP_0\). They can supply sharper
independent physical-component enclosures, but cannot silently be used as
the coherent \(p_j\). Nor is the finite polynomial asserted to satisfy the
heat equation exactly.

The quantitative information retained beyond the closed homogeneous Gram
relaxation is the actual rational theta polynomial, its signed coefficient
images on the declared domain, and a complete shared residual allowance.
An event fixes
\(r_0=-p_0,\ r_1=-p_1\), so it fixes the first two real Schur parameters
when admissible. That affine information is not replaced by arbitrary
source multiplier directions.

Taking \(A=1\) makes the physical return exact without a normalizer
allowance: \(\alpha_x=0\). The producer also checks the general event
identity
\[
 Q_L/A^2=2f_3^2-3f_2f_4-18(L+(\log A)_{xx})f_2^2
\]
algebraically. This fixture does not validate an uncomputed high-sector
normalizer or transplant its error constants.

## 3. Error ledger and bounded execution

| Obligation | Producer and required treatment |
| --- | --- |
| All omitted integer modes | Existing physical mode-tail formula, with the actual shift/time hypotheses and derivative orders checked |
| Retained source beyond \(U\) | Concave tangent bound with the actual order \(j\), including order-82 common-moment tail where used |
| Quadrature | Outward Arb/Acb integral radii, propagated with absolute Taylor weights |
| Polynomial rounding | Outward evaluation of the exact rational polynomial formed from midpoint jets |
| Parameter and complex-cell variation | Closed rational cell images and the actual complex-distance Taylor radius |
| Shared analytic residual | The sum of mode, source, quadrature and Taylor allowances for \(H-P_0\), not the full image width of \(H\) |
| Component dependence | Genuine derivatives of \(P_0\), real Schur recursion through degree four, and separate direct \(h_0,\ldots,h_6\) boxes |
| Cutoff or moving-center derivatives | None: the contour, mode cutoff, endpoint and Taylor center are frozen |
| Time uncertainty | Physical heat relation and order-six enclosures; no unmodified heat equation for a normalized or truncated field |

The implementation-selected budget is fixed before its retained run:
192 bits and a fresh 256-bit replay; maximum 90 seconds for each source
evaluator construction and 300 seconds for the whole retained run.
Each integral retains the original 200,000 evaluation cap and depth 30.
The wrapper must report actual costs and any budget stop. Do not infer
a speed advantage from the cap. Resident working data are bounded by
83 source-jet slots, the fixed polynomial sizes, and a small validation
record; no parameter sweep or large archive is authorized by this contract.
The process memory cap is 1 GiB; a failure to enforce or measure that cap
must be disclosed rather than presented as a measured bound.

Target total added component error is \(10^{-10}\), with separate
mode/source/quadrature budgets \(10^{-12}\) each and Taylor budget
\(10^{-11}\). Actual values, including which budget dominates, belong
in the producer record.

The fixed cases, all within \(D_0\), are:

- Real points \((.01,25),(.105,35),(.2,45)\).
- Real cells \([.1,.11]\times[28,29]\) and
  \([.01,.2]\times[34,34.1]\).
- Complex cell \([.1,.11]\times[34,34.1]+i[.4,.6]\).
- Six complex points: \(t=.01,.2\) at
  \((x,y)=(25,1),(35,.5),(45,1)\).
- The event-validation cell \(D_*\), plus its radius-\(1/2\) shared
  residual neighborhood.

Use the complete real-source implementation as the separate source-return
comparator where valid. Intersecting enclosures are diagnostics; each
method still needs its own complete outward error proof.

## 4. Consumer, controls and stop

The threshold-sign consumer first checks the event equations. If feasible,
the real Schur recursion gives an enclosing joint coefficient set through
degree four. A signed optimizer must cover that entire set, including
constant and boundary-parameter cases. The canonical consumer derivation
is saved separately; its general algebra is infrastructure, not a
source-specific opposing sign.

Controls include exact polynomial heat events with their own residuals,
boundary Schur parameters, derivative factorial normalization, and a
nonconstant analytic normalizer. The physical consumer must retain each
genuine event. Existing Euler-factor, weighted-square, finite-prime,
reflected-source and positive-primitive controls are screened by their
actual premises: they do not inherit this unchanged theta polynomial
and its source-specific error allowance. Their generic analyticity or
heat equation alone supplies no such constants. Distinguish exact fixtures
from the analytic premise screen.

**Stopping answer:** a validated complete interface on the fixed box, or
a concrete failed component/error/admissibility budget. An empty event
set stops the fourth-order consumer and matched sign comparison on this
box. Do not weaken a good first-jet enclosure to manufacture an event,
enlarge the grid for an apparent improvement, or compare against a weaker
baseline while suppressing the known first-jet certificate.

The unresolved arithmetic application is a paid, coupled center and
order-four residual on a useful uncovered domain, such as a justified
part of the UAR sector. The existing UAR increment theorem by itself is
not that interface. This contract does not extend its derivative
neighborhood or prove a sign for its retained expression.

Source versions consumed at the start of this round are recorded in the
[round-three source receipt][versions] at repository HEAD
`574b658061c5144a78d44a805fe2c116d86f9397`, with individual hashes for
working-tree planning inputs. Later generated sources are pinned in their
own numerical records and the round assessment.

[program]: ../../04_boundary_winding/research-overview/03_FOURTH_ORDER_ARITHMETIC_AND_ACTUAL_PROFILE_PROGRAM_20261020.md
[old-note]: ../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md
[versions]: ../../04_boundary_winding/numerics/ROUND_THREE_SOURCE_VERSIONS_20261020.json
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[target]: ../../../../../avoid/01_restating_the_target.md
[normalization]: ../../../../../avoid/08_normalization_and_constant_slips.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[signed]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

Execution: the [complete Project 11 interface](../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/15_COMPLETE_FOURTH_ORDER_INTERFACE_20261020.md) and [conditioned consumer](05_EXACT_EVENT_CONDITIONED_FOURTH_ORDER_SCHUR_CONSUMER_20261020.md) passed the bounded validation. The OS rejected a hard address-space cap; measured peak memory was below 34 MB, and the 300-second elapsed limit was checked rather than enforced by an outer interrupt. These implementation limits are disclosed in the source record. The event set is empty on D*, so no fourth-order sign comparison is claimed. See the [round review](../../04_boundary_winding/reviews/03_FOURTH_ORDER_AND_ACTUAL_PROFILE_ROUND_REVIEW_20261020.md).
