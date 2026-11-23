# DSCT Week 2 Source and Provenance Map

Prompt 303 source map for the two contracted meetings only. DSCT wrappers point to shared canonical material; shared prose and harness code are not copied here.

| DSCT need | Canonical owner | Exact source | DSCT use |
|---|---|---|---|
| Week 2 identity and dates | DSCT | `planning/fall-2026-spine.md`, `jeremy_task_tracking/questions/009_dsct_week2_identity.md` | Tuesday is Building Your AI Lab; Thursday is Containers and Repeatability; Week 3 remains Logic, Claims & Proof. |
| Week 1 reasoning method | DSCT | `week-01/student/reasoning-method.md` | Reused as the Tuesday/Thursday receipt structure. |
| AI verification stance | DSCT | `week-01/student/ai-verification-expectation.md` | Reused concretely as “Love AI more. Trust AI less.” |
| Shared learning objectives and safety | `local_ai_lab_setup` | `curriculum/shared/week2/02_learning_objectives_and_safety.md` | Tuesday guide/run-of-show points here; no duplication. |
| Shared local-AI architecture | `local_ai_lab_setup` | `curriculum/shared/week2/05_local_ai_architecture.md`, `06_ollama_models_and_hardware.md`, `07_aider_as_a_client.md`, `08_localhost_apis_and_local_vs_cloud.md` | Tuesday system mental model and role distinctions. |
| Shared readiness workflow | `local_ai_lab_setup` + `windows_classroom` | `curriculum/shared/week2/09_run_the_readiness_check.md`, `10_first_local_ai_interaction.md`, `11_troubleshoot_with_evidence.md`, `12_readiness_assignment.md` | Tuesday evidence sequence and NOT READY boundary. |
| DSCT bounded claim exercise | `local_ai_lab_setup` | `curriculum/dsct/week2_extension.md` | Exact string-normalization request, expected baseline/diff/final, four-part reflection. |
| Shared module sequencing | `local_ai_lab_setup` | `curriculum/week2_module_manifest.yml` (`dsct` sequence) | Confirms shared pages precede the DSCT extension and assignment. |
| Windows command names and behavior | `windows_classroom` | `docs/week2_student_guide.md`, `scripts/week2_classroom.ps1` | Exact `Check`, `Baseline`, `Launch`, `Diff`, `Final`, `Reset -ConfirmReset` surface. |
| Local-only launcher/model boundary | `windows_classroom` | `scripts/student_agent.ps1` | Confirms loopback-only launch and fixed `ollama_chat/qwen3:8b`; no cloud fallback. |
| Reference integration pattern | `computer_science_2` | `planning/week-02-local-ai-lab-integration.md`, `assignments/week-02-local-ai-readiness.md`, `reports/006_week2_local_ai_stitch.md` | Demonstrates thin wrapping and claim/evidence/limit crosswalking without copying. |
| Thursday concept and artifact | DSCT | `week-02/student/thursday/README.md`, `container-example/`, `repeatability-receipt.md` | Bounded recipe → image → container → output → check activity. |
| Thursday runtime decision | DSCT + instructor preflight | `week-02/instructor/thursday-run-of-show.md`, `student/help-and-runtime-status.md` | Docker syntax is conditional; fallback is the default until verified. |

## Container source search result

Before authoring Thursday, current source was searched across `computer_science_2`, `local_ai_lab_setup`, and `windows_classroom` for `container`, `Dockerfile`, `Containerfile`, `docker`, `podman`, `image`, `reproducible`, `repeatability`, and dependency pinning. No authoritative Week 2 classroom container lesson, runtime receipt, or student command surface was found. Existing mentions are conceptual or historical/experimental. Thursday therefore remains a small DSCT-owned lesson rather than an infrastructure extension.

## Non-duplication check

The DSCT package does not copy the shared Week 2 pages, shared rubric, or Windows harness. It links to them, states what students should notice, and owns only the DSCT sequence, reflection/exit artifacts, run-of-show, runtime status, and repeatability example.
