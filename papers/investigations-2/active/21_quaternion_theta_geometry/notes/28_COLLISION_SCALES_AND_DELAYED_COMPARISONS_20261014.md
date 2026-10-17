# Collision scales and delayed comparisons

> **Chat-history routing update, 17 October 2026.** Current histories: [Chat 14 — Review quaternion theta handoff](../chat-histories/0014_2026-10-15T02-29-33Z_review-quaternion-theta-handoff.json). Use this investigation’s [local registry](../chat-histories/index.json) and [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json) for current numbers and preserved provenance; this supersedes the routing and numbering below. All future investigation 21 chats belong in this investigation’s `chat-histories/` folder.

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from this
turn's session metadata. Parallel internal analytic review and independent
exact rational checks support the calculations below. This analysis is
conditional on a hypothetical collision; it supplies no theta counterexample
and no new theta positivity bound.

A finite-order collision has a universal negative pole in its normalized
stationary Laguerre form. The manuscript already proves the pole and its
residue for every multiplicity. This continuation explains that geometry,
computes the finite part, identifies stronger canceling poles introduced by
an earlier-time split, and proves a weaker sufficient criterion allowing
prescribed logarithmic energy losses.

The starting point is [Note 27](27_RESULTS_ASSESSMENT_AND_RESEARCH_PATHS_20261014.md).
The established all-multiplicity statements are the local splitting lemma,
stationary predecessor lemma, bounded-loss theorem and finite collision
criterion in the [manuscript](../manuscript/quaternion_theta_geometry.tex),
labels `fc:hermite`, `fc:predecessor`, `fc:bounded-loss` and
`fc:rh-collision`. [Note 21](21_ONE_SIDED_STATIONARY_ESTIMATES_AND_THETA_PILOT_20261014.md)
supplies the double/cubic controls and source-specific limitations;
[Note 25](25_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_20261014.md) supplies
the actual smooth delay.

## Time orientation and the double collision

Assume H is real analytic, solves H_t=-H_xx, and has a nondegenerate double
zero at (T,x_*), with T>0 and c=H_xx(T,x_*) nonzero. Put s=T-t and
y=x-x_*. Its leading parabolic model is

\[
 H(T-s,x_*+y)=\frac c2(y^2+2s)
   +\text{terms of higher parabolic order}.
\]

Increasing time moves a nonreal conjugate pair onto the real axis at T,
then separates it into two real roots:

| Time | Leading root displacements from x_* |
| --- | --- |
| t=T-s<T | plus/minus i sqrt(2s) |
| t=T | a double root at zero |
| t=T+u>T | plus/minus sqrt(2u) |

The root errors are O(s) or O(u), respectively. For c>0, before the event
there is a positive local minimum. Its height falls because H_t=-H_xx<0.
For c<0 the sign-reversed local maximum rises to zero. In either case the
value and its curvature have the same sign on the predecessor branch.

On the genuine moving branch H_x=0, with s decreasing to zero,

\[
 H=cs+O(s^2),\quad H_{xx}=c+O(s),\quad
 E=H^2=c^2s^2+O(s^3),\quad
 \mathcal L_0=-H H_{xx}=-c^2s+O(s^2).
\]

Thus absolute energy and absolute signed deficit both tend to zero, but

\[
 \boxed{\mathcal L_0/E=-1/s+O(1).}
\]

There is no divergent physical curvature in this generic example. The
singularity belongs to curvature divided by the collapsing amplitude.
A bounded relative loss prevents an extremum from losing all its height
in finite time. An absolute error of order abs(H) permits precisely that
collapse, since abs(H) is of order s whereas E is of order s^2.

## Why the derivative stationary set is also necessary

The exact cubic heat model

\[
 H(t,x)=y^3-6(t-T)y
\]

has, at t=T-s, one real zero y=0 and a nonreal pair
y=plus/minus i sqrt(6s). Here H_x=3y^2+6s is strictly positive on the
real axis, so there is no current stationary point of H before the event.
The first stationary test would see nothing locally.

At the stationary point of H_x, namely H_xx=0 at y=0,

\[
 H=0,\quad H_x=6s,\quad H_{xxx}=6,\quad
 E=36s^2,\quad\mathcal L_1=-36s,
\]

and again L_1/E=-1/s. In fact L_0=3y^4+36(t-T)^2 is nonnegative
everywhere in this model, including at the triple collision. The second
stationary set detects the collapse of the slope at the surviving real
zero. These are exact polynomial controls, not theta examples.

## Every finite multiplicity and its next coefficient

Suppose H(T,.) has exact multiplicity m=2r+j at x_*, with r>=1 and
j either 0 or 1. Set W=partial_x^j H, so W has even multiplicity 2r.
Use collision jets

\[
 A=\partial_x^mH(T,x_*)\ne0,\quad
 B=\partial_x^{m+1}H(T,x_*),\quad
 D=\partial_x^{m+2}H(T,x_*),\quad k=A/r!.
\]

The heat Taylor series is

\[
 H(T-s,x_*+y)=\sum_{p,q\ge0}
 \frac{s^p y^q}{p!q!}\partial_x^{2p+q}H(T,x_*).
\]

After substituting y=s z, the analytic extension of s^(-r) W_x has
value A z/(r-1)!+B/r! at s=0. Its z derivative is nonzero. The
implicit-function theorem therefore gives a real analytic stationary
predecessor

\[
 W_x(T-s,\chi(s))=0,\qquad
 \chi(s)=x_*-\frac{B}{rA}s+O(s^2).
\]

The displacement is O(s), smaller than the O(sqrt(s)) complex-root scale.
Define

\[
 \alpha=\frac{D}{(r+1)A}-\frac{B^2}{2rA^2}.
\]

The next amplitude coefficient is obtained from the three terms containing
D s^(r+1), B s^r y, and A s^(r-1)y^2:

\[
 W(T-s,\chi(s))=k s^r\{1+\alpha s+O(s^2)\}.
\]

Since dW(T-s,chi(s))/ds=W_xx exactly on this branch,

\[
 W_{xx}/W=r/s+\alpha+O(s).
\]

For even m, j=0 and E=W^2 exactly. For odd m, j=1 and the same Taylor
series gives the more precise statement

\[
 H=-\frac{B}{r(r+1)r!}s^{r+1}+O(s^{r+2}),\qquad
 H/H_x=-\frac{B}{r(r+1)A}s+O(s^2).
\]

Thus in the odd case

\[
 E=W^2\left\{1+\frac{B^2}{r^2(r+1)^2A^2}s^2+O(s^3)\right\}.
\]

In both cases,

\[
 \boxed{\frac{\mathcal L_j}{E}=-\frac r s-\alpha+O(s),
 \qquad E\sim k^2s^{2r},\quad
 \mathcal L_j\sim-rk^2s^{2r-1}.}
\]

The pole residue r=floor(m/2), stationary branch displacement and leading
energy asymptotics are already established in the manuscript. The explicit
finite part alpha and odd H/H_x coefficient refine that result here.

For odd m the surviving real zero x_zero(s) has displacement
-B s/((r+1)A)+O(s^2). Explicitly,
chi(s)-x_zero(s)=-B s/[r(r+1)A]+O(s^2), explaining why H is one order smaller than H_x
at the observer. The other local roots are nonreal before T. The local
Hermite splitting of H_x shows that H_x has no real zero nearby on that
side; the first stationary condition is locally absent. These facts concern
a sufficiently small neighborhood of this hypothetical finite event.

One transport distinction matters. With xi(t)=chi(T-t),

\[
 \frac d{dt}E(t,\xi(t))=
 \begin{cases}
 2\mathcal L_0,&h_1=0,\\
 2\mathcal L_1+2\xi' h_0h_1,&h_2=0.
 \end{cases}
\]

The extra odd-branch term divided by E is O(s), because xi' is bounded
and H/H_x=O(s). The exact identity involving only L_1 is
one half the derivative of H_x^2, not one half the moving derivative of E.

## How the prescribed delay redistributes the pole

Keep a=pi/16, b=1/4 and mu=a^2+b^2. At every time v define the complete
residual

\[
 C_j(v,x)=-W_{xx}(v,x)-2aW_x(v,x)-\mu W(v,x).
\]

Only its current value simplifies on W_x(t,x)=0. Earlier stationarity is
never imposed. Thus at the current observation,

\[
 C_j=-W_{xx}-\mu W,\quad
 G_j=C_j(t-\delta,x),\quad
 P_j=WG_j,\quad Q_j=W(C_j-G_j/2).
\]

Let rho_W=W^2/E, equal to 1 for even m and 1+O(s^2) for odd m. Then

\[
 \frac{P_j/2+Q_j}{E}
 =\frac{\mathcal L_j}{E}-\mu\rho_W
 =-\frac r s-(\alpha+\mu)+O(s),
\]

and the exact cancellation implies

\[
 \boxed{\frac{Q_j}{E}=-\frac{P_j}{2E}-\frac r s
                     -(\alpha+\mu)+O(s).}
\]

For the prescribed smooth rule delta=t/[2(1+t log(1+x^2))], the limiting
delay at any finite candidate with T>0 is strictly positive. Write this
limit as delta_* and g=C_j(T-delta_*,x_*). The complete earlier field is
analytic along the observer, so if g is nonzero,

\[
 \frac{P_j}{E}=\frac gk s^{-r}(1+O(s)).
\]

When r>1, the two split products have opposite poles stronger than the
combined 1/s deficit. Their intermediate powers also cancel as required
by the exact identity; keeping only the two most visible powers would
not generally be a valid full expansion.

More precisely, let A_min=(-P_j/E)_+ and B_min=(-Q_j/E)_+ be diagnostic
minimal losses on this known-nonzero branch. These are not admissible
source-defined coefficients for a proof. If r>1 and g is nonzero, then

\[
 A_{\min}/2+B_{\min}\sim\frac{|g/k|}{2}s^{-r},
\]

whereas the combined required loss is r/s+O(1). Any separate nonnegative
loss budgets must be at least these minima. Avoiding magnitudes worse
than 1/s in P_j/E and Q_j/E is equivalent here to
G_j=O(s^(r-1)). A small constant bound for G_j is insufficient.

For a double or cubic collision r=1, put gamma=g/k. Then

\[
 P_j/E=\gamma/s+O(1),\qquad
 Q_j/E=-(1+\gamma/2)/s+O(1).
\]

Retained positivity requires gamma>=0 at leading order; a bounded
absorption loss requires gamma<=-2. No gamma satisfies both necessary
conditions. The endpoint equalities would still require lower-order
checks, but cannot cure this incompatibility.

For diagnostic delays delta/s tending to a finite rho>=0, the leading heat
polynomial instead gives

\[
 P_j/E\sim-\frac{r(1+\rho)^{r-1}}s,
\]
\[
 Q_j/E=\frac{r\{(1+\rho)^{r-1}/2-1\}}s+O(1)
\]

when delta=rho s+O(s^2); for delta/s tending to rho without a rate the
remainder in the second formula is o(1/s). If its displayed coefficient
vanishes, this formula asserts only the cancellation of the leading pole.
For r>1, a large rho can make absorption favorable, but the retained
product carries the deficit. Such delays use the unknown collision time
as a diagnostic scale; they are not a proposed implementable protocol.

## A split can fail even on the favorable side

Consider the exact polynomial H=y^4-12u y^2+12u^2 with u=t-T. At y=0
and u>0,

\[
 E=144u^4,\qquad\mathcal L_0=288u^3>0,\qquad
 C_0=24u-12\mu u^2.
\]

For any fixed 0<delta<T, keeping earlier times positive near the event,

\[
 P_0/E=\frac{2(u-\delta)-\mu(u-\delta)^2}{u^2}
 =-\frac{2\delta+\mu\delta^2}{u^2}
   +\frac{2+2\mu\delta}{u}-\mu,
\]

while Q_0/E cancels the adverse quadratic pole. Exactly,

\[
 P_0/(2E)+Q_0/E=2/u-\mu.
\]

The full stationary Laguerre form is favorable on this branch, yet a
bounded separate retained loss fails as u decreases to zero. The earlier
sample eventually lies across the event. This demonstrates a restriction
introduced by splitting; it is a polynomial control outside the theta
source class. It is not a theta obstruction to the current delay.

## Which enlarged losses still rule out collision

A bound L_j>=-K_j E with K_j locally bounded excludes the universal pole.
The pole also shows that a coefficient integrable in time along the
predecessor branch would suffice: any coefficient admitting the collision
would have to dominate r/s+O(1), whose integral diverges. This is a
branchwise condition; two-dimensional local integrability alone does not
control a stationary curve.

For a prescribed power loss E^p,

\[
 \frac{-\mathcal L_j}{E^p}
 \sim r|k|^{2-2p}s^{2r(1-p)-1}.
\]

A locally bounded coefficient is incompatible with this multiplicity if
p>1-1/(2r). At equality the ratio has finite positive limit
r|k|^(1/r); below it the ratio tends to zero. The leading model therefore
permits those weaker losses. Every fixed p<1 loses this automatic
exclusion for sufficiently high multiplicity. For example:

| Multiplicity | r | Critical power p |
| --- | --- | --- |
| 2 or 3 | 1 | 1/2 |
| 4 or 5 | 2 | 3/4 |
| 6 or 7 | 3 | 5/6 |

There is a useful intermediate class between E and any fixed sublinear
power of E.

**Proposition.** Fix M>0 and a finite q>=0 before evaluating signs. Define

\[
 F_q(e)=e\{1+\log_+(M/e)\}^q\quad(e>0),\qquad F_q(0)=0,
 \qquad\log_+(z)=\max(0,\log z).
\]

Suppose nonnegative K_0,K_1 are locally bounded through every candidate
positive-time collision and, on their corresponding current stationary
sets, satisfy

\[
 \mathcal L_j\ge-K_jF_q(E),\qquad j=0,1.
\]

For the nontrivial analytic theta heat family, these inequalities exclude
all positive-time multiple real zeros in the covered domain. If they cover
the full domain of the manuscript's finite collision criterion, they imply
RH. Covering only a declared subdomain excludes collisions only there,
provided the needed predecessor neighborhoods are included.

**Proof.** Any candidate has finite spatial multiplicity because H(T,.) is
analytic and nontrivial; for theta, H(T,0)>0 guarantees nontriviality. On its
established predecessor branch,

\[
 1+\log_+(M/E)=2r\log(1/s)+O(1),
\]
\[
 \frac{-\mathcal L_j}{F_q(E)}
 =\frac{r}{s\{2r\log(1/s)\}^q}(1+o(1))\longrightarrow\infty.
\]

The last limit follows from exponential growth dominating a fixed power
of log(1/s). It contradicts local boundedness of K_j. No division occurs
at E=0; all quotients in this proof are taken on the known-nonzero
hypothetical predecessor. The separate finite collision criterion supplies
the RH implication. QED.

For q>0 this is an extension of the original sufficient criterion: its
effective coefficient relative to E is unbounded at a collision, so the
old bounded-loss theorem cannot simply be invoked with that coefficient.
The finite-order argument above is the replacement proof. The same
conclusion holds with different fixed finite q and M for the two tests.

Finite-order analyticity is particularly relevant when q>1. Put
beta=1/(q-1). The scalar function y(t)=exp(-(T-t)^(-beta)) for t<T,
extended by zero for t>=T, is smooth and satisfies

\[
 y'=-\beta y\{\log(1/y)\}^q.
\]

For M=1 it satisfies y'>=-beta F_q(y) yet reaches zero. It is not analytic
at T and is not a backward-heat or theta example. It shows why a general
smooth finite-time decay argument alone would not justify the proposition
for q>1.

The nonlinear gauge is prescribed, rather than fitted to observed values.
The unknown theta-specific estimate is still substantive:
F_q(e)=o(e^p) as e tends to zero for every fixed p<1. In particular a
square-root absolute error bound does not imply it. Defining K_j using an
observed adverse quotient or assuming an unknown energy floor would not
establish the proposed estimate.

## Consequences for the next discussion

The local geometry suggests keeping the full signed observation together
near small energy. Separate delayed positivity may demand stronger
cancellation than the collision argument itself needs. Higher multiplicity
provides a useful stress test even if generic double collisions are the
first source of intuition.

The logarithmic-loss proposition opens a potentially easier target than
bounded relative loss, while retaining enough strength to exclude every
finite-order analytic collision. Its usefulness depends on whether actual
theta arithmetic can produce such an estimate. No source estimate of this
kind is established here. The finite height-112 certificate, outer theorem,
and unresolved cusp coverage are unchanged.

## Validation and provenance

The [exact checker](../numerics/check_collision_behavior.py) uses only the
Python standard library. It constructs finite heat polynomials from raw
rational collision jets, independently eliminates two stationary-branch
coefficients, and compares the resulting physical observations with the
formulas above. The [receipt](../numerics/COLLISION_BEHAVIOR_CHECKS_20261014.json)
records 1,072 named assertions over 60 jet cases of multiplicities 2 through
13, double/cubic controls, 30 delay comparisons, and stronger-pole and
power-exponent checks. The finite part is tested using independently formed
Laguerre numerators and energy denominators.

The [internal review](../reviews/20_COLLISION_BEHAVIOR_AND_LOGARITHMIC_LOSS_REVIEW_20261014.md)
separates the analytic arguments from the finite algebra checks. The
logarithmic-limit proposition is proved analytically; the finite checker
does not establish it or analytic branch existence. No theta quadrature,
manuscript revision, commit, tag or snapshot folder is part of this turn.

Reproduce from the investigation's numerics directory:

```sh
python3 check_collision_behavior.py
```

The script writes its deterministic small receipt beside itself. All
permanent files are below 1 MiB. The chat retains formal-replay registration
11 and thread 01a13d64-ba41-7362-acfe-bf5978c84d11; the authorized recorder
captures the actual final reply through the bounded exact-turn workflow.
