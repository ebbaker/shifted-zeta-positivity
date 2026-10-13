# Elliptic insertion transport and its heat obstructions

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: `gpt-6-astra` (Codex); reasoning effort **ultra**, inherited
from the actual parent session configuration. This is an incremental
research derivation and bounded control, not a manuscript or an RH claim.

## Result and decision

The moving-period connection can be transported exactly through the physical
insertion. A symmetric pair of short periods then gives an entire,
heat-compatible nonlocal identity with explicit upper spectral shifts.
However, a single period used on the whole real line has a growing carrier
and cannot be heat integrated at positive time. The short-period repair
changes the observed source: its value at the origin is negative and it
introduces a cusp. These are concrete obstructions to using the auxiliary
channel as a positive density or an independently visible physical anchor.

All finite balanced angular jets are scalar derivative dictionaries, not
just the first jet. The full imaginary elliptic law still restricts the
integer preparation beyond that dictionary. This calculation does not turn
that restriction into a value-and-slope lower bound or a stationary sign.
The first bounded task is complete; continuation requires an inequality on
the **complete** nonlocal channel and its correction, or a multiplier that
cancels the artificial endpoint contribution with a paid residual.

## 1. Conventions and the exact inserted lattice law

Use the conventions of the [review seeds](ANGULAR_GLUING_AND_RIGIDITY_REVIEW_SEEDS_20261013.md):
\[
 F(u,z)=e^{u+\pi z^2/2}\Theta(e^{4u},e^{2u}z),\qquad
 M=\frac{(D^2-1)F}{16},\qquad D=\partial_u\big|_z.
\]
Here the angular coordinate is \(z\); the spectral coordinate below is
\(x\). The classical elliptic and inversion laws are
[DLMF 20.2.8](https://dlmf.nist.gov/20.2.E8) and
[DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32), respectively. They were
checked against the primary source on 13 October 2026. The following
transport is our explicit calculation in this convention.

There are two generators, with either sign allowed:
\[
\begin{array}{c|c|c|c}
&p(u)&\kappa&p'(u)\\\hline
\text{real period}&\pm e^{-2u}&\pi&-2p\\
\text{imaginary quasiperiod}&\pm i e^{2u}&-\pi&2p.
\end{array}
\]
Both have \(p''=4p\), and both obey
\[
 F(u,z+p)=e^qF(u,z),\qquad
 q=\kappa(pz+p^2/2).
\tag{1}
\]
Define \(B_\kappa=\partial_z-\kappa z\). Then the full inserted identity is
\[
 \boxed{
 e^{-q}M(u,z+p)
 =M(u,z)+\frac{-2p'B_\kappa F_u-p''B_\kappa F
                    +(p')^2B_\kappa^2F}{16}.}
\tag{2}
\]
All terms in (2) are evaluated at the unshifted \((u,z)\) on its right side.
There is no assumption of positivity. In particular,
\(B_\kappa^2=\partial_z^2-2\kappa z\partial_z+\kappa^2z^2-\kappa\);
the final scalar term must be retained.

For a derivation, let \(T_p f(u,z)=f(u,z+p(u))\). The derivative at fixed
shifted angular coordinate transports as
\[
 T_pD=(D-p'\partial_z)T_p,
 \qquad e^{-q}(D-p'\partial_z)e^q=D-p'B_\kappa,
\]
because \(q_u-p'q_z=\kappa p'z\). Consequently the normalized insertion
is \(((D-p'B_\kappa)^2-1)F/16\). Expanding gives (2), including the
\(-p''B_\kappa F\) connection term. This derivation differentiates the
moving period and the gauge together.

The symmetric translation removes precisely the terms odd in \(p\):
\[
 \mathcal A_p(u,z):=\frac12\sum_{\sigma=\pm1}
 e^{-\kappa(\sigma pz+p^2/2)}M(u,z+\sigma p)
 =M(u,z)+\frac{p^2}{4}B_\kappa^2F(u,z).
\tag{3}
\]
The cancellation in (3) is algebraic averaging, not an omitted derivative.

## 2. Why a full-line moving period cannot be integrated as proposed

Let \(h(u)=F(u,0)=e^u\Theta(e^{4u},0)\). Inversion gives \(h(-u)=h(u)\),
and the balanced angular equation proved in section 5 gives
\(F_{zz}(u,0)=\pi h'(u)\). Equation (2), or (3), at \(z=0\) becomes
\[
 N_a(u,0)=\Phi_e(u)+\frac\pi4e^{-4u}(h'-h),\qquad a=e^{-2u},
\tag{4a}
\]
\[
 N_b(u,0)=\Phi_e(u)-\frac\pi4e^{4u}(h'+h),\qquad b=i e^{2u}.
\tag{4b}
\]
The odd terms of (2) vanish here because \(F\) is even in \(z\).
As \(u\to+\infty\), \(h(u)\) equals \(e^u\) plus a superexponentially small remainder;
reflection supplies the other tail. Thus
\[
 N_a(u,0)\sim-\frac\pi2e^{-5u}\quad(u\to-\infty),\qquad
 N_b(u,0)\sim-\frac\pi2e^{5u}\quad(u\to+\infty).
\tag{5}
\]
The normalizer in (2) does not remove this carrier. The full-line integral
against \(e^{tu^2+ixu}\) is not absolutely convergent when
\(\operatorname{Re}t>0\), for any fixed complex \(x\). For real
\(t\ge0,x\in\mathbb R\), absolute convergence and the ordinary improper
integral both fail. At \(\operatorname{Re}t=0,z=0\), the real-period
normalized channel does converge if \(\operatorname{Im}x<-5\), and the
imaginary-period channel if \(\operatorname{Im}x>5\); this does not give the
physical real spectral channel. On \(\operatorname{Re}t<0\), Gaussian decay
does permit the normalized full-line channel. Analytic continuation or
subtraction across this boundary would be an additional operation requiring
its own ledger, not the entire heat lift already proved for \(M\).

## 3. An entire short-period identity, with its endpoint term

On \(u\ge0\), the real period is short and
\[
 f(u,z)=F(u,z)-e^{u+\pi z^2/2},\qquad
 J_t(x,z)=\int_0^\infty e^{tu^2+ixu}f(u,z)\,du.
\tag{6}
\]
The subtracted term is killed by \(D^2-1\) and by
\(B=\partial_z-\pi z\). Both \(f\) and every fixed derivative decay
superexponentially on this half-line, locally uniformly in \(z\).
Thus \(J\) is entire in \(t,x,z\).

For completeness, retain the unsymmetrized channel
\[
 L^+_t(x,z)=\frac12\int_0^\infty e^{tu^2+ixu}
 e^{-\pi(az+a^2/2)}M(u,z+a)\,du,
 \qquad K^+_t=\frac12\int_0^\infty e^{tu^2+ixu}M(u,z)\,du.
\]
Equation (2), followed by one integration by parts, gives
\[
\begin{aligned}
L^+_t-K^+_t={}&\frac18 B\big\{-f(0,z)
 +(1-ix)J_t(x+2i,z)+2it\,\partial_xJ_t(x+2i,z)\big\}\\
 &+\frac18B^2J_t(x+4i,z).
\end{aligned}
\tag{7}
\]
Indeed \(\int_0^\infty wa(f_u-f)du
=-f(0,z)+(1-ix)J_t(x+2i,z)+2itJ_{t,x}(x+2i,z)\).
This displays the endpoint that would be lost by integrating the moving
period as a constant. The upper endpoint is zero by the tail estimate below.

To obtain a full-line channel, use the symmetric real period on the
positive half-line and the symmetric imaginary period on the negative one:
\[
 \mathcal A(u,z)=
 \begin{cases}
 M(u,z)+e^{-4u}B_+^2F(u,z)/4,&u\ge0,\\
 M(u,z)-e^{4u}B_-^2F(u,z)/4,&u<0,
 \end{cases}
 \qquad B_\pm=\partial_z\mp\pi z.
\tag{8}
\]
Each line is exactly the average of normalized shifted \(M\)'s in (3).
The assignment at the single point \(u=0\) is immaterial for integration.
Inversion gives \(\mathcal A(-v,z)=\mathcal A(v,-iz)\) for \(v>0\).
The scalar \(u=0,z=0\) values agree; agreement for general \(z\) is not needed
and no differentiability at this splice is assumed.

Define
\[
 \mathscr A_t(x,z)=\frac12\int_{\mathbb R}e^{tu^2+ixu}\mathcal A(u,z)\,du.
\]
The exact nonlocal relation is
\[
 \boxed{\mathscr A_t(x,z)=K_t(x,z)+\frac18
 \left\{(B_w^2J_t)(x+4i,z)
       +(B_w^2J_t)(-x+4i,-iz)\right\},}
 \qquad B_w=\partial_w-\pi w.
\tag{9}
\]
The operator in each parenthesis acts on \(J\)'s own angular argument before
evaluation; it is not a derivative in the displayed composite \(z\).
The odd connection and endpoint terms in (7) cancel under the exact
\(\pm a\) averaging, leaving (9). All channels in (9) are entire in
\((t,x,z)\in\mathbb C^3\), and each heat integral satisfies
\(\partial_t=-\partial_x^2\). The shifts \(x+4i\) and \(-x+4i\) are
evaluated by the defining half-line integrals, where they introduce
\(e^{-4u}\); no approximation on a small unshifted spectral disk is used.

## 4. Complete tail and projection ledger

Here is one explicit majorant, adequate for any compact rectangle. Write
\(s=e^{2u}\), suppose \(|z|\le Z\), and take \(u\ge U\ge0\) with
\(s\ge4Z\). For every nonzero integer \(n\),
\[
 -\pi n^2s^2+2\pi|n|sZ\le-\frac\pi2n^2s^2.
\]
For a theta summand, its logarithmic \(u\)-derivatives satisfy
\[
 |\ell_u|\le1+4\pi n^2s^2+4\pi|n|sZ,\qquad
 |\ell_{uu}|\le16\pi n^2s^2+8\pi|n|sZ.
\]
Set
\[
 C_M(Z)=\frac{(1+4\pi+4\pi Z)^2+16\pi+8\pi Z+1}{16},\quad
 C_N(Z)=C_M(Z)+\pi+3\pi^2+2\pi^2Z.
\]
The inserted summand is bounded by \(C_M n^4s^4\) times the exponential.
The entire real-period correction in (2) is bounded by
\((\pi+3\pi^2+2\pi^2Z)n^4s^4\) times the exponential. The zero mode
contributes zero to both. Since
\[
 \sum_{n\ge1}n^4e^{-qn^2}\le
 \frac{e^{-q}}{1-16e^{-3q}},\qquad q\ge\pi/2,
\]
both the symmetric and unsymmetric normalized short-period fields obey
\[
 |\mathcal A(u,z)|\le
 C_*e^{9|u|-(\pi/2)e^{4|u|}},\qquad
 C_*:=\frac{2C_N(Z)e^{\pi Z^2/2}}{1-16e^{-3\pi/2}}
\tag{10}
\]
for \(|u|\ge U\), using reflection on the negative half. The symmetric
field permits a smaller constant, but that is unnecessary here. In the
unsymmetric case (10) applies on its chosen short half-line, not on the
divergent opposite tail of section 2.

For \(|t|\le T\), \(|\operatorname{Im}x|\le X\), additionally require
\[
 A_U:=2\pi e^{4U}-2TU-9-X>0,\qquad 8\pi e^{4U}\ge2T.
\]
The complete two-sided tail of the transform with its factor \(1/2\) is at
most
\[
 \boxed{\frac{C_*}{A_U}
 \exp\{TU^2+(9+X)U-(\pi/2)e^{4U}\}.}
\tag{11}
\]
To prove this, the exponent's derivative is at most \(-A_U\) on
\([U,\infty)\). Extra fixed derivatives introduce polynomial factors and
admit the same superexponential domination, establishing the asserted
entireness and differentiation under each integral. No claim of a
numerically optimized enclosure is made. The record evaluates (11) on
\(|t|\le1, |\operatorname{Re}x|\le20, |\operatorname{Im}x|\le1,
|z|\le1\), with \(U=1\), as a floating diagnostic.

Projection remains essential. At \(z=0\), let \(v=|u|\). Equations (4) and
(8) give
\[
 \mathcal A(u,0)=\Phi_e(u)+C(v),\qquad
 C(v)=\frac\pi4e^{-4v}(h'(v)-h(v))
 =-2\pi^2e^v\sum_{n\ge1}n^2e^{-\pi n^2e^{4v}}.
\tag{12}
\]
Thus
\[
 \boxed{\mathscr A_t(x,0)=H_t(x)
 -2\pi^2\int_0^\infty e^{tu^2+u}\cos(xu)
       \sum_{n\ge1}n^2e^{-\pi n^2e^{4u}}\,du.}
\tag{13}
\]
The physical slope is obtained by differentiating **both** terms. The
cosine transform of the positive summand in (13) has no established sign
at a stationary point of \(H\). Consequently a bound on \(\mathscr A\)
alone is not a bound on \((H,H_x)\).

The inserted shifted field itself is not positive:
\[
 \mathcal A(0,0)=\sum_{n\ge1}
 \{2\pi^2n^2(n^2-1)-3\pi n^2\}e^{-\pi n^2}<-\frac1{10}.
\tag{14}
\]
An elementary certificate suffices. Using \(3<\pi<22/7\), \(\pi^2<10\),
\(e<3\), and \(e^3>\sum_{k=0}^8 3^k/k!>20\), the \(n=1\) term is less
than \(-1/9\). The remaining terms are bounded above by
\[
 \sum_{n\ge2}\frac{20n^4}{20^{n^2}}
 \le\frac{1/500}{1-81/(16\cdot20^5)}.
\]
Their sum with \(-1/9\) is less than \(-1/10\); the checker verifies these
rational inequalities exactly. This is a source sign at one explicitly
shifted point, not a stationary theta-transform sign.

The splice also has a precise cusp at \(z=0\):
\[
 C'(0+)=\frac\pi4(h''(0)+4h(0))
 =\frac\pi4\{16\Phi_e(0)+5h(0)\}>0.
\tag{15}
\]
Here \(h'(0)=\Phi_e'(0)=0\). Hence \(\mathcal A(u,0)\) is continuous
but not differentiable at zero, and its derivative jumps by \(2C'(0+)\).
For fixed real \(t\), ordinary half-line integration by parts gives
\[
 \mathscr A_t(x,0)=-\frac{C'(0+)}{x^2}+O_t(x^{-4})
 \quad(x\to+\infty).
\tag{16}
\]
The physical transform has no such splice term. The apparent large-height
visibility of this auxiliary observable is therefore also present in its
subtracted correction. It cannot be transferred to \(H\) for free.

## 5. The whole finite angular hierarchy is scalar

Termwise theta heat, \(\Theta_{yy}=4\pi\Theta_r\), and the balanced gauge
give the particularly simple equation
\[
 F_u=\pi^{-1}F_{zz}-\pi z^2F.
\tag{17}
\]
It can also be verified on each summand directly: the first angular
derivative terms cancel. Since the operator on the right is independent of
\(u\), \(M\) obeys the same equation. Write
\[
 [z^{2m}]F=Q_m(D)h,\quad [z^{2m}]M=Q_m(D)\Phi_e,
\]
where
\[
 Q_{-1}=0,\quad Q_0=1,\qquad
 Q_{m+1}=\frac{\pi DQ_m+\pi^2Q_{m-1}}{(2m+2)(2m+1)}.
\tag{18}
\]
In particular
\[
 Q_1=\frac\pi2D,\quad Q_2=\frac{\pi^2}{24}(D^2+2),\quad
 Q_3=\frac{\pi^3}{720}(D^3+14D),\quad
 Q_4=\frac{\pi^4}{40320}(D^4+44D^2+60).
\]
An independent finite-sum formula is
\[
 Q_m(D)=\pi^m\sum_{k=0}^m
 \frac{\prod_{j=0}^{k-1}(D-1-4j)}{2^{m-k}(m-k)!(2k)!}.
\tag{19}
\]
It follows by expanding the gauge and applying repeated scale derivatives
to the theta summands. The rational checker verifies (18) against (19),
including parity, through \(m=12\).

Full-line integration by parts has no endpoint for the original smooth
source \(M\), giving
\[
 [z^{2m}]K_t=Q_m\big(i(2t\partial_x-x)\big)H_t,\qquad
 K_{t,zz}=\pi i(2t\partial_x-x)K_t+\pi^2z^2K_t.
\tag{20}
\]
The operator powers in (20) must retain the noncommutation of \(x\) and
\(\partial_x\). These formulas do **not** say that every jet vanishes at a
collision. At an ordinary double zero with \(t>0\),
\[
 [z^4]K_t=-\frac{\pi^2t^2}{6}H_{xx},
\]
which is nonzero. Its nonvanishing comes from the physical second derivative,
not a new independent source anchor. At \(t=0\), equation (20) instead
factors as \(K_0(x,z)=H_0(x)U_x(z)\), where
\(U_x''=(\pi^2z^2-i\pi x)U_x\), \(U_x(0)=1,U_x'(0)=0\).

There is nevertheless a distinction between local derivative transport and
global lattice preparation. Replacing the integer coefficients by any symmetric
normally convergent preparation \(c_n=c_{-n}\) leaves (17)--(19) and the real period intact.
The imaginary quasiperiod forces \(c_n=c_{n+1}\), as the defect calculation
in the review seeds shows. The checker changes \(c_{\pm1}\) to \(1.1\): the
balanced PDE remains true while the imaginary law fails. This control is
not claimed to retain modular reflection or the genuine physical source.
The full elliptic constraint is thus additional to the local PDE, but all
finite angular jets of the actual prepared source still carry only the
scalar dictionary (20). No signed bound follows from source uniqueness.

## 6. Reproduction and the next gate

Run from the repository root:

```sh
python3 papers/investigations-2/active/02_angular_jacobi_gluing/numerics/check_elliptic_transport.py
```

The [script](../numerics/check_elliptic_transport.py) uses only the Python
standard library. Its [small record](../numerics/ELLIPTIC_TRANSPORT_RECORD_20261013.json)
contains the exact polynomial and origin-sign controls, 18 direct
fixed-angular-derivative theta checks at \(u=-1/2,0,1/2\) for both periods,
and the coefficient-perturbation control. The maximum normalized transport
residual in the recorded run is about \(1.28\times10^{-15}\). Those direct
theta checks use \(|n|\le24\) and floating arithmetic: they diagnose signs
and missing connection terms, but are not interval enclosures. The analytic
tails (10)--(11) supply the domain justification, not a claimed certified
floating margin. No heat integral or stationary branch was numerically
enclosed in this task.

The next useful question is whether the exact relation (9), with the full
projection correction (13), admits a signed multiplier or an observation
inequality that pays its endpoint and angular continuation. Passing that
gate would justify transfer to direction 03 or 06. Repeating the scalar
jets, treating (14) as positive, or using the auxiliary \(x^{-2}\) term as
physical visibility fails the gate. If no such complete inequality is
specified, the next bounded identity task should move to the rank-two
addition program rather than extending this computation automatically.
