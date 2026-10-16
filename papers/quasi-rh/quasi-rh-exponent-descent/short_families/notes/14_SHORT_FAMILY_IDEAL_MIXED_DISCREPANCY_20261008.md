# Exact ideal mixed discrepancy for the adaptive tail

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: exact algebraic and Stieltjes identities, plus elementary tail bounds.
No new signed power estimate, zero-free region, or exponent descent is proved.
These are internal mathematical deductions and finite algebra checks, not
independent specialist review.

## Outcome

The integer mixed-discrepancy method has an exact ideal analogue, and it can
be connected directly to the manuscript's actual adaptive convolution tail.
The logarithmic derivation of the two truncated Mobius factors introduces
one von Mangoldt factor without discarding their signed compensation. A
pointwise Stieltjes decomposition then retains the principal density, both
cutoff endpoints, complex character values, all overlapping factors, and the
row-dependent adaptive selector. A capped high/high Riesz formulation makes
both low/high edge sums explicit.

This is an additional exact interface for an arithmetic estimate. It does
not supply that estimate. In particular, neither low/high edge is bounded
here, and replacing the mixed terms by separate Mertens/PNT envelopes does
not resolve the existing power barrier.

The source identities being extended are the short-family manuscript,
Section 4, and the product-coordinate closure in
`papers/prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_CLOSURE_ATTEMPT_20261004.md`,
Sections 1--3. The sharper integer complete-functional remainder in
`fixed_scale_descent/notes/3_ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md`
is not assumed to transfer to these ideal/Hecke quantities.

## 1. Zero-extended ideal coefficients and their logarithmic derivation

All convolution variables belong to the manuscript's good ideal monoid
\(\mathcal I_S\). For a fixed nonzero physical row \(u\), retain the actual
completely multiplicative, zero-extended character \(\lambda_u\), and put

\[
 f_u(n)=\mu_K(n)\lambda_u(n),\qquad
 g_u(n)=\Lambda_K(n)\lambda_u(n).
 \tag{1}
\]

Here \(\Lambda_K(p^j)=\log\mathrm Np\) for good prime ideals \(p\) and
integers \(j\ge1\), and it is zero otherwise, including the unit ideal.
No squarefreeness or coprimality condition is imposed on separate factors.

For a coefficient sequence \(a\), let
\(\mathscr Da(n)=a(n)\log\mathrm Nn\). This is a derivation for ideal
convolution, since \(\log\mathrm N(ab)=\log\mathrm Na+\log\mathrm Nb\).
The identities \(\mu_K*\mathbf1=\delta_1\) and
\(\Lambda_K*\mathbf1=\log\mathrm N\), or their Euler factors, give

\[
 \mu_K*\Lambda_K=-\mu_K\log\mathrm N.
\]

Multiplication by \(\lambda_u\) commutes with convolution, including when
factors overlap or contain a deletion prime. Therefore

\[
 k_u:=f_u*g_u=-f_u\log\mathrm N.
 \tag{2}
\]

This is exact for every ideal and every physical row, without a bound for a
Hecke L-function. In particular \(k_u(1)=0\).

For \(z\ge1\), define
\[
 m_{u,z}=f_u\mathbf1_{\mathrm Nn\le z},\qquad
 b_{u,z}=m_{u,z}*m_{u,z}=c_z\lambda_u.
\]
Equation (2) gives
\(\mathscr Dm_{u,z}=-(k_u\mathbf1_{\mathrm Nn\le z})\), and hence

\[
 (\log\mathrm Nd)b_{u,z}(d)
 =-2\big[(k_u\mathbf1_{\mathrm Nn\le z})*m_{u,z}\big](d).
 \tag{3}
\]

The norm cutoff in the first factor on the right is on the WHOLE product
in \(k_u=f_u*g_u\), not independently on its two factors.

## 2. The exact logarithmic bridge to the adaptive tail

Use the manuscript's fixed annulus, \(z=\sqrt{CD}\),
\(Y_u=D^{1-\theta}/L_u\), and complete free ideal sum

\[
 S_u(X)=\sum_m\lambda_u(m)W(\mathrm Nm/X).
\]

The actual adaptive tail is
\[
 T_u(D)=-\sum_{\mathrm Nd>Y_u}b_{u,z}(d)S_u(D/\mathrm Nd).
 \tag{4}
\]

At the unit ideal \(b_{u,z}(1)=1\); its term occurs exactly when
\(Y_u<1\). Divide (3) by \(\log\mathrm Nd\) only for \(d\ne1\).
The resulting exact formula is

\[
\begin{split}
 T_u(D)={}&-\mathbf1_{Y_u<1}S_u(D)\\
 &+2\sum_{\substack{\mathrm N(ab)\le z,\ \mathrm Nc\le z\\
                   \mathrm N(abc)>Y_u,\ \mathrm N(abc)>1}}
 \frac{f_u(a)g_u(b)f_u(c)}{\log\mathrm N(abc)}
 S_u\!\left(\frac D{\mathrm N(abc)}\right).
\end{split}
 \tag{5}
\]

Every sum is finite. The apparent extra condition \(\mathrm N(abc)>1\)
only avoids division by zero; \(g_u(1)=0\). The product selector in (5)
is still row-dependent. No completed row kernel has been used, so this
pointwise identity does not insert an unsupported selector into Poisson.

## 3. The correct principal density coefficient

Define the right-continuous finite sums

\[
 \Psi_u(t)=\sum_{\mathrm Nb\le t}g_u(b),\qquad
 \delta_u=\mathbf1_{\psi_u\ {\rm principal}},\qquad
 E_u(t)=\Psi_u(t)-\delta_ut,
 \tag{6}
\]

where \(\psi_u\) is the inducing primitive Hecke character of the manuscript.
The density coefficient here is \(\delta_u\), not the free ideal-sum
residue \(\kappa_u\). Indeed, for \(\Re s>1\),

\[
 \sum_n\frac{g_u(n)}{(\mathrm Nn)^s}
 =-\frac{\mathcal Z'_u}{\mathcal Z_u}(s),\qquad
 \mathcal Z_u(s)=\sum_n\frac{\lambda_u(n)}{(\mathrm Nn)^s}.
\]

A principal primitive character gives a simple pole of \(\mathcal Z_u\) at one,
with residue \(\kappa_u\), and therefore a pole of
\(-\mathcal Z'_u/\mathcal Z_u\) of
residue **one**. The deleted Euler factors are holomorphic and nonzero at
one and do not multiply that residue. For example, on a principal row the
weighted prime-power sum is the full ideal von Mangoldt sum minus the
prime powers at the deleted primes, with the same leading density one.

The identities below require no asymptotic estimate for \(E_u\): (6) is an
exact definition. The classical fixed-character interpretation of the
principal density does not assert conductor-uniform error bounds.

## 4. Raw centered Stieltjes formula, with both endpoints

Fix \(\eta_0=3/2\). Nonunit ideal norms are integers at least two, so
replacing a lower bound less than \(\eta_0\) by \(\eta_0\) removes no
von Mangoldt atom. This choice also avoids creating divergent separated
continuum integrals from \(1/\log t\) at \(t=1\).

For each pair \(a,c\) in (5), write

\[
 x=\mathrm Na\,\mathrm Nc,\quad
 \ell=\max\{\eta_0,Y_u/x\},\quad r=z/\mathrm Na,\quad
 F_{u,x,D}(t)=\frac{S_u(D/(xt))}{\log(xt)}.
 \tag{7}
\]

If \(\ell\ge r\), the contribution is zero. Otherwise the sum over
the von Mangoldt factor is exactly
\(\int_{(\ell,r]}F_{u,x,D}(t)\,d\Psi_u(t)\). Put
\(E_{u;\ell}(t)=E_u(t)-E_u(\ell)\). Stieltjes integration by parts gives

\[
\begin{split}
 \int_{(\ell,r]}F(t)\,d\Psi_u(t)
 ={}&\delta_u\int_\ell^rF(t)\,dt
   +F(r)E_{u;\ell}(r)
   -\int_\ell^rE_{u;\ell}(t)F'(t)\,dt.
\end{split}
 \tag{8}
\]

The values at both cutoffs are right-continuous: an atom exactly at
\(\ell\) is excluded and one at \(r\) is included. The lower endpoint
has not been dropped; it is retained in the increment \(E_{u;\ell}\).
Equation (8), multiplied by \(2f_u(a)f_u(c)\) and summed, together with
the explicit unit term in (5), is the requested complete centered bridge.
It holds for complex \(\lambda_u\); no real sign or positivity is used.

If \(\mathcal DW(v)=vW'(v)\), its derivative is explicitly

\[
 F'_{u,x,D}(t)=\frac1t\left\{
 \frac{S_{u,\mathcal DW}(D/(xt))}{\log(xt)}
 -\frac{S_{u,W}(D/(xt))}{\log^2(xt)}\right\}.
 \tag{9}
\]

For zero-integral \(W\), integration by parts gives
\(\int\mathcal DW=-\int W=0\). Thus both free sums in (9) have zero
principal Poisson frequency. The distinct von Mangoldt density term
\(\delta_u\int F\) in (8) still must be retained. Zero integral alone
does not delete it.

One can split \(a\) at a real cutoff \(U\ge1\) and \(b\) at
\(V\ge1\), keeping all four combinations. These are a capped high/high
part, both low/high edge parts, and a low/low part, all still subject to
\(\mathrm N(ab)\le z\) and \(\mathrm N(abc)>Y_u\). The low/low part
is exactly empty if

\[
 UVz\le Y_u.
 \tag{10}
\]

No such deletion is claimed outside (10). It follows simply from
\(\mathrm N(abc)\le UVz\) on that part. In particular, arbitrary small
fixed row conductor does not license discarding either low/high edge.

At the concrete test point \(h=a=2/5,\theta=1/40\), one can take
\(U=V=D^{1/50}\). On the enlarged significant row range
\(\mathrm Nu\le D^{17/40}\), the existing bound \(L_u\ll\mathrm Nu\)
gives \(Y_u\gg D^{11/20}\), whereas
\(UVz=\sqrt C D^{27/50}\). Their exponent margin is \(1/100\), so
the low/low contribution is exactly empty for sufficiently large \(D\).
This makes the first analytic test a capped high/high term together with
both low/high edges, rather than four independent terms. No estimate for
those three surviving terms is supplied. The omitted farther rows still
require the Schwartz argument, not this cutoff comparison.

## 5. Complete capped high/high Riesz representation

For any ideal sequence \(a\), put

\[
 \mathcal L_a(R)=\sum_{\mathrm Nn\le R}a(n)
                       \log\frac R{\mathrm Nn}.
\]

For \(R\ge UV\), define

\[
\begin{split}
 M_{u;U}(s)&=\sum_{U<\mathrm Na\le s}f_u(a),\\
 E_{u;V}(t)&=\Psi_u(t)-\Psi_u(V)-\delta_u(t-V),\\
 \mathcal C_{u;U,V}(R)&=
 \int_U^{R/V}M_{u;U}(s)E_{u;V}(R/s)\,\frac{ds}{s},\\
 \mathcal H_{u;U,V}(R)&=
 \sum_{\substack{\mathrm Na>U,\ \mathrm Nb>V\\\mathrm N(ab)\le R}}
 f_u(a)g_u(b)\log\frac R{\mathrm N(ab)},\\
 \mathcal D_{u;U,V}(R)&=
 \sum_{U<\mathrm Na\le R/V}f_u(a)
 \left\{\frac R{\mathrm Na}-V
        -V\log\frac R{V\mathrm Na}\right\}.
\end{split}
 \tag{11}
\]

Set the last three quantities to zero for \(R<UV\). Then exactly

\[
 \mathcal H_{u;U,V}(R)=
 \mathcal C_{u;U,V}(R)+\delta_u\mathcal D_{u;U,V}(R).
 \tag{12}
\]

Proof: expand both finite increments in \(\mathcal C\). A pair of
arithmetic atoms \(a,b\) integrates over
\(\mathrm Na\le s\le R/\mathrm Nb\) and contributes the logarithm
in \(\mathcal H\). The continuous part for a fixed \(a\) is

\[
 \int_{\mathrm Na}^{R/V}(R/s-V)\,\frac{ds}{s}
 =\frac R{\mathrm Na}-V-V\log\frac R{V\mathrm Na}.
\]

There is no independence assumption, absolute value, or missing terminal
band in this calculation. At equality in a product cap the logarithm,
or the displayed density bracket, vanishes.

Both edge sums are exposed by the all-scale identity

\[
\begin{split}
 \mathcal L_{k_u}(R)={}&\mathcal H_{u;U,V}(R)
 +\sum_{\mathrm Na\le U}f_u(a)\mathcal L_{g_u}(R/\mathrm Na)\\
 &+\sum_{\mathrm Nb\le V}g_u(b)\mathcal L_{f_u}(R/\mathrm Nb)\\
 &-\sum_{\substack{\mathrm Na\le U,\ \mathrm Nb\le V\\
                   \mathrm N(ab)\le R}}
      f_u(a)g_u(b)\log\frac R{\mathrm N(ab)}.
\end{split}
 \tag{13}
\]

This is inclusion-exclusion on the two cutoffs, valid for every \(R>0\).
The final low/low cap is redundant only when \(R\ge UV\). The first
edge sum is low/full and the second full/low; subtracting their common
low/low part once retains both genuine low/high edges. Equation (2) also
gives

\[
 \mathcal L_{k_u}(R)
 =-\sum_{\mathrm Nn\le R}f_u(n)\log\mathrm Nn
                      \log\frac R{\mathrm Nn}.
 \tag{14}
\]

To recover (5) from this Riesz formulation without losing sharp boundaries,
write \(K_u(R)=\sum_{\mathrm Nn\le R}k_u(n)\). For smooth \(\varphi\)
on \([A,B]\), finite partial summation twice gives

\[
 \sum_{A<\mathrm Nn\le B}k_u(n)\varphi(\mathrm Nn)
 =\big[K_u(R)\varphi(R)-\mathcal L_{k_u}(R)R\varphi'(R)\big]_A^B
  +\int_A^B\mathcal L_{k_u}(R)(R\varphi'(R))'\,dR.
 \tag{15}
\]

Use \(A=\max\{\eta_0,Y_u/\mathrm Nc\}\), \(B=z\), and
\(\varphi(R)=S_u(D/(R\mathrm Nc))/\log(R\mathrm Nc)\), only when \(A<B\), then sum
with coefficient \(2f_u(c)\). If \(A\ge B\), that contribution is empty and is set to zero.
The unit term is still supplied separately by (5). Insert (12)--(13) in (15); their boundary terms must be inserted
as well. Formula (15) is not permission to drop a derivative or an edge.

## 6. Relation to the original detector and the complete row weight

Equations (3)--(15) are identities for the same \(T_u\), so they add no
loss to the manuscript's equivalence between its zero-integral full moment
and its adaptive tail moment. For the following detector statement, assume explicitly that \(\int W=0\).
For a fixed row, the manuscript's all-scale completion shows \(A_{u,W}(D)-T_u(D)=O_{N,u,W}(D^{-N})\) for every
\(N\). Consequently, after removing a compact initial scale interval,
the Mellin transform of this mixed-discrepancy expression differs from

\[
 \frac{\widehat W(s)}{\mathcal Z_u(s)}
 \tag{16}
\]

by an entire function. Every detecting pole is preserved. This assertion
uses the existing free-factor completion, not a new Mobius estimate, and
does not replace its conductor dependence by fixed-row constants when
summing over the family.

For completeness, an elementary uniform bound is
\(T_u(D)\ll_W D\log^2(2D)\). Indeed,
\(|S_u(D/\mathrm Nd)|\ll_W D/\mathrm Nd\) on its nonempty support,
and
\(\sum_d|b_{u,z}(d)|/\mathrm Nd\le(\sum_{\mathrm Na\le z}1/\mathrm Na)^2
\ll\log^2(2D)\). Therefore, for \(H=D^h\) and any fixed \(\eta>0\),
the complete Schwartz-weighted normalized tail moment on
\(\mathrm Nu>D^{h+\eta}\) is \(O_N(D^{-N})\) for every \(N\), choosing
the Schwartz decay order after \(N\).

If desired, choose \(0<\theta<1-h\). The unit term \(Y_u<1\) then
requires \(L_u>D^{1-\theta}\), hence \(\mathrm Nu\gg D^{1-\theta}\)
by the manuscript's radical comparison. It lies in the negligible row
region just described. For a general \(\theta\) its exact term in (5)
is retained. This is a supporting elementary bound, not an estimate for
the unresolved significant rows.

## 7. Finite verification and the remaining obligation

The [checker](../../numerics/check_short_family_ideal_discrepancy.py) is a standalone deterministic,
standard-library checker with JSON on stdout and no generated files.
Its [retained record](../../numerics/short_family_ideal_discrepancy_record_20261008.json)
lists 638 named equality checks; two fresh runs reproduced it byte-for-byte.
It uses six distinct good prime-ideal symbols with norms
\((7,7,13,13,25,31)\), arbitrary completely multiplicative sixth-root
phases, and deletion zeros. Comparisons keep logarithms as formal variables
and use exact arithmetic in \(\mathbb Q[\zeta_6][\log p]\).

Its scope is finite algebra and endpoint conventions. It does not validate
native sextic reciprocity, an actual physical row character, Poisson decay,
the Hecke prime ideal theorem, or an asymptotic signed moment.

The missing input is still a power bound for the COMPLETE expression (8),
or equivalently (12)--(15) with all density and edge terms, under the
manuscript's complete row weight. Complex character values do not supply a
one-sided Landau argument automatically. Positive separate majorants can
destroy precisely the compensation at issue. No new signed gain is claimed.

The companion [divisor packet result](15_SHORT_FAMILY_DIVISOR_PACKET_CANCELLATION_20261008.md)
controls one actual sector, while the [product-sector barrier](16_SHORT_FAMILY_PRODUCT_BARRIER_20261008.md)
locates the cross-total-product cancellation still needed. The
[scoped review](../../reviews/SHORT_FAMILY_SIGNED_PACKET_REVIEW_20261008.md)
records their joint logical limits.
