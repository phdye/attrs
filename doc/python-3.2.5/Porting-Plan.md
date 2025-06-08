# Porting Plan for Python 3.2.5

This document outlines a phased approach for porting `attrs` to run under Python 3.2.5. Each phase is designed to be achievable within a single Codex session and builds upon the progress of the previous phases.

## Phase 1: Initial Setup and Environment Preparation
- Set up a Python 3.2.5 interpreter in the environment (for example using `pyenv`).
- Run the test suite under Python 3.2.5 to capture baseline failures.
- Identify immediate syntax errors or imports that fail due to missing standard library features.
- Document all initial failures in `doc/python-3.2.5/Baseline-Report.md` for reference.

## Phase 2: Update Packaging and Tooling
- Modify `pyproject.toml` and any CI configuration to allow Python 3.2.5 as a supported version.
- Update dependencies or pin older versions that still support Python 3.2.
- Ensure the project can be installed in a Python 3.2.5 environment using `pip`.

## Phase 3: Basic Compatibility Fixes
- Replace syntax introduced after Python 3.2 (e.g., f-strings) with older equivalents.
- Provide polyfills or conditional imports for standard library modules introduced after 3.2.
- Run the test suite again and document remaining issues.

## Phase 4: Feature Backports
- Identify features from newer Python versions that `attrs` relies on (e.g., `typing` features, `functools` improvements).
- Implement backports or wrappers to provide these features on Python 3.2.5.
- Keep these backports isolated in a dedicated module (e.g., `src/attr/_compat32.py`).

## Phase 5: Adjust Test Suite
- Update tests to accommodate differences in behavior on Python 3.2.5.
- Skip tests that rely on language features unavailable on 3.2.5 or provide alternative assertions.
- Ensure the test suite passes on Python 3.2.5, at least for core functionality.

## Phase 6: Documentation and Cleanup
- Document any limitations or behavioral differences in the official documentation.
- Remove or refactor deprecated code that cannot be supported on Python 3.2.5.
- Finalize the port by updating `README.md` and `docs/` with Python 3.2.5 support notes.

Each phase should conclude with a git commit summarizing the progress, ensuring an incremental and trackable migration path.
