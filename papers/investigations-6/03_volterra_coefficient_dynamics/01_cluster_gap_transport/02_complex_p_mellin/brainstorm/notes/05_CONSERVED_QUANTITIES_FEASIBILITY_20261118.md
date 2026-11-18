# Conserved quantities in the exterior moment hierarchy

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and reasoning effort are
unavailable in this chat's recorded configurations; no settings are
inferred. Status: **exploratory analytical derivations, with exact finite
algebra checks and a same-assistant self-check**. No independent assessment
or canonical numerical gain is claimed.

**There are genuine conserved quantities for finite polynomial heat
flows. The counterparts found here for the complete hierarchy are
infinite-order encodings of the initial field and finite-block quantities
with an explicit exterior flux.** The most useful candidate identified
here is a fourth-order block invariant whose flux cancels common
translation and whose remaining departure from affine exterior motion is
controlled by exterior curvature. It is a candidate for sharper joint
enclosures, not yet a barrier against collisions.

This author-requested exploration stays in the existing brainstorm. It
does not change the manuscript, main progress register, source budgets or
the parallel continuation. The reading basis is the manuscript's
[integer hierarchy][integer], [coupled lattice][lattice],
[joint dynamics][joint], [finite approximation][finite],
[forward block laws][forward] and [two-sided formulation][two-sided],
with recent Notes [29][n29], [35][n35], [39][n39], [42][n42] and [43][n43].
The remaining manuscript statements were checked for their domains and
comparison requirements. Note43's centered direct estimator is the current
same-information baseline; the older manuscript predates that acquisition.

Read the [result index][results] and [avoid index][avoid], particularly
[cluster18][cluster], [collision controls12][controls],
[classification01][classification], [premises02][premises],
[scope07][scope] and [joint bounds12][joint-bounds]. Under that
classification, the work below consists of identities and one scoped
obstruction. It is not an RH-equivalent criterion. The proposed use of a
block invariant becomes a quantitative milestone only after a strict
enclosure or cost improvement has actually been measured.

## 1. The pair equations give a balance law

Use physical forward time throughout:

\[
 H_t=-H_{zz},\qquad B=H_z/H,\qquad
 D'=2-4DM,\qquad M'=2M^2-\mathcal F,
 \qquad \mathcal F=12S_2+16DS_3.
 \tag{1}
\]

On a fixed zero-free contour, Burgers' equation
\(B_t=-\partial_z(B_z+B^2)\) conserves
\((2\pi i)^{-1}\oint B\,dz\). This is the already counted total
multiplicity. Two simple roots merging into a double do not change it.

An energy-like polynomial in the pair data is

\[
 E=2M-2DM^2+D\mathcal F.
 \tag{2}
\]

Regarding \(\mathcal F(t)\) as a prescribed forcing, (1) is the
time-dependent Hamiltonian pair \(D'=E_M,\ M'=-E_D\). Along the
actual full hierarchy, the product rule gives exactly

\[
 E'=D\mathcal F'.
 \tag{3}
\]

Thus (2) is conserved for constant forcing, but not generally for the
physical forcing. The higher moment rows are what determine its flux.
Subtracting \(\int D\mathcal F'\,dt\) makes a constant, but requires
the same uncontrolled history; it supplies no new estimate by itself.

The manuscript already proves the regular identity

\[
 (D')^2-2DD''+8\mathcal F D^2=4.
 \tag{4}
\]

Its value is fixed by the pair law, independently of initial data. In
particular, it remains true at a merger, where \(D=0,D'=2\). It is a
useful consistency identity, not a positive energy that obstructs merging.
Writing \(r=\sqrt D\) on a positive-gap chart instead gives
\(r''=2\mathcal F r-r^{-3}\); the inverse-cubic term has the attractive
sign. The square-root coordinates must stop at a merger, whereas (1)–(4)
remain regular on a counted pair tube.

## 2. A complete finite polynomial has nontrivial first integrals

Let \(P(t,z)=\sum_{j=0}^N a_j(t)z^{N-j}\), \(a_0=1\), be a
monic polynomial satisfying \(P_t=-P_{zz}\). Its coefficients obey

\[
 a_j'=-(N-j+2)(N-j+1)a_{j-2},\qquad a_{-1}=a_{-2}=0.
 \tag{5}
\]

Consequently every coefficient of the finite polynomial
\(e^{t\partial_z^2}P(t,z)=P(0,z)\) is conserved. Explicitly,

\[
 I_j(t)=\sum_{r=0}^{\lfloor j/2\rfloor}
   \frac{t^r}{r!}\frac{(N-j+2r)!}{(N-j)!}a_{j-2r}(t)
   =a_j(0).
 \tag{6}
\]

There are also autonomous integrals, with no explicit time variable. For
\(N\ge2\), set \(\theta=-a_2/[N(N-1)]\). Equation (5) gives
\(\theta'=1\), so every coefficient of
\(e^{\theta\partial_z^2}P\) is constant. Its coefficient of
\(z^{N-2}\) vanishes identically. The other nonleading coefficients
give \(N-1\) independent integrals: the transformation straightens the
polynomial coefficient flow into translation of the single clock
\(\theta\). This is finite polynomial integrability, not a claim about
arbitrary infinite moment sequences.

For root geometry, let \(x_1,\ldots,x_N\) be the complete finite divisor,
\(\bar x=N^{-1}\sum x_i\), \(y_i=x_i-\bar x\), and
\(p_k=\sum_i y_i^k\). On a simple-root chart,
\(x_i'=2\sum_{j\ne i}(x_i-x_j)^{-1}\). Pairwise cancellation gives

\[
 \bar x'=0,\quad p_2'=2N(N-1),\quad p_3'=0,\quad
 p_4'=4(2N-3)p_2.
 \tag{7}
\]

For \(N\ge4\), a concrete conserved quantity is therefore

\[
 \boxed{C_4=\frac{2N-3}{4N(N-1)}p_2^2-\frac14p_4.}
 \tag{8}
\]

If \(b_j\) are the centered polynomial coefficients, Newton identities
give the equivalent expression
\(C_4=b_4-(N-2)(N-3)b_2^2/[2N(N-1)]\). The quantities in (6)–(8)
are symmetric polynomials and continue through root collisions.

This finite integrability has relevant prior literature: Deconinck,
Kimura and Segur's [2007 paper][dks] reports conserved quantities for the
rational Burgers pole system. Its abstract was inspected, not its full
proof. Equations (5)–(8) are derived here directly. Sokal's
[2023 seminar][sokal] discusses the same finite heat-zero dynamics and
the matrix representation below. No novelty claim is made for these
finite identities; precise reading and retrieval scope is in the
[reference catalog](../references/README.md).

### A conserved positive value can coexist with collision

Translate the manuscript's quartic control to any physical time \(T\):

\[
 P(t,z)=(z^2-b^2)^2-(t-T)(12z^2-4b^2)+12(t-T)^2,
 \qquad b>0.
 \tag{9}
\]

Here \(N=4\), and direct coefficient substitution gives
\(C_4=2b^4/3>0\) for every time. Nevertheless both \(+b\) and
\(-b\) are double zeros at \(t=T\). This screens a proposal to use the
positivity of (8) alone as a collision barrier. It does not rule out a
stronger combination of invariants and source-specific geometric bounds.

The invariant nevertheless carries useful shape information. For a
centered even quartic, the quadratic discriminant in the variable
\(z^2\) is

\[
 \Delta_{z^2}=p_2^2/6-4C_4.
\]

If \(p_2>0\) and \(C_4>0\), the four roots are real and simple
exactly when \(p_2^2>24C_4\). Equality gives the two double roots.
Thus the invariant together with the variance clock determines this
finite collision threshold. The direct quartic discriminant has the same
information; no improvement over that comparator is claimed.

For the canonical infinite divisor, the positive-power sums in (7)–(8)
are not absolutely convergent. The polynomial's top-degree coefficients
also have no literal infinite-degree counterpart. An invariant of a
growing product cutoff therefore needs a separate renormalization and
boundary-flux proof. The fixed-order inverse-moment convergence in the
manuscript is not such a proof.

## 3. The usual finite Calogero spectral integrals collapse

The first-order finite root law implies
\(x_i''=-8\sum_{j\ne i}(x_i-x_j)^{-3}\). Its embedding into the
second-order attractive Calogero system has energy

\[
 \mathcal H=\frac12\sum_i(x_i')^2
             -4\sum_{i<j}(x_i-x_j)^{-2}=0.
 \tag{10}
\]

The equality is algebraic on the first-order heat-flow locus: if
\(s_i=\sum_{j\ne i}(x_i-x_j)^{-1}\), the three-index cross terms
cancel and \(\sum_i s_i^2=2\sum_{i<j}(x_i-x_j)^{-2}\).

More generally define

\[
 L_{ii}=2s_i,
 \qquad L_{ij}=\frac2{x_i-x_j}\quad(i\ne j).
 \tag{11}
\]

This matrix is nilpotent for every distinct finite configuration. To see
this, represent differentiation of polynomials of degree below \(N\)
by their values at the nodes. For \(Q(z)=\prod_i(z-x_i)\), its matrix
\(A\) has
\(A_{ii}=s_i\) and
\(A_{ij}=Q'(x_i)/[Q'(x_j)(x_i-x_j)]\). These are derivatives of the
Lagrange cardinal polynomials. With \(W=\operatorname{diag}Q'(x_i)\),
\(L=2W^{-1}AW\). Differentiation has \(A^N=0\), proving

\[
 L^N=0,\qquad \operatorname{tr}L^k=0\quad(k\ge1).
 \tag{12}
\]

Thus the familiar spectral powers do not provide additional nonzero
finite invariants on this special first-order locus. The coefficient
integrals (6)–(8) still exist. No statement about regularized traces of an
infinite operator follows: their domain, convergence and boundary terms
would have to be constructed independently.

## 4. A precise obstruction to universal finite moment invariants

Consider a \(C^1\) candidate
\(I(t,D,S_1,\ldots,S_P,T_2,\ldots,T_P)\), on an open domain with
\(D\ne0\). Suppose it is a first integral of the regular hierarchy
for freely variable moment tails through order \(P+2\), with no
source-specific constraint relating those tails to the retained head.
**Then it is locally constant.** This is an obstruction for this
universal finite-head class, not for a fixed canonical trajectory,
an infinite functional, or a finite divisor satisfying algebraic moment
relations.

Proof: the highest tail coordinates occur in the derivative only as

\[
 -4P(P+3)D
   \left(I_{S_P}S_{P+2}+I_{T_P}T_{P+2}\right).
 \tag{13}
\]

Omit the odd term if \(P=1\). No lower row contains either highest
coordinate. Independent variation therefore forces both derivatives of
\(I\) to vanish. Descending in \(P\) removes all moment dependence.
The remaining equation is
\(I_t+(2-4DM)I_D=0\) for variable \(M\). Since \(D\ne0\), it
forces \(I_D=I_t=0\). A \(C^1\) identity on a neighborhood crossing
\(D=0\) cannot acquire a new nonconstant value only on that hypersurface.

The free-tail premise is not merely about fictitious sequences. At fixed
\(D\), take sufficiently many freely located real exterior roots outside
a strict collar. The kernels
\((w^2-D)^{-r}\), \(1\le r\le P+2\), and
\(w(w^2-D)^{-r}\), \(2\le r\le P+2\), have linearly independent
derivatives: their leading inverse powers at infinity are all different.
Hence evaluations of these derivatives at \(2P+3\) suitable distinct
exterior points form a nonsingular matrix. The moment map has full local
rank there, and this holds generically in that freely variable polynomial
exterior class. In such neighborhoods the tail variation used in (13) is
physical at a polynomial initial slice. It is not asserted for the
unchanged theta source or a fixed small number of exterior roots.

This explains why searching for a universal polynomial or rational
combination of only a few \(S/T\) rows is unlikely to succeed. It does
not exclude a quantity involving a whole counted block, a paid exterior
history, or the complete generating field.

## 5. Exact constants for the full canonical field

The heat equation does supply an infinite family of exact constants:

\[
 \mathcal J(t,z)=\sum_{r=0}^\infty
            \frac{t^r}{r!}\partial_z^{2r}H(t,z)=H(0,z).
 \tag{14}
\]

This is an actual convergent identity for the source in the manuscript,
not merely a formal heat-operator expansion. Substituting its cosine
integral turns the sum into multiplication by
\(\sum_r(-tu^2)^r/r!=e^{-tu^2}\). Absolute interchange on compact
\((t,z)\) sets is justified by the integrable majorant
\(e^{(\Re t+|t|)u^2+|\Im z|u}\Phi(u)\); any fixed spatial derivative
adds only a power of \(u\). The source's double-exponential decay pays
this majorant.

It can even be expressed using the complete zero divisor without its
amplitude. Set \(E_t(z)=H(t,z)/H(t,0)\), the normalized opposite-paired
product. For real \(t\),

\[
 \frac{(e^{t\partial_z^2}E_t)(z)}
      {(e^{t\partial_z^2}E_t)(0)}
       =\frac{H(0,z)}{H(0,0)}.
 \tag{15}
\]

The denominator is \(H(0,0)/H(t,0)>0\). This uses the entire field
and an infinite jet, and does not contradict Section 4. It records the
initial data in different coordinates; its existence alone neither bounds
the truncation error nor supplies a collision-free initial field.

There is a related distinction in the parent Volterra chain. Its
[base manuscript][base] proves
\(\beta_n'=\beta_n(\beta_{n+1}-\beta_{n-1})\), \(\beta_0=0\),
and a banded Lax identity. A finite prefix obeys the exact flux law

\[
 \frac{d}{dt}\sum_{n=1}^K\beta_n=\beta_K\beta_{K+1}.
 \tag{16}
\]

Closing an artificial chain by \(\beta_{K+1}=0\) changes that law.
For the full positive theta weight, the multiplication-operator spectrum
is the whole real line at every time; this follows from full support,
without asserting a bounded Lax propagator. The total positive trace sum
is not finite: summable \(\beta_n\) would make the Jacobi matrix bounded,
contradicting its unbounded multiplication spectrum. These familiar
spectral facts are shared by many positive weights and do not fix the
zeros of the Fourier readout.

## 6. A finite block invariant with a complete exterior flux

This is the candidate worth retaining from the exploration. Let one
fixed cleared contour count \(N\ge4\) roots, initially on a real-simple
chart, and assume its interior contains the block's convex hull. A
cleared enclosing circle suffices. Remove the whole block from the
complete logarithmic derivative:

\[
 R(t,z)=B(t,z)-\sum_{i=1}^N\frac1{z-x_i(t)},\qquad
 x_i'=2\sum_{j\ne i}\frac1{x_i-x_j}+2R(t,x_i).
 \tag{17}
\]

The exterior may be nonreal; \(R\) is its complete analytic contribution
inside the contour, with the original regularization. Use the centered
\(p_k\) and \(C_4\) from (8), now for this block only, and put

\[
 \psi_i=y_i^3-\frac{2N-3}{N(N-1)}p_2y_i-\frac{p_3}{N}.
 \tag{18}
\]

Then the exact block balance is

\[
 \boxed{C_4'=-2\sum_i\psi_iR(t,x_i).}
 \tag{19}
\]

For completeness, \(\bar x'=2\overline R\). Differentiation of the
centered powers gives

\[
 \begin{aligned}
 p_2'&=2N(N-1)+4\sum_i y_iR(t,x_i),\\
 p_3'&=6\sum_i(y_i^2-p_2/N)R(t,x_i),\\
 p_4'&=4(2N-3)p_2+
          8\sum_i(y_i^3-p_3/N)R(t,x_i).
 \end{aligned}
 \tag{20}
\]

Substitution in (8) cancels the internal terms and proves (19). Unlike
the adjacent edge charts, these symmetric block quantities and their
analytic exterior traces remain regular through an internal merger while
the whole-block boundary stays clear. This continuation follows from
the counted contour power sums, rather than differentiating singular
individual root velocities at the merger.

### Common translation and linear exterior variation cancel explicitly

Write
\(R(t,\bar x+y)=a(t)+b(t)y+r(t,y)\), choosing
\(a=R(t,\bar x)\), \(b=R_z(t,\bar x)\). The two finite identities

\[
 \sum_i\psi_i=0,\qquad \sum_i\psi_i y_i=-4C_4
\]

turn (19) into

\[
 C_4'-8bC_4=\mathcal E_4,
 \qquad \mathcal E_4=-2\sum_i\psi_i r(t,y_i).
 \tag{21}
\]

Thus an exactly affine exterior makes
\(e^{-8\int_{t_0}^t b(v)\,dv}C_4(t)\) constant. For a genuine
nonlinear exterior, suppose \(|y_i|\le\rho\) and
\(|R_{zz}|\le C_2\) on every segment from \(\bar x\) to \(x_i\).
Taylor's integral remainder gives the explicit allowance

\[
 |\mathcal E_4|\le C_2\sum_i|\psi_i||y_i|^2
                    \le4N C_2\rho^5.
 \tag{22}
\]

Indeed \(|p_2|\le N\rho^2\), \(|p_3|\le N\rho^3\), and
\(|\psi_i|\le(4-1/(N-1))\rho^3\le4\rho^3\). Integrating (21)
with the displayed multiplier gives a paid near-conservation statement
if \(b,C_2,\rho\) and the initial value have whole-time enclosures.
Calling it near-conservation before paying those values would overstate
the result. The fifth-power allowance is a local scale statement, not
a canonical asymptotic estimate.

The cancellation can be retained directly in one contour kernel. With
\(Z=z-\bar x\), define

\[
 K_4(z)=\sum_i\frac{\psi_i}{z-x_i}
                +\frac{4C_4}{(z-\bar x)^2}.
\]

The complete exterior Cauchy formulas give

\[
 \mathcal E_4=-\frac2{2\pi i}\oint_\Gamma B(t,z)K_4(z)\,dz.
 \tag{23}
\]

The coefficients of \(Z^{-1}\) and \(Z^{-2}\) in this combined kernel
vanish. This is the same affine cancellation as (21), now available
before independent contour errors are bounded. For example,
\(R_{zz}(t,w)=2(2\pi i)^{-1}\oint_\Gamma B(t,z)/(z-w)^3\,dz\);
on a circle of radius \(r_\Gamma\), a uniform error \(e_B\) contributes
at most \(2r_\Gamma e_B/\delta^3\) when \(w\) is at distance at least
\(\delta\) from the circle. Coordinate, quadrature and whole-time
errors remain additional obligations. The combined kernel may be more
informative than this separate derivative allowance.

An exact six-root check shows why the exterior must remain. For the
block \((-2,-1,1,2)\) with exterior \((-5,5)\),

\[
 C_4=23/12,\quad C_4'=-55/42,\quad b=-2/25,
 \qquad C_4'-8bC_4=-29/350.
 \tag{24}
\]

The same four roots without the exterior have \(C_4'=0\). Both values
were obtained independently from the root velocities and from (19) in
exact rational arithmetic. This example tests the missing flux, rather
than testing only an isolated model that is conserved by construction.

## 7. Collision controls and the scope of a possible gain

The [catalog controls][controls] were screened against the premises of
these formulas. **None is rejected by the universal heat identities.**
On a cleared counted block, (19) includes its exterior flux and still
allows its known collision. For sources with all Gaussian exponential
moments, (14) also holds for the control's own initial field.

| Control | Outcome of the conservation screen and missing additional premise |
| --- | --- |
| Shifted quartic (9), and the isolated quadratic | Exact conserved quantities coexist with the collision; literal theta source and infinite canonical population are absent. Equation (9) explicitly defeats positivity of C4 alone. |
| Cosine plus a constant | Heat pullback and contour count survive its double zero. It lacks the complete theta source; no new positive-gap conclusion is licensed by conservation. |
| Euler-factor translates | The generic balances hold. The unchanged normalized theta coefficients/completion fail; no favorable canonical flux value transfers automatically. |
| Weighted-square sources | Generic balances still hold at the documented event. Full reflected unit-weight theta source equality fails, despite square support and selected endpoint identities. |
| Reflected super-Gaussian | Heat and local block laws still apply. Literal theta arithmetic and the canonical order-one premise fail; the global canonical product passage is not imported. |
| Smooth shape and positive-primitive controls | Positivity, evenness and strong decay preserve the generic identities. Complete theta arithmetic/profile transfer fails. Auxiliary primitive positivity does not set the flux in (21). |
| Finite-prime, finite-score and finite-profile variants | Their preserved finite data do not supply full source equality and a paid joint flux. Their particular missing reflection, arithmetic or complete-profile premise remains the one in controls12. |
| Changed observation kernels or fractional zero profiles | The actual cosine/Newman equation or integer divisor realization, respectively, is missing. They are not counterexamples to identities for the physical heat divisor. |

The first row has an exact executable collision check. The remaining rows
are an analytical premise screen against the catalog's documented
witnesses, not newly repeated numerical certificates. No numerical check
of RH or a global exclusion is claimed.

## 8. Assessment and a bounded follow-up

The answer to the author's question is affirmative at the finite-polynomial
and full-field levels. What is still missing is a conserved or nearly
conserved quantity that constrains an individual canonical gap more
efficiently than the current direct source calculation. Count conservation,
the zero Calogero energy, and the heat pullback do not supply that result.
Section 4 specifically screens universal invariants made from finitely
many freely variable moment rows.

The useful follow-up is **finite-block heat invariants with a complete
exterior flux**, especially (21)–(23). This has three concrete advantages
as a question: internal forces cancel exactly, common translation costs
nothing, and the nonlinear error starts with exterior curvature. It also
uses a block chart that can remain regular when adjacent edge charts fail.
These are structural properties, not an acquired canonical width gain.

Before opening a sustained new investigation, a bounded feasibility test
should fix one already counted block, one physical interval and one
complete source record. It should compare a joint enclosure using
(21) or (23) with direct centered contour extraction given exactly the
same data. Preserve the quartic collision in the control input. Require
a strict useful improvement after paying exterior, coordinate, time and
arithmetic errors, or record the precise reason it fails. A bound on C4
alone must not be substituted for a minimum-gap bound: the collision
example already prevents that inference.

I would retain this candidate for that test, but would not yet organize a
new program around a presumed positive conserved energy of the infinite
hierarchy. No new investigation or numerical source campaign is started
by this note.

The [exact check program][code] and [small execution record][record] cover
finite heat pullback, autonomous coefficient integrals, nilpotent matrices,
the quartic collision, nonzero block flux and generic moment-coordinate
rank examples. General claims rest on the derivations above; these checks
are not independent review or evidence for a canonical sign. The
[self-check](../reviews/01_CONSERVATION_SELF_CHECK_20261118.md) records the
scope and remaining gap.

[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[cluster]: ../../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[classification]: ../../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint-bounds]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[base]: ../../../../manuscript/main.tex
[integer]: ../../manuscript/sections/02_integer_hierarchy.tex
[lattice]: ../../manuscript/sections/14_coupled_lattice.tex
[joint]: ../../manuscript/sections/09_joint_dynamics.tex
[finite]: ../../manuscript/sections/10_finite_hierarchy.tex
[forward]: ../../manuscript/sections/17_forward_statistics.tex
[two-sided]: ../../manuscript/sections/19_two_sided_refinement.tex
[n29]: ../../notes/29_VCD_GT_CM_ZERO_INDEXED_COUPLED_LATTICE_20261118.md
[n35]: ../../notes/35_VCD_GT_CM_RECURSIVE_TWO_SIDED_FORMULATION_20261118.md
[n39]: ../../notes/39_VCD_GT_CM_E34_EXTENDED_SOURCE_AND_FORCING_20261118.md
[n42]: ../../notes/42_VCD_GT_CM_E36_CORRELATED_DISCRIMINANT_20261118.md
[n43]: ../../notes/43_VCD_GT_CM_CORRELATION_GAIN_CONTINUATION_20261118.md
[dks]: https://doi.org/10.1088/1751-8113/40/20/014
[sokal]: https://mediacentral.ucl.ac.uk/Play/95003
[code]: ../numerics/check_conservation_20261118.py
[record]: ../numerics/01_CONSERVATION_EXACT_CHECKS_20261118.json
