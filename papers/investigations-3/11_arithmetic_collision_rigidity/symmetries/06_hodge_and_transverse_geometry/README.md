# S06 Hodge duality and transverse two source geometry

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual effort **max**.
Exploratory direction using established identities and scoped obstructions;
no new geometric sign estimate.

## Question and additional ingredient

Can the manifold techniques of Investigation 22 supply a useful symmetry
or estimate after transverse theta information or a coupled signed
two-source identity is inserted into the physical observation? This is
the additional Hodge direction requested in this conversation. The
[assessment][review] identifies why a bare Hodge dual or a tangential ASD
calculation alone does not suffice. The [program guide][guide] gives the
common target and controls; [S05][jets] supplies simplified source jets.

The first research obligation is to specify the extra ingredient beyond
the existing restricted geometry and explain how it reaches the actual
spectral transform. No general impossibility of geometric methods is
asserted.

## Known identities and boundaries

The four-dimensional construction has
\[
 \alpha_f=\operatorname{Re}(f(z)\,dz\wedge dw)/\sqrt2,
 \quad *\alpha_f=\alpha_f,\quad
 \alpha_f\wedge\alpha_g=\operatorname{Re}(f\bar g)\,dV.
\]
The Laguerre polarization retains one negative coefficient-space
eigenvalue even though all input forms are self-dual. The example
f(z)=1+z^2 has negative Laguerre value at zero. A positive norm discards
the mixed sign; it cannot be substituted for the physical pairing.
Self-duality of two-forms in four dimensions also differs from the
quarter turn of one-forms in the two-dimensional jet plane.

On the marked elliptic family \(\tau=p+iq\), the ASD curvature is
\[
 F=2\pi i(q\,dp\wedge dq-dr\wedge ds),\qquad *F=-F.
\]
Its physical path is \(\gamma(u)=(\tau=ie^{4u},z=0)\). The adapted
connection restricts to zero there, and the natural external product on
gamma times gamma is flat. Hence tangential differentiation on these
specified restrictions cannot supply a new curvature-sign term.

Transverse derivatives before restriction retain
\[
 [\nabla_X,\mathcal D^k]\big|_{z=0}
       =-k(k-1)\pi q^{-1}\mathcal D^{k-2}\big|_{z=0}.
\]
On the two-dimensional zero section the p,q curvature is nonzero. A use
of p-variation needs a justified transform to the physical observation;
the spectral x is not the elliptic base coordinate p. Changing the
Hermitian metric while fixing the arithmetic section changes its norm;
transport the observation covector too when using a bundle isometry.

## Read in this order

1. [Note 07][note] and [Review 14][review] for the distinction between
   Hodge, modular, and first-jet dualities.
2. [Investigation 22 manuscript][manifold], Hodge pairing and marked
   real Gauss-map sections, for the signed observations and boundary costs.
3. [ASD metric freedom and physical restriction][metric], especially
   transverse commutators and the scoped remaining opportunity.
4. [Complete signed two-source bridge][bridge], including primitive
   lower edges, the energy corner, and all heat and phase factors.
5. [Coupled theta product and parity sectors][coupled] and
   [parity cutoff continuation][parity], for the genuinely coupled
   source identity and its exact Gram obstruction.

## Three possible subproblems

**Transverse transfer.** Choose a concrete transverse derivative or mixed
commutator, compute it before physical restriction, and derive an exact
formula in the physical transform. Retain the source section and its dual
test covector. Specify the signed term or remainder whose estimate would
improve. The already-known lower-jet commutators alone are background.

**Signed boundary currents.** Use the mixed Hodge pairing or disk/current
identity with an explicit boundary domain. Identify an arithmetic estimate
of the full boundary contribution at the physical energy scale. Integrated
positivity without a paid boundary-to-central comparison does not answer
the collision question. The sharp disk boundary cost is already known.

**Coupled source symmetry.** Retain independent q=e^(4u), r=e^(4v) and the
addition variables X=z+w, Y=z-w. The known identity has the mixed operator
\[
 \exp\{(q-r)\partial_X\partial_Y/(2\pi)\}
 \sum_{\epsilon=0}^1
 \vartheta_\epsilon(X,i(q+r))\vartheta_\epsilon(Y,i(q+r)).
\]
Both complete source operators must act before the physical restriction.
At q unequal to r the mixed term remains. Both post-source parity matrices
are indefinite, and estimating the sectors separately loses cancellation.
The open task is a different coupled constraint or signed estimate that
retains both sectors, every endpoint, and the correct cutoff domain.

These are subproblems of one direction, not three established new
mechanisms. Choose one for a first bounded attempt.

## First task and gate

Write a short exact-observation contract: extra geometric/arithmetic input,
physical transform, complete signed expression, domain, boundary and
commutator terms, comparison target, and the control premise it uses.
Then derive the identity and isolate a specific estimate that could be
proved without assuming the desired nonvanishing. Only proceed to a
numerical or more elaborate geometric construction when this contract
identifies a concrete improvement to test.

A useful bounded outcome is a paid signed/boundary estimate with an
explicit constant, a lower complete error or matched cost, or a scoped
obstruction for the proposed transfer. Stop if the map returns only the
old Laguerre expression with its unknown sign, the physical curvature
term vanishes, the bound uses an uncontrolled auxiliary norm, or sector
splitting removes the required cancellation. The unchanged compact ASD
theta extension has known obstructions; do not reopen it without naming
which hypotheses are changed and what estimate that change supplies.

## Controls and output

All holomorphic collision controls admit the generic self-dual forms.
Square-series controls share many local theta-jet calculations; reflected
smooth controls share source parity. Only an actual complete arithmetic
identity or estimate distinguishes the theta application. Use the
[program control map][guide] and do not interpret generic calibrated
volume or Yang–Mills positivity as a physical signed margin.

Create `notes/`, `numerics/`, and `reviews/` here for a new attempt. Save
the exact map, every boundary/commutator term, chosen metric and frame,
failed premises, constants or counterexamples, source identities, and
actual model/effort. Return any useful signed estimate to S01 or S03.
Preserve the canonical Investigation 22 sources and the current chat's
existing registration, following the [guide][guide].

[guide]: ../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[review]: ../../reviews/14_HODGE_AND_MODULAR_SYMMETRY_ASSESSMENT_20261018.md
[note]: ../../notes/07_HODGE_MODULAR_DUALITY_AND_ROTATION_DEFECT_20261018.md
[jets]: ../05_covariant_theta_jets/README.md
[manifold]: ../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[metric]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md
[bridge]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md
[coupled]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/06_COUPLED_THETA_PRODUCT_AND_PARITY_SECTORS_20261015.md
[parity]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/07_PARITY_STRIP_CUTOFF_AND_FULL_STARTING_FACTOR_20261015.md
