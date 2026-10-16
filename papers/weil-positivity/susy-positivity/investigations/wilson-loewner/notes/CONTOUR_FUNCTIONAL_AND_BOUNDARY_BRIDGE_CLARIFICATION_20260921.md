# The contour functional and the meaning of the proposed arithmetic bridge

21 September 2026. Prepared for Edward Baker.

**Model:** GPT-6 (Codex; developer-provided identity).
**Effort:** not exposed in this session; not inferred.
**Status:** conceptual clarification and research-order revision, prepared with LLM assistance. No physical boundary realization or new Schwinger--Dyson reduction is claimed.

## 1. Revision of the proposed order

Baker asks to identify the most natural functional formulation before carrying out the growing-trace handoff. This takes priority over the sequence proposed in Section 7 of [the preceding assessment](WILSON_FUNCTIONAL_EVOLUTION_AND_ARITHMETIC_MATCHING_20260921.md).

The abstract readout R in that assessment stated a sufficient compatibility condition. It did not supply a physical mechanism, a choice of boundary states, or a construction of R. The source generating functional was a general way to organize unknown moments. It should not be treated as a preferred physical realization before the geometric and boundary variables are specified.

For the currently chosen pure-YM observable, the natural starting object is the Wilson functional of the entire contour. The immediate question is what contour or network variables a boundary response would retain, and how those variables behave under growth, insertion, and cutting. The Schwinger--Dyson calculation should then address that specified object.

## 2. An area derivative already contains the first insertion

At fixed positive field-flow resolution tau, set

\[
 \mathscr W_\tau[C]=\left\langle N^{-1}\operatorname{tr}
                 \operatorname{Hol}_{B_\tau}(C)\right\rangle.
\]

The quantum theory and measure are fixed. C is an argument of the functional, not a random contour. For C_t equal to the genuine trace followed by its return chord, the existing W_tau(t) is the restriction mathscr W_tau[C_t].

Define the oriented area derivative by attaching an infinitesimal positively oriented 12-plaquette at a marked point of the return chord. In the Hermitian-connection conventions of the [growing-trace note](GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md),

\[
 \frac{\delta\mathscr W_\tau[C_t]}
      {\delta\sigma^{12}(r q(t))}
 =i\left\langle N^{-1}\operatorname{tr}
             (\widehat F_{12,t}(r)Q_t)\right\rangle.
 \tag{1}
\]

The marked occurrence and its transport path matter, particularly for self-intersections. This identity is at smooth-field resolution and inherits the existing assumptions for passage through the expectation. It is not a claim about an unrenormalized cusped continuum loop.

The existing tip-cancellation result therefore becomes

\[
 \boxed{\frac{d}{dt}\mathscr W_\tau[C_t]
   = k_t\int_0^1 r\,dr\,
       \frac{\delta\mathscr W_\tau[C_t]}
            {\delta\sigma^{12}(r q(t))}.}
 \tag{2}
\]

The infinitesimal signed area swept at chord parameter r is k_t r dr dt. For constant commuting curvature, integrating r gives k_t/2, the established oriented-area growth, checking the sign and factor in (2).

This reformulates the existing result geometrically. It is a chain rule and does not determine the Wilson functional. Knowing W at one contour does not give its derivatives in neighboring contour directions. Higher insertion moments are naturally related to repeated marked area/path derivatives, with their ordering and contact terms retained.

The standard area/path-derivative formulation and its relation to the Yang--Mills Schwinger--Dyson identity are discussed in [Makeenko, Lecture 3, equations (3.1)--(3.4)](https://arxiv.org/pdf/0810.2183). That equation constrains a divergence of an area derivative; it is not the particular directional derivative in (2). At finite N its splitting terms require multi-loop expectations. Thus a natural enlarged functional domain is loop collections and, where needed, marked networks. Positive field-flow time additionally requires differentiating B_tau[A] in the field identities.

## 3. What the abstract readout meant

Suppose m stores all relevant expectation values and obeys dot(m)=A_t m. A readout b=R m keeps only the information used as the boundary output. For fixed R,

\[
 \dot b=R A_t m.
\]

For an autonomous boundary law dot(b)=B_t b, one needs R A_t m=B_t R m on the physically reachable sector. Otherwise two states with the same boundary output may have different output derivatives because information discarded by R affects the future. A time-dependent R contributes dot(R)m as well. This is the origin of the previous compatibility equation.

The simplest illustration is dot(b)=a b+c h, where h is a hidden insertion moment. Retaining b alone does not determine dot(b) unless the coupling c vanishes or an independently proved relation controls h from b on the relevant sector.

For a linear block hierarchy

\[
 \dot b=A_t b+B_t h,\qquad \dot h=C_t b+D_t h,
\]

eliminating h gives, whenever the hidden propagator U_D exists,

\[
 \dot b=A_t b+B_tU_D(t,0)h_0
       +\int_0^t B_tU_D(t,s)C_s b_s\,ds.
\]

This generally introduces history dependence in the evolution parameter. Arithmetic delays b_omega(x-log n) instead act in the boundary coordinate at the same omega. These are different types of nonlocality. An exact reduction must explain why additional time-history dependence disappears or is represented by retained state variables.

Thus the readout condition encodes the main closure problem. It is not a theorem that such a readout exists or that an arbitrary projection preserves a closed evolution. The boundary preparation mapping an arbitrary input f into the physical state is a further required part of the construction.

## 4. A direct boundary-kernel formulation makes the bridge concrete

A less abstract formulation would specify a physical two-boundary observable O_t(x,y), its endpoint contractions or probe states, and its normalization, then set

\[
 \mathcal K_t(x,y)=\langle\mathcal O_t(x,y)\rangle,
 \qquad b_t(x)=\int_{I_L}\mathcal K_t(x,y)f(y)\,dy.
 \tag{3}
\]

The observable in (3) is a proposed format, not one already constructed by the scalar chord loop. One must specify what x and y label and how the Wilson network couples them. The full observable is gauge invariant; endpoint matter or boundary states cannot be silently assumed available in pure YM. External probe constructions must specify their contractions without changing the fixed bulk action by assumption.

The physical contour variation, including endpoint and normalization changes, would calculate dot(K). The arithmetic bridge then asks whether

\[
 \boxed{\partial_t\mathcal K_t(x,y)
  =-\dot\omega(t)\,
    (G_{\omega(t),L}^{(x)}\mathcal K_t)(x,y),\qquad
    \mathcal K_0(x,y)=\delta(x-y).}
 \tag{4}
\]

The distributional formula is to be interpreted on admissible test inputs with the required core/domain statements. Integrating against any f gives the desired boundary equation immediately. Given well-posedness and the identity initial condition, the resulting transfer is the arithmetic V. This is the concrete meaning of the abstract readout compatibility condition for this kernel realization.

Equation (4) asks the field insertions caused by growth to equal a known integral/delay operation in the output coordinate x. This is the substantive identity to discover. The raw collapsed-loop value W[point]=1 is not the distribution delta(x-y); a family of scalar expectations is not automatically the correctly initialized boundary response.

If a boundary radius r is eventually identified with x=log r, translation x to x-log n means dilation r to r/n. This offers a geometric interpretation of the arithmetic delay that can be tested. It is only a coordinate dictionary: it supplies neither a dilation-producing physical mechanism nor the coefficient Lambda(n)/sqrt(n).

## 5. What to decide before the handoff

The preliminary deliverable should specify one candidate contour/network functional with meaningful boundary arguments. It should answer:

1. What are the boundary input, output, and their physical pairing?
2. Which contour family does Loewner growth vary, including its return path or endpoint contraction?
3. Why is the initial boundary response the identity, and what establishes causal support?
4. Do growth and field identities stay within this functional family, or which marked contours and networks must be added?
5. What physical meaning could translation of the boundary coordinate have?

For the current pure-YM calculation, the contour functional and its marked multi-loop extension are the most direct geometric starting point. Whether they contain a suitable arithmetic boundary response remains open. Sources can then serve as coordinates on the selected family. They need not determine the family in advance.

No new Schwinger--Dyson calculation or manuscript change was performed for this clarification.
