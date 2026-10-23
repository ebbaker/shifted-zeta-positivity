# Fractional reciprocal bounds and time-integrated ordinary-event payments

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex), reasoning effort ultra**, verified by the parent from this research turn's metadata. **Status: analytic derivation, not independently reviewed.** This note changes the integral consumer rather than claiming an endpoint simplicity estimate.

Read the [result index](../../../../result-summaries/README.md), [collision-control summary](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), especially patterns 01, 02, 07, 12 and 20. A finite energy for an observation that remains finite at a double zero cannot exclude that double. All bounds below are available to the direct integration comparator.

## 1. Two complementary integral consumers

The manuscript's full two-sheet reciprocal energy is

\[
E_\tau=2\int_D |F_\tau(z)|^{-1}\,dA_z.
\]

It diverges logarithmically at an ordinary double. Two weaker, useful consumers remain quantitatively bounded: the fixed-time fractional reciprocal integral for exponent below one, and the heat-time average of the original energy. These are **finite bounds**, not new RH-equivalent criteria. Their finiteness is compatible with ordinary double events.

## 2. A sharp gap-uniform fractional pair bound

Let \(D=D(C,R)\), and suppose

\[
F(z)=(z-\alpha)(z-\beta)V(z),\qquad |V(z)|\ge\nu>0
\]

on the disk. Coincident roots are allowed. For every \(0<p<1\),

\[
\boxed{\quad
2\int_D |F(z)|^{-p}\,dA_z
\le \frac{2\pi R^{2-2p}}{(1-p)\nu^p}.
\quad} \tag{FP1}
\]

There is no root separation or interior field floor in FP1. The constant is sharp over this information class, attained by \(F(z)=\nu(z-C)^2\).

**Proof.** The arithmetic-geometric mean inequality gives

\[
\frac1{|z-\alpha|^p|z-\beta|^p}
\le\tfrac12\bigl(|z-\alpha|^{-2p}+|z-\beta|^{-2p}\bigr).
\]

For any point \(\gamma\), the integral over an area-\(\pi R^2\) disk of the radial decreasing function \(|z-\gamma|^{-2p}\) is at most its integral over the disk centered at \(\gamma\). One elementary proof uses layer cake and
\(\operatorname{area}(D\cap D(\gamma,r))\le\min(\pi R^2,\pi r^2)\). Thus

\[
\int_D |z-\gamma|^{-2p}\,dA_z
\le2\pi\int_0^R r^{1-2p}dr
=\frac{\pi R^{2-2p}}{1-p}.
\]

Apply this at both roots, multiply by \(2\nu^{-p}\), and obtain FP1. At the coalesced centered example every inequality is equality. At \(p=1\) that same example diverges, so the restriction cannot be removed for the stated class. \(\square\)

For the [manuscript's complete-source ordinary-event chart](../manuscript/reciprocal_hodge_energy/sections/06_heat_chart.tex), \(R=r\) and \(\nu=3|A|/4\) are already derived from complete canonical moments and the event curvature. Hence FP1 is an endpoint-uniform bound **conditional on that finite chart**, including its singular central fiber. It is not uniform in event height or curvature. Fractional powers are integral weights here; no unprovided single-valued differential on the double cover is asserted.

## 3. An explicit time-strip payment for the original energy

Use the [manuscript's complete-source event chart](../manuscript/reciprocal_hodge_energy/sections/06_heat_chart.tex), with its fixed disk \(D(0,r)\), real \(0<\tau\le\sigma\), deflated unit floor \(\nu=3|A|/4\), root midpoint \(m_\tau\), and half gap \(a_\tau\). The chart proves

\[
|m_\tau|<r,\qquad
 a_\tau^2\ge6\tau/5,
\]

rather than assuming a root gap. The [full direct quadratic sandwich](../manuscript/reciprocal_hodge_energy/sections/05_remainders.tex) therefore gives

\[
E_\tau
\le\frac{4\pi}{\nu}\operatorname{arsinh}
 \frac{r+|m_\tau|}{a_\tau}
\le\frac{4\pi}{\nu}\operatorname{arsinh}
 \frac{K}{\sqrt\tau},
\qquad K=2r\sqrt{5/6}. \tag{TP1}
\]

No root-location acquisition or numerical gap floor is needed beyond the already proved event chart. This is an inherited pointwise bound followed by a new explicit integral payment, not an improved fixed-time endpoint estimate.

For every \(0<s\le\sigma\),

\[
\boxed{\quad
\int_0^s E_\tau\,d\tau
\le\frac{4\pi}{\nu}
\left[s\operatorname{arsinh}\frac K{\sqrt s}
       +K\sqrt{s+K^2}-K^2\right]
\le\frac{4\pi s}{\nu}
\left[\operatorname{arsinh}\frac K{\sqrt s}+\frac12\right].
\quad} \tag{TP2}
\]

**Proof.** A primitive of \(\operatorname{arsinh}(K/\sqrt\tau)\) is

\[
\tau\operatorname{arsinh}(K/\sqrt\tau)+K\sqrt{\tau+K^2}.
\]

Its limit at zero is \(K^2\). Also
\(K(\sqrt{s+K^2}-K)=Ks/(\sqrt{s+K^2}+K)\le s/2\).
Integrating TP1 gives both inequalities. The energy at the single singular time may be infinite; Tonelli and the displayed integrable majorant give the stated improper and Lebesgue integral unambiguously. \(\square\)

In particular the omitted event-time strip costs \(O(s\log(1/s))\), with every constant displayed. This permits complete finite acquisitions on \([s,\sigma]\) to be combined with a paid interval containing the event, without acquiring a collapsing gap on that omitted strip.

## 4. Time weights and moving subdomains

For every real \(\beta<1\),

\[
\boxed{\quad
\int_0^s \tau^{-\beta}E_\tau\,d\tau
\le\frac{4\pi s^{1-\beta}}{\nu}
\left[
 \frac{\log(1+2K/\sqrt s)}{1-\beta}
 +\frac1{2(1-\beta)^2}
\right].
\quad} \tag{TP3}
\]

Indeed \(\operatorname{arsinh}x\le\log(1+2x)\), and for \(0<\tau\le s\),

\[
\log(1+2K/\sqrt\tau)
\le\log(1+2K/\sqrt s)+\tfrac12\log(s/\tau).
\]

Integrating the two terms gives TP3. The restriction \(\beta<1\) is sharp for a universal finite bound over ordinary double charts: the exact quadratic heat control \(F_\tau=z^2-2\tau\) has \(E_\tau=2\pi\log(1/\tau)+O(1)\), and the weighted integral diverges for every \(\beta\ge1\).

For measurable moving subdomains \(\Omega_\tau\subseteq D\) and any scalar kernel satisfying \(|W(\tau,z)|\le W_0\tau^{-\beta}\), TP3 gives the complete bound

\[
\left|\int_0^s\int_{\Omega_\tau}
       \frac{W(\tau,z)}{|F_\tau(z)|}\,dA_z\,d\tau\right|
\le\frac{W_0}{2}\int_0^s\tau^{-\beta}E_\tau d\tau.
\tag{TP4}
\]

Thus bounded spatial tests, time-averaged reciprocal quantities, and omitted time strips in this declared observation have explicit payments even though the fixed-time energy is not endpoint-uniform. Moving-domain transport derivatives, boundary traces, and kernels singular in the spatial variable require their own estimates; TP4 does not provide them.

## 5. Sibling comparison and the exact obstruction

The BW10 files already contain integrated-energy statements for **different observations**:

* [BW10 Note 12, sections 3–4](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md), section 3 proves that inverse-square root-gap energy has \(1/t\) growth and a nonintegrable endpoint time cost. Section 4 proves finite time energy after derivative rescaling, while preserving the ordinary cap phase. TP2 changes neither result.
* [BW10 Note 15, HI2–HI3](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md) bounds and averages the completed-ratio energy; endpoint multiplicity disappears from that fixed-weight limit. TP2 concerns \(2\int |H|^{-1}dA\), not that ratio.
* [BW10 Note 21](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md) and [Note 22](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md) pay physical signed-tube traces against the phase measure and keep all faces and derivative-scale corrections. A three-dimensional bulk bound such as TP4 does **not** give their one-dimensional cap trace or a bound for \(1/(H^2+H_x^2)\).
* [BW09's complete signed cap budget](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/research-overview/03_ANALYTICAL_PHASE_SURPLUS_PROGRAM_20261020.md) still requires an independently proved signed phase surplus. A finite positive reciprocal average supplies no such sign and no extra cap pair.

These duplication checks prevent the finite time bound from being relabeled as progress on a sibling's missing endpoint or arithmetic margin. Its useful consumer is expressly the bounded spacetime reciprocal integral and its paid event-time truncation error.

## 6. Controls and continuation decision

FP1 and TP1--TP4 use only a local analytic pair chart and paid unit/source constants. The quadratic heat control attains the endpoint behaviors and passes them. Matching ordinary events in the catalogued controls pass the corresponding own-data local chart as well. The estimates are therefore compatible with collisions, which is necessary for the chosen consumer. Their source distinctions remain separate: quadratic/atomic models fail unchanged theta arithmetic; Euler-factor modifications change that arithmetic; weighted-square and finite-prime controls fail the full normalized reflection conjunction; reflected and primitive controls fail the unchanged normalized square coefficients; BW10's close positive-source controls fail ordinary Dirichlet arithmetic. None is asserted to share the full canonical class.

**Outcome.** Two complete finite integral bounds are available without an endpoint field floor: a sharp fractional pair estimate and an explicit heat-time-strip payment for the original reciprocal energy. They do not shrink the class of allowed ordinary events and close no RH, simplicity, signed-phase, or all-height coverage gate. An actual later consumer should specify its integral kernel and domain before acquisition. No numerical campaign is needed for these analytic bounds.
