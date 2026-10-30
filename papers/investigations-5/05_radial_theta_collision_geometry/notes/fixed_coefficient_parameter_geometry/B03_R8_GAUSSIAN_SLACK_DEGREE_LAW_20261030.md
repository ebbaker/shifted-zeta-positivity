# B03 R8: Gaussian slack, full-polynomial convergence, and its efficiency limit

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **max**, new Investigation05 **chat0050**, *Continue B03 R8 analysis*, thread `01a18e52-fa91-7b61-b31b-b311eee675f8`. This is a proof-author analytical return and self-check, not a separate-model assessment. [Progress06](../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md) alone owns live status.

**Return.** The proposed Gaussian-retaining compression is computable and convergent for the **entire degree-dependent polynomial**, not just individual monomials. At the prescribed critical equality of inner radius and Gaussian slack, its direct payment satisfies
\[
 \log \widehat T_N^{\rm G}
 =-\frac{255\sqrt2}{8}\sqrt N+O(\log N),\qquad
 (\widehat T_N^{\rm G})^{1/N}\longrightarrow1. \tag{1}
\]
The constants are fixed at the unchanged center, and the statement assumes \((|b|,|h_1|)\ne(0,0)\). Explicit two-sided bounds and a sufficient degree rule are proved below. The payment improves R7 at degree four, but the old Cauchy payment decays geometrically and is **eventually strictly smaller**. At the existing positive point the largest possible further direct-margin improvement is less than **0.012%** of its accepted lower margin. No new source values or degree sweep are needed to decide this question.

This is a sufficient error estimate and a scoped efficiency comparison, not an RH-equivalent reformulation or a new coverage theorem. It does not establish a signed source lower bound, remove the independent quadratic-time payment or repair center-discriminant degeneracy. No manuscript, snapshot or DRAFT_HISTORY milestone is requested. The accepted R7 proof and its editorial clarification remain unchanged.

## 1. Fixed source, exact row, and the variable degree

Use the complete unit theta source and literal cosine of [Note26](26_ADAPTIVE_RADIUS_AND_PHASE_ALIGNED_IBP_B03_R5_20261030.md), the same drift and unit preparation, and
\[
 \tau=\tfrac14,\quad a=64,\quad R=\tfrac1{32},\quad r=\tfrac1{128},
 \quad T_0=\tfrac{17}{64}.
\]
Write \(t=T-\tau,x=A-a,h_j=\partial_A^jH(\tau,a),b=h_2,B=|b|,\eta=|h_1|\). The complete positive moment already acquired at 384 bits is
\[
 X_1=\int_0^\infty u e^{T_0u^2+4u}\Phi(u)\,du>0.
\]
It is distinct from the signed jet \(h_1\). Its single inherited enclosure is reused; this is not a two-precision reacquisition. Set
\[
 \Delta=T_0-\tau-r=r=\tfrac1{128},\quad
 \delta=4-r=\tfrac{511}{128},\quad
 \lambda=\delta-r=\tfrac{255}{64},\quad
 \beta=\lambda/\sqrt r=\tfrac{255\sqrt2}{8}.
 \tag{2}
\]

For \(N\ge1\), put \(n=N+1\), \(w=r(u^2+u)\) and \(s=(\tau+r)u^2+ru\). Define
\[
 p_{S,n}=\frac{w^n}{n!},\quad p_{h,n}=u p_{S,n},\quad
 p_{b,n}=2p_{S,n}+\frac{ruw^{n-1}}{(n-1)!}
 =\frac{r^n}{n!}u^n(1+u)^{n-1}(n+2+2u),
 \quad P_N=Bp_{b,n}+\eta p_{h,n}. \tag{3}
\]
These are exactly the requested family, with nonnegative coefficients and no constant term. Each of \(p_{b,n},p_{h,n}\) has \(n+1\) supported monomials. Their union has \(n+2\); the estimates below apply linearity to the two pieces separately.

The [R7 kernel proof](B03_R7_TAYLOR_SUBTRACTED_COMMON_MOMENT_BOUND_20261030.md) extends without changing its source: for \(E_j(z)=e^z-\sum_{k=0}^jz^k/k!\),
\[
 K_{>N}=\tfrac12\sum_{\sigma=\pm1}e^{\tau u^2+i\sigma au}
 \{(-2b+i\sigma h_1u)E_N(tu^2+i\sigma xu)
       +i\sigma bxu E_{N-1}(tu^2+i\sigma xu)\}.
 \tag{4}
\]
The discarded correction has parameter degree at most one, so (4) is valid for every \(N\ge1\). On the complex inner bidisk, \(|K_{>N}|\le e^sP_N\). Coefficientwise exponential majorization also proves
\[
 \sum_{m+\ell>N}|g_{m\ell}|r^{m+\ell}
 \le\int_0^\infty \Phi e^sP_N\,du. \tag{5}
\]
Indeed expand the two exponential tails in \(t,x\), take the sum of coefficient magnitudes at radius \(r\), then use \(|-2b+i\sigma h_1u|\le2B+\eta u\) and integrate. The positive resulting series is dominated by the displayed complete integral. Thus this pays the coefficient absolute tail as well as the function remainder. All mode and exterior contributions remain present.

The unchanged signed finite coefficients are
\[
 f_{m\ell}=\frac{(-1)^m h_{2m+\ell}}{m!\ell!},\quad
 q_{m\ell}=f_{m\ell}-p^{\rm heat}_{m\ell},\quad
 g_{m\ell}=b(\ell-2)q_{m\ell}+h_1(\ell+1)q_{m,\ell+1},
\]
where the heat polynomial is \(h_0+h_1x+b(x^2/2-t)\). The full signed products are formed before taking absolute values. A general degree still requires its finite jets through \(h_{2N+1}\); the tail theorem does not acquire missing jets.

## 2. Explicit optimizer and complete-moment payment

For integers \(m\ge0\) define
\[
 u_0=0,\quad M_0=1,\qquad
 u_m=\frac{\sqrt{\delta^2+8rm}-\delta}{4r}
     =\frac{2m}{\sqrt{\delta^2+8rm}+\delta},\quad
 M_m=u_m^m e^{-ru_m^2-\delta u_m}\quad(m\ge1).
 \tag{6}
\]
For \(m=0\), the endpoint value is defined directly, without using an undefined \(0^0\). For \(m>0\), the logarithmic derivative of \(u^m e^{-ru^2-\delta u}\) is \(m/u-2ru-\delta\), strictly decreasing through zero. Its unique maximizer is (6); both endpoints give zero. Therefore
\[
 M_m=\max_{u\ge0}u^m e^{-ru^2-\delta u}.
\]
This is an evaluated elementary expression, not an unevaluated supremum.

For a nonnegative-coefficient polynomial \(Q(u)=\sum_{k\ge1}q_ku^k\), set
\[
 \mathcal G(Q)=\sum_{k\ge1}q_kM_{k-1}.
\]
Pointwise, \(e^sQ\le u e^{T_0u^2+4u}\mathcal G(Q)\) for \(u>0\); the endpoint follows by continuity. Multiplying by \(\Phi\) and integrating gives
\[
 \boxed{\int_0^\infty\Phi e^sQ\,du\le X_1\mathcal G(Q),\qquad
 \widehat T_N^{\rm G}=X_1\{B\mathcal G(p_{b,n})+
                                     \eta\mathcal G(p_{h,n})\}.} \tag{7}
\]
Every term is explicitly computable from factorials, binomial coefficients, square roots and exponentials. In particular
\[
 \mathcal G(p_{S,n})=\frac{r^n}{n!}\sum_{j=0}^n\binom njM_{n+j-1},\quad
 \mathcal G(p_{h,n})=\frac{r^n}{n!}\sum_{j=0}^n\binom njM_{n+j},
\]
\[
 \mathcal G(p_{b,n})=2\mathcal G(p_{S,n})+
 \frac{r^n}{(n-1)!}\sum_{j=0}^{n-1}\binom{n-1}jM_{n+j-1}. \tag{8}
\]
There are only linearly many terms in (8), although acquiring the signed finite polynomial is a separate cost. Do not apply an additional Cauchy factor to (7).

R7's \(\mathcal C(Q)=\sum q_k(k-1)!/\delta^{k-1}\) discarded the Gaussian. For \(m\ge1\), \(M_m<m!/\delta^m\), by the exponential-series bound and the strictly retained Gaussian at the positive maximizer; \(M_0=1\). Consequently \(\mathcal G(P_N)<\mathcal C(P_N)\) for a nonzero row. In contrast the R7 general-degree extension itself diverges: its highest monomials contain \(r^n(2n)!/(n!\delta^{2n})\) in the \(\eta\) part, or \(2r^n(2n-1)!/(n!\delta^{2n-1})\) in the \(B\) part; their successive ratios tend to infinity. This failure is only of that discarded-Gaussian payment.

## 3. Full-polynomial two-sided degree bounds

Assume \(B+\eta>0\), and introduce positive explicit constants
\[
 L=X_1 e^{\delta/2-r/4-1}(1-r/4)(rB+\eta),\qquad
 K=X_1 e^{\delta^2/(4r)}[(1+2r)B+\eta].
 \tag{9}
\]
For every \(N\ge1\),
\[
 \boxed{\frac{L}{N+1}e^{-\beta\sqrt{N+1}}
 \le\widehat T_N^{\rm G}
 \le K(N+2)e^{-\beta\sqrt N}.} \tag{10}
\]
The upper constant is intentionally coarse; (8), not (10), is the useful formula for a particular finite payment. The lower bound is a lower bound on this *paid allowance*, not on the true signed remainder.

**Upper bound.** For a nonnegative polynomial with \(d\) supported monomials,
\[
 \sup_{u>0}(Q/u)e^{-ru^2-\delta u}
 \le\mathcal G(Q)\le
 d\sup_{u>0}(Q/u)e^{-ru^2-\delta u}. \tag{11}
\]
Each monomial maximum is bounded by the maximum of the sum. This step explicitly controls the entire polynomial rather than inferring its behavior from a leading monomial.

Write \(v=u+1/2\) and \(A=e^{\delta/2-r/4}\). Then
\[
 u(u+1)=v^2-1/4\le v^2,\quad
 e^{-ru^2-\delta u}=A e^{-rv^2-\lambda v}.
\]
Hence the two functions in (11) are bounded by
\[
 A\frac{r^n}{n!}v^{2n}e^{-rv^2-\lambda v}
 \quad(p_{h,n}),
\qquad
 A\frac{r^n}{n!}v^{2n-2}(n+1+2v)e^{-rv^2-\lambda v}
 \quad(p_{b,n}). \tag{12}
\]
For integers \(j\ge1\), \(y=v/\sqrt{j/r}\), and \(j!\ge(j/e)^j\),
\[
 \frac{r^jv^{2j}}{j!}e^{-rv^2-\lambda v}
 \le e^{-r(v-\sqrt{j/r})^2-\lambda v}
 \le e^{\lambda^2/(4r)-\beta\sqrt j}. \tag{13}
\]
The first inequality uses \(\log y\le y-1\); the second completes the square. For the second expression in (12), use
\(2v^{2n-1}\le v^{2n-2}+v^{2n}\). Apply (13) at \(j=n-1,n\) and use \(r^n/n!=(r/n)r^{n-1}/(n-1)!\). Its bound is
\[
 A e^{\lambda^2/(4r)}
 [1+r(n+2)/n]e^{-\beta\sqrt{n-1}}
 \le A e^{\lambda^2/(4r)}(1+2r)e^{-\beta\sqrt{n-1}},
\]
because \(n\ge2\). Apply (11) with \(d=n+1\) separately to both polynomials. Finally \(A e^{\lambda^2/(4r)}=e^{\delta^2/(4r)}\), proving the upper half of (10).

**Lower bound.** Evaluate the left side of (11) at
\(v=\sqrt{n/r}\), \(u=\sqrt{n/r}-1/2>0\). For \(p_{h,n}\) the value is exactly
\[
 A\frac{(n-r/4)^n}{n!}e^{-n-\beta\sqrt n}.
\]
Integral comparison for \(\sum_{k=1}^n\log k\) gives
\(n!\le e n(n/e)^n\); Bernoulli's inequality gives
\((1-r/(4n))^n\ge1-r/4\). Thus this value is at least
\(A(1-r/4)e^{-\beta\sqrt n}/(en)\).
At the same point the ratio of the \(p_b\) function to the \(p_h\) function is
\[
 \frac2u+\frac{n}{u(u+1)}\ge r,
\]
since \(u(u+1)=n/r-1/4\). Linearity of \(\mathcal G\) and (11) prove the lower half of (10). Both bounds apply to the full polynomial with either \(B\) or \(\eta\) zero.

Taking logarithms in (10) proves (1), including its exact square-root exponent. In particular this is not a geometric rate. For any target \(\varepsilon>0\), a sufficient explicit rule is
\[
 N\ge\max\left\{1,\left\lceil
 \left(\frac2\beta\max\{0,\log(K/\varepsilon)\}\right)^2
 \right\rceil\right\}. \tag{14}
\]
Indeed \(N+2\le e^{2\sqrt N}\le e^{\beta\sqrt N/2}\) for \(N\ge1\), since \(\beta>4\). Thus the upper bound is at most \(K e^{-\beta\sqrt N/2}\). For fixed source inputs, the two sides of (10) show that the degree required to make this payment at most \(\varepsilon\) has order \((\log(1/\varepsilon))^2\). This is a degree law for the allowance, not an operation count for source acquisition or a frequency-coverage law.

## 4. Tail monotonicity proved; final-margin monotonicity not imported

The exact selected tail is strictly decreasing with \(N\) for a nonzero row. Here is a proof specific to (7). The maximizers \(u_m\) increase with \(m\), and
\[
 M_{m+j}\le u_{m+j}^{\,j}M_m\quad(j=1,2).
\]
For a polynomial whose monomials in \(\mathcal G\) have indices \(m\le2n\), multiplication by \(w/(n+1)\) decreases its \(\mathcal G\)-value by a factor at most
\[
 \frac{r(u_{2n+2}^2+u_{2n+1})}{n+1}
 \le1-\frac{(\delta/2-r)u_{2n+2}}{n+1}<1. \tag{15}
\]
Use \(2ru_{2n+2}^2+\delta u_{2n+2}=2n+2\) and \(\delta>2r\). This applies to \(p_S\) and \(p_h\) from \(n\) to \(n+1\). For the other part \(ruw^{n-1}/(n-1)!\), the multiplier is \(w/n\) and its maximal index is \(2n-2\); the same calculation uses \(u_{2n},u_{2n-1}\) and denominator \(n\). Its value also strictly decreases. Add the nonnegative pieces.

This proves monotonicity of **the tail alone**. The new finite sum grows with degree; no monotonicity of \(F_N+\widehat T_N^{\rm G}\) or \(d_N^{\rm G}\) is claimed. R5's Cauchy proof of that different monotonicity is not imported.

## 5. Primitive and direct comparisons

For \(N\ge1\), (4) vanishes to order at least two in \(u\), so the exact lower primitive boundary vanishes. Complete theta decay pays infinity; at a finite cutoff the R7 joint boundary and original exterior must still be retained. Differentiating the analytic exponential series gives, just as in R7,
\[
 |(K_{>N})_{uu}-K_{>N}|\le e^s\mathscr L P_N,\quad
 \mathscr LQ=Q''+2(D+a)Q'+[(D+a)^2+2r+1/2]Q,
 \quad D=2(\tau+r)u+r.
\]
For general \(B,\eta\), paying this polynomial with \(X_1\mathcal G\) requires **\(N\ge2\)**: \(\mathscr Lp_b\) then has no constant term. At \(N=1\) it generally has a positive constant term, whose ratio to the moment's factor \(u\) is unbounded at zero. The direct bound has no such restriction. This is a limitation of this primitive moment payment, not a failure of the primitive identity.

For \(N\ge2\), the inherited termwise \(\psi<\Phi/9\) gives
\[
 \widehat T_N^{\rm P,G}=\frac{X_1}{72}\mathcal G(\mathscr LP_N)
 \ge\frac{a^2}{72}\widehat T_N^{\rm G}
 =\frac{512}{9}\widehat T_N^{\rm G}>\widehat T_N^{\rm G}. \tag{16}
\]
The comparison uses coefficientwise \(\mathscr LP_N\ge a^2P_N\). Separately, for the exact polynomial-envelope integrals the R7 identity extends to
\[
 \frac18\int\psi e^s\mathscr LP_N-\int\Phi e^sP_N
 =\frac18\int\psi e^s[2aP_N'+(2aD+a^2+1)P_N]>0.
\]
These two comparisons have different objects. Neither rejects other primitive estimates or signed integration.

## 6. Final paid allowance and comparison with Cauchy

Keep all three independent ingredients explicit:
\[
 F_N=\sum_{1\le m+\ell\le N}|g_{m\ell}|r^{m+\ell},\quad
 D_0=h_1^2-2bh_0,\quad
 d_N^{\rm G}=|D_0|-2b^2r-F_N-\widehat T_N^{\rm G}.
 \tag{17}
\]
When this is positive, the inherited coefficient is exactly
\(c_N^{\rm G}=d_N^{\rm G}/(1+h_0^2+h_1^2+b^2)\); the physical row gives
\[
 |(H,H_A)|\ge\frac{d_N^{\rm G}}
 {\sqrt{4b^2+(|h_1|+r|b|)^2}}.
\]
The identically informed direct first-jet strip has this same information and at least this margin. The spatial flow adds no source separation. The matched scalar Taylor consumers use \(X_1\mathcal G(p_{S,n})\) and \(X_1\mathcal G(p_{h,n})\), respectively, with their own signed degree-\(N\) polynomials (the \(H_A\) polynomial is formed separately).

Let \(M_C>0\) be the unchanged accepted complete-source outer C envelope from R5. Its payment is
\[
 T_N^{\rm C}=M_C\frac{q^{N+1}[(N+2)-(N+1)q]}{(1-q)^2},
 \qquad q=r/R=1/4. \tag{18}
\]
With the same \(F_N\), equations (10) and (18) prove
\[
 \log\frac{\widehat T_N^{\rm G}}{T_N^{\rm C}}
 =N\log4-\beta\sqrt N+O(\log N)\longrightarrow+\infty.
 \tag{19}
\]
Thus Cauchy eventually gives a strictly smaller **final allowance** and a strictly larger \(d_N\). No crossover degree is computed or needed. A minimum of the two tails is valid but only guarantees nonworsening; it does not establish a new useful strict gain or acquisition saving. If \(B=\eta=0\), both rows and \(D_0\) vanish, so no positive certificate results; (1)/(19) are not asserted for that zero case.

At \(N=4\), \(\mathcal G<\mathcal C\) and the accepted [E02 R7 assessment](../../reviews/fixed_coefficient_parameter_geometry/E02_R7_TAYLOR_SUBTRACTED_ASSESSMENT_20261030.md) already imply
\[
 d_4^{\rm G}>d_4^{\rm R7}>1.89988\,10^{-19},\qquad
 0<d_4^{\rm G}-d_4^{\rm R7}<\widehat T_4^{\rm R7}<2.153\,10^{-23}.
 \tag{20}
\]
The improvement is less than \(0.012\%\) of the accepted lower margin. Old C degree four is negative; its saved degree-eight case is positive. R8 preserves that finite comparison but adds no new certified point. The same-information R7 scalar floors remain positive and can only improve: \(|H|>6.38928\,10^{-10}\), \(|H_A|>4.17477\,10^{-10}\). Therefore the example still exercises no simple-zero crossing. We have not computed a new \(\mathcal G\) value or a new flow/C01 constant; the new insight is its analytical degree law.

## 7. What convergence cannot supply

Analyticity and the existing outer Cauchy bound imply
\(F_\infty=\sum_{m+\ell\ge1}|g_{m\ell}|r^{m+\ell}<\infty\).
By (5)/(7), \(0\le F_\infty-F_N\le\widehat T_N^{\rm G}\), and
\[
 d_N^{\rm G}\longrightarrow
 d_\infty=|D_0|-2b^2r-F_\infty. \tag{21}
\]
Both Cauchy and Gaussian payments approach this same limit. If the limit is positive then sufficiently large degrees pass; if it is nonpositive then every \(d_N^{\rm G}\le d_\infty\le0\). Equation (21) describes the obligation; it is not a claim that the limit is positive or a new criterion to support by sampling.

A useful regional continuation needs an **independently derived quantitative signed-source lower bound** that pays the coefficient variation and the time cost on a declared domain, with explicit radius/degree choices and transfer to the intended target. For example, a proved lower bound for \(|D_0|-2b^2r\), together with a proved smaller bound for \(F_\infty\) or a finite signed sum plus its complete tail, would suffice. No such uniform gap is acquired here. It cannot be defined as an unknown positive regional minimum. If \(D_0=0\) the current certificate fails for every \(N\); even before paying \(F_N\), \(|D_0|>2b^2r\) is necessary. Faster tail convergence changes none of these dependencies.

For each fixed degree the positive constants in (7) are frequency independent. The accepted R7 linear-budget versus quadratic-discriminant argument therefore still gives eventual high-frequency rejection for this fixed-radius, fixed-degree rule. This does not contradict degree convergence, which fixes the center first. No statement uniform in degree or frequency, efficient adaptive cover, or actual theta collision follows.

## 8. Controls, status, and continuation

The compression is generic for positive sources with the stated moment. It does not itself distinguish theta from a colliding control. On any admissible event-containing ball, the exact row forces every valid positive-margin test to fail at the control's collision; an upper moment bound can hold while the signed gap in (17) fails. Use each control's own source, moment domain and event location.

The [control register](../../../../../result-summaries/12_collision_controls_and_screening.md) supplies the screens: weighted-square and finite-prime controls fail full theta reflection/unit coefficients; Euler-factor sources alter the arithmetic, and their negative-Laguerre witnesses alone do not locate collision balls; reflected, smooth-shape and positive-primitive controls lack theta's complete square arithmetic; Gaussian-polynomial controls are not the unit theta source. Atomic/finite-profile controls need their own admissible source/primitive domain and fail the stated full-profile or eventual-simplicity inputs. Conditional endpoint controls retain their RH assumption and arithmetic failure. Changed observation kernels fail literal cosine/Newman reconstruction; relaxed profiles are not physical events. Merely naming a failed theta identity does not make this generic upper bound discriminate those controls. No control datum is transferred to (1/4,64).

**B03 R8 analytical work is complete, with same-assistant checking; separate E02 R8 assessment is next.** The bounded result is convergence with a sharp stretched-exponential law and eventual inferiority to the existing geometric Cauchy allowance, while preserving a finite already-known certificate. No fresh acquisition packet is justified by the old point's negligible tail reduction. After assessment, a new B task must target a substantive signed source margin or a different declared information mechanism before coverage work; **B04 remains gated**.

See the [self-review](../../reviews/fixed_coefficient_parameter_geometry/B03_R8_GAUSSIAN_SLACK_SELF_REVIEW_20261030.md), [fixed assessment packet](../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R8_GAUSSIAN_SLACK_ASSESSMENT_20261030.md), and [continuation/model handoff](B03_R8_RETURN_AND_MODEL_HANDOFF_20261030.md). The small exact bookkeeping record verifies inherited hashes, rational constants and saved R7 inequalities; it does not prove an infinite-degree theorem by sampling.

Follow the [result index](../../../../../result-summaries/README.md), particularly [theta bookkeeping](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../avoid/README.md): [target classification](../../../../../avoid/01_restating_the_target.md), [control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [shared-premise review](../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [numerics after the question](../../../../../avoid/10_numerics_ahead_of_the_question.md), [separate bounds](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [noncircular constants](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md).
