# Bounded pilot run plan

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model gpt-6.1-sol (Codex), reasoning effort ultra.

Before execution: fixed t=157/1000, y0²=87677/2500000, N=690988,
P={2,3,5,7,11}. Check only the sharp finite-sum row at y0, using
outward fixed-point arithmetic at 110 bits and 45-digit scalar helpers.
No inference over y or other N is licensed by this pilot. Baseline is the
historical floating sharp value about .00178 at the same point, and the
historical plain row is negative at this lower time. This pilot resolves
whether the sharp point margin survives rigorous arithmetic.

Maximum budget: one full row, one CPU process, 600 seconds, estimated
resident memory below 512 MiB; four small brute-force cases and exact
weight identities first. Abort on hash mismatch, failed small-case check,
invalid scalar range, or error-bound premise failure. No grid expansion
or precision increase on inconclusive output. The separate tail adapter
has its own bounded plan. No multimillion-row producer campaign.

Arithmetic-check amendment before final replay: the first 96.94-second run
produced a positive enclosure. A same-model check identified an unstated
bridge for scalar G^-sigma errors. Replace that bridge with a direct
interval-width bound and rerun the single row once (600-second cap),
retaining the final verified implementation and record. This changes no
mathematical target or sample selection. Peak memory is now recorded and
the wall limit is enforced by an alarm.
