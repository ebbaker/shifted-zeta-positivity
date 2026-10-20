# Internal review of the event-conditioned positive-source obstruction

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Parent reviewer **gpt-6-astra (Codex)**,
actual effort **ultra**, reviewing a separate same-model agent's work.
This is internal LLM review, not independent specialist review.

**Assessment: the scoped obstruction in [Note 04][note] is supported.**
It tests a stronger information class than the earlier centered-model
remainder obstruction: positive source, actual all-real threshold, exact
event cancellations, fixed time/height and uniform moment upper bounds.

The parent checked the complete three-atom source and heat law, the
quadratic in cos(λz) and its discriminant factorization, the strict
location of both future cosine roots in (-1,1), and the backward
Gaussian average. The latter is positive on the real axis, while the
entire cosine polynomial has complex zeros. These establish the exact
threshold T, rather than merely a local event with an assumed threshold.

Direct differentiation gives the stated h2,h3,h4. Substitution of the
critical curve gives the exact face pair, including its factor λ² in
the denominator. The pair is negative throughout its stated symmetric
interval and its normalized curvature diverges negatively as q→1.
Normalization H(T,0)=1 and the common support bound π/10 give the
uniform complete moment budgets even along this degenerating family.
The shrinking critical-curve interval is explicitly retained.

During review the parent requested screening against the newly selected
b=40 observation, in addition to the older b=20 one. The strengthened
subfamily q>=99/100 passes both. The alternating cos(3) bound, positive
exponential series and Machin π lower bound rigorously pay the constants.
The resulting S also exceeds the new adaptive L2(20). This improves the
scope of the counterexample to the actual current consumer.

The parent replayed the [exact checker][checker] successfully: symbolic
polynomial identities, five rational q values, the critical-value
substitution, and the elementary bounds pass. These computations check
finite algebra and constants; the analytic proof carries the continuum
of parameters and the threshold claim.

The failures of full theta premises are material: the control is atomic,
has infinitely many simultaneous threshold events, lacks theta's eventual
simplicity at that threshold, and fails the imaginary-axis lower floor
at sufficiently large b. It therefore does **not** defeat an estimate
using the unchanged complete theta source, the whole imaginary-axis
profile, or those additional threshold properties. The note states this
scope repeatedly. It also separates the unbounded quotient obstruction
from the fixed-control opposing-sign obstruction; adding a lower bound
on |h2| removes only the former argument.

The accepted stop is the reduced-information opposing-sign attempt.
BW-01 and BW-08 remain open. No theta event, region or Newman bound is
claimed. This follows the [control discipline][controls] and [scoped
exclusion rule][scope].

[note]: ../notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md
[checker]: ../numerics/check_event_conditioned_positive_source.py
[record]: ../numerics/EVENT_CONDITIONED_POSITIVE_SOURCE_20261020.json
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
