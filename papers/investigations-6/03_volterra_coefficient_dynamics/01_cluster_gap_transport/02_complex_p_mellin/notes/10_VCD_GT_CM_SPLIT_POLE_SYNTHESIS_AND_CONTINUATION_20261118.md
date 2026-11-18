# Split-pole integer closure: synthesis and continuation

18 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI
Codex LLM assistance. Actual lead model and effort unavailable in the guarded
chat registry. Conceptual recommendation Astra/ultra; bounded proof and review
helpers requested gpt-6.1-sol/ultra, without independent serving attestation.

**Proved in-note and accepted within the stated domains by E11:** the author's
separate-pole proposal gives a componentwise closed infinite integer hierarchy
for the complete relative moments and the gap coordinate. The equivalent
S/T basis is regular through target and exterior mergers. This is an exact
representation, not a new signed bound. [Assessment05][review] ·
[Result index][results] · [Cluster18][cluster] · [Avoid index][avoid] ·
[Classification01][class] · [Scope07][scope] · [Lifts03][lifts]

The [sole register][register] owns status. The [17 November synthesis][prior]
remains the record of the earlier damped-contour pass. The new work answers
an explicit author proposal after that pass; it does not silently change the
scope of its static exclusions. [B04 contract][b04]

The requested closure check is complete; no execution packet remains ready. Conditional future routing, if a quantitative continuation is requested:

| Task | Type / recommendation | Dependency | Deliverable |
| --- | --- | --- | --- |
| B03, new revision | B / Astra ultra; choose a useful quantitative consequence | Unissued; the accepted coupled hierarchy is now an available input | Specify a signed estimate or controlled truncation, its rate and remainder, and an equally informed direct comparator before freezing an E packet |

## 1. What the proposed factorization adds

Let s²=D, Q=w²-D=(w-s)(w+s), and define the complete exterior sums
\[
 P_{p,q}=\sum_j(w_j-s)^{-p}(w_j+s)^{-q},\qquad
 p,q\in\mathbb Z_{\ge0},\quad p+q\ge2.
\]
The exact elementary decompositions are
\[
 T_2=P_{1,2}+sP_{2,2}=P_{2,1}-sP_{2,2}
       =\tfrac12(P_{1,2}+P_{2,1}).
\]
Thus the coefficient in this first add/subtract step is s=sqrt(D).
The enlargement retains the odd displacement information absent from the
S-only family. In general,
\[
 S_n=P_{n,n}\ (n\ge1),\qquad
 T_n=\tfrac12(P_{n-1,n}+P_{n,n-1})=\sum_j w_jQ_j^{-n}\ (n\ge2).
\]
Conversely set k=max(p,q). The identity
\[
 (w-s)^{-p}(w+s)^{-q}
  =\frac{(w-s)^{k-p}(w+s)^{k-q}}{Q^k}
\]
has a polynomial numerator of degree at most 2k-2. Reducing powers of w with
w²=Q+D yields a finite linear combination of Q^(-n), n>=1, and w Q^(-n),
n>=2, with polynomial coefficients in s. Consequently the full mixed family
is represented by the two S/T sequences. No nonabsolute T1 is introduced in
this reduction. [Split-pole proof][split] · [Regular-basis proof][regular]

## 2. Closed equations

All primes below mean physical time. For n>=1, with empty sums zero,
\[
\begin{aligned}
 S_n'={}&2n\sum_{r=1}^{n}S_rS_{n+1-r}
       +2n\sum_{r=2}^{n}T_rT_{n+2-r}
       +2nD\sum_{r=2}^{n}S_rS_{n+2-r}\\
       &-4n(n+2)S_{n+1}-4n(n+3)D S_{n+2}.
\end{aligned}
\]
For n>=2,
\[
\begin{aligned}
 T_n'={}&2(2n-1)\sum_{r=2}^{n}T_rS_{n+1-r}
       +4nD\sum_{r=2}^{n}T_rS_{n+2-r}\\
       &-4(n^2+n-1)T_{n+1}-4n(n+3)D T_{n+2}.
\end{aligned}
\]
Together with D'=2-4DS1, these use only this relative hierarchy. In particular,
\[
\begin{aligned}
 M'&=2M^2-12S_2-16DS_3,\qquad M=S_1,\\
 S_2'&=8MS_2-32S_3+4DS_2^2-40DS_4+4T_2^2,\\
 T_2'&=(6M+8DS_2)T_2-20T_3-40DT_4.
\end{aligned}
\]
The new T2 equation stays inside the enlarged family. The displayed equations
reach higher indices, so they establish an infinite hierarchy, not a finite
truncation. No existence/uniqueness theorem for an infinite ODE with arbitrary
sequence data is claimed. The absolute midpoint is still supplied by the
original field and counted pair contour; this statement does not reconstruct
its drift from the absolutely convergent relative moments alone.

## 3. Complete divisor and collision qualifications

Both proofs start with finite polynomial heat velocities and pair the exterior
interactions before taking any complete limit. The formally occurring T1, or
P10 and P01 separately, cancels; P10-P01=2s P11 is convergent. Every retained
moment is absolutely summable by the inherited collar, strip and unit count.
The complete canonical passage uses fixed target-circle observables and the
paired-product slice approximation with its heat jet. Target contributions
are integrated around both target poles, and their full rational residue sum
vanishes; individual mixed-weight target residues need not vanish.

The P recurrence in [Note08][split] applies on D!=0 charts with a local analytic
s and includes pure-axis moments. Its coefficients involve 1/s. The S/T equations
in [Note09][regular] have polynomial D coefficients and extend analytically
through D=0 and through exterior multiplicities. For example,
\[
 P_{2,0}=S_1+2DS_2+2sT_2.
\]
At a target merger D'=2. An unsymmetrized P20 can therefore have a square-root
term when T2 at the merger is nonzero, even though S and T remain regular.
The explicit finite polynomial control in Note09 realizes this possibility;
no nonvanishing T2 at a canonical merger is asserted.

The control screen includes an exact even quartic heat family with a double
target and a double exterior location. It obeys the hierarchy at the collision.
It fails the canonical growing-population/source premises, so it is a test of
the structural equations rather than a canonical collision example. The other
[controls][controls] retain the failed-premise accounting in the proof and
review. No numerical collision certificates were rerun. [Premises02][premises]

## 4. What changes and what remains open

The earlier denominator-only nonclosure statement for generic polynomial
heat fields remains correctly scoped: S moments alone lose odd spatial
information. The enlarged family restores it and closes componentwise.
The prior no-o(log T) static-envelope comparison did not include the full
canonical dynamics and does not exclude using these coupled equations.

This pass acquires no improved canonical signed forcing estimate, invariant
inequality, finite closure, transport allowance or independent gap anchor.
The unchanged theta source and paid tube remain the setting of the complete
application. The requested integer-closure check is complete. A further
quantitative continuation would need a specified inequality or controlled
truncation using the coupled equations, with its remainder and direct
comparator; no such additional proof contract is issued here. No new manuscript,
source change or numerical campaign was made. The [small execution record][record]
and [guarded chat history][chats] retain this pass's provenance.

[register]: ../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md
[prior]: 07_VCD_GT_CM_SESSION_SYNTHESIS_AND_CONTINUATION_20261117.md
[b04]: ../brainstorm/notes/04_VCD_GT_CM_B04_SPLIT_POLE_CLOSURE_CONTRACT_20261118.md
[split]: 08_VCD_GT_CM_E09_SPLIT_POLE_INTEGER_HIERARCHY_20261118.md
[regular]: 09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md
[review]: ../reviews/05_VCD_GT_CM_E11_INTEGER_CLOSURE_ASSESSMENT_20261118.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[lifts]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md

[record]: ../numerics/04_VCD_GT_CM_INTEGER_CLOSURE_RECORD_20261118.json
[chats]: ../chat-histories/README.md
