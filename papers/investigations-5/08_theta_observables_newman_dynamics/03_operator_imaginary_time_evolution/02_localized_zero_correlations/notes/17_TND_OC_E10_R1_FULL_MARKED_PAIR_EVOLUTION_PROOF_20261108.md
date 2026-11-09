# TND-OC-E10 r1 — time modulus for the full marked Gaussian pair

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Runtime model `gpt-6.1-sol`, reasoning
effort unavailable. OC chat0008. **Proved in-note, proof-author checked,
pending separate internal assessment E12.** The proof uses the assessed
parent inputs at their existing evidence levels.

[Result index][results], [avoid index][avoid], [geometry13][geometry],
[controls12][controls], [classification01][a01], [premises02][a02],
[scope07][a07] and [sibling reuse15][a15] set the scope. This is a
quantitative evolution bound for a fixed smoothed statistic. An
independently supplied profile at one time gains an explicit additive
transport allowance through the whole interval. The estimate is
compatible with collisions and supplies no RH criterion.

## Setting and theorem

Use the complete canonical \(H_\lambda\), \(\partial_\lambda H=-H_{zz}\),
with \(0\le\lambda\le1/2\) and zeros \(z_j=x_j+iy_j\) counted by
multiplicity labels. Keep [B06][b06] and [B09 (1)–(2)][design] fixed. For
each finite \(T\ge10\), take \(X\) uniform on the whole \([T,2T]\), \(h=1\),
\[
 \ell=\min(1,4\pi/\log T),\qquad
 \tau=1/4,\quad \epsilon=\tau\ell,\quad J=\ell^2,\qquad
 Q=[-1,1]+i[-1,1].
\]
All of these are fixed in Newman time. Set \(W_X(z)=w_{X,1}(x)\kappa_0(y)\)
as in the [existing window][window], and use the complete planar Gaussian
\(G_\epsilon(w)=(2\pi\epsilon^2)^{-1}\exp(-|w|^2/(2\epsilon^2))\). Write
\[
 \begin{aligned}
 f_{X,u}(z)&=J W_X(z)G_\epsilon(X+\ell u-z),\\
 r_{\lambda,X}(u)&=\sum_j f_{X,u}(z_j),\\
 d_{\lambda,X}(u,v)&=\sum_j f_{X,u}(z_j)f_{X,v}(z_j),\\
 R_{2,\lambda,X}&=r_{\lambda,X}\otimes r_{\lambda,X}-d_{\lambda,X},\\
 \overline r_\lambda&=\mathbb E_X r_{\lambda,X},\qquad
 \overline R_{2,\lambda}=\mathbb E_X R_{2,\lambda,X},\\
 C_\lambda&=\overline R_{2,\lambda}
                    -\overline r_\lambda\otimes\overline r_\lambda .
 \end{aligned}
\]
The tensor product is the pointwise product in the two separate
observation coordinates. It uses one center in \(R_{2,\lambda,X}\).
The self term has \(J^2W_X^2\) and deletes precisely \(j=k\). If
\(m\) labels coincide, their ordered \(m(m-1)\) distinct-label terms
remain. The observation function retains both real and imaginary
coordinates at each mark and does not truncate the Gaussian.

Let \(A\ge1\) be the finite absolute constant of [parent Note18 (4)][p18],
and \(L=\log(2+2T)\). Define
\[
 \begin{aligned}
 a_0&=\frac{J}{2\pi\epsilon^2}=\frac1{2\pi\tau^2},\\
 a_1&=a_0\left(\frac{15}{4}+\frac1{\epsilon\sqrt{\mathrm e}}\right),\\
 a_2&=a_0\left(24+\frac{15}{2\epsilon\sqrt{\mathrm e}}
                        +\frac1{\epsilon^2}\right),\\
 R_*&=2ALa_0,\qquad L_1=A^2L^2(48a_2+124a_1),\\
 L_d&=A^2L^2[96(a_0a_2+a_1^2)+248a_0a_1],\\
 L_2&=2R_*L_1+L_d,\qquad L_C=4R_*L_1+L_d .
 \end{aligned}                                                   \tag{1}
\]
For \(\lambda,\mu\in[0,1/2]\), the sup norm differences of
\(r_{\lambda,X}\), \(d_{\lambda,X}\) and \(R_{2,\lambda,X}\) at the two
times are bounded by \(L_1|\lambda-\mu|\), \(L_d|\lambda-\mu|\) and
\(L_2|\lambda-\mu|\), uniformly in \(X\). The first and pair bounds
hold with the same constants for \(\overline r_\lambda\) and
\(\overline R_{2,\lambda}\). For \(C_\lambda\) the bound is
\(L_C|\lambda-\mu|\). The norms are on \(Q\) or \(Q^2\) as appropriate.
There is no minimum root gap in (1). The exterior derivative and
integrated errors are given in §4.

## 1. General compact-test estimate

Use the canonical strip \(|y|\le1\) and the uniform bounds from
[parent Note17][p17] and [parent Note18][p18], with [E09][p09r] and
[E13][p13r]. Let \(\mathcal C_X=\{j:|x_j-X|\le3\}\),
\(n_X=|\mathcal C_X|\), \(m_X=\#\{j:|x_j-X|\le1\}\), and
\(L_X=\log(2+X)\). The imported estimates are \(n_X\le12AL_X\),
\(m_X\le2AL_X\), and \(|E_X(z)|\le31AL_X\) for \(|x-X|\le1,\ |y|\le1\),
where \(E_X\) is the exterior of the full opposite-paired field. In
particular, \(A\) covers time zero and has no assigned numerical value.

For real \(C^2\) \(f\) supported in \(|x-X|\le1\), take
\(F_1=\sup_{|y|\le1}|\nabla f|\), \(F_2=\sup_{|y|\le1}\|D^2f\|_{\rm op}\)
using the Euclidean norm. Write \(S_f=\sum_j f(z_j)\). At any time
with simple roots throughout a collar of this support, the implicit
function theorem and local root exhaustion give the finite chain
rule. The terms for roots in the collar beyond the support vanish.
For each active root the complete Newman-time velocity is
\(2\sum_{k\in\mathcal C_X,\ k\ne j}(z_j-z_k)^{-1}+2E_X(z_j)\).
The collision-time velocity has the opposite sign. If \(d=x_j-x_k\),
\(e=y_j-y_k\), then the contribution of an unordered local pair to
\(\partial_\lambda S_f\) is \(-2K_f(z_j,z_k)\), where
\[
 \begin{aligned}
 K_f(z_j,z_k)
 &=\frac{(f_y(z_j)-f_y(z_k))e-(f_x(z_j)-f_x(z_k))d}{d^2+e^2}\\
 &=\int_0^1\frac{e^2 f_{yy}(z_k+\theta(z_j-z_k))
                  -d^2 f_{xx}(z_k+\theta(z_j-z_k))}
                  {d^2+e^2}\,d\theta .
 \end{aligned}                                                   \tag{2}
\]
The two mixed derivatives cancel in the chord integral. The chord
lies in the closed strip, so \(|K_f|\le F_2\). This uniform bound
requires no continuous extension to the diagonal. Keep only pairs
with at least one label in the support strip \(|x-X|\le1\). In a pair
with one active and one inactive label, the inactive gradient is
zero, so (2) uses only the active velocity. Distinct inactive labels
at the same repeated root require neither a quotient nor a velocity.
Their multiplicities still enter the forces on active labels.

At most \(m_X n_X\) unordered pairs enter. The exterior contribution
is \(2\sum_{j\ {\rm active}}\nabla f(z_j)\cdot
(\Re E_X(z_j),\Im E_X(z_j))\), with its two components included.
Thus
\[
 |\partial_\lambda S_f|
 \le 2m_X n_X F_2+2m_XF_1(31AL_X)
 \le A^2L_X^2(48F_2+124F_1).                                  \tag{3}
\]
This extends the parent's scalar calculus to the general compact
test used here. It is evaluated instantaneously. Membership in
\(\mathcal C_X\) is a force decomposition, so differentiating an
indicator of that cluster is unnecessary.

## 2. Gaussian and product constants

The cutoff \(P(t)\) equals 1 for \(t\le0\), equals
\(1-10t^3+15t^4-6t^5\) on \([0,1]\), and equals 0 for \(t\ge1\).
Its first two derivatives vanish at both junctions.
On \((0,1)\), \(|P'|=30t^2(1-t)^2\le15/8\), while
\(|P''|=60t(1-t)|1-2t|\le10/\sqrt3<6\) by maximizing
\(15s(1-s^2)\) over \(s=|1-2t|\in[0,1]\).
Thus \(0\le w_{X,1}\le1\), \(|w_{X,1}'|\le15/4\) and
\(|w_{X,1}''|\le24\). The transverse cutoff \(P(|y|-1)\) has
value 1 and both derivatives zero throughout \(|y|\le1\),
including its edges. Each cutoff is constant near the kink of its
absolute-value argument.

Write \(b=(2\pi\epsilon^2)^{-1}\) and \(\rho=|w|/\epsilon\).
The gradient norm is \(b\epsilon^{-1}\rho e^{-\rho^2/2}\),
maximized at \(\rho=1\). The Hessian eigenvalues in the radial and
tangential directions are \(b\epsilon^{-2}(\rho^2-1)e^{-\rho^2/2}\)
and \(-b\epsilon^{-2}e^{-\rho^2/2}\), with the same value at
\(w=0\). For \(s=\rho^2\), \(|s-1|e^{-s/2}\le1\) on \([0,1]\),
and on \([1,\infty)\) its maximum is \(2e^{-3/2}<1\) at \(s=3\).
Consequently \(\|D^2G_\epsilon\|_{\infty,\rm op}\le b/\epsilon^2\).
Translation and reflection in \(w=X+\ell u-z\) preserve these norms
for \(z\) derivatives. The product rule for \(JW_XG_\epsilon\)
gives the first three constants in (1), with the two mixed terms
costing \(2(15/4)a_0/(\epsilon\sqrt{\mathrm e})\). They hold
uniformly on the strip for all observations.

For \(f=f_{X,u}\), \(g=f_{X,v}\),
\(\nabla(fg)=f\nabla g+g\nabla f\) and
\[
 D^2(fg)=fD^2g+gD^2f+\nabla f\otimes\nabla g+
                                  \nabla g\otimes\nabla f.
\]
The operator norm of a rank-one term is the product of the two
vector norms. Hence \(F_1(fg)\le2a_0a_1\) and
\(F_2(fg)\le2a_0a_2+2a_1^2\). These are physical \(z\) derivatives,
so \(J\) and \(\epsilon\) are precisely those in (1).

## 3. Pathwise and averaged bounds across all multiple events

Since \(L_X\le L\), (3) for \(f_{X,u}\) and \(f_{X,u}f_{X,v}\)
gives \(L_1,L_d\) for the respective derivatives. Also
\(0\le r_{\lambda,X}\le m_Xa_0\le R_*\).
On simple intervals the product rule costs at most \(2R_*L_1\)
for \(r_{\lambda,X}(u)r_{\lambda,X}(v)\). Including the derivative
of the same-label term gives \(L_2\).

Here is the assembly for every center using [parent Note19 §§2–4][p19].
Take the common closed padded box
\(K=[T-2,2T+2]\times[-2,2]\) in real coordinates.
At each reference time, choose a rectangle with horizontal sides
\(y=\pm2\) and vertical sides in the collars of the union of all
supports \([T-1,2T+1]\), avoiding the finitely many zero abscissae
at that time. Its boundary stays zero free in a time neighborhood.
The argument principle and Rouché's theorem in small disjoint
root disks preserve each multiplicity and give continuous
convergence of the root multiset. All contributing roots are inside.
Summing the continuous functions \(f_{X,u}\) and \(f_{X,u}f_{X,v}\)
over that multiset gives joint continuity in time, center and
observation parameters. Globally \(C^2\) zero extension already
accounts for smooth support crossings in the derivatives.

The repeated points in \([0,1/2]\times K\) satisfy
\(H_\lambda(z)=H_{\lambda,z}(z)=0\) and form a compact set.
The analytic family has nonzero slices (\(H_\lambda(0)>0\)).
At each multiplicity \(m\ge2\) the parent Hermite exhaustion gives
\(z_j=z_0+\sqrt{2(\lambda-\lambda_0)}h_j+O(|\lambda-\lambda_0|)\)
with distinct \(h_j\). The \(m\) labels exhaust the single isolating disk of the event. Their leading
separations dominate the error for sufficiently close nonzero time
on either side. At the event time the disk has only the center root.
Thus each repeated point is isolated in space and time, also at
box and time boundaries by the same local argument. Compactness
gives finitely many such points and finitely many projected times.
Simultaneous events at different roots are included.

On each complementary interval the roots in the contributing
rectangle have simple analytic local labels. The derivative bounds
are uniform in \(X,u,v\). Integrate on the intervals, take one-sided
limits by continuity, and sum the durations of their intersections
with \([\min(\lambda,\mu),\max(\lambda,\mu)]\). This proves the
global bounds for \(S_f\) with (3) and for \(r,d,R_2\) with (1).
There is no factor for the number of events. For \(S_f\) one can
use a rectangle around its own support inside the same box.

For \(\overline r,\overline R_2\), continuity gives measurability
and the bounds are uniform under the fixed probability average.
Differentiation on the common simple intervals also follows by
dominated convergence from these uniform difference bounds.
For the connected subtraction use
\(\|\overline r_\lambda\|_\infty\le R_*\) and
\[
 \|\overline r_\lambda\otimes\overline r_\lambda-
         \overline r_\mu\otimes\overline r_\mu\|_\infty
 \le 2R_*L_1|\lambda-\mu|.
\]
This is the separate additional cost that gives \(L_C\).
The inequalities hold for every pair of observation points, so
taking the supremum controls the full function. Interactions with
a third label can occur in a signed derivative of the pair.
Here they are bounded through the scalar pathwise estimate and
the population bound, without factorizing a third intensity.
The bound controls magnitude and has no signed derivative
information. There is no normalization by the local count.

## 4. Complete exterior and integrated cutoff error

For active \(z=x+iy\) put \(w=x+4i\) and
\(\mathcal F_\lambda=H_\lambda'/H_\lambda\). The full field is
\[
 E_X(z)=\mathcal F_\lambda(w)
 -\sum_{k\in\mathcal C_X}\frac1{w-z_k}
 +\sum_{k\notin\mathcal C_X}
     \left(\frac1{z-z_k}-\frac1{w-z_k}\right).
                                                               \tag{4}
\]
This is parent Note18 (11), obtained from the complete
opposite-paired Hadamard sum by subtracting the finite cluster
and comparing at \(z,w\). The safe-line term is exact. In the
absolute difference series, each term is bounded by
\(5/|x-x_k|^2\) and the shell \(h\le|x-x_k|<h+1\), \(h\ge2\),
has at most \(2A[L_X+\log(h+2)]\) exterior labels.
The full absolute difference cost is \(\le25AL_X\), by
parent Note18 (12)–(13). The safe-line and finite subtraction
costs are \(\le2AL_X\) and \(\le n_X/3\le4AL_X\).
This accounts for \(31AL_X\) with the original pairing.

For integer \(M\ge2\), replace just the difference series in (4)
by its terms with \(|x-x_k|<M\). The discarded series is bounded by
\[
 \begin{aligned}
 10A\sum_{h=M}^\infty\frac{L_X+\log(h+2)}{h^2}
 &\le 10A\int_{M-1}^\infty\frac{L_X+\log(t+2)}{t^2}\,dt\\
 &=10A\left(\frac{L_X+\log(M+1)}{M-1}
            +\frac12\log\left(1+\frac{2}{M-1}\right)\right)\\
 &\le e_M(X):=\frac{10A}{M-1}[L_X+\log(M+1)+1].
 \end{aligned}
\]
The integrand decreases for \(t\ge1\), and the last line uses
\(\log(1+s)\le s\). Formula (3)'s exterior term then incurs an
absolute derivative error \(\le2m_XF_1e_M(X)\). In this replacement
the roots and the multiplying profile values remain the exact
canonical ones.

Let \(m_*=2AL\) and
\(e_M^*=10A[L+\log(M+1)+1]/(M-1)\). First and self derivative errors
are bounded by \(2m_*a_1e_M^*\) and \(4m_*a_0a_1e_M^*\).
In the pathwise product of first intensities the two differentiated
factors give a combined \(4R_*m_*a_1e_M^*\), since each undifferentiated
factor is bounded by \(R_*\). The raw pair and connected errors
are therefore
\[
 B_{2,M}=(4R_*m_*a_1+4m_*a_0a_1)e_M^*,\qquad
 B_{C,M}=(8R_*m_*a_1+4m_*a_0a_1)e_M^* .                      \tag{5}
\]
For the second bound the derivative of the product of the averaged
first intensities adds a second \(4R_*m_*a_1e_M^*\).
All cutoffs are Borel in the parameters: each finite sum is
locally a symmetric sum over a finite root multiset, with closed
or open inequalities defining the memberships. For the truncated
difference sums the horizontal search is bounded at fixed \(M,T\)
and one can use a rectangle with a collar for that larger region.
Multiplicity at exterior events creates no singular term in (4).
The uniform summability of the difference series supplies the
corresponding measurability of its full sum.

The exact profiles are Lipschitz, hence absolutely continuous
pointwise. The time integrals of the exact derivatives give the
profile increments, and assignment of integrands at the finite
relevant event times is immaterial. At fixed \(X\) the scalar
integrated error is \(\le2m_*F_1e_M^*|\lambda-\mu|\) (or
\(2\sup_s m_X(s)F_1e_M(X)|\lambda-\mu|\) locally).
For the averaged pair and connected increments it is
\(B_{2,M}|\lambda-\mu|\) and \(B_{C,M}|\lambda-\mu|\) in sup norm,
by bounded integration and averaging. The integrands obtained by
the substitution in (4) are approximations to derivatives along
the exact divisor. This argument preserves the complete dynamics
and all Gaussian weights.

## 5. Transport, height cost and exact quadratic check

Suppose an independently supplied \(\widehat R_\mu\) has
\(\|\overline R_{2,\mu}-\widehat R_\mu\|_{\infty,Q^2}\le e_0\).
The triangle inequality gives error \(\le e_0+L_2|\lambda-\mu|\)
for \(\overline R_{2,\lambda}\) against that same profile.
For a connected initial approximation use \(L_C\). In particular
this gives the time-zero version in B09 (16). With the prescribed
\(\epsilon\), \(a_0=O(1), a_1=O(\log T), a_2=O((\log T)^2)\) as
\(T\to\infty\). Thus \(R_*=O_A(\log T)\), \(L_1,L_d=O_A((\log T)^4)\)
and \(L_2,L_C=O_A((\log T)^5)\). This is an upper allowance in the
prescribed blur regime. There is no numerical evaluation of \(A\)
or evidence of optimality.

In the local two-label model \(z^2-2\lambda\), use physical
coordinates, \(W=1\) near the roots and the Gaussian without the
unfolding prefactor, as in B09 (17). Let
\(F(u,v)=G_\epsilon(u)G_\epsilon(v)\) and
\(D_x=\partial_{\Re u}-\partial_{\Re v}\),
\(D_y=\partial_{\Im u}-\partial_{\Im v}\).
On the positive side the two ordered contributions are the
translations of \(F\) by \(\pm\sqrt{2\lambda}\) along the
\(D_x\) direction. Their Taylor sum is
\(2F+2\lambda D_x^2F+O(\lambda^2)\). For negative local parameter
the displacement is along \(D_y\) with length \(\sqrt{2|\lambda|}\),
so the sum is \(2F-2\lambda D_y^2F+O(\lambda^2)\).
This gives one-sided slopes \(2D_x^2F\) and \(-2D_y^2F\), with
right-minus-left jump \(2(D_x^2+D_y^2)F\). At \(u=v=0\) the
exact ordered sum is
\[
 2(2\pi\epsilon^2)^{-2}e^{-2|\lambda|/\epsilon^2}.
\]
Its value at the double root counts both ordered pairs. The
right-minus-left derivative jump is
\(-8(2\pi\epsilon^2)^{-2}/\epsilon^2\). A fixed nonunit \(J\)
would simply multiply these pair quantities by \(J^2\).
The two-sided diagnostic also fits an interior time by replacing
\(\lambda\) with \(\lambda-\lambda_0\) in this local polynomial.
It shows that in the local analytic heat class a Lipschitz profile
can have a kink at a collision. It supplies no canonical event.

## 6. Controls and evidence boundary

This is the premise screen of [B09 §6][design] against the existing
[collision register][controls], with the proven estimate substituted
for the target. The chord identity is generic for the local analytic
heat class with the stated force decomposition and bounded test
derivatives. The canonical strip, counts and safe-line estimates
are paid inputs specific to this application. A control lacking
canonical provenance might still admit its own regularity bound
with suitable estimates.

| Control | Premise check and scope |
| --- | --- |
| Euler-factor | The unchanged theta/xi coefficients and completion fail. Local heat cancellation applies, while the common canonical strip/count/field package requires a separate proof for the modified family. |
| Weighted-square and finite theta-tail | Full normalized reflection and complete unit weights fail for the finite square truncations or nontrivial finite changes. Finite endpoint matches do not give canonical count and exterior inputs. Where the analytic heat hypotheses hold, the local argument can allow the recorded events. |
| Reflected super-Gaussian | The complete integer-square theta expansion fails. Reflection and the primitive endpoints can coexist with collision and local smooth-statistic calculus. |
| Smooth shape and positive primitive | The exact theta coefficient expansion fails. The positive shape and primitive data alone do not give the canonical inputs or B09's missing same-center joint estimate. |
| Finite-prime orbit | Full reflection and the all-coefficient identity fail despite finite constraints. Uniform canonical strip/field bounds are not transferred by those constraints. |
| Atomic and exact finite-profile thresholds | Complete theta profile and growth fail, as does eventual simplicity in these threshold examples. That last property is a distinction, not an E10 hypothesis. A locally finite analytic divisor may satisfy the compact assembly even with globally simultaneous events. |
| RH-conditional theta-close endpoint | Ordinary Dirichlet-series arithmetic fails. Doubles at an endpoint are consistent with Lipschitz regularity. No shared canonical numerical constant is assigned. |
| Variable observation kernel | The full cosine/Newman heat equation fails for the variable-kernel source, leaving the required zero-velocity step without its premise. This differs from smoothing observations of the fixed source. |
| Fractional-profile relaxation | Integer labelled-divisor realizability fails. Positivity of a fractional measure alone cannot give the ordered-label subtraction or finite-multiset assembly. |

Reflection rigidity for normalized polynomially weighted square combs
identifies the canonical source when both full reflection and the
complete square model hold. The four-family comparison separates
the failures of reflection and of integer-square support. Neither
comparison asks for a separating inequality from the present
regularity theorem. The quadratic check above directly exhibits
compatibility with collision. This screen uses the existing
witnesses and their scopes, without rerunning numerical certificates.

The B06/E08 transfer retains its internal shared-premise assessment
and supplies the observation convention, with initial profile
acquisition still separate. Green use still requires the paid
one-point term, unsmoothing/background/tails, a strict same-time
upper value and visibility. A gap application requires the initial
gap, isolation and signed exterior control. The frozen estimate
only concerns these fixed blurred first and pair observables in
the declared time and center regime. E03/E04 remain separate
pending assessments and E09 remains an optional finite benchmark.

All six [r1 obligations][request] have in-note proofs or premise
checks as specified. The displayed constants are unchanged. The
proof-author check covered inactive repeated labels, both cutoff
junctions, the common compact event set, the two differentiated
products, and the time integral of the exact exterior remainder.
No bounded repair or changed premise was needed. The claim status
awaits the separate E12 audit.

[request]: ../research-progress/handoffs/23_TND_OC_E10_R1_FULL_PAIR_EVOLUTION_REQUEST_20261108.md
[design]: 16_TND_OC_B09_FULL_PAIR_EVOLUTION_DESIGN_20261108.md
[window]: ../manuscript/sections/12_full_pair_transfer.tex
[b06]: 11_TND_OC_B06_CENTER_LAW_AND_JOINT_SOURCE_DECISION_20261108.md
[p17]: ../../notes/17_TND_O_E08_LOCALIZED_TRANSVERSE_CALCULUS_20261107.md
[p18]: ../../notes/18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md
[p19]: ../../notes/19_TND_O_E12_COLLISION_STABLE_MOMENT_ASSEMBLY_20261107.md
[p09r]: ../../reviews/06_TND_O_E09_LOCALIZED_CALCULUS_ASSESSMENT_20261107.md
[p13r]: ../../reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[geometry]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a15]: ../../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md
