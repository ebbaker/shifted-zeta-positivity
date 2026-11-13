# Returning to Green potentials and reusing RSCT tools

**Historical version.** Rewritten after the analytical manuscript on 12 November 2026. Use the [current manuscript-linked comparison in GNP-RS](../../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/brainstorm/external/01_RSCT_MANUSCRIPT_COMPARISON_AND_PROPOSED_QUESTIONS_20261112.md) for ongoing discussion. This earlier version is retained without replacing its original scope or history.

12 November 2026, America/New_York. Discussion prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0004, actual title “Review RSCT research status.” The recorded model-configuration list is empty; actual backend model and reasoning effort are unavailable.

**Status: research-prioritization discussion and proposed intermediate questions, not a new proof or an executed port.** Investigation 09's current actual-Green mean theorem gives a reasonable basis for prioritizing its RS child. This is a judgment about available intermediate work, not evidence that it is close to proving RH. No task, manuscript change, numerical campaign, or investigation relocation is activated by this note. Existing status owners remain the [GNP register](../../../09_green_potentials_newman_flow/research-progress/01_GNP_RESEARCH_PROGRESS_20261110.md), [GNP-RS register](../../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md), and [RSCT register](../../research-progress/01_RSCT_RESEARCH_PROGRESS_20261111.md).

The [result index](../../../../../result-summaries/README.md), specifically [cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md) and [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../avoid/README.md), especially [classification01](../../../../../avoid/01_restating_the_target.md), [shared premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scoped exclusions07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [separate bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), govern the comparison. The proposed uniform mean below is an unproved quantitative milestone, not a target-equivalent criterion. No numerical checks are offered as evidence for an all-center conclusion.

## Why a return to 09 is reasonable

At \(L_X=\log(X/(4\pi))\), the [current E07 note](../../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/19_GNP_RS_MANUSCRIPT_AND_AVERAGED_GREEN_VALUES_20261111.md) proves from its named inherited inputs
\[
\frac1U\int_U^{2U}J_{1/L_X}(X)^p\,dX\longrightarrow0
\quad(p>0\text{ fixed}),
\]
and convergence of the exponential mean to one for each fixed exponent below four. Its evidence level is **proved in-note from the named inherited inputs; same-assistant self-check only**. This concerns the actual canonical Green observable. It has no rate, applies at \(c=1\), and samples different physical times as \(X\) varies. It supplies neither a fixed-time zero count nor a bound at every center. Sparse exceptional centers can survive every displayed mean conclusion.

By comparison, RSCT's latest results acquire local errors and rule out proposed lower bounds on carefully specified enlarged phase classes. Those are useful results, but a new favorable canonical sign has not been obtained. Returning to 09 would resume a branch with a positive theorem about its actual observable and identifiable questions about its quantitative strength. It would not remove 09's unresolved exceptional-center arithmetic.

The geometric distinction must remain explicit. With zeros \(x_j+iy_j\),
\[
J_T(X)=\sum_{y_j>0}\operatorname{atanh}
 \frac{\sin(\pi y_j/8)}{\cosh(\pi(X-x_j)/8)}\ge0.
\]
At an all-real threshold, \(J_\Lambda(X)=0\) for every \(X\), including when a multiple real zero exists. Thus a small or zero threshold Green value alone cannot exclude that event. [GNP-RS Note20](../../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/20_GNP_RS_GREEN_GEOMETRY_AND_CRITICAL_TIME_20261111.md) already establishes this distinction. The separate parent time-zero problem also remains open; the moving-time child theorem does not solve it.

## The most concrete transfer is growing-parameter bookkeeping

GNP-RS E05 proves, with \(P\) fixed while \(U\to\infty\),
\[
\frac1U\int_U^{2U}R_P(X,1)\,dX\longrightarrow
\mu_P:=\zeta(3/2)\prod_{p\le P}(1-p^{-3/2})-1,
\qquad \mu_P\to0\quad(P\to\infty).
\]
The exact complete residual is
\[
R_P(X,c)=\int_{W_X}K(x-X)
 \frac{|V_{c/L_X}(x)-E_P(x)-e^{i\phi_{c/L_X}(x)}\overline{E_P(x)}|^2}
 {|E_P(x)|^2}\,dx.
\]
Here \(W_X=[X-(32/\pi)\log X,X+(32/\pi)\log X]\); time and the chosen reference cutoff remain fixed inside each spatial integral. [E06](../../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/17_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_20261111.md) pays comparison overhead for \(P(X)=\lfloor L_X^2\rfloor\), including phase error at most \(18/L_X\), while leaving the actual adaptive residual unestimated at every center. Fixed-\(P\) means do not imply the required growing-\(P\) estimate.

RSCT [R8](../../notes/10_RSCT_B01_R8_GROWING_PRIME_CALIBRATION_20261111.md) addressed an analogous quantifier problem in a different construction: expose the complete dependence on a calibrated prime set, then prove a uniform budget before letting that set grow. Its factor
\[
C_{\mathcal Q}=\prod_{p\in\mathcal Q}(1-p^{-1/2})^{-1}
\]
and its particular sufficient budget belong to that phase-model construction. They cannot simply be inserted into GNP's actual-height moment proof.

The transferable method is the explicit tracking of parameter dependence. A concrete next question for 09 would be to write
\[
\frac1U\int_U^{2U}R_P(X,1)\,dX=\mu_P+E(U,P)
\]
and seek a proved error estimate valid for a declared growing range, ideally including \(P\) of order \((\log U)^2\). This is **a proposed quantitative question, not an acquired bound or ready execution packet**. It would require inspecting the canonical moment proof's dependence on the Euler product, oscillatory pairs, reference normalization, endpoints and tails. A cutoff fixed across a dyadic block but growing between blocks is already an intermediate gain. Passing from that version to the original center-dependent \(P(X)\) needs an additional comparison or a direct proof; even uniform fixed-cutoff means do not automatically permit a cutoff varying inside the height integral.

Such a result could support quantitative density or averaged-Green improvements. It would still permit rare bad centers. No rate, full-band extension, fixed-time statement, or every-center exclusion is claimed here. The option is attractive because its success would be measured by an actual error bound, not by another restatement of the desired sign.

## Two further tools worth retaining

**Local analytic approximation and error propagation.** RSCT [R4](../../notes/06_RSCT_B01_R4_MICROSCOPIC_EVENT_EXPANSION_20261111.md) and [R9](../../notes/11_RSCT_B01_R9_MIRROR_JET_COMPATIBILITY_20261111.md) provide the complete normalized local model on \(z=a+w/L\), with \(O(a^{-3/4})\) analytic error and explicit derivative payment through order four. Their nonvanishing carrier \(A\) and 09's carrier satisfy
\[
C_-=(A/2)e^{-i\Theta},\qquad V=H_T/C_-=2e^{i\Theta}(H_T/A).
\]
This identifies a compatible normalization; it does not transfer an unpaid logarithmic estimate. Both investigations inherit the complete evolved reflected representation and its remainder from [Polymath v2 §4](https://arxiv.org/html/1904.12438v2#S4) and the repository's later approximation inputs. RSCT's contribution to reuse is its local scaling, event subtraction and explicit product/derivative payments, not ownership of the original provider.

The local model may help a specified Green boundary-log or deflation calculation. If an actual order-\(m\) zero is known, writing \(f(w)=w^m g(w)\) separates \(\log|f|=m\log|w|+\log|g|\). The [parent deflation section](../../../09_green_potentials_newman_flow/manuscript/sections/09_deflation.tex) already has this general strategy, stable divided differences, root-log integrals and conditional contour floors. The proposed reuse would add the small-scale RS error estimates to that existing machinery.

Several premises remain: the required actual divisor/count, a lower bound for the regular factor, and every derivative needed by the chosen deflation ledger. In particular the parent's approximate-knot error estimate through second factor derivatives needs derivatives through \(n+3\); for a double-root pair this includes order five, beyond R9's explicitly paid four. The common larger analytic disk suggests how to pay a further fixed derivative, but that payment and its domain must be written down when used. Event subtraction is conditional on the actual event and cannot be imposed at arbitrary Green centers.

A fixed microscopic disk does not cover the full \(O(\log X)\) Green window. Patchwise reuse needs uniform estimates, fixed physical time, normalization conversion and cutoff/correction accounting. Shrinking the entire Green strip would also lose 09's existing outer Euler comparison: at microscopic imaginary height the formal shifted-zeta real part approaches \(1/2+c/4<1\). The intended reuse is local work on the boundary, with 09's strip and prime baseline retained. More accurate field evaluation alone does not estimate the residual above.

**Calibrated phase controls for testing proposed estimates.** R8–R9 retain all magnitudes, multiplicativity, actual prime phases through \(Y=\gamma L^2(\log L)^2\), fixed \(0<\gamma<9/256\), and, in R9, one mirror-jet condition, yet permit negative RSCT Poisson values. Eventually \(Y\) exceeds 09's chosen prime cutoff \(L^2\). This makes them useful tests of an argument that uses only prime calibration and generic algebraic constraints.

It does **not** prove failure of 09's adaptive Euler reference: \(D_a\) and the integrated logarithmic Green value are different functionals. R9 controls a fixed set of local observations, not 09's complete growing spatial window or its actual same-height orbit. To apply the construction as a Green-method obstruction one must evaluate the exact proposed Green or residual expression on the same model, with every window and error term included. Auxiliary independent-prime integration is not an actual-height average. Existing fixed-reference and tangent failures in 09 retain their original scope.

## Lower-priority transfers and control screen

RSCT's fixed-height matrix does not add a missing favorable bound to 09; 09 already controls its outer lines, while its difficult contribution is the signed real-boundary logarithm. The mirror inequality requires an all-real event and has no general converse. The denominator-free Poisson expression can be retained as a local diagnostic, but replacing the Green observable by it would return to RSCT's unproved sign problem. Ordinary positive-source geometry and additional finite constraints do not by themselves supply a new arithmetic input.

The analytical screen for the proposed uniform mean reuses [E07 §5](../../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/19_GNP_RS_MANUSCRIPT_AND_AVERAGED_GREEN_VALUES_20261111.md) and [RSCT R9 §5](../../notes/11_RSCT_B01_R9_MIRROR_JET_COMPATIBILITY_20261111.md): Euler/translated sources alter canonical coefficients and subtraction; weighted-square/finite-tail/finite-prime-orbit controls fail the full source and/or reflection; reflected/smooth/primitive controls fail complete theta arithmetic; atomic/finite-profile/continuous thresholds and counter-kernels fail the actual canonical moment/residual inputs and full profile; conditional endpoint controls retain their conditional premise and fail ordinary Dirichlet arithmetic; variable-readout controls fail the literal cosine/physical flow; relaxed Green profiles do not identify the exact integer zero multiset and full boundary field. R9's artificial multiplicative point fails the actual same-height orbit and has no established global all-real field. No controls are relocated to an unproved witness domain. A mean theorem may coexist with an isolated collision, so absent canonical premises are not claims that every control must violate the proposed mean law. No numerical control certificate was rerun.

**Discussion recommendation:** prioritize 09's actual-Green line of work; keep RSCT's local error estimates and phase controls as supporting tools. The most concrete first discussion is whether the fixed-reference moment proof can be made quantitative in a growing cutoff. The proof route is not yet established, and a successful average would leave the exceptional-center problem open. No research status is changed by this recommendation.

The existing chat stays in [RSCT chat-histories](../../chat-histories/README.md). The start-of-turn refresh verifies the preceding final reply and its completed turn. The current exact turn is `01a1d0ce-fdd8-76b0-8bf5-8f22d9bcf9f7`; its final capture is arranged only after completed public text is refreshed. Current capture metadata remain in the registry, not this note.
