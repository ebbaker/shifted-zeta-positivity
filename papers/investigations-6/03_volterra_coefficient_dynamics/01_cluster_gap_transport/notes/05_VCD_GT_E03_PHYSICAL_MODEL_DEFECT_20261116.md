# VCD-GT-E03 r1 — Heat defect of the physical Jacobi truncation

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Explicit helper dispatch
**gpt-6.1-sol / ultra**. Separate backend attestation and the lead's
actual configuration are unavailable.

**Proved in-note within the stated class; [E05 r2 accepted without mathematical correction](../reviews/04_VCD_GT_E03_RESIDUAL_ASSESSMENT_20261116.md).** This status sentence is the only post-assessment change.
The physical finite-model defect has an entire formula and a regular
two-zero contour contribution. Taking its absolute norm before time
integration costs a four-factor degree loss times the elapsed time
against the next physical head on comparable contour geometry. The
signed contribution and the canonical margin remain unpaid. This is
an intermediate estimate and comparison under [pattern 01][a01].
See the [frozen request][request], [B01 decision][decision],
[overview][overview], [result index][results], [coefficient cluster][cluster],
[control catalog][catalog], [avoid index][avoid] and
patterns [02][a02], [07][a07] and [12][a12].

## 1. Finite-matrix heat defect

Fix a compact physical-time interval \(I=[u,v]\subset[0,1/2]\) and
use the complete even theta density. Write
\(W_\lambda(s)=e^{\lambda s^2}\Phi(s)\),
\(Z_\lambda=\int_{\mathbb R}W_\lambda(s)\,ds\), and
\(d\mu_\lambda=W_\lambda\,ds/Z_\lambda\).
For its normalized literal Fourier transform \(F_\lambda\),
\(Z_\lambda'/Z_\lambda=\int s^2\,d\mu_\lambda=\beta_1\) since
\(P_1(s)=s\). The source tail and Gram positivity give differentiability
of the moments and the recurrence coefficients on a real neighborhood
of \(I\). The exact physical equation is
\((\partial_\lambda+\partial_z^2+\beta_1)F_\lambda=0\).
The normalized monic norms are \(h_0^*=1\) and
\(h_N^*=\prod_{j=1}^N\beta_j\). The entries of \(J_N\), on sites
\(0,\ldots,N-1\), are the zero diagonal and \(a_j=\sqrt{\beta_j}\)
between sites \(j-1,j\). Set \(\beta_0=0\), and suppress time in formulas
at one fixed \(\lambda\). Write \(f=e^{izJ_N}\) and \(G_N=f_{00}\).
These conventions and the physical law
\(\dot a_j=a_j(\beta_{j+1}-\beta_{j-1})/2\) are from
[parent manuscript §§2–3][ms]. The dot means \(\partial_\lambda\).

For \(N\ge2\), let \(B=(U-L)/2\), where \(U,L\) are the strict
upper and lower parts of \(J_N^2\). Thus \(B\) is skew-symmetric
with upper entries \(B_{k,k+2}=a_{k+1}a_{k+2}/2\). The commutator
\([B,J_N]\) is symmetric and has only first off-diagonals. The
third off-diagonals cancel because both products contain the same
three successive links. On edge \(j\) the commutator is
\(a_j(\beta_{j+1}-\beta_{j-1})/2\), with the outgoing \(\beta_N\)
set to zero in this finite calculation. Hence
\[
 \dot J_N=[B,J_N]+\beta_N\beta_{N-1}\partial_{\beta_{N-1}}J_N ,
\]
where the partial derivative holds all other retained links fixed.
The derivative of the finite exponential in the direction
\([B,J_N]\) is \([B,f]\), by similarity or termwise differentiation
of its power series. Its \(00\)-entry is \(a_1a_2 f_{20}\) for
\(N\ge3\) and zero for \(N=2\). Since
\((J_N^2 f)_{00}=\beta_1 f_{00}+a_1a_2 f_{20}\) with the second term
absent at \(N=2\), and \(\partial_z^2 f=-J_N^2f\), the defect is
\[
 R_N:=(\partial_\lambda+\partial_z^2+\beta_1)G_N
    =\beta_N\beta_{N-1}\partial_{\beta_{N-1}}G_N .
 \tag{1}
\]

The finite spectral theorem gives \(G_N=(2\pi i)^{-1}
\oint_{\Sigma}e^{izw}\mathcal R_{00}(w)\,dw\), where
\(\mathcal R(w)=(w-J_N)^{-1}\), and the positively oriented
\(\Sigma\) encloses all eigenvalues in the matrix spectral variable
\(w\). It can be fixed under small changes of the coefficients.
The characteristic determinant is \(P_N(w)\) by the monic
recurrence. In the following two cofactors, expansion down the
deleted column reduces the off-diagonal factors to a single
chain. The remaining trailing determinant is \(1\) or \(w\):
\[
 \mathcal R_{0,N-1}=\frac{\prod_{j=1}^{N-1}a_j}{P_N(w)},\qquad
 \mathcal R_{0,N-2}=\frac{w\prod_{j=1}^{N-2}a_j}{P_N(w)} .
\]
These also hold for \(N=2\). In \(\partial\mathcal R=
\mathcal R(\partial J_N)\mathcal R\) the two last-edge terms coincide
by symmetry, so
\(\partial_{\beta_{N-1}}\mathcal R_{00}
=a_{N-1}^{-1}\mathcal R_{0,N-2}\mathcal R_{0,N-1}\).
Inserting (1) yields the entire identity
\[
 R_N(z)=\frac{h_N^*}{2\pi i}\oint_\Sigma
                   \frac{w e^{izw}}{P_N(w)^2}\,dw .
 \tag{2}
\]
At \(N=1\), \(G_1=1\) and \(R_1=\beta_1\). Formula (1) uses a
retained edge and therefore has domain \(N\ge2\). In (2) the integrand
at \(N=1\) uses \(P_1(w)=w\) and the residue gives \(h_1^*=\beta_1\).
There is no model two-zero cluster at \(N=1\).

## 2. Entire phase and explicit strip allowance

Let \(x_1,\ldots,x_N\) be the Gaussian nodes, the eigenvalues of \(J_N\).
Put \(q=2N\). Form \(V_N\) as the barycenter of
\((x_1,x_1,\ldots,x_N,x_N)\) with uniform probability coordinates
on the \(q\)-coordinate simplex. Write
\(\chi_N(z)=\mathbb E e^{izV_N}\).
For fixed doubled nodes let \(A_k=[s^k]\prod_j(1-s x_j)^{-2}\).
The simplex monomial integral gives
\(\mathbb E V_N^k=k!A_k/(q)_k\), where \((q)_k\) is the rising
factorial and \((q)_0=1\). Indeed the normalized simplex moment
of the coordinate monomial with powers \(k_i\) is
\(\prod_i k_i!/(q)_{\sum_i k_i}\), from successive beta integrals.
The multinomial coefficients cancel the numerator factorials.
The coefficient of \(w^{-1}\) in \(w^\ell/P_N(w)^2\) is zero for
\(\ell<q-1\) and equals \(A_{\ell-q+1}\) otherwise. Expanding
\(e^{izw}\) on \(\Sigma\) and applying these coefficient identities
therefore gives the confluent divided difference
\[
 \frac{1}{2\pi i}\oint_\Sigma \frac{e^{izw}}{P_N(w)^2}\,dw
      =\frac{(iz)^{q-1}}{(q-1)!}\chi_N(z).
\]
Both series converge absolutely on compact sets, by boundedness of
the nodes and of \(\Sigma\). See the [de Boor passage record][deboor]
for the classical contour and simplex formulas. Differentiation in \(z\) and division
by \(i\) insert the \(w\) required by (2). Thus
\[
 R_N(z)=(-1)^{N-1}h_N^*\frac{z^{2N-2}}{(2N-2)!}\Psi_N(z),
 \qquad
 \Psi_N(z)=\chi_N(z)+\frac{z\chi_N'(z)}{2N-1}.
 \tag{3}
\]
At \(N=1\), \(V_1=0\) and \(\Psi_1=1\), as in (2).

Write \(S_2=\sum_jx_j^2\), \(S_4=\sum_jx_j^4\), and take
\(L_*\ge\max_j|x_j|\). The alternating site signs conjugate \(J_N\)
to \(-J_N\); the node permutation under reflection makes \(V_N\)
symmetric. Expanding the logarithm of the knot product gives
\(A_2=S_2\) and \(A_4=(S_2^2+S_4)/2\). In particular
\[
 \mathbb E V_N^2=\frac{2S_2}{(q)_2},\qquad
 \mathbb E V_N^4=\frac{12(S_2^2+S_4)}{(q)_4}.
 \tag{4}
\]
All odd \(A_k\) vanish and the even coefficients are nonnegative.
For real \(t\) and \(|t|L_*<q\), \((q)_k\ge q^k\) gives
\[
 \mathbb E e^{tV_N}\le\prod_{j=1}^N(1-tx_j/q)^{-2}
 \le\exp\!\left(\frac{t^2 S_2}{q^2(1-t^2 L_*^2/q^2)}\right).
 \tag{5}
\]
The last inequality follows after pairing positive and negative
nodes from \(-\log(1-r)\le r/(1-r)\) for \(0\le r<1\).
This is the doubled-node estimate, with no unbounded source variable.

For \(0\le Y\le1\) and \(|\Im z|\le Y\), the centered formulas and
Taylor's integral remainder give
\[
 |\chi_N(z)-1|\le \tfrac12|z|^2 M_Y,\qquad
 |\chi_N'(z)|\le |z| M_Y,\qquad
 M_Y=\mathbb E(V_N^2 e^{Y|V_N|}).
\]
For the derivative, subtract the zero mean from
\(\mathbb E(iV_N e^{izV_N})\) and integrate the first-order difference.
The Cauchy–Schwarz inequality and symmetry bound \(M_Y\) by
\(\sqrt{2\,\mathbb E V_N^4\,\mathbb E e^{2YV_N}}\).
Use \(B_j=\operatorname{arcosh}^2(2j+12)/16\) from
[parent manuscript §4][ms]. For \(N\ge2\) set
\[
 \overline L_N=2\sqrt{B_{N-2}},\quad
 \overline S_N=2(N-1)B_{N-2},\quad
 \overline Q_N^{\,V}=\frac{12(\overline S_N^2+
                         \overline L_N^2\overline S_N)}{(2N)_4}.
\]
The Jacobi row sums give \(L_*=\overline L_N\) and the trace
gives \(S_2=2\sum_{j<N}\beta_j\le\overline S_N\). Then
\(S_4\le\overline L_N^2\overline S_N\). The strict inequality
\(\overline L_N<N\) follows by inverting
\(\cosh(2N)\ge1+2N^2+2N^4/3>2N+8\) for \(N\ge2\).
Consequently the following allowance is valid jointly on the full
physical-time interval and strip:
\[
 \boxed{\;
 |\Psi_N(z)-1|
 \le \varepsilon_N^R(|z|,Y):=
 |z|^2\left(\tfrac12+\frac1{2N-1}\right)
 \sqrt{2\overline Q_N^{\,V}
       \exp\!\left(
       \frac{Y^2\overline S_N}{N^2(1-Y^2\overline L_N^2/N^2)}
       \right)} .\;}
 \tag{6}
\]
Take \(\varepsilon_1^R=0\). Since \(B_{N-2}=O(\log^2(N+1))\),
the exponential is bounded uniformly in \(Y\), and (6) is
\(O(|z|^2\log^2(N+1)/N)\). This estimate also holds at unrestricted
\(\Re z\) with the displayed \(|z|^2\) factor. A relative phase
statement needs the allowance below one.

## 3. Regular two-zero contour defect

Use the [completed E02 transfer][e02r] and its [proof][e02].
Take one fixed circle \(\Gamma=\{|z-a|=\rho\}\), with real center,
positive orientation and length \(L=2\pi\rho\). At every time both
\(F_\lambda\) and \(G_{N,\lambda}\) are nonzero on the circle and
have exactly two counted zeros inside. Their pairs lie in an inner
convex region with distance at least \(b>0\) from \(\Gamma\).
Write \(Q_N=(z-c_N)^2-D_N\) for the monic model pair polynomial,
\(G_N=Q_N A_N\) on the closed disk and a neighborhood, and
\(h_N=A_N'/A_N\), with prime denoting \(z\)-derivative here.
The unit is nonvanishing in the closed disk. Its divided difference
\(K_N\) at the roots of \(Q_N\) is \(h_N'(c_N)\) when \(D_N=0\).
Use the corresponding \(c,D,Q,K\) for \(F\). Squares of half
separations are signed real discriminants by conjugation symmetry.
Centers and discriminants are differentiable in time through any
internal merger, by their fixed-contour moments.

For \(p_{k,N}=(2\pi i)^{-1}\oint_\Gamma z^k G_N'/G_N\,dz\), set
\(c_N=p_{1,N}/2\), \(D_N=p_{2,N}/2-c_N^2\).
Under the integral, time differentiation of \(G_N'/G_N\) is the
\(z\)-derivative of \(\dot G_N/G_N\). Integration by parts gives
\(\dot p_{k,N}=-k(2\pi i)^{-1}\oint_\Gamma z^{k-1}\dot G_N/G_N\,dz\).
Using \(\dot G_N=-G_N''-\beta_1G_N+R_N\) in
\(\dot D_N=\dot p_{2,N}/2-2c_N\dot c_N\) cancels the scalar
potential, since \(\oint_\Gamma(z-c_N)\,dz=0\). In the remaining
heat term use
\[
 G_N''/G_N=Q_N''/Q_N+2Q_N'h_N/Q_N+h_N'+h_N^2.
\]
The last two terms are holomorphic. The integral of
\((z-c_N)Q_N''/Q_N\), divided by \(2\pi i\), is 2, using its
\(2/z\) Laurent term at infinity. For the cross term,
\(2(z-c_N)Q_N'/Q_N=4+4D_N/Q_N\). The constant integrates to zero
against \(h_N\), and the second term gives \(4D_NK_N\) by the
contour formula for the divided difference. Thus
\[
 r_N=-\frac{1}{2\pi i}\oint_\Gamma(z-c_N)\frac{R_N}{G_N}\,dz,
 \qquad
 \dot D_N=2+4K_ND_N+r_N .
 \tag{7}
\]
The contour only requires the outer modulus floor. In particular the
formula holds at \(D_N=0\), when \(\dot D_N=2+r_N\).
All quantities in (7) are real by conjugation symmetry. The same
calculation for \(F\) gives \(\dot D=2+4KD\). For an algebraic
interpretation of \(r_N\), the same moment differentiation at
fixed time with respect to the last retained link gives
\(r_N=\beta_N\beta_{N-1}\partial_{\beta_{N-1}}D_N\) locally
where the boundary count is unchanged. This does not estimate its sign.

At \(N=2\), write \(a_1=\sqrt{\beta_1}\) and \(t=a_1z\).
Then \(G_2=\cos t\) and \(\dot a_1=a_1\beta_2/2\), giving
\[
 R_2(z)=-\frac{a_1\beta_2 z}{2}\sin t
       =-\frac{h_2^*z^2}{2}\frac{\sin t}{t}.
\]
The doubled-node law has \(V_2/a_1\) of density
\(3(1-w^2)/4\) on \([-1,1]\), by grouping the uniform four-coordinate
simplex into two pairs. Integrating this density gives
\(\chi_2(z)=3(\sin t-t\cos t)/t^3\) with its removable value.
Differentiating \(t^3\chi_2(z)\) as a function of \(t\) gives
\(\Psi_2(z)=\sin t/t\), the same residual as (1) and (2).
For any fixed contour containing two cosine zeros, these roots
scale as \(a_1^{-1}\), so \(\dot D_2=-\beta_2D_2\).
The residue of \(R_2/G_2\) at either root \(z_j\) is
\(\beta_2z_j/2\); the contour in (7) gives
\(r_2=-\beta_2D_2\). Since \(G_2''/G_2=-\beta_1\),
the heat part of (7) equals zero, checking the full model equation.

## 4. Signed transport, including all model and transfer terms

Take a collar logarithm with \(\sup_\Gamma|\log(F/G_N)|\le\ell_N\),
model boundary logarithmic derivative bound \(M_N\), and the
coordinate allowances \(e_N\ge|c-c_N|\), \(d_N\ge|D-D_N|\).
The E02 estimate, denoted here by \(\kappa_N\) to distinguish it
from the heat defect \(R_N\), is
\[
 |K-K_N|\le\kappa_N=
 \frac{L\ell_N}{\pi b^3}
 +\frac{LM_N}{2\pi b^4}\big((4\rho-2b)e_N+d_N\big),\quad
 e_N=\rho\ell_N/2,\quad d_N=\rho(2\rho-b)\ell_N
 \tag{8}
\]
when using the stated E02 coordinate estimates. Tighter paid
coordinate bounds may replace the last two expressions. For example,
a uniform modulus floor \(m_N\) and a strict uniform error
\(\delta_N<m_N\) on \(\Gamma\) give a collar by continuity and
\(\ell_N=-\log(1-\delta_N/m_N)\) using the model denominator.
A strict separated homotopy on the collar is another acquisition
described in [E01 §4][e01]. A transferred count alone supplies
neither a collar budget nor an inner buffer. Also
\(|K_N|\le LM_N/(2\pi b^2)\) by the E02 formula with kernel \(1/Q_N\).

Use
\[
 \begin{aligned}
 S_N(t)&=4\int_t^v K_N(s)\,ds,\quad W_N(t)=e^{S_N(t)},&
 E_K(t)&=4\int_t^v\kappa_N(s)\,ds,\\
 W(t)&=\exp(4\int_t^v K(s)\,ds),&
 \mathcal C_N(x)&=2\int_x^v W_N(t)\,dt,\qquad
 \mathcal C(x)=2\int_x^v W(t)\,dt,\\
 \mathfrak R_N(x)&=\int_x^v W_N(t)r_N(t)\,dt,&
 \mathfrak T_N^+(x)&=2\int_x^v W_N(t)(e^{E_K(t)}-1)\,dt .
 \end{aligned}
\]
The discrepancy \(|\mathcal C-\mathcal C_N|\) is at most
\(\mathfrak T_N^+\) from the exponential bounds. For the physical
margin \(\mathcal M(x)=D(v)-\mathcal C(x)=W(x)D(x)\), (7) gives
\[
 \begin{aligned}
 W_N(x)D_N(x)&=D_N(v)-\mathcal C_N(x)-\mathfrak R_N(x),\\
 \mathcal M(x)-W_N(x)D_N(x)
   &=D(v)-D_N(v)+\mathfrak R_N(x)
                              -(\mathcal C(x)-\mathcal C_N(x)).
 \end{aligned}                                                    \tag{9}
\]
The error evolution itself, with \(e=D-D_N\), is
\[
 \begin{aligned}
 \dot e&=4K_N e+4(K-K_N)D-r_N,\\
 W_N(x)e(x)&=e(v)+\mathfrak R_N(x)
                  -4\int_x^v W_N(t)(K-K_N)(t)D(t)\,dt .
 \end{aligned}                                                    \tag{10}
\]
The last integral is bounded in modulus by
\(4(\rho-b)^2\int_x^v W_N(t)\kappa_N(t)\,dt\); both roots are in the
disk of radius \(\rho-b\) about \(a\), so their half-separation
has modulus at most \(\rho-b\). The endpoint term in (10) may be
enclosed with \(d_N(v)\).

Let \(L_v\le D(v)\) be acquired without transport, for example
from counted endpoint contour moments and their errors. A sufficient
strict margin at \(x=u\) is
\[
 W_N(u)D_N(u)+L_v-D_N(v)+\mathfrak R_N(u)-\mathfrak T_N^+(u)>0 .
 \tag{11}
\]
Then \(D>0\) throughout \(I\) since \(\mathcal C(x)\) decreases as
\(x\) increases. A nonnegative margin allows \(D(u)=0\), with
strict positivity for \(u<x\le v\) when \(u<v\). At \(u=v\)
the integrals vanish. Replacing \(\mathfrak R_N\) by the endpoint
identity in (9) recovers the model cost \(\mathcal C_N\).
Thus the exact identities alone add no signed numerical estimate.

For the evaluation ledger, let \(\widetilde K_N\) have model
error \(\eta_K(t)\) (including outer contour/coordinate evaluation)
and let \(\widehat S_N(t)\) approximate \(4\int_t^v\widetilde K_N\)
with uniform-in-\(t\) error \(\eta_S(t)\). Set
\(s(t)=\eta_S(t)+4\int_t^v\eta_K\) with its nonnegative integral
enclosed above, and \(\widehat W(t)=e^{\widehat S_N(t)}\).
Then \(W_N\le\widehat W e^s\) and
\(|W_N-\widehat W|\le\widehat W(e^s-1)\).
For a model \(\widetilde r_N\) with error \(\eta_r(t)\),
\[
 |W_N r_N-\widehat W\widetilde r_N|
 \le\widehat W\big(e^s\eta_r+(e^s-1)|\widetilde r_N|\big).
 \tag{12}
\]
To pay \(\eta_r\) for a contour evaluator, write \(g=2\rho-b\).
For an approximate center, numerator and denominator with errors
\(\gamma_c,\gamma_R,\gamma_G\) on the circle, suppose
\(\gamma_G<m_N\le\inf_\Gamma|G_N|\) and
\(\sup_\Gamma|\widetilde R_N|\le\widetilde T\). Subtract the
defect integrands in (7), using \(|z-c_N|\le g\), to get the
allowance
\[
 \eta_r \;=\; \frac{L}{2\pi}\left[
 \frac{g\gamma_R}{m_N}
 +\frac{g\widetilde T\gamma_G}{m_N(m_N-\gamma_G)}
 +\frac{\gamma_c\widetilde T}{m_N-\gamma_G}\right]
 +\eta_{\Gamma,r}.
 \tag{13}
\]
Here \(\eta_{\Gamma,r}\) encloses the error of integrating the
evaluated model integrand. The quantities in (13) may depend on
time. An analytic exact integral has no evaluation allowance.
A quadrature for the signed \(\widehat W\widetilde r_N\) needs
its own error added to the integral of (12). For the transfer
term in (11), evaluate and enclose above the integral of
\(2\widehat W e^s(e^{\widehat E_K}-1)\), where
\(\widehat E_K\ge E_K\) includes integration of (8).
Both time integrations need bounds for interpolation/quadrature
and exponent evaluation where applicable. The endpoint product
\(W_N(u)D_N(u)\) uses the same product error as (12) with the
paid model endpoint error, and \(D_N(v)\) needs its own enclosure.
Use the lower enclosures of the signed terms and upper enclosures
of the subtracted terms in (11). Samples alone supply no continuous
time bound. Neither integration introduces a denominator involving
the internal separation of either pair.

## 5. Equal coefficient data and the absolute-integration comparison

The finite head \(G_N\) uses \(\beta_1,\ldots,\beta_{N-1}\) at
each time. The exact heat defect adds \(\beta_N\) in (1)–(3);
the interior derivatives of the retained coefficients are supplied
by the physical Volterra law at this cost. The same data specify
\(G_{N+1}\) pointwise in time. Each retained link first enters
the corresponding model Taylor germ at order \(2j\) by the one
first walk to site \(j\) and back. The leading nonzero term in
(3) uses \(h_N^*=\prod_{j=1}^N\beta_j\), so the last link enters
the defect independently of the retained prefix. The exact moment
and exponential expressions for \(\Psi_N\) depend only on the
nodes of \(J_N\), and (6) needs no actual coefficients.

The [completed E01 return][e01r] and [proof §§2–5][e01] give
jointly in \(\lambda\in I\)
\[
 F_\lambda(z)-G_{N+1,\lambda}(z)
  =(-1)^{N+1}\frac{h_N^*\beta_{N+1}z^{2N+2}}{(2N+2)!}
       E_{N+1,\lambda}(z),\qquad
 |E_{N+1,\lambda}(z)-1|\le\epsilon_{N+1}(|z|,Y)
 \tag{14}
\]
for \(|\Im z|\le Y\le1\). The identity is entire. The phase
allowance is \(O(|z|^2\log^2(N+1)/N)\) with a uniform constant.
The actual next-head error amplitude uses the unacquired
\(\beta_{N+1}\), and its bound can use
\(\beta_{N+1}\le B_N-\beta_N\le B_N\), so (14) gives a paid
allowance at the existing prefix. The variance and fourth moment
of the error law at degree \(j\) generally use, respectively,
links through \(\beta_{j+1}\) and \(\beta_{j+2}\); its
degree-only allowance acquires neither. For \(j=1\) the head is
constant, and the actual residual \(R_1=\beta_1\) buys \(G_2\).
See [parent E21][e21], [E22][e22] and [E24][e24] for the
time-zero antecedents of (14).

Set \(\Pi_N=(2N-1)(2N)(2N+1)(2N+2)\). On any fixed compact
\(A\subset\{|\Im z|\le1,\ z\ne0\}\), put \(Z_A=\sup_A|z|\),
\(p=\varepsilon_N^R(Z_A,1)\) and \(q_*=\epsilon_{N+1}(Z_A,1)\).
When \(p,q_*<1\), (3) and (14) give
\[
 \frac{\Pi_N}{\beta_{N+1}|z|^4}\frac{1-p}{1+q_*}
 \le\frac{|R_N(z)|}{|F_\lambda(z)-G_{N+1,\lambda}(z)|}
 \le\frac{\Pi_N}{\beta_{N+1}|z|^4}\frac{1+p}{1-q_*}.
 \tag{15}
\]
This is an actual pointwise comparison, uniform in \(\lambda\)
and \(z\in A\) after the factor \(1/(\beta_{N+1}|z|^4)\) is
extracted. In particular its lower growth is at least of order
\(N^4/\log^2(N+1)\) on \(A\) for all large \(N\), using
\(\beta_{N+1}\le B_N\). The same formula without the two-sided
phase comparison states the exact leading ratio near zero for
each fixed \(N\). It compares a heat residual with a field error.
The residual is not itself a time-integrated discriminant error.

For a contour comparison let \(\Gamma\) lie in the strip,
\(Z_*=\sup_\Gamma|z|>0\), and choose uniform model floors
\(m_j\le\inf_{I\times\Gamma}|G_j|\) for \(j=N,N+1\).
For \(N+1\), assume the direct comparator's count, collar and
inner buffer have been paid with the same \(b\), either by
independent verification or transfer. Write
\(H=\sup_I h_N^*\) and choose one paid
\(\overline\beta\ge\sup_I\beta_{N+1}\), for example \(B_N\)
or \(\sup_I(B_N-\beta_N)\). Take \(p,q_*\) as above with
\(Z_*\) in place of \(Z_A\); the corresponding upper bounds
hold even if the circle contains \(z=0\).
Define
\[
 T_R=\frac{H Z_*^{2N-2}}{(2N-2)!}(1+p),\qquad
 \delta_+=\frac{H\overline\beta Z_*^{2N+2}}{(2N+2)!}(1+q_*).
 \tag{16}
\]
The absolute contour bound from (7) is
\(|r_N|\le C_\Gamma T_R/m_N\), where
\(C_\Gamma=Lg/(2\pi)=\rho(2\rho-b)\).
For a paid uniform \(M\ge \sup_I K_N\), one can take
\[
 |\mathfrak R_N(u)|\le
 A_R=C_\Gamma (T_R/m_N)Q_\Delta(M),\quad
 Q_\Delta(M)=\int_0^\Delta e^{4M t}\,dt,\quad \Delta=v-u .
 \tag{17}
\]
For \(M\ne0\) this last factor is \((e^{4M\Delta}-1)/(4M)\);
at \(M=0\) it is \(\Delta\). A paid signed primitive can replace
this factor by the smaller or equal \(\int_u^v W_N\), if available.
For the direct endpoint contour discriminant the E02 collar moment
estimate gives the snapshot allowance
\[
 A_{\rm dir}= C_\Gamma[-\log(1-\eta)],\qquad
 \eta=\delta_+/m_{N+1}<1 .
 \tag{18}
\]
This is one uniform pointwise budget on \(I\); evaluating it at
one time can also use the corresponding local data. From
(16)–(18), for these particular uniform allowances,
\[
 \frac{A_R}{A_{\rm dir}}
 =\frac{m_{N+1}}{m_N}\,Q_\Delta(M)
    \frac{\eta}{-\log(1-\eta)}
    \frac{\Pi_N}{\overline\beta Z_*^4}\frac{1+p}{1+q_*}.
 \tag{19}
\]
On a fixed compact circle, for comparable floors,
\(0<\eta\le1/2\), and bounded \(M\), this ratio is comparable to
\(\Delta\Pi_N/(\overline\beta Z_*^4)\) for large degree and
\(\Delta>0\). Indeed \(\eta/[-\log(1-\eta)]\) stays between
\(1/2\) and 1, the phase factors approach one, and
\(Q_\Delta(M)/\Delta\) is bounded above and below under the
stated conditions. With \(\overline\beta=B_N\) the degree
and time factor is of order \(\Delta N^4/\log^2(N+1)\)
for the fixed circle. A shorter slab changes the payment by its
elapsed time, and unequal floors enter explicitly. Equation
(19) compares the absolute-residual allowance alone with the
direct allowance. The other transport, endpoint and evaluation
budgets in (8)–(13) remain. The comparison establishes no lower
bound on the signed \(\mathfrak R_N\) or on the cost of evaluating
it by a method that exploits cancellation.

The direct tests are \(D_j(x)-d_j(x)>0\) at a chosen slice, or
its positive uniform lower enclosure over \(I\) for a full slab.
They require the same outer zero count and collar data but no
model evolution estimate. A separately paid direct complete-source
contour evaluator can use exactly the same moment comparison.
If the unnormalized Fourier numerator and mass have errors
\(\epsilon_{\rm num},\epsilon_Z\) against \(A\) and \(Z_{\rm app}>0\),
respectively, and \(Z_\lambda\ge
Z_{\min}>0\), the field error against \(A/Z_{\rm app}\) is at most
\((\epsilon_{\rm num}+\|A/Z_{\rm app}\|\epsilon_Z)/Z_{\min}\) on the
contour. This follows by subtracting the normalized values.
The Fourier numerator \(A\) must be a holomorphic evaluator
with the needed collar and symmetry properties for the direct
moment test. Complete-source truncation, quadrature and mass
enclosures are independent inputs to this comparator. Separated
root jets offer another comparison only where their slope and
separation data are independently paid.

## 6. Quadratic check, controls and scope

For the unnormalized exact heat field
\(F_\lambda=(z-a)^2-2(\lambda-T)\) and model \(G=F\), the heat
defect with its zero normalization potential is zero and \(K=K_N=0\).
On a buffered circle one has \(D(v)=2(v-T)\) and
\(\mathcal C(u)=2(v-u)\). The strict margin is exhausted at
\(u=T\) and the exact margin is negative for \(u<T\).
A time scalar normalization changes only the potential which
cancels in the contour argument above. This tests the sign,
endpoint orientation and uniform treatment of a double root.

The exact finite and contour identities use the literal Fourier/heat
premise, positive recurrence coefficients where used and the specified
pair geometry. The degree bound uses the separate adjacent envelope,
and (14) uses the source cosh input. The analytical screen is against
[controls12][catalog], [E01 §6][e01], [E02 §4][e02] and
[discussion28 §5][discussion]. The strict margin of any counted
tube ending later than its double event and starting at that event
is exhausted by the exact physical identity.

| Control | Premises and scope |
| --- | --- |
| Exact quadratic heat field | Passes the local contour hypotheses with a zero heat defect, and exhausts the gap at the event. It lacks the positive theta source and its Jacobi probability law. |
| Weighted-square sources | Pass the envelope and the error-law tests at their stated events. They fail full canonical reflection and the unchanged square coefficients, which the algebraic defect does not use. The recorded finite-source class also lacks a finite all-real global anchor. |
| Euler-factor sources | Fail unchanged ordinary theta and Dirichlet coefficients. The tested member \(c=1/2,p=23\) fails the index-zero envelope at time zero; this gives no family-wide envelope verdict. A threshold witness alone supplies no specified counted pair. |
| Reflected super-Gaussian, smooth shape and positive-primitive sources | Fail unchanged integer-square theta arithmetic. The super-Gaussian fails the inherited exponential score confinement, while the smooth/primitive families' weaker quantitative premises are untested in their catalog parameter ranges. Their local heat and contour identities still apply to counted tubes. |
| Atomic and continuous finite-profile thresholds | Fail the unchanged full theta profile and the catalog's eventual-simplicity premise. Atomic chains terminate; the finite matrix calculation applies at indices with the required positive norms. The inherited three-atom event fails the index-one adjacent bound. |
| Finite-prime, finite-head and finite-score controls | Fail the full canonical identities despite preserving selected finite data. The applicable law/phase tests in E01 are consistent with this. Varying-source high events and finite-data matches do not give a fixed canonical tube. |
| RH-conditional normalized endpoint controls | Fail ordinary Dirichlet arithmetic and retain RH as a premise. Their endpoint doubles screen any claim of strictness at a nonnegative endpoint margin. |
| Changed polynomial observation kernels and actual-profile relaxations | Fail, respectively, the literal Fourier/heat observation or the premise of a prescribed actual field with a counted pair. |

The proved quantitative limitation concerns the specific
absolute contour and time allowance (16)–(19) with its geometry
and phase inputs. A canonical tube, actual coefficient data,
incoming \(L_v\), evaluation enclosures and a signed estimate
that beats the equal-data direct comparator remain open. The
algebraic part of candidate A survives. The next research question
for B02 is an acquired source-sensitive cancellation or a
different justified consumer of the same inputs, with E05 pending.
No numerical campaign or new control certificate was used.

[request]: ../research-progress/handoffs/VCD-GT-E03-r1.md
[decision]: ../brainstorm/notes/01_VCD_GT_B01_SIGNED_DEFECT_DECISION_20261116.md
[overview]: ../research-overview/01_VCD_GT_RESEARCH_OVERVIEW_20261116.md
[ms]: ../../manuscript/main.tex
[deboor]: ../../references/04_QUADRATURE_ERROR_PHASE_PASSAGES_20261116.md
[e01]: 03_VCD_GT_E01_PHYSICAL_TIME_SIGNED_ERROR_20261116.md
[e01r]: ../research-progress/handoffs/VCD-GT-E01-r1-return.md
[e02]: 04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md
[e02r]: ../research-progress/handoffs/VCD-GT-E02-r1-return.md
[e21]: ../../notes/20_VCD_E21_COMPLETE_ERROR_PROBABILITY_LAW_20261116.md
[e22]: ../../notes/21_VCD_E22_QUANTITATIVE_ERROR_PHASE_20261116.md
[e24]: ../../notes/22_VCD_E24_DIRECTED_ERROR_AND_PREFIX_COMPARISON_20261116.md
[discussion]: ../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md
[results]: ../../../../../result-summaries/README.md
[cluster]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
