def group_by_chain(items, rel):
    """Union-find: if a ~ b and b ~ c, then a, b and c share a group (connected components).

    Result is an equivalence relation by construction, in first-seen order.
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

    groups = {}
    for i, item in enumerate(items):
        groups.setdefault(find(i), []).append(item)
    return list(groups.values())
