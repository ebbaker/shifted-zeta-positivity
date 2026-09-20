# An all-input cumulative append bound from forward/backward energy

20 September 2026. Prepared for Edward Baker.

**Model:** OpenAI GPT-6 (Codex; developer-provided identity).
**Effort setting:** not exposed in this session; not inferred.
**Status:** internal computer-assisted proof: analytic operator reduction,
outward rational certificates at 40 and 60 digits, and a separate floating
reduction check. Independent specialist review remains outstanding.

## 1. Result

For the original complete arithmetic transfer, with unchanged normalization,
\[
 L=\frac12,\quad h=\frac1{20},\quad w=\frac1{1000},\qquad
 V_{w,L+h}=\begin{pmatrix}X&0\\Y&Z\end{pmatrix},
\]
\[
 E=I-X^*X,\qquad F=I-ZZ^*,\qquad
 \boxed{\ \|F^{-1/2}YE^{-1/2}\|<\frac{951}{1000}<1.\ }
 \tag{1.1}
\]
This bound covers every old input and every new-output test in the ordinary
interval Hilbert spaces. The inherited \(E,F\succeq\delta I\),
\(\delta=.000049998\), justifies their inverses; the new calculation also
supplies sufficient local positivity to justify these inverses independently.
No enlarged-window central certificate is substituted for the coupling task.

The key additional step is an exact forward/backward energy factorization
of the cumulative mixed response. It transfers a relative generator-coupling
bound to (1.1), using the **actual** diagonal evolution on both sides.
All four spatial blocks of that relative coupling are controlled, including
the two one-sided complements and the full corner complement. The latter
uses a Carleman **operator norm**, not its divergent central HS norm or an
HS sum over positive-shift logarithmic channels.

The certified unshifted block comparison is
\[
 \begin{pmatrix}.87&.265\\.081&.493\end{pmatrix},
 \qquad \left\|\begin{pmatrix}.87&.265\\.081&.493\end{pmatrix}\right\|
       <.95.
 \tag{1.2}
\]
The bounded perturbation for \(0\le s\le w\) raises the proved upper
estimate to less than \(.950012797294\), leaving the rational margin in
(1.1). The .802 finite quotient remains a diagnostic lower quotient and is
not used in this proof.

This closes the designated bounded append test. It is not a new positivity
horizon: larger windows were already studied elsewhere in the program.
It does not provide an all-depth continuation, a physical Wilson transfer,
or a localization construction. Instantaneous positivity is used here as
a sufficient tool; no claim is made that the method already handles a
trajectory with indefinite instantaneous local forms.

## 2. Exact cumulative transfer of a relative generator bound

Write the complete causal generator on the split interval as
\[
 G_{s,L+h}=\begin{pmatrix}G_{s,L}&0\\-2H_s&G_{s,h}\end{pmatrix},
 \qquad Q_{s,\ell}=\Re G_{s,\ell}.
 \tag{2.1}
\]
In reflected old coordinates \(r=L-y\),
\[
 (H_s f)(t)=\int_0^L
 \left[\frac{e^{-5(t+r)/2}}{1-e^{-2(t+r)}}-e^{(t+r)/2}\right]
 \cosh(s(t+r))f(L-r)\,dr.
 \tag{2.2}
\]
The gamma corner and the signed pole are both present. Since \(L+h<\log2\),
no delayed integer contribution enters this window.

Let \(U_\ell(t,s)\) be the forward evolution for the original generator
between shifts \(s\) and \(t\), with \(U_\ell(s,s)=I\). In particular
\(U_\ell(t,0)=V_{t,\ell}\). This is an evolution family, not an assumed
bounded inverse of a positive-shift compact operator. Its construction and
the energy identities are justified below.

**Energy-transfer lemma.** If, for all \(0\le s\le w\),
\[
 |\langle v,H_s f\rangle|
 \le\kappa\sqrt{Q_{s,L}[f]\,Q_{s,h}[v]},
 \tag{2.3}
\]
then \(\|F^{-1/2}YE^{-1/2}\|\le\kappa\).

Indeed, the triangular evolution equation and Duhamel's formula give
\[
 Y=2\int_0^w U_h(w,s)H_sV_{s,L}\,ds.
 \tag{2.4}
\]
The two exact energy balances are
\[
 E[f]=2\int_0^w Q_{s,L}[V_{s,L}f]ds,
\qquad
 F[v]=2\int_0^w Q_{s,h}[U_h(w,s)^*v]ds.
 \tag{2.5}
\]
The second identity is essential: differentiate
\(\|U_h(w,s)^*v\|^2\) with respect to the **starting** shift \(s\).
Its endpoint difference is \(\|v\|^2-\|Z^*v\|^2\), the new-output
defect. It is not the forward new-input energy integral with the reflection
forgotten. Applying (2.3) inside (2.4) and then Cauchy--Schwarz in shift gives
\[
 |\langle v,Yf\rangle|\le\kappa\sqrt{E[f]F[v]}.
 \tag{2.6}
\]
The coercive defects turn this bilinear inequality into the claimed norm
bound. There is no operator exponential of an instantaneous lower metric.

### Evolution and domains

Here is a construction that does not divide by \(V_s\). On a window let
\(\mathsf S_u\) be right translation by spatial delay \(u\), with zero
history. The positive gamma part of the absorbed central generator is
\[
 A_\Gamma=\int_0^\infty (I-\mathsf S_u)\nu(du),\qquad
 \nu(du)=\frac{2e^{-5u/2}}{1-e^{-2u}}du.
 \tag{2.7}
\]
Both \(\int_0^1 u\nu(du)\) and \(\int_1^\infty\nu(du)\) are finite.
Truncating at \(u=\epsilon\) gives compound-Poisson convolution probability
measures
\(e^{-t\nu_\epsilon(\mathbb R_+)}\sum_{n\ge0}t^n\nu_\epsilon^{*n}/n!\).
Their Laplace transforms converge to
\(\exp[-t\int(1-e^{-pu})\nu(du)]\); the finite first moment gives
tightness, and uniqueness of Laplace transforms gives the convolution
semigroup limit. Averaging the contraction translations against these
measures constructs a strongly continuous contraction semigroup with
generator \(-A_\Gamma\).

The full \(G_0=(w_0+4)I+A_\Gamma+2R_{-1/2}\) differs by bounded
operators on a finite window. Also \(G_s-G_0\) is a bounded,
norm-continuous perturbation, of norm at most \(s^2/8\) on either local
window. Bounded perturbation and its convergent variation-of-constants
series therefore construct \(U_\ell(t,s)\). One can take the zero-left-trace
\(H^1\) domain as a core before closure: causal resolvent smoothing
\((I+\epsilon\partial_x)^{-1}\) commutes with the gamma generator and
converges in its graph norm. Smooth approximation on this domain supplies
the differentiation identities. The same argument after reflection treats
the adjoints.

The positive lower bounds proved below give the local contraction and
energy estimates by differentiating scalar squared norms, followed by
density. Identities (2.5) first hold on the core. Their energy maps extend
boundedly into the shift-integrated form spaces; equivalently one integrates
away from the endpoints and uses the strong endpoint limits. This extends
(2.5)--(2.6) to every \(L^2\) input. The off-diagonal generator is bounded
by the Carleman estimate below, so the full triangular evolution satisfies
(2.4). The original beta/pole transfer solves this same initial-value
problem on the core and is bounded on each finite window; uniqueness
identifies its mixed block with (2.4).

## 3. Endpoint-aware local metrics with their cross blocks controlled

Use the original finite tower with \(M=128\),
\[
 T_{M,\ell}=w_0I+\sum_{n=0}^{M-1}\frac2{a_n}(I-\Re S_{1/a_n})
             +2|c_\ell\rangle\langle c_\ell|
             -2|s_\ell\rangle\langle s_\ell|,
\]
\[
 a_n=2n+\tfrac12,\quad
 c_\ell(x)=\cosh((x-\ell/2)/2),\quad
 s_\ell(x)=\sinh((x-\ell/2)/2).
 \tag{3.1}
\]
The positive omitted gamma forms imply \(Q_{0,\ell}\succeq T_{M,\ell}\).
The certificate rounds the scalar **down** to
\(w_-=-5.372184<w_0\) and denotes the resulting lower operator by
\(\widetilde T_\ell\). This is a lower estimate, not a change in the
physical or arithmetic local normalization.

Let \(P_\ell\) select cosines \(0,\ldots,31\), including the constant,
in the ordinary interval norm. Reflection only changes their signs. These
heads impose no artificial zero endpoint values. In this split the exact
lower operator has blocks \(A_{\rm ex},B_{\rm ex},C_{\rm ex}\). An exact
rational matrix \(A_\ell\preceq A_{\rm ex}\), with all entry errors
removed, satisfies the following certified inequalities:

| Quantity | Old window \(\ell=L\) | New window \(\ell=h\) |
|---|---:|---:|
| \(A_\ell\) lower floor | \(4/125=.032\) | \(31/20=1.55\) |
| \(C_{\rm ex}\) lower floor \(c_\ell^0\) | \(161/50=3.22\) | \(369/100=3.69\) |
| \(\|A_\ell^{-1/2}B_{\rm ex}\|^2\le r_\ell^2\) | \(11/1000\) | \(13/10^6\) |

The last row includes every column of the infinite complement. It is not
a norm of a truncated cross matrix alone. Choose
\(\eta_L=1/40\), \(\eta_h=1/200\). Cauchy--Schwarz and Young's
inequality applied to the actual metric cross block give
\[
 \widetilde T_\ell\succeq
 \mathcal M_\ell:=(1-\eta_\ell)A_\ell\oplus d_\ell I,
 \qquad d_\ell=c_\ell^0-r_\ell^2/\eta_\ell.
 \tag{3.2}
\]
Thus
\[
 d_L=2.78,\qquad d_h=3.6874,\qquad
 \mathcal M_L,\mathcal M_h\succeq mI,\quad m=3/100.
 \tag{3.3}
\]
The cross blocks have been paid for explicitly; they have not been discarded.
The two diagonal blocks in \(\mathcal M\) make this split energy-orthogonal.

This treats the logarithmically concentrated join directions in the
**entire complement**. The head is not claimed to approximate them.
Their mixed response is bounded by the scale-invariant corner norm in
Section 4, while the complement metrics in (3.3) retain sufficient energy.

### Why the previous compactness obstruction does not apply

The forward and backward maps
\[
 \mathcal I f(s)=\sqrt{2\alpha}\,\mathcal M_L^{1/2}V_{s,L}f,
\qquad
 \mathcal O v(s)=\sqrt{2\alpha}\,\mathcal M_h^{1/2}U_h(w,s)^*v,
\quad \alpha=1-\frac{w^2}{8m},
 \tag{3.4}
\]
satisfy \(\mathcal I^*\mathcal I\preceq E\) and
\(\mathcal O^*\mathcal O\preceq F\). Their integrated lower forms
can be compact; neither is inverted. Instead
\(\mathcal I E^{-1/2}\) and \(\mathcal O F^{-1/2}\) are contractions
into the energy spaces. The bounded normalized mixed generator acts between
those spaces. This factorization uses the exact coercive \(E,F\), and
provides usable directional lower energy without pretending that a finite
tower integral alone has a uniform inverse.

The head/complement decomposition also splits these shift-integrated energy
spaces into four mixed blocks. Controlling all four pointwise in shift,
uniformly, controls their multiplication operator and hence the full
cumulative coupling. No finite restriction of the initial inputs is made.

## 4. Four mixed operator blocks, including the logarithmic corner

Set \(H=H_0\). In reflected coordinates its kernel is
\[
 H(t,r)=\sum_{n=1}^\infty e^{-a_n(t+r)}-e^{(t+r)/2}.
 \tag{4.1}
\]
Here the old input is identified with its reflection in \(r\). The local
forms \(Q_{s,L}\) and \(\widetilde T_L\) commute with this reflection,
so their relative coupling norms are unchanged. The independent coefficient
check explicitly restores the cosine signs \((-1)^j\).
The certified finite and one-sided estimates, before the factors
\(1-\eta_\ell\), are
\[
 \|A_h^{-1/2}P_hHP_LA_L^{-1/2}\|<\frac{171}{200}=.855,
 \tag{4.2}
\]
\[
 \|P_h^\perp HP_LA_L^{-1/2}\|^2\le\frac{23}{1000},
 \qquad
 \|P_L^\perp H^*P_hA_h^{-1/2}\|^2\le\frac{19}{100}.
 \tag{4.3}
\]
Both estimates in (4.3) include all uncomputed output rows beyond 2047.

For the complement/complement block, the positive gamma kernel obeys
\[
 \frac{e^{-5u/2}}{1-e^{-2u}}\le\frac1{2u},\quad u>0.
\]
Weighted Schur with weight \(r^{-1/2}\), or its unitary logarithmic
coordinate transform, gives the rectangular Carleman operator bound
\(\|1/[2(t+r)]\|\le\pi/2\). In logarithmic coordinates the corresponding
convolution profile is \(1/[4\cosh((x-y)/2)]\), whose integral is
\(\pi/2\). This controls arbitrarily small join scales without summing
their HS mass. Orthogonal projections do not enlarge the norm.

The growing pole is rank one. Let
\[
 \mathfrak f_\ell(N)=\frac2\ell\left(\frac\ell\pi\right)^4
                        \frac1{3(N-1)^3}.
\]
Its omitted cosine coefficient norms give
\[
 \|P_h^\perp HP_L^\perp\|
 \le\frac\pi2+\prod_{\ell=L,h}
       \left[\frac{1+e^{\ell/2}}2\sqrt{\mathfrak f_\ell(32)}\right]
 =:\,c_{\rm corner}.
 \tag{4.4}
\]
The pole has not been set to zero; its contribution is enclosed in the
certificate.

Combining (3.2) and (4.2)--(4.4), the four operator blocks of
\(\mathcal M_h^{-1/2}H\mathcal M_L^{-1/2}\) have upper bounds
\[
 \begin{pmatrix}
 \dfrac{.855}{\sqrt{(1-\eta_L)(1-\eta_h)}}&
 \sqrt{\dfrac{.19}{(1-\eta_h)d_L}}\\[6pt]
 \sqrt{\dfrac{.023}{(1-\eta_L)d_h}}&
 \dfrac{c_{\rm corner}}{\sqrt{d_Ld_h}}
 \end{pmatrix}
 \preceq_{\rm entrywise}
 \begin{pmatrix}.87&.265\\.081&.493\end{pmatrix}.
 \tag{4.5}
\]
Their explanatory decimal values are respectively
\(.868065041,.262085421,.079983699,.490611082\).
For any old and new inputs the two-by-two block norm comparison is valid;
entrywise order here is used only for a nonnegative scalar comparison
matrix, not mistaken for operator order of an arithmetic form.

The exact test \((19/20)^2I-B^*B\succ0\) for the rational matrix on
the right of (4.5) has positive diagonal entries and determinant
\[
 \frac{350573621}{40000000000}>0.
 \tag{4.6}
\]
Hence
\[
 |\langle v,Hf\rangle|
 <.95\sqrt{\mathcal M_L[f]\mathcal M_h[v]}.
 \tag{4.7}
\]
The corner block is now below .493 in its directional metrics. Increasing
matrix resolution alone did not establish this: the norm estimate (4.4)
and both analytic one-sided tails are indispensable.

## 5. Uniform shift correction and the cumulative conclusion

The inherited complete-generator estimate gives, on each local window,
\[
 \|G_{s,\ell}-G_{0,\ell}\|\le s^2/8,
 \qquad Q_{s,\ell}\succeq\mathcal M_\ell-s^2I/8
                  \succeq\alpha\mathcal M_\ell,
 \quad \alpha=1-w^2/(8m)>0.
 \tag{5.1}
\]
For the mixed block, \(H_s(t,r)=H(t,r)\cosh(s(t+r))\). Its signed
perturbation is bounded by the positive majorant:
\[
 \|H_s-H\|\le\Delta:=
 \frac{w^2R^2}{2}\cosh(wR)
 \left[\frac\pi2+\sqrt{(e^L-1)(e^h-1)}\right],\qquad R=L+h.
 \tag{5.2}
\]
The square root is exactly the norm of the unprojected growing-pole kernel.
An outward enclosure gives
\(\Delta<2.6516720750\,10^{-7}\). Since \(\mathcal M_\ell\succeq mI\),
\[
 |\langle v,H_s f\rangle|
 \le\frac{.95+\Delta/m}{1-w^2/(8m)}
                   \sqrt{Q_{s,L}[f]Q_{s,h}[v]},
\]
\[
 \frac{.95+\Delta/m}{1-w^2/(8m)}
 <.950012797294<\frac{951}{1000}.
 \tag{5.3}
\]
Apply the exact energy-transfer lemma to obtain (1.1). Every shift between
zero and \(w\) is included. As a useful consequence, the Schur complement
of the full append defect satisfies
\[
 E-Y^*F^{-1}Y\succeq(1-.951^2)E
                   \succeq(1-.951^2)\delta I>0.
 \tag{5.4}
\]
This is a cumulative spatial-coupling statement with a quantitative margin.

## 6. Infinite-complement bounds and how the finite arithmetic is enclosed

### 6.1 Diagonal metrics

For \(k_j=j\pi/\ell\), \(\rho_0=\ell^{-1/2}\),
\(\rho_j=\sqrt{2/\ell}\), the exact finite-tower cosine representation is
\[
 \widetilde T_{ij}=d_i\delta_{ij}+R_{ij}+2c_ic_j-2s_is_j,
\quad d_j=w_-+\sum_{n=0}^{M-1}\frac2{a_n}\frac{k_j^2}{a_n^2+k_j^2},
\]
\[
 R_{ij}=2\rho_i\rho_j\sum_{n=0}^{M-1}
 \frac{a_n^2(1-(-1)^i e^{-a_n\ell})}
      {(a_n^2+k_i^2)(a_n^2+k_j^2)}
 \quad(i\equiv j\pmod2),
 \tag{6.1}
\]
and \(R_{ij}=0\) for opposite parity. The pole coefficients are
\(c_j=\sinh(\ell/4)\rho_j/(1/4+k_j^2)\) on even modes and zero on odd;
\(s_j=-\cosh(\ell/4)\rho_j/(1/4+k_j^2)\) on odd modes and zero on even.
These are the inherited Robin-to-Neumann identities, now evaluated at
\(M=128,N=32\).

Positivity of \(R\), the even pole form, and monotonicity of \(d_j\) give
\[
 C_{\rm ex}\succeq
 [d_N-2\cosh^2(\ell/4)\mathfrak f_\ell(N)]I.
 \tag{6.2}
\]
For \(i<N,j\ge J\), the cross entries obey
\[
 |B_{ij}|\le E_i\rho_j/k_j^2,
\quad E_i=2\rho_i\sum_{n<M}
       \frac{a_n^2(1+e^{-a_n\ell})}{a_n^2+k_i^2}
       +2(|c_i|\sinh(\ell/4)+|s_i|\cosh(\ell/4)).
 \tag{6.3}
\]
Therefore the entire omitted column Gram is at most
\(\mathfrak f_\ell(J)\sum_{i<N}E_i^2\,I\). With \(J=2048\),
the squared physical remainder bounds are below \(3.030\,10^{-7}\)
on the old side and \(3.837\,10^{-10}\) on the new side. Finite columns
\(N,\ldots,J-1\) are retained, and the certificate proves
\(B_{\rm ex}B_{\rm ex}^*\preceq r_\ell^2A_\ell\) by an outward LDL
test including that remainder. This proves the metric table in Section 3.

### 6.2 Both one-sided mixed tails

For an exponential rate \(a\), write
\[
 I_j^\ell(a)=\rho_j\frac{a(1-(-1)^je^{-a\ell})}{a^2+k_j^2}.
\]
The exact mixed coefficient in reflected coordinates is
\[
 H_{ij}=\sum_{n=1}^\infty I_i^h(a_n)I_j^L(a_n)
                       -I_i^h(-1/2)I_j^L(-1/2).
 \tag{6.4}
\]
For an output length \(b\), input length \(a\), output mode \(j\ge J\)
and input mode \(i<N\), the positive decreasing-series integral estimate
\(\sum_{n\ge1}(a_n^2+k_j^2)^{-1}\le\pi/(4k_j)\) gives
\[
 |H_{ji}|\le\rho_j^b\rho_i^a
                 \left(\frac\pi{4k_j}+\frac{C_{b,a}}{k_j^2}\right),
\]
\[
 C_{b,a}=\sum_{d=b,a,a+b}\frac{e^{-5d/2}}{1-e^{-2d}}
            +\frac{1+e^{b/2}}2\,2(e^{a/2}-1).
 \tag{6.5}
\]
The three exponential sums bound the endpoint factors in (6.4); the last
term retains the signed pole in absolute value. Set
\(u=b/4\), \(v=C_{b,a}(b/\pi)^2\). All remaining rows have squared
HS norm at most
\[
 R_{b,a}=\frac2b\frac{2N-1}{a}
 \left[\frac{u^2}{J-1}+\frac{uv}{(J-1)^2}
                      +\frac{v^2}{3(J-1)^3}\right].
 \tag{6.6}
\]
Using HS here is legitimate and small enough because the **input head is
finite**. It is not the infinite corner/corner HS estimate excluded in the
previous session. The physical squared tail bounds are below .000384751
for old head to new complement and .038509654 for new head to old
complement. Finite rows \(N,\ldots,J-1\) plus these tails are tested
against respectively \((23/1000)A_L\) and \((19/100)A_h\), proving
both inequalities (4.3).

### 6.3 Exact infinite series, roundoff and sign decisions

Separate the non-exponential part of (6.4):
\[
 S(x,y)=\sum_{n\ge1}\frac{a_n^2}{(a_n^2+x)(a_n^2+y)}
       =\frac{P(y)-P(x)}{y-x},
\quad P(k^2)=\frac k2\Im\psi(5/4+ik/2).
 \tag{6.7}
\]
For coincident arguments use
\[
 P'(k^2)=\frac{\Im\psi(5/4+ik/2)}{4k}
                   +\frac{\Re\psi'(5/4+ik/2)}8,
\quad P'(0)=\psi'(5/4)/4.
 \tag{6.8}
\]
The ordinary digamma partial-fraction expansion proves these identities.
The certificate shifts its argument 32 times by the exact recurrence and
uses eight Euler--Maclaurin terms at real part \(33.25\). The expansion
agrees with [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2). The periodic
Bernoulli remainder, using \(|B_{16}(\{t\})|\le|B_{16}|<8\), bounds
the digamma error by \(8/(16\,33^{16})\) and its derivative error by
\(8/33^{17}\). These bounds follow directly by integrating
\(|z+t|^{-17}\) and its derivative, with \(\Re z>33\).
The imaginary logarithm is enclosed with a half-angle arctangent series
and its alternating remainder. There is no floating special-function call.

The three exponentially decaying corrections in (6.4) retain 256 rates.
The omitted terms are bounded by
\[
 13\,\frac{3e^{-a_{257}h}}{a_{257}^2(1-e^{-2h})}<10^{-13}.
 \tag{6.9}
\]
Here 13 exceeds the product of the two basis normalization maxima.
Rate features are rounded to integer multiples of \(10^{-20}\), with
certified error at most \(10^{-20}\) per feature. The metric features
have magnitude below 27; their rank-sum error is bounded by
\(M(54\,10^{-20}+10^{-40})\). Mixed old and new features have magnitude
below 1 and 3, respectively; a bound \(256\cdot40\,10^{-20}\)
covers their triple-product errors. These errors and (6.9) are included
before matrix entries are rounded to denominator \(10^{12}\).

Every final entry has a proved absolute error at most
\(e=10^{-12}\). Subtracting \(NeI\) from a symmetric rounded head
makes it a lower matrix \(A_\ell\). For a rectangular block with at
most \(32\cdot2016\) entries, the operator error is at most \(256e\).
Its rounded Gram is computed by **exact integer dot products**, and the
Gram error is bounded by
\(2\|W_{\rm rounded}\|_{\rm HS}(256e)+(256e)^2\).
Finite sign decisions use outward rational LDL recursions on the resulting
32- or 64-dimensional matrices. Positive pivots certify positive
definiteness; they are not reported as eigenvalue lower bounds.

As a separate exact control of (6.7)--(6.8), ten coefficients, including
coincident frequencies and strongly unequal frequencies, are enclosed by
4096 positive series terms and monotone integral tail bounds. The much
narrower Euler--Maclaurin enclosures lie inside those independent intervals.

## 7. Full arithmetic memory and relation to the preceding obstruction

The original finite-shift response is still
\[
 k_w=q_w-4wb(e^{-b\cdot}*q_w)-4wa(e^{a\cdot}*q_w),
\quad a=1/2-w,\quad b=1/2+w,
\]
\[
 q_w(u)=\frac{2\pi^w}{\Gamma(w)}e^{-au}(1-e^{-2u})^{w-1}.
 \tag{7.1}
\]
For \(u=q_w*f\), both pole states obey
\[
 p_\lambda(L+t)=e^{\lambda t}p_\lambda(L)
       +\int_0^t e^{\lambda(t-v)}u(L+v)dv,
 \qquad \lambda=-b,a.
 \tag{7.2}
\]
The beta history in \(u(L+t)\) is the full old-input convolution.
Equation (2.4) is a second representation of this same mixed transfer;
neither history nor either signed state is reset at the join.

Real causal convolution gives \(Z^*=J_hZJ_h\), so the defect in (2.5)
also satisfies \(F=J_h(I-Z^*Z)J_h\), as required. The fixed local
constant, ordinary input/output norms and identity initial normalization
are unchanged. No output smoother, path average, or auxiliary loss appears.

The [preceding HS obstruction](CUMULATIVE_ENERGY_HS_OBSTRUCTION_20260920.md)
remains valid for its specified finite-tower-plus-floor proxy and HS
complement estimate. This calculation does not turn its large HS norm
into a small one. It instead factors the actual cumulative coupling through
energy histories and bounds the generator corner in operator norm. Its
finite matrices retain endpoints and metric cross effects; the infinite
corner and both omitted one-sided spaces are estimated analytically.

## 8. Reproduction, evidence and what this changes

From the repository root:

```sh
python3 -B papers/susy-positivity/investigations/critical-path/numerics/certify_cumulative_operator_coupling.py --output /tmp/cumulative-operator-replay.json
python3 -B papers/susy-positivity/investigations/critical-path/numerics/certify_cumulative_operator_coupling.py --digits 60 --output /tmp/cumulative-operator-replay-60.json
python3 -B papers/susy-positivity/investigations/critical-path/numerics/check_cumulative_operator_reduction.py --certificate /tmp/cumulative-operator-replay.json --output /tmp/cumulative-operator-reduction-replay.json
```

The certificate is standard-library-only. Both precisions passed, with
identical rational comparison constants. The separate NumPy checker uses
the earlier physical-delay quadrature, independently of the new
digamma/series matrix construction. Its first 8-by-8 mixed coefficients
agree within \(5.016\,10^{-13}\) at both tested quadrature orders. This
is a floating consistency check, not an interval error bound or the proof
of positivity. Neither the .802 finite cumulative diagnostic nor a
central form on the enlarged interval was used as a certificate.

Saved small records contain the scalar bounds, LDL checks, source hashes
and a small coefficient control. No large generated matrices are stored.
The [handoff](RESEARCH_CONTINUATION_AFTER_OPERATOR_COUPLING_20260920.md)
and provenance record identify the new files and preserved state. All
337 pre-existing files checked in the two investigation directories,
including current manuscript v0.5, snapshots and existing uncommitted
research, remain unchanged. No manuscript claim was silently promoted.

The analytic reduction, evolution-domain argument, and implementation still
require specialist review. The result is stronger than a favorable finite
quotient: it supplies an all-input, energy-weighted bound on the requested
cumulative join. It shows how local directional energy can pay for the
logarithmically concentrated coupling without requiring a small absolute
gamma tail. What remains for the broader program is a continuation invariant
that survives larger windows and eventually the prime delays, and a method
for regimes where these instantaneous local positive metrics cease to be
available. This one successful append does not establish either.

The Gaussian physical exclusion is unchanged. Further physical work needs
a new independently specified action or observable; this arithmetic proof
provides no new localization interpretation.
