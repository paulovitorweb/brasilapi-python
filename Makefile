# Variables
PYTHON = python
POETRY = poetry

# Targets
.PHONY: install test lint check

install:
	$(POETRY) install

test:
	$(POETRY) run pytest
	$(POETRY) run coverage-badge -f -o coverage.svg

lint:
	$(POETRY) run ruff check .

check: lint test
