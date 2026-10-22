# From evaluated Chern/Hopf mass to critical-wall amplitude estimates

22 October 2026, America/New_York. Written for **Edward Baker** with
substantial LLM assistance. Actual recorded authoring model
**gpt-6.1-sol (Codex), reasoning effort ultra**, verified from this turn's
metadata.

**Status: synthesis of existing results proved in-note in their specified
conditional local scope.** This write-up collects the established mass,
comparison and signed endpoint results into their dedicated investigation
home. It adds no new theorem or numerical acquisition and does not upgrade
the original internal LLM reviews. The detailed shared sources [03][n3],
[04][n4], [05][n5] and [06][n6] prevail if a transcription disagrees.

Read the [result index][results] and [avoid index][avoid], specifically
[heat geometry][geometry], [collision controls][controls],
[criterion classification][a01], [scope][a07] and [coupled terms][a12].
The bounds below are quantitative local estimates and comparisons, not
evidence for a new RH-equivalent criterion. In particular, a finite
geometric integral is compatible with a multiple endpoint.

## 1. Setting and what is actually estimated

Use the fixed physical jet frame for a jointly holomorphic heat field,

\[
 H_\tau=-H_{zz},\qquad G=(H,H_z),\qquad
 E=|H|^2+|H_z|^2,\qquad
 J=H_zH_{zzz}-H_{zz}^{\,2}.
\]

Let W=D times Omega be the complete physical product window of [Note 03][n3],
where D=[-T,T]+i[-Y,Y], Omega={|z-a|<=R}, a is real and T=Y=d/2.
Its boundary jet is nonzero.
The conditional ordinary-double construction starts with
H(0,a)=H_z(0,a)=0 and h_2=H_zz(0,a)!=0, and supplies one holomorphic
critical graph c(tau) and critical value V(tau)=H(tau,c(tau)).

The D_j are upper bounds for |partial_z^j H| on the ambient polydisk
used by that sufficient-window contract. Its associated constants are
epsilon_1=D_2R+D_3d, epsilon_2=D_3R+D_4d,
M_0=D_2(d+R²/2) and m_*=5hR/8, with h=|h_2|. These are conditional
source-paid bounds, not acquired theta values.

Four consumers were distinguished in [Note 05 §1][n5]: spatial Gauss area,
the physical tube/phase cap, the critical-wall amplitude budget, and BW12's
complete signed endpoint response. Their dimensions, denominators and
signs differ. The present write-up concerns the first and third. It
supplies no transform from this positive mass to the full Weil form or
the complete BW12 covariance response.

For the canonical-source application, use exactly
H(tau,z)=int_0^infinity exp(tau u²)Phi(u)cos(zu)du, with the unchanged
full source and reflection ledger in home 02. Thus H is real on the real
slice and

\[
 \mathsf C_j(t,x)=\int_0^\infty u^j e^{tu^2}\Phi(u)\cos(xu)\,du,
 \qquad
 \mathsf S_j(t,x)=\int_0^\infty u^j e^{tu^2}\Phi(u)\sin(xu)\,du.
\]

On the real critical wall x=c(t),

\[
 \mathsf S_1=0,\quad V=\mathsf C_0,\quad V'=\mathsf C_2,
 \quad q=-H_{xx}/H=V'/V,\quad \sigma=\operatorname{sign}V,
\]
\[
 \boxed{\sigma(\mathsf C_2-k\mathsf C_0)=|V|(q-k).}       \tag{1}
\]

Thus an upper q budget controls a specified signed moment budget. It
does not follow merely from positivity of a four-dimensional density.
No RH hypothesis is used in the local results below. A separately
declared all-real paired-product theorem may supply q>0 in a simple gap;
the square q² itself does not supply that sign.

## 2. Evaluated full boundary and positive mass

With g=G/sqrt(E), A=-ig*dg and C=A wedge dA/(4pi²), [Note 03][n3] proves

\[
 Q=\int_{\partial W}\mathcal C
       ={1\over2\pi}\oint_{\partial D}d\arg V.
                                                               \tag{2}
\]

Both projective charts, all four heat faces and the spatial wall are
retained. The wall generally has nonzero flux; its separate contribution
cancels only in the full assembly. The conditional ordinary double has
Q=1. This evaluates the inherited local charge/discriminant winding;
it adds no arithmetic information by itself.

For delta>0, [Note 04][n4] gives the positive measure

\[
 d\mu_\delta=
 \left({i\over2\pi}\partial\bar\partial\log(E+\delta^2)\right)^2
 ={2\delta^2|J|^2\over\pi^2(E+\delta^2)^3}\,dV.
\]

If E>=e_0>0 on the complete boundary, ||DG||<=L there, and S is its
three-volume, then

\[
 |\mu_\delta(W)-Q|\le B_\delta
 \le\beta\delta^2,\qquad
 \beta={SL^3\over\pi^2e_0^{5/2}}.
\]

Every bounded measurable weight obeys

\[
 \left|\int_W w\,d\mu_\delta\right|
                    \le\|w\|_\infty(Q+B_\delta).         \tag{3}
\]

These are useful bounds for their specified density and weights.
Singular weights need additional payment. Weighted Stokes also retains
the integral of dw wedge C_delta. An unnormalized determinant integral
still pays delta^(-2); neither that cost nor a real-curve trace is removed
by the charge evaluation.

## 3. Spatial Gauss-area calibration

Put D_z=HH_zz-H_z² and

\[
 g_2={|D_z|^2\over E^2},\qquad
 N_\delta=|D_z|^2+\delta^2(|H_z|^2+|H_{zz}|^2),\qquad
 \gamma_\delta={N_\delta\over\pi(E+\delta^2)^2}.
\]

The unregularized raw Gauss area is integral g_2 dA_z; gamma_delta
uses normalization by pi. The exact spatial Green formula is

\[
 \int_\Omega\gamma_\delta\,dA_z
 ={1\over4\pi}\int_{\partial\Omega}
                  \partial_n\log(E+\delta^2)\,ds.        \tag{4}
\]

Using Note 03's constants |H|<=M_0, |H_z|<=epsilon_1, |H_zz|<=D_2
and E>=m_*² on the spatial wall, define

\[
 F_\delta={4TYR\epsilon_1(M_0+D_2)\over m_*^2+\delta^2}.
\]

It bounds the complex-time averaged normalized area and stays finite
as delta tends to zero. The same data pay the absolute area bias

\[
 Z_\delta={\delta^2\over m_*^2+\delta^2}F_0,
 \qquad F_\delta+Z_\delta=F_0.                           \tag{5}
\]

This uses a floor only on the spatial wall. The zero-regulator boundary
expression at the event includes its normalized defect mass one, in
addition to the canceled smooth Gauss map; it does not discard that atom.

The exact bulk interface uses the mixed-curvature Schur complement

\[
 s_\delta={\delta^2|J|^2\over(E+\delta^2)N_\delta},\qquad
 d\mu_\delta={2\over\pi}s_\delta\gamma_\delta\,dV.
\]

A paid s_delta>=c_delta gives the upper certificate
T_delta=pi(Q+B_delta)/(2c_delta). For **Note 04's existing global
constant c_delta on Note 03's sufficient ordinary-double window**, [Note 05][n5]
proves for every delta>0

\[
 T_\delta\ge{5242880\pi\over23273}
                 \left({D_2\over h}\right)^4 F_0>707F_0,
 \qquad h=|h_2|,\quad D_2\ge h.                         \tag{6}
\]

This compares upper certificates, not the true integrals. Choosing a
finite regulator cannot rescue that implementation. Other windows,
sharper/localized curvature information or an error term in a complete
signed expression are outside this scoped failure.

## 4. The sharp spatial critical-wall trace

On H!=0 write p=H_z/H. Then

\[
 g_2={|p_z|^2\over(1+|p|^2)^2},\qquad
 g_2(t,c(t))=q(t)^2.
\]

On a zero-free disk |z-c|<=r with p(c)=0 and |p|<=P, [Note 06][n6] proves

\[
 \boxed{q(t)^2\le{1+P^2\over\pi r^2}
                           \int_{|z-c|<r}g_2\,dA_z.}   \tag{7}
\]

Indeed Schwarz gives |p(c+w)|<=P|w|/r. The circle mean of |p_z|² is
at least |p_z(c)|², and the radial denominator integral is
pi r²/(1+P²). Equality holds for linear p. This improves the less sharp
unweighted-submean factor (1+P²)² while retaining its hypotheses.

The critical value pays the hypotheses:

\[
 |H(c+w)|\ge|V|-D_2r^2/2>0,\qquad
 |p|\le {D_2r\over|V|-D_2r^2/2}.                        \tag{8}
\]

Near the conditional double, V=tB with b<=|B|. Thus r proportional to t
keeps P bounded and (7) prices a t^(-2) squared trace. For the larger
zero-free scale r=rho sqrt(t), the sharp factor gives the correct
logarithmic q budget rather than a spurious power divergence. But a
uniform normalized area allowance a_* on that scale is at least one:
the inner disks z=c(t)+ty carry limiting density (1+|y|²)^(-2)dA_y.
That uniform-area certificate does not improve direct D_2/(bt).

## 5. Full bulk-to-curve cost and matched direct comparison

For completeness, the four-dimensional to one-dimensional trace can be
paid, rather than presumed. Note 03 supplies |c-a|<=3R/8,
b=h-eta>=3h/4, b_+=h+eta, eta<=h/4, and |J|>=j_0=37h²/64.
Set t_*=d/4, alpha=1/2 and choose rho>0 so that
rho t_*<=5R/8 and H_-=b(1-alpha)-D_2rho²t_*/2>0. The complex tube is

\[
 \mathcal U_t=\{|\tau-t|<\alpha t,\ |z-c(\tau)|<\rho t\}\subset W.
\]

Define, exactly as in [Note 06 §3][n6],

\[
 H_+=b_+(1+\alpha)+D_2\rho^2t_*/2,\quad P=D_2\rho/H_-,
 \quad U=H_+^2+D_2^2\rho^2,
\]
\[
 A=D_2H_++D_2^2\rho^2t_*,\quad
 N=A^2+\lambda^2D_2^2(1+\rho^2t_*^2),\quad
 c_*={\lambda^2j_0^2\over(U+\lambda^2)N},\quad\lambda>0.
\]

Use delta=lambda t, held constant in each application on W. The spatial
trace (7), then the heat-disk submean for holomorphic V'/V, costs
(1+P²)/(pi²alpha²rho²t^4). The actual tube has
s_delta>=c_*/t² and regulator-bias multiplier
(1+lambda²/H_-²)². Combining these with (3) gives

\[
 |q(t)|\le{C_{\rm top}\over t},\qquad
 C_{\rm top}=\left(1+{\lambda^2\over H_-^2}\right)
 \sqrt{{(1+P^2)(1+\beta\lambda^2t_*^2)\over2\alpha^2\rho^2c_*}}.
                                                               \tag{9}
\]

The transformation z=c(tau)+w has complex determinant one. All mass
errors are paid on the complete fixed W, including its spatial wall and
imaginary-time faces. This is a genuine bound with the correct logarithmic
endpoint order. It is not an unpriced conversion of an average to a trace.

However N>=lambda²D_2² and U>=D_2²rho² imply

\[
 {C_{\rm top}\over D_2/b}
          \ge{48\sqrt2\over37}{D_2\over h}>1.            \tag{10}
\]

Thus this **tube/local-Schur/total-mass certificate** is weaker than
the equally informed direct |q|<=D_2/(bt). Local scaling repairs the old
inverse-regulator power loss; it does not establish an estimating gain.
A sharper acquired local mass or coupled signed estimate is not excluded.

## 6. Signed endpoint cancellation and its first regular coefficient

The useful signed information comes from retaining the critical-value
coupling. Put a_2=h-epsilon_2>=7h/8 and

\[
 K_0={1\over2}(D_4+D_3^2/a_2),\qquad K=K_0/b.
\]

Differentiating H_z(t,c(t))=0 and using the heat equation gives

\[
 c'={H_{zzz}\over H_{zz}},\qquad
 V'=-H_{zz},\qquad
 V''=H_{zzzz}-{H_{zzz}^2\over H_{zz}},\qquad |V''|\le2K_0.
\]

Since V=tB, B'=int_0^1 sV''(st)ds, so |B'|<=K_0. Therefore

\[
 \boxed{q={1\over t}+r,\quad |r|\le K,\qquad
 \mathsf C_2-{\mathsf C_0\over t}=tB',\quad |tB'|\le K_0t.}
                                                               \tag{11}
\]

Combining (1) and (11) gives the paid barrier
sigma[C_2-(1/t+K)C_0]<=0 and

\[
 \left|\int_\epsilon^{t_*}q\,dt-\log(t_*/\epsilon)\right|
                                      \le K(t_*-\epsilon).      \tag{12}
\]

The residual has finite endpoint limit log(|B(t_*)|/h). It preserves the
compulsory coefficient one; it does not give ICW's strictly subunit
logarithmic budget. Direct critical-value estimation with the same data
derives the identical signed remainder.

There is also a signed center. With h_j=H_{z^j}(0,a),

\[
 r_0={h_3^2-h_2h_4\over2h_2^2}
      ={\mathsf C_2\mathsf C_4+\mathsf S_3^2\over2\mathsf C_2^2}
                     \quad\hbox{at the conditional event}.
\]

The existing unit bound |B+h_2|<=eta on |tau|<=d gives, by Cauchy,

\[
 K_1={8\eta\over bd^2}+K^2,\qquad
 |r(t)-r_0|\le K_1t,
\]
\[
 \left|\int_\epsilon^{t_*}q\,dt-\log(t_*/\epsilon)
                -r_0(t_*-\epsilon)\right|
                 \le{K_1\over2}(t_*^2-\epsilon^2).       \tag{13}
\]

Hence k(t)=1/t+r_0+K_1t is an upper barrier in (1). The actual theta
sign of C_2C_4+S_3² is unpaid; positivity of the source does not assign it.
For the square trace, the correct subtraction has **two** singular terms:

\[
 |q^2-t^{-2}-2r_0t^{-1}|\le2K_1+K^2.                   \tag{14}
\]

For the exact heat quartic H=z²-2t+nu(z^4-12tz²+12t²),
c=0 and q=1/t-6nu/(1-6nu t), so r_0=-6nu has either sign while the local
ordinary-double charge remains one. The subleading 2r_0/t cannot be
discarded as an integrable error.

## 7. Regulator, acquisition and next source payments

On the critical wall the exact regularized density is

\[
 \pi\gamma_\delta={V'^2\over V^2+\delta^2},\qquad
 q^2=\left(1+{\delta^2\over V^2}\right)\pi\gamma_\delta.
\]

Fixed delta costs up to 1+delta²/(b²epsilon²) on [epsilon,t_*]. For the
signed q_delta=VV'/(V²+delta²), the lost budget is exactly

\[
 \int_\epsilon^{t_*}(q-q_\delta)dt
 ={1\over2}\log{1+\delta^2/V(\epsilon)^2
                         \over1+\delta^2/V(t_*)^2}.      \tag{15}
\]

It restores log(1/epsilon) at fixed delta. Adaptive delta=lambda t adds
delta delta'/(V²+delta²) to the derivative of the regularized primitive;
its leading term is lambda²/[t(h²+lambda²)]. Neither regularization
choice deletes the endpoint budget.

For a real wall approximation |hat c-c|<=omega, with absolute source
errors e_j at hat c, the coupled moment allowance is

\[
 E_k\le e_2+|k|e_0+D_3\omega+|k|D_2\omega^2/2.          \tag{16}
\]

The C_0 wall error is quadratic because H_z(c)=0. All segments, tails,
quadrature, rounding and the sign sigma must be paid from the same
unchanged canonical source. For k=1/t+O(1), e_2=O(t), e_0=O(t²) and
omega=O(t) suffice to preserve an O(t) canceled-moment allowance. These
are sufficient accuracy scales, not a complexity theorem or a certificate
of exact event matching. Here e_j denotes source error, not the earlier
complete-boundary energy floor e_0.

An acquired r_0 error e_r costs e_r(t_*-epsilon) in (13), but
2e_r log(t_*/epsilon) in the integrated square subtraction (14). Fixed
positive coefficient uncertainty does not certify a bounded renormalized
square endpoint integral.

The [collision-control register][controls] applies with its separate
preservation lists: H=z fails the ordinary-double/J-floor hypothesis;
polynomial controls retain local collisions; Euler-factor controls change
the canonical arithmetic; weighted-square/finite-prime controls fail full
reflection/unchanged coefficients and are not assigned an all-real heat
slice; reflected/primitive controls lack the canonical square expansion;
close RH-conditional endpoint controls fail ordinary Dirichlet arithmetic.
No control is being assigned theta's complete source. The results are
expected to pass at matching analytic event germs.

**What remains open.** Acquire or prove a genuinely sharper coupled signed
theta estimate, or a localized mass/error estimate for a named complete
consumer, and compare it with direct estimation receiving the same
information. Home 02 remains the common source supplier. Neither scoped
certificate failure closes all weighted/localized methods. No actual
theta sign, exclusion margin, higher-multiplicity or all-height conclusion
follows from this local write-up.

## Source and review map

Shared [Notes 01–02][notes] hold the chart primitives and punctured sectors;
[Note 03][n3] completes the physical boundary and pays geometry/floors;
[Note 04][n4] gives mass and bounded-weight estimates; [Note 05][n5] proves
the direct area/bias and global-certificate comparison; [Note 06][n6]
proves the sharp trace and signed endpoint estimates. Original internal
[Review 05][r5], [Review 06][r6] and [Review 07][r7] retain their contributing-agent
scope. The [Gauss receipt][c5] and [critical-wall receipt][c6] bind their
original exact finite-algebra scripts and sources; they are not analytic
formalizations or theta certificates. This home's [write-up review][review]
checks faithful presentation and routing, with no new validation claim.

[n3]: ../../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[n4]: ../../notes/04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md
[n5]: ../../notes/05_TARGET_INVENTORY_AND_FINITE_REGULATOR_GAUSS_COMPARISON_20261022.md
[n6]: ../../notes/06_CRITICAL_WALL_TRACES_AND_SIGNED_ENDPOINT_BUDGET_20261022.md
[notes]: ../../notes/README.md
[r5]: ../../03_heat_transport_and_charges/reviews/05_COMPLETE_BOUNDARY_AND_INTEGRAL_BOUNDS_REVIEW_20261022.md
[r6]: ../../03_heat_transport_and_charges/reviews/06_FINITE_REGULATOR_GAUSS_COMPARISON_REVIEW_20261022.md
[r7]: ../../03_heat_transport_and_charges/reviews/07_CRITICAL_WALL_TRACE_AND_ENDPOINT_BUDGET_REVIEW_20261022.md
[c5]: ../../03_heat_transport_and_charges/numerics/CHB_GAUSS_COMPARISON_CHECKS_20261022.json
[c6]: ../../03_heat_transport_and_charges/numerics/CHB_CRITICAL_WALL_CHECKS_20261022.json
[review]: ../reviews/01_HOME_AND_RESULTS_WRITEUP_REVIEW_20261022.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
