# Fixed Gevrey complete asymptotics and moving-taper bounds: consolidated review

20 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
Actual model **gpt-6-astra (Codex), reasoning effort ultra**.
Initial same-model derivations and checks at HEAD **663e006**; complete first-order and moving-taper continuations checked at HEAD **341152b**.
This is an internal research review, not specialist or cross-model review.

**Verdict.** The current claims in [Note 16 §§11–14](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md) pass the recorded internal checks. For every fixed declared Gevrey taper under RH, the actual complete norm has the exact first-order constant given by the full multiplicity-dependent profile sum. The proof now pays the actual scaled height tail. Section 13 now gives \((\log N)d_N^2\to K=\sum_{\rho\ {\rm distinct}}m_\rho^2/|\rho|^2\) under RH, with real coefficients and the complete tail retained. The constant \(Z\) is its all-simple special case. A separate estimate tracks the exponentially growing constant for the specified moving almost-linear family and proves convergence on stated slow schedules. The earlier estimates below remain valid historical steps. The [Note 12 §13](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) moving-taper lower rates are compatible with these upper results. No RH-to-simplicity conclusion, sharp moving-taper asymptotic, specialist validation, or literature-priority claim is made.

The [result index](../../../../../../../result-summaries/README.md), [control register](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md) apply. In particular this review retains [scoped conclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [complete payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [gain before expansion](../../../../../../../avoid/20_volume_without_a_gain.md). The gains are actual complete-norm estimates for the declared tapered Möbius polynomials and, in §9, the sharp constant for the full polynomial infimum using finite mixtures. These are quantitative conclusions, not another event-equivalent criterion.

## 1. Objects, hypotheses, and exact claims

Write \(L=\log N\), and let \(W\) be a fixed real compact extension supported in \([-1,1]\), normalized by \(W(0)=1\), with
\[
 \|W^{(j)}\|_1\le A^{j+1}(j!)^\sigma,\qquad 1<\sigma<2.
\]
Its restriction to \([0,1]\) is \(w\). The approximation and complete error are
\[
 V_{N,w}(s)=\sum_{n\le N}\mu(n)n^{-s}w(\log n/L),
 \qquad
 E_{N,w}=\frac1{2\pi}\int_{\mathbb R}
 \frac{|1-\zeta(\tfrac12+it)V_{N,w}(\tfrac12+it)|^2}
      {\tfrac14+t^2}\,dt.
\]
The general upper and asymptotic theorems assume RH and no inverse-derivative moment. The earlier IC4 corollary assumes simplicity in addition; AD2 now identifies the general multiplicity-dependent infimum constant under RH alone. Fixed-taper constants may depend on the one fixed extension; §8 separately states and audits the moving-family uniformity. In the fixed- and moving-taper statements, the coefficients remain the original finite Möbius coefficients multiplied by the declared taper. AD uses finite Dirichlet multiplier mixtures of these polynomials, which belong to the larger infimum class.

The reviewed conclusions have the following distinct scopes.

| Claim | Checked conclusion | Essential restriction |
|---|---|---|
| GC1–GC23 | Uniform domination by \((3+|t|)^{(\sigma-1)/2+\eta}\); an integrable uniform height tail; \(E_{N,w}\to0\) | One fixed compact Gevrey extension, \(1<\sigma<2\) |
| QR1–QR12 | Earlier bound \(E_{N,w}\ll_{W,B}(\log\log N)^B/\log N\), now strengthened by ST | Valid historical estimate for each fixed taper |
| CH1–CH14 | Exact first-order norm on each fixed compact height interval, with remainder \(O_{T,w}(\log L/L^2)\) | Endpoints avoid zero ordinates; height remains fixed |
| PM1–PM6 | The complete weighted series of limiting local costs converges | A limiting-series bound, distinct from the actual norm tail |
| JL1–JL16 | A joint-scale lower rate for specified almost-linear moving tapers at an exact order-\(m\) event | The complete moving-kernel and remote-height budgets are paid separately |
| ST1–ST20 | Uniform scaled height tail and \(LE_{N,w}\to\sum C_{m_\rho}(w)/|\rho|^2\) | One fixed taper; all zero multiplicities retained |
| IC1–IC4 | \(d_N^2\asymp1/L\) under RH; \(Ld_N^2\to Z\) under RH plus simplicity | Infimum over polynomials; the sharper constant has an additional premise |
| MU1–MU16 | \(E_{N,\eta}\le C e^{C\eta^{-a}}/L\), \(a>1/(2-\sigma)\) | Fixed cutoff, \(L^{-\theta_0}\le\eta<1/4\), fixed \(0<\theta_0<1\) |
| AD1–AD18 | \((\log N)d_N^2\to\sum m_\rho^2/|\rho|^2\) under RH | Full polynomial infimum; finite target set, tapers and filter degree fixed before N tends to infinity |

For a zero of exact multiplicity \(m\), the local profile is
\[
 \mathcal E_{m,w}(z)
 =1-\frac{z^m}{(m-1)!}\int_0^1u^{m-1}w(u)e^{-zu}\,du,
 \qquad
 C_m(w)=\int_0^1
 \left|\frac{(u^{m-1}w(u))^{(m)}}{(m-1)!}\right|^2du.
\]
The flat endpoint hypotheses eliminate the boundary terms needed for this representation. The earlier lower cost \(C_m\ge m^2\), and the strict tradeoff between different multiplicities for a single fixed taper, remain valid. The new upper allowance does not contradict them.

## 2. Global domination: inputs and complete analytic payment

The imported estimates were reopened in their primary sources. [Carneiro–Chandee–Milinovich, Theorem 2](https://arxiv.org/pdf/1309.1526), supplies
\[
 |S(t)|\le(\tfrac14+o(1))\frac{\log t}{\log\log t}
\]
under RH. Its introductory counting formula and one-sided limits retain endpoint multiplicities. [Chandee–Soundararajan, Theorem 1.1](https://arxiv.org/pdf/0908.2008), supplies the critical-line bound \(|\zeta(\tfrac12+it)|=t^{o(1)}\). Neither result assumes simple zeros. The proof uses both estimates only in their declared RH ranges.

The moving-line kernel
\[
 K_H(v)=\frac1{2\pi}\int W(u)e^{(H+iv)u}\,du
\]
satisfies
\[
 |K_H(v)|\le C e^H e^{-c|v|^{1/\sigma}}
\]
with \(C,c\) independent of both \(H\) and \(v\). This uniformity is essential. Integration by parts transfers derivatives to \(W\) against the full complex exponential, producing \(|H+iv|^{-j}\). Differentiating the growing exponential instead would introduce constants that are not justified for the later height-dependent choices of \(H\).

The exact convolution retains every coefficient:
\[
 V_{N,w}(s)=\int_{\mathbb R}
 \frac{K_H(v)}{\zeta(s+(H+iv)/L)}\,dv.
\]
It starts on an absolutely convergent Dirichlet line and shifts within the RH zero-free right half-plane. The complete coarse reciprocal bound and Gevrey decay pay the horizontal contour pieces. The reciprocal is regular at the pole of zeta, and no zero residue is crossed or deleted.

The sharper reciprocal coefficient in GC13 is also paid. Put \(U=\log t\), \(\ell=\log U\). The complete count in \([t-v,t+v]\), with multiplicities, obeys
\[
 n_t(v)\le \frac v\pi\log(t/(2\pi))
          +(\tfrac12+\epsilon)\frac U\ell,
 \qquad 0\le v\le t/2.
\]
Concavity bounds the smooth counting increment; the two argument terms supply the half coefficient. Infinitesimal endpoint enlargement covers closed intervals, including an atom at \(v=0\). The exact positive Stieltjes integral for the zero Poisson sum has elementary integrals \(\pi/2\) and \(1/a\). Its remaining all-zero tail is \(O(aU/t)\). Exact gamma and rational completion terms cancel the logarithmic main term.

One wording error was found and repaired during independent review. The anchor for the integrated reciprocal estimate must be
\[
 |1/\zeta(2+it)|\le\zeta(2),
\]
not the upper bound for \(|\zeta(2+it)|\). The former follows from the absolutely convergent reciprocal Euler series and gives the required direction. The corrected stage uses it; no conclusion or subsequent constant changes.

The global proof then uses two overlapping ranges, each with a complete tail payment.

For \(U\le L^b\), with fixed \(b<1/\sigma\), remove exactly the nearby radius-\(r\) zero cluster, where \(r=d/\ell\). The anchored difference of logarithmic derivatives is absolutely convergent. Its regular part is \(O_d(U\log\ell)\), and integration across the smaller disk costs \(o(U)\). The exact completion ratio also costs \(o(U)\); it is retained. If the cluster has \(M\) zero occurrences, choosing \(H=M+1\) bounds each local factor and gives the moment exponent
\[
 (\sigma-1)M\log(M+2)+O_W(M+1).
\]
This includes arbitrary multiplicity and uses no inverse leading derivative. The cluster count gives the stated low-height exponent. The full omitted Fourier tail starts at scale \(L/\log U\); \(b<1/\sigma\) makes its Gevrey decay dominate the coarse reciprocal allowance uniformly, including arbitrarily large external heights.

For \(U\ge L^b\), choose \(H=\kappa U\). On the central Fourier range the shifted heights remain comparable to \(t\), and GC13 gives exponent
\[
 (\tfrac12+\epsilon)(b^{-1}-1)+o(1).
\]
The kernel factor adds \(\kappa\). The Euler bound covers larger real shifts. Beyond \(|v|>tL/2\), the coarse reciprocal bound is dominated by the full Gevrey tail. Since \(L\le U^{1/b}\), this is uniform even when \(t\) greatly exceeds \(N\).

Taking \(b\) near \(1/\sigma\), then the small fixed parameters, gives GC3. A finite cluster cover pays bounded heights uniformly in \(N\); finitely many small \(N\) and conjugation complete the coverage. The squared majorant is integrable when \(2\eta<2-\sigma\). Pointwise convergence away from the countable zero set therefore yields actual complete-norm convergence by dominated convergence. This is a full-height upper result, rather than a bound for one coefficient or a formal local model.

## 3. Earlier quantitative rate and distance corollary

This valid earlier proof is retained as a historical step. The complete first-order theorem in §7 now removes its logarithmic upper allowance for each fixed taper.

The QR proof preserves the preceding uniformity and improves qualitative convergence to a rate. Choose
\[
 (\sigma-1)/2<q<1/2,\quad
 T=L^A,\quad A>1/(1-2q),\quad
 d=(\log L)^B/L.
\]
Global domination pays the height tail by \(o(1/L)\). The union of radius-\(d\) intervals around all zero ordinates costs \(O(d)\), since the weighted zero sum with exponent \(-2+2q\) converges. Overlaps only increase this upper allowance; there is no separation or simplicity premise.

On the complementary set, cap the distance to the nearest zero by \(D\le1/4\). The complete xi-product difference anchored at \(2+it\) gives
\[
 \sup_{|z|\le D/2}|\zeta'/\zeta(\tfrac12+it+z)|
       \ll \log(3+|t|)/D.
\]
The cap excludes the zeta pole and keeps the completion regular at bounded heights. The exact identity \(\int K_1=1\) is used before taking absolute values, yielding the coherent central error
\[
 O\!\left(\frac{\log(3+|t|)}{LD}\right).
\]
The remaining Fourier range begins at least at a constant times \((\log L)^{B-1}\). The condition
\[
 \frac{B-1}{\sigma}>2
\]
makes Gevrey decay dominate both the \(O((\log L)^2)\) reciprocal cost and its logarithmic growth on the entire unbounded tail. The resulting remainder is smaller than every fixed negative power of \(L\).

Assigning points to nearest-zero cells gives the integrated distance bound \(O(1/d)\). The associated complete zero-weight series converges. Squaring the pointwise estimate therefore costs \(O(1/(L^2d))\), with no additional height factor for the uniform remainder because the norm weight is integrable. Combining the three regions proves QR1. All nonlocal heights are paid before integration.

There is an immediate standard distance corollary. With the convention of [Note 12 §5](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md),
\[
 d_N^2=\inf_{A(s)=\sum_{n\le N}a_nn^{-s}}
 \frac1{2\pi}\int_{\mathbb R}
 \frac{|1-\zeta(\tfrac12+it)A(\tfrac12+it)|^2}{\tfrac14+t^2}\,dt,
\]
the displayed polynomial \(V_{N,w}\) is an admissible competitor. Hence
\[
 d_N^2\le E_{N,w}.
\]
For \(w_p(u)=\exp(1-(1-u)^{-p})\), the fixed extension has order \(1+1/p\). Given any fixed \(B>3\), choose a fixed
\(p>\max\{1,2/(B-3)\}\). Then
\[
 \boxed{d_N^2\ll_B
       \frac{(\log\log N)^B}{\log N}.}
\]
The implied constant includes that fixed choice of extension. This is a direct corollary of the written upper proof, not a claim about a best-known rate. Its growing logarithmic allowance is compatible with the classical multiplicity-squared lower bound. QR alone gives no estimate at the simple-zero leading constant; the separately proved §7 infimum corollary now gives that constant under the additional simplicity assumption.

## 4. Compact-height norm and limiting profile mass

The CH proof retains the whole Laurent principal part at each zero, together with its analytic remainder. Coherent subtraction of that analytic remainder gives an \(O(1/L)\) error throughout a fixed neighborhood. Extending the principal-part integrals across the Fourier tail uses the horizontal-distance bound \((L/H)^j\); this explicitly covers possible cancellation of the imaginary displacement near \(v=-Ly\). Gevrey decay pays that tail and every remote height.

The local profiles decay as \(O((1+|y|)^{-1})\). This controls the entire fixed annulus, not only a bounded scaled window. The cross term, weight replacement, and omitted model tail give
\[
 E_{N,w}^{|t|\le T}
 =\frac1L\sum_{\substack{\rho\ {\rm distinct}\\|\Im\rho|<T}}
       \frac{C_{m_\rho}(w)}{|\rho|^2}
   +O_{T,w}(\log L/L^2),
\]
when the endpoints avoid zero ordinates. The compact zero-free complement is paid separately. Constants may depend on \(T\), the taper, and its fixed zero neighborhoods.

The PM estimate concerns a different limit. The full Leibniz expansion and Gevrey derivative bound imply
\[
 \log C_m(w)\le2(\sigma-1)m\log m+O_W(m+\log m).
\]
The one-sided argument bound gives
\(m\le(\tfrac12+o(1))\log|\gamma|/\log\log|\gamma|\).
The ordinary unit-window zero count then proves convergence of
\(\sum C_{m_\rho}(w)/|\rho|^2\), with the stated power tail for \(\sigma<2\).

Neither CH nor PM alone permits a first-order global exchange of limits. The original GC height tail has no factor \(1/L\), and CH has constants depending on its fixed height. That was the remaining payment at the earlier checkpoint. Section 7 now supplies an actual uniform scaled tail, so the complete first-order limit is proved by combining that new estimate with CH. The convergence of the limiting profile series is not used as a substitute for the actual tail.

## 5. Moving almost-linear tapers: joint scales and the actual lower cost

The JL continuation in Note 12 §13 uses one fixed Gevrey cutoff \(\chi\), sets \(Q(r)=r\chi(r)\), and takes
\[
 w_\eta(u)=(1-u)\chi((1-u)/\eta).
\]
It is normalized, nonnegative and decreasing, equals the linear taper outside its shrinking endpoint layer, and is flat at one. The exact model costs satisfy
\[
 C_1=1+d\eta,\qquad
 C_m=A_m\eta^{3-2m}(1+O_m(\eta))\quad(m\ge2),\qquad
 A_m=\frac{\|Q^{(m)}\|_2^2}{((m-1)!)^2}>0.
\]
The derivative support length is essential: it yields a uniform quadratic Fourier prefactor, with moving decay scale
\[
 |K_{H,\eta}(v)|
 \le C_H(1+v^2)^{-1}e^{-c_H(\eta|v|)^\beta}.
\]
Under
\[
 \eta_N\to0,\qquad
 (\eta_NL)^\beta/\log L\to\infty,
\]
this bound pays the complete reciprocal tail, including all noncentral zeros. The growing-window Laurent expansion retains every principal term. Its first Laplace integral decays as \(O((1+|y|)^{-1})\); the higher ones decay as \(O((1+y^2)^{-1})\), uniformly in the layer width.

The actual approximation error is bounded by
\[
 |e_N(\rho+iy/L)-\mathcal E_{m,w_\eta}(iy)|
 \ll_{\rho,m,M}(1+|y|)^{m-1}/L
 \quad (|y|\le M/\eta).
\]
After multiplying by \(\eta^{m-2}\), this is \(O(1/(\eta L))\). For \(m\ge3\), it is not a uniform absolute error of that size before normalization. This distinction was expressly checked.

The rescaled finite-window limit and Plancherel give
\[
 \liminf_N\eta_N^{2m-3}L E_{N,w_{\eta_N}}
       \ge A_m/|\rho|^2.
\]
A conjugate pair contributes twice this amount. With \(\eta_N=L^{-\theta}\), \(0<\theta<1\), the lower rate is
\[
 \liminf_N\frac{E_{N,w_{L^{-\theta}}}}
                  {L^{\theta(2m-3)-1}}
       \ge A_m/|\rho|^2.
\]
For a double, this forces growth of \(LE\), but does not force full-norm divergence in the stated range. For an exact triple and \(1/3<\theta<1/2\), it forces \(E\to\infty\). Exact partial summation and the [Balazard–de Roton RH Mertens bound](https://arxiv.org/pdf/0810.3587) simultaneously make the extracted coefficient divided by \(\sqrt N\) tend to zero. This separates that coefficient test from the complete error by an actual lower rate.

Section 8 now supplies an explicitly paid upper bound for the declared moving family. Its exponential allowance does not oppose these fixed-multiplicity lower costs. Applying the fixed-taper GC, QR, or ST estimates with constants silently uniform in \(\eta_N\) would still be invalid. Neither the JL nor the new MU proof claims the endpoint layer scale \(\eta\asymp1/L\).

## 6. Review record and supersession

The consolidated record uses three separate same-model review paths: phase, arithmetic, and Gaussian. The coordinator also independently checked the principal global and rate derivations. Coverage is explicit: the global GC proof received independent phase and Gaussian audits in addition to the coordinator's check; the QR proof received phase, arithmetic, and Gaussian audits. CH and JL received separate checks of their constants, annuli or growing windows, and complete tail payments. PM was checked separately from the actual-height argument. These are separate analytic checks within the same model family, not independent specialist validation.

The earlier bounded Lean artifact for the abstract two-cost projection identity formalizes none of GC, QR, CH, PM, JL, ST, IC, MU, or AD. No analytic Lean proof, machine-checked contour argument, or formal verification of these global approximation results is claimed here.

The anchor-direction correction is resolved. The new §§7–8 supersede the earlier statements that the fixed-class global first-order passage and every moving-family upper payment were missing. The exact fixed-taper profile constant and the specific MU uniform upper bound are now proved in-note and separately checked. Section 9 additionally checks the exact full-infimum constant K, using finite Dirichlet filters. A sharp moving-taper asymptotic and an opposing signed arithmetic or winding estimate excluding an original multiple zero remain unproved. No novelty, universal optimality, or specialist-review claim is attached to this checkpoint.


## 7. Complete first-order tail, exact constant, and infimum corollaries

This continuation reviews ST1–ST20 and IC1–IC4 in [Note 16 §11](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md). The arithmetic and Gaussian paths independently derived the same scaled-tail estimate. Each checked the other's derivation; the phase path and coordinator checked the complete argument separately. The infimum corollaries were also checked with their hypotheses and order of limits explicit. **Verdict: pass after the bounded-height uniformity clarification described below.**

The new subtraction is performed in the exact convolution before taking absolute values:
\[
 e_N(t)=\int K_H(v)
 \left(1-\frac{\zeta(1/2+it)}
 {\zeta(1/2+it+(H+iv)/L)}\right)\,dv.
\]
The kernel has integral one. The quotient factors into the complete nearby zero product and its nonvanishing regular factor, including the exact gamma and rational completion. The cluster radius is \(r=d/\log\log t\), its count includes every multiplicity, and \(H=M+1\).

For each local factor, the exact difference has the bound
\[
 |1-r_j|\le
 \frac{|(H+iv)/L|}{D(t)}\sqrt{1+v^2/H^2},
 \qquad D(t)=\min(1/4,\operatorname{dist}(t,\{\gamma\})).
\]
Telescoping the whole product yields \(M\) times the \(M\)-th power of the geometric factor. The regular completion factor equals one at zero shift. Its bounded logarithmic derivative therefore supplies an additional displacement factor in its difference from one. Neither step bounds the two large terms separately, replaces a repeated root by a simple residue, or presumes a lower gap.

The added kernel moment does not change the decisive exponent. The largest gamma factor becomes \(\Gamma((M+2)/\beta)\), divided by \((M+1)^M\). Stirling retains the leading term \((\sigma-1)M\log(M+2)\), with only an \(O_W(M+1)\) remainder. The polynomial factors from the regular logarithmic derivative are subpower in height. Choosing
\((\sigma-1)/2<q<1/2\) with a strict margin gives the central error \(t^q/(LD(t))\).

Every remote Fourier height is still paid. In the low-height range \(U=\log t\le L^b\), \(b<\beta\), the cutoff is of order \(L/\log L\). The complete reciprocal exponent is dominated uniformly on the entire exterior interval, including arbitrarily large imaginary shifts. The subtracted constant has its own smaller tail and is retained. The stronger observation
\[
 (L/\log L)^\beta/(U+\log L)\longrightarrow\infty
\]
makes the integrated remainder \(O_J(L^{-J}t^{-J})\) for every fixed \(J\). It therefore remains negligible after multiplying the squared norm by \(L\).

Combining the coherent bound with the earlier global majorant gives
\[
 |e_N(t)|\ll t^q\min\{1,(LD(t))^{-1}\}
                    +O_J(L^{-J}t^{-J}).
\]
At a zero ordinate the bounded branch applies. The cluster and the auxiliary shift may change with \(t\); no derivative in \(t\) is taken, and all estimates are pointwise with uniform counts.

On each actual nearest-zero cell,
\[
 \int_{\mathbb R}\min\{1,(L|x|)^{-2}\}\,dx=4/L.
\]
The cell is only a subset of this integral. Weight comparability is used within distance \(1/4\), so arbitrary close zeros cause no loss. Distinct locations receive cells; multiplicities may harmlessly be included in the upper count. The complete weighted zero sum converges because \(q<1/2\). Where \(D=1/4\), a smaller ordinary integral is paid separately.

In the high-height range, the earlier majorant suffices because the defining inequality gives \(L\le(\log t)^{1/b}\). This controls the scaled norm there. Absorbing the fixed logarithmic powers in the exponent margin proves
\[
 \sup_{N\ge2}L E_{N,w}^{>T}
       \ll_{W,\epsilon}T^{\sigma-2+\epsilon},
 \qquad 0<\epsilon<2-\sigma.
\]
The initial bounded-\(T\) range is now explicitly justified: CH1 bounds the scaled norm on a fixed compact interval for large \(N\); finitely many remaining \(N\) have finite norms. Adding the already established tail at a large fixed endpoint supplies the uniform constant for every \(T\ge2\). This clarification was applied before acceptance and avoids hiding a supremum over \(N\) in an unspecified constant.

The actual scaled tail, together with CH1, now proves
\[
 \lim_{N\to\infty}L E_{N,w}
    =S_w:=\sum_{\rho\ {\rm distinct}}
                 \frac{C_{m_\rho}(w)}{|\rho|^2}<\infty.
\]
Both ordinate signs are retained. This strengthens the earlier logarithmically weakened bound and pays the former global limit passage. It uses no inverse-derivative moment and permits arbitrary multiplicities.

For the infimum, \(d_N^2\le E_{N,w}\) and the already imported [Burnol lower bound, Theorem 1.3](https://arxiv.org/pdf/math/0103058), give
\[
 0<K:=\sum_{\rho\ {\rm distinct}}\frac{m_\rho^2}{|\rho|^2}
 \le\liminf Ld_N^2\le\limsup Ld_N^2\le S_w<\infty.
\]
Thus \(d_N^2\asymp1/\log N\) under RH. Finiteness of \(K\) follows also from \(C_m\ge m^2\) and the finite upper sum. This fixed-taper comparison alone does not replace its upper coefficient by \(K\) in the presence of multiple zeros. Section 9 now checks a finite-filter construction that reaches \(K\) for the larger polynomial infimum.

If simplicity is assumed in addition, fix an almost-linear taper first. Its coefficient is \(C_1=1+d_\chi\eta\), so
\(\limsup Ld_N^2\le(1+d_\chi\eta)Z\) for every positive fixed \(\eta\). Taking the infimum of these bounds and applying Burnol yields
\[
 \lim_{N\to\infty}L d_N^2=Z,
 \qquad Z=2+\gamma_E-\log(4\pi).
\]
This is a sequential argument about the infimum over polynomials. It neither selects a moving \(\eta_N\), claims the corresponding asymptotic for the original linear Möbius polynomial, nor obtains simplicity from RH. The profile constant retains the actual multiplicity costs throughout.

## 8. Moving-taper upper bound with its constants tracked

This continuation reviews MU1–MU16 in [Note 16 §12](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md), for the family defined in [Note 12 §13](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md). The phase path derived the estimate; the arithmetic and Gaussian paths independently checked every stated parameter and tail range, and the coordinator also checked it. **Verdict: pass, with the scope wording restricted to compatibility rather than a logical counterexample to RH implying simplicity.**

Fix the cutoff of order \(1<\sigma<2\), a number \(0<\theta_0<1\), and \(a>1/(2-\sigma)\). Uniformly for
\[
 L^{-\theta_0}\le\eta<1/4
\]
at sufficiently large \(L\), the checked bound is
\[
 \boxed{E_{N,\eta}\le C_1\exp(C_2\eta^{-a})/L.}
\]
The constants depend on the fixed cutoff and declared fixed parameters. The exponential is an allowance in this upper proof, not an actual lower bound or a necessary cost for every method.

The transition has amplitude \(\eta\) and width \(\eta\). Its \((n+2)\)-nd \(L^1\) derivative costs \(\eta^{-n}\), including the fixed left transition in the same bound. Integration by parts against the full complex exponential therefore gives
\[
 |K_{H,\eta}(v)|\le
 \frac{Ce^H}{1+H^2+v^2}
 \exp\{-c(\eta\sqrt{H^2+v^2})^\beta\}
\]
with constants independent of \(H,\eta,v\). The first absolute moment at \(H=1\) grows only as \(1+\log(1/\eta)\); it is expressly paid.

Put \(X=\eta L\), \(\lambda=\log(1/\eta)\). The low/high split now uses \(U\le X^b\) and its complement. The support-sensitive moments give the additional leading cost \(M\lambda\). For the coherent one-extra moment, the largest term is
\(\eta^{-M}\Gamma(M/\beta)/(M+1)^M\), up to a fixed exponential in \(M\). Its logarithm retains
\((\sigma-1)M\log(M+2)+M\lambda\).
The \(M=0\) first moment contributes the separate factor \(1+\lambda\). No further multiple of \(M\lambda\) is hidden in an implicit constant.

The full low-height tail starts at
\(\eta|v|\gtrsim X/\log X\). Since \(X\ge L^{1-\theta_0}\), one has \(\log L\ll_{\theta_0}\log X\). All positive reciprocal terms are at most a constant times
\[
 \log X\,[X^b+\log(3+\eta|v|)],
\]
which is uniformly smaller than \((\eta|v|)^\beta\). The whole tail is \(O_J(L^{-J}t^{-J})\), including the subtracted constant. At high heights, \(\log L\le\log U/b+\lambda\) introduces precisely the declared \(\lambda U/\log U\) penalty. The complete exterior interval starts at \(\eta|v|\ge tX/2\) and is paid using \(\log L=O(\log U)\).

The absorption threshold is correctly quantified. The height bound has exponent
\(q_0U+c_*\lambda U/\log U\), with \(q_0\) arbitrarily close to \((\sigma-1)/2\) and \(c_*\) arbitrarily close to \(1/2\). The strict condition \(a>1/(2-\sigma)\) permits \(q<1/2\) and \(a_0<a\) with \(c_*/(q-q_0)<a_0\). Above \(\log U=a_0\lambda\), the term fits inside \(qU\); below it, its entire cost is bounded by \(C\eta^{-a}\). This explicitly covers \(\lambda\) much larger than \(\log U\).

Coherent telescoping then gives the same nearest-zero minimum as in §7, multiplied by \(\exp(C\eta^{-a})\). Its low-height scaled integral is bounded by that allowance. Bounded heights have only a fixed-power cost in \(\eta^{-1}\), also absorbed. In the high range,
\(L\le\eta^{-1}(\log|t|)^{1/b}\); the remaining \(\eta^{-1}\) is absorbed by the same exponential. Squaring changes fixed constants, not \(a\). This pays the complete norm, rather than only a compact interval or a limiting profile.

For \(\eta_N=(\log L)^{-\kappa}\), \(0<\kappa<2-\sigma\), choose \(a\) with \(\kappa a<1\). The actual result is
\[
 E_{N,\eta_N}\le L^{-1+o(1)}\longrightarrow0.
\]
These schedules also satisfy JL8. The JL contribution of a fixed order-\(m\) zero requires only a fixed power \((\log L)^{\kappa(2m-3)}\) in \(LE\), which is compatible with the larger written upper allowance. More generally the ratio of that allowance to the fixed-\(m\) lower scale is proportional to
\(e^{C\eta^{-a}}\eta^{2m-3}\), which grows as \(\eta\to0\).

The reviewed statements therefore supply no contradiction to a putative multiple zero. They prove neither a necessary schedule threshold nor a sharp moving-family constant. The original Möbius identity, exact completion, and all multiplicities remain intact; the distinct generic controls' preservation lists are not combined into a purported arithmetic counterexample. No analytic formalization, specialist validation, novelty, or literature-optimality claim is made for either continuation.


## 9. Finite Dirichlet filters and the full infimum constant

20 October 2026 continuation, from checkpoint 39d6dba. Prepared for Edward
Baker with substantial LLM assistance, **gpt-6-astra, actual effort ultra**.
This is separate same-model internal review, not specialist validation.

A further adversarial check rederived the Fourier normalization and
contour shift, the anchored completed regular factor, the algebraic local
ratio inequality, the adaptive kernel moments, and coverage of both
height ranges in GC and ST. No shared-premise flaw was found in that
bounded check. The primary [Burnol lower bound](https://arxiv.org/pdf/math/0103058)
and [Bettin–Conrey–Farmer formulation and Theorem 1](https://arxiv.org/pdf/1211.5191)
were reopened: the infimum permits these polynomial coefficients, and
the specified-linear-polynomial theorem's additional inverse-derivative
hypothesis is not an extra premise of the new construction.

**Dependency and verdict.** The finite-filter conclusion passes the
independent derivation and checks below, **conditional on the internally
established Note 16 §11 scaled-tail and exact fixed-taper theorem (ST)**.
ST is a prior result of this research, not an independently published
external theorem. Its original proof has separate same-model internal
reviews; this assessment does not turn those checks into specialist or
cross-model verification. The new proof checked here is the finite
arithmetic filtering, actual mixed-profile transfer, complete dominated
peak limit, and ordered optimization of the infimum. The arithmetic and Gaussian paths supplied separate full derivations; the phase path and coordinator checked the complete construction. The final AD1–AD18 argument in Note 16 §13 was read in full, including its local-norm normalization repair and complex moment identity.

### 9.1. Finite arithmetic filters and polynomial length

The proposed peak at τ is
P_{τ,k}(s)=[(1+2^{τ−s})/2]^k[(1+3^{τ−s})/2]^k. Under RH its boundary
modulus is at most one, and its value at τ is exactly one. At any other
critical-line point at least one factor has modulus strictly below one:
otherwise both ordinate differences times log 2 and log 3 are integral
multiples of 2π. A nonzero difference would make log 2/log 3 rational,
contradicting unique prime factorization. Thus the peak tends to zero
at every other fixed ordinate. This is pointwise separation, not a
uniform gap, density, equidistribution, or interpolation assertion.

Each peak is supported on 2^a3^b with 0≤a,b≤k, so its Dirichlet length
is at most 6^k. The correction
V_{n,w0}+Σ_{τ∈F}P_{τ,k}(V_{n,wτ}−V_{n,w0}) has length at most 6^k n.
Taking n=floor(N/6^k) preserves admissibility, and log N/log n tends to
one for each fixed k. No bound uniform in both k and this logarithmic
ratio is needed or asserted. Choosing F conjugation-symmetric and the
same real taper at conjugate locations gives real coefficients: the
paired peak coefficients are complex conjugates.

### 9.2. Actual mixed profiles, with the entire norm retained

The multiplier partition is A_τ=P_{τ,k}, A_0=1−ΣP_{τ,k}; its sum is
identically one. Hence the full error is exactly Σ_j A_j e_{n,wj}, not
an approximation obtained by comparing separate norms. At each order-m
zero, this identity also preserves the exact finite-n Taylor jets
1+O((s−ρ)^m).

For fixed k, the compact CH estimate on a whole isolated zero disk is
e_{n,wj}(ρ+iy)=E_{m,wj}(iℓy)+O(1/ℓ), ℓ=log n, while
E_{m,wj}(ix)=O((1+|x|)^{-1}). Analyticity of each fixed multiplier gives
[A_j(ρ+iy)−A_j(ρ)]E_{m,wj}(iℓy)=O_k(|y|/(1+ℓ|y|))=O_k(1/ℓ).
This pays the full annulus as well as the shrinking central window.
The compact complement has error O(1/ℓ). Consequently the actual mixed
compact limit has the coherent density p_eff=Σ_j A_j(ρ)p_{m,wj}.
Its squared norm includes every cross term. The repaired primary text
correctly states the **unscaled** local norm as
||p_eff||²/(ℓ|ρ|²)+O(log ℓ/ℓ²); its scaled error is therefore
O(log ℓ/ℓ), not O(log ℓ/ℓ²).

The boundary bounds |A_τ|≤1 and |A_0|≤1+|F| dominate the complete actual
mixed squared tail by a fixed multiple of the sum of the base-taper
tails. ST therefore supplies tightness after multiplication by log n.
This completes the mixed global limit. The argument uses ST only for
its real fixed base tapers; it does not silently require a separately
proved complex-taper theorem. Complex values occur in a finite linear
combination whose cross-profile limit was just checked directly.

### 9.3. The complete peak limit and independent local optimization

For the fixed finite set F and the finitely many fixed tapers, the mixed
profile summand is bounded, uniformly in k, by
C_F[ C_m(w0)+Σ_{τ∈F}C_m(wτ)]/|ρ|². Every series in this finite sum is
summable by ST. Dominated convergence on the full countable zero set
therefore gives the chosen local taper exactly on F and the default
taper at every other zero. There is no discarded remote zero tail, even
if a remote phase lies arbitrarily close to a peak for some k.

The primary AD13 additionally pays this limit by a finite-height
geometric term B_H θ_H^k and the complete profile tail. Its θ_H<1
follows from the explicit two-prime separation for finitely many
off-diagonal pairs. The tail constant 4(J+1)² bounds both S_k and its
pointwise limit, and is independent of k. Choosing H after the fixed
family, then k, controls the entire difference; no uniformity in zero
separation is claimed.

Choose F first so that the default taper's complementary profile mass
is small. At each of its finitely many locations choose a fixed flat
Gevrey approximation to (1−u)^m. The endpoint cutoff changes the m-th
source derivative by a uniformly bounded function supported on a layer
of shrinking length, so its local cost approaches m². Such tapers admit
compact extensions of any one fixed Gevrey order between one and two.
All tapers are fixed before k, and k is fixed before N tends to infinity.
Taking the peak limit only in the resulting constant, then the outer
approximation tolerance to zero, proves the upper constant K. Burnol's
already imported multiplicity-squared lower bound gives the reverse
inequality. These ordered operations do not prescribe a moving k_N or
swap unproved uniform limits.

### 9.4. No accidental cancellation below the moment floor

For each effective complex density and each 0≤r<m,
∫_0^1 u^r p_eff(u)du=δ_{r0}, because the individual densities satisfy
these conditions and Σ_j A_j(ρ)=1. If K_m(u,0) is the real endpoint
reproducing kernel of polynomials of degree below m, complex Hilbert
orthogonality therefore gives exactly

\[
 \|p_{\rm eff}\|_2^2=m^2+\|p_{\rm eff}-K_m(\cdot,0)\|_2^2.
\]

The interpolation does not cancel any required moment or produce a
cost below m². It removes the additional restriction that one fixed
taper must serve locations of different orders. The final constant
K=Σ_{distinct ρ}m_ρ²/|ρ|², with both ordinate signs, retains every true
multiplicity. Thus the result is compatible with multiple zeros and
provides no RH-to-simplicity conclusion. It concerns an infimum over
all admissible finite Dirichlet polynomials, not a universal prescribed
Möbius taper, a finite zero-certification algorithm, or a new simplicity
criterion.


## 10. Exact finite filters and the cost of root isolation

20 October 2026, from checkpoint `5f7d894`. Prepared for Edward Baker
with substantial LLM assistance, **gpt-6-astra, actual effort ultra**.
Separate same-model internal derivations and checks; no specialist
validation, analytic formalization or priority claim.

**Verdict: pass for FR1–FR13 in [Note 16 §14](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md).**
The arithmetic path and coordinator derived the positive three-term
annihilator; the phase path independently checked its signs, endpoint
case, exact zeros and length. Finite products are still bounded by one
and give exact prescribed profiles on every node of the fixed finite
set. The mixed-profile theorem from §13 then retains all cross terms;
outside that set, the summable profile majorant depends on the fixed
number of target tapers, not the number or degrees of annihilating
factors. Thus FR7 genuinely removes the earlier finite-height
attenuation term, while paying the complete remaining tail. The finite
set and filters are fixed before the N limit. This does not assert a
uniform moving-set theorem or alter the infimum constant K.

The phase path derived the general complex-coefficient lower bound
and reopened [Redheffer's primary Theorem 11](https://msp.org/pjm/1953/3-4/pjm-v3-n4-p11-s.pdf).
Frequency centering gives type at most log M/2; applying the sharpened
Bernstein inequality to the real part and integrating arccos proves
|Delta|log M≥2 arccos(epsilon). The exact-zero lower pi/|Delta|
and the explicit upper pi/|Delta|+log2 agree to leading order for small
gaps. This is sharp two-point resolution, not a claim of optimal total
length for many targets. The same calculation with boundary supremum A
checks FR10 and the sine quotient in FR11; A² prices the stated
supremum-based tail allowance, not the actual integrated error.

Finally, the retained coordinate x=2 gamma gives the Hermite ordinate
gap sqrt(t/2)(lambda_k−lambda_j)+O(t). FR13 and the double-cluster
threshold v≥pi²/2 at t=v/(log N)² follow for exact unit-bounded isolation
using length at most N. They apply only when the construction actually
isolates the roots. A shared taper at both simple heat roots needs no
such isolation. No fixed-zeta ST theorem is transferred to a heat-deformed
function, and no new signed phase surplus, multiple-zero exclusion,
or multiplicity-free upper constant is claimed.

A further adversarial audit rederived the primary count and reciprocal bounds, shifted Gevrey kernel, worst-case coalesced-cluster factor, compact normalization and both remote-tail ranges. No concrete defect was found in that bounded check. The full cluster power is necessary in the coalesced test and remains paid; closed-window counts use outer one-sided limits. The Gaussian path also read the final FR1–FR13 integration and checked all constants. These are same-model internal audits, not specialist validation.

## 11. Consolidation manuscript review

20 October 2026. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort ultra**. The user-requested [canonical draft](../manuscript/main.tex) consolidates the analytic estimates and their remaining bottleneck; detailed proofs stay in the notes. Separate arithmetic and analytic reads checked the displayed constants, hypotheses, ordered limits and primary citations. The final source specifies the convolution domain, uses the local profiles together with ST for mixed cross terms, sends the outer tolerance to zero, and preserves the zero-dependent local remainder constant. The Gram discussion distinguishes cancellation to bounded size from the subsequent O(epsilon) energy precision. The bounded Lean check is not identified with the general-m projection theorem.

The BW09 comparison was checked against that route’s current manuscript and phase-surplus register: shared heat/contour identities and all-real-base ratio estimates are distinguished from original-zeta RH arithmetic. The positive-threshold event-coverage and strict-cap-surplus gates remain open. This consolidation claims no new simplicity or RH proof. Compilation and rendering are document checks, not mathematical validation.

The six-page PDF compiled without unresolved references or layout warnings. All six rendered pages were inspected for readable equations, clipping and page flow; all local manuscript links resolved. These checks concern the saved document only.
