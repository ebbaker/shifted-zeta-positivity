# J-E03: global sign certificate and signed-averaging assessment

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**.

**Disposition: accepted within this internal assessment; J-E03 complete.**
No material mathematical or implementation defect was found in
[Return11][return] and its fixed certificate. No correction is required.
The accepted claims, for the complete canonical source at physical heat
time zero, are
\[
R'(u)>0,\quad K(u)>0\quad(u>0),\qquad
A_{k+\ell}\ge A_k\ge48c_0^3/Z_0>0
\quad(k,\ell\in\mathbb Z_{\ge0}). \tag{1}
\]
The comparison is at determinant order **three**. Its positivity was
already in the recorded baseline; the accepted structural consequence
is normalized index monotonicity. No new coefficient range, increasing-order
argument, all-minor theorem, novelty claim or RH conclusion is accepted.

**Review relationship:** the coordinating assistant also authored the E02
implementation. This is same-assistant, same-model internal assessment,
with three fresh read-only contributing same-model checks of the code,
analytical estimates and transfer. Those checks share source inputs and
do not constitute independent specialist review. The root performed the
sole compact numerical replay in this assessment.

## 1. Scope and versions

The scope is [Continuation12][packet]'s five-part checklist. All previous
notes, requests, code and records remain unchanged. HEAD is
`c97b376dcbf81f05ea3a4f7d360da168af4a1345`; the research inputs include
working-tree files. Key assessed versions are:

| Input | SHA-256 |
| --- | --- |
| Note09, analytical proof and E02 request | `0fb3a7dd974cd858dd0941e6b89863aaaea9f8a62ee172d37de27bd7970cb5a9` |
| Return11 | `6cad8ab91ca36ad3eb1ab5c8d36e636a7dfeb9432e64e3a95395093775b09819` |
| Continuation12 | `aec3535875848b80b9741d6a82925780897060dc0acc4f33053f093e3f0cb34f` |
| Interval program | `f89ba42e36f5fc83f063574166ae81e431f7647d28e4e11cc5cb5ba1b93d10d7` |
| Interval record | `cc5266c631e6cdbd9ef7d966a82969e5703da133e6adc5f2c1ab2badcee76b6b` |
| Exact algebra program | `7299cf57d715e65316c3c07c362798a92f696560cf83621d47dd6b57fea1a34e` |
| Exact algebra record | `3fa68adb4c45c102c701e8eac24e97c36cf411542257d34132d82edaf384af7d` |

The [assessment record][record] gives the full input/checker hashes,
library versions, replay timing and exact record checks. The pre-return
Active register hash is
`c47aa7d47f41960af27b87fb065458061a587a72bea6fe2538cba258dc01682d`;
the overview hash is
`2824c915c1538e0d0977eed1b92cef831d16500466d959c3e6df81c935edc31a`.

Read with the [result index][results], especially [theta identities][theta]
and [controls][controls], and the [avoid index][avoid], especially
[shared-premise reviews][shared], [normalization][normalization],
[joint expressions][joint], [status][status] and [scope][scopes].

## 2. Algebra, tail and analytic errors

The joint formulas in Note09 (2)–(3) are correct. Differentiating the
first two columns of the Wronskian creates repeated columns, giving
\(\mathcal W'=\mathcal W_1\); also \(\mathcal A'=\mathcal B\).
Quotient differentiation gives exactly
\[
K=\frac{q_0\mathcal A\mathcal W_1
-3(q_0\mathcal B-q_1\mathcal A)\mathcal W}{\Phi^6}.
\]
The expanded numerator has 29 terms, coefficient absolute sum 76,
ordinary degree six and weighted degree thirteen, so the bound 84 is
conservative. The preserved exact program checks the r2 numerator and
\(4^{13}\) scaling, the Gaussian zero and generic even-source low zeros.
The actual recorded polynomial data also have these degrees and sums.

A fresh [integer-polynomial first-mode check][firstmode] regenerates
only P0–P7 and verifies the R1, T1 and R1' rational formulas. It closes
the tail dependence by exact cross-multiplication:
\[
\mathcal N(P)(2t-3)=3\cdot2^{26}t^{11}p(t),
\]
giving the stated \(K_1=3\cdot2^{26}t^5p(t)/(2t-3)^7\) and leading
coefficient \(3\cdot2^{30}\). Its [record][firstmode-record] retains the
checks and script hash. No numerical point or additional derivative was
introduced.

All analytical estimates in Note09 (6)–(22) are accepted:

| Estimate | Assessment |
| --- | --- |
| Differentiated theta remainder | Recurrence bound, \(\mathcal S<2^{23}\), \(B_j<2^{28}\) and denominator payment \(5+25=30\) are valid |
| Effective tail | Weighted scaling and \(8\cdot640\cdot6^7<2^{31}\) give the stated errors; first-mode bounds dominate them at \(t\ge128\) |
| Complex source disks and Cauchy bounds | Disks stay in the convergence region; \(2^{35},2^{145}\) safely bound the joint numerators |
| Origin coefficient tail and deflation | Coefficient error \(2^{-146+2j}\), U/V errors \(2^{-150},2^{-16}\) and acquisition through 70 are valid |
| Normalized complex disks and theta tail | Supremum bounds \(2^{53},2^{163}\), jet tail \(2^{-530}\) and joint errors \(2^{-502},2^{-391}\) are valid |
| Middle Taylor errors | Degree 63 with \(h/\rho=1/32\) gives the stated bounds below \(2^{-266},2^{-156}\) |

In particular, the first-mode comparison and complete remainder prove
\(R'>63t^2,K>2^{30}t^7\) for \(t\ge128\). The exact Taylor sum
\(437/9>43\), together with \(\pi>3\), proves that this covers
\(u\ge1\). This is an effective tail, not an extrapolation from samples.

## 3. Compact implementation and exact replay

The origin code acquires all 71 coefficient balls from 24 summands and
adds the prescribed full-source errors before using parity. It then
uses \((k+j)!a_{k+j}/k!\) for derivative coefficients. The source order
70 is exactly sufficient for degree 63 with the seventh derivative.

**Full-source evenness, not the 24-term approximation, licenses the origin
cancellations.** Containment of zero in a computed ball would not suffice
to remove a coefficient. Here exact parity and the separately proved
\(u,u^5\) factors justify the removal; numerical containment is only a
consistency check. The extracted polynomials have degrees 31 and 29 in
\(x=u^2\), and their analytic remainders are subtracted.

The middle code implements Note09 (17) directly, with
\(t(c+s)=t(c)e^{4s}\). Its inverse powers and normalized mode amplitudes
are correct. It does not invert the tiny source amplitude or pretend
that the normalized jets are ordinary derivatives of \(\nu_0\).

The power-to-Bernstein transformation is correct and performed with Arb
balls. Taking the least lower coefficient bounds the entire polynomial;
the code then subtracts the full Cauchy and joint theta-tail errors. No
point sample accepts a cell. Arb's midpoint/radius and series-precision
conventions agree with the [primary documentation][arb-doc] and
[series documentation][series-doc].

One unchanged fixed-certificate replay completed in **4.305158625 seconds**,
using python-flint **0.9.0**, FLINT **3.6.0**, at **128 bits**. All non-timing
fields match the preserved E02 record. No new cells, terms, degree,
precision or domain were used. The [exact assessment checker][checker]
also verifies input/code hashes and **1,149** serialized ball enclosures
using rational mantissa/exponent arithmetic, rather than trusting saved
status strings or decimal displays.

| Piece | Exact cover and accepted lower bounds after errors |
| --- | --- |
| Origin | One leaf \(x\in[0,1/4096]\); \(\mathcal A(\phi)/u>1762\), \(\mathcal N(\phi)/u^5>2^{54}\) |
| Middle | 126 adjacent leaves \([m/128,(m+1)/128]\), \(m=2,\ldots,127\); \(\mathcal A(\nu)>2^{-17}\), \(\mathcal N(\nu)>2^{-86}\) |
| Tail | Every \(u\ge1\), by the audited analytical proof |

There are no failed or unresolved leaves. The origin's right endpoint
corresponds to \(u=1/64\), exactly the first middle endpoint. The last
middle endpoint is 1, shared with the tail. Denominators and real scaling
factors are positive. At zero the deflated functions mean their analytic
continuations; strict R' and K positivity is asserted only for \(u>0\).
Thus there is no missing join or compact-region obligation in (1).

## 4. Signed transfer, controls and conclusion

The real determinant identity retains all lower endpoints, including
the odd derivative endpoint when a moment index would otherwise be
negative. The ordered chamber cancels the composition factor \(1/3!\),
leaving \(F_k=(2k)!(2k+2)!(2k+4)!\). At \(k=0\), the triangular
coefficient matrix gives \(M_0=48c_0^3>0\).

The divided-difference determinant has the correct orientation, and
[de Boor (52)][deboor] gives the simplex constant \(1/2\).
The certified \(R'>0,K>0\) imply that its signed observable h is
coordinatewise increasing. The strict ordered grids are distributive
sublattices; the crossed-endpoint identity proves the pairwise lattice
inequality for both Vandermondes. [FKG Proposition 1][fkg] permits
increasing real observables, including a negative h.

On compact truncated chambers the integrands are bounded and continuous
up to coincident nodes. Exhaustion uses the four absolutely convergent
unnormalized integrals \(Z_k,Z_{k+\ell},M_k,M_{k+\ell}\), so an unbounded
tilt and signed h do not invalidate the limit. The covariance identity
therefore gives (1), with no quadrature of \(Z_k\).

Primary import inspection remains limited to FKG Proposition 1 and its
support discussion, and de Boor's displayed simplex formula; the full
papers are not being certified. No Karlin–Rinott theorem is imported.

The controls have the scope stated in Note09. Translated/altered
arithmetic sources fail the literal canonical series and its quantitative
payments; finite endpoint matching cannot replace complete evenness.
Reflected and shape/positive-primitive controls do not supply the canonical
expansion and bounds. The Gaussian gives the generic equality case.
No uncomputed R'/K sign is attributed to any control, and a positive-time
collision does not contradict this finite-order theorem. The original
negative origin C is preserved.

**Accepted:** the global canonical source pair and normalized order-three
index comparison in (1), with the stated internal-review status.
**Corrections:** none. **Unresolved obligations for this fixed claim:**
none identified. J-E03 and the current J-B01–J-E03 sequence are complete.
The broader all-order/RH objective is outside this completed packet.
The [continuation note][continuation] records the stopping boundary and
model guidance; no further execution is issued.

[return]: ../notes/11_J_E02_R1_GLOBAL_SIGN_CERTIFICATE_RETURN_20261101.md
[packet]: ../notes/12_CONTINUATION_FOR_SOL_J_E03_GLOBAL_SIGN_ASSESSMENT_20261101.md
[record]: ../numerics/J_E03_ASSESSMENT_RECORD_20261101.json
[checker]: ../numerics/j_e03_assessment_check.py
[firstmode]: ../numerics/j_e03_firstmode_check.py
[firstmode-record]: ../numerics/J_E03_FIRSTMODE_RECORD_20261101.json
[continuation]: ../notes/13_CONTINUATION_AFTER_J_E03_ACCEPTED_ASSESSMENT_20261101.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[shared]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[normalization]: ../../../../../avoid/08_normalization_and_constant_slips.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[status]: ../../../../../avoid/06_status_stronger_than_the_evidence.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[arb-doc]: https://python-flint.readthedocs.io/en/latest/arb.html
[series-doc]: https://python-flint.readthedocs.io/en/latest/arb_series.html
[fkg]: https://math.bme.hu/~balint/oktatas/perkolacio/percolation_papers/fortuin_kasteleyn_ginibre.pdf
[deboor]: https://ftp.cs.wisc.edu/Approx/dvdsurvey.pdf
