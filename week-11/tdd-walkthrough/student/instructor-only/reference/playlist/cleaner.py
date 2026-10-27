from playlist.songs import song_key


def clean_playlist(tracks):
    """Keep one track per song: the earliest one added. Return them in playlist order."""
    keepers = {}
    for track in sorted(tracks, key=lambda t: t.id):
        keepers.setdefault(song_key(track), track)
    return sorted(keepers.values(), key=lambda t: t.id)
