# Quasi-RH exponent descent

Prepared for Edward Baker, 8 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

This investigation asks whether a fixed zero strip strictly inside the
critical strip can force the Riemann hypothesis through arithmetic exponent
descent or exclusion of positive-time Newman collisions. It continues the
[initial bridge note](../prime-variance-exponents/notes/QUASI_RH_NEWMAN_BRIDGE_20261008.md)
and the [prime-variance project](../prime-variance-exponents/README.md).

The [investigation summary and notes index](notes/README.md) maps the five
project folders and their current results and open tasks.
For the next research session, start with the
[short-family continuation](short_families/notes/7_SHORT_FAMILY_CONTINUATION_20261008.md)
and [dependency ledger](notes/RESEARCH_LEDGER_20261008.md), then consult the detailed
[Codex continuation note](notes/CODEX_CONTINUATION_20261008.md) for the broader program.
It integrates a review of
[character amplification](../quasi-rh-character-amplification/README.md),
the latest remaining mixed character sum, and a conditional short-family
descent map, alongside covariance, height-adapted, Newman, and other routes.
The [relevance review](reviews/CHARACTER_AMPLIFICATION_RELEVANCE_REVIEW_20261008.md)
records source qualifications and scoped checks. The new family estimates
needed for iteration remain unproved; zeta-only quasi-RH does not supply
them automatically.

The first continuation establishes several analytic reductions and
obstructions, and sharpens the complete arithmetic remainder. It does not
prove quasi-RH implies RH, a new zero-free strip, or the required arithmetic
contraction. The proposed implication remains a research target; no claim
of mathematical priority or independent specialist validation is made.

## Focused continuation: short families

The [new results](short_families/notes/7_SHORT_FAMILY_CONTINUATION_20261008.md) enlarge the
controlled overlap sector to dyadic blocks \(BF^2G^2\ge D^{1-a}\),
correct two missing conjugations in the earlier exact formulas, and show
that a second Poisson transform returns the coprime core to its original
Möbius form. Its prime-selected part alone exceeds every useful target by
more than a quarter power, so prime and composite columns cannot all be
estimated separately. The unrestricted signed core remains open.

A newly imported sixth-order sieve gives the generic baseline
\(\mathfrak M\ll D^{1+\varepsilon}H^{1/6}\), which extracts only
exponent one. Composite replication, weights, and lower-order families
inherited from the same moment do not improve the extraction floor.
The [scoped review](reviews/SHORT_FAMILY_CORE_AND_OVERLAP_REVIEW_20261008.md)
separates the new deductions, imported theorem, and remaining obligation.
No new zero-free boundary is established.

## Results of the third continuation

| Record | New result | Remaining obligation |
| --- | --- | --- |
| [Small-cofactor reduction](short_families/notes/2_SHORT_FAMILY_SMALL_COFACTOR_20261008.md) | Removing the original diagonal permits a second Poisson sum and rapid decay in another cofactor/overlap sector; an actual unit column obstructs extension of the old positive dual theorem | Signed estimate in the remaining small-cofactor, low-overlap region |
| [Selected inverse distribution](mixed_character_families/notes/2_SELECTED_INVERSE_DISTRIBUTION_20261008.md) | A legal positive-frame transposition, bounded primitive-character fibers, controlled repeated-character cubic terms, and an exact finite-character obstruction to discarding phases | Signed cycle over three inequivalent primitive characters, or a weaker direct fixed-vector estimate |
| [Quadratic moment strength and barrier](integer_quadratic_lift/notes/2_QUADRATIC_MOMENT_STRENGTH_AND_BARRIER_20261008.md) | The target would improve every odd primitive quadratic character; its actual prime-pair absolute majorant is at least order \(X^2\) | Signed cancellation beyond individual bounds and the classical large sieve |
| [Normalized heat criterion](newman_collisions/notes/3_NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md) | Holomorphic disk errors and derivative control; explicit real-collision exclusion above \(e^{64/\varepsilon}\) for \(t\in[\varepsilon,1/2]\), from the imported effective approximation | Certified middle-height coverage and a new argument as the time floor tends to zero |

The [third results note](notes/THIRD_CONTINUATION_RESULTS_20261008.md)
links each separate scoped review and states the next bounded tasks.
The arithmetic remainders remain open; the heat result does not supply
all-positive-time collision exclusion.

## Results of the second continuation

| Record | New result | Remaining obligation |
| --- | --- | --- |
| [Short-family extraction](short_families/notes/1_SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md) | One fixed short-family moment can be reused finitely to remove the prime-mask error, without an initial strip or scale supremum | Actual short-family estimate, especially the small-cofactor dual blocks |
| [Mixed conductor refinement](mixed_character_families/notes/1_MIXED_CONDUCTOR_REFINEMENT_20261008.md) | Buffered continuous cutoff certificate and an additional removable plain-conductor sector using selected inverse mass | Signed estimate beyond both refined cutoffs |
| [Integer quadratic response lift](integer_quadratic_lift/notes/1_INTEGER_QUADRATIC_RESPONSE_LIFT_20261008.md) | Exact complete prime-response replication with logarithmic deletion error; larger conductors fit the proposed moment budget | New weighted small-conductor prime moment, including its coherent principal term |
| [Theta collision arithmetic](newman_collisions/notes/2_ZETA_COLLISION_ARITHMETIC_20261008.md) | Every fixed finite theta cutoff has an eventually negative Wronskian; exact error bounds support compact conditional certificates | Derivative-controlled normalized approximation and arithmetic collision exclusion |

Each note has a separate scoped review linked from the
[results summary](notes/SECOND_CONTINUATION_RESULTS_20261008.md).
The new finite algebra checks passed; collision numerics are explicitly
uncertified reconnaissance. No new zero-free boundary is established.

## The common parameter

The internally reviewed fixed-probe theorem in the parent project gives

\[
\mathcal V_g(X)=O(X^{2+\delta})
\iff |\Re\rho-1/2|\le\delta/2
\quad\text{for every nontrivial zeta zero}.
\]

Its least admissible exponent \(\delta_*\) is attained. Quasi-RH means
\(\delta_*<1\); RH means \(\delta_*=0\). In the conventional Newman
normalization the strip theorem supplies
\(0\le\Lambda_{\rm DN}\le\delta_*^2/2\). The lower bound is already
unconditional; the new task would have to exclude a positive optimum or
a positive transition time.

## Results of the first investigation

| Record | Result | Status |
| --- | --- | --- |
| [Fixed scale descent](fixed_scale_descent/notes/1_FIXED_SCALE_DESCENT_CRITERION_20261008.md) | A contraction of normalized variance from \(X\) to \(X/b\), with a power-decaying remainder, forces a strictly smaller exponent. An exact signed prime-profile identity isolates the needed estimate. | Iteration proved; arithmetic contraction open |
| [Spectral edge and logarithmic savings](fixed_scale_descent/notes/2_SPECTRAL_EDGE_AND_LOG_SAVINGS_20261008.md) | At a positive admissible exponent, little-o is equivalent to absence of boundary zeros. A symmetric spectral model has every logarithmic saving but no smaller power. | Deductions from the inherited explicit formula; model is not actual primes |
| [Arithmetic feedback and resonance](fixed_scale_descent/notes/3_ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md) | The complete mixed Möbius/von Mangoldt scalar has remainder \(O(X^{-7/12})\). Its moving-cutoff transform preserves every forbidden-zero residue. A filtered probe exposes a concrete signed delay defect. | Deductions from cited arithmetic identities; new cancellation estimate open |
| [Newman flow and collisions](newman_collisions/notes/1_NEWMAN_FLOW_AND_COLLISION_SCOUT_20261008.md) | A positive zeta threshold must occur at a finite real multiple zero. A positive, even, decreasing, rapidly decaying kernel shows that those analytic properties and a narrow strip do not force threshold zero. | Deductions from cited heat-flow theorems; counterexample concerns general kernels |

Two distinctions govern the program. First, attainment of an optimal
*variance bound* does not imply that a zero lies on the edge of its strip;
the supremum may be approached only at unbounded height. Second, a constant
contraction at arithmetic factor scales such as \(X^{1/2}\) may produce
only logarithmic savings. A contraction at fixed multiplicative scales
such as \(X/2\) can produce the needed power gain.

On the heat-flow side, existing strict strip improvements can degenerate
near a positive collision time. General kernel positivity and decay do
not exclude that behavior. Additional information specific to zeta is
still needed.

## The next arithmetic target

For \(E_\delta(X)=X^{-2-\delta}\mathcal V_g(X)\), the sufficient target is

\[
E_\delta(X)\le qE_\delta(X/b)+CX^{-\eta},
\qquad b>1,\quad0<q<1,\quad\eta>0.
\]

If such a statement were available at every positive admissible
\(\delta<1\), applying it at \(\delta_*\) would contradict optimality.
The present project does not assert it. One bounded scout is the
complete signed defect in the arithmetic note, equations (14)--(18),
with both scale cutoffs, continua, and terminal bands retained. The known
remainder has enough power decay for a small improvement; the unresolved
part is the signed arithmetic functional.
The continuation note keeps this sufficient route alongside other possible
endpoints; a proof need not pass through this particular recurrence.

Every candidate argument must survive two checks: it must control
hypothetical zeros approaching the edge at unbounded height, and its
contraction must accumulate into a power gain. A transform that merely
cancels the detector's forbidden poles has not proved a smaller strip.

## Verification and layout

The [initial review](reviews/INITIAL_REVIEW_20261008.md) records separate
same-model proof checks and their scope. The
[exact calculations](numerics/README.md) verify finite algebraic identities
and remainder exponents using rational arithmetic. They are not a
numerical proof of any asymptotic prime estimate.

Research notes live in each investigation's `<project>/notes/` folder;
the [shared notes index](notes/README.md), continuation plans, and dependency
ledger live in `notes/`. Checks remain in `reviews/`, and reproducible
calculations in `numerics/`. This is a research package; no manuscript has
been created. [DRAFT_HISTOR.md](DRAFT_HISTOR.md) records the initial working
state and will index later commits or tags without draft snapshot folders.
Third-party PDFs and large derived data stay outside the repository under
[LARGE_FILES.md](../../LARGE_FILES.md).
