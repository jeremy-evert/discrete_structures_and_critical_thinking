# Prompt 302 — Semester Spine & Weekly Architecture Contract

Run date: 2026-08-14. This is a source-contract and reconciliation pass, not
lesson authoring.

## 1. Executive contract verdict

| Contract | Verdict |
|---|---|
| SEMESTER ARC COHERENCE | GO |
| WEEKLY ARCHITECTURE CONTRACT | GO |
| WEEKS 3-14 TOPIC COVERAGE | GO |
| CATALOG COVERAGE | GO |
| PROFESSIONAL MINDS SLOT CONTRACT | GO WITH YELLOWS |
| ZYBOOKS SOURCE MAPPING | GO WITH YELLOWS |
| HANDOFF TO WEEK 2 AUTHORING | GO WITH YELLOWS |

The yellows are honest source availability seams: no local Professional Minds
checkout was present, and the existing ZyBooks CSV has malformed unquoted
commas in some section-title rows. Neither changes the frozen structural
contract. No Week 2 or Weeks 3–14 lesson was authored.

## 2. Authority and reconciliation summary

Current direct authority is Question 009: Week 1 kickoff; Week 2 Tuesday
Building Your AI Lab; Week 2 Thursday Containers and Repeatability; formal
DSCT Weeks 3–14; Week 15 travel buffer; Week 16 Farkle + ML; Week 17 Final
Reflection. Prompt 301's landed Week 1 package is preserved and referenced.
The catalog metadata remains the hard coverage constraint. Professional Minds'
known architecture is adapted to T/Th. Existing ZyBooks classifications remain
source facts. Old lessons and 300B–300E reports were used as historical
evidence, not as overriding authority.

The stale one-old-lesson-per-week Weeks 2–15 spine is superseded. Historical
lesson skeletons remain tracked and their new roles are explicit.

## 3. Final 17-week semester table

The complete dated table is canonical in `planning/fall-2026-spine.md`.

| Weeks | Contract |
|---|---|
| 1 | Aug 18/20 — landed Semester Kickoff Week |
| 2 | Aug 25/27 — Building Your AI Lab / Containers and Repeatability |
| 3–14 | Sep 1–Nov 19 — the twelve frozen formal topics in the topic map |
| 9 exception | Oct 15 Thursday Fall Break; Tuesday-only pair-style work |
| 15 | Nov 24/26 — Thanksgiving/Mexico asynchronous-travel buffer |
| 16 | Dec 1/3 — Farkle + Machine Learning synthesis |
| 17 | Dec 8/10 in finals week — Final Reflection write-up |

Future weeks are `CONTRACTED_NOT_AUTHORED`, not student-ready claims.

## 4. Tuesday weekly chassis

Professional Minds AI Fluency ~8 min; Professional Minds Wednesday strand ~12
min; technical lecture/demo ~47 min; reasoning challenge/check/exit ~8 min.
Total: 75 minutes. The AI lens is “What would a convincing wrong answer look
like this week?” and uses Sources → Rules/Assumptions → Work → Check →
One-Sentence Summary.

## 5. Thursday weekly chassis

Professional Minds Friday strand ~10–12 min; Pair Programming or Show & Tell
~50–55 min; critique/revision/evidence receipt/exit ~8–10 min. Total: 75
minutes. Pair artifacts may be executable or modeling/checking artifacts.
Show & Tell requires explanation, defense, critique, revision, and visible
evidence.

## 6. Weeks 3–14 technical topic map

| Week | Core | Question | Thursday |
|---:|---|---|---|
| 3 | Logic, Claims & Proof | Does a true conclusion mean the argument was valid? | Pair Programming |
| 4 | Sets, Functions & Sequences as Representations | What did the representation assume, omit, or blur? | Show & Tell |
| 5 | Algorithms, Correctness & Growth | “It worked on my examples” proves what? | Pair Programming |
| 6 | Integer Properties & Cryptography | What assumptions make a security claim true? | Show & Tell |
| 7 | Induction, Recursion & Recurrences | Where is the logical bridge? | Pair Programming |
| 8 | Counting & Combinatorial Reasoning | Are cases exhaustive, exclusive, and counted once? | Show & Tell |
| 9 | Probability, Uncertainty & Evidence | How do assumptions and simulation fool us? | Tuesday pair-style; Thursday Fall Break |
| 10 | Relations, Equivalence, Partial Orders, Matrices & Digraphs | What properties does the classification satisfy? | Show & Tell |
| 11 | Graphs & Network Reasoning | Correct graph solution or wrong model? | Pair Programming |
| 12 | Trees, Search & Decision Structures | What disappears in a hierarchy? | Show & Tell |
| 13 | Boolean Algebra, Circuits & SAT | Is the transformation equivalent under every assignment? | Pair Programming |
| 14 | Finite-State Machines, Invariants & Model Limits | What states/transitions or limits were forgotten? | Show & Tell / mini-capstone |

The full primary-concept, failure-mode, source-lesson, catalog, ZyBooks, and
dependency table is `planning/fall-2026-topic-map.md`.

## 7. Catalog coverage matrix

Sets W4; functions W4; propositional and predicate logic W3; Boolean algebra
W13; graph theory W11; matrices W10; proof techniques W3/W7; combinatorics W8;
finite state machines W14. Result: all nine official catalog topics covered.

## 8. AI Fluency failure-mode map

W3 invalid-but-fluent proof; W4 silent domain/codomain or lost distinction; W5
edge-case failure and missing correctness argument; W6 attacker/number-theory
assumption hidden; W7 missing base case/circular leap; W8 double counting or
incomplete cases; W9 false independence/base-rate neglect/gambler's fallacy or
simulation overclaim; W10 failed equivalence/order property; W11 wrong graph
model; W12 unjustified hierarchy; W13 non-equivalent simplification or SAT
confusion; W14 omitted state/transition or ignored model limit.

## 9. Thursday rotation and artifact map

Frozen rotation: Pair Programming W3, W5, W7, W11, W13; Show & Tell W4, W6,
W8, W10, W12; W14 Show & Tell / mini-capstone. W9 is the Fall Break exception
with pair-style work folded into Tuesday. Artifact families are recorded in
`runs/2026-08-14_prompt302_semester_spine_weekly_architecture/derived/thursday_rotation.csv`.

## 10. Professional Minds source-slot status

The architecture has three durable slots: Tuesday AI Fluency, Tuesday
Wednesday-source strand, and Thursday Friday-source strand. The architecture
is canonical; all per-week Wednesday/Friday lesson anchors are
`SOURCE_PENDING` because no local `professional_minds` checkout was present.
No Professional Minds files were modified or fabricated.

## 11. Old lesson-file reconciliation

Orientation becomes Week 1/2 habit source. Logic/proof/sequences split across
W3/W4/W7. Functions/matrices split across W4/W10. Algorithms, cryptography,
recursion, counting, probability, relations, graphs, trees, Boolean algebra,
and finite-state machines map respectively to W5–W14 as specified. Synthesis/
applications supports W14 and W16 rather than becoming another formal topic.
No skeleton was deleted. See `derived/lesson_reconciliation.csv`.

## 12. ZyBooks remap result

The proposed semantic remap moves Sets from the old W3 target to W4, moves
Finite State Machines from the old W5 target to W14, and renames the remaining
families to the frozen topic titles. KEEP, OPTIONAL, and UNUSED are preserved;
no live ZyBooks page, configuration, or due date was accessed or changed.

The canonical CSV remains unchanged because several section-title fields
contain unquoted commas, making a safe row-preserving rewrite impossible from
the current schema. The complete family-level proposal is
`runs/2026-08-14_prompt302_semester_spine_weekly_architecture/derived/zybooks_remap_diff.csv`.

## 13. Deterministic validation results

PASS: exactly 17 weeks; landed Week 1 reference; exact Week 2 identities;
exactly 12 formal Weeks 3–14; all catalog topics; Week 9 no Thursday; Week 15
async reserved; Week 16 Farkle + ML; Week 17 reflection; frozen Thursday
rotation; no stale one-lesson operational spine; no formal topic in Weeks 1/2;
no points, weights, or unauthorized due dates; referenced source paths exist;
Week 16 prerequisites precede it; both chassis fit 75 minutes. YELLOW: KEEP
ZyBooks rows are coherently proposed by section family but not rewritten in the
malformed canonical CSV. Machine-readable results are in `derived/validation.json`.

## 14. Unresolved yellows and open policy questions

Per-week Professional Minds source anchors remain pending. ZyBooks canonical
row remap remains pending schema-safe normalization or source confirmation.
Questions 004–008 remain open: grading/final format, project/tooling,
non-code path, career-strand assessment, and due-date cadence. Prompt 302 does
not answer them. Week 17 therefore records role only, not a rubric or weight.

## 15. Files changed

Created/updated in DSCT: `planning/fall-2026-spine.md`,
`planning/fall-2026-weekly-architecture.md`,
`planning/fall-2026-topic-map.md`, the supersession note in
`planning/fall-2026-course-design.md`, this report, and the complete run
evidence under `runs/2026-08-14_prompt302_semester_spine_weekly_architecture/`.
The canonical ZyBooks CSV was intentionally not changed.

## 16. Exact handoff to Prompt 303 Week 2 authoring

Prompt 303 may author exactly two Week 2 source packages: Tuesday Aug 25
**Building Your AI Lab**, adapted from CS2, and Thursday Aug 27 **Containers
and Repeatability**. It must preserve the landed Week 1 bridge, use this
semester spine and Tuesday/Thursday architecture, and not reopen Question 009.
It must not shift Weeks 3–14, author formal DSCT topics, answer Questions
004–008, or begin downstream Course Foundry, Savnac, Marker/Coach, watcher,
Synthetic Student, or NRP work.

## Final handoff status

DSCT and JTT source SHAs before this pass are recorded in the run receipt.
The DSCT contract is ready for the Prompt 303 Week 2 authoring handoff with
the two documented yellows above.
