# Thursday, August 27 — Containers and Repeatability

**Length:** 75 minutes
**Core question:** What additional claim is supported when an environment recipe makes a result reproducible?

## Preflight checklist

Run this on the classroom image or supplied station before class. This is an instructor check, not a student installation task.

- [ ] Record the Windows image/runtime date and station class without collecting student identifiers.
- [ ] Probe for an approved runtime (`docker` or another instructor-approved runtime); do not assume one exists.
- [ ] If using the executable path, verify the runtime can inspect the supplied base image locally and run the supplied example without an unannounced pull, admin prompt, cloud account, or network exposure.
- [ ] Confirm the exact command syntax selected for the day and mark it `VERIFIED` in the status page.
- [ ] If any item is unresolved, choose the supplied-receipt path. Do not make students install a runtime or fetch an image.
- [ ] Have the sanitized supplied receipt and the [repeatability receipt template](../student/thursday/repeatability-receipt.md) ready.

**Current Prompt 303 status:** the classroom container runtime and base-image availability are **UNVERIFIED** from this Linux authoring environment. Plan for the fallback unless the preflight above changes the status before class.

## Run of show — exactly 75 minutes

| Minutes | Segment | Core / flex | Instructor move and visible student evidence |
|---:|---|---|---|
| 0–8 (8) | Tuesday bridge | Core | Revisit `READY`, baseline, diff, and final. Ask why a passing test in one environment does not establish reproducibility in another. |
| 8–18 (10) | Recipe → image → container → output | Core | Use the supplied tiny example. Students name what changes at each arrow and write one supported claim plus one remaining limit. |
| 18–28 (10) | Inspect the recipe | Core | Read `Containerfile` and `repeatability_example.py`. Identify source, base image, working directory, copied input, command, and deterministic expected output. |
| 28–38 (10) | Preflight branch | Core | Announce `EXECUTABLE` only if verified; otherwise announce `SUPPLIED RECEIPT`. Show that a missing runtime is an environment fact, not a student reasoning failure. |
| 38–55 (17) | Run or reconstruct the observation | Core | Executable path: instructor-approved conditional commands, then capture output. Fallback: inspect the sanitized receipt and reproduce the reasoning from source and expected output. Label the evidence path. |
| 55–65 (10) | Compare evidence | Core | Pairs fill “supports / does not support” rows: recipe, image, running instance, output, passing check. Include “ran in a container” versus “conclusion is justified.” |
| 65–72 (7) | Receipt and challenge | Core | Students complete the repeatability receipt and challenge one overclaim in a partner's summary. No grading score is assigned here. |
| 72–75 (3) | Exit check and Week 3 bridge | Core | Collect the exit check. Close: explicit environments improve reproducibility evidence; they do not replace correctness reasoning. Formal Logic, Claims & Proof begins next week. |

## Executable path (conditional)

Use only if the preflight verifies both the runtime and local base image. The student guide marks these Docker-syntax commands as conditional instructor-demo commands; do not ask students to install Docker, pull an image, log in to a registry, or use elevation.

```powershell
# CONDITIONAL / INSTRUCTOR-DEMO ONLY — run only after preflight verification.
docker --version
docker image inspect python:3.12-slim
docker build --pull=false --tag dsct-week2-repeatability:local student\thursday\container-example
docker run --rm dsct-week2-repeatability:local
```

Expected output from the supplied example is a single deterministic summary such as `normalized=Ada Lovelace` followed by `check=PASS`. Record the exact observed output; do not claim a run occurred if the runtime was not verified.

## Fallback path

Use the sanitized supplied receipt when the runtime or base image is unavailable, when preflight is incomplete, or when a student machine cannot execute the conditional path. This proves that the student can inspect and reason about a supplied reproducibility record; it does not prove that the student's machine built or ran a container.

## Flex points

If the executable path is verified and quick, spend up to 5 flex minutes comparing a deliberate recipe change (for example, an unpinned base tag) and asking what new uncertainty it introduces. If the runtime is unavailable, spend those minutes on two overclaim rewrites. Do not turn the session into Docker administration.
