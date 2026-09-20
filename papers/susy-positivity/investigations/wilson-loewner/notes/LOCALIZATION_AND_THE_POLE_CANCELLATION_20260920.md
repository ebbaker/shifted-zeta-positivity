# Localization as a candidate explanation of the gamma/pole cancellation

20 September 2026. Research direction and auxiliary calculation, prepared for Edward Baker.

**Model:** OpenAI GPT-6 (Codex). **Reasoning effort:** the configured effort is not exposed to the assistant in this session; no level is inferred.

**Origin:** Edward Baker suggested revisiting supersymmetric localization, recalling the extension of Pestun's Wilson-loop work discussed with Ofer Aharony during his open-Wilson-line research. This note develops that suggestion in relation to item 6.2 of the [fixed-window response calculation](FIXED_WINDOW_WILSON_RESPONSE_OBSTRUCTION_20260920.md).

**Status:** localization is a plausible mechanism to investigate, not an established realization. The finite product below is an exact auxiliary Gaussian/Berezin identity. Its spectrum is prescribed from the arithmetic comparison; no supercharge, localization complex or physical Wilson-to-response dictionary deriving it has been constructed.

## 1. Relevant literature and the distinction it suggests

Pestun reduces selected circular Wilson-loop expectations on the four-sphere to a matrix integral. His one-loop calculation expresses fluctuation cancellations through kernel/cokernel multiplicities of an equivariant complex; this is the relevant structural mechanism for testing a proposed surviving mode spectrum. [Pestun, arXiv:0712.2824, Section 4, especially equations (4.23)–(4.25)](https://arxiv.org/pdf/0712.2824).

Baker's own Section 3.3 distinguishes the defect problem from that circular-loop construction and suggests reduction to a one- or two-dimensional theory, given the preserved bosonic symmetry and endpoint renormalization. [Baker, arXiv:1102.4948, Sections 3.3–4](https://arxiv.org/pdf/1102.4948).

Wang develops localization for supersymmetric defect networks in four-dimensional \(\mathcal N=4\) SYM, with a two-dimensional gauge theory coupled to boundary topological quantum mechanics. Section 5.1, equation (5.5), includes bilocal endpoint operators joined by gauge transport. Section 4.4 explicitly leaves a normal-fluctuation determinant unevaluated and motivates its being one. These are relevant tools and a stated limitation, not a result for our arithmetic operator. [Wang, *Taming Defects in \(\mathcal N=4\) Super-Yang-Mills*, arXiv:2003.11016](https://arxiv.org/pdf/2003.11016).

The next physical comparison should therefore use a defect-preserving localization construction and the original conformal open-line geometry as controls. Simply applying the circular-loop matrix model to the polynomial bulge would not be justified.

## 2. An exact auxiliary product for the complete prime-free factor

For \(0<L<\log2\), the preceding note obtains the arithmetic factor

\[
 K_\omega^{<}(p)=
 \pi^\omega
 \frac{\Gamma((p+5/2-\omega)/2)}
      {\Gamma((p+5/2+\omega)/2)}
 \frac{p-1/2-\omega}{p-1/2+\omega}.
 \tag{2.1}
\]

Its causal compression is the full arithmetic transfer on that window. Outside this compression the integer comb is still required.

The earlier auxiliary gamma model used one complex Gaussian mode at each rate \(a_n=2n+1/2\), including \(n=0\). Modify that **auxiliary model** as follows: retain the complex bosons for \(n=1,\ldots,N\), and include one complex Grassmann pair of weight \(p-1/2\). Choose the Berezin orientation so that its Gaussian integral equals \(p-1/2\). For real \(p>1\), define

\[
\begin{split}
 Z_N(p)
 &=
 \left(\int d\bar\chi\,d\chi\,
     e^{-(p-1/2)\bar\chi\chi}\right)
 \prod_{n=1}^N
 \left(\int_{\mathbb C}\frac{d^2z_n}{\pi}
     e^{-(p+a_n)|z_n|^2}\right)\\
 &=(p-1/2)\prod_{n=1}^N(p+2n+1/2)^{-1}.
 \tag{2.2}
\end{split}
\]

All bosonic integrals also converge at \(p\pm\omega\) for the stipulated \(0\le\omega\le1/2\). Complex bosons matter: real Gaussians would give square roots.

Put \(z_\pm=(p+1/2\pm\omega)/2\). Direct finite-product algebra gives

\[
\begin{split}
 \frac{Z_N(p-\omega)}{Z_N(p+\omega)}
 ={}&\frac{p-1/2-\omega}{p-1/2+\omega}\\
 &\times
 \frac{\Gamma(N+1+z_+)\Gamma(1+z_-)}
      {\Gamma(N+1+z_-)\Gamma(1+z_+)}.
\end{split}
\]

Consequently,

\[
 \boxed{
 \pi^\omega\lim_{N\to\infty}N^{-\omega}
 \frac{Z_N(p-\omega)}{Z_N(p+\omega)}
 =K_\omega^{<}(p).
 }
 \tag{2.3}
\]

The first rational pole in the original factorization is accounted for by removing the \(n=0\) boson. The remaining rational factor is accounted for by the Grassmann pair. This is an algebraic way for precisely the required mode cancellation and signed factor to occur.

It is **not** a supersymmetric model merely because bosons and fermions appear. Their pairing, the absence of the lowest boson, the surviving odd mode and their multiplicities must follow from an actual \(Q\)-complex and its boundary conditions. Nor is the Berezin factor itself a positive Hilbert-space norm.

The normalization \(N^{-\omega}\pi^\omega\) is still supplied externally. Differentiating the finite expression makes this obligation explicit:

\[
 -\left.\partial_\omega\log
 \left[\pi^\omega N^{-\omega}
 \frac{Z_N(p-\omega)}{Z_N(p+\omega)}\right]\right|_{\omega=0}
 =
 \log N-\log\pi+\frac2{p-1/2}
       -2\sum_{n=1}^N\frac1{p+2n+1/2}.
\]

Its limit is

\[
 a_0^{<}(p)=
 \psi\!\left(\frac54+\frac p2\right)-\log\pi+\frac2{p-1/2}.
 \tag{2.4}
\]

Reintroducing the removed lowest mode rewrites this with the original fixed local term \(w_0=\psi(1/4)-\log\pi\). Thus the product matches the entire specified prime-free symbol under the chosen normalization, rather than only its gamma spectrum. Localization must determine the compatible finite renormalization; freedom to choose a counterterm is not evidence for its arithmetic value.

### A mode-counting test without that additive local constant

Differentiating (2.4) with respect to the Laplace variable yields an absolutely convergent condition:

\[
 \boxed{
 \partial_p a_0^{<}(p)
 =2\sum_{n=1}^\infty\frac1{(p+2n+1/2)^2}
       -\frac2{(p-1/2)^2}.
 }
 \tag{2.5}
\]

Equivalently, for \(\Re p>1\),

\[
 \partial_p a_0^{<}(p)
 =2\int_0^\infty
 u e^{-pu}
 \left[\frac{e^{-5u/2}}{1-e^{-2u}}-e^{u/2}\right]du.
 \tag{2.6}
\]

This removes a \(p\)-independent additive generator normalization, but not arbitrary \(p\)-dependent counterterms. It provides a sharp comparison for a computed virtual mode character. The relative weight \(-1/2\) of the odd mode is not, by itself, a claim of a negative physical energy: the auxiliary Gaussian depends on \(p-1/2\) in the right half-plane. Identifying \(p\) with a physical equivariant or boundary parameter is part of the missing dictionary.

## 3. What localization would have to establish

There are four concrete tests.

1. **A compatible observable and charge.** Specify the conformal open line, the defect, the endpoint polarizations and the reference sector on the spherical or hemispherical geometry. Verify closure under one localization supercharge, with its square preserving the required boundary data. The earlier fixed-H, constant-Poincare endpoint obstruction does not exclude conformal Killing-spinor constructions. For localization of a whole network it is \(Q\)-closure of that whole observable that must be proved; independent closure of every factor is a sufficient condition, not an automatic necessity.

2. **Actual surviving modes.** Compute the relevant fluctuation complex, boundary modes and observable insertions. Determine whether their contribution yields (2.5), including multiplicities, rather than assigning that character by hand. The full answer might involve the reduced theory's correlators as well as a one-loop determinant; there is no reason to assume all required factors must arise from the determinant alone.

3. **A nontrivial physical shift.** The localization deformation parameter multiplying a \(Q\)-exact term cannot simply be called \(\omega\): under the localization hypotheses, a fixed \(Q\)-closed expectation is independent of it. A physical mass, boundary coupling, admissible contour/area parameter or source deformation could vary nontrivially, but its relation to \(\omega\), and to \(p\), must be derived. Boundary contributions and changes of the observable have to be included.

4. **The boundary response and its norm.** A localized scalar expectation or partition ratio is not yet a causal operator on arbitrary \(L^2(I_L)\) input. Derive the source map, identity limit, right-Laplace causal realization and the physical adjoint. If the resulting operator retains the identity-plus-regular-kernel form excluded in the previous note, localization cannot change that mathematical obstruction. A successful construction must produce the different, singular limiting response structure required there.

The fourth test also separates cancellation from positivity. Cohomological signs can explain a determinant cancellation without explaining an ordinary reflected positive metric. One must retain the physical adjoint rather than silently substituting an R-symmetry-twisted pairing.

## 4. Recommended continuation and remaining positivity problem

The useful immediate investigation is a **localization compatibility and mode-counting calculation** for the original conformal open-line/defect setup, using the hemispherical defect framework as a comparison. The first deliverable should be an explicit preserved \(Q\), its boundary conditions and the resulting unpaired-mode contribution, or a scoped obstruction to obtaining (2.5). This should precede a full interacting calculation on a contour whose localization compatibility is unknown.

Success would explain part of the prescribed arithmetic response and could motivate a more appropriate boundary operator. It would still leave the finite normalization, the continuum operator dictionary, and the arithmetic delays beyond \(\log2\) to be derived. The auxiliary product (2.3) already shows why matching a special function alone does not settle those questions.

The cumulative objective remains
\[
 \|f\|^2=\|V_{\omega,L}f\|^2+\|\mathcal B_{\omega,L}f\|^2,
\]
with independently defined physical amplitudes. Localization must not be used to infer this from a signed determinant. Later spatial gluing must still bound the full cross map in the old-input and new-output defect metrics, together with admissible shift changes and the all-depth condition \(L_j\to\infty,\ \omega_j\downarrow0\).

No additional numerical experiment, localization theorem, contraction certificate or arithmetic Loewner driver is claimed in this note. The product and derivative identities are analytical calculations. The manuscripts remain unchanged.

This note was developed with OpenAI GPT-6 (Codex) following Edward Baker's suggestion. Its proposed physical interpretation requires independent verification.
