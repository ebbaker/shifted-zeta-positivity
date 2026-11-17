# VCD-GT-E03 r3 — Signed error and compensation at the collision time scale

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Explicit helper dispatch
**gpt-6.1-sol / ultra** as recorded in the frozen request. Separate backend
attestation and the lead's actual configuration are unavailable.

**Proved in-note conditional on one fixed isolated double event.**
All five input hashes in the [frozen request][request] matched. This is
an intermediate, source-linked asymptotic diagnostic for the fixed event
of [Note06][r2]. It resolves the leading signed compensation and compares
the complete combination and its residual with the next head at equal
acquired coefficient input. Separate internal assessment follows the return.
[Decision03][decision] [Result index][results] [Local heat geometry][geometry]
[Coefficient cluster][cluster] [Avoid index][avoid] [Classification][a01]
[Control catalog][catalog] [Control screening][a02] [Scope][a07]
[Separate bounds][a12]

## 1. Statement on the fixed tube

Use the event and geometry of [Note06 §§1–3][r2]. Fix an isolated
double zero of the complete normalized physical field \(F_T\) at
\(a\in\mathbb R\setminus\{0\}\), with \(0<T<1/2\). Use its fixed circle
\(\Gamma=\{|z-a|=\rho\}\) and disk in \(|\Im z|<1\), avoiding the origin,
with a positive outer buffer on a fixed compact neighborhood \(I\) of
\(T\). Write \(F_t=Q A,\ G_{j,t}=Q_j A_j\) in the disk, where \(Q\)
and \(Q_j\) are the monic pair polynomials with real centers \(c,c_j\)
and signed discriminants \(D,D_j\), and \(A,A_j\) are the respective
nonvanishing factors. Write \(A_*=A(T,a)\in\mathbb R\setminus\{0\}\).
For degree \(N\) put \(e_N=D-D_N\) and \(e_0=e_N(T)\).
The divided differences \(K,K_N\) use their own pair arguments and
the logarithmic derivatives of \(A,A_N\), as in [E02 §2][e02].

For \(v=T+s/N^2\), define the oriented integrals (including \(v<T\))
\[
 \begin{aligned}
 W_{N,v}(t)&=\exp\!\left(4\int_t^v K_N(x)\,dx\right),\\
 \mathfrak R_N(s)&=\int_T^v W_{N,v}(t)r_N(t)\,dt,\\
 \mathfrak H_N(s)&=4\int_T^v W_{N,v}(t)(K-K_N)(t)D(t)\,dt .
 \end{aligned}                                                     \tag{1}
\]
Here \(r_N\) is the exact scalar defect of [E03 r1 §3][r1]. Define
\[
 \alpha=\frac{4}{a^2},\qquad
 C_a(s)=\sum_{m\ge0}\frac{(8s/a^2)^m}{(2m)!},\qquad
 J_a(s)=\int_0^s C_a(x)\,dx,\qquad
 H_a(s)=C_a(s)-1-\alpha J_a(s).
\]
With \(\varepsilon_N=\log^2(N+1)/N\), uniformly for \(s\) in each fixed
compact real interval,
\[
 \boxed{\quad
 \begin{aligned}
 \frac{e_N(v)}{e_0}&=C_a(s)+O(\varepsilon_N),\\
 \frac{r_N(v)}{N^2 e_0}&=-\alpha C_a(s)+O(\varepsilon_N),\\
 \frac{\mathfrak R_N(s)}{e_0}&=-\alpha J_a(s)+O(|s|\varepsilon_N),\\
 \frac{\mathfrak H_N(s)}{e_0}&=H_a(s)+O(\varepsilon_N).
 \end{aligned}\quad}                                               \tag{2}
\]
Constants may depend on the fixed event, tube and interval of \(s\).
The event error \(e_0\) is eventually nonzero and has sign
\((-1)^{N+1}\operatorname{sgn}A_*\). The errors in (2) are absolute
after the indicated normalization. They hold through zeros of the
limiting profiles and through physical and model mergers.

## 2. Contour first variation and root scale

Put \(h_j^*(t)=\prod_{k=1}^j\beta_k(t)\), \(p_j(t)=h_j^*(t)/(2j)!\),
\(Z_*=\max_\Gamma |z|=|a|+\rho\), and \(\bar p_j=\sup_I p_j\).
[E01 (2), (7)][e01] and [E03 r1 (3), (6)][r1] give on the fixed disk
\[
 \begin{aligned}
 \Delta_j(t,z)&=F_t(z)-G_{j,t}(z)=(-1)^j p_j(t)z^{2j}E_{j,t}(z),\\
 R_N(t,z)&=(-1)^{N-1}(2N)(2N-1)p_N(t)z^{2N-2}\Psi_{N,t}(z),
 \end{aligned}                                                     \tag{3}
\]
where \(E_{j,t}-1=O(\varepsilon_j)\) and
\(\Psi_{N,t}-1=O(\varepsilon_N)\) uniformly on the disk and \(I\).
The adjacent bound gives \(\bar p_j\le B_{j-1}^j/(2j)!\) with
\(B_{j-1}=O(\log^2(j+1))\). Thus \(j^k \bar p_j M^{2j}\to0\) for
every fixed \(k\ge0,\ M>0\), by \((2j)!\ge j^j\).
The exact normalized monic norm flow, used in [Note06 §4][r2], gives
\[
 (\log p_j)'=\beta_j+\beta_{j+1}-\beta_1,\qquad
 \left|\log\frac{p_j(t)}{p_j(T)}\right|
     \le (B_j+B_0)|t-T|.
                                                                    \tag{4}
\]
In particular, on the critical time scale \(p_j(t)/p_j(T)
=1+O(\log^2(N+1)/N^2)\) for \(j=N,N+1\).
This comparison uses positivity and an upper bound on the log derivative.

Denote \((2\pi i)^{-1}\oint_\Gamma\) by \(\langle\,\cdot\,\rangle\),
including the differential \(dz\). At fixed \(t\), take moments of
the two pairs in the variable \(z-c(t)\). The physical first moment
vanishes. On a fixed zero-free collar of \(\Gamma\), the small
ratio \(\Delta_j/F_t\) gives the holomorphic logarithm
\[
 \mathcal L_j(t,z)=\log(G_{j,t}(z)/F_t(z))
      =-\Delta_j(t,z)/F_t(z)+O(p_j(t)^2 Z_*^{4j})
      \qquad (z\in\Gamma).
\]
The remainder uses the fixed positive floor on \(\Gamma\) and the
single-time bound in (3). A slightly wider radius suffices to
guarantee a strict log-series condition on the collar for all large
\(j\). Integrating by parts, the model minus physical \(k\)-th moment
is \(-k\langle(z-c)^{k-1}\mathcal L_j\rangle\). Therefore
\[
 \begin{aligned}
 c_j-c&=O(p_j(t)Z_*^{2j}),\\
 D_j-D
   &= -\langle (z-c)\mathcal L_j\rangle -(c_j-c)^2\\
   &= \left\langle\frac{(z-c)\Delta_j}{F_t}\right\rangle
                   +O(p_j(t)^2 Z_*^{4j}).
 \end{aligned}
\]
For physical roots \(z_\pm=c\pm\sqrt D\), the factor \((z-c)/Q\)
is the half-sum of the two Cauchy kernels, with the same formula at a
double. Their numerator \(\Delta_j/A\) is holomorphic in the disk.
Thus, writing \(e_j=D-D_j\) at degree \(j\),
\[
 e_j(t)=-\frac12\sum_\pm\frac{\Delta_j(t,z_\pm)}{A(t,z_\pm)}
                      +O(p_j(t)^2 Z_*^{4j}).                       \tag{5}
\]
This gives \(D_j-D=O(p_j(t)Z_*^{2j})\) directly from the contour.
At \(T\), (5) and (3) yield
\[
 e_j(T)=
 -\frac{(-1)^j p_j(T)a^{2j}}{A_*}\,[1+O(\varepsilon_j)].              \tag{6}
\]
In (5) at \(t=T+s/N^2\), the remainder divided by
\(p_j(T)|a|^{2j}\) is \(O(p_j(T)(Z_*^2/|a|)^{2j})\) for
\(j=N,N+1\), by (4). It decreases faster than any power of \(1/j\).
This relative estimate retains an actual norm factor even if
individual links are small.

The contour formulas make \(c,D\) differentiable in \(t\) and bounded
with their derivatives on \(I\). The physical equation \(D'=2+4KD\),
bounded \(K\), and \(D(T)=0\) give
\[
 c(t)=a+O(|t-T|),\qquad D(t)=2(t-T)+O((t-T)^2).
\]
Take the square root of a nonnegative real to be nonnegative, and of a
negative real to have positive imaginary part. For reals \(x,y\),
\(|\sqrt x-\sqrt y|\le\sqrt{|x-y|}\), by the ordinary real inequality
for equal signs and Pythagoras for opposite signs. For \(t=T+s/N^2\),
one has \(N\sqrt{D(t)}=\sqrt{2s}+O(N^{-2})\) uniformly on fixed
\(s\) compacts, by factoring
\(D(t)=2(s/N^2)(1+O(|s|/N^2))\) at \(s\ne0\), and using
\(D(T)=0\) at \(s=0\). The fixed-contour coordinate estimates and the
factorial bound then give, for both physical and degree-\(N\) model
pairs,
\[
 N(z_\pm-a)=\pm\sqrt{2s}+O(N^{-1}),\qquad
 N(z_{\pm,N}-a)=\pm\sqrt{2s}+O(N^{-1}).                              \tag{7}
\]
The square root inequality includes changes of root type. On either
pair \(z_\pm^*\), the local analytic log at \(z_\pm^*/a=1\) satisfies,
for \(k=2N,2N-2\),
\[
 k\log(z_\pm^*/a)=\pm 2\sqrt{2s}/a+O(N^{-1}).
\]
Hence the average of \((z_\pm^*/a)^k\) is \(C_a(s)+O(N^{-1})\)
uniformly. Each power is uniformly bounded on the fixed \(s\) compact,
also for \(s<0\) and \(a<0\).

On the contour, \(|Q|,|Q_j|\) have fixed positive lower bounds from
the buffer. Dividing out these polynomials and subtracting yields
\(A_j-A=O(p_j(t)Z_*^{2j})\) there and on the disk by maximum modulus.
The smooth time dependence of \(F_t\) and of the physical coordinates
gives \(A(t,\cdot)-A(T,\cdot)=O(|t-T|)\) by the same boundary
comparison and maximum modulus. Since \(A(T,\cdot)\) is holomorphic,
all relevant factor values at the roots in (7) equal
\(A_*+O(N^{-1})\), with a fixed positive modulus floor for large \(N\).
Now insert (3), (4) and the power averages into (5) and divide by (6).
This proves the first line of (2). The pair average gives the oscillatory
profile for \(s<0\).

## 3. Defect and integrated drift transfer

Let \(z_{\pm,N}\) be the degree-\(N\) pair. The exact defect formula
[E03 r1 (7)][r1] gives, again by the half-sum of two Cauchy kernels,
\[
 r_N(t)=-\left\langle(z-c_N)\frac{R_N(t,z)}{G_{N,t}(z)}\right\rangle
       =-\frac12\sum_\pm \frac{R_N(t,z_{\pm,N})}{A_N(t,z_{\pm,N})}.   \tag{8}
\]
The identity holds at coincident roots. Substitute (3), (4), (7)
and the factor comparison into (8). Its leading signed coefficient is
\(-(-1)^{N-1}(2N)(2N-1)p_N(T)a^{2N-2}/A_*\), times \(C_a(s)\).
Dividing by \(N^2 e_0\) in (6) gives the second line of (2), since
\((2N)(2N-1)/(N^2 a^2)=\alpha+O(N^{-1})\).
The model time equation is the exact residual equation of
[E03 r1 §§1–3][r1]. The scalar phase bounds in (3) are used pointwise
in time.

By [E02 §2][e02] and the fixed contour floor and derivative bound
from [Note06 §1][r2], \(K_N\) is uniformly bounded on \(I\).
For \(x\) between \(0\) and \(s\),
\(W_{N,v}(T+x/N^2)=1+O(|s|/N^2)\).
Insert the uniform defect estimate into (1) and change variables
\(t=T+x/N^2\). This proves the residual integral in (2), with
\(O(|s|\varepsilon_N)\) after normalization even at arbitrarily short
or negatively oriented intervals.

To estimate the drift integral, subtract the exact physical and
model discriminant equations:
\[
 e_N'=4K_Ne_N+4(K-K_N)D-r_N .
\]
Since \(\partial_t W_{N,v}=-4K_N W_{N,v}\), integration from \(T\)
to \(v\) gives the exact identity in either orientation
\[
 W_{N,v}(T)e_0=e_N(v)+\mathfrak R_N(s)-\mathfrak H_N(s).             \tag{9}
\]
The terms already estimated and \(W_{N,v}(T)=1+O(|s|/N^2)\)
give the fourth line of (2). Thus the two signed integrals taken
together have profile
\((\mathfrak R_N-\mathfrak H_N)/e_0=1-C_a(s)+O(\varepsilon_N)\).
The summed combination in (9) has the exact normalized value
\(W_{N,v}(T)\). This argument gives an integrated \(K\)-transfer
estimate.

## 4. Signs, compensation, and the shorter time scale

For \(u=\sqrt{8|s|}/|a|\), the normalized profiles take the following
real values, with all integral profiles zero at \(s=0\).

| Time | \(C_a(s)\) | \(\alpha J_a(s)\) | \(H_a(s)\) |
| --- | --- | --- | --- |
| \(s>0\) | \(\cosh u\) | \(u\sinh u-\cosh u+1\) | \(2(\cosh u-1)-u\sinh u\) |
| \(s<0\) | \(\cos u\) | \(1-\cos u-u\sin u\) | \(2(\cos u-1)+u\sin u\) |

These follow by integration with \(\alpha\,ds=\pm u\,du\). The
signed residual integral has normalized profile \(-\alpha J_a(s)\).
At every nonzero profile value the corresponding normalized quantity
eventually has its sign. At the zeros \(u=(m+1/2)\pi\) of \(C_a\) on
the negative side, the first two lines of (2) are \(O(\varepsilon_N)\)
on their event scales. The integral profiles there remain
\(1-u\sin u\) for \(\alpha J_a\) and \(u\sin u-2\) for \(H_a\).
The residual integral also has separate zeros of its own profile.
For example \(u=2\pi\) with \(s<0\) gives \(\alpha J_a(s)=0\).
Any ratio to a vanishing leading profile requires a finer estimate.

The sum of the absolute values of the three terms on the right of (9)
divided by the absolute value of their signed sum tends uniformly on
fixed \(s\) compacts to
\[
 \chi(s)=|C_a(s)|+|\alpha J_a(s)|+|H_a(s)|.
\]
For \(s>0\), \(\alpha J_a(s)>0\) and
\(u\sinh u-2(\cosh u-1)>0\). The latter function and its first
derivative vanish at zero, and its second derivative is \(u\sinh u>0\).
Thus \(H_a(s)<0\) and \(\chi(s)=1+2\alpha J_a(s)\).
This factor can be arbitrarily large by choosing a large fixed \(s>0\)
before the \(N\) limit. At \(s<0,\ u=\pi\), the three leading terms
of (9) are \(-1,-2,4\) in units of \(e_0\), so \(\chi=7\).
These are comparisons of actual signed terms and their separate
absolute magnitudes. An evaluator may still need budgets for all the
terms before making use of the cancellation.

For \(\tau_N=o(N^{-2})\), put \(s_N=N^2\tau_N\). On the interval
between \(T\) and \(T+\tau_N\), (2) gives
\[
 \frac{e_N(t)}{e_0}\longrightarrow 1,\qquad
 \frac{r_N(t)}{r_N(T)}\longrightarrow 1
\]
uniformly, since \(C_a(0)=1\) and \(r_N(T)/(N^2e_0)\to-\alpha\).
For \(\tau_N\ne0\), this recovers
\(\mathfrak R_N(s_N)\sim\tau_N r_N(T)\) in either orientation.
Equivalently its normalized size is
\(-\alpha s_N[1+O(|s_N|+\varepsilon_N)]\).
Taylor expansion gives
\(H_a(s)=-16s^2/(3a^4)+O(s^3)\) near zero.
The fourth line of (2) gives
\(\mathfrak H_N(s_N)/e_0=O(|s_N|^2+\varepsilon_N)\).
This estimate controls its absolute limit on the event-error scale.
A relative subcritical drift asymptotic for unrestricted \(s_N\to0\)
would need a sharper error that decreases with the interval length.

## 5. Comparison at the same first \(N\) links

The residual \(R_N\) and \(G_{N+1}\) both use exactly
\(\beta_1,\ldots,\beta_N\) as their actual coefficient inputs. Define
\[
 b_N=\frac{\beta_{N+1}(T)a^2}{(2N+1)(2N+2)}>0 .
\]
The first omitted link enters the next-head error amplitude.
Using (6) at each degree separately yields
\[
 \frac{e_{N+1}(T)}{e_0}=-b_N[1+O(\varepsilon_N)],\qquad
 \frac{e_{N+1}(v)}{e_0}=-b_N[C_a(s)+O(\varepsilon_N)].               \tag{10}
\]
For the second estimate apply the first line of (2) at degree \(N+1\)
and argument \(((N+1)/N)^2s\). The smooth profile varies by \(O(N^{-1})\)
on the enlarged compact. In (10) use \(\beta_{N+1}(T)\le
B_N-\beta_N(T)\le B_N\), which gives \(b_N=O(\log^2(N+1)/N^2)\).
Each normalization uses the actual same-degree norm, with no lower
bound on the omitted link.

The following comparisons to the eventually nonzero **event**
next-head error \(e_{N+1}(T)\) are uniform absolute estimates after
multiplication by \(b_N\):
\[
 \begin{aligned}
 b_N\,\frac{e_N(v)+\mathfrak R_N(s)-\mathfrak H_N(s)}{e_{N+1}(T)}
      &=-1+O(\varepsilon_N),\\
 b_N\,\frac{\mathfrak R_N(s)}{e_{N+1}(T)}
      &=\alpha J_a(s)+O(|s|\varepsilon_N),\\
 b_N\,\frac{r_N(v)}{N^2 e_{N+1}(T)}
      &=\alpha C_a(s)+O(\varepsilon_N).
 \end{aligned}                                                     \tag{11}
\]
The complete combination has magnitude asymptotic to
\(1/b_N\) times the next-head error at \(T\), at least of order
\(N^2/\log^2(N+1)\) larger. The exact unweighted error at the common
target \(T\) is
\[
 \frac{e_N(v)+\mathfrak R_N(s)-\mathfrak H_N(s)}{W_{N,v}(T)}=e_N(T).
\]
Divide by \(W_{N,v}(T)\) before comparison with \(e_{N+1}(T)\), or
weight the next-head error by the same \(W_{N,v}(T)\). Either gives
the exact same-ordinate ratio \(e_N(T)/e_{N+1}(T)\), and
\(W_{N,v}(T)=1+O(|s|/N^2)\) preserves the asymptotic in (11).

For fixed \(s\) with \(J_a(s)\ne0\)
the residual integral has magnitude asymptotic to
\(|\alpha J_a(s)|/b_N\) times that same comparator.
The next-head error at \(v\) in (10) describes a different target time.
At a zero of \(C_a\), its modulus is \(O(b_N\varepsilon_N|e_0|)\),
with no sign asserted there.

On the shorter time scale with \(\tau_N\ne0\), the earlier signed
comparison follows from \(\mathfrak R_N(s_N)\sim \tau_N r_N(T)\)
and [Note06 (6)][r2], or from (6) and (8) at \(T\). With
\(\Pi_N=(2N-1)(2N)(2N+1)(2N+2)\),
\[
 \frac{\mathfrak R_N(s_N)}{e_{N+1}(T)}
     \sim\frac{\tau_N\Pi_N}{\beta_{N+1}(T)a^4}.
\]
For \(\tau_N=N^{-3}\) this is
\(\sim 16N/(\beta_{N+1}(T)a^4)\).
The sign here uses \(e_{N+1}(T)=-D_{N+1}(T)\).
The comparison matches the first \(N\) link indices. The next-head
evaluation at \(T\) needs only the coefficient snapshot at \(T\).
A direct comparator has access to all shared measurements. Whole-slab
coefficient acquisition, numerical evaluation, and access to
complete-source data have separate costs outside this error comparison.

## 6. Analytical controls and scope

The proof uses the literal normalized Fourier observation under
quadratic heat tilt, the stipulated fixed isolated double event and
buffer, infinite positive Jacobi norms, the E01 cosh and adjacent
envelopes and the exact E03 r1 residual law with its phase estimate.
The same proof applies to fixed even positive Fourier source families
possessing all these premises, with the needed time domination and
exponential moments. Constants concern each fixed source and event.
The controls below were screened analytically against their documented
premises. [E01 §6][e01] [E03 r1 §6][r1] [Note06 §5][r2]
[Control catalog][catalog]

| Control | Premise verdict |
| --- | --- |
| Exact quadratic heat collision | Gives \(c=a,\ D=2(t-T),\ K=0\). Its exact incoming gap is exhausted at \(T\). The quadratic lacks the infinite positive Jacobi source for (3) and (6). |
| Three- and four-square fixed double controls | Their own counted interior events pass the heat law, the phase and coefficient envelopes, and the exact residual law. The half-line score argument includes the vanishing junction term. The critical profiles apply on their event tubes and fail to distinguish them from a stipulated theta event. They lack the full canonical reflection and complete equal square coefficients, which the proof does not use. Their finite-source class has no finite all-real heat threshold. |
| Euler-factor controls | Their literal transforms have a quadrature law. The tested \(c=1/2,\ p=23\) member fails the \(B_0\) premise at time zero, so it fails the inherited whole-range bound. This test gives no verdict at an arbitrary interior event interval or for other members. A threshold witness alone supplies no fixed counted tube. The ordinary theta and Dirichlet coefficients change. |
| Reflected super-Gaussian and smooth shape or positive-primitive controls | The super-Gaussian fails the inherited exponential score confinement. Its degree bounds remain untested. The smooth and primitive controls lack the canonical summand score, and their weaker quantitative envelopes remain untested in the catalog scopes. They lack the unchanged integer-square arithmetic. |
| Finite-tail, finite-prime and finite-score/head controls | The screened positive weights can retain the relevant envelopes while failing the full canonical identities. The orbit constructions vary the source and escape in height. A finite match gives no fixed canonical event. A fixed control event satisfying all the premises is covered by the theorem on its own tube. |
| Atomic and compact thresholds | Finite atomic chains terminate, and the inherited three-atom example fails the adjacent bound at index one. The compact triangular extensions lack the positive-density premise of the inherited score proof. Their quantitative envelopes require a separate test. |
| RH-conditional normalized endpoint controls | They retain RH as a hypothesis and fail ordinary Dirichlet series arithmetic. Their time-zero doubles lie outside the interior-event hypothesis. |
| Changed observation, actual-profile relaxation | The former fails the prescribed literal Fourier heat observation. The latter fails to specify an actual physical field with a counted pair. |

The event remains stipulated for the complete canonical source.
This local comparison acquires no canonical tube, coefficient values,
strict gap margin, global threshold or numerical certificate. It
quantifies compensation for (9) within the fixed event and matched
prefix class. Other signed estimators, source-specific bounds,
and changing heights and clusters remain outside this comparison.

[request]: ../research-progress/handoffs/VCD-GT-E03-r3.md
[decision]: ../brainstorm/notes/03_VCD_GT_B03_CRITICAL_SCALE_DECISION_20261116.md
[e01]: 03_VCD_GT_E01_PHYSICAL_TIME_SIGNED_ERROR_20261116.md
[e02]: 04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md
[r1]: 05_VCD_GT_E03_PHYSICAL_MODEL_DEFECT_20261116.md
[r2]: 06_VCD_GT_E03_FIXED_EVENT_DEFECT_20261116.md
[results]: ../../../../../result-summaries/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[cluster]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
