# Topological zero transport: literature and proof self-review

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**, verified against the active turn metadata. This is **same-assistant self-review**, not independent specialist review.

**Disposition: the stated large-heat estimates and complete-boundary identities are proved in the new working manuscript; priority and publishable novelty remain unconfirmed.** The [new maintained paper](../manuscript/topological_zero_transport/README.md) is a sibling of the existing catalogue. [Note 12](../notes/12_GROWING_COMPLEX_CAPS_AND_VANDERMONDE_PHASE_20261023.md) records the incremental result. The [build record](../manuscript/topological_zero_transport/BUILD_RECORD.json) binds the delivered files and checks. The original catalogue's files were checked against their pre-write hashes and preserved.

This assessment follows the [result index](../../../result-summaries/README.md), [heat-geometry summary](../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../avoid/README.md), [target classification](../../../avoid/01_restating_the_target.md), [coupled estimates](../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [literature/novelty discipline](../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## 1. The result being assessed

The paper centers the physical identity

\[
I_0=\frac{k_\epsilon}{2\pi}\operatorname{Im}\int d\log(\Delta\mathscr U)
 +J_++J_-+R-Q.
\]

The normalized jet is exactly (H,H_z). The cap is a three-dimensional integral, Q is the complex collision charge sum binom(m_p,2), and R includes every remaining spatial/joining face. The one-dimensional real initial integral in Note 11 is a different observable. The manuscript does not combine its bounds with the physical formula without a bridge theorem.

The quantitative increment is a complex-time estimate uniform for K=o(L sqrt(kappa)) canonical roots, where L~log(T)/4 and kappa~8TL, together with an O(m eta) estimate for the continuously lifted logarithm of a perturbed clock discriminant. For fixed imaginary width Y and projective radius r/L:

- the full terminal cap divided by m tends to r²Y/pi;
- its Vandermonde contribution divided by m is O(r² e_T/L²), where e_T=(K+1+L²)/(L sqrt(kappa));
- its analytic-factor contribution supplies the leading cap term;
- each imaginary-time face on [theta T,T] has flux per root -r²Y log(1/theta)/(4pi L)+o(1/L);
- the fixed projective spatial wall has exactly zero flux.

These are large-heat, potentially growing-height statements. They are not fixed-heat high-height estimates. The population is fixed on each individual rectangle and may grow between rectangles. A fixed early event core has a different closure limit, including Q/2 on each imaginary-time face for shrinking width; that allocation is not an independent upper bound for Q.

## 2. Search scope and access record

Primary-source searches covered the de Bruijn–Newman deformation, positive-time high-height zeros, heat-root dynamics and logarithmic Hamiltonians, complex caloric multiple zeros, discriminants/resultants, Hopf and Chern–Simons forms, integration along fibers, moving root boundaries, Vandermonde perturbations, and large positive heat-time cosine limits. Searches combined these terms and followed relevant citations in the retrieved papers. The manuscript has **17 external references plus the research archive**. Search-result snippets and aggregators were used for discovery, not as proof sources.

This was a substantial targeted review, not an exhaustive citation census. No exact external counterpart of the stated growing-population physical-cap theorem was located. That negative search result does not certify originality. Particular gaps remain in older scanned sources and in general literature on logarithmic determinant perturbations and fiber integration.

| Primary source | Passage/access checked | Consequence for this draft |
| --- | --- | --- |
| [de Bruijn, *The roots of trigonometric integrals* (1950)](https://pure.tue.nl/ws/portalfiles/portal/1769368/597490.pdf), DOI 10.1215/S0012-7094-50-01720-0 | Institutional original scan and bibliographic record; original full theorem text was not freshly extracted. The normalization-specific reality statement was checked in Polymath's introduction. | Heat deformation and eventual reality are classical. The new proof does not import an unverified quantitative constant from the scan. |
| [Newman, *Fourier transforms with only real zeros* (1976)](https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf) | Primary paper's opening description and publication metadata. | Threshold/classification background; no novelty claimed for the deformation. |
| [Newman–Wu, *Constants of de Bruijn–Newman type in analytic number theory and statistical physics* (2020)](https://www.ams.org/bull/2020-57-04/S0273-0979-2019-01668-1/S0273-0979-2019-01668-1.pdf) | Primary survey abstract and introduction. | Historical and statistical-physics context. No technical theorem is imported into the cap estimate. |
| [Ki–Kim–Lee, *On the de Bruijn–Newman constant* (2009)](https://www.sciencedirect.com/science/article/pii/S0001870809001133) | Publisher abstract and metadata; full proof was not newly obtained. | Eventual reality/simplicity at high height for every fixed positive heat time is prior work. No unverified numerical onset is used. |
| [Polymath, *Effective approximation of heat flow evolution of the Riemann xi function* (2019)](https://arxiv.org/html/1904.12438) | Full text: normalization, introduction, Theorem 1.5 and Section 9; the preceding Note 11 review records the root-localization import in detail. | Fixed-positive-time height asymptotics and barrier methods are established. The new manuscript's large-T complex strip bound is derived from the source instead. |
| [Csordas–Smith–Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant, and the Riemann hypothesis* (1994)](https://www.math.kent.edu/~varga/pub/paper_206.pdf) | Original scan retrieved/indexed, with limited text extraction. Attribution and equation context cross-checked in Rodgers–Tao and Hall–Ho. A direct temporary download attempt returned HTTP 403. | Zero motion and inverse-square interactions are not new. No inaccessible formula is a premise of the proof. |
| [Rodgers–Tao, *The de Bruijn–Newman constant is non-negative*, corrected v5](https://arxiv.org/abs/1801.05914v5) | Full HTML Section 4: logarithmic Hamiltonian (57), energy (58), localized exterior contributions in Lemma 4.18. | Pair energies and localization already have a sophisticated theory. The finite discriminant factorization is not a new dynamics or a replacement for the complete exterior factor. |
| [Dobner, *A proof of Newman's conjecture for the extended Selberg class*](https://arxiv.org/abs/2005.05142v2) | Current primary abstract and version metadata; journal citation checked. The v2 author text was updated in January 2026. | Alternative route and broader setting are acknowledged; its proof is not imported. |
| [Hall–Ho, *The heat flow conjecture for polynomials and random matrices* (2025)](https://link.springer.com/article/10.1007/s11005-025-01946-9) | Full publisher text, Proposition 3.1 and Remark 3.2. | Polynomial root motion and its Calogero–Moser relation are established. Conjectural random-matrix limits are not used as theorems. |
| [Montgomery, *The pair correlation of zeros of the zeta function* (1973)](https://www-personal.umich.edu/~hlm/paircor1.pdf) | Original paper's opening theorem and corollaries. | The theorem's hypotheses and restricted Fourier range must not be replaced by full GUE/PCC. No pair-correlation theorem is needed here. |
| [Whitehead, *An expression of Hopf's invariant as an integral* (1947)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079004/) | Original publication metadata; later access encountered a browser challenge. Formula and convention checked through Rudolph's explicit discussion. | The normalized topological integral is classical. The manuscript checks its own sphere-volume normalization directly. |
| [Chern–Simons, *Characteristic forms and geometric invariants* (1974)](https://math.mit.edu/juvitop/pastseminars/notes_2019_Fall/Chern-Simons.pdf) | Original text's introduction and transgression discussion; publisher metadata. | The boundary-form framework is prior work. The special first-jet pullback is derived explicitly here. |
| [Rudolph, *Whitehead's integral formula, isolated critical points, and the enhancement of the Milnor number* (2010)](https://arxiv.org/pdf/0912.4974) | Full abstract and Section 1, including the stated reduction of a three-form integral to a one-form by fiber integration. | Especially relevant overlap: fiber reduction itself is not new. The candidate contribution must be the precise physical root-tube calculation and quantitative canonical regime. |
| [Gelfand–Kapranov–Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants*](https://link.springer.com/book/10.1007/978-0-8176-4771-1) | Publisher overview, contents and original/reprint metadata; full book not read in this round. | Classical algebraic background. The needed product, local resultant and charge calculation are given in the manuscript. |
| [Papanicolaou–Kallitsi–Smyrlis, *Entire solutions for the heat equation* (2021)](https://ejde.math.txstate.edu/Volumes/2021/44/papanicolaou.pdf) | Full text, Theorem 4.1 and the subsequent zero-motion discussion, printed pages 18–20. | Isolation of complex multiple caloric zeros is known. Their forward-heat convention is reversed here; the local charge formula is proved from the backward-heat polynomial. |
| [Angenent, *The zero set of a solution of a parabolic equation* (1988)](https://math.jhu.edu/~js/Math745/angenent.par1.pdf) | Original scanned source and metadata; full extraction was unavailable, and a direct temporary download returned HTTP 403. | General real zero-number background only. The local birth statement is independently derived from Hermite splitting. |
| [Pashaev–Gurkan, *Abelian Chern–Simons vortices and holomorphic Burgers hierarchy* (2007)](https://arxiv.org/pdf/hep-th/0611029) | Primary text: abstract, zero evolution, Chern–Simons connection; journal metadata cross-checked with [MathNet](https://www.mathnet.ru/eng/tmf6078). | A connection among Chern–Simons theory, holomorphic evolution and zeros already exists. Its gauge field is different from this normalized first jet; that distinction is stated without claiming a wholly new connection. |

An additional primary-source screen examined the introduction and flow discussion in [Romik's orthogonal-polynomial expansions paper](https://danromik.com/resources/papers/riemannxi-acta-online-first.pdf), including its Pólya–de Bruijn background and theta normalization. It is relevant context for the broad program, but no result from it is used in this focused manuscript. The review does not claim to have read every page of every source above.

## 3. Novelty assessment and editorial decision

The broad slogan “topology relates zeros to boundary integrals” has substantial prior art. So do resultant-discriminant identities, heat-induced zero motion, and fiber integration of Hopf forms. A paper advertised chiefly on those slogans would overstate its contribution.

The narrower candidate is the conjunction of four explicit statements for the unchanged canonical source: physical projective disks, a population-linear phase bound, a growing-rank complex-time cap estimate retaining the analytic factor, and the proportional-late-interval edge asymptotic. This is a useful quantitative realization, but its novelty should be evaluated by a specialist familiar with both heat-root asymptotics and geometric integral formulas. The elementary Vandermonde lemma may itself be familiar in another formulation; it is not advertised as a new determinant theory.

The manuscript is therefore retained as a separate, readable working paper, with conservative contribution language in its introduction. It makes no claim that the bounds improve an existing RH/Newman-constant result, or that asymptotic boundary analysis alone yields a new event budget from time zero. Before publication, the main novelty question is whether the stated uniform physical-cap result is already an immediate or explicit consequence of a stronger known complex-time approximation. No reviewers have been contacted.

## 4. Proof audit

| Item | Check and scope |
| --- | --- |
| Local degree | The weighted leading heat polynomial has distinct Hermite roots. Substituting tau=v², z=vw gives discriminant order n(n-1)/2; the Weierstrass resultant identifies it with local intersection degree. The real birth increment 2 floor(n/2) is kept distinct. |
| Normalization and signs | The sphere form has integral 4pi² with the declared complex orientation. The initial face has sign minus; the upper imaginary face is oriented -dt du dv. Thus Q=I_T-I_0+J_++J_-+R. |
| Physical cap reduction | G=h(q,1), A=d arg(h)+a(q), and C=d arg(h) wedge omega/(4pi²). Harmonic averaging is applied to a nonvanishing holomorphic h over an actual disk, not a formal root expansion. A continuously lifted phase is required. |
| Moving side | The projective radius is constant over the entire chosen tube. Pullback of omega vanishes on that wall. Radius changes along a tube and joining complements are not discarded. |
| Vandermonde estimate | Sum the linear logarithm term before taking absolute values. The harmonic coefficient total is at most 2(m-1); the quadratic remainder is bounded with sum d^(-2). This gives 4(m-1)eta/pi+8m eta²/9 <=2m eta for eta<=pi/8. |
| Source concentration | Positive lower and upper bounds retain every theta index. The proof includes normalization, a Gaussian near/right bound, and the far-left exponential tail. All three required weighted moments are controlled. |
| Complex strip and rank | Only the imaginary part of w enters the exponential trigonometric bound. Rouché gives simple inverse solutions on fixed disks; real signs and derivative bounds identify the first K positive roots. Local uniqueness patches them over the rectangle. |
| Lifted phase | Each normalized derivative lies in a disk about one, producing a single logarithm after the exact factor exp(isL²) is removed. No uncontrolled asymptotic derivative is taken. |
| Late edge | The same physical radius r/L_T and population are used at both endpoint caps. L'_t=2L_t/kappa_t supplies the coefficient log(1/theta)/(4L_T). |
| Event core | Compact floors pay the non-imaginary faces by volume; real conjugation equates the two imaginary contributions. The Q/2 limit is conditional on this complete geometry and is not an independent estimate of Q. The canonical-flow assumption is explicit for all cap asymptotics in this theorem. |

Corrections made during this self-review: the asymptotic part of the fixed-core theorem now explicitly assumes the canonical flow and fixed positive ranks; “real type” is defined; a typesetting typo in the core geometry was repaired. The initial compiling macro conflict and missing script font package were also repaired before delivery. No unresolved compiler warning is used to conceal a missing reference or equation.

## 5. Controls and numerical scope

The exact quadratic heat event H=z²-2tau has charge one, cap k_epsilon arctan(Y/T)/pi, and zero regular projective walls. Its inverse disks pinch backward at q²=-2tau. It demonstrates the missing joining/closure contribution directly.

The stationary sine flow H=exp(lambda²tau) sin(lambda z)/lambda has constant root positions and constant Vandermonde, but nonzero cap k_epsilon m lambda²Y/pi. It demonstrates that the analytic factor cannot be dropped and principal endpoint phases cannot replace lifted ones.

The [diagnostic script](../numerics/check_topological_caps_20261023.py) and [small record](../numerics/TOPOLOGICAL_CAP_CHECKS_20261023.json) contain 105 Vandermonde cases, a direct physical quadratic-disk pullback quadrature, a winding control and saddle-reference checks. The largest direct-cap discrepancy was approximately 8.62e-11. The harmonic-regrouping discrepancy was at most 2.71e-13. These are floating diagnostics, not interval certificates or actual theta evaluations; the analytic proof stands independently.

The [repository collision controls](../../../result-summaries/12_collision_controls_and_screening.md) remain admitted by the generic identities. Euler-factor controls change the canonical source; weighted-square/finite-prime controls lack its full unchanged reflection or coefficients; reflected/positive-primitive controls lack the unchanged square expansion; close positive endpoints need not carry ordinary Dirichlet arithmetic. The large-heat proof uses its stated positive source bounds, and is not claimed to exclude every noncanonical source sharing those bounds.

## 6. Remaining research and validation

The unresolved analytic task is a height-dependent bound on the complete early attachment and imaginary-time boundary, together with an independently useful lower bound for the fixed initial cap. Relative bounds or an upper bound on the number of creation events would be meaningful progress. The fixed-core constant B has not been made uniform in growing height, and its allocation formula already contains the unknown Q.

Document checks comprise successful compilation, equation/citation resolution, visual inspection of every delivered page, local-link checking, file-size checks, and preservation of the existing catalogue hashes. Exact build evidence is in the linked record. These checks validate document integrity and elementary diagnostics; they do not supply independent mathematical or novelty review.
