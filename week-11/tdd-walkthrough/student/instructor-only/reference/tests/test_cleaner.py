from fixtures import GLASS_HARBOR, NIGHT_BUS, PAPER_MOONS, SLOW_ORBIT_1, TRACKS
from playlist.cleaner import clean_playlist
from playlist.track import Track


def test_three_listings_of_one_song_become_the_earliest_one():
    assert clean_playlist(TRACKS) == [SLOW_ORBIT_1, PAPER_MOONS, GLASS_HARBOR, NIGHT_BUS]


def test_a_playlist_with_no_duplicates_comes_back_unchanged():
    assert clean_playlist([PAPER_MOONS, GLASS_HARBOR]) == [PAPER_MOONS, GLASS_HARBOR]


def test_an_empty_playlist_stays_empty():
    assert clean_playlist([]) == []


def test_the_input_order_does_not_change_which_song_is_kept():
    shuffled = [TRACKS[2], TRACKS[5], TRACKS[4], TRACKS[0], TRACKS[3], TRACKS[1]]
    assert clean_playlist(shuffled) == [SLOW_ORBIT_1, PAPER_MOONS, GLASS_HARBOR, NIGHT_BUS]


def test_cleaning_twice_changes_nothing():
    once = clean_playlist(TRACKS)
    assert clean_playlist(once) == once
