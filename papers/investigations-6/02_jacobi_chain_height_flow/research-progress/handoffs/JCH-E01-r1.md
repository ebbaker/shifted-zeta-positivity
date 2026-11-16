# JCH-E01 — r1 frozen request: finite-chain scalar error

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Request dispatch selection:
**gpt-6-astra / ultra**; actual backend model and effort unavailable.
Execution selected and authorized: **GPT-6.1 Sol / Ultra**.

**Type E.** The approximation, observation, proof route, domain and
completion test are fixed. Parent: JCH-B01, [decision](../../brainstorm/notes/01_JCH_B01_READOUT_DECISION_20261113.md).
Live owner: [sole JCH register](../01_JACOBI_CHAIN_RESEARCH_PROGRESS_20261113.md).
This request is immutable; append/link a return rather than rewriting it.

## Exact prerequisites

Read and verify every file in
[input manifest](../../numerics/01_JCH_E01_R1_INPUT_MANIFEST_20261113.json),
whose SHA-256 is
`6fafa20add1debfbe74378e42e2c044d34a34b9c6bec5d0f1ce4d0c35b40273d`.
It pins the complete source, inherited chain and check, source crosswalk,
plan, decision, control screen, inspected primary-source record and controls.
Hashes identify working-tree versions, not proof. A mismatch stops dependent
execution until the owner determines whether a new request is needed.
There is **no prerequisite VCD theorem**, certified coefficient table or
numerical source evaluation for this analytical request.

## Fixed objects and target

Use complete (\Phi), (W_*=e^{u^2/2}\Phi), (Z_*=\int W_*),
(d\mu_*=W_*du/Z_*), (J_*) unitarily identified with multiplication
by (u) including its domain. Let (\Pi_N) select sites (0,\ldots,N-1),
(J_N=\Pi_NJ_*\Pi_N|_{\operatorname{ran}\Pi_N}), (N\ge1).
Put (P_N) for the degree-(N) monic orthogonal polynomial and
(h_N=\int P_N^2d\mu_*=prod_{j=1}^Na_j^2).
In particular, the error constant uses the omitted boundary coupling (a_N).

The only physical observation is

\[
H_{1/2-\tau}(x)=\frac{Z_*}{2}\langle e_0,
 e^{-\tau J_*^2}e^{ixJ_*}e_0\rangle,
\qquad
H_N(\tau,x)=\frac{Z_*}{2}\langle e_0,
 e^{-\tau J_N^2}e^{ixJ_N}e_0\rangle.                 \tag{R1}
\]

Domain: (0\le\tau\le1/2), (x\in[-X,X]\subset\mathbb R),
any finite (X\ge0). Thus (0\le\lambda=1/2-\tau\le1/2);
real Newman height is twice zeta height. Norm: scalar absolute error,
uniform on this real rectangle. No complex-height, derivative, relative,
logarithmic, Green or whole-state estimate is requested.

Derive, or precisely identify a failure of,

\[
|H-H_N|\le\frac{Z_*}{2}h_NS_N(\tau,x),\qquad
S_N(\tau,x)=\sum_{k=0}^{N}
 \frac{\tau^kx^{2N-2k}}{k!(2N-2k)!}.                 \tag{R2}
\]

Derive the complete-source fallback, with
(M_1=\int e^{u^2}d\mu_*<\infty),

\[
\sup|H-H_N|\le C_*2^{-N}\cosh(X\sqrt{2N}),
\qquad C_*=Z_*M_1/2.                                \tag{R3}
\]

Give an explicit sufficient integer (N(X,\epsilon)) for R3 to be at
most (\epsilon>0), using (\cosh t\le e^t). One permitted formula is
to take (L=\log2), (b=\sqrt2X),
(d=\max(0,\log(C_*/\epsilon))), and

\[
N\ge\max\left(1,\left\lceil
 \left(\frac{b+\sqrt{b^2+4Ld}}{2L}\right)^2
\right\rceil\right).                               \tag{R4}
\]

Verify edge cases and adjust an elementary constant only with a recorded
correction. Do not evaluate (C_*) or claim a certified numerical depth.
The gain is a formula proving convergence for growing (N) on each finite
height rectangle, not an efficient or sharp transport rate.

## Frozen derivation method

1. Identify (e_0)'s spectral measure for (J_N) with the positive
   (N)-node Gaussian quadrature for (\mu_*), with exactness through
   degree (2N-1). Prove or explicitly justify the full-line setting.
2. For real (s), use the degree-(2N-1) Hermite interpolant to
   (\cos(su)) at the (N) real nodes, matching first derivatives.
   Its pointwise remainder is bounded by
   (P_N(u)^2|s|^{2N}/(2N)!). Integrate to obtain the scalar pure-height
   error. The proof may use repeated Rolle's theorem; no unjustified
   complex mean-value point is permitted.
3. Use (e^{-\tau u^2}\cos(xu)=
   \mathbb E\cos((x+\sqrt{2\tau}G)u)), (G\sim N(0,1)),
   including (\tau=0). Justify exchanges; evaluate the exact even
   Gaussian moment to obtain R2.
4. Use the minimizing property of the monic orthogonal polynomial to
   show (h_N\le m_{2N}\le N!M_1). For (T=1/2), reorganize
   (N!S_N(T,X)=T^N\sum_{j=0}^N[N!/(N-j)!]
   (X^2/T)^j/(2j)!), and bound the falling factorial by (N^j).
   Derive R3/R4, with every normalization factor retained.
5. Identify the sole matched baseline: direct Gaussian quadrature with
   these same nodes/weights is exactly R1. No speed or acquisition advantage
   follows. Distinguish finite-operator readout error from exact-state
   prefix tail, and (J_N^2\) from (\Pi_NJ_*^2\Pi_N).
6. Recheck the [actual control screen](../../notes/01_JCH_B01_SOURCE_AND_CONTROL_SCREEN_20261113.md),
   especially the exact three-atom event. Positive generic error bounds
   survive collisions. A failed allowance is not a lower actual error.

## Acceptance, allowed work and stop

Acceptance requires one self-contained derivation of R2 and R3/R4 with
constants, quantifiers, endpoint and boundary conventions, a source-matched
quadrature comparison, and the controls/scope just stated. It must explicitly
list the missing practical inputs (a_1,\ldots,a_N,Z_*,M_1), their
certification cost and the absence of a relative lower margin. A precise
failed proof step also completes the analytical task with a limited
disposition; it does not establish a universal no-go.

Finite work: **one theorem family, one domain, one analytical derivation,
at most one routine correction pass; zero numerical campaigns**.
Routine algebra, standard inequalities, a direct proof of the stated
interpolation ingredient and normalization repairs are permitted. Changing
the observable, physical source, boundary convention, domain or coefficient
hypotheses; adding a transport mechanism; or borrowing an unproved VCD
bound requires a B decision. Continue unaffected checks but do not replace
the request silently.

Save `notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md`, a compact
return at `research-progress/handoffs/JCH-E01-r1-return.md`, and update
only the JCH register, branch navigation and DRAFT_HISTORY. Record actual
date, dispatch and available backend provenance, request/input hashes,
proof status, corrections, limits and next declared task. Read the live
register before editing. No parent/shared/chat registry edits.

When E01 completes, proceed under standing authorization to **[E]
JCH-E02 — GPT-6.1 Sol / Ultra**, one assessment of this unchanged request
and its actual return, including at most one response check. A separate
worker/model is internal source-sharing review, not specialist independence.
