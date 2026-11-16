# B05 — complete-source Fourier estimates and their zero consumer

16 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance. Lead actual model and effort unavailable in accessible runtime/archive configurations. Fixed proof and assessment helpers explicitly dispatched **gpt-6.1-sol / ultra**; no separate backend attestation. Chat0003, second research turn.

**Research synthesis; [E20 accepted the three proofs and this synthesis within their stated scopes](../reviews/07_VCD_E20_CANONICAL_FOURIER_ASSESSMENT_20261116.md).** Separate internal shared-model/shared-premise assessment, not independent specialist review. No mathematical correction was required; this editorial status sentence is the only post-assessment change. B05 follows the [midpoint synthesis15](15_VCD_MIDPOINT_RESEARCH_SYNTHESIS_20261116.md) through [decision10](../brainstorm/notes/10_VCD_B05_CANONICAL_FOURIER_SCORE_DECISION_20261116.md) and [decision11](../brainstorm/notes/11_VCD_B05_CANONICAL_CONSUMER_TEST_DECISION_20261116.md). It obtains a quantitative estimate using the complete canonical source, compares it with an explicit sufficient zero test, and tests that consumer on the actual source. No Fourier-zero confinement theorem or induction is proved.

Read the [result index](../../../../result-summaries/README.md), [cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [control catalog12](../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../avoid/README.md), [classification01](../../../../avoid/01_restating_the_target.md), [scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [separate-bounds12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The estimates below are intermediate quantitative results. The pointwise comparison is a sufficient condition with an actual lower-modulus consumer; its proposed all-height use is disproved within the specified class. The earlier unspecified shrinking-strip target remains classified once in overview02; no sample checks support it.

## 1. Complete source and exact shifted comparison

All statements below are at \(\lambda=0\). Retain the unchanged source, probability normalization and literal Fourier readout:
\[
 Z=\int_{\mathbb R}\Phi(u)\,du,\qquad
 F(z)=\frac1Z\int_{\mathbb R}\Phi(u)e^{izu}\,du
     =\frac{\xi((1-iz)/2)}{4Z}.
\]
The [E06](06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md) decomposition is
\[
 -\Phi'/\Phi=8\pi\sinh(4u)+b(u),\qquad
 B(z)=\frac1Z\int_{\mathbb R}b(u)\Phi(u)e^{izu}\,du.
\]
For \(z=x+iy\), put \(F_\pm=F(z\pm4i)\). [E18 / Note17](17_VCD_E18_EXTERIOR_ANCHOR_COMPARISON_20261116.md) proves
\[
 4\pi(F_--F_+)+B(z)=izF(z).                                      \tag{1}
\]
For fixed \(0<y<1\), both shifted fields are nonzero and
\[
 |F_+|\asymp_y e^{-\pi x/8}x^{(11+y)/4},\qquad
 R=F_-/F_+=O_y(x^{-y/2}) \quad(x\to+\infty).
\]
Constants and onset can be chosen uniformly on every compact subinterval of \(0<y<1\), not down to \(y=0\). Define
\[
 \Delta=4\pi(|F_+|-|F_-|)>0
\]
for sufficiently large \(x\). Equation (1) supplies the concrete pointwise consumer
\[
 |F(z)|\ge\frac{\Delta-|B(z)|}{|z|}.
                                                               \tag{2}
\]
Thus \(|B|<\Delta\) would exclude a zero at that point. Positivity or complete-source membership alone does not establish this comparison.

## 2. Fourier-scale bound retaining all canonical modes

[E17 / Note16](16_VCD_E17_CANONICAL_REMAINDER_CONTOUR_BOUND_20261116.md) works with
\(g=b\Phi=-\Phi'-8\pi\sinh(4u)\Phi\), which is holomorphic in \(|\Im u|<\pi/8\). It never presumes that the quotient \(b\) is holomorphic there. The exact first-mode cubic cancels before the complete mode sum is bounded. For the explicitly defined positive allowance \(A_Y\) in Note16 equation (4),
\[
 |B(x+iy)|\le e^{-v|x|}A_Y(\cos4v),\quad |y|\le Y,
 \quad 0\le v<\pi/8,
\]
and for each fixed \(0\le Y<1\),
\[
 A_Y(\delta)\sim\frac{15}{Z(1-Y)}\delta^{-7/2},
\]
\[
 \inf_{0\le v<\pi/8}e^{-v x}A_Y(\cos4v)
 \sim\frac{15}{Z(1-Y)}\left(\frac{ex}{14}\right)^{7/2}e^{-\pi x/8}.
                                                               \tag{3}
\]
This is the precise asymptotic of the displayed termwise absolute allowance after optimizing the horizontal shift. It is not a lower bound on \(|B|\), on the unsplit contour integral, or on every possible estimate. The asymptotic is not uniform as \(Y\uparrow1\).

The [E18 return addendum](../research-progress/handoffs/VCD-E18-r1-return.md) pins E17 and completes the comparison: for fixed \(0<y\le Y<1\), the allowance (3) divided by \(\Delta\) is comparable to \(x^{(3-y)/4}\), hence diverges. The expected exponential decay has been obtained; this particular polynomial loss defeats (2).

## 3. Arithmetic improvement and the exact consumer obstruction

Let \(s=(1-iz)/2=\sigma-ix/2\), \(\sigma=(1+y)/2\). Here \(s\) is the completed-zeta argument, not the Laplace variable of the chain-memory notes. E18 derives the exact identity
\[
 U(z):=\frac{B(z)}{4\pi F_+}
 =1-R-D(s)Q(s),\qquad
 D(s)=\frac{(2s-1)(s-1)}{2(s+2)(s+1)},\qquad
 Q(s)=\frac{\zeta(s)}{\zeta(s+2)}.                              \tag{4}
\]
The denominator is nonzero by the exterior Euler product. In \(\Re s>1\), the quotient has coefficients
\[
 a_n=\prod_{p\mid n}(1-p^{-2})=\sum_{d\mid n}\frac{\mu(d)}{d^2}.
\]
These \(a_n\) are arithmetic Dirichlet coefficients, not the Jacobi links bearing the same letter in earlier notes. Their absolute series diverges for \(\Re s\le1\); the quotient itself is regular on \(1/2<\Re s<1\).

[E19 / Note18](18_VCD_E19_CANONICAL_CONSUMER_OBSTRUCTION_20261116.md) derives
\(\sum_{n\le u}a_n=u/\zeta(3)+O(1)\) and uses partial summation to give the coarse pointwise bound
\[
 Q(\sigma+it)=O_\sigma(t^{1-\sigma}),\qquad t\ge2,\quad 1/2<\sigma<1.
                                                               \tag{5}
\]
Combining (4), (5) and the anchor scale gives the further quantitative corollary
\[
 \boxed{|B(x+iy)|=O_y\!\left(e^{-\pi x/8}x^{(13-y)/4}\right)},
 \qquad x\to+\infty,quad 0<y<1\text{ fixed}.                 \tag{6}
\]
Indeed \(|U|=O_y(x^{1-\sigma})\), and
\((11+y)/4+1-\sigma=(13-y)/4\). This improves the power \(7/2\) of (3) at each such line, using the exact arithmetic representation. It remains an absolute upper estimate; relative to \(\Delta\) its upper allowance is of order \(x^{(1-y)/2}\), not a proved small quantity. No claim of optimality or novelty is made for this elementary zeta estimate.

The consumer can be tested more decisively. E19 extracts every fixed rational-frequency vertical mean of \(Q\) by a finite Dirichlet sum with cutoff \(\lfloor T^2\rfloor\), whose mean error is \(O_{q,\sigma}(T^{1-2\sigma}\log T)\). For each fixed finite prime prefix \(P\), the nonnegative weight
\[
 W_P(t)=\prod_{p\in P}(1+\cos(t\log p-\pi/3))
\]
has mean one and its \(Q\)-weighted mean is
\[
 \prod_{p\in P}\left(1+\frac{(1-p^{-2})e^{-i\pi/3}}{2p^\sigma}\right).
\]
As the prime prefix grows, this product has unbounded modulus and a winding phase with step size tending to zero. For every fixed real projection, it has arbitrarily large positive and negative real parts. Nonnegativity of each fixed weight transfers this to actual values of \(Q\) on every height tail. The order of limits is fixed \(P\), then \(T\to\infty\); no uniform growing-prefix estimate or effective height is asserted.

Since \((D-1)Q=O_y(x^{-\sigma})\to0\) and \(R\to0\), conjugation and (4) imply
\[
 \limsup_{x\to\infty}\Re(e^{-i\theta}U(x+iy))=+\infty,
 \qquad
 \liminf_{x\to\infty}\Re(e^{-i\theta}U(x+iy))=-\infty          \tag{7}
\]
for every fixed \(\theta\in\mathbb R\), \(0<y<1\). In particular,
\[
 \boxed{\displaystyle
 \limsup_{x\to\infty}\frac{|B(x+iy)|}
 {4\pi(|F(x+iy+4i)|-|F(x+iy-4i)|)}=+\infty.}                 \tag{8}
\]
**The uniform-in-height reverse-triangle comparison fails for the exact canonical source itself.** Improving an upper bound cannot make that global comparison true. Every fixed half-plane trap for this normalization also fails. This is stronger than the failure of allowance (3), and has a different proof.

## 4. What the result does and does not settle

The failed classes are (i) the displayed termwise-absolute horizontal-contour allowance as a payment for (2); (ii) an eventual all-height bound \(|B|<\Delta\) on a fixed interior line; and (iii) a fixed half-plane bound on \(U\) or \(DQ\). Equations (7)–(8) do not prove nonreal Fourier zeros. Large values and unbounded real projections are not zeros, nor do they show that the particular value \(1-R\), required at a zero of \(F\), is ever attained.

A pointwise test on selected regions, a height-dependent phase chosen from independently controlled data, a nonlinear correlation, and a degree-dependent compact argument remain outside these exclusions. The exact identity alone does not supply one of those mechanisms. A phase defined using the unknown nonzero field would only hide the original target.

The actual controls are screened in Note16 §5 and Note17 §4. The complete integer-square expansion, analytic reflection and literal completed-zeta readout fail in the appropriate perturbed families. E10/E12 smooth compact multipliers retain real tails and finite canonical tests, but their own score product has a nonzero compact correction and cannot have the required holomorphic strip continuation. E07's nonreal-zero class still loses higher smooth reflection. No new nonreal-zero conclusion is assigned to the smooth controls. For (8), no perturbed control is needed: the intended complete source itself defeats the proposed comparison.

## 5. Disposition and remaining research input

B05 has pursued its complete-source mechanism through two formulations and a dependent exact-source test. It has obtained the Fourier-scale estimate (3), the exterior lower scale and pointwise consumer (2), the improved source estimate (6), and the scoped actual-source obstruction (8). It has not obtained a signed canonical tail estimate that controls zeros, a stable degree update, or a terminal condition.

The next conceptual task is to select a different signed consumer for the exact E15 kernel-defect transport. A candidate must specify which complete-source correlation survives its approximation, how that correlation is acquired without evaluating the unknown full Fourier response, and the actual contour or degree-step margin it pays. At most two concrete mechanisms per pass; do not reissue the disproved all-height disk/half-plane comparison or merely tighten its upper envelope. If no such quantitative premise can be derived, record the mathematical gap rather than asserting a zero result from source identification.

The [live register02](../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md) owns statuses. The [continuation03](03_VCD_TAIL_CLOSURE_INDUCTION_CONTINUATION_20261116.md) owns the next handoff. All source readings and external-copy limitations are in [reference record03](../references/03_CANONICAL_SCORE_FOURIER_PASSAGES_20261116.md). No numerical or coefficient campaign, manuscript revision, or external publication was performed.
