# From the growing-trace hierarchy to a functional equation and arithmetic matching

21 September 2026. Prepared for Edward Baker.

**Model:** GPT-6 (Codex; developer-provided identity).
**Effort:** not exposed in this session; not inferred.
**Status:** research assessment and proposed next calculation. The source-functional packaging below is a conditional algebraic identity. No new Yang--Mills closure, continuum construction, arithmetic realization, or positivity theorem is claimed. Prepared with LLM assistance.

## 1. What the current plan actually establishes

The [genuine-trace note](GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md), especially Sections 4 and 7, derives two evolution equations in a fixed interacting theory. The [handoff](RESEARCH_CONTINUATION_AFTER_GROWING_TRACE_20260921.md), lines 93--117, proposes applying finite-regulator Schwinger--Dyson identities to the derivative moment. The live [outlook](../sections/10_outlook.tex) explicitly leaves arithmetic matching until a useful physical evolution and boundary construction have been found.

Thus there is a concrete physical next step, but no completed mechanism identifying its generator with the arithmetic one. In particular, no real Loewner driver, clock, boundary readout, or source-functional reduction has been derived that yields the prime-power delays. These are research obligations, not consequences of the current hierarchy.

The useful refinement is to seek closure on a functional of a sufficiently rich observable family. A finite scalar ODE for the single loop expectation is unnecessary. One must then identify a boundary sector or quotient of that functional evolution with the arithmetic transfer.

## 2. Two meanings of functional differential equation

On the physical side, the unknown can be a functional of contours, insertion sources, and boundary data. Derivatives with respect to those sources generate the curvature insertions and product expectations in the hierarchy.

On the arithmetic side, the known operator equation is already an evolution for a boundary function with spatial delays and a singular integral. These are different roles for the word functional. Deriving a loop/source equation does not by itself identify its boundary reduction with the arithmetic delay equation.

For a general deterministic Loewner driver the tip also depends on the driver's history. A local tip ODE available for the linear-driver example must not be assumed for arbitrary drivers. A functional state can retain that geometric information explicitly, or the contour can be treated as prescribed external data.

## 3. A concrete source-functional construction

Fix the same action, state, chord completion, and positive field-flow resolution as in the genuine-trace note. At the smooth-field level define the gauge-invariant, configuration-dependent observables

\[
 O_0=N^{-1}\operatorname{tr}Q_t,\qquad
 O_1=N^{-1}\operatorname{tr}(J_tQ_t),
\]
\[
 O_{D,\mu}=N^{-1}\operatorname{tr}(\mathcal D_{\mu,t}Q_t),\qquad
 O_2=N^{-1}\operatorname{tr}(\mathcal P_tQ_t).
\]

Their expectations are the existing W, M1, M_D, and M2. The identities hold before averaging:

\[
 \partial_tO_0=ikO_1,\qquad
 \partial_tO_1=\dot q^\mu O_{D,\mu}+2ikO_2.
\]

Introduce a separate source for each decorated observable, with labels retaining positions and noncommutative word order inside each trace. Sources are commuting because the complete traced observables are scalars; their labels must not identify different ordered words. Include further loops, networks and insertion types when the identities generate them. Define

\[
 Z_t[j]=\left\langle\exp\left(\sum_\alpha j_\alpha O_\alpha(t)\right)\right\rangle.
 \tag{1}
\]

The sum denotes finitely supported sources initially; continuous insertion labels become source functions and integrals. If exponential integrability is not established, use (1) only as a formal moment-generating series to the orders whose moments exist. It does not inherit an analytic generating functional from the two moment assumptions in the short-time theorem.

Now

\[
 \left.\frac{\delta Z_t}{\delta j_0}\right|_{j=0}=W(t),\qquad
 \left.\frac{\delta Z_t}{\delta j_1}\right|_{j=0}=M_1(t).
\]

Products of observables are obtained by higher source derivatives, with no large-N factorization. If the selected family has explicitly derived polynomial evolution

\[
 \partial_tO_\alpha=F_{\alpha,t}(O),
\]

then differentiation at fixed quantum measure gives

\[
 \boxed{\partial_t Z_t[j]=
 \sum_\alpha j_\alpha
 F_{\alpha,t}\!\left(\frac{\delta}{\delta j}\right)Z_t[j].}
 \tag{2}
\]

In particular, the part of this differential operator already fixed by the notes is

\[
 ikj_0\frac{\delta}{\delta j_1}
 +j_1\left(\dot q^\mu\frac{\delta}{\delta j_{D,\mu}}
              +2ik\frac{\delta}{\delta j_2}\right).
 \tag{3}
\]

The remaining terms have not been computed. Equation (2) is a construction rule, not a claimed new closed Yang--Mills equation. Merely assigning a new source to each unknown repackages the hierarchy. The useful result would be explicit rules determining every generated term, a specified invariant family or a bounded residual, and a well-posed evolution with physical initial data. At collapsed contour the undecorated holonomy is known, but all local insertion moments are not fixed by W(0)=1.

## 4. Where the quantum dynamics enters

The geometric variation and the field Schwinger--Dyson identities play distinct roles. On a finite lattice, Haar integration by parts gives the exact identity

\[
 \langle\nabla_e^a f\rangle
 =\langle f\,\nabla_e^aS_{\rm lat}\rangle.
\]

For a smooth test insertion X and finitely many source observables, substituting f = X exp(sum j O) yields

\[
 \left\langle\left[
 \nabla_e^aX+X\sum_\alpha j_\alpha\nabla_e^aO_\alpha
       -X\nabla_e^aS_{\rm lat}
 \right]e^{\sum jO}\right\rangle=0.
 \tag{4}
\]

The next calculation should choose the link insertions needed for the derivative moment, do the color contractions, and translate the resulting identities into source derivatives. Loop splitting produces product expectations, represented by higher derivatives of Z, rather than a product-of-expectations assumption. Equations (2) and (4) are respectively geometric transport and dynamical constraints; one cannot simply call the loop Laplacian the Loewner-time generator.

The calculation must retain:

- The transverse insertions D3 F3nu and D4 F4nu in four dimensions.
- Ordered two-curvature and higher insertions, plus finite-N multi-trace terms.
- The response of the flow map B_tau[A] to the original integration variable A.
- All contact and endpoint terms; an unflowed limit requires its own cusp renormalization.

A finite lattice gives exact field identities but ordinarily has discrete contour moves. Passing from that recursion to a continuously growing smooth contour requires an explicit interpolation/regulator argument. It is not supplied by writing a time derivative. Alternatively one can work with a regulator that supports the smooth variation, provided its measure identities are justified.

Makeenko's [lecture 3](https://arxiv.org/pdf/0810.2183) gives the continuum loop-equation structure, including the large-N product form and regularization issues. [Shen--Smith--Zhu](https://arxiv.org/abs/2512.00570) provides an example where closing a lattice Yang--Mills--Higgs recursion requires open lines. It supports enlarging the observable family as a method; it is a different action and not a closure theorem for the present pure-YM observable.

## 5. The arithmetic equation is already specified

Let b_omega = V_{omega,L} f. Translate the boundary window to (0,L), and extend b by zero outside it. The target is

\[
 \partial_\omega b_\omega=-G_{\omega,L}b_\omega,
 \qquad b_0=f.
 \tag{5}
\]

At zero shift the full nonsymmetric generator acts on a smooth test b as

\[
\begin{aligned}
 (G_{0,L}b)(x)={}&w_0b(x)
 +2\int_0^\infty n_\Gamma(u)
       [b(x)-\widetilde b(x-u)]\,du\\
 &+4\int_0^x\cosh(u/2)b(x-u)\,du\\
 &-2\sum_{\substack{n\ge2\\\log n<L}}
       \frac{\Lambda(n)}{\sqrt n}\widetilde b(x-\log n).
\end{aligned}
 \tag{6}
\]

Here n_Gamma(u) = exp(-u/2)/(1-exp(-2u)), w0 = psi(1/4)-log(pi), and the difference in the gamma integral is essential at u=0. Its tail beyond x is also retained. Formula (6) combines the existing [arithmetic generator](../sections/03_shift_evolution.tex) with the [fixed-window spatial formula](../sections/s_fixed_window.tex), after translating the interval.

At finite shift the full symbol is

\[
 a_\omega(p)=\frac12\{a_0(p-\omega)+a_0(p+\omega)\}.
 \tag{7}
\]

Consequently the delayed b(x-u) in the gamma integral acquires cosh(omega u), the pole kernel acquires the same factor, and the prime-power coefficients acquire cosh(omega log n); the local w0 and undelayed b(x) in the gamma difference keep their displayed coefficients. This follows directly from the shifted logarithmic derivatives on Re p > 1, and remains meaningful on the finite-window smooth core at omega=1/2. It supplies the finite-shift comparison rather than matching only the first derivative.

Thus a physical functional equation must explain precise translation operators and their coefficients. The current chord hierarchy has not identified a mechanism for the delays log n with weights Lambda(n)/sqrt(n).

## 6. The missing bridge as a testable identity

Suppose the physical construction yields a linear hierarchy state m_t^f for every boundary input f, with evolution

\[
 \partial_t m_t^f=\mathcal A_t m_t^f.
\]

The state can be infinite-dimensional and include product expectations; scalar closure is not required. A physically specified linear boundary readout R_t must give b_t = R_t m_t^f and satisfy

\[
 \boxed{(\dot R_t+R_t\mathcal A_t)m
 =-\dot\omega(t)G_{\omega(t),L}R_t m}
 \tag{8}
\]

on the sector generated by all admissible f, with R_0 m_0^f=f. For a fixed readout this reduces to an intertwining identity R A_t = -omega'(t) G_omega R. A time-dependent normalization contributes the dot(R) term and cannot be ignored. The initialization presumes omega(0)=0 for this version of the comparison.

This is a proposed precise bridge, not a construction of R or of m^f. It states what boundary closure means: physical information discarded by the readout must not feed an unaccounted term into the boundary evolution. The response, clock, and driver must be specified independently of inserting the answer G by definition. Causality, the strong identity limit, operator/core domains, and uniqueness must be proved before equality with V follows.

The scalar W(t) currently computed supplies none of the arbitrary-input structure required by (8). It can be a diagnostic or component of a later boundary construction. In the linear-driver example W_tau(t)=1-c_tau t^3+O(t^(7/2)); by contrast V_omega f=f-omega G_0 f+o(omega). This rules out a naive identification of that single scalar with the entire transfer at a clock with nonzero initial speed. It does not exclude a selected matrix element with vanishing initial response, a clock with different initial scaling, or another boundary observable. A cubic clock alone would still supply no boundary generator.

Matching the transfer equation is separate from proving a positive balance for I-V*V. Neither ordinary loop expectation nor a formal functional equation supplies the needed norm identity automatically.

## 7. Recommended sequence and concrete deliverable

1. Carry out the existing handoff: compute the finite-regulator Schwinger--Dyson reduction of the derivative moment, displaying transverse, splitting/contact, and flow-response terms with their coefficients.
2. Introduce source channels for exactly those generated terms. Write the first complete source equations and an explicit rule for their further generation. State whether they close in a useful family or exhibit the remaining residual.
3. Define a candidate boundary response linear in arbitrary f, and derive its evolution from the same source system. Specify its initial distributional kernel and causal support.
4. Test (8) first for 0<L<log 2, including the local constant, singular gamma difference, and full causal pole response. This is a later arithmetic test, not an entrance requirement for the physical calculation.
5. Cross the first delay threshold log 2<L<log 3. Derive the generator contribution -(2 log 2/sqrt(2)) cosh(omega log 2) T_{log 2} from the physical construction. Then determine whether one rule produces every prime-power delay and the full finite-shift transfer.

The immediate deliverable should therefore be an explicit source-functional equation and its observable-domain statement, with a separately stated boundary matching criterion. The current notes establish the start of the first task. They do not yet supply the source equation's full operator or the boundary projection needed for the later tasks.
