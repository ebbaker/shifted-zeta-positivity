# Continuation: sharp zero-count stability and growing clock windows

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

**Subsequent completion, 22 October 2026:** [Note 09](09_SHARP_C2_DIVISOR_STABILITY_20261022.md) proves the fixed-disk C² candidates with a stronger bias coefficient; [Note 10](10_GROWING_CLOCK_WINDOWS_20261022.md) extracts the growing spatial clock corollary. The historical text below is retained; its candidate/open or fixed-rank-only wording describes the earlier checkpoint. Continuation provenance: gpt-6-astra, effort max; same-assistant self-review only.

**Recommendation:** characterize the central analytic result first. The next substantive task is **ZHM-10: sharp stability of weighted divisors under analytic field perturbations**. A short growing-rank consequence of the existing theta bounds should be extracted alongside it. A genuinely stronger source estimate for the complete exterior force or signed physical boundary comes afterward.

This is a continuation and prioritization note. The C² estimates proposed below are research targets, with proof routes and exact tests; they have not been added as proved theorems to the manuscript. The growing-window observation in Section 3 is a direct consequence checked here from the existing explicit finite inequalities. No RH, endpoint-simplicity or priority claim is made.

## 1. Starting point and reading path

The maintained [41-page manuscript](../manuscript/zero_count_heat_transport/README.md) contains self-contained local energy, divisor, transport, pair-matrix and theta-concentration results. Read its Sections 2–3, 6 and 9, the [internal review](../reviews/01_ZERO_COUNT_HEAT_TRANSPORT_MANUSCRIPT_REVIEW_20261022.md), the [extensions note](07_LOCALIZED_ROOT_COVER_ENERGY_AND_MANUSCRIPT_EXTENSIONS_20261022.md), and the [base progress register](../research-progress/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRESS_20261022.md). Earlier ZHM-01–08 retain their completed scope; ZHM-09–11 remain open.

Use the [result index](../../../result-summaries/README.md), especially [cluster 13](../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), and the [avoid index](../../../avoid/README.md). Relevant patterns are [01: restating the target](../../../avoid/01_restating_the_target.md), [12: separate versus coupled estimates](../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [13: a factor is not the target](../../../avoid/13_a_factor_is_not_the_target.md), [16: unchecked imports and novelty](../../../avoid/16_unchecked_imports_and_novelty_claims.md), and [20: expansion without a quantitative gain](../../../avoid/20_volume_without_a_gain.md).

The numerical appendix uses an existing RHE04 certificate only. No fresh numerical campaign is needed for the next tasks. Keep the working manuscript in this base folder; no Investigations 5 move is needed yet.

## 2. First substantive task: characterize the C² stability rate

The present compact regularization has field error O(η/ε), while the bias estimate uses only a Lipschitz test and gives O(ε^(1/M)). Their separate optimization yields O(η^(1/(M+1))). This is a valid upper estimate, explicitly not an optimality theorem. The actual consumers are C², and analytic root clusters have moment cancellation that those separate absolute estimates do not use.

### 2.1 Harmonic reproduction and a sharper regularization bias

Work on a fixed disk D(a,R), with f holomorphic on a neighborhood of its closure, exactly one zero a of order m, and boundary floor b>0. For 0<ε<b, test whether the compact regularized divisor satisfies

\[
 \int_D h\,d\mu_{\varepsilon,p}(f)=m h(a)
 \qquad(p>0)
\]

for every real harmonic h on a neighborhood of the closed disk.

The suggested proof is target-space radial averaging of the holomorphic trace over the m preimages of f(z)=w. Define the trace by a contour integral, so no labeling or simplicity of those preimages is assumed. Its harmonic mean should remove the linear Taylor term exactly.

Then, under the paid local floor |f(z)|≥c|z−a|^m, seek the C² bias bound

\[
 \left|\int_D\psi\,d\mu_{\varepsilon,p}(f)-m\psi(a)\right|
 \le \frac m2\|D^2\psi\|_{\infty,D}
                  (\varepsilon/c)^{2/m}.
 \tag{C1}
\]

Here the Hessian is the real two-dimensional Hessian, with operator norm. A stronger explicit coefficient may follow by integrating the radial second moment; first establish the conservative bound (C1). The support lies inside the disk and the exact mass is m. State all cutoff and neighborhood hypotheses, including nonregular cutoff levels.

If proved, separate optimization with the existing field allowance would improve the upper exponent to 2/(M+2). That still need not be the best estimate available with the same acquired local geometry.

### 2.2 Main target: a direct weighted-divisor perturbation theorem

Retain the disk and its known single cluster, assume

\[
 |f(z)|\ge c|z-a|^m\quad(z\in\overline D),\qquad
 b=\min_{\partial D}|f|>0,
 \qquad\|f-g\|_{\infty,\overline D}\le\eta<b,
\]

with both fields holomorphic on a neighborhood of the closed disk. Let the m zeros of g inside D, counted with multiplicity, be ζ_1,…,ζ_m. The concrete candidate estimate is

\[
 \left|\sum_{\nu=1}^m\psi(\zeta_\nu)-m\psi(a)\right|
 \le |\nabla\psi(a)|\,R\log\frac b{b-\eta}
  +\frac m2\|D^2\psi\|_{\infty,D}
                    (\eta/c)^{2/m}.
 \tag{C2}
\]

A proof should establish the following points explicitly:

1. Rouché preserves the complete cluster count; it is used as a classical input, not presented as a new counting theorem.
2. Every zero of g lies within (η/c)^(1/m) of a.
3. On the boundary, g/f lies in the disk centered at 1 of radius η/b<1. A holomorphic logarithm exists on a sufficiently thin boundary collar, and its boundary values have size at most log[b/(b−η)].
4. The contour trace of the sum of zero displacements can be integrated by parts to bound its modulus by R log[b/(b−η)].
5. Apply the real Taylor formula to the sum of ψ values. Bound the linear term using the sum of displacements, not the sum of their absolute values.

The desired consequence is an explicit fixed-geometry rate
O(η^min(1,2/m)). Extend it to finitely many disjoint clusters by addition, retaining each local constant. Do not assume a lower bound for the analytic unit of g or a separation between its split roots unless the proof actually needs one.

This has a stronger information contract than a field error known only on the support of one test function: the entire disk, its boundary and the unit floor are controlled. Compare under matched information. In particular, do not claim that (C2) improves Theorem 3.2 under exactly its weaker assumptions.

### 2.3 Exact calibrations and acceptance criteria

For m≥2, f(z)=z^m, g(z)=z^m−η with η>0, and ψ(z)=|z|² give

\[
 \sum_{g(\zeta)=0}\psi(\zeta)-m\psi(0)=m\eta^{2/m}.
\]

This is an exact exponent test, not a numerical experiment. For m=1 a linear test and a translated root give order η. Linear tests with translated clusters check the necessity of the centroid term. Use smooth compact extensions of these tests when comparing against the manuscript's compact-test formulation.

Also check nonconstant analytic units, complex perturbations, amplitude rescaling, and approaching cluster boundaries. Under common multiplication of f and g by A≠0, c, b and η all scale by |A|; the ratios in (C2) should retain their meaning. A shrinking boundary margin is a real conditioning cost. No claim of uniformity across merging clusters is allowed without a new cluster-level hypothesis.

**Success:** a complete proof or a counterexample for the stated class, explicit constants, an exact exponent calibration in the declared norm, and a comparison with classical root perturbation results. A clean identification as a useful specialization is an acceptable outcome. Do not assert algorithmic or minimax optimality from the scalar potential's 1/ε Lipschitz constant.

## 3. Quick extraction: the existing bounds permit growing clock windows

The final scope paragraph of manuscript Section 9.3 was too restrictive in saying that every growing-rank regime requires a new uniform estimate. Its finite tests already display their dependence on K. The wording was corrected without changing the theorem's fixed-rank statement.

Fix 0<β<π/4, allow an integer-valued K=K(t), and retain

\[
 Z=(K-\tfrac12)\pi+\beta,\quad
 \epsilon_0=ZM_1/L,\quad
 \epsilon_1=(1+Z)M_1/L.
\]

Whenever ε_0<sin β and ε_1<cos β, the existing sign and derivative proof applies at that time to all first K roots. It gives

\[
 \max_{j\le K}|Lx_j-(j-\tfrac12)\pi|
 \le\arcsin\epsilon_0.
\]

Because the explicit M_1 is O(κ^(-1/2)) independently of K,

\[
 K(t)=o(L\sqrt\kappa)
 \tag{C3}
\]

is sufficient for the uniform unfolded location error to tend to zero. This uses the existing concentration estimate; it is not a new saddle theorem.

For any contiguous block ending by rank K, put δ=π^(-1)arcsin ε_0<1/4. The finite matrix estimate gives

\[
 \|\mathcal L(y)-\mathcal L_*\|_{\rm op}
 \le16\delta\sum_{d=1}^{m-1}(d-2\delta)^{-3}
 \le\frac{16\zeta(3)}{(1-2\delta)^3}\delta
 \le128\zeta(3)\delta.
 \tag{C4}
\]

The constant is independent of the population size. Thus the normalized matrix error is O(K/(L√κ)). At each time this compares matrices of the same potentially growing dimension. An absolute physical-matrix error tending to zero needs the stronger sufficient condition K=o(√κ/L), because the physical scaling contributes L²/π².

**Next bounded deliverable:** write this as a short explicit corollary, check every constant, and update the manuscript's fixed-rank/growing-rank distinction consistently. Do not turn (C3) into PCC/GUE statistics, an endpoint-simplicity statement, or a new exterior-force estimate.

Changing the population in time creates entry/exit terms. The fixed-m cumulative discriminant identity cannot be extended merely by substituting m(t). Also read [BW10's differentiated saddle note](../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md) before proposing a new spatial or velocity estimate. Its stronger inputs require their own explicit import audit; they are not supplied by the first-moment theorem alone.

## 4. Bound the prior-art question before expanding the manuscript

A bounded primary-source triage identified these exact comparison points:

| Source | Verified relevant material | Comparison required |
| --- | --- | --- |
| [Leon Simon, Introduction to Geometric Measure Theory](https://web.stanford.edu/class/math285/ts-gmt.pdf), Ch. 2 §3, (3.4)–(3.5), pp. 53–54 | Weighted area formula counting inverse images | The localized power-energy identity is a holomorphic specialization after constant valence is proved. |
| [Jean-Pierre Demailly, Complex Analytic and Differential Geometry](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), III-(2.15), pp. 143–144 | Logarithmic potential represents the divisor current | Distinguish classical divisor/regularization structure from the explicit compact cutoff and stability allowances. |
| [Bernard Beauzamy, How the Roots of a Polynomial Vary with its Coefficients](https://doi.org/10.4153/CMB-1999-001-6), 1999, Theorems 1 and 4; §3 | Explicit local polynomial root perturbation in a coefficient norm; multiplicity-sensitive root scale | Match the norm and information contract. A nearby-root statement is not automatically a complete-cluster or weighted-test theorem. |
| [Phong–Sturm, Algebraic estimates, stability of local zeta functions, and uniform estimates for distribution functions](https://annals.math.princeton.edu/articles/11641), 2000, §2 Theorem 1, pp. 281–282 | Uniform rational-integral estimates using root cluster scales | Relevant if the program seeks uniform singular-energy estimates through merging clusters; retain their degree, root-location and exponent conditions. |

The first two are author-hosted texts. The Beauzamy full publisher text and the Phong–Sturm journal text were inspected in the delegated triage; the latter is also available at the [EMIS journal mirror](https://www.maths.tcd.ie/EMIS/journals/Annals/152_1/phong.pdf). This is a starting bibliography, not a comprehensive originality search. No cited source is asserted to prove (C2) in its precise holomorphic-field/C²-test form.

Before calling the strengthened statement new, check the relevant roots-as-measures, holomorphic traces and perturbation literature under the same assumptions. If the statement is already known, cite it and characterize the explicit constants/application rather than multiplying representations.

## 5. Later source and cap work

After the stability characterization and short spatial corollary, return to ZHM-09 only with a specified norm and growing-window regime for the **complete centered exterior residual**. Keep all omitted-root/unit and normalization terms. A residual reconstructed from already-known root velocities is a consistency check; a useful independent estimate should be derived from the source and pay its time derivatives.

ZHM-11 needs a fully declared physical boundary and every closing face. The exact imaginary-time closure formulas show why a vanishing projective side or a simple terminal population alone is insufficient. RHE's already positive fixed-window trace is not a new negative-witness opportunity.

Use the [collision-control register](../../../result-summaries/12_collision_controls_and_screening.md). Generic local stability and transport theorems must remain valid for collision controls. The unchanged theta-source premise excludes Euler-factor modifications; weighted-square and finite-prime controls fail full reflection; reflected/positive-primitive controls lack the unchanged square expansion; normalized endpoint controls fail ordinary Dirichlet-series arithmetic. None of these distinctions supplies a favorable theta sign without an estimate.

Once the standalone theorem's scope, conditioning and prior-art relationship are clear, obtain specialist review of that compact core before considering a broader manuscript expansion or moving the next research phase to Investigations 5. This is a recommendation, not a message sent to a reviewer.

## 6. Instructions for the next research session

1. Read the sources and scope rules in Section 1; preserve the existing manuscript and unique history registration.
2. Audit the candidate harmonic reproduction, C² bias and direct estimate (C2). Keep exact boundary, interior and unit data visible.
3. Test the constants and exponent against the exact monomial/translation controls before using numerics.
4. Compare the result with primary literature under matched hypotheses. Record proved, inherited, conditional and unproved items separately.
5. Integrate only a completed quantitative gain or precisely scoped counterexample. Keep the new work in base notes, with its review in base reviews; update the existing overview/progress and edit the maintained manuscript in place.
6. Extract the growing-clock consequence (C3)–(C4) as a short separate corollary. Keep temporal population changes and the full-force problem separate.
7. Finish the bounded round with a proof or scoped failure, source comparison, concise manuscript changes if warranted, and an updated research ledger. Do not start a numerical sweep or declare an RH/exclusion task complete because the accounting identity is available.

## 7. Chat-history verification

This conversation is **Continue late heat caps research**, uniquely registered as home 11 history **0001**. The [dedicated verification receipt](../11_late_heat_caps_and_charge_transport/chat-histories/CHAT_HISTORY_VERIFICATION_CONTINUATION_20261022.json) checks exact completed public-message agreement with the source, stored and canonical hashes, numbering and creation/first-capture provenance, and the presence of the previous manuscript-delivery reply and its completed turn.

The older verification receipt in that folder concerns the distinct founding home-10 conversation and is preserved. Manuscript placement at the portfolio base does not relocate either archive. Later routine refreshes legitimately change counts and hashes; the receipt is a timestamped verification, not a replacement index and not a claim to contain this turn's unsent final reply. The standing bounded exact-turn capture will be arranged at the end of this reply.

