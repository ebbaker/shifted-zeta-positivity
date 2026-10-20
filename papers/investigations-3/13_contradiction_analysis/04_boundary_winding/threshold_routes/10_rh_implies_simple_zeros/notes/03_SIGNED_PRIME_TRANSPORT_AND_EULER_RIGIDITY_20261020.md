# Signed prime transport and effective Euler-control rejection

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded session metadata. Separate same-model derivation
and [internal review](../reviews/03_SIGNED_TRANSPORT_AND_COEFFICIENT_REVIEW_20261020.md);
no specialist review or claim of methodological priority.

**Outcome:** exact signed prime transport and pole/main cancellation;
a quantitative failure for the stated RH error-envelope strategy; and
effective arithmetic rejection of every nonconstant member of a declared
finite Euler-polynomial control class. No multiple theta zero, height
interval, strict cap surplus or negative Gaussian deficit is obtained.

This continues [Note 02](02_FINITE_PRIME_FEJER_RESOLUTION_TEST_20261020.md)
within the [program](../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md).
The [result index](../../../../../../../result-summaries/README.md),
[collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../../../../avoid/README.md) apply, particularly
[equivalent targets](../../../../../../../avoid/01_restating_the_target.md),
[control premises](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[separate payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
and [gain before expansion](../../../../../../../avoid/20_volume_without_a_gain.md).
The signed finite-prime sum is retained until the global error bound is
applied. This is a different estimating step from Note 02's absolute-prime
payment, with its own scope.

## 1. Notation and a checked RH input

Retain Note 02's squared-sinc test and exact identity
\[
 S_\Delta(\gamma)=G_\Delta(\gamma)+P_\Delta(\gamma)-Q_\Delta(\gamma),
 \qquad m(\gamma)\le S_\Delta(\gamma)
\]
under RH at an actual zero ordinate. Put
\[
 V=2\pi\Delta,\quad X=e^V,\quad
 \Psi(x)=\sum_{n\le x}\Lambda(n),\quad E(x)=\Psi(x)-x,
 \quad F(v)=e^{-v/2}E(e^v).
\]
Thus
\[
 Q_\Delta(\gamma)=\frac2V\Re\int_1^X
 x^{-1/2-i\gamma}\left(1-\frac{\log x}{V}\right)d\Psi(x).   \tag{1}
\]
This is a finite Stieltjes sum; it makes no critical-strip continuation of an Euler series.

A primary source checked here is Lee–Nosal, [*Sharper bounds for the error in the prime number theorem assuming the Riemann Hypothesis*, arXiv:2312.05628v4](https://arxiv.org/pdf/2312.05628v4), equation (1) and Theorem 1.2. The former records, under RH and for `x>=2`,
\[
 |E(x)|\le\sqrt x\left(2\log x+\frac{(\log x)^2}{8\pi}\right).
\]
For `1<=x<2`, `Psi(x)=0`. Consequently the explicit convenient global envelope
\[
 \boxed{|F(v)|\le W(v):=\sqrt2+2v+\frac{v^2}{8\pi},\qquad v\ge0} \tag{2}
\]
is available. Its extra constant avoids a separate small-x computation. The same source proves the sharper bound
\[
 |F(v)|\le\frac{v(v-\log v)}{8\pi},\qquad v\ge\log101,       \tag{3}
\]
which will screen the exact control below. Neither imported result assumes simplicity; neither is claimed to be the best presently available bound.

## 2. The complete signed transport identity

Let
\[
 \alpha=\frac12-i\gamma,\qquad
 M_{V,\gamma}=\int_0^V e^{\alpha v}(1-v/V)dv
 =\frac{e^{\alpha V}-1-\alpha V}{V\alpha^2}.
\]
Integrate (1) by parts after writing `dPsi=dx+dE`. At the upper endpoint the taper vanishes; at the lower endpoint `E(1)=-1`, which supplies the term **+1**. No endpoint term may be dropped. We obtain
\[
 Q_\Delta(\gamma)=\frac2V\left[1+\Re M_{V,\gamma}
     +I_{V,\gamma}\right],                                \tag{4}
\]
where the real signed correlation is
\[
 I_{V,\gamma}=\int_0^V F(v)\,k_{V,\gamma}(v)dv,
\]
\[
 \boxed{k_{V,\gamma}(v)=
 \left[\frac12(1-v/V)+\frac1V\right]\cos(\gamma v)
 +\gamma(1-v/V)\sin(\gamma v).}                            \tag{5}
\]
Indeed the differentiated weight is
\[
 -x^{-3/2-i\gamma}\left[(1/2+i\gamma)(1-\log x/V)+1/V\right],
\]
which proves all signs and the frequency multiplier gamma in (5).

**Pay the main and pole terms together.** The exact pole contribution of Note 02 is
\[
 P_\Delta(\gamma)=\frac4{V^2}\Re\frac{\cosh(\alpha V)-1}{\alpha^2}.
\]
Hence the apparently large `exp(V/2)` part of M cancels identically with its partner in P. Define
\[
 R_{V,\gamma}=P_\Delta(\gamma)-\frac2V(1+\Re M_{V,\gamma})
 =-\frac2V+\frac2{V^2}\Re
 \frac{e^{-\alpha V}-1+\alpha V}{\alpha^2}.                 \tag{6}
\]
The exact consumer is therefore
\[
 \boxed{S_\Delta(\gamma)=G_\Delta(\gamma)+R_{V,\gamma}
                         -\frac2V I_{V,\gamma}.}           \tag{7}
\]
Moreover
\[
 \boxed{\left|R_{V,\gamma}+\frac2V\right|
 \le\frac{1/V+4/V^2}{\gamma^2+1/4}.}                       \tag{8}
\]
To check the bound, `|exp(-alpha V)-1|<=2`, `|alpha|^2=gamma^2+1/4`, and `Re(1/alpha)=(1/2)/(gamma^2+1/4)`.

Thus the ensuing failure is not caused by independently bounding two large terms that should have cancelled. The finite-source normalization and both pole terms are fully paid.

## 3. What the global RH envelope actually proves

Applying (2) only at this point gives
\[
 |I_{V,\gamma}|
 \le\sqrt{\gamma^2+1/4}\,A(V)+B(V),                        \tag{9}
\]
where the elementary integrals are exact:
\[
 A(V)=\int_0^V W(v)(1-v/V)dv
 =\frac{\sqrt2V}{2}+\frac{V^2}{3}+\frac{V^3}{96\pi},
\]
\[
 B(V)=\frac1V\int_0^V W(v)dv
 =\sqrt2+V+\frac{V^2}{24\pi}.
\]
The factor `sqrt(gamma^2+1/4)` follows by bounding the complex factor `(1/2+i gamma) exp(-i gamma v)` before taking its real part. The resulting two-sided interval for the signed consumer has half-width
\[
 L_{V,\gamma}:=\frac2V\left[\sqrt{\gamma^2+1/4}\,A(V)+B(V)\right].
                                                                    \tag{10}
\]
At the microscopic rule `Delta=c log gamma`, so `V=2 pi c log gamma`,
\[
 L_{V,\gamma}\sim\frac{\gamma V^2}{48\pi}
 =\frac{\pi c^2}{12}\,\gamma(\log\gamma)^2.                \tag{11}
\]
Meanwhile the exact gamma term from Note 02 tends to `1/(2 pi c)` and R tends to zero. The available interval therefore supplies no order-one upper bound, much less a bound below two. Improvements such as (3) change lower-order factors of this payment, not its derivative loss.

The putative event is retained: if `m(gamma)>=2`, (7) merely imposes
\[
 \frac2V I_{V,\gamma}\le G_\Delta(\gamma)+R_{V,\gamma}-m(\gamma).
                                                                    \tag{12}
\]
This is compatible with (9). It is not an independently proved opposite sign. Nothing in the global RH bound changes (12) into a contradiction.

**Scope and sharpness of the loss.** For the information class consisting only of arbitrary real functions `F` satisfying `|F|<=W`, the exact norm of this real linear functional is
\[
 \sup_{|F|\le W}\left|\frac2V\int_0^V F(v)k_{V,\gamma}(v)dv\right|
 =\frac2V\int_0^V W(v)|k_{V,\gamma}(v)|dv.
\]
Choosing `F=W sign(k)` attains it in the measurable class; smooth approximations attain the supremum arbitrarily closely. Along `V=2 pi c log gamma`, elementary averaging of `|sin(gamma v)|` gives
\[
 \frac2V\int_0^V W|k|\sim\frac{\gamma V^2}{24\pi^2}.       \tag{13}
\]
Indeed the sine term dominates and `A(V)~V^3/(96 pi)`. The periodic function `|sin u|-2/pi` has a bounded primitive. Integration by parts against the polynomial weight `W(v)(1-v/V)` gives an averaging error `O(V^2/gamma)` in its weighted integral. After multiplication by gamma this is `O(V^2)`; the cosine term contributes at most `O(V^3)`. Both are smaller than the main `gamma V^3` term. Thus the frequency loss is inherent in this **pointwise-envelope-only** information class. These optimizing F are not asserted to be Chebyshev functions of primes or to preserve arithmetic. Equation (13) is not a no-go theorem for the complete unchanged prime data.

## 4. A multiple zero's resonant mode fits well inside the RH envelope

This observation explains why the preceding estimate cannot see simplicity. A zero pair `1/2+-i gamma`, each of multiplicity m, has the usual individual explicit-formula contribution
\[
 E_{m,\gamma}(x)=-2m\Re\frac{x^{1/2+i\gamma}}{1/2+i\gamma},
\quad
 F_{m,\gamma}(v)=-2m\Re\frac{e^{i\gamma v}}{1/2+i\gamma}.
                                                                    \tag{14}
\]
Its normalized amplitude is at most `2m/sqrt(gamma^2+1/4)`: for fixed m it is very small at high ordinate and fully consistent with a global `O(v^2)` normalized error budget. This concerns an individual mode; no termwise absolute summation of the full zero formula is used.

Nevertheless the mode is exactly resonant with the signed transport. Differentiate its smooth contribution, retaining its own lower endpoint if using integration by parts. Direct integration in (1) gives its contribution to Q as
\[
 \boxed{Q[E_{m,\gamma}]
 =-m\left[1+\left(\frac{\sin(V\gamma)}{V\gamma}\right)^2\right].}
                                                                    \tag{15}
\]
The first term is the zero at the center; the second is its reflected partner. The factor gamma in (5) recovers this order-one mass from an error mode of amplitude `O(m/gamma)`. Therefore a bound controlling only the size of E naturally allows the signal that a multiple zero would require.

For a separate limited control on the meaning of (14), the smooth counting model
`Psi_model(x)=x+E_{m,gamma}(x)` has nonnegative derivative for `x>=4m^2`, because
`Psi_model'(x)=1-2m x^{-1/2} cos(gamma log x)>=0` there. It has a much smaller error than the RH budget and still carries (15). It lacks prime support and an Euler product, and is not a counterexample to a theorem about zeta. Its only role is to show that eventual positivity of a counting density does not remove the displayed loss.

## 5. The exact Euler control also satisfies the global RH error class

The stronger required test uses the actual endpoint control, not the smooth illustration. For
\[
 D_p(s)=\zeta(s)(1+\sqrt p\,p^{-s})^2,
\]
its logarithmic prime coefficients differ from zeta's at `p^r` by
`2 log p (-1)^{r-1}p^{r/2}`. Its own signed Chebyshev sum therefore obeys
\[
 \Psi_p(x)-\Psi(x)=2\ell\sum_{1\le r\le\log x/\ell}
 (-1)^{r-1}p^{r/2},\qquad\ell=\log p.
\]
Summing the geometric progression proves
\[
 \boxed{|\Psi_p(x)-\Psi(x)|\le2\ell\sqrt x.}                \tag{16}
\]
If `q=sqrt p` and the upper integer is `M>=1`, its sum is
`q(1-(-q)^M)/(1+q)`. For odd M, its modulus is at most `q^M`
because `q<=q^M`; for even M it is strictly smaller than `q^M`.
The sum is empty for `x<p`. This proves (16).

In fact, for every prime **`p>=101` the control satisfies exactly the same
global envelope (2)**, including its constants. For `x<p` its Chebyshev
sum is unchanged. For `x>=p`, combine (3) with (16) and use
`2 log p<=2 log x`:
\[
 e^{-v/2}|\Psi_p(e^v)-e^v|
 \le \frac{v(v-\log v)}{8\pi}+2\log p
 \le W(v),\qquad v\ge\log p .
\]
Thus screening is for the actual input used in (9), not merely for an
unspecified big-O class.

Even the unchanged leading classical constant does not distinguish the control eventually. Combining (3) with (16) gives
\[
 |\Psi_p(e^v)-e^v|\le\sqrt{e^v}\,\frac{v^2}{8\pi}
\]
whenever
\[
 v\ge\log101,\qquad v\log v\ge16\pi\log p.                \tag{17}
\]
The control's coefficients are signed and fail zeta's exact nonnegative coefficient condition; its completion also changes conductor. Those failures are retained. They do not alter the fact that the named global RH error estimate is shared. A proof using more arithmetic than (2) could still distinguish them, but applying (2) alone cannot claim to have done so.

The control's completion has conductor `p^2`. Its own gamma/conductor
term is `G_{Delta,p}=G_Delta+2 log p/V`; the pole term is unchanged and
the prime measure is `dPsi_p`. Retaining these terms gives precisely
Note 02's response: at an added double-zero ordinate
`gamma_k=(2k+1)pi/log p`,
\[
 S_{\Delta,p}(\gamma_k)-S_\Delta(\gamma_k)
 =2\left[1+\frac{\{V/\log p\}(1-\{V/\log p\})}{(V/\log p)^2}\right]\ge2.
\]
There is no comparison using the control's zeros but zeta's conductor
or coefficients.


## 6. Effective rejection by logarithmic coefficient positivity

The unchanged coefficients do provide a stronger discriminator than
the global bound above. Consider exactly the finite class
\[
 D(s)=\zeta(s)\prod_{p\in\mathcal S}P_p(p^{-s}),\qquad
 P_p(z)=\prod_{j=1}^{d_p}(1-\beta_{p,j}z),\qquad
 |\beta_{p,j}|=\sqrt p,
\]
where \(\mathcal S\) is finite and each polynomial has real coefficients
and constant term one. A nonconstant factor introduces a vertical
lattice of zeros on the critical line. A conductor exponential does
not change that zero set. This proposition needs no RH assumption.

In \(\Re s>1\), the absolutely convergent logarithmic derivative has
coefficients
\[
 -D'/D=\sum_{n\ge2}a_D(n)n^{-s},\qquad
 a_D(p^k)=\log p\left(1-\sum_{j=1}^{d_p}\beta_{p,j}^{\,k}\right).
                                                               \tag{18}
\]
Unique prime-power support prevents different primes from cancelling
this coefficient.

**Proposition.** If \(d=d_p\ge1\), a negative coefficient occurs for
some \(1\le k\le12^d\), with the explicit margin
\[
 a_D(p^k)\le-\left(\frac{\sqrt3}{2}d p^{k/2}-1\right)\log p
 \le-\left(\sqrt{3/2}-1\right)\log p<0.                    \tag{19}
\]
For every integer \(N\ge1\), there is such a \(k\) in
\([N,12^dN]\).

**Proof.** Write \(\beta_{p,j}=\sqrt p\,e^{2\pi i\theta_j}\).
Among \(12^d+1\) points \(r(N\theta_1,\ldots,N\theta_d)\) modulo one,
\(0\le r\le12^d\), two occupy the same one of \(12^d\) cubes of side
\(1/12\). Their index difference \(q\) satisfies
\(1\le q\le12^d\) and \(\|Nq\theta_j\|\le1/12\) for every \(j\).
Put \(k=Nq\). Each cosine is at least \(\sqrt3/2\), so
\(\Re\sum_j\beta_{p,j}^k\ge(\sqrt3/2)d p^{k/2}>1\).
The sum is real because the reciprocal roots are invariant under
conjugation. Equation (18) proves (19), including its stated uniform
margin. ∎

For \(P_p(z)=(1+\sqrt p\,z)^2\), the sharper witness is already
\(a_D(p^2)=(1-2p)\log p<0\). Thus actual zeta positivity
\(a_\zeta(p^k)=\log p>0\) rejects the whole declared nonconstant finite
class, not merely the chosen endpoint example. The bound \(12^d\)
is effective, not optimized.

**The event-to-coefficient implication is missing.** A multiple zero
of the original zeta function does not imply a finite factor
\(P_p(p^{-s})\), nor the vertical periodicity it introduces. Dividing
by a local zero polynomial need not preserve an Euler product or an
ordinary Dirichlet series. Consequently (19) rejects these controls
but does not reject the hypothesized original event.

Arbitrary infinite Euler assemblies are outside this proposition.
In that setting it would also be unjustified to assume a local
factor's zeros survive analytic continuation of the complementary
product: that continuation may supply compensating poles. Absolute
convergence in the initial half-plane does not settle this issue.

Even nonnegative logarithmic coefficients combined with all-realness
do not bound an atom by one. Under the same RH assumption,
\(\zeta(s)^r\), \(r\ge2\), has completion \(\xi(s)^r\), nonnegative
coefficients \(r\Lambda(n)\), and all original zero masses multiplied
by \(r\). Its complete Poisson and Fejér identities scale by \(r\).
It fails the unchanged gamma degree, pole order and coefficients:
these become \(r,r,r\Lambda(n)\), respectively; its conductor remains
one. This comparison does not have all of zeta's exact arithmetic
data. In particular the bound \(a_\zeta(p^k)\le\log p\) rejects it.
No impossibility result for the full unchanged data follows.

### An isolated endpoint control retaining the gamma factor and conductor

The gamma and conductor distinction by itself also has a precise
limitation. For sufficiently large \(A>0\), set
\[
 F_A(x)=H(0,x)(1-x^2/A^2)^2,\qquad
 \Phi_A=\Phi+2A^{-2}\Phi''+A^{-4}\Phi''''.                 \tag{20}
\]
Evenness and decay remove every boundary term in the Fourier
integrations by parts, so these are an exact source/transform pair.
The source is strictly positive. To prove this, let
\[
 C_j=\max\{0,-\inf_{\mathbb R}\Phi^{(j)}/\Phi\},\quad j=2,4.
\]
Both constants are finite: the positive theta source is smooth and
\(\Phi''/\Phi\sim16\pi^2e^{8|u|}\),
\(\Phi''''/\Phi\sim256\pi^4e^{16|u|}\) at infinity.
These differentiated tails are recorded in
[Investigation 21, Note 52, equation (7)](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md).
Thus, if \(A^2\ge\max\{1,4C_2,2\sqrt{C_4}\}\),
\[
 \Phi_A/\Phi\ge1-2C_2/A^2-C_4/A^4\ge1/4.                 \tag{21}
\]
The source is smooth, even, and has all Gaussian moments; its
double-exponential tail remains of the same type. Its integral is
unchanged. Choose \(A\) outside the discrete zero set of \(H(0,\cdot)\).
Under the same RH assumption, \(F_A\) has only real zeros and exact
added double zeros at \(\pm A\). Real-zero heat preservation and the
local splitting law give all-real simple slices for every \(t>0\).
The double pair yields nonreal zeros just below zero, so the threshold
is exactly zero.

Writing \(s=1/2+ix/2\), its completed function is
\[
 8F_A(x)=\xi(s)B_A(s),\qquad
 B_A(s)=[1+4(s-1/2)^2/A^2]^2 .
\]
The function \(D_A(s)=\zeta(s)B_A(s)\) has the same displayed gamma
factor, conductor one and functional equation; its pole at one is
still simple, with residue \((1+A^{-2})^2\). These statements do not
make it a degree-one member of a class requiring a Dirichlet series.
Indeed \(D_A(\sigma)\sim16\sigma^4/A^4\), whereas any ordinary
Dirichlet series absolutely convergent in a right half-plane tends
to its first coefficient. It also fails nonnegative logarithmic
coefficients directly:
\[
 -D_A'/D_A(\sigma)
 =-\zeta'/\zeta(\sigma)
   -\frac{16(\sigma-1/2)}{A^2+4(\sigma-1/2)^2}<0
\]
for sufficiently large real \(\sigma\). The first term decays
exponentially and the subtracted term is asymptotic to \(4/\sigma\).

This control has an isolated added double pair rather than a periodic
Euler-factor lattice. It screens the named source and completion
premises, and fails the arithmetic premises explicitly. It supplies
no counterexample with zeta's unchanged coefficients. The threshold
on \(A\) is analytical in terms of the finite constants \(C_2,C_4\);
no numerical event height is asserted.

## 7. A known stronger input that detects multiplicity

The weak Mertens estimate
\[
 \int_1^X\frac{M(x)^2}{x^2}\,dx\ll\log X,\qquad
 M(x)=\sum_{n\le x}\mu(n),                                 \tag{22}
\]
implies RH and simplicity; see [Ng, introduction, equation (8)](https://arxiv.org/pdf/math/0310381).
It is unproved and is **not** imported here as a consequence of RH.
Bounds on negative moments of \(\zeta'(\rho)\) over every zero already
presuppose simplicity; Ng explicitly identifies this dependency.

For the relevant implication, let \(f(y)=e^{-y/2}M(e^y)\). From (22),
\(\int_0^Y|f|^2\ll1+Y\), whence
\(\int_0^\infty|f|^2e^{-\epsilon y}dy\ll\epsilon^{-1}\).
Cauchy–Schwarz gives
\[
 \left|\int_0^\infty f(y)e^{-(\epsilon+i\gamma)y}dy\right|
 \ll\epsilon^{-1}\quad(0<\epsilon\le1).
\]
The integral is holomorphic for \(\Re z>0\) and equals
\(1/[(z+1/2)\zeta(z+1/2)]\) by continuation from its initial convergence
half-plane. It rules out a pole there, and its boundary bound rules
out order \(m\ge2\), which would grow as \(\epsilon^{-m}\).
This is a benchmark for the missing strength of the arithmetic input,
not a new research milestone or a derived bound.

## 8. Relation to the contour consumer and decision

For an adjacent pair \(u<v\) born at an ordinary double event, the
known root dynamics give, with \(Y=(v-u)^2\),
\[
 Y'=8-4YP,\qquad
 P=\sum_{r\notin\{u,v\}}\frac1{(u-r)(v-r)}>0 .
\]
The difference series is absolutely convergent. The local limit
\(P\to S=\sum_{r\ne a}m_r/(a-r)^2\) from Note 01 yields
\(Y=8t-16St^2+o(t^2)\) and
\[
 Y(t)=8\int_0^t\exp\left(-4\int_s^tP(r)\,dr\right)ds>0 .
\]
These are compatible with an endpoint double event. They do not
force a later collision. The dynamics are already present in
[Polymath, Proposition 3.1](https://arxiv.org/html/1904.12438v2)
and [Rodgers–Tao, Lemma 12(i)](https://arxiv.org/pdf/1801.05914).
No novelty is claimed for this identity. In particular the inherited
large-time spatial cosine approximation must not be differentiated
in heat time without a uniform derivative estimate.

This continuation closes the estimating strategy **apply only the
global RH Chebyshev-error envelope (2) after the exact single
partial-summation transport (4)**. Its explicit payment grows as
\(\gamma\log^2\gamma\) at microscopic bandwidth, even after the exact
main/pole cancellation. The precise envelope-only norm has the same
order, and the exact endpoint control satisfies the same input bound.
It does not close signed correlations using unchanged prime support,
constraints linking frequencies, justified zero deflation, or other
kernel estimates.

Equation (19) supplies a genuine arithmetic rejection of the finite
control class, but not the required theta inequality. To advance
RHS-02, one must derive a bound for the unchanged zeta data which
conflicts with an actual hypothetical multiple zero; neither
relabeling (12) nor rejecting an unrelated factor supplies it.
There is still no independently justified cap surplus for RHS-03,
nor a new excluded height or multiplicity class for RHS-04.
The [progress register](../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md)
retains those open gates. No numerical scan or manuscript is warranted
by these findings.
