# A cap at infinity: retained phase and the large-time theta profile

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), reasoning effort ultra**,
verified from this turn's metadata. Separate agents of the same model
derived and checked the calculations; no specialist or cross-model review.

**Status: analytical brainstorm, with exact model calculations and a
large-positive-time asymptotic derived below.** No later theta collision,
negative excess winding, quantitative threshold improvement, uniform
high-index estimate, or selected-wall global continuation is established.
This starts the user-requested `brainstorm/` record for further discussion
in route chat 0002. The earlier diagnosis remains in [Note 03][n3].

The [result index][results], [control catalogue][controls], and
[avoid index][avoid] apply, especially [reformulations][a01],
[control premises][a02], and [scope][a07]. Infinity is assessed as an
estimating possibility, not a new equivalent criterion counted as progress.

## 1. Infinity means a limit of complete finite contours

Interpret the cap as \(t=T+R\), with \(R\to+\infty\). For each finite
regular cap, assume that the two roots born at the initial ordinary event
continue as finite simple graphs to that cap. Write \(N(R)\) for the
number of simple roots strictly between the cap endpoints. With the
orientations and initial-event accounting of Note 03,
\[
 I_{\rm cap}(R)=-(N(R)+1)\pi,\qquad
 W_{\rm truncated}(R)=-N(R)/2,\qquad
 W_{\rm physical}(R)=-1-N(R)/2.                 \tag{1}
\]
The two wall integrals vanish exactly. A contour with a collision on its
cap is excluded; use regular truncation times instead.

Already its endpoint phases prevent a zero cap contribution. If
\(h_2=H_{xx}(T,a)\ne0\), their unit phases remain
\(-i\,\operatorname{sgn}h_2\) and \(+i\,\operatorname{sgn}h_2\).
They are opposite at every finite truncation. A continuous limiting cap
with these endpoint limits cannot be a constant phase path. Identifying
both ends as a single point at infinity does not give a continuous phase
map there.

If the roots stay adjacent for all finite times, (1) gives
\(I_{\rm cap}=-\pi\) for every \(R\), including its limit.
For isolated interior heat events with the local index law, \(N(R)\)
increases by twice their collision charge; simple root walls prevent
entry through a side. Thus a finite limiting count is eventually
constant. A limit with \(N_\infty\ge2\) would imply extra roots at some
finite cap already. Unbounded counts instead give unbounded negative
phase, not a finite winding at infinity.

An infinite-cap argument could be useful if independent source
asymptotics computed a strict excess phase and established the wall
identification and all limiting bounds. It does not remove the cap's
phase obligation. No new finite collision first appears only at infinity
by taking the limit of these discrete finite counts.

## 2. Exact quadratic: phase moves into endpoint layers

For \(H(\tau,y)=y^2-2\tau\), put \(r=\sqrt{2R}\). The root-to-root cap
is \(y\in[-r,r]\), with
\[
 E=(y^2-r^2)^2+4y^2,\qquad Q=2(y^2+r^2),\qquad
 \partial_y\arg J=-\frac{2(y^2+r^2)}{(y^2-r^2)^2+4y^2}.
\]
Its integral is exactly \(-\pi\) for every \(R>0\).

Set \(z=y/r\) and \(\epsilon=2/r\). Multiplication of the jet by the
positive constant \(r^{-2}\) leaves its phase unchanged:
\[
 J/r^2=z^2-1+i\epsilon z,\qquad
 \frac{d\arg J}{dz}
 =-\frac{\epsilon(1+z^2)}
 {(1-z^2)^2+\epsilon^2z^2}.                    \tag{2}
\]
A continuous phase lift in the open interval is
\[
 \varphi_R(z)=-\pi-\arctan\frac{\epsilon z}{1-z^2},
\]
with endpoint values \(\varphi_R(-1)=-\pi/2\) and
\(\varphi_R(1)=-3\pi/2\). The density in (2) tends to zero at each
fixed \(-1<z<1\), but its signed measures converge to
\[
       -\frac{\pi}{2}\delta_{-1}-\frac{\pi}{2}\delta_1.           \tag{3}
\]
Indeed the density is even and negative, has total mass \(-\pi\),
and converges uniformly to zero on every compact interior subinterval.
In physical endpoint coordinates \(y=-r+v\), or \(y=r-v\),
with fixed \(v\ge0\), its magnitude tends to \(1/(1+v^2)\);
each endpoint layer carries a half of the cap's phase.

The normalized jet tends to \(z^2-1\), which vanishes at both endpoints.
Its constant interior phase is therefore not a continuous nonvanishing
compactification. Dropping the cap after taking the pointwise interior
limit would lose exactly \(-\pi\).

### Finite bounds for what "near the endpoints" means

In this subsection let phase mass mean the positive measure
\(d\mu_R=-d\arg J=(Q/E)\,dy\) for the quadratic. For \(0<\delta<1\),
the middle interval \(-1+\delta\le z\le1-\delta\) has exactly
\[
 M_{\rm mid}(R,\delta)
 =2\arctan\frac{\epsilon(1-\delta)}{\delta(2-\delta)}
 \le\frac{\epsilon}{\delta}
 =\frac{2}{r\delta}.                              \tag{4}
\]
Each endpoint interval has mass \(\pi/2-M_{\rm mid}/2\).
For a prescribed error \(\eta>0\), the explicit condition
\(R\ge2/(\eta^2\delta^2)\) makes the middle mass at most \(\eta\)
radians. Thus (3) has a finite-parameter estimate.

In the original spatial coordinate, take disjoint endpoint windows
\([-r,-r+V]\) and \([r-V,r]\), where \(0<V<r\). Each window has mass
\[
 M_{\rm end}(R,V)
 =\arctan\left(V+\frac{V^2}{2(r-V)}\right),          \tag{5}
\]
and
\[
 0\le M_{\rm end}-\arctan V
 \le\frac{V^2}{2(r-V)(1+V^2)}.
\]
Consequently the mass outside both windows obeys, already at finite \(R\),
\[
 0\le M_{\rm outside}
 =2\arctan\frac1{V+V^2/[2(r-V)]}
 \le\frac2V.                                      \tag{6}
\]
Choosing \(V\ge2/\eta\) and \(R>V^2/2\) captures all but \(\eta\)
radians of the total \(\pi\) in those two windows.
Their physical widths do not shrink: they are \(O(1)\) while the cap
length is \(O(\sqrt R)\). Their relative widths tend to zero.
These statements are exact inequalities, not numerical observations.

### What a uniform simple-root estimate would require

Endpoint localization is not automatic from simplicity alone. A useful
general sufficient estimate makes its additional premise explicit.
At a simple left root \(u\), let \(s=f'(u)\ne0\) and suppose
\[
 |f''(u+d)|\le K|s|\quad(0\le d\le V),\qquad \rho=KV<1.
\]
Taylor's formula gives
\[
 f(u+d)/s=d+e_0,\quad f'(u+d)/s=1+e_1,\qquad
 |e_0|\le Kd^2/2,\quad |e_1|\le Kd.
\]
Both normalized components are positive inside the window. Its net
phase decrease is exactly \(\arctan[f(u+V)/f'(u+V)]\), so
\[
 \arctan\frac{V(1-\rho/2)}{1+\rho}
 \le M_{\rm end}\le
 \arctan\frac{V(1+\rho/2)}{1-\rho}.                 \tag{7}
\]
The inward right-root version is the same after reversing the local
coordinate. These are net phase bounds; no monotonicity was assumed.
Capturing nearly \(\pi/2\) requires a window large relative to the jet's
unit derivative scale and a small relative-curvature error \(KV\).
The quadratic has \(K=1/r\), which supplies both for fixed large \(V\)
and then sufficiently large \(r\). A general theta cap needs its own
relative-curvature bound and sufficiently separated windows.

## 3. Positive atomic control: a nonzero limiting cap

The positive cosine-source family
\(H(t,x)=1+e^{t-T_0}\cos x\) has actual all-real threshold \(T_0\).
Center at \(y=x-\pi,\ \tau=t-T_0\), and put
\(\alpha_R=\arccos(e^{-R})\). On its selected root-to-root cap,
\[
 J/e^R=e^{-R}-\cos y+i\sin y,\qquad |y|\le\alpha_R.
\]
Here \(\alpha_R\to\pi/2\), and after parametrizing by \(y=\alpha_R z\),
\[
 J/e^R\longrightarrow-\exp(-i\pi z/2)
 \quad\hbox{uniformly on }[-1,1].
\]
This limit is continuous and nonzero, but still contributes \(-\pi\).
Equivalently the physical phase density is
\[
 -\frac{1-e^{-R}\cos y}{1-2e^{-R}\cos y+e^{-2R}}\longrightarrow-1.
\]
Thus even a well-behaved compactified cap need not vanish.
The family has no later events; other simultaneous threshold events
are outside the selected contour. It lacks the complete theta source
and theta's eventual simplicity at the threshold.

## 4. The complete theta source has a calculable large-time profile

This calculation concerns \(t\to+\infty\), not large spatial height at
fixed time. Use the manuscript's normalization
\[
 H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
\quad
 \Phi(u)=\sum_{n\ge1}
 (2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]
Write
\[
 e^{tu^2}\Phi(u)=2\pi^2 e^{q_t(u)}b(u),\qquad
 q_t(u)=tu^2+9u-\pi e^{4u}.
\]
Every source summand is positive on \(u\ge0\). Direct comparison gives
\[
 0<c:=1-\frac3{2\pi}\le b(u)\le
 C:=\sum_{n\ge1}n^4e^{-\pi(n^2-1)}<\infty,\qquad b(u)\to1.
                                                               \tag{8}
\]
The upper bound follows by dropping the negative terms and using
\(e^{4u}\ge1\); the lower bound retains the \(n=1\) summand.
The same summable upper bound justifies the limit of the other summands.

For sufficiently large \(t\), let \(L=L_t\) be the large stationary point:
\[
 4\pi e^{4L}=2tL+9,\qquad
 L=\frac{\log t+\log\log t-\log(8\pi)+o(1)}4.                    \tag{9}
\]
There is one such large point: \(q_t''=2t-16\pi e^{4u}\) strictly
decreases, while \(q_t'(0)=9-4\pi<0\) and the maximum of \(q_t'\)
is positive for large \(t\). Thus \(q_t'\) has a small zero giving a
local minimum and a large zero giving this maximum of \(q_t\).
Taking logarithms in the stationary equation first gives
\(L\sim\log t/4\), and substitution gives the second formula in (9).

Put \(A=\pi e^{4L}\) and \(\kappa=16A-2t=8tL-2t+36\). The exact
identity
\[
 q_t(L+v)-q_t(L)
 =tv^2-A(e^{4v}-1-4v)                            \tag{10}
\]
pays both localization and the limiting Gaussian:

* For \(v\ge0\), \(e^{4v}-1-4v\ge8v^2\), so (10) is at most
  \(-\kappa v^2/2\).
* Fix a small \(\delta>0\). For \(-\delta\le v\le0\), Taylor's
  integral remainder gives \(e^{4v}-1-4v\ge8e^{-4\delta}v^2\).
  For sufficiently large \(t\), (10) is therefore at most
  \(-c_\delta\kappa v^2\), with \(c_\delta=e^{-4\delta}/4>0\).
* On \(0\le u\le L-\delta\), the maximum of \(q_t\) is at an endpoint.
  Eventually \(q_t(L-\delta)>q_t(0)\), since the former is asymptotic
  to \(tL^2\). Its integral is bounded by
  \(L\exp(q_t(L)-c_\delta\kappa\delta^2)\) times the constant in (8).

For \(v=w/\sqrt\kappa\), (10) tends to \(-w^2/2\) uniformly on
bounded \(w\)-intervals; its error there is \(O(|w|^3/\sqrt\kappa)\).
The preceding domination and far-left bound consequently give
\[
 H(t,0)\sim2\pi^2e^{q_t(L)}\sqrt{\frac{2\pi}{\kappa}}.           \tag{11}
\]
They also give convergence of every fixed absolute moment of the
normalized spectral variable \(\sqrt\kappa(U-L)\) to the corresponding
standard Gaussian moment. In particular
\(\mathbb E|U-L|=O(\kappa^{-1/2})\).
The far-left probability is bounded by a constant times
\(L\sqrt\kappa e^{-c_\delta\kappa\delta^2}\), so normalization has not
been omitted from that tail payment.

It follows directly, by writing the cosine integral as an expectation,
that
\[
 F_t(z):=\frac{H(t,z/L_t)}{H(t,0)}
       =\mathbb E\cos(zU/L_t)\longrightarrow\cos z              \tag{12}
\]
in \(C^j\) on every bounded real interval for each fixed \(j\).
For example \(\mathbb E|U/L-1|=O((L\sqrt\kappa)^{-1})\);
the elementary sine/cosine Lipschitz bounds give the same order for
the \(C^1\) error on a fixed interval. Higher derivatives use the
corresponding moment bounds. No numerical saddle or unproved interchange
of an oscillatory tail is used.

For any fixed \(k\), (12) shows that the \(k\)-th positive real zero obeys
\[
             L_t x_k(t)\longrightarrow(k-\tfrac12)\pi.         \tag{13}
\]
To justify the indexing, take small disjoint neighborhoods of the first
finitely many positive cosine zeros. Uniform convergence excludes zeros
in the complement, including near zero. Uniform derivative convergence
gives a fixed derivative sign in each neighborhood, and opposite signs
at its endpoints give exactly one simple zero. This proves (13) without
assuming all-realness of the other complex zeros.

Thus fixed-index roots approach zero as \(t\to\infty\). This is convergence
of their locations, not a proof of eventual monotonic motion or a result
uniform in growing \(k\).

## 5. What this profile says about the chosen walls

If the two walls continue globally as adjacent fixed positive indices
\(k,k+1\), (13) gives
\[
 w_+(t)-w_-(t)\sim\frac{\pi}{L_t}\longrightarrow0.
\]
Under the hypothetical all-real threshold, future simplicity preserves
their order whenever the required finite continuations exist.
Identifying the originally chosen walls globally remains a continuation
premise; (12) alone does not provide that identification.

Their rescaled cap has endpoints tending to
\((k-\tfrac12)\pi,(k+\tfrac12)\pi\), hence is one cosine lobe.
The derivative-channel rescaled jet satisfies
\[
 F_t+iF_t'\longrightarrow \cos z-i\sin z=e^{-iz},
\]
so it carries \(-\pi\). Positive rescaling of the imaginary component
preserves the root-endpoint phase increment and, on a finite nonzero
closed contour, preserves winding through a nonvanishing homotopy.

The **physical** jet is instead
\[
 \frac{J(t,z/L)}{H(t,0)}=F_t(z)+iL F_t'(z).
\]
It must not be confused with \(F_t+iF_t'\). The \(C^1\) error bound above
gives \(J/H(t,0)=\cos z-iL\sin z+o(1)\) on fixed real compacts.
Near the intermediate extremum, \(z=k\pi+w/L\), this becomes
\[
 \frac{J}{H(t,0)}\longrightarrow(-1)^k(1-iw).
\]
Its phase derivative in \(w\) is \(-1/(1+w^2)\), whose full integral
is \(-\pi\). This describes the retained half-turn in an interior
phase layer of width \(O(L^{-1})\) in \(z\), or \(O(L^{-2})\) in the
original \(x\) coordinate. Spatial coalescence of the walls at infinite time is
therefore not a finite collision; in the scaled coordinates the
two endpoints remain distinct.

The fixed-center asymptotic is also instructive:
\[
 H(t,x)/H(t,0)=\cos(L_t x)+o(1)
\]
uniformly for \(x\) in a fixed bounded interval, by
\(\mathbb E|U-L|=O(\kappa^{-1/2})\). A sign change at the original
positive collision height cannot be used as an interior cap sign
without checking the walls: fixed-index walls eventually lie below
every fixed positive \(x\).

The large-time cosine limit is not a distinguishing RH sign.
The leading-tail comparison (8) is shared by many sources; it is fully
compatible with the adjacent-root scenario. The unchanged theta source
was used to derive its constants, not to obtain an excess phase.

### A finite error interface for the theta phase layer

The actual theta estimate can also be made quantitative without claiming
uncomputed constants. Under the normalized complete-source law above,
write \(m_1=\mathbb E|U-L|\), \(m_2=\mathbb E(U-L)^2\). On \(|z|\le Z\),
\[
 |F-\cos z|\le\varepsilon_0:=Zm_1/L,\qquad
 |F'+\sin z|\le\varepsilon_1:=(1+Z)m_1/L,
\]
\[
 |F''+\cos z|\le\varepsilon_2:=(2+Z)m_1/L+m_2/L^2.              \tag{14}
\]
These follow by differentiating the expectation and applying the real
sine/cosine Lipschitz bounds; in the last inequality use
\(|(U/L)^2-1|\le2|U/L-1|+(U/L-1)^2\).
In particular the physical jet error from
\(M_L(z)=\cos z-iL\sin z\) is bounded by
\[
 |(F+iLF')-M_L|\le
 \mathcal E:=\sqrt{\varepsilon_0^2+L^2\varepsilon_1^2}
 =O(\kappa^{-1/2}).                              \tag{15}
\]

For \(L\ge1\), \(|M_L|\ge1\). If a complete bound supplies
\(\mathcal E<1\) on the entire interval, the quotient of the actual
jet by \(M_L\) stays in a disk centered at 1 avoiding zero. Its argument
error at any point is at most
\(\arcsin(\mathcal E/|M_L|)\), with one continuous argument branch.
For cuts \(z=k\pi\pm A/L\), \(0<A/L<\pi/2\), put
\[
 r_A=\sqrt{\cos^2(A/L)+L^2\sin^2(A/L)}.
\]
The model central phase decrease and actual decrease \(C\) satisfy
\[
 C_0=2\arctan[L\tan(A/L)],\qquad
 |C-C_0|\le2\arcsin(\mathcal E/r_A).               \tag{16}
\]
Provided the cuts lie inside a cap between adjacent simple actual roots,
the full decrease is \(\pi\). Therefore
\[
 |\pi-C|\le \frac2A+2\arcsin(\mathcal E/r_A).       \tag{17}
\]
This controls the **net** outside phase. To interpret it as positive
phase mass, a sufficient complete monotonicity condition is
\[
 2\varepsilon_1+\varepsilon_0+\varepsilon_2+
 \varepsilon_0\varepsilon_2<1,
\]
since expansion of \(F'^2-FF''\) then gives a strictly positive lower
bound. The source moment asymptotics ensure this eventually for fixed
\(Z\), but no explicit onset time is certified here.

For comparison, fixed scaled endpoint strips of width \(b\in(0,\pi/4)\)
have model total decrease \(2\arctan(\tan b/L)\).
If each actual endpoint is within \(b\) of its corresponding cosine
root and the cuts are inside the actual cap, the same phase perturbation
bound gives total net endpoint phase at most
\[
 \frac{2\tan b}{L}
 +2\arcsin\frac{\mathcal E}{r_b},\qquad
 r_b=\sqrt{\sin^2b+L^2\cos^2b}\ge1.              \tag{18}
\]
Here the bound is also valid for the absolute value of the net endpoint
phase. **Finite-bound correction during manuscript review, 20 October:**
the exact cut modulus \(r_b\) makes the arcsine defined under
\(\mathcal E<1\). The earlier looser denominator \(L\cos b\) may be
used only with the additional condition \(\mathcal E<L\cos b\).
The large-time conclusion is unchanged.
One may verify the root/cut conditions by requiring
\(\varepsilon_0<\sin b\) and \(\varepsilon_1<\cos b\) on the lobe
enlarged by the two root neighborhoods. Sign and derivative bounds give
one root in each neighborhood and no root in the intervening interval.
Thus the large-time theta calculation puts the phase in an **interior**
layer, not the quadratic's endpoint layers.

## 6. A precise surplus budget, and what it still needs

For a root-wall cap with the ordinary birth contract, define signed
decreases \(M_{\rm ends}\) and \(M_{\rm mid}\) on disjoint endpoint
windows and their complementary middle. Then
\[
 M_{\rm ends}+M_{\rm mid}=(N+1)\pi,\qquad N\ \text{even}.
\]
If independent, fully paid estimates established
\[
 M_{\rm ends}\ge\pi-\eta_R,\qquad
 M_{\rm mid}>\eta_R,                              \tag{19}
\]
their sum would exceed \(\pi\). Quantization would force
\(N\ge2\) and total decrease at least \(3\pi\), hence a later event.
A directly proved middle surplus with exact endpoint arguments would
serve the same purpose. No bound of \(3\pi\) need be obtained by coarse
integration if a strict excess over \(\pi\) can be certified.

This is a concrete error budget for a proposed estimate, not a new
theta estimate. The quadratic exactly saturates the budget:
\[
 M_{\rm mid}=\pi-M_{\rm ends}
 =2\arctan\frac{\epsilon(1-\delta)}{\delta(2-\delta)}.
\]
Counting its small positive middle phase while dropping the equally
large endpoint deficits would manufacture a false surplus.
For the theta fixed-label asymptotic, (18) instead puts vanishing phase
at the endpoints and nearly all \(\pi\) in the middle. Quadratic endpoint
bounds cannot be transferred to that geometry.

Concentration also depends on the chosen jet scale. For any \(\beta>0\)
constant along the cap,
\[
 J_\beta=f+i\beta f',\qquad
 -d\arg J_\beta=\frac{\beta Q}{f^2+\beta^2(f')^2}\,dx.
\]
Positive imaginary-component rescaling preserves winding, but a
simple-root linear model now has density
\(\beta/(d^2+\beta^2)\) and window mass \(\arctan(V/\beta)\).
For the quadratic, choosing \(\beta=r/2\) removes endpoint concentration
in the scaled \(z\) coordinate. For theta, choosing \(\beta=1/L\)
gives \(F+iF'\to e^{-iz}\), distributing phase across the cosine lobe.
Time-dependent positive \(\beta(t)\) is allowed in the finite-contour
homotopy; an \(x\)-dependent choice adds a derivative term to the
displayed phase density.

The potentially contradictory quantity is therefore the fully accounted
signed surplus in (19), not localization by itself. Its missing input
is a theta estimate incompatible with the ordinary half-turn. The
asymptotic and conditional error bounds here do not provide that input.

## 7. Other meanings of infinity and the remaining opportunity

If instead the cap expands to \(x=\pm\infty\) at a fixed time, a sequence
of root-endpoint caps containing infinitely many real zeros has one
additional \(-\pi\) contribution for each added lobe. Its unrenormalized
phase diverges. Subtracting a reference count is a new renormalized
quantity requiring its own justification; it is not a zero cap term.

The quadratic and atomic controls above screen the idea that infinity
alone removes the cap. The two-event quartic from Note 03 has two extra
interior cap zeros after its later event and retains cap phase \(-3\pi\)
at every later regular time; its first event is not its all-real threshold.
The higher-multiplicity control requires its own initial index.
Euler-factor, weighted-square, finite-prime, reflected and
positive-primitive controls keep the catalogue's stated source and
threshold distinctions; no unsupplied global wall system is assigned
to them here.

**Continuation assessment.** Infinity can simplify a cap by giving an
explicit asymptotic profile. The calculation above yields the ordinary
half-turn for adjacent fixed labels. A useful contradiction would still
require an independent estimate or wall identification incompatible with
that outcome, with uniform control in whatever index/time regime it uses.
BW09-05's signed extension remains deferred. This brainstorm does not
reactivate a numerical campaign or change the bounded HFCE outcomes.

[n3]: ../notes/03_ROOT_FOLLOWING_WALLS_AND_CAP_COUNT_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
