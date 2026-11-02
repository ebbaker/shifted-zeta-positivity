# J-E02 r1: audited tail and global sign certificate

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**.

**Complete successful return.** The effective tail proof passes its audit.
Outward-rounded Bernstein certificates cover the origin and all 126
middle cells. At physical heat time zero the complete canonical source
therefore satisfies
\[
\boxed{R'(u)>0,\qquad K(u)>0\quad(0<u<\infty).} \tag{1}
\]
The audited signed-averaging transfer consequently applies at order three.
This is an in-note proof with an Arb-certified compact part, awaiting
**[E] J-E03 — Sol** assessment. Checks to date are contributing internal
same-model LLM checks, not independent specialist review. There is no
new coefficient range, determinant-order induction or RH conclusion.

## 1. Contract, versions and execution

This executes [Note09 Section 7, J-E02 r1][request]. Note09's actual
SHA-256 is
`0fb3a7dd974cd858dd0941e6b89863aaaea9f8a62ee172d37de27bd7970cb5a9`.
HEAD is `c97b376dcbf81f05ea3a4f7d360da168af4a1345`; the inputs include
working-tree research. Preserved input hashes match Note09, including
Return07, Continuation08, Note05 and both r2 numerical artifacts. None
of the prior requests, notes, programs or records was edited.

| Artifact | Purpose |
| --- | --- |
| [Interval program][program] | Full-source coefficient balls, joint series, whole-interval Bernstein bounds, errors and cover |
| [Interval record][record] | All 127 accepted leaves, exact dyadic enclosures, source/origin coefficients, input/code hashes and timing |
| [Exact algebra audit][algebra] | Joint identities, degrees, r2 equivalence, Gaussian and generic even-source cancellations |
| [Algebra record][algebra-record] | Exact 29-term numerator and the checked identities |
| [Replay/validation record][validation] | Installed replay, preserved-input and cover checks |

The arithmetic is **python-flint 0.9.0, FLINT 3.6.0 (Arb)**, at **128 bits**.
The dependency was available through an isolated temporary installation;
no uncertified floating fallback was used. The compact certificate's first
arithmetic run took **4.293901875 seconds**; the exact algebra audit took
**2.275538375 seconds**. Separate installed-replay times and total measured
arithmetic are recorded in the validation record. All are within the
30-minute allowance. Dependency setup, code preparation, analytical audit
and write-up are outside that arithmetic timing.

Exactly 24 terms, Taylor degree 63 and P0–P70 were used. The middle
formula accesses only P0–P7. No new Q polynomial was generated; the
algebra check reused the preserved Q10 record. There was no refinement
to 256 bits, subdivision, unresolved cell, counterpoint, coefficient-minor
calculation or quadrature. No caps were enlarged and no mathematical
correction to Note09 was needed.

The overview's pre-return hash is
`71290b1a431d7d96edbf418243f9333bb6bc93957d60805acf973241799ea5e9`;
the Active register's hash is
`dd836ef07a7c2ad90bc8d6b29dba405d6562318bf5d88aba17c42d44fa2ee058`.
The [sole live register][progress] owns status. Read with the
[result index][results], especially [theta identities][theta] and
[controls][controls], and the [avoid index][avoid], especially
[joint bounds][joint], [numerical scope][numerical-scope],
[status strength][status] and [scoped conclusions][scopes].

## 2. Joint algebra and analytical audit

For Note09's \(\mathcal A,\mathcal B,\mathcal W,\mathcal W_1,\mathcal N\),
exact differentiation gives
\(\mathcal A'=\mathcal B\), \(\mathcal W'=\mathcal W_1\).
With actual source jets \(\phi_j=\Phi^{(j)}\), quotient algebra gives
\[
R'=\mathcal A(\phi)/\Phi^2,\quad
C=\mathcal W(\phi)/\Phi^3,\quad
K=\mathcal N(\phi)/\Phi^6,
\]
\[
\mathcal N=q_0\mathcal A\mathcal W_1
-3(q_0\mathcal B-q_1\mathcal A)\mathcal W. \tag{2}
\]
The exact audit verifies equivalence to the preserved r2 state numerator,
including the \(4^{13}\) factor. Expanded \(\mathcal N\) has 29 terms,
ordinary degree six, weighted degree thirteen and coefficient absolute
sum **76**, so Note09's bound 84 is safe. \(\mathcal A\) has degree two
and weight three. Gaussian substitution gives \(\mathcal N=0\).
Substitution of a generic even source verifies that \(\mathcal A\) has
only odd powers starting at \(u\), and \(\mathcal N\) only odd powers
starting at \(u^5\). These are exact identities, not numerical thresholds.

The following bounds in Note09 (6)–(22) were checked without change:

- The summand recurrence gives \(M_j\le5\,64^j\) through order seven.
  The seven stated rational terms for \(\mathcal S\) sum to 4,493,321;
  the remaining geometric bound is below \(2^{-8}\), giving
  \(\mathcal S<2^{23}\) and \(B_j<2^{28}\).
- The normalized quotient error pays both numerator and denominator
  contributions, \(5+25=30\). The normalized box of radius six and
  \(8\cdot640\cdot6^7=1433272320<2^{31}\) give the stated full-source
  tail errors, with no differentiation of an unspecified remainder.
- On the complex source disks, the bounds \(1216<2^{11}\),
  \(|\mathcal A|<2^{35}\), \(|\mathcal N|<2^{145}\) are safe.
  For the last two, \(12\,2^{31}<2^{35}\) and
  \(84\cdot13!\,2^{105}<2^{145}\) suffice.
- Origin Cauchy deflation gives errors below \(2^{-150}\) and
  \(2^{-16}\). The omitted 24-term source is below \(2^{-146}\) on
  the acquisition circle, giving coefficient errors \(2^{-146+2j}\).
- On normalized disks, \(|t|>3/2\), \(\Re t>1\) give the bounds
  \(2^{53},2^{163}\). The omitted normalized jets are below
  \(2^{-530}\); the joint errors are therefore \(2^{-502},2^{-391}\).
  Cauchy with initial \(h/\rho=1/32\) gives the two stated middle
  remainders below \(2^{-266},2^{-156}\).

These are audits of the supplied elementary estimates. No new external
theorem or literature claim is imported. The [Arb documentation][arb-doc]
specifies the midpoint/radius enclosures and bit precision used here.

## 3. Effective infinite tail

The proof preserves the complete differentiated arithmetic remainder and
the first-summand cancellation. For \(t\ge128\), Note09's exact
polynomial comparison gives
\(R_1'>64t^2\), \(K_1>3\cdot2^{29}t^7\).
The full-source error satisfies
\[
|R'-R_1'|<2^{55}t^3e^{-3t},\qquad
|K-K_1|<2^{142}t^{13}e^{-3t}.
\]
The decreasing quantities \(te^{-3t}\), \(t^6e^{-3t}\), evaluated at
128 using \(e>2\), bound the relative errors by \(2^{-322}\) and
\(2^{-200}\). Hence the audited conclusion is
\[
\boxed{t\ge128\ \Longrightarrow\ R'>63t^2,\quad K>2^{30}t^7.} \tag{3}
\]
The join is rigorous: \(\sum_{j=0}^6 4^j/j!=437/9>43\), and
\(\pi>3\), so \(\pi e^4>129>128\). Thus (3) covers every
\(u\ge1\), including the common endpoint.

## 4. Compact certificate and margins after errors

Every decision below uses ball lower bounds; decimal displays are only
readable summaries. Exact integer mantissa/exponent endpoints are in the
record. The full source is retained through coefficient or remainder
enclosures even though exactly 24 summands are evaluated.

| Piece | Full covered domain | Precision/leaves | Conservative lower bounds after all errors |
| --- | --- | --- | --- |
| Origin | \(x=u^2\in[0,1/4096]\), hence \(0\le u\le1/64\) | 128 bits; 1 leaf, depth 0 | \(\mathcal A(\phi)/u>1762\), \(\mathcal N(\phi)/u^5>2^{54}\) |
| Middle | All 126 cells \([m/128,(m+1)/128]\), \(m=2,\ldots,127\) | 128 bits; 126 leaves, depth 0 | \(\mathcal A(\nu)>2^{-17}\), \(\mathcal N(\nu)>2^{-86}\) |
| Tail | \(u\ge1\) | Analytical proof | (3) |

**Origin.** Acquire \(a_0,\ldots,a_{70}\) with the stated coefficient
errors and rounding. Set odd coefficients to their exact full-source
values zero. Form derivative series by
\([u^k]\phi_j=(k+j)!a_{k+j}/k!\), then the complete joint numerators.
Only the symbolically proved parity and coefficients below the deflation
orders are removed. A finite theta sum is never declared even.
The resulting degree-31/29 polynomials in \(x\) are bounded by Bernstein
coefficients on the whole interval. Subtracting \(2^{-150}\) and
\(2^{-16}\) gives recorded lower bounds approximately
1762.07830259031124 and \(2.98891625087108505\cdot10^{16}\).
These imply the conservative rational bounds in the table.

The endpoint values also overlap an independent evaluation of the
inherited formulas
\(2\Phi(0)^2\widehat R'(0)\) and \(32\Phi(0)^6J(0)\), using the
same 24 retained exponentials and a rigorous omitted-tail enclosure.
This is a normalization check; the whole-interval lower bounds establish
the compact signs.

**Middle.** Taylor coefficients come directly from Note09 (17), using
\(t(c+s)=t(c)e^{4s}\), inverse powers of this \(t\), and the normalized
summand exponentials. They are not obtained by inverting the tiny source
amplitude or by treating \(\nu_j\) as derivatives of \(\nu_0\).
Form (2) in series, convert both degree-63 polynomials to Bernstein form
on \([-h,h]\), and subtract the full joint tail and Cauchy errors.
No center sample accepts a sign.

Both minimum middle lower bounds occur on \([127/128,1]\): they are
approximately \(1.10091456560077379\cdot10^{-5}\) and
\(2.46055290487880818\cdot10^{-26}\). These are lower bounds for
the normalized numerators, not for \(R'\) or \(K\) in physical units.
Homogeneity and \(\nu_0>1\), with the positive real scaling factors in
Note09 (18), give the original signs. The original source \(\Phi>0\)
supplies the denominator signs in the origin and unnormalized formulas.

The recorded leaves have exactly adjacent rational endpoints. The origin
ends at \(1/64\), the middle starts there and ends at 1, and the tail
covers 1 onward. There are **no gaps, failed cells or unresolved cells**.
At \(u=0\), the quotients mean analytic continuations; (1) asserts strict
positivity only for \(u>0\), as required.

## 5. Consumer, controls and continuation

The accepted [r2 transfer][r2] now has its original global premises.
For every finite integer \(k,\ell\ge0\), at order three,
\[
\boxed{A_{k+\ell}\ge A_k\ge A_0=48c_0^3/Z_0>0,}\qquad
D_{3,k}\ge\frac{48c_0^3Z_k}{(2k)!(2k+2)!(2k+4)!Z_0}>0. \tag{4}
\]
No numerical value of \(Z_k\) or coefficient-minor scan was needed.
The structural comparison is (4); order-three coefficient positivity
itself was already in the recorded baseline. No novelty claim is made.
The old negative origin \(C\) is preserved, and the signed integral
continues to permit its negative source region.

Note09's control screen applies unchanged. Translated Euler-factor and
altered weighted-square/finite-prime sources fail the exact canonical
series and its quantitative tail payments; finite endpoint matching does
not replace full evenness. Reflected super-Gaussians retain evenness but
lack this series and first-summand bound. Smooth shape or primitive
positivity supplies neither the canonical coefficients nor these bounds.
The Gaussian gives \(\mathcal N=0\) in the generic identity and is not
required to satisfy this strict canonical certificate. No uncomputed
control sign or universal collision-exclusion consequence is asserted.

**J-E02 r1 is complete. Next: [E] J-E03 — Sol.** Assess the fixed global
sign/transfer claim (1)–(4), its analytical constants, interval arithmetic,
joins, control scope and claimed payoff. The [continuation note][continuation]
provides the concrete checklist and model guidance. J-E03 is ready and
has not been executed by this return; a structural gap found there returns
to J-B02. No wider research task or numerical campaign is started.

[request]: 09_J_B02_GLOBAL_TAIL_AND_COMPACT_CERTIFICATE_20261101.md#7-frozen-execution-request-j-e02-r1
[program]: ../numerics/j_e02_certificate.py
[record]: ../numerics/J_E02_R1_INTERVAL_RECORD_20261101.json
[algebra]: ../numerics/j_e02_algebra_audit.py
[algebra-record]: ../numerics/J_E02_R1_ALGEBRA_RECORD_20261101.json
[validation]: ../numerics/J_E02_R1_REPLAY_VALIDATION_20261101.json
[r2]: 07_J_E01_R2_SIGNED_AVERAGING_AND_Q10_P7_RETURN_20261101.md
[continuation]: 12_CONTINUATION_FOR_SOL_J_E03_GLOBAL_SIGN_ASSESSMENT_20261101.md
[progress]: ../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[numerical-scope]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[status]: ../../../../../avoid/06_status_stronger_than_the_evidence.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[arb-doc]: https://python-flint.readthedocs.io/en/latest/arb.html
