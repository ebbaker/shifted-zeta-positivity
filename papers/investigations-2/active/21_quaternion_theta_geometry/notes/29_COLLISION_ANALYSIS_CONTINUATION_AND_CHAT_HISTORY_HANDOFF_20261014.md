# Collision analysis: continuation and chat-history handoff

> **Chat-history routing update, 17 October 2026.** Current histories: [Chat 14 — Review quaternion theta handoff](../chat-histories/0014_2026-10-15T02-29-33Z_review-quaternion-theta-handoff.json). Use this investigation’s [local registry](../chat-histories/index.json) and [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json) for current numbers and preserved provenance; this supersedes the routing and numbering below. All future investigation 21 chats belong in this investigation’s `chat-histories/` folder.

14 October 2026 (America/New_York). Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**,
verified from the source session metadata. This note records the completed
collision analysis and prepares a new research chat; it proves no new
theta-specific estimate.

## Start here

The user requested collision analysis for intuition before further
brainstorming, and now requests a new chat, verified history, a continuation,
and a recommendation between Codex and ChatGPT.

Read in this order:

1. [Note 28: collision scales and delayed comparisons](28_COLLISION_SCALES_AND_DELAYED_COMPARISONS_20261014.md).
2. [Review 20: analytic assessment and exact checks](../reviews/20_COLLISION_BEHAVIOR_AND_LOGARITHMIC_LOSS_REVIEW_20261014.md).
3. [Note 27: broader results assessment and research paths](27_RESULTS_ASSESSMENT_AND_RESEARCH_PATHS_20261014.md).
4. [Note 26: inherited coverage and protocol handoff](26_CONTINUATION_AND_CHAT_HISTORY_HANDOFF_20261014.md), consulting its linked sources for domain details.

The next substantive task is to **brainstorm theta-specific paths forward**,
especially estimates that preserve the combined signed stationary product
and allow a prescribed logarithmic energy loss. Rank concrete mechanisms
and their missing arithmetic inputs before selecting one narrow lemma or
small diagnostic. Broad numerical sweeps and additional height extensions
are not the requested next step.

## What was established, and what was already known

Write h_k=partial_x^k H, H_t=-H_xx,
E=h_0^2+h_1^2, and L_j=h_{j+1}^2-h_j h_{j+2}.
The manuscript already proves the all-multiplicity stationary predecessor,
universal collision pole, bounded-loss theorem, and collision criterion:
labels `fc:hermite`, `fc:predecessor`, `fc:bounded-loss`, and
`fc:rh-collision` in the [manuscript](../manuscript/quaternion_theta_geometry.tex).
Do not present those results as discoveries of this chat.

For a hypothetical finite-order collision at (T,x_*), T>0, of multiplicity
m=2r+j, r>=1 and j in {0,1}, put s=T-t and W=h_j. Observe the genuine moving
stationary predecessor W_x=0. With collision jets
A=H^(m)(T,x_*) nonzero, B=H^(m+1)(T,x_*), D=H^(m+2)(T,x_*), and k=A/r!,
Note 28 refines the predecessor as

\[
 \chi(s)=x_*-\frac{B}{rA}s+O(s^2),\qquad
 \alpha=\frac{D}{(r+1)A}-\frac{B^2}{2rA^2},
\]

\[
 W=k s^r(1+\alpha s+O(s^2)),\qquad
 \frac{\mathcal L_j}{E}=-\frac r s-\alpha+O(s).
\]

For even multiplicity E=W^2 exactly on this branch. For odd multiplicity,

\[
 \frac{H}{H_x}=-\frac{B}{r(r+1)A}s+O(s^2),\qquad
 E=W^2(1+O(s^2)).
\]

The explicit finite part and odd coefficient are refinements from this
chat. The residue r=floor(m/2) is inherited from the manuscript.

Time orientation matters: as t increases, a nonreal conjugate pair reaches
the real axis at T and then splits into real roots. The double model has
H approximately c(y^2+2s)/2, E approximately c^2s^2, and L_0 approximately
-c^2s. Its physical curvature stays finite; the ratio to a vanishing
amplitude creates the pole. The cubic model H=y^3-6(t-T)y has no real H_x=0
predecessor, but H_xx=0 detects L_1/E=-1/s. L_0 is globally nonnegative in
that cubic control, so the second stationary test is indispensable.

On h_1=0, the moving energy derivative is E'=2L_0. On h_2=0 it is
E'=2L_1+2xi' h_0h_1; retain the extra transport term. Its ratio to E is O(s)
on the collision predecessor. Only the moving derivative of H_x^2/2 is
exactly L_1 in the odd case.

## Main diagnostic: a positive delay can hide essential cancellation

Use the existing constants a=pi/16, b=1/4, mu=a^2+b^2 and complete residual

\[
 C_j(v,x)=-W_{xx}(v,x)-2aW_x(v,x)-\mu W(v,x).
\]

Only current stationarity removes the drift term. Earlier samples do not
satisfy a stationary condition. The prescribed smooth delay is

\[
 \delta(t,x)=\frac{t}{2(1+t\log(1+x^2))},\quad \tau=t-\delta,
\]

with retained and absorption products

\[
 P_j=W(t,x)C_j(\tau,x),\quad
 Q_j=W(t,x)\{C_j(t,x)-C_j(\tau,x)/2\}.
\]

Their exact recombination on the current stationary set is

\[
 P_j/2+Q_j=\mathcal L_j-\mu W^2.
\]

At a finite positive-time collision the delay has a positive limit delta_*.
If the earlier residual tends to a nonzero value
 g=C_j(T-delta_*,x_*), then

\[
 \frac{P_j}{E}=\frac g k s^{-r}(1+O(s)),\qquad
 \frac{Q_j}{E}=-\frac{P_j}{2E}-\frac r s-(\alpha+\mu)+O(s).
\]

For r>1, the separate products have stronger opposite poles than the
combined observation. Intermediate powers can also cancel; do not truncate
both products to their most conspicuous powers and infer the full remainder.
Avoiding individual magnitudes worse than 1/s requires the earlier residual
to vanish to order at least r-1 along the observer. A diagnostic minimum of
separate nonnegative loss budgets behaves like |g/k|/(2s^r), compared with
the combined r/s scale. This diagnostic quotient is not an admissible way
to define a source coefficient for a proof.

A favorable-side quartic heat control has L_0>0 but a negative retained
product of order E/u^2 under a fixed delay. Therefore separate retained
positivity can fail even where the combined Laguerre form is favorable.
These polynomial controls diagnose proof mechanisms; they are not theta
counterexamples. Shrinking-delay calculations are diagnostic only: a delay
chosen using an unknown collision time is not a source-defined protocol.

## New conditional target: prescribed logarithmic loss

For fixed M>0 and finite q>=0, define

\[
 F_q(e)=e[1+\log_+(M/e)]^q\quad(e>0),\qquad F_q(0)=0.
\]

If independently established coefficients K_j, locally bounded through
candidate events, satisfy on both requisite stationary sets

\[
 \mathcal L_j\ge-K_j F_q(E),
\]

then every finite-order analytic collision in the covered domain is
excluded. Indeed the predecessor has

\[
 \frac{-\mathcal L_j}{F_q(E)}
 \sim\frac{r}{s[2r\log(1/s)]^q}\longrightarrow\infty.
\]

With the full domain required by the manuscript's collision criterion,
this would imply RH. **No theta-specific estimate of this kind has been
proved.** The new statement is a conditional sufficient criterion and a
possible research target. For q>0 it relaxes bounded relative loss. It is
not an application of the old bounded-loss theorem with an unbounded
coefficient. For q>1 the proof uses finite-order analyticity: smooth flat
scalar functions can reach zero under such a loss bound. That scalar control
is not an analytic heat or theta example.

A bounded coefficient multiplying E^p excludes multiplicity 2r+j by this
argument only when p>1-1/(2r). Every fixed p<1 misses sufficiently large
multiplicity. F_q(E)=o(E^p) for every fixed p<1, so square-root absolute
errors remain too large. Do not infer a bound from a sampled energy floor,
or define K_j by dividing the observed deficit by the energy gauge.

## Validation and unchanged coverage

The [exact rational checker](../numerics/check_collision_behavior.py) and
[execution receipt](../numerics/COLLISION_BEHAVIOR_CHECKS_20261014.json)
record 1,072 assertions: 60 jet cases with multiplicities 2 through 13,
double/cubic controls, 30 delay comparisons, canceling poles, and power-loss
exponents. A parent replay was byte-identical to the independent agent's
receipt. Source SHA256 is
`d54cd227f2be4a184e123105dec6f20fa798f5f85a96359d2c1304fb4efc5cd0`;
receipt SHA256 is
`4c918a39f1b261bef99536e4d51ffd017c97ca04e2adcbc74733e3661c3fd3e5`.
The checker covers finite algebraic examples. Analytic branch existence,
all-multiplicity statements, and the logarithmic limit require the written
proofs. Review 20 is internal LLM review, not external peer review or formal
verification. No theta quadrature was run for this collision analysis.

Coverage inherited from Notes 25–26 is unchanged:

- For 0<=t<=1/2 and |x|<=112, sqrt(E)>10^(-17) and L_j>0 on the respective
  current stationary sets. This is not full retained/absorption positivity
  everywhere in that finite box.
- The new regular h_1=0 branch in 107<x<108 and h_2=0 branch in 109<x<110
  have positive retained and absorption products for all comparison times
  0<=v<=t. That assertion applies to these branches.
- Full outer signs hold for theta=t log(|x|/(4pi))>=3+epsilon at sufficiently
  large height, with the cutoff unevaluated. Smooth-delay comparison signs
  hold for theta>=13/4 at sufficiently large height in an already covered
  outer region. A separate explicit threshold-5 result uses X=4pi exp(10^9).
- The finite transition above 112 and the unbounded inner cusp remain open.

The stable 39-page manuscript integrates Notes 19–22. Notes 24–28 remain
outside it. This chat made no manuscript revision, commit, tag, or snapshot
folder. The collision milestone is recorded in
[DRAFT_HISTORY.md](../DRAFT_HISTORY.md).

## Suggested next research discussion

Compare a few concrete theta-source mechanisms for the combined stationary
inequality. For each candidate, state the exact signed quantity controlled,
the cancellation retained, the arithmetic input still missing, and whether
it can plausibly yield bounded relative loss or only logarithmic loss.
Use the double/cubic and higher-multiplicity controls to reject mechanisms
that would also incorrectly exclude the polynomial examples. A route may
legitimately use special theta structure absent from those examples, but
that structure must be made explicit. Recommend one next analytic lemma
or narrowly scoped diagnostic after this comparison.

A suitable opening for the new chat is:

> Continue investigation 21 from Note 29, then read Note 28, Review 20, and
> Note 27. We have analyzed hypothetical finite-order collisions and now
> want to brainstorm theta-specific paths forward. Focus on preserving
> cancellation in the combined stationary Laguerre observation and on
> whether a prescribed logarithmic energy-loss bound might be more
> accessible than bounded relative loss. Distinguish the manuscript's
> existing universal collision pole from Note 28's refinements and
> conditional criterion. Compare a few concrete analytic mechanisms,
> identify the exact missing arithmetic inputs, and recommend one next
> lemma or small diagnostic. Do not begin broad numerical sweeps or further
> finite-height certification yet.

## Verified history and repository continuity

Checkout HEAD, read during this handoff:
`d48a69cc0f1761f52ff190e256cccc6ba9e403d7`.
Research Notes 27–29, the collision checker/receipt, Review 20, the history
verification receipt, and archive #11 are working-tree additions; the
investigation draft history and formal replay registry are modified.
These files are not contained in that HEAD. Use the existing local checkout
or explicitly transfer the working changes when changing environments.
Read current status again before any future commit.

The current conversation is **Review quaternion theta handoff**, thread
`01a13d64-ba41-7362-acfe-bf5978c84d11`, archive number **11**, uniquely
registered in the formal replay lane:

- [Archived public conversation](../chat-histories/0014_2026-10-15T02-29-33Z_review-quaternion-theta-handoff.json).
- [Registry](../chat-histories/index.json).
- [Verification receipt](../reviews/CHAT_HISTORY_COLLISION_HANDOFF_VERIFICATION_20261014.json).

Creation was 2026-10-15T02:29:33.891Z (14 October, 22:29:33.891 EDT).
First capture was 2026-10-15T02:30:37.165Z. At verification the archive held
15 completed public messages (3 user and 12 assistant), totaling 34,584
bytes. All signatures matched the supported source parser, stored-byte and
canonical hashes passed, earlier public messages were an unchanged prefix,
and number, filename, title, creation and first-capture identity were
preserved. Both previous research turns' actual final messages and completion
events were verified. The other eight registered archives were unchanged.

The verification receipt is a point-in-time record. Later legitimate
refreshes change counts and hashes. This handoff turn's unsent final was not
part of that verification; a bounded exact-turn follow-up will capture the
actual final after completion. Do not prewrite planned assistant text into
an archive. Raw source exports remain outside the repository.

Note 26 describes an earlier conversation, number 10, and historical HEAD;
it must not overwrite this chat's identity. A new chat must register its own
actual id and title. Use investigation 21's `chat-histories/` by default for
that new research chat; preserve this chat's explicit formal replay home.
Read repository `AGENTS.md` and `tools/CHAT_HISTORY.md`, refresh at the start
and end of replies, and use the bounded exact-turn completion worker until
native hook activation is verified. Native hooks have not been verified
active in this chat. Record the new chat's actual model and effort rather
than inheriting this note's settings by assumption.

## Platform recommendation

Use **local Codex in the existing RH_Codex project** for the continuation.
The practical advantage is continuity with the current checkout, exact
checks, repository notes, and archival workflow. OpenAI's
[environment guidance](https://learn.chatgpt.com/docs/environments/modes)
describes Local mode as working directly in the current project directory;
a separate cloud environment does not automatically receive local files.

ChatGPT can be useful for a separate conceptual second opinion after being
provided this note and Note 28. The recommendation concerns workflow and
available context, not a claim that a product label establishes stronger
mathematical reasoning. Preserve the local working changes whichever
interface is used.
