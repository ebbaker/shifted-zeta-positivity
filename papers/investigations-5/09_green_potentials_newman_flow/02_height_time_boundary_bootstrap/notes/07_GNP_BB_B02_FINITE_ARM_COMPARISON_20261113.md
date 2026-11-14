# B02 finite Riemann–Siegel arm comparison on the \(1/L_X\) curve

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Delegated tool selection
**gpt-6.1-sol / ultra**. Backend configuration beyond that selection
is unavailable.

**Status.** Bounded feasibility comparison and execution proposal.
The finite-sum powers and variation payments are checked below.
The combined canonical estimate remains a proof target. No field scan
was used. This is a quantitative fixed-depth comparison under the
[B02 specification][overview], [Notes01][start], [03][baseline] and
[05][program]. Read the [result index][results] and [avoid index][avoid],
with [heat-flow cluster11][r11], [controls12][r12], [classification01][a01],
[control premises02][a02] and [scope07][a07].

## 1. Field, cutoff and ordinary zeta target

Use \(H_0(z)=\xi((1-iz)/2)/8\) and \(\partial_\lambda H=-H_{zz}\).
Fix \(X\) large, \(x=\Re z\), \(|x-X|\le1\) and \(7/12\le y=\Im z\le9/8\).
Put \(L_x=\log(x/(4\pi))\), \(L(z)=\operatorname{Log}(z/(4\pi))\),
and freeze \(\lambda=1/L_X\) throughout the box. For the parameter
comparison write \(\lambda=c/L_X\), \(c_x=\lambda L_x\).
For the fixed target \(c=1\) and \(|c_x-1|\le10^{-4}\)
eventually, from \(|L_x-L_X|\le1/(X-1)\).

Use \(C_\pm=\mathcal A e^{\pm i\Theta}/2\) and
\(s_\lambda=(1-iz)/2+\lambda L(z)/4-i\pi\lambda/8\) of [Note03][baseline].
The [parent transition formulas][provider] use [HDA CS6][hda] on fixed
recentered charts (\(r=1,b=9\)), with the full Gaussian exterior and
eventual gates. At each \(x\), freeze the exact integer
\(N_x=\lfloor\exp(L_x/2)\rfloor\). Put \(s_\lambda=\sigma-i\tau_D\)
and \(\tau_R=x/2+\pi\lambda/8+\lambda\Im L(z)/4\). Both frequencies are
\(\asymp x\). The normalized field is
\[
\begin{split}
 H_\lambda/C_-&=D_N+R_N+Q_N+E_N,\\
 D_N&=\sum_{n\le N_x} n^{i\tau_D}a_D(n),&
 a_D(u)&=u^{-\sigma}\exp(\lambda(\log u)^2/4),\\
 R_N&=e^{2i\Theta}\sum_{n\le N_x}n^{-i\tau_R}a_R(n),&
 a_R(u)&=u^{(y-1)/2}\exp\{\lambda[(\log u)^2-\Re L(z)\log u]/4\}.
\end{split}                                                     \tag{1}
\]
Here \(Q_N=e^{-\pi^2\lambda/64}\mathcal R_{N_x}/C_-\) and
\(E_N=(H_\lambda-F_{N_x})/C_-\) retain the correction and provider
remainder. The target is \(Z_\lambda=\zeta(s_\lambda)\) at the exact
complex argument and frozen time. These are value estimates with each
cutoff used at its own point.

On the chosen box \(\Re L(z)\ge L_x\), so
\(\sigma\ge(1+y)/2+c_x/4\ge124997/120000>33/32\).
The ordinary [Dirichlet series][zseries] and [Euler product][euler]
give \(|1/Z_\lambda|\le\zeta(\sigma)\le33\). In general the limiting
absolute-series condition is \(y>1-c/2\), with a fixed positive margin
for this Euler-product floor.

## 2. Dyadic estimate and variation

[Montgomery–Vaughan, Chapter 16][mv], Definitions 16.1–16.2 and
(16.55)–(16.58), apply to arbitrary subintervals of \([M,2M]\).
For \(f(u)=T\log u/(2\pi)\), take their derivative parameter
\(\theta=1\) and their scale \(T/(2\pi)>0\). The reference derivatives
match exactly for every required order and tolerance.
For either phase sign by conjugation, \(T\asymp x\) gives
\[
 \sup_{I\subset[M,2M]}\left|\sum_{n\in I}n^{\pm iT}\right|
 \ll x^k M^{l-k}+M/x.                                            \tag{2}
\]
Half-open pieces have the same included integers as suitably chosen
closed intervals. Theorems 16.23 and 16.25 give
\(A(k,l)=(k/(2k+2),(k+l+1)/(2k+2))\) and
\(B(k,l)=(l-1/2,k+1/2)\). In particular
\[
 (k_j,l_j)=A^j AB(0,1)=
 \left(\frac1{2^{j+3}-2},1-\frac{j+2}{2^{j+3}-2}\right)
 \quad(j\ge0).                                                   \tag{3}
\]
Thus \(j=0,2,4\) give \((1/6,2/3),(1/30,13/15),(1/126,20/21)\).
The definitions, process statements and inverse first-derivative
term were checked in the author text, printed pp. 32–33, 37, 41.
Sibling [Notes25][b08], [29][b10] and [31][b10audit] route to
earlier source checks. Their log-ratio phases, Mellin means and
averaging windows are separate from the pointwise phase here.

The logarithmic derivatives are
\[
 u\,a_D'(u)/a_D(u)=-\sigma+\lambda\log u/2,\qquad
 u\,a_R'(u)/a_R(u)=(y-1)/2-\lambda\Re L(z)/4+\lambda\log u/2 .
\]
They are uniformly bounded for \(1\le u\le\exp(L_x/2)\).
On each clipped block \([M,M']\) with \(M'\le2M\), the supremum
plus total variation is \(O(a(M))\), by integrating \(|a'|\ll a/u\).
Partial summation multiplies (2) by \(O(a(M))\), without further
loss within a block. There are \(O(1+L_x)\) blocks.

## 3. Fixed comparison at \(y\ge7/12\)

Let \(K=\lfloor\exp(L_x/8)\rfloor\). For \(n\le K\),
\[
 a_D(n)\le n^{-[(1+y)/2+7c_x/32]}\le n^{-129/128},
\]
since the minimum exponent under the clock gate is
\(969979/960000>129/128\). The inequality \(e^v-1\le ve^v\)
pays heat-weight removal on the finite prefix by
\(\sum_{n\ge2}n^{-129/128}(\log n)^2/(4L_X)\).
The ordinary zeta tail beyond \(K\) costs at most
\(32K^{-1/32}\ll x^{-1/256}\) once \(\exp(L_x/8)\ge2\).
The remaining heat-weighted sum ends at \(N_x\).

For the dominant tail use the real scales
\(\exp(L_x/8),\exp(L_x/4),\exp(L_x/2)\). In each range start the
dyadic blocks at its left endpoint, with pieces open on the left and
closed on the right. This includes each integer beyond \(K\) exactly
once through \(N_x\). With \(v=\log M/L_x\), the first term of (2)
after weighting has power of \(x/(4\pi)\) at most
\[
 E_D(v)=k+(l-k-(1+y)/2-c_x/4)v+c_xv^2/4 .                         \tag{4}
\]
The largest value at each \(v\) occurs at \(y=7/12\). At \(c_x=1\)
the power is \(k+(l-k-25/24)v+v^2/4\).
Clock variation adds at most \(|c_x-1|(v-v^2)/4\le1/160000\).

| Range for \(v\) | Pair index from (3) | Left power | Right power |
| --- | --- | --- | --- |
| \([1/8,1/4]\) | 4 | \(-5/16128\) | \(-1/1344\) |
| \([1/4,1/2]\) | 2 | \(-1/320\) | \(-1/120\) |

Convexity bounds each interval by its largest endpoint power.
With clock variation the power is at most
\(-1531/5040000<-1/4096\). The inverse-derivative term costs
\(O(x^{-1/2})\) per block because \(a_D(M)\le1\) and \(M\ll\sqrt x\).

For the entire reflected population use \(j=0\) on clipped dyads
from 1 through \(N_x\), including integer 1. The carrier satisfies
\(|e^{2i\Theta}|\le(x/(4\pi))^{-y/2}\) since
\(\Im[z(L(z)-1)]=\int_0^y\Re L(x+iu)\,du\ge yL_x\)
and \(\lambda\Im L(z)\ge0\).
The reflected block power is
\[
 E_R(v)=\tfrac16-\tfrac y2+
             (\tfrac y2-\tfrac{c_x}4)v+\tfrac{c_x}4v^2,
 \qquad 0\le v\le1/2.
\]
Its endpoints are \(1/6-y/2\le-1/8\) and
\(1/6-y/4-c_x/16\le-1/24+1/160000\). Convexity gives at most
\(-1/32\). For the inverse term use \(a_R(M)\le M^{1/16}\), since
\(y\le9/8\) and the heat factor is at most 1. Thus
\(x^{-y/2}M^{17/16}/x\ll x^{-1/2}\).

The parent provider gives \(Q_N=O(x^{-(1+y)/4})\).
Indeed \(e^{-\pi^2\lambda/64}|\mathcal A(0,z)/\mathcal A(\lambda,z)|
=\exp(-\lambda\Re(L(z)^2)/16)\le1\) eventually, the normalized
carrier costs \(O(x^{-y/4})\), and the correction factor
\(O(x^{-1/4})\) holds uniformly in the fractional cutoff.
The remaining envelope is \(E_N=O(x^{-3/4})(1+O(x^{-y/2}))\).
Its inherited fixed-buffer estimate includes the complete Gaussian
exterior. The exact complex shift and clock are used in (1).

**Proposed execution contract.** Acquire the canonical estimate
from the cited provider with every chart and buffer gate explicit.
For fixed finite \(A,B\) require
\[
 \sup_{\substack{|\Re z-X|\le1\\7/12\le\Im z\le9/8}}
 \left|\frac{H_{1/L_X}(z)}{C_-(1/L_X,z)}-Z_{1/L_X}(z)\right|
 \le A/L_X+B(1+L_X)(X-1)^{-1/4096}.                              \tag{5}
\]
Impose \(33[A/L_X+B(1+L_X)(X-1)^{-1/4096}]\le1/16\).
The box then passes the direct normalized nonvanishing test.
[Polymath v2, Theorem 3.2][poly] applied to initial width \(1\),
plus conjugation, would give \(|\Im\rho|<7/12\) for zeros with
\(\Re\rho=X\) at time \(1/L_X\). The provider for the \(9/8\)
boundary is HDA CS6. A Cauchy or Green consumer on the same box
has the same arithmetic input (5). Common-time enclosures,
finite-height coverage and iteration toward the line need further
estimates.

## 4. Scoped limit of this payment scheme

At \(c_x=1\) put \(\delta=(y-1/2)/2\), so the limiting real
part is \(1+\delta\). An absolute prefix through exponent \(a\)
needs \(a<4\delta\) for the stated summable heat-removal majorant.
The dominant tail power for pair \(j\) is
\[
 E_j(v)=v(g_j(v)-\delta),\qquad
 g_j(v)=k_j/v-(j+3)k_j+v/4 .
\]
With \(j=0\) alone, \(E_0(4\delta)=1/6-2\delta\); \(E_0\)
decreases up to \(1/2\). This payment requires \(y>2/3\) in
\(1/2<y\le3/4\). With \(j=2\) alone the cutoff power at
\(v=1/2\) is \(1/80\) when \(\delta=0\). Improving the small
blocks with larger \(j\) can lose the cutoff saving.

For the lower envelope of all pairs (3), let \(q=2^{j+2}\) and
\(v_j=q/((j+1)q+2)\) for \(j\ge1\).
The adjacent affine parts \(k_j-(j+3)k_jv\) cross at \(v_j\).
These crossings decrease strictly with \(j\), so adjacent
comparison places pair \(j\) on \([v_{j+1},v_j]\) and pair 0
on \([v_1,1/2]\). There \(g_j''(v)=2k_j/v^3>0\).
The values at the crossings are \(v_j/4-1/q\), strictly
decreasing for \(j\ge4\). The latter comparison reduces to
\(q-1>2(j+1+2/q)(j+2+1/q)\), checked at \(j=4\) and implied for
\(j\ge5\) by \(q-1\ge2(j+2)(j+3)\) by induction.
At \(v_1,v_2,v_3,1/2\) the values lie below the
\(v_4=32/161\) value \(351/10304\). Thus
\[
 \max_{0<v\le1/2}\min_{j\ge0}g_j(v)=351/10304,\qquad
 y_{\rm chain}=\tfrac12+2(351/10304)=2927/5152 .
\]
For each fixed \(y_0>y_{\rm chain}\), \(a=1/8<4\delta\)
and finitely many pairs (3) yield strict limiting powers that
survive sufficiently small clock drift. For \(1/2<y_0\le
y_{\rm chain}\), \(4\delta<v_4\), and the absolute-prefix,
separate \(A\)-chain dyadic payment lacks a negative power at
\(v_4\). The restriction is on this specific allowance. An
improved bound at the intermediate scale could use other pairs,
joint summation or a different heat-removal estimate. At the
limiting \(y=1/2\) the ordinary zeta tail and floor also need an
argument beyond uniform absolute convergence.

## 5. Collision-control premise screen

The premise screen applies [cluster12][r12] to (1)–(5).
The general exponent-pair estimate concerns its specified phases.
The canonical application also depends on the coefficients and provider.

| Control | Failed premise of this comparison |
| --- | --- |
| Euler-factor / translated heat controls and older counter-kernels | Complete unmodified theta source and its exact unit-coefficient RS arithmetic identifying the dominant arm with a finite portion of ordinary zeta |
| Weighted-square and nontrivial finite-source controls | Full coefficient sequence jointly with full source reflection, beyond square support and endpoint matches |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Exact canonical arithmetic square expansion needed for (1), despite reflection or matched primitive endpoints |
| Finite-prime orbit controls | Full reflection and coefficient matching beyond selected primes and prefix |
| Atomic fixed-event, exact finite-profile and compact continuous controls | Complete canonical source and coefficients beyond finitely matched observations |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic, with their RH hypothesis still conditional |
| Fixed amplitude with variable readout | Actual cosine oscillator and Newman equation needed by the field provider |
| Actual-profile relaxed positive measures | Integer zeros identified with the exact field, beyond a feasible finite-profile measure |

Reflection rigidity uses the full square support, reflection and
normalization hypotheses. If a comparison box contains a control's
zero and the comparison carrier is nonzero there, its relative
deviation at that point is 1 and the proposed \(1/16\) test fails.
The listed witnesses can lie outside the box and time curve.

[overview]: ../research-overview/01_GNP_BB_RESEARCH_OVERVIEW_20261113.md#separate-contour-and-observation-investigation
[start]: 01_GNP_BB_CONTINUATION_AND_PROMPT_20261113.md
[baseline]: 03_GNP_BB_B01_COLLAR_COMPARISON_20261113.md
[program]: 05_GNP_BB_ANALYTICAL_PROGRAM_AND_SELECTION_PROTOCOLS_20261113.md
[provider]: ../../manuscript/sections/10a_transition_green.tex
[hda]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[b08]: ../../01_riemann_siegel_evolution/notes/25_GNP_RS_B08_EXPONENT_PAIR_LOCALIZATION_20261112.md
[b10]: ../../01_riemann_siegel_evolution/notes/29_GNP_RS_B10_SIGNED_MELLIN_MEAN_ESTIMATE_20261112.md
[b10audit]: ../../01_riemann_siegel_evolution/notes/31_GNP_RS_B10_PREINTEGRATION_PROOF_AUDIT_20261112.md
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=44
[zseries]: https://dlmf.nist.gov/25.2.E1
[euler]: https://dlmf.nist.gov/25.2.E11
[poly]: https://arxiv.org/html/1904.12438v2#S3
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
