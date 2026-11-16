# TN6-E04 r1 — Cross-manuscript analytical review

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Recorded review dispatch was
**GPT-6.1 Sol / Ultra**. Independent attestation of the backend and runtime
effort is unavailable. The review worker drafted JCH, was separate from
the other drafting workers, and shares the frozen inputs with all four.
It is an internal LLM assessment. See the [result index][results],
[avoid index][avoid], [shared-premise guidance][shared] and
[evidence-status guidance][status].

**Disposition: Accepted as analytical drafts within stated scope.**

The [frozen manuscript contract][request] and
[30-file input map][manifest] identify the mathematical dependencies.
The [cross-review record][record] identifies the exact manuscripts and
input versions. The branch source maps and assessments give the
individual derivation provenance. Their source status is retained.
This review checks the analytical text. The parent coordinates the
separate PDF build, extraction and visual checks.

## Shared source and clocks

The four drafts use
\(W_\lambda=e^{\lambda u^2}\Phi\) and
\(H_\lambda(z)=\tfrac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du\).
All derive smooth reflection of the complete theta sum from
\(p(-u)-p(u)=\sinh u\) and use positivity on the positive half-line.
Each checks the \(p'(0)=-1/2\) endpoint, the split theta Mellin term
\(1/[s(s-1)]\), and the factor \(8\) from \(t=e^{4u}\) at
\(s=(1-iz)/2\). These give \(H_0(z)=\xi(s)/8\) in the common
physical convention, together with \(\partial_\lambda H=-H_{zz}\).
The reverse clock is \(\tau=1/2-\lambda\), so the source in that
clock carries \(e^{-\tau u^2}\), and \(\partial_\tau H=H_{zz}\).
The double-exponential tail justifies each fixed differentiated
integral. The drafts keep theorem-specific height and error domains.

The sampled QTT amplitudes are \(\sqrt h\,W_\lambda(u_{\boldsymbol b})\).
JCH transports its probability-normalized \(L^2(\mu_*)\) state, with
Lebesgue realization \(\sqrt{W_*/Z_*}\,e^{-\tau u^2+ixu}\).
VCD instead orthogonalizes at each moving slice and restores that
slice's \(Z_\lambda/2\) in its scalar formula. ITP prepares \(\sqrt{m_{L,j}}\),
which represents \(\sqrt{P_hW_\lambda}\) under the \(L^2(du)\) cell
isometry. Each targets the same physical scalar, and the approximation
statements use their specified error norms. The two Jacobi bases coincide at the
base slice. Replacing raw \(h_N(1/2)\) with \(h_N(1/2)/h_0(1/2)\)
in the JCH remainder is essential.

## Individual derivations and limits

| Draft and assessment | Checks and scope |
| --- | --- |
| [QTT draft][qtt], [source map][qttmap], [assessment][qttreview] | The holomorphy rectangle contains the Cauchy circles and the \(\rho=5/4\) ellipse. Direct differentiation, geometric tails and the analytic cosine bounds give the \(2^{57}\) derivative cap and \(2^{-192}\) exterior allowance. Symmetric Laurent coefficients give the factor of two in the Chebyshev error. At \(d=512,m=64,L=72\) the polynomial degree gives bond cap \(641\). The exact generator has bond cap three, while the exact multiplier for positive reversed time has full Vandermonde unfolding rank at each cut. Two product phase contractions give the midpoint cosine with weight \(h=2^{-71}\). The error ledger in the scaled absolute norm sums below \(2^{-36}\) on \(0\le\lambda\le1/2,\ 40\le x\le80,\ |y|\le8\). Direct scalar integration of the same polynomial removes the midpoint term. Coefficient acquisition, conditioning, practical contraction and larger heights remain open. |
| [JCH draft][jch], [source map][jchmap], [assessment][jchreview] | Entire Fourier uniqueness gives polynomial density for both \(\mu_*\) and \((1+u^2)\mu_*\), the latter giving the graph core. Transported multiplication fixes the spectral domains, including the prepared-vector meaning at nonreal height. Parity removes the diagonal. The reference-vacuum state has exact one-excitation prefixes and a squared \(\ell^2\) tail. Fixed-prefix mass escape follows from fixed-coordinate Fourier decay. The principal-square boundary correction is exactly \(a_N^2e_{N-1}e_{N-1}^*\). The returning walks locate the first missed moment and identify its defect as \(h_N^*\). Real Hermite interpolation followed by Gaussian averaging yields \(S_N\), and the complete-source score estimate yields \(N=\lceil4K\log(16K)\rceil\) for the stated real scalar tolerance in fixed base-mass units. The perturbation argument uses exact nominal edge midpoints only for \(\widehat J\). The 16-site example separates uniform ideal error and nine-point rounding from the unsuccessful 128-bit coefficient-width gate. Exact Gaussian quadrature gives identical scalar output. Prefix transport rates, useful growing-height bounds, conditioning and signed estimates remain open. |
| [VCD draft][vcd], [source map][vcdmap], [assessment][vcdreview] | Positive finite Gram matrices and differentiated moments give differentiable monic polynomials. The lower-degree orthogonality calculation yields \(\partial_\lambda P_n=-\beta_n\beta_{n-1}P_{n-2}\) and \(\partial_\lambda\log h_n=\beta_n+\beta_{n+1}\). Subtracting adjacent derivatives gives the Volterra equation. With \(J^2=L+D+U\), the orthonormal basis derivative is \(A=-L-D/2\), hence \(A=(U-L)/2-J^2/2\) and \(J'=[(U-L)/2,J]\) entrywise on finite sequences. Reversing the clock reverses the coefficient derivative. The score lower bound, integration by parts and Jensen give \(\arcosh^2(2n+12)/16\) uniformly in heat time. The raw norm product divided by the base mass supplies its probability-measure counterpart in the finite-chain consumer. The weighted-square control brackets match the cited records. Degree asymptotics, stability of prefixes and signed readout remain open. |
| [ITP draft][itp], [source map][itpmap], [assessment][itpreview] | Conditional mass splitting is isometric, and the common embedding uses an appended uniform reference bit. The exact source factors telescope locally with summable deviations from identity, controlled by the interval minimum and parent oscillation. Weighted state convergence uses the square-root inequality and the projection kernel bounded by \(h/2\). Local phase factors converge in operator norm on compact \(z\) sets and their exact conditional mean supplies the centered sinc multiplier. The full-line Fourier estimate depends only on \(b=|y|\), and at \(U=2,\ L=30,\ |y|\le8\), the bound \((1736+330)/2^{32}<5\cdot10^{-7}\) is physical absolute error over all real \(x\). The fixed center-point comparison fails uniformly because of its exact alias frequencies, while direct integration of the step density gives identical output. The projected time derivative uses \(P_h(u^2W)\). Uniformly accurate acquisition of \(2^{32}\) formal masses, growing-prefix ranks, global source-factor operator limits and numerical phase evaluation over unbounded real heights remain separate tasks. |

## Bounded response check

The initial VCD manuscript fixed the physical Fourier factor but omitted
the time-zero \(\xi/8\) endpoint calculation. The review requested the
primitive endpoint and split Mellin derivation in §2. It also requested
wording in the growing-height discussion that preserves the already
proved sufficient exact-coefficient depth. On bounded recheck the returned
draft includes the normalization derivation and separates sufficient
depth from sharp depth and certified coefficient precision. Its Volterra
and coefficient estimates are unchanged.

## Scope of the four results

The Hermite and dyadic proofs bound scalar observations in distinct error
norms. QTT uses a prescribed zeta-prefactor scale, JCH uses \(H_{1/2}(0)\),
and ITP uses unscaled physical \(H_\lambda\). None divides by a varying
or potentially zero field. The VCD coefficient envelope controls the
monic norm input and retains the real scalar scope of its downstream
consumer. The drafts separate exact formal representations, derived
absolute allowances, archived interval evidence and unpaid numerical work.

The heat and chain identities also hold for sources with collisions.
The atomic control has low rank, exact terminating readout and regular
coefficient evolution while the scalar has a double zero. Positive
weighted-square controls can pass the score proof and still collide.
Evenness, positive source mass and approximability therefore leave the
signed and zero-sensitive questions open. Each scope remains as stated
in the branch control screens and the [collision catalog][controls].
The final sections identify the outstanding challenge specific to each
representation. No new numerical experiment, scientific mechanism or
extension of the frozen contract was assessed.

[request]: ../research-progress/handoffs/TN6-E04-r1.md
[manifest]: ../numerics/14_TN6_E04_MANUSCRIPT_INPUTS_20261114.json
[record]: ../numerics/16_TN6_MANUSCRIPT_CROSS_REVIEW_20261114.json
[shared]: ../../../avoid/05_same_model_reviews_and_shared_premises.md
[status]: ../../../avoid/06_status_stronger_than_the_evidence.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[qtt]: ../01_qtt_newman_flow/manuscript/main.tex
[qttmap]: ../01_qtt_newman_flow/notes/05_QTT_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md
[qttreview]: ../01_qtt_newman_flow/reviews/02_QTT_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md
[jch]: ../02_jacobi_chain_height_flow/manuscript/main.tex
[jchmap]: ../02_jacobi_chain_height_flow/notes/03_JCH_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md
[jchreview]: ../02_jacobi_chain_height_flow/reviews/02_JCH_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md
[vcd]: ../03_volterra_coefficient_dynamics/manuscript/main.tex
[vcdmap]: ../03_volterra_coefficient_dynamics/notes/02_VCD_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md
[vcdreview]: ../03_volterra_coefficient_dynamics/reviews/02_VCD_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md
[itp]: ../04_exact_infinite_tensor_products/manuscript/main.tex
[itpmap]: ../04_exact_infinite_tensor_products/notes/03_ITP_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md
[itpreview]: ../04_exact_infinite_tensor_products/reviews/02_ITP_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md
