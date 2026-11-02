# J-E01 r1: representation audit and origin/tail feasibility return

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**.

**Complete bounded return: the representation and classical normalization
pass, but the proposed curvature condition fails near the origin.**
For the complete canonical source at physical heat time zero,
\(R'(u)>0\) and \(C(u)<0\) for all sufficiently small positive \(u\).
Both signs are positive eventually in the tail. This rejects the
everywhere monotone-convex source-curve mechanism selected by J-B01;
it does not reject the integral representation, coefficient positivity,
or arguments allowing signed integration. **Next: [B] J-B01 — Astra.**

| Check in [frozen r1][request] | Return |
| --- | --- |
| Real coefficient-determinant representation, every finite \(r\ge1,k\ge0\) | Verified, including all lower endpoints and chamber constant |
| Csordas–Varga specialization and ordinary/exponential normalization | Verified, including \(k=1\) |
| Convex-graph lemma, Jacobi reconstruction and signed derivative algebra | Verified as identities/conditional implication |
| Origin: \(R'\), \(C\) | Positive, **negative**, respectively, near zero |
| Tail: \(R'\), \(C\) | Both eventually positive; no effective cutoff obtained |

## 1. Contract, inputs and evidence

This executes only J-E01 **r1**, [Note01 Section 7][request]. The
[progress register][progress] owns status. The request-bearing Note01 hash
is unchanged:
`a2097d5952d1767781a6a0917f2acfd98b64d21f9a393755d62686863aae1717`.
HEAD remains `c97b376dcbf81f05ea3a4f7d360da168af4a1345`; research inputs
include uncommitted files. Shared Note02, Note03 and Continuation04 match
their frozen hashes. The [execution record][record] records actual input
and code hashes. The Jensen overview's actual hash before this return's
navigation update is
`813c34b97347503a8a20d98c4659d376065a08e8acb8374a81bcf6e4ff43ce88`;
the Active progress-register version is
`c0802009dab0133b82355d082c441393639e1e58ffb9f160c1a4d78b306f5953`.
Nothing was reset to a historical version.

The [standard-library calculation][code] generates only \(Q_0,\ldots,Q_8\),
checks the mixed identities and rational sign proofs below, and records
the full signed polynomial coefficients. There is **no numerical theta
acquisition**, grid, coefficient scan, higher-order sign test or new heat
flow. Exact rational inequalities suffice; the optional 128/256-bit
acquisition was unnecessary. All exact identity and sign assertions in
the recorded calculation pass.

This is an in-note derivation with exact algebra and same-session,
same-model contributing checks; it is not independent specialist review.
The internal endpoint cross-check corrected the second quotient derivative
to the coefficient **7** in (7) below before the retained record was run.
No correction to the frozen request or its representation is needed.

Read with the [result index][results], especially [theta identities][theta]
and [controls][controls], and the [avoid index][avoid], especially
[normalization][normalization], [joint expressions][joint],
[scoped exclusions][scopes] and [imports][imports]. This is a precise
obstruction to one sufficient source condition, not an RH-equivalent
reformulation being numerically supported.

## 2. Integral, endpoints and ordered chamber

Keep \(b_n=\int_0^\infty u^{2n}\Phi(u)\,du\),
\(c_n=b_n/(2n)!\), \(\gamma_n=n!c_n\), and \(c_n=0\) for \(n<0\).
Modular reflection gives the smooth even extension of \(\Phi\), so every
odd derivative at zero vanishes. For every fixed derivative order \(s\),
the differentiated theta series gives
\[
|\Phi^{(s)}(u)|=O_s\bigl(e^{(4s+9)u-\pi e^{4u}}\bigr)
\quad(u\to\infty).
\]
The derivative of one summand is an exponential times a polynomial of
degree at most \(s+2\) in \(\pi n^2e^{4u}\); the omitted summands are
dominated by a convergent polynomially weighted Gaussian sum. Thus all
polynomially weighted absolute derivative integrals and boundary limits
used below exist. There is no derivative-order-uniform bound asserted.

For \(f_m=u^{2m}/(2m)!\), repeated integration by parts gives
\[
\int_0^\infty f_m\Phi^{(2i)}
=\left[\sum_{\ell=0}^{2i-1}(-1)^\ell f_m^{(\ell)}
\Phi^{(2i-1-\ell)}\right]_0^\infty
+\int_0^\infty f_m^{(2i)}\Phi=c_{m-i}. \tag{1}
\]
For \(m\ge i\), every endpoint vanishes and the remaining integral is
the defining moment. For \(m<i\), the polynomial derivative is zero
and the sole possible endpoint is
\(-\Phi^{(2i-2m-1)}(0)=0\). Its order is positive and odd. No negative
factorial is used, including \(m=0<i\).

Apply determinant composition with \(m=k+j\). Absolute convergence
follows by finite expansion into products of the integrals just bounded:
\[
D_{r,k}=\frac1{r!}\int_{(0,\infty)^r}
\det[\Phi^{(2i)}(u_\ell)]_{i,\ell}
\det\!\left[\frac{u_\ell^{2k+2j}}{(2k+2j)!}\right]_{j,\ell}
\,d\mathbf u.
\]
The product is symmetric under permutations of the integration variables.
The \(r!\) ordered chambers cancel \(1/r!\), giving exactly
\[
D_{r,k}=\frac{\displaystyle\int_{0<u_1<\cdots<u_r}
\left(\prod_\ell u_\ell^{2k}\right)
\prod_{a<b}(u_b^2-u_a^2)
\det[\Phi^{(2i)}(u_\ell)]_{i,\ell}\,d\mathbf u}
{\displaystyle\prod_{j=0}^{r-1}(2k+2j)!}. \tag{2}
\]
This holds for every finite \(r\ge1,k\ge0\), including \(k<r-1\).
At \(k=0\), the coefficient matrix is upper triangular, so
\(D_{r,0}=c_0^r\), with no exception to (2).

## 3. Required classical normalization

In the specialization \(f=1,\lambda=0\) of
[Csordas–Varga][cv], set
\(q(u)=-\Phi'(u)/(u\Phi(u))=-2(\log S)'(u^2)\),
\(S(x)=\Phi(\sqrt x)\). Their Theorem 2.1 gives \(q'(u)>0\).
For \(j\ge0\), integration by parts gives
\(\int_0^\infty u^{2j+2}\Phi(u)q(u)\,du=(2j+1)b_j\).
Expanding the complete signed double integral therefore gives, for \(k\ge1\),
\[
\begin{aligned}
I_k&=\iint u^{2k}v^{2k}\Phi(u)\Phi(v)(v^2-u^2)
 [q(v)-q(u)]\,du\,dv\\
&=2(2k+1)b_k^2-2(2k-1)b_{k-1}b_{k+1}>0. \tag{3}
\end{aligned}
\]
Both differences have the same sign off the diagonal. This reproduces
the cited Proposition 2.2 transfer; no lower endpoint or negative moment
is omitted at \(k=1\). Factorial conversion gives
\[
T_k^\gamma=\left(\frac{k!}{(2k)!}\right)^2
\left[b_k^2-\frac{2k-1}{2k+1}b_{k-1}b_{k+1}\right]>0,
\quad
D_{2,k}=\frac{T_k^\gamma+\gamma_{k-1}\gamma_{k+1}/(k+1)}{(k!)^2}>0.
\tag{4}
\]
In particular,
\(T_1^\gamma=b_1^2/4-b_0b_2/12\) and
\(D_{2,1}=b_1^2/4-b_0b_2/24=T_1^\gamma+b_0b_2/24\).
This is the mandatory known baseline, not a new coefficient estimate.

Inspection scope: printed pp.177–181 of the existing archived reading
copy, Theorem 2.1, multiplier (2.11), Proposition 2.2 and Theorem 2.4
were visually checked by a contributing same-model audit. Section 3's
constructive proof was not audited. The archive hash remains the one in
the shared catalog; no new literature claim or download is needed.

## 4. Conditional transfer and exact Jacobi algebra

For \(R=\Phi''/\Phi\), \(T=\Phi^{(4)}/\Phi\), and
\(C=R'T''-T'R''\), the three-source-point determinant factors as
\(\prod_j\Phi(u_j)\det[1;R(u_j);T(u_j)]\).
If \(R'>0\), then \(d^2T/dR^2=C/(R')^3\). At ordered nodes its last
determinant equals
\[
(R_2-R_1)(R_3-R_1)
\left[\frac{T_3-T_1}{R_3-R_1}-\frac{T_2-T_1}{R_2-R_1}\right].
\]
Thus the proposed \(R'>0,C\ge0\) imply the claimed order-three sign.
The lemma is correct; the canonical source does not satisfy its premise.

Use the unchanged Jacobi vector field in [shared Note02][closure],
\(L=4u\), \(B=e^{L/4}\theta_3(e^L)\),
\(Q_0=U+\tfrac32(a^2-1)\), and
\(Q_{j+1}=\mathcal DQ_j+aQ_j/4\). Since \(B'/B=a/4\),
\[
\Phi^{(j)}(u)=4^jB(4u)Q_j/8.
\]
The reconstruction follows also from
\(p=(B(4u)-e^u)/2\) and
\(p''-p=B(4u)(4a'+a^2-1)/2=B(4u)Q_0=8\Phi\).
This checks [Planat–Solé (5.10)–(5.12)][ps] in this normalization;
their concavity certificates are not inputs. Differentiation and row
factoring give precisely Note01 (10)–(11), including the factor
\(4^{r(r-1)}/8^r\) in the source determinant.

Writing \(q_j=Q_j(Z(4u))\), complete signed expressions are
\[
\boxed{R'=\frac{2^6(q_0q_3-q_1q_2)}{q_0^2}},\qquad
\boxed{C=\frac{2^{18}}{q_0^3}
\left(q_0q_3q_6-q_0q_4q_5-q_1q_2q_6
+q_1q_4^2+q_2^2q_5-q_2q_3q_4\right)}. \tag{5}
\]
The six-term mixed numerator is the determinant
\(\det[q_0,q_1,q_2;q_2,q_3,q_4;q_4,q_5,q_6]\).
The record contains all \(Q_j\) (3,4,8,11,18,24,35,45,61 terms) and
the expanded 21-term and 151-term numerators in \((a,U,\chi)\).
It verifies quotient differentiation and the mixed cancellation before
any signs are taken. For example, putting
\(A=q_0q_3-q_1q_2\), \(B_1=q_0q_5-q_1q_4\),
\[
\begin{aligned}
D_R&=q_0^2q_4-q_0q_2^2-2q_0q_1q_3+2q_1^2q_2,\\
D_T&=q_0^2q_6-q_0q_2q_4-2q_0q_1q_5+2q_1^2q_4,
\end{aligned}
\]
then \(AD_T-B_1D_R=q_0^2N\), where \(N\) is the numerator in (5).
All displayed denominators are positive: \(B>0\), and every theta
summand is positive for \(u\ge0\), so \(q_0=8\Phi/B>0\).

## 5. Origin: exact obstruction within the eighth derivative

Set \(z=U(0)\), \(p_j=4^jQ_j(0,z,0)\),
\(e_j=\Phi^{(j)}(0)/\Phi(0)=p_j/p_0\).
Odd \(p_j\) vanish, and the recurrence gives
\[
\begin{aligned}
p_0&=z-3/2,\\
p_2&=-2z^2-45z+15,\\
p_4&=204z^3+382z^2+3600z-570,\\
p_6&=6792z^4-103020z^3-86732z^2-473220z+44340,\\
p_8&=-419184z^5-7138392z^4+50105664z^3
+25608112z^2+92818800z-5767320. \tag{6}
\end{aligned}
\]
For \(x=u^2\), write \(\widehat R(x)=R(\sqrt x)\),
\(\widehat T(x)=T(\sqrt x)\). Taylor division through \(x^2\) gives
\[
\begin{aligned}
\widehat R'(0)&=(e_4-e_2^2)/2,&
\widehat T'(0)&=(e_6-e_2e_4)/2,\\
\widehat R''(0)&=(e_6-7e_2e_4+6e_2^3)/12,&
\widehat T''(0)&=(e_8-6e_2e_6+6e_2^2e_4-e_4^2)/12. \tag{7}
\end{aligned}
\]
The coefficient 7 includes both numerator/denominator cross terms in
the quotient. Combining (7) before estimating gives
\[
\widehat R'(0)=\frac{A_0(z)}{2(z-3/2)^2},\quad
H_0:=\widehat R'(0)\widehat T''(0)-\widehat T'(0)\widehat R''(0)
=\frac{N_0(z)}{24(z-3/2)^3}, \tag{8}
\]
where
\[
A_0=200z^4-104z^3+1062z^2-4620z+630,
\]
\[
\begin{aligned}
N_0&=\det\begin{pmatrix}p_0&p_2&p_4\\p_2&p_4&p_6\\p_4&p_6&p_8\end{pmatrix}\\
&=-144000000z^9-14169600z^8+75393792z^7-292523904z^6\\
&\quad+50243245056z^5-116509484160z^4-3665813760z^3\\
&\quad-118349320320z^2+31853606400z-1257379200.
\end{aligned}
\]

There is an exact sign certificate without high-precision acquisition.
For \(z=s+47/10\),
\[
A_0=11146451/125+(2038228/25)s+(130518/5)s^2+3656s^3+200s^4>0
\quad(s\ge0).
\]
All coefficients of \(-N_0(s+47/10)\), in ascending powers, are positive:
\[
\begin{gathered}
8463384528037456608/78125,\quad3746831892646326696/15625,\\
715213161129392928/3125,\quad3065507985611376/25,\\
1021377866198976/25,\quad221477700264768/25,\quad6312096285696/5,\\
114971943168,\quad6105369600,\quad144000000.
\end{gathered}
\]

The canonical endpoint satisfies the needed lower bound. From
\(A(0)^2=4U(0)\) and \(A(0)=\pi\theta_3(1)^4\),
\[
z=\pi^2\theta_3(1)^8/4>
\frac{(157/50)^2}{4}(1+2\cdot3/70)^8
=\frac{6698045526361744}{1407422119140625}>47/10. \tag{9}
\]
Here \(157/50<\pi<22/7\) and \(e^{22/7}<70/3\), so
\(e^{-\pi}>3/70\) and \(\theta_3(1)>1+2e^{-\pi}\).
The script verifies the coarse pi bounds via Machin's identity and
alternating rational arctangent sums. For the exponential it uses the
rational upper bound
\(\sum_{j=0}^{20}q^j/j!+[q^{21}/21!]/(1-q/22)\), \(q=22/7\).
All omitted theta terms are positive, so discarding them is valid for
this analytic lower bound; no theta-tail approximation is being claimed.

Equations (8)–(9) prove \(\widehat R'(0)>0\), \(H_0<0\).
The exact chain rule gives
\[
R'=2u\widehat R',\qquad C=8u^3
(\widehat R'\widehat T''-\widehat T'\widehat R'').
\]
Analytic evenness therefore gives
\[
\boxed{R'(u)=2\widehat R'(0)u+O(u^3)>0,\quad
C(u)=8H_0u^3+O(u^5)<0}
\]
for all sufficiently small positive \(u\). Only the leading coefficients
were acquired, using derivatives through eight; the remainder statement
uses analyticity, not an additional derivative computation or interval
cutoff. Thus \(C(0)=0\) is a removable vanishing factor, while its required
sign on the adjacent punctured interval is definitively wrong.

## 6. Tail: both signs pass with differentiated remainder

Put \(t=\pi e^{4u}\). For the first summand,
\[
\phi_1=e^u(2t^2-3t)e^{-t},\qquad
(\log\phi_1)'=9-4t+12/(2t-3).
\]
Generate only the needed summand polynomials
\(P_0(y)=2y^2-3y\),
\(P_{j+1}=4yP_j'+(1-4y)P_j\), through \(j=6\). Then
\(\Phi^{(j)}=e^u\sum_{n\ge1}P_j(n^2t)e^{-n^2t}\).
Let \(M_j\) be the sum of absolute coefficients of \(P_j\), and
\(K_j=\sum_{n\ge2}n^{2j+4}e^{-(n^2-4)}<\infty\).
For \(t\ge1\) the differentiated omitted sum obeys
\[
|E_j|\le e^uM_jK_jt^{j+2}e^{-4t},\qquad0\le j\le6. \tag{10}
\]
The same dominating sums justify termwise differentiation. In particular
\(E_j/\phi_1=O(t^je^{-3t})\) as \(t\to\infty\).

For an exact first-summand check, put \(d=2t-3\),
\(A_t=P_2(t)/t\), \(B_t=P_4(t)/t\),
\(r=A_t'd-2A_t\), \(s=B_t'd-2B_t\). Then
\[
R_1'=4tr/d^2,\qquad C_1=64t^3(rs'-sr')/d^4.
\]
The record gives the full polynomials; their leading terms are
\(r=128t^3+O(t^2)\), \(rs'-sr'=2^{20}t^7+O(t^6)\).
Equivalently,
\[
\begin{aligned}
R_1'&=128t^2(1+O(t^{-1})),&R_1''&=1024t^2(1+O(t^{-1})),\\
T_1'&=4096t^4(1+O(t^{-1})),&T_1''&=65536t^4(1+O(t^{-1})).
\end{aligned}
\]
Forming the full mixed expression first gives
\(C_1=2^{22}t^6(1+O(t^{-1}))\). Propagating (10) through the
normalized quotient derivatives gives
\(R'=R_1'+O(t^3e^{-3t})\),
\(R''=R_1''+O(t^4e^{-3t})\),
\(T'=T_1'+O(t^5e^{-3t})\),
\(T''=T_1''+O(t^6e^{-3t})\), and hence
\[
\boxed{R'\sim128t^2>0,\qquad C\sim2^{22}t^6>0}.
\]
The curvature remainder is \(O(t^8e^{-3t})\), negligible relative to
\(t^6\). These are eventual signs, not a computed effective cutoff.

## 7. Controls, scope and continuation

The [registered controls][controls] retain exactly the premise screen in
Note01 Section 5. Euler-factor and altered weighted-square sources fail
the complete canonical orbit/reconstruction; finitely matched endpoints
do not license all odd-derivative cancellations. Fully reflected
super-Gaussian sources retain the generic endpoint identity but fail
canonical reconstruction. Smooth positive-primitive and scalar
source-concavity controls do not supply the derivative-ratio conditions.
No uncomputed claim that these controls fail \(R'>0,C\ge0\) is made.
Positive-time collisions do not contradict a finite-order coefficient
statement at time zero. No new collision computation is needed for this
audit of a premise that the actual theta source itself fails.

**The failed condition is the everywhere requirement \(C\ge0\) for this
particular source curve.** The local concave graph even gives negative
three-node source determinants when all nodes are sufficiently near
zero. This does not determine their weighted integral. The exact
representation, classical order-two baseline, and recorded known
order-three coefficient positivity retain their status. No passage from
weak consecutive positivity to all minors, or from this finite pilot to
RH, is asserted.

J-E01 is complete with a scoped failed feasibility test. Return to
**[B] J-B01 — Astra** to choose whether to retain (2) with a mechanism
that allows signed source determinants or change the selected mechanism.
Do not send the now-false global curvature premise to J-B02. The
[model-change continuation][continuation] supplies the reading order and
pasteable prompt. No further research task is started by this return.

[request]: 01_J_B01_COEFFICIENT_REPRESENTATION_DECISION_20261101.md#7-frozen-execution-request-j-e01-r1
[progress]: ../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[closure]: ../../notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md
[code]: ../numerics/j_e01_audit.py
[record]: ../numerics/J_E01_R1_EXACT_RECORD_20261101.json
[continuation]: 04_CONTINUATION_AFTER_J_E01_ORIGIN_OBSTRUCTION_20261101.md
[cv]: https://www.math.kent.edu/~varga/pub/paper_161.pdf
[ps]: https://arxiv.org/html/2608.19160v1#S5.SS1
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[normalization]: ../../../../../avoid/08_normalization_and_constant_slips.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[imports]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
