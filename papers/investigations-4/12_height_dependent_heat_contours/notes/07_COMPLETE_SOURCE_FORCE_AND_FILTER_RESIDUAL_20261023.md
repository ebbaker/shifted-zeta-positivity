# Complete source force and the filtered pair residual

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Status: **proved finite force/error estimates under the stated hypotheses; no new theta spectral upper bound**. Internal same-model review is recorded separately; no specialist review or priority claim.

This continuation follows the [program](../research-overview/02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md), [result index](../../../../result-summaries/README.md), [heat geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [theta-source register](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and [avoid index](../../../../avoid/README.md), especially [target classification](../../../../avoid/01_restating_the_target.md), [controls](../../../../result-summaries/12_collision_controls_and_screening.md), [coupled estimates](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The new quantitative output is a complete-theta distant-force error of order \(N C_T(1+\log R_c)/R_c\) for the derivative of the bounded filter, with no internal-gap denominator and no \(1/t\) loss. A second result controls the same force from a **relative wall-value error**, without differentiating that error. These are useful finite approximation estimates, not reformulations of simplicity and not proofs that the remaining local force has a favorable signed budget. HDC-07's near-source residual problem and HDC-10 remain open.

## 1. Declared population and the exact coupled quantity

Use the unchanged field
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\qquad
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\quad H_t=-H_{zz}.
\]
Fix \(0<t_0<T<\infty\) and a tracked finite population of \(N\ge2\) distinct real roots \(x_i(t)\), lying in \([-A,A]\). For wall statements the population must be exactly all roots in the stated wall, counted with multiplicity. No root enters or leaves. At each simple time write \(H=UP\), \(P=\prod_i(z-x_i)\), and \(b=U_z/U\). Put
\[
v_{ij}=e_i-e_j,\quad W_{ij}=(x_i-x_j)^{-2},\quad
L=\sum_{i<j}W_{ij}v_{ij}v_{ij}^T,\quad
R=(I+4tL)^{-1},\quad F=I-R,\quad q=\operatorname{Tr}F.
\]
The generic finite algebra in this section requires real simple roots, not RH. **RH first enters in Section 2**, where it supplies the complete canonical real-root product and the all-real exterior.

Write \(D_{ij}b=(b(x_i)-b(x_j))/(x_i-x_j)\), and
\[
c_{ij}=W_{ij}\|Rv_{ij}\|^2,\qquad J=\operatorname{Tr}(FR).
\]
The complete root equation and differentiation of the resolvent give
\[
x_i'=2\sum_{j\ne i}(x_i-x_j)^{-1}+2b(x_i),
\]
\[
q'=4\sum_{i<j}c_{ij}\left[1-8tW_{ij}
 +4t\sum_{k\ne i,j}\frac1{(x_i-x_k)(x_j-x_k)}
 -4tD_{ij}b\right].                                      \tag{1}
\]
In particular the exterior-force contribution is
\[
Q_b=-16t\sum_{i<j}c_{ij}D_{ij}b.                          \tag{2}
\]
These are the inherited complete equations, organized to retain \(L+tL'\). The filter identity that makes their error estimates usable is
\[
\sum_{i<j}c_{ij}=\operatorname{Tr}(R^2L)=\frac{J}{4t},
\qquad 0\le J\le\min\{q,(N-1)/4\}.                       \tag{3}
\]
To prove the bound, diagonalize the real symmetric \(4tL\); its nonzero eigenvalues \(a\) contribute \(a/(1+a)^2\le1/4\), and each contribution is at most \(a/(1+a)\). The constant mode contributes zero. This does not assume that \(L\) commutes with \(L'\).

Consequently, if an approximation to the **divided differences** has error at most \(\beta(t)\), evaluated on the same actual population and with the same actual \(R\), then
\[
|Q_b-Q_{\widetilde b}|\le4\beta J
 \le\beta\min\{4q,N-1\}.                                 \tag{4}
\]
This is a force error estimate, not a comparison of filters computed on different roots. Root/population errors require their own estimate, as in [Note 09](09_BACKWARD_FILTER_TRANSPORT_AND_TERMINAL_PRECISION_20261023.md).

## 2. A paid canonical distant-force bound

Assume RH and use the complete paired product established in [BW10 Note 19][motion]:
\[
H(t,z)=H(t,0)\prod_{r>0}(1-z^2/r(t)^2).
\]
There is no spatial linear exponential factor. Individual reciprocal sums are paired; their divided differences converge absolutely. The exterior unit therefore obeys
\[
D_{ij}b=-\sum_{r\notin\{x_1,\ldots,x_N\}}
 \frac1{(x_i-r)(x_j-r)}.                                  \tag{5}
\]
If the selected population is a consecutive real block, every omitted real root is outside its convex hull and every summand is positive before the minus sign. Thus \(Q_b\ge0\): the exterior force raises \(q'\). This sign is compatible with the known late-time compression and is **not** a useful upper bound for \(q\) by itself. For a nonconsecutive population, omitted roots between selected roots need not have this sign; the distant-tail statement below still holds.

For completeness the explicit canonical constants imported from that note are
\[
C_b^*=(1-16e^{-3\pi})^{-1},\quad C_\Phi=2\pi^2 C_b^*,\quad
h_*=\frac{\pi(2\pi-3)}4e^{-\pi e},
\]
\[
B_T=T/e^2+9/(2e),\quad D_T=B_T^2/(2\pi),\quad
A_T=\log(C_\Phi/(2h_*))+D_T,\quad C_T=(A_T+1)/(2\log2).
\]
Complete-source Jensen estimates prove, uniformly for \(0\le t\le T\),
\[
\sum_{|r|>R_c}\frac1{r^2}\le
\mathcal B_T(R_c)=\frac{2C_T(\log R_c+2)}{R_c},\qquad R_c\ge2. \tag{6}
\]
This pays every theta index and the entire distant zero tail; it is not a fitted density estimate. The underlying complex zero count does not require RH; the real-root use in (5) does.

Choose a spatial cutoff \(R_c>A\), \(R_c\ge2\), and retain every exterior root with \(|r|\le R_c\) in (5). Call the resulting derivative in (1) \(q'_{\le R_c}\), keeping the **exact internal roots and filter**. For \(|x_i|\le A\),
\[
0\le\sum_{|r|>R_c}\frac1{(x_i-r)(x_j-r)}
\le\beta_{T,A}(R_c):=
\frac{\mathcal B_T(R_c)}{(1-A/R_c)^2}.
\]
Equations (2)--(4) now prove
\[
\boxed{0\le q'-q'_{\le R_c}\le4\beta_{T,A}(R_c)J
 \le\beta_{T,A}(R_c)\min\{4q,N-1\}.}                       \tag{7}
\]
For \(R_c\ge2A\), the last bound is at most
\[
4(N-1)\mathcal B_T(R_c)
=\frac{8(N-1)C_T(\log R_c+2)}{R_c}.                       \tag{8}
\]
The constant \(A\) can be supplied independently of unknown internal gaps by the finite rank enclosure in [BW10 Note 19][motion], RM9--RM11, or by an acquired complete wall. It is not a uniform-in-height constant unless the chosen population supplies one.

**Integrated form.** With the same fixed \(T,A,R_c\),
\[
0\le \int_{t_0}^T(q'-q'_{\le R_c})dt
\le(T-t_0)(N-1)\beta_{T,A}(R_c).                          \tag{9}
\]
For a bounded upper time \(T\), populations with \(A=A_h\), and any source-prescribed cutoffs \(R_{c,h}\ge2A_h\) tending to infinity, the normalized derivative-tail error is \(O_T(\log R_{c,h}/R_{c,h})\), hence tends to zero. If \(T\) grows, \(C_T\) and the interval length must be retained; no uniform large-heat conclusion follows. In the signed backward formula the nonnegative omitted term is subtracted, so dropping it gives a conservative upper estimate; it cannot be claimed as a measured gain.

This improves the singular raw-pair error: replacing \(\|Rv\|\) by \(\|v\|\) gives \(32t\beta\sum W_{ij}\), which can be arbitrarily large for small gaps. Equation (7) stays bounded by \((N-1)\beta\). It also replaces an unacquired whole-wall logarithmic-derivative bound for the **distant** contribution by the explicit \(O(\log R_c/R_c)\) source tail. It does not control the retained nearby exterior roots, or establish cancellation between those roots and the internal term in (1).

## 3. Relative wall values control the remaining analytic force

Let \(\Gamma\) be a piecewise \(C^1\) Jordan wall of length \(\ell_\Gamma\). Let \(H\) and a reference \(G\) be holomorphic in its interior and a neighborhood of its closure. Assume \(G\ne0\) on the wall and
\[
\sup_\Gamma |H/G-1|\le\eta<1.                            \tag{10}
\]
Rouche gives equal interior zero counts. Define the exterior logarithmic derivatives \(b_H,b_G\) by removing **all** their respective interior zeros. The zeros of \(G\) need not coincide with those of \(H\). There is a single-valued wall logarithm
\[
\ell(w)=\log(H/G)(w),\qquad |\ell(w)|\le\varepsilon_\ell:=-\log(1-\eta).
\]
It is holomorphic in a thin annulus around the wall, even if \(H/G\) has zeros and poles deeper inside. Cauchy subtraction and integration by parts give, for every interior \(z\),
\[
b_H(z)-b_G(z)=\frac1{2\pi i}\oint_\Gamma\frac{\ell(w)}{(w-z)^2}\,dw,
\]
\[
D_{ij}(b_H-b_G)=\frac1{2\pi i}\oint_\Gamma\ell(w)
\left[\frac1{(w-x_i)^2(w-x_j)}+
\frac1{(w-x_i)(w-x_j)^2}\right]dw.                         \tag{11}
\]
Although the usual \(H_z/H\) representation has internal poles, their Cauchy contributions cancel against the prepared polynomial. This is why (11) remains meaningful through internal collisions when evaluated as analytic divided differences.

If every selected \(x_i\) lies distance at least \(d>0\) from \(\Gamma\), then
\[
\beta_{\rm wall}=\frac{\ell_\Gamma}{\pi d^3}\varepsilon_\ell,
\qquad |Q_{b_H}-Q_{b_G}|\le4\beta_{\rm wall}J.             \tag{12}
\]
No derivative error for the approximation in (10) is needed, and no internal gap floor appears. The full correlated contour expression (11), summed with \(c_{ij}\), can be used before taking an absolute value. Equation (12) is its safe fallback, not a claim that the correlated integral is smaller for theta.

For an affine exterior reference \(b_G(z)=a z+c\), its exact contribution is \(-4aJ\); a constant contributes zero. More generally all known \(b_G\) stays inside (1). Compared with the original absolute fallback
\[
\beta_{\rm abs}=\frac{\ell_\Gamma}{2\pi d^2}\sup_\Gamma|H_z/H|,
\]
the residual error in (12) is smaller than that whole-force fallback whenever
\(2\varepsilon_\ell/d<\sup|H_z/H|\). This compares a residual error with an unreferenced whole-force bound; it does not assert total-estimate improvement without paying \(b_G\). For a comparison using the same retained reference, replace \(\sup|H_z/H|\) by \(M_{\rm rel}=\sup|H_z/H-G_z/G|\) in the derivative fallback. Then (12) is smaller if \(2\varepsilon_\ell/d<M_{\rm rel}\); neither residual fallback universally dominates the other. The improved estimate can be zero for an exact reference even when the individual logarithmic derivative is large. If (10) is not acquired, there is no improvement to report. See [Note 08](08_CURVED_CONTOUR_TRANSPORT_AND_HEIGHT_GRAPH_20261023.md) for the associated polynomial and discriminant bounds.

## 4. Explicit complete-source wall acquisition error

The wall bound (10) is an acquisition gate. The following gives explicit full-source errors for it, not an assertion that any proposed wall satisfies the gate.

For complex time with \(\Re\tau\le T\), \(T\ge0\), and \(|\Im z|\le Y\), choose \(Y,U\ge0\) and an integer \(n_0\ge1\), and truncate the defining source to \(n\le n_0\) and \(0\le u\le U\), retaining both polynomial terms exactly; call this holomorphic finite-integral approximation \(H_{n_0,U}\). Put
\[
\mathfrak b=T/e^2+(9+Y)/(2e),\qquad m=n_0+1,
\qquad \rho_m=16e^{-\pi(2m+1)}<1,
\]
and let \(\Gamma(0,x)=\int_x^\infty e^{-v}dv/v\). Then
\[
|H-H_{n_0,U}|\le E_{n_0,U}(T,Y):=
\frac{\pi^2m^4}{2(1-\rho_m)}e^{\mathfrak b^2/(2\pi m^2)}
\Gamma(0,\pi m^2/2)
+\frac{C_\Phi}{4}e^{\mathfrak b^2/(2\pi)}
\Gamma(0,(\pi/2)e^{4U}).                                 \tag{13}
\]
**Proof.** On \(u\ge0\) each theta summand is positive, bounded by \(2\pi^2n^4 e^{9u-\pi n^2e^{4u}}\). Consecutive \(n\ge m\) positive majorants have ratio at most \(16e^{-\pi(2m+1)}\), so the whole omitted index tail is bounded by its first term divided by \(1-\rho_m\). Also \(u^2\le e^{2u}/e^2\) and \(u\le e^{2u}/(2e)\), hence
\[
Tu^2+(9+Y)u-\pi m^2e^{4u}
\le\frac{\mathfrak b^2}{2\pi m^2}-\frac{\pi m^2}{2}e^{4u}.
\]
Substitution \(v=(\pi m^2/2)e^{4u}\) bounds the index-tail integral on the entire half-line. The complete source bound \(\Phi\le C_\Phi e^{9u-\pi e^{4u}}\) gives the second term for \(u>U\). This overcounts their overlap safely. Finally \(|\cos(zu)|\le e^{Y u}\) and \(|e^{\tau u^2}|\le e^{Tu^2}\).

Any quadrature error must be added. If a reference \(G\) has acquired wall floor \(m_G=\inf_\Gamma|G|>0\), and an acquired bound \(E_{\rm ref}\ge\sup_\Gamma|H_{n_0,U}-G|\), then (10) follows with
\[
\eta=(E_{n_0,U}+E_{\rm ref})/m_G<1.                       \tag{14}
\]
In particular \(G=H_{n_0,U}\) still requires its wall floor and its complete interior count/factor. Finite-source nonreal zeros outside this wall are irrelevant to the local comparison and cannot be assigned theta's global reality.

At fixed \(T,Y\), (13) tends rapidly to zero as \(n_0,U\to\infty\); the bound itself is independent of \(\Re z\). That independence is not a high-height advantage: the required floor may decay sharply with height. Equations (13)--(14) retain the exact place where complete oscillatory cancellation and relative accuracy must be acquired. Source positivity or a moment majorant alone supplies no positive real-axis wall floor.

## 5. Controls, interpretation, and next task

* For \(H=z^2-2t\), \(b=0\), \(q=1/2\), and the **whole** bracket in (1) vanishes. A force error bound does not force \(q\) to vanish. Pure Hermite births likewise have \(L+tL'=0\), while every collision mode survives in \(F\).
* For \(H=z^2-a_0^2-2t\), \(q=2t/(a_0^2+4t)\). Equation (1) gives \(q'=2a_0^2/(a_0^2+4t)^2\); its pole at complex time \(-a_0^2/4\) is a distinct resolvent obligation.
* For \(H=e^{k^2t}\sin(kz)\), roots are stationary, so \(q'>0\) for any nontrivial finite block. Its exact exterior \(b(x_i)=-\sum_{j\ne i}(x_i-x_j)^{-1}\) cancels internal root velocity. Dropping that force gives the wrong derivative.
* The Euler-factor and close positive-endpoint controls can satisfy appropriate real-root local identities, but change the canonical source. Close endpoint controls fail ordinary Dirichlet arithmetic; small relative source tolerance alone cannot give uniform all-height simplicity. Weighted-square controls do not have a global all-real time and fail full reflection. Reflected/smooth/primitive-compatible controls lack the unchanged integer-square expansion. The generic wall lemma applies to any of them on a valid local wall; it makes no collision exclusion there. Their exact failed premises are recorded in [control register 12](../../../../result-summaries/12_collision_controls_and_screening.md).

Equations (7)--(9) are a quantitative **canonical source tail milestone**: the distant force can be truncated with a paid, collision-uniform filtered error. Equations (11)--(14) supply a finite relative-error acquisition interface and a precise comparison with the absolute fallback. Neither estimate bounds the retained local coupled expression in (1) below the needed threshold. The scoped failure is that *distant-tail smallness plus local force identities* does not bound \(q\); exact polynomial births already have zero tail and nonzero \(q\). This does not exclude using exact theta correlations in the retained local expression.

The next source task is to bound that retained expression or acquire relative wall information at a source-prescribed microscopic time/height scale. A terminal-reference approach must pay [Note 09's](09_BACKWARD_FILTER_TRANSPORT_AND_TERMINAL_PRECISION_20261023.md) backward error; a high-height estimate must pay [Note 10's](10_EXACT_COLLISION_SPECTRUM_AND_GLOBAL_REDUCTION_20261023.md) short-gap population, not merely the average density. HDC-07 is advanced but its full useful residual remains unacquired; HDC-10 and HDC-11 are not complete.

[motion]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
