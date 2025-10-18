.PHONY: clean test coverage build install lint

# ============================================================================ #
# CLEAN COMMANDS
# ============================================================================ #

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -rf dist/
	rm -rf build/

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage*
	rm -fr htmlcov/
	rm -fr .pytest_cache

# ============================================================================ #
# LINT COMMANDS
# ============================================================================ #

lint:
# Lint all files in the current directory (and any subdirectories).
	ruff check --fix

format:
# Format all files in the current directory (and any subdirectories).
	ruff format

# ============================================================================ #
# BUILD COMMANDS
# ============================================================================ #

build: clean
	flit build --format wheel

# ============================================================================ #
# INSTALL COMMANDS
# ============================================================================ #

install: clean
	uv sync --all-extras --dev
