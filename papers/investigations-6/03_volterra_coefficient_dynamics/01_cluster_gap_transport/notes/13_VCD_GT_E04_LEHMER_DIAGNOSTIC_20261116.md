# Complete-source diagnostic on the proposed first Lehmer pair tube

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Explicit helper dispatch
**gpt-6.1-sol / ultra**. Separate backend attestation and the lead's actual
recorded settings are unavailable.

**Floating contour and time diagnostic.** A finite quantitative application
of the conditional contour transfer, with the complete canonical source
specified before execution. The applied source error is a node-level
allowance from the companion proof. See the [frozen request](../research-progress/handoffs/VCD-GT-E04-r1.md),
[Decision04](../brainstorm/notes/04_VCD_GT_B04_CANONICAL_LEHMER_ACQUISITION_20261116.md),
[E08 oracle proof](12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md),
[Note04 transfer](04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md),
[result index](../../../../../result-summaries/README.md) and
[avoid index](../../../../../avoid/README.md), especially
[classification01](../../../../../avoid/01_restating_the_target.md),
[controls02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [numerical scope10](../../../../../avoid/10_numerics_ahead_of_the_question.md).

## Evaluation and error scope

The fixed circle has center \(a=140101/10\) and radius \(\rho=9/10\).
The times lie in \([0,v]\), \(v=1/10\). For \(t>0\), the complete
physical field is approximated at each contour node by the Gaussian
trapezoid sum with spacing \(h\) and \(|r|\le12\). Put
\(s=(1+i(z+2i\sqrt t\,r))/2\). The individual gauged field values use
\[
 \frac{s(s-1)\zeta(s)}{16}
 \exp\!\left(\frac{\pi a}{8}+\log\Gamma(s/2)-\frac{s}{2}\log\pi\right).
\]
At \(t=0\) use the same xi formula directly. Conjugation recovers the lower
semicircle and pairs opposite lattice terms at the two real nodes. Within
each level the \(r=0\) values are reused from \(t=0\). No incomplete zeta
polynomial or exterior inverse-square sum is used.

The fixed levels are 160/224 context bits, Gaussian spacings \(1/3\) and
\(1/4\), circles with 64/128 nodes and time Chebyshev–Lobatto grids with
16/32 subintervals. Python-flint 0.9.0 (FLINT 3.6.0), Python 3.10.0 on
macOS arm64, computes complex and real balls. At positive time, the E08
strip-width-2 source allowances from the infinite lattice and omitted tails
are approximately respectively \(0.142261,4.96112\times10^{-7}\) and
\(9.81\times10^{-45}\) at either level, in units of \(e^{\pi a/8}H_t\).
At time zero the additional lattice allowance is zero. The scalar and
finite quadrature arithmetic uses ball enclosures. Each approximate
normalized field log is anchored at the positive real circle node, then
unwrapped using neighboring ratios. When the sampled modulus floor is
\(m\) and the source allowance is \(\delta<m\), the perturbation of each
anchored log is bounded by \(-2\log(1-\delta/m)\), provided the phase
increments remain separated from the branch cut. This allowance is
propagated through the finite moment, kernel and time rules a second time
using the same field values. Neither ball pass assigns a radius for the
continuous spatial or time quadrature.

The winding test checks the polygon of field values and the winding-zero
polygon for \(H_t(z)/(z-a)^2\). The pair moments and \(K\) use the periodic
log formulas of Decision04 with the circular trapezoid rule. The estimated
pair buffer is \(\rho-|c-a|-\sqrt{|D|}\) for the reconstructed unordered
pair. The polygon winding and the reconstructed buffer are diagnostics for
the sampled problem. Transferring them to the actual analytic circle and
whole real time interval requires separate bounds.

For time quadrature, a Chebyshev polynomial interpolates the measured
\(K\) and is integrated exactly as a polynomial to give the model primitive
\(4\int_t^v K\). Its exponential is evaluated at the same time nodes, then
integrated by Clenshaw–Curtis with the factor 2. The absolute run repeats
these operations on the sampled \(|K|\). All measured \(K\) values are
negative. The time rules pay arithmetic in the finite formulas, including
in the source-padded comparison. The error of replacing the continuous
\(K\) by its interpolant and integrating the exponent by the outer rule
is empirical. The coupled-level differences and the mismatch with the
exact integrating-factor identity do not bound either error.

## Sampled results

| Diagnostic | Coarse | Fine |
| --- | ---: | ---: |
| Sampled polygons with winding two | 17 of 17 | 33 of 33 |
| Minimum gauged sampled modulus | 1,142,295.407 | 1,142,295.407 |
| Maximum neighboring field phase change (radians) | 0.240253 | 0.120209 |
| Maximum neighboring normalized phase change (radians) | 0.080657 | 0.040608 |
| Minimum estimated pair buffer | 0.417522263 | 0.417522263 |
| Maximum relative sampled source allowance | \(1.25\times10^{-7}\) | \(4.35\times10^{-13}\) |
| Largest imaginary component in \(c-a,D,K\) | \(5.45\times10^{-39}\) | \(5.87\times10^{-58}\) |
| \(K\) sampled range, rounded | \([-0.609622120,-0.603774328]\) | \([-0.609622120,-0.603774328]\) |
| Direct \(D(0)\) | 0.001421176730808 | 0.001421176730808 |
| Incoming \(D(v)\) | 0.178736852567582 | 0.178736852567582 |
| \(W(0)\), signed | 0.784574835048330 | 0.784574835048330 |
| \(W(0)\), absolute | 1.274575675038570 | 1.274575675038570 |
| \(B\), signed | 0.177621833068434 | 0.177621833068434 |
| \(B\), absolute | 0.226304207962253 | 0.226304207962253 |
| \(D(v)-B\), signed | 0.001115019499148 | 0.001115019499148 |
| \(D(v)-B\), absolute | −0.047567355394671 | −0.047567355394671 |
| \((D(v)-B)/W(0)\), signed | 0.001421176730808 | 0.001421176730808 |
| Absolute cost and its own weight, same formula | −0.037320150012459 | −0.037320150012459 |
| Absolute cost with the signed \(W(0)\) for comparison | −0.060628194111962 | −0.060628194111962 |

The measured centers at \(0,v\) have offsets \(0.0634308475673\) and
\(0.0597049225291\). They are the same at the displayed precision across
the two levels. The numerical relative-source gate and phase separation
on the sampled polygons pass at both levels. The source-padded radii for
the finite-rule signed margin are \(1.06\times10^{-6}\) and
\(4.22\times10^{-12}\) including arithmetic. They charge the source
allowance through the finite formulas only. On the common time grid the
largest displayed \(K\) difference is \(1.89\times10^{-15}\) and the
\(D\) values round to the same binary64 numbers. Signed transport minus
direct \(D(0)\), computed before display rounding, is about
\(7.00\times10^{-18}\) and \(4.25\times10^{-35}\). It is a consistency
residue for coupled numerical rules.

The two consumers use the same canonical source values and \(D(0)\)
target. Signed transport is normalized by its own \(W(0)>0\) to match
that target. The absolute cost gives a negative weighted margin even when
compared with the signed weight. The direct endpoint rule needs just the
time-zero evaluations (33 and 65 xi calls), already available in the
transport run. Full transport used 36,897 and 196,673 xi calls across the
levels, with 22.55 and 150.66 s measured in xi and 22.65 and 151.15 s
for the two level executions. Contour consumption after source evaluation
took 0.019 and 0.074 s, with another 0.002 and 0.007 s for the time
rules. No Jacobi coefficient family was used. The
[four-call preflight at each precision](../numerics/E04-r1-benchmark.json)
projected 274 s for the fixed source work.

The [small record](../numerics/04_VCD_GT_LEHMER_DIAGNOSTIC_20261116.json)
records the numeric diagnostics. Display midpoints are rounded to
binary64 and the reported radii characterize the original ball arithmetic.
Both complete gauged field grids, before source padding, are retained in
`/private/tmp/vcd-gt-lehmer/E04-r1-{coarse,fine}-fields.json.gz`. Each
serialized real/imaginary ball component is an integer midpoint and radius
at a recorded common decimal exponent. The small record pins each gzip
file and its decompressed bytes. Both hashes and the array shapes were
verified, and replay of the same contour formulas reproduced every
reported sampled \(D,K\). A replay check using
\(k_0+\sum_{k\ge1}|k_k|\) for the padded Chebyshev coefficients also
bounded the finite interpolating polynomial \(K\) above by −0.6034
(coarse) and −0.6035 (fine) on the real time interval. That sign check
concerns the interpolating polynomials.

To regenerate both levels with python-flint 0.9.0, run the
[numerical script](../numerics/vcd_gt_lehmer_diagnostic.py) with
`--cache-dir /private/tmp/vcd-gt-lehmer --output /private/tmp/vcd-gt-lehmer/E04-r1-record.json`.

## Controls and consequence

The same pipeline evaluates exactly specified
\(H_t(z)=(z-a)^2-2(t-1/20)\), with its double time included. Its exact
\(K=0\), \(D(t)=2(t-1/20)\), \(W(0)=1\) and \(B=1/5\) give
\(D(v)-B=-1/10\). This model fails the strict positive passage test in
both computed levels. The largest computed errors in the control
were \(2.58\times10^{-32}\) and \(1.11\times10^{-61}\) in \(D\), and \(1.73\times10^{-26}\) and \(3.56\times10^{-55}\) in \(K\), coarse and fine respectively. This check covers the orientation, the zero pair-gap
and the cost at the polynomial event.

The [control inventory](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [Note04 §4](04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md#4-endpoint-and-control-checks)
provide the analytical premise screen. Euler-factor controls change the
canonical completion. Weighted-square and finite-tail examples change
the reflection/completion or coefficients. Reflected, smooth-shape and
positive-primitive controls lack unchanged integer-square arithmetic.
Finite-prime/head/score controls lack the full canonical identities.
Atomic and finite-profile controls differ from the full theta profile and
threshold eventual simplicity. The RH-conditional endpoint control changes
ordinary Dirichlet arithmetic. Changed observation kernels lack the literal
physical heat equation, while finite-profile relaxations need an actual
analytic field with a counted pair. The named alternative sources receive
no new numerical scans here. The quadratic shares the relevant contour and
heat calculus and still spends its entire incoming gap at the double time.

The observed signed-versus-absolute comparison motivates assessing whether
uniform contour and time allowances fit within the roughly \(0.001115\)
weighted signed margin for this finite tube. Continuous count and
canonical passage remain open.
