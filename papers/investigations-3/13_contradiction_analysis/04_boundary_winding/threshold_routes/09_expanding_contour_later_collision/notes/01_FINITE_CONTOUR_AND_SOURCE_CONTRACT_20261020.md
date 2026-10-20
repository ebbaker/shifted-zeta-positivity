# A finite contract and the unsigned coupled-remainder obstruction

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**, actual reasoning
effort **ultra**, verified by the parent from recorded metadata.

**Status: proved-in-note scoped obstruction; source feasibility audit.**
The selected attempt to obtain negative regularized degree from an
unsigned disk centered at 1 closes before new theta acquisition. This
does not obstruct a signed source approximation with a nonconstant
center. No theta event or phase inequality is certified here.

Read the [result index][results], [collision controls][controls] and
[avoid index][avoid], particularly [target classification][a01],
[control screening][a02], [scope][a07] and [coupled errors][a12].
The [program][program] supplies the physical index theorem and defines
the later-event target. The obstruction below concerns one estimating
method, not the research route.

## 1. Frozen analytical contract

Use the unchanged complete theta source and physical normalization
\[
 H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,\qquad
 H_t=-H_{xx},\qquad J=H+iH_x .
\]
For this analytical test take
\[
 0<T\le1/5,\quad 1001\le a\le1002,\quad
 H(T,a)=H_x(T,a)=0,\quad h_2\in\mathbb R\setminus\{0\},
 \quad h_3\in\mathbb R.
\]
There is no uniform curvature floor. The left height endpoint is already
excluded on the inherited time slab \(1/100\le T\le1/5\); its inclusion
does not claim a newly feasible event. The hypotheses describe a
hypothetical event class, not a nonemptiness assertion.
For the intended contradiction also assume \(T=\Lambda\), an actual
all-real threshold; the local remainder and disk propositions themselves
do not require that extra hypothesis.

Set \(R=1\), \(c^2=2\), and use the forward domain
\[
 D=\{0<\tau<1,\ y^2<2\tau\},\qquad \tau=t-T,\quad y=x-a.
\]
This is one fixed finite geometry, not a numerical acquisition domain.
The complete source exists on its compact time/space closure
\(t\le6/5,\ |y|\le\sqrt2\). The supported numerical interfaces cited
below do not cover this contract.

Require an isolating neighborhood of the double event, real analyticity
on a neighborhood of the closure, and nonzero \(J\) on both complete
arms and cap away from the apex. For the physical interpretation, assume
finitely many interior multiple events, with their actual multiplicities.
The local jet reference
\[
 L=-h_2\tau+i(h_2y-h_3\tau),\qquad
 c_L=\frac{h_2^2}{\sqrt{2h_2^2+h_3^2}}
\]
satisfies \(|L|\ge c_L\sqrt{\tau^2+y^2}\).
The continuous quotient \(Z=J/L,\ Z(0,0)=1\) is the primary consumer.
Its target is \(W_Z(D)<0\). Orientation is \(dt\wedge dx\): the cap
runs from its negative \(y\) endpoint to its positive endpoint.

The inherited [forward radius][forward] is
\[
 r_*=\min\{1,|h_2|/(16C_3(T)),\sqrt{|h_2|/(4C_4(T))}\},
 \qquad \sigma_*=r_*^2/4 .
\]
Thus \(R=1>\sigma_*\), so this contract extends beyond that particular
certified forward neighborhood. This fact supplies no witness.
All apex radii remain event-dependent. Section 2 gives a complete
analytical apex payment; no independent constant residual is divided by
small \(L\).

## 2. A complete coupled source bound

Put \(w_T=e^{Tu^2}\Phi\), and retain the exact kernel
\[
 K(\tau,y;u)=e^{\tau u^2}\{\cos((a+y)u)-iu\sin((a+y)u)\}.
\]
At the exact event,
\[
 J-L=\int_0^\infty w_T(u)
 [K(\tau,y;u)-K(0,0;u)-\tau K_\tau(0,0;u)-yK_y(0,0;u)]\,du.       \tag{1}
\]
All event cancellations are preserved before taking an absolute value.
For \(A=\tau u^2,\ B=yu\), differentiate \(K(s\tau,sy;u)\) twice
in \(s\). Its real vector is a rotation of
\((A^2-B^2,2AB)\), followed by a diagonal map with norm
\(\max(1,u)\) and the factor \(e^{sA}\). Consequently
\[
 \left|\frac{d^2}{ds^2}K(s\tau,sy;u)\right|
 \le e^{s\tau u^2}\max(1,u)(\tau^2u^4+y^2u^2).                  \tag{2}
\]
Here \(\sqrt{(A^2-B^2)^2+4A^2B^2}=A^2+B^2\); no separate mixed
term is required. Integrating the Taylor remainder against \(1-s\)
and the positive complete source yields
\[
 |J-L|\le\frac12\{M_4\tau^2+M_2y^2\},\qquad
 M_k=\int_0^\infty e^{(T+1)u^2}\Phi(u)u^k\max(1,u)\,du.           \tag{3}
\]
These finite moments include every theta mode and the whole half-line.
They can be replaced uniformly by the moments at \(T+1=6/5\).
Thus \(C=\max(M_2,M_4)/2\) gives \(|J-L|\le C\rho^2\), and
\(\rho\le c_L/(2C)\) implies \(\operatorname{Re}Z\ge1/2\).
If a numerical moment is used, its quadrature and both source tails
must be paid; (3) itself is an exact analytical inequality.

Although (2) improves the triangle estimate containing \(2|\tau y|M_3\),
it is still unsigned. Its proof holds for any nonnegative admissible
cosine source with these complete moments, using that source's own data.
It uses neither integer-square arithmetic nor normalized reflection.
It is an apex certificate and a coupled-envelope improvement, not a
theta-specific sign or a measured winding gain.
With the same complete moments the old and new absolute payments obey
\[
 e_{\rm old}=\tfrac12(M_4\tau^2+2M_3|\tau y|+M_2y^2),\qquad
 e_{\rm old}-e_{\rm new}=M_3|\tau y|.
\]
This exact improvement is in an unsigned remainder allowance; it is not
the program's signed winding gain \(G\).

## 3. What an unsigned relative disk can prove

**Proposition 1 (actual-field statement).** If a continuous, nonzero
boundary field \(Z\) satisfies \(|Z-1|\le1\) everywhere on the closed
boundary, then \(W_Z=0\).

Indeed the disk \(\{|z-1|\le1\}\) lies in the closed right half-plane,
and its only point on the imaginary axis is 0. Nonvanishing therefore
places the entire boundary image in \(\operatorname{Re}z>0\).
The principal argument is a continuous closed lift. Hence any nonzero
degree requires
\[
                 \sup_{\partial D}|J-L|/|L|>1,                 \tag{4}
\]
interpreting the quotient at the apex by its continuous limit.
The strict reverse condition is necessary, not sufficient.

**Proposition 2 (information-class statement).** A consumer supplied
only the pointwise disks \(|Z(s)-1|\le E(s)\), with \(E(s)\ge0\), and
continuity/nonvanishing cannot conclude \(W_Z<0\). The constant boundary
field \(Z=1\) satisfies all those data and has degree 0.

This second assertion is deliberately narrow. The corresponding
\(J=L\) need not be a physical heat jet. The proposition does **not**
discard and then claim to refute retained heat equations, complete
source correlations, or other signed observations. Its role is to
identify what is lost if (1) is collapsed to an unsigned disk.
Derivative correlations do not change that statement unless they
actually exclude the constant candidate.

If (3) proves a relative radius at most 1 on the entire boundary,
both this consumer and the same-data right-half-plane consumer prove
the exact regularized degree 0. In winding units their best upper bounds
are \(U_{\rm base}=U_{\rm new}=0\), \(G=d=\delta=0\). These values are
conditional logical outcomes, not measured theta margins. If the
full-boundary radius test fails, no complete degree upper bound has been
obtained from it; the measurement fields are unavailable, not zero.

## 4. Heat-compatible controls with the exact event jet

For every \(h_2\ne0\) and real \(h_3\), the polynomial
\[
 H_c=h_2(y^2/2-\tau)+h_3(y^3/6-\tau y)                           \tag{5}
\]
solves the heat equation and has the exact prescribed \(h_2,h_3\) at its
double event. If \(h_3=0\), it is the quadratic control. If \(h_3\ne0\),
put \(r=h_2/h_3,\ v=y+r\). Then
\[
 6H_c/h_3=v^3-3(r^2+2\tau)v+2r^3,
 \qquad
 \Delta=108\{(r^2+2\tau)^3-r^6\}.
\]
Since \(r\ne0\), \(\Delta>0\) for every \(\tau>0\), equals 0 at
\(\tau=0\), and is negative immediately before 0. The actual all-real
threshold is therefore \(\tau=0\); there is no later multiple event.
Its sole real-time discriminant zero is at 0. Its coupled remainder is
\[
 J_c-L=h_2y^2/2+h_3(y^3/6-\tau y)+i h_3y^2/2.                    \tag{6}
\]
Thus any proposed disk data that dominate the modulus of (6)
pointwise also admit a physical heat jet with precisely the selected
event jets and zero regularized degree. No theta moments are assigned
to this polynomial. It screens heat/event/jet-only claims.

For the quadratic on a general forward cone
\(0<\tau<R,\ y^2<k\tau\), its exact maximum boundary relative
remainder is
\[
 E_{\rm quad}(k,R)=\frac{k\sqrt R}{2\sqrt{R+k}}.                  \tag{7}
\]
The arm expression increases with \(\tau\), and at fixed cap time the
expression \(y^2/(2\sqrt{R^2+y^2})\) increases with \(|y|\), proving
(7). If \(k\le2\), it is strictly below 1 for all finite \(R\).
If \(k>2\), it exceeds 1 exactly when
\[
                       R>\frac{4k}{k^2-4}.                    \tag{8}
\]
Nevertheless \(W_Z=0\) for every \(k,R>0\). For the selected \(k=2,R=1\),
\(E_{\rm quad}=1/\sqrt3\). Overall sign changes do not alter these
ratios or degrees. This pays the own-polynomial control rather than
rejecting it solely for lacking a theta label.

Positive atomic actual-threshold and finite-profile controls also admit
the source remainder (1) and their own version of (3); none is forced
to have negative degree by those facts. Euler-factor controls must use
their own source and an actually supplied event; a threshold lower bound
is not an event. Weighted-square, finite-prime, reflected and
positive-primitive controls share (1) at their admissible local events
but do not receive a finite all-real threshold without a separate proof.
Their missing complete theta coefficients or reflection premises are
as catalogued in [cluster 12][controls]. Smooth-density or two-channel
auxiliary positivity alone supplies no event contract. No unrecorded
numerical parameters are assigned to any control.

## 5. Existing source feasibility and the surviving estimate request

The [sixth-derivative interface][interface] is justified on
\([1/100,1/5]\times[25,45]\), including its stated complex strip.
Its validation event box is already empty by its first component.
Neither it nor its residual number transfers to height \([1001,1002]\).

The [high-height interface][high] supplies components 0–2 on
\([1/100,1/5]\times[999,1001]\). With its center \(x=1000\),
degree 24 and bound \(M_{52}/G_*<9.632889\,10^{10}\), spatial distance
2 alone produces a Taylor allowance about \(2.08\,10^{-7}G_*\),
before the other payments. This is not its inherited
\(2.165\,10^{-12}G_*\) allowance. Extending to \(a=1002\), adding
components 3–6, or using the present cap at \(T+1\), requires new
domain/derivative/phase-gap verification. In particular the tempting
small event test \(T=1/10\pm10^{-6},a\in[1001,1002]\) is not covered
by the cited sixth-order source receipt.

**Subsequent bounded subcase.** [Note 04][event-gate] revalidates the
inherited high-height **first-jet** cache on precisely that small box
and certifies \(H>4.1345\,10^{-4}G_*\) throughout it. The event class
there is empty. That restricted value exclusion does not validate
sixth derivatives on the box or the present cap at \(T+1\), and
does not supply the signed estimate requested below.

The closed attempt is obtaining negative degree by improving only (3).
No quadrature is justified for that goal. A changed, concrete request is:
retain a **nonconstant signed proxy** for the full coupled remainder.
For fixed \(N,U\), let \(Q_{N,U}\) be (1) with its single bracket
retained, modes \(1,\ldots,N\) and \(0\le u\le U\). Define
\[
 P=L+Q_{N,U},\qquad Z_P=P/L,\qquad Z_P(0,0)=1.
\]
The full omitted-source remainder has the same quadratic vanishing:
\[
 |J-P|\le B_{\rm tail}(\tau,y)
 =\tfrac12(M^{\rm tail}_4\tau^2+M^{\rm tail}_2y^2),               \tag{9}
\]
where the tail moments cover the union of omitted modes and the
retained modes beyond \(U\), with no double counting or omission.
The theta mode terms are nonnegative for \(u\ge0\).

The actual next estimate request is a complete, finite proof of
\[
 W_{Z_P}=-1,\qquad
 B_{\rm total}(\tau,y)<|P(\tau,y)|\quad
       \hbox{on every boundary point away from the apex},       \tag{10}
\]
plus the common apex extension. Here \(B_{\rm total}\) includes (9),
quadrature, arithmetic, retained-approximation errors, full parameter
uncertainty, and propagation. A finite approximant must preserve the
coupled bracket or separately pay its apex vanishing; independent
constant error disks are invalid there. The complete first-jet event
gate comes first. No value for \(N,U\), sign, or successful margin in
(10) has been acquired.

The matched direct baseline uses the **same** \(P\) and total error:
\[
 |Z-Z_P|<|Z_P|
       \quad\Longleftrightarrow\quad |J-P|<|P|.                  \tag{11}
\]
Division by \(L\) gives no stronger homotopy-separation test on its own.
The direct baseline uses a punctured apex and the paid initial index;
the regularized implementation uses its continuous apex. A useful gain
must therefore come from an improved signed source proxy or correlated
error, with the same-data baseline recomputed, rather than from the
division or the zero-centered tail bound. Equation (10) is an explicit
future estimate request, not a claimed theorem about theta.

A second concrete signed acquisition could use
\[
 A=-h_2\tau H+(h_2y-h_3\tau)H_x,\qquad
 B=(h_3\tau-h_2y)H-h_2\tau H_x,\qquad
 Z=(A+iB)/|L|^2.                                                \tag{12}
\]
In particular \(B\) is one complete source observation with kernel
\[
 e^{(T+\tau)u^2}\Phi(u)
 \{(h_3\tau-h_2y)\cos((a+y)u)+h_2\tau u\sin((a+y)u)\}.
\]
When every negative-real-ray crossing is simple, its full boundary
degree is \(-\sum\operatorname{sign}(dB/ds)\), summing precisely the
crossings \(B=0,A<0\) in positive boundary orientation. A certificate
must locate and separate every such crossing, control its derivative,
exclude additional crossings on the remaining arcs, and pay the apex.
For the quadratic \(H=y^2-2\tau\), \(B=-2y^3\); every non-apex
boundary point with \(B=0\) has \(A=4\tau^2>0\). It has no
negative-ray crossing even when (7) exceeds 1. Thus (12) retains a
signed observation absent from the failed disk test; neither its
complete theta crossing data nor a negative crossing count is acquired.

[program]: ../research-overview/01_EXPANDING_CONTOUR_RESEARCH_PROGRAM_20261020.md
[forward]: ../../05_later_laguerre_violation/notes/02_QUANTITATIVE_FORWARD_NEIGHBORHOOD_EXCLUSION_20261020.md
[interface]: ../../../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/15_COMPLETE_FOURTH_ORDER_INTERFACE_20261020.md
[high]: ../../../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/12_HIGH_HEIGHT_SIGNED_CONSUMER_AND_MATCHED_COMPARISON_20261018.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[event-gate]: 04_BOUNDED_THETA_EVENT_GATE_20261020.md
