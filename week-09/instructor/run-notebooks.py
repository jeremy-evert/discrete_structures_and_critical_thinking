"""Execute the Week 09 Python notebooks and save their cell outputs.

This lightweight runner supports the Python code cells and SVG display used by
these instructor notebooks. Use a Jupyter kernel in VS Code for normal
interactive notebook work.
"""

from __future__ import annotations

import ast
import contextlib
import io
import json
import sys
import time
import traceback
import types
from pathlib import Path


INSTRUCTOR_DIR = Path(__file__).resolve().parent
NOTEBOOKS = sorted(INSTRUCTOR_DIR.glob("*.ipynb"))
ACTIVE_OUTPUTS: list[dict] | None = None


class SVG:
    """Small stand-in for IPython.display.SVG."""

    def __init__(self, data: str):
        self.data = data

    def _repr_svg_(self) -> str:
        return self.data


def display(value: object) -> None:
    """Capture the SVG and plain-text displays used by these notebooks."""
    if ACTIVE_OUTPUTS is None:
        return

    svg_repr = getattr(value, "_repr_svg_", None)
    if callable(svg_repr):
        ACTIVE_OUTPUTS.append(
            {
                "output_type": "display_data",
                "data": {
                    "image/svg+xml": svg_repr(),
                    "text/plain": "<SVG graphic>",
                },
                "metadata": {},
            }
        )
        return

    ACTIVE_OUTPUTS.append(
        {
            "output_type": "display_data",
            "data": {"text/plain": repr(value)},
            "metadata": {},
        }
    )


display_module = types.ModuleType("IPython.display")
display_module.SVG = SVG
display_module.display = display
ipython_module = types.ModuleType("IPython")
ipython_module.display = display_module
sys.modules["IPython"] = ipython_module
sys.modules["IPython.display"] = display_module


def execute_cell(source: str, namespace: dict) -> object | None:
    """Execute a cell and return its final expression, if it has one."""
    tree = ast.parse(source)
    if tree.body and isinstance(tree.body[-1], ast.Expr):
        final_expression = tree.body[-1]
        preceding = ast.Module(body=tree.body[:-1], type_ignores=[])
        exec(compile(ast.fix_missing_locations(preceding), "<notebook-cell>", "exec"), namespace)
        expression = ast.Expression(body=final_expression.value)
        return eval(compile(ast.fix_missing_locations(expression), "<notebook-cell>", "eval"), namespace)

    exec(compile(tree, "<notebook-cell>", "exec"), namespace)
    return None


def save_notebook(path: Path, notebook: dict) -> None:
    path.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


def run_notebook(path: Path) -> bool:
    global ACTIVE_OUTPUTS

    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__"}
    execution_count = 0
    started = time.perf_counter()
    succeeded = True

    for cell_number, cell in enumerate(notebook["cells"], start=1):
        if cell.get("cell_type") != "code":
            continue

        execution_count += 1
        cell["execution_count"] = execution_count
        cell["outputs"] = []
        ACTIVE_OUTPUTS = cell["outputs"]
        output_buffer = io.StringIO()

        try:
            with contextlib.redirect_stdout(output_buffer):
                result = execute_cell("".join(cell.get("source", [])), namespace)
            captured = output_buffer.getvalue()
            if captured:
                cell["outputs"].append(
                    {"output_type": "stream", "name": "stdout", "text": captured}
                )
            if result is not None:
                cell["outputs"].append(
                    {
                        "output_type": "execute_result",
                        "execution_count": execution_count,
                        "data": {"text/plain": repr(result)},
                        "metadata": {},
                    }
                )
        except BaseException as error:
            succeeded = False
            captured = output_buffer.getvalue()
            if captured:
                cell["outputs"].append(
                    {"output_type": "stream", "name": "stdout", "text": captured}
                )
            cell["outputs"].append(
                {
                    "output_type": "error",
                    "ename": type(error).__name__,
                    "evalue": str(error),
                    "traceback": traceback.format_exception(
                        type(error), error, error.__traceback__
                    ),
                }
            )
            save_notebook(path, notebook)
            print(f"FAILED {path.name}, code cell {cell_number}: {type(error).__name__}: {error}")
            break
        finally:
            ACTIVE_OUTPUTS = None

        save_notebook(path, notebook)

    duration = time.perf_counter() - started
    result_word = "completed" if succeeded else "failed"
    print(f"{result_word}: {path.name} ({duration:.1f} seconds)")
    return succeeded


def main() -> int:
    if not NOTEBOOKS:
        print(f"No notebooks found in {INSTRUCTOR_DIR}")
        return 1

    overall_started = time.perf_counter()
    failures = []
    for notebook_path in NOTEBOOKS:
        if not run_notebook(notebook_path):
            failures.append(notebook_path.name)

    overall_duration = time.perf_counter() - overall_started
    print(f"Run finished in {overall_duration:.1f} seconds.")
    if failures:
        print("Notebook failures: " + ", ".join(failures))
        return 1
    print(f"All {len(NOTEBOOKS)} notebooks completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
