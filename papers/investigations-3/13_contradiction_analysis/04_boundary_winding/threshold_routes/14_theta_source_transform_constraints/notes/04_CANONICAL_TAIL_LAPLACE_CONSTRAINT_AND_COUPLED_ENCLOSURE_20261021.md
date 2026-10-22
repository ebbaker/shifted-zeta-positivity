# A quantitative constraint on the actual theta tail and its coupled first jet

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Analytic continuation of [Note 03][n03]; no
numerical experiment. Proofs and [self-review][review] are by the
authoring assistant only, without independent specialist review or
novelty claim.

## 1. Result and exact comparison

The actual remainder after retaining modes 1 through m has a normalized
source multiplier that is a positive Laplace mixture. Its variable is
\(h=e^{4u}-1\), not the physical frequency or heat time. The construction
below gives all of the following analytically:

- an explicit positive representing measure with every lattice index;
- a common complex-source bound smaller than 4 on a fixed right strip;
- a global source-derivative bound \(L_m\), with the displayed bound
  asymptotic to \(24/(\pi m^3)\);
- a coupled enclosure of the physical value and first derivative by
  the convex hull of one curve of incomplete integrals;
- a strictly positive, explicit support-function improvement over the
  pointwise envelope using the **same** known lower and upper source
  bounds, including their positivity and first spectral gap.

This answers the immediate question from Note 03: the actual residual
does satisfy a quantitative analytic constraint that prevents arbitrary
alignment with the oscillatory kernel. The comparison is an analytic
bound for a relaxation, not a measured approximation error or a claim
to improve the strongest existing arithmetic evaluator.

The limitation is also precise. Positive weighted-square sources retain
the same mixture structure. Finite-prime collision controls can match
the particular constants used here, as proved in Section 8. Thus this
gain does not yet give the missing theta-specific physical sign. Full
head/tail modular cancellation remains an additional obligation.

Use the [result index][results], [theta/arithmetic cluster][arithmetic],
[controls][controls] and [avoid index][avoid], particularly
[classification][a01], [premise matching][a02], [scoped statements][a07] and
[complete signed estimates][a12]. The [older positive-tail cone][cone]
and [Note 01][n01] already retain shared mode weights in a physical jet.
The addition here is the explicit source-variable Laplace law and its
quantitative transfer; convex-hull language itself is not new.

**Classification:** a quantitative estimate with a specified comparison
class, rather than a new reformulation of the zero-exclusion target.

**Contract.** The residual is the actual half-line theta tail after a
fixed integer cutoff m>=1. Both components use the same multiplier.
The signed comparison is on real \((t,x)\), and is uniform on any
\(|t|\le T,\ 0<x_0\le x\le x_1<\infty\). The direct comparison
keeps the same source floor, envelope and complete integrals. It drops
only the multiplier's monotonicity. No contour shift or numerical
acquisition is part of this comparison.

## 2. Exact positive measure from the unchanged coefficients

Keep the complete mode normalization from Notes 01–02:
\[
 \lambda_n=\pi n^2,\qquad
 \phi_n(u)=\lambda_n e^{5u}(2\lambda_ne^{4u}-3)
                     e^{-\lambda_ne^{4u}}.
 \tag{1}
\]
In particular every mode is positive for u>=0. Fix m>=1 and put
\[
 \begin{gathered}
 R_m(u)=\sum_{n>m}\phi_n(u),\qquad
 k=m+1,\quad a=\lambda_m,\quad b=\lambda_k,\quad \Delta=b-a,\\
 h=e^{4u}-1,\qquad D=2a-3>0,\quad \gamma=D/(2a)>1/2.
 \end{gathered}
 \tag{2}
\]
For n>m define
\[
 \Delta_n=\lambda_n-a,\quad \delta_n=\lambda_n-b,\qquad
 A_n=\frac{\lambda_n^2}{a^2}e^{-\Delta_n},\quad
 B_n=\frac{3\lambda_n\Delta_n}{a^2D}e^{-\Delta_n}.
 \tag{3}
\]
All these masses are positive. Direct division of the source polynomials
gives the identity
\[
 \frac{\phi_n(u)}{\phi_m(u)}
 =e^{-\Delta_n h}\left(A_n+B_n\frac{\gamma}{\gamma+h}\right).
 \tag{4}
\]
For example, the algebra behind it is
\((2\lambda_nq-3)/(2aq-3)=\lambda_n/a+
3(\lambda_n-a)/(a(2aq-3))\), with q=1+h. The covariant lower-order
source term has therefore been retained.

Let \(\mathsf E_\gamma\) be the probability measure on [0,infinity)
with density \(\gamma e^{-\gamma s}\). Its Laplace transform is
\(\gamma/(\gamma+h)\). This elementary use of the Laplace transform
uses the convention in [DLMF §1.14(iii)][laplace]; the representing
measure here is constructed directly, without invoking a converse
representation theorem. Define
\[
 E_m=\sum_{n>m}(A_n+B_n)=\frac{R_m(0)}{\phi_m(0)},
 \tag{5}
\]
\[
 \nu_m=\frac1{E_m}\sum_{n>m}
 \left[A_n\delta_{\delta_n}
       +B_n\,\operatorname{Law}(\delta_n+\mathsf E_\gamma)\right].
 \tag{6}
\]
Here \(\delta_{\delta_n}\) denotes a point mass; the two uses of
delta are distinguished by the subscript. This is a probability measure.
For clarity, \(\operatorname{Law}(\delta_n+\mathsf E_\gamma)\)
means translation of that exponential probability measure by \(\delta_n\).
Set
\[
 p_m(h)=\int_0^\infty e^{-sh}\,d\nu_m(s).
\]
The exact residual identity is
\[
 \boxed{R_m(u)=E_m\phi_m(u)e^{-\Delta h}p_m(h).}
 \tag{7}
\]
Its lowest atom is
\[
 \eta_m=\nu_m(\{0\})=\frac{A_k}{E_m}\in(0,1).
 \tag{8}
\]
The inequality is strict because B_k>0. Therefore
\[
 p_m(0)=1,\qquad \lim_{h\to\infty}p_m(h)=\eta_m,
 \qquad (-1)^j p_m^{(j)}(h)\ge0\quad(j\ge0,h\ge0).
 \tag{9}
\]
All moments of (6) are finite: its discrete masses have Gaussian decay
in n, and its continuous part is an exponential distribution with
fixed positive rate. This justifies the derivatives at h=0 as well
as on h>0. In particular p_m is decreasing and convex in h, and has
all the further alternating derivative inequalities. These assertions
do not say that the physical transform is completely monotone in x.

Equations (7)–(9) give the matched pointwise bounds
\[
 \boxed{A_k\phi_m(u)e^{-\Delta h}
       \le R_m(u)\le E_m\phi_m(u)e^{-\Delta h}.}
 \tag{10}
\]
Both constants and the first gap are retained in the comparison below.

## 3. Quantitative analyticity and a complete derivative payment

The formula in (6) extends p_m holomorphically to
\(\Re h>-\gamma\). For \(0\le r<\gamma\), positivity gives
\[
 |p_m(h)|\le\frac1{E_m}\sum_{n>m}
 \left(A_n+B_n\frac\gamma{\gamma-r}\right)e^{r\delta_n}
 \quad(\Re h\ge-r).
 \tag{11}
\]
The sum converges because r<gamma<1. It is a quantitative bound,
not merely a claim that an analytic continuation exists.

A simple uniform constant follows. Put
\(\rho_c=((k+1)/k)^4 e^{-c\pi(2k+1)}\).
Since \(B_n\le(3/D)A_n\), successive A_n ratios after inserting
\(e^{r\delta_n}\) are at most \(\rho_{1-r}\). Thus, when this
ratio is less than one,
\[
 |p_m(h)|\le\frac{A_k}{E_m}
       \frac{1+3\gamma/[D(\gamma-r)]}{1-\rho_{1-r}}.
 \tag{12}
\]
Choose r=gamma/2. Then 1-r>1/2, k>=2 and pi>3 imply
\(\rho_{1-r}<81/1024<1/4\): use \(e^6>2^6\) in the exponential
majorant. Also D>3 and A_k/E_m<1. Consequently
\[
 \boxed{|p_m(h)|<4\quad(\Re h\ge-\gamma/2),\qquad m\ge1.}
 \tag{13}
\]
In source coordinates this supplies the fixed right-strip bound
\[
 \boxed{|p_m(e^{4v}-1)|<4\quad
           (\Re v\ge0,\ |\Im v|\le\pi/24),\qquad m\ge1.}
 \tag{14}
\]
Indeed \(\Re(e^{4v}-1)\ge\sqrt3/2-1>-1/4>-\gamma/2\).
This statement is about a right half-strip. It grants no separate
reflected continuation to the finite tail or its reference mode.

There is a sharper real-source derivative bound. Define the unnormalized
first moment of the shifted measure by
\[
 Q_m=\sum_{n>m}\left[(A_n+B_n)\delta_n+B_n/\gamma\right].
 \tag{15}
\]
For q>=1 and s>0,
\(q s e^{-s(q-1)}\le\max(1,s)\le1+s\); at s=0 it is zero.
The zero atom therefore costs nothing in differentiating (7)'s multiplier:
\[
 \boxed{0\le-\frac d{du}p_m(e^{4u}-1)
 \le\frac{4(E_m-A_k+Q_m)}{E_m}\qquad(u\ge0).}
 \tag{16}
\]
This bound is independent of heat time and observation height.

All infinite sums in this payment have an explicit elementary majorant.
Set
\[
 \begin{gathered}
 A=A_k,\quad C=1+3/D,\quad c_m=B_k/A_k=\frac{3\Delta}{Db},\\
 \rho=\left(\frac{k+1}{k}\right)^4e^{-\pi(2k+1)}<1,\qquad
 F=\frac{2k\rho}{(1-\rho)^2}
       +\frac{\rho(1+\rho)}{(1-\rho)^3}.
 \end{gathered}
 \tag{17}
\]
For n=k+j, \(A_n\le A\rho^j\),
\(A_n+B_n\le C A\rho^j\), and
\(\delta_n=\pi(2kj+j^2)\). Summing the geometric first and
second moments gives
\[
 \begin{aligned}
 E_m-A&\le A\left(c_m+\frac{C\rho}{1-\rho}\right),\\
 Q_m&\le A\left[C\pi F+
          \frac{c_m+(3/D)\rho/(1-\rho)}\gamma\right].
 \end{aligned}
 \tag{18}
\]
Since E_m>=A, a fully explicit choice in (16) is
\[
 L_m=4\left[c_m+\frac{C\rho}{1-\rho}+C\pi F+
          \frac{c_m+(3/D)\rho/(1-\rho)}\gamma\right].
 \tag{19}
\]
In particular
\[
 \boxed{L_m\sim\frac{24}{\pi m^3}\quad(m\to\infty).}
 \tag{20}
\]
This is the asymptotic of the **proved upper bound** (19), not an
assertion about the exact maximum derivative. It follows from
\(c_m\sim3/(\pi m^3)\), gamma tending to 1, and exponentially
small rho. Equations (13) and (19) instantiate the quantitative
regularity premise that was only conditional in Note 03.

## 4. A common measure for the physical value and derivative

For real t,x define
\[
 W_m(t,u)=e^{tu^2}\phi_m(u)e^{-\Delta(e^{4u}-1)}>0,\qquad
 \mathbf k_x(u)=(\cos(xu),-u\sin(xu)),
 \tag{21}
\]
\[
 \mathbf J_m(t,x)=\int_0^\infty W_m(t,u)\mathbf k_x(u)du,
 \quad
 \mathbf K_m(t,x;v)=\int_0^v W_m(t,u)\mathbf k_x(u)du.
 \tag{22}
\]
Let
\(z_m(u)=[p_m(e^{4u}-1)-\eta_m]/(1-\eta_m)\).
This is decreasing from 1 to 0. Its derivative defines a probability
measure \(d\sigma_m(v)=-z_m'(v)dv\). In particular
\(z_m(u)=\sigma_m([u,\infty))\), with endpoint conventions immaterial
for this continuous measure. Fubini now gives the exact first-jet identity
\[
 \boxed{
 \begin{pmatrix}H-H_{\le m}\\ H_x-(H_{\le m})_x\end{pmatrix}
 =A\mathbf J_m+(E_m-A)
       \int_0^\infty\mathbf K_m(t,x;v)d\sigma_m(v).}
 \tag{23}
\]
Here H_{<=m} is the original half-line sum of modes 1 through m.
The measure sigma_m depends on the source and cutoff only. The same
measure works for both jet entries, and for different parameter points.
Independent extremizers at different observations would discard that
additional coupling.

Every integral here includes its entire stated interval. On compact
complex (t,z) sets, W_m times the required polynomial and exponential
spectral factors has double-exponential decay. Also 0<=z_m<=1 and its
measure has total mass one. These bounds justify Fubini and all physical
first-jet derivatives. No finite source window or lattice tail is omitted.
The convex comparison below is stated only for real t,x.

For fixed t,x let
\[
 \mathcal C_m=A\mathbf J_m+(E_m-A)
      \operatorname{conv}\{\mathbf K_m(v):0\le v\le\infty\},
 \tag{24}
\]
where K_m(infinity)=J_m. The curve is compact, since K_m is continuous
and converges at infinity. Equation (23) places the actual residual jet
in this compact convex set. It is the sharp closed image of the relaxed
class of all decreasing multipliers between 0 and 1. Indeed a decreasing
multiplier is a mixture of initial-interval indicators; possible missing
mass and a nonzero limiting value correspond to atoms at 0 and infinity.
Conversely every such mixture is decreasing. If endpoint values 1 and
0 are required, the same closed image follows by taking limits of finite
cutoffs. This sharpness is for the monotone relaxation, not for the
smaller canonical Laplace class or its derivative-restricted subclass.

## 5. Strict analytic gain against a matched positive envelope

The direct pointwise relaxation of (10), retaining both its floor and
ceiling, has the jet image
\[
 \mathcal B_m=A\mathbf J_m+(E_m-A)
 \left\{\int_0^\infty W_m(t,u)a(u)\mathbf k_x(u)du:
                         0\le a(u)\le1\right\}.
 \tag{25}
\]
This comparator already uses positivity, the first source gap and the
known lowest atom. It is stronger than a symmetric absolute envelope.
For a real covector ell put
\(G_\ell(u)=\ell_0\cos(xu)-\ell_1u\sin(xu)\),
\(f(u)=W_m(t,u)G_\ell(u)\). The two exact support functions are
\[
 \begin{aligned}
 h_{\mathcal B_m}(\ell)&=A\ell\cdot\mathbf J_m
                 +(E_m-A)\int_0^\infty f_+(u)du,\\
 h_{\mathcal C_m}(\ell)&=A\ell\cdot\mathbf J_m
                 +(E_m-A)\max_{0\le v\le\infty}\int_0^v f(u)du.
 \end{aligned}
 \tag{26}
\]
The first formula chooses a=1 where f>0 and a=0 where f<0. The second
follows from the compact curve in (24). Thus value/derivative coupling
has not been replaced by independent component intervals in either side.

For every x>0 and nonzero ell, G_ell has alternating positive and
negative intervals arbitrarily far along the half-line. This is immediate
for ell_1=0; otherwise the u sin(xu) term dominates on the interior of
successive sine lobes. Choose a negative interval I_- followed by a
positive interval I_+, and set
\[
 d_\ell=\min\left\{\int_{I_-}(-f(u))du,
                         \int_{I_+}f(u)du\right\}>0.
 \tag{27}
\]
For any cutoff v, either I_+ is still wholly omitted (if v is before
the end of I_-), or I_- is wholly included. The identity
\[
 \int_0^\infty f_+-\int_0^v f
 =\int_v^\infty f_++\int_0^v f_-
\]
therefore proves
\[
 \boxed{h_{\mathcal C_m}(\ell)
 \le h_{\mathcal B_m}(\ell)-(E_m-A)d_\ell
 <h_{\mathcal B_m}(\ell).}
 \tag{28}
\]
This is a strict analytic comparison in every nonzero first-jet direction,
not a numerical observation. The negative of ell supplies the matching
strict improvement of lower directional bounds.

The gain is uniform on any compact |t|<=T, x_0<=x<=x_1 with x_0>0,
and unit ell. Both support functions are continuous there by an
integrable common majorant, including uniform convergence of K_m(v)
as v tends to infinity. Their positive difference has a positive
minimum by compactness. No uniform positive constant as x tends to
zero or infinity is asserted by this argument.

There is also a fully explicit compact-domain example. For ell=(1,0),
take
\[
 I_-=[5\pi/(6x),7\pi/(6x)],\qquad
 I_+=[11\pi/(6x),13\pi/(6x)].
\]
On them the respective signed cosines are at least sqrt(3)/2. With
\(U=13\pi/(6x_0)\), equation (21) gives the common lower bound
\(W_m(t,u)\ge aD\exp(\Delta-be^{4U}-TU^2)\) for 0<=u<=U.
Consequently (28) holds throughout the rectangle with
\[
 d_{(1,0)}\ge\frac{\sqrt3\pi}{6x_1}
                aD\exp(\Delta-be^{4U}-TU^2)>0.
 \tag{29}
\]
This conservative symbolic constant establishes the claimed complete
uniform improvement without sampling. Its usefulness in a particular
physical estimate is a separate question.

## 6. What has and has not transferred to the physical problem

Equation (23) is a new component of the present study: a quantitatively
constrained actual residual with one common source law in the two
physical observations. Equation (28) proves that retaining this law's
monotonicity reduces a precisely specified physical error set. It is
stronger than merely writing a source identity or asserting smoothness.

For a receiving jet calculation, the complete possible field jet lies
in \(\mathbf H_{\le m}+\mathcal C_m\), with any additional acquisition
errors added explicitly. A separating covector can exclude zero from
that set on a specified regime. This is the ordinary convex-separation
consumer, not an independently proved theta lower bound in this note.
No separating physical margin is asserted here.

The comparison is not against all known theta estimates. The existing
[positive arithmetic carrier theorem][positive] proves more, including
positivity of higher-mode transforms and a complex strip, under its
stated time range. The [earlier cone][cone] and Note 01 use other
arithmetic moment data. No inclusion in either direction between those
enclosures and (24) has been proved here. The existing [S01 paired
endpoint theorem][s01] estimates the complete shifted residual of a
different approximant. Equation (28) is not a superiority claim over it.

In particular, R_m is the tail of an **unshifted** finite half-line
sum. Neither it nor phi_m is a complete even source. We have not shifted
their whole-line transforms or discarded their lower-end defects.
[Note 02][n02] gives the necessary connector when changing approximants.
The [modular-cancellation theorem][modular] still forces every algebraic
endpoint term of head and tail to cancel in the complete theta field.
A sharper absolute or relative tail allowance does not by itself control
that small signed sum near a multiple zero.

## 7. Source-law refinements that remain available

The monotone hull deliberately relaxes the exact measure (6). Two
stronger pieces remain explicit rather than hidden:

- p_m is a positive Laplace transform, not an arbitrary decreasing
  function. Its full atom/continuous decomposition and all moment
  constraints survive in (6). A Laplace-mixture jet hull is therefore
  contained in (24), but no further strictness claim is made here.
- The same sigma_m in (23) works at different t,x. A proof involving a
  stationary condition, heat evolution, or several observations should
  retain that common measure instead of optimizing each point separately.

These identify where a subsequent signed analysis could use more of the
source. They do not supply an automatic sign, finite closure, or global
height theorem. Finite selected moments alone face the following control.

## 8. Matching controls and the precise remaining gap

For bounded positive square coefficients c_n, the same algebra gives a
positive measure with masses c_n A_n and c_n B_n. Thus the positive
Laplace structure and monotonicity do not force the coefficients to be
canonical. The [finite-prime control theorem][finite-prime] permits a
fixed canonical prefix and any finite list of real linear measurements.
Preserve the prefix through k=m+1 and the source's value and first
derivative at u=0. Then:

- A=A_k is unchanged, since c_k=1;
- E_m is unchanged, since it is R_m(0)/phi_m(0);
- Q_m is unchanged. To see this, for
  \(F(h)=R_m(u(h))/\phi_m(u(h))\),
  \(Q_m=-F'(0)-\Delta F(0)\), where this derivative is in h.
  Its value is a fixed linear combination of R_m(0) and R_m'(0),
  since \(du/dh=1/4\) at zero.

The controls therefore have the same eta_m, the same derivative payment
(16), and the same monotone jet enclosure (24), while admitting the
theorem's high-gap double events. The common complex bound (13) can
also be retained. In the proof of (12), the canonical bound is less
than \(3/(1-81/1024)=3072/943\). Choose the control's coefficients
within 1/5 of 1, as the theorem allows, and preserve E_m as above.
The corresponding upper bound is at most
\((6/5)(3072/943)<4\). Thus this is a quantitative control match,
not merely a shared qualitative smoothness statement.

The controls fail complete normalized source reflection and the
unchanged full coefficient sequence. Those facts are not used to
derive the strict gain (28). Their fixed event heights are not prescribed:
they escape to infinity. There is no contradiction with the compact
uniform comparison or with a possible future finite-domain separator.

The other [registered controls][controls] keep their distinct roles.
Finite weighted-square controls retain the mixture form for a nonempty
higher tail, with their own masses; no equality of their constants to
theta's is asserted. Euler-factor translated sources change the original
square expansion. Reflected super-Gaussian and smooth/positive-primitive
controls lack this canonical positive square-tail law and its displayed
envelope; no unproved match is assigned to them. Polynomial/atomic and
compact-profile controls likewise do not provide the analytic arithmetic
tail used here. Excluding these other classes does not overcome the
finite-prime match just proved.

**Disposition.** Keep the actual-tail regularity theorem and the strict
coupled-envelope comparison as analytic progress. No numerical pilot is
needed to establish either. A next signed attempt must use the relation
between the retained head and the same complete tail law, including full
reflection where it matters; adding more finitely many source measurements
alone does not resolve the displayed control match. The arithmetic
discriminator, HMC-05 and the physical exclusion remain open; HMC-06
remains gated.

[n01]: 01_TWO_ENDPOINT_TAIL_CONSTRAINT_20261021.md
[n02]: 02_FULL_REFLECTION_ADJOINT_AND_CONNECTOR_AUDIT_20261021.md
[n03]: 03_ANALYTIC_SCOPE_AND_QUANTITATIVE_SOURCE_CONSTRAINTS_20261021.md
[review]: ../reviews/04_CANONICAL_TAIL_CONSTRAINT_SELF_REVIEW_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[arithmetic]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[cone]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/10_POSITIVE_TAIL_CONE_AND_FINITE_BOX_CERTIFICATE_20261015.md
[positive]: ../../../../../11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/03_positivity.tex
[modular]: ../../../../../11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/04_modular_collisions.tex
[s01]: ../../../../../11_arithmetic_collision_rigidity/symmetries/01_modular_self_duality/notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md
[finite-prime]: ../../../../../11_arithmetic_collision_rigidity/notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md
[laplace]: https://dlmf.nist.gov/1.14.iii
