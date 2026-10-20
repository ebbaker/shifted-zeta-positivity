# Remote-gap complete payment and bounded event attempts: review

20 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
**gpt-6-astra (Codex), reasoning effort ultra**, verified from turn metadata.
Separate same-model derivations and checks; no specialist review, cross-model
review or novelty claim.

**Verdict.** [Note 13 §§7–8](../notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md) proves a complete same-bandwidth comparison for a fixed sinc power at every width and all sufficiently large heights, and a distinct exact separate-payment statement for a normalized remote addition. The hypotheses do not cover all signed kernels or coherent mixed prime cancellation. The short continuations in [Note 06](../notes/06_SIGNED_CORRELATION_RESOLUTION_AND_MOBIUS_ENERGY_20261020.md) and [Note 14 §6](../notes/14_EXACT_THETA_MODE_GRAM_CANCELLATION_20261020.md) correctly identify unsuccessful event-conditioned implications. No original multiple zero is excluded; RHS-02's positive signed-estimate gate remains unmet.

The [result index](../../../../../../../result-summaries/README.md), [controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md) apply, especially [scoped conclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [complete payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [gain before expansion](../../../../../../../avoid/20_volume_without_a_gain.md). These additions remain in existing notes. No new manuscript or numerical campaign was justified.

## 1. Independent complete-envelope audit

### Fourier and prime payment

The Fourier transform of \(k=\operatorname{sinc}^{2q}(\pi\delta x)\) is the convolution of \(2q\) probability densities \(\delta^{-1}1_{[-\delta/2,\delta/2]}\). Its support, nonnegativity, and \(C^2\) regularity at \(q=2\) are correct. The log-concavity import is exactly [Prékopa, Theorem 7, pp. 342–343](https://rutcor.rutgers.edu/Prekopa/pdf/SCIENT2.pdf); the theorem and its proof using marginalization were independently read. Uniform interval densities, including their zero exterior, satisfy its hypotheses.

With \(D=\gamma^2-g^2>0\), direct Fourier differentiation gives
\[
\widehat h=\phi+\frac{i\gamma}{\pi D}\phi'
                     -\frac1{4\pi^2D}\phi''.
\]
The sign and each factor of \(2\pi\) agree with RG4. Log-concavity yields \(\phi\phi''\le(\phi')^2\) on the support interior; \(C^2\) continuity and the zero first two endpoint derivatives extend the modulus comparison to knots and support endpoints. Thus \(C(h)\ge C(k)\) is termwise for the actual discrete prime-power samples, without replacing those samples by a continuous norm.

On the outer shell \(z=2\pi q\delta-u\in[1,2]\), the spline formula is exact once \(2\le2\pi\delta\):
\[
\phi(u/(2\pi))=\frac{\delta^{-2q}z^{2q-1}}
 {(2q-1)!(2\pi)^{2q-1}}.
\]
Writing \(r=2q-1\) gives \(\phi'/\phi=-2\pi r/z\) and \(\phi''/\phi=4\pi^2r(r-1)/z^2\). Substitution reproduces RG10 exactly, including the coefficient
\[
\frac{2r[(r+1)\gamma^2+(r-1)g^2]}{D^2z^2}.
\]
For sufficiently large \(\gamma\), the squared relative gain lies between positive multiples of \(\gamma^{-2}\), uniformly in this shell. Taking a square root is legitimate because the ratio tends uniformly to one, giving the claimed unsquared gain.

The prime-number-theorem shell estimate is correctly normalized:
\[
\sum_{e^{B-2}\le n\le e^{B-1}}\frac{\Lambda(n)}{\sqrt n}
\sim2(e^{-1/2}-e^{-1})e^{B/2},\qquad B=2\pi q\delta.
\]
It follows by partial summation from \(\sum_{n\le x}\Lambda(n)=x+o(x)\); see [Tao's Notes 4, Theorem 6](https://terrytao.wordpress.com/2021/02/12/246b-notes-4-the-riemann-zeta-function-and-the-prime-number-theorem/), independently checked. Prime powers have not been discarded. Endpoint atoms are \(O(Be^{-B/2})\) and do not affect the asymptotic. A fixed sufficiently large \(B\) threshold gives a lower bound valid for every larger real \(B\), hence a fixed \(\delta_0(q)\); no height-dependent exceptional bandwidth remains.

### Gamma, poles and uniformity

From [DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6), the displayed positive derivative series for \(w(y)=\Re\psi(1/4+iy/2)-\log\pi\) is correct. It converges locally uniformly, proving that \(w\) is even and increasing in \(|y|\). The asymptotic follows from [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2). Pairing \(x\) and \(-x\) gives the complete RG6 integral; no tail or remote negative interval is omitted. Since
\[
w(\gamma+x)+w(\gamma-x)\ge w(\gamma)+w(0),\qquad
w(\gamma+x)-w(\gamma-x)\ge0\quad(x\ge0),
\]
the coefficient in RG7 is \(M_2(k)/(4\pi D)\), as stated.

The poles are conjugate evaluations because both kernels have real coefficients. At each point \(-\gamma\pm i/2\), the multiplier is exactly \(-(g^2+1/4)/D\); hence RG8 retains the signed pole sum correctly. Only \(P(k)>0\) can cause a loss. Both complex-sine estimates used in RG9 are valid, and \((\gamma^2+1/4)/D\) stays bounded once \(\gamma\ge\max(2g,1)\).

The two regimes cover every positive bandwidth with a single eventual height threshold:

- For \(0<\delta\le\delta_0\), setting \(v=\delta\gamma\) gives gamma gain \(\gg\gamma\log\gamma/v^3\). The pole allowance is \(O_{q,\delta_0}(\min(1,v^{-2q}))\). For \(v\le1\), the gain-to-allowance ratio is at least a constant times \(\gamma\log\gamma\); for \(v\ge1\), it is at least that quantity times \(v^{2q-3}\ge1\). Thus the gamma increase pays the poles uniformly, including arbitrarily rapid \(\delta\downarrow0\).
- For \(\delta\ge\delta_0\), RG11 gives prime gain \(\gg_q\gamma^{-2}\delta^{-2q}e^{q\pi\delta}\). The possible pole loss is \(O_q(\gamma^{-2q}\delta^{-2q}e^{q\pi\delta})\). Their ratio tends to zero uniformly as \(\gamma\to\infty\) because \(q\ge2\); the gamma difference is already positive.

The kernels are entire and have at least quadratic decay in every fixed horizontal strip: the signed multiplier leaves \(O(|x|^{2-2q})\). Thus the explicit-formula and gamma integrals have the required convergence, including \(q=2\). Integer \(q\), fixed \(g\), and fixed \(q\) are essential stated restrictions.

### Scope retained

This is a fully paid comparison for the specified centered sinc-power family with one remote-gap quadratic multiplier. It proves neither a general signed-kernel obstruction nor a retained signed-prime estimate. It does not transfer the result to growing \(q\) or \(g\), arbitrary carriers, or carriers centered near the remote gap. The absence of a numerical height threshold is correctly stated; no finite-height certificate or multiple-zero exclusion is claimed. The scope wording in the staged draft is consistent with the proof.

## 2. Independent gap and remote-component check

The remote-component derivation was checked separately by the arithmetic reviewer and by root. The elementary floor-integral calculation gives the stated negative real part on |t|<=1/8, independently of a putative event. The Fourier translation has the positive phase exp(2 pi i gamma v), which exactly cancels the prime phase in the shifted explicit formula. All gamma, pole and prime-power terms in (RG13) are retained. When ell(gamma)=0 the added component has value zero at the target, and its separately paid allowance is nonnegative. This proves the narrow comparison (RG14); it does not compare coherent moduli or mixtures whose normalization changes.

Root also independently checked the centered sinc proof. In particular the second-moment scale is delta^(-3) for every fixed power; for sinc fourth it is exactly 1/(2 pi² delta³). The two width ranges cover all delta>0, while the height threshold depends on the fixed power and gap. No numerical value for that threshold is asserted.

## 3. Local reciprocal energy and coherent theta tail

Root rederived the localized double-pole coefficient 8 w(gamma)/|rho zeta''(rho)|² from the Laurent coefficient 2/(rho zeta''(rho)), retaining the 1/(2 pi) integral normalization and horizontal displacement alpha/2. A window of width proportional to alpha has event size alpha^(-3), whereas the checked pointwise RH reciprocal bound pays alpha^(1-2V). The exponent would oppose a double only for V<2; the large-height parameter grows. This is a failure of that particular localized pointwise payment, not of all signed local correlations.

The coherent theta-tail formulas were checked separately by the phase reviewer and by root. The displayed polynomial for Phi_n'' is positive for n>=2; the all-mode summability is already paid in Note 14. Its twice-integrated cosine transform is strictly positive, but the differentiated kernel takes both signs. At a zero the logarithmic-slope difference equals -F'/T exactly. No extra inequality follows by substituting the event into this identity.

## 4. Bounded contour and reflection attempt

The BW09 boundary form and its endpoint charge still give the multiplicity baseline (m-1)pi. A checked original-source identity, with psi(u)=sum_n exp(u-pi n²exp(4u)), Phi=(psi''-psi)/8 and psi'(0)=-1/2, is

8H(t,x)=1/2+(2t-1-x²)P(t,x)+4t²P_t(t,x)+4txP_x(t,x),

where P is the cosine transform of exp(tu²)psi. Root checked both integrations by parts and the boundary half-unit. At t=0 this says H=-(1+x²)[P-1/(2(1+x²))]/8. A multiple zero is therefore exactly rational first-order contact; the identity supplies no independent contact bound. The positive-time derivative terms remain signed. This failed implication is recorded here without creating another criterion.

The canonical-system assessment already in [Review 08](08_RECIPROCAL_PRECISION_AND_KERNEL_REVIEW_20261020.md) was rechecked against [Suzuki, §1](https://arxiv.org/pdf/1606.05726): strict half-plane comparison and no common real zero are separate premises. A repeated real factor survives in F+iF'. Neither that construction nor the primitive identity yielded a strict winding surplus.

The original source/control preservation lists, all-zero multiplicities, complete arithmetic weights and lack of a pre-zero all-real interval remain explicit. No finite-height certification or all-height exclusion has been obtained, and the BW09 manuscript/registers remain unchanged.
