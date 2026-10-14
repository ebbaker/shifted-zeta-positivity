# What a local collision theorem would contribute

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6-astra` (Codex), reasoning effort **ultra**.

A quantitative local collision theorem in investigation 19 would supply a
rigorous test of proposed physical positivity estimates. Its strongest
additional contribution is an explicit interval of failure at stationary
points, together with a precise description of the colliding zeros. It
would sharpen the requirements on a successful theta argument without
supplying that argument's missing positive estimate.

## What has changed since the proposal

[Proposal 3](PATHS_FORWARD_AFTER_CONSOLIDATION_CODEX_20261013.md#3-a-local-theorem-available-in-19)
outlined an implicit-function construction and a computable remainder.
The [fixed outward witness](../../active/19_euler_factor_controls/notes/2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md)
now proves the control bound \(\Lambda_{1/2,41}>1/5\). The newer
[manuscript](../../active/19_euler_factor_controls/manuscript/euler_factor_controls.tex),
Theorem 1.4 and Section 7, also gives a witness-based asymptotic lower bound
\[
\Lambda_{c,p}>t_m-S_2t_m^2-Qa^{-6},\qquad
 a=\tfrac12\log p,\quad t_m=\log(1/c)/a^2.
\]
Its stated explicit ranges include \(Q=1/50\) for
\(1/2\le c<1,\ p\ge29\), and \(Q=1/10\) for
\(e^{-2}\le c<1,\ p\ge293\). The manuscript awaits the specialist review
specified in the [investigation guide](../../active/19_euler_factor_controls/README.md);
this assessment does not certify that manuscript's proofs or arithmetic.

Consequently another proof only of a lower bound of this order has limited
incremental value. The remaining distinct target is the actual ordinary
collision branch, its location, its local zero geometry and a quantitative
stationary failure interval.

## The collision branch as an analytic target

Write \(G(t,x)=H_t^{c,p}(x)\), and let \(l=\log(1/c)\).
The exact shifted-copy formula suggests a unique nearby ordinary double
zero \((T_*,X_*)\) with
\[
 T_*={l\over a^2}-{S_2l^2\over a^4}+O(a^{-6}),\qquad
 X_*={\pi\over a}-{S_2\pi l\over a^3}+O(a^{-5}).
\]
A useful theorem must make the error constants and lower threshold on
\(a\) computable, uniformly for \(c\) in a declared compact subinterval
of \((0,1)\). Local uniqueness means uniqueness in the specified
neighborhood of the scaled point \((l,\pi)\).

At an ordinary double zero, \(G=G_x=0\) and \(G_{xx}\ne0\).
The exact equation \(G_t=-G_{xx}\) gives the leading local expression
\[
 G(t,x)=G_{xx}(T_*,X_*)
 \left({(x-X_*)^2\over2}-(t-T_*)\right)
 +\text{higher order terms}.
\]
Thus the local pair is nonreal immediately before the collision and real
immediately after it. Proving this with quantitative neighborhoods would
identify a genuine event in the flow. A separate continuation or Rouche
argument is needed to identify it with the pair inserted at time zero;
use \(T_*\), rather than the tracked label \(T_0\), until then.

## An exact stationary identity and its margin

The following elementary consequence would connect the branch theorem
directly to the broader program's first conditional Laguerre inequality.
It holds for any sufficiently smooth real solution of the backward heat
equation with an ordinary double zero, independently of the arithmetic
origin of the solution.

By the implicit-function theorem applied to \(G_x=0\), there is a local
real stationary curve \(x_s(t)\) through \((T_*,X_*)\). Along it,
\[
 {d\over dt}G(t,x_s(t))=G_t+(\partial_x G)\,x_s'=-G_{xx}(t,x_s(t)).
\]
Since \(G(T_*,X_*)=0\), integration gives the exact identity
\[
 G(t,x_s(t))=\int_t^{T_*}G_{xx}(s,x_s(s))\,ds.
\]
Consequently,
\[
 \boxed{\mathscr L_0(G;t,x_s(t))
 =-G_{xx}(t,x_s(t))\int_t^{T_*}G_{xx}(s,x_s(s))\,ds.}
\]
Continuity makes \(G_{xx}\) retain a nonzero sign in a sufficiently small
neighborhood. If computable constants \(h,m,M>0\) establish
\[
 m\le |G_{xx}(t,x_s(t))|\le M
 \quad (T_*-h\le t\le T_*),
\]
then for that predecessor interval
\[
 -M^2(T_*-t)\le\mathscr L_0(G;t,x_s(t))
 \le-m^2(T_*-t)<0\quad(t<T_*).
\]
The identity and conditional bounds follow from the displayed argument;
explicit values of \(h,m,M\) for the proposed control branch remain to
be established. They would quantify a whole interval of failure on the
physical stationary locus and the linear decay of the raw margin as the
collision is approached. This is more directly useful to the program
than a large negative ratio obtained by division by a small value of
\(G^2\).

## How the broader program would use it

A proposed identity or estimate for
\(\mathscr L_0(H)\ge0\) on \(H_x=0\) could be tested on this exact
stationary curve. If it uses only hypotheses retained by the control, the
negative margin gives a concrete contradiction. If it contains a defect
term for a hypothesis the control violates, that term must account for
the negative value. A positive decomposition with all such defects
incorrectly set to zero cannot pass this test.

For investigation 18, the
[control proposition](../../active/18_rank_two_automorphic_lift/notes/1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md#5-proposition-4-the-control-test)
shows that the same cusp kernel and every Hecke relation away from the
selected prime can coexist with a positive collision time. The local
theorem would quantify how this failure appears in the complete physical
form. It would not strengthen the already established qualitative claim
that finitely many Euler factors, combined only with properties shared
by the controls, cannot imply the desired global conclusion.

For investigation 02, the useful next connection would be an explicit
full-gluing defect in a named candidate identity, evaluated on the
control. Its
[continuation brief](../../active/02_angular_jacobi_gluing/reviews/CONTINUATION_AND_BRAINSTORM_BRIEF_20261013.md)
already has nearby collision controls against the generic correction
bounds. Merely furnishing another control would add little; making the
failed hypothesis and its quantitative contribution visible would help
assess a new multiplier.

The leading coefficients also clarify what the local mechanism uses.
For a general even analytic background heat flow with \(H_0(0)\ne0\),
the same expansion replaces \(-S_2\) by
\(2H_0''(0)/H_0(0)\). At this order the arithmetic background enters only
through central curvature. The multiplier sets the leading time scale,
and the background curvature supplies its first correction. This
observation does not establish a general impossibility result for methods
using more information, but it prevents attributing this local mechanism
to full theta arithmetic.

## Scope and recommended stopping point

The global Newman constant concerns all zeros; the distinction between a
local collision and that global threshold is fundamental to the
[general theory](https://arxiv.org/abs/1901.06596). Establishing this branch
would give \(\Lambda_{c,p}\ge T_*\), not the reverse inequality. It
would give no bound for the genuine theta constant. It also would not
settle the second conditional target
\(\mathscr L_1(H)=H_{xx}^2-H_xH_{xxx}\) on \(H_{xx}=0\).

The branch has low height \(X_*\sim\pi/a\). It therefore cannot by
itself screen an argument confined to large heights or one using genuine
low-height zero verification. Fixed-\(c\) bounds do not automatically
cover the varying family \(c_p=\operatorname{sech}(\delta a)\), which
approaches zero. Each stronger application requires its own domain and
hypothesis check.

A bounded next theorem should deliver the ordinary branch, explicit
remainder bounds and the stationary margin above. Connecting it to one
named 02 or 18 candidate would give the result a concrete consumer. The
claim that this branch is the globally last collision should remain a
separate problem. The broader payoff is a precise standard that a new
positive mechanism must meet: show which genuine-theta input excludes
this fully described failure, and turn that input into a complete signed
estimate.
