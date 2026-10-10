# Paired contour bounds and uniform product remainders

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is not exposed to this session
and is not inferred. Derivations and separate-agent audits are internal
LLM work, not independent mathematical validation.


This completes the analytic contour checkpoint proposed in the
[strategy note](8_RH_STRATEGY_WITH_QUASI_RH_AND_NEXT_ANALYTIC_TARGET_20261010.md):
the complete paired source has a matched contour representation, explicit
growth bounds and a product-index remainder uniform on one shrinking-time
sector and its physical complex disks. A cutoff of order x log x suffices
for any prescribed polynomial error after the natural exponential is
removed. These are magnitude and approximation bounds, not a signed
Fourier estimate or nonvanishing theorem. The [Mellin continuation](10_MATCHED_MELLIN_BESSEL_TRANSFORM_AND_RAW_CHANNEL_OBSTRUCTION_20261010.md)
explains why full modular cancellation must precede this truncation.

## 1. Definitions and the intrinsic source strip

Use the complete source

\[
 \Phi(z)=\sum_{n\ge1}
 (2\pi^2n^4e^{9z}-3\pi n^2e^{5z})e^{-\pi n^2e^{4z}},
 \qquad m_t(z)=e^{tz^2}\Phi(z).
\]

The series and its derivatives converge locally uniformly in
\(\mathcal S=\{z:|\Im z|<\pi/8\}\), because
\(\Re(e^{4z})=e^{4\Re z}\cos(4\Im z)>0\). Jacobi gluing from Note 8,
extended by the identity theorem in this connected strip, gives
\(\Phi(-z)=\Phi(z)\). Real coefficients give
\(\Phi(\bar z)=\overline{\Phi(z)}\). Both properties hold for \(m_t\)
when \(t\) is real.

For integer \(j\ge0\), define the holomorphic source kernel

\[
 J_{j,t}(w)=\int_{\mathbb R}r^2(r^2-w^2)^j
                  m_t(w+r)m_t(w-r)\,dr.                 \tag{1}
\]

The integration variable \(r\) is real. This defines an even holomorphic
function on \(\mathcal S\), with
\(J_{j,t}(\bar w)=\overline{J_{j,t}(w)}\). In particular
\(J_{j,t}(iy)\) is real for real \(|y|<\pi/8\).

For each closed substrip, the theta tail gives an integrable majorant
locally uniform in \(w\), also after each fixed derivative or polynomial
insertion. One direct way to see the contour-end decay is to use Jacobi
reflection separately on the two arguments. Their largest absolute real
part is

\[
 \max(|s+r|,|s-r|)=|s|+|r|.
\]

At least one factor therefore has double-exponential decay at
\(|s|+|r|\). The other has at most Gaussian and exponential growth before
its own decay is used. Consequently the vertical sides at
\(\Re w=\pm R\) tend to zero faster than every fixed exponential as
\(R\to\infty\), uniformly on any fixed closed substrip and compact
time/frequency sets. This proves the holomorphy assertion and licenses
the contour shift below. No extension of the theta source across
\(|\Im w|=\pi/8\) is asserted.

## 2. Exact full-pair shift and its matched endpoint

With the conventions of Note 7,

\[
 \mathscr L_j(H_t;z)
  =(H_t^{(j+1)}(z))^2-H_t^{(j)}(z)H_t^{(j+2)}(z)
  =\int_{\mathbb R}e^{2izs}J_{j,t}(s)\,ds.
\]

For any \(0\le a<\pi/8\) and complex physical frequency \(z\), the
exact contour identity is

\[
 \boxed{\mathscr L_j(H_t;z)
  =e^{-2az}\int_{\mathbb R}e^{2izs}J_{j,t}(s+ia)\,ds.}   \tag{2}
\]

The integrals converge for each fixed \(t,z,a\). Formula (2) contains
the complete Jacobi-glued source; it has no finite approximation input.

For real \(x\), the half-line version is

\[
 \int_0^\infty e^{2ixs}J_{j,t}(s)\,ds
 =e^{-2ax}\int_0^\infty e^{2ixs}J_{j,t}(s+ia)\,ds
   +i\int_0^a e^{-2xy}J_{j,t}(iy)\,dy.                 \tag{3}
\]

The last term is purely imaginary, so that

\[
 \mathscr L_j(H_t;x)
 =2e^{-2ax}\Re\int_0^\infty e^{2ixs}J_{j,t}(s+ia)\,ds. \tag{4}
\]

The cancellation in (4) uses evenness of the complete kernel. A fixed
raw theta term, divisor channel, or product-index summand does not
automatically have this symmetry. Its vertical endpoint must be kept
until the modularly matched sum is recombined. For complex \(z\), use
the full-line equation (2), not a real-part version of (4).

## 3. Explicit weighted source norm

Set

\[
 c=\cos(4a),\quad U=\tfrac14\log(1/c),\quad
 \beta=\tfrac58,\quad b=4\pi-\tfrac{39}4,
\]
\[
 C_{\rm low}=\tfrac32+\frac3e+\frac8{e^2},\qquad
 C_0=4\pi^2+6\pi.
\]

Assume

\[
 0\le t\le\tfrac1{20},\qquad tU\le\tfrac38.           \tag{5}
\]

For any \(0\le B<\beta\), put \(\gamma=\beta-B>0\) and

\[
 D_B=2e^{\gamma\pi/8}
 \left(C_{\rm low}+\frac{C_0e^{-\pi}\gamma}{b-\beta}\right).
\]

Then, for every integer \(k\ge0\),

\[
 \boxed{
 I_{k,B}(t,a):=\int_{\mathbb R}|u+ia|^k e^{B|u|}
                  |m_t(u+ia)|\,du
 \le D_B k!\gamma^{-k-1}c^{-5/2}.}                     \tag{6}
\]

All constants are explicit and independent of \(t,a\) subject to (5).
The proof is elementary and retains every theta term.

For \(q>0\), the unimodal function \(v^p e^{-qv^2}\) satisfies

\[
 \sum_{n\ge1}n^p e^{-qn^2}
 \le\tfrac12\Gamma((p+1)/2)q^{-(p+1)/2}
       +\left(\frac{p}{2eq}\right)^{p/2}.              \tag{7}
\]

This follows, for example, by integrating the fact that each interval
superlevel set contains at most its length plus one positive integers.
For \(0<q\le\pi\), the last term in (7) is at most
\(\sqrt\pi(p/(2e))^{p/2}q^{-(p+1)/2}\). Applying this with
\(p=4,2\) and \(q=\pi c e^{4u}\), for \(0\le u\le U\), gives

\[
 |\Phi(u+ia)|\le C_{\rm low}c^{-5/2}e^{-u}.             \tag{8}
\]

Since \(tu\le3/8\), the heat factor and the physical imaginary-frequency
weight make the remaining exponential at most \(e^{-\gamma u}\).
Using \(|u+ia|\le u+a\), the integral over this low range is at most

\[
 C_{\rm low}c^{-5/2}
 \int_0^\infty(u+a)^k e^{-\gamma u}\,du
 \le C_{\rm low}c^{-5/2}e^{\gamma a}k!\gamma^{-k-1}.    \tag{9}
\]

For \(u=U+v\), \(v\ge0\), the parameter \(q\) is at least \(\pi\).
The elementary bounds \(n^4\le16^{n-1}\) and
\(n^2-1\ge3(n-1)\) give

\[
 \sum_{n\ge1}n^p e^{-qn^2}\le2e^{-q},\qquad p=2,4,
\]

because \(16e^{-3\pi}<1/2\). Consequently

\[
 |\Phi(U+v+ia)|
 \le C_0 c^{-9/4}e^{9v-\pi e^{4v}}.                   \tag{10}
\]

Multiplying by the heat and \(e^{Bu}\) weights, and using
\(e^{4v}\ge1+4v+8v^2\), gives

\[
 e^{B(U+v)}|m_t(U+v+ia)|
 \le C_0c^{-5/2}e^{-\pi}e^{-\gamma U}
       e^{-(b-B)v-(8\pi-1/20)v^2}.                    \tag{11}
\]

Here \(c^{1/4}e^{tU^2+BU}\le e^{-\gamma U}\), by (5),
and \(9+2tU\le39/4\). Finally

\[
 e^{-\gamma U}(U+a+v)^k
 \le k!\gamma^{-k}e^{\gamma(a+v)}
\]

and \(b-B-\gamma=b-\beta>0\). Dropping the negative quadratic
in (11), the tail integral is at most

\[
 C_0c^{-5/2}e^{-\pi}
 \frac{k!\gamma^{-k}e^{\gamma a}}{b-\beta}.             \tag{12}
\]

The modulus of the source on the shifted line is even in \(u\),
because \(m_t(-u+ia)=\overline{m_t(u+ia)}\). Adding twice (9) and
(12), and using \(a\le\pi/8\), proves (6).

For orientation only, ordinary floating-point evaluation gives
\(D_0\approx11.2613107867\) and
\(D_{1/20}\approx10.8981906364\). The exact displayed expressions,
not these decimal approximations, define the theorem's constants.

## 4. Explicit complete-pair bound

For \(|\Im z|\le B\), equations (2) and (6) imply

\[
 \boxed{
 |\mathscr L_j(H_t;z)|
 \le \frac{D_B^2 j!(j+2)!}{4\gamma^{2j+4}}
       c^{-5}e^{-2a\Re z}.}                           \tag{13}
\]

The factor in (13) can be better than separately bounding the two
derivative products. To verify it, insert (1) into (2) and put
\(u=s+r\), \(v=s-r\), whose real Jacobian is two. Then

\[
 r^2=\tfrac14(u-v)^2,\qquad
 r^2-(s+ia)^2=-(u+ia)(v+ia).
\]

After taking absolute values, the integral is at most

\[
 \tfrac18e^{-2a\Re z}\iint (u-v)^2
 |u+ia|^j|v+ia|^j W_B(u)W_B(v)\,du\,dv,
\]

where \(W_B(u)=e^{B|u|}|m_t(u+ia)|\) is even. The cross term
\(uv\) therefore integrates to zero. Since \(u^2\le|u+ia|^2\), the
remaining expression is at most

\[
 \tfrac14e^{-2a\Re z}I_{j,B}I_{j+2,B}.
\]

This proves (13), retaining the signed insertion for \(J_1\) before
the absolute bound is applied. It does not mistake source positivity
for Fourier positivity.

For completeness, the same shift of the full Fourier integral
\(2H_t(z)=\int m_t(u)e^{izu}\,du\) gives

\[
 |H_t^{(k)}(z)|
 \le\tfrac12D_B k!\gamma^{-k-1}c^{-5/2}e^{-a\Re z}.   \tag{14}
\]

## 5. A closed shrinking-time sector with its entire small disk paid

Use exactly the sector of the project manuscript:

\[
 0<t\le1/20,\quad1\le\kappa\le3/2,\quad
 L=\kappa/t,\quad x=4\pi e^L.
\]

Choose

\[
 a_x=\pi/8-4\pi/x,\qquad c_x=\cos(4a_x)=\sin(16\pi/x).
\]

The sector has \(x>32\), so \(0<a_x<\pi/8\) and
\(0<16\pi/x<\pi/2\). The elementary concavity bound
\(\sin y\ge2y/\pi\), \(0\le y\le\pi/2\), yields

\[
 c_x\ge32/x\ge4\pi/x,
 \qquad U_x\le\tfrac14\log(x/(4\pi))=L/4,
 \qquad tU_x\le\kappa/4\le3/8.                       \tag{15}
\]

Thus (5) holds uniformly as \(t\downarrow0\). For real \(x\), (13)
becomes the completely explicit estimate

\[
 |\mathscr L_j(H_t;x)|
 \le \frac{D_0^2j!(j+2)!}{4\beta^{2j+4}}
  \left(\frac{x}{4\pi}\right)^5
  \exp(-\pi x/4+8\pi).                               \tag{16}
\]

For the full physical disk \(|z-x|\le1/L\), use \(B=1/20\), since
\(L\ge20\), and \(\gamma=23/40\). The same contour gives

\[
 |\mathscr L_j(H_t;z)|
 \le\frac{D_{1/20}^2j!(j+2)!}{4(23/40)^{2j+4}}
 \left(\frac{x}{4\pi}\right)^5
 \exp(-\pi x/4+8\pi+\pi/(4L)).                       \tag{17}
\]

Indeed \(\Re z\ge x-1/L\) and \(2a_x/L\le\pi/(4L)\).
The source contour, its endpoints, and the genuine entire physical
function are covered directly; this does not extend the imported
finite-sum approximation outside its stated disk.

## 6. Raw half-plane bound for complete product-index cutoffs

The preceding full-source norm uses Jacobi cancellation on negative real
arguments. A product-index tail needs a separate raw absolute bound.
Define, for \(0<c\le1\),

\[
 A_c(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}+3\pi n^2e^{5u})
                         e^{-\pi c n^2e^{4u}},
\]
\[
 R_{p,B}(c,t)=\int_0^\infty\int_{\mathbb R}
 (1+s+|r|)^p e^{2Bs+2t(s^2+r^2)}
 A_c(s+r)A_c(s-r)\,dr\,ds.                          \tag{18}
\]

Assume \(p\) is a nonnegative integer,
\(0\le B\le1/20\), \(0\le t\le1/20\), and
\(tU\le2/5\), where \(U=\tfrac14\log(1/c)\). Set

\[
 \beta_* =3/5,\quad \gamma_* =3/5-B,\quad
 b_+=4\pi-49/5,\quad b_-=4\pi-58/5,\quad \eta=1/4,
\]
\[
 E_B=e^{\gamma_*}
 \left(C_{\rm low}+\frac{C_0e^{-\pi}\gamma_*}
                              {b_+-\beta_*}\right),
\]
\[
 Q_{p,B}=\frac{E_B^2(p!)^2}{2\gamma_*^{2p+2}}
 +\frac{C_{\rm low}^2e^\eta(p+1)!\eta^{-p-1}}{1-B}
 +\frac{C_{\rm low}C_0e^{\eta-\pi}p!\eta^{-p}}
              {(1-B)(b_--\eta)}.
\]

All denominators are positive. Then

\[
 \boxed{R_{p,B}(c,t)\le Q_{p,B}c^{-11/2}.}             \tag{19}
\]

To prove this, put \(u=s+r\), \(v=s-r\). The domain is \(u+v\ge0\),
and \(ds\,dr=du\,dv/2\). On \(u,v\ge0\),

\[
 1+s+|r|=1+\max(u,v)\le(1+u)(1+v).
\]

The same low/tail proof as (9)--(12), now with \(\beta_*\) instead of
\(\beta\), \(tU\le2/5\), and the polynomial \((1+u)^p\), gives

\[
 \int_0^\infty(1+u)^p e^{Bu+tu^2}A_c(u)\,du
 \le E_B p!\gamma_*^{-p-1}c^{-5/2}.                  \tag{20}
\]

Thus the positive quadrant contributes at most the first term in
\(Q_{p,B}\) times \(c^{-5}\le c^{-11/2}\).

The two mixed quadrants combine, after their Jacobian factors, into
the region \(u=y,v=-h\), \(0\le h\le y\). In this region
\(1+s+|r|=1+y\). The low Gaussian-sum estimate is valid at every
negative argument, giving

\[
 A_c(-h)\le C_{\rm low}c^{-5/2}e^h.
\]

It follows that the mixed contribution is at most

\[
 \frac{C_{\rm low}c^{-5/2}}{1-B}
 \int_0^\infty(1+y)^p e^{2ty^2+y}A_c(y)\,dy.         \tag{21}
\]

Indeed the inner integral is bounded by

\[
 \int_0^y e^{th^2+(1-B)h}\,dh
 \le\frac{e^{ty^2+(1-B)y}}{1-B},
\]

which cancels the \(B\)-dependence of the outer exponential. This
step pays the negative raw argument without pretending it has
Jacobi-glued decay.

For \(0\le y\le U\), equation (21) is bounded by

\[
 \frac{C_{\rm low}^2}{1-B}c^{-5}e^{(4/5)U}
 U(1+U)^p.
\]

Relative to \(c^{-11/2}\), the remaining factor is
\(e^{-6U/5}U(1+U)^p\). Since \(\eta=1/4<6/5\), this is at most
\(e^\eta(p+1)!\eta^{-p-1}\), proving the second contribution in
\(Q_{p,B}\).

For \(y=U+v\), use (10). The remaining exponential in (21) is at
most

\[
 c^{-5}e^{(4/5)U}e^{-\pi}
 e^{-b_-v-(8\pi-1/10)v^2}.
\]

After extracting \(c^{-11/2}\), use

\[
 e^{-6U/5}(1+U+v)^p\le e^\eta p!\eta^{-p}e^{\eta v}.
\]

Dropping the negative quadratic and integrating gives the third
contribution in \(Q_{p,B}\), completing (19).

Now truncate the complete raw pair only after shifting the complete
kernel, retaining every \((n,m)\) with \(nm\le M\). On
\(w=s+ia\), \(s\ge0\), the real decay exponent for a raw pair is

\[
 \pi c\big(n^2e^{4(s+r)}+m^2e^{4(s-r)}\big),
\]

and the bracket is at least \(2nm e^{4s}\ge2nm\). Split this
exponential in two equal pieces. For \(nm>M\), one piece is at most
\(e^{-\pi cM}\); the other is exactly the raw absolute source with
parameter \(c/2\). Since \(a<\pi/8<1\),

\[
 |r^2(r^2-(s+ia)^2)^j|\le(1+s+|r|)^{2j+2}.
\]

Assume additionally \(tU(c/2)\le2/5\). Then the absolute omitted part of the shifted half-line
integral in (4), without its external factor \(2e^{-2ax}\), is at most

\[
 \boxed{Q_{2j+2,0}(c/2)^{-11/2}e^{-\pi cM}.}         \tag{22}
\]

For complex physical frequencies, the half-line integral itself has
the same bound with \(Q_{2j+2,B}\), after including its factor
\(e^{-2a\Re z}\). Formula (4) is restricted to real frequencies. The
complete matched complex-frequency reconstruction is supplied below.

On the sector contour from (15), the stronger hypothesis required at
\(c/2\) is automatic:

\[
 tU(c/2)\le\tfrac38+\frac{\log2}{80}<\tfrac25.
\]

Thus (22) is uniform on the shrinking sector. It is an upper tail
payment, not a sign for the retained sum. For example, a cutoff of
order \(c^{-1}\log(1/c)\), with a sufficiently large fixed constant,
makes the displayed absolute tail algebraically small after the
external exponential is removed. Since \(c\asymp x^{-1}\), this
requires a product cutoff of order \(x\log x\); no short-family
arithmetic gain is hidden in this estimate.

## 7. Matched finite representation and explicit cutoff size

Let \(F_{j,P}(w)\) denote the exact raw \(nm=P\) contribution to
equation (1), so that \(J_{j,t}(w)=\sum_{P\ge1}F_{j,P}(w)\) when
\(\Re w\ge0\), \(|\Im w|<\pi/8\). All integrals and sums are
absolute on this half-strip by the raw bound just proved. Define

\[
 S^+_{j,M}(z)=\sum_{P\le M}\int_0^\infty
                       e^{2izs}F_{j,P}(s+ia)\,ds,
\]
\[
 S^-_{j,M}(z)=\sum_{P\le M}\int_0^\infty
                       e^{-2izs}F_{j,P}(s-ia)\,ds,
\]
\[
 \mathcal T_{j,M}(z)=e^{-2az}
                    (S^+_{j,M}(z)+S^-_{j,M}(z)).       \tag{23}
\]

This preserves both matched source contours. To derive it, first shift
the complete full line using (2). On its negative half set \(s=-q\)
and use the already established complete identity
\(J_{j,t}(-q+ia)=J_{j,t}(q-ia)\). Only then expand by \(P\) and truncate.
This order avoids assigning evenness to an individual raw channel.
For \(|\Im z|\le B\), \(0\le B\le1/20\), \(0\le t\le1/20\), and
\(tU(c/2)\le2/5\),

\[
 \boxed{
 |\mathscr L_j(H_t;z)-\mathcal T_{j,M}(z)|
 \le 2^{13/2}Q_{2j+2,B}\,e^{-2a\Re z}
                        c^{-11/2}e^{-\pi cM}.}        \tag{24}
\]

For real \(x\), conjugation gives
\(S^-_{j,M}(x)=\overline{S^+_{j,M}(x)}\), hence

\[
 \mathcal T_{j,M}(x)=2e^{-2ax}\Re S^+_{j,M}(x).
\]

There is no missing finite boundary in (23): the complete Jacobi
cancellation was proved before this approximation was defined. In
particular, \(\mathcal T_{j,M}\) is **not** being identified with the
Fourier transform of the raw real-axis kernel truncated at \(P\le M\).
That different operation would retain its own finite boundary terms.

For any \(A\ge0\) and \(\varepsilon>0\), it suffices to choose an
integer \(M\ge0\) satisfying

\[
 \boxed{
 M\ge\frac{(A+11/2)\log(1/c)
       +\log(2^{13/2}Q_{2j+2,B}/\varepsilon)}{\pi c}}
                                                               \tag{25}
\]

to obtain the fully explicit error
\(\varepsilon e^{-2a\Re z}c^A\). If the right-hand side is negative,
its replacement by zero is sufficient. On the sector contour,
\(M=O_{A,\varepsilon,j,B}(x\log x)\).

The same cutoff and error apply uniformly to every physical disk
\(|z-x|\le1/L\), taking \(B=1/20\) and the source contour \(a=a_x\)
fixed at its real center. Equations (23)--(25) therefore supply a
complete complex-contour representation with a quantitative remainder
on the stated shrinking sector. The remaining unknown is a useful
signed estimate for the retained matched response under genuine
physical stationarity.

## 8. Exact implication and remaining obstacle

The new quantitative conclusion is that the complete paired transform
can be moved to within \(4\pi/x\) of the intrinsic theta boundary,
uniformly throughout one closed shrinking-time sector, with its
complex physical disk and explicit constants paid. Equations (13),
(16), and (17) are absolute upper bounds.

They give no lower bound on either \(\mathscr L_0\) or
\(\mathscr L_1\), including at genuine stationary points. In particular,
the inequalities \(H_x=0\Rightarrow HH_{xx}\le0\) and
\(H_{xx}=0\Rightarrow H_xH_{xxx}\le0\) remain unproved. An argument that
takes absolute values at (13) loses precisely the signed correlation
the strategy needs. The honest next promotion is to retain that signed
integral while controlling the same matched contour and endpoints;
neither (16) nor its exponential scale is a positivity theorem.

Equations (23)--(25) sharpen that next question. On the complete physical
stationary set, it would suffice to show the real quantity
\(\mathcal T_{j,M}(x)\) is at least the error in (24). All product channels,
the signed insertion and both matched contours remain in this statement.
No such margin is established here. The source norms do not replace a
uniform signed correlation, and even a signed theorem in this one sector
would still need the predecessor neighborhoods and complementary threshold
coverage specified in Note 8.
