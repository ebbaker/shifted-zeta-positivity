# E05 r1 — common-time width-\(4/7\) tail

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Subagent dispatch recorded
**gpt-6.1-sol / ultra**. Independent backend and token-use metadata
were unavailable.

**Status: proved in-note from the named inherited inputs, submitted
for additional-agent assessment.** This executes [E05 r1][packet]
following [Decision03][decision] and [Note11][design]. The [result
index][results] and [avoid index][avoid] route through [heat-flow
cluster11][r11], [collision controls12][r12], [classification01][a01],
[shared premises02][a02] and [scoped exclusions07][a07].
This is a fixed-width quantitative tail theorem.

There exists a finite \(t_0>0\) such that
\[
 0<t\le t_0,\quad |x|\ge4\pi\exp(1/t),\quad H_t(x+iy)=0
 \quad\Longrightarrow\quad |y|<4/7.                             \tag{1}
\]
At each \(t\) this concerns all points in the spatial tail at that
same time. The new comparison covers a finite transition window
in \(t\log(x/(4\pi))\). The published all-real far tail is then
used to finish the union.

## 1. Primary input and order of constants

Polymath v2 equations (1), (3) and (4) use the same source \(\Phi\),
\(\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du\), and
\(H_0(z)=\xi((1+iz)/2)/8=\xi((1-iz)/2)/8\). The time and the
\(z\) scale therefore agree. Theorem 1.5(i) gives a finite absolute
\(C_P>0\) such that for every \(0<t\le1/2\), all zeros with
\(x\ge\exp(C_P/t)\) have \(y=0\). Theorem 3.2, with initial time
zero and initial upper width \(1\), gives the upper bound
\(y\le\sqrt{1-2t}\) for \(0<t\le1/2\). The initial bound follows
from the \(\xi\) zero strip. These primary passages were rechecked on
13 November. [Polymath v2 Theorem 1.5(i)][outer], [Theorem 3.2][poly].

Fix \(C\ge\max(8,C_P)+1\) and \(D=C+1\) before any new provider
constants. The finite-arm comparison will use \(1\le tL_x\le C\);
the positive provider below has range \(0\le tL_x\le D,\ t\le1/2\).
Here and throughout \(L_x=\log(x/(4\pi))\). Use the exact elementary
\(\mathcal A,\Theta,C_\pm,s_t\) of [Note06][e01] and the [parent
formulas][parent]. Write \(E_o=|C_+|+|C_-|\). All implied constants
below may depend on \(D\) and fixed widths, never on \(x,t\), an
integer cutoff position or an individual mode.

## 2. Positive-time provider on the extended window

We prove the value bound for \(|\Re z-x|\le1,\ |\Im z|\le9\) on a
chart centered at \(x\), with \(N=\lfloor\sqrt{x/(4\pi)}\rfloor\)
fixed. The approximant \(F_N^{\rm HDA}\) is the same elementary
two-arm cosine plus \(e^{-\pi^2t/64}\mathcal R_N(z)\) as in
[HDA CS4][hda] and [Note06 (1)][e01]. We will establish
\[
       |H_t(z)-F_N^{\rm HDA}(t,z)|
          \le h_D E_o(t,z)x^{-3/4}.                              \tag{2}
\]
The inherited initial input is CS3 on fixed charts, together
with CB4 calibration and CS16–17's base-strip and full-ray
bounds. HDA's existing proof status remains “proved in-note
from named classical inputs; same-model internal assessment only.”
The wider positive-time value range in (2) is proved here.
[HDA Assessment03][hreview].

**Windows and comparability.** Use the reserve target \((2,10)\)
above the \((1,9)\) target, with radius and transverse bound listed
in that order. Take \(P_b=b+12=21\) and fix \(c_b\ge1\) from CS17
on this fixed base with \(b=9\), including its full-ray majorant.
These constants concern the complete zero-time source on the base
and its shifted rays, and are chosen before any new window.
Set \(\mu_*=D/4+1\) and choose a fixed
\[
 V\ge\max\{16,b+8,D,16c_b,2\mu_*,\sqrt{8D(P_b+2)}\}.
                                                                    \tag{3}
\]
Reserve the enlarged initial chart \((2,10+2V)\) for this window.
For all three fixed charts retain the CS3 real corrected
Riemann–Siegel and sectorial gamma onsets and every zero-time
CS8–15 inequality listed in Note06 §1, with that chart's own
radius and strip. This retains all vertical-edge, real-edge
cutoff and ordinary upper-tail payments. After \(V\) is chosen,
fix the local gamma and Taylor constants on the enlarged chart.
Require \(x\ge16\pi,\ L_x\ge16,\ x^{1/3}\ge V\), the fixed-chart
positive/comparable real-part gates, and the local smallness
gates below. In particular \(\Re z\ge x/2\) on these charts
eventually, \(\log N\le L_x/2\le\Re L(z)\), and
\(L(z)=L_x+O_b(x^{-1})\) on the reserve target.

Let \(w=(1+iz)/2\) and \(w'=1-w\), \(M\) as in CS1, and
\(E_{\Gamma,0}=|M(w)|+|M(w')|\). Write
\(b_\pm=L(z)/2\pm i\pi/4\) and \(\alpha=M'/M\). By CB4 and its
conjugate, the zero-time gamma arms agree with \(C_\pm(0,z)\)
to relative \(O_b(x^{-1})\), and their logarithmic slopes
agree with the respective \(b_\pm\) to \(O_b(x^{-1})\).
The exact elementary heat factors at \(n=1\) are
\[
 C_\pm(t,z)=C_\pm(0,z)e^{t b_\pm^2/4}.
\]
Since \(\Re(b_\pm^2/4)=L_x^2/16+O_b(1+L_x/x)\) and \(t\le1/2\),
\[
 E_o(t,z)\asymp E_{\Gamma,0}(z)e^{tL_x^2/16}.                       \tag{4}
\]
Also \(E_o(t,z)\gg\mathcal G(x)\) on the reserve target. Indeed
\(E_{\Gamma,0}\ge2|\mathcal G(z)|\) by the arithmetic-geometric
mean, and \(\mathcal G(z)\asymp\mathcal G(x)\) in modulus on the
fixed base chart by CB4, or by its bounded log derivative.

**Exact source exteriors.** For \(t>0\) the full theta source
and Gaussian completion give
\[
 H_t(z)=\int_\mathbb R H_0(z-2iv)\,d\gamma_t(v),\qquad
 d\gamma_t(v)=(\pi t)^{-1/2}e^{-v^2/t}\,dv.                       \tag{5}
\]
Interchange with the cosine integral is justified by absolute
integration against the decaying source, since the Gaussian
moment of \(e^{2|v|u}\) is at most \(2e^{tu^2}\).
On \(V<|v|\le x^{1/3}\), CS17 bounds the normalized integrand
by \(O(x^{P_b})\) times the exponential with exponent
\[
 -v^2/t+|v|L_x/2+c_b|v|+c_b v^2/x.
\]
The three positive terms are at most
\((1/2+1/32+1/8)v^2/t\), using \(V\ge D\), \(V\ge16c_b\),
\(t\le1/2\) and the eventual gate \(x\ge4c_b\).
The exponent is at most \(-v^2/(4t)\). Splitting that
Gaussian in two gives a total normalized payment
\(O(x^{P_b}\exp(-V^2/(8t)))=O_D(x^{-2})\) by (3) and
\(tL_x\le D\).

For \(|v|=q\ge x^{1/3}\ge1\), use the full-ray bound following
CS17. Its logarithmic majorant relative to \(\mathcal G(x)\)
is at most
\[
 P_b\log(2q^3)+c_b(q+1)+(q/2)\log(2q^3).
\]
Require \(x\) large enough that this is at most \(q^2\) for all
\(q\ge x^{1/3}\), possible because the quotient by \(q^2\)
tends to zero. Then it is at most \(q^2/(2t)\) for \(t\le1/2\),
so the normalized far tail is \(O(\exp(-x^{2/3}/(4t)))\).
Enlarge the onset so it is at most \(O(x^{-3/4})\) uniformly
for \(t\le1/2\). Both estimates retain the full source and its
height-relative bound.

**Local initial remainder.** Insert CS3 at the fixed \(N\)
into (5) on \(|v|\le V\), with \(w\) shifted to \(w+v\) and
\(w'\) shifted to \(w'-v\). Sectorial calibration gives
\[
 |M(w_\pm\pm v)|\le C_{b,V}|M(w_\pm)|\,e^{\pm v L_x/2},
 \qquad (w_+,w_-)=(w,w').
\]
This follows by integrating \(\Re\alpha=L_x/2+O_{b,V}(1/x)\)
along the fixed real shift. The Gaussian moments of the
two positive weights are both \(e^{tL_x^2/16}\).
Thus the local CS3 remainder averages to
\(O(E_{\Gamma,0}x^{-3/4}e^{tL_x^2/16})=O(E_o x^{-3/4})\).

**All modes and their linear completions.** For
\(m_{\pm,n}=M(w_\pm)n^{-w_\pm}\), the exact initial mode on
the local shift is
\[
 m_{\pm,n}(z-2iv)=m_{\pm,n}(z)
       e^{\pm v(\alpha(w_\pm)-\log n)}
       \bigl(1+O_{b,V}(v^2/x)\bigr).                              \tag{6}
\]
The uniform log-gamma quadratic Taylor bound is \(C_{b,V}v^2/x\),
independent of \(n\) since \(-w_\pm\log n\) is linear. Require
\(C_{b,V}V^2/x\le1/2\), and sectorial calibration increasing \(x\)
as necessary. For \(d_n=\alpha(w_\pm)-\log n\) one has
\(|\Im d_n|\ll_b1\) and \(|\Re d_n|\le L_x/2+O_b(x^{-1})\),
using \(0\le\log n\le L_x/2\). Thus the real center
\(\mu=\pm t\Re d_n/2\) of the tilted Gaussian obeys
\(|\mu|\le\mu_*\) eventually, uniformly for every mode.
Completing the full linear Gaussian gives
\(\widetilde P_{\pm,n}=m_{\pm,n}e^{t d_n^2/4}\).
The normalized absolute Gaussian after tilt is a real translated
Gaussian times \(e^{t(\Im d_n)^2/4}\ll_b1\).
Its second moment is at most a fixed multiple of
\(t/2+\mu^2=O_D(1)\). Hence the local Taylor error in (6)
is \(O_D(|\widetilde P_{\pm,n}|/x)\). The exterior of the
linear completion has size
\[
 O_b(|\widetilde P_{\pm,n}|\exp(-(V-\mu_*)^2/(2t))).
\]
This follows by splitting the translated Gaussian exponent into
halves and integrating one half. It is an artificial tail of
the linear term only.

Convert to the elementary mode
\[
 P_{\pm,n}=C_\pm(0,z)n^{-1/2}e^{\mp iz\log n/2}
                 e^{t(b_\pm-\log n)^2/4}.
\]
CB4 gives a relative \(O_D(x^{-1})\) error, since the exponential
log difference is bounded by
\(O(t(1+L_x)/x)=O_D(x^{-1})\), in addition to the zero-time
calibration. Require each of these fixed bounds small, e.g.
\(2C_{D,b,V}(1+V)^2\le x\) after choosing a constant dominating
the Taylor and relative exponent errors. All \(N\) modes are
retained. In absolute value the heat factor after dividing by
the corresponding \(C_\pm(t,z)\) is
\(\exp(t[(\log n)^2-\Re L(z)\log n]/4)\le1\).
For \(y=\Im z\ge0\), the \(C_-\) arm has
\(\sum_{n\le N}n^{-(1+y)/2}\ll x^{1/4}\). The other has
\(|C_+/C_-|\ll_b x^{-y/2}\) by the phase derivative in
Note06, and
\(\sum_{n\le N}n^{(y-1)/2}\ll_b N^{(y+1)/2}\).
This also fits the \(O(E_o x^{1/4})\) envelope because
\(x^{-y/2}N^{(y+1)/2}\ll x^{(1-y)/4}\).
Conjugation swaps the estimates when \(y<0\). Therefore
\(\sum_{\pm,n\le N}|\widetilde P_{\pm,n}|\ll_D E_o x^{1/4}\)
as well. Summing Taylor and calibration errors gives
\(O_D(E_o x^{-3/4})\). Since \(V-\mu_*\ge V/2\),
(3) and \(tL_x\le D\) pay the full artificial tail population
by \(O_D(E_o x^{1/4-P_b-2})\).

**Retained correction.** The exact fixed-\(N\) correction is
\(\mathcal R_N=(-1)^N\mathcal G f_N\), with
\(f_N=a^{-1/2}\mathcal C(a-N)\) as in Note06. CS25 and CB4 give
\(\mathcal G'/\mathcal G=-\pi/8+O_{b,V}(x^{-1})\),
\(f_N=O_{b,V}(x^{-1/4})\) and
\(f_N'=O_{b,V}(x^{-3/4})\) on the enlarged fixed chart.
These are uniform in \(a(x)-N\in[0,1)\) by the removable
quotient and \(a(z)-a(x)=O_{b,V}(x^{-1/2})\).
Integrate the derivative bounds on the vertical shift to get
\[
 \mathcal R_N(z-2iv)
 =e^{i\pi v/4}\mathcal R_N(z)
       +O_{b,V}(|\mathcal G(z)| x^{-3/4}|v|e^{C_{b,V}|v|})
 \qquad(|v|\le V).
\]
The error averages to \(O_{b,V}(|\mathcal G(z)|x^{-3/4})\)
since \(t\le1/2\). The completed linear phase averages
to \(e^{-\pi^2t/64}\mathcal R_N(z)\). Its artificial tail
costs \(O(|\mathcal G(z)|x^{-1/4}e^{-V^2/(2t)})\),
within \(O_D(E_o x^{-3/4})\) by (3)–(4).
The true correction is only used on the fixed local window.
This retains it without division by a possibly vanishing
correction factor.

Combining the exterior, remainder, mode and correction bounds
gives (2), since the sum of the elementary modes is exactly the
cosine arm expression in CS4. At \(t=0\) use CS3 directly and
the mode calibration without Gaussian integration.
All enlarged-chart constants and their Taylor, gamma, cutoff and
source onsets are fixed after \(V\) and before the final height
gate. The stated inequalities hold eventually once those
constants have been fixed. No negative-time or derivative
extension is used.

## 3. Finite-window comparison at common fixed time

Fix \(t>0\) and evaluate at \(z=x+iy\) with \(4/7\le y\le9/8\)
and \(1\le c=tL_x\le C\). Apply (2) at real center \(x\)
throughout this range. The same time is used for every point;
there is no time recentering. Put \(Y=e^{L_x}\),
\(\ell=\Re L(z)\), \(\beta=\Im L(z)\). Use the decomposition
of [Note09 (1)][e02] at time \(t\), with the exact phases
\(\tau_D=x/2+\pi t/8-t\beta/4\),
\(\tau_R=x/2+\pi t/8+t\beta/4\), both in \([x/2,x]\)
eventually. The real drift \(\ell-L_x\ge0\) helps both amplitudes.
Also \(t\ell\le D+1\) eventually, by \(\ell-L_x=O(x^{-2})\).
The exact shifted argument has
\[
 \Re s_t=(1+y)/2+t\ell/4\ge29/28>33/32 .
\]
The ordinary Dirichlet series and Euler product therefore give
nonzero analytic \(Z_t=\zeta(s_t)\) with \(|1/Z_t|\le33\).
The carrier \(C_-\) is analytic and nonzero independently.
[DLMF §25.2][zeta].

Use the exact \(N=\lfloor Y^{1/2}\rfloor\) and
\(K=\lfloor Y^{1/8}\rfloor\), with \(Y^{1/8}\ge2\) in the onset.
On \(n\le K\) the dominant weighted term is at most
\(n^{-((1+y)/2+7c/32)}\le n^{-225/224}\).
Thus the finite head heat removal is at most \(A_Dt\), where
\(A_D=\tfrac14\sum_{n\ge2}n^{-225/224}(\log n)^2<\infty\).
The ordinary tail is at most \(32K^{-1/32}\ll x^{-1/256}\).
The weighted sum ends at the finite cutoff \(N\).

For the tail \(K<n\le N\) use the six intervals and fixed pairs
in [Note10 §1][e03]. On each scale interval \([a,b]\) take
clipped dyads starting at \(Y^a\) with borders open on the left
and closed on the right. This pays every integer of the tail
exactly once, including integers at joins; there are \(O(1+L_x)\)
blocks. Note09's arbitrary subinterval Montgomery–Vaughan
bound is \(\ll x^{k_j}M^{l_j-k_j}+M/x\), with \(M\) the left
dyad endpoint, the exact \(\tau_D,\tau_R\) as above, and
the reference phase \(T\log u/(2\pi)\).
Use Abel on each clipped dyad; the amplitude log derivative
times \(u\) is bounded by a constant depending on \(D\) since
\(t\ell=O_D(1)\), \(t\log u\le C/2\) and \(y\) is bounded.
Integrating that derivative gives the starting weight times
a fixed variation factor as in Note09. The constants remain
independent of the integer positions and \(t\).
[Montgomery–Vaughan, Definitions 16.1–16.2 and Processes A, B][mv].

For \(v=\log M/L_x\), the dominant primary power of \(Y\) is
\[
 E_D(v)=k_j+(l_j-k_j-(1+y)/2-c/4)v+cv^2/4.
\]
It decreases with \(c\) by \(-v(1-v)/4<0\). At \(c=1\),
the verified six-pair envelope \(g_j(v)\le q_*=351/10304\)
gives
\[
 E_D(v)=v[g_j(v)-(y-1/2)/2]\le-\rho/16,
 \qquad \rho=4/7-(1/2+2q_*)=17/5152>0 .
\]
Use \(\kappa=\rho/32=17/164864\). The inverse-derivative
term has cost \(O(x^{-1/2})\) per block since the dominant
weight is at most one and \(M\le\sqrt{Y}\).

Cover the complete reflected sum, including \(n=1\), by the
clipped dyads from 1 through \(Y^{1/2}\), using \(j=0\).
The carrier costs \(Y^{-y/2}\) by Note06. The primary power is
\(1/6-y/2+(y/2-c/4)v+cv^2/4\) on \([0,1/2]\).
It is convex and is nonincreasing in \(c\) at fixed \(v\).
Its endpoints at \(c=1,y=4/7\) are \(-5/42,-13/336\),
both below \(-1/32\). Its inverse-derivative term costs
\(O(x^{-1/2})\) per block from
\(Y^{-y/2}M^{17/16}/x\), because the reflected amplitude
is at most \(M^{1/16}\). Thus both complete signed tails
pay \(O_D((1+L_x)x^{-\kappa})\).

Finally \(Q_N=O(x^{-(1+y)/4})\) uniformly in \(N\) by the
correction/carrier proof of Note06. The elementary heat
amplitude ratio \(|\mathcal A(0,z)/\mathcal A(t,z)|\le1\)
holds for \(t\ge0\) and \(L_x\ge16\).
The remainder in (2) divided by \(C_-\) is
\(O_D(x^{-3/4})(1+O(x^{-y/2}))\); both carriers and every
Gaussian exterior paid in §2 are included. Hence, with a
finite \(B_D\) absorbing the fixed prefactors and block counts,
\[
 |H_t(z)/C_-(t,z)-Z_t(z)|
 \le A_Dt+B_D(1+L_x)x^{-\kappa}
 \qquad(1\le tL_x\le C,\ 4/7\le y\le9/8).                         \tag{7}
\]
The pointwise recentered value estimate suffices for this
common-time result. All cutoff changes compare to the same
exact \(H_t\).

## 4. Final gates, overlap and scope

After \(C_P,C,D,V\), the initial inputs, and \(A_D,B_D\) are
fixed, let \(x_0\) dominate every height gate used above.
Choose \(L_*>0\) so
\[
 \begin{gathered}
 L_*\ge\max\{2,1/\kappa,4224A_D\},\qquad
 4\pi e^{L_*}\ge x_0,\\
 4224B_D(1+L_*)(4\pi e^{L_*})^{-\kappa}\le1,
 \qquad t_0=1/L_*.
 \end{gathered}
\]
This is possible because the last left-hand side tends to
zero and is decreasing for \(L\ge1/\kappa\).
For \(0<t\le t_0\), \(x\ge4\pi e^{1/t}\) gives
\(L_x\ge1/t\ge L_*\), so every height gate holds and
\(33\) times the right side of (7) is at most \(1/64\) in
the finite window. Thus the analytic \(H_t/(C_-Z_t)\)
has no zero on the full compared transverse interval.
The global initial enclosure \(y\le\sqrt{1-2t}\le1\)
and conjugation exclude all zeros with \(|y|\ge4/7\)
there. For \(tL_x\ge C\),
\[
 x\ge4\pi e^{C/t}>\exp(C_P/t),
\]
and the published all-real tail applies, including at the
equality \(tL_x=C\) also covered by (7). The range
\(x\ge4\pi e^{1/t}\) has \(tL_x\ge1\), so these two
ranges cover it. Evenness covers negative \(x\).
This proves (1) with a symbolic finite \(t_0\).

The [Note06 control screen][e01] and [Note09 signed-tail
screen][e02] apply here. The canonical coefficient, complete
reflection, source and phase assumptions persist through
(2) and (7). Euler-factor/normalized-endpoint, weighted-square
and finite-source, reflected/primitive-compatible, finite-prime,
profile and variable-readout controls fail the corresponding
premises named there. Polymath's far-tail input is the theorem
for this same complete theta field and time normalization.
Generic positive sources and freely altered readouts do not
supply that premise. A control zero in a tested region with
nonzero carrier would give relative deviation \(1\).

The onset is unevaluated. The missing compact heights depend on
\(t\), and the cutoff \(4\pi e^{1/t}\) escapes to infinity as
\(t\downarrow0\). The claim concerns the fixed-width common-time
tail in (1). The [execution record][checks] logs inputs and
finite algebra; no field samples were used.

[packet]: ../research-progress/handoffs/GNP-BB-E05-r1.md
[decision]: ../brainstorm/notes/03_GNP_BB_B03_COMMON_TIME_DECISION_20261113.md
[design]: 11_GNP_BB_B03_COMMON_TIME_DESIGN_20261113.md
[e01]: 06_GNP_BB_E01_COMPLETE_OUTER_ESTIMATE_20261113.md
[e02]: 09_GNP_BB_E02_SIGNED_TAIL_WIDTH_20261113.md
[e03]: 10_GNP_BB_E03_ENVELOPE_ENDPOINT_AND_WIDTH_20261113.md
[checks]: ../numerics/07_GNP_BB_E05_INPUTS_AND_CHECKS_20261113.json
[parent]: ../../manuscript/sections/10a_transition_green.tex
[hda]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[hreview]: ../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[outer]: https://arxiv.org/html/1904.12438v2#S1.Thmtheorem5
[poly]: https://arxiv.org/html/1904.12438v2#S3
[zeta]: https://dlmf.nist.gov/25.2
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=44
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md

