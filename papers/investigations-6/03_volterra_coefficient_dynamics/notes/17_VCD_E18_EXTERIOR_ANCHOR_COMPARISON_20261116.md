# VCD-E18 — exterior anchor comparison for the canonical score

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded dispatch **gpt-6.1-sol / ultra**.
Separate backend model and effort attestation unavailable.

**Proved in-note.** [E18 r1][request] executes the fixed analytic comparison
in [B05 decision10][decision]. The outcome is a quantitative exterior
anchor scale and an exact normalization of the full score remainder. The
pointwise reverse-triangle test below is a sufficient dominance estimate
whose arithmetic input is open here. This is an anchor estimate and exact
identity in the sense of [Avoid 01][a01]. Background and scope follow the
[result index][results], [control catalog 12][controls], [avoid index][avoid],
[Avoid 02][a02] and [Avoid 07][a07].

## 1. Integration by parts with the complete source

Work at \(\lambda=0\) with the unchanged [manuscript source and
readout][manuscript]. Use the complete even source \(\Phi\),
\(Z=\int_{\mathbb R}\Phi(u)\,du>0\), \(d\mu(u)=\Phi(u)\,du/Z\), and
\[
 F(z)=\int_{\mathbb R}e^{izu}\,d\mu(u)
     =\frac{\xi((1-iz)/2)}{4Z}.
\]
The factor \(4\) follows from the whole-line integral being twice the
half-line cosine integral \(\xi((1-iz)/2)/8\). The corresponding
half-line normalization and square-summand formula were also checked
in Rodgers–Tao §1, equations (1)–(3), with the sign of \(iz\)
interchanged by the functional equation. [Rodgers–Tao, arXiv v5][rt]

Set \(V_0=-\log\Phi\) and retain the exact [E06][e06] bounded score
remainder \(b=V_0'-8\pi\sinh(4u)\). Define
\[
 B(z)=\int_{\mathbb R} b(u)e^{izu}\,d\mu(u)
     =\langle e_0,b(J)e^{izJ}e_0\rangle .
\]
Here \(e^{izJ}e_0\) is in its fixed-vector domain by the exponential
moments of \(\mu\), and \(b(J)\) is bounded. The double-exponential
tail of \(\Phi\) makes \(\Phi(u)e^{izu}\) vanish at both real endpoints.
The score decomposition makes \(\Phi'(u)e^{izu}\) absolutely integrable,
since its magnitude is bounded by
\((8\pi|\sinh(4u)|+\|b\|_\infty)e^{|\operatorname{Im}z||u|}\Phi(u)\).
Integration by parts over a finite interval followed by its expansion
to \(\mathbb R\) gives
\[
 \int_{\mathbb R}V_0'(u)e^{izu}\,d\mu(u)
  =-\frac1Z\int_{\mathbb R}\Phi'(u)e^{izu}\,du=izF(z).
\]
With \(F_\pm=F(z\pm4i)\), multiplication by \(e^{4u}\) shifts \(z\)
to \(z-4i\), and multiplication by \(e^{-4u}\) shifts it to \(z+4i\).
Therefore
\[
 4\pi(F_- -F_+) + B(z)=izF(z). \tag{1}
\]

## 2. Exterior bounds and the pointwise margin

Take \(z=x+iy\), \(0<y<1\), and \(s=(1-iz)/2=(1+y-ix)/2\).
The upper shift corresponds to \(w_+=s+2\). Reflection sends the
lower shift from \(s-2\) to \(w_-=3-s\). In the checked convention,
\[
 \xi(w)=\tfrac12 w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w),
 \qquad \xi(w)=\xi(1-w).
\]
Their respective arguments have real parts
\(\sigma_+=(5+y)/2\) and \(\sigma_-=(5-y)/2\), both greater than \(2\),
and imaginary parts \(-x/2\) and \(x/2\). These substitutions use the
classical functional equation alone. [Riemann, translated pp. 2–3][riemann]
[DLMF (25.4.3)–(25.4.4)][xi]

For \(w=\sigma+it\), \(\sigma>1\), the Euler product and
\(1-p^{-\sigma}\le |1-p^{-w}|\le1+p^{-\sigma}\) give
\[
 0<\frac{\zeta(2\sigma)}{\zeta(\sigma)}
    =\prod_p(1+p^{-\sigma})^{-1}
    \le |\zeta(w)|\le\zeta(\sigma).
\]
Indeed, the prime sums of \(p^{-\sigma}\) converge, and the lower and
upper bounds for every finite partial product pass to the limit. Both
exterior arguments therefore have zeta modulus in
\([1/\zeta(2),\,\zeta(2)]\) for every real \(x\). The real parts of
\(w_\pm\) exceed \(2\), so the polynomial factors are nonzero and
the gamma factors are regular and nonzero. This proves \(F_+F_-\ne0\)
throughout the stated domain. [Riemann, translated pp. 1 and 4][riemann]
[DLMF (25.2.1), (25.2.11)][euler] [DLMF §5.2(i)][gamdef]

For bounded positive \(a\) and \(T\to+\infty\), sectorial Stirling
gives uniformly
\[
 |\Gamma(a\pm iT)|
   =\sqrt{2\pi}\,T^{a-1/2}e^{-\pi T/2}\bigl(1+O(T^{-1})\bigr).
\]
The first-neglected-term remainder in the log expansion is
\(O(T^{-1})\) on \(|\arg(a\pm iT)|\le\pi/2\). For either sign,
the real part of the main logarithmic term is
\((a-\tfrac12)\log|a+iT|-T\arg(a+iT)-a\), with
\(\log|a+iT|=\log T+O(T^{-2})\) and
\(\arg(a+iT)=\pi/2-a/T+O(T^{-3})\) uniformly for bounded \(a\).
This proves the uniform magnitude estimate directly.
[DLMF (5.11.1), (5.11.9) and §5.11(ii)][stirling]

Put \(T=x/4\). The gamma argument is \(w_\pm/2\) and has imaginary
part of magnitude \(T\). The polynomial product \(w_\pm(w_\pm-1)\)
has modulus \(4T^2(1+O(T^{-2}))\) uniformly. Thus with
\(w=w_\pm\), \(\sigma=\operatorname{Re} w\), the corresponding anchor
has magnitude
\[
 \frac{\sqrt{2\pi}}{2Z}\pi^{-\sigma/2}
   T^{(\sigma+3)/2} e^{-\pi x/8}\,|\zeta(w)|
   \bigl(1+O(x^{-1})\bigr),
\]
uniformly for \(0<y<1\). In particular, on every fixed
\(0<y_0\le y\le Y<1\), the following
two-sided bounds have positive constants independent of \(y\) and \(x\)
for all sufficiently large \(x\).
\[
 |F_+|\asymp e^{-\pi x/8}x^{(11+y)/4},
 \qquad
 |F_-|\asymp e^{-\pi x/8}x^{(11-y)/4}.
\]
Writing \(r=F_-/F_+\) gives \(|r|=O(x^{-y/2})\), also uniformly
there. The bound tends uniformly to zero by \(y\ge y_0>0\).
Consequently
\[
 \Delta=4\pi(|F_+|-|F_-|)
       =4\pi |F_+|\bigl(1+O(x^{-y/2})\bigr)
       \asymp e^{-\pi x/8}x^{(11+y)/4}>0
\]
eventually on that interval. At any point of this domain the
reverse triangle inequality in (1) gives
\[
  |z|\,|F(z)|\ge \Delta-|B(z)|.
\]
The condition \(|B(z)|<\Delta\) therefore excludes a zero at that
point and supplies the displayed positive lower bound divided by
\(|z|\). The argument gives no cutoff uniform down to \(y=0\).

## 3. Normalized remainder and absolute Dirichlet summation

The exact gamma recurrence gives
\(\Gamma((s+2)/2)=(s/2)\Gamma(s/2)\). Hence, with the same \(\xi\)
normalization,
\[
 \frac{\xi(s)}{\xi(s+2)}
   =\frac{2\pi(s-1)}{(s+2)(s+1)}
      \frac{\zeta(s)}{\zeta(s+2)} .
\]
The cancellation takes place in \(1/2<\operatorname{Re}s<1\), where
the gamma factors are regular and \(s\ne0\); \(\zeta(s+2)\ne0\)
by the exterior product bound. [DLMF (5.5.1)][recurrence]

Using \(iz=1-2s\), divide (1) by the nonzero \(4\pi F_+\) and solve for
the canonical \(B\). The result is
\[
 \frac{B(z)}{4\pi F_+}
   = 1-r-D(s)\frac{\zeta(s)}{\zeta(s+2)},\qquad
 D(s)=\frac{(2s-1)(s-1)}{2(s+2)(s+1)}. \tag{2}
\]
The unprovided comparison for the pointwise test is
\(\left|1-r-D(s)\zeta(s)/\zeta(s+2)\right|<1-|r|\).
This involves the phase of the interior zeta value with the exact
exterior denominator and the same two anchors.

For \(\operatorname{Re}s>1\), dividing the two absolutely convergent
Euler products and expanding each local quotient gives
\[
 \frac{1-p^{-s-2}}{1-p^{-s}}
    =1+(1-p^{-2})\sum_{k\ge1}p^{-ks}.
\]
Unique factorization and absolute summation yield
\[
 \frac{\zeta(s)}{\zeta(s+2)}
     =\sum_{n\ge1}a_n n^{-s},\qquad
 a_n=\prod_{p\mid n}(1-p^{-2}),\qquad a_1=1.
\]
For a finite prime product, expansion is dominated in absolute value
by \(\sum_{n\ge1}n^{-\operatorname{Re}s}\) since every \(a_n\le1\).
Passage to all primes follows by this domination. All factors lie
in \((0,1)\), so comparison with the product over all primes gives
\(1/\zeta(2)\le a_n\le 1\). For every
\(\operatorname{Re}s\le1\), \(\sum_n |a_n n^{-s}|\) diverges
by comparison with the divergent real power sum. This rules out
absolute summation of these unmodified coefficients in the comparison
domain. The meromorphic quotient itself is holomorphic throughout
\(1/2<\operatorname{Re}s<1\), since \(\zeta(s)\) is regular there
and \(\zeta(s+2)\) is nonzero. Signed representations and estimates
are a separate question. [DLMF §25.2(i), (25.2.11)][euler]

## 4. Comparison scope and controls

Conditional on the proposed [E17][e17] best allowance of order
\(x^{7/2}e^{-\pi x/8}\) at fixed \(Y<1\), for any fixed
\(0<y\le Y\) the ratio of that allowance to \(\Delta\) is comparable
to \(x^{(3-y)/4}\). It tends to infinity. This is a comparison for the
specified termwise-absolute contour majorant after its optimization.
The actual \(|B|\) and cancellation-aware estimates of its integral
remain open in this comparison.

The [catalog][controls] controls distinguish the premises of (1)
from the arithmetic inputs to (2). Smooth integrable controls may
satisfy the integration-by-parts relation with their own score.

| Control class | Premise missing for the canonical comparison |
| --- | --- |
| Euler-factor translates | The literal transform has an extra finite factor, so the unchanged \(\xi\) completion and exact ratio in (2) fail. The normalized score also changes. |
| Weighted-square controls and finite square-mode changes | They change the coefficients in the complete square expansion and fail full canonical reflection. Their bounded own-score estimates in [E06][e06] do not give (2). |
| Reflected super-Gaussian | Reflection survives but the complete square expansion and bounded exponential-reference score remainder fail. |
| Smooth shape and positive-primitive controls | They lack the complete equal-coefficient square expansion and its literal \(\xi\) readout, including in the case of an identical primitive spectral asymptotic expansion. |
| Finite-prime orbit perturbations | They change canonical square coefficients and fail full reflection. Their retained finite identities do not supply both exterior evaluations. |
| Atomic fixed-event and finite-profile controls | The atoms lack a smooth positive density for this score. Compact triangular extensions lack full-line positivity and the canonical arithmetic transform. |
| RH-conditional normalized endpoint controls | They fail ordinary Dirichlet-series arithmetic and the unchanged theta source, even with their retained completion and with their stated RH assumption. |
| Fixed amplitude with a varied observation kernel | The source can remain canonical while the literal exponential readout required in (1) and (2) changes. |

The [E12/E15 midpoint screen][midpoint] has its own scope. Exact finite
tests with the canonical \(b\) can persist in smooth perturbations whose
pointwise own score and constant-coefficient square-source representation
fail. They do not inherit the use of the physical score in (1).
These screens assert premise failures for the recorded controls. The
positive anchor estimate tests the complete source at \(\lambda=0\)
on fixed interior lines, with constants uniform over compact
subintervals of \(0<y<1\).

[request]: ../research-progress/handoffs/VCD-E18-r1.md
[decision]: ../brainstorm/notes/10_VCD_B05_CANONICAL_FOURIER_SCORE_DECISION_20261116.md
[e06]: 06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md
[midpoint]: 15_VCD_MIDPOINT_RESEARCH_SYNTHESIS_20261116.md#2-finite-canonical-score-and-midpoint-data-leave-local-freedom
[e17]: ../research-progress/handoffs/VCD-E17-r1.md
[manuscript]: ../manuscript/main.tex
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[riemann]: https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf
[rt]: https://arxiv.org/pdf/1801.05914v5
[xi]: https://dlmf.nist.gov/25.4
[euler]: https://dlmf.nist.gov/25.2
[gamdef]: https://dlmf.nist.gov/5.2.i
[recurrence]: https://dlmf.nist.gov/5.5.E1
[stirling]: https://dlmf.nist.gov/5.11
