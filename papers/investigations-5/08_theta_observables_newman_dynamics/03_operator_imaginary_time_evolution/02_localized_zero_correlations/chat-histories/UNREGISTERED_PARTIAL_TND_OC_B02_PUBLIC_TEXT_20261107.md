# Unregistered partial public exchange — TND-OC-B02

Prepared for Edward Baker with OpenAI Codex assistance, 7 November 2026,
America/New_York. Actual environment-reported thread:
`01a1b947-82cc-732d-94e1-f3709c4410fd`.

This is a manual preservation of the visible research request and completed
public commentary. It is not a native chat registration or complete export.
Native source discovery failed, the app thread reader failed, and the actual
title, creation timestamp, current turn id, backend model and effort are
unavailable. Sequence labels below are not fabricated timestamps.
Private instructions, reasoning and tool traffic are excluded. The original
B02 and subsequent project-summary final replies were added only on later
turns after completion. The project-summary final below was retained from
the available prior-turn context, not verified against a native source.
The current new-session-handoff final reply has not yet been sent and is
not included. No planned answer is saved.
Existing registered histories and their index are unchanged.

## 1. User

Please read /papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/continuation-notes/03_TND_OC_AFTER_E02_AND_MODEL_CHANGE_20261107, and continue with [B] TND-OC-B02.

Track your progress in the research progress folder, write research notes in the notes folder, and record chat history in the chat-histories folder. Please provide guidance for the continuation at the end of your research, and a continuation note for model changes.

## 2. Assistant — completed commentary

I’ll read the continuation note, established results, and research safeguards, then work through TND-OC-B02 and record the results and handoff in the investigation folders.

## 3. Assistant — completed commentary

E02 provides a rigorous way to approximate the localized zero statistics, but it does not prove that they are small. B02’s task is to identify the arithmetic information that could supply that signed bound. I’m checking the exact formulas and collision controls before selecting a route.

## 4. Assistant — completed commentary

One useful distinction is emerging: the compact tests ignore real zeros, but the general logarithmic error bound still pays for them. I’m checking whether that creates a quantitative error floor for zero-free Euler-product approximations. I’m also examining whether a mean-square comparison retains enough cancellation to bound the desired statistic.

## 5. Assistant — completed commentary

The error floor can be made explicit. At a window centered on a real zero of multiplicity \(m\), replacing the logarithm by a harmonic approximation and then applying the full-disk absolute error bound gives \(E_Q\ge m\log 2/36\). That certificate cannot resolve defects with \(d^2\le m\log 2/72\).

This limits that particular estimation method; it is not a lower bound on the true transverse mass. I’ll write up the proof and its scope, together with the uncancelled term in the mean-square comparison.

## 6. Assistant — completed commentary

The proof and exact constant checks are written. B02 ends with a scoped obstruction, not a new zero exclusion: separate mean-square bounds leave a logarithmic cancellation unproved, while harmonic baselines incur the explicit real-zero error floor.

I’m preparing the progress update and a bounded Sol assessment packet. Native chat capture is still unavailable for this thread, so I’ll preserve the completed public exchange as a clearly labelled partial record.

## 7. Assistant — completed B02 final reply

Completed **TND-OC-B02** with a scoped obstruction. At a window centered on a real zero of multiplicity \(m\), the harmonic-baseline method’s full-disk error allowance satisfies
\[
E_Q\ge \frac{m\log 2}{36}.
\]
This limits that certificate; the desired canonical signed bound remains open.

Saved the proof, self-check, exact constant checks, and progress updates:

- [Research note](sandbox:/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/notes/04_TND_OC_B02_SIGNED_JENSEN_AND_HARMONIC_DISTANCE_20261107.md)
- [Continuation and model-change instructions](sandbox:/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/continuation-notes/04_TND_OC_AFTER_B02_AND_MODEL_CHANGE_20261107.md)

**Next: [E] TND-OC-E03 — Sol / ultra:** separately assess the proof, constants, and scope.

Native chat capture still lacks the source transcript. A labelled partial public exchange was saved; it excludes this final reply.

## 8. User

Can you summarize the current state of the project and what has been learned so far. Please use equations in your description, and verify that the chat capture is working now.

## 9. Assistant — completed commentary

I’ll check the current research registers and notes, then summarize the results with equations. I’ll also test chat capture and verify what it actually saves.

## 10. User

Also save the explanation in brainstorm/explanations

## 11. Assistant — completed commentary

I’ll save the explanation in this investigation’s `brainstorm/explanations/` folder. The capture check still fails for this conversation: the updated recorder supports the new local history format, but this thread’s source is unavailable, and the app’s thread reader also fails. The partial public record remains the available fallback.

## 12. Assistant — completed commentary

The explanation is saved. It separates the accepted source-to-statistic estimates from the signed bound still needed for exclusion, and includes the Green branch’s latest assessment. I’m checking the links and preserving the previous final reply in the partial chat record; the research task statuses are unchanged.

## 13. Assistant — completed final, retained from prior-turn context

Saved the detailed explanation in this branch’s `brainstorm/explanations/` folder: [01_PROJECT_STATE_AND_LESSONS_20261108.md](sandbox:/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/brainstorm/explanations/01_PROJECT_STATE_AND_LESSONS_20261108.md).

The current theta/Newman program has established **ways to detect hypothetical nonreal zeros and control approximation errors**. The central missing step remains **a sufficiently small signed estimate for the canonical theta field**.

We study
\[
H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du,
\qquad
\partial_\lambda H_\lambda=-\partial_z^2H_\lambda,
\]
with \(H_0(z)=\xi(\tfrac12-\tfrac{iz}{2})/8\). RH corresponds to all zeros of \(H_0\) being real. The operator realization describes this evolution, but source positivity alone does not control the zeros of the oscillatory transform.

Our principal localized observable is
\[
Q_{X,h}=\sum_j w\!\left(\frac{x_j-X}{h}\right)y_j^2,
\qquad z_j=x_j+iy_j.
\]
A conjugate pair \(x_0\pm id\) in the window’s plateau contributes \(2d^2\). Real zeros contribute zero, including multiple ones, so the observable does not demand simplicity.

We learned that some richer-looking statistics contain essentially the same information. Conjugation gives
\[
\sum_{j\ne k}w_jw_k(y_j-y_k)^2=2N_wQ_w.
\]
Likewise, the deterministic configuration product
\[
Z(\eta)=\prod_j(1+\eta w_jy_j^2)
\]
satisfies, in the canonical unit strip,
\[
\log(1+\eta)Q_w\le\log Z(\eta)\le\eta Q_w.
\]
Its hierarchy and remainders are controlled, but these identities do not themselves make the transverse mass small.

The main positive advance is the **internally assessed source-to-statistic comparison**. For the normalized field
\[
F(z)=\frac{s-1}{s}\zeta(s),\qquad s=\tfrac12-\tfrac{iz}{2},
\]
a complete-disk approximation error \(\delta\) yields
\[
|Q-\widehat Q|\le E_Q,\qquad
|\log Z-\widehat L_\eta|\le E_\eta,
\]
where
\[
E_\varphi=
\frac{\|\Delta\varphi\|_\infty}{2\pi}
C_X\left(\frac{\delta}{M_X}\right)^{2/(n_X+2)},
\qquad n_X=O(\log X).
\]
This handles logarithmic singularities and multiple zeros, with complete source-tail payments. Its exponent deteriorates with height, and numerical integration errors would still need separate treatment.

The required exclusion inequality is now explicit:
\[
\widehat Q+E_Q<2d^2
\quad\text{or}\quad
\widehat L_\eta+E_\eta<2\log(1+\eta d^2).
\]
**We can control the approximation error; we have not proved the remaining finite-source value sufficiently small.**

B02 clarified two obstacles. First, splitting the test Laplacian into positive and negative parts gives quadratic averages \(A_\pm\) and Jensen gaps \(J_\pm\), with
\[
S_\varphi=\frac{b}{4\pi}
\left[\log\frac{A_+}{A_-}+J_--J_+\right].
\]
Here \(b\) is their common Laplacian mass. Separate quadratic bounds leave the crucial cancellation \(J_--J_+\) uncontrolled—even zero-free nonconstant fields need that cancellation.

Second, B02 proved the sharp local bound
\[
\inf_{v\ \mathrm{harmonic}}
\int_{D(a,\ell)}|\log|F|-v|\,dA
\ge \frac{\pi\log2}{2}\,m\ell^2
\]
when \(F\) has an \(m\)-fold zero at \(a\). In our disk geometry, a real zero at the window center therefore forces
\[
E_Q\ge \frac{m\log2}{36}
\]
for the **harmonic-baseline/full-disk absolute-error method**. That method cannot resolve \(d^2\le m\log2/72\). This bounds an error allowance, not the true transverse mass. Methods retaining real zeros or exploiting the test’s vanishing remain open.

The Green sibling has reached a related limitation: its assessed short-mollifier quadratic residual has a positive averaged floor within its specified class. Neither branch has obtained the favorable signed canonical bound. Broad averages also retain the dilution of a single defect by \(h/T\).

**Next: [E] TND-OC-E03 — Sol / ultra**, to assess B02’s proof and scope separately. B02 currently has proof-author checking only.

**Chat capture is still not working for this conversation.** I checked both supported local source formats and the app reader; this thread’s source remains unavailable. File writing works. I preserved the previous completed final reply and this turn’s completed public messages in the labelled partial record; this final reply is not yet captured.

## 14. User

Please also provide a continuation note for a new brainstorm session, hopefully it will fix the chat history issue

## 15. Assistant — completed commentary

I’ll prepare a fresh-session brainstorm handoff that preserves B02’s review status and makes chat-source verification the first step. I’ll also check whether this conversation’s source has become available.

## 16. Assistant — completed commentary

The recorder still cannot find this conversation’s source. I’ll make capture verification the first step in the new-session handoff, and prepare B03 for a bounded brainstorm while keeping B02’s separate E03 assessment pending. A new session may help, but capture will need to be verified there.

