# E01 r1 — complete outer estimate and one inward step

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Subagent dispatch recorded
**gpt-6.1-sol / ultra**. Independent per-turn backend and usage metadata
were unavailable.

**Status: proved in-note from the named inherited inputs; proof-author
assessment only.** This executes [E01 r1][packet] under the authorization in
[Note01][authority]. The [execution record][checks] verifies all 17 frozen
inputs by size and SHA-256 and gives the unchanged request's hash.

The [result index][results] and [avoid index][avoid] route through
[heat-flow cluster 11][r11], [control cluster 12][r12], [classification 01][a01],
[shared premises 02][a02] and [scoped exclusions 07][a07].
This is a canonical approximation milestone with one zero-exclusion step.

## 1. Fixed setup and provider gates

Keep the complete theta \(H_\lambda\), \(H_0(z)=\xi((1-iz)/2)/8\),
and \(\partial_\lambda H=-H_{zz}\). For \(X\in[U,2U]\), freeze
\(\lambda=\lambda_X=1/L_X\), where \(L_X=\log(X/(4\pi))\), across
\[
 D_X=\{|\Re z-X|<1,\ 7/8<\Im z<9/8\}.
\]
Write \(a_X=\sqrt{1-2/L_X}\), \(b_X=a_X+1/16\), \(p_X=X+ib_X\) and
\(K_X=\{X+iy:a_X-1/16\le y\le a_X\}\).
Use \(z=x+iy\), \(L_x=\log(x/(4\pi))\), \(c_x=\lambda L_x\) and
\(L(z)=\operatorname{Log}(z/(4\pi))\) on the right half-plane. The prescribed
analytic carrier and shifted argument are
\[
\begin{aligned}
 \mathcal A(\lambda,z)&=\frac{\pi^{1/4}}{16}z^{7/4}
 e^{-\pi z/8+\lambda(L(z)^2-\pi^2/4)/16},\\
 \Theta(\lambda,z)&=\frac z4(L(z)-1)+\frac{\pi\lambda L(z)}{16}+\frac{7\pi}8,
 &C_\pm&=\tfrac12\mathcal A e^{\pm i\Theta},\\
 s_\lambda(z)&=(1-iz)/2+\lambda L(z)/4-i\pi\lambda/8,
 &Z_\lambda(z)&=\zeta(s_\lambda(z)).
\end{aligned}
\]

[HDA Note04, CS2–6][hda], with [Note03, CB4][cal] and the
[parent transition section][parent], gives the following exact
decomposition on fixed \((r,b)=(1,9)\) charts. Recenter at the real
coordinate \(x\) of the evaluated point and freeze
\(N=N_x=\lfloor\sqrt{x/(4\pi)}\rfloor\) on that chart and throughout
the convolution. For \(0\le\lambda L_x\le8\) at sufficiently large \(x\),
\[
 \begin{aligned}
 H_\lambda&=\mathcal A\sum_{n\le N}w_n\cos(\Theta-\nu\log n)
            +e^{-\pi^2\lambda/64}\mathcal R_N+\mathcal E_N,
 &|\mathcal E_N|&\le h_9x^{-3/4}(|C_+|+|C_-|),\\
 w_n&=n^{-1/2}e^{\lambda[(\log n)^2-L(z)\log n]/4},
 &\nu&=z/2+\pi\lambda/8,\\
 \mathcal R_N&=(-1)^N\mathcal G(z)a(z)^{-1/2}\mathcal C(a(z)-N),
 &a(z)&=\sqrt{z/(4\pi)},\\
 \mathcal C(p)&=\frac{\cos(2\pi(p^2-p)-\pi/8)}{\cos(2\pi p)},
 &\mathcal G&=[M((1+iz)/2)M((1-iz)/2)]^{1/2},
 \end{aligned}                                                     \tag{1}
\]
where \(M(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)/16\), with \(\mathcal G\)
positive on the large real axis. The fixed constant \(h_9\) is the
\(j=0\) constant of CS6 at nonnegative time. It includes the complete
source/Gaussian exterior, the cutoff joins and the local errors.
The provider's status is “proved in-note from named classical inputs;
same-model internal assessment only.” [HDA Assessment03][hreview].

Use the following finite inherited onsets, with real chart center \(x\).

1. Reserve target \((1,9)\), enlargement \((2,10)\), positive local
   chart \((2,10+2V_9)\), and the signed provider's negative local chart
   \((V_9+3,10)\). Each pair gives horizontal radius and transverse
   bound. Take \(P_9=21\) and fix \(c_9\ge1\) from CS16–17 for the base
   strip and the full-ray bounds, then choose
   \(V_9\ge\max(16,17,16c_9,8\sqrt{P_9+6})\) by CS18. Constants on the
   enlarged charts may depend on this fixed window.
2. On each reserved \((r',b')\), put \(W=(\log x)^2\),
   \(D=\max(4,b'+1)\). Apply the real corrected Riemann–Siegel onset on
   \([x/2,3x/2]\), sectorial gamma calibration and Euler summation at
   the fixed bounds, and all CS8–15 inequalities
   \[
    x\ge16\pi,\quad r'\le W\le x/2,\quad W+D\le\sqrt x,\quad
    a(x+W)-a(x-W)<1/2,\quad W^3\le x,\quad
    (W+1)/\sqrt x\le1,\quad W^2\ge(5/4)\log x+D^2 .
   \]
   The growing real edge crosses at most one threshold, where CS9's
   added-mode/correction difference applies. CS11 pays the upper edge
   with the ordinary Dirichlet tail; CS14 pays both vertical edges.
3. For CS16–25 require \(L_x\ge16\),
   \(x\ge\max(2(V_9+3),12)\) and \(x^{1/3}\ge V_9\). Require the CS16
   source-bound onset at real parts \(u\ge x/3\), and the fixed-chart
   gamma calibration/Taylor onsets in CB4 and CS22–25. For example, for
   a fixed local quadratic log-gamma bound \(C_{\rm loc}v^2/x\),
   \(2C_{\rm loc}(1+V_9)^2\le x\) gives the needed smallness uniformly
   on the windows. Also impose \(\log N\le\inf\Re L(z)\) on the fixed
   charts for CS24. This follows eventually from
   \(\log N\le L_x/2\) and \(\Re z\ge x/2\).
4. On the positive near exterior \(V_9<|v|\le x^{1/3}\), impose
   \(c_9v^2/x\le v^2/(8\lambda)\), for example by \(x\ge4c_9\) with
   \(\lambda\le1/2\). The terms \(|v|L_x/2+c_9|v|\) are bounded by
   \((1/4+1/32)v^2/\lambda\), by CS18 and \(\lambda L_x\le8\).
   Hence the combined Gaussian and CS17 exponent is at most
   \(-v^2/(4\lambda)\), giving the inherited normalized
   \(O(x^{P_9-V_9^2/32})\) payment. For the distant ray write
   \(w=|v|\ge x^{1/3}\ge1\). The full-ray logarithmic bound relative to
   \(\mathcal G(x)\) is at most
   \(P_9\log(2w^3)+c_9(w+1)+(w/2)\log(2w^3)\). Increase \(x\) until
   this is at most \(w^2\) for every \(w\ge x^{1/3}\), possible since
   the quotient by \(w^2\) tends to zero. Since \(\lambda\le1/2\),
   this gives the \(w^2/(2\lambda)\) domination of CS21 and a
   superpolynomial Gaussian tail. The artificial tails from the
   linearized completions use CS18–25. The positive real Gaussian
   center shifts are at most \(2+o(1)\) uniformly over \(n\le N\).
   Enforce a bound \(3\). The bounded complex Gaussian loss and
   \(\exp(-(V_9-3)^2/(2\lambda))\) tail factor pay even the
   \(x^{1/4}\) population in CS24. The true correction stays within
   the fixed local window.
5. CS19–20 also reserves the negative window with the same \(V_9\),
   the near exterior \(O(x^{P_9-5/4-V_9^2/64})\) and the distant
   Gaussian gate. The latter holds once
   \(\pi x/8+T L_x^2/16-x^2/(16T)\le-x^2/16\) for
   \(0<T\le\min(1/2,8/L_x)\). The signed linear tails are already
   covered by CS18. This is part of the inherited signed setup;
   (1) and its consumers use the nonnegative specialization and \(j=0\).

Each gate holds eventually. Fix a finite \(x_0\) above all these
onsets. In the outer rectangle use \(X\ge2\), \(X-1\ge x_0\),
\(L_X\ge64\), \(2/(XL_X)\le1/8\). The mean-value bound
\(|L_x-L_X|\le2/X\) yields \(7/8\le c_x\le9/8\) and
\(0<\lambda\le1/2\). Also \(X/2\le x\le3X/2\) and
\(N\ge\tfrac12\sqrt{x/(4\pi)}\) using \(x\ge16\pi\).
Every boundary point is covered, including a point whose real
coordinate is a cutoff threshold. The estimates on different charts
refer to the same exact field and time. No differentiation of the
cutoff or time recentering enters the comparison.

## 2. Carrier and complete comparison

On \(\overline D_X\), the elementary \(C_-\) is analytic and nonzero,
and
\[
 \Re s_\lambda(z)\ge(1+y)/2+c_x/4\ge37/32>9/8.
\]
For \(\sigma=\Re s\ge9/8\) the ordinary absolutely convergent Euler
product gives
\[
 |1/\zeta(s)|\le\prod_p(1+p^{-\sigma})\le\zeta(\sigma)
 \le1+1/(\sigma-1)\le9.
\]
Thus \(C_-Z_\lambda\) is analytic and nonzero on a neighborhood of
the closed rectangle independently of \(H_\lambda\).
[DLMF ordinary series and Euler product][euler].

Since \(\Theta_z=L(z)/4+\pi\lambda/(16z)\) and \(\Theta(\lambda,x)\)
is real, integration from \(x\) to \(x+iy\) gives
\(\Im\Theta\ge yL_x/4\). Indeed \(\Re L(x+iv)\ge L_x\) and
\(\Re(1/(x+iv))>0\). Write \(P=(4\pi)^{9/16}\). Then
\[
 |C_+/C_-|\le P x^{-y/2},\qquad |e^{i\Theta}|\le\sqrt P x^{-y/4}.
                                                                   \tag{2}
\]
As \(|\Im L(z)|<\pi/2\), we have
\(\Re(L(z)^2-\pi^2/4)\ge L_x^2-\pi^2/2>0\). In particular,
\(|\mathcal A(0,z)|/|\mathcal A(\lambda,z)|\le1\).

Use the parent's fixed \(g_9,f_9\) with
\[
 |\mathcal G|\le g_9|\mathcal A(0,z)|/2,\qquad
 |a(z)^{-1/2}\mathcal C(a(z)-N)|\le f_9 x^{-1/4}.
\]
The first follows by taking the geometric mean of the two zero-time
gamma calibrations CB4, whose phases in the two arms cancel, with
uniform relative \(O_9(x^{-1})\) errors. For the second,
\(|a(z)-a(x)|\le(9/8)/(2\sqrt{4\pi x})<1\) on the evaluation
line, and \(a(x)-N\in[0,1)\). At every denominator zero
\(p=(2k+1)/4\), \(k\in\mathbb Z\), the numerator's angle is
\(\pi(k^2-k-1)/2\), an odd multiple of \(\pi/2\).
The denominator has simple zeros, so the quotient is bounded on
\(\operatorname{dist}(p,[0,1])\le1\) after removal. Moreover
\(|a(z)^{-1/2}|\le(4\pi)^{1/4}x^{-1/4}\).
These bounds include every fractional cutoff position.

Expand the cosine in (1) and divide by \(C_-\). For
\(V_\lambda=H_\lambda/C_-\) this gives
\[
 \begin{aligned}
 V_\lambda&=D_N+R_N+Q_N+E_N,&
 D_N&=\sum_{n\le N}n^{-s_\lambda(z)}e^{\lambda(\log n)^2/4},\\
 R_N&=e^{2i\Theta}\sum_{n\le N}w_ne^{-i\nu\log n},&
 Q_N&=e^{-\pi^2\lambda/64}\mathcal R_N/C_-,
 \quad E_N=\mathcal E_N/C_- .
 \end{aligned}                                                     \tag{3}
\]
The \(C_-\) arm's \(e^{i\nu\log n}\) factor yields the displayed
\(s_\lambda\) exactly. For \(n\le N\),
\(\log n\le L_x/2\le\Re L(z)/2\), so
\[
 |n^{-s_\lambda(z)}e^{\lambda(\log n)^2/4}|
 \le n^{-(1+y)/2-c_x/8}\le n^{-67/64}\le n^{-33/32}.
\]
Using \(e^v-1\le ve^v\) for \(v\ge0\), and summing over the finite
arm, pays the heat-weight removal by \(A/L_X\), where
\(A=\tfrac14\sum_{n\ge2}n^{-33/32}(\log n)^2<\infty\).
The ordinary zeta tail costs
\(8N^{-1/8}\le C_Z x^{-1/16}\) with \(C_Z=8(2\sqrt{4\pi})^{1/8}\).
Only the ordinary Dirichlet series is extended to infinity.

For the complete reflected sum,
\[
 |w_ne^{-i\nu\log n}|\le n^\alpha,\qquad
 \alpha=(y-1)/2-c_x/8\in[-13/64,-3/64].
\]
Heat suppression applies to every \(n\le N\). The sum is at most
\(\int_0^N u^\alpha du\le(64/51)N^{1+\alpha}\). Since \(N\le\sqrt{x}\),
\[
 |R_N|\le (64/51)P x^{(1-y)/4-c_x/16}
         \le (64/51)P x^{-3/128}.                                  \tag{4}
\]
The correction and remaining error are separate:
\[
 |Q_N|\le g_9f_9\sqrt P\,x^{-(1+y)/4}\le g_9f_9\sqrt P\,x^{-15/32},
 \qquad |E_N|\le h_9x^{-3/4}(1+Px^{-y/2}).                         \tag{5}
\]
For \(Q_N\) use (2), the amplitude ratio, and \(e^{-\pi^2\lambda/64}\le1\).
For \(E_N\) use the full two-carrier envelope. All power costs are
bounded by the same prefactors times \(x^{-3/128}\) since \(x\ge1\).
Thus
\[
 \sup_{\overline D_X}|V_\lambda-Z_\lambda|
 \le A/L_X+B(X-1)^{-3/128},\qquad
 B=C_Z+(64/51)P+g_9f_9\sqrt P+h_9(1+P).
\]
The additional gates \(L_X\ge288A,\ X-1\ge(288B)^{128/3}\) make nine
times this bound at most \(1/16\). Together with §1 they define a
finite uniform \(U_*\), with no numerical onset required.
For \(F_\lambda=V_\lambda/Z_\lambda\) we obtain
\[
                  \sup_{\overline D_X}|F_\lambda-1|\le1/16.         \tag{6}
\]

## 3. Width and complete Green comparison

At \(L_X\ge64\), \(a_X\ge\sqrt{31/32}>31/32\) and \(a_X<1\).
Every closed disk of radius \(1/32\) centered on the length-\(1/8\)
segment from \(p_X\) to \(X+i(a_X-1/16)\) lies inside \(D_X\).
The lowest disk height is \(a_X-3/32>7/8\) and the highest is less
than \(35/32<9/8\). Cauchy on \(F_\lambda-1\) gives
\(M=(1/16)/(1/32)=2\). The anchor \(|F_\lambda(p_X)|\ge15/16\)
permits \(m=1/2\), and for \(0\le q\le h=m/(2M)=1/8\)
\[
 |F_\lambda(p_X-iq)|\ge m-Mq\ge m/2=1/4.
\]
This reaches the lower target with observation buffer
\(\eta=b_X-a_X=1/16<h\). De Bruijn contraction, Polymath Theorem 3.2
at \(t_0=0,y_0=1\), gives the initial enclosure \(y\le a_X\)
at time \(\lambda_X\). The time-zero hypothesis follows from
the completed \(\xi\) zero strip. Excluding the closed \(K_X\) and
using conjugation of the complete real-source field proves
\[
 H_{\lambda_X}(X+iy)=0\quad\Longrightarrow\quad
 |y|<\sqrt{1-2/L_X}-1/16.
\]
The strict endpoint follows from the closed exclusion and implies
the frozen weak bound. Equation (6) also gives direct nonvanishing
on the entire rectangle. [Cauchy's formula][cauchy], [Polymath §3][enclosure].

The full Green allowance is the harmonic-measure average of
\(\log|H_\lambda|\) on \(\partial D_X\) minus its value at \(p_X\).
Subtracting the harmonic \(\log|C_-Z_\lambda|\) leaves the
defect unchanged. By (6), the log modulus of \(F_\lambda\) is
at most \(\log(17/16)\) on all four edges and at least
\(\log(15/16)\) at the anchor. Harmonic measure has mass one,
so \(J_{\lambda,D_X}(p_X)\le\log(17/15)\). The boundary floor also
follows from (6).

For \(X+iy\in K_X\) use the disk of radius \(R=1/8\) around \(X+i\)
inside \(D_X\). Put \(u=b_X-1,\ v=y-1,\ d=u-v\).
Then \(u/R\in[1/4,1/2]\), \(d\in[R/2,R]\), and its positive
Green function with logarithmic pole is
\[
 G_{\rm disk}(p_X,X+iy)=\log\frac{R^2-uv}{Rd}
 =\log\bigl[u/R+(1-(u/R)^2)R/d\bigr]\ge\log(19/16).
\]
The last bound minimizes \(q+1-q^2\) on \([1/4,1/2]\).
Domain monotonicity follows from the maximum principle after
cancelling the pole. In the Green representation for the log
modulus each zero contributes its positive multiplicity times the
Green function. This follows by subtracting the finite interior
logarithmic poles and solving the bounded Dirichlet problem for the
resulting harmonic function. Thus the strict margin is at least
\(\log(285/272)>0\), excluding \(K_X\). In fact the exact Green
defect vanishes by the full floor in (6). There is no spatial
tail, quadrature or shape approximation. The source tails remain
within the paid provider error.

## 4. Control screen, source use and scope

| Control class | Premise that fails for this application |
| --- | --- |
| Euler-factor and translated controls | Unmodified ordinary coefficients in the dominant arm and ordinary tail. |
| Weighted-square, finite theta-tail and finite zero-tail controls | The complete canonical coefficient sequence and completed reflection identity needed together for the corrected expansion and CS11. |
| Reflected super-Gaussian, smooth and positive-primitive controls | Complete integer-square theta expansion with unit coefficients. Primitive endpoints or evenness do not supply the ordinary tail. |
| Cluster11 positive counter-kernels and exact-threshold models | The canonical completed \(\xi\) input and both arithmetic arms. |
| Finite-prime orbit controls | Full reflection and full coefficient agreement outside the selected primes and prefix. |
| Atomic fixed-event, finite-profile and compact continuous controls | Complete canonical source, including full growth profile and coefficients beyond the observations. |
| RH-conditional normalized-endpoint controls | Ordinary coefficient identity in (3). Their RH hypothesis remains conditional. |
| Fixed-amplitude variable-readout controls | Actual cosine/Newman readout in (1), even with the same amplitude and a finite readout prefix. |
| Inherited polynomial heat diagnostic | Canonical theta provider; the diagnostic concerns localization of global strip contraction. |

A control zero in a tested box with a nonzero comparison carrier
gives \(|F-1|=1\) there. A zero in the Green target contributes at
least the required Green margin and defeats the strict test. A
control may pass on a disjoint collision-free box. Reflection
rigidity retains its full conjunction of hypotheses.

On 13 November rechecked [Polymath v2][poly], Theorem 3.2 and its
application at \(t_0=0\), equation (5) for Theorem 1.3's printed
domain and §6.2 for the zero-time contour cross-check. The printed
explicit constants of Theorem 1.3 stop at \(y=1\); the required
larger chart is supplied by HDA CS6. Also checked DLMF 1.2.8
[§25.2][euler] for the ordinary Dirichlet series, Euler summation and
Euler product, [§25.10(ii)][rs] for the corrected real expansion,
[§5.11][gamma] for sectorial Stirling and [§1.9(iii)][cauchy] for Cauchy
differentiation. These sources are already catalogued in the
[branch source-use record][refs] or the HDA provider. Passage-level
checking and byte verification do not constitute an independent
audit of that provider.

The result covers one time curve at sufficiently large centers and one
inward step. Compact-height coverage, a narrower global strip at a
common time, time propagation and iteration remain outside the
proved result. At limiting \(c_x=1\) the coarse absolute payments in
(3)–(4) require \(y>3/4\), from their summability and reflected-decay
exponents. This limit concerns these payments; sharper estimates can
be considered separately. See the [assessment][review] and
[dated return][return].

[packet]: ../research-progress/handoffs/GNP-BB-E01-r1.md
[authority]: 01_GNP_BB_CONTINUATION_AND_PROMPT_20261113.md
[checks]: ../numerics/03_GNP_BB_E01_INPUTS_AND_CHECKS_20261113.json
[review]: ../reviews/02_GNP_BB_E01_SELF_ASSESSMENT_20261113.md
[return]: ../research-progress/handoffs/GNP-BB-E01-r1-return.md
[parent]: ../../manuscript/sections/10a_transition_green.tex
[hda]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[cal]: ../../../01_heat_density_asymptotics/ansatz/notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[hreview]: ../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[refs]: ../references/01_GNP_BB_B01_SOURCE_USE_20261113.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[euler]: https://dlmf.nist.gov/25.2
[cauchy]: https://dlmf.nist.gov/1.9.E31
[rs]: https://dlmf.nist.gov/25.10#ii
[gamma]: https://dlmf.nist.gov/5.11
[poly]: https://arxiv.org/html/1904.12438v2
[enclosure]: https://arxiv.org/html/1904.12438v2#S3

