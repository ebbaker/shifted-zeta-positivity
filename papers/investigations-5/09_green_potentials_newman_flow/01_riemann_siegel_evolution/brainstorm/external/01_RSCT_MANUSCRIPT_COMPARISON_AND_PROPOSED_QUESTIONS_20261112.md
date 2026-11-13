# Returning to Green potentials after the RSCT analytical synthesis

12 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0004, actual title “Review RSCT research status.” The recorded configuration does not identify the actual backend model or reasoning effort; neither is inferred.

**Status: rewritten comparison and proposed research questions, not a new theorem or an executed transfer.** This is the current version of the [earlier RSCT discussion](../../../../10_riemann_siegel_critical_time/brainstorm/notes/11_RSCT_TO_GREEN_TOOL_TRANSFER_DISCUSSION_20261112.md), now placed in GNP-RS’s requested external brainstorm folder. The earlier note remains a historical record. The chat remains registered in [RSCT chat-histories](../../../../10_riemann_siegel_critical_time/chat-histories/README.md).

The new reference is **Riemann–Siegel analysis at a possible positive Newman threshold: Complete local approximation, signed zero measurements, and the limits of calibrated phase constraints**, drafted for Edward Baker, 12 November 2026:

- [Compiled manuscript, outside the repository](/private/tmp/rsct-manuscript-20261112/riemann_siegel_critical_time.pdf).
- [Editable manuscript and build guide](../../../../10_riemann_siegel_critical_time/manuscript/README.md), with [main TeX source](../../../../10_riemann_siegel_critical_time/manuscript/main.tex).
- [Sources and evidence crosswalk](../../../../10_riemann_siegel_critical_time/manuscript/SOURCES.md).

The PDF is a regenerable temporary reading copy. The sources and build guide are the durable repository record. The manuscript preserves R1–R9’s original evidence levels; it is not an independent audit of the inherited HDA approximation theorem.

The [result index](../../../../../../result-summaries/README.md), particularly [heat-flow cluster11](../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md) and [collision controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../../avoid/README.md) govern this comparison. The specific rules are [classify quantitative milestones](../../../../../../avoid/01_restating_the_target.md), [screen shared premises](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [keep exclusions scoped](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [retain signed correlations](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## Assessment: prioritize the actual Green observable

Returning to 09 is reasonable because its RS child has an analytical theorem about the **actual canonical Green value**, with a concrete next question about quantitative strength. RSCT now has a coherent acquisition theory and a useful account of why several proposed sign arguments fail. It has not obtained the favorable canonical sign needed for collision exclusion.

This is a judgment about the available intermediate work, not a judgment that 09 is close to proving RH.

| Issue | GNP-RS, investigation 09 | RSCT, investigation 10 |
| --- | --- | --- |
| Actual quantity controlled | Dyadic means of the canonical Green value at moving time \(1/L_X\) | Complete local field and its derivatives, with a paid absolute error in the signed Poisson expression |
| Strongest positive analytical acquisition | Every fixed positive power mean tends to zero; exponential means below four tend to one | \(O(a^{-3/4})\) local analytic error, event subtraction, coefficient moments, fourth-jet payment |
| Current obstruction | The complete arithmetic residual at exceptional centers; no quantitative growing-cutoff mean yet | The actual correlated phase sign; increasingly constrained artificial phases still permit the collision-compatible sign |
| Natural next question | Make the fixed-reference mean quantitative in a growing cutoff | Identify a canonical constraint absent from the joint calibrated construction |
| What neither branch supplies | An every-center exclusion or a complete positive-threshold contradiction | An every-center exclusion or a complete positive-threshold contradiction |

For \(L_X=\log(X/(4\pi))\), [GNP-RS Note19](../../notes/19_GNP_RS_MANUSCRIPT_AND_AVERAGED_GREEN_VALUES_20261111.md) proves from its named inherited inputs
\[
\frac1U\int_U^{2U}J_{1/L_X}(X)^p\,dX\longrightarrow0
\qquad(p>0\ \text{fixed}),
\]
\[
\frac1U\int_U^{2U}e^{\alpha J_{1/L_X}(X)}\,dX\longrightarrow1
\qquad(0<\alpha<4\ \text{fixed}),
\]
and an eventual upper bound \(39\) for the fourth exponential mean. Convergence at exponent four is not proved. Its status is **proved in-note from the named inherited inputs; same-assistant self-check only**.

The time depends on the outer center \(X\), while remaining fixed inside each spatial integral. These results are at \(c=1\), have no rate, and do not imply fixed-time or every-center statements. Rare exceptional centers remain possible.

There is also a geometric limit to what the Green value can detect. With zeros \(x_j+iy_j\) in the upper half-strip,
\[
J_T(X)=\sum_{y_j>0}\operatorname{atanh}
\frac{\sin(\pi y_j/8)}{\cosh(\pi(X-x_j)/8)}\ge0.
\]
At an all-real threshold, \(J_\Lambda(X)=0\) for every \(X\), including at a multiple real zero. This is already established in [Note20](../../notes/20_GNP_RS_GREEN_GEOMETRY_AND_CRITICAL_TIME_20261111.md). A small threshold Green value alone does not exclude the event.

## What the RSCT manuscript contributes

The manuscript develops three reusable components, with different purposes.

**1. Complete local acquisition.** [Section 5](../../../../10_riemann_siegel_critical_time/manuscript/sections/04_microscopic_acquisition.tex), especially Theorem 5.2, writes
\[
z=a+w/L,\qquad
f_a(w)=H_T(a+w/L)/A(T,a+w/L),\qquad q_a=P_a+K_a,
\]
and pays the analytic error and fixed derivatives through order four by \(O_R(a^{-3/4})\). The full reflected sum and exact-gamma correction remain present. At an actual event,
\[
S_a=q_a-q_a(0)-wq_a'(0),\qquad
f_a-S_a=O_R(a^{-3/4}|w|^2).
\]
Proposition 5.4 pays the resulting signed-expression error. This is useful approximation and error propagation; it does not give a logarithmic floor or a favorable arithmetic value.

**2. Explicit dependence on a growing prime set.** [Section 7](../../../../10_riemann_siegel_critical_time/manuscript/sections/06_multiplicative_calibration.tex), Theorem 7.1 and Corollary 7.3, exposes the calibration cost
\[
C_{\mathcal Q}=\prod_{p\in\mathcal Q}(1-p^{-1/2})^{-1},
\qquad
\mathcal E_{\mathcal Q}=\frac{C_{\mathcal Q}L^4}{W},
\qquad
W\asymp\frac{e^{(1/4-c/16)L}}L.
\]
Only after proving uniform estimates does it allow \(\mathcal Q\) to grow. The sufficient range
\[
Y=\gamma L^2(\log L)^2,\qquad 0<\gamma<9/256,
\]
comes from \(\log C_{\{p\le Y\}}=(\sqrt\gamma+o(1))L\). The transferable practice is to expose every parameter dependence before exchanging a fixed-parameter limit for a growing-parameter assertion. This particular cost is specific to the auxiliary phase construction; it is not automatically a bound for GNP’s actual-height moments.

**3. Strong calibrated controls.** [Section 8](../../../../10_riemann_siegel_critical_time/manuscript/sections/07_mirror_jet.tex), Theorem 8.1, constructs one complete model retaining exact magnitudes, multiplicativity, actual leading phase, the correction, actual prime phases through \(Y\), and both event equations. At that same point,
\[
\mathcal D_a(q_*)\le-\kappa_\beta
 \frac{e^{(1/2-c/8)L}}{L^8},
\qquad
\mathcal J_a(q_*)\ge c_J
 \frac{e^{(1/2-c/8)L}}{L^8}>0.
\]
The second expression is the normalized necessary forced-mirror fourth-jet condition. This gives a useful test of an estimate based only on those data. The model explicitly disagrees with the actual phase at a prime beyond \(Y\), and no global all-real canonical field is constructed.

The threshold \(Y\) eventually exceeds GNP’s selected cutoff \(L^2\). That does **not** show failure of GNP’s adaptive reference: the local Poisson expression and the integrated Green logarithm are different functionals, and seven local observations are not a complete growing spatial window. An obstruction for GNP would require evaluating its exact residual or signed logarithmic expression on the same model with all window costs paid.

## Proposed first question: a quantitative residual mean with growing cutoff

Keep GNP’s strip \(0<\Im z<8\), its carrier \(C_-\), and
\[
K(t)=\frac1{16\cosh(\pi t/8)},\qquad
W_X=[X-(32/\pi)\log X,\ X+(32/\pi)\log X].
\]
At \(T=c/L_X\), set \(\sigma_c=1/2+c/4\),
\(\nu_T(x)=x/2+\pi T/8\), \(\phi_T(x)=2\Theta(T,x)\), and
\[
E_P(x)=\prod_{p\le P}
 \left(1-p^{-\sigma_c}e^{i\nu_T(x)\log p}\right)^{-1},
\qquad V_T=H_T/C_-.
\]
The complete normalized residual is
\[
R_P(X,c)=
\int_{W_X}K(x-X)
\frac{\left|V_T(x)-E_P(x)-e^{i\phi_T(x)}
                       \overline{E_P(x)}\right|^2}
{|E_P(x)|^2}\,dx.
\]
Physical time and reference cutoff stay fixed in each spatial integral.

[E05, Note14](../../notes/14_GNP_RS_E05_FINITE_EULER_RESIDUAL_20261111.md) proves, with \(P\) fixed during \(U\to\infty\),
\[
\frac1U\int_U^{2U}R_P(X,1)\,dX\longrightarrow
\mu_P=\zeta(3/2)\prod_{p\le P}(1-p^{-3/2})-1,
\qquad \mu_P\to0.
\]
[E06, Note17](../../notes/17_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_20261111.md) separately pays the comparison overhead for \(P(X)=\lfloor L_X^2\rfloor\): its joint phase cost is at most \(18/L_X\), uniformly over \(c\in[1/2,1]\) and the positive regulator. The remaining omitted-prime, exterior and complete-field comparison costs are also paid there. The actual adaptive residual is still unestimated at every center.

**Proposed question.** Can the canonical moment proof be made quantitative in \(P\), giving
\[
\left|\frac1U\int_U^{2U}R_P(X,1)\,dX-\mu_P\right|
\le \varepsilon(U,P),
\]
with a proved bound that tends to zero for a declared growing choice \(P=P_U\), ideally of order \((\log U)^2\)?

This is an **unproved quantitative milestone**, classified under avoid01, not an RH-equivalent criterion. No rate or growing-cutoff bound is acquired by writing the display. The first reviewable output would be a dependence ledger and a bound for \(\varepsilon\), or a precise obstruction to that bound.

A systematic attempt should retain the complete E05 proof and account for:

1. The size and reciprocal size of the finite Euler reference, with every dependence on \(P\) visible.
2. The complete oscillatory cross terms and any loss caused by the growing population.
3. The moving outer time \(1/L_X\), with time held fixed inside each spatial window.
4. Spatial and height endpoints, tails, normalization, and the full reflected correction.
5. The distinction between a cutoff fixed across a dyadic block and the original center-dependent \(P(X)\).

A theorem with \(P_U\) constant on each block is already a meaningful intermediate result. Uniform estimates for constant choices of \(P\) do not by themselves justify choosing \(P(X)\) inside the integral; that needs a direct proof or an additional comparison. Even a successful quantitative mean permits sparse exceptional centers and does not solve the parent’s separate time-zero signed-log problem.

## Proposed second question: local RS errors in existing deflation

The normalization conversion is exact:
\[
C_-=(A/2)e^{-i\Theta},\qquad
V=2e^{i\Theta}f_a.
\]
Thus RSCT Theorem 5.2 can be compared directly with GNP’s local field normalization. The shared approximation provider still belongs to HDA/GNP-RS; RSCT does not claim ownership of it.

The [parent’s deflation section](../../../manuscript/sections/09_deflation.tex) already contains stable divided differences, root-log integration and conditional regular-factor floors. A possible bounded transfer would attach RSCT’s microscopic analytic error to a specified instance of that existing construction.

For an actual order-\(m\) zero, \(f(w)=w^m g(w)\) gives
\[
\log|f(w)|=m\log|w|+\log|g(w)|.
\]
The remaining obligations are an actual divisor with a complete root count, a lower bound for the regular factor \(g\), and the derivatives required by the chosen error ledger. Small additive error in \(f\) alone does not control \(\log|g|\).

In particular, the parent’s approximate-knot estimate through second factor derivatives needs derivatives through order \(n+3\). For a pair of roots this includes order five, beyond RSCT’s explicitly paid four. A larger analytic disk suggests the Cauchy step, but the fifth-derivative bound and its constants must be written when used.

A fixed scaled disk covers a physical radius \(O(1/L)\), not the entire \(O(\log X)\) Green window. Covering that window requires compatible charts, a fixed physical time, and cutoff/correction accounting. Keep the existing Green strip and outer Euler baseline: shrinking the entire strip would move the ordinary-zeta comparison toward \(\Re s=1/2+c/4<1\), where that absolute-convergence argument no longer applies.

This transfer is worth pursuing only after selecting a concrete local consumer and identifying the divisor/floor input. Event subtraction cannot be imposed at arbitrary Green centers.

## Control screen and disposition

The proposed residual-mean question uses canonical moment inputs beyond generic positivity. The [control catalog](../../../../../../result-summaries/12_collision_controls_and_screening.md) is screened analytically, with no historical numerical certificate rerun:

| Control family | Premise absent from the unchanged canonical application |
| --- | --- |
| Euler-factor and translated sources | Unmodified coefficients, completion and prime subtraction |
| Weighted squares, finite tails and finite-prime orbits | Full source or reflection; a local collision is not automatically an all-real threshold |
| Reflected super-Gaussian, smooth and positive-primitive sources | Complete theta square-series arithmetic |
| Atomic, finite-profile and compact continuous thresholds | Full canonical profile and the actual coherent/residual mean laws |
| Conditional endpoint controls | Their conditional time-zero premise remains; ordinary Dirichlet arithmetic fails |
| Variable-readout and counter-kernel constructions | Literal cosine readout, full source or physical generator |
| Relaxed Green profiles | Exact integer zero measure and simultaneous full boundary-field identification |
| RSCT’s calibrated multiplicative point | Actual same-height phase trajectory; no complete Green-window law or global all-real field is established |

A mean theorem can coexist with isolated collisions. A missing premise is not a claim that every control violates the proposed mean law. The local-deflation question separately requires an actual divisor and a regular-factor floor; none of the generic shape controls supplies those canonical data.

**Recommendation for discussion:** prioritize the quantitative growing-cutoff mean question in 09. Retain RSCT’s local approximation and calibrated controls as supporting tools, with the local-deflation transfer conditional on a concrete consumer. The fixed-height matrix and another generic mirror inequality are lower priorities: they do not supply the missing signed boundary logarithm.

No research task is activated by this note. The [GNP register](../../../research-progress/01_GNP_RESEARCH_PROGRESS_20261110.md), [GNP-RS register](../../research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md), and [RSCT register](../../../../10_riemann_siegel_critical_time/research-progress/01_RSCT_RESEARCH_PROGRESS_20261111.md) retain their current statuses. The new RSCT manuscript is an analytical synthesis milestone; the comparison and proposed transfers remain discussion.
