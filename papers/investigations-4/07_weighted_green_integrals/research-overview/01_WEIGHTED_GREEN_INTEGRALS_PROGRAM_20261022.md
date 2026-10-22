# Weighted Green integrals: initial research program

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified from the current turn metadata.

**Two analytic rounds recorded, 22 October 2026.** The
[opening note](../notes/01_REGULAR_SLICE_AND_COUPLED_LOG_ENCLOSURES_20261022.md)
pays the regular slice and generic enclosures. The
[paired-source continuation](../notes/02_PAIRED_THETA_RESIDUAL_AND_MATCHED_DIRECT_COMPARISON_20261022.md)
strictly sharpens a canonical exponential-moment cap and pays a one-/two-source
residual enclosure. Direct density inherits the identical linear/quadratic
corrections and cubic allowance, so that declared class ties the same-data
baseline. A complete WGI gain/cost saving remains open; actual acquisition
and error schedules are unfrozen. There is no theta run, RH/simplicity
conclusion or specialist review. The sole detailed ledger is the
[progress register](../research-progress/01_WEIGHTED_GREEN_INTEGRALS_PROGRESS_20261022.md).

## Object and exact target

At fixed real time let H be holomorphic near a bounded smooth spatial
domain Ω, not identically zero, with (H,H_z) nonzero on its boundary.
Use the unchanged normalization H_t=−H_zz,
8H(0,z)=ξ(1/2+iz/2), and set
\[
 E=|H|^2+|H_z|^2,\quad u=\log E,\quad
 g_2=\frac{|HH_{zz}-H_z^2|^2}{E^2}.
\]
The normalized **completed** measure is
\[
 d\nu=\frac1{4\pi}\Delta u
 =\frac{g_2}{\pi}\,dA+\sum_a(m_a-1)\delta_a.
\]
Here m_a is the multiplicity of an H zero; the regular density is extended
across canceled common factors. An m-fold zero contributes m−1, not m,
to the atom. The unnormalized Gauss contribution is π(m−1).
For real ψ∈C²(Ω̄), Green's second identity gives
\[
 M_\psi:=\int_\Omega\psi\,d\nu
 =\frac1{4\pi}\oint_{\partial\Omega}
  (\psi\partial_nu-u\partial_n\psi)\,ds
 +\frac1{4\pi}\int_\Omega u\Delta\psi\,dA. \tag{W1}
\]
These are [survey G1–G2](../../brainstorm/05_BROAD_SURVEY_OF_TOPOLOGICAL_INTEGRAL_FORMULAS_FOR_RH_AND_SIMPLICITY_20261022.md)
and [BW10 GA1–GA7](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md)
in explicit normalized form. Projective cancellation does not remove
the original-vector atom.

## First bounded comparison contract

Use the sufficient ordinary-double window and constants already specified
in [Shared Note 03](../../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md)
and [Note 05](../../notes/05_TARGET_INVENTORY_AND_FINITE_REGULATOR_GAUSS_COMPARISON_20261022.md).
This is conditional on an event, not an acquired theta event. Freeze its
spatial disk D_R(a) and one regular real slice t₀=d/4>0. Confirm inherited
regularity on that slice before forming any density quotient.

Choose ψ(z)=(1−s)³ on s=|z−a|²/R²≤1, extended by zero outside.
It is C², ψ=∂_nψ=0 on the circle, and
\[
 \Delta\psi=\frac{12}{R^2}(1-s)(3s-1),\qquad
 M_\psi=\frac3{\pi R^2}\int_{D_R(a)}
 (1-s)(3s-1)\log E\,dA. \tag{W2}
\]
The exact kernel is negative for s<1/3 and positive for s>1/3.
The first analytic task is a complete, **coupled** enclosure of this
signed log integral using the canonical-source constraints from
[home 02](../../02_theta_source_constraints/README.md).
Upper jet bounds alone do not pay its negative-weight sector.
Unknown interior energy floors and endpoint nonvanishing are forbidden
inputs. Pay any excision or regularization bias explicitly.

Before quadrature, fix one common data package: complete canonical values
and jets through order two, any higher derivative allowances actually
used, the same chart and boundary constants, source-mode/ray tails,
reflection constraints, rounding and acquisition costs. Compare the
candidate with the stronger of direct weighted-density integration and
the existing unweighted Green certificate, since 0≤ψ≤1. At a singular
slice the direct target must also include Σ(m_a−1)ψ(a).
Grant both methods every acquired source datum and useful correlation.

**Acceptance:** prove a strict smaller complete upper certificate by a
declared positive margin, or a rigorous acquisition saving at the same
error target. Do not treat a different representation, floating timing,
or regularization alone as a gain. Stop this fixed contract if the signed
log payment gives no improvement; record its precise estimator class.
Actual theta numerics remain gated on this comparison design and a
potential analytic gain. No numerical parameters are being acquired now.

## Controls and global boundary

H=z²−2t retains the atom and supplies a mandatory endpoint control;
H=z has positive smooth Gauss density without a common zero. Apply
[cluster 12](../../../../result-summaries/12_collision_controls_and_screening.md)
to Euler-factor, weighted-square/finite-prime, reflected/primitive and
RH-conditional close endpoint controls using each family's own source
constants and failed arithmetic premise. Finite-source perturbations
have no all-real heat slice. Identities should retain their collisions;
an exclusion claim requires a new canonical quantitative distinction.

W1–W2 require no RH. RH→simplicity needs every endpoint height and finite
multiplicity, plus an endpoint-uniform estimate incompatible with the
completed atom. RH directly additionally needs the existing threshold,
confinement/no-escape and all-height coverage arguments. A finite bound
or a regular t>0 pilot settles neither. Gauss area is not the moving
real critical-wall q trace; g₂=q² there supplies neither its sign nor a
trace theorem. Those consumers remain separate.

Follow [results](../../../../result-summaries/README.md) and
[avoid](../../../../avoid/README.md), especially
[01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
