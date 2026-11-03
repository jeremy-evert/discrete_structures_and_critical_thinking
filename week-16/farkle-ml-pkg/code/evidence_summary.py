#!/usr/bin/env python3
"""Summarize a quick_v1-style evidence CSV using only the standard library.

This is an instructor-facing reader. It deliberately does not run Farkle,
train a model, or import the course vendor package.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, TextIO


REQUIRED_COLUMNS = (
    "seed",
    "games",
    "starts_a",
    "starts_b",
    "wins_a",
    "wins_b",
    "ties",
)
REPORTED_RATE_COLUMNS = (
    "win_rate_a",
    "win_rate_b",
    "win_rate_difference_pp",
)
INTEGER_COLUMNS = ("seed", "games", "starts_a", "starts_b", "wins_a", "wins_b", "ties")


@dataclass(frozen=True)
class EvidenceRow:
    """One validated row, with rates recomputed from raw counts."""

    seed: int
    games: int
    starts_a: int
    starts_b: int
    wins_a: int
    wins_b: int
    ties: int
    win_rate_a: float
    win_rate_b: float
    difference_pp: float
    ordering_sign: int

    def as_dict(self) -> dict[str, int | float]:
        result = asdict(self)
        result["win_rate_difference_pp"] = result.pop("difference_pp")
        return result


def _parse_nonnegative_int(raw: str | None, column: str, row_number: int) -> int:
    if raw is None or raw.strip() == "":
        raise ValueError(f"row {row_number}: {column} must be a nonnegative integer")
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(
            f"row {row_number}: {column} must be a nonnegative integer, got {raw!r}"
        ) from exc
    if value < 0:
        raise ValueError(f"row {row_number}: {column} must be nonnegative")
    return value


def _parse_row(raw: dict[str, str], row_number: int) -> EvidenceRow:
    values = {
        column: _parse_nonnegative_int(raw.get(column), column, row_number)
        for column in INTEGER_COLUMNS
    }
    games = values["games"]
    if games == 0:
        raise ValueError(f"row {row_number}: games must be positive")
    if values["starts_a"] + values["starts_b"] != games:
        raise ValueError(
            f"row {row_number}: starts_a + starts_b must equal games "
            f"({values['starts_a']} + {values['starts_b']} != {games})"
        )
    if values["wins_a"] + values["wins_b"] + values["ties"] != games:
        raise ValueError(
            f"row {row_number}: wins_a + wins_b + ties must equal games "
            f"({values['wins_a']} + {values['wins_b']} + {values['ties']} != {games})"
        )

    win_rate_a = values["wins_a"] / games
    win_rate_b = values["wins_b"] / games
    difference_pp = round((win_rate_a - win_rate_b) * 100, 10)
    if values["wins_a"] > values["wins_b"]:
        ordering_sign = 1
    elif values["wins_a"] < values["wins_b"]:
        ordering_sign = -1
    else:
        ordering_sign = 0

    for column in REPORTED_RATE_COLUMNS:
        if column not in raw:
            continue
        if raw[column].strip() == "":
            raise ValueError(f"row {row_number}: {column} must not be blank")
        try:
            reported = float(raw[column])
        except ValueError as exc:
            raise ValueError(f"row {row_number}: {column} must be numeric") from exc
        expected = {
            "win_rate_a": win_rate_a,
            "win_rate_b": win_rate_b,
            "win_rate_difference_pp": difference_pp,
        }[column]
        if not math.isclose(reported, expected, rel_tol=1e-6, abs_tol=1e-6):
            raise ValueError(
                f"row {row_number}: {column} does not match raw counts "
                f"(reported {reported}, expected {expected})"
            )

    return EvidenceRow(
        seed=values["seed"],
        games=games,
        starts_a=values["starts_a"],
        starts_b=values["starts_b"],
        wins_a=values["wins_a"],
        wins_b=values["wins_b"],
        ties=values["ties"],
        win_rate_a=win_rate_a,
        win_rate_b=win_rate_b,
        difference_pp=difference_pp,
        ordering_sign=ordering_sign,
    )


def read_rows(source: TextIO) -> list[EvidenceRow]:
    """Read and validate rows from an open CSV text stream."""

    reader = csv.DictReader(source)
    if reader.fieldnames is None:
        raise ValueError("CSV is empty or missing a header")
    missing = [column for column in REQUIRED_COLUMNS if column not in reader.fieldnames]
    if missing:
        raise ValueError(f"missing required columns: {', '.join(missing)}")
    rows = []
    for row_number, raw in enumerate(reader, start=2):
        if raw.get(None):
            raise ValueError(f"row {row_number}: too many CSV fields")
        if not any(value not in (None, "") for value in raw.values()):
            continue
        rows.append(_parse_row(raw, row_number))
    if not rows:
        raise ValueError("CSV has no data rows")
    return rows


def summarize(rows: Iterable[EvidenceRow]) -> dict[str, object]:
    """Return row details and descriptive cross-row checks."""

    row_list = list(rows)
    if not row_list:
        raise ValueError("cannot summarize an empty row set")
    differences = [row.difference_pp for row in row_list]
    signs = {row.ordering_sign for row in row_list}
    return {
        "rows": [row.as_dict() for row in row_list],
        "min_difference_pp": min(differences),
        "max_difference_pp": max(differences),
        "range_pp": max(differences) - min(differences),
        "sign_flip_detected": -1 in signs and 1 in signs,
    }


def summarize_csv(path: Path) -> dict[str, object]:
    """Read *path* and return its validated evidence summary."""

    with path.open(newline="", encoding="utf-8") as source:
        return summarize(read_rows(source))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="quick_v1-style evidence CSV")
    args = parser.parse_args(argv)
    try:
        result = summarize_csv(args.csv_path)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
