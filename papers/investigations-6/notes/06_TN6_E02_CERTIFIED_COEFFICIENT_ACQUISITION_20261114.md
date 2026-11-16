# TN6-E02 r1 — Certified complete-source acquisition and readout

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Explicit worker dispatch
**gpt-6.1-sol / ultra**. Backend identity and actual runtime effort are
unavailable as independently exposed metadata. Status **certified within
the frozen execution scope**, pending the separate TN6-E03 internal
assessment.

At 256 bits the 16-site chain acquired all sixteen positive Jacobi
couplings from seventeen complete theta moment enclosures. Its exact
nominal readout has uniform absolute error less than \(1.515\times10^{-25}\)
in units of \(H_{1/2}(0)\) for \(0\le\tau\le1/2,\ |x|\le8\).
All nine specified numerical readouts also met this rounded bound with
rounding included. The 128-bit attempt missed the coefficient uncertainty
cap. The matched direct baseline used less measured time for the nine
points on this run.

The [result index](../../../result-summaries/README.md), [tensor bounds 18](../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and [avoid index](../../../avoid/README.md) route to the inherited results
and scope limits. This is a finite absolute approximation result in the
classification of [avoid 01](../../../avoid/01_restating_the_target.md).
The acceptance target was \(10^{-8}\) in fixed base-mass units. The source
and controls remain those in the [B02 decision](../brainstorm/notes/02_TN6_B02_FINITE_COEFFICIENT_ACQUISITION_DECISION_20261114.md)
and [frozen r1 packet](../research-progress/handoffs/TN6-E02-r1.md).

## Complete source and permitted quadratures

The [GNP source chapter](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex)
fixes
\[
 W_*(u)=e^{u^2/2}\Phi(u),\qquad
 \Phi(u)=e^u\sum_{m\ge1}(2r_m^2-3r_m)e^{-r_m},\qquad
 r_m=\pi m^2 e^{4u}\quad(u\ge0).
\]
Use the complete even reflection. With full-line raw moments \(m_j\) and
\(Z_*=m_0\), the odd moments are zero and
\[
 H_{1/2-\tau}(x)=\int_0^\infty W_*(u)e^{-\tau u^2}\cos(xu)\,du,
 \qquad H_{1/2}(0)=Z_*/2.
\]
All tail payments use positivity of the canonical summands on the positive
half-line. The finite \(M=8\) integrand was evaluated on the four prescribed
panels up to \(U=2\). The moment calculation doubles those half-line
integrals. The separate direct calculation integrates the same finite series
times \(e^{-\tau u^2}\cos(xu)\) on those panels and keeps the half-line scale.

For the omitted modes inside the cutoff, \(2r_m^2-3r_m\le2r_m^2\).
Also \(e^{-r_m}\le e^{-\pi m^2}\), and the ratio of successive
\(m^4e^{-\pi m^2}\) is bounded above for \(m\ge9\) by
\(q=(10/9)^4e^{-19\pi}<1\). With \(a=9^4e^{-81\pi}\), the full-line
arithmetic allowance is
\[
 A_k=4\pi^2 U^{2k+1}e^{U^2/2+9U}\frac{a}{1-q}.
\]
For the spatial allowance put \(\rho=\pi e^{4u}\), \(R=\pi e^8\). The
[pinned ITP bound](../04_exact_infinite_tensor_products/notes/02_ITP_E01_EXACT_CELL_PHASE_TRANSFER_20261113.md)
gives \(\Phi(u)<10e^u\rho^2e^{-\rho}\). On \(u\ge2\) and \(0\le k\le16\),
\[
 2k\log u+u^2/2+u
 \le32\log u+u^2/2+9u
 \le u^2/2+41u
 \le16u^3
 \le\rho/2.
\]
The last inequality uses the cubic term of \(e^{4u}\) and \(\pi>3\).
With \(du=d\rho/(4\rho)\) and both half-lines, the integral of the
resulting bound gives \(B=10(R+2)e^{-R/2}\). Thus the full moment lies in
twice the retained ball plus \([0,A_k+B]\). The direct tail is bounded in
absolute value by \((A_0+B)/2\). This verifies the B02 constants as issued.
At 256 bits the stored arithmetic upper endpoints run from approximately
\(7.69\times10^{-97}\) for \(k=0\) to \(3.30\times10^{-87}\) for \(k=16\),
and the common spatial upper endpoint is about \(2.50\times10^{-2029}\).

The integrand callbacks use Acb sums, integer powers and entire exponential
and cosine functions. They remain enclosing on complex integration balls.
Each returned ball, including its real and imaginary intervals, is saved.
The callbacks apply the same issued tolerance \(2^{-p+32}\) at each panel
at precision \(p\). All acceptance comparisons use the returned enclosure.

## Raw norms, finite Jacobi matrix and uniform payment

The parity blocks have indices \(0,2,\ldots,16\) and \(1,3,\ldots,15\)
with entries \(m_{i+j}\). Exact parity orthogonality means that the LDL
pivot at degree \(n\) is the raw squared monic norm \(h_n\). Indeed,
without pivoting, eliminating all lower monomials of the same parity
implements orthogonal projection, and lower terms of the opposite parity
are already orthogonal. The interval algorithm divides only by certified
positive pivots. It records the enclosing \(h_n/m_{2n}\), radius divided
by midpoint of \(h_n\), and each positivity decision. Validated inversion
of the diagonally scaled blocks supplied condition upper bounds for both
parities at both precisions.

The coupling formula \(a_n=\sqrt{h_n/h_{n-1}}\) gives the finite chain
edges \(a_1,\ldots,a_{15}\); \(a_{16}\) is the edge lost at the cut.
All seventeen raw pivot intervals and sixteen coupling intervals were
strictly positive at both levels. The nominal matrix \(\widehat J\) is
exactly symmetric with zero diagonal and the stored exact dyadic edge
midpoints. Zero-pad the fifteen internal edge radii and take the maximum
sum of adjacent radii. This is \(\delta\), an upper bound for the maximum
absolute row sum and hence the spectral norm of \(J_{16}-\widehat J\)
by symmetry. The stored radius of edge 16 is excluded from this row sum.

For the probability measure \(W_*\,du/Z_*\), the positive complete
density gives all finite moments and strict Gram positivity. Its monic
norm at degree 16 is \(h_{16}/h_0\) in the notation here. These are the
hypotheses and normalization of [JCH R2](../02_jacobi_chain_height_flow/notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md).
At a uniform corner define the exact positive rational
\[
 S_{16}(1/2,8)=\sum_{k=0}^{16}\frac{8^{32-2k}}{2^k k!(32-2k)!}.
\]
R2 and nonnegative terms give the normalized chain truncation bound
\(Q=\operatorname{upper}(h_{16}/h_0)S_{16}(1/2,8)\). The ratio is
enclosed before multiplication by the exact rational factor.

For real symmetric \(A,B\), integrating the derivative of
\(e^{i(s-v)A}e^{ivB}\) in \(v\) bounds the norm of the unitary difference
by \(|s|\|A-B\|_2\). Taking real cosine and a Gaussian average with
\(s=x+\sqrt{2\tau}G\), \(G\) standard normal, gives
\[
 \|e^{-\tau A^2}\cos(xA)-e^{-\tau B^2}\cos(xB)\|_2
 \le (|x|+\sqrt{4\tau/\pi})\|A-B\|_2
 \le 9\|A-B\|_2.
\]
The diagonal parity matrix with entries \((-1)^j\) conjugates each chain
to its negative and preserves \(e_0\). The first diagonal entry of
\(e^{-\tau\widehat J^2+ix\widehat J}\) is therefore real. Both scalar
functions with exact matrices have magnitude at most one by the
self-adjoint functional calculus. For \(\widehat Z\) the exact mass
midpoint, this proves for the exact nominal physical scalar \(\widehat H\)
\[
 \frac{|H_{1/2-\tau}(x)-\widehat H(\tau,x)|}{Z_*/2}
 \le Q+9\delta+\eta_Z,\qquad
 \eta_Z=\frac{\operatorname{rad}(Z_*)}{\operatorname{lower}(Z_*)},
 \qquad
 \widehat H=\frac{\widehat Z}{2}
    \big[e^{-\tau\widehat J^2+ix\widehat J}\big]_{00}.
\]
At a nominated sample Acb encloses the matrix exponential with the
finite nominal square, verifies that the scalar imaginary enclosure
contains zero, and encloses the nominal physical real scalar with radius
\(r_j\). Its normalized rounding payment is \(2r_j/\operatorname{lower}(Z_*)\).
For overlap in physical units the chain scalar ball is enlarged by
\((Q+9\delta+\eta_Z)\operatorname{upper}(Z_*)/2\). The direct calculation
has its own tail payment. Moment integration, tails and arithmetic enter
the chain through the complete mass and LDL bounds.

## Certified allowances and measured costs

The upper bounds in the 256-bit column are rounded upward from the
[exact certificate](../numerics/09_TN6_E02_R1_CERTIFICATE_20261114.json).

| Quantity in base-mass units | 256-bit upper bound | Frozen cap |
| --- | ---: | ---: |
| \(Q\), uniform chain truncation | \(1.515\times10^{-25}\) | \(5\times10^{-9}\) |
| \(9\delta\), uniform coefficient perturbation | \(1.385\times10^{-46}\) | \(2\times10^{-9}\) |
| \(\eta_Z\), uniform mass perturbation | \(3.472\times10^{-68}\) | \(10^{-9}\) |
| Maximum sample rounding payment | \(1.740\times10^{-77}\) | \(10^{-9}\) |
| Maximum total among the nine chain samples | \(1.515\times10^{-25}\) | \(10^{-8}\) |
| Maximum normalized complete direct radius | \(3.812\times10^{-68}\) | \(10^{-9}\) |

The base mass \(Z_*\) has midpoint approximately \(0.1250039038038615\);
\(h_{16}/h_0\) is about \(1.90812634\times10^{-21}\). The smallest lower
endpoint of \(h_n/m_{2n}\) is at degree 16 and is about
\(1.96029264\times10^{-5}\). The maximum relative pivot radius is at the
same degree, about \(2.134\times10^{-45}\) at 256 bits and
\(2.487\times10^{-6}\) at 128 bits. The acquired 256-bit condition upper
bounds are below \(6.931\times10^7\) and \(2.020\times10^7\) for the
scaled even and odd blocks, respectively. At 128 bits
\(9\delta\) was approximately \(1.790589064\times10^{-7}\), above its
\(2\times10^{-9}\) cap. This is a width failure for the issued algorithm
at 128 bits. Its upper bound gives no lower bound on the actual approximation
error.

| Precision | Outcome | Integral calls | Matrix exponentials | Callbacks | Finite mode evaluations | Attempt wall time |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 128 bits | Acquisition width failed | 68 | 0 | 4,384 | 35,072 | 0.322 s |
| 256 bits | Complete pass | 104 | 9 | 15,636 | 125,088 | 1.521 s |

Every direct enclosure overlaps its enlarged chain enclosure. The
bounded differences between the exact nominal and the complete direct
scalar are in the certificate for each point. The largest absolute
upper bound is below \(7.771\times10^{-27}\) in physical units, at
\((\tau,x)=(1/2,8)\). This comparison checks consistency of two
enclosures with separately derived error payments.

Including the 128-bit attempt, acquisition used 1.136 s and the nine
matrix readouts used 0.152 s in their instrumented phases. Chain acquisition
plus nine readouts used 1.288 s, or 0.143 s per sample when amortized over
nine. Direct evaluation of all nine used 0.535 s, or 0.059 s per sample.
For first use, the successful acquisition plus first exponential used
0.818 s for those reported operations. Charging the earlier failed
acquisition gives 1.136 s by the same metric. The first direct point's
four integration calls used 0.0104 s. These first-use figures sum the
specified operations, while the nine-point phase totals include checkpoint
and phase overhead. End-to-end process wall time was 1.986 s including
startup and process overhead. The complete run used 20,020 source
callbacks and 160,160 mode evaluations. The largest integration and
matrix exponential timings were below 0.0060 s and 0.0037 s, respectively.
The run stopped at the first full pass without a 512-bit attempt or an
implementation correction. Timing compares this run only.

## Control screen and replay

Apply [controls 12](../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid 02](../../../avoid/02_shape_only_arguments_and_the_controls.md)
to the literal acquisition premises. Euler-factor, weighted-square and
finite-prime-orbit controls fail the complete normalized unshifted source
identity. Canonical coefficients and complete reflection are jointly
required. The reflected quartic, smooth and positive-primitive controls
fail the specified arithmetic expansion and numerical tails. At their
collisions the generic finite approximation can still apply. The
reflected quartic event has \(|x|=\pi/4\) in this height window. The
finite-support fixed-event and atomic finite-profile controls fail
strict Gram positivity through degree 16 when support is too small;
their continuous finite-profile versions fail the literal theta source.
The RH-conditional endpoint controls fail ordinary Dirichlet arithmetic
and retain their conditional status. Altered observation kernels still
permit the same amplitude acquisition but fail the full cosine/Newman
observation premise. The actual-profile positive-measure relaxation
supplies no canonical theta Fourier input. These analytical controls
screen the interpretation without re-integrating control sources.
The certificate supplies finite absolute approximation and nine rounding
enclosures. Signed margins, zero exclusions, growing-height conclusions
and computational scaling require separate results.

The [generator](../numerics/execute_tn6_e02_r1.py) verifies the frozen
request digest and every input byte count and digest before acquisition.
Use Python 3.12 with python-flint 0.9.0 / FLINT 3.6.0 and a new output path
to replay. The script does not require the recorded local executable path.

```sh
python3 papers/investigations-6/numerics/execute_tn6_e02_r1.py \
  --output /tmp/tn6-e02-r1-replay.json
```

The certificate stores Arb midpoint and magnitude radius as exact
dyadic rationals, and outward endpoints as their exact difference and
sum. The generator parses each enclosure and checks rebuilt Arb
containment. A read-only check of the saved record verified all 527
real-ball endpoint triples, positivity, imaginary containment of zero,
exact rational cap and overlap comparisons, and source count totals.
The [compact return](../research-progress/handoffs/TN6-E02-r1-return.md)
records the hashes and scope for E03. This remains a same-worker
execution check pending the separate internal assessment.
