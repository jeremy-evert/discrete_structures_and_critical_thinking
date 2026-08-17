# Report 305 — DSCT Week 2 assessment contract reconciliation

Branch: `golem/dsct-305-assessment-contract`

## What this is

Ports the Week 2 local-AI-readiness **assessment contract** and its 8-case
**acceptance fixture battery** from the stale, unmerged
`origin/agent/prompt305-dsct-assessment` branch onto current `main`,
additively, under `assessment/`. Nothing under `week-02/`,
`docs/grading-model.md`, `course_metadata.yaml`, or any Week 1 file was
touched. This is source/contract authoring only — the contract is not wired
into Marker, Coach, or any live grading path
(`policies.live_rollout: not authorized` is preserved unchanged in the
ported contract).

## Files landed

- `assessment/week-02-readiness-assessment-contract.yaml`
- `assessment/week-02-approved-materials.yaml`
- `assessment/fixtures/week-02/manifest.yaml`
- `assessment/fixtures/week-02/strong-complete-ready.md`
- `assessment/fixtures/week-02/strong-not-ready.md`
- `assessment/fixtures/week-02/assertion-only.md`
- `assessment/fixtures/week-02/deliciously-wrong-ai-style.md`
- `assessment/fixtures/week-02/invalid-counterexample.md`
- `assessment/fixtures/week-02/passing-test-universal-overclaim.md`
- `assessment/fixtures/week-02/supplied-receipt-as-own-evidence.md`
- `assessment/fixtures/week-02/wrong-system-model.md`
- `assessment/verify_week02_contract_paths.py` (the acceptance-check script,
  see below)

## What was ported unchanged

- **The full rubric-to-criteria mapping** in
  `week-02-readiness-assessment-contract.yaml`: all five criteria
  (`sources_evidence_provenance`, `rules_assumptions_system_model`,
  `work_traceable_workflow`, `check_counterexample_verification`,
  `summary_evidence_limits`) with their `marker_semantic_text`,
  `full_credit_observable_evidence`, `common_failure_modes`, and
  `critical_errors` blocks, verbatim. This prose does not reference any
  stale file path — it references the shared DSCT five-part reasoning
  method (Sources / Rules-Assumptions / Work / Check / Summary), which is
  still `week-01/student/reasoning-method.md` on `main`, unchanged.
- **`assignment.submission_path`** (`local-ai-readiness.md`),
  **`source_assignment`**, and **`course_extension`**
  (both `repository: local_ai_lab_setup`), unchanged — these point at the
  shared `local_ai_lab_setup` repo's Week 2 module and DSCT extension,
  which are untouched by main's Week 2 restructure and still exist at the
  referenced paths.
- **All 8 fixture submissions** (`strong-complete-ready.md` through
  `wrong-system-model.md`) and `manifest.yaml`, byte-identical to the stale
  branch. None of the fixture prose references a repo file path (they are
  self-contained synthetic student submissions), so none needed a path fix.

## What was repointed

`assignment.recurring_method.source.path`
(`week-01/student/reasoning-method.md`) needed no change — it already
matches `main`'s real Week 1 layout.

Three entries in `week-02-approved-materials.yaml` referenced the stale
branch's `week-02/student/tuesday/` subfolder layout, which does not exist
on `main` (`main`'s merged Week 2 layout is flat:
`week-02/student/tuesday-activity.md`, `thursday-activity.md`,
`week-02-evidence-assignment.md`, `week-02-evidence-rubric.md`). Repointed:

| citation_id | stale path | repointed path | why |
|---|---|---|---|
| `dsct-week2-tuesday-guide` | `week-02/student/tuesday/README.md` | `week-02/student/tuesday-activity.md` | This is `main`'s actual Tuesday guide; it contains the same evidence-card/workflow content the stale citation described. |
| `dsct-week2-reflection` | `week-02/student/tuesday/dsct-evidence-reflection.md` | `week-02/student/tuesday-activity.md` | No standalone reflection file exists on `main`; the claim/sources/rules/work/check/summary evidence card the stale file held lives inside `tuesday-activity.md`. |
| `dsct-week2-help-status` | `week-02/student/help-and-runtime-status.md` | `week-02/student/week-02-evidence-assignment.md` | No standalone help/runtime-status file exists on `main`; the truthful-NOT-READY / infrastructure-stop content the stale file held is `week-02-evidence-assignment.md`'s "Acceptance boundary" section. |

Each repointed entry's `section_or_topic` field was rewritten to name both
the new target and the reason for the repoint, so the manifest documents
its own provenance rather than silently changing.

`contract_version` was bumped `2026-08-14.1` → `2026-08-17.1` and
`manifest_version` `2026-08-14.1` → `2026-08-17.1` to mark this
reconciliation pass.

## What was deliberately left behind, and why

- **`source_revision` pins.** The stale `week-02-approved-materials.yaml`
  pinned each entry to a specific commit SHA in its own repo
  (`85ea3a2c...` for this repo, `b2b2ec1a...` for `local_ai_lab_setup`,
  `f87e340a...` for `windows_classroom`). Those SHAs predate this repo's
  merged Week 2 package and do not correspond to any commit that contains
  the repointed paths (e.g. `85ea3a2c` predates `tuesday-activity.md`
  entirely). Rather than fabricate new SHAs I cannot verify, this field was
  dropped. Re-pinning `source_revision` to real commit hashes is future
  work, not part of this port.
- **The stale branches' `week-02/` restructure**
  (`week-02/student/tuesday/`, `week-02/student/thursday/` subfolders) —
  explicitly out of scope per the prompt; `main`'s already-merged flat
  layout is project truth and was not touched.
- **The stale branch's `docs/grading-model.md` deletion** — not resurrected.
  `main`'s real grading model (45% Odyssey / 50% recurring / 5% final,
  Week 2 as the 30% weekly-gate readiness/setup entry) was read as truth
  and left untouched.
- **No new criteria were invented.** `main`'s merged
  `week-02/student/week-02-evidence-rubric.md` names a fifth Tuesday
  criterion, "Privacy and submission care" (3 of 20 points), that the
  ported contract's five reasoning-method criteria do not literally cover
  (the contract's criteria track Sources/Rules/Work/Check/Summary, not the
  rubric's five named headings one-for-one). The prompt's instruction was
  to preserve the contract's existing authored pedagogical content as-is,
  not invent new criteria, so this gap was **not** patched — it is flagged
  here as a known coverage gap for a future prompt to close explicitly,
  since a fail-closed Marker rubric should score privacy/submission care
  before any live grading uses this contract.
- **Live wiring.** Per the forbidden list and the contract's own
  `policies.live_rollout: not authorized`, this contract is not connected
  to Marker, Coach, or any grading path.

## Acceptance check: every referenced path resolves to a real file

`assessment/verify_week02_contract_paths.py` loads both YAML files and
asserts every referenced path exists:

- `assignment.submission_path` — special-cased: it names the file a
  *student* creates and submits (it cannot pre-exist as a repo file before
  any student has done the assignment), so the check instead asserts it is
  a bare filename (no path traversal) and that the exact filename string is
  referenced inside the document at `source_assignment.path`.
- `assignment.source_assignment.path`, `assignment.course_extension.path`,
  and `assignment.recurring_method.source.path` — checked for real
  existence on disk, resolved either against this repo's root (when
  `repository: discrete_structures_and_critical_thinking`) or against a
  sibling checkout `../<repository>` (when `repository` names another
  course repo, e.g. `local_ai_lab_setup`, `windows_classroom` — this
  machine has those checked out as siblings of this repo).
- Every entry in `week-02-approved-materials.yaml` — checked the same way,
  for completeness beyond the strict prompt-listed field set.

Real pass output (`python3 assessment/verify_week02_contract_paths.py`,
run from the repo root at the commit this work lands on):

```
PASS: assignment.submission_path 'local-ai-readiness.md' is a bare filename referenced by /mnt/brandy_nvme/jevert/git/local_ai_lab_setup/curriculum/shared/week2/12_readiness_assignment.md
PASS: assignment.source_assignment.path -> /mnt/brandy_nvme/jevert/git/local_ai_lab_setup/curriculum/shared/week2/12_readiness_assignment.md
PASS: assignment.course_extension.path -> /mnt/brandy_nvme/jevert/git/local_ai_lab_setup/curriculum/dsct/week2_extension.md
PASS: assignment.recurring_method.source.path -> /mnt/brandy_nvme/jevert/git/discrete_structures_and_critical_thinking/week-01/student/reasoning-method.md
PASS: approved-materials[dsct-reasoning-method].path -> /mnt/brandy_nvme/jevert/git/discrete_structures_and_critical_thinking/week-01/student/reasoning-method.md
PASS: approved-materials[dsct-ai-verification].path -> /mnt/brandy_nvme/jevert/git/discrete_structures_and_critical_thinking/week-01/student/ai-verification-expectation.md
PASS: approved-materials[dsct-week2-tuesday-guide].path -> /mnt/brandy_nvme/jevert/git/discrete_structures_and_critical_thinking/week-02/student/tuesday-activity.md
PASS: approved-materials[dsct-week2-reflection].path -> /mnt/brandy_nvme/jevert/git/discrete_structures_and_critical_thinking/week-02/student/tuesday-activity.md
PASS: approved-materials[dsct-week2-help-status].path -> /mnt/brandy_nvme/jevert/git/discrete_structures_and_critical_thinking/week-02/student/week-02-evidence-assignment.md
PASS: approved-materials[shared-local-ai-architecture].path -> /mnt/brandy_nvme/jevert/git/local_ai_lab_setup/curriculum/shared/week2/05_local_ai_architecture.md
PASS: approved-materials[shared-localhost-boundary].path -> /mnt/brandy_nvme/jevert/git/local_ai_lab_setup/curriculum/shared/week2/08_localhost_apis_and_local_vs_cloud.md
PASS: approved-materials[shared-readiness-check].path -> /mnt/brandy_nvme/jevert/git/local_ai_lab_setup/curriculum/shared/week2/09_run_the_readiness_check.md
PASS: approved-materials[shared-first-local-ai-interaction].path -> /mnt/brandy_nvme/jevert/git/local_ai_lab_setup/curriculum/shared/week2/10_first_local_ai_interaction.md
PASS: approved-materials[shared-troubleshooting-evidence].path -> /mnt/brandy_nvme/jevert/git/local_ai_lab_setup/curriculum/shared/week2/11_troubleshoot_with_evidence.md
PASS: approved-materials[shared-readiness-assignment].path -> /mnt/brandy_nvme/jevert/git/local_ai_lab_setup/curriculum/shared/week2/12_readiness_assignment.md
PASS: approved-materials[dsct-week2-extension].path -> /mnt/brandy_nvme/jevert/git/local_ai_lab_setup/curriculum/dsct/week2_extension.md
PASS: approved-materials[windows-week2-guide].path -> /mnt/brandy_nvme/jevert/git/windows_classroom/docs/week2_student_guide.md

17 passed, 0 failed
ALL PATHS RESOLVED.
```

A second, informal check confirms the fixture manifest's own
`submission_file` entries all resolve inside `assessment/fixtures/week-02/`
(all 8 `PASS`, `ALL FIXTURE FILES RESOLVED`) — not part of the prompt's
strict required field set, but included for completeness since the
fixtures are the acceptance battery this contract exists to support.

## Forbidden-list compliance

- Did not check out, merge, or rebase onto either stale branch; all stale
  content was read via `git show <branch>:<path>`.
- Did not modify `week-02/`, `docs/grading-model.md`,
  `course_metadata.yaml`, or any Week 1 file. (`git status` at the time of
  this commit shows only new files under `assessment/`, plus this report
  and the untracked prompt file.)
- Did not wire this contract into Marker, Coach, or any live grading path.
- Did not push either stale remote branch.
