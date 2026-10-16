# Prescribed shift evolution, cumulative storage, and a depth--shift continuation

19 September 2026. Prepared for Edward Baker from the discussion of the Wilson--Loewner manuscript and the shared background.

**Model:** OpenAI GPT-6 (Codex). **Reasoning effort:** the configured effort level is not exposed to the assistant in this session; no level is inferred.

**Status:** research-direction note and handoff to the new [critical-path investigation](../../critical-path/). This note organizes inherited identities and proposes a construction target. It establishes no new Wilson realization, contraction theorem, or all-depth positivity result. Numerical values below are quoted from existing records; no numerical experiment was run for this note.

Edward proposes using the boxed operator evolution next to equation (1.7) of the [shared background](../../../background_section.tex) as the prescribed flow, and reconnecting the Wilson construction to the depth--shift continuation developed in the shifted-zeta program. The proposed direction is to realize that exact evolution through a field-dependent boundary observable, explain its cumulative contraction by a positive pairing, and control the enlargement of the boundary interval separately.

## 1. The arithmetic evolution to realize

Use the shared normalization on \(I_L=(-L/2,L/2)\), with ordinary unweighted \(L^2\) norm. To avoid confusing the centered xi function with a zero-extended input, write

\[
H(p)=\xi(\tfrac12+p),\qquad
K_\omega(p)=\frac{H(p-\omega)}{H(p+\omega)},\qquad
a_\omega(p)=\frac{H'(p-\omega)}{H(p-\omega)}
            +\frac{H'(p+\omega)}{H(p+\omega)}.
\]

The operators \(V_{\omega,L}\) and \(G_{\omega,L}\) are the compressed causal realizations of \(K_\omega\) and \(a_\omega\), respectively, using a right-half-plane Laplace line \(\Re p>1\). The target is

\[
\boxed{\partial_\omega V_{\omega,L}
       =-G_{\omega,L}V_{\omega,L},\qquad V_{0,L}=I.}
\tag{1}
\]

This identity is already supplied by the arithmetic family. Finding the equation is not the missing result. The task is to derive an independently specified physical realization that satisfies it and has the required norm property.

The background states the evolution on admissible inputs, with a strong initial limit and a right derivative at zero on smooth compactly supported tests. It does not assert an operator-norm derivative at zero. The generator and its symmetric form must retain their stated domains; formal expressions involving unbounded operators do not replace those conditions.

At zero shift, the generator symbol is explicitly

\[
\begin{aligned}
a_0(p)={}&w_0
+2\int_0^\infty n_\Gamma(u)(1-e^{-pu})\,du
+\frac{2}{p+1/2}+\frac{2}{p-1/2}\\
&-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-p\log n},
\end{aligned}
\tag{2}
\]

where

\[
n_\Gamma(u)=\frac{e^{-u/2}}{1-e^{-2u}},\qquad
w_0=\psi(1/4)-\log\pi<0.
\]

Thus the matching problem includes the fixed local normalization, the gamma difference term, the pole response, and every prime-power delay with its prescribed coefficient and sign. A matching gamma spectrum alone supplies only part of (2). At nonzero shift the generator's prime-power coefficient contains the factor \(\cosh(\omega\log n)\); the finite-shift transfer itself has the fuller multiplicative integer comb described in the parent factorization.

## 2. The positivity to explain is cumulative

Define

\[
D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L},\qquad
Q_{\omega,L}[g]=\Re\langle g,G_{\omega,L}g\rangle.
\]

The second boxed identity next to background equation (1.7) is

\[
\boxed{\partial_\omega D_{\omega,L}
=V_{\omega,L}^*(G_{\omega,L}^*+G_{\omega,L})V_{\omega,L},
\qquad D_{0,L}=0.}
\tag{3}
\]

The right side is interpreted through the quadratic forms and differentiability specified in the background. Consequently,

\[
\begin{aligned}
\langle f,D_{\omega,L}f\rangle
&=2\int_0^\omega Q_{s,L}[V_{s,L}f]\,ds,\\
Q_{0,L}[f]
&=\lim_{\omega\downarrow0}
\frac{\langle f,D_{\omega,L}f\rangle}{2\omega}.
\end{aligned}
\tag{4}
\]

Positivity of every instantaneous form throughout the shift interval is sufficient for contraction. It is stronger than the cumulative condition \(D_{\omega,L}\succeq0\) actually needed. Positivity of the instantaneous form at just one shift is not, by itself, an integrated contraction argument.

The [storage-depth manuscript, Appendix A](../../../../shifted-zeta/storage-depth/manuscript/storage_depth.tex), records a polynomial input at \(L=\log7\), \(\omega=10^{-11}\), with normalized instantaneous energy between \(-2.999\times10^{-27}\) and \(-2.998\times10^{-27}\), but normalized cumulative defect approximately \(8.717034818878969\times10^{-38}>0\). These are inherited finite-input enclosures in that paper's working normalization. They establish neither contraction on every input at that pair nor negativity of the actual evolving integrand at the endpoint: the instantaneous test uses \(f\), whereas the integrand uses \(V_{s,L}f\).

The example motivates retaining the full accumulated response instead of requiring a positive factorization of \(Q_{\omega,L}\) across the entire parameter plane.

## 3. What a Wilson realization would have to do

Ordered Wilson transport obeys a first-order equation \(\partial_tU=\mathcal M_tU\). Equation (1) has the same formal transport structure, with connection \(-G_{\omega,L}\) on the space of boundary inputs. Declaring that operator to be a connection is a formal rewriting, not a field-theoretic construction.

The concrete target is an independently defined, normalized boundary transfer \(\mathcal V_{\omega,L}\), built from fields, endpoint states, a physical adjoint, and a specified family or ensemble of contours, for which

\[
\partial_\omega\mathcal V_{\omega,L}
=-G_{\omega,L}\mathcal V_{\omega,L},\qquad
\mathcal V_{0,L}=I.
\tag{5}
\]

Matching the equation and initial condition must be accompanied by uniqueness in the stated class of causal evolutions before concluding \(\mathcal V=V\).

The [smooth Wilson variation](../sections/05_variation.tex) supplies curvature, scalar-gradient, arclength or tangent-map, and endpoint insertions. Their averaged action must close into the right side of (5). This would generally require field equations, Ward identities, a controlled sector, or another proved reduction. The existing geometry-only obstruction does not exclude such closure, but a common supercharge does not establish it.

At fixed \(L\), if a contour parameter \(t\) is related to the arithmetic shift by \(\omega(t)\), the target reads

\[
\partial_t\mathcal V_{\omega(t),L}
=-\dot\omega(t)G_{\omega(t),L}\mathcal V_{\omega(t),L}.
\tag{6}
\]

Loewner capacity, the arithmetic shift, and boundary support length are distinct parameters until a dictionary is derived. The free fixed-endpoint covariance has no interior shape response; the current nonzero bulk response is only one interacting sector. Completing the endpoint, defect, and junction terms remains relevant as a test of a candidate realization, but the complete response should now be assessed against (5).

## 4. A proposed role for the reflected network

A promising target is a positive amplitude space and a linear map \(\mathcal B_{\omega,L}\) satisfying

\[
\boxed{\|f\|^2
=\|\mathcal V_{\omega,L}f\|^2
+\|\mathcal B_{\omega,L}f\|^2.}
\tag{7}
\]

After exact matching \(\mathcal V=V\), this gives

\[
D_{\omega,L}=\mathcal B_{\omega,L}^*\mathcal B_{\omega,L}\succeq0.
\tag{8}
\]

The reflected Wilson network could be investigated as a construction of the final norm in (7). Its physical adjoint and positive pairing would explain accumulated storage. This is a proposal: the current opposite-ray Gram kernel has not been identified with \(D\), and its positivity alone supplies neither the identity nor the normalization in (7).

The input and output norms must be the fixed arithmetic \(L^2\) norms. A parameter-dependent metric needs its own normalization and transport terms. Defining \(\mathcal B\) as the square root of \(D\) after assuming positivity would not provide an independent explanation. Likewise, a whole-line unitary realization available only under RH cannot serve as the unconditional starting construction.

## 5. The depth--shift target and the meaning of a critical path

The sufficient route stated in background Proposition 1.1 is

\[
L_j\to\infty,\qquad 0<\omega_j\downarrow0,\qquad
\|V_{\omega_j,L_j}\|\le1\quad\text{for every }j.
\tag{9}
\]

For each fixed smaller interval, zero extension and restriction transfer these norm bounds to its inputs. The fixed-test limit in (4) then establishes central positivity there. No rate linking \(L_j\) and \(\omega_j\), uniform positive margin, or smooth curve is required by this implication. The norm bound must hold for every input at each selected pair.

The word *critical* needs care. The [Wilson-lines discussion of the contraction region](../../wilson-lines/sections/07_region.tex) argues that under RH the true contraction region is the entire positive-shift, finite-length quadrant. Its conclusion that there is no nontrivial critical boundary concerns that region. It does not eliminate a constructive continuation schedule for proving bounds that deteriorate with length and shift.

The proposed new investigation should distinguish the true contraction region, the region where instantaneous-generator estimates are available, and the region a particular construction or certificate can control. Here a critical path means a successful continuation of the latter estimates toward (9), not an assumed boundary between true and false contraction.

The existing [adaptive-shift note](../../../../shifted-zeta/storage-depth/archive/background/1-critical_path_research.md) gives one sufficient route. Assuming \(Q_{0,L}\succeq m_LI>0\), define the energy multiplication norm

\[
\kappa_L=\sup_{f\ne0}
\left(\frac{Q_{0,L}[X_Lf]}{Q_{0,L}[f]}\right)^{1/2}.
\]

Here \(X_L=x\) on the centered interval, or \(x-L/2\) in the translated convention. The inherited estimate is

\[
Q_{\omega,L}\succeq\cos(2\omega\kappa_L)Q_{0,L},
\qquad 0\le\omega\kappa_L\le\pi/4.
\tag{10}
\]

Using a proved upper bound on \(\kappa_L\) supplies a sufficient small-shift schedule. It presupposes central positivity and therefore does not solve its spatial extension. The main storage-depth certificates take that central-extension route; the direct cumulative continuation remains a proposed alternative.

There is also an unconditional anchor at \(\omega=1/2\): the shifted quotient is inner, so its causal realization gives finite-window contractions. See [Suzuki (2012), section 1.4](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/bessatsu/open/B34/pdf/B34_023.pdf). Moving inward to smaller shifts is not justified by reversing a forward dissipation inequality. No bounded inverse of the positive-shift finite-window transfer is assumed.

## 6. Increasing the interval requires a gluing law

Equation (1) holds at fixed \(L\). Along a path with changing length, the input space and compression change as well. The fixed-window shift equation alone is not the full path derivative. A fixed-space identification would introduce additional length-variation terms; a finite spatial extension avoids assuming those derivatives exist.

Translate the interval to \((0,L+h)\) and split it into old and added pieces. Causality gives

\[
V_{\omega,L+h}=\begin{pmatrix}X&0\\Y&Z\end{pmatrix},
\quad X=V_{\omega,L},\quad Z=V_{\omega,h}.
\]

Suppose \(X\) and \(Z\) are strict contractions in operator norm. Put

\[
E=I-X^*X,\qquad F_{\mathrm{out}}=I-ZZ^*.
\]

The Schur complement of the new-input block of \(I-V^*V\) is

\[
S=E-Y^*F_{\mathrm{out}}^{-1}Y.
\]

Indeed the lower diagonal block is \(I-Z^*Z\), and
\(I+Z(I-Z^*Z)^{-1}Z^*=(I-ZZ^*)^{-1}\). Therefore

\[
\boxed{\|V_{\omega,L+h}\|\le1
\iff Y^*F_{\mathrm{out}}^{-1}Y\preceq E
\iff\|F_{\mathrm{out}}^{-1/2}YE^{-1/2}\|\le1.}
\tag{11}
\]

The strict inequality gives a strict contraction. The diagonal strictness is essential for the displayed inverses; a semidefinite extension requires a separate range-compatible formulation.

This is an inherited identity from the [cumulative-storage note](../../../../shifted-zeta/storage-depth/archive/background/2-cumulative_storage_path.md), not a new theorem of this proposal. It identifies the quantity a physical gluing construction should control: cross-interval transfer measured in the actual old-input and new-output defect metrics. Separate scalar lower bounds may lose the cancellations and directional information that matter.

The same source supplies a finite-step criterion allowing both length and shift to change. Its Cayley coordinate

\[
P_{\omega,L}=\frac2\omega\Re\big[(I-V_{\omega,L})(I+V_{\omega,L})^{-1}\big]
\]

obeys

\[
D_{\omega,L}=\frac\omega2(I+V_{\omega,L}^*)P_{\omega,L}(I+V_{\omega,L}).
\tag{12}
\]

It preserves the normalized spatial coupling and is compatible with reflection. Small-shift expansions in this coordinate must retain their core or finite-dimensional scope: \(P_{\omega,L}\) is bounded for positive shift, whereas the central Weil form is unbounded. There is no automatic uniform operator-norm approximation to the central form.

A successful recursion must prove that its increments satisfy \(\sum_jh_j=\infty\). Local extendibility does not exclude an accumulation at finite length. Arithmetic thresholds and possible crossings of weak directions also favor a finite-step criterion over an assumed smooth critical-curve ODE.

## 7. Proposed first work in critical-path

1. **Specify the exact physical transfer.** Define its input/output spaces, endpoint and reference states, regulator, adjoint, normalization, and shift parameter. State the candidate equation (5) before selecting a contour law.
2. **Test the insertion identity.** Use the Wilson variation to calculate the effective generator on a controlled sector, including the endpoint terms. Identify which of the four components in (2) have actually been obtained. Keep a missing arithmetic component explicit.
3. **Test cumulative storage.** Investigate whether the ordinary reflected network yields an amplitude map satisfying (7), or an exact cross-interval inequality of the form (11). A positive free kernel can be a control but is not the target identity.
4. **Carry out one joint continuation step.** Use the existing storage criteria and the [parent Loewner assembly](../../loewner/numerics/README.md) to diagnose a proposed length/shift update. Reuse its transfer, defect, and Cayley constructions rather than rebuilding them. Track complete outputs and an analytic complement bound before interpreting a finite matrix as an operator estimate.
5. **State the all-depth invariant.** Record the data that survive each step, the allowed changes in shift and length, and what prevents finite-length accumulation. A numerical sequence without this control remains exploratory.

The first deliverable should be a precise target-and-obligations document, followed by a narrowly specified calculation. The current Wilson--Loewner manuscript and its historical snapshots remain the record of the contour and field calculations already completed. This note supplies the conceptual handoff; it does not populate the new investigation or revise the manuscript's mathematical claims.
