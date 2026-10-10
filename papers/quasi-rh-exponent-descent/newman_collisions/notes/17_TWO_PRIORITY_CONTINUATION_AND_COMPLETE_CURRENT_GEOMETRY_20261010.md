# Two priority continuations and complete coherent-current geometry

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Algebra, interval replay and
cross-readings are internal LLM checks, not independent mathematical review.

This continues projects 09 and 13 from
[Heat Note 16](16_FIVE_PRIORITY_CONTINUATIONS_AND_SIGNED_ARITHMETIC_CHECKPOINTS_20261010.md).
Project 09 now has an explicit paid family of candidate-null dual kernels,
including all four difference/product sine/cosine terms. Its optimal
conditional moment-norm relaxation has surviving positive directions,
so that chosen mechanism cannot force the desired negative threshold
sign, and a genuine-height rank certificate verifies that this loss occurs
for actual arithmetic data. Project 13 now restores all 22,066 cutoff
terms and certifies a positive-time rectangle containing exactly one
simple genuine heat zero at every time. The common current geometry
below gives a sharp quantitative joint-vector lower bound and
distinguishes the carrier-sensitive test from its optimal
carrier-independent form.

## 1. Keep the actual complete state and its payments

Use the complete fixed-cutoff arithmetic branch
\[
 S=\sum_{n\le N}q_n=u+iv,\qquad S'=u'+iv',\qquad F_{t,N}=2u,
\]
with the exact symmetric normalizer \(H_t=A_tQ_t\). Derivatives are
at fixed time and integer cutoff. The carrier and amplitude coefficients
are differentiated as physical functions; the finite branch is not
assigned an independent Newman heat equation.

In the shrinking sector, set \(L=\log(x/(4\pi))\),
\(\kappa=tL\), \(N=\lfloor\sqrt{x/(4\pi)+t/16}\rfloor\).
The complete holomorphic interface gives
\[
 |Q_t-2u|\le\eta_N,\qquad |Q_t'-2u'|\le L\eta_N,
 \qquad \eta_N\le5e^{-\kappa(\kappa+4)/(16t)}.
\tag{1}
\]
The disk, reflected sum, natural-cutoff changes and Cauchy derivative
are all paid in [Heat Note 8](8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md),
using the imported
[Polymath approximation theorem](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem3).
The latter remains an analytic input, not a proof replay in the new code.
All new finite certificates must keep (1); no raw huge-height theta
quadrature is substituted for the normalized observation.

Define the complete current
\[
 \mathcal J=-\Im(S'\overline S)=u'v-uv'.
\tag{2}
\]
For a block and its full complement,
\[
 \mathcal J=\mathcal J_B+\mathcal J_C
          -\Im(S_B'\overline{S_C}+S_C'\overline{S_B}).
\tag{3}
\]
Every cross term is necessary. The previous negative actual block
current did not imply a negative complete current.

## 2. A sharp paid lower bound for the true joint vector

Put \(\varepsilon=\eta_N/2\),
\(O=(u,u'/L)\), \(V=(v,v'/L)\),
\(a=(-V_2,V_1)\), \(j=\mathcal J/L\). Then \(a\cdot O=j\).
The true normalized pair \(q=(Q_t,Q_t'/L)\) obeys
\(q=2(O-\delta)\) for some
\(\delta\in[-\varepsilon,\varepsilon]^2\), by (1).
The error square has support
\(\max|a\cdot\delta|=\varepsilon(|V_1|+|V_2|)\).
Consequently, whenever \(V\ne0\),
\[
 \boxed{\left\|(Q_t,Q_t'/L)\right\|\ge
 \frac{2\left(|\mathcal J|-
       \frac{\eta_N}{2}(L|v|+|v'|)\right)_+}
      {\sqrt{L^2v^2+(v')^2}}.}
\tag{4}
\]
Here \(r_+=\max(r,0)\). If \(V=0\), consistency gives
\(\mathcal J=0\), and this information alone gives lower bound zero.
There is no division by the complex amplitude \(S\).

This bound is sharp over compatible abstract quadratures and errors.
If \(|j|\) is no larger than the square support, choose an error
\(\delta\) with \(a\cdot\delta=j\) and take \(O=\delta\).
Otherwise take the maximizing corner of the square and add to it the
shortest perpendicular displacement
\(\operatorname{sgn}(j)(|j|-\varepsilon\|a\|_1)a/\|a\|_2^2\).
Both constructions attain (4). They are extremizers of the geometric
information, not asserted arithmetic realizations.

Thus the earlier necessary candidate condition
\[
 |\mathcal J|\le\frac{\eta_N}{2}(L|v|+|v'|)
\tag{5}
\]
is already optimal given only the complete current, invisible
quadratures and rectangular errors. Replacing the square by a Euclidean
ball gives a weaker test. The new content of (4) is the exact distance
and quantitative visibility margin, not a free strengthening of (5).

## 3. Difference and reflected-sum interference are linked exactly

Let
\[
 T_0=|S|^2+|S'|^2/L^2,\qquad R_0=S^2+(S')^2/L^2.
\]
Direct real algebra gives
\[
 u^2+(u'/L)^2=\tfrac12(T_0+\Re R_0),\qquad
 T_0^2-|R_0|^2=4\mathcal J^2/L^2.
\tag{6}
\]
The modulus observations and current use difference interference;
\(R_0\) retains the reflected phase sums. Under a constant carrier
rotation \(S\mapsto e^{i\gamma}S\), applied also to \(S'\),
\(R_0\mapsto e^{2i\gamma}R_0\), while \(T_0,\mathcal J\) remain
fixed. This auxiliary constant rotation is not a physical change of
height, where coefficient derivatives must also be retained.

The exact minimum observable energy over constant rotations is
\[
 \min_\gamma\{u_\gamma^2+(u_\gamma'/L)^2\}
 =\frac{T_0-|R_0|}{2}
 =\frac{T_0-\sqrt{T_0^2-4\mathcal J^2/L^2}}{2}.
\tag{7}
\]
It is the smallest singular value squared of
\(\begin{pmatrix}u&v\\u'/L&v'/L\end{pmatrix}\).
A nonzero complete current prevents perfect reflected-sum cancellation,
but does not determine the actual carrier angle.

There is also an exact square version, appropriate to (1):
\[
 \boxed{\min_\gamma
 \max\{|u_\gamma|,|u_\gamma'|/L\}
 =\frac{|\mathcal J|}
        {\max\{|LS+S'|,|LS-S'|\}}.}
\tag{8}
\]
When the matrix is singular the minimum is zero; the all-zero case is
interpreted separately as zero rather than a quotient. For an invertible
matrix \(M\), its real-readout ellipse obeys
\(O^T(MM^T)^{-1}O=1\). A centered square first meets this ellipse at
a corner maximizing the inverse-Gram quadratic form. That corner value
is
\[
 \frac{T_0+2|\Re(S'\overline S)|/L}{\mathcal J^2/L^2},
\]
whose reciprocal square root is (8). The exact corner extremizer is
checked by rational matrix inversion in the replay.

Therefore
\[
 |\mathcal J|>\frac{\eta_N}{2}
                    \max\{|LS+S'|,|LS-S'|\}
\tag{9}
\]
excludes every constant carrier angle. It is the sharp phase-independent
square test. The actual-angle condition (5) can be stronger, because
\(L|v|+|v'|\le\max\{|LS+S'|,|LS-S'|\}\).
No new lower bound for the current follows from these algebraic identities.

On \(S\ne0\), \(\mathcal J=-|S|^2\partial_x\arg S\). A real
double zero can occur at a nonzero complex amplitude when its phase is
\(\pi/2\) modulo \(\pi\) and its phase speed vanishes. Nonvanishing
complex amplitude alone is therefore insufficient. This is visible in
an actual smooth positive-kernel control, rather than only arbitrary
quadratures. Use the shifted positive average \(p_b\) of
[project 06 Note 2](../06_theta_lattice/notes/2_GREEN_KERNEL_ENDPOINT_EQUIVALENCE_AND_CONDITIONAL_JETS_20261010.md),
with \(0<b\le1/20\), and initial kernel
\(s e^{-Tu^2}p_b(u)\). Its half-line complex readout at time \(T\) has
real part \((s/2)B(x)\cos^2(bx)\), where
\(B=\int_{\mathbb R}e^{-\cosh u}e^{ixu}du\).
At \(x_*=\pi/(2b)>30\), its real part and first derivative vanish.

The imaginary part is nonzero. Indeed \(p_b(0)>1/4\) and
\(\|p_b''\|_{L^1(0,\infty)}<4\). For the latter, put
\(\varphi=e^{-\cosh u}\); integration of
\((\sinh u\,\varphi)'\) gives
\(\int\sinh^2u\,\varphi=\int\cosh u\,\varphi\), while
\(\int_{\mathbb R}\cosh u\,\varphi\le4e^{-1/2}<4\).
Thus \(\|\varphi''\|_{L^1(\mathbb R)}<8\), and the even shifted
average has half-line norm below four. Two integrations by parts give
\[
 \int_0^\infty p_b(u)\sin(xu)du
 =\frac{p_b(0)}x-\frac1{x^2}\int_0^\infty p_b''(u)\sin(xu)du
 >\frac{x-16}{4x^2}>0\quad(x>30).
\]
Hence \(S\ne0\) but \(\mathcal J=0\) at the control double zero.
Choose \(b\) avoiding the discrete zeros of \(B(x_*)\) to make it
ordinary. Its real readout has all-real zeros at time \(T\), by the
spectral argument imported in the cited note. The control has every
fixed Gaussian/exponential derivative weight. It rules out a deduction
of nonzero full current from those generic positive-kernel properties;
it is not a prescribed finite arithmetic-orbit state.

## 4. Exact cross-feed to project 09

At one center use Note 2's frozen
\(\mu=\Omega/c\), \(M_k=\sum q_n(\log n-\mu)^k=X_k+iY_k\).
Then \(S=M_0\) and the physical first derivative is exactly
\[
 S'=A M_0+(-d+ic)M_1,\qquad A=-d\mu\in\mathbb R.
\]
Thus
\[
 v'=AY_0-dY_1+cX_1,
\]
\[
 \boxed{\mathcal J=-c(X_0X_1+Y_0Y_1)
                       +d(X_0Y_1-Y_0X_1).}
\tag{10}
\]
For ordered pairs \(h=\log(nm)-2\mu\), \(\delta=\log(n/m)\),
the complete current kernel is
\[
 \mathcal J=\sum_{n,m\le N}w_nw_m
 \left[-\frac c2h\cos(T\delta)
                +\frac d2\delta\sin(T\delta)\right].
\tag{11}
\]
It is purely the difference-phase channel. The invisible quadratures in
(4)--(5) still depend on the actual carrier. The fourth-jet threshold
target in 09 retains both ratio and product channels; controlling (11)
alone is not an identity for that target.

[Project 09 Note 3](../09_prime_phase_torus/notes/3_PAID_DUAL_KERNELS_AND_ACTUAL_FREQUENCY_RELAXATION_LOSS_20261010.md)
defines \(e=(X_0,Y_1+(d/c)X_1)\),
\(u=(X_2,Y_3,X_4)\), and
\(\mathcal K=2Y_3^2+3X_2X_4-(\gamma/c^2)X_2^2\).
Its dual family is
\[
 \mathcal K_{\Lambda,B}=\mathcal K+e^T\Lambda e+2e^TBu.
\tag{12}
\]
At paid candidates each added term has an explicit measured payment
\(\Pi_{\Lambda,B}\). A certified upper bound \(U_{\Lambda,B}\)
would suffice only if
\[
 U_{\Lambda,B}+\Pi_{\Lambda,B}
                  +\widehat\Delta/(4c^6)<0.
\tag{13}
\]
The dual changes introduce sine kernels in both ratio and product
channels. They keep the prescribed weights, common height, actual
carrier and complete block/core interference. Large multipliers also
enlarge their candidate-error payment.

The optimal conditional Hilbert-space moment-norm envelope has a precise
limitation. If its residual Gram matrix \(H\) is positive definite,
the conditioned threshold matrix retains inertia two positive, one
negative. Its sharp relaxed maximum is strictly positive even when both
candidate coordinates and all jet errors are set to zero. This is a
conditional result about that relaxation, not a claim of certified
actual-theta Gram positivity at all heights.

There is now a genuine-height witness for the hypothesis. At
\(M=N=22066\), \(t_0=(2\log M)^{-1}\), \(x_0=4\pi M^2\),
five actual feature rows, at nodes \(1,2,8,128,11033\), have determinant
strictly between \(155566620\) and \(155566621\). All phases, the
common carrier, centering and drift are enclosed by outward intervals.
Every prescribed weight is positive, so this witness proves positive
definiteness of the complete five-feature Gram and its residual Schur
complement at that height. It is a noncandidate state: it verifies the
relaxation's genuine-data rank hypothesis, not an actual candidate with
a positive threshold sign. The conditioned zero-coordinate envelope is
still an enlarged class of moment vectors.

A separate positive coefficient control on \(n=1,2,4\) at
\(T\log2=(2k+1)\pi\), with coefficients \(1,2,1\), has
\(M_0=M_1=0\) at the actual common carrier and derivative drift, but
\(\mathcal K>0\) in the stated high-height range. Its local reweighting
keeps the full raw multiplier. These deliberately changed coefficients
are not the complete genuine heat approximant. They demonstrate why
frequency consistency, positivity and candidate equations alone cannot
force (13); the prescribed heat coefficients must enter more strongly.

## 5. A complete finite rectangle with genuine simple zeros

[Project 13 Note 3](../13_microlocal_phase_space/notes/3_COMPLETE_CURRENT_AND_PAID_SIMPLE_ZERO_RECTANGLE_20261010.md)
uses the same \((t_0,x_0)\) and the complete genuine cutoff to prove a
finite heat theorem on
\[
 \mathcal R=\{t_0\le t\le t_0+8\cdot10^{-6},\quad
                  x_0+0.3\le x\le x_0+0.4\}.
\tag{14}
\]
Here \(t_0\simeq0.04999103540097\),
\(x_0\simeq6118670856.7243349\). The entire rectangle has
\(t<0.05\), \(1<\kappa<1.000161\), and natural cutoff \(22066\).

At the center the negative block current is about \(-0.000673643\),
but the full complement contributes \(12.32324368\) and the cross
current contributes \(-0.21581201\). The complete current is therefore
\(12.10675803\), with paid gap above \(12.0455\) in (5).
Both real-vector cross energies are retained separately: the difference
channel is about \(-0.0437599560\), while the reflected-sum channel is
about \(0.00922600702\). The block sign cannot be assigned to the
complete state.

To cover (14), the checker expands the full signed coherent sum at height
offset \(0.35\), retaining jets through order five. Its sixth absolute
frequency moment pays the Taylor remainders over radius \(0.05\).
An explicitly integrated logarithmic-derivative residual pays the
physical spatial carrier and amplitude motion. Full time derivatives
then pay the time increment. Finally (1) pays the genuine heat remainder,
including its Cauchy derivative. No independent phases, core omission,
or independent finite-sum heat equation enters.

The final coarse enclosures are
\[
 -0.337<Q_t(x_0+0.3)<-0.246,\qquad
 0.851<Q_t(x_0+0.4)<0.941,
\]
\[
 10.20<Q_t'(x)<13.46\qquad ((t,x)\in\mathcal R).
\tag{15}
\]
The value and derivative heat payments are below \(0.009642\) and
\(0.193\), respectively. Endpoint signs and strict monotonicity give
exactly one zero of \(Q_t\), hence \(H_t\), inside this height interval
for every allowed time. At that zero \(H_t'=A_tQ_t'\ne0\); the
implicit-function theorem gives its smooth zero branch. Thus there is
no joint zero of \((H_t,H_t')\) anywhere on the rectangle. This
does not require an all-real-threshold hypothesis.

The uniform complete-current gap is greater than \(5.09\). Bounds
\(L<20.004\), \(|v|<1.401\), \(|v'|<3.447\) give
\(\sqrt{L^2v^2+(v')^2}<28.3\), so (4) independently yields
\[
 \|(Q_t,Q_t'/L)\|>0.35\quad\hbox{on }\mathcal R.
\tag{16}
\]
For this particular rectangle (15) is stronger: it directly gives a
joint-vector norm above \(0.5\). The current computation demonstrates
the paid geometry and complete recombination; the observed derivative
also certifies uniqueness and simplicity of the actual real zero.

The small
[interval certificate](../13_microlocal_phase_space/numerics/COMPLETE_CURRENT_RECTANGLE_CERTIFICATE_20261010.json)
contains all enclosures and transport budgets. It is source-bound and
replayed with 60-digit outward arithmetic. The analytic approximation
theorem and the manuscript's complex-disk deductions remain imported
inputs. This proves a bounded finite rectangle, with no assertion that
all genuine candidate states satisfy its current margin.

## 6. Checks and the next research input

[The shared current-geometry checker](../../numerics/check_coherent_current_geometry.py)
uses only standard-library Fraction arithmetic. Its
[source-bound record](../../numerics/COHERENT_CURRENT_GEOMETRY_RECORD_20261010.json)
has 22,492 passing exact checks: paid-square distance and extremizers,
2,112 nonsingular integer matrices, the difference/reflected-sum bridge,
constant rotations, centered amplitude drift, and complete ordered-pair
current regrouping. These are finite checks of algebra and sharpness;
the source note supplies the general proofs. They are not numerical
current bounds on the genuine state.

The project 09 checker passes 495 exact assertions and the genuine-height
rank certificate. Project 13 passes the complete-cutoff, recombination,
transport, endpoint and monotonicity assertions for (14). Both verify
their unchanged imported interval source's hash before import; their new
local integer-power routines use guaranteed outward rational division
or repeated directed multiplication. The
[shared review](../../reviews/HEAT_TWO_PRIORITY_SIGNED_CONTINUATION_REVIEW_20261010.md)
and [replay audit](../../reviews/HEAT_TWO_PRIORITY_SIGNED_CONTINUATION_CHECK_RECORD_20261010.json)
record source identities, byte-identical replay and the exact rational
checks of the displayed joint-vector bounds.

The next sector-wide input is either a paid complete current margin in
(5) or (9), or a prescribed-coefficient dual pair estimate beating (13).
The former targets any joint zero, while the latter uses the additional
all-real-threshold hypothesis and still needs higher-multiplicity
deflation. A bounded finite-region certificate and a uniform shrinking-
sector theorem have different coverage. No sector-wide collision
exclusion, new Newman bound, RH or novelty claim follows here.

The base manuscript and earlier project notes are preserved. Storage
follows [LARGE_FILES.md](../../../../LARGE_FILES.md); all new sources and
records are small, with no large data or snapshots.
