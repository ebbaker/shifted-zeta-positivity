# Actual-carrier attraction by radial logarithmic-slope squeezing

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort ultra**,
Investigation05 **chat0035**, *Test scalar carrier attraction*. Parent
synthesis with three read-only same-model contributing checks; shared
premises remain, no independent specialist or formal review.

**Status: complete proof in-note, pending fixed E08 R15 assessment.**
For the original prepared theta carrier at the unchanged physical mark
(T,A)=(1/4,2), under the accepted R10–R13 physical-mass inputs, we prove
\[
 \|h(s)-h_{\lambda_*}\|_{H^1(\mathbb R^3)}\longrightarrow0,
 \qquad \beta(h(s))\longrightarrow\lambda_*,\qquad
 \alpha(s)\longrightarrow\lambda_* .                         \tag{1}
\]
The mechanism is contraction of the full spatial range of
z=−h_r/(V'h). Its positive initial interval is proved for the complete
unit-heat-prepared source. Positivity makes beta a weighted average of z;
the exact coefficient defect then pays the range contraction. All
comparisons use the actual carrier and actual alpha. There is no second
scalar solution or inference from stationary uniqueness alone.

R13 is accepted in [Review46][r46]; R14 is accepted in [Review48][r48].
The entropy obstruction [Note94][n94] remains valid. We do not claim a
new entropy sign. [Progress05][progress] records this mechanism before
testing; [Review49][review] and [Continuation99][continuation] give the
assessment qualification and stopping boundary. This is an auxiliary-flow
milestone, not an RH-equivalent criterion or new collision exclusion.

## 1. Exact path and accepted inputs

Write r=|X|, with integrals in R3 unless stated otherwise, and set
\[
 V(r)=\tfrac12r^2+\tfrac12\log(1+r^2),\quad
 b(r)=V'(r)=r+\frac r{1+r^2},\quad v=\nabla V,
\]
\[
 d=\operatorname{div}v=3+\frac{3+r^2}{(1+r^2)^2},\quad
 b'=1+\frac{1-r^2}{(1+r^2)^2}\in[7/8,2],\quad
 \gamma=-\frac{d'}b=\frac{2(r^2+5)}{(1+r^2)^2(r^2+2)}\in[0,5].       \tag{2}
\]
Ratios at r=0 are their smooth even extensions; b/r lies in [1,2].
The actual equation remains
\[
 h_s=\Delta h+\alpha(s)\operatorname{div}(vh),\qquad
 \beta(h)=\frac{2G_h}{D_h},\quad G_h=\|\nabla h\|_2^2,
 \quad D_h=\int d h^2.                                      \tag{3}
\]
The original vector feedback is alpha=2G_W/D_W, not an independently
chosen coefficient. Accepted [Notes28][n28], [29][n29], [40][n40],
[67][n67], [82][n82] and [90][n90] give the global positive smooth radial
prepared path, finite-interval local classical regularity including the
origin, and the following quantitative inputs:
\[
 \int h=M>0,\quad \|W\|_2^2=E_0>0,\quad W=ah+e,\quad
 |a|^2=n=\mu^2/M^2\ge n_*=(70/73)^2>0,
\]
\[
 0<a_*\le\alpha(s)\le\bar\alpha<\infty,\qquad
 B(s)=\int_0^s\alpha(t)dt\ge a_*s,
\]
\[
 \|h\|_2^2\le M^2D_{82},\quad \|\nabla h\|_2^2\le M^2H_{82},\quad
 \|e\|_2^2\le L_\Sigma e^{-B/2},\quad
 \|\nabla e\|_2^2\le T_\Sigma e^{-B/2},                       \tag{4}
\]
where D82,H82 are D,H of Note82 (10). In particular the global H1
budget used below is already paid on this very path. Note90 (8)–(9),(20)
supplies explicit finite d1,d2 and
\[
 \delta=\alpha-\beta(h),\quad
 |\delta(s)|\le d_1e^{-B(s)/4}+d_2e^{-B(s)/2},
\]
\[
 |\|h(s)\|_2^2-E_0/n|\le\epsilon_E(s):=
 \frac{2\sqrt{E_0L_\Sigma}}n e^{-B(s)/4}
       +\frac{L_\Sigma}n e^{-B(s)/2}.                         \tag{5}
\]
The original physical vector-mass premise is retained in (4)–(5);
it cannot be omitted at an admitted double event. No new numerical
estimate or parameter acquisition is made here.

For lambda>0 put
\[
 q_\lambda=h_\lambda=\frac{M e^{-\lambda V}}{Z(\lambda)},\quad
 Z(\lambda)=\int e^{-\lambda V},\quad
 Q(\lambda)=\|q_\lambda\|_2^2
             =M^2\frac{Z(2\lambda)}{Z(\lambda)^2}.             \tag{6}
\]
Note90 proves Q is continuous, strictly increasing onto (0,infinity),
with positive continuous derivative: if p_lambda=e^(-lambda V)/Z(lambda),
then Q'/Q=2(E_lambda V−E_2lambda V)>0. Thus lambda* is the unique number
Q(lambda*)=E0/n, equivalently Z(2lambda*)/Z(lambda*)²=E0/mu².
The argument below first approximates the actual profile by q_beta;
only then does (5) select lambda*.

## 2. A complete-source payment for the initial slope interval

The exact raw positive carrier is
\[
 F(R)=\mathbf1_{R\ge1}\rho_{1/4}(R)
                  [1+(\log R)^2/4],\qquad h(0)=K_1*F,
 \quad K_1(X)=(4\pi)^{-3/2}e^{-|X|^2/4}.                     \tag{7}
\]
This is the same unit preparation as the prior notes. On R>=1 the
complete theta source, not a finite approximation, is
\[
 \rho_T(R)=\frac\pi4 R^{3/2}e^{(T/4)(\log R)^2}
       \sum_{j\ge1}(j^4-cj^2/R^2)e^{-\pi j^2R^2},
 \qquad c=3/(2\pi)<1/2.                                    \tag{8}
\]
All summands are positive. Their first differentiated series is
uniformly dominated on R>=1 by the Gaussian bounds in Note40. The
logarithmic derivative of the sum is therefore the positive weighted
average of the summand logarithmic derivatives, each satisfying
\[
 R(\log\rho_{T,j})'
 =\tfrac32+\tfrac T2\log R-2\pi j^2R^2
                         +\frac{2c}{j^2R^2-c}.              \tag{9}
\]
Moreover 2log R/[4+(log R)²]<=1/2. For R>=1 define the non-truncated
radial value f(R)=rho_(1/4)(R)[1+(log R)²/4]e^(-R²/4). Using pi>3
and 2c/(j²R²−c)<2 gives
\[
 R(\log f)'\le4+\tfrac18\log R-\tfrac{13}2R^2
                       \le-\tfrac{19}8 R^2.                 \tag{10}
\]
The second step uses 4<=4R² and log R<=R². Set g(q)=f(sqrt(q)), q>=1;
then (log g)'<=−19/16. Translation yields, for a>=1,t>=0,
\[
 \frac{\int_{a+t}^{\infty}g(q)dq}{\int_a^{\infty}g(q)dq}
       \le e^{-19t/16},\qquad
 \mathbb E[q-a\mid q\ge a]\le16/19.                         \tag{11}
\]
The expectation uses density proportional to g on the indicated tail.

Project the radial density 1_(|Y|>=1)f(|Y|) onto its first coordinate:
\[
 \nu(y)=2\pi\int_{\max(1,|y|)}^\infty Rf(R)dR.               \tag{12}
\]
It is positive, even, continuous at ±1, and has Gaussian tails.
Define its one-dimensional Stein integration factor directly by
\[
 \tau(y)\nu(y)=\int_y^\infty u\nu(u)du.                      \tag{13}
\]
This classical identity is annotated in [Reference17][ref17]; we derive
the required bounds and use no concentration or convergence theorem.
Fubini, evenness and (12) give for y>=0
\[
 \tau(y)=\tfrac12\mathbb E[R^2-y^2\mid R\ge\max(1,y)],       \tag{14}
\]
with measure Rf(R)dR, and tau is even. Equation (11) proves
\[
 0<\tau(y)\le
 \begin{cases}35/38,&|y|\le1,\\8/19,&|y|\ge1.\end{cases}    \tag{15}
\]
Although nu' has a jump at ±1, tau nu is C1 and (tau nu)'=−y nu.
Thus integration by parts has no missing sphere contribution. Gaussian
tails pay both endpoints for every exponential test. Under the tilted
probability density proportional to exp(ty)nu(y), this gives
\[
 \mathbb E_tY=t\mathbb E_t\tau.                              \tag{16}
\]
Formula (7), without changing its normalization, becomes
\[
 h(0,r)=(4\pi)^{-3/2}e^{-r^2/4}
                           \int e^{ry/2}\nu(y)dy.
\]
Consequently, for r>0,
\[
 -\frac{h_r(0,r)}{r h(0,r)}
       =\tfrac12-\tfrac14\mathbb E_{r/2}\tau
                         \in[41/152,1/2].                   \tag{17}
\]
Differentiation and the limit r=0 are justified by the same Gaussian
tails. Dividing by b/r in [1,2] proves the global seed
\[
 \boxed{m_0:=41/304\le z(0,r):=-\frac{h_r(0,r)}{b(r)h(0,r)}
                        \le M_0:=1/2\quad(0\le r<\infty).}  \tag{18}
\]
At zero define z(0,0)=−h_rr(0,0)/(2h(0,0)). In particular this estimate
covers the whole prepared inner ball; the raw exterior indicator in (7)
has neither been dropped nor reapplied after preparation.

## 3. Global slope confinement without assuming quotient growth

Let
\[
 m=\min\{m_0,a_*\}>0,\qquad
 \Lambda=\max\{M_0,\bar\alpha\}<\infty.                      \tag{19}
\]
We first pay the finite-time boundedness needed for comparison; it is
not inferred from an assumed bound on z. Integrating (18) gives
h(0,r)<=A0 exp(−m0V), A0=M/Z(M0), and
|grad h(0)|<=M0 b h(0). Since b<=2r and V>=r²/2,
\[
 \|h(0)^2+|\nabla h(0)|^2\|_\infty
       \le C_0:=A_0^2[1+4M_0^2/(e m_0)]<\infty.             \tag{20}
\]
This C0 is only a bound in this proof, not a replacement for the existing
source/residual coefficients denoted C0 elsewhere.

For F_s=h²+|grad h|² (the subscript labels time, not differentiation),
direct differentiation of (3), using d<=6, ||Dv||<=2 and |grad d|<=10,
gives
\[
 (\partial_s-\Delta-\alpha v\cdot\nabla)F_s
                         \le26\bar\alpha F_s.               \tag{21}
\]
Indeed the h² term is at most 12alpha h², while the gradient term is
at most 16alpha|grad h|²+20alpha|h||grad h|, and the latter mixed term
is at most 10alpha(h²+|grad h|²). Negative Hessian terms are discarded.
No time derivative of alpha is used. The constants follow directly from
(2); for example |d'|=2r(r²+5)/(1+r²)³<=10.

Here is a whole-space justification of the maximum bound from (21).
The function f_s=exp(−26baralpha s)F_s is locally smooth and uniformly
L1 on each finite interval by (4). Kato's inequality, obtained by smooth
convex approximation, makes w=(f_s−C0)_+ a distributional subsolution
of w_s<=Delta w+alpha v·grad w. Integrate against expanding radial
cutoffs. The divergence term contributes −alpha int d w<=0; the
remaining cutoff terms tend to zero since |v| grows at most linearly,
w<=f_s is L1 in space-time, and derivatives of the cutoff have their
usual R^(-1),R^(-2) bounds. Initial w is zero. Thus w=0 and
\[
 \|h(s)^2+|\nabla h(s)|^2\|_\infty
                         \le C_0e^{26\bar\alpha s}.         \tag{22}
\]
This finite-window bound suffices below; it is not a new uniform
higher-derivative hypothesis.

For a constant c>0 define the **linear** commuted variable
\[
 \xi_c=h_r/b+c h.
\]
It is smooth and even at zero, with xi_c(0)=h_rr(0)/2+c h(0).
It is bounded on every finite time interval: use (22) and b>=r outside
the unit ball and inherited local classical regularity on the closed
inner ball. Directly commuting the radial equation (3) gives
\[
 (\xi_c)_s=(\xi_c)_{rr}
 +\left(\frac{2b'}b+\frac2r+\alpha b\right)(\xi_c)_r
 +\left[\frac{d'}b+2(\alpha-c)b'+\alpha d\right]\xi_c
 -(\alpha-c)\left(2cb'-\frac{d'}b\right)h.                   \tag{23}
\]
The apparent singular drift equals
\[
 \frac4r+r\left[-\frac4{(1+r^2)(2+r^2)}
                    +\alpha\frac{2+r^2}{1+r^2}\right].      \tag{24}
\]
An even smooth radial function in (23) can therefore be viewed in R5
for the maximum principle: 4/r is exactly the radial Laplacian term,
the remaining vector drift is smooth with at most linear growth, and
the zeroth-order coefficient is bounded. This is a comparison proof
device for the same radial function, not a change of the physical PDE
or its three-dimensional mass measure.

For clarity, bounded subsolutions of this R5 comparison satisfy the
usual whole-space sign principle: subtract epsilon exp(Ks)(1+r²),
where K dominates the bounded potential and the linear drift on the
finite interval. A positive maximum is then in a compact region; the
local maximum principle, with an additional exponential removing the
upper bound on the potential, gives nonpositivity. Let epsilon decrease
to zero. This proves the needed comparison without boundary data at
infinity or an assumption that a spatial extremum is attained.

For c=m, alpha−c>=0 and 2cb'−d'/b>0; (23) has nonpositive source
and initially xi_m<=0. Hence xi_m<=0. For c=Lambda, the source is
nonnegative and xi_Lambda is initially nonnegative, so xi_Lambda>=0.
The actual h is positive, and local divisions by h are legitimate.
We have proved, rather than assumed,
\[
 \boxed{m\le z(s,r)\le\Lambda\quad(s\ge0,\ r\ge0).}         \tag{25}
\]
No positive global spatial lower bound for h is used.

## 4. Exact slope equation and the scalar feedback average

Writing h_r=−zbh in (3), or differentiating the logarithmic equation,
now gives the globally bounded smooth slope equation
\[
 z_s=z_{rr}+\left(\frac{2b'}b+\frac2r+(\alpha-2z)b\right)z_r
            +(\alpha-z)\left(2b'z-\frac{d'}b\right).        \tag{26}
\]
The R5 interpretation in (24) still applies, with alpha replaced by
alpha−2z in the final drift term. All coefficients needed for comparison
are bounded or grow at most linearly by (25).

Let K_s(r)=int_0^r z(s,t)b(t)dt. Then
\[
 h(s,r)=\frac{M e^{-K_s(r)}}{J_s},\qquad
 J_s=\int e^{-K_s},\qquad mV\le K_s\le\Lambda V,
\]
\[
 Z(\Lambda)\le J_s\le Z(m),\qquad
 h(s,r)\le A e^{-mV(r)},\qquad A=M/Z(\Lambda).               \tag{27}
\]
Thus all polynomial moments of h and h² required here are finite
uniformly in time. Also |grad h|<=Lambda |v| A exp(−mV), paying
the weighted first-derivative integrals and all radial boundary terms.
In particular integration by parts at zero and infinity is justified:
\[
 D_h=\int d h^2=-2\int vh\cdot\nabla h
                    =2\int z|v|^2h^2,
\]
\[
 \boxed{\beta(h)=\frac{\int z^2|v|^2h^2}
                           {\int z|v|^2h^2}.}               \tag{28}
\]
The denominator is positive since z>=m and h>0. Hence beta is a
positive weighted average of z. This spatial derivative identity is
the structural gain unavailable to the unrestricted R14 state class.

## 5. Range contraction with the actual forcing fully retained

Set
\[
 k=7m/4>0,\qquad K=4\Lambda+5.
\]
Here K is the reaction bound for this note, distinct from the R10
gradient constant. For any z in [m,Lambda],
k<=2b'z−d'/b<=K. Solve the two scalar Lipschitz ODEs with the SAME
actual alpha from (3):
\[
 u'=k(\alpha-u)+(K-k)(\alpha-u)_+,\quad u(0)=M_0,
\]
\[
 \ell'=k(\alpha-\ell)-(K-k)(\ell-\alpha)_+,\quad\ell(0)=m_0. \tag{29}
\]
The interval [m,Lambda] is invariant for each ODE since alpha is in it,
and ell<=u is preserved (at equality the upper derivative is at least
the lower derivative). Their derivatives are, respectively, the maximum
and minimum of c(alpha−u) and c(alpha−ell) over c in [k,K]. Thus u is
a supersolution and ell a subsolution of (26). Reaction differences are
uniformly Lipschitz on [m,Lambda]; freezing the bounded actual z in the
drift and using the comparison principle already paid above proves
\[
 \ell(s)\le z(s,r)\le u(s),\qquad \ell(s)\le\beta(s)\le u(s). \tag{30}
\]
One can compare the differences directly; no maximum of z needs to
be attained, and no nonlinear feedback equation for a second profile
is being solved.

Let w=u−ell. Subtracting (29) gives exactly
\[
 w'=-kw+(K-k)[(\alpha-u)_++(\ell-\alpha)_+].                 \tag{31}
\]
The bracket is dist(alpha,[ell,u])<=|alpha−beta| by (30). Consequently
\[
 \boxed{\operatorname{osc}_r z(s,r)\le w(s)\le\Omega(s):=
 \frac{111}{304}e^{-ks}
 +(K-k)\int_0^s e^{-k(s-t)}|\delta(t)|dt.}                  \tag{32}
\]
Every time, including the initial interval, is covered. With
\[
 \mathcal F(k,c;s)=
 \begin{cases}(e^{-cs}-e^{-ks})/(k-c),&k\ne c,\\
 s e^{-ks},&k=c,\end{cases}
\]
the accepted all-time defect (5) implies the explicit decay bound
\[
 \Omega(s)\le\frac{111}{304}e^{-ks}
 +(K-k)[d_1\mathcal F(k,a_*/4;s)+d_2\mathcal F(k,a_*/2;s)]
 \longrightarrow0.                                        \tag{33}
\]
This is the full stability payment. We use the exact forcing structure
f_s=delta(s)div(vh), which in (26) changes the reaction coefficient
through alpha and in (31) costs at most (K−k)|delta|. It also enters
the transport coefficient, but the constant spatial barriers have zero
gradient, so this adds no forcing cost. No estimate for
an arbitrary distribution in the dual-Lipschitz seminorm is promoted to
a stronger stability norm; no derivative of delta is taken. The bounded
slope and Gaussian weighted costs needed to manipulate the actual
equation have been proved in (18)–(28). The result is accordingly not
a shadowing theorem for arbitrary weak forcing.

## 6. Profile, gradient and parameter convergence with explicit costs

Put c(s)=beta(h(s)), so c is in [ell,u] and hence [m,Lambda]. From
(30)–(32), |z−c|<=Omega and
\[
 |K_s(r)-c(s)V(r)|\le\Omega(s)V(r).
\]
Both exponents are at least mV. The mean value theorem gives
|exp(−K_s)−exp(−cV)|<=Omega V exp(−mV). Define finite constants
and a radial envelope
\[
 J_1=\int V e^{-mV},\quad Z_\Lambda=Z(\Lambda),\quad
 P(r)=A\left[V(r)+\frac{J_1}{Z_\Lambda}\right]e^{-mV(r)}.
\]
Using |J_s−Z(c)|<=Omega J1 and both denominators >=Z_Lambda yields
\[
 \boxed{|h(s,r)-q_{c(s)}(r)|\le\Omega(s)P(r).}               \tag{34}
\]
Also h,q_c<=A exp(−mV). The actual derivative identity
\[
 \nabla h-\nabla q_c=-(z-c)vh-cv(h-q_c)                     \tag{35}
\]
therefore proves
\[
 \|h-q_c\|_{H^1}\le C_H\Omega,\quad
 C_H=\|P\|_2+A\||v|e^{-mV}\|_2+\Lambda\||v|P\|_2<\infty.  \tag{36}
\]
The sum of the L2 and gradient bounds dominates the H1 norm. All
displayed integrals are finite because V>=r²/2, |v|<=2r and V grows
at most quadratically plus a logarithm; they need no new acquisition,
Fisher-information hypothesis, compactness theorem or higher derivative
bound. This also explicitly pays the extra derivative cost beyond L2.

With B2=A sqrt(Z(2m)), both L2 norms are <=B2, so (5),(34) imply
\[
 |Q(c(s))-Q(\lambda_*)|
     \le\epsilon_E(s)+2B_2\|P\|_2\Omega(s)=:\mathcal E(s)
     \longrightarrow0.                                    \tag{37}
\]
Since c(s) remains in [m,Lambda], continuity and strict monotonicity
of Q first show lambda* belongs to this same interval and c(s) tends
to lambda*. This uses a proved approximation to the Gibbs family, not
the unsupported assertion that an omega-limit must be stationary.
Set
\[
 q_*=\min_{[m,\Lambda]}Q'(\lambda)>0,\qquad
 L_H=\sup_{[m,\Lambda]}\|\partial_\lambda q_\lambda\|_{H^1}<\infty.
\]
The first is positive by (6). For the second,
partial_lambda q_lambda=(E_lambda V−V)q_lambda; its gradient consists
of this factor times −lambda vq_lambda and −vq_lambda. Gaussian
domination on the compact positive lambda interval pays L_H. We obtain
\[
 \boxed{|\beta(h(s))-\lambda_*|\le\mathcal E(s)/q_*,\quad
 \|h(s)-q_{\lambda_*}\|_{H^1}
       \le C_H\Omega(s)+L_H\mathcal E(s)/q_*.}                \tag{38}
\]
Finally
\[
 \boxed{|\alpha(s)-\lambda_*|
             \le|\delta(s)|+\mathcal E(s)/q_*\longrightarrow0.}        \tag{39}
\]

There is also a direct check on the original feedback's own derivatives:
(4),(38) give W→a q_lambda* in H1, since
\[
 \|W-aq_{\lambda_*}\|_{H^1}
 \le\sqrt n\|h-q_{\lambda_*}\|_{H^1}
              +\sqrt{L_\Sigma+T_\Sigma}\,e^{-B/4}\to0.
\]
Thus G_W→n||grad q_lambda*||² and D_W→n int d q_lambda*²>0,
so the unchanged quotient 2G_W/D_W tends to lambda*. This explicitly
controls spatial derivatives in the original feedback, independently of
any inference from L2 convergence alone. No assertion alpha'→0 or bound
on its time derivative is made or needed. Equations (38)–(39) prove (1).

## 7. Direct comparison, controls and precise stopping boundary

The equally informed direct method receives the same complete source,
unit preparation, drift, physical mass, original alpha, uniform H1,
feedback defect and energy limit. It can perform every step (7)–(39).
There is no primitive-specific advantage, reduced full-energy allowance,
or relaxation of the physical-mass premise. The positive weighted-square
source controls inherit the termwise preparation estimate when their
same positive summands and preparation are given; at their admitted
double events mu=0, the inherited n>0/global-feedback/energy-selection
premises (4)–(5) fail. They are therefore not falsely excluded.

The remaining [control cluster12][controls] cases retain their own
conditions: a generic positive Gaussian, reflected source, smooth
primitive, finite-prime or conditional control receives no unproved
theta derivative bound or mass margin; an atomic control requires its
own preparation and derivative payment. A variable observation does
not inherit the literal-cosine mass argument; a negative Euler/Laguerre
quantity is not a double event. The present low-mark theorem gives no
exclusion at other marks and does not change these diagnostics.

The genuine residual, raw/prepared mismatch, centered primitive endpoints,
source C0/C1 terms, sphere cancellations and complete inner ball are
unchanged. The proof works on all of R3 after the original preparation;
(12)–(16) handle the raw sphere explicitly. No reset at r=1, discarded
initial mismatch or replacement source is allowed. The R14 state class
does not impose the common slope interval (25); this does not assert
that every individual counterexample violates every possible slope
band. Positive instantaneous entropy production is compatible with
attraction by (28)–(32). No new entropy sign is inferred.

**Bounded return: one complete actual-path argument. Stop here.** The
previous E07 route was unready; its missing attraction proof is supplied
within this B02 return, so no incomplete convergence execution contract
is issued. A fixed E08/Sol assessment is the next research action, with
the in-note claim provisional until assessed. Do not begin a scan, new
mechanism, manuscript integration or independent scalar-flow campaign.
Sol's accepted R5 main manuscript and companion are preserved. Read the
[result index][results], [avoid index][avoid], [shared-premise warning][a05],
[scope warning][a07], [import warning][a16] and [writer warning][a17].

[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: 29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n40]: 40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n67]: 67_UNIFORM_FEEDBACK_DIRECT_COMPARISON_B02_R10_20261029.md
[n82]: 82_COMMON_CARRIER_SYNCHRONIZATION_R12_20261029.md
[n90]: 90_CARRIER_FEEDBACK_DEFECT_AND_STATIONARY_CANDIDATE_R13_20261029.md
[n94]: 94_FIXED_CANDIDATE_ENTROPY_OBSTRUCTION_B02_R14_20261029.md
[r46]: ../reviews/46_COMPLETE_CARRIER_REDUCTION_E08_R13_ASSESSMENT_20261029.md
[r48]: ../reviews/48_FIXED_CANDIDATE_ENTROPY_E08_R14_ASSESSMENT_20261029.md
[review]: ../reviews/49_RADIAL_LOG_SLOPE_ATTRACTION_INTERNAL_REVIEW_R15_20261029.md
[continuation]: 99_RADIAL_ATTRACTION_AND_MODEL_CONTINUATION_R15_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[ref17]: ../references/17_STEIN_KERNEL_PREPARATION_IDENTITY_SCOPE_20261029.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a16]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[a17]: ../../../../avoid/17_parallel_writers_and_broken_registries.md
