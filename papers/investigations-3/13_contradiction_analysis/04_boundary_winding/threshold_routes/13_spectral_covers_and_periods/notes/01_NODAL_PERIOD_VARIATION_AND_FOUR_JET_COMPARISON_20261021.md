# BW-13: a paid nodal period and its first complete-source correction

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this research turn's metadata.

**Status: local analytic derivation, proved in-note; same-assistant
self-review only.** No independent or specialist review, acquired theta
event, numerical theta certificate, or simplicity conclusion.

The first correction to the regular vanishing period is
\[
 \boxed{\frac{P(\tau)}{2\pi i\sqrt A}
       =\tau+\kappa\tau^2+R_3(\tau),\qquad
 \kappa=\frac{5h_3^2-3h_2h_4}{48h_2^2},\quad
 |R_3(\tau)|\le C_3|\tau|^3.}                         \tag{1}
\]
Here \(h_j=H_{z^j}(T,a)\), \(h_0=h_1=0\), \(h_2\ne0\), and \(A=h_2/2\).
The constants and finite domain are specified below using the **complete**
theta source. This is conditional analysis at an assumed event, not a
claim that such an event exists.

The coefficient is exactly a combination of the existing BW-08 deflated
jet and a square:
\[
 \boxed{\kappa=\frac{3}{8}S_2+\frac{h_3^2}{16h_2^2},
 \qquad S_2=\frac{h_3^2}{9h_2^2}-\frac{h_4}{6h_2}.}     \tag{2}
\]
Thus this coefficient is a useful diagnostic and an interface to an
existing necessary bound, but does not add information to the same
four-jet. A positive coefficient is compatible with an even polynomial
having double endpoints and simple all-real zeros at every later time.

Read with the [program][overview], [progress register][progress],
[result index][results], [local-geometry cluster][local], and
[avoid index][avoid], particularly [classification][a01],
[matched controls][a02], [normalization][a08] and [scoped stops][a07].
The comparison declared before numerical checks is: does the first
post-quadratic coefficient provide a smaller admissible coefficient set
than direct use of the same complete event four-jet? Section 6 answers
no for this specific information class. Finite-time contour acquisition
and correlated source estimates are separate comparisons, not tested here.

## 1. Finite domain, regular time range, and branch contract

Use the unchanged normalization in [BW10's manuscript][manuscript]:
\[
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\quad H_t=-H_{zz},
\]
\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                    e^{-\pi n^2e^{4u}}.                \tag{3}
\]
All displayed moments include every index and the whole half-line.
Assume a real double event \((T,a)\), with \(T\ge0\). Set
\(x=z-a,\ \tau=t-T,\ h(x)=H(T,a+x)=x^2g(x)\), and
\[
 A=g(0)=h_2/2,\quad B=g'(0)=h_3/6,\quad C=g''(0)/2=h_4/24.
\]
Let, for \(j=2,3,4,6\),
\[
 M_j=\int_0^\infty u^j e^{(T+1)u^2+u}\Phi(u)\,du.
\]
These finite positive numbers bound the relevant spatial derivatives
on \(|x|\le1,\ |\tau|\le1\). A sufficient fully specified choice is
\[
 r=\min\{1,|A|/(4M_3)\},
\quad
 \sigma=\min\{1,\,3|A|r^2/(8M_2),\,|A|r/(4M_3),\,|A|/(4M_4)\}.
                                                               \tag{4}
\]
There is no uniform-in-height or uniform-in-event lower bound on these
radii. Small \(|A|\) can make this contract very expensive.

On the fixed circle \(C_r=\{|x|=r\}\), oriented counterclockwise,
Taylor's theorem gives
\[
 |g(x)-A|\le M_3r/6,\qquad |h(x)|\ge 3|A|r^2/4=:m_0,
\]
\[
 |H(T+\tau,a+x)-h(x)|\le M_2|\tau|\le m_0/2.
                                                               \tag{5}
\]
Consequently \(g\) has no zero in the closed disk, \(H\) has exactly
two zeros there counting multiplicity, and throughout this time disk
\[
 |H|_{C_r}\ge m:=3|A|r^2/8>0.                            \tag{6}
\]
The estimates are deliberately conservative.

There is exactly one critical time in this finite family, namely zero.
Indeed
\[
 |H_{zz}(T+\tau,a+x)-2A|\le M_3r+M_4\sigma\le |A|/2,
\]
and on \(C_r\)
\[
 |H_z-2Ax|\le M_3r^2/2+M_3\sigma\le3|A|r/8.
\]
Rouché's theorem gives a unique stationary point \(c(\tau)\) in the
disk; it is analytic because \(H_{zz}\ne0\). For
\(v(\tau)=H(T+\tau,a+c(\tau))\),
\[
 v(0)=0,\quad v'=-H_{zz}(T+\tau,a+c(\tau)),\quad
 |v(\tau)+2A\tau|\le |A||\tau|/2.
\]
Hence \(v(\tau)\ne0\) for \(0<|\tau|\le\sigma\). The two interior zeros
are simple on that punctured time disk, and the outer boundary is
regular even at \(\tau=0\). No global all-real hypothesis was used.

Choose one square root of \(A\), then its holomorphic continuation
\(\sqrt{g(x)}\) on the disk. On a collar of \(C_r\) define
\[
 w(\tau,x)=x\sqrt{g(x)}
 \left(1+\frac{H(T+\tau,a+x)-h(x)}{h(x)}\right)^{1/2},     \tag{7}
\]
using the square-root branch equal to 1 at \(\tau=0\).
Inequality (5) makes this single-valued and holomorphic there.

Let \(\delta_\tau\) be the vanishing-cycle homology class represented
by the **negative** of this lifted outer boundary. It is transported
by (7); no labeling of the two roots around a time loop is required.
For the quadratic \(H=x^2-2\tau\) and real \(\tau>0\), this means
left-to-right on the cut with \(w=+i\sqrt{2\tau-x^2}\), returning on
the other sheet, exactly as in proposal C4.

The primary differential is the ambient regular form \(w\,dx\):
\[
 P(\tau)=\oint_{\delta_\tau}w\,dx=-\oint_{C_r}w(\tau,x)\,dx.
                                                               \tag{8}
\]
The two boundary components of this finite cover have been retained;
(8) selects one, whose homology is the annulus core. The nonzero
outer-boundary integral is the period itself, not a boundary term
discarded from an interior estimate.

The comparison differential \(dx/w\) gives
\[
 Q(\tau)=-\oint_{C_r}\frac{dx}{w(\tau,x)},\qquad
 Q(0)=-\frac{2\pi i}{\sqrt A}.                            \tag{9}
\]
At the node its pullback to the normalization has a pole. By contrast,
\(P(0)=0\). For \(A=1,\ g=1\), (8)-(9) recover **both** exact
baselines \(P=2\pi i\tau,\ Q=-2\pi i\).

## 2. Variation with moving branches and boundary transport paid

For any closed moving lift parameterized by \(x=x(\tau,s)\),
\[
 \partial_\tau(w\,x_s)
   =w_\tau x_s+\partial_s(w\,x_\tau).
\]
The last term integrates to zero by periodicity of the **lifted**
closed curve. This is the transport cancellation, not an assumption
that the branch points are stationary.

In a cut representation \(P=2\int_{\alpha(\tau)}^{\beta(\tau)}w\,dx\),
the first derivative's endpoint terms are
\(2[w(\beta)\beta'-w(\alpha)\alpha']=0\). Repeated naive
differentiation on that open cut is unsafe: the resulting
\(H^{-3/2}\) expressions are not ordinary integrable endpoint
functions, and endpoint cancellations cannot simply be dropped.
The fixed contour (8) retains the transported class and avoids this
problem. Its projected outer boundary has zero velocity.

Differentiating (8), where (6) holds, gives the exact formulas
\[
 P'=\frac12\oint_{C_r}\frac{H_{zz}}w\,dx,
\qquad
 P''=-\oint_{C_r}
 \left(\frac{H_{zzzz}}{2w}-\frac{H_{zz}^2}{4w^3}\right)dx.
                                                               \tag{10}
\]
Thus \(P'=-Q\) is particular to the normalized quadratic model;
it must not be imported for a general theta germ.

At zero time these are ordinary residues. The needed ones are
\[
 \operatorname{Res}\frac{h''}{2\sqrt h}=\sqrt A,
\]
\[
 \operatorname{Res}\left(\frac{h^{(4)}}{2\sqrt h}
                  -\frac{(h'')^2}{4h^{3/2}}\right)
 =\frac{3C}{2\sqrt A}-\frac{15B^2}{8A^{3/2}}.
\]
The signs in (8) and (10) therefore give
\[
 P(\tau)=2\pi i\sqrt A
 \left[\tau+
       \left(\frac{15B^2}{16A^2}-\frac{3C}{4A}\right)\tau^2\right]
       +O(\tau^3),
\]
which proves the coefficient in (1). Either choice of \(\sqrt A\)
changes the sign of \(P\) too, so the normalized coefficient is
unchanged. No assumption \(h_2>0\) is needed.

For an additional check, the singular differential has expansion
\[
 Q(\tau)=-\frac{2\pi i}{\sqrt A}
 \left[1+\left(\frac{9C}{2A}-\frac{21B^2}{8A^2}\right)\tau
       +O(\tau^2)\right].                                  \tag{11}
\]
Its nonzero limit remains the allowed nodal residue.

## 3. Complete remainder and a finite extraction error

For \(F=\sqrt H\), on the fixed contour,
\[
 F_{\tau\tau\tau}
 =\frac{H_{\tau\tau\tau}}{2\sqrt H}
  -\frac{3H_\tau H_{\tau\tau}}{4H^{3/2}}
  +\frac{3H_\tau^3}{8H^{5/2}}.
\]
The heat equation and (6) give
\[
 D_3=\frac{M_6}{2\sqrt m}
       +\frac{3M_2M_4}{4m^{3/2}}
       +\frac{3M_2^3}{8m^{5/2}},\qquad
 C_3=\frac{rD_3}{6\sqrt{|A|}}.                            \tag{12}
\]
Since the contour length is \(2\pi r\), Taylor's integral remainder
along the complex segment from 0 to \(\tau\) proves (1), uniformly
for \(|\tau|\le\sigma\). Complete moments through order six suffice.
The bound contains the boundary floor and all powers of its inverse.

If \(\sqrt A\) is known exactly, a finite-time estimator
\[
 \widehat\kappa_\tau
 =\frac{\widehat P(\tau)/(2\pi i\sqrt A)-\tau}{\tau^2}
\]
with \(|\widehat P-P|\le E_P\) satisfies
\[
 |\widehat\kappa_\tau-\kappa|
 \le C_3|\tau|+\frac{E_P}{2\pi\sqrt{|A|}\,|\tau|^2}.       \tag{13}
\]
For a boundary approximation with \(|\widehat H-H|\le\epsilon<m\),
choose its square root by the straight homotopy from (7).
Integrating the derivative of the square root along that homotopy
gives, including a separate contour-quadrature error \(\epsilon_I\),
\[
 E_P\le\frac{\pi r\epsilon}{\sqrt{m-\epsilon}}+\epsilon_I.
                                                               \tag{14}
\]
An uncertain normalizer needs its own propagation; (13) does not
silently treat it as exact. In particular the subtraction followed
by division by \(\tau^2\) can amplify an absolute integration error.
No smaller time is automatically a more accurate coefficient estimate.

### An explicit source-tail interface

For completeness, these moments have a finite acquisition interface;
no discarded source tail is being assigned zero. For
\[
 M_j(B,Y)=\int_0^\infty u^j e^{Bu^2+Yu}\Phi(u)\,du,\quad B,Y\ge0,
\]
put \(q_N=16e^{-\pi(2N+3)}<1\). The ratio of successive terms in
\(\sum_{n>N}n^4e^{-\pi n^2e^{4u}}\) is at most \(q_N\). Positivity
of each theta summand for \(u\ge0\), followed by dropping its negative
part only for an upper bound, gives
\[
 \sum_{n>N}\Phi_n(u)
 \le\frac{2\pi^2(N+1)^4}{1-q_N}
       e^{9u-\pi(N+1)^2e^{4u}}.
\]
Hence a simple, conservative mode-tail payment on \([0,U]\) is
\[
 E_{j,N}^{\rm modes}
 =\frac{2\pi^2(N+1)^4}{1-q_N}\frac{U^{j+1}}{j+1}
       e^{BU^2+(Y+9)U-\pi(N+1)^2}.                       \tag{15}
\]
For the whole-source \(u\)-tail choose \(U>0\) with
\[
 16\pi e^{4U}\ge2B,\quad
 \lambda_j=4\pi e^{4U}-2BU-Y-9-j/U>0.
\]
The log derivative of
\(u^j e^{Bu^2+(Y+9)u-\pi e^{4u}}\) is decreasing for \(u\ge U\)
and at most \(-\lambda_j\). Therefore
\[
 E_j^{\rm outer}
 =\frac{2\pi^2}{1-q_0}
   \frac{U^j e^{BU^2+(Y+9)U-\pi e^{4U}}}{\lambda_j}        \tag{16}
\]
bounds the remaining integral. Such a \(U\) exists for every fixed
\(B,Y,j\). A certified finite sum/integral would add its own rounding
and quadrature error to (15)-(16). Spatial derivatives obey the same
interface using \(|\partial_z^j\cos(zu)|\le u^j e^{|\Im z|u}\);
time derivatives add two powers of \(u\).

These formulas prove finiteness and give explicit upper bounds.
They are not evaluated theta moments or claims of efficient acquisition.
The event equations apply to the complete integral (3), never to a
finite source truncation forced to share its cancellations.

## 4. Relation to the existing necessary arithmetic bound

Equation (2) is direct algebra. Under the additional all-real
theta-slice hypothesis with \(a>0\), [BW-08 Note 04][bw08] proves
\[
 S_2>L_2(a)
 =\frac1{2a^2}+\frac1{4b}\log\frac{b+1}{4\pi}
                 -\frac4{a^2+b^2},
 \qquad b=\max(a,40),
\]
and \(L_2(a)>1/(2a^2)+1/(40b)\). Thus its already established
necessary condition translates to
\[
 \kappa>\frac{h_3^2}{16h_2^2}+\frac38L_2(a).             \tag{17}
\]
This is inherited evidence in new coordinates, not a new improvement
to BW-08's constant or proof. Its original internal-review qualifications
remain. A contradictory upper bound is still missing.

For a real-rooted polynomial \(h=x^2g\), with every root of \(g\)
away from zero,
\[
 S_2=-(\log|g|)''(0)=\sum_{\rho:g(\rho)=0}\frac{m_\rho}{\rho^2}
 \ge0.
\]
Thus positivity of \(\kappa\) is already generic in this class.
It cannot rule out the double event used to define the period.

## 5. Controls and exact finite checks

The local derivation uses joint analyticity, the heat equation, an
isolated double event and a nonzero boundary. Positivity and arithmetic
enter only the explicit theta moment majorants and the separately
imported bound (17). The [control register][controls] therefore gives
the following matched screen.

| Control | What survives here | Missing premise or restriction |
| --- | --- | --- |
| Quadratic heat | Both exact C4 periods and \(\kappa=0\). | No unchanged theta source/arithmetic; (17) is not asserted. |
| Cubic and quartic polynomial heat | Equations (8)-(12), with polynomial derivative bounds; corrections of either sign are possible without an all-real hypothesis. | No theta source/growth; complex-time events are not physical events. |
| Even polynomial \((z^2-a^2)^2\) | Double endpoints, evenness, positive-time simple all-real zeros, and \(\kappa=3/(4a^2)>0\) at \(+a\). | No positive theta-source representation or complete imaginary-axis growth. Positivity of the correction alone fails as an exclusion. |
| RH-conditional close-source BW10 controls | Local period law at their exact double endpoints; broad source/completion properties and positive-time all-real simplicity. | Ordinary Dirichlet-series arithmetic; added doubles escape in height. |
| Euler-factor controls | Local law at any qualifying double event; BW-08 explains why its scalar imaginary-axis floor can also hold. | Unchanged Euler coefficients fail. Failure of that identity does not imply failure of (17); no new event location is claimed. |
| Weighted-square and finite-prime controls | Local analytic heat/collision calculation at qualifying double events. | Full normalized reflection and unchanged coefficients fail; finite-source cases have no all-real slice and are not inserted into (17). |
| Reflected super-Gaussian and positive-primitive controls | Local period law wherever the specified analytic double-event hypotheses hold; source moment bounds use their own sources. | Canonical integer-square data and the unchanged xi identity fail; preservation lists are not combined. |

The even polynomial control can be checked for **every** positive
time, not just a sample. Its heat flow is
\[
 H_*(\tau,z)=z^4-(2a^2+12\tau)z^2+a^4+4a^2\tau+12\tau^2.
\]
As a quadratic in \(z^2\), its sum and product of roots are positive,
and its discriminant is \(32a^2\tau+96\tau^2>0\). Thus it has four
distinct real roots for every \(\tau>0\). At \(z=a,\tau=0\),
\(B/A=1/a,\ C/A=1/(4a^2)\), proving the stated correction.
The exact source-specific floor (17) is not assigned to this control.

The cubic proposal control \(z^3-(4+6\tau)z+2\) has simultaneous
zeros of \(H,H_z\) at \(z^3=1,\ \tau=(-4+3z^2)/6\).
Only one event is real, at \((z,\tau)=(1,-1/6)\). The others have
nonreal time. This prevents treating complex period singularities as
a count of physical endpoint events.

The [checker][checker] uses rational Laurent coefficients from the
finite polynomial heat flow, independently of the closed formula
for \(\kappa\), and compares with that formula in seven cases:

| Initial local polynomial \(h\) | Exact \(\kappa\) |
| --- | --- |
| \(x^2\) | \(0\) |
| \(x^2+x^3/5\) | \(3/80\) |
| \(x^2+3x^4/10\) | \(-9/40\) |
| \(x^2+x^3/5+3x^4/10\) | \(-3/16\) |
| \(x^2-x^4/9\) | \(1/12\) |
| \(x^2+x^3+x^4/4\), the normalized even control at \(a=1\) | \(3/4\) |
| The mixed quartic plus the checker's \(x^5,\ldots,x^8\) perturbation | \(-3/16\) |

The higher-jet perturbation changes the cubic time coefficient but not
\(\kappa\), as the formula requires. Fourteen ordinary floating
contour evaluations also check orientation, the two quadratic periods,
and the stated remainder with explicit polynomial derivative
majorants. They are **diagnostics, not interval certificates**.
The [small receipt][receipt] records parameters, exact fractions,
floating discrepancies and the script hash. The written derivations,
not the number of checks, carry the analytic statements.

## 6. What the coefficient comparison closes, and what remains open

Let \(\Omega\) be any fixed admissible set of event data
\((h_2,h_3,h_4)\), with \(h_2\ne0\), obtained from the same source
information. The possible first period coefficients are exactly
\[
 \left\{\frac{5h_3^2-3h_2h_4}{48h_2^2}:(h_2,h_3,h_4)\in\Omega\right\}.
\]
This is also the exact direct four-jet image. Reexpressing this
coefficient as a period cannot shrink that set without adding input.

For an explicit direct error payment, let
\(|A-\widehat A|\le e_A,\ |B-\widehat B|\le e_B,\
 |C-\widehat C|\le e_C\), with
\(a_*:=|\widehat A|-e_A>0\),
\(b_*:=|\widehat B|+e_B\), \(c_*:=|\widehat C|+e_C\).
Differentiating the rational expression along the straight segment gives
\[
 |\kappa-\widehat\kappa|
 \le\left(\frac{15b_*^2}{8a_*^3}+\frac{3c_*}{4a_*^2}\right)e_A
       +\frac{15b_*}{8a_*^2}e_B+\frac{3}{4a_*}e_C.         \tag{18}
\]
This includes uncertain normalization and can use the same full-source
tail payments. Different interval implementations need not attain the
same enclosure; equality concerns the information set, not every
implementation or running time.

More generally, every coefficient of \(\tau^n\) in this one nodal
period is determined by the spatial \(2n\)-jet at the event. To see
this, expand
\[
 [\tau^n]\sqrt{H(T+\tau,a+x)}
 =\sum_{p=1}^n {1/2\choose p}h^{1/2-p}
   \sum_{\substack{k_1+\cdots+k_p=n\\ k_j\ge1}}
       \prod_{j=1}^p\frac{(-1)^{k_j}h^{(2k_j)}}{k_j!}.
                                                               \tag{19}
\]
The residue needs the coefficient of \(x^{2p-2}\), since
\(h^{1/2-p}=x^{1-2p}g^{1/2-p}\). Each numerator needs derivatives
of order at most \(2k_j+2p-2\le2n\), and the denominator needs
\(h\) through order \(2p\le2n\). The constant term has zero residue.
Joint analyticity of the heat family justifies its time Taylor
series; no convergence theorem for arbitrary formal heat data is used.

**Scoped stop.** Stop the proposed use of the first normalized nodal
coefficient, or its positivity, as an additional simplicity
discriminator when it is calculated solely from the same event
four-jet and independent absolute source-moment bounds.
This leaves finite non-asymptotic periods, correlations between
different cycles, and genuinely new arithmetic period estimates open.
It is not an impossibility theorem for spectral-cover methods.

SCP-01 and the local-double portion of SCP-02 now have explicit
analytic contracts. SCP-03 has a completed, scoped coefficient
comparison; an actual finite theta acquisition/cost comparison is
unexecuted. SCP-04 remains gated. The next useful task must name an
estimate or acquisition advantage outside the same-four-jet class,
and compare against direct use of that same additional information.
The HMC-05 and HMC-06 statuses are unchanged.

## Literature boundary and review

The proof above is a direct contour/residue calculation. For background,
the originating proposal cites [Seidel, Vanishing cycles and mutation][seidel].
[Novikov, Modules of Abelian integrals and Picard-Fuchs systems][novikov],
especially its introduction and Section 1, works with polynomial
Hamiltonians regular at infinity. That hypothesis is not supplied by
the entire theta cover. Neither source is being used to assert a finite
global period system here. No literature priority claim is made.

The [self-review][review] checks normalization, source tails, moving
branches, the finite comparison scope, and the distinction between
analytic proofs and numerical diagnostics.

[overview]: ../research-overview/01_SPECTRAL_COVERS_AND_PERIODS_PROGRAM_20261021.md
[progress]: ../research-progress/01_SPECTRAL_COVERS_AND_PERIODS_PROGRESS_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../../../avoid/08_normalization_and_constant_slips.md
[manuscript]: ../../10_rh_implies_simple_zeros/manuscript/main.tex
[bw08]: ../../08_deflated_jet_hierarchy/notes/04_ALL_HEIGHT_MULTIPLICITY_JET_BOUND_20261020.md
[checker]: ../numerics/check_nodal_period.py
[receipt]: ../numerics/NODAL_PERIOD_CHECK_20261021.json
[review]: ../reviews/01_NODAL_PERIOD_SELF_REVIEW_20261021.md
[seidel]: https://arxiv.org/abs/math/0007115
[novikov]: https://www.wisdom.weizmann.ac.il/~dnovikov/Papers/irredend.pdf
