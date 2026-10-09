# Continuation after the zero integral adaptive reduction

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Derivations and same-model reviews are internal checks, not independent
specialist validation or formal proof replay.

Based on commit 480581447dcd3e93c9c2f9c22a050d9c5100ff9d and the
working-tree [notes 8--10](10_SHORT_FAMILY_FACTORIZATION_CONTINUATION_20261008.md).
This is the next starting point for the short-family investigation.

## The revised target

The [profile and adaptive reduction](11_SHORT_FAMILY_MEAN_ZERO_ADAPTIVE_REDUCTION_20261008.md)
removes the principal correction from the new analytic target.
For every fixed smooth annular \(V\), choose
\[
 W=(1+t\partial_t)V,\qquad \int W(t)\,dt=0.
\tag{1}
\]
This is a sufficient detector class: \(\widehat W(s)=(1-s)\widehat V(s)\),
and the only common Mellin zero of all these profiles is \(s=1\).
The usual treatment at \(s=1\) remains separate.

Keep the exact Möbius convolution, including overlaps and nonsquarefree
products:
\[
 \begin{gathered}
 m_z=\mu_K\mathbf1_{Nn\le z},\quad c_z=m_z*m_z,\quad
 z=(CD)^{1/2},\quad \operatorname{supp}W\subset[c,C],\\
 \lambda_u(n)=\nu(n)\chi_n(u),\qquad
 S_u(X)=\sum_{(m,S)=1}\lambda_u(m)W(Nm/X),\\
 A_{u,W}(D)=-\sum_d c_z(d)\lambda_u(d)S_u(D/Nd).
 \end{gathered}
\tag{2}
\]
Let \(Q_u\) be the primitive conductor norm, \(E_u\) the extra
squarefree deletion ideal, and
\[
 L_u=Q_uNE_u\asymp_{\nu,S}N\operatorname{rad}_S(u),
 \quad Y_u=D^{1-\theta}/L_u,\quad 0<\theta<1.
\tag{3}
\]
Define the actual tail
\[
 T^{\rm ad}_{u,W}(D)
   =-\sum_{Nd>Y_u}c_z(d)\lambda_u(d)S_u(D/Nd).
\tag{4}
\]
The omitted small sector is empty when \(Y_u<1\), and otherwise
completion and the convergent radical-weight Euler product give
\[
 \frac1D\sum_{u\ne0}\Phi(Nu/H)
       |A_{u,W}(D)-T^{\rm ad}_{u,W}(D)|^2
          =O_N(D^{-N}),\qquad 1\le H\le D.
\tag{5}
\]
The complete original Schwartz row weight survives. No principal
rows are deleted: their zero frequency vanishes because of (1).

The next moment to prove is therefore
\[
 \boxed{\frac1D\sum_{u\ne0}\Phi(Nu/D^{4/5})
       |T^{\rm ad}_{u,W}(D)|^2
            \ll_{\varepsilon,W}D^{4/5+a+\varepsilon},
       \qquad 0\le a<1/12,}
\tag{6}
\]
for every profile (1), at one fixed \(\theta>0\).
This is equivalent to the same full moment for these profiles.
It remains unproved.

For a general profile the original correction is still necessary;
the optional identity in note 11 expresses it as
\(-\kappa_u D(\int W)M_z(u)^2\) together with the nonzero-frequency
tail. Equation (6) legitimately avoids this term by restricting
to a sufficient detector class, rather than discarding the term.

## Why the target is sufficient

The finite prime-mask extraction in note 1 works with signed and
complex profiles. If the moment in (6) holds, it gives the scalar
bound with exponent
\[
 b=\frac{1+a}{2}+\frac{5h}{12},\qquad h=4/5,
 \quad b=\frac56+\frac a2<\frac78.
\tag{7}
\]
For any possible zero \(\rho\ne1\), some profile (1) has
\(\widehat W(\rho)\ne0\). The inherited Mellin identity then gives
the stronger zero-free boundary, subject to its recorded source inputs.

There is also a norm recovery statement. Subject to the classical
fixed-character boundary \(A_{u,V}(t)=o(t)\), a sharp derivative-profile
moment with \(h+a<1\) implies the all-profile sharp moment with the same
exponents. The exact identity
\[
 A_{u,V}(D)=D\int_D^\infty A_{u,W}(t)\,\frac{dt}{t^2}
\]
and finite-row Minkowski prove this without a conductor-uniform
boundary estimate. It is not a claim to recover every Schwartz-weighted
all-row moment. Direct Mellin detection already makes (6) sufficient.

At the alternative row exponent \(h=8/9\), the same reduction leaves
the target \(a<1/108\) and gives
\(b=47/54+a/2<7/8\). No estimate at either exponent is proved here.

## What the new support buys

For \(d=ab>Y_u\), \(Na,Nb\le z\), exact support gives
\[
 Nm\ll D^\theta L_u,\qquad
 Na,Nb\gg D^{1/2-\theta}/L_u.
\tag{8}
\]
On a row \(u=\eta vr^6\), \(v\) sixth-power-free,
\[
 L_u\ll(Nu)^{1/6}(Nv)^{5/6}.
\]
The coherent inner rows \(u=r^6\), \(Nu\le D^{4/5}\), thus have
\[
 Y_u\gg D^{13/15-\theta},\quad
 Nm\ll D^{2/15+\theta},\quad
 Na,Nb\gg D^{11/30-\theta}.
\tag{9}
\]
Choosing, for example, a fixed \(0<\theta<11/30\) makes both
Möbius factors long on these rows. These are support statements.
For the complete Schwartz row family use the pointwise modulus
or dyadic row shells, not a global substitution \(Nu\le D^h\).

## The cancellation that a next argument must preserve

The [factor selection barrier](12_SHORT_FAMILY_FACTOR_SELECTION_BARRIER_20261008.md)
shows that zero integral does not make every remaining factor class
small. With \(\nu=1\), \(V\ge0\) nonzero and (1), the tail's actual
ordered prime-by-prime tuples \(a=p,b=q,p\ne q,m=1\) have coherent
normalized energy
\[
 \gg DH^{1/6}/(\log D)^4.
\tag{10}
\]
The proof uses an explicitly imported quantitative fixed-field prime
ideal theorem. This selected piece exceeds every useful budget by
more than a quarter power. It is not a lower bound for the full tail;
other factor classes must cancel it in any successful argument.

Grouping \(d=ab\) and applying Cauchy plus the imported generic
physical sextic sieve likewise retains a supplied upper-bound term
\(DH^{1/6}\), regardless of factor balance. The row-dependent threshold
in this grouped variable can be handled by a logarithmic maximal
partial-sum loss, but that does not improve the power.

A bounded next analytic task is to estimate the recombined \(m=1\)
amplitude together with the compensating \(m>1\) and composite-factor
terms, retaining the \(z\) cutoffs and \(Nd>Y_u\) selector before
squaring. An identity that groups these compensations may help;
estimating every prime/composite class separately cannot close (6).
The free-factor Poisson estimate supplies no corresponding transform
bound for the two remaining Möbius factors.

The original low-overlap transformed residual in note 4 and the
signed gcd identity in note 9 remain parallel exact formulations.
The adaptive selector cannot simply be inserted into their completed
row kernels.

## Evidence and open conclusion

The [scoped review](../../reviews/SHORT_FAMILY_MEAN_ZERO_REVIEW_20261008.md),
[standalone finite checker](../../numerics/check_short_family_mean_zero.py)
and [small record](../../numerics/short_family_mean_zero_record_20261008.json)
separate the new algebra and exponent checks from imported analysis.
The checks do not validate Poisson decay, the prime ideal theorem,
the generic sieve, or an asymptotic Möbius moment.

The continuation proves a sufficient zero-integral reduction,
a negligible adaptive small sector and a selected-factor obstruction.
The signed tail estimate, any stronger zero-free boundary and
descent to RH remain open.
