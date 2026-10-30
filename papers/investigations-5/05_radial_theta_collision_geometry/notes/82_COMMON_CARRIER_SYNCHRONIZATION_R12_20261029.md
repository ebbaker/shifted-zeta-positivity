# Common-carrier synchronization with complete H1 decay costs

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
ultra**, Investigation05 **chat0033**, *Investigate radial theta collision
geometry*. Parent research synthesis with same-model contributing
derivations and checks; no independent specialist review.

**Status: proved in-note under the accepted prepared-solution, common-kernel
and R10 uniform-feedback inputs; fixed E08 assessment pending.** At the
unchanged mark (T,A)=(1/4,2), each of J0,J1,J2 approaches its conserved-mass
multiple of the existing **time-dependent** positive carrier in H1. The
squared H1 errors have an explicit exp(-B/2) allowance valid from time
zero. All moment, Gaussian, derivative and transient costs are paid.
[Note83][n83] uses these errors in the genuine residual and the selected
signed production I1, obtaining its finite accumulated correction.

This is a quantitative correlation result beyond [R11][n76]'s boundedness.
The equally informed direct method supplies the proof. It does not reduce
dependence on the physical mass margin, establish stationary carrier
convergence, determine the remaining carrier production's sign or enlarge
the physical domain. [Progress05][progress] records the R12 consumer before
analysis. The [result index][results] and [pattern index][avoid], especially
[controls][controls], [scope][a07] and [quantitative utility][a20], govern
these distinctions. Under [avoid/01][a01], this is a paid supporting decay
estimate on an already covered physical mark, not a new noncollision
criterion.

## 1. Fixed source, path and zero-mass errors

Keep precisely the complete theta source, unit Gaussian preparation and
common fixed-mark propagator of [Notes28][n28]–[29][n29]. Put
\[
 q(u)=e^{u^2/4}\Phi(u),\quad
 \rho(X)=\mathbf1_{r\ge1}\frac{q(u)}{8\pi r^3},\quad
 r=|X|,\quad u=\tfrac12\log r,
\]
\[
 M_j=\int_0^\infty u^jq(u)\,du,\qquad M=M_0+M_2>0.
\]
All these moments are finite by the complete theta tail. Define
\[
 h^{\rm raw}=\rho(1+u^2),\quad h_0=K_1*h^{\rm raw},\quad
 h(s)=P_{s,0}h_0,
\]
\[
 F_j^{\rm raw}=\rho u^j\cos^{(j)}(2u),\qquad
 J_j(s)=P_{s,0}K_1*F_j^{\rm raw},\quad j=0,1,2.                 \tag{1}
\]
Here J0=U and J1=V; J2 is the actual second common-path frequency jet.
Multiplication by u occurs before preparation. Every spatial integral is
over R³, including the evolved inner ball.

The shared scalar equation is
\[
 \partial_sf=\Delta f+\alpha(s)\operatorname{div}(vf),\qquad
 v=X+\frac{X}{1+|X|^2},\qquad B(s)=\int_0^s\alpha(t)\,dt.
\]
Its inherited drift bounds are
\[
 \kappa I\le Dv\le2I,\qquad \kappa=\tfrac78,\qquad
 3\le d=\operatorname{div}v\le6.                              \tag{2}
\]
[Note67][n67] and its assessment supply the global solution and
\[
 a_*:=\frac15\left(\frac{6\pi^2E_0}{M^2}\right)^{2/3}>0,
 \qquad a_*\le\alpha(s)\le\bar\alpha:=\frac{2K}{3}<\infty,
 \quad K=K_\infty\ \text{or}\ K_\theta.                         \tag{3}
\]
E0=||W(s)||2² is the conserved spatial field energy. The positive physical
mass margin used to acquire K remains an upstream premise; it is not
obtained from the errors below. In particular B(s)>=a_*s tends to infinity.

Let m_j=int J_j=int F_jraw be the conserved scalar masses, and set
\[
 a_j=\frac{m_j}{M},\qquad e_j(s)=J_j(s)-a_jh(s),\quad j=0,1,2.
                                                                    \tag{4}
\]
Only the positive carrier mass M is in a denominator. No m_j is divided
by or assumed nonzero. These are fixed scalar coefficients, with no
physical-frequency differentiation of h, a_j or alpha. Each error solves
the same scalar equation and has exactly zero mass.

All fields in (1) and (4) are radial. The spatial square in [Note42][n42]
therefore gives, for each scalar error or carrier and its current energy,
\[
 \mathcal K(f)=10\|\nabla f\|_2^2+\nu\|f\|_2^2
                 -\mathscr H_{\rm rad}(f),\qquad
 \nu=\frac{21}{4},\quad \mathscr H_{\rm rad}(f)\ge0.            \tag{5}
\]
This identity requires radiality and the inherited smooth decay. It does
not require that f determine alpha through a separate feedback equation.

## 2. Initial moments and the full preparation cost

Set (b0,b1,b2)=(1,1/2,1). The inequalities
1<=1+u², u<=(1+u²)/2, and u²<=1+u² imply
|F_jraw|<=b_j hraw. Since |m_j|<=M_j, positivity of K1 gives
\[
 \|e_j(0)\|_1\le\ell_j:=2M_j,\qquad
 |e_j(0)|\le\left(b_j+\frac{M_j}{M}\right)h_0.                 \tag{6}
\]
The existing carrier second moment is
\[
 R_0=\int|X|^2h_0(X)\,dX
 =\int_0^\infty e^{4u}(1+u^2)q(u)\,du+6M.                     \tag{7}
\]
The +6M is the complete second-moment cost of unit Gaussian preparation.
It is retained in every use of R0. Weighted Cauchy–Schwarz now pays the
first moment of the error without another source integral:
\[
 \boxed{\int|X||e_j(0,X)|\,dX\le P_j,
 \qquad P_j^2:=\ell_j\left(b_j+\frac{M_j}{M}\right)R_0.}        \tag{8}
\]
Indeed the squared first absolute moment is at most the product of its
L1 norm and its second absolute moment; (6) bounds both factors.

If desired, replace M1 throughout these upper budgets by sqrt(M0M2).
Cauchy–Schwarz proves M1<=sqrt(M0M2), so only the already paid M0,M2,M,R0
are needed. More generally any upper budget M_j^+>=M_j may replace M_j
in ell_j and P_j. The signed masses in (4) remain their actual values.

Let
\[
 c_G=(8\pi)^{-3/2}=\|K_1\|_2^2,\qquad
 E_j=\|e_j\|_2^2,\quad G_j=\|\nabla e_j\|_2^2,\quad
 N_j=\|\Delta e_j\|_2^2.
\]
Gaussian Young estimates, applied to the raw error's L1 bound, give
\[
 E_j(0)\le c_G\ell_j^2,
 \qquad G_j(0)\le\frac34c_G\ell_j^2.                           \tag{9}
\]
The gradient factor is exact: ||grad K1||2²=3c_G/4. No smallness of the
initial errors has been assumed.

## 3. A paid intermediate gradient bound

Use the sufficient Nash constant and scalar barriers
\[
 c_N=\frac35(6\pi^2)^{2/3},\qquad
 D=\max\{c_G,(3\bar\alpha/c_N)^{3/2}\},
\]
\[
 r_{\rm u}=\frac{5\bar\alpha+
                \sqrt{25\bar\alpha^2+2\nu\bar\alpha}}2,
 \qquad H=D\max\{3/4,r_{\rm u}\},\qquad
 \overline G_j=\ell_j^2H.                                    \tag{10}
\]
L1 contractivity of the positive conservative propagator gives
||e_j(s)||1<=ell_j. The elementary Fourier/Nash inequality proved in
[Note76][n76] gives
\[
 G_j\ge c_NE_j^{5/3}\ell_j^{-4/3},\qquad
 E_j'\le-2c_NE_j^{5/3}\ell_j^{-4/3}+6\bar\alpha E_j.
\]
The initial bound (9) and scalar comparison imply E_j<=ell_j²D.
Retaining the full radial identity (5),
\[
 G_j'+2N_j+\alpha\mathscr H_{\rm rad}(e_j)
                    =\alpha(10G_j+\nu E_j).                  \tag{11}
\]
Since G_j²<=N_jE_j, it follows that
\[
 G_j'\le-\frac{2G_j^2}{\ell_j^2D}
                    +10\bar\alpha G_j+\nu\bar\alpha\ell_j^2D.
\]
The positive normalized root solves
2r²-10alpha_bar r-nu alpha_bar=0 and is exactly r_u in (10).
Using (9) proves
\[
 \boxed{G_j(s)\le\overline G_j\qquad(s\ge0).}                 \tag{12}
\]
This uses the accepted scalar barrier argument with the sharper radial
coefficient nu=21/4. It is an intermediate input to decay, not another
claimed uniform-L2 milestone. All ell_j and P_j displayed above are
strictly positive for theta, even if a signed mass m_j vanishes.

## 4. Common-path contraction and the full Fourier deficit

Freeze the actual alpha path and drive two diffusion trajectories with
the same Brownian increments:
\[
 dX_s^x=-\alpha(s)v(X_s^x)\,ds+\sqrt2\,d\mathcal B_s.
\]
Subtracting the equations removes the Brownian part. Equation (2) gives
\[
 \frac d{ds}|X_s^x-X_s^y|^2
 \le-2\kappa\alpha(s)|X_s^x-X_s^y|^2,
 \quad |X_s^x-X_s^y|\le e^{-\kappa B(s)}|x-y|.                 \tag{13}
\]
This is the inherited synchronous argument of [Note28][n28], not an
import of a new coupling theorem. The [existing reference annotation][refs]
identifies Eberle's selected introductory passage as classical context.

The backward expectation of exp(-i xi·X) therefore has Lipschitz constant
at most |xi|exp(-kappa B). Subtract its value at spatial origin before
pairing with e_j(0), whose mass is zero. Equation (8) yields
\[
 \boxed{|\widehat e_j(s,\xi)|
                  \le|\xi|P_je^{-\kappa B(s)}.}               \tag{14}
\]
No radial second-cancellation estimate is used, so no non-affine drift
curvature term has been dropped.

Our forward Fourier transform is unnormalized; Parseval has factor
(2pi)^(-3). This is the convention conversion recorded in [reference11][refs]
and [DLMF 1.14.8][dlmf]. Retaining the complete weighted deficit, for R>0,
\[
 G_j\ge R^2E_j-
              \frac{P_j^2e^{-2\kappa B}R^7}{35\pi^2}.          \tag{15}
\]
The exact coefficient follows from
\[
 (2\pi)^{-3}\int_{|\xi|<R}(R^2-|\xi|^2)|\xi|^2\,d\xi
 =\frac1{2\pi^2}\left(\frac{R^7}{5}-\frac{R^7}{7}\right)
 =\frac{R^7}{35\pi^2}.
\]
The exterior deficit is nonpositive. Optimizing (15) at
\(R^5=10\pi^2E_j/(P_j^2e^{-2\kappa B})\) gives
\[
 G_j\ge\frac57(10\pi^2)^{2/5}
              E_j^{7/5}(P_je^{-\kappa B})^{-4/5}.             \tag{16}
\]
For a zero error the consequence below is immediate; no division by its
energy is necessary. Define
\[
 c_F=\left(\frac75\right)^{5/7}(10\pi^2)^{-2/7},\qquad
 L_j=c_F\overline G_j^{5/7}P_j^{4/7}.                          \tag{17}
\]
Equations (12), (16) and 4kappa/7=1/2 prove
\[
 \boxed{E_j(s)\le L_je^{-B(s)/2}\qquad(s\ge0).}                \tag{18}
\]
This holds at zero as well as at late time. The complete initializer and
intermediate gradient costs have paid the transient. No optimal rate or
spectral-gap claim is made.

## 5. Matching gradient decay from time zero

Retain diffusion in (11). The inequality G_j²<=N_jE_j and (18) imply
N_j>=G_j²/(L_j exp(-B/2)). Set z_j=exp(B/2)G_j/L_j. Differentiation gives
\[
 z_j'\le-2z_j^2+\frac{21}{2}\alpha z_j+\nu\alpha
       \le-2z_j^2+\frac{21}{2}\bar\alpha z_j+\nu\bar\alpha.
                                                                    \tag{19}
\]
The extra alpha/2 is exactly the derivative of exp(B/2). The positive
root of 2r²-(21/2)alpha_bar r-nu alpha_bar=0 is
\[
 r_{\rm d}=
 \frac{21\bar\alpha+\sqrt{441\bar\alpha^2+32\nu\bar\alpha}}8
 =\frac{21\bar\alpha+\sqrt{441\bar\alpha^2+168\bar\alpha}}8.
\]
Choose the completely prepared constant
\[
 T_j=\max\left\{\frac34c_G\ell_j^2,\ L_jr_{\rm d}\right\}.
                                                                    \tag{20}
\]
Scalar comparison using (9) proves G_j<=T_j exp(-B/2) for all s>=0.
If G_j(0) is already available, it can replace its Gaussian upper bound
in (20). Thus the complete synchronization result is
\[
 \boxed{
 \left\|J_j(s)-\frac{m_j}{M}h(s)\right\|_{H^1}^2
 \le(L_j+T_j)e^{-B(s)/2}
 \le(L_j+T_j)e^{-a_*s/2},\qquad j=0,1,2,
 }                                                               \tag{21}
\]
where the squared H1 norm means ||f||2²+||grad f||2².
The **squared energy** decays as exp(-B/2); the **norm** decays as
exp(-B/4). There is no delayed entrance time, unpaid early transient or
division by a possibly zero physical jet mass. The carrier in (21)
continues to evolve; it is not asserted to be stationary or convergent.

## 6. Complete error diffusion and accumulated costs

Since B(0)=0 and B(infinity)=infinity, the exact tail payments are
\[
 \int_t^\infty\alpha(s)e^{-B(s)/2}\,ds=2e^{-B(t)/2},\qquad
 \int_t^\infty\alpha(s)e^{-B(s)/4}\,ds=4e^{-B(t)/4}.             \tag{22}
\]
Consequently the alpha-weighted squared errors in (21) are integrable.
A bilinear correction with one error factor and a uniformly bounded
carrier factor is integrable with the second payment in (22). Ordinary
time integrals are also finite using a_*>0.

Integrate the exact radial identity (11), retaining its nonnegative
remainder. Equations (18), (20), and (22) give
\[
 \boxed{\int_0^\infty
       [2N_j+\alpha\mathscr H_{\rm rad}(e_j)]\,ds
       \le G_j(0)+20T_j+2\nu L_j,}
\]
\[
 \int_0^\infty N_j\,ds
       \le\tfrac12G_j(0)+10T_j+\nu L_j.                       \tag{23}
\]
The corresponding tail bound is
\[
 \int_t^\infty N_j\,ds
 \le\left(\frac{21}{2}T_j+\nu L_j\right)e^{-B(t)/2},            \tag{24}
\]
with the sharper first term G_j(t)/2 available before using (20).
No third spatial derivative, higher spectral derivative or unknown
interpolation norm has entered. These are finite dissipation estimates
for the **errors**; they do not assert finite half-line dissipation for
the original nonzero-mass fields.

The same radial scalar proof as Section 3, now for h with mass M and
its Gaussian initializer, gives the carrier budgets
\[
 \|h(s)\|_2^2\le M^2D,
 \qquad\|\nabla h(s)\|_2^2\le M^2H.                           \tag{25}
\]
Neither norm is claimed constant. Equations (21), (22), (25) are the
complete inputs for the signed correction in [Note83][n83]. In particular
\[
 W=(a_0,a_1)h+(e_0,e_1),
\]
\[
 (2V,V+2J_2)=(2a_1,a_1+2a_2)h+(2e_1,e_1+2e_2).                \tag{26}
\]
These are exact decompositions along the actual common path. They do not
set the genuine residual to zero, split singular sphere quotients, or
supply a sign for the carrier production. The full residual-error
production must be integrated with its instantaneous error energy;
the old integrating-factor identity with a constant E0 cannot simply
be reused for a varying error energy.

## 7. Direct comparison, collision controls and stopping scope

The direct comparator receives the same positive carrier, full source
moments, physical mass information, uniform feedback, synchronous
contraction and retained radial diffusion. It obtains every estimate
above. Thus R12 has a new decaying correlation allowance, while an
additional primitive-specific benefit remains unproved. The primitive
representation is available to either side of the comparison.

| Control or class | Exact limitation of the present conclusion |
| --- | --- |
| Gaussian-polynomial and normalized positive-primitive controls | Their admitted compact regular paths share the generic contraction and diffusion arguments. An actual double event has zero vector mass, failing the positive physical floor that supplied the present global K. Primitive positivity or normalization does not repair that dependency. |
| Positive weighted-square sources | They may share the sufficient low-mark payment and these downstream estimates. Their registered events at other frequencies do not contradict (21) at A=2. At a genuine admitted event the positive mass premise fails. |
| Fixed-theta polynomial observation controls | They fail literal cosine in the upstream mass payment; theta's K cannot be imported into their zero-mass path. |
| Finite-prime, reflected, shape and RH-conditional endpoint controls | Retain their registered domains and conditionality. A genuine admitted double event fails the mass premise; no new event location or moment ratio was evaluated. |
| Euler-factor Laguerre witnesses | A negative Laguerre witness is not automatically a double event. No zero-mass conclusion is manufactured from such a witness. |
| Atomic/profile comparisons | The inherited smooth prepared solution hypotheses must first be checked. Admitted prepared or continuous versions still require their actual path bounds. |

A colliding control can have a finite alpha bound on every compact
interval of its regular lifespan. The constants in that application then
depend on the interval; there is no global contradiction. Supplying the
uniform global bound at an actual collision is the unavailable upstream
step. The [registered controls][controls] and [scope rule][a07] are kept
with this distinction.

The scope is exactly j=0,1,2, one fixed mark, the unchanged source,
preparation, feedback and common path. No parameter scan, numerical
acquisition, stationary-profile theorem, mass-only reduction, uniformity
in physical parameters or larger noncollision domain is claimed.
The finite correction in Note83 does not decide its remaining carrier
term. Once that complete comparison is recorded, R12's stopping rule
applies rather than selecting another consumer midstream.

## 8. Evidence and fixed assessment obligations

The mathematical derivation above is self-contained after the named
accepted solution/kernel/feedback and radial-square inputs. No external
nonlinear-feedback or convergence theorem is imported. [Reference11][refs]
retains its existing Hunter/Eberle version and selected-passage records;
[DLMF 1.14.8][dlmf] identifies the classical Fourier normalization. This
note makes no new source audit, literature-priority or optimality claim.

The fixed E08 assessment should check zero mass/common path; every raw
and Gaussian moment payment; both radial barrier roots; synchronous
contraction with kappa=7/8; the 1/(35pi²) Fourier deficit and its optimizer;
the squared-energy versus norm rate; complete diffusion/tail payments;
and the genuine residual/I1 assembly and control dependencies in Note83.
These are internal LLM results with shared inherited premises, pending
that fixed assessment and independent specialist review.

[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: 29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n42]: 42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md
[n67]: 67_UNIFORM_FEEDBACK_DIRECT_COMPARISON_B02_R10_20261029.md
[n76]: 76_UNIFORM_RESIDUAL_AND_FIXED_JET_CLOSURE_R11_20261029.md
[n83]: 83_FINITE_CENTERED_PRODUCTION_CORRECTION_R12_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[refs]: ../references/11_CONSERVATIVE_FEEDBACK_AND_DIFFUSION_CONTRACTION_20261028.md
[dlmf]: https://dlmf.nist.gov/1.14.E8
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
