# Prompt 311 — Pair Reasoning contract

## 1. Starting commit

`2ec8ea82b822a96d6bec987bb0306e51ce51376c` (branch `main`, also `origin/main`).

## 2. Prompt 304 dependency status

Prompt 304 (Pair Reasoning name reconciliation) is **ACCEPTED and merged to main**. Its report, `sidecar/reports/304_pair_reasoning_name_reconciliation.md`, was read in full and consumed rather than re-derived:

- The recurring activity is already named **Pair Reasoning** everywhere in current source (`assignments/pair-reasoning-report.md`, `docs/grading-model.md`, `planning/fall-2026-weekly-architecture.md`, `planning/fall-2026-topic-map.md`).
- Prompt 304 explicitly left the template's **driver/navigator role language and CS2-style content intact**, noting only the name changed. This prompt (311) is the one responsible for replacing that leftover CS2 machinery with the semantic six-field contract — Prompt 304 flagged it, did not fix it.
- No naming archaeology (search for "pair programming" / "paired-programming") was redone; Prompt 311 only re-ran the same searches as a residual check (see §9).

## 3. Files inspected

- `sidecar/prompts/311_define_pair_reasoning_contract.md` (this work order)
- `sidecar/reports/304_pair_reasoning_name_reconciliation.md`
- `assignments/pair-reasoning-report.md` (the pre-existing, CS2-flavored template — the target of this prompt)
- `docs/grading-model.md`
- `planning/fall-2026-weekly-architecture.md`
- `planning/fall-2026-topic-map.md`
- `docs/career-connection.md` (one incidental cross-reference to "a Pair Reasoning artifact" as example evidence)
- `docs/philosophy/teaching-patterns.md`, `docs/curriculum/course-sequence.md`, `docs/reports/curriculum-history-synthesis.md` (historical, PRESERVE-HISTORICAL per Prompt 304 — re-confirmed unchanged, not edited)
- `assignments/show-and-tell-artifact.md` (read only, for template-format consistency; not owned by this prompt)
- `planning/fall-2026-spine.md`, `planning/fall-2026-course-design.md` (read only, to trace the "Question 004" grading-category cross-reference described in §10)

## 4. Files changed

Only one file was changed:

- `assignments/pair-reasoning-report.md` — fully rewritten from a 5-line CS2-flavored stub (names + driver/navigator roles + build log + 3 bullets) into the canonical Pair Reasoning contract: before/during/after structure, the six semantic report fields, explicit non-duplication language, explicit "no required driver/navigator role," explicit "works without programming," and a compact 4-row rubric.

No other file required a change. `docs/grading-model.md`, `planning/fall-2026-weekly-architecture.md`, and `planning/fall-2026-topic-map.md` were inspected and found already consistent with the contract (5% weight, individual report, "Pair Reasoning" naming, no driver/navigator references) — see §8.

## 5. Final canonical Pair Reasoning contract summary

`assignments/pair-reasoning-report.md` now defines:

- **What it is:** exposing a student's reasoning to another human reasoner and recording what happened under challenge; the week's technical artifact (proof/model/code/simulation/checker/graph/truth table/derivation/counterexample) is separate, normal technical/Reasoning Odyssey evidence.
- **Before:** a compact individual starting position (claim/approach/prediction, why, optional assumption/confidence note).
- **During:** comparing reasoning (assumptions, definitions, strongest part of partner's case, challenges, discriminating evidence, AI-vs-verified-evidence distinction); disagreement not required — agreement triggers "test whether the agreement deserves confidence."
- **After:** one individual report per student covering the six semantic fields verbatim from the prompt (starting position, strongest challenge, evidence that mattered, what changed or survived, current position, what would change my mind next).
- **Programming:** explicitly optional; the same contract is stated to work for proofs, counterexamples, set/function/relation models, counting arguments, probability/simulation, graphs/trees, Boolean/SAT, finite-state models, and source/evidence analysis.
- **Individual accountability:** stated directly — the report must be un-swappable between partners.
- **Rubric:** 4 compact dimensions (authentic engagement, evidence over assertion, visible revision/preservation, individual accountability), explicitly not a 6-row bureaucratic breakdown of the six semantic fields, and explicitly not rewarding disagreement for its own sake.
- **Closing "what this is not" section:** not a resubmission of the technical artifact, not a shared artifact, not a driver/navigator log, not required to involve programming.

## 6. How the technical artifact and individual report are kept distinct

- The template's opening section states plainly that the week's technical artifact is produced and submitted through the week's own technical channel, and that "this report is not a second copy of that artifact."
- Field 3 of the report ("Evidence that mattered") explicitly asks what *bore on* the disagreement/confidence — i.e., how the artifact was *used* in reasoning, not a restatement of the artifact itself.
- The closing "What this report is not" section repeats the non-duplication boundary in plain terms and enumerates the artifact types it is not a resubmission of.
- `docs/grading-model.md` (unchanged) already grades the Pair Reasoning report as its own object ("Individual text-entry/upload report with rubric") separate from the 30% Weekly reinforcement/Reasoning Odyssey gate category, which is where the week's technical artifact is graded. No wording in the grading model conflates the two.

## 7. Three scenario walkthroughs

**1. Disagreement (e.g., Week 3 proof/counterexample).** Partner A claims an argument is valid; Partner B disputes a step. Report evidence: A's starting claim, B's specific objection (the challenged step), the proof check or counterexample that actually resolved it, what A revised (e.g., added a missing case) or what A successfully defended, A's now-current position, and what would still change A's mind (e.g., a case not yet checked). No code is required — the discriminating evidence is a proof step or counterexample, not a program.

**2. Agreement (e.g., Week 13 Boolean/SAT).** Both partners arrive at the same simplified expression. The contract routes this into "test whether the agreement deserves confidence": partners must find discriminating evidence anyway — e.g., checking an assignment neither had tried, or confirming the simplification against a truth table. Each student's report records the same starting position, the specific check attempted as the "strongest challenge" they posed to their own agreement, the evidence that check produced, whether the position survived or was refined, and what remaining case would still move it. This produces individual evidence even though there was no disagreement, and it is not merely "we agreed" — it forces an active confidence test.

**3. Non-programming week (e.g., Week 11 graph/network reasoning).** The technical task is a graph model and traversal; a checker or path-checker may exist, but the report itself needs no code. One partner's edge-meaning assumption differs from the other's; the strongest challenge is "your edge means X, but the source data means Y," resolved by re-checking the model against its source rather than by running code. All six fields fill naturally without any code, commit, or shared repository — consistent with §4's "Programming is optional, reasoning is required" requirement.

**Anti-duplication answer (required by the prompt):** *What evidence would disappear if the Pair Reasoning report were removed?* The evidence that would disappear is the record of each individual student's reasoning changing, narrowing, strengthening, or surviving contact with another human's challenge — the starting position, the specific challenge received, what evidence resolved it, and the resulting revision or confirmed confidence. The week's technical artifact would still exist and still be graded elsewhere; only the individual reasoning-under-challenge trail is unique to this report. This is not "the technical work" — the test in §B of the verification battery passes.

## 8. Grade-boundary audit

Inspected `docs/grading-model.md` in full (no edits made):

- Pair Reasoning report (A3 equivalent) remains listed at **5%**, unchanged (line 16).
- The aggregate-check arithmetic (`5+5+5+5+5+5+5+5+5+3+2+30+15+5 = 100%`, lines 28–47) is untouched and still sums to 100%.
- No other category weight was touched; no category was added, removed, or renamed.
- No shared artifact is newly double-counted: the report's own non-duplication language (§6 above) and the pre-existing grading-model separation between the Pair Reasoning report (5%) and the Weekly reinforcement/Reasoning Odyssey gate (30%, where the technical artifact lands) are unchanged and remain the enforcement mechanism.
- `planning/fall-2026-weekly-architecture.md` and `planning/fall-2026-topic-map.md` were checked for stray weight/category claims; none exist — both only describe activity mechanics and artifact examples, not grading arithmetic, and neither needed edits.

## 9. Validation commands/results

```
git diff --check
```
Exit 0, no whitespace/conflict-marker errors.

```
git diff --name-only
```
`assignments/pair-reasoning-report.md` (only file changed).

```
git status --short
```
` M assignments/pair-reasoning-report.md` (only entry; the repo's other worktrees/branches were untouched).

```
rg -n -i 'driver|navigator' docs planning assignments course_metadata.yaml
```
Two hits, both inside the new `assignments/pair-reasoning-report.md`, both stating driver/navigator is *not* required — no live requirement remains anywhere in current-source doctrine.

```
rg -n -i 'pair programming|paired-programming|paired programming' docs planning assignments course_metadata.yaml
```
Three hits: `docs/reports/curriculum-history-synthesis.md`, `docs/philosophy/teaching-patterns.md`, `docs/curriculum/course-sequence.md` — all three are the same PRESERVE-HISTORICAL documents Prompt 304 already classified as historical evidence, not current doctrine; plus one intentional mention inside the new template's own "Historical basis" line, which narrates the rename. No unexplained current-source hit.

```
rg -n -i 'pair reasoning|A3' docs/grading-model.md planning/fall-2026-weekly-architecture.md planning/fall-2026-topic-map.md
```
Confirms "Pair Reasoning" naming and the 5% A3-equivalent category line are present and unchanged.

## 10. Unresolved seams returned to Jeremy + ChatGPT

- `planning/fall-2026-weekly-architecture.md` lines 60–69 still describe a "Question 004"-era grading-category mapping that names a **"recurring weekly course work (concept-checks/labs/activities)"** category. That category name does not exist in the current `docs/grading-model.md` table (which instead has the explicit A3/A4/A7/etc. line items landed by Prompts 302/304). This paragraph appears to predate the finalized grading-model table and was left unedited here because touching it risks deciding grading arithmetic/category structure, which Prompt 311's hard stops explicitly forbid ("do not rebalance other categories," "do not decide the final overall grading arithmetic"). It does not create a duplication risk for Pair Reasoning specifically (it still routes the pair artifact to a category other than the individual report), but the stale category name itself should be reconciled — this looks like exactly the kind of item Prompt 310 (stale-source-seam inventory) is scoped to catch. Flagging it here rather than editing it.
- No other seam was found that Prompt 311 is authorized to fix but left unfixed.

## 11. Final commit SHA / working-tree state

Working tree was clean before the change (only the pre-existing, unrelated untracked file `prompts/305_week2_assessment_contract_reconciliation.md` was present in the main worktree and was never touched by this work, done in a separate worktree). After writing this report, the single change (`assignments/pair-reasoning-report.md`) plus this report file were committed on branch `worker/prompt311-pair-reasoning` and pushed to origin. See the accompanying task summary for the final commit SHA.
