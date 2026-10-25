# Compact weak transfer and a paid time join

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort xhigh**,
verified from session metadata. Thread `01a1709a-adbd-7c81-9322-6d02e1619fbb`,
chat **0010**.

**Status: compact transfer and local time-joining estimates proved in-note;
same-assistant review only.** No finite core is accepted, no useful global
joining tolerance is asserted, and no numerical execution was performed.
The gain is an explicit transfer using only field-error orders **0 and 2**,
with kernel derivatives through four, including the adaptive curvature,
actual covariance, signed source and the time-cutoff defect. These bounds
need not beat the earlier local bounds numerically. The bounded comparison
is delegated to Sol under the author's revised [workflow][workflow].

This continues [Notes 32][n32] and [33][n33]. Read the [result index][results],
[heat-flow cluster][geometry], [controls][controls] and [avoid index][avoid].
This is a quantitative approximation estimate under [avoid 01][a01], with
[status][a06], [scope][a07] and [cancellation][a12] restrictions. It is not
an RH criterion, an autonomous closure, or a stability theorem for a PDE.

## 1. Cover and the norm being paid

Fix the physical q=epsilon_g^2 of [Note 20][n20], eta>0, ell,h>0,
observation strip |y|<=Y, and the specified normalized product kernel K.
There is no change in source, physical potential offset, mass or regulator.
All time derivatives are at fixed physical coordinates.

Choose symbolic T_-,T_+ and positive tau_-,tau_+, with T_- satisfying
[Note 26][n26]'s negative gates and T_+ satisfying [Notes 30][n30]/[31][n31]'s
all-height positive gates, in particular T_+>=128. Take

\[
 I=[-T_--\tau_-,\ T_++\tau_+],\quad
 B_-=[-T_--\tau_-,-T_-],\quad B_+=[T_+,T_++\tau_+]. \tag{CJ1}
\]

The negative and positive models are G and P_* respectively. On fixed
I_0=[inf I,64], [Note 25][n25] supplies the exterior zero-field background;
on fixed I_1=[32,sup I], PE44 supplies P_*. Choose a finite X_0 above both
full-buffer thresholds and so that their stated component allowances meet
the declared exterior tolerances. Their overlap in time is [32,64]. This
choice is existential where PE44's constants/onset remain uninstantiated;
32,64,128 are not substituted for a proved onset.

For a spatial overlap width sigma>0, use the finite field on observation
core |x|<=X_0+sigma and exterior charts on |x|>=X_0. Its source comparison
is supplied on all of

\[
 I\times\{|x|\le X_0+\sigma+\ell+2,\ |y|\le Y+h+2\}. \tag{CJ2}
\]

The extra 2 is the fixed analytic enlargement in Notes 30--31; enlarge it
further if a chosen collar construction requires it. Thresholds must hold
on the whole enlarged support, not just at observation centers. The finite
source is entire, so it has no unpaid analytic-disk edge. Full-buffer
endpoint and exterior comparisons give a finite atlas of observable tuples.
This atlas is not a globally joined field.

The complete norm here consists of the following absolute errors, each
with a positive prescribed allowance theta_(V,alpha):

| Observable | Spatial orders |
| --- | --- |
| U, W | 0 through 4 |
| R, averaged C, J, actual Q | 0 through 2 |
| U_t, W_t, R_t, averaged C_t | 0 through 2 |
| averaged B, actual averaged source S | 0 through 2 |
| U, normal derivative of U, normal current on fixed observation boundaries | inherited from the preceding sup norms |

Initial/final time traces are included. These quantities pay PE37--PE39,
including both C_t and square C, Delta B, Delta Q and the differentiated
mean-gradient squares. The theorem below additionally pays third spatial
current derivatives internally to estimate the second source derivatives.
No fourth current derivative or fifth kernel derivative is required.
No claim about moving boundaries, time averaging or shrinking filters is made.

## 2. A finite transfer map on a compact full buffer

Let H solve H_t=-H_zz, and let F be holomorphic in z and C1 in real time,
with E=F_t+F_zz. All fields and their needed derivatives are smooth on a
neighborhood of the full convolution buffer. Let

\[
 |H-F|\le d_0,\quad |H_{zz}-F_{zz}|\le d_2,\quad |E|\le\eta_E. \tag{CJ3}
\]

For a tile, every scalar bound below is a supremum on its full buffer.
One may instead retain pointwise envelopes and their positive kernel
integrals; their numerical integration remains a separate allowance.
Set e_*=min sqrt(q)>0 on this compact buffer only. Choose caps
bar d_0,bar d_2, require d_j<=bar d_j, and take
P_j>=|F_j|+bar d_j for j=0,2. Positive finite-source moment bounds give
such caps without locating roots. Define

\[
 m=(|F|-\bar d_0)_+,\quad M=|F|+\bar d_0,\quad
 a=\max_{m\le v\le M}\frac{v}{q+v^2},\quad
 b_*=(q+m^2)^{-1},\quad k=\max_{m\le v\le M}\frac{2qv}{(q+v^2)^2}.
\tag{CJ4}
\]

Take their suprema when using scalar tile bounds. Always
`a<=1/(2e_*)`, `b_*<=e_*^-2`, `k<=e_*^-1`. Caps freeze the coefficients
before source refinement; they prevent a claimed linear error table from
silently changing its constants with d_j. Let

\[
 s=2a d_0,\quad w=k d_0,\quad
 v_m=a d_2+P_2b_*d_0+mP_2a w\quad(m=0,1,2),\quad
 z=\eta_E/(2e_*). \tag{CJ5}
\]

Use S=log(|F|^2+q), w_F=q/(|F|^2+q), c_F=w_F(1-w_F), and
V_(m,F)=w_F^m F_zz conjugate(F)/(|F|^2+q). Then CJ5 bounds, respectively,
|delta S|, |delta w_F|, |delta V_m|, and
|Z_m|=|w_F^m E conjugate(F)/(|F|^2+q)|. Also |delta c|<=w.
Here delta means H minus F; the scalar w is an allowance, not w_F.

**Proof.** The line segment between F and H has modulus in [m,M].
The real gradient norms of log(|u|^2+q) and q/(|u|^2+q) are 2|u|/D
and 2q|u|/D^2. The map conjugate(u)/D has operator derivative norm
at most 1/D. Telescope its product with F_zz and w_F^m, using
|w_H^m-w_F^m|<=m|w_H-w_F| and the fixed cap P_2. This gives CJ5.
The polynomial c(w)=w(1-w) is 1-Lipschitz on [0,1]. No simple-root or
nonzero-field premise is used.

Put r=log q, b=r_t+(r_xx+r_x^2)/2, and c=r_xx+r_x^2 (r_y=0).
The following are finite coefficient bounds on the same buffer:

\[
 a_0=\|r_t\|_\infty,\quad R_1=\|\nabla r\|_\infty,\quad
 R_2=\|\Delta r\|_\infty,\quad
 T_1=\|\nabla r_t\|_\infty,\quad T_2=\|\Delta r_t\|_\infty,
\]
\[
 T_h=\|2\nabla r\cdot\nabla r_t\|_\infty,\quad
 b_0=\|b\|_\infty,\quad c_0=\|c\|_\infty. \tag{CJ6}
\]

Norms of vectors are Euclidean. For K_alpha=partial^alpha K define

\[
 L_\alpha=\|K_\alpha\|_1,\ M_\alpha=\||\nabla K_\alpha|\|_1,
\ D_\alpha=\|\Delta K_\alpha\|_1,\ B_\alpha=\|\square K_\alpha\|_1.
\tag{CJ7}
\]

Only defined orders through four are used. M_alpha can be bounded by
L_(alpha+x)+L_(alpha+y); D_alpha,B_alpha by the corresponding second
pure derivative norms. These are finite polynomial-kernel integrals.
For nonnegative inputs define the following positive linear maps:

\[
 C_\alpha(w,c)=\frac{2M_\alpha R_1w+
 L_\alpha(R_2w+R_1^2c)}{4\pi},\qquad
 P_\alpha(s,w,c)=\frac{D_\alpha s}{4\pi}+C_\alpha(w,c), \tag{CJ8}
\]
\[
 C^t_\alpha(w_t,w,c_t,c)=\frac{1}{4\pi}\left[
 2M_\alpha(R_1w_t+T_1w)+L_\alpha(R_2w_t+T_2w+R_1^2c_t+T_hc)
 \right], \tag{CJ9}
\]
\[
 J_\alpha=\frac{M_\alpha v_0+L_\alpha R_1v_1}{2\pi},\qquad
 D^E_\alpha=\frac{2D_\alpha z+4M_\alpha R_1z+
                  2L_\alpha(R_2+3R_1^2)z}{4\pi}. \tag{CJ10}
\]

The direct time allowances are

\[
 s_t=2v_0+a_0w+2z,\quad
 w_t=a_0w+2v_1+2z,\quad
 c_t=a_0w+2v_1+4v_2+6z. \tag{CJ11}
\]

The subscripts on these nonnegative scalars label directly proved time
errors; they do not denote differentiating s or w.

## 3. Complete observable table and proof of derivative orders

Choose fixed bounds U_gamma^* for the spatial potential derivatives of
both fields, for 1<=|gamma|<=3. An elementary choice is
U_gamma^*=L_gamma S_* where

\[
 S_* =\max\{|\log q_{\min}|,\ |\log(P_0^2+q_{\max})|\}. \tag{CJ12}
\]

This uses the actual physical S, without subtracting its offset. Tighter
bounds from the finite field plus L_gamma s are allowed if enclosed within
fixed caps. Set e_gamma=L_gamma s, and

\[
 N_\alpha=\sum_{i=x,y}\sum_{\beta\le\alpha}{\alpha\choose\beta}
 \left[e_{\beta+i}U^*_{\alpha-\beta+i}
       +U^*_{\beta+i}e_{\alpha-\beta+i}\right],
\quad Q_\alpha=4L_\alpha v_0+B_\alpha s+L_\alpha c_0w+N_\alpha.
\tag{CJ13}
\]

All multi-indices in N_alpha have order at most three when |alpha|<=2.
The full table is:

| Difference | Absolute allowance |
| --- | --- |
| partial^alpha U, partial^alpha W; order <=4 | L_alpha s, L_alpha w |
| partial^alpha R, partial^alpha averaged C; order <=2 | P_alpha(s,w,w), C_alpha(w,w) |
| partial^alpha J; order <=3 internally | J_alpha |
| partial^alpha actual Q; order <=2 | Q_alpha |
| partial^alpha U_t, partial^alpha W_t; order <=2 | L_alpha s_t, L_alpha w_t |
| partial^alpha averaged C_t; order <=2 | C^t_alpha(w_t,w,c_t,w) |
| partial^alpha R_t; order <=2 | T_alpha := D_alpha s_t/(4pi)+C^t_alpha(w_t,w,c_t,w) |
| partial^alpha averaged B; order <=2 | L_alpha b_0 w |
| partial^alpha actual averaged source S; order <=2 | T_alpha+J_(alpha+x)+J_(alpha+y)+D^E_alpha |

**(CJ14).** For a Laplacian, sum the xx and yy component allowances.
For a normal trace, sum the relevant component bounds with the absolute
normal coefficients. The formulas also apply to subrectangles whose full
supports stay in the declared buffer.

Here is a derivation, to make the reduced source orders checkable.
For every holomorphic F the exact spatial identities in Note 31 are

\[
4\pi\langle\rho_F,\psi\rangle=\int S_F\Delta\psi+
2\int w_F\nabla r\cdot\nabla\psi+
\int(w_F\Delta r+c_F|\nabla r|^2)\psi, \tag{CJ15}
\]
\[
\pi j_F=\partial_{\bar z}V_{0,F}+(\partial_{\bar z}r)V_{1,F},
\quad S_{F,x}^2-S_{F,y}^2=4\Re V_{0,F}-\square S_F+c w_F. \tag{CJ16}
\]

They follow by differentiating D_F=|F|^2+q; the rational forms are smooth
even at multiple zeros. In CJ15, subtract the two fields and test against
K_alpha. The terms other than S Delta psi are exactly minus 4pi times
the pairing with C_F. This proves CJ8 for both R and C, retaining the
curvature cancellation. The current identity, after one integration by
parts, gives CJ10 since |partial_bar psi|=|grad psi|/2 for a real test
and |partial_bar r|=|grad r|/2.

Directly using F_t=-F_zz+E gives

\[
 S_{F,t}=-2\Re V_{0,F}+r_tw_F+2\Re Z_0,
\quad w_{F,t}=r_tc_F+2\Re V_{1,F}-2\Re Z_1,
\]
\[
 c_{F,t}=r_tc_F(1-2w_F)+2\Re(V_{1,F}-2V_{2,F})
                                -2\Re(Z_1-2Z_2). \tag{CJ17}
\]

The polynomial w(1-w)(1-2w) has derivative 1-6w+6w^2, of modulus
at most 1 on [0,1]. Thus CJ11 follows. Differentiating CJ15 itself at
fixed q(t,x), rather than differentiating an error bound, gives CJ9 and
the R_t row: all derivatives of grad r, Delta r and |grad r|^2 remain.
This proves both curvature-time and density-time comparisons without d_3.

For covariance, convolve the signed identity CJ16 first and then subtract
the actual squared filtered gradients. The first part costs
4L_alpha v_0+B_alpha s+L_alpha c_0w. Leibniz' rule on the two products
of mean gradients gives exactly N_alpha. This proves CJ13 for the actual
Q; separate positive unfiltered gradient-square estimates are not used.

Finally the actual source is
S_F=(1-2w_F)(r_t rho_F+grad r dot j_F), and direct differentiation yields
rho_(F,t)+div j_F=S_F+D_E, where

\[
D_E=\frac{2q\Re(E_z\overline{F_z})}{\pi D_F^2}
       -4\rho_F\Re\frac{E\overline F}{D_F}.
\]

Its weak form, obtained by varying CJ15 with delta F=E at fixed q, is

\[
4\pi\langle D_E,\psi\rangle=2\Re\int Z_0\Delta\psi
-4\Re\int Z_1\nabla r\cdot\nabla\psi
-2\Re\int\{Z_1\Delta r+(Z_1-2Z_2)|\nabla r|^2\}\psi. \tag{CJ18}
\]

It proves D^E_alpha. Subtract the two exact current balances to get the
last CJ14 row. This bounds the already defined signed source, not a source
invented from the desired equation. The proof needs J through order three,
whose one integration by parts uses only order-four K. Similarly R_t and
Q through order two use two extra kernel derivatives. K is C3 with bounded
weak fourth derivatives and no fourth-order boundary delta; smooth
approximation justifies these pairings. There is no unestimated E_z or
fifth derivative in the final table.

## 4. Finite source accuracy and overlap allowances

For F=H_f, the exact finite source field in Note 20, E=0. Use Note 23 LC2
and its corresponding weights/tails only for j=0,2:

\[
 d_j=I_j+M_j+T_j+A_j^{\rm nodal},\quad j=0,2. \tag{CJ19}
\]

Preserve interpolation I, omitted arithmetic modes M, complete-source
tail T and nodal arithmetic A separately. Field-evaluation arithmetic and
filter integration are additional errors. An implementation should evaluate
the weak formulas against the exact finite field with paid evaluation error;
it must not assume independent rounded jet values solve the heat equation.
Jets of orders 1 and 3 remain needed if choosing Note 23's pointwise
rho_t evaluator instead of this weak route. The reduction applies to this
fixed smoothed norm, not to pointwise density/current or arbitrary filters.

After fixing caps and coefficient bounds, every row of CJ14 has the form

\[
 E_{V,\alpha}=A_{V,\alpha}d_0+B_{V,\alpha}d_2+
 C_{V,\alpha}\eta_E,\qquad A,B,C\ge0. \tag{CJ20}
\]

The coefficients are given by the finite substitutions CJ5--CJ14, not an
unspecified Lipschitz constant. This is the source-accuracy table consumed
by the entire norm. On a finite collection of tiles, take the largest
coefficient for each row. For chosen positive theta_(V,alpha), one explicit
sufficient exact-finite-source requirement is

\[
 d_0\le\min\left(\bar d_0,\min_{A_{V,\alpha}>0}
          \frac{0.4\theta_{V,\alpha}}{A_{V,\alpha}}\right),\quad
 d_2\le\min\left(\bar d_2,\min_{B_{V,\alpha}>0}
          \frac{0.4\theta_{V,\alpha}}{B_{V,\alpha}}\right). \tag{CJ21}
\]

Empty inner minima impose no constraint. This reserves 80% for the mapped
CJ19 errors, 10% for subsequent field/observable evaluation arithmetic and
10% for averaging, as in Note 23. Nodal arithmetic in CJ19 is reported
separately from the later evaluation arithmetic; it is not counted twice.
Other allocations can be declared before evaluation. Time joins need the
extra C eta_E allowance in CJ20, so CJ21 alone does not accept a join.

For any fixed compact tile these demands are attainable as existence
statements by Note 20/23's source approximation. No manageable cost or
accepted numerical mesh follows. Large P_2/e_* or tiny e_* may make this
bound unusable. Amplitude-aware local integration or the older LC bounds
may do better; there is no asserted domination.

The finite overlap table is now explicit at the level of inputs:

| Overlap | Tuple-difference allowance for each CJ14 component |
| --- | --- |
| H_f / negative G on B_- inside the buffered core | CJ14(H,H_f) + Note 26's matching component bound; CJ14 with NE6 can fill any additional derivative row |
| H_f / positive P_* on B_+ inside the buffered core | CJ14(H,H_f) + PE6 |
| H_f / exterior zero field on I_0 and X_0<=|x|<=X_0+sigma | CJ14(H,H_f) + Note 25 OH6--OH10 with kernel derivative transfer |
| H_f / exterior P_* on I_1 in the same spatial band | CJ14(H,H_f) + PE44 |
| Exterior zero field / P_* on [32,64], |x|>=X_0 | Note 25 allowance + PE44 |

All are triangle inequalities through the same physical H and q. They pay
observable differences, not the field difference in a time-cutoff defect.
For that stronger input use NE6 for G, or PE7/PE9 for P_*, on the actual
compact full buffer. Their constants must be made effective before numerical
acceptance of a particular endpoint join.

## 5. A legitimate local time join, with its complete defect

On a compact overlap let F_1,F_2 have independent field-error allowances
h_(i,0),h_(i,2) against H, residual allowances eta_i, and a common analytic
buffer. Let theta(t) range in [0,1], be constant outside a band of width
tau>0, and satisfy |theta'|<=c_theta/tau. Choose it smooth and flat at
both band endpoints. Define the actual field

\[
 F=(1-\theta)F_1+\theta F_2. \tag{CJ22}
\]

It is holomorphic in space, preserves real/even symmetries when the
components have them, and matches those components with smooth endpoint
traces. Its exact heat residual is

\[
 E=(1-\theta)E_1+\theta E_2+\theta'(F_2-F_1). \tag{CJ23}
\]

Consequently CJ3 holds with

\[
 d_j=(1-\theta)h_{1,j}+\theta h_{2,j}\ (j=0,2),\quad
 \eta_E=(1-\theta)\eta_1+\theta\eta_2+
             |\theta'|(h_{1,0}+h_{2,0}). \tag{CJ24}
\]

Suprema can replace these pointwise allowances. If |theta'| is bounded
only by c_theta/tau, use that bound. The compact regulator floor and caps
are recomputed for F and the whole overlap. Applying CJ14 proves every
claimed observable/trace comparison for the joined field. This also proves
that its covariance is the actual Q_F, not a convex average of Q_1,Q_2.

Its exact equations are

\[
 U_t=-\tfrac12(\square U+U_x^2-U_y^2+Q)+\overline B+2\Re K*Z_0,
 \qquad \Delta U=4\pi(R+\overline C), \tag{CJ25}
\]
\[
 R_t=-\tfrac12\square R-\frac1{8\pi}\Delta(U_x^2-U_y^2+Q)
 +\frac1{4\pi}\Delta\overline B-\overline C_t
 -\tfrac12\square\overline C+\frac1{2\pi}\Delta\Re K*Z_0,
\quad R_t+\operatorname{div}J=\overline S+K*D_E. \tag{CJ26}
\]

The three displayed residual corrections have respective derivative
allowances `2L_alpha z`, `D_alpha z/(2pi)`, and `D^E_alpha` at the
orders used. These follow directly from CJ18 and are separate from the
comparison error. No PDE propagation estimate is used. For a fixed
component budget theta_(V,alpha), the additional cutoff cost in CJ20 is
at most

\[
 C_{V,\alpha}\frac{c_\theta}{\tau}(h_{1,0}+h_{2,0}). \tag{CJ27}
\]

A tolerance remains unpaid unless this and the component residual costs
fit it. Making the finite source finer does not remove h_(endpoint,0) or
the saddle residual. Increasing tau also changes the compact domain and
its coefficients, so it is not a free improvement.

This proves a local time-joining estimate, not an all-height time splice
of a fixed finite source. Note 25's positive-cutoff obstruction prevents
that finite source from supplying the required all-height potential after
64. Its own exact heat equation does not repair the missing comparison.

## 6. Exact unpaid spatial term and scope of the disposition

For a real spatial cutoff lambda(x,y), the tempting field construction
F=(1-lambda)H_f+lambda P_* satisfies on its transition band

\[
 \partial_{\bar z}F=(\partial_{\bar z}\lambda)(P_*-H_f). \tag{CJ28}
\]

Thus it is generally not holomorphic and CJ15--CJ16 cannot simply be
reused there. This is the failed **uncorrected spatial cutoff of fields**
route, not an impossibility for corrected/nonholomorphic models or other
joins. A compact time join does not fix that spatial term. An observable
blend has separate compatibility costs and is also not supplied here.

The remaining extra high difficulty task is a single spatial assembly
with a legitimate density/potential/current/actual-covariance system and
paid defects uniformly as the regulator shrinks. Routine finite coefficient
work and initial diagnostics need not wait for it. The [Sol packet][packet]
asks for that bounded follow-through now. HDA-17 advances to **Partial —
compact analytical contract; no accepted finite core**. HDA-18 remains
**Gated**; local time joining is paid symbolically, but effective endpoint
field allowances, informative costs and spatial assembly remain open.
HDA-16/19 retain their earlier scopes; HDA-20 is untouched.

## 7. Controls and evidence

The transfer/time-joining theorem is generic for holomorphic fields with
positive q on a compact buffer; colliding fields, including z^2-2t, satisfy
its premises. It excludes no collision control. The canonical-source
LC2/LC3/LC5 constants are the specific premises missing for changed-source
controls: Euler-factor modifications change the canonical completion;
weighted-square/finite-prime changes lack its unchanged full coefficients
and reflection; reflected smooth and positive-primitive controls lack the
canonical gamma-times-zeta/source identity. Atomic and heat-polynomial
controls lack the smooth theta source for CJ19, while still obeying the
local field identities. The fixed-event atomic and normalized-endpoint
controls in the [register][controls] likewise receive no collision
exclusion: their source/arithmetic premises differ, and the generic compact
comparison permits double events. No numerical control campaign was run.

[Review 17][review] checks the signs, source orders, kernel orders, scope
and cutoff payment by hand. It is same-assistant review, not HDA-20.
The maintained manuscript remains at its 65-page through-Note-31 scope.

**Next: Analysis and numerics — Sol.** Instantiate and compare the compact
weak budgets with the existing local route, using the bounded request in
[HDA-17-AN01 r1][packet]. Sol may complete routine coefficient algebra and
record its own disposition under the revised workflow. Escalate only a
specific hard obstruction, especially the unresolved spatial compatibility.

[n20]: 20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[n25]: 25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md
[n26]: 26_NEGATIVE_ENDPOINT_EVOLUTION_AND_COVARIANCE_20261024.md
[n30]: 30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md
[n31]: 31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md
[n32]: 32_CONTINUATION_FINITE_CORE_AND_JOINING_20261024.md
[n33]: 33_FINITE_CORE_JOINING_INTAKE_AND_ASTRA_HANDOFF_20261024.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a06]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[review]: ../reviews/17_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_SELF_REVIEW_20261024.md
[packet]: ../research-progress/handoffs/HDA-17-AN01.md
