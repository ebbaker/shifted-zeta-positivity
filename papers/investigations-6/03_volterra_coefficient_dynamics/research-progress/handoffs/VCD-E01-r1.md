# VCD-E01 — Frozen request r1

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Issuer dispatch: **gpt-6-astra /
ultra**; separate backend verification unavailable. Requested executor:
**gpt-6.1-sol / ultra**, selected by Edward Baker. Record actual dispatch
and any available execution metadata in the return; do not infer backend
attestation. **Type E — routine analytical derivation of a fixed route.**

Parent: VCD-B01. Sole register:
[01_VOLTERRA_RESEARCH_PROGRESS_20261113.md](../01_VOLTERRA_RESEARCH_PROGRESS_20261113.md).
Request r1 is immutable after issue. Append a return or link a separate
return; any mathematical change requires an explicit revised request.

## Prerequisites and exact versions

Read the [B01 decision](../../brainstorm/notes/01_VCD_B01_LOGARITHMIC_ENVELOPE_DECISION_20261113.md)
and verify the SHA-256 identities in
[01_VCD_B01_E01_INPUTS_20261113.json](../../numerics/01_VCD_B01_E01_INPUTS_20261113.json).
Those are the complete theta-source TeX, inherited chain/Volterra note and
self-check, branch plan/overview, source crosswalk, reference guide and B01
decision. The register can change as tasks proceed; it is not a frozen
mathematical input. An unchanged mathematical source may be used after
recording an explicitly verified editorial-only hash difference; an
unexplained or mathematical difference stops dependent work for B01.

## Fixed source, normalization and domain

Retain the full complete positive even theta source
Phi(u)=e^u sum_(m>=1)(2r_m²-3r_m)exp(-r_m),
r_m=pi m²exp(4u), on u>=0, with its actual smooth even reflection.
W_lambda=e^(lambda u²)Phi; V_lambda=-log W_lambda.
P_n are monic orthogonal for W_lambda du;
h_n=int P_n²W_lambda du, beta_n=h_n/h_(n-1), beta_0=0.
For every integer n>=0 and **uniformly 0<=lambda<=1/2**, prove

\[
 \boxed{\beta_n+\beta_{n+1}\le B_n,
 \quad B_n=\operatorname{arcosh}^2(2n+12)/16.}             \tag{E1}
\]

Here arcosh takes its nonnegative real branch. Keep a_n=sqrt(beta_n),
Z_lambda=h_0 and H_lambda(z)=Z_lambda <e0,e^(izJ(lambda))e0>/2.
There is no new height-domain claim: the output is a coefficient bound.
The one required consumer, for every finite integer N>=1, is

\[
 \boxed{h_N(1/2)/h_0(1/2)\le\prod_{j=0}^{N-1}B_j
 \le[\operatorname{arcosh}(2N+10)/4]^{2N}.}               \tag{E2}
\]

This supplies the normalized monic norm factor for the fixed J(1/2).
Do not call unnormalized h_N the normalized norm. JCH owns scalar
quadrature/readout error and TN6 owns shared transfer; neither result
is a prerequisite to proving E1/E2. No field sign, collision margin,
relative error, leading asymptotic or finite closure is requested.

## Fixed analytical method

1. Derive (log s_m)'=9+12/(2r_m-3)-4r_m for each positive summand.
   Use complete-source domination to differentiate the sum. Its score is
   the positive weighted mean, giving V_lambda'(u)>=4pi exp(4u)-13-u
   for u>=0, using pi>3 and 2lambda<=1. Do not use an m=1 replacement.
2. Prove uV_lambda'(u)>=cosh(4u)-11 by evenness and the two regions
   |u|<=1/2 and |u|>=1/2. The first uses |u|²+13|u|<=27/4 and
   cosh2<4. For the second, (4pi-1/|u|)exp(4|u|)>=10exp(4|u|)
   >=|u|+13 suffices. Check elementary constants explicitly.
3. Integrate (uP_n²W_lambda)' on the full line. Prove vanishing boundary
   terms and integrability from the complete tails. Degree orthogonality
   gives int uP_nP_n'W_lambda=n h_n, hence
   E_n[uV_lambda']=2n+1 under dnu_n=P_n²W_lambda du/h_n.
   The recurrence gives E_n[u²]=beta_n+beta_(n+1).
4. Establish convexity of f(v)=cosh(4sqrt(v)) on v>=0 from its positive
   power series. Jensen and step 2 give
   cosh(4sqrt(beta_n+beta_(n+1)))<=2n+12, proving E1.
   Do not apply Jensen directly to log², whose global concavity fails.
5. Apply E1 with n=j-1, discard beta_(j-1)>=0, multiply j=1..N,
   then use monotonicity of B_j to obtain E2. State explicitly why
   pointwise-in-n integration by parts yields the all-n assertion with
   common constants without needing a growing-derivative tail claim.
6. Recheck the B01 control screen, especially the weighted-square controls
   that share the score argument. An approximation bound can hold at a
   collision. Preserve each untested comparison and conditional qualifier.

## Output, acceptance and finite work limit

Save one derivation note in notes/, one short return in this handoff
folder, and update the sole register and concise DRAFT_HISTORY. Record
input hashes, date, model/effort provenance, proof result or exact failed
step, corrections and limitations. No numerical experiment is authorized
or needed. One proof route, one all-degree/time regime, one consumer,
one return and **at most one bounded correction pass**. Routine algebra,
elementary inequalities, domination details and notation corrections are
allowed. Do not optimize constants, import a new asymptotic theorem,
change source or observation, or enlarge the task into transport.

Acceptance is a complete proof of E1 and E2 with the stated constants and
quantifiers, full-source justification, and honest source-class/control
scope. If the route cannot establish them, the exact unsupported step or
failed allowance completes the return unfavorably. No unsupported
favorable conclusion. A new mechanism, target, time/degree regime or
conceptual theorem returns to VCD-B01; it is not an E correction.

E01 completion makes the existing VCD-E02 assessment eligible. Freeze its
request against the actual E01 result and exact source versions before
assessment. The E02 reviewer checks constants, monicity, boundary terms,
all-degree scope, normalized consumer and controls; model change alone
is not independent specialist review.

Permitted writes are confined to this VCD branch. Do not edit parent,
sibling, root-summary or chat-history files. The parent coordinator owns
shared updates and chat capture. No manuscript or snapshot is requested.
