# Higher Schur payments and a finite family of cutoff rectangles

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
GPT-6.1-sol (Codex), reasoning effort ultra, inherited from the verified
configuration of chat 6. All derivations, exact checks and agent audits
are internal LLM work, not independent mathematical validation.

This continues [Heat Note 18](18_CORRELATED_HOLOMORPHIC_PAYMENTS_AND_CANDIDATE_COVERAGE_20261010.md).
The real holomorphic remainder now has an explicit feasible jet body
through the fourth derivative. Its sharp conditional threshold maximum
reduces to an optimization over one real parameter. A finite-jet control
shows that retaining the correlations can change a failed independent-error
test into a strict exclusion. Another ordinary-double control shows why
the error correlations alone cannot furnish the missing arithmetic sign.
Companion projects sharpen the one-sided dual payment and certify three
additional disconnected rectangles at distinct genuine cutoff values.

## 1. Use the physical finite jets and one bounded remainder

At a center in the shrinking sector keep time, integer cutoff and the
derivative coordinate scale fixed. Set
\[
E=Q_t-F_{t,N},\quad f_j=F_{t,N}^{(j)}(x),\quad
q_j=Q_t^{(j)}(x),\quad
g(\zeta)=E(x+\zeta/L)/\eta,
\quad \alpha_j=\frac{E^{(j)}(x)}{j!L^j\eta}.
\tag{1}
\]
Here \(\eta>0\) is the full holomorphic disk bound of
[Heat Note 8](8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md),
including analytic reflection, normalizer conversion and cutoff changes.
Thus \(g\) is a real-symmetric holomorphic disk map bounded by one, and
\[
q_j=f_j+j!L^j\eta\alpha_j.
\tag{2}
\]
The \(f_j\) are the physical raw derivatives of the complete approximant.
Leading pure-phase or centered-moment jets have their separate physical
Bell residuals. Those residuals cannot be absorbed into the Schur body
unless their combined difference has its own proved full-disk bound.
The exact normalizer term remains
\(\gamma=18\partial_x^2\log A_t+9/x^2\).

At an all-real-time multiple zero with \(x\ne0\), the imported
[threshold deflation inequality](12_THRESHOLD_COLLISION_JETS_AND_PAID_LAGUERRE_TEST_20261009.md)
is
\[
\mathscr L(q)=2q_3^2-3q_2q_4-\gamma q_2^2\ge0.
\tag{3}
\]
This uses the all-real hypothesis; an arbitrary local analytic candidate
does not obey (3). A strict upper bound below zero for every compatible
remainder jet would exclude such a threshold candidate. The fourth-jet
criterion is still vacuous at some higher multiplicities; the existing
deflated hierarchy remains a separate obligation.

## 2. The complete real Schur body through order four

For real \(|s|<1\), the Schur step and its inverse are
\[
h(\zeta)=\frac{g(\zeta)-s}{\zeta(1-sg(\zeta))},\qquad
g(\zeta)=\frac{s+\zeta h(\zeta)}{1+s\zeta h(\zeta)},\quad s=g(0).
\tag{4}
\]
The Schwarz lemma makes \(h\) another real disk map. Conversely, the
inverse preserves the disk because \(|\zeta h(\zeta)|<1\) and the
real Möbius map preserves it. At \(|s|=1\), take the constant map
\(g\equiv s\) and terminate. This is the classical Schur algorithm;
see [Li and Sugawa, Section 2](https://arxiv.org/html/1902.02000#S2).
The inverse construction here suffices for the finite real-jet statement.

Let \(a,\lambda,\mu,r,s\in[-1,1]\), with
\(D_0=1-a^2\), \(D_1=1-\lambda^2\),
\(D_2=1-\mu^2\), \(D_3=1-r^2\). Define
\[
\begin{split}
b_0={}&\lambda,\\
b_1={}&D_1\mu,\\
b_2={}&D_1(D_2r-\lambda\mu^2),\\
b_3={}&D_1\{D_2(D_3s-\mu r^2)
-2\lambda\mu D_2r+\lambda^2\mu^3\}.
\end{split}
\tag{5}
\]
Then the exact first five coefficients are
\[
\begin{split}
\alpha_0={}&a,\qquad \alpha_1=D_0b_0,\\
\alpha_2={}&D_0(b_1-ab_0^2),\\
\alpha_3={}&D_0(b_2-2ab_0b_1+a^2b_0^3),\\
\alpha_4={}&D_0\{b_3-a(2b_0b_2+b_1^2)
+3a^2b_0^2b_1-a^3b_0^4\}.
\end{split}
\tag{6}
\]
These formulas follow by expanding
\(g=a+D_0(\zeta h-a\zeta^2h^2+a^2\zeta^3h^3-a^3\zeta^4h^4)+O(\zeta^5)\)
and repeating it for the inner maps. Every bounded real holomorphic
jet has such parameters by successive forward Schur steps. Conversely,
start with the constant innermost map \(s\) and apply four inverse
steps to obtain a bounded rational map with (6). Boundary parameters
terminate the map and ignore the later parameters, so (6) is a redundant
but exact parametrization including degenerate faces.

At a genuine candidate \(q_0=q_1=0\), the measured finite lower jets
fix
\[
a=-f_0/\eta,\qquad
\lambda=-\frac{f_1}{L\eta(1-a^2)}\quad(|a|<1).
\tag{7}
\]
If \(|a|>1\) or \(|\lambda|>1\), the candidate is already impossible.
If \(|a|=1\), the first derivative error and all higher ones vanish;
one needs \(f_1=0\), then \(q_j=f_j\) for \(j\ge2\). If
\(|a|<1\) and \(|\lambda|=1\), the remaining errors are fixed:
\[
\alpha_j=D_0(-a)^{j-1}\lambda^j\qquad(j\ge1).
\tag{8}
\]
There is no optimization or singular division on these faces.
For an interior first pair, only \(\mu,r,s\) remain free.

Even before the higher optimization, the second-error absolute bound is
\[
|\alpha_2|\le D_0\{1-(1-|a|)\lambda^2\}.
\tag{9}
\]
It follows from its exact center \(-D_0a\lambda^2\) and radius
\(D_0D_1\). This improves the free Cauchy bound in noncentral cases,
while the full signed body (6) retains more information.

## 3. The sharp conditional threshold test has one free parameter

Hold the actual \(a,\lambda\) from (7) fixed. At a fixed \(\mu\),
equations (2), (5) and (6) have the form
\[
q_2=C_2(\mu),\quad q_3=A_3(\mu)+B_3(\mu)r,
\]
\[
q_4=A_4(\mu)+B_4(\mu)r+C_4(\mu)r^2
+24L^4\eta D_0D_1D_2(1-r^2)s.
\tag{10}
\]
All coefficients are explicitly obtained from the physical \(f_j\) and
(6). For example, the center polynomial in \(q_4\) is obtained by
putting \(s=0\), and its values at \(r=-1,0,1\) determine its three
coefficients exactly.

Maximize (3) over \(s\). Since its coefficient is
\(-72L^4\eta q_2D_0D_1D_2(1-r^2)\), the maximum is attained at
\(s=-\operatorname{sgn}(q_2)\), with any value if that coefficient
vanishes. Put
\[
K=72L^4\eta D_0D_1D_2|q_2|,
\]
\[
\begin{split}
c_0={}&2A_3^2-3q_2A_4-\gamma q_2^2+K,\\
c_1={}&4A_3B_3-3q_2B_4,\\
c_2={}&2B_3^2-3q_2C_4-K.
\end{split}
\tag{11}
\]
The remaining expression is exactly \(c_0+c_1r+c_2r^2\).
Its maximum on \([-1,1]\) is
\[
M(\mu)=\max\left\{c_0-c_1+c_2,\ c_0+c_1+c_2,
\ c_0-\frac{c_1^2}{4c_2}\ \text{if }c_2<0,
\ \left|\frac{c_1}{2c_2}\right|\le1\right\}.
\tag{12}
\]
When the conditional vertex is absent, only the two endpoints are used.
Thus the exact optimal bound based on the local holomorphic jet body is
\[
\boxed{U_{\rm Schur}(f;\gamma,L,\eta)
=\max_{-1\le\mu\le1}M(\mu).}
\tag{13}
\]
Every extremal jet is realized in the local disk-map class; no arithmetic
or heat realization is asserted. The equivalent formulation before
quadratic elimination maximizes the two polynomial choices \(s=\pm1\)
over \((\mu,r)\in[-1,1]^2\), avoiding division near a changing vertex.
Either representation can be bounded by certified rational/interval
subdivision. A grid alone is not a certified maximum.

The useful strict test is \(U_{\rm Schur}<0\). Equivalently, the sharp
one-sided correction to the finite threshold expression is
\(\Delta_+=U_{\rm Schur}-\mathscr L(f)\), and the condition is
\(\mathscr L(f)+\Delta_+<0\). This correction can have either sign:
the prescribed lower error jets need not allow a zero higher-error jet.
One may replace it by \(\max(0,\Delta_+)\) for a conventional
nonnegative payment, at the cost of a weaker bound.

The coefficient arithmetic still requires the actual signed \(f_j\).
This is a reduction of their admissible error optimization, not a bound
for the complete prescribed arithmetic moments. Certified intervals
for the finite jets require maximizing over all compatible inputs as
well; a midpoint substitution would be invalid.

## 4. Correlation can change the sign of a paid certificate

There is an exact local finite-jet control where the improvement matters.
Take \(f_0=f_1=0\) and
\[
f_2=3\eta L^2,\qquad f_3=0,\qquad f_4=25\eta L^4.
\tag{14}
\]
Then \(a=\lambda=0\) and
\[
\alpha_2=\mu,\quad \alpha_3=(1-\mu^2)r,\quad
\alpha_4=(1-\mu^2)\{(1-r^2)s-\mu r^2\}.
\]
In units \(\eta L^2,\eta L^3,\eta L^4\), respectively,
\(q_2=3+2\mu\ge1\), \(q_3=6(1-\mu^2)r\).
The maximizing last parameter is \(s=-1\), giving
\[
q_4=1+24\mu^2+24(1-\mu^2)(1-\mu)r^2.
\]
For \(\gamma=0\), direct substitution yields
\[
\frac{\mathscr L(q)}{\eta^2L^6}
=-3(3+2\mu)(1+24\mu^2)
+72(1-\mu^2)(1-\mu)(-2-\mu)r^2\le-3.
\tag{15}
\]
The last term is nonpositive on the whole parameter square. If
\(|\gamma/L^2|\le1/10\), the additional term changes this upper
bound by at most \(25/10\), so
\[
\boxed{\mathscr L(q)\le-\tfrac12\eta^2L^6<0.}
\tag{16}
\]
This is a proved conditional exclusion for physical finite jets with
the particular values (14), using the general all-real threshold input.
It is not an assertion that the prescribed heat coefficients attain them.

In contrast, independent Cauchy intervals for (14), in the same units,
allow \(q_2\in[1,5]\), \(q_3\in[-6,6]\), \(q_4\in[1,49]\).
Their compatible box corner \((1,6,1)\) gives threshold value \(69\)
when \(\gamma=0\). The earlier triangle payment gives upper bound
\(357\). That box corner is not in the Schur body. Thus the stronger
analytic geometry can supply a strict sign that independent errors lose,
once the finite arithmetic jets themselves have a suitable signed shape.

## 5. Correlation alone permits an ordinary positive candidate

Take all finite jets through order four equal to zero and the bounded
real disk map
\[
g(\zeta)=\zeta^2\frac{1/2-\zeta^2}{1-\zeta^2/2}.
\tag{17}
\]
It is a product of \(\zeta^2\) and a disk automorphism applied to
\(\zeta^2\); its modulus is at most one on the disk. Its Schur
parameters are \((0,0,1/2,0,-1)\), and its coefficients give
\[
q_2=\eta L^2\ne0,\qquad q_3=0,\qquad q_4=-18\eta L^4,
\]
\[
\mathscr L(q)=\eta^2L^4(54L^2-\gamma)>0
\quad\text{if }\gamma<54L^2.
\tag{18}
\]
This candidate is ordinary double and satisfies every correlated error
constraint. It is a local bounded-analytic error control, with no
prescribed finite arithmetic state or global all-real heat flow claim.
It rules out a negative sign inferred from the error body alone.

For the zero-finite-jet case and \(\gamma=0\), the exact range is
\[
-32\sqrt3\,\eta^2L^6\le\mathscr L(q)\le72\eta^2L^6.
\tag{19}
\]
Indeed, after dividing by \(72\eta^2L^6\), the expression is
\((1-\mu^2)\{(1+\mu^2)r^2-2\mu(1-r^2)s\}\).
The maximum is \(1\), attained at \(\mu=0,|r|=1\). The minimum
is \(-2|\mu|(1-\mu^2)\), attained with \(r=0\) and
\(s=\operatorname{sgn}(\mu)\); its minimum occurs at
\(|\mu|=1/\sqrt3\). The independent box upper bound would be
\(216\eta^2L^6\). The improvement is substantial but leaves both
signs available in this enlarged error class.

## 6. Companion dual payment and the finite cutoff family

[Project 09 Note 5](../09_prime_phase_torus/notes/5_SHARP_ONE_SIDED_DUAL_PAYMENTS_ON_CORRELATED_CANDIDATES_20261010.md)
replaces the absolute candidate-null dual payment by the exact one-sided
minimum on the correlated lower-jet body. Its extremizers reduce to
boundary quartic critical points and possible interior stationary points,
with all moment-box corners retained when only moment intervals are known.
The signed pair bound must use the same dual coefficients and still retain
physical Bell residuals, normalizer errors and all four arithmetic channels.
A cheaper payment does not itself establish the signed pair estimate.

[Project 13 Note 5](../13_microlocal_phase_space/notes/5_MULTI_CUTOFF_CORRELATED_CANDIDATE_FAMILY_20261010.md)
certifies the three exact closed rectangles
\[
\mathcal R_M=[(2\log M)^{-1},1/20]
\times[4\pi M^2,4\pi M^2+8],\quad
M\in\{22067,22068,22080\}.
\tag{20}
\]
Every rectangle uses all \(M\) genuine terms, the constant natural
cutoff, its physical spatial/time transport, and the full holomorphic
payment. The certified counts and natural joint-vector bounds are

| Cutoff \(M\) | Closed strips | Simple genuine zeros at every time | Lower bound for \(\|(Q_t,Q_t'/L)\|\) |
|---|---:|---:|---:|
| 22067 | 29 | 12 | 0.03117 |
| 22068 | 28 | 12 | 0.02205 |
| 22080 | 32 | 13 | 0.0032919 |

All three rectangles exclude joint heat collisions. The first-jet Schur
test is explicitly checked on strips surviving the value screen, while
the paid derivative test certifies the zero count. In these particular
certificates the derivative margin already implies the Schur test, so
they do not demonstrate extra exclusion from its curvature. Most coarse
candidate-strip current enclosures are inconclusive; they do not imply
negative actual currents. These are three disconnected local windows in
different cutoff cells, with no assertion about the gaps or the remainder
of any full cutoff cell. The counts are exact within each stated rectangle,
not samples or a uniform theorem in \(M\).

## 7. Replay and the next uniform arithmetic target

The [higher Schur checker](../../numerics/check_higher_schur_threshold_payments.py)
checks (6) against independently composed rational series and inverse
parameter recovery, including boundary termination. It checks last-two
parameter maxima and the strict negative and ordinary-double positive
controls. Its [source-bound small record](../../numerics/HIGHER_SCHUR_THRESHOLD_PAYMENT_RECORD_20261010.json)
contains 50157 exact assertions, 3125 full parameter controls and 125
exact last-two-parameter maxima. The notes supply the general analytic
proofs; rational grids validate identities and controls rather than a
uniform arithmetic threshold sign.

The companion project checkers retain their earlier hash-bound sources.
[The shared review](../../reviews/HEAT_HIGHER_SCHUR_AND_MULTI_CUTOFF_CONTINUATION_REVIEW_20261010.md)
and [check record](../../reviews/HEAT_HIGHER_SCHUR_AND_MULTI_CUTOFF_CONTINUATION_CHECK_RECORD_20261010.json)
record source identities, internal derivation audits and fresh replays.

The next arithmetic input can be stated more tightly: certify the
complete physical finite jets at genuine candidates and prove the strict
one-variable bound (13), or prove a prescribed-coefficient signed dual
upper bound using the exact one-sided lower-jet payment. Both must be
uniform on a specified shrinking subsector and beat every physical
residual and normalizer payment. The covariance hierarchy of project 09
still offers a signed target, with its full tail payment retained.
The new finite family provides test cases but no estimate uniform as
\(t\downarrow0\), no full cutoff-cell coverage and no global endpoint
theorem. The manuscript is preserved. All new files follow
[LARGE_FILES.md](../../../../LARGE_FILES.md), and this continuation is
refreshed in the existing chat 6 record, preserving its original number.
