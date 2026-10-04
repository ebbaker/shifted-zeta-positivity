# Signed Mellin continuation and the low-frequency obligation

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the serving variant and
configured reasoning effort are not exposed and are not inferred.
Separate agents supplied derivations and fresh internal checks using the
inherited configuration. These are not independent specialist refereeing.

This continues the [initial investigation](INITIAL_DELTA_INVESTIGATION_20261004.md).
Keep the exact fixed probe, support constants A=e^(-1/4), B=e^(1/4),
and plus-exponent transform G from the [manuscript](../manuscript.tex).
All global estimates below quantify over every sufficiently large real X.
No new fixed global exponent below one is proved.

## Results of this continuation

Three statements sharpen the unresolved arithmetic target.

1. The retained signed response can be restricted to Mellin frequencies
   |t|<=X^(1/12)log X with an o(X) shell-norm error. The exact signed
   central quadratic kernel is displayed below. The proof bounds the
   outer frequencies without cancellation hypotheses.
2. Summing the cofactors before taking absolute values gives an exact
   Mertens-function integral, including the hard-cutoff boundary. Its
   lattice kernel has a nonzero logarithmic moment, the same constant
   that occurs in the balanced Vaughan continuum. Known Mertens bounds
   still give only subpower savings; they do not close the target.
3. For this exact response, a global estimate X^(3-kappa)L(X),
   L=X^(o(1)), 0<kappa<=1, would recover the endpoint exponent
   X^(3-kappa), even when L is unbounded. Separately, the fully uniform
   polynomial Type II hypothesis proposed in the source audit already
   implies a fixed zero-free strip from its t=0 slice alone.

The first two are unconditional reductions. The third consists of
conditional implications with proofs, not of a verified arithmetic input.
The key remaining task is a signed central estimate rather than an
absolute bound for individual Möbius factors.

## 1. A finite polynomial that keeps the complete arithmetic caps

Set D=X^(9/10), and use the retained response R_X from the initial note.
Let I_X contain every integer in [AX,2BX], including composites and prime
powers. Define real coefficients and a finite Dirichlet polynomial by

\[
a_X(n)=-\sum_{\substack{d\mid n\\d>D}}\mu(d)\log d
\quad(n\in I_X),\qquad
\mathcal A_X(s)=\sum_{n\in I_X}a_X(n)n^{-s}.
\tag{1}
\]

For all x in [X,2X], exactly

\[
R_X(x)=\sum_{n\in I_X}a_X(n)w(n/x).
\tag{2}
\]

Endpoint inclusion is harmless because w vanishes at both support ends.
Every divisor and cofactor condition is still present. In particular the
polynomial is not replaced by an unrestricted product of a divisor
polynomial and a cofactor polynomial: the cap AX<=dk<=2BX couples them.

Put

\[
F(s)=\int_A^B w(v)v^{s-1}\,dv=G(1/2-s).
\tag{3}
\]

For y real the finite logarithmic response is

\[
p_X(y)=\sum_{n\in I_X}\frac{a_X(n)}{\sqrt n}g(y-\log n).
\]

It is compactly supported. Fourier inversion, with the convention
\(\widehat f(t)=\int f(y)e^{-ity}dy\), gives

\[
p_X(y)=\frac1{2\pi}\int_{\mathbb R}
G(-it)\mathcal A_X(1/2+it)e^{ity}\,dt,
\qquad R_X(x)=\sqrt x\,p_X(\log x)
\quad(X\le x\le2X).
\tag{4}
\]

This is inversion of a finite arithmetic sum, not a contour shift across
zeta zeros. The integral converges absolutely: the polynomial is bounded
in t for fixed X and G(-it)=O_g((1+|t|)^(-6)).

## 2. The outer Mellin frequencies have subquadratic energy

We give an elementary mean-square proof to keep the input explicit.
For \(b_n=a_X(n)/\sqrt n\),

\[
S_X:=\sum_{n\in I_X}|b_n|^2\ll (\log X)^5.
\tag{5}
\]

Indeed |a_X(n)|<=d_2(n)log n. At prime powers,
(j+1)^2<=binomial(j+3,3), hence d_2(n)^2<=d_4(n) multiplicatively.
Counting quadruples gives
\(\sum_{n\le N}d_4(n)\le N(1+\log N)^3\).
Since n is comparable to X throughout I_X, (5) follows. No Möbius
cancellation is used here.

For any real interval J of length H>0,

\[
\int_J|\mathcal A_X(1/2+it)|^2\,dt
\ll (H+X)S_X.
\tag{6}
\]

To prove (6), let c be its center and majorize its indicator by
\(e^{1/4}\exp(-(t-c)^2/H^2)\). Integrating the expanded polynomial
against this Gaussian gives a constant times H and a matrix whose
absolute entries are
\(\exp[-H^2\log^2(n/m)/4]\).
For n,m<=N=floor(2BX),
\(|\log(n/m)|\ge|n-m|/N\).
Each row sum is at most

\[
1+2\sum_{j\ge1}e^{-H^2j^2/(4N^2)}\ll1+N/H.
\]

The inequality 2|b_nb_m|<=|b_n|^2+|b_m|^2 bounds the quadratic form
by this row sum times S_X. This proves (6), without a logarithmic loss
from an absolute Hilbert-kernel estimate.

For T>=1, define p_(X,T) by restricting (4) to |t|<=T, and set
R_(X,T)(x)=sqrt(x)p_(X,T)(log x). The complementary part satisfies

\[
\boxed{\quad
\|R_X-R_{X,T}\|_{L^2(X,2X)}^2
\ll_g X^2(\log X)^5\big(T^{-11}+XT^{-12}\big).
\quad}
\tag{7}
\]

For the proof, Plancherel on the whole y-axis bounds the squared norm of
the complementary p by
\((2\pi)^{-1}\int_{|t|>T}|G(-it)\mathcal A_X(1/2+it)|^2dt\).
On each band 2^jT<|t|<=2^(j+1)T, (6) bounds the polynomial mean
square by O((2^jT+X)S_X), while |G(-it)|^2=O_g((2^jT)^(-12)).
Summing the two geometric series gives
O_g(S_X(T^(-11)+XT^(-12))). Finally dx=e^y dy and
|R(x)|^2=x|p(log x)|^2, so the shell energy has weight x^2<=4X^2.
This proves (7).

In particular, with

\[
T_X=X^{1/12}\log X,
\qquad
\|R_X-R_{X,T_X}\|_2\ll_g X(\log X)^{-7/2}=o(X).
\tag{8}
\]

The term from T^(-11) in (7) is smaller at this choice. More generally
T=X^(1/12)(log X)^b gives o(X) error for b>5/12.
Alternatively T=X^(1/10) gives squared error
O_g(X^(9/5)(log X)^5), a power saving relative to X^2.
These are asymptotic statements with probe-dependent constants, not
explicit finite-range numerical certificates.

Combining (8) with the earlier divisor-elimination bound gives

\[
\boxed{\quad
\|V_g-R_{X,T_X}\|_2
\ll_g X^{9/10}\log X+X(\log X)^{-7/2}=o(X).
\quad}
\tag{9}
\]

Consequently the original response, the complete retained cofactor sum,
and this central Mellin response have the same admissible exponents
2+delta for every delta>=0, including delta=0. Their normalized shell
norms differ by o(1). The high-frequency proof applies to any coefficients
with the bound in (5); it does not by itself add an arithmetic power saving.

There is also a small-frequency refinement using the oddness of g. For
0<tau<=1, let
\(g_\tau(v)=(2\pi)^{-1}\int_{-\tau}^{\tau}G(-it)e^{itv}dt\).
G(-it) is purely imaginary and odd, with |G(-it)|=O_g(|t|). The cosine
part integrates to zero, and |sin(tv)|<=|tv| gives
|g_tau(v)|=O_g(|v|tau^3). On the complete shell caps,
|log x-log n|<=log 2+1/4. Cauchy-Schwarz and (5) therefore give

\[
\|R_{X,\tau}\|_2^2\ll_g X^3S_X\tau^6
\ll_g X^3(\log X)^5\tau^6.
\tag{9a}
\]

At tau=X^(-1/6)(log X)^(-b), b>5/6, this is o(X^2).
The convenient choice tau_X=X^(-1/5) instead gives
O_g(X^(9/5)(log X)^5). Hence the annular response obtained by keeping
tau_X<|t|<=T_X also differs from V_g by o(X) in shell norm.
Every fixed nonzero frequency eventually belongs to this annulus; this
removes only a shrinking neighborhood of zero.

## 3. The exact signed central kernel

Let ell=log 2 and

\[
Z_X(t)=X^{it}\mathcal A_X(1/2+it),\qquad
J(q)=\int_0^\ell e^{2u+iqu}\,du
=\frac{2^{2+iq}-1}{2+iq}.
\]

The remaining energy is exactly

\[
Q_T(X):=\|R_{X,T}\|_2^2
=\frac{X^2}{4\pi^2}\int_{-T}^T\int_{-T}^T
G(-it)\overline{G(-iv)}Z_X(t)\overline{Z_X(v)}J(t-v)\,dt\,dv.
\tag{10}
\]

The kernel is positive semidefinite as a quadratic form; it is not
pointwise nonnegative. Conjugate symmetry makes R_(X,T) real, and all
cross-frequency phases and all Möbius signs in (1) remain in (10).
The selected unproved inequality can now be written, for one fixed
0<kappa<=1,

\[
\boxed{\quad Q_{T_X}(X)\ll X^{3-\kappa}L(X),
\qquad L(X)=X^{o(1)}.\quad}
\tag{11}
\]

It is a finite, explicit signed central quadratic form on each shell.
G(0)=0 itself removes the single frequency t=0, not a neighborhood of it;
no neighborhood is deleted from (10). Bound (9a) additionally permits
replacing both integration bands by
\(\Omega_X=\{t:X^{-1/5}<|t|\le T_X\}\), with o(X) norm error.
The corresponding Q_(Omega_X)(X) is an equally valid version of (11).
This shrinking deletion supplies no bound at any fixed nonzero low
frequency. Moreover the Type II hypothesis
discussed below concerns individual factors on Re s=1, whereas (10)
concerns a capped convolution on Re s=1/2. They are different conditions.

## 4. Summing the cofactor channels before taking a bound

Write M(t)=sum_(n<=t)mu(n), and L(y)=sum_(k>=1)w(k/y).
For any fixed real D>=1 with D<Bx,

\[
R_{X,D}(x)=-\sum_{d>D}\mu(d)\log d\,L(x/d).
\]

Abel summation gives the exact signed formula

\[
\boxed{\begin{aligned}
R_{X,D}(x)={}&M(D)\log D\,L(x/D)\\
&+\int_{1/B}^{x/D}M(x/y)
\left[\frac{L(y)}y-\log(x/y)L'(y)\right]dy.
\end{aligned}}
\tag{12}
\]

M(D) means the sum up to floor(D); d>D is strict, including when D is
integral. To see the boundary sign, apply Stieltjes integration by parts
to f(t)=log t L(x/t) on (D,infinity). The upper boundary vanishes because
L(x/t)=0 for t>=Bx. The negative of the integral of f against dM equals
M(D)f(D)+integral_D^infinity M(t)f'(t)dt. Substitute y=x/t.
L and L' vanish at 1/B, so no additional cap term appears.

The lattice lemma proves L(y)=O_g(y^(-5)). Also L'(y)=O_g(y^(-5)):
put q(v)=v w'(v), so integral q=-integral w=0 and
D^5q=vD^6w+5D^5w is a finite measure, including its endpoint atoms.
The fifth-order Poisson estimate gives sum_k q(k/y)=O_g(y^(-4));
differentiating the locally finite lattice sum gives
L'(y)=-y^(-1)sum_k q(k/y).
Thus both

\[
\int_{1/B}^\infty\frac{|L(y)|}{y^2}dy<\infty,
\qquad
\int_{1/B}^\infty\frac{|L'(y)|}{y}dy<\infty.
\tag{13}
\]

If |M(t)|<=C t epsilon_D for D<=t<=Bx, (12)-(13) imply uniformly on
the shell, when D<=X,

\[
|R_{X,D}(x)|\ll_g C\epsilon_D x\log(2x).
\tag{14}
\]

The cutoff boundary is bounded by
O_g(C epsilon_D x(D/x)^6log D). No harmonic cofactor loss occurs because
the lattice sum is formed before applying an absolute Mertens envelope.

For a conditional polynomial bound M(t)=O(t^(1-eta)), 0<eta<=1/2,
the same argument, with the y^eta weights retained, gives

\[
|R_{X,D}(x)|\ll_{g,\eta,C_\eta} x^{1-\eta}\log(2x),
\qquad \|R_{X,D}\|_2^2\ll_{g,\eta,C_\eta} X^{3-2\eta}(\log X)^2.
\tag{15}
\]

Here C_eta is the assumed Mertens-bound constant. The relevant integrals
converge since L,L'=O(y^(-5)); the boundary is
O_g(x^(1-eta)(D/x)^(6-eta)log D). At D=X^(9/10), the discarded
sector is below X^2, so (15) would imply delta<=1-2eta, with the exact
endpoint recovered in Section 5. The polynomial Mertens bound itself
would already imply a fixed zero-free half-plane by the holomorphic
Dirichlet integral for 1/zeta. It is not an available unconditional input.

The lattice multiplier also explains the nonzero continuum:

\[
\int_0^\infty L(y)y^{-s-1}dy=\zeta(s)F(s)
\quad(\Re s>1),
\tag{16}
\]

with holomorphic continuation to Re s>-5 from the left-hand integral.
At s=1 the preparation zero F(1)=0 cancels the pole of zeta. Therefore

\[
\int_{1/B}^\infty\frac{L(y)}{y^2}dy
=F'(1)=c_w=-\frac{H(-1/2)}{2\sqrt\nu}<0,
\qquad
\int_{1/B}^\infty\frac{L'(y)}y dy=c_w.
\tag{17}
\]

The second identity follows by integration by parts with zero endpoint
terms. It would be wrong to obtain zero in the first identity by
integrating each lattice sample separately and then summing: at s=1
the absolute harmonic sum needed for that interchange diverges.
The same c_w is required by the balanced Vaughan reduction.

A current primary-source check found Lee and Leong's
[9 September 2026 version, Theorem 1.1](https://arxiv.org/pdf/2208.06141v5),
which supplies unconditional Mertens bounds on the scale
t log t exp(-c Phi(t)), where
Phi(t)=(log t)^(3/5)(loglog t)^(-1/5) and c>0.
For D=X^(9/10), an eventual decreasing envelope in (14) gives only
O_g(X^3(log X)^4 exp(-c'Phi(X))) energy for some c'>0.
This is another subpower baseline, not an improvement over the existing
Johnston-Yang prime-response envelope and not a fixed saving in exponent.
Its role here is to test the newly displayed signed Mertens representation.

## 5. Subpower losses can be removed at the exponent endpoint

Let \(\mathcal T_X\) be any of R_X, R_(X,T_X), the annular response, or the correctly centered balanced
Vaughan response. The proved reductions give
\(\|V_g-\mathcal T_X\|_2=O_g(X)\), with o(X) for the cofactor and frequency responses.
Suppose for one 0<kappa<=1,

\[
\|\mathcal T_X\|_2^2\ll X^{3-\kappa}L(X),\qquad L(X)=X^{o(1)}.
\tag{18}
\]

For every fixed delta with 1-kappa<delta<=1, the triangle inequality
and the subpower condition give Vcal_g(X)=O(X^(2+delta)).
The manuscript's fixed-probe theorem gives the corresponding closed
zero strip for each such delta. Intersecting these strips yields
Re rho<=1-kappa/2 for every nontrivial zero. Its converse then gives

\[
\boxed{\quad
\mathcal V_g(X)=O(X^{3-\kappa}),
\qquad \|\mathcal T_X\|_2^2=O(X^{3-\kappa}).\quad}
\tag{19}
\]

The second estimate follows from the norm comparison again. At kappa=1,
this yields RH and the exact quadratic bound. Constants and thresholds
need not be uniform as delta approaches 1-kappa. The conclusion is an
endpoint admissible bound, not a claim that this exponent is optimal.

This strengthens the initial note's elementary strict-exponent transfer:
an unbounded subpower loss does not obstruct endpoint recovery for this
exact fixed arithmetic response once its proved spectral equivalence is
used. It says nothing about arbitrary coefficients and proves no kappa.

## 6. The proposed uniform Type II input already contains a fixed strip

Here the quantifier matters. Consider the all-real-block version of the
candidate in the [source audit](BILINEAR_INPUT_SOURCE_AUDIT_20261004.md):
for some fixed omega>0 and all sufficiently large real X, uniformly over
every required real dyadic block and its terminal partial blocks,

\[
\sup_{|t|\le X^{1/4+\omega}}
\left|\sum_{\substack{M<m\le2M\\m>U}}
\frac{\mu(m)}{m^{1+it}}\right|\ll X^{-\omega/3},
\qquad U=X^{11/24}.
\tag{20}
\]

Assume in particular that the central full block M=sqrt(X) is included.
It is inside the permitted balanced range, and m>U is then redundant.
Taking t=0 and X=Y^2 gives, for every sufficiently large real Y,

\[
\Delta(Y):=\sum_{Y<n\le2Y}\frac{\mu(n)}n
\ll Y^{-\eta},\qquad \eta=2\omega/3.
\tag{21}
\]

This alone implies that zeta has no zero with Re s>1-eta. We give a
proof that does not assume ordinary convergence of sum mu(n)/n.
For Re z>0, absolute interchange gives

\[
\int_0^\infty\Delta(Y)Y^{-z-1}dY
=\frac{2^z-1}{z}\frac1{\zeta(1+z)}.
\tag{22}
\]

For each n the integration interval is n/2<=Y<n. This gives its factor
n^(-z)(2^z-1)/z. The integrand is zero for Y<1/2 and bounded on finite
intervals. Assumption (21) extends the left-hand side holomorphically to
Re z>-eta. The entire multiplier (2^z-1)/z, with value log 2 at zero,
has all its zeros on Re z=0. At z=rho-1 for a nontrivial zeta zero,
its real part is negative, so it does not cancel the pole of 1/zeta,
whatever the zero multiplicity. Uniqueness of meromorphic continuation
excludes Re rho>1-eta. The usual zero-free line at one and Euler product
complete the stated half-plane.

Thus (20), even at t=0, would imply the exact variance exponent

\[
\delta=1-2\eta=1-4\omega/3
\tag{23}
\]

for the small positive omega allowed by the audited Type II lemma.
This is a stronger strip than the one obtained by applying that lemma's
mean-square saving W^(-3/10) at W=X^omega, which would correspond to
kappa=3omega/10, up to logarithms. This comparison is a diagnostic of
the proposed hypothesis, not an unconditional claim or a conclusion
attributed to the cited authors. The cited input is
[Lemma 3.5(iv), equations (3.6) and (3.8), pp. 30-31](https://arxiv.org/pdf/2411.05770v2).

If only a single predetermined grid of full dyadic blocks is assumed,
the all-real-Y transform argument above does not follow from their t=0
totals. Bounds for terminal partial blocks, or an explicit all-real-block
quantifier, are needed. No missing quantifier is supplied by inference.
Conversely, deleting low frequencies changes the audited lemma to a
short-minus-long response and leaves the longer arithmetic response to
estimate; preparation does not remove it automatically.

## 7. Why a separated cofactor endpoint can be too strong

There is a precise spectral reason to retain the cofactor cross terms.
Put

\[
T_\mu(x)=\sum_{n\ge1}\mu(n)\log n\,w(n/x),\qquad
q_\mu(y)=e^{-y/2}T_\mu(e^y).
\]

Since D=X^(9/10)=o(X), the k=1 channel of R_X is -T_mu(x) on the
whole shell for all sufficiently large X: every active n>=AX exceeds D.
Initially for Re s>1/2, its true Laplace transform is

\[
\int_0^\infty q_\mu(y)e^{-sy}dy
=G(-s)\frac{\zeta'(1/2+s)}{\zeta(1/2+s)^2}.
\tag{24}
\]

The n=1 term is zero because log 1=0; for n>=2 the entire translated
probe lies above y=0 since log 2>1/4. Differentiating the absolutely
convergent reciprocal-zeta Dirichlet series therefore proves (24) with
no initial-cap correction.

Fix 1/2<theta<1. If the individual channel satisfied

\[
\int_X^{2X}|T_\mu(x)|^2dx=O(X^{1+2\theta}),
\tag{25}
\]

then there could be no nontrivial zeta zero with Re rho>=theta.
Strictly larger real parts are excluded by true Laplace holomorphy,
using the same dyadic Cauchy-Schwarz argument as in the manuscript.
For a boundary zero rho=theta+i gamma, that argument also bounds the
transform at s=rho-1/2+epsilon by O(1/epsilon) as epsilon decreases to
zero. Indeed the weighted contribution from each log-dyadic shell is
O(exp(-epsilon j log 2)), and their sum is O(1/epsilon).

However, a zero rho of multiplicity m makes zeta'/zeta^2 a pole of
order m+1>=2. The fixed-probe noncancellation theorem gives
G(1/2-rho)!=0 because theta>1/2. Thus (24) has magnitude asymptotic
to a positive constant times epsilon^(-(m+1)), a contradiction.
This boundary exclusion is not asserted at theta=1/2, where probe zeros
on the imaginary axis require separate consideration.

In contrast, the same energy exponent for the signed prime response
V_g corresponds to delta=2theta-1 and permits zeros on Re rho=theta.
The full cofactor multiplier explains the difference: with F from (3),
the exact meromorphic product is

\[
-F(s)\zeta(s)\frac{\zeta'(s)}{\zeta(s)^2}
=-F(s)\frac{\zeta'(s)}{\zeta(s)}.
\tag{26}
\]

The identity initially follows from the absolutely convergent full
convolution for Re s>1. At a multiplicity-m zero, multiplication by
zeta reduces the order m+1 pole to a simple pole. This is an exact
convolution and local meromorphic explanation; it does not claim an
unconditionally convergent zero expansion for the Möbius channels.
Nor is the full multiplier zeta substituted for a finite cofactor cutoff
or for the moving shell cutoff. The earlier norm comparisons remain
the valid transfer for R_X.

Thus a method demanding (25) separately for every cofactor imposes a
strict boundary exclusion beyond what the corresponding signed-response
bound needs. This is an obstruction to that sufficient method, not a
counterexample to the actual-prime target.

## 8. Research decision and verification scope

The direct envelope attempt (12)-(15) preserves the summed cofactor
structure but still demands Mertens cancellation at fixed power strength.
The proposed factorwise Type II hypothesis (20) is an even less economical
route in the sense that its low-frequency slice already supplies the
desired kind of all-height strip before the bilinear theorem is invoked.

The selected next analytic target is (11), or the analogous centered
balanced quadratic form, with actual arithmetic signs and all caps kept.
For the Mellin version the outer frequencies need no further hypothesis.
A useful next estimate should control this signed form directly, rather
than replacing it with a uniform absolute factor bound of already
zero-strip strength. The endpoint observation means a subpower loss is
acceptable at a first fixed-power milestone.

The [fresh internal review](../reviews/SIGNED_MELLIN_CONTINUATION_REVIEW_20261004.md)
records the checks of transform conventions, Gaussian mean square,
frequency exponents, hard-cutoff Abel boundary, derivative measures,
low-frequency quantifiers, and endpoint recovery. No numerical exponent
fit, new numerical certificate, manuscript revision, snapshot folder,
commit, or push is part of this continuation. No priority claim is made.
