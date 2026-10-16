# Evaluation of the candidate bulk theories package

12 September 2026. AI-assisted mathematical review of the package in [candidate-bulk-theories](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/susy-positivity/brainstorm/candidate-bulk-theories/README.md). The original research files were not changed.

## Assessment

This is a substantive first investigation with useful operator constructions, exact transport identities, and appropriately scoped failures. Its main accomplishment is a concrete framework in which the missing arithmetic identity can be tested. It establishes neither a new positivity range for the full Weil form nor a field-theoretic symmetry that selects all its arithmetic data.

The relative complex is the strongest foundation for a positive boundary state. The exact loop construction is the strongest arithmetic ingredient because it already accounts for every active prime repetition and its interval endpoint correction. The scalar derivative deformation is informative, but its demonstrated coefficient failures mean it needs a structural revision. I would not prioritize adding continuous residual corrections to that unchanged scalar family.

## 1. What I checked and what holds up

I read the README, four model notes, failures, continuation, reproduction guide, source audit, and new checker. I rederived the principal relative-complex projection, the finite-horizon Poisson and scattering-defect identities, the first and mixed derivative formulas, the contact in the infinite-channel limit, and the scalar finite-coupling repetition expansion.

The gamma partial fractions and high-frequency asymptotic were checked against [DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6) and [DLMF 5.11](https://dlmf.nist.gov/5.11). The other model comparisons were inspected at the level of their stated equations; this is not a complete fresh audit of every literature attribution or infinite-dimensional domain statement.

The supplied new checker was rerun using its recorded bundled Python, with output outside the source repository. It passed. Observed maximum discrepancies were:

| Diagnostic | Maximum discrepancy |
|---|---:|
| Gamma amplitude/kernel pairing | \(3.28\times10^{-14}\) |
| Actual logarithmic-delay pairing | \(1.78\times10^{-15}\) |
| First deformation derivative | \(2.00\times10^{-10}\) |
| Mixed product derivative | \(1.21\times10^{-7}\) |

These are floating-point diagnostics, not continuum positivity certificates. I did not rerun the historical rational-certificate suite in this review, and I make no priority or specialist-validation claim.

### Relative cohomology

The map \(D_a u=(u,u'/a)\) and the degree-one class of \((F,0)\) resolve the earlier exact-state concern correctly. The harmonic representative is

\[
\sqrt{2/a}\,(F-u_f,-u_f'/a),\qquad
(1-a^{-2}\partial_x^2)u_f=F.
\]

It is killed by \(D_a^*\), and its norm reproduces the known gamma kinetic channel. The use of a different differential from the energy-amplitude factor is mathematically substantive.

The limitation is also correctly stated: the harmonic projection performs the old minimization. Representative independence, invariance under same-range reparametrization, and invariance under heat evolution of an already harmonic state are exact, but they do not select the arithmetic couplings. This is presently a Hilbert-complex realization with supersymmetric operators, rather than a derived local superspace action whose Ward identity forces the Weil pairing.

### Exact arithmetic loop

For \(W=(I-rT)^{-1}\),

\[
W+W^*-I=W^*(I-r^2T^*T)W
\]

gives the stated positive residence/escape pairing, including its endpoint term. Consequently one prime's entire contribution is exactly \(a(\|f\|^2-\|Yf\|^2)\). This is better arithmetic information than matching only the leading singularity of a small-coupling variation. Its unresolved sign is real, and the package correctly retains it as a difference of norms.

### Infinite-channel deformation

For \(B(s)=\sum_k(2/a_k)s/(a_k^2+s)\), minimization really gives the positive boundary multiplier \(B(\tau^2|m(\tau)|^2)\). The first variation has the factor \(h(\tau)=2\tau^2B'(\tau^2)\), and \(h\to1\) requires the infinite tower. The distributional contact in the inverse transform of \(h\) is essential and is handled correctly.

This mechanism works for arbitrary prescribed delay labels. Its ability to produce a leading translation singularity demonstrates useful flexibility; it does not yet explain why the labels and coefficients should be arithmetic.

## 2. Additional obstruction: the prime 3 already exceeds the scalar coefficient range

The finite product family in [04_COHERENT_DEFORMATION.md, equation (11a)](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/susy-positivity/brainstorm/candidate-bulk-theories/04_COHERENT_DEFORMATION.md:114) has one factor \(1-\alpha_p e^{-i\tau\log p}\) per prime, with \(0<\alpha_p<1\). Its singular cosine coefficients are

\[
-\frac{\alpha_p^n}{n},
\]

whereas the target coefficients are \(-2(\log p)p^{-n/2}\). Matching the first repetition requires

\[
\alpha_p=\frac{2\log p}{\sqrt p}.
\]

For \(p=2\), this is approximately \(0.980258\), within the stated range. This is a positive control for first-coefficient matching. For \(p=3\), it is approximately \(1.268568\), outside that range. Thus as soon as \(L>\log3\), the stipulated family already cannot match the first 3-delay using only continuous residual corrections.

Allowing a positive real \(\alpha>1\), while retaining uniform invertibility on the whole line, does not fix this particular problem:

\[
\log|1-\alpha e^{-it}|
=\log\alpha-\sum_{n\ge1}\frac{\alpha^{-n}}n\cos(nt).
\]

Its first oscillatory coefficient has magnitude \(1/\alpha<1\). The case \(\alpha=1\) is outside the uniformly invertible setup. Multiple copies, other weights, new primitive channels, or a different transfer could change this conclusion, but each is a structural modification of the specified family.

The package already proves a separate repetition failure for \(p=2\): matching its first term produces second cosine coefficient magnitude \((\log2)^2\approx0.480453\), rather than \(\log2\approx0.693147\). This becomes active at \(L>\log4\).

These are singular coefficient mismatches. A continuous kernel cannot cancel an incorrect delta on an active translation line as a distribution on arbitrary test pairs. This does not prohibit correction blocks that themselves generate new delta terms; it specifies what such blocks must do.

## 3. The proposed next step must distinguish a tangent residual from a finite-coupling residual

The derivation explicitly warns against setting a tangent parameter to one. The continuation nevertheless prioritizes canceling the translated \(k\) kernel and the mixed \(V\) kernel while seeking an exact restricted completion. Those kernels describe derivatives at zero coupling. Canceling them does not by itself cancel the full finite-coupling error.

For a single 2-delay, put \(d=\log2\), \(\alpha=2d/\sqrt2\), and

\[
m_\alpha(\tau)=1-\alpha e^{-id\tau}.
\]

Define the exact regular remainder

\[
r_\alpha(\tau)
=B(\tau^2|m_\alpha(\tau)|^2)-B(\tau^2)-\log|m_\alpha(\tau)|.
\]

It is continuous and \(O(\tau^{-2})\), hence integrable, for fixed \(0<\alpha<1\). The logarithmic piece supplies the delta series. On a window \(\log2<L\le\log3<2\log2\), all its repeated delta shifts after the first are inactive. Thus the exact finite-coupling kinetic change on that interval is the desired first-prime term plus the compressed convolution kernel of \(r_\alpha\).

The first derivative of this remainder at zero is \((1-h(\tau))\cos(d\tau)\), giving the package's translated \(k\). But at the actual matching coefficient,

\[
r_\alpha(0)=-\log(1-\alpha)\approx3.925014,
\]

while its first-order prediction there is only \(\alpha\approx0.980258\). This is a comparison of whole-line multiplier values, not by itself a theorem about a compressed interval operator.

To check the distinction on a permitted input as well, I used

\[
f(x)=
\begin{cases}
\exp\!\bigl(-1/[1-(x/0.49)^2]\bigr)(1+0.3ix)e^{3ix},&|x|<0.49,\\
0,&|x|\ge0.49,
\end{cases}
\]

which belongs to \(C_c^\infty(I_1)\). Direct Fourier quadrature of the printed exact symbol gives:

| Quantity | Computed value |
|---|---:|
| \(\|f\|^2\) | \(0.0653741512885\) |
| Exact finite-coupling energy change \(Z_\alpha(f,f)-K[f]\) | \(+0.00346853325\) |
| First-order prediction \(-\alpha(2\pi)^{-1}\int h(\tau)\cos(d\tau)|\widehat f(\tau)|^2d\tau\) | \(-0.00405814876\) |

The exact change and tangent prediction have opposite signs on this input. Two refined quadratures differed by approximately \(4.2\times10^{-11}\) for the exact change. This is a numerical diagnostic, not an interval enclosure. Small-coupling controls in the same calculation recover the derivative and show the error shrinking quadratically.

The appropriate next target is therefore the exact finite-coupling remainder, or a complete differential evolution whose integration is proved to produce the desired form. First- and second-order residual calculations remain useful diagnostics, but should be identified as such.

## 4. How I would redirect the next investigation

1. Retain the relative complex as the positive-state framework.
2. Use the exact primitive-loop identity as the arithmetic reference, since it already has the correct repetitions and endpoint terms.
3. Before adding correction blocks, require any revised finite-coupling rule to pass the first 2-delay, first 3-delay, and repeated-2 singular coefficient tests. These are analytical filters, not positivity sweeps.
4. For a first-prime-only test, compute the exact \(r_\alpha\) response and specify the class of correction blocks that could represent it. A few scalar pole amplitudes are finite-rank; they cannot generically be assumed to cancel an arbitrary convolution residual. A field-valued block may have infinite rank, so it must be judged from its actual response.
5. Seek a shared conservation or coupling identity that relates the gamma state and exact loop histories. The exact difference-of-norms organization is useful bookkeeping, but declaring its range map a contraction would assume the missing inequality.

The result merits another focused research pass. Its value is that broad questions have become explicit projection, transport, and kernel calculations. The next pass should address the finite-coupling arithmetic selection problem before investing in detailed corrections to a family whose active delta coefficients already fail.

## Reproduction

- [Additional checker](check_finite_coupling.py)
- [Additional diagnostic record](finite-coupling-diagnostics.json)
- [Fresh replay of the supplied new diagnostics](supplied-model-diagnostics.json)

The additional code uses NumPy and a recurrence/asymptotic evaluation of the digamma function. It checks that implementation against a 200,000-channel positive partial sum at moderate frequencies, compares two quadrature resolutions, and includes small-coupling controls. No zeta-zero data, target spectral square root, or numerical full-Weil eigenvalue claim enters this review.
