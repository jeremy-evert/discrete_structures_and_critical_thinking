class CycleError(Exception):
    """Two or more functions need each other, so there is no first one to test."""


def leaves_first(graph):
    """An order in which every function comes after everything it depends on.

    Raises CycleError, naming the loop, if functions depend on each other.
    """
    order = []
    done = set()

    def visit(name, path):
        if name in done:
            return
        if name in path:
            loop = path[path.index(name):] + [name]
            raise CycleError("dependency cycle: " + " -> ".join(loop))
        for needed in sorted(graph[name]):
            visit(needed, path + [name])
        done.add(name)
        order.append(name)

    for name in sorted(graph):
        visit(name, [])
    return order
