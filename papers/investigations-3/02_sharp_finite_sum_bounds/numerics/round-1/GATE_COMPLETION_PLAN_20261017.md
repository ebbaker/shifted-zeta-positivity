# Bounded completion of the remaining largest leg sectors

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol (Codex), reasoning effort ultra.

The first fixed pass certified legs 3,2,1 in full. Leg 0 reached its
30000-box cap after completely covering patterns 0..171; it left pattern
172 partly evaluated and patterns 173..242 unopened. There were no
unresolved depth-limit leaves. This is a resource stop, not a failed gate.
The first record and code are preserved unchanged.

This second, fixed pass starts at pattern 172 and checks its full original
root again, then patterns 173..242. It does not reuse the partly completed
pattern 172. The per-pass limits remain 45 seconds, 30000 boxes, depth 36,
40-digit arithmetic, memory 512 MiB. No precision or target change occurs.
If this pass remains incomplete, report its missing sectors and stop;
no third completion run is planned. No finite-row sweep is performed.

The wrapper hash-pins the original code and first execution record,
requires the recorded completed prefix to be exactly 0..171 and its
unresolved-depth count to be zero, verifies the other three legs passed,
and creates the original 243 patterns before selecting the fixed suffix.
Completion is accepted only if every suffix pattern finishes without
unresolved leaves. The combined certificate is the union of the complete
prefix and suffix, together with the three complete smaller legs. It does
not infer coverage from accepted-leaf hashes or sampled values.
