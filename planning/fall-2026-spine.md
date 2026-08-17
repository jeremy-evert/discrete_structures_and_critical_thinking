# DSCT Fall 2026 — authoritative 17-week semester spine

**Status:** `CONTRACTED_NOT_AUTHORED` unless marked otherwise. This is the
dated Tuesday/Thursday source contract for COMSC-2043-1420 (12:30–1:45 PM,
Gen. Thomas P. Stafford Center, Room 259). It supersedes the prior
one-old-lesson-per-week Weeks 2–15 allocation.

**Frozen 2026-08-17 (Jeremy, executed by Cleo/Lead Foreman):** resolves
Decision cluster E (`sidecar/raw/2026-08-17_dsct_design_decision_pile.md`).
Week 3 is a runway week (Prompts 307/316), not a formal topic week, which
drops the formal core to eleven slots, Weeks 4–14, against twelve candidate
topic bundles. See "The Week 14 merge" below for the resolution and its
justification.

| Week | Tuesday | Thursday | Semester identity | Status |
|---:|---|---|---|---|
| 1 | Aug 18 | Aug 20 | Semester Kickoff Week / Reasoning Odyssey; landed Week 1 package | `LANDED` |
| 2 | Aug 25 | Aug 27 | Building Your AI Lab | `CONTRACTED_NOT_AUTHORED` |
| 3 | Sep 1 | Sep 3 | Containers + minimum-useful LaTeX (runway, not a formal topic week) | `CONTAINER_TOOLCHAIN_AUTHORED` |
| 4 | Sep 8 | Sep 10 | Logic, Claims & Proof | `CONTRACTED_NOT_AUTHORED` |
| 5 | Sep 15 | Sep 17 | Sets, Functions & Sequences as Representations | `CONTRACTED_NOT_AUTHORED` |
| 6 | Sep 22 | Sep 24 | Algorithms, Correctness & Growth | `CONTRACTED_NOT_AUTHORED` |
| 7 | Sep 29 | Oct 1 | Integer Properties & Cryptography — **Odyssey Checkpoint 1** | `CONTRACTED_NOT_AUTHORED` |
| 8 | Oct 6 | Oct 8 | Induction, Recursion & Recurrences | `CONTRACTED_NOT_AUTHORED` |
| 9 | Oct 13 | Oct 15 — Fall Break, no class | Counting & Combinatorial Reasoning (Tuesday only) | `CONTRACTED_NOT_AUTHORED` |
| 10 | Oct 20 | Oct 22 | Probability, Uncertainty & Evidence | `CONTRACTED_NOT_AUTHORED` |
| 11 | Oct 27 | Oct 29 | Relations, Equivalence, Partial Orders, Matrices & Digraphs — **Odyssey Checkpoint 2** | `CONTRACTED_NOT_AUTHORED` |
| 12 | Nov 3 | Nov 5 | Graphs & Network Reasoning | `CONTRACTED_NOT_AUTHORED` |
| 13 | Nov 10 | Nov 12 | Trees, Search & Decision Structures | `CONTRACTED_NOT_AUTHORED` |
| 14 | Nov 17 | Nov 19 | Boolean Algebra, Circuits & Finite-State Machines: Model Limits — **Odyssey Checkpoint 3**, Show & Tell mini-capstone | `CONTRACTED_NOT_AUTHORED` |
| 15 | Nov 24 | Nov 26 — Thanksgiving, no normal class | Thanksgiving / Mexico asynchronous-travel buffer; no new formal DSCT topic | `ASYNC_RESERVED` |
| 16 | Dec 1 | Dec 3 | Farkle + Machine Learning synthesis experience | `VALIDATED` |
| 17 | Dec 8 | Dec 10 | Final Reflection write-up during finals week (Dec 7–11) | `CONTRACTED_NOT_AUTHORED` |

Week 1 is the landed Prompt 301 package: `reports/301_week1_launch_package.md`,
`planning/week-01-source-map.md`, and `week-01/`. Week 2 names are resolved by
Question 009 and are identities/contracts only in this pass. Week 3 is the
pinned-container/minimum-useful-LaTeX runway (Prompts 307/316); its toolchain
(`week-03/container/`, `week-03/student/container-latex-skill-ladder.md`,
`week-03/instructor/container-latex-instructor-notes.md`) is authored and
live-tested, but it does not carry a formal Tuesday/Thursday chassis run-of-show
the way Week 2 and Weeks 4–14 do. Weeks 4–14 are exactly eleven formal DSCT
topic weeks. Week 15 reserves travel and asynchronous integration without
inventing an assignment or due date. Week 16 is now authored and validated
against the canonical shared Farkle + Machine Learning core; its package
begins at `planning/week-16.md` and `week-16/`, with real validation evidence
retained under `sidecar/runs/`. Week 17 is reflection/write-up only; grading
weight and final format remain open under Question 004.

## The Week 14 merge

Decision cluster E's twelve candidate bundles do not fit eleven slots
without exactly one merge. Jeremy chose Boolean Algebra/Circuits/SAT and
Finite-State Machines/Invariants/Model Limits, evaluated against his own
stated criteria — common Discrete Math structure, Critical Thinking value,
and what he has actually taught before:

- **What he has taught before:** the archived Spring 2026 offering
  (`archive/spring-2026/canvas-71253-snapshot-20260714-195606.json`) taught
  these as the last two topic weeks before the Farkle synthesis week, in
  this exact order — Boolean Algebra (old Week 12), then Finite-State
  Machines (old Week 13). Merging the two adjacent weeks he already taught
  back-to-back preserves the maximum amount of his proven ordering and
  reuses `lessons/12-boolean-algebra.md` and `lessons/13-finite-state-machines.md`
  directly, rather than disturbing the middle of the sequence (e.g. folding
  Cryptography into Integer Properties, or Trees into Graphs, both of which
  he has also taught as standalone weeks).
- **Common in Discrete Math:** Boolean algebra and finite-state machines are
  routinely taught adjacently as the two "formal symbolic systems" topics —
  one static (circuits/expressions), one dynamic (state and transition) —
  and both feed the same catalog requirement family.
- **Critical Thinking value:** both ask the same underlying question at
  different scales — *what can this formal system establish, and what can
  it not?* — which is a stronger capstone lens than either topic alone, and
  matches the existing bundle's own critical-thinking framing ("model
  limits").
- This also keeps the merge at the very end of the sequence, where the week
  is already the Reasoning Odyssey mini-capstone and Show & Tell finale
  (Prompt 315/313), rather than disrupting a mid-semester prerequisite
  chain.

The other candidate merges floated in the design-decision quarry (folding
Trees into Graphs, treating Algorithms/Correctness as a recurring lens
rather than its own week, folding Cryptography into Integer Properties) are
explicitly **not** adopted — Jeremy has taught all of those as standalone
weeks before and none of them were chosen.

## Historical continuity table

Old (Spring 2026 taught, non-Farkle topic weeks) → new Fall 2026 slot:

| Spring 2026 taught order | Fall 2026 Week |
|---|---:|
| Logic and Proofs | 4 |
| Functions and Matrices (functions half) | 5 |
| Algorithms | 6 |
| Cryptography | 7 |
| Recursion | 8 |
| Counting (+ Advanced Counting, merged) | 9 |
| Probability | 10 |
| Relations (+ Matrices representation half) | 11 |
| Graphs | 12 |
| Trees | 13 |
| Boolean Algebra + Finite-State Machines (merged) | 14 |

Every Fall 2026 topic bundle traces to a Spring 2026 taught week; nothing is
newly invented. Two merges consolidate twelve historical topics into eleven
Fall 2026 slots: Counting/Advanced Counting (already implicit in the
existing twelve-bundle candidate list) and Boolean Algebra/Finite-State
Machines (this decision).

The Tuesday/Thursday instructional chassis and the detailed Weeks 4–14 source
map are canonical in `fall-2026-weekly-architecture.md` and
`fall-2026-topic-map.md`. Future unmarked weeks are not student-ready lessons.
