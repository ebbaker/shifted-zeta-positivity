# Residual bounds from arbitrary anchors and compact sector edge extensions

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Authoring and reviewing model: **gpt-6-astra (Codex)**, actual reasoning effort **max**.

**Status: proved in-note from the stated inherited analytic estimates.** Proposition 1 gives an explicit bound for every subinterval of the existing UAR sector. Proposition 2 extends the coherent edge model and corrected-transition estimates to arbitrary fixed compact positive scaling bands, with constants and a small-time onset depending on the band. The second statement does not supply numerical values for that new onset. Neither result proves a physical lower margin or extends certified collision exclusion.

This is a continuation of [UAR-03][edge] and [UAR-04][increment], with the unchanged [UAR-01 contract][contract]. The [result summaries][results] and [patterns to avoid][avoid] apply, especially [signed recombination][a12], [scoped claims][a07] and [collision controls][controls]. Classification: quantitative approximation and residual estimates, not a new nonvanishing criterion. The associated [manuscript integration review][review] is internal self-review; no independent specialist validation is claimed.

## 1. Inherited quantities

Use the complete level-one theta source, its symmetric normalizer \(A\), phase \(\theta\), \(\omega=\theta_x<0\), analytic correction \(\widehat C_N^{\rm an}\), and

\[
f_N=(G_N-\widehat C_N^{\rm an})/A,\qquad
r_N=H/A-f_N,\qquad
Z_v=e^{-i\theta}(v-i v_x/\omega).
\]

The natural integer is \(N(x)=\lfloor\sqrt{x/(4\pi)+t/16}\rfloor\), with crossings \(\xi_n=4\pi(n^2-t/16)\). Put \(h_n=f_n-f_{n-1}\), so \(r_n-r_{n-1}=-h_n\). For fixed \(t\), the ordinary piecewise residual integral from \(a\) to \(b\) is denoted \(I_t(a,b)\). It is additive and changes sign when its endpoints are reversed. If \(a\leq b\),

\[
I_t(a,b)=i\left\{
Z_{r_{N(b)}}(b)-Z_{r_{N(a)}}(a)
+\sum_{a<\xi_n\leq b}Z_{h_n}(\xi_n)\right\}.                 \tag{1}
\]

Use the initial right chart at an initial crossing. At a terminal left description, omit the coincident switch and use the old chart; the value agrees. No delta mass is inserted into the ordinary integral.

Set

\[
L_x=\log(x/(4\pi)),\quad
S_x=e^{-3L_x/4-tL_x^2/16},\quad
Z_x=e^{-L_x/4-tL_x^2/16}.
\]

The scalar \(Z_x\) here is a positive envelope; \(Z_v\) is the rotating linear map. In the original sector \(0<t\leq1/20,\ 1\leq tL_x\leq2\), UAR-04 bounds the retained residual endpoint by \(1.53S_x\). Its remaining rotating endpoint errors are bounded by

\[
\Delta_x=160e^{L_x/4-tL_x^2/16}/x^2,\qquad
9\epsilon_x,\qquad \epsilon_x=1000Z_xe^{-3.99L_x}.
\]

The useful ratios are

\[
\Delta_x/S_x=(10/\pi^2)e^{-L_x}<2.1\,10^{-9},\qquad
\epsilon_x/S_x=1000e^{-3.49L_x}<5\,10^{-28}.                 \tag{2}
\]

These are inherited uniform bounds, not new physical observations.

## 2. An explicit estimate from any starting height

**Proposition 1.** For \(a,b\in J_t=[4\pi e^{1/t},4\pi e^{2/t}]\), \(0<t\leq1/20\), put \(a_*=\min(a,b)\). Then

\[
\boxed{|I_t(a,b)|<3.246\,S_{a_*}.}                          \tag{3}
\]

In particular, if \(a_*=4\pi e^{\kappa_*/t}\),

\[
|I_t(a,b)|<
3.246\exp\{-(\kappa_*^2+12\kappa_*)/(16t)\},
\qquad 1\leq\kappa_*\leq2.                                \tag{4}
\]

This improves the generic \(2\mathcal B(t)\) rebasing deduction by rerunning the estimating argument at the actual lower endpoint. The earlier \(2\mathcal B(t)\) payment was valid when only the original prefix theorem was used.

**Proof.** Assume \(a\leq b\). Let \(\delta=t/16\), \(U_x=\sqrt{x/(4\pi)+\delta}\), and

\[
\overline S(v)=
\exp\left\{-\frac{t\log^2(v^2-\delta)+12\log(v^2-\delta)}{16}\right\}.
\]

At each crossing, UAR-03 gives

\[
|Z_{h_n}(\xi_n)|<3Z_{\xi_n}/n^2
\leq 3\overline S(n)/n.                                  \tag{5}
\]

The last inequality uses \(\sqrt{n^2-\delta}\leq n\). Both \(\overline S(v)\) and \(3\overline S(v)/v\) decrease for \(v\geq U_a\). Also

\[
-\overline S'(v)=
\overline S(v)\frac{\{t\log(v^2-\delta)+6\}v}{4(v^2-\delta)}
\geq \frac{tL_a+6}{4}\frac{\overline S(v)}v.                \tag{6}
\]

Pay the first discrete term separately and bound the rest by an integral. With \(\beta_a=12/(tL_a+6)\), this gives, for every prefix from \(a\),

\[
\sum_{a<\xi_n\leq b}|Z_{h_n}(\xi_n)|
\leq \frac{3}{U_a}S_a+\beta_a(S_a-S_b).                    \tag{7}
\]

The estimate remains valid with no crossings. A coincident terminal switch can only be removed under the left description; the residual endpoint in (1) changes with it.

Apply the retained endpoint bounds to the already assembled expression (1). With \(C=1.53\),

\[
|\widehat\Xi(a,b)|
\leq(C+\beta_a+3/U_a)S_a+(C-\beta_a)S_b
\leq\{C+\max(C,\beta_a)+3/U_a\}S_a.                        \tag{8}
\]

Here \(\beta_a\leq12/7\) and \(3/U_a<3e^{-10}<.000137\). Thus

\[
|\widehat\Xi(a,b)|<
(1.53+12/7+.000137)S_a<3.245S_a.                          \tag{9}
\]

Both remaining endpoint errors decrease with height. Even using UAR-04's deliberately redundant edge payment, they cost at most

\[
2\Delta_a+36\epsilon_a
<(4.2\,10^{-9}+1.8\,10^{-26})S_a.
\]

Adding this to (9) proves (3). Reversing the endpoints proves the general case. Equation (4) is substitution, not extrapolation. QED.

The dependence on the starting height matters more than the small coefficient refinement in (8). At \(t=.05\), a subinterval beginning at \(4\pi e^{30}\) has bound below \(3.3\,10^{-11}\), whereas the original sector-wide ceiling is \(2.846\,10^{-7}\). These are different subinterval contracts; the comparison expresses the decaying envelope, not a measured error ratio.

There is still no physical exclusion from (3) alone. The actual anchor, the complete signed change of \(f_N\), its transitions and the physical normalization remain necessary. On the UAR-05 box there are no interior crossings, and the existing two-endpoint residual payment is stronger than this general crossing allowance. Consequently this corollary does not reverse [UAR-06's matched comparison][consumer] or reopen its stopped configuration.

## 3. Coherent edge models on other compact scaling bands

The upper value \(\kappa=2\) enters UAR-03 partly through the common truncation lengths. That numerical choice is not essential to the compact-contour construction.

Fix

\[
0<\kappa_-\leq\kappa_+<\infty,\qquad p>0,\qquad0<\eta<p.
\]

Use the same \(A,\widehat C_N^{\rm an}\), exact heat edge, and reflected channels as UAR-01. At centers \(c=4\pi e^L\) with \(\kappa_-\leq tL\leq\kappa_+\), use \(D_c=\{|z-c|\leq1/L\}\). In UAR-03's double-contour model replace both limits by the common value

\[
V_t=S_t=\sqrt{p\kappa_+/t}.                               \tag{10}
\]

The limits depend on \(t\) and the fixed band, not on the chart center. The original choice is \(p=4,\ \kappa_+=2\).

**Proposition 2.** There exist \(t_0>0\) and \(C>0\), depending only on \(\kappa_-,\kappa_+,p,\eta\), such that for \(0<t\leq t_0\), all centers in this band and either extremal frozen cutoff:

\[
\sup_{D_c}|e_{\rm edge,N}-\widehat e_{\rm edge,N}^{\,p}|
\leq C Z_c e^{-(p-\eta)L}.                               \tag{11}
\]

The models with the same \(N\) agree exactly on chart overlaps. At a crossing the entering exact heat mode and adjacent retained edge difference, after division by \(A\), have error at most twice the right side of (11).

For every fixed nonnegative integer \(j\), on the real half-window \(W_c\),

\[
|\partial_x^j(e_{\rm edge,N}-\widehat e_{\rm edge,N}^{\,p})|
\leq j!(2L)^j C Z_c e^{-(p-\eta)L}.                       \tag{12}
\]

There is also \(C_h>0\), depending on the fixed band, such that the original corrected transitions satisfy

\[
\sup_{D_{\xi_n}}|h_n|\leq C_h Z_{\xi_n}/\xi_n,\qquad
|Z_{h_n}(\xi_n)|\leq C_h' Z_{\xi_n}/n^2.                 \tag{13}
\]

Hence their sum over every prefix of the compact band is

\[
O_{\kappa_-,\kappa_+}\left(
\exp\{-(\kappa_-^2+12\kappa_-)/(16t)\}\right).             \tag{14}
\]

The constants in (11) and its allowed onset need not be the published \(1000\) and \(1/20\). No numerical onset for a new band is asserted.

### Proof of the error and overlap statements

All limits below are uniform over the fixed band as \(t\downarrow0\). We have \(L\geq\kappa_-/t\to\infty\), \(c\to\infty\), \(q=N+1/2\asymp e^{L/2}\), and \(|q-a|\leq1/2+o(1)\), including the alternate cutoff. The contour avoids its poles and logarithmic cut. On \(D_c\), the reflected real parameters are \(\sigma=1/2+O(1/L)\). Direct expansion of the explicit \(m_0,\alpha,m_t\) formulas, or the earlier [matching note's prefactor bound][matching], gives

\[
P(t,\operatorname{Re}z)/|A(t,z)|=O_{\kappa_-,\kappa_+}(Z_c),
\qquad |\omega(x)|\geq L/5\quad(x\in W_c)                 \tag{15}
\]

for sufficiently small \(t_0\). For the first estimate, its real logarithmic correction is \(O((1+L)/c)\), and movement by \(1/L\) in the imaginary direction has bounded normalizer cost. In the second, \(\omega=-L/4+O_{\kappa_-,\kappa_+}(1/c)\); the half-window change is absorbed by reducing \(t_0\).

The global contour majorant and gamma/reflection estimate in UAR-03, equations (8)–(9), remain applicable once \(c\) is sufficiently large. With \(u=\sigma+\sqrt t\,v\), their Gaussian-weighted product has a bound

\[
C_0\exp\{-(1-\delta_t)v^2+\lambda_t|v|\},
\qquad \delta_t\to0,\quad \lambda_t\to0.                 \tag{16}
\]

These limits are uniform: the non-Gaussian quadratic coefficient is \(O(1/c)\), the linear coefficient is \(O(1/q)\), and \(t\leq t_0\). The gamma bound uses reflection on the infinite left tail; it is not a fixed-sector Stirling expansion there.

Since \(V_t^2=p\kappa_+/t\geq pL\), the Mills bound for the two tails of (16) is \(O(e^{-(p-\eta)L})\). Explicitly, take \(t_0\) so that the coefficient losses in (16), including \(\lambda_t/V_t\), are less than a fixed fraction of \(\eta/p\); absorb the remaining tail prefactor into \(C\).

On the retained \(v\) interval, \(|u|\leq1+ \sqrt{p\kappa_+}\) for small \(t\). The unintegrated contour estimate is therefore

\[
C_1\exp\{-\pi r^2+o(1)|r|\}.
\]

For \(|r|\geq S_t\) this is bounded by \(C_2e^{-3r^2}\), after reducing \(t_0\). Its two tails cost \(O(e^{-3S_t^2})=O(e^{-3pL})\), which is smaller than the required bound. The complement is partitioned into the full-contour heat tails and the central-heat contour tails, so it is counted once. Pay both reflected channels using (15). The analytic correction is identical in the exact and finite edge and cancels from their difference. This proves (11).

Identical \(t,N,V_t,S_t\) give identical analytic models on overlaps. The exact residue identity \(\mathscr E_n-\mathscr E_{n-1}=-m_n^{\rm heat}\) then proves the twice-error compensation statement. Cauchy's estimate at distance \(1/(2L)\) from the disk boundary proves (12) for the complete normalized error. These derivative bounds do not differentiate a real-axis majorant.

### Proof of the corrected-transition estimate

Use the earlier [matching note][matching], equations (13)–(19), on radius \(r=1/L\) about a crossing. The geometric quantities there obey

\[
d=O(r/n),\quad E=O(r/n^2),\quad
D_0,D_1,D_s=O(1/c),\quad \Delta=O(1).
\]

For \(t\leq\min(t_0,1/2)\), its explicit matching exponent is \(O(1/c)\). The entering leading mode minus the printed jump is consequently \(O(P/c)\).

The printed jump must still be replaced by its analytic version. The exact single-wave formula has \(a-n=O(r/n)\), phase derivative \(\psi'=(a-n)/(2a)=O(r/c)\), and slow logarithmic amplitude derivative \(O(1/c)\). Integrating that slow derivative over the vertical segment costs \(O(rP/c)\). Division by the actual complex \(A\), using (15), proves the first bound in (13). Real symmetry, the disk estimate and \(|\omega|\geq L/5\) give the second by the coupled Schwarz-Pick estimate; a fixed constant suffices because \(R|\omega|\geq1/5\).

Every included crossing has \(n>e^{\kappa_-/(2t)}\). The positive envelope \(Z_c\) decreases with height, so

\[
\sum |Z_{h_n}|
\leq C_h'\,
\frac{\exp\{-(\kappa_-^2+4\kappa_-)/(16t)\}}
{e^{\kappa_-/(2t)}-1}.
\]

The denominator correction \(1/(1-e^{-\kappa_-/(2t)})\) is bounded after fixing \(t_0\). This proves (14), with no cancellation between distinct crossings. QED.

## 4. What the extensions do and do not provide

The compact-band result permits \(\kappa_-<1\) or \(\kappa_+>2\) after choosing a suitable small-time onset. Increasing \(p\) enlarges the retained contour and yields a smaller omitted-tail order. It does not automatically make the retained signed model small or inexpensive to evaluate.

The explicit original UAR-04 bound has not been extended outside \(1\leq\kappa\leq2\). Its finite gamma/heat correction and retained saddle value require their own estimates in a new band. Nor does a compact-band theorem cover all \(x\) at fixed \(t\): that would let \(\kappa=t\log(x/(4\pi))\) grow without bound. Larger positive times, fixed-width complex strips and other completed arithmetic sources also require fresh hypotheses and estimates. Time derivatives would add the moving truncation endpoints and the normalizer/forcing terms.

Equation (12) extends an edge-error derivative budget, not a complete second-jet or Laguerre certificate. The main outstanding physical task remains a lower bound for the retained approximation with all residual and variation costs paid.

## 5. Validation and control scope

The [small checker][checker] verifies the explicit reserve in Proposition 1 at 192/256 bits, its sample subinterval ceiling, exact jump-sign and rebasing fixtures, and the complete zero-residual polynomial-event limitation. It also verifies the source identities of the unchanged UAR-03/04 inputs. The [receipt][record] records actual provenance. These checks support the constants and bookkeeping; the written monotonicity and compact-band estimates supply the uniform proofs.

The manuscript integration replays UAR-03, UAR-04 and UAR-06, the last including the existing five source-specific event rejections and separate Euler negative-Laguerre witness. No theta constant is assigned to an altered source. Finite-prime and weighted-square controls lack the unchanged full theta coefficients/reflection; smooth, reflected and positive-primitive controls lack the theta square expansion and corresponding contour; Euler changes alter level or coefficients; polynomial controls lack the gamma/RS source. The generic endpoint identity still holds for such controls and supplies no nonzero physical anchor.

[edge]: 09_UNIFORM_COHERENT_EDGE_AND_CUTOFF_MATCHING_20261019.md
[increment]: 10_UNIFORM_SIGNED_RESIDUAL_INCREMENT_20261019.md
[consumer]: 12_MATCHED_COMPLETE_CONSUMER_AND_COST_COMPARISON_20261019.md
[contract]: ../../notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md
[matching]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md
[review]: ../../../reviews/18_UAR_ANALYTIC_MANUSCRIPT_AND_GENERALIZATION_REVIEW_20261019.md
[checker]: ../numerics/check_rebased_residual_envelope.py
[record]: ../numerics/REBASED_RESIDUAL_ENVELOPE_20261019.json
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
