# ITP-B01: integrate the unresolved phase exactly

13 November 2026, America/New_York. Intended author **Edward Baker**;
substantial OpenAI Codex LLM assistance. This worker's recorded dispatch is
**gpt-6-astra / ultra**; independently verified backend metadata unavailable.
One conceptual round, two architectures and one matched baseline.

| Next task | Type/model | Readiness | Deliverable |
| --- | --- | --- | --- |
| ITP-E01 r1 | E — GPT-6.1 Sol / Ultra | Ready and authorized | Full-line weighted L1 refinement theorem and uniform strip readout, with the specified constant/target or precise failure |
| ITP-E02 | E — GPT-6.1 Sol / Ultra | After E01 return | Assessment of topology, constants, tails and comparison |

**Select dyadic source averages with exact integration of the unresolved
phase.** The [fixed specification](../../notes/01_ITP_B01_FIXED_TRANSFER_TARGET_20261113.md)
and [frozen request](../../research-progress/handoffs/ITP-E01-r1.md) change
the convergence topology explicitly from a compact operator-norm product
estimate to weighted L1 convergence of the prepared amplitude and uniform
absolute convergence of its Fourier readout. This is a permitted B01
architecture decision, not an undeclared E-task change.

The [result index](../../../../../result-summaries/README.md) and
[avoid index](../../../../../avoid/README.md), particularly
[controls 12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[classification 01](../../../../../avoid/01_restating_the_target.md),
[premises 02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[representations 03](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scope 07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
govern the interpretation. This is a quantitative approximation milestone,
with a proposed absolute error 10^-6 uniformly in real height, fixed
transverse strip |y|<=8 and 0<=lambda<=1/2. It is not a normalized relative
or logarithmic error claim, and cannot imply a zero exclusion.

## The two architectures

1. **Inherited phase/source-ratio products with phase frozen at the last
   represented cell:** local source ratios telescope and phase factors
   approach identity at fixed height. Their compact bound contains |x|h.
   More decisively, a readout that puts the entire cell mass at its center
   is an atomic lattice measure: at x=2*pi*k/h all center phases coincide
   up to one sign. Its all-height error cannot tend to zero as h tends to
   zero through such approximants. This is a failure of that fixed-grid,
   point-phase architecture in the supremum norm over all real heights;
   it does not exclude compact-height convergence or other quadratures.
2. **Selected: the same source-average recursion, exact cell phase.**
   On each unit slab retain the dyadic ratios and their growing support,
   but evaluate the conditional expectation of the entire unresolved
   phase product. It is the elementary factor sinc(z*h/2) times the phase
   at the center, not a point-phase replacement. The resulting density
   is the cellwise average P_h W. Weighted L1 control transfers directly
   to all real heights, avoiding both |x|h and a global positive floor.

The common baseline is direct scalar integration of the **same** cellwise
constant density. The selected network and baseline give exactly the same
readout and error bound. Thus the gain is a stronger, honest convergence
statement for this limiting contraction, not a tensor speed advantage.
The recursion still requires cell masses from the complete source; source
ratio gates retain growing support, and no bounded rank or cheap
coefficient-acquisition rule is supplied.

## Fixed scope and quantitative target

Use the complete W_lambda=e^(lambda*u^2)Phi, the Fourier factor 1/2 and
tau=1/2-lambda. Set h=2^-L, cells [jh,(j+1)h), centers c_j=(j+1/2)h,
m_j(lambda)=integral_cell W_lambda and

    A_L(lambda,z) = sinc(z*h/2) sum_j m_j(lambda) exp(i*z*c_j)/2.

The readout is entire in z at each finite cutoff, including the removable
point z=0. Its complete-line sum uses the full source and converges on
every horizontal strip. The first estimate to derive is

    sup_(lambda in [0,1/2], x in R, |y|<=8) |H_lambda(x+iy)-A_L(lambda,x+iy)|
       <= h exp(8h) V_8/4,
    V_8 = sup_lambda integral_R exp(8|u|)|W'_lambda(u)| du.

The candidate constant is V_8<=868. With U=2 and L=30, the finite-cell
readout also pays (1/2) integral_(|u|>2) exp(8|u|)W_(1/2)(u)du.
E01 must prove a complete <=10^-6 allowance or explain its failure;
these constants are proposed and are not accepted results at B01.
The full-line theorem concerns all L>=0, while this one tuple measures
its consequence. No array of the billions of formal cells is allocated.

Compact ratio-product existence is inherited. The new question is the
weighted full-line quantitative transfer after analytically retaining
the phase tail. Its proof route is an elementary cell-mean Poincare
inequality, the complete source derivative envelope, and exact cell
integration. No new external theorem or unproved arithmetic estimate is
needed. The result remains a generic regular-source approximation theorem.

## Actual controls and failed premises

Smooth reflected and positive-primitive colliding controls can meet the
weighted W^(1,1) assumptions and can obey this approximation bound with
their own derivative constants. **No approximation premise is required to
fail at their collision.** The inherited source arithmetic is absent, but
that alone does not show a different numerical bound. Their events are
faithfully approximated rather than ruled out.

| Catalog family | Premise boundary in this request |
| --- | --- |
| Euler-factor/translated sources | Unchanged theta source fails; weighted derivative estimates may still hold. No claim that the particular constant 868 rejects their event. |
| Weighted-square/finite-prefix/finite-prime families | Complete coefficient/reflection conjunction fails. Piecewise regular reflected densities can still satisfy the W^(1,1) estimate; finite event times are not called all-real thresholds. |
| Reflected super-Gaussian and smooth/positive-primitive controls | Canonical square arithmetic fails; smooth density, decay and local ratio products may all pass. The bound is compatible with their actual collisions. |
| Atomic threshold controls | The L1 absolutely continuous density and W^(1,1) assumptions fail. Their exact rank-one event still refutes an interpretation based only on positive tensors. |
| Continuous finite-profile extensions | The W^(1,1) theorem applies when their extension has that regularity; canonical full profile/arithmetic and threshold simplicity remain absent, without a sign consequence. |
| RH-conditional endpoint controls | Ordinary Dirichlet-series arithmetic fails; conditional construction remains conditional. Close-source approximation does not reject their doubles. |
| Fixed theta source with altered kernels | Literal Fourier/Newman readout fails; the sinc identity is proved only for the retained exponential readout. |
| Actual-profile relaxed positive measure | It is not an integer zero configuration or a specified theta amplitude. Its moment feasibility is not a field value here. |

This is an analytical premise screen using existing witnesses, not a new
collision computation. Other kernels, counter-kernels and smooth-density
controls are treated by their actual regularity/readout premises; no sign
statement is made for any of them. The atomic lattice aliasing comparison
is a theorem target about one approximating architecture, not about zeros
of theta or impossibility of every infinite tensor product.
