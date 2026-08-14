# Tuesday, August 25 — Building Your AI Lab

**Length:** 75 minutes
**Core question:** What does each local-AI observation prove, and what does it not prove?

## Before class

- Read the canonical shared pages `local_ai_lab_setup/curriculum/shared/week2/01_start_here.md`, `02_learning_objectives_and_safety.md`, `05_local_ai_architecture.md`, `09_run_the_readiness_check.md`, `10_first_local_ai_interaction.md`, `11_troubleshoot_with_evidence.md`, and `12_readiness_assignment.md`.
- Read `local_ai_lab_setup/curriculum/dsct/week2_extension.md` and the DSCT [student guide](../student/tuesday/README.md).
- Use `windows_classroom/docs/week2_student_guide.md` and `scripts/week2_classroom.ps1` as the command authority. Do not substitute commands from memory.
- Have one sanitized instructor/supplied evidence set ready for the NOT READY branch and one READY demonstration if classroom readiness is mixed.
- Keep the [help/runtime status page](../student/help-and-runtime-status.md) visible.

## Run of show — exactly 75 minutes

| Minutes | Segment | Core / flex | Instructor move and visible student evidence |
|---:|---|---|---|
| 0–7 (7) | Week 1 bridge | Core | Revisit Sources → Rules / Assumptions → Work → Check → Summary and “Expected / Actual / Tried.” Students predict why a green tool check cannot certify a correct answer. |
| 7–17 (10) | Architecture mental model | Core | Draw Student → Aider → localhost → Ollama → `qwen3:8b` → response/change. Students label PowerShell, Python, Git, Aider, Ollama, model, and localhost by role. |
| 17–25 (8) | Safety and privacy boundary | Core | State: no installation, model download, cloud account, API key, admin repair, or network exposure. Students identify one safe stop/escalate condition. |
| 25–35 (10) | Guided `Check` | Core | Run the exact source-backed Windows command from the supplied folder. Pause at each row: command, service, model, inference, or exercise. Record `READY` or accurate `NOT READY` plus the first `W2-...` code. |
| 35–43 (8) | Baseline as a claim test | Core | In a READY demonstration, run `Baseline`. Ask: what claim is challenged by the failing title-case assertion? Students write the baseline observation and limit. |
| 43–55 (12) | Bounded `Launch` or supplied evidence | Core | READY students use the exact DSCT extension request in the supplied exercise. NOT READY students inspect a sanitized supplied transcript/diff and mark it as demonstration evidence, not their machine's readiness evidence. |
| 55–63 (8) | `Diff` inspection | Core | Run `Diff` in the READY path. Students compare expected and actual: `student_code.py` only, `.upper()` → `.title()`. Ask what the diff establishes and leaves open. |
| 63–71 (8) | Independent `Final` and reflection | Core | Run `Final` in the READY path. Students complete claim, baseline/counterexample, diff, and limit in the DSCT receipt; NOT READY students use the supplied result and explicitly mark the source. |
| 71–75 (4) | Exit check and transition | Core | Collect the five-question exit check or oral equivalent. Close: Week 1 made reasoning visible; Week 2 makes environment/evidence reproducible; Week 3 applies the habits to formal logic, claims, and proof. |

## Branch rules

### READY branch

Students may execute `Baseline`, the exact bounded `Launch`, `Diff`, and `Final` commands from the Windows guide. A completed Aider request is a proposal; acceptance requires reading the diff and running the independent final test.

### Accurate NOT READY branch

Do not turn setup failure into student failure. Students record the exact status/code, stop at the safe boundary, and work from the sanitized instructor receipt. They may answer all reasoning questions except claims about their own machine. Their receipt must say `SUPPLIED DEMONSTRATION EVIDENCE`, not `my machine was READY`.

### Flex points

If the class is mixed, shorten the architecture drawing to 6 minutes and add 4 minutes to the evidence comparison. If all students are NOT READY, replace live `Baseline`/`Launch`/`Diff`/`Final` with the instructor receipt and spend the protected time on claim/evidence/limit analysis. Do not spend flex time on repair clinics.

## Exit evidence

Each student leaves with a privacy-reviewed DSCT reflection receipt and an exit response. The shared submission remains the canonical `local-ai-readiness.md`; DSCT adds the four labeled reflection parts in the shared assignment's `### Course-specific reflection` section.
