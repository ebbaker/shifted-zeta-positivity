# Decision on the cosine and quartic first responses

29 October 2026, America/New_York. Research begun 28 October. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Investigation06 chat0003, **Compare auxiliary collision flows**.

**ACF-B01 R1 completes with a scoped failure.** Exactly two candidates
were compared. No C1 or E01 packet is selected. This is a design decision
about the response mechanisms below, not closure of auxiliary-flow
research or of all uses of these generators.

| Candidate | Normalized observable | Decision and reason |
| --- | --- | --- |
| Complete theta source multiplied by exp(s cos(au)), with a fixed | Initial s derivative of F(t,s,a)/F(t,s,0) | Do not select variance positivity or bounded response as the separator. The derivative is a positive variance at admitted collisions, including controls with double-exponential decay. |
| Complete theta source multiplied by exp(su⁴) | Initial s derivative of F(t,s,a)/F(t,s,0), divided by M4/M0 | Do not select a guaranteed nonzero first response. It can be exactly zero at a nondegenerate collision of a positive, even, entire, double-exponentially decaying source whose quartic family is entire. |

[Note02](../notes/02_COSINE_QUARTIC_RESPONSE_COMPARISON_AND_SCOPED_FAILURE_20261029.md)
contains the equations, physical slice, jet and normalization terms,
analytic domains, tail accounting, controls and direct comparison. Its
new control corrects the domain gap in the older Gaussian/quartic test:
three exact event constraints survive a double-exponential damping by a
transverse implicit-function argument. This is proved in-note with
same-assistant checking, without a certified finite damping value.

The complete canonical coefficients remain present in the candidate
definitions, but the selected response estimates use only generic source
properties. A missing canonical premise in a control is not itself a
signed estimate. Neither candidate acquired a canonical inequality whose
derivation could be handed to E01 with a useful acceptance test. There is
no reason to run a simulation to confirm the analytical failures.

If the author continues, the named different question is **a signed
interaction bound between distinct square modes, retaining the complete
\(n\ne m\) sum and the unchanged unit coefficients**,
before choosing another flow from its apparent sensitivity. A renewed
ACF-B01 round must name the actual interaction term and an independently
estimable inequality, and explain which tested premise a collision
control fails. No third flow or observable is defined or compared here.

[Progress01](../research-progress/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_PROGRESS_20261028.md)
owns live status; [Continuation03](../notes/03_ACF_B01_SCOPED_FAILURE_AND_MODEL_CONTINUATION_20261029.md)
contains the bounded next question and model-change prompt. The
[result index](../../../../result-summaries/README.md),
[control register](../../../../result-summaries/12_collision_controls_and_screening.md),
[avoid index](../../../../avoid/README.md),
[target rule](../../../../avoid/01_restating_the_target.md) and
[scope rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
apply. No repository-wide result status is promoted by this design return.
