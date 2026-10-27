# Unconditioned finite source acquisition at collision scale

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.
Chat0005, **Continue heat-flow research**, thread
`01a17e41-99d3-79c1-b932-2bae84ad0d47`.

**Status: proved in-note conditional finite approximation theorem with
explicit truncation and quadrature bounds; internal same-model checks.
No executed theta interval certificate, excluding source sign, or improved
Newman upper bound.** Unlike [Note09][n09], this construction does not
insert exact low moments or exact event cancellations into its approximant.
It pays their acquisition by shrinking the complete raw source error.
A simple midpoint baseline has large cost; analytic source quadrature
reduces the number of derivative terms to a quantified logarithmic scale.

The source and its majorant are inherited from Note09 and
[Polymath equations (3)-(4)][poly]. Existing shifted finite-mode methods
are in [arithmetic-rigidity Note06][modes]; this is an acquisition and
normalization improvement, with no method-priority claim. Apply the
[result index][results], [controls][controls], [avoid index][avoid],
[classification][a01], [scope][a07], and [coupled-estimate rule][a12].
[Review06][review] records the read-only same-model checks.

## 1. Fixed parameters and a genuinely unconditioned model

Let t_c,a be arbitrary finite real numbers, m>=2, c!=0, and N>=0 an
integer. In the application c=H_z^(m)(t_c,a)/m! at a hypothetical event;
none of the source error bounds below uses H=H_z=...=H_z^(m-1)=0.
Fix rbar>0, S>=4, R>0, and consider real 0<r<=rbar with complex
|s|<=S+1, |w|<=R+1. Put

\[
 T=\max(0,t_c+\bar r^2(S+1)),\quad
 \Theta=|t_c|+\bar r^2(S+1),\quad A=9+\bar r(R+1),
 \quad D=m+N+1,\quad\varepsilon=|c|r^D.                  \tag{1}
\]

Write Phi_K for the first K **unchanged** theta modes. For frequency
cutoff V, node count M, h=V/M and v_j=(j-1/2)h, define the finite field

\[
 G_{r,K,V,M}(s,w)=h\sum_{j=1}^M
 e^{(t_c+r^2s)v_j^2}\Phi_K(v_j)\cos((a+rw)v_j).           \tag{2}
\]

For each fixed r,K,V,M this is an entire heat solution in s,w. Its
definition uses the complete canonical coefficients inside Phi_K, not
event-conditioned Taylor coefficients. The truncation does not preserve
global theta reflection, zero geometry, or the all-real threshold.
Only its proved local approximation will be used.

## 2. Complete frequency and arithmetic-mode tails

For v>=0 each source summand is positive. The inequality
2n^2 e^(4v)>=n^2+e^(4v) gives

\[
 0<\Phi(v)\le C_\Phi e^{9v-(\pi/2)e^{4v}},\quad
 C_\Phi=2\pi^2\sum_{n\ge1}n^4e^{-\pi n^2/2}
 \le \overline C=\frac83\pi^2e^{-\pi/2}.                 \tag{3}
\]

For the last bound, consecutive summands have ratio at most
16e^(-3pi/2)<1/4. This also gives an explicit upper constant rather
than requiring evaluation of another infinite source sum.

Choose

\[
 W=\max\left(1,\frac12\log\frac{4(T+A)}\pi\right),
 \qquad L_V=\frac\pi4 e^{4V}.
\]

For every v>=W, v^2,v<=e^(2v), so Tv^2+Av<=L_v. Hence, on the full
complex buffers, the raw frequency tail satisfies for V>=W

\[
 Q_V:=\int_V^\infty
 e^{(t_c+\bar r^2(S+1))v^2+\bar r(R+1)v}\Phi(v)dv
 \le\frac{\overline C}{4L_V}e^{-L_V}.                    \tag{4}
\]

This follows by bounding the remaining exponent by -L_v and substituting
y=L_v; the factor 1/(4y) is bounded by 1/(4L_V). In particular set

\[
 L_* =\max\left(L_W,1,\log\frac{\overline C}{\varepsilon}\right),
 \qquad V=\frac14\log\frac{4L_*}\pi.                     \tag{5}
\]

Then Q_V<=epsilon/4. The formula remains valid if the logarithm is
negative, and permits a larger convenient V, such as a rational endpoint.
At fixed event parameters

\[
 V(r)=\frac14\log\log(1/r)+O(1)\quad(r\downarrow0).       \tag{6}
\]

For the omitted arithmetic modes let L=K+1>=2. The same source inequality
and the consecutive-term ratio imply

\[
 0\le\Phi-\Phi_K\le C_K e^{9v-(\pi/2)e^{4v}},\quad
 C_K\le4\pi^2 L^4e^{-\pi L^2/2}
       \le4\pi^2e^{-\pi L^2/4}.                         \tag{7}
\]

Here the tail ratio is below 1/2, and 4log L<=pi L^2/4 for L>=2.
A finite bound for its remaining integral is

\[
 B_*:=W e^{TW^2+AW}+\frac{e^{-L_W}}{4L_W}
 \ge\int_0^\infty e^{Tv^2+Av-(\pi/2)e^{4v}}dv.           \tag{8}
\]

Choose an integer

\[
 L\ge\max\left(2,
 \sqrt{\frac4\pi\max\left(0,
             \log\frac{16\pi^2B_*}{\varepsilon}\right)}\right),
 \qquad K=L-1.                                         \tag{9}
\]

The error from these omitted modes on [0,V] is at most C_K B_*<=epsilon/4.
Thus K=O(sqrt(log(1/r))) at fixed parameters. A growing K is only a
controlled source approximation; it supplies no new arithmetic inequality.

## 3. Complete quadrature payments

### 3A. A conservative midpoint baseline

Let S_j(K)=sum_(n=1)^K n^j and put

\[
 C_0=2\pi^2 S_4(K)e^{9V},
\]
\[
 C_1=30\pi^2 S_4(K)e^{9V}
       +15\pi S_2(K)e^{5V}+8\pi^3 S_6(K)e^{13V},
\]
\[
 D_v=e^{TV^2+\bar r(R+1)V}
   [(2\Theta V+|a|+\bar r(R+1))C_0+C_1].                 \tag{10}
\]

These constants bound the v derivative of the retained integrand on
0<=v<=V and on the entire complex s,w buffers. In detail,

\[
 \Phi_n'(v)=
 [30\pi^2n^4e^{9v}-15\pi n^2e^{5v}
                  -8\pi^3n^6e^{13v}]e^{-\pi n^2e^{4v}},
\]

while |t_c+r^2s|<=Theta and |a+rw|<=|a|+rbar(R+1).
The complex sine and cosine are bounded by exp(rbar(R+1)v).
Integrating the Lipschitz error on each midpoint cell gives

\[
 \left|\int_0^V e^{(t_c+r^2s)v^2}\Phi_K(v)
                \cos((a+rw)v)dv-G_{r,K,V,M}\right|
 \le\frac{D_v V^2}{4M}.                                 \tag{11}
\]

Choose M>=max(1,ceil(D_v V^2/epsilon)). This pays epsilon/4 uniformly
on the buffers. Equations (4), (7), and (11) already prove, for the
exact finite field (2), raw error at most 3epsilon/4.

The same **fixed** nodes and coefficients are used for every s,w. This
matters: unrelated adaptive point evaluations do not define a holomorphic
error to which Cauchy estimates can be applied.

### 3B. Analytic source quadrature with exponential convergence

The large midpoint cost is avoidable at the level of approximation
terms. This is a Taylor expansion of the **source integration variable**,
not an expansion conditioned on the event's vanishing jets.
Fix d=1/16. With f(v;s,w) the retained integrand of (11), put

\[
 B_v=e^{\Theta(V+2d)^2+|a|d+\bar r(R+1)(V+2d)}
 [2\pi^2S_4(K)e^{9(V+d)}+3\pi S_2(K)e^{5(V+d)}].          \tag{11a}
\]

For each real center v_0 in [0,V], f is holomorphic on |v-v_0|<=d
and bounded by B_v there, uniformly on the s,w buffers. Indeed
Re(e^(4v))=e^(4Re v)cos(4Im v)>0, so the arithmetic damping has modulus
at most one, even when a disk extends to negative Re v. The other
factors have the displayed bounds.

Partition [0,V] into J=ceil(V/d) cells of length h=V/J and midpoints u_j.
Define

\[
 \mathcal Q_r(s,w)=\sum_{j=1}^J\sum_{k=0}^{q-1}
 \frac{2(h/2)^{2k+1}}{(2k+1)!}
              \partial_v^{2k}f(u_j;s,w).                 \tag{11b}
\]

Integrating the Taylor series through degree 2q-1 gives exactly (11b).
Cauchy on the radius-d disk bounds its pointwise remainder by
B_v(h/(2d))^(2q)/(1-h/(2d))<=2B_v 4^(-q). Therefore

\[
 \left|\int_0^V f(v;s,w)dv-\mathcal Q_r(s,w)\right|
 \le2VB_v4^{-q}\le\varepsilon/4                         \tag{11c}
\]

when q>=max(1,ceil(log(8VB_v/epsilon)/log4)). Every derivative term
in (11b) satisfies the scaled heat equation: differentiation in v
commutes with partial_s+partial_w^2. All nodes, orders and coefficients
are fixed for the annulus. Thus this is another finite analytic heat
model with the same three-quarter raw error budget.

At fixed event parameters, J=O(log log(1/r)), log B_v=
O((log log(1/r))^2), and q=O(log(1/r)). The number of derivative terms
is consequently O(log(1/r)log log(1/r)). Derivative generation, arithmetic
precision, cancellation, and bit complexity are not measured by that
term count; no fast implemented evaluator is claimed.
In particular log B_v contains |a|d: the displayed order grows with
height and supplies no uniformly inexpensive coverage up to exp(C/b).

### 3C. Finite-arithmetic allowance

For numerical use, a further epsilon/4 is reserved for certified
coefficient/evaluation error. A concrete heat-preserving way to implement
the midpoint reference (2) is to absorb the fixed phase into real coefficients

\[
 A_j=h e^{t_cv_j^2}\Phi_K(v_j)\cos(av_j),\quad
 B_j=h e^{t_cv_j^2}\Phi_K(v_j)\sin(av_j)
\]

and use sum_j exp(r^2s v_j^2)[A_j cos(rwv_j)-B_j sin(rwv_j)].
Replacing these coefficients by fixed certified approximations preserves
holomorphy and the heat equation. It costs at most

\[
 \varepsilon_{\rm coeff}\le
 e^{\bar r^2(S+1)V^2+\bar r(R+1)V}
       \sum_j(|\Delta A_j|+|\Delta B_j|).                  \tag{12}
\]

Require this to be <=epsilon/4. Additional error when evaluating the
resulting finite analytic function at a point must still be enclosed at
that point. For (11b), apply Leibniz to the finite v derivatives; the
source derivatives are fixed coefficients multiplying v derivatives of
the heat kernel. Fixed approximations to those source coefficients still
give heat solutions. Their finite weighted error must likewise be bounded
on the buffers by epsilon/4; (12) is the payment for the midpoint reference,
not automatically the same constant for (11b). No interval arithmetic
execution is asserted by writing these allowances.

## 4. Normalized derivatives and the existing energy consumer

For either exact finite model, or its fixed-coefficient implementation
with the corresponding finite-arithmetic allowance paid,
the total raw error on the complex buffers is at most epsilon. Unit
Cauchy buffers then prove for every fixed finite j,ell

\[
 \boxed{\sup_{|s|\le S,|w|\le R}
 \left|\partial_s^\ell\partial_w^j
 \frac{H(t_c+r^2s,a+rw)-G_r(s,w)}{cr^m}\right|
 \le j!\ell! r^{N+1}.}                                  \tag{13}
\]

No low moment has been declared zero in G_r. The earlier debit
sum epsilon_n r^(n-m) is replaced by paying raw accuracy epsilon=|c|r^D
before division. At an event the low jets of the actual field still
vanish; that fact is used to establish its Hermite neighborhood and
conditioning for energy transfer, not to manufacture the approximant.

Once f=H/(cr^m) and g=G_r/(cr^m) satisfy Note09 (15), and
r^(N+1)<=h/2 with its stated wall constant h, its transfer gives

\[
 |I_r-I(G_r)|\le3K_m r^{N+1}.                            \tag{14}
\]

The actual gates, count, |c| and scaled discriminant costs are retained
from Note09. For r_j=2^(-j)r_0 this additional allowance sums to at most
3K_m r_0^(N+1)/(1-2^(-(N+1))). It changes the bounded remainder, not the
logarithmic coefficient. No candidate-exclusion gain is claimed.

V,K,M and coefficient precision are selected for each real r and then
**frozen throughout the annulus and during s,w differentiation**.
There is no claimed holomorphic family in r. Differentiation in r would
produce endpoint and changing-model terms. In particular this approximant
cannot be substituted into Note10's complex-r parity/Cauchy proof without
a new argument; the static transfer (14) is sufficient here.

## 5. Costs, direct first jets, and control screen

The theorem removes an exact-moment input; it does not remove the cost of
resolving a small oscillatory field. It requires raw accuracy proportional
to |c|r^(m+N+1), effective wall/conditioning data for energy, and a fixed
finite m. Formula (10) grows with |a|. The displayed midpoint choice is
very conservative: for the chosen minimal schedules,
M<=r^(-D) exp(O((log log(1/r))^2)) at fixed parameters, after choosing the
least admissible integer. The analytic alternative (11b) has the much
smaller derivative-term count proved above, at the cost of growing source
derivative order and a separately paid coefficient implementation. Neither
construction is an executed moment evaluator or a bit-complexity theorem.

At a fixed candidate event all constants are finite. They need not be
uniform as a,m,|c|^(-1),wall costs or t_c vary. For a slab, t_c<=B allows
the majorant T to be uniform, but this alone supplies no amplitude lower
bound, candidate coverage, or sign margin.

For the direct first-jet consumer one can instead prescribe an absolute
raw tolerance delta and replace epsilon by delta throughout (5),(9),(11).
Cauchy gives |H-G|<=delta and |H_z-G_z|<=delta/r on the physical inner
set. Choosing delta<=min(delta_0,r delta_1) pays arbitrary prescribed
absolute first-jet errors without knowing c or m. This is a finite error
acquisition result. The excluding vector margin remains exactly the
existing [positive-threshold Section 5A][firstjet] obligation. Existing
[HDC Note13][hdc13] and [Note15][hdc15] contain actual compact first-jet
certificates and comparisons; no new compact coverage is asserted here.

The earlier source-Gram alternative is also already screened:
[threshold-jet Note02][gram] proves failure of the homogeneous norm and
finite-Gram relaxation with exact theta Gram entries, and
[Note03][grampos] provides positive continuous controls. Positivity does
not repair that relaxation. Adding the exact mass anchor plus its norm
constraint forces the unchanged multiplier, returning to the physical
signed problem. This return does not reopen that branch.

All heat-polynomial/local analytic controls pass the conditional energy
transfer; they need not have a theta source for that interface. For a
different positive source the raw tail theorems require its **own**
verified majorant, rather than assigning it (3). Euler-factor,
weighted-square, reflected, smooth-shape, positive-primitive,
finite-prime and finite-profile families fail the literal unchanged
theta-mode input in different ways listed in the control register.
That distinguishes the approximation being computed, but **no derived
inequality here rejects their collisions**. RH-conditional endpoint
controls are not unconditional positive-threshold counterexamples.

CE-02 now has an unconditioned finite acquisition theorem including
analytic quadrature costs; effective conditioning, economical evaluation
and any useful arithmetic exclusion remain open. CE-03 reuses its existing
transfer. CE-04/06 acquire no strict saving or new positive slab.
See [Note14][next] for the executable continuation and [the register][progress].

[n09]: 09_COMPLETE_SOURCE_AND_SCALED_ENERGY_TRANSFER_20261027.md
[poly]: https://arxiv.org/html/1904.12438v2
[modes]: ../../../investigations-3/11_arithmetic_collision_rigidity/notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md
[firstjet]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[hdc13]: ../../../investigations-4/12_height_dependent_heat_contours/notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md
[hdc15]: ../../../investigations-4/12_height_dependent_heat_contours/notes/15_COMPLETE_PHYSICAL_CAP_COMPARISON_20261023.md
[gram]: ../../../investigations-3/13_contradiction_analysis/02_threshold_jet_sign/notes/02_EVENT_CONDITIONED_THETA_GRAM_OBSTRUCTION_20261020.md
[grampos]: ../../../investigations-3/13_contradiction_analysis/02_threshold_jet_sign/notes/03_POSITIVE_MULTIPLIER_GRAM_EXTENSION_20261020.md
[review]: ../reviews/06_FINITE_TIME_COMPARISON_AND_SOURCE_ACQUISITION_REVIEW_20261027.md
[next]: 14_SECOND_RETURN_AND_NEXT_CANONICAL_CALCULATION_20261027.md
[progress]: ../research-progress/02_COLLISION_ENERGY_RESEARCH_PROGRESS_20261027.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
