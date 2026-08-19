# Job 321 — DSCT guarded production reconcile and closeout

## Outcome

Take an already accepted DSCT `GREEN TO WRITE` preflight and perform exactly one bounded production reconcile against the freshly reverified SWOSU Canvas target, then independently read it back and close the course honestly.

This job is authorized only when launched through:

`bash sidecar/launch_luna.sh production`

and only when canonical `origin/main` contains the accepted preflight report with:

`**Verdict:** `GREEN TO WRITE``

## Freshness gate before any write

Before mutating production:

1. fetch canonical DSCT `origin/main`;
2. verify the accepted preflight report is still canonical;
3. capture the current DSCT and dependency/tooling SHAs;
4. freshly re-identify the exact production DSCT course;
5. re-read enrollments/submissions and any other facts that make destructive reconciliation unsafe;
6. rerun the production dry-run/semantic diff;
7. compare it to the accepted preflight envelope.

If target identity, source/tooling truth, or the planned mutation changed materially, **STOP BEFORE WRITE** and report the drift. The launcher's human authorization does not authorize a materially different plan.

## Authorized production action

You may perform only the bounded DSCT content/configuration reconcile proved by the fresh preflight and freshness gate.

You may not:

- cross-list or de-cross-list sections;
- change another Canvas course;
- perform unexplained pruning/deletes;
- widen scope to CS1, Computer Architecture, or CS2;
- modify JTT;
- route around institutional security controls;
- use the dirty shared Course Foundry checkout as deployment-defining source.

Use exact SHAs and an isolated worktree/clone for deployment-defining shared tooling.

## Reconcile rules

- production is single-writer;
- workers may inspect or prepare bounded repairs but do not receive production-write authority;
- zero unexplained deletes;
- every create/update must be explainable from accepted desired state;
- if the Week 2 historical WAF/content seam reappears, diagnose safely and do not hammer retries;
- if a verifier is proven defective, prove production truth independently rather than manufacturing unnecessary writes.

## Required closeout

After the write:

1. independently read back production;
2. rerun the production dry-run and prove the cleanest achievable fixed point;
3. verify module and item publish state;
4. verify grading groups, weights, and `drop_lowest` rules;
5. verify due dates and lock dates;
6. verify links/files/assets as far as tooling permits;
7. sweep for duplicates, zombies, placeholders, stale historical items, and undeclared omissions;
8. walk representative student paths, including sentinel weeks 1, 2, 3, 6, 9, 14, 15, 16, and 17;
9. verify submission paths and asynchronous access assumptions;
10. name every remaining yellow explicitly.

Do not define success as merely receiving successful Canvas API responses. The course must be student-usable.

## Evidence

Write:

`sidecar/reports/321_luna_production_closeout.md`

Include:

- launch authorization timestamp/provenance;
- exact DSCT/tooling SHAs;
- fresh production target identity;
- pre-write dry-run/semantic diff;
- actual production mutations;
- post-write readback;
- fixed-point/idempotency evidence;
- student-path checks;
- named yellows;
- exact remaining human action, if any.

End with exactly one verdict:

`**Verdict:** `DEPLOYED``

or

`**Verdict:** `NOT DEPLOYED``

## Done

The job is complete only when production has been independently verified and the canonical report is durable on DSCT `main`.
