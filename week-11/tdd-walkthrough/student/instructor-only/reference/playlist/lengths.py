def length_label(seconds):
    """Return 'short', 'normal', 'long' or 'epic' for a track length in seconds."""
    if seconds < 0 or seconds > 3600:
        raise ValueError("length out of range: {0}".format(seconds))
    if seconds >= 600:
        return "epic"
    if seconds >= 300:
        return "long"
    if seconds >= 180:
        return "normal"
    return "short"
