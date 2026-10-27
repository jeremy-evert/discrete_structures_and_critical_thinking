# Thursday 10-29 facilitator page: students repeat the process

**For Jeremy · Pair Reasoning day · 12:30–1:45 PM (75 minutes) · materials: `WORKBOOK`, `GLOSSARY`, `starter/` folder**

Students run Tuesday's process (behaviors → bins and boundaries → a naive match that fails transitivity → witness → fix → symmetry → ties → pieces together → depends-on order) on a **different, parallel problem**: finding repeated songs in a playlist. Same 19 step numbers as Tuesday's ladder. Step N in the workbook ↔ `tdd-step-NN` in the demo; the playlist version is on the tags `student-ref-step-NN` (instructor only).

## 1. What this changes in the existing Thursday plan (read this first)

Nothing below is silent. The existing `week-11/instructor/thursday-run-of-show.md` is **kept in shape and extended**. Four things you should decide on purpose:

| # | Existing contract says | What this workbook does | What to do |
|---|---|---|---|
| 1 | "Do not require code or driver/navigator roles. A paper matrix is inspectable." | Code is the **default**, because you asked for the same process as Tuesday. A **paper path** exists for every step (predict, hand check, digraph), so code is never *required* to earn the evidence. No roles are assigned. | Say aloud: "Code is the plan; paper is allowed." If you want the written contract kept literal, tell students the paper path is equal. **Your call, not mine.** |
| 2 | Table ends at 1:25 although the meeting is 75 minutes (12:30–1:45). | The table below fits **75** minutes. | The 1:12–1:25 "model limit" block shrinks to 3 minutes at the end. |
| 3 | Week 11 README: submit the individual Pair Reasoning report. But `assignments/pair-reasoning-report.md` says the category is **retired** (Decision 029, no points). | The pair's evidence is the Evidence Sheet (C3). The workbook's fields line up with the six report fields (section 5), so the report is easy to write if you still ask for it. | Decide whether the report is still collected. I did not touch either file. |
| 4 | Checkpoint 2 is individual and "do not paste the Pair Reasoning report". | Workbook C1 (summary) and the red/green output are *inputs* to checkpoint items 3 and 4. Nothing is submitted in place of the checkpoint. | Remind students: the checkpoint is still their own writing. |

Individual authorship is preserved: **each student writes their own PREDICT boxes and their own One-Sentence Summary.** Print one workbook per student, or one per pair plus a blank sheet each for predictions.

## 2. Minute by minute (75 minutes)

| Clock | Min | Move | Visible work | Replaces / extends |
|---|---|---|---|---|
| 12:30–12:38 | 0–8 | **Individual starting position, no partner yet.** Show the rule: "same artist and lengths within 5 seconds counts as the same song." Each student writes: *Will this rule always sort songs into clean groups? Yes or no, and why.* | One written sentence each, on paper. | Replaces "state initial classification" (same job, new object). |
| 12:38–12:43 | 8–13 | Pairing norms (compare reasoning, do not divide labor; disagreement is allowed; no roles). Remind them the checkpoint replaces the Decision Gate. | Pairs seated. | Kept; shortened from 8 to 5. |
| 12:43–12:50 | 13–20 | **Set up and the why.** Read A1–A3 aloud (soup, smoke alarm, red is normal). Pairs do A4 (starter folder, pytest check) and paste the A5 rules into Claude. Paper-path pairs skip the install. | `python3 -m pytest -q` prints "no tests ran". | New. This is where the time goes wrong if you let it; keep it to 7. |
| 12:50–1:20 | 20–50 | **Pair build, Steps 1 to 7 (core).** Circulate; use the 60-second check below. Step 6 is the one that matters most: they invent the counterexample before the computer finds it. | Red at Step 6, green at Step 7; counterexample written; digraph drawn. | Replaces "compare representations; seek discriminating witnesses." The digraph and witness are still the artifacts. |
| 1:20–1:30 | 50–60 | **Cross-pair challenge.** Pair A gives Pair B its three Slow Orbit lengths; B checks by hand (gaps 1→2, 2→3, 1→3) and by running them. Then they swap roles: B's numbers to A. Question: *is your partner pair's counterexample really a counterexample?* | Hand check; one agreement or one disagreement, with the numbers. | Kept (it was 13 min). |
| 1:30–1:40 | 60–70 | **Individual write-up.** Each student writes C1 (One-Sentence Summary) alone, finishes the honesty log C2, and starts or revises their checkpoint. Pairs that are ahead continue Steps 8 onward. | One sentence each; the log. | Kept (individual report and checkpoint time). |
| 1:40–1:45 | 70–75 | **Name the model limit and collect.** Ask: *What does our "same song" key get wrong?* (Expected: typos, "Live" versions, different spellings of an artist.) Collect the Evidence Sheet (C3). Preview network modeling if there is time. | Boundary statement said aloud. | Kept, from 13 minutes to 5. |

**If you are behind at 1:20:** skip Step 3 (it is green from the start, the least necessary) and Step 5's explanation; do not skip Step 6 or Step 7. Steps 8 to 19 are homework or a later class. Do not try to finish more than the core.

**Realism note (not measured):** the core of seven steps in 30 minutes is tight for a pair that finds testing hard. I have not timed real students. The dry run (REPORT.md) gives a model-student estimate only. Watch the first pair finishing Step 2; if they take more than 8 minutes, cut Step 3 right away.

## 3. Check a pair in 60 seconds

Walk up, point at the screen, ask these three things. Stop as soon as one fails; fix that.

1. **"Where are your predictions?"** They should have handwriting for the current step *from before* the run. No predictions = they are copying Claude. Ask them to cross out and re-predict the next step.
2. **"Show me red and tell me why it's red."** They point at the line with `E` or the failing test name and say it in their own words. "It failed" is not enough; "it failed because 1 and 3 aren't alike even though both are alike with 2" is.
3. **"What did you change, and did you or Claude choose it?"** They name a number or a sentence that is theirs. At Step 6, the three lengths are theirs, not Claude's.

Quick pass/fail: all three answered = leave them alone for 10 minutes.

## 4. When pairs get stuck

| Symptom | Likely cause | Do this |
|---|---|---|
| `pytest: command not found` | not on PATH | Use `python3 -m pytest -q`. |
| `No module named pytest` | not installed | `python3 -m pip install pytest`. If the network is blocked, switch the pair to the paper path. |
| `No module named playlist` / import error | wrong folder | Run pytest from the `playlist-lab` folder, not from `tests`. |
| Claude writes the whole program at once | the A5 rules were not pasted | Paste the rules again; "do ONLY this step." Delete the extra files. |
| Claude "fixes" the test instead of the code | rule 3 | Say: never change a test to make it pass. Restore the test. |
| Step 1 is already green | the stub is not a stub | Ask Claude to make `length_label` return `None` only. |
| Tests are red and nobody can read the wall of text | too much output | Read only the last line and the line starting with `E`. |
| **Cannot invent the counterexample (Step 6)** | thinks in single pairs | Ask: *"What is the largest gap that counts as alike? Now put listing 2 in the middle and listing 1 on one side and listing 3 on the other. How far apart are 1 and 3?"* Do not give numbers. |
| All Step 6 tests pass | their gap 1→3 is not over 5 | "Add up the two small gaps: is it more than 5?" |
| Step 7: key looks wrong | the regex changed things | Ask Claude to print `song_key` for the three tracks and compare to their prediction. |
| One partner is doing all the typing | normal | Ask the quiet one to read their PREDICT aloud before each run. |
| A laptop fails | environment | Move to the paper path: PREDICT, hand check the gaps, draw the digraph, write the summary. Same evidence. |

Principle for you: **never type for them.** Ask a question that makes the next move visible.

## 5. What the pair submits, and how it maps

**Pair submits one page:** the Evidence Sheet (workbook C3): last step finished, pasted red-at-Step-6 and green-at-Step-7 output (photo or text), their counterexample in words, one wrong prediction and why, one thing they would change.
**Each student keeps their own:** PREDICT boxes, the honesty log (C2), the One-Sentence Summary (C1).

Mapping to the six fields of the existing Pair Reasoning report, so no new form is needed:

| Pair Reasoning report field | Where it appears in the workbook |
|---|---|
| 1 Starting position | The 12:30 written sentence (before pairing) |
| 2 Strongest challenge | The cross-pair challenge at 1:20 (their numbers checked by another pair) |
| 3 Evidence that mattered | Red at Step 6, green at Step 7, the hand-checked gaps and the digraph |
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
