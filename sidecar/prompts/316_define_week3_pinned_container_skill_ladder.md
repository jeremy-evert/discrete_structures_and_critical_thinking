# Prompt 316 — Define the Week 3 pinned-container skill ladder

## Purpose

Turn the accepted Week 3 infrastructure direction into a bounded, evidence-backed course contract.

The design decision is now settled at the course level:

- **Students begin from a supplied, pinned, ready-to-run container image.**
- They are **not** required to build the image from scratch before they can succeed.
- Containers are not decorative infrastructure hidden behind the course. They are part of the practical computing reality students are learning to work inside.
- Using an LLM to help deploy, inspect, explain, or troubleshoot a container is legitimate and expected professional behavior.
- The learning goal is not memorizing container syntax. The learning goal is being able to get a known-good environment running, understand enough of what is happening to inspect it, notice when something is wrong, recover from bounded failures, and verify the result.
- Students should build deeper container skills on top of that successful baseline rather than paying an installation/configuration tax before the reasoning work begins.

Jeremy's governing metaphor for the skill ladder is essentially: start with a car that runs, then learn enough mechanical judgment to recognize when it is bent, put heat on the bumper, straighten it, and learn to brake sooner next time. Translate that into professional student-facing language, not the literal metaphor unless it genuinely improves instructor notes.

This prompt may implement and verify that settled direction. It must **not** silently choose unrelated course policy.

## Required evidence to consume

Read current `main` before editing.

Also consume the Prompt 307 empirical evidence. At the time this prompt was authored, the accepted Prompt 307 worker commit was:

`08501ab5a4da1201988919be0b754e33d11cdd55`

with report:

`sidecar/reports/307_week3_container_latex_student_path_probe.md`

and run evidence under:

`sidecar/runs/307_week3_container_latex_probe/`

If Prompt 307 has subsequently been promoted to `main`, use the promoted copy as current source. If it has not, inspect the named accepted worker commit rather than pretending the report exists on `main`.

Prompt 307 established, among other things:

- a successful host-`pdflatex` baseline;
- a one-command wrapper path;
- changed PDF artifact evidence;
- bounded failures for wrong working directory, missing/misnamed source, LaTeX source error, output-location confusion, and container/runtime invocation error;
- the useful distinction between conceptual knowledge, required shell knowledge, recovery-only knowledge, and details wrappers may safely hide;
- **no tested containerized LaTeX happy path yet**;
- no final runtime/image/engine choice.

Use those limits honestly.

Also inspect relevant current DSCT Week 3 planning/source surfaces and the reusable Computer Architecture container/LaTeX design identified by Prompt 307. Reuse ideas where justified, but do not copy architecture-specific course semantics into DSCT.

## Frozen pedagogical contract

### 1. Known-good first success

The official Week 3 student path must begin with a **supplied OCI-compatible image pinned immutably**, preferably by digest in the operational contract.

The student should be able to move from repository checkout to a successful containerized compile/run with a small documented command sequence and no requirement to author a `Containerfile` first.

A mutable floating tag by itself is insufficient for the reproducibility claim.

### 2. Container is visible, not magical

Do not hide the entire container layer behind an opaque launcher.

A helper script or wrapper is allowed and encouraged where it removes irrelevant flag plumbing, but the student experience must still make these facts inspectable:

- which image is being used;
- that the image is pinned;
- which local source/work directory is mounted or exposed to the container;
- where the output artifact appears;
- whether the command succeeded or failed;
- enough of the invocation/log/error to reason about recovery.

The student does not need to memorize every raw runtime flag.

### 3. LLM use is normal, verification is mandatory

Week 3 should explicitly permit and normalize using an LLM to help:

- explain the supplied container command;
- adapt an invocation to the documented supported runtime;
- interpret an error message;
- propose a recovery step;
- explain a bind mount, working directory, image reference, source path, or output path;
- suggest a bounded diagnostic command.

But the course doctrine remains:

**Love AI more. Trust AI less.**

An LLM-proposed deployment or repair is not success. The student must execute it, inspect the result, and use evidence to decide whether the environment/artifact is actually correct.

### 4. Skill ladder

Build the Week 3 experience around a progression like this:

1. **Run** — launch the supplied pinned environment and produce the intended artifact.
2. **Inspect** — identify the image, source path, mounted/work path, output path, exit result, and resulting artifact.
3. **Explain** — in plain language, explain what the container command is doing at the level needed for the course.
4. **Perturb** — encounter or introduce one or more bounded failures.
5. **Diagnose** — use the error/output and, when useful, an LLM to propose a repair.
6. **Recover** — fix the issue and rerun.
7. **Verify** — prove the repaired run produced the intended result rather than merely exiting without an obvious complaint.
8. **Extend later** — deeper container skills may be added later, including inspecting or modifying a container recipe and eventually building an image, but those are not prerequisites for the first Week 3 success.

### 5. Minimum container literacy

The Week 3 contract should teach the smallest durable concepts that make later recovery possible. At minimum, students should leave able to distinguish, in practical terms:

- image versus running container;
- pinned image identity versus a floating label/tag;
- host path versus container path;
- source/input versus generated output;
- current working directory and why relative paths fail;
- mounted/bind-mounted work versus files trapped only inside a disposable container;
- success versus a nonzero/error result;
- rerun/reproduce after a repair.

Do not turn this into a general container administration course.

### 6. Failure/recovery is first-class

The student path must include bounded recovery work. Prompt 307's failure matrix is a strong starting point.

At least one container-specific failure must be real rather than simulated prose. Useful candidates include:

- wrong host working directory;
- wrong source or mount path;
- wrong container-side working path;
- output written somewhere the student did not expect;
- invalid entrypoint/command;
- incorrect image reference or intentionally substituted known-bad reference, if this can be done safely and reproducibly;
- malformed source that causes the in-container toolchain to fail.

The student should not be rewarded for causing maximum chaos. The point is controlled diagnosis and recovery.

### 7. LaTeX is an instrument

Week 3 also establishes minimum-useful LaTeX, but LaTeX configuration trivia is not the course objective.

The container should own the chosen LaTeX toolchain once that toolchain has been empirically validated.

Students should work with a small `.tex` source, make a meaningful edit, compile it in the container, inspect the PDF, and verify that the rendered artifact reflects the source change.

The source path and output PDF path should remain visible enough to support recovery.

### 8. Equality and ordinary hardware

The official path must not depend on a paid AI subscription, premium hardware, GPU access, or an instructor-only machine.

A student using the supported ordinary path must have the same reasoning ceiling as a student with stronger local hardware or paid tools.

## Empirical work required before claiming the path is ready

Do not promote an untested container happy path merely because the design decision is settled.

Perform a bounded empirical validation of the proposed official path on an available representative environment.

The validation should preserve receipts for:

1. runtime/version/environment identity;
2. exact pinned image reference and immutable digest;
3. image availability/pull/build provenance;
4. first successful containerized compile;
5. artifact location and inspection;
6. bounded source edit;
7. second compile proving the changed source reached the PDF;
8. at least the essential path/mount/container-invocation/source-error failure cases;
9. recovery after those failures;
10. a clean rerun from fresh/disposable state;
11. commands/output sufficient for another maintainer to reproduce the claim.

If the chosen image/toolchain must first be built and published by the course team, that is allowed. Students still receive the pinned ready-to-run result. Preserve the recipe and provenance so the image is reproducible by maintainers even though students are not required to build it in Week 3.

## Runtime and engine boundary

Do **not** choose a runtime or LaTeX engine by taste alone.

Prompt 307 returned these as empirical decisions because the container happy path was not tested.

Tara may select and test a reasonable candidate path based on current supported course/lab reality and reusable repository evidence. Prefer an OCI-compatible design that does not unnecessarily couple course semantics to one vendor.

If multiple runtimes can consume the same image but only one is the supported classroom path, document that distinction clearly.

If the candidate cannot be validated on the intended/representative environment, stop the unsupported claim and return the exact missing evidence rather than writing aspirational student instructions.

## Expected implementation surfaces

Inspect before editing. Likely relevant surfaces include:

- Week 3 planning/student/instructor material if present;
- `planning/fall-2026-weekly-architecture.md` where only a narrow infrastructure clarification is needed;
- a bounded Week 3 container/LaTeX contract or student path;
- scripts/wrappers/Containerfile/image metadata needed for the tested path;
- evidence under `sidecar/runs/316_*`;
- report `sidecar/reports/316_week3_pinned_container_skill_ladder.md`.

Do not opportunistically rewrite unrelated weeks.

## Acceptance tests

The finished work must demonstrate all of these scenarios.

### Scenario A — clean first success

A student with the documented prerequisites uses the supplied pinned image and documented command path to produce the expected PDF/artifact without first writing/building a container image.

### Scenario B — changed source reaches artifact

The student edits a bounded `.tex` source, reruns the containerized toolchain, and proves the resulting PDF reflects the edit.

### Scenario C — path or mount failure

A realistic path/mount/working-directory mistake produces an inspectable failure or wrong result, the student diagnoses it, repairs it, reruns, and verifies recovery.

### Scenario D — tool/source failure

A bounded LaTeX/source error occurs inside the supplied environment. The student reads useful evidence, repairs the source, and verifies the corrected artifact.

### Scenario E — container invocation failure

A bounded container-specific invocation problem occurs. The student can distinguish the container/runtime problem from a mathematical or LaTeX-content problem and recover.

### Scenario F — LLM-assisted repair

A plausible LLM suggestion can be used as part of diagnosis or deployment, but the final student evidence explicitly distinguishes **proposal** from **verified repair**.

### Scenario G — no premium ceiling

The documented ordinary path completes without a paid AI account, premium hardware, or instructor-only access.

## Hard stops

Do not use this prompt to decide or change:

- the eleven-week formal DSCT topic spine;
- Pair Reasoning or Show & Tell semantics/cadence;
- Decision Gate or checkpoint grading policy;
- Farkle/ML grading policy;
- World Bible ontology;
- overall grading percentages;
- late work, attendance, revision/resubmission, or drop-lowest policy;
- Canvas or Savnac content;
- unrelated cross-course infrastructure standards.

If implementing the tested Week 3 path exposes a genuine course-level fork not resolved above, preserve the evidence and return the smallest concrete question to Jeremy + ChatGPT.

## Git discipline

- Pull/fetch current state before work.
- Inspect before editing.
- Keep Prompt 316 bounded.
- One logical change per commit with clear messages.
- Preserve evidence receipts.
- Do not perform unrelated cleanup.
- Push the completed bounded work and report exact commits, paths, validation results, and any returned decision seams.
