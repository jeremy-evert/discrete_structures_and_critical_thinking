def compare(a, b):
    """Returns -1, 0 or 1 by comparing lengths."""
    return (a.seconds > b.seconds) - (a.seconds < b.seconds)
