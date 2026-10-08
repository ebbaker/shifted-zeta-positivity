# The optimal exponent, its spectral edge, and logarithmic savings

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed and are not inferred.
Status: new analytic deductions conditional on the local fixed-probe
theorem and explicit formula, with a proof supplied below. This is an
internal same-model investigation, not independent specialist refereeing.
The abstract countermodel is not a statement about actual zeta zeros.

## 1. Inputs and scope

Use the fixed response, plus-exponent transform, and unnormalized variance
from the [prime-variance manuscript](../../prime-variance-exponents/manuscript.tex):

\[
G(z)=\int g(v)e^{zv}\,dv,\qquad
V_g(x)=\sqrt{x}\,p_g(\log x),\qquad
\mathcal V_g(X)=\int_X^{2X}|V_g(x)|^2\,dx.
\]

The inputs are its fixed-exponent theorem, noncancellation lemma,
sixth-power decay lemma, and complete linear explicit formula. In
particular, for sufficiently large real \(y\),

\[
p_g(y)=\sum_\rho a_\rho e^{(\rho-1/2)y}+r_0(y),\qquad
a_\rho=-m_\rho G(1/2-\rho),\qquad
\sum_\rho|a_\rho|<\infty,\qquad r_0(y)=O_g(e^{-5y/2}).
\tag{1}
\]

Zeros are distinct and their multiplicities are included in \(a_\rho\).
If \(0<\Re\rho-1/2<1/2\), then \(a_\rho\ne0\).
All variance estimates below concern **every sufficiently large real**
\(X\), not just a selected sequence.

The locally proved optimal-exponent identity is

\[
D:=\delta_*=2\sup_\rho(\Re\rho-1/2),\qquad
\mathcal V_g(X)=O(X^{2+D}).
\tag{2}
\]

The infimum defining \(D\) is an attained *admissible variance exponent*.
This does not assert that any zero attains the supremum of its real part.
For the questions below assume \(0<D<1\), and put \(\alpha=D/2\).
Thus all zeros satisfy \(\Re\rho-1/2\le\alpha\), but the boundary
\(\Re\rho=1/2+\alpha\) may contain no zeros.

## 2. Exact little-o criterion at the edge

**Proposition 1.** More generally, suppose \(0<D<1\) is any admissible
strip exponent. The following are equivalent:

1. \(\mathcal V_g(X)=o(X^{2+D})\).
2. No zeta zero has \(\Re\rho=(1+D)/2\).

The proposition does not require that \(D\) be the optimal exponent.
By functional-equation symmetry, item 2 also excludes the opposite strip
boundary. At \(D=0\), the present proof of the converse cannot simply be
reused: the local noncancellation theorem has deliberately been invoked
only for off-critical zeros.

**Proof.** Define

\[
q(y)=e^{-\alpha y}p_g(y),\qquad \ell=\log2.
\]

The exact change of variables \(x=e^y\) gives

\[
E(Y):=e^{-(2+D)Y}\mathcal V_g(e^Y)
=\int_0^\ell e^{(2+D)u}|q(Y+u)|^2\,du.
\tag{3}
\]

Write the edge series as

\[
F(y)=\sum_{\Re\rho-1/2=\alpha}a_\rho e^{i(\Im\rho)y}.
\tag{4}
\]

Absolute summability in (1) and dominated convergence show

\[
q(y)=F(y)+o(1)\qquad(y\longrightarrow\infty).
\tag{5}
\]

The little-o here is the usual scalar limit and hence is uniform for all
arguments beyond a sufficiently large threshold. Indeed each nonedge
term has the additional factor
\(e^{-(\alpha-\Re\rho+1/2)y}\to0\), and the sum of its coefficient
majorants is finite. The normalized trivial-zero remainder also vanishes.
If there are no edge zeros, (3)–(5) immediately imply \(E(Y)\to0\).

Conversely suppose \(E(Y)\to0\). Since the weight in (3) is bounded
above and below by positive constants, the unweighted local square
integrals of \(q\) tend to zero. Partitioning a long interval into pieces
of length \(\ell\) gives, for any fixed starting point \(Y_0\) in the
range of (1),

\[
\frac1T\int_{Y_0}^{Y_0+T}|q(y)|^2\,dy\longrightarrow0.
\tag{6}
\]

Initial and final partial intervals are harmless because (1) makes
\(q\) bounded there and on the tail. Cauchy–Schwarz therefore implies
that the mean of \(q(y)e^{-i\gamma_0y}\) tends to zero for every fixed
real \(\gamma_0\).

If \(\rho_0=1/2+\alpha+i\gamma_0\) were an edge zero, termwise
averaging in (1), justified by the summable majorant, instead gives

\[
\lim_{T\to\infty}\frac1T
\int_{Y_0}^{Y_0+T}q(y)e^{-i\gamma_0y}\,dy=a_{\rho_0}\ne0.
\tag{7}
\]

Every term with a positive real-part gap has mean zero; every other edge
frequency has oscillatory mean zero. Coincident roots were already
combined using their positive multiplicity. This contradicts (6), and
proves the proposition. \(\square\)

**A stronger averaged identity.** The same argument, now applied to the
absolutely convergent double Fourier series \(|F|^2\), yields

\[
\lim_{T\to\infty}\frac1T\int_{Y_0}^{Y_0+T}E(Y)\,dY
=K_D\sum_{\Re\rho=(1+D)/2}|a_\rho|^2,
\qquad
K_D=\frac{2^{2+D}-1}{2+D}.
\tag{8}
\]

Thus an edge zero forces a positive normalized mean and a positive
limsup. No uniform positive lower bound for every large \(X\) is
asserted here.

## 3. What this does and does not imply for exponent descent

If \(D=\delta_*\) and its zero supremum is attained, Proposition 1 rules
out every little-o improvement at that endpoint. In particular, any
proved estimate

\[
\mathcal V_g(X)\ll\frac{X^{2+D}}{(\log X)^A},\qquad A>0,
\tag{9}
\]

would rule out edge zeros. It would not, by itself, rule out zeros whose
real parts approach the edge at heights tending to infinity.

If \(D=\delta_*>0\) and there are no edge zeros, Proposition 1 gives
\(o(X^{2+D})\) automatically, while the definition of \(D\) still
forbids every bound \(O(X^{2+D-\eta})\) with \(\eta>0\).
There is no contradiction: an optimal big-O power can coexist with
little-o at that same power.

This observation pinpoints the missing quantifier. Excluding each zero
*on* a boundary is weaker than producing a single positive gap below that
boundary for *all* zeros.

The manuscript's fixed-exponent theorem and the signed-Mellin endpoint
argument remove \(X^{o(1)}\) losses **at the same power**. They do not
turn (9), even for every fixed \(A\), into a smaller power.

## 4. An abstract countermodel with all logarithmic savings

**Proposition 2.** For every \(0<D<1\), there is a real response
\(p_D\) made from an absolutely summable, conjugation- and
reflection-symmetric spectrum, using the same fixed probe \(G\), such
that its associated variance has optimal exponent exactly \(D\), has
no spectral point on the edge, and satisfies

\[
\mathcal W_D(X)\ll_D
X^{2+D}\exp\{-c_D(\log X)^{2/3}\}.
\tag{10}
\]

Consequently \(\mathcal W_D(X)=O_{D,A}(X^{2+D}/(\log X)^A)\)
for every fixed \(A>0\), but no positive power saving is possible.

**Construction and proof.** Put \(\alpha=D/2\) and for integers
\(n\ge1\) set

\[
\lambda_n=\alpha\left(1-\frac1{n+1}\right),\qquad
\gamma_n=e^{n^2},\qquad
\mathcal S_D=\{\pm\lambda_n\pm i\gamma_n:n\ge1\}.
\tag{11}
\]

All four signs are included independently, and all points have
\(|\Re s|<\alpha\). Their real-part supremum is \(\alpha\), attained
only as the height tends to infinity. Define, for real \(y\ge0\),

\[
p_D(y)=\sum_{s\in\mathcal S_D}b_s e^{sy},\qquad b_s=-G(-s),
\quad W_D(x)=\sqrt{x}\,p_D(\log x),\quad
\mathcal W_D(X)=\int_X^{2X}|W_D(x)|^2\,dx.
\tag{12}
\]

Reality of \(g\) gives conjugate coefficients at conjugate spectral
points, so \(p_D\) is real. The same noncancellation lemma, together
with oddness of \(G\), gives \(b_s\ne0\) at every point in (11).
Uniform sixth-power decay gives

\[
|b_s|\le C_g e^{-6n^2}\quad
(s\in\{\pm\lambda_n\pm i\gamma_n\}).
\tag{13}
\]

The series is therefore absolutely and locally uniformly convergent for
real \(y\ge0\). Both positive and negative real-part terms satisfy

\[
e^{-\alpha y}|p_D(y)|
\le C_g\sum_{n\ge1}
\exp\left\{-6n^2-\frac{\alpha y}{n+1}\right\}
\le C_{g,D}e^{-c_Dy^{2/3}}.
\tag{14}
\]

For the final inequality use \(n+1\le2n\), retain \(e^{-3n^2}\)
as a summable factor, and minimize
\(3n^2+\alpha y/(2n)\) over positive real \(n\). Its minimum is a
positive \(D\)-dependent constant times \(y^{2/3}\). Equation (3)
applied to this model proves (10), after adjusting the positive constant.

It remains to check that cancellation cannot conceal a smaller power.
For \(\Re z>\alpha\), termwise integration gives

\[
P_D(z)=\int_0^\infty e^{-zy}p_D(y)\,dy
=\sum_{s\in\mathcal S_D}\frac{b_s}{z-s}.
\tag{15}
\]

The right side is meromorphic on the entire plane. Indeed the spectral
points have no finite accumulation; on each compact set the sufficiently
large-height denominators are bounded below by a fixed multiple of
\(\gamma_n\), and (13) gives normal convergence. Each spectral point
is a genuine simple pole with residue \(b_s\ne0\).

Suppose \(\mathcal W_D(X)=O(X^{2+d})\) for some \(d<D\).
The manuscript's dyadic-shell Cauchy–Schwarz argument, which uses only
the relation between \(W_D\) and \(p_D\), makes the integral in (15)
holomorphic for \(\Re z>d/2\). Choose \(n\) large enough that
\(\lambda_n>d/2\). Uniqueness of meromorphic continuation would then
make the nonzero pole at \(\lambda_n+i\gamma_n\) removable, a
contradiction. Thus the optimal exponent is exactly \(D\). \(\square\)

**Limitation.** This is a spectral countermodel using the exact fixed
probe, noncancellation, absolute summability, and the two elementary zero
symmetries. It is not the actual prime response, does not assert an Euler
product, does not reproduce the full zeta zero counting asymptotic, and
is not a counterexample to RH or to an arithmetic implication
quasi-RH \(\Rightarrow\) RH. It disproves only an inference from these
analytic properties and arbitrary fixed logarithmic savings alone.

## 5. A quantitative tail formulation

The place where a rate enters can be made explicit. For an admissible
\(\alpha=D/2\), write the nonnegative gaps as

\[
\varepsilon_\rho=\alpha-\Re\rho+1/2,\qquad
A(u)=\sum_{0\le\varepsilon_\rho\le u}|a_\rho|.
\tag{16}
\]

Then the nontrivial-zero part of the normalized response obeys

\[
|q(y)|\le\sum_\rho|a_\rho|e^{-\varepsilon_\rho y}
+O_g(e^{-(5/2+\alpha)y}).
\tag{17}
\]

If there is no edge mass, \(A(0)=0\), and \(A(u)\to0\) as
\(u\downarrow0\); this recovers qualitative little-o. If more strongly
\(A(u)\le C u^r\) for small \(u>0\), Stieltjes integration by parts
in (17) gives

\[
|q(y)|=O(y^{-r}),\qquad
\mathcal V_g(X)=O\left(X^{2+D}(\log X)^{-2r}\right).
\tag{18}
\]

For example, the relevant Laplace bound is
\(\int e^{-yu}\,dA(u)=y\int_0^\infty e^{-yu}A(u)\,du\),
and the latter is \(O(y^{-r})\); the region away from zero is
exponentially small. This is a sufficient condition, not a necessary
description of cancellation in the actual response.

Polynomial or even very fast decay of *weighted mass near the edge* is
still different from an empty interval of gaps. A true power improvement
requires a positive zero-free gap: for some \(\eta>0\), every zero
must satisfy \(\Re\rho-1/2\le\alpha-\eta\).

## 6. Consequence for the next research target

There are two logically distinct routes worth keeping separate.

- A strict exponent improvement valid at the attained admissible exponent
  \(D=\delta_*\in(0,1)\) would immediately contradict its optimality.
  No edge-attainment hypothesis is needed. This is sufficient for
  quasi-RH to imply RH, but such a theorem remains unproved.
- A little-o or logarithmic improvement at \(D=\delta_*\) only removes
  edge zeros. To turn it into RH one additionally needs an arithmetic
  theorem excluding positive nonattained suprema, or a uniform positive
  gap below any positive candidate edge. Neither is supplied by the
  existing variance equivalence or exact convolution identities.

A proposed descent inequality should therefore be tested on a sequence
of hypothetical off-critical zeros approaching the candidate edge at
unbounded heights. Arguments that merely annihilate a pole exactly on
the boundary have not yet addressed that case.

## 7. Internal proof-check record

The deductions above were checked for the exact factor \(2+D\) in the
variance change of variables, multiplicities, the noncancellation range,
dominated convergence, the difference between an attained admissible
power and an attained spectral supremum, normal convergence of the model
Laplace series, and the all-real-\(X\) quantifier. No numerical experiment,
new zeta zero-free strip, or actual-prime exponent improvement is claimed.
