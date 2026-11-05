# RGD-B02 r3: boundary-matched Gaussian reference and a growth-scale stop

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6-astra / ultra**, chat0007,
thread `01a1a819-6502-7722-93b6-a63794209eda`.
Type **B**, activated by the author under [Handoff16][input].
[Review09][review] records proof-author/same-model checks; a separate
E04 r6 assessment is ready but unexecuted. No numerical work was run.

## 1. Return and classification

The one primary attempt is a **boundary-matched Gaussian source**, whose
coefficient determinant has an explicit positive margin at every size.
The residual is the complete signed difference from theta, with its
endpoint cancellations retained before any matrix comparison. This
avoids both a fixed finite-rank reference and Note10's polewise
triangle/Harnack payment. It nevertheless has a different, proved stop.

For every fixed M>0, on 1<=r<=M k as k tends to infinity, the absolute
ratio of the canonical determinant to this reference tends to zero;
its rth root also tends to zero, uniformly. Therefore the exact
preconditioned matrix residual cannot stay below any fixed delta<1.
Even the exact scalar determinant residual has relative magnitude
tending to one. This is a failure of **uniform positive relative slack
for this reference**, not a negative canonical determinant and not an
exclusion of every tolerance approaching one.

The single local adjustment adds a real quadratic logarithm while
preserving both boundary values. Every nonzero adjustment loses the
premise of nonnegative reference minors at all r,k: one of the two
edge families contains a negative minor. This does not exclude every
proportional subregion of that adjusted reference.

These are scoped analytical obstructions in the sense of
[avoid/01][a01] and [avoid/07][a07], not an RH-equivalent criterion
presented as progress. The identities and Gaussian reference margin
are standard algebra; no novelty claim is made. The quantitative gain
is the bound (9) on the actual determinant ratio and the resulting
necessary lower bound (12) on every induced-norm payment, without
separating the residual. The [result index][results], [control cluster12][controls]
and [avoid index][avoid], especially [12][a12] and [16][a16], govern scope.
No published zero certificate, global reality premise, or simplicity
assumption is used in this new argument.

## 2. Complete source and matching both Green boundary values

Retain [Note10][note10] and its accepted E04 r5 normalization:
\[
 C(z)=\int_0^\infty\Phi(u)\cosh(u\sqrt z)\,du
 =\tfrac18\xi((1+\sqrt z)/2)=\sum_{m\ge0}c_mz^m,
 \quad C(1)=b=\tfrac1{16},\quad c_m=0\ (m<0).
 \tag{1}
\]
The complete unit-weight infinite square source is unchanged. Its Green
primitive satisfies p''-p=8 Phi, p'(0)=-1/2, and
c0=b-d0/8, d0=integral p>0. Note10 (20) gives 1/32<c0<b.
Write E=C/c0 and e_m=c_m/c0, so E(0)=1. Set
\[
 t=\log(b/c_0)>0,\qquad
 C_G(z)=c_0e^{tz},\qquad
 \Phi_G(u)={c_0\over\sqrt{\pi t}}e^{-u^2/(4t)}.
 \tag{2}
\]
The elementary Gaussian integral gives the displayed transform of
Phi_G. Thus C_G(0)=c0 and C_G(1)=b exactly. Its boundary-compatible
primitive is
\[
 p_G(u)=8\int_u^\infty\sinh(v-u)\Phi_G(v)\,dv>0.
 \tag{3}
\]
Differentiating gives p_G''-p_G=8 Phi_G and
p_G'(0)=-8 C_G(1)=-1/2. Tonelli gives
integral p_G=8 integral (cosh v-1)Phi_G(v)dv=8(b-c0)=d0.
The comparison therefore matches c0, b and d0; it does not drop the
Green endpoint atom. The Gaussian is an auxiliary reference, not a
claim that the canonical square source has changed.

Put Delta E=(C-C_G)/c0. It is the transform of the entire signed
source difference (Phi-Phi_G)/c0, and
\[
 \Delta E(0)=\Delta E(1)=0,\qquad
 \varepsilon_m={1\over c_0(2m)!}\int_0^\infty
                (\Phi-\Phi_G)(u)u^{2m}\,du
             =e_m-{t^m\over m!}\quad(m\ge0).
 \tag{4}
\]
For m<0 set epsilon_m=e_m=0 and the Gaussian coefficient to zero.
Every theta mode and every source tail is present. No norm of either
source separately is used in the stop below.

## 3. A nonzero reference margin at every dimension

For r,k>=1 define real r-square matrices
\[
 A_{ij}=e_{k+j-i},\quad B_{ij}=g_{k+j-i},\quad
 g_m=\begin{cases}t^m/m!&m\ge0,\\0&m<0,\end{cases}
 \quad K=B^{-1}(A-B).
\]
The target is D_(r,k)=c0^r det A. Factor column j of B by
 t^(k+j)/(k+j)! and row i by t^(-i). The remaining entry is the
falling factorial (k+j)_(i). These are monic polynomials of degree i;
their evaluation determinant is the Vandermonde at k,k+1,...,k+r-1.
When i>k+j, that falling factorial is exactly zero, so this proof also
handles every negative-index entry. Consequently
\[
 m_{r,k}:=\det B
 =t^{rk}\prod_{j=0}^{r-1}{j!\over(k+j)!}>0,
 \qquad m_{r,k}\ge\left({t\over r+k}\right)^{rk}.
 \tag{5}
\]
The last inequality follows by bounding every factor in
(k+j)!/j! by r+k. This infinite-rank reference has no analogue of
Note10's fixed-N determinant vanishing.

The exact, correlated comparison is
\[
 {D_{r,k}\over c_0^r m_{r,k}}=\det(I+K).
 \tag{6}
\]
If an induced matrix norm obeyed ||K||<=delta<1, real homotopy would
give det(I+K)>0 and det(I+K)>=(1-delta)^r. Equation (6) alone is an
identity, not progress on its sign. The next section tests this
sufficient mechanism using the actual complete target, before choosing
any residual majorant.

## 4. Full-source growth and an explicit ratio upper bound

The accepted complete-source estimate in Note10 (18) is
Phi(u)<=4 pi^2 exp(9u-pi exp(4u)), u>=0. For R>0, put
alpha_R=(9+sqrt(R))/4. Substitution v=pi exp(4u), together with
cosh(sqrt(R)u)<=exp(sqrt(R)u), gives
\[
 E(R)\le {\pi^{2-\alpha_R}\Gamma(\alpha_R)\over c_0}
 < F(R):=32\pi^{2-\alpha_R}\Gamma(\alpha_R).
 \tag{7}
\]
This uses all modes and the already proved c0>1/32. It imports no
unproved canonical estimate. In particular log E(R)=O(sqrt(R)log R)
for R>=2. An elementary justification, requiring no asymptotic Gamma
formula, is Gamma(alpha)<=1+N! for N=ceil(alpha): use
v^(alpha-1)<=1+v^N and integrate against exp(-v). Thus log F(R) has
the same upper growth bound.

Since e_m>=0, e_m R^m<=E(R) for m>=0. Scale entry (i,j) of A by
R^(k+j-i). Its determinant becomes R^(rk)det A and each entry has
absolute value at most E(R); negative indices stay zero. Hadamard's
inequality yields
\[
 |\det A|\le r^{r/2}E(R)^rR^{-rk}.
 \tag{8}
\]
Combining (5) and (8), for every r,k>=1 and R>0,
\[
 \boxed{\left|{D_{r,k}\over c_0^r m_{r,k}}\right|
 \le U_{r,k}(R):=
 r^{r/2}E(R)^r\left({r+k\over tR}\right)^{rk}
 \le\overline U_{r,k}(R):=
 r^{r/2}F(R)^r\left({r+k\over tR}\right)^{rk}.}
 \tag{9}
\]
This is an upper bound on the actual determinant ratio. It is not a
lower bound on the determinant and is not based on independent
residual-entry errors. Although Hadamard loses cancellations, an upper
bound tending to zero suffices for the obstruction.

Fix M>0 and use the growing-index domain
\[
 k\longrightarrow\infty,\qquad1\le r\le Mk,
 \qquad R_k={k^2\over(\log k)^2}\quad(k\ge3).
 \tag{10}
\]
By choosing M sufficiently large, this covers any fixed positive
proportional ratio k/r, as well as r=k and k>r+1 in the dual
representation. A fixed M covers k/r>=1/M. It also includes fixed r.
No claim is made here about k fixed and r tending to infinity.
Equation (7) gives log F(R_k)=O(k). Since log(r+k)=log k+O_M(1)
and (log r)/k tends to zero uniformly in (10),
\[
 \log\overline U_{r,k}(R_k)
 \le-rk\log k+2rk\log\log k+O_M(rk),
 \quad \overline U_{r,k}(R_k)^{1/r}\longrightarrow0
 \quad\hbox{uniformly in (10)}.
 \tag{11}
\]
Constants may depend on the fixed source, t and M, not r or k.
No numerical cutoff is asserted or sought.

## 5. The exact premise that fails, and its limits

For any induced matrix norm, (6) and (9) imply
\[
 \boxed{\|K\|\ge1-\overline U_{r,k}(R_k)^{1/r}.}
 \tag{12}
\]
If ||K||<1, every eigenvalue of I+K has modulus at least 1-||K||,
so |det(I+K)|>=(1-||K||)^r; (12) follows. If ||K||>=1 it is
immediate. Thus no payment of the **exact complete K** can establish
||K||<=delta_*<1 uniformly on (10). This is stronger than failure of
a particular triangle estimate. Invertible simultaneous row/column
scalings change B^(-1)A by similarity, leaving the determinant and
spectral obstruction intact.

Also, directly from (9)--(11),
\[
 {\det A-m_{r,k}\over m_{r,k}}\longrightarrow-1,
 \qquad { |\det A-m_{r,k}|\over m_{r,k}}\longrightarrow1.
 \tag{13}
\]
No scalar comparison with a fixed relative slack epsilon>0,
|det A-m|<=(1-epsilon)m, can hold throughout (10).
A tolerance approaching one is **not excluded**. But once |det A|<m,
the strict inequality |det A-m|<m is equivalent to det A>0. Merely
asking for that shrinking slack would restate the target under
[avoid/01][a01]; it needs an independently proved signed estimate.

The scale diagnostic is quantitative. Even if the exponential slope
were allowed to vary, any fixed ||K||<=delta<1 on (10) would require,
by (9),
\[
 t_{r,k}\le {r+k\over R_k(1-\delta)^{1/k}}
               r^{1/(2k)}E(R_k)^{1/k}
          =O_{M,\delta}\!\left({(\log k)^2\over k}\right).
 \tag{14}
\]
This necessary vanishing scale is incompatible with retaining both
C_G(0)=c0 and C_G(1)=b within the single-exponential family, which fixes
t=log(b/c0)>0. Equation (14) is a diagnostic of this family, not a
second reference attempt or a sufficient condition for a moving reference.

## 6. The one localized adjustment: a quadratic logarithm

Allow one real quadratic correction while preserving the same two
normalizations:
\[
 E_2(z)=\exp\big((t+q/2)z-qz^2/2\big),\quad
 C_2=c_0E_2,\quad q\in\mathbb R.
 \tag{15}
\]
Then E_2(0)=1 and C_2(1)=b. To match the first canonical coefficient
as well, choose q=2(e1-t). No sign or nonzero claim about that canonical
number is needed for the following complete dichotomy.

If q>0, E_2(x) tends to zero as x tends to positive infinity. If all
Taylor coefficients were nonnegative, its constant coefficient one
would force E_2(x)>=1. Hence some e_j^[2]<0 and the reference minor
D^[2]_(1,j)=c0 e_j^[2] is negative.

If q<0, the exact dual generating function
H_2(z)=1/E_2(-z)=exp((t+q/2)z+qz^2/2) tends to zero on the positive
axis. Some h_j^[2]<0. Note10's purely algebraic duality, with zero
negative indices, gives D^[2]_(j,1)=c0^j h_j^[2]<0.
For q=0 this is the unchanged Gaussian reference and Section 5 applies.

Thus a nonzero real quadratic correction cannot supply a nonnegative
reference at **all** r,k. The failed premise is universal reference
positivity; the witnesses are in edge families. This does not prove
failure of every proportional-index subset, exclude all polynomial or
nonpolynomial reference constructions, or say anything negative about
the canonical theta determinants. The permitted local adjustment is
exhausted; no higher-degree repair is attempted.

## 7. Controls and evidence discipline

A strict-positive control makes the distinction in Section 5 explicit.
For ell>0 set
\[
 C_*(z)={\cosh(\ell\sqrt z)\over16\cosh\ell},\quad
 c_{*,0}={1\over16\cosh\ell},\quad
 t_*=\log\cosh\ell>0.
 \tag{16}
\]
This has the same b=1/16 and growth no larger than used in Section 4.
The checked [DLMF product 4.36.2][dlmf] gives
E_*(z)=prod_(j>=1)(1+x_j z), x_j=4ell^2/((2j-1)^2 pi^2)>0.
Every rectangular determinant is strictly positive. An elementary
proof avoids assuming RH or a strict-PF theorem: for a finite product,
the upper Toeplitz matrix is a product of upper bidiagonal I+x_j S
matrices, all of whose minors are nonnegative. In Cauchy--Binet for
rows 0,...,r-1 and columns k,...,k+r-1, shift the full row block by one
in each of the first k factors and use identity choices thereafter.
That term is (x1...xk)^r>0. For at least k factors all other terms are
nonnegative; passing to the locally convergent product preserves this
strict lower bound. A finite matrix of size r+k suffices throughout.
Using its direct cosh growth in place of the theta-specific F in (7),
the same Gaussian-reference ratio and uniform-slack stop apply.
So that stop is compatible with positivity of every target determinant.

This control is the atomic source c_*,0 delta_ell, not smooth canonical
theta. Its distributional Green primitive
p_*(u)=8 c_*,0 sinh(ell-u) for 0<=u<=ell, and zero otherwise, has
p_*'(0)=-1/2 and the
same boundary relation. It is a positive-reference control, not a
certified positive-time collision.

The inherited [Gaussian-mixture finite-prefix control in Note10][note10]
remains relevant: any prescribed finite real-simple prefix may coexist
with nonreal zeros farther away. An all-radius real-simple prefix would
assume RH plus simplicity. Neither is used to construct (2).
The repository collision screen is retained with its exact-source limits:

| Family in cluster12 | Canonical-application premise absent |
| --- | --- |
| Euler-factor shifted sources | Unmodified unit-weight theta source/Dirichlet coefficients |
| Weighted-square and finite-source controls | Complete infinite unit-weight square sum and full reflection |
| Reflected super-Gaussian; smooth positive-primitive controls | Canonical arithmetic square expansion |
| Finite-prime orbit and finite-profile controls | Complete source identity rather than selected profiles or identities |
| BW-01 atom controls | Smooth canonical source and complete profile |
| RH-conditional endpoint controls | Ordinary theta Dirichlet-series arithmetic |
| Fixed-amplitude variable-kernel controls | The actual cosh/cosine transform equation |

These source differences do not establish that a quantitative inequality
fails on each control. Positive-time collisions are not counterexamples
to arbitrary time-zero finite inequalities. The present stop concerns a
reference/payment class and is intentionally reproduced by (16), whose
time-zero determinants are all positive. No collision-control numerics
or finite zero-prefix tests were run.

## 8. Disposition and continuation

**RGD-B02 r3 complete as a scoped conceptual return.** One primary
reference and one localized adjustment were investigated. The primary
has a nonzero margin in growing dimension and a fully correlated
residual, but its uniform relative-slack premise provably fails. The
local correction fails universal reference positivity. No paid positive
growing-index induction step, new theta positivity range, or all-index
result has been obtained. Park this Gaussian/quadratic-reference attempt.

**Next: [E] RGD-E04 r6 — Sol**, the bounded analytical assessment in
[Packet17][packet17]. It checks this fixed proof and its scope; it does
not acquire moments, optimize thresholds, test more zeros, or select
another mechanism. [Handoff18][guide] gives model-change and chat
continuity instructions. After assessment, any proposed B02 r4 must
first address the growth mismatch with a different reference or an
independently controlled signed residual; no such candidate or research
activation is asserted here. Earlier notes and frozen handoffs remain
unchanged. This is no manuscript milestone or investigation closure.

[input]: ../research-progress/handoffs/16_RGD_E04_R5_RETURN_AND_MODEL_CONTINUATION_20261104.md
[note10]: 10_RGD_B02_R2_RECIPROCAL_POLE_INDUCTION_AND_SCOPED_STOP_20261104.md
[review]: ../reviews/09_RGD_B02_R3_AUTHOR_AND_SAME_MODEL_CHECKS_20261104.md
[packet17]: ../research-progress/handoffs/17_RGD_E04_R6_GAUSSIAN_REFERENCE_ASSESSMENT_20261104.md
[guide]: ../research-progress/handoffs/18_RGD_B02_R3_RETURN_AND_MODEL_CONTINUATION_20261104.md
[dlmf]: https://dlmf.nist.gov/4.36.E2
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
