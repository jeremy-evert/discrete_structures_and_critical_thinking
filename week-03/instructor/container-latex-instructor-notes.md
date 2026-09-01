# Week 3 container/LaTeX instructor notes

Scope: this note supports the student path in
`week-03/student/container-latex-skill-ladder.md`. It does not set grading
weights, cadence, or Decision Gate policy — see the hard stops in Prompt
316's spec (`sidecar/prompts/316_define_week3_pinned_container_skill_ladder.md`).

## The one-sentence framing

Students start with a car that runs. The goal is not memorizing container
syntax; it is building enough mechanical judgment to notice when something
is bent, apply a bounded repair, and verify the result — then, over time,
learning to avoid the mistake earlier. Use professional language with
students ("known-good baseline," "bounded failure," "verify, don't assume")
rather than the literal car metaphor unless it clearly lands better with a
given section.

## What is validated vs. what is a returned decision

Validated on this seat (rootless Podman 5.4.0, Rocky Linux 9.6): image
build, Scenario A (clean first success), Scenario B (edit reaches artifact),
Scenario C (path/mount failure + recovery), Scenario D (LaTeX source error +
repair), Scenario E (container/runtime invocation failure + recovery), a
disposable clean rerun, and no premium-hardware/paid-account dependency
(Scenario G). See `sidecar/reports/316_week3_pinned_container_skill_ladder.md`
for the full report and `sidecar/runs/316_week3_container_latex_ladder/` for
receipts.

**Done (2026-08-31):** the validated image is published to
`ghcr.io/jeremy-evert/dsct-week3-latex` (tag `v1`, digest
`sha256:e7987919298c909f1a7f52247b8a7b54395cbde2400e2d6f3e8c5078425e2fca`),
the GHCR package is **public**, anonymous pull is verified, and
`run-latex.sh`'s `DEFAULT_IMAGE_REF` is re-pinned to that digest. Jeremy
refreshed the GitHub credential and ran the push by hand from `april` (the
automated worker was classifier-blocked from pushing). See
`week-03/container/IMAGE_CONTRACT.md` → "Registry publication (2026-08-31)"
for the full record and the offline-fallback override.

**Not yet done:** a live LLM-assisted repair trial (Scenario F) — the
skill-ladder doc's guidance on distinguishing an AI *proposal* from a
*verified repair* is written from the same evidence pattern demonstrated in
Scenarios C/D/E (read the message, decide the category, fix it yourself,
verify with the PDF), but no live model session was run against this
specific wrapper.

## Worked example available for in-class use

`lectures/ai_reasoning_latex_from_data/` (compiled report:
`final/build/main.pdf`) is a real, evidence-backed worked example of
claim/evidence/assumptions/check/confidence, built on a local-model GPU
concurrency benchmark and tied to DSCT via an ordering relation and a
product-rule count. It is linked from the student skill-ladder doc as
required reading before Step 1. Useful if you want a second concrete
instance of "a clean run is not proof" beyond the container wrapper itself
-- the overlap-factor check in that report and the "verify the PDF content,
not the exit code" instruction in Step 4 below are the same move.

## Suggested in-class use of the failure matrix

Any of Scenarios C, D, or E can be assigned as a "find the bug" exercise
without telling students in advance which category it is — the point is
recognizing *from the wrapper's own output* which of the three failure
families (path/mount, container/runtime, LaTeX source) they are looking at,
not memorizing a fixed list of error strings.

## Runtime scope note

`run-latex.sh` currently targets rootless Podman specifically
(`--userns=keep-id` and SELinux `relabel=private` on the bind mount were
both required to get a working, non-root-owned artifact on this Rocky Linux
seat). If a lab machine runs Docker instead, `DSCT_WEEK3_RUNTIME=docker` is
exposed as an override, but the Podman-specific flags have not been
validated against Docker's flag surface. Treat Podman as the supported
classroom runtime until a Docker path is separately tested.
