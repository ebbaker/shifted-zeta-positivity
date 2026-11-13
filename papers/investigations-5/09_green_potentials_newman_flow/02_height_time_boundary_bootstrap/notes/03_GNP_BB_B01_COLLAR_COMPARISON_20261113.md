# B01: one outer-layer step and the estimate that can pay it

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and effort are
unavailable in branch chat0001's recorded configurations.

**Status: bounded conceptual decision, coefficient feasibility analysis,
and proved conditional geometric implications; same-assistant checking.**
The canonical comparison estimate is an **E01 proof target**, not a
completed zero-enclosure theorem. No numerical field run was performed.
See the [decision][decision], [assessment][review] and [frozen request][packet].

Read the [result index][results] and [avoid index][avoid], particularly
[heat-flow cluster11][r11], [controls12][r12], [classification01][a01],
[premise02][a02] and [scope07][a07]. The finite positive-time width gain
below is a quantitative milestone target, not an RH equivalence. The
comparison function is explicitly known and independently nonzero on
the chosen domain; it is not defined through unknown theta zeros.

## 1. Freeze one domain and one gain

Keep the complete theta field, H_0(z)=ξ((1−iz)/2)/8 and
∂_λH=−H_zz. Take X∈[U,2U], every sufficiently large U, and

\[
 L_X=\log(X/(4\pi)),\quad \lambda_X=L_X^{-1},\quad
 a_X=\sqrt{1-2/L_X},\quad b_X=a_X+1/16.                 \tag{1}
\]

At each center, hold λ=λ_X fixed throughout all complex/spatial
calculations. This is one prescribed time curve, not a time slab.
The initial **global** enclosure |Im z|≤a_X at that time follows
from the time-zero strip and [Polymath v2, Theorem 3.2][poly].
Require L_X≥64, hence a_X≥31/32. The proposed improvement is

\[
 H_{\lambda_X}(X+iy)=0\quad\Longrightarrow\quad
 |y|\le a_X-1/16.                                    \tag{2}
\]

It has observation buffer η=1/16 and segment length h=1/8.
It is a statement at every center of the curve. It does not assert
a narrower global strip at one fixed time, cover finite heights,
or improve a bound for Λ. Conjugation covers the lower half-plane.

Use the rectangle and compact target

\[
 D_X=\{z:|\Re z-X|<1,\ 7/8<\Im z<9/8\},\quad
 K_X=\{X+iy:a_X-1/16\le y\le a_X\},\quad p_X=X+ib_X.
                                                               \tag{3}
\]

There is no curved-contour approximation. All four rectangle edges
are part of the Green comparison. For the field route, radius 1/32
disks about the whole inward segment lie in D_X: its lowest disk
height is a_X−3/32≥7/8, with strict slack for L_X≥64, and its highest
is at most 35/32<9/8.

## 2. Choose an independently nonzero analytic normalization

Use the elementary C_− of the [parent transition section][outer],
not an unidentified gamma normalization. With L(z)=Log(z/(4π)),

\[
 \mathcal A=\frac{\pi^{1/4}}{16}z^{7/4}
 e^{-\pi z/8+\lambda(L(z)^2-\pi^2/4)/16},\quad
 \Theta=\frac z4(L(z)-1)+\frac{\pi\lambda L(z)}{16}+\frac{7\pi}8,
 \quad C_-=\tfrac12\mathcal A e^{-i\Theta},
\]
\[
 s_\lambda(z)=\frac{1-iz}{2}+\frac{\lambda L(z)}4
                  -\frac{i\pi\lambda}8,\quad
 Z_\lambda(z)=\zeta(s_\lambda(z)),\quad
 V_\lambda=H_\lambda/C_-,\quad F_\lambda=V_\lambda/Z_\lambda.
                                                               \tag{4}
\]

On the whole closed rectangle, put x=Re z and c_x=λ_X L_x.
The eventual gate 7/8≤c_x≤9/8 gives

\[
 \Re s_\lambda(z)\ge15/16+7/32=37/32>9/8.
                                                               \tag{5}
\]

Thus Z is analytic and nonzero there, without RH or a theta field
floor. From the ordinary [Euler product][euler],
|1/ζ(s)|≤∏_p(1+p^(−σ))≤ζ(σ)≤1+1/(σ−1)≤9 for σ≥9/8.
The carrier C_−Z is consequently analytic and nonzero on a
neighborhood of the closed rectangle. Its log modulus has zero
complete-boundary Green defect there. No global zero-free claim
for Z, or pole removal on the old strip 0<y<8, is made.

The selected arithmetic target is

\[
 \boxed{\sup_{\overline D_X}|F_{\lambda_X}-1|\le1/16.}   \tag{6}
\]

Unlike assuming nonvanishing of H, (6) has a prescribed approximant
and the convergent error payments below. Nevertheless (6) is still
unproved for the canonical field at this B01 return. An E01 result
must acquire those payments, not merely assume (6).

## 3. Why the complete finite-arm estimate is tractable here

The inherited [HDA Note04, CS6][hda] supplies the complete field on
fixed charts, with [its existing internal assessment][hreview]. Use
the already consumed r=1,b=9 charts, retaining all enlarged Gaussian
buffers and onsets. For each x recenter a chart and freeze
N_x=⌊√(x/(4π))⌋ there. Differentiate only the exact F, never this
piecewise cutoff formula. The parent gives

\[
 V_\lambda=D_N+R_N+Q_N+E_N,
\]
\[
 D_N=\sum_{n\le N_x}n^{-s_\lambda(z)}e^{\lambda(\log n)^2/4},
\quad
 R_N=e^{2i\Theta}\sum_{n\le N_x}w_n e^{-i\nu\log n},
\quad
 w_n=n^{-1/2}e^{\lambda[(\log n)^2-L(z)\log n]/4},
\quad\nu=z/2+\pi\lambda/8.                              \tag{7}
\]

Here Q_N is the retained corrected RS term divided by C_−;
E_N is the remaining full-field error. They are paid separately.
These formulas and their provider hypotheses, not the old b=4
conclusion, are reused. The published numerical constants of
Polymath Theorem 1.3 do not cover y=9/8.

For n≤N_x, log n≤L_x/2≤Re L(z)/2. Hence

\[
 |n^{-s_\lambda(z)}e^{\lambda(\log n)^2/4}|
 \le n^{-(1+y)/2-c_x/8}\le n^{-67/64}\le n^{-33/32}.     \tag{8}
\]

Write S_2=Σ_{n≥2}n^(−33/32)(log n)^2<∞. The inequality
e^v−1≤ve^v pays removal of the heat weight by S_2/(4L_X).
The omitted **ordinary** zeta series costs at most 8N_x^(−1/8),
using (5). No infinite heat-weighted Dirichlet series is introduced.

The full reflected arm must use the same heat gain. With the inherited
carrier bound |e^(2iΘ)|≤C x^(−y/2), its absolute finite sum satisfies

\[
 |R_N|\le Cx^{-y/2}\sum_{n\le N_x}n^{(y-1)/2-c_x/8}
 \le C' x^{(1-y)/4-c_x/16}\le C' x^{-3/128}.            \tag{9}
\]

The sum's exponent ranges over a fixed compact subset of (−1,∞),
so its integral-test constant is uniform. In contrast, the old
coarser O(x^((1−y)/4)) allowance does not decay here. This is the
consequential estimating choice: retain the heat suppression in the
entire reflected population.

The parent's correction and field payments give the following
feasibility ledger. Constants depend only on fixed chart/provider
data, not on U, X, or a fractional cutoff.

| Contribution to the modulus of V−Z | Payment to be assembled in E01 |
| --- | --- |
| Dominant-arm heat weight | S_2/(4L_X) |
| Ordinary series tail | 8N_x^(−1/8), hence O(x^(−1/16)) |
| Complete reflected population | O(x^(−3/128)) by (9) |
| Corrected RS term Q_N | O(x^(−(1+y)/4)), at most O(x^(−15/32)) |
| Provider error E_N | O(x^(−3/4))(1+O(x^(−y/2))) |
| Shifted argument and clock | Exact s_λ(z) retained; λ_X frozen, so no replacement error |
| Derivative | Cauchy on exact F−1 after the uniform value payment; no extra field derivative assumption |
| Source/Gaussian tails | Already paid by the inherited fixed-buffer provider, whose full hypotheses remain |

Thus a concrete E01 target is finite constants A,B and an explicit
finite list of eventual gates giving

\[
 \sup_{\overline D_X}|V_{\lambda_X}-Z_{\lambda_X}|
 \le A/L_X+B(X-1)^{-3/128},\quad
 9[A/L_X+B(X-1)^{-3/128}]\le1/16.                       \tag{10}
\]

This analysis identifies convergent terms, not an evaluated onset or
an accepted full proof of (10). E01 must justify uniform carrier and
correction constants, all chart overlap/cutoff gates and the reduction
of the ledger to (10). It may leave the inherited finite constants
symbolic and state the resulting onset inequalities.

## 4. Both consumers, using exactly the same data

**Normalized-field extension, conditional on (6).** At p_X take
m=1/2, since |F(p_X)|≥15/16. [Cauchy's derivative formula][cauchy]
on the full radius 1/32 disks gives |F'|≤32/16=2=M.
Thus h=m/(2M)=1/8>η=1/16, with retained floor m/2=1/4.
The new layer through a_X−1/16 is nonzero. Combining with the
initial enclosure proves (2), conditional on acquiring (6).

**Complete Green comparison, conditional on (6).** Normalizing by
C_−Z cancels its harmonic contribution on D_X. All four boundary
edges have log|F|≤log(17/16), while log|F(p_X)|≥log(15/16).
Harmonic measure has total mass one, giving the complete allowance

\[
 J_{D_X}(p_X)\le\log(17/15).                            \tag{11}
\]

No side is dropped. No quadrature, spatial exterior, or contour-shape
error occurs in this bounded exact comparison. The provider's source
tails still belong to (10).

For an explicit target margin, the disk of radius R=1/8 centered
at X+i is contained in D_X. Put u=b_X−1 and v=y−1 for y in K_X;
u/R∈[1/4,1/2], d=u−v∈[R/2,R]. The disk Green formula is

\[
 G_{\rm disk}(p_X,X+iy)
 =\log\frac{R^2-uv}{Rd}
 =\log\left[\frac uR+\left(1-\frac{u^2}{R^2}\right)\frac Rd\right]
 \ge\log(19/16).                                      \tag{12}
\]

The formula follows directly from its logarithmic pole, harmonicity
elsewhere and zero circle boundary values. Domain monotonicity
(maximum principle after canceling the pole) gives G_D≥G_disk.
Since 17·16=272<285=19·15, (11) is strictly below (12).
It excludes K_X, with no boundary-zero ambiguity because (6) itself
supplies a full boundary floor.

**Decision.** Select the normalized-field acquisition. With these
same data, (6) already proves F≠0 throughout the rectangle by the
triangle inequality; the derivative and Green calculations are
consistent consumers, not extra arithmetic gains. Rouché with the
constant approximant 1 would be another check of these same data,
not a third search. The useful research task is the complete estimate
(10). B10's averaged residual supplies neither (10) nor a pointwise
bound (11). Its admissible total Green allowance can grow; this is
insufficiency of that averaged input for this consumer, not a negative
theorem about all Green methods.

## 5. Analytical collision-control screen and limits

This is a premise screen using [cluster12][r12], not a rerun of its
numerical certificates. Generic analytic, Cauchy and Green identities
also hold for controls when their hypotheses hold.

| Control | Failed premise of this canonical acquisition |
| --- | --- |
| Euler-factor/translated controls | Unmodified complete theta coefficients identifying the dominant finite arm with the ordinary ζ in (4) |
| Weighted-square and finite-tail controls | Full unit coefficient sequence together with source reflection; square support or finite endpoint matches are insufficient |
| Reflected super-Gaussian control | Complete integer-square theta arithmetic needed for (7)–(10) |
| Smooth shape and positive-primitive controls | Same exact arithmetic identification, despite their shape/primitive properties |
| Finite-prime orbit controls | Full reflection and complete coefficient agreement beyond the selected primes/prefix |
| Atomic fixed-event, finite-profile and compact continuous controls | Full canonical source/profile and coefficients, beyond selected observations |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic; their RH hypothesis remains conditional |
| Fixed-amplitude variable-readout controls | Actual cosine/Newman field used by the provider |
| Inherited polynomial heat diagnostic | Theta source/provider; it still refutes only pointwise localization of global strip contraction |

If a valid field test on a control includes one of its zeros, then
|F−1|≥1 at that zero whenever the comparison carrier is nonzero;
(6) cannot hold. For a Green target containing such a zero, J≥g_K,
so the strict comparison fails. A control's collision can lie outside
this high-height, near-y=1 domain; no blanket rejection on a disjoint
zero-free box is required. Reflection rigidity is retained with its
full conjunction of hypotheses, not treated as a separate arithmetic
estimate. Relaxed measures and RSCT phase calibrations are not
identified with the canonical field/coefficients in (7).

At c=1 the displayed absolute summability allowance requires
(1+y)/2+1/8>1, i.e. y>3/4; its reflected power is (3−4y)/16.
This marks a limit of **these coarse absolute payments**, not a
lower bound on the true error or an impossibility theorem for sharper
summation. The chosen rectangle remains strictly above this threshold.
Iterating the same allowance toward zero is not justified. Finite-height
coverage, a common-time enclosure and time propagation remain separate.

The [source-use record][refs] preserves inherited review levels and
primary-source domains. No priority claim is made for this elementary
outer-layer method. B01 is complete when its decision and frozen
request are saved; E01 requires a later author-activated execution.

[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[outer]: ../../manuscript/sections/10a_transition_green.tex
[hda]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[hreview]: ../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[poly]: https://arxiv.org/html/1904.12438v2#S3
[euler]: https://dlmf.nist.gov/25.2.E11
[cauchy]: https://dlmf.nist.gov/1.9.E31
[refs]: ../references/01_GNP_BB_B01_SOURCE_USE_20261113.md
[decision]: ../brainstorm/notes/01_GNP_BB_B01_DECISION_20261113.md
[review]: ../reviews/01_GNP_BB_B01_SAME_ASSISTANT_ASSESSMENT_20261113.md
[packet]: ../research-progress/handoffs/GNP-BB-E01-r1.md
