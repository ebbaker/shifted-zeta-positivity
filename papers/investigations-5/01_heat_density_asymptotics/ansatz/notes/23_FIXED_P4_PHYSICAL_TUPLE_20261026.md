# Fixed-P4 physical tuple on the compact regulator switch

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, base chat0025, thread `01a179ab-8856-7ba0-89a2-500b2d854c80`,
turn `01a179ec-1178-7b91-a108-042fe3108232`. Configuration is verified
from the public session's turn metadata. Contributing agents supplied
read-only same-model analytical checks, not independent validation.

**Status: proved in-note from named inputs, same-model internal
assessment only. HDA-A03-AN02 r1 closes at its frozen fixed-P4 physical
scope.** All requested rows hold on [63,65] at sufficiently large height.
The proof below establishes the corrected collars and weak consumers;
it does not replace an error symbol in the earlier leading-model theorem.
No numerical, machine-symbolic, sampling or interval research was run.

The [opening manifest](23_FIXED_P4_PHYSICAL_TUPLE_INPUTS_20261026.json)
pins the exact request and current inputs. [Assessment17](../reviews/17_FIXED_P4_PHYSICAL_TUPLE_ASSESSMENT_20261026.md)
records acceptance and limits; the [work record](../numerics/A03_AN02_ANALYTICAL_WORK_RECORD_20261026.json)
binds final evidence. Read the [result index](../../../../../result-summaries/README.md),
[heat-flow11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../../avoid/README.md), especially
[classification01](../../../../../avoid/01_restating_the_target.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[signed payments12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status19](../../../../../avoid/19_status_files_that_lag_the_findings.md).
This is a quantitative approximation theorem, not an RH criterion.

## 1. The theorem and its unchanged inputs

Fix ell,h,eta>0. There exist finite C,X0, depending on these data and
the named compact source/sector bounds, such that all statements below
hold for 63<=t<=65, X=|x|>=X0 and physical |y|<=1. Use the complete
averaging support, collars and rectangles r=ell+2, b=1+h+2, with
one further analytic unit. No numerical value of X0 is asserted.
Let Lambda=1+logX, e=X^-7 and A=|S(t,s)|+|S(t,1-s)|.
Keep exactly

\[
H_t=-H_{zz},\quad H(0,z)=\xi((1+iz)/2)/8,\quad
P=P_4=\sum_{w=s,1-s}S(t,w)T(t,w),\quad T=1+C_2+C_4,
\quad s=(1+iz)/2.
\tag{PT1}
\]

The full canonical theta source, Note19's fixed coefficient order J=2,
chosen implicit gamma saddle and determinant branch are unchanged.
The physical regulator is exactly q=epsilon_g² of parent Note20;
the fixed spatial filter is K=k_ell k_h, with no time average or mass
normalization. Write varrho=logq to distinguish it from the chart radius.
For F=H,P define actual quantities

\[
D_F=|F|²+q,\ S_F=\log D_F,\ w_F=q/D_F,\ \chi_F=w_F(1-w_F),
\quad \rho_F=\frac{q|F_z|²}{\pi D_F²},\quad
j_F=\frac{qF_{zz}\overline{F_z}}{\pi D_F²},
\]
\[
U_F=K*S_F,\ W_F=K*w_F,\ R_F=K*\rho_F,\ J_F=K*j_F,
\quad Q_F=K*(S_{F,x}²-S_{F,y}²)-(U_{F,x}²-U_{F,y}²),
\]
\[
C_F=\Delta S_F/(4\pi)-\rho_F,\quad
b_{reg}=\varrho_t+(\varrho_{xx}+\varrho_x²)/2,
\quad \mathcal S_F=(1-2w_F)(\varrho_t\rho_F+
                     \nabla\varrho\cdot(\Re j_F,\Im j_F)).
\tag{PT2}
\]

Here C_F is the actual regulator curvature C_reg for a holomorphic F.
Write delta for H minus P in any observable. Every spatial derivative
below is a real multi-index, at fixed physical time and coordinates.

| Outputs | Spatial orders | Absolute bound |
| --- | --- | --- |
| delta U, delta W | <=4 | C e |
| delta R, K*delta C | <=2 | C e |
| delta J, delta Q (including Delta delta Q) | <=2 | C e Lambda² |
| delta J used internally for source balance | <=3 | C e Lambda² |
| delta U_t, delta W_t, delta R_t, K*delta C_t, K*(b_reg delta w), K*delta mathcal S | <=2 | C e X Lambda² |
| 2Re K*Z0 | <=4 | C e |
| K*D_E | <=2 | C e |

Z0 and D_E are the actual retained model residual corrections in PT9
and PT21 below. The last two rows pay the heat-potential correction,
its Laplacian through order two, and the density/current balance
correction. All compatibility and field-join corrections listed in
Section7 vanish identically for this unjoined holomorphic model.

The actual compact input is [Ansatz Note20](20_COMPACT_POSITIVE_FIELD_BRIDGE_20261026.md)
RB5, not t=64 inserted into an eventual onset:

\[
|\partial_z^j(H-P)|\le C A e\Lambda^j\ (0\le j\le3),\quad
|(H-P)_t|\le C A e\Lambda²,\quad |E|\le C A e,
\]
\[
E=P_t+P_{zz}=-\sum_{w=s,1-s}S(t,w)\mathscr Q C_4(t,w).
\tag{PT3}
\]

The exact operator mathscr Q and finite residual identity are Note19
FO23/FO30. All ordinary arithmetic, middle, connectors and infinite ends
were paid before the compact field bound. The proof retains PT3's
separate field, direct-time and residual inputs. No propagation from a
small residual, assumed initial zero reality or fitted data is used.

## 2. Acquire corrected phases, every collar and analytic unit

Work first near positive real height. Put a_pm(t,z)=S(t,(1±iz)/2)
T(t,(1±iz)/2). Note19's finite FO8 formula, on the actual compact
interval, gives

\[
C_2=O(X^{-3}),\ C_4=O(X^{-5}),\quad
T_w=O(X^{-4}),\ T_{ww}=O(X^{-5}).
\tag{PT4}
\]

Indeed each monomial is a fixed power of t/B times products of
alpha^(j)(p)=O(X^-j), p_w=B^-1=O(1); differentiating once raises
the inverse-height order by one. The sectorial derivatives through
the finite order needed here are already available in Note19 at J=2.
Thus |T-1|<1/4 after an onset, so both corrected arms are zero-free
on all the larger buffers and conjugate on the real axis.

Choose their coherent logarithms and define holomorphic functions

\[
\mathfrak A=\exp[(\log a_++\log a_-)/2],\quad
\Theta=(\log a_+-\log a_-)/(2i),\quad P=2\mathfrak A\cos\Theta.
\tag{PT5}
\]

Mathfrak A is positive and Theta real on the real axis. Using
(log S)_w=alpha(p)+t alpha''(p)/(4B²), PT4 and the compact saddle
expansion from Notes20/22 gives, on the full buffers,

\[
\Theta_z=\tfrac14\log(X/(4\pi))+O(\Lambda/X),\quad
\Theta_{zz}=O(X^{-1}),\quad
\mathfrak A_z/\mathfrak A=O(1),\qquad \omega=\Theta_x\asymp\Lambda.
\tag{PT6}
\]

For example with D4(w)=(log S)_w+T_w/T,
Theta_z=[D4(s)+D4(1-s)]/4; the sum gives log-height growth while
the difference defining the amplitude derivative is bounded. These
are derivatives of exact holomorphic arms. The classical analytic inputs
are [Cauchy1.9.31](https://dlmf.nist.gov/1.9.E31),
[Rouche and maximum modulus](https://dlmf.nist.gov/1.10#iv) and the
[sectorial gamma bounds](https://dlmf.nist.gov/5.11#ii), rechecked in
their primary DLMF statements on 26 October 2026. Re Theta_z>=c Lambda
throughout the fixed rectangle for large X. Since
partial_y ImTheta=ReTheta_z and ImTheta(x)=0, a zero of cosTheta
there must be real. Real phase levels (j+1/2)pi have one simple zero
c_j each and separation comparable to1/omega. Their number intersecting
any fixed horizontal support is O(omega).

Choose nested disjoint phase disks of fixed sufficiently small radii
below half the phase spacing. Their physical radii are comparable to
1/omega and fit inside the reserved analytic unit, including every
disk meeting the filter support. On their complement,
|cosTheta|>=c cosh(ImTheta). Since the corrected carrier sum is
|a_+|+|a_-|=2|mathfrak A|cosh(ImTheta), this is a full transverse
carrier-sum floor, not a real-axis amplitude bound. Corrected and
uncorrected saddle envelopes are comparable by PT4.

Rouche on the large disks and PT3 exclude any additional H zeros in
the complement and give exactly one H zero a_j per P disk. Real type
forces that zero to be real. On the smaller radius C e/omega circle,
the model slope dominates PT3, giving

\[
|a_j-c_j|\le Ce/\omega,\quad
|F_z(\text{its root})|\ge c\mathfrak A(t,c_j)\omega,
\quad F=H,P.
\tag{PT7}
\]

These conclusions acquire the P4 collars anew; they are not imported
from the leading saddle's zero set. On nested scaled disks
u=omega_c(z-c_j), normalized by A_c=mathfrak A(t,c_j), write
P/A_c=u B(u), H/A_c=(u-e0)C(u), |e0|<=Ce. On the larger boundary

    C-B=(H-P)/[A_c(u-e0)]+e0(P/A_c)/[u(u-e0)]=O(e).

Both units extend holomorphically through their respective roots.
The maximum principle gives |C-B|<=Ce throughout the disk; the
explicit cosine and compact bounds keep B and C above and below fixed
positive moduli. Hence log(C/B)=O(e) with the needed smaller-disk
derivatives from Cauchy.

At each real root set v_F=F_zz/F_z. For P,
v_P=2 mathfrak A_z/mathfrak A+Theta_zz/Theta_z=O(1).
PT3's jets0--3, PT7 and displacement along the collar give
|v_H-v_P|<=Ce omega, hence both residues are bounded. On larger
collars the exact pole decompositions are

\[
F_{zz}/F=v_F/(z-\text{root}_F)+g_F(z),\quad
|g_F|\le C\omega²,\quad |g_H-g_P|\le Ce\omega².
\tag{PT8}
\]

On the boundary the relative floor and jet bounds prove the difference
bound. Subtract the two explicit poles, whose boundary difference has
the same bound, then apply the maximum principle to the analytic
remainder. This proves PT8 inside. Actual local root tracks, when
needed, obey a_t=v_H and c_t=v_P-E(t,c)/P_z(t,c); their difference
is O(e omega+e/omega). Algebraic residues have not been confused with
model velocities. No population cutoff or collar indicator is differentiated.

## 3. Prove the weak primitive and pole bounds for every positive q

Define smooth quantities, including their values at zeros, by

\[
V_{m,F}=w_F^m F_{zz}\overline F/D_F,
\qquad Z_m=w_P^m E\overline P/D_P,\qquad m=0,1,2.
\tag{PT9}
\]

All L1 norms in this note use planar area on a full fixed support
buffer. We prove

\[
\boxed{\|\delta S\|_1+\|\delta w\|_1\le Ce,\quad
\|\delta V_m\|_1\le Ce\Lambda²,\quad \|Z_m\|_1\le Ce.}
\tag{PT10}
\]

The scalar argument holds for arbitrary positive spatial Q(u)=q/A_c²,
held fixed pointwise while changing the field. For scalar f,g, away
from their removable zero sets,

    |log[(|f|²+Q)/(|g|²+Q)]|<=2|log|f/g||,
    |Q/(|f|²+Q)-Q/(|g|²+Q)|<=|log|f/g||/2.

Use the units above and integrate the translation of log|u| along
the root segment. Its gradient is1/|u|, uniformly integrable on the
fixed disk, so the scaled log/weight integral costs Ce, not e log e.
Restore physical area, sum O(omega) disks and use the relative floor
on the complement to obtain the first bound in PT10. The common
physical log|A_c|² cancels only in the difference; no potential
renormalization is performed. Polynomial weights in w, in particular
chi=w(1-w), inherit the same Ce comparison.

For the poles put

    Pi_m[f]=(u-a)^(-1)[Q/(|f|²+Q)]^m |f|²/(|f|²+Q).

Remove disks of radius C e around both roots. Their pole integrals
are O(e). On the complement interpolate
f_s=(u-se0)B exp[s log(C/B)]. The bounded scalar weight and its
derivative with respect to log|f_s| give
|partial_s Pi_m|<=Ce(|u-se0|^-2+|u-se0|^-1). Thus

    integral |Pi_m[(u-e0)C]-Pi_m[uB]| <=Ce(1+|log e|).

No derivative or lower bound of Q enters. Physical area and the pole
factor give per-collar translation Ce(1+|log e|)/omega. Summing collars
costs Ce(1+|log e|)=O(e Lambda), since e=X^-7. Residue differences
cost Ce omega globally; PT8's regular parts and the changed scalar
weights cost at most Ce omega². The exterior is pointwise
O(e omega²). This proves the second PT10 bound with the requested
Lambda², including its logarithmic payment explicitly.

For the residual, E/P has residue E(t,c)/P_z(t,c)=O(e/omega).
On collar boundaries |E/P|<=Ce from the separate PT3 residual and
floor. Subtract the pole and apply the maximum principle: its regular
part is O(e). Multiplication by w^m(1-w) removes the singularity in
the smooth Z_m circuit. The pole costs O(e/omega²) per physical
disk and the regular part the same; sum O(omega) disks and the
O(e) exterior to prove ||Z_m||_1<=Ce. No E_z, E_t or inverse
regulator estimate is needed in this weak bound.

## 4. Pay the exact flat regulator before multiplying the weak bounds

On [63,65] the original regulator can be written exactly

\[
\varrho(t,u)=a(t)-\beta(t)u²,\quad a=2\log E_0,\quad
\beta=0\ (t\le64),\quad \beta=\chi_{reg}/\kappa\ (t>64).
\tag{PT11}
\]

The source saddle M0,kappa and E0 are those of parent Notes19--20,
not the gamma factor M or its complex saddle. Both a and beta are
smooth with bounded required derivatives on this compact interval.
For delta=t-64>0, Note22's exact flat-switch calculation gives
log beta=-64/delta+f(delta), with f smooth at0. Direct differentiation
therefore proves

    |beta'|<=C beta[1+log_+²(1/beta)]   (beta>0),
    beta'=0 when beta=0.

Choose a fixed sufficiently large B0, for example B0=pi after
increasing the height onset. In the regime beta X<=B0, monotonicity
of v(1+log²(1/v)) for small positive v yields, on the full buffer,

\[
|\nabla\varrho|+|\Delta\varrho|\le C,\quad
|\varrho_t|+|b_{reg}|\le C X\Lambda²,\quad
|\nabla\varrho_t|\le C\Lambda²,\quad
|\Delta\varrho_t|\le C\Lambda²/X.
\tag{PT12}
\]

The exact derivatives are varrho_x=-2beta u,
varrho_xx=-2beta, varrho_t=a'-beta'u²,
varrho_xt=-2beta'u, varrho_xxt=-2beta'. Retain, as applicable to
the actual time circuits, q_t=q varrho_t, q_x=q varrho_x,
q_xx=q(varrho_xx+varrho_x²) and
q_xt=q(varrho_xt+varrho_x varrho_t). Terms below64 have beta=0
and bounded a derivatives; they are included, without a limiting shortcut.

In the regime beta X>B0, compact arm asymptotics and PT4 imply
log|a_+(t,u)|=-pi u/8+O(Lambda²), uniformly for bounded |u-X|.
Since (X-r-1)²>=X²/2 eventually,

\[
\lambda_q:=\frac{\sup_{|u-X|\le r+1}\epsilon_g(t,u)}
                    {\mathfrak A(t,X)}\le Ce^{-cX},\qquad
|\log\lambda_q|\le C(1+X²).
\tag{PT13}
\]

Indeed loglambda_q<=-beta X²/4+pi X/8+C Lambda², and B0=pi
leaves a strictly negative linear term. All varrho derivatives and
the finite products used below grow at most polynomially in X.

On each collar the unit floor gives
w_F<=a_q²/(|z-root|²+a_q²), a_q=C lambda_q/omega;
outside, w_F<=C lambda_q². Radial integration and bounded residues
give

\[
\int w_F\le C\lambda_q²[1+(1+|\log\lambda_q|)/\omega],
\]
\[
\int|w_F F_{zz}/F|\le C\{\omega²\lambda_q²
               [1+(1+|\log\lambda_q|)/\omega]+\lambda_q\}.
\tag{PT14}
\]

For w_P E/P replace omega² by e in the regular part and the pole
coefficient by e/omega. Thus every fixed polynomial coefficient
times w, V1,V2 or Z1,Z2 is exponentially paid. V0 and
Z0 are not declared exponentially small: their PT10 comparison or
residual bound is used where their coefficients are constant.
Increase X0 so all required fixed polynomial times exp(-cX) are
below e. No global lower floor of q is introduced.

## 5. Static, direct-time and curvature rows

Let ||psi||_(k) be the sum of test sup norms through order k. The
exact weak identity for a holomorphic F is

\[
4\pi\langle\rho_F,\psi\rangle
=\int S_F\Delta\psi+2\int w_F\nabla\varrho\cdot\nabla\psi
 +\int[w_F\Delta\varrho+\chi_F|\nabla\varrho|²]\psi.
\tag{PT15}
\]

Subtract before taking absolute values. PT10 and PT12 give
|<delta rho,psi>|<=Ce||psi||_(2). In the resolved regime the
S difference is still Ce, while each coefficient-weighted w/chi
term is separately paid by PT14. Hence the same bound holds there.
Using psi=partial^gamma K, |gamma|<=2, proves the static R row.
The static U,W rows follow directly from their L1 differences and
bounded weak kernel derivatives through four.

For any F with F_t=-F_zz+E_F, direct differentiation gives

\[
S_{F,t}=-2\Re V_{0,F}+\varrho_t w_F+2\Re Z_{0,F},
\]
\[
w_{F,t}=\varrho_t\chi_F+2\Re V_{1,F}-2\Re Z_{1,F},
\]
\[
\chi_{F,t}=\varrho_t\chi_F(1-2w_F)
  +2\Re(V_{1,F}-2V_{2,F})-2\Re(Z_{1,F}-2Z_{2,F}).
\tag{PT16}
\]

Here Z_m,H=0 and Z_m,P=Z_m of PT9. These identities use the actual
field equations; they are not obtained by differentiating PT10.
PT10/PT12, or the individual weighted bounds PT14, prove

\[
\|\delta S_t\|_1+\|\delta w_t\|_1+
       \|\delta\chi_t\|_1\le C\tau_X,\qquad
\tau_X=e X\Lambda².
\tag{PT17}
\]

For example varrho_t delta w costs exactly Ce X Lambda² in
the unresolved regime. In the resolved regime varrho_t w and all
weighted V1/Z1 terms are polynomial times exponentially small;
the unweighted delta V0 and Z0 remain O(e Lambda²) and O(e).
Convolution proves the requested U_t,W_t orders<=2. PT17 also pays
their spatial derivatives internally through four if needed, by
moving derivatives to K; no extra time derivative is taken.

Differentiate PT15 at fixed physical coordinates and fixed test:

\[
\begin{split}
4\pi\langle\rho_{F,t},\psi\rangle={}&\int S_{F,t}\Delta\psi
 +2\int(w_{F,t}\nabla\varrho+w_F\nabla\varrho_t)\cdot\nabla\psi\\
 &+\int[w_{F,t}\Delta\varrho+w_F\Delta\varrho_t
 +\chi_{F,t}|\nabla\varrho|²
 +2\chi_F\nabla\varrho\cdot\nabla\varrho_t]\psi.
\end{split}
\tag{PT18}
\]

At each finite point q>0 makes this an ordinary differentiation of
smooth circuits on compact support. Uniformity is then supplied by
PT12/PT14/PT17. Every subtracted term is <=C tau_X||psi||_(2).
This is a direct density-time proof, independent of current balance.
With |gamma|<=2, the total kernel order is <=4, proving R_t.

For curvature, directly subtract PT15 from <Delta S,psi>:

    4pi<C_F,psi>=-2int w_F gradvarrho dot gradpsi
                 -int[w_F Deltavarrho+chi_F|gradvarrho|²]psi.

Its direct time derivative has the last two lines of PT18 with the
minus sign and without the S_t term. It proves static Ce and time
C tau_X curvature comparisons through spatial order two, using at
most three kernel derivatives. In particular both C_t and square C
remain in the final equation. Lastly b_reg delta w, with the same
two-regime payments, proves its requested C tau_X filtered row.

## 6. Current, full covariance and actual signed source

The exact current identity, proved by differentiating the smooth
fraction F_zz conjugate(F)/D_F even across zeros, is

\[
\pi j_F=\partial_{\bar z}V_{0,F}
                      +(\partial_{\bar z}\varrho)V_{1,F}.
\tag{PT19}
\]

In a test pairing the first derivative transfers to psi. PT10/PT12
or PT14 therefore give a weak order-one current difference
Ce Lambda²||psi||_(1). Consequently partial^gamma delta J has
that rate for all |gamma|<=3; internal order3 costs K order4.
No division by F_z between roots occurs.

For G_F=S_{F,x}²-S_{F,y}² retain the exact signed spatial identity

\[
G_F=4\Re V_{0,F}-\square S_F
                        +(\varrho_{xx}+\varrho_x²)w_F,
\quad \square=\partial_x²-\partial_y².
\tag{PT20}
\]

It follows from square|F|²=4Re(F_zz conjugate F) and
square logD+S_x²-S_y²=(square D)/D. Subtract PT20 before bounding:
PT10 and the regulator split prove partial^gamma K*delta G
=O(e Lambda²) through |gamma|<=2, using K through order4.
Separately bounding the two positive gradient squares is not used.

To pay the actual mean products, write
grad S_F=(2Re L_F,-2Im L_F)+w_F gradvarrho,
L_F=(1-w_F)F_z/F. Exterior floors give |F_z/F|<=C omega;
on collars F_z/F=1/(z-root)+O(omega). The simple poles have
uniformly integrable planar mass, with O(omega) disks of radius
O(1/omega); their sum is O(1). The exterior and analytic units cost
O(omega). The regulator term is bounded by PT12 or PT14. Thus
||grad S_F||_1<=C Lambda and |partial^nu U_F|<=C Lambda for
1<=|nu|<=3. Static mean differences are Ce. The full Leibniz sum
therefore gives partial^gamma delta(U_x²-U_y²)=O(e Lambda),
|gamma|<=2. Subtract these actual full means from K*G to obtain
delta Q=O(e Lambda²), including both second derivatives and Delta Q.
The physical additive potential is retained; covariance is not defined
from an equation or replaced by component means.

For P let its actual residual density correction be

\[
\mathcal D_E=\frac{2q\Re(E_z\overline{P_z})}{\pi D_P²}
                   -4\rho_P\Re Z_0.
\tag{PT21}
\]

Vary PT15 in direction E at fixed q. Since deltaS=2ReZ0,
deltaw=-2ReZ1 and deltachi=-2Re(Z1-2Z2), this proves exactly

\[
\begin{split}
4\pi\langle\mathcal D_E,\psi\rangle={}&2\Re\int Z_0\Delta\psi
 -4\Re\int Z_1\nabla\varrho\cdot\nabla\psi\\
 &-2\Re\int[Z_1\Delta\varrho
                  +(Z_1-2Z_2)|\nabla\varrho|²]\psi.
\end{split}
\tag{PT22}
\]

PT10/PT12 or PT14 gives |<D_E,psi>|<=Ce||psi||_(2). The raw
E_z term in PT21 is paid by this equivalent signed weak expression,
not deleted. Thus K*D_E through order2 and 2Re K*Z0 through order4
have the requested Ce bounds.

Finally direct differentiation of the actual density/current circuits
gives rho_F,t+div j_F=mathcal S_F+D_EF, with D_EH=0. Therefore

    K*delta mathcal S=delta R_t+div delta J+K*D_E.

PT18 is already proved independently. With internal current order3
and PT22, spatial orders<=2 of this actual signed source difference
are C tau_X. No integral of the source's absolute raw integrand and
no product of filtered means is substituted for the signed source.

## 7. Full inventory, equations and maximum kernel order

For this single model the compatibility field partial_bar P vanishes.
Thus the general GS8/GS12 quantities T_C,(T_C)_t,T_J,Xi,D_B are
identically zero, as are their requested spatial derivatives.
C_tot=C_reg, whereas E=E4 is retained and generally nonzero:
T_U=2ReZ0 and D_E are exactly the quantities paid above.
Spatial, moving and temporal field-join addends vanish because there
is no field join, time splice or moving filter in this packet.

The model equations, with actual Q and the unchanged q/K, are

\[
U_t=-\tfrac12(\square U+U_x²-U_y²+Q)
                +K*(b_{reg}w)+2\Re K*Z_0,\quad
\Delta U=4\pi(R+K*C),
\]
\[
\begin{split}
R_t={}&-\tfrac12\square R-\tfrac1{8\pi}\Delta(U_x²-U_y²+Q)
 +\tfrac1{4\pi}\Delta K*(b_{reg}w)\\
 &-K*C_t-\tfrac12\square K*C+\tfrac1{2\pi}\Delta\Re K*Z_0,
\end{split}
\]
\[
R_t+\operatorname{div}J=K*\mathcal S+K*\mathcal D_E.
\tag{PT23}
\]

H has the same equations with residual corrections zero. Every
component used in these displayed equations and in Note59's fixed
full-tuple inventory is now paid at the stated orders. The internal
V0 and c_r w rows through spatial order two follow directly from PT10
and PT12/PT14, where c_r=varrho_xx+varrho_x². Fixed-time and fixed
observation-boundary traces inherit the displayed uniform filtered
bounds; no moving-boundary transport theorem is asserted. The density
equation is asserted at its displayed scalar order; differentiating
the whole equation twice would demand extra covariance derivatives
not requested here. The separately proved R_t row through order2
uses PT18 instead and does not incur those extra derivatives.

| Consumer | Largest test differentiation | Largest filtered order | Maximum kernel order |
| --- | --- | --- | --- |
| U,W; heat-potential correction | 0 | 4 | 4 |
| R, direct R_t, residual D_E | 2 | 2 | 4 |
| C,C_t from their own weak identities | 1 | 2 | 3 |
| J, including source's internal current | 1 | 3 | 4 |
| signed covariance stress | 2 | 2 | 4 |
| actual mean products | gradients transferred once, then derivatives | 3 on U | 3 |

The fixed k(v)=(315/256)(1-v²)^4 on |v|<=1 is C3 with a bounded
piecewise-polynomial weak fourth derivative and no boundary delta
through order4. Products and scalings give the required K bounds.
Pairings with its weak derivatives follow by smoothing or weak
integration by parts. No fifth kernel derivative is used.
Apply the exact identities to the whole translated test before
splitting estimates into collars/exterior and regulator regimes.
The splits are inequalities, not differentiated test partitions;
there are no omitted collar-boundary, moving or temporal commutators.

## 8. Onset, limits, screening and disposition

Choose X0 after fixing ell,h,eta. Impose the compact Notes19--20
branch/field gates, PT4 near-one gates, ReTheta_z>=c Lambda,
the nested-collar and Rouche smallness conditions, e omega<1,
B0/X<=1/2 (the monotonicity bound is used only where beta X<=B0),
and the finite list
of polynomial exp(-cX)<=X^-7 absorptions used above. All are eventual
inequalities with fixed constants and therefore give a finite
sufficient onset. The theorem claims no numeric height or useful
cost at that height. Negative real charts follow by evenness and
the even physical regulator.

The physical rates improve the inherited parent Note31 PE44 main
comparison rows by five height powers at this fixed compact scope,
and its X^-3 residual corrections by four. The full exact-q tuple,
actual covariance, both curvature derivatives and all nonzero model
defects remain. No estimate in the frozen requested rows is unpaid.
This neither sharpens Note28's simplified-layer O(1) absolute/
O(1/logX) normalized law nor reassembles the all-time construction.
Notes58--61 retain their separate source/evaluator/weak-filter
height-cost obligations; a regulator-floor-free approximation proof
is not a finite-node filter algorithm or a useful height-cost theorem.
The bounded-height compact core and intermediate positive-time band
are not covered by this high-height result.

The source-specific input is the complete canonical xi/gamma/ordinary-
arithmetic comparison PT3. Euler-factor and finite-prime perturbations
lack the unchanged full coefficients; weighted-square, finite-cutoff
and atomic controls lack the full canonical completion; reflected,
smooth and positive-primitive controls lack the same complete source
and arithmetic identity. The weak pole and physical transfer lemmas
are generic and may apply to simple collars of controls too. They
are not claimed to reject every derived control bound or prove global
noncollision/RH. This is the premise screen required by Control12.

**Disposition — Analysis, Sol:** HDA-A03-AN02 r1 Complete/CLOSED at
its fixed-P4 [63,65] high-height physical scope, with uninstantiated
finite constants/onset and same-model internal assessment only.
HDA-A03 remains Partial for the wider physical-layer program;
LT-06 now has this completed bounded consumer, with wider switch/core
and sharper-layer obligations distinguished. Parent HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled remain unchanged. No manuscript
build or independent inherited-chain audit is claimed by this note.

**Next deliverable — Analysis, Sol:** existing
[HDA-A08-AN01 r1](../research-progress/handoffs/HDA-A08-AN01.md), the
first small-positive slab [1/2,1], to improve the regional coverage
map. Prove its full buffered canonical field/jet/direct-time/residual
comparison or record its first precise failed estimate. Integration
of this new physical theorem into the technical companion/Book is a
separate production follow-through, not a new mathematical claim.
