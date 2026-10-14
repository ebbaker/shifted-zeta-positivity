# Folded parity cusps and the 09-to-06 factorization test

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: `gpt-6-astra` (Codex); reasoning effort **ultra**.
This is an internal analytic continuation, not independent mathematical
validation. It develops the first bounded task in the
[06 program](INITIAL_RESEARCH_PROGRAM_20261013.md) using the exact
[09 two-coset reduction](../../../inactive/09_rank_two_theta_addition/notes/1_COMPLETE_TWO_COSET_REDUCTION_20261013.md).

**Result.** The modular-folded even-even lattice coset has a negative
Fourier response at all sufficiently large real frequencies, for both
complete paired kernels `J_0` and `J_1`. Consequently that individual
coset is not a positive-definite translation kernel and cannot have a
convergent positive autocorrelation factorization. This is an analytic
obstruction with every theta term retained; it does not depend on a
truncated numerical sign. The other coset cancels the offending algebraic
tail exactly. Neither the complete kernels nor their stationary signs
are refuted. The restriction to the **modular-folded** cosets matters:
the smooth, resummed raw parity split is a different decomposition.
Section 6 gives a **separate** negative zero-frequency certificate for
that raw same-parity coset, including its even reflection average.

## 1. The complete folded parity split

For `u >= 0`, write the genuine source as

\[
\Phi(u)=\sum_{n\ge1}p_n(u),\qquad
p_n(u)=\bigl(2\pi^2n^4e^{9u}-3\pi n^2e^{5u}\bigr)
             e^{-\pi n^2e^{4u}}.
\tag{1}
\]

Every term is positive on this half-line. Let

\[
A(u)=\sum_{n\ge1,\ 2\mid n}p_n(u),\qquad
B(u)=\sum_{n\ge1,\ 2\nmid n}p_n(u),\qquad A+B=\Phi.
\tag{2}
\]

Set `a=(log 2)/2`. Direct rescaling of the **complete** even subtotal gives

\[
A(u)=2^{-1/2}\Phi(u+a),\qquad u\ge0.
\tag{3}
\]

The two even folded sources used below are

\[
m_{A,t}(u)=e^{tu^2}A(|u|),\qquad
m_{B,t}(u)=e^{tu^2}B(|u|).
\tag{4}
\]

They are nonnegative and sum to `m_t(u)=e^{tu²}Phi_e(u)`. They have
rapid decay and all polynomial moments, locally uniformly for `t` in
every compact real interval. Their half-line restrictions are smooth up
to zero, but their even extensions are not differentiable at zero.

To connect (2) to the full rank-two theta addition, first fold the
physical source variables and then use scales `e^{4|u|},e^{4|v|}`.
The lattice change `(n,m) -> (alpha,beta)=(n+m,n-m)` has two cosets:

\[
\begin{array}{c|c|c}
\text{transformed indices}&\text{original indices}&\text{source pair}\\
\alpha,\beta\text{ both even}&n,m\text{ same parity}
 &A\otimes A+B\otimes B\\
\alpha,\beta\text{ both odd}&n,m\text{ opposite parity}
 &A\otimes B+B\otimes A.
\end{array}
\tag{5}
\]

In particular the even-even transformed coset contains both even-even
and odd-odd original indices. It is not just `A tensor A`. The signs of
nonzero lattice indices do not alter parity. In the full integer theta
expression the zero-index contributions are killed by the actual source
differential insertion; (1) already incorporates that cancellation.
There is no deletion of a nonzero axis term in passing to (5).

For every fixed derivative order, differentiation of a summand in (1)
produces a polynomial in `u` and `q=pi n²e^{4u}`, times an exponential
factor and `e^{-q}`. On `u >= 0`, half of `e^{-q}` dominates any such
polynomial and the other half supplies an integrable, summable majorant.
This remains true after `e^{tu²}` for compact `t`. Thus the folded
theta sums, half-line differentiation, Fourier moments, and the paired
integrals below admit absolute exchanges. This supplies the convergence
needed here without a raw positive-heat full-line termwise Mellin exchange.

## 2. An exact nonzero derivative at the folding point

At zero a direct differentiation gives

\[
p_n'(0)=e^{-q_n}(-8q_n^3+30q_n^2-15q_n),
\qquad q_n=\pi n^2.
\tag{6}
\]

For every even positive `n`, `q_n >= 4pi` and the expression in (6) is
strictly negative. Define

\[
c=-A'(0+)
 =\sum_{n\ge1,\ 2\mid n}(8q_n^3-30q_n^2+15q_n)e^{-q_n}
 =-2^{-1/2}\Phi'(a)>0.
\tag{7}
\]

The full genuine source is smooth and even, hence `Phi'(0)=0` and
`B'(0+)=c`. Multiplication by `e^{tu²}` does not change these first
derivatives at zero. The derivative jumps of (4) are therefore `-2c`
and `+2c`, for every real `t`. They cancel in their sum.

There is a simple explicit bound on the constant. With

\[
c_2=(512\pi^3-480\pi^2+60\pi)e^{-4\pi},
\]

\[
0<c-c_2\le
\frac{8\pi^3\,4^6e^{-16\pi}}
 {1-(3/2)^6e^{-20\pi}}.
\tag{8}
\]

Indeed the omitted even indices start at 4, each coefficient is bounded
above by `8pi³n^6`, and successive even-index majorants have ratio at
most `(3/2)^6 exp(-20pi)`. For scale only, ordinary floating evaluation
gives `c_2 approximately 0.03949868261495417` and the right side of (8)
approximately `1.503e-16`. The exact expressions and their analytic
inequalities, not these decimal approximations, establish `c>0`.

## 3. Exact paired response normalization

Use the original normalization

\[
h_A(t,x)=\tfrac12\widehat m_{A,t}(x)
 =\int_0^\infty e^{tu^2}A(u)\cos(xu)\,du,
\qquad h_B\text{ similarly},\qquad H=h_A+h_B.
\tag{9}
\]

For real functions `f,g`, define the polarized Laguerre expression

\[
Q_j(f,g)=f^{(j+1)}g^{(j+1)}
 -\tfrac12\{f^{(j)}g^{(j+2)}+g^{(j)}f^{(j+2)}\},
\quad L_j(f)=Q_j(f,f).
\tag{10}
\]

Let `J_j^{sigma tau}` be the paired integral in the initial program
with sources `m_sigma(s+r)m_tau(s-r)`. Changing `r` to `-r` shows
`J_j^{AB}=J_j^{BA}`. The usual change `u=s+r,v=s-r` has absolute
Jacobian two. Symmetrization of its multiplier gives, exactly,

\[
\widehat J_j^{\sigma\tau}(2x)=Q_j(h_\sigma,h_\tau).
\tag{11}
\]

No smoothness across the folding point is required in this calculation:
absolute polynomial moments justify Fubini and Fourier differentiation.
The result follows from the same normalization as the
[complete-kernel note](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/7_COMPLETE_LAGUERRE_KERNELS_AND_TRIPLE_ZERO_LIMIT_20261010.md).

The same-parity and opposite-parity folded kernels are

\[
J_j^{\rm same}=J_j^{AA}+J_j^{BB},\qquad
J_j^{\rm opp}=2J_j^{AB},\qquad J_j=J_j^{\rm same}+J_j^{\rm opp}.
\tag{12}
\]

Their Fourier responses consequently satisfy

\[
C_j:=\widehat J_j^{\rm same}(2x)=L_j(h_A)+L_j(h_B),\quad
O_j:=\widehat J_j^{\rm opp}(2x)=2Q_j(h_A,h_B),\quad
C_j+O_j=L_j(H).
\tag{13}
\]

These equalities retain both derivative levels, including the signed
factor `r²-s²` when `j=1`.

## 4. A rigorous negative Fourier tail for the same-parity coset

Repeated half-line integration by parts in (9) gives

\[
h_A(t,x)=\frac{c}{x^2}+O_T(x^{-4}),\qquad
h_B(t,x)=-\frac{c}{x^2}+O_T(x^{-4}).
\tag{14}
\]

The derivative version, for each fixed nonnegative integer `k`, is

\[
\partial_x^k h_A(t,x)=
 \frac{(-1)^k(k+1)!c}{x^{k+2}}+O_{T,k}(x^{-k-4}),
\quad
\partial_x^k h_B(t,x)=
 -\frac{(-1)^k(k+1)!c}{x^{k+2}}+O_{T,k}(x^{-k-4}).
\tag{15}
\]

Here `|t| <= T` and `x -> +infinity`. Formula (15) follows by applying
integration by parts to the differentiated integral with amplitude
`u^k e^{tu²}A(u)` (or `B`); it is not an unsupported differentiation of
the big-O in (14). All required amplitude derivatives are integrable
uniformly on the indicated compact time interval. Boundary terms at
infinity vanish. At zero, the first nonzero cosine/sine boundary term
is determined by the slope in (7), and the next has two additional
inverse powers of `x`.

For `f(x)=c/x²`, direct differentiation gives

\[
L_j(f)=-\frac{(j+1)!(j+2)!c^2}{x^{2j+6}}.
\tag{16}
\]

Substitution of (15) into (13) proves

\[
\boxed{C_j(t,x)=
 -\frac{2(j+1)!(j+2)!c^2}{x^{2j+6}}
 +O_{T,j}(x^{-2j-8}).}
\tag{17}
\]

In particular

\[
C_0=-4c^2x^{-6}+O_T(x^{-8}),\qquad
C_1=-24c^2x^{-8}+O_T(x^{-10}).
\tag{18}
\]

For each compact time interval, both expressions are strictly negative
above some finite frequency threshold. This proof does not supply an
effective numerical threshold. That is a separate job for a bounded
outward-arithmetic witness.

The full `H` is Schwartz in real frequency, with all fixed derivatives,
because its full source is smooth with rapid decay. Equations (13) and
(17) therefore also give

\[
O_j(t,x)=\frac{2(j+1)!(j+2)!c^2}{x^{2j+6}}
 +O_{T,j}(x^{-2j-8}).
\tag{19}
\]

The algebraic tails cancel only after the two cosets are recombined.
Cancellation of their leading terms alone is not a sign estimate for
the much smaller complete response.

Each folded coset kernel is real, even, continuous, and integrable.
A continuous integrable positive-definite translation kernel must have
nonnegative Fourier transform. Thus (18) refutes positive definiteness
of `J_0^{same}` and `J_1^{same}` and refutes a sum of positive
autocorrelations for either one. This inference uses a **negative
Fourier value**, not a negative source-kernel value. No explicit finite
Gram minor or claim of a two-point obstruction is needed or supplied.

The [outward replay](../../../inactive/09_rank_two_theta_addition/numerics/check_rank_two_to_paired.py)
also supplies an effective witness at `t=0,x=60`, hence kernel Fourier
frequency `2x=120`. Its [small record](../../../inactive/09_rank_two_theta_addition/numerics/RANK_TWO_TO_PAIRED_RECORD_20261013.json)
gives, with the endpoints below rounded outwards,

\[
-2.536417\cdot10^{-14}<C_0(0,60)<-2.509075\cdot10^{-14},
\]
\[
-1.088143\cdot10^{-16}<C_1(0,60)<-1.072289\cdot10^{-16}.
\tag{18a}
\]

The replay retains theta terms 1, 2, and 3, uses 1,024 Simpson panels
on the half-source interval `[0,1]`, encloses the fourth-derivative
quadrature remainders, and pays all omitted theta and source tails.
Its 60-digit directed arithmetic establishes these bounded signs;
the floating scout is not the certificate. No sector stationarity is
asserted at this witness.

## 5. The matrix obstruction and the exact surviving target

The polarized response matrix is

\[
\mathcal Q_j(t,x)=
\begin{pmatrix}
L_j(h_A)&Q_j(h_A,h_B)\\
Q_j(h_A,h_B)&L_j(h_B)
\end{pmatrix}.
\]

Equations (15)-(16) show

\[
\mathcal Q_j=
-\frac{(j+1)!(j+2)!c^2}{x^{2j+6}}
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
 +O_{T,j}(x^{-2j-8}).
\tag{20}
\]

The parity contrast vector `(1,-1)` has negative quadratic response
for large `x`. Hence the matrix is not positive semidefinite. An
invertible real constant change of the two source coordinates acts by
congruence and cannot repair this failure. This rules out a positive
matrix factorization for this entire folded parity matrix, not an
identity designed only for its physical direction `(1,1)`.

Put `D=h_A-h_B`. Polarization gives the exact identities

\[
\boxed{C_j=\tfrac12\{L_j(H)+L_j(D)\},\qquad
O_j=\tfrac12\{L_j(H)-L_j(D)\}.}
\tag{21}
\]

The physical direction cancels the cusp channel exactly. This also
shows what the two-coset identity alone has and has not achieved: it
isolates an explicit troublesome contrast channel, but does not prove
the sign of `L_j(H)`.

Writing `v_k=(h_A^{(k)},h_B^{(k)})` and `e=(1,1)`, the remaining full
target is the precise quadratic expression

\[
L_j(H)=(e^Tv_{j+1})^2-(e^Tv_j)(e^Tv_{j+2}).
\tag{22}
\]

On the required complete stationary set `e^T v_{j+1}=0`, it reduces to

\[
-(e^Tv_j)(e^Tv_{j+2})\ge0,
\qquad j=0,1.
\tag{23}
\]

These constraints are respectively `H'=0` and `H''=0`. They impose no
separate stationarity on either parity subtotal. Imposing those extra
conditions would change the problem. Any continuation through this
folded representation must retain the cross-coset cancellation and
control (22) or (23) after it; a lower bound for each diagonal sector
cannot provide the desired proof.

## 6. Why this is not a universal parity obstruction

The complete raw subtotal, before even folding, is instead

\[
A_{\rm raw}(u)=2^{-1/2}\Phi_e(u+a),\qquad
B_{\rm raw}(u)=\Phi_e(u)-A_{\rm raw}(u),\qquad u\in\mathbb R.
\tag{24}
\]

Both are smooth and rapidly decreasing. They are generally not even;
`B_raw` is negative sufficiently far down the negative half-line. With
the half-Fourier normalization, the exact resummed transform is

\[
h_{A,\rm raw}(t,x)
=2^{-1/2}e^{ta^2-iax}H_t(x+2ita),\qquad
h_{B,\rm raw}=H_t-h_{A,\rm raw}.
\tag{25}
\]

This follows by substituting `v=u+a` in the absolutely convergent
integral of the already-resummed shifted source. In general the raw
coset kernels are not even and their Fourier responses are complex,
so they do not directly furnish the real positive-definite factorization
sought in 06. A subsequent reflection or another recombination is a
separate candidate and is not ruled out by (17).

Crucially, convergence of the **resummed** sources in (24) does not
justify integrating their individual raw theta summands at positive
heat. For fixed `n`, the original summand behaves as
`-3pi n² exp(5u)` as `u -> -infinity`; multiplication by `exp(tu²)`
is nonintegrable there when `t>0`. The folded construction in Sections
1-5 avoids that exchange and has the separate endpoint cost proved
above. Neither representation permits silently taking the convergence
advantage of one and the smoothness advantage of the other.

There is nevertheless a separate, easier obstruction to the raw
same-parity coset. At `t=0`, let

\[
H_0=H_{t=0}(0)=\int_0^\infty\Phi(u)\,du>0,\qquad
I_2=\int_0^\infty u^2\Phi(u)\,du>0,
\quad\kappa=2^{-1/2}.
\]

The complete source is even, so its first and third Fourier derivatives
vanish at zero and its second is `-I_2`. By (25), the raw even transform
at `t=0` is `kappa exp(-iax)H(x)` and the other is the difference from
`H`. Differentiating those exact expressions yields

\[
C_{0,\rm raw}(0,0)
=(2-\sqrt2)H_0I_2-\frac{a^2H_0^2}{\sqrt2},
\]
\[
C_{1,\rm raw}(0,0)
=(2-\sqrt2)I_2^2-(1+\sqrt2)a^2H_0I_2.
\tag{26}
\]

For example, with `q=H''(0)=-I_2`,
`L_1(h_A)=kappa²(q²+a²H_0q)` and
`L_1(h_B)=(1-kappa)²q²+(2kappa+kappa²)a²H_0q`.
This checks the derivative-level normalization and the extra phase
terms in the second formula; they cannot be discarded.

The same replay encloses these two complete moments using 1,024 outward
cell ranges on `[0,1]`, again with all theta and source tails. The result
is recorded under `raw_unfolded_coset_zero_frequency_certificate` and
implies the outward-rounded inequalities

\[
-3.124613\cdot10^{-4}<C_{0,\rm raw}(0,0)
 <-2.914205\cdot10^{-4}<0,
\]
\[
-1.316605\cdot10^{-5}<C_{1,\rm raw}(0,0)
 <-1.211979\cdot10^{-5}<0.
\tag{27}
\]

Unlike the folded asymptotic proof, this establishes the signs at one
specified time and frequency. The raw kernels are real but generally
not even; their even reflection averages have Fourier transform equal
to the real part of the raw response. At zero this averaging leaves
(27) unchanged. Thus neither raw same-parity kernel, **nor its even
reflection average**, has a positive-definite translation-kernel
factorization. This is an independent obstruction to that particular
attempt to repair the raw decomposition. It does not rule out a
different construction which mixes its two cosets. Continuity in heat
time also makes both strict zero-frequency signs persist on some open
interval about `t=0`; this argument supplies no effective time radius.

## 7. Decision

The 09-to-06 transfer disproves the first positive factorization
candidate in two natural realizations: the modular-folded same-parity
coset has a negative high-frequency tail, and the smooth resummed raw
same-parity coset has a certified negative response at zero, retained
by simple even reflection. **Independent positive autocorrelations of
these cosets cannot establish the requested signs.** The full
factorization and both full stationary signs remain open. The useful
next analytic step is a source-derived recombination that handles the
cross-coset terms, followed by a sign estimate for the complete physical
response. An identity or passing finite test alone does not discharge
that estimate or the required global time and height coverage.
