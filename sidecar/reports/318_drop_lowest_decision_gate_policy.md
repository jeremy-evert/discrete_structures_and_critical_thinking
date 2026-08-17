# Report 318 — Drop one regular Decision Gate policy

**Prompt:** `sidecar/prompts/318_define_drop_lowest_decision_gate_policy.md`
**Branch:** `worker/prompt318-drop-lowest`
**Worktree:** `/tmp/dsct-prompt318` (isolated; main shared checkout was never
touched)
**Starting commit SHA:** `219af60` (`origin/main` at worktree creation —
"Accept Prompt 309: World Bible cross-course provenance map")
**Final commit SHA:** `2d67ec5` — "Add drop-one-regular-Decision-Gate policy
to grading model (Prompt 318)"

## 1. Prerequisite confirmation

The dispatch briefing asserted Prompts 314, 315, and 317 were already
accepted and merged to `main`. Verified directly by reading current
`docs/grading-model.md` at the worktree's starting SHA rather than trusting
the prompt file's own description of prior state, per instructions:

- **Prompt 314 (Decision Gate contract):** confirmed landed. The grading
  table names the category `Decision Gate (weekly reinforcement category)`
  at 30%, with the internal gradebook name `weekly reinforcement` explicitly
  kept distinct from the student-facing name, matching Prompt 314's settled
  decision.
- **Prompt 315 (checkpoints + Farkle synthesis):** confirmed landed. The
  table shows `Reasoning Odyssey checkpoints` at 15% (Weeks 7, 11, 14, each
  one-third) and a separate `Farkle + Machine Learning Synthesis` row at 5%
  (Week 16 only, explicitly "not part of" the Decision Gate category). The
  "Aggregate check" section sums `45% Odyssey (Decision Gates + checkpoints)
  + 45% other recurring work + 5% Farkle + ML Synthesis + 5% final = 100%`.
- **Prompt 317 (revision/resubmission/highest-score):** confirmed landed. A
  full `## Revision, resubmission, and highest-score policy` section exists
  at the end of `docs/grading-model.md`, dated 2026-08-17, stating the
  highest-recorded-score-across-attempts rule this prompt's Scenario B/C
  depend on.

Because main was ahead of what the Prompt 318 author could see, its own
"Settled surrounding doctrine" list (weights, checkpoint placement, highest-
score rule) was treated as already reflected in current source, and only the
narrow drop-lowest addition itself was implemented.

## 2. Files inspected

- `docs/grading-model.md` (edited — see below)
- `planning/fall-2026-weekly-architecture.md` — read in full around its
  "Reasoning Odyssey continuity and grading map" and "Exceptions" sections
  (lines ~100–160). No drop-lowest, per-attempt, or category-arithmetic
  language present; it only maps chassis slots to category names. No edit
  needed.
- `planning/fall-2026-topic-map.md` — grepped for `Decision Gate`, `weekly
  gate`, `drop-lowest`; zero hits. No edit needed.
- `assignments/weekly-problem-solving-writeup.md` — the reusable Decision
  Gate template; grepped for `Decision Gate`, `30%`, `drop`, `category`,
  `late`, `revision`, `highest`. Only one relevant line, describing it as a
  reusable structure a week's Decision Gate "may use... directly or adapt";
  it carries no scoring/category arithmetic to update. No edit needed.
- `assignments/week-16-farkle-evidence-receipt.md` (checked by name/role only
  — confirmed via `docs/grading-model.md` that Farkle+ML is its own category,
  not a Decision Gate; no drop-lowest language present there to begin with).
- `sidecar/prompts/314_define_decision_gate_contract.md`,
  `315_define_odyssey_checkpoints_and_farkle_synthesis.md`,
  `317_define_revision_resubmission_highest_score_policy.md` — read for
  provenance/terminology consistency (category names, "regular Decision
  Gate" phrasing, order-of-operations phrasing reused verbatim where
  applicable).
- `sidecar/reports/305_reasoning_vocabulary_inventory.md` — not re-read in
  full for this prompt; Prompt 314's own report already digested and applied
  its terminology guidance, and this prompt makes no new naming decisions.
- Full-repo grep for stale terms: `drop lowest`, `drop-lowest`, `weekly
  gate`, `Reasoning Odyssey gate`, `Reasoning Quest`, `Decision Gate`, `late
  work`, `resubmit`, `revision`, `highest score`. Hits outside
  `docs/grading-model.md` are confined to: (a) `sidecar/prompts/*` and
  `sidecar/reports/*` (prior prompts/reports — provenance, left untouched
  per "use historical files only as provenance, do not rewrite archives"),
  and (b) `sidecar/raw/*` design dumps (raw historical notes — left
  untouched for the same reason). No stale drop-lowest language exists
  outside those archival locations and `docs/grading-model.md` itself.

## 3. Current-state conflicts found

One, narrowly scoped: the closing paragraph of the "Chassis and rotation
boundaries" section in `docs/grading-model.md` still listed `drop-lowest
behavior` as an open "deployment question," and separately claimed only the
checkpoint weeks and Farkle placement were "settled by Prompt 315." Both
statements were accurate when written but are now stale given Prompt 318's
settled policy. No other conflicts were found — no other file asserted or
implied a different drop-lowest rule, a different eligible category set, or
different order-of-operations.

## 4. Files changed

- `docs/grading-model.md` only, two edits:
  1. Added a new `## Drop one regular Decision Gate` section immediately
     after the existing revision/resubmission/highest-score section,
     containing the exact policy statement, the four-step order of
     operations, eligibility/non-eligibility lists, the missing-gate
     carve-out, and the rationale paragraph distinguishing this rule from
     continuous late work and from the revision/highest-score policy.
  2. Updated the trailing sentence of that revision section (which
     previously said only resubmission-window mechanics and the hard-close
     date were deployment seams) and the closing paragraph of the "Chassis
     and rotation boundaries" section (which previously listed drop-lowest
     behavior as an open deployment question) so both now correctly state
     that the drop-lowest **policy** is settled by Prompt 318 and only its
     gradebook/compiler **wiring** remains a deployment seam.

No other source file required a change.

## 5. Exact final policy wording

As landed in `docs/grading-model.md`:

> **Drop one regular Decision Gate:** after each Decision Gate has resolved
> to its retained highest recorded score across attempts, omit the single
> lowest regular Decision Gate score from the 30% Decision Gate category
> calculation.

Order of operations:

1. Grade each attempt for academic quality.
2. Apply the canonical late-work adjustment to that attempt where
   applicable.
3. For each regular Decision Gate, retain the student's highest recorded
   attempt score (the policy above).
4. Across the student's regular Decision Gates, omit the single lowest
   retained Decision Gate score from the 30% category calculation.

Eligible: regular Decision Gates in the recurring 30% Decision Gate category
only, including a never-submitted regular gate recorded as zero/missing.

Not eligible: Reasoning Odyssey Checkpoints (15%, Weeks 7/11/14), Week 16
Farkle + Machine Learning Synthesis (5%), Pair Reasoning reports, Show & Tell
reports, or any other non-Decision-Gate category.

## 6. Required verification scenarios

**Scenario A — ordinary lowest score drops.** Retained regular-gate scores
`92, 88, 95, 74, 91`. Step 4 identifies `74` as the single lowest retained
score among the five regular gates and omits it; the category calculation
uses `92, 88, 95, 91`. Verified: `74` is dropped.

**Scenario B — revision changes which gate is dropped.** Initial retained
scores: Gate X = `60` (dropped), Gate Y = `72`, others higher. Gate X is
later revised and its retained score rises to `89` (step 3: highest-recorded-
score policy replaces `60` with `89` because `89 > 60`). Step 4 is
re-evaluated on the new retained set; Gate Y at `72` is now the lowest
regular retained score and becomes the dropped gate instead of Gate X.
Verified: `72`, not the improved gate, is omitted — matching the spec's
"the identity of the dropped gate can change automatically" statement.

**Scenario C — later weaker resubmission cannot hurt.** Gate retains `90`.
A later attempt, after quality grading and late adjustment, records `81`.
Step 3 (Prompt 317's highest-recorded-score rule) compares `81` against the
existing retained `90`; since `81 < 90`, the retained score stays `90`. This
resolution happens entirely inside step 3, before step 4's drop logic ever
runs, so the drop-lowest rule never even observes the `81` attempt. Verified:
the gate still retains `90` before — and after — the category drop logic is
applied.

**Scenario D — one missing gate.** A student has exactly one never-submitted
regular Decision Gate (recorded as 0/missing) plus otherwise-completed
regular gates, e.g. `0, 85, 90, 88, 93`. Step 4 finds `0` is the lowest
retained score among regular gates and it is eligible per the "Missing and
zero-score behavior" rule, so it becomes the dropped gate; the category
calculation uses `85, 90, 88, 93`. Per the settled rule, this does not close
the assignment — it remains open for late submission/revision under Prompt
317 and the canonical late-work policy while the course submission system is
open. If the student later submits and its retained score rises above `0`,
step 4 re-evaluates: the drop would then move to whichever regular gate is
newly lowest (which could again be this gate, at its new low-but-nonzero
score, or a different gate, depending on the resulting set). Verified: the
missing gate may consume the single drop without the assignment being closed.

**Scenario E — special objects are protected.** A low Week 7/11/14
checkpoint score, a low Week 16 Farkle + ML score, a low Pair Reasoning
score, and a low Show & Tell score all live in categories other than the 30%
Decision Gate category (15%, 5%, 5%, 5% respectively, per the landed Prompt
315/312 category table). Step 4 of the policy is scoped explicitly to "the
student's regular Decision Gates" only, and the "Not eligible for the drop"
list in the landed text names all four of these categories by name. None of
them can be selected as the single dropped item regardless of how low their
score is. Verified: all four are protected.

## 7. Deployment seam

DSCT source doctrine is now unambiguous on the drop-lowest policy itself
(what gets dropped, in what order, and what is protected). What remains an
external deployment seam, not decided here:

- how the highest-recorded-score comparison (Prompt 317) and the drop-lowest
  comparison (this prompt) are actually computed and wired together inside
  whatever grading engine/compiler DSCT eventually uses (e.g. Course Foundry,
  or a Canvas/Savnac weighted-assignment-group mechanism with a native
  "drop lowest N" feature, if one is used instead);
- exact Canvas/Savnac object IDs and due dates for each regular Decision
  Gate, which determine what "regular Decision Gate" resolves to as a
  concrete list of gradebook items each semester;
- whether the eventual gradebook implementation recomputes the drop
  dynamically on every new submission/regrade event, or on a batched
  schedule — this report specifies the required *result* (drop is
  re-evaluated whenever a retained score changes) but does not mandate an
  implementation mechanism, per the hard-stop against implementing external
  grading-engine changes here.

This report documents the seam precisely and stops at the DSCT repository
boundary, per the prompt's hard stops. No later prompt has authorized
cross-repository implementation of this seam as of this report.

## 8. Confirmation: no Canvas/Savnac write occurred

Confirmed: this job made no network calls, no Canvas API/Savnac API
interaction, and no write to any external grading system. All work was
read/grep/edit operations against files inside the isolated worktree
`/tmp/dsct-prompt318`, followed by a local commit and (per instructions) a
push of the branch to `origin` — `git push` to the DSCT source repository
only, not to any Canvas or Savnac endpoint.

## 9. Hard-stop compliance check

- 30% Decision Gate weight: unchanged.
- 15% checkpoint weight: unchanged.
- 5% Farkle + ML weight: unchanged.
- No additional drops created (single drop only).
- No checkpoint or special category made droppable.
- Canonical late-work arithmetic: not touched; `docs/grading-model.md`
  continues to defer to the shared curriculum / Course Foundry adapter as
  before.
- Revisions/resubmissions at checkpoints: not closed; Prompt 317 language
  left intact.
- No new final-submission cutoff invented.
- No other grading category redistributed.
- Week 4–14 topic spine: not touched.
- World Bible contract: not touched.
- Canvas/Savnac: not touched (see §8).
- Jeremy Task Tracking: not touched.
- No opportunistic cleanup performed beyond the two bounded edits described
  in §4; other stale-term hits found by the required grep sweep were left in
  their archival locations (`sidecar/prompts/*`, `sidecar/reports/*`,
  `sidecar/raw/*`) as provenance, per instructions not to rewrite archives.

## 10. Git discipline notes

One logical change, one commit (`2d67ec5`), scoped entirely to
`docs/grading-model.md`. `git diff --check` was run and reported no
whitespace issues. No concurrent/untracked work was present in the isolated
worktree to preserve or disturb. Branch `worker/prompt318-drop-lowest` was
pushed to `origin`; not merged to `main`.
