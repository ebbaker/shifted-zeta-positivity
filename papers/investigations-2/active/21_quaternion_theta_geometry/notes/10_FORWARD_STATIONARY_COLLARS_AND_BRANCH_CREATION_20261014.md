# Forward stationary collars and the branch-creation guard

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
The parent session verified these settings in its current recorded turn;
this analytic subtask inherited that session configuration.

[Note 8](8_COMPENSATED_STATIONARY_SIGN_DERIVATION_20261014.md) supplies
strict stationary signs on a closed bounded rectangle. The next time
step need not re-establish the arithmetic cross-term sign independently
on every regular stationary branch: an established strict sign propagates
forward until a branch degenerates or reaches a spatial boundary. This
note gives explicit paid guards against both events. It also gives a heat
polynomial showing why the guards cannot be omitted.

The main result is a conditional continuation theorem; Section 6 derives
one small new theta collar from Note 8's existing paid enclosures. This is
not an all-height estimate. The bounds below concern the complete heat
solution. They do not apply to separate compensated channels without the
residual in Note 8.

## 1. Complete-source constants for a time collar

Let h_k=partial_x^k H and use the genuine positive theta source
w_t(u)=exp(t u^2) Phi(u). Fix 0<=t_0<t_0+Delta<=tau<=1 and define

\[
M_m(\tau)=\int_0^\infty u^m e^{\tau u^2}\Phi(u)\,du.
\]

Normal convergence, positivity, and |sin|,|cos|<=1 give

\[
|h_m(t,x)|\le M_m(\tau),\qquad
\partial_t h_m=-h_{m+2}.
\tag{1}
\]

These constants include every theta index and the whole integration
half-line. An elementary reproducible upper bound is

\[
M_m(\tau)\le 2m!\sum_{n\ge1}
\frac{\alpha_n^2e^{-\alpha_n}}{(4\alpha_n-9)^{m+1}},
\qquad \alpha_n=\pi n^2.
\tag{2}
\]

Indeed phi_n is positive on u>=0 and is at most
2 alpha_n^2 exp(9u-alpha_n exp(4u)); the inequality
exp(4u)>=1+4u+8u^2 bounds its heated exponent by
-alpha_n-(4 alpha_n-9)u-(8 alpha_n-tau)u^2.
Dropping its last nonpositive term and integrating proves (2).
For a finite evaluation through n=N, its remaining positive series is
at most its n=N+1 term divided by 1-rho_N, where

\[
\rho_N=\left(\frac{N+2}{N+1}\right)^4
e^{-\pi(2N+3)}<1.
\tag{3}
\]

The denominator factor in (2) only decreases the successive-term
ratio; the numerator ratio and the exponential give (3). Thus these
moment payments introduce no unpaid cutoff. Tighter validated local
jet bounds can replace (1) in the proposition below.

For m>=1 there is also a convenient entirely rational coarse bound. Put
q=(3/8)^3. The inequalities pi>25/8, pi<22/7 and e>8/3 imply

\[
M_m(\tau)<\widehat M_m:=
2m!\left(\frac{22}{7}\right)^2
\left(\frac27\right)^{m+1}\frac{q}{1-q^3}.
\tag{3a}
\]

In fact 4 pi n^2-9>(7/2)n^2, and the summands in (2) are at most
the displayed prefactor times n^(2-2m) q^(n^2). For m>=1 the factor
n^(2-2m) is at most one, and the sum of q^(n^2) is bounded by q/(1-q^3),
because its consecutive ratios are at most q^3. The rational pi/e
bounds are the same ones used in Note 8; no decimal comparison is used.

## 2. A guarded forward-collar theorem

Fix j in {0,1} and a compact spatial interval [a,b], a<b. At the
base time t_0 suppose a rigorous complete-source slice certificate gives

\[
d_j\le\inf_{x\in[a,b]}
\sqrt{h_{j+1}(t_0,x)^2+h_{j+2}(t_0,x)^2},\qquad d_j>0,
\tag{4}
\]
\[
e_j\le\min\{|h_{j+1}(t_0,a)|,|h_{j+1}(t_0,b)|\},
\qquad e_j>0.
\tag{5}
\]

The stationary roots x_nu of h_{j+1}(t_0,.) in (a,b) are then
finite and regular. Require the strict initial sign at every one:

\[
-h_j(t_0,x_\nu)h_{j+2}(t_0,x_\nu)>0.
\tag{6}
\]

Put B_j=sqrt(M_{j+3}(tau)^2+M_{j+4}(tau)^2). The sufficient
step-size conditions are

\[
\boxed{\Delta B_j<d_j,\qquad
       \Delta M_{j+3}(\tau)<e_j.}
\tag{7}
\]

Then all stationary points in the full closed slab
[t_0,t_0+Delta] x [a,b] lie on exactly the continuations chi_nu(t)
of the initial roots. Every branch remains regular and in (a,b), and

\[
h_{j+1}=0\quad\Longrightarrow\quad
\mathscr L_j=-h_jh_{j+2}>0
\tag{8}
\]

throughout the slab. If there are no initial stationary roots, there
are none in the slab. To propagate both observations, verify (4)--(7)
separately for j=0,1 with a common Delta. In particular the j=0
conclusion alone then excludes H=H_x=0 on this closed slab.

### Proof and quantitative margins

At a fixed x, (1) and integration in time give

\[
\sqrt{h_{j+1}(t,x)^2+h_{j+2}(t,x)^2}
\ge d_j-(t-t_0)B_j>0.
\tag{9}
\]

At x=a,b the corresponding scalar estimate preserves the nonzero
boundary signs by (5), (7). Thus a stationary root cannot become
degenerate, leave the interval, or enter across an edge. The implicit
function theorem continues every initial root; compactness extends its
continuation across the full closed time interval. Conversely a root
at any later time can be continued backward to t_0, because the same
two stopping events are excluded. This proves complete branch coverage,
including exclusion of newly created stationary pairs. Finiteness on the
base slice follows from regularity and compactness, with nonzero edges.

On one such branch put A=h_j(t,chi_nu(t)), C=h_{j+2}(t,chi_nu(t)).
Differentiating the stationary equation and using heat gives

\[
\chi_\nu'=\frac{h_{j+3}}C,\qquad A'=-C,
\qquad C'=-h_{j+4}+\frac{h_{j+3}^2}C.
\tag{10}
\]

The sign s_nu=sgn(C) is constant. At the base time A has sign
-s_nu by (6). The identity A'=-C therefore gives

\[
\frac d{dt}(-s_\nu A)=|C|>0,
\qquad |A(t)|\ge |A(t_0)|=:a_\nu>0.
\tag{11}
\]

In particular A cannot reach zero. On the branch (9) becomes
|C|>=d_j-(t-t_0)B_j. Consequently

\[
\mathscr L_j(t,\chi_\nu(t))
\ge a_\nu\,[d_j-(t-t_0)B_j]>0,
\qquad \mathcal E(t,\chi_\nu(t))\ge a_\nu^2.
\tag{12}
\]

The energy bound holds for both levels: it is H^2 when j=0, and
is at least H_x^2 when j=1. These are lower bounds obtained from a
certified initial amplitude and exact evolution, not quotients by an
unproved physical norm.

There is also an individual curvature guard. From (10),

\[
\frac d{dt}|C|=-s_\nu h_{j+4}
                  +\frac{h_{j+3}^2}{|C|}
\ge-M_{j+4}(\tau).
\tag{13}
\]

Writing c_nu=|C(t_0)|, one may replace the bracket in (12) by the
larger of d_j-(t-t_0)B_j and c_nu-(t-t_0)M_{j+4}(tau).
While the latter is positive, it also gives the drift estimate

\[
|\chi_\nu(t)-\chi_\nu(t_0)|
\le\frac{M_{j+3}(\tau)}{M_{j+4}(\tau)}
\log\frac{c_\nu}{c_\nu-(t-t_0)M_{j+4}(\tau)}.
\tag{14}
\]

The zero-M_{j+4} case uses its continuous limit
(t-t_0)M_{j+3}/c_nu. This individual drift bound can guide moving
spatial tubes; it does not replace the global guard (9) against other
branches appearing elsewhere.

## 3. What the guard costs in a finite certificate

The slice data in (4) can be paid without guessing root locations.
Cover [a,b] by closed intervals. Outside isolated root intervals,
certify |h_{j+1}|>=v_cell>0. Within each root interval, certify
|h_{j+2}|>=c_cell>0 and opposite signs of h_{j+1} at its endpoints.
The latter isolates exactly one root. The minimum of all v_cell and
c_cell is an admissible d_j; the outermost endpoint margins give e_j.
Certified h_j signs on the isolated intervals provide the a_nu in
(12). All these are interval decisions on the complete paid jets.

This reuses the structure of Note 8's root-exclusion and regularity
records. A time grid can refresh d_j, e_j, and the amplitude bounds as
it advances. The step must be strictly shorter than (7); equality is
not a valid guard. A moving spatial interval also requires explicit
edge transversality or edge-sign checks. Overlapping certificates can
instead retain fixed spatial intervals.

The method is deliberately one-sided in time: (11) increases the signed
amplitude forward. A backward step additionally needs an initial
amplitude payment, for example Delta M_{j+2}(tau)<a_nu, because then
the signed amplitude can decrease. No assertion about propagation
through t=0 or an unguarded degenerate stationary point follows.

## 4. A quartic heat control creates a bad stationary branch

The necessity of the birth guard is stronger than the familiar quadratic
and cubic collision controls. Let y=x-a, delta=t-T, A_*>0, and set

\[
Q(t,x)=\frac{y^4}{4}-3\delta y^2+3\delta^2-A_*.
\tag{15}
\]

It satisfies Q_t=-Q_xx exactly. For delta=-h<0, with
0<h<sqrt(A_*/3), the only first stationary point is y=0,
where Q=3h^2-A_*<0 and Q_xx=6h>0. Its first stationary
Laguerre sign is strictly positive. The second stationary set is
empty, since Q_xx=3y^2+6h>0 everywhere.

At delta=0, Q_x=y^3 has a triple stationary root and Q=-A_*;
the derivative-pair gap (4) is zero there. For small delta>0 the
central stationary branch satisfies

\[
\mathscr L_0(Q;t,a)=-6\delta(A_*-3\delta^2)<0.
\tag{16}
\]

The new outer stationary points y=+/-sqrt(6 delta) have positive
first sign. Meanwhile the two second stationary points
y=+/-sqrt(2 delta) have

\[
\mathscr L_1(Q)=48\delta^2>0.
\tag{17}
\]

Thus both strict initial stationary conditions do not themselves
propagate forward through a degenerate stationary event. At the later
time delta=sqrt(A_*/3), Q(t,a)=Q_x(t,a)=0 is a double collision.
Taking T>0 and choosing a in the spatial interval places all these
local events at positive time. This control lacks the positive
integrable theta source. It refutes any claim based only on heat and
initial stationary signs, while satisfying all identities used above.

## 5. Precise continuation value and remaining obligation

For a bounded theta computation, (7) turns verified slice gaps into a
concrete next time collar, and (11) transports the signed amplitude
without another cross-term sign argument. The obstruction is explicit:
a derivative-pair gap can close, or a stationary branch can reach an
unguarded edge. Such events must remain unresolved until paid by a
new local calculation; they cannot be skipped as though they were
physical zero collisions.

At arbitrary heights, the source-moment constants in (1) are absolute,
whereas the slice gaps d_j and e_j can be very small. This theorem does
not make their ratio uniform. A scalable all-height result still needs
source-specific normalized derivative-gap and edge controls, or a
rigorously covered moving-domain family with those payments at every
step. Increasing the number of collars without proving their required
gaps and coverage is not a global RH argument.

## 6. A concrete collar from the existing theta certificate

The replay
[check_forward_stationary_collars.py](../numerics/check_forward_stationary_collars.py)
and its [small exact record](../numerics/FORWARD_STATIONARY_COLLAR_CHECKS_20261014.json)
use the stored outward dyadic endpoints of Note 8's certificate, with its
exact byte hash checked before use. They require no new numerical
quadrature. On each of its 34 cells, expand the retained aggregate
four-jet enclosure by its paid complete-index error. The maximum of
the two distances from zero for jets j+1 and j+2 supplies a lower
bound for the derivative-pair norm; taking the minimum over the cover
gives (4). The first/last cell enclosures supply (5). These full-time
enclosures in particular hold on the base slice t_0=3/50.

The exact rational comparisons give usable floors

\[
d_0,e_0>\frac1{500000},\qquad
d_1,e_1>\frac1{1000000},
\]
\[
a_0>\frac9{100000},\qquad
a_1>\frac3{200000},\qquad
\widehat M_3+\widehat M_4<\frac9{100},\quad
\widehat M_4+\widehat M_5<\frac3{25}.
\tag{18}
\]

Here a_j is the minimum initial amplitude floor among the isolated
stationary branches for that level. The initial branch cells are
[31,32] for j=0 and [9,10], [34,35] for j=1. Their amplitudes and
curvatures have strict opposite signs. The replay also checks the
other cells' original direct or monotone-endpoint exclusions, including
the cells whose broad whole-cell derivative interval contains zero.

Taking Delta=1/200000 satisfies both strict inequalities (7). Hence
the complete-source theorem proves both stationary signs on

\[
[3/50,12001/200000]\times[7,41],
\tag{19}
\]

with no unguarded branch births or entries. More explicitly, (12) and
(18) give, on the respective genuine stationary sets in this collar,

\[
\mathscr L_0>\frac{279}{2000000000000},\qquad
\mathscr L_1>\frac3{500000000000}.
\tag{20}
\]

The corresponding stationary energy floors are 81/10^10 and
9/(4*10^10). Evenness transfers these statements to the reflected
negative-height collar. The small extension illustrates the theorem;
its coarse global moments are not intended to compete with a direct
validated calculation across a much larger time slab.

The replay passes 234 exact checks, including coefficientwise heat and
quotient-free stationary-branch identities for the finite heat evolutions
of every spatial monomial through degree 14, the quartic control, exact
cell coverage, and all stated collar inequalities. It checks the finite
algebra and payments; the analytic proof of branch coverage and source
moment applicability remains the argument in Sections 1--2.
