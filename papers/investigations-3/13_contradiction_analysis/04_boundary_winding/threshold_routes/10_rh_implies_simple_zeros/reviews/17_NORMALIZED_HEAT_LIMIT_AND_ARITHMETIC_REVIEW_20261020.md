# Internal review of the normalized-heat continuation

20 October 2026. Prepared for Edward Baker with LLM assistance. Actual model **gpt-6-astra**, effort **ultra**. Separate same-model analytic check; not specialist, cross-model, formal, or priority validation. Reviewed from checkpoint `071cee983f0c094943b5462c577ade35454d4cf5`.

Reviewed the complete scaled-tail and real-axis proofs in [Note 17](../notes/17_NORMALIZED_HEAT_GLOBAL_LIMIT_AND_ARITHMETIC_COSTS_20261020.md), (CN1)–(CN21) and (RN1)–(RN12). The verdict is a pass after one scope correction, now applied: the uniform local convolution and \(O(L^{-1})\) product estimates in CN19–20 hold on the fixed **critical-line segment**, while analyticity and Taylor estimates are taken from a surrounding disk. The former wording “whole fixed disk” was not supported by the displayed imaginary-axis Fourier estimates.

## Normalized numerator and complete tails

The exact Gaussian formula uses real displacement \(\sqrt{\tau}x\) with density \(\pi^{-1/2}e^{-x^2}\), hence variance \(\tau/2\) and heat generator \(\partial_s^2/4\). This agrees with both the theta formula and the local Hermite normalization. Absolute Fubini is justified by the original superexponential source, not by separately heating the meromorphic completion factor.

The primary [Chandee–Soundararajan Theorem 1.1](https://arxiv.org/pdf/0908.2008) was reopened: its stated RH bound implies the critical-line \(t^\varepsilon\) estimate used here. Phragmén–Lindelöf and the Euler half-plane give the declared uniform bound to the right of that line. Reflection of the complete \(\xi\) function handles negative Gaussian displacements without inserting an uncontrolled left-half-plane zeta bound.

In CN8–9, Stirling gives a quadratic completion error \(O((a+a^2)/t)\). Completing the Gaussian square cancels precisely \(\tau(\Re\alpha)^2/4\); the surviving exponent is bounded uniformly for \(0\le\tau\le\tau_0\), including \(\tau\downarrow0\). The region \(a\ge t/2\) is suppressed by \(e^{-a^2/\tau}\) against the complete order-one bound. The normalization \(\tau^{-1/2}\) is harmless uniformly down to zero on that remote region. Thus CN7 supplies the required uniform normalized numerator without using a height condition of the form \(\exp(C/\tau)\).

The completion cancellation in CN12 is exact: the numerator uses the complete original \(F=\xi(1/2+\cdot)\), so the completion ratio is \(A(s+b_y)/A(s)\), with no remaining \(A(s+a)\). Removing all cluster zeros retains every multiplicity. For each cluster factor the two inequalities in CN14 follow from the same elementary denominator comparison as ST. Choosing \(H=M+1\) is decisive:
\[
(1+\sqrt V|x|/H)^M\le e^{\sqrt V|x|}.
\]
All its Gaussian moments are finite constants depending only on the fixed bound \(V\). The extra variable therefore does not change the sharp Gevrey moment exponent \((\sigma-1)M\log M\).

Both omitted tails are paid in the correct order. The large inverse-convolution variable is treated after performing the complete Gaussian numerator integral, using CN7. For the central inverse-convolution variable, the omitted Gaussian range has suppression \(e^{-c_Vr^2L^2}\), which dominates the coarse reciprocal payment \(e^{CU\log(2+L)}\) throughout \(U\le L^b\), \(b<1/\sigma<1\). The high-height range needs only CN7 and the existing sharp reciprocal estimate. No absolute two-variable estimate is silently extended over both unbounded variables.

The resulting nearest-zero-distance estimate gives the same scaled-cell integral \(4\), requires no minimum spacing, and counts every occurrence of a zero. The high-height inequality \(L\le(\log t)^{1/b}\) pays the remaining scaled tail. Finite exceptional \(N\), bounded heights, and \(v\) in a fixed compact interval are all covered. This justifies CN3 with the stated fixed-taper and bounded-\(v\) scope.

## General multiplicity profile and exhaustion

The polynomial \(P_{m,v}\) has the heat-generator coefficient \((v/4)^k\), including the correct factorial. For \(k\ge1\), lower Laurent terms and the next Taylor coefficient contribute \(O(L^{-1})\) on the fixed critical-line segment; the \(k=0\) term uses the already coherent CH subtraction. Taking \(2K+2\ge m+1\) pays the heat Taylor remainder against \(V=O(L^m)\).

At zero, only \(f_m^{(m-1)}(0)=1\) contributes to the leading integration-by-parts boundary term. Every lower derivative appearing in CN4 has zero initial data, and all terminal data vanish. Thus CN21 and the displayed density are correct, for odd and even multiplicities. The local profile is \(O((1+|Ly|)^{-1})\), and the complete tail estimate promotes the compact norm limits to CN5. Uniformity on compact \(v\)-sets follows from uniform compact estimates and the uniform positive tail bound; no derivative convergence follows.

## Real-axis arithmetic obstruction

RN5 correctly retains the complete \(\xi\) function across every real displacement. With \(R=(\log\sigma)^2\), its bound proves RN6 uniformly over the whole remote Gaussian tail. The central Gaussian tilt has mean \(ta/2\), variance \(t/2\), and pays the curvature error through its third and fourth moments. The difference \(a-\alpha=(\log A)'-\alpha=-1/(6\sigma^2)+O(\sigma^{-4})\) cannot cancel the leading curvature correction. Both terms
\[
\frac{t^2\log^2(\sigma/(2\pi))}{64\sigma}
\quad\text{and}\quad \frac{t}{8\sigma}
\]
are required and are correctly retained.

The ordinary-Dirichlet-series exclusion applies even to conditional convergence: convergence at a real point bounds the terms, hence gives absolute convergence two units to its right and exponentially fast approach to the first coefficient. RN3 contradicts that approach. Essential singularity alone would not have established this far-right conclusion; the proof keeps the two issues separate.

These results establish an actual complete boundary-norm theorem for the explicitly changed target, together with its arithmetic and analytic limitations. They neither assign the original Burnol lower bound to that target nor supply a multiplicity-independent original-zeta upper bound. The fixed-neighborhood perturbation cost in [Note 17 §8](../notes/17_NORMALIZED_HEAT_GLOBAL_LIMIT_AND_ARITHMETIC_COSTS_20261020.md), NT3, is compatible with the theorem and explains why a sharp small-perturbation transfer cannot be assumed.


## Essential singularity and the actual transfer cost

The coordinator separately checked NT1–NT4. Positivity of each original
theta summand gives F_t(1/2)>0, and A'(1)=1/2. In alpha=1/(s−1)+b(s),
b'(1)=0, so the analytic nonzero factor and NT1 constant are correct.
The growth exp[t/(4y²)] along Re s=1 survives every finite-order zero
or finite pole subtraction. This is an interior analytic failure of
the declared expression, not a critical-line divergence assertion or
a standalone proof against a far-right Dirichlet series.

For NT3, the leading difference is (v/2)A_2(iLy). Its Fourier transform
decays quadratically, so the full fixed-neighborhood cross term and
weight variation cost O(L^−2), without a logarithmic loss. The carrier
changes the already bounded local product by O(L^−2). Thus the exact
positive coefficient v²||uw||²/(4|rho|²) cannot be omitted when transferring
a sharp norm coefficient back to zeta. This remains a fixed-taper,
fixed-double-zero statement; it does not exclude coherent transfers or
other completions.

The original 148 tagged displays of Note 16 are preserved. No new
numerics or Lean assertion is used as a premise; the six-page manuscript
is unchanged. These checks are same-model internal evidence, not
specialist validation of the original ST theorem or this continuation.


## Focused follow-up on uniformity and the omitted Gaussian

A separate same-model pass checked CN7–CN9 and CN17 against the original
GC/ST estimates. Completing the square in CN9 leaves the exponent
\[
-\tau A_0^2/4+\tau B_0^2/4+
\frac{\tau(A_0+C/t)^2}{4(1-C\tau/t)}
=O_{\tau_0}(1+\log^2(t)/t),
\]
uniformly as \(\tau\downarrow0\). The reciprocal variance factor stays
bounded for \(t\ge2C\tau_0\). In CN17 the omitted Gaussian's positive
linear-to-quadratic ratio is \(O_V(U/(rL^2))=o(1)\), and its resulting
\(e^{-c_Vr^2L^2}\) dominates both the reciprocal factor and kernel mass
\(e^{CU\log(2+L)+H}\). The remote complete-function bound covers the
remaining region beyond \(|a|=t/2\). No additional correction was found.
This checks the new estimates within the imported internal GC/ST scope;
it is not an independent validation of those original premises.
