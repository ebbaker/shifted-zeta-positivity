# Review of the all-multiplicity physical remainder audit

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6-astra (Codex)**,
reasoning effort **ultra**. This is a separate subagent review within the
same-model research session, not independent specialist review.

**Assessment: the stated all-finite-multiplicity remainder extension and
scoped obstruction are supported by the written argument.** The
[note][note] keeps the unchanged physical jet (H,Hx), replaces the
double-event normalization by its first nonzero jet h_m, and pays the
whole boundary using derivatives only through m+2. Its conclusion is
the inherited negative degree. It does not supply a zero-winding
arithmetic estimate or exclude any theta event.

## Finite-derivative expansion

The reviewer rederived both parity cases in equation (3). Expanding H
in time through q=floor(m/2), then expanding each spatial term through
m-2k, gives the displayed heat polynomial. When m is odd, the final
time remainder uses H^(m+1) and exactly completes the last term in
b_(m+1). When m is even, it instead uses H^(m+2), producing the separate
r^2/(q+1)! term. Applying the same calculation to Hx reverses those
parities and yields b_m in the leading remainder. Thus the proof does
not require an infinite Taylor majorant or an unacknowledged higher
derivative.

The expansions use exact vanishing of every original event derivative
below order m. Their paths stay inside the complete rectangle for both
signs of time. Approximate cancellations or interval event locations
are explicitly outside the unpaid analytic formula, which is the
appropriate limitation.

## Boundary, orientation and source errors

The recurrence nP_n=yP_(n-1)-2tau P_(n-2) rules out every common zero
of (P_m,P_(m-1)) except (0,0). For |tau|>=1/(4m^2), descending this
recurrence gives the claimed crude coefficient L^(m-1), with
L=2m^2(m+2). For smaller |tau| on the boundary, |y|=1 and the
exponential-series comparison leaves at least 2/(3(m-1)!). Both imply
ell_m=1/(2L^(m-1)). The norm conversion uses sqrt(2), and the weaker
factor two in ell_m is conservative.

The spacetime scaling determinant is r^3>0; the constant target scaling
has determinant 1/(h_m^2 r^(2m-1))>0. Consequently the sign of h_m does
not reverse winding. The second component is the original Hx, and this
calculation does not confuse the physical index with the degree of
(H^(m-2),H^(m-1)). Equation (6) makes the sum of the two remainder
allowances at most ell_m/2. Straight-line homotopy therefore covers
all four faces and corners. The degree -floor(m/2) is explicitly
inherited from the existing index result.

For the all-mode exterior, u^J is bounded by the exponential tangent
at U, the source exponent is concave there, and D_J>0 pays the full
integral. The denominator 1-16exp(-3pi exp(4U)) correctly sums a
majorant for successive modes. On [0,U], the low-source tail follows
from the two stated bounds on (v+k)^4 and (v+k)^2 and the exact
Eulerian generating sum for (k+1)^4. These two regions are disjoint
and exhaustive. The finite interval factor e^(bU^2) needs b>=0, which
holds in the intended positive-threshold application. The requested
explicit b>0 scope and correction of literal carriage returns in the
parity-indicator TeX were both incorporated before final review.

The normalized numerical-component payment in equation (9) has the
correct powers r^m and r^(m-1). It makes clear why an arbitrarily small
analytic radius is not an acquired numerical certificate at fixed
absolute error. No cost advantage or uniform multiplicity margin is
claimed.

## Exact controls

The reviewer inspected and replayed the [checker][checker] with its
output outside the checkout. All **11 multiplicity rows, m=2,...,12**,
passed for asymmetric P_m+P_(m+1)+P_(m+2) and negative normalization,
at both the larger diagnostic radius and the sufficient small radius.
The complete polynomial coefficient envelopes bound the full rectangle;
they are not boundary samples. The checker independently verifies the
PDE, spatial derivative and recurrence identities before checking the
parity payments. The inherited degree is labeled as inherited in the
[record][record], rather than being represented as a newly computed
winding certificate.

This finite replay checks normalization and the explicit payments. The
proof for every finite m is the analytic argument reviewed above, not
an extrapolation from the tested orders. No actual theta moment,
theta event or numerical source-tail evaluation was acquired.

## Scope of the obstruction

The admitted information class consists only of the centered Hermite
boundary field and symmetric nonnegative component allowances. It
contains the exact model for every allowance, including zero. That
single admissible model prevents a universal zero-degree conclusion;
under the strict boundary margin, every admitted curve has the
negative inherited degree. The same retained information also permits
the interior model event in a direct first-jet test.

This statement does not exclude an estimate using additional signed
arithmetic data, correlated residuals that remove the model, or an
event-free domain. It does not assign theta source identities to the
polynomial controls. The note keeps those distinctions explicit, in
accordance with [target classification][a01], [control screening][a02],
[scope discipline][a07] and [same-model review limits][a05].

The useful completion is the actual all-multiplicity audit of BW-01's
existing payment: nondegeneracy at order two is no longer required,
but the selected reduced information remains incapable of the intended
contradictory degree. Another source of signed arithmetic information
is still needed.

[note]: ../notes/02_ALL_MULTIPLICITY_REMAINDER_AUDIT_20261020.md
[checker]: ../numerics/check_all_multiplicity_remainders.py
[record]: ../numerics/ALL_MULTIPLICITY_REMAINDER_CONTROLS_20261020.json
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
