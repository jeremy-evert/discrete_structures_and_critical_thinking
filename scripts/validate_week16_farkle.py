#!/usr/bin/env python3
"""Validate DSCT-specific Week 16 seams without duplicating shared tests."""

import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "lessons" / "week-16-farkle-evidence.py"
PROVENANCE = ROOT / "lessons" / "vendor" / "farkle_ml" / "_SHARED_PROVENANCE.json"
RECEIPT_DIR = ROOT / "sidecar" / "runs"

REQUIRED_AUTHORED_FILES = [
    ROOT / "planning" / "week-16.md",
    ROOT / "week-16" / "README.md",
    ROOT / "week-16" / "student" / "farkle-evidence-lab.md",
    ROOT / "week-16" / "instructor" / "guide.md",
    ROOT / "assignments" / "week-16-farkle-evidence-receipt.md",
    RUNNER,
]

REQUIRED_COLUMNS = {
    "seed",
    "games",
    "starts_a",
    "starts_b",
    "wins_a",
    "wins_b",
    "ties",
    "turns_a",
    "turns_b",
    "farkles_a",
    "farkles_b",
    "win_rate_a",
    "win_rate_b",
    "win_rate_difference_pp",
}


def write_receipt(stamp, status, lines):
    RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
    receipt = RECEIPT_DIR / f"week16_farkle_validation_{stamp}.md"
    receipt.write_text(
        "\n".join([
            "# DSCT Week 16 Farkle validation receipt",
            "",
            f"- UTC: {stamp}",
            f"- status: **{status}**",
            *lines,
            "",
        ]),
        encoding="utf-8",
    )
    print(receipt)
    return receipt


def run_command(args, out_dir):
    result = subprocess.run(
        [sys.executable, str(RUNNER), *args, "--out-dir", str(out_dir)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return result


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ROOT / "artifacts" / "week16_farkle_validation" / stamp
    out_dir.mkdir(parents=True, exist_ok=True)

    missing = [path for path in REQUIRED_AUTHORED_FILES if not path.exists()]
    if missing:
        write_receipt(
            stamp,
            "FAIL",
            ["- missing authored file: " + str(path.relative_to(ROOT)) for path in missing],
        )
        return 1

    if not PROVENANCE.exists():
        write_receipt(
            stamp,
            "YELLOW",
            [
                "- shared vendor package has not been synchronized",
                "- required action from the shared checkout:",
                "  `python scripts/sync_consumer.py ../discrete_structures_and_critical_thinking/lessons/vendor/farkle_ml --apply`",
            ],
        )
        return 1

    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))

    initial_dir = out_dir / "initial"
    initial = run_command(
        ["initial", "--games", "10", "--seed", "17"],
        initial_dir,
    )
    (out_dir / "initial_stdout.txt").write_text(initial.stdout, encoding="utf-8")
    (out_dir / "initial_stderr.txt").write_text(initial.stderr, encoding="utf-8")
    if initial.returncode != 0:
        write_receipt(
            stamp,
            "FAIL",
            [
                f"- shared commit: `{provenance.get('shared_commit', 'unknown')}`",
                f"- initial runner failed with exit {initial.returncode}",
                f"- log: `{(out_dir / 'initial_stderr.txt').relative_to(ROOT)}`",
            ],
        )
        return initial.returncode

    initial_csv = initial_dir / "initial_result.csv"
    with initial_csv.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 1 or not REQUIRED_COLUMNS.issubset(rows[0]):
        write_receipt(
            stamp,
            "FAIL",
            ["- initial CSV did not preserve required DSCT raw evidence columns"],
        )
        return 2

    bundle_dir = out_dir / "bundle"
    bundle = run_command(
        ["bundle", "--games", "10", "--bundle", "quick_v1"],
        bundle_dir,
    )
    (out_dir / "bundle_stdout.txt").write_text(bundle.stdout, encoding="utf-8")
    (out_dir / "bundle_stderr.txt").write_text(bundle.stderr, encoding="utf-8")
    if bundle.returncode != 0:
        write_receipt(
            stamp,
            "FAIL",
            [
                f"- shared commit: `{provenance.get('shared_commit', 'unknown')}`",
                f"- bundle runner failed with exit {bundle.returncode}",
                f"- log: `{(out_dir / 'bundle_stderr.txt').relative_to(ROOT)}`",
            ],
        )
        return bundle.returncode

    bundle_csv = bundle_dir / "quick_v1_results.csv"
    with bundle_csv.open(newline="", encoding="utf-8") as handle:
        bundle_rows = list(csv.DictReader(handle))
    if len(bundle_rows) < 2:
        write_receipt(
            stamp,
            "FAIL",
            ["- repeated bundle did not preserve multiple per-seed rows"],
        )
        return 3

    if any(not REQUIRED_COLUMNS.issubset(row) for row in bundle_rows):
        write_receipt(
            stamp,
            "FAIL",
            ["- bundle CSV lost required raw evidence columns"],
        )
        return 4

    receipt = write_receipt(
        stamp,
        "GREEN",
        [
            f"- shared commit: `{provenance.get('shared_commit', 'unknown')}`",
            f"- initial evidence: `{initial_csv.relative_to(ROOT)}`",
            f"- bundle evidence: `{bundle_csv.relative_to(ROOT)}`",
            f"- bundle rows: {len(bundle_rows)}",
            "- raw starts/wins/ties/turns/Farkles survived into the DSCT evidence surface",
            "- course-facing runner completed without GPU/cloud/paid-service dependency",
        ],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
