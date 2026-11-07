# B02 terminology: two-zero event, local quotient and critical curve

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, actual **gpt-6-astra / max**, verified in current turn metadata; branch chat0004, turn `01a1b35f-4a75-7e93-91df-062718fa6862`. This is a clarification within the existing **[B] TND-O-B02** discussion, not a new research result or route selection.

The author asks about three terms in the preceding reply. The equation numbers below were checked against the current manuscript's build auxiliary file and the corresponding TeX sections. The manuscript and previously hash-bound notes/returns are unchanged.

## 1. Two zeros, one double zero

Manuscript (5.1), p.10, assumes \(h=h_x=0\), \(h_{xx}=a\ne0\). At the event time this is a spatial zero of exact multiplicity two. Two simple real zeros merge into that double zero, as in (5.6). The phrase “double collision” in the manuscript refers to this zero multiplicity; it does not count pairwise encounters. The author's reading of the conditions as a collision of two zeros is correct.

For clearer discussion, use **two-zero collision** or **double-zero event**. Three zeros merging at one point would give a triple zero: \(h=h_x=h_{xx}=0\), \(h_{xxx}\ne0\). Multiple simultaneous pair collisions at distinct locations are another matter. No universal convention for the phrase “double collision” in particle mechanics is being asserted.

## 2. The local energy does not diverge

The preceding reply's phrase **“local energy divergence” was imprecise**. The divergent quantity is the local kinetic-form-to-mass ratio, manuscript (6.4), p.13. The local kinetic form itself tends to zero, as (6.3) states.

The definition at the opening of §6 is
\[
\epsilon=\tau_*-\tau>0,
\]
the time remaining before the event in increasing imaginary time. Equivalently, since \(\lambda=\lambda_0-\tau\), it is \(\lambda-\lambda_*\). It tends to zero from above on the real-pair side. It is not an error term or a separate perturbation parameter.

On the interval \(I_\tau\) between the approaching roots, (6.2)–(6.4) give
\[
M_{\rm loc}=\int_{I_\tau}h^2dx
\sim\frac{16\sqrt2}{15}a^2\epsilon^{5/2}\to0,
\]
\[
T_{\rm loc}=\int_{I_\tau}h_x^2dx
\sim\frac{4\sqrt2}{3}a^2\epsilon^{3/2}\to0,
\qquad
\frac{T_{\rm loc}}{M_{\rm loc}}\sim\frac5{4\epsilon}\to\infty.
\]
Here \(\sim\) means that the ratio of the two displayed positive quantities tends to one. The denominator vanishes faster than the numerator. The quotient can be described as local kinetic form per unit squared-amplitude mass, or a local Rayleigh quotient. The manuscript retains the form-domain qualification. The full-state energy and its normalized version in §4, including (4.4), remain finite and smooth. Note08's exact \(M'=-2T\) additionally identifies the local quotient as half the negative logarithmic mass derivative.

## 3. The critical curve tracks a spatial extremum

Proposition5.1 in §5.2, p.11, defines the local analytic curve \(x_c(\tau)\) by
\[
h_x(\tau,x_c(\tau))=0,\qquad x_c(\tau_*)=x_*.
\]
“Critical” means stationary with respect to the spatial variable \(x\). Because \(h_{xx}(\tau_*,x_*)\ne0\), the implicit-function theorem gives a unique nearby curve. It follows a local minimum when the curvature is positive and a local maximum when it is negative.

The critical value is \(v(\tau)=h(\tau,x_c(\tau))\). Equation (5.3) states
\[
x_c'=-\frac{h_{xxx}}{h_{xx}},\qquad v'=h_{xx},
\]
with the derivatives on the right evaluated along that curve. The first follows by differentiating \(h_x(\tau,x_c(\tau))=0\) and using \(h_{x\tau}=h_{xxx}\); the second follows from the chain rule, \(h_x=0\) there, and \(h_\tau=h_{xx}\). At the collision \(v=0\), while nearby its value is generally nonzero. The extremum can be followed smoothly through the collision even though the two individual zero trajectories have square-root behavior.

For the leading quadratic model in (5.2), \(h=a[(x-x_*)^2/2+\tau-\tau_*]\), the critical curve is simply \(x_c(\tau)=x_*\) and its value is \(v=a(\tau-\tau_*)\). This is a local explanatory model, not a theta computation.

The [research note08](08_TND_O_B02_LOBE_BALANCE_AND_EVENT_COORDINATES_20261106.md) and [continuation09](09_TND_O_B02_DISCUSSION_CONTINUATION_AND_MODEL_CHANGE_20261106.md) keep their mathematical statements and evidence status. **Next: [B] TND-O-B02 — Astra**, further discussion of the event anatomy. No control route, successor E task, model change or manuscript revision is selected here. The existing unique chat0004 archive is preserved; capture uses the repository wrapper.
