# Review of the book, supporting program and near-axis continuation

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. The main assistant and three contributing/reviewing agents used the same model. This is internal same-model review, not independent specialist refereeing or formal verification.

## Assessment

No blocking mathematical gap was found in the current [book.tex](../manuscript/book.tex). Its strongest completed result is the RH-conditional fixed-positive-offset Gaussian comparison and the actual conserved spatial graph. The exact collision balance is a valid consumer, and the book correctly leaves the multiplicity-sensitive arithmetic estimate open. Its selective theorem/proof structure is appropriate for the author's intended role for the book. The broader [main.tex](../manuscript/main.tex) remains a repository of useful facts, references and finite checks.

The requested [overview](../research-overview/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRAM_20261023.md) and [progress document](../research-progress/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRESS_20261023.md) accurately identify the next task. Their distinction between a completed outer wall and an unbounded interior resource is essential. The near-axis branch was executed in [Note 19](../notes/19_NEAR_AXIS_CLUSTER_AND_QUADRATIC_EXTERIOR_20261023.md). It acquires a quantitative transfer estimate, but does not complete the canonical multiplicity-sensitive goal.

All manuscript sources and existing build records were left unchanged. No Git commit was made. The review read the analytical sources; it did not rebuild the PDFs or rerun the earlier Arb certificates, and does not renew those numerical certificates' validation status.

## Findings for a future authorized manuscript edit

1. **Missing nonvanishing symbol in the broader manuscript.** In [transport_reference.tex](../manuscript/transport_reference.tex), lines 103–105, the reference hypothesis is literally split into `$G(u,w)` and `e0$`. The intended condition is $G(u,w)\ne0$ on the whole time–wall cylinder. This matters because the following wall quotient divides by $G$. The surrounding proof makes the intended assumption recoverable, but the displayed hypothesis should be restored before circulation. It was not changed in this task.
2. **The broader manuscript's status narrative is behind the book.** [outlook.tex](../manuscript/outlook.tex), lines 24–39, describes acquiring the canonical contour comparison as the next task, although book Theorems 1.1 and 3.1 now establish the fixed-offset version. The opening and conditional graph discussion in [conserved_contours.tex](../manuscript/conserved_contours.tex) should eventually be cross-referenced to that precise completed scope. Its statements are historical/local scope declarations, not refutations of the book. No general global graph or simplicity result has been acquired, so those caveats remain necessary.
3. **Instructions versus historical preferences.** The overview/register contain prior manuscript-promotion and dated-draft directions. The current explicit instruction forbids manuscript updates and Git commits; no promotion or snapshot was made. Historical chat-identity paragraphs belong to their originating chats and were not reassigned to this chat.

These are the actionable source/status findings. The first is a mathematical-hypothesis transcription defect in the auxiliary manuscript; neither establishes a defect in the book's principal theorem.

## Detailed book checks

| Source region | Checked reasoning | Assessment and limit |
| --- | --- | --- |
| Lines 165–276 | Paired order-one product, $H$-coordinate zero count, Euler/digamma anchor, and the global $F$-normalized Gaussian tail | The tail is paid relative to the small complete field, not merely absolutely. Multiplicities remain allowed. |
| Lines 278–356 | Complex Gaussian moments, first correction, fixed-margin Cauchy derivatives, acquired floor | Orders and normalizations check. Constants depend on fixed offsets and margins; no limit to the axis is licensed. |
| Lines 366–477 | Finite-buffer ODE, horizontal coverage, tangent estimate, $H\,dz$ and primitive conservation, upward motion | Correct within the real $c/L^2$ clock and fixed offsets. Nonvanishing is acquired before the velocity quotient is used. |
| Lines 494–558 | All-multiple field $G_0$, source convolution, logarithmic bounds and both count terms | The cosine term exactly restores the linear count term lost by scaling. The control genuinely shares the estimates consumed by the contour proof. |
| Lines 688–743 | Hermite splitting, event finiteness, one-sided balance and sharp multiplicity conversion | The endpoint event costs $2\lfloor m/2\rfloor$, and the cubic attains $M=3R/2$. |
| Lines 774–807 | Smooth outer transitions and horizontal-end resource | Zero-freeness removes the upper/lower transition contributions; it does not remove earlier nonreal population or end influx. A fixed wall in the same corridor has the same resource reduction. |
| Lines 872–919 | Reference determinant, heat defect, localization and antisymmetric prefix–tail kernel | Signs and factors check. The positive part must follow the coupled sum, and a small absolute tail is not a high-zero relative error. |
| Lines 981–1038 | Weierstrass charts, nearby-level variation, area formula and ordered regulator limits | Correct for fixed analytic field/window. Uniformity in height or regulator-dependent windows is not supplied. |

The imported nearby-polynomial-root theorem was checked directly in Parusiński–Rainer, *Optimal Sobolev regularity of roots of polynomials*, Theorem 1, printed page 1344 ([author-hosted published paper](https://math.univ-cotedazur.fr/~parus/publis/ens.pdf), [DOI](https://doi.org/10.24033/asens.2376)). It supplies uniform $W^{1,p}$ derivative control for continuous roots of monic degree-$n$ polynomials with $C^{n-1,1}$ coefficients, for $1\le p<n/(n-1)$. The finite holomorphic-chart application uses an admissible $p>1$ and retains physical chart-length factors. This was an import check, not an audit of the full published proof. The source is now indexed in the investigation's [reference catalog](../references/README.md).

## Review of the new estimate

Two separate agents checked the full proof in Note 19; another checked the Gaussian algebra and polynomial diagnostic. The following points are decisive:

- The complete cluster includes every root in the fixed-radius interval, with multiplicity. Its exterior factor is nonzero at the center even when the center is a multiple zero.
- Translating and deflating the order-one product gives a global exterior bound. This pays the entire Gaussian tail without an assumed local floor and without dropping exterior roots.
- The exterior second logarithmic derivative is nonpositive. Retaining it gives the exact finite-polynomial transform with $d=1-2sB\ge1$ and effective time $s/d$.
- The absolute Gaussian tilt is performed on the original horizontal line. Its real mean is distinct from the complex argument in the explicit polynomial formula; no unproved contour translation of the full field is used.
- A separate proof check verified the elementary Chebyshev restricted-range argument for complex polynomials, including degrees zero and one. It removes the coefficient-majorant loss without importing a polynomial-norm theorem.
- The self-contained Gaussian polynomial lemma bounds the local cubic error by $C(m+1)^{3/2}L^{-2}\mathcal E_s$. The degree cost remains controlled for $m\le C_rL$. The complete tail contributes $Ce^{-\kappa L^2}\mathcal E_s$.
- At $s=0$, a vanishing cluster polynomial makes both fields and the absolute envelope vanish; no division is used. At $s>0$, the absolute envelope is positive.
- The finite real-rooted polynomial array proves an order-one omission error for a linear exterior carrier using the stated coarse information alone. It is not a canonical theta counterexample. Sharper local counts, smaller-degree regimes and stronger arithmetic inputs are outside that negative conclusion.

The [small rational calculation](../numerics/10_QUADRATIC_CLUSTER_DIAGNOSTIC_20261023.json) confirms the declared finite examples of that polynomial diagnostic. It neither certifies theta zeros nor establishes the asymptotic theorem; the latter has an analytical proof in the note.

The $O(L^{-1/2})$ error is relative to the **absolute Gaussian integral of the model integrand**, not to the comparison field. The theorem therefore does not imply a model floor or a zero-count comparison. $G_0$ passes all its consumed inequalities. No new simple-zero proportion, per-site exclusion or useful upper bound on $\mathcal R_Y$ is established. This is partial progress on the near-axis transfer task, with the arithmetic discrimination and its complete consumer still open.

## Research discipline and next decision

The [result summaries](../../../../result-summaries/README.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md) and [avoid index](../../../../avoid/README.md) were consulted before continuing. In particular, the result is classified according to [avoid/01](../../../../avoid/01_restating_the_target.md), tested on shared-premise controls under [avoid/02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), and its negative conclusion is limited as required by [avoid/07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The next mathematical decision should concern an actual multiplicity-sensitive estimate for the cluster or complete resource. Refining the generic Gaussian transfer alone cannot meet that objective. Any proposed root-count use of Note 19 must acquire the model-boundary margin relative to the stated absolute Gaussian envelope; any resource use must retain earlier mass, one-sided end current and height coverage. The present review recommends retaining the result in research notes until that stronger consequence exists and the author explicitly authorizes a manuscript change.
