# Prompt 309 — World Bible provenance across CS1, CS2, and DSCT

**Status:** FOREMAN-READY READ-ONLY CROSS-COURSE ARCHAEOLOGY — complete.
**Scope:** read-only evidence gathering only. No World Bible policy is chosen
here. See "Decisions returned to Jeremy + ChatGPT" below.

## 1. DSCT starting commit

- Repository: `discrete_structures_and_critical_thinking`
- Branch used for this work: `worker/prompt309-world-bible` (isolated worktree
  at `/tmp/dsct-prompt309`, created from `origin/main`)
- Starting/base commit: `419b55bf1410670597ebe271138e6bd50577e0f2`

## 2. Repository / ref / commit inventory

| Repo | Path inspected | Branch | Commit SHA |
|---|---|---|---|
| DSCT | `/tmp/dsct-prompt309` (isolated worktree of `discrete_structures_and_critical_thinking`) | `worker/prompt309-world-bible` from `origin/main` | `419b55bf1410670597ebe271138e6bd50577e0f2` |
| CS1 | `/mnt/brandy_nvme/jevert/git/computer_science_1` (read-only, direct) | `main` | `f4fe3c38ebfc7d57bda625bcfa023390a67fe26c` |
| CS2 | `/mnt/brandy_nvme/jevert/git/computer_science_2` (read-only, direct) | `main` | `8f7b498d9738dac9fe4ef9b99549692c17c7ba7a` |

CS1 and CS2 repository names/paths were confirmed directly (both accessible,
both contain course-shaped content — `assignments/`, `rubrics/`, `docs/`);
no name resolution ambiguity arose.

## 3. Search method and exact terms

DSCT (run directly, from `/tmp/dsct-prompt309`):

```sh
grep -rli "world bible" .
grep -rli "living record" .
grep -rli "project record" .
grep -rli "project receipt" .
grep -rli "charter" .
grep -rli "current state" .
grep -rli "known debt" .
grep -rli "what changed" .
grep -n -i "world bible" <candidate files, one per hit above>
find . -iname "*world*bible*"
grep -n -i "bootstrap|transfer student|new student" -r planning docs assignments week-01 week-02
grep -n -i "world" assignments/pair-reasoning-report.md assignments/show-and-tell-artifact.md \
  assignments/career-artifact-sequence.md assignments/week-16-farkle-evidence-receipt.md
```

CS1 and CS2 were each searched by a dedicated read-only sub-agent using the
same required term family plus course-specific extensions, using `rg -ni`
(ripgrep) equivalents of:

```sh
rg -ni "world bible|living record|project record|project receipt|charter|current state|known debt|what changed" .
rg -ni "carry.?forward|carries forward|bring (it|this|your) (from|into)|next course|into cs2|cs2 will|portab"
rg -ni "real.?world|fictional|non-?fiction|real domain"
rg -ni "fresh start|bootstrap|first entry|initialize.*world bible"
rg -ni "append.only|do not overwrite|never delete|preserved as.is|history is preserved"
rg -li "cyoag|choose your own adventure|world bible" archive/
```

DSCT also benefits from a prior read-only archaeology pass, Prompt 305
(`sidecar/reports/305_reasoning_vocabulary_inventory.md`, DSCT commit
`797819e`, superset of the required 309 term list plus Reasoning
Odyssey/Quest/Gate/checkpoint vocabulary). Prompt 305's World Bible findings
are consistent with and cited alongside this report's own direct search
results; Prompt 305 itself explicitly deferred CS1/CS2 archaeology to Prompt
309 (`sidecar/reports/305_reasoning_vocabulary_inventory.md:210-213`).

## 4. Implementation cards

### 4.1 CS1 — `computer_science_1@f4fe3c3`

| Question | Answer | Citation | Label |
|---|---|---|---|
| Student-facing name(s) | "World Bible"; also referred to as the "Judgment Log" when discussing its role in the grading toolkit | `docs/curriculum/judgment_toolkit.md:167` | STUDENT-FACING IMPLEMENTATION / CURRENT DOCTRINE |
| First introduction | Week 2, Step 0 — a one-paragraph "founding charter" explicitly called "the seed of your World Bible"; moved from Week 1 to Week 2 on 2026-07-24 so Week 1 stays universal across sibling courses | `assignments/odyssey_gates/week-02.md:9-25`; `docs/curriculum/judgment_toolkit.md:177-182` | STUDENT-FACING IMPLEMENTATION |
| Required/optional | Required, graded evidence | `assignments/A2-coding-odyssey-project.md:38-39` ("Keep your World Bible current every week... It's graded evidence, not optional bookkeeping.") | STUDENT-FACING IMPLEMENTATION |
| Artifact shape/location | A section (`## The World Bible`) inside the home-base assignment file, described as "a living document"; no separate file format/repo location is prescribed — student keeps it themselves; no dedicated template file exists in `templates/` | `assignments/A2-coding-odyssey-project.md:95-108` | STUDENT-FACING IMPLEMENTATION |
| Fields/prompts requested | "Your founding charter (from Week 2)"; "Current state of the world"; "One line per week: what gate you passed, what broke"; "A running 'known debt' list" | `assignments/A2-coding-odyssey-project.md:97-102` | STUDENT-FACING IMPLEMENTATION |
| World types offered | Four bounded genres: Frontier Settlement, Investigation Bureau, Starship Log, Small Business — bounded "so genre-based peer grouping and grading stay tractable" | `assignments/A2-coding-odyssey-project.md:43-50` | STUDENT-FACING IMPLEMENTATION |
| Fiction vs. real-domain flexibility | None found; all four genres are fictional/simulated framings, no "model your real project" option | absence confirmed by search | ASPIRATIONAL/NOT IMPLEMENTED (i.e., not offered) |
| Update cadence | Weekly, tied to gate weeks: "one line per week: what gate you passed, what broke" | `assignments/A2-coding-odyssey-project.md:101`; `assignments/odyssey_gates/week-02.md:86-90` | STUDENT-FACING IMPLEMENTATION |
| Relationship to weekly gates | Tightly wired; every `assignments/odyssey_gates/week-NN.md` ends with a World Bible reminder; named as the "Judgment Log" instrument in the five-instrument grading toolkit | `docs/curriculum/judgment_toolkit.md` (instrument table, line 31) | STUDENT-FACING IMPLEMENTATION / CURRENT DOCTRINE |
| Grading relationship | Reviewed at three checkpoints (Week 2 existence-only, mid-semester, Week 17 full rubric); no independent point weight — folded into "Reasoning Odyssey checkpoints 15%" and weekly reinforcement pools | `rubrics/odyssey_gates/week-02_rubric.md:6-12`; `rubrics/odyssey_gates/week-17_rubric.md:15-24`; `docs/grading-model.md`; `assignments/A2-coding-odyssey-project.md:139-141` | STUDENT-FACING IMPLEMENTATION |
| Relationship to Pair/Show/social work | Not directly wired to `A3-pair-programming.md`; wired to Week 17 final Debrief and Week 14 "Full Trail Debrief" show-and-tell tie-in | `rubrics/odyssey_gates/week-17_rubric.md:39-41`; `docs/curriculum/judgment_toolkit.md:151-152` | STUDENT-FACING IMPLEMENTATION |
| AI/tool-use evidence expectations | Light-touch, only at Week 17: the Log doubles as the student's own AI-practice "Routine" evidence | `docs/curriculum/judgment_toolkit.md:186-189`; `assignments/odyssey_gates/week-17.md:31-33` | STUDENT-FACING IMPLEMENTATION |
| History preserved vs. overwritten | Append-only by design; backfilling flagged as a scored defect at Week 17 | `rubrics/odyssey_gates/week-17_rubric.md:20-21,34-37` | STUDENT-FACING IMPLEMENTATION |
| Portability/carry-forward language | **NONE FOUND.** Explicit `carry.?forward` etc. search returned only one unrelated hit about pedagogy ("tutor-not-typist ethos carries forward," `docs/course-ethos.md:162`), not the artifact | absence confirmed by search | **NO CARRY-FORWARD EVIDENCE FOUND** |
| Bootstrap path | N/A as a "returning student" case — CS1 is first in sequence; World Bible starts fresh in Week 2 by design; no "if you already have one" branch exists anywhere | `assignments/odyssey_gates/week-02.md:9-25` | STUDENT-FACING IMPLEMENTATION (fresh-start only) |
| Contradictions found | (a) Week 17 Debrief prompt references a "Week 1 founding charter" though the charter is a Week 2 deliverable — a stale, uncorrected reference after the documented Week 1→2 move; (b) the unrelated dev/planning file `ROADMAP.md` is separately described as "a living record," a false-positive-prone grep collision with the student artifact, not the same thing | `assignments/odyssey_gates/week-17.md:16` vs. `assignments/odyssey_gates/week-02.md:9-25` and `docs/curriculum/judgment_toolkit.md:177-182`; `START_HERE.md:21-22`, `ROADMAP.md:3-8` | AMBIGUOUS (minor, uncorrected residue) |

### 4.2 CS2 — `computer_science_2@8f7b498`

**Critical disambiguation:** CS2's repository contains two unrelated things
both called "World Bible." `sidecar/worlds/README.md:120-133` explicitly
warns: "World Bible vs. the student's World Bible — do not confuse these."

1. **"The Four Living Worlds Bible"** (`sidecar/worlds/` — `capability_map.md`,
   `continuity_ledger.md`, four world-lore files, `four_calls/`, `four_faces/`,
   `transfer_portal/`) — an internal authoring canon for course-builders, not
   student-facing. `sidecar/worlds/README.md:3-13`: "Not student-facing...
   Never hand a student this directory." This is INTERNAL SCAFFOLDING, not
   the artifact DSCT should model.
2. **The student's own World Bible** — defined once, canonically, in
   `assignments/A2-coding-odyssey-project.md`. This is what the table below
   describes.

| Question | Answer | Citation | Label |
|---|---|---|---|
| Student-facing name(s) | "World Bible," consistently, no variant | `assignments/A2-coding-odyssey-project.md:34` (verified directly: `## World Bible` heading) | STUDENT-FACING IMPLEMENTATION |
| First introduction | Assignment text (A2) plus orientation deck frame "The World Bible Remembers," onboarding beat 3 of 5 | `assignments/A2-coding-odyssey-project.md`; `presentations/beamer/orientation/welcome-to-the-odyssey.tex:41,88-96` | STUDENT-FACING IMPLEMENTATION |
| Required/optional | Required, woven into every weekly gate submission (Weeks 2-14); rubric-scored, not standalone | every `assignments/odyssey_gates/week-NN.md`; `rubrics/odyssey_gates/week-03_rubric.md`, `week-14_rubric.md` | STUDENT-FACING IMPLEMENTATION |
| Artifact shape/location | Student-maintained file/section inside the student's own project; no LMS object, no shipped template (`templates/` has no World Bible template) | `assignments/A2-coding-odyssey-project.md:36` (verified directly: "Keep a short living project record...") | STUDENT-FACING IMPLEMENTATION for concept; format unspecified |
| Fields/prompts requested | "charter, current state, one line per week saying what changed/broke, known debt, tests/evidence, and important design choices. It is a project receipt, not duplicate homework." | `assignments/A2-coding-odyssey-project.md:36-38` (verified directly) | STUDENT-FACING IMPLEMENTATION |
| World types offered | Same four fixed genres as CS1: Frontier Settlement, Investigation Bureau, Starship Log, Small Business | `assignments/A2-coding-odyssey-project.md:5-8` (verified directly) | STUDENT-FACING IMPLEMENTATION |
| Fiction vs. real-domain flexibility | Not offered as a binary choice; all four options are fictional-but-domain-grounded; no literal own-real-project substitute found | absence confirmed by search | ASPIRATIONAL/NOT IMPLEMENTED (not offered) |
| Update cadence | "one line per week saying what changed/broke" — content-gated, not ceremonial; every active gate file (Weeks 2-14) repeats "Keep one concise World Bible entry: what changed, evidence used, and any remaining debt" | `assignments/A2-coding-odyssey-project.md:37`; `docs/grading-model.md:57-66` | STUDENT-FACING IMPLEMENTATION |
| Relationship to weekly gates | Tightly wired: codified as evidence-pattern item #4 of 4 for every weekly gate | `docs/grading-model.md:57-66` | STUDENT-FACING IMPLEMENTATION / CURRENT DOCTRINE (doctrine and implementation match verbatim) |
| Grading relationship | Folded into each gate's rubric as one scored dimension (never its own category): e.g. Week 3 "boundary reasoning and World Bible 6" of 25; Week 14 "AI review/accountability and World Bible 10" of 60 | `rubrics/odyssey_gates/week-03_rubric.md`; `week-14_rubric.md` | STUDENT-FACING IMPLEMENTATION |
| Relationship to Pair/Show/social work | None found; A3 (Pair) and A4/A7 (Show & Tell) are separate 5%-weighted categories with no World Bible cross-reference | absence confirmed by search of `docs/grading-model.md` | NOT PRESENT |
| AI/tool-use evidence expectations | Bundled directly: gate evidence item 4 is "World Bible entry plus AI proposal/diff/test/read/reason/accept-or-reject evidence when AI helped"; rubrics score "AI accountability" adjacent to the World Bible line | `docs/grading-model.md:65-66`; `docs/curriculum/judgment_toolkit.md` | STUDENT-FACING IMPLEMENTATION |
| History preserved vs. overwritten | Append-only, explicit for the intra-course Transfer Portal case: "their prior World Bible history is preserved as-is (old entries are never rewritten...)"; base weekly-log framing implies append-only by design though not stated in those exact words in A2 | `sidecar/worlds/transfer_portal/README.md:132-134` | STUDENT-FACING IMPLEMENTATION (transfer case) / CURRENT DOCTRINE (general case — no populated student example exists to confirm in practice) |
| Portability/carry-forward language | **NONE FOUND** in either direction. Explicit non-carry-forward for the underlying codebase: "a fresh CS2-native codebase/world, inspired by prior experience but not a continuation of CS1 code" (verified directly). The only portability mechanism implemented is *intra-course* world-to-world Transfer Portal, not cross-course | `assignments/A2-coding-odyssey-project.md:5-7` (verified directly); `sidecar/worlds/transfer_portal/README.md` | **NO CARRY-FORWARD EVIDENCE FOUND** (codebase explicitly does not carry forward; document/artifact carry-forward is simply never addressed) |
| Bootstrap path | No dedicated "how to start your World Bible" instructions found (checked `START_HERE.md`, `README.md`, `week-02.md`, orientation deck); Week 2's ungraded "light world seed" gate is the de facto first-entry moment but reuses the generic weekly-entry boilerplate even though nothing has changed yet | absence confirmed by search | ASPIRATIONAL/NOT IMPLEMENTED (gap, not contradiction) |
| Contradictions found | None substantive between doctrine (`docs/grading-model.md`, `judgment_toolkit.md`) and student-facing text — the six-field formula is reproduced near-verbatim across A2, gate files, and the orientation deck. One naming-collision risk flagged: the internal "Four Living Worlds Bible" (`sidecar/worlds/`) shares the exact term and could be mis-cited as the student implementation by a loose grep; the repo itself anticipated and guarded against this | `sidecar/worlds/README.md:120-133` | AMBIGUOUS (naming collision, guarded against in-repo) |

### 4.3 DSCT — `discrete_structures_and_critical_thinking@419b55b`

| Question | Answer | Citation | Label |
|---|---|---|---|
| Student-facing name(s) | "World Bible" used consistently where mentioned at all | `week-02/student/week-02-evidence-assignment.md:44`; `docs/career-connection.md:55`; `week-02/README.md:57` | STUDENT-FACING IMPLEMENTATION (mentions only — see below) / CURRENT DOCTRINE |
| First introduction | **No dedicated introduction exists.** `week-01/README.md` names the course "Reasoning Odyssey" but never mentions World Bible; no `assignments/reasoning_odyssey_gates/` directory was ever built (an early prompt, 011, called for building one — not found at current HEAD) | `week-01/README.md:1-40` (verified directly, no World Bible reference); `prompts/011_reasoning_odyssey_kickoff_and_week2_proof_slice.md:60-61` ("No `World Bible` or `Reasoning Odyssey` concept exists anywhere in this repo yet. You are building it...") | ASPIRATIONAL/NOT IMPLEMENTED |
| Required/optional | **Explicitly optional and explicitly not graded**, at the only point it is mentioned in current student-facing text | `week-02/student/week-02-evidence-assignment.md:44-45`: "Optional World Bible notes may carry a student context forward, but they are not required and are not graded in Week 2."; `week-02/README.md:56-58`; `reports/303_week2_instructional_package.md:50-53` | STUDENT-FACING IMPLEMENTATION (of non-requirement) |
| Artifact shape/location | **No canonical filename, template, or submission shape found anywhere.** No file matching `*world*bible*` exists in the repo other than the prompt files for 305/309 themselves | `find . -iname "*world*bible*"` returned only `sidecar/prompts/305_...md` and `sidecar/prompts/309_...md` | ASPIRATIONAL/NOT IMPLEMENTED |
| Fields/prompts requested | None specified anywhere in current student-facing or planning source; the raw design quarry proposes a rich future field set (claims, definitions, assumptions, examples/counterexamples, sources, evidence, uncertainty, confidence, what changed the student's mind, preserve/revise/reject vocabulary) but this is explicitly unresolved design language, not an implemented contract | `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:153-252`; `sidecar/raw/2026-08-17_dsct_design_decision_pile.md:197-246` | ASPIRATIONAL/NOT IMPLEMENTED |
| World types offered | None offered to DSCT students; `planning/fall-2026-weekly-architecture.md:41-45` speaks generically of "a chosen world, system, organization, scenario, or problem space" without naming fixed genres the way CS1/CS2 do | `planning/fall-2026-weekly-architecture.md:41-45` | CURRENT DOCTRINE (planning language only) |
| Fiction vs. real-domain flexibility | Explicitly **more open** than CS1/CS2 in doctrine: "This does not need to be fictional — a real system/domain the student is interested in modeling logically is equally valid" | `prompts/011_reasoning_odyssey_kickoff_and_week2_proof_slice.md:63-66` | ASPIRATIONAL/CURRENT DOCTRINE (never reached a built assignment file to become implementation) |
| Update cadence | None stated; no cadence instruction of any kind was found (searched for "maintain/keep/update... world bible") | absence confirmed by search | ASPIRATIONAL/NOT IMPLEMENTED |
| Relationship to weekly gates/checkpoints | Doctrine describes intended chassis slots (Tuesday reasoning-challenge/exit-check; Thursday Pair Reasoning/Show & Tell artifact) as "natural continuity handoffs," explicitly "uses of existing slots, not new meetings, assignments, or time allocations" — but no actual weekly file implements this handoff yet | `planning/fall-2026-weekly-architecture.md:51-58` | CURRENT DOCTRINE, not yet STUDENT-FACING IMPLEMENTATION |
| Grading relationship | **None.** `docs/grading-model.md` contains zero mentions of "World Bible" across its full category table; Week 2 and the career-artifact-sequence assignment both explicitly disclaim a separate grade for it | `docs/grading-model.md` (grep returned no hits); `week-02/student/week-02-evidence-assignment.md:44-45`; `reports/303_week2_instructional_package.md:50-53` | STUDENT-FACING IMPLEMENTATION (of "not graded") |
| Relationship to Pair/Show/social work | None implemented; no mention of World Bible found in `assignments/pair-reasoning-report.md` or `assignments/show-and-tell-artifact.md` | absence confirmed by direct grep of both files | NOT PRESENT |
| AI/tool-use evidence expectations | None tied specifically to World Bible; the course-wide "Love AI more. Trust AI less." stance applies generally but has no World-Bible-specific binding | `week-01/README.md:33-36` (general AI stance, not World-Bible-specific) | NOT PRESENT (as a World-Bible-specific link) |
| History preserved vs. overwritten | Undetermined — no artifact exists yet to preserve or overwrite | n/a | ASPIRATIONAL/NOT IMPLEMENTED |
| Portability/carry-forward language | One phrase, "may carry a student context forward," appears in Week 2 evidence assignment, but this is presented alongside "not required and are not graded" and does not specify from where (a prior DSCT week? a prior course?) or to where; the raw design quarry (not DSCT student-facing source) explicitly poses cross-course literal-carry-forward as an open question, not a decision | `week-02/student/week-02-evidence-assignment.md:44`; `sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:203-215` ("Open design question: should a student literally carry the same World Bible from CS1 into CS2 and DSCT...") | **FAMILY RESEMBLANCE / NO LITERAL CARRY-FORWARD EVIDENCE FOUND** |
| Bootstrap path | None found; no transfer/new-student instructions exist anywhere in DSCT source | absence confirmed by search (`bootstrap\|transfer student\|new student` across planning/docs/assignments/week-01/week-02) | ASPIRATIONAL/NOT IMPLEMENTED |
| Contradictions found | (a) `week-02/README.md` explicitly states the Week 2 Evidence Portfolio "is recurring weekly course work, not a Reasoning Odyssey write-up," yet `docs/grading-model.md`'s weekly-reinforcement row states "Week 2's local-AI-lab/Container-Connections evidence portfolio also lands here as the week's readiness/setup entry" (i.e., inside the Odyssey-gate 30% category) — a labeling tension already flagged independently by Prompt 305 as a `GRADEBOOK-SEAM`/`DUPLICATE-HOMEWORK RISK`; (b) `planning/fall-2026-weekly-architecture.md` (current chassis contract) has zero direct Odyssey/World-Bible wiring into actual Tuesday/Thursday files despite Prompt 013 having been dispatched specifically to add that wiring — the reconciliation intent exists in doctrine/prompt form but was not confirmed as landed in the inspected week-level files | `week-02/README.md:56-58` vs. `docs/grading-model.md` weekly-reinforcement row; `sidecar/reports/305_reasoning_vocabulary_inventory.md` (Week 2 Evidence Portfolio row); `prompts/013_reasoning_odyssey_fabric_reconciliation.md:46-49` | AMBIGUOUS |

Additional DSCT-specific evidence:
- No `rubrics/` directory exists in DSCT at all (`sidecar/runs/305_foreman_acceptance.md:23`, confirmed here: `ls rubrics/` → not present).
- The Fall 2026 Canvas snapshot in `archive/spring-2026/canvas-71253-snapshot-20260714-195606.json` contains zero World Bible hits — corroborating that no World Bible object has ever existed as a live Canvas gradebook item in DSCT.
- Prompt 011 (dated prior to current HEAD's content) explicitly documents the starting condition: "No `World Bible` or `Reasoning Odyssey` concept exists anywhere in this repo yet." Subsequent work added scattered doctrine mentions but never built a dedicated assignment/template/gate file for it.

## 5. Doctrine-vs-implementation findings (summary)

| Course | World Bible status |
|---|---|
| CS1 | STUDENT-FACING IMPLEMENTATION, fully built: named assignment section, weekly cadence instruction, rubric-scored at 3 checkpoints, append-only enforcement at Week 17. Doctrine (`judgment_toolkit.md`) and implementation are tightly reconciled (explicit dated reconciliation passes: 2026-07-24, 2026-07-27, 2026-08-12), with one minor uncorrected stale reference (Week 1 vs. Week 2 charter). |
| CS2 | STUDENT-FACING IMPLEMENTATION, fully built: named assignment section (`A2`), weekly cadence instruction, rubric-scored inside every gate (Weeks 2-14), explicit append-only policy for intra-course world transfer. Doctrine and implementation match near-verbatim. A separate, non-student-facing "Four Living Worlds Bible" internal-authoring artifact exists under the same name and must not be conflated with the student artifact — the repo itself warns against this. |
| DSCT | **ASPIRATIONAL / NOT IMPLEMENTED**, with a handful of thin, consistent, non-contradictory doctrine mentions. No dedicated assignment, template, rubric, cadence instruction, or gate wiring exists. The only student-facing statements about it explicitly say it is optional and ungraded. The richer "reasoning history" progression (claims, assumptions, evidence, confidence, what changed the student's mind) exists solely in the raw design quarry (`sidecar/raw/2026-08-16_...md`, `sidecar/raw/2026-08-17_...md`), which is explicitly pre-decisional planning material, not course source. |

## 6. Cross-course comparison matrix

| Dimension | CS1 | CS2 | DSCT |
|---|---|---|---|
| Purpose | Ownership/identity: what's my world, what did I build, what broke | Design/engineering judgment: charter, current state, debt, tests/evidence, design choices | Proposed (not built): reasoning history — claims, evidence, confidence, revision |
| Artifact shape | Section inside `assignments/A2-coding-odyssey-project.md`; student-maintained, no fixed file format | Same pattern: section inside `assignments/A2-coding-odyssey-project.md`; student-maintained, no fixed file format | No artifact exists; only passing mentions in Week 2 and career-connection docs |
| Personalization mechanism | Choice of 1 of 4 fixed fictional-but-domain-grounded genres | Same 4 fixed genres, same framing | Undoctrine'd/open: "a chosen world, system, organization, scenario, or problem space," explicitly may be non-fictional |
| Persistence/history | Append-only; backfilling penalized at Week 17 rubric | Append-only, explicit for intra-course Transfer Portal case | N/A — no artifact to persist |
| Evidence fields | Charter, current state, weekly one-liner, known-debt list | Charter, current state, weekly one-liner, known debt, tests/evidence, design choices | None specified (proposal only, in raw quarry: claims/assumptions/evidence/confidence/what changed mind) |
| Engineering/reasoning depth | Ownership-level (what exists, what broke) | Engineering-level (design decisions, debt, contracts implicitly via course content) | Proposed reasoning-level (claims, counterexamples, confidence) — not built |
| Update cadence | Weekly, one line per gate week | Weekly, one line per gate week, explicitly change-gated ("what changed/broke") | None stated |
| Grading connection | Folded into gate/checkpoint pools; reviewed at Week 2/mid/Week 17, no independent weight | Folded into every gate rubric as a scored sub-line (e.g., 6/25, 10/60) | None; explicitly disclaimed as ungraded where mentioned |
| Bootstrap path | Fresh-start only (CS1 is first in sequence); no "prior artifact" case exists | No dedicated bootstrap instructions found; Week 2 light seed reuses generic weekly boilerplate | None found anywhere |
| Carry-forward language | None found | None found (codebase explicitly does NOT carry forward from CS1; document carry-forward simply unaddressed) | One ambiguous phrase ("may carry a student context forward") with unspecified source/direction; raw quarry poses cross-course carry-forward as an open question |
| Anti-bureaucracy posture | Strong: "not optional bookkeeping" is paired with "one line per week," light 6-10pt scoring inside larger rubrics, honest-incompleteness explicitly not punished | Strong: "It is a project receipt, not duplicate homework" (verbatim in A2); orientation deck explicitly disclaims "decorative lore... busywork... a second homework track" | Doctrine-only: raw quarry states the same anti-bureaucracy principle ("must not become compulsory fiction or ceremonial weekly journaling") but there's no built artifact yet for the principle to apply to |
| Relationship to Odyssey/gate structure | Explicitly named as one of five instruments in the "Judgment Toolkit," tightly wired into every weekly gate file | Explicitly one of four evidence-pattern items required in every weekly gate | Proposed only: doctrine says existing Tuesday/Thursday chassis slots would be the natural home, but no week-level file currently implements this wiring |

## 7. Observed commonalities

Mechanics/purposes that actually recur across two or more course sources
(CS1 and CS2 both have built implementations; DSCT is doctrine-only, so DSCT
entries below are marked as doctrine, not implementation):

1. **Same student-facing name.** "World Bible" is used identically in CS1
   and CS2 assignment text, and is the only name DSCT doctrine uses too.
2. **Same four world genres.** CS1 and CS2 both offer exactly Frontier
   Settlement, Investigation Bureau, Starship Log, Small Business — identical
   list, identical fictional-but-domain-grounded framing. (DSCT doctrine
   explicitly does not fix a genre list and is more open than either.)
3. **Weekly, content-gated update cadence.** Both CS1 and CS2 use "one line
   per week" tied to "what changed/broke" rather than a fixed-length
   ceremonial entry. (DSCT doctrine states no cadence at all yet.)
4. **Folded into existing gate rubrics, not a standalone grade category.**
   Both CS1 and CS2 score the World Bible as a sub-line inside weekly/
   checkpoint rubrics rather than a separate gradebook object. (DSCT
   explicitly disclaims any grade for it where it is mentioned at all —
   consistent in spirit, though for a different reason: nothing exists to
   grade.)
5. **Explicit anti-bureaucracy framing in doctrine and/or student text.**
   CS1 ("graded evidence, not optional bookkeeping" — paired with a
   one-line cadence to keep it light), CS2 ("a project receipt, not
   duplicate homework," verbatim in the student-facing assignment), and the
   DSCT raw design quarry (an explicit design principle: "must not become
   compulsory fiction or ceremonial weekly journaling") all converge on the
   same anti-ceremony posture, even though only CS1/CS2 have shipped an
   artifact for the posture to govern.
6. **No literal cross-course carry-forward implemented anywhere.** Neither
   CS1 nor CS2 has any student-facing or doctrine text saying a World Bible
   document itself moves from one course's repository/submission into
   another's. DSCT has one ambiguous, unelaborated phrase gesturing at
   carrying "a student context forward" with no specified source course.
7. **Append-only / preserve-history intent.** CS1 explicitly penalizes
   backfilling (evidence of not having kept it current); CS2 explicitly
   preserves prior entries verbatim in the one carry-forward mechanism it
   does implement (intra-course Transfer Portal). Both converge on
   "preserve the historical record, don't rewrite it," matching the raw
   quarry's stated principle for a future DSCT design ("preserve earlier
   judgments rather than rewriting history").

## 8. Course-specific divergences

1. **DSCT has no implementation at all**, while CS1 and CS2 both have fully
   built, rubric-scored, gate-wired artifacts. This is the largest
   divergence and the reason Prompt 309 exists.
2. **DSCT doctrine explicitly allows non-fictional framing**
   ("a real system/domain the student is interested in modeling logically
   is equally valid," `prompts/011...md:63-66`) where CS1 and CS2 both
   restrict students to exactly four fictional-but-domain-grounded genres
   with no real-domain substitute offered anywhere.
3. **CS2 has an internal, non-student-facing "Four Living Worlds Bible"**
   authoring-canon artifact (`sidecar/worlds/`) that shares the exact same
   name as the student artifact but is a completely different thing — CS1
   has no equivalent internal-canon directory, and DSCT has neither.
4. **CS2's World Bible is explicitly bundled with AI-accountability evidence**
   in the same gate-evidence bullet (`docs/grading-model.md:65-66`); CS1
   ties AI-practice evidence to the Log only lightly, at Week 17 only; DSCT
   has no World-Bible-specific AI evidence binding (though it has a general,
   course-wide AI stance).
5. **CS2 has an explicit intra-course world-transfer mechanism**
   (Transfer Portal, letting a student switch worlds mid-course while
   preserving history); CS1 has no equivalent world-switch mechanism
   documented; DSCT has neither, and doesn't yet have worlds to switch
   between.
6. **CS1's charter is a fixed one-time Week-2 event**, reviewed for
   existence only at Week 2 and then for evolution at Week 17; CS2's charter
   is part of the same six-field bundle reviewed at every gate from Week 3
   onward, a more continuously-scored cadence than CS1's checkpoint-only
   model.

## 9. Carry-forward evidence matrix

| Course | Literal same-artifact carry-forward implemented? | Optional reuse/import language? | Thematic continuity only? | No carry-forward language found? | Hidden prior-course assumption? | Explicit fresh-start/bootstrap support? |
|---|---|---|---|---|---|---|
| CS1 | No | No | No — no reference to any other course at all | **Yes — no carry-forward language found in CS1** | No | Implicit only (CS1 is first in sequence; Week 2 charter always starts fresh; no explicit bootstrap doc but no bootstrap need exists either) |
| CS2 | No | No (only intra-course world-transfer, not cross-course) | No — one explicit *non*-continuity statement re: codebase ("not a continuation of CS1 code") | **Yes — no carry-forward language found in CS2** (for either CS1→CS2 or CS2→next-course direction) | No | No dedicated bootstrap doc found; Week 2 light-seed gate serves this role informally |
| DSCT | No | One ambiguous phrase, unspecified source/direction, explicitly not required/graded | Possibly — doctrine gestures at "a chosen world... can become the context," open-ended | Partially — the phrase exists but doesn't constitute real carry-forward evidence | No | None found anywhere |

**Overall finding: no source in any of the three repositories implements
literal same-artifact carry-forward across courses.** The strongest
cross-course claim available is the raw DSCT design quarry's own framing:
"preserve the same recognizable artifact family... allow students to carry a
prior world forward when it remains useful... do not make prior enrollment a
hidden prerequisite" (`sidecar/raw/2026-08-16_dsct_reasoning_course_design_dump.md:203-217`)
— but this is explicitly labeled in its own source as a "strong
recommendation for later discussion," i.e., pre-decisional, not implemented
policy in any repository.

Per the required labeling convention: **any claim of CS1→CS2→DSCT World
Bible continuity beyond a shared name, a shared four-genre convention (CS1/
CS2 only), and a shared anti-bureaucracy posture is FAMILY RESEMBLANCE / NO
LITERAL CARRY-FORWARD EVIDENCE FOUND.**

## 10. Bootstrap/transfer-student evidence

- **CS1:** No explicit bootstrap doc; not needed at current HEAD since CS1 is
  the first course and every student starts the World Bible fresh at Week 2
  by design.
- **CS2:** No explicit "how to start your World Bible" doc found, despite
  CS2 being downstream of CS1 in the sequence, which is exactly where a
  bootstrap/import decision would matter most. The Week 2 "light world seed"
  gate is the closest thing to a bootstrap moment, but it reuses generic
  weekly-entry boilerplate ("what changed, evidence used, remaining debt")
  even though, at a true first entry, nothing has changed yet — a minor
  content mismatch, not a contradiction.
- **DSCT:** No bootstrap or transfer-student language found anywhere in the
  repository. This matters directly for Jeremy + ChatGPT's decision: if DSCT
  chooses any carry-forward posture, CS2's own gap (no working bootstrap
  pattern despite being downstream of CS1) is a preexisting problem DSCT
  would inherit, not a solved pattern DSCT could just copy.

## 11. Anti-bureaucracy findings

Concrete evidence for the "record meaningful change, not empty ceremony"
principle, per course:

- **CS1 (present, implemented):** "Keep your World Bible current every
  week... It's graded evidence, not optional bookkeeping" is paired with a
  literal one-line-per-week format (`A2-coding-odyssey-project.md:97-102`).
  Grading explicitly forgives unresolved debt if honestly reported rather
  than penalizing incompleteness (`week-17_rubric.md:27-30`, "the point is
  an honest record of judgment over the semester, not a spotless project").
  Slight tension noted: the Week 17 rubric does treat *evidence of skipping
  weeks* (backfilling) as a defect, which is a real enforcement mechanism
  pushing toward "you must actually touch this every week," not purely
  "only when something changed."
- **CS2 (present, implemented, strongest language of the three):**
  Verbatim in the student-facing assignment: "It is a project receipt, not
  duplicate homework" (`A2-coding-odyssey-project.md:38`). Orientation deck:
  "Not decorative lore. Not busywork. Not a second homework track."
  (`welcome-to-the-odyssey.tex:92`). Doctrine: "a living World Bible to make
  student judgment visible without creating duplicate homework"
  (`docs/curriculum/judgment_toolkit.md:3-4`). Transfer Portal instructions
  explicitly warn against overbuilding: "a few minutes, not a review board...
  Don't build policy theater for an edge case."
  (`sidecar/worlds/transfer_portal/README.md`). Grading integration keeps
  weight small (never more than 6-10 of 25-60 points per gate).
- **DSCT (doctrine only, not yet tested against a built artifact):** The
  raw design quarry states the same principle explicitly — "must not become
  compulsory fiction or ceremonial weekly journaling," and "a topic must
  stand on its own when forcing the carried world would be artificial"
  (`sidecar/raw/2026-08-17_dsct_design_decision_pile.md:246-248`). The one
  built student-facing DSCT statement consistent with this ("optional...
  not required and are not graded in Week 2") is the closest thing to
  implemented anti-bureaucracy evidence DSCT currently has — but it reads
  more like "we haven't built it yet" than "we deliberately made it
  lightweight," since no cadence or field set exists yet to be lightweight
  about.

No mandatory-weekly-entry-regardless-of-substance requirement was found in
any of the three repositories.

## 12. Contradictions / uncertainties

- **CS1:** Week 17 Debrief file references a "Week 1 founding charter" that
  is actually a Week 2 deliverable — an uncorrected stale reference after a
  documented Week 1→2 move. Minor.
- **CS1:** `ROADMAP.md` (an unrelated instructor/dev planning file) reuses
  "living record" language, creating a false-positive-prone grep collision
  for anyone doing this kind of archaeology later. Flagged for future
  workers, not a real inconsistency in the student artifact itself.
- **CS2:** The internal "Four Living Worlds Bible" (`sidecar/worlds/`)
  shares the literal name "World Bible" with the student artifact; the repo
  guards against this confusion explicitly, but a careless read of CS2 could
  easily overstate CS2's World Bible complexity by citing the internal canon
  instead of the six-field student version. This report used only the
  student-facing artifact (`assignments/A2-coding-odyssey-project.md`) as
  authority for the CS2 implementation card.
- **DSCT:** `week-02/README.md` calls the Week 2 Evidence Portfolio "not a
  Reasoning Odyssey write-up," while `docs/grading-model.md` places that
  same portfolio inside the 30% weekly-reinforcement/Odyssey-gate category
  — a labeling tension independently flagged by Prompt 305 as a
  `GRADEBOOK-SEAM`/`DUPLICATE-HOMEWORK RISK`. Not resolved here; carried
  forward as an open item.
- **DSCT:** Prompt 013 was dispatched specifically to wire Odyssey/World
  Bible continuity into `fall-2026-weekly-architecture.md`, and that file
  does now contain a "Reasoning Odyssey continuity and grading map" section
  — but no actual week-level (Week 3-14) file was found implementing that
  wiring at current HEAD. Weeks 3-17 remain `CONTRACTED_NOT_AUTHORED` per
  Prompt 013's own scope note (`prompts/013...md:54`), so this is an honest
  gap, not a broken promise — the doctrine layer is ahead of the
  not-yet-authored content layer by design.
- **General:** the DSCT raw design quarry's "CS1/CS2 progression" language
  (ownership → design/engineering → reasoning history) is itself a proposal
  written *by/for DSCT planning*, not a description sourced from the CS1/CS2
  repositories. The actual CS1/CS2 implementation cards in this report (built
  independently, from the CS1/CS2 repos themselves) substantially confirm the
  *ownership* framing for CS1 and a *design/engineering* framing for CS2 in
  spirit, but the CS1/CS2 repos do not use the quarry's specific proposed
  vocabulary (e.g., CS1 doesn't literally ask "what am I proud of?"; CS2
  doesn't literally use the words "interfaces/contracts" or "accepted/
  rejected proposals" inside the World Bible field list — those exact terms
  were not found in either repo's World Bible section). Treat the quarry's
  progression as a reasonable summary of the *shape*, not a literal quotation
  of either course's actual field list.

## 13. Decisions returned to Jeremy + ChatGPT

This report deliberately does not choose:

1. Whether DSCT's World Bible is a literal cross-course carry-forward
   artifact or a fresh DSCT-native artifact with an optional import path —
   no repository currently implements literal carry-forward, so either
   choice starts from the same (empty) baseline.
2. Whether the DSCT student-facing name stays exactly `World Bible`.
3. DSCT's actual field list — the raw quarry's reasoning-history proposal
   (claims, assumptions, evidence, confidence, what changed the student's
   mind, preserve/revise/reject vocabulary) is unimplemented anywhere and
   remains a proposal, not evidence of a working pattern.
4. DSCT's update cadence — CS1 and CS2 both converge on "one line per week,
   content-gated," which is evidence worth weighing, but DSCT has not
   adopted or rejected it.
5. Whether DSCT offers fixed genres (CS1/CS2 pattern) or open real-domain
   framing (DSCT's own existing, more permissive doctrine language).
6. Whether the World Bible is graded, and if so, whether it follows CS1's
   checkpoint-review model or CS2's every-gate-scored model.
7. How DSCT would solve the bootstrap/transfer-student gap that CS2 itself
   never solved, if DSCT adopts any cross-course carry-forward posture.
8. Whether DSCT wires World Bible continuity into the Tuesday/Thursday
   chassis as doctrine already proposes (`fall-2026-weekly-architecture.md`)
   once Weeks 3-17 are actually authored.

## 14. Verification results

### A. Repository provenance audit
Every course-level finding above cites repository + exact commit/ref + path.
CS1 and CS2 paths listed in sections 4.1/4.2 were spot-verified directly by
this report's author (not only by the sub-agents) via `ls` and direct file
reads against the stated commits; results matched sub-agent citations. No
memory-only claim is included.

### B. Surface coverage audit

| Surface | CS1 | CS2 | DSCT |
|---|---|---|---|
| Planning/design docs | Found — `docs/curriculum/judgment_toolkit.md` | Found — `docs/curriculum/judgment_toolkit.md`, `docs/grading-model.md` | Found — `planning/fall-2026-weekly-architecture.md`, raw design quarry files |
| Assignments | Found — `assignments/A2-coding-odyssey-project.md`, `assignments/odyssey_gates/week-NN.md` | Found — `assignments/A2-coding-odyssey-project.md`, `assignments/odyssey_gates/week-NN.md` | Found only as passing mentions — `week-02/student/week-02-evidence-assignment.md`; no dedicated World Bible assignment exists |
| Rubrics | Found — `rubrics/odyssey_gates/week-02_rubric.md`, `week-17_rubric.md` | Found — `rubrics/odyssey_gates/week-03_rubric.md` through `week-14_rubric.md` | **NOT PRESENT** — DSCT has no `rubrics/` directory at all |
| Student-facing templates/content | Partial — no dedicated template file, only assignment prose | Partial — no dedicated template file, only assignment prose | **NOT PRESENT** — no template or dedicated content exists |
| Grading model | Found — folded into checkpoint pools, `docs/grading-model.md` | Found — folded into every gate rubric, `docs/grading-model.md` | Found, but explicitly states no grade — `docs/grading-model.md` has zero World Bible mentions |
| Sidecar reports/raw history | Found — `reports/015_reasoning_odyssey_fabric_reconciliation.md`, `reports/007_...md` | Found — `sidecar/prompts/017_build_four_living_worlds_bible.md`, `sidecar/runs/*` | Found — `sidecar/reports/305_reasoning_vocabulary_inventory.md`, `sidecar/runs/305_foreman_acceptance.md`, raw quarry files |

### C. Doctrine-versus-implementation audit
Every major World Bible behavior in section 6 (comparison matrix) and
sections 4.1-4.3 (implementation cards) is labeled CURRENT DOCTRINE,
STUDENT-FACING IMPLEMENTATION, HISTORICAL/PROVENANCE, ASPIRATIONAL/NOT
IMPLEMENTED, or AMBIGUOUS. No planning-language finding is reported as
implemented; DSCT's rich reasoning-history field proposal is explicitly and
repeatedly labeled ASPIRATIONAL throughout this report, not implied as built.

### D. Carry-forward claim audit
Section 9 (carry-forward evidence matrix) and section 13 apply the required
label explicitly: **no source in CS1, CS2, or DSCT implements literal
cross-course World Bible carry-forward.** Any apparent continuity across the
three courses (shared name, shared four-genre convention in CS1/CS2, shared
anti-bureaucracy posture, shared "preserve don't rewrite history" intent) is
labeled **FAMILY RESEMBLANCE / NO LITERAL CARRY-FORWARD EVIDENCE FOUND**
rather than overstated as implemented continuity.

### E. Write-scope audit

```
$ git -C /tmp/dsct-prompt309 diff --check
(no output — clean)
$ git -C /tmp/dsct-prompt309 diff --name-only 419b55bf1410670597ebe271138e6bd50577e0f2
(this worktree's own branch-point commit — the correct baseline, since
 origin/main has since advanced from concurrent Foreman workers on other
 prompts; diffing against a moving origin/main would falsely attribute their
 commits to this job)
sidecar/reports/309_world_bible_cross_course_provenance.md
$ git -C /tmp/dsct-prompt309 status --short
?? sidecar/reports/309_world_bible_cross_course_provenance.md
```

Only the required report changed in DSCT. CS1 and CS2 were inspected
read-only throughout (`ls`, direct file reads, and sub-agent `rg`/`grep`
searches only); no writes were made to either sibling repository, confirmed
by not running any write command against those paths at any point in this
session.

## Definition-of-done self-check

1. CS1, CS2, and DSCT each have an evidence-backed implementation card — done, section 4.
2. Current doctrine is distinguished from actual student-facing implementation and history — done throughout, explicit labels on every row.
3. The cross-course comparison exposes both commonality (section 7) and divergence (section 8).
4. Carry-forward/bootstrap claims do not exceed explicit evidence — section 9 applies the required "no evidence found" / "family resemblance" labels rather than overstating continuity.
5. Anti-bureaucracy evidence is concrete (quoted, cited) rather than aspirational, for CS1/CS2; DSCT's is honestly labeled as doctrine-only pending an actual artifact — section 11.
6. Every substantive finding has repo + commit/ref + path provenance — sections 4, 6-11 throughout.
7. No future World Bible policy has been chosen — section 13 lists exactly what remains open.
8. Jeremy + ChatGPT can decide the DSCT World Bible contract from actual course lineage: CS1 and CS2 both ship a real, working, lightweight, rubric-integrated, non-carry-forward, four-genre World Bible; DSCT currently has none built, with thin, non-contradictory, more permissive (fiction-optional) doctrine language and one richer but explicitly unresolved reasoning-history proposal in the raw design quarry.
