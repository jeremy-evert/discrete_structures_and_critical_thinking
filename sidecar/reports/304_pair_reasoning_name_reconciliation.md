# Prompt 304 — Pair Reasoning name reconciliation

## Result

The settled recurring DSCT pair-activity name is now **Pair Reasoning** in every current operational source that named the activity. This was a naming reconciliation only: no grading weight, schedule, activity semantics, or Canvas/Savnac configuration changed.

## Starting state

- Starting commit: `7c62f310e4cb584d3f47617c1757d97de1de7245`
- Source migration commit: `44169f8d53eeb63d4345f44db6d4d8604bb7f277`
- Protected pre-existing worktree item: the untracked `prompts/305_week2_assessment_contract_reconciliation.md` was neither staged, modified, moved, nor deleted.

### Search commands

```bash
rg -n -i -C 2 -e 'pair programming' -e 'paired-programming' -e 'paired programming' -e 'A3' .
rg -l -i -e 'pair programming' -e 'paired-programming' -e 'paired programming' . | sort
rg -n -i -e 'pair programming' -e 'paired-programming' -e 'paired programming' assignments docs planning lessons course_metadata.yaml
rg -n -i 'pair-programming-report' . -g '!archive/**' -g '!raw/**' -g '!runs/**'
```

The exact old-name search returned 22 path-level hits. `A3` was inspected only where it denoted the recurring pair-activity category; opaque hashes and unrelated identifiers were not terminology hits.

## Before-state inventory and disposition

| Path / relevant context | Disposition | Reason |
|---|---|---|
| `assignments/pair-programming-report.md:1` reusable current template heading | RENAME | Current reusable activity template. Renamed to `assignments/pair-reasoning-report.md` with the heading updated. |
| `docs/grading-model.md:16,59` A3-equivalent label and Thursday rotation | RENAME | Current Fall 2026 source model; only the activity/category name changed. |
| `planning/fall-2026-weekly-architecture.md:24,27,54` Thursday chassis and continuity handoff | RENAME | Current operational weekly architecture. Artifact examples and cadence remain unchanged. |
| `planning/fall-2026-topic-map.md:12,14,16,20,22` Weeks 3/5/7/11/13 Thursday-mode labels | RENAME | Current operational topic map. Only the label changed. |
| `docs/curriculum/course-sequence.md:19,24` archived-Canvas inference | PRESERVE-HISTORICAL | Explicitly a historical map, not Fall 2026 doctrine. |
| `docs/philosophy/teaching-patterns.md:7` archive-grounded Spring 2026 description | PRESERVE-HISTORICAL | Preserves observed historical terminology. |
| `docs/reports/curriculum-history-synthesis.md:11,17` historical course synthesis | PRESERVE-HISTORICAL | Report of past courses, not current course source. |
| `prompts/013_reasoning_odyssey_fabric_reconciliation.md` | PRESERVE-HISTORICAL | Completed/historical prompt evidence. |
| `reports/013_reasoning_odyssey_fabric_reconciliation.md` | PRESERVE-HISTORICAL | Historical reconciliation report. |
| `reports/302_semester_spine_weekly_architecture_contract.md` | PRESERVE-HISTORICAL | Accepted Prompt 302 report evidence. |
| `reports/304_dsct_grading_model.md` | PRESERVE-HISTORICAL | Pre-existing grading-model report; it is evidence, not current doctrine. |
| `runs/2026-08-14_prompt302_semester_spine_weekly_architecture/derived/professional_minds_slots.csv` | PRESERVE-HISTORICAL | Prompt 302 generated receipt. |
| `runs/2026-08-14_prompt302_semester_spine_weekly_architecture/derived/thursday_rotation.csv` | PRESERVE-HISTORICAL | Prompt 302 generated receipt. |
| `raw/20260815T192936Z__dsct-012-drop-zybooks.raw.txt` | PRESERVE-HISTORICAL | Captured raw execution evidence. |
| `archive/fall-2024/canvas-64613-snapshot-20260714-195513.json` | PRESERVE-HISTORICAL | Immutable archived Canvas snapshot. |
| `archive/fall-2025/canvas-69072-snapshot-20260714-195525.json` | PRESERVE-HISTORICAL | Immutable archived Canvas snapshot. |
| `archive/spring-2025/canvas-66486-snapshot-20260714-195600.json` | PRESERVE-HISTORICAL | Immutable archived Canvas snapshot. |
| `archive/spring-2026/canvas-71253-snapshot-20260714-195606.json` | PRESERVE-HISTORICAL | Immutable archived Canvas snapshot. |
| `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md` | PRESERVE-HISTORICAL | New design quarry records the prior term while stating the settled replacement. |
| `sidecar/prompts/304_reconcile_pair_reasoning_name.md` | PRESERVE-HISTORICAL | The work order necessarily names the term it retires. |
| `sidecar/prompts/305_inventory_reasoning_odyssey_world_bible_vocabulary.md` | PRESERVE-HISTORICAL | Future bounded inventory prompt; its search vocabulary is intentional. |
| `sidecar/prompts/310_inventory_dsct_stale_source_seams.md` | PRESERVE-HISTORICAL | Future seam-audit prompt; its stale-name criterion is intentional. |

No hit required `AMBIGUOUS-STOP`: each current reference either plainly named the recurring activity or was historical evidence. Technical references to programming as a tool remain intact, including the template's driver/navigator role language and artifact examples such as checkers, simulators, and verifiers.

## Files changed

- `assignments/pair-programming-report.md` → `assignments/pair-reasoning-report.md`
- `docs/grading-model.md`
- `planning/fall-2026-topic-map.md`
- `planning/fall-2026-weekly-architecture.md`

## Validation

Before the source commit:

```bash
git diff --check
git diff --name-status
git diff -- <four changed paths>
rg -n -i -e 'pair programming' -e 'paired-programming' -e 'paired programming' assignments docs planning -g '!docs/curriculum/**' -g '!docs/philosophy/**' -g '!docs/reports/**'
rg -n 'Pair Reasoning' assignments/pair-reasoning-report.md planning/fall-2026-weekly-architecture.md planning/fall-2026-topic-map.md docs/grading-model.md
```

Results:

- `git diff --check` passed.
- The diff contained only the four current-source paths above (one is a git rename) and 11 textual substitutions; no activity, grading, cadence, or artifact semantics changed.
- The residual current-source old-name search returned no unexplained hit.
- `Pair Reasoning` is present in the renamed template, the weekly architecture, all five intended topic-map rows, and both grading-model references.
- Paragraph/table-row spot checks confirmed that programming remains available as an instrument inside Pair Reasoning, while the recurring activity label is now Pair Reasoning.

## Decision-boundary return

None. This reconciliation did not decide reflection questions, feedback placement, grading structure, Week 4–14 cadence, Week 2/3 allocation, or any other course-design question reserved by Prompt 304.
