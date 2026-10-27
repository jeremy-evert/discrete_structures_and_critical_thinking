from fixtures import SLOW_ORBIT_1, SLOW_ORBIT_2, SLOW_ORBIT_3, PAPER_MOONS, TRACKS
from playlist.songs import looks_alike, same_song, song_key
from relations import reflexive_failure, symmetric_failure, transitive_failure


def test_same_song_is_reflexive():
    assert reflexive_failure(same_song, TRACKS) is None


def test_same_song_is_symmetric():
    assert symmetric_failure(same_song, TRACKS) is None


def test_same_song_is_transitive():
    witness = transitive_failure(same_song, TRACKS)
    assert witness is None, (
        "not transitive: {0.id} ~ {1.id} and {1.id} ~ {2.id}, but {0.id} !~ {2.id}"
        " (lengths {0.seconds}, {1.seconds}, {2.seconds})".format(*witness)
    )


def test_looks_alike_is_still_not_an_equivalence():
    """Keep the old counterexample on record: 'close in length' is a hint, not a rule."""
    assert transitive_failure(looks_alike, TRACKS) == (SLOW_ORBIT_1, SLOW_ORBIT_2, SLOW_ORBIT_3)


def test_song_key_puts_the_three_listings_in_one_bin():
    assert {song_key(t) for t in (SLOW_ORBIT_1, SLOW_ORBIT_2, SLOW_ORBIT_3)} == {("lantern hill", "slow orbit")}
    assert song_key(PAPER_MOONS) != song_key(SLOW_ORBIT_1)
