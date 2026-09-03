# DSCT lecture digest — Wednesday, September 3, 2026

## Evidence and privacy

- Course: Discrete Structures and Critical Thinking (COMSC-2043-1420), Fall 2026, Canvas course `74035`.
- Source: fresh local Whisper/CTranslate2 (`medium.en`) transcription of the protected MP4, run on April's GPU.
- Protected MP4: `2026-09-03_discrete-structures-meeting-recording.mp4` (original filename: `Fall 2026 Discrete Structures (COMSC-2043-1420)-20260903_123226-Meeting Recording.mp4`), 268.9 MB, ~70 minutes, protected under `/mnt/ironwolf-scratch/video_mechanics/protected_raw/zoom/2026-09-03/`.
- Fresh transcript: `dsct_audio.vtt` / `.txt` alongside the protected MP4.
- This digest intentionally omits student names, chat, incidental remarks, cold-call responses, and identifying classroom details. Several students are named in the raw transcript; none are named here.

## Teaching goals

1. Use the existing GPU Showdown benchmark table as a live reasoning exercise: observation → modest, falsifiable claim.
2. Introduce sampling bias / survivorship bias as a concrete failure mode for overgeneralizing from a small hardware sample, using the WWII "armor the returning planes" story as the anchor analogy.
3. Model an honest, live failure: attempt Podman/WSL2 verification on the instructor's own machine in front of the class, hit a real platform-level hang, and demonstrate the correct response (stop, capture evidence, file a help desk ticket, don't burn class time on an administrative wall students can't fix either).
4. Walk the `fun_with_LaTeX` public repository end to end: AI-assisted script generation, the safety-review step before running anything, the two-pass nature of LaTeX builds, and closing the loop by having the AI write durable onboarding documentation back into the repo.
5. Model git hygiene as an explicit teaching move (ignoring build byproducts, cleaning up history) rather than an incidental aside.

## Concepts actually covered

### GPU Showdown table: cold start vs. warm start

The class reopened the existing GPU Showdown benchmark table (from the earlier GPU Showdown module) and used it to introduce "warm start delay" — the gap between one GPU job finishing and the next one starting when jobs are queued back-to-back — using a cold-engine-vs-warm-engine car analogy as the bridge. The instructor's own two machines were used as a concrete before/after: a much older card handling back-to-back jobs roughly five times slower than the newer one in this specific pairing.

### Reading the table for real observations

Students identified real patterns in the table: which architecture family appeared only once (evidence of a small, non-random sample rather than "that family is rare"), that all runs happened on Windows machines and required a WSL2/Linux tunnel rather than running the CUDA stack natively, and that one older-generation card outperformed a nominally newer one in the same family. Each observation was pushed toward "what would you do with that information" and "what would it take to convince a skeptic" rather than left as a passing remark.

### Sampling bias, taught through survivorship bias

A student's genuine intuition ("Intel machines held up better against the sample than I expected") became the anchor for a direct sampling-bias lesson: the WWII bomber armor-placement story (reinforcing returning planes' bullet-hole locations, when the correct move was reinforcing the *undamaged* locations on planes that never returned) was used to show that six machines physically present in one building cannot license a claim about GPU families in general — only about this specific, non-random fleet.

### Computing Commons pointer

The instructor pointed the class at the recently published Computing Commons podcast on resilience (course `24298`, Files), framed as a short, optional listen relevant to the course's broader posture toward setbacks — directly connected to the live troubleshooting failure that followed minutes later.

### Live, unstaged Podman/WSL2 failure

The instructor attempted to verify Podman/WSL2 on his own machine live, in front of the class, as this week's expected setup check. The attempt genuinely failed: Ubuntu would not finish launching, PowerShell hung, and an interrupt was required. Rather than debugging Windows internals live for the rest of the period, the instructor explicitly modeled the intended recovery posture: stop, don't force it, note that this is an administrative/platform-level wall (not a student skill gap), commit to filing a help desk ticket, and revisit next class. A quick poll of the room showed mixed results — some students had Podman/WSL2 working, several did not — and the instructor committed to following up.

### `fun_with_LaTeX`: AI-assisted setup, live and including a real mistake

The instructor switched to the public `fun_with_LaTeX` repository (course-linked, student-accessible) and used a chat AI tool live to extend a prior minimal example into something more complete. Notable teaching moments, all live and unstaged:

- The AI-generated setup script triggered an explicit safety warning before running, which the instructor called out as expected and correct behavior, not a bug to route around.
- The AI assistant, when asked to locate a folder, searched from *inside* that same folder and reported it missing — the instructor used the "using your phone as a flashlight to find your phone" framing to make the mismatch memorable, then corrected it live.
- LaTeX's two-pass build behavior was explained concretely: the first pass writes supporting files (such as a table of contents), which only render correctly once a second pass reads that file back in — a blank-looking first pass is expected, not a failure.
- The instructor closed the loop by asking the AI assistant to write a durable "how to use this folder" onboarding document directly into the repository, framing this as the actual payoff of AI assistance: not just getting an answer, but getting a durable artifact a future student (or future self) can read instead of re-deriving the same steps.
- The session ended with an explicit git-hygiene pass: `.gitignore` should exclude build byproducts like the compiled `main.pdf` rather than tracking regenerated output, and a messy git history from the session's experimentation was cleaned up live as a modeled practice, not left as clutter.

### Close

The instructor was explicit that this session was infrastructure/tooling-focused by design, and that the next class period moves directly into discrete mathematics and critical thinking content.

## Useful examples and timestamps

| Approx. time | Evidence / teaching move |
|---|---|
| 00:00–07:30 | Logistics; introduces the GPU Showdown table as today's live reasoning exercise |
| 07:30–10:30 | Cold start vs. warm start explained via the car-engine analogy, applied to GPU job queuing |
| 10:30–19:00 | Table reading: architecture-family counts, Windows/WSL2 caveat, generation-vs-performance anomaly |
| 19:00–24:30 | Sampling bias / survivorship bias (WWII bomber armor story) tied back to the six-machine sample |
| 24:30–26:00 | Pointer to the new Computing Commons resilience podcast |
| 26:00–35:00 | Live Podman/WSL2 verification attempt; genuine hang and interrupt; help-desk-ticket recovery framing; room poll |
| 35:00–47:00 | `fun_with_LaTeX` repo: AI-generated setup script, safety-warning step, running it |
| 47:00–55:00 | AI assistant's live folder-lookup mistake, corrected in real time |
| 55:00–63:00 | Two-pass LaTeX build explained; durable "how to use this folder" doc requested from the AI assistant |
| 63:00–70:00 | Git hygiene: `.gitignore` for build byproducts, cleaning up history; close and next-class pivot |

*(Timestamps are approximate, rounded to the nearest clean topic break in the transcript.)*
