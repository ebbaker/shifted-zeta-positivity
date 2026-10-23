# Critical amplitude growth and propagated physical Laguerre floors

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, confirmed by the root research turn.

**Status: proved in-note under the declared real Laguerre--Pólya heat
regime, with an effective event-conditioned canonical-source application.**
The critical amplitude is convex in physical heat time, and the minimum
of the physical Laguerre numerator on a continued adjacent cap is
nondecreasing. A source-controlled ordinary-event chart therefore pays
an explicit lower numerator and physical jet-amplitude floor. This
removes the need to assume the corresponding floor separately in RHE
Note 11. It does not supply an event-independent lower curvature, RH,
or a collision exclusion.

Read the [result index][results] and [avoid index][avoid], particularly
[controls][controls], [criterion classification][a01], [scope][a07],
[known-forced signs][a11], and [coupled terms][a12]. The known Laguerre
signs are inputs, not the milestone. The new estimating outputs are the
quantitative amplitude, full-cap, and physical-jet lower bounds below.

## 1. Precise real heat regime

Let `H(t,z)` solve `H_t=-H_zz`, be holomorphic in the spatial variable
and sufficiently differentiable jointly for the derivatives used below.
Assume that, on an interval of real times, each spatial slice is a real
Laguerre--Pólya (LP) entire function. Let `a(t)<b(t)` be continued
consecutive simple real zeros. Write

\[
 h_j=\partial_z^jH,\quad
 Q=h_1^2-h_0h_2,\quad E=h_0^2+h_1^2
 \qquad\text{on the physical real line}.               \tag{1}
\]

The existing paired product under RH supplies this regime for the
canonical field at positive times; see [BW10 Note 19][bw19]. The theorem
is also valid for other LP heat fields with their own normalization.
There is no assertion that source positivity alone gives this regime.

We use these elementary consequences of the real-zero product:

* `Q>0` throughout a simple adjacent-root cap, including its endpoints.
* Each derivative of an LP function is LP, so
  `h_2^2-h_1 h_3>=0` and `h_3^2-h_2 h_4>=0` on the real line.
* If a nonzero LP function `F` has at least one real zero, then at every
  real point where `F` is nonzero,
  `(F')^2-FF''>0`. Indeed division by `F^2` gives the nonnegative
  Gaussian term plus the sum of squared reciprocal distances to all
  real zeros, and at least one term is positive.

In particular `H'` has a zero inside the selected cap by Rolle's
theorem. This supplies the strict inequality needed below and excludes
the irrelevant zero-free exponential exception. No unproved lower
root gap is being inserted into that strictness statement.

## 2. Convex critical amplitude and its exact growth lower

There is a unique critical point `c(t)` in the cap. Off the zeros,
`(H'/H)'=-Q/H^2<0`; the quotient runs from positive to negative infinity
across the gap. At its unique zero, `H''` is nonzero. Thus `c(t)`
continues differentiably, and in an analytic heat family it is analytic.
Put `V(t)=H(t,c(t))`. Its sign is constant while this cap continues.

The critical-point equation and heat equation give exactly

\[
 c'=\frac{h_3}{h_2},\qquad
 V'=-h_2,\qquad
 V''=h_4-\frac{h_3^2}{h_2}
     =-\frac{F}{h_2},\qquad
 F=h_3^2-h_2h_4\ge0,                                 \tag{2}
\]

with jets evaluated at `c(t)`. Since `Q(c)=-Vh_2>0`, the signs of
`V` and `h_2` are opposite. Hence

\[
 \boxed{\frac{d^2}{dt^2}|V(t)|\ge0.}                  \tag{3}
\]

Now suppose this cap is born from an ordinary double at `(T_0,x_*)`:
`H=H_z=0`, `h_2^0=H_zz(T_0,x_*)!=0`. Write `s=t-T_0>0`.
The local ordinary chart shows `V(T_0)=0` and
`V'(T_0+)=-h_2^0`. Convexity and the tangent-line inequality give,
for the entire subsequent continuation of this cap within the declared
LP regime,

\[
 \boxed{|V(t)|\ge |h_2^0|s,\qquad
        |V'(t)|\ge |h_2^0|.}                          \tag{4}
\]

In particular the critical value is nonzero for every positive `s`.
At the critical point the physical numerator obeys

\[
 \boxed{Q(t,c(t))=-Vh_2=|V||V'|
                         \ge |h_2^0|^2s.}            \tag{5}
\]

One also has `q=V'/V=(log|V|)' >=1/s`, because a convex positive
function vanishing at zero satisfies `s(|V|)' >= |V|`. This is a lower
endpoint budget, consistent with the compulsory logarithm. It is not
the strict subunit upper budget sought by the critical-wall program.

The mixed-jet identity in (2) already appears in [I4/10 Note 01][ch01];
[I4/10 Note 02][ch02] records the known LP sign of `F`. The quantitative
global continuation consequences (3)--(5), rather than reacquisition of
that sign, are the present output. No new arithmetic sign is claimed.

Critical control alone is insufficient for a full-cap floor:
`Q_x(t,c)=-Vh_3` need not vanish. The minimum of `Q` need not occur at
the critical point. The following separate argument addresses that gap.

## 3. The full-cap minimum propagates forward

**Theorem.** On every interval where the hypotheses in Section 1 hold,

\[
 m(t):=\min_{a(t)\le x\le b(t)}Q(t,x)
 \quad\text{is nondecreasing}.                       \tag{6}
\]

**Proof at an interior minimizer.** Here `h_0!=0` and

\[
 Q_x=h_1h_2-h_0h_3=0,\qquad h_3=h_1h_2/h_0.
\]

The first derivative's LP inequality therefore reads

\[
 h_2^2-h_1h_3=-\frac{h_2}{h_0}Q\ge0.                \tag{7}
\]

Since `Q>0`, this gives `h_2/h_0<=0`. In fact `h_2` cannot vanish.
If it did, the stationary equation would give `h_3=0`, and
`Q=h_1^2>0` would give `h_1!=0`. But `H'` is LP, is nonzero at this
point, and has at least one real zero inside the cap. Its strict
logarithmic-derivative inequality would give
`h_2^2-h_1h_3>0`, a contradiction. Thus `h_2/h_0<0`.

Use the LP inequality for `H''`,
`h_2h_4<=h_3^2`. Multiplication by the **negative** ratio `h_0/h_2`
reverses its direction:

\[
 h_0h_4\ge\frac{h_0h_3^2}{h_2}
             =\frac{h_1^2h_2}{h_0}.
\]

The heat equation gives

\[
 Q_t=h_2^2-2h_1h_3+h_0h_4
 \ge h_2^2-\frac{h_1^2h_2}{h_0}
 =-\frac{h_2}{h_0}Q>0.                              \tag{8}
\]

This is an estimate at spatial minimizers, not a claim that `Q_t>=0`
at every real spatial point. The latter claim is false in general.

**Proof at a moving endpoint.** At a simple root `r(t)`,
`r'=h_2/h_1`. Since `Q(t,r)=h_1(t,r)^2`,

\[
 \frac d{dt}Q(t,r(t))
 =2(h_2^2-h_1h_3)(t,r(t))\ge0.                        \tag{9}
\]

Both moving walls are therefore included; they cannot be treated as
fixed spatial points when differentiating the minimum.

**Multiple minimizers and passage to the minimum.** Fix a compact
time interval inside the simple-root regime. Map the moving cap to
`0<=y<=1` by `x=a(t)+(b(t)-a(t))y`, and call the resulting smooth
function `G(t,y)`. It and its time derivative are uniformly continuous
on that compact rectangle. Its minimum `m(t)` is locally Lipschitz.
At an active interior minimizer, `G_t=Q_t`, because `Q_x=0`; at either
active endpoint `G_t` is (9). Thus every active minimizer has `G_t>=0`.

For `h>0`, choose any minimizer `y_h` at time `t+h`. Then

\[
 m(t+h)-m(t)\ge G(t+h,y_h)-G(t,y_h).
\]

Every convergent subsequence of `y_h` has a limit that minimizes
`G(t,.)`. Uniform differentiability in time therefore proves that the
lower right Dini derivative of `m` is nonnegative. Equivalently, at
almost every differentiability time its derivative is nonnegative.
Local Lipschitz continuity and absolute continuity give (6). This
handles arbitrary ties between minimizers and the two moving walls.

## 4. A complete source-controlled initial floor

Use the canonical ordinary-event chart of [RHE Note 01][rhe01] and
the manuscript, translated to `(T_0,x_*)`. Set `A=h_2^0/2`, and
`f_s(x)=H(T_0+s,x_*+x)/A`. On the full real cap, for
`0<s<=sigma`, the paid chart gives

\[
 \frac32\le f_s''\le\frac52,\qquad
 f_s'(k(s))=0,\qquad f_s\le0.
\]

For the RH-to-simplicity application the relevant hypothetical ordinary
event is at `T_0=0`; positive-time simplicity under RH is already an
inherited classical input. No new positive-time canonical double is
being alleged.

Write `y=x-k(s)`. Integration of the curvature lower gives
`|f_s'(x)| >=3|y|/2`. Taylor's theorem with the upper curvature gives

\[
 -f_s(x)\ge-f_s(k)-\frac54y^2.
\]

The LP convex amplitude bound (4) improves the local critical value
to `-f_s(k)=|V|/|A|>=2s`. Since `-f_s>=0` on this cap,

\[
 \begin{aligned}
 Q/A^2&=f_s'^2+(-f_s)f_s''\\
 &\ge\frac94y^2+\frac32\left(2s-\frac54y^2\right)
 =3s+\frac38y^2.
 \end{aligned}
\]

Thus an actual complete full-cap floor has been derived:

\[
 \boxed{m(T_0+s)\ge\frac34|h_2^0|^2s
                  \qquad(0<s\le\sigma).}             \tag{10}
\]

The lower bracket for `-f_s(x)` may become negative near an endpoint;
the inequality remains valid there because the preceding use of
`f_s''>=3/2` was made against the actual nonnegative `-f_s`.

Without the LP amplitude improvement, the original chart only supplies
`-f_s(k)>=3s/2`. The same calculation gives the useful but weaker
`m>=9|h_2^0|^2s/16`. This identifies exactly where the additional
all-real LP information improves the constant.

Combining (6) with (10) now gives, for the full subsequent continued cap,

\[
 \boxed{q_*(t):=\frac34|h_2^0|^2\min(t-T_0,\sigma)
       \le Q(t,x)\quad(a(t)\le x\le b(t)).}           \tag{11}
\]

No new minimum has to be assumed or reevaluated at each later time.
The source enters through the original event curvature and the complete
moment-derived `sigma`; the LP regime supplies propagation. Formula
(11) is not height uniform, and neither existence nor numerical values
of a hypothetical canonical double event are asserted.

## 5. A derived physical jet-amplitude lower

On a declared real time window, take the complete-source upper

\[
 M_2\ge\sup |H_{xx}|.
\]

For the canonical source on `|t|<=S`, one may use
`M_2=integral_0^infinity u^2 exp(Su^2)Phi(u)du`, with all mode/ray
tails already paid by the manuscript. On the physical cap,

\[
 q_*\le Q=H_x^2-HH_{xx}\le E+M_2\sqrt E.
\]

Solving this scalar quadratic gives the explicit lower

\[
 \boxed{|J(t,x)|=\sqrt E\ge j_*(t):=
 \frac{\sqrt{M_2^2+4q_*(t)}-M_2}{2}
 =\frac{2q_*(t)}{\sqrt{M_2^2+4q_*(t)}+M_2}>0.}        \tag{12}
\]

The rationalized expression is preferable for interval acquisition.
This is a derived physical jet floor; no original jet floor was assumed.
Near the ordinary birth it has the necessary order `s`, and `E>=j_*^2`
has order `s^2`. Its constants can be much smaller than a locally
acquired floor; no numerical advantage is claimed.

The RHE Note 11 transfer now has a paid event-conditioned denominator:
with its `B,W,d,C,J_4`,

\[
 \boxed{|R_\eta(t)|\le
       \frac{\pi\eta^2J_4}{6q_*(t)}.}                \tag{13}
\]

This prices the necessary inverse-time cost through (11), rather than
postulating a nondegenerating `q_*`. For any finite later interval,
(11)--(12) also provide a floor for complete source/grid error budgets
and for the signed amplitude-weighted trace. The equally informed
direct estimator receives the same floors and transfer.

Every occurrence of `|h_2^0|` can be replaced by a separately paid
positive canonical curvature lower `h_*`. [Note 12](12_CANONICAL_ANCHORS_AND_ISOLATED_EVENT_FLOORS_20261022.md) supplies explicit choices from a normalized real-root product and complete count/tail bounds, or from a zero-free deflated unit, higher source moments and Harnack without RH. Both retain their declared root-isolation distances. The present
argument does not infer that curvature lower from an absolute upper
moment or from the known LP signs. If the actual event curvature is
unknown, (11) is an explicit event-conditioned estimate, not an
acquired numerical all-height floor.

The [internal review](../reviews/07_CANONICAL_AMPLITUDE_AND_BULK_LOWER_REVIEW_20261022.md) records separate same-model proof audits. The [canonical mass lower](14_CANONICAL_BULK_MASS_LOWER_BOUND_20261022.md) is an independent signed-trace input, not a pointwise physical-jet floor.

## 6. Controls, duplication screen, and stopping boundary

For the exact quadratic `H=A(z^2-2s)`, `|V|=|h_2^0|s`,
`Q_min=|h_2^0|^2s`, and the critical amplitude and critical numerator
bounds (4)--(5) are equalities. The full-cap bound (10) loses only its
declared coarse-chart constant. Thus these amplitude lower bounds are
compatible with a collision; they do not oppose its local heat law.

LP polynomial and Hermite heat controls satisfy the new theorems with
their own constants. Under its declared RH hypothesis, an Euler-factor
control has the same analytic propagation but changed arithmetic.
Weighted-square/finite-prime or positive-source controls may fail the
all-real LP regime; only the local event-chart part without the LP
improvement is then available. Reflected/primitive controls are not
assigned an all-real LP slice without proof. The separate preservation
lists of [cluster 12][controls] remain in force.

The duplication screen found the critical identities and local signed
budget in I4/10 Note 01, and the known LP sign/finite stopped tail-moment
pilot in I4/10 Note 02. The present work neither reruns that pilot nor
counts the known sign as new. The gain is its quantitative amplitude
consequence, the minimum principle over the moving cap, and the
source-effective floors (11)--(12). No new source-arithmetic inequality,
excluded height, or simplicity theorem has been obtained.

The remaining obstacle is precise. An event-independent canonical
lower for the unknown curvature, or a complete additional arithmetic
estimate that conflicts with the allowed positive-time growth, remains
unproved. These results make an existing denominator payment explicit;
they do not remove its compulsory endpoint scale.

[rhe01]: 01_FINITE_COVER_CONTRACT_AND_ENERGY_ENCLOSURE_20261022.md
[bw19]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[ch01]: ../../10_chern_hopf_integral_estimates/notes/01_ESTABLISHED_MASS_TRACE_AND_AMPLITUDE_RESULTS_20261022.md
[ch02]: ../../10_chern_hopf_integral_estimates/notes/02_COUPLED_SIGNED_THETA_TAIL_ESTIMATES_20261022.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
