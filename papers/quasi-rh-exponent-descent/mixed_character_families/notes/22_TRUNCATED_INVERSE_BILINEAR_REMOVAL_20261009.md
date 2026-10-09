# Truncated inverse decomposition and a controlled bilinear sector

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. Same-model derivations and audits
are internal validation, not independent specialist review or formal verification.

This note proves a conditional removal for the **original selected positive
mixed moment**. An exact two-factor truncated inverse identity expresses the
inverse as a signed combination of plain responses. The part whose combined
cofactor has norm at most \(U^{1/10}\) has squared-response saving at least
\(1/125\), before literal source buffers. Weighted Cauchy then controls its
entire interaction with the rest, with saving approximately \(1/250\).
The surviving large-cofactor correlation remains unproved.

The imported analytic inputs are exactly the all-length bin bounds in
source (8.1)–(8.2), printed pp. 57–58, and the selected plain-fourth/slot
mass used in [notes 16–20](20_ORDERED_FOURTH_CONTINUATION_20261009.md).
The [primary manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
was read in memory; its SHA-256 is
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The deep source estimates and their family/bin hypotheses remain imported.

## 1 Original moment and hypotheses

Work on the good ideal monoid outside the fixed excluded set \(\mathcal S\).
Every row uses its actual multiplicative zero-extended native character
\(\psi_u\), with the original fixed ray factor and orientation retained.
Let
\[
 D=U^r,\quad N=U^m,\quad d=2a-1,\qquad
 M_u=D^{-1/2}\sum_{\mathfrak n}
       \mu_F(\mathfrak n)\psi_u(\mathfrak n)
       A_0(\mathrm N\mathfrak n/D).
                                                        \tag{1}
\]
The original fixed smooth profile \(A_0\) is supported in \([c,C]\), with
\(0<c<C\); the original bounded real powers and permitted pure norm twist
are included in the source profile convention. The selected weight is
\[
 V_u=1_{\mathcal C_+}(u)|S_u|^4|Q_J(u)|^2,\qquad
 F=\sum_u V_u|M_u|^2.                                  \tag{2}
\]
No selector is removed. Assume the source hypotheses that give, for every
permitted bounded length/profile and arbitrarily small additional loss,
\[
 \sum_u V_u\ll U^{1+\varepsilon}H^b,\qquad
 |M_u|^2\ll U^{dr+12er+\varepsilon}H^b.                  \tag{3}
\]
Here \(e>0\) is the already chosen source buffer. For a plain response
\[
 P_u(X)=\sum_{\mathfrak l}\psi_u(\mathfrak l)
                       A_0(\mathrm N\mathfrak l/X),
 \qquad S_u(X)=X^{-1/2}P_u(X),
\]
the reflected source bound, uniformly for the lengths used below, is
\[
 |S_u(U^x)|^2
 \ll U^{d(1-x)+(24-12x)e+\varepsilon}H^b.                \tag{4}
\]
Equation (4) comes from the reflected central line \(1-a-6e\), with
the source's conductor factor. Its nonprincipal-row and Mellin-tail
hypotheses are retained. It is not a bound for arbitrary coefficient
sequences. Constants depending on \(c,C\), the fixed field, finite ray
data and permitted profile family are harmless. The height exponent
\(b\) may increase under the finitely many products below.
The source's cumulative \(T_1/2\) allowance for extra Mellin frequencies
is also retained. Any conversion of \((1+T_1)^{A_A}\) into an arbitrarily
small added \(U\)-loss must use the source quantifier order and choose its
height schedule accordingly before the later external parameter. An
already fixed positive power cost from that schedule must instead be
carried in the exponents and deducted from the reserves, just like \(e\).

Use the closed comparison region
\[
 9/25\le d\le21/50,\qquad 7/10\le r\le73/100.            \tag{5}
\]
The actual operational region has a strict upper \(r\)-endpoint; proving
the bounds on (5) covers it. The same original whole-slot and witness
hypotheses as [note 19](19_SOURCE_SLOT_WITNESS_CERTIFICATE_20261009.md)
remain necessary to turn a new fourth estimate into the program's energy
implication.

## 2 Exact truncated inverse identity

Put \(Z=(CD)^{1/2}\), and on the good ideal monoid define
\[
 B_Z(\mathfrak n)=\mu_F(\mathfrak n)
                         1_{\mathrm N\mathfrak n\le Z},
 \qquad c_Z=B_Z*B_Z.                                    \tag{6}
\]
Then, including the endpoints and all prime powers,
\[
 \mu_F(\mathfrak n)
 =2B_Z(\mathfrak n)-(c_Z*\mathbf1)(\mathfrak n)
 \quad(\mathrm N\mathfrak n\le Z^2).                    \tag{7}
\]
Indeed, let \(R=\mu_F-B_Z\). Its support has norm strictly greater than
\(Z\), so \(R*R*\mathbf1\) has support strictly greater than \(Z^2\).
Using \(\mu_F*\mathbf1=\delta\), expand
\[
 B_Z*B_Z*\mathbf1=\mu_F-2R+R*R*\mathbf1.
\]
This proves (7), including the unit. On the original annulus, eventually
\(cD>Z\), while \(\mathrm N\mathfrak n\le CD=Z^2\).
Thus its \(2B_Z\)-term vanishes and multiplicativity, including physical
zeros, gives the exact regrouping
\[
 \boxed{M_u=-D^{-1/2}\sum_{\mathrm N\mathfrak t\le CD}
 c_Z(\mathfrak t)\psi_u(\mathfrak t)
 P_u(D/\mathrm N\mathfrak t).}                          \tag{8}
\]
No squarefree restriction is added to \(\mathfrak t\) or \(\mathfrak l\).
Each of the two factors defining \(c_Z\) is squarefree, but their product
can have valuation two. Higher powers in the complete reconstructed
coefficient cancel exactly. A character value that vanishes at a prime
continues to vanish in every positive power; there is no division by it.

The plain profile in (8) is literally
\(A_0(\mathrm N\mathfrak l/(D/\mathrm N\mathfrak t))\).
Only its permitted length changes. No \(\mathfrak t\)-dependent
character or deletion set is substituted for \(\psi_u\). If the original
profile carries a pure norm twist, it stays in that same profile; any
factor exposed by a different notation is a scalar of modulus one.

## 3 Short combined cofactor and its pointwise bound

Set \(T=U^\alpha\), \(\alpha=1/10\), and partition (8) exactly into
\[
 M_u=M_{I,u}+M_{L,u},\qquad
 M_{I,u}=-D^{-1/2}\sum_{\mathrm N\mathfrak t\le T}
    c_Z(\mathfrak t)\psi_u(\mathfrak t)P_u(D/\mathrm N\mathfrak t).
                                                               \tag{9}
\]
For large \(U\), \(T\le Z\). Every divisor of a short \(\mathfrak t\)
then has norm at most \(Z\), so on this sector only
\[
 c_Z(\mathfrak t)=(\mu_F*\mu_F)(\mathfrak t),\qquad
 c_Z(\mathfrak p)=-2,\quad c_Z(\mathfrak p^2)=1,
 \quad c_Z(\mathfrak p^k)=0\ (k\ge3).                    \tag{10}
\]
Consequently \(|c_Z(\mathfrak t)|\le\tau_F(\mathfrak t)\).
Fixed-field ideal counting and partial summation give
\[
 \sum_{\mathrm N\mathfrak t\le T}
 |c_Z(\mathfrak t)|(\mathrm N\mathfrak t)^{(d-1)/2}
 \ll_\varepsilon T^{(1+d)/2+\varepsilon}.                \tag{11}
\]
For \(y=\log_U\mathrm N\mathfrak t\), the plain length exponent is
\(x=r-y\), in \([3/5,73/100]\). The normalization is exact:
\[
 D^{-1/2}P_u(D/\mathrm N\mathfrak t)
       =(\mathrm N\mathfrak t)^{-1/2}S_u(D/\mathrm N\mathfrak t).
\]
Apply (4), then sum absolute coefficients only in this controlled sector.
Equations (9)–(11) imply
\[
 |M_{I,u}|^2\ll
 U^{d(1-r)+(1+d)\alpha+(24-12r+12\alpha)e+\varepsilon}H^b.
                                                               \tag{12}
\]
The saving relative to \(dr\), before buffers, is
\[
 \lambda_I(d,r)=d(2r-1)-(1+d)/10\ge1/125.                \tag{13}
\]
Both monotonicities are positive on (5), so the minimum is at
\((d,r)=(9/25,7/10)\). This is a uniform inequality, not a sampled grid.
Multiplying by the original mass in (3) bounds
\(F_I=\sum_uV_u|M_{I,u}|^2\) with the same gain.

## 4 Removing the square and every cross term

Define \(F_L=\sum_uV_u|M_{L,u}|^2\), retaining the original selected
weights. The exact identity is
\[
 F-F_L=2\operatorname{Re}\langle M,M_I\rangle_V-F_I.
\]
Weighted Hilbert Cauchy therefore gives
\[
 |F-F_L|\le2\sqrt{F F_I}+F_I.                           \tag{14}
\]
This controls the complete interaction, without any estimate for \(F_L\).
Use the existing envelope (3) for \(F\), and (12) for \(F_I\).
The two buffer terms must be combined **before** maximizing \(r\):
\[
 \tfrac12(12re)+\tfrac12(24-12r+12\alpha)e
       =(12+6\alpha)e=\tfrac{63}{5}e.                  \tag{15}
\]
If \(0<e\le1/1200000\), the \(F_I\)-term has more saving than the
cross term, and
\[
 \boxed{|F-F_L|\ll_\varepsilon
 U^{1+dr-\delta_e+\varepsilon}H^b,\qquad
 \delta_e=\frac1{250}-\frac{63}{5}e
       \ge\frac{7979}{2000000}.}                       \tag{16}
\]
This fixed buffer allowance also has to satisfy the source's own \(e_0\)
and the original simultaneous-witness budgets. It supplies an upper
allowance, not a license to choose a buffer larger than those budgets.
Any already fixed positive buffer stays visible in (12) and (16); it
cannot be hidden inside every requested \(\varepsilon\).
Equation (16) uses the small additional-loss ordering in (3)–(4);
fixed extra frequency or profile-envelope power costs must be added to
its error exponent before applying the target comparison.

The reserve over the current sufficient saving \(\chi=1/700\) is at least
\[
 \delta_e-\chi\ge\frac{35853}{14000000}>0.               \tag{17}
\]
The removal also fits the older stronger target \(\chi=1/540\), with
unbuffered reserve \(29/13500\); its literal buffer is subtracted as in
(15). The fine-slot certificate is not used to manufacture this sector
gain. It selects which remaining full-moment theorem is sufficient.

## 5 The exact surviving signed correlation

The new sufficient target is
\[
 \boxed{F_L\ll_\varepsilon U^{1+dr-1/700+\varepsilon}H^b.} \tag{18}
\]
By (16)–(17), it is equivalent at this target exponent to the original
new mixed estimate for \(F\), under the imported hypotheses. Its exact
expanded form is
\[
 F_L=D^{-1}
 \sum_{\substack{\mathrm N\mathfrak t>T,\,
                 \mathrm N\mathfrak t'>T\\
                 \mathrm N\mathfrak t,\mathrm N\mathfrak t'\le CD}}
 c_Z(\mathfrak t)\overline{c_Z(\mathfrak t')}
 \sum_u V_u\psi_u(\mathfrak t)\overline{\psi_u(\mathfrak t')}
 P_u(D/\mathrm N\mathfrak t)
 \overline{P_u(D/\mathrm N\mathfrak t')}.                \tag{19}
\]
Thus the row kernel is a positive Gram kernel before pairing with the
signed coefficients. Absolute pairwise estimation remains a stronger
problem. The two inverse factors within each \(c_Z\) keep their literal
cuts \(\mathrm N\mathfrak a,\mathrm N\mathfrak b\le Z\), and the plain
factor keeps \(cD\le\mathrm N(\mathfrak a\mathfrak b\mathfrak l)\le CD\).
The strict lower cut is on their **product**, not on each factor.

For \(\mathrm N\mathfrak t>Z\), the coefficient \(c_Z\) is generally
not multiplicative and cannot be replaced by \(\mu_F*\mu_F\). The
surviving sector includes unbalanced factors and short plain quotients;
it is not a uniformly balanced two-factor sum. A dyadic partition must
keep these cases and the original product inequality. If one later
extracts \(\mathfrak g=(\mathfrak t,\mathfrak t')\), the exact weights are
\(c_Z(\mathfrak g\mathfrak a)c_Z(\mathfrak g\mathfrak b)\), with the
exterior factor \(|\psi_u(\mathfrak g)|^2\). They are not the squarefree
inverse-pair weights from notes 14–15.
Only \((\mathfrak a,\mathfrak b)=1\) is forced; the common factor
\(\mathfrak g\) may still meet either residual factor.

This is an alternative reduction of the original positive \(F\).
It cannot silently inherit the old near-gcd/large-ratio selectors after
this regrouping. Nor can the signed remainder from notes 14–15 be
enlarged using the positivity of (19). Any combined reduction needs its
own exact tuple-level identity.

The [joint transform](21_SIGNED_JOINT_TRANSFORM_20261009.md) preserves the
complete coprimality projector and reveals frequency-divisor support.
Using it for (19) still requires a proof with this new coefficient class,
all factor cuts and all native masks. No bound for (18), new mixed moment,
or stronger zero-free boundary follows from the sector removal alone.

## 6 Validation

The [finite checker](../../numerics/check_mixed_signed_bilinear.py) and
[small record](../../numerics/mixed_signed_bilinear_record_20261009.json)
test the exact truncated identity, squareful reconstruction, original
normalization, zero-preserving regrouping, selected positive weights,
complete cross terms and rational buffer ledger. Their local finite-field
characters and formal ideal norms are not a construction of native
operational rows or zero bins. The analytic source estimates, ideal
counting and the unbounded remaining correlation are outside finite
verification. See the [same-model review](../../reviews/MIXED_TRUNCATED_INVERSE_BILINEAR_REVIEW_20261009.md).
