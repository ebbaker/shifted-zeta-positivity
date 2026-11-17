# VCD-GT-E04 r3 — auxiliary geometry return

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance, chat0003 continuation. Fixed execution
dispatch selected **gpt-6.1-sol / ultra**. Separate backend attestation
and actual lead settings are unavailable.

**Geometry acquired pending internal review.** The lead relayed E03 r5's
wider-radius error verification before execution. One run was made
under the [frozen geometry packet][request]. The nine issued input
pins matched before the run. On return the eight other pins matched
and [Decision07's documented rendering correction][correction] accounts
for the single changed digest.

| File | SHA-256 |
| --- | --- |
| Frozen E04 r3 request | 62523e5f3d3ed1fac42dc2c5a68a076a370656fe986d0bbd0afe02ac04a3af02 |
| Decision07 as issued | f20c91a87c5b972cb45b3f7e26dc4a55d5e64499c808d220117b645d7aeaa392 |
| Decision07 after rendering correction | 51f393fb86bce0a279bd7d7faae273bbef0ccba99401b8f46fede06de1b34931 |
| Geometry replay code | 8353074c4db8b15e10fbbafcaaf097b1241d0d27b21a0bfae047323cda154122 |
| Record09 | 43059f2de5b5aa36185dc2d23327ef4830b638da84b05f55a7e880cb2b4b0f07 |
| Note22 | 1e07e07323eac5d0e2e841a5b48f59082cf3cceef44965464a0a8f8c3d252042 |

The wide disk error is \(E(8/5)<7441.88723\). The original collar
uses \(E(21/20)<0.03124\). Both boundary pairs pass with the same
sign on 16 time cells and 64 arcs per boundary. The auxiliary inner and
outer real-part floors exceed \(1{,}047{,}453.80\) and \(89{,}911.67\).
The common winding counts two zeros inside \(3/4\) and those same
two inside \(8/5\) throughout \(0\le t\le1/10\).

The separate original-collar moment calculation completes all 512
closed time cells and gives
\(\lvert c-a\rvert<0.063763113\), \(\lvert D\rvert<0.179116620\).
The latter bounds use both interval extremes. The run uses zero
xi calls, zero drift-kernel evaluations and no early positivity
input. The preflight uses six cells and projects 7.07 s at the cap.
The full run takes 0.92 s. All recorded gates pass. The exact quadratic
passes the geometry and moment controls while its analytic full-slab
signed margin is \(-1/10\). The record balls, outward reported values,
links and hashes were cross-checked without a repeat run.
[Note22][note] · [Replay code][code] · [Record09][record]

The new geometry pays the sufficient inputs of the conjugate exterior
sign estimate on the named tube. The required magnitude remains unpaid.
E05 r8 owns separate internal review of these pinned outputs and
one bounded replay. The [sole register][register] owns status.

[request]: VCD-GT-E04-r3.md
[correction]: VCD-GT-B06-r2-rendering-correction.md
[note]: ../../notes/22_VCD_GT_E04_JOINT_STRIP_GEOMETRY_20261116.md
[code]: ../../numerics/vcd_gt_joint_strip_geometry.py
[record]: ../../numerics/09_VCD_GT_JOINT_STRIP_GEOMETRY_20261116.json
[register]: ../01_VCD_GT_RESEARCH_PROGRESS_20261116.md
