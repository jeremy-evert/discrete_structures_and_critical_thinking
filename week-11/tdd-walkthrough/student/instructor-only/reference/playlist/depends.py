class CycleError(Exception):
    """Two or more functions need each other, so there is no first one to test."""


def leaves_first(graph):
    """An order in which every function comes after everything it depends on."""
    order = []
    seen = set()

    def visit(name):
        if name in seen:
            return
        seen.add(name)
        for needed in sorted(graph[name]):
            visit(needed)
        order.append(name)

    for name in sorted(graph):
        visit(name)
    return order
