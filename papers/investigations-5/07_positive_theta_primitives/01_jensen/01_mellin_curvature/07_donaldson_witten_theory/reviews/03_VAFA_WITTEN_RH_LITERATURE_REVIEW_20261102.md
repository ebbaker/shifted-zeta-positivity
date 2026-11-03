# Literature review of the Vafa–Witten connection to the Riemann hypothesis

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewer **gpt-6-astra**, actual recorded reasoning effort **xhigh**. Source-based literature assessment by one assistant, not independent specialist review.

**The relationship is already present in the published mathematics, although this search did not locate an earlier explicit statement of the exact anomaly-Mellin RH formulation in Addendum09.** Its two essential ingredients were available by 1994: the theta-valued Vafa–Witten anomaly and Riemann's theta integral. The strongest supported description is an explicit synthesis and physical interpretation of established identities. Historical priority for that synthesis remains unestablished.

This assesses [Addendum09](../../notes/09_VAFA_WITTEN_CONTINUATION_AND_BRAINSTORM_ADDENDUM_20261102.md) and the RH construction in [Return02, Sections 3–6](../notes/02_POINT_INSERTIONS_AND_VAFA_WITTEN_ANOMALY_RETURN_20261101.md). It does not audit novelty of the separate Donaldson point-insertion obstruction or execute MC07-B03. The previous [Review02](02_MC07_E02_SEPARATE_REVIEW_20261101.md) checked correctness at stated scope and explicitly did not perform a novelty review.

## Historical sources

| Source | Relevant established connection |
| --- | --- |
| [Riemann, 1859](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf), translation p.3 | Theta Mellin integral, Jacobi inversion, continuation by splitting at one, and the completed xi integral. |
| [Zagier, 1975](https://people.mpim-bonn.mpg.de/zagier/files/scanned/NombresDeClassesEtFormesModulaires/fulltext.pdf), Theorem 2, p.884 | Nonholomorphic completion of the weight-3/2 Hurwitz class-number generating function, with a unary-theta correction and theta period in its transformation law. This is the mathematical ancestry of the shadow used here. |
| [Vafa–Witten, 1994](https://arxiv.org/pdf/hep-th/9408074v2), Section 4.2, especially (4.30) and (4.32), pp.65–67 | The completed CP² numerator already has an antiholomorphic derivative proportional to the full integer-square theta sum. |
| [Manschot, 2017 preprint, v2 2018](https://arxiv.org/pdf/1709.10098v2), (2.7)–(2.9), Section 3.4 | Makes the theta shadow and nonholomorphic period explicit in the Vafa–Witten setting before 2020; develops higher-rank iterated integrals. These are not the coupling Mellin transform in Return02. |
| [Dabholkar–Putrov–Witten, 2020](https://arxiv.org/pdf/2004.14387v3), (1.2), (3.1)–(3.11), (4.38) | Supplies the modern SO(3) normalization and physical derivations of the anomaly from noncompact field space, including a two-dimensional description. |
| [Johnston–Males, 2022 preprint / 2023 publication](https://doi.org/10.1017/S001309152300041X), preprint Theorems 1.7 and 2.2 | An adjacent connection between K3 Vafa–Witten coefficient sequences and asymptotic Jensen hyperbolicity / higher Turán inequalities. It concerns different sequences and a different manifold. |

Versions, exact inspection scopes, search terms and external PDF receipts are recorded in [the source record](../../../../references/10_VAFA_WITTEN_RH_LITERATURE_SOURCES_20261102.md). Only selected relevant passages were checked; the cited papers have not received full proof audits here.

## The RH formulation follows directly from the historical formulas

Write \(y=\operatorname{Im}\tau\), \(q=e^{2\pi i\tau}\). The first equation in Vafa–Witten (4.32) is

\[
\partial_{\bar\tau}f_0(\tau,\bar\tau)
=\frac{3}{16\pi i}\,y^{-3/2}
\sum_{n\in\mathbb Z}\bar q^{n^2}.
\]

Their completed numerator is \(f_0=3\widehat h_0\). DPW uses \(Z_0=f_0/\eta^3\); the earlier partition-function convention has an additional \(\eta^{-3}\). Because eta is holomorphic, the response in Return02 can equally be written

\[
\mathcal A(\beta)
=\left.\frac{16\pi i}{3}(\beta/2)^{3/2}
\partial_{\bar\tau}f_0\right|_{\tau=i\beta/2}
=\sum_{n\in\mathbb Z}e^{-\pi\beta n^2}
=\Theta(\beta).
\]

Thus the extraction of theta is already an immediate specialization of the 1994 equation. The 2020 physics clarifies its origin; it is not required to discover the theta identity algebraically. The derivative is taken before restriction to the imaginary axis.

With \(\Theta-1=2\sum_{n\ge1}e^{-\pi\beta n^2}\), Gaussian integration gives, for \(\operatorname{Re}s>1\),

\[
\frac12\int_0^\infty(\mathcal A(\beta)-1)
\beta^{s/2-1}\,d\beta
=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Riemann's split-at-one formula, also recorded in [DLMF 25.5.13–14](https://dlmf.nist.gov/25.5#E13), then gives exactly

\[
\frac12+\frac{s(s-1)}4\int_1^\infty
(\mathcal A(\beta)-1)
\left(\beta^{s/2}+\beta^{(1-s)/2}\right)\frac{d\beta}{\beta}
=\xi(s).
\]

The zero-mode subtraction and constant \(1/2\) belong to this classical completion. Exponential decay makes the displayed integral entire in \(s\). The resulting zero-location assertion is exactly RH. **This derivation supports mathematical dependence on old results; it does not establish that an earlier author wrote down this exact physical formulation.**

## What the literature establishes about novelty

| Claim | Assessment |
| --- | --- |
| A completed CP² Vafa–Witten anomaly produces ordinary theta | Explicitly published in 1994; mathematical completion predates it. |
| The completed theta Mellin integral is xi | Classical, already in Riemann's 1859 paper. |
| The normalized anomaly can therefore be assigned a completed Mellin period equal to xi | Direct corollary of those identities. No new analytic theorem is needed for this step. |
| A previous publication explicitly gives this precise coupling-period RH equivalence | Not located in this bounded search; priority remains unresolved. |
| The anomaly supplies a new sign estimate or makes RH follow from duality | Not established by the reviewed construction or the inspected source statements. |

The noncompact-boundary mechanism is also published physics. DPW's four-dimensional calculation leaves its absolute measure normalization undetermined, and the physical sign has an orientation caveat; Return02 fixes conventions from the mathematical completion. These limitations do not invalidate the function identity, but they constrain claims about a newly constructed physical observable.

The most useful mathematical description is **the classical Mellin transform of the theta shadow of a completed Vafa–Witten partition function**. “Shadow” here means the modular function extracted from the nonholomorphic completion by a normalized antiholomorphic derivative. It is not a new spectral operator whose eigenvalues are Riemann zeros.

There is an information loss visible directly in Return02: \(\partial_{\bar\tau}\) annihilates its holomorphic class-number contribution. Those coefficients cannot supply a further estimate through this extraction alone. A separate identity could still use additional information, but it would need to show how that information reaches the complete signed Mellin observable.

Likewise, Poisson reflection of the extracted scalar theta is distinct from S-duality of one gauge sector. On the selected line \(\tau=i\beta/2\), ordinary \(S\) sends \(\beta\) to \(4/\beta\) and mixes sectors; the Mellin completion uses \(\beta\mapsto1/\beta\). Return02 already states this distinction correctly. Symmetry of xi about its critical line does not itself locate all its zeros there.

## The adjacent Jensen and Turán connection

Johnston–Males explicitly discusses RH in Section 1.2 and applies the asymptotic Hermite/Jensen method to specified K3 counting sequences. For fixed degree, hyperbolicity holds eventually in the shift index; the permitted sequences include specified arithmetic subsequences and sector restrictions. This is not simultaneous control of every degree and shift.

The paper is relevant background for the broader Jensen program. It neither identifies those counting coefficients with the canonical xi coefficients nor transfers its inequalities to the CP² anomaly period. Treating it as the missing Mellin bound would require a new comparison theorem. The preprint statements and proof route were inspected; their detailed coefficient formulas were not independently audited.

## Search scope and recommended attribution

The search on 2 November 2026 combined Vafa–Witten spelling variants and the two central arXiv identifiers with “Riemann hypothesis”, “Riemann zeta”, “xi”, “Mellin transform”, “Mellin period”, “holomorphic anomaly”, and “shadow”. It followed the 2020 references back to the original completion and checked the adjacent Jensen result. Full extracted texts of the 1994, 2018 and 2020 PDFs had no occurrence of “Mellin” or “Riemann hypothesis”; this is supplementary evidence, not proof of absence from the literature. Search engines return incomplete and sometimes loose matches; no exhaustive citation-database audit or author consultation was performed.

A keyword search also finds Witten's interview using RH as an analogy for the explanatory role of a conjecture, and an unrefereed numerical-comparison note citing DPW and Riemann-related formulas. Neither checked passage establishes the exact anomaly-period identity. The source record retains these leads and their inspection limits rather than treating co-occurrence of names as a precedent.

Suggested attribution for a later write-up:

> Combining the classical theta Mellin representation of Riemann's xi function with the CP² Vafa–Witten holomorphic anomaly, in the normalization of Dabholkar–Putrov–Witten, gives an explicit nonlocal coupling-period reformulation of RH. The construction synthesizes established identities; no priority claim or new zero-location estimate is asserted.

Addendum09's existing statement that it makes no historical novelty claim remains appropriate. Its “success” can be understood as achieving the author's requested physical dictionary. A stronger research contribution would need an independently justified estimate for the unchanged signed insertion, or another demonstrable advantage over working directly with theta. MC07-B03 remains unexecuted; this literature review supplies no new comparison domain.

This assessment follows the [result index](../../../../../../../result-summaries/README.md), especially [the theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../../../avoid/README.md), particularly [reformulation versus estimate](../../../../../../../avoid/01_restating_the_target.md) and [unchecked imports and novelty claims](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md). No new inequality is proposed or claimed to pass the [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md).

## Follow-up assessment of usefulness for proving RH

2 November 2026. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra / xhigh**. This is a strategic judgment from the existing construction and selected published identities; it does not execute MC07-B03.

**At present this is predominantly a reformulation, with no demonstrated improvement in the hard estimate. I would give it low priority as a route to proving RH, while allowing one bounded attempt to find an additional usable boundary inequality.** An equivalent formulation can be powerful when it exposes a new inequality or structure; equivalence itself is neither a benefit nor an obstruction.

The evidence for caution is specific:

- The normalized response is exactly theta. Derivatives of that equality reproduce theta derivatives; they do not by themselves add a sign theorem.
- The antiholomorphic derivative removes the holomorphic class-number series. Extra counting information therefore does not automatically reach the extracted observable.
- Return02 (12) retains the sign-changing h3 insertion and its covariance corrections. This construction has not covered even the first requested comparison interval [0,2].
- A physical Hilbert space does not identify Riemann zeros with a self-adjoint spectrum. The construction supplies a coupling integral, not that spectral identification.

There are actual physical tools in the surrounding theory. DPW Section4.4 expresses the anomaly as a boundary supercurrent insertion, and Section4.3 supplies a Hilbert-space trace with fermion parity. The PDF equations are (4.32) and (4.21), respectively; the HTML numbers are (77) and (66). The boundary identity is a potential starting point for further inserted identities, but its established evaluation already yields the theta sum. The trace is a supertrace, with a factor (-1)^F, so ordinary positivity of a thermal expectation cannot simply be assigned to it. [Primary source](https://arxiv.org/html/2004.14387v3).

The useful unanswered question is whether a further identity applies to the *complete* determinant/Mellin insertion and produces a sign or quantitative bound that is not obtained merely by differentiating the anomaly equation. A successful route must control any additional boundary, contact or mixed-insertion terms. Expressing the unknown sign as another unspecified correlator would leave the obstacle in place.

A positive-square representation, a usable bound on the signed covariance terms, or a controlled deformation preserving the exact target would materially change this assessment. These are examples of the kind of output required, not constructions supplied by this review. None follows from localization, duality or supersymmetry alone in the presently checked argument.

**Recommendation:** retain the physical dictionary, permit only the already bounded one-route feasibility check if pursued, and otherwise park this as background until an explicit identity with additional sign information is available. No broader theory search or numerical campaign is justified by the reformulation alone. This is a judgment about the current construction, not an exclusion of all gauge-theoretic approaches to RH.


## Clarification: the response is fixed, while the Mellin zero problem remains

2 November 2026. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra / xhigh**. Explanatory follow-up; no new result or execution of MC07-B03.

The physics constrains the anomaly response strongly: in the published completion and normalization it determines exactly the theta function. The missing ingredient is a further theorem about zeros after the coupling Mellin transform. Calling the original observable weakly constrained would therefore misdescribe the situation.

The selected theory is the Vafa–Witten twist of four-dimensional N=4 gauge theory on CP², with gauge group SO(3) and w2=0. Its coupling is tau=theta_YM/(2pi)+4pi i/g². Although spacetime is compact, scalar field values can escape to infinity on the Coulomb branch. The formal supersymmetric integration-by-parts argument for holomorphy then acquires a boundary contribution. In that region the gauge group reduces to U(1), and integer magnetic flux n has quadratic action, producing the term conjugate(q)^(n²). Summing the fluxes gives the theta factor in the anomaly. These statements are explained in [DPW, introduction and Sections 3–4](https://arxiv.org/html/2004.14387v3); the original anomaly is [Vafa–Witten (4.32)](https://arxiv.org/pdf/hep-th/9408074v2).

The derivative of Z is an unnormalized inserted path integral, or coupling response; division by Z would instead give a logarithmic response. The A(beta) used above rescales the former by known factors. At theta_YM=0 and tau=i beta/2 it equals Theta(beta), with beta=8pi/g². The antiholomorphic derivative must be taken before restricting tau to that line. Beta is a coupling variable here, not an asserted physical temperature.

The subsequent parameter s is introduced by integrating over beta. For s=sigma+it, the Mellin weight includes exp((it/2) log beta), allowing complex cancellations. RH is a zero-location statement for the analytically continued, completed transform. It is not a zero-location statement for Theta or Z, and no identification of those zeros with physical energy eigenvalues has been supplied. Positivity of the extracted real-coupling theta sum and the exact anomaly formula do not alone resolve this cancellation problem.

As an elementary mathematical comparison, define a self-adjoint diagonal operator on l²(Z) by H e_n=pi n² e_n. Then Tr(exp(-beta H))=Theta(beta), yet the Mellin transform of its nonzero-mode heat trace is already the classical gamma-zeta expression displayed above. Thus a self-adjoint operator whose heat trace is theta does not by itself constitute a Hilbert–Pólya realization: its eigenvalues are pi n², not Riemann-zero ordinates. This comparison is a direct calculation, not an additional identification of the Vafa–Witten Hamiltonian.

Subsequent disposition, 2 November 2026: the author authorized MC07-B03, now completed in [Return03](../notes/03_BOUNDARY_WARD_FEASIBILITY_RETURN_20261102.md) with an explicit surviving residual and no new bound. Its [self-check](04_MC07_B03_BOUNDARY_WARD_SELF_CHECK_20261102.md) is by the same assistant, gpt-6-astra / xhigh. Earlier statements that B03 was unexecuted describe this literature review at the time it was written.
