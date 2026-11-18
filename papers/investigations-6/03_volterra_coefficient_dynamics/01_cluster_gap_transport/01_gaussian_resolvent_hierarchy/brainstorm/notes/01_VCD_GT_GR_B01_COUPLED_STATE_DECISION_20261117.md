# B01 — finite holomorphic evolution, radial observations, and spatial moments

17 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI
Codex LLM assistance. Lead actual model/effort unavailable in chat0001's
recorded configurations. Intended effort ultra; bounded E helpers requested
as gpt-6.1-sol/ultra, distinct from independent serving attestation.

**B decision, not a quantitative gain.** This is preparatory representation
work under [avoid01](../../../../../../../avoid/01_restating_the_target.md).
Read the [result index](../../../../../../../result-summaries/README.md),
[cluster18](../../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[control screen12](../../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../../../../avoid/README.md), especially
[scope07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [joint bounds12](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
The [sole register](../../research-progress/01_VCD_GT_GR_RESEARCH_PROGRESS_20261117.md)
owns activation. E01's fixed audit must be completed before the E02/E03
requests are frozen. Parent Note44 remains preliminary evidence.

## Fixed problem and comparison of the two candidates

Keep the complete theta H, H_t=-H_zz, the separately paid count-two tube,
c,D,w_j,a_j and frozen ell in the overview. T>=64, L=log T, ell=1/L,
c in [T,2T], |D|<=d ell^2, max(2,4 sqrt(d))<=a<=L and |w_j|>=r0=a ell.
Targets lie within r0/4. Include both D signs, D=0 and multiplicities.
Neither external simplicity nor an earlier real pair is an assumption.

1. Radial chi_s(w)=exp(-s|w|^2), s=R^-2, is bounded and its finite
   telescoping weights are nonnegative. Its merger evolution is not
   automatically C1. We retain it as a slice observable and do not silently
   import the analytic contour proof into this nonholomorphic weight.
2. Holomorphic E_s(w)=exp(-s w^2) is analytic in w, with modulus
   exp(-s x^2+s y^2). On the source strip and each finite positive interval
   s_-<=s<=s_+, the full weighted sum exists. It retains complex phase,
   may grow vertically, and has no general zero endpoint at s=infinity.

**Selection:** finite holomorphic Gaussian evolution, coupled to the
branch-free resolvent and an odd spatial companion. Keep radial observations
by the exact conversion below. This hybrid uses the advantages and pays the
costs of both proposals; it claims no finite autonomous closure.

## Selected observations and exact conversions

For p=1,2,3 define
G_{s,p}=sum_j E_s(w_j)/a_j^p, A_{s,p}=sum_j chi_s(w_j)/a_j^p,
and Delta_{s,p}=A_{s,p}-G_{s,p} with its literal complete sum.
The unweighted integer moments S_p are also retained, through S4 where
needed for the S2 derivative. Every finite split retains its complement:
S_p=G_{s,p}+(S_p-G_{s,p}); successive s values give the full telescope.
Radial reconstruction uses all scale endpoints as in parent Note44.

At each occurrence,
|chi_s-E_s|=e^(-s|w|^2)|1-exp(2s y^2-2isxy)|.
This expression is retained; a usable bound may use the straight segment
exponential inequality, but must pay the vertical exp(s y^2). There is no
claim that Delta is small at a microscopic R. Fixed physical s and s of
order L^2 must be compared separately in B02.

The branch-free local resolvent is R(eta)=sum_j(a_j-eta)^(-1) on
|eta|<inf|a_j|, at least the disk |eta|<r0^2-|D|. A local contour
formula can use a smaller disk where its auxiliary poles remain inside
the actual chosen circle; do not confuse these two radii.
The odd spatial observable is T2=sum_j w_j/a_j^2. E02 proves S2' and
one contour evolution formula for T2, retaining the full log field where
closure requires it. The conditional ordered quantity P=sum w_j/a_j
must disappear before an absolute canonical passage or receive its full
prescribed product convention. It is not an absolute new state coordinate.

## Fixed proof route for E02 and E03

E02: verify the finite S2' law in Note44, remove pairwise singularities,
then pass at each reference slice through opposite/conjugate complete
products, counted contour moments and the heat derivative. Prove the
resolvent expansion on its true collar disk, the contour expression and
derivative of T2, and regularity through multiple roots. The reference-slice
argument does not assert common-time convergence of polynomial flows.

E03: put h(t,w)=H_z(t,c(t)+w)/H(t,c(t)+w). On zero-free contours,
h_t=-h_ww-2h h_w+c' h_w. For f=e^(-s w^2)/(w^2-D)^p, express G_{s,p}
as the outer strip contour integral of f h minus the inner circle
|w|=r0/2. The outer contour tends to the horizontal lines Im w=+/-4.
Choose vertical cuts avoiding projected zeros using the unit count, and
bound their log fields by safe-line subtraction; the Gaussian kills these
edges. Then differentiate the horizontal-integral representation uniformly
on the real tube. This avoids assuming smooth individual root labels or
one time-uniform sequence of vertical contours. Retain the inner residues.

For fixed s, the candidate differential operator after integration by parts
is integral of (p D' E_s/Q^(p+1)-f_ww-c'f_w)h + f_w h^2, outer minus inner.
All signs and contour orientations must be checked. A moving s would add
-s' w^2 f; ell and selected s values are frozen here. The full h^2 keeps
all interactions. For M=sum scale pieces, 2M^2 always includes every
cross-scale product. No bandwise positivity is required.

## Intended quantitative consumer and controls

B02 will compare at most two finite-split consumers: a fixed physical
Gaussian with an explicitly small normalized forcing complement, and
microscopic Gaussian localization with its full phase/conversion cost.
The exact forcing is ell^4(12S2+16DS3); the baseline is K L at fixed a,d,
with O(sqrt L) negative Riccati allowance and O(L)exp(O(sqrt L)) transport
cost on a paid fixed scaled interval. Any quantitative estimate must
receive an equally informed direct comparator. The incoming D value,
initial layer, tube duration and endpoint equality remain explicit.

The documentary control screen in parent Note44 §7 and Assessment19 §2
is reapplied: polynomial quadratic/quartic flows share the identities and
can collide; finite population lacks canonical growing counts but can pass
a coarse upper count. Euler-factor controls change theta and its endpoint
count discrepancy. Weighted-square/finite-source/finite-prime classes lose
full reflected unit-weight equality; documented endpoint-defective classes
also lose the fixed strip. Reflected super-Gaussians lose order<=1.
Smooth-shape/primitive controls change arithmetic; strip/count/density
transfer is untested. Fixed-event atomic/finite profiles lose theta growth.
RH-conditional endpoint controls keep their RH premise and changed
arithmetic; doubles at time zero are allowed. Changed observation kernels
lose the physical cosine law; fractional profiles lose the integer divisor.
Identical-count opposite-sign slices pass coarse aggregate bounds but supply
no canonical common-time tube. None of the representations rejects a control
merely by being an identity. E02/E03 need no new literature import.

If the two selected Gaussian consumers fail, preserve their exact estimating
class and route the identified repair to B03. Do not enlarge a helper's
packet or claim that all Gaussian, radial or canonical methods are excluded.
