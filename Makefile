# Shell to use with Make
SHELL := /bin/sh

# Export targets not associated with files
.PHONY: test coverage bootstrap pip virtualenv clean virtual_env_set

# Clean build files
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	find . -name "__pycache__" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf $(PROJECT).egg-info
