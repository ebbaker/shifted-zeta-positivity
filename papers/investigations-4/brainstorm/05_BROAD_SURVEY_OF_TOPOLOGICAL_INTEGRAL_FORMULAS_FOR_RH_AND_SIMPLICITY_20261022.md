# Topological integral formulas beyond the Chern–Hopf comparison

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified from this conversation's turn metadata.
Three contributing agents audited the three requested source collections;
their checks are internal, same-model LLM work, not independent specialist
review. No novelty or priority claim is made.

**Status: comparative research summary with explicit classical identities
and elementary screening calculations. No new theta-specific integral
bound, RH result, or simplicity exclusion is established.** The purpose is
to choose useful integral consumers and estimating mechanisms, beyond the
direct Chern–Hopf comparison already completed in [shared Note 05][i4n5].

## 1. Findings and priorities

There are worthwhile alternatives, but they offer different kinds of help.
The most promising *near-term estimator* is weighted Green localization.
The cleanest alternative *collision-count integrand* is a compactly
supported real degree/Thom integral. The most interesting *different
degeneration observable* is the full energy of the reciprocal differential
on a spectral double cover, evaluated through Riemann bilinear relations.
The last detects a divergence that bounded Gauss mass does not detect.

| Priority | Formula and actual consumer | What would constitute a useful result | Present assessment |
| --- | --- | --- | --- |
| 1 | Weighted Green/Poincaré–Lelong: localized spatial Gauss mass, including multiplicity atoms | A tighter complete weighted bound from correlated canonical-source information than direct density integration | Closest to an existing paid consumer; §3 |
| 2 | Compact real Thom/degree integral: physical spacetime collision count | A cheaper or sharper signed bulk enclosure than complete boundary winding, on identical data | Exact finite-scale identity without an inverse-energy denominator; §4 |
| 3 | Riemann bilinear relations for reciprocal-form energy | An independently obtained upper energy or dual-period bound that controls logarithmic degeneration | Most distinct simplicity observable; its upper bound is completely unpaid; §5 |
| Supporting | Extremal length/capacity on the degenerating collar | A paid conformal-modulus or energy bound | Quantitative partner of priority 3, not a separate sign mechanism; §5 |
| Secondary | Spherical area formula / Robin-pencil averaging | Independently cheaper counts or weighted bounds for a selected Gauss-area region | Exact representation, but costs more counting information; §6 |
| Existing alternatives | Signed Laguerre localization, physical phase transport, Schur-ratio boundary energy | A new full-source signed estimate for their already identified targets | Mature consumers to retain, not rediscover; §7 |
| Reserve | Lefschetz/trace, operator-index, Bochner and Gauss–Bonnet programs | A new density/operator bridge and a usable complete inequality | No ready replacement for the missing arithmetic estimate; §8 |

For the immediate task I recommend **one weighted Green comparison**. For
a broader new research direction, I recommend **reciprocal Hodge energy**,
after first specifying its boundary and period acquisition contract. A
real Thom pilot is attractive if the objective is acquisition cost or
replacement of a difficult phase boundary by a localized bulk integral.
These are recommendations for bounded tasks, not evidence for their success.

For RH directly, a finite-domain collision estimate still needs the
existing threshold argument, confinement/no-escape hypotheses and coverage
of all relevant heights; the full-Weil and all-degree Jensen routes have
their own global quantifiers. For RH → simplicity, the all-real
positive-time regime is an input from RH, while the singular t↓0 limit
remains to be controlled. A formula valid on each t>0 slice does not by
itself settle that limit.

The [result index][results] and [avoid index][avoid] govern this assessment.
In particular, consult [collision controls][controls], [heat geometry][geom],
[arithmetic bookkeeping][arithmetic], [geometric realizations][realizations],
and avoid patterns [01][a01], [02][a02], [03][a03], [07][a07], [12][a12],
[13][a13], [15][a15] and [20][a20]. An equivalent criterion is classified
once; testing it on examples is not progress toward its proof. A new
representative of an old invariant earns its place through an estimate or
cost advantage, rather than through a new name.

The three leading directions now have separate organizational homes:
[07 Weighted Green](../07_weighted_green_integrals/README.md),
[08 Real Thom/degree](../08_real_thom_degree_integrals/README.md), and
[09 Reciprocal Hodge energy](../09_reciprocal_hodge_energy/README.md).
Each owns its detailed future-task register. This 22 October setup is
organizational; all first research contracts remain Unstarted, and none
of the formula-level assessments or inherited stops below is upgraded.

## 2. What the survey covered, and what is already closed

The audit followed the indices and current source/review chains across
the requested collections, with targeted reading of the formulas and
latest objections. It was not a line-by-line rereading of every archived
conversation or generated numerical record. Source statements and scoped
reviews prevail over overview wording.

| Collection | Coverage and relevant findings |
| --- | --- |
| Threshold routes BW01–08 | Local double/all-multiplicity winding, later nonreal/collision/Laguerre routes, derivative and deflated-jet reductions. Local forward splitting supplies no later negative witness; finite moments, positive sources and finite profile observations retain explicit collisions. |
| BW09 | Root-wall cap counts, signed Laguerre averages, exact real regularized degree integral, and failed specified Gaussian-cap comparison. These already provide non-Hopf formulas. |
| BW10 | RH → simplicity targets: signed physical tubes, critical-wall amplitudes, reciprocal/Dirichlet approximation energies, root motion, Gauss-area concentration and the original spectral-cover proposals. Different norms and multiplicity weights must be kept separate. |
| BW11–12 | Global jet geometry and relative charge/signed reconstruction. Resolved curvature disks and complete signed covariance have explicit direct comparators. This survey uses BW12 as an interface, not as a new Chern–Hopf project. |
| BW13–15 | Spectral periods, canonical-source constraints and Jensen degeneration. First local nodal coefficient is existing four-jet information; finite nonlocal periods remain open. Finite Jensen strictness does not prevent limiting multiplicity. |
| Investigation 22 | All physical-jet geometry themes: stationary and marked topology, real/complex multiplicities, wall flux, signed turning/chords, theta connections and arithmetic identities, collision controls and outer estimates. The consolidated reviews distinguish actual geometry from the still unpaid signed physical observation. |
| Investigations 4, homes 01–06 | Compact Weil circle comparison; canonical source; currents and charges; periods; Jensen surfaces; complete signed reconstruction. Shared notes, overviews, registers and current reviews were included. The current source-input priority and reserve/gated statuses are preserved. |

Useful entry points are the [threshold-route index][bw], [Investigation
22][inv22], [Investigations 4][i4], [BW10 notes][bw10notes], [BW13][bw13]
and [BW15][bw15]. Two especially important stops are:

* [Shared Note 05][i4n5] and [Review 06][i4r6] prove that the **existing
  global inverse-Schur certificate** loses to the direct Green certificate
  by a factor exceeding 707 for **every finite regulator**, on the stated
  sufficient ordinary-double window. This is a comparison of certificates,
  not of the actual integrals. Do not repeat regulator optimization in
  that class. Localized or source-dependent comparisons remain outside it.
* [BW13 Note 01][period] shows that the first correction to the local
  vanishing period is determined by the same event four-jet already used
  directly. Its reviewed stop concerns that coefficient comparison, not
  every period or energy observable. The reciprocal cycle period itself
  is also already present there and in [BW10 proposal C4][globalideas].

## 3. Weighted Green formulas: localize the actual Gauss consumer

Fix a real time and a bounded smooth spatial domain Ω, with H holomorphic
near its closure and not identically zero. Write

\[
 E=|H|^2+|H_z|^2,\quad u=\log E,\quad
 g_2={|HH_{zz}-H_z^2|^2\over E^2}.
\]

At common zeros use the **original vector jet**, before canceling its
common factor. The completed measure, with a normalization explicit here,
is

\[
 d\nu={1\over4\pi}\Delta u
      ={g_2\over\pi}\,dA_z+\sum_a(m_a-1)\delta_a.       \tag{G1}
\]

The first term means the regular density away from common zeros, extended
as a locally integrable density. Indeed, at an m-fold zero,
E=|z-a|^{2(m-1)}\widetilde E with positive smooth \(\widetilde E\).
Thus the logarithmic factor contributes exactly m−1 to (G1).
This is [BW10 GA1–GA7][gauss] in normalized distributional form; it must
not be confused with the canceled projective map's regular area alone.
The classical logarithmic-zero identity is recorded in [Oh, Remark
4.31](https://web.math.berkeley.edu/~sjoh/pdfs/notes-math222a.pdf).

For a real C² weight ψ and a boundary without common zeros, Green's second
identity gives the following direct extension of the existing unweighted
formula:

\[
 \boxed{\int_\Omega\psi\,d\nu
 ={1\over4\pi}\int_{\partial\Omega}
       (\psi\partial_nu-u\partial_n\psi)\,ds
  +{1\over4\pi}\int_\Omega u\Delta\psi\,dA_z.}          \tag{G2}
\]

This follows distributionally from (G1), or by excision and retention of
the small-circle terms. For ψ compactly supported, only the last integral
remains. For ψ=1 it returns the established spatial Green baseline.
Consequently a localized target can be attacked directly, with no
four-dimensional inverse-Schur comparison.

**Potential use.** Select ψ for one named spatial error region or weighted
Gauss consumer, and compare (G2) with the completed direct target
∫ψg₂/π dA+Σ_a(m_a−1)ψ(a), or with density integration on a regular
slice, using the same source data. A smaller error allowance would be useful even
without excluding a collision. A prescribed positive weight can also
retain a known multiplicity quantum instead of letting it disappear in
projective cancellation.

**Unpaid estimate.** Compactly supported Δψ generally changes sign.
Upper bounds on E alone do not give an upper bound for the complete
right side: its negative-weight part also needs lower/logarithmic
information. Separate absolute payments can destroy the desired gain.
The natural input is a *coupled* enclosure of the weighted log energy,
not an assumed interior jet floor.

One can similarly apply Poisson–Jensen to a holomorphic critical value
V(τ)=H(τ,c(τ)), where H_z(τ,c(τ))=0 and H_zz≠0. On a disk of radius R
centered at τ₀, with V(τ₀)≠0 and no boundary zeros,

\[
 {1\over2\pi}\int_0^{2\pi}\log|V(\tau_0+Re^{i\theta})|d\theta
 -\log|V(\tau_0)|
 =\sum_j n_j\log{R\over|\tau_j-\tau_0|}.                \tag{G3}
\]

Along the real critical branch V′/V=−H_xx/H=q, so this addresses the
same logarithmic amplitude as ICW. It does not remove it: after translating
an ordinary endpoint to t=0, its zero contributes q=1/t+O(1). A useful Jensen bound must pay the
basepoint value and complete boundary logarithms. It cannot assume the
unknown endpoint value is nonzero. See [McMullen's Jensen formula](https://abel.math.harvard.edu/~ctm/home/text/class/harvard/213a/06/html/home/course/course.pdf).

Neither (G2) nor an area average controls a moving real-curve trace by
itself. In [Note 05][i4n5], g₂=q² on the real critical wall, but the trace,
sign and singular endpoint payments remain distinct. A new trace estimate
must name its function class and constants.

## 4. Real Thom/degree integrals: a different finite-scale collision estimator

Use real spacetime, oriented by dt∧dx, and the fixed physical frame

\[
 F=(H,H_x),\quad E_R=H^2+H_x^2,\quad
 \mathcal L_1=H_{xx}^2-H_xH_{xxx},\qquad H_t=-H_{xx}.
\]

Take D bounded with piecewise smooth oriented boundary, H real analytic
near its closure, no identically zero spatial slice, and F nonzero on ∂D.
The existing physical index theorem gives, for its isolated finite-order events,

\[
 {1\over2\pi}\oint_{\partial D}\beta=-K(D),\quad
 \beta={H\,dH_x-H_x\,dH\over E_R},\quad
 K(D)=\sum_{p\in D}\lfloor m_p/2\rfloor.                \tag{T1}
\]

See [Investigation 22 Note 04][realindex] and [Note 06][wallflux].
The associated regularized bulk formula is already in [BW09 Note 05,
equation (9)][bw09energy]. The following compact-support specialization
is a useful alternative representative of this same invariant.

Choose 0<b<min∂D|F| and a nonnegative smooth density ρ supported in the
target ball B_b(0), with integral one. Since
det D_(t,x)F=H_xH_xxx−H_xx²=−𝓛₁, the degree formula gives

\[
 \boxed{\int_D\rho(H,H_x)\mathcal L_1\,dt\,dx=K(D).}     \tag{T2}
\]

The standard input is the compactly supported pullback formula for
degree; see [Guillemin–Haine, §3.6](https://math.mit.edu/classes/18.952/spring2013/docs/book.pdf).
Restrict to F⁻¹(B_b), where the map is proper over the ball and the degree
is constant. This proves (T2) without a limiting regulator, complex time,
or an inverse physical-energy denominator.

**Potential use.** A complete upper enclosure strictly below one excludes
events in D; an enclosure narrower than direct winding could also be an
estimator improvement. Localizing the bulk near small jets might reduce
acquisition cost on some domains. The integrand is signed: 𝓛₁ need not
be nonnegative for an arbitrary heat field. Do not replace this by an
unjustified positivity claim.

**Actual costs.** The full boundary floor is still needed to choose b.
A rescaled target cutoff has size of order b⁻² and corresponding derivative
costs. The nonlinear localization and cancellations must be enclosed from
the same canonical source. A boundary method might remain cheaper. The
existing [theta winding pilot][wallflux] used 698 boundary enclosures
versus 255 for its practical direct interior baseline; that is a finite
comparison, not a universal verdict on either method.

There is also an exact finite-Gaussian allowance. For λ>0, put

\[
 I_\lambda={\lambda\over\pi}\int_D e^{-\lambda E_R}\mathcal L_1\,dt\,dx.
\]

Because (1−e^(−λE_R))β extends smoothly across F=0, Stokes yields

\[
 I_\lambda=K(D)+{1\over2\pi}\oint_{\partial D}e^{-\lambda E_R}\beta,
\qquad
 |I_\lambda-K(D)|\le {e^{-\lambda b^2}\over2\pi}
                       \oint_{\partial D}|\beta|.       \tag{T3}
\]

This is a derived estimator identity, not a theta bound. The infinite
Gaussian support is why its boundary correction cannot be dropped.

For comparison, let W be a bounded domain in C²_(τ,z), with H holomorphic
near its closure and both domain and target carrying complex orientations.
The complex jet G=(H,H_z) has det_C DG=J=H_zH_zzz−H_zz².
A nonnegative normalized target density φ
compactly supported below min∂W|G| gives the analogous positive formula

\[
 \int_W\phi(G)|J|^2\,dV=\deg(G,W,0).                  \tag{T4}
\]

This is the complex area/degree formula, with multiplicities, rather than
a new characteristic number. A localized signed error could potentially
be paid using this measure. It cannot dominate an arbitrary Gauss target
outside its support: H=z already has positive Gauss density and J=0.
The real version (T2) is the more direct alternative to the present
four-dimensional program.

**Endpoint caveat.** An integral on 0<t≤T misses an event at t=0. For
RH → simplicity, enclose the endpoint with both signs of time, or retain
and pay the corresponding relative boundary contribution. RH supplies
no zero collision count at negative time. The precise exclusion threshold
below one is an existing integer-count criterion, not a new theorem
toward RH.

## 5. Reciprocal Hodge energy and Riemann bilinear relations

This is the strongest candidate for a genuinely different *observable*.
On a smooth finite double cover X_t of a spatial domain,

\[
 w^2=H(t,z),\qquad \omega_t={dz\over w},\qquad
 \mathcal E_t={i\over2}\int_{X_t}\omega_t\wedge\bar\omega_t
             =2\int_\Omega {dA_z\over|H(t,z)|}.          \tag{R1}
\]

At a simple branch point ω is regular in the square-root coordinate, so
this integral is locally finite. It has a different multiplicity response
from the bounded spatial Gauss mass. The reciprocal cycle integral was
already considered in [BW10 C4][globalideas] and [BW13 equations (9),
(11)][period]; the proposed consumer is its **full energy or pairing with
dual periods**, not that previously recorded cycle integral.

For a compact smooth surface and a holomorphic differential ω, with
symplectic periods A_j,B_j, the classical bilinear relation is

\[
 \boxed{{i\over2}\int_X\omega\wedge\bar\omega
       =\sum_{j=1}^g\operatorname{Im}(\bar A_jB_j).}     \tag{R2}
\]

See [Riemann Surfaces and Integrable Systems, §3.1.2](https://people.sissa.it/~grava/RS2021.pdf).
It permits an energy to be evaluated through *paired*, rather than
separately positive, period data. On compact smooth odd-degree Jensen
curves y²=J_(2g+1)(x), g≥1, dx/y is holomorphic and (R2) applies.

For the finite physical cover, retain its boundary. On a cut domain where
dF=ω, the exact identity is

\[
 \mathcal E={i\over2}\int_{\partial X_{\rm cut}}F\bar\omega.       \tag{R3}
\]

Paired cut edges recover the period terms; every unpaired outer boundary
arc remains. Meromorphic compactifications require their pole/excision
terms. The entire theta cover is not itself a compact finite-genus curve.
One cannot cap it and retain (R2) unchanged.

### An explicit degeneration lower bound

The following screening calculation is elementary and is included to
identify the scale any upper estimate must beat. Recenter a local pair as

\[
 H(z)=(z^2-a^2)U(z),\qquad |U(z)|\le M,\qquad 0<2|a|<R.
\]

On 2|a|≤|z|≤R, |H|≤(5/4)M|z|². Its two-sheet preimage therefore gives

\[
 \boxed{\mathcal E\ge {16\pi\over5M}\log{R\over2|a|}.}    \tag{R4}
\]

Indeed integrate 2·4/(5M|z|²) in polar coordinates. If an independently
proved complete upper bound \(\mathcal E\le B\) were uniform in the
endpoint limit, then

\[
 |a|\ge {R\over2}\exp\!\left(-{5MB\over16\pi}\right).    \tag{R5}
\]

For an endpoint-uniform consequence, R must be fixed and M and B uniform
over the family, with U holomorphic and nonvanishing on the pair chart.
No such theta upper bound is obtained here. The quadratic H=z²−2t has
a=√(2t), U=1 and logarithmically diverging energy as t↓0, while retaining
bounded Gauss mass, a nonvanishing exterior jet and a perfectly valid
reciprocal cycle period. Those weaker inputs cannot supply B.

More generally, near H=(z−a)^mU with U(a)≠0, (R1) has radial behavior
\(\int r^{1-m}dr\): finite for m=1, logarithmically divergent for m=2,
and more strongly divergent for m>2. Local reciprocal integrability thus
rephrases simplicity for a holomorphic field. This equivalence is stated
once; it is the **source-paid upper estimate**, not the equivalence or
its checks, that would constitute progress.

### Capacity explains the missing quantitative input

For a round annulus A(r,R),

\[
 \operatorname{mod}A={1\over2\pi}\log(R/r),\qquad
 \operatorname{cap}A={2\pi\over\log(R/r)}.
\]

The second expression uses the Dirichlet energy of a harmonic function
with boundary values 0 and 1, without a factor 1/2. For a closed real
one-form α with period p around the annulus, circlewise Cauchy–Schwarz
gives

\[
 \int_A|\alpha|^2\,dA\ge {p^2\over2\pi}\log(R/r).        \tag{R6}
\]

The modulus convention is [McMullen, §6](https://people.math.harvard.edu/~ctm/papers/home/text/class/harvard/219/course/course.pdf);
the displayed energy inequality follows by integrating the circlewise
bound p²/(2πs). This is a quantitative mechanism for degeneration, but
topology alone gives no upper bound on modulus or energy.

**Bounded task.** On one finite cover, compare all period/boundary costs
in (R3) with direct same-source evaluation of ∫|H|⁻¹. Specify the
normalization and how singular neighborhoods are paid. On canonical
Jensen curves, also pay the scaled limiting transfer: all finite curves
can be strictly hyperbolic while the limiting entire function has a double
zero. Neither positive Im(period matrix) nor finite simple branch points
prevents that degeneration. This remains a research reserve, not an
activated global proof program.

## 6. Spherical area and Robin-pencil averaging

For the canceled meromorphic projective coordinate p=H_z/H,

\[
 \int_\Omega {|p_z|^2\over(1+|p|^2)^2}\,dA_z
 =\int_{\mathbb{CP}^1}N_\Omega(\lambda)
                   {dA_\lambda\over(1+|\lambda|^2)^2}.  \tag{A1}
\]

Here the target measure has total area π, and N counts preimages with
multiplicity. For finite λ the relevant pencil is H_z−λH, with the
persistent common divisor removed; add the (G1) atom when the original
jet has a common zero. The area formula is the relevant classical input;
see [Eremenko, §2](https://www.math.purdue.edu/~eremenko/dvi/ahl.pdf),
whose spherical area is normalized to one rather than π.

This could be useful if particular direction counts, or their weighted
average, are cheaper to certify than the source density. Apply it to a
specified domain/sector and compare with (G2). Ordinary polynomial degree
gives a finite compact budget; an entire theta exhaustion needs its own
count and boundary payments. Selecting λ=0 does not turn an average over
all directions into the critical-wall trace. (A1) preserves neither that
trace nor the required physical orientation automatically.

## 7. Existing signed integral consumers worth retaining

These are alternatives to a new characteristic-class program, but the
repository already knows them.

**Laguerre localization.** With Q=H_x²−HH_xx and ψ≥0 compactly supported,

\[
 \int\psi Q\,dx=2\int\psi H_x^2\,dx
                        -{1\over2}\int\psi''H^2\,dx.   \tag{S1}
\]

This can reduce derivative acquisition, and a negative complete integral
would supply a negative Laguerre witness. [BW09 Note 05][bw09energy]
already establishes it and its screens: the unweighted integral is
nonnegative, and any test with nonnegative cosine transform is also
nonnegative for every admissible positive source. An origin-centered
Gaussian therefore cannot give the desired negative witness. A useful
task needs an explicit event-centered weight, a later window outside
the known local positive region, and a full signed two-source estimate.

**Physical phase transport.** Where E_R>0, set ρ=Q/E_R and j=Q_x/E_R.
Then ρ_t+j_x=0; this asserts no source-free conservation across collisions.
The complete moving-root-wall calculation gives mass π in
an adjacent simple gap; the outer cap through m split roots is
(m−1)π. These are [BW09 cap identities][rootcaps] and [BW10 tube
formulas][tubes], with every wall, transverse face and trace error retained.
Smooth phase walls and bounded speed can coexist with endpoint collision.
The scalar current 2H_x/H has a different survival obligation; it cannot
be substituted for phase transport.

**Critical-wall amplitude and signed observation.** The ICW consumer is
\(\log(B(T)/B(\epsilon))=\int_\epsilon^Tq(t,c(t))dt\).
On H_x=0, q=C₂/C₀ and S₁=0; the signed upper comparison is
σ(C₂−kC₀)≤0, σ=sign C₀. Investigation 22 also has the signed
observation target WB_∂≤CW²+ε|W| on prescribed stationary cones.
New Hodge/Green/adjoint identities should be judged against these complete
consumers, not a positive auxiliary source norm. The canonical-source
supplier is [home 02][sourcehome]; the current survival/amplitude scope is
in [ICW Note 02][icw].

**Schur/Herglotz boundary energy under RH.** Write
F(z)=ξ(1/2+z), R_ε(z)=F(z)/F(z+ε). The complete ratio energy satisfies

\[
 \lim_{\epsilon\downarrow0}{1\over2\pi\epsilon}
 \int_{\mathbb R}{|1-R_\epsilon(it)|^2\over\sigma^2+t^2}\,dt
 =\sum_\lambda{c_{m_\lambda}\over\sigma^2+\lambda^2},\qquad
 c_m=m\left(1-{\binom{2m}m\over4^m}\right).             \tag{S2}
\]

Here σ>0, and λ ranges over distinct signed ordinates of zeros iλ, with
multiplicities m_λ. See [BW10 Note 15][ratio] for the hypotheses and
complete infinity payment. This is a concrete multiplicity-sensitive
integral. An opposing arithmetic upper bound could be useful; positivity
and contractivity alone do not provide it. Do not transfer a bound from
a changed heat completion or compact norm without its already identified
arithmetic and tail costs.

## 8. Broader formulas: where their missing inputs lie

| Family | Why it does not currently supply the needed bound |
| --- | --- |
| Gauss–Bonnet / Riemann–Hurwitz / Euler counting | Useful for exact curvature and branch bookkeeping. The established Gauss defect is finite, π(m−1), and curvature defect −2π(m−1). Bounded total area/curvature therefore permits a collision. Uniform integrability or a stronger norm would be additional analytic input. |
| Bochner–Kodaira, Weitzenböck, Reilly identities | Potential sources of energy/trace inequalities only after specifying the metric, constrained section space and boundary payments. Investigation 22's [connection][connection] and [coordination analysis][coordination] already find flat physical pullbacks and infinite ambient action. The latter gives a compact Kähler obstruction to retaining simultaneously a smooth ASD Chern connection, the degree-one theta line bundle and its nonzero holomorphic section. Generic ambient positivity does not bound the signed physical path observation. These are scoped stops, not exclusions of every constrained PDE estimate. |
| Atiyah–Singer / APS, Mathai–Quillen, Bott localization | A compact Thom representative is already concrete in §4. A further operator-index route must supply the elliptic operator, symbol/Fredholm domain, density bridge and all boundary/eta corrections. An index identity alone supplies no signed arithmetic estimate. Operator heat-kernel time is distinct from physical theta heat time. |
| Lefschetz/Hodge interpretation of the full Weil form | The [Connes–Consani–Marcolli trace-pairing formulation](https://arxiv.org/abs/math/0703392) is relevant background, but positivity of its relevant pairing is precisely the unresolved RH input. In I4 home 01 the [complete circle comparison][circle] is already exact with fixed-test errors; literal circle positivity and specified repairs fail. Any new positive energy must represent the complete gamma, pole and prime form and prove the required one-sided comparison. |
| Equivariant Lefschetz trace on smooth Jensen surfaces | The real locus is a union of circles, so its Euler characteristic is zero independently of the number of ovals. An ordinary alternating Lefschetz trace therefore cannot recover the required g+1 components. Marked cycles or full real/Smith–Betti information, followed by quantitative bounds, would be needed. See the existing [Jensen topology][jensen] and [polynomial-heat continuation][jensenheat]. |
| Maslov index / spectral flow / residues | A new operator or pairing can bring useful analytic estimates. Merely renaming the existing real-loop winding, complex intersection number or discriminant residue does not add information. No suitable additional operator estimate has been acquired in this survey. |

For a full-Weil route, a mathematically meaningful contract would be an
actual positive energy E_N[f] and a proved one-sided comparison, or a
vanishing complete error as N→∞ for every fixed test f. The identity of
the full target is essential: a separately positive gamma sector or a
curve with positive period matrix does not identify that form. This is
the existing I4-W gate, not a new criterion milestone.

## 9. Collision controls and distinct multiplicity weights

All identities above are intended to hold at matching collisions. They
are not themselves exclusion mechanisms. The relevant screen from
[cluster 12][controls] is:

| Control | What it tests, and what would have to distinguish a theta estimate |
| --- | --- |
| H=z | Positive spatial Gauss density with J=0; prevents generic domination by complex-jet degree mass. It is not an ordinary double and does not meet a nonzero determinant event contract. |
| H=z²−2t and the neighboring-root quartic | On local windows enclosing only the ordinary double: real count one, complex charge one, finite Gauss mass, nonvanishing outer contours, smooth local phase walls and logarithmic reciprocal-energy divergence. Conserved total zero multiplicity or bounded area does not preserve simplicity. They lack the unchanged arithmetic theta source. |
| Euler-factor controls | Positive even source and substantial analytic structure can retain positive-time collisions. Original Euler coefficients/completion change. Generic positivity or local topology does not distinguish them. |
| Weighted-square / finite-prime controls | Square support, selected arithmetic identities and finitely many measurements can retain collisions. Full normalized reflection/unchanged coefficients fail. Finite-source controls have no all-real heat slice; do not assign them an RH product sign. |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | Strong reflection, positivity, decay or primitive endpoints do not suffice. Their unchanged normalized integer-square theta expansion fails. Keep each control's preservation list separate. |
| RH-conditional close endpoint controls | Can preserve all-real positive-time behavior, displayed completion and very close positive source data yet have endpoint doubles. Ordinary Dirichlet-series arithmetic fails. They directly screen an attempted RH → simplicity argument using only those analytic data. |
| Earlier counter-kernels and full-Weil controls | Apply each only to its established analytic event or form class. A heat event is not assigned to every Weil control. A proposed full-Weil transfer needs its own exact bridge and matched premise screen. |

No new exclusion estimate is claimed, so no control is declared rejected
by a numerical test. For any future claimed exclusion, name the specific
premise or proved quantitative bound that the matching control fails.
Full theta reflection together with unchanged normalized coefficients
identifies the intended source in the proved rigidity class; identifying
it is not the missing signed estimate.

Keep the normalizations distinct:

| Observable | Contribution associated with an m-fold spatial zero |
| --- | --- |
| Real spacetime physical index | −floor(m/2) |
| Complex heat/spatial jet intersection | m(m−1)/2 |
| Completed spatial Gauss measure | π(m−1), or m−1 in (G1) |
| Real outer split-root cap | (m−1)π under its stated cap geometry |
| Reciprocal differential energy | Locally finite at m=1; logarithmic divergence at m=2; stronger divergence for m>2 |
| Completed-ratio boundary coefficient | c_m in (S2), rather than m² |

These different quantities cannot be identified by a thin-domain limit or
by the fact that each detects some aspect of multiplicity.

## 10. Recommended bounded follow-ups and disposition

1. **Weighted Green estimator:** select one explicit bounded spatial ψ
   and a named Gauss/error consumer. Retain its atom and every term in
   (G2). Compare a coupled log-energy enclosure with direct density
   integration on the same full-source data. Stop if the sign-changing
   log payment costs as much as the direct target. Do not add a numerical
   campaign before this comparison is specified.
2. **Alternative real count estimator:** choose an already paid spacetime
   domain and compare (T2) or (T3) with complete winding. Charge the
   boundary floor, cutoff resolution, signed products and source tails.
   Success can mean a narrower enclosure or reduced acquisition, even
   without a new excluded region. Endpoint simplicity needs its extra
   relative/negative-time treatment.
3. **Broader simplicity pilot:** specify one finite cover and the complete
   (R3) period/boundary contract. Determine whether canonical-source
   information controls its energy more effectively than direct reciprocal
   integration. The logarithmic obstruction (R4) is the calibration.
   Mere finite t>0 integrability, or finite-degree Jensen strictness, fails
   the endpoint-uniform objective.

This survey leaves CHB-07's scoped Note 05 failure, the ICW survival/sign
gates, and I4 homes 04–06 reserve/gated statuses unchanged. It does not
reopen the same-four-jet period comparison, the failed terminal-floor
survivor comparison, or the failed specified compact-Weil repairs.

The formula-level outcome is concrete: (G2) gives a weighted boundary/log
representation of the actual Gauss target; (T2) gives an exact finite-scale
real collision integral; and (R1)–(R4) identify a period-energy consumer
with a quantitatively different degeneration scale. The common missing
ingredient remains a complete, coupled canonical-theta estimate strong
enough for the selected consumer.

### Verification and provenance

The three source audits cross-checked current stops and formula
normalizations. The primary classical references linked above were
consulted for degree, logarithmic zero measures, bilinear relations,
annulus modulus and spherical-area conventions. Identities (G2), (T2)–(T4)
and the local bounds (R4)–(R6) are elementary specializations/derivations
displayed here, not claimed new research theorems. An additional internal
formula review checked signs, factors, compact/bordered hypotheses and
the distinction between identities and unpaid bounds. Local links and
file size were checked. No theta quadrature, interval certificate, global
estimate or independent specialist review is claimed.

[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[geom]: ../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[arithmetic]: ../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[realizations]: ../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../avoid/01_restating_the_target.md
[a02]: ../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a13]: ../../../avoid/13_a_factor_is_not_the_target.md
[a15]: ../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md
[a20]: ../../../avoid/20_volume_without_a_gain.md
[i4]: ../README.md
[i4n5]: ../notes/05_TARGET_INVENTORY_AND_FINITE_REGULATOR_GAUSS_COMPARISON_20261022.md
[i4r6]: ../03_heat_transport_and_charges/reviews/06_FINITE_REGULATOR_GAUSS_COMPARISON_REVIEW_20261022.md
[sourcehome]: ../02_theta_source_constraints/README.md
[icw]: ../03_heat_transport_and_charges/notes/02_INTERIOR_CURRENT_WALLS_AND_BACKWARD_SURVIVAL_20261022.md
[bw]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/README.md
[bw10notes]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/README.md
[bw13]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/13_spectral_covers_and_periods/README.md
[bw15]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/15_jensen_surface_degeneration/README.md
[bw09energy]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/05_TOPOLOGICAL_ALTERNATIVES_AND_ENERGY_OBSERVATIONS_20261020.md
[rootcaps]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/03_ROOT_FOLLOWING_WALLS_AND_CAP_COUNT_20261020.md
[gauss]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md
[tubes]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[ratio]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md
[period]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/13_spectral_covers_and_periods/notes/01_NODAL_PERIOD_VARIATION_AND_FOUR_JET_COMPARISON_20261021.md
[globalideas]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/brainstorm/04_GLOBAL_HEAT_GEOMETRY_PROPOSALS_AND_INITIAL_SCREENS_20261021.md
[inv22]: ../../investigations-2/active/22_theta_manifold_geometry/README.md
[realindex]: ../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[wallflux]: ../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[connection]: ../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/01_COVARIANT_SOURCE_AND_ASD_CONNECTION_20261015.md
[coordination]: ../../investigations-2/active/22_theta_manifold_geometry/notes/00_research_coordination/03_PRIORITIZED_SIGNED_BOUND_RESEARCH_PATHS_20261015.md
[circle]: ../01_compact_weil_positivity/notes/01_CIRCLE_COMPARISON_AND_POSITIVE_COMPLETION_OBSTRUCTIONS_20261021.md
[jensen]: ../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md
[jensenheat]: ../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/07_REAL_PROJECTIVE_JETS_AND_JENSEN_HEAT_SURFACES_20261015.md
