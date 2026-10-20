# BW-08: imaginary-axis jet bound and BW-01 consumer contract

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**; actual reasoning
effort **max**, verified from the recorded turn metadata.

**Bounded task.** Strengthen the mirror-only deflated fourth-jet bound at
a hypothetical exact double threshold event of the unchanged theta flow,
then transfer it to the critical values on the two time faces in BW-01.
This is a necessary-condition estimate, not an RH-equivalent exclusion
criterion or a numerical search for a threshold event. No speed claim is
proposed. The earlier BW-01 absolute-remainder obstruction stays in force.

Read the [result summaries][results], [local laws][laws], [controls][controls]
and [patterns to avoid][avoid], particularly [target classification][a01],
[control premises][a02] and [scoped conclusions][a07]. The [initial note][initial]
requires a quantitative restriction and a named physical consumer; an
identity by itself does not pass.

## Parameters and complete source

Assume T=Lambda>0, a>=20, H(T,a)=Hx(T,a)=0 and h2=Hxx(T,a)!=0.
All zeros of H(T,.) are real. T and a are hypothetical variables, not
measured events. The source and normalization are exactly those of
[BW-01 Contract 02][source]: H_t=-H_xx, with the complete positive theta
source on [0,infinity). Neither its coefficients nor its time variable
are changed. The classical time-zero identity is
H(0,z)=xi(1/2+iz/2)/8.

The selected nonoscillatory observation is
D_T(b)=partial_b log H(T,ib), b>0. The intended estimate combines its
positive-source monotonicity in T with its exact xi value at T=0, and
compares it with the canonical product at the all-real time T.
The mirror-only comparator is
S_a=h3^2/(9h2^2)-h4/(6h2)>=1/(2a^2).

## Named boundary consumer and payments

BW-01 receives the curve c(t) defined by Hx(t,c(t))=0, c(T)=a, and
v(t)=H(t,c(t))/h2. Its selected boundary observation is
v(T+s)+v(T-s) at the two physical time faces. It must be a signed,
finite-s statement, with an explicit positive range for s; the jets at T
alone are not the delivered consumer. A bound on this pair alone does
not determine winding on the entire boundary.

Use a rectangle |t-T|<=delta<T, |x-a|<=rho<a, and complete upper bounds
B_j for |partial_x^j H|, j=3,...,6. Prove persistence and uniqueness of
the critical curve using a nonzero lower bound for Hxx, and pay the
third time derivative of v using these B_j. The exact complete moments
M_j(T+delta) are admissible bounds. No numerical theta quadrature or
jet acquisition is planned in this task. If illustrating a numerical
implementation, inherit BW-01's N=4,U=1 full-source budget only in its
stated b<1 range, add quadrature/rounding and parameter errors, and
provide the product allowance through order four. Never differentiate
a previously assigned scalar error allowance.

## Frozen checks and acceptance

The coefficient table uses hypothetical heights a=20,100,1000,10000;
none is asserted to contain an event. Compare the explicit new lower
bound with 1/(2a^2). Enclose every displayed logarithm using rational
series and outward decimal rounding, with pi enclosed by Machin's
formula. This table checks the bound's size, not theta jets or RH.

Exact polynomial controls use their own finite sources:

- (z^2-a^2)^2 at a=1 and a=20, including a negative overall multiple;
- (z^2-20^2)^2(z^2-21^2)(z^2-22^2), to test the extra-root term and
  whether a colliding all-real slice can satisfy the new scalar floor;
- the a=1 quartic flow on T=1/4, rho=1/8, delta=1/256, to check the
  finite-time transfer with complete polynomial derivative bounds.

Compute polynomial jets independently from the coefficients and compare
with the exact root sums; compute the critical-value expansion from the
finite heat flow and compare with the derived second/third derivatives.
The full-source theta identity is not assigned to a polynomial. Screen
the other control families analytically against the actual premises;
do not invent numerical thresholds for existence-only constructions.

Pass this bounded task only if the analytic lower bound strictly improves
the mirror bound on a stated interval, and its paid finite-time consumer
is proved. Any surviving collision control must be reported. Failure of
an independent upper estimate to contradict this necessary condition
is an open obligation, not a zero-winding certificate. Higher
multiplicities and a<20 remain outside this task.

Source parent: b39c6cc9b4756bc14c2e500e327169db88571d1f; research setup
and BW-01 additions are uncommitted. The small execution record will hash
this contract, the result note, the checker and the reused source note.

[initial]: 01_INITIAL_RESEARCH_NOTE_20261019.md
[source]: ../../01_local_double_winding/notes/02_PAIRED_FACE_CONTRACT_20261019.md
[results]: ../../../../../../../result-summaries/README.md
[laws]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
