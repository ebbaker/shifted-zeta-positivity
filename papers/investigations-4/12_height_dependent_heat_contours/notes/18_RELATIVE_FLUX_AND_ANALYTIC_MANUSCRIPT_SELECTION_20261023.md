# Relative flux and the selective analytic manuscript

23 October 2026, America/New_York. Drafted for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Separate contributing and reviewing agents used the same model.

The author's requested “from the book” direction is now the maintained [selective manuscript](../manuscript/book.tex), titled *Heat collisions and relative zero flux*. The [earlier research draft](../manuscript/main.tex) remains intact. The new version selects one continuous argument; it is not a claim of publication readiness or optimal arithmetic estimation. [Internal review](../reviews/15_RELATIVE_FLUX_ANALYTIC_MANUSCRIPT_REVIEW_20261023.md).

Read with the [result index](../../../../result-summaries/README.md), [local heat results](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../avoid/README.md), [target classification](../../../../avoid/01_restating_the_target.md), and [coupled-estimate rule](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The earlier nonreal consumer is stated once and is not itself an RH theorem. The quantitative improvement below is relative to a specified absolute source estimate.

## The selected argument

For a conjugation-symmetric smooth moving window, put
\[
\mathcal R_\psi=N_{\psi,\mathrm{nr}}(a)+F^+_{\psi,\mathrm{nr}}.
\]
The exact balance is
\[
N_{\psi,\mathrm{nr}}(b)+\sum_{a<t_e\le b}2\lfloor m_e/2\rfloor\psi(t_e,x_e)
=N_{\psi,\mathrm{nr}}(a)+F^+_{\psi,\mathrm{nr}}-F^-_{\psi,\mathrm{nr}}.
\]
Here the flux uses the full moving-window derivative. Endpoint coverage gives the sharp bounds D_K≤R_ψ and M_K≤(3/2)R_ψ. A cubic heat collision attains both constants.

The natural boundary is a level window ψ=χ(G) of an analytic reference field. Its smooth relative-current numerator is
\[
A_\psi=\operatorname{Re}\{D\chi(G)(G_tH_z-G_zH_t)\overline{H_z}\}.
\]
For two heat fields the determinant is W=H_{zz}G_z−H_zG_{zz}. The derivative denominator in the reference velocity cancels, even at a critical reference level. For e=G−cH, the one-sided flux is at most
\[
\|D\chi\|_\infty(E_t\mathcal N+E_1\mathcal L),
\]
with a stronger factor for radial χ. The root population and path length have independent anchored analytic bounds. Outer cutoffs, endpoint coverage and carrier zeroth-order terms remain in the formulas.

## The arithmetic refinement

The exact canonical theta summands define a head A_N and the **complete** tail T_N. The reference is the head heat field; the target is unchanged. The manuscript proves
\[
W(H,G_N)=\int_{u>v>0}e^{t(u^2+v^2)}
[A_N(u)T_N(v)-A_N(v)T_N(u)]K_z(u,v)\,du\,dv.
\]
The source difference is strictly positive on u>v because T_N/A_N is strictly decreasing. The proof is a one-line derivative of the exact ratio of two square-source summands followed by summation of positive pairwise differences. Both the source difference and K_z vanish on the diagonal, giving quadratic diagonal cancellation.

For any common symmetric kernel majorant M_z, the ordered absolute bound improves the unordered bound by exactly
\[
2\int_{u>v>0}e^{t(u^2+v^2)}A_N(v)T_N(u)M_z(u,v)\,du\,dv.
\]
It is strictly positive for the displayed minimum majorant. There is no uniform factor of improvement and no sign conclusion for the oscillatory kernel. Positive reweightings of the square terms retain the ordering, so weighted-square collision controls share it. The full coefficient identity and complete tail have not yet yielded a useful height-uniform estimate.

The paper also gives explicit all-tail bounds, a local xi Taylor reference with its exact heat defect, and an Euler-product local anchor. The latter's absolute continuation can force an extremely small backward width. It is not a useful-width theorem.

## Selection and provenance

[Brainstorm Note 07](../brainstorm/notes/07_NONREAL_WINDOW_TRANSPORT_AND_REGULARIZED_CURRENT_20261023.md) supplies the nonreal balance, sharp consumer and fixed-regulator errors. [Note 08](../brainstorm/notes/08_ANCHORED_SMALL_VALUES_AND_EXACT_CURRENT_LIMIT_20261023.md) supplies the exact current limit, anchored chart bounds and symmetric near-real refinement. The new manuscript extends these to moving windows, the reference determinant, mismatch estimates, and the ordered arithmetic source formula. The proofs are included there; this note is the concise research crosswalk.

The Hermite local collision model remains because it proves the balance and sharp constants. Pair-matrix spectral theory, forest filters, coefficient propagation, physical-cap experiments and exploratory numerical tables remain in the earlier draft and their notes: they do not advance this single flux argument. The technical current-limit proof follows the central geometry and arithmetic; finite-regulator stability is an appendix.

**Status: proved in manuscript at its stated finite analytic scope; separate same-model internal review.** The new claims are exact identities, sharp finite multiplicity constants, and scoped arithmetic upper-bound improvements. Useful earlier nonreal discrimination, height-uniform flux size, admissible width and global simplicity remain open. No new numerical campaign or manuscript snapshot folder was created; no commit or tag was assigned.
