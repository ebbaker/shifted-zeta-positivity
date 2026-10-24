# Theorem centered revision of the book

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Contributing and reviewing agents used the same model; this is internal research and editorial review.

The author requested a rewrite around the strongest current result, with **RH implies simple zeros** as the overarching goal, and explicitly requested convenient dated TeX drafts in addition to Git history. The maintained [book](../../manuscript/book.tex), now titled *Conserved heat contours toward simple zeta zeros*, centers the proved fixed-offset theorem from [Note 18](18_RH_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_THEOREM_20261023.md). Its role is an acquired analytic intermediate result. A useful bound on the earlier nonreal population or the complete simplicity resource remains open.

## The argument selected for the book

The opening theorem assumes RH with arbitrary multiplicities. For fixed positive offsets, fixed c>0 and L=log Y, it gives

\[
\frac{H(-s,z)}{F(z)e^{sp(z)^2}}
=1+s p'(z)(1+2sp(z)^2)+O(L^{-2}),\qquad 0\le s\le cL^{-2},
\]

including fixed-order spatial derivative bounds on smaller strips. The proof retains the full complex Gaussian exponential and controls the entire horizontal tail after division by the complete initial field. It does not assume the negative-time floor it derives.

The acquired nonvanishing then supports an actual finite-buffer material flow. It preserves H dz and the primitive image, remains a graph covering the target band, and has displacement and tangent change O(1/log Y). The upward direction is proved for the spatial graph as backward duration increases. It is not a sign statement for zero current.

The positive-source field F(z/2)^2[1+cos((log 2)z/4)] has only even-multiplicity real zeros under RH, shares the two leading zero-count terms, and satisfies the coarse estimates used in this proof. It is included immediately after the contour theorem, with its source convolution and counting calculation. This identifies the information that the new theorem does not distinguish. A translated quadratic heat model separately explains why one cannot send the offset to the microscopic scale through an allowed double without retaining the cluster factor.

## The new bridge to a simplicity estimate

Book Corollary 5.4 is an explicit consequence of combining the acquired wall with the previously proved collision balance. For S=c/(log Y)^2, choose a smooth window

\[
\psi_Y(t,x+iy)=\eta(x)\chi\!\left(y/\varepsilon(x,-t)\right),
\]

where eta is one on [Y,2Y], supported inside the covered extended interval, and chi has fixed thin upper and lower transitions about the material graph. Choose both cutoffs in [0,1], with chi even. The fixed positive-offset nonvanishing theorem puts every point with chi' nonzero inside a zero-free corridor for every t in [-S,0]. At each regular zero the terms containing chi' therefore vanish; only eta'(x) chi Re(v) survives, where v=H_zz/H_z is the root velocity. Consequently

\[
M_Y\le\frac32\left(N_{\psi_Y,\mathrm{nr}}(-S)
                  +\mathcal F_{\mathrm{ends},\mathrm{nr}}^+\right).
\]

Here M_Y counts labels at nonsimple endpoint sites. The earlier population and horizontal-end inward flux retain their complete definitions. A fixed wall within the same acquired corridor would remove the same vertical transition terms; no additional arithmetic gain is claimed merely from material motion. The material velocity H_z/H differs from the root velocity H_zz/H_z.

If the full right-hand resource is at most alpha times total endpoint multiplicity, the simple fraction is at least 1-3alpha/2. Resource o(N) gives density-one simplicity on the covered bands; a resource below two for an individual-site window excludes a multiple zero there. These are conditional consequences of the finite balance. The book acquires none of these resource bounds, and a cumulative assertion still needs height coverage and its low-height exceptions.

## Section crosswalk

| Book location | Purpose | Research basis |
| --- | --- | --- |
| Sections 1 and 2 | State and prove the complete relative Gaussian expansion, floor and derivative estimates | Note 18, Sections 1–3; classical product/count and Euler/digamma inputs |
| Section 3 | Actual conserved graph, finite containment, coverage, tangent and upward motion | Note 18 material-flow argument; the conservation law developed in Note 16 |
| Section 4 | All-multiple positive-source control and the microscopic-offset obstruction | Note 18 and Review 09 |
| Section 5 | Local heat birth, exact moving nonreal balance, sharp multiplicity bounds and the wall-resource corollary | Earlier book and Notes 07–08; new combination with the acquired zero-free corridor |
| Section 6 | State the missing arithmetic estimate and retain the exact coupled current | Earlier reference determinant and full theta prefix–tail identity, now subordinated to the resource target |
| Appendix A | Prove the complete field representation with the ordered rho then delta limits | Earlier current-limit proof and the Parusiński–Rainer root-variation import |

The detailed absolute anchor, source-ordering budget, broad spectral alternatives and numerical background remain in the older dated book, main.tex and their research notes. They are not needed to prove the new main theorem. The positive-time Hermite/joint consumer from Note 12 remains a useful alternative research direction; without an acquired canonical bound on its q statistic, including its full separate proof here would interrupt the present contour-to-resource argument. No discarded route is declared impossible.

The reference-window discussion now explicitly separates a matched field-level window G=cH, whose regular boundary velocity is H_zz/H_z, from material H dz conservation. The full source residual, outer localization and any heat defect are retained before taking a positive part. The field limits apply to each fixed field and fixed smooth window; no uniform high-height or regulator-dependent-window limit is asserted.

## Draft retention and validation

The author's explicit request supersedes the earlier no-draft practice **for this book**. The exact previous book is [draft 01](../../manuscript/book_draft_20261023_01_relative_flux.tex); the revised source is also preserved as [draft 02](../../manuscript/book_draft_20261023_02_fixed_offset.tex). These are small standalone TeX files in the existing manuscript directory. No snapshot folders, commit or tag were created. Future substantial rewrites can retain another dated TeX draft while keeping the concise [milestone index](../../DRAFT_HISTORY.md). The broad working main.tex and its included sections were not edited in this revision.

The [build receipt](../../manuscript/BOOK_CONTOUR_BUILD_RECORD_20261023.json) records exact source, draft and PDF hashes. Both the desktop compiler and local LaTeX build succeeded. The final PDF has 15 pages, no unresolved references or box warnings; all pages were rendered and inspected. [Review 10](../reviews/10_THEOREM_CENTERED_BOOK_REVIEW_20261023.md) records the mathematical integration checks and two incorporated clarity repairs. Compilation and internal review are not independent specialist validation.

## Research status and continuation

The author-requested [new overview](../../research-overview/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRAM_20261023.md) and [progress register](../../research-progress/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRESS_20261023.md) now organize the next work from this milestone; they add no new arithmetic estimate.

SCF-04 is fulfilled as a theorem-centered **intermediate manuscript** milestone. SIMP-03 has a substantive revised manuscript; its stronger eventual simplicity scope remains open. The fixed-offset portions of SCF-01/02 remain proved; SCF-03 and the multiplicity-restricting goals SIMP-01/02 remain open. The book establishes neither RH nor a new simplicity proportion.

The next mathematical work is to bound the complete earlier-mass/end-flux resource or obtain a multiplicity-sensitive near-axis comparison using the actual theta arithmetic. It must explain which premise excludes the all-multiple control and retain all source, carrier, small-value and coverage costs. [Continuation 19](19_CONTINUATION_AFTER_FIXED_OFFSET_THEOREM_20261023.md) still gives the analytic handoff; its earlier statement that the book was untouched is superseded by this author-requested rewrite.

See the [result summary](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [shared-premise warning](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [coupled-estimate discipline](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [SCF register](../research-progress/03_CONSERVED_SPATIAL_CONTOURS_PROGRESS_20261023.md) and [SIMP register](../research-progress/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRESS_20261023.md). This chat retains history 0008 in brainstorm/chat-histories and its existing thread identity.
