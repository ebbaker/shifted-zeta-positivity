# GNP-RS-E01 r1 — uniform outer Green baseline in a shrinking Newman-time band

11 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Issuing chat0001 has no actual
model/effort recorded in its capture metadata.

**Type E; recommended GPT-6.1 Sol.** The mechanism, source, domain and
proof route have been selected by B01. The remaining work is a bounded
analytical derivation and complete error accounting. No numerical
implementation, experiment or model change is performed by issuing this
request. This revision is frozen; retain it and append a separate return.

**Owner:** [sole GNP-RS register](../01_GNP_RS_RESEARCH_PROGRESS_20261110.md).
**Prerequisite:** [B01 Note01](../../notes/01_GNP_RS_B01_TRANSITION_SCALE_GREEN_BASELINE_20261111.md)
and its [decision](../../brainstorm/notes/02_GNP_RS_B01_DECISION_20261111.md).
Exact local source identities are recorded in the
[B01 input/handoff record](../../numerics/02_GNP_RS_B01_INPUTS_AND_HANDOFF_20261111.json).
Verify those inputs before treating the request as current; report drift.

## Question, fixed objects and domain

Prove the proposed uniform approximation to the **outer part** of the
Green functional, without estimating the sign of its critical-boundary
logarithm. Keep the complete normalized theta source and
\(\partial_\lambda H=-H_{zz}\), strip \(0<\Im z<8\), center \(X+4i\)
and \(K(t)=1/[16\cosh(\pi t/8)]\).

Fix
\[
 L_X=\log(X/(4\pi)),\qquad \lambda=c/L_X,\qquad
 1/2\le c\le1,\qquad X\ge X_*.
\]
All statements must hold for **every** such \(X,c\), not on average
or at selected heights. The time parameter stays fixed across each
spatial integral. Use exactly Note01 (3)'s \(C_-(\lambda,z)\), with
the upper-half-plane logarithm, and define
\[
 V_\lambda=H_\lambda/C_-,\qquad
 I_\lambda(X)=\int_{\mathbb R}K(x-X)
       \log|V_\lambda(x+i0)|\,dx .
\]
The quotient at the single boundary point zero is irrelevant to the
integral; justify its logarithmic integrability. Do not assume a
positive floor for \(H_\lambda\) on the real line.

Set
\[
 P_{c,\lambda}(X)=\sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\log n}
 \frac{n^{-5/2-c/4}}{1+n^{-4}}
 \cos\!\left[\left(\frac X2+\frac{\pi\lambda}{8}\right)\log n\right].
\]

## Required statement and evidence standard

Produce a proof from the named inherited inputs that there are finite
\(C_*,X_*\), independent of \(X,c\) in this domain, such that
\[
 \left|J_{c/L_X}(X)-I_{c/L_X}(X)+P_{c,c/L_X}(X)\right|
 \le C_*/L_X.
 \tag{E01}
\]
Give the dependence of these constants and a finite onset ledger in
terms of inherited fixed-buffer constants. They may remain
numerically unevaluated; do not call them certified or give guessed
values. For the fixed defect margin
\(m_*=\sin(\pi/8)/(2\cosh(\pi/8))\), record the further sufficient
error gate \(L_X>4C_*/m_*\). This does not acquire the main-value bound.

A valid alternative return is a **precise failure of this proposed
derivation**, naming its first unsupported step and what remains true.
Do not silently weaken the uniform quantifiers or switch to an
RH-equivalent premise to obtain completion.

## Four proof groups and complete payments

1. **Normalization and integrability.** Check/reuse Note01's harmonic
   cancellation lemma. Retain both real tails, the upper boundary,
   the center and the integrable logarithmic-square singularity at zero.
   No additional time-zero \(G(X,1)\) correction belongs to this carrier.

2. **Outer field comparison.** Use HDA Ansatz Note04 CS3/CS6 and
   Assessment03, with fixed target buffers \(r=1,b=9\) and all enlarged
   heat buffers/onsets specified in that source. Recenter at each real
   \(x\); do not use a fixed-radius constant on a growing chart. On
   \(|x-X|\le R_X=(32/\pi)\log X\), prove for \(y=4,8\)
   \[
   V_\lambda(x+iy)=
   \zeta\!\left(\frac{1+y}{2}+\frac c4
           -i\left(\frac x2+\frac{\pi\lambda}{8}\right)\right)
    +O(L_X^{-1})
   \]
   uniformly. Start from the complete two-arm finite sum, retain its
   correction and residual, and justify:
   the \(O(\lambda)\) weight removal only in the dominant safe-line sum;
   the reflected full-population bound;
   the RS correction and \(O(x^{-3/4})\) provider remainder;
   the \(O(\lambda(R_X+1)/X)\) center-parameter replacement; and
   uniformity through every fractional cutoff.
   Do not assign the narrower Polymath Theorem 1.3 constants to \(y=4,8\).
   The HDA theorem is the specified wider-strip provider.

3. **Floor, logs and remote boundary.** Use the independent
   \(\sigma\ge5/2\) Euler/Dirichlet floor in Note01 (10), then make the
   normalized field error \(<1/4\) by an explicit eventual gate.
   Transfer only these safe-line logarithms. For \(|x-X|>R_X\), use
   the exact inherited unit-interval bound for \(\log|H_\lambda|\)
   together with the explicit carrier, uniformly for \(0\le\lambda\le1/2\).
   Pay both remote directions, including neighborhoods of zero.
   Establish the intended \(O(X^{-3}\log^2X)\) tail or a stated
   still-sufficient \(o(1/L_X)\) bound. No unbounded Gaussian or
   logarithmic tail may be suppressed by notation.

4. **Prime combination and scope.** Use the parent's exact Fourier
   transform of \(K\) and the absolutely convergent safe-line Euler
   logarithm to obtain the coefficient and phase in \(P\), retaining
   the mass \(1/2\). Combine the finite-window, center and tail payments
   to prove (E01). Include the uniform integer-cutoff prime-tail bound
   \(Q^{-3/2-c/4}/(3/2+c/4)\). State that the critical-line integral
   remains exact and its favorable value unproved.

Point-of-use sources and their hypotheses are mandatory. The inherited
HDA estimates retain their internal-review status; this task is not a
fresh independent verification of their whole proof.

## Work limit, choices and stop rule

One proof/return note in notes/, one same-assistant analytical
self-check in reviews/, one compact input/check record in numerics/,
and at most one bounded correction pass. Routine changes of sufficient
constants, enlarging a finite onset, and partitioning the exact tail
into unit intervals are permitted. No numerical campaign, manuscript,
different carrier/source/clock, changed consumer, higher-order program
or altered time band is authorized.

If the fixed HDA provider, the claimed carrier relation, or a uniform
tail/floor cannot be made to support this statement, stop that dependent
group and return the failure to **B01 revision 2 — Astra**, identifying
the conceptual choice required. A corrected sign or elementary constant
within the same route is ordinary E work. Do not broaden the theorem
to time zero, fixed positive times, shrinking depth or the finite initial
height range.

## Return and continuation

Record actual model/effort when available, input drift, proof status,
all four group dispositions, constants/onsets and the exact remaining
main-value gap. Update the sole register, DRAFT_HISTORY and canonical
parent continuation; keep this issued r1 and the B01 evidence intact.
Follow the control screen and scoped-negative rules in Note01.
Use the existing unique child chat registration or register a new
child-only chat, then refresh and arrange the bounded exact-turn capture.

After a successful E01, the substantive next choice is an independent
signed estimate for \(I_\lambda-P_{c,\lambda}\), not a second derivation
of (E01). Recommend **Astra for that B decision** if a concrete route
is ready to specify. Do not activate it or claim exclusion automatically.
