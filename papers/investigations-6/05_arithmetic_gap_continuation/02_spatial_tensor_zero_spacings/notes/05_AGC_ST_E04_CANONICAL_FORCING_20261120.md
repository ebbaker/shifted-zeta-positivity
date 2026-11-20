# Complete forcing for common high labels on a positive-time slab

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. Executor dispatched as gpt-6.2-sol, effort ultra. Serving configuration has no separate attestation. AGC-ST-E04 r1, proof on the stated slab, pending separate assessment.

Fix \(I=[t_0,t_*]\subset(0,1/2]\) for the literal theta field. The inherited inputs are the common-time high clock positions and projected unit count of [Polymath v2, Theorem 1.5(i), (ii), (iv) and §9](https://arxiv.org/pdf/1904.12438v2#page=10), the exact complete laws of [AGC §4](../../manuscript/sections/04_continuation.tex), and the [E03 signed estimate](04_AGC_ST_E03_PAIRED_FORCING_20261120.md). The [B03 decision](../brainstorm/notes/03_AGC_ST_B03_CANONICAL_EXHAUSTION_20261120.md) and [frozen request](../research-progress/handoffs/AGC_ST_E04_REQUEST_R1_20261120.md) specify the finite labels, uniform value exhaustion and one stopped comparison. Bounds below are uniform over the fixed slab and sufficiently high target labels. The onset may depend on \(t_0\).

## The clock and a common finite head

Write \(\ell(x)=\log(x/(4\pi))\) and
\[
 G(x,t)=\frac{x}{4\pi}\ell(x)-\frac{x}{4\pi}
               +\frac{11}{8}+\frac{t}{16}\ell(x),\qquad
 G(q(v,t),t)=v .
\]
Use \(q_n(t)=q(n,t)\), and denote the actual root with that clock label by \(x_n(t)\). Fix a high label \(n\), and set
\[
 X=q_n(t_*),\quad L=\ell(X),\quad
 \epsilon=X^{-ct_0},\quad E=L\epsilon,\quad
 \nu=n+\tfrac12,\qquad J=\left\lfloor\frac{XL}{1000\pi}\right\rfloor .
\]
Choose the absolute source exponent \(c>0\) sufficiently small, in particular with \(ct_0<1\). The target has \(a=x_n(t)\), \(b=x_{n+1}(t)\), \(g=b-a\) and \(D=g^2/4\). Select the occurrences \(l_m=x_{n-m}(t)\), \(r_m=x_{n+1+m}(t)\) for \(1\le m\le J\) on the whole slab.

The clock derivatives in physical \(x\) are
\[
 G_x=\frac{\ell(x)}{4\pi}+\frac{t}{16x},\quad
 G_{xx}=\frac1{4\pi x}-\frac{t}{16x^2},\quad
 G_{xxx}=-\frac1{4\pi x^2}+\frac{t}{8x^3}.
\]
Throughout \(x\in[X/2,2X]\), \(L/(8\pi)\le G_x\le L/(2\pi)\) for large \(X\). The inverse satisfies
\[
 q_v=G_x^{-1}\asymp L^{-1},\qquad
 q_{vv}=-G_{xx}G_x^{-3}=O((XL^3)^{-1}),\qquad
 q_{vvv}=3G_{xx}^2G_x^{-5}-G_{xxx}G_x^{-4}
                      =O((X^2L^4)^{-1})                         \tag{1}
\]
there, with the right-hand sides evaluated at \((q(v,t),t)\). Also \(G_t=\ell(x)/16\), so on the high clock
\[
 q_t=-\frac{\pi}{4}
       \left(1+\frac{\pi t}{4q\,\ell(q)}\right)^{-1},\qquad
 |q_t|\le\pi/4.                                                 \tag{2}
\]
It follows that \(q(n,t)=X+O(1)\). The distance from \(q(n,t)\) to each endpoint of \([3X/4,5X/4]\) is at least \(X/5\) for large \(X\). Thus the index displacement available in \(G\) on each side is at least \(XL/(40\pi)\). The entire index interval \([n-J-1,n+J+2]\) therefore lies within the band of (1), with clocks in \([3X/4,5X/4]\).

Choose \(X\) large enough that \(X/3\) is above the source height onset on \(I\) and \(G(X/3,t)\) is above the source index onset, uniformly on \(I\). Both requirements are possible since the slab is bounded away from zero and \(G(X/3,t)\asymp XL\). Polymath (i) exhausts the high roots, and (ii) and its argument-principle proof give exactly one occurrence in each high label disk. On the working band the position errors are \(O(\epsilon)=o(L^{-1})\) and adjacent clock points are spaced by \(\asymp L^{-1}\). The disks can be chosen disjoint and symmetric about the real axis. Reality and simplicity follow, and the simple roots patch across time with the same label. All retained roots lie in \([X/2,2X]\), \(a,b=X+O(1)\), and \(n,n+1\) are consecutive. Every root with projection in \([X/2,2X]\) belongs to this high-label description, since its source clock is in \([X/3,3X]\) and above the buffered index onset. [Polymath v2, proof of (i), (ii)](https://arxiv.org/pdf/1904.12438v2#page=60) · [CM canonical comparisons, common labels](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/manuscript/sections/13_canonical_time.tex)

The two extreme retained clocks are at least \(2\pi J/L\) from their respective near target clock by the lower bound on \(q_v\). Since \(J\ge XL/(2000\pi)\) for large \(X\), their actual distances are at least \(X/2000\) after paying the endpoint errors. Every exterior occurrence inside the working band and omitted from the head is beyond one of these extremes by order. Every exterior occurrence outside the band has horizontal distance at least \(X/3\) from \([a,b]\) for sufficiently large \(X\). Hence every omitted occurrence has horizontal distance at least \(R_0=c_0X\), for instance \(c_0=1/4000\). This uses no reality or simplicity of the low divisor.

## The paired clock error

At a slice use \(q\) for \(q(\cdot,t)\), and let \(g_{\rm cl}=q(\nu+\tfrac12)-q(\nu-\tfrac12)\). Then \(g=g_{\rm cl}+O(\epsilon)\) and \(g_{\rm cl}\asymp L^{-1}\), giving \(g\asymp L^{-1}\). For \(\sigma=m+\tfrac12\), the clock distances are \(p_- =q(\nu-\tfrac12)-q(\nu-\sigma)\) and \(p_+=q(\nu+\sigma)-q(\nu+\tfrac12)\). Integrating the slope around \(\nu\) using (1) gives \(p_\pm=m q_v(\nu)+O(m^2/(XL^3))\). A symmetric expansion gives \(g_{\rm cl}=q_v(\nu)+O((X^2L^4)^{-1})\). The actual distances \(d_-=a-l_m,\ d_+=r_m-b\) satisfy \(d_\pm=p_\pm+O(\epsilon)\). With \(x_{m,\pm}=d_\pm/g\) and \(\delta_\pm=x_{m,\pm}-m\),
\[
 \delta_\pm=\frac{(p_\pm-mg_{\rm cl})+(d_\pm-p_\pm)
                             -m(g-g_{\rm cl})}{g},\qquad
 |\delta_\pm|\ll mE+\frac{m^2}{XL^2}.                           \tag{3}
\]
In particular \(|\delta_\pm|/m\ll E+J/(XL^2)=o(1)\), so the Taylor allowance can use \(x_{m,\pm}\ge m/2\) at large height.

For the signed sum keep the common denominator until the two distances have been added. The clock numerator is
\[
 p_++p_- -2mg_{\rm cl}
   = q(\nu+\sigma)-q(\nu-\sigma)
              -(2m+1)\big[q(\nu+\tfrac12)-q(\nu-\tfrac12)\big].
\]
In each symmetric difference the second derivative cancels. Taylor's formula with (1) gives \(q(\nu+h)-q(\nu-h)=2h q_v(\nu)+O(h^3/(X^2L^4))\). The two linear terms then cancel since \(2\sigma=2m+1\), leaving \(O(m^3/(X^2L^4))\). The actual numerator differs by \(O(\epsilon)-2m(g-g_{\rm cl})=O(m\epsilon)\). Thus
\[
 |\delta_++\delta_-|\ll mE+\frac{m^3}{X^2L^3}.                    \tag{4}
\]
The term \(mE\) includes the normalized actual-target denominator error. No derivative of an actual position error is used.

Set \(K_J^{\rm cl}=1-(J+1)^{-3}\). By E03 the exact difference \(K_J-K_J^{\rm cl}\) equals \(-\sum_{m\le J}\kappa_m(\delta_++\delta_-)\) plus a nonnegative remainder at most \(15\cdot2^6\sum_{m\le J}(\delta_+^2+\delta_-^2)m^{-6}\), where \(\kappa_m\le6m^{-5}\). The respective absolute allowances using (4) and (3) are
\[
 \begin{aligned}
 &\ll E\sum_{m\le J}m^{-4}+(X^2L^3)^{-1}\sum_{m\le J}m^{-2}
                  \ll E+(X^2L^3)^{-1},\\
 &\ll E^2\sum_{m\le J}m^{-4}+(X^2L^4)^{-1}\sum_{m\le J}m^{-2}
                  \ll E^2+(X^2L^4)^{-1}.
 \end{aligned}                                                  \tag{5}
\]
These give a two-sided head error. If the linear deterministic errors in (3) are paid separately, their allowance is \(O((XL^2)^{-1})\) from \(\sum m^{-3}\). The paired estimate pays \(O((X^2L^3)^{-1})\) for the surviving deterministic component including the quadratic allowance. On the frozen normalization \(E=LX^{-ct_0}\) dominates both allowances. An equally informed direct calculation pairs the same labeled sums before taking absolute values and obtains (4)–(5) with identical allowances.

## The full signed exterior and the two limits

For an exterior occurrence at horizontal distance \(d=\operatorname{dist}(\Re\rho,[a,b])>0\), use \(r=\rho-b\) on the right or \(r=a-\rho\) on the left. Then \(\Re r=d\), \(Q_\rho=r(r+g)\), and the coupled integral of E03 yields
\[
 \left|24D^2Q_\rho^{-2}+32D^3Q_\rho^{-3}\right|
    =|k(r/g)|\le \tfrac32 g^4 d^{-4},\qquad
 |Q_\rho^{-1}|\le d^{-2}.                                      \tag{6}
\]
For the first estimate \(|r+s|\ge d\) in the integral along \(0\le s\le g\). This is a bound on the whole coupled contribution. The sums retain all occurrences with their signs or complex values, and conjugation makes the complete sums and any horizontal truncation real.

For \(R\ge c_0X\), the two horizontal unit shells with \(R+j\le d<R+j+1\) contain \(O(L+\log(2+R+j)+1)\) occurrences, uniformly in \(t\). This uses the projected count of Polymath (iv) with reflection for negative projections. An interval meeting zero can be split at zero and covered by finitely many unit intervals. For \(p=2,4\), dyadic bands \(2^jR\le d<2^{j+1}R\) have \(O(2^jR)\) such unit intervals times their logarithmic allowance. Summing \(2^{(1-p)j}(L+\log(2+R)+1+j)\) gives
\[
 \sum_{d\ge R}d^{-p}
   \ll_p R^{1-p}[L+\log(2+R)+1],                                \tag{7}
\]
where the sum is over occurrences. In particular the \(K\) tail is \(O(g^4[L+\log(2+R)+1]/R^3)\) uniformly, and the \(M\) tail is \(O([L+\log(2+R)+1]/R)\). With \(R_0=c_0 X\) and \(g\asymp L^{-1}\), (6)–(7) bound the absolute contribution of the entire complement of the finite head by \(O((XL)^{-3})\) for \(K\) and \(O((XL)^{-1})\) for \(2DM\). [Polymath v2, proof of projected unit count](https://arxiv.org/pdf/1904.12438v2#page=61)

At fixed \(X\) these same value bounds tend to zero uniformly on \(I\) along arbitrary horizontal cutoff radii tending to infinity. More generally it suffices that the included set contains all occurrences up to radii whose infimum over \(I\) tends to infinity. These are exhaustions of actual common-time divisors. They require no independently evolved finite polynomials and no differentiation of tail terms or cutoff assignments. Subdividing a fixed exact finite partition reorganizes the same retained occurrences. Moving or replacing a wall preserves that statement on cleared overlaps with the same occurrence assignments. The exact complete moment time law used below follows from the separate fixed-order contour passage in [E02](03_AGC_ST_E02_PAIR_AND_FORCING_20261120.md).

After the fixed-target value exhaustion, take the high-label limit over the selected heads. The clock deficit \((J+1)^{-3}\) has order \((XL)^{-3}\). Combining it with (5) and the signed complement, and using \(E=o(1)\), gives
\[
 |K-1|\ll E+(X^2L^3)^{-1}+(XL)^{-3}                              \tag{8}
\]
on the whole fixed slab. The finite head consists entirely of high real roots. The estimate includes every remaining occurrence, including possible low nonreal or multiple roots. The limits are in the values of the complete forcing and interaction at the specified target.

## One backward comparison and its direct counterparts

In \(2DM\) the normalized single-clock contribution is \(f(x)=1/[2x(x+1)]\), with \(|f'(x)|\ll m^{-3}\) for \(x\asymp m\). By (3) the difference of the head from \(\sum_{m\le J}2 f(m)=J/(J+1)\) is
\[
 O\!\left(E\sum_{m\le J}m^{-2}+(XL^2)^{-1}\sum_{m\le J}m^{-1}\right)
         =O(E+(XL)^{-1}),
\]
using \(\log(2+J)=O(L)\). Including the complete \(M\) tail and the clock deficit yields
\[
 |V|=|1-2DM|\ll E+(XL)^{-1}.                                    \tag{9}
\]
The high labels give a cleared moving count-two contour, for instance a circle centered at the actual midpoint with radius \(g\) at large height. The nearest exterior real roots are at distance \((3/2+o(1))g\) from its center by (3) at \(m=1\), and all other exterior projections are farther or in the distant complement. The count and clearance follow from the imported high real simple labels, so the exact pair law with its complete exterior holds throughout this slab.

In backward time \(u=t_*-t\), put \(D(0)=D(t_*)\asymp L^{-2}\) in this time coordinate. Use (9) at the initial time for \(V(0)\) and (8) uniformly for \(K\ge1-\eta^2\) in the [AGC joint barrier](../../manuscript/sections/04_continuation.tex). The square-root deficiency and the initial bound allow a barrier parameter \(v\ll\sqrt E+(XL)^{-1}\). On \(0\le u\le t_*-t_0\) this gives
\[
 D(u)\ge D(0)-O\big(u[\sqrt E+(XL)^{-1}]\big).                   \tag{10}
\]
The relative loss tends to zero for fixed duration because \(L^2\sqrt E\to0\). Only a uniform value inequality and integration enter this comparison. Since (9) is actually available throughout the slab, integrating \(D_u=-2V\) directly gives the smaller two-sided allowance \(|D(u)-D(0)|\ll u[E+(XL)^{-1}]\) when using those whole-time \(V\) inputs.

The inherited data already give \(D(t)-D_{\rm cl}(t)=O(\epsilon/L)\) slice by slice in physical time, with \(D_{\rm cl}(t)=\tfrac14(q_{n+1}(t)-q_n(t))^2\), since \(g-g_{\rm cl}=O(\epsilon)\) and \(g+g_{\rm cl}=O(L^{-1})\). The \(q\)-derivative of the speed (2) is \(O((X^2L)^{-1})\) on the band, since \((q\ell(q))^{-1}\) has derivative \(-(\ell(q)+1)/(q^2\ell(q)^2)\). Hence \(|g_{\rm cl}'|\ll(X^2L^2)^{-1}\), \(|D_{\rm cl}'|\ll(X^2L^3)^{-1}\), and two evaluations with the same input give
\[
 |D(t)-D(s)|\ll \epsilon/L+|t-s|/(X^2L^3).                     \tag{11}
\]
This direct comparison is stronger at fixed positive time separation than (10), while its positional allowance does not vanish as \(|t-s|\to0\).

[Polymath v2 §9, immediately after (104)](https://arxiv.org/pdf/1904.12438v2#page=60) gives the stronger \(O(\epsilon/L)\) position error for high zeros at the nearest clock. The source contribution in (3)–(9) is \(L\) times the uniform absolute position error. With that passage it is \(O(\epsilon)\), and the direct positional terms in (11) and \(D-D_{\rm cl}\) improve to \(O(\epsilon/L^2)\) as well. The [CM spatial-jet comparison](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/manuscript/sections/13_canonical_time.tex) additionally uses a holomorphic spatial residual with Cauchy bounds and the physical equation. Its \(\epsilon_{\rm jet}=\epsilon+L/X\) gives \(|D_t|=O(\epsilon_{\rm jet})\) and an integrated allowance \(O(|t-s|\epsilon_{\rm jet})\). That time-derivative bound uses more than the real position values and projected counts used here.

## Scope

The forcing estimate and the backward comparison use the high region already covered by published localization on a fixed positive-time slab. The deterministic clock improvement is relative to separately bounded left and right displacements. The equally informed direct estimate ties, and the source position error dominates the deterministic improvement. This establishes neither new coverage nor a numerical onset, resource bound, or conclusion about time zero, RH or the Newman constant.

The geometric step uses a positive pre-event target gap and can apply to collision controls at their eligible slices. Canonical acquisition here uses all high labels of the unchanged normalized source. Euler-factor controls change the analytic exterior. Weighted squares and finite-source changes alter the coefficients, and finite-prime orbit controls fail full reflection. Reflected and positive-primitive controls lack the canonical square expansion. Fixed-event and finite-profile controls lack the full profile or eventual simplicity at the event. RH-conditional endpoint controls fail ordinary Dirichlet arithmetic, and the variable-kernel control fails the fixed physical heat equation. The geometric inequalities give no further separation conclusion from these differences. [Collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Results index](../../../../../result-summaries/README.md) · [Patterns index](../../../../../avoid/README.md) · [Known-coverage comparisons](../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
