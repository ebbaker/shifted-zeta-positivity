# A complete masked discrepancy bridge for the squarefree residual

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: exact identities and conductor accounting, with an explicit
semiprime obstruction. No new signed moment estimate or exponent descent.
This derivation and its finite checks are internal validation, not
independent specialist review or formal proof verification.

## Result and scope

The mixed-discrepancy bridge of note 14 has an exact version for the
**squarefree total-product response at the retained cutoff**
\(Y_u=D^{9/20}/L_u\). The useful organization fixes two squarefree,
coprime outer factors \(c,m\), and adds their product \(h=cm\) to the
deletion mask of the inner character. The ordinary convolution
\(\mu\lambda_{u,h}*\Lambda\lambda_{u,h}\) is then already supported on
squarefree ideals coprime to \(h\). Consequently one can retain every
prime power inside a genuine product convolution and use the capped Riesz
identities, instead of inserting an unsupported squarefree selector into
the mixed integral.

The resulting identity retains the principal density, both edges, their
low/low overlap, every prime power, both adaptive endpoints, and all
deletion zeros. At this cutoff the earlier support argument for deleting
low/low does not apply. Moreover, balanced semiprimes have coefficient
\(+2\) and can lie wholly in the low/high edge. Thus opposing-edge
cancellation from note 19 does not bound this retained response. The
derivation supplies an exact arithmetic interface; its signed mean square
remains the same open target.

## 1. Definitions and the added mask

All ideals belong to the manuscript's good ideal monoid \(\mathcal I_S\).
Write \(N\) for ideal norm. Keep the actual zero-extended physical
character
\[
 \lambda_u(n)=\nu(n)\chi_n(u)
 =\psi_u(n)\mathbf1_{(n,E_u)=1},
 \qquad L_u=Q_uNE_u,
 \tag{1}
\]
where the primitive inducing character \(\psi_u\) is extended by zero
at its conductor and at the fixed bad primes. The extra deletion ideal
\(E_u\) has support disjoint from that conductor. Use
\[
 z=\sqrt{CD},\quad
 m_z(n)=\mu_K(n)\mathbf1_{Nn\le z},\quad c_z=m_z*m_z,
 \quad Y_u=D^{9/20}/L_u,
 \tag{2}
\]
and a smooth profile \(W\) supported on \([c_0,C]\subset(0,\infty)\).
The exact squarefree response is
\[
 T_{u,\mathrm{sf}}
 =-\sum_{\substack{d,m\\Nd>Y_u\\dm\ \mathrm{squarefree}}}
 c_z(d)\lambda_u(dm)W(N(dm)/D).
 \tag{3}
\]
The algebra below holds without \(\int W=0\). Zero integral is required
when using the previously proved moment equivalence and completion inputs.

For a fixed squarefree good ideal \(h\), define
\[
 \lambda_{u,h}(n)=\lambda_u(n)\mathbf1_{(n,h)=1},\qquad
 f_{u,h}(n)=\mu_K(n)\lambda_{u,h}(n),\qquad
 g_{u,h}(n)=\Lambda_K(n)\lambda_{u,h}(n).
 \tag{4}
\]
The coefficient \(\lambda_{u,h}\) remains completely multiplicative,
including all zero values; no such claim is made for \(f_{u,h}\) or
\(g_{u,h}\).
Here \(\Lambda_K(p^j)=\log Np\) for every \(j\ge1\); the factor
\(j\) must not be inserted. Ordinary ideal convolution gives
\[
 k_{u,h}:=f_{u,h}*g_{u,h}
 =-f_{u,h}\log N.
 \tag{5}
\]
Thus \(k_{u,h}(1)=0\), and it vanishes on nonsquarefree ideals and
on ideals meeting \(h\). Equation (5), rather than an independence
assertion, is what allows the squarefree projection to coexist with a
product convolution.

Prime powers are essential to (5) before recombination. For example,
at a repeated prime \(p^j\), \(j\ge2\), the terms with von Mangoldt
factors \(p^j\) and \(p^{j-1}\) have opposite Möbius signs and equal
weights \(\log Np\). If a total ideal has two repeated primes, no
single prime-power factor can leave a squarefree Möbius factor, so all
such terms already vanish. All these cancellations occur at a common
total ideal and retain its common physical phase, including a possible
deletion zero.

## 2. Exact logarithmic bridge with squarefree outer factors

Put
\[
 U_{u,\mathrm{sf}}(D)
 =\mathbf1_{Y_u<1}\sum_{m\ \mathrm{squarefree}}
                  \lambda_u(m)W(Nm/D).
 \tag{6}
\]
Then exactly
\[
\boxed{
 T_{u,\mathrm{sf}}=-U_{u,\mathrm{sf}}(D)
 +2\!\sum_{\substack{c,m\ \mathrm{squarefree}\\(c,m)=1,\ Nc\le z}}
 \mu_K(c)\lambda_u(cm)
 \sum_{\substack{Nt\le z\\Nt\,Nc>Y_u\\Nt>1}}
 \frac{k_{u,cm}(t)}{\log(Nt\,Nc)}W(Nt\,Nc\,Nm/D).
}
 \tag{7}
\]
Every sum is finite on the profile support. In particular, the inner
nonunit factor forces \(N(cm)\le CD/2\).

To prove (7), logarithmically differentiate the two truncated Möbius
factors, as in note 14:
\[
 (\log Nd)c_z(d)
 =-2\!\sum_{\substack{tc=d\\Nt,Nc\le z}}
          (\mu_K*\Lambda_K)(t)\mu_K(c).
 \tag{8}
\]
For a squarefree total ideal \(d m\), its factors \(t,c,m\) must be
squarefree and pairwise coprime. Fixing \(c,m\) and putting \(h=cm\),
the coefficient
\((\mu_K*\Lambda_K)(t)\lambda_u(t)\mathbf1_{(t,h)=1}\)
is precisely \(k_{u,h}(t)\) by (5). This proves all nonunit terms of
(7). The only divisor with \(\log Nd=0\) is \(d=1\), whose exact
contribution is (6) with a minus sign. No coprimality or squarefreeness
was imposed on the separate factors of the convolution in (5).

An equivalent expanded version of (7) has an inner sum over \(a,\ell\):
\[
 \sum_{\substack{N(a\ell)\le z\\N(a\ell c)>Y_u\\N\ell>1}}
 \frac{f_{u,h}(a)g_{u,h}(\ell)}{\log N(a\ell c)}
                      W(N(a\ell h)/D),\qquad h=cm.
 \tag{9}
\]
Here \(\ell\) runs over all prime powers. The expanded terms in (9)
may have nonsquarefree \(a\ell\); their complete coefficient cancels
by (5). Restricting (9) separately to primes coprime to \(a\) also
gives (7), but then the two-variable cumulative measures no longer have
the simple product form used below. One must choose a complete identity,
not retain the product integral while silently deleting its prime powers.

## 3. Principal density and exact centered Stieltjes formula

To avoid confusing a discrepancy function with the deletion ideal, set
\[
 \Psi_{u,h}(x)=\sum_{N\ell\le x}g_{u,h}(\ell),\quad
 \delta_u=\mathbf1_{\psi_u\ \mathrm{principal}},\quad
 \mathscr E_{u,h}(x)=\Psi_{u,h}(x)-\delta_u x.
 \tag{10}
\]
The added finite mask does not change the inducing primitive character
or the residue one of its logarithmic derivative at a principal pole.
The density coefficient is therefore \(\delta_u\), and is not the
free-character residue \(\kappa_u\). No prime ideal theorem is needed
to define (10) or prove the identities below.

For clarity, the mask changes the unmasked prime-power sum by exactly
\[
 \Psi_{u,h}(x)=\Psi_u(x)-\Delta_{u,h}(x),\qquad
 \Delta_{u,h}(x)=
 \sum_{p\mid h}\sum_{\substack{j\ge1\\(Np)^j\le x}}
                     \lambda_u(p)^j\log Np.
 \tag{11}
\]
Primes already deleted contribute zero. For \(x\ge2\), uniformly in
the row and the mask,
\[
 |\Delta_{u,h}(x)|\le\omega(h)\log x
                   \le (\log Nh/\log2)\log x.
 \tag{12}
\]
This elementary polylogarithmic bound concerns one prime-power
discrepancy. After multiplication by all Möbius factors and summation
it is not a moment bound for the resulting response.

For each fixed \(c,m,a\), let \(h=cm\), \(\eta_0=3/2\), and
\[
 \alpha=\max\{\eta_0,Y_u/(Na\,Nc)\},\quad
 \beta=z/Na,\quad
 F(x)=\frac{W(Na\,Nh\,x/D)}{\log(Na\,Nc\,x)}.
 \tag{13}
\]
When \(\alpha\ge\beta\), that summand is empty. Otherwise its
von Mangoldt sum in (9) is exactly
\(\int_{(\alpha,\beta]}F\,d\Psi_{u,h}\). With
\(\mathscr E_{u,h;\alpha}(x)
=\mathscr E_{u,h}(x)-\mathscr E_{u,h}(\alpha)\), it equals
\[
 \boxed{
 \delta_u\int_\alpha^\beta F(x)\,dx
 +F(\beta)\mathscr E_{u,h;\alpha}(\beta)
 -\int_\alpha^\beta\mathscr E_{u,h;\alpha}(x)F'(x)\,dx.
 }
 \tag{14}
\]
The lower endpoint has not been discarded: it is present in the centered
increment. Right-continuous values exclude an atom at \(\alpha\) and
include one at \(\beta\), exactly as required by \(N(a\ell c)>Y_u\)
and \(N(a\ell)\le z\). The artificial lower value \(3/2\) removes
no nonzero von Mangoldt atom and keeps the separated continuous terms
away from a logarithmic singularity.

For \(\mathcal DW(v)=vW'(v)\),
\[
 F'(x)=\frac1x\left\{
 \frac{\mathcal DW(Na\,Nh\,x/D)}{\log(Na\,Nc\,x)}
 -\frac{W(Na\,Nh\,x/D)}{\log^2(Na\,Nc\,x)}\right\}.
 \tag{15}
\]
Multiplying (14) by \(2\mu_K(c)\lambda_u(h)f_{u,h}(a)\),
summing all allowed outer factors, and adding (6) with a minus sign
recovers (7). Although \(\int\mathcal DW=-\int W\), zero integral
does not remove the separate von Mangoldt density term in (14).

## 4. Complete mixed discrepancy, both edges and low/low

Fix arbitrary \(U,V\ge1\), with equality assigned to the low side.
For each fixed \(u,h\), define
\[
 \mathcal L_b(R)=\sum_{Nn\le R}b(n)\log(R/Nn),\qquad
 M_{u,h;U}(s)=\sum_{U<Na\le s}f_{u,h}(a),
\]
\[
 \mathscr E_{u,h;V}(x)
 =\Psi_{u,h}(x)-\Psi_{u,h}(V)-\delta_u(x-V).
 \tag{16}
\]
For \(R\ge UV\), put
\[
 \mathcal C_{u,h;U,V}(R)
 =\int_U^{R/V}M_{u,h;U}(s)
                  \mathscr E_{u,h;V}(R/s)\,\frac{ds}{s},
\]
\[
 \mathcal D_{u,h;U,V}(R)
 =\sum_{U<Na\le R/V}f_{u,h}(a)
       \left\{R/Na-V-V\log(R/(VNa))\right\},
\]
\[
 \mathcal H_{u,h;U,V}(R)
 =\sum_{\substack{Na>U,\ N\ell>V\\N(a\ell)\le R}}
      f_{u,h}(a)g_{u,h}(\ell)\log(R/N(a\ell)).
 \tag{17}
\]
Set these three quantities to zero for \(R<UV\). Expanding the finite
atomic measures, with their continuous density, proves
\[
 \mathcal H_{u,h;U,V}(R)
 =\mathcal C_{u,h;U,V}(R)+\delta_u\mathcal D_{u,h;U,V}(R).
 \tag{18}
\]
Indeed, an atomic pair integrates over
\(Na\le s\le R/N\ell\) and gives \(\log(R/N(a\ell))\).
For the continuous part at fixed \(a\),
\[
 \int_{Na}^{R/V}(R/s-V)\,\frac{ds}{s}
 =R/Na-V-V\log(R/(VNa)).
\]
At cap equality these displayed weights vanish.

The full convolution Riesz sum is exactly
\[
\begin{split}
 \mathcal L_{k_{u,h}}(R)={}&
 \mathcal C_{u,h;U,V}(R)+\delta_u\mathcal D_{u,h;U,V}(R)\\
 &+\sum_{Na\le U}f_{u,h}(a)\mathcal L_{g_{u,h}}(R/Na)\\
 &+\sum_{N\ell\le V}g_{u,h}(\ell)\mathcal L_{f_{u,h}}(R/N\ell)\\
 &-\sum_{\substack{Na\le U,\ N\ell\le V\\N(a\ell)\le R}}
    f_{u,h}(a)g_{u,h}(\ell)\log(R/N(a\ell)).
\end{split}
 \tag{19}
\]
This is two-cutoff inclusion-exclusion. Its first edge is low/full,
its second is full/low, and the final correction subtracts their common
low/low contribution once. Thus both genuine low/high edges and the
low/low contribution remain. All three terms use the same mask \(h\)
and all their prime powers.

For recovery of the actual sharp adaptive selector, let
\[
 K_{u,h}(R)=\sum_{Nt\le R}k_{u,h}(t),\quad
 A_c=\max\{\eta_0,Y_u/Nc\},\quad B=z,\quad
 \varphi_{c,m}(R)=\frac{W(RNh/D)}{\log(RNc)}.
 \tag{20}
\]
If \(A_c<B\), finite partial summation twice gives
\[
\begin{split}
 \sum_{A_c<Nt\le B}k_{u,h}(t)\varphi_{c,m}(Nt)
 ={}&\left[K_{u,h}(R)\varphi_{c,m}(R)
 -\mathcal L_{k_{u,h}}(R)R\varphi'_{c,m}(R)\right]_{A_c}^{B}\\
 &+\int_{A_c}^{B}\mathcal L_{k_{u,h}}(R)
                         (R\varphi'_{c,m}(R))'\,dR.
\end{split}
 \tag{21}
\]
When \(A_c\ge B\), the contribution is zero, not the signed integral
with reversed endpoints. Substitution of (19) in **both the boundary
and integral terms** of (21), followed by the outer sum in (7), is a
complete mixed-discrepancy formula for \(T_{u,\mathrm{sf}}\).
Explicitly,
\[
 R\varphi'_{c,m}(R)
 =\frac{\mathcal DW(RNh/D)}{\log(RNc)}
  -\frac{W(RNh/D)}{\log^2(RNc)},
\]
\[
 (R\varphi'_{c,m}(R))'
 =\frac1R\left\{
 \frac{\mathcal D^2W(RNh/D)}{\log(RNc)}
 -\frac{2\mathcal DW(RNh/D)}{\log^2(RNc)}
 +\frac{2W(RNh/D)}{\log^3(RNc)}\right\}.
 \tag{22}
\]
Right-continuous cumulative sums in (21) include the upper cap and exclude
the lower cap. No endpoint, derivative, density or edge has been dropped.

The old sufficient criterion for an empty low/low piece was
\(UVz\le Y_u\). At the current cutoff,
\[
 UVz\ge z=\sqrt C D^{1/2}>D^{9/20}\ge Y_u
 \tag{23}
\]
for all sufficiently large \(D\). Hence that support argument cannot
discard low/low on any row here. This is a failure of the old sufficient
criterion; it is not a claim that every numerical choice of the profile
or arithmetic masks gives a nonzero low/low term.

## 5. Complete outer-divisor weights and surviving semiprimes

Regroup (7) by the squarefree outer product \(h=cm\). Since \(h\) is
squarefree, \(c\mid h\) determines \(m=h/c\) and enforces
\((c,m)=1\). For \(R>1\), define
\[
 J_{h;z,Y}(R)
 =\sum_{\substack{c\mid h\\Nc\le z\\RNc>Y}}
                         \frac{\mu_K(c)}{\log(RNc)}.
 \tag{24}
\]
Then
\[
 T_{u,\mathrm{sf}}=-U_{u,\mathrm{sf}}(D)
 +2\sum_{h\ \mathrm{squarefree}}\lambda_u(h)
       \sum_{1<Nt\le z}k_{u,h}(t)
                    W(Nt\,Nh/D)J_{h;z,Y_u}(Nt).
 \tag{25}
\]
All cutoff inequalities in (24) are retained, including equality at
\(Nc=z\) and strictness at \(RNc=Y\).

On the part \(Nh\le z\) that meets the profile, \(RNh\ge c_0D\)
implies \(R\ge c_0D/z\gg D^{1/2}>Y_u\). Thus for sufficiently large
\(D\) every divisor of \(h\) is admitted in (24), and
\[
 J_{h;z,Y_u}(R)=\sum_{c\mid h}\frac{\mu_K(c)}{\log R+\log Nc}
 =\int_0^\infty e^{-t\log R}
                  \prod_{p\mid h}(1-e^{-t\log Np})\,dt>0.
 \tag{26}
\]
For the unit \(h\), the integral is \(1/\log R\); its contribution
on this balanced part is empty once \(c_0D>z\). Positivity of (26)
does not give positivity of (25): the factor
\(k_{u,h}(t)=-\mu_K(t)\lambda_{u,h}(t)\log Nt\)
still has its Möbius sign and complex character value. Nor does it
control the remaining range \(Nh>z\), with the capped divisor weight.

The obstruction can be checked exactly on two distinct good primes
\(q,r\) with \(Nq,Nr\le z<N(qr)\) and
\(1\le Y_u<\min(Nq,Nr)\). In the original coefficient,
\[
 c_z(q)=c_z(r)=-2,\qquad c_z(qr)=2,\qquad
 -\sum_{d\mid qr,\ Nd>Y_u}c_z(d)=2.
 \tag{27}
\]
In (25), the only inner nonunit squarefree possibilities are
\((t,h)=(q,r),(r,q)\). Writing \(Q=\log Nq\), \(R_0=\log Nr\),
their coefficients after factoring out
\(\lambda_u(qr)W(N(qr)/D)\) are
\[
 2Q\left(\frac1Q-\frac1{Q+R_0}\right)
   =\frac{2R_0}{Q+R_0},\qquad
 \frac{2Q}{Q+R_0}.
 \tag{28}
\]
Their sum is \(+2\). There is no unit-cofactor cancellation. If
\(U\ge1\) and \(V<\min(Nq,Nr)\), every expanded von Mangoldt
term for this total product has \(a=1\) and \(\ell=q\) or \(r\).
Thus this common-total-product contribution lies entirely in the
low/high edge; the opposing edge, high/high and low/low supply zero for
this semiprime. The claim survives arbitrary character values and
deletion zeros because the total ideal is common throughout.

This is compatible with note 19, whose canceled nonunit packets have
different cutoff geometry, including \(Y>z\). It forbids transferring
that packet cancellation to (27). It is an obstruction to a proposed
local edge contraction, not a lower bound for the complete edge or
complete tail: other total products may compensate it.

## 6. Conductor and row-weight budgets

Let \(\mathfrak q_u\) be the primitive conductor. With
\[
 h_u^\sharp=\prod_{\substack{p\mid h\\p\nmid\mathfrak q_u E_u}}p,
 \qquad E_{u,h}=E_u h_u^\sharp,
 \tag{29}
\]
the new zero extension is exactly
\(\lambda_{u,h}(n)=\psi_u(n)\mathbf1_{(n,E_{u,h})=1}\), and
\[
 Q_{u,h}=Q_u,\quad L_{u,h}=L_uNh_u^\sharp\le L_uNh,
 \quad\tau(E_{u,h})\le\tau(E_u)\tau(h).
 \tag{30}
\]
On a nonzero outer summand, \(\lambda_u(h)\ne0\) forces
\((h,\mathfrak q_uE_u)=1\). Consequently \(h_u^\sharp=h\) and
\(L_{u,h}=L_uNh\) exactly on those summands. The weaker inequality
in (30) also covers the identically zero outer terms.
The inducing conductor is unchanged; the completion/deletion modulus
need not be. Deleting primes from a von Mangoldt sum has the elementary
cost (12), while deleting them from a Möbius sum changes its complete
coefficient sequence. One cannot use the former bound as a replacement
for an estimate for \(M_{u,h;U}\).

On any nonzero summand of (7), the profile and \(Nt\le z\) give
\[
 c_0D/z\le Nh\le CD/2.
 \tag{31}
\]
Thus the added outer mask ranges from norms of order \(D^{1/2}\) up
to order \(D\). On a significant row shell
\(Nu\le D^{2/5+\eta}\), with fixed \(0<\eta<1/20\), the existing
comparison \(L_u\ll Nu\) only supplies
\[
 Q_u\le L_u\ll D^{2/5+\eta},\qquad
 L_{u,h}\ll D^{7/5+\eta}.
 \tag{32}
\]
More locally, if \(L_u\asymp D^\ell\), \(Nh\asymp D^\beta\),
and \(Na\asymp D^\alpha\), then
\[
 0\le\ell\le2/5+\eta+o(1),\quad
 1/2+o(1)\le\beta\le1+o(1),\quad
 N\ell_{\rm VM}\le z/Na\ll D^{1/2-\alpha},\quad
 L_{u,h}\ll D^{\ell+\beta}.
 \tag{33}
\]
Here \(\ell_{\rm VM}\) denotes the von Mangoldt ideal, to distinguish
it from the conductor exponent \(\ell\). The support further requires
\(Na\,N\ell_{\rm VM}\,Nh\asymp D\). A fixed-character prime ideal
theorem is not a uniform estimate over (32)--(33).

For any attempted use of the existing free-character completion with
the new mask, assume explicitly \(\int W=0\) and put
\(S_{u,h}(X)=\sum_n\lambda_{u,h}(n)W(Nn/X)\). Its pointwise bound
has the parameters
\[
 |S_{u,h}(X)|\ll_{A,W}
 \tau(E_{u,h})\sqrt{Q_u}\,(L_{u,h}/X)^A.
 \tag{34}
\]
It follows by the same finite deletion inclusion-exclusion as the
manuscript. At an original small-divisor scale \(X=D/Nd\), \(Nd\le Y_u\),
its ratio is at most
\[
 L_{u,h}Nd/D\le Nh_u^\sharp D^{-11/20}.
 \tag{35}
\]
Arbitrary decay follows from (34) on a free sum only when an additional
bound, such as \(Nh_u^\sharp\le D^{11/20-\kappa}\), gives a fixed
margin. No such bound covers (31). More basically, neither the Möbius
sum \(M_{u,h;U}\) nor the prime-power sum \(\Psi_{u,h}\) in (19)
is a free-character sum, so (34) does not estimate them even in a
favorable numerical range. The fixed-cofactor representation has not
restored the original free \(m\)-sum.

The whole squarefree tail has the elementary uniform bound
\(T_{u,\mathrm{sf}}\ll_{\varepsilon,W}D^{1+\varepsilon}\): on
each total ideal, \(\sum_{d\mid n}|c_z(d)|\le\tau_3(n)\ll D^\varepsilon\),
and there are \(O(D)\) ideals on the annulus. Consequently the complete
Schwartz row weight makes \(Nu>D^{2/5+\eta}\) negligible to arbitrary
power, choosing its decay order afterwards. The unit exception (6)
requires \(L_u>D^{9/20}\), hence \(Nu\gg D^{9/20}\), and lies in
this negligible region. Formula (6) remains exact before that argument.
The selector in every formula still uses the original \(L_u\), not
the larger \(L_{u,h}\).

## 7. What a new estimate must prove; validation scope

For every required zero-integral derivative profile, the proposed bound
is still
\[
 D^{-1}\sum_{u\ne0}\Phi(Nu/D^{2/5})
                    |T_{u,\mathrm{sf}}|^2
          \ll_{\varepsilon,W}D^{4/5+\varepsilon}.
 \tag{36}
\]
Equations (7), (14) and (19)--(21) are exact representations of its
same response vector. They prove no contraction and add no power gain.
A successful mixed-discrepancy estimate must retain their signed
combination over \(c,m,a\), including both endpoints and all density,
edge and low/low terms, with the conductor/mask ranges above. Separately
bounding every selected semiprime piece would discard compensation
across total products that remains unproved.

The previously proved nonsquarefree response has energy
\(O(D^{19/24+\varepsilon})\). It therefore permits the equivalence of
(36) and the full target by the weighted triangle inequality. This
does not give an additive moment identity with an error of that size.

The accompanying
[checker](../../numerics/check_short_family_squarefree_discrepancy.py)
and [small record](../../numerics/short_family_squarefree_discrepancy_record_20261008.json)
have been run twice with byte-for-byte identical records. The direct
coefficient model uses 141 formal ideals of norm at most 1000 on four
distinct prime symbols with assigned norms \((2,3,5,7)\). These are a
formal multiplicative monoid, not a claimed realization as native good
ideals. Two exact rational specializations of the additive logarithms
check 1490 added-mask convolutions, 22680 projected-tail identities and
22680 outer-divisor regroupings. The cases include the strict adaptive
lower endpoint, the weak upper cap, and the unit boundary \(Y<1\)
versus \(Y=1\). The convolution enumeration includes 2388 terms at
nonsquarefree inner products before their cancellation.

An independent expansion compares the original truncated \(a b m\)
tuple directly with the full prime-power \(c m(a\ell)\) bridge in
2820 exact \(\mathbb Q[\zeta_6]\) checks, including original deletion
zeros and the added coprimality mask. A further 10416 term-level checks
retain common phases and deletion zeros, and six checks reproduce
the semiprime coefficient in (28). These finite rational substitutions
are tests of the algebraic proof, not a proof of a rational-function
identity from finitely many evaluations.

The same script imports the existing exact discrepancy checker and
reruns it on all 64 outer deletion supports, unioned with an original
deletion set, for trivial and nontrivial assigned phases with density
coefficients one and zero respectively. These are formal cases, not a
computation of native inducing characters. This gives
128 masked mixed-integral checks, 128 complete edge closures and 768
raw centered Stieltjes checks. Those comparisons use the existing exact
ring \(\mathbb Q[\zeta_6][\log p]\), with no numerical quadrature.
The proof of (21) is finite Stieltjes partial summation and is not
replaced by a numerical integration test.

These checks validate finite algebra and endpoint conventions. They
do not certify a prime ideal theorem, conductor-uniform Möbius
cancellation, Poisson, physical reciprocity, or (36). The script is
standard-library code, depends only on the earlier checker source,
and writes deterministic small JSON to stdout.

Sources: [note 14](14_SHORT_FAMILY_IDEAL_MIXED_DISCREPANCY_20261008.md),
[note 17](17_SHORT_FAMILY_SQUAREFREE_TAIL_REDUCTION_20261008.md),
[note 19](19_SHORT_FAMILY_EDGE_COMPENSATION_20261008.md), and the
[current manuscript](../short_family_reductions.tex). All deep analytic
inputs keep their previously declared imported status.
