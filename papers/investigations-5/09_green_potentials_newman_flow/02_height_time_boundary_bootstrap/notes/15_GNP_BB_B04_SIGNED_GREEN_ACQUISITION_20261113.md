# B04: a signed Green acquisition on a fixed-depth collar

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, **gpt-6.1-sol / ultra** by explicit
tool selection. **Status: conditional consumer and exact reduction to
one unpaid canonical local quadratic estimate.** This is the bounded
Green comparison for [B04 r1][packet]. The comparison uses the actual theta
field at \(t_X=1/L_X\), \(L_X=\log(X/(4\pi))\), and a fixed target below
\(\gamma=2927/5152\). Each spatial integral holds its time fixed.
[Result index][results], [avoid index][avoid], [classification01][a01],
[premises02][a02], [scope07][a07].

## Common target, observation and complete contour

Use the same benchmark \(y_*=567/1000\) as the broader finite-pair route.
The existing [E03 proof][e03] supplies an initial upper width
\(a=73/128>\gamma\) for every sufficiently large real \(X\). Let
\[
 \ell=17/32,\quad u=39/64,\quad b=37/64,\quad H=u-\ell=5/64,\quad
 p=X+ib,\quad W=(3H/\pi)\log X,
 \qquad D_X=\{|\Re z-X|<W,\ \ell<\Im z<u\}.
\]
The benchmark target \([y_*,a]\) on the centerline lies inside
\(K_X=\{X+iy: 9/16\le y\le a\}\). This larger target would yield the
conditional width \(9/16\). The disk centered at \(X+ia\) of radius
\(5/128\) lies in the rectangle once \(W\ge5/128\). In units \(1/128\)
the observation and deepest target have disk coordinates \(+1,-1\).
The disk Green formula and domain monotonicity give
\[
 g_K:=\inf_{z\in K_X}G_{D_X}(p,z)\ge \log(13/5).
\]
The minimum in the disk occurs at the deepest point, by monotonicity
of the Green kernel on the diameter below the observation.
The local domains cover every real center and have four boundary
edges. [Geometry Note08][geometry].

Set \(F=H_{t_X}/(C_-\zeta(s_{t_X}))\) with the exact carrier and
argument of [E01][e01]. On \(|x-X|\le W\), \(c_x=t_XL_x\) differs
from 1 by \(O(W/(XL_X))\). Recenter each fixed \((1,9)\) HDA
chart at the evaluated coordinate \(x=\Re z\). The provider's
time restriction, cutoff and full remainder still hold with a
finite onset, as in E01–E03. Since
\(\Re L(z)\ge L_x\) and \(y\ge17/32\),
\[
 \Re s_{t_X}(z)\ge65/64-1/40000>1+1/65
\]
once \(|c_x-1|\le 10^{-4}\). The ordinary Euler product then gives
\(|1/\zeta(s_{t_X})|\le66\) on the full closed rectangle.
The analytic denominator is nonzero on a neighborhood of it.
The [E03 estimate][e03] at lower edge \(4/7\) pays a separate
observation floor \(|F(p)|\ge15/16\) and \(F=1+o(1)\) uniformly on the
top edge. This uses its proof with the very same constants for the
\(c_x\) drift, recentered charts, and cutoff at each \(x\); the only new
gate is \(W<X/2\) and \(2W/(XL_X)\le
\min(10^{-4},(4/7-\gamma)/16)\). The estimate is nowhere required at
or below the benchmark target.

## Complete signed consumer from a local quadratic bound

Harmonic normalization cancels \(\log|C_-\zeta(s_{t_X})|\).
Let \(d\omega=d\omega_{D_X}^p\) be the probability harmonic measure.
For analytic \(F\) on this domain, including near its boundary,
\[
 \sum_{z_j\in D_X}m_jG_{D_X}(p,z_j)
 \le \tfrac12\log\!\left(1+
 \frac{\int_{\partial D_X}|F-1|^2\,d\omega-|F(p)-1|^2}{|F(p)|^2}\right).
                                                               \tag{1}
\]
Indeed \(\int F\,d\omega=F(p)\) cancels the linear term exactly on
expanding \(|F|^2\) around the constant 1. For the log bound one
can map the disk conformally onto the rectangle taking its origin
to \(p\), apply Jensen and the concavity inequality
\(\int\log|F|\le\tfrac12\log\int|F|^2\) on the inner circles,
and pass to radius 1. The rectangle has a Jordan boundary, the
continuous boundary \(|F|^2\) permits dominated convergence,
and the interior zero contributions increase to the Green sum.
This proof covers possible boundary zeros without assuming an
inner-boundary logarithmic floor. Boundary and observation costs
enter (1) with their actual measures.

With \(|F(p)|\ge15/16\), (1) gives a strict Green margin if
\(\int|F-1|^2d\omega\le9/2\), since
\((15/16)^2((13/5)^2-1)=81/16>9/2\).
On the same domain and with this floor, a small uniform error
would imply this quadratic bound. The converse fails for analytic
functions. For example, on the unit disk with central observation,
\(1+2((1+z)/2)^m\) has supremum error 2 and boundary quadratic
error tending to zero by dominated convergence. This comparison
concerns the norm data on the same domain. The broader finite-pair
proof only needs its own narrower direct-exclusion domain.
Equation (1) supplies a finite positive-time milestone conditional
on a separately specified arithmetic estimate, rather than a
hypothesis identifying an unknown Green defect with a zero count.

The side mass is \(O(e^{-\pi W/(2H)})=O(X^{-3/2})\), by the
\(\cosh\times\cos\) barrier in [Note08][geometry]. The crude finite
provider bound \(|H_{t_X}/C_-|\ll X^{1/4}\) holds there by the
nonnegative heat suppression of each finite weight, the
subdominant carrier, the correction and full remainder. This is
the positive population bound of [E05 §2][e05] with the stated
fixed chart and bounded \(c_x\). The reciprocal bound therefore
makes the complete side quadratic payment \(O(X^{-1})\).
The top edge costs \(o(1)\) by the paid comparison above. On the
bottom, the harmonic measure of the finite rectangle is dominated
by the following Poisson kernel of the containing strip, evaluated
at its same observation \(p\):
\[
 P(v)=\frac{\sin(\pi(b-\ell)/H)}
 {2H[\cosh(\pi v/H)-\cos(\pi(b-\ell)/H)]},\qquad
 \int_{\mathbb R}P(v)\,dv=2/5 .
\]
For this domination, extend a nonnegative continuous bottom test
function by zero on the rest of the strip boundary. Its nonnegative
harmonic extension in the strip dominates the rectangle extension
by the maximum principle. Approximation gives the inequality for
the quadratic data on the whole bottom segment.

## The single new estimate

Put \(K=\lfloor e^{L_X/32}\rfloor\), \(N=\lfloor e^{L_X/2}\rfloor\),
\(\tau_X=X/2+\pi/(8L_X)\), and define
\[
 w_n=n^{-65/64}\exp((\log n)^2/(4L_X)),\qquad
 T_X(v)=\sum_{K<n\le N} w_n e^{i(\tau_X+v/2)\log n}.
\]
A sufficient target, still unpaid, is
\[
 \boxed{\ \int_{\mathbb R}P(v)|T_X(v)|^2\,dv\le4/66^2
                       \quad\text{for every sufficiently large real }X.\ }  \tag{2}
\]
The following reduction uses the complete canonical field. On the
bottom segment the finite head \(n\le K\) costs \(O(1/L_X)\)
to remove the heat weight, since its weighted summability exponent
is at least \(65/64-1/40000-1/128>1+1/256\).
The ordinary zeta series beyond \(K\) costs \(O(X^{-1/2080})\).
The full reflected arm still decays by \((1/6,2/3)\) and the
proof of [E02][e02], with primary block endpoints
\(-19/192\) and \(-11/384\) at \(c_x=1,y=17/32\).
The latter loses at most \(1/160000\) under the drift gate.
Both are below \(-1/48\); its inverse derivative term is
\(O(X^{-1/2})\) per dyad. The correction costs
\(O(X^{-(1+\ell)/4})\), the full provider remainder
\(O(X^{-3/4})(1+O(X^{-\ell/2}))\).
Every term besides the dominant tail is thus uniformly \(o(1)\).

At \(x=X+v\), the actual cutoff \(N_x\) differs from \(N\)
by at most one when \(|v|\le W\), by the derivative of the
square-root real scale. The added or omitted term has size
\(O(X^{-57/128})\). For common terms the exact bottom summand is
the corresponding summand of \(T_X\) times
\(\exp(-t_X(L(x+i\ell)-L_X)\log n/4)\).
Its difference from the frozen summand has relative magnitude
\(O(W/X)\), since \(|L(x+i\ell)-L_X|=O(W/X)\) and
\(t_X\log n=O(1)\). Summing this over all modes costs
\(O((W/X)X^{1/4})=o(1)\), using the positive population bound
or the elementary bound \(w_n\le n^{-57/64}\).
No floor is differentiated, and no infinite heat-weighted arm
is introduced. Thus uniformly for \(|v|\le W\),
\[
 F(X+v+i\ell)-1=
 \frac{T_X(v)+o(1)}{\zeta(s_{t_X}(X+v+i\ell))}.
\]
With (2), Poisson domination and the triangle inequality for the
weighted quadratic norm give bottom payment
\(66^2(\sqrt{4/66^2}+o(1))^2=4+o(1)\).
Together with the top and both sides this pays (1) beyond a finite
onset. The Green test excludes the closed target \(K_X\).
Combining with E03's initial width \(a\) and conjugation gives
\(|y|<9/16\) along the curve, and hence the common
\(567/1000\) target. Neither width is claimed here from (2)
without its proof.

## Exact signed estimator and the B10 limit

The normalized strip kernel has Fourier transform
\(\widehat P(\omega)=\sinh((u-b)|\omega|)/\sinh(H|\omega|)\)
in the convention \(\widehat P(\omega)=\int P(v)e^{i\omega v}dv\),
with value \(2/5\) at zero. To see this, solve the harmonic
extension of the bounded bottom datum \(e^{i\omega v}\) with
zero top datum by separation of variables, and use the
strip harmonic measure. The exact left side of (2) is
\[
 \frac25\sum_{K<n\le N} w_n^2+
 2\Re\sum_{K<m<n\le N}w_mw_n
   e^{i\tau_X\log(n/m)}
   \frac{\sinh((u-b)\log(n/m)/2)}
        {\sinh(H\log(n/m)/2)}.                                  \tag{3}
\]
The diagonal is \(O(K^{-25/32})\) since
\(w_n^2\le n^{-57/32}\). Thus an upper bound on this signed sum,
including near-equal indices, is the remaining estimation task.
A separate absolute bound on the summands cannot establish a
uniform constant. For \(N/2<m<n\le N\), every weight is comparable
to \(X^{-57/128}\) and the kernel multiplier is bounded below by
a positive constant (continuity on \([0,\log 2/2]\)).
The absolute allowance from those pairs alone grows at least
as \(X^{7/64}\). This is a statement about the termwise
absolute allowance for (3).

The [B10 proof][b10], [audit][audit] and [internal assessment][review]
establish a signed correlation bound consumed by a residual
**center-average** on intervals of length
\(\mathcal L\ge U^{17/81+\rho}\), for fixed
\(0<\rho\le47/162\), \(\mathcal L\le U\), and block-constant
prime cutoff \(2\le P_U\le\lfloor L_U^2\rfloor\).
The inner physical integration uses the original fixed strip,
offset and \(c=1\) setup with the time frozen in each calculation;
the Mellin translations act on an auxiliary zeta variable.
The inherited signed log transfer with growing cutoff gives a
Green mean \(O_\rho(L_U^{-1/3})\), and a fixed-threshold
exceptional proportion \(O_{h,\rho}(L_U^{-1})\).
The upper bound on total Green mass is
\(O_\rho(\mathcal L L_U^{-1/3})\). It grows with the admissible
height-window scales and allows fixed-width contributions of
constant size. Even bounds on every interval of these lengths
would allow a bounded bump of width one and fixed amplitude.
B10's source estimate retains the \(R^{19/60}\) error in
translated mean-square integrals; it has no bounded short-window
replacement at the new \(O(1)\) Poisson scale. Original offsets,
kernel and signed correlation also differ from (3).
The original upper observation is independently estimated in
the B10 consumer. Its mean conveys no lower floor at a changed
observation, since even the exact Green defect is invariant under
multiplying the field by a nonzero constant. Our lower floor comes
from E03 at the actual observation and time.

**Decision for this alternative.** The geometric and other
field payments identify (2), or a directly acquired complete
signed logarithmic cap below the same explicit Green margin,
as a genuinely different acquisition. The critical term in (3)
is the actual local signed correlation on the physical height
trajectory, with the stated weights and cutoff. Existing
averages and absolute pair allowances leave it unpaid.
The broader finite-pair estimate at the common benchmark can
therefore proceed independently. This note does not acquire
an every-center arithmetic estimate, a common-time extension,
a compact-height bound or iteration.

## Collision-control screen

The Green consumer is generic. With an independently nonzero
carrier, any control having a zero in the target would violate
the strict combined margin whenever its contour and observation
satisfy the hypotheses. A disjoint collision-free box may
pass. The proposed estimator uses the following specifically
canonical premises. [Collision controls12][controls],
[B10 screen][b10], [E01 screen][e01].

| Control | Failed premise of the canonical reduction |
| --- | --- |
| Euler-factor and translated sources, older heat counter-kernels | Unchanged ordinary Dirichlet coefficients and the canonical complete two-arm provider |
| Weighted-square and finite-tail sources | Full unit coefficient sequence together with full reflection |
| Reflected super-Gaussian, smooth shape and primitive-compatible sources | Exact normalized theta square arithmetic |
| Finite-prime orbit | Full coefficients and reflection beyond the selected primes and prefix |
| Atomic, finite-profile and compact continuous controls | Full canonical source, coefficients and profile beyond matched observations |
| RH-conditional normalized endpoint | Ordinary zeta Dirichlet arithmetic |
| Fixed-amplitude variable readout | Actual cosine heat field |
| Relaxed measures and free or calibrated phase variables | The actual integer zero divisor or the exact common physical phase in (3), respectively |

The screen does not imply that a control fails an analogous mean,
or that an all-source logarithmic upper bound is impossible. For
reflection rigidity the full conjunction of source assumptions
is retained.

[packet]: ../research-progress/handoffs/GNP-BB-B04-r1.md
[geometry]: 08_GNP_BB_B02_GEOMETRY_AND_OBSERVATION_20261113.md
[e01]: 06_GNP_BB_E01_COMPLETE_OUTER_ESTIMATE_20261113.md
[e02]: 09_GNP_BB_E02_SIGNED_TAIL_WIDTH_20261113.md
[e03]: 10_GNP_BB_E03_ENVELOPE_ENDPOINT_AND_WIDTH_20261113.md
[e05]: 12_GNP_BB_E05_COMMON_TIME_TAIL_20261113.md
[b10]: ../../01_riemann_siegel_evolution/notes/29_GNP_RS_B10_SIGNED_MELLIN_MEAN_ESTIMATE_20261112.md
[audit]: ../../01_riemann_siegel_evolution/notes/31_GNP_RS_B10_PREINTEGRATION_PROOF_AUDIT_20261112.md
[review]: ../../01_riemann_siegel_evolution/reviews/16_GNP_RS_B10_PREINTEGRATION_ASSESSMENT_20261112.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
