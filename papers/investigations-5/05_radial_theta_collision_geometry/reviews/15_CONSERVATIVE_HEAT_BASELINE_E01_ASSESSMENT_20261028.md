# CTF-E01 R1 finite heat measurement assessment

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 chat0009 **Continue conservative theta flow**.

**Status: same-model internal assessment of a completed floating packet.**
The root writer acquired the numerics; two read-only subagents checked
routine tail/control algebra and implementation. This is not independent
specialist review or interval certification.

The [return note][note], [program][code] and [record][record] answer the
issued [CTF-E01 R1 question][packet]: actual finite-time allowances,
informative sampled scales and matched acquisition cost. All 110 F values
and 172 distinct H/M/C/F quantities were acquired at both requested
precisions, with no extra parameter cases or refinement. Counts total
93,552 scalar calls and initial run time 1.78331 seconds. The request's
Note25 hash matches. The fixed cap and source cutoffs were respected.

The spherical coordinate normalization and the factors exp(4u), exp(8u)
for second/fourth spatial moments check. Theta summands are positive on
u>=0. The retained N=6 source has explicit positive tail payments, and
u cutoffs 2 (theta) and 6 (control) have separately derived outer-tail
payments. The bounds use only elementary exponential tangents and a
geometric theta-index ratio. No omitted theta terms were silently set to
zero in the claimed observation.

The exact control H and H_a remain exactly zero in the collision
comparison; quadrature residuals are recorded only as diagnostics. Its
M2 and C values also agree with independent Gaussian generating-function
formulas at the requested absolute tolerance. At a=0 the first component's
derivative vanishes by evenness, and the return does not call that a
collision. Ratios have explicitly named resolved denominators and remain
undefined for exact zero or unresolved observations.

Every finite residual obeys its inherited allowance within the floating
acquisition diagnostics. That is a consistency check of Note25. The new
information is less favorable: the mass-only bound fails to resolve
several small theta H components even at s=256; correction improves the
listed scales but requires M2 and C4. The control's C4 values are thousands,
so the first collision component's next-moment allowance remains larger
than its signal at every listed time. The control satisfies all generic
heat premises and fails only the canonical theta-source premise; diffusion
does not provide a new separating condition. Other controls retain their
inherited scope in [the control register][controls].

Cost accounting includes both precisions, all moments and shared source
setup. Direct runs first with cold source and quadrature caches; additional
heat measurements benefit from those caches. Their incremental cost is
80,376 calls, compared with 13,176 for the direct comparator. The five
heat scales and direct reuse are explicit. Even a single listed scale plus
the stated moments exceeds that direct call count in this implementation.
The control has cheaper analytic direct formulas. No speed advantage,
all-height claim, collision exclusion or new zero-free domain is supported.

Before delivery, code review identified missing C2/C4 acquisition payments
in the displayed allowances and an absent acceptance gate for unresolved
ratio denominators. These reporting issues were corrected from saved raw
values without numerical reintegration. It also identified incomplete
preservation of partial data and overwritten refinement provenance on
future interrupted/refined paths. The delivered program preserves those
raw values and earlier attempts and requires a complete expected grid for
global success flags. No interruption or refinement occurred here; these
paths were checked by reading and are not claimed as run-tested. The
record distinguishes executed and delivered script hashes, keeps the
original scalar observations and acquisition metrics, and identifies its
reporting correction. Initial and final scientific values were compared
without further quadrature.

The precision difference and library quadrature estimates are not rigorous
roundoff or quadrature bounds. Analytic tails are evaluated without
directed rounding. The 1e-12 C target is therefore a floating acceptance
standard, not a certificate. No unresolved case remained under that
standard. The [result index][results], [avoid index][avoid], especially
[scope][scope], [question before numerics][question] and [known-result
checks][known], limit the conclusion to this frozen pilot.

**Disposition:** Complete CTF-E01 R1, retaining unfavorable measurements.
The program's conceptual question remains open. **Next: [B] CTF-B01 —
Astra**, to select a conservative flow/observable contract or record a
scoped failed class. E02 remains gated on that choice. E04 manuscript
integration was not performed as part of this calculation.

[note]: ../notes/27_CONSERVATIVE_HEAT_BASELINE_E01_RETURN_20261028.md
[code]: ../numerics/16_measure_conservative_heat_baseline_20261028.py
[record]: ../numerics/16_CONSERVATIVE_HEAT_BASELINE_MEASUREMENTS_20261028.json
[packet]: ../research-progress/handoffs/CTF-E01_BASELINE_HEAT_MEASUREMENTS_REQUEST_R1_20261028.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[question]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[known]: ../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
