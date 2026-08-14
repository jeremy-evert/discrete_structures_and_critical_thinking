# DSCT Week 2 — Build the Lab, Then Make Results Reproducible

**Tuesday, August 25, 2026:** Building Your AI Lab
**Thursday, August 27, 2026:** Containers and Repeatability

Week 1 asked us to make reasoning inspectable with **Sources → Rules / Assumptions → Work → Check → One-Sentence Summary**. Week 2 applies the same habit to a technical environment and its evidence.

The recurring question is:

> What does this observation prove, and what does it not prove?

This week is a tooling and reproducibility bridge, not a second orientation week and not formal DSCT topic instruction. Week 3 begins the contracted **Logic, Claims & Proof** sequence.

## Student path

### Tuesday — Building Your AI Lab

1. Read the shared local-AI pages selected by the instructor.
2. Use the [DSCT Tuesday guide](student/tuesday/README.md) to trace the system and interpret `Check`.
3. If the classroom harness reports `READY`, complete the supplied `Baseline → Launch → Diff → Final` workflow.
4. If it reports accurate `NOT READY`, preserve that evidence and use the instructor/supplied-evidence branch.
5. Complete the [DSCT evidence/reflection receipt](student/tuesday/dsct-evidence-reflection.md) using the shared `local-ai-readiness.md` assignment as the canonical submission surface.
6. Use the [Tuesday exit check](student/tuesday/exit-check.md).

### Thursday — Containers and Repeatability

1. Inspect the tiny [repeatability example](student/thursday/container-example/).
2. Use the [Thursday guide](student/thursday/README.md) to distinguish a recipe, image, running container, output, and check.
3. Follow the instructor's preflight decision. The container run is conditional until a runtime and local base image are verified.
4. Complete the [repeatability evidence receipt](student/thursday/repeatability-receipt.md), either from the executable path or from the supplied receipt path. Label which path produced the evidence.
5. Use the [Thursday exit check](student/thursday/exit-check.md).

## Ownership boundaries

- `local_ai_lab_setup` owns the shared explanation, shared readiness assignment, evidence model, and DSCT extension.
- `windows_classroom` owns the Windows execution harness and exact `Check`, `Baseline`, `Launch`, `Diff`, `Final`, and `Reset -ConfirmReset` command surface.
- `computer_science_2` is a reference integration showing how a course wraps the shared module.
- DSCT owns this week's sequence, the connection to Reasoning Odyssey habits, the claim/evidence/limit reflections, and the bounded repeatability activity.

See [Week 2 source map](../planning/week-02-source-map.md) and [runtime/help status](student/help-and-runtime-status.md).

## Policy boundary

This package introduces no new DSCT points, weights, grading category, or due-date cadence. “Exit check” and “receipt” name learning evidence, not a claimed grading policy. Do not submit credentials, private data, full paths, or unrelated terminal history.
