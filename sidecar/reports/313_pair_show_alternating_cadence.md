# Prompt 313 — Pair Reasoning / Show & Tell alternating cadence: report

**Status:** DONE — cadence contract landed; one seam returned open (Week 3
topic-map staleness), not decided here.

## 1. Starting commit SHA

`2ec8ea82b822a96d6bec987bb0306e51ce51376c` (origin/main at the time this
worktree/branch was created).

## 2. Prompt 311/312 dependency status

Not yet landed on `main` as of the starting commit: only the prompt specs
(`sidecar/prompts/311_define_pair_reasoning_contract.md`,
`sidecar/prompts/312_define_show_and_tell_contract.md`) exist; no
`sidecar/reports/311_*` or `sidecar/reports/312_*` report was present.
Sibling worktrees `worker/prompt311-pair-reasoning` and
`worker/prompt312-show-and-tell` existed but were still sitting at the same
commit as `main` (no divergent commits yet). Per instructions this prompt did
not block on them; it consumed the settled decisions already documented in
`sidecar/prompts/313_define_pair_show_alternating_cadence.md` and
`sidecar/raw/2026-08-17_dsct_design_decision_pile.md` directly, and did not
reopen or redesign the 311/312 semantic contracts.

## 3. Files inspected

- `sidecar/prompts/313_define_pair_show_alternating_cadence.md` (work order)
- `sidecar/raw/2026-08-17_dsct_design_decision_pile.md` (source quarry,
  especially "Decision cluster C/D/E")
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `docs/grading-model.md`
- `docs/career-connection.md`
- `assignments/pair-reasoning-report.md`, `assignments/show-and-tell-artifact.md`
- `sidecar/prompts/307_probe_week3_container_latex_student_path.md` and its
  report `sidecar/reports/307_week3_container_latex_student_path_probe.md`
- `sidecar/prompts/316_define_week3_pinned_container_skill_ladder.md`
- `reports/302_semester_spine_weekly_architecture_contract.md`,
  `reports/304_dsct_grading_model.md` (historical/frozen decision reports —
  read for provenance only, not edited)
- `sidecar/prompts/311_define_pair_reasoning_contract.md`,
  `sidecar/prompts/312_define_show_and_tell_contract.md`

## 4. Files changed

- `planning/fall-2026-weekly-architecture.md` — added a new "Pair Reasoning /
  Show & Tell cadence (Prompt 313)" subsection under the Thursday chassis.
  This is the only file changed. `planning/fall-2026-topic-map.md` and
  `docs/grading-model.md` were deliberately left untouched (see §6 and §11).

## 5. Baseline cadence now expressed by current source

`planning/fall-2026-topic-map.md`'s "Thu mode / intended artifact family"
column already encoded the correct baseline before this prompt ran:

| Week | Mode |
|---|---|
| 4 | Show & Tell |
| 5 | Pair Reasoning |
| 6 | Show & Tell |
| 7 | Pair Reasoning |
| 8 | Show & Tell |
| 9 | Pair-style work folded into Tuesday (Thursday = Fall Break) |
| 10 | Show & Tell |
| 11 | Pair Reasoning |
| 12 | Show & Tell |
| 13 | Pair Reasoning |
| 14 | Show & Tell / Reasoning Odyssey mini-capstone |

This already matches the settled decision exactly (Week 4 starts with Show &
Tell, Week 5 Pair Reasoning, strict alternation, Week 9 as the only
interruption). What was missing was a source-committed *statement* of the
cadence rule and its starting point in the planning contract
(`fall-2026-weekly-architecture.md`), which previously only said "Pair
Reasoning or Show & Tell" without naming the alternation, its Week 4 start,
or the one-mode-per-week rule. This prompt added that statement; it did not
change any per-week mode assignment in the Week 4–14 range.

## 6. One-mode-per-week audit result

**PASS.** For every Week 4–14 row in `planning/fall-2026-topic-map.md`, the
"Thu mode" column names exactly one recurring social mode (Pair Reasoning or
Show & Tell), never both. `docs/grading-model.md`'s two Thursday-artifact
categories (A3-equivalent Pair Reasoning, A4/A7-equivalent Show & Tell) list
disjoint week sets for weeks 4–14 (Pair Reasoning: 5, 7, 11, 13; Show & Tell:
4, 6, 8, 10, 12, 14) — no week appears in both lists. No normal formal week
requires both events.

## 7. Runway-boundary audit result

**Week 2** ("Building Your AI Lab") carries no Pair Reasoning / Show & Tell
label anywhere inspected; it is out of the alternation entirely, as
expected.

**Week 3** is the seam. `sidecar/prompts/307_probe_week3_container_latex_student_path.md`,
its accepted report, and `sidecar/prompts/316_define_week3_pinned_container_skill_ladder.md`
all establish Week 3 as a pinned-container / minimum-useful-LaTeX runway week
("tools runway rather than formal discrete math" — design-decision quarry,
Decision cluster D, line ~324). The quarry explicitly calls Week 3 a
"reproducibility-focused Pair Reasoning experience" (Decision cluster A,
line ~112/115) as its own, separately-scoped tooling activity — distinct
from the Week 4–14 graded Pair Reasoning category.

However, `planning/fall-2026-topic-map.md` still carries a full Week 3 row
("Logic, Claims & Proof") labeled `Pair Reasoning · checker, counterexample
generator, proof verifier`, and `docs/grading-model.md` still lists "3"
inside its formal Pair Reasoning graded-week list. Both predate the settled
Week 3 runway/container direction and were not updated when Prompts 307/316
landed. This means: **Week 3's pair-style runway work does not shift Week 4**
(Week 4 is still correctly Show & Tell — confirmed), so the alternation
itself is not broken. But whether Week 3's old "Logic, Claims & Proof"
technical bundle is graded as a full Pair Reasoning week, folded into another
Week 4–14 slot, or dropped/reorganized (the quarry's own "twelve bundles vs.
eleven Week 4–14 slots" problem, Decision cluster E) is unresolved. This
prompt's hard stops forbid choosing the final Week 4–14 technical topics and
forbid inventing exception policy, so this seam is reported, not resolved
(see §11).

## 8. Calendar/special-week exception table

| Week | Exception | Treatment status |
|---|---|---|
| Week 1 | Compressed kickoff week (Prompt 301); not part of this chassis | Already decided |
| Week 2 | Building Your AI Lab; no Pair Reasoning/Show & Tell slot | Already decided |
| Week 3 | Runway (pinned-container + LaTeX, Prompts 307/316); may contain pair-style reproducibility work under its own contract | Already decided that it does not shift Week 4; topic-map/grading-model staleness is a separate open seam (§7, §11) |
| Week 9 | Thursday (Oct 15) is Fall Break; no class meeting that day | Already decided — pair-style work folded into Tuesday, no Thursday artifact promised, no make-up assignment invented (`fall-2026-weekly-architecture.md` Exceptions section, unchanged by this prompt) |
| Week 15 | Asynchronous Thanksgiving/travel buffer; no formal topic or chassis | Already decided — outside Week 4–14 alternation entirely |
| Week 16 | Farkle + ML synthesis (special contract, Prompt 315) | Already decided; not touched by this prompt (hard stop) |
| Week 17 | Final reflection/closeout | Already decided — outside the alternation |

No new exception was invented. No make-up assignment, extra async report, or
grading penalty was added for Week 9 or any other week.

## 9. Grading-boundary audit

- Pair Reasoning report (A3-equivalent): still 5%, unchanged.
- Show-and-Tell reflection (A4-equivalent): still 5%, unchanged.
- Friday feedback report (A7-equivalent, tied to Show & Tell weeks): still
  5%, unchanged.
- No new grade category was created.
- No normal Week 4–14 week creates both graded social-event objects
  (confirmed §6).
- The two categories intentionally contain different week counts (Pair
  Reasoning: 5, 7, 11, 13 = 4 full weeks + Week 9 pair-style Tuesday work;
  Show & Tell: 4, 6, 8, 10, 12, 14 = 6 weeks) because of the odd eleven-week
  core and the Week 9 calendar exception — this is expected, not a defect,
  per the prompt's own §5 grading-boundary contract.
- `docs/grading-model.md` was not edited; its arithmetic (`100%` total) was
  not touched, per the hard stop against repairing unrelated grading-model
  arithmetic.

## 10. Validation commands/results

```
$ git diff --check
(no output — clean)

$ git diff --name-only
planning/fall-2026-weekly-architecture.md

$ grep -n "Pair Reasoning\|Show & Tell" planning/fall-2026-weekly-architecture.md \
    planning/fall-2026-topic-map.md docs/grading-model.md
(confirms: Week 4–14 topic-map Thu-mode column alternates S&T/PR starting at
Week 4 = Show & Tell; grading-model.md's A3 vs A4/A7 week lists are disjoint
for weeks 4–14; weekly-architecture.md now states the cadence rule
explicitly)
```

Full diff was inspected manually; the only change is the new "Pair Reasoning
/ Show & Tell cadence (Prompt 313)" subsection added to
`planning/fall-2026-weekly-architecture.md`, plus no other lines touched.

## 11. Unresolved seams returned to Jeremy + ChatGPT

1. **Week 3 topic-map/grading-model staleness (the main seam).**
   `planning/fall-2026-topic-map.md`'s Week 3 row ("Logic, Claims & Proof",
   Pair Reasoning mode) and `docs/grading-model.md`'s inclusion of Week 3 in
   the formal Pair Reasoning graded-week list predate the settled Week 3
   runway/pinned-container direction (Prompts 307/316) and the quarry's own
   framing of Week 3 as "tools runway rather than formal discrete math."
   This does not break the Week 4–14 alternation (Week 4 is still correctly
   Show & Tell), but it leaves Week 3's old technical bundle and its
   Pair-Reasoning grading status inconsistent with the current runway
   decision. Resolving it requires deciding where (or whether) the
   "Logic, Claims & Proof" bundle relocates inside the eleven Week 4–14
   slots (quarry Decision cluster E: "twelve bundles vs. eleven Week 4–14
   slots") and whether Week 3's pair-style reproducibility work should
   appear in the formal Pair Reasoning grading category at all. Both are
   topic-selection/grading-count decisions this prompt's hard stops forbid
   making.
2. No other open cadence seam was found. Weeks 1, 2, 9, 15, 16, 17 all have
   already-decided treatments (§8), and the Week 4–14 alternation itself
   requires no further decision.

## 12. Final commit SHA / working-tree state

Working tree was clean after committing the single change described in §4.
See the top-level report for the final commit SHA (recorded in the branch
`worker/prompt313-cadence`, pushed to `origin/worker/prompt313-cadence`).
