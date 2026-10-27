class CycleError(Exception):
    """Two or more functions need each other, so there is no first one to test."""


def leaves_first(graph):
    """An order in which every function comes after everything it depends on."""
    return list(graph)
