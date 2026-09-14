# Sphere and Schur quantization: first concrete pairing tests

14 September 2026. **Focused working note**, following the
[broad defect-observable survey](DEFECT_OBSERVABLE_SURVEY.md).
This compares specific protected sectors and source prescriptions. It is
not a draft paper and does not select a final RH candidate.

The new results are explicit source tests: the real Gaussian boundary
sector gives the quarter-shift gamma factor and the gamma mass spectrum;
raising-operator states in the interacting rank-one sphere model have a
computable non-geometric Gram matrix; an elementary Schur difference
identity gives a local Euler factor, while its actual state overlaps have
different repetition coefficients. The full conformal Schur benchmark
also has a computable positive electric-sector pairing. These statements
identify which preparations deserve further work, without introducing a
program of residual estimates.

## 1. Target, scope, and benchmark systems

Use the conventions of [the foundational analysis](ANALYSIS.md). For
\(F=E_Lf\), \(f\in C_c^\infty(I_L)\), \(I_L=(-L/2,L/2)\), set

\[
\begin{split}
Q_L[f]={}&\frac1{2\pi}\int_{\mathbb R}
\bigl[b_{1/4}(\tau^2)+w_0\bigr]|\widehat F(\tau)|^2\,d\tau
+P_L[f]\\
&-2\sum_{m\log p<L}(\log p)p^{-m/2}
\operatorname{Re}\langle F,U_{m\log p}F\rangle,\\
b_{1/4}(\tau^2)={}&\sum_{n\geq0}\frac{2}{a_n}
\frac{\tau^2}{a_n^2+\tau^2},\qquad a_n=2n+\tfrac12,\\
w_0={}&\psi(\tfrac14)-\log\pi,\\
P_L[f]={}&2\left|\int f(x)\cosh(x/2)\,dx\right|^2
-2\left|\int f(x)\sinh(x/2)\,dx\right|^2.
\end{split}
\tag{1}
\]

Here \(\widehat F(\tau)=\int e^{-i\tau x}F(x)\,dx\) and
\(U_dF(x)=F(x-d)\). A match means the **whole** expression (1) is the
norm of an independently specified, complex-linear preparation, with
compatibility as \(L\) increases. The theory's construction may remain
a credible, explicit hypothesis. Its arithmetic covariance may not be
inserted among those hypotheses.

| Benchmark | Purpose of this calculation | What is not being assumed |
|---|---|---|
| 3D free hypermultiplet, real Gaussian boundary module | Fix the Mellin normalization and identify the gamma factor and oscillator levels. | That the Gaussian state's norm is the Weil form. |
| 3D \(T[SU(2)]\), the \(U(1)\) theory with two hypermultiplets | Compute an interacting protected pairing and test repeated charged insertions. | That the raising generator is an arithmetic prime-return operator. |
| 4D \(SU(2)\), \(N_f=4\), Schur sector | Test an explicit conformal theory, its Wilson-sector norm, and its full spherical-vector difference equation. | That one selected matter factor represents the complete gauge-theory norm. |
| Elementary Schur \(q\)-Weyl sector | Compute the simplest common-state interference and compare a shift identity with a physical overlap. | That this effective abelian example alone supplies a complete UV construction or the full conformal benchmark. |

The two interacting benchmarks are different theories. No direct
dimensional reduction identifying \(T[SU(2)]\) with the four-flavour 4D
theory is asserted. A proposed interface between systems needs its own
definition and pairing identity.

Sphere and Schur quantization use the positive pairing
\(T(\rho(a)b)\) discussed in the survey. On the algebraic core, left and
right actions satisfy \(R_a^\dagger=L_{\rho(a)}\); \(\rho\) is an
antilinear algebra automorphism, not an arbitrary replacement for the
physical adjoint. An unbounded closure, an infinite insertion series, or
a distributional boundary state needs a separate domain argument.

## 2. Sphere quantization: the real boundary module fixes the gamma data

### 2.1 The actual Gaussian state and its pairing

The real boundary module in Gaiotto's §§7.2–7.3 is the Schrödinger
representation. In oscillator units take

\[
\mathcal H_{\mathbb R}=L^2(\mathbb R,dy),\quad
X=y=X^\dagger,\quad P=\partial_y=-P^\dagger,\quad
\Omega(y)=\pi^{-1/4}e^{-y^2/2}.
\tag{2}
\]

The relevant boundary construction and its Mellin interpretation are
described in [Gaiotto, §§7.2–7.3](https://arxiv.org/html/2307.12396#S7.SS2).
We compute with the explicitly normalized real representation (2),
rather than importing normalization constants from distributional
hemisphere formulas.

The dilation group is
\(D_r\psi(y)=e^{r/2}\psi(e^r y)\). Direct Gaussian integration gives

\[
\langle\Omega,D_r\Omega\rangle=(\cosh r)^{-1/2}.
\tag{3}
\]

On even states the unitary logarithmic-coordinate map is
\((\mathcal U\psi)(u)=\sqrt2 e^{u/2}\psi(e^u)\). Fourier transformation
with the unitary factor \((2\pi)^{-1/2}\) gives

\[
(\mathcal M\Omega)(\tau)
=2^{-3/4-i\tau/2}\pi^{-3/4}
\Gamma(\tfrac14-i\tau/2).
\tag{4}
\]

Indeed, substitute \(s=1/2-i\tau\) into
\(\int_0^\infty y^{s-1}e^{-y^2/2}\,dy
=2^{s/2-1}\Gamma(s/2)\), the gamma integral after \(y^2/2=t\).
[Gamma integral](https://dlmf.nist.gov/5.2.E1)

Consequently the natural dilation preparation
\(\Phi(f)=\int f(r)D_r\Omega\,dr\) has the exact positive norm

\[
\|\Phi(f)\|^2=\int_{\mathbb R}\rho_{\rm G}(\tau)
|\widehat f(\tau)|^2\,d\tau,\qquad
\rho_{\rm G}(\tau)=
\frac{|\Gamma(\tfrac14+i\tau/2)|^2}{2^{3/2}\pi^{3/2}}.
\tag{5}
\]

The density integrates to one. This supplies the correct quarter-shift
without choosing a tunable gamma parameter. But (5) has an exponentially
decaying spectral density and the smooth kernel (3); it is not (1).
This is the complete answer for this preparation, not a reference form
whose discrepancy we propose to estimate.

### 2.2 The same module gives the gamma tower, with a precise limitation

The positive oscillator
\(H_{\rm osc}=\tfrac12(-\partial_y^2+y^2)\), restricted to even states,
has eigenvalues \(2n+1/2=a_n\). Thus

\[
b_{1/4}(\tau^2)=
2\operatorname{Tr}_{\mathcal H_{\rm even}}
\left[H_{\rm osc}^{-1}
\frac{\tau^2}{H_{\rm osc}^2+\tau^2}\right].
\tag{6}
\]

This identifies the previously used positive gamma tower with a standard
Hamiltonian in a named boundary module. For example, the diagonal
Hilbert–Schmidt source with entries
\(\sqrt{2/a_n}\,i\tau/(a_n+i\tau)\,\widehat F(\tau)\)
has the gamma norm after integration with \(d\tau/(2\pi)\).
For smooth compactly supported inputs this source has finite norm.

Equation (6) does **not** derive that resolvent-weighted source as a
particular QFT insertion. The choice of source and its physical gluing
interpretation remain work to do. This is an interpretation of the
classical positive tower, not a novelty claim for its factorization.

The associated archimedean phase, with the standard Tate/Fourier
normalization and the orientation specified here, is

\[
S_\infty(\tau)=\pi^{-i\tau}
\frac{\Gamma(\tfrac14+i\tau/2)}{\Gamma(\tfrac14-i\tau/2)},
\qquad |S_\infty(\tau)|=1.
\]

Its derivative is

\[
-i\overline{S_\infty}S_\infty'
=\operatorname{Re}\psi(\tfrac14+i\tau/2)-\log\pi
=b_{1/4}(\tau^2)+w_0.
\tag{7}
\]

The last equality follows from the
[digamma partial fractions](https://dlmf.nist.gov/5.7.E6).
The scalar \(\pi^{-i\tau}\) changes the contact term and must be retained.
The derivative in (7) is negative at zero, whereas a norm is nonnegative.
Unitarity of this phase does not prove positivity of its derivative.

This recovers the familiar archimedean local-factor mechanism in a
specific supersymmetric boundary setting. The existing
[arithmetic-weight comparison, §§6–7](../../../brainstorm/theory-landscape-20260913/SELECTION_TESTS.md)
already distinguishes the positive weight from its signed logarithmic
derivative. The boundary interpretation is useful; it does not remove
that distinction or establish equality with the canonical semilocal
positive pairing.

## 3. The interacting sphere benchmark: exact charged-state norms

For \(T[SU(2)]\) and real FI parameter \(t\), use its realization on
twisted half-densities on \(\mathbb CP^1\). In one coordinate chart the
raising generator and normalized spherical vector can be written

\[
E=\partial_z,\qquad
\Omega_t(z)=(1+|z|^2)^{-1+it},\qquad d\mu=d^2z/\pi.
\tag{8}
\]

Here \(\|\Omega_t\|=1\). Multiplying the vector by
\(\Gamma(1-it)\) restores the partition-function normalization
\(Z_t=\pi t/\sinh\pi t\), with \(Z_0=1\).
These model data come from
[Gaiotto, §3.2](https://arxiv.org/html/2307.12396#S3.SS2).

Repeated differentiation gives

\[
E^n\Omega_t=(-1)^n(1-it)_n\bar z^{\,n}
(1+|z|^2)^{-1+it-n}.
\]

Angular integration makes distinct powers orthogonal. The radial beta
integral evaluates the diagonal entries exactly:

\[
\begin{split}
\langle E^m\Omega_t,E^n\Omega_t\rangle
&=\delta_{mn}N_n(t),\\
N_n(t)&=\frac{(n!)^2}{(2n+1)!}\prod_{k=1}^{n}(k^2+t^2).
\end{split}
\tag{9}
\]

To see the second line, put \(u=|z|^2\). The remaining integral is
\(\int_0^\infty u^n(1+u)^{-2n-2}\,du
=(n!)^2/(2n+1)!\). The original trace normalization multiplies every
entry in (9) by the same \(Z_t\).

This computes a whole infinite family of interacting protected norms.
It also answers a specific prime-return proposal:

- The vacuum return \(\langle\Omega_t,E^n\Omega_t\rangle\) is zero
  for every \(n>0\), by charge conservation.
- Interpreting the norms of repeated insertions as geometric returns
  fails as well. Their ratios are

\[
\frac{N_{n+1}(t)}{N_n(t)}
=\frac{(n+1)^2((n+1)^2+t^2)}{(2n+3)(2n+2)}.
\tag{10}
\]

In particular the second ratio exceeds the first by
\((19+t^2)/30>0\). Multiplying \(E\) by a constant cannot make these
ratios equal. Neither real FI tuning nor overall trace normalization
repairs the geometric-repetition prescription.

This rules out **bare repeated charged insertions as the proposed
returns**, not the theory. A source with coefficients \(c_n(f)\) in
these states has norm \(\sum_n N_n(t)|c_n(f)|^2\), on the domain where
the sum converges. Its arithmetic identification would have to come
from an independently defined coefficient map. Mixed charged/neutral
operators, vortex modules, and gluing kernels are different prescriptions
and remain available.

## 4. Schur quantization: complete norms versus local factor identities

### 4.1 A conformal benchmark with an explicit positive electric sector

Take the \(SU(2)\), \(N_f=4\) theory, real \(0<q<1\), and trivial
flavour fugacities. Write \((a;Q)_\infty=\prod_{j\geq0}(1-aQ^j)\).
In the electric sector, the Wilson generator acts as
\(W=2\cos\theta\). Specializing the spherical-vector norm in
[Gaiotto–Teschner, §5.1.5](https://arxiv.org/html/2406.09171#S5.SS1.SSS5)
gives the normalized measure

\[
d\nu_q(\theta)=\frac{\omega_q(\theta)}{Z_q}\frac{d\theta}{2\pi},
\quad
\omega_q(\theta)=4\sin^2\theta\,
\frac{|(q^2e^{2i\theta};q^2)_\infty|^4}
{|(-qe^{i\theta};q^2)_\infty|^{16}},
\quad Z_q=\int_0^{2\pi}\omega_q(\theta)\frac{d\theta}{2\pi}.
\tag{11}
\]

This measure is finite and positive. Normalization by \(Z_q\) is stated
explicitly to set the vacuum norm to one; any matching theorem must
also determine the physical overall normalization.

For the natural Wilson preparation \(a_f(W)=\int f(x)e^{ixW}\,dx\),
defined by bounded functional calculus on this sector, the complete
pairing is

\[
B_q(f,g)=\int_0^{2\pi}
\overline{\widehat f(-2\cos\theta)}\,
\widehat g(-2\cos\theta)\,d\nu_q(\theta).
\tag{12}
\]

Its input kernel is \(C_q(r)=\int e^{2ir\cos\theta}\,d\nu_q(\theta)\),
an entire function of \(r\). Thus this prescription cannot reproduce
the separated prime delta terms, or the unbounded gamma form. This
uses the actual norm of a named conformal model. It makes no claim
about preparations involving unbounded magnetic insertions or an
infinite family of line operators.

### 4.2 An elementary shift produces the correct local repetition series

Consider the elementary Schur factor

\[
\chi_q(v)=(-qv;q^2)_\infty^{-1},\qquad
\frac{\chi_q(q^2v)}{\chi_q(v)}=1+qv.
\tag{13}
\]

This is the quantum-dilogarithm factor appearing in the elementary
\(q\)-Weyl example; see the spectrum generator in
[Gaiotto–Teschner, RG flow, §3.1.1](https://arxiv.org/html/2503.16685#S3.SS1.SSS1).
The second identity follows directly by cancelling the infinite products.

Now make the **trial arithmetic identification**
\(q=p^{-1/2}\), \(v=-e^{i\tau d}\), \(d=\log p\), and put
\(J_p(\tau)=1-p^{-1/2}e^{i\tau\log p}\). Then

\[
2\operatorname{Im}\partial_\tau\log J_p(\tau)
=-2(\log p)\sum_{m\geq1}p^{-m/2}\cos(m\tau\log p).
\tag{14}
\]

The series converges absolutely. It has the exact coefficient for every
repetition, including the distinction between the primitive coefficient
\(\log p\) and the repeated length \(m\log p\). For \(p=2\), its first
two terms have coefficients \(-2\log2/\sqrt2\) and \(-\log2\).

The unshifted \(\log\chi_q\) contains the extra factor
\((1-q^{2m})^{-1}\) in its coefficients. It is precisely the ratio in
(13) that removes this descendant factor. Keeping this distinction is
essential when assigning an observable to the Euler factor.

There are three unresolved identification issues, not error estimates:

1. Equation (14) is a phase derivative, not a norm. It does not make
   the Schur factor itself an RH-positive observable.
2. Choosing a different \(q=p^{-1/2}\) for every prime changes the
   quantization parameter. It is not a construction within one fixed
   field theory. A fixed \(q\) with integer powers cannot simultaneously
   implement \(q^{k_2}=2^{-1/2}\) and \(q^{k_3}=3^{-1/2}\): that would
   imply \(2^{k_3}=3^{k_2}\). Continuous defect parameters or other
   correspondences are not excluded, but have not been supplied here.
3. In the full four-flavour benchmark, the spherical vector has the
   massless shift ratio

\[
\frac{\varphi_0(q^2v)}{\varphi_0(v)}
=\frac{(1+qv)^8}
{(1-v^2)(1-q^2v^2)^2(1-q^4v^2)}.
\tag{15}
\]

Equation (15) is obtained by specializing the same spherical vector
used in (11). It includes all matter and vector factors. Extracting
one numerator factor and discarding the others is not a calculation
of the complete theory's pairing. Physical \(q\)-shifts also act on
magnetic flux and analytically continued holonomy; the substitution
in (14) is not a proof that they translate a real spacetime coordinate.

### 4.3 A useful improvement: the RG map retains the common positive state

The 2025 paper on Schur RG flow supplies a more suitable formulation for
the next matching calculation. With charge lattice \(\Gamma\), the
quantum torus has

\[
X_\gamma X_\eta=q^{\langle\gamma,\eta\rangle}X_{\gamma+\eta}.
\]

Its formulation transports a UV line \(a\) to a framed expansion
\(F_a\) and a common spectrum-generator state \(\mathscr S\). The
pairing takes the form

\[
I(a,b)=c_q\langle F_a\mathscr S,F_b\mathscr S\rangle_{\ell^2(\Gamma)},
\qquad c_q=(q^2;q^2)_\infty^{2r}>0.
\tag{16}
\]

The same \(\mathscr S\) corrects both the dualization map and the
pairing. The general construction includes conjectural input and
domain conditions; formal series alone do not guarantee finite norms.
[Gaiotto–Teschner, RG flow, §§1–2](https://arxiv.org/html/2503.16685)

This is especially relevant to the present objective: (16) retains
normalization and all interference within one state. For a linear
arithmetic source, the target would be
\(c_q\|F_{a(f)}\mathscr S\|^2=Q_L[f]\). An isometric change of
description does not repair an already mismatched source; its value
here is to make the full pairing computable for new source choices.

### 4.4 Exact common-state calculation in the elementary sector

We can test that distinction without conjecturing an arithmetic source.
Restrict the elementary spectrum generator to its one charge ray and
use \(\ell^2(\mathbb Z)\), with bilateral shift \(Xe_n=e_{n+1}\).
Omit the known common positive factor \(c_q\) for the moment. Set

\[
\mathscr S=\sum_{n\geq0}c_ne_n,\qquad
c_n=\frac{(-q)^n}{(q^2;q^2)_n},\qquad
Z=\sum_{n\geq0}|c_n|^2<\infty.
\tag{17}
\]

This is the Fourier-series realization of the same \(\chi_q\) as in
(13), not a separately chosen metric. The coefficient recurrence is

\[
(1-q^{2n})c_n=-q c_{n-1},\qquad n\geq1.
\tag{18}
\]

It yields an explicit **whole norm with interference**:

\[
\begin{split}
\|(1+qX)\mathscr S\|^2
&=(1+q^2)Z+2q\operatorname{Re}\langle\mathscr S,X\mathscr S\rangle\\
&=\sum_{n\geq0}q^{4n}|c_n|^2.
\end{split}
\tag{19}
\]

Both expressions are exact: in the last line each coefficient of
\((1+qX)\mathscr S\) is \(q^{2n}c_n\). Thus the negative cross term
and the contact are already tied by the trace data.

The actual normalized repeated overlap nevertheless differs from the
isolated factor in (14). Put
\(r_m=(-1)^m\langle\mathscr S,X^m\mathscr S\rangle/Z\). Then

\[
r_m=\frac{q^m}{Z}\sum_{n\geq0}
\frac{|c_n|^2}{\prod_{j=1}^{m}(1-q^{2(n+j)})}
>q^m\qquad(m\geq1).
\tag{20}
\]

The strict inequality follows term by term, with positive summands.
All sums converge because \((q^2;q^2)_n\) tends to a nonzero limit.
This is an exact exclusion of the prescription “identify this state
overlap with the prime return”; no estimate of an infinite residual
is needed. It also shows why reading the repetition law from one
functional equation would have given the wrong physical pairing.

The example is an abelian protected-sector control. It does not prove
that the elementary effective theory has the desired global UV
construction, or that (17) is the state of the four-flavour theory.
Its value is an explicit, independently positive common-state calculation
that the richer theory can be compared against.

## 5. What these results change in the research plan

### 5.1 A useful exclusion about source regularity

Any preparation \(f\mapsto\int_{I_L}f(x)U_x\Omega\,dx\), with
\(U_x\) unitary and \(\Omega\) a fixed finite-norm vector, is a bounded
map from \(L^2(I_L)\) into the physical Hilbert space. In contrast, for
fixed nonzero \(\chi\in C_c^\infty(I_L)\),

\[
Q_L[\chi(x)e^{iNx}]/\log N\longrightarrow\|\chi\|^2.
\tag{21}
\]

This follows from \(b_{1/4}(\tau^2)\sim\log|\tau|\), the rapid decay
of \(\widehat\chi\), and the fixed-interval boundedness of the remaining
terms of (1). It explains the failure of (5) and (12) in a common way.
Exact realization needs a source unbounded relative to this input
\(L^2\) norm, such as a controlled infinite insertion family or a
distributional preparation with finite output on smooth tests. This
does not obstruct QFT: local fields are themselves distributions.

This is a source-selection statement. It neither requires a globally
closed factor on the union of all intervals nor rules out interacting
boundary/defect sectors. The global closability restriction in the
[earlier selection tests](../../../brainstorm/theory-landscape-20260913/SELECTION_TESTS.md)
still applies to claims of that stronger kind.

### 5.2 The local-factor bridge is exact, but it is not the new theorem

For a finite prime set \(\mathcal P\), put
\(S_p=J_p/\overline{J_p}\) and
\(S_{\mathcal P}=S_\infty\prod_{p\in\mathcal P}S_p\).
Equations (7) and (14) give

\[
-i\overline{S_{\mathcal P}}S_{\mathcal P}'
=b_{1/4}(\tau^2)+w_0
-2\sum_{p\in\mathcal P,m\geq1}(\log p)p^{-m/2}
\cos(m\tau\log p).
\tag{22}
\]

If \(\mathcal P\) contains the primes below \(e^L\), integrating (22)
against \(|\widehat F|^2/(2\pi)\) and adding \(P_L[f]\) gives (1).
Inactive repetitions vanish by support. No all-prime Euler product
on the critical line has been used.

This is the phase version of the previously recorded logarithmic-weight
identity. Multiplication by \(S_{\mathcal P}\) is unitary, but its phase
derivative is negative at \(\tau=0\). The signed pole form also remains
outside it. Repackaging these classical local factors is not a new Weil
positivity proof or the promised constructive-QFT reduction.

The useful new question is whether a specified defect module or RG
gluing construction converts the *complete* expression, including the
poles, into a pairing such as (16). Simply choosing a covariance equal
to (1), or transporting the canonical semilocal norm without proving
equality, would assume or repeat the missing step.

### 5.3 Recommended next calculation and stopping conditions

Keep **sphere boundary modules and Schur RG/gluing pairings** as the two
leading directions. The explicit normalizable-state smearing and bare
repetition prescriptions tested here should not be pursued further.

| Direction | Concrete next object | Evidence needed before specializing a paper |
|---|---|---|
| Sphere quantization | A boundary or vortex module in the rank-one gauge theory, with an infinite operator source whose real adjoint and Mellin action are explicit. Keep the real Gaussian/oscillator module as the normalization control. | A derived source rule and full reflected pairing; prime operations must arise from actual correspondences rather than assigning arbitrary coefficients to an orthogonal basis. |
| Schur quantization | The \(SU(2)\), \(N_f=4\) framed line expansions and common spectrum generator in the RG description, allowing magnetic/electric interference and specified interface states. | One fixed theory and quantization parameter, a source in the domain of (16), and a calculation including every vector/matter factor and the pole normalization. |

Use \(L=1\) for the first prime, \(L=5/4\) for the two-prime test,
and \(L=3/2\) to include the first repetition of 2. A result at one
interval is preliminary evidence, not the all-support implication.
At each stage compute the whole proposed norm and compare identities;
if it fails, change the observable prescription or the system.

The RG formulation is the strongest new computational lead for the
arithmetic part because it retains one common state. The sphere boundary
module gives the clearest archimedean control. Neither has yet supplied
the required arithmetic source or a matched first-prime pairing.
Boundary Liouville, integrable defects, gauge networks, and the other
systems in the broad survey remain alternatives. A system-specific
paper should wait for a more substantive match than the classical
gamma/Euler-factor identities above.

## 6. Reproduction and status

The [check program](../numerics/check_sphere_schur.py) and
[small record](../numerics/records/sphere-schur-checks.json) test the finite
algebra used in (9)–(10), (13), (15), and (18)–(20). The program retains
the finite-product end factors and finite-vector boundary coefficient;
it does not silently treat a truncation as an infinite identity.
Its floating-point overlap illustration is separately labelled.

The Gaussian/Mellin integral, beta integral, infinite-product convergence,
and source-regularity arguments are written calculations. The checks
are not an analytical proof verifier, a construction of an interacting
QFT, or a Weil positivity certificate. The general Schur RG framework's
conjectural hypotheses are not promoted to unconditional theorems here.
