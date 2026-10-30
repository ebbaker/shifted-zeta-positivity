# R11: admissible primitive production tests with all derivative and trace costs

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), effort ultra**,
Investigation05 **chat0033**. Parent research return with three same-model contributing derivations
and checks; internal LLM assessment, not specialist review.

**Status: proved in-note within the inherited prepared solution class.**
The actual terminal tests for the selected production term are admissible.
Unit Gaussian preparation pays their first two spatial derivatives and
initial sphere traces using the existing residual norm. With the accepted
uniform feedback bound, these payments are uniform in auxiliary time.
There is no derivative-loss obstruction in this setting. The result does
not give a favorable sign or a primitive advantage over an equally
informed direct method. The complete joint primitive formula reconstructs
exactly the same prepared source.

The fixed physical mark is (T,A)=(1/4,2); the complete theta source,
actual jets, common feedback path, cutoff and full inner ball are unchanged.
The declared consumer is the full weighted-energy and unit-interval
integrated-dissipation bound specified in the R11 progress intake and
proved by the direct method in [Note76][n76]. This
note supplies its primitive-test comparison, not a new collision criterion.
The relevant safeguards are [result index][results], [control register][controls],
[pattern index][avoid], [separate bounds][a12] and [quantitative utility][a20].

## 1. The actual terminal test, including every cutoff derivative

Use the manuscript's fixed cutoff, here denoted zeta to distinguish it
from the terminal test eta. Put
\[
 h(r)=\zeta(r)\log r,\quad \lambda(r)=1+(1+r^2)^{-1},\quad
 b=hX,\quad v=\lambda X,\quad d=3\lambda+r\lambda',
\]
\[
 c=-hr\ell_T',\quad
 \sigma=r(h\lambda'-\lambda h'),\quad
 \beta=\sigma X,\quad
 \gamma=hrd'-\lambda rc'.                                      \tag{1}
\]
Thus the complete first-order commutator is C1=beta dot grad+gamma.
For explicit expansion,
\[
 h'=\zeta'\log r+\zeta/r,
\quad c'=-(h'r+h)\ell_T'-hr\ell_T'',
\]
\[
 \gamma=hrd'+\lambda r\{(h'r+h)\ell_T'+hr\ell_T''\}.             \tag{2}
\]
No cutoff term has been discarded. The cutoff-supported coefficients
h,b,c,sigma,beta,gamma vanish near the origin and are smooth across the
cutoff transition; v and d retain their original values there.

Write Z=omega R, omega=(1+r²)^(-2). Componentwise,
\[
 \eta_j=2C_1^*(\omega Z_j)
       =-2\operatorname{div}(\omega\beta Z_j)+2\omega\gamma Z_j.
                                                                    \tag{3}
\]
For radial Z this is exactly
\[
 \boxed{\eta_j=2\omega\left[-\sigma r\partial_r Z_j+
 \left(\gamma-3\sigma-r\sigma'
             +\frac{4\sigma r^2}{1+r^2}\right)Z_j\right].}       \tag{4}
\]
In particular sigma' includes zeta''. This is not a truncated exterior
formula. At r=1, full reflection gives ell_T'(1)=-3; hence
sigma=-3/2, sigma'=0, gamma=-9/2, and
\[
 \eta_j(1)=+\tfrac34\partial_rZ_j(1)-\tfrac32Z_j(1).             \tag{5}
\]
There is no automatic vanishing terminal trace. This terminal trace is
also not the initial-support trace of the transported/prepared test.

Let B1=sup omega|beta| and B0=sup omega|gamma| be the existing weighted
coefficients. Equation (3), viewed distributionally, gives for any H1
scalar test f
\[
 |\langle\eta_j,f\rangle|
 \le2\|Z_j\|_2(B_1\|\nabla f\|_2+B_0\|f\|_2).                \tag{6}
\]
Thus eta is already controlled as an H^-1 functional by the existing Y
budget. One need not bound the derivative of Z appearing in (4).

## 2. Unit preparation pays the derivative transfer

Fix the actual alpha path on a regular compact interval. The forward
propagator P_(s,0) solves f_s=Delta f+alpha div(vf); its adjoint is generated
by Delta-alpha v dot grad. For the actual production pairing,
\[
 \chi_{s,j}=K_1*P_{s,0}^*\eta_j.
\]
For x in R³, a unit vector e, and k=0,1,2, define
\[
 f_{k,x,e}(s,y)=P_{s,0}[D_{x,e}^kK_1(x-\cdot)](y).
\]
Duality and (6) give
\[
 |D_e^k\chi_{s,j}(x)|
 \le2\sqrt{Y_j(s)}
       \{B_1\|\nabla f_{k,x,e}(s)\|_2+B_0\|f_{k,x,e}(s)\|_2\},
 \qquad Y_j=\|Z_j\|_2^2.                                      \tag{7}
\]
This moves derivatives to a known Gaussian **before** forward propagation.
It requires no commutation between P and derivatives, no mark derivative
of alpha, and no additional derivative of Z. It works at s=0 as well as
at positive auxiliary time because K1 is fixed unit preparation.

Here are complete seed budgets. Let C_G=(8 pi)^(-3/2), and write
E_k=||D_e^kK1||2², G_k=||grad D_e^kK1||2². Rotation and translation do
not affect these quantities. Direct Gaussian integration yields
\[
\begin{array}{c|ccc}
 k&0&1&2\\ \hline
 E_k/C_G&1&1/4&3/16\\
 G_k/C_G&3/4&5/16&21/64.
\end{array}                                                     \tag{8}
\]
For verification, the Fourier transform of K1 is exp(-|xi|²), and
under the normalized exp(-2|xi|²) Gaussian each coordinate has variance
1/4. Thus E_k/C_G=(2k-1)!!/4^k and G_k/E_k=(2k+3)/4.
The L1 budgets are
\[
 \|K_1\|_1=1,\quad \|D_eK_1\|_1=1/\sqrt\pi<1,
 \quad \|D_e^2K_1\|_1\le1.                                   \tag{9}
\]
The last inequality follows directly from
D_e²K1=((x dot e)²/4-1/2)K1 and the variance 2 of the K1 Gaussian.
It suffices here; no approximate numerical constants are used.

### Finite-path allowance without a physical mass premise

For a generic scalar forward solution set E=||f||2² and G=||grad f||2².
The inherited drift bounds d<=6, Dv<=2I and |Delta d|<=30 give
\[
 E'\le6\alpha E,\qquad G'\le10\alpha G+30\alpha E.
\]
Writing B=integral_0^s alpha, therefore
\[
 E(s)\le e^{6B}E_k,
\quad G(s)\le e^{10B}\{G_k+\tfrac{15}{2}(1-e^{-4B})E_k\}.       \tag{10}
\]
Equations (7)–(10) control all three required test derivatives uniformly
in x on every compact regular lifespan interval. This version imports no
positive physical mass margin; its constants depend on B(s).

### Uniform allowance when the accepted feedback theorem applies

Suppose 0<=alpha(s)<=a_bar, where a_bar=2 K_infinity/3 is supplied by
[Note67][n67] and its assessment at this same mark. Define
\[
 c_N=\frac35(6\pi^2)^{2/3},\qquad
 E_* =\max\{C_G,(3\bar\alpha/c_N)^{3/2}\},
\]
\[
 r_* =\frac{5\bar\alpha+
                   \sqrt{25\bar\alpha^2+60\bar\alpha}}2,
 \qquad G_*=E_*\max\{3/4,r_*\}.                                \tag{11}
\]
Then, for every seed in (8)–(9),
\[
 \|f_{k,x,e}(s)\|_2^2\le E_*,\qquad
 \|\nabla f_{k,x,e}(s)\|_2^2\le G_*                            \tag{12}
\]
uniformly in s,x,e,k.

Here is a self-contained derivation. Positivity and conservation of P
imply L1 contraction, so ||f(s)||1<=1, including signed derivative seeds.
With Fourier convention Plancherel=(2pi)^(-3) integral |fhat|², for every
R>0,
\[
 R^2E-G\le(2\pi)^{-3}\|f\|_1^2
                   \int_{|\xi|<R}(R^2-|\xi|^2)d\xi
          =\frac{R^5}{15\pi^2}\|f\|_1^2.
\]
Optimize R³=6 pi² E/||f||1² to obtain
G>=c_N E^(5/3)/||f||1^(4/3). Consequently
E'<=-2 c_N E^(5/3)+6 a_bar E. The upper barrier in (11) proves E<=E_*.
The exact gradient identity and ||Delta f||2²>=G²/E then give
\[
 G'\le-2G^2/E_*+10\bar\alpha G+30\bar\alpha E_*.
\]
The positive root after dividing by E_* is r_*; (8) gives the other
barrier 3E_*/4. This proves (12) without a new source or unknown-solution
constant. For alpha_bar=0, the same formulas and barriers remain valid.

Set
\[
 D_*=2(B_1\sqrt{G_*}+B_0\sqrt{E_*}).                            \tag{13}
\]
Then for radial chi, including r=1,
\[
 \boxed{\max_{k=0,1,2}\|\partial_r^k\chi_{s,j}\|_\infty
                 \le D_*\sqrt{Y_j(s)}.}                        \tag{14}
\]
The bound controls the primitive test relative to Y; it does not assume
Y is already uniform. It imports precisely the physical information used
to acquire alpha_bar, and cannot be used to prove that premise itself.

## 3. Primitive admissibility and a paid absolute allowance

Let r=exp(2u), c_j(u)=exp(Tu²)u^j cos^(j)(Au), j=0,1, and
psi_theta(u)=exp(u)A_theta(exp(2u)). The joint derivative is exactly
\[
 (\partial_u^2-1)[c_j\chi(r)]
 =q_{j,0}\chi(r)+q_{j,1}\chi_r(r)+q_{j,2}\chi_{rr}(r),
\]
\[
 (q_{j,0},q_{j,1},q_{j,2})
   =(c_j''-c_j,\ 4r(c_j'+c_j),\ 4r^2c_j).                     \tag{15}
\]
The 4r c_j term in q_(j,1) is the derivative of 2r in the second
u derivative; omitting it changes the operator.

Equations (10) or (14), multiplied by the fixed exp(Tu²) polynomial
factors and r², are dominated by the complete theta tail. In particular
psi f', psi' f vanish at infinity and the bulk integral converges
absolutely. The actual tests satisfy the primitive lemma. The only
boundary contribution is
\[
 \mathcal B_0=\chi_{s,0}(1)/16+A_\theta(1)\chi_{s,0}'(1)/4;
 \qquad \mathcal B_1=0.                                       \tag{16}
\]
Both terms are paid by (14). They are not removed by the evolving
sphere cancellation R(1)=-T(1).

For a concrete finite constant, put
\[
 L_j=\mathbf1_{j=0}\sqrt2
       \sqrt{(1/16)^2+(A_\theta(1)/4)^2}
       +\frac{\sqrt3}{8}\int_0^\infty\psi_\theta(u)|q_j(u)|_2\,du.
                                                                    \tag{17}
\]
Then the componentwise primitive formula and Euclidean Cauchy–Schwarz
give the fully paid allowance
\[
 \boxed{|I_1(s)|\le D_*\sqrt{L_0^2+L_1^2}\sqrt{Y(s)}.}          \tag{18}
\]
This bounds the three derivative coefficients jointly at each u; it is
still an absolute estimate and asserts no signed improvement. Equation
(18) enters production multiplied by alpha, so for any epsilon>0 its
contribution is at most epsilon Y+
alpha_bar² D_*²(L0²+L1²)/(4 epsilon). It does not erase C0, J2, diffusion
or any inner-region term. The simpler direct allowance remains
\[
 |I_1|\le2\sqrt Y(B_1\sqrt G+B_0\sqrt{E_0})
 \le2\sqrt{E_0Y}(B_1\sqrt{K_\infty}+B_0).                     \tag{19}
\]
No strict ranking of (18) against (19), and no improved complete energy
allowance from (18), has been established. The prior signed exterior
completion is also available to the direct comparator.

## 4. Retaining the whole joint expression reconstructs the same source

There is a useful exact formulation before taking any absolute values.
Define the spherical Gaussian seed
\[
 k_r(y)=\frac1{4\pi}\int_{S^2}K_1(y-r\theta)\,d\theta,
\quad
 g_{j,u}=(c_j''-c_j)k_r
        +4r(c_j'+c_j)\partial_rk_r+4r^2c_j\partial_r^2k_r.
                                                                    \tag{20}
\]
Then in L1 intersect H1,
\[
 \boxed{K_1*F_j^{\rm raw}
 =\mathbf1_{j=0}\left\{\frac{k_1}{16}
                    +\frac{A_\theta(1)}4\partial_rk_r\big|_{r=1}\right\}
       +\frac18\int_0^\infty\psi_\theta(u)g_{j,u}\,du.}          \tag{21}
\]
To verify it, polar integration first gives
K1*F_j=integral_0^infinity Phi(u)c_j(u)k_(exp(2u)) du.
Apply the two integrations by parts to this Banach-valued test.
Spherical averaging of translated directional Gaussian derivatives and
Minkowski give uniform L1 and H1 bounds for k_r and its first two r
derivatives from (8)–(9), with third Gaussian derivatives only in the
known H1 seed budget. The theta tail dominates the r² factors in (20),
so the Bochner integral and both integrations by parts are valid. The
same facts justify approximation by compact u intervals. The endpoint
terms are exactly (21), with both j=1 endpoints zero.

Apply P_(s,0), then omega C1, and pair with 2Z_j. The result is precisely
the corresponding component of I1, retaining all derivatives and both
initial sphere contributions. Applying a norm estimate to the **entire**
right side of (21) is therefore applying it to the actual prepared source
on the left. The direct method has that same source and may use (21).
This identifies a comparison requirement, not a no-go theorem: a useful
signed advantage would have to exploit actual source–residual–path
correlation beyond the norm data used in (6), (14) and (19).

For clarity about scope, if Z_j were permitted to vary freely in an L2
sphere independently of W and its jets, the sharp upper and lower
pairings with fixed omega C1 W_j would be ±2 sqrt(Y_j)||omega C1 W_j||2.
The primitive representation leaves this elementary relaxed optimization
unchanged. The actual residual is constrained by its definition and
trajectory, so this observation does not prove an obstruction for actual
theta solutions or exclude a future correlated estimate.

## 5. A scoped sign test for the residual coefficient geometry

The primitive test has no established fixed sign. This can be made
precise for a larger class without pretending it is the actual theta
trajectory. On r>=3/4 the cutoff is one. Write
\[
 a_b=r\log r,\qquad
 a_1=r(r\lambda'\log r-\lambda),\qquad
 C_1=a_1\partial_r+\gamma.
\]
For arbitrary smooth radial triples W=(U,0), J2=0, define the actual
algebraic residual R=A_TW−(2V,V+2J2). Then
\[
 I_1=8\pi\int_0^\infty r^2\omega^2
             (a_bU'+cU)(a_1U'+\gamma U)\,dr.                 \tag{22}
\]
On r>1, a_b>0 and a_1<0. On 3/4<r<1, a_b<0 and a_1<0 as well:
\(r\lambda'\log r\le\tfrac12\log(4/3)<1/6\), whereas
\(\lambda\ge3/2\). The principal coefficient a_b a_1 therefore has
opposite signs on these two regions.

Choose nonzero smooth phi supported in a compact annulus inside either
region and U_n(r)=phi(r)sin(nr). Terms with at most one derivative are
O(n), while the leading squared derivative has the limit
\[
 \lim_{n\to\infty}\frac{I_1[U_n]}{n^2}
 =4\pi\int r^2\omega^2a_ba_1\phi^2\,dr.                   \tag{23}
\]
To justify the averaging, write cos²(nr)=(1+cos(2nr))/2 and integrate
the compact smooth oscillatory term once by parts. The limit is positive
on the inner annulus and negative on an exterior annulus. Thus the
coefficient geometry and residual definition alone do not make I1
semidefinite. This calculation retains the whole inner ball.

**Scope:** these triples are not simultaneously generated by the fixed
theta source, literal cosine jets and unit preparation. They are not
collision controls or counterexamples along the actual theta path.
Equation (23) only screens a geometry-only sign argument. Actual
source/path correlations remain outside this scoped observation.

The endpoint version of the joint integrand also shows the correlations
that a theta-path estimate would have to retain. At the fixed mark,
\[
 (f_0''-f_0)(0)=-\tfrac92\chi_0(1)
                   +4\chi_{0,r}(1)+4\chi_{0,rr}(1),
 \qquad (f_1''-f_1)(0)=-4\chi_1(1).                          \tag{24}
\]
These are identities, not sign claims. Positivity of the primitive or of
the common propagator supplies no sign for an input eta of unknown sign.
The completion term (16) is a signed functional of propagated traces,
not a positive scalar constant. The exact evolving cancellation
R(s,1)=−T(s,1) does not set those nonlocal traces to zero.

## 6. Controls and continuation meaning

Finite-path admissibility is generic for the stated weighted coefficients
and unit-prepared class. The positive Gaussian-polynomial control has a
positive normalized primitive and the same transfer identity, but lacks
the unchanged theta sum. The polynomial observation control keeps that
sum and the transfer but lacks literal cosine. Weighted-square, reflected,
Euler-factor and finite-prime controls retain the distinctions in the
[control register][controls]; none is rejected merely by this test-domain
argument. Uniformity additionally requires the admitted uniform-alpha
premise. At an admitted zero-mass collision that premise is unavailable
on the full horizon, so (14) is not an exclusion without new information.
A low-mark bound need not reject another frequency's event.

The useful completed obligation is the explicit derivative/trace payment.
The remaining issue for a primitive advantage is signed correlation or a
strict quantitative cost improvement after full production is compared.
If the equally informed direct argument already pays the declared uniform
consumer, R11's stop rule applies: record that completed consumer and do
not manufacture another one merely to retain a primitive claim.

[n67]: 67_UNIFORM_FEEDBACK_DIRECT_COMPARISON_B02_R10_20261029.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md

[n76]: 76_UNIFORM_RESIDUAL_AND_FIXED_JET_CLOSURE_R11_20261029.md
