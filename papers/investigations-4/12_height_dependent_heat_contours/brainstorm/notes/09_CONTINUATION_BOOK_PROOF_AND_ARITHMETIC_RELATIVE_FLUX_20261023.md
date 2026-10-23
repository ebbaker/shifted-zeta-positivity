# Continuation for the analytic flux paper and high level brainstorm

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. This is a context handoff, not a new mathematical result.

## Start here

The author wants a **high-level brainstorm before the next technical research task**. He has not yet read the newly prepared paper. Preserve room to reconsider the mathematical organization and the choice of reference; the manuscript is a developed proposal, not an author-approved final argument.

The current paper is [Heat collisions and relative zero flux][book], a 12-page selective analytic manuscript. It centers an exact nonreal balance with a flux term and a natural moving boundary defined by a reference heat field. It now includes sharp multiplicity bounds, a complete-field representation, independently sourced finite bounds, and an ordered theta source identity with a genuine improvement over a specified absolute estimate. **Useful high-height size and earlier nonreal discrimination remain open.** No RH theorem or new global simplicity proportion follows.

Read this note first, then the [current OBF progress register][progress], the paper's first three sections, and [Review 15][review]. The [selection note][selection] records how the paper relates to the previous research. The original [Continuation 05][old-continuation] is historical: its opening transport/current tasks have since been completed at finite analytic scope. Do not restart them as though they remained unproved.

## The author's priorities

The discussion began with continuing analytic open-boundary research. The author then asked for the results to enter a manuscript, with a separate selective version aimed at a proof “from the book” in the sense of Erdős. The earlier manuscript is the first research draft from which to select; a result should enter the selective paper only if it belongs in its coherent argument.

The subsequent directions were explicit:

- Center the paper on the most elegant formula, including a flux term and a natural boundary, ideally moving with the heat flow.
- Estimate its terms as effectively as possible using actual **theta or xi arithmetic information**.
- Characterize the results as optimally as possible subject to elegance. Sharp constants, exact cancellations and clean hypotheses matter; length or the number of auxiliary results is not the objective.
- Keep analytic results primary. Numerical work is supporting work for a stated analytic question.

The author has now requested this handoff for a high-level brainstorm. Preparing it does not authorize starting a separate chat or silently continuing into another research campaign. In the next conversation, first discuss the central object, the available arithmetic information and what an optimal useful statement should mean.

## Where the work lives

The research checkout is `/Users/ebbaker/Documents/shifted-zeta-positivity`. This investigation is `papers/investigations-4/12_height_dependent_heat_contours/`; exploratory work and this continuation belong in its `brainstorm/` subfolder. The originally supplied `/papers/brainstorm/investigations-4/notes/05_...` link was obsolete; the files were relocated to this investigation's brainstorm home. The [relocation receipt][relocation] explains the corrected affiliation.

| Item | Role |
| --- | --- |
| [manuscript/book.tex][book] | Current selective paper; the source open in the author's editor |
| [manuscript/main.tex][first-draft] | Preserved first research draft with spectral, coefficient, contour and finite computational material |
| [Manuscript guide][manuscript-guide] and [build record][build] | Two versions, compiler validation, source/PDF identity and 12-page rendering record |
| [Note 18][selection] and [Review 15][review] | Selection/provenance and detailed mathematical/control checks |
| [Brainstorm Note 07][note07] | Finite nonreal transport, sharp consumer, approximation and carrier requirements |
| [Brainstorm Note 08][note08] and [Review 03][review08] | Exact current limit, anchored analytic bounds, complete-source allowance and near-real refinement |
| [OBF register][progress] | Sole detailed owner of OBF-01 through OBF-06 |
| [Research reset, Note 16][reset] | What the broader first-draft program did and did not achieve |
| [Statistical-mechanics brainstorm, Note 06][statmech] | Optional background if the author returns to criticality or forest-response analogies |

The reading PDF is a generated artifact at `output/pdf/height-dependent-heat-contours/book.pdf` under the checkout, ignored by Git. The current source compiled successfully both locally and in the desktop editor; all 12 rendered pages were inspected. The original main source and its five included section files were preserved byte-for-byte in the preceding revision. No Git commit/tag or manuscript snapshot folder was created. The build record describes that checkpoint; later edits can legitimately change it.

## The exact central balance

The physical field satisfies
\[
H_t=-H_{zz},\qquad H(t,\bar z)=\overline{H(t,z)}\quad(t\in\mathbb R).
\]
Assume H is nonzero and jointly holomorphic on a connected complex neighborhood of a compact time-space cylinder. Work on a fixed real interval I=[a,b] and a compact spatial region inside it. Let ψ(t,z) be a smooth, conjugation-symmetric moving window with 0≤ψ≤1 and uniformly compact support. All root sums count spatial multiplicity. At regular roots, the velocity is v=H_{zz}/H_z. Define
\[
N_{\psi,\mathrm{nr}}(t)=\sum_{H(t,z)=0,\ \Im z\ne0}\psi(t,z),
\qquad
F^\pm_{\psi,\mathrm{nr}}=
\int_a^b\sum_{H(t,z)=0,\ \Im z\ne0}
[\pm(\psi_t+\nabla\psi\cdot v)]_+\,dt.
\]
At a real collision (t_e,x_e) of multiplicity m_e, the nonreal loss is 2 floor(m_e/2). With
\[
B_\psi=\sum_{a<t_e\le b}2\lfloor m_e/2\rfloor\psi(t_e,x_e),
\]
the exact formula is
\[
\boxed{N_{\psi,\mathrm{nr}}(b)+B_\psi
=N_{\psi,\mathrm{nr}}(a)+F^+_{\psi,\mathrm{nr}}-F^-_{\psi,\mathrm{nr}}.}
\]
The endpoint convention includes b and excludes a. If ψ_t+u·∇ψ=0, the flux is relative motion ∇ψ·(v−u). A global smooth material velocity is not required for the general changing-window formula.

Put R_ψ=N_{ψ,nr}(a)+F^+_{ψ,nr}. If ψ(b,x)=1 at the real multiple endpoint zeros in a core K, then
\[
D_K:=\sum(m_x-1)\le R_\psi,
\qquad M_K:=\sum m_x\le\tfrac32R_\psi.
\]
Both constants are sharp: the cubic heat field z³−6tz attains them. R_ψ<2 excludes every real multiple endpoint site in K. These finite statements need no RH. RH is an additional reality premise when the consumer is applied to **all** canonical endpoint zeros. Under a complete covering scheme, sublinear total allowances would address almost-all simplicity; exclusion of every exception needs stronger local control.

A double-scale contracting tube h(t)²=h₀²−2t contains the quadratic pair of z²−2t, but the cubic pair enters it at t=−h₀²/4. Its two entering labels pay for the endpoint triple. A natural moving boundary does not make inflow optional.

For a fixed moving-window family,
\[
R_\psi=N_{\psi,\mathrm{nr}}(b)+B_\psi+F^-_{\psi,\mathrm{nr}}.
\]
Extending the initial time backward cannot decrease this exact conservative resource. A larger useful backward width must be justified through better completed estimates or geometry, with the same endpoint target.

## The natural boundary and its cancellation

Take a real-type analytic reference G and a conjugation-symmetric target cutoff χ. The proposed window is ψ=χ(G), with radial transition curves |G|=r. At regular reference points they move with velocity −G_t/G_z; for an exact heat reference this is its own heat motion. Critical reference levels need not admit a regular material velocity, but the smooth formula remains valid.

Write Dψ=ψ_x−iψ_y and
\[
A_\psi=\psi_t|H_z|^2+\operatorname{Re}(D\psi H_{zz}\overline{H_z}).
\]
Then
\[
A_\psi=\operatorname{Re}\{D\chi(G)(G_tH_z-G_zH_t)\overline{H_z}\}.
\]
For two heat fields, the central residual is
\[
\boxed{\mathcal W(H,G)=H_{zz}G_z-H_zG_{zz}.}
\]
The apparent derivative denominator in the boundary velocity cancels. This is the current paper's preferred geometric centerpiece. G=cH makes the relative flux vanish, but gives no independent bound on the earlier nonreal population.

**Localization remains part of the statement.** Either use a bounded spatial domain on whose collar G avoids supp χ at all times, extending the window by zero, or set ψ=ηχ(G) with a fixed compact cutoff 0≤η≤1. In the latter case the extra numerator is
\[
\chi(G)\operatorname{Re}(D\eta H_{zz}\overline{H_z}).
\]
Take the positive part after adding all contributions. Include every component when level sets merge. If χ=1 on |w|≤r_* and |G−cH|<r_* on the endpoint core, the reference window covers its true zeros; the core must lie inside the chosen domain, and η=1 there when used.

For the reference-packet window ψ=χ(G), set e=G−cH. Independent error bounds |e_t|≤E_t, |e_z|≤E_1 give
\[
F^+_{\psi,\mathrm{nr}}\le F^+_{\psi,\mathrm{all}}
\le\|D\chi\|_\infty(E_t\mathcal N+E_1\mathcal L),
\]
where \(\mathcal N\) is the time-integrated complete root count and \(\mathcal L\) the complete root path length in an encompassing compact region. For physical heat fields E_t may be E_2≥|e_{zz}|. For χ(w)=χ₀(|w|²/r²), |e|≤E₀ improves the prefactor to
\[
\min\{\|D\chi\|_\infty,\ 2\|\chi_0'\|_\infty E_0/r^2\}.
\]
For ψ=ηχ(G), this controls the matched contribution; add the positive outer-cutoff flux to bound the whole window. Optimize the entire bound using one common constant c. The population/path bounds can be acquired independently, but are coarse. Small reference error alone does not make the total resource small.

If a nonvanishing real-type carrier B is removed, let f=H/B, g=G/B, λ=B_z/B and c_B=B_t/B+B_{zz}/B. The normalized heat operator is T_B=∂_z²+2λ∂_z+c_B. Its relative determinant is
\[
\mathcal W_B=f_{zz}g_z-f_zg_{zz}+c_B(fg_z-gf_z).
\]
The drift cancels; the zeroth-order term does not. For two normalized heat fields the temporal error requires E_t≤E₂+2‖λ‖E₁+‖c_B‖E₀. A reference heat defect also contributes. These costs must survive any proposed high-height normalization.

## What actual theta and xi information has supplied

The normalization is
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad 8H(0,z)=\xi(1/2+iz/2),
\]
\[
\Phi=\sum_{n\ge1}\Phi_n,\qquad
\Phi_n(u)=(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]
Let A_N=Σ_{n≤N}Φ_n and T_N=Σ_{n>N}Φ_n. The head defines an exact heat reference G_N; H always retains the **complete** tail. The determinant has an exact head–tail kernel
\[
K_z(u,v)=\frac{uv}{2}\{(v-u)\sin(z(u+v))+(u+v)\sin(z(u-v))\},
\qquad K_z(v,u)=-K_z(u,v).
\]
Using the explicit summand ratios proves T_N/A_N is strictly decreasing. Thus
\[
D_N(u,v)=A_N(u)T_N(v)-A_N(v)T_N(u)>0\quad(u>v),
\]
and
\[
\boxed{\mathcal W(H,G_N)=\int_{u>v>0}e^{t(u^2+v^2)}D_N(u,v)K_z(u,v)\,du\,dv.}
\]
There is **no factor 1/2** on this ordered half-plane. Both factors vanish on the diagonal, making their product locally O((u−v)²).

For a common symmetric nonnegative kernel majorant M_z, the ordered absolute bound is smaller than the unordered A_N(u)T_N(v) bound by exactly
\[
2\int_{u>v>0}e^{t(u^2+v^2)}A_N(v)T_N(u)M_z(u,v)\,du\,dv.
\]
This is strictly positive for the manuscript's displayed minimum majorant. The kernel itself is oscillatory and generally complex: the positive source difference does not give a flux sign. The improvement is relative to that comparator, not every possible estimate retaining reference oscillation, and has no proved uniform factor.

The paper also supplies:

- An explicit complete tail envelope from the geometric ratio of n⁴ exp(−πn²e^{4u}), giving derivative allowances E_{j,N}. The ratio is for these envelope terms, not directly for Φ_n. Combined with independently paid N and L, these give a finite relative-flux allowance on a fixed negative-time band.
- A local xi reference G_K=Σ_{k=0}^K(−t)^k H₀^{(2k)}/k!, with exact heat defect d_K=(−t)^K H₀^{(2K+2)}/K!. Its temporal-error form includes the defect once. Negative-time remainders are proved directly under the complete source integral; no positive-time error theorem is continued by assertion.
- A positive anchor at z=0 from the complete theta source, and a local Euler-product anchor away from the critical line. Their finite analytic constants can be very expensive at large height. The Euler anchor's elementary absolute continuation may force an extremely small backward width.

A finite theta prefix does not inherit the full source reflection or an all-real heat regime. Small absolute source tails may dominate an exponentially small high-height field. The exact ordered identity is available for stronger analysis; useful normalized size has not yet been obtained.

## The analytic foundation already in place

The field regulator is
\[
k_\rho(w)=\frac{\rho^2}{\pi(|w|^2+\rho^2)^2}.
\]
The positive flux has the exact finite-scope representation
\[
F^+_{\psi,\mathrm{nr}}
=\lim_{\delta\downarrow0}\lim_{\rho\downarrow0}
\int_I\int\vartheta_\delta(\Im z)k_\rho(H)[A_\psi]_+\,dA\,dt.
\]
The nonreal cutoff is a measuring factor, not part of the moving window. Without it the limit includes all roots, including real motion. Local Weierstrass charts and the checked Parusiński–Rainer root theorem give uniform L^p control, p>1, for nearby levels; hence no excess current is concentrated at the isolated heat collisions. The order of limits matters.

An independent anchor theorem gives root count n_*(α) and path length C(α)R(1+|I|/d) from a holomorphic tube of complex time width d, spatial radius 4R, an upper bound M and a real-time center anchor m>0, with α=m/M. It needs no H_z floor. The constants are finite but not numerically evaluated; the global source-at-zero construction can be extremely poor for a distant band. Fixed-degree and physical-time rescaling are essential.

The same analysis gives a small-value bound W_ψ(r)≤πLr². That absolute-variation bound is not itself the directional flux. Symmetric windows admit a local O(δ²) near-real omission estimate with field-dependent constants. Exact regulator convergence supplies **no uniform finite-regulator bias rate** under degeneration. Fixed-regulator approximation errors worsen as the regulator shrinks, so a fixed source error cannot simply pass unchanged to ρ=0.

## What is open and what the brainstorm should explore

The [progress register][progress] remains authoritative. OBF-01 is established at finite analytic scope. OBF-02 has the exact current limit, anchor and mismatch results, but not useful normalized size. OBF-03 has complete-source allowances and the ordered arithmetic gain, but no useful height-uniform estimate. OBF-04, useful earlier nonreal discrimination, remains open. OBF-05, an admissible height-dependent width with full coverage and a completed comparison, remains open. OBF-06, coefficient crossing transfers or a complete first-jet side estimate, is secondary.

The first inherited global objective is RH-conditional almost-all simplicity, compatible with a sublinear total allowance. Every-zero simplicity is a stronger target. The current paper gives tools for these objectives rather than a new proportion or an exclusion.

The following are **questions for the author-led brainstorm**, not conclusions or a preselected execution plan:

1. **What should “optimal subject to elegance” mean?** The event weights, balance and multiplicity constants are exact or sharp. Arithmetic error rates, reference choice, normalization and admissible widths are not known to be optimal. Which of these would make the next result both useful and conceptually complete?
2. **Which reference makes the geometry and arithmetic cooperate?** The source head is an exact heat solution but loses full reflection. The xi Taylor reference retains exact initial arithmetic but has a heat defect. A normalized or more complete reference may preserve the desired cancellations at a different cost. Compare their total resource, coverage and localization, not only their local field error.
3. **Can the signed determinant or ordered integral be estimated before losing oscillatory cancellation?** The positive ordered source difference and quadratic diagonal vanishing are useful structure; their existence is not yet the desired high-height bound. What additional theta/xi information can control the remaining kernel and the derivative-weighted current?
4. **How should earlier nonreal population and relative flux be treated together?** The balance exposes both. Suppressing one term can leave the other unchanged. A joint arithmetic estimate might be more natural than separately loose bounds, but it must genuinely bound the completed resource.
5. **What boundary is natural for the whole population?** Assess level sets, normalized levels or justified moving tubes while retaining outer height boundaries, merging components and endpoint coverage. A local cancellation cannot pay an omitted population.
6. **What is the smallest decisive analytic deliverable after the discussion?** A useful bound on one prescribed band, a proved asymptotic estimate with the required uniformity, or a scoped obstruction with a matching comparator would advance the program. A new notation for the unknown flux or another uncalibrated finite constant would not.

Do not automatically start a large numerical scan, polish the manuscript before the conceptual discussion, or repeat the completed finite transport audit. The broader spectral/forest/coefficient material is available in the first draft if it supplies a direct missing estimate. Its omission from this paper is editorial selection, not a claim that it is mathematically uninteresting or impossible to reconnect.

## Controls and standards to carry forward

Read the repository [result index][results] and [avoid index][avoid], especially [local heat results][heat-results], [the collision controls][controls], [target classification][a01], [shared-premise screening][a02], [coupled estimates][a12] and [scoped exclusions][a07]. Review 15 contains the detailed control table.

The generic transport and anchor theorems admit collision controls; that is expected. The new source ordering survives **positive reweightings of the square summands**, so weighted-square controls share it. Euler-factor, reflected, primitive-compatible, finite-prime and finite-profile controls rule out various shortcuts based only on shared qualitative or finitely sampled data. A proposed theta-specific estimate must identify the premise or quantitative bound that separates its target from the relevant controls. Full source identification is not already a small event budget.

Do not confuse signed net flux with one-sided nonreal entry, an all-root current with nonreal current, or either with the physical first-jet cap integral. Retain the time derivative of a moving cutoff, outer localization, carrier zeroth-order term, heat defects, omitted labels, repeated crossings and coverage. Do not assume an earlier all-real interval, a hidden separation floor or an unproved small chart constant. Scope limitations are not universal impossibility theorems.

The paper's mathematical status is **proved at stated finite analytic scope with separate same-model internal review**. The review checked primary sources and corrected signs, normalizations and proof details. It is not independent specialist refereeing, formal verification or a priority determination.

## Continuation and history instructions

Use repository [AGENTS.md][agents], [LARGE_FILES.md][large] and [tools/CHAT_HISTORY.md][history-policy]. Research notes belong in this brainstorm's `notes/`, reviews in `reviews/`, and supporting computations in `numerics/`. Update the OBF register when mathematical status changes; HDC status remains in the parent investigation. Cite detailed work rather than expanding milestone histories. Keep all tracked files below 1 MiB and create no manuscript snapshot folders. Do not edit the synced ChatGPT project files under `sources/`.

If later asked to revise the currently open paper, edit the existing `manuscript/book.tex` in place and use the desktop `compile_latex_document` tool on the saved file. Keep its editor open. The present handoff request does not change that TeX source, compile a replacement PDF, or open another tab.

This conversation is **Continue boundary flux research**, thread `01a16acd-c816-7173-b5a2-154812a049c9`, uniquely registered as [brainstorm history 0005][chat]. Preserve its number and filename. A genuinely new brainstorm chat registers its own actual thread identity in this same `brainstorm/chat-histories/` folder; it must not reuse history 0005's identity. The earlier history 0002 and 0003 registrations remain distinct. Refresh the actual conversation at the beginning and end with the repository tool and arrange its bounded exact-turn final capture unless trusted completion hooks have been verified.

A suitable next-chat instruction is:

> Read this continuation and the linked current progress register. Start with a high-level brainstorm with me about the most elegant and strongest useful characterization of the moving-boundary balance. Focus on estimating the full resource using actual theta/xi arithmetic, keeping exact cancellations and the natural heat-flow boundary central. Distinguish sharp established statements from open estimates. Do not begin a numerical campaign or expand the manuscript before we choose the conceptual direction.

[book]: ../../manuscript/book.tex
[first-draft]: ../../manuscript/main.tex
[manuscript-guide]: ../../manuscript/README.md
[build]: ../../manuscript/BOOK_BUILD_RECORD_20261023.json
[selection]: ../../notes/18_RELATIVE_FLUX_AND_ANALYTIC_MANUSCRIPT_SELECTION_20261023.md
[review]: ../../reviews/15_RELATIVE_FLUX_ANALYTIC_MANUSCRIPT_REVIEW_20261023.md
[progress]: ../research-progress/01_OPEN_BOUNDARY_FLUX_PROGRESS_20261023.md
[old-continuation]: 05_CONTINUATION_ANALYTIC_OPEN_BOUNDARY_FLUX_20261023.md
[note07]: 07_NONREAL_WINDOW_TRANSPORT_AND_REGULARIZED_CURRENT_20261023.md
[note08]: 08_ANCHORED_SMALL_VALUES_AND_EXACT_CURRENT_LIMIT_20261023.md
[review08]: ../reviews/03_ANCHORED_SMALL_VALUES_AND_CURRENT_LIMIT_REVIEW_20261023.md
[reset]: ../../notes/16_RESEARCH_RESET_AND_NEXT_STEPS_20261023.md
[statmech]: 06_STATISTICAL_MECHANICS_HEAT_CRITICALITY_AND_FOREST_SUSCEPTIBILITY_20261023.md
[relocation]: ../CHAT_HISTORY_RELOCATION_20261023.json
[results]: ../../../../../result-summaries/README.md
[heat-results]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[agents]: ../../../../../AGENTS.md
[large]: ../../../../../LARGE_FILES.md
[history-policy]: ../../../../../tools/CHAT_HISTORY.md
[chat]: ../chat-histories/0005_2026-10-23T22-07-13Z_continue-boundary-flux-research.json
