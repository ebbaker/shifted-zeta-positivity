# Heat-root motion, finite caps, and higher-dimensional contours

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning
effort **max**. This is an internal research assessment and manuscript
integration record, not specialist review or a new simplicity theorem.

The author's two suggestions are to study the motion and size of the cap
through heat flow, and to revisit the quaternionic and octonionic contour
constructions. Both have concrete starting points. The first joins two
existing results that had been stated separately; the second has explicit
signed boundary currents to test. Neither requires assuming that a larger
ambient space supplies a new sign.

Read this with the [result index](../../../../../../../result-summaries/README.md), the
[heat-geometry summary](../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), the
[hypercomplex summary](../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md), and the
[avoid index](../../../../../../../avoid/README.md), especially
[target classification](../../../../../../../avoid/01_restating_the_target.md),
[coordinate lifts](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), and
[complete signed payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. Notes 17–18 are now incorporated into the canonical manuscript

The [manuscript](../manuscript/main.tex) retains the existing results and
adds three sections with their hypotheses and proof mechanisms:

| Section | Material preserved | Scope retained |
| --- | --- | --- |
| 5: complete normalized heat limit | Note 17's carrier, complete scaled tail, locally uniform bounded-scaled-time profile sum, double-zero transfer cost, and fixed-time arithmetic defects | RH for the approximation theorem; fixed taper and bounded scaled time; no original lower bound transferred to the changed target |
| 6: sharp arithmetic repair | Note 18's finite coefficient heat, first variation, moment projection, exact optimal complete transfer coefficient, and explicit double-profile example | Fixed finite filtered-Gevrey families, with the polynomial-length limit taken first; no unrestricted moving-coefficient theorem |
| 7: exact completion | Exact convergent mode decomposition, entire left remainder, second-mode obstruction, horizontal contour prescriptions, and quotient drift | Fixed positive heat time; no global zero-free normalizer or new critical-line norm theorem |

The distinction between the least correction to a specified profile and
the least norm of a repaired profile is explicit. For the example with
heat cost two, the closest repaired profile has cost
`6 - 192/pi^4 > 4`; this does not change the original infimum coefficient
`K`. The full proofs remain in [Note 17](../notes/17_NORMALIZED_HEAT_GLOBAL_LIMIT_AND_ARITHMETIC_COSTS_20261020.md)
and [Note 18](../notes/18_ARITHMETIC_HEAT_TRANSFER_AND_EXACT_COMPLETION_20261021.md).
Historical statements that the manuscript was unchanged describe those
earlier checkpoints and have not been rewritten.

## 2. Which cap, and which infinity?

In the [BW09 manuscript](../../09_expanding_contour_later_collision/manuscript/main.tex), the root-wall contour is a closed
curve in the real `(t,x)` plane. At a finite terminal time `t`, its top
cap is the spatial interval between the two selected roots. Its physical
length is their difference, not an unspecified infinite arc. Along a
root wall, the full tangential change of `arg(H+i H_x)` is zero because
the wall velocity is `H_xx/H_x`. The top cap closes this finite contour.

There are three different limiting operations in the surrounding work:

- Increasing the terminal **heat time** of this root strip.
- Sending a boundary in a **source-integral contour** to large spectral
  argument, where the source decay must pay that boundary.
- Exhausting **ordinate height** in an approximation norm, as in Notes
  16–18.

They cannot substitute for one another. In particular, BW09's winding
identity is already exact at finite terminal time. If the selected roots
remain adjacent and simple, its cap-phase decrease is exactly `pi` at
every such time, whatever its length. The outer cap from an `m`-fold
event has decrease `(m-1)pi` when its original `m` roots stay consecutive.
A useful improvement must add source information beyond this count.

## 3. The selected cap has a known late-time length under RH

[BW10 Note 01, Section 2](../notes/01_FINITE_WALLS_ARITHMETIC_RESOLUTION_AND_GAUSSIAN_SCREEN_20261020.md) proves under RH that every fixed
positive root rank continues analytically and remains finite and simple
on each compact positive-time interval. The roots born from a hypothetical
multiple zero at time zero occupy consecutive fixed ranks. This supplies,
in BW10's conditional setting, the wall identification left as an
additional premise in BW09's large-time section.

BW09 proves for the **complete original theta source** that

\[
4\pi e^{4L_t}=2tL_t+9,\qquad
L_t=\frac{\log t+\log\log t-\log(8\pi)+o(1)}4,
\]
\[
\frac{H(t,z/L_t)}{H(t,0)}\longrightarrow\cos z,
\qquad L_t x_k(t)\longrightarrow(k-\tfrac12)\pi
\]

for fixed positive `k`, locally uniformly in the rescaled spectral
variable, including every fixed derivative. Here `x=2 gamma` at time
zero; these are the manuscript's physical heat coordinates.

Combining the two established results gives, for a selected adjacent pair
with labels `k,k+1`,

\[
g_k(t):=x_{k+1}(t)-x_k(t)
 =\frac{\pi+o(1)}{L_t}\sim\frac{4\pi}{\log t},\qquad
\frac{x_k(t)+x_{k+1}(t)}2=\frac{k\pi+o(1)}{L_t}.
\tag{1}
\]

For the outer roots of a selected `m`-fold cluster, the numerator of the
length is `(m-1)pi+o(1)`. These statements apply to each fixed label,
even if its initial ordinate is very high; they give no uniform or
certified onset time as that label increases.

The physical jet has its phase concentrated on an interior layer of
width `O(L_t^-2)` in `x`, whereas the cap has width `O(L_t^-1)`.
Thus a shrinking cap can retain a whole half-turn. It does not have a
regular nonvanishing limiting jet at its collapsed endpoint to which
one could automatically apply finite-contour winding invariance.
Location asymptotics cannot be differentiated to assert eventual
monotonicity without further estimates.

For a double birth, local Hermite splitting gives
`g(t) ~ 2 sqrt(2t)` as `t` decreases to zero. Together with (1), this
implies that this gap attains a positive maximum at some finite time;
it initially opens and ultimately tends back to zero. It does not imply
a positive-time collision. This combination is a consequence of existing
results under the hypothetical RH-plus-double-zero assumption, not an
exclusion of that assumption.

There is already a finite width estimate available from BW09's complete
source moments. Set
`d mu_t(u)=e^(t u^2) Phi(u) du/H(t,0)` and
`m_1(t)=E_mu |U-L_t|`. On a fixed real rescaled interval `[-Z,Z]`,

\[
\varepsilon_0=Zm_1/L_t,\qquad
\varepsilon_1=(1+Z)m_1/L_t
\]

bound the errors in the cosine profile and its first derivative. If the
two relevant cosine-root neighborhoods of radius `beta<pi/4` lie inside
that interval, `epsilon_0<sin beta` and `epsilon_1<cos beta`, there is
one simple root in each neighborhood and no root between them. At each
root, `|sin(z-c)|<=epsilon_0`, with `c` the corresponding cosine zero.
Consequently

\[
\left|g_k(t)-\frac\pi{L_t}\right|
 \le\frac{2\arcsin\varepsilon_0}{L_t}.
\tag{2}
\]

To identify these with the specified ranks, apply the same enclosure
and intervening zero exclusion from zero through the selected pair.
Equation (2) is a direct finite consequence of BW09's estimates. Its
practical use requires certified moment bounds and the declared root
label; no numerical onset certificate has been produced in this reply.

## 4. An exact gap equation isolates the exterior-root contribution

Root motion under this heat equation is established literature. See
[Rodgers–Tao, Section 4, Theorem 4.16](https://arxiv.org/html/1801.05914#S4),
which states the principal-value root equations in its negative-time
contradiction interval. The positive-time version needed here follows
directly from BW10's paired product, so we do not import that theorem
outside its stated time range.

At a simple positive root `x_k`, implicit differentiation and
`H_t=-H_xx` give `x_k'=H_xx/H_x`. Write the even paired product as

\[
H(t,z)=H(t,0)\prod_{j\ge1}(1-z^2/x_j(t)^2).
\]

Its regular logarithmic derivative at `x_k` gives

\[
x_k'=\frac1{x_k}
 +2\sum_{j\ne k,\ j>0}
 \left(\frac1{x_k-x_j}+\frac1{x_k+x_j}\right).
\tag{3}
\]

The paired series converges absolutely because its summands are
`O(x_j^-2)`. Equivalently it is twice the symmetric principal-value
sum over all other signed roots. Evenness and order one remove an
additional linear-exponential drift in this product.

Let `a(t)<b(t)` be adjacent roots, `g=b-a`, and let `R(t)` be all signed
roots other than these endpoints. Subtract (3) at the two endpoints:

\[
S_{\rm ext}(t)=\sum_{r\in\mathcal R(t)}
              \frac1{(b-r)(a-r)}\ge0,
\]
\[
\boxed{g'=\frac4g-2gS_{\rm ext},\qquad
       (g^2)'=8-4g^2S_{\rm ext}.}
\tag{4}
\]

Every remaining root is exterior to the open gap, so every term is
positive; the exterior sum itself is absolutely convergent. Equation
(4) separates mutual repulsion from compression by the other zeros.
Repulsion of individual zeros does not imply that every gap increases.

For an adjacent pair born from an exact double zero at time zero,
integration from a positive `epsilon` and then `epsilon -> 0` gives

\[
g(t)^2=8t-4\int_0^t g(s)^2S_{\rm ext}(s)\,ds,
\qquad 0<g(t)\le\sqrt{8t}\quad(t>0).
\tag{5}
\]

The improper integral exists by its nonnegative integrand and the
finite-interval identity. This is a genuine quantitative upper bound,
but a generic one compatible with a double endpoint. For example
`H=x^2-2t` has equality and no exterior roots. The positive atomic
control `H=1+e^t cos x` has a double birth at `x=pi` and gap
`2 arccos(e^-t)`, tending to `pi`; it also obeys the bound. Its source
is atomic rather than the unchanged theta source.

Compression occurs precisely when `g^2 S_ext>2`. By (1) and (5), a
hypothetical theta double branch satisfies
`integral_0^t g^2 S_ext = 2t - g(t)^2/4`; this balance is consistent
with a gap tending to zero only at infinite time. Demanding that the
integral reach `2t` at a finite time is another statement of the
collision target, not an independently proved estimate.

The useful unresolved question is whether the complete theta source
controls this exterior interaction, the cap center, or the signed
phase density over the intermediate time range in a way incompatible
with an original double endpoint. The root equation itself does not
provide that incompatibility. Equations (2), (4), and (5) provide
quantitative diagnostics for such a study, rather than a fresh
RH-equivalent criterion supported by numerical examples.

## 5. What higher-dimensional boundaries are actually available?

The focused review covered the relevant sections of the current
[Investigation 21 manuscript](../../../../../../investigations-2/active/21_quaternion_theta_geometry/manuscript/quaternion_theta_geometry.tex), especially the regular
lifts, complete-source contour shift, signed circle current, and
closed self-dual forms. It also covered the later continuation in
[Notes 57](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/57_CIRCLE_DEFECT_MULTIPLICITY_AND_RADIUS_20261015.md), [61](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/61_JET_SURFACES_REAL_GAUSS_MAP_AND_ORIENTED_TURNING_20261015.md), [62](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/62_THETA_JET_BUNDLE_AND_SEMIFLAT_HYPERKAHLER_GEOMETRY_20261015.md),
and [63](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/00_research_coordination/63_MANIFOLD_GEOMETRY_AND_THETA_BUNDLE_CONTINUATION_20261015.md). This is a targeted contour assessment, not a
new line-by-line verification of all 96 manuscript pages.

There are several different constructions, with different boundaries.

**The original source contour.** The manuscript shifts the complete
source into `0<Im u<pi/8`. Its finite left edge cancels in the real
projection using reflection of the complete source; its right edge
decays double-exponentially. Splitting into theta summands before that
cancellation is not justified. This is already a useful contour
deformation, but it remains a complex one-dimensional source contour.

**The quaternionic and octonionic lifts.** The quaternionic field has
the form `G_m=H^(m)(tau,z)+j H^(m+1)(tau,z)`, where an auxiliary
coordinate displaces the complex heat time. The octonionic extensions
retain a prescribed physical trace and obey their monogenic equations.
Full four- and eight-dimensional boundary reconstructions involve
hypersurfaces of dimensions three and seven; they are not ordinary
one-dimensional argument-principle contours. The off-slice heat
dependence, boundary orientation, and multiplication brackets must be
retained in any proposed integral formula.

Merely allowing extra components can remove a planar winding:
`cos(phi) exp(i theta)+j sin(phi)` contracts the unit complex circle to
the point `j` as `phi` runs from zero to `pi/2`, without vanishing.
This elementary ambient homotopy is not asserted to preserve the heat
PDE. It explains why an ambient norm or an unconstrained deformation
does not automatically preserve the physical winding detector. In the
declared octonionic lift, higher jets can also keep its total norm
nonzero at an ordinary collision of `H` and `H_x`.

**A signed four-dimensional flux.** [Note 50](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md) supplies a
rigorous Stokes identity with no unproved singular-kernel formula.
At fixed physical heat time, set

\[
\alpha_f=\frac1{\sqrt2}\Re(f(z)\,dz\wedge dw),\qquad
\beta_f=\frac1{\sqrt2}\Re(P_f(z)\,dw),\qquad P_f'=f.
\]

Then `alpha_f` is closed and self-dual, `d beta_f=alpha_f`, and

\[
\alpha_f\wedge\alpha_g=\Re(f\overline g)\,dV,
\qquad
\int_\Omega\alpha_f\wedge\alpha_g
=\int_{\partial\Omega}\beta_f\wedge\alpha_g.
\tag{6}
\]

The combination `alpha_(j+1)^2-alpha_j wedge alpha_(j+2)` has physical
coefficient `L_j=h_(j+1)^2-h_j h_(j+2)`. This is a genuine signed
boundary quantity. Its coefficient pairing is indefinite, so
positivity of the separate self-dual norms does not settle its sign.
Localizing a bulk integral back to the physical line also needs an
estimate. A bounded product domain or a tube around a selected root
interval is a concrete domain to try, provided every side face and
localization error is kept.

**The spectral-circle projection.** [Note 46](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/46_OCTONIONIC_BOUNDARY_CURRENT_AND_SIGNED_CUTOFF_TARGET_20261015.md) already
reduces a projected octonionic associator to

\[
\phi_j(\theta)=h_j(t,x)\Re h_j(t,x+Re^{i\theta}),\qquad
\mathcal L_j=-\frac4{R^2}h_j^2
 +\frac4{R^2}\langle(1-\cos2\theta)\phi_j\rangle
\tag{7}
\]

on the full stationary set `h_(j+1)=0`, for `j=0,1`. Its complete-source
cutoff error on the circle is paid in that note. The scalar disk
reproduction constant is four; enlarging to the particular
eight-dimensional harmonic-ball estimate considered there gives 70,
not an automatic improvement. This comparison is about those specific
reproduction bounds, not every possible higher-dimensional domain.

Equation (7) makes the relevant contour observation explicit. The
signed integral is more informative than paying its negative and
positive parts separately: Note 57 proves that at a hypothetical
collision of multiplicity `2r+j`, fixed-radius separate masses can
grow relative to physical energy like `(T-t)^(-r)`, while their exact
signed difference has only the required `(T-t)^(-1)` loss. The local
square-root radius scale does not remove that remaining singular loss.
Thus optimizing a radius alone is not the missing sign argument.

**Geometry carrying the actual theta lattice.** Note 62 expresses the
complete source as a prescribed theta jet on the elliptic family
`tau=i exp(4u)` and gives a curved local semi-flat hyperkähler model.
This is the most specific geometric input in the reviewed material.
The physical heat weight becomes `exp(t (log y)^2/16)` and the Fourier
phase becomes `y^(ix/4)`, with `y=exp(4u)`. The Jacobi heat equation on
the theta bundle is a different evolution. Global jet transition laws,
the connection terms, and a signed estimate after this full physical
transform are still missing. A cycle or contour on that family would
be useful if it supplies such an estimate; its existence alone does
not do so.

## 6. Control screen and a bounded continuation

The [control register](../../../../../../../result-summaries/12_collision_controls_and_screening.md) prevents confusing a representation
with a separating estimate. The current proposals have the following
responses; no new source inequality has been proved that rejects all
relevant controls.

| Control | What the present comparison accepts | Premise absent from the original-theta application |
| --- | --- | --- |
| Quadratic and higher heat polynomials | Root equations and generic holomorphic/Hodge constructions | The complete arithmetic theta source and its infinite zero distribution |
| Positive atomic threshold family | Multiple endpoint, later simplicity, root-wall half-turn | Continuous original theta source and its large-time saddle law |
| Euler factor with `c=1` under RH | All-real multiple endpoint and later simple roots; generic lifts | Unchanged reciprocal coefficients and conductor-one zeta arithmetic |
| Weighted-square and finite-prime controls | Source-square bookkeeping and generic lifts | Full reflection; the finite-source examples also lack an all-real heat slice, so the all-real gap equation is not asserted there |
| Reflected and positive-primitive controls | Reflection or primitive positivity, and generic lifts | Original normalized integer-square expansion |
| BW10's close positive-source endpoint controls | Leading theta tail, reflection, completion and residue, with added doubles | Ordinary Dirichlet-series arithmetic; their properties must not be combined with a different control's stronger shape claims |

The new quantitative content in this discussion is the explicit assembly
of the selected-wall length information and the elementary gap balance,
not a new collision-excluding estimate. Higher-dimensional reconstruction
is classified as a representation until it yields a new numerical
constant, sign, or inequality for the complete source.

A focused next calculation would keep one selected adjacent root pair,
its center and gap, and compare the exterior term in (4) with a
complete-source signed boundary observation such as (6) or (7). It
should first recover the existing `pi` cap budget, keep every boundary
face and source remainder, and state precisely which additional
theta identity improves the estimate. The four-dimensional flux is
available now; a new octonionic topology is not needed to begin that
comparison. Turning this into a theorem still requires a new bound,
not merely selecting a more elaborate contour.

No numerical root-tracking campaign, new sign region, changed BW09
status, or new manuscript snapshot is claimed. The user's ideas remain
open for discussion; the exact completion obstructions in Notes 17–18
do not exclude these different geometric uses of heat flow.

## 7. Integration validation

The manuscript was checked against the statements and limit order in
Notes 17–18. The exact double-profile constants and coefficient-heat
first variation were separately checked algebraically. The final PDF
was compiled with two clean pdfLaTeX passes, with no unresolved
references or overfull boxes; all eleven pages were rendered and
visually inspected. Build intermediates remain outside the repository.
The [small build receipt](../numerics/MANUSCRIPT_NOTES_17_18_BUILD_20261021.json)
records source and PDF hashes, page count, and validation scope.

These are consolidation checks, not a new verification of the complete
analytic tail theorem. No specialist review, formal analytic proof,
new simplicity result, commit, or tag is asserted.
