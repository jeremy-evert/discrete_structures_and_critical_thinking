from __future__ import annotations

import csv
from pathlib import Path

import pytest

from evidence_summary import read_rows, summarize_csv


FIXTURE = Path(__file__).parent / "fixtures" / "quick_v1_results.csv"
CORE_COLUMNS = ["seed", "games", "starts_a", "starts_b", "wins_a", "wins_b", "ties"]


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str] = CORE_COLUMNS) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def test_fallback_bundle_rates_range_and_sign_flip() -> None:
    result = summarize_csv(FIXTURE)

    assert [row["seed"] for row in result["rows"]] == [17, 6262, 2026]
    assert [row["ordering_sign"] for row in result["rows"]] == [-1, 1, 1]
    assert [row["win_rate_a"] for row in result["rows"]] == [0.3, 0.6, 0.8]
    assert [row["win_rate_b"] for row in result["rows"]] == [0.7, 0.4, 0.2]
    assert [row["win_rate_difference_pp"] for row in result["rows"]] == [-40.0, 20.0, 60.0]
    assert result["min_difference_pp"] == -40.0
    assert result["max_difference_pp"] == 60.0
    assert result["range_pp"] == 100.0
    assert result["sign_flip_detected"] is True


def test_denominator_mismatch_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "bad.csv"
    write_csv(
        path,
        [{"seed": 1, "games": 10, "starts_a": 5, "starts_b": 4, "wins_a": 5, "wins_b": 5, "ties": 0}],
    )

    with pytest.raises(ValueError, match=r"starts_a \+ starts_b must equal games"):
        summarize_csv(path)


def test_missing_required_column_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "missing.csv"
    write_csv(
        path,
        [{"seed": 1, "starts_a": 5, "starts_b": 5, "wins_a": 5, "wins_b": 5, "ties": 0}],
        fieldnames=["seed", "starts_a", "starts_b", "wins_a", "wins_b", "ties"],
    )

    with pytest.raises(ValueError, match="missing required columns: games"):
        summarize_csv(path)


def test_equal_wins_are_a_tie_and_do_not_flip_sign(tmp_path: Path) -> None:
    path = tmp_path / "tie.csv"
    write_csv(
        path,
        [{"seed": 7, "games": 10, "starts_a": 5, "starts_b": 5, "wins_a": 4, "wins_b": 4, "ties": 2}],
    )

    result = summarize_csv(path)

    assert result["rows"][0]["ordering_sign"] == 0
    assert result["rows"][0]["win_rate_difference_pp"] == 0.0
    assert result["sign_flip_detected"] is False


def test_empty_file_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "empty.csv"
    path.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="CSV is empty or missing a header"):
        summarize_csv(path)
