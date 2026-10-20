# Strip kernels, gap replacement and exact theta-mode cancellation: review

20 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
**gpt-6-astra (Codex), reasoning effort ultra**, verified turn metadata.
Separate same-model delegated checks and root integration review; no
specialist review, cross-model review or novelty claim.

**Verdict.** The extensions in [Note 11 §7](../notes/11_FULL_ABSOLUTE_PRIME_ENVELOPE_AND_LOGARITHMIC_SPREAD_20261020.md) and [Note 13 §6](../notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md), and the original-source estimate in [Note 14](../notes/14_EXACT_THETA_MODE_GRAM_CANCELLATION_20261020.md), pass within their stated hypotheses. They sharpen the boundaries of specific estimating routes. They do not supply the opposing signed arithmetic estimate required by RHS-02, a strict cap surplus, or an original multiple-zero exclusion.

The [result index](../../../../../../../result-summaries/README.md), [controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md) apply, particularly [scope](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [complete payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [gain before expansion](../../../../../../../avoid/20_volume_without_a_gain.md).

## 1. Strip-analytic extension and signed-route assessment

### Strip extension: pass

Reviewed [Note 11 §7](../notes/11_FULL_ABSOLUTE_PRIME_ENVELOPE_AND_LOGARITHMIC_SPREAD_20261020.md) against installed Note 11 and the primary [Goldston–Gonek Lemma 1](https://arxiv.org/pdf/math/0511092), p. 3. No mathematical defect found.

- Choosing an individual closed substrip of width `b>1/2` makes contour shifting valid with vanishing vertical edges. The exponential Fourier decay makes the complete prime payment absolutely convergent because `1/2+b>1`. The primary lemma explicitly permits this strip-analytic domain and real-axis decay faster than `|x|^{-1}`.
- For every finite upper cutoff `T`, the existing explicit-formula/Gram proof retains a uniform bound on the damped cutoff and its second derivative. Its constants do not involve the Fourier-decay constant or strip margin. The arithmetic sum is finite before averaging, and the full logarithmic pair moment pays the zero-sum interchange.
- The integrals over `[A,T]` increase with `T`; thus the passage to the complete half-line uses monotone convergence of those nonnegative integrals, regardless of whether the auxiliary smooth cutoffs themselves are monotone in `T`. Weighted Cauchy–Schwarz gives the same full Fourier-tail bound.
- Exponential Fourier decay and quadratic spatial decay justify pointwise Poisson summation. The harmonic-overlap argument and mass–moment inequality survive without an upper support endpoint. The old support-based auxiliary statement `I Delta>=1` is unnecessary here. The existing complete gamma and pole budgets then give the same sharp leading `1/2` floor; Fejer remains an admissible attaining family.

This is an extension of the declared absolute-payment class, not a signed arithmetic estimate or a multiplicity exclusion. No uniform strip margin is needed for the universal estimating constants, although each kernel separately needs the stated margin for its complete explicit formula.

### Exact event-conditioned Riemann–Siegel attempt: no new estimate

Keeping the exact paired half-function and both event equations did not give an opposing signed bound. Multiplying by a finite mollifier `M` yields the exact first-jet transformation

`(zeta M, (zeta M)') = (M zeta, M zeta' + M' zeta)`.

At a putative double zero both components vanish. Where `M` is nonzero this transformation is invertible; where it vanishes it loses information. This observation is only an assessment of the attempted scalar pointwise multiplication, not an exclusion of correlated mollifier methods. No improved conditional remainder or lower bound for the deflated coefficient was proved. The exact Riemann–Siegel half-function phase calculation likewise leaves an uncontrolled derivative at the event; another criterion is not warranted.

I also checked the primary September 2026 paper [Lamzouri, arXiv:2609.02882v2](https://arxiv.org/html/2609.02882v2). Its Lemma 3.1 estimates a full-window pair sum with additive error `O_f(T sqrt(log T))`. For the normalized squared kernel `K(0)=1` of Lemma 3.2, a single double zero contributes diagonal excess `m^2-m=2`; for an arbitrary Lemma 3.1 test the excess is `2 fhat(0)`. The displayed error is far above the normalized scale. The theorem does not provide a uniform shrinking-window estimate. Its density conclusion therefore supplies no one-event estimate beyond the existing Note 06 resolution requirement. This is not a lower bound on every possible localization method and does not warrant another research note solely updating a proportion.

## 2. Second independent strip check

**Verdict: pass.** The extension removes finite Fourier support while retaining the exact absolute-prime, gamma, and pole requirements. The universal constants in the tail and joint-cost inequalities do not require a uniform strip-width margin across a sequence.

1. **Admissibility and complete formula.** For each individual kernel choose `1/2<b<a_h`. The horizontal contour shift has vanishing vertical edges by (X1), and proves (X2). Thus `phi` is integrable and the full prime-power payment converges absolutely, by comparison with `sum Lambda(n)n^(-1/2-b)`. Real quadratic decay makes the logarithmic pair moment finite. [Goldston--Gonek, Lemma 1](https://arxiv.org/pdf/math/0511092), PDF page 3, explicitly allows a strip wider than `1/2` with integrable polynomial decay, and does not require evenness or compact Fourier support. Its subsequent comment distinguishes these hypotheses from the narrower compact-support version in its cited reference. The declared contract meets the lemma by choosing an interior closed strip.

2. **Uniform tail and all-zero Fubini.** The independent finite upper cutoff `T` gives `||J_T||_1+||J_T''||_1 << exp(-A/4)` uniformly for `T>=A`. Neither the strip width nor the pointwise Fourier constant enters this estimate. The full zero sum, including all multiplicities, has the same absolute bound against `log(2+|x-y|)`; the finite pair moment therefore justifies its exchange with the probability-pair integral. The positive prime-power Gram sum is bounded by the full `C` using `|S|^2<=|S|`; Fourier support is unnecessary. Restriction to `[A,T]` gives (X3). These restricted nonnegative integrals increase with `T`, so monotone convergence followed by weighted Cauchy--Schwarz proves the complete half-line tail bound. No monotonicity of the cutoff profiles themselves is required.

3. **Poisson and the joint cost.** The spatial periodization converges uniformly by real quadratic decay. Its Fourier coefficients follow by absolute Fubini, and (X2) gives an absolutely convergent Fourier series for every positive period parameter, uniformly on compact parameter intervals. The pointwise Poisson identity is therefore justified. Positivity and Tonelli permit the same harmonic-overlap and integration arguments. The joint lower bound uses the pointwise Poisson inequality directly; no remnant of `I Delta>=1` or a finite bandwidth is needed.

4. **Leading conclusion and scope.** The gamma budget still bounds the pair logarithmic moment, and the exact pole payment remains a separate hypothesis. The prior optimization then yields the same one-half leading complete-envelope floor, attained by the existing centered Fejer sequence. The strip-dependent constants above establish convergence only and disappear before this universal argument. As before, a uniform infimum statement requires uniformly satisfied gamma and pole budgets. This extension does not cover real-sign-changing kernels, a strip reaching only the boundary `1/2`, unbudgeted pole cancellation, or a separately estimated signed prime term. The central-gap companion theorem does not automatically transfer either budget. The source/test-kernel and unchanged-prime-weight distinctions are preserved.

No mathematical correction is requested.

## 3. Original theta-mode Gram check

**Disposition: pass.** The estimate is for the unchanged theta source at every sufficiently large real height, without RH. It limits the specified diagonal-margin or robust independent-error argument; it does not exclude a multiple zero.

1. **Full remainder summability.** The recurrence `P_(r+1)=(1−4s)P_r+4sP_r′` and substitution `s=πn² exp(4u)` give the stated endpoint and half-line norm bounds. For each fixed derivative order and fixed power of `u`, these are a polynomial in `πn²` times `exp(−πn²)`, hence summable. In particular `g_n^(5)=u Phi_n^(5)+5 Phi_n^(4)` and `g_n^(4)(0)=4 Phi_n'''(0)` make the asserted summability of `C_n` explicit. This pays every integration-by-parts remainder and permits the full diagonal and off-diagonal sums.

2. **Exact signs and derivative handling.** Four integrations by parts give (T6) with both displayed remainder terms positive. A separate sine-transform calculation for `g_n=u Phi_n` gives (T7), including `2 A_n/a³` and the negative fifth-order remainder. No derivative of a big-O estimate is used. The summable error majorants yield `D(a)=c_theta/a⁴+O(a^−6)` by direct multiplication.

3. **Strictly positive diagonal coefficient.** `A_n=exp(−Y_n)(−8Y_n³+30Y_n²−15Y_n)` is correct. The n=2 term is strictly negative because `Y_2=4π>12`; hence the convergent square sum `c_theta` is positive. Complete-source evenness gives `sum A_n=0` without forcing the square sum to vanish.

4. **Completion and exponential scale.** Independently checked [DLMF 25.2.8](https://dlmf.nist.gov/25.2.E8), [25.4.4](https://dlmf.nist.gov/25.4.E4), and [5.11.9](https://dlmf.nist.gov/5.11.E9). On the fixed complex disk, the Euler remainder gives `zeta(s)≪a^(1−sigma)` uniformly for `1/4≤sigma≤3/4`. The completion has size at most `a^(5/2−sigma/2) exp(−πa/8)`, so the coarser bound in (T11) is valid. Cauchy on that disk controls `F′` with no logarithmic or derivative-remainder omission. Thus `J≪a⁵ exp(−πa/4)`, and division by the positive asymptotic diagonal gives `J/D≪a⁹ exp(−πa/4)`. With `a=2 gamma`, the exponential is correctly `exp(−π gamma/2)`.

5. **Scope and final wording.** The ratio bound holds at every sufficiently large real `a`, not merely at a hypothetical event. At an order-at-least-two real zero, `J=0` and `X=−D` are compatible with all estimates. The final robust-error formulation is precise: a margin `X≥−(1−eta)D` has `eta≤J/D`, and robustness against every additive perturbation of magnitude at most `eta D` requires `eta<J/D`. The text correctly exempts favorable one-sided enclosures and does not assert an algorithm-independent complexity lower bound.

No remaining mathematical correction was found. The result supplies a quantitative cancellation cost in the stated information class, not the missing event-conditioned signed lower bound.

## 4. General gap replacement and integration check

Root rechecked the finite-cutoff limiting proof, absolute Poisson justification, normalized zero-moving factors on both sides of zero, Fourier division equation, all-mode endpoint expansion, and the a=2 gamma exponential normalization. A compact gap contains only finitely many odd real zeros; even zeros inside a negative sign interval do not change its pairing. The strip and gap extensions retain their different hypotheses. In particular, replacing a signed kernel does not transfer its arithmetic or completion budgets.

For the separately authored gap extension, root checked that every normalized factor is at most one on the exterior of the central gap, cancels one inner endpoint zero, and adds one outer endpoint zero. The resulting endpoint multiplicities are even. In the Fourier division formula, the integrating-factor sign is negative as displayed, and the integral above the original support vanishes by h(a)=0. Applying the same reasoning to the inverse moves proves equality of minimal symmetric bandwidth, without preserving internal Fourier gaps. Finite rational multipliers preserve the stated strip decay after removable singularities are filled. These checks establish the asserted zero-sum order with all noncentral multiplicities retained; they do not establish an order of the completed arithmetic envelopes.

The theta-mode calculation uses the unchanged source and holds without RH at all sufficiently large heights. It is a failure of the specified relative diagonal estimate, not evidence for a multiple theta zero or a lower bound on every coherent signed calculation. The original controls retain their separate arithmetic, reflection and tail failures; none receives the original source's data by substitution.

The exact event-conditioned scalar mollifier attempt and the checked density theorem yielded no new one-event estimate. They are recorded only as bounded assessments here; no further criterion or research note was created for them. No new numerical campaign was justified. The existing exact-rational fixtures and BW09 manuscript/registers are unchanged and were not rerun as evidence for these new analytic statements.

Research notes, indexes, overview and progress are updated together. No manuscript snapshot was created. The original all-zero goal remains open.
