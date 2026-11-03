# Week 16 evidence summary (instructor-only)

This directory is a small, standard-library-only reader for a `quick_v1`-style evidence CSV. It is an instructor check surface, not a student programming assignment: it does not contain a Farkle engine, a simulator, machine-learning code, or an import from `lessons/vendor`.

The fixture is synthetic course evidence copied from `week-16/fallback/quick_v1_results.csv`. Its provenance is documented here rather than added as a CSV field so the fixture remains byte-identical to the fallback. The three rows are the course's 10-game samples for seeds 17, 6262, and 2026, with balanced starts.

From raw counts, `evidence_summary.py` validates the required columns and denominators, recomputes A and B win rates, computes the A-minus-B difference in percentage points, records an ordering sign (`-1`, `0`, or `1`) for each row, and reports minimum, maximum, range, and whether both positive and negative signs occur.

Run from this directory:

```text
pytest
python evidence_summary.py fixtures/quick_v1_results.csv
```

The tests cover the happy path, denominator mismatch, missing column, tie handling, and an empty file. They are intentionally green; no red test is expected.
