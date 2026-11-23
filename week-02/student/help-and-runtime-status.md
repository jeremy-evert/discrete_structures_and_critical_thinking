# Week 2 Help and Runtime Status

This page separates source facts from local verification. It is intentionally conservative: an unverified capability is not presented as a student promise.

| Item | Status | Evidence / owner | Student implication |
|---|---|---|---|
| Shared local-AI explanation and readiness assignment | `SOURCE_BACKED` | `local_ai_lab_setup/curriculum/week2_module_manifest.yml` and `curriculum/shared/week2/` | Use the shared pages and `local-ai-readiness.md`; DSCT adds only its extension. |
| DSCT string-normalization extension | `SOURCE_BACKED` | `local_ai_lab_setup/curriculum/dsct/week2_extension.md` | Use the exact supplied request and four-part reflection. |
| Windows `Check` / `Baseline` / `Launch` / `Diff` / `Final` / `Reset -ConfirmReset` surface | `SOURCE_BACKED` | `windows_classroom/docs/week2_student_guide.md`, `scripts/week2_classroom.ps1` | Use only the documented commands in the supplied folder. |
| Local-AI model/configuration (`qwen3:8b`, loopback) | `SOURCE_BACKED` | `windows_classroom/scripts/student_agent.ps1` and shared architecture pages | Do not change the model, endpoint, or privacy boundary. |
| Target classroom Windows readiness on Aug 27 | `UNVERIFIED` | No live Windows classroom station was available during DSCT authoring | Instructor preflight decides the Tuesday/Thursday live branch. |
| Approved container runtime on target classroom stations | `UNVERIFIED` | No current required-repository container lesson or classroom runtime receipt found | Do not install or assume one; use the supplied receipt unless preflight verifies it. |
| Docker-syntax example and local base image | `UNVERIFIED` | DSCT-owned conditional example only; not a canonical classroom harness command | Instructor-demo only after verification; no image pull is promised. |
| Thursday supplied-receipt activity | `GO` | Tracked DSCT receipt, example, and run-of-show | All students can practice evidence reasoning without a runtime. |
| Cloud accounts, API keys, admin repair, network exposure | `SOURCE_BACKED` safety boundary | `local_ai_lab_setup/AGENTS.md`, shared safety page, Windows launcher | Never required for Week 2. |

## Help boundary

If a command fails, preserve the exact status/code and ask the instructor. A valid `NOT READY` or unavailable-runtime observation is useful evidence. Do not repair institutional infrastructure during class.
