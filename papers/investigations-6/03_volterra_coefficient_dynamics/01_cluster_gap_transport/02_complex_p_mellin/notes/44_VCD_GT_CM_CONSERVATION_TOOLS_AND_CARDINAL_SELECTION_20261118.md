# B10 r4 — Conservation tools and the selected interpolation refinement

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual root model and effort are unavailable
in CM chat0006's guarded metadata. E38/E39 helpers were explicitly selected
as `gpt-6.1-sol`, effort `ultra`; selection is not serving attestation.

**Status: analytical mechanism selection and a scoped pair-flux identity.**
The conservation manuscript provides useful cancellation and error-accounting
tools, but it does not yet provide an improved canonical gap estimate. The
selected E38 milestone is the fixed interpolation refinement proposed in
[Continuation43](43_VCD_GT_CM_CORRELATION_GAIN_CONTINUATION_20261118.md).
The [sole progress register][register] owns current status.

Read [result summaries][results] and [avoid][avoid], specifically
[cluster18][cluster], [controls12][controls], [classification01][class],
[premises02][premises], [scope07][scope] and [joint12][joint]. The two
candidates below are a finite error-width improvement and a representation
with a scoped error comparison, respectively; neither is an RH-equivalent
criterion. The prospective numerical gate is a factor of ten, fixed before
execution, rather than an assertion-count or precision milestone.

| Task | Type / recommended model | Dependency | Bounded output |
| --- | --- | --- | --- |
| E38 | E / Sol; explicit cardinal proof and fixed replay | Independent proof preflight | Degree32 norm <17; unchanged-source whole-minimum width compared with Record19 |
| E39 | E / Sol; nonauthor assessment | E38 proof and final outputs | Proof/rounding/control audit and one matching replay |
| Further affine-flux acquisition | B / Astra; missing signed/correlated input | Not selected for execution | A paid source/coordinate/time estimate that beats the equally informed direct kernel |

## 1. What the conservation manuscript supplies

The [child manuscript][manuscript], Sections 2 and 6–7, gives finite
coefficient integrals, the homogeneous flux law

    J' - 2m b J = 2 < B K_J >,
    K_J = Z^(-2) sum_i J_i y_i^2/(Z-y_i),

where B=H_z/H, Z=z-c, b is the derivative at c of the complete
exterior logarithmic derivative, and <f>=(2 pi i)^(-1) integral_Gamma f dz.
The constant and linear exterior terms cancel before a triangle bound.
Its radius-square allowance, symmetric-quartet refinement and coordinate
payment are directly reusable bookkeeping. Their premise is a completely
counted block with a cleared enclosing contour, not a finite exterior cutoff.

Three limitations matter for this parent task. A two-root isolated block
has no nonconstant centered autonomous coefficient integral: its sole
centered degree of freedom is the heat clock. C4 therefore supplies no
new invariant for this pair. For a quartet C4 can remain positive at a
collision; variance and the discriminant must be retained jointly. Finally,
the finite-head obstruction assumes freely variable tails and does not
exclude canonical constrained tails or the optional E16 approximation task.
The [nonauthor tool assessment][review] checks these distinctions.

## 2. An exact pair adaptation, retaining the heat clock

Let a stationary cleared contour enclose exactly two zeros x_±=c±s,
counting multiplicity, with its interior containing their convex hull.
Put D=s², Q=(z-c)²-D, and R=B-Q_z/Q, the complete holomorphic exterior.
This allows complex s and either sign of real D. Set b=R_z(c).
At a simple slice, the physical heat-root equations give

    D' = 2 + 2s [R(c+s)-R(c-s)]
       = 2 + 4bD + E_D.                                  (1)

The intrinsic term 2 cannot be dropped: D is not one of the autonomous
integrals in the child's general-flux theorem. Cauchy's formula for R,
including cancellation of the interior rational poles, gives

    R(c+s)-R(c-s) = < 2s B/(Z²-D) >,
    b = < B/Z² >,
    E_D = 4D² < B/[Z²(Z²-D)] >.                         (2)

All quantities are symmetric contour functions of the counted divisor.
Thus (1)–(2) extend through an internal merger while the outer count and
clearance persist. At D=0, D'=2; no fictitious zero barrier is created.
These identities are compatible with the parent's D'=2-4DM:

    M = -b - D < B/[Z²(Z²-D)] >.

If |R_zzz|<=C3 on the two straight center-to-root segments, Taylor expansion
through degree two gives

    |E_D| <= (2/3) C3 |D|².                              (3)

Indeed each third-order remainder is at most C3|s|³/6; their difference,
multiplied by 2s, gives (3). This is a conditional local estimate, not an
acquired canonical C3 bound. A time-dependent integrating factor
mu(t)=exp(-4 integral_(t0)^t b(v) dv) yields the exact paid balance

    mu(t)D(t)-D(t0) = integral_(t0)^t mu(v)[2+E_D(v)] dv.  (4)

Uncertainty in b affects both mu and the same remainder. Coordinate,
quadrature, arithmetic and true time-uniform errors must accompany any
future use. A formal integrating factor is not an improvement by itself.

## 3. Why affine separation alone is not the selected gain

For exact c,D, |D|<A² and uniform |B-Bhat|<=epsilon on |Z|=A, (2) gives

    error(E_D) <= 4 epsilon |D|²/[A(A²-|D|)].              (5)

This smaller remainder is useful, but b must be paid too. Applying the
same pointwise source-error model to the combined exterior term in (1)
gives the direct triangle allowance

    B_direct = 4A epsilon |D|/(A²-|D|).

The independently bounded affine and residual terms give exactly

    4 epsilon |D|/A + 4 epsilon |D|²/[A(A²-|D|)]
      = B_direct.                                        (6)

Therefore **this split, with independent triangle bounds from the same
uniform B-error, does not improve this direct allowance**. This is an exact
algebraic comparison of these stated allowances, not their sharp support,
not a lower bound on actual error, and not an obstruction to joint-time
propagation, correlated supports or an independently better b estimate.
The child's sharper J-flux comparison concerns a different functional:
it subtracts an affine response whose uncertainty must still be accounted
for when reconstructing the pair's full derivative.

The existing source record controls G rather than B=G_z/G directly.
Converting it needs derivative error and a denominator floor, or a paid
integration-by-parts log kernel. The source point-error epsilon in (5)
cannot be set equal to Record16's field error. A newly counted quartet
would additionally change the population and require new source geometry.
No such acquisition is issued in this pass.

## 4. Selected main-line step: exact cardinal amplification

The actual 33 Lobatto nodes are x_j=cos((32-j)pi/32). Let h_0=h_32=1/2
and h_j=1 otherwise. For the exact implemented DCT-I interpolant,

    ell_j(x)=(2h_j/32) sum_(k=0)^32 h_k T_k(x_j)T_k(x).

Weighted discrete orthogonality gives a norm at most8 on [-1,1]; outside
that interval the cardinal signs agree with the alternating nodal values
of T32, so the norm is exactly T32(|x|). Thus on [-503/500,1] it is below17.
The full derivation and implementation audit belong to [E38 Note45][proof].
Both independent author and nonauthor preflights match the reversed node
ordering and endpoint weights. Complex nodal errors obey the same norm
bound. Outward coefficient balls continue to pay transform arithmetic.

Only the original pre-time nodal source/spatial error is multiplied by17
instead of1100. The negative-time majorant, true-field time remainder,
polynomial derivative weights, archive, degree, source nodes, precision,
contour nodes and physical interval remain fixed. Both centered and sharp
independent-moment direct estimators receive the same new budget. Re-enclose
the affected geometry and consumers; use a fixed tenfold whole-minimum
width gate against Record19. This is tighter error accounting for the same
source data, not new observations or improved recursive convergence.

## 5. Collision controls and scope

The cardinal bound and flux identity are generic and hold for every
control with their stated interpolation or local heat premises. No control
is supposed to fail the generic algebra. The exact quadratic control must
still contain D=0 at its collision and fail a strictly positive whole-time
gap contract. The child quartic likewise keeps positive C4 at its double
zeros, so C4 positivity is explicitly rejected as a standalone barrier.

The [catalog][controls] screen distinguishes the actual failed premises:
Euler-factor translates change the normalized theta coefficients and
completion; weighted squares fail the full reflected unit-weight source;
reflected super-Gaussians fail literal arithmetic and canonical order one;
smooth shape/positive-primitive controls fail complete canonical arithmetic
and profile equality. Finite-prime controls fail full reflection; finite
score/profile variants fail the particular full-source/profile premises
listed in the catalog. Atomic threshold profiles lack the complete canonical
population and eventual simplicity. RH-conditional endpoint perturbations
change ordinary Dirichlet arithmetic and retain RH as an input. Changed
observation kernels fail the literal cosine/Newman equation; fractional
profiles lack integer divisor realization. Static divisor surgery does not
supply a common canonical heat tube. Naming those failures does not make
the generic estimate a discriminator: the finite application still depends
on the unchanged source archive, independent counts and strict margins.

The new pair identity has no all-height conclusion. The numerical gate,
if attained, concerns only the same pair and I=[-.0003,.1]. It pays neither
the 388-root census's missing forward tube nor stable truncation, common-time
finite-divisor approximation, all-edge closure or a Newman upper bound.
Previous records and both manuscripts remain unchanged.

[register]: ../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md
[manuscript]: ../01_conservation_laws/manuscript/main.tex
[review]: ../reviews/20_VCD_GT_CM_CONSERVATION_TOOL_ASSESSMENT_20261118.md
[proof]: 45_VCD_GT_CM_E38_CARDINAL_SOURCE_REFINEMENT_20261118.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
