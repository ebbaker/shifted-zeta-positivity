# Arithmetic feedback, the exact scalar remainder, and resonance

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed. This is internal same-model
analysis, not independent specialist refereeing. No new zero-free strip,
variance saving, or implication from quasi-RH to RH is claimed.

The deductions below use the internally established fixed-probe results in
`papers/prime-variance-exponents` at repository commit
`07d6090a1c789383d3d7e0f9e223e5bd15b741e8`. They do not independently certify
that manuscript. The additional calculations here are the sharper complete
von Mangoldt remainder, its consequence for moving-cutoff pole transmission,
and the distinction between contraction at factor scales and at fixed
multiplicative scales.

## 1. The complete mixed feedback with a power remainder

Use the fixed real probe of the earlier project. Set

\[
A=e^{-1/4},\qquad C=2e^{1/4},\qquad q=7/3,
\qquad \ell(v)=\int_1^2 y w(v/y)\,dy,
\]
\[
\lambda(X)=\frac1{qX}\sum_{n\ge2}\Lambda(n)\ell(n/X),
\qquad D(z)=\frac1q\int_A^C\ell(v)v^{z-1}\,dv.
\]

The continuum constant used below is
\(c_w=\int_0^\infty w(v)\log v\,dv\).

The inherited scalar detector gives, for \(1/2\le\beta\le1\),

\[
\lambda(X)=O(X^{\beta-1})
\quad\Longleftrightarrow\quad
\Re\rho\le\beta\text{ for every nontrivial zero}
\quad\Longleftrightarrow\quad
\mathcal V_g(X)=O(X^{1+2\beta}).                 \tag{1}
\]

All estimates in this note are over every sufficiently large real \(X\).
Let \(U=X^{11/24}\), and define the right-continuous increments

\[
M_U(s)=\sum_{n\le s}\mu(n)-\sum_{n\le U}\mu(n),\qquad
E_U(t)=(\psi(t)-t)-(\psi(U)-U).
\]

Keeping von Mangoldt weights is useful here: it avoids any loss from
discarding higher prime powers. Define the fixed aggregate

\[
G(v)=(v\ell'(v))',\qquad
\mathscr F(v)=\sum_{k\ge1}kG(kv)
\]

and the complete arithmetic functional

\[
\mathcal Q(X)=\frac1{qX^2}\int_U^\infty\!\int_U^\infty
M_U(s)E_U(t)\mathscr F(st/X)\,ds\,dt.           \tag{2}
\]

The sum defining \(\mathscr F(v)\) is finite at each positive \(v\).
The kernel vanishes for \(v\ge C\), and
\(\mathscr F(v)=O_w(v^3)\) at zero. Thus the integration region is exactly
\(s,t>U\), \(st<CX\); it is bounded, and includes all terminal product
bands. At integer \(U\), its atom is excluded by the right-continuous
increments. For all sufficiently large \(X\), \(U^2\le AX\).

Write

\[
J_\Lambda(X;U)=c_w\sum_{d\le U}\frac{\mu(d)}d
+\frac1{qX}\sum_{m>U,n>U}A_U(m)\Lambda(n)\ell(mn/X),
\qquad A_U(m)=\sum_{d\mid m,\ d>U}\mu(d).
\]

The density cancellation and two integrations by parts from the inherited
centering and mixed-feedback notes apply verbatim with \(\psi\) in place
of \(\theta\). They give the exact identity

\[
J_\Lambda=\mathcal Q+R_{\rm density},\qquad
R_{\rm density}=-\frac1{qN}\sum_{d\le U}\mu(d)r_f(N/d),
\qquad N=X/U,                                      \tag{3}
\]

where \(f(v)=v^{-1}\int_v^\infty\ell(s)\,ds\),
\(r_f(y)=\sum_{k\ge1}f(k/y)-y\int f\), and

\[
|R_{\rm density}|\ll_w(U^2/X)^8=X^{-2/3}.           \tag{4}
\]

The seventh-order scalar comparison in the centering note, section 5,
gives the other complete remainder:

\[
\lambda-J_\Lambda
=O_w\!\left(X^{-7}\{U^7(1+\log X)+U^{14}\}\right)
=O_w\!\left(X^{-91/24}(1+\log X)+X^{-7/12}\right).
                                                               \tag{5}
\]

Consequently

\[
\boxed{\lambda(X)=\mathcal Q(X)+R(X),\qquad
R(X)=O_w(X^{-7/12}).}                              \tag{6}
\]

Here \(R=(\lambda-J_\Lambda)+R_{\rm density}\). Equation (6) retains
the entire arithmetic mixed integral; it does not assume that the two
errors are independent, bound a terminal range separately, or replace
the moving cutoff inside a fixed-cutoff Mellin formula. Its scalar
remainder is stronger than the \(O(X^{-1/2})\) consequence of the earlier
norm comparison.

For \(\delta=2\beta-1\), define

\[
F_\beta(X)=X^{1-\beta}\lambda(X),\qquad
Q_\beta(X)=X^{1-\beta}\mathcal Q(X).
\]

Then admissibility of \(\delta\) implies \(F_\beta=O(1)\), and

\[
F_\beta(X)=Q_\beta(X)+O_w(X^{-(\beta-5/12)}).
                                                               \tag{7}
\]

The remainder in (7) has at least the fixed power \(1/12\) throughout
\(\beta\ge1/2\). Thus this remainder does not obstruct a sufficiently
small descent from any positive \(\delta\). The missing estimate concerns
the signed functional \(Q_\beta\) itself.

## 2. Constant contraction at arithmetic factor scales is too weak

The actual factors in (2) lie in
\([X^{11/24},CX^{13/24}]\). They are power scales of \(X\), rather than
fixed multiples of \(X\). This distinction changes what an iteration proves.

Consider even the strong hypothetical recurrence

\[
f(X)\le r f(X^\vartheta)+C X^{-\eta},\qquad
0<r<1,\quad0<\vartheta<1,\quad\eta>0,              \tag{8}
\]

for a nonnegative normalized error. It does not force
\(f(X)=O(X^{-\epsilon})\) for any \(\epsilon>0\). Indeed, set

\[
p=\frac{\log(1/r)}{\log(1/\vartheta)}>0,\qquad
f(X)=(\log X)^{-p}\quad(X>1).
\]

Then \(r f(X^\vartheta)=r\vartheta^{-p}f(X)=f(X)\): the homogeneous
equality already has only logarithmic decay. This is a deterministic
counterexample to the inference from (8), not an arithmetic counterexample.
Likewise a recurrence with
\(r\sup_{X^a\le Y\le X^b}f(Y)\), \(0<a\le b<1\), admits the same
example with \(\vartheta=a\), since the displayed \(f\) is decreasing.

In logarithmic coordinates \(t=\log X\), a factor-scale step sends
\(t\) to \(\vartheta t\); reaching a fixed initial range takes only
\(O(\log t)=O(\log\log X)\) steps. A fixed multiplicative step
\(X\mapsto X/c\), \(c>1\), instead sends \(t\) to
\(t-\log c\) and supplies \(O(\log X)\) steps, sufficient for a power.

This shows why a proposed "contractivity of the two half-scale errors"
must be inspected quantitatively. A constant less than one may remove a
logarithmic factor without changing the admissible exponent. The fixed
multiplicative-scale descent criterion in this project's main research
note addresses a stronger kind of recurrence.

## 3. The moving-cutoff functional preserves every forbidden pole

There is a direct rigorous resonance test for the actual functional (2),
including multiple zeros. It does not require representing arithmetic
errors as a sum over zeros.

Fix a sufficiently large \(X_0\). The scalar detector's true Mellin
formula, with its compact initial cap retained, is

\[
\int_{X_0}^\infty\lambda(X)X^{-z}\,dX
=-D(z)\frac{\zeta'}{\zeta}(z)-C_{X_0}(z),
\qquad\Re z>1,                                     \tag{9}
\]

where \(C_{X_0}\) is entire. The full scalar vanishes below a positive
fixed scale, so the removed interval is compact in \(\log X\).
By (6),

\[
\mathcal R(z)=\int_{X_0}^\infty R(X)X^{-z}\,dX
\]

is holomorphic on \(\Re z>5/12\), with absolute local uniform
convergence there. It follows initially on \(\Re z>1\), and then by
meromorphic continuation, that

\[
\boxed{\int_{X_0}^\infty\mathcal Q(X)X^{-z}\,dX
=-D(z)\frac{\zeta'}{\zeta}(z)-C_{X_0}(z)-\mathcal R(z).} \tag{10}
\]

The integral in (10) is asserted to converge initially; its right side
provides continuation. At every nontrivial zero \(\rho\) with
\(\Re\rho>1/2\), of multiplicity \(m_\rho\), the fixed-probe
noncancellation theorem says \(D(\rho)\ne0\), and hence

\[
\operatorname{Res}_{z=\rho}\mathcal M[\mathcal Q](z)
=-m_\rho D(\rho)\ne0.                              \tag{11}
\]

Thus the complete *moving-cutoff* feedback transmits the full scalar
residue. No rightmost zero, spectral gap, or simplicity assumption is
used. The proof explicitly avoids substituting \(U(X)\) into a transform
formula proved for fixed \(U\).

For comparison, the inherited fixed-cutoff multiplier is

\[
\mathcal F_U(z)=1-\zeta(z)\sum_{d\le U}\mu(d)d^{-z},
\qquad \mathcal F_U(\rho)=1.                         \tag{12}
\]

Every finite weighted average of such multipliers with weights summing
to one still equals one at \(\rho\). Every finite product also equals
one. Weights summing to zero annihilate that pole and thereby lose
detection of that zero by this residue. These are algebraic obstructions
to automatic contraction from
cutoff averaging or repeated use of the same convolution identity. They
are not obstructions to a new arithmetic inequality for the actual input.

## 4. What logarithmic decay does and does not exclude

Suppose the admissible strip is \(\Re\rho\le\beta\), with
\(\beta>1/2\). If one could prove the additional conclusion
\(F_\beta(X)\to0\), it would exclude a zero *on* the boundary
\(\Re\rho=\beta\). To see this, put \(t=\log X\) and
\(f(t)=F_\beta(e^t)\). The transform from (9) has at
\(s=i\gamma\), corresponding to \(\rho=\beta+i\gamma\), residue
\(-m_\rho D(\rho)\). But boundedness and \(f(t)\to0\) imply

\[
\lim_{\epsilon\downarrow0}\epsilon
\int_{\log X_0}^\infty e^{-(\epsilon+i\gamma)t}f(t)\,dt=0.
                                                               \tag{13}
\]

For (13), split the integral at a fixed large \(T\): the compact part
vanishes after multiplication by \(\epsilon\), and the tail is bounded
by \(\sup_{t\ge T}|f(t)|\). This contradicts the nonzero residue.

Excluding the boundary is weaker than finding an improved closed strip.
A supremum of zero real parts need not be attained by a zero. The fact
that the optimal *variance estimate* is attained does not imply that a
rightmost zero exists. Consequently, logarithmic decay or small-o at the
optimal power cannot by itself finish the proposed descent argument.

## 5. A finite-delay filter clarifies the next arithmetic obligation

Take fixed \(h>0\), \(0<r<1\), and the normalized response
\(f_\beta(t)=e^{(1-\beta)t}\mathcal Q(e^t)\). The delay defect is

\[
\Delta_{\beta,h,r}(t)=f_\beta(t)-r f_\beta(t-h).       \tag{14}
\]

For transforms starting at a fixed sufficiently large \(t_0\), finite
initial intervals contribute only entire functions. The multiplier of
the meromorphic transform is

\[
1-r e^{-sh}.                                        \tag{15}
\]

At a boundary zero \(s=\rho-\beta=i\gamma\), its modulus is at least
\(1-r\). In fact it is nonzero throughout
\(\Re s>\log r/h\), since \(r e^{-h\Re s}<1\) there. Thus a strict
delay-contraction filter does not silently cancel a hypothetical
boundary pole. A new power estimate for this defect would have to be
proved by actual signed arithmetic cancellation; it cannot be produced
merely by applying the existing identity twice.

The raw arithmetic form of (14) is

\[
\Delta_{\beta,h,r}(\log X)
=X^{1-\beta}\left\{\mathcal Q(X)
-r e^{(\beta-1)h}\mathcal Q(e^{-h}X)\right\}.          \tag{16}
\]

Both terms in (16) retain their own full product domain and their own
cutoff. Equation (7) quantifies exactly the cost of replacing either by
the original scalar. There is also a direct single-probe representation.
With \(c=e^h\), define

\[
\ell_{\beta,c,r}(v)=\ell(v)-r c^\beta\ell(cv).
\]

Then, exactly,

\[
\lambda(X)-r c^{\beta-1}\lambda(X/c)
=\frac1{qX}\sum_{n\ge2}\Lambda(n)\ell_{\beta,c,r}(n/X),
                                                               \tag{17}
\]
\[
D_{\beta,c,r}(z)=D(z)(1-r c^{\beta-z}).              \tag{18}
\]

The new fixed probe has zero ordinary moment, the same available
smoothness, and support in \([A/c,C]\). Its logarithmic moment is
\(q c_w(1-r c^{\beta-1})\), so the continuum in a new arithmetic
decomposition is explicitly determined and cannot be dropped. Thus
subtracting the delayed response produces another detector with a known
multiplier; it does not already prove a better estimate for it.

This gives a concrete object for a next scout:

1. Expand (16) using the finite von Mangoldt/Vaughan coefficient identity,
   retaining both continua and both terminal bands, before taking any
   absolute values.
2. Separate the terms whose bounds follow from the already-proved smooth
   lattice remainders. Their total is explicitly affordable by (7).
3. Identify any remaining signed cross-scale term for which multiplicative
   arithmetic, rather than independent error envelopes, might yield a
   uniform estimate. Test a proposed cancellation against (15) first.
4. Use a finite numerical scout only to reject bad signs or constants and
   check boundary bookkeeping. A finite range cannot certify the required
   all-real-\(X\) inequality or asymptotic contraction coefficient.

No estimate of the residual term in step 3 is proved here. This formulation
does establish that the remainders are already below the desired scale,
and states a falsifiable criterion for evaluating a proposed new mechanism.

## Source links and verification scope

- [Scalar detector](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/SCALAR_DETECTOR_20261004.md),
  sections 2--4 and 6: scalar normalization, noncancellation, cap and strip equivalence.
- [Prime-discrepancy centering](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/PRIME_DISCREPANCY_CENTERING_20261004.md),
  sections 3 and 5: exact density remainder and improved scalar comparison.
- [Mixed discrepancy feedback](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/MIXED_DISCREPANCY_FEEDBACK_20261004.md),
  sections 2--3, 5--8: complete increment identity, aggregate decay,
  deterministic resonance calculations and exact coefficient closure.
- [Aggregated-kernel continuation](../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/AGGREGATED_KERNEL_CONTINUATION_20261004.md),
  section 6: fixed-cutoff multiplier and warning about moving cutoffs.

The proofs above were checked algebraically against those identities. No
numerical asymptotic evidence, new empirical bound, or external literature
claim is used. The resonance argument for the actual moving cutoff is
deduced from its full error comparison, not from a model zero expansion.
