import pytest

from playlist.lengths import length_label


def test_short_tracks_are_under_three_minutes():
    assert length_label(0) == "short"
    assert length_label(90) == "short"
    assert length_label(179) == "short"


def test_normal_tracks_are_three_to_under_five_minutes():
    assert length_label(180) == "normal"
    assert length_label(240) == "normal"
    assert length_label(299) == "normal"


def test_long_tracks_are_five_to_under_ten_minutes():
    assert length_label(300) == "long"
    assert length_label(450) == "long"
    assert length_label(599) == "long"


def test_epic_tracks_are_ten_minutes_up_to_one_hour():
    assert length_label(600) == "epic"
    assert length_label(1800) == "epic"
    assert length_label(3600) == "epic"


def test_lengths_outside_zero_to_3600_are_rejected():
    with pytest.raises(ValueError):
        length_label(-1)
    with pytest.raises(ValueError):
        length_label(3601)
