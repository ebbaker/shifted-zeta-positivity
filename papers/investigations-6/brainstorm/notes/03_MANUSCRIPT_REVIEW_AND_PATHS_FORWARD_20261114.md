# Investigation 6 manuscript review and paths forward

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. This chat's captured model
configurations are empty; the actual backend model and reasoning effort
are unavailable and are not inferred from earlier worker selections.

The four manuscripts provide a coherent representation and approximation
framework for the complete Newman field. The strongest connection between
the branches is the Volterra coefficient bound feeding the Jacobi-chain
remainder. QTT gives an explicit compact-box rank bound, while exact cell
integration removes a fixed lattice's all-height aliasing problem.
Neither a new zero-exclusion estimate nor a computational speed advantage
has been established.

This is a high-level internal manuscript review and discussion note. All
four current TeX sources were read, including their proofs and challenges,
and compared with the existing cross-review, finite acquisition assessment
and control records. The prior disposition remains **“Accepted as
analytical drafts within stated scope.”** No blocking discrepancy was
identified in this reading of the principal arguments. This does not supply
independent specialist review or a fresh replay of the numerical certificate.

Read the [result index](../../../../result-summaries/README.md) and
[avoid index](../../../../avoid/README.md), especially
[cluster 18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[controls 12](../../../../result-summaries/12_collision_controls_and_screening.md),
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[05](../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[20](../../../../avoid/20_volume_without_a_gain.md).

## What each manuscript supplies

All four retain the complete theta source, the physical factor
\(H_\lambda(z)=\frac12\int W_\lambda(u)e^{izu}\,du\),
\(H_0(z)=\xi((1-iz)/2)/8\), and reversed time
\(\tau=1/2-\lambda\). Their approximation norms differ.

| Manuscript | Main result | Interpretation and limit |
| --- | --- | --- |
| [QTT](../../01_qtt_newman_flow/manuscript/main.tex), §§3–5 | A polynomial construction on 72 binary coordinates has bond dimensions at most **641**, with **scaled absolute error below \(2^{-36}\)** for \(0\le\lambda\le1/2\), \(40\le\Re z\le80\), \(\lvert\Im z\rvert\le8\). | A constructive rank/error theorem with exact coefficients and contractions. The scale is \(S(x)=e^{\pi x/8}/(1+x)^{7/4}\). Stable coefficient acquisition, arithmetic costs and growing-height ranks remain open. Integrating the same polynomial directly removes the midpoint error. |
| [Fixed Jacobi chain](../../02_jacobi_chain_height_flow/manuscript/main.tex), §§2–6 | A self-adjoint infinite chain generates height and heat evolution exactly; an \(N\)-site chain has an explicit scalar remainder and sufficient depth \(N=\lceil4K\log(16K)\rceil\), \(K=X+\log(1/\epsilon)+1\). | Uniform real-height absolute error at most \(H_{1/2}(0)\epsilon\) for \(\lvert x\rvert\le X\), \(0\le\tau\le1/2\), \(0<\epsilon\le1\), with exact inputs. The finite scalar is exactly Gaussian quadrature. This is not a bound on the full state's omitted prefix. |
| [Volterra coefficients](../../03_volterra_coefficient_dynamics/manuscript/main.tex), §§3–5 | The moving coefficients obey the Volterra lattice and an entrywise Lax identity. For all \(n\ge0\), \(\beta_n+\beta_{n+1}\le\operatorname{arcosh}^2(2n+12)/16\), uniformly in \(0\le\lambda\le1/2\). | Since \(a_n=\sqrt{\beta_n}\), the squared couplings have a logarithm-squared upper envelope and the couplings have a logarithmic upper envelope. This controls the norm product in the chain error. It is not a sharp asymptotic or a collision separator. |
| [Exact dyadic products](../../04_exact_infinite_tensor_products/manuscript/main.tex), §§3–6 | Exact mass refinement converges in weighted state norm. Integrating phase within each cell gives a sinc factor and **physical absolute error below \(5\times10^{-7}\)** for every real height, \(\lvert\Im z\rvert\le8\), \(0\le\lambda\le1/2\), at \(U=2,L=30\). | An all-height absolute approximation with exact cell masses. The displayed tuple has **\(2^{32}\) formal masses**. Compressed acquisition and contraction are unproved. Source-factor operator-norm convergence is local to bounded intervals; the full-line theorem is weighted state convergence. |

The QTT scale, the Jacobi base-mass scale and the dyadic physical absolute
scale must be kept separate. In particular, the dyadic all-height result
does not preserve relative accuracy as the field becomes small. The QTT
bound is also absolute, even though it uses a useful height-dependent scale.

## The strongest current connection

The Volterra paper's useful quantitative step comes from the complete
source's confinement, rather than the lattice equation alone. Integration
by parts against a squared orthogonal polynomial gives an exact expectation
identity; a lower bound for the logarithmic derivative of the weight and
Jensen's inequality convert that identity into the all-degree envelope.

The Jacobi paper then uses the normalized monic norm
\(h_N^*=h_N(1/2)/h_0(1/2)=\prod_{j=1}^N\beta_j(1/2)\).
It proves

\[
 \frac{|H_{1/2-\tau}(x)-H_N(\tau,x)|}{H_{1/2}(0)}
 \le h_N^*\sum_{k=0}^N
       \frac{\tau^k x^{2N-2k}}{k!(2N-2k)!}.
\]

Thus better information about the norm product has an identified use:
it directly improves a scalar error or sufficient chain depth. The
resulting \(O(K\log K)\) depth is sufficient, not optimal and not a
statement about the work needed to acquire its coefficients.

The [finite acquisition assessment](../../reviews/02_TN6_E03_ACQUISITION_ASSESSMENT_20261114.md)
accepts an actual **16-site** certificate: seventeen complete-source even
moments, sixteen positive couplings, and total normalized absolute error
below **\(1.515\times10^{-25}\)** for the ideal nominal scalar on
\(\lvert x\rvert\le8\), \(0\le\tau\le1/2\). Rounding is additionally certified at
nine evaluated points. The failed 128-bit width gate and successful 256-bit
attempt are both retained. This establishes finite feasibility.

It does not establish speed: the original measured chain setup plus nine
readouts took 1.288 seconds, versus 0.535 seconds for direct integration.
Those figures concern that workload, include the recorded instrumentation,
and achieve different output radii. They neither imply a general speed law
nor exclude an advantage for another workload.

## What the representation results mean

The bond-two single-excitation construction encodes **every** square-summable
coefficient sequence. Its small bond dimension does not bound the number
of amplitudes that must be known. The Jacobi paper proves that every fixed
prefix loses its prepared-state mass at large real height, while the full
norm stays positive; a quantitative rate remains open.

Similarly, QTT's bond-three heat generator does not imply a bond-three
finite-time propagator. The exact sampled Gaussian multiplier has full
unfolding rank at each cut for positive reversed time in the stated bit
ordering. This leaves controlled approximations, alternative representations
and state-specific rank bounds available.

The dyadic paper isolates a useful numerical distinction. A fixed
center-point lattice repeats phases at alias frequencies, producing an
all-real-height error at least \(Z_\lambda/2\) when full-line masses are
used. Exact integration inside each cell supplies the missing sinc factor.
This obstruction is specific to that fixed center-point rule; it is not
an obstruction to finite approximation on compact height intervals or to
other discretizations. Direct integration of the same step density already
has exactly the corrected scalar value.

These distinctions identify where a future estimate must add information:
coefficient acquisition, approximation of the prepared state, or control
of the actual oscillatory observation. Re-expressing the same scalar alone
does not supply any of those estimates.

## Collision-control screen

The catalogued controls were applied as an analytical premise screen; their
existing collision certificates were not rerun. Approximation milestones
are allowed to hold for colliding sources. A proposed collision-exclusion
claim must fail on a domain containing the relevant witness. Failure of a
control to equal theta does not itself show that a derived bound separates it.

| Control | Outcome relevant to these manuscripts |
| --- | --- |
| Euler-factor translates | They lack the unchanged theta summand formula. The [VCD screen](../../03_volterra_coefficient_dynamics/notes/02_VCD_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md) gives an actual envelope failure at \(c=1/2,p=23,\lambda=0\); that test is not extended to every prime. |
| Positive three- and four-square sources | **Pass the same logarithmic envelope and collide.** The positive weights cancel out of each summand score; the even extensions satisfy the integration-by-parts hypotheses. They fail complete equal theta coefficients and full modular reflection. Their [three-square](../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md) and [four-square](../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/03_TWO_ENDPOINT_SQUARE_COLLISION_20261015.md) events are respectively near \((\lambda,x)=(1/4,44.1303)\) and \((1/100,83.5324)\). |
| Reflected super-Gaussian | It lacks the canonical integer-square source. Its polynomially growing logarithmic derivative fails the displayed exponential confinement premise at large source coordinate. This is not a verified failure of its coefficient inequality. |
| Smooth shape and positive-primitive sources | They lack the exact theta arithmetic/summand score. Their satisfaction of the weaker coefficient envelope is untested. Positivity, reflection-like endpoints, decay or a positive primitive therefore cannot be promoted to a separator. The primitive examples retain their sufficiently-small-damping scope. |
| Atomic and finite-profile examples | Atomic examples lack the positive full-line density and its score, but permit an exact terminating chain and a low-rank collision. Compact continuous extensions require their own density hypotheses. |
| Finite-prime perturbations and RH-conditional endpoint examples | The former fail complete canonical reflection; the latter fail ordinary Dirichlet-series arithmetic and retain their RH hypothesis. Finite prime constraints or finite profiles are insufficient as universal separators. |
| Fixed amplitude with altered kernel; actual-profile measure relaxation | The former lacks the literal cosine/Newman observation despite unchanged coefficients. The latter does not represent the required integer zero configuration or physical Fourier field. Neither is a counterexample to the stated literal theta approximations. |

The strongest immediate warning is the weighted-square row: even improving
the present confinement constants need not distinguish theta from a
colliding source. A zero-sensitive application must identify and estimate
additional information that matters to the physical cancellation.

## Three paths for discussion

These are **proposed intermediate milestones**, classified under avoid 01;
none is an RH-equivalent criterion or a proved new mechanism. This review
does not activate an execution task or alter a progress register.

1. **Sharpen recurrence information with the scalar remainder as its use.**
   This is the most direct analytical continuation. Begin by checking
   whether the already proved adjacent-sum constraints improve the norm
   product when retained jointly: the displayed product bound currently
   bounds each factor separately. That may only improve constants, which
   should be reported as such. A more substantial target is individual
   coefficient asymptotics, effective lower bounds and uniform remainders
   that improve a specified high-height depth or precision requirement.
   Success must be measured against the current product/remainder at the
   same height, time range and error scale. Weighted-square controls may
   also satisfy an improvement; no sign inference follows automatically.

2. **Quantify propagation of the prepared Jacobi state.**
   The exact dynamics is available, but the rate of escape along the
   chain is missing. A bounded next question is to estimate
   \(\sup_{0\le\tau\le1/2,\lvert x\rvert\le X}\sum_{n\ge N}|v_n(\tau,x)|^2\)
   with an explicit useful dependence on \(N,X\). This would address the
   physical meaning of height transport and the required number of
   one-excitation amplitudes. It must distinguish projection of the true
   state from evolution with a truncated generator, paying boundary
   effects if the latter is used. It is a state-approximation milestone;
   low rank and generic propagation bounds remain compatible with collisions.

3. **Combine compression with exact phase integration.**
   The QTT polynomial construction and the dyadic sinc readout suggest
   asking whether cell masses or a piecewise-polynomial source can be
   represented compactly while integrating the oscillatory phase exactly.
   The target is a proved rank/error/acquisition bound that avoids the
   current billions of formal masses, or improves a specified growing-height
   allowance. No such combined bound is claimed here. Its comparison must
   be direct integration of the identical approximate density; the source
   error and cancellation scale still have to be paid. The fixed lattice
   obstruction does not apply to this exact-phase alternative.

My preference is the first path, with the second as the clearest route
back to the original height-transport question. The third is an analytical
compression question with a natural computational use. If the immediate
priority is zero exclusion, the missing first step is a concrete
source-sensitive estimate that a known colliding control fails. No ready
estimate of that kind emerges from the four manuscripts alone; this is a
statement about these results, not an exclusion of future coefficient or
tensor methods.

## Review and session record

The [existing cross-review](../../reviews/03_TN6_ANALYTICAL_MANUSCRIPT_CROSS_REVIEW_20261114.md)
and [analytical continuation](../../notes/10_ANALYTICAL_MANUSCRIPTS_CONTINUATION_AND_MODEL_HANDOFF_20261114.md)
remain the status and continuation sources. Classical background was
spot-checked against [DLMF §3.5](https://dlmf.nist.gov/3.5#vi) for the Jacobi
matrix/Gauss-rule correspondence and [Lindsey, Proposition 13](https://arxiv.org/html/2311.12554v3#S4.SS1)
for polynomial-exact QTT interpolation. The
[Van Assche survey](https://arxiv.org/abs/2202.11017v1) and its existing
[passage record](../../03_volterra_coefficient_dynamics/references/01_VCD_MANUSCRIPT_SOURCE_PASSAGES_20261114.md)
identify the classical lattice background. These references already have
repository catalogs; no new literature-priority claim is made.

The shared chat **Review investigations-6 manuscripts**, thread
`01a1daa9-a0cf-7811-b81b-166b83d6bc9e`, is registered as
[chat 0003](../../chat-histories/0003_2026-11-14T15-25-12Z_review-investigations-6-manuscripts.json).
The recorder initially rejected a newly present `moderation: null` field.
Its adapter now accepts only that observed empty value; populated values
and unfamiliar fields remain rejected. The 90 recorder/adapter tests passed,
and exact-source registration succeeded. Counts, hashes and capture times
belong to the [live registry](../../chat-histories/index.json).
The final reply requires the usual bounded exact-turn follow-up; no native
completion-hook activation is asserted. The small
[review record](../../numerics/19_TN6_MANUSCRIPT_REVIEW_RECORD_20261114.json)
identifies the reviewed manuscripts and verification scope.
