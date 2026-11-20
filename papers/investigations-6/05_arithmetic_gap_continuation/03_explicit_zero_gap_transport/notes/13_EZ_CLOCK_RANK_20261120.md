# The absolute rank of the positive-time clock zeros

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance. AGC-EZ-E11 analysis, recorded gpt-6.2-sol/ultra, with the real-axis comparison selected by the gpt-6.2-astra/ultra lead. Written derivation accepted within scope in the [E12 assessment](../reviews/06_EZ_HIGH_RANK_ASSESSMENT_20261120.md).

At physical time \(t=1/2\), the unique zero near Polymath's sufficiently high clock location with label \(j\) is exactly the \(j\)-th positive zero of \(H_t\), counted with multiplicity. The proof identifies the integer offset from an imaginary-axis growth coefficient. It establishes eventual matching and leaves the height onset unevaluated.

## The published local counts

Write \(g(x)=g(x,t)\) for Polymath's clock and \(a_j\) for its roots \(g(a_j)=j\):

\[
 g(x)=\frac{x}{4\pi}\left(\log\frac{x}{4\pi}-1\right)+\frac{11}{8}
                    +\frac{t}{16}\log\frac{x}{4\pi}.
\]

De Bruijn's all-real theorem at \(t=1/2\) appears in Polymath's introduction. The displayed theta source there has positive summands for \(u\ge0\), since \(2\pi n^2e^{4u}-3>0\), so \(H_t(0)>0\). Let \(N(x)\) count positive zeros \(x_k\le x\), with multiplicity. Polymath's Theorem 1.5(i)–(ii) and the end of the proof after (104) give a unique simple zero near each sufficiently high \(a_j\), no other sufficiently high zeros, and location error \(O(a_j^{-ct}/\log a_j)\). The trivial clock spacing from \(g'(x)\sim\log x/(4\pi)\) makes these windows disjoint and ordered. Thus after a fixed sufficiently large cutoff \(b\) in a clock gap, an integer \(d\) and a function \(e\) satisfy

\[
 N(x)=\lfloor g(x)\rfloor+d+e(x),\qquad |e(x)|\le1,
 \quad x\ge b. \tag{1}
\]

The support of \(e\) lies in the union of the intervals between each \(a_j\) and its actual zero, with endpoint values immaterial in integrals. The number of clocks in \([R,2R]\) is \(O(R\log R)\), and each contributes \(O(R^{-1-ct}/\log R)\) to \(\int |e(x)|\,dx/x\). The dyadic contributions \(O(R^{-ct})\) sum. Theorem 1.5(iii) states \(N(x)=g(x)+O(1)\). Its proof leaves a bounded argument variation on a finite portion of the upper edge. The discussion after the theorem marks the sharper floor formula as a suggestion. A sign check at \(g(X)=j+1/2\) gives \(d\equiv0\pmod{2}\), since the two terms of Proposition 9.1(i) at the real endpoint have sum of sign \((-1)^j\) by Lemma 9.2, and \(\operatorname{sgn}H_t(X)=(-1)^{N(X)}\). This check leaves the full integer to be determined. [Polymath v2, §1, (26) and Theorem 1.5](https://arxiv.org/html/1904.12438v2#S1) · [§9, Proposition 9.1, Lemma 9.2 and (104)](https://arxiv.org/html/1904.12438v2#S9)

## The count as a logarithmic growth coefficient

The even order-one Hadamard product, equivalently the pairing in Polymath's (105), is \(H_t(z)/H_t(0)=\prod_{k\ge1}(1-z^2/x_k^2)\). Pairing cancels the genus-one exponential factors, and evenness forces the remaining linear exponential to be constant. The products converge since \(N(x)=O(x\log x)\) at infinity. For \(Y>0\), sum the identity \(\log(1+Y^2/x_k^2)=\int_{x_k}^\infty K_Y(x)\,dx\), where \(K_Y(x)=2Y^2/[x(x^2+Y^2)]\). Positivity permits the interchange and gives

\[
 \log\frac{H_t(iY)}{H_t(0)}=\int_0^\infty K_Y(x)N(x)\,dx. \tag{2}
\]

The range below \(b\) contributes \(O(1)\) as \(Y\to\infty\), since \(K_Y\le2/x\) and \(N(x)=0\) near zero. The error \(e\) in (1) contributes \(O(1)\) by its integrability against \(dx/x\). Set \(p(s)=\lfloor s\rfloor-s+1/2\), a mean-zero function with bounded primitive. With the substitution \(s=g(x)\), the weight for \(p\) is \(K_Y(x)/g'(x)\). Choose \(b\) large enough that \(g'(x)>0\) and \(g''(x)>0\) for \(x\ge b\). This weight is decreasing to zero and is bounded at \(b\) uniformly in \(Y\). Integration by parts against the bounded primitive shows that the sawtooth contributes \(O(1)\). Hence one may integrate \(g(x)+d-1/2\) over \([b,\infty)\) in (2), with an \(O(1)\) error.

The term linear in \(x\) can be extended to \(0\) for an \(O(1)\) cost, by integrability of \(|\log x|\) there. With \(x=Yu\), the resulting integral is \(\tfrac{Y}{4}(\log(Y/(4\pi))-1)\), using \(\int_0^\infty (1+u^2)^{-1}du=\pi/2\) and \(\int_0^\infty \log u\,(1+u^2)^{-1}du=0\) by inversion. The constant \(7/8+d\) is multiplied by \(\log(1+Y^2/b^2)=2\log Y+O(1)\).

For the clock's term proportional to \(t\), compare the integral of \(K_Y(x)\log(x/(4\pi))\) to the one with weight \(2\mathbf 1_{x\le Y}/x\) on \([b,\infty)\). The latter equals \(\log^2(Y/(4\pi))+O(1)\). In scaled variable \(u=x/Y\), the difference uses the signed weight

\[
 W(u)=\frac{2}{u}\left(\frac1{1+u^2}-\mathbf1_{u\le 1}\right).
\]

Its integral over \((0,\infty)\) is zero by \(u\mapsto1/u\), its absolute log moment is finite, and \(\int_0^{b/Y}|W(u)|du=O(Y^{-2})\). Thus the difference, weighted by \(\log(Y/(4\pi))+\log u\) on \([b/Y,\infty)\), is \(O(1)\). Putting the terms together yields

\[
 \log H_t(iY)=\frac{Y}{4}\left(\log\frac{Y}{4\pi}-1\right)
      +\frac{t}{16}\log^2\frac{Y}{4\pi}+\left(\frac74+2d\right)\log Y+O(1). \tag{3}
\]

The order-one input and product convention are as in Polymath. [§1, (3)–(4)](https://arxiv.org/html/1904.12438v2#S1) · [§9, (105)](https://arxiv.org/html/1904.12438v2#S9)

## Independent evaluation from the complete source

Let \(F_0(Y)=H_0(iY)\), an even positive function. For \(Y>0\), evenness and (1)–(2) of Polymath give \(F_0(Y)=\xi((1+Y)/2)/8\). Put

\[
 P(Y)=\frac{Y}{4}\left(\log\frac{Y}{4\pi}-1\right)+\frac74\log Y.
\]

Stirling's estimate gives \(\log F_0(Y)=P(Y)+O(1)\). In detail, with \(s=(1+Y)/2\), the completed formula gives \((s/2)\log(s/(2\pi))-s/2+(3/2)\log s+O(1)\) for the logarithm. The shift by \(1\) in \(s=(1+Y)/2\) adds \(\tfrac14\log Y\) to the coefficient \(3/2\). The zeta factor has \(\log\zeta(s)=o(1)\) from its Dirichlet series on the positive real axis. [Polymath v2, (1)–(2)](https://arxiv.org/html/1904.12438v2#S1) · [Lemma 5.1(v)](https://arxiv.org/html/1904.12438v2#S5)

For \(V\) normal of mean zero and variance \(2t\), the positive Gaussian formula is \(H_t(iY)=\mathbb E F_0(Y+V)\). Indeed the normal average of \(\cosh((Y+V)u)\) is \(e^{tu^2}\cosh(Yu)\), and positivity justifies the interchange. Write \(A_Y=P'(Y)=\tfrac14\log(Y/(4\pi))+7/(4Y)\). On \(|v|\le Y^{1/4}\), Taylor's estimate gives \(P(Y+v)=P(Y)+A_Yv+O(Y^{-1/2})\). Thus \(F_0(Y+v)\) lies between fixed positive constant multiples of \(e^{P(Y)+A_Yv}\). Completing the square writes \(e^{A_Yv}\) times the normal density as \(e^{tA_Y^2}\) times a normal density with mean \(2tA_Y=O(\log Y)\) and variance \(2t\). The shifted normal probability of the central range tends to one.

On \(Y^{1/4}<|v|\le Y/2\), the same Stirling bound and the estimate for \(P'\) give \(F_0(Y+v)\ll e^{P(Y)+C|v|\log Y}\). The Gaussian tail integral of this upper bound divided by \(e^{P(Y)}\) is \(O(e^{-c_tY^{1/2}})\). On \(|v|>Y/2\), Stirling, evenness and continuity on bounded intervals give a global bound \(F_0(Y+v)\le \exp(C(1+|Y+v|)\log(2+|Y+v|))\). Since \(|Y+v|\le3|v|\) here, the quadratic Gaussian exponent controls this last tail by \(O(e^{-c_tY^2})\). Therefore

\[
 \log H_t(iY)=P(Y)+tA_Y^2+O(1)
   =P(Y)+\frac{t}{16}\log^2\frac{Y}{4\pi}+O(1). \tag{4}
\]

This uses the positive imaginary-axis average in Polymath's heat-kernel representation. [§4, (35)](https://arxiv.org/html/1904.12438v2#S4)

Comparing (3) and (4) gives \(2d\log Y=O(1)\), so \(d=0\). At the midpoint \(g(X_j)=j+1/2\), there are exactly \(j\) positive roots through \(X_j\) for all sufficiently large \(j\). The unique root in the window at \(a_j\) therefore has rank \(j\). This matches absolute labels in the product and Polymath's clock. At those ranks the inherited position error is \(O(a_j^{-ct}/\log a_j)\), and subtracting neighboring bounds gives the same order for the gap error. This proof fixes the additive integer and supplies no tighter location error or evaluated cutoff.

## A finite-prefix count and the time-zero benchmark

A finite alternative is one verified prefix count at a cutoff \(X\) known to lie in the eventual gap between clock labels \(j\) and \(j+1\). The amount to pay is an exact integer \(N(X)\) and a proved local-count overlap at \(X\). For example, at the all-real time choose the counterclockwise rectangle \([0,X]+i[-1,1]\) and certify \(H_t\ne0\) on its boundary and an enclosure of \((2\pi i)^{-1}\oint H_t'/H_t\) containing just one integer. The left boundary has positive values and all roots are real. At a verified gap there is no boundary root, so winding gives \(N(X)\) counting multiplicity without enumerating the prefix. Subtracting \(j\) fixes \(d\). The effective normalized-field bounds in Theorem 1.3 apply on the upper side with \(x\ge200\). The remaining contour portions and the winding accuracy require their own controlled enclosures. No finite count was run here. [Polymath v2, Theorem 1.3 and §9 proof of Theorem 1.5(iii)](https://arxiv.org/html/1904.12438v2#S1)

Platt–Trudgian Theorem 1 certifies that the first \(12{,}363{,}153{,}437{,}138\) zeros of positive zeta ordinate through \(\gamma=3{,}000{,}175{,}332{,}800\) lie on the critical line, corresponding to the cutoff \(x=2\gamma=6{,}000{,}350{,}665{,}600\) at \(t=0\). Section 2 combines critical-line sign changes with a Turing count to establish completeness, with finer isolation only as needed. A transfer to an exact \(t=1/2\) count at a chosen fixed cutoff would additionally need a crossing account or a positive-time count. Corollary 2 uses their finite verification and Polymath's Table 1 to obtain \(\Lambda\le0.2\), improving Polymath's \(\Lambda\le0.22\). The absolute rank calculation here starts at an already established all-real time. [Platt–Trudgian v1, Theorem 1 and §2](https://arxiv.org/pdf/2004.09765v1#page=2) · [Corollary 2](https://arxiv.org/pdf/2004.09765v1#page=5) · [Polymath v2, Table 1](https://arxiv.org/html/1904.12438v2#S10)

## Scope and controls

This is a fixed-time count calibration with an arithmetic normalization. It pays for the real divisor, the complete high-tail location theorem, and the exact completed-zeta identity in (4). Euler-factor controls alter that identity. In the cosine-multiplier family the imaginary-axis logarithm at time zero acquires the term \(aY+O(1)\). Weighted-square and finite-source controls lack the all-real divisor and the high tail. Reflected and positive-primitive constructions, finite-prime perturbations, and fixed-event or finite-profile controls lack the unchanged completed-zeta identity, even when they retain selected endpoint or profile data. The conditional normalized-endpoint controls retain a displayed completion but fail the ordinary Dirichlet-series arithmetic. A changed observation kernel also fails the exact cosine/heat identity used by (2) and (4). These premise checks concern this rank calculation at the stated time. [Results index](../../../../../result-summaries/README.md) · [Collision and source controls](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns index](../../../../../avoid/README.md) · [Target classification](../../../../../avoid/01_restating_the_target.md) · [Control screening](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) · [Scope of exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
