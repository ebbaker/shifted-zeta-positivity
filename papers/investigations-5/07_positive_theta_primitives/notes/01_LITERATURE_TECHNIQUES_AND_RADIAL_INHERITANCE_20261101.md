# Literature techniques and the radial theta inheritance

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**.

**Status: brainstorming literature synthesis.** The useful common thread is to preserve a complete signed expression until an additional structure determines its sign: modular boundary behavior, determinant composition, or a theta-specific differential identity. Positivity of a primitive alone does not supply that structure. This note adds literature leads and compares techniques; it proposes no new RH criterion, global sign theorem, or numerical campaign. It precedes a research overview.

Read with the [result index](../../../../result-summaries/README.md), especially [theta identities](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), especially [target reformulations](../../../../avoid/01_restating_the_target.md), [separate absolute bounds](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [unchecked imports](../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

The [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md) supplies the exact normalization. The [new source records](../references/02_LITERATURE_ADDITIONS_20261101.md) preserve versions, passages inspected and limitations. The scan is selective through 1 November 2026. Statements in new preprints are reported claims, not results independently verified in this investigation.

## 1. Classical techniques and the information they add

### Convexity and integration by parts

For the half-line primitive
\[
p(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}},\qquad J(a)=\int_0^\infty p(u)\cos(au)\,du,
\]
the exact relations are
\[
p''-p=8\Phi,\quad p'(0)=-\tfrac12,\qquad
8H(0,a)=\tfrac12-(1+a^2)J(a).
\]
The differential identity gives convexity, and integration by parts yields
\[
J(a)=a^{-2}\int_0^\infty p''(u)(1-\cos au)\,du>0\quad(a\ne0).
\]
This is the productive use of Pólya's convexity criterion: it replaces an oscillatory integral by a positive one. It does not sign H, whose zeros are crossings with a particular rational profile. The [Csordas source](https://arxiv.org/html/1309.0055v2), Theorem 3.4, and the opening note distinguish this cusp-even primitive from the smooth physical source.

### Hardy's modular boundary argument

The completed primitive G has a complex-source boundary accessible through the exact theta transformation. Hardy's argument uses limiting weighted moments of Xi with alternating signs, contradicting an eventual fixed sign. The critical ingredient is modular cancellation at that boundary, not just real-axis positivity. The [Dixit–Kumar–Maji–Zaharescu account](https://arxiv.org/html/1712.08435v1), Introduction (1.1)–(1.6), connects the undifferentiated theta expression directly to this mechanism.

The result is infinitely many critical-line zeros. It neither locates every zero nor proves simplicity. The opening note's circular boundary approach is retained; no assertion about arbitrary tangential approaches is added.

### Integrated kernels and composition of determinant signs

Csordas–Norfolk–Varga use
\[
K(x)=\int_x^\infty\Phi(\sqrt v)\,dv,
\]
which differs from p and G. Their proof first establishes strict log-concavity of K. This assigns a negative sign to ordered 2-by-2 minors of K(x+y). A beta-integral identity and the determinant-of-integrals composition formula transfer that sign to gamma-normalized moments. The resulting coefficient inequalities are stronger than positivity of the unnormalized moments.

Printed pp. 523–527 of the [1986 paper](https://www.math.kent.edu/~varga/pub/paper_157.pdf) were visually inspected, including Proposition 2.1, Lemmas 2.2–2.3 and the beginning of Proposition 2.4. The detailed theta inequalities in Section 3 and first-index verification in Section 4 remain outside this reading. A useful lesson is already explicit on p. 525: log-concavity of a different, ordinary tail integral is insufficient for their purpose. The variable and normalization are part of the mechanism.

### Correlations and positive definiteness

For the associated kernel
\[
\mathcal K_1(v)=\int_{\mathbb R}\Phi(u+v)\Phi(u-v)u^2\,du,
\]
the opening note's normalization gives
\[
H_a(0,a)^2-H(0,a)H_{aa}(0,a)
=\int_{\mathbb R}\mathcal K_1(v)\cos(2av)\,dv.
\]
Csordas, Theorem 3.7, identifies **positive definiteness** as the property that signs the Fourier transform. Pointwise positivity is inadequate. The all-order associated-kernel characterization is an RH-equivalent reformulation in this setting; it is not an independently established mechanism. The constructive question would be whether a particular theta identity gives a usable Gram or determinant representation. No such representation is asserted here.

### Coefficient asymptotics and adapted bases

The 2019 Griffin–Ono–Rolen–Zagier result uses precise coefficient asymptotics to obtain a Hermite limit, giving hyperbolicity for every fixed degree at sufficiently large shift. Romik's positive-coefficient orthogonal-polynomial expansion is a different basis strategy, with no automatic real-rootedness of sums. Biane–Pitman–Yor's probability laws give exact Mellin/Laplace identities and inversion/size-bias relations; the variable whose distribution is positive or infinitely divisible must remain explicit. These three tools are already in the [opening bibliography](../references/01_ANNOTATED_BIBLIOGRAPHY_20261031.md), and none supplies the missing global spectral inequality merely by being a positive representation.

## 2. Literature missing from the opening collection

The catalog now adds nine records to the original eleven. These are omissions from Investigation07's bibliography, not a claim that no other repository investigation has encountered them.

| Source | Technique worth extracting | Scope |
| --- | --- | --- |
| [Griffin–Ono–Rolen–Thorner–Tripp–Wagner](https://arxiv.org/html/1910.01227v3), published 2022 | Hermite-basis coefficient estimates make the shift threshold effective: n >= c exp(d/2); Lemma 2.4 gives a sufficient coefficient error budget | The threshold still depends on degree. Finite verified-zero consequences are one-way implications |
| [O'Sullivan](https://arxiv.org/html/2007.13582v2), published 2021 | Hermite-weighted polynomial combinations and detailed xi coefficient asymptotics | Its P-polynomials differ from ordinary Jensen J-polynomials; introductory results inspected |
| [Ribeiro–Yakubovich](https://arxiv.org/html/2304.09545v2), 2023 | Bessel/modified-Bessel theta transformation extends the Hardy mechanism to specified Hecke-type series | Summability, bounded shifts and parameter-domain restrictions matter; infinitely many line zeros |
| [Ribeiro](https://arxiv.org/html/2401.02813v1), 2024 | Fekete–Fejér sign-change counting makes a subclass quantitative | Selected shifted combinations have a sqrt(T)/log(T) lower bound; this is not a better ordinary-zeta zero-proportion estimate |
| [Planat–Solé](https://arxiv.org/html/2608.19160v1), 19 August 2026 | Reports second-level kernel concavity using either first-theta-term/tail bounds or Jacobi differential dynamics with a cone barrier | Preprint claim; selected arguments read, certificates not rerun; source-coordinate sign, not spectral noncollision |
| [Banerjee–Bringmann–Rolen](https://arxiv.org/html/2609.14295v2), 18 September 2026 | General asymptotic framework for coefficient inequalities and partial converses to Hermite–Jensen phenomena | Adjacent toolkit; introductory assumptions inspected, applicability to our kernels unproved |
| [Liu–Mao](https://arxiv.org/html/2610.04972v1), 4 October 2026 | Reports infinite log-concavity via logarithmic-ratio recurrences, saddle estimates, finite verification and a closure argument | Preprint claim about ordinary Taylor coefficients; not all Jensen hyperbolicity |
| [Farmer](https://arxiv.org/html/2008.07206v2), published 2022 | Separates generic Hermite/differentiation behavior from information about RH | Interpretive reading lead, not an impossibility theorem against coefficient methods |
| [Dimitrov–Lucas](https://doi.org/10.1090/S0002-9939-2010-10515-4), 2011 | Older bridge between quadratic Turán inequalities and degree-three Jensen hyperbolicity | Bibliographic lead; publisher PDF inaccessible in this scan, full proof uninspected |

Two distinctions particularly affect the next discussion.

**The Planat–Solé geometry is a theta differential-state geometry.** Their autonomous variables are built from theta derivatives, and their argument concerns the distinguished Jacobi trajectory. This differs from the Euclidean radial realization of Investigation05. The potentially reusable idea is a differential identity that constrains the complete sign expression, followed by a first-contact barrier. It is not evidence that every three-dimensional realization has such a barrier.

**The Liu–Mao coefficient normalization matters.** They write xi(1/2+sqrt(x)) = sum lambda_n x^n. The exponential coefficients are n! lambda_n. A result about iterates of log-concavity for one sequence must not silently be transferred to the other. Their simultaneous control of coefficient index and iteration order is the technique to examine; its claimed infinite conclusion is not the all-minors condition for real-rootedness.

The two Sra preprints were **already collected** on 31 October. Their author pages still list the same versions: [order-four sign regularity](https://suvrit.github.io/papers/csordas/), v1 of 10 October, and [reciprocal-xi positivity](https://suvrit.github.io/papers/riem-xi/), v2 of 29 October. The first reports reverse regularity through order four, with failure at order five for its particular kernel; the second includes PF256 and finite-interval Laguerre conclusions using finite zero verification. Their specific conclusions should not be combined into a global theorem about p, G or the associated correlation kernels.

## 3. Techniques inherited from Investigation05

### Three-dimensional Green transfer

With A(r)=sum exp(-pi n^2 r^2) and r=exp(2u), the identity Phi(u)=r^(5/2) Delta_3 A(r)/2 enables Green's formula. The equivalent scalar identity is
\[
\int_0^\infty\Phi f
=\frac{f(0)}{16}+\frac{p(0)f'(0)}8
+\frac18\int_0^\infty p(f''-f).
\]
Both endpoint terms matter. This is [Note73](../../05_radial_theta_collision_geometry/notes/73_BOOK_INTEGRATION_BY_PARTS_AND_FEEDBACK_PAIRINGS_20261029.md)'s principal reusable interface. At positive physical time, the rapidly decaying p is appropriate; inserting exp(tu^2) into G's full-line transform would destroy convergence because G has only exponential tails.

### Adjoint propagation and complete derivative costs

For a common propagator, a pairing with an evolved density can be pulled back to a transported test and evaluated using the primitive identity. The exact product contains (c''-c)b+2c'b'+cb'', plus the sphere trace. [Note75](../../05_radial_theta_collision_geometry/notes/75_PRIMITIVE_TEST_COSTS_AND_SIGNED_COMPARISON_R11_20261029.md) subsequently controls the actual tests and traces using Gaussian preparation and energy estimates. Thus the earlier possible derivative-cost obstacle was resolved in its declared prepared class. A favorable signed production estimate or superiority to the equally informed direct method was not established.

### Signed first-jet comparison through a simple zero

The later work used (H,H_a), avoiding division by H at its zeros. It formed joint polynomial expressions before interval enclosure, used adaptive radius/degree, Taylor subtraction, and retained Gaussian slack in the complete remainder. A finite rectangle [31/128,33/128] x [64,66] crosses a simple zero while H_a stays negative. This is a real local capability, with internal assessments, but the same source information already gives a direct derivative margin. [Bottleneck Note32](../../05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/32_HIGH_HEIGHT_CANCELLATION_BOTTLENECKS_AND_TROUBLESHOOTING_20261030.md) records the source claims and limitations.

### Factorization and conservative deformations

The [radial Darboux construction](../../05_radial_theta_collision_geometry/notes/17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md) changes a forced radial equation and its test together while preserving H and its spectral multiplicities. Common conservative flows likewise preserve the complete observation. These are alternate exact representations that might expose estimates; conservation itself cannot manufacture a physical first-jet margin. Existing uniform feedback results already use such a margin.

### Endpoint diagnostics for a genuinely changed transform

Transporting only the source changes the spectral family. For the specific drift X+X/(1+|X|^2) and fixed logarithmic cosine, the transported endpoint leaves a leading sine/z term. Comparing bounded-strip zero counts with entire growth gives the [source-transport obstruction](../../05_radial_theta_collision_geometry/notes/CHAT0053_SOURCE_TRANSPORT_UNBOUNDED_STRIP_OBSTRUCTION_20261031.md): at each nonzero finite auxiliary time, zeros escape every bounded horizontal strip. Status is proved in-note with same-assistant assessment. The exclusion belongs to that family, not all transports.

### What the unsuccessful estimates teach

Primitive reconstruction cancels algebraic endpoint terms to recover a much smaller spectral quantity. Separately bounding those terms, Poisson modes, or model/remainder cross terms can lose the needed cancellation. Note32 scopes the failed absolute primitive payments, fixed Gaussian reference, fixed transport window and unsigned feedback closures. It also records what remains outside each failure. In particular, a large remainder can contribute constructively; a proof need not force every remainder to be small.

## 4. A useful next brainstorming focus

My preference is to compare **the CNV determinant-composition mechanism** with **the theta-specific differential closure used in the recent concavity preprints**, while retaining Investigation05's complete signed pairings. These are reading and derivation questions, not proposed criteria:

1. Which exact identity gives the favorable sign in each argument, and where does it use the full theta source rather than generic positivity or shape?
2. Does integrating an associated correlation object produce a tractable determinant identity? Establish its exact boundary terms and normalization before conjecturing a sign.
3. Can the resulting identity control a complete quadratic expression, allowing a constructive mixed term, instead of estimating primitive pieces separately?

Before accepting a new sign claim, the [registered controls](../../../../result-summaries/12_collision_controls_and_screening.md) must be tested against its actual hypotheses. Positive-primitive controls preserve positivity, completion and algebraic endpoint asymptotics; weighted-square controls preserve square support and finitely many endpoints but fail full reflection; reflected controls lack the complete integer-square structure; Euler-factor controls change the arithmetic coefficients. Whether any one satisfies a newly chosen Jacobi differential or integrated-correlation premise remains to be checked, not assumed. No new candidate is asserted or screened in this note.

This leaves a concrete conceptual task: identify the extra theta relation that survives integration and controls the signed interaction. The literature supplies examples of that strategy succeeding for weaker conclusions; Investigation05 supplies exact transfer formulas and precise warnings about where absolute estimates lose the information.
