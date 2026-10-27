from fixtures import GLASS_HARBOR, PAPER_MOONS
from playlist.songs import looks_alike
from playlist.track import Track


def test_same_artist_and_lengths_4_seconds_apart_look_alike():
    assert looks_alike(Track(10, "A", "Zed", 100), Track(11, "B", "Zed", 104))


def test_lengths_exactly_5_seconds_apart_still_look_alike():
    assert looks_alike(Track(10, "A", "Zed", 100), Track(11, "B", "Zed", 105))


def test_lengths_6_seconds_apart_do_not():
    assert not looks_alike(Track(10, "A", "Zed", 100), Track(11, "B", "Zed", 106))


def test_different_artists_never_look_alike():
    assert not looks_alike(Track(10, "A", "Zed", 204), PAPER_MOONS)


def test_capital_letters_in_the_artist_do_not_matter():
    assert looks_alike(Track(10, "A", "lantern hill", 100), Track(11, "B", "LANTERN HILL", 101))


def test_same_artist_but_very_different_lengths_do_not():
    assert not looks_alike(PAPER_MOONS, GLASS_HARBOR)
