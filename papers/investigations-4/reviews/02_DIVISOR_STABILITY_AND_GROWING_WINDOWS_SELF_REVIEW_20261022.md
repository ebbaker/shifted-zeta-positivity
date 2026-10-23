# Divisor stability and growing clock windows: self-review

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded **gpt-6-astra (Codex), effort max**.

**Disposition: the specified fixed-disk C² theorem and growing spatial corollary pass this same-assistant proof audit.** This review is by the assistant that wrote the derivations. It is neither a separate-agent review nor independent specialist validation. No mathematical priority, RH, endpoint-simplicity or acquired exterior-force claim is endorsed.

Sources reviewed: [stability Note 09](../notes/09_SHARP_C2_DIVISOR_STABILITY_20261022.md), [clock Note 10](../notes/10_GROWING_CLOCK_WINDOWS_20261022.md), and the maintained manuscript's [Section 3](../manuscript/zero_count_heat_transport/sections/03_regularization.tex) and [Section 9](../manuscript/zero_count_heat_transport/sections/08_theta_concentration.tex). The targets come from [Continuation 08](../notes/08_CONTINUATION_SHARP_DIVISOR_STABILITY_AND_GROWING_CLOCK_WINDOWS_20261022.md). Historical initial-manuscript checks remain in [Review 01](01_ZERO_COUNT_HEAT_TRANSPORT_MANUSCRIPT_REVIEW_20261022.md).

## 1. Harmonic reproduction and bias

The contour trace uses f′/(f−w); its residues give the full preimage multiplicities. A nonzero boundary floor makes the contour expression holomorphic throughout |w|<b, including critical values. On the disk a harmonic test has a holomorphic real part on a neighborhood. Weighted area followed by angular averaging gives m h(a), without labeled simple branches.

The measure has exact mass m, compact support inside the disk and integrable density at zeros for every p>0. The regularization is C¹,¹ near a positive cutoff level, so critical cutoff points add no interface measure. The multizero test f=z²−1, ε=1, R=2 verifies that this convention remains meaningful at a critical level: the z² trace 2(1+w) averages to 2.

Integrating the root-radius bound against the radial target density gives the factor p/(p+2/m). Cancelling the affine Taylor polynomial leaves half the real Hessian operator norm times that second moment. The monomial and |z−a|² attain the result, including the coefficient. The proof explicitly states R,c>0; this positivity was made explicit during the audit before delivery.

For several disks, the complement floor is retained to avoid omitted measure. The p≥1 optimization solves η/ε≈ε^(2/M), yielding exponent 2/(M+2). For p<1 it solves ηᵖ/εᵖ≈ε^(2/M), yielding 2p/(pM+2). The test remains C_c² for the field-error pairing. No claim that these separate regularization rates are optimal is made.

## 2. Direct perturbation and conditioning

Rouché is an identified classical input preserving the complete count, not a novel counting result. The interior field error and positive unit floor bound every descendant's radius, including repeated roots. The branch of log(g/f) is needed only on a thin boundary collar where |g/f−1|<1. It is single valued there, so contour integration by parts has no unrecorded branch increment.

The residue formula for the sum of displacements has the sign
S=−(2πi)⁻¹∮log(g/f) dz. The perimeter bound is R log[b/(b−η)], with no extra m factor. The summed real Taylor remainder is at most m‖D²ψ‖∞(η/c)^(2/m)/2. No error for f′−g′, root separation, or lower bound for g's unit is used. This proves C2 as stated.

Finite-cluster addition compares only the union unless a complement exclusion is supplied. Fixed θ<1 controls the logarithm for η≤θb. Common amplitude scaling cancels in both ratios. Vanishing boundary floors and merging reference disks are explicitly outside uniformity claims; the example f_d=z²−d² records c=3d/2 and b=3d²/4 on the shrinking disk around d. The logarithmic boundary constant is not called sharp.

## 3. Exact calibrations and information comparison

For m≥2, zᵐ−η has quadratic discrepancy mη^(2/m), zero centroid, and field-supremum error η on the fixed unit disk. For m=1 a translated root and linear test give discrepancy η. These fixed tests have compact smooth extensions independent of η. They calibrate the best exponent over the declared C²-test class, without an algorithmic or unrestricted minimax conclusion.

For g=(z−d)ᵐ, d>0, the exact field error (1+d)ᵐ−1 is attained at z=−1. Its linear discrepancy md confirms the need for the centroid term. Complex perturbations and e^(λz)(zᵐ−τ) check phase independence and nonconstant analytic units with the explicitly paid floor/error data. These are exact analytic controls, not floating-point experiments or interval certificates.

The direct theorem controls a complete disk and compares actual divisors. The older field theorem uses only error on the test support and compares regularized measures. The improved regularization bias uses the original acquired local geometry; the stronger direct rate is not assigned to the weaker field-error contract.

## 4. Spatial clock corollary

The first-moment allowance is independent of K. The finite sign/derivative tests and the zero-free complementary intervals work at each time for arbitrary finite K(t). Z≤πK and 1+Z≤(1+π)K give the sufficient window K=o(L√κ) and uniform unfolded error O(K/(L√κ)).

For the matrix sum, d−2δ≥(1−2δ)d and δ<1/4 give
16δΣ(d−2δ)⁻³≤16ζ(3)δ/(1−2δ)³≤128ζ(3)δ.
There is no factor growing with the block size. Physical scaling multiplies by L²/π², so the absolute physical error is O(KL/√κ); K=o(√κ/L) is the separate sufficient condition for its vanishing. Each comparison is between matrices of the same dimension at that time.

No derivative of K(t) is taken. The cumulative discriminant theorem remains fixed-population; entry/exit terms are not suppressed. BW10 Note 20's covariance, higher moments and variance estimates were read but not imported. The complete centered residual is still unpaid.

## 5. Literature and collision controls

Note 09's comparison gives the inspected locations in Simon's weighted area formula, Beauzamy's local polynomial perturbation bounds, Barlet's opening finite-fiber trace problem, Parusiński–Rainer's coefficient-curve/Sobolev and Wasserstein formulations, and Phong–Sturm's cluster-scale integral theorem. Their norms, output metrics and hypotheses are retained. No source is claimed to state the precise disk-supremum/C² estimate. Demailly's text was unavailable in this round and supplies no new imported claim. The bounded search supports the stated classical-specialization characterization, not priority.

The [collision-control register](../../../result-summaries/12_collision_controls_and_screening.md) supplies a premise screen, not a new computation. Generic divisor stability admits all finite multiplicities and applicable control fields. The canonical clock allowance belongs only to its unchanged displayed source. Euler-factor, weighted-square/finite-prime, reflected/positive-primitive, and normalized endpoint controls fail respectively that source, full reflection, the unchanged square expansion, and ordinary Dirichlet arithmetic. No qualitative late-clock conclusion separates all colliding sources.

## 6. Integration and verification

Proposition 3.5, Theorem 3.6 and Corollary 9.4 are added to the maintained project; the smooth-kernel proposition is now 3.7 and cumulative cancellation is 9.5. Front matter, introduction, conclusion, theorem map, overview, ledger and milestone history have matching scope. Earlier notes retain their historical text with completion pointers. New research belongs to base chat 0010; no earlier archive is relocated or reused.

The final build and file checks are recorded below. These establish document consistency and source/output identity, not mathematical validity or independent review. No new numerical sweep, certificate, manuscript snapshot, Git commit or tag was created. ZHM-10's fixed-geometry target and the short spatial extraction are complete; ZHM-09 and ZHM-11 remain open. Specialist review of the compact core remains recommended and unperformed.

### Final build and presentation receipt

Both the desktop editor compiler and latexmk/pdfTeX (TeX Live 2023) succeeded. The delivered PDF has **44 pages, 608,383 bytes**, with no final LaTeX warnings, overfull/underfull boxes, unresolved references/citations or duplicate labels. All 227 labels are unique and every source reference resolves; extracted PDF text has no unresolved-reference markers.

All 44 pages were rasterized and visually checked in contact sheets. New proof pages 8–10 and 39–40 were also inspected individually. The final explicit-positive-constant clarification changed only rendered pages 8–9, which were checked again. No clipping, overlap or missing glyphs was observed. Local links in the updated Markdown records resolve, and their whitespace checks pass. The [build record](../manuscript/zero_count_heat_transport/BUILD_RECORD.json) binds all eleven TeX sources and the delivered PDF by SHA-256. Temporary build products and page images remain outside the repository; every delivered file is below 1 MiB.
