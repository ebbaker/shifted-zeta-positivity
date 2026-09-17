# Along a path the motion is not an endpoint motion: what Proposition 6.1 does and does not say

**Author: Claude Opus 5 (Anthropic).** 17 September 2026. Short note recording a
correction raised by Edward Baker against
[manuscript 0.1](../manuscript.pdf) Section 6 and the readings taken from it in
the [scattering note](SCATTERING_AND_OPEN_WILSON_LINES_20260917.md), Section 2.3.

**The objection is right about the reading and not about the proposition.**
Proposition 6.1 is a partial derivative at fixed $\omega$, and is correct as
stated; the phrase "fixed tail and moving head" describes one direction of the
$(\omega,L)$ plane and does **not** survive to motion along a critical path,
where $\omega$ moves too. Working out what does survive produced an explicit
algebra that was not in the manuscript, and it tightens the proposal's open
question rather than loosening it.

**No manuscript change has been made.** Section 5 lists what this requires.

---

## 0. Summary

1. **Proposition 6.1 stands as a partial derivative.** Its hypothesis fixes
   $f\in C_c^\infty(I_{L_0})$ and $\omega$, and lets $L>L_0$ vary. The whole-line
   transfer $V_\omega$ carries no $L$, which is exactly why the endpoint term is
   the whole of $\partial_L$.
2. **Along a path $t\mapsto(\omega(t),L(t))$ it is not the whole of the motion:**
   \[
    \frac{d}{dt}V_{\omega,L}=\big(\dot L\,B_L-\dot\omega\,G_{\omega,L}\big)V_{\omega,L},
   \]
   and the second term is the full Weil generator --- non-local, carrying the
   prime atoms. So along a critical path the line's head moves *and* the
   connection along the whole line is deformed at the same time. The Wilson-line
   picture of a dragged endpoint is a picture of the $L$-direction alone.
3. **What survives is stronger than the derivative statement.** Proposition 2 of
   the [inner-function note](INNER_FUNCTION_AND_RESONANCE_20260917.md) is not a
   derivative: under RH, $\langle f,D_{\omega,L}f\rangle=\int_{L/2}^\infty|(V_\omega f)|^2$
   at **every** $(\omega,L)$. The defect is a boundary quantity pointwise on the
   whole plane, with no path involved. Only "the *motion* is an endpoint motion"
   was directional, and that is the clause to withdraw.
4. **The algebra, which is new here.** With $B_L=\frac12\delta_{L/2}\otimes\mathrm{ev}_{L/2}$:
   \[
    \partial_\omega B_L=0,\qquad
    G_{\omega,L}B_L=0,\qquad
    [G_{\omega,L},B_L]=-B_LG_{\omega,L}\neq0,
   \]
   and Proposition 6.2's flatness collapses to the explicit identity
   $\partial_LG_{\omega,L}=B_LG_{\omega,L}$. All four verified to machine zero in
   a discretization.
5. **Consequence for the proposal, and it is the useful part.** Remark 4.5 of the
   manuscript asked for non-commutativity transverse to $\omega$. It exists:
   $[G_{\omega,L},B_L]\neq0$, so the $(\omega,L)$ connection is genuinely
   **non-abelian**. But it is flat and the quarter-plane is simply connected, so
   the holonomy is still path-independent. The non-commutativity is present in
   the algebra and absent from the holonomy, and the only two ways it can become
   visible are the ones already on the list: the punctures of Section 6.4, or the
   domain failure of Proposition 6.3.

## 1. What the proposition assumes

Proposition 6.1 fixes $f\in C_c^\infty(I_{L_0})$ and $\omega$, takes $L>L_0$, and
computes
\[
 \frac{\partial}{\partial L}\big(V_{\omega,L}f\big)
 =\tfrac12\,(V_\omega f)(L/2)\,\delta_{L/2},
\]
the trailing term vanishing because $V_\omega$ is causal and $f$ is supported in
$I_{L_0}$. The step that makes the endpoint the *whole* of the variation is that
$V_{\omega,L}=\mathbf 1_{I_L}\cdot(V_\omega f)$ with $V_\omega$ **independent of
$L$**: all of the $L$-dependence sits in the indicator. Nothing in the proof
assumes a path, and nothing in it is affected by one.

The conclusion drawn in the manuscript's abstract --- "the line has a fixed tail
and a moving head" --- is a statement about $\partial_L$. Written without that
qualification it invites the path reading, and under the path reading it is
false.

## 2. Along a path

If $\omega$ and $L$ both move, the chain rule gives
\[
 \frac{d}{dt}V_{\omega(t),L(t)}
 =\dot L\,\partial_LV+\dot\omega\,\partial_\omega V
 =\big(\dot L\,B_L-\dot\omega\,G_{\omega,L}\big)V_{\omega,L},
\]
using Proposition 6.1 for the first term and equation (2.14) for the second. The
two terms are of completely different type: $B_L$ is rank one and supported at a
point, $G_{\omega,L}$ is the full causal generator whose kernel is continuous
plus atoms at $m\log p$. **Endpoint plus bulk.**

This matters for the gauge-theory reading in two ways.

*Against it.* The open Wilson line analogy of the scattering note, Section 2.3 ---
a ray with a pinned end on a defect and a free moving end --- describes $\partial_L$.
Motion along a critical path is not that: it is dragging the endpoint while the
connection along the whole line is simultaneously deformed.

*For it.* That is precisely the two-term structure a deformed Wilson line has in
the first place --- an endpoint term and a shape term. Theorem 4.2 removed the
shape term in the $\omega$-direction alone, by showing that direction is abelian.
The mixed motion puts a second term back, and Section 3 shows it does not commute
with the first.

## 3. The algebra

Write $B_L=\frac12\delta_{L/2}\otimes\mathrm{ev}_{L/2}$, so that
$\partial_LV_{\omega,L}=B_LV_{\omega,L}$.

**(i) $\partial_\omega B_L=0$.** $B_L$ is built from the geometry of the interval
and carries no shift.

**(ii) $G_{\omega,L}B_L=0$, exactly.** $G_{\omega,L}B_Lf$ is a multiple of
$P_L(g_\omega*\delta_{L/2})$, and $(g_\omega*\delta_{L/2})(x)=g_\omega(x-L/2)$
vanishes for $x<L/2$ because $g_\omega$ is causal. So it vanishes on $I_L$ up to a
null set. The endpoint operator injects at the leading edge, and the causal
generator can only transport to the right of it, which is outside the interval.

**(iii) Hence $[G_{\omega,L},B_L]=-B_LG_{\omega,L}$, and it is not zero:**
$B_LG_{\omega,L}f=\frac12(g_\omega*f)(L/2)\,\delta_{L/2}$, the boundary value of
the generated field. The commutator is **one-sided** --- the pair generates a
triangular rather than a commutative algebra.

**(iv) Flatness becomes an identity.** Proposition 6.2 reads
$\partial_\omega B_L+\partial_LG_{\omega,L}+[G_{\omega,L},B_L]=0$; by (i) and
(iii) it collapses to
\[
 \boxed{\ \partial_LG_{\omega,L}=B_LG_{\omega,L}.\ }
\]
This is directly checkable and true: $\partial_L(G_{\omega,L}f)$ is
$\frac12(g_\omega*f)(L/2)\delta_{L/2}$ by the same indicator-differentiation as
Proposition 6.1, which is exactly $B_LG_{\omega,L}f$. So Proposition 6.2 is not
only a formal consequence of equality of mixed partials; it has explicit content,
and the content is that **the generator's own $L$-variation is its boundary
value.** That is a strengthening of the manuscript, not a correction to it.

*Numerical check (scratch, not a registered programme).* On a $400$-point grid
with a causal kernel $e^{-0.7t}\cos(1.3t)$ and a smooth compactly supported
input: $\max|P_LG\delta_{L/2}|=0$; the integrated form of (iv),
$G_{\omega,L'}f-G_{\omega,L}f=\int_L^{L'}B_sG_{\omega,s}f\,ds$, holds with
maximum discrepancy $0$ against a signal of size $1.7\times10^{-1}$; and
$\max|G_{\omega,L}B_Lf|=0$ while the coefficient of $B_LG_{\omega,L}f$ is
$2.0\times10^{-2}$.

## 4. What this does to the open question

Remark 4.5 of the manuscript concluded that the missing non-commutativity must be
supplied **transverse to $\omega$**, and listed the endpoint direction first.
Section 3 settles that sub-question: the transverse non-commutativity **exists**,
$[G_{\omega,L},B_L]=-B_LG_{\omega,L}\neq0$. The $(\omega,L)$ connection is
non-abelian.

It is also flat, and the quarter-plane is simply connected, so the holonomy is
path-independent and the non-abelian structure is invisible in it. That is a
sharper statement of the obstruction than the manuscript had, because it says
exactly what would have to fail for the structure to become visible:

1. **Non-simple-connectivity.** A flat non-abelian connection on a punctured
   domain has non-trivial monodromy. The punctures are the atoms of
   Section 6.4 --- the prime periods. This is now the *only* route by which the
   non-commutativity found in Section 3 can carry information, which raises
   Problem 6.6 from one item on a list to the deciding computation.
2. **Failure of the connection to exist.** Flatness was derived on the core;
   Proposition 6.3 says $B_L$ has no form-bounded closure. Wherever the
   connection genuinely fails to exist, the flatness argument does not apply, and
   the domain failure is exactly where the structure could hide. This links
   Problem 6.5 to Problem 6.6 for the first time: they are not two independent
   loose ends but the two ways a flat non-abelian connection can still have
   holonomy.

That is a better position than before. The proposal's mechanism is no longer
missing; it is present but trivialized by flatness and simple connectivity, and
there are exactly two named ways to untrivialize it.

## 5. Corrections required

Manuscript (none made):

1. **Abstract and Section 6.1.** Qualify "fixed tail and moving head" as a
   statement about $\partial_L$ at fixed $\omega$, and add the chain-rule display
   of Section 2 above with the remark that along a path the motion is endpoint
   plus bulk.
2. **Section 6.2.** Replace the formal proof of Proposition 6.2 with, or add to
   it, the explicit computation of Section 3: $\partial_\omega B_L=0$,
   $G_{\omega,L}B_L=0$, $[G,B_L]=-B_LG$, and flatness as
   $\partial_LG_{\omega,L}=B_LG_{\omega,L}$.
3. **Section 6.4 and Problems 6.5, 6.6.** Add Section 4 above: the transverse
   non-commutativity exists and is trivialized by flatness plus simple
   connectivity, so the punctures and the domain failure are the only two routes,
   and the two problems are linked.
4. **Add the checks of Section 3** to the check programme; they are exact finite
   algebra and belong with the existing ones.

Notes: the scattering note's Section 2.3 should carry the same qualification, and
does after this note is filed.

## 6. Status

- Sections 1 and 2 are elementary and unconditional.
- Section 3's four statements are written computations, all elementary, and are
  verified numerically to machine zero in a discretization. (ii) uses only
  causality of $g_\omega$; it does not use RH.
- Section 4's first route is a standard fact about flat connections on punctured
  domains; its second is an observation about where the flatness derivation
  applies, not a proof that the structure hides there.
- The identity of Section 3(iv) *strengthens* Proposition 6.2; nothing in the
  manuscript is retracted, and the only thing withdrawn is an unqualified phrase
  in the abstract and the corresponding reading in the scattering note.
