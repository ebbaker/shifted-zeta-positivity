# Actual Sonin enclosures and a resolved trial-space accuracy test

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed. Separate same-model agents derived and checked the prolate,
source, and projection estimates; the lead implemented their combined
certificate. This is internal mathematical and computer-assisted evidence,
not independent human refereeing.

**Outcome.** The enclosure task in the [previous handoff](SONIN_CONTINUATION_AFTER_TRACE_AUDIT_20260929.md)
has now been implemented for a nonzero, explicitly specified actual-Sonin
trial space and both prescribed sources. All projection tails are included.
The computed trace approximants are positive, but the chosen two-vector
space cannot achieve the proposed precision: one omitted actual Sonin
direction proves that it misses more than **0.00373** and **0.00712** of
the positive trace for the even and odd sources, respectively. This is
an accuracy obstruction for this trial choice, not a negative arithmetic
residual or an obstruction to the Sonin program.

The full Hilbert–Schmidt residual upper enclosures are also available, though coarse.
The work does not yet evaluate the complete arithmetic residual, certify
its sign, or establish a new positivity interval. No finite Weil certificate,
CCM calculation, manuscript, commit, or push is part of this continuation.

Supporting derivations are the [prolate certificate](SONIN_PROLATE_RESOLVENT_CERTIFICATE_20260929.md)
and [source norm certificates](SONIN_SOURCE_NORM_CERTIFICATES_20260929.md).
The [critical review](../reviews/SONIN_ACTUAL_ENCLOSURE_REVIEW_20260929.md)
and [new handoff](SONIN_CONTINUATION_AFTER_ENCLOSURE_TEST_20260929.md)
record what should follow this bounded test.

## 1. Quantities, domains, and what was actually enclosed

Keep the conventions and smooth-source comparison in the
[canonical audit](SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md).
The positive-axis state space is \(\mathcal H=L^2(0,\infty;dx)\),
\(\mathcal Fh(y)=2\int_0^\infty\cos(2\pi xy)h(x)dx\),
\(\chi=1_{(0,1)}\), \(R=I-\chi\), \(C=\chi\mathcal F\chi\),
and \(M=(I-C^2)^{-1}\). The actual cutoff-1 Sonin projection is
\[
\Pi=R-R\mathcal F\chi M\chi\mathcal F R.
\tag{1}
\]
Conjugate by \(Wh(t)=e^{t/2}h(e^t)\) when using logarithmic
convolution or \(U_av(t)=v(t-a)\). At prime 2 put
\[
a=\log2,\quad r=2^{-1/2},\quad D=I-rU_a,\quad
G=D^*D=\alpha I-r(U_a+U_{-a}),\quad\alpha=3/2,
\]
\[
\mathcal K=\operatorname{Ran}\Pi,\quad A=(\Pi G\Pi)|_{\mathcal K},
\quad \ell^2=(1-r)^2,\quad k_G=(1+r)^2.
\tag{2}
\]

For each exact arithmetic source \(F=f_j\) specified below, let
\(L_F=C_FD\), \(W_F=(L_F\Pi)^*:\mathcal H\to\mathcal K\),
and \(\mathsf H_F=W_FW_F^*\). The scalar is
\[
h_0=\operatorname{Tr}\mathsf H_F=\|C_FD\Pi\|_{\rm HS}^2
=\mathcal B_\infty[D F].
\tag{3}
\]
For an injective finite synthesis map \(Q:\mathbb C^d\to\mathcal K\)
whose columns are actual Sonin vectors, define
\[
A_d=Q^*AQ,\quad H_d=Q^*\mathsf H_FQ,\quad
J_d=Q^*\mathsf H_FAQ,\quad K_d=Q^*A^2Q.
\tag{4}
\]
These finite matrices and a global scalar enclosure for (3) are certified
here. No finite cosine projection is substituted for \(\Pi\).

The columns of \(Q\) need **not** be orthonormal. With
\(Y_d=Q A_d^{-1}Q^*W_F\), \(\mathcal R_d=W_F-AY_d\),
Galerkin orthogonality \(Q^*\mathcal R_d=0\) gives
\[
B^{[d]}=\operatorname{tr}(A_d^{-1}H_d),\qquad
\mathcal B_2[F]-B^{[d]}=\|A^{-1/2}\mathcal R_d\|_{\rm HS}^2,
\tag{5}
\]
\[
\|\mathcal R_d\|_{\rm HS}^2
=h_0-2\Re\operatorname{tr}(A_d^{-1}J_d)
+\operatorname{tr}(A_d^{-1}K_dA_d^{-1}H_d).
\tag{6}
\]
Thus (A15)–(A16) of the previous note survive unchanged for this
nonorthogonal basis. In particular
\[
\ell^2(\mathcal B_2-B^{[d]})
\le\|\mathcal R_d\|_{\rm HS}^2
\le k_G(\mathcal B_2-B^{[d]}).
\tag{7}
\]
This removes unnecessary Gram square-root errors. Coercivity and the
certified positive finite matrices ensure that the inverses used exist.

## 2. Certified prolate constants, including the infinite complement

The independent interval certificate establishes
\[
I-C^2\ge\gamma I,\qquad\gamma=57/10^6,
\qquad\|M\|\le\gamma^{-1}<17544.
\tag{8}
\]
It uses the cosine Taylor kernel through \(j=31\), represented in
\(e_k(x)=\sqrt{4k+1}P_{2k}(x)\), \(0\le k<32\).
The full omitted nuclear tail is less than \(1.5\,10^{-40}\).
Interval LDL proves the finite inequality with this perturbation retained;
the orthogonal complement is handled explicitly.

An exact dyadic matrix defines the polynomial correction to the identity
\(\mathscr R_{32}\), with
\[
\|M-\mathscr R_{32}\|<9.2\,10^{-32},\qquad
\|CM-C_{32}\mathscr R_{32}\|_1<2.7\,10^{-31},\qquad
\|C\|_1<2.858.
\tag{9}
\]
The last bound uses a column-wise nuclear decomposition, not an assumed
eigenvalue computation. All positivity decisions are outward Arb interval
comparisons. A separate 192-bit replay passed the same simple caps.
The trial calculation below needs (8) and the last bound in (9); the
sharper polynomial inverse is retained for the next trace calculation.

## 3. The same exact smooth source family

Let \(b=9/20\), \(\phi(x)=\exp[-1/(1-(x/b)^2)]\) on
\(|x|<b\), extended by zero, and
\[
f_0=\frac{(-\partial_x^2+1/4)\phi}
{\|(-\partial_x^2+1/4)\phi\|_2},\qquad
f_1=\frac{(-\partial_x^2+1/4)(x\phi)}
{\|(-\partial_x^2+1/4)(x\phi)\|_2}.
\tag{10}
\]
These are the earlier (A17) sources at \(L=1\). Both exponential
moments vanish exactly; their ordinary \(L^2\) norms are 1 and their
additive parity is respectively even and odd. No source replacement is
made in the mathematical claim.

Arb/Acb integration on a compact interior, together with explicit
exponential endpoint bounds, certifies their norms. Some useful upward
rounded bounds are:

| Quantity | Even source \(f_0\) | Odd source \(f_1\) |
|---|---:|---:|
| Unnormalized \(L^2\) norm, display only | 10.92489867686765 | 4.30234515884264 |
| \(\|f_j\|_1\) upper | 0.653950308086 | 0.686080643314 |
| \(\|f_j'\|_1\) upper | 36.184255321 | 37.726019671 |
| \(\|f_j''\|_1\) upper | 3090.581059252 | 3296.172957907 |

The record includes exact rational interval endpoints and derivative
\(L^2\) norms through order four. It never treats the nonanalytic bump
endpoint as an analytic integration point.

## 4. Actual trial vectors and complete tail bounds

Use positive-axis Legendre seeds
\[
b_n(x)=\sqrt{2n+1}P_n(2x-3)1_{[1,2]}(x).
\tag{11}
\]
Their low cosine leakage has the elementary factorial bound
\[
\left(\int_0^p|\mathcal Fb_n(y)|^2dy\right)^{1/2}
\le p^{n+1/2}\epsilon_n,\quad
\epsilon_n=\frac{2\pi^n}{(2n+1)!!},\quad p\ge1.
\tag{12}
\]
To prove it, substitute \(t=2x-3\) and integrate Rodrigues' formula
\(n\) times. This gives
\(\int_{-1}^1P_n(t)e^{izt}dt
=i^nz^n(2^nn!)^{-1}\int_{-1}^1(1-t^2)^ne^{izt}dt\).
The beta integral bounds the spherical Bessel factor by
\(|z|^n/(2n+1)!!\). Integrating the resulting \(y^{2n}\)
bound gives (12), including its normalization.

For an exactly compact smooth seed, take the standard step
\(\theta(t)=e^{-1/t}/(e^{-1/t}+e^{-1/(1-t)})\) on \(0<t<1\),
extended by 0 and 1, and set
\[
\eta_n(x)=b_n(x)\theta((x-1)/\varepsilon_c)
\theta((2-x)/\varepsilon_c),\qquad\varepsilon_c=10^{-40}.
\tag{13}
\]
It is smooth in the ambient positive-axis space, supported in \([1,2]\),
and zero on \((0,1)\). Its arbitrarily thin transition is not numerically
sampled: \(|P_n|\le1\) gives the global bound
\[
\|\eta_n-b_n\|\le\rho_n:=\sqrt{2(2n+1)\varepsilon_c}.
\tag{14}
\]
Define the **exact** trial vector \(q_n=\Pi\eta_n\).
For any \(v=Rv\), (1) implies
\[
\|v-\Pi v\|^2=\langle\chi\mathcal Fv,M\chi\mathcal Fv\rangle.
\tag{15}
\]
Combining (8), (12), and (14) therefore encloses the whole tail:
\[
\|q_n-b_n\|\le d_n:=\gamma^{-1/2}\epsilon_n+\rho_n,
\qquad\|q_n\|\le1.
\tag{16}
\]

Let \(c_n=RGb_n=\alpha b_n-rU_ab_n\). The lower translate
\(U_{-a}b_n\) is supported below the cutoff and is killed by \(\Pi\).
The upper translate has Fourier leakage up to frequency 2, because
\(\mathcal F U_a=U_{-a}\mathcal F\). Consequently
\[
\|Aq_n-c_n\|\le z_n:=k_Gd_n+(\alpha+2^n)\gamma^{-1/2}\epsilon_n.
\tag{17}
\]
This is a full \(L^2\) bound. No unobserved spatial region is discarded.
Orthogonality and disjoint translated supports give
\[
\langle b_i,Gb_j\rangle=\alpha\delta_{ij},\qquad
\langle c_i,c_j\rangle=(11/4)\delta_{ij}.
\tag{18}
\]
We use \(Q=(q_{20},q_{24})\). Its Gram matrix is close to the identity
by (16), so it is injective. Conservative certified bounds are

| Degree | \(\|q_n-b_n\|\) upper | \(\|Aq_n-c_n\|\) upper |
|---|---:|---:|
| 20 | \(1.772\,10^{-13}\) | \(1.858\,10^{-7}\) |
| 24 | \(3.972\,10^{-18}\) | \(6.498\,10^{-11}\) |
| 21, omitted-direction check only | \(1.295\,10^{-14}\) | \(2.715\,10^{-8}\) |

The very small projection defects do not imply that these vectors capture
most of a smoothed trace. Section 8 tests that separate issue.

## 5. Compact convolution enclosures with exact integer arithmetic

In logarithmic coordinates the proxy seed is
\(B_n(t)=e^{t/2}b_n(e^t)\), supported on \([0,a]\).
Use a uniform grid of width \(h=a/N\), \(N=16384\), so both seed
endpoints and the prime shift align exactly. Let \(B_{n,h}\) be its
cell averages and \(F_h\) the continuous linear interpolant of the exact
source samples. Although the zero-extended seed has endpoint jumps, its
**interior** derivative is square integrable. On each cell the residual
\(B_n-B_{n,h}\) has zero mean. Taking a primitive and applying the
Dirichlet and mean-zero Poincare inequalities gives
\[
\|C_F(B_n-B_{n,h})\|_2
\le\frac{h^2}{\pi^2}\|F'\|_1\|B_n'\|_{L^2(0,a)}.
\tag{19}
\]
There is no whole-line \(H^1\) assertion about the discontinuous seed.
The linear interpolation Green kernel also gives
\[
\|F-F_h\|_1\le\frac{h^2}{8}\|F''\|_1.
\tag{20}
\]
The cell-average contraction \(\|B_{n,h}\|_2\le1\) and Young's
inequality combine (19)–(20) into a certified convolution error.

All required seed averages are exact polynomial antiderivatives with Arb
enclosures of their algebraic endpoints:
\[
\int B_n(t)dt=\sqrt{2n+1}\sum_k
\frac{p_k e^{(k+1/2)t}}{k+1/2},\quad
P_n(2x-3)=\sum_kp_kx^k.
\tag{21}
\]
The squared interior derivative norm is the exact polynomial integral
\(\int_1^2|b_n(x)/2+xb_n'(x)|^2dx\).
Samples and averages are rounded to multiples of \(2^{-80}\), with
their errors retained. Integer polynomial multiplication computes their
discrete convolution exactly; it is not a floating FFT certificate.

Convolving a piecewise linear hat with a cell box yields a quadratic
cardinal B-spline. Its integer-shift Gram weights are
\(11/20,13/60,1/120\) at displacements \(0,1,2\), and zero beyond.
The resulting continuous inner products are therefore exact integer sums
times \(h^3/(120\,2^{320})\). Translations by \(a\) are shifts by
\(N\) coefficients. This computes all compact response inner products
needed for \(H_d,J_d\); support selection is itself verified by an Arb
inequality, rather than inferred from rounded zero samples.

Write \(y_i=L_Fb_i\), \(v_i=L_Fc_i\), with certified proxy functions
\(\widetilde y_i,\widetilde v_i\). The source and seed approximation
bounds give
\[
\|L_Fq_i-\widetilde y_i\|\le e_i,
\qquad \|L_FAq_i-\widetilde v_i\|\le e_i^A.
\tag{22}
\]
For example the first error is the compact-convolution bound times
\(1+r\), plus \((1+r)\|F\|_1d_i\); the second uses the
factor \(\alpha+r\) and adds \((1+r)\|F\|_1z_i\).
Then
\[
|H_{ij}-\langle\widetilde y_i,\widetilde y_j\rangle|
\le e_i\|\widetilde y_j\|+e_j\|\widetilde y_i\|+e_ie_j,
\]
\[
|J_{ij}-\langle\widetilde y_i,\widetilde v_j\rangle|
\le e_i\|\widetilde v_j\|+e_j^A\|\widetilde y_i\|+e_ie_j^A.
\tag{23}
\]
Equations (16)–(18) analogously enclose \(A_d,K_d\). The true
\(J_{ij}\) is \(\langle L_Fq_i,L_FAq_j\rangle\); its order
and translation direction are retained. The recorded response errors at
this grid lie between \(4.45\,10^{-6}\) and \(5.73\,10^{-6}\).

## 6. A full, but intentionally coarse, scalar trace bound

The cutoff decomposition from the audit is
\(L_0=\Pi+\sum\lambda_n^2|\zeta_n\rangle\langle\zeta_n|\ge\Pi\).
The smoothed cutoff trace has error kernel \(\delta\), which differs
from the Sonin kernel \(\epsilon\). For \(\rho\ge1\),
\[
\delta(\rho)=\operatorname{Tr}(C\chi\vartheta(\rho^{-1})\mathcal F\chi),
\qquad |\delta(\rho)|\le\|C\|_1.
\tag{24}
\]
This agrees with [Connes–Consani, Proposition 2, (42)–(43)](https://arxiv.org/html/2006.13771v1#S2).
It follows that for every compact smooth kernel \(H\),
\[
0\le\mathcal B_\infty[H]\le\Gamma[H]+\|C\|_1\|H\|_1^2.
\tag{25}
\]
No sign of the complete Weil form is assumed.

The source certificate proves the full gamma-multiplier upper bound
\(m(t)\le\tfrac12\log(1+4t^2/25)\). Plancherel and Jensen give
\(\Gamma[H]\le(n/2)\log(1+4k/(25n))\), where
\(n=\|H\|_2^2\), \(k=\|H'\|_2^2\). This expression is
increasing in both variables, so the norm bounds for \(H=DF\) yield
certified values for (25), without Fourier quadrature. They give
\[
h_0(f_0)<11.509,\qquad h_0(f_1)<11.989.
\tag{26}
\]
The code also uses \(h_0\ge\ell^2B^{[2]}\), which follows from
the variational inverse bound. These are enclosures, not accurate
evaluations of \(h_0\). The smaller kernel bound for \(\delta\)
must not be mislabelled as the same bound for \(\epsilon\).

## 7. Certified rank-two output and its limits

The [trial record](../numerics/records/sonin_trial_enclosure.json) contains
every matrix entry as an outward dyadic ball, source/program hashes, all
parameters, and full projection and convolution errors. Interval LDL
checks the finite positive matrices. Upward/downward rounded summaries are:

| Quantity | Even source | Odd source |
|---|---:|---:|
| \(B^{[2]}\) | [0.0074225, 0.0074246] | [0.0122013, 0.0122039] |
| \(\|\mathcal R_2\|_{\rm HS}^2\), upper | 11.497 | 11.965 |
| \(\mathcal B_2\), resulting broad upper | 134.023 | 139.476 |

The full trace is at least \(B^{[2]}\). Positivity clips any harmless
negative lower endpoint introduced by storing a broad ball around a
nonnegative quantity. All infinite tails are included in these enclosures.
The matrix errors are small; the very broad \(h_0\) enclosure dominates
the upper residual budget. This already fails to resolve the intended
trace scale, but a weak upper bound alone does not show that the trial
space itself is inadequate. The next check supplies that distinction.

## 8. One omitted direction proves a genuine accuracy shortfall

Add \(q_{21}\) only as an omitted-direction witness, keeping the exact
same sources, projection, compressed metric, and smooth seed convention.
The trial spaces \(\operatorname{span}(q_{20},q_{24})\) and
\(\operatorname{span}(q_{20},q_{24},q_{21})\) are nested. Thus
\[
\mathcal B_2[f]-B^{[2]}[f]\ge B^{[3]}[f]-B^{[2]}[f].
\tag{27}
\]
The [omitted-direction calculation](../numerics/records/sonin_omitted_direction.json)
and [comparison check](../numerics/records/sonin_omitted_direction_check.json)
certify
\[
\boxed{\mathcal B_2[f_0]-B^{[2]}[f_0]>0.00373,\qquad
\mathcal B_2[f_1]-B^{[2]}[f_1]>0.00712.}
\tag{28}
\]
The unrounded difference intervals have lower endpoints above
0.0037377615 and 0.0071266917, respectively. By (7), the corresponding
squared full Hilbert–Schmidt residuals are greater than 0.00032 and
0.00061. These lower bounds do not depend on the coarse \(h_0\) upper
bound or on increasing arithmetic precision.

Applying (25) to the unshifted source also gives
\(\mathcal B_\infty[f_0]<3.950\) and
\(\mathcal B_\infty[f_1]<4.114\). Both traces are nonzero because
their transported traces have positive trial lower bounds. Therefore
\[
\frac{\mathcal B_2[f_0]-B^{[2]}[f_0]}{\mathcal B_\infty[f_0]}
>9\,10^{-4},\qquad
\frac{\mathcal B_2[f_1]-B^{[2]}[f_1]}{\mathcal B_\infty[f_1]}
>1.7\,10^{-3}.
\tag{29}
\]
The chosen rank-two approximation cannot meet a
\(10^{-8}\mathcal B_\infty[f]\) trace-error allocation, even with
perfect evaluation of its entries. This third vector is a lower-bound
witness for omitted trace, not an attempt to cure the issue by a rank sweep.
The main rank-two scheme stops here as specified in the handoff's decision rule.
This does not exclude using it at a coarser tolerance. The complete residual
has not been computed, so its source-specific sign-resolution scale is not
yet known; \(10^{-8}\mathcal B_\infty\) is the explicit small-error
benchmark inherited from the return-tail comparison, not a necessary RH threshold.

## 9. What is the next analytical obligation?

This session completes the existence-and-enclosure lemma for an explicit
actual trial family, but rejects that family's precision as a full trace
approximation. It does not refute the residual comparison or any
Sonin-specific sign law. Positivity of \(B^{[2]}\) or \(B^{[3]}\)
does not establish positivity of \(Q_1\).

The next bounded target should use the now-certified polynomial resolvent
to evaluate the **scalar smoothed archimedean trace** accurately:
\[
\epsilon(\rho)=\operatorname{Tr}(CM B_\rho),\qquad
B_\rho=\chi\vartheta(\rho^{-1})R\mathcal F\chi,
\quad\|B_\rho\|\le1.
\tag{30}
\]
Replacing \(CM\) by \(C_{32}\mathscr R_{32}\) costs less than
\(2.7\,10^{-31}\), uniformly in \(\rho\). The remaining work is
finite polynomial–cosine integration, with rigorous parameter/source
quadrature and a separately bounded gamma integral. The source fourth
derivative certificates already bound its Fourier tails.

This scalar task should be completed before selecting a new trial space:
it supplies the correct total trace scale and tests conditioning without
another arbitrary rank choice. Any subsequent trial space must be selected
to capture the smoothed source responses, not merely to have tiny projection
defects. The separate Chebyshev return moments and signed place-addition
estimate remain uncomputed. Even accurate finite-source traces would be
diagnostics, not an all-support inequality or an arithmetic limit theorem.

## 10. Reproduction and artifact policy

The programs require Python and `python-flint==0.9.0`; NumPy/SciPy are not
used to decide any recorded certificate. From `arithmetic-storage/numerics`,
the commands below regenerate the small records (use a copied directory or
explicit output paths to preserve the saved ones):

```sh
python3 -B source_norm_enclosures.py
python3 -B prolate_certificate.py --rank 32
python3 -B sonin_trial_enclosure.py --grid 16384
python3 -B sonin_trial_enclosure.py --grid 16384 --seed-degrees 20 24 21 --output records/sonin_omitted_direction.json
python3 -B sonin_omitted_direction_check.py
```

Do not use Python `-O` or `-OO`; the source integration script uses
assertions as certificate guards. The other programs also use explicit
exceptions for failed checks. Code hashes bind records to their generators;
they identify the arithmetic that must be replayed, not a substitute for
that replay. Dyadic interval serialization can vary across precision/runtime
settings; compare proved bounds and containment, not merely display strings.

Only code, parameter/error records, and notes are retained. Grid arrays,
integer convolution arrays, and polynomial inverse matrices are regenerable
and remain outside repository artifacts or in memory. Every saved file is
well below the repository's 1 MiB convention. No draft snapshot is created.
