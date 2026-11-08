# Full Gaussian marginal manuscript author check

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual recorded model/effort
unavailable, authenticated chat0003. This is the proof author's check,
not a separate assessment, independent review or specialist review.

**Mathematical status: preliminary derivations, proof-author checking
only; separate E07 assessment pending.** Accepted E02 input remains
accepted at its existing internal level. E03/E04 stay pending on their
original source bytes. The manuscript rewrite changes emphasis and adds
results; it does not promote earlier sources.

## Claim checks

| Claim | Check and scope |
| --- | --- |
| Full N-coordinate law and k-marginal | Integrating N-k Gaussian factors leaves (N-k)! copies of each ordered distinct tuple. The factorial density has mass (N)_k, not one. |
| Soft localization | Independent thinning has random count. Its factorial mixture is weighted by (m)_k Pr(M=m); separately normalized weighted k-tuples are not generally consistent fixed-size marginals. |
| Self subtraction | Expanding the product of first intensities produces w_j² self terms. Multiplicity m leaves m(m-1) coincident-position ordered pairs. No geometric-diagonal deletion. |
| Generating functional and order tail | Finite product expansion gives every order; Z_k<=M_W^k and the exponential tail give the stated bound. This is not a dynamical closure. |
| Gaussian smoothing and bias | tau=epsilon²/2 yields the planar heat kernel; semigroup contraction gives the weak bias. Density convergence to an atomic measure is not claimed. |
| Spatial tails | Union over an omitted index slot gives k M_W^(k-1)T, with A_e^k for sup norm. Requires finite total weight. No untruncated Gaussian-window canonical tail was acquired. |
| Center and separation | Both coordinate maps have unit absolute Jacobian; the difference of two width-e observations has width sqrt(2)e. Integrating the full complex center discards a common transverse mark. |
| Real-zero benchmark | Both imaginary Gaussian factors remain, while the real spacing sum is nonzero. The primary correlation is not an all-real vanishing statistic. |
| Center law and unfolding | A compact declared center probability law gives a mixture; Jacobian J_X^k preserves factorial mass. Physical isotropic smoothing becomes anisotropic after unequal unfolding scales. |
| Connected pair | Averaging r_X*r_X-d_X and subtracting the two means gives Cov_pi(r_X,r_X)-E_pi d_X exactly. This identity supplies no covariance cancellation. |
| Circular benchmark | The joint density is normalized by Fourier orthogonality, not assumed for theta. The finite kernel and fixed-separation limit are derived. |
| Two-disk support | Squared-radius buffer is exactly 1015/9216>0 for h<=1. theta_++theta_-=1 and both equal 1/2 on the axis, so real labels survive once. |
| Reflected source estimate | H0 and the exact finite cosine source are real entire. Conjugating the multiplier and disk preserves delta, the anchor and E_X. No negative-real-part Euler product is used. |
| Population | Each of the two larger disks has <=n_X labels, so 2n_X is a valid upper bound, including overlap and all approximant collar weights. |
| Derivatives | |P'|<=15/8, |P''|<=6; partition and vertical-cutoff derivative supports are disjoint. Squared-cutoff horizontal cost is 609/(8h²), vertical 609/32<1536. Gaussian gradient is a Euclidean norm. |
| Uniform full-pair error | One-point cost E_X U/pi, product bound 4n_X A times that cost, and diagonal cost E_X V/pi yield the theorem. It controls all observed u,v, since compactness is in the source zero variable. |
| Small-width and center scope | AU,V=O_h(epsilon^-6); no optimality claim. Compact-center averaging integrates J_X² times the error. Sup norm does not alone imply global L¹ control. |
| Canonical precision | Both complete-source tails are retained. Finite cutoff existence pays approximation error only; no canonical profile or practical evaluator is supplied. |

The new proof uses the accepted E02 approximation directly. It does not
use the unassessed B02 harmonic obstruction or B04 scalar-pair theorem
as a premise. Those earlier results remain in supporting appendices.

## Controls and corrections

The cluster12 families were screened at the level of premises, as
recorded in Note09 and manuscript §8. Generic marginal identities must
also hold for collision controls; the source specialization requires the
unchanged complete theta source and its anchor. Neither success on a
toy configuration nor failure of a control's arithmetic premise estimates
the canonical correlation. The original collision certificates were not
rerun, and no numerical RH evidence is claimed.

The exact bookkeeping record independently enumerates the retained-count
mixture for weights (1,1/2,1/3), checks the weighted self subtraction
against direct distinct-label sums, and rejects the incorrect linear-weight
self correction. It also checks multiplicity coefficients and the rational
support/derivative constants. These calculations support transcription;
the analytical proofs carry the results.

One inherited control-table sentence was corrected during integration:
real double zeros no longer have zero weight for the primary object.
They remain counted by the full pair function. The earlier sentence
applied to the scalar projections only. The revised table retains the
control's actual failed arithmetic premise.

**A scalar projection does not determine the full pair function.**
**Uniform approximation of that function does not determine its canonical
profile.** The rewrite resolves the first scope mismatch and explicitly
leaves the second analytical question open. These sentences are not
universal exclusion results.

## Production record and disposition

The source proofs, bibliography, cross references, exact bookkeeping,
PDF compilation and visual inspection are recorded in the current
[build record](../manuscript/BUILD_RECORD.json) and
[E06 validation](../numerics/08_TND_OC_E06_MANUSCRIPT_VALIDATION_20261108.json).
The earlier E05 return remains the historical 26-page milestone; the
stable current PDF and build record are replaced by this rewrite.
No manuscript snapshot directory was created.

E06's derivation and manuscript work is complete at proof-author-check
level. E07 should assess the new fixed claims and their E02 interface,
allowing one bounded correction. A substantive change to the primary
object, source, center law or time regime returns to conceptual task B06.
