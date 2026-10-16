# Endpoint matter: continuation of the Wilson-line investigation

18 September 2026. Written by OpenAI GPT-6 (Codex) for Edward Baker.

**Status.** Active research continuation of manuscript 0.8, not an amendment to its archived text. The baseline is saved at `drafts/2026-09-18-v08-endpoint-baseline/`. Read this note and [the follow-through calculation](ENDPOINT_TRANSPORT_AND_SHIFT_20260918.md) before the older continuation prompts. No realization of the full Weil form, contraction theorem, or RH claim is made.

## 1. Why this question is open

The proposal is to construct the shifted transfer through an actual open Wilson line with endpoint matter. Three prior results constrain that proposal without excluding it:

- Scalar causal convolutions commute after interval compression. A realization must reproduce this scalar sector; its underlying gauge theory need not be abelian.
- The connection defined from a single-valued transfer is flat by construction. This is not vanishing of spacetime field strength. Loewner Section 4.1 already corrects the earlier interpretation: the physical field-strength insertion would enter the deformation coefficient, not the curvature of the reconstructed parameter-space connection.
- A convergent positive radial spectral correlator has a Stieltjes transform and cannot be directly identified with the winding transfer. A derived scattering response is a different object. It requires its own construction and positivity argument.

The fractional-dimension result excludes the positive point-count interpretation of the prescribed continuation `theta^m` for `1<m<2`. It does not exclude continuously varying boundary or spectral parameters in a fixed-dimensional field theory. The archimedean calculation in the next note makes that distinction explicit.

The scalar transfer's contraction criterion retains its full arithmetic difficulty. None of these qualifications weakens the need to derive the prime contribution and the positive pairing independently.

## 2. The actual endpoint sector

The candidate is the N=4 bulk theory coupled to a three-dimensional fundamental defect hypermultiplet, with scalar endpoints joined by supersymmetric semicircles. The construction and leading endpoint propagator are in Baker, [arXiv:1102.4948](https://arxiv.org/pdf/1102.4948), Sections 3.1–3.2, especially equations (30)–(31). The propagator is proportional to `1/|x-y|`. This differs from the dimension-one protected scalar insertion on the ordinary half-BPS line used in the earlier delay test. No all-order protection of the endpoint weight is inferred.

Choose a coordinate along a straight line **within the defect** and points `+r` and `-r`, with `r>0`. This is a proposed coordinate dictionary, not the original paper's normal ray into the bulk. Put `u=log(r1/r2)>0`. After removing the leading normalization and multiplying by `sqrt(r1 r2)`, the free scalar kernels are

\[
 G_s(u)=\frac1{2\sinh(u/2)},\qquad
 G_o(u)=\frac1{2\cosh(u/2)}.
\]

The subscripts denote endpoints on the same and opposite rays of the defect coordinate. Their even average is

\[
 G_+(u)=\frac{G_s(u)+G_o(u)}2
       =\frac{e^{-u/2}}{1-e^{-2u}}
       =\sum_{n\ge0}e^{-(2n+1/2)u}=n_\gamma(u).
 \tag{2.1}
\]

The odd average is `G_-(u)=e^(-3u/2)/(1-e^(-2u))`. Thus parity gives the quarter and three-quarter towers without rescaling `u`. Equation (2.1) is an exact elementary identity. The positive tower is already known in this program; the proposed endpoint interpretation is what is being tested.

For a free scalar, the field combination `[q(r)+q(-r)]/2` has the even-average covariance. The factor `1/2` here gives the chosen kernel normalization. In the interacting gauge theory this sum is not gauge covariant: the two terms transform at different points. It must be replaced by a specified network of transports. Section 3 makes one gauge-invariant candidate explicit and the follow-through note explains why it is not yet a Gram kernel.

### The difference energy

Writing `a_n=2n+1/2`, the exact integral identity is

\[
 2\int_0^\infty(1-\cos\tau u)n_\gamma(u)\,du
 =2\sum_{n\ge0}\frac{\tau^2}{a_n(a_n^2+\tau^2)}
 =\Re\psi(\tfrac14+\tfrac{i\tau}2)-\psi(\tfrac14).
 \tag{2.2}
\]

The integrand is integrable at zero because the difference factor is quadratic. Termwise integration follows from nonnegativity; the last equality follows from the convergent digamma difference series. This recovers the central archimedean multiplier `b(tau^2)`. It does not recover the contact `w0`, the pole form, or the negative prime terms.

## 3. A gauge-invariant candidate, and the limits of the perturbative evidence

For real defect coordinates `x<y`, let `C_{x,y}` be the semicircle in the upper bulk half-plane with diameter `[x,y]`, consistently oriented from the right endpoint to the left. Fix the scalar coupling as in the original semicircle operator. Denote the resulting gauge-invariant endpoint bilinear by `O(x,y)`; the transporter maps the color space at `y` to that at `x` and is contracted with the appropriate fundamental and antifundamental endpoint fields. The R-symmetry polarizations must also be those of the operator, not arbitrary scalar insertions.

For `r1>r2>0`, define

\[
 \mathcal E_+(r_1,r_2)
 =\frac{\sqrt{r_1r_2}}2
   \big[\mathcal O(r_2,r_1)+\mathcal O(-r_2,r_1)\big].
 \tag{3.1}
\]

Each summand is a gauge-invariant open-line operator. Its leading expectation reproduces (2.1), up to the known scalar propagator normalization. This constructs the **pairwise observable**, not a positive two-variable Hilbert-space kernel or a family with one common supercharge. Those distinctions are substantive.

Equation (58) of the source reports a first correction multiplying the semicircle expectation by a distance-independent factor in its stated self-energy normalization. Applied to the two summands with that same normalization, it would preserve (2.1) through the displayed order. This is an inherited perturbative reading, not a newly computed loop correction, and there is a renormalization qualification that must be resolved before using it as protection of the kernel.

### A local renormalization qualification

The radial self-energy integral appearing before the source's final normalization has, up to its overall sign and prefactor, the elementary dependence

\[
 J(p,\Lambda)=\int_0^\Lambda
 \log\frac{(q+p)^2}{(q-p)^2}\,dq
 =2p\big[(R+1)\log(R+1)-(R-1)\log|R-1|\big],
 \quad R=\Lambda/p>1.
 \tag{3.2}
\]

The singularity at `q=p` is integrable. Expansion gives

\[
 J(p,\Lambda)=4p[\log(\Lambda/p)+1]+O(p^3/\Lambda^2).
 \tag{3.3}
\]

A momentum-independent local wavefunction counterterm subtracts a logarithm at a fixed scale `mu`; it cannot remove `log(p/mu)` for every momentum. Hence normalizing the propagator at one scale is not by itself a proof that the endpoint kernel keeps its power at all separations. The full gauge-invariant observable may have compensating endpoint or vertex contributions. This note does not calculate their cancellation and does not infer an anomalous dimension from the gauge-dependent propagator alone. The requested next loop calculation is therefore the **full observable in one specified local scheme**, not importing the normalization of a single diagram as an all-scale theorem.

### What a change of weight would do

For a conformal weight `Delta>0`, the same free-form image average is

\[
 G_{+,\Delta}(u)=\tfrac12\big[(2\sinh(u/2))^{-2\Delta}
                      +(2\cosh(u/2))^{-2\Delta}\big]
 =e^{-\Delta u}\sum_{n\ge0}\frac{(2\Delta)_{2n}}{(2n)!}e^{-2nu}.
 \tag{3.4}
\]

At `Delta=1/2+delta`, its first variation is

\[
 G_{+,\Delta}(u)=\sum_{n\ge0}e^{-(2n+1/2)u}
    [1+\delta(2H_{2n}-u)]+O(\delta^2),\quad H_0=0.
 \tag{3.5}
\]

For fixed positive `u` this follows by differentiating a convergent series. The `n`-dependent harmonic numbers show that an anomalous weight changes more than an overall normalization. This is a concrete diagnostic for the interaction calculation.

## 4. Repairing the scope of the earlier delay test

The one-sided beta integral for `[2 sinh(u/2)]^(-2 Delta)` converges at zero only for `Delta<1/2`. At the half-integer protected weights used in the old zero-delay claim, the factor `Gamma(1-2 Delta)` is singular. Analytically continuing a phase derivative and then setting the weight to a pole does not define a renormalized correlator.

For `Delta=1/2`, a finite difference is unambiguous:

\[
 \int_0^\infty(e^{-pu}-e^{-qu})G_s(u)\,du
   =\psi(q+\tfrac12)-\psi(p+\tfrac12),
 \tag{4.1}
\]

for `Re p, Re q>-1/2`. Its phase is generically not constant. Higher weights need more subtractions and local terms. The protected zero-delay claim consequently needs a specified subtraction prescription; the old finite checks of its analytically continued trigonometric formula do not establish that physical claim. The convergent Stieltjes no-winding result remains intact within its hypotheses. Equation (4.1) is not the target scattering amplitude.

## 5. Results, remaining questions, and checks

**Established here:** the exact image identity (2.1), multiplier (2.2), cutoff logarithm (3.2)–(3.3), weight variation (3.4)–(3.5), and subtracted transform (4.1). A gauge-invariant pairwise candidate has been specified, with its leading kernel.

**Continued in the next note:** its common-supercharge test, the distinction between pairwise transports and a Gram construction, and an exact determinant realization of the shifted archimedean factor on a fixed even tower.

**Not established:** endpoint protection in a common local renormalization scheme; a common physical supercharge for the full kernel; a positive gauge-theory Gram representation; the arithmetic terms; a physical interpretation of the determinant's shift; positivity of the full Weil form.

The standard-library [check program](../numerics/check_endpoint_matter.py) tests the identities independently by rational identities, direct quadrature, finite series and finite Clifford algebra. The continuation has its own [registry and hash-bound replay](../validation/endpoint_matter.py), with provenance in `ENDPOINT_MATTER_RECORD.json`. This keeps the unchanged manuscript 0.8 build record truthful; its original `validation/drafts.py` registry is not repurposed to imply these results are already in that manuscript. On eventual manuscript integration, migrate this check into that registry and rebuild/review the PDF.

**Baseline verification.** The manuscript/PDF and all nine snapshots pass the original identity check. All 1067 old numerical cases pass their programmed tolerances, but the original strict replay differs in floating-point diagnostics on this runtime. Those records were preserved, not silently replaced. See `numerics/records/endpoint-baseline-replay-audit.json` for the exact differences and runtime.

Sources: [Baker, arXiv:1102.4948](https://arxiv.org/pdf/1102.4948), the [Wilson-lines target](../sections/02_conventions.tex), [delay section](../sections/11_delay.tex), [Loewner Section 4](../../loewner/sections/04_realizations.tex), and [fractional-dimension point-count proof](../../fractional-dimension/sections/06_pointcount.tex). Source-derived physics statements above are distinguished from the new algebraic derivations.
