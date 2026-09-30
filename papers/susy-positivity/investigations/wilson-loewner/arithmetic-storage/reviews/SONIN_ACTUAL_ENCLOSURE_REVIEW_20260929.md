# Internal critical review of the actual-Sonin enclosure test

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed. This consolidates separate same-model checks of the
prolate certificate, source integrals, full projection errors, compact
convolution implementation, and omitted-direction inference. It is not
independent human refereeing.

**Verdict.** The [main enclosure note](../notes/SONIN_ACTUAL_PROJECTION_ENCLOSURES_20260929.md)
and its records support certified bounds for a genuine Sonin-projected
trial family. They also support a strict lower bound on its missed positive
trace. They establish no sign of the complete arithmetic residual.

## 1. Checks of the infinite-dimensional inputs

The [prolate derivation](../notes/SONIN_PROLATE_RESOLVENT_CERTIFICATE_20260929.md)
uses the correct half-axis Legendre normalization and exact factorial
moments. The nuclear cosine Taylor tail, squared-operator perturbation,
interval LDL, exact dyadic inverse approximation, and full inverse residual
are consistent. The complement outside the polynomial space is retained.
An independent 192-bit replay passed the same gap and norm caps as the
256-bit record. The condition number is large but explicitly bounded.

The [source derivation](../notes/SONIN_SOURCE_NORM_CERTIFICATES_20260929.md)
has correct differentiation recurrences, pole-neutrality, and normalization.
Its Acb callback claims analyticity only away from the endpoint poles;
both omitted bump tails are enclosed analytically. The L1 root split
handles the absolute-value kink explicitly. The gamma upper bound uses
the digamma integral and recurrence, then a Jensen expression increasing
in both norm variables. It does not assume Weil positivity. Source record
hashes match the corresponding generating code.

The scalar cutoff bound is legitimate because the already audited
cutoff operator is the Sonin projection plus a positive trace-class
prolate correction. The kernel bounded by `||C||1<2.858` is **delta**,
not epsilon. Confusing these kernels would invalidate the smaller bound;
the final notes and program use the cutoff domination correctly.

## 2. Projection and compact-matrix checks

The exact trial vectors are `Pi eta_n`; the functions integrated on compact
intervals are only proxies with rigorous global L2 errors. The factorial
cosine-leakage bound follows from Rodrigues' formula and includes the
integration factor. Leakage up to frequency 2 is retained when bounding
`Aq_n`; cutoff-1 leakage alone would be insufficient.

The smooth transition of width `10^-40` is handled by a global norm bound,
not by numerically pretending to resolve it. The trial seeds are smooth
compact functions of the positive-axis variable; source smoothness and
pole neutrality are separate properties. The full projection-tail bounds
are valid without truncating the spatial line.

The finite synthesis map need not be an isometry. Galerkin orthogonality
gives the same residual identity for its positive compressed matrix. The
matrix order `J=Q* H A Q`, its real cross term, and the last trace term
in (6) were checked by direct expansion. The actual finite A and H
matrices passed interval positivity checks.

The spline implementation has the correct Gram weights `66,26,1` over
120 and the factor `h^3/scale^4`. Discrete convolutions are exact integer
polynomial products. The source interpolation error `h²||F''||1/8` and
the seed cell-average error `h²||F'||1||B'||2/pi²` are justified. The
latter uses the seed derivative inside each cell; it does not wrongly
treat the zero-extended seed as a whole-line H1 function. Prime translations
align exactly with grid cells. A review suggestion added an explicit Arb
check that the source grid covers its support, so floating candidate grid
selection is not a certificate decision.

## 3. What the numbers establish

The rank-two trial trace lies in `[0.0074225,0.0074246]` for the even
source and `[0.0122013,0.0122039]` for the odd source. The broad full
residual upper bounds are valid but do not resolve the trace accurately.
They retain all infinite tails; their width is predominantly the coarse
scalar h0 bound, not merely the spatial approximation error.

An additional degree-21 vector provides a rigorous **omitted-direction
witness**. The original and enlarged trial spaces use exactly the same
projection, metric, cutoff convention and sources, so Galerkin
monotonicity applies. Outward subtraction gives missed trace exceeding
0.00373 and 0.00712. This conclusion survives even perfect evaluation
of the original rank-two entries. The comparison program verifies the
parameter match and generator bindings and checks the strict inequalities.

The result rejects the specific `10^-8 B_infinity` accuracy allocation
for this trial space. It does not prove that this tolerance is necessary
for every source-specific sign question, nor that the trial space is
useless at all coarser tolerances. There is no arithmetic residual sign
claim: the missed quantity is part of an independently positive Sonin trace.

## 4. Decision and evidence limits

| Item | Status |
|---|---|
| Actual prolate inverse and nuclear bounds | Internal interval certificate, including infinite complement |
| Smooth source norms and derivatives | Internal interval certificate, including endpoint tails |
| Actual-Sonin finite matrices | Certified via compact proxies plus full L2 errors |
| Full Galerkin trace error | Enclosed, but upper bound too broad for a precise trace diagnostic |
| Selected rank-two small-error target | Refuted by one certified omitted direction |
| Complete first-prime arithmetic residual | Not evaluated or sign-certified |
| Arbitrary-support positivity | No new inequality or limit theorem |

The appropriate next task is the finite polynomial–cosine evaluation of
the scalar smoothed archimedean trace using the certified resolvent.
That should establish the trace scale before another trial space is
chosen. A source-adapted space may later be worthwhile, but routine
degree/rank increases are not supported by this test. The signed
place-addition covariance and its arithmetic contribution remain open.

All programs/records are small, and no large grid arrays or matrices are
saved. Reproduction must use ordinary Python, not `-O`/`-OO`, because the
source program retains assertion guards. The record hashes establish
provenance; arithmetic replay establishes the numerical bounds. The
[new continuation](../notes/SONIN_CONTINUATION_AFTER_ENCLOSURE_TEST_20260929.md)
preserves these distinctions.
