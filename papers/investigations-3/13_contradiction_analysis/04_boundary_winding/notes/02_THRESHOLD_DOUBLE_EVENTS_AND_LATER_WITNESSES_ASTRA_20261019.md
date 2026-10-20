# Double threshold events and later witnesses

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
actual reasoning effort **xhigh**, verified from recorded turn metadata.

**Status: exploratory targets and inherited deductions.** The first target
is an ordinary double zero at a hypothetical positive threshold of the
unchanged theta flow. A second contradiction would force a later nonreal
zero or real multiple zero of that same flow. Neither missing arithmetic
implication is established. This note does not create a full research
program or progress register.

The [result summaries][results], especially [local index and threshold
results][indices], separate the inherited reductions from new estimates.
The [patterns to avoid][avoid], especially [target classification][a01],
[control premises][a02], and [scoped conclusions][a07], govern their use.
The all-multiplicity global contradiction is RH-strength; the double-event
restriction leaves possible higher-multiplicity threshold witnesses open.

## First target at the positive threshold

Assume RH fails, set T=Lambda>0, and choose a finite positive real multiple
zero x_* of H_T. Existence uses the predecessor's finite-collision reduction
and uniform positive-time nonreal-zero confinement. For the first target,
add the restriction

\[
H(T,x_*)=H_x(T,x_*)=0,\qquad h_2:=H_{xx}(T,x_*)\ne0.
\]

All zeros of H_T are real; for t>T they are real and simple. The double
restriction is not supplied by threshold existence. Several threshold
events may occur at distinct positions. The [predecessor][predecessor],
`prop:finitecollision` and `lj:threshold`, and [Polymath][polymath],
Proposition 3.1, supply the relevant facts.

In a sufficiently small isolating spacetime domain D around (T,x_*),
with nonzero boundary jet and orientation dt wedge dx, the physical jet
has winding -1. The original boundary target is an independent arithmetic
determination W(D)=0, or W(D)>-1. The event lies inside D, with time faces
on opposite sides of T; a boundary passing through the event is inadmissible.
An event-dependent neighborhood exists analytically, but its construction
alone supplies no arithmetic certificate or quantitative boundary margin.

## A later witness contradicts the proposed threshold

The unchanged flow has one threshold. The precise form of a larger-Lambda
contradiction is to deduce one of the following from the hypothetical event
and additional genuine arithmetic information:

1. A nonreal zero H(t_1,z_1)=0 at some t_1>T. The threshold property then
   requires Lambda>t_1>T=Lambda.
2. A real multiple zero at some t_1>T. Local splitting gives nonreal zeros
   at times just below t_1; one can choose such a time still above T.
3. A boundary-regular region D_+ with closure in t>T and negative physical
   jet winding. The index law forces an event in D_+, reducing to item 2.

Any strictly positive separation t_1-T suffices, even if it depends on the
assumed event. There is no need to iterate to infinity or obtain a uniform
time increment. An increased upper bound for Lambda, or a larger threshold
for a modified source, would not give this contradiction.

The two winding targets therefore have opposite arithmetic objectives:

| Region | Consequence of the hypothetical threshold | Missing arithmetic conclusion |
| --- | --- | --- |
| D isolates the double event at T | W(D)=-1 | W(D)=0 |
| D_+ lies wholly after T | W(D_+)=0 | W(D_+)<0 |

For the second row, all-real simplicity for t>T makes the physical jet
nonzero throughout D_+ and its boundary. The assertion that the genuine
arithmetic forces the incompatible winding is the unproved step.

A possible scalar witness is

\[
\mathcal L(t,x)=H_x(t,x)^2-H(t,x)H_{xx}(t,x)<0
\quad\text{at some }t>T.
\]

For the theta function, its order-one canonical product at an all-real time
implies nonnegative Laguerre expression on the real axis. Thus negativity
would contradict the threshold. This is a sufficient witness, not a claim
that every nonreal zero must give this particular negative expression.

The local calculation already constrains this route. At an ordinary double
event, the heat equation gives

\[
\partial_t\mathcal L(T,x_*)=h_2^2>0,\qquad
\mathcal L(T+s,x_*)=s h_2^2+O(s^2)>0
\quad(s>0\text{ sufficiently small}).
\]

The nearby roots are real and simple for small positive s, with positions
x_* plus or minus sqrt(2s)+O(s). These are inherited local facts, not a
later-witness mechanism. The proposed opposite sign cannot come from this
same-point immediate Taylor behavior. A later witness would need additional
arithmetic consequences beyond the local split.

## What an extension beyond multiplicity two needs

At exact multiplicity m, F=partial_x^(m-2) H has a double zero and satisfies
the heat equation. It is a different function, however: differentiating
changes the source and arithmetic observations. A theorem restricted to H
cannot automatically be applied to F. Dividing out repeated roots on the
threshold slice likewise does not produce the unchanged heat flow.
Generic perturbations that split a multiple event also change the function.
Each proposed reduction needs preservation of the premises used in the
double-event proof, with its full error contract.

Two extensions remain reasonable questions. A boundary estimate formulated
without H_xx nonvanishing might work for every multiplicity directly,
because the existing index is -floor(m/2). Alternatively, a derivative
argument might extend through the predecessor's deflated mirror hierarchy,
which uses orders m, m+1 and m+2 and needs new bounds at those orders.
Neither is supplied by a successful second-through-fourth-derivative test
alone. In particular m=2 and m=3 both have index -1, so induction on the
winding magnitude does not separate all spatial multiplicities.

## Control screens and a bounded replay

The [control summary][controls] supplies the relevant distinctions. These
screens test proposed premises; they do not establish an arithmetic gain.

| Control | Consequence for these targets | Premise unavailable from the control |
| --- | --- | --- |
| Quadratic and Hermite heat polynomials | Negative local winding and forward real splitting coexist | Complete theta source and arithmetic coefficients |
| Even quartic threshold model in `lj:quartic` | Positive all-real threshold, double events, mirror equality, and no later events coexist | Complete theta source, infinite zero structure and arithmetic contract |
| Positive-kernel threshold controls q and q_(T,a) | Positive-source heat structure alone cannot force a later witness | Canonical theta arithmetic |
| Weighted-square and finite-prime controls | Selected arithmetic support or finite compatibility permits events | Full reflection and the unchanged complete coefficient data |
| Reflected smooth and positive-primitive controls | Reflection or positive auxiliary channels permit events | The complete normalized theta square expansion |
| Euler-factor modifications | Generic functional and heat identities permit positive thresholds | Unchanged theta arithmetic coefficients |

The unchanged exact polynomial checker was rerun for degrees 2 through 16:
60 rectangle cases and 1573 assertions passed. The small [execution
record][replay] gives its source hash, command and output provenance. It
checks the existing finite index examples; it is neither a new theta
certificate nor evidence for either RH-strength arithmetic implication.
The quartic threshold screen uses its existing closed-form proof, not an
invented numerical event location for any analytic control.

## Subsequent program

The requested [overall program](../research-overview/01_THRESHOLD_BOUNDARY_WINDING_RESEARCH_PROGRAM_20261019.md), [progress register](../research-progress/01_THRESHOLD_BOUNDARY_WINDING_PROGRESS_20261019.md), and [eight sub-investigations](../threshold_routes/README.md) now organize these possibilities. This exploratory note remains their discussion source; its inherited deductions are not upgraded to new arithmetic results.

## Next mathematical question

Start with an ordinary positive threshold event and identify a specific
signed theta observation whose bounds could either erase the required
local winding or force nonzero winding in a later region. Before attempting
an estimate, state the domain, the full source and normalization, the
threshold information actually used, and the strict error margin required.
The first useful outcome can be a restricted estimate or a precise
obstruction; excluding all double threshold events would still leave the
higher-multiplicity question.

[results]: ../../../../../result-summaries/README.md
[indices]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[predecessor]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[polymath]: https://arxiv.org/html/1904.12438v2#S3
[replay]: ../numerics/THRESHOLD_CONTROL_REPLAY_20261019.json
