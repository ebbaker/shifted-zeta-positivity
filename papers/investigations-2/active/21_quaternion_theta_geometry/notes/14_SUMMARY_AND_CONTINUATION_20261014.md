# Investigation 21 summary and continuation

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**,
verified in this turn's transcript metadata. Parallel LLM mathematical
and implementation reviews supported the research summarized here.

Investigation 21 now proves both genuine stationary signs and a physical
norm gap throughout 0<=t<=1/2, |x|<=100. Complete-source contour shifting
also gives explicit absolute jet errors at the gamma exponential scale
for arbitrary heights. The remaining RH obligation is a normalized
stationary sign, or an admissible bounded-loss estimate, in an unbounded
region where time tends to zero as height increases.

## Mathematical setup

Keep the complete theta source and the independent real Newman time:

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad H(0,z)=\tfrac18\xi(1/2+iz/2),\qquad H_t=-H_{zz}.
\]

The adopted Fueter field is

\[
F(t,q)=H(t+\overline{z_1},z_0)
       +\mathbf jH_z(t+\overline{z_1},z_0),
\qquad q=z_0+\mathbf jz_1.
\]

On the physical real slice, F=H+j H_x and E=|F|^2=H^2+H_x^2.
For h_k=partial_x^k H define L_j=h_(j+1)^2-h_j h_(j+2), j=0,1.
The manuscript proves the RH reduction to absence of H=H_x=0 at
positive time; it suffices to exclude these collisions for 0<t<=1/2.
The two nonnegative signs L_j>=0 on the genuine stationary sets
h_(j+1)=0 suffice through the local predecessor theorem. A loss
L_j>=-K_j E also suffices if K_j>=0 remains locally bounded through
every candidate joint zero.

## Results established

| Result | Domain or precise scope | Main reference |
|---|---|---|
| Complete-source central norm gap and both stationary signs | 0<=t<=1, \|x\|<=8 | [Manuscript](../manuscript/quaternion_theta_geometry.tex), section 11; [Note 8](8_COMPENSATED_STATIONARY_SIGN_DERIVATION_20261014.md) |
| Full threshold time certificate | 272 closed cells on [0,1/2] x [7,41] | [Note 9](9_FULL_THRESHOLD_TIME_COVER_AND_HEIGHT_41_GAP_20261014.md) |
| Guarded forward continuation | A'=-C preserves the initial strict sign along regular stationary branches; derivative-pair and edge gaps prevent births and entry | [Note 10](10_FORWARD_STATIONARY_COLLARS_AND_BRANCH_CREATION_20261014.md) |
| Higher-height certificate | 510 further closed cells on [0,1/2] x [40,100] | [Note 11](11_CORRELATED_TRANSPORT_AND_HEIGHT_100_CERTIFICATE_20261014.md) |
| Arbitrary-height absolute jet payments | Complete-source shifted contour and adaptive cutoffs; normalized truncation errors smaller than any prescribed power, with p chosen accordingly; retained quadrature paid separately | [Note 12](12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md) |
| Remaining normalized signed target | Possible collisions satisfy T log\|a\|<=C; use a padded region with C'>C | [Note 13](13_NORMALIZED_SIGN_TARGET_IN_THE_COLLISION_CUSP_20261014.md) |

Combining the central result, the height 41 certificate and the three
higher bands gives

\[
\boxed{|F(t,x)|>10^{-16}\quad(0\le t\le1/2,\ |x|\le100).}
\]

Both stationary signs hold throughout this strip. On its higher band
40<=|x|<=100 the explicit stationary margins are L_0>10^(-30) where
h_1=0 and L_1>2*10^(-32) where h_2=0. No sign cell, direct norm cell
or merged branch window remains unresolved in the three new bands.
A possible positive threshold collision must therefore have |a|>100.

The computational improvement was to sum retained theta center jets
before evaluating their common Taylor monomials. This preserves endpoint
cancellation while retaining every positive remainder payment. The
higher-height run uses K=2, N=4, 256-bit Arb/Acb arithmetic, source
cutoff U=1, and space, time and Gaussian Taylor orders 16, 8, 32.

All three higher-band replays matched their records except elapsed
runtime. The retained exact auditor passes 6682 semantic checks, including
coverage, genuine stationary decisions, all retained pairings, 128 regular
branch windows, norm extraction and source bindings. These are internal
validated calculations and LLM reviews, not specialist refereeing or
formal verification.

## The remaining theorem

For x>0 put c=pi/8 and Z_k=e^(cx)h_k. Then

\[
Q_j=Z_{j+1}^2-Z_jZ_{j+2}=e^{2cx}L_j,
\qquad \mathcal N=Z_0^2+Z_1^2=e^{2cx}E.
\]

The next global target is, for j=0,1,

\[
Z_{j+1}=0\ \Longrightarrow\ Q_j\ge0
\]

throughout a padded moving region

\[
0<t\le1/2,\qquad |x|>100,\qquad t\log|x|<C',\quad C'>C.
\]

The classical localization constant C is unspecified. The collision
limit gives <=C, not a strict inequality with the same C. No numerical
cutoff can be extracted from that qualitative statement alone.
An alternative is \(Q_j\ge-K_j\mathcal N\) with K_j locally bounded through every
candidate joint zero. Neither absolute accuracy nor a quotient by an
unproved norm establishes this bound. No positive lower gap uniform in
height, and no assertion of simplicity at all time-zero zeros, is required.

For paid normalized approximations Z_k=p_k+r_k, |r_k|<=epsilon_k,
a concrete sufficient stationary condition is

\[
p_{j+1}^2-p_jp_{j+2}\ge
\epsilon_{j+1}^2+|p_j|\epsilon_{j+2}
+|p_{j+2}|\epsilon_j+\epsilon_j\epsilon_{j+2}.
\]

This is a nonnegative-sign target. All finite arithmetic cross terms
remain on its left side. Note 13 gives the corresponding direct
bounded-loss test without division.

## Prioritized continuation

1. **Implement a whole-cell normalized contour certificate.** Start with
   a small overlapping pilot such as [0,1/2] x [96,104]. Freeze the
   contour and cutoffs at each cell's right endpoint Y using Note 12's
   a_Y, N(Y), U(Y). Pay retained quadrature and variation throughout
   both parameters, together with the complete index and integration
   tails. The current contour checker only compares selected points.

2. **Decide the genuine stationary observations on that pilot.** Exclude
   stationarity only with paid derivative bounds or the rigorous
   monotone-endpoint test. Isolate regular branches, merge neighboring
   signed cells where needed, and retain unresolved cells explicitly.
   Evaluate Q_j minus its full error payment, or the direct norm floor,
   using the same physical jets as the existing certificate.

3. **Seek a source-specific signed estimate that scales.** Analyze the
   retained normalized paired sum in the region t log|x| bounded. A
   theorem must establish the signed surplus or locally bounded loss
   for every possible predecessor neighborhood. Further finite bands
   can test a method, but do not supply infinite coverage by themselves.

The contour identity belongs to the complete even source before any
raw-index truncation; individual raw channels lack its vertical
cancellation. Form physical jets before choosing an adaptive shift or
cutoff. The exact normalized derivative is partial_x Z_k=Z_(k+1)+c Z_k,
so ordinary stationarity of Z_j is not genuine stationarity. On a moving
stationary branch the normalized squared amplitude has the extra drift
term c chi' Z_j^2. Forward collars also retain their branch-creation
and edge guards. These constraints should remain explicit in the next
implementation and derivation.

The next deliverable is a derivation, a reproducible whole-cell contour
pilot and its small record, and an internal review identifying any
remaining signed remainder or unresolved cells.

## Reproduction and working files

Use the existing checkout at
`/Users/ebbaker/Documents/shifted-zeta-positivity`. Current research files
include uncommitted and untracked work; a new checkout from the present
Git commit would omit that work. Preserve one stable manuscript and the
existing open editor. The [35-page manuscript](../manuscript/quaternion_theta_geometry.tex)
and [build record](../manuscript/BUILD_RECORD.json) contain the current
source/PDF hashes, proof scope and validation. The
[analytic review](../reviews/8_SHIFTED_CONTOUR_AND_COLLISION_CUSP_INTERNAL_REVIEW_20261014.md)
and [higher-height review](../reviews/9_HIGHER_HEIGHT_CERTIFICATES_INTERNAL_REVIEW_20261014.md)
are the latest assessments.

From the investigation's numerics directory, the lightweight exact audit
uses the Python standard library:

```sh
python3 audit_correlated_source_height_records.py --output /tmp/inv21-height-audit.json
```

With python-flint 0.9.0 available, the contour implementation checks use
256-bit arithmetic by default:

```sh
python3 check_shifted_contour_payments.py --output /tmp/inv21-contour-payments.json
```

The [higher-band guide](../numerics/CORRELATED_SOURCE_HEIGHT_README_20261014.md)
gives the exact validated replay commands. The contour checker's five
heights through 10^12 evaluate tail formulas; its eight paid jet
comparisons are at x=41, t=0,1/2. They are not a whole-cell sign
certificate or an evaluation of millions of retained theta terms.

Save further derivations in notes/, code and small records in numerics/,
assessments in reviews/, and concise milestones in DRAFT_HISTORY.md.
Follow AGENTS.md and LARGE_FILES.md; keep raw session exports outside
the repository. No commit, tag, or manuscript snapshot was created
for this summary.

## Conversation continuity

This conversation is registered as chat 9 in the investigation's
[history folder](../chat-histories/README.md), titled
**Continue quaternion theta geometry**, actual thread id
`01a13c35-bd7e-7421-99b1-9bf423809c0c`. Preserve that registration and
its original identity. The [registry](../chat-histories/index.json)
is authoritative for current capture times, counts, sizes, model
configuration and hashes; do not freeze those changing values here.

Use tools/refresh_chat_history.py at the beginning and end of later
turns. Arrange the bounded --after-turn/--defer capture as the final
tool action before replying so the actual completed final message is
archived. Native completion-hook activation has not been verified.

## Suggested next session prompt

> Continue investigation 21 from notes/14_SUMMARY_AND_CONTINUATION_20261014.md
> in the existing local checkout. Preserve the independent-time Fueter
> lift and the height 100 certificate. Implement the complete-source
> shifted-contour four-jet method on a small closed overlapping pilot
> near x=100, freezing contour parameters per cell and paying every
> retained, omitted and parameter error. Test the genuine normalized
> stationary forms, retain all cross terms and unresolved cells, and
> use the result to pursue the signed target in Note 13's moving small-time
> region. Save the derivation, code, small execution record and internal
> review. Refresh this investigation's chat history through the shared
> recorder. Do not treat a successful finite pilot as an all-height proof.
