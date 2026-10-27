from playlist.songs import same_song


def is_duplicate(a, b):
    """First attempt: b is a repeat of a when it is the same song and was added later."""
    return same_song(a, b) and b.id >= a.id
