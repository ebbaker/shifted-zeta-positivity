# B04: Green mass, averaging resolution and the next value test

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual current runtime model:
**gpt-6-astra**; reasoning effort is not exposed. No subagents were used.

**Status: proved in-note from the named inherited inputs; proof-author
checking only.** The new calculations quantify the single-defect signal
and the failure of one inherited density-based upper allowance to resolve
it. They give no favorable canonical value. B04 compares two routes and
uses one focused clarification, the exact Green mass/window calculation.
The [decision][decision] selects a bounded E06 feasibility screen.

## 1. Fixed object and classification

Keep Newman time zero, the literal theta source, and the inherited
complete positive representation from [parent Note25][green]:
\[
a=\pi/8,\qquad
G(u,y)=\operatorname{atanh}(\sin(ay)\operatorname{sech}(au)),
\qquad J(X)=\sum_{j:y_j>0}G(X-x_j,y_j),\quad 0<y_j<1.
\tag{1}
\]
Multiplicities are included; real zeros have zero contribution. The
canonical signed boundary representation is unchanged:
\[
J(X)=\mathcal L(X)-P(X)+G(X,1).
\tag{2}
\]
[E03 Note06][acquisition], read with [E05 Note07][clarification], acquires
this value to arbitrary prescribed error. Its further strict comparison
with \(m(d,r)=\sin(a)d/\cosh(ar)\) remains unpaid.

The [result index][results], especially [clusters11][heat] and
[12][controls], and [avoid index][avoid], especially [target01][target],
[control02][screen] and [scope07][scope], govern the claims below.
Equations (3)–(10) are a quantitative signal/allowance comparison, not
another reformulation promoted as a sign result. Parent [Note20][moments]
already shows the all-order transverse-moment allowance cannot resolve
one pair. This note does not reopen that optimization: it computes the
linear-depth mass and exact constants for the present Green consumer.

## 2. One focused clarification: exact mass and finite windows

For every \(0\le y\le1\),
\[
\boxed{\int_{\mathbb R}G(u,y)\,du=\pi y.}
\tag{3}
\]
Indeed differentiation under the integral is justified by an integrable
exponential majorant uniform in y on [0,1]. With t=sinh(au),
\[
\int_{\mathbb R}\partial_yG(u,y)\,du
=\cos(ay)\int_{\mathbb R}\frac{dt}{t^2+\cos^2(ay)}=\pi.
\]
The integral vanishes at y=0. This also checks the factor: one upper
zero is counted, not both members of its conjugate pair.

For \(\ell\ge0\), define \(M_\ell(y)=\int_{-\ell}^{\ell}G(u,y)du\).
The same calculation gives the exact finite-window formula
\[
M_\ell(y)=2\int_0^y
 \arctan\!\left(\frac{\sinh(a\ell)}{\cos(at)}\right)dt.
\tag{4}
\]
With the inherited \(K_G=2a/\cos^2a\),
\[
0\le\pi y-M_\ell(y)
 \le\frac{2K_Gy}{a}e^{-a\ell}.
\tag{5}
\]
This follows by integrating \(G(u,y)\le K_Gy e^{-a|u|}\) on the two tails.

For a center interval [X−L,X+L], L>r>=0, a selected upper zero with
\(|x_j-X|\le r\) and \(y_j\ge d>0\) forces its normalized average
signal to be at least
\[
S_{L,r}(d)=\frac{M_{L+r}(d)+M_{L-r}(d)}{4L}.
\tag{6}
\]
This is the exact minimum of the selected-zero contribution over the
declared rectangle: G increases with y and decreases with |u|, so the
window integral is minimized at y=d and |x_j−X|=r. Differentiating the
shifted integral, or comparing its two endpoint values, verifies the
latter monotonicity. Other zeros only increase J. For fixed r and d,
\(S_{L,r}(d)\sim\pi d/(2L)\); the two tails in (5) pay the error.
This is a signal calculation, not an acquired upper comparison.

More generally, a finite added positive divisor with upper heights
y_1,...,y_k changes any nonnegative normalized observation
\(T^{-1}w((X-A)/T)dX\), with bounded w, by at most
\[
\frac{\pi\|w\|_\infty}{T}\sum_{j=1}^k y_j.
\tag{7}
\]
Tonelli and (3) prove this directly. Thus an o(1) error statement alone
has insufficient specified resolution for a finite defect. This is a
statement about the positive-divisor observation class. It does not
construct another canonical theta source or claim that all such
perturbations retain arithmetic or source positivity. Fixed-window
information, a sufficiently sharp rate, and canonical additional
constraints remain outside this limitation.

## 3. Route A: what the inherited density estimate actually pays

Use the already imported canonical estimate, with one fixed c in (0,1)
and D_c>=1 independent of sigma:
\[
N_\zeta(\sigma,V)\le D_c V\log V\,
 e^{-c(\sigma-1/2)\log V},\quad V\ge2,\quad 1/2<\sigma<1.
\tag{8}
\]
Theorem 2.4 and §4 (18) of Maples–Rodgers v2 were rechecked;
[source-use09][sources] records the passage and canonical ownership.
No explicit numerical value of D_c is asserted.

Let T>=4 and split the complete Green sum into upper zeros with
x_j in [T/2,5T/2] and the remainder. Put
\(B_T^+(v)=\#\{j:x_j\in[T/2,5T/2],y_j>v\}\), 0<v<1.
With s=(1−iz)/2, an upper zero corresponds, after conjugation, to a
right-half-plane zeta zero at ordinate x_j/2. Consequently
\[
B_T^+(v)\le N_\zeta(1/2+v/2,2T)
 \le2D_cT\log(2T)e^{-(c/2)v\log(2T)}.
\]
There is **no extra reflection factor two**: only upper H zeros are
counted here. Layer cake gives
\[
\sum_{x_j\in[T/2,5T/2],y_j>0}y_j
\le\frac{4D_c}{c}T\bigl(1-(2T)^{-c/2}\bigr).
\]
By (3), their center average on [T,2T] is at most pi/T times this sum.
Zeros outside the band are more than T/2 from every relevant center.
Use the inherited complete-zero tail with n=floor(T/2), q=exp(−a), and
the parent full unit-count constant A:
\[
\mathcal R_G(T)=2AK_Ge^{-an}
 \left\{\frac{\log(3+2T)+\log(n+1)}{1-q}
       +\frac{q}{(n+1)(1-q)^2}\right\}.
\]
All remote zeros, including negative horizontal coordinates, are paid.
Thus the explicit chosen allowance is
\[
\boxed{\frac1T\int_T^{2T}J(X)dX\le
 U_{\rm den}(T):=
 \frac{4\pi D_c}{c}\bigl(1-(2T)^{-c/2}\bigr)+\mathcal R_G(T).}
\tag{9}
\]
Its main term tends to a positive constant. For comparison, a selected
upper zero at x_0=3T/2, height d, has exact average signal
\(s_T(d)=M_{T/2}(d)/T\le\pi d/T\). Concavity in c gives
\((1-(2T)^{-c/2})/c\ge1-(2T)^{-1/2}\ge1/2\) for T>=4.
Therefore
\[
\boxed{\frac{U_{\rm den}(T)}{s_T(d)}
 \ge\frac{2D_cT}{d}\ge2T,
 \qquad T\ge4,\quad0<d\le1.}
\tag{10}
\]
The comparison already fails for a centrally placed selected zero; a
smaller guaranteed signal near an interval endpoint cannot repair it.
Even halving constants or improving numerical acquisition cannot bridge
this resolution gap in the stated allowance.

**Scope:** (10) lower-bounds a particular upper allowance relative to a
conditional signal. It is not a lower bound on the actual J or average,
and does not show that every consequence of (8), every signed analytical
estimate, or every statistics method fails. The direct coupled quantity
in (2) may be much smaller, including zero. A successful analytical route
still needs additional canonical value information at the local scale,
with an error below the declared defect signal. No such estimate was
obtained in this bounded comparison.

## 4. Route B: one question that can change the next decision

Select X=30, d=1/2, r=1 and h=m(d,r)/4. These are fixed design choices,
not measured outcomes. The target box is inside established low-height
RH verification: |x|<=31 corresponds to zeta ordinate at most 15.5.
Platt–Trudgian v1 Theorem 1 is used only for that calibration label;
it does not replace any E03 source/tail payment or set J(30)=0, since
the Green sum also sees remote zeros.

The next question is whether E03's displayed **uniform midpoint
certificate recipe** fits a panel cap of 10^6 for this single tuple.
It is a cost screen, not a field-value or zero-location computation.
[E06 Request18][request] freezes R,Q,delta selection, finite arithmetic
and radial searches, explicit derivative and quadrature bounds, evaluation
error allocations, a bounded scalar-arithmetic effort and outcomes.
It reports logarithms of the required panel count rather than allocating
that many panels. It also records the field-error resolution demanded
at a node, without pretending it is a measured working precision.

If the displayed recipe exceeds the cap, that recipe stops and a later
B decision must choose whether to improve its local-log/integration
bounds. If it passes, this merely clears the panel-count screen: an
actual evaluator still needs a separate implementation contract paying
node construction, finite arithmetic and runtime. An unresolved threshold
at the fixed arithmetic cap is an inconclusive return. No expansion to
more centers or higher precision is automatic. No numerical research is
performed by B04, and no favorable value is predicted.

## 5. Controls, retained evidence and stopping boundary

The analytical screen was run against the classes in [controls12][controls]
and the supplementary cases in Note07 §5. Generic formulas (3)–(7), when
their stated strip and consumer hypotheses hold, retain a defective
field's own Green response and do not distinguish theta.

| Class | Premise or scope that must remain explicit |
| --- | --- |
| Euler-factor controls | Canonical conductor-one coefficients and the exact prime baseline change; (8) with theta's D_c is not assigned to them. |
| Weighted squares, finite theta/zero tails and finite-prime orbits | Complete normalized theta source/reflection conjunction is absent; selected finite data do not supply it. |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | Full reflection or primitive positivity does not supply the integer-square arithmetic/xi identity. |
| Atomic fixed-event, finite-profile and continuous extensions | Complete theta coefficients/profile and eventual simplicity hypotheses are absent where claimed; keep each family's preservation list. |
| Conditional normalized endpoint controls | Ordinary Dirichlet arithmetic fails; functional equation and completion need not fail. Real doubles alone create no interior Green mass. |
| Variable readouts and three-profile relaxations | Respectively the full physical readout, or the integer zero/source constraints, are missing. |
| q and q_(T,a), smooth-density and two-channel cases | The first two lack the canonical transform/arithmetic; the last is a scoped norm-factorization exclusion, not a universal field control. |
| Finite added divisor in (7) | This is explicitly a relaxed positive-divisor class, with no claim of canonical source or arithmetic realization. |

A positive-time collision is not silently moved to time zero, and a
control can pass a box containing none of its defects. The inherited
conditioning, short-polynomial and harmonic-baseline obstructions retain
their classes and the evidence correction in Note07 §5. E03's vanishing
error theorem and HDA/RS's local transfer remain useful acquisition inputs;
neither supplies the missing value or authorizes a provider substitution.

**B04 completes at a quantified failure of this density-based averaging
allowance and one fixed feasibility-screen contract.** No favorable
canonical signed value, numerical certificate or universal obstruction
has been acquired. The [proof-author check][check] is the only new review.
Next: **[E] TND-OG-E06 — Sol6.1**, ready but unexecuted at B04 close.

[decision]: ../brainstorm/notes/09_TND_OG_B04_VALUE_ROUTE_DECISION_20261108.md
[green]: ../../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md
[moments]: ../../notes/20_TND_O_E10_R2_ALL_ORDER_TRANSVERSE_MOMENTS_20261107.md
[acquisition]: 06_TND_OG_E03_COMPLETE_SIGNED_LOG_ACQUISITION_20261108.md
[clarification]: 07_TND_OG_E05_ASSESSMENT_CALCULATIONS_20261108.md
[sources]: ../references/09_TND_OG_B04_VALUE_RESOLUTION_SOURCE_USE_20261108.md
[request]: ../research-progress/handoffs/18_TND_OG_E06_SINGLE_TUPLE_FEASIBILITY_REQUEST_20261108.md
[check]: ../reviews/07_TND_OG_B04_VALUE_RESOLUTION_AUTHOR_CHECK_20261108.md
[results]: ../../../../../../result-summaries/README.md
[heat]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[target]: ../../../../../../avoid/01_restating_the_target.md
[screen]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
