# An affordable prime-pair sector and an additive signed finishing form

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: a proved near-pair bound and an additive prime-power comparison
using the already imported quadratic large sieve. The separated signed
prime-pair estimate and the improved family strip remain open. Internal
checks are not independent specialist validation or formal proof checks.

This continues [Note 2](2_QUADRATIC_MOMENT_STRENGTH_AND_BARRIER_20261008.md)
with the actual prepared coefficients. For the useful example \(h=7/5\),
all distinct prime pairs at distance at most \(X^{3/8}\) fit a strictly
smaller budget by elementary counting. The cross terms between primes
and higher powers also fit additively using the inherited sieve, without
assuming the desired moment. The exact remaining obligation is a real
signed sum over separated primes, with comparison reserve \(1/40\).
This is a controlled nonzero sector and a sharper checkpoint, not a
solution of the needed dispersion estimate.

## 1. Actual coefficients and a generic norm already available

Let \(1<h<2\), \(Q=X^{2-h}\), \(T=1+h/2\), and
\[
 S_a=\sum_n\Lambda(n)\chi_a(n)\ell(n/X),\quad
 P_a=\sum_{p\ \mathrm{odd}}c_p\chi_a(p),\quad
 c_p=\log p\,\ell(p/X),\quad R_a=S_a-P_a,
 \quad \mathcal W_h=\sum_{a\le Q}^{*}a^{-1/2}|S_a|^2.
\]
The star retains odd squarefree rows, including the principal row \(a=1\).
Every Jacobi deletion zero is kept. The fixed annular support of \(\ell\)
puts the prime columns in \([A_\ell X,C_\ell X]\), with
\(|c_p|\ll_\ell\log(2X)\).

Elementary prime-power counting from Note 2 gives
\[
 E_R:=\sum_{a\le Q}^{*}a^{-1/2}|R_a|^2
       \ll_\ell X\sqrt Q\log^4(2X)
       =X^{2-h/2+o(1)}.                              \tag{1}
\]
On a dyadic block \(a\asymp A\le Q<X\), the already imported
squarefree quadratic large sieve gives
\[
 \sum_{a\asymp A}^{*}a^{-1/2}|P_a|^2
       \ll_\varepsilon X^{2+\varepsilon}A^{-1/2}.
\]
The constants absorb the fixed support scale and prime coefficient
norm \(\sum_p|c_p|^2\ll X\log^2(2X)\). Summing the geometric block
bounds, including the block starting at one, yields the available
\[
 E_P:=\sum_{a\le Q}^{*}a^{-1/2}|P_a|^2
       \ll_{h,\ell,\varepsilon}X^{2+\varepsilon}.     \tag{2}
\]
This is a deduction from the same source theorem as Note 1, not an
additional family hypothesis. It gives no improved strip.

## 2. An additive comparison with all prime-power cross terms paid

Expanding the exact whole row squares and applying weighted Cauchy gives
\[
 \mathcal W_h=E_P+E_R+2\Re\sum_{a\le Q}^{*}a^{-1/2}P_a\overline{R_a},
 \qquad
 |\mathcal W_h-E_P|\le E_R+2\sqrt{E_PE_R}
        \ll_{h,\ell,\varepsilon}X^{2-h/4+\varepsilon}. \tag{3}
\]
No prime-power cross term has been set to zero, and (2), rather than an
unproved target for \(E_P\), pays the cross term. This strengthens the
previous norm equivalence to an additive power-small comparison whenever
\[
 h>4/3,\qquad T-(2-h/4)=3h/4-1>0.               \tag{4}
\]
At \(h=7/5\), the error exponent is \(33/20\), leaving reserve
\(1/20\) below \(T=17/10\). For \(1<h\le4/3\), this additive
argument has no positive reserve; Note 2's weighted norm equivalence
still applies. The threshold in (4) limits this particular generic
comparison, not the validity of the full target.

## 3. A nonzero near-pair sector that needs no dispersion theorem

Keep the exact kernel
\[
 J_Q(k)=\sum_{a\le Q}^{*}a^{-1/2}(k/a),\qquad
 W_Q=\sum_{a\le Q}^{*}a^{-1/2}\ll\sqrt Q.
\]
For every \(k\), including nonunits, \(|J_Q(k)|\le W_Q\).
The exact diagonal is
\[
 D_Q=\sum_p|c_p|^2\sum_{\substack{a\le Q\ \mathrm{odd\ sf}\\p\nmid a}}a^{-1/2}
       \ll_\ell X\sqrt Q\log^2(2X).               \tag{5}
\]
For sufficiently large \(X\), all these supported primes exceed \(Q\)
and the inner sum equals \(W_Q\); the masked expression (5) is valid
at every finite scale.

For any \(1\le\Delta\le X\), define the genuine signed sector
\[
 N_Q(X;\Delta)=\sum_{\substack{p,q\ \mathrm{odd}\ p\ne q\\|p-q|\le\Delta}}
            c_p\overline{c_q}J_Q(pq).
\]
There are \(O_\ell(X(\Delta+1))\) ordered integer pairs in the fixed
window at these distances. The prime pairs are a subset. Thus, with no
prime-density input and no conjecture about character cancellation,
\[
 \boxed{|N_Q(X;\Delta)|\ll_\ell
          X(\Delta+1)\sqrt Q\log^2(2X).}          \tag{6}
\]
This does not call the near-pair restriction positive; the modulus is
paid using its actual cardinality. Shared factors with a row only
decrease the bound. It treats distinct pairs, not merely the diagonal.

Fix \(0<\delta<h-1\) and take \(\Delta=X^{h-1-\delta}\). Then
\[
 |N_Q(X;\Delta)|\ll_{h,\ell,\varepsilon}
              X^{T-\delta+\varepsilon}.          \tag{7}
\]
The exponent \(h-1\) is the endpoint of this entrywise cardinality
budget. For a gap cutoff \(X^d\), it has exponent \(2-h/2+d\)
and fits the target exactly when \(d\le h-1\). This is a limitation
of the bound (6), not a lower bound for the actual near-pair sum.

## 4. The exact separated signed residual

Define the remaining paired form
\[
 F_{h,\delta}(X)=
 \sum_{\substack{p,q\ \mathrm{odd}\\|p-q|>X^{h-1-\delta}}}
       c_p\overline{c_q}J_{X^{2-h}}(pq).           \tag{8}
\]
It is real by reversal of \(p,q\), and need not be nonnegative.
The principal row and the profile signs remain in the kernel and
coefficients. For \(4/3<h<2\), (3), (5), and (7) give the additive
identity with controlled error
\[
 \boxed{\mathcal W_h(X)=F_{h,\delta}(X)
                  +O_{h,\ell,\delta,\varepsilon}
                    (X^{T-\rho+\varepsilon}),\qquad
 \rho=\min\{h-1,\ 3h/4-1,\ \delta\}>0.}       \tag{9}
\]
Therefore the full moment target \(\mathcal W_h\ll X^{T+\varepsilon}\)
is equivalent, with the usual every-epsilon convention, to the
**one-sided** bound \(F_{h,\delta}(X)\ll X^{T+\varepsilon}\).
Positivity of \(\mathcal W_h\) also gives the new useful lower bound
\(F_{h,\delta}\ge-O(X^{T-\rho+\varepsilon})\); it gives no upper
bound of the desired size. The squarefree-removal transform in Note 2
continues to apply unchanged to this surviving kernel, including its
\((d,pq)=1\) mask.

The concrete checkpoint is
\[
 h=7/5,\quad\delta=1/40,\quad Q=X^{3/5},\quad
 \Delta=X^{3/8},\quad T=17/10,\quad\rho=1/40,
\]
\[
 \mathcal W_{7/5}=F_{7/5,1/40}+O_\varepsilon(X^{67/40+\varepsilon}).
 \tag{10}
\]
The diagonal/prime-power squared norm exponent is \(13/10\); the
prime-power cross error is \(33/20\); the near-pair error is \(67/40\).
These are paid independently of the requested \(17/10\) estimate.

The entrywise absolute obstruction also survives the new restriction.
Note 2's Proposition 2 proves that the full off-diagonal absolute sum is
\(\gg_\ell X^2\). The absolute near-pair sum itself obeys (6), and at
the choice in (7) it is \(O(X^{T-\delta+\varepsilon})=o(X^2)\), on
taking \(\varepsilon<2-T+\delta\). Subtraction therefore proves
\[
 \sum_{\substack{p,q\ \mathrm{odd}\\|p-q|>X^{h-1-\delta}}}
       |c_pc_qJ_{X^{2-h}}(pq)|\gg_\ell X^2.        \tag{11}
\]
Thus removing the affordable sector does not repair an entrywise
absolute-value approach to the exact surviving form. This corollary
uses the already imported prime number theorem behind Note 2's lower
bound; it introduces no new uniform character prime theorem.

## 5. Priority after this checkpoint

The affordable near-pair sector removes a concrete part of the actual
form, and (10) specifies exactly how much error a transform argument
may spend. It does not control separated primes, improve the old
\(15/8\) hybrid bottleneck, or remove the principal response. Note 2's
\(7/40\) deficit under the favorable individual exponent \(B=7/8\)
remains. Its simultaneous fixed odd-quadratic-family implication also
remains. The comparative review's decision to defer this branch is
therefore unchanged, but it now has a precise bounded resumption task:
prove a signed estimate for (8) in a stated separated-prime/conductor
regime, pay its complement and compare the resulting saving to \(7/40\).
A successful transform must retain the actual profile signs and the
squarefree-removal zero mask; an entrywise estimate for the whole form
still has the obstruction proved in Note 2.

The [new checker](../../numerics/check_short_quadratic_checkpoint.py)
checks full finite signed decompositions with rational coefficient and
positive row-weight substitutes, including masks, both sides of the
strict separation threshold, and all prime-power cross terms. These
substitutes verify algebra; they are not a numerical evaluation of the
analytic detector. The [record](../../numerics/short_quadratic_checkpoint_record_20261009.json)
checks the exact rational reserves in (4), (7), and (10). No unbounded
moment or new zero-free result is certified. The sole non-elementary
inputs are the already imported Heath-Brown quadratic large sieve in
Note 1 and the prime number theorem in Note 2 for (11); no new external
result is invoked.

Two fresh runs reproduce the record byte for byte: 42,049 exact
assertions across both programs, including 36 signed pair partitions.
There are nonzero near-pair and prime-power cross terms in the finite
cases, so the partition checks do not rely on those terms vanishing.
