# Exact correlated error jets and the limit of a disk-only collision certificate

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the active reasoning effort is not exposed to this
worker and is not inferred. These are internal LLM derivations and exact
arithmetic checks, not independent mathematical validation.

This continues investigation 17, especially the [carrier identity](12_EXACT_CARRIER_DEFECT_AND_CUTOFF_EDGE_MASS_20261010.md) and [bounded-loss criterion](16_NEXT_STEPS_AND_BOUNDED_LOSS_COLLISION_CRITERION_20261010.md). No genuine
theta sign, new collision domain, or RH conclusion is proved here.

## Result

The complete holomorphic disk input admits an exact four-parameter real
description of its error jets through order three. Incorporating physical
stationarity reduces the robust bounded-loss tests to one real variable for
`H_x=0` and two for `H_xx=0`. This can improve finite certificates over
independent Cauchy boxes, without introducing any additional approximation
assumption.

There is a precise stopping rule: at a strict interior point of the existing
correlated first-jet candidate body, the disk information permits a local
real-analytic backward heat solution with a double zero. This remains true
with the actual prescribed smooth finite sum and normalizer as the center of
the approximation tube. Thus exact disk correlation cannot by itself prove
the collision target throughout that interior. Extra information about the
genuine theta preparation is essential.

## 1. Exact real Schur jets through order three

Freeze `t,N` at a real center `x`, write `R=1/L`, and normalize the complete
error as
\[
g(w)=\frac{e(x+w/L)}{\eta},\qquad
e=Q-F,\qquad |g(w)|\le1\quad(|w|\le1).
\]
Since `e` is real on the real axis, its Taylor coefficients are real. Write
\[
g(w)=u_0+u_1w+u_2w^2+u_3w^3+O(w^4).
\]
The exact feasible set is the image of `[-1,1]^4` under
\[
\begin{aligned}
u_0&=a,\\
u_1&=(1-a^2)b,\\
u_2&=(1-a^2)\{(1-b^2)c-ab^2\},\\
u_3&=(1-a^2)\{(1-b^2)[(1-c^2)d-bc^2-2abc]+a^2b^3\}.
\end{aligned}\tag{1}
\]
In particular `e^(j)(x)=eta j! L^j u_j`; the factorial is essential.

Here is a short derivation, so the formulas do not depend on an unexamined
interpolation theorem. For a real Schur function with `g(0)=a` and `|a|<1`,
the disk automorphism `(g-a)/(1-ag)` vanishes at zero. Dividing by `w`
produces another Schur function `h`, by Schwarz's lemma, and
\[
g(w)=\frac{a+wh(w)}{1+awh(w)}.
\]
Schwarz's lemma here follows from the maximum principle applied on disks of
radius `r<1` to a holomorphic function vanishing at zero, then taking
`r` to one. Apply this step three times with initial values `a,b,c`, and
take the next constant to be `d`. Expansion yields (1). Conversely every
choice in the cube is realized by these inverse disk automorphisms. If one
parameter has modulus one, the corresponding Schur function is constant
and the recursion terminates; (1) already implements all these cases.
Every finite jet of an arbitrary Schur function is recovered this way,
because the remaining tail changes no displayed coefficient.

For example `a=+-1` forces `u_1=u_2=u_3=0`; if `|a|<1,b=+-1`, then
`u_2=-a(1-a^2)` and `u_3=a^2 b(1-a^2)` are forced. These boundary cases must
not be processed by division through zero in an implementation.

An equivalent convex representation is the finite Toeplitz condition
\[
T_3=\begin{pmatrix}
u_0&0&0&0\\u_1&u_0&0&0\\u_2&u_1&u_0&0\\u_3&u_2&u_1&u_0
\end{pmatrix},\qquad I-T_3T_3^T\succeq0.\tag{2}
\]
The one-variable Caratheodory--Fejer contraction criterion is discussed and
proved by successive contractive extensions in Gupta and Misra,
[The Caratheodory--Fejer interpolation problem for the polydisc, Section 3.1](https://math.iisc.ac.in/~gm/gmhomefiles/papers/CFIntThm.pdf).
Its real-coefficient specialization follows by conjugation averaging an
interpolant, or directly from (1). Necessity of (2) also follows by
compressing multiplication by `g` to the first four Hardy coefficients.
The explicit recursion (1) is sufficient for all results below, so a
certificate need not invoke or numerically solve a semidefinite problem.

## 2. Physical normalizer and stationary products

Let
\[
\lambda=A'/A,\quad m_2=\lambda^2+\lambda',\quad
m_3=\lambda^3+3\lambda\lambda'+\lambda'',\quad
f_j=(AF)^{(j)}/A,\quad K_j=H^{(j)}/A.
\]
All derivatives are physical spatial derivatives at fixed `t,N`. Then
\[
\begin{aligned}
K_0&=f_0+\eta u_0,\\
K_1&=f_1+\eta(\lambda u_0+Lu_1),\\
K_2&=f_2+\eta(m_2u_0+2\lambda Lu_1+2L^2u_2),\\
K_3&=f_3+\eta(m_3u_0+3m_2Lu_1+6\lambda L^2u_2+6L^3u_3).
\end{aligned}\tag{3}
\]
The exact robust disk-only tests are
\[
\sup_{(a,b,c,d)\in[-1,1]^4,\ K_1=0}
\{K_0K_2-C_0(K_0^2+K_1^2)\}\le0,\tag{4}
\]
\[
\sup_{(a,b,c,d)\in[-1,1]^4,\ K_2=0}
\{K_1K_3-C_1(K_0^2+K_1^2)\}\le0.\tag{5}
\]
These imply Note 16's two physical bounded-loss inequalities, since `A>0`.
The maximizations retain a common holomorphic error; using separate bounds
on the four `K_j` destroys that correlation. A finite failure of (4) or (5)
means the input does not certify the target, not that genuine theta fails it.

## 3. Exact conditional intervals and reduced tests

Suppose `|a|<1`, put `D=1-a^2`, and write `s=u_1`. The first two
coefficients are feasible exactly when `|s|<=D`. Define
\[
b=s/D,\quad M_2=-as^2/D,\quad
R_2=D-s^2/D=D(1-b^2).\tag{6}
\]
Then the exact conditional interval is
\[
u_2\in[M_2-R_2,M_2+R_2].\tag{7}
\]
For `R_2>0` and a selected feasible `u=u_2`, put
\[
c=(u-M_2)/R_2,\quad
M_3=D\{(1-b^2)(-bc^2-2abc)+a^2b^3\},\quad
R_3=D(1-b^2)(1-c^2).
\]
The exact conditional third-coefficient interval is
\[
u_3\in[M_3-R_3,M_3+R_3].\tag{8}
\]
If `R_2=0`, `u_2=M_2` and `u_3=Da^2b^3` are forced. If `|a|=1`, all
higher coefficients vanish. These are explicit formulas at every boundary.

On `K_1=0`, choose `a` and set
\[
s(a)=-(f_1/\eta+\lambda a)/L.
\]
Retain exactly those `a` with `|a|<=1` and `|s(a)|<=1-a^2`, using the
forced boundary jets when `|a|=1`. For interior `a`, let
\[
\bar K_2=f_2+\eta(m_2a+2\lambda Ls+2L^2M_2).
\]
Then (4) is equivalent to the one-dimensional inequality
\[
\sup_a\{K_0\bar K_2+2\eta L^2R_2|K_0|-C_0K_0^2\}\le0.
\tag{9}
\]
For `K_2=0`, choose `a,s` with `|a|<1,|s|<=D` and set
\[
u=-(f_2/\eta+m_2a+2\lambda Ls)/(2L^2).
\]
Retain the pair exactly when `|u-M_2|<=R_2`, including the forced boundary
case. The central third physical jet is
\[
\bar K_3=f_3-3\lambda f_2+
\eta\{(\lambda''-2\lambda^3)a+3(\lambda'-\lambda^2)Ls+6L^3M_3\}.
\tag{10}
\]
Thus (5) is equivalent to the two-dimensional inequality
\[
\sup_{a,s}\{K_1\bar K_3+6\eta L^3R_3|K_1|
-C_1(K_0^2+K_1^2)\}\le0.\tag{11}
\]
The possible endpoint cases `a=+-1`, with `s=u=u_3=0`, are checked
separately and included in this supremum.
The last Schur parameter was optimized exactly, with its sign aligned with
the multiplying physical jet. The normalizer terms in (10) result from
eliminating `u_2` using physical `H_xx=0`, not normalized `Q_xx=0`.

For a cell computation, enclose `f_j,lambda,lambda',lambda'',L,eta` with
outward arithmetic and subdivide the remaining parameter domain. Rejection
of a box requires a rigorous infeasibility test; unresolved boxes stay in
the candidate set. Near singular Schur coordinates, use the division-free
cube formula (1), the Toeplitz condition (2), or explicit boundary cases.
Interval arithmetic on ill-conditioned divisions is not a certificate.
Data intervals may be conservatively treated as independent, but this can
lose additional source correlation.

## 4. Sharp limits near vanishing first jets

Correlation reduces a *conditional* uncertainty radius when lower jets
approach an extremal Schur boundary. It provides no uniform improvement of
the third Cauchy constant: `g(w)=w^3` has `u_0=u_1=u_2=0,u_3=1`, hence
`e'''=6 eta L^3` while all lower errors vanish. This remains true after
physical normalization because all lower error contributions in (3) are
zero.

The geometric obstruction is stronger than that sharp constant. With
`A=1,F=0`, choose the real Schur function
\[
g_b(w)=\frac{w(b+w^2)}{1+bw^2},\qquad 0<b<1.
\]
It has `u_0=u_2=0,u_1=b,u_3=1-b^2`. Therefore `H_xx=0`,
\[
K_0=0,\quad K_1=\eta Lb,\quad K_3=6\eta L^3(1-b^2),
\]
and
\[
\frac{K_1K_3}{K_0^2+K_1^2}=6L^2\frac{1-b^2}{b}\longrightarrow+\infty.
\tag{12}
\]
This is a family of admissible spatial errors, not a claimed single heat
orbit or a theta example. It shows directly why the residual radius in
(11), linear in `|K_1|`, need not scale like the squared first jet.

## 5. Local heat no-go at every strict interior first-jet candidate

The following statement preserves the prescribed approximation family, not
merely the zero approximation used in (12).

**Proposition (local non-identifiability from a disk tube).** Fix an interior
point `(t_0,x_0)` of a fixed-cutoff patch. Suppose `A(t,z)` is nonzero and
holomorphic in a neighborhood of the relevant closed spatial disks, positive
on the real axis, and `F(t,z)` is holomorphic there and real on the real
axis. Suppose `A,F`, the positive error allowance `eta(t,x)`, and the positive
disk radius `R(x)` vary continuously with their parameters, jointly and
uniformly on each relevant compact complex disk. If at the point
\[
a_*=-F(t_0,x_0)/\eta_0,\qquad
s_*=-R_0 F_x(t_0,x_0)/\eta_0,
\qquad a_*^2+|s_*|<1,\tag{13}
\]
then there exists a real polynomial backward heat solution `H_t=-H_xx`
which has a double spatial zero at `(t_0,x_0)` and satisfies
\[
|H(t,z)/A(t,z)-F(t,z)|<\eta(t,x)
\quad (|z-x|\le R(x))\tag{14}
\]
for every `(t,x)` in a sufficiently small open neighborhood of the point.

**Proof.** Write `a=a_*`, `b=s_*/(1-a^2)`. Strictness gives `|a|,|b|<1`.
For `c` in `(-1,1)` define
\[
h(w)=\frac{b+cw}{1+bcw},\qquad
g(w)=\frac{a+wh(w)}{1+awh(w)}.
\]
These rational functions are holomorphic on a neighborhood of the closed
unit disk and `sup_|w|<=1 |g(w)|<1`. Their first two coefficients are `a,s_*`,
while the coefficient of `w^2` ranges over the open interval (7), whose
radius is positive. Thus
\[
H_*(z)=A(t_0,z)\{F(t_0,z)+\eta_0g((z-x_0)/R_0)\}
\]
obeys `H_*(x_0)=H_*'(x_0)=0`. Choose `c` to avoid the single value, if any,
for which `H_*''(x_0)=0`. This is possible because `R_2>0` and at the
vanishing first jet physical `H_*''=A(F''+e'')`.

The approximation tube has strict uniform slack on its closed disk. By
continuity and holomorphy, slightly enlarge the disk while keeping positive
slack relative to `eta_0`. Taylor polynomials `P` of `H_*` about `x_0`
converge uniformly on this enlarged disk. Every truncation of degree at
least two preserves the zero constant and linear coefficients and the
nonzero quadratic coefficient exactly. Take a sufficiently high truncation
so `P/A(t_0,.)-F(t_0,.)` still has strict slack; this uses the positive
minimum of `|A(t_0,.)|` on the compact disk.

Now set
\[
H(t,z)=\sum_{j=0}^{\lfloor\deg P/2\rfloor}
\frac{[-(t-t_0)]^j}{j!}P^{(2j)}(z).
\tag{15}
\]
The sum is finite, has real coefficients, solves `H_t=-H_xx`, and equals
`P` at `t_0`. The strict uniform slack, nonvanishing of `A`, and parameter
continuity preserve (14) for all sufficiently close times and centers. The
slightly enlarged disk accommodates the shifted centers and moving radii.
The double zero at `(t_0,x_0)` is retained. QED.

The proposition concerns a sufficiently small open fixed-cutoff patch;
cutoff jumps and closed sector boundaries require their own compatibility
argument. It does not construct a solution with the genuine theta initial
condition, global theta symmetry, its positive complete spectral source, or
the global high-height estimates. None of those are claimed to follow from
the local tube. Its conclusion is exactly that disk control, physical
normalization and local backward heat analyticity together leave actual
collisions possible inside every strict interior first-jet candidate.

For the constructed solution, the even-multiplicity predecessor argument
in Note 16 gives `HH_xx/(H^2+H_x^2)=1/(t_0-t)+O(1)` on its earlier `H_x=0`
branch. Hence a locally bounded loss cannot be proved from those inputs
alone on the tube neighborhood. The obstruction persists however small the
strict tube is; it is not an assertion about the size of the genuine error.

## 6. Practical next use

Use (9) and (11) to improve retained complete stationary-cell certificates,
especially when a lower-jet constraint consumes much of the Schur disk.
They give a complete error model through third order and a principled
comparison with independent Cauchy payment.

Do not make that finite-jet optimization the main analytic milestone. If a
candidate remains strictly inside the first-jet body, the local no-go shows
that a genuine exclusion or bounded-loss theorem must use source information
that distinguishes theta from the alternative heat solutions. A smaller
*proved* disk bound may first remove the candidate; otherwise the missing
input is correlation beyond arbitrary bounded holomorphic error.

The companion [exact checker](../numerics/check_correlated_jet_geometry.py) and [record](../numerics/CORRELATED_JET_GEOMETRY_RECORD_20261010.json) check (1) by independent
formal power-series arithmetic over rational numbers, all finite Toeplitz
principal minors on a rational parameter grid, the degenerate boundary
cases, the conditional endpoint intervals, and physical stationary drift
elimination. It does not evaluate theta, certify a spatial cell, or turn a
finite parameter sample into a proof of the displayed general identities.

A complete outward example using the actual prescribed finite sum is given in [Note 19](19_STATIONARY_SURVEY_AND_CERTIFIED_DISK_AMBIGUITY_20261010.md). It demonstrates stationary-sign ambiguity at a separated first jet; it is distinct from the interior collision proposition above.
