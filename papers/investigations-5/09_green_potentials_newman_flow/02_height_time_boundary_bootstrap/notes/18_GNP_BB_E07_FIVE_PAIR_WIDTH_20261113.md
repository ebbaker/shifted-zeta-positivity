# E07 r1 — five exponent pairs give width \(567/1000\)

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Subagent dispatch recorded
**gpt-6.1-sol / ultra**. Independent backend and usage metadata
were unavailable.

**Status: proved in-note from the named inherited inputs, proof-author
checked and submitted for E08 additional-agent assessment.** This
executes [E07 r1][packet] following [Notes14][pairs] and [17][decision].
The [result index][results] and [avoid index][avoid] route through
[heat-flow cluster11][r11], [controls12][r12], [classification01][a01],
[shared premises02][a02] and [scope07][a07]. The quantitative conclusion
is a width \(y_*=567/1000\), attained on the prescribed curve and
separately on a common-time exterior.

## 1. Domains and the complete field

Use \(H_0(z)=\xi((1-iz)/2)/8\) with the complete theta source and
\(\partial_t H=-H_{zz}\). Set \(z=x+iy\), \(L_x=\log(x/(4\pi))\),
\(Y=e^{L_x}\), \(c=tL_x\), and \(L(z)=\operatorname{Log}(z/(4\pi))=
\ell+i\beta\) on the right half-plane. Use the elementary
\(C_\pm=\mathcal A e^{\pm i\Theta}/2\) and
\(s_t=(1-iz)/2+tL(z)/4-i\pi t/8\) of [Note06][e01]. Throughout,
\(y_*\le y\le9/8\), \(x\) is sufficiently large, and \(0<t\le1/2\).

- On the curve use \(t=1/L_X\) across the whole closed rectangle
  \(|x-X|\le1,\ y_*\le y\le9/8\), with \(L_X=\log(X/(4\pi))\).
  Take the fixed \(r=1,b=9\) value provider, including all initial,
  enlarged fixed-chart and Gaussian gates in
  [Note06 §1][e01], and the relevant height and cutoff gates of
  [Note09 §1][e02]. Explicitly impose \(X\ge2\), \(L_X\ge64\),
  \(X-1\) above the inherited height onsets, and
  \(1/((X-1)L_X)\le10^{-5}\). Then \(X/2\le x\le3X/2\) and
  \(|c-1|\le10^{-5}\) by the mean-value bound
  \(|L_x-L_X|\le1/(X-1)\). In particular \(c\le8\).
- For the common-time proof, fix the finite absolute constant \(C_P\)
  of Polymath Theorem 1.5(i) in the matching source, height and heat
  normalization, then \(C\ge\max(8,C_P)+1\) and \(D=C+1\).
  Use [Note12 §2][e05] for the fixed \(r=1,b=9\) positive-time value
  provider at \(0\le tL_x\le D\), with all its gates. In its order of
  constants, the fixed base growth constants precede the Gaussian
  window, the enlarged zero-time charts and their local constants.
  Fix those data and the resulting provider onset before the
  comparison constants. Apply it at \(1\le c\le C\).
  The same \(t\) is used across the spatial tail. The published
  all-real theorem supplies a separate farther range.
  [Polymath Theorem 1.5(i)][outer], [E06 Review05][r05].

At every point recenter at its actual real coordinate \(x\), retaining
\(N=N_x=\lfloor Y^{1/2}\rfloor\) as the integer cutoff of that fixed
chart and its Gaussian approximation. Take \(x\ge16\pi\),
\(L_x\ge16\), \(Y^{1/8}\ge2\), and let \(K=K_x=\lfloor
Y^{1/8}\rfloor\). Then \(Y^{1/2}/2\le N\le Y^{1/2}\) and
\(Y^{1/8}/2\le K\le Y^{1/8}\). This pointwise cover also includes
every cutoff threshold. The exact field and the frozen time at an
evaluation point do not change when the chart cutoff changes.

Write \(s_t=\sigma-i\tau_D\), \(Z_t=\zeta(s_t)\). The full
[Note09 (1)][e02] formula at time \(t\) gives
\[
 \frac{H_t}{C_-}=D_N+R_N+Q_N+E_N,\qquad
 D_N=\sum_{n\le N} a_D(n)n^{i\tau_D},\qquad
 R_N=e^{2i\Theta}\sum_{n\le N}a_R(n)n^{-i\tau_R},
\]
\[
 \begin{aligned}
 \sigma&=(1+y)/2+t\ell/4,&
 \tau_D&=x/2+\pi t/8-t\beta/4,&
 \tau_R&=x/2+\pi t/8+t\beta/4,\\
 a_D(u)&=u^{-\sigma}e^{t(\log u)^2/4},&
 a_R(u)&=u^{(y-1)/2}e^{t[(\log u)^2-\ell\log u]/4}.
 \end{aligned}
\]
For \(0<\beta<\pi/2\) and \(t\le1/2\), both frequencies are in
\([x/2,x]\) at the declared heights. The drift \(\ell-L_x\)
is \(\tfrac12\log(1+(y/x)^2)\ge0\), and is retained exactly in
\(s_t\) and the amplitudes. It reduces both amplitude moduli
relative to using \(L_x\). It also gives \(t\ell\le D+1\)
eventually in the common-time domain, and a fixed bound in
the curve domain.

## 2. Both finite arms and the full error

Uniformly on both domains \(c\ge1-10^{-5}\). The real argument
and finite head margins satisfy
\[
 \sigma\ge(1+y)/2+c/4\ge413399/400000>33/32,\qquad
 (1+y)/2+7c/32\ge3207193/3200000>513/512 .
\]
The ordinary Euler product gives a nonzero analytic \(Z_t\) with
\(|1/Z_t|\le\zeta(\sigma)\le33\); the strict real margin extends
to a neighborhood of each comparison point at fixed \(t\).
The elementary \(C_-\) is independently analytic and nonzero
on the right half-plane. For \(n\le K\), \(\log n\le L_x/8\)
gives \(a_D(n)\le n^{-1-1/512}\). The inequality
\(e^w-1\le we^w\) for \(w\ge0\) pays the finite head heat removal
by \(At\), where
\[
              A=\tfrac14\sum_{n\ge2}n^{-1-1/512}(\log n)^2<\infty .
\]
The ordinary zeta series beyond \(K\) costs at most
\(32K^{-1/32}\le32\cdot2^{1/32}Y^{-1/256}\).
Only the ordinary series is extended to infinity.
[DLMF ordinary series and Euler product][zeta].

For the high dominant population \(K<n\le N\), take the real
cuts \(Y^v\) in the table below. Within each range start dyadic
blocks at the left cut and clip the last dyad at the right
cut. Use left-open, right-closed pieces. If a cut is integral,
that integer goes to the previous piece, including the first cut
in the head and the final cut in the last dyad. Thus each desired
integer occurs once. An integer at \(N\) is included whether or
not \(Y^{1/2}\) is integral.

For either exact frequency \(T=\tau_D,\tau_R\), the
Montgomery–Vaughan bound on arbitrary \(I\subset[M,2M]\) is
\[
              \left|\sum_{n\in I} n^{\pm iT}\right|
               \ll x^kM^{l-k}+M/x .
\]
In Definitions 16.1–16.2 use derivative parameter \(\theta=1\)
and scale \(T/(2\pi)\). The positive phase \(T\log(u)/(2\pi)\)
matches every required derivative exactly; conjugation covers
the negative sign. A half-open subinterval with at least two
integers has the same integer set as the closed interval between
its first and last integers. A singleton costs at most \(1\)
and is included in \(x^kM^{l-k}\) for the fixed pairs and \(M,x\ge1\).
The empty sum is zero. The usual \(A,B\) transforms in Theorems
16.23 and 16.25 preserve exponent pairs, and \(P=AB(0,1)=(1/6,2/3)\).
The following words act from right to left on \(P\).
These primary passages were rechecked. [Montgomery–Vaughan][mv],
[Source use02][src02], [Source use03][src03].

On each clipped block, \(|u\,a'(u)/a(u)|\) is bounded by a
fixed \(J\) for both weights: the log derivatives times \(u\)
are \(-\sigma+t\log u/2\) and
\((y-1)/2-t\ell/4+t\log u/2\), respectively, with
\(t\log u\le c/2\). Here \(J\) is absolute on the curve
domain and may depend on \(D\) on the common-time domain.
Thus the supremum plus total variation is at most
\(2^J(1+J\log2)a(M)\), paying Abel summation of the arbitrary
partial sums. The total block count is \(O(1+L_x)\), since a
range \([Y^a,Y^b]\) uses at most \(1+(b-a)L_x/\log2\)
dyads. Constants depend only on the declared data.

For \(v=\log M/L_x\) the dominant primary power of \(Y\)
after weighting is bounded by
\[
 E_D(v)=k+\bigl(l-k-(1+y)/2-c/4\bigr)v+cv^2/4.
\]
At \(c=1\), it is \(v[g(v)-(y-1/2)/2]\) with
\(g(v)=k/v+l-k-1+v/4\). The five-piece calculation is

| Scale \(v\) | Word | Pair \((k,l)\) | \(g\) at left | \(g\) at right |
| --- | --- | --- | --- | --- |
| \([1/8,4/25]\) | \(A^5\) | \((1/254,247/254)\) | \(1/32\) | \(841/25400\) |
| \([4/25,89/500]\) | \(A^5BA^2\) | \((11/1642,1573/1642)\) | \(5443/164200\) | \(4883141/146138000\) |
| \([89/500,11/50]\) | \(A^4BABA\) | \((1/102,385/408)\) | \(303221/9078000\) | \(1873/56100\) |
| \([11/50,9/20]\) | \(A^3BA^2BA\) | \((13/502,445/502)\) | \(18371/552200\) | \(5531/180720\) |
| \([9/20,1/2]\) | identity | \((1/6,2/3)\) | \(-37/2160\) | \(-1/24\) |

Each endpoint is at most \(q=669/20000\) and \(g''(v)=2k/v^3\ge0\)
on each piece. Since \((y_*-1/2)/2=q+1/20000\) and \(v\ge1/8\),
the primary power at \(c=1\) is at most \(-1/160000\).
The clock dependence is \(-v(1-v)/4\) per unit increase in
\(c\); at \(c\ge1\) it only improves the power. The curve drift
costs at most \(10^{-5}/16=1/1600000\), so even across the
whole curve box \(E_D\le-9/1600000<-1/200000\).
Take \(\kappa=1/200000\). For the secondary term
\(a_D(M)\le1\) since \(\log M\le L_x/2\) and \(\ell\ge L_x\),
so \(a_D(M)M/x=O(x^{-1/2})\) per block.
See the [small exact replay and input record][checks].

For the reflected population use \(P\) on clipped dyads
covering \([1,Y^{1/2}]\), including \(n=1\) exactly once.
The phase integral in Note06 gives
\(|e^{2i\Theta}|\le Y^{-y/2}\) on both domains.
The primary power of \(Y\) is at most
\[
 E_R(v)=1/6-y/2+(y/2-c/4)v+cv^2/4,\qquad 0\le v\le1/2.
\]
It is convex, with endpoints bounded by \(-701/6000\) and
\(-180397/4800000\) at \(y=y_*\), \(c=1-10^{-5}\).
Both are strictly below \(-1/32\). For the inverse-frequency
term the heat factor in \(a_R\) is at most one, so
\(a_R(M)\le M^{1/16}\). With the carrier its cost is at
most \(O(x^{-y/2}M^{17/16}/x)=O(x^{-1/2})\).
This handles the entire reflected cutoff population.

For the correction \(Q_N\), CB4 and the bounded removable
quotient \(\mathcal C(a(z)-N)\) give the uniform bounds in
[Note06 §2][e01]; in particular the correction factor costs
\(O(x^{-1/4})\) even at cutoff positions. The geometric gamma
factor is comparable to \(|\mathcal A(0,z)|/2\), while
\(|\mathcal A(0,z)/\mathcal A(t,z)|\le1\) by \(L_x\ge16\)
and \(|\beta|<\pi/2\). Use \(e^{-\pi^2t/64}\le1\) and
\(|e^{i\Theta}|\le Y^{-y/4}\) to get
\(Q_N=O(x^{-(1+y)/4})\). The full remaining error \(E_N\) is
\(O_D(x^{-3/4})(1+O(x^{-y/2}))\) after dividing the provider's
two-carrier envelope by \(C_-\). All true and artificial
Gaussian/source tails are included in that inherited value bound,
with the original \(c\le8\) provider on the curve and the proved
larger positive-time provider on the finite common-time window.
The reviews retain their respective evidence levels.
[Review03][r03], [Review05][r05].

Adding the complete payments, with \(Y=x/(4\pi)\), gives
\[
       |H_t/C_- -Z_t|
          \le At+B_D(1+L_x)x^{-\kappa}.
\]
The constant \(B_D\) absorbs only finite prefactors from the fixed
pairs, block count, variations, ordinary tail, correction and
remainder. The curve domain uses its own finite prefactor and
provider onset. All normalized comparisons concern exact
analytic fields at fixed time.

## 3. Curve and common-time conclusions

**Curve.** Since \(x\ge X-1\) and
\(L_x\le L_X+1/(X-1)\), increasing the curve prefactor to \(B\)
gives, uniformly on the whole closed curve rectangle,
\[
    |H_{1/L_X}/C_--Z_{1/L_X}|
       \le A/L_X+B(1+L_X)(X-1)^{-\kappa}.
\]
In addition to §1, impose \(L_X\ge\max(1/\kappa,4224A)\) and
\(4224B(1+L_X)(X-1)^{-\kappa}\le1\) beyond a finite height.
The last left side decreases to zero on the eventual range,
by logarithmic differentiation. The factor \(33\) times the
whole bound is then at most \(1/64\). In particular the closed
rectangle is zero-free by the independent carrier and
\(|H_t/(C_-Z_t)-1|\le1/64\). The de Bruijn contraction in
Polymath Theorem 3.2 starts from width \(1\) by the \(\xi\) zero
strip and gives width \(\sqrt{1-2/L_X}\le1\) at the prescribed
time. Together with conjugation, the rectangle gives
\[
 X\ \text{sufficiently large},\quad
 H_{1/L_X}(X+iy)=0\ \Longrightarrow\ |y|<567/1000 .
\]
The time is fixed within each rectangle. [Polymath §3][poly].

**Common time.** Let \(x_0\) dominate all the fixed height
gates of §§1–2 for the range \(1\le tL_x\le C\). After the
provider and comparison constants are fixed, choose \(L_*\)
so that
\[
 L_*\ge\max(2,1/\kappa,4224A),\qquad
 4\pi e^{L_*}\ge x_0,\qquad
 4224B_D(1+L_*)(4\pi e^{L_*})^{-\kappa}\le1.
\]
This is possible because \((1+L)(4\pi e^L)^{-\kappa}\)
is decreasing for \(L\ge1/\kappa\) and tends to zero.
Set \(t_*=1/L_*\). At \(0<t\le t_*\), \(x\ge4\pi e^{1/t}\)
gives \(L_x\ge1/t\ge L_*\) and \(tL_x\ge1\). In the transition
window \(At\le A/L_*\) and the monotonic tail payment give
relative error at most \(1/64\) after the factor \(33\).
The provider and exact \(s_t\) then exclude the closed
\([y_*,9/8]\) at each point of the transition window. The
initial enclosure at this fixed \(t\) pays higher transverse
coordinates, and conjugation pays the lower half-plane.
At every \(x\) with \(tL_x\ge C\),
\(x\ge4\pi e^{C/t}>e^{C_P/t}\), so Polymath Theorem 1.5(i)
gives \(y=0\) for zeros. This includes the common endpoint
\(tL_x=C\) of the two ranges. Evenness gives the result
for negative \(x\). Hence
\[
   0<t\le t_*,\quad |x|\ge4\pi e^{1/t},\quad H_t(x+iy)=0
              \quad\Longrightarrow\quad |y|<567/1000 .
\]
This is an exterior at a common fixed time. The source
and normalizations agree with Polymath's by §1.
[Polymath Theorem 1.5(i)][outer].

## 4. Controls and scope

The [Note06 §4][e01], [Note12 §4][e05] and [Note17 §5][decision]
premise screens continue to apply. Euler-factor and normalized
endpoint controls lack ordinary coefficient identification.
Weighted-square, finite-tail and finite-prime changes lack the
full coefficients and normalized reflection together.
Reflected, smooth and primitive-compatible controls lack the
complete canonical square arithmetic. Atomic and finite-profile
controls lack the complete source/profile and corresponding
coefficients. Variable readouts lack the actual cosine heat
field. Relaxed positive measures lack identification with the
actual integer divisor. Arbitrary phase changes lack the exact
logarithmic phase used in the subinterval bound. A control zero
in the compared region, with a nonzero carrier, has relative
deviation \(1\). The published far-tail step requires that same
complete canonical field.

The new width is below \(4/7\) by \(31/7000\) and below E03's
scoped A-chain threshold by \(727/644000\). No additional
exponent-pair search, numerical field evaluation or evaluated
onset enters this result. Compact heights, the near-zero-time
barrier, a time-zero bound and any global Newman conclusion need
different inputs. The [global-use audit][global] specifies those
obligations. The small [record][checks] verifies finite
arithmetic and byte identities.

[packet]: ../research-progress/handoffs/GNP-BB-E07-r1.md
[pairs]: 14_GNP_BB_B04_BROADER_PAIR_COMPARISON_20261113.md
[decision]: 17_GNP_BB_B04_DECISION_AND_EXECUTION_CONTRACT_20261113.md
[global]: 16_GNP_BB_B04_GLOBAL_CONSUMER_AUDIT_20261113.md
[e01]: 06_GNP_BB_E01_COMPLETE_OUTER_ESTIMATE_20261113.md
[e02]: 09_GNP_BB_E02_SIGNED_TAIL_WIDTH_20261113.md
[e05]: 12_GNP_BB_E05_COMMON_TIME_TAIL_20261113.md
[r03]: ../reviews/03_GNP_BB_E01_E03_ADDITIONAL_AGENT_REVIEW_20261113.md
[r05]: ../reviews/05_GNP_BB_E05_COMMON_TIME_REVIEW_20261113.md
[checks]: ../numerics/13_GNP_BB_E07_INPUTS_AND_CHECKS_20261113.json
[src02]: ../references/02_GNP_BB_SIGNED_TAIL_SOURCE_USE_20261113.md
[src03]: ../references/03_GNP_BB_B04_SOURCE_USE_20261113.md
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=44
[zeta]: https://dlmf.nist.gov/25.2
[outer]: https://arxiv.org/html/1904.12438v2#S1.Thmtheorem5
[poly]: https://arxiv.org/html/1904.12438v2#S3
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md

