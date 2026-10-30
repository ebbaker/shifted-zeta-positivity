# Uniform residual energy and every fixed common-path jet

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
ultra**, Investigation05 **chat0033**, *Investigate radial theta collision
geometry*. Parent synthesis with three same-model contributing derivations
and checks; no independent specialist review.

**Status: proved in-note within the inherited prepared radial solution
class, using the accepted R10 theorem and full production identities.**
The declared R11 consumer is paid: the full weighted residual energy is
uniformly bounded in auxiliary time, and its complete dissipation is
bounded on every fixed-length sliding interval. Every fixed common-path
spectral jet also has a uniform L2 bound. The direct method supplies these
results; no primitive-specific advantage or larger physical domain is
established.

The [primitive analysis][n75] separately pays every transported-test
derivative and sphere trace. Together these notes complete the bounded
comparison in [Note74][n74]. The [internal review][review] records the
proof checks and their shared premises; a fixed [E08 R11 packet][packet]
is ready for assessment. [Progress05][progress] remains the sole live
register.

## 1. Fixed inputs and the declared consumer

Use precisely the complete theta source, unit Gaussian preparation,
physical mark (T,A)=(1/4,2), original feedback and common-path jets. Put
\[
 q(u)=e^{u^2/4}\Phi(u),\qquad M_j=\int_0^\infty u^jq(u)\,du,
 \qquad M=M_0+M_2.
\]
The preserved spatial energy is E0=||W(s)||2², not the norm of a time
derivative. All spatial integrals are over R³. With the source operator
and cutoff fixed as in [Note40][n40],
\[
 W=(U,V),\quad \mathcal T=(2V,V+2J_2),\quad
 Z=\omega\mathcal R=\omega(b\cdot\nabla W+cW-\mathcal T),
 \qquad \omega=(1+r^2)^{-2},
\]
\[
 G=\|\nabla W\|_2^2,\quad Y=\|Z\|_2^2,\quad Q_2=\|J_2\|_2^2,
 \quad \mathcal F=G+Y+Q_2.
 \tag{1}
\]
J2 is the actual running second frequency derivative along the fixed
feedback path. In particular it is not replaced by −u(X)²U after
preparation. No physical parameter derivative of alpha is introduced.

[Note67][n67] and [Review36][r36] supply global existence and a paid
constant K, chosen as K_infinity or its analytical bound K_theta:
\[
 G(s)\le KE_0,\qquad 0\le\alpha(s)\le\bar\alpha:=2K/3
 \quad(s\ge0).
 \tag{2}
\]
The positive physical mass margin used to obtain K remains an upstream
premise. It is not proved anew by the residual argument. The same source
payment gives
\[
 e_+=(8\pi)^{-3/2},\qquad
 e_-=c_3^{3/2}(70/73)^{7/2}(26/3)^{-3/2},\qquad
 c_3=\frac37\left(\frac{15}{14\pi}\right)^{2/3},
\]
\[
 E_0\ge e_-M^2,\qquad \frac{M_2}{M}<\frac1{73},\qquad
 \alpha(s)\ge a_*:=\frac15
       \left(\frac{6\pi^2E_0}{M^2}\right)^{2/3}>0.
 \tag{3}
\]
The conversion M2/M<1/73 follows from the assessed M2/M0<1/72.
All moments Mj are finite by the complete theta tail.

For dissipation use the strongest existing full production theorem,
including [Note47][n47]'s signed exterior improvement:
\[
 \mathcal F'+\mathscr D_{\rm R}+\alpha\mathscr H_{\rm rad}
 \le(\kappa_0+\kappa_1\alpha)(\mathcal F+E_0),
 \tag{4}
\]
\[
 \mathscr D_{\rm R}=N+2\|\nabla Z\|_2^2+2\|\nabla J_2\|_2^2,\quad
 N=\|\Delta W\|_2^2,\quad \mathscr H_{\rm rad}\ge0,
\]
\[
 \kappa_0=8+A_2^2+A_1+A_0,\qquad
 \kappa_1=274/25+B_1+B_0.
\]
This keeps the full C0/C1 commutators, all cutoff derivatives, one complete
N payment, the true preparation residual, the second jet and the entire
inner ball. The new size estimate will be inserted into this complete
inequality, rather than inferred from one improved term.

Under [avoid/01][a01], the consumer is a quantitative supporting estimate,
not an RH-equivalent noncollision criterion. The comparison uses the same
source, physical mass information, preparation, path and coefficient
budgets on both sides.

## 2. A uniform L2 bound for each fixed common-path jet

For any fixed nonnegative integer j, set
\[
 F_j^{\rm raw}
 =\mathbf1_{r\ge1}\frac{q(u)}{8\pi r^3}u^j\cos^{(j)}(2u),
 \qquad J_j(s)=P_{s,0}K_1F_j^{\rm raw}.
\]
Positivity and mass conservation of the scalar propagator imply
|Pf|<=P|f| and L1 contraction. Unit Gaussian preparation has the same
property. Since the radial measure is q(u)du,
\[
 \|J_j(s)\|_1\le\|F_j^{\rm raw}\|_1\le M_j.
 \tag{5}
\]
This holds for the signed cosine derivatives as well as the positive
carrier. Each jet solves its own scalar equation along the same fixed
path; no coupled hierarchy or new feedback is required.

For completeness derive the sufficient Fourier/Nash constant. For a
Schwartz scalar f with ||f||1<=m, write E=||f||2² and
Gf=||grad f||2². With unnormalized forward Fourier transform, Parseval
has factor (2pi)^(-3). For k>0,
\[
 k^2E-G_f
 \le(2\pi)^{-3}m^2\int_{|\xi|<k}(k^2-|\xi|^2)\,d\xi
 =\frac{m^2k^5}{15\pi^2}.
\]
Maximization at k³=6pi²E/m² gives
\[
 G_f\ge c_N E^{5/3}m^{-4/3},\qquad
 c_N=\frac35(6\pi^2)^{2/3}.
 \tag{6}
\]
The zero function is handled separately. This is not a claim of the
optimal Nash constant. The Fourier normalization is also recorded in
the existing [classical-input annotation][refs].

Let Qj=||Jj||2². The exact scalar energy identity and d=div(v)<=6 give
\[
 Q_j'=-2\|\nabla J_j\|_2^2+\alpha\int d|J_j|^2
 \le-2c_N M_j^{-4/3}Q_j^{5/3}+6\bar\alpha Q_j.
 \tag{7}
\]
The right side is nonpositive when
Qj>=Mj²(3 alpha_bar/cN)^(3/2). Gaussian Young gives
Qj(0)<=e+ Mj². Scalar comparison therefore proves
\[
 \boxed{\mathcal D(K):=\max\{e_+,(2K/c_N)^{3/2}\},\qquad
        Q_j(s)\le M_j^2\mathcal D(K)\quad(s\ge0).}
 \tag{8}
\]
This is uniform in auxiliary time **for each fixed j**, with a different
moment budget for each order. It asserts no bound uniform in j, no
simultaneous analytic norm and no uniformity across physical parameters.

In particular either of the following is a paid normalized second-jet
allowance:
\[
 \mathfrak q=\frac{M_2^2}{E_0}\mathcal D(K)
 \quad\hbox{or}\quad
 \mathfrak q_\theta=\frac{\mathcal D(K)}{73^2e_-},
 \qquad Q_2/E_0\le\mathfrak q\le\mathfrak q_\theta.
 \tag{9}
\]
If the actual initial Qj(0) is already available, e+ in (8) can instead
be replaced by Qj(0)/Mj². No acquisition is needed for the displayed
analytical bound.

## 3. The defining residual identity closes its size

First, without estimating residual evolution,
\[
 \sqrt Y\le C_b\sqrt G+C_c\sqrt{E_0}
                       +\|\omega\mathcal T\|_2,\qquad
 C_b=\|\omega b\|_\infty,\quad C_c=\|\omega c\|_\infty.
\]
Use the exact relation vector, splitting
T=(2V,V)+(0,2J2), and omega<=1:
\[
 \|\omega\mathcal T\|_2\le\sqrt5\sqrt{E_0}+2\sqrt{Q_2}.
 \tag{10}
\]
The true nonzero residual appears on the left. Its initial commutator
defect is never removed. This estimate does not split the singular
quotients in the exterior gradient representation.

Both apparent new coefficient costs are already paid by the existing
budgets. The fixed cutoff obeys 0<=eta<=1 and vanishes for r<=1/2.
For r>=1, log r<=r gives omega|b|<=r²/(1+r²)²<=1/4.
For 1/2<=r<=1, use log2<3/4 and
max r/(1+r²)²=9/(16sqrt3)<1/3. Hence
\[
 C_b\le1/4.
 \tag{11}
\]

To control Cc without acquiring another supremum, use
\[
 \lambda=1+(1+r^2)^{-1},\quad
 d=3+\frac{3+r^2}{(1+r^2)^2},\quad
 d'=-\frac{2r(5+r^2)}{(1+r^2)^3},
\]
\[
 \gamma=b\cdot\nabla d-v\cdot\nabla c,\quad
 |\gamma|\le B_0(1+r^2)^2,\quad
 c'=\frac{\eta\log r\,d'}{\lambda}
                  -\frac{\gamma}{\lambda r},\qquad c(1)=0.
 \tag{12}
\]
All cutoff derivatives are contained in this full gamma and B0.
Integrating from r=1, on 1/2<=r<=1 the B0 contribution to omega|c|
is at most 4B0 log2<3B0, while the source contribution is at most
\[
 \log2\{d(1/2)-d(1)\}=\frac{27}{25}\log2<\frac34.
\]
For an exact elementary check, the series
log2=2 sum_(k>=0) 3^(-2k-1)/(2k+1) is strictly less than
2/3+1/36=25/36, by bounding all denominators with k>=1 by 3.

On r>=1 the B0 contribution is bounded by
\[
 B_0\,\frac{\log r+(r^2-1)+(r^4-1)/4}{(1+r^2)^2}
 \le\frac58 B_0.
\]
Here log r<=r²/2, r²/(1+r²)²<=1/4 and r4/(1+r²)²<=1 suffice.
The remaining contribution is at most
\[
 \frac14\int_1^\infty\log t\,(-d'(t))\,dt
 =\frac{3\log2-1}{8}<\frac34.
\]
Integration by parts and q=t² give
int_1^infinity (d(t)-3)/t dt=(3log2-1)/2, which verifies the last
integral. Below r=1/2, c=0. Thus the global bound is
\[
 \boxed{C_c\le3B_0+3/4.}
 \tag{13}
\]
No new coefficient acquisition or theta truncation has entered.

Choose q as either allowance in (9), and define
\[
 \mathfrak y=
 \left[\frac{\sqrt K}{4}+3B_0+\frac34+\sqrt5+2\sqrt q\right]^2,
 \qquad
 \mathcal F_*:=E_0(K+\mathfrak y+q).
 \tag{14}
\]
Equations (2), (8), and (10)–(13) prove the requested whole-energy bound:
\[
 \boxed{Y(s)\le E_0\mathfrak y,\qquad
             \mathcal F(s)\le\mathcal F_*\quad(s\ge0).}
 \tag{15}
\]
Every constant is determined by paid initial/source information. The
entire inner ball is retained, and R(s,1)=−T(s,1) still supplies its
exact combined cancellation. No evolving sphere boundary condition
is imposed. At fixed ball radius Rb, the same result also gives
||R(s)||_(L2(B_Rb))²<=(1+Rb²)^4 E0 y; it is not an unweighted global
residual bound.

## 4. The full production pays every fixed-length dissipation window

Set C*=kappa0+(2K/3)kappa1. Insert (15) into (4) and integrate:
\[
 \boxed{\int_t^{t+\ell}
      (\mathscr D_{\rm R}+\alpha\mathscr H_{\rm rad})\,ds
 \le\mathcal F_*+C_*(\mathcal F_*+E_0)\ell}
 \quad(t\ge0,\ \ell>0).
 \tag{16}
\]
Indeed the sharper first line is
F(t)−F(t+ell)+C*(F_*+E0)ell, and F(t+ell)>=0. In particular ell=1
pays the declared uniform unit-window consumer. Starting at zero gives
\[
 \mathcal F(S)+\int_0^S
       (\mathscr D_{\rm R}+\alpha\mathscr H_{\rm rad})\,ds
 \le\mathcal F(0)+C_*(\mathcal F_*+E_0)S.
 \tag{17}
\]
This cumulative allowance grows linearly. Finite total dissipation over
the half-line, pointwise uniform dissipation, convergence and a limiting
profile are not claimed. The retained terms include C0's diffusion
absorption, the full C1 payment and the radial remainder. No term in the
complete production is silently omitted.

## 5. Quantitative comparison and the R11 stopping boundary

Combine the new bound with the inherited allowance, using
Xi(s)=kappa0 s+kappa1 B(s):
\[
 \boxed{\mathcal F(s)\le
   \min\{(\mathcal F(0)+E_0)e^{\Xi(s)}-E_0,\ \mathcal F_*\}.}
 \tag{18}
\]
Because alpha>=a_*, Xi(s)>=(kappa0+kappa1 a_*)s. Also F_*>=F(0)
by its construction. Therefore the new allowance is strictly smaller
than the old displayed envelope for
\[
 s>s_c:=
 \frac{\log[(\mathcal F_*+E_0)/(\mathcal F(0)+E_0)]}
      {\kappa_0+\kappa_1a_*}.
 \tag{19}
\]
This is a finite, nonnegative crossover between sufficient allowances,
not a numerical constant ranking, actual energy ratio or assertion of
actual energy growth. It improves the earlier residual envelope even
after that envelope receives the accepted uniform feedback bound.

The same direct method supplies every step. Thus **the declared uniform
consumer is complete without a primitive-specific gain**. This is
Note74's stopping condition. The primitive test in Note75 is now
uniformly controlled as well, since its bound uses sqrt(Y), but it
does not reacquire the physical margin spent in K. Parent B02 remains
partial; no second mechanism or parameter campaign is started here.

## 6. Collision controls and exact dependencies

The L1/diffusion and defining-residual argument is generic once a bounded
common feedback path is supplied. Complete theta and literal cosine
pay the physical margin upstream and define the fixed source coefficient
B0. If that comparison operator is used on another field, (10) still
bounds its actual residual, including any raw mismatch.

| Control or comparison class | Premise and scope |
| --- | --- |
| Gaussian-polynomial and normalized positive-primitive controls | They share elementary diffusion estimates and the primitive identity. At an admitted double event, m=0 fails the positive mass floor used to supply R10's K. Primitive positivity does not repair this. |
| Positive weighted-square sources | They can share the sufficient low-mark moment payment. Known collisions at other frequencies do not contradict a bound at A=2; at an actual event the positive mass premise fails. Unit coefficients/full reflection are not premises of the generic Nash lemma. |
| Fixed-theta variable-kernel controls of Note51 | They can have m=0 at this mark. They fail literal cosine in the mass-margin payment, so the theta K cannot be imported into their feedback path. |
| Finite-prime, reflected, shape and RH-conditional endpoint controls | Keep their recorded domains. At any admitted double event the positive mass premise fails. No new source ratios or event locations were evaluated. |
| Euler-factor Laguerre witnesses | Such a witness is not automatically a double event. Apply the generic lemma only when its actual path hypotheses hold; do not manufacture a zero-mass statement. |
| Atomic/profile controls | Inherited smooth-source assumptions must be checked before admission. Prepared or continuous versions still need the actual path and mass-margin hypotheses. |

For a colliding control, alpha can be bounded on any compact interval
inside its lifespan. The resulting constants then depend on that
interval and give no contradiction. Nothing here supplies uniform
feedback at zero physical mass or beyond an unproved regularity horizon.

The [result index][results], [control register][controls] and
[pattern index][avoid], especially [scoped exclusions][a07],
[separate bounds][a12] and [quantitative utility][a20], govern this
interpretation. The result is a useful complete energy estimate in the
already covered low-mark regime, not evidence for an RH conclusion.
No literature-priority claim or specialist review is made.

[n75]: 75_PRIMITIVE_TEST_COSTS_AND_SIGNED_COMPARISON_R11_20261029.md
[n74]: 74_PRIMITIVE_PRODUCTION_ANALYSIS_AND_MODEL_CONTINUATION_20261029.md
[n40]: 40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n47]: 47_EXTERIOR_SOURCE_RESIDUAL_COUPLING_B02_R5_20261029.md
[n67]: 67_UNIFORM_FEEDBACK_DIRECT_COMPARISON_B02_R10_20261029.md
[r36]: ../reviews/36_UNIFORM_FEEDBACK_E08_R10_ASSESSMENT_20261029.md
[review]: ../reviews/39_PRIMITIVE_TEST_AND_UNIFORM_CLOSURE_INTERNAL_REVIEW_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_PRIMITIVE_TEST_AND_UNIFORM_CLOSURE_R11_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[refs]: ../references/11_CONSERVATIVE_FEEDBACK_AND_DIFFUSION_CONTRACTION_20261028.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
