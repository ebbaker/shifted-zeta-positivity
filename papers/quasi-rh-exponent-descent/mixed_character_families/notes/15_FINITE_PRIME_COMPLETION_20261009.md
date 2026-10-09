# Finite prime completion of the selected signed ratio remainder

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. Same-model algebra checks are
internal validation, not independent specialist review or formal verification.

This continues equation (5) of mixed note 13. It gives an exact completion
of every small-prime state before estimating the selected signed remainder.
The crossing shell created by that completion is controlled with a uniform
positive power reserve when the complete prime mask has norm at most
\(U^{1/250}\). The completed stable-core correlation remains unproved.
The additional Mellin calculation shows why the finite-prime multiplier
itself cannot supply a fixed power saving.

## 1. Original data and a complete prime mask

Retain exactly
\[
 D=U^r,\quad Y=U^{1/2},\quad
 V_u=\mathbf1_{\mathcal C_+}(u)|S_u|^4|Q_J(u)|^2,
 \quad \sum_uV_u\ll_\varepsilon U^{1+\varepsilon}H^b,
\]
\[
 M_u=D^{-1/2}\sum_d\mu_F(d)\psi_u(d)A_0(Nd/D).
\]
All ideals are good, the profile and slots are the original source-compatible
ones, and \(\psi_u\) retains its physical zero extensions and fixed ray
factor. Let \(P\) be any row-independent squarefree good ideal. Its prime
divisors need not be norm-ordered. Assume \(NP\le U^\eta\).

For \(x>0\), put \(T_{Np}A(x)=A(Np\,x)\) and
\[
 \Delta_{P,u}A_0(x)
 =\prod_{p\mid P}(1-\psi_u(p)T_{Np})A_0(x)
 =\sum_{b\mid P}\mu_F(b)\psi_u(b)A_0(Nb\,x).
 \tag{1}
\]
Every contributing inverse ideal has a unique factorization
\(d=be\), with \(b\mid P\) and \((e,P)=1\). Therefore
\[
 M_u=D^{-1/2}\sum_{\substack{e\ \mathrm{squarefree}\\(e,P)=1}}
          \mu_F(e)\psi_u(e)\Delta_{P,u}A_0(Ne/D).
 \tag{2}
\]
This is an exact reindexing, including complex profiles. The transformed
profile has support in \([c/NP,C]\) if the original support is
\([c,C]\). It is row-dependent and is not an additional permitted source
profile. Every summand of (1), and not its union support alone, retains
the original physical annulus \(cD\le N(be)\le CD\).

## 2. The stable core and the controlled crossing shell

For a pair \(d=be,d'=b'e'\), define
\[
 f_0=ee'/(e,e')^2,\qquad
 f_P=bb'/(b,b')^2.
\]
Both are squarefree and coprime, and the original good inverse ratio is
\[
 f_{\mathrm{inv}}(d,d')=f_0f_P,
 \qquad 1\le Nf_P\le NP.
 \tag{3}
\]
The stable high-core form is the following real signed sum:
\[
 \mathcal R_P=D^{-1}\sum_u V_u
   \sum_{\substack{e,e'\ \mathrm{squarefree}\\(ee',P)=1\\Nf_0>Y}}
     \mu_F(e)\mu_F(e')\psi_u(e)\overline{\psi_u(e')}
     \Delta_{P,u}A_0(Ne/D)
     \overline{\Delta_{P,u}A_0(Ne'/D)}.
 \tag{4}
\]
Its reality follows by ordered-pair reversal. Since \(Nf_P\ge1\), all
four local states of every prime of \(P\) are allowed whenever
\(Nf_0>Y\). Thus expansion of (4) is precisely the part of the original
high-ratio form with \(Nf_0>Y\). The exact complementary crossing form is
\[
 \mathcal X_P=D^{-1}\sum_uV_u
 \sum_{\substack{d,d'\ \mathrm{squarefree}\\
                       Nf_0\le Y<Nf_0Nf_P}}
 \mu_F(d)\mu_F(d')\psi_u(d)\overline{\psi_u(d')}
 A_0(Nd/D)\overline{A_0(Nd'/D)},
 \tag{5}
\]
and
\[
 \boxed{F_{J,>1/2}=\mathcal R_P+\mathcal X_P.}
 \tag{6}
\]
The strict endpoint is unchanged: equality with \(Y\) belongs to the low
side, and every crossing term has \(Y<Nf_{\mathrm{inv}}\le YNP\).
The existing original-annulus absolute pair count, together with the
selected fourth mass, gives
\[
 |\mathcal X_P|
 \ll_\varepsilon U^{1+\varepsilon}H^b(YNP)^{1/2}
 \le U^{5/4+\eta/2+\varepsilon}H^b.
 \tag{7}
\]
No complete-row enlargement, scalar Möbius estimate or modified fourth
mass input is used in (7). It bounds the crossing shell without trying to
estimate the completed stable-core sum by separate absolute packets.

For the common saving \(c_*=1/540\), let
\(\gamma=dr-c_*-1/4\). Mixed note 9 proves throughout its operational
wedge that
\[
 \gamma\ge\gamma_*
 =\frac{140772625414022617}{64335535541550000000}
 =0.0021881006232257\ldots.
\]
Choosing \(\eta=1/250\) leaves the exact crossing-shell reserve
\[
 \gamma_*-\frac1{500}
 =\frac{12101554330922617}{64335535541550000000}
 =0.0001881006232257\ldots>0.
 \tag{8}
\]
Thus the target (5) in mixed note 13 follows if one proves
\[
 (\mathcal R_P)_+
 \ll_\varepsilon U^{1+dr-1/540+\varepsilon}H^b
 \tag{9}
\]
for any one prescribed complete mask \(P\) satisfying that norm budget.
Multiplying (9) by \(D\) recovers the normalization of note 13.
Equation (9) remains a new correlation obligation, not a consequence of
the completion. It includes cross terms between all divisors of \(P\).

For a different cap \(Y=U^\upsilon\), the same identity has crossing cost
\(U^{1+\upsilon/2+\eta/2+\varepsilon}H^b\). The mask budget is legal
by this particular argument only when
\(\upsilon/2+\eta/2<dr-c_*\). The new
[joint gcd/core reduction](14_SIGNED_HIGH_GCD_REDUCTION_20261009.md)
retains \(\mathrm Ng<cU^{1/125}\) and
\(\mathrm Nf>U^{2r-2/125}\). At that latter edge the elementary cap
cost alone is \(U^{1+r-1/125}\), which exceeds the target throughout
the working domain. Moreover, allowing both inverse columns to acquire
a prime of \(P\) can move their gcd across its new boundary. This
completion therefore remains an alternative presentation at the original
half-power edge; applying it to the new joint remainder needs a separately
controlled crossing shell for both restrictions.

## 3. The canceled-prime mask is retained locally

For one prime \(p\mid P\), fix \(e,e'\) prime to \(p\), and abbreviate
\(A=A_0(Ne/D)\), \(A_p=A_0(Np\,Ne/D)\), with primed versions for
\(e'\). Before multiplying by the remaining factors, its four states sum to
\[
 A\overline{A'}
 -\psi_u(p)A_p\overline{A'}
 -\overline{\psi_u(p)}A\overline{A'_p}
 +|\psi_u(p)|^2A_p\overline{A'_p}
 =(A-\psi_u(p)A_p)
       \overline{(A'-\psi_u(p)A'_p)}.
 \tag{10}
\]
The fourth term is the state where \(p\) divides both inverse columns.
Its factor \(|\psi_u(p)|^2\) is exactly the canceled physical gcd zero
mask. If the row is deleted at \(p\), the two one-sided terms and the
common-prime term vanish together. Removing the gcd mask would invalidate
(10). For the remaining gcd \(g_0=(e,e')\), multiplicativity likewise
retains \(|\psi_u(g_0)|^2\); neither mask has been discarded.

## 4. What a complete small-prime multiplier can and cannot do

Let \(\widehat A_0(s)=\int_0^\infty A_0(x)x^{s-1}\,dx\).
Finite Mellin inversion gives, with no contour move,
\[
 \Delta_{P,u}A_0(x)
 =\frac1{2\pi i}\int_{(\sigma)}\widehat A_0(s)x^{-s}
        E_{P,u}(s)\,ds,
 \quad E_{P,u}(s)=\prod_{p\mid P}(1-\psi_u(p)(Np)^{-s}).
 \tag{11}
\]
The Jacobian from the profile dilation is \((Nb)^{-s}\). The unweighted
identity \(\sum_{b\mid P}\mu_F(b)=0\) consequently supplies no cancellation
in (11). At a coherent phase \(\psi_u(p)=1\), the real-axis multiplier is
the nonzero Euler product \(\prod_{p\mid P}(1-(Np)^{-\sigma})\).
This is a multiplier observation, not a realization of a selected detector
bin or a lower bound for the selected fourth energy.

More generally, for every fixed \(\sigma>0\), the inherited fixed-field
prime ideal theorem and \(\log NP\le\eta\log U\) imply uniformly in
the row, height and allowed mask that
\[
 U^{-o(1)}\le |E_{P,u}(\sigma+it)|\le U^{o(1)}.
 \tag{12}
\]
For \(0<\sigma<1\), split its primes at \(T=\log U\). Partial summation
gives \(\sum_{Np\le T}(Np)^{-\sigma}
 \ll_\sigma T^{1-\sigma}/\log T\). Above \(T\), the number of prime
divisors is at most \(\eta\log U/\log T\), so their corresponding sum
is at most \(\eta\log U\,T^{-\sigma}/\log T\). The resulting bound is
\(o(\log U)\). The cases \(\sigma=1\) and \(\sigma>1\) are easier.
Finally use \(1-(Np)^{-\sigma}\le|1-\psi_u(p)(Np)^{-\sigma-it}|
\le1+(Np)^{-\sigma}\), treating finitely many small primes separately.
The zero convention \(\psi_u(p)=0\) gives factor one and causes no issue.

Thus the finite prime completion is useful only if it exposes an additional
correlation estimate in (9); its isolated Euler multiplier cannot guarantee
any fixed saving \(U^{-c}\). This does not rule out oscillatory cancellation
inside (11) or compensation between distinct stable cores.

## 5. A three-variable Euler diagnostic retaining every gcd state

There is an independent exact Dirichlet-series representation. In an
initial half-plane of absolute convergence, put
\[
 \mathscr D_u(s,t,z)=
 \sum_{\substack{g,a,b\ \mathrm{squarefree}\\\text{pairwise coprime}}}
 \frac{\mu_F(a)\mu_F(b)|\psi_u(g)|^2
               \psi_u(a)\overline{\psi_u(b)}}
 {(Ng)^{s+t}(Na)^{s+z}(Nb)^{t+z}}.
\]
Its exact Euler factor is
\[
 \boxed{\mathscr D_u(s,t,z)=
 \prod_{p\ \mathrm{good}}
 [1-\psi_u(p)(Np)^{-s-z}
   -\overline{\psi_u(p)}(Np)^{-t-z}
   +|\psi_u(p)|^2(Np)^{-s-t}].}
 \tag{13}
\]
For example, absolute convergence holds when the three real parts
\(\Re(s+z),\Re(t+z),\Re(s+t)\) exceed one. At \(z=0\), (13)
factors into the reciprocal of the two good-Euler-factor Hecke L-functions.
For other \(z\), their product has the exact collision correction
\[
 1+|\psi_u(p)|^2(Np)^{-s-t}
                     (1-(Np)^{-2z})/
       [(1-\psi_u(p)(Np)^{-s-z})
        (1-\overline{\psi_u(p)}(Np)^{-t-z})].
 \tag{14}
\]
Here (14) is the factor of the correction multiplying the two reciprocal
L-functions, not an extra summand in (13). It records the canceled gcd
state and shows explicitly why introducing a ratio cutoff changes the
uncut inverse square. Continuing (13), moving Perron contours, or averaging
the selected weight cannot be justified just by scalar reciprocal growth;
the moving selected correlation is still needed.

## 6 Completion compatible with the new joint remainder

The fixed-gcd estimate from note 14 also controls a different completion
boundary. This permits a prescribed finite-prime completion of its new
near-coprime remainder, without imposing a separate cutoff on the
\(P\)-free ratio core.

Retain
\[
 G_0=cU^{1/125},\qquad NP\le U^{\eta_1},\qquad
 \eta_1=\frac1{25000},\qquad K=\frac{G_0}{NP}.
 \tag{C1}
\]
Here \(P\) is squarefree, good and row-independent, with exactly the same
complete dilation operator \(\Delta_{P,u}\) as above. Let
\(g_0=(e,e')\) for the \(P\)-free columns, and define the real completed
form
\[
 \mathcal C_{J,P}=D^{-1}\sum_uV_u
 \sum_{\substack{e,e'\ \mathrm{squarefree}\\
                   (ee',P)=1\\N(e,e')<K}}
 \mu_F(e)\mu_F(e')\psi_u(e)\overline{\psi_u(e')}
 \Delta_{P,u}A_0(Ne/D)
       \overline{\Delta_{P,u}A_0(Ne'/D)}.
 \tag{C2}
\]
All original physical annuli remain in the individual divisor summands.
The transformed profile is not substituted into a source inverse bound.
There is no additional \(Nf_0\) restriction in (C2).

For \(d=be,d'=b'e'\), their actual common gcd is
\[
 g=g_Pg_0,\qquad g_P=(b,b'),\qquad Ng_P\le NP.
 \tag{C3}
\]
Thus \(Ng_0<K\) implies \(Ng<G_0\) for every prime state in the
completion. Original annular balance then automatically places each
nonzero expanded term above the original half-power edge and above the
new near-maximal edge \(Nf>U^{2r-2/125}\). This allows all absent,
one-sided and common-prime states to be completed before imposing any
source bound.

Let \(g^{(P)}\) denote the factor of a squarefree ideal \(g\) supported
outside \(P\). The remaining terms in the actual low-gcd form have
\[
 Ng<G_0,\qquad Ng^{(P)}\ge K.
 \tag{C4}
\]
These predicates depend only on the original gcd \(g\), not on its
cofactor partition. Their aggregate is therefore a union of whole
fixed-gcd forms from note 14:
\[
 \mathcal B_{J,P}=D^{-1}
 \sum_{\substack{g\ \mathrm{squarefree}\\
                   Ng<G_0\\Ng^{(P)}\ge K}}
 \sum_u V_u|\psi_u(g)|^2T_g(u).
 \tag{C5}
\]
The exact partition is
\[
 \boxed{\mathcal R_{J,\mathrm{near}}
             =\mathcal C_{J,P}+\mathcal B_{J,P}.}
 \tag{C6}
\]
Equality with \(K\) belongs to the boundary form, while equality with
\(G_0\) remains outside both forms, as in note 14's low-gcd target.

Since (C4) implies \(Ng\ge K\), note 14's original-profile fixed-gcd
bound and ideal counting yield, eventually when \(K\ge1\),
\[
 |\mathcal B_{J,P}|
 \ll_\varepsilon U^{1+\varepsilon}H^bD^dK^{-d}
 \ll_\varepsilon U^{1+dr-d(1/125-\eta_1)+\varepsilon}H^b.
 \tag{C7}
\]
This uses the shortened inverse estimate only inside each complete
\(T_g\), at the original annular profile. The row-dependent operator
\(\Delta_{P,u}\) in (C2) receives no unsupported source-profile estimate.
No elementary absolute ratio-shell bound is used in (C7).

The available uniform reserve is
\[
 d\left(\frac1{125}-\frac1{25000}\right)-\frac1{540}
 \ge \frac9{25}\frac{199}{25000}-\frac1{540}
 =\frac{17107}{16875000}
 =0.0010137481481481\ldots>\frac1{1000}.
 \tag{C8}
\]
All inherited source-buffer, profile, height and small analytic losses
must be allocated strictly inside this reserve, as for note 14's
underlying shortened inverse estimate.

If the source's preliminary buffer is already fixed and gives the literal
inverse exponent \(\kappa=d+\rho\), retain that power in the first bound
of (C7): its exponent becomes
\[
 1+dr-d(1/125-\eta_1)
            +\rho(r-1/125+\eta_1).
 \tag{C8a}
\]
For \(0\le\rho\le1/100000\), \(r\le73/100\), the remaining uniform
reserve is at least
\[
 \frac{17107}{16875000}
 -\frac1{100000}\left(\frac{73}{100}-\frac{199}{25000}\right)
 =\frac{67940623}{67500000000}
 =0.0010065277481481\ldots>\frac1{1000}.
 \tag{C8b}
\]
Remaining small losses and the final finite height order are chosen after
this literal buffer cost is paid. At an already fixed larger buffer one
must check the actual \(\rho\) against (C8a), rechoose the buffer if the
source permits it, or decline the local completed cut; it is not an
arbitrarily small loss merely because \(\rho\) is numerically small.

Consequently one may seek the completed arithmetic target
\[
 (\mathcal C_{J,P})_+
 \ll_\varepsilon U^{1+dr-1/540+\varepsilon}H^b
 \tag{C9}
\]
for any one prescribed complete mask satisfying (C1). The controlled
boundary in (C7), note 14's high-gcd removal and the old small-core bound
then imply equation (5) of note 13. The completed target (C9) remains
unproved. In particular, the \(P\)-free coprime sector \((e,e')=1\)
still survives, with all its selected cross terms.

The norm budget here is narrower than the original half-power completion:
\(1/25000\), rather than \(1/250\). The former makes a complete fixed-gcd
boundary affordable; it does not make the near-maximal elementary ratio
cap affordable. It is the joint gcd membership, together with the
source-compatible shorter inverse estimate, that distinguishes this
compatible completion from the old ratio-shell completion.


## 7 Scope of the finite checks

The companion standard-library [checker](../../numerics/check_mixed_finite_prime_completion.py) and its [record](../../numerics/mixed_finite_prime_completion_record_20261009.json) report 153,705 exact assertions.
It compares the original inverse
amplitude with (2), verifies (6) at strict cutoff equality in both native
orientations, and tests the local four-state identity with physical zeros
and complex profiles. It computes the exact reserve (8). Its formal phases
are not native reciprocity data or actual selected zero bins. It establishes
neither (9), a new mixed moment, nor any new zero-free boundary.
