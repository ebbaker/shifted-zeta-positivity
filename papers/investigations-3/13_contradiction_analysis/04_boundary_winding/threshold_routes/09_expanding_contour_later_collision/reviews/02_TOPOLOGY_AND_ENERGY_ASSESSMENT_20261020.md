# Mathematical audit of the topology and energy assessment

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6-astra (Codex)**,
actual reasoning effort **ultra**, verified from the parent turn metadata.

**Status: separate same-model mathematical audit; no blocking error
found.** This is not cross-model or specialist review and supplies no
independent numerical implementation. The audited [Note 05][note] has
SHA-256
`aac1e09bdb4792f01d79e9aba141335a6166b4ae64bf98923e2906e84f635b74`.
The parent separately checked the primary-literature reference; this
audit concentrates on the displayed mathematics and its claimed scope.
The [result index][results] and [avoid index][avoid], especially
[review independence][a05] and [scoped conclusions][a07], apply.

The first-jet boundary map takes values in \(\mathbb C^\times\), whose
loop classes are classified by winding. The projective map has degree
\(2W_J\). These claims do not exclude richer information from a different
field, domain, or operator realization.

Direct differentiation verifies both phase identities and
\[
Q_t+Q_{xx}=2(H_{xx}^2-H_xH_{xxx}).
\]
The latter is another Laguerre form, with no automatic favorable sign.
The note correctly restricts the implication from all-realness to the
relevant Laguerre–Pólya setting, rather than arbitrary entire functions
having real zeros.

The localized integration-by-parts identity has the correct coefficient
\(-1/2\) on \(\int\psi''H^2\), and its finite-interval endpoint term is
\([-\psi HH_x+\psi'H^2/2]_a^b\). Compact support removes that term.
Integrating in time introduces no extra time-boundary term because no
time integration by parts is used. Negative average with a nonnegative
weight really implies a negative point, but the existence of an
unspecified successful weight is only a reformulation of that point
witness.

The symmetric two-source kernel has coefficients
\((u+v)^2/4\) and \((u-v)^2/4\), with the displayed positive signs.
Consequently a nonnegative cosine transform prevents a negative average
for every admissible nonnegative cosine source. The corrected example
explicitly centers its Gaussian at \(x=0\): translating to an event
height introduces an oscillatory cosine factor and changes the screen.
The stated integrability assumptions justify the exchanges.

The jet-energy balance includes both moving-wall fluxes with their
correct signs. On a nondegenerate stationary branch,
\(b'=H_{xxx}/H_{xx}\), \(V'=-H_{xx}\), and
\((V^2/2)'=Q(t,b(t))\). A connected branch with fixed nonzero curvature
cannot return to its initial zero. This does not assert global
continuation or eliminate other critical branches.

The angular-energy coefficient is \(4\pi^2\), and the zero-winding
oscillatory example has exactly \(2\pi^2B^2/\ell\) energy. A small
physical-contour energy could exclude the initial event; large
regularized-contour energy cannot force an extra event or its sign.
For the bulk formula,
\[
d\alpha_\epsilon
=\frac{2\epsilon^2\,dH\wedge dH_x}{(E+\epsilon^2)^2},
\qquad
dH\wedge dH_x
=-(H_{xx}^2-H_xH_{xxx})\,dt\wedge dx.
\]
These verify the orientation and the final factor \(-1/\pi\).
Boundary convergence suffices for the limit; the note does not
improperly take the pointwise limit inside the area integral.

The finite real-root velocity has factor 2, giving
\(x'=-2\nabla U\) and \(U'=-2\sum_i(\partial_iU)^2\).
Bounded configurations keep all noncolliding contributions to \(U\)
bounded below, so a collision would contradict its decrease. This uses
the complete finite real-root system. The two-event quartic fails that
premise between its events, and infinite theta roots require the
additional controls stated in the note.

The quadratic and cubic substitutions have strictly positive future
\(Q\); polynomial integral identities are invoked only where their
integrability hypotheses hold. The nonpolynomial table is explicitly
a premise screen, not a new calculation on every control.

**Assessment:** the note identifies a sensible alternative *estimate
request*, a fixed localized signed Laguerre functional. Removing
pointwise \(H_{xx}\) from its evaluation could help, but the additional
spatial integration, signed cancellation, and growing weight
derivatives may offset that benefit. No practical advantage, negative
theta margin, or later-collision result has been demonstrated. A
successful negative average would directly contradict future
all-realness and need not first force a later real collision inside
the BW09 contour. The note appropriately records no new completed
theta-estimate milestone.

[note]: ../notes/05_TOPOLOGICAL_ALTERNATIVES_AND_ENERGY_OBSERVATIONS_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
