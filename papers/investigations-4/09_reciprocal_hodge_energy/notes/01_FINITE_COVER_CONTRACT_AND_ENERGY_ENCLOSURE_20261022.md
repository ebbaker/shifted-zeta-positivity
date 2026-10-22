# Finite cover contract and reciprocal energy enclosure

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified from the active root turn metadata.

**Status: RHE-01 analytic contract complete; RHE-02 finite direct baseline
upper bound proved, Hodge advantage and actual theta acquisition open.** The chosen object is a
bordered physical cover near a hypothetical ordinary double. This is
conditional local analysis, not an assertion that theta has such an event.
The [calibration](02_FULL_QUADRATIC_ENERGY_AND_TRANSVERSE_PAYMENT_20261022.md)
stops a specific compression to bounded boundary norms and the core period.
The [review](../reviews/01_CONTRACT_AND_QUADRATIC_PILOT_REVIEW_20261022.md)
records internal same-model assessment.

Read the [result index][results], [avoid index][avoid],
[control register][controls], [criterion rule][a01],
[scoped conclusion rule][a07] and [coupled estimate rule][a12].
Reciprocal integrability as a restatement of simplicity is already
classified in the [program][program]; the objective here is a complete
energy interval and its comparison, not another simplicity criterion.

## 1. One finite physical cover

Use the unchanged source
\[
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\quad
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                       e^{-\pi n^2e^{4u}},\quad H_t=-H_{zz}.
\]
Assume a real event \((T,x_*)\), \(T\ge0\), with
\(H=H_z=0\) and \(A=H_{zz}(T,x_*)/2\ne0\).
Use \(x=z-x_*\), \(\tau=t-T\). Reuse [BW13 Note 01, §1][bw13],
rather than postulating a root gap. Set
\[
 M_j=\int_0^\infty u^j e^{(T+1)u^2+u}\Phi(u)\,du,
 \quad j=2,3,4,6,
\]
\[
 r=\min\{1,|A|/(4M_3)\},\quad
 \sigma=\min\{1,3|A|r^2/(8M_2),|A|r/(4M_3),|A|/(4M_4)\}.
                                                        \tag{1}
\]
The declared bounded comparison window is \(\sigma/2\le\tau\le\sigma\),
with spatial domain \(\Omega=\{|x|<r\}\). The endpoint question
\(0<\tau\le\sigma\), \(\tau\downarrow0\), is separate. These constants
depend on the assumed event and its curvature; no uniformity in height,
event or multiplicity is claimed.

BW13 proves on the closed outer circle
\[
 |H(T+\tau,x_*+x)|\ge m=3|A|r^2/8>0,                    \tag{2}
\]
and precisely two interior zeros counting multiplicity. They are simple
for \(0<|\tau|\le\sigma\); the only singular fiber in this time disk is
\(\tau=0\). Thus
\[
 X_\tau=\{(x,w):|x|\le r,\ w^2=H(T+\tau,x_*+x)\},
 \qquad\omega_\tau=dx/w                                  \tag{3}
\]
is a smooth compact bordered annulus on the bounded window. Its Euler
characteristic is \(2\chi(D)-2=0\); even boundary monodromy gives two
boundary components. Its complex orientation fixes all integrals.
At a simple branch use \(x=\alpha+\xi^2\); \(\omega\) is regular.
There is no pole or branch-point excision payment on a smooth fiber.
At the nodal fiber the differential is singular; that fiber is not included
in the finite enclosure contract.

Let \(h(x)=H(T,x_*+x)=x^2g(x)\). Choose \(\sqrt A\), continue
\(\sqrt g\), and label the outer lift by
\[
 w=x\sqrt{g(x)}\left(1+\frac{H(T+\tau,x_*+x)-h(x)}{h(x)}\right)^{1/2}
                                                        \tag{4}
\]
with the root near 1. The other lift has the opposite sign. Take the
counterclockwise labeled outer lift as the core generator \(c_\tau\).
This is the opposite orientation to BW13's \(\delta_\tau\);
\(q=\oint_{c_\tau}\omega=-Q_{\rm BW13}\).
No first four-jet coefficient comparison is reopened.

Choose the two points over \(x=r\) as marked boundary basepoints. Join
them by a simple arc \(\beta\) in the annulus, transverse to the core,
and cut along it to a disk \(D_\tau\). Its lift, homotopy, orientation,
and integration atlas must be supplied with an acquisition. Transport the
marked cut on the real time interval; avoid the branch points, or use
their regular \(\xi\) charts. Both physical boundaries and both copies
of \(\beta\) remain in \(\partial D_\tau\). Set \(F(p_0)=0\) at one
cut corner and \(dF=\omega\) throughout this single disk. The same
primitive must be used on every edge.

## 2. Complete boundary energy and its error

The exact energy and Stokes formula are
\[
 \mathcal E_\tau=\frac i2\int_{X_\tau}\omega\wedge\bar\omega
       =2\int_\Omega\frac{dA_x}{|H|}
       =\frac i2\oint_{\partial D_\tau}F\bar\omega.        \tag{5}
\]
Indeed \(d(F\bar\omega)=\omega\wedge\bar\omega\).
For paired cut edges orient \(e_+\) as part of \(\partial D\), and
identify \(e_-\) oppositely under gluing. Then
\[
 \int_{e_+\cup e_-}F\bar\omega
       =J_e\overline{P_e},\quad
 J_e=F_+-F_-,\quad P_e=\int_{e_+}\omega.                 \tag{6}
\]
The jump is constant. Every unpaired physical boundary arc remains.
Independent choices of primitive constants on the two boundary components
erase the transverse connector and do not give (5).

For comparison, on a compact boundaryless surface the usual symplectic
edge pairs give \(\sum_j\operatorname{Im}(\bar A_jB_j)\), with
\(a_j\cdot b_j=+1\). This normalization agrees with
[Grava, §3.1.2, Lemma 3.1.16 and Corollary 3.1.17][bilinear], checked
22 October 2026. The present annulus has no compact genus-one period
pair and cannot be capped without additional differential and boundary
data. Its transverse path is a relative period.

Here is a complete, conditional enclosure interface. Parametrize each
oriented edge by \(s\in[0,1]\), and write its pulled-back form as
\(\omega=b_j(s)ds\). Suppose certified functions satisfy
\[
 |F_j-\widehat F_j|\le\delta f_j,\qquad
 |b_j-\widehat b_j|\le\delta b_j.
\]
The bounds include path position, tangent and endpoint uncertainties in
the same atlas, rather than just integrand error on an uncertain path.
If \(\widehat E\) is the real part of a computed version of
\((i/2)\sum_j\int\widehat F_j\overline{\widehat b_j}\,ds\), then
\[
 |\mathcal E-\widehat E|\le E_{\rm int}
 +\frac12\sum_j\int_0^1
  (\delta f_j|\widehat b_j|+|\widehat F_j|\delta b_j
                       +\delta f_j\delta b_j)\,ds=:E_* . \tag{7}
\]
Here \(E_{\rm int}\) includes outer quadrature and arithmetic rounding.
Intersect \([\widehat E-E_*,\widehat E+E_*]\) with \([0,\infty)\).
Primitive errors come from paid path integrals of the same form, including
the common normalization and relative-period errors. Equation (7) is not
an acquired interval and is not an independent upper energy estimate.

## 3. Complete source and singular neighborhoods

Home [02][source] supplies the common canonical source. For
\(\operatorname{Re}t\le S\), \(|\operatorname{Im}z|\le Y\), spatial
derivatives of order \(j\) are bounded by
\(M_{j,Y}(S)=\int u^j e^{Su^2+Yu}\Phi(u)du\).
Use the complete source and the simultaneous event equations
\(H(T,x_*)=H_z(T,x_*)=0\); independently varied error bars may only be
used as a stated relaxation of this common-source feasible set.

An explicit acquisition ledger extends [the scalar source contract, §2][scalar]
to complex spatial domains. Keep \(n\le N\), \(0\le u\le U\), \(U\ge1\).
Put \(k=N+1\), \(\lambda_n=\pi n^2\),
\[
 \rho=((k+1)/k)^4e^{-\pi(2k+1)},\quad b=4\lambda_k-9-Y.
\]
If \(\rho<1\), \(b>0\), \(S\le8\lambda_k\), the entire omitted-mode
half-line is bounded by
\[
 L_{j,Y}=\frac{2\lambda_k^2e^{-\lambda_k}j!}
                    {(1-\rho)b^{j+1}}.                 \tag{8}
\]
For each retained mode let
\(b_n=4\lambda_ne^{4U}-9-2SU-Y>0\). If also
\(S\le8\lambda_ne^{4U}\), its omitted exterior ray is bounded by
\[
 R_{n,j,Y}=2\lambda_n^2e^{SU^2+(9+Y)U-\lambda_ne^{4U}}
       \sum_{a=0}^j {j\choose a}\frac{U^{j-a}a!}{b_n^{a+1}}. \tag{9}
\]
To prove (8), bound the positive leading terms geometrically in \(n\)
and use \(e^{4u}\ge1+4u+8u^2\). For (9), set \(u=U+v\), use the
same inequality for \(e^{4v}\), and expand \((U+v)^j\).
The negative summand is dropped only for these upper bounds, and is
retained in finite integration. These are disjoint omitted pieces.

Finite quadrature requires derivative enclosures, for example composite
midpoint error \(\sum h_\ell^3\sup_{\ell}|f''|/24\), plus outward
rounding of coefficients, nodes and transcendentals. Spatial and time
uncertainty require higher moments on the enlarged tube. Full reflection
holds for complete \(\Phi\), not independently for its head and tail.
No cutoff, source measurement or numerical event has been acquired here.

Absolute field error alone is insufficient to enclose reciprocal energy
on a cell that might contain a multiple root. On the unbranched complement,
with \(|H-\widehat H|\le\epsilon<|\widehat H|\), use
\[
 \frac1{|\widehat H|+\epsilon}\le\frac1{|H|}
       \le\frac1{|\widehat H|-\epsilon}.                \tag{10}
\]
The floor in (10) is paid on that complement, not assumed throughout
\(\Omega\). Near each of the two simple roots acquire a root-factor chart
\(H=(x-\alpha)V\), \(0<v_-\le|V|\le v_+\), on a root-centered disk
of radius \(\eta\). Its full two-sheet energy obeys
\[
       4\pi\eta/v_+\le\mathcal E_{\rm disk}
                           \le4\pi\eta/v_-.             \tag{11}
\]
This follows either by polar integration or by
\(\omega=2d\xi/\sqrt{V(\alpha+\xi^2)}\).
Acquire the root count, uncertain center, factor bounds, disk disjointness,
partition boundaries and their errors for both methods. Such simple-root
disks need not have radii or factor floors uniform as \(\tau\downarrow0\).
No global interior floor or limiting root gap is an input.

## 4. A finite upper bound from the complete event chart

The inherited chart supplies a constructive baseline, without assuming
an interior field floor or a root gap. For real \(0<\tau\le\sigma\),
BW13 gives
\[
 |H_{zz}-2A|\le|A|/2,\qquad
 |v(\tau)+2A\tau|\le |A|\tau/2,
 \quad v(\tau)=H(T+\tau,x_*+c(\tau)),                     \tag{12}
\]
where \(c(\tau)\) is the unique critical point. Reality and uniqueness
make \(c(\tau)\) real. After division by real \(A\), the function on
\([-r,r]\) is strictly convex, has negative critical value and positive
values at its endpoints. Its two roots \(\alpha<c(\tau)<\beta\) are real.
Taylor's theorem at \(c(\tau)\) gives
\[
 |\alpha-c(\tau)|,|\beta-c(\tau)|\ge\sqrt{6\tau/5},
 \qquad d=\beta-\alpha\ge2\sqrt{6\tau/5}.                \tag{13}
\]
Indeed \(|v|\ge3|A|\tau/2\) and \(|H_{zz}|\le5|A|/2\).

Factor \(H=(x-\alpha)(x-\beta)V(x)\). The divided difference formula
\[
 V(x)=\int_{s,t\ge0,\ s+t\le1}
 H_{zz}(T+\tau,x_*+s\alpha+t\beta+(1-s-t)x)\,ds\,dt
\]
follows by two applications of the fundamental theorem of calculus
along complex segments, with removable limits at repeated nodes.
The disk is convex and the simplex has area \(1/2\), so (12) implies
\[
 |V-A|\le|A|/4,\qquad |V|\ge3|A|/4.                    \tag{14}
\]
This is a deflated-unit floor derived from event curvature, not a floor
for \(H\) at its zeros.

For completeness, split the base disk into its intersections with the
two disjoint disks \(B(\alpha,d/2),B(\beta,d/2)\), and the remainder.
On the first disk \(|x-\beta|\ge d/2\); its integral of
\(1/(|x-\alpha||x-\beta|)\) is at most \(2\pi\), and similarly for
the second. On the remainder use
\(1/(pq)\le(p^{-2}+q^{-2})/2\); both distances lie between \(d/2\)
and \(2r\). Consequently
\[
 \int_\Omega\frac{dA}{|x-\alpha||x-\beta|}
       \le4\pi+2\pi\log(4r/d).
\]
The full two-sheet energy obeys the completely specified upper bound
\[
 \boxed{\mathcal E_\tau\le B(\tau):=
 \frac8{3|A|}\left[4\pi+2\pi\log\left(2r\sqrt{\frac5{6\tau}}\right)\right].}
                                                               \tag{15}
\]
Thus \(\mathcal E_\tau\in[0,B(\sigma/2)]\) uniformly on the declared
bounded window. This is a parameterized analytic enclosure: its event
curvature and source moments have not been acquired for an actual theta
event. It is a direct reciprocal majorant available to both methods.
It grows as \(\log(1/\tau)\); it provides no endpoint exclusion.

## 5. Declared comparison and next gate

The comparator evaluates exactly the middle expression in (5), receiving
the same source cells, moments, reflection and matching constraints,
root charts, cuts, path observations, precision and rounding allowances.
It may use any paid change of variable or relative-period information.
Compare complete intervals, not an isolated favorable boundary term.
Success is strict interval containment, a smaller paid upper endpoint,
or a measured total acquisition/evaluation benefit. Both methods inherit
(15), so this baseline supplies no Hodge estimating advantage. No such
benefit has been established for actual theta in this round.

Before any theta campaign, the [quadratic pilot][pilot] tests the proposed
compression to a bounded core period and bounded exterior data. It fails:
the transverse connector carries the missing degeneration. This stops
that compression only. The next admissible candidate must specify a
coupled bound on the relative period **and** full physical boundary term,
or a concrete acquisition comparison for them; it must survive (7) and
the direct comparator. Merely bounding source moments or increasing
period precision does not supply that estimate.

[program]: ../research-overview/01_RECIPROCAL_HODGE_ENERGY_PROGRAM_20261022.md
[pilot]: 02_FULL_QUADRATIC_ENERGY_AND_TRANSVERSE_PAYMENT_20261022.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[source]: ../../02_theta_source_constraints/README.md
[scalar]: ../../03_heat_transport_and_charges/notes/03_SCALAR_SOURCE_CONTRACT_AND_SURVIVOR_WIDTH_20261022.md
[bw13]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/13_spectral_covers_and_periods/notes/01_NODAL_PERIOD_VARIATION_AND_FOUR_JET_COMPARISON_20261021.md
[bilinear]: https://people.sissa.it/~grava/RS2021.pdf
