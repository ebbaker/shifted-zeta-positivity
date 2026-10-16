# Limits of composite replication, row weights, and inherited lower-order families

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and configured reasoning-effort label are not exposed to this agent and are not inferred.

Status: elementary conditional deductions about extraction from the existing short-family moment. No moment estimate or new zero-free region is proved. The statements concern explicitly selected rows and inherited moment bounds; no classification of all phase-trivial rows is needed.

## 1. All composite sixth powers give an equivalent repeated-row obligation

Use the fixed field, character, excluded set, profile, and zero extension of [the short-family refinement](1_SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md), equations (1)--(4). In particular, let

\[
 A(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)W(Nn/D),\qquad
 B_r(D)=A_{r^6}(D)
       =\sum_{(n,Sr)=1}\mu_K(n)\nu(n)W(Nn/D).
\]

Here integral ideals outside \(S\) have their fixed primary generators; the rows \(r^6\) are distinct. Put \(Q=D^{h/6}\), \(0<h\le1\), and

\[
 \mathcal C_h(D)=Q^{-1}\sum_{Nr\le Q\atop(r,S)=1}|B_r(D)|^2.
\]

For every fixed \(\beta>0\), the following are equivalent, with the usual quantifier “for every \(\varepsilon>0\)”:

\[
 A(D)\ll D^{\beta+\varepsilon}
 \quad\Longleftrightarrow\quad
 \mathcal C_h(D)\ll D^{2\beta+\varepsilon}.
 \tag{1}
\]

**Proof, including the composite masks.** For every fixed \(r\), exact Euler-factor completion and its inverse give

\[
 A(D)=\sum_{d\mid\operatorname{rad}(r)}\mu_K(d)\nu(d)B_r(D/Nd),
 \qquad
 B_r(D)=\sum_{\operatorname{rad}(d)\mid\operatorname{rad}(r)}
             \nu(d)A(D/Nd).
 \tag{2}
\]

The second sum allows arbitrary prime powers but is finite by the annular support. These are identities of the original masked sums, not an assertion that a sixth-power row equals the unmasked row.

If the left side of (1) holds, then for any \(\delta>0\),

\[
 |B_r(D)|\ll D^{\beta+\delta}
       \prod_{p\mid r}(1-(Np)^{-\beta-\delta})^{-1}.
 \tag{3}
\]

For every \(\eta>0\), this product is \(\ll_{\beta,\delta,\eta}(Nr)^\eta\). Indeed, for all sufficiently large prime norms, each local factor is at most \((Np)^\eta\); the remaining finitely many local factors contribute one fixed constant. Since \(Nr\le Q\), ideal counting and sufficiently small choices of \(\delta,\eta\) give the right side of (1).

Conversely, retain only prime ideals with \(Q/2<Np\le Q\). Their number is \(J\asymp Q/\log Q\), so the right side of (1) implies

\[
 J^{-1}\sum_{Q/2<Np\le Q}|B_p(D)|^2\ll D^{2\beta+\varepsilon}.
\]

The extra factor \(Q/J\ll\log Q\) is absorbed in the arbitrary epsilon loss. The prime-row completion argument in the refinement then gives

\[
 P(t)\Longrightarrow P(\max\{\beta,(1-h/6)t\}).
\]

Starting from ideal counting \(P(1)\), finitely many reuses give \(P(\beta)\) when \(\beta<1\); for \(\beta\ge1\), ideal counting already suffices. This proves (1).

**Necessary qualification.** An arbitrary composite \(r\asymp Q\) can have a fixed small prime factor. One cannot replace the prime deletion estimate by the uniform claim \(|A(D)-B_r(D)|\ll(D/Q)^t\). The inverse product (3), rather than that false deletion estimate, proves the forward direction. The reverse direction deliberately returns to the large-prime subsum.

There are \(\asymp Q\) explicit composite sixth-power rows, compared with \(\asymp Q/\log Q\) prime sixth-power rows. Replacing primes by all composites therefore improves the count only logarithmically. Inserting the existing full-family hypothesis

\[
 \sum_{0<Nu\le D^h}|A_u(D)|^2\ll D^{1+a+h+\varepsilon}
 \tag{4}
\]

into (1) gives exactly

\[
 b_6(h,a)=\frac{1+a}{2}+\frac{5h}{12}.
 \tag{5}
\]

Thus the normalized all-composite repeated-row estimate remains equivalent to its target fixed-character bound. This is a statement about that positive subsum; it does not say that the rest of the full family contains no additional useful information.

## 2. Row weights cannot improve the replication power by themselves

For any \(R\) selected explicit sixth-power rows and any complex weights \(w_r\),

\[
 \left|\sum_r w_rB_r(D)\right|^2
 \le\left(\sum_r|w_r|^2\right)\sum_r|B_r(D)|^2.
 \tag{6}
\]

If the desired coherent signal is \((\sum_r w_r)A(D)\), its effective replication factor is

\[
 J_{\rm eff}=\frac{|\sum_r w_r|^2}{\sum_r|w_r|^2}\le R\ll D^{h/6}.
 \tag{7}
\]

The inequality is sharp for equal weights. Negative or complex weights cannot raise this upper bound. Combining (4), (6), and (7) cannot give a moment contribution smaller than the power in (5). Weighted prime deletion or an exact divisor identity must additionally pay its own error or smaller-scale terms; removing those terms cannot increase the available \(J_{\rm eff}\).

Equivalently, for nonnegative energy weights \(\lambda_r\), the unweighted moment alone gives \(\sum\lambda_r|B_r|^2\le\|\lambda\|_\infty M\). Division by \(\sum\lambda_r\) gains at most \(R\), since \(\sum\lambda_r/\|\lambda\|_\infty\le R\).

This is a sharp bound for extraction using the unweighted moment and Cauchy--Schwarz. It is not a no-go theorem against a new signed correlation estimate, an estimate for a stronger weighted moment, or a coefficient-specific identity that uses additional cancellation.

## 3. Quadratic or cubic subfamilies inherited from the sextic moment have exactly the same floor

For a genuine order-\(d\) family, assume \(a_d\ge0\) and
\(0<h_d<d\), so its scale contraction lies strictly between zero
and one. With its *own* hypothesis

\[
 \sum_{Nv\le D^{h_d}}|C_v(D)|^2\ll D^{1+a_d+h_d+\varepsilon},
\]

the same prime-power completion argument gives

\[
 b_d(h_d,a_d)=\frac{1+a_d}{2}+\frac{d-1}{2d}h_d,
 \qquad c_d=1-\frac{h_d}{d}.
 \tag{8}
\]

It retains \(\chi_n^{(d)}(p^d)=\mathbf1_{p\nmid n}\), and finite reuse removes the prime-mask error just as before. At equal \(h_d,a_d\), smaller \(d\) is a genuine extraction advantage, but equality of the moment inputs must be proved.

For \(d\mid6\), take \(k=6/d\) and select the sextic rows \(u=v^k\). Their values are exactly those of the order-dividing-\(d\) character \(\chi_n(v)^k\), with the same zero extension. The map has multiplicity at most k on nonzero element rows, so restriction changes the inherited moment only by a fixed factor. Its row length is

\[
 h_d=\frac{dh}{6}.
\]

The inherited upper bound remains \(D^{1+a+h+\varepsilon}\). Written in the normalization of (8), it has

\[
 a_d=a+h-h_d.
\]

Consequently,

\[
 \boxed{\quad
 b_d\left(\frac{dh}{6},a+h-\frac{dh}{6}\right)
 =\frac{1+a}{2}+\frac{5h}{12},\qquad
 c_d=1-\frac h6.
 \quad}
 \tag{9}
\]

In particular, quadratic rows \(u=v^3\) have \(h_2=h/3\), \(a_2=a+2h/3\); cubic rows \(u=v^2\) have \(h_3=h/2\), \(a_3=a+h/2\). Their repeated rows \(v=p^d\) map to the original \(u=p^6\). Neither the count, the mask, the recurrence, nor the final exponent has improved.

For example, \(h=8/9,a=0\) gives \(47/54\) in all three presentations. The inherited quadratic parameters are \((h_2,a_2)=(8/27,16/27)\); the cubic parameters are \((4/9,4/9)\). Exact rational arithmetic checked these identities, also at \(h=2/3\) and with a nonzero loss. These checks concern exponent bookkeeping only.

A useful quantitative target follows: a new bound on the selected order-\(d\) family that saves \(D^\sigma\) over its inherited bound would improve the extracted exponent by exactly \(\sigma/2\). Merely changing the name or parametrization of the family saves nothing.

## 4. Fixed-core repetitions and their scope

For a fixed core \(v\), the rows \(u=vr^6\) satisfy the exact identity

\[
 A_{vr^6}(D)=\sum_n\mu_K(n)\nu(n)\chi_n(v)
                  \mathbf1_{(n,r)=1}W(Nn/D).
 \tag{10}
\]

They replicate the twisted target \(A_v\), with its existing zeros at primes dividing \(v\); they do not automatically replicate \(A_1\). For \(p\nmid vS\), the completion coefficient is \(\nu(p)\chi_p(v)\), not merely \(\nu(p)\). Their count is at most \(O((D^h/Nv)^{1/6})\). A fixed finite list of cores changes constants only. Growing cores introduce growing twists and cannot inherit fixed-character constants without an additional uniformity theorem.

The preceding results count explicit sixth powers and fixed cores. They do not classify all possible phase-trivial rows or rule out an approximation using other rows on a finite annulus. Such an approximation would need a new correlation estimate for the actual coefficients, including every deleted-prime mask and any dependence on growing conductors.

## Research consequence

Composite rows, free row weights, and lower-order subfamilies inherited solely from the same sextic moment do not improve the power floor. The productive target is an actual power saving in a specified selected-family moment or in the signed residual, rather than a larger bookkeeping collection of repeated rows. The existing small-cofactor reduction remains the place where a new analytic estimate is required; this note does not estimate that residual.
