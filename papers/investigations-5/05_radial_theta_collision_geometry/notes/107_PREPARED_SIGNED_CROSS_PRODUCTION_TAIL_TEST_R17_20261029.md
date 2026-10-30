# R17: the prepared pointwise cross-production sign fails in the full tail

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
ultra**, Investigation05 **chat0040**, *Continue radial theta research*.
Parent synthesis and three read-only same-model contributing checks;
shared premises remain. No independent specialist or formal review.

**Status: proved in-note, pending E08 R17 assessment. Scoped failure of
the selected pointwise mixed-production sign route.** For the unchanged
complete theta source, literal mark (T,A)=(1/4,2), prescribed unit heat
preparation, and the exact integration-by-parts density defined below,

\[
 \frac{C_{\beta_0}(r)}{r^2h_0(r)^2}
 \longrightarrow 16|a|^2\left(\frac{\pi}{1+4\pi}\right)^2>0.
 \tag{1}
\]

Thus this density is positive at every sufficiently large radius. This
does **not** determine its spatial integral, the full signed numerator,
or the sign of alpha minus beta. No physical-mass premise is removed.

The pre-analysis intake is in [Progress05][progress]. [Notes104][n104]
and [106][n106] govern this one bounded decision after accepted R16.
Apply the [result index][results], [flow cluster][flow], [controls][controls]
and [avoid index][avoid], particularly [target classification][a01],
[separate-sign losses][a12], [scope][a07] and [circular inputs][a14].
This is an obstruction to a specified sufficient proof step, not a new
noncollision criterion. [Review54][review] records the internal checks.

## 1. The one selected route and its original-alpha consumer

Use the actual path and notation of [Note101][n101]:

\[
 W_s=\Delta W+\alpha\operatorname{div}(vW),\qquad
 h_s=\Delta h+\alpha\operatorname{div}(vh),\qquad
 v=X+\frac{X}{1+|X|^2},\quad d=\operatorname{div}v\in[3,6],
\]
\[
 a=\frac{\int W}{M},\quad M=\int h,\quad n=|a|^2,\quad e=W-ah,
 \qquad \beta=\frac{2\|\nabla h\|_2^2}{\int dh^2}.
\]

The complete signed identity is

\[
 (\alpha-\beta)D_W=Q_\beta(e)+\int C_\beta(X)\,dX,
 \qquad Q_\beta(e)=2\|\nabla e\|_2^2-\beta\int d|e|^2,
\]
\[
 C_\beta(X)=-2(a\cdot e(X))
                 (2\Delta h(X)+\beta d(X)h(X)).             \tag{2}
\]

The proposed sufficient decomposition would pay the mixed term through
the local lemma C_beta<=0, together with a separate nonpositive payment
for Q_beta(e), on a first-exit interval with alpha<=L. It would then give
alpha<=beta<=L using R16's local carrier comparison, replacing R16's
failed unsigned allowance. The Q payment and the passage from a non-strict
bound to a complete invariant-barrier proof were not assumed settled.
The initial sign lemma was the first necessary test of this particular
route. It fails, so these later steps are not pursued.

The class being rejected is **this everywhere-nonpositive density lemma
in the representation (2)**, not every representation differing by a
divergence and not every integrated signed estimate. No assertion that
previous work had claimed this lemma is made.

Only initial preparation is tested. No mass-paid global alpha bound,
R12 decay, R13 defect or E0/n, or R15 attraction is used. The positive
physical mass is used below only to make the counter-sign strict; it
does not pay a new ceiling. A zero-mass specialization is kept explicit.

## 2. Exact source and non-truncated Gaussian tail bounds

Write R=|Y|, u=(log R)/2 and

\[
 F(Y)=\mathbf1_{R\ge1}\rho_{1/4}(R)(1+u^2),\quad
 \chi(u)=\frac{(\cos(2u),-u\sin(2u))}{1+u^2},
 \quad h_0=K_1*F,\quad W_0=K_1*(F\chi),                    \tag{3}
\]

where K1(X)=(4pi)^(-3/2)exp(-|X|²/4). The multiplier is applied in the
raw Y variable, before convolution. In particular W0/h0 is not chi
evaluated at the observation radius. The complete series from
[Note98 §2][n98] is

\[
 \rho_{1/4}(R)=\frac\pi4R^{3/2}e^{(\log R)^2/16}
 \sum_{j\ge1}(j^4-cj^2/R^2)e^{-\pi j^2R^2},
 \qquad c=\frac3{2\pi}<\frac12.                            \tag{4}
\]

For R>=1 define L(R)=exp(pi R²)F(R), and set L=0 inside the sphere.
All summands are retained. Positivity and R>=1 give

\[
 L(R)\ge c_0:=\frac\pi4(1-c)>0,
\]
\[
 L(R)\le\frac\pi4 S_4 R^{3/2}e^{(\log R)^2/16}
               (1+(\log R)^2/4),\qquad
 S_4=\sum_{j\ge1}j^4e^{-\pi(j^2-1)}<\infty.                \tag{5}
\]

The logarithm of this upper envelope is o(R²). Hence for every
epsilon0>0 there is a finite C_epsilon0 such that

\[
 c_0\le L(R)\le C_{\varepsilon_0}e^{\varepsilon_0R^2}
 \quad(R\ge1).                                            \tag{6}
\]

The upper bound also holds for the zero extension. This proves, rather
than assumes, the complete-source tail property used below. No finite
square truncation, unquantified discarded term, source derivative or
asymptotic differentiation occurs.

## 3. Exact conditional representation and its second-moment limit

For each X define the probability measure

\[
 dP_X(Y)=\frac{K_1(X-Y)F(Y)\,dY}{h_0(X)}.                   \tag{7}
\]

The denominator is strictly positive. Put

\[
 D=\pi+\tfrac14,\quad d_*=1+4\pi=4D,\quad
 \kappa=\frac\pi{d_*},\quad m=X/d_*.
\]

Completing the square is exact:

\[
 \pi|Y|^2+\tfrac14|X-Y|^2
       =\kappa|X|^2+D|Y-m|^2.                               \tag{8}
\]

Thus P_X has density proportional to exp(-D|Y-m|²)L(|Y|), with the
entire raw support |Y|>=1 still present. For r=|X| sufficiently large,
the unit ball about m lies outside that sphere, and its normalizer N_X
obeys the uniform lower bound

\[
 N_X\ge c_0\int_{|Z|\le1}e^{-D|Z|^2}\,dZ=:N_->0.          \tag{9}
\]

Here Z=Y-m. From (6), for any delta>0,

\[
 e^{-D|Z|^2}L(|m+Z|)
 \le C_\delta e^{2\delta r^2/d_*^2}
                         e^{-(D-2\delta)|Z|^2}.            \tag{10}
\]

Fix epsilon>0. Choose delta so small that A_delta=D-2delta>0 and
2delta/d_*²<A_delta epsilon²/2. For r>=2d_*, (9)-(10) give

\[
 E_X\!\left[(1+|Z|^2/r^2)\mathbf1_{|Z|>\varepsilon r}\right]
 \le \frac{C_\delta}{N_-}
 e^{[2\delta/d_*^2-A_\delta\varepsilon^2/2]r^2}
 \int_{\mathbb R^3}(1+|Z|^2)e^{-A_\delta|Z|^2/2}\,dZ
 \longrightarrow0.                                       \tag{11}
\]

On the complementary region |Z|²/r²<=epsilon². Since epsilon is
arbitrary, this pays the required second moment, not merely weak
concentration:

\[
 \boxed{E_X\left|Y/r-X/(d_*r)\right|^2\longrightarrow0.}    \tag{12}
\]

All bounds are rotationally invariant. In particular |Y| tends to
infinity in P_X probability as r tends to infinity. This is a statement
about the changing conditional measure (7), not the unconditioned source
moments. Small raw moments cannot be treated as uniform bounds for this
family of conditioned distributions.

## 4. The actual prepared ratios and Laplacian

The observation ratio satisfies |chi(u)|<=1 and chi(u)->0 as u->infinity;
indeed |chi(u)|<=1/sqrt(1+u²). Equations (3),(7) imply

\[
 \frac{W_0(X)}{h_0(X)}=E_X\chi((\log|Y|)/2)\longrightarrow0. \tag{13}
\]

To justify the limit directly, split at a fixed large |Y| threshold;
the ratio is uniformly small beyond it and its probability inside it
tends to zero by (12). No oscillatory cancellation has been assumed.

Differentiate the Gaussian kernel, not an asymptotic formula for h0:

\[
 \Delta K_1(X-Y)=
       (|X-Y|^2/4-3/2)K_1(X-Y),
\]
\[
 \frac{\Delta h_0(X)}{h_0(X)}
       =E_X[|X-Y|^2/4-3/2].                                \tag{14}
\]

The complete Gaussian tail (6), with delta<pi, justifies differentiation
under the integral and all polynomial weights. No derivative falls on
the exterior indicator; there is no unrecorded trace at R=1. The
prepared observation X ranges over all R3, including the full inner ball.
Using (12) in (14) gives

\[
 \boxed{\frac{\Delta h_0(r)}{r^2h_0(r)}
 \longrightarrow\frac14(1-1/d_*)^2=4\kappa^2.}             \tag{15}
\]

In particular no inference of a derivative asymptotic from a function
asymptotic was needed. Since F is nonzero with Gaussian decay, h0 is
positive and smooth with finite H1 norm, and beta0 is finite with
denominator at least 3||h0||²>0.

## 5. Counter-sign, its mass dependency, and its precise scope

From (13),

\[
 \frac{a\cdot e_0}{h_0}
       =a\cdot\frac{W_0}{h_0}-n\longrightarrow-n.
\]

As d<=6 and beta0 is finite, (15) then proves

\[
 \frac{C_{\beta_0}(r)}{r^2h_0(r)^2}
 =-2\frac{a\cdot e_0}{h_0}
       \left(2\frac{\Delta h_0}{r^2h_0}+\frac{\beta_0d}{r^2}\right)
 \longrightarrow16n\kappa^2.                              \tag{16}
\]

For completeness the strict n>0 at the fixed actual mark can be paid
without invoking any global-flow conclusion. Let M_j=int_0^infinity
u^j q(u)du. [Note55][n55] proves M4<M2/24 with M2>0. For x>=0,
sin x>=x-x³/6 (integrate cos x>=1-x²/2). Therefore

\[
 -H_A(1/4,2)=\int_0^\infty u q(u)\sin(2u)\,du
 \ge2M_2-\tfrac43M_4>\tfrac{35}{18}M_2>0.                  \tag{17}
\]

Unit preparation preserves this mass. This is an existing physical-mass
fact, used **only to make the counter-sign strict**. It is not relabeled
as a mass-free regularity input or fed back into R10. In particular (16)
is a general limit for any a; when n=0, a=0 and C_beta is identically
zero. No division by n is made.

Equations (16)-(17) prove (1). They also show |e0|/h0->|a|, so no
uniform bound |e0|<=theta|a|h0 with theta<1 holds initially. This is a
consequence of the same test, not a claim about the weighted L2 error.
The absolute tail is Gaussian-small and all the integrals in (2) are
finite. Its positive contribution may be outweighed by the rest of
space. Neither a numerical cutoff radius nor a tail dominance claim is
asserted.

**This refutes only the everywhere-nonpositive mixed-density lemma in
(2).** It establishes no sign for int C_beta, Q_beta(e), their sum,
alpha-beta, or any positive auxiliary time. The old direct global
regularity proof at this already mass-separated mark remains valid.

## 6. Controls, identical direct information, and retained costs

The new input was literal complete-source Gaussian preparation and its
conditional observation ratio, rather than the failed unsigned R16
barriers. The calculation discovers that the tail limit only requires
bounded chi tending to zero. It consequently also works for every fixed
literal frequency, including A=0, with this heavier carrier. It does not
extract a useful arithmetic or low-frequency discriminator.

| Registered control | Premise actually tested / limitation |
| --- | --- |
| Positive weighted squares | A positive first-square coefficient gives the same kappa and complete L bounds, up to constants. At A=2, (17) applies and the same pointwise lemma fails. At its double event A*>44, a=0 and C_beta=0; that event is not a positive-tail counterexample. |
| Finite-prime positive square realizations | When the recorded square tails and positive leading square are present, the same tail argument applies; keep their own frequency and mass. No new event or matching coefficients are asserted. |
| R6 polynomial observations | Fail literal chi; chi may not be bounded or vanish. They do not instantiate (13) without a separate proof. |
| Reflected super-Gaussian, smooth/positive-primitive controls | The exact tail factorization (4)-(6) is not supplied for them. Their known events remain, but this theorem assigns them no unproved Gaussian tail limit. |
| Gaussian-polynomial cosine | Has its own raw tail and normalized observation; no claim of the exact theta L or kappa. Its collision facts are retained, not replayed. |
| Euler-factor controls | No matching prepared tail calculation is made. Negative Laguerre witnesses are not automatically zero vector masses. |
| Atomic/profile and continuous compact controls | Fail the unbounded-support lower L bound in (6); conditional escape (12) is not inferred. |
| RH-conditional endpoints and earlier q/q_(T,a) controls | Retain their conditionality, threshold and source-class qualifications; (4)-(6) must be checked before applying this test. |
| SUSY smooth-density/two-channel forms | Concern other forms, not an instantiated preparation (3); no fabricated premise failure is assigned. |

The control screen follows [cluster12][controls] and [Note101 §6][n101].
The actual theta data already defeat the selected lemma; the weighted
control is not used to pretend that all source-sensitive estimates fail.
The equally informed direct method receives (7)-(17) and exactly the
same negative conclusion, with no primitive/residual advantage.

No evolved carrier forcing is set to zero: (alpha-beta)div(vh) remains
actual. The source residual, raw/prepared mismatch, full C0/C1,
commutators, combined sphere cancellation and entire inner ball remain
as in Notes31/40/47. This initial convolution test neither invokes a
residual estimate nor replaces it. It uses the full exterior indicator
inside the convolution; it never cuts the prepared field at r=1.

## 7. Decision and continuation

**Stop the selected pointwise mixed-production route.** The full-tail
counter-sign is proved on the unchanged actual source, with no numerical
campaign, source modification, parameter expansion or manuscript edit.
The integrated signed-feedback problem remains open. A future route
must explicitly pay spatial cancellation (including the positive tail)
or select a separately justified ceiling gap; neither is selected here.

**Next: [E] CTF-E08 R17 — Sol**, the [fixed six-check assessment][packet].
Its task is to check this proof and its narrow scope, not to find another
mechanism. E07 remains unready: no closing estimate exists. Parent B02
remains partial, E03/B03 gated; [Continuation108][next] supplies research
and model-change guidance. All derivations here are self-contained
Gaussian algebra and inequalities from the cited repository inputs;
no external asymptotic or convergence theorem is imported.

[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[n104]: 104_NEXT_ASTRA_HANDOFF_AFTER_ANALYTICAL_INTEGRATION_20261029.md
[n106]: 106_MASS_FREE_FEEDBACK_ASSESSMENT_AND_MODEL_CONTINUATION_R16_20261029.md
[n101]: 101_MASS_FREE_FEEDBACK_DEFECT_AND_SLOPE_CLOSURE_TEST_R16_20261029.md
[n98]: 98_RADIAL_LOG_SLOPE_ATTRACTION_B02_R15_20261029.md
[n55]: 55_COSINE_JET_CORRELATION_B02_R7_20261029.md
[review]: ../reviews/54_PREPARED_CROSS_PRODUCTION_TAIL_INTERNAL_REVIEW_R17_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_PREPARED_CROSS_PRODUCTION_TAIL_ASSESSMENT_R17_20261029.md
[next]: 108_SIGNED_TAIL_ROUTE_DISPOSITION_AND_MODEL_CONTINUATION_R17_20261029.md
[results]: ../../../../result-summaries/README.md
[flow]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a14]: ../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
