# Dimension, transform, and zero-density comparison

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**.
Chat0016, *Identify equation 2.1 Mellin form*.

**Status: conceptual comparison of existing identities and their scopes.**
No new flow, collision criterion, numerical campaign or manuscript revision.
The author's question is what higher dimensions and the transform actually
accomplish, and whether Investigation01's heat-density tools provide a
natural connection to zeros. The present assessment is that dimension three
has an algebraic motivation, while its added value for collision bounds
remains unestablished.

## 1. Why three occurs, and what this establishes

In [the current book](../book/main.tex), Section1.2, the radial formula
\[
\Delta_d e^{-\pi n^2r^2}
=(4\pi^2n^4r^2-2d\pi n^2)e^{-\pi n^2r^2}
\]
matches the canonical source after multiplication by \(r^{5/2}/2\)
precisely at \(d=3\) within this Gaussian realization. The theta inversion
weight \(r^{-1}\) also matches the three-dimensional Kelvin weight.
This supplies a smooth positive Newtonian potential and useful Green and
inversion identities. It is not an arbitrary choice of notation.

But angularly constant initial data and a unique rotation-equivariant
evolution remain radial. The current spectral observation sees only the
spherical mean. Thus the added angular variables supply no independent
initial information. Radial Euclidean heat still has the nontrivial drift
\(2r^{-1}\partial_r\); this statement does not identify it with cylinder
heat. Ordinary cylinder heat gives \(e^{-sz^2}H(0,z)\), while transported
Newman flow is \(\partial_tG_t=\mathcal L^{-1}u^2\mathcal LG_t\).
The occurrence of a Laplacian in the source identity alone does not make
Newman evolution ordinary spatial heat.

## 2. What the heat-density tools actually observe

The [Investigation01 physical equations](../../01_heat_density_asymptotics/book/sections/05_physical.tex)
act on the complex spectral plane \(z=x+iy\). For spatially constant
\(\epsilon>0\), at a fixed time,
\[
\rho_\epsilon(t,z)
=\frac{\epsilon^2|H_z(t,z)|^2}{\pi(|H(t,z)|^2+\epsilon^2)^2}
=\frac1{4\pi}\Delta_{x,y}\log(|H(t,z)|^2+\epsilon^2).
\]
The [underlying contour manuscript](../../../investigations-4/12_height_dependent_heat_contours/manuscript/book.tex),
Section2, proves local weak convergence to
\(\nu_t=\sum_{H(t,a)=0}m_a\delta_a\). Consequently, on a bounded
domain with zero-free boundary, the integral tends to the number of zeros
counted with multiplicity. At finite regulator, positive density or positive
mass is not by itself a zero certificate. A finite-error application needs
enclosures sufficient to distinguish the integer count. The actual
spatially varying regulator in Investigation01 also has the recorded
curvature corrections; it cannot silently be replaced by the constant
regulator identity.

This is a direct link to zeros because the density is a nonlinear function
of the completed spectral integral and its derivative. Its logarithm and
denominator cannot generally be moved inside that integral and applied
pointwise to the auxiliary potential V. In the Mellin strip the integral
I and H have the same zeros because their prefactor is nonvanishing, so
one can form a zero density from I there; doing so retains the entire
oscillatory cancellation problem. It does not turn local source positivity
into a zero bound.

The two real dimensions here have a direct role: they are the domain of
the holomorphic function whose zeros are being measured. They are different
from the auxiliary three-dimensional source space.

## 3. Counting, multiplicity, and exclusion

An enclosing region has total mass two both for two simple zeros and for
one double zero. Section8 of the underlying contour manuscript therefore
uses a separate finite-divisor observable. With planar heat kernel
\(K_s=(4\pi s)^{-1}e^{-|z|^2/(4s)}\) and
\(N=\nu(\mathbb C)\), it proves
\[
8\pi s\int(K_s*\nu)^2\,dA-N
=\sum_a m_a(m_a-1)
+\sum_{a\ne b}m_am_b e^{-|a-b|^2/(8s)}.
\]
For a fixed finite divisor, the small-s limit detects multiplicity excess.
When recovered from regulated density, the regulator limit is taken first.
A finite-scale or evolving application must pay localization and resolution
errors; counting and concentration identities alone exclude no collisions.
The double model \(H(t,z)=z^2-2t\) obeys these generic identities and
has multiplicity excess two at its double event. It lacks the unchanged
canonical theta source, but violates no premise of these counting identities.

## 4. The earlier source-space heat detector is dimension-independent

[Note25](25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md),
Section3, already records missing leading diffusion modes at a marked
zero or collision. The elementary reason works for integrable signed data
f in any dimension d with the indicated finite absolute moments:
\[
(4\pi s)^{d/2}(e^{s\Delta}f)(0)
=\int f-\frac1{4s}\int|Y|^2f(Y)\,dY+R_s,
\qquad |R_s|\le\frac1{32s^2}\int|Y|^4|f(Y)|\,dY.
\]
This follows by expanding the Gaussian with
\(|e^{-v}-1+v|\le v^2/2\) for \(v\ge0\). Assigning total mass H,
and derivative mass H_z, makes a collision visible as two missing leading
coefficients. Detection does not require d=3. This statement concerns the
spectrally weighted integrable density in Note25, not V, whose 1/r tail is
not integrable in Euclidean volume.

Note25's smooth positive-source collision control passes this heat theorem
on its stated moment/convergence domain, despite failing the canonical
integer-square theta premise. [Note29](29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md)
also records that positive-carrier estimates convert an independently
available first-jet lower bound into regularity; they do not produce that
lower bound. No new control run is claimed here.

## 5. Present interpretation

The scalar transform is faithful; the spatial realization organizes it;
the spectral zero density measures its zeros. Their exactness does not
establish an independent estimate on cancellation or multiplicity.
A claim that the three-dimensional construction improves the zero problem
would need a specific estimate transferred from that construction with its
hypotheses and errors justified. No such improvement is established by
this comparison. This does not rule out coupled fields, other observations,
or canonical source-specific estimates.

This assessment follows the [result index](../../../../result-summaries/README.md),
especially [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md),
and the [pattern index](../../../../avoid/README.md), particularly
[geometric re-realizations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
Investigation01's own [frontier discussion](../../01_heat_density_asymptotics/book/sections/08_frontier.tex)
separates its approximation programme from the independent lower data needed
for collision applications. Existing source status and internal-review
qualifications remain unchanged. No external literature was newly imported.
