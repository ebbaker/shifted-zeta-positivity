# Uniform signed gap enclosure on the fixed Lehmer tube

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Helper dispatch explicitly set
**gpt-6.1-sol / ultra**. Separate backend attestation and the lead's actual
recorded settings are unavailable.

**Certified local enclosure; accepted within scope by [E05 r6](../reviews/08_VCD_GT_CANONICAL_GAP_CERTIFICATE_ASSESSMENT_20261116.md).** This post-assessment status update leaves the assessed mathematics and numerical bounds unchanged. For the fixed
circle \(|z-a|=9/10\), \(a=140101/10\), and real time \(0\le t\le1/10\),
the replay encloses two zeros inside \(|z-a|<3/4\) throughout and gives a
strict positive lower bound on their pair coordinate \(D(t)\). The signed
margin uses a uniform upper bound for the exact drift, yielding an exact
time-cost bound. This is the finite test selected by
[B05](../brainstorm/notes/05_VCD_GT_B05_UNIFORM_SIGNED_CERTIFICATION_20261116.md)
and the [E04-r2 request](../research-progress/handoffs/VCD-GT-E04-r2.md).
See [results](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[avoid](../../../../../avoid/README.md) and its
[classification01](../../../../../avoid/01_restating_the_target.md),
[control premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## Source and cell computation

The only canonical data are the hash-checked fine field array from the
[E04-r1 diagnostic](13_VCD_GT_E04_LEHMER_DIAGNOSTIC_20261116.md). It contains
33 Chebyshev–Lobatto times and 128 circle values at each, before the
[Note12 source allowance](12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md), in
the gauge \(G=e^{\pi a/8}H_t\). The tensor field \(P\) keeps Fourier powers
0 through 32 and time degree 32. Each recorded decimal midpoint is an
exact rational input, its reconstruction and further coefficient
arithmetic enclosed with Arb. The Euclidean norm of the two archived
component radii gives a bound on sample displacement from that midpoint.
Together with the original lattice and tail error this feeds the analytic
interpolation budget of [Note14 §2](14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md#2-fixed-tensor-polynomial).
The resulting \(\sup|G-P|<0.03124\) holds for the entire disk
\(|z-a|\le21/20\) and real interval. This bound includes source error,
spatial aliasing and discarded terms, and real-time Chebyshev interpolation
of the true field. It uses the auxiliary spatial majorant on radius five
and the heat equation for the true field. The archive comparison from r1
supplies zero terms of this error budget.

For implementation let \(w=z-a\) and \(x=20t-1\). On each circle, the
normalized polynomial \(\sigma P/w^2\) is a sum of Chebyshev time
polynomials times angular factors \(e^{i(n-2)\theta}\). At each angular
node the absolute time derivative in \(x\) is bounded by the sum of
\(k^2\) times absolute Chebyshev coefficient bounds. The full circle
angular derivative bound uses \(|n-2|\) times the absolute coefficient
bounds with their radial powers. Thus evaluating at the midpoint and adding
half-width times the relevant derivative bound covers each time cell and,
for the geometry check, each angular arc. The derivative bounds apply to
\(P\). The exact field is separately covered by the disk error divided
by the square of the evaluation radius. Geometry uses this combined disk
error directly to lower-bound real parts and upper-bound moduli. When
computing a complex log, a rectangular ball adds the disk radius to each
component. Conjugation of the exact field covers the reflected half of
each circle and combines reflected terms in the contour means.

The sign \(\sigma=+1\) passed the two full circular boundaries at radii
\(3/4,21/20\) using 16 time cells and 64 angular arcs each. Their true
normalized real parts are above \(1{,}060{,}683\) and \(1{,}160{,}688\),
respectively. The argument principle then gives count two at both
boundaries and zero zeros in the collar. The analytic principal log of
\(G/w^2\) is available on the annulus by the real-part minimum principle.
A fixed real centering constant gives modulus bounds below \(1.737\) for
the centered log on each boundary. [Note14 §3](14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md#3-count-collar-and-centered-log).

The 128-node moment and kernel means pay their annular trapezoid tails
using those true-field log bounds. Each time cell first encloses both
moments and uses their real interval coordinates directly in
\(Q=(w-(c-a))^2-D\) and the exact drift kernel. Across all 512 cells,
\(|Q|>0.29708118\) on the inner and \(|Q|>0.80112371\) on the outer
boundary. Each target-node interval denominator also excludes zero.
The separate absolute allowances for the two moment formulas are below
\(5.014\times10^{-9}\) and \(1.048\times10^{-8}\). The corresponding \(K\)
allowance is below \(1.877\times10^{-8}\) in every time cell, in addition to
the direct propagation of field and coordinate uncertainty through the
finite quadrature. The resulting aggregate drift enclosure is
\[
 -0.615518848 \le K(t)\le -0.599329616
 \quad (0\le t\le 1/10).
\]
The enclosures pay uncertainty throughout each closed time cell. Neither
time integration nor root-slope estimates enter this part of the proof.
[Note14 §4](14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md#4-angular-tails-and-interval-coordinates).

## Matched endpoint comparison

The direct \(D(0)\) and incoming \(D(v)\) use the two actual archived rows
on the same 128-node contour, carrying the sampled source error at their
scale before tensor amplification. At \(t=0\) the archive uses direct xi
with zero lattice error. The same true-field annular moment tails apply.
The record also includes the two looser tensor endpoint enclosures.
Outward-rounded intervals for the direct rows are
\[
 \begin{aligned}
 D(0)&\in[0.00142117117778,\,0.00142118228384],\\
 D(v)&\in[0.17873684703288,\,0.17873685810228].
 \end{aligned}
\]
With the fixed \(k_U=-59/100\), the formula
\(B_U=(e^{4k_U v}-1)/(2k_U)\) gives
\(B_U<0.178151971243388\) and \(W(0)\le e^{4k_Uv}<0.789780673932803\).
The positive signed margin exceeds \(0.0005848757894980\), and division by
the weight upper bound gives a lower bound \(0.0007405546993009\) for
\(D(0)\). The exact signed cost from any later \(t\) to \(v\) is at
most the cost from zero, and \(0<W(t)\le1\) since \(K<0\). Thus the
weighted margin also lower-bounds \(D(t)\) throughout the tube, where
the two zeros are distinct and real. The separate absolute cost is at least \(1/5\),
which exceeds \(D(v)\) by more than \(0.02126314189772\). This tests the
absolute-cost comparison for this tube. The direct endpoint concludes
positivity with a stronger lower bound and uses the full shared endpoint
source values.

## Control and replay

The same proof path for the exact polynomial \(w^2-2(t-1/20)\) passes both
collar checks. On the 512-cell partition the returned \(K\) interval
contains zero and the cost interval contains \(1/5\). The interval gap at
the double time contains zero. Using the lower cost from the uniform
lower drift bound and the upper incoming gap gives a margin below
\(-0.09993\), so this control fails the strict passage test. The other
controls retain the premise verdicts of [Note12 §6](12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md#6-scope-and-control-screen)
and [Note14 §5](14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md#5-certificate-outputs-and-exact-control).
In particular the Euler-factor completion is changed, weighted-square
coefficients and full reflection are unavailable together, and the
reflected, smooth and positive-primitive sources lack the unchanged theta
square arithmetic. The local contour calculus alone does not discriminate
those colliding sources.

The [code](../numerics/vcd_gt_lehmer_certificate.py) uses 224-bit
Arb/acb via python-flint 0.9.0, FLINT 3.6.0, Python 3.10.0 on macOS arm64.
The six-cell preflight took about 0.004 s and projected under 11 s if all
prescribed time partitions were attempted. The tensor stage took about
0.15 s and the complete run about 0.86 s, including both the canonical
and quadratic time partitions. Canonical xi calls were zero. The
[record](../numerics/05_VCD_GT_LEHMER_CERTIFICATE_20261116.json) pins the
source input and program hashes, exact ball output, caps, realized cells
and measured runtime. Replay with `--cache-dir /private/tmp/vcd-gt-lehmer`
and `--output` pointing at a new JSON record. The loader also checks the
branch's `numerics-archives/` or its mirror under `VCD_GT_ARCHIVES` and
requires both gzip and decompressed-content hashes. A missing or corrupt
archive fails closed. The result concerns the one fixed two-zero tube.
