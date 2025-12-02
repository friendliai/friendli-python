speakeasy run --skip-versioning && \
uv venv --python 3.13 && \
uv sync --group dev && \
uv run scripts/auto-fix.py && \
uv pip install git+https://github.com/friendliai/sdk-transpiler.git && \
uv run python -m sdk_transpiler --config pyproject.toml --log-level DEBUG && \
uvx ruff check --fix-only src/ && \
uvx ruff format src/ && \
git restore src/friendli/core/utils/annotations.py && \
rm -rf src/friendli_core && \
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
