# DSCT Luna Burn

This is the current control surface for Discrete Structures & Critical Thinking.

Job 321 preflight correctly returned `BLOCKED` because the current repository did not yet contain complete student-facing source for Weeks 4–15 and Week 17. That report remains provenance. The next active burn is therefore source completion, not another live-system preflight.

## Active Burn — source completion

Human command:

```bash
bash sidecar/launch_luna.sh source
```

Canonical job:

`sidecar/jobs/322_dsct_source_completion.md`

Canonical report:

`sidecar/reports/322_luna_dsct_source_completion.md`

Success marker:

```text
**Verdict:** `SOURCE READY FOR PREFLIGHT`
```

Authority:

- DSCT source authoring, DSCT-local validation, worker dispatch/review, commits, and safe promotion to DSCT `main` are authorized.
- SWOSU production Canvas writes are **NOT AUTHORIZED**.
- Savnac writes are **NOT AUTHORIZED**.
- Course Foundry/shared dependency mutation is **NOT AUTHORIZED** in this burn.

This burn exists to remove the exact source blocker proved by Job 321. Luna should adapt already-frozen Fall 2026 contracts and historical taught material into complete Week 4–15 and Week 17 packages, reconcile Week 2 source truth, validate the semester package, and leave one durable source-ready verdict.

## Next Burn — fresh preflight

After canonical DSCT `main` contains an accepted:

```text
**Verdict:** `SOURCE READY FOR PREFLIGHT`
```

run a **fresh** Luna shift:

```bash
bash sidecar/launch_luna.sh
```

Canonical job:

`sidecar/jobs/321_dsct_preflight_to_green_to_write.md`

Canonical preflight report:

`sidecar/reports/321_luna_preflight_to_green_to_write.md`

Success marker:

```text
**Verdict:** `GREEN TO WRITE`
```

Production Canvas authority in preflight: **READ ONLY**.

The fresh preflight must not inherit the old BLOCKED verdict as current truth. It re-verifies source, tooling, non-production state, live target identity, and the production semantic diff from current canonical Git.

## Final Burn — production

Human command after an accepted canonical `GREEN TO WRITE`:

```bash
bash sidecar/launch_luna.sh production
```

Canonical job:

`sidecar/jobs/321_dsct_production_closeout.md`

Canonical closeout report:

`sidecar/reports/321_luna_production_closeout.md`

Success marker:

```text
**Verdict:** `DEPLOYED`
```

The production invocation is fresh human authorization only for the bounded production plan proved by preflight and re-proved by the production freshness gate.

## Durable rules

- DSCT is the owning worksite.
- Do not select work from JTT.
- Do not take CS1, Computer Architecture, or CS2 work.
- Shared Course Foundry dirt is preserved, not cleaned or trusted as deployment-defining source.
- Source completion does not depend on Course Foundry at all.
- Preflight/production use isolated worktrees/clones and exact SHAs for shared tooling.
- Workers do bounded work; Luna inspects receipts and owns integration.
- Jeremy is not the message bus.
- Historical Prompt 320, Report 319, and the first BLOCKED Job 321 report remain provenance, not the current launch interface.
- Work First: finish the real course and prove it. Do not preserve ceremony that no longer helps delivery.
