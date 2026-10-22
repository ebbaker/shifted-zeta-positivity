# Actual regular theta fiber comparison

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified from this research turn's metadata.

**Status: one actual regular theta fiber enclosed with outward ball
arithmetic; native boundary interval strictly contained in native direct
interval at the declared accuracy target.** The implementation comparison
uses t=0 and |z-35|<=8, with exactly two certified simple branches. It uses
neither RH nor hypothetical collision parameters. A single-machine timing
advantage is scoped to the stated algorithms, oracle, meshes and disk;
the equally informed direct method may reuse the boundary identity.
There is no intrinsic method ordering or endpoint exclusion.

The [receipt][record], [replay script][script], [fixed contract][fixed]
and [separate same-model internal review][review] hold the finite evidence.
Use the [result index][results], [avoid index][avoid],
[control register][controls], [criterion classification][a01],
[matched controls][a02], [scope rule][a07] and [coupled estimates][a12].
This is an acquisition/enclosure comparison for [Note 03][previous],
not a new simplicity criterion.

## 1. Fixed geometry and objective

The contract was fixed before consumer energy runs, following initial
geometry feasibility probes: physical heat time t=0, base disk
Omega={|z-C|<R}, C=35, R=8, differential omega=dz/w on w²=H_0(z).
The complete energy is E=2 integral_Omega |H_0|^(-1)dA. Simple branches
are regular points of the cover and contribute to this full energy.

Both native consumers receive the same certified source Taylor oracle,
root balls, unit chart and 160-bit arithmetic. The stopping target is a
complete interval of diameter at most 25% of its positive midpoint.
Boundary levels are 512,1024,2048,4096 half-circle cells, with the same
number of regularized transverse cells. Direct levels are square grids
32,64,128,256 in nonsingular cover coordinates. The first passing level
is used; failed earlier levels remain charged. Record the common setup,
consumer-only and fresh total times, as well as unit-evaluation counts.
No floating convergence difference pays a quadrature error.

## 2. The complete canonical source and actual branches

Use the exact identity
\[
 H_0(z)=\frac18\xi\left(\frac{1+iz}{2}\right),\qquad
 \xi(s)=\frac{s(s-1)}2\pi^{-s/2}\Gamma(s/2)\zeta(s).
                                                               \tag{1}
\]
[Rodgers–Tao, Introduction (1)–(3)][rt] equates (1) with the unchanged
canonical theta-source integral and its reflection normalization. This
source identity is an imported classical input. The computation uses
Arb gamma/zeta series and scalar balls; it does not replace the source by
a finite zero list or a separately reflected mode head. [Python-flint's
acb documentation][flint] specifies rectangular complex enclosures.

The replay certifies winding number exactly two on |z-35|=8. It covers
every angular arc by a complex rectangle whose H_0 image excludes zero,
and sums enclosed endpoint argument increments. Convex image rectangles
pay the arc-to-chord homotopy; positive real part of each endpoint ratio
fixes the short phase increment. The winding interval isolates integer 2.
The recorded full-boundary field floor is greater than 6.6759e-7.

Exact rational real sign brackets and independent local Rouché estimates
give the two simple real roots
\[
 \alpha\simeq28.26945028346938758091450396712,\qquad
 \beta\simeq42.04407927754310998525695918780.                \tag{2}
\]
Their proof brackets, derivative floors and Rouché margins are in the
receipt. Together with count two, they exhaust the disk's zeros. Their
outer radius balls are about 8.28e-30 and 1.66e-29; displayed decimal
root approximations alone are not the certificate.

Thus V(z)=H_0(z)/[(z-alpha)(z-beta)] is holomorphic and nonvanishing
on the closed disk. Paid 512-cell boundary unit ranges give a whole-disk
floor |V|>5.1459e-8 and upper |V|<8.1965e-6, by maximum principles for
V and 1/V. Those ranges avoid the nonpositive real axis. Normalize log V
real at z=43, where V>0. The imaginary harmonic part of log V agrees
with the continuous principal boundary argument and stays between -pi
and pi by the maximum principle. Hence b=V^(-1/2), positive on the real
interval, is a coherent holomorphic branch. This is a newly acquired
regular-fiber chart, not Note 01's event-conditioned curvature chart.

## 3. Source approximation and all cell errors

For u>=0 each canonical summand has the positive factor
2 pi n² exp(4u)-3>0. The positive complete source therefore implies |H_0(C+zeta)|<=M on |zeta|<=16,
where M=H_0(-16i)=H_0(16i), because |cos(x+iy)|<=cosh(y).
The exact canonical evaluation gives M<0.255277. Set N=65 and compute
the degree-64 Taylor polynomial P at C with all coefficient balls retained.
The series cap is explicitly 65. With rho=8/16 and d=1-rho, Cauchy's
coefficient estimates pay the complete omitted analytic tail:
\[
 \epsilon_H=M\rho^N/d,
\]
\[
 \epsilon_{H'}=(M/16)\rho^{N-1}(N/d+\rho/d^2),
\]
\[
 \epsilon_V=\frac{M}{2\cdot16^2}\rho^{N-2}
 \left[\frac{N(N-1)}d+\frac{2N\rho}{d^2}
                         +\frac{2\rho^2}{d^3}\right].    \tag{3}
\]
Numerically epsilon_H<1.384e-20 and epsilon_V<4.641e-19.
Double synthetic divided difference gives Q=P[alpha,beta,z]. Since
H_0(alpha)=H_0(beta)=0, the exact unit is H_0[alpha,beta,z]. The
simplex formula bounds their difference by epsilon_V, the uniform
second-derivative tail divided by two. Root uncertainties enter the
synthetic coefficients as balls; no division by a near-zero root factor
is used in a branch cell.

For efficient range evaluation on a cell, use the second Taylor polynomial
of Q at that rectangle's midpoint z_0. If delta=z-z_0, add a disk error
M_3,poly |delta|³/6, where
\[
 M_{3,\rm poly}=\sum_{k\ge3}k(k-1)(k-2)|Q_k|9^{k-3}.
                                                               \tag{4}
\]
Here Q_k are coefficients in powers of z-C. The rectangle is checked
to stay within |z-C|<=9, and polynomial point
values/derivatives retain all coefficient balls. Add epsilon_V once for
the actual physical points |z-C|<=8. Rectangular supersets can extend
outside the physical disk; the polynomial remainder is paid on radius 9,
while the source remainder is asserted only on the physical subset.
This range oracle is not an analytic quadrature callback on arbitrary
complex neighborhoods. Unresolved finite bounds, unit zeros or branch
cuts cause failure rather than skipped cells.

All computations use python-flint 0.9.0, FLINT 3.6.0, at 160 bits. Arb
outward rounding pays coefficient, root, elementary-function, measure,
polynomial and source-tail errors. Multiplying a complete cell range by
its enclosed measure pays its quadrature error. The resulting widths
are dominated by cell range and primitive propagation, not by an
unreported floating truncation estimate.

## 4. Two complete native consumers

Put m=(alpha+beta)/2, a=(beta-alpha)/2 and y_0²=(z-alpha)(z-beta),
with y_0(43)>0. Reflection and the positive real unit give q=iQ, Q>0,
and real p<0 along the plus-to-minus transverse path through beta.
The phase rotation in Note 03 is therefore lambda=1 exactly.

On the plus outer boundary z=C+8 exp(i theta), set
\[
 B(\theta)=\frac{8i e^{i\theta}b(z)}
 {(z-m)\sqrt{1-a^2/(z-m)^2}},\quad
 v(\theta)=\int_0^\theta\operatorname{Re}B(s)ds.
\]
The square root near 1 is coherent since |z-m|>a. Conjugation gives
B(2pi-theta)=-conj B(theta), hence
\[
 Q=2\int_0^\pi\operatorname{Im}B\,d\theta,\quad
 R_{\rm ext}=4\int_0^\pi v\operatorname{Im}B\,d\theta,
 \quad E=-Qp+R_{\rm ext}.                                \tag{5}
\]
If B_j encloses a whole cell of width h, its prefix v_j is the sum of
all previous h Re B_k, and the within-cell primitive is enclosed by
v_j+[0,h] Re B_j. This pays every cumulative primitive and mixed
product uncertainty. Q and R_ext use the same outer ranges; their
correlation is conservatively relaxed when adding their intervals.

With u_0=arcosh((43-m)/a), the regular transverse integral is
\[
 p=-2u_0\int_0^1 b(m+a\cosh(u_0t))dt.                    \tag{6}
\]
No singular endpoint is omitted. The real cut payment is -Qp/2 and
the full physical-boundary payment is -Qp/2+R_ext.

The direct comparator uses exactly the same root/unit oracle. Let delta=m-C,
\[
 U(\theta)=\operatorname{arcosh}
 \frac{-\delta\cos\theta+\sqrt{64+(a^2-\delta^2)\sin^2\theta}}a.
\]
The cover map z=m+a cosh(s+i theta), -U<=s<=U, retains both branches
and sheets. Its nonsingular full-energy formula, including its Jacobian,
is
\[
 E=4\int_0^\pi\int_0^1
 \frac{U(\theta)}{|V(m+a\cosh(tU(\theta)+i\theta))|}
 \,dt\,d\theta.                                         \tag{7}
\]
The factor four uses s and conjugation symmetries. Every cell includes
uncertain roots, shifted boundary extent, coordinate map and unit errors.
There is no interior H floor, root exclusion disk or omitted branch cap.

## 5. Certified intervals and measured implementation comparison

| Native consumer | Mesh | Complete energy interval | Relative diameter | Target |
| --- | --- | --- | --- | --- |
| Boundary | 512 | [25,887,815.641027, 36,647,942.875403] | 34.4127% | Not yet |
| Boundary | 1024 | [28,770,927.163097, 33,752,291.350598] | 15.9344% | Pass |
| Direct | 32² | [26,240,287.008854, 44,252,411.258855] | 51.1035% | Not yet |
| Direct | 64² | [28,728,270.232214, 34,655,897.029090] | 18.7038% | Pass |

These are outward rounded summaries of the exact rational endpoints in
the receipt. The boundary interval is strictly inside the native direct
interval. Its exterior correction is strictly negative on this disk,
with a complete interval approximately [-5.87525e6,-2.98802e6]. This
is a local acquired sign, not a uniform arithmetic simplicity premise.

The timed common source/root/count/unit acquisition was 1.273027 s. Including the failed earlier levels, the boundary consumer used 3,072 unit evaluations and 0.268675 s; direct used 5,120 and 0.536675 s. The direct/boundary consumer ratio was 1.99749. Adding the same common setup gave 1.541702 s versus 1.809702 s, a ratio of 1.17383. These are the final settled-code replay measurements, not portable speed constants.

Fresh acquisition time here means the timed common setup plus native
consumer passes. It excludes interpreter startup, imports and receipt
serialization. All failed earlier meshes are included in the consumer
totals; no best-of-repeated-run statistic is used.

Both methods receive the same shared setup, including the global branch
chart. Direct absolute-energy integration alone could omit some branch
work or use another acquisition scheme. No minimal-cost claim is made.
After the boundary observations are shared, direct evaluation may use (5)
or intersect the native intervals. Its equally informed final interval
then inherits the boundary improvement. The measured native speed and
width gain therefore do not prove intrinsic Hodge superiority.

The recorded interval signs are replayed from actual balls. Hashes identify
the scripts and fixed contract, not the truth of a mathematical assertion.
Timings are machine dependent and are not required to reproduce exactly.
The arithmetic outputs should replay in the recorded environment; another
environment must rerun every sign, branch, width and containment test.

## 6. Controls and continuation

The quadratic and neighboring-root controls still retain ordinary-double
energy degeneration. Euler factors change canonical arithmetic;
weighted-square/finite-prime controls fail complete normalized reflection
and unchanged full coefficients; reflected/primitive controls lack the
canonical square sequence. Their preservation lists remain separate.
No identity in (5)–(7) rejects those controls at a collision. A finite
collision-free control box can correctly pass the same computation.

This result establishes useful finite acquisition on one unchanged theta
fiber, and an implementation-specific gain for the stated native boundary
consumer. It does not control t down to a hypothetical collision, every
height, higher multiplicities or a simple off-line zero. RHE-05 remains
gated. The next bounded task is to separate source setup and reusable
boundary acquisition from the consumer cost, then choose one declared
accuracy or reuse objective; a broad height/time sweep is not implied.

[previous]: 03_REAL_PRIMITIVE_REDUCTION_AND_BOUNDED_MODEL_REMAINDER_20261022.md
[record]: ../numerics/03_ACTUAL_THETA_COMPARISON_20261022.json
[script]: ../numerics/03_compare_actual_theta_fiber_20261022.py
[fixed]: ../numerics/03_ACTUAL_THETA_COMPARISON_CONTRACT_20261022.md
[review]: ../reviews/03_ACTUAL_THETA_FIBER_COMPARISON_REVIEW_20261022.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[rt]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D4B85BA067E2D5A71D87E4FFB0D21E46/S2050508620000062a.pdf/the-de-bruijn-newman-constant-is-non-negative.pdf
[flint]: https://python-flint.readthedocs.io/en/latest/acb.html
