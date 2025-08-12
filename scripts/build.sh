speakeasy run --skip-versioning && \
uv run scripts/auto-fix.py && \
uv python pin 3.13 && \
uv pip install git+ssh://git@github.com/friendliai/sdk-transpiler.git && \
uv run python -m sdk_transpiler --config pyproject.toml --log-level DEBUG && \
uv pip uninstall friendli && \
uv build && \
VERSION=$(uv run python -c "
with open('src/friendli/core/_version.py', 'r') as file:
    for line in file:
        if '__version__' in line:
            print(line.split('=')[1].strip().strip('\"\''))
            break
") && \
uv pip install ./dist/friendli-${VERSION}-py3-none-any.whl
