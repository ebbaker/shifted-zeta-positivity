# Root-following walls transfer the question to the cap count

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**, actual reasoning
effort **ultra**, verified from the parent turn metadata.

**Status: proved in-note, subject to the [round review][review].** This
is a finite root-transport identity and a scope check on the program's
root-following alternative. It gives no theta exclusion. The [result
index][results], especially [physical indices and walls][topology], and
[avoid index][avoid], especially [target reformulations][a01] and
[scoped conclusions][a07], apply. No novelty priority is asserted.

## Exact cap phase

Let f be real C2 on [u,v], with simple zeros at u and v and exactly N
interior zeros, all simple. Set j=f+i f'. It never vanishes on this
interval: at a zero of f the derivative is nonzero, and elsewhere f is
nonzero. Then the continuous phase increment is exactly

\[
 \Delta_{u\to v}\arg(f+if')=-(N+1)\pi.                 \tag{1}
\]

To prove this, partition at the zeros. Between consecutive zeros f has
one strict sign. If f>0, j stays in the right half-plane, starts on the
positive imaginary axis and ends on the negative imaginary axis. The
unique lift in that half-plane decreases by pi between its endpoints.
For f<0 multiply j by -1, which changes no phase increment. Each of the
N+1 subintervals therefore contributes -pi. Critical points between zeros
need not be counted, and pointwise monotonicity of the phase is not
assumed. There are finitely many zeros under these compactness and
simplicity hypotheses.

## Finite moving-root strip

Suppose the two roots born at an ordinary double event p=(T,a) have been
continued as finite C1 graphs w_-(t)<w_+(t) on [T+eta,T+R], where
0<eta<R. Require H(t,w_±(t))=0 and Hx(t,w_±(t))!=0 on the entire graphs,
and assume the cap t=T+R has only simple zeros between the endpoints.
Choose eta inside the established local splitting neighborhood, so the
bottom endpoints are adjacent real roots. These are existence and
boundary conditions, not consequences of drawing a cone.

Along each wall J=iHx has a constant argument, because Hx keeps its
sign. Equivalently, implicit differentiation gives w'=Hxx/Hx and the
moving-wall numerator is

\[
 H_xH_{xx}-HH_{xxx}+w'(HH_{xx}-H_x^2)=0.             \tag{2}
\]

Orient the strip by dt wedge dx. The top cap runs left to right and has
phase -(N+1)pi by (1); the bottom cap runs right to left and has phase
+pi. Both walls contribute zero. Consequently

\[
 \operatorname{wind}_{\partial S}J=-N/2.           \tag{3}
\]

Integrality shows N is even. Alternatively the opposite endpoint
orientations at the bottom persist on the simple walls, forcing the same
parity. For analytic heat flow with isolated finite interior events, the
physical index theorem then yields

\[
 N=2\sum_{p'\in S,\ t(p')>T+\eta}\lfloor m(p')/2\rfloor.
                                                               \tag{4}
\]

This is also a complete regularized degree calculation: L has nonzero
real part on t>T, so its winding on the truncated strip is zero; a paid
right-half-plane apex patch for Z=J/L fills the removed local piece.
Thus the completed forward root-wall domain has W_Z=-N/2. The usual
small lower neighborhood enclosing the original event adds its index -1,
giving physical winding -1-N/2. This last statement uses index additivity
and a nonvanishing gluing contour, not a claim that an arbitrary finite
lower connector has phase exactly -pi.

## What this does and does not buy

A signed arithmetic proof that the terminal cap contains at least two
extra real roots, while the two walls remain simple and compact, would
force a later event by (3). Merely following roots does not prove that
cap count. If one assumes that the walls remain consecutive, one has
already fixed N=0 and hence W_Z=0. At a hypothetical theta threshold,
future simplicity preserves adjacency whenever these compact root graphs
exist. The missing estimate is therefore an independent arithmetic cap
count that contradicts this inherited root order.

The root implicit-function theorem gives local continuation. On a finite
closed chart, a convergent endpoint with Hx bounded away from zero permits
continuation. Escape from the chart, loss of an a priori derivative bound,
or failure of a numerical tracker does not prove a collision. This note
makes no uniform all-height confinement assertion.

The baseline and this consumer give the *same exact count* when supplied
with the same complete cap/root-order information: G=0. For N=0 the
regularized upper bound is U_base=U_new=0, deficit d=0 and strict margin
delta=0; equality supplies no contradiction. These numbers concern this
analytic information class, not a measured theta estimate or runtime.

## Own-control substitutions

For H=y²-2tau, walls ±sqrt(2tau) contain no interior cap roots: N=0,
W_Z=0, physical winding -1, for either overall sign.

For F(s,y)=y⁴-12sy²+12s²-3, the first event is s=-1/2 and the second
is s=1/2. For s>-1/2 the outer born-root walls are

\[
 w_\pm(s)=\pm\sqrt{6s+\sqrt{24s^2+3}}.
\]

They stay simple through s=1. The bottom just above -1/2 has N=0; at
s=1 the cap has two internal roots ±sqrt(6-3sqrt3), while its outer
endpoints are ±sqrt(6+3sqrt3). Thus N=2, top phase -3pi, truncated
winding -1 and full physical winding -2. This correctly detects the
later ordinary double; s=-1/2 is not the all-real threshold.

The multiplicity-four event y⁴-12tau y²+12tau² does not meet the
ordinary-double born-pair contract. Its physical index -2 is checked
separately in [the exact contour replay][controls-note].

The positive atomic actual-threshold family in [BW-01][atomic] has only
simple future zeros. Select the two adjacent roots splitting from one
isolated event; on any finite compact continuation satisfying this
contract, N=0. Its exact source therefore gives the same zero regularized
winding, despite positive source mass and exact event cancellation.
Euler-factor threshold lower bounds do not identify roots usable as
walls. The weighted-square, finite-prime, reflected and positive-primitive
controls require their own established event and continuation data;
none receives an invented threshold or cap count here. The full premise
screen and unchanged-theta distinctions are in [cluster 12][screen].

**Continuation decision:** retain (1) as an exact cap consumer, but do not
count the root-wall coordinate choice as a sign gain. Resume this
alternative only with a new complete-source estimate of the terminal
root count and paid continuation of the chosen walls. The parabolic
signed-proxy estimate in [Note 01][contract] remains a separate option.

[review]: ../reviews/01_FINITE_CONTOUR_ROUND_REVIEW_20261020.md
[contract]: 01_FINITE_CONTOUR_AND_SOURCE_CONTRACT_20261020.md
[controls-note]: 02_EXACT_CONTOUR_CONTROLS_20261020.md
[atomic]: ../../01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[topology]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[screen]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
