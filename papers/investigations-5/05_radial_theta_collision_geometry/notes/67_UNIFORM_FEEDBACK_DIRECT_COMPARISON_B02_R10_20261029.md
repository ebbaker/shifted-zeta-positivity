# CTF-B02 R10: the direct margin also pays uniform feedback

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 **chat0031**, **Continue CTF-B02 Astra assessment**.

**Status: proved in-note; same-assistant analytical checks only.** The
selected unpaid consumer was a bound for G/E0 and alpha independent of
the auxiliary horizon, at the unchanged physical mark (T,A)=(1/4,2).
The displayed direct estimate in Note29 grows with that horizon.
The stronger direct comparison below pays the entire new consumer:
the same theta source information gives H>(70/73)M, and a generic
carrier/diffusion argument converts a positive physical mass margin
into an explicit time-uniform gradient and feedback bound.

This strengthens quantitative regularity on the already covered mark.
**No source-residual advantage is demonstrated.** B is
not bounded on the half-line: it grows at least linearly.
[Self-assessment35][review] is internal checking, not E08; the fixed
[E08 R10 packet][packet] is ready. [Progress05][progress] retains the
intake and owns live status.

## 1. Fixed consumer, source and comparison

The R10 intake selected one question under [Continuation66][n66]:
can complete source information pay
\[
 \sup_{s\ge0}G(s)/E_0\le K_\infty<\infty,\qquad
 \sup_{s\ge0}\alpha(s)\le2K_\infty/3
 \tag{1}
\]
with all constants paid before evolution? An equally informed direct
method was explicitly allowed to strengthen its estimates. This is a
quantitative supporting milestone under [avoid01][a01], not a new
noncollision criterion. The stopping rule was to return a useful bound
if the direct method already pays the consumer.

Use the inherited prepared radial solution class of [Note28][n28]:
\[
 W=(U,V),\quad W_s=\Delta W+\alpha\operatorname{div}(vW),\quad
 v=X+\frac{X}{1+|X|^2},\quad E_0=\|W_s\|_2^2>0,
\]
\[
 G=\|\nabla W\|_2^2,\quad g=G/E_0,\quad
 D=\int(\operatorname{div}v)|W|^2,\quad
 \alpha=2G/D,\quad B(s)=\int_0^s\alpha,\qquad g/3\le\alpha\le2g/3.
 \tag{2}
\]
At p=(1/4,2), keep the complete q(u)=exp(u²/4)Phi(u), literal cosine,
and unit preparation:
\[
 \rho=\mathbf1_{r\ge1}\frac{q(u)}{8\pi r^3},\quad
 u=\tfrac12\log r,\quad
 W_0=K_1*\{\rho(\cos(2u),-u\sin(2u))\},
\]
\[
 h_0=K_1*\{\rho(1+u^2)\},\quad
 M_j=\int_0^\infty u^jq(u)\,du,\quad M=M_0+M_2,
\]
\[
 R_0=\int_0^\infty e^{4u}(1+u^2)q(u)\,du+6M,\qquad
 \mu=\left|\int W_0\right|=|(H,H_a)|.
 \tag{3}
\]
Here K_t=(4 pi t)^(-3/2)exp(-|X|²/(4t)); 4 pi r² rho dr=q du.
Multiplication precedes preparation. V and all higher jets use the
common fixed-mark propagator, without differentiating the feedback.

The carrier h solves the same scalar equation along the realized alpha
path. [Note29][n29] gives h>=|W|, int h=M, and
\[
 R=\int|X|^2h,\qquad R'\le6M-2\alpha R,\qquad
 R\ge c_3\mu^{7/3}E_0^{-2/3},\quad
 c_3=\frac37\left(\frac{15}{14\pi}\right)^{2/3}.
 \tag{4}
\]
These hold first on compact intervals before Smax. The six in (3) is
the full preparatory cost; all spatial integrals include the inner ball.

## 2. The same source data give a larger direct physical margin

[Note55][n55] proves q' <= (1/5-74u)q by an inequality for every positive
square summand, with the complete sum and tail retained. Integration of
(u q)' and Cauchy--Schwarz give
\[
 74M_2\le M_0+M_1/5\le M_0+\sqrt{M_0M_2}/5.
 \tag{5}
\]
The endpoint u q vanishes at zero and infinity; Note55's differentiated
complete-tail bounds justify this first-moment integration. If
z=M2/M0>=1/72, then sqrt(z)<=sqrt(72)z<9z. Equation (5) would imply
(361/5)z<1, whereas (361/5)z>=361/360>1. Thus
\[
 \boxed{M_2/M_0<1/72.}
 \tag{6}
\]
For real x, cos x>=1-x²/2, since 1-cos x=2 sin²(x/2)<=x²/2. Hence
\[
 H(1/4,2)\ge M_0-2M_2>\frac{35}{36}M_0>\frac{70}{73}M,\qquad
 \boxed{\mu\ge\mu_*:=\frac{70}{73}M>0.}
 \tag{7}
\]
No numerical evaluation of H is used. This H floor is stronger than
the earlier displayed 35M2/18 floor for |Ha|, which is <35M0/1296 by
(6). The earlier floor remains valid. With actual moment budgets, the
direct side may also use sqrt((M0-2M2)²+(35M2/18)²); (7) is a convenient
paid floor, not an optimality claim.

Even R7's weaker M4/M2<1/24 alone gives M2/M0<1/24 by Cauchy--Schwarz
and mu>22M/25. The stronger (7) uses the already proved source slope,
not a new source premise. No physical domain is enlarged.

## 3. A generic direct theorem: uniform carrier moments and increments

For any inherited radial solution with finite E0,M,R0,G0 and a supplied
0<mu_*<=mu, set
\[
 r_*:=c_3\mu_*^{7/3}E_0^{-2/3}>0.
 \tag{8}
\]
Literal theta is needed only to pay (7). With the unnormalized forward
Fourier transform, ||W||1<=M implies |hat W|<=M. Retaining the full
weighted deficit, as in the [stronger R9 direct comparison][direct],
gives for k>0
\[
 G\ge k^2E_0-\frac{M^2k^5}{15\pi^2},\qquad
 \frac1{2\pi^2}\int_0^k(k^2-t^2)t^2dt=\frac{k^5}{15\pi^2}.
\]
The maximum occurs at k³=6 pi² E0/M². Therefore
\[
 g\ge\frac35\left(\frac{6\pi^2E_0}{M^2}\right)^{2/3},\qquad
 \boxed{\alpha\ge a_*:=\frac15
       \left(\frac{6\pi^2E_0}{M^2}\right)^{2/3}>0.}
 \tag{9}
\]
This is an elementary mass Fourier estimate, not a claim of the optimal
Nash constant. No zero-mass hypothesis is used. Equations (4), (9) yield
\[
 R(s)\le e^{-2a_*s}R_0+\frac{3M}{a_*}(1-e^{-2a_*s}),\qquad
 \boxed{r_*\le R(s)\le R_*:=\max\{R_0,3M/a_*\}.}
 \tag{10}
\]
Put chi=R*/r*>=1, L=(log chi)/2 and c=3M/r*. Dividing (4) by R and
integrating on any [t,t+ell] within the lifespan proves
\[
 \boxed{B(t+\ell)-B(t)\le L+c\ell,\qquad
        \int_t^{t+\ell}g(s)\,ds\le3(L+c\ell).}
 \tag{11}
\]
The second inequality uses g<=3 alpha. This uniform increment bound is
the input to the next step. Its positive moment floor r* explicitly
costs a physical margin; carrier positivity and E0>0 do not supply it.

## 4. Retaining diffusion gives the time-uniform bound

[Note42][n42] gives, with N=||Delta W||2² and Hrad>=0,
\[
 g'=-2N/E_0+\alpha(10g+21/4-\mathscr H_{\rm rad}/E_0).
\]
Since N/E0>=g² and alpha<=2g/3, one has 2g²>=3 alpha g. Thus
\[
 y:=g+\tfrac34,\qquad \boxed{y'\le7\alpha y.}
 \tag{12}
\]
No positive lower diffusion variance or order-three derivative cost is
required. Keeping this diffusion improves the exponent 10 obtained by
dropping it in Note42.

Choose delta=1/(7c)=r*/(21M). If s>=delta, (11) supplies t in
[s-delta,s] with g(t)<=3(L+c delta)/delta=3c(1+7L). Integrating (12)
from t to s and using (11) gives y(s)<=[3/4+3c(1+7L)]exp(7L+1).
If 0<=s<=delta, integration from zero gives
y(s)<=(g0+3/4)exp(7L+1). Consequently
\[
 \boxed{K_\infty+\tfrac34
 :=e\,\chi^{7/2}\max\left\{g_0+\tfrac34,\,
      \tfrac34+\frac{9M}{r_*}
           \left(1+\tfrac72\log\chi\right)\right\},\qquad
 g(s)\le K_\infty.}
 \tag{13}
\]
This was proved before Smax. If Smax were finite, (13) would keep G
bounded there, contradicting Note28's continuation criterion. Hence
Smax=infinity and the bound holds for every s>=0. Global existence was
not assumed, and no summability of local restart times was used.

In particular,
\[
 a_*\le\alpha(s)\le2K_\infty/3,\qquad
 a_*s\le B(s)\le\min\left\{\frac{2K_\infty s}{3},\,
       \frac12\log\frac{R_0}{r_*}+\frac{3Ms}{r_*}\right\}.
 \tag{14}
\]
Uniform feedback does not mean bounded cumulative compression. No
limiting profile, convergence or sharp long-time asymptotic is claimed.

## 5. A complete analytical theta payment

All inputs of (13) are initial budgets. They can also be bounded without
numerical acquisition. Let
\[
 \eta=70/73,\quad d_0=26/3,\quad e_+=(8\pi)^{-3/2},\quad
 e_-=c_3^{3/2}\eta^{7/2}d_0^{-3/2},
\]
\[
 r_-=c_3\eta^{7/3}e_+^{-2/3},\quad
 a_-=(6\pi^2e_-)^{2/3}/5,\quad
 R_+=\max\{d_0,3/a_-\},\quad \chi_+=R_+/r_-.
 \tag{15}
\]
[Note63][n63] pays R0/M<d0 with its full preparation cost. Gaussian
Young bounds give E0<=e+ M² and G0<=(3/4)e+ M². The time-zero case of
(4), with (7), gives E0>=e- M². It follows that
\[
 r_*\ge r_-M,\quad a_*\ge a_-,\quad R_*\le R_+M,\quad
 1\le\chi\le\chi_+,\quad g_0\le3e_+/(4e_-).
\]
The right side of (13) increases with chi>=1 and M/r*. Thus
\[
 \boxed{K_\theta+\tfrac34
 :=e\,\chi_+^{7/2}\max\left\{\tfrac34+\frac{3e_+}{4e_-},\,
    \tfrac34+\frac9{r_-}\left(1+\tfrac72\log\chi_+\right)\right\},
 \qquad g(s)\le K_\infty\le K_\theta.}
 \tag{16}
\]
This is an explicit finite constant, not a measured or optimized value.
It replaces a horizon-growing allowance with a horizon-independent one.
Under q -> lambda q, E0,G0 scale by lambda² and M,R0,mu* by lambda;
(13)--(16) are unchanged. No acquisition-cost or numerical sharpness
ranking is asserted.

## 6. Residual obligations and the stronger direct comparison

The source residual remains the genuine nonzero preparation defect of
[Notes31][n31]/[40][n40], with its full forced commutator equation.
At r=1, Rcal=-Theta and the combined numerator Theta+Rcal cancels.
No quotient is split, multiplier is moved through K1, cutoff derivative
is discarded, or inner-ball energy is removed.

The consumer (1) does not need a residual bound. For its existing
weighted consumer on finite [0,S], retain exactly
F=G+||omega Rcal||2²+||J2||2² and [Note47][n47]'s complete constants
kappa0=8+A2²+A1+A0 and kappa1=274/25+B1+B0. Note40 pays their finite
source/coefficient budgets and F0. The inherited dissipation Dcal,
including the nonnegative radial remainder, satisfies
\[
 e^{-\mathcal M(s)}(\mathcal F(s)+E_0)
 +\int_0^s e^{-\mathcal M(q)}\mathscr D(q)\,dq
 \le\mathcal F(0)+E_0,\qquad
 \mathcal M(s)=\kappa_0s+\kappa_1B(s).
 \tag{17}
\]
Equation (14) now gives F(s)+E0 <= (F0+E0)exp((kappa0+2 kappa1
K_infinity/3)s). This is finite on every finite horizon, **not uniform
in time for the residual or higher jets**. Their source constants are
not silently needed for (13), and no new weighted estimate is claimed.

| Comparison | What it supplies |
| --- | --- |
| Note29's displayed direct conversion | Global regularity from mu*>0; its displayed G allowance grows with the horizon. |
| Same direct information, (9)--(13) | A time-uniform bound for G/E0 and alpha, by a mass Fourier estimate and an elementary sliding-interval argument; no new source acquisition. |
| Literal theta information | Pays (7) and (15). Positive weighted-square sources share the sufficient input at this low mark. |
| R7 same-B correlations and R8 local variance | Their supporting gains remain. Neither is needed for this direct uniform bound; no numerical sharpness or cost comparison is made. |
| R9 and its stronger direct deadline | Sw=6(10 pi²)^(-2/5)(M R0)^(2/5)E0^(-2/5)<S9 remains an upper-deadline statement under m=0, not a lower regularity bound. |

For a fair quantitative comparison, first give the older direct
conversion the same retained diffusion (12). It then supplies
\[
 {\cal U}_7(s):=(g_0+\tfrac34)(R_0/r_*)^{7/2}
                 e^{21Ms/r_*}-\tfrac34.
\]
Our combined direct allowance is min{U7(s),K_infinity}; it is never
worse and is strictly smaller than U7(s) for
\[
 s>s_c:=\frac{r_*}{21M}
 \log\frac{K_\infty+3/4}{(g_0+3/4)(R_0/r_*)^{7/2}}<\infty.
 \tag{18}
\]
Here sc>=delta because chi>=R0/r* and the maximum in (13) is at least
g0+3/4. Thus the strict gain is not credited to the avoidable exponent-10
loss in the older bound. Neither comparator uses a new source datum.

At the actual mark, mu*>0 was obtained before auxiliary evolution.
Applying (14) at the finite number Sw is only a checkpoint on this
already noncolliding trajectory. It is not independent regularity
under m=0. The dependency is source budget -> direct physical margin
-> uniform feedback.

**Decision:** the strengthened direct method pays the selected consumer.
No source-residual advantage is demonstrated. This does not exclude
other signed, diffusion or source-specific estimates, or assert that
(13) is optimal. Parent B02 remains partial.

## 7. Control premises and stopping boundary

The [registered controls][controls], [earlier counter-kernels][old-controls]
and [scoped form obstructions][form-controls] supply the comparison
families. These are analytical premise checks; event certificates were
not numerically replayed.

| Control | Actual shared or failed premise |
| --- | --- |
| Exact Gaussian-polynomial cosine | Shares the generic radial flow and finite moment/diffusion estimates. Its collision has mu=0, so r*>0 fails. At T=1/4, M2/M0=7/24>1/72 explicitly fails the theta moment payment. Its event frequency is 2 sqrt(6), not 2. |
| Positive weighted squares | The per-summand slope and (7) apply at T=1/4,A=2 to admissible positive weights. Their registered high-frequency events are outside this mark and have mu=0. Missing unit coefficients/reflection is not a failed premise of this sufficient low-mark estimate. |
| R6 polynomial kernels | Retain theta moments but fail literal cosine, so the passage to (7) is unavailable. Their constructed m=0 fails the generic positive-margin premise. A finite cosine prefix does not repair this. |
| Finite-prime orbit | Altered arithmetic/reflection; an admitted actual event fails mu*>0. No event at this mark or new quantitative moment failure is asserted. Positive weighted-square realizations inherit the low-mark result when its hypotheses apply. |
| Reflected super-Gaussian | Its registered event has mu=0 and a different frequency. Its R10 moment ratio is unacquired; no ratio failure is invented. |
| Smooth shape / positive primitive | Positivity and decay can admit the carrier comparison, but actual collisions fail mu*>0. Shape alone does not supply (7); their slope/ratio has not been evaluated here. |
| Euler-factor, every p | Shifted source/conductor; no R10 ratio evaluation. A negative Laguerre witness is not necessarily a double event and does not itself set mu=0. A genuine admitted double event fails the positive margin. |
| Atomic/profile / continuous compact | Atomic inputs are outside the imported source-function theorem. Admitted continuous prepared versions satisfy the generic bound if a positive margin is supplied; actual events fail it. No local-existence extension is presumed. |
| RH-conditional endpoint | Retain RH conditionality and escaping double heights. Those events have mu=0; no unconditional exclusion or new R10 measurement follows. |
| Earlier q and q_(T,a) counter-kernels | Preserve their positive-source and threshold statements. No CTF carrier or solution is presumed without verification; an event instantiated in the inherited prepared class fails mu*>0. No same-mark source slope or moment budget is asserted. |
| SUSY smooth-density / two-channel | These concern other Weil forms and factorization claims, not an instantiated (2)--(3) solution. This note claims neither full-Weil positivity nor such a factorization; no CTF quantitative failure is assigned. |

Positive mass is direct physical information, not an arithmetic separator.
No known collision is excluded from a class whose premises it shares.

**Stop R10. Next: [E] CTF-E08 R10 — Sol**, the fixed proof/cost/scope
assessment. [Continuation68][next] supplies model-change guidance.
No second candidate, new mark, acquisition campaign, numerical evolution,
manuscript expansion or subagent was used. Uniform control of the full
residual and uniformity over all physical marks remain unproved.

## 8. Provenance and classical inputs

Thread 01a189c5-8cc0-7870-9ab3-7a816387871a; turn
01a189c5-8f0f-7e02-bbc1-7cb941c486f7; **gpt-6-astra / max**, verified in
session metadata. The sole registration is [chat0031][history].
Read the [result index][results], [spatial-flow results][spatial], and
[avoid index][avoid], particularly [control premises][a02], [scope][a07]
and [quantitative utility][a20].

The Fourier convention and Parseval identity were checked in
[DLMF 1.14.1](https://dlmf.nist.gov/1.14.E1) and
[1.14.8](https://dlmf.nist.gov/1.14.E8), 29 October 2026.
Iteration in three coordinates and conversion from the unitary transform
gives the (2 pi)^(-3) factor used here.
The [existing classical-input annotation][refs] records this inspection
and inherited PDE references. The global cosine inequality is proved
above; checking [DLMF 4.19.1--2](https://dlmf.nist.gov/4.19) does not
make series truncation a global bound. All new constants are derived
here. No literature priority, specialist or formal verification is claimed.

[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: 29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n31]: 31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[n40]: 40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n42]: 42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md
[n47]: 47_EXTERIOR_SOURCE_RESIDUAL_COUPLING_B02_R5_20261029.md
[n55]: 55_COSINE_JET_CORRELATION_B02_R7_20261029.md
[n63]: 63_RADIAL_SECOND_CANCELLATION_DEADLINE_B02_R9_20261029.md
[n66]: 66_RADIAL_DEADLINE_ASSESSMENT_AND_MODEL_CONTINUATION_20261029.md
[direct]: CTF_B02_R9_WEIGHTED_DIRECT_COMPARISON_CHAT0029_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[review]: ../reviews/35_UNIFORM_FEEDBACK_B02_R10_SELF_ASSESSMENT_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_UNIFORM_FEEDBACK_ASSESSMENT_REQUEST_R10_20261029.md
[next]: 68_UNIFORM_FEEDBACK_AND_MODEL_CONTINUATION_20261029.md
[history]: ../chat-histories/0031_2026-10-29T22-26-27Z_continue-ctf-b02-astra-assessment.json
[refs]: ../references/11_CONSERVATIVE_FEEDBACK_AND_DIFFUSION_CONTRACTION_20261028.md
[results]: ../../../../result-summaries/README.md
[spatial]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[old-controls]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[form-controls]: ../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md

