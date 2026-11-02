# RH formulations, the role of concavity, and a research direction

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**.

**Status: mathematical explanation and research-strategy assessment.** The user's steering is to use earlier investigations as a toolkit for a more direct RH program; their unfinished heat-flow questions do not determine this investigation's agenda. Classical RH equivalences below are reference points, not new results. No new sufficient theta estimate is adopted or claimed. The elementary diagnostic in Section3 has an explicit algebraic proof and exact-arithmetic checks, but no independent specialist review and no novelty claim.

Companion notes: [literature survey](01_LITERATURE_TECHNIQUES_AND_RADIAL_INHERITANCE_20261101.md), [theta differential closure](02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md), and [additional source records](../references/04_RH_FORMULATION_SOURCES_20261101.md). Read with the [result index](../../../../result-summaries/README.md), particularly [theta identities](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), particularly [reformulations](../../../../avoid/01_restating_the_target.md), [shape-only implications](../../../../avoid/02_shape_only_arguments_and_the_controls.md), and [unchecked imports](../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## 1. The broader objective

The ultimate analytic goal is to prove that the complete theta cosine transform
\[
H(z)=\int_0^\infty\Phi(u)\cos(zu)\,du
\]
has only real zeros. This is RH in the normalization used here. It does not require proving that all zeros are simple. A useful research program seeks an exact structure of the canonical theta source that forces this zero property, or a genuinely new estimate toward an established complete criterion.

The useful distinction is between three kinds of achievement:

1. A source inequality, such as a concavity theorem, is a theorem about theta and can be valuable independently of RH.
2. A transfer theorem identifies exactly which coefficient or spectral inequalities follow from it.
3. A complete mechanism controls an RH-equivalent family in all its parameters. An identity giving that family is a reformulation; a new inequality or factorization that actually controls it is the missing progress.

The present tools fit the source-to-coefficient determinant route most naturally. My recommendation is a strategy judgment about that fit, not a claim that this is the most likely route to an RH proof among all approaches.

## 2. What the concavity statements imply

The connection between real zeros and concavity begins on the spectral side. For a real-rooted polynomial, and for the corresponding canonical product of H under RH, logarithmic differentiation away from zeros gives
\[
-\frac{d^2}{dz^2}\log|H(z)|=\sum_\rho\frac{m_\rho}{(z-\rho)^2}\ge0\quad(z\in\mathbb R).
\]
Consequently \(H'^2-HH''\ge0\), with the inequality extending through real zeros. Here the absolute value matters: H changes sign. A source-concavity statement concerns a different function before Fourier transformation, so a transfer theorem is needed to extract even a necessary zero condition from it.

Set
\[
S(x)=\Phi(\sqrt x),\qquad \mathcal L[f]=(f')^2-ff''.
\]
The assertion in question is
\[
\mathcal L[S]>0,\qquad (\log\mathcal L[S])''<0.
\tag{1}
\]
The second inequality is equivalently \(\mathcal L[\mathcal L[S]]>0\). It is not an established RH criterion. The relevant implication is the sufficient kernel condition of **Csordas–Dimitrov (2000), Theorem2.4(b)**. For an admissible kernel, strict concavity of both \(\log S\) and \(\log\mathcal L[S]\) implies double Turán inequalities for
\[
b_n=\int_0^\infty u^{2n}\Phi(u)\,du,
\qquad \gamma_n=\frac{n!}{(2n)!}b_n.
\]
Writing
\[
T_n=\gamma_n^2-\gamma_{n-1}\gamma_{n+1},\qquad
E_n=T_n^2-T_{n-1}T_{n+1},
\]
ordinary and double Turán inequalities are \(T_n\ge0\), \(E_n\ge0\), respectively. RH implies these coefficient inequalities; the source condition is another way to establish them. This does **not** reverse the implication from RH to necessary tests. Nor should one silently identify a sufficient source hypothesis with a necessary source characterization of all-real Fourier zeros.

The original [Csordas–Dimitrov paper](https://www.dcce.ibilce.unesp.br/~dimitrov/papers/varga.pdf), Definition2.2, imposes positivity, strip analyticity, evenness, decrease and super-Gaussian derivative decay; Theorem2.4 retains those assumptions, and Remark2.5 discusses relaxation. [Csordas's later account](https://arxiv.org/html/1309.0055v2), Open Problem4.14, explicitly describes the desired consequence as necessary-condition progress. The [Planat–Solé preprint](https://arxiv.org/html/2608.19160v1#S7) reports a proof of (1), with the same scope; its certificates have not been independently audited here.

One useful order-two comparison is exact. Define the Jensen polynomial
\[
J_\gamma^{2,n}(X)=\gamma_n+2\gamma_{n+1}X+\gamma_{n+2}X^2.
\]
Its discriminant is \(4T_{n+1}\). Ordinary Turán is thus precisely the quadratic Jensen condition. The double Turán expression is another structured determinant:
\[
E_n=\gamma_n\det[\gamma_{n+j-i}]_{i,j=0}^2,\quad n\ge2.
\tag{2}
\]
This follows from the Desnanot–Jacobi identity. It must not be identified with every cubic Jensen condition or with all Toeplitz minors of a different coefficient normalization.

## 3. Why iterating source concavity is not automatically a complete criterion

There is a simple exact diagnostic. Take
\[
P(x)=x^2+6x+17,\quad Q(x)=x^2+6x+1,
\quad S_0(x)=e^{-x}P(x),\quad\phi_0(u)=S_0(u^2).
\]
Both polynomials are positive on \(x\ge0\), and direct differentiation gives
\[
\mathcal L[P]=2Q,\qquad\mathcal L[Q]=2P.
\tag{3}
\]
Since \(\mathcal L[e^{-ax}f]=e^{-2ax}\mathcal L[f]\),
\[
\mathcal L^{\circ j}[S_0](x)=2^{2^j-1}e^{-2^jx}
\begin{cases}P(x),&j\text{ even},\\Q(x),&j\text{ odd}.
\end{cases}
\tag{4}
\]
Every iterate is positive and strictly log-concave on the source half-line. Nevertheless the cosine transform is
\[
\int_0^\infty\phi_0(u)\cos(zu)\,du
=\frac{\sqrt\pi}{32}e^{-z^2/4}
\bigl[z^4-36z^2+332\bigr].
\tag{5}
\]
The polynomial equals \((z^2-18)^2+8\): it has no real zeros and has four nonreal zeros. Formula(5) follows by differentiating the Gaussian cosine transform twice and four times. Thus even the entire scalar iteration chain on the source half-line does not generally force real Fourier zeros. This example has Gaussian decay, so it is not itself in the stricter admissible class just quoted.

For completeness, the failure of the **first two levels** persists inside that admissible class. Set
\[
S_\varepsilon(x)=e^{-x-\varepsilon x^2}P(x),\qquad
\phi_\varepsilon(u)=e^{-u^2-\varepsilon u^4}P(u^2),\quad\varepsilon>0.
\]
Writing \(R_\varepsilon=2Q+2\varepsilon P^2\),
\[
\mathcal L[S_\varepsilon]=e^{-2x-2\varepsilon x^2}R_\varepsilon>0.
\]
The polynomial controlling its second iterate is
\[
\begin{aligned}
N_\varepsilon&=(R_\varepsilon')^2-R_\varepsilon R_\varepsilon''
+4\varepsilon R_\varepsilon^2\\
&=8P+24\varepsilon P^2+48\varepsilon^2P^2Q+16\varepsilon^3P^4>0.
\end{aligned}
\tag{6}
\]
Consequently both concavity statements hold for every \(\varepsilon>0\). The source is positive, even, entire and strictly decreasing for \(u>0\), since \(P-P'=x^2+4x+11>0\); every derivative has the required super-Gaussian decay.

As \(\varepsilon\downarrow0\), its Fourier transforms converge locally uniformly in the complex plane to (5): on a compact frequency set the integrands are dominated by a Gaussian times a polynomial times \(e^{M|u|}\). Choose a small disk about any simple nonreal zero of (5), avoiding the real axis. Rouché's theorem preserves a nonreal zero for all sufficiently small positive \(\varepsilon\). No explicit numerical value of that threshold is asserted. This is a counterexample to the general sufficiency of the two source-concavity statements, not a theta counterexample or an objection to methods that use additional exact theta identities.

The [exact algebra check](../numerics/source_concavity_diagnostic.py) verifies (3), (5)'s polynomial and (6), with [execution record](../numerics/SOURCE_CONCAVITY_DIAGNOSTIC_20261101.json). It is not a numerical test of RH. Related Gaussian-polynomial diagnostics appear in Csordas, Example3.12; the particular elementary construction here carries no novelty claim. No all-iterate assertion is made for \(\varepsilon>0\).

There is also the heat covariance already derived in Note02:
\[
\mathcal L^{\circ j}[e^{\tau x}S]
=e^{2^j\tau x}\mathcal L^{\circ j}[S].
\]
Any such source-iterate sign, if established, is insensitive to heat time. The canonical Jacobi system contains additional information; one should not discard it and expect the resulting scalar shape conditions to locate a heat threshold.

## 4. The formulation most naturally suited to these tools

Use the entire squared-variable transform
\[
F(w)=H(i\sqrt w)=\sum_{n\ge0}c_nw^n,
\qquad c_n=\frac{b_n}{(2n)!}>0,
\qquad \gamma_n=n!c_n.
\tag{7}
\]
Evenness removes the square-root ambiguity. RH says exactly that the zeros of \(F\) are negative real. For this order-one-half entire function, the classical Aissen–Schoenberg–Whitney–Edrei characterization gives
\[
\boxed{\mathrm{RH}\ \Longleftrightarrow\ (c_n)\in\mathrm{PF}_\infty
\ \Longleftrightarrow\ \text{every finite minor of }[c_{j-i}]_{i,j\ge0}\text{ is nonnegative},}
\tag{8}
\]
with \(c_n=0\) for \(n<0\). Here PF means Pólya frequency. This classical equivalence is explained in [Katkova, TheoremC and its application to xi](https://arxiv.org/html/math/0505174v1).

The reason to favor this formulation is practical. Our current tools concern determinants, normalized source moments, preservation of signed products, exact differential relations and rigorous tails. These are compatible with a coefficient-matrix problem before the oscillatory cosine integration. There is still no established all-order transfer from the Jacobi ODE to (8).

The matrices must be distinguished carefully:

| Object | Relevant property | Meaning |
| --- | --- | --- |
| Raw moment matrix \([b_{i+j}]\) | Positive semidefinite | Automatic from a positive source; does not imply RH |
| Source derivative matrix \([S^{(i+j)}(x)]\) | Selected alternating determinant signs | Source concavity and higher shape information |
| Ordinary coefficient Toeplitz matrix \([c_{j-i}]\) | Every minor nonnegative | Exact RH formulation |
| Exponential coefficients \(\gamma_n=n!c_n\) | Every Jensen polynomial hyperbolic | Another exact RH formulation |

The consecutive coefficient minors
\[
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1}
\]
are useful observables. Passing from this selected family to all minors requires the correct theorem: strict consecutive positivity with its hypotheses is available; weak nonnegativity of an arbitrary selected family must not be substituted for total positivity. [Lin–Shi (2026), Lemma4.4 and Section6](https://hexagonmath.org/2610.00521v1) discusses this distinction. The exact coefficient evolution in that paper can be retained if heat deformation later helps; it does not oblige this investigation to use heat flow.

## 5. Jensen and spectral formulations as companion viewpoints

The classical Jensen criterion states that every
\[
J_\gamma^{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j
\]
must have only real zeros, for every \(d,n\ge0\). In fact all degrees at shift \(n=0\) suffice. [Griffin–Ono–Rolen–Zagier, Introduction](https://arxiv.org/html/1902.07321v1) states this precisely. This is a helpful way to explain why a quadratic or double Turán theorem is incomplete: the unbounded degree requirement remains. It is not the claim that an arbitrarily large finite set of successful tests would establish RH.

A genuinely different complete hierarchy acts on the **spectral transform**. Define
\[
|H(x+iy)|^2=\sum_{n=0}^\infty\Lambda_n[H](x)y^{2n},
\]
where
\[
\Lambda_n[H](x)=\frac1{(2n)!}\sum_{j=0}^{2n}(-1)^{j+n}
\binom{2n}{j}H^{(j)}(x)H^{(2n-j)}(x).
\]
For this entire function, all \(\Lambda_n[H](x)\ge0\), for every \(n\) and real \(x\), is an RH-equivalent condition. The first two nontrivial expressions are
\[
\Lambda_1=H'^2-HH'',\qquad
\Lambda_2=\frac{HH^{(4)}-4H'H^{(3)}+3H''^2}{12}.
\]
This \(\Lambda_2\) is not \(\mathcal L[\mathcal L[H]]\), and neither is a source derivative of \(S\). The generalized hierarchy corresponds to positive definiteness of the associated kernels
\[
K_n(v)=\int_{\mathbb R}u^{2n}\Phi(u+v)\Phi(u-v)\,du.
\]
For the half-line normalization here, the exact constant is
\[
\Lambda_n[H](x)=\frac{2^{2n-1}}{(2n)!}
\int_{\mathbb R}K_n(v)\cos(2xv)\,dv.
\]
This follows from the full-line formula in [Csordas, Theorems2.4 and3.7](https://arxiv.org/html/1309.0055v2); the printed half-line statement has a normalization inconsistency already documented in the opening bibliography.

This spectral route would become preferable if an exact theta addition or product identity yielded a usable Gram representation for these correlations. Its low-order milestone is more directly zero-sensitive than another source-concavity iterate, but global positive definiteness remains difficult. A first spectral Laguerre inequality alone is not the complete hierarchy.

The sufficiency of the full hierarchy has a direct explanation. At a nonreal zero x+iy with y nonzero, the sum defining |H(x+iy)| squared would vanish despite all its terms being nonnegative. If H(x) is nonzero the constant term prevents this. If H has a zero of order m at x, the coefficient of y to the power 2m is the positive number |H^(m)(x)/m!| squared, again preventing it. Positivity of only the first coefficient gives no such argument.

## 6. Where existing literature places the difficult regime

The distinction is not simply finite versus infinite numbers of inequalities: an all-index theorem at fixed order is already infinite. The crucial missing uniformity is in **order as well as index**.

- Katkova proves fixed-order asymptotic multiple positivity. Her Section2 gives an integral representation of coefficient determinants using a Vandermonde-square factor, but also a complex oscillatory product; the square alone does not sign the integral.
- [Griffin et al., Theorem1.1](https://arxiv.org/html/1910.01227v3) prove Jensen hyperbolicity in a region \(n\ge c e^{d/2}\). This still leaves unbounded degree at small shift. Their finite verified-zero consequences should not be read in reverse.
- [Michałowski (July2026), Theorem1.1](https://arxiv.org/html/2607.16795v1) reports \(D_{r,k}>0\) for \(k\ge10^{18}r^3\). It is a uniform-in-order tail claim, not all-order positivity at small index. The paper and certificates have not been audited here.
- [Sra (October2026)](https://suvrit.github.io/papers/csordas/) reports reverse regularity of \(S(x+y)\) through order four and failure at order five. This cautions specifically against extending that source-kernel sign pattern to every order. It is not a failure of the coefficient Toeplitz criterion or evidence against RH; the reported certificate was not rerun here.

[Farmer's analysis](https://arxiv.org/html/2008.07206v2) gives an additional reason to demand more than generic asymptotic behavior: Hermite limits can reflect smoothing under differentiation, rather than arithmetic information excluding an off-line zero. This is a caution about a mechanism, not an impossibility theorem for every coefficient approach.

## 7. Recommended research emphasis and inherited tools

I would organize the next discussion around **theta-specific determinant inequalities for the ordinary coefficients**, with (8) as the fixed destination and Jensen hyperbolicity as a companion description. Source concavity supplies examples and low-order inputs, not the entire proposed induction. A general theorem for arbitrary determinant order, or a genuinely new region with order and index controlled together, would be a meaningful intermediate outcome. Reproving known low-order statements is useful validation only if it tests a mechanism that extends further.

The first bounded question is whether the Jacobi differential algebra yields a relation among the **integrated coefficient determinants** that has a favorable sign and retains the theta information. A relation among pointwise derivatives alone is insufficient. The source-side derivative order and the coefficient-matrix order are different parameters; a recurrence connecting them must be derived rather than assumed. Any next estimate should state the region it actually improves relative to the known fixed-order or tail results.

The useful inheritance from Investigation05 is methodological: exact primitive integration by parts with both boundary terms; full-source normalization and derivative identities; forming a signed quadratic or determinant expression before bounding its parts; compact interval certification joined to analytic tail control; and controls that reveal when an argument uses only generic source shape. These can be used at heat time zero. Conservative feedback, radial drift choices and collision deadlines are not standing requirements for the new program.

No new theta sufficiency claim is introduced here, so the registered controls are not presented as having passed or failed a new premise. The explicit diagnostic in Section3 screens only scalar source concavity. Once a concrete determinant estimate is proposed, the [existing controls](../../../../result-summaries/12_collision_controls_and_screening.md) must be checked against its actual hypotheses. Full canonical theta data can identify the source, but identification does not establish the missing sign.

The reason to favor this route is that it matches the available algebra while keeping a complete RH criterion visible. The reason to remain selective is that no scalable sign-preserving bridge from the Jacobi state to all coefficient minors has yet been found. Finding that bridge, or proving a new quantitative part of it, is the substantive research task.
