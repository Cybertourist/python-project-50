install:
	uv sync

lint:
	uv run flake8 gendiff tests

test:
	uv run pytest
