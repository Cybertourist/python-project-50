install:
	uv sync

lint:
	uv run flake8 hexlet_code tests

test:
	uv run pytest
