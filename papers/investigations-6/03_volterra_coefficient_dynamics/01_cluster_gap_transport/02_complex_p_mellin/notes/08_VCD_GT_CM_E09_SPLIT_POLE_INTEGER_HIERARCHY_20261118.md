# VCD-GT-CM-E09 r1 — Split-pole integer hierarchy

18 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. Requested helper dispatch **gpt-6.1-sol / ultra**.
Independent serving-model and actual reasoning-effort metadata unavailable.

**Proved in-note on the frozen paid \(D\ne0\) charts, pending E11 internal
assessment.** All six pins in the [frozen request][request] matched.
The recurrence closes with finitely many terms per equation in an
infinite hierarchy. It is a representation under [Classification01][class].
[B04 contract][b04] · [Result index][results] · [Cluster18][cluster] ·
[Controls12][controls] · [Avoid index][avoid] · [Premises02][premises] ·
[Scope07][scope]

## 1. Domain and recurrence

Use the unchanged complete theta field with \(\partial_tH=-H_{zz}\)
and the independently paid count-two tube in the [parent law][parent]
and [CM time law][cm02]. Freeze \(T\ge64\), \(L=\log T\), \(\ell=L^{-1}\),
\(\max(2,4\sqrt d)\le a\le L\), \(r_0=a\ell\), \(c\in[T,2T]\), and
\(|D|\le d\ell^2\le r_0^2/16\). The targets are within \(r_0/4\) of
\(c\). Every exterior occurrence has \(|w_j|=|\rho_j-c|\ge r_0\), and
all multiplicities are counted. On a local chart with \(D\ne0\) choose
an analytic \(s\) with \(s^2=D\). Set \(z_\pm=c\pm s\), \(d_0=2s\),
\(x_j=w_j-s\), \(y_j=w_j+s=x_j+d_0\), \(Q_j=x_jy_j=w_j^2-D\), and
\[
 P_{p,q}=\sum_j x_j^{-p}y_j^{-q}
 \qquad(p,q\in\mathbb Z_{\ge0},\ p+q\ge2).
\]
Use \(M=P_{1,1}\). Every derivative below is in physical time.

For \(m,n\ge1\) define the finite convolution
\[
 C_{m,n}=
 \sum_{i=2}^{m}P_{i,0}P_{m+1-i,n}
 +\sum_{j=1}^{n-1}P_{m,j}P_{0,n+1-j}.
 \tag{1}
\]
On the axes define
\[
 C_{m,0}=\sum_{i=2}^{m-1}P_{i,0}P_{m+1-i,0}\quad(m\ge2),
 \qquad
 C_{0,n}=\sum_{j=2}^{n-1}P_{0,j}P_{0,n+1-j}\quad(n\ge2).
 \tag{2}
\]
Empty sums are zero. All factors lie in the prescribed family. Set
\(A_d=2/d_0-d_0M\). For \(p,q\ge1\),
\[
 \begin{aligned}
 P_{p,q}'={}&p\big[C_{p+1,q}-(p+3)P_{p+2,q}-(q+2)P_{p+1,q+1}
                                 +A_dP_{p+1,q}\big]\\
 &+q\big[C_{p,q+1}-(p+2)P_{p+1,q+1}-(q+3)P_{p,q+2}
                                 -A_dP_{p,q+1}\big].
 \end{aligned}                                                    \tag{3}
\]
The pure-axis equations are
\[
 \begin{aligned}
 P_{p,0}'&=p\big[C_{p+1,0}-(p+3)P_{p+2,0}-2P_{p+1,1}
                                   +(2/d_0)P_{p+1,0}\big],
                         &&p\ge2,\\
 P_{0,q}'&=q\big[C_{0,q+1}-2P_{1,q+1}-(q+3)P_{0,q+2}
                                   -(2/d_0)P_{0,q+1}\big],
                         &&q\ge2.
 \end{aligned}                                                    \tag{4}
\]
The gap coordinate evolves by
\[
 d_0'=4/d_0-2d_0M,\qquad s'=A_d .
 \tag{5}
\]
Equations (1)–(5) use no separate first-power sum, and center velocity
cancels from the relative evolution. The right sides can reach total
degree \(p+q+2\). Closure means a componentwise identity for the
relative moments and separation of the given heat field. The inherited
pair contour still determines the absolute center. Existence and
uniqueness for arbitrary sequences in the infinite system are outside
this assertion.

## 2. Finite heat algebra and first-power cancellation

Start with finite polynomial heat flow at a simple-root slice.
The physical velocity is \(\rho'=2\sum_{\eta\ne\rho}(\rho-\eta)^{-1}\).
Use the first-power symbols only in this finite calculation.
The targets give
\[
 z_+'=2/d_0-2P_{1,0},\qquad
 z_-'=-2/d_0-2P_{0,1},\qquad
 P_{1,0}-P_{0,1}=d_0P_{1,1}.                              \tag{6}
\]
The difference in (6) holds occurrence by occurrence and directly
gives (5). The exterior relative velocities are
\[
 \begin{aligned}
 x_j'&=2(x_j^{-1}+y_j^{-1})
    +2\sum_{k\ne j}(w_j-w_k)^{-1}-2/d_0+2P_{1,0},\\
 y_j'&=2(x_j^{-1}+y_j^{-1})
    +2\sum_{k\ne j}(w_j-w_k)^{-1}+2/d_0+2P_{0,1},
 \end{aligned}
\]
where \(k\) ranges over exterior occurrences. Differentiating
\(f_{p,q}(w)=(w-s)^{-p}(w+s)^{-q}\) using \(x_j',y_j'\) gives the
finite equation
\[
 \begin{aligned}
 P_{p,q}'={}&p\big[(2/d_0-2P_{1,0})P_{p+1,q}
                -2P_{p+2,q}-2P_{p+1,q+1}+U_{p+1,q}\big]\\
 &+q\big[(-2/d_0-2P_{0,1})P_{p,q+1}
                -2P_{p+1,q+1}-2P_{p,q+2}+U_{p,q+1}\big],\\
 U_{m,n}={}&-2\sum_{j<k}
     \frac{f_{m,n}(w_j)-f_{m,n}(w_k)}{w_j-w_k}.
 \end{aligned}                                                    \tag{7}
\]
Omit the corresponding bracket when its prefactor \(p\) or \(q\)
vanishes.

The elementary negative divided difference, obtained by taking the
difference in the \(w-s\) factor and then in the \(w+s\) factor, is
\[
 -\frac{f_{m,n}(u)-f_{m,n}(v)}{u-v}
 =\sum_{i=1}^{m} f_{i,0}(u) f_{m+1-i,n}(v)
  +\sum_{j=1}^{n} f_{m,j}(u) f_{0,n+1-j}(v).
 \tag{8}
\]
For example, the first sum uses
\(-[(u-s)^{-m}-(v-s)^{-m}]/(u-v)
=\sum_{i=1}^m (u-s)^{-i}(v-s)^{-m-1+i}\), multiplied by
\((v+s)^{-n}\). The second sum uses the corresponding identity at
\(-s\), multiplied by \((u-s)^{-m}\). The full kernel is symmetric
in \(u,v\), also at the diagonal by continuity. Thus the factor of
two in \(U_{m,n}\) converts the unordered pair sum into an ordered
off-diagonal sum. In the first convolution, subtracting the diagonal
removes \(mP_{m+1,n}\). The second removes \(nP_{m,n+1}\).

For \(m,n\ge1\) the endpoint \(i=1\) and the endpoint \(j=n\)
leave \((P_{1,0}+P_{0,1})P_{m,n}\); the remaining products are
(1). In the two blocks of (7) these endpoints combine with the
center contributions to give respectively
\(-d_0M P_{p+1,q}\) and \(+d_0M P_{p,q+1}\) by (6). On the pure
\(m\)-axis the endpoints \(i=1,m\) give \(2P_{1,0}P_{m,0}\).
They cancel the first-power term of the \(p\)-block in (7).
The pure \(n\)-axis gives \(2P_{0,1}P_{0,n}\) and cancels in the
\(q\)-block. The remaining products are (2). This proves (3)–(4)
before any infinite limit.

In the complete divisor, (6)'s difference remains absolute as the
series \(\sum_j d_0/Q_j\), with \(O(|\rho_j|^{-2})\) summands in the
tail. It also equals the limit of the difference with a common cutoff.
No absolute convergence of the separate first-power sums is assumed.

## 3. Complete canonical passage and target residues

Fix a reference time on a \(D\ne0\) chart and a stationary physical
circle \(\Gamma\) about its center, of radius \(r_0/2\).
Make it positive and shrink the chart so it encloses the same two
targets, stays zero-free, and leaves every exterior occurrence
outside. The argument-principle moments give analytic \(c,D\) on a
complex-time neighborhood of the reference slice. The two targets
are analytic there after the local choice of \(s\). Denote their
quadratic by \(Q(t,z)\) and put
\(k(t,z)=(z-z_+)^{-p}(z-z_-)^{-q}\). Then
\[
 P_{p,q}(t)=-\frac{1}{2\pi i}\oint_\Gamma
       k(t,z)\left(\frac{H_z}{H}(t,z)-\frac{Q_z}{Q}(t,z)\right)\,dz .
 \tag{9}
\]
In the finite product this follows by summing the integrals of
\(k(z)/(z-\rho_j)\) for the exterior occurrences, each equal to
\(-k(\rho_j)\) by the vanishing residue at infinity. In the canonical
product use the inherited genus-one log derivative, whose series is
normal on the circle. Its constant and \(1/\rho_j\) regularizers
integrate to zero against \(k\), since \(k\) decays as \(z^{-p-q}\)
and all its poles lie inside \(\Gamma\). The strip, unit count and
collar make \(\sum_j |k(\rho_j)|\) finite. This gives (9) with
the full exterior divisor. [Parent §§1–2][parent] ·
[GR Note02 §§1,3][gr02] · [GR assessment][gr05]

The term \(kQ_z/Q\) in (9) accounts for the target poles. Its
integral around **both** targets vanishes, since it is rational with
all poles inside \(\Gamma\) and decays as \(z^{-p-q-1}\).
Individual residues can be nonzero. For \(p=2,q=0\), they are
\(-d_0^{-2}\) at \(z_+\) and \(+d_0^{-2}\) at \(z_-\).
Any split of the target contour must include these terms or their
exact cancellation. For \(p=q\) the integrand \(kQ_z/Q\) is a
spatial derivative and the two residues vanish individually.

On the fixed circle, differentiate (9) with the full moving weight
\(k_t=k[p z_+'/(z-z_+)+q z_-'/ (z-z_-)]\) and with
\[
 \partial_t(H_z/H)=-H_{zzz}/H+H_zH_{zz}/H^2,\qquad
 Q_t=-2(z-c)c'-D'.
\]
The target correction can be differentiated as a single zero contour
integral. Analyticity of the contour observable extends through
exterior multiplicities on the local \(D\ne0\) chart. In the finite
multiple-root case, perturb the root factors at the reference time
to be simple, keeping each target inside \(\Gamma\) and the others
outside. Evolve each perturbed polynomial from its own reference
slice. The contour expression and its derivative converge by the
time-slice spatial jets and strict clearance. Every term in the
already canceled right sides (3)–(5) also converges. Thus the finite
equations hold at exterior multiplicities.

For the canonical passage, truncate the opposite-paired Hadamard
product by modulus at each reference time, keeping all ties, conjugate
and opposite groups and multiplicities, with prefactor \(H(t,0)\)
at that reference time. Each truncated polynomial has its own
physical heat evolution initialized at the reference slice. The
canonical strip and unit count give the inherited uniform inverse-square
product tail \(O(\log N/N)\) for \(|\rho|>N\) and compact spatial
convergence through order three by Cauchy. The time jet of \(H_z/H\)
on \(\Gamma\) therefore converges by the displayed heat formula.
The time jets \(c',D'\) from the argument-principle moments converge
on the same circle. For large \(N\), the two target factors agree
exactly at the reference slice. Since \(s\ne0\) on the chart, the
branch can be chosen with the same value there and \(s'=D'/(2s)\)
passes to the limit. These give convergence of the derivative in (9).

For every fixed index pair, the omitted occurrences have
\(|x_j|,|y_j|\gg|\rho_j|\) for \(N>4T+8\). The same shell count gives
\(\sum_{|\rho_j|>N}|x_j|^{-p}|y_j|^{-q}
=O_{p,q,C_{\rm u}}(N^{1-p-q}\log N)\) on the real paid tube, with
\(C_{\rm u}\) the inherited unit-count constant. Every moment in
(3)–(5) thus converges absolutely and each equation passes to
the limit at the reference time. On compact subcharts, fixed circles
from a finite cover supply positive minima for the contour
denominators, including \(|s|\) for the branch derivative. This gives
the same first-jet argument uniformly at fixed \(T\) and fixed
indices. Only the reference slice and its heat jet enter this
passage. Endpoints on the \(D\ne0\) chart have inward derivatives.
[GR Note02 §3][gr02] · [GR assessment][gr05] ·
[CM assessment §2][cm04]

## 4. Checks against the inherited pair and moment laws

Since \(D=d_0^2/4\), (5) yields \(D'=2-4DM\).
Also \(S_n=P_{n,n}\) and
\(T_n=(P_{n-1,n}+P_{n,n-1})/2=\sum_j w_j Q_j^{-n}\) for \(n\ge2\).
In (3) with \(p=q=n\), use
\[
 P_{n+1,n}-P_{n,n+1}=d_0S_{n+1},\qquad
 P_{n+2,n}+P_{n,n+2}=2S_{n+1}+d_0^2S_{n+2}
\]
to obtain
\[
 S_n'=n(C_{n+1,n}+C_{n,n+1})-4n(n+2)S_{n+1}
            -n(n+3)d_0^2S_{n+2}-nd_0^2 MS_{n+1}.
 \tag{10}
\]
For \(n=1\), \(C_{2,1}+C_{1,2}=M(P_{2,0}+P_{0,2})
=M(2M+d_0^2S_2)\), which proves
\(M'=2M^2-12S_2-16DS_3\).

For \(n=2\) the convolution sum is
\[
 S_2(P_{2,0}+P_{0,2})+P_{3,0}P_{1,2}+P_{2,1}P_{0,3}
                          +P_{3,1}P_{0,2}+P_{2,0}P_{1,3}.
\]
The identities used to simplify it are given by \(xy=Q\),
\(y-x=d_0\), \(x+y=2w\).

| Ordered pair \((U,V)\) | \(U+V\) | \(U-V\) |
| --- | --- | --- |
| \((P_{2,0},P_{0,2})\) | \(2M+d_0^2S_2\) | \(2d_0T_2\) |
| \((P_{2,1},P_{1,2})\) | \(2T_2\) | \(d_0S_2\) |
| \((P_{3,0},P_{0,3})\) | \(2T_2+2d_0^2T_3\) | \(d_0(3S_2+d_0^2S_3)\) |
| \((P_{3,1},P_{1,3})\) | \(2S_2+d_0^2S_3\) | \(2d_0T_3\) |

Combining the two crossed pairs with these sums and differences
cancels the \(T_2T_3\) and \(d_0^4 S_2S_3\) contributions. The total is
\(4MS_2+2T_2^2+d_0^2 MS_3+(d_0^2/2)S_2^2\). In (10), \(d_0^2=4D\)
then gives
\[
 S_2'=8MS_2-32S_3+4DS_2^2-40DS_4+4T_2^2 .
\]
This recovers the full spatial term of [GR Note02][gr02].
On the pure axis a check with one exterior occurrence gives
\(P_{2,0}'=-8x^{-4}-4x^{-3}y^{-1}+4d_0^{-1}x^{-3}\) from (4),
agreeing with the direct velocity \(x'=4/x+2/y-2/d_0\).
Label exchange gives the reflected one-occurrence check.

## 5. Label exchange and the merger

Replacing \(s\) by \(-s\) swaps \(P_{p,q}\) and \(P_{q,p}\) and
changes the signs of \(d_0,A_d\). The formulas transform by this
relabelling. In (8) this follows directly from swapping the rational
factors. At real time, conjugation fixes \(P_{p,q}\) when \(D>0\)
and exchanges \(P_{p,q}\) and \(P_{q,p}\) when \(D<0\).

At a target merger \(t_*\), the inherited counted pair law gives
\(D'(t_*)=2\) and the collar still separates the exterior. The
spatial contour (9) can use \(s\) as an independent parameter
in the weight \(k\) near \(s=0\), while retaining the actual target
factor \(Q(t,z)\) in the deflation. Thus the exterior sum has a
joint analytic extension in physical \(t\) and the parameter \(s\)
there. Separate its even and odd powers in \(s\) and substitute
\(s^2=D(t)\). This gives \(P_{p,q}=A(t)+s B(t)\) with \(A,B\)
locally analytic. The values at the merger are
\[
 A(t_*)=\sum_j w_j(t_*)^{-p-q},\qquad
 B(t_*)=(p-q)\sum_j w_j(t_*)^{-p-q-1}.
\]
These are the constant and linear coefficients of
\((w-s)^{-p}(w+s)^{-q}\). The sums are absolute. If \(B(t_*)\ne0\),
then \(s'=1/s-2sM\) gives \(P_{p,q}'\sim B(t_*)/s\) approaching
the merger on a chosen branch. This conditional singularity concerns
an unsymmetrized coordinate. Diagonal and symmetric combinations
extend analytically, and \((P_{p,q}-P_{q,p})/(2s)=B(t)\)
has a removable division at \(s=0\). This scope leaves the
collision-regular enlarged hierarchy to E10 and makes no assertion
that the conditional coefficient is nonzero at a canonical merger.
In the finite even polynomial heat flow initialized by
\(H(0,z)=(z^2-1)^2\), the target double at \(c=1\) leaves two exterior
occurrences at displacement \(-2\). Thus \(B(0)=-1/2\) for \(P_{2,0}\),
an explicit case of the coordinate singularity in this finite class.

## 6. Premise screen and disposition

The finite algebra works on separated counted polynomial heat
tubes and does not exclude their collisions. Those controls lack
the canonical growing population. The complete application uses
the inherited order-one paired product, strip and closed-slab count,
unchanged canonical field, and an independently cleared target
contour. The [documented controls][controls] and [E04 premise
screen][cm04] identify the failures or unpaid transfers. Euler factors
alter the canonical count discrepancy, although a coarse upper count
can survive. Endpoint-defective weighted-square, finite-source,
finite-score and finite-prime subclasses fail the fixed strip and
lose full reflected unit-weight theta equality. The reflected
super-Gaussian fails the order bound used for this product. Smooth
shape and positive-primitive controls change arithmetic with
strip/count transfer unpaid. Atomic and finite-profile controls lack
the growing canonical divisor or full profile. Conditional endpoint
mergers change ordinary Dirichlet arithmetic and assume RH. Changed
observations fail the physical cosine law, fractional profiles lose
integer multiplicity, and changed static/scalar examples lack a paid
canonical common-time tube or a realized divisor, respectively.
The algebra provides no quantitative collision discriminator.

No finite-dimensional closure, signed forcing gain, extra tube or
transport anchor follows from these equations. The proof keeps
the original family and source and uses fixed orders throughout.
E11 assesses the split and collision-regular proofs together.

[request]: ../research-progress/handoffs/VCD-GT-CM-E09-r1.md
[b04]: ../brainstorm/notes/04_VCD_GT_CM_B04_SPLIT_POLE_CLOSURE_CONTRACT_20261118.md
[cm02]: 03_VCD_GT_CM_E02_COMPLEX_POWER_TIME_LAW_20261117.md
[cm04]: ../reviews/03_VCD_GT_CM_E04_CONTOUR_PROOFS_ASSESSMENT_20261117.md
[parent]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[gr02]: ../../01_gaussian_resolvent_hierarchy/notes/02_VCD_GT_GR_E02_CANONICAL_MOMENTS_20261117.md
[gr05]: ../../01_gaussian_resolvent_hierarchy/reviews/03_VCD_GT_GR_E05_INITIAL_PROOFS_ASSESSMENT_20261117.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
