# Piper 001 — DSCT Course Verification Recon

Verification date: 2026-08-20

Read anchor: `jeremy-evert/discrete_structures_and_critical_thinking@21881a2a2b2b4a7303dee902f5b630bc8c37318f` (`main` at verification start).

External compiler anchor inspected: `jeremy-evert/course_foundry@969b50aa7f07dedb96049103f52b8bcc9fa0ac5c` (`main` at verification time).

This report is reconnaissance only. No project-truth, Canvas, Savnac, Zoom, Teams, JTT, or shared-repository mutation was performed.

## 1. Executive State

- Fall 2026 DSCT identity is clear and current in `course_metadata.yaml`: COMSC-2043-1420, Discrete Structures / operational display name Discrete Structures and Critical Thinking, traditional in-person, Stafford 259, Tuesday/Thursday 12:30–1:45 PM, 2026-08-17 through 2026-12-11.
- The repository now contains meaningful source for all Weeks 1–17. The older claim that Weeks 4–14 were only a frozen spine is superseded by Job 322 and the current week packages. Week 2 remains a source-level external-dependency yellow; Week 15 is intentionally asynchronous; Week 9 is intentionally Tuesday-only because of Fall Break.
- The Fall 2026 source grading model reconciles to exactly 100%. It settles the Decision Gate / Odyssey checkpoint / Farkle split, one dropped regular Decision Gate, revision/resubmission, and highest-recorded-score doctrine. Exact Canvas mechanics remain implementation seams.
- Current public Course Foundry `main` does **not** match the now-complete DSCT source. Its DSCT builder still says it emits only Weeks 1–2 and explicitly lists Weeks 3–17 as an omission. More seriously, `production_deploy.py` assigns DSCT production course 74035 while the current `dsct_savnac_desired_course()` rejects every course id except Savnac course 4. Therefore the current public production build path is internally contradictory and cannot be treated as a proven current full-semester deploy path.
- Report 319 remains valid evidence that Week 1 reached production completely and Week 2 reached production partially before a CloudFront/WAF content block. Newer Report 321 confirms the live course still had Week 1 at 8 items and Week 2 at 7 items, while also revealing a larger production concern: unrelated published modules, a kickoff-only grading topology, and existing student submissions. Report 321 therefore supersedes Report 319's narrower "not blocking today" conclusion, not its Week 1/2 historical facts.
- Production Canvas course 74035 is the only currently evidenced Fall 2026 DSCT target. The latest repo evidence is read-only and reports 15 active students plus existing submissions. No current safe reconcile, prune, or full-semester production push is proven.
- No current repository source inspected establishes a settled lecture-recording delivery workflow into Canvas. Microsoft Teams and Zoom both support native automatic recording workflows, but actual availability depends on institutional license/admin policy, organizer settings, consent policy, storage/retention configuration, and the classroom machine. These are Flo/job-site verification items.
- Current truth is therefore: **source substantially ready; compiler/deployment and live-course reconciliation not ready to infer; recording infrastructure feasible in principle but unverified locally.**

## 2. Week 1–17 Readiness Matrix

Status here follows the assignment's source-readiness definition. Compiler and live states are shown separately and must not be inferred from a GREEN source row.

| Week | Topic/Role | Source Authored | Compiler Wired | Live Evidence | Status | Important Gap |
|---:|---|---|---|---|---|---|
| 1 | Reasoning Odyssey launch / reasoning as evidence | Yes: student Tuesday/Thursday activities, exits, help/tools, reasoning method; instructor run-of-show | Yes in current public Course Foundry W1/2 builder | Production evidence: published `DSCT Week 1 — Reasoning Odyssey`, 8/8 items in Report 319; newer Report 321 still observes 8 Week 1 items | `GREEN — authored/source-complete` | Current compiler revision has not been re-executed; live student-view/usability still needs a fresh job-site check |
| 2 | Build the local AI lab; reproducibility and evidence | Yes locally, plus authoritative shared sources from `local_ai_lab_setup` and `windows_classroom` | Yes in current public W1/2 builder, but depends on sibling repos | Production evidence: 7/19 items after WAF block in Report 319; newer Report 321 still sees 7 Week 2 items | `YELLOW — partial` | Shared dependency seam; 12 items never proven live; current production builder course-id contradiction; student link/file behavior needs recheck |
| 3 | Container + minimum-useful LaTeX skill ladder | Yes; Tuesday and Thursday are combined in the student ladder with instructor notes | No in current public Course Foundry DSCT builder | None proven | `GREEN — authored/source-complete` | Nonstandard package shape and no current compiler wiring |
| 4 | Logic, Claims & Proof | Yes; formal Tuesday/Thursday package, Show & Tell, Decision Gate | No | None proven | `GREEN — authored/source-complete` | AUTHORED only; no current build/Savnac/production evidence |
| 5 | Sets, Functions & Sequences | Yes; formal package, Pair Reasoning, Decision Gate | No | None proven | `GREEN — authored/source-complete` | AUTHORED only |
| 6 | Algorithms, Correctness & Growth | Yes; formal package, Show & Tell, Decision Gate | No | None proven | `GREEN — authored/source-complete` | AUTHORED only |
| 7 | Integer Properties & Cryptography | Yes; Pair Reasoning; Odyssey Checkpoint 1 replaces ordinary Decision Gate | No | None proven | `GREEN — authored/source-complete` | AUTHORED only; checkpoint gradebook mechanics unproven |
| 8 | Induction, Recursion & Recurrences | Yes; Show & Tell; Decision Gate | No | None proven | `GREEN — authored/source-complete` | AUTHORED only |
| 9 | Counting / Fall Break exception | Yes; Tuesday package; Thursday intentionally absent for Fall Break | No | None proven | `GREEN — authored/source-complete` | Compiler must encode intentional Thursday absence rather than treating it as missing content |
| 10 | Probability, Uncertainty & Evidence | Yes; Show & Tell; Decision Gate | No | None proven | `GREEN — authored/source-complete` | AUTHORED only |
| 11 | Relations, Orders, Matrices & Digraphs | Yes; Pair Reasoning; Odyssey Checkpoint 2 replaces ordinary Decision Gate | No | None proven | `GREEN — authored/source-complete` | AUTHORED only; checkpoint gradebook mechanics unproven |
| 12 | Graphs & Network Reasoning | Yes; Show & Tell; Decision Gate | No | None proven | `GREEN — authored/source-complete` | AUTHORED only |
| 13 | Trees, Search & Decision Structures | Yes; Pair Reasoning; Decision Gate | No | None proven | `GREEN — authored/source-complete` | AUTHORED only |
| 14 | Boolean/Circuits/SAT + FSM/model limits | Yes; Show & Tell mini-capstone; Odyssey Checkpoint 3 replaces ordinary Decision Gate | No | None proven | `GREEN — authored/source-complete` | AUTHORED only; two distinct evidence objects must not be accidentally merged or double-counted |
| 15 | Thanksgiving / travel asynchronous buffer and recovery | Yes; explicit asynchronous buffer with no new required topic, meeting, or due date | No | None proven | `GREEN — authored/source-complete` | Compiler must preserve the intentional no-new-obligation semantics |
| 16 | Farkle + Machine Learning synthesis | Yes and separately source-validated; Farkle evidence receipt/rubric and executable support material exist | No | None proven | `GREEN — authored/source-complete` | Special 5% category not wired in current public DSCT compiler |
| 17 | Final individual reflection / course close | Yes; final reflection plus rubric and instructor run-of-show | No | None proven | `GREEN — authored/source-complete` | Final 5% group, date, publication, and student-view behavior unproven |

The source matrix therefore has 16 GREEN weeks and one YELLOW week (Week 2). That does **not** mean the course is deployment-green: Weeks 3–17 stop at AUTHORED in current publicly verifiable compiler truth.

## 3. Assessment and Policy Reconciliation

### Settled and internally coherent in current DSCT source

- `docs/grading-model.md` sums directly to **100%**: eight 5% recurring groups plus 3% technical presentation/demo plus 2% course evaluation, 30% Decision Gates, 15% Reasoning Odyssey checkpoints, 5% Farkle + Machine Learning Synthesis, and 5% final individual reflection.
- The normal technical-evidence rhythm is one ordinary Decision Gate in applicable weeks. Weeks 7, 11, and 14 use Odyssey Checkpoints 1–3 **instead of** an ordinary Decision Gate for that week. Week 16 Farkle + ML is a separate 5% category and is neither a Decision Gate nor an Odyssey checkpoint.
- One regular Decision Gate is dropped after each gate has resolved to the student's retained highest recorded attempt score. Checkpoints, Farkle, Pair Reasoning, Show & Tell, and other categories are not eligible for that drop.
- Revision/resubmission doctrine is settled for evidence-bearing reasoning work: submissions remain revisable while the course system remains open; each attempt is evaluated fresh; the existing shared continuous late-work adjustment applies; and the **highest recorded score** across attempts remains the grade of record. A weaker later attempt cannot lower an already-earned score.
- Pair Reasoning and Show & Tell are separate recurring evidence families. Show & Tell includes the previously separate critique/feedback skill without creating a second 5% feedback category.
- The current course metadata explicitly says **no required textbook and no required external course** for Fall 2026. ZyBooks identifiers and chapter lists are historical provenance only, not an operational requirement.
- Week 15 is a no-new-obligation asynchronous buffer. Week 16 Farkle + ML and Week 17 low-stress individual reflection are canonical source outcomes; there is no current comprehensive programming exam category.

### Deployment conflicts / unknowns

- Current public Course Foundry DSCT output has **no weighted assignment groups** for its Week 1/2 partial slice; `savnac_deploy.py` explicitly documents that partial-weight condition.
- Latest live Canvas evidence in Report 321 says all 13 observed published assignments are in `Semester kickoff week` at 5%, `Assignments` is 0%, and `apply_assignment_group_weights=false`. This is materially inconsistent with the 100% source grading model.
- Exact Canvas/Savnac implementation of highest-attempt retention, ongoing resubmission windows, one dropped regular Decision Gate, exact due dates, and the institutional hard-close date remains unproven.
- Week 2's 40-point Evidence Portfolio is represented in the current W1/2 builder, including a rubric parser, but its correct semester-level category weighting is not established by that builder.
- Current source settles policy; current public compiler and current live gradebook do not yet prove that policy is faithfully implemented.

## 4. Canvas / Compiler Truth Chain

The required truth chain is kept deliberately separate:

`AUTHORED → WIRED → BUILT/EXECUTED → SAVNAC → PRODUCTION`

### AUTHORED

- DSCT repository `main@21881a2...` contains meaningful Week 1–17 source.
- Job 322's older missing-week hypothesis is superseded: Weeks 4–14 and 17 are now authored; Week 15 is intentionally async; Week 9 intentionally has no Thursday package.
- Week 2 is the one source yellow because its instructional package intentionally consumes sibling authoritative material from `local_ai_lab_setup` and `windows_classroom`.

### WIRED

Publicly verifiable current Course Foundry `main@969b50a...` is **only wired for DSCT Weeks 1–2**:

- `course_foundry/dsct_desired_course.py` describes itself as a deterministic Week 1/2 builder.
- `deployment_omissions()` explicitly lists `Weeks 3-17` with the stale reason `semester architecture exists, but no authored deployable instructional package`.
- `course_foundry/savnac_deploy.py::_build_dsct` invokes that builder using the DSCT, local-AI-lab, and Windows sibling roots.

There is also a current public production-path contradiction:

- `course_foundry/production_deploy.py` registers DSCT production course **74035** and invokes `_build_dsct(..., 74035)`.
- The current `dsct_savnac_desired_course()` rejects any `course_id` other than **4**.

Therefore current public Course Foundry `main` cannot be accepted as a working DSCT production builder without a fresh local reproduction and reconciliation of which Course Foundry revision is actually intended. Report 319 described an earlier allowlist fix for `{4, 74035}`; that behavior is not present in the current public file inspected here.

### BUILT / EXECUTED

Historical evidence exists, but it is revision-scoped:

- Report 319 records an earlier production dry-run of **29 create / 0 update / 0 delete** for the W1/2 slice and a subsequent production push.
- Report 321 records fresh DSCT source validation and says an isolated Course Foundry checkout at local SHA `9ca412b...` passed a DSCT adapter validation. That SHA is not currently retrievable from the GitHub repository, so it is evidence about the worker's local checkout, not a reproducible public GitHub anchor.
- No fresh build of current Course Foundry `main@969b50a...` was performed by Piper, and its course-id guard shows that a production build should currently fail before reconcile.

### SAVNAC

- Savnac DSCT course id **4** is encoded in current Course Foundry.
- Report 319 refers to prior Savnac validation as background.
- Newer Report 321 explicitly says **no Savnac target read or dry-run was used** in that preflight.
- Thus no current full-semester Savnac state is proven. Current public code could at most build the W1/2 slice for Savnac 4.

### PRODUCTION

Latest durable read-only evidence says:

- target course: **74035**, `Fall 2026 Discrete Structures (COMSC-2043-1420)`;
- 15 active students and 1 active teacher at the time of Report 321;
- Week 1: 8 items, historically deployed and published;
- Week 2: 7 items, historically partial after the CloudFront/WAF block;
- live shell also contained five unrelated published modules beyond DSCT Week 1/2, 13 published assignments in a conflicting kickoff-only grading topology, and existing submissions on A01–A05;
- no deletes/writes were authorized or performed in Report 321.

**Furthest proven state by slice:**

- Week 1: `PRODUCTION` historically, subject to fresh student-view verification.
- Week 2: `PRODUCTION` **partial**, subject to WAF-content and shared-source verification.
- Weeks 3–17: `AUTHORED`; no current public compiler wiring or live evidence proves a later state.

## 5. Known Production Yellows

1. **Week 2 CloudFront/WAF condition remains materially unresolved.** Report 319 established that 12 intended Week 2 objects failed while a trivial probe page succeeded, strongly suggesting a content-sensitive edge/WAF condition rather than a general Canvas outage. Newer Report 321 still observed only 7 Week 2 items, so there is no evidence the missing 12 were later deployed.
2. **Report 319 is partially superseded by Report 321.** Its Week 1 complete / Week 2 partial facts still line up with newer readback. Its conclusion that the Week 2 yellow was "not blocking today" was a time-local Tuesday judgment; Report 321 later identified larger launch risk from unrelated published content, conflicting grading topology, and existing submissions.
3. **Live production is not a clean target.** Report 321 found 7 published modules and 38 items, with only two DSCT Week modules plus unrelated kickoff/career/advisor/optional surfaces. A reconcile cannot safely decide create/update/delete semantics until the intended fate of those live objects is adjudicated.
4. **Existing student activity raises the rollback/prune risk.** A01–A05 already had submissions in the latest evidence. Any future mutation must preserve student work and must not infer that unrelated-looking objects are disposable.
5. **The live gradebook does not implement the current source model.** The observed 5%-kickoff-only grouping with weighting disabled is not the settled 100% DSCT source grading topology.
6. **Current public Course Foundry has a DSCT production-build contradiction.** This is now a pre-Canvas blocker: the public production registry selects 74035 while the DSCT builder rejects 74035.
7. **Student usability remains unproven beyond object counts.** A later Flo pass must verify module order, published status, assignment visibility, rubrics, dates, files/links, student-view access, duplicate/stale content, and no accidental ZyBooks/paid-resource requirement.

## 6. Stale-Truth Hazards

- **Old missing-week claims:** older planning/report language that Weeks 4–14 or Week 17 are only skeletons is superseded by current source and Job 322.
- **Current Course Foundry W1/2 omission text:** `dsct_desired_course.py` still claims Weeks 3–17 lack authored deployable source. That is now false as a statement about DSCT source and should be treated as evidence that compiler wiring is stale, not evidence that the weeks are absent.
- **Report 319's temporary launch judgment:** "not blocking today" was correct only for the first Tuesday launch moment and should not be reused as semester readiness.
- **Report 321's local Course Foundry SHA:** `9ca412b...` was reported from an isolated local clone but is not currently retrievable from GitHub. Do not substitute it for current public Course Foundry `main` without job-site/local evidence.
- **Historical ZyBooks facts:** `course_metadata.yaml` retains identifiers and chapter provenance, but explicitly marks them historical. A later verifier must not turn these into a required textbook/LTI dependency.
- **Historical Canvas snapshots:** `archive/*` semester snapshots are provenance, not Fall 2026 current truth.
- **Savnac course 4:** it is a sandbox target, not proof of production state and not student-visible production.
- **Canvas object existence:** a module/page/assignment existing in an API inventory does not prove publication, correct ordering, student visibility, working links/files, correct rubric, or correct gradebook behavior.
- **Worker reports:** reports are evidence tied to their inspected SHAs and time. They do not override current project truth when current source/code directly disagrees.

## 7. Recording Verification Contract

### What the DSCT repository currently establishes

No inspected current DSCT source establishes a canonical lecture-capture platform, automatic-recording policy, retention period, or Canvas destination for lecture links. The course is in-person in Stafford 259, so recording readiness must be verified in the actual teaching environment rather than inferred from a personal machine or vendor feature list.

### Current vendor capability evidence

**Microsoft Teams**

- Microsoft documents a meeting option named **Record and transcribe automatically**. An admin meeting policy can allow organizers to use it, but for ordinary meetings the organizer normally still enables the option per meeting; Teams Premium meeting templates can enforce a setting when licensed/configured.
- Teams non-channel meeting recordings are stored in the organizer's **OneDrive for Business**; channel meeting recordings are stored in the channel's **SharePoint** site.
- Recording/transcription permissions, explicit participant consent, and expiration are admin-policy controlled. Microsoft's current settings reference documents automatic expiration as configurable and gives 120 days as the default setting value, subject to tenant policy and retention controls.
- Official references inspected:
  - <https://learn.microsoft.com/en-us/microsoftteams/manage-teams-auto-recording>
  - <https://learn.microsoft.com/en-us/microsoftteams/recording-transcription-overview>
  - <https://support.microsoft.com/en-US/teams/meetings/play-share-and-download-meeting-recordings-in-microsoft-teams>
  - <https://learn.microsoft.com/en-us/microsoftteams/settings-policies-reference>

**Zoom**

- Zoom supports **automatic recording** at meeting start, either to the local computer or, where licensed, to the cloud.
- Audio transcription is a cloud-recording feature and requires an eligible paid account, cloud recording enabled, and audio transcription enabled; account/group enablement can require owner/admin privileges.
- Zoom supports account/group/user auto-deletion of cloud recordings after a configured number of days. Deleted cloud recordings can remain in Trash for 30 days when the recovery setting is enabled.
- Zoom always notifies meeting participants that recording is occurring; client consent/disclaimer behavior is account-type/admin-policy dependent, and guest recording notification remains required.
- Official references inspected:
  - <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067954>
  - <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065911>
  - <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066493>
  - <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0068228>

### Minimum Flo verification checklist

Flo should record evidence, not choose a winner in advance:

- [ ] **Zoom institutional identity/license recognized:** sign in with the actual institutional account on the real intended teaching environment and capture the account/license state needed for recording.
- [ ] **Zoom local 60-second test:** start a test meeting, record locally for approximately 60 seconds, stop, verify playable audio/video/screen-share output and exact local storage path.
- [ ] **Zoom cloud recording availability:** if the institutional account exposes cloud recording, run a bounded cloud test and verify processed recording plus transcript availability; if unavailable, record the exact license/admin blocker.
- [ ] **Zoom automatic recording:** verify whether automatic recording can be enabled for the relevant meeting; distinguish user-controlled setting from admin-locked policy.
- [ ] **Zoom consent/notification:** verify the actual participant notification/consent behavior that students will encounter and record any institutional/legal guidance needed.
- [ ] **Zoom retention:** identify the actual account/group auto-delete setting and whether the instructor can exempt/export recordings before deletion.
- [ ] **Teams institutional identity/license recognized:** sign in with the actual institutional Microsoft account and record the effective meeting/recording entitlement.
- [ ] **Teams 60-second recording test:** run a real test meeting, record and transcribe for approximately 60 seconds, then verify playback and transcript.
- [ ] **Teams storage location:** verify whether the test lands in organizer OneDrive or channel SharePoint and record the exact institutional location/permissions.
- [ ] **Teams automatic recording:** verify whether `Record and transcribe automatically` is available and whether it must be enabled per meeting, can be enforced by a template, or is blocked by policy/license.
- [ ] **Teams consent/retention:** verify effective participant-consent policy and actual recording/transcript expiration/retention policy for the institutional tenant.
- [ ] **Canvas delivery path:** identify one simple, durable student-facing location for lecture links in the DSCT course and test that a student-view user can reach the recording without excess permissions. Do not create it without separate authorization.
- [ ] **Actual classroom repeat:** repeat the selected platform's full 60-second test on the actual Stafford 259 teaching machine/network/audio/display path. A successful office/laptop test is not sufficient.
- [ ] **Failure fallback:** document the manual start-recording fallback and the after-class verification step if automatic recording is unavailable or unreliable.

Recommended operating principle for the later implementation: prefer the institution's native recording/transcription/storage stack over an added third-party recorder bot unless the institution explicitly approves the third party. The operational workflow should include a start-of-class visual verification that recording/transcription is actually active, an after-class check that the asset processed, and a retention/export policy that prevents silent expiration. This report deliberately does **not** choose Zoom or Teams.

## 8. Proposed Flo Scope

### Work that genuinely requires Flo / job-site / credentials / local execution

1. **Resolve the actual Course Foundry checkout truth on Brandy.** Record `git status`, `HEAD`, upstream relationship, and whether the locally reported `9ca412b...` work exists only in a local/dirty/unpushed state. Do not clean or promote it merely to make the report prettier.
2. **Reproduce the current DSCT builder behavior from pinned revisions.** Using exact DSCT/shared-source/Course Foundry SHAs, build the desired course locally and record module/object/group counts plus a deterministic digest. Specifically prove whether production course 74035 currently fails at the DSCT course-id guard.
3. **Verify the Week 2 sibling sources locally.** Confirm the exact `local_ai_lab_setup` and `windows_classroom` source SHAs and all paths consumed by the builder.
4. **Run a bounded Savnac verification if authorized.** Confirm sandbox course 4 identity first; then build/dry-run and, only under separate write authorization, test the full intended package. Record student-view behavior separately from API success.
5. **Fresh production read-only inspection of course 74035.** Recount modules/items/assignments/groups/submissions, verify Week 1 and Week 2 state, identify unrelated content without deleting it, and verify live identity immediately before any future mutation.
6. **Generate a desired-vs-live semantic diff.** Do not choose deletes where student submissions or ambiguous unrelated content exist. Mark those as owner-adjudication items.
7. **Student usability pass.** Test publication, navigation/order, dates, rubrics, submission types, links/files, access permissions, duplicate/stale surfaces, optional-vs-required resources, and Canvas Student View where available.
8. **Recording tests.** Execute the Zoom and Teams checklist above with institutional accounts, then repeat the viable option(s) on the actual Stafford 259 classroom machine/network/audio path.
9. **Preserve evidence.** Return compact receipts with exact SHAs, commands, target IDs, counts, and screenshots/paths where appropriate. No secrets or tokens in receipts.

### Work another Piper can perform without job-site access

- Continue GitHub-only provenance archaeology around Course Foundry branches/commits and identify whether a full-semester DSCT adapter has been pushed under a non-main branch.
- Re-review newly landed DSCT source or policy changes against the Week 1–17 matrix.
- Re-check vendor documentation if Zoom/Teams product behavior or licensing guidance changes.
- Compare future Flo receipts against the source contract and call out any unsupported GREEN claim.

A second Piper is not required **before** the first Flo dispatch: the highest-value unknowns now require local checkout, credentialed Canvas/Savnac, institutional identity/license, and classroom-hardware evidence.

## 9. Owner Decisions Needed

1. **Production live-content adjudication before any reconcile/prune.** Jeremy/Olivia must decide the intended fate of the unrelated published modules/assignments already present in Canvas 74035, especially where student submissions exist. A worker must not infer deletion authority from apparent irrelevance.
2. **Lecture-capture platform and retention/delivery policy, after evidence.** Do not choose Zoom versus Teams from feature lists alone. Once Flo verifies both institutional identities/licenses, classroom reliability, storage, consent, and retention behavior, Jeremy/Olivia can choose the operating platform and the preferred Canvas link-delivery convention if both remain viable.

No owner decision is needed to re-run validators, inventory current code, inspect live state read-only, perform explicitly authorized sandbox tests, or execute the bounded 60-second recording tests.

## 10. Recommendation to Olivia

**READY TO DISPATCH FLO**

- DSCT source truth is now sufficiently mapped: 16 source-GREEN weeks, one Week 2 source yellow, and explicit special-week semantics.
- The most important compiler question is no longer conceptual: current public Course Foundry is visibly stale/partial and internally contradictory for production DSCT, so the actual Brandy checkout and executable behavior must be verified locally.
- The latest production evidence already establishes that course 74035 is not a clean empty target and has student submissions; fresh credentialed read-only inspection and semantic-diff evidence are now the right next move.
- Zoom/Teams capability is feasible on paper but requires institutional-account and actual-classroom-machine tests before any platform choice.
- Flo should verify and report; any compiler repair, Canvas mutation, pruning, platform configuration, or production promotion remains separately authorized work.
