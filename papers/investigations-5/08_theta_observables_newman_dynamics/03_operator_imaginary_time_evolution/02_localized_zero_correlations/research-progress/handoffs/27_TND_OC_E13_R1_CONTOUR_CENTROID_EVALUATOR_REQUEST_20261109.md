# E13 r1 request: complete contour-centroid Gaussian evaluator

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, OC chat0009. Authoring thread
settings recorded as `gpt-6-astra / max`; per-turn backend
configuration unavailable. Root authored this packet, without delegation.

**Task:** TND-OC-E13, revision r1. **Type E — execution.**
**Recommended model: GPT-6.1 Sol**, author-selected effort.
The source, observable, acquisition algorithm, constants, work caps and
success/failure tests are fixed. **Ready, unactivated.** No executor has
been dispatched. [Progress02][progress] is the sole status owner.
[Inputs27](27_TND_OC_E13_R1_INPUTS_20261109.json) freezes mathematical
versions; policy/navigation drift is reconciled separately.

## 1. Purpose and unchanged target

Execute the conditional theorem in [Note20][note]. The additional data
are complete **cell counts and first complex moments**, not individually
isolated simple real zeros. Return a certified value for exactly Note19's
blurred marked separation projection at
\[
 T=1000,\quad X\sim{\rm Unif}[1000,2000],\quad
 h=\ell=1,\quad\epsilon=1/4.
\]
Both imaginary-mark factors, same-center weights and distinct
multiplicity labels remain. This is a finite canonical projected value,
not the full Q² function, an asymptotic law or collision exclusion.

For z=x+iy,w=x'+iy', use precisely
\[
 K(z,w)=\frac{32\sqrt2}{51}\frac{\sqrt\pi}{2000}
 [\operatorname{erf}(2000-m)-\operatorname{erf}(1000-m)]
 e^{-25(x-x')^2/36}
 e^{-(8/17)(y-1/2)^2}e^{-(8/17)(y'+1/2)^2},
 \quad m=(x+x')/2.                                   \tag{1}
\]
Do not change either edge, a mark, the blur, window width or
normalization. All ordered cell pairs contribute; do not truncate
Gaussian pairs by apparent smallness unless their complete discarded
ball sum is included within the final arithmetic-radius gate.
The center/gap factor is symmetric, but K itself generally is not:
the two imaginary-mark factors differ. Any reuse or pairing must retain
both ordered contributions and their correct marks.

## 2. Fixed proof checks before the canonical run

Check Note20's following obligations once, with at most one bounded
correction preserving the target, frozen gates and final \(<1/100\) goal:

- P1: \(Z(z)=\zeta(1/2-iz/2)\) has exactly H0's divisor in the fixed
  rectangle, without poles or spurious completion zeros.
- P2: Complete theta majorant/anchor, Jensen global count, Gaussian
  omitted weight \(<2^{-44}\), and pair tail \(<2^{-32}\) under N≤1024.
- P3: Kernel gradient/Hessian constants \(9/T,18/T\), and diagonal
  constants \(4/T,10/T\), including finite center edges.
- P4: Complex first-moment cancellation of both real linear terms,
  two-variable Taylor telescoping and correct n_C self subtraction.
- P5: Contour nonvanishing/count extraction, centered first moment,
  validated midpoint remainder and Euclidean centroid enclosure.
- P6: Exact arithmetic/error allocation, replayability and retained
  finite scope. Run the small exact-constant replay.

A change of source, mechanism, observable or mathematical premise is
outside routine repair: record the failed clause and return to B10 r3.
Do not waive a gate because the known low-height zeros are expected real.

## 3. Complete source and count acquisition

Use the fixed rectangle
\[
 \mathcal R=(988,2012)+i(-3/2,3/2)
\]
and exact canonical \(Z(z)=\zeta(1/2-iz/2)\).
Every evaluation must be an outward complex-ball enclosure, including
the underlying zeta algorithm's complete remainder. The chosen default
runtime is python-flint 0.9.0 if available/installable in an isolated
environment; record the actual Python, python-flint and FLINT versions.
The design session's default python3 had no flint. Runtime preflight/setup
is allowed; installation failure is an explicit environment return,
not a mathematical contradiction. Do not replace intervals by floats.

Use B07's certified winding rule: partition each boundary into oriented
straight segments; enclose the **entire segment image** under Z in a
convex complex rectangle excluding zero. Enclose each endpoint ratio's
principal argument strictly inside (-pi,pi). Sum argument balls divided
by 2pi and require exactly one enclosed integer. A nonnegative count is
required. Endpoint samples alone do not certify nonvanishing.

First obtain the complete outer count N and require \(N\le1024\).
An outer contour that cannot be certified within caps is a failed gate;
do not move the fixed outer rectangle. N=0 is admissible: the finite
sum is zero and the declared tail still applies.

Recursively subdivide occupied cells:

1. Try a cut perpendicular to the longest side, at fractions
   \(1/2,3/8,5/8\), in that order; ties choose the real direction.
   Coordinates stay exact dyadic. There are at most three distinct cut
   choices per node, with only the precision ladder below.
2. Certify child boundaries and complete counts by the same rule.
   Require their counts to sum to the parent count. A failed cut may
   use the next declared fraction; do not omit points near a cut.
3. Stop on a zero count, or on an occupied cell whose squared diameter
   is at most \(2^{-24}\). Occupied counts may exceed one.
4. All accepted occupied leaf counts must sum to N. Retain enough
   tree/boundary information to replay completeness and nonvanishing.

The proof has no minimum-gap or simple-root premise. The finite
implementation can fail if proposed boundaries come too close to zeros.
That is an allowed outcome, not evidence that a zero is noncanonical.

## 4. First moments with a fixed certified quadrature

For each occupied cell, use its exact dyadic geometric center a_C and
\[
 G_C(z)=(z-a_C)Z'(z)/Z(z),\quad
 q_C=(2\pi i)^{-1}\oint G_C(z)\,dz,\quad
 c_C=a_C+q_C/n_C .
\]
Use **centered** moments, not subtraction of large uncentered power sums.

On each boundary segment [z0,z1], take its exact midpoint z_m and
length L. Enclose the integral by
\[
 (z_1-z_0)G_C(z_m)
 \quad\text{with additional complex-disk radius}\quad
 L^3\,\sup_{[z_0,z_1]}|G_C''|/24.                     \tag{2}
\]
Convert the disk allowance to an outward rectangular ball if needed.
Evaluate Z through cubic power-series order over an input complex ball
covering the entire segment; coefficient k encloses \(Z^{(k)}/k!\).
Use the literal derivative factor \(-i/2\) from s(z).
Formal series differentiation/division and the factor 2 on the
quadratic coefficient yield a bound for \(G_C''\).
Division requires a denominator ball excluding zero. No assertion that
the interior of the cell is zero-free is made.

Bisect quadrature segments as needed within caps. Sum all segment
balls and remainders, divide by \(2\pi i n_C\), and choose an exact dyadic
point \(\widehat c_C\). Its **Euclidean** error from every point of the
centroid enclosure, including midpoint rounding, must be
\(\sigma\le2^{-24}\). This is not a coordinatewise-radius substitution.
The squared diameter gate ensures each true root in C is within
\(r=2^{-12}\) of the exact centroid by convexity.

## 5. Evaluate the same-center pair and certify the final error

Compute with certified real-ball erf/exponential arithmetic
\[
 \widehat P=\sum_{C,E}n_Cn_EK(\widehat c_C,\widehat c_E)
             -\sum_C n_CK(\widehat c_C,\widehat c_C). \tag{3}
\]
The diagonal coefficient is \(n_C(n_C-1)\).
No real-axis replacement of imaginary parts and no independent-center
product is allowed. Evaluate all finite center integrals exactly through
(1); their transcendental rounding belongs to the following gate.

Require the arithmetic evaluation of (3) to have radius at most
\(1/400\). Add the analytic allowance
\[
 E_{\rm ana}=
 \frac{36(1024)^2+9(1024)}{1000\,2^{24}}+2^{-32}<1/400.       \tag{4}
\]
A final radius \(<1/200\), hence \(<1/100\), completes the pilot.
A tighter bound from actual certified N, diameters and centroid errors
is allowed within the same proof. No expected sign, repulsion shape,
realness or comparison with a random-matrix profile is an acceptance gate.

Source/log approximation, frequency cutoff, center quadrature and
unsmoothing have no separate unpaid terms: this route uses exact source
balls and the unchanged exact Gaussian contraction. A replacement by
truncated theta data would require a revised source-access contract
including both arithmetic/radial and derivative/ratio errors.

## 6. Work limits and permitted implementation choices

- Precision ladder: **128, 256, 512 bits**, no fourth level.
- At most **100000 distinct attempted cell-tree nodes**, including
  failed-cut children; tree depth at most **96**.
- At most **1000000 accepted boundary/quadrature segments** retained
  across the run; individual segment subdivision depth at most **96**.
- At most **2000000 wrapper-level canonical zeta/series evaluations**
  across all attempts and precision levels. A scalar or cubic-series
  call counts as one; this does not bound library-internal operations.
- N≤1024 and at most 1024 occupied leaves.
- At most **3200000 elementary kernel evaluations per precision pass**
  and **9600000 total**. Count erf and exponential calls. The direct
  bound \(3L^2+2L+16\), L≤1024, fits each pass; symmetry/reuse is allowed.
- The cumulative canonical acquisition/evaluation wall-clock cap is
  **30 minutes**, enforced externally even during a library call.
  Environment setup, proof reading and documentation are separate;
  they do not authorize more canonical runtime.
- One bounded implementation/proof repair is allowed, with **no reset**
  of numerical counters or runtime. No scan of heights, widths, new
  source algorithms, extra cut fractions or enlarged caps.

Caching shared contour edges, scheduling cells, avoiding duplicate kernel
factors and choosing refinements inside these caps are routine execution
choices. Preserve the proof meaning of every enclosure. Stop at the
first exhausted gate and report it precisely.

## 7. Outputs and evidence

Return:

- A proof-check disposition for P1–P6 and any bounded correction.
- Source runtime versions, exact outer count, cell count/completeness
  records, contour nonvanishing/winding records, centered-moment
  enclosures and exact dyadic centroids with certified radii.
- The finite projected value, its arithmetic ball, analytic allowance
  and final canonical enclosure; or the exact failed gate.
- Actual wrapper counts, precision levels, subdivision counts,
  cumulative elapsed time and whether an external timeout occurred.
- A replay command and code in numerics/, a small execution record,
  an assessment in reviews/, a sole-register update and a continuation.

Preserve all issued packets and historical failures. Hash inputs before
execution; record policy/navigation drift separately from mathematical
changes. Keep individual tracked files below 1 MiB. Large regenerable
contour logs belong outside Git/repository under LARGE_FILES.md, with a
small hash/parameter record and regeneration guide; do not commit large
derived tables or third-party PDFs. Source hashes identify versions,
not mathematical truth. Do not hand-edit registered chat archives.

Permitted research edits are inside this OC investigation: new execution
notes, numerics code/small records, assessment and return/continuation,
plus its existing navigation, sole progress register and DRAFT_HISTORY.
Chat archives change only through the shared-lock recorder. Do not
alter manuscripts, sibling statuses, prior issued packets or root
result/avoid summaries as part of this finite execution.

Success supplies a finite projected canonical estimate only.
Failure is scoped to this fixed method and budget. A new mathematical
mechanism, different target or enlarged run requires **[B] TND-OC-B10 r3 /
Astra**, with the named failed input. E09's compact-window packet,
E10/E12's time modulus and E03/E04 remain unchanged.

[note]: ../../notes/20_TND_OC_B10_R2_CONTOUR_CENTROIDS_AND_GAUSSIAN_ESTIMATE_20261109.md
[progress]: ../02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PROGRESS_20261108.md

