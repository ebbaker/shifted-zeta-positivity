# Finite reciprocal-energy part and a positive endpoint correction

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, confirmed from the root research turn metadata.

**Status: proved in-note, conditional on the existing ordinary-event
chart; not a theta collision exclusion.** The manuscript already proves
the coefficient of the logarithmic divergence. This note strengthens its
unspecified bounded remainder to an exact limit, a nonnegative coefficient
series, and effective finite-jet enclosures. On the source-controlled chart
the excess over the quadratic finite part is at most
`12 pi/(23^3 |A|)`. Both direct and boundary consumers may use this estimate.
No actual theta event or its event-conditioned constants are acquired.

Read the [result index][results] and [avoid index][avoid], especially
[collision controls][controls], [criterion classification][a01],
[scope][a07], [normalization][a08], [complete coupled estimates][a12],
and [gain before expansion][a20]. This is an applicable estimate for an
already defined integral, rather than a new simplicity criterion. Its
increment is the explicit bounded endpoint interval and its convergent
refinement, not a new equivalent formulation of RH.

## 1. Fixed chart and exact statement

Use the hypothetical ordinary event of [Note 01][n01] and manuscript
Section 6. Translate its spatial center to zero and write

\[
 F_\tau(z)=H(T+\tau,x_*+z),\qquad
 h(z)=F_0(z)=z^2g(z),\qquad A=g(0)\ne0.
\]

The spatial domain is the fixed disk `D_r={|z|<r}` from that chart, centered
at the event. There are exactly two simple real roots for `0<tau<=sigma`,

\[
 \alpha_\tau=m_\tau-a_\tau,\quad
 \beta_\tau=m_\tau+a_\tau,\quad a_\tau>0,
 \qquad
 F_\tau(z)=((z-m_\tau)^2-a_\tau^2)V_\tau(z).
\]

The established estimates give

\[
 m_\tau=O(\tau),\quad a_\tau^2\asymp\tau,
 \quad |V_\tau|\ge\nu=3|A|/4,
 \quad |V_\tau(m_\tau)-A|\le J\tau,
 \quad |(V_\tau^{-1/2})'|\le L.                    \tag{1}
\]

All constants here belong to this fixed event and disk. The limiting
unit `g` is nonvanishing on the closed disk. Choose its holomorphic
inverse square root coherently and expand

\[
 b(z)=g(z)^{-1/2}=\sum_{n\ge0}b_nz^n,
 \qquad |b_0|^2=|A|^{-1}.
\]

Define the complete two-sheet energy

\[
 \mathcal E_\tau=2\int_{D_r}\frac{dA_z}{|F_\tau(z)|}.
\]

**Theorem.** The following limit exists:

\[
 \boxed{\displaystyle
 \lim_{\tau\downarrow0}
 \left[\mathcal E_\tau-\frac{2\pi}{|A|}\log\frac1\tau\right]
 =\frac{4\pi}{|A|}\log(\sqrt2\,r)+Q_r,\qquad
 Q_r=2\pi\sum_{n\ge1}\frac{|b_n|^2r^{2n}}n.}       \tag{2}
\]

Equivalently,

\[
 \boxed{\displaystyle
 Q_r=2\int_{D_r}\left|\frac{b(z)-b_0}{z}\right|^2dA_z\ge0.}
                                                               \tag{3}
\]

The removable value at zero in (3) is `b_1`. Equality `Q_r=0` holds
exactly when `g` is constant on the disk. The phase choice of the square
root changes none of these quantities.

The circular domain and its center matter to the sign: the angular
orthogonality used below need not hold on an arbitrary spatial domain.
The theorem does not assign a finite energy to the singular fiber.

## 2. Root scale and limiting unit

First, the heat equation gives

\[
 F_\tau(0)=-2A\tau+O(\tau^2).
\]

This follows by integrating the time derivative once and using the
bounded fourth spatial derivative for the time Taylor remainder. The
manuscript's deflated-unit derivative bound `|V_tau'|<=M_3/6` gives

\[
 V_\tau(0)=A+O(\tau),
\]

because `V_tau(m_tau)=A+O(tau)` and `m_tau=O(tau)`. Evaluating the
factorization at zero therefore gives

\[
 (m_\tau^2-a_\tau^2)V_\tau(0)=-2A\tau+O(\tau^2),
 \qquad
 \boxed{a_\tau^2=2\tau+O(\tau^2).}                 \tag{4}
\]

There is no premise asserting this more precise root gap: it follows
from the event, heat equation and previously proved chart.

The divided-difference identity in the manuscript gives

\[
 V_\tau(z)=\int_{s,t\ge0,\ s+t\le1}
 F_\tau''\bigl(s\alpha_\tau+t\beta_\tau+(1-s-t)z\bigr)
 \,ds\,dt.                                           \tag{5}
\]

As `tau->0`, the integrands converge uniformly for `|z|<=r` to
`h''((1-s-t)z)`, since the derivatives are continuous on the common
compact chart and both roots tend to zero. Their integral is
`h[0,0,z]=g(z)`. Thus `V_tau->g` uniformly on the closed disk.
In particular `|g|>=nu`. Choose the square roots so their values at zero
converge. The common unit neighborhood and holomorphic continuation then
give uniform convergence

\[
 b_\tau:=V_\tau^{-1/2}\longrightarrow b.
\]

No quantitative convergence rate for this last assertion is needed.
The bounds `|b_tau|<=nu^(-1/2)` and `|b_tau'|<=L` remain uniform.

## 3. Convergence of the complete remainder

Let

\[
 \mathcal E_{0,\tau}=2\int_{D_r}
 \frac{dA_z}{|z-\alpha_\tau|\,|z-\beta_\tau|}.
\]

Subtract the full quadratic model, with no omitted branch caps:

\[
 R_\tau:=\mathcal E_\tau-|b_\tau(m_\tau)|^2\mathcal E_{0,\tau}
 =2\int_{D_r}
 \frac{|b_\tau(z)|^2-|b_\tau(m_\tau)|^2}
 {|z-\alpha_\tau|\,|z-\beta_\tau|}\,dA_z.             \tag{6}
\]

We verify uniform integrability at the merging pair, rather than
applying dominated convergence to a moving singular denominator. Fix
`0<epsilon<r`. For sufficiently small time, both roots lie in
`D_epsilon`. For any `gamma` in this disk, polar integration about
`gamma` and Cauchy--Schwarz give

\[
 \int_{D_\epsilon}\frac{dA_z}{|z-\gamma|}\le2\pi\epsilon.
\]

Also `|z-m_tau| <= (|z-alpha_tau|+|z-beta_tau|)/2`. Consequently,

\[
 \int_{D_\epsilon}
 \frac{|z-m_\tau|}{|z-\alpha_\tau|\,|z-\beta_\tau|}\,dA_z
 \le2\pi\epsilon.                                    \tag{7}
\]

The straight segment from `m_tau` to `z` stays in the original disk,
so (1) gives

\[
 \bigl||b_\tau(z)|^2-|b_\tau(m_\tau)|^2\bigr|
 \le2\nu^{-1/2}L|z-m_\tau|.
\]

Thus the absolute contribution of `D_epsilon` to (6) is at most
`8 pi nu^(-1/2)L epsilon`, uniformly for sufficiently small time.
The limiting numerator has the same linear vanishing at zero, so its
corresponding limiting integral over `D_epsilon` obeys the same bound.
On the closed annulus `epsilon<=|z|<=r`, numerator and denominator
converge uniformly, and the denominator stays bounded away from zero.
First take the time limit on that annulus and then let `epsilon->0`.
This proves

\[
 R_\tau\longrightarrow
 2\int_{D_r}\frac{|b(z)|^2-|b_0|^2}{|z|^2}\,dA_z.
                                                               \tag{8}
\]

The mixed term in the numerator is retained. To evaluate it, expand

\[
 |b|^2-|b_0|^2
 =2\operatorname{Re}\bigl(\overline{b_0}(b-b_0)\bigr)
   +|b-b_0|^2.
\]

For each centered circle, the angular average of `b-b_0` is exactly
zero. Its mixed integral against the radial weight `|z|^(-2)` is
therefore zero. This cancellation is justified by absolute integrability
near zero, already proved. The remaining term gives (3). Orthogonality
of the Taylor monomials on each circle and radial integration give

\[
 2\int_{D_r}\frac{|b-b_0|^2}{|z|^2}\,dA_z
 =4\pi\sum_{n\ge1}|b_n|^2\int_0^r\rho^{2n-1}\,d\rho
 =2\pi\sum_{n\ge1}\frac{|b_n|^2r^{2n}}n.
\]

One may first integrate over a smaller disk and pass to `r` by
monotone convergence. This proves the series formula without discarding
or separately overestimating a mixed contribution.

## 4. The logarithmic constant

The complete quadratic energy on a centered radius-`R` disk obeys

\[
 \mathcal E_0(a;D_R)=4\pi\log(2R/a)+O(a^2/R^2).
\]

The disk centered at `m_tau` with radius `r-|m_tau|` is contained in
`D_r`, which in turn is contained in the disk centered at `m_tau` with
radius `r+|m_tau|`. Applying the quadratic bounds to these two disks
therefore yields

\[
 \mathcal E_{0,\tau}=4\pi\log(2r/a_\tau)+o(1)
 =2\pi\log(1/\tau)+4\pi\log(\sqrt2\,r)+o(1),          \tag{9}
\]

where (4) fixes the constant `sqrt(2)`. By (1),

\[
 \left||b_\tau(m_\tau)|^2-|A|^{-1}\right|
 \le\frac{J\tau}{|A|\nu}.
\]

Multiplying this by the `O(log(1/tau))` quadratic energy gives an
error tending to zero. Equations (6), (8), and (9) prove (2), with the
factor two for both sheets retained throughout.

For the exact quadratic heat control `F_tau=A(z^2-2tau)`, all
`b_n` with `n>=1` vanish. The formula reduces to its exact quadratic
finite part, providing a normalization check rather than an exclusion.

## 5. Explicit finite-jet enclosures

Write `s_n=|b_n|^2 r^(2n)` for `n>=1`. Any established bound

\[
 \sum_{n\ge1}s_n\le U_b                                      \tag{10}
\]

gives a finite complete enclosure, for every integer `N>=0`:

\[
 \boxed{\displaystyle
 2\pi\sum_{n=1}^N\frac{s_n}{n}
 \le Q_r\le
 2\pi\sum_{n=1}^N\frac{s_n}{n}
 +\frac{2\pi}{N+1}\left(U_b-\sum_{n=1}^Ns_n\right).}   \tag{11}
\]

Indeed the omitted weights are at most `1/(N+1)`. The bracket is
nonnegative under (10). A general unit floor gives, by Parseval on the
boundary circle,

\[
 U_b=\nu^{-1}-|A|^{-1}.
\]

A bound on `|b-b_0|` gives a sharper choice. In the event chart,
Taylor's theorem for `h` gives

\[
 |g(z)-A|\le\delta:=M_3r/6\le |A|/24,
 \qquad \nu_0:=|A|-\delta>0.                            \tag{12}
\]

Integrate the derivative of `w^(-1/2)` along the segment from `A` to
`g(z)`; that segment stays in the radius-`delta` disk about `A`, where
a coherent branch exists. It gives

\[
 |b(z)-b_0|\le\frac{\delta}{2\nu_0^{3/2}},
 \qquad
 U_b=\frac{\delta^2}{4\nu_0^3}.                         \tag{13}
\]

Parseval for `b-b_0` proves (10) for this choice. In particular,

\[
 \boxed{\displaystyle
 0\le Q_r\le\frac{\pi\delta^2}{2\nu_0^3}
 \le\frac{12\pi}{23^3|A|}.}                            \tag{14}
\]

The last inequality uses `delta<=|A|/24` and
`nu_0>=23|A|/24`. It is a quantitative refinement of the manuscript's
unspecified bounded endpoint remainder. It controls the excess over the
quadratic finite part on this deliberately small source-controlled disk;
it is not a bound for the divergent unrenormalized energy.

The coefficients can be obtained from the endpoint source jet:

\[
 g(z)=\sum_{k\ge0}\frac{h^{(k+2)}(0)}{(k+2)!}z^k,
 \qquad g(z)b(z)^2=1.
\]

The latter identity recursively determines every `b_n` after choosing
`b_0`. For example

\[
 b_1=-\frac{h'''(0)}{12A^{3/2}},\qquad
 Q_r\ge\frac{\pi|h'''(0)|^2r^2}{72|A|^3}.             \tag{15}
\]

The branch convention in `A^(3/2)` is the one matching `b_0`; its
modulus in the lower bound is unambiguous. A vanishing cubic jet does
not imply a vanishing correction: later coefficients must be retained.

For acquired coefficient intervals `s_n in [ell_n,u_n]`, with all
rounding, event, source-tail, and radius uncertainty included, one safe
enclosure is

\[
 2\pi\sum_{n=1}^N\frac{\ell_n}{n}\le Q_r\le
 2\pi\left[\frac{U_b}{N+1}
 +\sum_{n=1}^Nu_n\left(\frac1n-\frac1{N+1}\right)\right],
                                                               \tag{16}
\]

where `U_b` is replaced by a certified upper bound if uncertain.
The upper formula follows by rewriting (11), avoiding any subtraction
of uncertain tail mass. The exact-data tail is `O(U_b/N)`; coefficient
intervals must also be refined if a vanishing final width is required.
No coefficient acquisition or numerical run is claimed here.

## 6. Canonical strictness and the precision limitation

For a hypothetical canonical theta event, `Q_r>0` at every fixed
positive chart radius. Otherwise (3) would force `b` and then `g` to be
constant; hence `H(T,x_*+z)=Az^2` on a disk and, by analytic continuation,
on the entire plane. Thus `H(T,z)=A(z-x_*)^2`. The canonical cosine
transform is even in `z`; because `A` is nonzero this polynomial can be
even only if `x_*=0`. But the unchanged complete half-line source is
strictly positive, so

\[
 H(T,0)=\int_0^\infty e^{Tu^2}\Phi(u)\,du>0,
\]

contradicting the polynomial's zero at zero. The complete moment bounds
in the manuscript justify this finite positive integral. This proves
strictness, but gives **no positive
floor uniform in the event, height, or chart radius**. In particular the
correction tends to zero as the disk radius tends to zero. Its strict
sign is compatible with a collision and is not an opposing estimate.

There is also a numerical precision distinction. If the coefficient
`C=2 pi/|A|` of `log(1/tau)` is enclosed separately with fixed nonzero
width `Delta C`, the separately subtracted energy interval generally
carries uncertainty `Delta C log(1/tau)`. Exact bounded remainders do
not remove that cost. To obtain bounded uncertainty by this subtraction
requires `Delta C=O(1/log(1/tau))`; convergence to an exact finite part
requires the stronger `Delta C=o(1/log(1/tau))`, or a separately paid
correlated-product estimate. This statement concerns separate interval
payment, not an impossibility theorem for correlated acquisition. The
same issue appears as `|p| epsilon_q` in the period product of
[Note 03][n03]. Formula (16) estimates the endpoint finite part directly,
without pretending that a fixed-precision subtraction at arbitrarily
small time has acquired it accurately.

## 7. Controls, sibling comparison, and remaining obstacle

The exact quadratic heat family has `Q_r=0` and still collides. A
nonconstant analytic-unit heat control can have `Q_r>0` and still
collide. Neighboring-root controls retain the same local finite-part
mechanism. Thus neither nonnegativity nor canonical strict positivity
contradicts ordinary-double degeneration. The energy itself remains

\[
 \mathcal E_\tau=\frac{2\pi}{|A|}\log(1/\tau)
 +\frac{4\pi}{|A|}\log(\sqrt2 r)+Q_r+o(1).
\]

Euler-factor controls change the canonical arithmetic source;
weighted-square and finite-prime controls fail unchanged complete
coefficients and the complete normalized reflection conjunction;
reflected/primitive controls fail the unchanged square-index coefficient
sequence. Their preservation lists are separate, as in [cluster 12][controls].
None of those missing literal theta premises is used in Sections 1--5
to reject a collision. Section 6 uses canonical evenness and complete
source positivity only to rule out exact local quadraticity, not to
exclude a multiple zero.

The sibling [BW10 Note 12, Section 3][bw12] already computes finite
parts of **root-interaction and kinetic energies**, retaining exterior
forcing. The [RHE manuscript][manuscript] already proves the leading
logarithm of the **spatial reciprocal energy** treated here. Neither
fact is claimed new. Equations (2), (11), and (14) give the additional
finite spatial-energy constant and effective signed interval. They
supply no new excluded height, multiplicity class, or RH threshold.

The useful stopping point is an explicit convergent endpoint estimator
and a small source-controlled excess bound. A theta estimate opposing
the allowed logarithmic divergence, and coverage beyond ordinary real
doubles, remain open. No manuscript expansion or broad numerical
campaign is needed to record this increment.

[n01]: 01_FINITE_COVER_CONTRACT_AND_ENERGY_ENCLOSURE_20261022.md
[n03]: 03_REAL_PRIMITIVE_REDUCTION_AND_BOUNDED_MODEL_REMAINDER_20261022.md
[manuscript]: ../manuscript/reciprocal_hodge_energy/main.tex
[bw12]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
