# Prompt 305 — DSCT Reasoning Odyssey vocabulary inventory

## Scope and starting point

This is an independent, read-only archaeology pass over DSCT. The starting
commit was `797819e3962ec8b240993a8b62d72b2a30fee769` (`797819e`). The only
intended write from this job is this report. No ontology, grading policy,
World Bible carry-forward rule, cadence, or student-facing rename is decided
here.

The repository has no `AGENTS.md` and no `rubrics/` directory at this commit.
The project README describes the repository as under construction; the more
specific source contracts below were therefore treated as current truth, and
raw design files and historical reports were treated as provenance rather
than authority.

## Search coverage and exact commands

The initial broad search was:

```sh
rg -n -i -C 2 'Reasoning Odyssey|Coding Odyssey|Reasoning Quest|Reasoning Gate|World Bible|weekly reinforcement|weekly write-up|evidence receipt|reflection|Pair Reasoning|Pair Programming|Show & Tell|A3|A4|A7|checkpoint' --glob '!sidecar/reports/305_reasoning_vocabulary_inventory.md' .
```

The required term-family file inventory was repeated with these exact
commands (the fixed-string form prevents regular-expression interpretation of
the labels):

```sh
for t in 'Reasoning Odyssey' 'Coding Odyssey' 'Reasoning Quest' 'Reasoning Gate' 'World Bible' 'weekly reinforcement' 'weekly write-up' 'evidence receipt' 'Pair Reasoning' 'Pair Programming' 'Show & Tell' 'A3' 'A4' 'A7'; do
  echo "### $t"
  rg -il --fixed-strings "$t" . --glob '!raw/**' --glob '!sidecar/reports/305*' | sort
done
```

The focused source inspection was:

```sh
rg -n -i 'Reasoning Odyssey|World Bible|weekly reinforcement|weekly write-up|checkpoint|evidence receipt|Pair Reasoning|Pair Programming|Show.?and.?Tell|Friday feedback|event reflection|Reasoning Quest|Reasoning Gate|Coding Odyssey|A3|A4|A7' docs/grading-model.md planning/fall-2026-weekly-architecture.md planning/fall-2026-topic-map.md planning/fall-2026-course-design.md planning/week-16.md assignments week-01 week-02 week-16 reports/304_dsct_grading_model.md sidecar/reports/304_pair_reasoning_name_reconciliation.md sidecar/raw/2026-08-17_dsct_design_decision_pile.md
rg -n -i 'Reasoning Odyssey|World Bible|weekly write-up|Reasoning Quest|Reasoning Gate|event reflection|Pair Reasoning|Pair Programming|Show.?and.?Tell|Coding Odyssey|A3|A4|A7' sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md prompts/011_reasoning_odyssey_kickoff_and_week2_proof_slice.md prompts/013_reasoning_odyssey_fabric_reconciliation.md reports/013_reasoning_odyssey_fabric_reconciliation.md sidecar/prompts/304_reconcile_pair_reasoning_name.md
find . -type d -name 'rubrics' -print
```

The first command found 6,243 matching context lines before consolidation.
The second pass was used after drafting the inventory to check that every
meaningful family below was represented. Archive snapshots were searched for
legacy/provenance terms, but were not treated as current DSCT policy.

## Object-level inventory

| Term / label | Representative paths | Status | Apparent student action | Apparent artifact | Gradebook object? | Persistence | Work mode | Similar term / collision | Source or provenance note | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| **Reasoning Odyssey** | `week-01/README.md`; `docs/grading-model.md:23,30-32`; `week-16/README.md`; `assignments/week-16-farkle-evidence-receipt.md` | Current doctrine and current grading label | Make a claim, expose sources/assumptions/work/check, and maintain a longitudinal reasoning trail across technical weeks | Weekly Odyssey gate evidence; larger checkpoint package; Week 16 receipt | Yes: 30% weekly gate + 15% checkpoints in `docs/grading-model.md` | Semester-spanning; Week 1 launches it, Week 16 uses it, Week 17 remains a reflection seam | Individual; may include pair/show-and-tell evidence | Overlaps `weekly write-up`, `evidence receipt`, `Reasoning Quest/Gate`, and `World Bible` | `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:113-150` calls it a persistent spine, but also says the ontology remains to be made crisp | HIGH for existence; MEDIUM for exact boundary |
| **World Bible** | `planning/fall-2026-weekly-architecture.md:41-64`; `week-02/student/week-02-evidence-assignment.md:44`; `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:153-252` | Current planning/provenance concept; not a fully specified student submission contract | Maintain a chosen world/system/problem context and, potentially, claims, definitions, evidence, uncertainty, and change history | Persistent living context/record; no canonical filename or required submission shape found | Not independently established; Week 2 explicitly says optional notes are not graded | Intended persistent across weeks; cross-course carry-forward is explicitly open | Individual | Potentially the implementation of / container for Odyssey; could duplicate weekly evidence if every week requires an update | Current architecture says context is optional/useful and not mandatory fiction; raw quarry proposes a stronger history but marks carry-forward and cadence open | MEDIUM: paths establish intended role but not final object contract |
| **Reasoning Quest** | `sidecar/prompts/305_inventory_reasoning_odyssey_world_bible_vocabulary.md`; `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:125-147,467,618`; `sidecar/raw/2026-08-17_dsct_design_decision_pile.md:148-179` | Raw/provenance proposal; no current operational assignment found using the label | Proposed weekly individual evidence package / confidence beacon | Proposed weekly package, but no current file or gradebook object named Quest | Not independently established | Proposed weekly/event-scale | Individual, with social evidence possibly attached | Alias/overload risk with `Reasoning Gate`, weekly gate, weekly write-up, and evidence receipt | The raw decision pile explicitly asks whether Quest or Gate is the student-facing name and what a checkpoint adds | LOW: proposal-only evidence; ambiguity is named by the source itself |
| **Reasoning Gate** | `sidecar/prompts/305_inventory_reasoning_odyssey_world_bible_vocabulary.md`; `docs/grading-model.md:23`; `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:125-147` | Mixed: current grading table uses “Odyssey gate”; student-facing name is unresolved | Proposed/implicit threshold package demonstrating the week's reasoning is inspectable | Weekly gate object with gate rubric in grading model; no separate assignment file found | Yes as part of 30% weekly gate category, but exact object naming is not finalized | Weekly | Individual; can incorporate pair/public work | Same collision cluster as Quest, weekly write-up, and evidence receipt | `docs/grading-model.md` operationalizes “Weekly reinforcement / Reasoning Odyssey gate”; raw quarry says not to create five names for same work | MEDIUM: current category exists, distinct Quest/Gate ontology does not |
| **Weekly reinforcement** | `docs/grading-model.md:23,30-32`; `week-02/student/week-02-evidence-assignment.md:27-32`; `planning/week-16.md:89-97` | Current grading category label | Complete the substantive weekly technical evidence and interpretation | Week 2 portfolio, formal weekly gate evidence, Week 16 evidence receipt | Yes, 30% category | Recurring weekly | Individual submission; Week 2 work is performed in pairs but individually explained/submitted | Overlaps the Odyssey gate and may be mistaken for a second homework stream | Week 2 explicitly says this is recurring work, not a new category, while grading model places it inside the 45% Odyssey family | HIGH for category; MEDIUM for student-facing package boundary |
| **Weekly problem-solving write-up / weekly write-up** | `assignments/weekly-problem-solving-writeup.md`; `planning/fall-2026-course-design.md:104`; `prompts/011_reasoning_odyssey_kickoff_and_week2_proof_slice.md:57-60`; `reports/013_reasoning_odyssey_fabric_reconciliation.md:39-43` | Current reusable template plus historical/provenance label | Write Sources, Rules/Assumptions, Work, Check, One-Sentence Summary with reproducible evidence | One readable reasoning artifact; no current week-specific submission path | Ambiguous: earlier prompt says distinct from Odyssey; current grading model says the weekly gate is the evidence receipt for actual work | Recurring | Individual | ALIAS/DUPLICATE-HOMEWORK risk with weekly gate, Quest, and evidence receipt | Template is concrete; Prompt 013 says weekly write-ups and recurring labs are the same work, while Prompt 011 contains older contradictory framing | HIGH for template; MEDIUM for relation to Odyssey |
| **Evidence receipt / reasoning receipt** | `assignments/week-16-farkle-evidence-receipt.md`; `planning/fall-2026-weekly-architecture.md:24-25,54-64`; `week-02/instructor/thursday-run-of-show.md:14`; `week-16/instructor/guide.md:232` | Current operational artifact pattern | Preserve searchable observations, checks, interpretation, and limits; submit or leave a trace | Receipt text/files, often using five-part method; Week 2 has six named searchable files plus reflection | Sometimes: current grading model gives gate receipts a grade and separately gives presentation/feedback receipt categories | Event/week-specific, feeding semester trail | Individual; can contain pair or public-event evidence | OVERLOAD: “receipt” names both the evidence format and a possible graded object; overlaps write-up/gate | Weekly architecture requires an individual receipt after critique/revision; Week 16 names a specific receipt assignment | HIGH for function; MEDIUM for whether receipt is a format, object, or both |
| **Pair Reasoning report / reflection** | `assignments/pair-reasoning-report.md`; `docs/grading-model.md:16,59-61`; `planning/fall-2026-topic-map.md:12,14,16,20,22`; `sidecar/reports/304_pair_reasoning_name_reconciliation.md` | Current activity/category name after Prompt 304; contract details still incomplete | Record roles, attempted/built work, evidence, one win, stuck point, next step, and possibly an individual reflection | Individual Pair Reasoning report | Yes: 5%, A3 equivalent | Repeats on selected rotation weeks | Pair activity, individually reported | Historical `Pair Programming` is stale as activity label; distinctness from Odyssey receipt still open | Prompt 304 changed terminology only; it explicitly did not decide pedagogy, grading, or reflection questions | HIGH for current name; MEDIUM for artifact boundary |
| **Pair Programming / paired-programming report** | `archive/*/canvas-*-snapshot*.json`; `docs/curriculum/course-sequence.md`; historical reports and Prompt 304 provenance | STALE-LEGACY in current DSCT operational naming; still relevant historical source vocabulary | Historical pair programming / driver-navigator activity and report | Historical pair report/category, represented in current model as A3-equivalent | Historical/current model seam: A3 equivalent remains in grading model | Historical recurring activity | Pair, individually accountable | ALIAS with current Pair Reasoning where the recurring DSCT activity is intended; ordinary programming references remain literal programming | Prompt 304 report documents 22 old-name path-level hits and confirms current intended surfaces migrated | HIGH for stale name; LOW for whether every archive hit denotes same object |
| **Show & Tell / Show-and-Tell reflection** | `assignments/show-and-tell-artifact.md`; `docs/grading-model.md:17,60-61`; `week-02/instructor/thursday-run-of-show.md`; `planning/fall-2026-topic-map.md:14,18,20,22` | Current activity/category family | Present/defend a proof, problem, demo, program, or idea; capture learning and a question; use peer questions for revision | Individual Show-and-Tell reflection plus shown artifact | Yes: 5%, A4 equivalent; its related feedback is another 5% A7-equivalent | Event-specific on alternating weeks | Public defense/explanation, individually reflected | Duplicate-homework risk if reflection restates Odyssey gate; distinctness from Pair Reasoning and feedback still requires contract | Assignment template says peer questions are evidence of revision or clarification; raw quarry says social dimensions should differ | HIGH for family; MEDIUM for exact reflection boundary |
| **Friday feedback report / peer-feedback report** | `docs/grading-model.md:18,61`; `reports/304_dsct_grading_model.md:36`; `planning/fall-2026-weekly-architecture.md:24-25` | Current grading category label; no standalone assignment template found | Receive critique, revise/expose evidence, and record individual feedback/revision | Individual critique/revision/evidence receipt | Yes: 5%, A7 equivalent | Event-specific on Show & Tell weeks | Peer-feedback / individual revision | OVERLOAD with generic evidence receipt; GRADEBOOK-SEAM with Show & Tell reflection and Odyssey gate | Current model calls it Friday feedback although the DSCT chassis is Tuesday/Thursday; exact student-facing name and rubric remain open | MEDIUM: current category/function are explicit, but the standalone artifact and naming are not |
| **Reasoning Odyssey checkpoint** | `docs/grading-model.md:24,30-32,82`; `sidecar/raw/2026-08-17_dsct_design_decision_pile.md:176-180` | Current category, unspecified schedule/shape | Produce a larger/deeper Odyssey evidence package at selected weeks | Checkpoint object with checkpoint rubric; weeks and exact distinction not selected | Yes: 15% | Occasional/selected weeks | Individual | UNRESOLVED against ordinary gate; both are called Odyssey objects and raw source asks what makes checkpoint larger/deeper | Grading model explicitly leaves exact checkpoint weeks and deployment questions open | MEDIUM: category is current, but object semantics are not supplied |
| **Event reflection** | `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:129-147,1137`; `sidecar/raw/2026-08-17_dsct_design_decision_pile.md:148-179` | Raw/provenance proposal; no exact current DSCT assignment label found | Record what changed when reasoning met other people | Proposed social-change reflection, possibly inside Quest | Not established | Event-specific | Individual after pair/public interaction | DUPLICATE-HOMEWORK risk with Pair Reasoning report, Show-and-Tell reflection, and feedback report | Raw quarry specifically says social reflections should not restate the Quest, which confirms the collision is anticipated, not resolved | LOW: proposal-only and no current artifact contract |
| **Coding Odyssey / coding-odyssey** | `assignments/project-and-final-reflection.md`; `docs/curriculum/course-sequence.md`; `lessons/10-graphs.md`; `lessons/14-synthesis-and-applications.md`; archive Canvas snapshots | STALE-LEGACY | Historical persistent coding/project work and final reflection | Historical project/Git/reflection family | Historical category/assignment semantics vary by archive | Semester/project-scale in historical courses | Individual, often code/project-centered | STALE-LEGACY predecessor/neighbor to Reasoning Odyssey; not evidence that DSCT should retain coding as ontology | Raw quarry says reasoning supersedes coding as the persistent DSCT work; current project reflection still records the historical basis | HIGH for historical existence; MEDIUM for exact archive-to-archive equivalence |
| **A3 / A4 / A7** | `docs/grading-model.md:16-18,37,59-61`; `reports/304_dsct_grading_model.md:34-36,49,66`; archive snapshots; Prompt 304 | Provenance/category shorthand, not stable student-facing labels | A3: pair activity report; A4: Show-and-Tell reflection; A7: feedback/revision report | Three individual graded category families in current model | Yes, 5% each | Rotation/event-specific | A3 pair; A4 public defense; A7 peer feedback | NAME/semantic inheritance may look like aliases, but the current model treats them as separate category buckets; do not infer object identity from codes | Prompt 305 requires A-label lookup where semantic; Prompt 304 says inspect A3 only when it denotes recurring pair activity | HIGH for current semantic mapping; MEDIUM for historical continuity |

## Name versus function matrix

| Name currently used | Function the source appears to require |
|---|---|
| Reasoning Odyssey | Longitudinal course frame / reasoning history, with graded weekly and checkpoint evidence attached somewhere in the family. |
| World Bible | Persistent context or living record in which a student's claims, definitions, evidence, and changes may accumulate. |
| Reasoning Quest | Proposed weekly individual evidence package; source does not establish whether this is the student-facing name. |
| Reasoning Gate | Current weekly threshold/category label for acceptable reasoning evidence; whether it is the same package as Quest is unresolved. |
| Weekly reinforcement | Current gradebook category for substantive recurring weekly evidence, including Week 2 setup and Week 16 synthesis. |
| Weekly write-up | Reusable five-heading reasoning artifact: sources, assumptions, work, check, summary. |
| Evidence receipt / reasoning receipt | Searchable evidence record showing observations, work, checks, interpretation, and limits; may be a format inside another object or a graded submission. |
| Pair Reasoning report | Individual accountability record for a pair-based challenge activity. |
| Pair Programming | Historical name for much of the same recurring pair-activity family; programming is still an instrument, not necessarily the activity identity. |
| Show & Tell reflection | Individual account of a public explanation/defense and what peer questions changed or clarified. |
| Friday feedback / peer-feedback report | Individual record of critique, revision, or evidence exposure associated with a public artifact; exact boundary from a generic receipt is open. |
| Reasoning Odyssey checkpoint | Proposed larger/deeper Odyssey evidence object; source establishes a grade category but not the defining threshold. |
| Event reflection | Proposed individual account of social change in reasoning; no current standalone contract found. |
| Coding Odyssey | Historical coding/project-centered persistent frame, apparently superseded in DSCT by Reasoning Odyssey. |
| A3 / A4 / A7 | Legacy/inherited category identifiers whose current semantic functions are pair report, Show & Tell reflection, and feedback report respectively. |

## Collision-class findings

### ALIAS

- `Pair Programming` is a stale name for the recurring DSCT pair activity now
  called `Pair Reasoning` where the source is talking about that activity.
  `sidecar/reports/304_pair_reasoning_name_reconciliation.md` is provenance for
  the completed naming migration; this report does not redo or extend it.
- `weekly write-up`, `evidence receipt`, and the current `weekly Odyssey gate`
  all describe materially overlapping evidence-bearing work. The repository
  does not prove whether they are one student object with format names or
  several objects.

### OVERLOAD

- `Reasoning Odyssey` names both a persistent intellectual frame and, in the
  grading model, a 30% weekly gate plus a 15% checkpoint family.
- `evidence receipt` names a method/format in weekly architecture and a
  concrete assignment in Week 16; it also appears as a possible feedback or
  presentation receipt.
- `reflection` is used for Week 2 evidence interpretation, Show & Tell, final
  reflection, and proposed event reflection. These are not safely one object.

### DUPLICATE-HOMEWORK RISK

- The same student's weekly claim/check/evidence could be requested as a
  weekly write-up, Quest/Gate, Odyssey receipt, World Bible update, and social
  reflection. The raw quarry explicitly warns against this at
  `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:1119-1137`.
- Show & Tell reflection plus A7 feedback plus an Odyssey receipt could ask
  for three restatements unless each has a distinct function. The source
  currently distinguishes public explanation from critique/revision, but does
  not provide complete student-facing contracts.
- Pair Reasoning report plus a generic event reflection has the same risk.

### STALE-LEGACY

- `Coding Odyssey` / `coding-odyssey` remains in historical course sequence,
  project/reflection, lesson, and archived Canvas material. The raw quarry
  describes the DSCT direction as Reasoning Odyssey, but no archive-wide
  equivalence or migration policy should be inferred.
- `Pair Programming` remains in historical archives and provenance reports;
  current operational DSCT surfaces were migrated by Prompt 304.

### GRADEBOOK-SEAM

- The current model has 30% weekly gate + 15% checkpoints = 45% Odyssey
  family, while also naming 5% Pair Reasoning, 5% Show & Tell, and 5% A7
  feedback. A single weekly experience may contribute evidence to multiple
  categories, but the safe boundary and submission count are not specified.
- Week 2 is explicitly a 40-point portfolio under the Weekly reinforcement /
  Odyssey gate category, while also saying it is not a Reasoning Odyssey
  write-up. This is a useful current distinction but exposes the naming seam.
- A3/A4/A7 are gradebook/category inheritance labels, not proof that the
  student-facing objects should be named A3/A4/A7 or that they are aliases.

### UNRESOLVED

- Whether the student-facing weekly name is `Reasoning Quest`, `Reasoning
  Gate`, `weekly write-up`, `evidence receipt`, or a deliberately smaller
  combination.
- Whether the World Bible is a container inside the Odyssey, the persistent
  implementation of it, an optional context layer, or a separately submitted
  artifact. Current planning makes context useful/optional; raw design makes
  stronger proposals but marks cadence and carry-forward open.
- What makes a checkpoint larger/deeper than an ordinary gate, and which weeks
  receive one.
- Whether Pair Reasoning and Show & Tell reflections are sufficiently distinct
  from the weekly Odyssey evidence to justify separate submission/category
  treatment.
- Whether `Friday feedback report`, `peer-feedback report`, and a generic
  `evidence receipt` are one function with several names or distinct records.

## Medium/low-confidence claims and ambiguity citations

All MEDIUM and LOW rows in the inventory have representative paths in their
row. Consolidated ambiguity notes are:

- World Bible: `planning/fall-2026-weekly-architecture.md:41-64` describes an
  optional/useful context, while `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:153-252`
  proposes a richer persistent reasoning history and leaves literal
  carry-forward open. No canonical submission file was found.
- Reasoning Quest: the only meaningful hits are the prompt and raw design
  quarry (`sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:125-147,467,618` and
  `sidecar/raw/2026-08-17_dsct_design_decision_pile.md:148-179`); the latter explicitly asks Quest vs
  Gate as an unanswered question.
- Reasoning Gate: `docs/grading-model.md:23` establishes a current weekly
  gate category, but no separate Quest/Gate assignment or gate rubric was
  found in the inspected current surfaces.
- Weekly write-up relation: the concrete template is
  `assignments/weekly-problem-solving-writeup.md`, but
  `prompts/011_reasoning_odyssey_kickoff_and_week2_proof_slice.md:57-60`
  distinguishes it from Odyssey while the current model folds the weekly
  evidence into the Odyssey gate. This is a historical/current seam.
- Evidence receipt: `planning/fall-2026-weekly-architecture.md:24-25,54-64`
  uses receipt as a recurring evidence function, while
  `assignments/week-16-farkle-evidence-receipt.md` makes it a concrete
  assignment. The format-versus-object boundary is therefore uncertain.
- Pair Reasoning boundary: Prompt 304's report says the migration changed the
  name only and did not define pedagogy or reflections; the current report
  template and grading row establish a report/category but not its relation
  to the Odyssey receipt.
- Show & Tell / feedback: `docs/grading-model.md:17-18,60-61` establishes two
  categories, but no standalone A7 assignment template was found and the
  weekly architecture describes a combined critique/revision/receipt slot.
- Checkpoint: `docs/grading-model.md:24,82` establishes the category while
  leaving exact weeks and deployment questions open; the raw decision pile
  asks what distinguishes it from a normal gate.
- Event reflection: raw quarry only; `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:1137`
  describes a desired non-duplicative function but no current student-facing
  artifact exists.
- Coding Odyssey archive mapping: current repository paths prove historical
  use, but archive snapshots are not uniform enough to claim one stable
  object definition across semesters.
- A3/A4/A7 continuity: `docs/grading-model.md:16-18` supplies the current
  semantic mapping; historical archive hits supply provenance, not a final
  cross-semester object identity.

## Limited sibling lookups

No sibling repository lookup was needed or used. The DSCT source explicitly
points to A3/A4/A7 as semantic inheritance, but the required meanings were
available in DSCT's current `docs/grading-model.md`, DSCT reports, and local
archive snapshots. Broad CS1/CS2 World Bible archaeology is explicitly
reserved for Prompt 309, so no sibling repository or cross-course conclusion
is smuggled into this inventory.

## Questions for Jeremy + ChatGPT

1. Is `Reasoning Odyssey` only the semester spine, or also the student-facing
   name of the weekly evidence package?
2. Should students see `Reasoning Quest`, `Reasoning Gate`, or neither? If
   both remain, what observable distinction must a student understand?
3. Is the World Bible required, optional, or only updated when meaningful
   context changes? Is it a container, a record, or a separate submission?
4. What evidence makes a checkpoint larger/deeper than a gate, and how many
   checkpoint submissions exist?
5. Which social artifacts are genuinely distinct: Pair Reasoning report,
   Show & Tell reflection, event reflection, and A7 feedback report?
6. Should evidence receipts be a reusable format embedded in graded objects,
   or named gradebook submissions in their own right?
7. How should gradebook category labels A3/A4/A7 relate to student-facing
   names without leaking inherited shorthand or multiplying submissions?

## Coverage and verification

Inspected source families:

| Source family | Result |
|---|---|
| `planning/` | Inspected weekly architecture, topic map, course design, and Week 16 plans. Found current Odyssey/context, Pair Reasoning, Show & Tell, receipt, and grading-placement language. |
| `docs/` | Inspected `docs/grading-model.md`, curriculum sequence, and philosophy/history references. Found current category model plus Coding Odyssey and A-label provenance. |
| `assignments/` | Inspected weekly write-up, Pair Reasoning, Show & Tell, Week 16 receipt, and project/final reflection templates. |
| `rubrics/` | **Absent** at this commit (`find . -type d -name rubrics -print` returned no path). Week 2 has a student-facing rubric under `week-02/student/`, which was inspected separately. |
| Student-facing course content | Inspected `week-01/`, `week-02/`, and `week-16/` README, student, instructor, and relevant activity files. |
| `sidecar/reports/` and `sidecar/raw/` | Inspected Prompt 304 report, grading/history reports, the 2026-08-16 design quarry, and 2026-08-17 decision pile as provenance. The raw files were not treated as current doctrine. |
| Historical archive | Searched Canvas snapshots for Coding Odyssey and A3/A4/A7; used only to establish legacy/provenance existence. |

After drafting, the required terms were searched again with the exact commands
listed above. Every meaningful term family discovered is represented in the
object matrix or explicitly classified as historical/provenance, ambiguous,
or absent as a standalone current object. The only report change is this
file; no planning, assignment, rubric, course-source, raw-quarry, sibling,
Canvas, or JTT file was modified.

The report intentionally stops at evidence inventory. It does not settle the
ontology, gradebook policy, World Bible continuity, checkpoint cadence, or
whether any collision should be resolved by renaming, merging, or splitting.
