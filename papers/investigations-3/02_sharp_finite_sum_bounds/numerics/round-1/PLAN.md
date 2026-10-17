# Fixed candidate tail/error budget pilot

17 October 2026. Prepared for Edward Baker with LLM assistance, Codex research subagent; actual serving model and effort are not exposed in this subagent context.

This plan precedes the reproducible adapter run. Preliminary unretained floating exploration and one preliminary directed trial were already started; this is not a claim that those exploratory choices were preregistered.

Question: at exact t=157/1000, fixed X=6000000185827 and y0²=87677/2500000, do the inherited uniform approximation and OV-free infinite-tail bounds have positive margins without extending the finite index lane beyond N*=3840000?

Fixed candidate list: M=153814 (inherited head, negative control), then M=600000 (larger convolution head). N*=3840000 and M_err=3000 stay fixed; the finite-lane budget uses N0=690988, m0=2000. No row sweep, search or adaptive candidate generation occurs in this adapter. The domain is exact time 157/1000, all N>=N*, y in [sqrt(87677/2500000), sqrt(343/500)], all natural-cutoff x-windows, including seams. The numerical enclosure uses y-box [1872719/10^7,23409/125000] and extended hull [1872719/10^7,8282512/10^7].

Budget per fixed candidate: 120 seconds wall time and 512 MiB peak resident memory; sequential total budget 240 seconds. The adapter aborts after the wall limit and records actual wall/peak memory. A resource overrun invalidates the planned resource gate, even if arithmetic results are available. The source and adapter hashes, exact substitutions, raw gates and selected required gate set are recorded.

The inherited scalar approximation is paid in full. OV is redundant under the exact partition in audit note 4 §3.2; omit it only from the newly stated decisive bound. Apply the proved reverse y-then-N reduction in note 4 §3.5: the contraction A-cap needs its all-N gate only on the y-box, while both error caps still need gates on the full extended hull. Preserve and report the false extended-hull A-cap gate. Historical target/time/floor/regression comparisons are retained as historical outputs, never silently changed to true. New exact target/hull/time gates replace the corresponding historical application-specific gates. No new finite row or full Newman certificate is asserted by this calculation.

Before the fixed candidate run, the adapter replaces the duplicate identical CN.ln(d) evaluations in ln_pair with one evaluation and the identical lower/upper padding. The arithmetic values and bounds are unchanged; the exact splice is recorded with the parameter substitutions. The initial inherited-head run (32.24 s, 146.2 MiB) passed resource gates and failed all three contraction gates, and is rerun under the final adapter for matching provenance.
