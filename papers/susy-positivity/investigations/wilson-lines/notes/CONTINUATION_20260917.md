# Continuation note, 17 September 2026 (end of session)

**Author: Claude Opus 5 (Anthropic).** Handoff for the next session, which will
be a new chat. Read in this order: §§1--3 here, then
[the sampling note](SAMPLING_AND_THE_DEFICIT_20260917.md), which is the current
front, then [the manuscript](../manuscript.pdf) (30 pages), then the remaining
notes in the order [the index](README.md) gives.

**A ready prompt for that session is in
[NEW_SESSION_PROMPT.md](NEW_SESSION_PROMPT.md)**, with the task, the fallback,
the trap list and the conventions in a form that can be pasted directly.

---

## 1. Where things stand

**Manuscript 0.3**, *Deformation flows for the shifted Weil family: the transfer
as an all-pass filter*, 30 pages, ten sections and an appendix. Builds clean, no
overfull boxes and no undefined references, recorded after a page review,
snapshotted as `drafts/2026-09-17-v03`, and
`python3 validation/drafts.py check --replay` passes over 206 recorded cases.
Versions 0.1 (18 pages) and 0.2 (29 pages) are preserved at
`drafts/2026-09-17-v01` and `drafts/2026-09-17-v02`.

**Every recommendation in the six research notes has been folded in.** The
notes remain as written, with their own recommendation sections, and are now
historical: the manuscript is the current statement. Nothing in the notes is
retracted; the one thing withdrawn anywhere was an unqualified phrase, and it is
gone from the manuscript.

**Nothing in the manuscript assumes the Riemann hypothesis** except where a
statement is explicitly labelled conditional, and no source is constructed, no
positivity is proved, and no gauge theory is matched or excluded.

## 2. The six facts a new session needs

**(a) The transfer is an all-pass filter.** $|K_\omega(i\tau)|=1$ for every real
$\tau$ and every $\omega$, exactly and unconditionally, from the functional
equation and the reality of $\xi$ alone. Everything in Sections 4--7 of the
manuscript is a consequence. If you remember one thing, remember this one.

**(b) The Weil symbol is a group delay and the zeros are resonances.** The phase
derivative of the filter is $2\theta'(\tau)=b(\tau^2)+w_0$, which *explains* the
companion investigation's density identity rather than reproducing it; and each
zero contributes a Lorentzian of width $\omega$ and mass $4\pi\omega$ to
$|K_\omega-1|^2$, so the Weil form is a total resonant response.

**(c) Under RH the contraction defect is a boundary flux.**
$\langle f,D_{\omega,L}f\rangle=\int_{L/2}^\infty|(V_\omega f)|^2$: the flow
pushes mass out of the leading endpoint and never pulls it in.

**(d) The shift--length plane is settled, and it is not a place to look.** The
contraction region is monotone in $L$ with supremum one or infinity and nothing
between, so contraction at every $L$ is *equivalent* to the absence of zeros at
distance more than $\omega$. The family is a graded criterion, one zero-free
strip per shift. Under RH the region is the whole quadrant, so **there is no
critical path**; and monotonicity makes the plane a **disproof instrument** on
which only a certified value above one carries information.

**(e) The endpoint algebra is triangular and flat.** $\partial_\omega B_L=0$,
$G_{\omega,L}B_L=0$ by causality, $[G,B_L]=-B_LG\neq0$, and flatness is the
identity $\partial_LG_{\omega,L}=B_LG_{\omega,L}$. So the non-commutativity the
proposal wanted *exists* and is trivialized by flatness plus simple
connectivity. Exactly two things can untrivialize it, and they are the two open
problems.

**(f) The form's symmetry group is a conformal one.** Every kernel depends on
$x-y$, so the functional is translation-invariant in $x$; with $x=\log r$ that is
dilation in $r$, and reflection is inversion. The Möbius maps preserving
$\{0,\infty\}$ are exactly those two, so **the Weil form's exact symmetry group is
the residual conformal group of a ray with one end pinned at the origin.** On a
ray the Mellin variable is the dilation eigenvalue and $s=\Delta+i\tau$, so
$\Delta=\frac12$ --- which Condition 9.3 requires for an unrelated reason --- puts
it on the critical line. Positivity is also invariant along a conformal orbit, by
Sylvester, so the whole orbit of the target is an equally good target.

**(g) The margin is a frame bound, and the scale is the prime cutoff.** Under RH,
$\lambda_{\min}(Q_{0,L})$ is the lower frame bound of the Riemann zeros as a
sampling set for the Paley--Wiener space $PW_{L/2}$, whose generating function is
$\xi$ --- so the de Branges route and the margin question are **the same
question**. A counting argument gives strict positivity a reason: the zeros have
superlinear density, a Cartwright-class function of type $L/2$ has a linear zero
budget, so no nonzero one vanishes on them. The budgets cross at
$\tau_c=2\pi e^L$ with maximal sample deficit $D(L)=2e^L-\frac74$ exactly, and
since $e^L=X$ is the prime cutoff, the crossover *is* the explicit-formula
balance. See [the sampling note](SAMPLING_AND_THE_DEFICIT_20260917.md).

**(h) There is a trap, and it caught me once.** Unimodularity forces
$\operatorname{Re}a_\omega(i\tau)=0$, which looks like it kills $Q_{\omega,L}$.
It does not: $a_\omega$ has poles at $\operatorname{Re}p=+\omega$, so its
continuation to the axis is not the causal symbol, and the residues crossed are
the whole form. The contour may be moved for $K_\omega$ and may not for
$a_\omega$. The same trap applies to the Cayley symbol $a_{\rm cum,\omega}$,
which is purely imaginary on the axis.

## 3. Recommended pathway, in order

**1. The lower frame bound of the zeros on $PW_{L/2}$.** This is what "how the
margin collapses" means, now that the margin has been identified (fact (g)), and
it absorbs what used to be two separate items --- the zero-placement precision
and the reading of Suzuki. Three steps, in order: read
[arXiv:2301.00421](https://arxiv.org/abs/2301.00421) and the non-uniform sampling
literature as **machinery**, not background; recompute upper bounds on
$\lambda_{\min}$ in a basis built from the deficit band $|\tau|<\tau_c=2\pi e^L$
rather than from polynomials or from $\gamma_1$, calibrating against Zhu; and run
the control with an artificial zero set of the same density but no arithmetic,
which separates a density effect from an arithmetic one. **Nothing quantitative
can be claimed before the second step**, for the reason in §4.

**2. The group-delay test on a specific open Wilson line.** The superconformal
defect setting is now the natural place for it rather than one the test was
expected to fail: fact (f) says the target's symmetry is that geometry's residual
conformal symmetry, and the vanishing theorem of arXiv:1102.4948 therefore reads
as an alignment. Take a protected open Wilson line two-point function there,
extract the phase of its spectral kernel against the dilatation eigenvalue, and
compare its derivative with $2\theta'(\tau)$. A bounded delay kills the
candidate; the wrong coefficient kills it too. No arithmetic, no positivity, and
it is the first test in this program that a gauge theory can fail. Manuscript
Condition 9.1.

**3. Problems 8.6 and 8.7 of the manuscript**, which Section 8 shows are the two
forms of one question: whether the endpoint flow closes on a domain where
$Q_{\omega,L}$ is also closed (a smearing question, with the profile fixed by
Condition 9.3), and what a matrix-valued residue at one atom would have to
satisfy.

**4. The conformal congruence at the endpoint.** Positivity is invariant along a
conformal orbit (Proposition 9.6), so the semicircle form is an equally good
target on a *compact* contour. But the Jacobian of the ray-to-semicircle map
degenerates at the endpoints --- exactly where Proposition 8.5 obstructs. Whether
that softens the endpoint or leaves the form domain bears directly on item 3.

**5. Does the vanishing theorem generalize** beyond the $\mathcal N=2$
fundamental-hypermultiplet class of arXiv:1102.4948?

*Why this order.* Item 1 is where a numerical fact is asking for a proof and the
machinery now exists; item 2 is the only one that can close the physics side
quickly, in either direction, and costs least among the gauge-theory items.

## 4. What not to redo

- **Do not look for a critical path in the $(\omega,L)$ plane.** Corollary 7.3
  settles it: under RH the contraction region is the whole quadrant. The earlier
  shifted-zeta programme's path was a boundary of the *generator* region, which
  collapses like $\sqrt{m_L}$ under RH as well and is eleven orders of magnitude
  from anything detectable at $L=\log7$.
- **Do not revive the sufficient generator condition** $\omega\kappa_L<\pi/4$.
  Same reason, quantified in Remark 7.7.
- **Do not expect the flow formulation to escape the criticality.** A bound at
  fixed $\omega$ buys a zero-free strip of width $\omega$ and nothing more.
- **Do not produce certified upper bounds on $\lVert V_{\omega,L}\rVert$.** They
  certify nothing. Only a certified value above one carries information.
- **Do not fit a decay law to the recorded margins.** Every one of them is a
  trial-space Rayleigh quotient, hence a basis-dependent upper bound, and two
  independent computations differ by about $250$ orders of magnitude at $L=2$.
  A law fitted to them is a law about the basis. This also qualifies manuscript
  Proposition 7.6, whose $\kappa_L\sqrt{m_L}$ relation rests on three values
  from one basis family. The sampling note, §5, has the numbers.
- **Do not evaluate $a_\omega$ or $a_{\rm cum,\omega}$ on the imaginary axis.**
  See fact (f).
- **Do not look for the object among characters.** A holonomy in a
  finite-dimensional representation of a compact group has a bounded group delay;
  the required delay grows like $\log\tau$.
- **Do not repeat the argument that conformal invariance forbids the target.**
  It was wrong, and version 0.3 corrects it: the transformation that destroys the
  prime atoms is dilation in $x$, that is $r\mapsto r^\lambda$, which is not a
  Möbius map. The Weil form is exactly invariant under dilation in $r$ and
  inversion, which together are the residual conformal group of a ray with one
  end pinned --- so conformal symmetry is aligned with the target. See
  [the conformal correction note](CONFORMAL_CORRECTION_20260917.md) and
  manuscript Section 9.4.

## 5. Open threads not on the pathway

- **The de Branges structure function** --- if the frame bound of item 1 is
  expressible through it, that is the theorem to chase, and it is the one route
  here that could produce a result rather than a constraint.
- **The shape term on the fibre** (Remark 8.8): flatness concerns the
  two-parameter slice, not the infinite-dimensional space of contours, and the
  fibre of the correspondence is where the non-Abelian Stokes shape term acts.
  Whether it acts trivially there is uncomputed, and either answer is
  information.
- **The spectrum of dimensions** (Section 9.4): the requirement is not that the
  theory break conformal invariance but that it carry a continuum of dimensions
  with Mellin weight $-\zeta'/\zeta$. The principal series is a continuum, so the
  two are consistent; the named object in that direction is Bost--Connes, and
  this program has not entered that literature.
- **The exploratory `mpmath` computations** in `numerics/exploratory/` are not
  registered checks. If anything from them earns a place in the manuscript beyond
  what the Blaschke model already covers, port it under the repository
  conventions.

## 6. Conventions

- Research notes here, reviews in [`reviews/`](../reviews/README.md), with the
  author model named at the top of anything written by a language model.
- Check programs are standard library only, print JSON to stdout, keep a
  preserved record under `numerics/records/`, and are registered in the `CHECKS`
  dictionary of `validation/drafts.py`. There is one, with 206 cases.
  Computations needing excluded libraries go in `numerics/exploratory/` and are
  labelled as unregistered.
- Snapshot before replacing a manuscript version:
  `drafts.py save YYYY-MM-DD-vNN`. See [the build guide](../BUILD.md).
- Everything stays under 1 MiB per file; see the repository's
  [large-file policy](../../../../../LARGE_FILES.md).
- A session without delete permission in the repository folder will leave a stale
  `.git/index.lock` after any git command; remove it with
  `rm -f .git/index.lock` before the next commit.
