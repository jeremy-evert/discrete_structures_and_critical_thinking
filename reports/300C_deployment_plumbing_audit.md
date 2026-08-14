# 300C — DSCT deployment-plumbing audit

## 1. Executive plumbing verdict

**Overall: NO-GO.** The existing generic pipe is real: Imprint has a typed `DesiredCourse` contract and reconciles through Harbor, and Harbor has the module/page/assignment/rubric operations that such a plan needs. But Fall 2026 DSCT does not currently enter that pipe. There is no DSCT `DesiredCourse` producer, no DSCT adapter registered in Course Foundry's normal graph, and no DSCT-specific dry path. The first failing seam is therefore **DSCT Git source → machine-readable desired state** (`course_foundry`), a `CODE`/`ARCHITECTURE DUPLICATION` finding independent of DSCT's incomplete content.

300C reached **Level 0 — static architecture only**. No plan was invented and no Savnac or real-Canvas write occurred.

## 2. What 300B established and what this audit does not re-litigate

300B remains authoritative: Tuesday is content-level `GO WITH YELLOWS`; Week 2 is `NO-GO`; semester readiness is `NO-GO`; and source coherence is conflicted. This audit neither authors nor resolves those inputs. A complete future DSCT source would still stop at the missing adapter described below.

## 3. Audited repository SHAs and runtime context

| Repository | SHA | State / note |
|---|---|---|
| DSCT | `69984ecead1b572203b9ac73291d9e6df74e7ed3` | clean; matches 300B |
| Course Foundry | `39208d7148bf7ae8a5676f7334d79c8219a8b4b6` | clean |
| Imprint | `ef17850f905f20962674a2f5b52b06679e7d9c7f` | clean |
| Harbor | `a5b3eb2d9f58285aa7617c88bebcb2c505c7aaed` | clean |
| Savnac | `c2d11e96b7d4bc64b8550619281720f5fd4a2dbf` | clean |
| semester_kickoff_week | `94d8591369c350996f6984b05d0a9d50cee764a8` | clean; read only for DSCT Week 1 relevance |
| task tracking | `14a85bd0f058ad830d709c6b507792136ac36581` | unrelated `bin/tmux-snag` untracked and preserved; drifted from 300B's stated `2f49088` |

The clean repositories were offered `git pull --ff-only`, but each pull failed before contact with GitHub because the host rejected `/etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf`. The audit therefore records local checked-out SHAs, not a remote-freshness claim. Runtime host: `maise`.

## 4. Current deployment architecture graph

```text
DSCT course_metadata.yaml ──> course_information_page ──> Harbor ──> target Canvas
                                     (single page; direct, legacy/parallel)

DSCT lessons/assignments/planning ──> [NO DSCT producer] ──> DesiredCourse
                                                               │
CS1 DesiredCourse producer ───────────────────────────────────┘
                                                               v
                                                        Imprint push_course
                                                               v
                                                         Harbor Canvas API
                                                               v
                                                     Savnac or real Canvas

semester_kickoff_week ──> semester_kickoff_savnac_load_adapter ──> Harbor
                           (M/W/F direct reconciliation; legacy duplicate)
```

The detailed edge receipt is `runs/2026-08-14_prompt300C_deployment_plumbing_audit/derived/deployment_edges.csv`.

## 5. DSCT source → desired-state producer

### 2A. Course Foundry selection

**No.** `course_foundry/course_foundry/run.py` declares `_KNOWN_COURSES = {24298, 1}` and only registers UCS101 and CS1 load/sync adapters. DSCT's source comment identifies Savnac course `4`, but there is no `elif args.course == 4`, no registration, and no DSCT adapter. Node `n001_select_course_and_repo.py` requires both adapters and stops on their absence.

### 2B. Desired state

**No producer exists.** Searches found `cs1_desired_course.py` and `cs2_desired_course.py`, but no DSCT/`COMSC-2043` builder and no use of DSCT lessons, assignments, or planning to construct `DesiredCourse`, `DesiredModule`, or `DesiredObject`. The first missing executable seam is a deterministic DSCT plan builder in Course Foundry (or a course-owned producer deliberately wired into Course Foundry); content incompleteness is a separate input issue.

### 2C. Existing partial source support

| DSCT source family | Producer / adapter | Output contract | Imprint? | Harbor direct? | Tested? | Current status | Exact evidence |
|---|---|---|---|---|---|---|---|
| `course_metadata.yaml` | `course_information_page.load_course_metadata` + `render_course_information_markdown` | one standalone Canvas Page | no | yes | static only; config absent | `WORKING_BUT_LEGACY` generic capability, not a course plan | `course_foundry/course_foundry/course_information_page.py` |
| lessons, assignments, planning | none | none | no | no | no | `PLANNED_NOT_IMPLEMENTED` | no DSCT producer discovered; see edge receipt |
| shared kickoff material | `compute_kickoff_plan` + `semester_kickoff_savnac_load_adapter` | private kickoff plan / direct reconcile | no | yes | not invoked | `WORKING_BUT_LEGACY` for M/W/F courses; not DSCT-reusable as-is | `course_foundry/course_foundry/semester_kickoff_content_map.py`, `load_adapters.py:466` |

## 6. Imprint contract and Course Foundry cutover state

`imprint.schema.DesiredCourse` supports a course label/id, ordered modules, objects of `page`, `assignment`, or `file`, assignment groups, rubric criteria, due dates, and source references. `imprint.reconcile.push_course` produces a structured `ReconcileResult`: create/update/skip/delete decisions and per-item log entries.

`dry_run=True` still reads live state but skips every create/update/delete. `force` and non-`none` `prune_scope` are gated on non-dry runs by `imprint.safety.require_destructive_action_allowed`; a real target needs explicit `--confirm-live-write`, while a declared sandbox can use `--sandbox`. Pruning is limited to Imprint-modeled Page/Assignment module items.

The actual current cutover is incomplete:

- CS1 is `CANONICAL_CURRENT`: `cs1_savnac_load_adapter` builds `cs1_savnac_desired_course` and calls `imprint.reconcile.push_course`.
- `semester_kickoff_savnac_load_adapter` is still `WORKING_BUT_LEGACY`: it lists/creates/updates Harbor objects directly. Imprint's own `AGENTS.md` names this explicitly as the remaining uncut-over adapter.
- Course Information is another deliberately standalone direct-Harbor reconciliation path, explicitly outside `DesiredCourse` because it is not attached to a module.
- DSCT has neither an Imprint plan nor a direct full-course adapter.

Thus Imprint engine: **GO WITH YELLOWS** (code compiles, but the documented pytest suite could not run because the local interpreter lacks `pytest` and `pydantic`). DSCT → Imprint seam: **NO-GO**.

## 7. Harbor transport readiness

Harbor is the only intended Canvas HTTP boundary for this pipeline: Imprint imports `CanvasClient` and typed functions from `harbor.api`; no DSCT producer exists that could bypass it. Harbor exposes list/get/create/update/delete operations for modules, module items, pages, assignments, rubrics/associations, and assignment groups—the DSCT object types Imprint can model. `CanvasClient` optionally enforces a course allowlist based on `CANVAS_ENFORCE_COURSE_ALLOWLIST` and `CANVAS_ALLOWED_COURSE_IDS`; default enforcement is off. `harbor.api._check_status` masks a bearer token found in an error response.

**CODE CONTRACT PROVEN:** yes, by source and successful `compileall`.

**LOCAL TEST PROVEN:** no. Focused pytest command could not start because `/usr/bin/python3` has no `pytest`; direct import also stopped because `pydantic` is absent. No dependency was installed for this audit.

**SAVNAC NETWORK PATH PROVEN:** no. **REAL CANVAS NETWORK PATH PROVEN:** no.

## 8. Savnac target, reachability, and safe read evidence

Current Savnac documentation says Canvas runs in a private VM hosted on **Brandy**, at `http://192.168.122.172:3000`; Maise is not its expected direct host. `harbor/docs/savnac.md` says the normal programmatic path is direct from Brandy after explicitly sourcing `~/.config/canvas/savnac.env`; it must not be auto-loaded. The DSCT metadata comment claims a Savnac course `4`, but Savnac's current operational document only establishes course `1` as the original CS1 test course. Therefore `4` is source-backed as a claim but not verified as an extant/current DSCT sandbox course.

No local canvas or Savnac env file exists on Maise. A noninteractive SSH attempt to the documented Brandy route failed locally with `socket: Operation not permitted`, before it could perform the read-only login probe. This is `RUNTIME`/`EXTERNAL VERIFICATION`, not evidence that Savnac is down. No credentials were read or logged.

## 9. Highest DSCT dry-run level achieved

**Level 0.** A real DSCT desired plan cannot be generated, so Levels 1–4 cannot be legitimately attempted. A hand-made plan would only test Imprint generically and was forbidden by this prompt. The separate source-backed target/network read is also unproven.

## 10. Real Canvas path and safety gates

Harbor defaults `CANVAS_API_BASE_URL` to `https://swosu.instructure.com`; configuration supplies the actual base URL/token. Imprint's CLI defaults to non-destructive `prune_scope=none`, `force=False`, and requires `--dry-run` to make its reconciliation read-only. It requires an expected-host marker only when one is supplied, and it refuses destructive real-target actions absent `--confirm-live-write`. No source-backed Fall 2026 DSCT real Canvas course ID was found, so no real-Canvas call was appropriate or attempted.

## 11. Course Foundry graph node readiness for DSCT

| Node | DSCT callable today? | Inputs | External side effects | Course-specific assumptions | Proof | Blocker |
|---|---|---|---|---|---|---|
| select course/repo (`n001`) | no | course ID, repo path | none | IDs 24298/1 only in normal CLI | `run.py`, `n001_select_course_and_repo.py` | no DSCT registration |
| load (`n002`) | no | registered load adapter | normal adapters write | CS1/UCS101 only; no dry-run parameter in node | `n002_load_course_into_canvas.py` | no DSCT adapter; ordinary graph is write-oriented |
| verify (`n003`) | no | registered sync adapter | can be read-only | CS1/UCS101 only | `sync_adapters.py` | no DSCT adapter |
| sufficiency (`n004`) | not entered | evaluator | model work | not audited by 300C | graph source | earlier node stop |
| classify/remediate (`n005/n006`) | not entered | classifier/remediation adapter | potential worktree/model work | outside 300C | graph source | earlier node stop; prohibited scope |

Course Foundry → Imprint → Harbor is the current CS1 path, not a universal current path. It coexists with the direct-Harbor kickoff and standalone-page routes.

## 12. Shared Week 1 deployment seam

An adapter exists, but it is not directly reusable for DSCT. `semester_kickoff_savnac_load_adapter(kickoff_repo_path, course_id, course_label, monday_overlay_path, assignment_group_name)` can accept an arbitrary course ID/label and calls Harbor directly, not Imprint. Yet `semester_kickoff_content_map.py` hard-codes Monday/Wednesday/Friday modules and fixed 2026-08-17/19/21 dates. DSCT meets Tuesday/Thursday, so object naming, module placement, and due-day mapping are wrong. The DSCT framing slot is only a `monday_overlay_path`; it is not a general T/Th course-specific input model. This is a deployment seam requiring adapter/mapping work, separate from the missing DSCT framing content.

## 13. Seam-by-seam verdict matrix

The canonical machine-readable matrix is `runs/2026-08-14_prompt300C_deployment_plumbing_audit/derived/seam_verdicts.csv`. In short: seams 1, 2, 9, 10, 11, 12, 13, and 14 are `NO-GO`; 3 and 8 are `UNKNOWN — NEEDS SPECIFIC EVIDENCE`; 4 and 6 are `GO WITH YELLOWS`; and 5 is `GO`.

## 14. First failing seam

**`course_foundry`: no DSCT `DesiredCourse` producer.** Exact proof: Course Foundry has explicit CS1/CS2 desired-course modules but no DSCT/COMSC-2043 counterpart; `run.py` wires only 24298 and 1. Classification: `CODE` plus `ARCHITECTURE DUPLICATION`. It blocks Tuesday/Week 2 only if deployment through the intended architecture is required; it blocks all later DSCT deployment absolutely. The smallest remedy belongs primarily in Course Foundry.

## 15. Could complete DSCT content be deployed tomorrow?

**No.** Complete content would not become a deterministic desired state without new plumbing. The first change is a DSCT plan builder; then it must be registered with a dry-run-safe Course Foundry entrypoint, target course `4` must be verified by a safe read, and the normal Savnac path must be available from the executing host.

## 16. Smallest implementation that makes DSCT deployment boring

In `course_foundry`, add one `dsct_desired_course.py` that reads only tracked DSCT source/metadata and emits `imprint.schema.DesiredCourse`, with explicit source references and no invented course content/dates. Add DSCT's source-backed target configuration/registration and a **dry-run-only** normal entrypoint that calls Imprint. Separately, either keep Week 1 out until its DSCT T/Th mapping exists or add a narrow DSCT kickoff mapper; do not reuse the M/W/F adapter unchanged. Then verify Savnac course 4 with a read-only Harbor call. Harbor and Imprint need no preliminary feature work unless implementation reveals a concrete schema gap.

## 17. What blocks Tuesday / Week 2 / later only

- **Tuesday:** content is 300B's `GO WITH YELLOWS`; deployment cannot be previewed through the intended DSCT path. The shared M/W/F kickoff adapter is not compatible with DSCT T/Th.
- **Week 2:** blocked independently by 300B's content `NO-GO`, plus this missing desired-state producer.
- **Later / real Canvas:** additionally blocked by the absence of a source-backed Fall 2026 real Canvas ID and no live network proof.

## 18. Questions requiring Jeremy

None. Every missing element is an engineering or external-verification task, not an unresolved instructor-policy choice.

## 19. Evidence appendix

Commands and unedited non-secret outputs are under `runs/2026-08-14_prompt300C_deployment_plumbing_audit/raw/`. `repo_states.json` records SHAs, state, and the failed refresh condition. The audit read the 300A/300B prompts, reports, and handoff receipts named by Prompt 300C; it read repository instructions before repo-specific validation. Focused pytest was unavailable without dependencies; `python3 -m compileall -q course_foundry/course_foundry imprint/imprint harbor/harbor` passed.
