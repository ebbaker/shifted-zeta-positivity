# Homogeneous block integrals and a paid contour comparison

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual recorded model and effort unavailable.
Status: **proved in this working draft, with exact finite algebra checks
and same-assistant assessment**. This is the dated CQ-E01 return under
the [opening contract](01_SETUP_AND_BOUNDED_FOLLOWUP_20261118.md), not a
live progress register. Full proofs are in the
[manuscript](../manuscript/main.tex), Sections 2, 6 and 7.

Read the [result index][results] and [avoid index][avoid], particularly
[cluster18][cluster], [controls12][controls], [classification01][class],
[premises02][premises], [scope07][scope] and [joint bounds12][joint].
The result is an identity and intermediate estimate. It is not an
RH-equivalent criterion or an acquired canonical width improvement.

## The extension that was proved

Fix physical H_t=-H_zz, a zero-free counted contour enclosing an N-root
block and its convex hull, the complete B=H_z/H, and
R=B-sum_i 1/(z-x_i). Let c be the block mean and y_i=x_i-c.
For a symmetric, translation-invariant polynomial J, homogeneous of
degree m and conserved by the isolated finite heat-root flow, write
J_i=partial J/partial x_i. The internal first-integral identity,
translation invariance and Euler's formula give

\[
 J'=2\sum_i J_iR(x_i),\qquad
 \sum_iJ_i=0,\qquad \sum_i y_iJ_i=mJ.
\]

With b=R_z(c) and r(y)=R(c+y)-R(c)-by, the exact balance is

\[
 J'-2mbJ=\mathcal E_J=2\sum_iJ_i r(y_i)
   =\frac2{2\pi i}\oint_\Gamma B(z)K_J(z)\,dz,
\]

\[
 K_J(z)=\sum_i\frac{J_i}{z-x_i}-\frac{mJ}{(z-c)^2}
       =\frac1{(z-c)^2}\sum_i\frac{J_i y_i^2}{z-x_i}.
\]

This is a full-exterior identity. Its first two inverse-distance terms
cancel. Counted power sums recover the symmetric coefficients and extend
the identity through internal mergers; individual singular velocities are
not evaluated at a merger. The manuscript also gives a generic small
constant perturbation argument for this continuation.

There is a whole finite family in the stated class. For the centered
monic polynomial Q(y), put theta=p2/[2N(N-1)]. The coefficient of
y^(N-j) in exp(theta partial_y^2) Q, for j=3,...,N, is a degree-j
translation-invariant heat integral. The N-2 centered integrals are
independent. J3=-p3/3 and J4=C4. Together with the centroid they recover
N-1 autonomous integrals of the complete finite coefficient flow.
Their use inside a larger divisor retains the exterior flux above.

## The exact comparison class

For exact block coordinates and a circle |z-c|=A with |y_i|<=rho<A,
use the same uniform source error sup|B-Bhat|<=epsilon. The separate
Cauchy allowance and combined-kernel allowance are

\[
 B_{\rm sep}=2A\epsilon\sum_i\frac{|J_i|}{A-|y_i|}
                 +2m|J|\epsilon/A,
\]

\[
 B_{\rm comb}=\frac{2\epsilon}{A}
                  \sum_i\frac{|J_i||y_i|^2}{A-|y_i|}
       \le(\rho/A)^2 B_{\rm sep}.
\]

For a centered quartet and J=C4,
q2=sum J_i y_i^2=-p2 p3/6. One more kernel expansion gives

\[
 B_{\rm cubic+asym}=2\epsilon|q2|/A^2
   +(2\epsilon/A^2)\sum_i\frac{|J_i||y_i|^3}{A-|y_i|}.
\]

If the quartet is reflection-symmetric, p3=0 and this is at most
(rho/A)^3 Bsep. Approximate symmetry keeps the displayed asymmetry
payment; source-error parity is not assumed.

**The radius factors compare the displayed allowances, not total canonical
errors.** Bsep is not claimed to be a sharp independent-moment feasible
range. A direct contour method allowed the same kernel gets the same
cancellation. The parent's [Note42][parent-comparison] supplies the
comparison discipline, not a source certificate for this new block.

## Coordinate payment and limits

For two N-tuples x,xhat within maximum coordinate error e, assume their
straight homotopy keeps every centered root inside radius rho, and that
the fixed contour of radius A0 stays distance at least delta from all
roots and all homotopy centers. For C4 the manuscript proves

\[
 \sup_\Gamma|K(x)-K(\widehat x)|\le G,
 \quad G=Ne(20\rho^2/\delta+20\rho^3/\delta^2+6\rho^4/\delta^3).
\]

The derivative row bound sum_j |partial_j psi_i|<=20 rho^2 pays the
variation of the gradient, while |C4|<=3N rho^4/4 pays the moving center
in the double-pole term. If |Bhat|<=Bstar, then

\[
 |\mathcal E_4(B,x)-\mathcal E_4(\widehat B,\widehat x)|
 \le2A0[\epsilon\sup|K(\widehat x)|+(Bstar+\epsilon)G].
\]

The mixed error is included. This coordinate allowance can consume the
field-error gain. Quadrature, arithmetic, source acquisition, contour
count/clearance and between-time control must also be paid in a numerical
application. No such canonical application was run in this bounded pass.

## Fixed checks and collision screen

The [exact rational program](../numerics/check_affine_flux.py) and
[record](../numerics/01_AFFINE_FLUX_EXACT_CHECKS_20261118.json) use precisely
the two six-root examples and quartic control selected in the opening
contract. No scan or extra source campaign was added.

| Case | Exact check |
| --- | --- |
| Block (-2,-1,1,2), exterior (-5,5), circle radius 4 | C4=23/12, C4'=-55/42, affine-corrected flux=-29/350; Bsep=421/18, Bcomb=31/18 and Bcubic=43/72 per unit epsilon |
| Same symmetric block, allowance ratios | Bcomb/Bsep=31/421 and Bcubic/Bsep=43/1684; these are finite-geometry allowance ratios |
| Block (-3,-1,2,5), exterior (-8,9), circle radius 6 | p3=165/8, q2=-8085/64, C4=861/128, corrected flux=7306487/13213200; verifies the nonzero asymmetry term |
| Shifted quartic, b=2, T=1/20 | C4=32/3>0 at an exact double event; discriminant in z^2 is zero |

Root-velocity derivatives, exterior balances and exterior-residue
evaluations agree exactly. These checks do not prove the general result;
the displayed derivations do. They share their author and premises.

The manuscript's Section 8 carries the analytical screen against
[controls12][controls]. Euler-factor changes fail the unchanged source;
weighted squares fail full reflected unit-weight equality; the reflected
super-Gaussian fails the canonical order-one/arithmetic premises; smooth
and positive-primitive controls fail the complete theta profile. The
generic heat balances hold for their actual fields and preserve their
collisions. Their historical numerical certificates were not replayed.
The finite-head exclusion is separately limited to freely variable tails
on an open domain; it is not imposed on the unchanged theta trajectory.

The completed bound is reusable by the parent, but a strict total
canonical improvement remains an unresolved, unactivated question.

[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[cluster]: ../../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[class]: ../../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[parent-comparison]: ../../notes/42_VCD_GT_CM_E36_CORRELATED_DISCRIMINANT_20261118.md
