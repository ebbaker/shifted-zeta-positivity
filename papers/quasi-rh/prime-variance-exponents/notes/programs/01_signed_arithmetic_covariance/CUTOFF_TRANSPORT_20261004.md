# Exact cutoff transport and the common response in Vaughan averages

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not inferred. These are internal algebraic
derivations and exact finite checks, not independent specialist refereeing.
No new global prime-variance exponent is proved.

## Outcome

Changing the two Vaughan cutoffs gives complete signed annulus identities.
After retaining the logarithmic continuum, their differences are
unconditionally small in the previously established balanced range. A
positive average over such cutoffs preserves the same unresolved prime
response. Its variation across cutoffs is small, but this does not bound its
mean. Thus cutoff averaging alone supplies no contraction.

There is a useful refinement of the available coordinates: for a first
saving \(\kappa\), the localization budget only requires
\(UV\le X^{1-\kappa/12}\), rather than the stronger quadratic-error
condition \(UV\le X^{11/12}\). The corresponding cofactor and central
Mellin powers can both be reduced to \(\kappa/12\). All these statements
are proved reductions; the signed energy estimate remains open.

The only inputs are the lattice estimates proved in the
[Möbius/Vaughan reduction](../../MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md)
and the coefficient and Fourier estimates proved in the
[signed Mellin continuation](../../SIGNED_MELLIN_CONTINUATION_20261004.md).
The probe, support \([A,B]\), and all-real-shell convention are unchanged.

## 1. Definitions and complete cutoff differences

Keep \(X\) fixed while \(x\in[X,2X]\). Put

\[
L(y)=\sum_{k\ge1}w(k/y),\qquad
H(y)=\sum_{k\ge1}(\log k)w(k/y)-c_wy,
\]
\[
I_U(x)=\sum_{d\le U}\mu(d)H(x/d),\quad
C_{U,V}(x)=\sum_{d\le U,r\le V}\mu(d)\Lambda(r)L(x/(dr)),\quad
P_V(x)=\sum_{r\le V}\Lambda(r)w(r/x).
\]

With the existing definitions of \(B_{U,V}\) and \(M_1(U)\), write

\[
T_{U,V}(x)=B_{U,V}(x)+c_wxM_1(U).
\]

The complete Vaughan identity says, exactly,

\[
\boxed{T_{U,V}=V_g-I_U+C_{U,V}-P_V.}                 \tag{1}
\]

In particular \(P_V=0\) throughout the shell when \(V<AX\).
The formulas below first retain it, so that the identity remains valid
when a cutoff is moved beyond that safe range.

For \(1\le U_1<U_2\), keeping \(V\) fixed,

\[
\boxed{\begin{aligned}
T_{U_2,V}-T_{U_1,V}
={}&-\sum_{U_1<d\le U_2}\mu(d)H(x/d)\\
&+\sum_{U_1<d\le U_2,r\le V}
\mu(d)\Lambda(r)L(x/(dr)).
\end{aligned}}                                                   \tag{2}
\]

This can also be derived before invoking (1). Expanding
\(A_U(m)=\sum_{dk=m,d>U}\mu(d)\) gives

\[
B_{U_2,V}-B_{U_1,V}
=-\sum_{U_1<d\le U_2}\mu(d)
\sum_{k\ge1,r>V}\Lambda(r)w(dkr/x).
\]

The identity \(1*\Lambda=\log\) replaces the inner sum by
\(\sum_k(\log k)w(dk/x)-\sum_{r\le V}\Lambda(r)L(x/(dr))\).
Its continuum is exactly canceled by
\(c_wx[M_1(U_2)-M_1(U_1)]\). This proves (2), including its signs.
Without centering, the raw Type II difference contains
\(-c_wx\sum_{U_1<d\le U_2}\mu(d)/d\); it has not been shown small
separately.

For \(1\le V_1<V_2\), keeping \(U\) fixed,

\[
\boxed{\begin{aligned}
T_{U,V_2}-T_{U,V_1}
={}&\sum_{d\le U,V_1<r\le V_2}
\mu(d)\Lambda(r)L(x/(dr))\\
&-\sum_{V_1<r\le V_2}\Lambda(r)w(r/x).
\end{aligned}}                                                   \tag{3}
\]

Here \(\mu*1=\delta_1\) gives
\(\sum_{d>U,k}\mu(d)w(dkr/x)=w(r/x)-\sum_{d\le U}\mu(d)L(x/(dr))\).
The final prime-response annulus in (3) vanishes if \(V_2<AX\).
Dropping it without this restriction would be an incorrect transport
identity.

The mixed difference is particularly simple:

\[
\boxed{\begin{aligned}
&T_{U_2,V_2}-T_{U_2,V_1}-T_{U_1,V_2}+T_{U_1,V_1}\\
&\qquad=\sum_{U_1<d\le U_2,V_1<r\le V_2}
\mu(d)\Lambda(r)L(x/(dr)).
\end{aligned}}                                                   \tag{4}
\]

Every integer in each half-open annulus is included. Every lattice sum
retains all cofactors permitted by the physical support
\(AX\le drk\le2BX\); no terminal product band is replaced by a rectangle.
These identities hold for real cutoffs, including integer endpoints.

## 2. Quantitative annulus costs

Use the constants \(\mathscr C_w,\mathscr C_v\) from the lattice lemma,
and define

\[
S_5(a,b)=\sum_{a<d\le b}d^5,\qquad
P_5(a,b)=\sum_{a<r\le b}\Lambda(r)r^5,\qquad
K_X=\mathscr C_w\log(2X)+\mathscr C_v.
\]

For \(U_2\le X\), (2) gives

\[
\|T_{U_2,V}-T_{U_1,V}\|_2
\le X^{-9/2}S_5(U_1,U_2)
\{K_X+\mathscr C_wP_5(0,V)\}.                  \tag{5}
\]

For \(V_2<AX\), (3) gives

\[
\|T_{U,V_2}-T_{U,V_1}\|_2
\le\mathscr C_wX^{-9/2}S_5(0,U)P_5(V_1,V_2). \tag{6}
\]

Equation (4) has the same bound with both moments restricted to their
annuli. For a simultaneous increase of both cutoffs, one may use the
two disjoint strips

\[
\begin{aligned}
\|T_{U_2,V_2}-T_{U_1,V_1}\|_2
\le X^{-9/2}\big[&K_XS_5(U_1,U_2)\\
&+\mathscr C_wS_5(U_1,U_2)P_5(0,V_2)\\
&+\mathscr C_wS_5(0,U_1)P_5(V_1,V_2)\big],       \tag{7}
\end{aligned}
\]

provided \(U_2\le X\) and \(V_2<AX\). There is no duplicated corner.
If the latter restriction fails, the norm of the complete prime-response
annulus in (3) must be added. At cutoffs comparable with \(X\), its
elementary bound can be cubic in energy and supplies no fixed saving.

These estimates use
\(|L(x/(dr))|\le\mathscr C_wX^{-5}(dr)^5\),
\(|H(x/d)|\le K_XX^{-5}d^5\), and the shell length \(X\).
They require no cancellation estimate for \(\mu\).
In particular \(S_5(0,U)\le U^6\) and the inherited elementary
Chebyshev bound gives \(P_5(0,V)\le(4\log2)V^6\). Consequently

\[
\boxed{\|T_{U,V}-V_g\|_2
\le X^{-9/2}\{K_XU^6+(4\log2)\mathscr C_w(UV)^6\}}
                                                               \tag{8}
\]

for \(1\le U\le X\), \(1\le V<AX\).

## 3. A cutoff region adapted to one fixed saving

Fix \(0<\kappa\le1\) and put \(q=(3-\kappa)/2\). Throughout

\[
U=X^u,\quad V=X^v,\quad u,v>0,\quad
u+v\le1-\kappa/12,                              \tag{9}
\]

the norm in (8) is \(O(X^q)\). The second term satisfies the desired
power directly. The first has the extra factor
\(V^{-6}\log X=O(1)\). More generally, for arbitrary cutoffs with
\(UV\le X^{1-\kappa/12}\), (8) supplies
\(X^{q+o(1)}\); the logarithmic qualification matters near bounded
\(V\). Taking \(V\ge(\log X)^{1/6}\) also gives the pure \(O(X^q)\)
budget. Shrinking the exponent sum in (9) by a fixed \(\eta>0\)
improves the norm error to \(O(X^{q-6\eta})\).

Thus every cutoff in (9) has the same exact admissibility of the target
\(\|T_{U,V}\|_2^2=O(X^{3-\kappa})\) as \(V_g\), by the triangle
inequality. This is an equivalence at a specified error budget, not a
bound on the retained response. For balanced cutoffs one can use

\[
U=V=X^{1/2-\kappa/24},\qquad
X^{1/2-\kappa/24}<m,n\le2BX^{1/2+\kappa/24}.      \tag{10}
\]

At \(\kappa=1\), this recovers \(11/24\). At the audit budget
\(\kappa=0.01\), it gives \(U=V=X^{1199/2400}\), and both Type II
factors are confined to the powers \(1199/2400\) and \(1201/2400\).
No generic bilinear estimate is thereby strengthened: a narrower factor
region still carries the full unresolved response.

One cannot move to a cutoff where Type II vanishes using this small-error
region. The sufficient empty-product condition is \(UV\ge2BX\), beyond
\(UV\le X^{1-\kappa/12}\) for every fixed positive \(\kappa\).
The transport cost becomes too large before that proposed anchor is
reached. In the elementary proof, this is where the lattice arguments
\(x/(dr)\) cease to be uniformly large.

## 4. The scalar and projected parts move together

Write \(\lambda(F)=\langle F,x\rangle/\|x\|_2^2\), where
\(\|x\|_2^2=(7/3)X^3\), and let \(P_\perp\) project off \(x\).
If a cutoff difference has norm at most \(E\), then

\[
\|P_\perp(T_2-T_1)\|_2\le E,\qquad
|\lambda(T_2)-\lambda(T_1)|
\le\sqrt{3/7}\,X^{-3/2}E.                       \tag{11}
\]

The scalar here is precisely
\(\lambda(B_{U,V})+c_wM_1(U)\), the mismatch required by the
[complete Gram split](PRELIMINARY_INVESTIGATION_20261004.md).
For an \(O(X)\) transport error it changes by \(O(X^{-1/2})\).
For the first-saving region (9), it changes by \(O(X^{-\kappa/2})\).
Transport preserves both obligations; it does not discharge either one.
These are the two pieces of the shellwise orthogonal identity, not two
logically independent global hypotheses. The companion
[scalar detector](SCALAR_DETECTOR_20261004.md) proves that an all-real-shell
power bound for either sign of the complete scalar alone already implies
the full energy bound, using the arithmetic transform and the manuscript's
spectral equivalence. Cutoff transport supplies no such scalar bound.

## 5. Why a cutoff average does not yet save energy

Take any finite family of admissible cutoffs and write
\(T_j=V_g+e_j\), with \(\|e_j\|_2\le E\) uniformly. For real
weights \(a_j\), let \(s=\sum_ja_j\) and \(L=\sum_j|a_j|\). Then

\[
\boxed{\left\|\sum_ja_jT_j-sV_g\right\|_2\le LE.}             \tag{12}
\]

Weights summing to one preserve the common response. For nonnegative
weights \(p_j\) summing to one, no loss grows with the number of cutoffs,
but neither does a saving appear. In fact the exact Hilbert-space identity
is

\[
\begin{aligned}
\sum_jp_j\|T_j\|_2^2-\left\|\sum_jp_jT_j\right\|_2^2
&=\frac12\sum_{i,j}p_ip_j\|T_i-T_j\|_2^2\\
&=\sum_jp_j\|e_j\|_2^2-\left\|\sum_jp_je_j\right\|_2^2
\le E^2.                                                       \tag{13}
\end{aligned}
\]

Thus averaging cutoffs with quadratic error reduces their average energy
by at most \(O(X^2)\). Any larger common energy remains. The same
identity applies after orthogonal projection; the scalar variance is at
most \(3E^2/(7X^3)\). This is a consequence of the actual arithmetic
identities, not an independence model for blocks.

Weights summing to zero remove \(V_g\) exactly, leaving only a small
combination of the already controlled errors. Such identities cannot
bound the common response without a separate estimate or anchor. Signed
weights with \(L\le X^\eta\) amplify an error budget corresponding to
\(\kappa_0\) into one corresponding to \(\kappa_0-2\eta\);
their total variation must therefore be charged.

The obstruction is limited to what follows from these transport and
averaging identities. A new arithmetic estimate for a smoothed cutoff
average would still be useful, because (12) transfers it to \(V_g\).
The identity does not supply that new estimate.

## 6. The corresponding cofactor and Mellin budget

The existing divisor error is
\(\|V_g-R_{X,D}\|_2\ll X^{-9/2}D^6\log D\).
The existing outer-frequency bound is

\[
\|R_{X,D}-R_{X,D,T}\|_2^2
\ll X^2(\log X)^5(T^{-11}+XT^{-12}).             \tag{14}
\]

It remains uniform when \(D\) varies: its proof only uses
\(|a_{X,D}(n)|\le d_2(n)\log n\), independent of the cutoff.
For the same fixed \(\kappa\), take

\[
D_\kappa=\frac{X^{1-\kappa/12}}{(\log X)^{1/6}},\qquad
T_\kappa=X^{\kappa/12}(\log X)^{5/12}.           \tag{15}
\]

Both omitted responses then have norm \(O(X^q)\). For (14), the
\(XT^{-12}\) term is exactly of size \(X^{3-\kappa}\), while the
\(T^{-11}\) term has power \(2-11\kappa/12<3-\kappa\).
Every surviving cofactor obeys

\[
k\le\frac{2BX}{D_\kappa}
=2BX^{\kappa/12}(\log X)^{1/6}.                 \tag{16}
\]

The small-frequency bound from the same note,
\(\|R_{X,D,\tau}\|_2^2\ll X^3(\log X)^5\tau^6\), also permits

\[
\tau_\kappa=X^{-\kappa/6}(\log X)^{-5/6}.        \tag{17}
\]

Consequently the complete retained response with
\(\tau_\kappa<|t|\le T_\kappa\) differs from \(V_g\) by
\(O(X^q)\) in shell norm. Its exact first-saving energy target is
equivalent to the target for \(V_g\). Increasing the three logarithmic
powers in the favorable directions makes the discarded norm \(o(X^q)\).
All fixed nonzero frequencies eventually remain; there is no new bound
on the fixed-frequency arithmetic.

With bare powers in (15)–(17), the errors are only
\(X^{q+o(1)}\), so the immediate equivalence is for subpower-loss
targets. An actual-prime subpower bound still recovers its exact endpoint
by the inherited closed-strip theorem in the
[overview](../../PROJECT_OVERVIEW_20261004.md). It would be incorrect to
claim pure endpoint bounds for an arbitrary approximant solely from a
subpower error. The displayed logarithmic choices avoid that distinction.

At \(\kappa=0.01\), the cofactor and outer-frequency powers in (16)
and (15) are \(1/1200\), while the small-frequency power is
\(-1/600\). These are asymptotic localization statements with
probe-dependent constants; they provide no useful numerical threshold
without a separate constant calculation.

## 7. Exact finite verification and next use

The standard-library script
[check_cutoff_transport.py](../../../numerics/01_signed_arithmetic_covariance/check_cutoff_transport.py)
represents each logarithm as an integer vector of prime logarithms. For
every product integer \(1\le n\le256\) and cutoffs
\(1,7/2,8,61/4,32\), it verifies the full Vaughan identity, both
one-cutoff identities, and every mixed rectangle. The result is
**57,600 exact coefficient-vector comparisons and 50 rational continuum
checks**, all passing. Prime powers, complete lattice cofactors, and
integer versus noninteger endpoints are retained. No floating arithmetic
or fitted exponent is involved. This is finite bookkeeping validation;
the displayed algebra proves the general identities.

The next use of these formulas is to audit a proposed overlap estimate
with a cutoff choice suited to its actual \(\kappa\) budget. By the
companion scalar detector, a bound for either sign of the complete
centered scalar is already a sufficient target. Small cutoff differences,
smoothing the cutoff, or taking a large collection of nearly identical
centered responses cannot supply that missing bound by themselves.
