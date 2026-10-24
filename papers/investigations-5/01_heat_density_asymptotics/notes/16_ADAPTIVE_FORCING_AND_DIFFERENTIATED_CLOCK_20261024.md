# Adaptive forcing, weak current, and a differentiated growing clock

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**Status: estimates proved in-note; exact algebraic controls and floating
evaluations of the stated allowances; same-assistant assessment only.**
This executes the first bounded task in [Note 15][handoff]. It does not
solve a reduced boundary evolution or supply independent review or a
certified finite onset. The regulator is the explicit p=1 prescription
of [Note 14][variable]; the underlying theta field remains unchanged.

Read the [result index][results], particularly [heat geometry][geometry]
and [collision controls][controls], and the [avoid index][avoid], especially
[quantitative milestones][classification], [evidence/status][status-rule]
and [normalizations][normalization]. This is a quantitative approximation
milestone. Its gains are the error bounds below, not a new RH criterion.

## 1. Contract and main gains

Retain H_t=-H_zz, M=H(t,0), f=H/M=E_t cos(uz), mu=E_t u,
v=Var_t u, and the saddle L,kappa of [Note 12][clock]. Fix compact spatial
averaging widths ell,h and a transverse buffer Y>h. The kernel is the
same product K=k_ell k_h, with k(s)=(315/256)(1-s^2)^4 on [-1,1],
zero outside. There is no time filter or moving-width commutator here.
An additional fixed positive time average can average every bound at
the constituent times, provided its whole support satisfies the gates.

Use a buffered carrier rectangle of halfwidth X~kappa^(1/3), with
carrier-maximal vertical walls as in Note 12. All root neighborhoods
touching the kernel support must lie strictly within this rectangle.
Strict gates supply a common time neighborhood for differentiation;
freeze the integer carrier population there. Differentiating the
integer floor used to choose a large rectangle is neither needed nor done.

Take

\[
\epsilon(t,x)=M_0(t)\kappa^{-1}e^{-x^2/(2\kappa)},\quad
M_0=2\pi^2e^{q_t(L)}\sqrt{2\pi/\kappa},\quad
q_t(u)=tu^2+9u-\pi e^{4u}.
\tag{AT1}
\]

The source exponent q_t is unrelated to q=epsilon^2 below. Retain
rho=q|H_z|^2/[pi(|H|^2+q)^2], the complex current
j=qH_zz conjugate(H_z)/[pi(|H|^2+q)^2], and w=q/(|H|^2+q).
Set r=log q. The potential forcing B_epsilon and current source
S_epsilon are exactly VE6 and VE9 of Note 14.

The results, uniform on this buffered growing window, are:

1. Fixed-size phase collars improve the p=1 static regulator allowance
   to O(kappa^-2). This strengthens, rather than invalidates, Note 14's
   O(kappa^-1) sufficient allowance.
2. The averaged potential forcing is O(L^2 kappa^-2). The weak current
   error, differentiated density bias, and averaged current source have
   allowance O(kappa^-5/3+L^2 kappa^-2)=o(L/kappa).
3. With alpha=mu'/mu, every covered real zero has
   a_j'=-alpha a_j+O(kappa^-7/6). The proof differentiates the complete
   source and uses the fourth-moment cancellation; it does not
   differentiate a position error.
4. The actual averaged current and density time derivative differ from
   those of the explicit moving **mu-clock** by O(L kappa^-7/6), which
   is o(L/kappa). This reference retains its finite-lattice phase.

The complete moments mu,mu' still enter that dynamical reference.
This is not an autonomous reduced PDE or a saddle-only dynamical model.
The physical density itself remains unnormalized.

## 2. Complete source bounds through the sixth moment

Extend Note 12's G_p(Y),D_p(Y),A_p(Y) from p<=3 to p<=6 by precisely
the same formulas (3)--(4). Its proof multiplies the complete-source
bound by |w|^p exp(Y|w|/sqrt(kappa)) and works for every fixed
nonnegative integer p. All theta indices, both tails, and normalization
are retained. The inherited finite gates, including Z_->0, remain.

Write e=e_mu, d=mu-L, so |d|<=e. For p>=1 put

\[
\overline B_p(Y)=2^{p-1}e^{Ye}
  \{A_p(Y)+e^p A_0(Y)\},\quad
\overline B_0(Y)=e^{Ye}A_0(Y).
\tag{AT2}
\]

These bound B_p(Y)=E[|u-mu|^p exp(Y|u-mu|)]. In particular
B_p(Y)=O(kappa^-p/2) for fixed p,Y. Set bar-v=A_2(0) and

\[
\nu=\frac{D_2(0)+D_0(0)}{Z_-}+\kappa e^2,
\quad |\kappa v-1|\le\nu=O(\kappa^{-1/4}).
\tag{AT3}
\]

For m_j=E(u-mu)^j, an explicit fourth-cumulant allowance is

\[
\begin{split}
|m_4-3v^2|\le E_4:={}&
\kappa^{-2}\frac{D_4(0)+3D_0(0)}{Z_-}
+4e A_3(0)+6e^2 A_2(0)+3e^4\\
&+3(\bar v+\kappa^{-1})\nu/\kappa
=O(\kappa^{-9/4}).
\end{split}\tag{AT4}
\]

Indeed the signed raw fourth moment about L differs from 3/kappa^2
by the first term, since the Gaussian fourth moment is three times its
mass. The central fourth moment equals
E(u-L)^4-4d E(u-L)^3+6d^2 E(u-L)^2-3d^4.
The remaining comparison of 3v^2 and 3/kappa^2 gives the last term.
No rate is inferred by differentiating a previous O bound.

Complete source differentiation, dP_t/dt=(u^2-Eu^2)P_t, gives

\[
\mu'=2\mu v+m_3,\quad
v'=2\mu m_3+m_4-v^2,\quad
m_3'=2\mu(m_4-3v^2)+m_5-4vm_3.
\tag{AT5}
\]

Consequently, with the bars in AT2 understood,

\[
|\alpha|\le 2v+B_3(0)/\mu,\quad
|v'|\le V_2:=2\mu B_3(0)+B_4(0)+v^2,
\]
\[
|m_3'|\le V_3:=2\mu E_4+B_5(0)+4vB_3(0)
=O(L\kappa^{-9/4}).
\tag{AT6}
\]

Unknown positive moments can everywhere be replaced by the explicit
upper bounds, and mu by L+e in numerators and L-e>0 in denominators.

## 3. Differentiating the carrier on the growing window

Use Note 12's A(z)=1-vz^2/2, a_*, delta, s=4delta and
r_0=s/mu, with the explicit upper moment allowances. Thus
a_*=1-O(kappa^-1/3), delta=O(kappa^-1/2), and each actual root
a_j is real/simple with |a_j-c_j|<=r_0,
c_j=(j+1/2)pi/mu. For real |z|<=X, Taylor expansion in u about mu
and differentiation under the complete integral give

\[
f_z=-\mu A\sin(\mu z)-vz\cos(\mu z)+E_z,
\quad |E_z|\le E_1:=\tfrac12X^2B_3(0)
+\tfrac16X^3\{\mu B_3(0)+B_4(0)\}.
\tag{AT7}
\]

For example the third u derivative of -u sin(uz) is
3z^2 sin(uz)+u z^3 cos(uz), which proves this finite remainder.
Separately, expanding cos(uz) through its cubic term inside
f_t=Cov(u^2,cos(uz)) gives

\[
f_t=-\mu'z\sin(\mu z)-\tfrac12v'z^2\cos(\mu z)
+\tfrac16 C_3z^3\sin(\mu z)+E_t^{(4)},
\]
\[
C_3=2\mu m_4+m_5-vm_3,\qquad
|E_t^{(4)}|\le T_4:=\frac{X^4}{24}
\{2\mu B_5(0)+B_6(0)+vB_4(0)\}.
\tag{AT8}
\]

The decisive cancellation is C_3-3mu'v=m_3'. Combining AT7--AT8,

\[
f_t-\alpha z f_z
=\tfrac16m_3'z^3\sin(\mu z)
+(\alpha v-v'/2)z^2\cos(\mu z)
+E_t^{(4)}-\alpha z E_z.
\tag{AT9}
\]

At a root, |cos(mu a_j)|<=sin s and |sin(mu a_j)|>=cos s.
Require the explicit derivative gate

\[
d_z:=\mu a_*\cos s-vX\sin s-E_1>0.
\tag{AT10}
\]

It holds eventually, with d_z~mu~L. Implicit differentiation now proves

\[
\boxed{|a_j'+\alpha a_j|\le E_v:=
\frac{V_3X^3/6+(|\alpha|v+V_2/2)X^2\sin s
                +T_4+|\alpha|XE_1}{d_z}
=O(\kappa^{-7/6}).}
\tag{AT11}
\]

The four numerator orders after division by d_z are respectively
O(kappa^-5/4), O(kappa^-4/3), O(kappa^-7/6), and
O(kappa^-7/6). Set V=|alpha|X+E_v=O(kappa^-2/3), an upper
bound for every covered root speed. This growing-label result uses
the same complete-source mechanism as [BW10 Note 20][saddle], but
retains cubic covariance terms needed when X grows.

Replacing alpha by 2/kappa is not silently done. The available
|alpha-2/kappa|=O(kappa^-5/4) would yield an X-multiplied velocity
error that is too large for the derivative comparison below on the
entire growing window.

## 4. Wider collars pay the narrow regulator layers

Fix beta=1/4 and strengthen the eventual carrier gate to s<beta/2.
Put R_c=beta/mu. Around each c_j use a collar disk of radius R_c,
while retaining r_0 for the much tighter root-location error. The
collars are disjoint. Require the full disks touching the averaging
support to stay in the comparison rectangle; sufficient buffers are
|x|+ell+2R_c<X and |y|+h+2R_c<Y.

The pointwise transverse cancellation in Note 12 gives outside these
collars and on their boundaries

\[
|f(z)|\ge b e^{\mu|\operatorname{Im}z|},\quad
b=a_*\{e^{-\beta}\sin\beta-\delta\}>0.
\tag{AT12}
\]

Inside a collar its single actual root a_j satisfies
|f(z)|>=c|z-a_j|, c=b/(2R_c), by applying the maximum principle
to the reciprocal of f(z)/(z-a_j). Here b=Theta(1), c=Theta(L),
whereas the small localization disks of Note 14 had b_*=Theta(kappa^-1/2).

Let Omega be the kernel support, with area A_Omega=4ell h. At most
n=2mu(ell+R_c)/pi+2 collars intersect it. The saddle prescription has
epsilon/M<=eta:=C_M/kappa, C_M=sqrt(2pi)/Z_-. Put a_e=eta/c and

\[
W_0=\frac{A_\Omega\eta^2}{b^2}
+n\pi a_e^2\log\{1+(2R_c/a_e)^2\},\quad
\Lambda_0=W_0+n\pi a_e^2.
\tag{AT13}
\]

Then

\[
\int_\Omega w\le W_0,\qquad
\int_\Omega\log(1+q/|H|^2)\le\Lambda_0,
\qquad W_0,\Lambda_0=O(\kappa^{-2}).
\tag{AT14}
\]

For the first bound use w<=eta^2/b^2 outside collars and
w<=a_e^2/(|z-a_j|^2+a_e^2) inside. Integrate over the radius-2R_c
disk about a_j. The logarithmic bound is Note 14's elementary disk
integral. Its disk term is O(kappa^-2 log(kappa)/L); log(kappa)/L
is bounded. No smoothing peak is sampled and no theta root is fitted.

Write h_2=H_zz/H, a meromorphic quotient distinct from the kernel width h.
It has residue a_j' at each covered zero. Set

\[
Q_2=\mu^2 B_0(Y)+2\mu B_1(Y)+B_2(Y),\quad
G=Q_2/b+V/(R_c-r_0).
\tag{AT15}
\]

Outside collars |h_2|<=Q_2/b, because both field bounds contain the
same exp(mu|Im z|). Inside a collar the analytic function
h_2-a_j'/(z-a_j) has boundary modulus at most G and hence the same
bound throughout. Also
integral w/|z-a_j| <=2pi a_e arctan(2R_c/a_e)<=pi^2 a_e.
Therefore

\[
\boxed{\int_\Omega |h_2|w\le I_0:=GW_0+n\pi^2Va_e
=O(L^2\kappa^{-2}+\kappa^{-5/3}).}
\tag{AT16}
\]

This separates the small moving-pole residue from its regular part.
It does not bound H_zz/H uniformly across a zero.

## 5. A distributional current bridge and a differentiated bias

Let nu=sum delta_(a_j) and J_nu=sum a_j' delta_(a_j) on the
covered region. These are respectively the local zero measure and its
complex current; they obey partial_t nu+div J_nu=0. For
partial_bar=(partial_x+i partial_y)/2, the exact identity is

\[
\boxed{j-J_\nu=\frac1\pi\left\{
h_2w(1-w)\partial_{\bar z}r
-\partial_{\bar z}(h_2w)\right\}.}
\tag{AT17}
\]

Away from zeros, differentiate w to obtain
partial_bar w=w(1-w)partial_bar r-qH conjugate(H_z)/(abs(H)^2+q)^2.
At a zero the residue contributes
partial_bar h_2=pi a_j' delta_(a_j), with w(a_j)=1.
The coefficient follows directly by integrating around a small circle:
the boundary integral of 1/(z-a_j) is 2pi i. This proves the
distributional identity; h_2 w is locally integrable. No division by H_z
or exclusion of stationary points between the zeros is needed.

For a real compact C^2 test psi, put
b_1=||grad r||, b_2=||Delta r|| on Omega. Pairing AT17 gives

\[
|\langle j-J_\nu,\psi\rangle|
\le E_J(\psi):=\frac{||\nabla\psi||+b_1||\psi||}{2\pi}I_0,
\tag{AT18}
\]
\[
|\langle\operatorname{div}(j-J_\nu),\psi\rangle|
\le E_D(\psi):=\frac{||\Delta\psi||+b_1||\nabla\psi||}{2\pi}I_0.
\tag{AT19}
\]

For AT19 use the complex test psi_x-i psi_y: its partial_bar
derivative is Delta psi/2. The vector convention is (Re j,Im j).

Now differentiate the **exact** weak identity VE15 of Note 14, at a
fixed test function, not its upper bound. Off the simple zeros,

\[
\partial_t\log(1+q/|H|^2)=w(r_t+2\Re h_2),\quad
w_t=w(1-w)(r_t+2\Re h_2).
\tag{AT20}
\]

The 1/|z-a_j| singularities are locally integrable. Factoring each
simple zero on a common time neighborhood, or excising disks and then
taking their radii to zero, justifies these distributional derivatives.
There is no extra point mass in the first time derivative of the
logarithm. Define

\[
\mathcal K_r(\psi)=||\Delta\psi||+2b_1||\nabla\psi||
+(b_2+b_1^2)||\psi||,
\]
\[
\mathcal K_{r,t}(\psi)=2b_{1t}||\nabla\psi||
+(b_{2t}+2b_1b_{1t})||\psi||,
\tag{AT21}
\]

where b_{1t}=||grad r_t||, b_{2t}=||Delta r_t||, and a_0=||r_t||.
The finite bounds are

\[
|\langle\rho-\nu,\psi\rangle|
\le E_R(\psi):=\mathcal K_r(\psi)\Lambda_0/(4\pi),
\]
\[
\boxed{|\langle\partial_t\rho-\partial_t\nu,\psi\rangle|
\le E_T(\psi):=\frac{\mathcal K_r(\psi)(a_0W_0+2I_0)
+\mathcal K_{r,t}(\psi)W_0}{4\pi}.}
\tag{AT22}
\]

To check the last coefficient, differentiate
w Delta r+w(1-w)|grad r|^2 in VE15. Its w_t coefficient is
Delta r+(1-2w)|grad r|^2; its remaining terms are
w Delta r_t+2w(1-w)grad r dot grad r_t. Together with
2w grad r dot grad psi these give exactly AT21--AT22.

Finally, from the two continuity equations and VE6,

\[
\boxed{|\langle\mathcal S_\epsilon,\psi\rangle|
\le E_T(\psi)+E_D(\psi),\qquad
|\langle\mathcal B_\epsilon,\psi\rangle|
\le [a_0+(b_2+b_1^2)/2]||\psi||W_0.}
\tag{AT23}
\]

For AT1, kappa'=8L+16tL/kappa-2, and Note 14 gives the explicit bounds

\[
a_0\le2L^2+3|\kappa'|/\kappa+X^2|\kappa'|/\kappa^2,
\quad b_1\le2X/\kappa,\quad b_2=2/\kappa,
\]
\[
b_{1t}\le2X|\kappa'|/\kappa^2,\qquad
b_{2t}=2|\kappa'|/\kappa^2.
\tag{AT24}
\]

For fixed K, AT22--AT24 prove the rates in Section 1. The large
2L^2 term is paid against W_0=O(kappa^-2), and the pole term against
I_0. The correlations with w have never been replaced by products of
separate means. The source bound is signed and weak: for the linear
zero H=z with spatially constant q, integral (1-2w)rho=0, whereas
integral |(1-2w)rho|=1/2. An absolute-value estimate of the raw source
would discard precisely this cancellation.

## 6. The moving lattice is a quantitative differentiated reference

Let the sums below run over all c_j=(j+1/2)pi/mu; only finitely many
terms have nonzero weight. Define

\[
R_c=k_h(y)\sum_j k_\ell(x-c_j),\qquad
J_c=-\alpha k_h(y)\sum_j c_j k_\ell(x-c_j).
\tag{AT25}
\]

Since c_j'=-alpha c_j, these obey R_c,t+partial_x J_c=0 exactly, with
R_c,t=alpha k_h(y)sum c_j k_ell'(x-c_j). Compact weights and their
vanishing edge derivatives handle roots crossing a kernel edge.

Set k_i=||k_ell^(i)||_infinity and h_0=||k_h||_infinity. Matching the
actual and carrier roots, using AT11 and |a_j-c_j|<=r_0, gives

\[
|K*\mathbf j-(J_c,0)|
\le E_J(K)+n h_0\{E_vk_0+|\alpha|r_0(k_0+Xk_1)\},
\]
\[
\boxed{|\partial_t(K*\rho)-\partial_tR_c|
\le E_T(K)+n h_0\{E_vk_1+|\alpha|r_0(k_1+Xk_2)\}
=O(L\kappa^{-7/6}).}
\tag{AT26}
\]

The current bound has the same order. In the first formula complex
modulus is identified with the Euclidean norm of the current vector.
Use |a k(x-a)-c k(x-c)|<=r_0(k_0+Xk_1), and the same inequality
with k' for the derivative; both a,c lie in the comparison interval.
Thus the density and current derivative comparison is obtained from
velocity estimates and weak bridges, not from differentiating the
static location allowance in Note 12.

The distinction between this reference and a smooth continuum matters.
With p=pi/mu, three integrations by parts in the periodization of
g(a)=a k_ell'(x-a) give

\[
|\partial_tR_c-(\mu'/\pi)k_h(y)|
\le |\alpha|h_0\frac{3p^2}{8\pi^3}
\{3||k_\ell^{(3)}||_1+(|x|+\ell)||k_\ell^{(4)}||_1\}.
\tag{AT27}
\]

Here sum_(n>=1)n^-3<=3/2 suffices; g'''=3k'''-a k''''.
The integral of g is one. The zero-extended kernel is C3, so these
integrations introduce no boundary terms. For every fixed height range,
AT26--AT27 imply the continuum derivative error
O(L kappa^-7/6+kappa^-1 L^-2)=o(L/kappa).
On X~kappa^(1/3), the |x|-dependent lattice phase term need not be
controlled below L/kappa by this estimate. Retain R_c there. This is
a limitation of the present continuum comparison, not a theorem that
every smoother kernel or improved phase estimate must fail.

For completeness, four integrations for a k_ell(x-a) give
|J_c+(mu'/pi)x k_h(y)| <= |alpha|h_0 p^3/720 times
[(|x|+ell)||k_ell^(4)||_1+4||k_ell^(3)||_1]. The static density
theorem of Note 12 remains unchanged at its leading rate.

## 7. Checks, finite evaluations, and control premises

The [standard-library script][script] verifies 16 cleared polynomial
identities for AT17 (away from its explicitly treated poles) and AT20
on H=z^2-2t, for four regulators. Nine exact rational moment checks
verify AT5 on three discrete source laws, including the equal-weight
two-atom law. The linear-zero radial integral above checks the signed
cancellation and its nonzero absolute mass. These are exact controls,
not a proof of the full theta estimates or an independent implementation.

The same script evaluates all finite allowances using source bounds
through degree six, with ell=10,h=.75,Y=1,beta=.25. The [record][record]
retains the failed collar/concentration gate at t=10^4. Examples of
**floating allowance / reference scale L/kappa**, not measured errors:

| t | averaged current-source allowance | differentiated moving-clock error allowance |
| ---: | ---: | ---: |
| 10^6 | 0.01783 | 106.31 |
| 10^9 | 8.012e-6 | 1.870 |
| 10^12 | 3.347e-8 | 0.01768 |
| 10^18 | 1.566e-12 | 0.001407 |

The conservative derivative bound is not small in the first two rows.
The passing inequalities are floating substitutions, not interval
certificates; exponential underflow in negligible tail terms is not an
exact zero. This allowance script performs no theta quadrature or root
acquisition. These evaluations demonstrate the size of the explicit
formulas, not independent accuracy.

A separate [six-observation pilot][pilot-script] compares zero-measure
contour observations with AT25 at t=10^6,10^9 and centers
0, 0.8(X-ell), 0.91(X-ell). It evaluates the time covariance before
the contour integral, so the analytically integrating-to-zero constant
E(u^2) is removed before floating subtraction. Source quadrature is
refined from order 32/cutoff 12 to order 48/cutoff 14 in saddle
coordinates; contour order is refined from 224 to 320, with heights
0.6 and 0.8. Eight theta modes are retained. No roots are found or fitted.

The largest observed continuum derivative discrepancy divided by
mu'/pi is 0.003143, at t=10^9 and x=2705.58. The moving-clock
discrepancy is at most 1.923e-9 on these samples, with a maximum
derivative refinement change of 3.991e-10 in the same units; several
smaller discrepancies are at or below their refinement changes.
The [pilot record][pilot-record] preserves each value and refinement.
This supports keeping lattice phase in the derivative observable;
it is not a validated global accuracy rate. Finite-epsilon transfer is
analytic in Sections 4--5, not measured by this zero-measure pilot.
No reduced trajectory is integrated.

The required collision screen is scoped as follows:

| Control | Premise or interpretation |
| --- | --- |
| H=z^2-2t | The algebraic current identity is checked away from zeros and the time identities hold after clearing denominators. At its double event the simple-root collar/velocity hypotheses fail; no event exclusion is inferred. |
| H=z with time-only epsilon | Passes the simple-root local bridge and exhibits the source cancellation exactly. It lacks the theta source and logarithmic growing clock. |
| Stationary cosine/sine heat field | Generic bridges hold and current is zero; its atomic source has no canonical moving saddle. It checks that the bridges do not manufacture motion. |
| Positive finite-atom collision controls | AT5 is generic and passes. At a collision the one-simple-zero collar and derivative floor cannot both hold. The complete theta source and its concentration bounds are absent. |
| Euler-factor controls | Change the canonical arithmetic/source in Note 12; the theta constants are not assigned to them. Generic identities may hold. |
| Weighted-square/finite-prime controls | Change weights and full reflection; no unchanged-source bounds or all-real continuation are supplied. |
| Reflected and positive-primitive controls | Lack the original theta square expansion and the particular complete-source allowances. |
| Nearby positive sources with the same leading tail | May share late-time concentration, transport and earlier collisions. These asymptotics are not an arithmetic discriminator or endpoint-simplicity criterion. |

The old four-family numerical gates are not rerun or represented as
newly certified. The premise failures above are those already documented
in Notes 09, 11--12 and the [control register][controls].

## 8. What remains

This advances HDA-02/04/05/06 within their partial status. It supplies
the selected adaptive forcing/current budgets and a differentiated
growing-window reference, including a continuum derivative on fixed
height ranges. It does not estimate the actual differentiated covariance
Q, identify a stable autonomous closure, or specify all boundary traces.

The next bounded options are to use the weak-current result to audit a
proposed closure against the actual covariance, or to derive the
positive-time outer-height approximation through amplitude turnover.
The latter still needs a new complete complex-saddle estimate. Independent
proof review and interval evaluation of a useful finite onset remain
open. A boundary solve is still gated; RH and endpoint simplicity are
not acceptance targets. See the [assessment][review] and [handoff][next].

[handoff]: 15_CONTINUATION_AFTER_MANUSCRIPT_AND_VARIABLE_EPSILON_20261024.md
[variable]: 14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md
[clock]: 12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md
[saddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[script]: ../numerics/adaptive_transport_checks.py
[record]: ../numerics/ADAPTIVE_TRANSPORT_CHECKS_20261024.json
[pilot-script]: ../numerics/adaptive_transport_theta_pilot.py
[pilot-record]: ../numerics/ADAPTIVE_TRANSPORT_THETA_PILOT_20261024.json
[review]: ../reviews/05_ADAPTIVE_TRANSPORT_SELF_REVIEW_20261024.md
[next]: 17_CONTINUATION_AFTER_ADAPTIVE_TRANSPORT_20261024.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[classification]: ../../../../avoid/01_restating_the_target.md
[status-rule]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[normalization]: ../../../../avoid/08_normalization_and_constant_slips.md
