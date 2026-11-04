# RGD-E02 r1 — certified two-case lower allowances

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual **gpt-6.1-sol (Codex), effort ultra**,
research chat0003, thread `01a1a77f-2607-7832-9902-29399c58b442`, turn
`01a1a789-4831-75e3-ac1d-91bbab495d0d`.

**Disposition: RGD-E02 r1 completed; both finite lower allowances certified.**
For the complete canonical source at physical heat time zero, the
[Packet04][packet] acquisition and the accepted Note01 error theorem give
\[
\boxed{Q_{3,1}\ge L_{1,2}>7\cdot10^{-23},\qquad
Q_{3,4}\ge L_{4,2}>10^{-74}.}
\]
Here Q3,k=D4,k*D2,k and L is exactly Note01 (19), with exact b=1/16,
the compact first-mode reference on [0,2], and full E+B(2) payment.
The simple rational floors are deliberately weaker consequences of the
computed lower bounds, not measurements or fitted targets.

The [certificate record][record] stores exact dyadic input/output balls,
versions, hashes and work counts. Its [script][code] includes both the
Arb acquisition and a standard-library exact verifier. The [self-assessment][review]
records author checking with fresh read-only same-model contributions;
separate E04 r2 assessment remains the recommended next task. This is
not independent specialist review or a formal proof of FLINT.

## 1. Fixed domain, theorem and numerical result

[Note01][source], accepted by [E04 Review01][review01], proves for each
fixed k that canonical Q3,k is bounded below by
\[
L_{k,2}=P_k(1/16,x^{[2]})-
\sum_{1\le|\alpha|\le6}|t_{k,\alpha}(x^{[2]})|
\prod_j(E_j+B_j(2))^{\alpha_j}.
\]
The polynomial is collected before absolute values; the k=1 boundary
terms and cancellation are retained, and k=4 has no b. The exact code
regenerates the same polynomials, permutation identities and translation
data as E03: 111 and 881 translated monomials including the constant.
All coefficient and polynomial hashes agree with the frozen diagnostic.
No D4 sign is used in that error theorem or in this acquisition.

The rigorously acquired reading values are:

| k | q enclosure display | Residual majorant upper endpoint display | Certified lower endpoint display |
| --- | --- | --- | --- |
| 1 | `[7.333591590231455889232e-23 +/- 2.55e-45]` | `[5.331069492108207161055e-26 +/- 3.93e-48]` | `[7.328260520739347682071e-23 +/- 1.99e-45]` |
| 4 | `[1.378703097586449692544e-74 +/- 5.00e-96]` | `[5.674238812808856406492e-78 +/- 2.07e-100]` | `[1.378135673705168806903e-74 +/- 1.49e-96]` |

**Display convention:** these are 22-digit Arb reading displays. Even
an exact dyadic endpoint can print with `+/-` because decimal conversion
introduces a display enclosure. The mathematical endpoints are the
serialized mantissa/exponent pairs; the record verifier checks those
pairs with Fraction arithmetic. The upper majorant need not enclose the
exact residual from below; it is used only as an upper bound.

## 2. Rigorous compact acquisition

The same eight exact compact integrals as E03 are acquired:
\[
x_j^{[2]}=\int_0^2 f_j(u)\,du,\quad
f_j(z)=\frac{z^{2j}}{8(2j)!}\exp(z-\pi\exp(4z)),\quad j=0,\ldots,7.
\]
For every fixed real pi parameter in the enclosing pi ball, f_j is
entire: integer powers and exponential composition have no branch cuts
or poles. This justifies ignoring the integration callback's analytic
flag; correctness is not inferred merely from testing points. Ball
operations enclose the true pi choice uniformly. The real path and real
integrand prove that each exact integral is real. The imaginary enclosure
containing zero is a consistency requirement, not the proof of reality.

Each of the five exact rational intervals
[0,1/8], [1/8,1/4], [1/4,1/2], [1/2,1], [1,2] is integrated by
python-flint acb.integral. Every finite complex segment ball is retained;
their outward sum gives X_j after real projection. All 40 segment balls
are finite and their imaginary parts contain zero. The verifier checks
segment coverage and containment of the sum of segment intervals in X_j.

The installed versions are **Python 3.12.14, python-flint 0.9.0, FLINT
3.6.0**, one arithmetic thread. Actual precision is **384 bits**; exact
relative and absolute goals are 2^-320 per segment. deg_limit=128,
eval_limit=5000, depth_limit=20 and use_heap=True match the packet.
The [python-flint API][acb] describes the analytic callback and accuracy
options. The [FLINT author's integration documentation][flintdoc]
describes rigorous adaptive Gauss–Legendre enclosures and the fact that
accuracy goals are not acceptance guarantees. The consulted FLINT page
is labeled 3.7.0-dev; the actual executable version remains 3.6.0 and is
recorded above. No new library or third-party PDF was installed or saved.

The exact acquisition radii are:

| j | Compact moment, approximate reading | Exact dyadic radius of X_j |
| --- | --- | --- |
| 0 | 0.0003598945119687580031818 | `381063309 * 2^(-350)` |
| 1 | 9.660941222003703701244e-7 | `533801109 * 2^(-351)` |
| 2 | 1.627644840705028004425e-9 | `498508367 * 2^(-354)` |
| 3 | 1.951114744896731063604e-12 | `572996425 * 2^(-353)` |
| 4 | 1.785488085717124493886e-15 | `586597313 * 2^(-358)` |
| 5 | 1.305273057733602794014e-18 | `748051997 * 2^(-364)` |
| 6 | 7.869627268918318332095e-22 | `325460037 * 2^(-369)` |
| 7 | 4.006747617224073630247e-25 | `976177359 * 2^(-354)` |

These radii pay quadrature truncation, pi uncertainty and arithmetic
rounding in the compact integrals. No heuristic quadrature-error estimate
or difference between precision passes is used as an error bound.

## 3. Complete tails and interval propagation

Compute in Arb, with positive denominators checked,
\[
E_j=\frac{e^{-4\pi}}{8(1-e^{-5\pi})(16\pi-1)^{2j+1}},
\]
\[
B_j(2)=\frac{e^{2-\pi e^8}}{8(2j)!}
\sum_{h=0}^{2j}\binom{2j}{h}\frac{2^{2j-h}h!}{(4\pi e^8-1)^{h+1}}.
\]
Note01 proves that E covers the whole n>=2 source and B the whole
first-mode exterior u>2. All E and B balls have positive lower endpoints.
B0 is about 1.75128e-4072 and B7 about 3.29191e-4079; every B is retained
and separately serialized. E+B is added outward, even when its midpoint
is unchanged. This resolves the unpaid rounding in the E03 floating run.
No truncated-domain Green identity is invoked and the canonical smooth
source is unchanged. The reference retains its positive atom description;
no PF property is assumed for it.

For the moment box X and tail balls, let
\[
q_k^- = \operatorname{lower}(P_k(1/16,X)),\quad
A_{k,\alpha}=\operatorname{absUpper}(t_{k,\alpha}(X)),\quad
T_j=\operatorname{upper}(E_j+B_j(2)).
\]
Every actual t at the exact compact moments lies in its evaluated ball,
so |t(actual x)|<=A. All T are positive. Outward multiplication and
summation, followed by an upper endpoint, give
\[
\mathcal R_k(x^{[2]},E+B)\le
U_k:=\operatorname{upper}\sum_{\alpha\ne0}A_{k,\alpha}T^\alpha.
\]
Finally ell_k=lower(q_k^- - U_k) is rigorous and
Q3,k>=L_(k,2)>=ell_k. All occurrences of x, in q and in every Taylor
coefficient, use the same enclosing X. This pays acquisition uncertainty
without treating it as a fictitious additional source tail. Dependencies
can only widen the bound; they are not assumed independent equalities.
All degrees 1,...,6 are retained.

## 4. Exact serialized-record verification and work limits

One independent arithmetic path inside the same script recomputes
polynomial intervals from the stored moment balls using Fraction. For
positive X endpoints, powers and products are bounded at endpoints;
signed polynomial coefficients are summed with the correct orientation.
Each translated coefficient is collected before its absolute upper bound.
For the tail payment the verifier forms exact upper(E)+upper(B), then
rounds **up** to an absolute dyadic grid 2^-384. This contains even the
nonzero B, regardless of whether it changes a midpoint. It evaluates an
exact rational residual upper bound and obtains lower bounds exceeding
both displayed rational floors. Both `witness_verified` fields are true.

The saved-record command also checks code/input hashes, segment sums,
fixed cases and moments, dyadic endpoint positivity and count consistency.
It passed under standard Python without importing FLINT. It trusts the
identified Arb integral/constant/tail enclosures and the analytical
Note01 theorem; it is not an independent implementation of integration,
transcendental constants or the entire FLINT library.

The sole acquisition completed in **0.713642541 seconds**, including
imports, exact assembly and rational propagation, with **4,546 callback
evaluations**. The 384-bit pass succeeded; no 512-bit refinement or
acquisition replay occurred. The separate saved-record verification took
**0.749134416 seconds**. There were no failed or capped cases and no
post-start implementation changes. All costs are local measurements.
The 180-second / 200,000-callback acquisition limits were respected.

## 5. Consequence, controls and boundaries

The accepted lower-order result gives D2,k>0 for the unchanged source.
Thus for lambda1=7e-23 and lambda4=1e-74,
D4,k>lambda_k/D2,k>0 at the two stated indices. This is a quantitative
comparison obtained by this payment; no numerical D2, D3, relative eta,
unbounded-index or higher-order claim was acquired. Existing finite-order
PF44 coverage already includes this pilot. No new positivity range,
Mellin/Gaussian estimate or RH conclusion is claimed.

Read the [result index][results], [theta cluster][theta] and
[control screen][controls], and [avoid index][avoid], especially
[joint payments][a12], [precision evidence][a04], [bounded numerics][a10]
and [scope][a07]. The claim-specific controls are those in E04 Review01:
weighted-square controls change unit coefficients; Euler-factor controls
change the literal source series; reflected and smooth positive-primitive
controls do not supply its complete unit-square expansion. Those premises
and their payments must be recomputed for altered sources. No uncalculated
failure of their finite L test is asserted. Positive-time collisions do
not contradict this time-zero finite-order result.

**Next: [E] RGD-E04 r2 — Sol**, separately assess this fixed certificate
and its consequence under the [continuation/model-change checklist][next].
The present [self-assessment][review] is by the proof/implementation author,
with same-model contributing checks and shared premises. B03 remains
gated; k=2,3, k>=5 and all order dependence are untouched. Do not run a
larger scan or alter the source/payment in this continuation. No parent/
sibling register, global summary or manuscript milestone was changed.

## Versions and replay instructions

Certificate SHA-256: `6db6276d65ea11706286cffa0aef899d1097f8e4bac76cbdd70f0ef40d692298`.
Code SHA-256: `b4863a6840cd4d68b10fe993f3f4cdc5e66dd8b3d44903445b306a50c8879db4`.
Frozen Packet04 SHA-256: `18bf3cfd702a38123bdf22b79f6a0e568b262fac1a4881330443afc95fbf3dd1`.
All six input hashes are in the certificate. Earlier Note01, E04 Review01,
E03 return/code/record and all frozen requests remain unchanged.

```text
python /absolute/path/to/10_radial_green_determinants/numerics/rgd_e02_two_case_certificate.py --verify /absolute/path/to/10_radial_green_determinants/numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json
```

To regenerate acquisition, use a Python environment with python-flint
and the script's --output option with a fresh temporary output path;
preserve the issued record. No regeneration is requested by this note.
The certificate is about 66 KB; there are no large derived arrays, PDF
builds or manuscript snapshot folders.

[packet]: ../research-progress/handoffs/04_RGD_E02_R1_RIGOROUS_TWO_CASE_ACQUISITION_20261104.md
[source]: 01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md
[review01]: ../reviews/01_RGD_E04_R1_BOUNDARY_PRESERVING_COMPARISON_ASSESSMENT_20261104.md
[record]: ../numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json
[code]: ../numerics/rgd_e02_two_case_certificate.py
[review]: ../reviews/02_RGD_E02_R1_CERTIFICATE_SELF_ASSESSMENT_20261104.md
[next]: ../research-progress/handoffs/05_RGD_E04_R2_AND_MODEL_CHANGE_AFTER_E02_20261104.md
[acb]: https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral
[flintdoc]: https://fredrikj.net/fdoc/html/acb_calc/integrate.html
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a04]: ../../../../../../../avoid/04_counts_and_precision_as_evidence.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
