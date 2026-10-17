# Continuation after the height 112 certificate and phase controlled delay

> **Chat-history routing update, 17 October 2026.** Current histories: [Chat 13 — Continue quaternion theta geometry](../chat-histories/0013_2026-10-15T00-47-29Z_continue-quaternion-theta-geometry.json). Use this investigation’s [local registry](../chat-histories/index.json) and [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json) for current numbers and preserved provenance; this supersedes the routing and numbering below. All future investigation 21 chats belong in this investigation’s `chat-histories/` folder.

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model **gpt-6.1-sol**, reasoning effort **ultra**, verified from
this turn's session metadata. This handoff records existing results and
the chat archive; it contains no new research calculation or theorem.

## 1. Start from the saved research and review

The latest research record is
[Note 25](25_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_20261014.md),
reviewed in [Review 19](../reviews/19_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_REVIEW_20261014.md).
Its [validation receipt](../numerics/PHASE_CONTROLLED_CUSP_CONTINUATION_CHECKS_20261014.json)
binds the sources, numerical records, fresh quadrature replays, and
[independent internal review](../reviews/PHASE_CONTROLLED_CUSP_INDEPENDENT_REVIEW_20261014.json).

[Note 24](24_PROPORTIONAL_DELAY_PHASE_OBSTRUCTION_AND_CONTINUATION_20261014.md)
provides the preceding proportional-delay obstruction and exact complex
source polarization. [Note 19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md)
contains the threshold-three outer theorem, maximal arithmetic-block
estimate, staircase entry terms, and independent-coordinate paired forms.
[Note 20](20_EXPLICIT_OUTER_HEIGHT_BOUND_20261014.md) gives the separate
explicit threshold-five height. These results and their qualifications
remain the analytical inputs.

The stable [manuscript](../manuscript/quaternion_theta_geometry.tex) and
its [39-page PDF](../../../../../output/pdf/quaternion_theta_geometry.pdf)
currently integrate Notes 19–22. Notes 24–25 have not been integrated into
that version. The [build record](../manuscript/BUILD_RECORD.json) and
[manuscript handoff](23_MANUSCRIPT_INTEGRATION_AND_CROSS_TIME_CONTINUATION_20261014.md)
identify that source and PDF. The repository HEAD remains
`560684890d84ab2287ae6ddcd69d763a21f8c0f2`; subsequent research is saved as
working-tree files. Preserve those files when resuming. No new manuscript
snapshot, commit, or tag was created during this conversation.

## 2. Current proved domains and their limits

Write \(h_k=\partial_x^kH\), \(E=h_0^2+h_1^2\), and
\(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\), \(j=0,1\).

### Finite physical norm and stationary signs

The combined certificates establish

\[
 0\le t\le\tfrac12,\quad |x|\le112:
 \qquad\sqrt E>10^{-17},\qquad
 h_{j+1}=0\Longrightarrow\mathcal L_j>0\quad(j=0,1).
\]

The newest [104–108](../numerics/FIXED_CUSP_BAND_104_108_20261014.json) and
[108–112](../numerics/FIXED_CUSP_BAND_108_112_20261014.json) bands add
64 closed cells and 128 stationary observations. These are stationary
implications, not a claim that both forms were tested positive at every
nonstationary point. Evenness supplies negative heights for the physical
norm and full Laguerre forms.

### Every earlier time on the new positive-height branches

Fix \(a=\pi/16\), \(b=1/4\), \(\mu=a^2+b^2\), and

\[
 C_k=-h_{k+2}-2ah_{k+1}-\mu h_k.
\]

At every current stationary point in \(104\le x\le112\), for every
\(0\le s\le t\le1/2\), the new certificate proves

\[
 h_j(t,x)C_j(s,x)>0,\qquad
 h_j(t,x)\{C_j(t,x)-C_j(s,x)/2\}>0.                       \tag{1}
\]

The two genuine branches are \(h_1=0\) in \(107<x<108\) and
\(h_2=0\) in \(109<x<110\), uniquely regular at every time, each with
eight closed slabs. The 16 branch/slab cases include both the half-time
and smooth delay rules. Earlier stationarity is never imposed. This
finite delayed-product claim is for the positive heights actually tested;
it is not asserted on all \(|x|\le112\) or reflected with an unchanged
drift parameter.

The proof retains the current and earlier fields' common physical spatial
displacement while independently ranging their time displacements. It
pays both complete source remainders before intersecting with current
stationarity. This removes the eight coarse undecided absorption cases;
those original verdicts remain recorded. The old uniform \(1/9\)
residual-cone test separately remains `INCOMPLETE` on 24 and 16 cells.
Neither kind of unresolved enclosure is a negative physical sign.

### The height-dependent outer delay

For the predetermined rule

\[
 \delta(t,x)=\frac{t}{2(1+t\log(1+x^2))},\quad\tau=t-\delta,
 \quad P_j=h_jC_j(\tau,x),\quad
 Q_j=h_j\{C_j(t,x)-C_j(\tau,x)/2\},
\]

there is a finite **unevaluated** \(X\) such that \(P_j,Q_j>0\) on both
current stationary sets when

\[
 |x|\ge X,\quad0<t\le1/2,\quad
 \theta=t\log\frac{|x|}{4\pi}\ge13/4.
\]

The retained and absorption normalized margins are \(1/8\) and \(1/2\).
The proof bounds the full carrier phase, including the zeta contribution,
and applies the uniform four-jet theorem at both comparison times.
This validates the new comparison in a region where full signs were
already known; it adds no asymptotic sign coverage or evaluated bridge
from 112.

The existing stronger full-sign theorem remains: for every fixed
\(\varepsilon>0\), both Laguerre forms are strictly positive at
sufficiently large height when \(\theta\ge3+\varepsilon\). Its cutoff
is unevaluated. The distinct explicit theorem has threshold five and
\(X_{\rm exp}=4\pi\exp(10^9)\). Neither statement fills the finite
transition or the unbounded inner cusp.

## 3. The next research task

Develop a **signed arithmetic-block estimate for the existing paired
kernel**, combining the current and earlier coefficients before taking
absolute bounds. Another representation alone is not the missing result:
Note 24 already provides the exact complex polarization.

Use the prescribed smooth delay above, fixed \(a=\pi/16\), \(b=1/4\),
and absorption fraction \(\lambda=1/2\) as the starting protocol. On
current \(h_{j+1}(t,x)=0\),

\[
 \mathcal L_j=\mu h_j^2+\tfrac12P_j+Q_j.                 \tag{2}
\]

The preferred target is \(P_j\ge0\), \(Q_j\ge-K_jE\). A combined-loss
variant may instead prescribe
\(P_j\ge-A_jE\), \(Q_j\ge-B_jE\), giving
\(\mathcal L_j\ge-(A_j/2+B_j)E\). All losses must remain locally bounded
through every candidate positive-time collision. Defining them after
observing a quotient by \(E\), or importing a finite norm floor into an
unbounded domain, does not establish that requirement.

For any fixed padding \(\eta>0\), the asymptotic theorem can confine
sufficiently high candidate collisions and nearby predecessor branches
to a moving inner domain below \(\theta<3+\eta\), using a smaller outer
margin first. The corresponding cutoff is still unevaluated. The
finite transition above 112 must be accounted for separately; do not
assert that every remaining finite-height collision already satisfies
\(\theta\le3\).

A concrete continuation should do the following:

1. Declare the positive-height inner domain, delay, block partition, and
   allowable losses before testing their signs. Start from the existing
   full-source kernel with absorption multiplier
   \((u^2-b^2)(1-e^{-\delta z^2}/2)\), \(z=u+ia\).
2. Combine the two times' coefficients at the same physical \(x\), while
   retaining **independent source coordinates and arithmetic indices**
   in the double integral. Keep both Hermitian and bilinear terms, correct
   complex conjugation, staircase entry contributions, all omitted-pair
   sectors, and the moving-delay derivatives.
3. Prove a signed estimate on a declared unbounded inner subdomain, or
   establish a theta-specific obstruction on genuine current stationary
   points there. A new bounded pilot or a control from another source
   class must retain its actual scope.

The finite shared spatial variable is the observation point's Taylor
displacement. It does not identify the two integration coordinates or
justify retaining only equal source indices. The entry phases in Note 19
cancel in physical \(x\), so their terms cannot be assigned a fictitious
oscillatory gain. Pointwise filter identities also do not authorize
freezing \(\delta_t,\delta_x,\delta_{xx}\) during transport.

## 4. Validation and quick restart

The preceding research turn passed **21 exact symbolic checks** and
**1,321 exact finite audit checks**. Fresh 192-bit interval-quadrature
replays of each new band match every saved field after excluding only
`elapsed_seconds`; the independent exact audit is byte-identical on the
same saved inputs. These checks were already completed in that turn and
were not rerun as new research for this archival handoff.

Use [Note 25's reproduction commands](25_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_20261014.md)
and [validation receipt](../numerics/PHASE_CONTROLLED_CUSP_CONTINUATION_CHECKS_20261014.json).
The exact postprocessing needs only Python's standard library; fresh
quadrature additionally needs python-flint 0.9.0. From `numerics/`, quick
replays are:

```sh
python3 check_phase_controlled_delay_identities.py \
  --output /tmp/inv21-phase-controlled-identities.json
python3 audit_fixed_cusp_band_extension.py \
  --record FIXED_CUSP_BAND_104_108_20261014.json \
  --record FIXED_CUSP_BAND_108_112_20261014.json \
  --output /tmp/inv21-cusp-extension-audit.json
```

Keep future research in `notes/`, computations and compact records in
`numerics/`, and assessments in `reviews/`. Follow `LARGE_FILES.md`;
retain all permanent files below 1 MiB, and create no manuscript snapshot
folders. If manuscript integration is requested, preserve the intended
author and LLM acknowledgment and update its source/PDF build record.

## 5. Chat history identity and closeout

This conversation remains uniquely registered in the explicitly required
formal replay lane, with its existing identity:

- Number **10**, title **Continue quaternion theta geometry**.
- Thread `01a13d07-4714-7f83-a8f5-700a61bc5e0e`.
- [Archive](../chat-histories/0013_2026-10-15T00-47-29Z_continue-quaternion-theta-geometry.json).
- [Registry](../chat-histories/index.json).
- Original creation: 15 October 2026, 00:47:29.557 UTC, or 14 October,
  20:47:29.557 America/New_York.
- First capture: 15 October 2026, 00:48:21.483 UTC, or 14 October,
  20:48:21.483 America/New_York.

The [point-in-time history verification receipt](../reviews/CHAT_HISTORY_CONTINUATION_VERIFICATION_20261014.json)
records the refreshed snapshot's actual count, byte size, stored and
canonical hashes, source equality, and unique registration. The shared
history lock and repository helpers verified every completed archived
public message against the source and confirmed that both preceding
research turns' final messages and completion events were recorded.
Original number, filename, title, creation times, first-capture provenance,
and earlier messages are preserved. Raw session exports remain outside
the repository. Commentary is public history; private instructions,
reasoning, tools, and subagent correspondence are excluded.

Current archival turn: `01a13d5a-999a-7210-b6fc-9ac159114c45`.
The snapshot receipt cannot contain this turn's unsent closing reply.
Closeout therefore refreshes completed public text and arranges the
bounded worker for this exact turn, which records the actual final reply
after completion. Later legitimate refreshes may change snapshot hashes
and counts. Native-hook activation remains unverified; continue using
`tools/refresh_chat_history.py` at the start and end of each reply and
its bounded `--after-turn`/`--defer` workflow as documented in
`tools/CHAT_HISTORY.md`. Preserve this registration when resuming.
