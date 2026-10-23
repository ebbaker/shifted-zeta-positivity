# Transferring derivative-weighted area to the signed physical tube

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, confirmed by the root research turn.

**Status: complete analytic transfer with explicit collar and physical
Laguerre-floor costs; sharp scoped obstructions to removing those costs.**
The area bound from [RHE Note 08][rhe08] supplies a finite bound for the
BW10 transverse trace remainder after an additional physical denominator
payment. It does not supply that payment. A raw line trace of the area
density is infinite even at a simple real zero. The exact quadratic
control shows that bounded weighted area cannot by itself uniformly
bound the BW10 remainder near an ordinary collision.

Read the [result index][results] and [avoid index][avoid], particularly
[controls][controls], [criterion classification][a01], [scope][a07],
[normalization][a08], and [complete coupled estimates][a12]. The result
is an explicit estimate and a scoped information limitation. It is not
a new simplicity criterion or a theta collision exclusion.

## 1. The consumer and the area data

Fix one real heat time. Write `H=H(t,.)`, `h_j=H^(j)`, and suppose
`a<b` are consecutive simple real zeros. On the real interval put

\[
 E(x)=H(x)^2+H'(x)^2>0,\qquad
 Q_0(x)=H'(x)^2-H(x)H''(x).
\]

Let

\[
 Q(x,v)=|H'(x+iv)|^2-
         \operatorname{Re}(H(x+iv)\overline{H''(x+iv)}).
\]

For a positive tube thickness `eta`, [BW10 Note 21, MT12][bw21]
gives the exact signed remainder

\[
 R_\eta=\int_a^b\frac{dx}{E(x)}
 \int_0^\eta\frac{(\eta-s)^2}{2\eta}\,Q_{vv}(x,s)\,ds,
\qquad
 Q_{vv}=3|H''|^2-4\operatorname{Re}(H'\overline{H'''})
                  +\operatorname{Re}(H\overline{H''''}). \tag{1}
\]

The physical cap itself has integral `integral_a^b Q_0/E=pi`.
That signed winding fact does not provide a positive lower bound for
`Q_0`; a floor used below is a separate paid input. All transverse
points of (1) lie in

\[
 K=[a,b]+i[0,\eta].
\]

Choose a bounded spatial domain `Omega` such that every point of `K`
has a radius-`d` disk contained in `Omega`, with `d>0`. Assume `H` is
holomorphic near its closure and is not identically zero. The data are

\[
 B\ge\sup_\Omega|H|,\qquad
 W\ge 2\int_\Omega\frac{|H'|^2}{|H|}\,dA,
 \qquad
 C=\sqrt{\frac{BW}{2\pi}}.                           \tag{2}
\]

Use the locally integrable continuation at all zeros, as in RHE Note 08.
No zero-free collar, root count, unit floor, or square-root branch is
required for the next estimate.

## 2. A branch-free derivative transfer

**Lemma.** For `j>=1` and `z in K`,

\[
 \boxed{|H^{(j)}(z)|\le
      \frac{(j-1)!\sqrt j}{d^j}\,C.}                  \tag{3}
\]

**Proof.** On the radius-`d` disk centered at `z`,

\[
 \int |H'|^2dA\le B\int\frac{|H'|^2}{|H|}dA\le BW/2.
\]

For a holomorphic function `f`, Taylor orthogonality on that disk gives

\[
 \int_{D(z,d)}|f|^2dA
 =\pi\sum_{n\ge0}\frac{|f^{(n)}(z)|^2d^{2n+2}}
                        {(n!)^2(n+1)}.
\]

Retain the `n=j-1` nonnegative term and set `f=H'`. This proves (3).
One may use a slightly smaller radius and pass up to `d` if a boundary
disk touches the declared spatial boundary.

In particular the bounds for derivatives one through four are

\[
 C/d,\qquad \sqrt2C/d^2,\qquad
 2\sqrt3C/d^3,\qquad 12C/d^4.
\]

Substitution into the complete numerator in (1), retaining all three
terms, yields

\[
 \boxed{|Q_{vv}(x,v)|\le J_4:={1\over d^4}
       \left[(6+8\sqrt3)C^2+12BC\right]
       \quad(x+iv\in K).}                             \tag{4}
\]

The kernel in (1) has integral `eta^2/6`. Therefore

\[
 \boxed{|R_\eta|\le\frac{\eta^2J_4}{6}\,J_E,
       \qquad J_E=\int_a^b\frac{dx}{E(x)}.}            \tag{5}
\]

This is an actual transfer from weighted spatial area to the physical
tube observable, with its unresolved physical normalization explicitly
retained. A compact energy floor gives the fallback
`J_E <= (b-a)/e_*`, exactly the type of physical input already paid in
BW10 Note 21. It is not obtained from `W`.

If an additional paid Laguerre floor satisfies

\[
 Q_0(x)\ge q_*>0\qquad(a\le x\le b),                 \tag{6}
\]

then the exact cap integral gives the sharper payment

\[
 J_E\le\frac1{q_*}\int_a^b\frac{Q_0(x)}{E(x)}dx
      =\frac\pi{q_*},\qquad
 \boxed{|R_\eta|\le\frac{\pi\eta^2J_4}{6q_*}.}       \tag{7}
\]

All-real product information or the paid local Hermite chart can supply
such a floor on the declared interval; neither is inferred from the area
bound. Equation (7) also applies to any real analytic cap for which (6)
has been established directly. No RH assumption is needed after these
specific inputs have been paid.

## 3. Complete canonical-source version

For a fixed real time `|t|<=S`, choose a disk `Omega=D(c,R)` centered
at `c=(a+b)/2`. It contains a radius-`d` collar of the tube whenever

\[
 0<d<R-\sqrt{((b-a)/2)^2+\eta^2}.
\]

Define the complete positive moments

\[
 M_{j,R}(S)=\int_0^\infty
       u^j e^{Su^2+Ru}\Phi(u)\,du.
\]

The unchanged source and RHE Note 08 give the explicit choices

\[
 B=M_{0,R}(S),\qquad W=4\pi R M_{1,R}(S),\qquad
 C=\sqrt{2R M_{0,R}(S)M_{1,R}(S)}.                     \tag{8}
\]

All theta-index and ray tails are those already paid in the manuscript
and RHE Note 08. Thus (4)--(7) are effective complete-source bounds
uniform in the real center `c`, **conditional on the stated spatial
collar and physical floor**. A numerical use still requires enclosing
the finite moments and `q_*` or `J_E`; no such execution is claimed.

The same transfer can instead use an acquired smaller area interval and
a locally acquired amplitude upper. A direct estimator given those
observations can use the identical derivative inequalities. No gain
over BW10's existing coherent remainder estimate, numerical-cost
advantage, or intrinsic method dominance has been measured.

## 4. What the ordinary event forces the transfer to pay

Take the exact heat control `H_t(z)=z^2-2t`, `t>0`. Its adjacent roots
are `a=-sqrt(2t)`, `b=sqrt(2t)`, and

\[
 Q_0(x)=2x^2+4t,\qquad
 E(x)=(x^2-2t)^2+4x^2,\qquad Q_{vv}=12.
\]

Consequently (1) is exactly

\[
 R_\eta(t)=2\eta^2J_E(t).
\]

The substitution `x=ty` gives

\[
 tJ_E(t)=\int_{-\sqrt{2/t}}^{\sqrt{2/t}}
       \frac{dy}{(ty^2-2)^2+4y^2}\longrightarrow\frac\pi4.
                                                               \tag{9}
\]

For a direct dominated-convergence proof, extend the integrand by zero
outside its interval. For `t<=1`, on `|y|<=1` the denominator is at
least one, and on `|y|>1` it is at least `4y^2`. This is an integrable
majorant; the pointwise limit is `1/[4(1+y^2)]`. Hence

\[
 \boxed{R_\eta(t)=\frac{\pi\eta^2}{2t}(1+o(1)).}       \tag{10}
\]

The formula is valid for any positive thickness schedule because its
`eta^2` dependence is exact. At `eta=r sqrt(2t)` it yields the inherited
[BW10 Note 22][bw22] limit `pi r^2`. The new point here is its comparison with
the derivative-weighted area data:

* On every fixed disk of radius `R` centered at zero,
  `W(H_t;D_R)<=8 pi R^2` for all `t`, by RHE Note 08. Fixed positive
  thickness makes (10) unbounded, despite this fixed common area budget.
  Thus no finite bound depending only on that common budget can bound
  the tube remainder uniformly to the event.
* On a shrinking disk of radius `K sqrt(t)`, a change of variables gives
  `W=8t integral_{|w|<K}|w|^2/|w^2-2| dA_w=O_K(t)`.
  If `K>sqrt(2(1+r^2))`, this disk contains the whole heat-scale tube.
  Its weighted area tends to zero, while `R_{r sqrt(2t)}->pi r^2>0`.
  Therefore a transfer that sends a vanishing weighted-area bound to a
  vanishing physical trace error is false in this declared local class.

Here `q_*=4t`, and (7) with the **exact** `J_4=12` gives
`|R_eta|<=pi eta^2/(2t)`, asymptotically sharp in (10). Thus the
inverse-time cost is necessary; the physical Laguerre-floor payment
has exactly the correct event scale. With (4) substituted for the exact
`J_4`, the same exponent survives but its constant is generally larger.

For a fixed multiplicity `m`, the scaling can be made fully quantitative
using the **existing** BW10 Note 22 chart. Set `tau=sqrt(2t)` and

\[
 H(t,a_0+\tau z)=a_m\tau^m p_\tau(z).
\]

On one fixed scaled spatial domain containing all scaled tubes of
thickness at most `r_*`, take an established collar `d_0>0`, upper
`B_0>=sup|p_tau|`, area upper
`W_0>=2 integral |p_tau'|^2/|p_tau| dA`, and the paid lower
`p_tau'^2-p_tau p_tau''>=l>0` on the selected scaled real cap.
The source normal-form bounds of Note 22 supply `B_0` and a derivative
upper on a slightly larger scaled disk; RHE Note 08's disk theorem then
supplies `W_0` uniformly for sufficiently small time. Its established
Laguerre estimate supplies `l`. These are event-dependent constants,
not new consequences of the unnormalized area upper.

Define

\[
 C_0=\sqrt{B_0W_0/(2\pi)},\qquad
 J_{4,0}=d_0^{-4}[(6+8\sqrt3)C_0^2+12B_0C_0].
\]

Changing spatial variables gives exactly the valid physical budgets

\[
 B=|a_m|\tau^m B_0,\quad W=|a_m|\tau^m W_0,\quad
 d=\tau d_0,\quad C=|a_m|\tau^m C_0,\quad
 q_*=|a_m|^2\tau^{2m-2}l.
\]

Thus `J_4=|a_m|^2 tau^(2m-4) J_(4,0)` in (4), and for every
`0<eta<=r_* tau`, (7) becomes

\[
 \boxed{|R_\eta(t)|\le
       \frac{\pi J_{4,0}}{12l}\frac{\eta^2}{t}.}       \tag{10a}
\]

This recovers the necessary heat-scale exponent at every fixed
multiplicity while retaining the physical MT12 denominator throughout.
The bound is generally weaker than the already established coherent
profile/error in BW10 Note 22. It adds a transfer contract for weighted
area, not a new Hermite-profile theorem or a height-uniform estimate.

There is a separate normalization obstruction: replacing `H` by
`lambda H`, `lambda>0`, leaves `R_eta` unchanged but sends `W` to
`lambda W`. The factors in (7) transform consistently: `B,C` scale
by `lambda`, and `J_4,q_*` scale by `lambda^2`. A bound proportional
to `W` alone, with no compensating normalization, fails even away from
an event. The canonical source has its own fixed normalization; this
scaling witness rules out the stated source-independent transfer, not
all additional inequalities for that exact source.

## 5. The zero-free raw-density trace and its obstruction at branches

For clarity, a conventional holomorphic trace estimate is available
when the declared collar contains no zero of `H`. Put

\[
 D(z)=\frac{|H'(z)|^2}{|H(z)|}.
\]

On each radius-`d` zero-free disk, choose a holomorphic square root of
`H`; then `H'/sqrt(H)` is holomorphic and has squared modulus `D`.
The submean inequality, integrated over a real interval `I`, gives

\[
 \boxed{\int_I D(x)dx\le\frac{W(H;\Omega)}{\pi d}}.   \tag{11}
\]

Indeed `D(x)<=1/(pi d^2) integral_{D(x,d)}D dA`, and for any fixed
spatial point the set of possible centers `x in I` has length at most
`2d`. The factor two is canceled by the definition of `W`. No global
square-root marking is needed because the local squared modulus is
unambiguous. The order `d^(-1)` cannot be improved uniformly: for
`H(z)=(z+s)^2` with its zero outside the collar, `D=4` identically.
On a long interval and its radius-`d` neighborhood the ratio of the
line integral to `W` tends to `1/(4d)` as its length divided by `d`
tends to infinity. This establishes the sharp scale, not optimality
of the constant `1/pi` in (11).

This raw trace is unusable on the complete adjacent-root cap. At a
simple real zero `r`,

\[
 D(x)=\frac{|H'(r)|}{|x-r|}(1+o(1)),
\]

so its one-dimensional integral diverges logarithmically from either
side. Its two-dimensional area is nevertheless finite. On the
normalization of the cover the differential `H' dz/sqrt(H)=2dw` is
regular at the branch point; changing to that regular coordinate also
changes the metric/parameter of the line observable. It cannot erase
the divergence of the declared base-coordinate density `D(x)dx`.
Branch excisions and the changed line measure must be paid explicitly.

There is also no pointwise domination of the physical phase density by
this raw density through a cap: for the quadratic control at `x=0`,
`D(0)=0` while `Q_0(0)/E(0)=1/t`. The missing curvature/critical-point
information is precisely why (4)--(7) use higher derivatives and the
physical denominator rather than replacing the cap by (11).

## 6. Scope and the remaining useful gate

These results furnish a rigorous transfer to the **existing** signed
tube remainder, but its constants retain the collar, amplitude and
physical-floor data. A sufficiently accurate acquired `W` could be
used in that contract; a practical improvement over complete source
jet bounds must be checked on a declared finite consumer. No such
comparison or new signed theta margin is established here.

The quadratic and Hermite heat controls obey the local area and transfer
identities with their own constants, and their collisions establish the
stated budget and trace obstructions. They lack the unchanged canonical
source, so this is not a universal no-go statement for arithmetic
information. Euler-factor controls change canonical completion and
coefficients. Weighted-square and finite-prime controls fail complete
canonical coefficients/reflection; reflected and positive-primitive
controls fail the unchanged square sequence. Preserve their separate
lists as in [cluster 12][controls]. None is being claimed to satisfy
the entire original-source conjunction.

The remaining obstacle is explicit: the new global area upper does not
control `J_E` or a nondegenerating `q_*`. Existing BW10 Note 22 already
pays the local critical concentration coherently and gives a sharper
event profile. Removing the necessary endpoint cost, or producing a
source estimate that opposes that profile, requires information beyond
the weighted-area budget. The phase Gauss-area density of BW10 Note 24
has a different projective denominator and is not identified with (1)
or (11) by this note.

[rhe08]: 08_DERIVATIVE_WEIGHTED_ENERGY_AND_GLOBAL_STRIP_BOUND_20261022.md
[bw21]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[bw22]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
