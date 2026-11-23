# Job 322 worker receipt — Weeks 10–12

**Worker branch:** `golem/job322-w10-12`  
**Starting commit:** `4b0e33a`  
**Scope:** Weeks 10–12 source packages and this receipt only.

## Prompt/source note

`sidecar/prompts/322_worker_w10_12.md` was absent in this isolated worktree.
The tracked Job 322 contract assigned worker C to Weeks 10–12, so it supplied
the bounded authority and invariants. No foreman integration, production,
Savnac, grading-weight, or sibling-repository action occurred.

## Authored package

| Week | Files | Required behavior |
|---|---|---|
| 10 | README; Tuesday activity; Decision Gate; two run-of-show files | Probability; Show & Tell; ordinary Decision Gate. |
| 11 | README; Tuesday activity; Checkpoint 2; two run-of-show files | Relations; Pair Reasoning; checkpoint replaces Decision Gate. |
| 12 | README; Tuesday activity; Decision Gate; two run-of-show files | Graphs; Show & Tell; ordinary Decision Gate. |

Every package includes dates, targets/prerequisites, technical example, AI
failure check, individual evidence path, correct Thursday mode, facilitation,
and historical/planning provenance. Reusable assignment contracts are
referenced instead of copied.

## Validation

Commands run after authoring:

```text
git diff --check
rg -n -i 'source_pending|todo|tbd|placeholder' week-10 week-11 week-12
rg -n 'Decision Gate|Checkpoint 2|Show & Tell|Pair Reasoning' week-10 week-11 week-12
for week_dir in week-10 week-11 week-12; do test -f "$week_dir/README.md"; test -f "$week_dir/student/tuesday-activity.md"; test -f "$week_dir/instructor/tuesday-run-of-show.md"; test -f "$week_dir/instructor/thursday-run-of-show.md"; done
```

Results: `git diff --check` passed; the placeholder-token search returned no
matches; expected cadence/evidence terms are present; the structural package
contract passed for all three weeks. Commit SHA: recorded in Git history for
this receipt's package commit.

## Handoff

Foreman should inspect this cluster and run the repository-level completion
validator once available, alongside other week-cluster packages. This
source-only package introduces no external/deployment yellow.
