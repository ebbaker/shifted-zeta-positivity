# MC08 milestone history

Prepared for Edward Baker with substantial LLM assistance; 2 November 2026, actual gpt-6.1-sol / ultra. This concise branch history indexes working source files; no manuscript snapshot folder was created and no commit or tag is claimed.

| Date | Investigation | Source snapshot / commit | Why it matters | Notes and checks |
| --- | --- | --- | --- | --- |
| 2026-11-02 | MC08-E01 r1, open quantum dynamics | [Return01](notes/01_NO_JUMP_ADMISSIBILITY_AUDIT_20261102.md), uncommitted source return | Proves R(v)>=1/8000*(2I-S-S*) for 0<=v<=1/25 directly on the infinite one-particle space; exact bounded no-jump completion. No new signed inequality. | [Exact support](numerics/MC08_E01_EXACT_BOUNDS_20261102.json); limited same-model checking described in Return01; E03 was pending at this milestone; later assessment below. [Continuation](research-progress/handoffs/01_MC08_E01_CONTINUATION_20261102.md). |
| 2026-11-02 | MC08-B01 r1, open quantum dynamics | [Decision02](notes/02_OPEN_SYSTEM_ARCHITECTURE_DECISION_20261102.md) and [E02 r2](research-progress/handoffs/02_MC08_E02_CONSTRUCTION_CONTRACT_R2_20261102.md), uncommitted source artifacts | Freezes quadratic/linear loss, vacuum-count stream, same-number phase readout and a compatible Fock proof route. Construction and E03 were pending at this decision snapshot; no sign gain. | Same-assistant design checks in Decision02; [model-change continuation](research-progress/handoffs/03_MC08_B01_CONTINUATION_20261102.md). |
| 2026-11-02 | MC08-E02 r2 and separate E03 | [Return03](notes/03_FERMIONIC_LINDBLAD_REALIZATION_20261102.md), frozen uncommitted source | Proves complete count instrument, fixed-N Hermitian collision/record error, signed readout and compatible vacuum-Fock extension. No new signed comparison. | [Assessment02](reviews/02_OPEN_QUANTUM_DYNAMICS_ASSESSMENT_20261102.md): accepted at stated scope without correction, separate same-model shared-input review. [Continuation](research-progress/handoffs/04_MC08_E02_E03_CONTINUATION_20261102.md). |
| 2026-11-02 | MC08-B02 signed-comparison decision | [Decision04](notes/04_SIGNED_COMPARISON_DECISION_20261102.md), uncommitted source, SHA256 `55a60e464bc69122f4ad07dd0290d989f6d435eb30abc4ef49902be179172a0f` | Reasoned stop: actual-theta intermediate-cone obstruction and activity/noise ratio cancellation, without endpoint-sign or ratio gain. | [Proof-author check03](reviews/03_MC08_B02_STOP_SELF_CHECK_20261102.md); [E04/model-change handoff05](research-progress/handoffs/05_MC08_B02_DECISION_AND_MODEL_CONTINUATION_20261102.md). |

B01 entry prepared for Edward Baker with substantial LLM assistance, actual **gpt-6-astra / max**, 2 November 2026.

E02 r2 was frozen before execution to compare collision and continuous count instruments in matching time bins; r1 is preserved. No architecture or source change.

E02/E03 milestone entry prepared for Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol / ultra**, 2 November 2026. No manuscript snapshot, commit or tag was created.


B02 milestone prepared for Edward Baker with substantial LLM assistance, actual **gpt-6-astra / xhigh**, 2 November 2026. No manuscript snapshot, commit or tag created.
