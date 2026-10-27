THRESHOLD = 0.5


def _split(full_name):
    parts = full_name.lower().split()
    return parts[0], parts[-1]


def edit_distance(a, b):
    """Fewest single-letter inserts, deletes, or swaps to turn a into b."""
    previous = list(range(len(b) + 1))
    for i, ch_a in enumerate(a, 1):
        current = [i]
        for j, ch_b in enumerate(b, 1):
            current.append(min(previous[j] + 1, current[j - 1] + 1, previous[j - 1] + (ch_a != ch_b)))
        previous = current
    return previous[-1]


def similar_names(a, b):
    """Same family name, and given names whose edit distance is small compared to their length."""
    first_a, last_a = _split(a)
    first_b, last_b = _split(b)
    if last_a != last_b:
        return False
    closeness = 1 - edit_distance(first_a, first_b) / max(len(first_a), len(first_b))
    return closeness >= THRESHOLD
