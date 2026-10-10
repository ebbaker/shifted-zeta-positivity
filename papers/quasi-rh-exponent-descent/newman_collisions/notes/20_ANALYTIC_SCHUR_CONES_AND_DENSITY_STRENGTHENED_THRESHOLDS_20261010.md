# Analytical Schur cones and density-strengthened thresholds

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This is an internal LLM derivation,
not independent mathematical validation. No numerical sweeps were used.
The three Schur regroupings,
both threshold polynomial coefficients, and the fourth-center difference
were checked by exact integer-coefficient polynomial arithmetic (six
identities).

This continues [Heat Note 19](19_HIGHER_SCHUR_PAYMENTS_AND_MULTI_CUTOFF_SIGNED_CONTINUATION_20261010.md)
and [Heat Note 12](12_THRESHOLD_COLLISION_JETS_AND_PAID_LAGUERRE_TEST_20261009.md).
All statements below are conditional
on their full holomorphic-disk remainder bound and, where used, their imported
all-real deflated mirror inequality. None establishes that the prescribed
arithmetic coefficients satisfy the resulting cone.

## 1. A robust cone with nonzero lower finite jets

Freeze the physical time, center, coordinate scale \(L\), and natural
integer cutoff \(N\). Let \(f_j=F_{t,N}^{(j)}(x)\),
\(q_j=Q_t^{(j)}(x)\), and let \(\eta>0\) be the complete
holomorphic-disk bound of Heat Note 8. The real disk map
\[
g(\zeta)=\frac{Q_t(x+\zeta/L)-F_{t,N}(x+\zeta/L)}{\eta}
       =\sum_{j\ge0}\alpha_j\zeta^j,\qquad |g|\le1,
\]
therefore gives \(q_j=f_j+j!\eta L^j\alpha_j\).
The finite jets here are the physical raw derivatives. Centered-moment
approximations have their additional Bell-residual payments.

Write the normalized finite jets and normalizer as
\[
A=\frac{f_2}{\eta L^2},\qquad
B=\frac{f_3}{\eta L^3},\qquad
C=\frac{f_4}{\eta L^4},\qquad
\Gamma=\frac{\gamma}{L^2}.
\]
At a candidate \(q_0=q_1=0\), set the first two real Schur parameters
\[
a=-f_0/\eta,\qquad
\lambda=-\frac{f_1}{\eta L(1-a^2)}.
\]
This section assumes \(|a|,|\lambda|<1\). As in Note 19, impossible
parameters already exclude the candidate, and boundary parameters have fixed
higher jets and must be treated without division.

Define
\[
H=1-a^2,\quad J=1-\lambda^2,\quad d=HJ,\quad
\widehat A=A-2Ha\lambda^2,\quad
m=\widehat A-2d,\quad K=\widehat A+2d,
\quad B_c=B+6Ha^2\lambda^3.
\tag{1}
\]
Here \(m\) is a curvature lower bound, not a root multiplicity; the
integer multiplicity in Section 4 is defined there separately.
Assume \(m>0\). Thus every compatible genuine second derivative has
positive sign. For \(v\in[-1,1]\), put \(T=1-v^2\). The remaining
Schur parameters are \(v,r,s\in[-1,1]\). Directly regrouping Note 19 gives
\[
\begin{split}
\alpha_2={}&dv-Ha\lambda^2,\\
\alpha_3={}&dTr-d\lambda v^2-2da\lambda v+Ha^2\lambda^3,\\
\alpha_4={}&dT\{(1-r^2)s-vr^2\}
             -2d\lambda T(v+a)r+k_4(v),\\
k_4(v)={}&d\lambda^2v^3+2da\lambda^2v^2-HaJ^2v^2
             +3da^2\lambda^2v-Ha^3\lambda^4.
\end{split}
\tag{2}
\]
Consequently
\[
X=\frac{q_2}{\eta L^2}=\widehat A+2dv\in[m,K],\qquad
Y=\frac{q_3}{\eta L^3}=Y_0(v)+6dTr,
\]
where
\[
Y_0(v)=B_c-6d\lambda(v^2+2av).
\tag{3}
\]
The normalized necessary threshold expression is
\[
\frac{\mathscr L(q)}{\eta^2L^6}=2Y^2-3XZ-\Gamma X^2,
\qquad Z=\frac{q_4}{\eta L^4}.
\]
Since \(X>0\), maximizing in \(s\) chooses \(s=-1\). At that value,
\[
Z=C+24k_4(v)-24dT
       +24dT(1-v)r^2-48d\lambda T(v+a)r.
\tag{4}
\]
The coefficient of \(r^2\) in the threshold expression is
\[
-D(v),\qquad
D(v)=72dT(1-v)\{\widehat A-d(1-v)\}\ge0.
\tag{5}
\]
This sign is the essential correlated cancellation. Independently chosen
second, third and fourth derivative errors do not preserve (5).

The linear coefficient has the useful exact simplification
\[
24dT S(v),\qquad
S(v)=Y_0(v)+6X\lambda(v+a)
=B_c+6\lambda\{dv^2+\widehat Av+\widehat Aa\}.
\tag{6}
\]
Thus the mixed \(a\lambda v\) terms cancel. For \(-1<v<1\), completing
the square gives
\[
\max_{|r|\le1}\{24dT S(v)r-D(v)r^2\}
\le\frac{2d(1+v)S(v)^2}{\widehat A-d(1-v)}
\le\frac{4d}{\widehat A}S(v)^2.
\tag{7}
\]
The last inequality follows because
\((1+v)/(\widehat A-d+dv)\) is increasing when
\(\widehat A>2d\). At \(v=\pm1\), the actual linear and quadratic
coefficients both vanish, so (7) remains an upper bound by direct evaluation.
No maximizer at a changing quadratic vertex needs to be found.

The signed scalar bounds used below are explicit. First,
\(v^2+2av\) has exact range \([-a^2,1+2|a|]\), so set
\[
B_*=
\max\bigl\{|B_c+6d\lambda a^2|,
             |B_c-6d\lambda(1+2|a|)|\bigr\}.
\tag{8}
\]
Then \(|Y_0(v)|\le B_*\). Since
\(dv^2+\widehat Av\) is strictly increasing on \([-1,1]\), set
\[
S_*=
\max\bigl\{
|B_c+6\lambda(d-\widehat A+\widehat Aa)|,
|B_c+6\lambda(d+\widehat A+\widehat Aa)|
\bigr\}.
\tag{9}
\]
Then \(|S(v)|\le S_*\). Equations (8) and (9) retain signs of the actual
third finite derivative and the forced first Schur parameter; they are
stronger than replacing each monomial by its absolute value.

For a lower bound on the fourth-derivative center, define
\[
\rho=d\{J(1-a)+2a\lambda^2\}.
\tag{10}
\]
Assume \(\rho>0\), and put
\[
C_*=C-24d-24Ha^3\lambda^4
              -\frac{54d^2a^4\lambda^4}{\rho}.
\tag{11}
\]
Then
\[
C+24k_4(v)-24dT\ge C_*.
\tag{12}
\]
Indeed, \(\lambda^2v^3\ge-\lambda^2v^2\), so its left side is at least
\[
C-24d-24Ha^3\lambda^4
       +24\rho v^2+72da^2\lambda^2v,
\]
and completing its square in \(v\) gives (11). The unconstrained
quadratic minimum is sufficient; restricting to \([-1,1]\) can improve it.

Write \(\Gamma_+=\max(\Gamma,0)\) and
\(\Gamma_-=\max(-\Gamma,0)\). If \(C_*\ge0\), equations (3)--(12)
prove the fully explicit analytical bound
\[
\boxed{
\frac{U_{\rm Schur}}{\eta^2L^6}
\le -3mC_*+2B_*^2+\frac{4d}{\widehat A}S_*^2
     -\Gamma_+m^2+\Gamma_-K^2.}
\tag{13}
\]
Therefore the strict signed cone
\[
\boxed{
3mC_*+\Gamma_+m^2
>2B_*^2+\frac{4d}{\widehat A}S_*^2+\Gamma_-K^2}
\tag{14}
\]
excludes an all-real-time multiple zero under the imported threshold
inequality. Formula (14) permits nonzero \(f_0,f_1,f_3\) and either sign
of \(\gamma\). It involves only arithmetic operations, absolute values
and two endpoint maxima. It does not require a numerical search.

For negative genuine second derivatives, multiply both \(Q\) and \(F\)
by \(-1\), replace \((A,B,C,a,\lambda)\) by their negatives, and apply
the same theorem. The threshold expression and \(\gamma\) are invariant
under this simultaneous change. This covers a second signed cone.

## 2. A particularly simple central and one-sided version

If \(\lambda=0\), then \(d=H\), \(\widehat A=A\),
\(B_*=S_*=|B|\), and \(C_*=C-24H\). Consequently, for
\(A>2H\) and \(C\ge24H\),
\[
\boxed{
\frac{U_{\rm Schur}}{\eta^2L^6}
\le-3(A-2H)(C-24H)
       +\left(2+\frac{4H}{A}\right)B^2
       -\Gamma_+(A-2H)^2+\Gamma_-(A+2H)^2.}
\tag{15}
\]
This allows any interior \(a\), so a nonzero finite value \(f_0\) is
allowed. With \(a=0\), \(H=1\). With \(B=0\) and \(\Gamma\ge0\),
(15) recovers Note 19's bound
\(-3(A-2)(C-24)\). For \(B\ne0\), its new quadratic payment
\((2+4/A)B^2\) follows from correlation, whereas an independent error box
would continue to admit order-one positive corners when \(B\to0\).

For the illustrative finite-jet center \((A,C)=(3,25)\), (15) gives
\[
\frac{U_{\rm Schur}}{\eta^2L^6}
\le -3+\frac{10}{3}B^2-\Gamma_++25\Gamma_-.
\tag{16}
\]
For instance, at \(\Gamma=0\), the whole open interval
\(|B|<3/\sqrt{10}\) is excluded. This is a proved tolerance of the
local analytical model, not evidence that actual heat coefficients lie in
that model cone.

## 3. A scalar tolerance corollary

For an explicitly uniform perturbation bound, suppose
\(|a|\le h<1\), \(|\lambda|\le\ell<1\), and set
\[
R=(1-h)-(1+h)\ell^2>0,
\qquad A_0=A-2h\ell^2,
\qquad m_0=A-2-2h\ell^2>0,
\qquad K_0=A+2+2h\ell^2,
\]
\[
P_4=24h^3\ell^4+\frac{54h^4\ell^4}{R},
\quad C_0=C-24-P_4\ge0,
\]
\[
B_0=|B|+6\{\ell(1+2h)+h^2\ell^3\},
\]
\[
S_0=|B|+6h^2\ell^3
                +6\ell\{1+(A+2h\ell^2)(1+h)\}.
\tag{17}
\]
Then \(\rho\ge dR>0\), \(m\ge m_0\),
\(K\le K_0\), \(C_*\ge C_0\),
\(B_*\le B_0\), \(S_*\le S_0\), and
\(4d/\widehat A\le4/A_0\). Hence
\[
3m_0C_0+\Gamma_+m_0^2
>2B_0^2+\frac{4}{A_0}S_0^2+\Gamma_-K_0^2
\tag{18}
\]
is a sufficient uniform cone.

The fourth-center perturbation in (17) is
\(O(h^3\ell^4+h^4\ell^4/R)\). In particular there is no separate
first-order \(24h\) or \(24\ell^2\) loss in this center bound. Those
terms remain attached to the beneficial \(v^2\) curvature before the
square is completed. This explains why the result is more useful than an
independent Taylor-error triangle estimate. The dominant noncentral costs
arise instead through the small first Schur parameter in \(B_0,S_0\).
For input intervals, the displayed constants must use proven lower bounds
for \(A,C,\Gamma_+\), and proven upper bounds for all adverse terms;
midpoint substitution is invalid.

## 4. A factorial-normalized central cone for every multiplicity

There is an equally transparent conditional hierarchy that does not become
vacuous at multiplicity four. Fix an integer \(m\ge2\), and suppose a
candidate has \(q_0=\cdots=q_{m-1}=0\) and the finite lower jets also
satisfy \(f_0=\cdots=f_{m-1}=0\). Repeated Schwarz implies
\(g(\zeta)=\zeta^m h(\zeta)\), with \(h\) a real Schur map. Thus the
first three still-free remainder coefficients have exactly the form
\[
\alpha_m=v,\qquad \alpha_{m+1}=Tr,
\qquad \alpha_{m+2}=T\{(1-r^2)s-vr^2\}.
\tag{19}
\]
Now use factorial-normalized finite jets
\[
A=\frac{f_m}{m!\eta L^m},\quad
B=\frac{f_{m+1}}{(m+1)!\eta L^{m+1}},\quad
C=\frac{f_{m+2}}{(m+2)!\eta L^{m+2}},\quad
\chi_m=\frac{b_x+m/(4x^2)}{L^2}.
\tag{20}
\]
Note 12's nonvacuous deflated condition is
\[
\mathscr D_m
=\frac{q_{m+1}^2}{(m+1)^2}
-\frac{2q_mq_{m+2}}{(m+1)(m+2)}
-\left(b_x+\frac{m}{4x^2}\right)q_m^2\ge0.
\tag{21}
\]
After division by \((m!)^2\eta^2L^{2m+2}\), its left side is
\[
(B+Tr)^2-2(A+v)\bigl[C+T\{(1-r^2)s-vr^2\}\bigr]
-\chi_m(A+v)^2.
\tag{22}
\]
Assume \(A>1\), \(C\ge1\). Maximize in \(s\) by choosing \(-1\).
The constant fourth-center term is \(C-1+v^2\), and the quadratic
\(r^2\) coefficient is
\[
-T(1-v)(2A+v-1)\le0.
\]
The linear \(r\) coefficient is \(2BT\). Completing its square costs
at most
\[
\frac{(1+v)B^2}{2A+v-1}\le\frac{B^2}{A}.
\]
The ratio is increasing because \(A>1\). Write
\(\chi_{m,+}=\max(\chi_m,0)\) and
\(\chi_{m,-}=\max(-\chi_m,0)\). Consequently
\[
\boxed{
\frac{\sup\mathscr D_m}{(m!)^2\eta^2L^{2m+2}}
\le-2(A-1)(C-1)+\left(1+\frac1A\right)B^2
      -\chi_{m,+}(A-1)^2+\chi_{m,-}(A+1)^2.}
\tag{23}
\]
A strict negative right side excludes this candidate at an all-real time.
For \(m=2\), conversion from factorial units and
\(\gamma=18b_x+9/x^2\) gives exactly the central version of (15).
The structural constants in (23) do not deteriorate with \(m\) after
factorial normalization.

The exact lower finite zeros in this extension are a restrictive condition;
they are not inferred from the genuine lower zeros. Nonzero lower finite
jets would require additional forced Schur steps, just as Section 1 does
for \(m=2\). That remains a useful analytical extension, not an established
uniform multiplicity argument for the prescribed sums.

## 5. Genuine zero density strengthens the target cone

[Heat Note 21](21_DEFLATED_LOCAL_GROWTH_AND_THRESHOLD_MULTIPLICITY_20261010.md)
uses the existing uniform count input from
[Polymath, Theorem 1.5(iv)](https://arxiv.org/html/1904.12438v2#S1).
Let \(C_{\rm count}\ge0\) be an absolute constant such that
\[
|N_T(R)-p_T(R)|\le C_{\rm count}\log(2+R),
\qquad 0<T\le\tfrac12,\quad R\ge4\pi,
\]
with the actual time-dependent smooth main term
\[
p_T(R)=\frac{R}{4\pi}\log\frac{R}{4\pi}-\frac{R}{4\pi}
       +\frac{11}{8}+\frac{T}{16}\log\frac{R}{4\pi}.
\]
The count includes every zero with \(0<\Re\rho\le R\), with
multiplicity. The constant is existential here; no numerical value is
assigned. Put
\[
D_0=8\pi(4C_{\rm count}+1),\qquad
X_0=\max\{(4\pi)^2,2D_0,3\}.
\tag{24}
\]
At an all-real time, let \(x\ge X_0\) be a root of exact multiplicity
\(m\). On the right block \((x+D_0,x+2D_0]\),
\[
p_T'(R)=\frac1{4\pi}\log\frac{R}{4\pi}+\frac{T}{16R}
       \ge\frac{\log x}{8\pi}.
\]
Also \(2+x+2D_0\le2+2x\le x^2\), so each endpoint count error is at
most \(2C_{\rm count}\log x\). Therefore the block contains at least
\[
\left(\frac{D_0}{8\pi}-4C_{\rm count}\right)\log x
=\log x
\]
roots, counted with multiplicity. At the all-real time they are real,
with distances from \(x\) at most \(2D_0\). This block is disjoint
from both the deflated cluster at \(x\) and the forced mirror cluster
at \(-x\). Hence the inverse-square sum over the fully deflated roots
satisfies
\[
S_0\ge\frac{m}{4x^2}+\frac{\log x}{4D_0^2}.
\tag{25}
\]
The complete-deflation identity proved in Note 21 is
\[
\mathscr D_m=q_m^2\left(S_0-\frac{m}{4x^2}\right).
\]
Thus the genuine threshold necessary condition strengthens to
\[
\boxed{\mathscr D_m\ge\frac{\log x}{4D_0^2}q_m^2.}
\tag{26}
\]
This is genuine root-density information, beyond the forced mirror
alone. For \(m=2\), \(\mathscr L=18\mathscr D_2\), so (26) is
equivalent to
\[
2q_3^2-3q_2q_4-\gamma_{\rm count}q_2^2\ge0,
\qquad
\boxed{\gamma_{\rm count}=\gamma+\frac{9\log x}{2D_0^2}.}
\tag{27}
\]
Consequently every order-four cone above remains valid on this height
range with \(\Gamma\) replaced by \(\gamma_{\rm count}/L^2\).
In the general-m cone (23), replace \(\chi_m\) by
\[
\boxed{\chi_{m,\rm count}
 =\chi_m+\frac{\log x}{4D_0^2L^2}.}
\tag{28}
\]
The positive and negative parts in each cone must be those of the new
coefficient. In the physical shrinking sector \(x=4\pi e^L\),
with \(D_0\) fixed, both added normalized coefficients are
\(\Theta(1/L)\). This is a genuine but asymptotically modest improvement
in the necessary signed target.

Changing the quadratic coefficient changes its approximation payment.
The full holomorphic-disk bound \(\eta\) and its Schur jet body are
unchanged, and the cones above pay the changed coefficient directly by
using its new positive and negative parts. If one instead applies a
finite-expression triangle payment, a physical Bell-residual payment, or
a complete quadratic dual, every allowance depending on the changed
coefficient must be recomputed. In particular the fixed quadratic block
must use the new normalizer coefficient, and any coefficient-dependent
scale in an analytical remainder must change with it. An old payment
cannot simply be appended to a new finite signed expression. The
complete arithmetic transformation and its retained primitive frontier
are described in
[project 09 Note 6](../09_prime_phase_torus/notes/6_ANALYTIC_COMMON_FACTOR_SMOOTHING_AND_PRIMITIVE_SIGNED_FRONTIER_20261010.md).

No actual prescribed finite jets have been shown to enter a strict cone,
with or without the density strengthening. A future uniform theorem
would have to prove entry on a specified shrinking subsector with all
coefficient-dependent payments, exact physical derivatives, and remaining
multiplicity and parameter coverage accounted for.

## 6. What has and has not been achieved

* The main order-four cone is a rigorous bound for the complete real Schur
  body with forced nonzero \(f_0,f_1\), allowing \(f_3\ne0\) and either
  normalizer sign. It exposes an exact mixed-term cancellation and retains
  the decisive adverse \(r^2\) sign. No search over Schur parameters is
  needed for this sufficient condition.
* Its \(m>0\) assumption forces \(q_2\ne0\). Therefore any compatible
  candidate is ordinary double. Multiplicity at least three is already
  incompatible with the same second-derivative cone, but obtaining that cone
  on all relevant candidates has not been shown.
* The general-m lemma gives a nonvacuous analytical paid deflation test under
  explicitly stated additional lower-jet hypotheses. It uses derivatives
  through \(m+2\), as required by Note 12.
* The genuine uniform zero count strengthens the required threshold sign
  by (26), giving the density-adjusted coefficients (27)--(28). Its
  constant remains symbolic, and its normalized gain is of order \(1/L\).
* The remaining central research obligation is arithmetic: establish that
  complete physical finite jets on a specified shrinking subsector fall in
  an oriented strict cone with the stated full-disk payment and exact
  normalizer. None of these inequalities supplies that missing sign.
* The bounds are sufficient, not sharp. Their deliberate losses are:
  unrestricted completion of the \(r\) square, separate endpoint maxima for
  \(Y_0\) and \(S\), and a global lower bound for the fourth center. They
  can fail on genuine exclusion cones; such failure is inconclusive.

The next analytical use is to rewrite an actual complete arithmetic jet
identity as a signed derivative shape plus a residual, and prove that
residual lies inside (14) or (18), with the density-adjusted coefficient
where applicable. In this role, the Schur calculation is a transparent
target inequality rather than the principal arithmetic theorem.
