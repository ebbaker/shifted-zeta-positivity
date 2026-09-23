# Research avenues after the WZW synthesis

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Status:** research assessment for discussion, with an elementary finite-model derivation. No new xi positivity result, WZW sewing construction, numerical experiment, or independent specialist review is claimed.

The assessment reads the [standalone manuscript](../manuscript.tex), all its sections, the [continuation](CONTINUATION_AFTER_WZW_WRITEUP_20260923.md), the manuscript audit, and the original WZW proposal, completed pilot, arithmetic-source note and their audits linked from [the note index](README.md). The cited literature was checked selectively for the proposed directions; this is not an exhaustive literature or novelty review.

The main gap is a construction connecting a fixed positive physical or canonical state norm to the unweighted causal arithmetic operator. The tensor balance, transported CS metric and arithmetic multiplier currently live in distinct settings. The raw four-point kernel has a specified compact initial limit, and the instantaneous arithmetic logarithmic generator can have negative real part even for a contractive transfer. A next project should address one of these exact gaps.

## 1. Cumulative storage for the arithmetic transfer

This is the preferred next project if the principal objective is arithmetic positivity. Start with the complete transfer or its Cayley transform, specify the state space and input/output maps, and seek an energy identity whose input and output norms are the unweighted L2 norms.

A useful calibration is already available from the polynomial control. For H(p)=p^2+gamma^2, gamma>0,

\[
 K_\omega(p)=\frac{(p-\omega)^2+\gamma^2}{(p+\omega)^2+\gamma^2},
 \qquad
 Z_\omega(p)=\frac{1-K_\omega(p)}{1+K_\omega(p)}
 =\frac{2\omega p}{p^2+\omega^2+\gamma^2}.
\]

Here is an explicit two-state realization, derived algebraically for this assessment. Set beta=sqrt(gamma^2+omega^2),

\[
 A=\begin{pmatrix}0&\beta\\-\beta&0\end{pmatrix},
 \qquad B=\sqrt{2\omega}\binom10.
\]

For a fixed omega, evolve in the causal coordinate r, not in omega:

\[
 \frac{dx}{dr}=(A-BB^*)x+\sqrt2 Bf,
 \qquad g=f-\sqrt2 B^*x,\qquad x(0)=0.
\]

Since A*=-A, direct differentiation gives

\[
 \frac{d}{dr}\|x(r)\|^2=|f(r)|^2-|g(r)|^2.
\]

The zero-state Laplace transfer from f to g is

\[
 1-2B^*(pI-A+BB^*)^{-1}B
 =\frac{p^2-2\omega p+\beta^2}{p^2+2\omega p+\beta^2}=K_\omega(p).
\]

Consequently, on every finite interval,

\[
 \|f\|_{L^2(0,L)}^2-\|g\|_{L^2(0,L)}^2=\|x(L)\|^2\ge0.
\]

At omega=0, B=0 and g=f. This model gives a positive cumulative storage mechanism compatible with the manuscript's negative shift-generator example. Its energy equation concerns the causal coordinate; it imposes no false monotonicity in omega. Finite products can be modeled by cascading such systems. An infinite cascade specified by assumed critical zeros would be conditional on RH and would not solve the arithmetic construction problem.

The substantive next step is to obtain a comparable realization directly from the complete prime/gamma/rational data. The first milestones should remain the continuation note's tests: the full response and strong identity limit for L<log(2), then the first generator delay with coefficient

\[
 -\sqrt2\log(2)\cosh(\omega\log(2))
\]

when the window crosses log(2). Every coupling, endpoint term and stored-energy contribution must enter the balance. The safe estimate ||V_(omega,L)||<=exp(bL) does not supply this balance after removing the weight.

Suzuki's [original canonical-system construction](https://arxiv.org/abs/1204.1827) is an appropriate comparison, but its explicit unconditional range is omega>1. Before developing new machinery, compare the later [Selberg-class construction](https://arxiv.org/abs/1606.05726) and the support-based construction cited in section 3 below. Keep any auxiliary power of the transfer, canonical depth, arithmetic shift, and L2 norm conversion explicit. A construction for a powered transfer is not automatically the required realization for K_omega itself.

**Decision criterion:** obtain a specified state-energy identity for the actual first arithmetic window, or isolate an explicit term preventing it. Another positive kernel defined by assuming the desired contractivity would not meet this criterion.

## 2. WZW sewing with descendants, using the free-fermion description

This is the preferred continuation if the principal objective is to understand the native physical operator. SU(2)_2 has a description by three massless Majorana fermions; see [the WZW TCSA study, Section V](https://arxiv.org/html/1301.0084). This offers a concrete basis for the descendant calculation. Correct sectors, spin structures, boundary-changing spin fields and null-state quotients remain essential; the pilot's spin-1/2 field is not an ordinary fermion insertion.

Begin with H_(0,1/2)=V_(1/2), the existing Cardy labels and the fixed tip normalization. Define the cut-boundary state spaces and the sewing map. Work first with a regulated collar or simple slit. A collar operator exp[-epsilon(L0-h)] on this module is a useful abstract control: it is contractive and tends strongly to identity as epsilon decreases to zero. It is not yet the normalized physical slit operator, and its scalar normalization must be derived from the actual sewing prescription.

The first deliverables are the physical reflected form, identity limit, composition, and agreement with the pilot's primary matrix elements. Low descendant levels can diagnose a proposed prescription, but a fixed finite truncation cannot establish a full-space identity limit or bound; cutoff control must be addressed.

**Decision criterion:** a defined map on the full state space with a controlled pairing, followed by a candidate input/output map to arithmetic L2. Merely increasing the number of conformal blocks does not address this obligation. This project can be valuable physical research even if no arithmetic identification follows.

## 3. Separate unitary boundary response from arithmetic causality

The functional equation gives |K_omega(iy)|=1 almost everywhere. Thus its boundary values define a unitary two-sided Fourier multiplier. This is distinct from the causal inverse Laplace operator defined on a safe right line. A compression of the former is contractive automatically; identifying it with the latter requires a support/analyticity argument.

This distinction is emphasized by [Suzuki, Chains of reproducing kernel Hilbert spaces generated by unimodular functions](https://arxiv.org/html/2012.11121), published in 2025. Its unimodular-function construction makes an isometric involution immediate, while one-sided kernel support is a further condition related to innerness. Its canonical-system theorems also have explicit additional hypotheses. The proposed application here is a comparison of operators and support, not a claim that the paper proves the missing arithmetic positivity.

A bounded diagnostic is to compute both kernels for the existing off-axis quartet

\[
 H_\delta(p)=((p-\delta)^2+\gamma^2)((p+\delta)^2+\gamma^2)
\]

with 0<omega<delta. Compute the contour-residue terms separating safe-line causal inversion from the boundary Fourier inversion and identify the response before the input arrives. Then determine which physical sewing or canonical assumption would exclude those terms. This is a way to expose the exact role of causality in a proposed positive-norm argument.

For xi, whole-half-plane innerness for all positive shifts is already RH-equivalent. Reformulating that condition as absence of response before the input arrives is not itself progress toward a proof. The value of this avenue is a precise acceptance test for the physical operator in section 2, or for an arithmetic storage construction in section 1.

**Decision criterion:** an explicit operator comparison and obstruction term. A positive boundary norm alone is insufficient.

## 4. Test the moving-driver scalar against a sewing anomaly

The pilot's completing-square bound suggests multiplying the amplitude by

\[
 \exp\left[-\frac{\nu}{8}\int_0^T\dot u(t)^2dt\right].
\]

At k=2, nu=1/4. Defining the driver energy I_T(u)=one-half times the integral of dot(u)^2, this equals exp[-I_T/16]. Since the level-2 central charge is c=3/2, it also equals exp[-c I_T/24]. This numerical equality is an algebraic observation, not a derivation of a physical normalization. The equality of these two coefficient expressions does not persist at arbitrary level.

[Wang's published work](https://arxiv.org/abs/1802.01999) relates loop Loewner energy to regularized determinants. The August 2026 preprint [Maibach--Peltola, Universality of the conformal anomaly](https://arxiv.org/abs/2608.23201) describes a relation between sewing cocycles, central charge and loop Loewner energy. Only its stated scope was checked here; its detailed theorem has not been audited for application to this slit.

These sources motivate a test, not an identification: loop energy, finite chordal driver energy, and the normalization of an amplitude versus its squared norm need not agree. Doubling, endpoint coordinates and corner terms can matter. The current normalized correlator cancels the common anomaly factor, so a factor cannot simply be inserted into it.

Specify a separate sewing or partition amplitude and expand about a constant driver, u=epsilon v. Compare its scalar logarithm at order epsilon^2 with -epsilon^2 times the integral of dot(v)^2 divided by 32, retaining all endpoint terms. Agreement would motivate an exact calculation; disagreement would reject this particular explanation without affecting the established pilot.

**Decision criterion:** a derived scalar with the correct sign, coefficient, gluing law and prescribed normalization. Even success would not establish the arithmetic norm dictionary or prime-delay response.

## Suggested order

For arithmetic progress, begin with section 1, using section 3 as a diagnostic of any proposed operator identification. For continued investigation of the physical WZW setting, begin with section 2; use section 4 as a limited normalization test within that work. The oscillator control is small enough to establish the desired form of the energy argument before attempting an infinite-dimensional realization.

The existing 132 controls concern the completed calculations. They do not test these proposed constructions and were not rerun for this discussion. Independent specialist review remains useful, especially for the boundary normalization and sewing interpretation. No manuscript milestone is asserted by this assessment.
