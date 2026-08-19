# Job 322 worker receipt — Weeks 13–14

- Worker branch: `golem/job322-w13-14`
- Scope: only the bounded Week 13 and Week 14 teachable source packages.
- Source basis: `planning/fall-2026-topic-map.md`,
  `planning/fall-2026-weekly-architecture.md`, `docs/grading-model.md`, and
  historical lessons 11–14.

## Delivered package

- `week-13/`: student overview, Tuesday tree/traversal activity, Thursday Pair
  Reasoning activity, ordinary Decision Gate instructions, and instructor
  guide.
- `week-14/`: student overview, Tuesday Boolean/state-model activity,
  Thursday Show & Tell guide, Odyssey Checkpoint 3 instructions, and
  instructor guide.

## Contract checks

- Week 13 is dated Nov 10/12, uses Pair Reasoning, and retains its ordinary
  Decision Gate.
- Week 14 is dated Nov 17/19, uses the Show & Tell mini-capstone, and states
  that Checkpoint 3 replaces the ordinary Decision Gate; it does not create a
  Week 14 Decision Gate.
- Both packages include a Tuesday AI Fluency check, individual technical
  evidence path, Thursday facilitation path, reusable-report references,
  provenance, and no required external tool/text/account.

## Validation run

```text
git diff --check
test -s <each of 10 authored package files>
rg for unresolved source markers in week-13/ and week-14/ (none found)
rg for reusable-report references and cadence invariants (found as expected)
```

All commands exited successfully. No Canvas, Savnac, sibling repository, or
grading-model change was made.
