# Euler-factor controls: exact flow, Laguerre witnesses and the size of \(\Lambda_{c,p}\)

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

First results of the [program](INITIAL_RESEARCH_PROGRAM_20261013.md).
Statements labelled Proposition have proofs here. The expansion of §4 is a
formal derivation confirmed numerically, not a theorem. Numbers come from
the [checker](../numerics/check_euler_factor_controls_claude_20261013.py)
and its [record](../numerics/EULER_FACTOR_CONTROLS_RECORD_20261013.json):
double precision, not interval certificates. No collision exclusion,
zero-free region or RH implication is claimed.

## Result and decision

1. **Exact flow (Proposition 1).** At every Newman time the control's
   transform is theta's transform plus two complex-shifted copies.
2. **Laguerre witnesses (Proposition 2).** One real point with
   \(\mathscr L_0(H^{c,p}_t;x_0)<0\) proves \(\Lambda_{c,p}>t\). Close to
   the last collision a witness always exists, at the real part of the
   colliding pair, so one-point evaluations can certify lower bounds
   arbitrarily close to it. In the computed cases witnesses exist at every
   sampled \(t\); far below the collision they can fail (§2).
3. **Table (§3).** In all twelve cases computed, the lowest off-line pair
   collides last among the three lowest pairs, near
   \(x^*\approx2\pi/\log p\). Its collision time \(T_0\) is a lower bound
   for \(\Lambda_{c,p}\) and equals it if every other pair collides
   earlier; the table writes \(\Lambda_{c,p}\) for \(T_0\). Throughout,
   \(T_0<t_m=4\log(1/c)/(\log p)^2<\delta^2/2\).
4. **Expansion (§4).** As \(p\to\infty\) at fixed \(c\),
   \[
   \Lambda_{c,p}=t_m-S_2\,t_m^2+O(t_m^3),\qquad
   S_2=\frac{\xi''(1/2)}{2\,\xi(1/2)}=0.0231049931\ldots,
   \]
   where \(S_2=\sum_{\gamma>0}\gamma^{-2}\) under RH. The ratio
   \((t_m-\Lambda_{c,p})/(S_2t_m^2)\) is 0.9997 at \(p=10007,\ c=\tfrac12\)
   and 1.0004 at \(p=10007,\ c=0.9\). The controls see theta, to first
   order, only through the curvature of \(\xi\) at the centre.
5. **Screening (§5).** Rigorously, every finite set of Euler factors is
   shared by a control with \(\Lambda>0\). Numerically,
   \(\Lambda_{1/2,p}>0.2\) for every prime \(p\le41\), while the lowest
   pair of \(\Phi_{1/2,43}\) collides at \(0.1951\).

**Decision.** Keep 19 as the portfolio's control screen. Next, certify
one witness with outward arithmetic (target: \(\Lambda_{1/2,41}>0.2\)).

## 1. Proposition 1: exact flow

With \(a=\tfrac12\log p\), the dilation lemma (review §1.4) gives, for all
\(t\ge0\) and complex \(x\),
\[
\boxed{H^{c,p}_t(x)=H_t(x)+\tfrac c2\,e^{ta^2}\bigl[e^{-iax}H_t(x+2ita)+e^{iax}H_t(x-2ita)\bigr].}
\tag{1.1}
\]
*Proof.* \(N_t[\Phi(\cdot\pm a)]\,(x)=e^{ta^2}e^{\mp iax}N_t[\Phi]\,(x\pm2ita)\).
\(\square\) Record N1 compares (1.1) with direct quadrature of the control
source at four points, including a complex \(x\); the largest relative
error is \(10^{-13}\).

The pure multiplier gives the scale. Under the backward heat flow,
\(1+c\cos ax\) evolves to \(1+ce^{ta^2}\cos ax\), and its zeros become real
at \(t_m=\log(1/c)/a^2\). Its Laguerre expression is
\(\mathscr L_0(1+C\cos ax)=Ca^2(C+\cos ax)\) with \(C=ce^{ta^2}\), which is
negative exactly where \(\cos ax<-C\) (check E3). For a product,
\(\mathscr L_0(Hm)=m^2\mathscr L_0(H)+H^2\mathscr L_0(m)\) (check E2).

## 2. Proposition 2: Laguerre witnesses

**Proposition 2.** If \(\mathscr L_0(H^{c,p}_t;x_0)<0\) for some real
\(x_0\), then \(t<\Lambda_{c,p}\).

*Proof.* \(H^{c,p}_t\) is a real entire function of order 1. For
\(t\ge\Lambda_{c,p}\) all its zeros are real (de Bruijn), so it belongs to
the Laguerre–Pólya class. Its Hadamard product then gives
\(-(\log H)''=\sum_k(x-x_k)^{-2}\ge0\), hence
\(\mathscr L_0=H^2\cdot(-(\log H)'')\ge0\) on \(\mathbb R\). \(\square\)

Near an off-line pair \(X\pm iy\), the pair contributes
\(2((x-X)^2-y^2)/((x-X)^2+y^2)^2\) to \(\mathscr L_0/H^2\), which is
\(-2/y^2\) at \(x=X\). Let \(S\) be the total contribution of all other
zeros at \(x=X\); it is positive when they are real, or farther from \(X\)
than their own imaginary parts. A witness exists at \(x_0=X\) whenever
\(2/y^2>S\). As the pair approaches its collision, \(y\to0\) while \(S\)
stays bounded, so the witness grows like \(-2/y^2\).

Witnesses need not exist far below the collision. For the weak control
\((p,c)=(2,0.05)\) at \(t=0\), the off-line zero is at \(9.065+10.642i\),
but \(\mathscr L_0>0\) at every point of a 1200-point grid on \((0,60]\);
at \(x=\pi/a\), \(\mathscr L_0/H^2=+0.0066\). This was found by the
verification pass and confirmed here; it is not in the record.

| \((p,c)\) | \(t/\Lambda\) | \(x_0=\operatorname{Re}z\) | \(\operatorname{Im}z\) | \(\mathscr L_0/H^2\) at \(x_0\) |
| --- | --- | --- | --- | --- |
| (2, 0.5) | 0 | 9.0647 | 3.7999 | \(-0.107\) |
| (2, 0.5) | 0.9 | 8.1156 | 1.0244 | \(-1.87\) |
| (2, 0.5) | 0.99 | 8.0227 | 0.3182 | \(-19.7\) |
| (101, 0.5) | 0 | 1.3614 | 0.5707 | \(-5.31\) |
| (101, 0.5) | 0.99 | 1.3574 | 0.0510 | \(-768\) |
| (10007, 0.9) | 0.99 | 0.6821 | 0.0100 | \(-2.0\cdot10^4\) |

At \(t=1.01\,\Lambda_{c,p}\) the normalized \(\mathscr L_0\) is positive at
all 1200 grid points on \((0,3x^*+10]\) in each case (record N3).

This makes certification cheap. One interval evaluation of
\(H,H_x,H_{xx}\) at one point proves \(\Lambda_{c,p}>t\), and the margin
grows as \(t\uparrow\Lambda_{c,p}\). For \((p,c)=(41,\tfrac12)\) and
\(t=0.2\), the pair has \(\operatorname{Im}z=0.0153\), and
\(\mathscr L_0/H^2=-8.6\cdot10^3\) at \(x_0=1.68413\) (record N4). Any
\(x_0\) within about \(0.01\) of that point is still a witness.

## 3. Table of \(\Lambda_{c,p}\)

Method: follow the \(k\)-th off-line zero from its exact position
\((2k+1)\pi/a+i\delta\) at \(t=0\), with adaptive steps in \(t\), until it
nearly reaches the axis. Then solve \(H=H_x=0\) by Newton in \((t,x)\); the
Jacobian is \(\begin{pmatrix}-H_{xx}&H_x\\-H_{xxx}&H_{xx}\end{pmatrix}\).
Quadrature is the trapezoid rule on \(\operatorname{Im}u=0.25\), stable
to 13 digits under grid refinement.

| \(p\) | \(c\) | \(\delta\) | \(t_m\) | \(\delta^2/2\) | \(\Lambda_{c,p}\) (lowest pair) | \(x^*\) | \(\Lambda/t_m\) | collisions of pairs \(k=1,2\) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 0.5 | 3.800 | 5.7708 | 7.220 | 5.04322 | 8.012 | 0.8739 | 3.069, 3.229 |
| 3 | 0.5 | 2.397 | 2.2972 | 2.874 | 2.17782 | 5.432 | 0.9480 | 2.119, 1.135 |
| 5 | 0.5 | 1.637 | 1.0704 | 1.339 | 1.04416 | 3.810 | 0.9755 | 1.0395, 1.0188 |
| 11 | 0.5 | 1.098 | 0.48220 | 0.6033 | 0.476849 | 2.591 | 0.9889 | 0.47646, 0.47542 |
| 41 | 0.5 | 0.709 | 0.201049 | 0.2515 | 0.200117 | 1.684 | 0.9954 | 0.200090, 0.200030 |
| 43 | 0.5 | 0.700 | 0.195989 | 0.2452 | 0.195103 | 1.663 | 0.9955 | 0.195079, 0.195023 |
| 101 | 0.5 | 0.571 | 0.130173 | 0.1629 | 0.129781 | 1.357 | 0.9970 | 0.129774, 0.129759 |
| 1009 | 0.5 | 0.381 | 0.057954 | 0.0725 | 0.0578767 | 0.907 | 0.99866 | 0.0578761, 0.0578748 |
| 10007 | 0.5 | 0.286 | 0.032679 | 0.0409 | 0.0326543 | 0.682 | 0.99925 | 0.0326542, 0.0326539 |
| 2 | 0.9 | 1.348 | 0.87718 | 0.908 | 0.857882 | 8.880 | 0.9780 | 0.6047, 0.7219 |
| 101 | 0.9 | 0.202 | 0.019787 | 0.0205 | 0.0197776 | 1.361 | 0.99954 | 0.0197774, 0.0197770 |
| 10007 | 0.9 | 0.101 | 0.0049673 | 0.00514 | 0.00496673 | 0.682 | 0.99989 | 0.00496673, 0.00496672 |

Observations, all numerical:

- The lowest pair (\(k=0\)) collides last of the three in every case. The
  higher pairs collide earlier, and not monotonically in \(k\): for
  \(p=3\), the \(k=2\) pair near \(x=28.6\), next to the first zero of
  \(\xi\), goes first. Pairs with \(k\ge3\) were not tracked; the heuristic
  that a pair's effective multiplier strength grows with height suggests
  they collide earlier still.
- \(x^*\to2\pi/\log p\): for \(p=10007\), \(x^*=0.6816\) against
  \(2\pi/\log p=0.6822\).
- \(\Lambda_{c,p}<t_m<\delta^2/2\) throughout. Under RH, de Bruijn's
  theorem gives only the last bound.
- The values for \((2,\tfrac12)\) and \((101,\tfrac12)\) agree with the
  estimates of the review's verification pass (5.04 and 0.1298).

## 4. The expansion \(\Lambda_{c,p}=t_m-S_2t_m^2+\cdots\)

*Derivation (formal).* Put \(A(z)=H_t(z)/H_t(0)=1+\tfrac12\kappa_tz^2+O(z^4)\)
with \(\kappa_t=H_t''(0)/H_t(0)\). Scale \(x=\xi/a\) and \(t=\tau/a^2\), and
write \(C=ce^{\tau}\). By (1.1) and the algebra of check E4,
\[
\frac{H^{c,p}_t(\xi/a)}{H_t(0)}=1+C\cos\xi+\varepsilon\,R(\xi,\tau)+O(a^{-4}),
\qquad\varepsilon=\frac{\kappa_t}{2a^2},
\]
\[
R(\xi,\tau)=\xi^2+C\bigl[(\xi^2-4\tau^2)\cos\xi+4\tau\xi\sin\xi\bigr].
\]
At \(\varepsilon=0\) there are double zeros at \(\xi=(2k+1)\pi\) when
\(C=1\), that is at \(\tau_0=\log(1/c)\). Put \(\xi=\pi+\eta\) and
\(C=1+\gamma\). The two equations become \(-\gamma+\eta^2/2+\varepsilon
R(\pi,\tau)=O(\varepsilon^2)\) and \(\eta=O(\varepsilon)\), so
\(\gamma=\varepsilon R(\pi,\tau_0)+O(\varepsilon^2)=4\varepsilon\tau_0^2+O(\varepsilon^2)\),
the same for every \(k\). Since \(\kappa_t=\kappa_0+O(t)\), this gives
\(\tau=\tau_0+2\kappa_0\tau_0^2/a^2+O(a^{-4})\). Dividing by \(a^2\),
\[
\Lambda_{c,p}=t_m+2\kappa_0t_m^2+\cdots=t_m-S_2t_m^2+\cdots,\qquad
S_2=-2\kappa_0=\frac{\xi''(1/2)}{2\xi(1/2)} .
\]
Unconditionally \(S_2=-\tfrac12\sum_\rho(\rho-\tfrac12)^{-2}\), which equals
\(\sum_{\gamma>0}\gamma^{-2}\) under RH. Quadrature gives
\(S_2=0.0231049931154\) (record N0, with \(8H_0(0)=\xi(1/2)=0.497120778188\)).

*What is assumed.* That the lowest pair determines \(\Lambda_{c,p}\), as in
§3, and that the remainders are uniform. A proof of the lower half,
\(\Lambda_{c,p}\ge t_m-S_2t_m^2-O(t_m^3)\), needs only Proposition 2 at
\(x_0=\pi/a\) and explicit Taylor bounds for \(H_t\) near 0. The upper half
needs every other pair to have collided, which uses information about all
zeros.

*Numerical confirmation.* \((t_m-\Lambda)/(S_2t_m^2)\) equals 0.946,
0.979, 0.990, 0.9957, 0.9982, 0.99884, 0.99948, 0.99971 for
\(c=\tfrac12\) and \(p=2,3,5,11,41,101,1009,10007\). For \(c=0.9\) and
\(p=2,101,10007\) it equals 1.085, 1.0017, 1.0004. The second-order term
changes sign between these two values of \(c\).

*Meaning.* To first order, a control sees theta only through \(S_2\), the
curvature of \(\xi\) at the centre. The multiplier sets the time scale.
The curvature of \(\xi\) speeds the collision: \(|H_t|\) grows away from
the real axis near \(x=0\), so the shifted copies in (1.1) act with more
than strength \(c\).

## 5. Screening consequences

- **Rigorous.** For every prime \(p\) and every \(0<c<1\),
  \(\Lambda_{c,p}>0\). The control satisfies the Euler factor, the
  \(q\)-adic self-similarity and the Hecke relation at every prime
  \(q\ne p\) ([18](../../18_rank_two_automorphic_lift/notes/1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md),
  Proposition 4). No argument that uses the Euler product at only finitely
  many primes, together with properties every control shares, can prove
  \(\Lambda\le0\).
- **Rigorous once certified.** Each witness of Proposition 2 proves a
  specific bound \(\Lambda_{c,p}>t\).
- **Numerical.** For \(c=\tfrac12\), \(\Lambda_{1/2,p}>0.2\) for every
  prime \(p\le41\); this needs only the lowest pair, so it is a lower
  bound. All fifteen primes up to 47 were computed:
  \(\Lambda_{1/2,41}\ge0.20012\), while the lowest pairs of
  \(\Phi_{1/2,43}\) and \(\Phi_{1/2,47}\) collide at 0.19510 and 0.18623.
  The best bound in the refereed literature, \(\Lambda\le0.2\), is due to
  Platt and Trudgian ([arXiv:2004.09765](https://arxiv.org/abs/2004.09765),
  Bull. LMS 53 (2021)), using Polymath's method with their verification of
  RH to height \(3\cdot10^{12}\). The sharper, not peer-reviewed claim
  \(\Lambda\le0.1787854\), pinned in the
  [Newman certificate audit](../../../newman_certificate_audit/README.md),
  is not used here; the same screen applies to it with every \(p\le47\).
  Any argument for such a bound must use, for each of these primes, some
  input that \(\Phi_{1/2,p}\) lacks: the Euler factor at \(p\), or, as in
  the existing proofs, direct evaluation of the genuine function at the low
  heights \(x^*\le8.1\) where these controls collide. Smaller \(c\) raises
  \(t_m\) and, by §4, \(\Lambda_{c,p}\) for large \(p\); it extends the
  list.
- **Where the screen bites.** The decisive collision is at low height,
  \(x^*\approx2\pi/\log p\). A method that checks low heights by direct
  evaluation of the genuine function sees these controls fail there.
  Large-height arguments are screened only by the higher pairs, whose
  collision times are smaller (task 4 of the program).

## 6. Checks

Run, from `numerics/`:

```sh
python3 -I check_euler_factor_controls_claude_20261013.py --output EULER_FACTOR_CONTROLS_RECORD_20261013.json
```

Standard library only; about 20 seconds.

- **Part E, exact.**
  - E1: roots of \(Q_p\) are off the critical circle and reciprocal.
  - E2: Laguerre product rule.
  - E3: the multiplier's Laguerre expression.
  - E4: algebra of the first-order expansion.
- **Part N, double precision.**
  - N0: \(S_2\) and \(\xi(1/2)\).
  - N1: the exact flow (1.1).
  - N2: the table, collision order and expansion ratios.
  - N3: witnesses below \(\Lambda\) and nonnegativity above.
  - N4: \(\Lambda_{1/2,p}\) for all primes \(p\le47\), and the witness for
    \(\Lambda_{1/2,41}>0.2\).
