# Global physical-jet correlations: an absolute-lag Fejer test

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, same HCB chat0003, thread `01a184c3-9ae9-7b53-ad7e-f4f104e0fe5b`.

**Status: proved scoped failure of a global correlation budget;
separate-agent same-model internal review only.** This continues
[Note12][n12] at the unchanged tL=2 benchmark. The tested estimate is a
finite vector van der Corput/Fejer inequality for the **whole physical
remainder**, with all correlations between the former blocks retained
inside each lag. It uses no exponent-pair block bound. Its subsequent
replacement of signed lag sums by absolute allowances defeats a uniform
leading-pair certificate, even with exact lag magnitudes and arbitrary
choice of shift length.

The quantitative diagnostic used here is an exact canonical recurrence:
D -> zeta(2)-1 at every large real center, and C_1 -> 1/2 on an unbounded
sequence of centers. Consequently the tested remainder allowance is at
least sqrt(17)/4>1 on that sequence, for **every** shift length, while
the retained n=1 pair has radius one. This is a statement about that
allowance; it proves neither a small actual jet nor growth of its signed
remainder. **This absolute-lag consumer stops; HCB-05 remains Open.**

[Review08][review] records the separate same-model assessment. The
[reference record][refs] checks the classical differencing context;
the exact constants and recurrence used here are proved below. No source
values, numerical experiment, sweep, new manuscript or snapshot was
produced. [Input identities][inputs] record provenance, not validation
of the inherited complete-field approximation proof chain.

Read the [result index][results], [heat-flow cluster11][r11],
[collision controls12][controls] and [avoid index][avoid], especially
[target classification][a01], [control premises][a02],
[scoped failures][a07] and [signed payments][a12]. This is an estimate
of a specified budget's limitations, not a new global noncollision
criterion or an RH result.

## 1. Freeze the same model; retain its physical first derivative

Keep H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8, and

\[
 L=\log(X/(4\pi)),\quad t=2/L,\quad
 N=\lfloor e^{L/2}\rfloor,\quad z=X+u/L,\quad |u|\le1.
\tag{1}
\]

Reserve |u|<=2 and the inherited fixed complex buffers. Freeze X,L,N
and A=E_o(t,X)>0 before spatial differentiation. Use Note12's exact
E,Theta,rho and write

\[
 \lambda=\log(z/(4\pi)),\quad T_0=z/2+\pi t/8,\quad q=E/A,
 \quad\alpha=\rho/L,\quad\beta_c=\Theta_z/L,
 \quad D_c=4L\beta_c=\lambda+\pi t/(4z).
\]
\[
 k_n=\log n,\quad W_n=n^{-1/2}e^{t(k_n^2-\lambda k_n)/4},
 \quad\phi_n=\Theta-T_0 k_n,
\]
\[
 r_n=1-2k_n/D_c,\qquad d_n=tk_n/(zD_c).
\tag{2}
\]

The algebraic physical-jet map is
mathsf T(v_0,v_1)=(v_0,(alpha v_0-v_1)/beta_c). Its exact n-pair
contribution is

\[
 B_n:=\mathsf T V_n
 =qW_n(\cos\phi_n,\ r_n\sin\phi_n+d_n\cos\phi_n).
\tag{3}
\]

This includes the derivatives of the amplitude, phase and heat weight.
For example the complete signed sum obeys
partial_z U_0=-(t/(4z)+i/2)U_1; its physical derivative is not replaced
by a logarithmic derivative or an unscaled moment. The map is not
differentiated. It divides only by the nonzero carrier phase slope.

Note12's elementary gates apply here: eventually q>=1/2,
|alpha|<=1/16, 1/5<=beta_c<=1/3, ||mathsf T||<6,
0<=r_n<=1 and 0<=d_n<=1/(Lz). At the real center u=0, q=1 exactly.
The leading vector B_1=q(cos Theta,sin Theta) has radius q.

Set R=sum_{n=2}^N B_n and M=N-1. The completion remains separate.
No artificial high/low split or old dyadic block is removed from R.

## 2. The complete cross-block physical correlations

Zero-extend the finite vector sequence and define

\[
 \mathcal D=\sum_{n=2}^N\|B_n\|_2^2,\qquad
 C_h=\sum_{n=2}^{N-h}B_{n+h}\mathbin{\cdot}B_n,
 \quad C_h=0\ (h\ge M).
\tag{4}
\]

Each C_h sums *all* pairs at separation h, including pairs in different
former blocks. Taking the signed sum first permits cancellation between
those pairs. Both physical jet components remain correlated.

To make this explicit, for m=n+h put delta=phi_m-phi_n and
psi=phi_m+phi_n. Direct multiplication gives

\[
 B_m\mathbin{\cdot}B_n=\frac{q^2W_mW_n}{2}\big[
 (1+d_md_n+r_mr_n)\cos\delta
 +(1+d_md_n-r_mr_n)\cos\psi
\]
\[
 \hspace{20mm}+(r_md_n+d_mr_n)\sin\psi
 +(r_md_n-d_mr_n)\sin\delta\big].
\tag{5}
\]

Thus the full physical square contains both difference phases
-T_0 log(m/n) and sum phases 2Theta-T_0 log(mn). A scalar estimate
for |U_0|^2 alone would omit terms in (5). No such omission is made.

## 3. A finite global van der Corput/Fejer estimate

For **every integer K>=1**, including K>M, finite Cauchy--Schwarz yields

\[
 \|R\|_2^2\le\frac{M+K-1}{K}
 \left[\mathcal D+2\sum_{h=1}^{K-1}(1-h/K)C_h\right].
\tag{6}
\]

For completeness, relabel x_j=B_{j+1}, 1<=j<=M, and set
S_a=sum_{b=0}^{K-1}x_{a-b}, 1<=a<=M+K-1, using zero extension.
Then sum_a S_a=K R and

\[
 \sum_a\|S_a\|_2^2
 =K\mathcal D+2\sum_{h=1}^{K-1}(K-h)C_h.
\]

Cauchy on the M+K-1 sliding vectors proves (6) with exactly its stated
factor. The proof covers all endpoints and arbitrary K; no limiting
mean or height average is substituted. This is the standard differencing
mechanism, cf. [Tao, Lemma1.1.6][tao], with this finite real-vector form
and its constants derived here.

The selected consumer provides nonnegative lag allowances b_h>=|C_h|,
sets b_h=0 beyond the actual support, and uses

\[
 \mathcal E_K^2:=\frac{M+K-1}{K}
 \left[\mathcal D+2\sum_{h=1}^{K-1}(1-h/K)b_h\right],
 \qquad\|R\|_2\le\mathcal E_K.
\tag{7}
\]

It retains cross-block cancellation *inside each exact C_h*, then loses
cancellation between different signed lags at (7). We test even the
best absolute choice b_h=|C_h|. Larger allowances can only worsen it.
K may depend arbitrarily on the actual X,u and correlations.

## 4. The diagonal already loses for the usual K<=M range

At u=0, W_n=n^(-1) exp(k_n^2/(2L)). Through the frozen cutoff,

\[
 W_n^2=n^{-2}e^{k_n^2/L}\le n^{-3/2},\qquad
 \|B_n\|_2\le(1+d_{\max})W_n.
\tag{8}
\]

For fixed n, W_n -> 1/n, r_n -> 1 and d_n -> 0. Uniformly in the
moving phase, the difference between ||B_n||^2 and W_n^2 tends to zero:
its absolute value is at most
W_n^2(|r_n^2-1|+|r_n d_n|+d_n^2). Dominated convergence, with zeros
padded beyond N, therefore gives at every large center

\[
 \mathcal D\longrightarrow d_*:=\sum_{n=2}^{\infty}n^{-2}
 =\zeta(2)-1>5/8.
\tag{9}
\]

The final strict inequality can be checked without numerical evaluation:
1/4+1/9+1/16+1/25+integral_6^infinity x^(-2)dx=2269/3600>5/8.
The carrier phase needs no limit for (9).

For 1<=K<=M, the factor in (7) is at least 2-1/M, so even with every
lag allowance set to zero its allocated squared radius is at least
(2-1/M)D, tending to 2(zeta(2)-1)>1. Thus that entire shift range fails
at every sufficiently large real center. This is failure of an upper
allocation; it is not a lower bound for ||R||.

## 5. Allowing every shift length: a canonical recurrent obstruction

At u=0, removing K<=M does not repair this absolute-lag consumer uniformly.
There are X_j -> infinity with

\[
 T_0(X_j)\log n\longrightarrow0\pmod{2\pi}
 \quad\text{for every fixed positive integer }n,
 \qquad T_0(X)=X/2+\pi/(4L).
\tag{10}
\]

Here is a self-contained existence proof. For a finite vector
(log2/(2pi),...,log J/(2pi)), partition its torus into arbitrarily small
boxes. Among infinitely many nonnegative integer orbit indices, one box
contains infinitely many indices. Two in that box can have arbitrarily
large difference. Their difference is an arbitrarily large integer
frequency that brings every coordinate within the box diameter of zero.
For successively larger J and smaller boxes choose increasing frequencies
v_j -> infinity. The continuous function T_0(X) is eventually strictly
increasing, with derivative 1/2-pi/(4XL^2)>0, and tends to infinity.
Invert T_0(X_j)=v_j. This proves (10); it needs no independence hypothesis
on the logarithms and gives no effective or sampled height sequence.

For fixed h,n, (5) is, uniformly in Theta,

\[
 B_{n+h}\mathbin{\cdot}B_n
 =\frac1{n(n+h)}
 \cos\{T_0\log((n+h)/n)\}+o(1).
\]

The terms involving the carrier sum phase tend to zero for each fixed
pair. Also |B_{n+h} dot B_n|<=C[n(n+h)]^(-3/4), a summable majorant
in n. Dominated convergence along (10) yields the **actual signed**
model correlations

\[
 C_h\longrightarrow\sum_{n=2}^{\infty}\frac1{n(n+h)}
 =\frac1h\sum_{n=2}^{h+1}\frac1n
 \quad(h\text{ fixed});\qquad C_1\longrightarrow\frac12.
\tag{11}
\]

This is a pointwise recurrent statement, not a height average or a
claim about the sum over h growing with N.

Eventually on this same sequence, D>=5/8 and b_1>=|C_1|>=7/16.
For every K>=2, (7)'s bracket is at least

\[
 \mathcal D+2(1-1/K)b_1\ge\frac58+\frac7{16}
 =\frac{17}{16}.
\tag{12}
\]

Its prefactor is at least one. For K=1, the squared allocation is
M D>=17/16 once M>=2. Hence **every** shift length, even one selected
from exact correlations after seeing the height, obeys

\[
 \boxed{\ \mathcal E_K\ge\sqrt{17}/4>1
 \quad\text{along the unbounded canonical sequence.}\ }
\tag{13}
\]

The statement concerns the allocated upper bound (7). Large allocated
error or positive low-lag correlations do not imply a small exact jet,
a collision, or growth of the actual remainder.

## 6. Complete physical error budget and net return

The full normalized model jet is V_F=sum_n V_n+V_c, with
R_c=exp(-pi^2t/64)G f_N. Retain the inherited finite, uninstantiated
bounds |f_N|<=B_0 X^(-1/4), |f_N'|<=B_1 X^(-3/4),
|G'/G|<=B_gamma, |G|/E(0,z)<=B_G from [crossover CS25][cross].
The completion components divided by q cost separately

\[
 r_0=B_GB_0X^{-1/4}e^{-t\lambda^2/16},\quad
 r_1=\frac{B_G}{L}
 (B_\gamma B_0X^{-1/4}+B_1X^{-3/4})e^{-t\lambda^2/16}.
\tag{14}
\]

This retains the actual completion derivative and the exact cancellation
of its constant time exponential against the carrier. Its transformed
payment divided by q is

\[
 c_R=\sqrt{r_0^2+((|\alpha|r_0+r_1)/\beta_c)^2}
 =O(X^{-3/8})\quad(tL=2).
\tag{15}
\]

For the **complete** field-minus-model difference, CS6 gives separately

\[
 |\Delta V_0|\le q C_0X^{-3/4},\qquad
 |\Delta V_1|\le q C_1\frac{1+L}{L}X^{-3/4}.
\]
\[
 c_H=X^{-3/4}\sqrt{C_0^2+
 ((|\alpha|C_0+C_1(1+L)/L)/\beta_c)^2}=O(X^{-3/4}).
\tag{16}
\]

These source payments are made **once for the whole field**; they are
not assigned independently to each mode or correlation and multiplied
by the population. D and C_h are exact model quantities. No evolution
argument is used, and no claim is inferred from F_N's nonzero residual.

For this scheme the raw net margin and guaranteed physical floor are

\[
 \mathfrak m_K=q-\mathcal E_K-qc_R-qc_H,\qquad
 \|V_H\|_2\ge\frac{(\mathfrak m_K)_+}{6},
 \quad V_H=(H/A,H_z/(LA)).
\tag{17}
\]

At the recurrent centers q=1. Equation (13) implies for every K

\[
 \boxed{\ \mathfrak m_K\le1-\sqrt{17}/4-c_R-c_H<0.\ }
\tag{18}
\]

Thus the returned positive physical floor is zero. The failed raw
margin stays negative even if completion and source errors are set to
zero; improving those errors cannot repair this comparison. All
inherited buffer/onset and approximation-proof status qualifications
remain. This is a full negative budget, not an assumed nonvanishing
condition and not a negative value for the actual jet norm.

## 7. What changed, what remains, and the stopping rule

Unlike Note12, this test does not split the arithmetic remainder into
independent dyadic error blocks. The finite global inequality (6) keeps
their pair correlations, the derivative-weight terms, and both sum and
difference phases. The exact loss is at (7), followed by comparison of
the entire remainder against only the n=1 pair. The obstruction survives
even perfect acquisition of every |C_h| and optimization of K.

This **does not test** keeping the signed aggregate in (6) through the
consumer, preserving cancellation between different lags, including the
leading/remainder mixed terms in a full jet square, or choosing a larger
arithmetically justified main block. Those are different information
classes. We have acquired the recurrent correlation limits (11) and the
scoped negative margin (18), not a favorable bound for the missing signed
aggregate. No new conditional criterion is opened here in its place.

The known outer comparator tL>=61/24, with its time domain, arithmetic
package and unevaluated onset, is unchanged. There is no new zero
coverage, effective onset, matched-margin/cost advantage, RH statement
or time-zero simplicity bound. Positive-threshold/all-height exclusion
and the RH-conditional time-zero target retain their separate coverage
requirements.

The [control screen][controls] is analytical. The finite vector inequality
holds for every sequence and cannot distinguish theta from a colliding
control. The quantitative specialization (8)--(11) uses the unchanged
canonical arithmetic weights and phase: Euler-factor controls alter
coefficients/factors; weighted-square controls lack full normalized
reflection and the canonical approximation, and have no all-real heat
time; reflected/primitive controls lack integer-square arithmetic;
finite-prime-compatible perturbations and close-source controls lack the
full unchanged arithmetic data. A free heat double or a positive carrier
does not supply the same canonical expansion or error theorem. No
favorable exclusion is claimed for any control, and an event outside
this local domain is not tested. No controls were numerically rerun.

**Disposition:** complete this HCB-05 round-3 test and stop the
leading-pair plus whole-remainder, absolute-lag Fejer consumer. Other
signed-lag and full-square methods remain open. HCB-05 remains Open at
time zero; HCB-09 adds same-model review only. HCB-02 and the other
inherited results remain unchanged, and P is not automatically activated.
No numerical sweep or new source evaluation is proposed by this return.

[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[cross]: ../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[inputs]: GLOBAL_CORRELATION_INPUTS_20261028.json
[n12]: 12_SIGNED_EXPONENT_PAIR_TEST_AND_SCOPED_STOP_20261028.md
[r11]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[refs]: ../references/03_GLOBAL_CORRELATION_PRIMARY_SOURCE_20261028.md
[results]: ../../../../result-summaries/README.md
[review]: ../reviews/08_GLOBAL_CORRELATION_TEST_INTERNAL_REVIEW_20261028.md
[tao]: https://terrytao.wordpress.com/wp-content/uploads/2011/03/higher-book.pdf
