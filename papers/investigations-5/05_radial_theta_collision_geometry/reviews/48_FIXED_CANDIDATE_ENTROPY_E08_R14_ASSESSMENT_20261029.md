# CTF-E08 R14 assessment: the fixed-candidate entropy obstruction

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 **chat0036**, *Assess CTF-E08 R14 obligations*.

**Disposition: accepted without mathematical correction on all seven
fixed obligations.** [Note94][proof] proves one precisely scoped failed
route: universal fixed-candidate entropy dissipation is false on the
smooth positive radial exact mass–energy class, even arbitrarily close
to its Gibbs candidate in H1. Its actual-path entropy/Fisher/forcing
payments, H-minus-one forcing tails and spatial L2 precompactness pass.
Actual attraction, actual nonconvergence and coefficient limits are not
established. A stronger actual-path estimate or another mechanism remains
a B02 decision; no convergence execution packet is ready.

This is a different-model **internal LLM assessment** of the Astra/ultra
proof, with three read-only Sol contributions and parent checking. The
contributors checked (1,2,6), (3–5), and (7 plus inherited inputs).
Shared premises remain; this is not specialist-independent or formal
review. No numerical sign sample or scan is used. [Review47][prior] is
the earlier proof-author internal review. The [frozen request][packet]
and all ten issued input hashes match; [record38][record] identifies
versions and protected files. [Return96][return] records the research
consequence and [Continuation97][next] the next decision.

## 1. Exact production, notation and actual forcing sign — pass

Use Note94's fixed q=M exp(−lambda V)/Z, v=grad V, d=div v and
beta=2G/D. The entropy test has gradient grad h/h+lambda v. Pairing it
with Delta h+beta div(vh), integrating both divergence terms, gives
\[
 P_\lambda=-I+\lambda A+\beta(A-\lambda C),\qquad
 J_\lambda=I-2\lambda A+\lambda^2C,
\]
and hence P_lambda=−J_lambda+(beta−lambda)T_lambda. Here A=int dh
is linear; D=int dh² is quadratic. At q, T=0 and beta=lambda.

The actual carrier has coefficient alpha=beta+delta, so the additional
pairing is **+delta T_lambda**, since
−int vh·(grad h/h+lambda v)=A−lambda C. The candidate is fixed;
neither alpha' nor beta' enters this derivative. There is no use of a
frozen-drift convergence theorem for the nonlinear feedback.

## 2. Actual chain rule, Fisher cost and both entropy forcing tails — pass

The inherited bounds are exactly those of accepted R13: mass M,
Ebar=M²D82, Gbar=M²H82, Rbar=max(R0,3M/a_*), bounded positive
original alpha, D_h>=3E0, and the two defect tails in Note90 (10).
R0 retains the complete unit-preparation contribution +6M. Historical
pending language in Note90 is superseded by [Review46][r46].

For Phi_eta=(h+eta)log(h+eta)−eta log eta,
\[
 h\Phi_\eta'(h)-\Phi_\eta(h)
 =h-\eta\log(1+h/\eta)=g_\eta(h),\quad0\le g_\eta(h)\le h.
\]
This proves Note94 (6), including its positive alpha d g_eta term.
For fixed eta the bound |Phi_eta(h)|<=c_eta h+h² pays diffusion
cutoff errors. On the expanding cutoff annulus, |v||grad chi_R| is
bounded, so drift errors are paid by the same integrable quantity.
They vanish after time integration by dominated convergence; increasing
nonnegative cutoffs also permit the nonnegative gradient term's limit.

The entropy lower bound follows from x log x>=−1/e with x=h exp(r²).
Together with h log h<=h² on h>=1, it gives
int|h log h|<=C_S=Ebar+Rbar+pi^(3/2)/e. Also
partial_eta Phi_eta=log(1+h/eta)>=0 and
\[
 |\Phi_\eta(h)|\le |h\log h|+(h+1)\log(h+1)
                   \le |h\log h|+2h+2h^2.
\]
Endpoint dominated convergence and gradient monotone convergence
therefore establish the exact integrated entropy identity and
\[
 \int_u^{u+1}I(h(s))\,ds\le2C_S+6\bar\alpha M.
\]
This pays compact-time Fisher integrability and a uniform unit-window
allowance, without asserting a pointwise uniform Fisher bound or a finite
half-line Fisher integral.

For the potential test chi_R V, diffusion cutoff terms cost at most
C int_annulus h because V<=r² and |grad V|<=2r. The drift cutoff
term costs C int_annulus r²h. Its time-integrated limit vanishes by
the inherited moment bound and dominated convergence. Thus
(int Vh)'=A−alpha C in integrated form. The resulting entropy is locally
absolutely continuous, with derivative P_lambda+delta T_lambda a.e.

Put K_T=6M+4lambda Rbar. Since |T_lambda|<=K_T, the precise tails are
\[
 \int_t^\infty|\delta T_\lambda|\,ds
 \le K_T\mathcal A_{\rm def}(t)/a_*,\qquad
 \int_t^\infty\alpha|\delta T_\lambda|\,ds
 \le K_T\mathcal A_{\rm def}(t).
\]
These are special divergence-structure pairings. The logarithmic test
is not being assigned the dual-Lipschitz seminorm from R13.

## 3. Radial moment surjectivity and exact base constraints — pass

Let k=d−lambda|v|². On any exterior radial domain k tends to minus
infinity, q tends to zero and q remains positive. A linear relation
c0+c1q+c2k=0 successively forces c2=c0=c1=0. If the corresponding
test-function moment map were not onto R³, a nonzero linear functional
would annihilate its image and contradict that independence. Smooth
radial tests w,u therefore realize the exact triples in Note94 (10).
Their compact supports fit in one annulus away from the spike origin.

The base energy equation has c derivative 2 at (tau,c)=(0,0), giving
c(tau)=−tau²||w||2²/2+O(tau³). The prescribed triples then give exactly
mass M, squared L2 norm Q and T_lambda=tau. Positivity follows from
the positive minimum of q on the fixed annulus. Outside it the base is
q; its Gaussian tail pays every stated integration by parts.

## 4. Spike scalings and exact two-constraint repair — pass

For z=a epsilon^(−1/2) psi(X/epsilon), psi=phi², the mass, squared L2
norm, gradient energy, Fisher information and second moment scale as
\[
 a\epsilon^{5/2}\!\int\psi,\quad
 a^2\epsilon^2\|\psi\|_2^2,\quad a^2G(\psi),\quad
 a\epsilon^{1/2}I(\psi),\quad
 a\epsilon^{9/2}\!\int r^2\psi.
\]
Here I(psi)=4||grad phi||2² is finite, including its zero extension.
The exact mass correction is m=−int z. Disjoint spike/annulus supports
leave the exact energy equation
\[
 U\ell^2+2B_\epsilon\ell+R_\epsilon=0,
 \quad U=\|u\|_2^2,\quad
 B_\epsilon=\langle b_\tau+m p,u\rangle,
\]
where B_epsilon=1+O(tau)+O(epsilon^(5/2)) and R_epsilon=O(epsilon²)
for fixed tau,a. For small tau,epsilon, B_epsilon>0, the discriminant
is positive, and the small root is
\[
 \ell=-\frac{R_\epsilon}
 {B_\epsilon+\sqrt{B_\epsilon^2-U R_\epsilon}}=O(\epsilon^2).
\]
The nonzero linear derivative is 2B_epsilon. Thus neither constraint
is merely asymptotic. Small smooth annular corrections preserve positivity;
on the spike ball the base remains exactly q.

The gradient cross term is bounded by ||Delta q||infinity int z and
tends to zero. Linear moments and D converge as stated. Fisher
subadditivity I(f+g)<=I(f)+I(g) gives the upper limit because I(z)->0;
off the shrinking ball the profile equals the corrected base, and the
omitted base Fisher integral tends to zero. This gives the matching
lower limit and the production limit (18).

## 5. Positive production, the diagonal and its limitations — pass

Differentiating the Fisher expression at q yields
DI(q)[j]=2lambda A(j)−lambda²C(j). Substitution into the production
formula, using beta(q)=lambda and T(q)=0, gives DP(q)[j]=0.
Smooth finite-dimensional annular perturbations therefore have
P(b_tau)>=−C0 tau² with finite C0 and D(b_tau)<=Dmax.

Choose a single finite L with 2LG(psi)/Dmax>C0+2 and set a²=L tau.
The fixed-tau production limit exceeds 2tau². Choose epsilon(tau) small
enough that its production error is below tau² and all the stated
moment/Fisher/correction errors are at most tau, with epsilon<tau².
Then P>tau² and ||h−q||H1=O(sqrt(tau))->0 at exact mass and energy.
Beta also tends to lambda; small beta−lambda supplies no missing sign.

For completeness the entropy convergence can be paid explicitly. On the
spike ball q is bounded below uniformly. Put H=a epsilon^(−1/2).
The inequality q log(1+z/q)<=z gives
\[
 (q+z)\log(1+z/q)\le z[1+\log(1+C H)].
\]
Its integral is at most C a epsilon^(5/2)[1+log(1+C H)] and tends to
zero on the stated diagonal. Annular entropy converges by smooth
convergence and a positive lower bound. This expands Note94's valid
cost estimate; it is not a correction or added hypothesis.

Every constructed state is smooth, positive, radial and Gaussian outside
a compact set. All individual Sobolev norms and moments are finite.
Uniform peak/higher-derivative bounds and actual-orbit realization are
absent. Arbitrary sharp R13 numerical allowances are not asserted to
admit these profiles. The proved conclusion is positive instantaneous
production on the declared state class, not a nonconvergent trajectory.

## 6. Radial constants, H-minus-one forcing and spatial compactness — pass

Integrating (r²h²)' gives
\[
 r^2h(r)^2=-2\int_r^\infty t h^2\,dt
           -2\int_r^\infty t^2hh'\,dt
 \le\frac{\|h\|_2\|\nabla h\|_2}{2\pi}.
\]
The constant uses the 4pi radial volume factor in each L2 norm.
An endpoint subsequence or radial H1 approximation justifies the endpoint.
Writing C_r=(Ebar Gbar)^(1/4)/sqrt(2pi), positivity gives
\[
 rh\le C_r,\quad \int r^2h^2\le C_r\sqrt{M\bar R},\quad
 \|vh\|_2\le2C_r^{1/2}(M\bar R)^{1/4}=V_2.
\]
Duality against the standard H1 norm yields
||f_s||Hminus1<=V2|delta|, so its ordinary tail is
(V2/a_*) A_def(t), and its alpha-weighted tail is V2 A_def(t).
An L2 bound on div(vh) is not claimed.

The spatial tail is exactly
int_{r>R}h²<=(C_r/R)int_{r>R}h<=C_r Rbar/R³. Local Rellich
compactness and a diagonal subsequence therefore give spatial L2
precompactness. They give no stationary/invariant limit conclusion.
The fixed-tau,a spike sequence also correctly exhibits discontinuity of
beta under L2 convergence on a bounded-H1 state class: gradient energy
can retain a defect. It is not a defect asserted on the actual orbit.
Neither beta nor original alpha has been proved convergent.

## 7. Comparator, physical premise, controls and boundary — pass

The direct comparator receives every actual-path input and proves all
the same entropy/topology payments and the same state-class obstruction.
No primitive-specific gain, smaller full allowance or physical-margin
removal follows. The positive physical vector mass remains upstream in
K and n; an admitted double event with mu=0 fails that premise.

The full theta source at (T,A)=(1/4,2), original PDE and feedback path,
complete preparation, genuine residual, raw mismatch, primitive endpoints,
full C0/C1, combined sphere cancellation and entire inner ball remain.
The synthetic test profiles change no physical source or trajectory.

The [control register][controls] is respected individually: weighted-square
controls may pass a low mark and collide elsewhere; Gaussian-polynomial,
reflected and smooth/primitive controls do not replace a positive physical
vector mass at an admitted double event; finite-prime/conditional controls
retain their source restrictions and conditionality. Variable observations
fail literal cosine/full Newman. A negative Euler-factor Laguerre witness
is not automatically a double event. Atomic/profile controls require the
declared preparation, regularity and moment hypotheses. No new event or
theta collision is inferred.

All seven checks complete the frozen E08 task. The next B02 decision is
an actual-path estimate strong enough to exclude/control this obstruction
and establish the required stability or dissipation, or a different
mechanism. More spatial compactness or stationary uniqueness alone does
not supply it. The [result index][results] and [avoid index][avoid], in
particular [target classification][a01], [shared premises][a05],
[scoped exclusions][a07] and [imports][a16], govern this disposition.
Sol's R5 manuscript and companion remain at their input bytes; no
integration, build, export, snapshot, commit or tag was performed.

[proof]: ../notes/94_FIXED_CANDIDATE_ENTROPY_OBSTRUCTION_B02_R14_20261029.md
[prior]: 47_FIXED_CANDIDATE_ENTROPY_INTERNAL_REVIEW_R14_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_FIXED_CANDIDATE_ENTROPY_ASSESSMENT_R14_20261029.md
[r46]: 46_COMPLETE_CARRIER_REDUCTION_E08_R13_ASSESSMENT_20261029.md
[return]: ../notes/96_FIXED_CANDIDATE_ENTROPY_R14_E08_RESEARCH_RETURN_20261029.md
[next]: ../notes/97_ENTROPY_ASSESSMENT_AND_MODEL_CONTINUATION_20261029.md
[record]: ../numerics/38_FIXED_CANDIDATE_ENTROPY_R14_E08_ASSESSMENT_RECORD_20261029.json
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a16]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
