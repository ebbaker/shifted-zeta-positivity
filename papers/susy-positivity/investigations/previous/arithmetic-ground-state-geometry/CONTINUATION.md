# Continue from the boundary response and the arithmetic sign tests

13 September 2026. Read [note 20](notes/20_ARITHMETIC_SIGN_AND_BOUNDARY_RESPONSE.md), [STATUS.md](STATUS.md), and the **live** manuscript, especially sections 10 and 14–15. [Note 19](notes/19_JOINT_RESPONSE_AND_FINITE_RANK_DEFECT.md) supplies the complete source construction; [note 18](notes/18_REVIEW_AND_NEUMANN_COMPARISON.md) supplies its independent high-sector cutoff. The [coverage map](MANUSCRIPT_COVERAGE.md) locates the earlier results. Historical notes, exact records and [dated drafts](archive/drafts/README.md) are preserved.

The objective is an analytical route to full Weil positivity on arbitrary compact support. A theorem proving the required sign separately for every support length would suffice. A physically compatible system across all envelopes is a separate, stronger construction task. Do not assume RH, fit zeros, or take an unknown positive square root of the complete target.

## 1. Preserve the exact unresolved criterion

On the full zero-extension logarithmic form domain, the known source satisfies
\[
\|\Phi_Lf\|^2=Q_L[f]+\langle P_Nf,D_NP_Nf\rangle,
\qquad D_N>0.
\]
With the note 19 notation,
\[
A^*A=W_L+\alpha I,\quad
\alpha=e^D+c_{\mathcal S}-w_0,\quad
T_H=(A|_Q)^*(A|_Q),\quad V=T_H^{-1},
\]
\[
H=T_H-\alpha I\ge\delta I,\quad
B=QW_LP,\quad M=PTP,\quad
G=Z^*Z=M-B^*VB,
\]
\[
Z=(I-\Pi_H)A|_{PX},\qquad
D_N=\alpha I+B^*(H^{-1}-V)B,
\]
\[
Q_L\ge0\quad\Longleftrightarrow\quad
S_N=G-D_N=PW_LP-B^*H^{-1}B\ge0.
\]
The source is a positive **completion**, not a positivity proof. All mixed terms, the unused output \(Zp\), the finite-rank error, and every active prime return remain present. At fixed \(L,P\), changing the remote delay or adding inactive primes changes the reference shift but not \(S_N\). The construction also applies to negative non-arithmetic targets.

The physical cap is still an isometric tensor label in these channels. Its metric does not supply the ordering. Keep the exact physical chiral-equation identification explicitly conditional wherever the metric-selection theorem is used.

## 2. New proved structure: the gamma mixed block is a boundary response

Write
\[
W_L=T_L+w_0I+P_L^{\rm pole}-J_L^{\rm off},\quad
b(s)=\sum_{k\ge0}\frac2{a_k}\frac{s}{a_k^2+s},\quad a_k=2k+\tfrac12.
\]
The constants, poles, distances \(m\log p\), and weights \((\log p)p^{-m/2}\) are the genuine arithmetic data. The remaining source/block calculus is generic.

After translating the interval to \((0,L)\), note 20 proves
\[
T_L=b(H_{\rm N})+\mathcal K_L,
\qquad \mathcal K_L\ge0\text{ bounded},\qquad
\|\mathcal K_L\|_{\rm ess}=\pi/2.
\]
Its mass summands are
\[
\mathcal K_a=
\frac{u_au_a^*+v_av_a^*+e^{-aL}(u_av_a^*+v_au_a^*)}{1-e^{-2aL}},
\quad u_a=e^{-ax},\quad v_a=e^{-a(L-x)}.
\]
The sum is strong, **not** operator-norm convergence. Every finite mass tail still has norm at least \(\pi/2\), even after finite-codimension compression. Do not treat this boundary term as compact.

The form domain is exactly \(\operatorname{Dom}b(H_{\rm N})^{1/2}\), and the operator domain is exactly \(\operatorname{Dom}b(H_{\rm N})\). Finite cosine sums form an operator core. These identities concern the input domain; they do not impose new boundary conditions on the gamma fields.

For \(e_j(x)=\nu_j\cos(j\pi x/L)\), \(\nu_0=L^{-1/2}\), \(\nu_j=\sqrt{2/L}\) for \(j>0\), the columns are explicit:
\[
\mathcal K_a e_j=\frac{\nu_ja}{a^2+(j\pi/L)^2}(u_a+(-1)^jv_a).
\]
For \(\mathcal K^{(J)}=\sum_{k<J}\mathcal K_{a_k}\),
\[
\|(\mathcal K_L-\mathcal K^{(J)})P_N\|
\le\sqrt{\frac{2(2N-1)}L}(a_J^{-1/2}+a_J^{-3/2})\longrightarrow0.
\]
Thus the **finite-input** version survives. The complete mixed block is
\[
B=Q\mathcal K_LP+QP_L^{\rm pole}P-QJ_L^{\rm off}P.
\]
Do not replace its square by the sum of three separate squares.

## 3. Strongest surviving route and its precise missing lemma

Use the existing cutoff bound
\[
W_L\ge b(H_{\rm N})-\beta_LI,
\quad d_j=b((j\pi/L)^2)-\beta_L\ge\delta>0\quad(j\ge N).
\]
At length one, the existing rational choice \(N=4,\delta=1/16\) remains available; it is only a high-sector certificate.

Let \(P_{N,K}\) project onto cosine modes \(N,\ldots,K-1\). Solve the **positive high-sector** finite problem
\[
(P_{N,K}HP_{N,K})Y_K=P_{N,K}B,
\qquad R_K=B-HY_K.
\]
The residual has only modes \(j\ge K\), and note 20 proves
\[
\boxed{\quad S_N\ge PW_LP-B^*Y_K-d_K^{-1}R_K^*R_K.\quad}
\]
This controls the infinite inverse response; it does not drop it. The general residual identity, a sharper diagonal-weighted tail, mass-column bounds and propagation of norm enclosure errors are in note 20, section 4.

**Missing lemma B:** derive an analytical rule \(K=K(L)\) and prove the right side, including all enclosure allowances, is nonnegative for every required \(L\). This is an independently checkable sufficient inequality at fixed parameters, but its all-length arithmetic sign is unproved. The generic residual identity does not explain why it should hold. Prove a signed cancellation involving the actual prime translations and boundary columns, or find a rigorous obstruction to a specific proposed cancellation.

At a fixed length with strictly positive \(S_N\), finite Galerkin certificates converge and eventually succeed. This is a conditional completeness statement, not a positivity theorem; it need not hold as a finite certificate on an exact null direction. Do not spend the next continuation merely improving high-sector iteration or running a large sweep.

## 4. Other routes and exact failure tests

Note 20 develops four substantially different approaches: ordered response with one-sided tails, the selected mixed-response estimate, a physical contraction/intertwining law, and the prime-discrepancy form.

The ordered inverse truncation
\[
F_\ell=\sum_{j=0}^{\ell}\alpha^jV^{j+1}
\]
is a **lower** bound for \(H^{-1}\). Hence \(PW_LP-B^*F_\ell B\) is an upper bound for \(S_N\). A rational counterexample exists for every finite order: a positive truncated Schur matrix can coexist with a negative exact target. Keep compressed resolvents and translations in order; even the symmetrized product of two positive matrices can be indefinite.

A physical contraction carrying \(Zp\) to a known vector of Gram \(D_N\) would force the ordering, but abstract existence of that contraction is exactly equivalent to \(G\ge D_N\). It must be derived from independent gluing data, including an arithmetic intertwining identity and the complementary output. A unit cap alone supplies no such identity.

The exact discrepancy formulation uses
\[
E(r)=\sum_{p^m\le e^r}\log p-e^r+1,\quad
h_f(r)=\operatorname{Re}\langle E_Lf,U_rE_Lf\rangle,
\]
\[
Q_L[f]=K_{\ge1}[E_Lf]+(4+w_0)\|f\|^2
-2\int_0^Le^{-r/2}h_f(r)\,dE(r).
\]
The lowest gamma response has been canceled **exactly** against the pole and density terms; it was not discarded. Derivative integration by parts is asserted only on the smooth core.

Replacing the prime measure by \(e^rdr\), with all archimedean data unchanged, gives a negative form already at \(L=2\): the unit cosine satisfies
\[
Q_2^{\rm dens}[\cos(\pi x/2)]<-2979/6125.
\]
The proof controls the entire higher-mass tower. This excludes a density-only mechanism or harmless removal of the discrepancy. It does not exclude more informative signed prime-counting arguments. The exact required discrepancy inequality for every input is a restatement of Weil positivity and must not be advertised as a new lemma proving it.

## 5. Arbitrary support and physical compatibility

A theorem proving \(S_{N_j,L_j}\ge0\) for a cofinal sequence \(L_j\to\infty\) suffices, by zero extension of the complete form. Dimensions, trial sizes, high gaps and precision may all vary with \(L_j\). No fixed dimension, uniform positive full-form gap or all-prime physical source is needed for this logical implication.

The separate physical task is a compatible family of exact sources across all envelopes. Note 19 only constructs compatible restrictions inside one fixed envelope, with its error retained. Rebuilt errors need not agree. All earlier no-go results keep their stated hypotheses; no claim excluding every physical gluing or every compact correction has been added.

## 6. Recording and validation

Ten standard-library programs replay **59** labelled exact checks. The previous 49 records are unchanged; ten new checks cover independent Green-kernel algebra, parity columns, counterexamples, mixed residuals, shift cancellation and rational density-obstruction bounds. They do not certify the analytical arguments or the arithmetic sign.

Continue in a new numbered note; update the report and status. Integrate mature results into the live manuscript only with a new dated draft snapshot, rebuild, visual review and updated build record. Refresh and replay the manifest using [validation/README.md](validation/README.md). Follow [ARCHIVES.md](ARCHIVES.md) and the root [LARGE_FILES.md](../../../../../LARGE_FILES.md). This pass produced no large data or arithmetic positivity sweep.
