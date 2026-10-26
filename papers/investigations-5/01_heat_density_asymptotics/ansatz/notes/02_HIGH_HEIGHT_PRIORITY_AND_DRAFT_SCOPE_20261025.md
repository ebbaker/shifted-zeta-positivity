# High-height priority, manuscript scope and next-chat specification

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.
Chat0022, thread 01a17572-5411-7f32-9a12-7d1ba46ad679.

## Author's decision

The author prioritized ansatz 4 and other high-height formulas, with
large height understood for **all times**, accurate asymptotics and
piecewise formulas around transitions. The requested artifacts are a
manuscript draft, research overview, corresponding progress document
and next-chat handoff within the ansatz folder.

The [maintained draft](../manuscript/main.tex) contains the entire
earlier formula catalogue, with most of the main argument devoted to
high height. [Overview](../research-overview/01_HIGH_HEIGHT_ANSATZ_RESEARCH_OVERVIEW_20261025.md)
and [progress](../research-progress/01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md)
own the new branch's scope and live tasks. Parent statuses and the
separate weak-filter cost queue are preserved.

## Analytical checks and distinctions made in this draft

The elementary positive-time cosine's factor pi^(1/4)/16 is a
full-cosine amplitude; the exact gamma arm has leading coefficient
pi^(1/4)/32. Its phase constant is 7pi/8. The deformation contributes
t(ell²-pi²/4)/16 to the log amplitude and pi t ell/16 to the phase.
The leading reduction is justified from the existing compact-positive
linear comparison, retaining that input's in-manuscript status.

The original t>=32 input is not evidence of a physical threshold at32.
Polymath's explicitly inspected small-positive-time domain is
0<t<=1/2, 0<=y<=1, X>=200, and its eventual two-carrier asymptotics
have a t-dependent large onset. A complete joining argument and
uniform extension toward0 are new tasks.

At t=0 the classical Riemann–Siegel sum supplies a real-axis value
anchor with all modes through floor(sqrt(X/(4pi))). The sign follows
from s(s-1)<0 and adding pi to the usual Hardy phase. Retaining these
modes leads to the candidate weights

    n^(-1/2) exp{t[(log n)^2-ell log n]/4}

and phase shifts -(X/2+pi t/8)log n. The candidate coordinate
tau=t ell follows for each fixed mode. The growing cutoff population,
correction term and full complex/time derivatives remain unpaid.
No universal transition constant or single-variable limiting profile
is asserted.

The exact negative-time Gaussian smoothing identity is recorded and
derived directly from the source. A positive-time remainder is not
continued to negative time. Large negative time and large height at
fixed negative time are distinct limits; the parent absolute density
estimate cannot establish a carrier-relative field approximation.

The arithmetic crossover near0 and the regulator layer near64 are
different. The latter retains the exact one-arm amplitude and center.
Its location shift is of order 1/log X, its rounding width of order
1/(X log X), and its inherited absolute density allowance is O(1).
A factor two in amplitude matters for refined recentering even when
it does not alter the coarse normalized leading layer.

The draft records a formal gamma-curvature correction as a checkpoint
for the next chat. It is not a proved second-order expansion. Arithmetic
remainders can be larger than a proposed 1/X correction and must enter
the ordering decision.

## Production and research status

No numerical, exact-arithmetic or machine-symbolic research was executed.
The [production assessment](../reviews/01_OPENING_MANUSCRIPT_PRODUCTION_ASSESSMENT_20261025.md)
records actual compilation and rendering checks. Those checks do not
constitute independent mathematical review. The maintained source and
small build record stay in the ansatz folder; the generated PDF is in
the ignored repository output/pdf tree under LARGE_FILES.md.

This is an opening program draft, not a mathematical acceptance
milestone or a new result-summary promotion. Existing Note01 remains
historical; its core-first recommendation is superseded for this
branch by the author's high-height priority.

Next **Analysis — Sol**:
[HDA-A01-AN01 r1](../research-progress/handoffs/HDA-A01-AN01.md), outer
calibration and one bounded signed-time arithmetic bridge. The earlier
core packet is retained without execution.
