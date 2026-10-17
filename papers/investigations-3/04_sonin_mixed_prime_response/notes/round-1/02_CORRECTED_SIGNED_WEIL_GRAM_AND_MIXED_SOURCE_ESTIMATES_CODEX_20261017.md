# Corrected signed Weil Gram identity and mixed source estimates

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort:
**ultra**. Parallel same-model checks examined the normalized transport
identity, modulation asymptotic, earlier source comparison and approximation
constants. These are internal checks, not Claude reconciliation or specialist
human review. Repository baseline: `b2a957e9edd5230b6343b2677cad057dbb9b7a6c`.

**Status: analytic continuation within round 1.** An explicit corrected
signed Weil–Gram identity is derived below. Its inverse-metric correction
is generally unbounded with both signs on a fixed prepared source interval,
even though the complete mixed response extends to a compact bounded
source operator. A construction gives signed enclosures for that complete
operator from boundary approximations. No numerical enclosure, sign of the
actual mixed response, or improvement of a Weil positivity margin is claimed.

This continues [Note 01][n01] and its next-input question. The
[result index][results], [Sonin summary 07][s07] and [avoid index][avoid]
remain the governing context. The derivative-free crossing bound and
first-prime compact source correction are **reused** from the
[closed source comparison][closed], §§2–3, and
[compact correction note][compact]. The additions here are the explicit
signed Gram correction, its signed asymptotic, and a compact-boundary
transfer and enclosure for arbitrary fixed finite-place quartets. The
identities are not a replacement criterion for global positivity; see
[avoid 01][a01], [07][a07], [10][a10] and [12][a12].

## 1 Fixed source and normalized transport

Use the conventions and actual Sonin projections of Note 01. In particular,
\(U_av(x)=v(x-a)\), the inner product is antilinear in its first slot,
\(\kappa_F(u)=\int\overline{F(x)}F(x+u)\,dx\), and
\[
F=\mathcal A h,\quad \mathcal A=-\partial_x^2+\tfrac14,
\quad h\in C_c^\infty(I_L;\mathbb C),\quad I_L=(-L/2,L/2).
\tag{1}
\]
Fix finite \(S\), distinct \(p,q\notin S\), and the same source at all
four corners. Write \(P=\Pi_S\), \(\mathcal K=\operatorname{Ran}P\),
\(V=C_F|_{\mathcal K}\), and
\[
r_j=j^{-1/2},\quad \beta_j=\frac{2r_j}{1+r_j^2},\quad
J_j=\frac{I-r_jU_{\log j}}{\sqrt{1+r_j^2}},\quad
E_j=J_j^*J_j-I=-\frac{\beta_j}{2}(U_{\log j}+U_{\log j}^*).
\tag{2}
\]
For \(A\subseteq\{p,q\}\), set
\[
J_A=\prod_{j\in A}J_j,\quad G_A=J_A^*J_A,\quad
\mathsf M_A=(PG_AP)|_{\mathcal K},\quad
\mathsf N_A=V^*G_AV,
\]
\[
Z_A[F]=\operatorname{Tr}_{\mathcal K}
\bigl((\mathsf M_A^{-1}-I)\mathsf N_A\bigr),\qquad
\mathcal R_{\rm met}=Z_{\{p,q\}}-Z_{\{p\}}-Z_{\{q\}}.
\tag{3}
\]
The inverse acts on \(\mathcal K\), with lower bound
\(\mathsf M_A\ge\prod_{j\in A}(1-\beta_j)I>0\).
Each \(\mathsf N_A\) is trace class by Hilbert–Schmidt factorization.
These definitions retain the full inverse; \(Z_\varnothing=0\). Scalar
normalization does not change the transported orthogonal projection, so
\[
B_{S\cup A}[F]=\operatorname{Tr}(\mathsf M_A^{-1}\mathsf N_A)
=B_S[J_AF]+Z_A[F].
\tag{4}
\]
Here \(C_{J_AF}=J_AC_F\), which justifies the source expression.

## 2 An explicit corrected signed Weil Gram identity

Put
\[
a_+=\log(pq),\qquad a_-=|\log(p/q)|>0.
\]
For any translation-invariant Hermitian source form \(T\), define
\[
\mathcal G_T[F]=\frac{\beta_p\beta_q}{2}
\Re\{T(F,U_{a_+}F)+T(F,U_{a_-}F)\}.
\tag{5}
\]
It is a signed contraction of the three-source Gram matrix on
\(F,U_{a_+}F,U_{a_-}F\). Its coefficient matrix has off-diagonal entries
\(\beta_p\beta_q/4\) at positions \(01,10,02,20\) and zero elsewhere;
its eigenvalues are \(0,\pm\beta_p\beta_q/(2\sqrt2)\). Equivalently,
\[
\mathcal G_T[F]=\frac{\beta_p\beta_q}{8}
\sum_{a\in\{a_+,a_-\}}\{T[F+U_aF]-T[F-U_aF]\}.
\tag{6}
\]
All these sources are still prepared. Their common support hull has length
at most \(L+a_+\); complete arithmetic forms on them must include all
prime powers active on that enlarged support.

The unweighted numerators in (4) satisfy
\[
G_{\{p,q\}}-G_{\{p\}}-G_{\{q\}}+I=E_pE_q.
\]
Consequently their mixed trace is
\(\operatorname{Tr}(V^*E_pE_qV)=\mathcal G_{B_S}[F]\). Subtracting
the four identities (4) therefore gives exactly
\[
\mathfrak M_{S;p,q}[F]=\mathcal G_{B_S}[F]+\mathcal R_{\rm met}[F].
\tag{7}
\]
The four shifts in \(E_pE_q\) are \(\pm\log p\pm\log q\); grouping
opposite shifts gives (5), including its coefficient.

Polarize the [finite Euler identity][euler]. For prepared sources of any
fixed compact support it says
\[
B_S=\Gamma-W_S+K_S=Q+W_{\notin S}+K_S,
\quad W_{\notin S}=W_{\rm full}-W_S.
\tag{8}
\]
Here \(Q\) is the complete pole-neutral Weil form, \(W_S\) is the sum
over primes in \(S\), and \(K_S\) is independently defined by its
boundary trace. Thus the requested corrected identity is
\[
\boxed{\mathfrak M_{S;p,q}
=\mathcal G_Q+\mathcal G_{W_{\notin S}}
+\mathcal G_{K_S}+\mathcal R_{\rm met}.}
\tag{9}
\]
Every correction is specified independently of subtracting \(Q\):
the arithmetic term is a finite active prime-power sum on the enlarged
support, the boundary term has the finite Euler trace representation,
and the metric term is (3). The identity holds without assuming that
\(S\) contains the active primes of the original or enlarged sources.

The Gram coefficient matrix is indefinite. Even positivity of the entire
Weil Gram matrix would not by itself sign its contraction in (5). Equation
(9) is an exact comparison with explicit additional terms, not a new sign
mechanism.

## 3 The metric correction has a necessary gamma principal part

Note 01 proved \(\mathfrak M_{S;p,q}=\Delta_p\Delta_qK_S\). Together
with (7) and the first equality in (8), this gives a second description:
\[
\boxed{\mathcal R_{\rm met}
=-\mathcal G_\Gamma+\mathcal G_{W_S}
+\bigl(\Delta_p\Delta_qK_S-\mathcal G_{K_S}\bigr).}
\tag{10}
\]
Section 4 proves that the parenthesized expression is a compact source
form on fixed \(L^2(I_L)\). The arithmetic term is bounded there. Thus
the gamma term in (10) is a principal part of the correction, rather than
an error that can be bounded uniformly by the source norm in every window.

More precisely, suppose \(L>a_-\). Choose real nonnegative
\(h\in C_c^\infty(I_L)\), positive in the interior of its support, with
support diameter \(d\) satisfying
\[
a_-<d<\min(L,a_+).
\]
Then \(\kappa_h(a_-)>0\) and \(\kappa_h(a_+)=0\). Use the exactly
prepared sources from Note 01,
\[
F_\tau=\tau^{-2}\mathcal A(e^{i\tau x}h)
=e^{i\tau x}\left(h-\frac{2i}{\tau}h'
+\frac{\mathcal Ah}{\tau^2}\right),\qquad \tau\to+\infty.
\tag{11}
\]
Their norms tend to \(\|h\|_2>0\). The digamma asymptotic
\(\gamma_\infty(t)=\log|t|-\log(2\pi)+O(|t|^{-1})\), from
[DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2), gives
\[
\mathcal G_\Gamma[F_\tau]
=c_h\cos(\tau a_-)\log\tau+O(1),\qquad
c_h=\frac{\beta_p\beta_q}{2}\kappa_h(a_-)>0.
\tag{12}
\]
To justify the uniform error, center the Fourier variable at \(\tau\).
The envelopes in (11) converge in \(C_c^\infty\), so the low-frequency
tail is uniformly Schwartz and the remaining integral uses the uniform
digamma expansion. The coefficient of \(\log\tau\) is the translated
inner product of the envelope. Replacing the envelope by \(h\) costs
\(O(\tau^{-1}\log\tau)\); the \(a_+\) coefficient is zero.

The finite \(S\)-arithmetic term in (10) is bounded, while its compact
terms tend to zero on the weakly null, bounded family (11). Therefore
\[
\boxed{\mathcal R_{\rm met}[F_\tau]
=-c_h\cos(\tau a_-)\log\tau+O(1).}
\tag{13}
\]
In particular, along \(\tau_n=2\pi n/a_-\) the correction tends to
\(-\infty\), and along \(\sigma_n=(2n+1)\pi/a_-\) it tends to
\(+\infty\), on sources with bounded nonvanishing norms. It has neither
a universal sign nor an \(L^2\)-norm bound on this prepared class. This
is an actual-Sonin statement for every fixed finite \(S\) and quartet;
it concerns \(\mathcal R_{\rm met}\), not the full mixed response.

For example, \(p=2,q=3,L=6/5,S=\varnothing\) includes both active primes
at its final corner and has \(a_-=\log(3/2)<L<a_+=\log6\).
Here \(c_h=(\sqrt6/6)\kappa_h(\log(3/2))\). Thus a bounded-remainder
repair of the proposed finite Weil–Gram reduction fails already for this
first pair. Equations (9)–(10) retain the cancellation that the full
mixed response requires.

## 4 Compactness of the complete mixed source form

Use the actual finite-place boundary operators from Note 01:
\[
Y_A=C_A(I-C_A^2)^{-1}T_A:R_+\mathcal H\longrightarrow\chi\mathcal H,
\qquad K_A[F]=2\Re\operatorname{Tr}(Y_AX_{F,e}),
\]
\[
Y_{\rm mix}=Y_{S\cup\{p,q\}}-Y_{S\cup\{p\}}
-Y_{S\cup\{q\}}+Y_S.
\tag{14}
\]
Every \(Y_A\) is compact because \(C_A\) is compact and its inverse
gap is positive. Combine the four operators before taking absolute bounds.

The closed source comparison §2 already proves the derivative-free estimate
\[
\|X_{F,e}\|_1\le\frac L2\|F\|_2^2.
\tag{15}
\]
Its proof inserts the support interval between the two convolution factors
in \(R_+C_F^*C_F\chi\); their squared Hilbert–Schmidt norms sum to
\(L\|F\|_2^2\). Reflecting the source gives the same bound for the
even multiplier. The argument is independent of the place set. It gives
\[
|\mathfrak M_{S;p,q}[F]|
\le L\|Y_{\rm mix}\|\,\|F\|_2^2.
\tag{16}
\]
For this extension, first allow any \(F\in C_c^\infty(I_L)\), without
moment conditions. The finite Euler identity holds for all such sources,
so the same cancellation identifies the combined boundary form with the
mixed trace there. Polarization and density therefore define a bounded
selfadjoint source operator \(H_{\rm mix,L}\) on all of \(L^2(I_L)\).

Here is a compactness proof that does not assume a multiple-prime
first-return kernel. Approximate the full compact operator \(Y_{\rm mix}\) in operator norm
by finite-rank \(Y_N\). Since the crossing kernel vanishes outside
\(x>0,z>0,x+z<L\), only the restriction from \((0,L)\) to
\((-L,0)\) matters; making that restriction does not increase the
approximation error. Reflect the restricted negative output, and write
\[
\mathcal J1_{(-L,0)}Y_N1_{(0,L)}=\sum_{j=1}^N|v_j\rangle\langle u_j|,
\qquad u_j,v_j\in L^2(0,L),\quad (\mathcal Jy)(z)=y(-z).
\]
Define, using zero extensions,
\[
w_N(s)=\sum_j\int_0^s\overline{u_j(x)}v_j(s-x)\,dx,
\quad k_N(s)=\Re w_N(|s|),\qquad |s|\le L.
\tag{17}
\]
The \(L^2\) convolution makes \(k_N\) continuous, real and even, with
\(k_N(0)=0\). Direct kernel integration gives
\[
2\Re\operatorname{Tr}(Y_NX_{F,e})
=\int_{-L}^L\kappa_F(s)k_N(s)\,ds
=\langle F,H_NF\rangle,
\quad (H_NF)(x)=\int_{I_L}k_N(y-x)F(y)\,dy.
\tag{18}
\]
There is no factor two in the even kernel \(k_N\); the factor two is
in the integral over positive shifts. \(H_N\) is selfadjoint and
Hilbert–Schmidt, though generally not finite rank. Equation (15) yields
\[
\boxed{\|H_{\rm mix,L}-H_N\|
\le L\|Y_{\rm mix}-Y_N\|.}
\tag{19}
\]
Taking a norm-convergent finite-rank boundary approximation proves that
\(H_{\rm mix,L}\) is compact. The same argument applies to each fixed
\(K_A\) and hence, on the enlarged support in §2, to
\(\mathcal G_{K_S}\). This proves the compactness used in (10)–(13).

The extension in (16)–(19) is an extension of the **combined source form**.
Individual \(B_A\) traces need not be finite on every \(L^2\) source;
no subtraction of infinite traces is used. Compactness here also does not
assert a Hilbert–Schmidt source kernel for general finite place sets.
The earlier first-prime proof uses finitely many ratios \(p^k\) on a
bounded logarithmic interval. Ratios involving two primes can be dense,
so that kernel proof cannot simply be copied.

## 5 A constructive signed enclosure with the full source complement

There are two approximation errors to pay. First obtain a boundary
approximation satisfying
\[
\|Y_{\rm mix}-Y_N\|\le\varepsilon_Y.
\tag{20}
\]
One actual-operator estimate for each corner is as follows. Suppose a
selfadjoint finite-rank \(C_{A,N}\) satisfies
\[
\|C_A-C_{A,N}\|\le\varepsilon_A,\quad
\|C_A\|\le c_A<1,\quad\|C_{A,N}\|\le c_{A,N}<1,
\quad I-C_A^2\ge g_AI.
\]
With the actual \(T_A\), define
\(Y_{A,N}=C_{A,N}(I-C_{A,N}^2)^{-1}T_A\). Resolvent subtraction gives
\[
\boxed{\|Y_A-Y_{A,N}\|
\le\frac{\varepsilon_A(1+c_Ac_{A,N})}
{(1-c_{A,N}^2)\sqrt{g_A}}.}
\tag{21}
\]
Indeed \(\|(I-C_A^2)^{-1}T_A\|\le g_A^{-1/2}\) and
\(\|C_A^2-C_{A,N}^2\|\le(c_A+c_{A,N})\varepsilon_A\).
Expanding the resolvent difference gives (21), without assuming the
two compressions commute. Summing the four certified corner errors gives
a permissible \(\varepsilon_Y\), while the finite approximants themselves
are combined with their signs before evaluating the source kernel. Only
finitely many adjoint columns of \(T_A\) enter each approximant; errors
in their evaluation must also be included in (20).

Second approximate the continuous kernel (17) by a finite-rank source
operator. Divide \(I_L\) into equal cells of width \(h=L/n\), with
centers \(x_i\), and use the piecewise constant kernel
\(k_N(x_j-x_i)\) on cell \(i\) times cell \(j\). Call its operator
\(J_{N,n}\), of rank at most \(n\). If
\[
\omega_N(h)=\sup\{|k_N(s)-k_N(t)|:
s,t\in[-L,L],\ |s-t|\le h\},
\]
then the kernel error and Schur bound give
\[
\|H_N-J_{N,n}\|\le L\omega_N(h),\qquad
\eta=L\{\varepsilon_Y+\omega_N(h)\}.
\tag{22}
\]
Evaluation and rounding errors in \(k_N\) add to the quoted modulus
bound. Hence the full-space signed enclosure is
\[
\boxed{J_{N,n}-\eta I\le H_{\rm mix,L}
\le J_{N,n}+\eta I.}
\tag{23}
\]
For the admissible source space, compress to the closed two-moment kernel
\[
\mathcal H_L^0=\{F\in L^2(I_L):\int e^{x/2}F(x)\,dx
=\int e^{-x/2}F(x)\,dx=0\}.
\]
The error is unchanged or reduced. A finite matrix in an orthonormal basis represents the compressed
\(J_{N,n}\) on the span of the projected cell indicators (equivalently,
use their Gram matrix in a generalized eigenvalue problem). Let \(\lambda_-,\lambda_+\) be its extremal eigenvalues. The source
complement remains infinite dimensional, so the scalar bounds are
\[
\boxed{
\bigl(\min(0,\lambda_-)-\eta\bigr)\|F\|_2^2
\le\mathfrak M_{S;p,q}[F]
\le\bigl(\max(0,\lambda_+)+\eta\bigr)\|F\|_2^2.}
\tag{24}
\]
If the finite span is zero, both finite spectral endpoints are taken as
zero. The \(\eta I\) allowance covers the full source complement and
cannot be removed by a favorable finite matrix. This is a signed enclosure
construction whose hypotheses are approximation errors for independent
actual operators, rather than an assumed Weil inequality.

## 6 Scope and the next useful input

Equation (9) answers the corrected-identity question, and (13) shows why a
bounded or one-sided metric remainder is unavailable when \(L>a_-\).
Equations (19)–(24) instead keep the full mixed cancellation and give a
route to signed bounds on its compact source operator. None has yet been
evaluated for an actual pair, so there is no signed numerical margin to
report. The original global inequality is unchanged.

The next concrete diagnostic, if pursued, is to enclose the combined
operator for a declared quartet and fixed support, including (20), the
kernel modulus and all source-complement errors. Before running it, choose
the error tolerance, resource cap and the residual budget its resulting
upper or lower endpoint would improve. A bare finite source matrix, the
sign of one sector in (9), or a large correction coefficient from (13)
does not supply that improvement. Formal review follows the coherent
round output under the [portfolio cadence][portfolio]; no cross-model
review is claimed by this continuation.

The controls retain their scopes from Note 01 and [summary 12][s12]. The
generic prepared two-dimensional example excludes a sign inference from
projection algebra; it lacks the actual Sonin projection. Smooth-density
controls alter the prime measure, and the two-channel obstruction concerns
a specified separated architecture, not the paired expression here.
Euler-factor collision controls change the arithmetic family;
weighted-square controls lack full reflection; reflected controls lack
the integer-square source; smooth/primitive controls lack the full theta
arithmetic. These identities assert no noncollision theorem based only on
their shared properties. No universal exclusion of collective prime
estimates is inferred.

[n01]: 01_EXACT_MIXED_RESPONSE_AND_FINITE_TRANSLATE_OBSTRUCTION_CODEX_20261017.md
[euler]: ../../../../investigations/sonin-critical-boundary/notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md
[closed]: ../../../../investigations/sonin-critical-boundary/notes/CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md
[compact]: ../../../../investigations/sonin-critical-boundary/notes/COMPACT_CORRECTION_AND_REVISED_B_20261003.md
[portfolio]: ../../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md
[results]: ../../../../../result-summaries/README.md
[s07]: ../../../../../result-summaries/07_sonin_critical_boundary.md
[s12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
