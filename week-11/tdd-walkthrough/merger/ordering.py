def sort_key(record):
    """Family name, then given name, then id. The id makes the key unique, so no two records tie."""
    parts = record.name.lower().split()
    return (parts[-1], parts[0], record.id)


def compare(a, b):
    """Returns -1, 0 or 1. Returns 0 only when a and b are the very same record."""
    return (sort_key(a) > sort_key(b)) - (sort_key(a) < sort_key(b))
