# Contour and normalization audit for the enlarged prime slot geometry

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning
effort are not exposed and are not inferred.

## Scope and conclusion

This review checks the transfer of the contour, Euler correction, principal
normalization, and order-of-choices arguments to

\[
\ell=\frac{1001}{6000},\quad b=\frac18,\quad
l_x=\frac{4249}{12000},\quad l_y=\frac{5749}{12000},\quad
h=\frac{3251}{4000}.
\]

The candidate boundary is \(\sigma_0=20999/24000=7/8-1/24000\).
The signal exponent remains exactly \(C(s)=s-11/16\). The contour
arguments introduce no further obstruction at these scales, provided
the source's structural analytic inputs hold. The principal correction
and excluded set must be shared by the physical sum and the signal.

The source is the [September 30 quasi-RH manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
SHA-256 `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The source passages inspected here are Proposition 2.1, Lemma 7.1,
Definition 10.1, Lemmas 10.3--10.6 and 11.1, the exact formulas and
principal/outer estimates in Section 16, and Sections 20.1--20.6.
This review does not establish the source's global reciprocal bounds,
reflection and moment machinery, or its seven-eighths theorem. No Lean
proof is replayed. The low and moment transfers have separate scoped
reviews.

## Exact high identity and moving slot primes

Definition 10.1 requires positive \(l_x,l_y\), nonnegative \(\ell\), and
\(h=1-l_x+\ell>0\); the chosen values satisfy these identities. The
finite compensated expression (12.5) still defines the physical probe.
The local multipliers leading to (16.2)--(16.7) are exact under changes
of these scale exponents. In particular the rescaled operation still
has multiplier \(Q^{z-w-1}\), and the completed-index operation still
has multiplier \(\eta(p)Q^{s+z-1}\). Neither formula assumes the
original numerical value \(\ell=1/6\).

All selected prime windows remain disjoint and are fixed as windows
before the scale tends to infinity. Their prime elements vary with the
scale. A fixed sufficiently fine even slot count is chosen with total
length equal to the new \(\ell\). Equation (16.3), with its full sum of
holomorphic products, is the correction for contour moves. It is never
replaced globally by quotients of individual factors at their zeros.

## Euler domain below seven eighths

The source's principal Euler region starts at \(\Re s=7/8\), so it
cannot be cited verbatim under a contradiction above the new boundary.
The explicit domain enlargement in the first extension remains sufficient:

\[
\Re s\ge87/100,\qquad \Re w\ge19/20,\qquad
\Re z\ge33/200.
\]

The new boundary exceeds \(87/100\). From (7.11) and (7.17), the
denominator parameters satisfy
\(|R|\le Q^{-221/100}\), \(|V|\le Q^{-99/100}\), and
\(|D|\le Q^{-87/100}\). They stay uniformly away from one. The
largest good-prime and ramified defects have exponents \(-181/100\)
and \(-41/50\), respectively. Thus normal convergence and the
\(q_u^\epsilon\) bound follow by the same ideal-count and divisor-product
arguments as on source page 55. The principal good-prime tail has decay
\(P_0^{-81/100}\), retaining the convenient \(P_0^{-4/5}\) bound.
This yields a target-independent cutoff ensuring the common correction
is within one half of one on \(\Re s>\sigma_0\).

For the principal multiplier, the four errors in (16.8) are bounded by
\(Q^{-87/100},Q^{-99/100},Q^{-134/100},Q^{-94/100}\).
Consequently \(B_p=-1+O(Q^{-87/100})\). The positive unselected
product majorant and the full tuple formula give the required absolute
principal bound \(Z^{\ell\Re z+\epsilon}\), uniformly in heights.
All-height bounds on fixed boxes likewise follow with finite scale
degree and height degree zero from the exact local formulas.

## Central and outer contours

The buffered central contour in Lemma 10.3 and Proposition 16.1 lies
in the first Euler region with parameter \(10e\). Its endpoints have
\(a\ge51/100\); neither the new geometry nor the new principal boundary
changes that fact. The source proof moves the full finite bin before
forming any pointwise amplitude subsets. This ordering is retained.

For small rows use the first Euler region with parameter \(1/3\),
because \(87/100+1/2>1+1/3\). On the terminal lines
\((\Re s,\Re w,\Re z)=(\beta_*+e,1/2,17/50)\), selected coprime
factors are bounded, and a selected ramified factor is \(O(Q^{1/2})\).
The strict ramified term is the largest one; all boundary terms remain
smaller. The full positive tuple bound (16.15) follows without division
by local factors. With \(d_{\min}=1/100\), the conservative small-row
saving relative to \(C(\beta_*)\) is

\[
\frac{l_y}{2}-h\left(\frac{17}{50}-\frac16\right)-2d_{\min}
=\frac{63}{800}-\frac{51}{100}\left(\ell-\frac16\right)>0.
\]

Large rows retain the absolute lines \((2,2,z_\infty)\). For any fixed
positive extension \(\zeta\), their exponent is bounded by
\(B_0+(h+\zeta)(1+\epsilon)-\zeta z_\infty+\epsilon\).
A sufficiently large fixed \(z_\infty\), chosen after \(\zeta\) and
before the target, provides any required saving. No short character
family estimate is used on this range.

## Principal residues and order of choices

The residue locations remain \(w=1,z=1/6\). The factor \(1/6\),
the Gaussian, and the formula for \(c_S\) remain as in (10.1).
The positive prime-slot asymptotic in Lemma 13.1 applies to any fixed
positive slot lengths and fixed ray group. The new normalizer therefore
has inverse of subpower size. Its error has a positive fixed saving
less than \((87/100)\min_i\ell_i\). The two contour savings are

\[
m_w=l_y/20=5749/240000,\qquad
m_z=h/600=3251/2400000.
\]

The same final excluded set must occur in the physical sum, \(H_\eta\),
\(c_S\), the slot normalizer, and the Mellin signal. Later exclusion
of a target-dependent finite set preserves the positive product-tail
majorant and only changes allowed constants and thresholds.

The geometry, fine slot mesh, detector widths, and positive exponent
reserves are fixed before the target. The contradiction gap
\(\beta_*-\sigma_0\) is common to all targets and may inform these
choices. Only then are target-specific arithmetic data and finite
internal height orders fixed. Lemma 11.1 chooses the target's height
exponent before the final external decay orders and thresholds.
The external orders do not increase the internal moment orders.

The source's Proposition 2.1 is already stated for arbitrary
\(\sigma_0\in(1/2,1)\). With the separately checked low and high
estimates, these transfers give its required common signal and
target-independent positive savings, conditional on the listed
structural inputs. This is a transfer audit, not a complete verification
of the external theorem.
