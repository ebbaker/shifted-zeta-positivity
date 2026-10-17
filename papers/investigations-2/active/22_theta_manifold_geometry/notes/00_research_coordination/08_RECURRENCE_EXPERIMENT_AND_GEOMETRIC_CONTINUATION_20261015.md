# Recurrence endpoint experiment and geometric continuation

> **17 October 2026 — history routing update.** Historical formal-replay routing below is superseded. Chats [20](../../chat-histories/0020_2026-10-15T15-16-42Z_brainstorm-theta-geometry-paths.json) now use this investigation's [local registry](../../chat-histories/index.json), as recorded in the [relocation receipt](../../CHAT_HISTORY_RELOCATION_20261017.json). Original identities, provenance and public messages are preserved. All future Investigation 22 chats belong in this local history folder.

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This is a research continuation note; no manuscript integration or theta signed-core theorem is claimed.

## Result of the requested experiment

The [adjoint recurrence calculation](../03_theta_bundles_and_connections/08_ADJOINT_RECURRENCE_ENDPOINT_EXPERIMENT_20261015.md) has been carried out. It yields useful endpoint approximation and coefficient-stability estimates, but **does not establish the needed signed estimate**. The finite current moves the unresolved observation to a single lower boundary trace. Attempting to remove that trace with the primitive endpoint normalization restores the original observation as the remainder, exactly.

This is a concrete outcome of the bounded experiment proposed in [Note 07](07_RESEARCH_PATHS_AFTER_COUPLED_PRODUCT_20261015.md), following the [coupled-product and reflection continuation](06_COUPLED_PRODUCT_AND_REFLECTION_CONTINUATION_20261015.md).

## Four results to retain

1. **A recurrence-adapted endpoint cutoff.** With the half-line averaging operator \(T\), prescribe \(J^{[L]}=-\tfrac12\sum_{k<L}T^kF\). Then \(\Delta J^{[L]}=F-T^LF\), and \(\sum F=-J_1^{[L]}+\sum T^LF\). The boundary weights are probabilities that a symmetric walk hits zero by time \(L\). Its residual satisfies

   \[
   |R_L(F)|\le p_L\sum_{n\ge1}n|F_n|,
   \qquad p_L=2^{-L}\binom L{\lfloor L/2\rfloor}=O(L^{-1/2}).
   \]

   The resulting finite endpoint approximation preserves the full starting factor and gives an \(O(L^{-1/2})\sqrt E\) transfer error. The flexible fixed-length criterion already accepts this rate. No sign follows from the cutoff.

2. **An exact failure of normalization cancellation.** For the endpoint residual \(r\),

   \[
   \sum r=B_L(r)+\eta R_L(\beta)+R_L(r-\eta\beta).
   \]

   Choosing \(\eta=-B_L(r)/R_L(\beta)\) cancels the displayed boundary term but forces \(R_L(r-\eta\beta)=\sum r\). For a fixed residual sequence \(r\) with nonzero total sum, \(\eta\) grows like \(\sqrt L\), precisely erasing the residual improvement. This failure does not rely on division by physical energy or stationarity.

3. **Quantitative stability of the recurrence.** For \(d_k=\Delta a_k\), endpoint defect \(e=\sum\beta_na_n-1/2\), and a physical mode test \(|f_n|\le C\beta_n\),

   \[
   F_a-F_\theta=\eta_f e+\sum_{k\ge1}D_k(f)d_k,
   \quad |\eta_f|\le C,
   \quad |D_k(f)|\le8C\beta_{k+1}.
   \]

   The Gaussian dual weights quantify perturbation from theta. At exact theta the defects vanish; the identity does not determine the sign of \(F_\theta\).

4. **A sharp finite-hierarchy rate.** Positivity, exact endpoint normalization and \(\Delta a_k=0\) for \(1\le k\le N\) imply \(O(1/N)\) control of every such physical observation. Positive finite ramp-plus-spike examples attain that order, including at \((t,x)=(0,0)\). Adding \(a_1=1\) removes the residual affine slope and improves the estimate to the Gaussian beta tail. These examples test a finite relaxation; they are not collision examples.

The primitive normalization also has the exact transform interpretation \(H_a(0,i)=1/16\). It is an imaginary spectral anchor, distinct from a real stationary sign inequality.

## What geometry now contributes

The [geometric companion](../01_physical_jet_geometry/01_ARITHMETIC_BOUNDARY_TRACE_AND_SIGNED_OBSERVATION_20261015.md) supplies three precise diagnostics.

- The rapidly decreasing recurrence currents with zero lower flux have a **one-dimensional cokernel**, detected by total sum. The primitive endpoint spans that missing boundary class. An arbitrary Green inverse therefore relocates the unknown instead of bounding it.
- An endpoint functional has a bounded reconstruction from a finite physical-jet relaxation exactly when it descends to the physical observation quotient. Its sharp norm is a pseudoinverse norm. Pointwise descent still permits blowup through degeneration, so vanishing order matters as well as rank.
- The chord needs a **signed** bound, \([WV]_+/E\), rather than absolute control of \(|V|/\sqrt E\). A boundary trace with the opposite sign to the starting jet can be large and harmless. Direction alone loses the radial order; an unmarked metric loses the physical orientation.

The manuscript already recognizes the need for physical orientation, and earlier source work already retained divergence terms. The additional information here is the explicit arithmetic boundary class, its failure under normalization cancellation, and the sharper signed trace target. None is itself a new positivity theorem.

## Recommended next calculation and decision rule

The next bounded experiment should seek a **joint coefficient/source conservation law** with a source-prescribed current, then estimate its full signed boundary trace. Schematically,

\[
r_n(u)=\Delta_nJ_n(u)+\partial_uK_n(u)+\rho_n(u).
\]

The pure finite-range coefficient-current ansatz has a rigorous pointwise obstruction in the declared polynomial/source-jet class. A joint law has a different scope, but simply integrating the existing primitive identity leaves an indefinite bulk. A successful calculation must show what new relation supplies the favorable sign.

After all summations and integrations, write

\[
V=AH+BH_x+CS+B_{\partial}+R,
\qquad |R|\le\varepsilon.
\]

On complete stationary starts, with \(\rho=\sqrt E>0\), the practical target is

\[
\boxed{\frac{W}{\rho}B_{\partial}
\le C_0\rho+\varepsilon_0.}
\]

This is weaker than asking for small absolute boundary values and implies the existing mixed-error chord criterion when \(A,B,C_0\) remain locally bounded and the errors vanish at the prescribed scales. Keep both stationary branches and all lower and cutoff endpoints. Do not optimize coefficients by division through \(H\), \(H_x\), \(S\), or \(E\); an independently derived cancellation must survive their degeneration.

The acceptance test for another geometric representation is an independently proved sign or vanishing-order estimate for this complete trace. If it only changes a metric, computes a pseudoinverse, or chooses a normalization coefficient using the unknown observation, stop that ansatz. The positive recurrence hierarchy is useful as a quantitative control family, but closeness to theta alone cannot decide theta's sign. Broader outer-bridge alternatives remain as ranked in Note 07; the current experiment does not change their coverage or constant requirements.

## Saved verification

The [checker](../../numerics/check_adjoint_recurrence_boundary.py) passes **6,892 exact rational assertions**, with an [execution receipt](../../numerics/ADJOINT_RECURRENCE_BOUNDARY_CHECKS_20261015.json) and independent replay described in the [review](../../reviews/08_ADJOINT_RECURRENCE_AND_GEOMETRIC_REVIEW_20261015.md). Finite surrogate checks are separate from the general analytic proofs. The manuscript remains unchanged, and the conversation retains formal replay history identity 20.
