# Compact surface sequences and the finite interval Weil program

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

**Classification:** synthesis of existing compact-surface and Weil
criteria, with an exact interval-to-circle comparison and a cap-extension
control. The proposed positive geometric comparison remains a target.
No new theta positivity, simplicity, or all-height estimate is established.

The user's suggestion has two concrete forms already connected to this
repository: compact real Jensen surfaces, and compact-circle spectral
models of the finite Weil form. Compactness can make global geometric
tools available. It does not remove the need to identify the complete
arithmetic form or to control what happens when a surface degenerates.
For the Weil route, convergence on each fixed compact test is enough;
a positive spectral gap uniform in the size of the geometry is unnecessary.

## 1 A sequence of compact surfaces already gives an RH formulation

[Investigation 22 Note 05][surfaces] constructs

\[
 f(z)=\xi(1/2+\sqrt z)=\sum_{k\ge0}\gamma_kz^k/k!,\qquad
 J_d(X)=\sum_{k=0}^d\binom dk\gamma_kX^k,
 \qquad C_g:\ y^2=J_{2g+1}(x).
 \tag{1}
\]

The square-root notation means the single-valued even power series.
Each coefficient is a complete positive theta moment. Here C_g means
the smooth projective normalization, including when the displayed
affine equation is singular. It is a closed compact complex curve
with its natural real involution. The inherited theorem is

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 b_0(C_g(\mathbb R))=g+1\quad\hbox{for every }g\ge1.
 \tag{2}
\]

Thus a sequence of compact manifolds, each with a specified real
structure, is already available. The prescribed number uses the original
degree 2g+1. Substituting the possibly smaller genus of the normalization
would lose information at singular models. Unmarked complex genus alone
does not distinguish real from nonreal branch points.

The source note proves the strict Jensen statement needed for (2) and
its compatibility with repeated zeros of f. The classical unshifted
Jensen criterion is also stated in [Griffin, Ono, Rolen and Zagier,
Introduction][jensen-paper]. There is no new equivalence claim here.

The limit preserves zero location more readily than zero separation:
J_d(z/d) tends locally uniformly to f, so real-rooted approximants give
an all-real limiting divisor, but distinct roots can merge. The inherited
control

\[
 f_*(z)=(1+z)\frac{\sinh(\pi\sqrt z)}{\pi\sqrt z}
       =(1+z)\prod_{n\ge1}(1+z/n^2)
 \tag{3}
\]

has a double at -1 while all its finite Jensen polynomials have distinct
negative roots. Its compact surfaces have the desired real-component
counts. It fails the canonical theta-coefficient premise, but shows why
(2) addresses RH and does not add simplicity to RH.

[BW15][bw15] already studies the quantitative degree limit. Its first
single-window acquisition comparison failed its specified speed target;
that does not rule out a new global identity or a separately specified
period observable. Repeating that computation is not the next step.

## 2 Heat transport remains meaningful on closed surfaces

For a fixed-degree polynomial family with distinct branch points,
continuation gives Gauss-Manin transport of homology. Closing the fibers
removes an outer spatial boundary, but a collision can still make a
fiber singular and collapse a cycle. Smoothness of every individual
normalized fiber does not make the whole normalized family smooth.

The inherited [surface-deficit calculation][deficit] makes this explicit.
For an odd polynomial Q of original degree 2g+1,

\[
 g+1-b_0(C_Q(\mathbb R))
 =\frac{N_{\rm nonreal}(Q)}2+
   \sum_{a\in\mathbb R:Q(a)=0}
              \left\lfloor\frac{\operatorname{mult}_aQ}{2}\right\rfloor.
 \tag{4}
\]

Under polynomial backward heat this deficit counts the remaining real
collision weight. Every fixed polynomial eventually has zero deficit.
That late-time fact is therefore insufficient. The uniform-degree
condition in the reciprocal Jensen hierarchy is already RH-equivalent.
Its auxiliary polynomial heat parameter is not physical theta heat time.
These distinctions carry the early-to-late lessons of [Note 18][n18]
into a compact setting without identifying different flows.

## 3 The Weil route admits a compact approximation strategy

The [project README][repo-readme] and [Weil-depth manuscript][weil]
already formulate the common target as positivity of Q_0 on every smooth
compactly supported complex test. Gamma, pole and prime contributions
are retained together. Exhausting all finite support intervals is enough;
there is no requirement that the finite-interval floors stay uniformly
above zero. The manuscript's diagonal proposition uses expanding support
and shrinking shift to express this fact in the transfer formulation.

For a proposed geometric version, specify closed compact manifolds M_j,
test maps I_j, and nonnegative energies E_j. A sufficient comparison is

\[
 Q_0[f]\ \ge\ E_j[I_jf]-\varepsilon_j[f],
 \qquad E_j[I_jf]\ge0,\qquad
 \varepsilon_j[f]\ge0,\quad\varepsilon_j[f]\longrightarrow0
 \tag{5}
\]

for each fixed compactly supported smooth f and all sufficiently large j.
Taking the limit gives Q_0[f]>=0. Exact convergence
E_j[I_jf] -> Q_0[f] is a stronger alternative. Neither requires convergence
uniformly over tests whose support grows with j. A fixed-support bound
epsilon_{j,L}||f||_X^2, with epsilon_{j,L}->0 for each L, would be a useful
way to supply the error. The test norm and the arithmetic matching must
be stated; no such estimate is supplied here.

Equation (5) is an elementary conditional specification, not an RH
milestone. A Hodge or Dirac norm is positive on many compact geometries;
the research content is a source-derived comparison with the complete
Weil form. Defining the energy by first assuming that form positive would
not construct the desired mechanism. Similarly, replacing a finite
self-adjoint form W by W-lambda_min(W)I creates a nonnegative form but
leaves a scalar correction to recover W; it supplies no sign for W.

There is a direct literature connection. [Connes and Consani][cycles]
construct spectral triples on circles of varying length from finite
Weil data. [Connes, Consani and Moscovici][ccm-paper] develop periodic
scaling-operator perturbations; their Theorem 1.1 is conditional on a
simple even lowest Weil eigenvector. Their Section 8 identifies that
ground-state condition and the required approximation to the true
ground state as missing steps. These constructions motivate the
comparison, rather than completing it.

The repository's [CCM investigation][ccm] has already tested strings,
graph operators and related realizations. Its specific threshold-energy
obstruction and continuation gate remain in force. A new one-sided
signed comparison or a different estimate on the physical complement
would be a substantive new input; a further realization of the same
positive finite pencil would not be one.

## 4 Closing an interval changes its prime translations

Here is an exact comparison before constructing any new geometry.
Work on L^2(0,P), with inner product antilinear in the first variable.
For 0<a<P let

\[
 (T_af)(x)=\mathbf1_{(a,P)}(x)f(x-a),\qquad
 (U_af)(x)=f((x-a)\bmod P).
\]

T_a is the zero-extended interval delay; U_a is the circle translation.
Their difference is the seam operator

\[
 U_a=T_a+W_a,\qquad
 (W_af)(x)=\mathbf1_{(0,a)}(x)f(x-a+P).
 \tag{6}
\]

Consequently, replacing the interval prime term
-c_a(T_a+T_a^*) by -c_a(U_a+U_a^*), where
c_a=Lambda(n)/sqrt(n)>0 and a=log(n), changes the form by

\[
 \delta Q_a[f]=-2c_a\operatorname{Re}
            \int_0^a\overline{f(x)}f(x-a+P)\,dx,
 \qquad
 |\delta Q_a[f]|\le2c_a
 \|f\|_{L^2(0,a)}\|f\|_{L^2(P-a,P)}.
 \tag{7}
\]

This correction has both signs. For 0<a<P/2, choose a unit smooth
function h supported inside (0,a), and put k(x)=h(x-P+a), supported
inside (P-a,P). For f_+=(h+k)/sqrt(2) and f_-=(h-k)/sqrt(2),
equation (7) gives delta Q_a[f_+]=-c_a and delta Q_a[f_-]=+c_a.
This is an exact analytic control, not a numerical experiment.

Localization can eliminate this particular error for each fixed finite
set of delays: if f vanishes on the relevant seam collars, W_a contributes
zero. That is useful for a fixed-test limit. It does not bound a complete
growing family of prime translations or the archimedean and pole changes.
Using periodic Fourier functions as a basis for the original zero-extended
form also does not replace T_a by U_a: a basis change preserves the seam
information in the matrix. In particular, (7) is not an assertion that
the cited CCM construction dropped its interval terms.

The scoped conclusion is that naive delay periodization has no universal
one-sided comparison with the interval prime term. It is not an exclusion
of compact spectral models or of a signed complete-form cancellation.

## 5 Capping the charge boundary retains its obstruction

There is an equally direct check on the BW12 side. Let Omega be a
four-ball in complex heat spacetime, and suppose G=(H,H_z) is nonzero
on its boundary. Its normalized boundary map g:S^3->S^3 has degree Q.
Attach a second four-ball to make S^4. If the same trivial rank-two
bundle admits a nonvanishing extension of G throughout the cap, its
normalization extends g over a ball. Hence g is null-homotopic and Q=0.
Conversely degree zero permits such a continuous nonvanishing cap map;
it does not prescribe a holomorphic heat extension.

Thus a nonvanishing cap in this specified construction is already the
zero-charge condition, not a consequence of closing the base manifold.
For H(t,z)=z^2-2t the isolated jet zero has complex degree one, so this
cap cannot be nonvanishing. One can instead allow zeros in the cap or
change the bundle, but then the extra zero or bundle data must be kept.
No conclusion about all compactification methods follows from this test.

The Hopf boundary S^3 is itself already a closed manifold. The existing
boundary difficulty concerns control of the map on it and its extension,
not a boundary of that S^3. Similarly, ordinary holomorphic scalar
functions on a connected closed Riemann surface are constant; the Jensen
construction uses meromorphic coordinates and marked branching. Closing
a surface reorganizes these data rather than discarding them.

## 6 The next useful comparison

The two routes serve different purposes. The Jensen family already
answers the existence question for a compact-surface RH formulation.
A new theta relation forcing its marked real topology, or controlling
period degeneration, would be useful; generic finite smoothness would not
settle the BW12 simplicity question.

For a return to the shifted-zeta positivity objective, the more direct
test is a compact-circle energy with an explicit source map and the
full signed interval-to-circle discrepancy. Seek (5) for each fixed
support, first identifying all prime, gamma and pole terms. The first
deliverable should be an actual one-sided estimate for that discrepancy
or a specified obstruction, not an additional geometry or numerical
support sweep. Equations (6)-(7) supply the elementary seam comparison
that any literal delay-periodization candidate must pass.

This continuation preserves the [result index][results] and
[avoid index][avoid], especially [criterion classification][a01],
[geometric realizations][a03], [factor identification][a13] and
[scoped conclusions][a07]. The [collision controls][controls] remain
applicable to any later theta exclusion claim. Positive-source or
reflection assumptions alone are not an identified compact positivity
mechanism: Euler-factor controls change the canonical arithmetic;
weighted-square controls lack the complete normalized reflection
conjunction; reflected/primitive controls lack the canonical square
coefficients. Those separate preservation lists are not combined.

Verification here consists of reading the inherited proofs and directly
checking the seam identities and cap obstruction. No new theta numerical
acquisition or independent review was performed. FTSR-00–07 and the
sibling BW15/CCM continuation gates are unchanged.

[surfaces]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md
[deficit]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/07_REAL_PROJECTIVE_JETS_AND_JENSEN_HEAT_SURFACES_20261015.md
[bw15]: ../../15_jensen_surface_degeneration/research-overview/01_JENSEN_SURFACE_DEGENERATION_PROGRAM_20261021.md
[n18]: 18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md
[repo-readme]: ../../../../../../../README.md
[weil]: ../../../../../../weil-positivity/shifted-zeta/weil-depth/manuscript/finite_horizon_weil.tex
[ccm]: ../../../../../../investigations/ccm-operator-realizations/README.md
[jensen-paper]: https://arxiv.org/html/1902.07321
[cycles]: https://arxiv.org/abs/2106.01715
[ccm-paper]: https://arxiv.org/html/2511.22755
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a13]: ../../../../../../../avoid/13_a_factor_is_not_the_target.md
