# GNP-RS-B03 next-session authorization

11 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance. The current chat archive records no actual
model or reasoning effort. The configurations below are the author's
selections for the next session.

**Edward Baker authorizes the next session to start GNP-RS-B03 immediately
on GPT-6 Astra at ultra effort and to carry ready follow-on work into
execution.** Use GPT-6.1 Sol at ultra effort for well-defined execution
when the session can select it. This includes useful, independent
calculations or proof checks during B03 and the execution of a sufficiently
specified follow-on task. The session can begin these without waiting
for another handoff or confirmation.

| Work | Model and effort | When to proceed | Deliverable |
| --- | --- | --- | --- |
| **[B] GNP-RS-B03** | **GPT-6 Astra, ultra** | Authorized for the next session | Choose a quantitative signed-log method and justify its route to the existing margin, or record the first unpaid estimate and its scope. |
| **[E] In-scope execution from B03** | **GPT-6.1 Sol, ultra**, when available | Start as soon as the inputs, route, scope and completion test are fixed | Prove or check the specified estimate, or return the first failed step. Record a separate task and its dependency in the live register when it is a follow-on milestone. |

Use a Sol 6.1 ultra subagent when the session supports model-specific
delegation and the work can proceed independently. Astra can continue the
conceptual analysis while Sol works on a fixed subproblem. If Sol 6.1
ultra is unavailable, continue useful in-scope work with the available
configuration and record the actual settings when exposed. Start with
the smallest derivation or check that can change the decision. Give any
computation a defined scope and stopping condition. Report meaningful
progress and significant compute use so Edward can monitor the work.
A newly discovered gap that requires choosing a different mechanism
returns to Astra for a conceptual decision.

## Research starting point

E01 gives \(J_\lambda=I_\lambda-P_{c,\lambda}+O(1/L_X)\) with the explicit
allowance \(C_*/L_X\). E03 proves the exact quadratic-moment limit at
\(c=1\) and the failure of the fixed quadratic-Jensen allowance at
arbitrarily high centers. The next target is an upper bound for
\(I_\lambda-P_{c,\lambda}\) below \(m_*-C_*/L_X\) for every sufficiently
large \(X\), including exceptional centers, on
\(\lambda=c/L_X,\ L_X=\log(X/(4\pi)),\ 1/2\le c\le1\) with
\(d=1/2,\ r=1\). Retain the complete theta field and the exact critical-log
tail. The [E03 return](08_GNP_RS_E03_RETURN_AND_MODEL_CHANGE_20261111.md)
links the proofs and details of the inherited inputs.

A Jensen-gap correction needs a quantitative lower bound on the gap
where it is needed. The shifted-zeta identity needs a coupled estimate
on \(\Delta+\mathcal Z\) with the pole and shifted zeros retained. A direct
logarithmic approach needs a signed estimate with the same every-center
scope. Use the [result index][results], [heat-flow cluster][r11],
[collision controls][controls] and [avoidance index][avoid], especially
[premise screening][a02], [scoped exclusions][a07] and
[separate bounds][a12]. Name the premise each relevant control fails.
Keep the separate parent time-zero, OC and OA work in their own tracks.

Use the [live register][progress] and save proofs, checks and decisions
as they close. Verify the frozen inputs in the E03 record before reuse.
The dated authorization supersedes the routing in Note08 and updates
live navigation. The frozen E03 proof and request remain the source
for its result. Register a new child-only chat in the
[child history folder][history] with its actual identity and record the
actual model and effort where available.

## Prompt for the next session

~~~text
Read notes/09_GNP_RS_B03_NEXT_SESSION_AUTHORIZATION_20261111.md in papers/investigations-5/09_green_potentials_newman_flow/01_riemann_siegel_evolution. Start [B] GNP-RS-B03 now on GPT-6 Astra at ultra effort. I authorize you to proceed with well-defined execution work in the same session using GPT-6.1 Sol at ultra effort where available, including bounded parallel checks and ready follow-on tasks. Continue through the next in-scope task when its inputs and success condition are fixed. Use focused checks and report meaningful progress and significant compute use so I can monitor it.
~~~

[progress]: ../research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md
[history]: ../chat-histories/README.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
