def sort_key(track):
    """Length, then artist, then title, then id. The id is unique, so no two tracks ever tie."""
    return (track.seconds, track.artist.lower(), track.title.lower(), track.id)


def compare(a, b):
    """Returns -1, 0 or 1. Returns 0 only when a and b are the very same track."""
    return (sort_key(a) > sort_key(b)) - (sort_key(a) < sort_key(b))
