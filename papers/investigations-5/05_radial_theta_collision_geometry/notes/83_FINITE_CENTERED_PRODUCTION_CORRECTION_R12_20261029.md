# Finite centered production correction and complete centered dissipation

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), effort ultra**,
Investigation05 **chat0033**. Parent research synthesis with same-model contributing derivations and
checks; no independent specialist review.

**Status: proved in-note within the inherited prepared radial solution
class, from [Note82][n82] and the accepted R10/R11 inputs; pending E08
assessment.** The exact common-carrier decomposition of the real residual
pays a finite cumulative alpha-weighted error for the selected I1 term.
The carrier contribution retains its full source and feedback-path
dependence and has no newly proved sign. The direct method supplies the
same bound; no primitive-specific gain or improvement of the complete
R11 energy allowance is asserted.

## 1. Fixed errors and inputs

Keep (T,A)=(1/4,2), the complete theta source, unit preparation, original
feedback, actual common-path jets and the existing positive carrier h.
Write M=int h, m_j=int J_j, a_j=m_j/M, j=0,1,2, and
\[
 e_j=J_j-a_jh,\qquad e=(e_0,e_1),\qquad
 a=(a_0,a_1),\qquad \tau=(2a_1,a_1+2a_2).
                                                               \tag{1}
\]
All masses are constant. The path alpha is the actual original feedback
path, not the feedback computed from a h or from e. Along that path,
J_j,h and e_j solve the same scalar equation L_s; no physical derivative
of alpha occurs.

[Note82][n82] supplies fully initial-paid constants L_j and T_j with
\[
 \|e_j(s)\|_2^2\le L_j e^{-B(s)/2},\qquad
 \|\nabla e_j(s)\|_2^2\le T_j e^{-B(s)/2}\quad(s\ge0).
                                                               \tag{2}
\]
These hold from s=0; no unpaid early-time interval is hidden. They include
the unit preparation and first absolute moment of the zero-mass prepared
error. Set
\[
 E_{01}=\sqrt{L_0+L_1},\quad T_{01}=\sqrt{T_0+T_1},\quad
 C_c=3B_0+\tfrac34,
\]
\[
 C_Z=\tfrac14T_{01}+C_cE_{01}+\sqrt5\sqrt{L_1}+2\sqrt{L_2},
 \qquad C_F=B_1T_{01}+B_0E_{01}.                                \tag{3}
\]
The coefficients Cb<=1/4 and ||omega c||infinity<=Cc are already proved
in [Note76][n76]. B0,B1 are the full cutoff commutator budgets:
\(B_1=\|\omega\beta\|_\infty\) and
\(B_0=\|\omega\gamma\|_\infty\) for
\(C_1=\beta\cdot\nabla+\gamma\).

Retain the accepted uniform actual-field budgets
\[
 \|W\|_2^2=E_0,\quad G\le KE_0,\quad
 Y=\|Z\|_2^2\le E_0\mathfrak y,
 \quad 0\le\alpha\le\bar\alpha=2K/3,
\]
\[
 Z_*:=\sqrt{E_0\mathfrak y},\qquad
 F_*^{(1)}:=\sqrt{E_0}(B_1\sqrt K+B_0).
                                                               \tag{4}
\]
The last symbol denotes a bound for ||omega C1 W||2, not the full
weighted energy F_R. The existing lower bound is
\[
 \alpha(s)\ge a_*:=\frac15
         \left(\frac{6\pi^2E_0}{M^2}\right)^{2/3}>0.
\]
The positive physical mass margin remains an
upstream premise of K. It is not recovered from the error decomposition.

## 2. Exact residual decomposition, including preparation and the sphere

Define
\[
 W_c=ah,\quad W_e=e,\quad
 \mathcal T_c=\tau h,\quad\mathcal T_e=(2e_1,e_1+2e_2).
\]
The genuine weighted residual splits exactly as
\[
 \boxed{Z=Z_c+Z_e,\qquad
 Z_c=\omega\{a\mathcal A_T h-\tau h\},\quad
 Z_e=\omega\{\mathcal A_Te-(2e_1,e_1+2e_2)\}.}                 \tag{5}
\]
Here A_T=b dot grad+c is the same fixed source operator. In particular,
Z_c is generally nonzero and is not a new zero-residual ansatz.
By (2), coefficient multiplication and the triangle inequality,
\[
 \boxed{\|Z_e(s)\|_2\le C_Ze^{-B(s)/4},\qquad
       \|\omega C_1e(s)\|_2\le C_Fe^{-B(s)/4}.}                \tag{6}
\]
The sqrt5 coefficient is exactly the norm of (2e1,e1); the second jet
contributes 2||e2||2. This estimate needs only the displayed H1 errors,
not a derivative of Z_e or a third spectral jet.

Both unweighted residuals R_c=Z_c/omega and R_e=Z_e/omega satisfy
\[
 \partial_sR_c=L_sR_c+[\mathcal A_T,L_s]W_c,\qquad
 \partial_sR_e=L_sR_e+[\mathcal A_T,L_s]e.                       \tag{7}
\]
All coefficients and cutoff derivatives in C0+alpha C1 remain. The
carrier is evolving through L_s and the path remains determined by W.

Preparation is also exact. Let h_raw=1_(r>=1)rho_T(1+u²), so h0=K1*h_raw.
Then A_T h_raw=2 rho_T u² on r>=1, distributionally including r=1:
the radial coefficient r log r kills the jump delta. Thus
\[
 R_{c,0}=a[\mathcal A_T,K_1*]h_{\rm raw}
          +K_1*\{\mathbf1_{r\ge1}\rho_T
                         [2a u^2-\tau(1+u^2)]\}.                 \tag{8}
\]
The raw carrier mismatch and the preparatory commutator are both kept.
For the actual theta pair, the original preparation residual remains
[A_T,K1*]W_raw. More explicitly, with e_raw=W_raw−a h_raw,
\[
 \boxed{R_{e,0}=[\mathcal A_T,K_1*]e^{\rm raw}
           +K_1*\{-a\mathcal A_T h_{\rm raw}+\tau h_{\rm raw}\}.}   \tag{8a}
\]
The second term is the true raw mismatch of the error triple. It does not
vanish merely because every e_j has zero integral. The sum of (8) and
(8a) is exactly the original prepared residual; neither is replaced by a
zero-mismatch surrogate.

At r=1, b=c=0 and omega=1/4. Therefore
\[
 Z_c(s,1)=-\tfrac14\tau h(s,1),\quad
 Z_e(s,1)=-\tfrac14(2e_1,e_1+2e_2)(s,1).                         \tag{9}
\]
Together these are the original combined sphere cancellation R+T=0.
No separately singular quotient or new boundary condition is introduced.
All norms and pairings include the entire inner ball.

## 3. The selected signed production has an integrable correction

Let
\[
 I_1=2\langle Z,\omega C_1W\rangle,\qquad
 I_c=2\langle Z_c,\omega C_1W_c\rangle,\qquad \delta I=I_1-I_c.
\]
Linearity gives the exact expansion
\[
 \boxed{\delta I
   =2\langle Z_e,\omega C_1W\rangle
      +2\langle Z,\omega C_1e\rangle
      -2\langle Z_e,\omega C_1e\rangle.}                        \tag{10}
\]
The last minus sign avoids counting the error–error term twice.
No independent estimate of the carrier's H1 norm is required. Use (4),
(6) and whole-space Cauchy–Schwarz, and define
\[
 A_I=2(C_ZF_*^{(1)}+Z_*C_F),\qquad B_I=2C_ZC_F.
\]
Then
\[
 \boxed{|\delta I(s)|\le A_Ie^{-B(s)/4}+B_Ie^{-B(s)/2}.}         \tag{11}
\]
Since B'=alpha>=0, for every 0<=t<S,
\[
 \int_t^S\alpha|\delta I|\,ds
 \le4A_I\{e^{-B(t)/4}-e^{-B(S)/4}\}
       +2B_I\{e^{-B(t)/2}-e^{-B(S)/2}\}.                        \tag{12}
\]
Consequently
\[
 \boxed{\int_t^\infty\alpha|I_1-I_c|\,ds
       \le4A_Ie^{-B(t)/4}+2B_Ie^{-B(t)/2},
 \qquad \int_0^\infty\alpha|I_1-I_c|\,ds\le4A_I+2B_I.}        \tag{13}
\]
The upper bound does not require B(infinity)=infinity; the positive
mass/energy regime supplies B>=a_*s in any event. If desired (11) gives
ordinary time decay with B replaced by a_*s. More importantly, (12)
pays the complete initial interval because (2) is valid at s=0.

Equation (13) concerns a correction. It is not a bound for
integral alpha|I1|, integral alpha|Ic|, total dissipation or total B.
It also proves no sign for I_c. In scalar form,
\[
 I_c=2|a|^2\langle\omega\mathcal A_T h,\omega C_1h\rangle
        -2(a\cdot\tau)\langle\omega h,\omega C_1h\rangle.        \tag{14}
\]
The carrier h, canonical source operator, cutoff and original alpha path
remain inside these pairings. Formula (14) is not a mass-only formula,
a stationary profile or a limiting-profile theorem.

## 4. Complete production bookkeeping

Here \(\mathcal F_R=G+Y+Q_2\) and
\(\mathscr D_R=N+2\|\nabla Z\|_2^2+2\|\nabla J_2\|_2^2\)
are the inherited actual energy and retained dissipation in Note76.

Retain l=log omega, h_omega=d−2v dot grad l, N=||Delta W||2², the actual
Q2=||J2||2², and the exact nonnegative radial remainder H_rad(W). The
full original identity, with only I1 split, reads
\[
\begin{split}
 \mathcal F_R'&+2N+2\|\nabla Z\|_2^2+2\|\nabla J_2\|_2^2
                       +\alpha\mathscr H_{\rm rad}(W)\\
 &=2\int|\nabla l|^2|Z|^2+2\langle Z,\omega C_0W\rangle\\
 &\quad+\alpha\left\{10G+\frac{21}{4}E_0
                  +\int h_\omega|Z|^2+\int d|J_2|^2+I_c\right\}
                  +\alpha\delta I .                          \tag{15}
\end{split}
\]
The spatial second derivatives, full C0, actual second jet, weighted
potential, whole inner ball and radial remainder have not been replaced
by carrier counterparts. In particular no H2 estimate of e is being
silently used to change C0 production.

For an explicit paid inequality, absorb the C0 principal product by
2A2 sqrt(YN)<=N+A2²Y and retain the other inherited Young payments.
Using h_omega<=265/24, d<=6 and 2|grad l|²<=8 gives
\[
\begin{split}
 \mathcal F_R'&+\mathscr D_R+\alpha\mathscr H_{\rm rad}(W)\\
 &\le A_1G+\kappa_0Y+A_0E_0\\
 &\quad+\alpha\{10G+\tfrac{21}{4}E_0
                       +\tfrac{265}{24}Y+6Q_2+I_c\}
                  +\alpha\delta I,
 \quad \kappa_0=8+A_2^2+A_1+A_0.                               \tag{16}
\end{split}
\]
Its integrated correction is at most (12); all remaining integrals
in (16) remain as written. The original sharper source-exterior
completion, with kappa1=274/25+B1+B0, remains a separately valid complete
bound. One must not simultaneously import that I1 completion into (16)
and then retain another full I_c+delta I payment for the same term.
Both estimates are available to the equally informed direct comparator.

Thus (13) is a genuine improvement over an O(B(S)) constant-envelope
allowance for this specified approximation error. It does not by itself
improve the full R11 bound F_R<=F_* or its fixed-window dissipation
allowance: I_c and the rest of (15) still require their ordinary payments.
There is no claim of finite total actual dissipation, convergence of alpha,
stationarity of h or a new physical domain.

## 5. The complete centered dissipation is integrable

There is a supporting cost consequence for the **centered fields**
themselves. It does not compare the entire actual production with an
entire carrier production. Set
\[
 E_e=\|e\|_2^2,\quad G_e=\|\nabla e\|_2^2,\quad
 Y_e=\|Z_e\|_2^2,\quad Q_e=\|e_2\|_2^2,\qquad
 \mathcal F_e=G_e+Y_e+Q_e,
\]
\[
 \mathscr D_e=\|\Delta e\|_2^2
                  +2\|\nabla Z_e\|_2^2+2\|\nabla e_2\|_2^2.
                                                               \tag{17}
\]
The energy F_e does **not** include E_e. In particular E_e is not
preserved and alpha is not computed from e.

The full inherited weighted proof applies to this radial error triple:
\[
 \boxed{\mathcal F_e'+\mathscr D_e
                 +\alpha\mathscr H_{\rm rad}(e)
       \le(\kappa_0+\kappa_1\alpha)(\mathcal F_e+E_e),}
 \qquad \kappa_1=274/25+B_1+B_0.                                \tag{18}
\]
To see why no extra hypothesis is being introduced, each e_j solves
L_s e_j; its residual is (5) and obeys (7), including the mismatch (8a).
The gradient identity has instantaneous E_e,
G_e'+2||Delta e||2²+alpha H_rad(e)=alpha(10G_e+21E_e/4).
The weighted residual and e2 energy identities are the same linear
identities used in the inherited proof. C0's principal term is absorbed
into one unit of ||Delta e||2². The exterior C1 completion uses the exact
residual definition and the canonical coefficient inequality 2<=k<=6,
not a raw-zero-mismatch premise. Its actual relation vector is
(2e1,e1+2e2). The same full cutoff and inner-region payments give (18).
No step requires E_e'=0 or feedback recomputed from e.

By (2) and (6), put
\[
 C_E=L_0+L_1,\qquad
 C_{\rm energy}=T_0+T_1+C_Z^2+L_2.
\]
Then
\[
 E_e\le C_Ee^{-B/2},\qquad
 \mathcal F_e\le C_{\rm energy}e^{-B/2}.                         \tag{19}
\]
The existing actual-path lower bound alpha>=a_*>0 gives
\[
 \int_t^\infty e^{-B(s)/2}ds\le\frac2{a_*}e^{-B(t)/2},\qquad
 \int_t^\infty\alpha(s)e^{-B(s)/2}ds\le2e^{-B(t)/2}.
\]
Integrate (18) directly, retain F_e(S)>=0 and use (19). This proves
\[
 \boxed{\int_t^\infty
       \{\mathscr D_e+\alpha\mathscr H_{\rm rad}(e)\}\,ds
 \le\left[C_{\rm energy}
      +2(C_{\rm energy}+C_E)(\kappa_0/a_*+\kappa_1)\right]
                              e^{-B(t)/2}.}                    \tag{20}
\]
The whole centered-dissipation integral, including the initial interval,
is finite by setting t=0. This is a direct integration of the differential
inequality for F_e. Reusing an integrating-factor formula for F_e+E_e
as if E_e were constant would be invalid and is not done here.

Every original diffusion/cutoff/source cost for this centered triple is
present. Equation (20) supplies no finite total **actual** dissipation:
the actual fields also contain the evolving carrier. Likewise it is not
a bound for the difference of the entire actual and carrier productions,
whose other cross terms have not been replaced in (15). No stationary
carrier or limiting alpha is assumed.

## 6. What the primitive does and does not add

The raw errors are exactly
\[
 e_j^{\rm raw}=\mathbf1_{r\ge1}\rho_T
          \{u^j\cos^{(j)}(2u)-a_j(1+u^2)\}.                    \tag{21}
\]
The same primitive transfer and common-path duality apply, with the full
joint derivative of this bracket times exp(Tu²) and the transported test.
There is a boundary detail worth preserving: the bracket's value at zero
is delta_(j0)−a_j, and its first u derivative is zero for j=0,1,2. Hence
the primitive sphere contribution for an error test chi is
\[
 (\delta_{j0}-a_j)
       \{\chi(1)/16+A_\theta(1)\chi_r(1)/4\}.                  \tag{22}
\]
In particular the j=1,2 errors need not have zero boundary terms even
though the original j=1,2 jets do. No endpoint is discarded by zero
spatial mass of e_j. The primitive source/preparation reconstruction
still gives the exact same initial errors that the direct method receives.

The direct proof uses synchronous contraction, zero mass, paid moments,
Fourier diffusion, bounded feedback and the actual residual definition.
It yields (2), (6) and (13) without a favorable primitive sign. Thus this
single declared R12 consumer is complete by the equally informed direct
method. The stopping rule applies; no replacement consumer is selected
merely to preserve a primitive advantage claim.

The [result index][results], [control register][controls] and
[pattern index][avoid] govern the interpretation. Admitted controls with
the same bounded common path share the mixing and production correction;
at an actual zero-mass collision the global physical mass premise used
to acquire the uniform feedback path fails. Low-mark bounds need not
reject events elsewhere. Variable observation controls cannot import the
literal-cosine mass payment. Primitive positivity itself separates none
of these classes. These statements preserve the recorded scopes and do
not exclude future source-specific correlation estimates.

[n82]: 82_COMMON_CARRIER_SYNCHRONIZATION_R12_20261029.md
[n76]: 76_UNIFORM_RESIDUAL_AND_FIXED_JET_CLOSURE_R11_20261029.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
