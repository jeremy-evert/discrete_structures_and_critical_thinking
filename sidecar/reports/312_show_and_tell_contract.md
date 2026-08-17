# Report 312 — DSCT Show & Tell contract

**Status:** COMPLETE (semantic category structure only; one arithmetic seam explicitly returned unresolved)
**Prompt:** `sidecar/prompts/312_define_show_and_tell_contract.md`
**Branch:** `worker/prompt312-show-and-tell`

## 1. Starting commit SHA

`2ec8ea82b822a96d6bec987bb0306e51ce51376c` (local/origin `main` at time of branch creation).

## 2. Files inspected

- `docs/grading-model.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `planning/fall-2026-course-design.md`
- `assignments/show-and-tell-artifact.md`
- `assignments/pair-reasoning-report.md`
- `docs/career-connection.md`
- `docs/curriculum/course-sequence.md`
- `docs/philosophy/teaching-patterns.md`
- `docs/reports/curriculum-history-synthesis.md`
- `reports/304_dsct_grading_model.md` (historical, not edited — see §4)
- `sidecar/prompts/311_define_pair_reasoning_contract.md` (cross-reference only, not modified)
- `sidecar/reports/305_reasoning_vocabulary_inventory.md` (prior open-question inventory; confirms this prompt's decisions were the flagged open seams)
- `week-02/instructor/thursday-run-of-show.md`, `week-02/` tree (grepped for Friday-feedback/A7/Show & Tell terms — none found)
- Full repo grep for `friday feedback|a7|show.?and.?tell|pair reasoning` (see §11)

No standalone `templates/weekly-rubric.md`-style rubric file existed for Show & Tell; the small rubric required by the prompt is now embedded directly in `assignments/show-and-tell-artifact.md`, matching the existing house style (`templates/weekly-rubric.md`, `week-02/student/week-02-evidence-rubric.md`).

## 3. Historical A4/A7 evidence consulted

No standalone current Friday-feedback/A7 assignment or rubric file exists in this repository. `sidecar/reports/305_reasoning_vocabulary_inventory.md:63` had already confirmed this: "no standalone A7 assignment template was found." The only current source expressing the A7-equivalent category was the now-removed row in `docs/grading-model.md` and its cross-references in `planning/fall-2026-weekly-architecture.md` and `reports/304_dsct_grading_model.md` (historical report, left as provenance — see §4). There was therefore nothing separate to retire as a file; the retirement is entirely a grading-model/authoring-doc reconciliation, not a file deletion.

## 4. Files changed/created/retired

Changed:
- `docs/grading-model.md` — merged the separate "Friday feedback report (A7 equivalent)" row into the "Show & Tell report (A4 equivalent)" row; updated the aggregate-check math and prose to reflect 8 recurring 5% categories instead of 9; added an explicit "Prompt 312 arithmetic seam" callout instead of silently re-balancing to 100%; updated the chassis/rotation prose that referenced "A4-equivalent and A7-equivalent categories."
- `planning/fall-2026-weekly-architecture.md` — updated the Thursday chassis table so the Pair-Reasoning-or-Show-&-Tell segment explicitly requires giving a peer professional critique, and the wrap-up segment explicitly names the individual Show & Tell report as the object that records both critique received and critique given, cross-referencing the new assignment contract and Prompt 312.
- `assignments/show-and-tell-artifact.md` — fully rewritten from a two-sentence stub into the canonical student-facing Show & Tell contract (see §5).

Created: none (the assignment file was rewritten in place, not added as a new file).

Retired: no standalone Friday-feedback/A7 file existed to retire (see §3). `reports/304_dsct_grading_model.md` is a historical point-in-time report and was deliberately **not** edited — it remains accurate provenance of what the model said before Prompt 312, consistent with "preserving historical/provenance evidence where appropriate."

Untouched deliberately: `planning/fall-2026-topic-map.md` (already only names "Show & Tell" generically per week, no A4/A7 language to reconcile), `docs/career-connection.md`, `docs/curriculum/course-sequence.md`, `docs/philosophy/teaching-patterns.md`, `docs/reports/curriculum-history-synthesis.md` (historical/adjacent mentions of "show-and-tell" as a lowercase generic activity name, not the graded-category contract; no A7/Friday-feedback language present).

## 5. Final canonical Show & Tell contract summary

`assignments/show-and-tell-artifact.md` now states:

- Show & Tell = public explanation and defense under questions, not presentation theater, on Weeks 4, 6, 8, 10, 12, 14.
- Four distinct products per event: (1) the week's technical artifact (graded elsewhere, not duplicated here), (2) the live public defense, (3) the individual Show & Tell report, (4) the required professional critique given to a peer, captured inside the same report.
- The report compresses the prompt's seven semantic elements into four student-facing prompts: claim defended + strongest evidence; strongest challenge received; what survived/changed + evidence boundary; and professional critique given to a peer + why it was useful.
- States the critique norm verbatim ("Critique the claim, assumption, evidence, inference, or model. Do not attack the reasoner.") and explicitly allows critique-under-agreement.
- Provides a five-row scoring contract (public claim/evidence, response to challenge, evidence-boundary awareness, professional critique given, individual accountability) and explicitly disclaims rewarding speaking polish, disagreement for its own sake, or rhetorical dominance.
- Closes with an explicit Pair Reasoning distinction paragraph.

## 6. How public defense and professional critique coexist in one event

Both are structurally required in the same Thursday Show & Tell slot and the same individual report: the ~50–55 minute segment in `planning/fall-2026-weekly-architecture.md` is where a student defends their own claim under audience questions *and* is expected to raise at least one professional critique of someone else's claim during the same event; the individual report then requires both halves (defense-side fields 1–3, critique-given field 4) in one submission, so neither skill can be produced without the other.

## 7. How the technical artifact and Show & Tell report remain distinct

The assignment file's "Four distinct things this week produces" section names the technical artifact first and states explicitly that Show & Tell "does not require a duplicate submission of it" and that the report should "not restate the technical artifact." The report's four fields ask only about what happened *when the reasoning became public* (claim + evidence shown, challenge received, revision/boundary, critique given) — none of which exist without the public event, unlike the technical artifact, which exists independent of Show & Tell.

**Anti-duplication test answer:** If the Show & Tell report were removed, the evidence that would disappear is: (a) the record of which claim was defended and what was publicly claimed as its strongest support, (b) the record of the strongest audience challenge and how the student responded (preserved/revised/narrowed/corrected/left unresolved), (c) the student's own statement of the evidence boundary, and (d) the record of the professional critique the student gave to a peer and why it was useful. None of this is the week's technical artifact itself — it is evidence of public defense, response to challenge, evidence-boundary awareness, and critique given, matching the prompt's required correct answer.

## 8. Scenario walkthrough results

1. **Presenter is wrong or overclaims, peer exposes a real flaw, presenter revises:** Field 3 ("what survived or changed") explicitly lists "corrected" and "rejected" as legitimate outcomes, and the rubric's "Response to challenge" row grants full credit for honestly capturing this, not for having been right originally. Rewarded.
2. **Presenter survives serious challenge, claim remains justified:** Field 3 explicitly lists "preserved" as a legitimate outcome alongside "strengthened." The rubric does not penalize a claim that survives scrutiny; it rewards the honest capture of what was tested. Rewarded.
3. **Peer agrees, student still must produce useful critique:** The critique-norm section states directly: "Agreeing with a peer is not an exemption from giving critique — probe whether the evidence deserves the confidence claimed." Field 4 requires a critique regardless of agreement. Rewarded.
4. **Non-programming week (proof, counterexample, counting argument, relation/model):** The technical-artifact list in the assignment ("proof, model, simulation, code, representation, derivation, graph, truth table, or evidence set") and the topic map's Show & Tell weeks (4 sets/functions, 6 crypto, 8 counting, 10 relations, 12 trees, 14 FSM) are non-code-centric by default; the report's four fields never mention code or programming, so they apply unchanged to a proof, counterexample, or counting-argument week. Rewarded.

All four cases reward critical professionalism (naming what was tested and how it was resolved) rather than combat or empty praise, per the rubric's explicit exclusions.

## 9. Pair Reasoning distinction check

`assignments/show-and-tell-artifact.md`'s closing section and `sidecar/prompts/311_define_pair_reasoning_contract.md`'s own framing state the distinction semantically, not by calendar rotation: Pair Reasoning = "what happened to my reasoning when another reasoner worked closely inside the problem with me" (close collaborative challenge inside the process); Show & Tell = "what happened when I made my reasoning public, defended it under questions, and professionally challenged someone else's reasoning" (public defense plus professional critique of a peer). Prompt 311's settled 5% Pair Reasoning contract and category were not reopened, reworded, or second-guessed by this work; `assignments/pair-reasoning-report.md` was read for cross-reference only and left unmodified.

## 10. Grade-boundary audit

- **Show & Tell remains exactly 5%:** confirmed — `docs/grading-model.md`'s merged row still reads `5%`.
- **Separate Friday-feedback/A7 category removed/folded, not left as another 5%:** confirmed — the old second row is gone; the merged row's description explicitly states it now covers "both public defense of a claim and required professional critique of a peer."
- **No unrelated category weight changed:** confirmed by diff — only the Show & Tell/A7 row and the aggregate-check arithmetic/prose changed; Pair Reasoning (5%), kickoff (5%), AI Fluency (5%), the two Professional Minds strands (5% each), career artifact sequence (5%), attendance (5%), technical presentation (3%), course evaluation (2%), weekly Odyssey gate (30%), Odyssey checkpoints (15%), and final reflection (5%) rows are byte-for-byte unchanged.
- **No technical artifact graded twice:** confirmed — the new assignment contract explicitly forbids duplicate submission of the technical artifact and the grading-model row's Odyssey/technical categories are untouched.
- **No new recurring category invented:** confirmed — the table now has one fewer named category (17 → merged into 16... concretely, the recurring-category count in the aggregate-check prose dropped from 9 to 8), not an added one.
- **Unresolved total-percentage seam:** **YES, explicitly flagged.** Removing the separate 5% Friday-feedback bucket without reopening the rest of the grading model leaves the table's direct sum at **95%**, not 100%. `docs/grading-model.md` now carries an explicit "Prompt 312 arithmetic seam (unresolved, reported rather than invented)" callout stating this in place of a silently-rebalanced 100% total, and states that Prompt 312 does not decide where the freed 5 points go. This is returned to Jeremy + ChatGPT per the prompt's explicit instruction not to invent a destination for those points.

## 11. Validation commands/results

```
$ git diff --check
(no output — clean)

$ git diff --cached --name-only
assignments/show-and-tell-artifact.md
docs/grading-model.md
planning/fall-2026-weekly-architecture.md

$ grep -rn -i "friday feedback\|A7 equivalent\|A7-equivalent" docs/ planning/ assignments/
docs/grading-model.md:75:A4-equivalent category (now also covering the retired A7-equivalent
```
(the only remaining hit is the reconciliation note itself, not a live separate category)

Full-diff inspection performed by hand; every changed hunk belongs to the Show & Tell contract, the explicit fold/removal of the separate Friday-feedback grading category, or a direct cross-reference consequence (the weekly-architecture chassis table and the arithmetic-seam callout). No unrelated content was touched.

## 12. Unresolved seams returned to Jeremy + ChatGPT

1. **Grading-arithmetic seam (primary):** with the separate A7/Friday-feedback 5% category folded into Show & Tell, `docs/grading-model.md`'s direct table sum is now 95%, not 100%. Prompt 312 explicitly does not decide the destination of the freed 5 points (redistribute, genuinely shrink the total and rebalance elsewhere, or something else) — that is a distinct grading-model decision for Jeremy + ChatGPT.
2. **Minor, out-of-scope observation (not touched):** `planning/fall-2026-weekly-architecture.md`'s "Reasoning Odyssey continuity and grading map" section (its own file, lines below the edited table) still references a "recurring weekly course work (concept-checks/labs/activities)" category under a "Question 004" framing that does not match any category name currently in `docs/grading-model.md`. This predates Prompt 312, is not caused by this fold, and was left alone to avoid overreaching into unrelated stale-seam cleanup (that class of issue is Prompt 310's territory). Flagging it here only for visibility.

## 13. Final commit SHA / working-tree state

Working tree staged and ready to commit on branch `worker/prompt312-show-and-tell` (branched from `main` at `2ec8ea82b822a96d6bec987bb0306e51ce51376c`). Final commit SHA recorded after commit+push: see branch `worker/prompt312-show-and-tell` at origin.
