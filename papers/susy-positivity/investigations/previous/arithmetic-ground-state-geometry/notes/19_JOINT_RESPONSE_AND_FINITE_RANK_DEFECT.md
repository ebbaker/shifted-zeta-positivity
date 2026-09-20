# Joint response: exact high-mode gluing and a finite-rank defect

13 September 2026. The result of this continuation is a closed positive
source on the full logarithmic domain with the exact identity

\[
\boxed{\qquad
\langle\Phi_L f,\Phi_L g\rangle
=Q_L(f,g)+\langle P_Nf,D_NP_Ng\rangle,\qquad D_N>0.
\qquad}
\tag{1}
\]

The extra form now has finite rank \(N\). The mode projection \(P_N\)
is an explicitly chosen Neumann cosine projection, selected by the
proved inequality in [note 18](18_REVIEW_AND_NEUMANN_COMPARISON.md).
It is not a spectral projection of the Weil operator. The norm is
exact on \(\ker P_N\), and the full low/high interaction is retained.

This improves note 17's infinite-rank compact error. It is still a
positive **completion**. A finite matrix inequality, displayed below
without assuming its sign, is exactly what remains to prove. The
construction works for a much wider class of semibounded forms and
does not itself explain arithmetic positivity.

## 1. Couple the whole source to one auxiliary field

Fix \(L>0\), \(D\ge L\), and a finite prime set \(\mathcal S\)
containing every prime with \(\log p<L\). Retain the explicit closed
gamma-and-pole source \(\mathcal A_0\) of note 15 and all observed
prime graph outputs of note 16. On \(X=L^2(I_L)\), set

\[
A f=\mathcal A_0 f\oplus\mathcal J_{\mathcal S}f,\qquad
\mathcal J_{\mathcal S}f=(\mathcal D_pE_Lf)_{p\in\mathcal S},
\qquad \operatorname{Dom}A=\mathcal D_{\log,L}.
\tag{2}
\]

The output \(\mathscr Y\) is the already specified positive direct
sum. The unit quartic cap can be retained in every channel. Put

\[
c_{\mathcal S}=\sum_{p\in\mathcal S}\frac{2\log p}{\sqrt p-1},
\quad
\alpha=e^D+c_{\mathcal S}-w_0=2\kappa>0.
\tag{3}
\]

The source identities, before any new feedback, give

\[
T:=A^*A=T_0+\mathcal J_{\mathcal S}^*\mathcal J_{\mathcal S}
=W_L+\alpha I,\qquad
T\ge mI,\quad m=e^D+L-2\sinh(L/2)>0.
\tag{4}
\]

Here \(\operatorname{Dom}T=\operatorname{Dom}T_L\). Positivity of
\(T\) follows from the explicit source and the old lower bound on
\(T_0\); it is not an assumption about \(W_L\).

A genuine change from note 17 is to prepare the same field in **all**
the source channels, minimizing, for fixed external drive \(v\),

\[
\|\mathcal A_0u\|^2+
\sum_{p\in\mathcal S}\|\mathcal D_pE_Lu\|^2
-2\Re\langle v,u\rangle .
\tag{5}
\]

Its unique response is \(u=T^{-1}v\). The prime vertices and their
positive energies are unchanged, but the field entering them is now
the same field entering the gamma-and-pole preparation. As before,
stability means a positive Hessian in \(u\), not a nonnegative joint
action in \(v,u\).

The first joint readout \(A(I-\alpha T^{-1}/2)\) satisfies

\[
\|A(I-\alpha T^{-1}/2)f\|^2
=Q_L[f]+\frac{\alpha^2}{4}\langle f,T^{-1}f\rangle.
\tag{6}
\]

Since \(T\ge T_0>0\), its defect is no greater in operator order than
the massless defect of note 17. This is a strict change of response
law, not a new choice of its old mass parameter. Equation (6) alone
still leaves an infinite-rank error.

## 2. Separate an explicitly controlled high sector

Choose \(N,\delta>0\) by note 18, so that, with \(P=P_N\), \(Q=I-P\),

\[
W_L|_{QX}\ge\delta I.
\tag{7}
\]

The notation means the closed form restricted to
\(Q\mathcal D_{\log,L}\), which is dense in \(QX\). Let \(A_H\) be
the restriction of \(A\) to this domain, and let

\[
T_H=A_H^*A_H,\qquad V=T_H^{-1},\qquad
H=T_H-\alpha I\ge\delta I.
\tag{8}
\]

All three operators act on \(QX\). In particular
\(T_H\ge(\alpha+\delta)I\), and its resolvent is compact. The only
spectral data used to choose this sector are those of the elementary
Neumann Laplacian.

The finite coupling and low block are

\[
B=QTP=QW_LP:PX\longrightarrow QX,\qquad M=PTP.
\tag{9}
\]

The operator-domain check at the end of note 18 makes \(B\) bounded.
It is not set to zero. Its explicit arithmetic expression is

\[
B=QT_LP+QP_L^{\rm pole}P
-\sum_{m\log p<L}(\log p)p^{-m/2}
  Q(T_{m\log p}+T_{m\log p}^*)P.
\tag{10}
\]

The scalar contact drops from this cross block because \(QP=0\).
For \(f=p+q\), the full target form is exactly

\[
Q_L[f]=\langle q,Hq\rangle
+2\Re\langle q,Bp\rangle
+\langle p,(M-\alpha I)p\rangle,
\tag{11}
\]

where the first expression is understood as a form if
\(q\notin\operatorname{Dom}H\).

## 3. Repeated stable responses remove the high-sector error

Define the positive coefficients

\[
a_j=\frac{\binom{2j}{j}}{4^j(2j-1)},\quad j\ge1,\qquad
a_1=\tfrac12,\quad
a_{j+1}=a_j\frac{2j-1}{2j+2}.
\tag{12}
\]

They are the coefficients of \(1-\sqrt{1-z}\). The response bound in
(8) gives

\[
\|\alpha V\|\le\theta:=\frac{\alpha}{\alpha+\delta}<1.
\tag{13}
\]

Consequently the explicitly convergent response series

\[
R=I-\sum_{j\ge1}a_j\alpha^j V^j,\qquad
R_\ell=I-\sum_{j=1}^{\ell}a_j\alpha^jV^j
\tag{14}
\]

defines a bounded positive invertible operator on \(QX\). Each \(V\)
is obtained by minimizing (5) over the high sector with the indicated
drive. All iterations have the same independently positive Hessian.
The scalar identity for the series proves

\[
R^2=I-\alpha V,\qquad
R T_H R=H,\qquad
\|A_H Rq\|^2=\langle q,Hq\rangle.
\tag{15}
\]

The series is the positive high-sector factor
\((I-\alpha V)^{1/2}\). This is stated explicitly: it is justified by
the independently proved gap (7), and is not an assumed positive
square root of the full unknown Weil form.

The convergence needed for an unbounded source is stronger than
operator-norm convergence of \(R_\ell\) alone. The scalar tail bound
gives

\[
\|A_H(R_\ell-R)\|
\le
\frac{a_{\ell+1}\alpha^{\ell+1}}
{(1-\theta)(\alpha+\delta)^{\ell+1/2}}
\longrightarrow0.
\tag{16}
\]

Here the difference extends boundedly to all of \(QX\). It follows
by taking the supremum of
\(\sqrt\lambda\sum_{j>\ell}a_j(\alpha/\lambda)^j\) for
\(\lambda\ge\alpha+\delta\). Thus the singular source limit is
controlled in the appropriate graph topology.

There is also a useful positive error formula for the finite series:

\[
E_\ell=T_HR_\ell^2-H\ge0,\qquad
\|E_\ell\|\le
\frac{2a_{\ell+1}\alpha\,\theta^\ell}{1-\theta},
\quad \ell\ge1.
\tag{17}
\]

It uses \(R_\ell\ge R>0\) and \(R_\ell+R\le2I\).
Each \(E_\ell\) is compact, and the bound tends to zero. There is no
claim of rapid convergence when \(\delta/\alpha\) is small.

### Every mixed return is retained by the response law

The inverse in (14) is not a commuting replacement of gamma and
prime responses. To make its noncommuting expansion explicit, write

\[
T_H=T_{0,H}+K_H,\quad
T_{0,H}=(\mathcal A_0|_{QX})^*(\mathcal A_0|_{QX})\ge mI,
\quad K_H=(\mathcal J_{\mathcal S}|_{QX})^*
                 (\mathcal J_{\mathcal S}|_{QX})\ge0.
\tag{18}
\]

One known choice is
\(t=\sum_{p\in\mathcal S}4d_pq_p/(1-q_p^2)\ge\|K_H\|\).
For \(V_0=(T_{0,H}+tI)^{-1}\),

\[
V=\sum_{j\ge0}\bigl[V_0(tI-K_H)\bigr]^j V_0,
\qquad
\|V_0(tI-K_H)\|\le \frac{t}{m+t}<1.
\tag{19}
\]

If there are no prime channels, \(t=0\) and this is just \(V_0\).
Furthermore

\[
K_H=c_{\mathcal S}I_{QX}
-\sum_{m\log p<L}(\log p)p^{-m/2}
  Q(T_{m\log p}+T_{m\log p}^*)Q.
\tag{20}
\]

Equations (19)–(20) specify the order and coefficients of every
mixed gamma/prime return. Compression and the intervening resolvents
must stay between the shifts. Replacing these words by a product of
scalar Euler multipliers would change the kernel. The positive
variational definition and the norm-convergent word expansion agree.

## 4. Keep the unused low-source output

The range of \(A_H\) is closed, since \(T_H\ge\alpha+\delta\).
Let \(\Pi_H\) be the orthogonal projection onto this range. It is
given by the bounded extension of

\[
\Pi_H=A_H V A_H^*.
\tag{21}
\]

On a low input \(p\), the original source decomposes as

\[
Ap=A_HVBp+Zp,\qquad
Z=(I-\Pi_H)A|_{PX},\qquad
Z(PX)\perp\operatorname{Ran}A_H.
\tag{22}
\]

The finite-dimensional positive Gram matrix of the unused component
is therefore

\[
G=Z^*Z=M-B^*VB\ge mI_{PX}>0.
\tag{23}
\]

For the last inequality, minimize the known positive \(T\)-energy
over the high input with the low input fixed. Since
\(\langle f,Tf\rangle\ge m\|f\|^2\), its minimum is at least
\(m\|p\|^2\). Thus no positivity of an unknown Schur block is being
assumed in (23).

There is a second stable high-sector response
\(y_p=H^{-1}Bp\), whose Hessian is positive by (7).
It too is obtained from the same response:
\(H^{-1}=\sum_{j\ge0}\alpha^jV^{j+1}\), with convergence in
operator norm by (13).
Define, in the **same** output space \(\mathscr Y\),

\[
\boxed{\quad
\Phi_L(p+q)=A_HR(q+H^{-1}Bp)+Zp.
\quad}
\tag{24}
\]

The two summands are orthogonal, by (22). Nothing from the original
low-source output is omitted: its projected part is replaced by the
new coherent high response and its orthogonal part \(Zp\) is kept.
Expanding (24) gives

\[
\|\Phi_L(p+q)\|^2
=\langle q,Hq\rangle+2\Re\langle q,Bp\rangle
+\langle p,(G+B^*H^{-1}B)p\rangle.
\tag{25}
\]

Comparison with (11) proves (1), with the explicit matrix

\[
\boxed{\quad
D_N=\alpha I_{PX}+B^*(H^{-1}-V)B
=\alpha\bigl(I_{PX}+B^*VH^{-1}B\bigr)>0.
\quad}
\tag{26}
\]

The inverse difference is positive because \(H=T_H-\alpha\ge\delta\)
and hence \(H^{-1}-T_H^{-1}=\alpha VH^{-1}\ge0\).
The error operator is \(P D_N P\); its rank is exactly \(N\).
Every target coefficient and every mixed term is unchanged.

Replacing \(R\) by \(R_\ell\) in (24) gives a positive approximate
source whose exact additional error is

\[
\bigl(Q+H^{-1}BP\bigr)^*E_\ell
\bigl(Q+H^{-1}BP\bigr)\ge0.
\tag{27}
\]

It tends to zero in operator norm by (17). Thus the finite-rank
completion is obtained as a controlled limit of explicit stable
response readouts, with their residuals kept throughout.

## 5. Closedness, adjoint and the necessary slow source correction

Subtracting (22) from (24) gives, on the source domain,

\[
\Phi_L-A=
A_H(R-I)Q+
A_H(RH^{-1}-V)BP=:F.
\tag{28}
\]

The first summand extends compactly to \(X\), since on an eigenmode
of \(T_H\) with eigenvalue \(\lambda\) its magnitude is

\[
\sqrt\lambda\left(1-\sqrt{1-\alpha/\lambda}\right)
=\frac{\alpha}{\sqrt\lambda
 (1+\sqrt{1-\alpha/\lambda})}\longrightarrow0.
\tag{29}
\]

The second summand is bounded and finite rank. In particular
\(\Phi_L=A+F\) is closed, has exactly
\(\operatorname{Dom}\Phi_L=\mathcal D_{\log,L}\), has the same graph
topology as \(A\), and retains \(C_c^\infty(I_L)\) as an operator
core. Its maximal physical adjoint is

\[
\operatorname{Dom}\Phi_L^*=\operatorname{Dom}A^*,\qquad
\Phi_L^*=A^*+F^*.
\tag{30}
\]

The bounded adjoint \(F^*\) is taken in the already specified positive
Hilbert spaces. The original interval distributional-adjoint domain
is unchanged. The form identity gives
\(\Phi_L^*\Phi_L=W_L+P D_NP\), with operator domain
\(\operatorname{Dom}T_L\).

The compact correction \(F\) is **not** finite rank or in any finite
Schatten class. Note 18 and bounded-perturbation min–max give
\(\lambda_n(T_H)=\log n+O_L(1)\). Equation (29), followed by
finite-rank singular-value interlacing for the second summand, gives

\[
\sqrt{\log n}\,s_n(F)\longrightarrow\alpha/2.
\tag{31}
\]

There is therefore no conflict with note 17's obstruction. The
**form error** is now finite rank; the **coherent source correction**
that achieved it still has the necessary slow infinite-rank decay.
For every finite series length \(\ell\ge1\), the additional error
in (27) remains infinite rank in general.

## 6. The remaining arithmetic problem is an exact finite matrix

Completing the high-sector square directly in (11) gives

\[
Q_L[p+q]=
\|A_HR(q+H^{-1}Bp)\|^2+
\langle p,S_Np\rangle,
\tag{32}
\]

\[
\boxed{\quad
S_N=M-\alpha I-B^*H^{-1}B=G-D_N.
\quad}
\tag{33}
\]

Since \(p\) is arbitrary and \(q=-H^{-1}Bp\) is admissible,

\[
Q_L\ge0\quad\Longleftrightarrow\quad S_N\ge0.
\tag{34}
\]

This is a criterion, **not an assumed conclusion**. Both \(G>0\)
and \(D_N>0\) are independently known; their difference need not
be positive. Equivalently the still-unproved finite comparison is
\(G^{-1/2}D_NG^{-1/2}\le I\).

The [exact algebra program](../numerics/check_joint_response.py)
includes an invertible rational source \(A\), a positive high block,
and a negative direction of \(T-\alpha I\), for which (24)–(26)
nonetheless hold exactly. It is a non-arithmetic control showing
that the construction cannot by itself be a positivity proof.

At \(L=1\), note 18 proves that \(N=4\) is admissible with
\(\delta=1/16\). The error in (1) then has rank four and the
unresolved comparison (33) is four by four. No numerical values or
positivity certificate for that matrix are claimed here.

This deduction does not give a new all-support theorem. Any closed
semibounded form with an explicit positive shifted source and a
proved positive high compression admits the same construction.
Its new content in this investigation is the complete source law,
domain control, convergent joint-return expansion, finite-rank
residual and quantitative selection of an elementary mode cutoff.

## 7. Support compatibility and the next investigation

Choose one envelope interval \(I_{L_*}\), its prime set, remote delay
and mode projection, and construct \(\Phi_*\) there once. For every
smaller centered interval let \(j_L:L^2(I_L)\to L^2(I_{L_*})\) be
zero extension. The source \(\Phi_*j_L\) is compatible with these
inclusions, and its Gram form is

\[
\|\Phi_*j_L f\|^2
=Q_L[f]+\langle f,j_L^*P_*D_*P_*j_L f\rangle.
\tag{35}
\]

The zero-extension definition of the logarithmic domain proves
closedness and the same compact-support core on each smaller
interval. Newly listed but inactive prime returns have zero overlap;
their contacts were already retained in the envelope's matching.
This establishes a compatible family **inside one fixed envelope**.

Rebuilding the construction on a larger envelope does not generally
preserve the compressed defect in (35). Thus no single all-support
source or all-prime limit has been constructed. The finite-rank
defects on different envelopes are not to be subtracted silently.

The next arithmetic step is to derive a useful structural bound for
\(G-D_N\), or an independently specified constraint that supplies
its positive gluing, while controlling how this finite comparison
changes under enlargement of the envelope. The response formula
(19) is a concrete starting point for estimates: it retains all
prime/gamma words and has a known convergence ratio. Merely
iterating the already solved high-sector series cannot settle the
remaining matrix sign. Numerical enclosure of \(S_N\) at one length
would be a finite-support certificate, not the missing all-support
physical law.

All formulas in this note are derived from the earlier explicit
sources, ordinary positive variational responses and note 18's
comparison. The new standard-library program verifies coefficient
identities, genuinely noncommuting finite block algebra, and the
rational cutoff example. It does not validate the analytical limits
or establish arithmetic positivity.
