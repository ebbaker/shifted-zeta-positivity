# Auxiliary disk and pair coordinates for the conjugate exterior estimate

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance, chat0003 continuation. Fixed execution
dispatch selected **gpt-6.1-sol / ultra**. Separate backend attestation
and actual lead settings are unavailable.

**Geometry acquired pending internal review.** On the same canonical
tube centered at \(a=140101/10\) for \(0\le t\le1/10\), the
auxiliary radius \(8/5\) contains exactly the two zeros already inside
\(3/4\), counted with multiplicity. The moment enclosures pay
\(\lvert c-a\rvert\le7/100\) and \(\lvert D\rvert\le1/5\) on every
time cell. These are the geometry inputs of the frozen conjugate
exterior estimate. The runtime used no values of \(K\), no early positive
gap premise and no new xi evaluations.
[Decision07][decision] · [Frozen E04 r3 request][request] · [Execution record][record]

## Source and two disk errors

The numerical input was the existing fine \(33\times128\) complete-source
array in the same constant gauge \(G_t=e^{\pi a/8}H_t\).
The program verified the original consumer by SHA-256 before loading it.
The consumer verified both the compressed archive and decompressed
content hashes, as well as the fixed grid metadata and shape.
The replay used 224-bit Arb, degree \(32\) in both coordinates and
the same source-lattice allowance as E04 r2.
[Original consumer][original-code] · [Archive guide][archive] · [Record][record]

Execution started after the E03 r5 proof owner confirmed the enlarged
radius formula and the lead relayed that confirmation. With \(S=5\),
\(\rho=9/10\) and \(R=8/5\), the formula uses \(R/\rho=16/9\),
\(R/S=8/25\), \(\rho/S=9/50\) and the time-remainder denominator
\((S-R)^{66}=(17/5)^{66}\). It retains the archive-radius and source
amplification, spatial aliasing and truncation, the time interpolation
operator norm \(65\), and the heat-law time interpolation remainder
for the true field. Every allowance was enclosed at 224 bits. The
output gives \(E(8/5)<7441.88723\), with real-time interpolation
contribution below \(8.731\times10^{-16}\). The smaller
\(E(21/20)<0.03124\) was recomputed with the original formula
and used for the original collar and pair moments.
[Note14 §2][tensor] · [Frozen E03 r5 request][proof-request] · [Record][record]

## Count and coordinates over the full slab

On each circle the code encloses \(P(t,w)/w^2\) at the time and angle
midpoints. It pads the real part by the normalized true-field error
and the time and angular derivative bounds over each entire closed
cell and arc. Conjugation covers the reflected arcs of the true
field. The common sign selected and verified was \(+1\). Both
boundary pairs passed at the first grid, 16 time cells and 64 arcs per
circle. The remaining scheduled refinements were unnecessary.

| Geometry test | Radii | Strict lower bounds for \(\Re(G_t/w^2)\), inner then outer |
| --- | --- | --- |
| Auxiliary disk, with \(E(8/5)\) | \(3/4,\ 8/5\) | \(1{,}047{,}453.80,\ 89{,}911.67\) |
| Original collar, with \(E(21/20)\) | \(3/4,\ 21/20\) | \(1{,}060{,}683.76,\ 1{,}160{,}688.49\) |

The right-half-plane condition gives zero winding for \(G_t/w^2\)
and winding two for \(G_t\) on each circle, uniformly over the slab.
The equal inner and auxiliary counts exclude every additional zero
between these two circles. The original collar pays the principal
log and its 128-point annular trapezoid tails. The same centered
log gives \(c-a=p_1/2\) and \(D=p_2/2-(p_1/2)^2\). The two
annular error allowances are below \(5.014\times10^{-9}\) and
\(1.048\times10^{-8}\), in addition to the complex field/coordinate
interval propagation. The code computes only these two log moments.
All 512 closed time cells give the outward intervals
\[
 c-a\in[0.0594957328,\ 0.0637631130],\qquad
 D\in[0.0007983892,\ 0.1791166200].
\]
The magnitude tests use both extremes of each interval. The
incidental positive lower \(D\) output is available to the same-data
direct comparator and was not used to pass either magnitude gate.
[Note14 §§3–4][tensor] · [Original assessment][assessment] · [Record][record]

## Controls, execution and scope

The exact quadratic \(w^2-2(t-1/20)\) passed both count tests at
the first grid. All 512 moment cells enclosed \(c-a=0\) and the
full linear range of \(D=2(t-1/20)\). Its double occurs at \(1/20\).
Analytically its zero-free factor is constant, so the signed cost
is \(1/5\), the terminal gap is \(1/10\), and the full-slab margin is
\(-1/10\). The geometry correctly accepts the control while its
strict signed passage test fails. The even quartic in the analytical
packet was not a numerical input. The broader source controls retain
the failed or untested premises in the strip source record and
Note12 §6. [E03 r5 request][proof-request] · [Strip source record][strip]
· [Collision controls][controls] · [Note12 §6][source]

The preflight timed two boundary cells and four coordinate cells.
It projected about 7.07 s at the full prescribed caps, including the
canonical and quadratic cases. The complete run took about 0.92 s
under a 60-second wall-clock gate on macOS arm64, Python 3.10.0,
python-flint 0.9.0 and FLINT 3.6.0. No gate failed in the recorded
run. The geometry schedule, benchmark accounting, exact balls,
input hashes and timings are in the small record. The script exits
on a missing or hash-mismatched archive. Replay with the existing
cache location supplied through the archive lookup or
`--cache-dir`, and use `--output` with a new record path.
[Replay code][code] · [Execution record][record]

The run pays precisely the additional geometry required to apply
the conditional conjugate exterior sign argument to this tube.
The frozen \(K\le-59/100\) budget still needs lower mass from
additional identified exterior zeros. Both methods receive the
same source array, strip bound, geometry, moment intervals and
physical pair law. The earlier matched minimum uses the directly
measured endpoint and a tighter interval. [Decision07][decision]
· [Matched minimum][minimum]

[decision]: ../brainstorm/notes/07_VCD_GT_B06_JOINT_CONJUGATE_SOURCE_DECISION_20261116.md
[request]: ../research-progress/handoffs/VCD-GT-E04-r3.md
[proof-request]: ../research-progress/handoffs/VCD-GT-E03-r5.md
[record]: ../numerics/09_VCD_GT_JOINT_STRIP_GEOMETRY_20261116.json
[original-code]: ../numerics/vcd_gt_lehmer_certificate.py
[code]: ../numerics/vcd_gt_joint_strip_geometry.py
[archive]: ../ARCHIVES.md
[tensor]: 14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md
[assessment]: ../reviews/08_VCD_GT_CANONICAL_GAP_CERTIFICATE_ASSESSMENT_20261116.md
[strip]: ../references/03_VCD_GT_STRIP_PRODUCT_SOURCE_USE_20261116.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[source]: 12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md
[minimum]: 19_VCD_GT_E03_MATCHED_GAP_MINIMUM_20261116.md
