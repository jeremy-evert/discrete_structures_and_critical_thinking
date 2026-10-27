from fixtures import TRACKS
from playlist.songs import same_song
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
