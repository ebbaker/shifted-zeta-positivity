# Review of the conditional parameter extension

Date: 8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed and are not inferred.
Scope: independently worked same-model review of the proposed parameter extension. This is not independent specialist refereeing, a complete audit of the external manuscript, or an unconditional zero-free theorem. No Lean development was replayed.

Reviewed derivation: [Parameter extension](../notes/PARAMETER_EXTENSION_20261008.md). Exact arithmetic record: [parameter_extension_check.json](../numerics/parameter_extension_check.json).

## Verdict and assumptions

The checked parameter argument closes conditionally at

\[
b_0=\frac78-\frac1{600000}=\frac{524999}{600000}.
\]

The assumptions are the external manuscript's family-wide bound \(\beta_*\le7/8\) and its structural reflection, detector, moment, and exact representation results. The latter have not been re-established in this review. Within that scope, the changed scales, the row-count application, and the contour-domain repair retain strictly positive margins. I found no remaining specific obstruction introduced by this perturbation.

The source fixes several statements at the original geometry. Accordingly, this conclusion requires the explicit extensions below; it is not a direct invocation of the originally stated propositions. It also does not establish that the 199-page external argument is correct. The main note should retain that conditional status when converting the candidate boundary into a local variance exponent.

## Geometry and the low estimate

Write \(r=1/100000\), retain \(\ell=1/6\), \(b=1/8\), and take

\[
h=13/16+r,\quad l_x=17/48-r,\quad l_y=23/48-r.
\]

The identity \(h=1-l_x+\ell\) survives. The finite compensated expression (source equation 12.5) and its Euler correction remain meaningful at these positive scales. The equality \(M+\ell=1\), however, becomes \(M+\ell=1-2r\); its use in the low estimate cannot be copied unchanged.

For a rescaled subset of total length \(d\), repeating the source's equations 15.1–15.3 gives \(M'+\ell'-1=-2r-3d\). This strengthens the intermediate dual-length bound but changes the relative squared-row penalty to

\[
\frac{(d-1/6+4r)_+}{4}.
\]

After Cauchy–Schwarz, counting the rescaled tuples, and retaining their coefficients, the additional exponent is

\[
f(d)=-d+\frac{(d-1/6+4r)_+}{8}\le0\qquad(0\le d\le1/6).
\]

The inequality holds whenever \(r\le1/24\). Both branches are decreasing after their respective endpoints; the potential positive branch begins only at \(d\ge1/6-4r\). The additive Gram requirements remain strict, including the formerly \(1/12\) length margin, now \(1/12-r\). Thus the low exponent is \(3/16-r/2\), while the principal signal has \(C_r(s)=s-11/16-r/3\). These coincide at \(s=b_0\).

## Moments, row counts, and high estimates

Fixing \(\kappa=3/4\) is legitimate: it lies in Lemma 18.1's stated parameter interval, and the assumed \(\beta_*\le7/8\) supplies its zero-free prerequisite. No extension to \(\kappa<3/4\) is used. Proposition 19.2 must be repeated with the exact baseline plain capacity. Its former \(\Delta/4\) penalty then disappears. The supplied prime length remains strictly above \(7/37\), including a sufficiently small extension of the row range above \(h\).

The resulting ideal exponent satisfies \(R_*\le1-2\delta/3\), since \(P_x/D_x\le2/3\) and the balancing parameter is at least one. On the relevant range \(\delta\le3/4\), changing the endpoint geometry therefore costs at most

\[
r(R_*+\delta+1/2)\le7r/4.
\]

The source's endpoint certificate leaves

\[
\frac{49}{440640}-\frac{7r}{4}
=\frac{51611}{550800000}>0.
\]

The floor and small-row ranges retain margins \(7/1200-38r/25\) and \(63/800-101r/150\). The conservative middle-range margin \(49/14400-243r/200\) is also positive. The frequency slopes keep their required sign. A sufficiently small fixed extension parameter fits both the prime-supply margin and this endpoint budget; a fixed sufficiently large terminal contour handles larger rows.

## Originally missing domain and its repair

The first review identified a genuine application gap: the source's second Euler region requires \(\Re s\ge7/8\), and Lemmas 10.3–10.6 are stated for boundaries at least \(7/8\). Under the new contradiction, \(b_0<\beta_*\le7/8\), the principal global line can leave that region. A positive exponent certificate alone does not repair this.

The displayed local formulas permit an explicit extension to \(\Re s\ge87/100\), keeping the other second-region bounds. Their worst good-prime and ramified defects become respectively \(Q^{-181/100}\) and \(Q^{-41/50}\). The Euler-tail exponent \(4/5\) remains available; the denominators stay uniformly away from zero. The principal multiplier becomes \(-1+O(Q^{-87/100})\), preserving positive normalizer-error decay. Small-row paths use the first Euler region with parameter \(1/3\); the ramified bound \(G_p\ll Q^{1/2}\) survives. The principal contour margins become \((23/48-r)/20\) and \((13/16+r)/600\), both positive. These checks justify repeating the corresponding contour proofs with the enlarged domain.

## Quantifiers and remaining validation

The geometric displacement, real losses, slot mesh, and positive exponent margins must be chosen independently of the target character. Constants, sufficiently large thresholds, and the eventual height choice may depend on that target. The order of choices must retain the source's separation between internal height/profile orders and later external tail orders. The perturbation stays in fixed bounded parameter intervals and introduces no new moving family or derivative-order dependence.

Under those conditions Proposition 2.1 gives the conditional contradiction. What remains outside this review is a full verification of the imported structural machinery, specialist assessment, and any formal proof replay. The resulting local variance exponent would be \(2b_0-1=224999/300000\), conditionally on that machinery.
