# Moving theta ground state, Ward residual, and the spectral-gap limit

10 October 2026. GPT-6 (Codex); serving variant and configured reasoning
effort unavailable. Internal LLM algebra checks are not independent review.

This scout develops [Program 03](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md)
with the genuine theta kernel and the signed interface of
[Note 13](../../notes/13_RECENT_HEAT_RESULTS_AND_PATHS_FORWARD_20261009.md).

## 1. Exact genuine state and the correct evolution

Use the full even theta kernel of the stable manuscript,
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}}\quad(u\ge0),
\]
and its even extension \(\Phi_e\). Set
\[
Z_t=H_t(0),\quad
\rho_t(u)=\frac{e^{tu^2}\Phi_e(u)}{2Z_t},\quad
g_t=\sqrt{\rho_t},\quad W_t=-\log\rho_t,\quad
\mu_j(t)=\int u^j\rho_t(u)\,du.
\tag{1}
\]
The factor two normalizes the full-line probability measure. Its
characteristic function is exactly
\[
C_t(x)=\int e^{ixu}\rho_t(u)\,du=H_t(x)/Z_t.
\tag{2}
\]
Thus \(H_0=\xi(1/2+ix/2)/8\) is reproduced, not an arbitrary kernel.
Theta decay implies uniform convergence of every integral and finite
parameter derivative on compact real time intervals. Direct differentiation
gives
\[
\dot Z_t=\mu_2Z_t,\quad
\dot\rho_t=(u^2-\mu_2)\rho_t,\quad
\dot g_t=\tfrac12(u^2-\mu_2)g_t,
\tag{3}
\]
\[
\dot C_t=-C_t''-\mu_2C_t,\qquad
\partial_t(Z_tC_t)=-\partial_x^2(Z_tC_t).
\tag{4}
\]
The nonlinear normalization term is necessary. Physical time does not
evolve the ground state by either sign of its annihilating Hamiltonian.

## 2. Closed operators and a moving-ground-state identity

Let \(B_t=\partial_u+W_t'/2\), initially on smooth compactly supported
functions, then take its closed maximal realization. Its adjoint is
\(B_t^\dagger=-\partial_u+W_t'/2\). Equivalently,
\[
\operatorname{Dom}B_t=\{f\in L^2:f\text{ locally absolutely continuous},
\ f'+W_t'f/2\in L^2\}.
\]
Use the analogous maximal adjoint domain. For this closed densely defined
operator, the block Dirac operator is selfadjoint on
\(\operatorname{Dom}B_t\oplus\operatorname{Dom}B_t^\dagger\). Its square
has the nonnegative components \(K_t=B_t^\dagger B_t\) and
\(\widetilde K_t=B_tB_t^\dagger\), with their product domains.
On the smooth core
\[
K_t=-\partial_u^2+W_t'^2/4-W_t''/2,\qquad B_tg_t=0.
\tag{5}
\]
The genuine theta asymptotic at \(u\to+\infty\) is
\[
W_t'(u)=4\pi e^{4u}-9-2tu+O(e^{-4u}),\quad
W_t''(u)=16\pi e^{4u}-2t+O(e^{-4u}).
\tag{6}
\]
The reflected negative tail follows by evenness. Both potentials in
\(D_t^2\) tend to \(+\infty\), locally uniformly on compact time intervals.
Their usual closed quadratic forms therefore have compact resolvent:
outside a large compact interval the potential controls the \(L^2\)
tail, and inside it the bounded-energy \(H^1\) inclusion is compact.
The zero mode of \(K_t\) is simple; the solution of
\(B_t^\dagger f=0\) is proportional to \(e^{W_t/2}\), which is not
square integrable. All domain assertions here concern this one-dimensional
spectral model, not a spatial Dirac equation for \(H_t\).

An additional exact identity follows from \(\dot W_t'=-2u\):
\[
\boxed{B_t\dot g_t=ug_t,\qquad
\|\dot g_t\|^2=\tfrac14(\mu_4-\mu_2^2),\qquad
\|B_t\dot g_t\|^2=\mu_2.}
\tag{7}
\]
Indeed \(B_t(Pg_t)=P'g_t\) for polynomial \(P\); apply this to (3).
The differentiated equation \(B_tg_t=0\) gives the same answer because
\(\dot B_t=-u\). Thus the Newman tangent has a nonzero partner component,
although the instantaneous state is a zero mode. Evolving it by
\(\pm K_tg_t=0\) would lose this tangent entirely.

## 3. Three exact Ward identities and their residual

For any polynomial insertion \(a\), all endpoint terms vanish:
\(\rho_t\) and its derivatives dominate polynomial growth.
Integrating \((a\rho_te^{ixu})'\) gives
\[
\mathbb E[aW_t'e^{ixu}]
=\mathbb E[a'e^{ixu}]+ix\mathbb E[ae^{ixu}].
\tag{8}
\]
For \(a=1,u,u^2\), this is
\[
\mathbb E[W_t'e^{ixu}]=ixC_t,\quad
\mathbb E[uW_t'e^{ixu}]=C_t+xC_t',\quad
\mathbb E[u^2W_t'e^{ixu}]=-i(2C_t'+xC_t'').
\tag{9}
\]
The first two insertions vanish at a collision; the third then equals
\(-ixC_t''\), which is generally nonzero at multiplicity two.
These are equality constraints with signed oscillatory insertions;
positivity of \(K_t\) does not assign them the required threshold sign.

Test the concrete Gaussian-closure mechanism. For any real \(\beta\), put
\(R_\beta(u)=W_t'(u)-\beta u\). Equation (9) yields
\[
\mathbb E[R_\beta e^{ixu}]=i(xC_t+\beta C_t'),\quad
\mathbb E[uR_\beta e^{ixu}]
=C_t+xC_t'+\beta C_t''.
\tag{10}
\]
If the first residual vanished for every real \(x\), uniqueness of the
Fourier transform for the integrable function \(R_\beta\rho_t\) would imply
\(R_\beta=0\). Consequently \(\rho_t\) would be Gaussian and
\(\beta C_t'=-xC_t\) would be the regular first-order closure.
The theta asymptotic (6) excludes this identity for every constant
\(\beta\). This is a sharp obstruction to this specified closure, rather
than to all possible arithmetic Dirac or Ward constructions.

At a collision the first residual vanishes automatically, while its
first \(x\)-derivative equals \(i\beta C_t''\). Small residual estimates
must therefore be proved in a norm that also controls the needed
derivative. Merely inserting the collision equations into a Ward identity
does not close the pair.

## 4. A real but small-frequency visibility bound

Let \(\lambda_t>0\) be the first positive eigenvalue of \(K_t\).
For \(h_x=e^{ixu}g_t\),
\[
B_th_x=ixh_x,\qquad
\langle h_x,K_th_x\rangle=x^2,\qquad
\langle h_x,g_t\rangle=C_t(x).
\]
The spectral gap inequality supplies a valid lower bound,
\[
\boxed{|C_t(x)|^2\ge 1-x^2/\lambda_t.}
\tag{11}
\]
It excludes zeros only for \(|x|<\sqrt{\lambda_t}\). It is stronger
in content than simply saying the Hamiltonian is nonnegative, but it
does not solve the high-height collision problem.
The admissible odd trial state \(ug_t\), orthogonal to \(g_t\), gives
\[
\lambda_t\le\frac{\|B_t(ug_t)\|^2}{\|ug_t\|^2}
=1/\mu_2(t).
\tag{12}
\]
Also \(\dot\mu_2=\mu_4-\mu_2^2\ge0\), and \(\mu_2(0)>0\).
Thus for \(t\ge0\) the frequency range available from this gap mechanism
is bounded above by the fixed number \(1/\sqrt{\mu_2(0)}\), whereas
the program's \(x=4\pi e^{\kappa/t}\) diverges as \(t\downarrow0\).
No numerical lower bound for \(\lambda_t\) has been claimed.

The positive smooth translated-kernel control from the Gaussian project
has a Dirac factorization of the same kind and an exact double
characteristic-function zero. It satisfies (7)--(10) and obeys (11);
at its collision, its gap necessarily satisfies \(\lambda_t\le x_*^2\).
This explains why a global positivity argument and the valid local
gap estimate are consistent with the control.

## 5. Threshold interface and stopping result

At \(C_t=C_t'=0\), the manuscript's normalized fourth-jet test is exactly
\[
\mathscr L(q)=(Z_t/A_t)^2
\{2C_t'''{}^2-3C_t''C_t''''-9C_t''{}^2/x^2\}.
\tag{13}
\]
The same product differentiation gives all higher deflation jets.
Every approximate arithmetic jet must still pay Note 13's measured
quadratic error; (9) supplies no opposite sign for (13).
No new approximation to theta or arithmetic block is introduced here.

The scout proves exact state matching, well-defined factorization,
a nontrivial moving-partner identity, and the limited spectral-gap
visibility estimate. It rules out constant-coefficient Gaussian closure
for the actual theta state. No theta-specific signed candidate inequality
or collision exclusion is established.

The strongest continuation is a quantitative estimate for the actual
residual \(R_\beta\), with derivatives and conditional consequences for
(13), or a different independently justified finite closure. Defining
coefficients by \(H_t'/H_t\) would introduce unknown poles rather than
prove such closure.

A definite choice for that next residual test is
\(\beta=1/\mu_2(t)\). The nonoscillatory Ward identities give
\(\mathbb E[uW_t']=1\) and
\(J_t:=\mathbb E[W_t'^2]=\mathbb E[W_t'']\), so
\[
\min_{\beta\in\mathbb R}\mathbb E[(W_t'-\beta u)^2]
=J_t-1/\mu_2(t)>0.
\tag{14}
\]
The minimum is attained at \(1/\mu_2\). Strict positivity follows from
the non-Gaussian theta asymptotic (6). This quantifies the precise
non-Gaussian score defect left by the attempted linear closure. It
is a bulk norm; at a collision the oscillatory residual in (10) still
vanishes, so (14) alone supplies no signed conditional lower bound.

All factorization and Ward formulas above are derived directly. The
general SUSY context in Note 14 is not being used as an external zeta
theorem. Files follow [LARGE_FILES.md](../../../../../LARGE_FILES.md).
