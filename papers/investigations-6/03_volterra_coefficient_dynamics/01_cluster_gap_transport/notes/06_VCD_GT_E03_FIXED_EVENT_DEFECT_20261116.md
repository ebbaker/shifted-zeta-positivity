# VCD-GT-E03 r2 — Signed quadrature defect near a fixed double event

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Explicit helper dispatch
**gpt-6.1-sol / ultra**. Separate backend attestation and actual lead
configuration are unavailable. The helper authored E01 and uses it
here with its separate internal assessment. E03 r1 is an inherited
proof dependency with separate assessment.

**Proved in-note conditional on one fixed isolated double event.**
All seven frozen input hashes matched. The contour retains the
four-factor degree loss of the field residual at the stipulated event.
The magnitude of the actual signed residual integral exceeds the
next-head discriminant error on shrinking slabs of length \(N^{-3}\),
and the absolute safety allowance overestimates the integral
on the fixed circle. This is a local comparison of the selected
estimator and a refinement of fixed-event resolution.
[Frozen request][request] [B02 decision][decision] [Result index][results]
[Local heat geometry][geometry] [Coefficient cluster][cluster]
[Avoid index][avoid] [Classification][a01] [Control screening][a02]
[Scope][a07] [Separate bounds][a12]

## 1. Conditional setting and relative error scale

Fix \(0<T<1/2\) and \(a\in\mathbb R\setminus\{0\}\). Assume the
complete normalized physical field \(F_\lambda\) has an isolated
double zero at \(z=a\) when \(\lambda=T\). Choose a circle
\(\Gamma=\{|z-a|=\rho\}\) avoiding the origin in its closed disk and
lying strictly inside \(|\Im z|<1\). Take it small enough that
\[
 F_T(z)=(z-a)^2 A_T(z),\qquad A_T(a)\ne0
\]
with \(A_T\) nonvanishing on the closed disk. Its value at \(a\) is
real by conjugation symmetry. Shrink a fixed compact interval
\(I\subset(0,1/2)\) about \(T\) so that there are two counted zeros
in a fixed smaller concentric disk throughout \(I\). This follows
from continuity and the argument-principle comparison on a smaller
circle, and gives a strictly positive outer buffer. Fix a positive
lower bound for \(|F_\lambda|\) on \(I\times\Gamma\), which exists
by compactness. All limiting statements here have \(N\to\infty\)
for this fixed event, interval and circle.

Use the notation \(h_j^*(\lambda)=\prod_{k=1}^j\beta_k(\lambda)\),
\(p_j(\lambda)=h_j^*(\lambda)/(2j)!\), and
\(\Delta_j=F_\lambda-G_{j,\lambda}\). The two input formulas are
\[
 \begin{aligned}
 \Delta_j(\lambda,z)&=L_j(\lambda,z)E_{j,\lambda}(z),
 & L_j(\lambda,z)&=(-1)^j p_j(\lambda)z^{2j},\\
 R_N(\lambda,z)&=(-1)^{N-1}
      \frac{h_N^*(\lambda)}{(2N-2)!}z^{2N-2}\Psi_{N,\lambda}(z).
 \end{aligned}                                                     \tag{1}
\]
Here \(R_N=(\partial_\lambda+\partial_z^2+\beta_1)G_{N,\lambda}\)
is the exact residual in E03 r1. On this fixed closed disk the
factors \(E_{j,\lambda}\) and \(\Psi_{N,\lambda}\) tend uniformly
to \(1\) on \(I\), by the explicit strip estimates. The proof uses
only those estimates, the actual residual/model equation and the
normalized physical heat law. [E01 §§1–3][e01] [E01 assessment][assess1]
[E03 r1 (1)–(7)][r1] [Parent fixed-event lemma][parent]

Set \(Z_*=\max_{\Gamma}|z|=|a|+\rho\) and
\(\bar p_j=\sup_{\lambda\in I}p_j(\lambda)\). The adjacent envelope yields
\(\bar p_j\le B_{j-1}^j/(2j)!\) with \(B_{j-1}=O(\log^2(j+1))\).
In particular for each fixed \(C>0\) and fixed \(k\ge0\),
\(j^k\bar p_j C^{2j}\to0\) by \((2j)!\ge j^j\).
On the fixed disk \(\sup|\Delta_j|=O(\bar p_j Z_*^{2j})\).
The same estimate at a single time uses \(p_j(\lambda)\) in place of
\(\bar p_j\). The residual bound on the disk is
\[
 \sup_{z}|R_N(\lambda,z)|
 \le C_0\,\frac{h_N^*(\lambda)}{(2N-2)!}\,Z_*^{2N-2},              \tag{2}
\]
with fixed \(C_0\) and all sufficiently large \(N\). These bounds
tend uniformly to zero, since
\(h_N^*/(2N-2)!=(2N)(2N-1)p_N\).
Strict comparison on the two circles now gives two counted
cluster zeros of each \(G_{j,\lambda}\) in the smaller disk for
all large \(j\), with one common buffer to \(\Gamma\).
A fixed collar of \(\Gamma\) inside the strip can also be taken.
Keep the physical floor positive there by continuity and use (1)
on that compact collar. The log-series comparison on the collar
has a boundary budget \(O(\bar p_j Z_*^{2j})\).
On \(\Gamma\), the model floors are bounded below and the model
\(z\)-derivatives are bounded uniformly by Cauchy's estimate on
a slightly larger compact region in the strip. In particular \(M_j\)
in E02 can be taken bounded. The coordinate comparison gives
\[
 \sup_I (|c_j-c|+|D_j-D|)=O(\bar p_j Z_*^{2j}).
 \tag{3}
\]
E02 then gives uniform \(K_j\to K\), with \(K_j\) the model unit
divided difference at its own pair. All of this geometry is local
to the assumed event. [E02 §§1–2][e02] [E02 assessment][assess2]

## 2. Signed residues and comparison at the event

At \(T\), use centered contour moments
\(m_{k,j}=(2\pi i)^{-1}\oint_\Gamma (z-a)^k G_j'/G_j\,dz\).
The physical moments for \(k=1,2\) vanish at the double. The
single-valued collar log \(H_j=\log(G_j/F_T)\) obeys
\[
 H_j=-\Delta_j(T,z)/F_T(z)+O\bigl(p_j(T)^2 Z_*^{4j}\bigr)
 \quad(z\in\Gamma).
\]
The remainder follows from the power series with the fixed positive
floor. Integration by parts on the closed contour gives
\(m_{k,j}=-k(2\pi i)^{-1}\oint_\Gamma(z-a)^{k-1}H_j\,dz\).
Thus \(c_j(T)-a=m_{1,j}/2=O(p_j(T) Z_*^{2j})\), and
\[
 \begin{aligned}
 D_j(T)
 &=\tfrac12m_{2,j}-\tfrac14m_{1,j}^2\\
 &=\frac{1}{2\pi i}\oint_\Gamma
                   (z-a)\,\frac{\Delta_j(T,z)}{F_T(z)}\,dz
       +O\bigl(p_j(T)^2 Z_*^{4j}\bigr)\\
 &=\frac{\Delta_j(T,a)}{A_T(a)}
       +O\bigl(p_j(T)^2 Z_*^{4j}\bigr).
 \end{aligned}                                                     \tag{4}
\]
The only pole of the linear term is simple at \(a\).
Dividing the error term by \(p_j(T)|a|^{2j}\) costs
\(O(p_j(T)(Z_*^2/|a|)^{2j})=o(1)\), even if individual links
are small. Since \(E_{j,T}(a)\to1\), this proves
\[
 D_j(T)\sim \frac{L_j(T,a)}{A_T(a)}\quad(j=N,N+1).                  \tag{5}
\]

For the model time defect use E03 r1 (7):
\[
 r_N(T)=-\frac{1}{2\pi i}\oint_\Gamma
                    (z-c_N(T))\frac{R_N(T,z)}{G_N(T,z)}\,dz .
\]
On the contour replacing \(c_N(T)\) by \(a\) and \(G_N(T,z)\)
by \(F_T(z)\) costs \(O(p_N(T)Z_*^{2N}\sup_\Gamma|R_N(T,z)|)\),
by the fixed floors and the preceding center bound. The linear
integral is \(-R_N(T,a)/A_T(a)\) by the same simple-pole calculation.
After division by \(h_N^*(T)|a|^{2N-2}/(2N-2)!\), the relative
remainder is \(O(p_N(T) Z_*^{2N}(Z_*/|a|)^{2N-2})=o(1)\)
by (2). Consequently
\[
 \boxed{\quad r_N(T)\sim-\frac{R_N(T,a)}{A_T(a)},\qquad
  \frac{r_N(T)}{D_N(T)}\sim\frac{(2N)(2N-1)}{a^2},\qquad
  \frac{r_N(T)}{D_{N+1}(T)}\sim
     -\frac{\Pi_N}{\beta_{N+1}(T)a^4},\quad
  \Pi_N=(2N-1)(2N)(2N+1)(2N+2).\quad}                              \tag{6}
\]
The first two quantities \(r_N(T)\) and \(D_N(T)\) both have
eventual sign \((-1)^N\operatorname{sgn}A_T(a)\), whereas
\(D_{N+1}(T)\) has the opposite sign. The residual at this event
therefore has no degree-independent favorable sign. All ratios
in (6) use relative remainder estimates at their own degrees.
In particular the \(N+1\) comparison uses no lower bound for
\(\beta_{N+1}(T)>0\).

The required actual coefficients for the residual evaluator and
\(G_{N+1,\lambda}\) are the same first \(N\) links. The exact
next-head asymptotic includes the first omitted factor
\(\beta_{N+1}(T)\); evaluating \(G_{N+1,\lambda}\) needs no such
extra link. An upper bound on the omitted factor comes from
\(B_N-\beta_N\), or \(B_N\) alone. No actual coefficient values
are acquired here. [E03 r1 §5][r1] [E01 §5][e01]

## 3. Unique nearby model double time

The physical equation \(D'=2+4KD\) and the exact model equation
\[
 D_N'=2+4K_ND_N+r_N
\]
hold on \(I\) through both types of double root. The contour formula
and (2) give \(r_N\to0\) uniformly there, using the fixed buffer
and model floor. Together with (3) and \(K_N\to K\), this yields
\(D_N'\to D'\) uniformly, in addition to \(D_N\to D\).
There is no need to bound derivatives of individual roots or to
impose the physical heat law on the model.

At \(T\), \(D(T)=0\) and \(D'(T)=2\). Shrink \(I\) once more,
independently of \(N\), so \(D'\ge1\) and the physical discriminant
has opposite signs at its two endpoints. Uniform \(C^1\) convergence
makes \(D_N\) strictly increasing with opposite endpoint signs for
all sufficiently large \(N\). It has exactly one zero in \(I\), at
a time \(\lambda_N\) with \(\lambda_N\to T\). A zero of \(D_N\)
is a double model zero by the fixed two-zero count. By the mean
value theorem,
\[
 \lambda_N-T=-\frac{D_N(T)}{D_N'(\xi_N)}
 \sim-\frac{L_N(T,a)}{2A_T(a)},                                     \tag{7}
\]
where \(\xi_N\) is between \(T\) and \(\lambda_N\), and
\(D_N'(\xi_N)\to2\). Both the model time displacement and
its direction are thus resolved for this fixed event.
[Parent fixed-event lemma][parent] [E03 r1 §3][r1]

## 4. Actual signed integral on a shrinking slab

Let \(\tau_N>0\) with \(\tau_N=o(N^{-2})\) and \(v_N=T+\tau_N\).
Let \(z_{\pm,N}(t)=c_N(t)\pm\sqrt{D_N(t)}\) denote the unordered
model pair at \(t\in[T,v_N]\). As \(D(T)=0\), \(c(T)=a\) and
both physical coordinates have bounded derivatives on \(I\),
(3) gives a fixed constant \(C_1\) with
\[
 \sup_{t\in[T,v_N],\,\pm}|z_{\pm,N}(t)-a|
 \le C_1\bigl(\sqrt{\tau_N}+\sqrt{\bar p_N Z_*^{2N}}\bigr)=o(1/N).
 \tag{8}
\]
This uses \(|\sqrt{D_N}|=\sqrt{|D_N|}\) regardless of root type.

Write \(Q_N=(z-c_N)^2-D_N,\ A_N(t,z)=G_N(t,z)/Q_N(t,z)\),
and \(A(t,z)=F_t(z)/((z-c(t))^2-D(t))\) for the two nonvanishing
units. Both denominators are bounded away from zero on \(\Gamma\)
and converge to each other uniformly there, by (3). The quotient
comparison on \(\Gamma\) and the maximum modulus principle yield
\(A_N-A\to0\) uniformly on the closed disk, jointly on \(I\).
The same boundary continuity and maximum modulus comparison give
continuity in \(t\) of \(A(t,z)\) uniformly on the disk. Thus
\(A_N(t,z_{\pm,N}(t))\to A_T(a)\) uniformly on the shrinking slab.

The exact contour for \(r_N\) admits a root-average formula:
\[
 r_N(t)=-\frac{g_N(t,z_{+,N}(t))+g_N(t,z_{-,N}(t))}{2},
 \qquad g_N=R_N/A_N.                                               \tag{9}
\]
Indeed \((z-c_N)/Q_N\) is the half-sum of the two simple Cauchy
kernels. At coincident roots both kernels agree and (9) is minus
the single value of \(g_N\). There is no reciprocal root separation.

The normalized norm obeys
\[
 (\log h_N^*)'=\beta_N+\beta_{N+1}-\beta_1
\]
by the monic norm flow and \(h_N^*=h_N/Z_\lambda\).
The bound \(B_N+B_0=O(\log^2(N+1))\) controls the absolute derivative
uniformly on \(I\), so \(h_N^*(t)/h_N^*(T)\to1\) on the shrinking
slab. By (8), \((z_{\pm,N}(t)/a)^{2N-2}\to1\) uniformly, using
\(|(1+w)^j-1|\le e^{j|w|}-1\). The phase \(\Psi_{N,t}\to1\)
uniformly on the fixed disk. Equation (1) now yields
\(R_N(t,z_{\pm,N}(t))/R_N(T,a)\to1\) uniformly, while the unit
factors tend uniformly to the same nonzero value \(A_T(a)\).
Together (6) and (9) show \(r_N(t)/r_N(T)\to1\) uniformly, including
when the slab contains the model double time.
[Parent manuscript §3][ms] [E03 r1 §§2–3][r1]

With \(W_N(t)=\exp(4\int_t^{v_N} K_N(s)\,ds)\), bounded \(K_N\)
gives \(W_N\to1\) uniformly on the slab. Define the signed integral
\(\mathfrak R_N(T)=\int_T^{v_N}W_N(t)r_N(t)\,dt\) as in E03 r1.
The uniform ratios give the comparison
\[
 \mathfrak R_N(T)\sim\tau_N r_N(T),\qquad
 \frac{|\mathfrak R_N(T)|}{|D_{N+1}(T)|}
       \sim\frac{\tau_N\Pi_N}{\beta_{N+1}(T)a^4}.                  \tag{10}
\]
The signed ratio to the absolute denominator has sign
\((-1)^N\operatorname{sgn}A_T(a)\) for large \(N\).
For \(\tau_N=N^{-3}\), the absolute ratio is
asymptotic to \(16N/(\beta_{N+1}(T)a^4)\); it is at least of order
\(N/\log^2(N+1)\) by the envelope. Other shrinking slab rates
retain the explicit \(\tau_N\Pi_N/\beta_{N+1}(T)\) dependence.

For comparison take fixed valid contour floors and a bounded \(M\)
in the absolute safety allowance \(A_R\) of E03 r1 (16)–(17), on
\([T,v_N]\) and the same \(\Gamma\). For a fixed such model floor
\(m>0\), write \(C_\Gamma=\rho(2\rho-b)\). The norm flow gives
\(\sup_{[T,v_N]}h_N^*/h_N^*(T)\to1\), the phase allowance at \(Z_*\)
tends to zero, and \(Q_{\tau_N}(M)/\tau_N\to1\) for the factor
\(Q_\Delta\) in r1 (17). Comparing (1), (6), and (10) with that
allowance gives
\[
 \frac{A_R}{|\mathfrak R_N(T)|}
   \sim \frac{C_\Gamma |A_T(a)|}{m}\left(\frac{Z_*}{|a|}\right)^{2N-2}.
 \tag{11}
\]
Since \(Z_*>|a|\), the fixed-circle safety allowance is far larger
than the actual signed term. Equations (10)–(11) concern that term
and its allowance in isolation. The exact E03 r1 identity for the
total error \(e=D-D_N\) contains
\[
 W_N(T)e(T)=e(v_N)+\mathfrak R_N(T)
        -4\int_T^{v_N}W_N(t)(K-K_N)(t)D(t)\,dt.
 \tag{12}
\]
The residual can cancel in combination with the incoming error
and transfer terms. A lower estimate for its absolute magnitude
supplies no corresponding lower estimate for the full signed correction
or a complete margin. [E03 r1 (9)–(10), (16)–(19)][r1]

## 5. Controls and scope

The proof also applies to an even positive-source probability
family given by a literal Fourier transform under the same quadratic
heat tilt, with infinite support, positive monic norms and the
exponential moments and local time domination needed for the tilt
and its differentiation. It requires the uniform E01 cosh and
adjacent envelopes and the E03 r1 exact residual and phase law
on its fixed event interval. No uniformity across different sources,
events or heights is asserted. [Control catalog][catalog]
[E01 §6][e01] [E03 r1 §6][r1]

| Control | Tested premise |
| --- | --- |
| Exact quadratic heat collision | It exhausts the exact incoming gap at the event and gives the same local heat orientation. It has no infinite positive Jacobi source, so it does not test (6) or (10). |
| Three- and four-square isolated double controls | These positive even extensions satisfy the E01 laws and quantitative envelopes uniformly through their catalog events, including the score integration with the vanishing junction factor. Their heat tilt and Jacobi deformation give the algebraic residual of r1, so the fixed-event comparison applies to each own counted local event. The complete equal square coefficients and full reflection fail and are unused here. Their local events do not give a finite all-real threshold. |
| Finite-prime orbit and finite score/head controls | The specified weighted sources can keep the required phase premises while failing complete canonical identities. The orbit events vary the source and escape in height, and finite canonical-score matching by itself provides no fixed event. |
| Euler, reflected, and smooth shape/primitive controls | The tested Euler member fails \(B_0\) at time zero. The reflected super-Gaussian fails the inherited score confinement. The smooth shape and primitive families lack the canonical summand score, with their weaker quantitative premises untested. |
| Atomic, compact, and normalized endpoint controls | Finite atomic chains terminate, and triangular compact extensions fail the global positive-density premise of the inherited score proof. RH-conditional endpoint doubles occur at time zero and retain their RH assumption, outside the interior-event hypothesis; endpoint reality alone permits a double. |
| Changed observation and relaxed profile data | These lack, respectively, the prescribed physical Fourier observation and a prescribed physical field with a counted pair. |

A fixed canonical collision was stipulated throughout. No data were
acquired for one, and no numerical certificates were rerun. The
comparison delimits the actual residual payment and its absolute
safety allowance on the given local geometry. It leaves source-specific
joint compensation, other signed contour estimators and independent
canonical information open. There is no local strict margin from this
test to compose across slabs.

[request]: ../research-progress/handoffs/VCD-GT-E03-r2.md
[decision]: ../brainstorm/notes/02_VCD_GT_B02_FIXED_EVENT_DECISION_20261116.md
[e01]: 03_VCD_GT_E01_PHYSICAL_TIME_SIGNED_ERROR_20261116.md
[e02]: 04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md
[r1]: 05_VCD_GT_E03_PHYSICAL_MODEL_DEFECT_20261116.md
[assess1]: ../reviews/02_VCD_GT_E01_TIME_EXTENSION_ASSESSMENT_20261116.md
[assess2]: ../reviews/03_VCD_GT_E02_COORDINATE_TRANSFER_ASSESSMENT_20261116.md
[parent]: ../../notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md
[ms]: ../../manuscript/main.tex
[results]: ../../../../../result-summaries/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[cluster]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
