import re

TOLERANCE_SECONDS = 5


def looks_alike(a, b):
    """Same artist (ignoring capitals) and lengths within 5 seconds of each other."""
    return (
        a.artist.lower() == b.artist.lower()
        and abs(a.seconds - b.seconds) <= TOLERANCE_SECONDS
    )


def song_key(track):
    """Normalize a listing to a key: artist and title, lowercase, no (brackets), no punctuation.

    Two listings are the same song exactly when their keys are equal.
    """
    title = re.sub(r"\([^)]*\)", " ", track.title.lower())
    title = re.sub(r"[^a-z0-9 ]", "", title)
    return (track.artist.lower().strip(), " ".join(title.split()))


def same_song(a, b):
    return song_key(a) == song_key(b)
