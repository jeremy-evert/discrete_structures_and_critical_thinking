# Prompt 304 — DSCT grading model

## Deliverable

Created `docs/grading-model.md` with an explicit named-category table modeled
on the CS2 source-model table. The model uses DSCT's Tuesday/Thursday chassis,
including the alternating Thursday Pair Programming / Show & Tell rotation.
It does not create a five-day cadence or a separate large synthesis-project
bucket.

## Full table

| Category | Weight | Canvas/Savnac object shape | Graded weeks / cadence |
|---|---:|---|---|
| Reasoning Odyssey technical write-up | 30% | Weekly individual text-entry/upload assignment with a rubric; the week's readable problem-solving artifact | Weeks 2–16 active cycle; Week 9 Tuesday-only, Week 15 asynchronous, Week 16 synthesis object |
| Reasoning Odyssey check, revision, and evidence receipt | 15% | Individual linked evidence/revision receipt with rubric for check, critique response, and carry-forward evidence | Weeks 2–16 when active; Thursday normally, Tuesday-only Week 9, asynchronous Week 15 |
| Tuesday AI Fluency failure-mode check | 5% | Short quiz, text-entry, or exit-ticket object with rubric | Weekly Tuesday Weeks 2–14; Week 15 async and Week 16 adapted where scheduled |
| Tuesday Professional Minds Wednesday-strand response | 5% | Individual reflection/text-entry object tied to shared Professional Minds source | Weekly Tuesday Weeks 2–14; Week 15 async |
| Thursday Professional Minds Friday-strand / career-artifact response | 5% | Individual reflection or career-artifact-sequence submission with rubric | Weekly Thursday Weeks 2–14 when Thursday meets; Week 15 async |
| Pair Programming report | 15% | Individual pair-programming-report upload/text-entry with roles, evidence, win, stuck point, next step, and reflection | Weeks 3, 5, 7, 9, 11, 13; Week 9 is Tuesday pair-style work |
| Show & Tell artifact and revision | 15% | Individual show-and-tell-artifact upload/link with explanation, peer-question evidence, critique, and revision rubric | Weeks 4, 6, 8, 10, 12, 14; never same week as Pair Programming |
| Week 16 Farkle + Machine Learning synthesis | 5% | Shared applied-experience evidence submission with individual reasoning/evidence receipt and rubric | Week 16 only |
| Week 17 individual final reflection | 5% | Low-stress individual text-entry/upload reflection with prompt choice and rubric; not an exam or Reasoning Defense | Week 17 only |
| **Total** | **100%** | | |

## Arithmetic check

The complete table sums to:

`30 + 15 + 5 + 5 + 5 + 15 + 15 + 5 + 5 = 100%`.

The named Reasoning Odyssey family is exactly:

`30% technical write-up + 15% check/revision/evidence receipt = 45%`.

The recurring non-Odyssey rows are:

`5% AI Fluency + 5% Tuesday Professional Minds + 5% Thursday Professional Minds/career artifact + 15% Pair Programming + 15% Show & Tell + 5% Week 16 synthesis = 50%`.

The final is:

`5% Week 17 individual reflection`.

Therefore:

`45% + 50% + 5% = 100%`.

There is no rounding issue: all rows use whole percentages and the Odyssey
family is exactly 45%, not an approximation.

## Chassis trace

| Chassis touchpoint | Table category or categories | Reason it maps |
|---|---|---|
| Tuesday AI Fluency (~8 min) | Tuesday AI Fluency failure-mode check (5%) | The contract names this as a durable Tuesday slot; the object captures the week's convincing-wrong-answer lens and check. |
| Tuesday Professional Minds Wednesday strand (~12 min) | Tuesday Professional Minds response (5%) | This is the contract's named Tuesday Professional Minds strand. |
| Tuesday technical lecture/demo (~47 min) | Reasoning Odyssey technical write-up (30%) | The write-up is the readable artifact of applying the week's technical concept in the persistent context. |
| Tuesday reasoning challenge/check (~8 min) | Reasoning Odyssey technical write-up (30%) and check/revision/evidence receipt (15%) | The challenge supplies the work; the check supplies evidence that the reasoning was tested and understood. |
| Thursday Professional Minds Friday strand (~10–12 min) | Thursday Professional Minds Friday-strand / career-artifact response (5%) | The response is the named receipt for this Thursday strand and can use the existing career-artifact-sequence template where that strand calls for career evidence. |
| Thursday Pair Programming (~50–55 min), alternating weeks | Pair Programming report (15%) | Directly uses the existing pair-programming-report artifact and the frozen rotation. |
| Thursday Show & Tell (~50–55 min), alternating weeks | Show & Tell artifact and revision (15%) | Directly uses the existing show-and-tell-artifact template; peer questions and revision are part of the object. |
| Thursday critique/revision/evidence receipt (~8–10 min) | Reasoning Odyssey check, revision, and evidence receipt (15%) | This is the receipt/carry-forward portion of the Odyssey family, not an extra weekly cadence. |
| Week 16 Farkle + ML synthesis | Week 16 Farkle + ML synthesis (5%) | Question 004 explicitly places it inside recurring work, so it is a named recurring row within the 50%. |
| Week 17 final reflection | Week 17 individual final reflection (5%) | Question 004 explicitly defines a low-stress individual reflection, not a comprehensive exam or defense. |

The Tuesday and Thursday categories are stated as weekly touchpoints, not as a
claim that both Thursday artifact types occur in one week. The Prompt 302
rotation is Pair Programming in Weeks 3, 5, 7, 11, 13 and Show & Tell in Weeks
4, 6, 8, 10, 12, 14, with Week 9's Tuesday pair-style exception and Thursday
Fall Break.

## Underspecified items and known inconsistency

No grading category was left unnameable: the frozen contract gives enough
information to name each category and its object shape. The exact
Professional Minds Wednesday/Friday source anchors remain `SOURCE_PENDING` in
the contract, so this model names their response objects and cadence without
inventing lesson-specific prompts.

The existing `assignments/programming-exam.md` stub is intentionally not used
as a category. It is inconsistent with Question 004's explicit “not a
comprehensive exam” decision and should remain a separate known issue for a
future pass.

## Validation

- No test suite applies to this planning-markdown-only repository.
- `git diff --check`: PASS.
- `make task-check`: unavailable; `/bin/bash: line 1: make: command not found`.
- `make check`: unavailable; `/bin/bash: line 1: make: command not found`.
- Push attempt: blocked; `origin` uses SSH and the environment has no `ssh`
  executable (`error: cannot run ssh: No such file or directory`).
