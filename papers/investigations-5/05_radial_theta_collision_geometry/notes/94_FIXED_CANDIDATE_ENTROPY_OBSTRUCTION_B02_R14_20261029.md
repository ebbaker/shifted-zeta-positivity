# Fixed-candidate entropy fails as a scalar-feedback Lyapunov mechanism

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
ultra**, Investigation05 **chat0035**, *Test scalar carrier attraction*.
Parent synthesis with three same-model contributing derivations/checks;
shared premises, no independent specialist or formal review.

**CTF-B02 R14: one precisely scoped failed route, proved in-note.**
For every M,lambda>0, the fixed-candidate relative entropy has strictly
positive scalar-feedback production at smooth positive radial profiles
with exactly the Gibbs candidate's mass and squared L2 norm, arbitrarily
close to that candidate in H1. Thus the universal entropy-dissipation
inequality needed by this selected mechanism is false, even locally in
H1. These profiles are not asserted to occur on the actual theta orbit.
No nonconvergent solution, failure of all attraction mechanisms, or failure
under separately paid stronger regularity is established.

The actual carrier's entropy chain rule, integrated Fisher information
and special forcing pairing are paid below. Its forcing also has a new
H-minus-one bound, and its spatial orbit is precompact in L2. Neither
fact identifies an omega-limit as stationary. The missing step is a valid
actual-path dissipation/stability mechanism, not equilibrium uniqueness.

[Progress05][progress] records the choice before testing. The inputs are
[Notes89][n89]–[90][n90], with **R13 accepted without mathematical correction**
in [Review46][r46]; historical pending language in Notes89–91 is not the
current disposition. Sol's R5 manuscript is preserved. [Review47][review]
records the present internal checks and [Continuation95][next] gives the
bounded next assessment. No new PDE, source, scan or manuscript work.
Under [avoid01][a01], this is a scoped auxiliary-flow mechanism test, not
an RH-equivalent criterion or a theta collision exclusion. The [result
index][results], [control register][controls] and [avoid index][avoid]
govern status; in particular [avoid07][a07] limits the negative conclusion.

## 1. Fixed equation, candidate and the selected production

On R3 keep v=grad V, V=(r²+log(1+r²))/2, d=div v, 3<=d<=6 and |v|<=2r.
For a fixed lambda>0 write
\[
 q=h_\lambda=Me^{-\lambda\mathcal V}/Z(\lambda),\quad Q=\|q\|_2^2,
 \quad F_\lambda(h)=\int h\log(h/q).
\]
For the actual consumer lambda=lambda_* and Q=E0/n, n=mu²/M²>0, as in
Note90. The structural argument below works for every M,lambda>0.
Write
\[
 G(h)=\int|\nabla h|^2,\quad D(h)=\int dh^2,\quad
 \beta(h)=2G(h)/D(h),
\]
\[
 A(h)=\int dh,\quad C(h)=\int|v|^2h,\quad
 T_\lambda(h)=A(h)-\lambda C(h),\quad
 I(h)=\int |\nabla h|^2/h.                                      \tag{1}
\]
A,C,T are linear functionals here; D is quadratic. They are unrelated to
the cutoff commutators or full weighted-energy production of Note89.
For smooth positive profiles with the stated integrability, direct
integration by parts gives the entropy production of the unchanged field
N(h)=Delta h+beta(h)div(vh):
\[
 \boxed{P_\lambda(h):=\langle\log(h/q)+1,\mathcal N(h)\rangle
 =-I(h)+\lambda A(h)+\frac{2G(h)}{D(h)}T_\lambda(h).}             \tag{2}
\]
Equivalently, with J_lambda=integral h|grad log h+lambda v|²,
\[
 P_\lambda=-J_\lambda+(\beta-\lambda)T_\lambda.                 \tag{3}
\]
Indeed J_lambda=I−2lambda A+lambda²C. At q,
T_lambda(q)=0, beta(q)=lambda and P_lambda(q)=0. The extra term in
(3) is precisely the term unpaid in Note90, not an omitted forcing error.
The classical fixed-coefficient identity applies when beta=lambda.
[Reference16][ref16] and its checked [JKO source][jko] concern that frozen
coefficient setting; no nonlinear convergence theorem is imported here.

## 2. Actual-path entropy, Fisher cost and forcing are paid

Use the **actual** carrier and original alpha from R10–R13. The accepted
uniform bounds are
\[
 \int h=M,\quad \|h\|_2^2\le\bar E=M^2D_{82},\quad
 \|\nabla h\|_2^2\le\bar G=M^2H_{82},\quad
 R_h=\int r^2h\le\bar R=\max(R_0,3M/a_*),
\]
\[
 0<a_*\le\alpha\le\bar\alpha,\quad
 D(h)\ge3E_0,\quad
 \delta=\alpha-\beta(h),\qquad
 \int_t^\infty|\delta|\le\mathcal A_{\rm def}(t)/a_* .           \tag{4}
\]
Here D_82,H_82 are the constants of Note82, not D(h).
R0 contains the entire unit-preparation contribution +6M. The tail is
A_def(t)=4d1 exp(−B(t)/4)+2d2 exp(−B(t)/2). The known physical mass
premise used to obtain K, n and these global bounds is retained.

First, entropy is finite without an assumed lower pointwise floor:
for h>=1, h log h<=h², whereas for every h>=0
\[
 h\log h\ge-r^2h-e^{-r^2}/e.
\]
Thus
\[
 \int|h\log h|\le C_S:=\bar E+\bar R+\pi^{3/2}/e,
 \qquad 0\le\int\mathcal Vh\le\bar R.                          \tag{5}
\]
The finite constant mass term in F_lambda is harmless.

Here is the chain-rule payment, rather than an assumption of uniform
Fisher information. For 0<eta<=1 set
\[
 \Phi_\eta(z)=(z+\eta)\log(z+\eta)-\eta\log\eta,\quad
 g_\eta(z)=z-\eta\log(1+z/\eta).
\]
On each compact regular time interval the inherited smooth positive
carrier equation gives locally
\[
 \partial_s\Phi_\eta(h)
 =\Delta\Phi_\eta(h)-\frac{|\nabla h|^2}{h+\eta}
    +\alpha\operatorname{div}(v\Phi_\eta(h))
    +\alpha d g_\eta(h).                                      \tag{6}
\]
Integrate with nonnegative expanding radial cutoffs chi_R, equal to one
on B_R, with derivatives bounded by c/R and c/R². For fixed eta,
|Phi_eta(h)|<=c_eta h+h². Diffusion boundary terms vanish with R; drift
boundary terms are bounded by c integral_{R<r<2R}|Phi_eta(h)| since
|v|<=2r. They vanish after time integration by dominated convergence,
using the uniform mass/energy bounds. Cutoffs can increase to one, so
monotone convergence pays the nonnegative gradient term. This proves
\[
 S_\eta(t)-S_\eta(u)
 =-\int_u^t\!\int\frac{|\nabla h|^2}{h+\eta}
   +\int_u^t\alpha\!\int d g_\eta(h),\quad S_\eta=\int\Phi_\eta(h).
\]
Since 0<=g_eta(h)<=h and Phi_eta decreases to h log h, with domination
|h log h|+(h+1)log(h+1)<=|h log h|+2h+2h², send eta down to zero.
Monotone convergence of the gradient term proves, rather than supposes,
\[
 S(t)-S(u)=-\int_u^t I(h(s))ds+\int_u^t\alpha A(h)ds,
 \qquad
 \int_u^{u+1}I(h(s))ds\le2C_S+6\bar\alpha M.                  \tag{7}
\]
The initial prepared endpoint has finite entropy by (5). This is
local-in-time integrability and a uniform unit-window bound, not a
pointwise uniform Fisher estimate or finite half-line Fisher integral.

Testing with chi_R V and passing to the limit gives
(d/ds) integral Vh=A−alpha C in the integrated sense. Its boundary
terms are controlled by the second-moment tail: V<=r², |grad V|<=2r
and d bounded. Therefore F_lambda is locally absolutely continuous and
\[
 \boxed{\frac d{ds}F_\lambda(h(s))
       =P_\lambda(h(s))+\delta(s)T_\lambda(h(s))\quad\text{a.e.}} \tag{8}
\]
The forcing contribution has the **paid special pairing**
\[
 |\delta T_\lambda(h)|\le(6M+4\lambda\bar R)|\delta|,
\]
\[
 \int_t^\infty|\delta T_\lambda(h)|ds
       \le\frac{6M+4\lambda\bar R}{a_*}\mathcal A_{\rm def}(t).   \tag{9}
\]
This uses the exact divergence structure of the actual forcing, not
continuity of entropy tests in the dual-Lipschitz topology. The same
alpha-weighted tail costs (6M+4lambda Rbar)A_def(t). Consequently the
forcing/Fisher payment is not the obstruction to this selected entropy
route. The unpaid quantity is the sign/coercivity of P_lambda itself.

## 3. Exact mass-energy base profiles with T_lambda>0

Put k=d−lambda|v|². Since v~X and d->3,
k(r)->−infinity, whereas q(r)->0. Thus the three radial functions
1,q,k are linearly independent on r>r0 for any fixed r0>0: an identity
c0+c1q+c2k=0 first forces c2=0 at infinity, then c0=0, then c1=0.
The three corresponding linear functionals on radial C_c^infinity
supported away from the origin are therefore independent. Their map
onto R3 is surjective (otherwise a nonzero linear combination annihilates
all such tests). Choose two such functions w,u with
\[
 (\int w,\langle q,w\rangle,\int kw)=(0,0,1),\qquad
 (\int u,\langle q,u\rangle,\int ku)=(0,1,0).                  \tag{10}
\]
Their supports lie in a fixed compact annulus. No new physical source is
selected: these are test states for the proposed generic inequality.
For small tau>0 the implicit function theorem applied to
\[
 2c+\tau^2\|w\|_2^2+2\tau c\langle w,u\rangle+c^2\|u\|_2^2=0
\]
gives c(tau)=−tau²||w||2²/2+O(tau³). Hence
\[
 b_\tau=q+\tau w+c(\tau)u>0,\quad
 \int b_\tau=M,\quad\|b_\tau\|_2^2=Q,\quad T_\lambda(b_\tau)=\tau. \tag{11}
\]
Positivity follows from the positive minimum of q on that annulus;
outside it b_tau=q, including near the origin and at infinity.
All derivatives, polynomial moments, entropy and Fisher information are
finite. All integration by parts in (2) is justified by the Gaussian tail.

Production is smooth for these finite-dimensional compact perturbations.
For any compact smooth j,
\[
 DI(q)[j]=2\lambda\int dj-\lambda^2\int|v|^2j,
 \qquad DP_\lambda(q)[j]=0.                                  \tag{12}
\]
The first identity follows by differentiating I and using grad q/q=−lambda v;
the second follows from T(q)=0 and beta(q)=lambda in (2).
Thus there exist finite C0,Dmax and tau0>0 with
\[
 P_\lambda(b_\tau)\ge-C_0\tau^2,
 \quad 0<D(b_\tau)\le D_{\max}\quad(0<\tau<\tau_0).             \tag{13}
\]
Here C0 is a scalar Taylor allowance, not the manuscript commutator.
These constants are defined by bounded derivatives on a compact interval
of positive compact perturbations; no numerical estimate is needed.

## 4. A gradient spike with vanishing mass, energy and Fisher cost

Fix a nonzero nonnegative smooth radial bump phi supported in the unit
ball, positive in its interior, and put psi=phi². Define
\[
 z_{\epsilon,a}(X)=a\epsilon^{-1/2}\psi(X/\epsilon),\quad a>0.
\]
Straight changes of variables give the exact scalings
\[
 \int z=a\epsilon^{5/2}\int\psi,\quad
 \|z\|_2^2=a^2\epsilon^2\|\psi\|_2^2,\quad
 G(z)=a^2G(\psi),\quad
 I(z)=a\epsilon^{1/2}I(\psi),                                 \tag{14}
\]
where I(psi)=4||grad phi||2². The second moment is
 a epsilon^(9/2) integral r²psi. At zeros use the usual zero extension
of |grad psi|²/psi. Every constant is finite, and G(psi)>0.

For fixed tau,a, restore the two constraints exactly, not just
asymptotically. Choose a smooth radial p supported in the outer annulus
with integral p=1. The mass correction is
m_epsilon=−integral z. Put
\[
 b_{\tau,\epsilon}=b_\tau+m_\epsilon p+\ell_\epsilon u,
 \qquad h_{\tau,\epsilon}=b_{\tau,\epsilon}+z_{\epsilon,a}.       \tag{15}
\]
For sufficiently small tau, <b_tau,u> is nonzero, tending to 1 as tau->0.
Take epsilon small enough that the spike and p,u supports are disjoint.
The energy equation for ell_epsilon has nonzero linear derivative
2<b_tau+m_epsilon p,u>, and residual
\[
 2m_\epsilon\langle b_\tau,p\rangle+m_\epsilon^2\|p\|_2^2
       +2\langle b_\tau,z\rangle+\|z\|_2^2=O(\epsilon^2).
\]
Its small root has ell_epsilon=O(epsilon²). This is also immediate
from the quadratic formula with its root continuous at zero. Therefore
\[
 \int h_{\tau,\epsilon}=M,\qquad
 \|h_{\tau,\epsilon}\|_2^2=Q,\qquad h_{\tau,\epsilon}>0.         \tag{16}
\]
The base corrections tend smoothly to zero on the fixed annulus; near
zero b_{tau,epsilon}=q. Positivity is preserved for small epsilon.

For fixed tau,a, the gradient cross term tends to zero, for example by
|<grad b,grad z>|<=||Delta b||infinity integral z on the spike ball.
All relevant linear moments converge, and h converges in L2 to b_tau.
Consequently
\[
 G(h_{\tau,\epsilon})\to G(b_\tau)+a^2G(\psi),\quad
 D(h_{\tau,\epsilon})\to D(b_\tau),\quad
 (A,C,T)(h_{\tau,\epsilon})\to(A,C,T)(b_\tau).                 \tag{17}
\]
Fisher convergence requires a separate argument. Cauchy–Schwarz pointwise
gives I(f+g)<=I(f)+I(g) for positive f and nonnegative g. Thus limsup I(h)
<=I(b_tau) by (14). Outside the shrinking spike ball h=b_{tau,epsilon};
the omitted base Fisher integral tends to zero. This gives the matching
liminf and hence I(h)->I(b_tau). The peak causes no unpaid Fisher cost.
Combining (2), (11), (17),
\[
 \boxed{P_\lambda(h_{\tau,\epsilon})\longrightarrow
 P_\lambda(b_\tau)+\frac{2a^2G(\psi)\tau}{D(b_\tau)}.}          \tag{18}
\]

## 5. Positive production arbitrarily close in H1

Choose one finite L>0 with 2L G(psi)/Dmax>C0+2 and set a²=L tau.
Equations (13),(18) make the limiting production greater than 2tau².
For each sufficiently small tau choose epsilon(tau)>0 so that the exact
profile (15) has P_lambda>tau². This is an analytical existence choice,
not a parameter scan or numerical sign sample. Choose epsilon(tau) also
small enough that each moment/Fisher convergence error and the H1 norm
of the constraint correction are at most tau, and epsilon(tau)<tau².
Then
\[
 \boxed{\int h=M,\quad\|h\|_2^2=Q,\quad
 h\longrightarrow q\ \text{in }H^1,\quad P_\lambda(h)>0.}       \tag{19}
\]
Indeed ||b_tau−q||H1=O(tau), and the spike's squared gradient norm is
L tau G(psi); its L2 norm and the constraint corrections vanish.
The second moments, Fisher information and beta also tend to their
values at q. Relative entropy tends to zero: it vanishes continuously
on the fixed annular perturbations; on the spike ball the entropy cost
is O(a epsilon^(5/2)(1+|log(a epsilon^(-1/2))|)), with bounded log q
there. Outside these sets h=q. The lower bound F_lambda>=0 follows
from equality of masses and convexity, and is consistent with positive
production away from q.

Every profile in (19) is smooth, strictly positive, radial, equals q
outside a compact set, and has all polynomial moments and all finite
Sobolev norms. H1, second moment and Fisher bounds are uniform along
the sequence and approach the equilibrium values. The sequence has
uncontrolled peak height and higher derivatives; epsilon<tau² can in
particular force its peak to diverge. No uniform L-infinity, H2 or
weighted higher-derivative bound is asserted.

This disproves the universal inequality P_lambda<=0 on this state class,
even in every H1 neighborhood of the selected equilibrium. It is an
infinitesimal entropy-production counterexample; no independently
evolved nonlinear trajectory or long-time well-posedness result for
these test profiles is needed or claimed. The actual prepared theta
orbit is not replaced by one of them. Specific numerical R13 upper
allowances are not asserted to admit them unless the needed slack and
additional actual-path restrictions are checked. Small H1 distance,
finite moments/Fisher cost, and a small beta−lambda alone cannot justify
the missing sign.

## 6. Additional actual-path topology payments, without stationarity

These short deductions clarify what remains after this failed route.
They are new consequences of (4), not stronger norms attributed to R13.
For a smooth radial H1 function, integration of (r²h²)' from r to infinity
and Cauchy–Schwarz give
\[
 r^2h(r)^2\le2\int_r^\infty t^2|h h'|dt
       \le\frac{\|h\|_2\|\nabla h\|_2}{2\pi}.
\]
The identity follows first for decaying smooth functions, then by radial
H1 approximation; an endpoint subsequence suffices before passage to
infinity. Thus for the nonnegative actual carrier,
\[
 rh(r)\le C_r:=\frac{(\bar E\bar G)^{1/4}}{\sqrt{2\pi}},\quad
 \int r^2h^2\le C_r\int rh\le C_r\sqrt{M\bar R}.
\]
It follows that
\[
 \|vh\|_2\le V_2:=2C_r^{1/2}(M\bar R)^{1/4},\qquad
 \|\mathfrak f_s\|_{H^{-1}}\le V_2|\delta(s)|,
\]
\[
 \boxed{\int_t^\infty\|\mathfrak f_s\|_{H^{-1}}ds
              \le(V_2/a_*)\mathcal A_{\rm def}(t).}            \tag{20}
\]
Here H-minus-one is the dual of the standard H1 norm, since
|<div(vh),phi>|<=||vh||2||grad phi||2. The alpha-weighted tail is
V2 A_def(t). This proves no L2 bound on div(vh).

The same radial bound gives a uniform L2 tail:
\[
 \int_{r>R}h^2\le(C_r/R)\int_{r>R}h
                  \le C_r\bar R/R^3.                         \tag{21}
\]
Uniform H1 gives local L2 compactness on each ball by the Rellich
compact embedding. A diagonal subsequence and (21) give precompactness
of the spatial orbit {h(s):s>=0} in L2. All its hypotheses are paid in
(4); no uniform pointwise H2 or moment of h² is assumed.

This is spatial compactness, not an invariance principle. For fixed tau
and a in (17), L2 convergence with a bounded H1 norm can retain a positive
gradient-energy defect, so beta is not continuous in L2 on that larger
state class. More actual time regularity may remedy passage to a limit,
but even a complete limiting trajectory still needs an argument making
it stationary. Neither (20),(21) nor a unique stationary candidate supplies
that argument. No coefficient limit follows; alpha would require its own
derivative/feedback control rather than a limit of h in L2 alone.

## 7. Direct comparison, controls and the stopping boundary

The strongest equally informed direct comparator receives exactly (4),
the full source, original alpha, physical mass margin, preparation, R12
errors and R13 transfers. It proves (5)–(9), (20),(21) identically and
encounters the same sign obstruction (19). No primitive-specific gain,
source erasure, smaller full residual allowance or physical-margin removal
is demonstrated. The actual carrier remains the one derived from the
unchanged theta source at (T,A)=(1/4,2).

The genuine residuals, raw carrier/centered mismatch, changed primitive
endpoints, full C0/C1, combined sphere cancellation and entire inner ball
are untouched. The whole-space entropy calculation introduces no wall at
r=1 and does not reset the source before preparation.

| Control or comparison | Exact scope or failed premise |
| --- | --- |
| The profiles (19) | Test the generic mass-energy entropy inequality; they are not claimed to be the complete-theta prepared source or points on its orbit. All spatial finiteness assumptions used by that inequality hold. |
| Weighted-square positive sources | Can pass a low-mark margin and collide at another mark; at an admitted double event mu=0 the physical positive-mass premise for global K and nD_h fails. No new event is inferred. |
| Gaussian-polynomial, reflected, smooth shape and positive-primitive controls | Generic scalar identities may hold; an admitted double event fails the positive physical vector-mass premise. Primitive positivity does not replace it. Keep their registered regularity and parameter domain. |
| Finite-prime and conditional endpoint controls | Preserve their declared restrictions/conditionality and differ from the full unchanged theta source; at admitted double events the positive-mass premise fails. No new moments or event locations are supplied. |
| Fixed-amplitude variable-observation control | Fails literal cosine/full Newman identity in the upstream mass payment; theta's K cannot be transferred to its zero-mass mark. |
| Euler-factor Laguerre witness | A negative witness is not by itself a double event; no zero-mass claim is manufactured. |
| Atomic/profile controls | Need the inherited preparation, regularity, moments and actual-path premises before applying this auxiliary analysis. |

**Stop:** the selected fixed-candidate entropy route fails as a universal
Lyapunov argument on the stated mass-energy/H1 information class. This
fulfills R14's scoped-failure boundary. Actual attraction, coefficient
limits and nonlinear shadowing remain open. A different functional or a
specific stronger actual-path dissipation mechanism is a future B02
choice, not an unrecorded extension of this test. No E07 convergence
contract is ready: there is no valid remaining convergence route whose
steps have merely been reduced to execution. The next fixed work is the
bounded E08 R14 assessment of this proof and its scope, recommended Sol.

[n82]: 82_COMMON_CARRIER_SYNCHRONIZATION_R12_20261029.md
[n89]: 89_COMPLETE_CARRIER_PRODUCTION_TRANSFER_R13_20261029.md
[n90]: 90_CARRIER_FEEDBACK_DEFECT_AND_STATIONARY_CANDIDATE_R13_20261029.md
[r46]: ../reviews/46_COMPLETE_CARRIER_REDUCTION_E08_R13_ASSESSMENT_20261029.md
[review]: ../reviews/47_FIXED_CANDIDATE_ENTROPY_INTERNAL_REVIEW_R14_20261029.md
[next]: 95_ENTROPY_ROUTE_DISPOSITION_AND_MODEL_CONTINUATION_R14_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[ref16]: ../references/16_FIXED_DRIFT_GIBBS_AND_FEEDBACK_SCOPE_20261029.md
[jko]: https://www.ceremade.dauphine.fr/~carlier/JorKinOtto
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
