# CTF-B02 R5: exterior source/residual coupling

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 **chat0023**, **Continue CTF-B02 coupled estimate**.

**Return — proved in-note, with same-assistant checks.** The one candidate
recorded in [Progress05][progress] holds. For the unchanged complete theta
operator, retain its signed multiplication term together with the actual
residual on r>=2. This lowers the compact compression coefficient by
exactly 49/600:
\[
 \boxed{\kappa_{1,\mathrm{src}}=\frac{274}{25}+B_1+B_0
       =\kappa_{1,\mathrm{rad}}-\frac{49}{600}.}
 \tag{1}
\]
The full theta series proves the source slope bound used below, including
every term of its differentiated tail. Actual second-jet costs and the
whole inner region are paid. This is an estimate using the **fixed theta
operator's coefficients**, not a separator of theta's trajectory from a
colliding control. No independent deadline bound for compression follows.

| Next task | Type and recommended model | Readiness and bounded output |
| --- | --- | --- |
| **CTF-E08 R5 — default** | **E — Sol:** assess one complete proof and integrate only supported conclusions | Ready; [frozen packet][packet], [continuation48][next] |
| CTF-B02 | B — Astra: trajectory-sensitive information remains a conceptual problem | Parent partial; another candidate is not selected here |
| CTF-E03 / CTF-B03 | E — Sol / B — Astra | Gated; no numerical acquisition or coverage extension is needed for (1) |

## 1. Frozen candidate, classification and domain

The R5 intake fixes P=[0,1/2] x [1,6], the existing functional, the split
r=2, the proposed slope bounds 2<=k<=6, and the numerical comparison
49/600 before verification. This note completes that candidate without
changing the radius, weight, cutoff, feedback, source or observation.

Use [Notes31][n31], [40][n40], [42][n42], [44][n44] and [46][n46].
Write the fixed physical mark as p=(T,A), reserving auxiliary time s:
\[
 W=(U,V),\quad J=J_2,\quad \Theta=(AV,V+AJ),\quad
 \mathcal R=\mathcal A_TW-\Theta,\quad Z=\omega\mathcal R,
 \qquad \omega=(1+r^2)^{-2}.
\]
Here J is the actual second running-frequency derivative of the common
propagator with its mark fixed. It solves J_s=L_sJ; it is not -u^2U.
Keep the complete reflected source and the fixed exponential cutoff
\[
 \mathcal A_T=b\cdot\nabla+c_T,\quad
 b=\eta(r)\log r\,X,\quad c_T=-\eta(r)r\log r\,\ell_T'(r),
 \quad\ell_T=\log\rho_T,\quad \eta=h(4r-2).
\]
All integrations remain over R^3 unless explicitly restricted. Set
\[
 E_0=\|W\|_2^2>0,\quad G=\|\nabla W\|_2^2,\quad
 Y=\|Z\|_2^2,\quad Q=\|J\|_2^2,\quad
 \mathcal F=G+Y+Q,\quad N=\|\Delta W\|_2^2.
\]
The generator, feedback and drift are unchanged:
\[
 L_s=\Delta+\alpha(v\cdot\nabla+d),\quad
 v=\lambda X,\quad \lambda=1+(1+r^2)^{-1},\quad
 d=\operatorname{div}v,\quad \alpha=2G/\!\int d|W|^2\ge0.
\]
Use the inherited prepared radial smooth/Schwartz solution on every
compact subinterval of its lifespan. The complete theta tail and unit
preparation supply that class as in Note40; its continuation theorem is
imported, not reproved here.

Under [target classification][a01], (1) is a quantitative intermediate
milestone, not an RH-equivalent reformulation. The [result index][results],
[avoid index][avoid], [controls][controls], [scope discipline][a07] and
[combined-bound rule][a12] govern the interpretation. The new source
input is a verified exterior logarithmic-slope interval. Its use in
the signed residual product is essential to this proof; that interval
alone is not claimed to characterize theta.

## 2. The complete source gives 2<=k<=6 on every r>=2

This section is uniform for 0<=T<=1/2. Put q=r^2>=4 and beta=3/(2pi).
The exact source factorization from Note40 is
\[
 \rho_T(r)=\frac{\pi}{4}r^{3/2}
 e^{-\pi r^2+(T/4)(\log r)^2}P(q),\qquad
 P(q)=1-\frac{\beta}{q}+\tau(q),
\]
\[
 \tau(q)=\sum_{n\ge2}\left(n^4-\frac{\beta n^2}{q}\right)
                   e^{-\pi(n^2-1)q}.
 \tag{2}
\]
The notation P(q) here uses q as its argument; Note40 uses P(r).
No term of (2) is omitted. Every summand is positive.

We first prove the deliberately loose but sufficient tail payments
\[
 0\le\tau(q)<\varepsilon,\qquad
 |q\tau_q(q)|<\varepsilon,\qquad
 |q^2\tau_{qq}(q)|<\varepsilon,\qquad \varepsilon=\frac1{100}.
 \tag{3}
\]
For one summand put x=pi(n^2-1)q>=36. Since beta<1/2, its zeroth,
q-weighted first and q^2-weighted second derivatives are bounded,
respectively, by
\[
 n^4e^{-x},\quad n^4(1+x)e^{-x},\quad
 n^4(x^2+2x+2)e^{-x}.
\]
For example the second derivative before absolute values is
\[
 \left[-\frac{2\beta n^2}{q^3}
 -\frac{2\pi(n^2-1)\beta n^2}{q^2}
 +\pi^2(n^2-1)^2\left(n^4-\frac{\beta n^2}{q}\right)\right]e^{-x}.
\]
For x>=36, all three polynomial factors are at most 2x^2, and
e^{x/2}>=x^4/384>=x^2. Each bound is therefore at most
2n^4e^{-x/2}<=2n^4e^{-6(n^2-1)}. For integer n>=2,
n^4<=16^{n-1} and n^2-1>=3+5(n-2). Summing the entire majorant gives
\[
 2\sum_{n\ge2}n^4e^{-6(n^2-1)}
 \le\frac{32e^{-18}}{1-16e^{-30}}
 <64e^{-18}<\frac1{4096}<\frac1{100}.
 \tag{4}
\]
Here e>2 suffices for both strict elementary inequalities. These
summable bounds also justify differentiation twice on q>=4.

Let p_0=1-beta/q, t=\tau/p_0 and
\[
 z(q)=\frac{2qP_q}{P}
     =z_0(q)+\frac{2qt_q}{1+t},\qquad
 z_0(q)=\frac{2\beta}{q-\beta}.
\]
We have p_0>=7/8, |qp_{0,q}|<=1/8 and
|q^2p_{0,qq}|<=1/4. The quotient rule and (3) give
\[
 |qt_q|\le\frac{64}{49}\varepsilon<\frac32\varepsilon,\qquad
 |q^2t_{qq}|\le\frac{632}{343}\varepsilon<2\varepsilon.
\]
For the second bound, the four coefficient payments are
8/7, 16/49, 16/49 and 16/343. Since t>=0,
\[
 |z-z_0|\le3\varepsilon,\qquad
 \left|2q\left(\frac{2qt_q}{1+t}\right)_q\right|
 \le14\varepsilon+9\varepsilon^2.
\]
Also z_0<=2/7 and |2qz_{0,q}|<=32/49. Thus
\[
 \boxed{|z|\le\frac27+\frac3{100}<\frac13,\qquad
 |2qz_q|\le\frac{32}{49}+\frac{14}{100}+\frac9{10000}<1.}
 \tag{5}
\]

Define the actual logarithmic source slope
\[
 L(r)=-r\ell_T'(r)
      =2\pi q-\frac32-\frac T2\log r-z(q),\qquad
 c_T(r)=(\log r)L(r)\quad(r\ge2).
 \tag{6}
\]
The elementary bounds 3<pi<4 and log r<=q yield
\[
 L\ge6q-\frac{11}{6}-\frac q4\ge5q>0.
 \tag{7}
\]
Differentiating (6) and using (5),
\[
 rL'=4\pi q-\frac T2-2qz_q\le16q+1\le\frac{65}{4}q,
\]
\[
 rL'-2L
 =3-\frac T2+T\log r+2z-2qz_q
 \ge3-\frac14-\frac23-1=\frac{13}{12}>0.
 \tag{8}
\]
Consequently 2<=rL'/L<=13/4. Also log r>=log 2>=2/3:
the latter follows by pairing 1/x and 1/(3-x) in its integral on [1,2].
Therefore
\[
 2\le\frac{rc_T'}{c_T}
      =\frac1{\log r}+\frac{rL'}L\le\frac{19}{4}.
 \tag{9}
\]

On this exterior eta=1. Define
\[
 a_b=r\log r,\qquad
 k(r,T)=\frac{v\cdot\nabla c_T-b\cdot\nabla d}{c_T}
       =\lambda\frac{rc_T'}{c_T}-\frac{rd'}L.
 \tag{10}
\]
This division is only made on r>=2, where (7) proves c_T>0.
For the fixed drift,
\[
 d=3+\frac{3+q}{(1+q)^2},\qquad
 -rd'=\frac{2q(q+5)}{(1+q)^3}\in[0,2],\qquad
 1\le\lambda\le\frac65.
\]
Equations (7), (9) and (10) now prove
\[
 \boxed{2\le k\le\frac65\frac{19}{4}+\frac1{10}
        =\frac{29}{5}<6\qquad(r\ge2).}
 \tag{11}
\]
Every radius and every square in the source has been paid. An asymptotic
for the leading mode alone would not establish this uniform result.

## 3. Keep the source term and residual together

The full commutator remains precisely Note40 (8):
\[
\begin{split}
 \mathscr C_0={}&-2(\partial_jb_i)\partial_{ij}
   -(\Delta b+2\nabla c_T)\cdot\nabla-\Delta c_T,\\
 \mathscr C_1={}&(b\cdot\nabla v-v\cdot\nabla b)\cdot\nabla
   +b\cdot\nabla d-v\cdot\nabla c_T.
\end{split}
 \tag{12}
\]
There is no mark derivative of alpha. On r>=2, radiality gives
\[
 \mathscr C_1W=a_1W'-kc_TW,\qquad
 a_1=r(r\lambda'\log r-\lambda).
\]
Using the **definition** Z=omega(a_b W'+c_TW-Theta), without setting
the residual to zero, yields
\[
 \boxed{\omega\mathscr C_1W=-kZ+
          \omega\{(a_1+ka_b)W'-k\Theta\}.}
 \tag{13}
\]
In particular, the signed source multiplication term creates -kZ,
while its price is the displayed gradient/actual-jet coupling.

Here a_1<0 and
\[
 \frac{|a_1|}{a_b}=\frac{\lambda}{\log r}-r\lambda'
 \le\frac95+\frac8{25}=\frac{53}{25}<4\le2k.
\]
It follows that |a_1+ka_b|<=ka_b. Since log r<=r/2 on r>=2,
\[
 \omega\le\frac1{25},\qquad
 \omega a_b\le\frac{q}{2(1+q)^2}\le\frac2{25}.
 \tag{14}
\]
The logarithmic inequality follows from the value and derivative of
r/2-log r at and above r=2.

Let F_c=omega((a_1+ka_b)W'-kTheta). The elementary vector inequality
2Z.F_c<=k|Z|^2+|F_c|^2/k, followed by the squared two-term bound, gives
\[
\begin{split}
 2Z\cdot\omega\mathscr C_1W
 &\le-k|Z|^2+\frac{|F_c|^2}{k}\\
 &\le-2|Z|^2+\frac{48}{625}|W'|^2
                    +\frac{12}{625}|\Theta|^2.
\end{split}
 \tag{15}
\]
All constants follow from 2<=k<=6 and (14). This is the selected
exterior coupled payment, rather than another separate B_0 norm bound.
At the physical marks A<=6 the exact jet vector satisfies
\[
 |\Theta|^2=A^2|V|^2+|V+AJ|^2
 \le(A^2+2)|V|^2+2A^2|J|^2
 \le38|W|^2+72|J|^2.
 \tag{16}
\]
Thus its costs are not omitted or replaced by a freely chosen jet.

## 4. The whole-space compact consequence

Use Note40's exact signed production:
\[
\begin{split}
 \mathcal F'={}&-2N-2\|\nabla Z\|_2^2-2\|\nabla J\|_2^2
   +2\!\int|\nabla\log\omega|^2|Z|^2
   +2\langle Z,\omega\mathscr C_0W\rangle\\
 &+\alpha\left\{\mathcal K+\int h_\omega|Z|^2+\int d|J|^2
                  +2\langle Z,\omega\mathscr C_1W\rangle\right\},
 \qquad h_\omega=11+\frac{q-5}{(1+q)^2}.
\end{split}
 \tag{17}
\]
Retain Note42's exact radial remainder:
\[
 \mathcal K=10G+\frac{21}{4}E_0-\mathscr H_{\rm rad},\qquad
 \mathscr H_{\rm rad}\ge0.
\]
The entire C_0 term is treated with the **unchanged** Note40 payments.
It consumes one unit of N, and its remaining upper allowance is
\[
 A_1G+\kappa_0Y+A_0E_0
 \le\kappa_0(\mathcal F+E_0),\qquad
 \kappa_0=8+A_2^2+A_1+A_0.
 \tag{18}
\]
Thus no second-order commutator or cutoff derivative is removed.

For r<2, keep the old pointwise first-order payment, using the same
global B_1,B_0:
\[
 2Z\cdot\omega\mathscr C_1W
 \le B_1|\nabla W|^2+(B_1+B_0)|Z|^2+B_0|W|^2.
 \tag{19}
\]
Because (h_omega)_q=(11-q)/(1+q)^3, its inner upper bound is
h_omega(4)=274/25. On r>=2 use (15)-(16), and the inherited global
h_omega<=265/24. Denote restricted energies by subscripts in/out,
for r<2 and r>=2 respectively. After retaining alpha H_rad on the
left, the complete alpha allowance has the following coefficients:

| Quantity | Inner coefficient | Exterior coefficient |
| --- | --- | --- |
| G | 10+B_1 | 10+48/625 |
| Y | 274/25+B_1+B_0 | 265/24-2=217/24 |
| Q | 6 | 6+864/625 |
| E | 21/4+B_0 | 21/4+456/625 |

These are coefficients of the restricted energies, not two copies of
their full norms. Every entry is bounded by
kappa_1,src=274/25+B_1+B_0: the exterior entries are all less than
274/25, and B_0,B_1>=0. Hence, with
\[
 \mathscr D=N+2\|\nabla Z\|_2^2+2\|\nabla J\|_2^2,
\]
we obtain
\[
 \boxed{\mathcal F'+\mathscr D+\alpha\mathscr H_{\rm rad}
 \le(\kappa_0+\kappa_{1,\rm src}\alpha)(\mathcal F+E_0).}
 \tag{20}
\]

The split at r=2 is a partition of an already derived volume integral.
No derivative or integration by parts is applied to its indicator.
There is therefore no new boundary flux at r=2. Near the origin the
original operator is zero; the complete transition region is covered
by (19). At r=1, R=-Theta and the combined numerator Theta+R vanishes.
Neither is divided separately by r log r. The full unit ball and all
of its energies remain present. The inherited decay justifies (17)
and its integrations throughout each compact lifespan interval.

## 5. Quantified allowance and matched comparison

Write B(s)=int_0^s alpha(q)dq and
M_src(s)=kappa_0 s+kappa_1,src B(s). Multiplication of (20) by exp(-M_src)
gives, for s<S_max,
\[
 e^{-M_{\rm src}(s)}(\mathcal F(s)+E_0)
 +\int_0^se^{-M_{\rm src}(q)}
        (\mathscr D+\alpha\mathscr H_{\rm rad})(q)\,dq
 \le\mathcal F(0)+E_0.
 \tag{21}
\]
The unchanged fixed-ball consequence is
\[
 \|\mathcal R(s)\|_{L^2(B_{R_b})}^2
 \le(1+R_b^2)^4\{(\mathcal F(0)+E_0)e^{M_{\rm src}(s)}-E_0\}.
 \tag{22}
\]
This is an actual smaller residual upper allowance than the same formula
with M_rad whenever B>0. It is not a bound on every higher derivative.

For the same data, functional, kappa_0 and **actual** B, the compact
upper allowances U_src=(F(0)+E0)exp(M_src) and
U_rad=(F(0)+E0)exp(kappa0 s+kappa1,rad B) obey
\[
 \boxed{\frac{U_{\rm src}}{U_{\rm rad}}
 =\exp\!\left[-\frac{49}{600}B(s)\right].}
 \tag{23}
\]
This is strict for B>0, and equality holds at B=0. Note44's completed
B_1<=69/4 also gives
\[
 \kappa_{1,\rm src}\le\frac{2821}{100}+B_0,\qquad
 \kappa_1-\kappa_{1,\rm src}\ge\frac{179}{100},
 \quad \kappa_1=30+B_0.
 \tag{24}
\]
The gain 49/600 is relative to the already improved radial constant,
not merely to the earlier coefficient30. It follows from coupling the
source term before taking norms; acquiring B_0 or another scalar
supremum is not required. B_0, B_1, kappa_0 and all initial data stay
unchanged.

These estimates still depend on an unknown compression integral. The
independent local G/alpha/B interval in Note42 is unchanged; one can
insert its B bound into (21), but no extension through its endpoint or
through a collision deadline is proved here. The gradient-only estimate
of Note42 remains available and is not claimed to be surpassed by (21).

Direct analysis with the same full source coefficients, radial fields
and actual jets can use exactly (13)-(20). No new physical first-jet
margin, collision-free rectangle, acquisition-cost advantage or
threshold coverage is obtained. The measurable gain is the compact
and fixed-ball residual allowance, including its explicit 49/600 rate.

## 6. Controls and the remaining source-specific problem

The proof of (11) uses the literal complete theta coefficient. However,
once that coefficient is fixed, (13)-(20) hold for **every** admitted
smooth radial W,J satisfying the residual definition and common
evolution. They do not use the additional theta-only statement that
the raw source mismatch vanishes. This distinction limits the result.

For the exact control
\[
 \Phi_*(u)=(64u^4+6)e^{-17u^2/4},\qquad
 (T,A)=(1/4,2\sqrt6)\in\mathscr P,
\]
the same operator still requires both terms
\[
 \mathcal R_{*,0}=[\mathcal A_T,K_1*]W_*^{\rm raw}
 +K_1*(\mathcal A_TW_*^{\rm raw}-\Theta_*^{\rm raw}).
 \tag{25}
\]
Its raw logarithmic source differs from theta's, so the second term is
not discarded. The prepared control satisfies the new estimate and
still has the finite collision deadline of Note28. Thus the new
intermediate gain excludes no control and cannot independently pay
that deadline for all its admitted data.

The other [registered controls][controls] retain these distinctions:

| Control | Failed literal source premise and retained scope |
| --- | --- |
| Weighted-square | Unit coefficients/full reflection fail; registered witnesses near 44.13 and 83.53 remain outside A in [1,6] |
| Finite-prime orbit | Selected-prime constraints do not give full reflection; no fixed compact location for its high-gap events |
| Reflected super-Gaussian | Complete square arithmetic fails; its pi/4 event is below this rectangle |
| Smooth shape / positive primitive | Their named properties do not give the literal complete theta amplitude; no event is newly placed here |
| Euler-factor | Arithmetic/conductor change; a Laguerre witness is not automatically a double event in this rectangle |
| RH-conditional endpoint | Retain the RH hypothesis, failed ordinary Dirichlet arithmetic and escaping double heights |
| Atomic / continuous compact | Atoms remain outside the imported smooth source-function theorem; admitted prepared comparisons retain their actual mismatch |

A source that fails the literal theta identity does not thereby fail
the derived coefficient bound when the **same theta operator** is used.
This is the [shape-only/control discipline][a02], not a new universal
obstruction. A future collision-excluding estimate must actually consume
additional information about the canonical trajectory or its prepared
data and show where the relevant control fails.

**Stop R5 here.** The bounded source-coefficient coupling and its exact
quantitative comparison are complete in-note. Parent B02 remains partial.
[Self-assessment25][review] records only same-assistant checks, not E08
or independent specialist review. The fixed [E08 R5 packet][packet]
routes the verification and proportionate manuscript integration to Sol.
No second candidate, numerical stage, radius optimization or manuscript
change was executed.

## 7. Provenance and inputs

Actual session metadata: thread 01a1889e-676b-7513-903a-476d0eb5a4ce,
turn 01a1889e-6990-7143-a14e-366791832f5b, model gpt-6-astra, effort max.
The [unique public archive][history] is chat0023. No subagents were used.
This is an internal LLM derivation with shared inherited premises; no
external specialist or formal verification is claimed.

The existing classical theta normalization was rechecked at
[NIST DLMF 20.2.3](https://dlmf.nist.gov/20.2.E3), retrieved 29 October 2026,
in the [existing reference record][dlmf]. The complete density
factorization is imported from Note40; inequalities (3)-(24) are derived
here, not attributed to DLMF. No new literature theorem or novelty claim,
PDF acquisition, numerical computation or interval certificate is used.

The following source hashes identify the preserved intake bytes; they
do not validate their mathematics. Progress05 is a live register and
is not treated as a frozen input after its R5 intake.

| Input | SHA-256 |
| --- | --- |
| notes/31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md | 9d2a9832f3a128d3bb2c3fc37eb7ab83547f2f9d35c16c82847ef7994795b8ec |
| notes/40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md | abbb999e364006ea3558869a29d39a648922c85f0df71e09fa23dd1c0b90440e |
| notes/42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md | 895a3f9524bb871d66f6ceae840e55f013f2a012df934abb78499dd73261634c |
| notes/44_RADIAL_COMPACT_COEFFICIENT_E07_R2_RETURN_20261029.md | d3f17cbc6cb822f7ce2fad1b35b92f9b976c4d33a364f1c5e1a9eb81112a347f |
| notes/46_STRICT_COMPACT_GAIN_INTEGRATION_CONTINUATION_20261029.md | 9a06dbfad0dc59110c09bdc3b3456409a63ff807228ec99d586d2cd4ab2bcbeb |
| reviews/24_RADIAL_COMPACT_GAIN_E08_ASSESSMENT_20261029.md | 98cca12fa3f6d4504a4dfdb7714efb002a2ce71845b01f7a31213555941ab340 |
| radial_deformations_and_zero_dynamics.tex | 3b913be9c78dd46c224380c7164673be4e967238e65ad95018773eb2fa7575c4 |
| book/main.tex | b954e99f992ff44fafc2745661257e2d5ce730360c3f9292862b195469f95abb |

[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_SOURCE_COUPLING_ASSESSMENT_REQUEST_R5_20261029.md
[next]: 48_SOURCE_COUPLING_SOL_CONTINUATION_20261029.md
[n31]: 31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[n40]: 40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n42]: 42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md
[n44]: 44_RADIAL_COMPACT_COEFFICIENT_E07_R2_RETURN_20261029.md
[n46]: 46_STRICT_COMPACT_GAIN_INTEGRATION_CONTINUATION_20261029.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[review]: ../reviews/25_SOURCE_COUPLING_B02_R5_SELF_ASSESSMENT_20261029.md
[history]: ../chat-histories/0023_2026-10-29T17-04-04Z_continue-ctf-b02-coupled-estimate.json
[dlmf]: ../references/01_CIRCLE_HEAT_AND_JACOBI_NORMALIZATIONS_20261027.md
