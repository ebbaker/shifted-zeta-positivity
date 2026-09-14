# Cumulative storage for the log 7 to log 8 extension

Working research, 10 September 2026. This uses the [Weil-depth v0.3 normalization](https://github.com/ebbaker/shifted-zeta-positivity/blob/a566944dc1be2899e37fce3d0e857516ced33d8f/papers/weil-depth/manuscript/finite_horizon_weil.tex) while the author's normalization verification proceeds separately. It continues the [cumulative-path note](../cumulative-path-20260910/cumulative_storage_path.md). Analytic deductions and the error proofs await independent review.

The extension is highly sensitive to cancellation. A rigorous central test-pair bound shows that its full relative coupling squared exceeds (1-1.84\times10^{-17}). The new slab itself admits a uniform full-operator contraction bound throughout (0<\omega\le1/2). The natural next estimate is therefore a bound on the residual of a proposed continuation, with the gamma and arithmetic contributions kept together.

No unrestricted contraction theorem at total depth (\log8) is established in this packet. The positive cumulative results below concern finite-dimensional input spaces, with **all output retained**.

## 1. The spatial split and the finite-input calculation

Set

\[
a=\log7,\qquad L=\log8,\qquad h=L-a=\log(8/7)<\log2.
\]

At positive shift, write

\[
V_{\omega,L}=\begin{pmatrix}X&0\\Y&Z\end{pmatrix},
\quad X=V_{\omega,a},\quad Z=V^\gamma_{\omega,h}.
\]

The new diagonal block has no arithmetic delays. The full transfer on (L) includes (n=1,\ldots,7), including the mixed-prime term (n=6). The delay (\log7=a) sends the initial interval ((0,h)) into the entire new slab.

Let (\mathcal U_N\subset L^2(0,a)) and (\mathcal W_M\subset L^2(0,h)) be polynomial spaces in orthonormal shifted Legendre bases. The code computes the full output Gram matrix on their direct sum:

\[
G_{ij}=\langle V f_j,V f_i\rangle_{L^2(0,L)},\qquad D_{N,M}=I-G.
\]

It also integrates the old inputs' output on ((0,a)). Consequently it can form, on these finite input spaces,

\[
E_N=I-X_N^*X_N,\quad F_M=I-Z_M^*Z_M,
\quad R_{N,M}=Y_N^*Z_M,
\]

where the outputs of (X_N,Y_N,Z_M) are **not** projected. Eliminating the new input gives the exact finite-input Schur expression

\[
S_{N,M}=E_N-W_{N,M},\qquad
W_{N,M}=Y_N^*Y_N+R_{N,M}F_M^{-1}R_{N,M}^*.
\]

The reported diagnostic is

\[
c_{N,M}^2=\lambda_{\max}
\big(E_N^{-1/2}W_{N,M}E_N^{-1/2}\big).
\]

If the unrestricted diagonal defects are coercive, (c_{N,M}\le c_{\rm full}): restricting the old input and the optimizing new input cannot increase the supremum. Thus a value below one does not provide the upper bound on full coupling that the proof needs. At (\omega=10^{-11}), unrestricted old-depth contractivity is itself not yet certified, so the numerical quantity is described only as finite-input coupling.

## 2. Central geometry: the new delay participates in cancellation

The central cross block has a particularly explicit form. For an old input (f), measured in physical coordinates, and (0<t<h),

\[
(B_0f)(t)=\int_0^a q(a+t-y)f(y)\,dy
-\sum_{n\in\{2,3,4,5,7\}}\frac{\Lambda(n)}{\sqrt n}f(a+t-\log n),
\]

where

\[
q(s)=e^{s/2}-\frac{e^{-5s/2}}{1-e^{-2s}}
=-\frac{G_0(s)}{2s}.
\]

Every displayed argument of (f) is in the old interval. In particular, the new-prime term is simply

\[
-\frac{\log7}{\sqrt7}f(t).
\]

This is not a small extra leakage term in the central storage metric. It cancels a substantial contribution already present in the rest of the cross block.

The central calculation uses exact polynomial moments. After reflecting the old coordinate, the singular kernel is (1/(au+hv)). Its moments satisfy

\[
\int_0^1\!\int_0^1\frac{u^k v^j}{au+hv}\,du\,dv
=\frac{I_j(a,h)+I_k(h,a)}{j+k+1},
\quad I_j(c,d)=\int_0^1\frac{t^j}{c+dt}\,dt.
\]

The identity follows by integrating the divergence of

\[
\left(\frac{u^{k+1}v^j}{au+hv},\frac{u^kv^{j+1}}{au+hv}\right).
\]

The smooth profile and the translated arithmetic polynomials then use ordinary polynomial moments. The exact threshold (\log7=a) is handled symbolically, rather than by a numerically uncertain subtraction.

The finite central diagnostics are:

| Old modes | New modes | (1-c_{N,M}^2) |
|---:|---:|---:|
| 32 | 8 | (3.97492493435\times10^{-10}) |
| 64 | 16 | (8.16574978342\times10^{-16}) |
| 128 | 32 | (1.83945352171\times10^{-17}) |

They are not converged estimates of the full slack. The increase in input spaces exposes more nearly critical directions.

At 128 old and 32 new modes, the component norms in the **same** central storage metrics are approximately:

| Cross contribution | Relative norm |
|---|---:|
| Complete gamma-plus-arithmetic block | (0.9999999999999999908) |
| Gamma alone | (2.1554\times10^{13}) |
| Arithmetic alone | (2.1554\times10^{13}) |
| New (\log7) term alone | (4.0228\times10^6) |
| Everything except that new term | (4.0228\times10^6) |

The component values are finite-input diagnostics. Their significance is the scale of cancellation: a triangle inequality across these pieces cannot prove a relative norm below one.

### A bound on the full central coupling

The strongest central singular directions were rounded to exact rational Legendre coefficients. For those test functions (x,y), the code encloses their two diagonal energies and their cross pairing, including the analytic profile error. Cauchy's inequality in the actual storage spaces gives

\[
c_{\rm full}^2\ge
\frac{|\langle y,B_0x\rangle|^2}{Q_{0,a}[x]\,Q^\gamma_{0,h}[y]}.
\]

The diagonal metrics exist by the v0.3 old-depth coercivity and the small-slab bound proved below. The enclosed result implies

\[
\boxed{c_{\rm full}^2>1-1.84\times10^{-17}.}
\]

Equivalently, any positive full central slack is smaller than (1.84\times10^{-17}). This bound does **not** prove (c_{\rm full}<1). The rational vectors, error parameters, and bound are saved in `central_128_32.json`; an increased-degree, increased-precision replay is saved separately. Both runs also certify positivity of the central form on the retained 160-dimensional input space after subtracting the operator profile error.

## 3. A uniform full-operator bound on the new slab

There is a comparatively simple result for the new diagonal block:

\[
\boxed{\|Z\|=\|V^\gamma_{\omega,h}\|\le e^{-0.06\omega},
\qquad 0<\omega\le\tfrac12.}
\]

Consequently,

\[
I-Z^*Z\succeq(1-e^{-0.12\omega})I,
\qquad I-ZZ^*\succeq(1-e^{-0.12\omega})I.
\]

After division by (2\omega), the lower bound is uniformly greater than (0.058) on this entire interval. This estimate controls the new storage inverse without restricting the new input to polynomials. In the zero-shift limit it also proves (Q^\gamma_{0,h}\succeq0.06I).

**Proof and interval verification.** In the notation of the preceding packet,

\[
\kappa^\gamma_\omega(t)=\frac{(2\pi)^\omega}{\Gamma(\omega)}t^{\omega-1}
\left(1+\sum_{j\ge1}G_j(\omega)t^j\right).
\]

The analytic profile is positive on (0\le t\le h), uniformly for (0\le\omega\le1/2). A degree-64 interval calculation, with the previously proved radius-3 Cauchy remainder, bounds it below by (0.4935). Thus Young's inequality bounds the transfer norm by the actual integral of this positive kernel.

Put

\[
J(\omega)=\sum_{j\ge1}\frac{G_j(\omega)h^j}{j+\omega}.
\]

The kernel integral is

\[
z(\omega)=\frac{(2\pi h)^\omega}{\Gamma(1+\omega)}(1+\omega J(\omega)).
\]

The gamma product gives

\[
(\log\Gamma)''(1+\omega)
=\sum_{n=0}^\infty\frac1{(n+1+\omega)^2}
\ge\frac{\pi^2}{2}-4
\]

on this shift range. Integrating twice, and using (\log(1+t)\le t), gives

\[
\frac{\log z(\omega)}{\omega}
\le\log(2\pi h)+\gamma
-\left(\frac{\pi^2}{4}-2\right)\omega+J(\omega).
\]

The right side is bounded above by (-0.0600528746) using 50 closed shift intervals of width (0.01), 768-bit Arb arithmetic, and the analytic profile remainder. The exact coefficient (G_1=-7/2) is used to avoid interval dependency in that term. This proves the rounded (-0.06) bound. No division by an interval containing zero is needed.

The interval data and proof checks are in `new_slab_bound.json`. Direct pointwise bounds at (4\times10^{-15},10^{-11},10^{-7}) are also saved there.

By causal compression, the same uniform norm bound applies to every shorter new slab. Thus reducing the depth step does not require a new diagonal-block argument.

## 4. Cumulative extension results

The cumulative calculation checks positivity of the full-output defect on each retained input space by Arb LDL factorization, after subtracting the analytic squared-norm error. For complex inputs the same Hermitian positive matrix controls all complex coefficient vectors.

At the certified reference shift (4\times10^{-15}), both the 32+8 and the 64+16 input spaces pass. The latter has finite coupling diagnostic

\[
1-c_{64,16}^2\approx8.165749783422688\times10^{-16}.
\]

Its effective old Schur minimum, divided by (2\omega), is approximately (6.54865\times10^{-31}). These eigenvalue and coupling values are diagnostics; the separately reported LDL positivity includes the full profile error.

The larger calculation at (\omega=10^{-11}) also passes on the direct sum of 128 old and 32 new polynomial modes. Its diagnostics are

\[
1-c_{128,32}^2\approx1.839453521711687\times10^{-17},
\qquad \lambda_{\min}(S_{128,32})/(2\omega)
\approx4.200466226186427\times10^{-33}.
\]

This 160-dimensional input space contains the degree-126 old-slab polynomial from the earlier negative-generator certificate, extended by zero into the new slab. Compression preserves that polynomial's generator value. Therefore, on this same input space at total depth (\log8\) and shift (10^{-11}\), cumulative contraction holds while instantaneous-generator positivity fails. This extends the earlier one-vector comparison to positivity on an entire input subspace. It still does not control the omitted input directions.

The run uses profile degree 280 and 6144-bit Arb arithmetic. Its full transfer error is below (7.109\times10^{-54}), and the finite-input squared-norm error subtracted before LDL factorization is below (1.799\times10^{-52}). These figures and the source hashes are recorded in `extension_128_32_1em11.json`.

On the 32+8 space, increasing the shift from (4\times10^{-15}) to (10^{-7}) changes the relative slack from approximately

\[
3.97492493435063\times10^{-10}
\quad\hbox{to}\quad
3.97492447282261\times10^{-10}.
\]

Both finite-input positivity checks pass. This small comparison does not show a useful gain from increasing shift. It does not establish shift monotonicity, and these fixed polynomial spaces are not fixed spaces in the Cayley coordinates. It would be premature to infer a critical curve from them.

### Varying the depth increment

Keeping the old depth (a=\log7) and the input dimensions 128+32 fixed, smaller first steps give much larger finite central slack:

| First-step length | Finite central slack diagnostic | Proved lower bound for that finite slack |
|---|---:|---:|
| (\tfrac14\log(8/7)) | (1.27068099025\times10^{-7}) | (10^{-7}) |
| (\tfrac12\log(8/7)) | (1.77992803192\times10^{-11}) | (10^{-11}) |
| (\log(8/7)) | (1.83945352171\times10^{-17}) | (10^{-17}) |

The last column includes the analytic profile error. For its stated value (\eta), the code proves positivity of the finite block

\[
\begin{pmatrix}(1-\eta)A_N&B_{N,M}^*\\B_{N,M}&F_M\end{pmatrix}.
\]

Its Schur complement gives (1-c_{N,M}^2>\eta). The factorization subtracts both the full profile error and (\eta) times the old-block profile error. These are finite-input upper bounds on coupling, not bounds on unrestricted coupling.

This is concrete support for adapting the depth increment to the available relative storage. The quarter-step is a more favorable first target for a full residual estimate than the entire jump. It has not been certified on unrestricted inputs, and its success would not yet establish the three remaining quarter-steps. The new diagonal bound already applies to it by compression.

## 5. A residual inequality for the missing new-input directions

The new-slab bound makes a more structured continuation test possible. Write the **scaled full defect** as

\[
\frac{I-V^*V}{2\omega}
=\begin{pmatrix}A&C^*\\C&F\end{pmatrix},
\qquad F=\frac{I-Z^*Z}{2\omega}\succeq f_\omega I,
\quad f_\omega=\frac{1-e^{-0.12\omega}}{2\omega}>0.058.
\]

Here (A=(I-X^*X-Y^*Y)/(2\omega)) and (C=-Z^*Y/(2\omega)). This (A) is the upper-left block of the enlarged defect, not the old defect by itself.

Let (J) be a proposed bounded operator extending an old input to a new input. Define its energy and its stationarity residual by

\[
H_J=A+C^*J+J^*C+J^*FJ,
\qquad R_J=C+FJ.
\]

Completing the square proves the exact identity

\[
\boxed{S=A-C^*F^{-1}C=H_J-R_J^*F^{-1}R_J.}
\]

Therefore, for a bounded coercive old reference metric (E\),

\[
H_J\succeq\eta E,\qquad
\|R_JE^{-1/2}\|^2<f_\omega\eta
\quad\Longrightarrow\quad S\succ0.
\]

The conclusion is a positive multiple of (E). This inequality evaluates the combined arithmetic-plus-gamma continuation before paying for its error. The error enters quadratically as a residual, instead of through separately enormous component norms.

For a Galerkin continuation (J_M\) taking values in the retained new-input space, solve its projected stationarity equation

\[
\Pi_M(C+FJ_M)=0.
\]

Its remaining residual lies entirely in the omitted new-input directions. This makes the next missing bound explicit:

\[
\|(I-\Pi_M)(C+FJ_M)E^{-1/2}\|.
\]

Neither this full residual norm nor the omitted old-input contribution has been enclosed here. A positive finite matrix does not control either one. The central slack scale suggests why preserving structure matters: a candidate energy with relative margin of order (10^{-17}) requires a relative residual amplitude of order (10^{-9}), using the new-slab floor, rather than allowing a triangle inequality among components of size (10^{13}). This is a scale illustration, not a proved error budget for the cumulative extension.

## 6. Full-output construction and validation

In the global coordinate (u=x/L), an old polynomial input is represented as its polynomial continuation minus the same continuation cut off at (a/L). A new input starts at (a/L). Causality then gives ordinary delayed polynomial fractional-power outputs. Because (h<\log2), the cutoff correction has only its gamma term; its delay coincides exactly with the new (n=7) arithmetic delay. The implementation combines those terms before forming the Gram matrix.

Every output pair is integrated with the enclosed fractional-power moments from the preceding packet. The transfer-profile error is a full operator norm bound (\delta), not an estimate on sampled outputs. For the retained orthonormal inputs, if (G) is the model Gram matrix, then

\[
\|D_{\rm exact}-D_{\rm model}\|
\le2\delta\sqrt{\operatorname{tr}G}+\delta^2.
\]

The positive factorization subtracts this error times the identity. The finite-input certificate therefore does not rely on the unvalidated eigenvalue diagnostics.

Independent checks compare the central constant cross form against direct integration of the original kernel, and the quarter-shift piecewise-constant full output Gram matrix against direct quadrature. Their discrepancies are below (4\times10^{-48}) and (3\times10^{-66}), respectively. The central coupling lower witness was replayed at larger degree and precision.

The next proof task is to certify the combined continuation residual in Section 5 and then control the old-input complement. Even a successful unrestricted log 8 extension would remain a finite-depth result; an all-depth path still requires steps with divergent total depth while the shift tends to zero.
