# Moving signed tubes and the physical cap trace

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Status: **proved in-note for the declared
bounded product tubes; same-assistant self-review only**. No specialist
review, new theta sign estimate, or simplicity exclusion.

This completes HMC-04 for one explicit domain class. It gives the moving
phase law, all eight faces of a four-dimensional signed Stokes formula,
its physical-energy correction, and a quantitative trace and transport
remainder. An exact change of primitive reduces this tube formula to a
planar transverse average. Under RH that average is at least the known
cap budget, with an explicitly paid excess. The comparison supplies no
additional signed gain.

Read with the [program][program], [progress][progress],
[result index][results], [geometric summary][geometry], [controls][controls]
and [avoid index][avoid], particularly [geometric re-realizations][a03],
[separate payments][a12], and [scoped conclusions][a07].

## 1. Domain and data contract

Retain the unchanged source and normalization of [Note 19][n19]:
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad 8H(0,z)=\xi(1/2+iz/2).
\]
Write \(h_j=\partial_z^jH\). Assume RH for the continued cap and the
all-real product conclusions. Fix \(0<\epsilon<T<\infty\), adjacent
positive root labels \(a=x_k,b=x_{k+1}\), \(g=b-a\),
\(c=(a+b)/2\), and a bound \(|a|,|b|\le A\) on this interval.
Note 19 RM9 supplies such a bound. The roots are simple for positive time.
On the physical rectangle define
\[
E(t,x)=h_0(t,x)^2+h_1(t,x)^2,\qquad
E(t,x)\ge e_*>0\quad
(\epsilon\le t\le T,\ |x|\le A).
\tag{MT1}
\]
This is a paid compact-interval input, not an assumed endpoint floor.
Section 6 gives complete-source bounds and a finite certificate rule for
it. Compactness and positive-time simplicity imply that a positive floor
exists; no numerical value is asserted here.

Use \(z=x+iv,w=p+iq\), Euclidean orientation
\(dx\wedge dv\wedge dp\wedge dq\), fixed \(U,V>0\), and a
positive \(C^1\) thickness \(0<\eta(t)\le\eta_*<\infty\). Set
\[
\Omega_t=[a(t),b(t)]\times[-\eta(t),\eta(t)]
                 \times[-U,U]\times[-V,V].
\tag{MT2}
\]
Stokes applies to this rectangle with corners. Time is an external
parameter, not one of the four spatial coordinates. The physical trace
means evaluation of a scalar coefficient at \(v=0\), not pullback of a
four-form to a line. No Fueter auxiliary heat coordinate is involved.

## 2. Physical phase transport, including the moving scale

Define the physical phase density and time current by
\[
\rho=\frac{h_1^2-h_0h_2}{E},\qquad
\omega=\frac{h_1h_2-h_0h_3}{E}.
\]
For \(J=H+iH_x\), direct differentiation gives
\[
-\partial_x\arg J=\rho,\qquad
\partial_t\arg J=\omega,\qquad
\rho_t+\omega_x=0.
\tag{MT3}
\]
These identities need only a real heat solution and \(E>0\).
Since \(J\ne0\) on the rectangle, compatible phase branches exist.
At either root \(r=a,b\), \(\rho(t,r)=1\) and
\(\omega(t,r)=h_2/h_1=r'\). Consequently
\[
\frac d{dt}\int_a^b\rho\,dx
=-[\omega]_a^b+b'\rho(b)-a'\rho(a)=0.
\tag{MT4}
\]
The adjacent-root cap has \(\int_a^b\rho\,dx=\pi\): between its
endpoints \(H\) has a fixed sign, so its jet stays in one open half-plane,
with the two opposite imaginary endpoint directions. This is the inherited
cap budget, not a new inequality.

Put \(K(t,y)=H(t,c+gy)\), \(-1/2\le y\le1/2\), and
\(v_c(t,y)=c'+g'y\). The full fixed-domain law is
\[
K_t=-g^{-2}K_{yy}+v_cg^{-1}K_y,\quad
J=K+iK_y/g,\quad
\partial_t(g\rho)+\partial_y(\omega-v_c\rho)=0.
\tag{MT5}
\]
Here densities on the right are evaluated at \(x=c+gy\).
In differentiating the jet, its imaginary component is
\(K_{yt}/g-g'K_y/g^2\). This cancels the spurious scale term that
would result from replacing the physical derivative by \(K_y\).
The flux \(\omega-v_c\rho\) vanishes at both ends.

## 3. Polarized Stokes, the weight correction, and all faces

Use [Investigation 21 Note 50][g50]'s real self-dual forms
\(\alpha_f=\operatorname{Re}(f\,dz\wedge dw)/\sqrt2\) and
\(\beta_f=\operatorname{Re}(P_f\,dw)/\sqrt2\), with \(P_f'=f\).
Choose \(P(t,z)=\int_0^zH(t,\zeta)d\zeta\), and choose \(P_{h_1}=H\).
Define
\[
Q(t,x,v)=|h_1(t,z)|^2-\operatorname{Re}(h_0(t,z)\overline{h_2(t,z)}),
\]
\[
C=h_0\overline{h_1}-P\overline{h_2},\qquad
\mathsf A=-\tfrac12\operatorname{Im}C,\quad
\mathsf B=\tfrac12\operatorname{Re}C,\quad
\theta=\mathsf A\,dx+\mathsf B\,dv.
\]
Expansion of the forms gives
\[
\beta_{h_1}\wedge\alpha_{h_1}-\beta_{h_0}\wedge\alpha_{h_2}
=\theta\wedge dp\wedge dq,\qquad
\mathsf B_x-\mathsf A_v=Q.
\tag{MT6}
\]
The factor \(1/2\) and the sign of \(\mathsf A\) follow from the
declared orientation. Introduce the physical weight \(W(t,x)=1/E(t,x)\),
independent of \(v,p,q\). Spatial differentiation yields
\[
d(W\theta\wedge dp\wedge dq)
=(WQ+W_x\mathsf B)\,dx\wedge dv\wedge dp\wedge dq.
\tag{MT7}
\]
Thus the weight derivative cannot be discarded in this primitive.
Let a bar denote the normalized transverse average over \([-\eta,\eta]\),
and put \(F=WQ\), \(I_\eta=\int_a^b\overline F\,dx\). The exact
normalized Stokes formula is
\[
I_\eta=\mathcal B_\eta-\mathcal W_\eta,
\tag{MT8}
\]
\[
\mathcal B_\eta=\frac1{2\eta}\left\{
\int_{-\eta}^{\eta}[W(b)\mathsf B(b,v)-W(a)\mathsf B(a,v)]\,dv
+\int_a^b W(x)[\mathsf A(x,-\eta)-\mathsf A(x,\eta)]\,dx\right\},
\quad
\mathcal W_\eta=\int_a^b W_x\overline{\mathsf B}\,dx.
\]
This displays every nonzero face: the \(x=b,a\) faces have respectively
positive and negative \(dv\wedge dp\wedge dq\) orientation; the
\(v=\eta,-\eta\) faces have respectively negative and positive
\(dx\wedge dp\wedge dq\) orientation. On each of the four \(p,q\)
faces, the pullback of \(dp\wedge dq\) is zero. Their fluxes vanish
exactly. The common auxiliary area \(4UV\) cancels in the normalization.

There is a useful exact simplification, which must not be confused with
dropping \(\mathcal W_\eta\). Set \(G=|H(t,x+iv)|^2\) and
\(\psi=\tfrac12\operatorname{Im}(P\overline{h_1})\). Direct calculation gives
\[
Q=\tfrac12G_{vv},\qquad
\theta=-\tfrac12G_v\,dx+d\psi,\qquad \psi_v=\mathsf B.
\tag{MT9}
\]
The boundary integral of \(W\,d\psi\) equals the correction
\(\int W_x\mathsf B\,dx\,dv\). In the equivalent primitive
\(-G_vdx/2\), this cancellation has already been performed, and
\(dW\wedge dx=0\). Real symmetry makes \(G\) even in \(v\), so
\[
\boxed{I_\eta=\int_a^b\frac{G_v(t,x,\eta)}{2\eta E(t,x)}\,dx.}
\tag{MT10}
\]
For this product domain and this weight, the entire four-dimensional
construction is exactly the planar transverse observation MT10.
This is a scoped equality, not a prohibition of different domains,
weights, source correlations or geometric estimates.

## 4. Quantitative physical trace and moving-domain remainder

Take uniform complete jet bounds \(|h_j(t,x+iv)|\le M_j\) for
\(0\le j\le6\), \(\epsilon\le t\le T\), \(|x|\le A\),
\(|v|\le\eta_*\). Define
\[
L_x=2(M_0M_1+M_1M_2),\quad L_t=2(M_0M_2+M_1M_3),
\]
\[
D_0=\frac{3M_2^2+4M_1M_3+M_0M_4}{e_*},
\quad
D_1=\frac{4M_3^2+7M_2M_4+4M_1M_5+M_0M_6}{e_*}
       +\frac{L_tD_0}{e_*}.
\tag{MT11}
\]
Indeed,
\[
Q_{vv}=3|h_2|^2-4\operatorname{Re}(h_1\overline{h_3})
                  +\operatorname{Re}(h_0\overline{h_4}),
\]
\[
Q_{vvt}=4|h_3|^2-7\operatorname{Re}(h_2\overline{h_4})
            +4\operatorname{Re}(h_1\overline{h_5})
            -\operatorname{Re}(h_0\overline{h_6}).
\]
Since \(|E_t|\le L_t\), these imply
\(|F_{vv}|\le D_0\), \(|F_{tvv}|\le D_1\). The denominator here
is physical \(E(t,x)\), not the generally different complex jet energy.

Evenness in \(v\) gives the exact signed remainder
\[
R_\eta:=I_\eta-\int_a^b\rho\,dx
=\int_a^b\frac1{E(t,x)}\int_0^\eta
       \frac{(\eta-s)^2}{2\eta}Q_{vv}(t,x,s)\,ds\,dx,
\quad
|R_\eta|\le\frac{g\eta^2D_0}{6}.
\tag{MT12}
\]
The constant follows by integrating the kernel, whose integral is
\(\eta^2/6\). No sign of a separate Hodge sector is used.

Differentiating the normalized moving integral, rather than treating its
domain or its normalization as fixed, gives
\[
I_\eta'=\int_a^b\overline{F_t}\,dx
+b'\overline F(b)-a'\overline F(a)
+\frac{\eta'}\eta\int_a^b
 \left\{\frac{F(x,\eta)+F(x,-\eta)}2-\overline F(x)\right\}dx.
\tag{MT13}
\]
The last braces contain both moving transverse faces and the derivative
of \(1/(2\eta)\). Equivalently this is the full derivative of
\(\mathcal B_\eta-\mathcal W_\eta\), including the time dependence of
its primitive and physical weight. Its interior derivative is explicitly
\[
F_t=\frac{|h_2|^2-2\operatorname{Re}(h_1\overline{h_3})
                      +\operatorname{Re}(h_0\overline{h_4})}{E}
+\frac{2(h_0h_2+h_1h_3)(t,x)\,Q(t,x,v)}{E^2},
\]
where the numerator in the first fraction uses the complex point and
the second fraction's parenthesized jets use the physical point.
For the original even theta function
\(P_t=-h_1\); a general non-even control instead has
\(P_t=-h_1+h_1(t,0)\), which must be kept if that representation is
differentiated directly.

Subtract MT4 from MT13. Taylor's formula gives
\[
\boxed{|R_\eta'|\le
\frac{\eta^2}{6}\{gD_1+(|a'|+|b'|)D_0\}
+\frac{g\eta|\eta'|D_0}{3}.}
\tag{MT14}
\]
For the last constant, evenness and \(|F_{vv}|\le D_0\) give
\(\left|F(\eta)-\overline F\right|\le D_0\eta^2/3\), by writing
the difference as \(\eta^{-1}\int_0^\eta sF_v(s)ds\).
Note 19 supplies finite/complete velocity comparisons. A cruder fully
declared bound is \(|a'|+|b'|\le2M_2/\sqrt{e_*}\), since at the
endpoints \(E=h_1^2\). This also proves finiteness of MT14 without an
unpaid inverse nearest-neighbor gap. No bound uniform as
\(\epsilon\downarrow0\) is obtained.
The compact theorem makes no isolated-double assumption: the complete
field and every member of a possible higher birth cluster remain in its
jets. The quadratic control below is only a witness against an unpaid
generic endpoint estimate.

For completeness, the original faces and weight correction have finite
absolute allowances. Put
\[
P_*=\sqrt{A^2+\eta_*^2}\,M_0,\quad
B_*=(M_0M_1+P_*M_2)/2,\quad
A_{1*}=(M_1^2+2M_0M_2+P_*M_3)/2.
\]
The straight primitive path remains in the strip, so \(|P|\le P_*\).
Also \(\mathsf A(t,x,0)=0\), \(|\mathsf A_v|\le A_{1*}\).
Therefore
\[
|\mathcal B_\eta|\le(2B_*+gA_{1*})/e_*,\qquad
|\mathcal W_\eta|\le gL_xB_*/e_*^2.
\tag{MT15}
\]
These are finiteness/payment bounds, not a sign estimate obtained by
paying sectors separately. If numerical enclosures of the two quantities
have absolute errors \(\delta_B,\delta_W\), their physical-observation
error is at most \(\delta_B+\delta_W+g\eta^2D_0/6\). No such
evaluation or cost benchmark has been run in this round.

## 5. The matched comparison has an upward, generic excess

Under RH, Note 19's paired product is a locally uniform limit of real-root
polynomials. For such a polynomial,
\[
|p(x+iv)|^2=c^2\prod_r((x-r)^2+v^2)
\]
has nonnegative coefficients in \(v^2\). Local uniform convergence,
also viewed as \(p(x+iv)p(x-iv)\) for complex \(v\), passes this
coefficient property to \(H\). Thus
\[
G(t,x,v)=\sum_{n\ge0}\ell_n(t,x)v^{2n},\qquad \ell_n\ge0.
\]
These are the classical generalized Laguerre coefficients, not a new
theta-specific positivity theorem. See Csordas–Vishnyakova,
[Theorem 1.2 and equation (1), pp. 1644–1645](https://d-nb.info/1372516522/34),
*The generalized Laguerre inequalities and functions in the
Laguerre–Pólya class* (2013),
[DOI](https://doi.org/10.2478/s11533-013-0269-x).
The product argument above suffices for the present direction; no converse
criterion is used.

MT9–MT10 now give, for fixed \(t\),
\[
I_\eta=\pi+
\int_a^b\frac{\sum_{n\ge2}n\ell_n(t,x)\eta^{2n-2}}{E(t,x)}dx,
\qquad
\boxed{\pi\le I_\eta\le\pi+g\eta^2D_0/6.}
\tag{MT16}
\]
The excess is nondecreasing in thickness. At fixed source data the
four-dimensional formula and MT10 give exactly the same observation;
the direct physical cap has no transverse trace error. This equality
establishes no computational speed comparison and no dominance theorem
for other estimating classes. In particular, an upper bound
\(I_\eta<\pi\) cannot hold for any genuine adjacent cap in this class,
regardless of how its endpoints arose. Keeping the known cap budget on
one side and its geometric reproduction on the other is not independent
information.

## 6. Complete-source constants and a finite floor rule

All jet allowances may be taken as
\[
M_j=\int_0^\infty u^j e^{Tu^2+\eta_*u}\Phi(u)\,du,
\qquad 0\le j\le6.
\tag{MT17}
\]
They converge because Note 19 proves
\(0<\Phi(u)\le C_\Phi e^{9u-\pi e^{4u}}\),
\(C_\Phi=2\pi^2/(1-16e^{-3\pi})\).
For a concrete tail rule, choose \(L\ge1\) with
\(16\pi e^{4L}\ge2T\) and
\(\lambda_j=4\pi e^{4L}-2TL-9-\eta_*-j/L>0\). Concavity of
\(Tu^2+(9+\eta_*)u+j\log u-\pi e^{4u}\) for \(u\ge L\) yields
\[
\int_L^\infty u^j e^{Tu^2+\eta_*u}\Phi(u)du
\le\frac{C_\Phi L^j
 e^{TL^2+(9+\eta_*)L-\pi e^{4L}}}{\lambda_j}.
\tag{MT18}
\]
On \([0,L]\), truncation after theta index \(N\ge1\) has allowance
\[
\frac{2\pi^2 L^{j+1}(N+1)^4
 e^{TL^2+(9+\eta_*)L-\pi(N+1)^2}}{1-r_N},\qquad
r_N=\left(\frac{N+2}{N+1}\right)^4e^{-\pi(2N+3)}<1.
\tag{MT19}
\]
This follows from the ratio of successive positive \(n^4\) majorants;
dropping each negative source term is used only for this error allowance.
Finite-interval quadrature needs its own outward-rounded error. The
formulas specify both infinite tails, not a finite-band source model.

One can obtain MT1 by a finite grid on
\([\epsilon,T]\times[-A,A]\). Suppose certified point values give lower
bounds \(e_j\) for \(H^2+H_x^2\), and every point of the rectangle
is within \(\delta_t,\delta_x\) of a grid point. Then
\[
e_*:=\min_j e_j-L_t\delta_t-L_x\delta_x>0
\tag{MT20}
\]
is a valid floor. The same complete-source tails apply to the evaluated
jets. Under the declared RH/positive-time assumptions, mesh refinement
and tightening evaluation errors eventually succeed, since the actual
compact minimum is positive. This is a terminating certificate procedure
in principle, with no claimed practical complexity or numerical receipt.
It does not assume or certify a floor at an original multiple endpoint.

## 7. Signed source residual and collision screening

There is a complete signed two-source expression for the remaining
trace payment. Set \(d\mu_t(u)=e^{tu^2}\Phi(u)du\), and
\(d(s)=\sinh(s)/s-1\), with \(d(0)=0\). Symmetrizing the
\(h_0\overline{h_2}\) term and using the cosine product identities gives
\[
R_\eta=\frac14\int_a^b\frac{dx}{E(t,x)}
\iint_{[0,\infty)^2}\left\{
(u+v)^2\cos((u-v)x)d(\eta(u+v))
+(u-v)^2\cos((u+v)x)d(\eta(u-v))
\right\}d\mu_t(u)d\mu_t(v).
\tag{MT21}
\]
Here \(v\) inside the double integral is a source variable only.
The double integral divided by four, with \(\cosh\) in place of
\(d\) and thickness replaced by transverse displacement, equals \(Q\).
Complete-source decay justifies
all products and exchanges on the bounded strip. Positive source weights
or \(d\ge0\) alone do not assign a sign to the oscillating terms.
MT16's sign uses the all-real product. Any future improved arithmetic
payment must retain the correlations in MT21 and outperform its declared
bound on a specified consumer; its representation is not that estimate.

The quadratic heat solution \(H(t,z)=z^2-2t\), \(t>0\), makes the
trace loss explicit:
\[
Q=2x^2+4t+6v^2,\quad E=(x^2-2t)^2+4x^2,\quad
R_\eta=2\eta^2\int_{-\sqrt{2t}}^{\sqrt{2t}}\frac{dx}{E(t,x)}.
\tag{MT22}
\]
The Taylor remainder constant \(1/6\) in MT12 is exact pointwise for
this quadratic transverse coefficient. For \(0<t\le1\), restrict the
integral to \([-t,t]\), where \(E\le8t^2\), to obtain
\[
R_\eta\ge\eta^2/(2t).
\tag{MT23}
\]
Fixed thickness diverges as the double endpoint is approached, and
\(\eta=c\sqrt t\) still leaves a nonvanishing excess. Translating the
polynomial places the double at any desired positive height. This
closes only an unpaid uniform trace-recovery claim for this generic
class; it does not exclude a theta-specific improvement.

| Control | What survives | Missing premise or limitation |
| --- | --- | --- |
| Quadratic and real-root Hermite heat polynomials | Phase law, signed Stokes, gauge reduction and nonnegative transverse coefficients; MT22 is exact | No original theta source or infinite theta spectrum; use their finite jet bounds, not MT17's theta constants |
| Positive atomic \(1+e^t\cos z\) | Double at \((0,\pi)\), later all-real simple roots; compact trace and geometric laws apply | Discrete source, not the normalized theta expansion; no HMC-02 theta saddle |
| Euler-factor control with \(c=1\), under RH | All-real endpoint with doubles and simple positive-time slices; the same generic identities and compact trace procedure apply | Changed completion and arithmetic coefficients; recalculate its source constants |
| Close positive endpoint controls of [Note 05][n05], under RH | Positive-time all-real slices and generic tube laws are compatible with the added original double | Original ordinary Dirichlet arithmetic fails; their separate preservation lists are not combined |
| Weighted-square and finite-prime controls | Local identities apply wherever a nonvanishing real jet and suitable real cap exist | No all-real heat slice for these nontrivial finite-source perturbations; do not apply the all-real-product conclusion to their full spectrum |
| Reflected and positive-primitive controls | Local polarized identities and bounded-strip trace estimates with their own constants | No original normalized integer-square expansion; no all-real heat slice is assumed here |

The successful compact trace estimate is therefore **not separating**.
HMC-04 is complete on MT2, while HMC-05's additional theta estimate and
HMC-06's endpoint exclusion remain open. The next bounded task is to
select and compare one complete-source correlation payment from MT21 or
the original phase current, with an explicit endpoint scale and control
response. No new contour construction or trajectory scan is justified
merely by the identities above.

The [finite exact replay][script] checks heat-polynomial orientation,
gauge, phase, transverse derivative and moving-average identities; its
[record][replay] is finite algebra only. [Review 20][review] records the
same-assistant assessment. The manuscript is unchanged in this round.

[program]: ../research-overview/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRAM_20261021.md
[progress]: ../research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[n19]: 19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[n05]: 05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[g50]: ../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[review]: ../reviews/20_MOVING_TUBE_AND_TRACE_REVIEW_20261021.md
[script]: ../numerics/check_hmc_moving_tube_algebra.py
[replay]: ../numerics/HMC_MOVING_TUBE_ALGEBRA_REPLAY_20261021.json
