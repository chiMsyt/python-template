# python-template

The starting point for new Python projects in this portfolio: packaging, quality gates,
CI/CD and benchmarks that already run, so a new project begins green instead of
accumulating that setup later.

The package inside (`python_template`, a small `slugify` function and CLI) exists only so
every gate has real code to check. Replace it with the project's own code.

## Develop

```console
uv sync
uv run pytest
```
