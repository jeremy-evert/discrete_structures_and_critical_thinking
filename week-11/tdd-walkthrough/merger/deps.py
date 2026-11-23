import ast
import inspect


class CycleError(Exception):
    """Two or more functions need each other, so there is no first one to test."""


def build_graph(*modules):
    """Map each top-level function to the set of our other top-level functions it calls."""
    trees = [ast.parse(inspect.getsource(m)) for m in modules]
    functions = {
        node.name: node
        for tree in trees
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }
    graph = {}
    for name, node in functions.items():
        called = {
            n.func.id
            for n in ast.walk(node)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
        }
        graph[name] = (called & set(functions)) - {name}
    return graph


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
        for dep in sorted(graph[name]):
            visit(dep, path + [name])
        done.add(name)
        order.append(name)

    for name in sorted(graph):
        visit(name, [])
    return order
