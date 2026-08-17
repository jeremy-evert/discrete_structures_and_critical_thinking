# Report 315 — Odyssey checkpoints and Farkle + ML synthesis

**Status:** COMPLETE (semantic category structure only)
**Prompt:** `sidecar/prompts/315_define_odyssey_checkpoints_and_farkle_synthesis.md`
**Branch:** `worker/prompt315-checkpoints-farkle-v2`

## 1. Starting commit SHA

`419b55bf1410670597ebe271138e6bd50577e0f2` (`origin/main` at worktree creation
time). A fresh isolated worktree was created at
`/tmp/dsct-prompt315`, branch `worker/prompt315-checkpoints-farkle-v2`, per
the shared-checkout collision warning. All reads/writes/commits happened
inside that worktree only.

While work was in progress, `origin/main` advanced by two more commits
(Prompt 310 acceptance, `ce23128`, `4b1bf56`), touching only
`sidecar/reports/310_dsct_stale_source_seam_inventory.md` — no overlap with
this prompt's files. The branch was intentionally left based at `419b55b`
rather than rebased, since there is no conflict; the accepting maintainer can
fast-forward/merge normally.

## 2. Prompt 312 and Prompt 314 dependency status — IMPORTANT DISCREPANCY

**The task briefing that dispatched this work stated Prompt 314 was "already
accepted and merged to main." This is incorrect as of this job.** Verified
directly:

```
$ git merge-base --is-ancestor bf059e7 origin/main && echo YES || echo NO
NO
$ git merge-base --is-ancestor 8951f1b origin/main && echo YES || echo NO
NO
```

Neither Prompt 312 (`worker/prompt312-show-and-tell`, report
`sidecar/reports/312_show_and_tell_contract.md`) nor Prompt 314
(`worker/prompt314-decision-gate`, report
`sidecar/reports/314_decision_gate_contract.md`) is merged into `origin/main`.
Both exist only as unmerged worker branches with completed reports. This
worktree's base checkout of `origin/main` therefore still has the **old**
9-recurring-category grading table (separate A4 "Show-and-Tell reflection"
and A7 "Friday feedback report" rows, no "Decision Gate" terminology
anywhere).

Per this prompt's own instruction — *"If Prompt 314 has not completed, avoid
simultaneous conflicting edits. Implement the checkpoint/Farkle decisions
only where safe and clearly report the remaining dependency"* — I did **not**
merge or cherry-pick either unmerged branch's full diff (which also touches
unrelated files: Week 2 assessment fixtures, `week-01/README.md`,
`assignments/show-and-tell-artifact.md`, etc., none of which are this
prompt's authority). Instead I:

- Consumed both branches' **reports** as settled doctrine (both are complete,
  reviewed, and directly named/relied-upon by Prompt 315's own text), and
- Reproduced, in `docs/grading-model.md` only, the two narrow, textually
  unambiguous prerequisite edits Prompt 315 explicitly assumes as background
  ("Decision Gate" as the canonical weekly name; the A7/Friday-feedback fold
  into Show & Tell as the source of the freed 5%) — the same edits already
  present, worked out independently, and reasoned about identically in the
  312 and 314 branches' own diffs to that file.
- Left every other file those two branches touch completely alone.

**Remaining dependency returned to Jeremy + ChatGPT / Foreman:** when Prompt
312 and/or Prompt 314 are actually merged to `origin/main`, `docs/grading-model.md`
will very likely need a manual 3-way reconciliation, since this branch's
edits to that file overlap the same rows/prose those branches touch
independently from the same original base. The semantic content should
match (I replicated their settled decisions), but a textual merge conflict
in `docs/grading-model.md` should be expected and is not a sign of a wrong
decision — it is duplicate parallel authorship of the same settled outcome
from three unmerged branches. Recommend merging 312 and 314 to main first,
then rebasing/reapplying this branch's checkpoint/Farkle-specific delta on
top (which is small: two new table rows, the checkpoint-week exclusion
clause, and the Week 16 category-placement sentences in five other files).

## 3. Files inspected

- `sidecar/prompts/315_define_odyssey_checkpoints_and_farkle_synthesis.md` (full spec)
- `sidecar/reports/314_decision_gate_contract.md` (read from `origin/worker/prompt314-decision-gate`, since absent on `main`)
- `sidecar/reports/312_show_and_tell_contract.md` (read from `origin/worker/prompt312-show-and-tell`, since absent on `main`)
- `docs/grading-model.md`
- `docs/career-connection.md` (checkpoint/gate cross-references only; not edited — see §4)
- `planning/fall-2026-topic-map.md` (Weeks 7/11/14 technical content, confirming the checkpoint-placement rationale; not edited — no grading language present)
- `planning/fall-2026-weekly-architecture.md`
- `planning/week-16.md`
- `week-16/README.md`, `week-16/instructor/guide.md`, `week-16/student/farkle-evidence-lab.md`, `week-16/fallback/quick_v1_results.csv` (grepped for grading language; none found beyond `planning/week-16.md`)
- `assignments/week-16-farkle-evidence-receipt.md`
- `planning/week-16-farkle-ml-plan.md`
- `planning/week-16-farkle-ml-target-map.md`
- `sidecar/reports/week16_farkle_ml_current_state.md`, `sidecar/reports/week16_farkle_ml_postmortem.md`, `sidecar/runs/week16_farkle_validation_20260816T211906Z.md` (read to confirm GREEN preservation boundary; not edited)
- `reports/304_dsct_grading_model.md` (historical point-in-time report; deliberately not edited, matching the provenance-preservation pattern already established by Prompt 312)

## 4. Files changed/created

Changed (6 files, no files created):

- `docs/grading-model.md` — grading table (Show & Tell/A7 fold, Decision Gate rename, checkpoint-week specificity, new Farkle + ML Synthesis row), aggregate-check arithmetic, and the "Chassis and rotation boundaries" prose.
- `planning/week-16.md` — "Grading placement" section only.
- `assignments/week-16-farkle-evidence-receipt.md` — one "Purpose" sentence only.
- `planning/week-16-farkle-ml-target-map.md` — one "Evidence receipt map" sentence only.
- `planning/week-16-farkle-ml-plan.md` — one "Evidence criteria" paragraph only.
- `planning/fall-2026-weekly-architecture.md` — the Question-004 grading-category mapping bullet and the Week 16 exceptions-list entry.

No file in `week-16/`, `lessons/`, `sidecar/reports/week16_farkle_ml_*`, or
`sidecar/runs/` was touched. No planning/topic-map spine restructuring, no
Pair Reasoning or Show & Tell contract file edit, no World Bible edit.

## 5. Final checkpoint semantics

- **Decision Gate** (30%, unchanged total) = the normal recurring individual
  weekly reasoning submission, on every active week **except** Weeks 7, 11,
  and 14.
- **Reasoning Odyssey Checkpoints** (15% total, unchanged) = three equal
  one-third (5% each) synthesis milestones in **Weeks 7, 11, and 14**. On a
  checkpoint week, the checkpoint is the week's *only* Odyssey submission —
  it replaces that week's Decision Gate rather than adding to it. A
  checkpoint requires synthesis of the student's own prior Decision
  Gate/course evidence across multiple weeks (what changed, what proved
  durable, what remains untested), not a new technical project.
- **Farkle + Machine Learning Synthesis** (5%, new standalone category) =
  Week 16 only. Not a Decision Gate, not a checkpoint, not folded into the
  30% or 15% categories.

## 6. Rationale/source evidence for Weeks 7, 11, and 14

Directly consumed from `planning/fall-2026-topic-map.md`'s canonical
Weeks 3–14 spine (unedited by this prompt, read only for confirmation):

- **Week 7** (`Wk 7 · Sep 29/Oct 1`) closes the induction/recursion/recurrence
  arc, the last topic in the logic→proof→representation→algorithms→integers→
  induction sequence — matching the prompt's "first major formal-reasoning
  arc" description exactly.
- **Week 11** (`Wk 11 · Oct 27/29`) is Graphs & Network Reasoning, immediately
  after counting (Wk 8), probability (Wk 9, whose Thursday is Fall Break —
  confirmed in the topic map row and in `fall-2026-weekly-architecture.md`'s
  Week 9 exception), and relations (Wk 10) — matching the prompt's
  "counting → uncertainty → relations → graphs" synthesis-point description.
- **Week 14** (`Wk 14 · Nov 17/19`) is already labeled in the topic map's own
  "Thu mode" column as `Show & Tell / Reasoning Odyssey mini-capstone ·
  state-machine runner/model defense`, i.e., the existing end-of-spine
  synthesis/model-limits location — matching the prompt's description
  precisely and requiring no spine change.

No topic-map edit was needed or made; the placements were already
structurally supported by the existing spine.

## 7. Proof that checkpoint weeks do not double-submit an ordinary gate

`docs/grading-model.md`'s Decision Gate row now reads: "...excluding Weeks 7,
11, and 14, which submit their Reasoning Odyssey Checkpoint instead of an
ordinary Decision Gate that week (no double submission)." The checkpoint
row's own description states a checkpoint is "the week's *only* Odyssey
submission — it replaces, not adds to, that week's Decision Gate." The
"Chassis and rotation boundaries" prose repeats this explicitly: "On a
checkpoint week, the checkpoint *is* that week's Odyssey submission; no
separate ordinary Decision Gate is also collected for the same week."
`planning/fall-2026-weekly-architecture.md`'s Question-004 mapping bullet
was edited to state the same exception directly at the point where it
previously implied every week (including 7, 11, 14) fed the ordinary weekly
category.

**Anti-bureaucracy walkthrough — Week 7:** Under the new source, a Week 7
student produces exactly one Odyssey object: the Checkpoint 1 synthesis,
built from their Tuesday/Thursday Week-7 reasoning work (logic/proof/
induction) plus a required look back across prior weeks' Decision Gates. They
do **not** also separately submit an ordinary Week 7 Decision Gate — the
grading-model row explicitly excludes Week 7 from the Decision Gate's graded
weeks. This matches the prompt's own required walkthrough result.

## 8. Final Week 16 Farkle + ML category placement

Own standalone 5% "Farkle + Machine Learning Synthesis" category. Removed
from the Decision Gate category's graded weeks (previously included via
"including Week 16 Farkle + ML synthesis," now removed with an explicit
redirect note). Not one of the three checkpoints. Confirmed consistent across
`docs/grading-model.md`, `planning/week-16.md`, `assignments/week-16-farkle-evidence-receipt.md`,
`planning/week-16-farkle-ml-plan.md`, `planning/week-16-farkle-ml-target-map.md`,
and `planning/fall-2026-weekly-architecture.md`.

## 9. Before/after grading arithmetic and 100% check

**Before (this worktree's `origin/main` starting state, pre-312/pre-314):**

```
9 recurring 5% categories (kickoff, AI Fluency, Wacky Wed, Fun Fri, A3,
  A4 Show-and-Tell, A7 Friday-feedback, career artifact, attendance) = 45%
+ technical presentation 3%
+ course evaluation 2%
+ Weekly reinforcement / Reasoning Odyssey gate 30% (included Week 16)
+ Reasoning Odyssey checkpoints 15% (unplaced weeks)
+ Final individual reflection 5%
= 100%
```

**After this prompt's edits:**

```
8 recurring 5% categories (kickoff, AI Fluency, Wacky Wed, Fun Fri, A3,
  Show & Tell [A4, now also covering retired A7], career artifact,
  attendance) = 40%
+ technical presentation 3%
+ course evaluation 2%
= 45% (non-Odyssey, non-Farkle, non-final recurring work)

+ Decision Gate 30% (Weeks 3-14 minus 7, 11, 14; excludes Week 16)
+ Reasoning Odyssey Checkpoints 15% (Checkpoint 1 Wk 7 / Checkpoint 2 Wk 11 /
  Checkpoint 3 Wk 14, 5% each)
= 45% (Odyssey family)

+ Farkle + Machine Learning Synthesis 5% (Week 16 only, new standalone
  category, funded by the Prompt 312 A7 retirement, not by reducing any
  other category)

+ Final individual reflection 5%

Total = 45 + 45 + 5 + 5 = 100%
```

Direct table sum: `5+5+5+5+5+5+5+5+3+2+30+15+5+5 = 100`. Confirmed no category
listed in the prompt's hard-stop list (Decision Gates 30%, checkpoints 15%,
Farkle 5%, Show & Tell 5%, Pair Reasoning 5%) was reduced to fund the new
category; the 5 points came entirely from the already-settled Prompt 312 A7
retirement, exactly as Prompt 315 directs.

## 10. Distinct-evidence audit answers

**What evidence would disappear if the checkpoint category were removed?**
The longitudinal synthesis evidence: a claim the student changed, narrowed,
rejected, or strengthened across multiple weeks; a named recurring reasoning
weakness/blind spot the student can now see; identification of which piece
of prior evidence/proof/model/counterexample/test the student now regards as
especially strong and why; an explicit account of where confidence rose or
fell for a justified reason; and an unresolved question or model limit that
could still change the student's mind — all with explicit pointers back to
the specific prior Decision Gates being synthesized. This is not recoverable
from "the Week 7/11/14 technical assignment" alone, since that assignment
(now excluded from the Decision Gate category on checkpoint weeks) only
produces that week's own reasoning trace, not a cross-week comparison of how
the student's reasoning has changed.

**What evidence would disappear if the Farkle + ML category were removed?**
The special cross-topic endgame synthesis: evidence that the student can (a)
combine probability/simulation reasoning, algorithmic/model evidence, and
repeated-measurement discipline into one end-of-semester judgment about a
Farkle strategy claim, (b) name the evidence boundary of what a computational
comparison can and cannot establish, (c) apply AI skepticism to a "fluent"
interpretation of the results, and (d) either defend, revise, or *refuse* to
declare a winner for a justified reason. This is distinct from "another
Decision Gate" because it requires synthesizing multiple semester-long
reasoning skills against one shared computational artifact, not producing a
single week's own reasoning trace.

## 11. Validation commands/results

```
$ git diff --cached --check
(no output — clean)

$ git diff --cached --name-only
assignments/week-16-farkle-evidence-receipt.md
docs/grading-model.md
planning/fall-2026-weekly-architecture.md
planning/week-16-farkle-ml-plan.md
planning/week-16-farkle-ml-target-map.md
planning/week-16.md

$ grep -rn "A7 equivalent\|Friday feedback report" docs/ planning/ assignments/
(no output — no stale A7/Friday-feedback language remains)

$ grep -rln "Decision Gate" docs/ planning/ assignments/
planning/fall-2026-weekly-architecture.md
docs/grading-model.md
assignments/week-16-farkle-evidence-receipt.md
planning/week-16-farkle-ml-plan.md
planning/week-16.md
planning/week-16-farkle-ml-target-map.md

$ grep -rn "Farkle + Machine Learning Synthesis" docs/ planning/ assignments/
(6 files, all category-placement statements — see §3/§8 above)

$ git diff --cached -- week-16/ lessons/ sidecar/reports/week16_farkle_ml_current_state.md sidecar/reports/week16_farkle_ml_postmortem.md sidecar/runs/ | wc -l
0
```

Full diff was inspected file-by-file; every changed line is a grading-
category/placement statement, none is a change to Week 16's central
question, semester payoff, Tuesday/Thursday task lists, validation evidence,
required path, or any Weeks-7/11/14 technical/topic content.

## 12. Unresolved seams returned to Jeremy + ChatGPT

1. **Prompt 312 and Prompt 314 are not actually merged to `origin/main`**,
   contrary to the dispatching task's premise. `docs/grading-model.md` was
   independently, narrowly edited on this branch to reproduce the two
   settled prerequisite decisions those branches already made (the A7 fold,
   Decision Gate naming), specifically because Prompt 315's own text and
   arithmetic assume they're already true. When 312/314 are actually merged,
   expect (and plan for) a manual textual merge/rebase of this branch's
   `docs/grading-model.md` changes — the semantics should already agree, but
   the diffs will collide line-for-line since three branches independently
   edited the same table from the same unmerged base.
2. Per-checkpoint rubric wording (the "exact student-facing template" the
   prompt explicitly leaves open) is not authored here — only the category
   structure, placement, and anti-duplication rule.
3. Exact Canvas/Savnac object IDs, due dates, late/drop-lowest policy for
   checkpoints and Farkle + ML remain deployment questions, per the prompt's
   explicit hard-stop boundary (not decided here).
4. World Bible contract and final topic-spine label reconciliation remain
   explicitly out of this prompt's authority and were not touched.

## 13. Final commit SHA / working-tree state

Committed on `worker/prompt315-checkpoints-farkle-v2` and pushed to
`origin/worker/prompt315-checkpoints-farkle-v2`. Not merged to `main` (per
instruction). See the commit log for the final SHA — this report was
committed together with the source changes in one commit.
