# E10 — limit of the reduced scalar envelopes

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Requested helper configuration
**gpt-6.1-sol / ultra**. Actual serving model and effort were unavailable.

**Proved in-note for the B04 scalar relaxation.** This is an allowance
test under [Classification01][classification] and [Scope07][scope].
It uses the [frozen request][request], the [pinned B04 decision][b04],
and the [accepted scalar inputs][e05]. Its proof and scope assessment
are by the same helper. [Result index][results] · [Avoid index][avoid]

## 1. Equilibrium and explicit bounds

Use the frozen normalization \(\ell=L^{-1}\), \(m=\ell^2M\),
\(\delta=D/\ell^2\), \(s_p=\ell^{2p}S_p\), \(\tau=\ell^3T_2\).
Dots denote scaled-time derivatives. The four equations of the
relaxation are
\[
 \dot m=2m^2-F,\qquad \dot\delta=2-4m\delta,\qquad
 F=12s_2+16\delta s_3,
\]
\[
 \dot s_2=8ms_2-32s_3+4\delta s_2^2-40\delta s_4+4\tau^2 .
\]
Fix positive \(B,B_2,B_3,B_4,B_\tau,d,K\), and choose
\[
 0<\gamma\le\min\{\sqrt{6B_2},\sqrt{K/2}\},\qquad
 L\ge \max\left\{1,\frac{\gamma^2}{B^2},
     \frac{1}{4d^2\gamma^2},
     \left(\frac{5\gamma^{3/2}}{6\sqrt{2}\,B_\tau}\right)^4
     \right\}.
\]
On any fixed scaled interval of positive length, set all entries
constant with \(h=\gamma\sqrt L\):
\[
 m=-h,\quad \delta=-\frac{1}{2h},\quad s_2=\frac{h^2}{6},
 \quad s_3=s_4=0,\quad \tau=\frac{5h^{3/2}}{6\sqrt2},
 \quad F=2h^2 .
\]
The opposite sign of \(\tau\) also works. The inequalities above give
\(|m|\le BL\), \(|\delta|\le d\), \(|s_p|\le B_pL\) for \(p=2,3,4\),
\(|\tau|\le B_\tau L\), and \(0<F\le KL\). If an additional bound
\(|s_1|=|m|\le B_1L\) is listed, use \(\min(B,B_1)\) in the threshold.
Every derivative and time increment of the displayed data vanishes,
so these data obey any nonnegative upper derivative or time modulus.

Here \(2m^2-F=0\), \(m\delta=1/2\), and \(12s_2+16\delta s_3=2h^2\).
The \(\dot s_2\) terms containing \(s_3,s_4\) vanish. The terms
\(8ms_2\), \(4\delta s_2^2\), and \(4\tau^2\) sum to
\[
 -\frac{4}{3}h^3-\frac{1}{18}h^3+\frac{25}{18}h^3=0.
\]
The adverse Riccati equilibrium holds throughout the interval
and survives any fixed elapsed buffer inside it.

## 2. Exact backward transport and matched comparator

For scaled times \(u<v\), let \(\Delta=v-u\) and
\(W(u,v)=\exp(-4\int_u^v m(r)\,dr)\). The scalar gap equation gives
\[
 W(u,v)\delta(u)
   = \delta(v)-2\int_u^v W(r,v)\,dr .
\]
The direct scalar evaluator receives the same \(m\) and terminal
\(\delta(v)\). Integrating the constant coefficients gives
\[
 W(u,v)=e^{4h\Delta},\qquad
 C(u,v)=2\int_u^v W(r,v)\,dr=\frac{e^{4h\Delta}-1}{2h}.
\]
The physical cost in units of \(D\) is \(\ell^2C(u,v)\).
For the supplied equilibrium the exact margin is
\(\delta(v)-C(u,v)=-W(u,v)/(2h)\). In a genuine application
\(\delta(v)\) is a separately paid anchor. For compatible exact inputs,
margin zero gives \(\delta(u)=0\), and nonnegative margin is equivalent
to \(\delta(u)\ge0\) since \(W>0\). The equilibrium has
\(\delta(v)<0\), outside a class requiring a positive incoming anchor.

The displayed equations and bounds alone permit \((-m)_+=\gamma\sqrt L\).
For fixed \(\Delta>0\) they also permit \(\log W=4\gamma\Delta\sqrt L\)
and \(\log C=4\gamma\Delta\sqrt L-\log(2\gamma\sqrt L)+o(1)\).
They therefore cannot imply uniform \(o(\sqrt L)\) bounds for the
negative side of \(m\), \(\log W\), or \(\log C\) on that class.
This tests the height exponent while leaving the best constants open.
The direct integration has the same multiplier, cost and margin.

## 3. Premise screen and scope

The [E01 premise screen][e01] for [Controls12][controls] carries
forward unchanged. In particular the Euler-factor and smooth
positive-primitive controls change theta arithmetic, the endpoint-defective
weighted-square controls fail the fixed-strip premise, the reflected
super-Gaussian fails the order bound, and the exact-count slices leave
common-time canonical heat evolution unpaid.

The E10 entries are real scalar functions. The test omits the common
complete integer divisor, unchanged theta source, and canonical contour
and Gaussian time equations. The calculation supplies no realization by
zeros, actual exception or counterexample to RH. The positive-anchor
case and estimates using additional signed canonical information
remain outside the exclusion.

[request]: ../research-progress/handoffs/VCD-GT-GR-E10-r1.md
[b04]: ../brainstorm/notes/04_VCD_GT_GR_B04_SCALAR_SUFFICIENCY_TEST_20261117.md
[e05]: ../reviews/03_VCD_GT_GR_E05_INITIAL_PROOFS_ASSESSMENT_20261117.md
[e01]: ../reviews/02_VCD_GT_GR_E01_INPUT_AUDIT_20261117.md#scope-at-the-return-gate
[results]: ../../../../../../result-summaries/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[classification]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
