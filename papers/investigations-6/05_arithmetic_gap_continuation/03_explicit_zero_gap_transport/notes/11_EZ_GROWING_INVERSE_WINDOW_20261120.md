# E10 R1 · A growing counted inverse window

20 November 2026. Prepared for Edward Baker with OpenAI Codex LLM assistance, recorded bounded dispatch **gpt-6.2-sol, ultra**. **Proved in-note**, accepted in the [separate internal assessment](../reviews/05_EZ_GROWING_WINDOW_ASSESSMENT_20261120.md). This is a quantitative position and adjacent-gap estimate at one sufficiently large physical time. The inputs are the complete theta source and the fixed inverse definitions of [parent Note 08 §§3–4](../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md) and [manuscript anchors](../manuscript/anchors.tex), frozen by [E10 R1](../research-progress/handoffs/AGC_EZ_E10_REQUEST_R1_20261120.md).

## 1. The Gaussian-relative disk

Use the frozen notation
\[
 p(u)=Tu^2+9u-\pi e^{4u},\quad 4\pi e^{4L}=2TL+9,\quad
 \kappa=8TL-2T+36,\quad S=\kappa+2T .
\]
Write \(W=\sqrt\kappa(U-L)\), \(a=\mathbb E_T U\), \(\mu=\mathbb E_T W\), \(\ell=a\sqrt\kappa\), and \(\alpha=2S/(3\kappa^{3/2})\). Put
\[
 r=\tfrac12\sqrt{\log\kappa},\qquad D=\ell r,\qquad
 E=O\!\left(\kappa^{-1}(1+r^6)e^{r^2/2}\right)
     =O\!\left(\kappa^{-7/8}(\log\kappa)^3\right).
\]
Here \(E\) denotes the nonnegative error bound specified in §2.

Extend the unnormalized density of \(W\),
\[
 F(w)=(2\pi)^{-1/2}e^{p(L+w/\sqrt\kappa)-p(L)}b(L+w/\sqrt\kappa),
\]
by zero for \(w<-L\sqrt\kappa\), where \(b\) is the full theta factor from the manuscript. With \(g(w)=(2\pi)^{-1/2}e^{-w^2/2}\), the frozen central estimate on \(|w|\le w_0=\kappa^{1/12}\) reads
\[
 |F(w)-g(w)(1-\alpha w^3)|\le A\,g(w)(1+w^4+w^6)/\kappa .
\]
For \(\zeta=\xi+i\eta\), absolute integration of this error against the Fourier weight uses \(e^{-\eta w}\). Completing the real Gaussian square gives \(e^{\eta^2/2}\) times the polynomial moment of \(G-\eta\), where \(G\) is standard Gaussian. Division by \(e^{-\zeta^2/2}\) therefore costs \(e^{\xi^2/2}\) times the polynomial moment. This gives \(O(\kappa^{-1}(1+r^6)e^{r^2/2})\) uniformly for \(|\zeta|\le r\).

For \(w\ge-\sqrt\kappa/4\) outside the central interval, the complete-source Gaussian majorant costs at most a constant times \(e^{-c w^2+r|w|}\). Since \(r/w_0\to0\), for all sufficiently large \(T\) this is bounded by \(e^{-cw^2/2}\) times that constant. The Gaussian model tail obeys the same estimate with a polynomial factor and another fixed \(c>0\). For \(-L\sqrt\kappa\le w<-\sqrt\kappa/4\), the far-left weight costs at most \(L\sqrt\kappa\,e^{-c_L\kappa+rL\sqrt\kappa}\) times a constant, where \(c_L\) stays bounded below. Here
\[
 rL/\sqrt\kappa=O\!\left((\log\kappa)^{3/2}/\sqrt\kappa\right)\to0 .
\]
Division by the Gaussian costs at most \(e^{r^2/2}\) on either tail. Their relative contributions are smaller than every inverse power of \(\kappa\). The growing weight thus retains the half-line endpoint.

Integrating the model exactly gives \(e^{-\zeta^2/2}(1+i\alpha(\zeta^3-3\zeta))\). At zero the normalization is \(1+O(\kappa^{-1})\). On the full disk, the Gaussian-relative perturbation of one is \(O(\alpha(r+r^3)+E)=o(1)\). Its logarithm differs from \(i\alpha(\zeta^3-3\zeta)\) by \(O(E)\), since the squared-error cost is \(O(\alpha^2(r+r^3)^2+E^2)=O(E)\). The linear coefficient of this logarithmic error is \(i(\mu+3\alpha)\). Cauchy's estimate at zero bounds its contribution on the disk by the same uniform error. With \(K_0(y)=\log\mathbb E_T e^{iy(U-a)/a}\) continued from zero this proves
\[
 \sup_{|\zeta|\le r}\left|K_0(\ell\zeta)+\tfrac12\zeta^2-i\alpha\zeta^3\right|\le E .
 \tag{1}
\]
Centering uses the exact \(a\). In particular \(\mu+3\alpha\to0\) and \(a\sim L\). The sharper fixed-disk mean estimate in the manuscript remains available separately.

## 2. A finite source and disk test

The following inequalities can be checked at a specified \(T\). Enclose the large saddle and the mean with justified errors, or take them as exact. Require \(w_0\le\sqrt\kappa/4\), \(L\ge1/4\) and
\[
 c=\frac{S/e-2T}{2\kappa}>0,\qquad
 \Delta=\min\{p(L)-p(0),c\kappa/16\}>0 .
\]
On \(u\ge L-1/4\), the inequality \(p''(u)\le-2\kappa c\) gives \(p(u)-p(L)\le-cw^2\). On the remaining interval \(p''\) is decreasing. The convex portion has its maximum at one of its endpoints, and the concave portion up to \(L\) is increasing. Thus the far-left maximum is at zero or at \(L-1/4\), giving the upper bound \(p(L)-\Delta\). These constants are admissible eventually since \(c\to1/(2e)\) and \((p(L)-p(0))/\kappa\to\infty\).

A global upper bound for \(b\) is \(b_*=(1-16e^{-3\pi})^{-1}\). For the central interval use
\[
 b_{\rm err}=\frac{24e}{S}+\frac{v_b}{1-v_b},\qquad
 v_b=16e^{-3S/(16e)}<1 .
\]
Indeed \(n^4\le16^{n-1}\), \(n^2-1\ge3(n-1)\) for \(n\ge1\), and \(\pi e^{4u}\ge S/(16e)\) on the central interval. These give the geometric higher-mode tail and the stated bound for \(|b-1|\). Define
\[
 \beta=\frac{2eS}{3\kappa},\qquad
 V=\alpha w_0^3+\beta w_0^4/\kappa,\qquad
 A=e^V\max\{\kappa b_{\rm err},\beta,\kappa\alpha^2/2\}.
\]
Taylor's formula for \(p(L+w/\sqrt\kappa)-p(L)\) bounds its remainder after the quadratic and cubic by \(\beta w^4/\kappa\). Changing the exponent costs at most \(e^V\) times its error. The quadratic remainder for the cubic exponential and the bound for \(b-1\) give the central density estimate with this \(A\).

For any \(s\ge0\) use
\[
\begin{split}
 D_s=e^{s^2/2}\Bigl[&
 \frac{A}{\kappa}(19+51s^2+16s^4+s^6)\\
 &+\int_{|w|>w_0}e^{s|w|}
 \left(\frac{b_*}{\sqrt{2\pi}}e^{-c w^2}
                  +g(w)(1+\alpha |w|^3)\right)dw\\
 &+\frac{b_*}{\sqrt{2\pi}}L\sqrt\kappa\,e^{-\Delta+sL\sqrt\kappa}\Bigr].
\end{split} \tag{2}
\]
This bounds the Gaussian-relative unnormalized error on \(|\zeta|\le s\). The central polynomial is one plus the fourth and sixth shifted Gaussian moments. The tails in (2) may be bounded by elementary Gaussian integrals. For \(D_0<1\) let
\[
 P=\alpha(r^3+3r),\qquad
 \epsilon=\frac{D_r+(1+P)D_0}{1-D_0},\qquad
 v=P+\epsilon.
\]
The normalized Gaussian-relative transform is then \(1+i\alpha(\zeta^3-3\zeta)+e(\zeta)\), with \(|e|\le\epsilon\). Require \(v<1\). The series for \(\log(1+h)\) bounds the error after the linear term by \(v^2/[2(1-v)]\). Cauchy's bound for the centering correction gives the following explicit choice in (1):
\[
 E=2\left(\epsilon+\frac{v^2}{2(1-v)}\right).
 \tag{3}
\]
The estimates in §1 give the stated eventual order of (2)–(3) when \(r=\tfrac12\sqrt{\log\kappa}\). No specified physical time was tested.

## 3. Inverse radius, exact count and errors

Set \(\Psi(y)=-(K_0(y)-K_0(-y))/(2i)\), \(\theta(y)=y-\Psi(y)\), and \(c_1=\gamma_3/(6a^3)\) with the exact third cumulant. Let \(M=\alpha r^3+E\), \(B=M/6\), \(Q=D/2-B\). Require \(M\le D/4\), which holds eventually. We have \(\sup_{|y|\le D}|\Psi(y)|\le M\). Cauchy bounds its coefficient majorant at \(D/2\) by \(B\), because the odd sum starts in degree three. On \(|y|=D/2\) and \(|q|<Q\), \(|y-q|>B\). Rouché counts one simple preimage \(Y(q)\) of \(q\) there. The preimages give a single holomorphic inverse by uniqueness, with \(|Y-q|\le B\). The argument also works after replacing all odd coefficients by their absolute values. For that inverse the coefficient polynomials of [parent Note 08 (3)](../../brainstorm/notes/08_SUMMING_THE_LARGE_TIME_ZERO_LOOP_20261120.md) are nonnegative and dominate individual terms of the full formula.

The real inverse increases from zero. In fact \(|\Psi'|\le2M/D\le1/2\) for \(|y|\le D/2\), and conjugation preserves the unique preimage over real \(q\). The complete field at physical position \(x=y/a\) has a nonzero exponential factor times \(\cos\theta(y)\). The crossings on \(0\le q\le D/4\) give all positive zeros through \(Y(D/4)/a\), simple and counted from the origin. Exactly the following indices are retained:
\[
 q_k=(k-\tfrac12)\pi,\qquad
 1\le k\le K(T)=\left\lfloor\frac{\ell\sqrt{\log\kappa}}{8\pi}+\frac12\right\rfloor .
 \tag{4}
\]
Thus \(C(T)=\sqrt{\log\kappa}/8\) in \(q_k\le C(T)\ell\). In physical units \(x_k=Y(q_k)/a=q_k/a+O(M/a)\), uniformly. In particular
\[
 K(T)\sim\frac{\sqrt2}{32\pi}\sqrt T(\log T)^2,\qquad
 x_{K(T)}\sim\frac{\sqrt2}{8}\sqrt T\log T ,
\]
using \(L\sim(\log T)/4\), \(\kappa\sim2T\log T\) and \(\log\kappa\sim\log T\). The count concerns positive real zeros through this height. It supplies no rank or spacing condition on the exterior.

For the cubic let \(Y_3-c_1Y_3^3=q\) on the branch through zero. Apply the same Rouché argument to \(c_1y^3\), whose majorant at \(D/2\) is at most \(B\). The odd remainder \(\Psi(y)+\alpha(y/\ell)^3\) is bounded by \(E\) on \(|y|\le D\) and vanishes to third order. In particular
\[
 |c_1\ell^3+\alpha|\le E/r^3,\qquad
 |J(y)|=|\Psi(y)-c_1y^3|\le2E(|y|/D)^5 .
 \tag{5}
\]
For the second bound subtract the exact cubic and apply the maximum principle to the quotient by \(y^5\). Eventually \(c_1<0\), since \(E/(\alpha r^3)\to0\). On the two inverse branches,
\[
 (Y-Y_3)\{1-c_1(Y^2+YY_3+Y_3^2)\}=J(Y).
\]
The factor has modulus at least \(1-3M/(4D)\ge13/16\). Since \(|Y|<D/2\), \(|Y-Y_3|\le E\) on \(|q|<Q\). This difference vanishes to fifth order at zero. Apply the maximum principle to \((Y-Y_3)/q^5\), then differentiate with Cauchy's estimate. With \(q=q_k\), \(q'=q+\pi=q_{k+1}\) and \(q'\le D/4\), we obtain
\[
 \left|x_k-\frac{Y_3(q)}{a}\right|
 \le \frac{E}{a}\left(\frac{q}{Q}\right)^5,\qquad
 \left|x_{k+1}-x_k-\frac{Y_3(q')-Y_3(q)}a\right|
 \le \frac{7\pi E}{aQ}\left(\frac{q'}{Q}\right)^4 .       \tag{6}
\]
Indeed \(Q\ge3D/8\), so for \(0\le z\le D/4\) the differentiated quotient has factor \(5+z/(Q-z)\le7\). The spacing itself is \((\pi/a)(1+O(M/D))=(\pi/a)(1+O(\kappa^{-1}))\), by \(Y'=1/(1-\Psi'(Y))\). Across the retained window the cubic positional error is \(O(\kappa^{-7/8}(\log\kappa)^2)\) in physical units. Its neighboring error is \(O(\kappa^{-11/8}(\log\kappa)^{3/2})\) in units of \(\pi/a\). Equation (6) retains a stronger small-index dependence.

## 4. Finite coefficients, their errors and the direct comparison

With exact \(a\), the inverse polynomial through degree \(2N+1\) needs odd cumulants through that degree. For \(s=q/Q\le2/3\), the remaining positional error is at most
\[
 \frac{B}{a}\frac{s^{2N+3}}{1-s^2}.
\]
For a neighboring difference use \(s=q'/Q\) and replace the factor after \(B/a\) by
\[
 \frac{\pi}{Q}\left(\frac{(2N+3)s^{2N+2}}{1-s^2}
                     +\frac{2s^{2N+4}}{(1-s^2)^2}\right).
\]
These are the Cauchy bounds for the Taylor tail and its derivative on a segment. If the computed coefficient of \(q^{2j+1}\) has error at most \(d_j\), add \(\sum_j d_j q^{2j+1}/a\) in position and \((\pi/a)\sum_j(2j+1)d_j(q')^{2j}\) in spacing. Enclosing the polynomial expressions in the supplied cumulant intervals gives admissible \(d_j\).

One can also perturb the phase inputs. At common exact coordinates let the errors in a finite polynomial for \(\Psi\) have coefficient bounds \(\epsilon_j\). Their envelope on \(|y|\le D/2\) is \(\sum_j\epsilon_j(D/2)^{2j+1}\). An omitted coefficient tail requires an analytic envelope, such as the Cauchy geometric sum from \(M\). If the total \(\delta\) satisfies \(D/4+B+\delta<D/2\), the perturbed inverse exists on a disk containing the retained \(q\)-interval. Subtract the two inverse equations and use the true phase bound \(2M/D\le1/2\) on the convex \(y\) disk to get \(|\widehat Y-Y|\le2\delta\). The adjacent-difference improvement from Cauchy uses the remaining strict complex radius.

For the cubic, if \(|\widehat c_1-c_1|\le d_c\) with \(d_cD^2\) sufficiently small, the same complex-disk argument keeps both cubic inverses with room beyond \(D/4\). Subtract their equations, factor the cubic difference and use the strict denominator bound. The inverse difference is \(O(d_cD^3)\) there and vanishes to order three. Division by \(q^3\) and Cauchy's estimate give \(O(d_cq^3)\) in position in \(y\) and \(O(\pi d_c(q')^2)\) in its adjacent difference. If \(|\widehat a-a|\le d_a\le a/2\), converting with \(\widehat a\) adds scale errors \(O(d_aq/a^2)\) and \(O(\pi d_a/a^2)\) in physical units. The coefficient error must include the uncertainty in the normalization used to form \(\widehat c_1\). At the outer scale \(q\asymp D\), sufficient orders to preserve (6) are \(d_c=O(E/D^3)\) and \(d_a=O(aE/D)\). Smaller indices have tighter budgets if the fifth-order savings in (6) are required.

The disk/count input cannot be replaced by the first \(m\) moments of an unrestricted positive source. Start with the strictly positive half-line density and add a fixed smooth nonnegative bump translated to height \(R\) with weight \(R^{-m-1}\). Its contributions to moments of degrees \(0,\ldots,m\) are \(O(R^{-1})\). Choose \(m+1\) interior bumps with an invertible moment matrix by taking sufficiently small supports about distinct positive points. Subtract a linear combination of these with the matching moment vector. The coefficients tend to zero, so for large \(R\) positivity and total mass one are preserved, with all specified moments exactly the same. The exponential moment at every fixed positive rate is unbounded in this family. These alternatives need not satisfy the uniform canonical envelope. A truncation degree alone thus supplies neither the inverse remainder nor the unobserved zero count. The local contour requires complete circle error and real clearance in addition to finite sampled derivative orders. A bound on the unobserved exterior also requires additional information.

For the matched direct calculation use (1) and (5). On the real interval the phase \(\theta\) increases from zero, so the same \(q_k\) count follows by crossing. For \(\theta_3(y)=y-c_1y^3\) the inequality \(|\theta(y)-\theta_3(y)|\le2E(|y|/D)^5\) gives signed brackets by testing \(\theta_3(y)-q_k\) against that error on either side of the cubic position. With \(c_1<0\) the real cubic has slope at least one. The shared holomorphic bound and difference equation give the adjacent scale (6) also for direct phase localization. In the field formulation the sign tests use the positive exponential factor on the real interval. Over \(|y|\le D/2\) this factor is at least \(e^{-r^2/8-E}\) by (1). An absolute field error must be scaled by that amplitude to recover the same phase clearance. The inverse lets the coefficients be reused across ranks. Direct bracketing gives the same positional and adjacent-error orders with the same cubic and analytic bounds. A comparison using additional complete-source evaluations would have different inputs.

## 5. Scope and controls

The milestone is the larger explicit family (4), measured by its count and physical errors (6). It concerns one asymptotically large physical time. A fixed-time overlap with published high-index estimates, an exterior count and a backward interval remain open at this stage. The complete source is used in (1)–(3). Euler-factor controls change the theta coefficients and \(b\). Weighted-square controls change the unit weights and full reflection. The reflected controls lack the canonical square expansion, and the smooth and primitive-compatible controls lack the normalized arithmetic theta expansion. Finite-prime, finite-profile and finite-tail variants also fail the complete-source identity even when selected observations agree. The changed-observation controls fail the literal cosine. Each case needs its own analytic envelope. The inversion and count apply to a control wherever it satisfies the same quantitative inequalities, with the resulting exclusion confined to that disk. [Inherited branch screen](07_EZ_ZERO_FORMULAS_AND_MIXED_HIERARCHY_CONTINUATION_20261120.md) · [Result index](../../../../../result-summaries/README.md) · [Control catalogue](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns index](../../../../../avoid/README.md) · [Milestone classification](../../../../../avoid/01_restating_the_target.md) · [Control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) · [Scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
