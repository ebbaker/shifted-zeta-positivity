# Original-inverse centered comparison: a quantified next route

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred. Parallel audits are
same-model internal checks, not independent specialist review or formal
verification.

This calculation follows the review of [Note 25](25_SQUAREPART_REMOVAL_AND_SMOOTH_OBSTRUCTION_20261009.md).
Under the imported source inputs, centering the **original** inverse-times-two-plain
product has a complete selected comparison saving exceeding 1/700 on the
certified operational region. The corresponding centered mixed moment is
still unproved. The positive comparison is not uniform on the larger coarse
working box.

## 1 The exact object and imported inputs

Keep the original inverse \(M_u\), plain profile \(B\), twists, physical
zeros, whole prime subset \(J\), and selected family \(\mathcal C_+\).
Write \(N=U^m\), \(D=U^r\), and
\[
 S_u(Y)=Y^{-1/2}\sum_l\psi_u(l)B(q_l/Y),\qquad
 T_u=M_uQ_J(u)S_u(N)^2,
 \quad F=\sum_{u\in\mathcal C_+}|T_u|^2.
\]
Use the source's original fixed profile convention at every length; no
character is divided out. As in Notes 22–25,
\[
 F\ll_\varepsilon U^{1+dr+12re_{\rm src}+\varepsilon}H^b.
 \tag{1}
\]

The [30 September source manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
printed p. 115, Lemma 17.1, supplies a marked inverse second moment for
**every subcollection of the original slots**, under its fixed native
presentation, coefficient, height and strict capacity hypotheses. Thus
the required input is directly
\[
 \sum_{u\in\mathcal C_+}|M_uQ_J(u)|^2
 \ll_\varepsilon U^{1+\varepsilon}H^b. \tag{2}
\]
It is not inferred by dividing a moment for \(Q_I\) by omitted slots.
The source norm is first formed on the selected family and then enlarged
positively to its theorem domain. Since \(z_J\le2/45\) and \(r<73/100\),
its capacities have fixed room:
\[
 r+2z_J\le737/900<1,\qquad
 2r+8z_J\le817/450<3. \tag{3}
\]
The original disjoint supports, excluded primes and bounded row-independent
slot coefficients still matter.

For the same permitted plain profile, source (8.1)–(8.2), printed pp. 57–58,
give the direct and reflected bounds
\[
 |S_u(U^y)|^2\ll_\varepsilon
 U^{dy+12ye_{\rm src}+\varepsilon}H^b,
 \qquad
 |S_u(U^y)|^2\ll_\varepsilon
 U^{d(1-y)+(24-12y)e_{\rm src}+\varepsilon}H^b.
 \tag{4}
\]
Their nonprincipal bin, all-length and profile hypotheses remain imported.
A parallel source audit checked the displayed statements in memory against
PDF SHA-256 `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`;
it did not reprove the source estimates. No third-party PDF was saved.

## 2 Center the original product before truncating the inverse

Set
\[
 Y_1=U^{1/4},\qquad Y_2=U^{2m-1/4},\qquad Y_1Y_2=N^2,
\]
and define
\[
 R_u=M_uQ_J(u)S_u(Y_1)S_u(Y_2),\qquad
 \Delta_u=T_u-R_u,
 \quad F_R=\sum_{u\in\mathcal C_+}|R_u|^2,
 \quad F_c=\sum_{u\in\mathcal C_+}|\Delta_u|^2. \tag{5}
\]
This is an additive identity with unchanged selected rows. The shorter
plain exponent is 1/4; the longer is \(2m-1/4\in(11/20,289/500)\)
on the coarse box. Apply the direct bound in (4) to the shorter factor
and the reflected bound to the longer one. Their literal squared buffer
costs are \(3e_{\rm src}\) and \((27-24m)e_{\rm src}\), respectively.
Together with (2),
\[
 F_R\ll_\varepsilon
 U^{1+d(3/2-2m)+(30-24m)e_{\rm src}+\varepsilon}H^b. \tag{6}
\]
Its saving relative to \(U^{1+dr}\) is
\[
 \lambda_R=d(r+2m-3/2)-(30-24m)e_{\rm src}. \tag{7}
\]

Weighted Hilbert Cauchy controls the complete comparison:
\[
 F-F_c=2\operatorname{Re}\langle T,R\rangle-F_R,
 \qquad |F-F_c|\le2\sqrt{F F_R}+F_R. \tag{8}
\]
Combining (1) and (6), its cross saving is exactly
\[
 \boxed{\delta_c=\frac d2(r+2m-3/2)
                   -(15-12m+6r)e_{\rm src}.} \tag{9}
\]
The calculation uses the marked second moment of the original \(M\).
There is no imported marked second moment for \(M_\dagger\), so one
must not silently replace \(M\) by that residual in this proof.

## 3 A conservative certified margin on the actual operational region

The existing [operational certificate](../../numerics/mixed_conductor_refinement_certificate_20261008.json)
and manuscript appendix enclose every actual operational tuple by
\[
 r>70571698/10^8,\qquad m>40398543/10^8,\qquad d\ge9/25.
\]
These enclosures are imported here. The certificate at review has SHA-256
`83d7a10a3d2200d41414c14012b74fa45fcb72be8831534b88a00c37559b3df4`.
They yield
\[
 d(r+2m-3/2)>769941/156250000=0.0049276224.
\]
Using the coarser upper cost \(15-12m+6r\le729/50\) and
\(0<e_{\rm src}\le1/1200000\),
\[
 \delta_c\ge\frac{6129153}{2500000000}=0.0024516612,
 \qquad
 \delta_c-\frac1{700}\ge
 \frac{17904071}{17500000000}=0.0010230897714\ldots. \tag{10}
\]
The correction square is stronger: using \(30-24m\le102/5\),
\[
 \lambda_R\ge3069139/625000000>\delta_{c,\rm lower}>1/700.
\]
Thus the stated source inputs prove the complete comparison with saving
at least (10), before any additional fixed power costs.

On the larger independent box \(r\ge7/10,m>2/5\), the infimum of
\(d(r+2m-3/2)\) is zero. The positive comparison must therefore be
stated on the certified operational region, rather than promoted to
the whole coarse box.

If separately fixed power losses \(\beta_F,\beta_R\) occur in (1)
and (6), the cross saving decreases by \((\beta_F+\beta_R)/2\),
and the correction-square saving decreases by \(\beta_R\). Polynomial
height factors may be retained as \(H^b\); any already chosen conversion
to a positive power of \(U\) must be charged. Preserve the source's
cumulative frequency allowance and the order of choosing finite internal
derivative orders, height schedule, and later external tail orders.
The source/witness certificate has its own smaller application budgets;
the reserve in (10) does not replace them.

## 4 The concrete next theorem and its first gates

After the complete comparison, the original sufficient target is equivalent
at exponent 1/700 to
\[
 \boxed{\sum_{u\in\mathcal C_+}
 |M_uQ_J(u)[S_u(N)^2-S_u(Y_1)S_u(Y_2)]|^2
 \ll_\varepsilon U^{1+dr-1/700+\varepsilon}H^b.} \tag{11}
\]
This theorem is still open. Notes 24–25 already give a controlled comparison
between the original uncentered target and \(F_\dagger\), so proving
(11) also bounds that residual. No comparison with a residual-centered
polynomial is required for this implication.

The equal-product identity cancels the leading principal plain response:
if \(S_u(Y)=\kappa_u\sqrt Y+E_u(Y)\) with a common row constant,
then \(\kappa_u^2N-\kappa_u^2\sqrt{Y_1Y_2}=0\).
The first auxiliary-row task is to prove the required error bound uniformly
over all admitted principal/fixed-ray rows and their deletion masks, with
the actual derivative and height allowances. Cancellation of this main
term is not a bound for all auxiliary growing-conductor rows.

Then either retain the selected family in a signed estimate, or prove an
appropriate positive comparison to a centered smooth family after accounting
for every added conductor sector. The [Note 21](21_SIGNED_JOINT_TRANSFORM_20261009.md)
joint coprimality kernel remains useful. [Note 18](18_NATIVE_ANNULAR_DIAGONAL_TEST_20261009.md),
section 4, already shows that the separately positive coefficient-diagonal
approach fails even after this standard centering. The new estimate must
control the signed aggregate rather than repeat that failed bound.

The [separate checker](../../numerics/check_note25_review.py) and
[record](../../numerics/note25_review_record_20261009.json) verify the exact
arithmetic in (3), (9)–(10), with the operational enclosures explicitly
imported. They do not prove the source inputs, the auxiliary-row estimates,
or (11). This is a feasibility result and a precise next proof obligation,
not a new mixed fourth theorem or a zero-free boundary result.
