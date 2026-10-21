# Fixed Gevrey global approximation and rate: consolidated review

20 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
Actual model **gpt-6-astra (Codex), reasoning effort ultra**.
Separate same-model derivations and analytic checks at HEAD **663e006**.
This is an internal research review, not specialist or cross-model review.

**Verdict.** The fixed-taper claims in [Note 16](../notes/16_GEVREY_GLOBAL_APPROXIMATION_AND_RATE_20261020.md) pass the recorded internal checks: uniform full-height domination, complete norm convergence, a quantitative upper rate, the compact-height asymptotic, and convergence of the limiting profile mass. The changing-taper lower bound in [Note 12 §13](../notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) also passes, with its joint-scale hypothesis and multiplicity-dependent normalization retained. The upper and lower statements concern different parameter contracts. None proves simplicity, a sharp global first-order constant, optimality, or priority over the existing literature.

The [result index](../../../../../../../result-summaries/README.md), [control register](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md) apply. In particular this review retains [scoped conclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [complete payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [gain before expansion](../../../../../../../avoid/20_volume_without_a_gain.md). The gain is an actual complete-norm upper bound for prescribed original Möbius coefficients; it is not another event-equivalent criterion.

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
Every upper statement below assumes RH, and every constant may depend on the one fixed extension. Neither simplicity nor an inverse-derivative moment is assumed. The coefficients remain the original finite Möbius coefficients multiplied by the declared taper.

The reviewed conclusions have the following distinct scopes.

| Claim | Checked conclusion | Essential restriction |
|---|---|---|
| GC1–GC23 | Uniform domination by \((3+|t|)^{(\sigma-1)/2+\eta}\); an integrable uniform height tail; \(E_{N,w}\to0\) | One fixed compact Gevrey extension, \(1<\sigma<2\) |
| QR1–QR12 | \(E_{N,w}\ll_{W,B}(\log\log N)^B/\log N\), for each fixed \(B>1+2\sigma\) | Constants are not uniform over changing tapers |
| CH1–CH14 | Exact first-order norm on each fixed compact height interval, with remainder \(O_{T,w}(\log L/L^2)\) | Endpoints avoid zero ordinates; height remains fixed |
| PM1–PM6 | The complete weighted series of limiting local costs converges | A limiting-series bound, distinct from the actual norm tail |
| JL1–JL16 | A joint-scale lower rate for specified almost-linear moving tapers at an exact order-\(m\) event | The complete moving-kernel and remote-height budgets are paid separately |

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

## 3. Quantitative rate and the distance corollary

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
The implied constant includes that fixed choice of extension. This is a direct corollary of the written upper proof, not a claim about a best-known rate. Its growing logarithmic allowance is compatible with the classical multiplicity-squared lower bound. No estimate at the simple-zero leading constant is obtained.

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

Neither fact permits a first-order global exchange of limits. The actual GC height tail has no factor \(1/L\), while CH has constants depending on its fixed height. QR still bounds \(LE\) by a growing power of \(\log L\). Thus the convergence of the limiting profile series does not establish that it equals \(\lim LE\).

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

No opposing upper bound is available for this moving family. Applying GC or QR with constants silently uniform in \(\eta_N\) would be invalid. Nor is there a claim at layer width comparable to \(1/L\).

## 6. Review record and remaining scope

The consolidated record uses three separate same-model review paths: phase, arithmetic, and Gaussian. The coordinator also independently checked the principal global and rate derivations. Coverage is explicit: the global GC proof received independent phase and Gaussian audits in addition to the coordinator's check; the QR proof received phase, arithmetic, and Gaussian audits. CH and JL received separate checks of their constants, annuli or growing windows, and complete tail payments. PM was checked separately from the actual-height argument. These are separate analytic checks within the same model family, not independent specialist validation.

The earlier bounded Lean artifact for the abstract two-cost projection identity formalizes none of GC, QR, CH, PM, or JL. No analytic Lean proof, machine-checked contour argument, or formal verification of the global approximation theorem is claimed here.

The anchor-direction correction is resolved. No blocking mathematical error remains in the reviewed versions. The fixed-taper upper theorem is a substantive change from a merely local lower-bound program, but it remains compatible with multiple zeros. A sharp global \(1/L\) upper constant, a uniform theorem for the changing tapers, and a signed arithmetic or winding estimate that excludes an original multiple zero remain unproved. No novelty, optimality, or specialist-review claim is attached to this checkpoint.
