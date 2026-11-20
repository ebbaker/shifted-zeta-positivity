# Explicit positive-time strip tail

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance. AGC-EZ-E07. Status **proved in-note** in the stated strip and comparison class. [Separate internal analytical assessment](../reviews/03_EZ_STRIP_TAIL_ASSESSMENT_20261120.md). Executor dispatched gpt-6.2-sol/ultra. Lead session gpt-6.2-astra/ultra.

## Bound

Use the physical time and height of Polymath v2. Let \(0<\tau\le t\le1/2\), \(1/5\le y\le1\), \(z=x+iy\), and put
\[
 Q=\frac{x}{4\pi},\qquad L=\log Q,\qquad
 L\ge\frac{32}{\tau}.
\]
Let \(\mathcal B_t(z)=M_t((1-iz)/2)\) be Polymath's nonvanishing normalizer from (6)–(11). Then
\[
 \left|\frac{H_t(z)}{\mathcal B_t(z)}-1\right|
 <\frac{15}{64}+\frac{7}{1000}<\frac14.
\]
In particular \(|H_t(z)|/|\mathcal B_t(z)|>3/4\) on this strip tail. This is an explicit, deliberately conservative specialization of the published effective approximation and its direct one-mode estimate. [Polymath v2, Theorem 1.3, equations (13)–(24)](https://arxiv.org/html/1904.12438v2#S1) · [Polymath v2, §9](https://arxiv.org/html/1904.12438v2#S9)

The normalizer \(\mathcal B_t\) here is the explicit Stirling factor. The half-line phase obstruction concerns the distinct integral lift from the opening gap manuscript. The estimate below supplies a sufficient bound on one strip subdomain of the published criterion. [Half-line phase obstruction](04_EZ_HALF_LINE_PHASE_OBSTRUCTION_20261120.md) · [Target classification](../../../../../avoid/01_restating_the_target.md)

## Cutoff, weights, and both leading terms

The hypotheses give \(L\ge64\), \(tL\ge32\), and \(x>2L^3\) using \(e^L\ge L^3/6\) and \(\pi>3\). In particular \(x\ge200\), so Theorem 1.3 applies. With its cutoff \(N=\lfloor\sqrt{Q+t/16}\rfloor\),
\[
 \sqrt Q-1<N\le\sqrt{Q+1/32},\qquad
 \log N\le L/2+\frac1{64Q}.
\]
For \(1\le n\le N\), the last bound also gives \(-1/(32Q)\le L-2\log n\le L\), hence \(|L-2\log n|\le L\). These bounds hold for the actual floor at every point, including each cutoff seam. The carrier \(\mathcal B_t\) is independent of that floor. Applying (13) with the specified \(N\) at the seam supplies the same pointwise bound, without any transfer of a reference across adjacent cells.

The exponent in \(b_n^t\) is \(t\log^2n/4\). From (21), using \(0\le y\le1\), one obtains
\[
 \begin{aligned}
 \Re s_*-\frac t4\log n
 &\ge\Re s_*-\frac t4\log N\\
 &\ge \frac{1+y}{2}+\frac{tL}{8}-\eta(x),\\
 \eta(x)&=\frac1{512Q}+\frac{1+8/x^2}{4x^2}<\frac14 .
 \end{aligned}
\]
Here the positive-part factor in (21) is at most \(1+8/x^2\), the loss from the floor estimate is \(t/(256Q)\), and \(t\le1/2\) bounds both losses. The resulting exponent exceeds \(4\). Hence \(b_n^t n^{-\Re s_*}\le n^{-4}\).

The first sum in (14) has leading term \(1\), and the second contributes its leading term \(\gamma\). Equation (20) and \(y\ge1/5\) give
\[
 |\gamma|\le e^{1/50-yL/2}\le e^{-319/50}<2^{-6}=\frac1{64}.
\]
For the higher terms of the second sum, use (20) and (22) together:
\[
 |\gamma|\, N^{y+|\kappa|}
 \le \exp\!\left(\frac1{50}+\frac1{64Q}+
                  \frac{\log N}{4(x-6)}\right)
 <e^{1/25}\le\frac{25}{24}<\frac{11}{10}.
\]
The strict exponent bound follows from \(Q>16\), \(\log N<L\), and \(x-6>L^3\). The bound on \(e^{1/25}\) follows by comparing its positive Taylor series with the geometric series. The product \(N^{y+|\kappa|}\) covers the factor \(n^y\) and the real part of the exponent involving \(\kappa\), regardless of its sign. Therefore all terms with \(n\ge2\) in the two sums together cost at most
\[
 \frac{21}{10}\sum_{n=2}^{N}n^{-4}
 \le\frac{21}{10}\left(2^{-4}+\int_2^\infty r^{-4}\,dr\right)
 =\frac7{32}.
\]

## Approximation errors

In (23) use \(\log(x/(4\pi n^2))=L-2\log n\) and \(t^2/16\le1/64\). Its nonnegative exponent is at most
\[
 h(x)=\frac{L^2/64+0.626}{x-6.66}
 <\frac1{64L}+\frac1{L^3}<\frac1{1000},
\]
where \(x-6.66>L^3\). The same weight and \(\gamma\) estimates apply to every term, now including \(n=1\). Thus
\[
 e_A+e_B\le\frac{21}{10}\left(1+\frac5{48}\right)(e^{h(x)}-1)
 <\frac3{500},
\]
using \(e^{h}-1\le h/(1-h)<1/500\).

In (24), the denominator \(N-0.125\) is greater than \(\sqrt Q-9/8\). Use \(3^y+3^{-y}\le10/3\) and \(|L+i\pi/2|\le L+\pi/2\). The positive correction in the exponent is then bounded above by
\[
 C(x)=\frac{62/15}{\sqrt Q-9/8}
     +\frac{3(L+\pi/2)+10.44}{x-12}<1.
\]
The first term is below \(1/2\) since \(\sqrt Q=e^{L/2}>2^{32}\). The second is below \(4/L^2<1/2\) since \(\pi<4\), \(L\ge64\), and \(x-12>L^3\). Equation (24) now yields
\[
 e_{C,0}\le Q^{-(1+y)/4}\exp(-tL^2/16+C(x))
 <e^{1-L/4}\le e^{-15}<\frac1{1000}.
\]
Adding the reflected leading term, both higher sums and all three approximation errors gives \(1/64+7/32+3/500+1/1000=15/64+7/1000\), as asserted.

## Scale and the inherited finite complement

Before rounding for the fixed cutoff, the reflected leading term costs \(O(Q^{-y/2})\). With \(\sigma_\tau=1/2+\tau L/8-\eta(x)\), the combined higher terms are bounded by
\[
 \frac{21}{10}\,2^{-\sigma_\tau}
     \left(1+\frac2{\sigma_\tau-1}\right).
\]
The two errors \(e_A+e_B\) cost \(O((1+L^2)/x)\). The last error retains the factor \(Q^{-(1+y)/4}e^{-tL^2/16}\) times \(\exp(O(Q^{-1/2}+L/x))\). These are the costs of the directly normalized one-mode triangle estimate with the literal coefficients. The published theorem already supplies the corresponding high-strip nonvanishing for sufficiently large height at fixed positive time. This calculation specifies a sufficient cutoff for a fixed margin. [Polymath v2, Theorem 1.5 and §9](https://arxiv.org/html/1904.12438v2#S9)

At the parent's \(t_0=\tau=1/10\), this cutoff is \(x_*=4\pi e^{320}\). The part of the final strip from \(14000+\sqrt{24/25}\) up to \(x_*\), with \(1/5\le y\le\sqrt{4/5}\), still needs a complete finite-height certificate or a smaller effective tail onset with a verified overlap. The initial height check and intermediate-time barrier are separate premises of the published canopy criterion. Its payoff would be \(t_0+y_0^2/2\) after all premises are supplied. Platt–Trudgian's published \(\Lambda\le0.2\) is the benchmark following Polymath's \(0.22\). The cutoff here diverges as \(\tau\downarrow0\). [Parent strip consumer](../../manuscript/sections/10_uniform_correction.tex) · [Polymath v2, Theorem 1.2](https://arxiv.org/html/1904.12438v2#S1) · [Platt–Trudgian, Corollary 2](https://arxiv.org/pdf/2004.09765#page=5)

The estimate uses the literal arithmetic terms and their complete source errors. The shifted Euler-factor, weighted-square and finite-prime controls change those terms. Reflected and positive-primitive controls lack the canonical square expansion needed for the approximation. Fixed-event and finite-profile sources lack the complete source budget. The RH-conditional endpoint control lacks ordinary Dirichlet arithmetic, and the altered-observation controls change the cosine field. Thus the numeric bounds from (13)–(24) remain specific to the theta field on the stated strip. [Result index](../../../../../result-summaries/README.md) · [Collision catalogue](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns index](../../../../../avoid/README.md) · [Control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) · [Known coverage](../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)


## Why this one-term comparison cannot meet the verified height at \(t=1/10\)

Added by the lead, gpt-6.2-astra/ultra, for Edward Baker, 20 November 2026. This is an analytical lower bound on the **allowance** of the specific triangle estimate used above. It isolates which information a continuation must add.

At \(t=1/10,\ y=1/5\) let \(14000\le x\le6.1\,10^{12}\). This interval includes the parent's wall and the physical height twice the ordinate in Platt–Trudgian's Theorem 1. In Polymath's (9), (17) take \(s=3/5-ix/2\). Since \(\Re(1/(s-1))<0\), \(|1/(2s)|\le1/x\), and \(|s|=(x/2)\sqrt{1+(6/(5x))^2}\), one has \(\Re\alpha(s)\le L/2+2/x\). Also \(L<28\) (indeed \(x/(4\pi)<10^{12}<e^{28}\), using \(e>27/10\) and \((27/10)^7>1000\)). It follows that
\[
 \Re s_* \le 3/5+(14+2/14000)/20 < 4/3.
\]
Since \(N\ge16\) and \(b_n^t\ge1\), even the omitted terms in the **first** Dirichlet sum alone have total absolute weight
\[
 \sum_{n=2}^N b_n^t n^{-\Re s_*}
 >\sum_{n=2}^{16}n^{-4/3}
 \ \ge\ \frac12\sum_{n=2}^8\frac1n+\frac13\sum_{n=9}^{16}\frac1n
 \ \ge\ \frac{481}{560}+\frac16
 =1+\frac{43}{1680}.
\]
Here \(n^{1/3}\le2\) through 8 and \(n^{1/3}<3\) through 16. Thus a lower bound taking the first unit term as its sole positive contribution and charging the other terms separately already lies below \(-43/1680\) before the reflected sum and analytic errors are paid. Better estimates of (23)–(24) alone cannot rescue this particular comparison there. The inequality says nothing adverse about the actual signed sum or the actual physical field on that line. A phase-correlated reference, signed error transport or a contour argument can use information that was discarded. [Polymath, Theorem 1.3 (9), (14)–(19)](https://arxiv.org/html/1904.12438v2#S1) · [Platt–Trudgian, Theorem 1](https://arxiv.org/pdf/2004.09765v1#page=2) · [Scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
