# AGC-JH-E03 request r2 (immutable, separate parity-control follow-through)

19 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. Lead actual settings unavailable; helper dispatch gpt-6.2-sol/ultra.

Type E; recommendation/authorized dispatch gpt-6.2-sol/ultra. Parent B03 decision04. Only notes/05_AGC_JH_PARITY_OSCILLATION_CONTROL_20261119.md and research-progress/handoffs/AGC_JH_E03_RETURN_R2_20261119.md writable. Read B03, root research instructions, result/avoid indexes, VCD error law and fixed-zero asymptotic; use the source above only as a comparison control. No shared files/history edits. One derivation and one correction pass; no scan. A source-specific theta sign is outside packet.

Prove or correct the following bounded analytical claim. Let an even positive probability measure have infinite support inside [-K,K], canonical G_N, h_N=product beta_1..beta_N, and an isolated simple pair zeta=x+iy, conjugate zeta with x,y>0. Work on a fixed counted pair circle and isolating simple-root disks; no assumption that the pair is real. Set A_N=h_N |zeta|^(2N)/(2N)!, theta=arg zeta. The inherited simplex error law should give E_N=1+O(1/N) on fixed complex disks (derive explicit bound from |U| and node support<=K and exact variance). Show zeta_N-zeta=−L_N(zeta)/F'(zeta)+o(A_N) with all perturbation errors justified, hence

 D_N-D = 2y (-1)^N A_N Im(exp(2iN theta)/F'(zeta)) + o(A_N).

Since A_(N+2)/A_N<=K^4 |zeta|^4/[(2N+1)(2N+2)(2N+3)(2N+4)], deduce the increment is the negative leading sinusoid plus o(A_N). On a fixed parity, if omega=4theta is neither 0 nor pi modulo 2pi, finite geometric sums give Cesaro mean zero and mean square 1/2. Prove the resulting normalized limsup>=1/2 and liminf<=−1/2 (or a justified smaller explicit constant); do not assume irrational rotation density.

Apply to T(v)=(1-|v|)_+ and mu(v)=[T(v)+(T(v-1)+T(v+1))/4]/(3/2). Verify normalization, nonnegativity, support [-2,2], literal Fourier F(z)=[sin(z/2)/(z/2)]²(1+cos(z)/2)/(3/2), pair zeta=pi+i a, a=acosh2, exact count on |z-pi|=3/2, 0<4arg zeta<pi, |F'(zeta)|=2sqrt3/(pi²+a²). Give explicit limsup/liminf for (D_(N+2)-D_N)/A_N on EACH parity, showing infinitely many positive and negative increments. State exactly that generic parity monotonicity is excluded on this continuous compact positive-source class; theta-specific arithmetic and more flexible induction are not excluded. The time is fixed zero; no positive-time collision or finite all-real threshold is asserted for this new control.

Optional: note what same asymptotic would say conditionally for a simple nonreal theta pair if inherited phase bound is used, but do not label hypothetical theta roots acquired. Completion is proof with constants and full scope, or named proof gap. Return to lead for E05 assessment; preserve r1 evidence.
