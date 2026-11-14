# E02 r1 — signed finite tails give width \(7/12\)

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Subagent dispatch recorded
**gpt-6.1-sol / ultra**. Independent backend and token-use metadata
were unavailable.

**Status: proved in-note from the named inherited inputs, submitted
for additional-agent assessment.** This is the fixed [E02 r1][packet]
contract following [Decision02][decision] and [Notes07][design] and
[08][geometry]. The [result index][results] and [avoid index][avoid]
route through [heat-flow cluster11][r11], [controls12][r12],
[classification01][a01], [shared premises02][a02] and [scope07][a07].
This is a quantitative approximation and zero-exclusion milestone.

## 1. Fixed clock, full field and zero-free carrier

Keep the complete theta field \(H_\lambda\), with
\(H_0(z)=\xi((1-iz)/2)/8\), \(\partial_\lambda H=-H_{zz}\).
For every sufficiently large real \(X\), put \(L_X=\log(X/(4\pi))\)
and freeze \(\lambda=1/L_X\) on the closed rectangle
\[
 \overline D_X=\{|x-X|\le1,\quad 7/12\le y\le9/8\},\qquad z=x+iy .
\]
Write \(L_x=\log(x/(4\pi)),\ Y=e^{L_x},\ c_x=\lambda L_x\),
\(L(z)=\operatorname{Log}(z/(4\pi))=\ell+i\beta\), using the
right-half-plane branch. The [Note06 §1 provider ledger][baseline]
applies to each chart centered at \(x\) with \(r=1,b=9\),
including enlarged charts, cutoff crossings, calibration and the
complete source and artificial Gaussian exteriors. Let \(x_0\) be
its finite provider onset. Retain the chart constants \(h_9,g_9,f_9\).
Impose \(X\ge2\), \(X-1\ge x_0\), \(L_X\ge64\),
\(2/(XL_X)\le1/10000\), \(Y^{1/8}\ge2\) and \(x\ge16\pi\)
for \(|x-X|\le1\); the last two follow eventually at \(x=X-1\).
Then \(X/2\le x\le3X/2\) and
\[
 |c_x-1|\le 1/10000,\qquad 0<\lambda\le1/2,\qquad
 0\le\ell-L_x=\tfrac12\log(1+(y/x)^2)\le (9/8)^2/(2x^2),
 \quad 0<\beta<\pi/2 .
\]
In particular \(0<\lambda L_x<8\) and \(\lambda\ell\le2\)
after enlarging the onset. The point lies in the fixed \(r=1,b=9\)
chart even on an edge or at a cutoff threshold. Use the exact
\(N=N_x=\lfloor Y^{1/2}\rfloor\) in that chart, including its
correction, and \(K=K_x=\lfloor Y^{1/8}\rfloor\) for the finite
dominant prefix. Both cutoffs are between half their real scales
and those scales.

Use the exact \(\mathcal A,\Theta,C_\pm,s_\lambda\) in Note06,
which agree with the [parent formulas][parent]. In particular,
\[
 s_\lambda(z)=\sigma-i\tau_D=(1-iz)/2+\lambda L(z)/4-i\pi\lambda/8,\quad
 \sigma=(1+y)/2+\lambda\ell/4 .
\]
The lower bound \(\sigma\ge19/24+9999/40000=124997/120000>33/32\)
follows from \(\ell\ge L_x\). Put \(Z_\lambda=\zeta(s_\lambda)\).
The ordinary Euler product in \(\sigma>1\) proves that \(Z_\lambda\)
is analytic and nonzero on a neighborhood of \(\overline D_X\), and
\(|1/Z_\lambda|\le\prod_p(1+p^{-\sigma})\le\zeta(\sigma)\le33\).
The elementary \(C_-\) is analytic and nonzero there independently.
[DLMF §25.2][zeta].

With \(V_\lambda=H_\lambda/C_-\), the full HDA formula gives
\[
\begin{aligned}
 V_\lambda&=D_N+R_N+Q_N+E_N,\\
 D_N&=\sum_{n\le N}a_D(n)n^{i\tau_D},&
 a_D(u)&=u^{-\sigma}\exp(\lambda(\log u)^2/4),\\
 R_N&=e^{2i\Theta}\sum_{n\le N}a_R(n)n^{-i\tau_R},&
 a_R(u)&=u^{(y-1)/2}
       \exp(\lambda[(\log u)^2-\ell\log u]/4),\\
 \tau_D&=x/2+\pi\lambda/8-\lambda\beta/4,&
 \tau_R&=x/2+\pi\lambda/8+\lambda\beta/4 ,
\end{aligned}                                                     \tag{1}
\]
where \(Q_N=e^{-\pi^2\lambda/64}\mathcal R_N/C_-\) and
\(E_N=(H_\lambda-F_N^{\rm HDA})/C_-\) have the meanings in
[Note06 §2][baseline]. Both actual real frequencies lie between
\(x/2\) and \(x\) on the eventual domain. The imaginary part of
\(L(z)\) is therefore included exactly in the phase, and the
real part is included exactly in the positive amplitudes.

The Note06 carrier proof, integrating
\(\Theta_z=L(z)/4+\pi\lambda/(16z)\) vertically, applies to every
\(0\le y\le9/8\) and gives \(|e^{2i\Theta}|\le Y^{-y/2}\).
The Note06 correction argument uses only \(L_x\ge16\) and this
upper bound on \(y\). Thus for \(P=(4\pi)^{9/16}\) the complete
separate bounds on the new box are
\[
 |Q_N|\le g_9 f_9 \sqrt P\,x^{-(1+y)/4}
          \le g_9 f_9\sqrt P\,x^{-19/48},\qquad
 |E_N|\le h_9(1+P)x^{-3/4}.                                      \tag{2}
\]
The cutoff joins and source/Gaussian terms are included at the
inherited HDA evidence level. No derivative of the cutoff is used.
[HDA CS6][hda], [HDA Assessment03][hreview].

## 2. Exponent pairs and dyadic variation

The [author-hosted Montgomery–Vaughan chapter][mv], printed pp. 32–33,
37 and 41, was checked on 13 November. Definitions 16.1–16.2 and
(16.55)–(16.58) give the exponent-pair bound on any subinterval
\(I\subset[M,2M]\), for real \(M>0\). For frequency \(T\) equal to
\(\tau_D\) or \(\tau_R\), choose their derivative parameter
\(\theta=1\), scale \(T/(2\pi)>0\), and phase
\(f(u)=T\log u/(2\pi)\). Every derivative of \(f\) is exactly the
reference derivative, for all required orders and tolerances.
Take conjugates for the negative sign. Theorems 16.23 and 16.25
give the \(A\) and \(B\) transforms. Starting with the trivial
pair \((0,1)\), \(AB(0,1)=(1/6,2/3)\), and its second and fourth
\(A\)-transforms are respectively \((1/30,13/15)\) and
\((1/126,20/21)\). The resulting bound with its secondary term is
\[
 \left|\sum_{n\in I}n^{\pm iT}\right|\ll x^k M^{l-k}+M/x.          \tag{3}
\]
Constants depend only on the fixed pairs since \(T/x\in[1/2,1]\).
For a half-open or singleton subinterval, apply the same theorem
to the closed interval between the smallest and largest included
integers when at least two integers are included. A singleton is
bounded by \(1\), which is covered by \(x^kM^{l-k}\) in the scales
\(1\le M\le\sqrt Y\) here. The empty sum is zero. This handles
partial sums at all endpoints. See the [canonical source record][mvr].

For either positive amplitude \(a=a_D,a_R\),
\[
 ua_D'/a_D=-\sigma+\lambda\log u/2,\qquad
 ua_R'/a_R=(y-1)/2-\lambda\ell/4+\lambda\log u/2 .
\]
Their absolute values are at most \(4\) on \(1\le u\le Y^{1/2}\)
using \(\lambda\ell\le2\), \(c_x\le1+10^{-4}\) and \(y\le9/8\).
On a clipped dyad \([M,M']\subset[M,2M]\) in this range,
\(a(u)\le2^4a(M)\) and \(\int_M^{M'}|a'(u)|\,du\le 4\log(2)2^4 a(M)\).
Abel summation of the exact phase multiplies the bound (3) by at
most \(2^4(1+4\log 2)a(M)\). The partition starts at real powers
of \(Y\), so no loss from rounding these left endpoints occurs.

## 3. Dominant prefix and both signed tails

For \(n\le K\), \(\log n\le L_x/8\) and
\[
 a_D(n)\le n^{-[(1+y)/2+7c_x/32]}\le n^{-129/128},
 \qquad 19/24+7(9999/10000)/32=969979/960000>129/128.
\]
With \(e^v-1\le ve^v\) for \(v\ge0\), the heat removal on this
finite prefix is at most \(A/L_X\), where
\[
 A=\tfrac14\sum_{n\ge2}n^{-129/128}(\log n)^2<\infty .
\]
The ordinary zeta series has tail beyond \(K\) bounded by
\(32K^{-1/32}\le32\cdot 2^{1/32}Y^{-1/256}\). The remaining
heat-weighted terms are exactly those from \(K<n\le N\).

For those terms cover \((Y^{1/8},Y^{1/4}]\) and
\((Y^{1/4},Y^{1/2}]\) by clipped dyads, starting each at its
left endpoint, doubling until the range is exhausted. Use left-open,
right-closed pieces. An integer at the internal junction belongs
to the first interval, an integer at the final endpoint is included,
and the first interval's lower endpoint belongs to the prefix if
it is an integer. Thus every desired integer occurs exactly once.
For each left endpoint \(M\) put \(v=\log M/L_x\). After weighting,
the first term in (3) is at most a constant times \(Y^{E_D(v)}\),
where
\[
 E_D(v)=k+\bigl(l-k-(1+y)/2-c_x/4\bigr)v+c_xv^2/4 .
\]
The complex logarithm's real difference \(\ell-L_x\) contributes
the exact factor \(e^{-\lambda(\ell-L_x)\log M/4}\le1\).
The largest value in \(y\) occurs at \(7/12\). At that value
and \(c_x=1\) the endpoints are as follows.

| \(v\)-range | \((k,l)\) | Left exponent | Right exponent |
| --- | --- | --- | --- |
| \([1/8,1/4]\) | \((1/126,20/21)\) | \(-5/16128\) | \(-1/1344\) |
| \([1/4,1/2]\) | \((1/30,13/15)\) | \(-1/320\) | \(-1/120\) |

The quadratics are convex. Clock variation adds at most
\(|c_x-1|(v-v^2)/4\le1/160000\). The resulting bound is
\[
 E_D(v)\le -1531/5040000 < -1/4096 .
\]
The inverse-derivative term costs \(O(x^{-1/2})\) per block
since \(a_D(M)\le1\) by \(\log M\le L_x/2\), and \(M\le\sqrt Y\).

For the reflected population cover \([1,Y^{1/2}]\) by clipped
dyads from \(1\), including the integer \(1\) and each later
junction once. Use \((k,l)=(1/6,2/3)\) on every block. With
the carrier bound in §1 and the same helpful real-log factor,
the primary reflected power is at most
\[
 E_R(v)=\tfrac16-\tfrac y2+
         (\tfrac y2-\tfrac{c_x}4)v+\tfrac{c_x}4v^2
 \qquad (0\le v\le1/2).
\]
The endpoints are at most \(-1/8\) and
\(-1/24+1/160000\), respectively. Convexity yields
\(E_R(v)\le-1/32\). For the secondary term
\(a_R(M)\le M^{1/16}\), because
\(0\le\log M\le L_x/2\le\ell\). After the carrier this costs
\(O(Y^{-y/2}M^{17/16}/x)=O(x^{-1/2})\) per block
(using \(y\ge7/12\)). This counts the entire reflected arm.

Each partition has \(O(1+L_x)\) blocks, since the number of
doublings on \([Y^a,Y^b]\) is at most \(1+(b-a)L_x/\log 2\).
Combining all payments and (2), then using \(x\ge X-1\) and
\(L_x\le L_X+2/X\), gives finite \(B\) independent of \(X\)
and the fractional cutoffs, such that
\[
 \sup_{\overline D_X}|V_\lambda-Z_\lambda|
 \le A/L_X+B(1+L_X)(X-1)^{-1/4096}.                             \tag{4}
\]
Here \(B\) absorbs the fixed three exponent-pair and Abel constants,
the fixed block-count factor, ordinary tail prefactor and the
two correction/remainder prefactors of (2). Conversion from \(Y\)
to \(x\) introduces only fixed powers of \(4\pi\).

## 4. Onset, width and screened scope

Set \(\delta=1/4096\). In addition to the gates of §1, choose
\(X_*\) so \(L_X\ge\max(4096,4224A)\) and
\(4224B(1+L_X)(X-1)^{-\delta}\le1\) for \(X\ge X_*\).
These gates are finite because the second left side tends to zero
and is nonincreasing when \(L_X\ge4096\), by logarithmic
differentiation. Then \(33\) times (4) is at most \(1/64\).
It follows that the exact analytic \(F=H_\lambda/(C_-Z_\lambda)\)
satisfies \(|F-1|\le1/64\) on the full closed rectangle and
\(H_\lambda\) is nonzero there. All constants and onsets remain
symbolic.

The contour is the complete \(\partial D_X\) at the fixed time
\(\lambda_X\), with prescribed observation
\(p_X=X+i(\sqrt{1-2/L_X}+1/32)\). This lies strictly inside and above
the initial enclosure since \(L_X\ge64\). The direct floor covers the
whole closed rectangle, so at the center it excludes all
\(7/12\le y\le\sqrt{1-2/L_X}\). The initial enclosure follows from
the time-zero \(\xi\) strip and Polymath Theorem 3.2, and the real
source gives conjugation. Hence for every real \(X\ge X_*\),
\[
 H_{\lambda_X}(X+iy)=0\quad\Longrightarrow\quad |y|<7/12.
\]
Each real center has its own bounded complete contour. No behavior
of a single varying-time holomorphic field or unbounded-contour
end limit is invoked. [Polymath §3][poly], [geometry][geometry].

The [Note06 control screen][baseline] applies to the unchanged
canonical source and provider. Euler-factor and normalized endpoint
controls fail the unchanged ordinary coefficients, weighted-square
and finite-tail controls fail the complete coefficients and reflection
together, reflected/smooth/primitive and older counter-kernels lack
the same arithmetic completion, finite-prime controls fail reflection
and the coefficient continuation, and atomic/finite-profile controls
lack the full source/profile. Variable-readout controls lack the
cosine heat field. The new dyadic payment also uses each actual
single logarithmic phase, which an arbitrary phase relaxation lacks.
On a box containing a control zero with nonzero comparison carrier
the relative deviation there equals \(1\).

The result is on the height-dependent \(1/L_X\) time curve and is
uniform in its full high-height tail. Finite-height coverage,
common-time contraction, a time-zero conclusion, and line-reaching
iteration require separate estimates. The [execution record][checks]
checks the finite algebra and input bytes. No field evaluation was used.

[packet]: ../research-progress/handoffs/GNP-BB-E02-r1.md
[decision]: ../brainstorm/notes/02_GNP_BB_B02_LOCAL_COVER_AND_SIGNED_TAIL_DECISION_20261113.md
[design]: 07_GNP_BB_B02_FINITE_ARM_COMPARISON_20261113.md
[geometry]: 08_GNP_BB_B02_GEOMETRY_AND_OBSERVATION_20261113.md
[baseline]: 06_GNP_BB_E01_COMPLETE_OUTER_ESTIMATE_20261113.md
[checks]: ../numerics/04_GNP_BB_E02_INPUTS_AND_CHECKS_20261113.json
[parent]: ../../manuscript/sections/10a_transition_green.tex
[hda]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[hreview]: ../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[mvr]: ../../01_riemann_siegel_evolution/references/03_GNP_RS_B10_EXPONENT_PAIR_AUDIT_SOURCE_20261112.md
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=44
[zeta]: https://dlmf.nist.gov/25.2
[poly]: https://arxiv.org/html/1904.12438v2#S3
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md

