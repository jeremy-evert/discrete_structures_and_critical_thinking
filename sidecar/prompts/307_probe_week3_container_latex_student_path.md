# Prompt 307 — Probe the Week 3 container + LaTeX student path

**Status:** FOREMAN-READY EMPIRICAL PROBE  
**Source quarry:** `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md`  
**Primary write scope:** DSCT report + bounded probe evidence only  
**Required report:** `sidecar/reports/307_week3_container_latex_student_path_probe.md`  
**Required run evidence:** `sidecar/runs/307_week3_container_latex_probe/`

## Direction already decided

The intended Week 3 runway is:

> **Containers + minimum-useful LaTeX**

LaTeX is an instrument for communicating mathematical and technical reasoning. Containers are an instrument for reproducible computational work. Neither Linux, Docker, nor TeX wizardry is the learning target.

The open question is empirical:

> **What is the smallest command-line understanding required to run, inspect, recover, and trust the reproducible environment we actually ask students to use?**

Prompt 307 gathers evidence for that decision. It does not make the policy decision.

## Decision explicitly NOT made

This prompt does not decide:

- whether students "must learn Linux";
- whether wrappers should hide almost all shell interaction;
- the final supported container runtime;
- the final LaTeX engine/toolchain;
- the final Week 3 lesson;
- the final Pair Reasoning exercise;
- whether local AI is required for recovery.

Those return to Jeremy + ChatGPT.

## Why this is Foreman-ready

The work is a bounded usability/reproducibility experiment. The worker must execute a student-like path, collect receipts, and report what knowledge the path actually demanded.

The Foreman is measuring the road, not choosing where the course should go.

## Safety and test constraints

Run only on environments already available to the worker.

Do not:

- install system software just to make a platform pass;
- require administrator/root access unless the currently intended student path already requires it, in which case report that as a finding;
- stop or reconfigure production services to simulate failure;
- mutate sibling repositories;
- publish live course content;
- claim support for an untested platform.

Use a disposable working directory or clearly bounded repo-local probe area. Preserve command/output receipts.

## Phase 1 — Establish the candidate path

Before executing anything, inspect current reusable sources that may already define or support the path, including where available:

- Container Foundations / container curriculum/templates;
- current DSCT toolchain material;
- Computer Architecture workbench/container evidence;
- `local_ai_lab_setup` / `windows_classroom` only where they materially affect the student environment;
- existing LaTeX/Tectonic/latexmk/TeX Live templates or receipts.

For each source used, record repository + commit SHA/ref + path.

Choose the **smallest plausible existing path** to probe. Do not invent a large new toolchain inside this prompt.

## Phase 2 — Record the test environment

For each environment actually tested, capture:

- OS and version;
- shell and version;
- container runtime and version, if present;
- container image/tag/digest or equivalent reproducibility identifier, if applicable;
- LaTeX engine/tool and version, if present;
- Python/tool versions only if used by the path;
- whether network access was required;
- whether admin/root privileges were required;
- whether any paid account/service was required;
- starting repository commit SHA.

Do not blur multiple platforms into one claim.

## Phase 3 — Execute the happy-path vertical slice

The probe must attempt a minimum useful student journey:

1. locate the supplied course/probe directory;
2. identify the supplied `.tex` source;
3. inspect/open the source using the normal student workflow;
4. make one small text edit;
5. add or change a small piece of mathematical notation relevant to DSCT;
6. compile using the candidate reproducible path;
7. locate the output PDF;
8. verify that a readable PDF was produced;
9. make a second small edit;
10. rerun the same path and verify that the output updates.

For every step record:

- exact command or UI action;
- expected result;
- observed result;
- whether shell knowledge was required;
- whether a wrapper/template hid shell detail;
- what concept the student still had to understand.

Store command/stdout/stderr receipts under `sidecar/runs/307_week3_container_latex_probe/`.

For generated PDFs, record at minimum file path, size, timestamp, and SHA-256 hash. Do not commit large/generated binary artifacts unless an existing repository convention explicitly calls for them.

## Phase 4 — Failure and recovery matrix

Test realistic, **safe** failures. At minimum probe these when the candidate path supports them:

### F1. Wrong working directory

Attempt the normal command from the wrong directory. Record:

- failure signal;
- what the student must notice;
- minimum recovery action;
- shell concept required.

### F2. Missing or misnamed source/path

Use a harmless wrong filename/path. Record the same evidence.

### F3. LaTeX source error

Introduce one bounded, reversible syntax error into the disposable probe source. Record:

- compiler/error output;
- whether the error points to a useful location;
- recovery steps;
- whether the student needs TeX-specific knowledge or only general error-reading habits.

### F4. Output-location confusion

Begin from the assumption that the student does not know where the generated PDF lands. Record what must be inspected or understood to find it.

### F5. Container/runtime invocation error

If safely testable without stopping services, use a harmless incorrect container/image/target invocation or equivalent bounded mistake. Do not disable or reconfigure the actual runtime merely to manufacture a failure.

If a failure case cannot be tested safely, mark it **NOT TESTED** with reason.

## Phase 5 — Wrapper versus raw-path comparison

Where an existing wrapper/template is available, compare:

- the normal student wrapper path;
- the underlying/raw command path only far enough to understand what the wrapper hides.

Classify observed knowledge into:

- **REQUIRED CONCEPTUAL KNOWLEDGE** — concepts students must understand even with perfect wrappers;
- **REQUIRED COMMAND/SHELL KNOWLEDGE OBSERVED** — shell operations the tested path genuinely requires;
- **RECOVERY-ONLY KNOWLEDGE** — not needed on the happy path but required when something breaks;
- **KNOWLEDGE WRAPPERS CAN HIDE SAFELY** — implementation detail with no demonstrated reasoning/recovery value;
- **TOOL-SPECIFIC KNOWLEDGE** — container/TeX details that may be avoidable if the toolchain changes.

Do not convert those observations into curriculum requirements. Report them.

## Phase 6 — Optional local-AI recovery observation

If a local AI assistant is already available without setup expansion, optionally use it on one or more failures.

For each AI-assisted recovery record:

1. the error/context given to the model;
2. the model's proposed action/explanation;
3. what was independently checked before acting;
4. whether the proposal worked;
5. whether a non-AI recovery path also existed.

AI may assist the experiment. It must not become the only demonstrated recovery route.

## Required report

Create `sidecar/reports/307_week3_container_latex_student_path_probe.md` containing:

1. starting commit SHA;
2. source/provenance inventory for the candidate path;
3. environment matrix;
4. happy-path step table;
5. failure/recovery matrix;
6. wrapper-versus-raw comparison;
7. observed knowledge classification;
8. optional AI-recovery findings;
9. untested platforms/claims;
10. explicit decisions returned to Jeremy + ChatGPT;
11. exact locations of run receipts;
12. verification/reproduction results.

## Hard stops

Do **not**:

- declare that DSCT now requires Linux command-line instruction;
- declare that students need no shell knowledge;
- choose the final container runtime;
- choose Tectonic vs latexmk/TeX Live or another engine as final doctrine;
- build a new container platform just to complete the probe;
- author final Week 3 student materials;
- decide final Pair Reasoning content;
- change grading;
- advertise an untested OS/platform as supported;
- treat AI-generated recovery advice as verification;
- write Canvas/Savnac.

## Verification battery

### A. Receipt completeness

Every **TESTED** happy-path and failure-path row must point to command/output evidence in the Prompt-307 run directory.

No "worked" claim without a receipt.

### B. Artifact verification

For each successful compile:

- confirm a PDF exists;
- record size and SHA-256;
- verify the second edit produces a changed output hash or equivalent evidence that recompilation incorporated the edit;
- visually or textually inspect the PDF enough to confirm it is readable and contains the intended bounded change, using available non-OCR tooling where possible.

### C. Clean rerun

From a fresh disposable working state, rerun the documented happy path once without improvising undocumented recovery steps.

If the second run requires undocumented knowledge, the path is not yet reproducible and must be reported as such.

### D. Privilege/dependency audit

Explicitly report whether the tested path required:

- admin/root;
- network access;
- a paid service/account;
- manual environment surgery;
- commands not present in the candidate student instructions.

Any hidden requirement is a finding, not something to conceal by fixing the machine.

### E. Scope audit

Run:

- `git diff --check`
- `git diff --name-only`

Only the required report, bounded Prompt-307 probe evidence, and disposable probe fixture files that are intentionally part of the receipt may remain changed. Do not alter course doctrine or sibling sources.

## Definition of done

Prompt 307 is complete only when:

1. at least one real candidate student path has been executed end to end on a named environment;
2. the happy path has reproducible command/output receipts;
3. realistic failure/recovery cases have been tested or explicitly marked not safely testable;
4. required conceptual, happy-path shell, recovery-only shell, wrapper-hidden, and tool-specific knowledge are separated;
5. successful compilation is verified by artifact receipts, not assertion;
6. a clean rerun succeeds or its failure is honestly documented;
7. hidden privilege/network/paid-service dependencies are surfaced;
8. platform support claims do not exceed the platforms actually tested;
9. the final Linux/container/LaTeX policy decision remains with Jeremy + ChatGPT.

The output should let Jeremy + ChatGPT answer the open Week 3 question from measured student-path evidence rather than intuition.