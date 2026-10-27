def cluster_by_chain(items, rel):
    """Put items in the same cluster if they are linked by a chain of matches.

    If a ~ b and b ~ c, then a, b and c share a cluster even when a !~ c.
    The clusters never overlap, so the result is an equivalence by construction.
    """
    parent = list(range(len(items)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if rel(items[i], items[j]):
                parent[find(j)] = find(i)

    clusters = {}
    for i, item in enumerate(items):
        clusters.setdefault(find(i), []).append(item)
    return list(clusters.values())
