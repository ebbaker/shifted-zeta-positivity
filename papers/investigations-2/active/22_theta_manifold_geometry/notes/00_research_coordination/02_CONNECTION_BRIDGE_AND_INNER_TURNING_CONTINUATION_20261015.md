# Connection bridge and inner turning continuation

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded session model **gpt-6-astra**, reasoning effort **ultra**, verified from this conversation's session metadata.

The first continuation of Investigation 22 completes the proposed insertion of the theta connection into the signed two-source transform. It also sharpens the local collision profile. The resulting identities narrow the missing estimate: tangential ASD curvature supplies no new signed term, the original cusp norm growth can be removed by a base metric change, and the second angular branch requires a distinct energy comparison even on a shrinking interval.

## Established continuation results

| Result | Consequence | Detailed argument |
| --- | --- | --- |
| Base-only ASD metrics satisfy `Delta b=4*pi*q`; choosing `b=2*pi*p²*q` gives unit norm and zero connection on the physical path | Cusp divergence of the original metric is representative-dependent. The curvature and vertical theta source operator remain unchanged | [Metric freedom and physical restriction](../03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md) |
| The physical path and its external two-source product have flat pulled-back connections | A new curvature-sign term cannot be obtained merely by rewriting tangential derivatives covariantly. This does not rule out transverse or global arithmetic information | Same note |
| Exact complete signed kernels, all primitive lower endpoints, and a covariant-jet evolution recurrence are available | Both heat factors, spectral phases and every theta index remain present. The branch-0 edge and physical-energy corner survive reconstruction | [Complete signed correlation bridge](../03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md) |
| With `s=T-t` and `x=chi(s)+s*xi`, the angle tends to `arctan(r*xi)` and `s*alpha_x` tends to `r/(1+r²*xi²)` | The positive turning core has width of order `s`, sharper than the existing `sqrt(s)` interval. A uniform strict quarter-turn gap would already exclude collisions | [Universal inner turning profile](../02_signed_turning_control/01_INNER_TURNING_PROFILE_20261015.md) |
| At odd collisions, `E_1^jet/E` tends to `1+r²*xi²` | The energies agree asymptotically at the stationary center, but not across a fixed inner scaled window. A source-to-angle estimate must carry this factor | Same note |

The original quarter-turn theorem passes review and needs no correction. The original ASD metric and curvature formulas remain correct; the new result identifies their metric freedom and sharpens the interpretation of their cusp growth.

## The complete signed target

Put `c_j(u)=u^j cos(xu+j*pi/2)` and

\[
 I_j=\int_0^\infty\psi(u)(\partial_u^2-1)
       [e^{tu^2}c_j(u)]\,du.
\]

The physical reconstruction is

\[
 8h_j=\tfrac12\delta_{j0}+I_j.
\]

Consequently the stationary lower-bound targets are exactly

\[
 I_1^2-I_0I_2-\tfrac12 I_2
 \ge-\kappa_0[\tfrac14+I_0+I_0^2+I_1^2]
 \quad\text{when }I_1=0,
\]
\[
 I_2^2-I_1I_3
 \ge-\kappa_1[\tfrac14+I_0+I_0^2+I_1^2]
 \quad\text{when }I_2=0.
\]

These are exact reformulations of the existing target, not new estimates. The coefficients must be prescribed from the complete source and remain locally bounded through every covered event. All finite positive-time collision predecessors, with both parities, must be covered.

The source-side differentiation now has an explicit recurrence. For `q=e^{4u}` and `J_k=(D^k theta)(0,iq)`,

\[
 J_k'=\frac q\pi J_{k+2}-(2k+1)J_k
       -k(k-1)\frac\pi qJ_{k-2}.
\]

The last term is the surviving transverse-jet correction. It cannot be removed by first setting the first-order commutator to zero at the zero section. The complete formulas for `Phi'` and `Phi''` in the correlation note retain these corrections and cancel the constant theta mode exactly.

## Next research gate

The useful next proposal must use theta information beyond the flat restricted connection. One geometric candidate is to retain transverse variation in `p=Re(tau)` before restriction, where the zero-section curvature is `2*pi*i*q dp wedge dq`, and derive a complete identity with its boundary flux and observation covector. The external spectral variable `x` is not that elliptic coordinate; any relation must be proved with the actual transform.

Before developing a larger geometric construction, require its explicit additional term and remainder to control one of the two displayed signed targets or a uniform strict quarter-turn gap. Apply the same proposal to the established positive-primitive collision controls and identify the arithmetic hypothesis they fail. A positive source norm or vanishing pulled-back curvature does not supply this discrimination. No new theta sign domain, collision exclusion, or RH conclusion has been obtained.

## Review and reproducibility

The [internal continuation review](../../reviews/02_CONNECTION_BRIDGE_AND_INNER_TURNING_REVIEW_20261015.md) records independent comparisons within the LLM-assisted team. The [execution manifest](../../numerics/CONNECTION_BRIDGE_AND_INNER_TURNING_CHECKS_20261015.json) binds the seven replayed scripts, their records, and the research-note versions.

The four initial programs pass their existing **344 assertions**. Three new programs pass **886 assertions**: 35 metric/path checks, 59 signed-transform and jet checks, and 792 finite heat-profile checks. The combined **1,230 assertions** include overlapping finite identities; they are not a count of theorems. The infinite-series convergence, all-multiplicity local theorem and uniformity arguments rely on the written analytic proofs. No interval theta-sign certificate was produced.

The stable manuscript and its PDF/build record are unchanged. This is a set of incremental notes and numerical replay records; no snapshot folder, commit, or tag was created. This conversation is registered as history 18 in the formal replay lane under the standing local override; the investigation's preexisting history 17 is unchanged.
