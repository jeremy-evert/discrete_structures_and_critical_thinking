# Job 321 — DSCT full-semester preflight to GREEN TO WRITE

## Outcome

Move **Discrete Structures & Critical Thinking** from its current source-ready state to an evidence-backed production-ready state, stopping with exactly one of:

- `GREEN TO WRITE`
- `BLOCKED: <one precise reason>`

This is a **preflight shift**. SWOSU production Canvas is read-only for the entire shift.

The owning repository is `jeremy-evert/discrete_structures_and_critical_thinking`.

## Current handoff from Job 322

Job 322 completed the source-authoring campaign and promoted it to canonical `main` with:

`sidecar/reports/322_luna_dsct_source_completion.md`

The accepted handoff verdict is:

```text
**Verdict:** `SOURCE READY FOR PREFLIGHT`
```

Treat that report as the immediate starting receipt, then verify it against current Git rather than re-running the old source-gap archaeology from scratch.

At the beginning of this shift:

1. capture the current DSCT SHA and verify the Job 322 report is canonical;
2. run `python3 scripts/validate_fall2026_source.py`;
3. run `python3 assessment/verify_week02_contract_paths.py` from the real Brandy DSCT checkout, where sibling repositories are expected at `../<repository>`;
4. verify the Week 2 sibling dependencies named by that validator rather than treating their absence in Job 322's disposable `/tmp` clones as current truth;
5. preserve Weeks 4–17 source unless fresh evidence proves a defect.

Do not reopen the semester authoring campaign merely because the older blocked Job 321 report said Weeks 4–15 and 17 were missing. Job 322 was created specifically to resolve that blocker.

## Older history, not current truth

Verify all of this before relying on it:

- production Canvas course has historically been `74035`;
- Report 319 said Week 1 was fully published and Week 2 was partial after a content-specific CloudFront/WAF 403;
- Prompt 320 told the prior Foreman to ship authoritative DSCT work without fabricating unauthored lessons;
- Week 3 had accepted container/LaTeX work;
- Week 16 Farkle/Machine Learning material had prior validation;
- the prior Job 321 preflight blocked on missing student-facing Weeks 4–15/17, but Job 322 subsequently authored and validated those packages;
- current Git has advanced since all earlier production reports.

Git, the Job 322 handoff, current reports, current source, and fresh read-only live state outrank this summary.

## Authority

You may:

- inspect and modify DSCT source, Sidecar, tests, validators, scripts, and documentation;
- create isolated DSCT branches/worktrees and dispatch bounded workers;
- inspect Course Foundry, Harbor, `foreman_interface`, shared curriculum repositories, and prior evidence when DSCT genuinely requires them;
- make bounded, backward-compatible shared-tooling repairs when DSCT cannot proceed without them, using isolated worktrees and explicit evidence;
- reconcile a non-production/Savnac DSCT target when current repository policy and a fresh bounded dry-run make that safe;
- promote accepted DSCT work/evidence to DSCT `main` when the governing Foreman contract allows it.

You may **not** write SWOSU production Canvas during this job.

Do not modify CS1, Computer Architecture, or CS2 course source. Do not modify JTT.

## Work First rule

The goal is a complete, teachable, internally consistent DSCT course ready for a bounded production reconcile.

Do not preserve stale prompt choreography merely because it exists. Preserve provenance, then collapse the remaining work into the smallest safe executable path.

Do not invent a new course because a historical week is incomplete. You **may repair missing student-facing DSCT material** when it is grounded by the accepted DSCT spine, grading model, existing reports/resources, and established course voice. When genuine pedagogical ambiguity remains, name it instead of silently choosing a different course.

## Required work

### 1. Establish current truth

Capture exact SHAs and verify the current course from Git:

- Job 322 source-completion receipt and validator;
- Weeks 1–17 student-facing source;
- assignments, rubrics, grading groups/weights/drop rules;
- Week 15 asynchronous behavior;
- Week 16 and Week 17 behavior;
- current deployment/validator support;
- Week 2 sibling dependency paths from the real Brandy checkout.

Classify each week from real source. Prefer the Job 322 classification unless current evidence disproves it.

### 2. Inspect production read-only

Freshly identify and verify the SWOSU production DSCT target. Historical course `74035` is a hint, not permission to assume identity.

Read only:

- course identity;
- modules/items/publish state;
- assignments/groups/weights/drop rules;
- due/lock dates;
- files/links where supported;
- enrollment/submission facts needed to avoid destructive reconciliation.

No production mutation is authorized.

### 3. Finish only proved Git-side gaps

Do as much real work as possible before asking for a production Foreman shift, but do not reopen already-accepted authoring without evidence.

Repair source, tests, validators, deployment manifests, grading contracts, or Sidecar truth only when current validation/live evidence proves them incomplete.

Give the historical Week 2 WAF/content seam one evidence-driven investigation. Do not evade institutional security controls and do not hammer production. Prefer source/rendering/request correctness or a harmless semantically equivalent representation when evidence supports it.

If old unmerged branches contain valid authored work, reconcile only content that current truth still lacks. Never resurrect stale deletions or old layouts wholesale.

### 4. Use isolated shared tooling

The shared Brandy Course Foundry checkout is known to accumulate runtime state and may be dirty.

Do not clean, reset, stash, normalize, or develop from unexplained shared dirt.

Use an isolated worktree/clone at an exact SHA for deployment-defining work. Record the exact Course Foundry SHA used. Treat any unpromoted containment branch as optional evidence, not canonical truth, unless it has been promoted.

### 5. Prove desired state

Before `GREEN TO WRITE`, produce a deterministic desired-course model and validate at minimum:

- complete intended module/week coverage;
- no unresolved tokens/placeholders;
- no accidental duplicate/zombie items;
- grading weights sum correctly;
- intended `drop_lowest` rules are present;
- due dates/lock dates are sane for Fall 2026;
- no undeclared destructive/prune behavior;
- links/assets resolve as far as tooling can prove;
- all source/tooling tests relevant to DSCT pass or have precisely named non-blocking yellows.

### 6. Reconcile non-production when useful

If a current Savnac/non-production target exists and the repository's current policy permits it, reconcile it only after a fresh dry-run.

Require:

- no unexplained deletes;
- explainable creates/updates;
- bounded target identity;
- post-write readback;
- two consecutive zero-delta dry-runs for fixed-point proof when practical.

If runtime policy blocks a permitted non-production write, stop at the runtime gate rather than routing around it. Leave the exact vetted command and evidence.

### 7. Produce the production semantic diff

Against the freshly verified SWOSU production target, generate a **read-only** semantic diff from the final desired model.

`GREEN TO WRITE` requires:

- exact production target identity proven fresh;
- no cross-list/topology mutation;
- no unexplained deletes;
- every create/update/delete, if any, understood and justified;
- grading/date/module/file behavior understood;
- the production deployer bounded to this one DSCT target;
- a clean independent readback plan;
- a source/tooling SHA set that will be rechecked before production writes.

## Evidence

Write the canonical report:

`sidecar/reports/321_luna_preflight_to_green_to_write.md`

It must include:

- DSCT SHA(s);
- Job 322 handoff verification;
- exact dependency/tooling SHAs;
- Week 2 sibling-dependency validation result;
- live target identity evidence;
- week-by-week source classification;
- work completed and commits promoted;
- validation commands/results;
- non-production reconcile evidence, if used;
- production semantic diff;
- named yellows;
- exact remaining production action.

End the report with exactly one machine-readable verdict line:

```text
**Verdict:** `GREEN TO WRITE`
```

or

```text
**Verdict:** `BLOCKED`
```

For `BLOCKED`, immediately state the single blocking reason.

## Done

This job is done when DSCT has either reached `GREEN TO WRITE` with durable evidence on canonical DSCT `main`, or one genuine blocker has been proved precisely enough that another agent does not need to rediscover it.

Do not perform the production write in this shift.
