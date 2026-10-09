# A controlled squarepart and a principal-row obstruction to the smooth estimate

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred. Same-model parallel
audits and finite checks are internal validation, not independent
specialist review or formal verification.

Continuing [Note 24](24_ADAPTIVE_COFACTOR_AND_DYADIC_KERNEL_20261009.md)
gives a new selected-sector estimate with all cross terms controlled.
It also shows that a proposed unrestricted, uncentered smooth estimate
for the large-cofactor polynomial is false in a principal-compatible
coefficient class. The selected nonprincipal high-conductor theorem is
not disproved. Its remaining correlation still needs a new estimate.

## 1 Remove a large common factor of the two inverse factors

Keep the literal original weight \(V_u\), profiles, whole slots, masks
and source assumptions of Notes 22–24. Write \(q_v=\mathrm Nv\),
\(\alpha_*=r/2-1/4\), \(T_*=U^{\alpha_*}\), and \(Z=\sqrt{CD}\).
The exact coefficient representation is
\[
 c_Z(g^2h)=\mu_F(h)d_{Z/q_g}(h),\qquad
 d_Y(h)=\sum_{a_0b_0=h}1_{q_{a_0},q_{b_0}\le Y},
\]
where \(g,h\) are squarefree and coprime. Here \(g\) is the common
factor of the **two truncated inverse factors** defining \(c_Z\).
It is not the common factor of an original inverse pair in Note 14,
nor the common factor of the two full marked columns in a row transform.

Set
\[
 \gamma(d,r)=\frac{(1-d)r}{2}+\frac1{250},\qquad
 G=U^{\gamma(d,r)},\qquad
 \frac{207}{1000}\le\gamma\le\frac{297}{1250}.
\]
Define the literal large-common-factor amplitude
\[
 H_{G,u}=-D^{-1/2}
 \sum_{\substack{g,h\ \mathrm{squarefree},\ (g,h)=1\\
          q_g\ge G,\ q_g^2q_h>T_*}}
 \mu_F(h)d_{Z/q_g}(h)\psi_u(g^2h)P_u(D/(q_g^2q_h)).       \tag{1}
\]
The factor caps in \(d\), the total original annulus in \(P\), and
every physical zero remain. Since \(2\gamma\ge207/500>23/200>\alpha_*\),
the product cut is automatically satisfied here for sufficiently large
\(U\); retaining it in (1) makes the support relation explicit.

For bounded fixed profiles, \(|\psi_u|\le1\), and all original rows,
\[
 \begin{aligned}
 |H_{G,u}|
 &\ll D^{-1/2}\sum_{q_g\ge G}
       \sum_{q_hq_l\le CD/q_g^2}d_{2,F}(h)\\
 &\ll_\varepsilon D^{1/2}U^\varepsilon
                        \sum_{q_g\ge G}q_g^{-2}
 \ll_\varepsilon D^{1/2}G^{-1}U^\varepsilon.             \tag{2}
 \end{aligned}
\]
The middle estimate uses the fixed three-factor divisor count on good
ideals; the last follows from ideal counting and partial summation.
This positive count is an upper bound after preserving the exact support,
not an assertion that \(d_Y\) is multiplicative.

The selected fourth mass from Note 22 consequently gives
\[
 F_G:=\sum_uV_u|H_{G,u}|^2
 \ll_\varepsilon U^{1+r-2\gamma+\varepsilon}H^b
       =U^{1+dr-1/125+\varepsilon}H^b.                  \tag{3}
\]
Let \(M_\dagger=M_*-H_G\), and \(F_\dagger=\sum_uV_u|M_{\dagger,u}|^2\).
The existing full envelope for \(F_*\) is
\(F_*\ll U^{1+dr+12re_{\rm src}+\varepsilon}H^b\), by the original
inverse bound and Note 24's controlled difference. Weighted Cauchy gives
the exact complete difference estimate
\[
 |F_*-F_\dagger|\le2\sqrt{F_*F_G}+F_G
 \ll_\varepsilon U^{1+dr-\delta_G+\varepsilon}H^b,
 \qquad \delta_G=\frac1{250}-6re_{\rm src}.             \tag{4}
\]
Under the same source buffer cap,
\[
 \delta_G\ge\frac1{250}-\frac{219}{50}e_{\rm src}
 \ge\frac{79927}{20000000},\qquad
 \delta_G-\frac1{700}\ge\frac{359489}{140000000}.        \tag{5}
\]
Its short square has the stronger saving \(1/125\). Combining (4) with
Note 24 retains the earlier total removal saving \(7979/2000000\),
and therefore the same fixed-cost reserve \(35853/14000000\).
All literal source, witness, profile and height costs retain their
previous separate budgets.

The smaller sufficient selected theorem is now
\[
 \boxed{F_\dagger\ll_\varepsilon
                     U^{1+dr-1/700+\varepsilon}H^b.}    \tag{6}
\]
It is equivalent at that exponent to the original target under these
controlled differences. Its exact inverse retains
\(q_g<G\), squarefree coprime \(g,h\), \(q_g^2q_h>T_*\),
both caps through \(d_{Z/q_g}(h)\), and the arbitrary plain quotient.
The signed squarefree core \(\mu_F(h)\) remains.

## 2 A legal large-sieve estimate still misses the target

For a literal factor block \((A,B,L)\) from Note 24 put \(Y=AB\).
Grouping the two inverse factors gives a sixth-power-free cofactor
coefficient (valuations at most two). For each fixed quotient \(l\)
its squared coefficient norm is \(O_\varepsilon(YU^\varepsilon)\).
The transferred sixth-order sieve applies, retaining the row zero
\(\psi_u(l)\) as a modulus-at-most-one multiplier. Minkowski over
the \(O(L)\) quotients and the original \(D^{-1/2}\) normalizer give
\[
 \sum_{\substack{q_u\ll U\\u\ \mathrm{sixth\text{-}power\text{-}free}}}|R_{\gamma,u}|^2
 \ll_\varepsilon L\Theta_6(U,Y)U^\varepsilon,
 \quad YL\asymp D.                                    \tag{7}
\]
The source input here is the [sixth-order large sieve](https://arxiv.org/html/2610.04045v1)
and its already imported native transfer; no transformed-bin pointwise
bound is assumed. Inserting the selected plain/slot pointwise envelope
gives exponent at the physical row radius \(O(U)\)
\[
 2dm+\Gamma_J+r-y+\max(1,5/6+y/3),\qquad y=\log_U Y\le r+O(1/\log U),
\]
with the fixed annular constants absorbed in the allowed small loss.
At exponent level the other terms of \(\Theta_6\) are smaller for
\(y\le r<73/100\). The same proof applies directly to the residual
blocks with \(q_{(a,b)}<G\) imposed inside their row-independent
coefficients; this restriction is not treated as a positive norm comparison
with the unsliced block. Use the baseline envelope \(\Gamma_J=dz_J\ge0\).
This expression decreases with \(y\), so the best short-quotient
endpoint is \(y=r\). Even there its deficit relative to (6) is
\[
 -1/6+r(1/3-d)+2dm+\Gamma_J+1/700
 \ge\frac{5423}{52500}>0.                              \tag{8}
\]
After dropping \(\Gamma_J\ge0\), the comparison increases in \(m\) and \(d\) (the latter derivative is
\(2m-r>0\)), decreases in \(r\) at \(d=9/25\), and has lower corner
\((d,m,r)=(9/25,2/5,73/100)\) with \(\Gamma_J\ge0\).
The strict working boundaries only strengthen that comparison.
This is a useful legal upper estimate, not the required new saving.

## 3 The unrestricted smooth remainder has a principal-row obstruction

This diagnostic concerns an explicitly specified broader class. Take
a genuinely principal fixed native/ray presentation, untwisted fixed
profiles with nonzero principal means, and \(J=\varnothing\).
For example choose nonzero nonnegative smooth \(A_0,B\). Let a smooth
nonnegative full-row envelope be bounded below on some fixed annulus
of \(q_u/U\). It includes good rows \(u=p^6\) whose polynomial
character is \(\psi_{p^6}(n)=1_{(n,p)=1}\).
Such rows are auxiliary: they are excluded from the original
sixth-power-free, nonprincipal, high-conductor selected family.

We prove that the full **uncentered** smooth moment cannot obey (6)'s
exponent uniformly in this class. The proof uses the usual fixed-field
prime ideal theorem, elementary ideal counting, and the analytic
continuation of the good-ideal zeta function
\[
 \zeta_{F,S}(s)=\zeta_F(s)\prod_{p\in S}(1-q_p^{-s}),\qquad
 \zeta_F(s)=\zeta(s)L(s,\chi_{-3}).
\]
The factorization follows prime by prime from splitting in the quadratic
field. The nonprincipal Dirichlet factor is entire and nonzero at one;
the finite Euler factors are nonzero when \(\Re s>0\).
Critical-line zeros of \(\zeta\) therefore supply nontrivial zeros of
\(\zeta_{F,S}\) with real part \(1/2\). These standard analytic facts
are recorded in [DLMF 25.10](https://dlmf.nist.gov/25.10) and
[DLMF 25.15](https://dlmf.nist.gov/25.15); no RH assumption is used.

### 3.1 The principal polynomial cannot satisfy a subcritical power bound

Put \(C_2(T)=\sum_{q_t\le T}(\mu_F*\mu_F)(t)/q_t\), and let
\(L(U)=M_{*,1}(U)\), with the unit denoting the unpunctured principal
polynomial, not a selected row. Smooth ideal counting gives
\[
 P_1(X)=\kappa_A X+O_{A_0}(X^{1/2}),\qquad
 \kappa_A=\operatorname{Res}_{s=1}\zeta_{F,S}(s)\widehat A_0(1)\ne0.
\]
Over the Eisenstein lattice the ideal count is its area term plus
\(O(X^{1/2})\); partial summation handles the fixed smooth profile.
The finitely many good-prime exclusions are a fixed inclusion-exclusion
sum. The summed normalized error is bounded by
\(\sum_{q_t\le T_*}|c_Z(t)|q_t^{-1/2}\ll T_*^{1/2+\varepsilon}\).
Thus
\[
 L(U)=M_1(U)+\kappa_A U^{r/2}C_2(U^{\alpha_*})+E(U),     \tag{9}
\]
where \(E(U)\ll_\varepsilon U^{\alpha_*/2+\varepsilon}\).

For \(\Re s>r/2\), the Mellin transform over \(U\ge U_0\), modulo
a correction holomorphic for \(\Re s>\alpha_*/2\), is exactly
\[
 \mathcal L(s)=
 \frac{\widehat A_0(1/2+s/r)}{r\zeta_{F,S}(1/2+s/r)}
 +\frac{\kappa_A}{s-r/2}
       \zeta_{F,S}\!\left(1+\frac{s-r/2}{\alpha_*}\right)^{-2}
 +\mathcal E(s),\qquad \mathcal E\ \mathrm{holomorphic\ for}\
                         \Re s>\alpha_*/2.             \tag{10}
\]
The second identity follows by integrating each sharp summatory step
from \(U=q_t^{1/\alpha_*}\) to infinity. The original profile remains
in the first term; no common-Mellin-variable substitution is used.

Write \(\vartheta=\alpha_*/r\in(0,1)\) and
\(E_{\rm crit}=(r-\alpha_*)/2\). Suppose for some \(\eta>0\) that
\(L(U)=O(U^{E_{\rm crit}-\eta})\). Its Mellin integral is then
holomorphic on \(\Re s>E_{\rm crit}-\eta\). The correction in (10)
is holomorphic at every pole considered below, because
\(E_{\rm crit}-\alpha_*/2=1/4\).
A nontrivial zero \(\rho\) of \(\zeta_{F,S}\) with \(\Re\rho\ge1/2\)
produces a pole in the second term of (10) at
\(s_\rho=r/2+\alpha_*(\rho-1)\), inside this domain.
For cancellation, the first term must also have a pole, so necessarily
\[
 \zeta_{F,S}(1-\vartheta+\vartheta\rho)=0.               \tag{11}
\]
That new zero has real part at least \(1/2\). Iterating (11) produces
zeros \(1+\vartheta^n(\rho-1)\) tending to one. This contradicts
the simple pole, and consequent punctured zero-free neighborhood, at
one. A zero of the profile's entire Mellin transform cannot evade the
argument: it can suppress a first-term pole, but cannot create one to
cancel the nonzero second term.

Consequently, for every \(\eta>0\),
\[
 L(U)\ne O(U^{E_{\rm crit}-\eta}).                       \tag{12}
\]
This is an oscillation/power obstruction, not a pointwise lower bound
at every scale, nor a claim of RH.

### 3.2 Actual annular principal rows transfer the obstruction

There are \(\gg U^{1/6}/\log U\) good prime ideals with
\(q_p\asymp U^{1/6}\) and \(p^6\) in the envelope's positive annulus.
For all such primes, the divisor bound on the original flattened
coefficient gives uniformly
\[
 |M_{*,p^6}(U)-L(U)|
 \ll_\varepsilon U^{r/2-1/6+\varepsilon}.              \tag{13}
\]
Indeed only full inverse columns divisible by \(p\) are deleted;
there are \(O_\varepsilon(DU^\varepsilon/q_p)\) counted with their
divisor multiplicities. Smooth counting likewise gives
\[
 S_{p^6}(U)=\kappa_B U^{m/2}
                   +O_\varepsilon(U^{m/2-1/6+\varepsilon}),
 \qquad \kappa_B\ne0.                                  \tag{14}
\]
The deletion error exponent in (13) is strictly below \(E_{\rm crit}\):
\[
 E_{\rm crit}-(r/2-1/6)=1/6-\alpha_*/2
                                      \ge131/1200.      \tag{15}
\]
For a given \(\eta>0\), choose
\(0<\delta<\min(\eta/4,131/4800)\). By (12), along arbitrarily large
scales \(|L(U)|>U^{E_{\rm crit}-\delta}\). The deletion in (13) is then
negligible for every prime-sixth row in this annulus. Their positive norm
sum is at least \(cU^{E_{\rm low}-2\delta}/\log U\), whose ratio to
\(U^{E_{\rm low}-\eta}\) diverges. Hence the full smooth norm is not
\(O(U^{E_{\rm low}-\eta})\), where
\[
 E_{\rm low}=1/6+(r-\alpha_*)+2m=5/12+r/2+2m.
\]
Its excess over the proposed mixed exponent is uniformly at least
\[
 E_{\rm low}-(1+dr-1/700)
 =-7/12+(1/2-d)r+2m+1/700
 \ge\frac{1439}{5250}>0.                                \tag{16}
\]
The conditional first-Poisson zero bound of Note 24 is only
\(O(U^{1+\varepsilon})\). Since \(E_{\rm low}\ge47/30>1\),
the complete **nonzero** first-frequency aggregate in this full smooth
problem also has positive oversized contributions along a sequence.
Its desired target-sized signed bound therefore fails in this class.
The controlled large-\(g\) piece does not fix this: (2) bounds its
amplitude by \(U^{dr/2-1/250+\varepsilon}\), strictly below the
principal obstruction exponent, with gap at least \(157/1000\).

For positive prime slots with nonzero principal means, all their scales
are below \(U^{1/6}\); the same row prime does not meet their windows.
Their principal lower bounds add \(z_J\) to \(E_{\rm low}\), up to
logarithms. Arbitrary signed slot coefficients do not permit this
addition. The zero-slot instance already refutes a uniform class theorem
covering it. A genuinely nonprincipal fixed ray factor or a zero-mean
inverse/plain profile is not covered by this diagnostic. An appropriately
centered two-plain difference can cancel the principal main response,
but its comparison estimate and marked child bounds must be proved.

## 4 Preserve the row restriction in the next estimate

The safe surviving theorem is (6) on the original selected family.
One cannot now justify its proof by proposing the same exponent for
every unrestricted uncentered smooth marked norm.
For a sixth-power-free physical-row restriction there is at least an
exact smooth-row interface:
\[
 1_{u\ \mathrm{sixth\text{-}power\text{-}free}}
 =\sum_{q^6\mid u}\mu_F(q).
\]
If \(\mathcal P_u=X^{-1/2}\sum_k a(k)\psi_u(k)\), then
\[
 \sum_{u\ \mathrm{sixth\text{-}power\text{-}free}}
 \Omega(q_u/U)|\mathcal P_u|^2
 =\sum_q\mu_F(q)\sum_v\Omega(q_q^6q_v/U)
  \left|X^{-1/2}\sum_k a(k)\psi_v(k)1_{(k,q)=1}\right|^2.              \tag{17}
\]
This is a finite identity for a compactly supported envelope and a fixed
native presentation; bounded unit/ray splits stay literal. Taking the
absolute values of its \(q\)-terms restores the principal rows whose
complete signed combination removes them. The high primitive-conductor
condition is additional and is not a radial smooth weight.

For comparison, a crude cutoff \(q\le Q\) in (17), using only
\(|\mathcal P_u|^2\ll XU^\varepsilon\), has tail bound
\(UXQ^{-5}U^\varepsilon\). For a smaller power cutoff
\(Q=U^\sigma\), \(0<\sigma<1/6\), this comparison cannot certify
the mixed target: it would need
\((r+2m+z_J-dr+1/700)/5>1/6\).
The full cutoff \(Q\ge(CU)^{1/6}\) makes the tail identically zero,
but leaves the complete signed mask aggregate to estimate. Neither
absolute mask summation nor a small arbitrary mask cutoff provides the
missing fixed gain.

Fixed-ray prime counting, if a compatible finite presentation requires it,
is supplied by [Pollack–Troupe, Theorem 2.1, printed p. 4](https://www.pollack-math.net/irreddiv-bams.pdf).
The standard inputs retain their imported status.

The next estimate must keep the selected/high-conductor row conditions,
prove a suitable signed mask aggregate, or establish a centered smooth
comparison with its own bounds. The large inverse-factor common part is
now removed. The surviving small-\(g\), signed squarefree-core correlation
is still open; no new mixed fourth theorem or zero-free boundary follows.

The [checker](../../numerics/check_mixed_squarepart_estimate.py) and
[record](../../numerics/mixed_squarepart_estimate_record_20261009.json)
test finite splits, zeros, cross terms, projector identities and rational
budgets. They do not prove the Mellin obstruction or an unbounded moment.
The [review](../../reviews/MIXED_SQUAREPART_AND_SMOOTH_REVIEW_20261009.md)
records the separate same-model audits and manuscript compilation.
