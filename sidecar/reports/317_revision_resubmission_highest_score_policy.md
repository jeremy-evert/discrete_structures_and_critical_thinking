# Report 317 — Revision, resubmission, and highest-score policy

**Prompt:** `sidecar/prompts/317_define_revision_resubmission_highest_score_policy.md`
**Starting commit SHA:** `2ec8ea82b822a96d6bec987bb0306e51ce51376c` (origin/main at dispatch time)
**Branch:** `worker/prompt317-revision-policy`

## Files changed

- `docs/grading-model.md` — added a new `## Revision, resubmission, and
  highest-score policy` section at the end of the document, and tightened the
  closing "deployment questions" sentence (dropped `late rules`, since that
  arithmetic is now referenced/settled rather than open, and left `due dates`
  in place since exact calendar dates remain a deployment seam).

No other file required a change. See "Files inspected" below for what was
checked and found not to need edits.

## Files inspected

- `docs/grading-model.md` (edited)
- `sidecar/prompts/314_define_decision_gate_contract.md` (read as provenance;
  not yet landed on main — see "Dependency status")
- `sidecar/prompts/315_define_odyssey_checkpoints_and_farkle_synthesis.md`
  (read as provenance; not yet landed on main — see "Dependency status")
- `sidecar/prompts/318_define_drop_lowest_decision_gate_policy.md` (skimmed
  for overlap; drop-lowest is out of scope here, confirmed no doctrine
  collision)
- `planning/fall-2026-weekly-architecture.md` — describes in-class
  Thursday "critique / revision / evidence receipt" as a same-day chassis
  slot; this is a different mechanic (in-session peer critique) from the
  cross-week resubmission/highest-score doctrine and needed no change
- `planning/fall-2026-topic-map.md`, `planning/fall-2026-course-design.md`,
  `planning/fall-2026-spine.md` — only generic "no due dates invented"
  language; no contradiction
- `assignments/weekly-problem-solving-writeup.md`,
  `assignments/week-16-farkle-evidence-receipt.md` — no late/resubmission
  claims requiring reconciliation
- `sidecar/raw/2026-08-17_dsct_design_decision_pile.md` and
  `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md` — consulted
  as provenance only, not as authority, per the prompt's instruction
- Full-repo searches (see "Stale/contradictory language found") for
  `too late`, `no credit`, `not accepted`, `closed submission`, `cannot be
  resubmitted`, `zero credit`, `final grade stands`, `late`, `resubmission`,
  `revision`, `due date`, `highest score`, `highest recorded`
- Upstream canonical policy (read-only, not edited, per hard stop on
  Marker/Course Foundry code):
  - `/mnt/brandy_nvme/jevert/git/swosu_cs_curriculum/shared/philosophy/late_work_policy.md`
  - `/mnt/brandy_nvme/jevert/git/course_foundry/course_foundry/late_work_policy.py`
  - `/mnt/brandy_nvme/jevert/git/course_foundry/tests/test_continuous_late_work_policy.py`
    (confirms `POLICY_SOURCE_PATH` / `POLICY_SOURCE_REVISION` wiring and the
    1-hour/12-hour/24-hour/21-day acceptance points cited in the prompt)

## Dependency status: Prompts 314 and 315

Neither Prompt 314 (Decision Gate naming) nor Prompt 315 (Odyssey checkpoints
+ Farkle/ML split) has a report or a merged-to-main edit as of this branch's
base commit (`2ec8ea8`) — `sidecar/reports/` contains no `314_*` or `315_*`
file, and `docs/grading-model.md` at that commit still uses the pre-314/315
category names (`Weekly reinforcement / Reasoning Odyssey gate`,
`Reasoning Odyssey checkpoints`, and the still-present `Friday feedback
report (A7 equivalent)` row). Sibling worktrees exist for both
(`worker/prompt314-decision-gate`, and a `worker/prompt315-*`/`golem/dsct-305-*`
family observed mid-flight in the shared repo checkout), confirming they are
in progress on separate branches, per this prompt's note that reconciliation
happens at Foreman merge time.

Per the prompt's own guidance ("do not wait on them" / "the existing raw
decision pile only as provenance, not authority"), this prompt's edit is
written against the current (pre-314/315) category names and section
structure so it applies cleanly to `main` today. The new section does not
rename any category and does not touch the weight table, so it should merge
independently of whichever ordering 314/315 land in; if either renames
`Reasoning Odyssey checkpoints` or restructures the weight table, that is a
purely mechanical cross-reference reconciliation at merge time, not a
doctrine conflict — the revision/highest-score doctrine attaches to
"Reasoning Odyssey checkpoints" and "the weekly gate" by function, not by a
specific literal string that a rename would silently orphan away from its
policy.

## Exact policy wording established

Added verbatim as `## Revision, resubmission, and highest-score policy` in
`docs/grading-model.md`, containing:

- The settled framing quote: *"Too late, sucker is not the policy. Better
  reasoning later is still better reasoning."*
- Seven numbered doctrine points covering: (1) revisions/resubmissions stay
  open while the course is open, and a later checkpoint does not by itself
  close an earlier gate; (2) each attempt judged fresh; (3) lateness never
  contaminates the academic-quality judgment, Marker/Coach see no
  timestamps; (4) the late-work multiplier is the existing shared
  curriculum default (1%/24h, continuous to the second/hour, excused-late
  time reduces counted lateness), with explicit non-reimplementation and
  citations to `swosu_cs_curriculum/shared/philosophy/late_work_policy.md`
  and `course_foundry/course_foundry/late_work_policy.py`; (5) the student
  keeps the highest recorded score across attempts, a later attempt can
  never lower an earned grade; (6) the incentive rationale (a strong late
  revision can still raise the grade; a weaker resubmission costs nothing);
  (7) what counts as substantive revision vs. cosmetic polish, with the
  prompt's own examples reused verbatim.
- A short plain-language "for students" paragraph restating all eight
  required semantic-result bullets from the prompt (due dates matter; late
  isn't worthless; late work still worth doing; revisions welcome;
  attempts may improve the grade; highest score kept; late adjustment still
  applies; substantive revision encouraged).
- A closing paragraph naming the remaining deployment seams explicitly
  (Canvas/Savnac resubmission-window mechanics, the exact end-of-course
  hard-close date, and the gradebook wiring for the highest-score
  comparison) as implementation work, not open policy.

## Stale/contradictory policy language found

None. Repo-wide searches for punitive/closing language (`too late`, `no
credit`, `not accepted`, `closed submission`, `cannot be resubmitted`, `zero
credit`, `final grade stands`) returned no DSCT source hits (the only "too
late" hit is the prompt file itself, and the only "not accepted" hit is an
unrelated sentence in an untracked reconciliation-prompt draft about check
output, not grading). `docs/grading-model.md`'s prior closing sentence
listed "late rules" among unresolved deployment questions, which was mildly
stale now that the late-work *arithmetic* is settled upstream and DSCT's
revision/resubmission layer on top of it is now settled too; it has been
narrowed to the items that are genuinely still open (exact dates, drop-lowest,
checkpoint-week selection). No other file asserted or implied that a
checkpoint closes earlier gates, or that a missed due date ends an
assignment's value.

## Deployment seam remaining

Yes, explicitly named in the new section's closing paragraph and here:

- Exact Canvas/Savnac resubmission-window / "still accepting submissions"
  mechanics are not yet chosen.
- The precise end-of-course hard-close date imposed by the institutional
  grading deadline is not chosen (the canonical late-work policy already
  states this boundary exists in principle; DSCT does not invent a date).
- How the highest-recorded-score comparison across attempts is actually
  wired into the gradebook/automation (e.g., where `course_foundry` or a
  DSCT-specific adapter performs the max-of-attempts comparison) is
  implementation work, not decided here per the hard stop on Marker/Course
  Foundry code.

These were already out of scope per the prompt's hard stops and are reported
rather than invented.

## Acceptance-scenario results

Walked all five scenarios from the prompt against the new policy text:

**A. Strong late first submission** — Point 3 grades the work for quality
with no timestamp visible to Marker/Coach; point 4 applies the standard
continuous multiplier afterward at the trusted edge; point 5 records that
adjusted score since it is the only (and therefore highest) attempt. The
work earns meaningful credit proportional to quality minus a small
continuous penalty, never a cliff. **Consistent.**

**B. Weak on-time first attempt, stronger late revision** — Point 1 keeps
the item open to a second attempt; point 2 grades the revision fresh; point
4 applies its own (possibly nonzero) late multiplier to the revision's own
timestamp; point 5 compares the two recorded scores and keeps the higher
(the revision) since it exceeds the first. **Consistent** — this is exactly
the incentive point 6 describes.

**C. Strong first attempt, worse later attempt** — Point 5 explicitly states
the comparison keeps the higher of the two recorded scores, and point 5's
last sentence ("a later attempt can never lower an already-earned grade —
at worst it simply does not replace it") directly covers this case. The
first, higher score remains the grade of record. **Consistent.**

**D. Criticism-driven revision** — Point 7 lists "responding to criticism or
counterevidence surfaced in Pair Reasoning or Show & Tell" as a canonical
example of substantive revision, and the general resubmission/highest-score
mechanics (points 1–5) apply identically regardless of what triggered the
revision. **Consistent.**

**E. Checkpoint boundary** — Point 1's second and third sentences directly
state that a later checkpoint does not, by itself, close an earlier gate to
revision, that a checkpoint "must not become a gradebook guillotine," and
that only an explicit, separately authoritative boundary (e.g., the
end-of-course grading deadline) can actually close submission. This
reproduces the prompt's own required framing nearly verbatim and is the
scenario the prompt was most concerned about. **Consistent.**

## Validation commands / results

```
$ git diff --check
(no output; exit 0)

$ git diff --name-status
M       docs/grading-model.md

$ grep -rniE "too late|no credit|not accepted|closed submission|cannot be resubmitted|zero credit|final grade stands" --include="*.md" .
(no DSCT-source hits; only unrelated matches in an untracked draft prompt file, outside this prompt's scope)
```

## Decisions that still genuinely require Jeremy + ChatGPT

- The exact end-of-course institutional hard-close date/time.
- Whether DSCT wants any course-specific exception to the shared late-work
  default (the canonical policy allows explicit, justified per-course
  exceptions; none is requested or invented here).
- The concrete Canvas/Savnac mechanism for "the submission system can still
  accept the work" (e.g., whether assignments stay permanently open or use
  a long resubmission window) — a pure deployment choice, not a doctrine
  choice.
- How/where the highest-of-attempts comparison is implemented in the
  grading pipeline (DSCT-specific adapter vs. reused `course_foundry`
  mechanism) — explicitly out of scope per the hard stop on Marker/Course
  Foundry code.

## Final commit SHA / working-tree state

Working tree at report time (before this report's own commit): one file
modified (`docs/grading-model.md`), diff-clean, no other pending changes on
this branch. This report and the `docs/grading-model.md` edit are committed
together as a single logical change (see git log after commit).
