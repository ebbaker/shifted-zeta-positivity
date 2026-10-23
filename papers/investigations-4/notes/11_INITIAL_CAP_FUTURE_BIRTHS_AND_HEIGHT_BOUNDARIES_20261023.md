# Initial cap integrals and later zero creation

23 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Same-assistant derivation and self-review;
no independent specialist review or priority claim.

**Status: proved in-note, using the explicitly identified Polymath
high-height estimates.** The real angular integral at time zero equals a
late real-zero count minus later births, initial multiplicity excess and
signed wall crossings, plus a bounded endpoint phase. For positive times
bounded away from zero, the canonical wall crossing term has an explicit
logarithmic main term. Moving barriers give a finite bound on all later
positive-height births and a vanishing relative bound after a shrinking
initial time layer. The physical Chern–Hopf cap has a separate compact
product formula below; it is not identified with the real angular integral.

This is the requested first milestone in bounding creation events and
understanding boundary terms, including bounds relative to a growing zero
population. It is not an exclusion theorem. The [result index][results],
[avoid index][avoid], [heat geometry][geometry], [collision controls][controls],
[classification][a01], [coupled estimates][a12] and [distinct targets][a13]
fix the scope. The new quantitative outputs are (8), (11), (15) and (16),
and the exact initial-slice defect in (5); the inherited transport identity
is not counted as a new sign estimate. [Self-review][review] records checks.

## 1. The initial integral and the complete creation balance

Use the unchanged theta field

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad H_t=-H_{zz}.
\]

For a positive endpoint R with H(0,R) nonzero define the real angular cap

\[
\mathcal I_R(0)=\frac1\pi\int_0^R
 \frac{H_x(0,x)^2-H(0,x)H_{xx}(0,x)}
      {H(0,x)^2+H_x(0,x)^2}\,dx.
\tag{1}
\]

At a multiple real zero, use the removable spatial value proved in
Section 2. This definition specifies the integral literally on the
initial slice; it is not an unspecified boundary indentation. It is
twice the real cap B(t) of manuscript equation (4.8), not the localized
Hodge energy or the three-dimensional physical cap of Section 8.

Let T>0. Assume the first jet is nonzero on x=R for 0<=t<=T, the final
real cap is regular, and H(T,R) is nonzero. The canonical field obeys
H(t,0)>0 and H_x(t,0)=0, so the lower wall contributes no crossing or
phase. All sums below are finite on this compact rectangle. Put

\[
\begin{aligned}
N_T(R)&=\#\{x\in(0,R):H(T,x)=0\},\\
\mathcal B_{0,T}(R)&=2\sum_{\substack{0<t<T,\ 0<x<R\\H=H_x=0}}
                  \lfloor m(t,x)/2\rfloor,\\
D_0(R)&=\sum_{\substack{0<a<R\\H(0,a)=0}}(m(0,a)-1),\\
E_0(R)&=-\frac1\pi\arctan\frac{H_x(0,R)}{H(0,R)}.
\end{aligned}
\tag{2}
\]

Here B counts the number of new real zeros produced by interior events.
A double or triple creates two real zeros; an order-m event creates
2 floor(m/2). Let W be the **signed net entry** of real roots through
the right wall. With F(t)=H(t,R), its exact convention is

\[
\mathsf W_{0,T}(R)=\sum_{F(t_j)=0}\operatorname{sgn}H_x(t_j,R)
 \frac{\operatorname{sgn}F(t_j+\eta_j)-
       \operatorname{sgn}F(t_j-\eta_j)}2.
\tag{3}
\]

The small eta_j isolate each crossing; even contacts contribute zero.
At a transverse crossing this is -sgn x'(t_j), so entry from the right
has positive sign. Then the organizing equation is

\[
\boxed{
\mathcal I_R(0)=N_T(R)-\mathcal B_{0,T}(R)-D_0(R)
                       -\mathsf W_{0,T}(R)+E_0(R).}
\tag{4}
\]

The [complete real birth theorem][transport] supplies the heat-event
weights and wall convention. Section 2 proves the remaining initial
endpoint assertion, including when simplicity at time zero is unknown.
Thus the terms in (4) are characterized individually, not hidden in one
unspecified remainder. If the initial roots are simple, D_0=0. Without
that hypothesis D_0 is nonnegative and must be retained.

## 2. The exact correction at a multiple initial zero

For a real analytic f, near a real zero a write f(x)=(x-a)^m u(x),
u(a) nonzero. Away from a put r=f'/f=m/(x-a)+u'/u. Direct cancellation gives

\[
\frac{f'^2-ff''}{f^2+f'^2}=-\frac{r'}{1+r^2}
\longrightarrow\frac1m\quad(x\longrightarrow a).
\]

The quotient extends continuously (in fact analytically) through a.
The principal arctangent of r jumps upward by pi at **each distinct**
real zero, irrespective of m. Integrating on the complementary intervals
therefore proves

\[
\mathcal I_R(0)=N_{\mathrm{distinct},0}(R)+E_0(R),\qquad
\lim_{t\downarrow0}\mathcal I_R(t)=\mathcal I_R(0)+D_0(R).
\tag{5}
\]

For the second identity, the local Hermite splitting theorem gives m
simple real descendants of each initial order-m real zero at small
positive time. There are no other births or wall crossings sufficiently
near zero after isolating the finitely many initial events. The endpoint
phase converges continuously. Applying the regular-cap formula at small
positive t proves (5). Applying the complete birth balance from that t
to T gives N_T=N_distinct,0+D_0+B+W, proving (4).

More locally, the normalized densities in (1) converge distributionally
from positive time to the initial density plus
sum_a (m_a-1) delta_a. To check this without assuming positivity, integrate
-d arctan r against a smooth test: integration by parts leaves bounded
arctangent terms and one unit at each simple root. Dominated convergence
and coalescence of the m roots give the stated atom. This is a specified
one-sided limit, not a universal prescription for an indented Hopf cap.

## 3. Endpoint phases and a bound on the number of events

The endpoint correction is explicit and satisfies

\[
|E_0(R)|<\frac12;\qquad
|E_0(R)|\le\frac{\arctan\rho_R}{\pi}
\ \text{if }|H_x(0,R)/H(0,R)|\le\rho_R.
\tag{6}
\]

At any admissible critical-point endpoint H_x(0,R)=0 it vanishes
exactly. Such a choice at time zero alone does not control the later
wall. On a regular moving wall satisfying H_x=lambda H with fixed real
lambda, the angular wall flux is exactly zero and no root crosses it:
along the wall d arg(H+iH_x)=d arctan lambda=0. Existence of that wall
over the full requested time interval is a separate geometric condition.

There need not be an unrestricted limit of E_0(R) as R grows. The exact
heat solution e^t cos x gives an oscillatory correction. Boundedness is
already useful: relative to a population of size R log R, this term is
O(1/(R log R)). No zero-free amplitude floor is needed for this bounded
arctangent assertion, only a nonzero endpoint for its stated convention.

Let A_0,T(R) be the number of distinct interior creation events. Since
each creates at least two real zeros, A<=B/2. If independently established
bounds give I_R(0)>=L_R, W>=w_R and N_T(R)<=U_T(R), then

\[
\boxed{
A_{0,T}(R)\le\frac{\mathcal B_{0,T}(R)}2
\le\frac{U_T(R)-L_R-w_R+1/2}{2}.}
\tag{7}
\]

One may retain an available lower bound for D_0 and the actual endpoint
phase to improve this allowance. A valid upper may also be rounded down
for the integer event count. This is the precise consumer for future
initial-integral and boundary estimates; a relative bound is an accepted
first target, with sharper absolute bounds a later refinement.

## 4. Canonical fixed-height walls at positive times

**Imported primary source.** D. H. J. Polymath, [Theorem 1.5 and Section 9][poly],
use exactly the normalization above. For 0<t<=1/2 they prove that all
sufficiently high zeros are real and simple, with a threshold exp(C/t),
and that the number C_t(R) of all complex zeros with 0<Re z<R, including
multiplicity, satisfies C_t(R)=g(R,t)+O(1) above that threshold, where

\[
g(R,t)=\frac{R}{4\pi}\log\frac{R}{4\pi}-\frac{R}{4\pi}
       +\frac{11}{8}+\frac{t}{16}\log\frac{R}{4\pi}.
\]

The constants are absolute; their numerical values are not acquired
here. All zeros lie in |Im z|<=1. The proof of Theorem 1.5(i), following
equation (104), gives the stronger localization
|x-x_n(t)|=O(x_n^(-ct)/log x_n), g(x_n(t),t)=n.
This statement, including its logarithmic denominator, is needed below.

Fix 0<delta<T<=1/2. For R sufficiently large relative to delta, every
zero on Re z=R throughout [delta,T] is real and simple. There are no
zeros on Re z=0, since H(t,iy) is the positive cosh integral, or on
Im z=+/-2. Consequently conservation of the complex divisor in this
strip says that the change of C_t(R) is exactly the signed real wall
entry W_delta,T(R). Collisions inside preserve this complex count. Thus

\[
\boxed{
\mathsf W_{\delta,T}(R)=\frac{T-\delta}{16}
          \log\frac{R}{4\pi}+O(1),\qquad
\frac{\mathsf W_{\delta,T}(R)}{N_T(R)}
 =\frac{\pi(T-\delta)}{4R}+o(R^{-1}).}
\tag{8}
\]

Avoid zeros at the two endpoint corners. Only finitely many nonreal
zeros remain at fixed T, so N_T(R) is asymptotic to R log R/(4 pi).
This is a proved relative boundary estimate, not a claim that the
absolute flux vanishes. Subtracting the displayed logarithmic main term
leaves an O(1) remainder, already a second possible normalization.

Here R is height in the H spatial variable, twice the usual zeta
ordinate at time zero. This is a large-height limit at fixed positive
heat times, distinct from the manuscript's large-heat-time clock limit.

The endpoint phase correction has order O(1/(R log R)) on the same
relative scale. Formula (8) concerns the **real spatial crossing term**;
it does not estimate the imaginary-time closures of a physical Hopf cap.

## 5. Moving barriers and a finite budget for future creation

For an integer n sufficiently large relative to delta, define the
positive wall c_n(t)>4 pi by

\[
g(c_n(t),t)=n+\tfrac12,\qquad \delta\le t\le T.
\tag{9}
\]

The implicit function theorem gives a real analytic wall, and exact
differentiation of g gives

\[
c_n'(t)=-\frac{\pi}{4}
 \frac{\log(c_n(t)/(4\pi))}
 {\log(c_n(t)/(4\pi))+\pi t/(4c_n(t))}.
\tag{10}
\]

In particular -pi/4<c_n'<0: the wall moves by less than pi/8 over the
whole time range. This is the speed of a defined barrier, not a claimed
derivative of an uncontrolled root-location remainder.

Choose c_n(delta) comparable to exp(A/delta), where A is a sufficiently
large absolute constant. The stronger localization from Section 4
implies that every high zero has g-coordinate within O(x^(-ct)) of an
integer, uniformly in t>=delta. Enlarge A so this error is below 1/4.
The wall's coordinate is a half-integer, so it is zero-free. Its bounded
displacement keeps it above every event threshold exp(C/t). The vertical
complex wall is also zero-free, since all zeros at this real part are
real. Thus no complex or real root crosses this moving boundary.

The total complex count M inside 0<Re z<c_n(t), |Im z|<2 is constant.
It satisfies M=C_delta(c_n(delta))<=C_1 delta^(-1) exp(A/delta) by the
imported count theorem. Every positive-height real event in (delta,T)
lies inside this boundary. Real births consume this finite population;
they cannot destroy real roots in backward heat time. In particular

\[
\boxed{
\sum_{\substack{\delta<t<T,\ x>0\\H=H_x=0}}\lfloor m(t,x)/2\rfloor
\le\frac M2\le C_2\delta^{-1}e^{A/\delta}.}
\tag{11}
\]

The number of distinct events is at most the left side. If the delta
slice has multiple real zeros, count their real descendants with their
initial multiplicity; alternatively start just after delta and take a
limit. That only reduces the available budget. A possible event at the
final time is excluded by the open interval. No regularity of a chosen
final cap is needed for the upper bound: first stop at regular earlier
times. Nonreal multiple events are not counted by (11).

There is a sharper data-dependent version. Let K_delta be the number
of **nonreal** zeros in the moving finite strip at delta, counted with
multiplicity. Conservation and the real-birth law give

\[
\mathcal B_{\delta,T}=K_\delta-K_{T^-}\le K_\delta\le M.
\tag{12}
\]

When the terminal slice is regular, K_{T^-}=K_T. This keeps an endpoint
event from being inadvertently counted. Subsequent bounds on K_delta
or on the real initial count improve the creation budget directly.

The same budget controls **all later times**. The classical de Bruijn
theorem, recalled in the [primary source][poly], makes every zero real
for t>=1/2. Hermite splitting then rules out any real creation event
strictly after 1/2: such an event would require nonreal roots immediately
before it. Count a possible event at 1/2 using the final real multiplicity,
which includes all its descendants. The same conserved complex population
therefore gives B_delta,infinity=K_delta. All nonreal zeros at delta lie
inside the barrier, so K_delta here is the entire positive-height nonreal
population. Bounds (11) and (14)-(15) consequently also hold for all
positive-height events after delta, with no upper time cutoff.

## 6. A shrinking initial time layer and relative event bounds

For any fixed 0<alpha<1, let R tend to infinity and set

\[
\delta_R=\frac{A}{\alpha\log R}.
\tag{13}
\]

For sufficiently large R, delta_R<T. The barrier construction in
Section 5 now lies at height comparable to R^alpha, and (11) gives

\[
\mathcal B_{\delta_R,T}=O_\alpha(R^\alpha\log R),\qquad
A_{\delta_R,T}=O_\alpha(R^\alpha\log R).
\tag{14}
\]

These count **all positive-height** real births/events in this time
interval, hence also those below R. Since N_T(R)~R log R/(4 pi),

\[
\boxed{\frac{A_{\delta_R,T}}{N_T(R)}
       =O_\alpha(R^{\alpha-1})\longrightarrow0.}
\tag{15}
\]

For example alpha=1/2 gives a relative O(R^(-1/2)) bound after a time
cutoff of order 1/log R. The prefactor A is an unspecified absolute
constant from the imported estimates, not a fitted or certified onset.

At the fixed outer wall R, the same uniform estimates give

\[
\boxed{\mathsf W_{\delta_R,T}(R)
 =\frac{T-\delta_R}{16}\log\frac{R}{4\pi}+O(1),\qquad
\mathsf W_{\delta_R,T}(R)/N_T(R)=O(R^{-1}).}
\tag{16}
\]

The remaining term is the early layer 0<t<=delta_R. Equations (15)-(16)
do not bound its births or crossings; the high-height hypothesis
R>=exp(C/t) is not uniform down to zero. This localizes the next task
to a shrinking interval instead of rejecting relative progress. One may
first aim to bound the early-layer contribution by a specified fraction
of N_T(R), then improve that fraction or its rate.

## 7. Compact expression for the original physical caps

Keep the physical field G=(H,H_z), connection A=Im(G* dG)/|G|^2 and
C=A wedge dA/(4 pi^2). On disjoint regular projective root tubes over
a complex-time rectangle, with a common fixed radius |H/H_z|<=epsilon,
put k=epsilon^2/(1+epsilon^2), h_j(tau)=H_z(tau,z_j(tau)) and

\[
\mathscr D_H(\tau)=\prod_{j=1}^m h_j(\tau).
\]

The inherited exact cap formula then combines into a single expression:
for any oriented heat edge e and the corresponding union of root discs,

\[
\boxed{I(e)=\frac{k}{2\pi}\operatorname{Im}\int_e
                         d\log\mathscr D_H.}
\tag{17}
\]

If H=UP, P=product_j(z-z_j), this product factors exactly as

\[
\mathscr D_H=(-1)^{m(m-1)/2}\,
 \underbrace{\prod_{i<j}(z_i-z_j)^2}_{\Delta_P}
 \underbrace{\prod_j U(\tau,z_j(\tau))}_{\mathscr U}.
\tag{18}
\]

The sign has zero logarithmic differential. Thus both the Vandermonde
phase and the exterior-factor phase enter the same scalar function.
The fixed-radius projective sides vanish. The top, bottom and two
real-time caps are increments of this same logarithm, so they telescope:

\[
I_T-I_{t_0}+J_++J_-=0.
\tag{19}
\]

This is a regular-tube statement. A tube has no event inside it. When
it is attached to an event core, the [complete physical assembly][assembly]
also retains the core, joining complement and chart terms. For a complete
regular event window W the organizing physical equation is

\[
I_{t_0}=I_T+I_{\rm remaining}
       -\sum_{p\in W}\binom{m_p}{2}.
\tag{20}
\]

All other outward faces belong to I_remaining; if an initial event is
on the boundary, first specify and retain its indentation/core. Complex
events and their weights in (20) differ from real births in (4). No
equality of these two initial integrals is asserted. The [existing
closure theorem][closures] shows why the remaining term matters even
when the late projective caps shrink to zero.

The next physical-cap task is to estimate d log D_H with its full unit
factor on a specified high-height complex-time boundary. The real-time
Polymath estimates above do not already supply that complex-time estimate.
This is a focused target, alongside the real early-layer birth budget,
not a requirement that either route immediately exclude every event.

## 8. Controls and next refinements

The shifted heat double x^2-2(t-a) and cubic x^3-6(t-a)x check interior
birth weights 2 and the signs in (4). At a=0 they give D_0=1 and 2;
omitting this term gives a false initial-cap formula. A stationary simple
root crossed by a moving wall checks net-entry sign. The cosine heat
field has oscillatory bounded endpoint correction and no event, while
the root-derivative product retains its nonzero physical cap phase.
[The small check record][checks] is floating diagnostics, not theta
certification; the proofs above do not depend on it.

The generic identities hold for applicable Euler-factor, weighted-square,
reflected and positive-source collision controls. They reject none.
Euler factors change the complete arithmetic source; weighted-square
and finite-prime controls fail full normalized reflection or unchanged
coefficients; reflected/primitive controls fail canonical coefficients;
close RH-conditional endpoint controls fail ordinary Dirichlet-series
arithmetic. The Polymath asymptotics here are imported for the unchanged
theta source, not assigned to any control merely from shared positivity.

The next refinements, in order, are: an early-layer crossing/birth bound
on 0<t<=A/(alpha log R); a useful lower bound for the literal initial
integral in (7); explicit constants/onsets for the positive-time barriers;
and a complex-time estimate for (17)-(18) retaining the complete physical
closures. Relative event bounds are a valid milestone. The full t=0
budget and the physical signed exclusion remain open.

[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[geometry]: ../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../avoid/01_restating_the_target.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a13]: ../../../avoid/13_a_factor_is_not_the_target.md
[transport]: ../manuscript/zero_count_heat_transport/sections/04_zero_transport.tex
[poly]: https://arxiv.org/html/1904.12438
[assembly]: 03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[closures]: ../11_late_heat_caps_and_charge_transport/notes/04_IMAGINARY_TIME_CLOSURE_CONCENTRATION_20261022.md
[review]: ../reviews/03_INITIAL_CAP_AND_HEIGHT_BOUNDARY_SELF_REVIEW_20261023.md
[checks]: ../numerics/INITIAL_CAP_HEIGHT_CHECKS_20261023.json
