# Outer-height contour bounds and a truncated-source potential obstruction

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this conversation's session metadata.

**Status: estimates and scoped obstruction proved in-note; same-assistant
review only.** This starts HDA-19. On compact time slabs ending at 64,
we obtain an explicit exponentially accurate outer approximation to the
regularized observables, including actual covariance. At each fixed
`t>64`, the positive-cutoff, piecewise-linear source field of Note 20
cannot approximate the source-anchored averaged potential uniformly in
height on the off-axis buffers stated below. This is a failure of that
representation for the full observable contract, not a density-only
impossibility theorem or a solution of the adaptive outer-density problem.

Read the [result index][results], especially [heat geometry][geometry] and
[collision controls][controls], and the [avoid index][avoid], especially
[target classification][a01], [scoped exclusions][a07] and
[numerics before a question][a10]. The gains are quantitative tail bounds
and a proved representation failure. No RH or simplicity criterion is
introduced. No numerical implementation, computation or Sol packet was
needed for this round. [Review 09][review] is by the same assistant.

## 1. Contract and normalization

Keep the complete canonical source and
\[
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
 \quad H_t=-H_{zz},\quad z=x+iy,
\]
\[
 \rho={q|H_z|^2\over\pi(|H|^2+q)^2},\quad
 j={qH_{zz}\overline{H_z}\over\pi(|H|^2+q)^2},\quad
 S=\log(|H|^2+q),\quad w={q\over |H|^2+q},\quad r=\log q.
\tag{OH1}
\]
The regulator is exactly Note 20 FB1--FB2, with fixed `eta>0`.
Use a fixed positive normalized product kernel `K=k_ell k_h` from Note 19,
with horizontal halfwidth `ell>0` and transverse halfwidth `h>0`.
There is no time averaging or varying filter width. Observe `|y|<=Y0`
and supply the entire buffer `|y|<=Y=Y0+h`, all real `x`.
Write `R=K*rho`, `J=K*j`, `U=K*S` and
\[
 Q=K*(S_x^2-S_y^2)-((K*S_x)^2-(K*S_y)^2).
\]
All errors below are absolute errors in the physical, unnormalized
observables; no sampled value or unknown zero is a denominator.

The first theorem fixes a compact interval `I=[t_a,t_b]`, with
`0<t_a<=t_b<=64`. Its proof also works for any finite `t_a<=t_b<=64`.
The obstruction instead fixes an individual `t>64`. Constants in either
result may depend on these time choices. No joint `t,x -> infinity`
uniformity follows from the compact-time estimates.

## 2. A complete-source contour estimate with paid ends

Fix `0<a<=pi/16`; this `a` is a source-contour displacement, not heat time.
Put
\[
 d=\cos(4a),\quad C_a=(1-16e^{-3\pi d})^{-1},\quad
 s=\max(t_b,0),\quad D=s+Y+10,\quad V=1+\log(D/d).
\]
Here `d>=1/sqrt(2)` and `16 exp(-3 pi d)<1`.
Define the explicit constants, for each fixed integer `j>=0`,
\[
\begin{split}
 A_j={}&e^{-t_a a^2}(2\pi^2+3\pi)C_a\left[
 e^{sV^2+(9+Y)V}{(V+a)^{j+1}-a^{j+1}\over j+1}
 +{1\over2}\sum_{k=0}^j {j\choose k}a^{j-k}
       \Gamma\left({k+1\over2}\right)\right].
\end{split}\tag{OH2}
\]
Then, on the entire height axis,
\[
 \boxed{|\partial_z^jH(t,x+iy)|\le A_j e^{-a|x|}
 \quad(t\in I,\ |y|\le Y).}
\tag{OH3}
\]
In OH2--OH3 the compact interval may have any finite upper endpoint;
the restriction `t_b<=64` is only needed for the observable transfer below.
The constants are conservative, but are finite expressions rather than
unknown suprema, fitted parameters or uncomputed oscillatory integrals.

**Proof.** The theta series converges normally on the source strip
`|Im u|<pi/8`. Its real reflection identity extends there by analytic
continuation. For `v>=0`, termwise absolute values give
\[
 |\Phi(v\mathbin{\pm}ia)|
 \le\sum_{n\ge1}(2\pi^2n^4e^{9v}+3\pi n^2e^{5v})
                   e^{-\pi d n^2e^{4v}}
 \le (2\pi^2+3\pi)C_a e^{9v-\pi d e^{4v}}.
\tag{OH4}
\]
The last inequality uses `n^2<=n^4`, `e^(5v)<=e^(9v)` and the successive
ratio bound `16 exp(-3 pi d)` for the leading positive series. Reflection
supplies the same bound with `v` replaced by `|v|` on the other half-line.
No theta mode is discarded.

Write the original cosine integral as one half of the full-line Fourier
integral. For `x>=0` move that whole contour to `R+ia`; for `x<0` move
it to `R-ia`. On the two vertical ends at `Re u=+/-M`, the integrands
are bounded by a polynomial times
`exp(s M^2+Y M+|x|a-pi d exp(4M))`, times a fixed constant. Thus both
ends tend to zero as `M->infinity`, for every `x`; no half-line endpoint
or artificial cutoff term is suppressed. The same argument applies to
the integrand multiplied by `(iu)^j`.

After shifting, the factor from height is `exp(-a|x|)`. The other factors
are bounded by `exp(-t_a a^2) (v+a)^j exp(sv^2+Yv)` on `v>=0`.
The half from the full-line formula cancels the two equal half-line
majorants. This gives the bound by the corresponding positive integral
using OH4. On `[0,V]` discard its negative exponential and integrate
`(v+a)^j`. For `v>=V`,
\[
 (s+1)v^2+(9+Y)v\le Dv^2\le {\pi d\over2}e^{4v},
\]
since `exp(4v)/v^2` increases there, `V<=D/d`, and the inequality holds
already at `V=1+log(D/d)`. The remaining exponential is at most
`exp(-v^2)`. Expand `(v+a)^j` and extend its tail integral down to zero.
This is OH2. Uniform bounds, not a differentiated asymptotic remainder,
also justify the source differentiation and `H_t=-H_zz` used below.

## 3. Exponentially accurate outer background before the spatial switch

For `I` ending at 64, `q=epsilon_b(t)^2` is independent of position. Set
\[
 e_* =\min_{t\in I}\epsilon_b(t)>0,\quad
 b=\sup_{t\in I}|r_t|,\quad
 E(x)=e^{-a\max(|x|-\ell,0)},
\]
\[
 L_x=\|K_x\|_1,\quad L_y=\|K_y\|_1,\quad L_2=\|\Delta K\|_1,
 \qquad G={2A_0A_1\over e_*^2}.
\]
These are explicit: `r_t=-t/(1+t^2)` and
`e_*=eta Phi(0) sqrt(pi)/[2(1+max(t_a^2,t_b^2))^(1/4)]`.
The canonical value `Phi(0)>0` is the convergent source series from Note 11.
The kernel norms are norms of its specified compact polynomials.

The approximation is the exact regulated background
\[
 (R_0,J_0,U_0,W_0,Q_0)=(0,0,r(t),1,0),\qquad W=K*w.
\tag{OH5}
\]
It is supplied by the zero field in the algebraic regulated equations;
no zero-counting measure is assigned to that identically zero field.
The following bounds hold uniformly for `t in I`, all real `x`,
`|y|<=Y0`:
\[
\begin{array}{ll}
 |R|\le {A_1^2\over\pi e_*^2}E^2,&
 |J|\le {A_1A_2\over\pi e_*^2}E^2,\\[2pt]
 |U-r|\le {A_0^2\over e_*^2}E^2,&
 |W-1|\le {A_0^2\over e_*^2}E^2,\\[2pt]
 |U_i|\le G E^2\ (i=x,y),&
 |U_t-r_t|\le {2A_0A_2+bA_0^2\over e_*^2}E^2.
\end{array}\tag{OH6}
\]
Writing `B=r_t w` and `s_r=r_t(1-2w)rho` for the actual forcing and
current source, we also have
\[
 |K*B-r_t|\le {bA_0^2\over e_*^2}E^2,
 \qquad |K*s_r|\le {bA_1^2\over\pi e_*^2}E^2,
\tag{OH7}
\]
\[
 |R_t|\le {2A_1A_3+bA_1^2\over\pi e_*^2}E^2
          +{4A_1^2A_0A_2\over\pi e_*^4}E^4.
\tag{OH8}
\]
The actual covariance, including its cancellation between squared means
and means of squares, satisfies
\[
 \boxed{|Q|\le4G^2E^4,\qquad
 |\Delta Q|\le[6L_2+4(L_x^2+L_y^2)]G^2E^4.}
\tag{OH9}
\]
All convolution points lie in the complete buffer, where OH3 has
`exp(-a|Re z|)<=E(x)`. Thus the exponential remains valid after averaging.

**Proof of the transfer.** Use `|H|^2+q>=q`,
`log(1+|H|^2/q)<=|H|^2/q` and
`|S_i|<=2|H||H_z|/q` to obtain the static inequalities.
The exact identities
\[
 S_t=-2\Re{H_{zz}\overline H\over |H|^2+q}+r_t w,
\]
\[
 \rho_t=-{2q\Re(H_{zzz}\overline{H_z})\over\pi(|H|^2+q)^2}
 +r_t(1-2w)\rho
 +4\rho\Re{H_{zz}\overline H\over|H|^2+q}
\tag{OH10}
\]
prove OH7--OH8 directly, without differentiating OH6. For OH9 compare the
two squares and two squared means using `|S_i|<=G E^2`. Move derivatives
of the first squares onto `K`; use
`Delta(v_i^2)=2v_i Delta v_i+2|grad v_i|^2` for `v_i=K*S_i`.
This gives respectively `2L_2` and `4(L_2+L_x^2+L_y^2)`, times `G^2 E^4`.
No covariance was chosen to make an equation hold.

Spatial derivatives of the linear averaged quantities are bounded by
convolving their respective pointwise allowances against
`|partial^alpha K|`. This covers the kernel's integrable weak derivatives
through order four, and hence the potential/density derivatives in the
fixed-filter equations. Initial/final time traces and spatial normal
traces inherit the same uniform bounds. Spatial regulator curvature is
identically zero here; the time forcing and current source are retained.
The background OH5 satisfies the exact adaptive equations on this slab.

For any prescribed absolute tolerance, these explicit bounds supply a
finite tail threshold and hold beyond it to infinity. For example,
`R<=delta` follows for
\[
 |x|\ge\ell+{1\over2a}\max\left(0,
      \log{A_1^2\over\pi e_*^2\delta}\right).
\tag{OH11}
\]
This is a uniform compact-time height result, not just Riemann--Lebesgue
convergence. It says that the regularized observable becomes small when
the fixed-in-height regulator dominates the field. It does not say that
high zeros disappear or that this approximation represents their count.

## 4. Why this payment fails after 64

At a fixed `t>64`, FB2 is exactly
\[
 \epsilon_g(t,x)=E_0(t)e^{-\beta(t)x^2/2},\quad
 E_0=\epsilon_b^{1-\chi}(M_0/\kappa)^\chi>0,
 \quad\beta=\chi/\kappa>0.
\tag{OH12}
\]
The `M_0` here is the real source-saddle normalization in Note 19.
The smallest regulator in the horizontal buffer is
`E_0 exp(-beta(|x|+ell)^2/2)`. Inserting it into the density payment gives
a factor `exp(beta(|x|+ell)^2-2a(|x|-ell))`, which diverges as height
increases. This establishes failure of this particular absolute-upper-
bound/floor argument. It does not establish divergence of the true density.
A field lower margin or a multiplicity-aware weak transfer is needed.

There is also an actual failure of the existing truncated-source
representation for the required potential, not just a failure of a bound.

## 5. A fixed positive cutoff creates an incompatible outer potential

Fix `t>64`. Let `f` be any continuous piecewise-linear function on `[0,U_s]`
with finitely many cells and `f(U_s)>0`, extended by zero beyond `U_s`.
This includes every exact positive theta-node interpolant in Note 20,
however many cells or retained theta modes it has. Set
\[
 g(u)=e^{tu^2}f(u),\qquad H_f(t,z)=\int_0^{U_s}g(u)\cos(zu)\,du.
\]
The field still satisfies the heat equation exactly when this source is
kept fixed. For a fixed transverse bound `Y`, put
\[
 B_f=|g'(0+)|+|g'(U_s-)|e^{YU_s}
  +\sum_{0<u_i<U_s}|[g']_{u_i}|e^{Yu_i}
  +\sum_i\int_{u_i}^{u_{i+1}}|g''(u)|e^{Yu}\,du.
\tag{OH13}
\]
All terms are finite and determined by the finite source. Two integrations
by parts, with the second performed cell by cell, give
\[
 H_f(t,z)={g(U_s)\sin(U_s z)\over z}+\mathcal E_f(z),
 \qquad |\mathcal E_f(z)|\le B_f/|z|^2\quad(|\Im z|\le Y).
\tag{OH14}
\]
The endpoint at zero in the first integration vanishes because `sin(0)=0`.
The second integration includes the jumps of `g'` and both end derivatives
in OH13. This is precisely the endpoint term absent from the complete
reflected theta contour argument.

Choose an off-axis observation center `y_*>h` and put
`d_y=y_*-h>0`, `Y=y_*+h`; assume the observation strip includes `y_*`.
Let
\[
 c_f=g(U_s)\sinh(U_s d_y)>0.
\]
Since `|sin(U_s z)|>=sinh(U_s d_y)` whenever
`d_y<=Im z<=Y`, OH14 implies
\[
 |H_f(t,z)|\ge{c_f\over2|z|}\quad
 (|z|\ge 2B_f/c_f,\ d_y\le\Im z\le Y).
\tag{OH15}
\]
Let `A_0` be OH2 for the singleton time interval `[t,t]` and this `Y`.
For real `xi>=2a/beta`, OH3 and OH12 give
\[
 |H(t,\xi+i v)|^2+q(t,\xi)
 \le(A_0^2+E_0^2)e^{-2a\xi}\quad(|v|\le Y).
\tag{OH16}
\]
Thus, whenever `x-ell>=max(1,2a/beta,2B_f/c_f)`, positivity of `K` yields
\[
\boxed{
 U_f(t,x,y_*)-U(t,x,y_*)\ge
 2a(x-\ell)-\log((x+\ell)^2+Y^2)
 +2\log(c_f/2)-\log(A_0^2+E_0^2).
}\tag{OH17}
\]
In particular the difference tends to positive infinity, with lower bound
`2a x-2 log x-O(1)`. This holds at every sufficiently large height, not
merely along a selected sequence. Negative heights follow by evenness.
The proof does not need a lower bound for theta, its zero positions, or
an assertion about high zeros. A positive fixed cutoff can be arbitrarily
small; it changes the threshold, not the eventual conclusion.

**Exact scope.** OH17 excludes a uniform absolute comparison of the
source-anchored averaged potential for this finite, positive-endpoint
source class, at every fixed `t>64`, on the stated off-axis buffered strip.
It therefore excludes this class from a full contract that requires that
potential along with density. It does **not** prove failure of density
alone, a claim at `y=0`, failure of smooth tapers with a vanishing endpoint,
or impossibility for height-dependent cutoffs, noncompact sources,
normalized relative approximations or weak comparisons. An arbitrary
spatial harmonic correction is not part of this source-anchored potential.
A fixed additive constant cannot remove the growing difference.

## 6. Coverage, controls, and the next analytical estimate

The controlled tail in Section 3 covers compact slabs up to 64. It has
no asserted overlap with Note 19's eventual large-positive-time clock,
whose regulator equals `epsilon_+` only from 128 onward and whose theorem
has further eventual gates. At `t>64` the unbounded adaptive exterior
remains open. At large positive time, the region beyond the clock's full
buffer `|x|=O(kappa^(1/3))` is still an uncovered spatial domain. The
constant in OH2 grows with the time ceiling, so it cannot silently be
used as a joint-limit error. No field or density splice has been made;
any future splice must pay its interfaces and time derivatives.

The next HDA-19 step is a noncompact, oscillation-preserving outer field
representation on a declared compact slab `[t_a,t_b]` with `t_a>64`.
A natural candidate is the conjugate gamma-factor pair from the heat
Riemann--Siegel analysis, with holomorphic relative error on root-scale
complex neighborhoods. Its first useful consumer would be the local
field floors and collars in Note 14 VE17--VE18, which pay the adaptive
weak bias without a global regulator floor. This candidate is a next
estimate to prove, not an established input here.

For source verification, Polymath's [version-pinned paper][polymath],
normalization (1)--(4), domain (5), Theorem 1.5 and the displayed local
formula in Lemma 9.2 were inspected. The stated high-zero theorem is for
`0<t<=1/2`; it cannot simply be assigned to this `t>64` task. The text
notes that larger bounded parameter ranges require changed estimates.
Those estimates, lower margins and differentiated errors remain work.
The existing reference record is updated; no new external theorem is
needed for OH2--OH17 and no numerical packet is justified yet.

The [control screen][controls] applies as follows:

| Control | What is shared or which premise is absent |
| --- | --- |
| Smooth colliding sources with suitable strip decay | Can obey analogous contour bounds with their own constants; decay is not a collision discriminator. |
| Euler-factor controls | May retain analytic strip decay, but the unchanged theta coefficient envelope OH4 is not automatically theirs. |
| Weighted-square / finite-prime controls | Do not inherit complete canonical reflection and coefficients; the negative half-line step must be re-established for their actual source. |
| Reflected, smooth-shape and positive-primitive controls | Reflection alone does not give the canonical complex-strip majorant; any valid generic bound still allows collisions. |
| Positive atoms and heat polynomials | Lack the smooth decaying full-line source used by OH2--OH4. Their regulated identities still hold. |
| Finite-source fields of Note 20 | They have their own exact heat equation, but the cutoff boundary term OH14 is nonzero. OH17 tests this actual proposed class. |

HDA-19 is **partial** with these two stated gains. HDA-17 has no newly
accepted mesh and HDA-18 remains gated. The negative endpoint is advanced
separately in [Note 26][negative]. The retained manuscript still ends at
Note 23's integration; these new proofs are research notes pending a
subsequent manuscript revision and independent review.

[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[polymath]: https://arxiv.org/html/1904.12438v2
[review]: ../reviews/09_OUTER_TAIL_AND_NEGATIVE_ENDPOINT_SELF_REVIEW_20261024.md
[negative]: 26_NEGATIVE_ENDPOINT_EVOLUTION_AND_COVARIANCE_20261024.md
