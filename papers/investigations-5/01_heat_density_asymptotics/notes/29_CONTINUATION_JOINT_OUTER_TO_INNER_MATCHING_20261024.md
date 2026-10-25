# Next-session continuation: joint outer bounds toward inner matching

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from chat 0006's session metadata.

**Recommended next task: Analytical — Astra, continuing HDA-19.**
Improve the time-dependent outer field estimate by a complex-contour or
saddle argument and identify its actual joint validity range. The current
range is unbounded in time but does not overlap the inner clock. There
is no pending numerical packet or Sol assignment. This is a manual
handoff for the author; it dispatches no chat or agent.

This is the current new-session entry note, superseding [Note 24][n24]'s
entry instructions while preserving its historical priority decisions.
Use the **live** [progress register][progress] if further work has occurred.
HDA-19 remains Partial; HDA-18 is Gated; HDA-20 has no independent review.

## 1. Workspace, instructions and chat provenance

Work in `/Users/ebbaker/Documents/shifted-zeta-positivity`, investigation
`papers/investigations-5/01_heat_density_asymptotics`. The ChatGPT mirror
and its synced `sources/` are reference material; do not edit them.
Read the repository [AGENTS.md][agents], [GPT workflow][workflow],
[large-file policy][large], [reference workflow][ref-workflow] and
[chat-history procedure][history-tool]. Preserve existing working-tree
changes; Notes 25--28 and their reviews were not committed by this chat.
No manuscript snapshots were created.

Astra owns analytical derivations and interpretation. Sol owns **all**
numerical implementation/execution, including quick exact-arithmetic or
machine-symbolic checks. Ordinary file editing, hashes and chat capture
are housekeeping. Do not create numerical work merely to alternate models.
The author manages chats and selects the actual model/effort. Verify and
record the next session's actual metadata; do not copy this note's model
label as evidence of what ran.

Chat 0006, **Continue infinite-height analysis**, has thread id
`01a1704b-7af1-7931-a76c-38f570b1aeef` and its sole registration in this
investigation's [chat-histories][histories]. Refresh that history only if
continuing that actual chat. A new session/chat must register its own
actual thread id, title, source transcript and unique archive identity;
do not reuse 0006's id or manually assign its number. Use the authorized
refresh tool at the start and end of replies, including the bounded
exact-turn final capture until trusted native activation is verified.
Do not hand-edit generated transcripts or their registry.

End every research reply with **Analytical — Astra** or **Numerics — Sol**,
a concrete next deliverable and a reason. For a numerical handoff, first
write a bounded request packet under the existing progress/handoffs
folder and link it in the sole register. No such packet is waiting now.

## 2. Focused reading order

1. The [live progress register][progress], current owner and HDA-16--20,
   then the [overview][overview], which owns the objective and equations.
2. [Result index][results], [heat-flow cluster][geometry], [collision
   controls][controls] and [avoid index][avoid], especially [classification][a01],
   [cancellation][a12], [scope][a07] and [numerics before a question][a10].
3. [Note 28][n28], JT1--JT21 and JT34--JT36: current model, time-dependent
   field budget, arbitrary-positive-q transfer, static potential jets,
   global-regulator bounds and exact model heat residual.
4. [Note 28][n28], JT22--JT33: regulator layer, exact implicit center and
   width. Read [Review 11][review11] for the same-assistant audit and limits.
5. [Note 27][n27], Sections 2--4 and GO30: complete convolution split,
   gamma phase, physical collars and exact five-term periodization.
6. [Note 19][n19], SC1--SC4 and its complete-source estimates: the existing
   inner domain and absolute error. [Note 14][n14], VE15--VE18, gives the
   adaptive weak identities; [Note 20][n20], FB1--FB2, fixes the regulator.
7. [Note 25][n25] and [Note 26][n26] only as needed for the pre-switch
   tails, scoped finite-cutoff failure and negative endpoint system.

The [reference catalog][refs] records inspected primary sections and
reading-copy provenance. Polymath's exact Gaussian convolution (35)
holds for every positive time; its separate small-time high-zero theorem
is not an automatic input at the times here. The DLMF sectorial bounds
are standard inputs. No independent specialist review exists.

## 3. Keep the objective and exact conventions

The goal is a relatively simple approximation to the **unnormalized**
averaged canonical density, eventually with all-time/all-height control,
correct adaptive evolution, fluctuations and boundary/source data.
Height is real x in z=x+iy. Use fixed positive spatial widths for the
current results; moving widths or time averaging need new budgets.

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\quad H_t=-H_{zz},
\qquad R_H=K*\frac{q|H_z|^2}{\pi(|H|^2+q)^2},\quad q=\epsilon_g^2.
\]

The global regulator is time-only below 64, interpolates smoothly to
`M_0 kappa^-1 exp(-x^2/(2kappa))` on 64<t<128, and equals that formula
above 128. These switch points are definitions, not certified theorem
onsets. Retain actual covariance Q, regulator forcing, spatial curvature
and current source, including both derivatives of the filtered curvature.
No covariance may be chosen simply to make an equation true.

## 4. Current mathematical gains and exact limitations

| Result | What is available | What is not supplied |
| --- | --- | --- |
| Note 25 | Complete-source exponential jet/observable tails on compact slabs ending at 64; scoped positive-cutoff potential obstruction above 64 | Not a density-only impossibility theorem or an exclusion of noncompact representations |
| Note 26 | All-real-height negative endpoint density/current/time/potential and actual Q/Delta Q comparison on its declared transverse scale | Positive full-system budgets |
| Note 27 | Two-gamma relative field estimate, physical simple collars, finite-phase outer density O(log^2 X/X) for each compact interval strictly above 64 | No uniformity across the switch when replacing density by the real zero measure |
| Note 28, JT4--JT5 | Density of the explicit two-gamma field with the exact same q: O(log^2 X/X) on each compact [32,T], including 64; O(X^-3/4(1+log^4 X)) on 32<=t<=(log X)/4 | No all-height positive-time theorem or inner overlap; fixed spatial averaging remains in this explicit model |
| Note 28, JT18a | Physical averaged potential and filtered w, spatial jets through order four, at the same field-error rate | No time jets, current or unfiltered gradient-product/covariance comparison |
| Note 28, JT22--JT33 | O(1) absolute coarse layer profile; O(1/log X) normalized resolved switching law, with location and width | No use of a coarse center in a much finer layer; no numerical center or onset certificate |
| Note 28, JT34--JT36 | Exact heat residual of the gamma model and its field-level bound | The model is not an exact heat solution; no propagation/evolution theorem follows just from that residual |

Every new proof is in-note and same-assistant reviewed. The maintained
manuscript still reflects the Note 23 integration; Notes 25--28 have not
yet been integrated or rebuilt. HDA-15's 192-cell trial remains rejected,
with its arithmetic/filtering failures preserved. HDA-17 has no newly
accepted finite-transition representation. Do not restart that numerical
trial without a specific analytical consumer and bounded question.

## 5. Formulas to resume from

Use the exact factor, not the inner saddle mass or Polymath's Stirling M_0:

\[
\mathcal M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\quad
\alpha=\mathcal M'/\mathcal M,\quad
\mathcal G_t=\mathcal M e^{t\alpha^2/4},\quad
P(t,z)=\mathcal G_t((1+iz)/2)+\mathcal G_t((1-iz)/2).
\]

The exact source representation is

\[
H(t,z)=\frac1{\sqrt{\pi t}}\int_{\mathbb R}e^{-v^2/t}
\frac{\xi((1+iz)/2+v)}8\,dv.
\]

The current relative error budget is JT11. Its leading loss is

\[
\frac{e^t(t+t^2\log^2X)}X,
\]

from integrating absolute values before comparison with the complex
Gaussian. The actual factor before the conservative simplification is
`exp(t (Im alpha)^2/4)`. The arithmetic, bounded middle, missing Gaussian
portion and infinite tails have separate payments in the same note.
Retain those pieces when changing contours; they cannot be reclassified
as zero merely because one saddle contribution is better controlled.

The local transfer lemma JT14--JT18 uses analytic units and simple
collars to compare `log(|F|^2+q)` and `q/(|F|^2+q)` in L1 for arbitrary
positive q. Its planar 1/r translation integral is independent of a
regulator floor. This is ready for reuse if the new field estimate
supplies the same controlled collars. It is not a theorem through a
multiple-root event.

For the switch, set

\[
A_X=|\mathcal G_t((1+iX)/2)|,\quad
\omega=\tfrac12\Re[\alpha+(t/2)\alpha\alpha']((1+iX)/2),\quad
b=\log(\epsilon_g/A_X),\quad d=b_+/\omega.
\]

The coarse profile is
`omega[k_h(y-d)+k_h(y+d)]/(2pi)`. Its implicit center is the unique
near-64 solution b(t_c,X)=0. With kappa_0=kappa(64),

\[
t_c-64=\frac{64}{\log X+\log(4e/(\pi\kappa_0))+O(1/\log X)}.
\]

At `t=t_c-128 tau/(pi X log X)`, the normalized density tends to
`[k_h(y-tau_+)+k_h(y+tau_+)]/(8pi)` with O(1/log X) error on bounded
tau and y ranges. These off-axis layers are regularized density, not
nonreal zeros. **The exact center must be retained:** the omitted error
in the inverse-logarithm location formula is much larger than the layer
width `1/(X log X)`.

## 6. Next analytical deliverable and acceptance tests

Begin with HDA-19, phase ANALYSIS, preserving the register as the sole
ledger. Investigate a complex shift or saddle for the complete convolution
that avoids the absolute Gaussian loss. The point is an improved **proved
joint range**, not a more elaborate representation of the same bound.

A candidate route is to shift the two reflected arms toward their complex
Gaussian saddles or to choose the saddle of the full gamma exponent.
This is a suggestion, not an established contour deformation. Work from
the entire xi convolution where appropriate; separate gamma factors and
arithmetic expansions have their own analyticity restrictions. Pay all
connecting contours, endpoints, poles if encountered, and arithmetic
remainders. A parameter-dependent sector must retain its actual margin.

The deliverable should state:

1. The representation and domain, including t, X, transverse buffer and
   every contour, with the unchanged canonical source and regulator.
2. A relative holomorphic field error with constants whose time dependence
   is visible, and the conditions under which it tends to zero.
3. Actual collar data or another complete route to observable comparison;
   reuse JT14--JT21 only where their hypotheses have been proved.
4. The resulting joint threshold X_out(t), compared with the **proved**
   inner window X_in(t) of order kappa^(1/3). State explicitly whether
   their validity sets intersect with the necessary buffers.
5. If they do not intersect, identify the intermediate regime and the
   missing estimate. Do not claim an obstruction to all representations
   from failure of this particular contour or bound.

The present outer condition X>=exp(4t) and inner polynomial window do
not overlap. Even replacing the exponential threshold by a polynomial
one would not automatically pay the gap. A contour failure or a still
nonoverlapping improved range is a valid scoped outcome if its proof and
next missing estimate are recorded honestly.

Then address the positive current/time/potential-time/actual covariance
budgets under HDA-16, or prepare a bounded Sol request only if a definite
finite computation changes the analytical decision. Do not infer those
budgets by differentiating the static density error. Preserve the exact
model heat residual and all adaptive terms.

## 7. Recording and end-of-session requirements

Save the next derivation in this investigation's notes, its assessment in
reviews, and any authorized numerical packet/results in the established
folders. Include Edward Baker, substantial LLM assistance, date and the
actual model/effort. Update the existing overview and sole progress
register, linking the new evidence without upgrading Partial to Complete
unless all of its acceptance obligations are met.

Keep milestone history concise and create no manuscript snapshot. Record
references when inspected; reuse existing PDF provenance. Preserve the
collision-control screen: the source-specific gamma/zeta/reflection
premises distinguish this approximation, while the general local
regulator lemma is not an exclusion principle. Review status remains
same-assistant unless a genuinely distinct reviewer is involved.

Finish with the saved result, its material limitations, and a next-model
recommendation. If the work remains analytical, recommend **Analytical —
Astra** with its missing estimate. Recommend **Numerics — Sol** only with
a specific question and bounded packet. Refresh the actual chat history
and arrange capture of the real final reply as documented.

[n24]: 24_CONTINUATION_FOR_GPT_ASTRA_INFINITE_HEIGHT_ANALYSIS_20261024.md
[n28]: 28_JOINT_OUTER_REGULATOR_TRANSFER_AND_SWITCH_LAYER_20261024.md
[n27]: 27_COMPACT_TIME_GAMMA_OUTER_DENSITY_20261024.md
[n26]: 26_NEGATIVE_ENDPOINT_EVOLUTION_AND_COVARIANCE_20261024.md
[n25]: 25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md
[n20]: 20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[n19]: 19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md
[n14]: 14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md
[review11]: ../reviews/11_JOINT_OUTER_AND_SWITCH_LAYER_SELF_REVIEW_20261024.md
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[overview]: ../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md
[refs]: ../references/README.md
[histories]: ../chat-histories/README.md
[agents]: ../../../../AGENTS.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[large]: ../../../../LARGE_FILES.md
[ref-workflow]: ../../../../REFERENCE_WORKFLOW.md
[history-tool]: ../../../../tools/CHAT_HISTORY.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
