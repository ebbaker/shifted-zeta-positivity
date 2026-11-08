# B04 r4 / B05: the two acquired metric scales and the remaining signed estimate

6 November 2026 America/New_York (7 November UTC). Prepared for **Edward Baker** with substantial Codex assistance. Lead tool-selected **gpt-6-astra/ultra**; E15 proof and E16 assessment selected **gpt-6.1-sol/ultra**. These are dispatch records, not independently verified backend identities. The root coordinator independently checked the arithmetic reduction below; its configuration is not inferred. No novelty or specialist-independence claim is made.

**Disposition:** the broadened search produced two substantive, quantitatively controlled metrics, not merely candidate definitions. E16 accepts their frozen proofs in [Note24](../../notes/24_TND_O_E15_GAUSSIAN_LAGUERRE_HIERARCHY_20261107.md) and [Note25](../../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md) within scope. This final bounded comparison uses those actual scales. The Green metric has the cleaner next arithmetic interface because it is scalar-invariant and detects zeros directly. A further exclusion proof is not ready: its critical-line logarithmic upper comparison is unproved, while the Gaussian route still lacks a signed estimate at its collision-amplitude scale. The authorization to revisit either metric or another kernel persists; this is an analytical dependency, not a permission boundary.

## 1. Gaussian Laguerre: the actual margin and its costs

For a real multiplicity-m event at (lambda*,x*), put a_m=partial_x^m H(lambda*,x*) and n=m−2. The proved resolving window has reverse distance t>0 and Gaussian **variance** v=kappa t, with 0<kappa<2. Writing delta=1−kappa/2, Note24 gives

\[
 A_{m-2}(\lambda_*-t,x_*,\kappa t)
 =-\delta|a_m|^2t+\mathcal E_m(t),\qquad
 |\mathcal E_m(t)|\le E_\kappa(t;|a_m|,C,D),
 \tag{1}
\]

where the displayed polynomial error uses complete source constants C=M_(m+1)(L)/2 and D=M_(m+2)(L)/2, with every multiplicity dependence paid by (5),(26) of Note24. A sufficient independently acquired lower comparison would be

\[
 A_{m-2}(\lambda_*-t,x_*,\kappa t)\ge-c|a_m|^2t,
 \quad 0\le c<\delta,\quad
 E_\kappa(t)<(\delta-c)|a_m|^2t.
 \tag{2}
\]

The present source bound is instead an absolute allowance

\[
 |A_n|\le n!\epsilon^{-n}\mathcal C_\epsilon(L).
\]

Relative to the needed margin, it costs n!epsilon^(−n)C_epsilon/(|a_m|²t). It has no favorable sign and no event-amplitude lower bound; its uniformity in every real center is not a uniform smallness estimate as height grows. The proof does pay all order-series, arithmetic-index and radial tails, so for a fixed known event the acquisition errors can be driven below any prescribed tolerance. It does not make that event-dependent tolerance cheap or give its normalization uniformly over heights/multiplicities.

The cancellation characteristic has v'=2; the resolving schedule has v'=−kappa. Starting at v0=kappa t0, cancellation leaves v<2t after exactly (2−kappa)t0/4, and backward continuation keeps variance positive for at most kappa t0/2. Thus the acquired hierarchy does not carry the resolving window to a remote endpoint. Generic positivity of weighted kinetic energy also misses the required threshold. The exact cubic control shows that first-level Laguerre positivity can coexist with an imaginary pair; no entire-function criterion is inferred from checking a finite order or from the existence of all derivative formulas.

This candidate has gained a complete all-order acquisition theorem and an all-finite-multiplicity diagnostic. Its next useful proof would have to establish (2), or a quantitatively stronger source-sensitive substitute, with the amplitude, width and continuation costs retained. No such signed estimate is presently derived from the literal theta coefficients. The colliding smooth positive-source control shares the generic identities and moment finiteness, so those properties alone cannot supply it.

## 2. Green potential: an explicit arithmetic baseline at time zero

The acquired Green statistic uses a=pi/8 and K(x)=1/[16cosh(ax)], with mass 1/2 on each boundary. At every canonical time in [0,1/2],

\[
 J_\lambda(X)=\sum_{y_j>0}
 \operatorname{atanh}\frac{\sin(ay_j)}{\cosh(a(X-x_j))}.
 \tag{3}
\]

It is positive, scalar-invariant, and an upper zero with y>=d, |x−X|<=r forces

\[
 J_\lambda(X)\ge\frac{\sin(a)d}{\cosh(ar)}.
 \tag{4}
\]

Note25 proves full boundary and zero tails, but only a coarse upper bound of order log(3+|X|). The following exact canonical arithmetic reduction sharpens what remains to be acquired at lambda=0; it is derived here, with a root read-only algebra check, rather than being part of E16's earlier frozen audit.

Define the critical-line logarithmic average and a uniformly convergent prime baseline by

\[
 \mathcal L(X)=\int_{\mathbb R}K(x-X)
        \log|\zeta(\tfrac12-ix/2)|\,dx,
\]
\[
 P(X)=\sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\log n}
       \frac{n^{-5/2}}{1+n^{-4}}\cos\!\left(\frac X2\log n\right).
 \tag{5}
\]

Here Lambda_vM is the von Mangoldt function, distinct from the Newman threshold. Then

\[
 \boxed{J_0(X)=\mathcal L(X)-P(X)+G(X,1),\qquad
 G(X,1)=\operatorname{atanh}\frac{\sin(\pi/8)}{\cosh(\pi X/8)}.}
 \tag{6}
\]

**Derivation and pole payment.** By xi reflection, H0(z)=xi(s)/8 with s=1/2−iz/2. The horizontal lines Im z=0,4,8 become Re s=1/2,5/2,9/2. In

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

the factors s, pi^(−s/2), Gamma(s/2), and constants have harmonic logarithmic moduli on the strip. Their polynomial/logarithmic growth is paid by the exponential boundary kernels, so their boundary-minus-interior functional is zero. The factor s−1 has a zero at z=i and contributes **+G(X,1)**. This explicitly cancels the pole of zeta at s=1; one must not treat log zeta as harmonic across that pole. These statements use freshly checked DLMF 25.4.3–4,25.2.11,5.2 and 5.11.1, with exact inspection recorded in [receipt14](../../references/14_TND_O_GREEN_PRIME_BASELINE_SOURCE_USE_20261107.md). Weighted absolute integrability of the critical-line logarithm follows from Note25 and the paid elementary/gamma factors.

On either safe s line, the Euler product and the absolute logarithmic expansion give

\[
 \log|\zeta(\sigma-ix/2)|
 =\sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\log n}
                  n^{-\sigma}\cos((x/2)\log n),\quad\sigma>1.
\]

The elementary Fourier transform of K is
\(\widehat K(\omega)=\tfrac12\operatorname{sech}(4\omega)\).
It follows, for example, by substituting u=e^(2ax) in the sech integral and evaluating the Euler beta integral at 1/2+i omega/(2a). At omega=(log n)/2, this is 1/(n²+n^(−2)). Therefore the safe-boundary minus interior coefficient is

\[
 \frac{n^{-9/2}}{n^2+n^{-2}}-n^{-5/2}
 =-\frac{n^{-5/2}}{1+n^{-4}},
\]

which proves (6) with all constants and signs. Absolute convergence justifies every prime-series interchange. There is an explicit complete-index tail, uniformly in **all** real X:

\[
 |P(X)-P_N(X)|\le\sum_{n>N}n^{-5/2}
 \le\frac23N^{-3/2},\qquad N\in\mathbb N,\ N\ge2.
 \tag{7}
\]

This uses 0<=Lambda_vM(n)/log n<=1. No derivative-order claim or numerical evaluation is attached to (7). The reduction applies specifically at lambda=0; the deformed family is not silently assigned the same Euler product.

The positivity already proved supplies the unconditional **lower** comparison

\[
 \mathcal L(X)\ge P(X)-G(X,1).
 \tag{8}
\]

The needed exclusion direction is an upper comparison with a strict absolute margin. For the declared defect class (4), it would suffice to prove

\[
 \mathcal L(X)<P(X)-G(X,1)+\frac{\sin(a)d}{\cosh(ar)}.
 \tag{9}
\]

No estimate (9) at an exclusion margin is obtained here. The right-side baseline has fully paid prime access; the remaining critical-line logarithmic mean is the difficult term. An absolute theta approximation is not a relative logarithmic estimate near its real zeros. Note25's exponential boundary tail carries its explicit height factor; (7) pays the separate prime index. Both errors must be smaller than the declared d,r margin in any use of (9). Merely replacing the critical-line term by an unproved prime approximation would assume precisely the missing information.

## 3. Choice, failure class and actual research boundary

The Green potential is the more attractive next arithmetic interface: it directly measures nonreal zeros without event-amplitude normalization, and at time zero its safe-line portion reduces to an explicit absolutely convergent prime series. Its collision behavior is only square-root continuous near a real double event, so it does not inherit the transverse y² moment's Lipschitz bound. The Gaussian defect instead resolves every finite real multiplicity and has a complete order/source hierarchy, but its useful signal is small in |a_m|²t and its natural resolving variance conflicts with spatial cancellation.

This comparison ends with two exact missing signed inequalities, (2) and (9), not a theorem that all localized methods fail. The obtained absolute source, density, count and safe-line estimates do not establish either one. No further proof contract with a paid route to those margins is presently ready. Further algebraic reformulation of the same unknown sign, increasing derivative order inside an absolute allowance, or a finite numerical test would not close this dependency. The original Gaussian Gram route and other justified future kernels remain available under the author's broad authorization.

The actual gains retained from the broadened search are: complete Gaussian all-order/index/radial acquisition; a quantitatively paid finite-multiplicity resolving signal and variance conflict; a complete positive Green-strip identity with both exponential tails and exact defect margin; and the canonical prime-baseline reduction (6)–(8) with uniform index error. The first two note packages have E16's internal shared-premise acceptance. The arithmetic reduction initially received lead derivation and a root read-only consistency check. Its exact subsequent E17 disposition is recorded in [Review10](../../reviews/10_TND_O_E17_PRIME_BASELINE_ASSESSMENT_20261107.md) and the sole register, separately from E16’s frozen scope. All are analytical; no numerical campaign, novelty assertion, RH conclusion or original-checkout edit follows.

[Result index](../../../../../../result-summaries/README.md), [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md), [pattern index](../../../../../../avoid/README.md), [target classification](../../../../../../avoid/01_restating_the_target.md) and [scoped-failure rule](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) apply. All-center exact vanishing/sign reformulations are not independent evidence. A later B revision may replace either candidate when it brings new canonical signed information; stopping this bounded attempt is not a request for renewed permission.
