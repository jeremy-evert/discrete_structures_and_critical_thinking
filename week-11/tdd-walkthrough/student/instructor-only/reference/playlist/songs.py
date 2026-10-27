TOLERANCE_SECONDS = 5


def looks_alike(a, b):
    """Same artist (ignoring capitals) and lengths within 5 seconds of each other."""
    return (
        a.artist.lower() == b.artist.lower()
        and abs(a.seconds - b.seconds) <= TOLERANCE_SECONDS
    )


def same_song(a, b):
    """Are these two listings the same song? (First attempt: use looks_alike.)"""
    return looks_alike(a, b)
