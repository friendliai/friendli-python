# Copyright (c) 2025-present, FriendliAI Inc. All rights reserved.

"""Nox sessions."""

from __future__ import annotations

import nox

nox.options.default_venv_backend = "uv"


@nox.session(name="lint:fix")
def lint_fix(session: nox.Session) -> None:
    """Run lint fix."""
    _install_dependencies(session, "lint")
    _run_python_linter(session, fix=True)


@nox.session(name="lint")
def lint(session: nox.Session) -> None:
    """Run lint."""
    _install_dependencies(session, "lint")
    _run_python_linter(session, fix=False)


@nox.session
def test(session: nox.Session) -> None:
    """Run the unit and regular tests."""
    _install_dependencies(session, "test")

    env = {
        "COV_CORE_SOURCE": "src",
        "COV_CORE_CONFIG": ".coveragerc",
        "COV_CORE_DATAFILE": ".coverage",
    }

    session.run(
        "pytest",
        "test/",
        "--cov=src",
        "--cov-branch",
        "--cov-report=xml",
        *session.posargs,
        env=env,
    )
    session.run("coverage", "report", "--show-missing", "-m")


def _run_python_linter(session: nox.Session, *, fix: bool = False) -> None:
    """Run python linters."""
    # License checker and black formatter
    _uv_pip_install(
        session,
        r"https://github.com/friendliai/periflow-backends.git#subdirectory=web/tools/license",
    )

    args = [] if fix else ["--check"]
    paths = ["src", "test"]
    session.run("license", *args, *paths, external=False)
    session.run("black", "--config", "pyproject.toml", *args, *paths, external=False)

    # Ruff
    args = ["--fix"] if fix else []
    session.run("ruff", "check", *args, *paths, external=False)

    # MYPY
    if fix:
        return

    env = {"MYPYPATH": "src"}
    args = ["--config-file=pyproject.toml", "--show-traceback", "--fast-module-lookup"]
    session.run("mypy", *args, *paths, external=False, env=env)


def _install_dependencies(session: nox.Session, group: str | None = None) -> None:
    session.run_install(
        "uv",
        "sync",
        *([f"--group={group}"] if group else []),
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )


def _uv_pip_install(session: nox.Session, *args: str) -> None:
    session.run_install(
        "uv",
        "pip",
        "install",
        *args,
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
