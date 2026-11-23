# Prompt 306 — Week 2 shared AI Lab reuse map

## Worker scope and conclusion

This is a source-cited archaeology report, not a Week 2 design. The evidence
supports a three-owner model: `local_ai_lab_setup` owns the shared teaching
spine and assignment contract; `windows_classroom` owns the Windows command
and runtime harness; each course repository owns its sequencing and course
extension. DSCT should write a thin course wrapper around those owners and
should not fork the shared pages or command surface.

The evidence loop is substantially present in the shared sources and CS2
crosswalk. The important qualification is that the classroom `READY` path and
real Aider execution are not demonstrated on this Linux host; those claims
remain source-coherent or prior-receipt claims, not `EXECUTED-NOW` claims here.

## Evidence base

The DSCT working copy began at `2483083a114b70f16ae6b696cef7fec5d3bdd46a`
(`2483083`, `origin/main`). The protected untracked root prompt
`prompts/305_week2_assessment_contract_reconciliation.md` was left alone in
the source checkout. External refs were independently resolved as follows:

| Repository | Ref inspected | Exact commit | Relevant evidence paths |
|---|---|---|---|
| `local_ai_lab_setup` | `main` | `b2b2ec1afcea98c59a5ab3818cd361a29eb0f99c` | `curriculum/shared/week2/01_start_here.md`–`12_readiness_assignment.md`, `curriculum/shared/week2/readiness_assignment_rubric.md`, `curriculum/cs2/week2_extension.md`, `curriculum/dsct/week2_extension.md`, `docs/readiness_report_spec.md` |
| `windows_classroom` | `main` | `f87e340aad4bf4e4e2c064abc676afdcc5260b48` | `scripts/week2_classroom.ps1`, `scripts/student_agent.ps1`, `docs/week2_student_guide.md`, `docs/week2_instructor_runbook.md`, `tests/`, `configs/ollama_inference_baseline.json` |
| `computer_science_2` | `origin/main` after fetch | `5c3c83db7a7b4cd84adf5de80c6b728f16cf6c9d` | `planning/week-02.md`, `planning/week-02-local-ai-lab-integration.md`, `assignments/week-02-local-ai-readiness.md`, `assignments/odyssey_gates/week-02.md`, `rubrics/odyssey_gates/week-02_rubric.md` |
| `computer_architecture` | `main` | `ba1eb7eccc5bf5731881a09a67422b6aa3903db8` | `planning/week-02.md`, `docs/grading-model.md`, `weeks/week-12/monday.md`, `weeks/week-12/friday.md`, `weeks/week-16/friday.md` |
| DSCT | `main` / `origin/main` | `2483083a114b70f16ae6b696cef7fec5d3bdd46a` | `week-02/`, `sidecar/reports/304_pair_reasoning_name_reconciliation.md`, `sidecar/reports/305_reasoning_vocabulary_inventory.md`, `sidecar/prompts/306_map_week2_shared_ai_lab_reuse.md` |

`computer_science_2` local `main` was `a14a1efb6bea3de455e1304fb7e07eb5c2ccb1b0`
and reported `[behind 36]`; it was not used as current truth. `origin/main`
was fetched and used instead.

## Ownership table

| Role/artifact | Owning repository and exact source | Artifact type | Disposition | Reason |
|---|---|---|---|---|
| Shared student-facing AI Lab | `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/01_start_here.md` through `12_readiness_assignment.md` | Instruction | **POINTER / REUSE CANONICAL** | The shared sequence explicitly serves every Week 2 course and separates observations from claims. |
| Readiness assignment | `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/12_readiness_assignment.md` | Assignment | **POINTER / REUSE CANONICAL** | One privacy-reviewed `local-ai-readiness.md` contract already exists. |
| Readiness rubric | `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/readiness_assignment_rubric.md` | Rubric | **POINTER / REUSE CANONICAL** | Shared scoring checks status, interpretation, components, reflection, and privacy. |
| Windows runtime harness | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`, `scripts/student_agent.ps1` | Code/harness | **POINTER / REUSE CANONICAL** | The command surface and local-only enforcement belong to the classroom runtime repository. |
| `Check` | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`; described in `docs/week2_student_guide.md` | Harness + instruction | **POINTER / REUSE CANONICAL** | `Check` is the gate for tool, API, model, configuration, and exercise readiness. |
| `Baseline` | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`; exercise contract from `local_ai_lab_setup@b2b2ec1` — `curriculum/cs2/week2_extension.md` | Harness + course extension | **ADAPT FOR DSCT** | The command is shared; the bounded exercise and expected failure are course-specific. |
| Bounded AI proposal / launch | Harness `windows_classroom@f87e340a` — `scripts/student_agent.ps1`; shared client explanation `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/07_aider_as_a_client.md` | Harness + instruction | **ADAPT FOR DSCT** | Aider/local model mechanics are shared; DSCT must later choose its own bounded request. |
| `Diff` | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`; shared review instruction `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/10_first_local_ai_interaction.md` | Harness + instruction | **POINTER / REUSE CANONICAL** | The actual diff capture and inspect-before-accept habit are reusable. |
| Independent `Final` | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`; shared contract `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/10_first_local_ai_interaction.md` | Harness + instruction | **ADAPT FOR DSCT** | The independent command is canonical; its fixture/test expectation must match the later DSCT exercise. |
| Reset/recovery | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`, `docs/week2_instructor_runbook.md` | Harness + safety contract | **POINTER / REUSE CANONICAL** | Reset is intentionally limited to a disposable exercise and requires confirmation. |
| Troubleshooting/evidence chain | `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/11_troubleshoot_with_evidence.md` | Instruction | **POINTER / REUSE CANONICAL** | The claim → observation → diagnostic → bounded action → rerun → escalate chain is generic. |
| CS2 sequencing/wrapper | `computer_science_2@5c3c83d` — `planning/week-02.md`, `planning/week-02-local-ai-lab-integration.md`, `assignments/week-02-local-ai-readiness.md` | Course wrapper | **COURSE-SPECIFIC / DO NOT COPY** | CS2 owns when/why the shared module appears and its `format_student_name` extension. |
| CS2 bounded extension | `local_ai_lab_setup@b2b2ec1` — `curriculum/cs2/week2_extension.md` | Course extension | **COURSE-SPECIFIC / DO NOT COPY** | The title-case exercise is evidence of a reusable pattern, not DSCT's selected exercise. |
| Computer Architecture epistemic framing | `computer_architecture@ba1eb7e` — `planning/week-02.md`; reinforcing examples in `weeks/week-12/monday.md` and `weeks/week-16/friday.md` | Course framing | **ADAPT FOR DSCT** | “AI may propose; evidence decides” and revision-after-evidence are portable principles, but Architecture's weekly frame and grade model are not DSCT content. |
| Existing DSCT Week 2 package | DSCT historical `85ea3a2cf446d2168d1d8210e297bf067389d51c` — `week-02/`, `reports/303_week2_ai_lab_containers_repeatability.md` | Course source/report | **STALE / SUPERSEDED** | It is a container/repeatability package, while Prompt 306's settled identity is Building Your AI Lab and the shared Windows path is now canonical. |
| DSCT current assessment fixtures | DSCT historical `e209a63d5f1c3021aae38f4d9d7831bb2122ae8c` — `assessment/week-02-readiness-assessment-contract.yaml`, `assessment/fixtures/week-02/` | Assessment contract/fixtures | **ADAPT FOR DSCT** | Useful evidence-boundary fixtures may inform later authoring; they do not replace the shared readiness assignment or decide pedagogy. |

## Reuse-disposition matrix and duplication audit

| Candidate | Provenance | Disposition | Reason / duplication finding |
|---|---|---|---|
| `curriculum/shared/week2/*` | `local_ai_lab_setup@b2b2ec1`, paths above | **POINTER / REUSE CANONICAL** | DSCT should link to these pages. Copying them would create a second shared-module owner. |
| `scripts/week2_classroom.ps1` and `student_agent.ps1` | `windows_classroom@f87e340a` | **POINTER / REUSE CANONICAL** | DSCT should invoke the command surface; it should not reimplement it. |
| `curriculum/cs2/week2_extension.md` | `local_ai_lab_setup@b2b2ec1` | **COURSE-SPECIFIC / DO NOT COPY** | The string-normalization request is explicitly not selected for DSCT. |
| CS2 crosswalk and readiness pointer | `computer_science_2@5c3c83d` — `planning/week-02-local-ai-lab-integration.md`, `assignments/week-02-local-ai-readiness.md` | **ADAPT FOR DSCT** | The ownership pattern is reusable; CS2 timing, Coding Odyssey language, and grading references are not. |
| Architecture Week 2 “AI proposes, evidence decides” | `computer_architecture@ba1eb7e` — `planning/week-02.md` | **ADAPT FOR DSCT** | Keep the epistemic distinction; do not import Architecture's schedule, grade model, or machine-dossier context. |
| DSCT `week-02/` container/repeatability surfaces | `DSCT@85ea3a2` | **STALE / SUPERSEDED** | Historical evidence only until a later author decides what, if anything, survives. No merge or cleanup was performed. |
| DSCT Week 2 assessment fixtures | `DSCT@e209a63` | **ADAPT FOR DSCT** | They encode evidence-quality edge cases, but Prompt 306 does not authorize changing the assessment contract. |
| DSCT `week-02` current source | `DSCT@2483083` — `week-02/`, `week-02/README.md` | **OPEN PEDAGOGICAL CHOICE** | Existing source must be compared with the shared module before authoring; this map does not choose the final student sequence. |
| DSCT final bounded exercise | No source yet | **MISSING** | The infrastructure loop exists, but the DSCT-specific claim/request/fixture is intentionally returned to Jeremy + ChatGPT. |

The main duplication seam is not a demonstrated duplicate of the shared pages
on current DSCT `main`; it is the historical DSCT `week-02/` package and its
container/repeatability assumptions alongside a separate shared Windows lab.
Later authoring should retire or explicitly supersede any conflicting
container path rather than silently maintain two Week 2 runtimes.

## Evidence-loop continuity

| Stage | Owner/source | Artifact type | Current tier | What is established / limitation |
|---|---|---|---|---|
| Check | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`; `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/09_run_the_readiness_check.md` | Harness + instruction | **VALIDATED-BY-RECEIPT** for the source package; **UNVERIFIED** for this host | Prior Windows receipts are present under `windows_classroom/runs/20260810T...`; this worker did not run PowerShell/Windows. |
| Baseline | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`; exercise/extension `local_ai_lab_setup@b2b2ec1` — `curriculum/cs2/week2_extension.md` | Harness + course extension | **SOURCE-COHERENT** | The command runs the supplied unittest suite and the CS2 extension defines an intentional title-case failure. No DSCT-specific baseline is selected. |
| Bounded AI proposal / launch | `windows_classroom@f87e340a` — `scripts/student_agent.ps1`; `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/07_aider_as_a_client.md` | Harness + instruction | **SOURCE-COHERENT** | Local model, loopback endpoint, and bounded request are specified. Real classroom execution is not demonstrated here. |
| Diff | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`; `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/10_first_local_ai_interaction.md` | Harness + instruction | **VALIDATED-BY-RECEIPT** | Windows run receipts include `raw/commands/020_fixture_git_diff.*`; the shared contract states one-file review. DSCT's exact expected diff remains open. |
| Final | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`; shared instruction same as above | Harness + instruction | **VALIDATED-BY-RECEIPT** | Windows run receipts include `raw/commands/021_fixture_final_test.*`; this does not validate a future DSCT fixture. |
| Read/reason | `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/10_first_local_ai_interaction.md`, `11_troubleshoot_with_evidence.md`; Architecture `ba1eb7e` — `planning/week-02.md` | Instruction | **SOURCE-COHERENT** | Sources require distinguishing generated proposal, observation, evidence, and inference. |
| Accept/reject from evidence | `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/10_first_local_ai_interaction.md`; CS2 wrapper `computer_science_2@5c3c83d` — `planning/week-02-local-ai-lab-integration.md` | Instruction + course wrapper | **SOURCE-COHERENT** | Baseline, diff, final test, and code reading are named as the acceptance evidence. DSCT's object remains unchosen. |
| Reset/recovery | `windows_classroom@f87e340a` — `scripts/week2_classroom.ps1`, `docs/week2_instructor_runbook.md` | Harness + safety contract | **VALIDATED-BY-RECEIPT** | Prior Windows post-reset receipts include `runs/20260810T220200Z_prompt013_wrapper_acceptance_pass/raw/post_reset_check.stdout.txt` and `raw/final_reset.json`. |
| Readiness/reflection receipt | `local_ai_lab_setup@b2b2ec1` — `curriculum/shared/week2/12_readiness_assignment.md`, `readiness_assignment_rubric.md`; CS2 wrapper at `computer_science_2@5c3c83d` | Assignment + rubric + wrapper | **SOURCE-COHERENT** | The report filename, shared questions, privacy preview, and course-specific reflection slots are explicit. Canvas/Savnac publication is not established. |

No tier above `SOURCE-COHERENT` is inferred from prose alone. The exact prior
receipt paths above are the reasons the corresponding harness stages are
`VALIDATED-BY-RECEIPT`; they are not evidence that this worker re-ran them.

## Historical and incoming DSCT Week 2 archaeology

No branch was merged, cherry-picked, or modified. The relevant refs found were:

| Ref | Exact commit | What it contains | Salvage / stale seam |
|---|---|---|---|
| `origin/agent/prompt303-dsct-week2` | `85ea3a2cf446d2168d1d8210e297bf067389d51c` | `week-02/` student/instructor package, container example, repeatability receipt, source maps, runtime receipts | Salvage the evidence-oriented inventory and explicit receipts if useful; stale assumption is that DSCT should own a container/repeatability runtime for this Week 2 lab. |
| `origin/agent/prompt305-dsct-assessment` | `e209a63d5f1c3021aae38f4d9d7831bb2122ae8c` | Week 2 readiness assessment contract and evidence-quality fixtures | Salvage boundary cases and failure-mode vocabulary; do not infer final grading or reflection semantics. |
| Historical Prompt 306 authoring refs | `f8f167f41bb2f10dc40a260294c3aeba74f55bde`, revised at `9d941d159814448e4dbaa75000812d718caf7030` | Prompt wording only | The revision tightened provenance and proof requirements; it is not a Week 2 source. |
| Current DSCT `main` | `2483083a114b70f16ae6b696cef7fec5d3bdd46a` | Accepted Prompt 304 and 305 reports plus current source | Current truth for the map; no historical branch was promoted by this job. |

The incoming branches are both behind current DSCT `main` and remain evidence
only. Their useful material is a report/fixture vocabulary; their conflicting
runtime or unfinalized pedagogy must not be carried forward automatically.

## DSCT STILL OWNS

DSCT still owns the course-specific wrapper: how the shared Building Your AI
Lab supports DSCT's claim/evidence/reasoning goals, what DSCT students are
asked to notice, and which current DSCT paths point to the shared owners. It
also owns any DSCT-specific fixture, prompt, reflection, and student-facing
sequencing that is later authorized.

Jeremy + ChatGPT must still choose the final bounded exercise, including
whether the string-normalization exercise is reused, replaced, or adapted;
the final Week 2 reflection language; the relationship to Pair Reasoning; and
any grading or schedule implications. Prompt 306 makes no such choices.

Actual infrastructure missing from this map is a DSCT-specific, selected
exercise fixture and its current execution receipt. The shared Windows
infrastructure is not missing; DSCT does not own it. A later implementation
prompt may need a DSCT pointer/crosswalk and then a bounded fixture, but this
archaeology report does not author either.

The historical DSCT container/repeatability package remains a provenance
pointer only until a later authorized decision says otherwise. It must not
silently become a second canonical owner.

## Verification commands and results

The following read-only checks were run:

```text
git fetch origin                         # computer_science_2: updated origin/main to 5c3c83d
git rev-parse HEAD / origin/main         # recorded exact refs above
git for-each-ref ...                     # inventoried DSCT and CS2 refs
git ls-tree -r --name-only ...           # located Week 2 paths without merging
PYTHONPATH=src python -m unittest discover -s tests -p 'test*.py' -v
```

`windows_classroom@f87e340a`: 81 tests passed with `PYTHONPATH=src`.
An initial test run without that source path failed with seven import errors;
that was an invocation-environment issue, not converted to a green claim.
`local_ai_lab_setup@b2b2ec1`: its test discovery returned 0 tests in this
checkout, so no validation claim is made for that repository. No PowerShell,
Ollama, Aider, Windows, Canvas, or Savnac action was attempted.

The sibling checkouts remained clean (`git status --short --branch` showed only
their `main` tracking lines). In the isolated DSCT job worktree, the write
scope was checked with:

```text
git diff --check
git diff --name-only
```

Before commit, the only intended changed path is this report. No DSCT source,
prompt, branch history, or sibling repository was changed by the archaeology
job.

## Worker Report contract

- **Branch:** `worker/prompt306-reuse`
- **Worktree:** `/tmp/dsct-prompt306`
- **Commit:** `851c5f481cc69df54283cacca24d16e36684940b` (report package; follow-up receipt repair commits may supersede this exact report blob)
- **Validation:** provenance inventory complete; nine loop roles mapped; Windows test battery 81/81 with `PYTHONPATH=src`; sibling status clean; `git diff --check` passed and the changed-path audit contained only this report
- **Yellows:** no Windows execution on this host; local AI test discovery has no tests; DSCT-specific exercise, reflection, and grading/schedule choices remain open; historical DSCT runtime package may conflict with shared Windows ownership
- **Boundary check:** report-only write; no source edits, merges, installations, resets, Canvas/Savnac/JTT actions, or pedagogical decisions
- **Recommendation:** Foreman should independently review this report, then accept/promote only the report commit. Later DSCT authoring should begin with canonical pointers and an explicitly selected DSCT exercise rather than copying the CS2 extension.
