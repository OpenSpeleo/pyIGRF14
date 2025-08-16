.PHONY: clean test coverage build install lint

# ============================================================================ #
# CLEAN COMMANDS
# ============================================================================ #

clean: clean-build clean-pyc ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -rf dist/
	rm -rf build/

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

# ============================================================================ #
# INSTALL COMMANDS
# ============================================================================ #

build: clean
	pip install flit
	flit build
