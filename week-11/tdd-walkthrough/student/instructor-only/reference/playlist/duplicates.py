from playlist.songs import same_song


def is_duplicate(a, b):
    """Same song. Written so swapping a and b cannot change the answer.

    Which copy to KEEP is a different question; see clean_playlist.
    """
    return same_song(a, b)
