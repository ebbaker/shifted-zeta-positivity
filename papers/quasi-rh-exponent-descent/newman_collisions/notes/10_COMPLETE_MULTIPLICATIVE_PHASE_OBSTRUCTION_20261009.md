# Complete multiplicative-phase obstruction for the signed collision vector

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model audits are internal checks, not independent validation.

This continues [Heat Note 8](8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md)
and the genuine-phase work in
[Heat Note 9](9_GENUINE_SIGNED_EDGE_CANCELLATION_AND_AVERAGED_PROBES_20261009.md).
The result below strengthens Note 8's independent-term phase obstruction:
even complete multiplicativity of a unit-modulus twist does not supply a
positive lower bound for the full signed value/derivative vector. All terms,
heat weights, amplitude derivatives, and derivative frequencies are retained.
The leading phase is fixed. The constructed twists need not arise from the
genuine height orbit and yield no collision of the heat function.

## 1. Exact vector and the scope of the relaxation

Use the same scaling and fixed-cutoff conventions as Note 8:

\[
1\le\kappa\le2,\qquad L=\kappa/t,\qquad
x=4\pi e^L,\qquad s=(1-ix)/2,\qquad
N=\left\lfloor\sqrt{e^L+t/16}\right\rfloor.
\tag{1}
\]

All limits below are uniform in \(\kappa\in[1,2]\) as \(t\downarrow0\).
Spatial derivatives hold time, the cutoff, and any twist fixed. Put
\(\alpha(s)=\alpha_r+i\alpha_i\), \(\alpha'(s)=u+iv\), and

\[
w_n=\exp\{t\log^2n/4-(1/2+t\alpha_r/2)\log n\},
\qquad \phi_n=\theta_t(x)+(x-t\alpha_i)\log n/2,
\]
\[
r_n=\frac2L\Re\{(\alpha(s)-\log n)(1+t\alpha'(s)/2)\},
\qquad c_n=\frac{tv\log n}{L}.
\tag{2}
\]

For the genuine fixed-cutoff approximation, these exact quantities give

\[
\mathcal V=
\left(F_{t,N}/2,\;2F_{t,N}'/L\right)
=\sum_{n\le N}w_n
(\cos\phi_n,\;r_n\sin\phi_n-c_n\cos\phi_n).
\tag{3}
\]

A completely multiplicative unit-modulus twist is a function
\(\chi:\mathbb N\to\mathbb C\) with \(\chi(1)=1\),
\(\chi(mn)=\chi(m)\chi(n)\), and \(|\chi(n)|=1\).
Define \(\psi_n=\phi_n+\arg\chi(n)\), interpreted modulo \(2\pi\), and

\[
\mathcal V_\chi=\sum_{n\le N}w_n
(\cos\psi_n,\;r_n\sin\psi_n-c_n\cos\psi_n).
\tag{4}
\]

Equivalently, multiply the first analytic term indexed by \(n\) by
\(\chi(n)\), and its reflected term by \(\overline{\chi(n)}\).
This preserves real symmetry. Holding the twist constant in a spatial
neighborhood preserves each exact local amplitude derivative and phase
frequency; thus (4) is also the scaled value/derivative vector of that
modified finite analytic approximation at the chosen point.

The heat factor \(e^{t\log^2n/4}\) is not replaced by a multiplicative
weight. In particular, its cross factor
\(e^{(t/2)\log m\log n}\) remains present when indices are multiplied.
Complete multiplicativity applies to \(\chi\), not to the heat weights.

## 2. The complete-sum obstruction theorem

**Theorem 1.** There exists \(t_0>0\) such that for every
\(0<t<t_0\), \(\kappa\in[1,2]\), and the exact data (1)--(2), a
completely multiplicative unit-modulus twist \(\chi\) satisfies

\[
\mathcal V_\chi=0.
\tag{5}
\]

The leading phase remains \(\psi_1=\theta_t(x)\). No term is omitted
from (4). The theorem asserts the existence of a twist at each parameter
point, not a common twist for an entire region or a twist from the genuine
height orbit. An explicit numerical value of \(t_0\) is not claimed.

The proof combines a bounded complete residual, a diverging isolated-prime
reservoir, and an elementary uniform contraction argument.

## 3. Uniform coefficient and frequency facts

The exact formulas and asymptotics in Note 8 give

\[
\alpha_r=L/2+O(x^{-2}),\quad
\alpha_i=-\pi/4+O(x^{-1}),\quad u=O(x^{-2}),\quad v=O(x^{-1}),
\]
\[
r_n=1-2\log n/L+O(t/(Lx)+1/(Lx^2)),\qquad c_n=O(t/x)
\tag{6}
\]

uniformly for \(n\le N\). Since \(\log N=L/2+o(1)\), the endpoint
value of \(r_n\) tends to zero. Moreover \(r_n\) is exactly affine
decreasing in \(\log n\), with slope
\(-2\Re(1+t\alpha'(s)/2)/L<0\) for small \(t\).
Consequently, after decreasing \(t_0\),

\[
\max_{n\le N}|r_n|\le1.01,\qquad
\max_{n\le N}|c_n|\le.01.
\tag{7}
\]

The squared weights satisfy

\[
\log w_n^2
=\{-(1+t\alpha_r)+(t/2)\log n\}\log n
\le\{-(1+t\alpha_r)+(t/2)\log N\}\log n.
\]

The negative of the last coefficient is
\(1+\kappa/4+o(1)\ge5/4+o(1)\). Thus, uniformly for small \(t\),

\[
w_n^2\le n^{-6/5}\qquad(1\le n\le N).
\tag{8}
\]

This uniform square-sum bound coexists with exponentially large absolute
coefficient sums. It is used only to select a bounded twisted residual.

The exact logarithmic slope of the unsquared weight is

\[
f'(\lambda):=\frac{d\log w}{d\lambda}
=-1/2-t\alpha_r/2+t\lambda/2,\qquad \lambda=\log n.
\tag{9}
\]

It is at most \(-.49\) up to \(N\) for sufficiently small \(t\), so
the weights decrease.

## 4. Isolated primes and a bounded complete residual

Select

\[
\mathcal P=\{p\text{ prime}:N/2<p\le3N/4\}.
\tag{10}
\]

Because \(2p>N\), a selected prime divides no other integer among
\(1,\ldots,N\). It occurs only as its own term. Its twist phase can
therefore be chosen independently without changing the twist of any
other retained integer. This independence is fully consistent with
complete multiplicativity.

For every prime \(q\le N\) outside \(\mathcal P\), choose
\(\chi(q)\) independently with uniform Haar measure on the unit circle.
Extend multiplicatively to every retained integer not in \(\mathcal P\).
Let \(T\) be the vector sum of these terms, including \(n=1\).
No such term depends on a selected-prime phase.

Unique factorization gives

\[
\mathbb E\{\chi(n)\overline{\chi(m)}\}=\mathbf1_{n=m},
\qquad
\mathbb E\{\chi(n)\chi(m)\}=0
\tag{11}
\]

for retained unselected integers, with the second identity excepting
\(n=m=1\). Indeed the exponent vector of a nontrivial integer is
nonzero, and independent Haar phases annihilate every nontrivial
character. This accounts for every cross term; no coefficient tail is
discarded.

For each \(n\ge2\), its random phase is uniform and

\[
\mathbb E\left|
(\cos\psi_n,r_n\sin\psi_n-c_n\cos\psi_n)
\right|^2=(1+r_n^2+c_n^2)/2.
\]

The leading vector has \(w_1=1\), \(c_1=0\), and fixed phase.
Hence

\[
\mathbb E|T|^2
=|(\cos\theta_t,r_1\sin\theta_t)|^2
+\frac12\sum_{\substack{2\le n\le N\\n\notin\mathcal P}}
w_n^2(1+r_n^2+c_n^2)
\]
\[
\le1.0201+1.0101\sum_{n=2}^\infty n^{-6/5}
\le1.0201+1.0101\int_1^\infty u^{-6/5}\,du<7.
\tag{12}
\]

Choose one realization with \(|T|\le\sqrt7\), and henceforth hold
all its prime phases fixed. This is an existence argument for a twist;
it is not a probabilistic assertion about genuine zeta phases.

## 5. The isolated-prime reservoir

For \(p\in\mathcal P\), write \(p=Nz\),
\(1/2<z\le3/4\). Define

\[
\mathfrak a(\kappa)=\kappa(4-\kappa)/16,
\qquad \mathfrak b(\kappa)=\kappa(\kappa+4)/16.
\]

Substitution into the exact weight gives, uniformly on this interval,

\[
w_p=e^{-\mathfrak b/t}z^{-1/2}(1+o(1)).
\tag{13}
\]

The bounded factor \(e^{t\log^2z/4}\) tends to one; the floor error
and the correction to \(\alpha_r=L/2\) are also uniform \(o(1)\).
Import the classical prime number theorem
\(\pi(y)\sim y/\log y\), the leading term of
[NIST DLMF, equation 27.12.4](https://dlmf.nist.gov/27.12#E4).
Partial summation, or the weighted consequence of that theorem on a
fixed relative interval, gives

\[
S:=\sum_{p\in\mathcal P}w_p
=(1+o(1))\frac{N}{\log N}e^{-\mathfrak b/t}
\int_{1/2}^{3/4}z^{-1/2}\,dz
\]
\[
=\left(\frac{2t}{\kappa}(\sqrt3-\sqrt2)+o(t)\right)
e^{\mathfrak a/t}.
\tag{14}
\]

The prime-number-theorem input is uniform here because the smallest
possible \(N\) tends to infinity and the relative interval is fixed.
In particular, \(\mathcal P\) contains arbitrarily many primes and
\(tS\to\infty\) uniformly, since
\(\mathfrak a(\kappa)\ge3/16\).

Equation (6), divided by \(t\), gives
\(r_p/t=2\log(N/p)/\kappa+o(1)\). Therefore, for small \(t\),

\[
t/4\le r_p\le1.5t,\qquad c_p=O(t/x).
\tag{15}
\]

The three positive sequences \(w_p,w_pr_p,w_pc_p\), in increasing
prime order, are decreasing. For the second sequence, both factors
decrease and \(r_p>0\). For the third, the exact identity
\(v=x(x^2+5)/(1+x^2)^2>0\) makes \(c_p\) a positive constant
times \(\log p\); its logarithmic derivative has sign
\(f'(\log p)\log p+1<0\), by (9) and
\(\log p=L/2+O(1)\to\infty\).

## 6. Three nearly equal ellipse groups

List the selected primes as \(p_1<\cdots<p_m\), and assign successive
primes cyclically to groups 1, 2, and 3. For any nonnegative decreasing
sequence \(a_1,\ldots,a_m\), the sums in these groups differ by at
most \(a_1\). To see this, extend the sequence by zeros; the difference
between group 1 and group 3 is bounded by

\[
\sum_{j\ge0}(a_{3j+1}-a_{3j+3})
\le\sum_{j\ge0}(a_{3j+1}-a_{3j+4})=a_1.
\]

The group sums are ordered, so all pairwise differences satisfy the
same bound. Apply this separately to the three sequences in Section 5.

Giving group \(j\) a common total phase \(\beta_j\) produces the exact
vector \(L_je(\beta_j)\), where

\[
e(\beta)=(\cos\beta,\sin\beta),\qquad
L_j=\begin{pmatrix}
\sum_jw_p&0\\
-\sum_jw_pc_p&\sum_jw_pr_p
\end{pmatrix}.
\tag{16}
\]

Put \(B=(L_1+L_2+L_3)/3\),
\(C=\sum_{p\in\mathcal P}w_pc_p\), and
\(D=\sum_{p\in\mathcal P}w_pr_p\). Then

\[
B=\frac13\begin{pmatrix}S&0\\-C&D\end{pmatrix},
\qquad
B^{-1}=\frac3S
\begin{pmatrix}1&0\\C/D&S/D\end{pmatrix}.
\tag{17}
\]

By (15), \(D/S\in[t/4,1.5t]\) and \(C/S=O(t/x)\), so
\(B\) is invertible and \(\|B^{-1}\|=O((tS)^{-1})\).
The cyclic-group bounds and (13), (15) give

\[
\max_j\|L_j-B\|=O(e^{-\mathfrak b/t}),
\]
\[
\epsilon:=\max_j\|B^{-1}(L_j-B)\|
=O\left(\frac{e^{-\mathfrak b/t}}{tS}\right)\longrightarrow0,
\qquad
\tau:=|B^{-1}T|=O((tS)^{-1})\longrightarrow0.
\tag{18}
\]

Every norm is the Euclidean vector norm or its induced matrix norm.
Both convergences are uniform. For the first, use
\(\mathfrak a+\mathfrak b=\kappa/2\); for the second, use (14).

## 7. An explicit contraction closes the exact vector

Let \(q_1=0\), \(q_2=2\pi/3\), and \(q_3=4\pi/3\).
Their unit vectors sum to zero. Hold \(\beta_3=q_3\), and set
\(\beta_1=u\), \(\beta_2=q_2+z_2\), with parameter
\(z=(u,z_2)\in\mathbb R^2\). The preconditioned equation
\(T+\sum_jL_je(\beta_j)=0\) becomes

\[
h(z)+E(z)+B^{-1}T=0,
\qquad h(z)=e(u)+e(q_2+z_2)+e(q_3),
\]
\[
E(z)=\sum_{j=1}^3 B^{-1}(L_j-B)e(\beta_j).
\tag{19}
\]

The derivative of \(h\) at zero is

\[
J=\begin{pmatrix}0&-\sqrt3/2\\1&-1/2\end{pmatrix},
\qquad \|J^{-1}\|=\sqrt2.
\]

Writing \(h(z)=Jz+R(z)\), elementary Taylor bounds give

\[
|R(z)|\le|z|^2/2,\qquad \|DR(z)\|\le|z|,
\qquad |E(z)|\le3\epsilon,\qquad
\|DE(z)\|\le\sqrt2\epsilon.
\tag{20}
\]

By (18), choose \(t_0\) small enough that
\(\epsilon\le.01\), \(\tau\le.02\), and all preceding uniform
conditions hold. On the closed ball \(|z|\le.1\), the fixed-point map

\[
\mathcal T(z)=-J^{-1}\{R(z)+E(z)+B^{-1}T\}
\]

has magnitude at most
\(\sqrt2(.005+.03+.02)<.078<.1\) and Lipschitz constant at most
\(\sqrt2(.1)+2(.01)<.162<1\).
Banach's contraction theorem supplies a fixed point. It solves the
exact two-coordinate equation, with no asymptotic remainder left in it.

For each selected prime in group \(j\), set
\(\chi(p)=e^{i(\beta_j-\phi_p)}\). This gives its prescribed total
phase. Keep all other retained prime phases at the chosen realization
from Section 4, set unused prime phases arbitrarily, and extend
completely multiplicatively. The isolation property ensures that this
last assignment changes only the selected-prime terms in the cutoff.
It proves (5).

## 8. What the theorem obstructs, and what remains open

The exact coefficients are not multiplicative, but the twist is. Thus
the theorem excludes a strictly positive joint lower bound for (4)
that is valid for every completely multiplicative unit-modulus twist
and uses only these exact coefficient and derivative data. The
independent-term obstruction of Note 8 does not need to be assumed.
The construction controls the complete twisted sum, including all
composite and small-prime terms, rather than an isolated packet alone.

The genuine case is \(\chi\equiv1\), with total phases coupled to the
same height through
\(\phi_n=\theta_t(x)+(x-t\alpha_i)\log n/2\).
The twists in Theorem 1 generally break that specific logarithmic orbit,
despite preserving multiplicativity. Their existence therefore does not
imply a zero of the genuine approximant, a collision of the heat flow,
or a failure of methods retaining the actual height correlations.

Nor does approximation of finitely many prime phases by a logarithmic
twist transfer (5) to a genuine collision. Changing the height also
changes the cutoff, the heat weights, the normalizer, the carrier phase,
and the derivative data. These simultaneous constraints are not paid by
such an approximation. No single twist producing zeros throughout a spatial neighborhood, or
actual-height realization of the constructed phases, is supplied here.

Note 8's full-disk remainder payment applies to the genuine heat function
and its genuine approximant. No analogous heat-function approximation
theorem is asserted for the twisted finite sum. Rather, (5) shows that a
signed lower-bound bridge valid for every multiplicative twist cannot
deliver even a positive bound, and hence cannot deliver the strictly
positive paid threshold required in the genuine case.

The principal missing input remains a local joint lower bound for the
**complete actual signed vector** (3), stronger than Note 8's collision
threshold, with its value, derivative, cutoff, and complex-neighborhood
errors paid. Note 9's genuine edge cancellation and averaged probes do
not remove that local requirement. A successful bridge must exploit
information stronger than arbitrary unit-modulus multiplicativity,
such as the actual height orbit and its signed correlations.

The [small checker](../../numerics/check_genuine_signed_heat_input.py)
checks only its stated finite algebraic and scalar assertions; it is not
a zero grid, a realization of these twists, or verification of the
prime number theorem. Analytic uniformity, character orthogonality,
the imported prime number theorem, and the contraction argument are
mathematical proof inputs. See the
[scoped review](../../reviews/HEAT_GENUINE_SIGNED_INPUT_REVIEW_20261009.md).
No RH assertion, actual collision, or literature-novelty claim is made.
