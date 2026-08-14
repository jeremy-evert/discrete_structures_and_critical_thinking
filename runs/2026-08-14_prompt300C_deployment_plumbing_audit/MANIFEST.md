# Prompt 300C deployment-plumbing audit

Date: 2026-08-14. Owner: `discrete_structures_and_critical_thinking`.

This run examined existing source and exercised only local compilation and safe connectivity/configuration checks. It made no course-content, Savnac, real-Canvas, ZyBooks, grading-pipeline, Marker, Coach, Dispatch, synthetic-student, or NRP changes.

Key receipts:

- `derived/repo_states.json` — repository state and refresh outcome.
- `derived/deployment_edges.csv` — file/function-level architecture graph.
- `derived/seam_verdicts.csv` — required seam verdicts.
- `derived/dry_run_level.json` — highest legitimate DSCT dry-run level.
- `raw/20260814T000000Z__validation.raw.txt` — test/compile results.
- `raw/20260814T000000Z__savnac_probe.raw.txt` — non-secret path/configuration proof.
