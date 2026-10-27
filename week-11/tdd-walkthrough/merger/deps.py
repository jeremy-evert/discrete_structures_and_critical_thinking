import ast
import inspect


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
    """An order in which every function comes after everything it depends on."""
    order = []
    seen = set()

    def visit(name):
        if name in seen:
            return
        seen.add(name)
        for dep in sorted(graph[name]):
            visit(dep)
        order.append(name)

    for name in sorted(graph):
        visit(name)
    return order
