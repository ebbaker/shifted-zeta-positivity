# Internal review of the fixed-offset Gaussian and contour theorem

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Two contributing agents checked the Gaussian proof and the flow/control consequences; a third agent separately audited the written note. All used the same model and inherited effort. This is internal LLM review, not specialist validation.

**Assessment:** [Note 18](../notes/18_RH_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_THEOREM_20261023.md) proves the concrete fixed-offset candidate from [Note 17](../notes/17_CONTINUATION_CONSERVED_SPATIAL_CONTOURS_20261023.md), under initial RH with multiplicities allowed, and supplies its first correction and material-flow consequences. No substantive gap was found at that scope. Precision corrections described below have been incorporated. There is no new simplicity conclusion.

## Proof checks

The canonical normalization is H_t=-H_zz and 8F(z)=xi(1/2+iz/2). Evenness eliminates the linear exponential in the paired order-one product; all zeros and multiplicities are retained. The absolute derivative sums converge, and the unit-interval count yields p^(k)=O(log height) for k>=1. Vertical integration from a fixed Euler offset correctly obtains p itself without an unjustified absolute unpaired reciprocal sum. The functional-equation sign, the -i/2 factor, and the gamma derivative in (9) agree. The source conventions were checked against [Elkies](https://people.math.harvard.edu/~elkies/M259.06/zeta2.pdf), whose xi is meromorphic, and [DLMF 25.4](https://dlmf.nist.gov/25.4), [5.11](https://dlmf.nist.gov/5.11). The note explicitly converts Elkies's completion. No sharp zero-count constant is imported.

The global horizontal ratio controls the full normalized Gaussian tail, including shifts to bounded real height and beyond. It divides by F before bounding; there is no missing lower bound on an exponentially small raw xi value. Gaussian domination is uniform for real 0<s<=c/log^2 Y for each fixed c. It has its continuous exact limit at s=0.

The first correction s p'(1+2s p^2) comes from the exact complex Gaussian second moment. The cubic logarithmic error and squared quadratic error contribute O(log^-2 Y). Completing the real square only to bound the remainder leaves the complex leading exponential intact and pays its bounded cancellation cost. A fixed enlarged strip gives honest Cauchy estimates; differentiating a pointwise asymptotic without that margin would not suffice. Nonvanishing follows from the proved relative ratio before the negative-time logarithmic derivative is defined.

The finite-buffer ODE has the correct backward-duration sign. Its O(1/log Y) displacement is smaller than every paid buffer, so the first-exit argument supplies full continuation. The continuous tangent logarithm, right-half-plane tangent, endpoint coverage and first displacement/tangent expansions follow. The material form and primitive image are exactly preserved. This controls the selected branch and escape in a finite rectangle; it neither assumes global properness nor requires avoiding other branches' critical values.

The positive reciprocal-square kernel gives -Im p comparable to log Y on the fixed strip. A sufficiently wide fixed zero-count window pays the lower bound. The O(1) change in the velocity is smaller than that lower bound, giving upward motion as heat time runs backward. The graph slope correction is O(1), so the fixed-x sign is also justified. This is a spatial motion statement, not a relative zero-current or physical three-form sign theorem.

## Corrections and controls

Four precision changes were made during review:

- The primitive is odd; the corrected wording is “the canonical primitive of the even field.”
- A cosine-factor zero has multiplicity at least two in the product, possibly more when it coincides with a zero of F.
- The q=1 Euler-factor control adds aX/pi+O(1) to its total count. Its relevant bounds persist, but it does not have the literal original counting formula.
- The standalone quadratic example at a fixed center is a local shrinking-scale obstruction. To put it in the high-height band one must translate the family with Y. The note now states both scopes.

The stronger control G_0(z)=F(z/2)^2[1+cos((log2)z/4)] was independently checked after these corrections. Scaling the squared field loses X log2/(4pi) in its linear counting term, and the cosine factor restores exactly that term. Thus it has the same two main counting terms as F with O(log X) error, all zeros have even multiplicity, and its fixed-strip logarithmic derivatives obey the same orders. The Fourier source is a convolution of positive even scaled theta densities followed by positive shifts. Convolution and shifts preserve enough superexponential decay for all real heat times. The control therefore passes the full analytic proof with its own constants while having no simple initial zeros.

This distinguishes failure of the exact canonical xi identity from failure of a derived bound: the control fails the former and passes the latter. It excludes a simplicity deduction from this coarse information class alone, not from every theta-specific estimate. The positive-source and weighted-square/reflected comparisons are scoped in the note against the [control register](../../../../../result-summaries/12_collision_controls_and_screening.md). The [avoid index](../../../../../avoid/README.md), especially [02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) and [07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), governs this interpretation.

## Gain, limits and recommendation

The extracted comparison improves the specifically stated one-step additive estimate: it gives a vanishing relative error for every fixed c on the c/log^2 Y clock, instead of an O_c(1) additive error whose elementary nonvanishing test needs small c. This does not claim superiority to every direct method; the proof itself is a direct Gaussian field estimate. The conserved flow transfers the estimate to geometry without adding arithmetic discrimination.

The result is conditional on RH, allows every multiplicity, keeps the offset bounded away from zero, has real time only, and does not provide evaluated constants or a numerical height threshold. It does not pay the earlier interior nonreal population, microscopic real-axis cutoff, one-sided collision resource, or height-end resource budget. The all-multiple control prevents treating these missing inputs as minor technicalities.

Record SCF-01/02 as **completed for the stated fixed-offset subproblem**, with the broader multiplicity-sensitive tasks still open. Keep SCF-03/04 and the overarching simplicity goals open. Retain the proof in notes pending a demonstrated use in the selective book; no automatic promotion into a manuscript. The next estimate should distinguish the all-multiple control and keep the true local cluster factor. Further fixed-offset expansion terms alone do not meet that requirement.

No numerical experiment was needed for this analytic proof. The symbolic Gaussian moments and controls were checked algebraically in the written argument. Reference files and external reading-copy receipts are in the [catalog](../../references/README.md); their hashes certify file identity only. See [Continuation 19](../notes/19_CONTINUATION_AFTER_FIXED_OFFSET_THEOREM_20261023.md).
