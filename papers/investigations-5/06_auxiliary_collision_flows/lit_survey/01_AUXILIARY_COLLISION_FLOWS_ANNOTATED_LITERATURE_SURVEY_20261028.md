# Auxiliary collision flows: annotated literature survey

28 October 2026, America/New_York. Prepared for **Edward Baker**, with substantial LLM research and drafting assistance from **gpt-6.1-sol (Codex), recorded reasoning effort ultra**. Parallel literature searches used the same model; this is not independent specialist review.

**Status: a thematic survey of forty references, with selected primary-source passage checks.** It responds to the [initial research overview](../research-overview/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_OVERVIEW_20261028.md) and the inherited [source-flow calculation, Note38](../../05_radial_theta_collision_geometry/notes/38_AUXILIARY_SOURCE_FLOWS_AND_COLLISION_RESPONSE_20261028.md). It identifies precedents and limitations; it does not select a flow, research plan or numerical campaign, establish a theta collision exclusion, or claim a diagnostic cost improvement.

## Scope, evidence and reading guide

The search followed four connected strands: universal source factors and stability-preserving operators; Lee–Yang measures and interaction parameters; zero dynamics and coalescing-root diagnostics; and parabolic zero counting, total positivity and the cosine flow's exact translation kernel. Searches used article titles, theorem terminology and cited primary references, with version checks through **28 October 2026**. This is substantial thematic coverage, not a systematic-review protocol or a claim to exhaust every related paper. Publication years and examined preprint revision dates are distinguished below.

Each entry gives the relevant result, its connection to the overview, the hypotheses or limitation that matter, and what was actually inspected. “Selected passages” means definitions, statements and surrounding discussion, not a complete proof audit. Several historical originals were available only as metadata, abstracts or scans; their mathematical statements are explicitly routed to a later checked source. No source's full abstract is reproduced. No numerical certificate from the literature was replayed.

The reusable [BibTeX bibliography](../references/sources.bib), [source catalog](../references/sources.json) and [PDF retrieval manifest](../references/lit_survey_pdf_manifest_20261028.json) accompany this note. Authorized reading copies are outside Git; download success does not upgrade an inspection. Earlier Rodgers–Tao and Newman–Wu provenance is retained in the catalog. The existing [result index](../../../../result-summaries/README.md), especially [heat-flow results](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md) and [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md) govern interpretation. In particular, see [target reformulations](../../../../avoid/01_restating_the_target.md), [shared control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [coordinate realizations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [unchecked imports](../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

| Connection to the overview | Closest references | Information the literature supplies | Premise still needed for a theta application |
| --- | --- | --- | --- |
| Multiplying the source by exp(sq) | ZP02, ZP04–ZP05 | Universal-factor classification and general-measure distinctions | Source-specific comparison when the factor is not universal |
| Designing local or finite-shift operators | ZP07–ZP12 | Symbol tests, function-space continuity and strip contraction | The operator's domain, its exponential if used as a flow, and comparison with the physical slice |
| Coupled fields and interaction parameters | LY01–LY06, LY10 | Ferromagnetic preservation, nonvanishing domains and controlled zero trajectories | An admissible representation of the complete canonical source |
| Following zero particles or higher jets | DY01–DY06 | Principal-value dynamics, localized energies, Lehmer tests and spacing regularization | New identities and error estimates for the changed flow |
| Continuing a collision through two parameters | DY08–DY10 | Puiseux structure, analytic squared gaps and partial discriminants | Certified evaluation and comparison at the same information cost |
| The bounded cosine flow | AX06–AX07 | Exact Bessel translate expansion and jump-process interpretation | A demonstrated normalized diagnostic advantage |

The closest initial reading set is **ZP05, ZP10–ZP12, LY10, DY01, DY09 and AX06**. Historical citations remain useful, but their inspection limits should travel with them.

## Connections that change how the overview can be read

### Universal preservation sharply restricts an exponential tilt

Pólya's universal-factor theorem, in the checked formulation of **ZP05, §2.2, Theorem 2**, says that a real analytic source multiplier φ is universal precisely when φ(iz) belongs to the Laguerre–Pólya class. Consequently, if q is even entire and real on the real axis, and φ(u)=exp(sq(u)) is an admissible universal multiplier for a fixed nonzero real s, its rotated zero-free even LP function must be C exp(−b z²), b≥0. Thus q(u)=q(0)+c u² with sc≥0. Requiring both signs of s leaves only amplitude changes. This is a direct consequence of the classical product representation, not a new theorem about theta.

The bounded cosine tilt with a≠0 therefore lies outside this universal-preserver family for every nonzero real s. Quartic tilts additionally have an integrability issue on general super-Gaussian source classes, even though the canonical theta tail admits them. These statements leave special-source estimates, diagnostics and nonexponential deformations open. They do not exclude auxiliary-flow research as a whole.

### The cosine flow is an exact average of translated observations

Let a be the fixed mark and write F for the overview's q(u)=cos(au) family. The classical identity in **AX06** gives, by termwise integration,
\[
F(t,s,z)=\sum_{n\in\mathbb Z} I_n(s)H(t,z+na).
\tag{S1}
\]
For complex parameters in compact sets, bounded q and the theta tail justify domination; for fixed t and z the translated H values also have a bound independent of the real shift n a. For real s≥0,
\[
e^{-s}F(t,s,z)=\mathbb E\,H(t,z+a(N_+-N_-)),
\quad N_+,N_-\text{ independent Poisson}(s/2).
\tag{S2}
\]
Hence the normalized generator is (T_a+T_{-a})/2−I, and on the real z axis its sup norm is at most that of H(t,·). This probabilistic identification is an elementary inference from the generating functions, with **AX07** giving the historical distribution name. It requires s≥0 for probability weights. Equation (S1) also exhibits an evaluation tradeoff: one pays for translated original observations and a controlled series tail. It establishes no speedup.

Positivity of that averaging operator does not imply real-zero preservation. A direct polynomial check is
\[
e^{s((T_a+T_{-a})/2-I)}z^2=z^2+s a^2,
\]
which has nonreal zeros for s>0. This is a polynomial operator control, not a canonical Fourier-source example.

There is also an exact **positive atomic source control**, included here as a short calculation rather than a literature import. For 1/2<p<1, take
\[
d\rho=(1-p)\delta_0+\frac p2(\delta_1+\delta_{-1}),\quad
H_\rho(z)=1-p+p\cos z.
\]
Its zeros are real and simple. Under q(u)=cos(πu),
\[
F_\rho(s,z)=(1-p)e^s+pe^{-s}\cos z.
\]
At s_c=\tfrac12\log(p/(1-p))>0 the zero at z=π is double, with F_{zz}=pe^{-s_c}>0 and F_s=2pe^{-s_c}>0. For s>s_c the equation cos z=−((1-p)/p)e^{2s} has nonreal zeros. Thus this positive bounded tilt can leave the real-zero class even when it starts there. The example fails continuity, the theta tail and canonical arithmetic; its atomic support does pass the strict-response test cos²(πu)=1. It claims nothing about the canonical source.

### Controlled interaction motion is an especially close precedent

**LY10** provides an actual auxiliary interaction parameter with disjoint zero trajectories and, in its Curie–Weiss specialization, strict motion of principal zeros. Its finite-spin ferromagnetic structure is essential. This is evidence that designing a useful auxiliary parameter is a meaningful mathematical question; importing its conclusion requires an appropriate representation of the source. The approximation/closure results **LY02** and **LY08** can preserve zero location in limits but permit multiple zeros. Neither closure nor positivity alone supplies a simplicity margin.

### An analytic squared gap belongs to established collision numerics

The overview's analytic D=(z_+−z_−)² has a direct counterpart in **DY09**, whose equations (3)–(5) continue sums and squared differences of coalescing eigenvalue branches. Its partial characteristic polynomial and discriminant extend that idea to clusters. **DY08** supplies Puiseux background. These are potential diagnostic precedents; their matrix algorithms and error models have not been transferred to the theta integral. The distinction between branch sensitivity and attainable precision in **DY10** is a useful comparison principle, not a universal obstruction to deterministic numerical improvement.

### Time orientation, operator type and function space matter

The overview uses H_t=−H_{zz}. Reversing to r=−t gives a forward scalar heat equation, so the zero-number results **AX04–AX05** concern the opposite time orientation and stated finite intervals or periodic domains. They do not automatically extend to fourth-order, nonlocal or coupled equations. Likewise, **ZP08** classifies individual differential preservers, while a flow needs its exponential and analytic domain; **ZP09** supplies a function-space framework for that distinction. **AX01–AX03** distinguish positive densities, positive semidefinite kernels and totally positive convolution kernels. These hypotheses cannot be substituted for one another.

## Collision-control interpretation

No exclusion criterion is proposed in this survey. The following is an analytic premise screen of the generic response identities and literature analogies, using the existing [control register](../../../../result-summaries/12_collision_controls_and_screening.md) and [Note38's control calculation](../../05_radial_theta_collision_geometry/notes/38_AUXILIARY_SOURCE_FLOWS_AND_COLLISION_RESPONSE_20261028.md). It is not a fresh numerical validation.

| Existing control class | What the bounded-tilt calculation shares | Distinguishing premise it fails or needs |
| --- | --- | --- |
| Euler-factor controls | Positive source, bounded cosine tilt and marked square response | Unchanged canonical Euler factors and coefficients |
| Weighted-square and finite-source controls | Local dominated tilt and positive response for their continuous positive half-line densities | Complete coefficients/full reflection; a local collision time is not automatically an all-real threshold |
| Finite-prime-compatible perturbations | Bounded source perturbations and finite arithmetic/measurement compatibility | Full reflection and unchanged complete theta coefficients |
| Reflected super-Gaussian controls | Positive continuous source, reflection and the same local response identities | Canonical square arithmetic |
| Smooth shape/positive-primitive controls | Strong shape or primitive positivity together with the same bounded response | Canonical arithmetic and any independently proved separating estimate |
| Note38's polynomial-Gaussian control | The marked cosine response at its stated event and local parameter range | Theta tail, all-time integrability and canonical arithmetic; positive quartic tilt diverges there |
| Atomic controls, including the calculation above | Nonnegative measure and bounded tilt | Continuity; strict response also needs support not confined to zeros of cos(au) |

These controls do not claim to satisfy ferromagnetic component hypotheses, operator-symbol stability, or a hypothetical quantitative theta estimate. A negative preservation result below is always attached to its stated class. An RH-equivalent all-degree Wronskian condition (**LY07**), probabilistic reformulation (**LY11**) or global regularity assertion is classified as a reformulation until an independent usable estimate is obtained. No research direction is closed merely by that classification.

## A. Universal factors, stability preservers and strip contraction

<a id="zp01"></a>

### ZP01 — Pólya and Schur (1914): multiplier sequences and the LP class

G. Pólya and I. Schur, *Über zwei Arten von Faktorenfolgen in der Theorie der algebraischen Gleichungen*, Journal für die reine und angewandte Mathematik **144** (1914), 89–113. [DOI](https://doi.org/10.1515/crll.1914.144.89); [digitized original volume](https://gdz.sub.uni-goettingen.de/id/PPN243919689_0144?tify=%7B%22view%22%3A%22info%22%2C%22pages%22%3A%5B93%5D%7D).

**Relevant result.** Classifies diagonal coefficient multipliers preserving real-rootedness and underlies the LP canonical-product description. **Relevance.** Supplies the right distinction between a diagonal multiplier sequence in Taylor coefficients and multiplication of a Fourier source; they are related operator theories, not identical operations. **Scope.** Original bibliographic identity and digital scan located; original German proof not inspected. The modern statement is available in Borcea–Brändén 2010 §3.1 and Newman–Wu Theorem 1. Treat this as a foundational original citation, not a fully read original.

<a id="zp02"></a>

### ZP02 — Pólya (1927): universal source factors

G. Pólya, *Über trigonometrische Integrale mit nur reellen Nullstellen*, Journal für die reine und angewandte Mathematik **158** (1927), 6–18. [Publisher/DOI](https://doi.org/10.1515/crll.1927.158.6).

**Relevant result.** The universal-factor characterization is the classical framework for source multiplication that preserves real Fourier zeros across an admitted fast-decay class. **Relevance.** Direct precedent for exp(sq(u)); it separates a universal preservation claim from a source-specific response calculation. **Scope.** Publisher metadata checked; original full text was access-restricted. Exact characterization and standing symmetry/decay assumptions inspected in Newman–Wu §2.2, Theorem 2, equations (8)–(11). Do not state that Pólya's original proof was inspected.

<a id="zp03"></a>

### ZP03 — de Bruijn (1950): strip shrinkage and strong universal factors

N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Mathematical Journal **17** (3) (1950), 197–226. [DOI](https://doi.org/10.1215/S0012-7094-50-01720-0); [TU/e record](https://research.tue.nl/en/publications/the-roots-of-trigonometric-integrals/); [institutional PDF link](https://research.tue.nl/files/1769368/597490.pdf).

**Relevant result.** If a real symmetric fast-decay source has transform zeros in |Im z|≤Δ, multiplying by e^{δu²}, δ>0, places zeros in |Im z|≤sqrt(max(Δ²−2δ,0)). **Relevance.** This gives a quantitative comparison that arbitrary auxiliary directions lack. Theorem 13 is the original reference for Gaussian strip shrinkage; the paper also studies more general universal factors and differential constructions. **Scope.** Metadata checked against TU/e (some Delft metadata incorrectly label 1948). Original PDF endpoints timed out/returned 403, so the theorem statement was checked in the primary Newman 1976 paper, Theorem 1, p.246, and Newman–Wu Theorem 7. No original de Bruijn proof audit claimed.

<a id="zp04"></a>

### ZP04 — Newman (1976): classification under all negative Gaussian times

Charles M. Newman, *Fourier Transforms with Only Real Zeros*, Proceedings of the American Mathematical Society **61** (2) (1976), 245–251. [DOI](https://doi.org/10.2307/2041319); [faculty-hosted original PDF](https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf).

**Relevant result.** Theorem 2, pp.246–247 classifies even nonnegative finite measures whose Gaussian-damped Fourier transforms have only real zeros for every positive damping parameter; Theorem 3 applies this to show the Riemann deformation has a finite lower threshold. The continuous class is expressed by a quartic/Gaussian factor times a canonical product, with explicit convergence and sign conditions, alongside a symmetric atomic case. **Relevance.** Shows how much stronger an all-time preservation property is than positivity and fast decay, and connects the theta question to statistical mechanics. **Scope.** Original introduction and Theorems 1–3 inspected, not a line-by-line proof audit. Newman's b has the opposite sign to the overview's t and a different spectral scaling.

<a id="zp05"></a>

### ZP05 — Newman and Wu (2020): survey and general-source classification

Charles M. Newman and Wei Wu, *Constants of de Bruijn–Newman type in analytic number theory and statistical physics*, Bulletin of the American Mathematical Society **57** (4) (2020), 595–614. [DOI](https://doi.org/10.1090/bull/1668); [arXiv:1901.06596v2](https://arxiv.org/abs/1901.06596v2), 13 March 2019; [full HTML](https://arxiv.org/html/1901.06596v2).

**Relevant result.** §2.2 gives Pólya's universal-factor criterion with assumptions; §2.3 explains strip contraction; §3 classifies possible real-zero-time sets according to Gaussian integrability of general even measures. **Relevance.** The closest broad survey to the overview, with examples that prevent source positivity or tail decay from being mistaken for a zero-location theorem. **Scope.** These sections inspected selectively; normalizations differ from the overview. Published year 2020 and arXiv revision year 2019 should both be retained.

<a id="zp06"></a>

### ZP06 — Ki, Kim and Lee (2009): positive-time eventual simplicity

Haseo Ki, Young-One Kim and Jungseob Lee, *On the de Bruijn–Newman constant*, Advances in Mathematics **222** (1) (2009), 281–306. [DOI](https://doi.org/10.1016/j.aim.2009.04.003); [institutional record](https://yonsei.elsevierpure.com/en/publications/on-the-de-bruijn-newman-constant/).

**Relevant result.** For each fixed positive time, all but finitely many zeros of the deformed xi function are real and simple, and the classical upper bound is made strict. **Relevance.** Supplies an existing theta-specific outer-region theorem that auxiliary collision diagnostics must respect; the remaining finite set and the behavior as time approaches zero remain material. **Scope.** Primary institutional abstract checked; exact main statement and stronger strip-shrinkage hypotheses also inspected in Newman–Wu §2.7, Theorems 13–14. Original proof was not obtained. No uniform finite height threshold is inferred.

<a id="zp07"></a>

### ZP07 — Borcea and Brändén (2009): full polynomial stability-preserver classification

Julius Borcea and Petter Brändén, *The Lee–Yang and Pólya–Schur Programs. I. Linear Operators Preserving Stability*, Inventiones Mathematicae **177** (3) (2009), 541–569. [DOI](https://doi.org/10.1007/s00222-009-0189-3); [arXiv:0809.0401v3](https://arxiv.org/abs/0809.0401v3), 13 March 2009; [PDF](https://arxiv.org/pdf/0809.0401v3).

**Relevant result.** Theorems 1.1–1.4 characterize stability-preserving polynomial operators by algebraic or transcendental symbols, with exceptional low-rank cases and a sign alternative in the real classification. **Relevance.** A systematic test for claims that an auxiliary linear operation preserves real roots; it replaces guesses based on positivity of coefficients or kernels. **Scope.** Main definitions and Theorems 1.3–1.4, pp.5–6 of preprint, inspected. Polynomial classification alone does not justify convergence or continuity on the theta entire function; those are separate analytic steps.

<a id="zp08"></a>

### ZP08 — Borcea and Brändén (2010): local differential generators and their symbols

Julius Borcea and Petter Brändén, *Multivariate Pólya–Schur classification problems in the Weyl algebra*, Proceedings of the London Mathematical Society (3) **101** (1) (2010), 73–104. [DOI](https://doi.org/10.1112/plms/pdp049); [arXiv:math/0606360v6](https://arxiv.org/abs/math/0606360v6), 6 November 2009; [PDF](https://arxiv.org/pdf/math/0606360v6).

**Relevant result.** Theorems 1.2–1.3, p.3 of preprint characterize finite-order differential stability preservers through the signed Weyl symbol. Example 4.2, p.21 recovers Hermite–Poulain: p(D) preserves real-rooted polynomials exactly when p has only real zeros. **Relevance.** Relevant to local higher-order and polynomial-coefficient auxiliary operators. **Scope.** Main theorems and Example 4.2 inspected. The classification of a single operator L does not automatically classify its semigroup e^{sL}; claims about flows require testing that exponential and its domain.

<a id="zp09"></a>

### ZP09 — Brändén (2014): entire-function extensions and operator norms

Petter Brändén, *The Lee–Yang and Pólya–Schur programs. III. Zero-preservers on Bargmann–Fock spaces*, American Journal of Mathematics **136** (1) (2014), 241–253. [DOI](https://doi.org/10.1353/ajm.2014.0003); [arXiv:1107.1809v1](https://arxiv.org/abs/1107.1809v1), 9 July 2011; [PDF](https://arxiv.org/pdf/1107.1809v1).

**Relevant result.** Theorems 3.1–3.2 extend symbol characterizations to bounded operators between weighted entire-function spaces; Theorem 3.4 gives a norm estimate; Theorem 4.5 gives composition of Lee–Yang preservers. **Relevance.** Supplies the analytic continuity framework missing from a polynomial-only screening argument, and a natural place to quantify amplification cost. **Scope.** Theorems 3.1–3.4 and 4.5 inspected. The weighted-space parameters and symbol bounds must actually hold; a formal Fourier multiplier is insufficient.

<a id="zp10"></a>

### ZP10 — Brändén and Chasse (2017): operators preserving and contracting strips

Petter Brändén and Matthew Chasse, *Classification theorems for operators preserving zeros in a strip*, Journal d'Analyse Mathématique **132** (2017), 177–215. [DOI](https://doi.org/10.1007/s11854-017-0018-3); [arXiv:1402.2795v2](https://arxiv.org/abs/1402.2795v2), 29 June 2016; [PDF](https://arxiv.org/pdf/1402.2795v2).

**Relevant result.** Classifies strip preservers for complex polynomials and develops conditions for real strip preservers and strip-contraction operators. Theorem 4.7, p.24 of preprint: f(z)=∫₀¹cos(λzt)g(t)dt with nonzero integrable nonnegative nondecreasing g on [0,1] gives a differential operator f(D) contracting a strip of half-width μ to sqrt(max(μ²−λ²/4,0)). **Relevance.** A concrete non-Gaussian operator family with a quantitative geometric conclusion, useful for comparison with the overview's unconstrained auxiliary families. **Scope.** Introduction and Theorems 4.4–4.7 inspected. The paper explicitly separates the two properties of a strong universal factor; proving contraction does not automatically give its finite-nonreal-zero property. Its cosine is the **operator symbol**, not the overview's bounded source weight.

<a id="zp11"></a>

### ZP11 — Cardon (2015; corrected 2026 preprint): complex-zero strip decrease

David A. Cardon, *Complex zero strip decreasing operators*, Journal of Mathematical Analysis and Applications **426** (1) (2015), 406–422. [DOI](https://doi.org/10.1016/j.jmaa.2015.01.026). Use [corrected arXiv:1401.0237v3](https://arxiv.org/abs/1401.0237v3), **20 October 2026**, [PDF](https://arxiv.org/pdf/1401.0237v3).

**Relevant result.** Theorem 1.5 gives explicit strip decrease when the LP operator symbol contains a negative Gaussian factor; Theorem 1.6 gives growth obstructions for genus≤1 symbols without such a factor. Lemma 1.3 requires Gaussian-type product <1/4 for convergence. **Relevance.** Distinguishes preservation from strict contraction and states costs and domains that auxiliary-flow arguments need. **Scope.** Corrected cover, Definitions 1.1–1.4 and Theorems 1.5–1.6 inspected. The v3 cover explicitly corrects errors/gaps in the published version and reports that its Conjectures 5.3/5.4 were false. This dated correction predates the survey's 28 October 2026 cutoff. No uncorrected conjecture is imported.

<a id="zp12"></a>

### ZP12 — Katkova, Tyaglov and Vishnyakova (2018): finite differences with variable coefficients

Olga Katkova, Mikhail Tyaglov and Anna Vishnyakova, *Linear finite difference operators preserving the Laguerre–Pólya class*, Complex Variables and Elliptic Equations **63** (2018), 1604–1619. [DOI](https://doi.org/10.1080/17476933.2017.1400539); [arXiv:1608.03924v2](https://arxiv.org/abs/1608.03924v2), 3 September 2016; [PDF](https://arxiv.org/pdf/1608.03924v2).

**Relevant result.** Proposition 1.1 and Theorem 1.2 classify nontrivial two-shift operators M₁(z)f(z+h)+M₂(z)f(z−h) preserving polynomial real-rootedness or LP; imaginary h and Hermite–Biehler coefficient conditions are central. **Relevance.** Directly addresses the two-shift form in the overview and shows that the direction of the shifts and coefficient structure matter. **Scope.** Proposition 1.1 and theorem statement inspected. The overview has real shifts, so this does not supply preservation for its cosine generator. Issue number is omitted because the arXiv and publisher indexing were inconsistent; volume and pages identify the article.

## B. Lee–Yang measures, coupled systems and interaction parameters

<a id="ly01"></a>

### LY01 — Lee and Yang (1952)

T. D. Lee and C. N. Yang, **Statistical Theory of Equations of State and Phase Transitions. II. Lattice Gas and Ising Model**, *Physical Review* **87**, 410–419 (1952). DOI [10.1103/PhysRev.87.410](https://doi.org/10.1103/PhysRev.87.410).

**Result and relevance.** The circle theorem locates the zeros of the ferromagnetic Ising partition function on the unit circle in the activity variable, equivalently on the imaginary axis in the uniform external field. This is the classical source of real-zero Fourier transforms built from interacting positive spin measures. The structural input includes ferromagnetic interactions and spin symmetry; positivity of the Gibbs weight alone does not locate zeros. For the overview, this gives the correct comparison class for source tilts realized as interaction changes.

**Scope.** Publisher metadata and abstract inspected; precise multivariate formulation checked in Newman–Wu (2020 survey; arXiv revision 2019), §2.5, equations (21) and following. Original theorem proof not reviewed. A canonical theta-source representation by such an interacting spin model is not established here.

<a id="ly02"></a>

### LY02 — Simon and Griffiths (1973)

Barry Simon and Robert B. Griffiths, **The (φ⁴)₂ field theory as a classical Ising model**, *Communications in Mathematical Physics* **33**, 145–164 (1973). DOI [10.1007/BF01645626](https://doi.org/10.1007/BF01645626).

**Result and relevance.** The authors approximate spatially cut off φ⁴ Euclidean fields by spin-½ Ising systems with ferromagnetic pair interactions and obtain Lee–Yang and GHS inequalities. This is a substantive precedent for proving a zero theorem by an auxiliary finite-dimensional realization and limit. It identifies more than a positive source: the approximating models carry a zero-preserving interaction structure. The one-site quartic density exp(−a x⁴−b x²), a>0, b real, is a standard Lee–Yang example; arbitrary higher-degree positive potentials do not share that property.

**Scope.** Original publisher abstract inspected; the quartic example and existence of sextic failures checked through Newman–Wu §2.5, not independently in the 1973 proof. No claim that the complete theta source has the required Ising approximation.

<a id="ly03"></a>

### LY03 — Newman (1974)

Charles M. Newman, **Zeros of the partition function for generalized Ising systems**, *Communications on Pure and Applied Mathematics* **27**(2), 143–159 (1974). DOI [10.1002/cpa.3160270203](https://doi.org/10.1002/cpa.3160270203).

**Result and relevance.** Newman's extension replaces two-point spins by suitable single-spin measures already having the Lee–Yang property. Ferromagnetic pair interactions retain nonvanishing when all external fields have positive real part; nonnegative linear combinations of spins consequently have real-zero Fourier transforms. The single-spin zero hypothesis is essential. Applying the theorem to the theta density as its own single-spin measure would require the very zero-location information sought. A useful application must instead establish a representation by known admissible component measures and permitted interactions.

**Scope.** Original publisher metadata inspected. Mathematical statement inspected in Newman–Wu (2020 survey), Theorem 11, and Dimitrov (2013), introduction conditions (i)–(iii). Original proof not reviewed. Strong tail integrability (all quadratic exponential moments in the quoted version) is among the hypotheses; weaker tails restrict interaction strength.

<a id="ly04"></a>

### LY04 — Lieb and Sokal (1981)

Elliott H. Lieb and Alan D. Sokal, **A general Lee-Yang theorem for one-component and multicomponent ferromagnets**, *Communications in Mathematical Physics* **80**, 153–179 (1981). DOI [10.1007/BF01213009](https://doi.org/10.1007/BF01213009).

**Result and relevance.** A measure on Rⁿ possessing the Lee–Yang property retains it after multiplication by a ferromagnetic pair interaction. The paper obtains one- and two-component consequences and multicomponent results with anisotropy conditions. This is an especially relevant general framework for coupled auxiliary fields: the multiplier and the initial measure both have to satisfy the theorem's structure. It supplies no theorem for arbitrary exp(sq(u)) merely because the multiplier is positive on the real source axis. Nor does an arbitrary geometric lift identify an admissible interaction.

**Scope.** Publisher abstract and bibliographic record inspected. Fine hypotheses and proof have not been checked in the original full text; no numbered theorem imported. The accessible Fröhlich–Rodriguez §2 states several usable versions with assumptions and is a better next point of entry for an actual application.

<a id="ly05"></a>

### LY05 — Ruelle (2010)

David Ruelle, **Characterization of Lee-Yang polynomials**, *Annals of Mathematics* **171**(1), 589–603 (2010). DOI [10.4007/annals.2010.171.589](https://doi.org/10.4007/annals.2010.171.589). [Publisher PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n1-p16-p.pdf); arXiv:0811.1327.

**Result and relevance.** Theorem 3 characterizes multiaffine Lee–Yang polynomials using an n-variable polynomial nonvanishing in the polydisk and its reflected polynomial. Proposition 2 records a contraction-related inner-radius inequality. Theorem 9 proves rigidity for the family with coefficients exp(βW_X): Lee–Yang membership along a positive sequence β→0 implies membership at every β>0 and forces a ferromagnetic pair-interaction form (up to allowed phases/constants). This is a precise scoped restriction on designing finite-spin source deformations. It does not exclude arbitrary continuous-source, nonpolynomial, local-parameter, or coupled-field flows.

**Scope.** Publisher PDF introduction, Proposition 2, Theorems 3 and 9, and physical interpretation §11 inspected. Theorem 9's finite multiaffine and fixed exponential-coefficient hypotheses must accompany any use. General Lee–Yang polynomials also exist beyond the pair-interaction subclass at a fixed parameter.

<a id="ly06"></a>

### LY06 — Fröhlich and Rodriguez (2012)

Jürg Fröhlich and Pierre-François Rodriguez, **Some applications of the Lee-Yang theorem**, *Journal of Mathematical Physics* **53**, 095218 (2012). DOI [10.1063/1.4749391](https://doi.org/10.1063/1.4749391). [arXiv:1205.6643v1](https://arxiv.org/abs/1205.6643v1), 30 May 2012.

**Result and relevance.** §2 surveys usable Lee–Yang hypotheses; Proposition 7 and §3 derive analytic thermodynamic limits of connected correlations off the imaginary-field axis. The proof introduces several auxiliary source fields and obtains a nonvanishing region Re h>Σ|ε_α| (equations (3.3)–(3.5)), enabling analytic logarithms and differentiated responses. This is a concrete precedent for controlling a multivariable auxiliary response in a certified nonzero domain. The domain is obtained from an existing Lee–Yang theorem; it does not yield the missing boundary noncollision assertion.

**Scope.** arXiv full text selected §2–3 passages inspected. Useful comparison with the overview's normalized responses and feedback regularity, conditional on a genuinely established nonvanishing domain. Bibliography checked against DOI redirect; the correct article number is 095218 (not the nearby 095223).

<a id="ly07"></a>

### LY07 — Dimitrov (2013)

Dimitar K. Dimitrov, **Lee-Yang measures and wave functions**, preprint [arXiv:1311.0596v1](https://arxiv.org/abs/1311.0596v1), 4 November 2013.

**Result and relevance.** Under the moment assumptions (3), (5), Theorem 1 gives a necessary and sufficient condition for a positive even measure's entire Fourier transform to have only real zeros: every Wronskian W(p₁,…,p_n;z), with p_j the orthonormal polynomials, has only imaginary zeros. The proof identifies these Wronskians with scaled Jensen/Appell polynomials. §4.2 connects the constructions with Toda dynamics and heat flow; §4.3 discusses ξ. This is directly related to auxiliary polynomial/wave-function realizations and offers a finite-family language for testing consequences of a proposed mechanism.

**Scope.** arXiv full text Theorem 1, equations (3), (5), §3.3 and §4.2–4.3 inspected; no published version verified. For the theta source, the all-n condition remains a reformulation of the target. Orthogonal-polynomial existence or moment positivity alone does not verify it.

<a id="ly08"></a>

### LY08 — Newman and Wu (2019)

Charles M. Newman and Wei Wu, **Lee–Yang Property and Gaussian Multiplicative Chaos**, *Communications in Mathematical Physics* **369**, 153–170 (2019). DOI [10.1007/s00220-019-03453-0](https://doi.org/10.1007/s00220-019-03453-0). [arXiv:1708.08820v3](https://arxiv.org/abs/1708.08820v3), 21 August 2018.

**Result and relevance.** Theorem 7 proves that the class of symmetric probability measures with some Gaussian exponential moment and imaginary-zero-only moment generating functions is closed under weak convergence. No uniform Gaussian-moment coefficient is assumed for the approximating sequence. Theorem 11 excludes real-zero transforms for distributions with certain superlinear exponential moments but no Gaussian exponential moment. The Villain model has the Lee–Yang property; some complex Gaussian multiplicative chaos models do not. This provides both a rigorous approximation passage and a warning that related field geometries can have different zero structures.

**Scope.** v3 Definition 6, Theorems 7 and 11, publisher abstract inspected. The theta tail satisfies the moment requirement; proving a sequence of approximants already belongs to the Lee–Yang class remains the substantive premise. The theorem concerns zero location, not simplicity, and permits real collisions in limits.

<a id="ly09"></a>

### LY09 — Simon (2022)

Barry Simon, **The strong Gauss–Lucas theorem and analyticity of correlation functions via the Lee–Yang theorem**, *Journal of Mathematical Physics* **63**(3), 033302 (2022). DOI [10.1063/5.0077229](https://doi.org/10.1063/5.0077229). [arXiv:2111.00650v1](https://arxiv.org/abs/2111.00650v1); [Caltech record](https://authors.library.caltech.edu/records/7ak9d-96772).

**Result and relevance.** Theorem 2.1 strengthens Gauss–Lucas to positivity of Re(P′/P) for a nonconstant polynomial nonvanishing in the right half-plane. Theorem 2.3 extends differentiation and logarithmic-derivative inequalities to specified weighted closures of stable polynomials; Theorem 2.7 converts positive-real-part analyticity into quantitative two-sided bounds. The application derives bounds and analytic correlation limits for Lee–Yang systems. This is a good source for auxiliary ratios or feedback regularity once a stable-function domain has independently been proved.

**Scope.** arXiv selected theorem statements and definitions inspected; published metadata checked in Caltech. Mere nonvanishing of an arbitrary entire function does not place it in the weighted closure used by Theorem 2.3. The half-plane bounds deteriorate toward its boundary and do not automatically control the real spectral collision slice.

<a id="ly10"></a>

### LY10 — Hou, Jiang and Newman (2023)

Qi Hou, Jianping Jiang and Charles M. Newman, **Motion of Lee–Yang Zeros**, *Journal of Statistical Physics* **190**, article 56 (2023). DOI [10.1007/s10955-023-03066-x](https://doi.org/10.1007/s10955-023-03066-x). [arXiv:2208.00917v1](https://arxiv.org/abs/2208.00917v1), 1 August 2022.

**Result and relevance.** Theorem 1 treats increasing one ferromagnetic edge interaction when the graph of strictly positive interactions is connected. Each principal zero is constant or strictly monotone, and the entire trajectories of distinct zeros are disjoint. Theorem 2 treats Curie–Weiss quadratic magnetization tilt and proves strict decrease of the moving principal zeros, with explicit limiting positions. Proofs use finite zero ODEs and, in the second case, a cooperative dynamical system. This is among the closest precedents for designing an auxiliary parameter with provable control of zero motion.

**Scope.** arXiv Theorems 1–2, Remarks 1–4 and beginning of ODE derivation inspected; journal metadata checked. For spin count n≥2, zero-coupling Curie–Weiss zeros coincide; they are simple for positive coupling. The finite-spin ferromagnetic structure has not been established for the canonical theta source, and no arbitrary-q monotonicity follows.

<a id="ly11"></a>

### LY11 — Konstantopoulos, Patie and Sarkar (2024)

Takis Konstantopoulos, Pierre Patie and Rohan Sarkar, **A new class of solutions to the van Dantzig problem, the Lee–Yang property, and the Riemann hypothesis**, *Annales de l'Institut Fourier* **74**(1), 377–421 (2024). DOI [10.5802/aif.3600](https://doi.org/10.5802/aif.3600). [Open publisher PDF](https://www.numdam.org/item/10.5802/aif.3600.pdf).

**Result and relevance.** The paper connects normalized Laguerre–Pólya characteristic functions with reciprocal transforms through van Dantzig pairs and constructs families from self-similar Markov-process exponents. Theorem 2.3 and Corollary 2.4 give explicit RH-equivalent formulations. Theorem 4.4 supplies a real-zero subclass under a Pick-function separation hypothesis, while showing the broader constructed class can contain nonreal zeros. This gives a modern probabilistic auxiliary construction and a precise reminder that probabilistic realizability alone is weaker than Lee–Yang membership.

**Scope.** Publisher PDF §§2.1, Theorems 4.1/4.4 and associated remarks inspected; no complete proof audit. Neither membership of ξ in the new real-zero subclass nor an estimate excluding canonical collisions is established by these formulations. The distinctions between the van Dantzig class and the Lee–Yang subclass are essential.

## C. Zero dynamics, arithmetic comparisons and collision diagnostics

<a id="dy01"></a>

### DY01 — Rodgers and Tao (2020; corrected arXiv v5, 2021)

Brad Rodgers and Terence Tao, *The De Bruijn–Newman constant is non-negative*, Forum of Mathematics, Pi **8** (2020), e6. DOI [10.1017/fmp.2020.6](https://doi.org/10.1017/fmp.2020.6). [arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5), 3 July 2021; [full text](https://arxiv.org/html/1801.05914v5).

**Inspected:** introduction; Section 4, Theorem 4.16, equation (56), Lemma 4.18; Section 4's formal Hamiltonian discussion and the Section 5–9 structure. Their normalization agrees exactly with the overview. The real simple zeros obey principal-value dynamics x'_k=2 PV sum_{j≠k}(x_k−x_j)^{-1} in the contradiction regime Λ<t≤0. Localized energy and gap identities make rigorous the relaxation toward approximately equal spacing that would follow from Λ<0; known zeta pair correlation contradicts the resulting local equilibrium.

**Relevance and limit:** this is the central successful precedent for changing from the entire function to an interacting-zero observable. The argument uses global density and arithmetic zero statistics, not source positivity alone. A modified q-flow needs new zero-motion, tail and energy identities. The unlocalized infinite Hamiltonian in the motivating discussion is formal; the localized estimates do the proof work.

<a id="dy02"></a>

### DY02 — Csordas, Smith and Varga (1994)

George Csordas, Wayne Smith and Richard S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann Hypothesis*, Constructive Approximation **10** (1994), 107–129. DOI [10.1007/BF01205170](https://doi.org/10.1007/BF01205170). [Author-hosted PDF](https://www.math.kent.edu/~varga/pub/paper_206.pdf).

**Inspected:** author-hosted PDF record and indexed text of pp. 109–110, Definition 1 and Theorem 1, equations (1.13)–(1.14); related dynamics cross-referenced in Rodgers–Tao. The paper defines Lehmer pairs using both the pair gap and interaction with the remaining zeros, and turns suitable pairs into explicit lower bounds on Λ. Sufficiently many appropriately strong pairs tending toward collision imply Λ≥0.

**Relevance and limit:** the needed quantity is a gap together with the surrounding-zero contribution, rather than gap size alone. This supplies a concrete benchmark for any proposed magnifier: does it reduce the nonlocal interaction information or its evaluation cost? These are lower-bound mechanisms. Their historical bounds are superseded by Rodgers–Tao, and the method does not exclude collisions on the positive-time slice. The PDF did not expose a continuous text layer to the browsing tool; inspection was limited to the stated indexed passages.

<a id="dy03"></a>

### DY03 — Stopple (2017)

Jeffrey Stopple, *Lehmer Pairs Revisited*, Experimental Mathematics **26** (2017), no. 1, 45–53. DOI [10.1080/10586458.2015.1107870](https://doi.org/10.1080/10586458.2015.1107870). [arXiv:1508.05870v2](https://arxiv.org/abs/1508.05870v2), 11 October 2015; [full text](https://arxiv.org/html/1508.05870v2).

**Inspected:** Sections 3–5; Theorem 1, pre-Schwarzian definition and equations (6)–(10); abstract's Theorem 2–3 summary. Assuming RH, the paper introduces strong Lehmer pairs through derivatives of PΞ=Ξ''/Ξ' at consecutive zeros and proves these satisfy the classical Lehmer-pair criterion. Further results link the diagnostic to derivatives of ζ and nearby zeros of ζ'.

**Relevance and limit:** this is a precedent for replacing a sum over the other zeros by locally evaluated higher jets. It is especially close to the overview's question of changing observable together with flow. The ratios contain inverse Ξ', so conditioning worsens near a multiple root; the derivative representation does not remove that problem. RH is an explicit premise throughout and prevents importing the criterion as an unconditional collision exclusion argument. Ξ(t)=ξ(1/2+it) uses ordinate t=z/2 relative to the overview; derivative/gap constants require rescaling.

<a id="dy04"></a>

### DY04 — Dobner (2021; revised arXiv v2, 2026)

Alexander Dobner, *A proof of Newman's conjecture for the extended Selberg class*, Acta Arithmetica **201** (2021), 29–62. DOI [10.4064/aa200603-23-7](https://doi.org/10.4064/aa200603-23-7). [arXiv:2005.05142v2](https://arxiv.org/abs/2005.05142v2), 10 January 2026; [full text](https://arxiv.org/html/2005.05142v2). The earlier title was *A New Proof of Newman's Conjecture and a Generalization*.

**Inspected:** introduction, Theorems 1–2, and equations (3) onward describing the deformed Dirichlet series. Theorem 1 establishes a de Bruijn–Newman threshold for the relevant completed functions in the extended Selberg class; Theorem 2 proves its nonnegativity. In the zeta case, a negative-time deformation is approximated by a gamma-like factor times ζ_t(s)=sum exp((t/4)log²n)n^−s, whose zeros yield off-line zeros of the deformed completed function. The method avoids detailed zeta-zero statistics.

**Relevance and limit:** it offers an arithmetic alternative to particle dynamics, using the source's Dirichlet-series structure. It suggests asking how an auxiliary tilt transforms that structure. It does not prove RH or prevent positive-time collisions, and is not a theorem for arbitrary positive Fourier densities.

<a id="dy05"></a>

### DY05 — Farmer and Rhoades (2005)

David W. Farmer and Robert C. Rhoades, *Differentiation evens out zero spacings*, Transactions of the American Mathematical Society **357** (2005), no. 9, 3789–3811. DOI [10.1090/S0002-9947-05-03721-9](https://doi.org/10.1090/S0002-9947-05-03721-9). [arXiv:math/0310252v3](https://arxiv.org/abs/math/0310252v3), 26 April 2004; [full text](https://arxiv.org/html/math/0310252v3).

**Inspected:** Theorems 2.1.1, 2.3.1 and 2.4.1–2.4.3, plus their scope discussion. For real-rooted polynomials multiplied by a real exponential, differentiation plus a real multiple of the original does not decrease the minimum gap. For order-one real entire functions with only real zeros, consecutive gaps of f'+af lie between the infimum and supremum of the original gaps. Under balanced linear zero-counting asymptotics, normalized high derivatives tend locally to cosine.

**Relevance and limit:** differentiation and combinations of adjacent derivative channels offer auxiliary observations with real-zero preservation under stated hypotheses. The all-real-zero premise already assumes the desired geometry on the input slice. The balanced linear-density cosine theorem does not apply directly to ξ's r log r zero density. The paper separately cites Ki's ξ-specific high-derivative limit; that imported theorem was not independently checked here.

<a id="dy06"></a>

### DY06 — Dyson (1962)

Freeman J. Dyson, *A Brownian-Motion Model for the Eigenvalues of a Random Matrix*, Journal of Mathematical Physics **3** (1962), 1191–1198. DOI [10.1063/1.1703862](https://doi.org/10.1063/1.1703862). [Publisher record](https://pubs.aip.org/jmp/article/3/6/1191/230695/A-Brownian-Motion-Model-for-the-Eigenvalues-of-a).

**Inspected:** publisher abstract; Rodgers–Tao Section 4, footnote 14 explicitly checks the connection. Matrix Brownian motion produces interacting eigenvalues described by a one-dimensional Coulomb gas, with the inverse-gap drift that motivates local-equilibrium ideas.

**Relevance and limit:** the overview's zero ODE shares the repulsive deterministic drift, and Rodgers–Tao expressly drew on equilibrium methods associated with Dyson dynamics. This is a source of energy and localization techniques. A deterministic theta-zero trajectory is not a sample of Dyson Brownian motion. Random-matrix level repulsion and almost-sure stochastic noncollision do not prove deterministic noncollision for a canonical entire function. Any stochastic auxiliary flow would require an exact comparison or recovery statement linking its observations to the original slice, and the Brownian noise changes the relevant evolution and precision accounting. No stochastic theorem is imported from an abstract-level inspection.

<a id="dy07"></a>

### DY07 — Freire et al. (2026 preprint)

Ricardo Freire, Cristian González-Riquelme, Claudio Muñoz, Felipe Poblete and Vicente Salinas, *Upper Bounds on the de Bruijn–Newman constant for Dirichlet L-functions with primitive real-valued characters*, [arXiv:2610.27343v1](https://arxiv.org/abs/2610.27343v1), 19 October 2026; [full text](https://arxiv.org/html/2610.27343v1). No journal publication was listed on the arXiv page inspected.

**Inspected:** abstract, Theorem 1.1, Lemma 3.3 and the Section 8 discussion giving 953/3200. This preprint reports an unconditional uniform bound Λ_L≤953/3200 for primitive real characters with conductor 3–400, by extending Polymath's approximation, retaining conductor dependence, and combining Platt's finite verification with interval calculations. Separate results using an improved global initial strip, including |Im z|≤3/4, are expressly conditional.

**Relevance and limit:** it gives a recent example of the exact comparison contracts an auxiliary method would need before changing a threshold conclusion: an initial strip, effective exterior approximation and finite barrier conditions. It keeps the standard quadratic deformation. The reported certificate suite was not replayed here; record it as a preprint's claimed result with the stated finite conductor scope, not a new bound for zeta or all conductors.

<a id="dy08"></a>

### DY08 — Texier (2018 issue; published 2019)

Benjamin Texier, *Basic matrix perturbation theory*, L'Enseignement Mathématique **64** (2018), no. 3/4, 249–263; published 24 July 2019. DOI [10.4171/LEM/64-3/4-1](https://doi.org/10.4171/LEM/64-3/4-1). [Publisher page](https://ems.press/journals/lem/articles/16370), [full PDF](https://ems.press/content/serial-article-files/44369).

**Inspected:** Section 4, Proposition 4.2, pp. 260–262, and Remark 4.3. This expository primary source proves Puiseux descriptions near coalescing eigenvalues, along with regularity statements for total spectral projectors; its bibliography identifies Kato's classical perturbation theory. The remark distinguishes the especially regular analytic Hermitian case.

**Relevance and limit:** analytic local polynomial factors of an entire function can be represented by companion matrices, connecting double zeros to the same square-root branch geometry. This is a mathematical analogy supporting the overview's analytic squared gap; that companion-matrix application is an inference, not a theorem for theta flows in this article. Hermitian degeneracies need not have square-root splitting; branch exponents depend on the perturbation and nondegeneracy assumptions. A blow-up of individual root derivatives is generic conditioning behavior and supplies neither improved diagnostic precision nor collision exclusion.

<a id="dy09"></a>

### DY09 — Nennig, Ghienne and Perrey-Debain (2026)

Benoit Nennig, Martin Ghienne and Emmanuel Perrey-Debain, *Fast recovery of parametric eigenvalues depending on several parameters and location of high order exceptional points*, Journal of Computational Physics **551** (2026), 114692. DOI [10.1016/j.jcp.2026.114692](https://doi.org/10.1016/j.jcp.2026.114692). [arXiv:2505.06141v2](https://arxiv.org/abs/2505.06141v2), 22 January 2026; [full text](https://arxiv.org/html/2505.06141v2).

**Inspected:** introduction equations (3)–(5), Section 2's partial characteristic polynomial construction, Section 3, Appendix B equations (56)–(58). The method recombines selected eigenvalues into regular polynomial coefficients. For a double event it uses g=λ_++λ_- and h=(λ_+−λ_-)², continuing these analytic quantities rather than singular individual branches. A partial discriminant generalizes the collision diagnostic to a root cluster.

**Relevance and limit:** this is a direct computational analogue of the overview's analytic squared gap and multi-parameter collision curve. It offers established numerical ideas for continuing or locating collisions. Its demonstrations concern discretized matrix problems; convergence-domain control for retained eigenvalue subsets is explicitly not fully resolved. Roundoff, truncation and omitted-root interactions need fresh estimates for theta zeros. No certified theta computation or cost advantage follows from this analogy.

<a id="dy10"></a>

### DY10 — Langbein (2018)

Wolfgang Langbein, *No exceptional precision of exceptional-point sensors*, Physical Review A **98** (2018), 023805. DOI [10.1103/PhysRevA.98.023805](https://doi.org/10.1103/PhysRevA.98.023805). [arXiv:1801.05750v3](https://arxiv.org/abs/1801.05750v3), 27 June 2018; [full text](https://arxiv.org/html/1801.05750v3).

**Inspected:** introduction, Sections III.2–III.3, equation (25), conclusions. In the studied coupled-mode sensor model, square-root eigenfrequency splitting does not yield the promised exceptional precision: the detected signal and its noise must be propagated together. Near degeneracy, individual mode quantities can change strongly while the measurable response remains regular.

**Relevance and limit:** this directly supports the overview's insistence on normalization, propagated error and observation cost before claiming a better diagnostic. It is an analogy about inference from branch sensitivity, not an obstruction theorem for deterministic Fourier-integral computation. A theta-specific advantage remains possible with a stated measurement/evaluation model and proven error budget. Eigenvalue splitting alone is insufficient evidence for that advantage. The published model's noise calculation must not be transferred quantitatively to mathematical root finding without a matching model.

## D. Parabolic zero counting, total positivity and the cosine kernel

<a id="ax01"></a>

### AX01 — Schoenberg (1948): variation-diminishing convolution

Isaac Jacob Schoenberg, *On Variation-Diminishing Integral Operators of the Convolution Type*, Proceedings of the National Academy of Sciences USA **34**(4) (1948), 164–169. [DOI](https://doi.org/10.1073/pnas.34.4.164).

**Result and relevance.** The paper characterizes variation-diminishing convolution operators through Pólya frequency kernels. Its p.165 equations (4)–(6) connect their bilateral Laplace transforms with reciprocals of Laguerre–Pólya functions. This supplies an established mechanism for controlling real sign variation under an auxiliary convolution. The Toeplitz kernel must be totally nonnegative; a positive integrable density alone does not give that property. The reciprocal Laplace-transform statement is different from asking that the Fourier transform of the source have only real zeros.

**Inspection and limit.** Publication metadata and selected original-PDF passages exposed by indexing were checked. Direct PMC retrieval returned a browser challenge; the entire original proof was not read. AX03 provides a separately checked modern statement of the transform dictionary.

<a id="ax02"></a>

### AX02 — Schoenberg (1951): the complete Pólya frequency theory

Isaac Jacob Schoenberg, *On Pólya frequency functions. I. The totally positive functions and their Laplace transforms*, Journal d'Analyse Mathématique **1** (1951), 331–374. [DOI](https://doi.org/10.1007/BF02790092).

**Result and relevance.** This is the foundational full treatment of Pólya frequency functions and their bilateral-Laplace characterization. It is the original reference behind the explicit theorem restated in AX03, Theorem 2.2. For the present investigation it identifies a precise stronger kernel property that could justify a variation-diminishing auxiliary evolution; source positivity should not be substituted for it. A theorem about the reciprocal transform also requires the correct transform variable and domain.

**Inspection and limit.** The publisher's title, year, volume and pages were verified. The original was subscription-preview only and its proof was not inspected; no numbered original theorem is imported here. Mathematical details used in this survey come from the separately checked 1948 announcement and 2022 restatement. This entry preserves original attribution rather than claiming an additional full reading.

<a id="ax03"></a>

### AX03 — Belton, Guillot, Khare and Putinar (2022): which positivity survives which operation

Alexander Belton, Dominique Guillot, Apoorva Khare and Mihai Putinar, *Preservers of totally positive kernels and Pólya frequency functions*, Mathematics Research Reports **3** (2022), 35–56. [DOI](https://doi.org/10.5802/mrr.12); [open PDF](https://www.numdam.org/item/10.5802/mrr.12.pdf).

**Result and relevance.** Definition 2.1 and Theorem 2.2 state the PF/reciprocal-Laplace dictionary. Theorem 5.4 shows that pointwise composition preserves every PF function only for positive homotheties. Theorems 4.3–4.4 distinguish special densities whose integer powers remain PF from generic Hirschman–Widder densities that fail under nontrivial polynomial composition. These results help distinguish ordinary positivity, positive semidefiniteness, total positivity, convolution and nonlinear source changes.

**Inspection and limit.** The stated sections and theorems were inspected in the publisher PDF. These rigidity statements concern specified pointwise compositions on whole classes. Multiplication by a fixed function exp(sq(u)), a flow generator and a source-specific estimate are different operations; this paper does not by itself exclude them or prove canonical theta noncollision.

<a id="ax04"></a>

### AX04 — Angenent (1988): the original parabolic zero-set theorem

Sigurd Angenent, *The zero set of a solution of a parabolic equation*, Journal für die reine und angewandte Mathematik **390** (1988), 79–96. [DOI](https://doi.org/10.1515/crll.1988.390.79); [public institutional scan](https://math.jhu.edu/~js/Math745/angenent.par1.pdf).

**Result and relevance.** The paper is the foundational source for the scalar one-dimensional parabolic zero-number theorem: under its regularity and boundary hypotheses, the number of zeros is nonincreasing in forward parabolic time and drops at multiple zeros. It supplies a rigorous collision-counting context for second-order auxiliary PDEs. The usable hypotheses in this survey are taken from the author's own restatement in AX05.

**Inspection and limit.** The original title and publication record were checked, but the web reader exposed only the scanned cover; direct retrieval returned HTTP 403. The original proof was not inspected. AX05's theorem pages were rendered and visually checked. No global count for the infinitely many theta zeros is inferred from a finite-interval theorem.

<a id="ax05"></a>

### AX05 — Angenent (1991): explicit hypotheses and the local collision picture

Sigurd Angenent, *Nodal properties of solutions of parabolic equations*, Rocky Mountain Journal of Mathematics **21**(2) (1991), 585–592. [DOI](https://doi.org/10.1216/rmjm/1181072953); [author PDF](https://people.math.wisc.edu/~angenent/preprints/1987NodalPropertiesRMMJ.pdf).

**Result and relevance.** Section 2, Theorem A treats classical scalar solutions of u_r=a u_xx+b u_x+c u on a finite rectangle, with a>0, the displayed coefficient regularity and nonzero endpoint values. Positive-time zero counts are finite and decrease across a multiple zero. The next page gives the local heat-polynomial expansion and discusses periodic boundaries. This links the overview's double-event expansion with established parabolic geometry.

**Inspection and limit.** Pages 585–586 were rendered and visually read because text extraction had broken font encoding. Newman time has the opposite orientation: u(r,x)=H(−r,x) solves forward heat. Fourth-order equations, real-shift nonlocal equations and systems require separate theorems. No finite global count or theta-specific lower margin follows from this statement.

<a id="ax06"></a>

### AX06 — NIST DLMF: the cosine tilt's exact Bessel expansion

NIST Digital Library of Mathematical Functions, *§10.35, Generating Function and Associated Series*, online reference accessed 28 October 2026. [Equation 10.35.1](https://dlmf.nist.gov/10.35.E1), [equation 10.35.2](https://dlmf.nist.gov/10.35.E2), [equation 10.35.5](https://dlmf.nist.gov/10.35.E5).

**Result and relevance.** These identities expand exp(s cos θ) into modified Bessel coefficients and evaluate their total sum. They give the exact translate representation (S1). For s≥0, the normalized coefficients are nonnegative and sum to one, producing (S2) and real-line sup-norm control. This locates the overview's nonlocal generator within classical special-function and jump-semigroup theory.

**Inspection and limit.** The official equations were checked directly. Applying them to the theta integral and identifying the probability kernel are elementary deductions in this note, not claims that DLMF treats theta collisions. The probability interpretation has a one-sided parameter restriction. Evaluation still requires translated observations and a series-tail bound; no zero-preservation or speedup theorem is supplied.

<a id="ax07"></a>

### AX07 — Skellam (1946): the normalized translation kernel's probability law

John Gordon Skellam, *The Frequency Distribution of the Difference between Two Poisson Variates Belonging to Different Populations*, Journal of the Royal Statistical Society **109**(3) (1946), 296. [DOI](https://doi.org/10.1111/j.2397-2335.1946.tb04670.x).

**Result and relevance.** The difference of two independent Poisson variables has the distribution now bearing Skellam's name. In the symmetric case with means s/2, its mass at integer n is e^(−s)I_n(s). Thus the normalized cosine-flow translation in (S2) has a standard probabilistic interpretation. The independent Poisson generating functions verify the identity directly and identify the shift variance a²s.

**Inspection and limit.** Publisher metadata and the preview record were inspected; the original full text was not obtained. No original theorem is imported beyond the bibliographic identification. The probability formula used here was independently derived from the two generating functions. A random-walk representation controls averaging, but does not make the canonical deterministic zeros stochastic or transfer stochastic noncollision results to them.

## Use of this bibliography

The common contribution of these sources is a set of precise comparison frameworks: operator symbols, admissible interacting measures, localized zero energies, analytic discriminants and specified normed function spaces. Their applications have different hypotheses. The bibliography records connections worth retaining during brainstorming without turning them into a selected program.

The two-parameter identities and the exact controls in the introductory discussion were checked algebraically by the drafting assistant. A bounded same-model reread checked the source-to-entry mappings and transfer qualifications, and prompted small hypothesis clarifications. No independent specialist mathematical review, certified theta computation, or measured diagnostic gain is claimed. The forty entries retain their individual reading scopes; a bibliography entry is not a verification of its complete proof.
