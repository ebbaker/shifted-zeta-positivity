# First approach to selective loss through Schur completion

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and reasoning effort are not exposed
and are not inferred. This is a bounded internal derivation, not independent
specialist refereeing. Three separate same-model agents checked the algebra,
head selection, source domains, and residual lifting. A small exact source
covariance calculation accompanies the derivation; it does not compute a
Sonin correction or certify global loss growth.

Repository baseline: `5052fc961dc755718f2cf88516e78096eb9e8edf`.
The existing uncommitted research was preserved. This note belongs to the
[selective loss program](overview.md), whose first approach is active.

The new concrete target is a full-complement certificate whose allowance
on the translated sum source is polynomial, even if its allowance on
other directions is large. The derivation identifies the exact finite
matrices and residual energies to estimate. It supplies no growing
window bound on them.

**Continuation status:** the
[complement and parity audit](02_complement_obstruction_and_parity_20261003.md)
shows that nonnegative endpoint-profile tails on an unbounded family are
already RH-equivalent. Their safety cannot be an assumed preliminary.
The conditional algebra below remains valid. The
[centered dual energy construction](03_centered_dual_energy_20261003.md)
provides a positive-main alternative with an explicit adverse response
and an independently positive reference metric.

## 1. Hypotheses and domains

Fix a finite prime set S and a support interval I of length L. Let H_src be the
closed L2(I) kernel of the three prescribed moments. On this Hilbert space use
the previously established positive selfadjoint source operator B with
B >= beta I, beta > 0, logarithmic form domain V = D(B^(1/2)), and bounded
selfadjoint correction K. Set

\[
H=B^{-1/2}KB^{-1/2},\qquad v=B^{1/2}F.
\]

H is bounded, compact, and selfadjoint. The exact form identity is

\[
q_{S,L}[F]=\langle v,(I-H)v\rangle,
\qquad F\in\mathcal V.
\tag{1}
\]

Only after S captures every active prime does q_(S,L) identify with the full
pole-neutral arithmetic Q. No fixed-S assertion is substituted for the
support-adapted growing family.

Choose an orthonormal finite head U0:C^m -> H_src, with projection E=U0 U0*,
and require Ran U0 contained in V. Write P=I-E. Decompose

\[
c=U_0^*v,\quad v_1=(I-E)v,\quad H_{00}=U_0^*HU_0,
\quad G=(I-E)HU_0,
\]
\[
D=I_{E^\perp}-(I-E)H(I-E),\qquad A_{00}=I_m-H_{00}.
\]

The substantive complement hypothesis is a full-space bound

\[
D\ge\delta I_{E^\perp},\qquad \delta>0.
\tag{2}
\]

A tested finite complementary matrix is insufficient. The bound must include
the entire source complement. No positivity of the finite head is assumed.

## 2. Exact full-domain Schur completion

Let

\[
S=A_{00}-G^*D^{-1}G.
\tag{3}
\]

Since D is bounded and boundedly invertible on E-perp, direct expansion gives
on all of V

\[
q_{S,L}[F]=
\|D^{1/2}(v_1-D^{-1}Gc)\|^2+\langle c,Sc\rangle.
\tag{4}
\]

Consequently

\[
q_{S,L}[F]=P_S[F]-\mathcal L_S[F],
\]
\[
P_S[F]=\|D^{1/2}(v_1-D^{-1}Gc)\|^2
          +\langle c,S_+c\rangle\ge0,
\quad \mathcal L_S[F]=\langle c,S_-c\rangle\ge0.
\tag{5}
\]

This clips only the finite signed Schur response after the full mixed term has
been retained. It does not demand S >= 0. Because Ran U0 is contained in V,
c_j=<B^(1/2)u_j,F>, so the loss is a bounded finite-rank source form on L2.
The positive form P_S=q_(S,L)+loss is closed on V: it is a bounded finite-rank
perturbation of the existing closed semibounded source form B-K.

## 3. Arbitrary tail-response columns and an exact energy enclosure

Take any finite-column map Y:C^m -> E-perp and define its full residual

\[
R=G-DY.
\tag{6}
\]

No Galerkin orthogonality or exact solve is required. The exact matrix energy
identity is

\[
G^*D^{-1}G=T_Y+R^*D^{-1}R,
\quad T_Y=G^*Y+Y^*G-Y^*DY.
\tag{7}
\]

Indeed this follows by substituting G=DY+R and expanding. T_Y itself need not
be nonnegative; retaining its signed entries is essential. With
S_Y=A00-T_Y, (2) gives the finite matrix enclosure

\[
S_Y-\delta^{-1}R^*R\ \le S\ \le S_Y.
\tag{8}
\]

The residual Gram R*R is the full Hilbert-space Gram of the actual residual
columns. Dropping components outside tested rows invalidates (8).

For any certified Hermitian lower matrix M <= S, (4) implies

\[
q_{S,L}[F]\ge
\|D^{1/2}(v_1-D^{-1}Gc)\|^2
+\langle c,M_+c\rangle-\langle c,M_-c\rangle.
\tag{9}
\]

Equivalently q_(S,L)+<c,M_-c> is an independently nonnegative closed form on
V. Its positive decomposition contains the two displayed positive terms
plus <c,(S-M)c>. This conclusion uses S-M >= 0 directly. It does NOT use
the generally false implication S_- <= M_-.

## 4. A positive main using the approximate response alone

An alternative retains a tail square without evaluating D^-1 G. For any
0 < epsilon < 1, put

\[
M_\epsilon=S_Y-(\epsilon\delta)^{-1}R^*R.
\]

Writing w=v1-Yc and using weighted Cauchy-Schwarz yields

\[
q_{S,L}[F]\ge
(1-\epsilon)\|D^{1/2}(v_1-Yc)\|^2
+\langle c,(M_\epsilon)_+c\rangle
-\langle c,(M_\epsilon)_-c\rangle.
\tag{10}
\]

The omitted nonnegative remainder is explicitly

\[
\epsilon\|D^{1/2}w-\epsilon^{-1}D^{-1/2}Rc\|^2
+\epsilon^{-1}\langle Rc,(\delta^{-1}I-D^{-1})Rc\rangle.
\]

Thus (10) follows from a genuine completion of squares, without asserting
positivity of q_(S,L). It pays a larger finite residual allowance in exchange
for an approximate, rather than exact, tail response in the displayed main.

## 5. Certified matrix errors and anisotropic residual allowances

Suppose a Hermitian matrix C_Y and a certified error e_Y satisfy
||C_Y-S_Y|| <= e_Y. Suppose also Theta >= R*R as finite matrices. Then

\[
M=C_Y-e_Y I-\delta^{-1}\Theta\le S.
\tag{11}
\]

Replace delta^-1 by (epsilon delta)^-1 for (10). If approximate residual
columns R_tilde satisfy ||R-R_tilde|| <= e_R, then, for every tau > 0,

\[
R^*R\le(1+\tau)\widetilde R^*\widetilde R
 +(1+\tau^{-1})e_R^2 I.
\tag{12}
\]

This is a valid explicit Theta. A directly certified full residual Gram is
preferable because it preserves anisotropy and cross correlations. Passing
only its trace or norm to (11) is valid but can lose the useful source weights.

Once M is fixed as an explicit exact finite Hermitian matrix, its negative
spectral part defines the loss. Numerical enclosure of that loss is a
separate finite task. Matrix entrywise lower endpoints do not constitute a
Loewner lower bound. Nor can positive or negative parts be ordered merely
because two Hermitian matrices are ordered.

## 6. A prescribed-template head with explicit source overlaps

Let W:C^m -> H_src have independent prescribed source columns. Set

\[
\Phi=B^{-1/2}W,\qquad G_0=W^*B^{-1}W>0,
\qquad U_0=\Phi G_0^{-1/2}.
\tag{13}
\]

No form-domain assumption on W is needed to construct this head:
B^-1/2 maps H_src into V. Independence makes the finite matrix G0 strictly
positive. U0 is an isometry with range in V, and

\[
B^{1/2}U_0=WG_0^{-1/2},\qquad
c=G_0^{-1/2}d_F,\quad d_F=W^*F.
\tag{14}
\]

Consequently the source overlaps are explicit prescribed-template overlaps,
not unknown B-eigenvector overlaps. The remaining matrices are

\[
C_0=W^*B^{-1}KB^{-1}W,\quad
J_0=(I-E)B^{-1/2}KB^{-1}W,
\]
\[
H_{00}=G_0^{-1/2}C_0G_0^{-1/2},\quad
G=J_0G_0^{-1/2},
\]
\[
T_0:=G_0^{1/2}SG_0^{1/2}
=G_0-C_0-J_0^*D^{-1}J_0.
\tag{15}
\]

For the disjoint translates W=[g,tau_r g], r>ell, the prescribed sources are
L2 orthonormal and

\[
d_{F_r}=W^*F_r=(1,1)^T/\sqrt2.
\tag{16}
\]

The moving-source overlap is therefore exact. Tail safety (2) remains an
independent full-space obligation; (13) does not make it automatic.

## 7. A joint finite matrix certificate without a scalar Gram inverse

Take Y0:C^m -> E-perp and define

\[
R_0=J_0-DY_0,
\]
\[
M_0=G_0-C_0-J_0^*Y_0-Y_0^*J_0+Y_0^*DY_0
             -\delta^{-1}R_0^*R_0\le T_0.
\tag{17}
\]

Certified evaluation errors and an upper residual Gram can be inserted exactly
as in (11). Find an explicit finite matrix Lambda >= 0 satisfying

\[
\boxed{M_0+G_0\Lambda G_0\ge0.}
\tag{18}
\]

Then, on the full form domain,

\[
\boxed{q_{S,L}[F]+d_F^*\Lambda d_F\ge0.}
\tag{19}
\]

Proof: (18) and M0 <= T0 imply T0+G0 Lambda G0 >= 0. Congruence gives
S+G0^(1/2) Lambda G0^(1/2) >= 0. Equations (4) and (14) yield (19).
Thus P_Lambda=q_(S,L)+d_F*Lambda d_F is an independently certified positive
main, and q_(S,L)=P_Lambda-d_F*Lambda d_F. It is closed on V because its
added loss is bounded and finite rank. The certificate uses G0 as a joint
matrix; replacing its inverse normalization by a worst scalar inverse is
unnecessary. There is no positive-part monotonicity step.

For W=[g,tau_r g], the loss is exactly d*Lambda d with d=(1,1)/sqrt2.
In the plus/minus physical-template basis, an arbitrarily large allowance
in the minus direction does not increase this particular loss. Nevertheless
the full matrix inequality (18), including its mixed entry, must be proved.
This permits a source-specific certificate rather than domination of every
head direction by the same scalar allowance.

More explicitly, put d_plus=(1,1)/sqrt2, d_minus=(1,-1)/sqrt2 and choose

\[
\Lambda=\ell_+d_+d_+^*+\ell_-d_-d_-^*,\qquad \ell_+,\ell_-\ge0.
\tag{20}
\]

The independently positive full-domain main supplied by (18) then satisfies

\[
Q[F_r]\ge-\ell_+,
\tag{21}
\]

regardless of the size of ell_minus. To see precisely which mixed condition
still remains, define the exact finite matrix C=G0^-1 M0 G0^-1 and its entries
in the physical plus/minus basis by

\[
a=d_+^*Cd_+,\quad b=d_+^*Cd_-,\quad d=d_-^*Cd_-.
\]

Condition (18) is equivalent by congruence to

\[
\begin{pmatrix}a+\ell_+&b\\\overline b&d+\ell_-\end{pmatrix}\ge0.
\tag{22}
\]

Thus if a+ell_plus<0, no choice of ell_minus repairs the test. If
a+ell_plus=0, the mixed entry b must vanish and the lower diagonal must be
nonnegative. If a+ell_plus>0, a sufficient and necessary lower-channel choice is

\[
\ell_-\ge\max\{0,\ |b|^2/(a+\ell_+)-d\}.
\tag{23}
\]

The targeted plus loss can therefore be bounded independently of a possibly
large minus allowance, but the mixed Schur condition cannot be dropped.
Equations (22)--(23) are exact finite statements. For rigorous computation
one can retain the joint matrix test (18); scalar worst bounds for G0 are
not required. A small strict margin in the plus diagonal can be useful to
accommodate the mixed term without claiming equality at a numerical endpoint.

This differs from the previous H spectral clipping: no unknown supercritical
eigenvectors enter the prescribed source overlaps, and only the plus physical
allowance needs tame growth for the selected probe. A single head chosen as
span{B^(1/2)F_r} would put the unknown Q[F_r]/B[F_r] directly into its head
diagonal; relabeling that scalar is no estimate. The independent two-template
resolvent head provides explicit matrix data to bound, but its full tail and
joint response estimates still have to be established.

## 8. Residual energy without the worst scalar gap

The delta bound in (17) is a fallback, not the desired final estimate.
Suppose the full residual has an independently controlled lift

\[
R_0=D^{1/2}Z_0.
\tag{24}
\]

Then R0*D^(-1)R0=Z0*Z0 exactly. Replace delta^(-1)R0*R0 in
(17) by any certified finite upper matrix N0>=Z0*Z0. Alternatively,
if an independently proved energy comparison D>=t M_tail>=0, t>0, and an
explicit full lift R0=M_tail^(1/2)Z0 are available, then

\[
R_0^*D^{-1}R_0\le t^{-1}Z_0^*Z_0.
\tag{25}
\]

To prove (25), D>=t M_tail gives
||D^(-1/2)M_tail^(1/2)||<=t^(-1/2); apply this to every finite
column combination. A semidefinite M_tail is allowed in this bounded,
strictly positive D setting. The full lift must still be constructed
and its norm bounded. Defining Z0=D^(-1/2)R0 merely renames the
uncontrolled inverse problem.

For a source-specific estimate only the combination

\[
\|Z_0G_0^{-1}d_F\|^2
\tag{26}
\]

enters the raw residual contribution to its Schur lower form.
Bounding all columns by their worst norm can be much less informative.
The same weighted lifting works directly in the orthonormal coordinates
of Sections 2 through 4.

For example, take a two-dimensional tail with D=diag(1/100,1),
G=[[0,1/10],[1,1/2]], Y=(1/2)D^(-1)G, and R=G/2.
For the head source c=(1,0), the weighted residual energy is exactly
1/4. The scalar estimate delta^(-1)||Rc||^2 is 25. This exact matrix
example illustrates why the residual's actual coupled direction matters;
it is not a Sonin computation or evidence of the desired rate.

The boundary-level coisometry and primal lifting in
[positive channel absorption](../POSITIVE_CHANNEL_ABSORPTION_20261003.md)
concern A_boundary=I-C^2. They do not automatically factor the relative
source tail D used here. Transferring that mechanism requires a separate
proof relating the two metrics.

A structured alternative, with P=I-E the full tail projection, starts
with any finite selfadjoint J satisfying
||H-J||<=eta<1. Then on the full tail

\[
D\ge M_J=(1-\eta)I_{E^\perp}-PJP.
\tag{27}
\]

If the finite-rank tail block PJP has every eigenvalue theta_k below
c0=1-eta, M_J is strictly positive. Its inverse is explicit:

\[
M_J^{-1}=c_0^{-1}I+
\sum_k\frac{\theta_k}{c_0(c_0-\theta_k)}P_k.
\tag{28}
\]

Here Pk are the full orthogonal projections onto the nonzero tail
eigenspaces. Thus R0*D^(-1)R0<=R0*M_J^(-1)R0 uses a full residual
Gram and finitely many weighted residual overlaps. It penalizes only
the actual coupling to a near-critical mode. Negative theta_k remain
in the signed comparator. A one-sided bound H<=J+eta I is sufficient
for (27); a norm bound is a convenient stronger input. Neither bound
has yet been established with useful growing-window constants.

## 9. An exact continuous shell calculation

For each integer j>=2 use the common source interval containing every
F_r for j<=r<=j+1 and the common prime set
S_j={p:p<=exp(j+1+ell)}, ell=1/2. A simultaneous translation may center
the interval. Choose the physical templates

\[
W_j=[g,\tau_jg,\tau_{j+1/2}g,\tau_{j+1}g].
\tag{29}
\]

Their supports have disjoint interiors, so Wj is an L2 isometry. Set
phi(u)=<g,tau_u g>; phi is even, supported on [-ell,ell], and phi(0)=1.
It need not be pointwise nonnegative. Its integral is zero because the
mean of g vanishes. For r in the shell,

\[
z_j(r)=W_j^*F_r=\frac1{\sqrt2}
\begin{pmatrix}
1\\ \phi(r-j)\\ \phi(r-j-1/2)\\ \phi(r-j-1)
\end{pmatrix}.
\tag{30}
\]

Define the exact finite covariance

\[
\Xi=\int_j^{j+1}z_j(r)z_j(r)^*\,dr.
\tag{31}
\]

It is independent of j. If

\[
a_0=\int_0^{1/2}\phi(u)^2\,du,\qquad
c_0=\int_0^{1/2}\phi(u)\phi(1/2-u)\,du,
\]

direct piecewise integration gives

\[
\boxed{\Xi=
\begin{pmatrix}
1/2&0&0&0\\
0&a_0/2&c_0/2&0\\
0&c_0/2&a_0&c_0/2\\
0&0&c_0/2&a_0/2
\end{pmatrix}.}
\tag{32}
\]

The first row correlations vanish since int_0^(1/2)phi=0. The two
endpoint moving profiles have disjoint interiors. Adjacent moving
profiles retain a small nonzero signed correlation; it was not dropped.

The probe is piecewise polynomial, so its normalized autocorrelation
on [0,1/2] is an exact rational polynomial of degree 31. Standard-library
Python rational arithmetic gives

\[
a_0=
\frac{905829525272184991390425650669612309}
     {14268586495175130610589494359168638432}
\approx0.06348418083168139,
\]
\[
c_0=
\frac{3642469869392964986970192762067757}
     {5095923748276832360924819413988799440}
\approx0.000714781077841805.
\tag{33}
\]

The exact eigenvalues are 1/2, a0/2, and
(3a0 plus or minus sqrt(a0^2+8c0^2))/4. The minimum is about
0.03173404459. All 15 rational principal minors of Xi and of Xi-I/32
are strictly positive. The moving-block row sums also prove the upper
bound, giving the exact enclosure

\[
\boxed{\frac1{32}I<\Xi\le\frac12I.}
\tag{34}
\]

The [small reproducible package](../../numerics/selective_loss_schur_20261003/README.md)
records the complete rational calculation. Its decimals are diagnostics;
the inequalities are decided by exact rational arithmetic.

If the joint certificate (18) is established for this common head with
one positive allowance Lambda_j over the entire shell, then its loss
and shell integral are

\[
L_j(r)=z_j(r)^*\Lambda_j z_j(r),\qquad
\mathcal A_j=\int_j^{j+1}L_j(r)\,dr
             =\operatorname{Tr}(\Lambda_j\Xi).
\tag{35}
\]

This is a continuous-separation identity, not a sampled approximation.
Equation (34) implies

\[
\frac1{32}\operatorname{Tr}\Lambda_j
\le\mathcal A_j\le\frac12\operatorname{Tr}\Lambda_j.
\tag{36}
\]

The first inequality is strict when Lambda_j is nonzero. Since
||z_j(r)||^2<=1 by orthonormality of Wj,

\[
L_j(r)\le\operatorname{Tr}\Lambda_j\le32\mathcal A_j.
\tag{37}
\]

This is a limitation as well as a usable estimate: averaging within
this fixed four-template family cannot hide an arbitrarily large
allowance in an uncharged direction. Polynomial shell averages are
equivalent, up to fixed constants, to a polynomial total allowance and
give polynomial pointwise bounds. In contrast, the adaptive two-template
head at one fixed r can place a large allowance in its uncharged
difference direction. That distinction matters when choosing the next
head family. More general growing or moving heads can behave differently;
(34) is not asserted for them.

The mean L2 source energy captured by the physical templates is
Tr Xi=1/2+2a0, approximately 0.62696836166. The mean physical orthogonal
residual energy is approximately 0.37303163834. These numbers do not
measure the tail energy of the transformed head U0 or the Sonin metric B.
No B inverse, K, actual Schur matrix, or growing-window loss was evaluated.

## 10. Head selection and noncircular complement control

The prescribed-template construction is useful only with a full safe
complement. It is not established that two or four geometric templates
give D>=delta I at large windows. A sufficient unconditional fixed-window
fallback is to take the actual first n B eigenvectors, whose eigenvalues
are b_k, and a certified bound ||K||<=k. Then

\[
\|P_nHP_n\|\le k/b_{n+1}.
\tag{38}
\]

Here Pn projects onto the complement of those first n eigenvectors.
Compact resolvent makes b_(n+1) tend to infinity at a fixed window, so a
finite safe head exists without assuming Q>=0. It can be enlarged by the
template lifts while preserving that norm tail bound. The current scalar
k and eigenvalue-count estimates can require enormous heads; (38) is
not a polynomial-cost or uniform-loss result.

Added head vectors must lie in V to give bounded source functionals.
Actual B eigenvectors satisfy this. They can be incorporated as physical
templates B^(1/2)e_k alongside the chosen g translates, after dependent
columns are removed. Equations (13) through (19) still apply, but all
additional source overlaps and allowances enter the loss. The simple
two-channel certificate and four-template covariance do not by themselves
bound these added contributions.

A head consisting only of v=B^(1/2)F gives

\[
\langle v,Sv\rangle=Q[F]-\|D^{-1/2}Gv\|^2
\]

when the block notation is interpreted on that head. Its clipped loss is
max(-Q[F]+mixed energy,0). No gain follows from defining this quantity
without independent estimates. For arbitrary F in V the head vector v
need not itself be in V; regularity also has to be checked.

Schur loss is not pointwise ordered with the exact relative spectral
loss <v,(I-H)_-v>. For T=I-H=[[0,1],[1,1]] and first-coordinate head,
the tail is one and the Schur loss operator is diag(1,0), while T_-
has positive entries on both diagonal coordinates and a first entry
less than one. One loss is larger on the first coordinate and smaller
on the second. No implication between their polynomial-growth statements
is claimed without additional comparison bounds.

Enlarging a head improves its compressed Schur form on the old head
and does not worsen a norm tail certificate. It need not decrease the
source's clipped Schur loss, because taking a negative part is not
operator-monotone. Keep an earlier valid scalar loss bound if it is
better; do not assume each enlarged head improves the allowance.

## 11. Global sufficient targets and next analytic tasks

Along the support-adapted family, any of the following would suffice:

- The source-weighted finite loss <c_r,(M_r)_-c_r> is polynomial in r.
- More generally it is O_epsilon(exp(epsilon r)) for every epsilon>0.
- In the prescribed two-template certificate, d_plus*Lambda_r d_plus
  has that growth.

Each assertion must hold for every sufficiently large real r, with full
complement and residual bounds. The established identity
Q[F_r]=q-M_g(r)+epsilon_g(r), together with the one-sided theorem, then
gives the RH implication. The matrix/head ranks and the allowances on
directions orthogonal to d_plus need not be bounded independently of r,
but their actual source contribution must be retained.

For common shell certificates, it is enough to prove
sum_j exp(-epsilon j) A_j<infinity for every epsilon>0. Polynomial
cumulative sums sum_(j<=N) A_j<=C(1+N)^m suffice. The common prime set,
the full complement, and all continuous-separation errors must be included.
For the specific four-template family, (36) shows that this is a bound
on the cumulative trace of the positive allowances as well.

The next tasks within Approach 1 are:

1. Determine whether the prescribed two-template complement has a useful
   one-sided upper relative bound. If it does not, construct a small
   signed comparator and certify the necessary additional modes.
2. Seek a structural estimate on the scalar
   a(r)=d_plus*G0^(-1)M0 G0^(-1)d_plus. The finite criterion is explicit:
   if a(r)>=-C(1+r)^m, choose ell_plus=max(0,-a(r))+1 and select the
   minus allowance by (23). Only ell_plus is charged to F_r. The positive
   margin one is arbitrary and can be replaced by another fixed margin.
3. Construct a full weighted residual lift, targeting the actual plus
   combination in (26). Preserve signed Gram and mixed terms and include
   all source leakage. The existence of an inverse solve is not a bound.
4. Compare adaptive two-template heads with common-shell heads using
   (34) through (37). The latter offer straightforward continuous coverage
   but lose the freely uncharged difference channel over a whole shell.
5. Before any larger computation, derive its source-domain, complement,
   and truncation constants and estimate the required head size. A finite
   set of successful windows cannot establish the global bound.

The first continuation establishes the algebra, the explicit physical
source coordinates, the selective two-channel criterion, and the exact
shell geometry. Tail safety with useful growing-window constants, joint
resolvent estimates, and the required loss rate remain unproved.

## 12. Sources and internal review

The setup and fixed-window domain statements come from
[closed source comparison](../CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md)
and the [general-window scaling audit](../../reviews/ALL_WINDOW_SCALING_AUDIT_20261003.md).
The mixed-column framework comes from
[effective relative tails](../ALL_WINDOW_EFFECTIVE_RELATIVE_TAILS_20261003.md).
The earlier signed Schur reduction is in
[spatial prime reduction](../ALL_WINDOW_SPATIAL_PRIME_REDUCTION_20261003.md).
The present source-selection strategy and ambient obstruction are linked
in [positive channel absorption](../POSITIVE_CHANNEL_ABSORPTION_20261003.md).
The arithmetic sufficiency statement is the established
[one-sided theorem](../GLOBAL_GROWTH_ONE_SIDED_20261003.md).

See the [internal review](../../reviews/SELECTIVE_LOSS_SCHUR_REVIEW_20261003.md)
for the checks and remaining obligations. No manuscript modification,
commit, push, or literature-priority claim is part of this continuation.
