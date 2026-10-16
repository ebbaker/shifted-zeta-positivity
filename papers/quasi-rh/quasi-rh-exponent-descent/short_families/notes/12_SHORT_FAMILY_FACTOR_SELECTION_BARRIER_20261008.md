# Factor selection still loses a power on zero integral profiles

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Derivations and same-model reviews are internal checks, not independent
specialist validation or formal proof replay.

Based on commit 480581447dcd3e93c9c2f9c22a050d9c5100ff9d and the
working-tree [adaptive reduction in note 11](11_SHORT_FAMILY_MEAN_ZERO_ADAPTIVE_REDUCTION_20261008.md).

## What the new reduction does and does not remove

Note 11 removes the actual small-product sector for
\(W=(1+t\partial_t)V\). On rows with small combined modulus
\(L_u=Q_uNE_u\), this removes the large prime columns in the
\(d=1\) free-factor sum together with their compensating composite
columns. Consequently the original prime-column projection is not
a lower bound for the new tail.

A different obstruction occurs inside the new tail itself. In the
legal specialization \(\nu=1\), select its ordered factor tuples
\[
 a=p,\quad b=q,\quad p\ne q,\quad Np,Nq\le z=(CD)^{1/2},
 \quad m=1.
\tag{1}
\]
Here \(p,q\) are good prime ideals. These are actual factorization
coefficients: \(\mu_K(p)\mu_K(q)=1\), with no extra aligning weight.
For a nonzero nonnegative smooth \(V\) supported inside \((c,C)\),
put \(W=(1+t\partial_t)V\). The normalized energy of (1) is
\[
 \boxed{\mathfrak E_{\rm pp}(D,H)
       \gg_{V,\Phi} \frac{D H^{1/6}}{(\log D)^4}.}
\tag{2}
\]
This holds for \(H=D^h\), \(0<h<1\), and sufficiently large \(D\).
It prevents a method that gives the useful moment budget separately
to every such factor class. It is not a lower bound for the full tail,
the full \(m=1\) piece, or the actual Möbius moment. Cross terms with
the other factor classes can cancel (1).

The specialization \(\nu=1\) is part of the permitted family. The
argument does not assert the same asymptotic for every nontrivial
fixed twist; an argument using extra properties of such a twist
would need its own analysis.

## The explicit prime-by-prime asymptotic

We use the quantitative fixed-field prime ideal theorem
\[
 \pi_K(x)=\operatorname{Li}(x)
       +O_K(x\exp(-c_K\sqrt{\log x}))
\tag{3}
\]
for sufficiently large \(x\). A possible fixed exceptional real zero
can be absorbed in this asymptotic after increasing the threshold.
One primary source for the necessary effective input is
[Das, Kadiri and Ng, Corollary 1.4](https://arxiv.org/html/2508.09480v1),
specialized to the trivial extension of \(K=\mathbb Q(\sqrt{-3})\);
subtracting prime powers and partial summation gives (3).
This is an imported analytic theorem, used for this obstruction only.
Ordinary \(\pi_K(x)\sim x/\log x\), without a quantitative remainder,
would not justify the cancellation of the leading logarithmic term.

The condition \(NpNq/D\in[c,C]\), together with \(Np,Nq\le z\),
forces each prime norm into a fixed annulus of size \(D^{1/2}\).
Apply (3) twice, allowing the sharp upper limits at \(z\).
After \(Np=D^{1/2}x\), \(Nq=D^{1/2}y\), the prime densities satisfy
\[
 \frac1{\log(D^{1/2}x)\log(D^{1/2}y)}
     =\frac4{(\log D)^2}+O_{c,C}((\log D)^{-3}).
\]
Thus the ordered sum, before excluding the diagonal, is
\[
 \begin{split}
 \sum_{\substack{Np,Nq\le z\\p,q\notin S}}
 W(NpNq/D)
 &=\frac{4D}{(\log D)^2}
   \int_0^{\sqrt C}\int_0^{\sqrt C}W(xy)\,dx\,dy
       +O_{V,c,C}(D/(\log D)^3)\\
 &=\frac{4D}{(\log D)^2}
   \int_c^C W(t)\log(C/t)\,dt
       +O_{V,c,C}(D/(\log D)^3).
 \end{split}
\tag{4}
\]
The second identity is the product-variable Jacobian, not a Mellin
cancellation assumption. Since \(W=(tV)'\), integration by parts gives
\[
 \int_c^C W(t)\log(C/t)\,dt=\int_c^C V(t)\,dt>0.
\tag{5}
\]
The diagonal \(p=q\) contributes \(O_V(D^{1/2}/\log D)\), which is
smaller than the error in (4). The finite omitted primes are also
irrelevant for large \(D\).

Now take coherent rows \(u=r^6\) with \(Nu\le H\). Their number is
\(\asymp_K H^{1/6}\), after identifying the six unit multiples of \(r\).
All supported primes have norm \(\gg D^{1/2}\), whereas
\(Nr\le H^{1/6}=D^{h/6}\), so none divides \(r\). Therefore
\(\lambda_{r^6}(p)=\lambda_{r^6}(q)=1\) when \(\nu=1\).
The row selector is also identically satisfied: every nonzero
summand has \(NpNq\ge cD>Y_u=D^{1-\theta}/L_u\), since \(L_u\ge1\)
and \(\theta>0\) is fixed.

The selected tail amplitude on every such row is consequently
\[
 -\sum_{\substack{p\ne q\\Np,Nq\le z}}W(NpNq/D)
 =-\frac{4D}{(\log D)^2}\int V(t)\,dt
       +O_V(D/(\log D)^3).
\tag{6}
\]
The minus sign is the original convolution sign. Its square is
positive. Since the unchanged \(\Phi\) is at least one on the inner
norm ball, dividing the squared amplitude by \(D\) and counting these
rows proves (2).

In the useful extraction range
\[
 a+\frac{5h}{6}<\frac34,
 \qquad h+a<\frac34+\frac h6,
\tag{7}
\]
the power in (2) exceeds the proposed \(D^{h+a+\varepsilon}\)
budget by more than \(1/4\), before arbitrarily small epsilons.
Logarithmic decay cannot close this gap.

## Why grouping and a generic sieve do not supply the missing gain

There is also an upper-bound diagnostic using the imported generic
physical sextic sieve from
[note 6](6_SHORT_FAMILY_SEXTIC_SIEVE_BARRIER_20261008.md).
It has operator factor
\[
 \mathcal L(H,X)=H+XH^{1/6}+H^{5/6}X^{1/3}
                              +H^{1/3}X^{5/6}
\tag{8}
\]
up to an epsilon power, for sixth-power-free ideal columns of size
\(X\) and the full physical rows. The transfer, multiplicities,
unit splitting and column masks have the status recorded there.

Group \(d=ab\), so the coefficients are \(c_z(d)\), and let
\(Nd\asymp X\), \(Nm\asymp Z\), \(XZ\asymp D\).
Because \(c_z\) is cube-free-supported and
\(|c_z(d)|\le\tau(d)\), these grouped columns are within that theorem
and have squared coefficient norm \(O_\varepsilon(XD^\varepsilon)\).
The free-factor coefficients have squared norm \(O(Z)\).

For each fixed \(m\), its profile \(W(NdNm/D)\) has uniformly bounded
seminorms after this dyadic restriction. Cauchy in \(m\), followed by
(8) on \(d\), supplies only
\[
 \mathfrak E_{X,Z}
 \ll_\varepsilon D^\varepsilon Z\,\mathcal L(H,X)
 \asymp D^\varepsilon\frac D X
      [H+XH^{1/6}+H^{5/6}X^{1/3}+H^{1/3}X^{5/6}].
\tag{9}
\]
The normalization is essential: before division by \(D\), Cauchy
pays \(Z\), summing the \(m\)-indexed sieve bounds pays another
\(Z\), and the squared \(d\)-coefficient norm pays \(X\).

The selector \(Nd>Y_u\) in this particular grouping can be covered
by a maximal partial-sum version of (8), with only logarithmic
loss. Order the finitely many \(d\)'s by norm, fixing ties. Every
threshold tail is the union of at most \(O(\log(2X))\) intervals from
a fixed binary partition. Cauchy for that union and the sieve on
each fixed interval give \(O(\log^2(2X))\) times (8), because the
intervals at each level partition the coefficient squared norm.
This justifies (9) for the row-dependent threshold in the grouped
\(d\) variable. It does not justify inserting an arbitrary selector
inside earlier completed row kernels, nor every regrouping of the
three factors.

For \(H=D^h\), \(X=D^x\), the four supplied exponents in (9) are
\[
 1+h-x,\quad 1+\frac h6,\quad
 1+\frac{5h}{6}-\frac{2x}{3},\quad
 1+\frac h3-\frac x6.
\tag{10}
\]
The second exponent survives every choice of balance:
\[
 \frac D X\cdot XH^{1/6}=DH^{1/6}.
\tag{11}
\]
At \(h=4/5\) it is \(17/15\), while a useful target is below
\(53/60\); at \(h=8/9\) the corresponding exponents are \(31/27\)
and \(97/108\). The gap is more than \(1/4\) in each case.
This describes the supplied generic upper bound, not an actual
lower bound for a Möbius block. No change of dyadic balance in
this argument proves the desired gain.

In particular the \(m=1\) block has \(X\asymp D\) and remains in
the tail. Its grouped coefficient squared norm has the full
power \(D\): besides the divisor bound from above, choose a subinterval
where \(|W|\) is bounded below. The prime ideal theorem applied to
that product region gives \(\gg D/(\log D)^2\) distinct balanced
semiprimes, with \(c_z(pq)=2\).
The zero integral of \(W\) provides no power saving in that
coefficient norm.

## Consequence for the next estimate

The new analytic task is the recombined adaptive tail in note 11,
for every derivative profile. Its short free factor on coherent rows
is useful structural information, but \(m=1\) is allowed and the
two Möbius factors still require cancellation across prime and
composite factor classes. A triangle inequality separating (1)
from the other classes cannot give the useful budget to both.

A further Poisson summation over \(a\) or \(b\) would encounter
Möbius coefficients rather than a free character sum; the free-factor
completion in note 11 supplies no transform estimate for them.
A new signed bilinear estimate, or a carefully recombined identity
retaining those coefficients, is still needed.

The [review](../../reviews/SHORT_FAMILY_MEAN_ZERO_REVIEW_20261008.md)
and [finite checker](../../numerics/check_short_family_mean_zero.py)
audit the integral identities and exponent arithmetic. They do not
certify the asymptotic prime theorem or the sought moment.
