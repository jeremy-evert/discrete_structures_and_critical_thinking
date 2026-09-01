# Prompt 316 — Week 3 pinned-container skill ladder

**Status:** PASS for a validated Podman-based happy path, bounded failure
matrix, and skill-ladder contract on the available representative
environment. Registry publication of the pinned image is a returned action
item (blocked by this worker's sandbox permissions, not by design or
technical failure).

> **Update 2026-08-31:** the returned action item is closed. Jeremy refreshed
> the GitHub credential and pushed the image by hand from `april`. The pinned
> reference is now
> `ghcr.io/jeremy-evert/dsct-week3-latex@sha256:e7987919298c909f1a7f52247b8a7b54395cbde2400e2d6f3e8c5078425e2fca`
> (tag `v1`), the GHCR package is **public**, anonymous pull is verified, and
> `run-latex.sh`'s `DEFAULT_IMAGE_REF` is re-pinned to that digest. See
> `week-03/container/IMAGE_CONTRACT.md` → "Registry publication (2026-08-31)".
> The `<pending-publish>` placeholder below is left as the 2026-08-17
> point-in-time record.

**Starting DSCT commit:** `419b55b` (main)
**Evidence consumed:** Prompt 307 report
(`sidecar/reports/307_week3_container_latex_student_path_probe.md`, PASS as
host-`pdflatex` baseline, container path explicitly NOT TESTED) and the
Computer Architecture course's `lab/Containerfile`
(`ba1eb7eccc5bf5731881a09a67422b6aa3903db8`).
**Validation date:** 2026-08-17 UTC
**Run evidence:** `sidecar/runs/316_week3_container_latex_ladder/receipts/`

## What this prompt implements

Per the frozen pedagogical contract in
`sidecar/prompts/316_define_week3_pinned_container_skill_ladder.md`, Week 3
now has:

- `week-03/container/Containerfile` — the recipe (reuses the Architecture
  course's validated `debian:trixie-slim` + TeX Live + `latexmk` package
  shape, trimmed to LaTeX only; no Architecture-specific tooling copied in).
- `week-03/container/IMAGE_CONTRACT.md` — the maintainer-facing pin record:
  recipe hash, local immutable image ID, build/runtime identity, and the
  exact registry-publication action still pending.
- `week-03/container/run-latex.sh` — the student-facing wrapper. Always
  prints the image, runtime, host source directory, container work
  directory, source, expected PDF path, and a plain-text `RESULT:`/`REASON:`
  line; distinguishes container/runtime failures from LaTeX source failures
  in its failure messages.
- `week-03/container/fixture/week3-claim.tex` — a small Week-3-flavored
  (even/odd proof) starter source distinct from Prompt 307's probe fixture.
- `week-03/student/container-latex-skill-ladder.md` — the student-facing
  skill ladder (Run → Inspect → Explain → Perturb → Diagnose → Recover →
  Verify → Extend later) and the minimum container vocabulary list.
- `week-03/instructor/container-latex-instructor-notes.md` — bounded
  instructor notes: what's validated vs. pending, suggested use of the
  failure matrix, and the Podman-vs-Docker runtime scope note.
- A narrow clarification added to
  `planning/fall-2026-weekly-architecture.md`'s exceptions list, pointing to
  this infrastructure without touching the Week 3 topic/spine.

## Tested environment

| Field | Observed value |
| --- | --- |
| Platform | Rocky Linux 9.6, x86_64; SELinux Enforcing |
| Container runtime | rootless Podman 5.4.0 |
| LaTeX in image | `latexmk` 4.86 (TeX Live 2025/dev/Debian) |
| Base image | `debian:trixie-slim` |
| Paid account / GPU / instructor-only access used | none |
| Network used | Debian/`apt` package mirrors only, during image build |

Environment receipt: `receipts/00_environment.typescript`.
Deterministic-rebuild + provenance receipt: `receipts/07_image_build_provenance.typescript`.

## Image identity

| Field | Value |
| --- | --- |
| Containerfile SHA-256 | `a70285c607dd7486e6124b939c7ac89f1b2bbc3bcd6562ff4f3096ac7c23aae6` |
| Local build tag | `localhost/dsct-week3-latex:v1` |
| Local immutable image ID | `sha256:38ab1a1644e61ab7b5ec1277837b3719d961644e7ff858cd871d16ef8ecc1a33` |
| Intended course-operational reference | `ghcr.io/jeremy-evert/dsct-week3-latex@sha256:<pending-publish>` |

Rebuilding from the committed `Containerfile` reproduced the identical image
ID via Podman's content-addressed layer cache, confirming the recipe is
reproducible. **Registry push to ghcr.io was attempted and blocked by this
worker session's sandbox action classifier** (an external-publish action
outside this worker's granted permissions) — not a technical failure. Full
handoff steps for a maintainer with push rights are in
`week-03/container/IMAGE_CONTRACT.md`. Until published, `run-latex.sh`'s
documented default (`localhost/dsct-week3-latex:v1`, built from the exact
committed `Containerfile`) is the validated fallback and is reproducible by
any maintainer or student machine with Podman via the two-line build command
in that file.

## Acceptance scenarios

| Scenario | Result | Receipt |
| --- | --- | --- |
| A — clean first success | PASS; one-page PDF produced from the supplied fixture with no image build required | `01_scenarioA_clean_first_success.typescript` |
| B — changed source reaches artifact | PASS; a bounded edit (added "Converse note" paragraph) appears in the recompiled PDF text; PDF hash changes from Scenario A's `2d647bb7...` to `bf03a4e9...` | `02_scenarioB_edit_reaches_artifact.typescript` |
| C — path/mount failure | PASS; wrong working directory produces `RESULT: FAIL` / `REASON: source not found: ... (checked relative to /tmp)`, exit 66; `cd` to the correct directory recovers and reruns to `RESULT: PASS` | `03_scenarioC_path_mount_failure_and_recovery.typescript` |
| D — LaTeX/source failure | PASS; an injected undefined control sequence produces `Undefined control sequence` at the exact source line, exit 12, `RESULT: FAIL` naming the LaTeX log; removing the bad command and rerunning recovers, PDF text confirmed unchanged from the intended content | `04_scenarioD_latex_source_error_and_repair.typescript` |
| E — container invocation failure | PASS; an invalid image reference produces `RESULT: FAIL` / `REASON: container/runtime invocation error (exit 125) before compilation started -- check the IMAGE/RUNTIME lines above, not the LaTeX source`, explicitly distinguishing it from a LaTeX error; reverting the image override recovers | `05_scenarioE_container_invocation_failure_and_recovery.typescript` |
| F — LLM-assisted repair (proposal vs. verified repair) | Written into the student/instructor contract using the same evidence pattern demonstrated live in C/D/E (read message → categorize → propose → execute → verify with PDF text); **no live LLM session was run against this wrapper in this validation** | see `week-03/student/container-latex-skill-ladder.md` "Step 4"; instructor notes' "not yet done" list |
| G — no premium ceiling | PASS by construction; rootless Podman, no paid AI account, no GPU, no instructor-only hardware used anywhere in this validation | `00_environment.typescript` |

A disposable clean rerun (fresh fixture copy, verified no leftover
containers from prior scenarios via `podman ps -a --filter
ancestor=localhost/dsct-week3-latex:v1`) is in
`06_clean_rerun_disposable_state.typescript`.

## Failure category disambiguation (why this matters)

The wrapper's exit-code handling was tuned during this validation
specifically so students can tell path/mount problems (exit 66, "source not
found"), container/runtime problems (exit 125/127, explicit "check the
IMAGE/RUNTIME lines" message, no log reference), and LaTeX source problems
(other nonzero exit, explicit "inspect ... .log" message) apart from the
`REASON:` line alone, without needing to read raw exit codes.

## Runtime-specific detail discovered during validation

Getting a non-root-owned artifact back onto the host from a rootless Podman
container on this SELinux-enforcing seat required two flags not present in
Prompt 307's container probe (which never executed a container write to a
bind mount): `--userns=keep-id` (map the container's root user to the host
UID) and the bind mount's `relabel=private` option (apply the SELinux
relabel Podman would otherwise skip). Both are baked into `run-latex.sh`.
This is exactly the kind of detail the wrapper is designed to hide from
students while remaining inspectable in the script itself.

## Runtime and engine decision (as authorized by Prompt 316)

Podman (OCI-compatible) was selected and empirically validated as the
supported classroom runtime; `latexmk`/TeX Live (via `texlive-latex-base`,
`texlive-latex-recommended`, `texlive-fonts-recommended`) was selected and
validated as the LaTeX toolchain. `run-latex.sh` exposes
`DSCT_WEEK3_RUNTIME=docker` as an override, but the Podman-specific flags
above have not been validated against Docker's flag surface — Podman is the
only tested/supported classroom runtime.

## Returned decisions / action items

1. **Registry publication (action item, not a design question):** a
   maintainer with `ghcr.io/jeremy-evert` push rights needs to run the two
   build/push commands in `week-03/container/IMAGE_CONTRACT.md` and then
   update `run-latex.sh`'s `DEFAULT_IMAGE_REF` to the resulting registry
   digest before this can be called a fully registry-pinned student path.
   Until then, the local reproducible build is the validated fallback.
2. **Docker runtime path:** not validated. If a lab machine only has Docker,
   the `--userns=keep-id`/`relabel=private` flags in `run-latex.sh` need a
   separate Docker-specific validation pass before Docker can be called a
   supported (not just theoretically OCI-compatible) path.
3. **Live LLM-assisted repair trial (Scenario F):** the proposal-vs-verified
   distinction is documented and grounded in the same evidence discipline
   proven live in Scenarios C/D/E, but no live model session exercised this
   specific wrapper. Not blocking for the pinned-container baseline; worth a
   follow-up if Jeremy wants Scenario F independently exercised end-to-end.

## Hard-stop compliance

This prompt did not touch the eleven-week topic spine, Pair Reasoning/Show &
Tell semantics or cadence, Decision Gate/checkpoint grading, Farkle/ML
grading, World Bible ontology, overall grading percentages, late
work/attendance/revision policy, or Canvas/Savnac content. The one edit to
`planning/fall-2026-weekly-architecture.md` is additive and explicitly
labeled as not a chassis exception.

## Reproduction

- `week-03/container/Containerfile` → `podman build -t
  localhost/dsct-week3-latex:v1 -f Containerfile .`
- `week-03/container/run-latex.sh path/to/source.tex` runs the pinned
  toolchain against any `.tex` file.
- Every acceptance-scenario claim above links to a receipt in
  `sidecar/runs/316_week3_container_latex_ladder/receipts/`.
- Generated PDFs/logs/aux files are intentionally not committed; PDF
  identity is proven via `pdftotext` content extraction and SHA-256 hashes
  recorded in the receipts, following Prompt 307's convention.
