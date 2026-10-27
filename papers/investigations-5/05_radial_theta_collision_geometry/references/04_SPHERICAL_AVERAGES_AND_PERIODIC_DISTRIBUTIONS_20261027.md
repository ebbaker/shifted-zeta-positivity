# Spherical averages and periodic distributions: selected references

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Used in [Note07](../notes/07_SPATIAL_SPHERES_LOGARITHMIC_MODES_AND_PERIODIC_LATTICES_20261027.md). These are selected-passage checks, not whole-book audits.

## NIST Digital Library of Mathematical Functions

Primary sources: [10.49.3](https://dlmf.nist.gov/10.49.E3), [10.54.1–2](https://dlmf.nist.gov/10.54).

Checked online on 27 October 2026: j_0(w)=sin(w)/w and the n=0 angular integral giving j_0(w)=(1/2) integral_0^pi exp(i w cos(theta)) sin(theta) dtheta. With w=z rho, the angular integral is the normalized spherical average in R^3. Its value at zero is the removable entire value one; complex z is allowed. These identities fix only the angular kernel and normalization. They do not give a collision exclusion or a lattice realization of the source.

This extends the existing canonical NIST-DLMF entry in sources.json. Online reference; no artificial PDF.

## Victor Ivrii, Partial Differential Equations

Author and title checked in the [online contents](https://www.math.utoronto.ca/courses/apm346h1/20169/PDE-textbook/contents.html). Source examined: the APM346 online textbook in the 20169 course URL; no immutable edition identifier or revision date is asserted. Retrieved 27 October 2026.

Checked passage: [Section 11.2, “Fourier series,” equations 11.2.9–12](https://www.math.utoronto.ca/courses/apm346h1/20169/PDE-textbook/Chapter11/S11.2.html). A full-rank lattice-periodic distribution has a Fourier series on the reciprocal lattice. Ivrii writes the modes with exp(i m dot x); Note07 instead uses exp(2 pi i k dot x) and defines its reciprocal lattice accordingly. The transform then consists of coefficients multiplying delta masses at k. This is standard distributional Fourier-series background.

The spherical-average obstruction in Note07 is proved there by rotation averaging this support and using continuity of an L^1 Fourier transform. It is not attributed to a theorem claimed to be stated by Ivrii. Full-rank periodicity, equality as distributions, and global L^1 of the resulting radial field are the decisive hypotheses. The conclusion is zero radial mean, not zero original periodic field.

This is an author-hosted online textbook section, retained as a linked reference. No PDF was used or downloaded.

## Internal radial-Bessel predecessor

The [10 October positive three-dimensional theta lift](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/notes/1_POSITIVE_THREE_DIMENSIONAL_THETA_LIFT_AND_NONLOCAL_GENERATOR_20261010.md) supplies the exact inverse radial marginal, its nonlocal generator, a proven theta-trajectory positivity interval 0<=t<=1/20, and the positive radial double-zero control. Its [internal review](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md) is not an independent review.

The [following sine-jet note](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/notes/2_SINE_COLLISION_JETS_AND_HIGH_DIMENSION_THETA_OBSTRUCTIONS_20261010.md), Sections 1–2, retains signed collision jets and cutoff endpoint terms. These passages were inspected; no new audit of its later high-dimensional claims was performed.

Note07 relabels that construction's radius rho to distinguish it from the original theta radius r=exp(2u). Its checker was replayed unchanged; see the [replay receipt](../numerics/07_INHERITED_RADIAL_CHECK_REPLAY_20261027.json).
