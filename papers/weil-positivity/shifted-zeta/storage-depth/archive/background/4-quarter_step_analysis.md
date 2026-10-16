# Crossing the first quarter-step

Research note, 10 September 2026. This continues the [extension analysis](../log7-log8-extension-20260910/extension_analysis.md) and the [cumulative-storage path](../cumulative-path-20260910/cumulative_storage_path.md). All claims use the working normalization and analytic framework of the [Weil-depth v0.3 manuscript](https://github.com/ebbaker/shifted-zeta-positivity/blob/a566944dc1be2899e37fce3d0e857516ced33d8f/papers/weil-depth/manuscript/finite_horizon_weil.tex). The author's normalization verification remains separate. The new arguments and implementation require independent mathematical review.

The quarter-step now has a full-operator certificate at a small positive shift. A separate residual calculation explains why the new-slab complement can be controlled: its cost is small relative to the energy of the proposed continuation, even though a comparison of unrelated worst-case bounds would fail badly.

These are two distinct results. The full-operator certificate uses the paper's existing global head/tail method. The new residual method allows arbitrary new inputs but still restricts the old input to 128 polynomial modes. It has not yet supplied a self-contained recursion on all old inputs.

## 1. The quarter-step and the certified path

Set

\[
a=\log 7,\qquad h=\tfrac14\log(8/7),\qquad
L_q=a+h=1.979292997211443960891938648676\ldots.
\]

The rational ceiling \(L_*=99/50=1.98\) contains this depth. Running the unchanged v0.3 all-input certificate at that ceiling gives

\[
\boxed{Q_{0,L_*}\succeq 10^{-31}I.}\tag{1}
\]

Compression by zero extension gives the same floor for every \(0<L\le L_*\). This is a full form-domain statement, including the infinite-dimensional complement of the retained polynomial head.

The manuscript's bounded generator-change estimate, evaluated at \(L_*\), gives

\[
\|Q_{s,L_*}-Q_{0,L_*}\|\le C_*s^2,
\qquad C_*<16.555621568003036.
\]

At \(s_*=5\times10^{-17}\),

\[
C_*s_*^2<4.13890539200076\times10^{-32}<\tfrac12\,10^{-31}.
\]

Consequently, for every \(L\le L_*\) and \(0\le s\le s_*\),

\[
Q_{s,L}\succeq5\times10^{-32}I.
\]

The energy evolution and its strong zero-shift limit then imply

\[
\boxed{
\|V_{\omega,L}\|\le e^{-5\times10^{-32}\omega},\qquad
0<\omega\le5\times10^{-17},\quad L\le1.98.
}\tag{2}
\]

Writing \(D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L}\), this gives

\[
D_{\omega,L}\succeq\bigl(1-e^{-10^{-31}\omega}\bigr)I.\tag{3}
\]

At \(\omega=s_*\), the displayed storage floor exceeds \(4.99\times10^{-48}\). Its rounded value is \(5\times10^{-48}\), but the exact expression is slightly smaller than that rounded number.

Together with the paper's old-depth interval \(0<\omega\le4\times10^{-15}\), this certifies the whole staircase path

\[
(\log7,4\times10^{-15})
\longrightarrow(\log7,5\times10^{-17})
\longrightarrow(L_q,5\times10^{-17}).\tag{4}
\]

Every intermediate point on both segments is covered. The shift reduction is sufficient; no claim is made that it is necessary or sharp. This is a concrete path segment, not an identified critical curve or an all-depth sequence.

## 2. What this says about cumulative relative coupling

At the quarter-step, use the causal split

\[
V_{\omega,L_q}=\begin{pmatrix}X&0\\Y&Z\end{pmatrix},\qquad
E=I-X^*X,\quad F_{\rm out}=I-ZZ^*.
\]

The diagonal defects are coercive in the shift interval above. The cumulative coupling from the preceding note is

\[
c_D(\omega)=\|F_{\rm out}^{-1/2}YE^{-1/2}\|.
\]

Its Schur complement is

\[
S_D=E-Y^*F_{\rm out}^{-1}Y.
\]

If the full defect is bounded below by \(dI\), minimizing over the new input gives \(S_D\succeq dI\). Since \(E\preceq I\), it follows that \(S_D\succeq dE\). Apply (3) to obtain

\[
\boxed{c_D(\omega)^2\le e^{-10^{-31}\omega}<1,
\qquad 0<\omega\le5\times10^{-17}.}\tag{5}
\]

Thus the path really does preserve cumulative storage and its unrestricted relative coupling. This particular bound is a consequence of the separate full central certificate and the generator estimate; it does not exploit the possibility that cumulative storage survives a negative instantaneous generator.

## 3. The new residual estimate

Now work at zero shift. In the spatial decomposition,

\[
Q_{0,L_q}=\begin{pmatrix}A&B^*\\B&F\end{pmatrix},\qquad
A=Q_{0,a},\quad F=Q^\gamma_{0,h}.
\]

The new diagonal block is purely gamma because \(h<\log2\). Let \(\mathcal U_{128}\) be the polynomials of degree at most 127 on the old interval, expressed in its orthonormal shifted Legendre basis.

Choose a continuation \(J:\mathcal U_{128}\to\mathcal W_{32}\), where \(\mathcal W_{32}\) is the new-slab polynomial space of degree at most 31. The proposed matrix is the Galerkin minimizer \(-F_{32}^{-1}B_{32}\), rounded to exact decimal rational coefficients. Define the actual continuation energy and its full residual by

\[
H_J=A+B^*J+J^*B+J^*FJ,\qquad R=B+FJ.\tag{6}
\]

All operators here are restricted only on the old input side. In particular, \(R\) takes values in the entire new \(L^2\) space, and \(F\) is the unrestricted new-slab operator.

Completing the square gives the exact identity

\[
\boxed{S=A-B^*F^{-1}B=H_J-R^*F^{-1}R.}\tag{7}
\]

The calculation proves

\[
\boxed{
R^*F^{-1}R\preceq0.004\,H_J,
\qquad S\succeq0.996\,H_J,
}\tag{8}
\]

and, in a separate guarded matrix test,

\[
\boxed{S\succeq10^{-8}A\quad\hbox{on }\mathcal U_{128}.}\tag{9}
\]

Therefore the central form is coercive on

\[
\mathcal U_{128}\oplus\mathcal D(F^{1/2}).\tag{10}
\]

The new input in (10) is arbitrary in the full gamma form domain. There is no new-input cutoff in this conclusion. Although \(J\) uses 32 modes, every correction to that continuation is covered by (7)–(9).

### Why the energy used for the residual matters

The following values are numerical diagnostics; the rounded inequalities (8)–(9) are the enclosed sign certificates:

| Quantity | Diagnostic value |
|---|---:|
| Smallest continuation energy relative to old energy | \(1.27068099025\times10^{-7}\) |
| Largest residual penalty relative to old energy | \(3.33284235720\times10^{-3}\) |
| Largest residual penalty relative to continuation energy | \(3.35287397777\times10^{-3}\) |

Here “residual penalty” denotes the sufficient bound \(R^*R/f_0\), where \(F\succeq f_0I\).

Comparing the second row with the first would fail by a factor exceeding 26,000. They concern different directions. The third row keeps the direction of the residual aligned with the continuation energy, and it is below 0.004. Thus unrestricted optimization of the new input costs less than 0.4% of the proposed continuation's energy in every old direction retained here.

This is the useful progress toward recursion: a small margin relative to the old energy can coexist with a manageable residual relative to the remaining energy.

## 4. A full new-slab coercivity estimate

The residual bound uses the stronger short-slab estimate

\[
\boxed{F\succeq f_0I,\qquad f_0>1.73617237627376657.}\tag{11}
\]

For completeness, write

\[
G_0(t)=e^{t/2}\frac{t}{\sinh t}-4t\cosh(t/2)
=1+\sum_{j\ge1}g_jt^j,\qquad g_1=-\tfrac72,
\]

and \(\ell_h=\gamma+\log(2\pi h)\). In the unit new coordinate \(v\), the gamma row sum is

\[
(F1)(v)=-\ell_h-\tfrac12\log(v(1-v))
-\tfrac12\sum_{j\ge1}\frac{g_jh^j}{j}
\bigl(v^j+(1-v)^j\bigr).\tag{12}
\]

The interval calculation establishes \(G_0(t)>0\) throughout \([0,h]\). Consequently the off-diagonal kernel of \(F\) is negative. On a smooth core the ground-state identity reads

\[
F[g]=\int_0^1(F1)(v)|g(v)|^2\,dv
+\frac14\int_0^1\!\int_0^1
\frac{G_0(h|u-v|)}{|u-v|}|g(u)-g(v)|^2\,du\,dv.
\]

Its second term is nonnegative. Using \(v(1-v)\le1/4\), the exact linear term, and \(v^j+(1-v)^j\le1\) gives

\[
f_0\ge-\ell_h+\log2+\frac{7h}{4}
-\frac12\sum_{j=2}^{M}\frac{|g_j|h^j}{j}
-\frac{128(h/3)^{M+1}}{(M+1)(1-h/3)}.\tag{13}
\]

The radius-3 profile bound from v0.3 controls the last term. The identity and lower bound extend by closure to the full form domain. Since \(F^{-1}\preceq f_0^{-1}I\), it suffices to bound the full residual Gram \(R^*R\).

## 5. Keeping all residual output, including endpoint terms

The central cross operator in physical coordinates is

\[
(Bf)(t)=\int_0^a q(a+t-y)f(y)\,dy
-\sum_{n\in\{2,3,4,5,7\}}\frac{\Lambda(n)}{\sqrt n}
f(a+t-\log n),\qquad 0<t<h,
\]

where

\[
q(s)=e^{s/2}-\frac{e^{-5s/2}}{1-e^{-2s}}
=-\frac{G_0(s)}{2s}.
\]

In particular, the new-prime term is \(-\log7\,f(t)/\sqrt7\). The gamma and arithmetic contributions remain combined in the residual and its Gram; they are not bounded separately there.

Let \(r=h/a\) and write the unit old input polynomial as \(\phi(u)\). The singular part of the normalized new output is exactly

\[
-\frac{\sqrt r}{2}\left[
\phi(1+rv)\log\frac{v+a/h}{v}-H_\phi(1+rv)
\right],\tag{14}
\]

where

\[
H_\phi(z)=\int_0^1\frac{\phi(z)-\phi(u)}{z-u}\,du
\]

is a polynomial. The smooth profile contributes ordinary polynomial terms after truncation, and the arithmetic translations of \(\phi\) are exact polynomials. Applying \(F\) to a polynomial continuation adds polynomial multiples of \(\log v\) and \(\log(1-v)\). Hence the model residual has the form

\[
\widetilde Rf(v)=p_f(v)+l_f(v)\log v+r_f(v)\log(1-v).\tag{15}
\]

All products in its Gram are integrated with exact polynomial/logarithmic moments, enclosed by Arb. No new-output modes are discarded.

The coefficient of \(\log v\) at the joining endpoint is

\[
\tfrac12\bigl(\sqrt{h/a}\,\phi(1)-(J\phi)(0)\bigr)
\]

in the normalized coordinates. Boundary matching would cancel this leading term. It was not imposed in this calculation: the endpoint terms are retained explicitly and their full norms are included. The certificate therefore does not depend on assuming endpoint cancellation.

To control the analytic approximation, set

\[
\eta_M(L)=\frac{256(L/3)^{M+1}}{(M+1)(1-L/3)}.
\]

The expansion of \(\log(v+a/h)\) through degree \(T\) has uniform remainder at most

\[
\frac{r^{T+1}}{(T+1)(1-r)}.
\]

For normalized Legendre inputs, the coefficients of their continuations beyond the endpoint are

\[
\phi_i(1+rv)=\sqrt{2i+1}
\sum_{k=0}^i\binom{i}{k}\binom{i+k}{k}r^kv^k.
\]

These positive coefficients give a direct bound on the old-to-new continuation norm used with the logarithm remainder. Together with the profile bounds, the code obtains

\[
\|R-\widetilde R\|\le\delta,
\quad
\delta\le\eta_M(a+h)+\text{logarithm error}
+\eta_M(h)\|J\|.
\]

If \(G=\widetilde R^*\widetilde R\), then

\[
R^*R\preceq G+
\bigl(2\delta\sqrt{\operatorname{tr}G}+\delta^2\bigr)I.\tag{16}
\]

The model continuation energy differs from \(H_J\) by at most
\(\eta_M(a+h)(1+\|J\|^2)I\). A Frobenius bound is used for \(\|J\|\). These budgets, and the old-block profile error in (9), are subtracted before the positive-pivot LDL tests. The certificate is therefore about the true operators in the working normalization, not just the truncated profile.

## 6. What was checked

The primary residual run uses 128 old modes, 32 continuation modes, profile degree 320, logarithm degree 80, and 6144-bit Arb arithmetic. Its residual-output operator error is below \(2.477\times10^{-58}\). The three guarded checks—Schur positivity, (8), and (9)—all pass.

A replay with profile degree 340, logarithm degree 90, and 6656-bit arithmetic passes the same inequalities, with residual-output error below \(5.693\times10^{-62}\). Both runs reconstruct a rational continuation and save all its coefficients. A smaller 32-old/8-continuation calculation also passes, with residual factor 0.006.

Independent numerical checks compare the residual representation with the original gamma kernel and compare the complete Gram with direct quadrature on a smaller example. The respective errors are below \(4.15\times10^{-36}\) and \(3.09\times10^{-84}\). These are cross-checks, not positivity certificates or an independent normalization audit.

The separate full-operator certificate (1) uses the unchanged reference implementation with 256 retained modes, profile degree 260, and 3072-bit arithmetic. Its analytic tail floor exceeds 0.56716. Both reflection sectors pass after subtracting the complete head/tail model-error budget, which is below \(9.187\times10^{-43}\). Positive LDL pivots establish the required sign; their magnitudes are not claimed as spectral floors. The floor \(10^{-31}\) is the value explicitly tested by the full head/tail criterion.

The saved reference result contains the validation bounds and pivots. Replaying its wrapper rebuilds the matrices; a separate copy of those large raw matrices was not saved. The unchanged reference source, helper sources, exact continuation coefficients, parameters, and result hashes are included or referenced in this packet's audit trail.

## 7. A full central coupling bound, obtained afterwards

One can also turn (1) into a conservative unrestricted central relative bound at the split. The arithmetic source windows for \(n=2,3,4,5,7\) are pairwise disjoint at this quarter-step. Their combined cross-operator norm is therefore

\[
\left(\sum_n\frac{\Lambda(n)^2}{n}\right)^{1/2}.
\]

The singular gamma term has norm at most \(\pi/2\), and the smooth term has norm at most \(K_*\sqrt{ah}/2\). Thus

\[
\|B\|\le b<3.676127660640516,\qquad
B^*F^{-1}B\preceq tI,\quad t=b^2/f_0<7.783740118207815.
\]

The full certificate implies \(S\succeq mI\), where \(m=10^{-31}\). Since \(A=S+B^*F^{-1}B\),

\[
S\succeq\frac{m}{m+t}A,
\qquad
1-\|F^{-1/2}BA^{-1/2}\|^2
\ge\frac{m}{m+t}>10^{-32}.\tag{17}
\]

This is an a posteriori consequence of the global certificate. Using it to justify that same certificate recursively would be circular. The much larger finite-old relative margins in Section 3 do not automatically apply to unrestricted old inputs.

An additional arithmetic estimate, unused in these certificates, gives a joint row-sum bound below 2.92624 at depth 1.98, compared with the reference method's sum of separate delay-chain bounds 3.12926. It may improve later tail estimates, but no improvement to (1) is claimed from it here.

## 8. What the next recursive inequality should preserve

For any coercive continuation energy \(H_J\), the natural residual parameter is

\[
\theta=\|F^{-1/2}R H_J^{-1/2}\|^2.
\]

The exact residual identity gives

\[
\theta<1\quad\Longrightarrow\quad
S\succeq(1-\theta)H_J.\tag{18}
\]

At a positive shift, the same algebra applies to the bounded Cayley-storage blocks from the cumulative-path note, provided their diagonal forms and \(H_J\) are coercive. It would then certify cumulative storage directly. Thus a prospective depth–shift path should preserve both a positive continuation energy and a residual factor below one, measured in that energy. A small old-energy margin alone is an incomplete measure of how difficult the extension is.

The quarter-step supplies a full successful step and a concrete central instance of (18) with all new directions controlled. What remains for a reusable recursion is to extend the residual estimate across the old complement, including its interaction with the retained old space, without recertifying the entire enlarged operator from the beginning. A direct positive-shift version would also address the cumulative regime beyond instantaneous generator positivity.

The mixed-space central result (10) alone does not imply transfer contraction on those initial inputs: the shift evolution can move their old components outside \(\mathcal U_{128}\). The positive-shift conclusion in Section 1 uses the separate unrestricted central certificate precisely to avoid this gap.

No unrestricted result at \(\omega=10^{-11}\), no completion of the remaining three quarters to \(\log8\), and no proof that an iterative path reaches unbounded depths are established here. The demonstrated step is a finite-horizon advance within the current proof framework.
