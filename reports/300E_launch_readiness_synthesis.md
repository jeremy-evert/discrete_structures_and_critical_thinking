# Prompt 300E — DSCT Launch Readiness Synthesis

Audit date: **Friday, 2026-08-14**  
First meeting: **Tuesday, 2026-08-18, 12:30–1:45 PM, Stafford 259**  
Course: **COMSC-2043-1420, Discrete Structures & Critical Thinking**

This is a synthesis and sequencing report. It does not author course content,
change Course Foundry, write to Savnac/Canvas, run Marker on students, run a
watcher, launch NRP, or execute Prompt 301.

## 1. Executive answer: Can Jeremy teach Tuesday?

**YES — GO WITH YELLOWS.** Jeremy can walk into Stafford 259 and teach a
coherent first DSCT class if Tuesday is treated as a bounded, local/shared
source kickoff: explain the DSCT reasoning identity, adapt the existing kickoff
activity to a Tuesday/Thursday rhythm, give only source-supported help/tools/
accessibility guidance, and state a conservative bridge to the next meeting.

The yellow is real: the DSCT-specific framing is not authored, the shared
kickoff is Monday/Wednesday/Friday-shaped, and the current DSCT deployment path
cannot produce or publish a course plan. Those facts make the LMS/student path
unsafe to claim as ready; they do not make a first in-person teaching meeting
impossible. The Week 2 identity must be owned before a precise Week 2 promise
is published, but it need not be fabricated in order to teach the first
orientation meeting.

## 2. Verdict stack

| Question | Verdict | Boundary of the verdict |
|---|---|---|
| Tuesday first-class teachability | **GO WITH YELLOWS** | Local/shared source is enough for a bounded first meeting; DSCT framing and T/Th adaptation remain to be authored. |
| Week 1 LMS/student path | **NO-GO** | No DSCT desired-state producer is registered, and the reusable kickoff adapter is M/W/F-shaped rather than T/Th-safe. |
| Week 2 instruction | **NO-GO** | Orientation versus logic/proof remains a material source decision; neither candidate has a complete teachable package. |
| Week 2 deployment once content exists | **NO-GO** | A DSCT `DesiredCourse` builder/registration and DSCT-safe T/Th mapping are missing; Savnac course `4` is only source-backed, not verified. |
| Week 2 automated Marker/Coach feedback | **NO-GO** | Generic engines are usable, but DSCT lacks an offering-specific rubric adapter, observable criteria, and an approved substantive Coach bundle. |
| Full semester | **NO-GO** | Weeks 2–15 are mostly skeleton/template-supported; Weeks 16–17 and grading/project policy remain unresolved. |

These are deliberately separate axes. The deployment and automated-assessment
NO-GOs must not be collapsed into the content verdict, and neither may be
back-projected into “Tuesday cannot be taught.”

## 3. MINIMUM VIABLE TUESDAY — 2026-08-18 12:30 PM

This checklist is the smallest credible first-meeting package. It is a list of
completion actions for the next implementation prompt, not work performed by
300E.

| Item | Why actually needed Tuesday | Source/evidence | Owner | State now | Smallest completion action |
|---|---|---|---|---|---|
| DSCT identity and purpose | Students need to know what kind of reasoning course they entered. | `course_metadata.yaml`; fall-2026 design blueprint; 300B | Jeremy + DSCT source owner | Partially present at blueprint level | Write a short DSCT-specific opening that names claims, assumptions, work, checking, and concise conclusions. |
| Tuesday/Thursday run-of-show | The reusable guide is M/W/F-shaped and cannot be presented as DSCT’s schedule. | `semester_kickoff_week` guide/activity; 300B and 300C | DSCT source owner | Generic material exists; T/Th adaptation missing | Convert the first-meeting activity and next-meeting handoff to Tuesday/Thursday language without changing the shared source’s meaning. |
| First activity and exit evidence | A first class needs a bounded student action and a way to see what students understood. | Shared kickoff `student_activity.md` and exit ticket; 300B | DSCT source owner | Reusable activity exists | Add DSCT framing and a small evidence/check prompt; do not invent grading weights. |
| Immediate help, accessibility, and tools message | Students need safe next actions, but unsupported local policy must not be invented. | Shared guide caveats; 300B | Jeremy | Yellow; no DSCT-specific checklist | Include only source-supported Canvas/portal/help/accessibility/tool guidance and label anything that still needs local confirmation. |
| Conservative bridge to the next meeting | The first class should not promise a false Week 2 sequence. | 300B source-conflict finding | Jeremy | Unresolved | Either record the Week 2 choice before publication or use bounded language (“we begin the DSCT reasoning sequence next”) without naming an unchosen topic. |

The Tuesday package does **not** require a full semester, a production LMS
load, automated grading, a watcher, or NRP. Jeremy can keep the source bundle
locally available and teach from it if the LMS path is unavailable.

## 4. NOT A TUESDAY BLOCKER

The following may remain unfinished when class begins, subject to the narrow
Tuesday package above:

- the complete Week 2 lesson, assignment, rubric, exemplar, and Coach bundle;
- the DSCT `DesiredCourse` producer, Course Foundry registration, and Imprint
  dry-run path;
- verification of the claimed Savnac course `4` target or Maise-to-Brandy
  runtime reachability;
- real Canvas/Savnac publication, real student data, and real grading writes;
- a DSCT Marker rubric adapter, automated Coach feedback, and local DSCT
  synthetic acceptance battery;
- the watcher/valve implementation, Dispatch live proving, and any duplicate
  watcher work;
- Synthetic Student Laboratory expansion and every NRP job;
- Weeks 3–17 authoring, late-semester project/final design, grading weights,
  project/tooling policy, non-code policy, career-strand grading, and the
  general due-date policy;
- historical salvage or generalized Course Foundry/Marker research.

These are not “unimportant.” They are simply not legitimate reasons to stop a
bounded first in-person meeting.

## 5. Reconciled A–D evidence

### 5.1 Ledger interpretation

300A establishes repository runway, not course readiness. 300B establishes
instructional source readiness. 300C establishes the source-to-deployment
failure seam. 300D establishes assessment-contract readiness. Repeated mentions
of “Week 2 missing” across B, C, and D are one dependency chain with three
different consequences, not three independent content blockers.

| Finding | Source report | Verdict | Evidence class | Tuesday impact | Week 2 impact | Semester impact | Owner | Dependency | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| Core Maise repository set is present and accounted for | 300A | Ready | `DEPLOYMENT_CODE` | None | Enables work | Enables work | Maise/JTT | Clean source checkouts | High |
| Shared kickoff and reasoning templates exist | 300B | Partial / reusable | `COURSE_CONTENT` | Enables bounded teaching | Requires DSCT adaptation | Reusable spine | DSCT source owner | Shared kickoff source | High |
| DSCT framing, immediate tool/help guidance, and T/Th path are under-authored | 300B | Yellow | `COURSE_CONTENT` | Yellow for a clean class | Must be corrected for student experience | Repeats as weekly authoring gap | Jeremy + DSCT | Shared material | High |
| Five-part reasoning format exists at template/design level | 300B, 300D | Coherent but under-instantiated | `COURSE_CONTENT` | Useful teaching spine | Must become observable criteria | Must recur weekly | DSCT author | Real assignment package | High |
| Operational Week 2 spine says orientation; blueprint says logic/proof/sequences/sets | 300B | Unresolved conflict | `SOURCE_CONFLICT` / `JEREMY_DECISION` | Does not prevent bare kickoff; affects bridge | First gate; blocks honest package | Cascades through W2/W3 pacing | Jeremy/source owner | Question 009 | High |
| No complete Week 2 lesson/activity/assignment/rubric/exemplar/material bundle exists | 300B | No-go | `COURSE_CONTENT` | None if Tuesday is bounded | Direct blocker | Indicates semester under-authoring | DSCT author | Week 2 identity | High |
| No DSCT `DesiredCourse` producer or Course Foundry registration exists | 300C | No-go | `DEPLOYMENT_CODE` | LMS path no-go; local teaching survives | Blocks intended deployment | Blocks full course deployment | Course Foundry + DSCT | Stable source references | High |
| Imprint and Harbor generic contracts are substantially reusable | 300C | Go / yellow | `DEPLOYMENT_CODE` | None | Avoids wholesale rewrite | Supports later scale | Imprint/Harbor | DSCT producer | High |
| Shared kickoff adapter is direct-Harbor and M/W/F-shaped | 300C | Not reusable as-is | `DEPLOYMENT_CODE` | LMS path no-go | T/Th mapper required | Legacy debt | Course Foundry + kickoff owner | DSCT T/Th contract | High |
| Claimed Savnac course `4` and Maise read path are unverified | 300C | Unknown | `RUNTIME_VERIFICATION` | Not needed for local teaching | Must verify before claiming target | Real deployment gate | Harbor/Savnac operator | Safe read access | High |
| Marker generic engine is usable for drafts | 300D | Go | `ASSESSMENT_CONTRACT` | None | Does not solve DSCT semantics | Reusable | Marker | Clean inputs | High |
| DSCT rubric adapter and observable DSCT criteria are missing | 300D | No-go | `ASSESSMENT_CONTRACT` / `COURSE_CONTENT` | None | Blocks trustworthy automated feedback | Must be authored/adapted | DSCT + Marker | Frozen W2 rubric | High |
| Coach generic engine works but lacks substantive DSCT material | 300D | No-go at DSCT seam | `ASSESSMENT_CONTRACT` | None | Blocks grounded feedback | Repeats per package | DSCT + Coach | Approved material bundle | High |
| Marker→Coach schema and Dispatch contract are generic and bounded | 300D | Go with yellows | `ASSESSMENT_CONTRACT` | None | Supports later integration | Reusable | Marker/Coach/Dispatch | DSCT contract | High |
| Watcher/valve is external and in flight elsewhere | 300D | External dependency | `EXTERNAL_WATCHER` | Not a blocker | Integration checkpoint only | Needed for automation later | External watcher owner | Frozen handoff contract | High |
| Local synthetic smoke works generically; DSCT lab inputs do not exist | 300D | Yellow / DSCT no-go | `ASSESSMENT_CONTRACT` | None | Run after real inputs | Precedes useful scale | DSCT + lab | W2 rubric/materials | High |
| NRP is scale-only | 300D | Defer | `RESEARCH_SCALE` | None | None | Research after local evidence | NRP/lab owner | Stable local contract | High |
| Grading/final, project/tooling, non-code, career, and due-date policies are open | 300B; JTT questions 004–008 | Jeremy-owned | `JEREMY_DECISION` | None for kickoff | Due-date policy can affect W2 publication; others later | Blocks honest semester mechanics | Jeremy | Existing question files | High |

The only new source conflict requiring a new question is Week 2 identity. It is
created as `jeremy_task_tracking/questions/009_dsct_week2_identity.md` in the
separate tracking change.

## 6. True critical path

The shortest trustworthy path has a teaching bypass for Tuesday and a separate
content/deployment/assessment chain for Week 2. The rows below use the prompt’s
deadline buckets rather than a generic priority scale.

| ID | Exact objective | Lane | Repo(s) | Kind | Prerequisite | Unlocks | Deadline bucket | Parallelism |
|---|---|---|---|---|---|---|---|---|
| CP-1 | Produce the bounded DSCT Tuesday framing, T/Th run-of-show, activity/exit check, and source-supported help/tools message. | Tuesday | DSCT + shared kickoff read-only | `AUTHORING` | 300B evidence | Coherent first class | **MUST BEFORE TUESDAY** | Can run beside read-only target verification; do not share a write checkout. |
| CP-2 | Own the orientation-versus-logic/proof decision and record the selected operational identity. | Week 2 gate | JTT + DSCT | `DECISION` | 300B conflict | Honest Week 2 authoring brief | **MUST BEFORE TUESDAY** for a precise bridge; otherwise before W2 authoring | Can run beside CP-1 only if the Tuesday bridge remains topic-neutral. |
| CP-3 | Author the selected Week 2 lesson/instructor guide, reading selections, examples, activity, write-up, rubric, exemplar, concept check, check step, and AI-verification expectation. | Instruction | DSCT | `AUTHORING` | CP-2; cadence decision if dates are published | Student- and instructor-ready Week 2 contract | **SHOULD DURING WEEK 1** / **MUST BEFORE WEEK 2 STARTS** | Can run beside CP-4 after the identity/schema is frozen. |
| CP-4 | Define a minimal deterministic DSCT desired-state contract using tracked source references, no invented dates/content, and a T/Th-safe module shape. | Deployment | DSCT + Course Foundry | `ENGINEERING` | CP-2; stable source-reference shape | Safe builder implementation without redoing content | **SHOULD DURING WEEK 1** | Can run beside CP-3; T/Th object mapping waits for CP-1/CP-3 details. |
| CP-5 | Verify the claimed Savnac DSCT target and executing-host read path using a safe read only. | Deployment | Harbor/Savnac/operator | `VERIFICATION` | Access and source-backed candidate target | Evidence for target selection or a documented runtime fallback | **SHOULD DURING WEEK 1** | Independent of CP-1–CP-3; can run in a separate checkout/host. |
| CP-6 | Implement/register the DSCT builder and run the highest honest local/dry-run verification. | Deployment | Course Foundry + DSCT + Imprint/Harbor contracts | `ENGINEERING` + `VERIFICATION` | CP-3 source package; CP-4 contract; CP-5 target evidence for target-specific work | Week 2 deployment candidate | **MUST BEFORE WEEK 2 STARTS** if LMS delivery is required | Must not race another worker editing Course Foundry; use a separate worktree/branch. |
| CP-7 | Freeze DSCT rubric/material manifest, add a fail-closed DSCT rubric adapter, and run the 3–5-case local synthetic battery. | Assessment | DSCT + Marker + Coach + synthetic lab | `ENGINEERING` + `VERIFICATION` | CP-3 real rubric/materials | Trustworthy automated-feedback candidate | **MUST BEFORE WEEK 2 STARTS** only if automation is promised; otherwise manual fallback | Can run beside CP-6 after CP-3, with separate worktrees. |
| CP-8 | Choose Week 2 delivery mode: intended dry-run-verified path, or exact source-backed manual delivery with no shadow canonical copy; verify student/instructor artifacts. | Release gate | DSCT + Course Foundry/Harbor as applicable | `VERIFICATION` | CP-3 plus CP-6, or documented fallback | Trustworthy Week 2 start | **MUST BEFORE WEEK 2 STARTS** | Serial gate after the selected delivery evidence. |
| CP-9 | Hand the frozen contract to the external watcher/valve effort and verify only the integration seam. | Feedback | External watcher + Marker/Coach/Dispatch/Harbor | `VERIFICATION` / `OPTIONAL` | CP-7 contract and watcher availability | Future automated feedback path | **CAN WAIT UNTIL AFTER WEEK 2** | Do not implement a duplicate watcher. |
| CP-10 | Author semester batches (begin with Weeks 3–5), resolving policy questions before grading/project mechanics. | Semester | DSCT | `AUTHORING` | CP-2; W2 evidence is the pattern | Sustainable semester build | **SEMESTER / RESEARCH / SCALE ONLY** | Parallel only in distinct source worktrees after W2 contract is stable. |
| CP-11 | Expand synthetic cases and run an informative local model comparison; package for NRP only if local evidence justifies scale. | Research/scale | Synthetic Student Laboratory + NRP | `OPTIONAL` / `VERIFICATION` | CP-7, CP-9, reviewed manifests | Research evidence, not course policy | **SEMESTER / RESEARCH / SCALE ONLY** | Safe after local contracts; never on Tuesday/Week 2 critical path. |

### Lane summary

- **Lane 1, Tuesday:** CP-1, with CP-2 only needed for a topic-specific
  transition. This is the shortest route to the room.
- **Lane 2, Week 2 instruction:** CP-2 → CP-3.
- **Lane 3, deployment:** CP-4 and CP-5 can begin in parallel after the
  decision/contract boundary; CP-6 follows CP-3 for a real package.
- **Lane 4, assessment:** CP-3 → CP-7. Marker/Coach generic readiness is not
  a substitute for the DSCT rubric/material contract.
- **Lane 5, watcher:** CP-9 is an integration checkpoint only. The watcher is
  not re-planned or reimplemented here.
- **Lane 6, semester:** CP-10 follows the Week 2 pattern in bounded batches.
- **Lane 7, research/scale:** CP-11 follows local evidence; NRP stays out of
  launch sequencing.

## 7. End-of-Week-1 gate

By the end of DSCT’s first instructional week, all of the following must be
true for the course not to be running ahead of its authored material:

1. Tuesday’s framing/activity and Thursday’s continuation are source-backed,
   T/Th-shaped, and available to Jeremy and students through the selected
   delivery mode.
2. The Week 2 identity is recorded as a durable decision, not left as two
   contradictory labels.
3. The selected Week 2 package has a completeness checklist and named source
   revisions; no skeleton lesson is represented as complete.
4. If Week 2 due dates are shown to students, question 008 has been answered
   or a cadence has been explicitly approved. No date is copied from historical
   Canvas or invented from a weekday pattern.
5. The DSCT deployment contract identifies source references, module/object
   ordering, T/Th placement, target-selection inputs, and dry-run safety.
6. The assessment contract names observable evidence for the selected topic and
   states whether feedback is manual or automated; it does not silently treat
   Dispatch as a grader.

## 8. Before-Week-2 gate

Before the first real Week 2 meeting, the following exact student-facing and
instructor-facing artifacts must exist for the selected identity:

- an instructor guide/lesson sequence with objectives, timing, definitions,
  assumptions, examples, checks, and a transition;
- the required ZyBooks selections with source-backed section references;
- at least one worked/example artifact and a concept check;
- an in-class or preparatory activity with a visible evidence/checking step;
- a student assignment/write-up using the five-part structure: Sources,
  Rules/Assumptions, Work, Check, and One-Sentence Summary;
- an observable rubric with criterion wording capable of distinguishing proof
  from assertion, valid from invalid counterexample, simulation evidence from
  overclaim, and disclosed/verified AI assistance from unsupported answers;
- a proof/counterexample exemplar if logic/proof is selected, or the equivalent
  topic-specific exemplar if orientation is selected;
- a DSCT-specific checking/verification step and AI-verification expectation;
- an approved Coach material bundle containing stable source path/content ID,
  topic/section, content, source revision/hash, and assignment scope;
- source references suitable for a deterministic deployment adapter, plus a
  dry-run receipt or a documented exact-source manual delivery fallback;
- a student-facing location and instructor copy whose contents agree. If LMS
  transport is not ready, manual delivery must use the same tracked source
  artifacts, not a second unofficial course source.

Automated Marker/Coach feedback is a separate conditional gate. If it is not
ready, Week 2 may use human/manual review without changing the pedagogical
contract, provided no automation is promised to students.

## 9. Engineering sequencing / what must wait for content

| Engineering action | Classification | Rationale |
|---|---|---|
| DSCT `DesiredCourse` producer | **CAN BUILD NOW WITHOUT CONTENT RISK**, but only as a schema/contract skeleton | It can safely establish typed inputs, source references, ordering, dry-run behavior, and fail-closed missing-input checks. It must not invent Week 2 content, dates, or grading. The final object mapping waits for CP-3. |
| Course Foundry registration | **SHOULD WAIT FOR WEEK 2 CONTRACT** | Registration can be mechanically small, but wiring a guessed DSCT shape creates rework and makes an incomplete source look deployable. |
| T/Th kickoff mapper/cutover | **SHOULD WAIT FOR WEEK 1/TUESDAY CONTRACT** | The existing mapper is hard-coded M/W/F and the DSCT overlay slot is not a general T/Th input model. |
| Savnac course-4 read verification | **SHOULD WAIT FOR SAVNAC TARGET VERIFICATION** | It is the verification itself and can run independently; do not turn a source comment into a target fact. |
| DSCT rubric adapter | **SHOULD WAIT FOR WEEK 2 CONTRACT** | 300D explicitly forbids parsing DSCT by analogy to the CS1 adapter. Freeze criterion text and caller-supplied points policy first. |
| Local Marker/Coach battery | **SHOULD WAIT FOR WEEK 2 CONTRACT** | The generic smoke already exists; DSCT cases require real criteria, material, and expected labels. |
| Watcher integration | **SHOULD WAIT FOR WATCHER PROJECT** | The external watcher owns orchestration/detection; 300E supplies a seam, not a duplicate implementation. |
| Dispatch live proving | **CAN WAIT UNTIL AFTER WEEK 2** | Dispatch is a comment socket and not a grading authority; no live write is required for the first two gates. |
| Synthetic Student Laboratory DSCT experiment | **LATER / SCALE ONLY** | It becomes meaningful only after the real assignment/rubric/material contract exists. |
| NRP battery | **LATER / SCALE ONLY** | NRP is not required for teaching or Week 2 trust. |

Building the DSCT desired-state producer before the Week 2 conflict is
resolved is safe only at the minimal interface level described above. Building
the full object inventory, due dates, rubric wiring, or T/Th module schedule
before CP-2/CP-3 would create direct rework risk.

## 10. Open Jeremy decisions

| Decision | Existing question file | Needed by | Blocks Tuesday? | Blocks Week 2? | Can defer? | Recommended default if Jeremy has not answered |
|---|---|---|---|---|---|---|
| Week 2 orientation versus logic/proof identity | `questions/009_dsct_week2_identity.md` (new) | Before a precise Week 2 bridge; before CP-3 | Bare kickoff: no; precise bridge: yes | **Yes** | No, not if Week 2 is to be trustworthy | Use the dated spine’s orientation placement as the provisional operational default because it is later, dated, and specific; preserve blueprint logic/proof intent until Jeremy confirms rather than silently rewriting source. |
| Grading weights and final format | `questions/004_dsct_grading_and_final_format.md` | Semester grading and Weeks 16–17 | No | Not for a manually reviewed first W2 package | Yes | Leave weights/final format uncommitted; do not invent points. |
| Project choices and tooling | `questions/005_dsct_project_and_tooling.md` | Project authoring | No | No for a non-project W2 package | Yes | Permit no unrecorded project/tool assumption. |
| Non-code participation path | `questions/006_dsct_non_code_participation_path.md` | Programming/simulation weeks | No | No if selected W2 package does not require code | Yes | Do not promise a path or make code mandatory until answered; choose a non-code-neutral W2 activity. |
| Career-evidence strand assessed or advisory | `questions/007_dsct_career_strand_assessment.md` | Later rubric/grade design | No | No | Yes | Treat it as ungraded/advisory until explicit policy, without changing the question’s durable status. |
| Student due-date cadence | `questions/008_dsct_student_due_date_cadence.md` | Any published Week 2 due dates; later deployment | No | **Yes if dates are published** | Only by withholding invented dates | Use meeting-relative language or no date rather than copying historical cadence. |

Questions 004–008 were read in their current state: all are `OPEN` and all
have blank Jeremy-answer sections. No question is duplicated. The new 009 file
is the one required by the unresolved Week 2 source conflict.

## 11. Prompt 301+ sequence with model assignments and parallelism

The following is the smallest executable sequence. It is a plan only; none of
these prompts was run by 300E.

| Prompt | Title | Goal | Owns repos | Prerequisites | Can parallelize with | Stops before | Suggested model/player | Why this model |
|---|---|---|---|---|---|---|---|---|
| 301 | DSCT Tuesday launch package | Author and verify the bounded DSCT first-class/T/Th package, with a conservative bridge if the Week 2 decision is still pending. | DSCT; read-only `semester_kickoff_week` | 300E report and shared source | Read-only Savnac target verification; 302 decision work in a separate checkout | Week 2 content, Course Foundry, Canvas/Savnac writes, Marker, NRP | **Luna Medium** | Source-constrained instructional authoring and a small package do not need the largest reasoning model. |
| 302 | DSCT Week 2 identity and source contract | Obtain/record Jeremy’s orientation-versus-logic/proof choice and freeze the selected source/reading order and cadence inputs. | JTT + DSCT | Question 009; 300B conflict ledger | 301 can finish only with topic-neutral bridge; CP-4 schema sketch can prepare in a separate worktree | Week 2 lesson authoring and deployment registration | **Luna Large** | This is the consequential synthesis/ambiguity gate where source authority and durable policy must be reconciled. |
| 303 | DSCT Week 2 instructional package | Produce the complete selected Week 2 student/instructor/material/rubric contract and an approved Coach bundle. | DSCT | 302; answer 008 if dates are published | 304’s minimal contract skeleton; target read verification | Course Foundry registration, real LMS writes, automated student grading | **Luna Large** | The package spans pedagogy, source truth, observable evidence, and AI-verification semantics. |
| 304 | DSCT desired-state deployment on-ramp | Implement/register the deterministic DSCT builder, T/Th-safe mapping, dry-run entrypoint, and safe target-selection checks. | Course Foundry + DSCT; contract-only Imprint/Harbor use | 302 schema; 303 source package for final mapping; 300C | 303 authoring and 305 adapter work, with separate worktrees | Real Canvas/Savnac writes and production cutover | **code-oriented Codex worker** | Mechanical repository navigation, typed contract work, and deterministic tests are code-heavy and bounded. |
| 305 | DSCT assessment contract and local acceptance | Add the fail-closed DSCT rubric adapter, preserve authored criteria/points policy, and run the 3–5-case local synthetic acceptance battery. | Marker + DSCT + Coach/test harness | 303 frozen rubric/material bundle | 304 in a separate worktree | Watcher implementation, real students, NRP | **code-oriented Codex worker** | The work is interface/fixture/test implementation; the model should follow an already-frozen contract. |
| 306 | Week 2 delivery decision and verification | Verify that the student/instructor package is coherent and select intended dry-run delivery or exact-source manual fallback. | DSCT + Course Foundry/Harbor as applicable | 303 plus 304; 305 only if automation is promised | None at the final gate | Live writes unless separately authorized | **Terra Medium** | A compact release judgment benefits from cross-repo evidence without requiring a large authoring context. |
| 307 | Watcher/feedback seam integration | Exchange the frozen contract with the external watcher/valve effort and verify only the handoff to Marker/Coach/Dispatch. | External watcher + Marker/Coach/Dispatch/Harbor | 305; external watcher available | 308 semester authoring | Any duplicate watcher or grading-policy implementation | **Terra Medium** | Integration review and ownership boundaries matter more than bulk code generation. |
| 308 | DSCT semester authoring batch 1 | Extend the proven evidence spine to bounded later weeks, starting with Weeks 3–5 and only resolved policy areas. | DSCT | 302; Week 2 gate complete | 307 if source files/worktrees are distinct | NRP and broad semester omnibus work | **Luna Medium** | Repetitive, source-grounded authoring benefits from a medium model and bounded scope. |
| 309 | DSCT local evaluation and scale decision | Expand synthetic cases, compare locally, and decide whether any NRP experiment is informative. | Synthetic Student Laboratory + NRP launcher | 305, 307, frozen manifests | 308 after interfaces stabilize | Automatic NRP launch; no scale without a reviewed contract | **code-oriented Codex worker** | Reproducible fixtures, receipts, and launch plumbing are mechanical; scale remains a human judgment gate. |

Safe concurrency rules:

- 301, 302, and read-only target verification may overlap only with separate
  worktrees or non-writing access. 301 must not publish a topic-specific Week 2
  claim before 302.
- 303 and the minimal 304 contract skeleton may overlap after the contract
  boundary, but final deployment mapping waits for 303.
- 304 and 305 may run concurrently after 303 only in separate branches/
  worktrees because they touch different repositories but share the frozen
  contract.
- 306 is a serial release gate. 307 is external integration, not a reason to
  hold a manual Week 2 path.
- 308 and later work may parallelize only when workers do not edit the same
  DSCT checkout. No two write-heavy workers should share a checkout.

## 12. Future-state ownership architecture

```text
DSCT Git source (course truth: Jeremy/DSCT)
    │
    ▼
Course Foundry DSCT desired-state builder (translation/registration)
    │
    ▼
Imprint (reconciliation)
    │
    ▼
Harbor (Canvas transport and safety boundary)
    │
    ▼
Savnac / Canvas (target; target identity and runtime must be verified)

submission arrival
    │
    ▼
external watcher/valve (orchestration/detection; in flight elsewhere)
    │
    ▼
Marker (assessment draft and escalation)
    │
    ▼
Coach (grounded remediation draft)
    │
    ▼
external watcher/valve
    │
    ▼
Dispatch (feedback comment socket; never a grading authority)
    │
    ▼
Harbor (comment transport and allowlist boundary)
    │
    ▼
feedback comment

synthetic DSCT contracts
    │
    ▼
local synthetic acceptance
    │
    ▼
Synthetic Student Laboratory
    │
    ▼
NRP only when scale is useful and local contracts are reviewed
```

Course source owns what the course should be. Course Foundry owns translation
into desired state. Imprint reconciles. Harbor transports. Marker drafts
assessment, Coach drafts remediation, Dispatch posts comments, and the watcher
owns orchestration. Synthetic and NRP lanes validate/scale; they do not define
course policy.

## 13. Risks and fallback plan

| Risk | Least-bad safe fallback | What must not happen |
|---|---|---|
| Savnac/LMS is not ready Tuesday | Teach the bounded package from the local/shared tracked source; provide a consistent source location and explain that transport is pending. | Do not claim a successful deployment, invent a Canvas ID, or create an unofficial second source of truth. |
| DSCT adapter is not ready by Week 2 | Deliver the exact tracked Week 2 artifacts manually or through an already-authorized source path, with a manifest and instructor copy; keep deployment work dry-run-only until safe. | Do not hand-author a divergent Canvas object set or reuse the M/W/F adapter unchanged. |
| Marker/Coach is not ready by Week 2 | Use human/manual review against the same frozen rubric and material bundle; make no automated-feedback promise. | Do not let Marker’s generic engine invent DSCT criteria, let Coach cite empty materials, or treat Dispatch as grading. |
| Week 2 identity remains unanswered | Teach Tuesday with a topic-neutral bridge and do not publish a false W2 sequence; escalate the decision before authoring/publishing W2. | Do not silently rewrite the spine or blueprint based on a recommendation. |
| Watcher remains unavailable | Keep the contract receipt-bearing and use manual feedback; integrate later. | Do not duplicate the external watcher or bypass ownership boundaries. |
| Local synthetic/NRP evidence is weak | Stop at local fail-closed acceptance and human review. | Do not promote NRP into a launch gate or use synthetic labels as course policy. |

## 14. Evidence appendix

This synthesis consumed the required completed reports and their derived
evidence without repeating their audits:

- 300A: `jeremy_task_tracking/reports/300A_maise_repo_bootstrap.md`,
  `jeremy_task_tracking/runs/2026-08-14_prompt300A_maise_repo_bootstrap/derived/repo_handoff.json`,
  and `derived/dependency_edges.csv`.
- 300B: `reports/300B_course_source_truth_audit.md`, with
  `runs/2026-08-14_prompt300B_course_source_audit/derived/current_content_inventory.csv`,
  `semester_readiness.csv`, `source_conflicts.csv`, and
  `historical_structure_summary.json`.
- 300C: `reports/300C_deployment_plumbing_audit.md`, with
  `runs/2026-08-14_prompt300C_deployment_plumbing_audit/derived/deployment_edges.csv`,
  `seam_verdicts.csv`, `dry_run_level.json`, and `repo_states.json`.
- 300D: `reports/300D_assessment_evaluation_readiness.md`, with
  `runs/2026-08-14_prompt300D_assessment_evaluation_audit/derived/assessment_contract_matrix.csv`,
  `dsct_failure_mode_matrix.csv`, `synthetic_acceptance_plan.md`,
  `watcher_handoff_contract.md`, and receipts `synthetic_smoke.json` and
  `repository_state.json`.
- Current question state: JTT questions `004`–`008` are all OPEN with blank
  Jeremy-answer sections. The new question `009` owns the unresolved Week 2
  identity conflict.

### Synthesis checkout state

At synthesis start, the clean checkouts were:

| Checkout | SHA | Refresh result |
|---|---|---|
| `jeremy_task_tracking` | `d4404c7afbf9b7c007ebfc32af661153404473cd` | `git pull --ff-only`: already up to date |
| `discrete_structures_and_critical_thinking` | `fbceb2b1308be17142c8b9743c15e4e8f6ffb31c` | `git pull --ff-only`: already up to date |

The 300B–300D reports retain their own audited source SHAs and runtime
limitations. 300E does not reinterpret a failed SSH/runtime probe as proof
that Savnac is broken.

### Scope boundary

Only this report and its run artifacts are written in DSCT by 300E. The JTT
pointer and the one required Week 2 question are separate tracking changes.
No implementation repository was changed, no production write was attempted,
and Prompt 301+ was not executed.

