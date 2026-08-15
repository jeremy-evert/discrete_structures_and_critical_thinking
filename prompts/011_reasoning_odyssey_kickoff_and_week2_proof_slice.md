# Prompt 011 — DSCT Reasoning Odyssey kickoff + Week-2 proof slice (Prompt 126 slice 3/4, part A)

## Status

READY. This is new construction, not a naming reconciliation (DSCT has zero
existing Odyssey/World-Bible infrastructure, unlike CS1/CS2). Scoped
deliberately small per Prompt 126's own execution rule — prove one week
before fanning to all fifteen.

Governing precedent, must follow exactly:
- `jeremy_task_tracking/questions/answered_questions/003_...` (Reasoning
  Odyssey general doctrine: name, weekly rhythm, no unpaid required work,
  no second gradebook).
- `jeremy_task_tracking/questions/answered_questions/004_dsct_grading_and_final_format.md`
  (DSCT weights: 45% weekly Reasoning Odyssey write-ups, 50% recurring
  weekly course work, 5% low-stress final reflection; weekly categories are
  tied into the Reasoning Odyssey fabric, Week 16 synthesis is recurring
  course work not a giant separate bucket).
- `jeremy_task_tracking/questions/answered_questions/005_dsct_project_and_tooling.md`
  (open medium/tool choice; hard reasoning/evidence contract — inquiry,
  grounding, known/unknown state, bridge, auditable work trail, checking,
  limitations, why a skeptic should believe the conclusion; rubrics judge
  that contract, not conformity to a preferred medium).

**Explicitly still open — do NOT guess these, leave visible TBD markers
instead:**
- `questions/006_dsct_non_code_participation_path.md` — whether/how a
  non-code-dependent equivalent path exists for programming/simulation-
  flavored weeks (this affects Weeks 4–15 per that question's own note; it
  does not block the kickoff or Week 2, which is logic/proofs, not code).
- `questions/007_dsct_career_strand_assessment.md` — whether the career
  strand is assessed or advisory.
- `questions/008_dsct_student_due_date_cadence.md` — actual due dates.

## Real existing DSCT structure (read before writing)

- `planning/fall-2026-spine.md`: 17-week T/Th spine. Week 1 = universal
  cross-course kickoff (no DSCT content). Weeks 2–15 = one lesson each from
  `lessons/01-*.md` through `14-*.md` (14 lessons, 14 weeks — check the
  exact file-to-week mapping in the spine, do not assume lesson N = week N).
  Week 16 = review/integration buffer. Week 17 = finals.
- `assignments/weekly-problem-solving-writeup.md`: existing reusable weekly
  template (Sources / Rules-Assumptions / Work / Check Your Answer /
  One-Sentence Summary) — this is the 50% "recurring weekly course work"
  category per Question 004, and is NOT itself the Reasoning Odyssey.
- No `World Bible` or `Reasoning Odyssey` concept exists anywhere in this
  repo yet. You are building it, grounded in Question 005's doctrine: the
  student picks a persistent, bounded context (world, domain, system,
  organization, or problem space they care enough to revisit) and uses it
  as the through-line for their weekly discrete-structures reasoning. This
  does not need to be fictional — a real system/domain the student is
  interested in modeling logically is equally valid per Question 005.

## Scope — this leaf only

1. Write `assignments/reasoning-odyssey-kickoff.md`: the DSCT Reasoning
   Odyssey kickoff/home-base document. It must:
   - explain what the Reasoning Odyssey is and why it exists in DSCT
     specifically (continuity/ownership across proofs, logic, graphs,
     probability, etc. — not a bolt-on writing assignment);
   - explain the World Bible as the living record of the student's chosen
     world/domain and their reasoning inside it;
   - state plainly that medium/tool choice is open (Question 005) but the
     reasoning/evidence contract (the 8 elements: inquiry, grounding,
     known/unknown state + bridge, auditable trail, checking, limitations,
     why a skeptic should believe it) is not;
   - explain the weekly rhythm: each week's discrete-structures concept
     gets used/reasoned-about inside the student's own World Bible context;
   - note explicitly, in plain student-facing language, that the exact form
     of code/simulation-flavored weeks is still being finalized (do not
     invent a specific accommodation policy — just say plainly this will be
     clarified, citing no internal question numbers to students);
   - state the grading placement per Question 004 (weekly Reasoning Odyssey
     write-ups are 45% of the course, distinct from the 50% recurring
     weekly course-work category) without inventing exact per-week point
     values beyond what's needed for the one worked example in step 2.
2. Build exactly **one** fully worked weekly gate as the proof slice: the
   week mapped to `lessons/02-logic-proofs-and-sequences.md` per the real
   spine. Create `assignments/reasoning_odyssey_gates/week-XX.md` (use the
   real week number from the spine, not an assumption) with guidance, a
   concrete task connecting logic/proofs to the student's World Bible,
   a submission path, and points consistent with Question 004's 45%
   category — show your point-value reasoning in the deliverable rather
   than asserting a number with no basis. Pair it with
   `rubrics/reasoning_odyssey_gates/week-XX_rubric.md` that assesses the
   Question 005 reasoning/evidence contract, not medium conformity.
3. Do **not** build gates for any other week. Do not touch
   `assignments/weekly-problem-solving-writeup.md`'s existing 50% category.
   Do not invent due dates (use "TBD — pending course due-date-cadence
   decision" literally where a date would go). Do not invent a non-code
   accommodation policy. Do not touch any other course repo.

## Do not

- Do not fan this out to all 15 weeks — this is a one-week proof slice.
- Do not invent exact calendar due dates.
- Do not invent a specific non-code-equivalency policy for Weeks 4–15.
- Do not change any existing DSCT grading weights/categories.
- Do not touch any other repo.

## Deliverable

Write `reports/011_reasoning_odyssey_kickoff_and_week2_proof_slice.md` in
this repo: what was built, the point-value reasoning for the one worked
week, every TBD marker left and why, and an explicit note that this is a
one-week proof slice awaiting Foreman/Jeremy review before the remaining 13
weeks are built.
