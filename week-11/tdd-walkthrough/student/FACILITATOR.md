# Thursday 10-29 facilitator page: students repeat the process

**For Jeremy · Pair Reasoning day · 12:30–1:45 PM (75 minutes) · materials: `WORKBOOK`, `GLOSSARY`, `starter/` folder**

Students run Tuesday's process (behaviors → bins and boundaries → a naive match that fails transitivity → witness → fix → symmetry → ties → pieces together → depends-on order) on a **different, parallel problem**: finding repeated songs in a playlist. Same step numbers as Tuesday's prompts (`STEPS.md`, 00 to 14). The playlist reference solution is on the tags `student-ref-step-NN`, which use the same ladder numbering as Anna's `tdd-step-NN` tags (instructor only).

## 1. What this changes in the existing Thursday plan (read this first)

Nothing below is silent. The existing `week-11/instructor/thursday-run-of-show.md` is **kept in shape and extended**. Four things you should decide on purpose:

| # | Existing contract says | What this workbook does | What to do |
|---|---|---|---|
| 1 | "Do not require code or driver/navigator roles. A paper matrix is inspectable." | Code is the **default**, because you asked for the same process as Tuesday. A **paper path** exists for every step (predict, hand check, digraph), so code is never *required* to earn the evidence. No roles are assigned. | Say aloud: "Code is the plan; paper is allowed." If you want the written contract kept literal, tell students the paper path is equal. **Your call, not mine.** |
| 2 | Table ends at 1:25 although the meeting is 75 minutes (12:30–1:45). | The table below fits **75** minutes. | The old 1:12–1:25 "model limit" block becomes a 5-minute block at the end (1:40–1:45), and the other blocks shrink to fit. |
| 3 | Week 11 README: submit the individual Pair Reasoning report. But `assignments/pair-reasoning-report.md` says the category is **retired** (Decision 029, no points). | The pair's evidence is the Evidence Sheet (C3). The workbook's fields line up with the six report fields (section 5), so the report is easy to write if you still ask for it. | Decide whether the report is still collected. I did not touch either file. |
| 4 | Checkpoint 2 is individual and "do not paste the Pair Reasoning report". | Workbook C1 (summary) and the red/green output are *inputs* to checkpoint items 3 and 4. Nothing is submitted in place of the checkpoint. | Remind students: the checkpoint is still their own writing. |

Individual authorship is preserved: **each student writes their own PREDICT boxes and their own One-Sentence Summary.** Print one workbook per student, or one per pair plus a blank sheet each for predictions.

## 2. Minute by minute (75 minutes)

| Clock | Min | Move | Visible work | Replaces / extends |
|---|---|---|---|---|
| 12:30–12:38 | 0–8 | **Individual starting position, no partner yet.** Show the rule: "same artist and lengths within 5 seconds counts as the same song." Each student writes: *Will this rule always sort songs into clean groups? Yes or no, and why.* | One written sentence each, on paper. | Replaces "state initial classification" (same job, new object). |
| 12:38–12:43 | 8–13 | Pairing norms (compare reasoning, do not divide labor; disagreement is allowed; no roles). Remind them the checkpoint replaces the Decision Gate. | Pairs seated. | Kept; shortened from 8 to 5. |
| 12:43–12:50 | 13–20 | **Set up and the why.** Read A1–A3 aloud (soup, smoke alarm, red is normal). Pairs do A4 (starter folder, pytest check) and paste the A5 rules into Claude. Paper-path pairs skip the install. | `python3 -m pytest -q` prints "no tests ran". | New. This is where the time goes wrong if you let it; keep it to 7. |
| 12:50–1:20 | 20–50 | **Pair build, class fast path: Steps 01, 06, 07, 08.** Step 01 on paper (pairs, matrix, digraph; 8 min). Then 06 (a rule that looks right), **07 (they invent the counterexample before the computer finds it: the one that matters most)**, 08 (the repair). Circulate; use the 60-second check below. Steps 02–05 and 09–14 are homework or next class. | Matrix and digraph on paper (Step 01), red at Step 07, green at Step 08; counterexample written. | Replaces "compare representations; seek discriminating witnesses." The matrix, digraph and witness are still the artifacts, now produced by the pair's own relation. |
| 1:20–1:30 | 50–60 | **Cross-pair challenge.** Pair A gives Pair B its three Slow Orbit lengths from Step 07; B checks by hand (gaps 1→2, 2→3, 1→3) and by running them. Then they swap roles: B's numbers to A. Question: *is your partner pair's counterexample really a counterexample?* | Hand check; one agreement or one disagreement, with the numbers. | Kept (it was 13 min). |
| 1:30–1:40 | 60–70 | **Individual write-up.** Each student writes C1 (One-Sentence Summary) alone, finishes the honesty log C2, and starts or revises their checkpoint. Pairs that are ahead continue Steps 8 onward. | One sentence each; the log. | Kept (individual report and checkpoint time). |
| 1:40–1:45 | 70–75 | **Name the model limit and collect.** Ask: *What does our "same song" key get wrong?* (Expected: typos, "Live" versions, different spellings of an artist.) Collect the Evidence Sheet (C3). Preview network modeling if there is time. | Boundary statement said aloud. | Kept, from 13 minutes to 5. |

**If you are behind at 1:20:** drop Step 06b's explanation and do Step 01 as a joint demo on the projector. Do not skip Step 07 or Step 08.

**Realism note (not measured with real students):** a model playing a struggling student, given the first workbook, estimated 100–120 minutes for the original seven-step core, which is why the class path is now only Steps 01, 06, 07, 08 (a model estimate, not a timing). A second model dry run of the fast path alone (Steps 01, 06, 07, 08) estimated about 50 minutes of work, 65–75 with reading, setup and write-up, which is more than the 30-minute build slot. So plan for **Step 08 to be finished together on the projector** if the room is slow, and for pairs to finish Part C at home. If the first pair needs more than 12 minutes for Step 06, tell everyone to paste the Step 06 tests as written and move to Step 07.

## 3. Check a pair in 60 seconds

Walk up, point at the screen, ask these three things. Stop as soon as one fails; fix that.

1. **"Where are your predictions?"** They should have handwriting for the current step *from before* the run. No predictions = they are copying Claude. Ask them to cross out and re-predict the next step.
2. **"Show me red and tell me why it's red."** They point at the line with `E` or the failing test name and say it in their own words. "It failed" is not enough; "it failed because 1 and 3 aren't alike even though both are alike with 2" is.
3. **"What did you change, and did you or Claude choose it?"** They name a number or a sentence that is theirs. At Step 07, the three lengths are theirs, not Claude's.

Quick pass/fail: all three answered = leave them alone for 10 minutes.

## 4. When pairs get stuck

| Symptom | Likely cause | Do this |
|---|---|---|
| `pytest: command not found` | not on PATH | Use `python3 -m pytest -q`. |
| `No module named pytest` | not installed | `python3 -m pip install pytest`. If the network is blocked, switch the pair to the paper path. |
| `No module named playlist` / import error | wrong folder | Run pytest from the `playlist-lab` folder, not from `tests`. |
| Claude writes the whole program at once | the A5 rules were not pasted | Paste the rules again; "do ONLY this step." Delete the extra files. |
| Claude "fixes" the test instead of the code | rule 3 | Say: never change a test to make it pass. Restore the test. |
| Step 04a is already green | the stub is not a stub | Ask Claude to make `length_label` return `None` only. |
| Tests are red and nobody can read the wall of text | too much output | Read only the last line and the line starting with `E`. |
| **Cannot invent the counterexample (Step 07)** | thinks in single pairs | Ask: *"What is the largest gap that counts as alike? Now put listing 2 in the middle and listing 1 on one side and listing 3 on the other. How far apart are 1 and 3?"* Do not give numbers. |
| All Step 07 tests pass | their gap 1→3 is not over 5 | "Add up the two small gaps: is it more than 5?" |
| Step 08: key looks wrong | the regex changed things | Ask Claude to print `song_key` for the three tracks and compare to their prediction. |
| One partner is doing all the typing | normal | Ask the quiet one to read their PREDICT aloud before each run. |
| A laptop fails | environment | Move to the paper path: PREDICT, hand check the gaps, draw the digraph, write the summary. Same evidence. |

Principle for you: **never type for them.** Ask a question that makes the next move visible.

## 5. What the pair submits, and how it maps

**Pair submits one page:** the Evidence Sheet (workbook C3): last step finished, pasted red-at-Step-07 and green-at-Step-08 output (photo or text), their counterexample in words, one wrong prediction and why, one thing they would change.
**Each student keeps their own:** PREDICT boxes, the honesty log (C2), the One-Sentence Summary (C1).

Mapping to the six fields of the existing Pair Reasoning report, so no new form is needed:

| Pair Reasoning report field | Where it appears in the workbook |
|---|---|
| 1 Starting position | The 12:30 written sentence (before pairing) |
| 2 Strongest challenge | The cross-pair challenge at 1:20 (their numbers checked by another pair) |
| 3 Evidence that mattered | Red at Step 07, green at Step 08, the hand-checked gaps, the matrix and the digraph (Step 01 shows how) |
| 4 What changed or survived | Wrong predictions crossed out (not erased); the old counterexample kept as a test |
| 5 Current position | C1, the One-Sentence Summary |
| 6 What would change my mind next | The model-limit question at 1:40 (typos, live versions) |

The contract's rule "when AI materially contributes, distinguish an AI proposal from independently verified evidence" is the honesty log (C2).

## 6. Setup checklist for you (Wednesday)

- [ ] Python 3.9+ and pytest work on **your** machine and on a student-type laptop (`python3 -m pytest -q` on the starter prints "no tests ran").
- [ ] Print: one workbook per student (see `README.md` for the page count) and the glossary (3 pages), plus 3 spare Evidence Sheets.
- [ ] Post `starter/` as a zip (the *only* code students get). **Do not post `instructor-only/`**; it holds the answers.
- [ ] Decide the code-optional question in section 1, row 1.
- [ ] Tuesday: after you demonstrate, tell them Thursday is "your turn, same moves, new problem."

## 7. Where each workbook step sits on Tuesday's ladder

| Workbook step | Tuesday prompt (`STEPS.md`) | Anna's tags (`tdd-step-NN`) | Playlist reference tags (`student-ref-step-NN`) |
|---|---|---|---|
| 00 rules (Part A5) | 00 Session rules | none | none |
| 01 pairs, matrix, arrows | 01 Seating relation | demo | demo `step01` |
| 02 four questions, witnesses | 02 Property checker | demo | demo `step02` |
| 03 classify five relations | 03 Classify relations | demo | demo `step03` |
| 04a / 04b `length_label` bins | 04 letter_grade bins | 01 red, 02 green | 01 red, 02 green |
| 05 same label is an equivalence | 05 Same bin is an equivalence | 03 green | 03 green |
| 06a / 06b `looks_alike` | 06 Fuzzy name match | 04 red, 05 green | 04 red, 05 green |
| 07 transitivity counterexample | 07 Transitivity counterexample | 06 red | 06 red |
| 08 key fix | 08 Canonical key fix | 07 green | 07 green |
| 09a / 09b chains | 09 Group by chains | 08 red, 09 green | 08 red, 09 green |
| 10a / 10b symmetric | 10 Symmetric equals | 10 red, 11 green | 10 red, 11 green |
| 11a / 11b antisymmetric | 11 Antisymmetric sort | 12 red, 13 green | 12 red, 13 green |
| 12a / 12b end to end | 12 merge_duplicates | 14 red, 15 green | 14 red, 15 green |
| 13a / 13b depends-on order | 13 Dependency order | 16 red, 17 green | 16 red, 17 green |
| 14a / 14b cycle | 14 Cycle smell | 18 red, 19 green | 18 red, 19 green |

Instructor-only files (never post): `instructor-only/reference/` (the full solution, one commit per tag), `instructor-only/ladder_check.sh` (runs pytest at every tag in a throwaway clone), `instructor-only/check_demos.sh` (runs the Step 01–03 demos against recorded output).
