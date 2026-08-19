# DSCT Luna Burn

This is the current two-burn control surface for Discrete Structures & Critical Thinking.

## Burn 1 — preflight

Human command:

```bash
bash sidecar/launch_luna.sh
```

Goal: let a fresh Luna Foreman do the Git/source/tooling/live-read work required to reach an evidence-backed production decision without writing SWOSU production Canvas.

Canonical job:

`sidecar/jobs/321_dsct_preflight_to_green_to_write.md`

Canonical preflight report:

`sidecar/reports/321_luna_preflight_to_green_to_write.md`

Success marker:

`**Verdict:** `GREEN TO WRITE``

Production Canvas authority in this burn: **READ ONLY**.

## Burn 2 — production

Human command after an accepted canonical GREEN TO WRITE:

```bash
bash sidecar/launch_luna.sh production
```

Canonical job:

`sidecar/jobs/321_dsct_production_closeout.md`

Canonical closeout report:

`sidecar/reports/321_luna_production_closeout.md`

Success marker:

`**Verdict:** `DEPLOYED``

The production invocation is fresh human authorization only for the bounded production plan proved by preflight and re-proved by the production freshness gate.

## Durable rules

- DSCT is the owning worksite.
- Do not select work from JTT.
- Do not take CS1, Computer Architecture, or CS2 work.
- Shared Course Foundry dirt is preserved, not cleaned or trusted as deployment-defining source.
- Use isolated worktrees/clones and exact SHAs for shared tooling.
- Workers do bounded work; Luna inspects receipts and owns integration.
- Jeremy is not the message bus.
- Historical Prompt 320 and Report 319 remain provenance, not the launch interface.
- Work First: finish the real course and prove it. Do not preserve ceremony that no longer helps delivery.
