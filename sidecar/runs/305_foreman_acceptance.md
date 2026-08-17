# Prompt 305 — Foreman acceptance receipt

## Package reviewed

- Prompt: `sidecar/prompts/305_inventory_reasoning_odyssey_world_bible_vocabulary.md`
- Worker: Locke (isolated Luna worker)
- Worker branch / original package commit: `worker/prompt305-vocabulary` / `9a478734`
- Integrated report commit after non-overlapping main advancement: `4599bb4e786d85ef07dc10f5391c18058e348c54`
- Report: `sidecar/reports/305_reasoning_vocabulary_inventory.md`
- Foreman baseline before integration: `d47596b` (Prompt 311 addition only, no overlap with the report)

## Acceptance contract

**What Foreman required:** a read-only, source-cited vocabulary inventory that covers current and historical/provenance object families; separates source doctrine from proposals; inventories aliases, overloads, duplicate-homework risks, stale legacy, gradebook seams, and unresolved questions; and makes no ontology or grading decision.

**What would have failed acceptance:** a source edit beyond the report, a missing required search family, an unlabeled medium/low-confidence inference, a claim that a raw design proposal was current doctrine, or any resolution of the named design questions.

## Independent Foreman checks

```bash
git diff --check origin/main..HEAD
git diff --name-only origin/main..HEAD
test ! -d rubrics
rg -n -i -e 'Reasoning Odyssey' -e 'Coding Odyssey' -e 'Reasoning Quest' -e 'Reasoning Gate' -e 'World Bible' -e 'weekly reinforcement' -e 'weekly write-up' -e 'checkpoint' -e 'evidence receipt' -e 'reflection' -e 'Pair Reasoning' -e 'Pair Programming' -e 'Show & Tell' -e 'A3' -e 'A4' -e 'A7' planning docs assignments week-01 week-02 week-16 sidecar/raw sidecar/reports -g '!sidecar/reports/305_reasoning_vocabulary_inventory.md' | wc -l
rg -n 'Collision-class findings|ALIAS|OVERLOAD|DUPLICATE-HOMEWORK RISK|STALE-LEGACY|GRADEBOOK-SEAM|UNRESOLVED|Medium/low-confidence' sidecar/reports/305_reasoning_vocabulary_inventory.md
git show --check --stat 4599bb4
```

Results:

- Diff scope is exactly `sidecar/reports/305_reasoning_vocabulary_inventory.md`.
- Whitespace/diff checks pass.
- `rubrics/` is absent and the worker report says so explicitly.
- The broad current/historical vocabulary scan returned 300 matching source lines; the report consolidates the meaningful object families rather than pretending raw-hit count is ontology.
- The report contains all required collision classes and a dedicated medium/low-confidence section with representative source paths.
- Manual source comparison confirms the report treats the raw design dump and decision pile as provenance/proposals, not as a decision to apply.
- No course source, Canvas/Savnac, JTT, sibling repository, secret, production, or destructive action occurred.

## Foreman decision

**ACCEPT.** The report is sufficient evidence for the later Jeremy + ChatGPT ontology decision. It intentionally returns, rather than resolves, the distinct weekly-object, checkpoint, World Bible, and social-artifact/gradebook seams.

## Truth ledger

- `authored_owner`: Locke (worker)
- `authored_evidence`: isolated branch `worker/prompt305-vocabulary`, original commit `9a478734`
- `wired_owner`: Assistant Foreman
- `wired_evidence`: Prompt 305 scope, report-only authority, explicit acceptance contract above
- `executed_owner`: Locke; independently checked by Assistant Foreman
- `executed_evidence`: worker report package and Foreman commands/results above
- `promoted_owner`: Assistant Foreman
- `promoted_evidence`: integrated commit `4599bb4`; publication follows this receipt

## Remaining yellows

The accepted report deliberately leaves these for the human/course-design decision queue: Quest versus Gate identity, World Bible's role/cadence/carry-forward rule, checkpoint definition and timing, distinction among social artifacts, and the A3/A4/A7 measurement model.
