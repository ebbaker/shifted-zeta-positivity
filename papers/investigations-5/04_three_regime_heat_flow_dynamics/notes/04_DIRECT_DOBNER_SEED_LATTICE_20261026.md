# Direct canonical seed lattice: removing recurrence for tau >= 32

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.

**Status: proved in-note with separate same-model internal review.**
This acquires canonical seed disks at every point of a vertical lattice
and replaces Note02's large recurrence allowance by a fixed spacing on
each declared family 32<=tau<=C. Its elementary proof is separate from
the [small-time seed family][small], which is needed near tau=0.
The published K_C,y_0(C) remain uninstantiated. No numerical zero bound,
RH improvement or literature priority is asserted.

Read the [result index][results], [avoid index][avoid],
[classification rule][classify] and [control cluster][controls]. The
analytical control screen and regime limitations in [Note03 Section7][small]
apply. See [Review02][review] and the [sole progress register][progress].
The counted gain is seed acquisition and deletion of recurrence in this
budget, not a new proof that negative-time nonreal zeros exist.

## 1. Exactly one seed zero and a uniform boundary floor

Write a=log2, P=2pi/a and

\[
 c_{\tau,k}=-\tau a/4+i(2k+1)\pi/a,
 \qquad D_{\tau,k}=\{|w-c_{\tau,k}|\le1/2\},\quad k\in\mathbb Z.
 \tag{L1}
\]

For every tau>=32 and every k, Z_tau has exactly one zero, counted with
multiplicity, in D_tau,k, and

\[
 \min_{\partial D_{\tau,k}}|Z_\tau|>1/8,\qquad
 Z_\tau(\alpha_\tau)<21/8,\quad
 \alpha_\tau=-\tau a/4-1/2.
 \tag{L2}
\]

Proof: for w=c_tau,k+zeta the n=1,2 terms are exactly
F(zeta)=1-exp(-a zeta). On |zeta|=1/2 the exponential Taylor series gives

\[
 |F|\ge a/2-(e^{a/2}-1-a/2)
       =1+a-\sqrt2>1/4.
 \tag{L3}
\]

The last inequality uses a>2/3 and sqrt2<17/12. The full remaining
series, uniformly on the disk and independently of its imaginary center,
is bounded by

\[
 T_\tau=\sum_{n\ge3} n^{1/2}
       e^{-(\tau/4)\log n\log(n/2)}.
 \tag{L4}
\]

For n=3, log3>1 and log(3/2)>2/5 imply its term is
<(7/4)e^{-16/5}<1/12. The last step follows from e^{16/5}>21,
already given by its Taylor polynomial through degree5. For n>=4,
log(n/2)>=log2>2/3 gives a bound <n^{-9/2}. Hence

\[
 T_\tau<1/12+4^{-9/2}+\int_4^\infty x^{-9/2}\,dx
       =1/12+1/512+1/448<1/8.
 \tag{L5}
\]

The elementary logarithm bounds follow from
log((1+t)/(1-t))=2 sum_{j>=0} t^{2j+1}/(2j+1) at t=1/3,1/2,1/5;
the square-root bounds follow by squaring positive rational numbers.
Only the zero zeta=0 of F lies within radius1/2; its other zeros are
spaced by P. Rouche therefore gives exactly one zero for Z_tau and the
boundary floor >1/4-1/8=1/8. At the left edge
Z_tau(alpha_tau)=1+sqrt2+T_tau<1+17/12+1/8<21/8, proving L2.

The zero count one implies that the seed zero is simple. No finite
truncation, sampled wall, fitted onset or numerical contour is used.

## 2. Direct transport and its complete height allowance

Fix C>=32, 32<=tau<=C and d>0. With the same constants as [Note02][budget],
choose

\[
 Y_{\rm app}=\max\{(126K_C)^5,
                  [20\tau\log_+(48K_C)]^{3/2}\},
 \qquad Y_{\rm map}=4\pi e^{4(1+d)/\tau},
\]
\[
 Y=1+\max\{1,y_0(C),\tau/2,Y_{\rm app},Y_{\rm map}\}.
 \tag{L6}
\]

The field gate is Note02 B3 with W=21/8 and delta=1/8. The mapping
gate follows exactly from alpha_tau in L2. The real-coordinate condition
is automatic: with B=tau a/4+1/2 one has B/C<=a/4+1/(2C)<1, so
Y>=1 implies B<=C Y^{1/4}. All other published domain gates are paid.

Choose the first lattice center y_k=(2k+1)pi/a satisfying y_k-1/2>=Y.
The entire disk then lies at heights between Y and

\[
 U=Y+1+P.
 \tag{L7}
\]

Dobner's normalized field error is <delta/3 on its boundary and the
actual seed wall is >delta. Rouche transfers the one-zero count directly;
there is **no translation-approximation or recurrence error**. The gamma
factor is nonzero high in the upper half-plane. The map J is injective
there since |J'-1|<=1/2 on a convex upper region. Thus the mapped disk
contains exactly one simple zero of xi_{-tau}. Canonical rotation as in
Note02 B10 gives

\[
 \Im z\le-2d,\qquad
 2Y\le\Re z\le2U+\tau\pi/2,
\]
\[
 R_*(\tau)\le
 \left((2U+\tau\pi/2)^2+
  [1+2B+(\tau/2)\log(\sqrt{B^2+U^2}/(2\pi))]^2\right)^{1/2}.
 \tag{L8}
\]

The allowance above the selected starting height is now the fixed
1+2pi/log2, replacing Note02's L_rec plus its disk width. The seed
count, contour floor, strip and scalar-series bound are all acquired.
The remaining uninstantiated quantities are K_C,y_0(C). Holding C fixed
is essential; the imported constants are not declared uniform as
C->infinity. Larger lattice indices also give distinct simple nonreal
zeros after the same paid onset.

## 3. Limits and relation to the small-time continuation

This does not extend the two-term argument to tau->0. Its absolute tail
majorant L4 increases to sum_{n>=3} n^{1/2}=infinity. That is a failure
of this fixed-radius absolute-dominance payment, not a zero-free statement
about Z_tau or an obstruction to another canonical approximation.

The [small-time theorem][small] instead gives an analytical seed family
for all 0<tau<=1 and a uniform double-exponential witness upper envelope.
The intermediate range 1<tau<32 is not quantified by these two notes;
Note02 retains its seed-parameterized budget there. No all-negative-time
uniform constant or new matched fixed-transverse-strip Book bound is
claimed. Positive thresholds and multiple endpoints are compatible with
both constructions.

[small]: 03_SMALL_TIME_CANONICAL_SEEDS_AND_WITNESS_ENVELOPE_20261026.md
[budget]: 02_DOBNER_COMPLETE_CONDITIONAL_BUDGET_20261026.md
[review]: ../reviews/02_DOBNER_CANONICAL_SEED_ACQUISITION_REVIEW_20261026.md
[progress]: ../research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[classify]: ../../../../avoid/01_restating_the_target.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
