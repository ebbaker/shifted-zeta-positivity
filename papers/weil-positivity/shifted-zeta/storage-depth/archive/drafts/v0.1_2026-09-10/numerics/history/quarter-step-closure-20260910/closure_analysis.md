# The quarter-step old-complement gap is closed

Research note, 10 September 2026. This continues the [quarter-step analysis](../quarter-step-20260910/quarter_step_analysis.md), using the working normalization of the [Weil-depth v0.3 manuscript](https://github.com/ebbaker/shifted-zeta-positivity/blob/a566944dc1be2899e37fce3d0e857516ced33d8f/papers/weil-depth/manuscript/finite_horizon_weil.tex). The author's normalization verification remains separate. The analytic deductions and computer-assisted certificates are research results requiring independent review.

For this quarter-step, the residual inequality now covers the full old form domain. Both infinite-dimensional input complements, and their coupling to the retained modes, are controlled. The proof uses a spatial head/complement construction and does not assume the earlier global certificate at depth 1.98.

## 1. The full-domain result

Let

\[
a=\log7,\qquad h=\tfrac14\log(8/7),\qquad
L_q=a+h=1.97929299721144396089\ldots,
\]

and write

\[
Q_{0,L_q}=\begin{pmatrix}A&B^*\\B&F\end{pmatrix}.
\]

Keep the exact rational continuation from the preceding packet and extend it to every old input by

\[
J=J_{128,32}P_{128}.
\]

Thus it uses the original 128 old polynomial coefficients to propose 32 new polynomial coefficients, and vanishes on the old orthogonal complement. Define

\[
H_J=A+B^*J+J^*B+J^*FJ,\qquad R=B+FJ.
\]

The new certificate proves

\[
\boxed{R^*F^{-1}R\preceq0.9H_J}\tag{1}
\]

on the **entire old form domain**, with \(H_J\) coercive. Completing the square therefore gives

\[
\boxed{
S=A-B^*F^{-1}B
=H_J-R^*F^{-1}R
\succeq0.1H_J.
}\tag{2}
\]

The new input eliminated by \(F^{-1}\) is unrestricted. The constants 0.9 and 0.1 are exact rational certificate thresholds, not rounded floating-point eigenvalue estimates.

The preceding factor 0.004 remains a stronger statement on the original 128-mode old space. It has not been promoted to an all-old bound. The new uniform factor is 0.9.

## 2. An inequality that carries the energy through the step

The result also gives a bound on the complete enlarged form. For arbitrary admissible old and new inputs \(f,g\), write \(g=Jf+v\). Then

\[
Q_{0,L_q}[f,g]=H_J[f]+2\operatorname{Re}\langle Rf,v\rangle+F[v].
\]

Equation (1) bounds the cross pairing by
\(\sqrt{0.9}\,H_J[f]^{1/2}F[v]^{1/2}\). Hence

\[
\boxed{
Q_{0,L_q}[f,g]
\ge(1-\sqrt{0.9})\bigl(H_J[f]+F[g-Jf]\bigr)
\ge0.05\bigl(H_J[f]+F[g-Jf]\bigr).
}\tag{3}
\]

This is the desired finite-step inequality in continuation coordinates. It identifies the energy carried by the old input and the cost of departing from its proposed continuation.

The carried old metric is \(H_J\). It can be much smaller than the preceding metric \(A\) in critical directions. Thus (2) preserves at least 10% of the candidate continuation energy; it does not promise 10% of the original old energy. Controlling how \(H_J\) changes at later depths remains part of an eventual path argument.

## 3. How the omitted inputs were controlled

The verification head contains 256 old polynomial modes and 32 new modes. The proposed continuation itself remains the original 128-to-32 map. Everything outside this 288-dimensional verification head is handled analytically.

Two estimates made this possible. First, a positive piecewise-constant Schur weight bounds the full combined arithmetic operator by

\[
\|T_{L_q}\|<1.949177212012646.
\]

The earlier sum of individual delay-chain bounds was above 3.12. The new bound retains the way the arithmetic shifts interact. It applies to all inputs, because it is a pointwise weighted row inequality for the continuum operator. A separate verification checks all 2,152 intervals on which any shifted weight can change.

Second, orthogonality of the old tail permits integration by parts in the smooth gamma cross kernel. Its bound is reduced to approximately 0.001289 at 256 old modes. The singular cross kernel retains its Carleman bound \(\pi/2\).

Combining the local gamma tail floors and the joint arithmetic bound gives:

| Quantity | Enclosed bound, displayed approximately |
|---|---:|
| Old gamma tail floor, 256 modes | 3.7145175783 |
| New gamma tail floor, 32 modes | 5.7344638966 |
| Gamma cross norm upper bound | 1.5720851019 |
| Combined arithmetic norm upper bound | 1.9491772121 |
| Full joint complement floor | 0.9067586427 |

The complement includes old-tail/new-tail coupling. Its coupling back into the verification head is computed from **complete output Grams**, with no output cutoff. The signed gamma and arithmetic contributions, including endpoint logarithms and translated support windows, remain combined in those Grams.

At the original 128-plus-32 verification split, the complement floor was already positive, above 0.33467, but the final sufficient sign test failed. Enlarging the old verification space both raises the complement floor and accounts explicitly for the additional old modes' coupling. The failed first attempt is retained in the packet; it is not a negative witness for the true form.

## 4. The direct relative test is not circular

The identity alone would not justify (1). To prove it, the calculation tests the more strongly coupled form

\[
M_{0.9}=\begin{pmatrix}
H_J&R^*/\sqrt{0.9}\\
R/\sqrt{0.9}&F
\end{pmatrix}.
\]

Its full-domain positivity implies (1) by its own Schur complement. No new-depth coercivity result is assumed in this argument.

The graph change of coordinates is the identity on the joint complement, so the modified complement can still be bounded explicitly. Its certified floor exceeds

\[
0.7616605490419337.
\]

Separate old and new output Grams determine the complete leakage from the head into this complement after the graph transformation and cross-block enlargement. The guarded finite Schur test for \(M_{0.9}\) passes all 288 pivots. Its total analytic error budget is below

\[
6.253\times10^{-53}.
\]

The proof, including the transformation of the two leakage Grams and its error estimates, is given in the [spatial complement lemma](spatial_complement_lemma.md). The direct residual validator reads the matrix archive, not the separate full-coercivity sign result.

## 5. The step also supplies its own positive-shift path

A separate sign test on the same spatial decomposition certifies the explicit floor

\[
\boxed{Q_{0,L_q}\succeq10^{-33}I.}\tag{4}
\]

This test includes both complements and all their interaction with the head. Its final analytic error budget is below \(1.026\times10^{-55}\). Positive LDL pivots establish the required sign; their magnitudes are not being used as spectral floors. The value \(10^{-33}\) is explicitly inserted into the full head/complement inequality before verification.

The manuscript's generator-change estimate has constant
\(C_{L_q}<16.536113848659\). Therefore

\[
Q_{s,L}\succeq5\times10^{-34}I,
\qquad L\le L_q,\quad0\le s\le5\times10^{-18}.
\]

The energy evolution gives

\[
\boxed{
\|V_{\omega,L}\|\le e^{-5\times10^{-34}\omega}<1,
\qquad L\le L_q,\quad0<\omega\le5\times10^{-18}.
}\tag{5}
\]

In particular, the whole depth segment from \(\log7\) to \(L_q\) is covered at the indicated positive shifts. The cumulative defect satisfies

\[
D_{\omega,L}\succeq(1-e^{-10^{-33}\omega})I.
\]

The unrestricted cumulative relative coupling at the spatial split consequently obeys

\[
c_D(\omega)^2\le e^{-10^{-33}\omega}<1.
\]

These are consequences of the new spatial certificate alone. The preceding packet's stronger small-shift interval, obtained with the global method, remains a separate result. Equation (1) is a central-form residual statement; its factor 0.9 has not been transferred directly to the positive-shift Cayley-storage metric.

## 6. Evidence and remaining scope

The main construction uses profile degree 320, logarithm-series degree 100, and 6144-bit Arb arithmetic. The full spatial matrix archive contains the head matrix and separate old/new output Grams as midpoint/radius balls. Source hashes, exact continuation coefficients, parameters, all final pivots, and analytic error budgets are recorded. The full 256-plus-32 construction took about 21 minutes in this environment; subsequent relative tests reuse its archive.

Independent checks compare the new formulas with direct quadrature and the original cross-block construction:

| Check | Maximum discrepancy |
|---|---:|
| Complete old-output cross and adjoint Grams versus quadrature | \(<1.63\times10^{-54}\) |
| Adjoint gamma cross output versus the original kernel | \(<8.96\times10^{-50}\) |
| Exterior-log moments versus quadrature | \(<1.67\times10^{-65}\) |
| Adjoint projection versus the original cross block | \(<6.12\times10^{-910}\) |

The quadrature checks are consistency checks; the positivity claims come from the guarded Arb sign certificates and their analytic reductions. This packet does not claim a second independent full reconstruction of the 256-plus-32 matrices or an independent normalization audit.

The finite quarter-step gap is now closed. The remaining research problem is to repeat and control this construction at subsequent depths: choose the next continuation, keep its candidate energy positive, and certify a full residual factor below one. No estimate here guarantees that the verification dimensions remain manageable, that step lengths avoid accumulation at finite depth, or that the path reaches unbounded horizons. The unrestricted cumulative regime at shift \(10^{-11}\) also remains open.

See the [README](README.md) for reproduction commands and the [direct all-old result](relative_256_32.json), [spatial coercivity result](closure_256_32.json), and [positive-shift corollary](path_corollary.json) for the machine-readable records.
