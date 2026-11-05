# RGD-B03 r2: the exact payment fails, while the true coefficient tail decays

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6-astra (Codex), effort ultra**,
research chat0004, thread 01a1a7c1-13a2-7371-8010-b0ace507476e,
turn 01a1a7c1-f46e-7771-80f4-f28b810aa0bc.

**Disposition: bounded B03 r2 attempt complete, with a proved scoped
obstruction and a worked alternative.** Proof-author checking and
read-only same-model analytical contributions only; separate E04
assessment is pending. No numerical experiment, integration, new moment
acquisition or certificate was performed.

The unchanged compact-reference, independent primitive-moment Taylor
payment satisfies
\[
L_{r,k}=q^*_{r,k}-\mathcal R_{r,k}<0
\quad\hbox{for every fixed }r\ge2\hbox{ and all sufficiently large }k.
\tag{1}
\]
This concerns the **exact collected payment**, not merely Note05's upper
bound for it. It says nothing negative about the canonical determinant.

Removing the spatial cutoff repairs the source error: an explicit
relative coefficient bound tends to zero as
\(128\exp[-j/(16\log j)]\). But every fixed finite-mode reference retaining
the exact boundary has infinitely many nonreal zeros and therefore cannot
supply all-order reference positivity. These findings motivate the
separately classified [B02 full-source repair][repair]. That repair has a
conditional joint-order contour theorem, not an acquired theta range.

Read the [result index][results], [theta cluster][theta], [controls][controls]
and [avoid index][avoid], especially [reformulations][a01],
[scoped exclusions][a07], [numerical scope][a10], [known-baseline checks][a11]
and [joint signed estimates][a12]. The [sole progress register][progress]
owns status. [Packet10][request] remains the frozen request.

## 1. The attempted induction and what must propagate

Retain complete canonical theta at physical time zero, ordinary
coefficients, negative-index zeros, and \(b=1/16\):
\[
c_j=b\delta_{j0}+\frac18(d_{j-1}-d_j),\qquad
D_{n,k}=\det[c_{k+j-i}]_{i,j=0}^{n-1}.
\]
All Green endpoint contributions remain present. The consumer is
\[
Q_{r,k}=D_{r,k}^2-D_{r,k-1}D_{r,k+1}
       =D_{r+1,k}D_{r-1,k}.
\tag{2}
\]

The principal attempt is a reference comparison with quantitative
conditioning. Its proposed input package \(H_r\) consists of an
independently specified coefficient reference, positive reference
bounds \(m_{n,k}\le D_{n,k}(c^*)\) and condition bounds
\(H_{n,k}(c^*)/D_{n,k}(c^*)\le K_{n,k}\) for orders \(n\le r\),
complete residual bounds, and the already justified actual lower-order
signs. A step must obtain the next **reference** margin and condition
bound independently, pay the complete error, and retain the information
for reuse. It may not assume the wanted canonical next-order sign.

This is a proposed stronger comparison package, not an acquired
invariant or a new RH criterion. Note05 supplies its exact product-error
consumer: for positive reference determinants \(d_\pm\) of orders
\(r+1,r-1\), and relative perturbation bounds \(e_\pm\),
\[
|Q_{r,k}-d_+d_-|
 \le d_+d_-(e_++e_-+e_+e_-).
\tag{3}
\]
The nonlinear product is essential. The reference signs and conditioning
are separate obligations. Sections 2–4 show why the selected fixed
references cannot furnish this package globally.

## 2. Failure of the exact old Taylor payment

Use exactly Note05's \(U=2\) definitions:
\[
a_j=\frac1{8(2j)!}\int_0^Uu^{2j}p_1(u)\,du,\quad
C_j(z)=b\delta_{j0}+a_{j-1}-a_j+z_{j-1}-z_j,
\]
with negative indices zero, \(c_j^*=C_j(0)\), and
\[
P_{r,k}(z)=D_{r+1,k}(C(z))D_{r-1,k}(C(z)).
\]
This is the already combined polynomial, of degree at most \(2r\).
Write
\[
P_{r,k}(z)-P_{r,k}(0)=\sum_{\alpha\ne0}p_\alpha z^\alpha,\quad
\mathcal R_{r,k}=\sum_{\alpha\ne0}|p_\alpha|T^\alpha,\quad
T_j=E_j+B_j(2).
\]
Put
\[
a=16\pi-1,\qquad K=\frac{e^{-4\pi}}{8(1-e^{-5\pi})},
\qquad E_j=K/a^{2j+1}.
\tag{4}
\]

For every \(r\ge2,k\ge1\),
\[
[z_{k-1}^{2r}]P_{r,k}=1.
\tag{5}
\]
Indeed, retain only the homogeneous linear contribution of \(z_{k-1}=t\).
The only nonzero coefficient changes are \(C_{k-1}=-t,\ C_k=t\).
The index-\(k\), order-\(n\) matrix is lower bidiagonal with diagonal
\(t\) and subdiagonal \(-t\), so its determinant is \(t^n\).
The product of orders \(r+1,r-1\) is \(t^{2r}\); lower-degree terms
cannot change this coefficient. Therefore
\[
\boxed{\mathcal R_{r,k}\ge T_{k-1}^{2r}\ge E_{k-1}^{2r}.}
\tag{6}
\]

For \(j\ge2\), \(U=2\) gives \(0<c_j^*\le a_{j-1}\), because
\(u^2/[(2j)(2j-1)]\le1/3\). Consequently
\[
0<c_j^*\le a_0\,\frac{U^{2j-2}}{(2j-2)!}.
\tag{7}
\]
If \(k\ge r+2\), all entries in both reference determinants have index
at least two. A permutation uses indices
\(\ell_i=k+\sigma(i)-i\), with \(\sum_i\ell_i=nk\).
Convexity of \(\log\Gamma\) gives
\(\prod_i(2\ell_i-2)!\ge[(2k-2)!]^n\). Thus, with
\(V_k=a_0U^{2k-2}/(2k-2)!\),
\[
|D_{n,k}(c^*)|\le n!V_k^n,\qquad
|q^*_{r,k}|\le(r+1)!(r-1)!\,V_k^{2r}.
\tag{8}
\]
Define
\[
A_k=\frac{K}{aa_0}\frac{(2k-2)!}{(aU)^{2k-2}}.
\tag{9}
\]
Then
\[
\frac{\mathcal R_{r,k}}{(r+1)!(r-1)!\,V_k^{2r}}
\ge\frac{A_k^{2r}}{(r+1)!(r-1)!}.
\tag{10}
\]
Since \(A_{k+1}/A_k=(2k)(2k-1)/(aU)^2\), \(A_k\to\infty\).
In particular,
\[
k\ge r+2,\qquad A_k^{2r}>(r+1)!(r-1)!
\tag{11}
\]
imply \(\mathcal R_{r,k}>|q^*_{r,k}|\), proving (1).
If \(q^*>0\), also \(\mathcal R/q^*\to\infty\); if \(q^*\le0\),
the lower allowance fails without that ratio.

This analytical stopping rule has explicit \(r,k\) dependence; no
threshold was measured. It strengthens Note05's entry-envelope
obstruction while preserving all accepted finite results. Collecting
more monomials or raising precision cannot rescue this unchanged payment.
The actual signed residual is not bounded from below: the independent
box permits high-moment perturbations the canonical tail need not realize.
Different correlations, tail vectors and references are not excluded.

## 3. A worked alternative: true large-index coefficient errors decay

Remove the spatial cutoff but initially retain one full mode and \(b\).
For \(j\ge1\),
\[
c_j^{[1]}=\int_0^\infty\Phi_1(u)\frac{u^{2j}}{(2j)!}\,du>0.
\]
The zero coefficient also contains the endpoint atom in Section 4.
For every integer \(j\ge e^{16}\),
\[
\boxed{0<\frac{c_j-c_j^{[1]}}{c_j^{[1]}}
 \le128\exp\!\left[-\frac{j}{16\log j}\right].}
\tag{12}
\]
The constants and threshold are convenient analytical choices, not
measured optimal values.

Put \(t=\pi e^{4u}>3\). Since
\(\Phi_n=e^ue^{-n^2t}(2n^4t^2-3n^2t)\),
\(\Phi_n/\Phi_1\le2n^4e^{-(n^2-1)t}\).
Using \(n^4\le16^{n-1}\), \(n^2-4\ge5(n-2)\), and
\(16e^{-5\pi}<1/2\), sum every omitted mode to obtain
\[
\frac{\sum_{n\ge2}\Phi_n}{\Phi_1}\le64e^{-3\pi e^{4u}}.
\tag{13}
\]
Let \(L=\log j,\ B=\tfrac14\log[j/(16\pi L)]\), and \(A=B-1/4>0\).
Let \(\mu_j\) have density proportional to \(u^{2j}\Phi_1(u)\).
The bounds
\[
\pi^2e^{9u-\pi e^{4u}}\le\Phi_1(u)\le2\pi^2e^{9u-\pi e^{4u}}
\]
bound its numerator over \([0,A]\) and its denominator from below
over \([B,B+1/4]\), giving
\[
\mu_j([0,A])
\le\frac{8A}{2j+1}e^{-9/4}(A/B)^{2j}
 \exp[ej/(16L)]
\le\exp[-7j/(4L)].
\tag{14}
\]
For the last inequality use \(B\le L/4\),
\(8A/(2j+1)\le L/j\le1\), \(\log(A/B)\le-1/(4B)\), and \(e<4\).
Above \(A\), (13) is at most \(64\exp[-3j/(16eL)]\).
Splitting its \(\mu_j\)-expectation at \(A\) and using \(e<3\)
proves (12). No spatial exterior is omitted.

For a determinant consumer set \(J=k-r\ge e^{16}\), assume separately
\(d_\pm=D_{r\pm1,k}(c^{[1]})>0\), and put
\[
\mathcal K=\max_\pm H_{r\pm1,k}(c^{[1]})/d_\pm\ge1.
\]
Here \(H\) is Note05's collected absolute determinant polynomial. If
\[
\frac{J}{16\log J}\ge\log(1024(r+1)\mathcal K),
\tag{15}
\]
then (12) gives \(\epsilon\le[8(r+1)\mathcal K]^{-1}\) uniformly on
both matrices. Homogeneity and \(e^x-1\le2x\) for \(0\le x\le1/8\)
give \(e_\pm\le[(1+\epsilon)^{r\pm1}-1]\mathcal K\le1/4\).
The complete product estimate (3) yields
\[
|Q_{r,k}-d_+d_-|\le(9/16)d_+d_-,\qquad
Q_{r,k}\ge(7/16)d_+d_->0.
\tag{16}
\]
This is a new coefficient payment, not a bound on the old \(\mathcal R\).

An additional, unproved conditioning estimate
\(\log\mathcal K\le A_0(r+1)^2\log(2k)\) would turn (15) into
\[
\frac{k-r}{16\log(k-r)}
 \ge\log(1024(r+1))+A_0(r+1)^2\log(2k).
\tag{17}
\]
The suggested scale \(k\gg r^2(\log k)^2\) is conditional on that
estimate and on reference signs. Neither is established here.

## 4. A fixed finite-mode boundary-preserving reference cannot be PF-infinity

For fixed \(N\ge1\), put
\[
p_N=\sum_{n=1}^Np_n,\quad
A_N(z)=\frac18\int_0^\infty p_N(u)\cosh(u\sqrt z)\,du,\quad
C_N(z)=b+(z-1)A_N(z).
\tag{18}
\]
The even series removes any square-root branch ambiguity. Let
\[
\Phi_N=(p_N''-p_N)/8>0,\quad \beta_N=-p_N'(0)/8,\quad
\tau_N=b-\beta_N
=\sum_{n>N}(4\pi n^2-1)e^{-\pi n^2}/8>0.
\tag{19}
\]
Complete canonical reflection supplies the final equality. Green
integration, with the unchanged boundary, gives
\[
C_N(z)=\tau_N+\int_0^\infty\Phi_N(u)\cosh(u\sqrt z)\,du,
\]
\[
C_N(-t^2)=\tau_N+\int_0^\infty\Phi_N(u)\cos(tu)\,du
\longrightarrow\tau_N>0.
\tag{20}
\]
Every coefficient is positive. Hence there are no nonnegative real
zeros and only finitely many negative real zeros.

For \(R=|z|\), \(s=(\sqrt R+1)/4\), substitution in \(A_N\) gives
\[
|C_N(z)|\le b+\frac{N(R+1)}{32}\pi^{-s}\Gamma(s).
\tag{21}
\]
The entire order is at most \(1/2\). Its infinitely many positive
coefficients make it nonpolynomial. Hadamard factorization for order
less than one therefore forces infinitely many zeros; only finitely
many are real. Thus **infinitely many zeros are nonreal**.

The standard entire PF-infinity characterization excludes
\(C_N\in PF_\infty\). Moreover, not all contiguous \(D_{r,k}(C_N)\)
can be strictly positive: if they were, Katkova's Lemma 3, applied for
each finite order, would imply PF-infinity. Its summability hypothesis
holds since \(C_N(1)=b\). These classical imports are identified in
[the source inspection][refs].

This locates no failing pair, does not prove failure along \(k=1\), and
does not exclude references varying with \(r,k\). The compact reference
has an additional upper-endpoint oscillation and is outside this zero-set
argument. The theorem excludes the selected fixed finite-mode global
reference repair, not complete canonical theta or correlated estimates.

## 5. Exact propagation shows what regularity an induction needs

This is a diagnostic calculation, not a third theta comparison. On a
domain where the relevant signs have been justified, put
\[
F_r=\log D_r,\quad \mathcal Lf(k)=2f(k)-f(k-1)-f(k+1),\quad
\lambda_r=\mathcal L F_r.
\]
Desnanot–Jacobi gives
\[
\lambda_{r+1}=2\lambda_r-\lambda_{r-1}
 +\mathcal L\log(1-e^{-\lambda_r}).
\tag{22}
\]
An unexplained \(\lambda_r>0\) invariant would assume the next-order
sign. The useful diagnostic is its additional second-difference term.

For the independently positive benchmark \(a_j=1/j!\), column factorial
extraction and the Vandermonde determinant of monic falling factorials give
\[
D^*_{r,k}=\prod_{i=0}^{r-1}\frac{i!}{(k+i)!},\qquad
\lambda_r^*(k)=\log(1+r/k).
\tag{23}
\]
Negative-index zeros are respected. For \(t_r=\lambda_r-\lambda_r^*\),
\[
t_{r+1}=2t_r-t_{r-1}+\mathcal Lg_r,\qquad
g_r(k)=\log[1+(k/r)(1-e^{-t_r(k)})].
\tag{24}
\]
If \(|t_r|\le\omega<\lambda_r^*\), then
\(\rho=(k/r)(e^\omega-1)<1\) and
\(|g_r|\le-\log(1-\rho)\): every nonlinear term is paid, but an
unstructured error is amplified by approximately \(k/r\).

A worked smoother bound is possible. Suppose a \(C^2\) interpolation on
\([k-1,k+1]\), with \(x\ge r\), satisfies
\[
|t_r|\le ar/x,\quad |t_r'|\le br/x^2,\quad |t_r''|\le cr/x^3,
\quad \rho_0=ae^a<1.
\]
Then
\[
|\mathcal Lg_r(k)|\le C(a,b,c)/(k-1)^2,\quad
C=\frac{e^ac}{1-\rho_0}
+\frac{e^a(2b^2+2b)+a^2e^{2a}}{(1-\rho_0)^2}.
\tag{25}
\]
For verification set \(A=x/r,\ d=1+A(1-e^{-t})\). The partial derivatives
are \(g_t=Ae^{-t}/d\), \(g_{tt}=-A(1+A)e^{-t}/d^2\),
\(g_{xt}=e^{-t}/(rd^2)\), and \(g_{xx}=-(1-e^{-t})^2/(r^2d^2)\).
Use the chain rule and
\(-\mathcal Lg(k)=\int_{-1}^1(1-|s|)g''(k+s)\,ds\).
If these budgets persist through order \(n-1\), the recurrence telescopes:
\[
|t_n-nt_1|\le Cn(n-1)/[2(k-1)^2].
\tag{26}
\]
This has a useful joint-order scale but is not initialized for theta.
Propagating the derivative budgets requires third and fourth derivatives,
so the displayed finite regularity package is not closed. The interpolation
is an additional premise, not a theorem about real-index theta minors.
No sufficiently accurate theta-to-factorial comparison is asserted.

## 6. Domain audit, control screen and return

| Domain | Established here | Remaining gap |
| --- | --- | --- |
| Fixed small \(k\), growing \(r\) | All boundary terms retained; no fixed finite-mode global reference is available | Full-source order mechanism and margins |
| \(k\) near \(r\) | Boundary ranks remain \(\max(r-k+1,0),\max(r-k,0),\max(r-k-1,0)\) | Transition estimate and joining argument |
| Fixed \(r\), unbounded \(k\) | Exact old payment fails; actual coefficient tail decays | Repaired reference signs and conditioning |
| Joint large \(r,k\) | Conditional criterion (17); separate full-source criterion in Note08 | Its scalar inputs and the entire complementary region |

The payment obstruction applies to the specified compact reference and
geometric \(E\), not the actual signed tail. The true-tail theorem uses
literal unit-square weights and \(n^2\) separation. Weighted-square
controls require new weight payments; Euler-factor controls shift the
source; reflected and smooth primitive controls lack this square
expansion. None is claimed to fail an uncomputed determinant inequality.
The propagation algebra is generic and screens out no control by itself.
The finite-mode theorem uses its explicit positive endpoint atom.
A positive-time collision is not a counterexample to a time-zero
finite-order claim.

Katkova already proves eventual positivity for every fixed order. The
new question is quantitative joint dependence and the growing complement,
not another fixed-order tail certificate. The stronger reported joint-order
baseline is identified in Note08, Section 7; see [references][refs].
Under the author's broader request, [B02 r1][repair] selects one
complete-source repair. [The continuation packet][continuation] records
assessment, execution and model-change guidance. This return does not
prove RH or increase the acquired theta positivity range.

[request]: ../research-progress/handoffs/10_RGD_B03_R2_INDUCTION_INDEX_ERROR_AND_MODEL_CONTINUATION_20261104.md
[progress]: ../research-progress/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_PROGRESS_20261104.md
[repair]: 08_RGD_B02_R1_COMPLETE_SOURCE_CONTOUR_MARGIN_20261104.md
[continuation]: ../research-progress/handoffs/11_RGD_B03_B02_RETURN_AND_MODEL_CONTINUATION_20261104.md
[refs]: ../references/README.md
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a11]: ../../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
