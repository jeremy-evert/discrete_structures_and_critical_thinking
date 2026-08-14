# Prompt 300B — Discrete Structures course source-of-truth audit

Audit date: 2026-08-14
Audited repository: `/mnt/nora/git/discrete_structures_and_critical_thinking`
Audited branch/SHA: `main` / `1fa96ee7bc8d45af2cb0d185743759d8d027c088`
300A handoff SHA: `1fa96ee7bc8d45af2cb0d185743759d8d027c088`

The checkout was clean and matched the recorded handoff. `git fetch origin` and
the JTT pull were attempted, but the environment rejected the permissions on
`/etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf`; the audit therefore uses the
freshest safely available checked-out source and does not claim remote freshness.
No DSCT course source was authored or deployed.

## 1. Executive content verdict

Fall 2026 DSCT is presently a strong instructional design blueprint plus a
small set of reusable templates, not a teachable semester course. The source
clearly intends a reasoning-centered bridge from mathematics and programming:
precise claims, proof/counterexample, discrete models, code/simulation, visible
checking, and concise conclusions. The implementation is thin: 14 lesson files
contain only objectives, key content, and historical references; there are no
week-dated student activities, actual problem sets, substantive reflections,
portfolio artifacts, or tests.

Required verdicts:

- **A. Tuesday source readiness: GO WITH YELLOWS.** Shared kickoff guides,
  activities, readings, assignments, and rubrics exist, so Jeremy has a usable
  generic launch structure. The DSCT-specific framing slot is still the CS1
  reference, the shared material is Monday/Wednesday/Friday-shaped while DSCT
  meets Tuesday/Thursday, and AI/accessibility/help/tool instructions are not a
  complete DSCT first-day package. The smallest action is a short DSCT framing
  and Tuesday/Thursday adaptation with an explicit transition to Week 2.
- **B. Week 2 source readiness: NO-GO.** The later dated spine maps Week 2 to
  `lessons/01-orientation-and-learning-practice.md`, which is a 577-byte
  skeleton, and no actual activity, assignment instance, rubric instance,
  instructor material, or student artifact exists. The blueprint instead calls
  Week 2 logic/proof/sequences/sets. This needs source reconciliation plus
  authoring before Week 2 starts.
- **C. Semester instructional-source readiness: NO-GO.** Weeks 2–15 are
  skeleton-only or template-supported, Week 16 is explicitly TBD, and Week 17
  has no resolved final structure. This is a content verdict, independent of
  Canvas/Savnac deployment.
- **D. Source-of-truth coherence: CONFLICTED.** The dated spine is the most
  authoritative operational calendar, but it conflicts with the blueprint's
  week labels and does not resolve the resulting student path.
- **E. Intellectual identity: YES, at design level; not yet reliably in the
  student experience.** The design blueprint, five-part write-up, teaching
  patterns, and DSCT Monday Moment README visibly support reasoning. The
  lessons and assignments do not yet repeatedly instantiate that spine.

## 2. Can Jeremy teach Tuesday from the source we have?

**GO WITH YELLOWS**, assuming the question is content only and deployment is
magically perfect. The shared source supplies a timed instructor guide, reading,
student activity, exit ticket, generic Week 1 assignments, and rubrics:

| Need | Evidence | State |
|---|---|---|
| Course identity/framing | `course_metadata.yaml`; `planning/fall-2026-course-design.md`; shared `monday_survive_this_semester/reading.md` | Course identity exists; shared framing still says “CS1 reference instance” and the DSCT slot is not written. |
| Learning rhythm | shared Monday/Wednesday/Friday instructor guides and README | Usable generic rhythm, but not adapted to DSCT’s Tuesday/Thursday meetings. |
| Reasoning/evidence | `assignments/weekly-problem-solving-writeup.md`; `templates/weekly-rubric.md`; shared Expected/Actual/Tried practice | Strong transferable foundation; not yet a DSCT first-day student artifact. |
| Study practice | shared reading/activity/instructor guide: small steps, debugging story, evidence, Pomodoro, SMART goals | Exists and is teachable. |
| Immediate tools/accounts | shared guides say Canvas/portal but do not provide a DSCT-specific account/tool checklist | Yellow; source does not establish a complete immediate checklist. |
| AI expectations | `planning/fall-2026-course-design.md`; `monday_moments/README.md` | DSCT-shaped principle exists; no first-day student-facing AI instruction or weekly Moment exists. |
| Accessibility/help | shared generic help language and portal caveats; no DSCT accessibility/help page or exact local support path | Yellow; do not invent local policy. |
| First-day activity/evidence | shared `monday_survive_this_semester/student_activity.md` and exit ticket | Exists, but generic and Monday-shaped. |
| Transition to DSCT content | `planning/fall-2026-spine.md` says Week 2 orientation; no usable Week 2 lesson | Missing as a student-ready transition. |

The Tuesday blocker is not the absence of all kickoff material. It is the
missing DSCT adaptation and the unresolved course transition. Do not treat the
shared repo’s generic completeness as DSCT-specific completeness.

## 3. Week 1 content readiness

Instructor-ready: **partial**. Jeremy can teach the generic launch sequence
from the shared guide and activity. Student-source-ready: **partial**. The
shared handouts, assignments, and rubrics exist. Conceptually planned only:
DSCT framing, DSCT’s precise-reasoning explanation, the T/Th adaptation, and
the transition to actual DSCT work. Missing: a DSCT-specific first-day package,
explicit accessibility/help source, and a concrete immediate tools/accounts
checklist.

Category: `AUTHORING GAP`, with the calendar/framing part also a `SOURCE
CONFLICT`. Blocks Tuesday only in the “teach DSCT cleanly” sense; it does not
block a generic orientation. Smallest action: author the DSCT Monday-slot
equivalent as a short Tuesday launch segment, adapt the shared activity to T/Th,
and state what students do before the next meeting. This audit does not perform
that action.

## 4. Week 2 content readiness

The operational reading of the dated spine is authoritative for dates and
meeting rhythm because it is later, dated, specific, and explicitly written as
the Course Foundry structural input. Under that reading, Week 2 is
`lessons/01-orientation-and-learning-practice.md`. It contains objectives,
topic nouns, and historical pointers only. No lesson sequence, examples,
slides/handout, activity, write-up instance, rubric instance, concept check,
or AI-verification exercise exists.

The pedagogical blueprint remains the stronger source for intended learning
design and says Week 2 is logic/proof/sequences/sets, with a proof-feedback
exemplar required. The two files are not merely different views of one
calendar: the week numbers change the first DSCT-specific experience and all
ZyBooks mappings. Therefore this is a **SOURCE CONFLICT**, not a harmless label
variation. The smallest action before Week 2 is Jeremy/source-owner
reconciliation of the operational Week 2 identity, followed by authoring the
selected package. If the blueprint’s logic/proof intent is retained, the
proof-feedback exemplar and a complete claim/proof activity must exist before
that week; if the spine’s orientation week is retained, that package must be
authored instead. Week 1 can be used to prepare either package, but cannot
substitute for it.

## 5. Source-authority map and conflicts

| Topic | Competing/current sources | Most authoritative current interpretation | Confidence | Needs Jeremy? | Why |
|---|---|---|---|---|---|
| Course identity | `course_metadata.yaml`; course-design blueprint | COMSC-2043, operational display name “Discrete Structures and Critical Thinking,” in-person T/Th at Stafford 259 | High | No | Metadata is explicit and provenance-backed. |
| Operational calendar | course-design blueprint; dated 17-week spine | Use the dated spine for the calendar, while retaining blueprint outcomes; reconcile the Week 2 label before student publication | High | Yes | Later dated spine is more specific, but conflict is material. |
| Week 1 | shared kickoff repo; DSCT spine; course blueprint | Universal kickoff is Week 1, but DSCT’s own framing and T/Th delivery are unfinished | High | Yes | Shared source deliberately leaves course-specific slot open. |
| Week 2/logic proof | blueprint; spine; ZyBooks CSV | Spine maps logic/proof to W3 and orientation to W2; blueprint maps logic/proof to W2 | High | Yes | Affects content order and reading. |
| Reasoning method | blueprint; weekly write-up; weekly rubric; teaching-pattern history | Five-part evidence format is the intended common method; only the template layer is implemented | High | No | Authoring gap, not a new policy. |
| AI strand | DSCT Monday Moment README; shared AI Fluency architecture | DSCT has a local “audit AI reasoning” concept, but no complete DSCT delivery map or authorized generic import | Medium | Yes | Avoid copying adjacent-course design by inference. |
| Late semester | blueprint; spine; historical references in lesson 14 | Project/reflection intent exists; Week 15–17 dates/format remain unresolved in current source | High | Yes | No durable DSCT record supports the newer Farkle claim. |
| ZyBooks | `planning/zybooks-section-decisions.csv`; metadata; JTT report pointers | Use the 126-row local mapping structurally; live adoption/roster/LTI/dates require external verification | High | No for source audit | 300B must not scrape or change live vendor state. |
| Grading/final/project policy | templates and design prose | Not decided in current durable source | High | Yes | Do not invent weights, final format, or tooling. |

## 6. Fall 2026 semester readiness matrix

The machine-readable form is `runs/.../derived/semester_readiness.csv`. In
summary: Week 1 is **PARTIAL**; Weeks 2–15 are **SKELETON ONLY** because the
lesson and/or reusable template does not constitute a scheduled instructional
package; Week 16 and Week 17 are **PLANNED ONLY**. The spine’s holiday notes
correctly remove Thu Oct 15 and Thu Nov 26, but no corresponding lesson
materials or alternate pacing are authored.

Important named gaps from the blueprint: proof-feedback exemplar, matrix
example, cryptography scenario, supported coding environment, counting decision
tree, probability simulation starter, graph modeling cases, Boolean-to-circuit
bridge, finite-state builder, synthesis project guide/success criteria, and
review/final structure. Each is an `AUTHORING GAP` unless a policy choice is
required first.

## 7. Reasoning Odyssey / critical-thinking coherence

The design stance is coherent and unusually specific: students should state a
claim, identify definitions and assumptions, do inspectable work, check it,
and communicate a concise conclusion. The reusable write-up and rubric embody
`Sources`, `Rules/Assumptions`, `Work`, `Check`, and `One-Sentence Summary`.
Historical teaching-pattern evidence supports this as a genuine recurring
practice rather than a new invention.

Implementation is discontinuous:

- The five-part structure is explicitly implemented in the weekly write-up and
  rubric templates, but no week-dated assignment instances use it.
- Lessons mention proof, modeling, code, and simulation, but do not provide
  worked examples, checks, or revision tasks.
- Pair-programming and show-and-tell templates name evidence, but no current
  schedule or artifact connects them to course weeks.
- The local Monday Moment README is DSCT-shaped: it says to audit fluent but
  invalid proofs and identify the violated rule. It is a README/template, not
  a student-ready weekly strand.
- No durable source in the current JTT ledger establishes the phrase “Reasoning
  Odyssey,” “love AI more, trust AI less,” or a specific DSCT late-semester
  Farkle/machine-learning plan. Adjacent CS1/AI artifacts are not DSCT truth.

**Identity answer:** yes, the source visibly supports a reasoning-centered
course at blueprint level; no, it does not yet reliably deliver that identity
week by week. Reinforce the spine later by turning the five-part method into
real weekly prompts/rubrics, adding proof/counterexample critique, and making
AI verification a DSCT-specific evidence task.

## 8. AI-verification strand readiness

The DSCT README at `monday_moments/README.md` is a strong local concept: AI is
useful as an object of study, and students should find gaps in convincing
proofs. `planning/fall-2026-course-design.md` adds label-and-verify guidance.
That is better than merely copying generic AI material. But there is one README
and one template, zero weekly Moments, no rubric criterion, and no first-day
student guidance. Status: **PARTIAL / AUTHORING GAP**, later than Tuesday except
for a short expectation statement. The separate `ai_fluency` repository is
shared architecture, not proof of a DSCT implementation.

## 9. ZyBooks/readings coherence

The local CSV verifies the requested structural totals: **126 rows: 75 KEEP,
46 OPTIONAL, 5 UNUSED**. Every KEEP row has a `target_week_topic`; the local
plan maps them to W3–W15 rather than the shared kickoff. OPTIONAL rows are
classified as optional in the manifest and are not, in the current DSCT source,
marked KEEP elsewhere. The lean design is conceptually coherent: roughly 60%
required sections leave room for instructor-created reasoning work.

What cannot be established here: live course roster, active assignment state,
current section contents, due dates, LTI, or whether live configuration matches
the local CSV. Those are `EXTERNAL VERIFICATION` for 300C/later deployment
work, not grounds to guess. Workload is still a risk because the instructor
materials that make a lean reading path teachable are absent. The planned
weeks are not duplicated in the CSV, but the W2/W3 source conflict is a
reading-order contradiction.

## 10. Historical material worth salvaging

The bounded archive summary is `derived/historical_structure_summary.json`.
The best salvage candidates are the recurring five-part problem-solving rubric;
small programs/simulations with visible tests and output; cryptography pair
work; finite-state/Hamilton-path applications; coding-odyssey/project
artifacts; spring 2026 Farkle/Q-learning material; and reflection patterns.
Historical due dates, grade weights, final formats, and Canvas objects are not
Fall 2026 authority.

## 11. Authoring gaps versus Jeremy decisions

`AUTHORING GAP`: DSCT Week 1 framing/T/Th adaptation; every usable lesson
package; proof-feedback exemplar; matrix example; cryptography scenario;
supported coding environment; counting decision tree; probability starter;
graph cases; Boolean/circuit bridge; finite-state builder; project guide;
success criteria; weekly student artifacts; and DSCT AI Moments.

`SOURCE CONFLICT`: Week 2 identity and the corresponding W2/W3 reading/order;
late-semester blueprint versus spine shape.

`JEREMY DECISION`: grading weights and final format; project choices/tooling;
non-code path for programming-dependent work; student-facing due-date cadence;
whether career evidence is assessed course-wide or advisory-only. No newer
durable evidence resolved these candidates. Question files 004–008 were
created in JTT for these policy choices.

`EXTERNAL VERIFICATION`: live ZyBooks adoption/roster/LTI/section state and
live LMS objects. Owned by later deployment work.

`LATER QUALITY IMPROVEMENT`: richer historical salvage, full AI Fluency
cross-course reconciliation, and polishing every later-week example after the
launch-critical packages exist.

## 12. MUST BEFORE TUESDAY

1. Resolve and author the DSCT-specific kickoff framing and T/Th path; include
   the immediate help/accessibility/tools information that source actually
   supports.
2. Decide whether the operational Week 2 is orientation or logic/proof, then
   state that choice consistently in the spine, blueprint, and reading map.
3. Do not represent the current lesson skeletons as student-ready content.

## 13. SHOULD DURING WEEK 1

Author the selected Week 2 package, including a real activity, student
write-up, evidence/rubric expectations, instructor example, and concept check.
If logic/proof is selected, the proof-feedback exemplar is the smallest
non-negotiable example. Resolve the later policy questions before building
grading or project mechanics.

## 14. CAN WAIT

Weeks 3–17 authoring after the W2 decision; complete AI Moment sequence;
historical refinements; live ZyBooks/LMS verification; and any deployment or
assessment infrastructure. Those belong to 300C/300D or later prompts as
specified by the parent audit.

## 15. Question files created or proposed

Created in clean JTT: `questions/004_dsct_grading_and_final_format.md`,
`005_dsct_project_and_tooling.md`, `006_dsct_non_code_participation_path.md`,
`007_dsct_career_strand_assessment.md`, and
`008_dsct_student_due_date_cadence.md`. They are not Tuesday blockers, but
they block honest semester assessment authoring. No question was created for
the unsupported “new Farkle” claim; there is no durable evidence from which to
formulate it as an established decision.

## 16. Exact handoff to Prompt 300E

Prompt 300E should consume this report and the four derived artifacts, then
combine them with 300C deployment and 300D assessment/testing evidence. Carry
forward: Tuesday **GO WITH YELLOWS** (content-only), Week 2 **NO-GO**,
semester source **NO-GO**, source coherence **CONFLICTED**, and identity
**reasoning-centered in design but under-authored in implementation**. Do not
interpret the report as evidence that Canvas/Savnac is current; no deployment
was performed. The single shortest content path is: DSCT kickoff adaptation →
Week 2 source decision → one complete Week 2 instructional package → repeat
the evidence spine for later weeks.

## 17. Evidence appendix

- 300A handoff: `jeremy_task_tracking/reports/300A_maise_repo_bootstrap.md`
- 300A machine handoff: `jeremy_task_tracking/runs/2026-08-14_prompt300A_maise_repo_bootstrap/derived/repo_handoff.json`
- current inventory: `runs/2026-08-14_prompt300B_course_source_audit/derived/current_content_inventory.csv`
- semester matrix: `runs/2026-08-14_prompt300B_course_source_audit/derived/semester_readiness.csv`
- conflict table: `runs/2026-08-14_prompt300B_course_source_audit/derived/source_conflicts.csv`
- historical summary: `runs/2026-08-14_prompt300B_course_source_audit/derived/historical_structure_summary.json`
- source receipt/raw check: `runs/2026-08-14_prompt300B_course_source_audit/receipts/source_state.json` and `raw/20260814T_prompt300B_source_checks.raw.txt`
- key current source: `course_metadata.yaml`, `planning/fall-2026-course-design.md`, `planning/fall-2026-spine.md`, `planning/zybooks-section-decisions.csv`, `monday_moments/README.md`
- shared Week 1 source: `/mnt/nora/git/semester_kickoff_week/`
