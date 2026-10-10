# Centered relative block and an adverse genuine coherent current

10 October 2026. Prepared with substantial LLM assistance. Model: GPT-6
(Codex); the exact serving variant and configured reasoning effort are not
available and are not inferred. The derivations and interval replay are
internal checks, not independent mathematical review.

This continues [Note 1](1_HUSIMI_READOUT_DRIFT_AND_COHERENT_INTERFERENCE_20261010.md)
with a genuine macroscopic block \(N/2<n\le N\). The result is an exact
centered logarithmic-moment transformation, full coherent recombination,
and an outward interval showing that this actual block's phase current can
be negative in the shrinking sector. This is a different obstruction from
discarding off-diagonal packet energy: the tested quantity explicitly retains
the coherent interference and physical amplitude drift.

The certified example is \(N=M=22066\), \(\kappa=1\),
\(t=(2\log M)^{-1}<1/20\), \(x=4\pi M^2\). Its normalized block current
is enclosed by
\[
 -181.169106<\frac{\mathcal J_B}{w_M^2}<-181.169105<0.
\tag{1}
\]
The block has 11033 genuine terms. It is not a complete-sum sign result or
a heat collision. No independently chosen phase or multiplicative twist is
used in (1).

## 1. Genuine finite state and a centered transformation

Use the full paid arithmetic approximant of [Heat Note 13](../../notes/13_RECENT_HEAT_RESULTS_AND_PATHS_FORWARD_20261009.md).
At one center put
\[
 q_n=w_ne^{i\phi_n},\quad
 w_n=\exp\left(\frac t4\log^2n-
              (\tfrac12+\tfrac t2\alpha_r)\log n\right),
 \quad \phi_n=\theta+T\log n,
 \quad T=\frac{x-t\alpha_i}{2}.
\]
The underlying genuine heat state, domain and scalar sign remain those of
Note 1: \(\psi_t=e^{tu^2/2}\sqrt{\Phi_e}\), its Wigner readout, and
\(\partial_tH=-H_{xx}\). This note transforms a block of its fixed-cutoff
arithmetic approximation; it does not assign that block an autonomous
Newman heat generator.

The cutoff \(N\), time \(t\), and central derivative scale \(L\) are fixed
throughout spatial differentiation. The physical coefficients still vary
with \(x\). Define
\[
 \ell_N=\log N,\quad \delta_n=\log(N/n),\quad
 a_N=\tfrac12+\tfrac t2\alpha_r-\tfrac t2\ell_N,
\]
\[
 Z_k=\sum_{N/2<n\le N}
    \delta_n^k\exp(a_N\delta_n+t\delta_n^2/4-iT\delta_n),
 \qquad k=0,1,\ldots.
\tag{2}
\]
Every \(\delta_n\) lies in \([0,\log2)\). Completing the logarithmic
square gives the exact centered block identity
\[
 S_B:=\sum_{N/2<n\le N}q_n=q_NZ_0.
\tag{3}
\]
There is no asymptotic remainder in (2)–(3), and the common physical height
is retained. The factor \(e^{t\delta^2/4}\) must remain: dropping it is an
additional approximation to the actual weights.

Write \(\alpha'=U+iV\),
\[
 c=\tfrac12(1+tU/2),\quad
 \Omega=\tfrac12\Re\{\alpha(1+t\alpha'/2)\},
 \quad \lambda_N=\Omega-c\ell_N.
\]
The exact physical derivatives are
\[
 T'=c,\quad a_N'=tV/4=:a',\quad
 \frac{q_N'}{q_N}=\gamma_N=-a'\ell_N-i\lambda_N,
 \quad g=a'-ic,
\]
\[
 S_B'=q_N(\gamma_NZ_0+gZ_1).
\tag{4}
\]
Thus replacing the physical derivative by \(-icZ_1\) loses both carrier
motion and amplitude drift. At frozen \(a_N,t,N\),
\(Z_1=i\partial_TZ_0\) is an auxiliary moment identity. It is not a
license to freeze those physical coefficients while differentiating \(x\).

Equivalently, with \(z_N=r_N-ic_N\),
\(r_N=4\lambda_N/L\), \(c_N=tV\ell_N/L\), and
\(d=4c/L+itV/L\), the block collision coordinates are
\[
 W_B=\sum_Bq_nz_n=q_N(z_NZ_0+dZ_1),\qquad
 \mathcal B=(\Re S_B,\Im W_B)
           =(\Re S_B,4\Re S_B'/L).
\tag{5}
\]
These are the genuine signed value and derivative contribution of the same
block; no inconsistent value/derivative cutoffs are introduced.

## 2. Both coherent phase types survive recombination

The exact block energy is
\[
 |\mathcal B|^2=
 \tfrac12\{|S_B|^2+|W_B|^2+\Re(S_B^2-W_B^2)\}.
\tag{6}
\]
The modulus terms in (6) contain every phase difference. The squared terms
contain the reflected phase sums, including \(2\phi_N\); the latter are
not determined by the difference phases alone.

Let \(C=\{1,\ldots,N\}\setminus B\), and define \(S_C,W_C\) by the
same genuine coefficients. The complete vector has exactly
\[
 |\mathcal V_N|^2=|\mathcal B|^2+|\mathcal C|^2
 +\Re\{S_B\overline{S_C}+S_BS_C+
           W_B\overline{W_C}-W_BW_C\}.
\tag{7}
\]
The final line is the entire block/complement interference. It can have
either sign. Neither the transformed block energy nor a current sign may
be inserted into the complete collision criterion without this line.

For higher jets put \(\Gamma(\delta)=\gamma_N+g\delta\) and use the
physical fixed-time derivatives of its coefficients. The first four
logarithmic derivative polynomials are
\[
 P_0=1,\quad P_1=\Gamma,\quad P_2=\Gamma^2+\Gamma',
 \quad P_3=\Gamma^3+3\Gamma\Gamma'+\Gamma'',
\]
\[
 P_4=\Gamma^4+6\Gamma^2\Gamma'+3(\Gamma')^2
                    +4\Gamma\Gamma''+\Gamma'''.
\tag{8}
\]
Each \(P_j\) is a polynomial in \(\delta\) of degree at most \(j\).
Writing its coefficients \(p_{jk}(t,x)\) gives
\[
 S_B^{(j)}=q_N\sum_{k=0}^jp_{jk}Z_k,
 \qquad f_j=F_{t,N}^{(j)}=2\Re(S_B^{(j)}+S_C^{(j)}).
\tag{9}
\]
This supplies the full fourth-jet dictionary. In particular every derivative
of \(U,V,c,\Omega\), and the normalizer implicit in \(q_n\), is retained
in (8). The centered identity for the complex sum and its derivatives extends
analytically at fixed cutoff. On the complex neighborhood used to pay Cauchy
errors, one uses the analytic extensions
\(\alpha_r=(\alpha(s)+\alpha(1-s))/2\),
\(\alpha_i=(\alpha(s)-\alpha(1-s))/(2i)\), and
\(q_n=e^{i\theta}p_{t,n}(s)\). The holomorphic approximant there is
\(F(z)=S(z)+S^\#(z)\), with
\(S^\#(z)=\sum e^{-i\theta(z)}p_{t,n}(1-s(z))\). The real-part formula
in (9) applies on the real axis; it is not applied off-axis in the Cauchy
payment. No varying coordinate is conjugated inside a holomorphic summand.

## 3. A candidate-conditioned coherent current test

Define the phase current, without dividing by a possibly vanishing amplitude,
\[
 \mathcal J_B=-\Im(S_B'\overline{S_B}).
\]
Using (4) yields the interference-sensitive identity
\[
 \frac{\mathcal J_B}{w_N^2}
 =\lambda_N|Z_0|^2+c\Re(Z_1\overline{Z_0})
                         -a'\Im(Z_1\overline{Z_0}).
\tag{10}
\]
The common carrier phase cancels in this particular current. Therefore
(10) uses coherent difference phases, while the phase-sum information for
the actual real pair is still carried by (5)–(7). This distinction matters:
a current bound is a necessary-condition route, not a replacement of the
joint observation by a complex modulus.

For \(S=S_B+S_C\), its complete current is
\[
 \mathcal J=-\Im(S'\overline S)
 =\mathcal J_B+\mathcal J_C
 -\Im(S_B'\overline{S_C}+S_C'\overline{S_B}).
\tag{11}
\]
Writing \(S=u+iv\), \(S'=u'+iv'\) gives
\(\mathcal J=u'v-uv'\). At an actual collision, the fully paid
approximation from Note 13 implies
\[
 |u|\le\eta_N/2,\qquad |u'|\le L\eta_N/2,
\]
and hence the exact candidate-conditioned necessary inequality
\[
 |\mathcal J|
 \le\frac{\eta_N}{2}
       \{L|\Im S|+|\Im S'|\}.
\tag{12}
\]
There is no division by \(S\) and no exception at a complex zero of the
coherent sum. A strict reverse of (12), established for actual candidate
states, would exclude them. This is a concrete signed checkpoint involving
the complement term in (11), rather than only a positive bulk norm.

Positive individual weights and mostly positive \(\lambda_n\) do not
make (10) positive. For example,
\[
 \Re(Z_1\overline{Z_0})=
 \sum_{n\in B}A_n^2\delta_n+
 \sum_{n<m\in B}A_nA_m(\delta_n+\delta_m)
                  \cos(T(\delta_n-\delta_m)),
\tag{13}
\]
where \(A_n=e^{a_N\delta_n+t\delta_n^2/4}>0\). The second sum retains
all adverse interference. Formula (1) demonstrates its adverse sign for a
genuine macroscopic block, with the drift term in (10) included.

## 4. A certified actual-block example

The standard-library checker
[check_block_current.py](../numerics/check_block_current.py) uses outward
60-digit Decimal intervals. Its parameters are exactly
\[
 M=N=22066,\quad \kappa=1,\quad t=(2\log M)^{-1},\quad x=4\pi M^2.
\]
The natural cutoff is indeed \(M\), since
\(M<\sqrt{M^2+t/16}<M+1\). Thus all 11033 terms in (2) are actual
relative-block terms in the sector of Note 13.

The elementary real-axis data are
\[
 \alpha_r=\tfrac L2+\tfrac14\log(1+x^{-2})-(1+x^2)^{-1},
 \quad \alpha_i=\frac{3x}{1+x^2}-\tfrac12\arctan x,
\]
\[
 U=\frac{7x^2-5}{(1+x^2)^2},\qquad
 V=\frac{x(x^2+5)}{(1+x^2)^2}.
\tag{14}
\]
Pi is enclosed by the alternating Machin arctangent series, with its
explicit first-omitted-term bound. The identity is verified from
\(\tan(4\arctan(1/5)-\arctan(1/239))=1\), with the angle in
\((0,\pi/2)\). Large arctangent is evaluated as
\(\arctan x=\pi/2-\arctan(1/x)\). Reduced sine/cosine use Taylor
polynomials on \(|s|\le4\), with the explicit Lagrange remainders.
Every elementary arithmetic operation is rounded outward. Monotone
\(\log\) and \(\exp\) use adjacent values around Decimal's correctly
rounded outputs, as documented in the
[Python Decimal specification](https://docs.python.org/3/library/decimal.html).
No ordinary binary float enters this enclosure.

The carrier phase is reduced analytically to avoid subtracting two huge
terms. At this integer height,
\[
 \phi_M\equiv\pi(M\bmod2)-\pi+\tfrac14\arctan x
 -\tfrac x8\log(1+x^{-2})+
       \tfrac t2\alpha_i(\alpha_r-\log M)\pmod{2\pi}.
\tag{15}
\]
This is the exact principal-branch phase from the manuscript. It supplies
the actual signed readout (5), rather than an independently selectable
carrier.

The small [certificate](../numerics/BLOCK_CURRENT_CERTIFICATE_20261010.json)
also encloses
\[
 -0.000673643<\mathcal J_B<-0.000673642,
\]
\[
 0.01035355<\mathcal B_1<0.01035356,\qquad
 0.001391829<\mathcal B_2<0.001391830,
\]
\[
 0.00010913326<|\mathcal B|^2<0.00010913327.
\tag{16}
\]
Consequently this is neither a vanishing block nor a candidate collision.
The current computed from (10) overlaps the separately reconstructed
\(-\Im(S_B'\overline{S_B})\) enclosure. The negative upper endpoint
in (1) is decided by interval arithmetic, not by agreement of hashes.
The build record hashes identify the exact small source and certificate.

## 5. Remainder discipline and the next signed checkpoint

The exact transformation (2)–(11) adds no model error. Recombining the
complement restores precisely the same \(F_{t,N}\), so the complete
genuine jet payment remains
\[
 |Q_t^{(j)}-f_j|\le j!L^j\eta_N,\qquad
 \eta_N\le5e^{-\mathfrak b/t},\quad 0\le j\le4.
\tag{17}
\]
The threshold test is still
\(2f_3^2-3f_2f_4-\gamma f_2^2< -\Delta\), with the full measured
quadratic payment \(\Delta\) of Note 13. Formula (9) is an exact way
to assemble it; a negative block current is not that fourth-jet inequality.
The normalizer and its drift are already included in the coefficients and
must not be removed during this assembly. Higher-multiplicity obligations
from the threshold hierarchy also remain.

For a proposed further compression, there is an explicit payment. Replacing
\(e^{t\delta^2/4}\) by its degree-\(K\) Taylor polynomial gives, with
\(\tau=t(\log2)^2/4\), \(m=\#B\),
\[
 |S_B-\widetilde S_B|
 \le w_Nm\,e^{\max(a_N,0)\log2+\tau}
                         \frac{\tau^{K+1}}{(K+1)!}.
\tag{18}
\]
The error for \(W_B\) is bounded by (18) times
\(|z_N|+|d|\log2\). The \(j\)-th jet payment multiplies (18) by
\(\sup_{0\le\delta\le\log2}|P_j(\delta)|\), because time and
\(\delta_n\) are fixed while differentiating; it includes all coefficient
derivatives in (8). Such compression can be paid at a fixed rectangle by
choosing \(K\), but this absolute bound with fixed \(K\) does not furnish
a uniform shrinking-time payment on arbitrarily large \(N\): its relative
factor \(N t^{K+1}\) diverges in the present sector. This diagnoses the
stated compression bound, not the size of the actual signed Taylor error.
The certificate retains the
full exponential and has no error of type (18).

The next bounded task is therefore the complete candidate-conditioned
combination (11): obtain a signed estimate on
\[
 \mathcal J_C-\Im(S_B'\overline{S_C}+S_C'\overline{S_B})
\]
strong enough, together with the actual \(\mathcal J_B\), to violate
(12), or insert the moment dictionary (9) into the paid fourth-jet test.
Any proposed argument assigning a nonnegative phase current to every
genuine relative block is stopped by (1). The result leaves open a
candidate-conditioned relation for the complete state; it does not prove
an actual collision, a new Newman bound, or RH.
