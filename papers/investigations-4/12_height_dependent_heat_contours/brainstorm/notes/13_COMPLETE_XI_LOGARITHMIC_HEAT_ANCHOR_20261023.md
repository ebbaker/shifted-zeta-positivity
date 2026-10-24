# Complete-xi negative-heat Euler anchor on logarithmic time widths

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. This is a proved analytic estimate at the stated scope, with separate same-model [internal review][review]; it has not received specialist review. It improves one existing anchor implementation, without bounding the earlier nonreal population or the full simplicity resource.

**Attribution and scope.** The Gaussian-modified Dirichlet series and gamma shift used below already occur in [Alexander Dobner's work][dobner], Equation (3), Theorem 4 and Section 4. This note gives a directly normalized estimate uniform near zero heat time in the Euler region and compares its anchor width with the existing [book][book]. It claims no novelty for the representation and no new global simplicity theorem. The [research overview][overview] and [progress register][progress] place this supporting estimate under SIMP-01; it does not complete that goal.

Follow the [result index][results], [collision controls][controls] and [avoid index][avoid], particularly [target reformulations][a01], [shared premises][a02], [scoped exclusions][a07] and [coupled estimates][a12].

## 1. Statement

Use the canonical normalization

\[
 H_t=-H_{zz},\qquad 8H(0,z)=\xi(1/2+iz/2).
\]

Set

\[
 K(s)=\frac{s(s-1)}2\pi^{-s/2}\Gamma(s/2),\qquad
 L(s)=\operatorname{Log}\frac{s}{2\pi},
\]

where \(\operatorname{Log}\) is principal. Fix

\[
 1<\sigma_0\le\sigma_1<\infty,\qquad
 0<A<4(\sigma_0-1),\qquad
 \delta=\sigma_0-1-\frac A4>0.
\]

For \(\sigma\in[\sigma_0,\sigma_1]\), \(s=\sigma+i\tau\), \(|\tau|\) large, and \(0\le\epsilon\le A/\log|\tau|\), put

\[
 s_\epsilon=s-\frac{\epsilon L(s)}4,\qquad
 Z_\epsilon(w)=\sum_{n\ge1}n^{-w}
                 \exp\!\left[-\frac\epsilon4(\log n)^2\right].
\]

At \(z=-2\tau+i(2\sigma-1)\), the following estimates hold uniformly throughout that range:

\[
 \boxed{
 8H(-\epsilon,z)
 =K(s)e^{-\epsilon L(s)^2/16}
 \left[Z_\epsilon(s_\epsilon)
       +O_{\sigma_0,\sigma_1,A}(|\tau|^{-1})\right].}
 \tag{1}
\]

\[
 Z_\epsilon(s_\epsilon)=\zeta(s_\epsilon)+E_\epsilon,
 \qquad
 |E_\epsilon|\le\frac\epsilon4\zeta''(1+\delta).
 \tag{2}
\]

The constants and sufficiently-large-height threshold exist and depend only on the displayed fixed parameters; they have not been evaluated numerically. Formula (1) has its literal continuous \(\epsilon=0\) interpretation, where the equality without its error term is exact.

For all sufficiently large \(|\tau|\), \(\Re s_\epsilon\ge1+\delta\). Set

\[
 b_\delta=\frac{\zeta(2+2\delta)}{\zeta(1+\delta)}>0.
\]

Then

\[
 \boxed{
 |H(-\epsilon,z)|\ge
 \frac{|K(s)|}{8}
 e^{-\epsilon\Re(L(s)^2)/16}
 \left[b_\delta-\frac\epsilon4\zeta''(1+\delta)
                   -\frac C{|\tau|}\right].}
 \tag{3}
\]

In particular, the bracket is at least \(b_\delta/2\) for all sufficiently large \(|\tau|\), uniformly for \(0\le\epsilon\le A/\log|\tau|\). No RH assumption is needed.

At \(\epsilon=\kappa/(\log|\tau|)^2\), with \(\kappa\) in a fixed compact subset of \([0,\infty)\),

\[
 \boxed{
 \frac{H(-\epsilon,z)}{H(0,z)}
 =e^{-\kappa/16}\left[1+O\!\left(\frac1{\log|\tau|}\right)\right].}
 \tag{4}
\]

The error in (4) is uniform also for \(\sigma\) in the indicated compact interval. This conclusion refers only to the Euler-region line \(|\Im z|=2\sigma-1>1\), and its real-type/even symmetries, not to neighborhoods of actual critical-line zeros.

## 2. Complete Gaussian representation and contour shift

The real heat convolution is exact:

\[
 H(-\epsilon,z)=\frac1{\sqrt{4\pi\epsilon}}
 \int_{\mathbb R}e^{-v^2/(4\epsilon)}H(0,z+v)\,dv.
\]

It follows directly by inserting the full theta integral and using the Gaussian Fourier transform. Absolute convergence follows from the super-exponential theta source and the fixed value of \(\Im z\). By the functional equation \(\xi(s)=\xi(1-s)\), and the change \(v=-2u\), it becomes

\[
 8H(-\epsilon,z)=\frac1{\sqrt{\pi\epsilon}}
 \int_{\mathbb R}e^{-u^2/\epsilon}\xi(s+iu)\,du.
 \tag{5}
\]

Put \(\lambda=\epsilon L(s)/4\), so \(s_\epsilon=s-\lambda\). Shift the \(u\) contour from \(\mathbb R\) to \(\mathbb R+i\lambda\). The latter is a horizontal line translated also in its real coordinate, which is harmless. Its imaginary displacement is \(\Re\lambda\). Throughout the strip between these lines,

\[
 \Re(s+iu)\ge\sigma-\Re\lambda
              =\Re s_\epsilon\ge1+\delta.
\]

Indeed, \(\Re L(s)=\log(|s|/(2\pi))\le\log|\tau|\) for all sufficiently large \(|\tau|\), uniformly for \(\sigma\) in the compact interval. This also bounds \(|\lambda|\) by a fixed constant depending on \(A\). The Euler series is therefore absolutely convergent throughout this contour deformation; no pole is crossed. The Gaussian suppresses the vertical end segments, because \(\xi\) grows at most polynomially times \(e^{C|u|}\) in the fixed real strip. This justifies the shift for every \(\epsilon>0\) in the range.

After writing \(u=w+i\lambda\), the exact identity is

\[
 \frac{8H(-\epsilon,z)}{K(s)e^{-\epsilon L(s)^2/16}}
 =\frac1{\sqrt{\pi\epsilon}}
 \int_{\mathbb R}e^{-w^2/\epsilon}
       \zeta(s_\epsilon+iw)R(s,-\lambda+iw)\,dw,
 \tag{6}
\]

where

\[
 R(s,q)=\frac{K(s+q)}{K(s)}e^{-qL(s)/2}.
\]

All exponential cancellation was performed before estimating the integral. In particular, no absolute value was applied to an oscillatory Gaussian before extracting its carrier.

## 3. Gamma-carrier estimate, including the full tails

The standard sectorial Stirling expansion gives, for \(s\) with bounded positive real part and \(|\Im s|\) large,

\[
 \frac{K'(s)}{K(s)}=\frac{L(s)}2+O(|\tau|^{-1}),
 \qquad
 \left(\frac{K'}K\right)'(s)=O(|\tau|^{-1}).
\]

The estimates are uniform also along each segment from \(s\) to \(s+q\) when \(|q|\le|\tau|/2\) and the real parts stay in a fixed compact subinterval of \((1,\infty)\). In the present application, \(\Re q=-\Re\lambda\) is bounded, \(\Im q=w-\Im\lambda\), and this compactness follows from \(\Re s_\epsilon\ge1+\delta\). Therefore, after reducing the local cutoff to \(|w|\le|\tau|/4\) and taking \(|\tau|\) large,

\[
 |\log R(s,-\lambda+iw)|
 \le\frac C{|\tau|}
 \left[|\lambda|+|w|+(|\lambda|+|w|)^2\right].
 \tag{7}
\]

One may choose \(\log K\) analytically in this right half-plane, so the logarithmic Taylor identity used in (7) has no branch discontinuity. It follows from \(|e^v-1|\le|v|e^{|v|}\) that the normalized Gaussian integral of \(|R-1|\) over \(|w|\le|\tau|/4\) is \(O(|\tau|^{-1})\). To see the uniformity, \(|\lambda|\) is bounded and \(\epsilon\le A/\log|\tau|\le1\) eventually, so the factor

\[
 \exp\!\left(\frac{Cw^2}{|\tau|}+\frac{C|w|}{|\tau|}\right)
\]

is absorbed in \(e^{-w^2/(2\epsilon)}\); the Gaussian expectations of \(1\), \(|w|\) and \(w^2\) are bounded uniformly. Since \(|\zeta(s_\epsilon+iw)|\le\zeta(1+\delta)\), the local error in (6) is \(O(|\tau|^{-1})\).

The complementary integral is not discarded. Stirling on a vertical strip, completed by compactness near bounded imaginary part, gives fixed \(B,C>0\) such that, for every real \(w\),

\[
 |R(s,-\lambda+iw)|
 \le C|\tau|^B(1+|w|)^B e^{C|w|}.
 \tag{8}
\]

For example, the gamma ratio contributes

\[
 \exp\!\left[\frac\pi4
       (|\tau|-|\tau+w-\Im\lambda|)\right]
 \le e^{C+(\pi/4)|w|};
\]

the additional factor \(e^{-qL/2}\) contributes a power of \(|\tau|\) times \(e^{(\pi/4)|w|}\), and the polynomial prefactor is bounded by a fixed power of \(|\tau|(1+|w|)\). This proves (8) also near \(w=-\tau\), where the numerator gamma factor has bounded imaginary part.

For \(|w|>|\tau|/4\), \(\epsilon\le1\), and sufficiently large \(|\tau|\), the polynomial factors and \(e^{C|w|}\) are absorbed by \(e^{w^2/(2\epsilon)}\), leaving a normalized Gaussian tail bounded by

\[
 C|\tau|^B e^{-c\tau^2/\epsilon},
\]

with fixed positive \(c\). In particular, this is \(O(|\tau|^{-1})\), uniformly over the entire positive \(\epsilon\) range. The same estimate covers the complementary tail with \(R\) replaced by \(1\). Equations (6)–(8) thus give

\[
 \frac{8H(-\epsilon,z)}{K(s)e^{-\epsilon L(s)^2/16}}
 =\frac1{\sqrt{\pi\epsilon}}
   \int_{\mathbb R}e^{-w^2/\epsilon}\zeta(s_\epsilon+iw)\,dw
   +O(|\tau|^{-1}).
\]

Termwise Gaussian integration of the absolutely convergent complete Dirichlet series proves (1). It produces \(e^{-\epsilon(\log n)^2/4}\) for every \(n\), with no finite cutoff or omitted coefficient.

## 4. Euler margin and microscopic specialization

For \(\Re w\ge1+\delta\), the inequality

\[
 0\le1-e^{-\epsilon(\log n)^2/4}
     \le\frac\epsilon4(\log n)^2
\]

gives (2). The Euler product gives

\[
 |\zeta(w)|\ge\prod_p(1+p^{-\Re w})^{-1}
 =\frac{\zeta(2\Re w)}{\zeta(\Re w)}\ge b_\delta.
\]

This proves (3), including the stated eventual half-margin. Since \(\epsilon\le A/\log|\tau|\), the error tends to zero uniformly.

For (4), \(\epsilon=\kappa/(\log|\tau|)^2\) and

\[
 L(s)=\log|\tau|-\log(2\pi)
       +i\operatorname{sgn}(\tau)\frac\pi2+O(|\tau|^{-1}).
\]

Thus \(\epsilon L(s)^2=\kappa+O(1/\log|\tau|)\) and \(s_\epsilon-s=O(1/\log|\tau|)\). Absolute convergence bounds \(\zeta'\) on a slightly enlarged Euler half-plane, while the Euler lower bound controls division by \(\zeta(s)\). Combining (1)–(2) gives (4).

## 5. Matched comparison and precise usefulness

The [book's current Euler anchor][book] uses the sufficient condition

\[
 \epsilon A_2(2\sigma-1)<m_0,
\]

where \(A_2\) is an absolute theta-source moment independent of \(\tau\) and \(m_0\) is the complete Euler lower bound for \(|H(0,z)|\). Stirling makes

\[
 m_0\asymp_\sigma
 |\tau|^{\sigma/2+3/2}e^{-\pi|\tau|/4}.
\]

Consequently, that particular sufficient condition forces an exponentially decreasing heat width. The coupled Gaussian-carrier calculation establishes a positive Euler anchor on the much larger width \(A/\log|\tau|\), with \(A<4(\sigma_0-1)\). At the top width its carrier has magnitude comparable to \(|\tau|^{-A/16}\), relative to \(K(s)\). At the mean-spacing-squared clock \(\kappa/(\log|\tau|)^2\), the relative field ratio has the nonzero limit \(e^{-\kappa/16}\).

This improves an explicitly identified high-height anchor bottleneck and preserves all theta/xi coefficients. It neither makes the earlier nonreal population small nor supplies the complete relative inward-flux budget. A high-height local Jensen use would additionally need modulus upper bounds on its chosen enclosing disks; the present statement does not silently supply the root-path constants or useful nonreal discrimination. In particular, **the theorem does not supply uniform bounds on a complex-time collar, required by the book's anchored root-path theorem**. It is not by itself SIMP-01 completion or a new simplicity proportion.

The mechanism is already present in [Alexander Dobner, *A proof of Newman's conjecture for the extended Selberg class*, arXiv:2005.05142v2, 10 January 2026][dobner]. Equation (3), Theorem 4 and Section 4 use the same Gaussian-modified Dirichlet series and nonlinear gamma shift

\[
 J_t(s)=s+\frac{|t|}{4}\operatorname{Log}\frac{s}{2\pi}.
\]

Theorem 4's displayed general error has a coarse exponential loss in \(1/|t|\); its proof retains a sharper dependence on the absolute Gaussian Dirichlet series before that final simplification, in Equation (34) and the subsequent summation. In an Euler half-plane that absolute series stays bounded, so the existing mechanism is well suited to near-zero specialization. The present proof supplies the directly normalized \(O(|\tau|^{-1})\) Euler-region estimate and explicit book-anchor comparison without claiming novelty for the representation or a new global theorem. A broader priority comparison would be needed before publishing any novelty claim.

## 6. Controls and scope

The conclusion is an exterior Euler-region nonvanishing estimate, not simplicity. Weighted-square/reflected [controls][controls] that lack this exact complete xi Euler factor do not satisfy the canonical input, but naming this failure is not a simplicity exclusion. A finite Euler-factor modification may share a corresponding exterior anchor and still collide inside; this is consistent with the theorem. Quadratic/cubic collision models do not contradict an exterior anchor. This result therefore cannot be used to exclude a control's interior collision, and its arithmetic distinction must not be overstated.

The scoped failure repaired is the absolute-source continuation bound for a fixed Euler anchor. No assertion is made that all prior anchors or all negative-time methods had exponentially small widths. This classification follows the repository standards on [shared premises][a02] and [scoped exclusions][a07].

## 7. Sources and internal review

The primary classical inputs checked were:

- [NIST DLMF 25.4.3–25.4.4](https://dlmf.nist.gov/25.4): xi functional equation and factorization.
- [NIST DLMF 5.11.1–5.11.2 and sectorial remainder discussion](https://dlmf.nist.gov/5.11): gamma/digamma asymptotics.
- [Dobner's Theorem 4 and Section 4][dobner]: the established Gaussian-modified Dirichlet mechanism, with the precise comparison explained above.

A separate same-model contributing agent, **gpt-6-astra, ultra**, checked the contour sign, all factors of two/four, uniform local gamma remainder, normalized full Gaussian tails, Euler lower margin and microscopic ratio. Its review found no mathematical issue within the stated real-negative-time scope. The [opening-round review][review] records the assessment. This is internal LLM review, not independent specialist validation.

[review]: ../reviews/04_ANALYTIC_SIMPLICITY_OPENING_ROUND_REVIEW_20261023.md
[overview]: ../research-overview/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRAM_20261023.md
[progress]: ../research-progress/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRESS_20261023.md
[book]: ../../manuscript/book.tex
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[dobner]: https://arxiv.org/pdf/2005.05142
